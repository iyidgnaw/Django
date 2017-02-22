## Python

#### Function

- the default parameter can be not according to the origin order only when you use the "key-value " pair the state your value.

  ~~~python
  def enroll(name,gender,age=6,city="beijing"):
      pass

  >>>enroll("wangdiyi","male")
  >>>enroll("wangdiyi","male",22)
  >>>enroll("wangdiyi","male",city = "boston")
  ~~~

  ​

- **Do not use changeable object as your default parameter!**

  ```python
  def add_end(L=[]):
  	L.append("a")
      
  >>>add_end()//after this, the L is ["a"]
  >>>add_end()//at the beginning of the function the L is ["a"] instead of empty.
  ```

- use changeable parameter, the changeable parameter is not changeable in the function, it will be a tuple.

  ```python
  def calc(*numbers):
      sum = 0;
      for n in numbers:
          sum +=n
      return sum
  //the length of numbers is changeable.

  //you can use your own list as parameter
  >>>lst = [1,2,3]

  >>>calc(*lst)//=calc(1,2,3)
  ```

- keyword parameter:

  ```python
  def person(name, age, **kw):
      pass

  >>>person("wangdiyi",22)//keyword parameter is not mandatory, the keyword parameter now is an empty dictionary {}.
  >>>person("wangdiyi",22,city="beijing")
  //if you write one or several "key-value" pair, it will be included in a dictionary.
  <<<<<<< HEAD
  //you can define your own dictionary, and use it
  dic1 = {city:"beijing"}
  person("wangdiyi",22,**dic1)
  //you can define your own dictionary, and use it
  >>>dic1 = {city:"beijing"}
  >>>person("wangdiyi",22,**dic1)
  ```
  #### String

  - Coding:  ACSII 1 byte per char, Unicode 2 byte per char. ACSII can only represent English while Unicode can represent almost all languages. But the problem is using Unicode to encode English will lead to some redundant occupation of memory. So that we got UTF-8. 

  - Handling computers or servers, the characters are encoded by Unicode. However, they are saving in UTF-8 in txt.

  - txt(UTF-8) ---> Memory(Unicode)---->editing--->Back to UTF-8 and saved in txt.

  - ```python
    >>>b'ABC'.decode('ascii')
    'ABC'
    >>>b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
    '中文'
    len('ABC') = 3 is the length of the string , 
    len(b'ABC') = 3 is the amount of bytes of the string.
    ```
#### Iterate

- check iterable:

  ```python
  from collections import Iterable
  >>>isinstance('abc',Iterable)
  True
  ```


- iterate:

  ```python
  for i, value in enumerate(['A','B','C']):
      print i,value

  0,A
  1,B
  2,C
  ```

  ​

#### List and Tuple

- List have:

  - insert(i,item), this is **O(N)** time complexity.
  - pop()
  - pop(i): pop and delete the element at index i, this is **O(N)** time complexity.
  - sort(): **O(n logn)**

- you can cut your List as follows:

  ```python
  lst = [1,2,3,4,5,6,7,8,9,0,20]
  lst[::5]//select every 5 elements
  lst[:10:2]//select every 2 elements among first 10 elements
  ```

- To generate a duplicate list:

  ```python
  >>>lst = [0] * 5
  [0,0,0,0,0]
  ```

- **Comprehensions!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**

  ```python
  >>>[x * x for x in range(1,11)]
  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

  >>>[x * x for x in range(1,11) if x%2 == 0]
  [4, 16, 36, 64, 100]

  >>>[m+n for m in 'ABC' for n in 'XYZ']
  ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

  >>>d = {'x':'A'}
  >>>[k+'='+v for k,v in d.items()]
  ['x=A']
  ```

- **Generator**

  ```python
  g = (x * x for x in range(1,11))

  >>>for n in g:
     		print (n)
  0
  1
  4
  ...
  /////////////////every time, the generator only generate one element according to the method.

  def fib(max):
      n,a,b = 0,0,1
      while n<max:
          print (b)
          a,b = b,a+b
          n +=1
      return 
  ///this is a function for fibonacci
  def fib(max):
      n,a,b = 0,0,1
      while n<max:
          yield b
          a,b = b,a+b
          n +=1
      return 
  ///this is a generator for fibonacci
  you can use it by for loop

  for n in fib(6):
      print n
      
  ///the generator stop at the yield line, and return back to the yield line at next calling.
  ```


#### To check the implementing time of a function, we use Timer:

```python
import timeit
def test1():
    l = []
    for i in range(1000):
        l.append(i)
        
print("time is ",timeit.timeit("test1()",setup="from __main__ import test1",number=10000),"milliseconds")


//we import the test1 function from main because we want to test the single function but not others.
```

#### Two pointer method for the ordered Linked List add():

