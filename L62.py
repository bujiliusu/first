# from http.client import HTTPResponse
# from urllib import request
# from urllib import parse
# import ssl
# base_url = 'https://movie.douban.com/j/search_subjects?'
# ua = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
# #type=movie&tag=热门&page_limit=50&page_start=0
# params = parse.urlencode({
#     'type':'movie',
#     'tag':'热门',
#     'page_limit':50,
#     'page_start':0
# }
# )
# url = base_url + params
# context = ssl._create_unverified_context()
# rq:request.Request = request.Request(url, headers={'User-agent':ua})
# response:HTTPResponse = request.urlopen(rq,context=context)
# #print(response.read().decode(encoding="utf-8", errors="strict"))
# with response:
#     print(2,response.geturl())
#     print(2,response.info())
#     print(3,rq.get_header('User-agent'))
#     print(4, response.read())
# import urllib3
# from urllib3.response import HTTPResponse

# with urllib3.PoolManager()as pool:
#     response:HTTPResponse = pool.request("GET", url, headers={'User-agent':ua})
#     print(response)
#     print(response.data)

import requests
from requests.models import Request,Response
headers={
    'User-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}
url = 'https://www.baidu.com'
session = requests.session()
urls = [url, url]
with session:
    for url in urls:
        # with requests.request('GET', url, headers=headers) as response:
        with session.get(url, headers=headers)as response:
            print(1,response.request.headers)

