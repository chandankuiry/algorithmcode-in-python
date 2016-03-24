# it take O(k) time where k is the size of the list
from timeit import Timer
def test1():
    l = []
    for i in range(1000):
        l = l + [i]
# append is take O(1) time
def test2():
    l = []
    for i in range(1000):
        l.append(i)
#List comprehension

def test3():
    l = [i for i in range(1000)]
#list range least amount of time you can see in output
def test4():
    l = list(range(1000))
    


t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

#output
#concat  6.54352807999 milliseconds
#append  0.306292057037 milliseconds
#comprehension  0.147661924362 milliseconds
#list range  0.0655000209808 milliseconds
