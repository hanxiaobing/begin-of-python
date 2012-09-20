from sys import argv
from os.path import exists
#import sys , os
script,from_file,to_file = argv

print ("Copying from %s to %s" %(from_file,to_file))#少了最后半个括号，print函数没有结束，所以一直提示非法字符。调试了半天找不出原因。把后面代码全部注释掉才找到原因。

# we could do these two on one line too,how?
input = open(from_file)
indata = input.read()
#indata = open(from_file).read()

print ("The input file is %d byte long"%len(indata))

print ("Does the output file exist? %r" % exists(to_file))
print ("Ready ,hit RETURN to continue,CTRL-C to abort.")
#input ()#该语句一直无法通过调试，尚未找出原因

output = open(to_file,'w')
output.write(indata)

print ("Alright ,all done.")

output.close()
input.close()#粗心input写成了intput
