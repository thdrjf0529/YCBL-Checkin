# -*- coding: utf-8 -*-
import logging
import requests
import os
result = b'success\n'
# url
url = "http://www.yecaibuluo.com/portal/api/checkIn"
# cookie
cookie = os.environ["COOKIE"]

payload = "{\"token\":\"glados_network\"}"
headers = {
  'accept': 'application/json, text/plain, */*',
  'dnt': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
  'content-type': 'application/json;charset=UTF-8',
  'origin': 'http://www.yecaibuluo.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'http://www.yecaibuluo.com/',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': cookie
}
def do_action():
    logger = logging.getLogger()
    response = requests.request("POST", url, headers=headers, data = payload)
    result = response.text.encode('utf8')
    logger.info(result)
    print(result)
    return result


if __name__ == '__main__':
    do_action()
