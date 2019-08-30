#提交关键词搜索
import requests as rqs

def getURLText(url,word):
    try:
        kv = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        ret=rqs.get(url,headers=kv,params=word)
        ret.raise_for_status()
        ret.encoding=ret.apparent_encoding
        print('{}\n{}\t{}'.format(url,ret.request.url,len(ret.text)))
    except:
        print('{} 访问异常'.format(url))

def Baidu_searchWord(kv):
    BaiduSearch_url='https://www.baidu.com/s'
    getURLText(BaiduSearch_url,kv)

def So360_searchWord(kv):
    So360Search_url='https://www.so.com/s'
    getURLText(So360Search_url,kv)

if __name__=="__main__":
    kv1={'wd':'baidu'}
    kv2={'q':'360'}
    Baidu_searchWord(kv1)
    So360_searchWord(kv2)


