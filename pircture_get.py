import requests as rqs
import os

def getPircture(url,path):
    if not os.path.exists(root):
        os.mkdir(root)
    try:
        if not os.path.exists(path):

            kv = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
            }
            ret=rqs.get(url,headers=kv)
            ret.raise_for_status()
            with open(path,'wb') as f:
                f.write(ret.content)
                f.close()
                print("保存成功")
        else:
            print("文件已经存在")
    except:
        print('{} 访问异常'.format(url))


if __name__=="__main__":
    url="https://ss0.bdstatic.com/-0U0bnSm1A5BphGlnYG/tam-ogel/20d5c57e839fa986939e2e6aec94728b_222_222.jpg"
    root="D://picture"
    path=root+url.split('/')[-1]
    getPircture(url,path)

