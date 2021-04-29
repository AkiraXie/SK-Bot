import nonebot
from nonebot.adapters.cqhttp import Bot
from nonebot.log import default_format, logger


nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter('cqhttp', Bot)
app = nonebot.get_asgi()


nonebot.load_plugin('haruka_bot')
nonebot.load_plugins('src/plugins')


logger.add("logs/error.log",
           rotation="00:00",
           retention='1 week',
           diagnose=False,
           level="ERROR",
           format=default_format,
           encoding='utf-8')


if __name__ == "__main__":
    nonebot.run(app="bot:app")
