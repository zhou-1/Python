# 基本数据类型  
# Number 数字  
int, float, bool, complex 复数

# String 字符串  
+：连接多个字符串     
%s: 字符串  (在字符串后面再加上% (‘XX’))   
格式化字符串： %格式化；format进行格式化   
python3: unicode 字符串     
python2: str 字符串 + unicode 字符串     

# List 列表   
[]  
一个容器来存放很多的数据  
a[1, 2, 3, 4, 5, 6, 'a', 'b']   
a.append() #新增一个元素   
del a[] #删除一个元素    
列表推导式：     
b = 'hello world'  
c = [i for i in b]   


# Tuple 元祖  
()    
*最后一个元素后面加一个',' 用在单个元素     

# Difference between List and Tuple
Tuples are immutable, lists are mutable. 元组是不可变的， 而列表是可变的。       l 
元组通常由不同的数据，而列表是相同类型的数据队列。
元组表示的是结构，而列表表示的是顺序。举个例子来讲：当你想记录棋盘上一个子的坐标时， 应该使用元组;    
当你想记录棋盘上所有子的坐标（一系列相同的数据），使用列表。  
你不能将列表当作字典的key， 而元组可以。   
由于元组支持的操作比列表小， 所以元组会比列表稍稍快上那么一丢丢。但是除非你有巨量的数据要处理，否则无所谓。   

# Sets 集合   
{1,2}    
大括号中必须要有value   


# Dictionary 字典     
{}   
一个容器以键值对key value的方式来存放很多的数据    
i.e. a = {'ac:1, 'b':2}   
字典中的键必须是不可变对象   


