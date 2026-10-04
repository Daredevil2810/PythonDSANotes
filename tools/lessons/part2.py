from part1 import add

add(id="functions-basics", section=3, title="Functions: def, parameters & return", time="10 min",
 summary="Write a piece of logic once and reuse it anywhere.",
 what="A **function** is a named block of reusable code. You define it with `def`, give it inputs called **parameters**, and it can hand back a result with `return`.",
 why="Without functions you would copy-paste the same code again and again. Functions keep programs short, testable and readable. Every DSA solution you will write is a function.",
 simple="A function is a **coffee machine**. You press a button (call it), put in beans and water (parameters), and it gives you coffee (the return value). You don't rebuild the machine every time you want coffee.",
 tech="`def name(params):` creates a function object. `return` ends the function and sends a value to the caller. If there is no `return`, the function returns `None`. Arguments can be positional, keyword or default.",
 table=dict(head=["Kind","Example","Meaning"], rows=[["Positional","add(5, 3)","Matched by position"],["Keyword","add(b=3, a=5)","Matched by name"],["Default","def greet(name=\"Devanshu\")","Used if nothing is passed"]]),
 blocks=[
  dict(title="Define, call, return", code=r'''def greet():
    print("Hello Developer!")

greet()                      # call it

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)''', output="Hello Developer!\nSum: 8",
   lines=[("def greet():","Creates a function called `greet` that takes no inputs. Nothing runs yet."),("greet()","The parentheses **call** it, and now the body runs."),("def add(a, b):","Two parameters, `a` and `b`, act like blank slots."),("return a + b","Sends the sum back to whoever called the function."),("result = add(5, 3)","5 goes into `a`, 3 into `b`. The returned 8 is stored in `result`.")]),
  dict(title="Three ways to pass arguments, and a default", code=r'''def add(a, b):
    return a + b

print(add(5, 3))          # positional
print(add(b=3, a=5))      # keyword

def welcome(name="Devanshu"):
    print("Welcome,", name)

welcome()
welcome("Ravi")

def no_return():
    x = 1

print(no_return())''', output="8\n8\nWelcome, Devanshu\nWelcome, Ravi\nNone",
   lines=[("add(5, 3)","By position: first value to `a`, second to `b`."),("add(b=3, a=5)","By name, so the order doesn't matter."),('def welcome(name="Devanshu"):',"If the caller passes nothing, `name` falls back to this default."),("welcome()","Uses the default."),('welcome("Ravi")',"Overrides the default."),("print(no_return())","No `return` line, so the function gives back `None`.")])],
 mistakes=["Printing inside a function when you meant to `return`. A printed value can't be reused by other code.","Using a mutable default like `def f(x=[])`. The same list is reused across calls.","Forgetting the parentheses when calling: `greet` is the function, `greet()` runs it."],
 use="Whenever you notice the same steps twice, or when a piece of logic deserves a name. In interviews, write the solution as a function so it's easy to test.",
 qa=[("What is the default return type of a function?","`None`, if you don't explicitly return something."),("Difference between parameter and argument?","A parameter is the name in the definition (`a`). An argument is the actual value you pass in the call (`5`).")],
 tryit=dict(task="Write a function `square(n)` that returns the square of `n`. Print `square(6)`.", hint="`n * n` or `n ** 2`.", solution=r'''def square(n):
    return n * n

print(square(6))''', output="36"),
 related=["recursion-math-01","arrays-strings-09"])

