#coding=utf8
import requests
import itchat
from wxpy import *

#481a92ac7ca94a9da5598cf368a06ec2
#8edce3ce905a4c1dbb965e6b35c3834d
KEY = '481a92ac7ca94a9da5598cf368a06ec2'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
# @itchat.msg_register(itchat.content.TEXT)
@itchat.msg_register('Text', isGroupChat = True)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    # busy = '【自动回复】您好，该用户正在上课，稍后才能看到您的信息，如有急事请拨打该用户临时手机号码13690469569。'.decode('utf-8')
    return reply or defaultReply
    # return busy

itchat.auto_login(hotReload=True)
itchat.run()