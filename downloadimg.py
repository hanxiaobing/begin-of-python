# -*- coding: utf-8 -*-
import urllib.request
import sys
urltxt=open("D:\我的文档\Dropbox\SuperMemo\新建文本文档.txt")
url=urltxt.readlines()
localname='1.gif','2.gif','3.gif','4.gif','5.gif','6.gif','7.gif','8.gif','9.gif','10.gif','11.gif','12.gif','13.gif','14.gif','15.gif','16.gif','17.gif','18.gif','19.gif'
for i in range(0,len(url)-1):
#url=""
#for 
    urllib.request.urlretrieve(url[i],localname[i])
#   urllib.request.urlretrieve(url[i].split("#"))
    print ("The %d is downloading,total %d\n Please wait..." %(i+1,len(url)-1))
print ("All done")
