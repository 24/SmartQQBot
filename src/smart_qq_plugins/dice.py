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

# =====骰子功能=====

dice_flag = re.compile("^\.r\s(\d*)d(\d*)(\s.*)?")
def is_dice(key):
    result = re.findall(dice_flag, key)
    if result:
        return result[0]
    return None

@on_all_message(name='dice')
def dice(msg, bot):
    result = is_dice(msg.content)
    if result:
        num, numrange, reason = result[0],int(result[1]),result[2]
        if num:
            num = int(num)
        else:
            num = 1
        reply = bot.reply_msg(msg, return_function=True)
        logger.info("RUNTIMELOG " + str(msg.from_uin) + " dice, trying to reply....")
        result = [random.randint(1,numrange) for x in range(num)]
        reply_content = "因为："+reason+",投出了："
        for num in result:
            reply_content += str(num)+"+"
        reply_content = reply_content[:-1]+'='+str(sum(result))
        reply(reply_content)
