import subprocess
import time
import requests
'''
 curl 'http://labexamen.gzhu.edu.cn/exam_xuexi_online.php' -H 'Connection: keep-alive' -H 'DNT: 1' --data 'cmd=xuexi_online' --compressed --insecure
'''

def 实验室刷时间():

    url = "http://labexamen.gzhu.edu.cn/exam_xuexi_online.php"
    payload = {
        "Cookie": "wsess=lcs2mi3knvt4cf9fko0ea1lp46",
        "Origin": "http://labexamen.gzhu.edu.cn",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "Referer": "http://labexamen.gzhu.edu.cn/redir.php?catalog_id=6&cmd=dati&mode=test",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
    }
    data = "cmd=xuexi_online"

    r = requests.post(url,data=data,headers=payload)
    txt = r.text
    print(txt)

if __name__ == "__main__":
    while True:
        实验室刷时间()
        time.sleep(30)
