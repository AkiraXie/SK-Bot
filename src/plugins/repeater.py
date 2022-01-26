from collections import defaultdict

from nonebot import on_message
from nonebot.adapters.onebot.v11 import GroupMessageEvent


def default_recording():
    return {
        'message': "",
        'repeated': False,
        'sender': 0
    }


recording = defaultdict(default_recording)

repeater = on_message(priority=20)


@repeater.handle()
async def repeat(event: GroupMessageEvent):
    rec = recording[event.group_id]
    if event.raw_message == rec["message"]:
        if not rec['repeated'] and rec['sender'] != event.user_id:
            rec['repeated'] = True
            await repeater.send(event.get_message())
    else:
        rec['message'] = event.raw_message
        rec['sender'] = event.user_id
        rec['repeated'] = False
