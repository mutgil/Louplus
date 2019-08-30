#获得多个网站的robots协议内容
import requests as rqs

def getRobotsTxt(url):
    try:
        kv = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        ret=rqs.get(url,headers=kv)
        ret.raise_for_status()
        ret.encoding=ret.apparent_encoding
        print('{}\n{}'.format(url,ret.text))
    except:
        print('{} 访问异常'.format(url))


if __name__=="__main__":
    url_lists=['http://www.baidu.com/robots.txt','http://www.qq.com/robots.txt','http://news.sina.com.cn/robots.txt','http://news.qq.com/robots.txt','http://www.moe.edu.cn/robots.txt']
    for i in url_lists:
        getRobotsTxt(i)

