# this one is like your script with argv
def print_two(*args):
    arg1,arg2=args
    print ("arg1:%r,arg2:%r"%(arg1,arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print ("arg1:%r,arg2:%r"%(arg1,arg2))

# this just takes one argument
def print_one(arg1):
    print ("arg1: %r"%arg1)

# this one takes no arguments
def print_none():
    print ("I got nothing'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
#函数定义是以def开始
#函数名称以字符和下划线组成
#函数名称紧跟着括号
#括号中可以包含多个参数，参数之间以逗号，隔开
#参数名称不能重复
#函数名称括号后面不要忘了还有个冒号:
#函数定义的内容（代码）用缩进来表示
#函数结束位置取消缩进即可