add(id="args-kwargs", section=3, title="*args and **kwargs", time="10 min",
 summary="Accept any number of inputs in one function.",
 what="`*args` collects any number of extra **positional** arguments into a tuple. `**kwargs` collects any number of extra **keyword** arguments into a dictionary.",
 why="Sometimes you can't know how many inputs a function will get, for example a `total()` that adds 2 numbers today and 20 tomorrow. You also see `*args, **kwargs` constantly in Django and library code.",
 simple="You are ordering at a food stall. `*args` is *\"and a few more things, whatever you have\"* in a plain list. `**kwargs` is *\"and these special requests\"*, each with a label: `spice=\"high\"`, `extra=\"cheese\"`.",
 tech="The single `*` packs leftover positional arguments into a **tuple**. The double `**` packs leftover keyword arguments into a **dict**. The names `args` and `kwargs` are only convention; the stars are what matter.",
 blocks=[
  dict(title="*args", code=r'''def total(*nums):
    print(nums)
    return sum(nums)

print(total(1, 2, 3))
print(total(10, 20, 30, 40, 50))''', output="(1, 2, 3)\n6\n(10, 20, 30, 40, 50)\n150",
   lines=[("def total(*nums):","The star means: put every positional argument into one tuple called `nums`."),("print(nums)","Shows that it really is a tuple."),("return sum(nums)","`sum()` adds up all items, however many there are.")]),
  dict(title="All of it together", code=r'''def info(name, *skills, **details):
    print("Name:", name)
    print("Skills:", skills)
    print("Details:", details)

info("Devanshu", "Python", "Django", location="India", experience="Fresher")''', output="Name: Devanshu\nSkills: ('Python', 'Django')\nDetails: {'location': 'India', 'experience': 'Fresher'}",
   lines=[("def info(name, *skills, **details):","`name` is a normal parameter. `*skills` swallows any extra positional values. `**details` swallows any extra `key=value` pairs."),('info("Devanshu", "Python", "Django", ...)','"Devanshu" → `name`. "Python" and "Django" → the `skills` tuple.'),('location="India", experience="Fresher"',"These have names, so they go into the `details` dictionary.")])],
 mistakes=["Putting `*args` after `**kwargs`. The order must be: normal parameters, `*args`, keyword defaults, `**kwargs`.","Expecting `args` to be a list. It is a tuple.","Passing keyword arguments to a function that only has `*args`; that raises a `TypeError`."],
 use="Use `*args`/`**kwargs` for flexible helpers, wrappers that pass inputs on to another function, and when you cannot predict the number of inputs.",
 qa=[("What are *args and **kwargs used for?","`*args` accepts multiple positional arguments (as a tuple). `**kwargs` accepts multiple keyword arguments (as a dictionary)."),("Can you use both in one function?","Yes, in this order: `def func(positional, *args, keyword_default=None, **kwargs)`.")],
 tryit=dict(task="Write `average(*nums)` that returns the average of any numbers. Print `average(10, 20, 30)`.", hint="Total divided by how many: `sum(nums) / len(nums)`.", solution=r'''def average(*nums):
    return sum(nums) / len(nums)

print(average(10, 20, 30))''', output="20.0"),
 related=[])

add(id="scope-legb", section=3, title="Scope & the LEGB rule", time="8 min",
 summary="Where a variable lives, and how Python finds it.",
 what="**Scope** is the part of the program where a variable can be seen. Python looks for a name in four places, in this order: **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in (LEGB).",
 why="Scope bugs are some of the most confusing ones: a variable that seems to exist but doesn't, or a function that changes a value you didn't expect. It is also a favourite interview question.",
 simple="Think of searching for a pen. First your **pocket** (local). Then your **bag** (enclosing function). Then the **room** (global). Finally the **shop** (built-in). You use the first pen you find, and never look further.",
 tech="Inside a function, assigning to a name creates a **local** variable by default. To rebind a module-level name you must declare it `global` (or `nonlocal` for an enclosing function). Names like `len` and `print` come from the built-in scope.",
 blocks=[
  dict(title="Three variables named x", code=r'''x = 10          # Global

def outer():
    x = 20      # Enclosing
    def inner():
        x = 30  # Local
        print(x)
    inner()

outer()
print(x)''', output="30\n10",
   lines=[("x = 10","A global variable, visible everywhere in this file."),("x = 20","A new variable `x` that lives only inside `outer`. It does not change the global one."),("x = 30","Another new `x`, only inside `inner`."),("print(x)  # inside inner","Python looks Local first, finds 30, and stops."),("print(x)  # last line","Out here only the global `x` exists, so 10 is printed.")]),
  dict(title="Changing a global with the global keyword", code=r'''counter = 0

def add_one():
    global counter
    counter += 1

add_one()
add_one()
print(counter)''', output="2",
   lines=[("global counter","Tells Python: don't make a new local `counter`, use the global one."),("counter += 1","Now this really changes the global variable. Without the `global` line you'd get an `UnboundLocalError`.")])],
 mistakes=["Assigning to a global name inside a function without declaring `global`.","Using the same variable name at every level and then not knowing which one prints.","Overusing `global`. Prefer passing values in and returning results."],
 use="Keep variables as local as possible. Reach for `global` only for true program-wide settings or counters, and prefer function parameters and return values.",
 qa=[("What is the LEGB rule?","The order in which Python looks up a name: Local → Enclosing → Global → Built-in."),("How do you modify a global variable inside a function?","Declare it with the `global` keyword first.")],
 tryit=dict(task="What does this print? Predict first, then run it:\n`x = 5` / `def f(): x = 8; return x` / `f()` / `print(x)`", hint="The `x` inside `f` is a separate local variable.", solution=r'''x = 5

def f():
    x = 8
    return x

f()
print(x)''', output="5"),
 related=[])

