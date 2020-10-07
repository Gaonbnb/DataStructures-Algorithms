
#循环不变量
def find(S, val):
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j
        j += 1
    return -1
#递归
# 阶乘的递归
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
print(factorial(5))
#类空间的应用
class a:
    A = 5
    def aa(self):
        
        a.A += 1
        def aaaa(self):
            a.A += 1
        aaaa(self)
#aaa = a()
#aaa.aa()
#print(a.A)
# global代表全局变量，nonlocal代表上一级函数的变量
# global可以用在任何位置，nonlocal只能用于嵌套函数中，并且外层函数定义了相应的变量

# 画线加标记
def draw_line(tick_length, tick_label=""):
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)

def draw_ruler(num_inches, major_length):
    # 画开始的0
    draw_line(major_length, "0")
    for j in range(1, 1+num_inches):
        # 画分割
        draw_interval(major_length - 1)
        # 画主刻度
        draw_line(major_length,str(j))

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)
draw_ruler(3, 3)
# 自己的改写
def draw_line(major_length, tick_label=""):
    line = "-" * major_length 
    if tick_label:
        line += " " + tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)
    
class Ruler:
    def __init__(self, ruler_length, major_length):
        self.ruler_length = ruler_length
        self.major_length = major_length
    def draw_ruler(self):
        draw_line(self.major_length, "0")
        for i in range(1, self.ruler_length+1):
            draw_interval(self.major_length-1)
            draw_line(self.major_length, str(i))

#ruler = Ruler(5, 5)
#ruler.draw_ruler()
# 二分查找,自写
# 自爆了
#def binary_search(data, target, low, high):
#    if
#    binary_search(data[:((low + high) // 2)], target, 0, )
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif:
            target < data[mid]
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
# 有个好处是所有数字都查了一遍了
# 只要是可以迭代的list都可以自动生成
#mylist = list(range(100))
#mylist = list(iter((1,2,3,4,5)))
mylist = list(iter(range(100)))
#print(mylist)
binary_search(mylist, 66, 0, len(mylist)-1)
