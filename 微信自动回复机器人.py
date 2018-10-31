#!/usr/bin/python
#encoding:utf-8
import requests
import itchat
import itchat as it
import random
KEY='3a991c455b944c8ca5c4c776a1a54ff2'
it.login()
def get_response(msg):
    apiUrl='http://www.tuling123.com/openapi/api'
    data={
        'key':KEY,
        'info':msg,
        'userid':'wechat-robot',
    }
    try:
        r=requests.post(apiUrl,data=data).json()
        return r.get('text')
    except:
        return
@itchat.msg_register(itchat.content.TEXT)
#注册消息响应事件，消息类型为itchat.content.TEXT，即文本类型
def tuling_replay(msg):
    defaultReplay='I received:'+msg['Text']#返回同样的文本消息
    robots=['--By机器人仝胖胖']
    replay=get_response(msg['Text'])+random.choice(robots)
    return  replay or defaultReplay
@itchat.msg_register(itchat.content.PICTURE,itchat.content.RECORDING,itchat.content.SHARING,itchat.content.VIDEO)
def tuling_replay(msg):
    itchat.send(('那我就祝你越吃越胖，越长越难看'),msg['FromUserName'])
itchat.auto_login(enableCmdQR=True)#绑定消息响应事件后，让itchart运行起来，监听消息
#hotReload=True 保持登录 ；enableCmdQR=True 每次扫码登录
itchat.run()