这个方法对于其他的针对链表结构需要知道上一个元素的算法也同样适用。

比如我们需要删除第ｉ个元素，那么我们就可以使用两个指针，第二个指针达到指定元素时，previous指针恰好指向其上一个元素，由此就可以简单的删除下一个元素了。

```python
def add(self,item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
        if current.getData() > item:
            stop = True
        else:
            previous = current
            current = current.getNext()

    temp = Node(item)
    if previous == None:
        temp.setNext(self.head)
        self.head = temp
    else:
        temp.setNext(current)
        previous.setNext(temp)
```

#### Range and Slice

```python
range(5) = [0,1,2,3,4]
range(1,5) = [1,2,3,4]
lst = list(range(5))
lst[n:m] = [lst[n]....lst[m-1]]
lst[n:] = [lst[n]...(end)]
lst[n:-1] = [lst[n]...lst[(len(lst)-2)]]# lst[1,-1] = [1,2,3]



```

#### The "In" operation:

The `in` operator, like most other operators, is just a call to a `__contains__` method (or the equivalent for a C/Java/.NET/RPython builtin). `list` implements it by iterating the list and comparing each element; `dict` implements it by hashing the value and looking up the hash; `blist.blist` implements it by walking a B+Tree; etc. So, it could be O(n), O(1), O(log n), or something completely different.

http://stackoverflow.com/questions/17539367/python-dictionary-keys-in-complexity

#### Generator and Iterator

You have two way to make a generator, the following :

```python
lst = [str(i) for i in range(10)]
```

if you replace the bracket with a pair of parenthesis, it become a generator:

```python
lst = (str(i) for i in range(10))
```

You can also replace the output of your function to "yield" and make a function defintion to a generator definition.

```
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done' 
```

All generator are Iterator, for Iterator ,you can use next() to retrieve the next element or use a for-loop to go throught the whole iterator (also list())

**The important implementation of generator is the permutation of list:**

```
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
```

#### Map and Reduce

```python
map(str,  list(range(10)))
"""
	map will receive a high order function as the first parameter and a iterative object as the second one.
	Returning a iterator.
	Thus if you want the whole result of map, you need to use list()
	Remember that the function in map should receive one parameter and return one object as well.
"""
```

```python
"""
	reduce will also receive two parameter as map while it's for executing the iterative accumulate.
	Thus the high order function in reduce must receiving two parameter as well.
	Return is not a iterator but an single object.
"""
#def add(x,y):
#	return x+y
reduce(add, [1, 3, 5, 7, 9])
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```



#### Filter

```Python
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# result: [1, 5, 9, 15]
```

## Incredible simple solution for prime generator...

```python
def _odd_iter():
    """
        generator for odd numbers
    """
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    """
        high order function
        return a function that judge the remainder of n
    """
    return lambda x: x % n > 0


def primes():
    """
        Very exicted program!!!
        Every time next() will go to the next line of "yield n"
        which will add another layer of filter to the already existing filters
        when n = 7 
        it = filter(_not_divisible(7),filter(_not_divisible(5),filter(_not_divisible(3),_odd_iter())))
        this is unbelivable simple solution...
    """
    yield 2
    it = _odd_iter() 
    while True:
        n = next(it) 
        yield n
        it = filter(_not_divisible(n), it) 

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```



#### Sorted

```python
sorted([36, 5, -12, 9, -21], key=abs,reverse=True)
"""
	sorted() is also a high order function can receive a function as second parameter.
	the function in key will receive one element each time and return one object.
	Remember, the "key" is just the name of the function but not actually calling it from here.
	So don't write key=abs()
	The sorted() can also receive a reverse parameter which is default False
"""
```



#### Python Closure And Decorator

https://segmentfault.com/a/1190000004461404

Decorator is a function that decorate other function. Add some information of the existing function.

```python
def info(func):
    print("Call %s"%func.__name__)
    return func()

@info
def test():
    print("this is main function.")
    
>>>Call test
this is main function.
```

This is also one usage of closure.

If you don't know the parameter needed by the decorated function, you can:

```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

Closure is :

在函数内部声明nested函数，nested函数可以使用外部函数声明的变量，并且能够在外部函数的生存周期结束后仍然保有所用变量的引用关系，就如同把使用到的外部函数的变量“包”在了一个包裹里面一样，这个包裹本身就被称为“闭包”（closure）。需要注意的是，外部函数要把内部的nested函数作为返回值返回，才能完成闭包的过程。



```python
def outer():
    count =  1
    def inner():
        print(count)
        
    return inner
```

需要注意的是闭包仅能够保存引用的结构，但是并没有固定住引用的值

```python
def outer():
    fnlst = []
    for i in range(3):
        def inner():
            print(i)
        fnlst.append(inner)
    return fnlst

