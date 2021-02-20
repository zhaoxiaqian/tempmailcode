# Code in Python
import requests
import json
import re
import time

def get_verification_code(email):
    validation_code = None
    for i in range(50):   #进行50次刷新 
        req = requests.get('https://snapmail.cc/emaillist/' + email)
        if req.status_code == 200:
            #方法一  直接分割法      通过请求回来的内容进行 分析   找到验证码前后的字符 进行分割   例如  <p>您请求的邮箱验证代码为: <b>910310</b>
            #邮件内容前有<b>后面有</b>
            code = req.text.split('</b>') 
            #分割后得到 <p>您请求的邮箱验证代码为: <b>910310
            print(code[0].split('<b>')[1]) 
            #分割后得到验证码
            #方法二   通过json解析邮件内容后再寻找
            email_text = json.loads(req.text)[0]['html']    #通过json查看邮件内容放在json中的那个字段内
            #  print(email_text)
            validation_code = re.search('([0-9]{6})', email_text)   #直接找数字0-9并且出现了6次的
            print(validation_code)
            break
        print("等待5s后刷新")
        time.sleep(5)
        #等待5秒
    if validation_code:
        print('validation_code:' + validation_code.group(1))
        return validation_code.group(1)





def random_emil():
    #通过当前时间戳做为邮箱前缀 共10位
    print(int(time.time()))
    emaiaddr= str(int(time.time()))+"@snapmail.cc"
    print(emaiaddr)
    return emaiaddr

get_verification_code(random_emil())
#random_emil()
