from sys import argv

script, input_file =argv

def print_all(f):
    print (f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print (line_count, f.readline())#bug(f.readline())点错写成了逗号

current_file = open(input_file)

print ("First let's print the whole file :\n")

print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

rewind(current_file)

print ("Let's print three lines:")

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1#current_line+=1
print_a_line(current_line,current_file)

current_file.close()
#用with方法可以保证安全关闭文件
line_number = 0
with open('test.txt', encoding='utf-8') as a_file:  
    for a_line in a_file: 
        line_number += 1        
        print('{:>4} {}'.format(line_number, a_line.rstrip()))