add(id="lambda-higher-order", section=3, title="lambda, map, filter & reduce", time="12 min",
 summary="Tiny one-line functions, and the tools that use them.",
 what="A **lambda** is a small anonymous function written in one line: `lambda arguments: expression`. `map`, `filter` and `reduce` take a function and apply it to a whole collection.",
 why="They let you transform, select and combine data in a single readable line. `sorted(..., key=lambda ...)` is used all the time in interview solutions.",
 simple="`map` is a **stamp** pressed on every page of a notebook. `filter` is a **sieve** that lets only the right items through. `reduce` is a **snowball**: it keeps rolling over the items, collecting everything into one number.",
 tech="A lambda may contain only a single expression (no statements). Functions are first-class objects in Python, so they can be passed as arguments. `map` and `filter` return lazy iterators, which is why we wrap them in `list()`. `reduce` lives in `functools`.",
 table=dict(head=["Function","What it does","Example"], rows=[["map()","Apply a function to every item","map(lambda x: x*x, nums)"],["filter()","Keep items that pass a test","filter(lambda x: x>0, nums)"],["reduce()","Combine all items into one","reduce(lambda x,y: x+y, nums)"]]),
 blocks=[
  dict(title="lambda vs def, and sorting with a key", code=r'''add = lambda a, b: a + b
print(add(5, 3))

pairs = [(1, 2), (3, 1), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)''', output="8\n[(5, 0), (3, 1), (1, 2)]",
   lines=[("add = lambda a, b: a + b","Same as `def add(a, b): return a + b`, but on one line. The result of the expression is returned automatically."),("key=lambda x: x[1]","`sorted` asks: \"what should I sort by?\" The lambda answers: the second item of each pair."),("[(5, 0), (3, 1), (1, 2)]","Sorted by 0, 1, 2 (the second values).")]),
  dict(title="map, filter and reduce", code=r'''from functools import reduce

nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
print(reduce(lambda x, y: x + y, nums))

def square(x): return x * x
def operate(func, val): return func(val)
print(operate(square, 5))''', output="[2, 4, 6, 8, 10]\n[2, 4]\n15\n25",
   lines=[("map(lambda x: x * 2, nums)","Doubles every number."),("filter(lambda x: x % 2 == 0, nums)","Keeps only the even ones."),("reduce(lambda x, y: x + y, nums)","Adds 1+2, then 3, then 4, then 5, and ends with 15."),("operate(square, 5)","A function passed into another function. This works because functions are first-class objects.")])],
 mistakes=["Writing a long, complicated lambda. If it needs more than one simple expression, use `def`.","Printing `map(...)` directly and being surprised. Wrap it in `list()`.","Forgetting `from functools import reduce`."],
 use="Use a lambda for a short throwaway function (especially as a `key=`). Use `def` as soon as the logic has a name or more than one step.",
 qa=[("Difference between def and lambda?","`def` creates a named function that may contain many statements. A lambda is anonymous and limited to one expression."),("Can a lambda have multiple expressions?","No, only one expression (no loops or multiple statements)."),("How can you pass a function into another function?","Functions are first-class objects, so you simply pass the name: `operate(square, 5)`.")],
 tryit=dict(task="From `numbers = [10, 15, 22, 33, 42, 55, 60]` get the even numbers with `filter` and a lambda, and print the average of all numbers using `reduce`.", hint="Average = total / count. Use `reduce` for the total.", solution=r'''from functools import reduce

numbers = [10, 15, 22, 33, 42, 55, 60]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

average = reduce(lambda a, b: a + b, numbers) / len(numbers)
print("Average:", average)''', output="Even numbers: [10, 22, 42, 60]\nAverage: 33.857142857142854"),
 related=[])

