# 钉钉信息发送
# -*- coding:utf-8 -*-
import requests

def ding_talk(content,at_type,at_mobile=""):
    url =""
    text = {
        "msgtype":"text",
        "text":{
            "content":content
        },
        "at":{
            "atMobiles":[],
            "isAtAll": "false"
        }
    }
    headers = {"Content-Type": "application/json"}

    if at_type == 1: # 表情包专用群
        url = "https://oapi.dingtalk.com/robot/send?access_token=fd32659c682107df79c0fe0afa6e75b28cb1d780a00ae827b138e8e3a3970a53"
    elif at_type == 2: #　测试组专用群
        url = "https://oapi.dingtalk.com/robot/send?access_token=19a4ad7c34aeff6d808ca15f86d58185488c08e53bbf7a9bd36043df6c3033c1"
    elif at_type == 0: # 给自己发信息
        url = "https://oapi.dingtalk.com/robot/send?access_token=3fe06d48c0671decb2fad4b33defda4cb2903ffdfbc3119bc9adf7377a8b537b"
    else: #其他的都到大群
        url = "https://oapi.dingtalk.com/robot/send?access_token=3fe06d48c0671decb2fad4b33defda4cb2903ffdfbc3119bc9adf7377a8b537b"

    t = requests.post(url, json=text,headers=headers)

    print(t.text)


if __name__ == "__main__":
    while 1:
        text = input("你要说的：")
        ding_talk(text,1)