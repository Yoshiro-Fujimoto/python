#print("Hello World")
#型変換
num=1
tmp="1"
print(int(tmp) )
print(type(int(tmp)) )
print(str(num) + "番目")

#f-strings
print(f"num:{num}")

#リスト(配列)
num_list=[1,2,3]
print(num_list)
print(num_list[-1]) # [-1]一番後ろの要素にアクセス

men_list = [["John", "Fred","AAA"], ["Tanaka", "Sato"]]
print(men_list[1][0])
print(len(men_list))

a=1
b=2  
c=a+b**2
print(c)

d=5%2  #・・・余り
print(d)
i=4
print(i%2 == 0)  #・・・倍数判定

#関係演算子
print(a==b)
print(a!=b)
print("a"=="a")
print("Fred" in men_list[0])

#論理演算子
x = 10
y = 2
print(x > 2 and y > 1)
print(x > 2 and y > 3)

#複合代入演算子
x = 10
y = x+10
print(y)
x += 10
print(x)

# Q.if文を使って
#   num が 10以上(10を含む) の時は [9より大きい]
#   num が 10未満(10を含まない) の時は [10より小さい] と出力せよ
num=8
if num>=10:
    print("9より大きい")
else:
    print("10より小さい")

# Q2. 任意の0以上の自然数 variable_num が
# 3の倍数なら[Fizz]
# 5の倍数なら[Buzz]
# 15の倍数なら[FizzBuzz]
# いずれでもないなら [variable_num] を出力せよ
# 0の場合は0を出力せよ
variable_num=6
if variable_num==0:
    print(0)
elif variable_num%15 == 0:
    print("FizzBuzz")
elif variable_num%5 == 0:
    print("Buzz")
elif variable_num%3 == 0:
    print("Fizz")
else:
    print(variable_num)


#for
for i in range(0, 10, 2):
    print(i)

num_list = [1, 2, 3]
for i in range(0,len(num_list)):   #・・・len リストの数
    print(num_list[i])

for i in range(1,5):
    if i>=3:
        i=i+1
    
    print(i)

#continue,break
for i in range(1,9):
    if  i==3 or i==5 or i== 7:
        continue
    print(i)

for i in range(1,9):
    if  i==4 :
        break
    print(i)

i=0
while i>=0:    #・・・条件式がTrueの時に実行
    i+=1
    if i==3:
        print("break")
        break
    else:
        print(i)

i=0
while True:   
    i+=1
    if i==3:
        print("break")
        break
    else:
        print(i)

i=0
abc=True
while abc:   
    i+=1
    if i==3:
        print("break")
        abc=False
    else:
        print(i)

#関数
def myfunction(a):
    b=a+1
    return b
print(myfunction(2))

#クラス
class SimpleData:
    # クラス
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum2(self):
        return self.a + self.b


class myclass(SimpleData):
    def __init__(self, a,b,c):
        super().__init__(a,b)
        self.c =c

    def sum3(self):
        return self.a + self.b + self.c

aaa = myclass(2,3,4)
print(aaa.sum3())
bbb= myclass(2,3,4)
print(bbb.sum2())

#オーバーライド
class SimpleData:
    # クラス
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum2(self):
        return self.a + self.b


class myclass(SimpleData):
    def __init__(self, a,b,c):
        super().__init__(a,b)
        self.c =c

    def sum2(self):
        return (self.a + self.b)/2

    def sum3(self):
        return self.a + self.b + self.c


class myclass2(SimpleData):
    def __init__(self, a,b,c):
        super().__init__(a,b)
        self.c =c

    def sum2(self):
        return (self.a + self.b)/2

    def sum3(self):
        return self.a + self.b + self.c

aaa = myclass(2,3,4)
print(aaa.sum2())
bbb = myclass2(2,3,4)
print(aaa.sum2())