# ---------------- OOP ----------------
add(id="classes-objects", section=4, title="Classes & objects", time="12 min",
 summary="Bundle data and behaviour together using a blueprint.",
 what="A **class** is a blueprint. An **object** (instance) is a real thing built from that blueprint. `__init__` runs automatically when an object is created, and `self` means \"this particular object\".",
 why="Large programs are easier to manage when related data and actions live together. Django models, forms and views are all classes, so OOP is the base of backend work.",
 simple="A class is the **architect's plan of a house**. You can't live in a plan. Each real house built from it is an **object**. All houses follow the plan, but each has its own owner and its own colour.",
 tech="`__init__(self, ...)` is the initialiser (commonly called the constructor). `self` is the first parameter of an instance method and refers to the object the method was called on, similar to `this` in Java. Attributes set on `self` belong to that one instance.",
 blocks=[
  dict(title="The Developer class", code=r'''class Developer:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show_info(self):
        print(f"{self.name} works as a {self.role}")

dev1 = Developer("Devanshu", "Python Developer")
dev2 = Developer("Ravi", "Tester")
dev1.show_info()
dev2.show_info()''', output="Devanshu works as a Python Developer\nRavi works as a Tester",
   lines=[("class Developer:","Starts the blueprint named `Developer`."),("def __init__(self, name, role):","Runs by itself the moment an object is created. It receives the values you pass in."),("self.name = name","Stores the value **on this object**, so `dev1` and `dev2` each keep their own name."),("def show_info(self):","A method: a function that belongs to the class. `self` gives it access to this object's data."),('dev1 = Developer("Devanshu", "Python Developer")',"Builds an object. Python calls `__init__` for us; `self` is filled in automatically."),("dev1.show_info()","Calls the method on `dev1`, so it prints dev1's details.")])],
 mistakes=["Forgetting `self` as the first parameter of a method.","Writing `name = name` instead of `self.name = name`, so nothing is stored on the object.","Mixing up the class (`Developer`) with an object (`dev1`)."],
 use="Use a class when you have several pieces of data that belong together and actions that work on them: a user, a bank account, a linked-list node.",
 qa=[("What is a class and what is an object?","A class is a blueprint; an object is an instance of that class."),("What is self in Python?","It represents the instance of the class itself and lets methods access its attributes and other methods."),("Is __init__ a constructor?","Yes, it initialises the object when it is created.")],
 tryit=dict(task="Create a class `Car` with `brand` and `year`. Add a method `describe()` that prints `Toyota, 2020`. Make one car and call it.", hint="Copy the `Developer` pattern: `__init__` stores both values, `describe` prints an f-string.", solution=r'''class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def describe(self):
        print(f"{self.brand}, {self.year}")

Car("Toyota", 2020).describe()''', output="Toyota, 2020"),
 related=["linked-list-01"])

add(id="method-types", section=4, title="Instance, class & static methods", time="8 min",
 summary="Three kinds of methods, and when each one fits.",
 what="An **instance method** works with one object (`self`). A **class method** works with the class itself (`cls`). A **static method** needs neither; it's just a function that lives inside the class for organisation.",
 why="This is a classic interview question, and it shows you understand where data belongs: with one object, with all objects, or with neither.",
 simple="In a school: an **instance method** is *\"this student's marks\"*. A **class method** is *\"the school's total number of students\"*. A **static method** is *\"a calculator on the principal's desk\"*: useful, but it doesn't care about any particular student or the school.",
 tech="`@classmethod` receives the class as its first argument (`cls`), so it can read or change class-level data and create instances. `@staticmethod` receives no automatic first argument.",
 blocks=[
  dict(title="All three together", code=r'''class Demo:
    def instance_method(self):
        print("Called using object")

    @classmethod
    def class_method(cls):
        print("Called using class")

    @staticmethod
    def static_method():
        print("Called without object or class reference")

d = Demo()
d.instance_method()
Demo.class_method()
Demo.static_method()''', output="Called using object\nCalled using class\nCalled without object or class reference",
   lines=[("def instance_method(self):","Gets the object as `self`. Can use the object's own data."),("@classmethod","A **decorator**: it changes how the method below it behaves."),("def class_method(cls):","Gets the class itself as `cls`."),("@staticmethod","Marks a method that gets neither `self` nor `cls`."),("d.instance_method()","Needs an object, `d`."),("Demo.class_method()","Can be called on the class directly; no object needed.")])],
 mistakes=["Using a static method when you actually need to read class data (you need a class method).","Forgetting the decorator line, then wondering why `cls` behaves like `self`."],
 use="Instance method by default. Class method for alternative constructors or class-wide data. Static method for helper functions related to the class but independent of it.",
 qa=[("Difference between @classmethod and @staticmethod?","`@classmethod` accesses class data through `cls`. `@staticmethod` has no `self` or `cls` and behaves like a normal function inside the class.")],
 tryit=dict(task="Add a class variable `count = 0` to a `Student` class. Every time a student is created, increase it. Create 3 students and print `Student.count`.", hint="Inside `__init__`, write `Student.count += 1`.", solution=r'''class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

Student("A"); Student("B"); Student("C")
print(Student.count)''', output="3"),
 related=[])

