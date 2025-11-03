# 以写入模式打开note.txt文件，文件句柄赋值给fp变量
from io import TextIOWrapper

fp: TextIOWrapper=open('note.txt',mode='w')

# 使用print函数将字符串'北京欢迎你！'输出到文件中
print('北京欢迎你!',file=fp)

# 关闭文件句柄，确保内容写入磁盘
fp.close()
#在Python文件操作中，fp 是 "file pointer"（文件指针）的缩写，也称为 "file handle"（文件句柄）。
# 它代表一个指向已打开文件的引用对象，通过这个对象可以对文件进行读写操作。