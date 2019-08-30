#提交关键词搜索
import requests as rqs

def getIPaddress(url,word):
    try:
        kv = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        ret=rqs.get(url,headers=kv,params=word)
        ret.raise_for_status()
        ret.encoding=ret.apparent_encoding
        print('{}\n{}\t{}'.format(url,ret.request.url,len(ret.text)))
#        print(ret.text[:1000])
    except:
        print('{} 访问异常'.format(url))



if __name__=="__main__":
   IP='59.172.73.152'
   kv={'ip':IP}
   url='http://www.ip138.com/ips138.asp'
   getIPaddress(url,kv)

