# -*- coding: utf-8 -*-
import random
import re
from smart_qq_bot.logger import logger
from smart_qq_bot.signals import (
    on_all_message,
    on_group_message,
    on_discu_message,
    on_private_message,
)


# =====唤出插件=====

# 机器人连续回复相同消息时可能会出现
# 服务器响应成功,但实际并没有发送成功的现象
# 所以尝试通过随机后缀来尽量避免这一问题

REPLY_SUFFIX = (
    '~',
    '!',
    '?',
    '||',
)

call_flag = re.compile("村饭")
def is_call(key):
    result = re.findall(call_flag, key)
    if result:
        return result[0]
    return None

@on_all_message(name='callme')
def callme(msg, bot):
    if is_call(msg.content):
        reply = bot.reply_msg(msg, return_function=True)
        logger.info("RUNTIMELOG " + str(msg.from_uin) + " calling me out, trying to reply....")
        reply_content = "干嘛（‘·д·）" + random.choice(REPLY_SUFFIX)
        reply(reply_content)
