# -*- coding: UTF-8 -*-

import requests
import sys
def msm():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    r = requests.get(url='http://192.168.1.155/sms/InterFace.php?m=和我看APP接口测试完成!')
    print(r.text)




if __name__ == "__main__":
    msm()