add(id="inheritance", section=4, title="Inheritance, super() & overriding", time="12 min",
 summary="Build a new class on top of an existing one.",
 what="**Inheritance** lets a child class reuse the attributes and methods of a parent class. `super()` calls the parent's version. If the child defines a method with the same name, it **overrides** the parent's.",
 why="You avoid rewriting shared code. A `Manager` is also an `Employee`, so it should not need to repeat everything an employee has.",
 simple="A child inherits **the family surname and recipes**, but can add her own talents or cook a recipe differently. The parent class is the family; the child class is a family member with extras.",
 tech="`class Child(Parent)` makes `Parent` a base class. `super().__init__(...)` runs the parent's initialiser. Types: **single** (one parent), **multiple** (several parents), **multilevel** (parent → child → grandchild) and **hierarchical** (one parent, several children).",
 blocks=[
  dict(title="Employee → Developer", code=r'''class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working")

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def code(self):
        print(f"{self.name} codes in {self.language}")

dev = Developer("Devanshu", "Python")
dev.work()
dev.code()''', output="Devanshu is working\nDevanshu codes in Python",
   lines=[("class Developer(Employee):","The brackets say: `Developer` inherits from `Employee`."),("super().__init__(name)","Asks the parent to set up `self.name`, so we don't repeat that code."),("self.language = language","Something only developers have."),("dev.work()","`Developer` has no `work` method of its own, so Python finds it in `Employee`."),("dev.code()","This one is the child's own method.")]),
  dict(title="Overriding (the mini task)", code=r'''class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"{self.name} earns {self.salary} per month")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_info(self):
        super().show_info()
        print(f"Manages a team of {self.team_size} people")

emp = Employee("Devanshu", 40000)
mgr = Manager("Ravi", 80000, 10)
emp.show_info()
mgr.show_info()''', output="Devanshu earns 40000 per month\nRavi earns 80000 per month\nManages a team of 10 people",
   lines=[("def show_info(self):  # in Manager","Same name as the parent's method, so this version **overrides** it for managers."),("super().show_info()","Reuses the parent's printing first..."),('print(f"Manages a team of ...")',"...then adds the manager-only line.")])],
 mistakes=["Forgetting to call `super().__init__()`, so parent attributes never get set.","Overriding a method and forgetting that the parent version no longer runs unless you call `super()`.","Using inheritance when the relationship is \"has a\" rather than \"is a\"."],
 use="Use inheritance when the child truly *is a kind of* the parent (a Manager is an Employee) and shares real behaviour.",
 qa=[("How do you call the parent constructor in a child class?","Using `super().__init__()`."),("What happens if parent and child have the same method?","The child's method overrides the parent's (method overriding)."),("Name the types of inheritance.","Single, multiple, multilevel and hierarchical.")],
 tryit=dict(task="Make `Animal` with a method `speak()` that prints `Some sound`. Make `Dog(Animal)` that overrides it to print `Woof`. Call it on a Dog.", hint="Same method name in the child class.", solution=r'''class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

Dog().speak()''', output="Woof"),
 related=["linked-list-01"])

