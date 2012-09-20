#\t表示tab键
tabby_cat="\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\ a \\ cat."
#单引号与双引号效果相同
fat_cat ='''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)
#成对的""(单引号)""(双引号)在python中都表示 引号中的内容为 字符串
print ("I'm 6'2\" tall.")#将2后面的双引号还原为真实双引号，避免配对错误
print ('I am 6\'2" tall.')#将6后面的单引号还原为真实单引号
