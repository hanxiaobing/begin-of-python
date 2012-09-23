print ("Let's practice everything.")
#print函数，注意 Python3 与 Python2 的区别
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
#print函数中双引号，单引号均可使用，注意匹配即可。转义符\的使用

#三双引号""",表示多行格式化文本。再次注意转义字符的使用。
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print ("-------------------------")
print (poem)
print ("-------------------------")


five = 10 -2 +3 -6
print ("This should be five:%s" %five)

#自定义函数，参数与返回值
def secret_formula(started):
    jelly_beans = started *500
    jars = jelly_beans /1000
    crates = jars/100
    return jelly_beans,jars,crates

#自定义函数的使用
start_point =10000
beans,jars,crates = secret_formula(start_point)

print ("With a starting point of: %d" % start_point)
print ("We'd have %d beans,%d jars, and %d crates." % (beans,jars,crates))

start_point = start_point / 10

print ("We can also do that this way:")
print ("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))
# print 函数中包含自定义函数
