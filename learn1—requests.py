import requests

r=requests.get("https://www.baidu.com")

print(r.status_code)
r.header
r.text
r.encoding
r.apparent_encoding
r.content

#爬取代码通用代码框架

import requests

def getHTMLText(url):
    try:
        r.requests.get(url,tiomeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__=="__main__":
    url="http://www.biadu.com"
    print(getHTMLText(url))
    
#ConnectionError,网络连接异常
#HTTPErro,HTTP错误异常
#URLRequired,url缺失异常
#TooManyRedirects,超过最大重定向次数异常
#ConnectTimeout,链接超时异常
#Timeout,请求url时，超时异常

#r.raise_for_status()

#requests库方法
#request()
#get()请求url位置资源
#head()请求后响应头信息
#post()请求向url位置的资源后附加新的数据
#put()请求向url位置存储一个资源，覆盖原url位置资源
#patch()请求局部更新URL位置的资源，即改变该处资源的部分内容
#delete()请求删除URL位置存储的资源
        
