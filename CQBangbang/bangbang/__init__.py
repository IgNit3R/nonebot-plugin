# -*- coding: UTF-8 -*-
from nonebot import *
from aiocqhttp.exceptions import Error as CQHttpError
from . import main

bot = get_bot()

@scheduler.scheduled_job('interval', minutes =1)
async def new():
    await main.getNew(bot)

@bot.on_message("group")
async def bestdori(context):
    qun = context["group_id"]
    shield = await main.qunShield(int(qun))
    if shield == 1:
        msg = str(context["message"])
        try:
            if msg.find('.search') != -1:
                msg = int(msg[msg.find('.search'):][7:])
                if msg > 900 and msg < 10000:
                    await main.serchMap(bot,qun,msg)
        except:
            pass
        try:
            if msg.find('.map') != -1:
                msg = int(msg[msg.find('.map'):][4:])
                if msg > 900 and msg < 10000:
                    await main.getMap(bot,qun,msg)
        except:
            pass