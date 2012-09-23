#from sys import argv

#script,filename=argv
import sys

script,filename=sys.argv
#以上为import的两种不同用法
print ("We're going to erase %r."% filename)
print ("If you don't want that, hit CTRL-C(^C).")
print ("If you do want that, hit RETURN.")

input ("?")
#如何识别键盘输入？
#CTRL-C Python解释器快捷键中断进程，所以可以用来结束程序 else 有效输入但是不赋值，此句仅用于程序暂停供人确认。
print ("Opening the file...")
target = open(filename,'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1=input("line 1:")
line2=input("line 2:")
line3=input("line 3:")

print ("I'm going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write ("%s\n%s\n%s" %(line1,line2,line3))#用法基本与print相同。%前不用逗号

print ("And finally, we close it.")
target.close()
#使用open 及read 函数处理上述文件
test_content=open(filename)
print (test_content.read())
