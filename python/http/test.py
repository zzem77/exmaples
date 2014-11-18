# coding: utf8
import urllib
import urllib2

# url = "http://webhacking.kr/challenge/web/web-02/"
url = "http://webhacking.kr/index.html?enter=1"

# urllib을 스는 이유 -urlencode()
login_form = {"id": "aaa", "pw": "aaaa"}
login_req = urllib.urlencode(login_form)

request = urllib2.Request(url, login_req)
response = urllib2.urlopen(request)

# print response.read()

cookie = response.headers.get('Set-Cookie')

print cookie