add(id="encapsulation", section=4, title="Encapsulation & private attributes", time="8 min",
 summary="Protect data so it is changed only in safe ways.",
 what="**Encapsulation** means restricting direct access to data and exposing safe methods instead. In Python, a name that starts with a double underscore (`__balance`) is treated as private.",
 why="If anyone can set `balance = -999` directly, bugs are guaranteed. With encapsulation, changes go through methods like `deposit()` which can check the rules.",
 simple="A bank doesn't let you walk into the vault. You talk to the **cashier**, who follows rules for deposits and withdrawals. The vault is the private data; the cashier is the method.",
 tech="Python does not have true private members. A double-underscore name is **name-mangled** to `_ClassName__name`, which makes accidental access fail. A single underscore (`_x`) is only a convention that means \"internal, please don't touch\".",
 blocks=[
  dict(title="BankAccount", code=r'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance      # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())

try:
    print(acc.__balance)
except AttributeError:
    print("AttributeError: __balance is private")''', output="1500\nAttributeError: __balance is private",
   lines=[("self.__balance = balance","The double underscore marks the attribute as private."),("def deposit(self, amount):","The approved way to change the balance. This is where you'd add checks."),("def get_balance(self):","The approved way to read it."),("acc.__balance","Direct access from outside fails with an `AttributeError`.")])],
 mistakes=["Believing `__x` is truly secret. It can still be reached as `_BankAccount__balance`.","Making everything private. Do it only for data that needs protecting."],
 use="Use it for data with rules (money, passwords, counters) where you want to control how it changes.",
 qa=[("How do you make attributes private in Python?","Prefix the name with a double underscore (`__`)."),("What is encapsulation?","Hiding internal data and exposing it only through methods.")],
 tryit=dict(task="Add a `withdraw(amount)` method to `BankAccount` that only withdraws if there is enough balance; otherwise print `Insufficient funds`.", hint="Compare `amount` with `self.__balance` using `if`.", solution=r'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.withdraw(1500)
acc.withdraw(300)
print(acc.get_balance())''', output="Insufficient funds\n700"),
 related=[])

add(id="polymorphism-abstraction", section=4, title="Polymorphism & abstraction", time="10 min",
 summary="Same method name, different behaviour, and forcing a structure on child classes.",
 what="**Polymorphism** means one name, many behaviours: different classes can each have their own `sound()`. **Abstraction** hides details and forces child classes to implement certain methods, using an abstract base class (`ABC`).",
 why="Code can treat many kinds of objects the same way (`for bird in birds: bird.sound()`) without caring which one it is. Abstraction guarantees every shape *has* an `area()`.",
 simple="Press the **horn** button in any vehicle: a car beeps, a bike rings, a truck blares. Same button, different result. That's polymorphism. A driving-licence rule that says *\"every vehicle must have a horn\"* is abstraction.",
 tech="Polymorphism here is achieved by method overriding. A class derived from `ABC` with `@abstractmethod` methods cannot be instantiated; subclasses must implement all abstract methods first.",
 blocks=[
  dict(title="Polymorphism with birds", code=r'''class Bird:
    def sound(self):
        print("Some sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")

class Crow(Bird):
    def sound(self):
        print("Caw Caw")

for bird in [Sparrow(), Crow()]:
    bird.sound()''', output="Chirp Chirp\nCaw Caw",
   lines=[("class Sparrow(Bird):","Inherits from `Bird`."),("def sound(self):","Both children define `sound` differently."),("for bird in [Sparrow(), Crow()]:","One loop treats different objects the same way."),("bird.sound()","Python picks the right version for each object.")]),
  dict(title="Abstraction with Shape", code=r'''from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

sq = Square(5)
print(sq.area())

try:
    Shape()
except TypeError:
    print("Cannot create an abstract Shape")''', output="25\nCannot create an abstract Shape",
   lines=[("class Shape(ABC):","An abstract base class: a rule-book, not a real shape."),("@abstractmethod","Every child **must** provide its own `area`."),("class Square(Shape):","Fulfils the rule by implementing `area`."),("Shape()","Not allowed: you can't build something that's only a rule.")])],
 mistakes=["Forgetting to implement every abstract method in the child, which makes the child abstract too.","Confusing overriding (same name in child) with overloading (Python doesn't support classic overloading)."],
 use="Polymorphism whenever one loop or function should handle many related types. Abstraction when you want to enforce a common interface (shapes, payment methods, database backends).",
 qa=[("What is method overriding?","A subclass defines a method with the same name as one in its parent class, replacing it."),("Why use abstraction?","To enforce a structure and hide implementation details."),("How does OOP connect to Django?","Models are classes representing tables, views can be classes, and forms are classes for validation and rendering.")],
 tryit=dict(task="Make an abstract class `Shape` with `area()`. Create `Rectangle(w, h)` and print the area of a 4 × 6 rectangle.", hint="Copy the `Square` example but store two values.", solution=r'''from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

print(Rectangle(4, 6).area())''', output="24"),
 related=[])

# ---------------- Files, exceptions, modules ----------------
add(id="file-handling", section=5, title="File handling", time="10 min",
 summary="Read from and write to files, safely.",
 what="File handling means opening a file, reading or writing it, and closing it. The `with` statement does the closing for you automatically.",
 why="Backends write logs, save uploads and store data. Reading and writing files is the first step to programs that remember things after they stop running.",
 simple="A file is a **notebook**. Mode `r` means you only read it. `w` means you tear out everything and write fresh pages. `a` means you add notes at the end. `with` is a helpful assistant who closes the notebook for you, even if you get interrupted.",
 tech="`open(name, mode)` returns a file object. Modes: `r` (default), `w` (overwrite), `a` (append), `r+` (read and write), `b` (binary). `with open(...) as f` guarantees `f.close()` even if an exception occurs.",
 table=dict(head=["Mode","Meaning"], rows=[["r","Read (default)"],["w","Write, overwrites existing content"],["a","Append to the end"],["r+","Read and write"],["b","Binary mode (images, video)"]]),
 blocks=[
  dict(title="Write, read, append", code=r'''file = open("demo.txt", "w")
file.write("Hello, this is a test file.\n")
file.write("Python file handling is easy!")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()

with open("demo.txt", "a") as f:
    f.write("\nAdding a new line safely.")''', output="Hello, this is a test file.\nPython file handling is easy!",
   lines=[('open("demo.txt", "w")',"Opens (and creates if needed) `demo.txt` for writing. Anything already inside is erased."),("file.write(...)","Writes text. `\\n` is a new line."),("file.close()","Releases the file. Forgetting this can lose data."),("file.read()","Returns the entire content as one string."),('with open("demo.txt", "a") as f:',"Opens in append mode and closes automatically at the end of the block, even on errors.")]),
  dict(title="Reading line by line", code=r'''with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip())''', output="Hello, this is a test file.\nPython file handling is easy!\nAdding a new line safely.",
   lines=[("for line in f:","A file can be looped over, one line at a time. Great for big files because it doesn't load everything at once."),("line.strip()","Removes the invisible newline at the end of each line, so `print` doesn't double-space.")], needs_prev=True)],
 mistakes=["Using `w` when you meant `a`, which wipes the file.","Not closing the file. Use `with`.","Forgetting that `read()` returns text, not a list of lines (use `readlines()` or loop)."],
 use="Always prefer `with open(...)`. Use `r` to read, `a` to log or add, and `w` only when you really want to start fresh.",
 qa=[("Why use with open() instead of open()?","It automatically closes the file, even if an error occurs."),("Difference between 'w' and 'a'?","'w' overwrites the file; 'a' appends to the end."),("How to read a file line by line?","`with open(\"demo.txt\") as f:` then `for line in f: print(line.strip())`.")],
 tryit=dict(task="Write the numbers 1 to 3 into `nums.txt`, one per line, then read the file back and print its contents.", hint="Use `\"w\"` and a loop with `f.write(f\"{i}\\n\")`.", solution=r'''with open("nums.txt", "w") as f:
    for i in range(1, 4):
        f.write(f"{i}\n")

with open("nums.txt") as f:
    print(f.read())''', output="1\n2\n3"),
 related=[])

add(id="exceptions", section=5, title="Exception handling", time="12 min",
 summary="Keep your program alive when things go wrong.",
 what="An **exception** is an error that happens while the program is running. `try` holds risky code, `except` says what to do if it fails, `finally` always runs, and `raise` lets you create an exception yourself.",
 why="Users type letters instead of numbers, files go missing, networks drop. Good programs handle these gracefully instead of crashing.",
 simple="You're cooking and the gas runs out. **try**: cook the meal. **except**: if the gas fails, switch to the induction stove. **finally**: either way, wash the pan afterwards.",
 tech="Python checks `except` clauses in order and runs the first one that matches. `except Exception as e` catches almost everything and gives you the error object. A **syntax error** is detected before the program runs; an **exception** happens at runtime.",
 blocks=[
  dict(title="try / except / finally", code=r'''def safe_divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Invalid input, not a number!")
    finally:
        print("Execution complete.")

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, "x")''', output="5.0\nExecution complete.\nCannot divide by zero!\nExecution complete.\nInvalid input, not a number!\nExecution complete.",
   lines=[("try:","Code that might fail goes here."),("except ZeroDivisionError:","Runs only if the error is a division by zero."),("except TypeError:","Runs if the types don't mix, such as `10 / \"x\"`."),("finally:","Runs every time: success, handled error, or unhandled error. Used for cleanup.")]),
  dict(title="Catching several errors, and raising your own", code=r'''try:
    nums = [1, 2, 3]
    print(nums[5])
except IndexError as e:
    print("Error:", e)

try:
    int("abc")
except (ValueError, ZeroDivisionError):
    print("Handled multiple exceptions")

age = 15
try:
    if age < 18:
        raise ValueError("You must be at least 18 years old")
except ValueError as e:
    print(e)''', output="Error: list index out of range\nHandled multiple exceptions\nYou must be at least 18 years old",
   lines=[("except IndexError as e:","`as e` stores the error object so we can print its message."),("except (ValueError, ZeroDivisionError):","One block can handle several error types if you put them in a tuple."),('raise ValueError("...")',"Creates an error on purpose to enforce a rule. Here it's caught right away so the program continues.")])],
 mistakes=["A bare `except:` that hides every error, including ones you needed to see.","Putting too much code inside `try`. Wrap only the risky line(s).","Catching a general `Exception` before a specific one; the specific block never runs."],
 use="Wrap operations you can't fully control (user input, files, network). Raise your own exceptions to enforce business rules.",
 qa=[("What is the purpose of finally?","Code in `finally` always runs, and is used for cleanup."),("Difference between syntax error and exception?","A syntax error is found before running. An exception happens at runtime."),("Can we use multiple except blocks?","Yes, or one block with a tuple: `except (ValueError, ZeroDivisionError):`."),("Why raise exceptions manually?","To enforce business logic or validation rules.")],
 tryit=dict(task="Write `to_int(text)` that returns `int(text)`, or prints `Not a number` and returns `None` if conversion fails. Test it with `\"42\"` and `\"hi\"`.", hint="`int(\"hi\")` raises a `ValueError`.", solution=r'''def to_int(text):
    try:
        return int(text)
    except ValueError:
        print("Not a number")
        return None

print(to_int("42"))
print(to_int("hi"))''', output="42\nNot a number\nNone"),
 related=[])

add(id="modules-packages", section=5, title="Modules & packages", time="8 min",
 summary="Split code across files and reuse code that others wrote.",
 what="A **module** is a single `.py` file. A **package** is a folder of modules that contains an `__init__.py` file. You bring them in with `import`.",
 why="No real project lives in one file. Modules keep code organised, and Python's huge standard library (math, random, os, datetime…) is available just by importing it.",
 simple="A module is a **toolbox** with tools for one job. A package is the **garage shelf** holding several toolboxes. You don't forge a hammer each time: you open the box and take it out.",
 tech="`import math` loads the module and you use `math.sqrt`. `from math import sqrt, pi` pulls names directly. Imports can be at the top of a file (usual) or inside a function.",
 blocks=[
  dict(title="Using built-in modules", code=r'''import math
print(math.sqrt(25))
print(math.pi)

from math import sqrt, pi
print(sqrt(16))''', output="5.0\n3.141592653589793\n4.0",
   lines=[("import math","Loads the whole `math` module. You must write `math.` before its functions."),("math.sqrt(25)","Square root, always returned as a float."),("from math import sqrt, pi","Imports just those two names, so you can use them without the `math.` prefix.")]),
  dict(title="Making your own module", code=r'''# file: greet.py
def say_hello(name):
    return f"Hello, {name}!"

# file: main.py (in the same folder)
import greet
print(greet.say_hello("Devanshu"))''', output="", noRun=True,
   lines=[("# file: greet.py","Any `.py` file can be imported. The file name (without `.py`) is the module name."),("import greet","Python finds `greet.py` in the same folder and loads it."),("greet.say_hello(...)","Calls the function that lives inside that module.")]),
  dict(title="A small package", code=r'''mypackage/
    __init__.py        # marks the folder as a package
    math_utils.py
    string_utils.py''', output="", noRun=True, plain=True,
   lines=[("__init__.py","This file tells Python the folder is a package.")])],
 mistakes=["Naming your own file the same as a standard module (e.g. `random.py`), which hides the real one.","`from module import *` makes it unclear where names come from.","Circular imports: file A imports B and B imports A."],
 use="Split code when a file grows long or when pieces are reusable. Import only what you need.",
 qa=[("Difference between module and package?","A module is a single Python file. A package is a collection of modules in a folder with `__init__.py`."),("How do you import specific things?","`from math import sqrt, pi`."),("Can you import a module inside a function?","Yes, imports can be local or global.")],
 tryit=dict(task="Write `save_user_info(name, age)` that appends `name - age` to `user_info.txt` using `with`, wrapped in try/except/finally. Print `User info saved successfully.` on success and `Operation complete.` at the end.", hint="Combine the file and exception lessons: `try:` → `with open(..., \"a\")` → `except Exception as e:` → `finally:`.", solution=r'''def save_user_info(name, age):
    try:
        with open("user_info.txt", "a") as f:
            f.write(f"{name} - {age}\n")
        print("User info saved successfully.")
    except Exception as e:
        print("Error saving user info:", e)
    finally:
        print("Operation complete.")

save_user_info("Devanshu", 22)''', output="User info saved successfully.\nOperation complete."),
 related=[])
