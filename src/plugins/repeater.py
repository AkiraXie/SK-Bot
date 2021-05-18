from collections import defaultdict

from nonebot import on_message
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent
from nonebot.adapters.cqhttp.message import Message


def default_recording():
    return {
        'message': Message(),
        'repeated': False,
        'sender': 0
    }

recording = defaultdict(default_recording)

repeater = on_message(priority=20)

@repeater.handle()
async def repeat(bot: Bot, event: GroupMessageEvent):
    rec = recording[event.group_id]
    if raw_message(rec['message']) == raw_message(event.message):
        if not rec['repeated'] and rec['sender'] != event.sender.user_id:
            rec['repeated'] = True
            await bot.send(event, rec['message'])
    else:
        rec['message'] = event.message
        rec['sender'] = event.sender.user_id
        rec['repeated'] = False

def raw_message(message):
    raw = ''
    for segment in message:
        if segment.type == 'image':
            raw += segment.data['file']
        else:
            raw += str(segment)
    return raw