f1,f2,f3 = outer()
f1()
f2()
f3()

>>>>
2
2
2
```

如上的例子中，闭包返回了三个函数，print指向的目标都是i，但是i是一个不断变化的值，因此在第三次i的值改变后i才确定了下来，前两次的print的目标也都变成了这个改变后的i。

```ptyhon
def outer():
    fnlst = []
    for i in range(3):
        def inner(j=i):
            print(j)
        fnlst.append(inner)
    return fnlst

f1,f2,f3 = outer()
f1()
f2()
f3()

>>>>
0
1
2
```

使用一个参数保存住当前的i的值，每个j的生存周期仅是当前的函数内部，不会因为i的改变而发生变化，由此就能够达到我们本来希望达成的目的。

总结起来说就是：不要在闭包中使用外部函数可能改变的变量。



#### OOP

- 在python中可以在类的声明之外，添加属性

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

me = Student("Diyi",100)
me.age = 10

def test():
    print("Function for test")

me.test = test
me.test()
print(me.age)

>>>Function for test
10
```

- 可以在需要私有的域前面加两个下划线以此来避免外部直接访问和修改。

```python
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```

如果外部有访问的需求，就添加get函数

如果外部有修改私有域的需求，那就添加set函数，这样做的好处在于可以在set函数中进行类型判断，避免错误地修改私有域。



##### Polymorphism

多态的意义就在于子类可以改写并覆父类的方法，同时，多态的继承能够保证子类至少可以应用在父类可应用的位置上。

```python
def run_twice(animal):
    animal.run()
    animal.run()
    
class Animal:
	def run(self):
        print("Animal is running...")
        
class dog(Animal):
    def run(self):
        print("Dog is running...")
        
        
class cat(Animal):
    pass

a = Animal()
d = dog()
c = cat()
for i in [a,d,c]:	
	run_twice(i)
    
>>>>
Animal is running...
Animal is running...
Dog is running...
Dog is running...
Animal is running...
Animal is running...
```

任何依赖与父类元素的方法，都可以向下兼容子类的元素。所谓的开闭原则：

对扩展开放：允许新增`Animal`子类；

对修改封闭：不需要修改依赖`Animal`类型的`run_twice()`等函数。

##### 动态

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

只要对象包含有run（）这个方法，它就可以作为run_twice（）的合法输入。

在java中这样不行，我们必须规定一种类型，只有该类型或该类型的子类的元素可以作为合法的输入。

因此在python中，我们只需要一个对象“像鸭子一样”就可以把它当鸭子使用。



##### Special Methods

```python
class Book:
   def __init__(self, title, author, pages):
      print "A book is created"
      self.title = title
      self.author = author
      self.pages = pages

   def __str__(self):
      return "Title:%s , author:%s, pages:%s " % \
              (self.title, self.author, self.pages)

   def __len__(self):
      return self.pages

   def __del__(self):
      print "A book is destroyed"


book = Book("Inside Steve's Brain", "Leander Kahney", 304)

print book
print len(book)
del book
```

You can also define the basic operator from yourself.

```python
class Vector:

  def __init__(self, data):
    self.data = data

  def __str__(self):
    return repr(self.data)

  def __add__(self, other):
    data = []
    for j in range(len(self.data)):
      data.append(self.data[j] + other.data[j])
    return Vector(data)

  def __sub__(self, other):
    data = []
    for j in range(len(self.data)):
      data.append(self.data[j] - other.data[j])
    return Vector(data)
```

So, when you call the len(), it's just call the inner len function.

```python
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
```

##### 类内部域声明及限制（slots）

类内部实现，可以在函数外部声明变量，由此使得全部类成员函数均可调用

```python
def Animal:
    animaltype = "Animal"
```

同时我们可以在类的声明结束之后在实例化之后动态绑定方法，

```python
a = Animal()
a.age = 10
print（a.age)
```

为了限制在类的声明结束之后的动态绑定，我们可以在类的原始声明中加入：

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

由此声明之后的类实例就只能有name和age两个属性。即使在类的定义内部，你也只能绑定两个属性。



##### Type()

type()可以用来动态创建一个类，也就是在程序执行的过程中创建一个类。

```python
>>> def fn(self, name='world'): # 先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
```

首先我们将类中需要的函数声明好，然后确定新类需要继承的类，然后确定类名。

type()函数接受的第一个参数是类名，第二个参数是该类继承的类（注意此处由于允许多重继承的存在，所以才用了一个tuple来记载继承的父类名称，当没有继承关系时，我们只继承object父类，但是此时也要写成tuple的形式），第三个参数是一个dict，里面写清楚key和value的关系，key是类成员函数的名称，value是这个成员函数要绑定的函数对象的名称。



##### metaclass and Object Relational Mapping(ORM)

...用到再看吧。。。

http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000

