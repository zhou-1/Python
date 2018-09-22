import requests
import os
root='D://picss//'
url='https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1489195978&di=97db7195ade7d2d77e3d31b9d54fbf9f&src=http://www.swelnus.com/uploads/allimg/150925/2089-150925093K4-51.jpg'
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
        #判断根目录是否存在，os.madir()创建根目录
    if not os.path.exists(path):
        
        r=requests.get(url)
        #判断文件是否存在，不存在将从get函数获取
        with open(path,'wb')as f:
             #wb存为二进制文件
            f.write(r.content)
            #将返回内容写入文件 r.content返回二进制形式
           
            f.close()
            print('文件保存成功')
    else:
        print('文件已经存在')
        
except:
    print('爬取失败')
    
# https://zhuanlan.zhihu.com/p/25768026   
