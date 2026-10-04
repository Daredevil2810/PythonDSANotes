# Lessons 1-5 (Python Basics + Control Flow). Text supports `code` and **bold**.
LESSONS = []
def add(**kw): LESSONS.append(kw)

add(id="what-is-python", section=1, title="What is Python & how it runs", time="6 min",
 summary="What kind of language Python is, and what happens between pressing Run and seeing output.",
 what="Python is a **high-level, interpreted, dynamically typed, object-oriented** language. In plain words: you write code that reads almost like English, Python runs it line by line for you, and you never have to tell it in advance what *type* each value is.",
 why="Python is used for backend web development (Django, Flask), data science, automation and scripting. It is also the most popular language for interview preparation because you can focus on the **logic** instead of fighting the syntax.",
 simple="Think of two ways to translate a book. A **compiler** translates the whole book first, then hands you the finished copy. An **interpreter** sits next to you and translates one sentence at a time while you listen. Python is the second kind, so you can test an idea instantly.",
 tech="Python source is first compiled to **bytecode** (the `.pyc` files you see in `__pycache__`), and the **Python Virtual Machine (PVM)** then interprets that bytecode. You never run a separate compile step like in C/C++.",
 steps=["You write `hello.py`.","Python compiles it to bytecode (automatically, invisibly).","The PVM reads the bytecode and runs it, one instruction at a time.","Output appears in your terminal."],
 blocks=[dict(title="Your first program", code=r'''print("Hello, PyDSA!")
print(2 + 3)''', output="Hello, PyDSA!\n5",
  lines=[('print("Hello, PyDSA!")',"`print()` shows something on the screen. Text goes inside quotes, so Python knows it is text and not a command."),
         ("print(2 + 3)","No quotes this time, so Python calculates `2 + 3` first and prints the result, `5`.")])],
 mistakes=["Forgetting the quotes around text: `print(Hello)` makes Python look for a variable called `Hello`.","Mixing tabs and spaces for indentation. Pick 4 spaces and stay with it.","Thinking Python has no types. It does. It just works them out for you while the program runs."],
 use="Use Python when you want to get an idea working quickly: scripts, web backends, data work, and interview problems.",
 qa=[("Is Python compiled or interpreted?","Both, in a way. Python source is compiled to bytecode, and that bytecode is interpreted by the Python Virtual Machine (PVM). You don't run the compile step yourself."),
     ("What does 'dynamically typed' mean?","The type of a variable is decided at runtime from the value it holds, so you don't declare types in advance."),
     ("Name some uses of Python.","Backend web development (Django/Flask), data science, automation and scripting.")],
 tryit=dict(task="Print your name on one line and the result of `10 * 4` on the next line.", hint="Two `print()` calls. Put your name in quotes, but not the calculation.", solution=r'''print("Devanshu")
print(10 * 4)''', output="Devanshu\n40"),
 related=[])

add(id="variables-data-types", section=1, title="Variables & data types", time="12 min",
 summary="Store values in named boxes, and meet the eight types you will use every single day.",
 what="A **variable** is a name that points to a value. A **data type** says what kind of value it is: a whole number, text, a list, and so on.",
 why="Every program stores and moves data around. Choosing the right type decides what you can do with the data: you can sort a list, look up a dictionary by key, and a set removes duplicates for you.",
 simple="Imagine a kitchen with labelled jars. The label is the **variable name** (`sugar`), what is inside is the **value**. A *list* is a shelf of jars in order, a *set* is a bowl where duplicates are not allowed, and a *dictionary* is a recipe book: look up the name, get the details.",
 tech="Variables are references (names) bound to objects in memory. Types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, `dict`. `list`, `set` and `dict` are **mutable**; `int`, `float`, `str`, `bool` and `tuple` are **immutable**.",
 table=dict(head=["Type","Example","Mutable?","What it is"], rows=[["int","10","No","Whole numbers"],["float","3.14","No","Decimal numbers"],["str","\"Hello\"","No","Text"],["bool","True / False","No","Yes/no values"],["list","[1, 2, 3]","Yes","Ordered, can change"],["tuple","(1, 2, 3)","No","Ordered, cannot change"],["set","{1, 2, 3}","Yes","No duplicates, no order"],["dict","{\"a\": 1}","Yes","Key → value pairs"]]),
 blocks=[
  dict(title="A profile using several types", code=r'''name = "Devanshu"
age = 22
skills = ["Python", "Django", "HTML"]
profile = {"name": name, "age": age, "skills": skills}
print(profile)

print(type(skills))
print(len(skills))''', output="{'name': 'Devanshu', 'age': 22, 'skills': ['Python', 'Django', 'HTML']}\n<class 'list'>\n3",
   lines=[('name = "Devanshu"',"A `str` (text) stored in the variable `name`."),("age = 22","An `int`. No quotes, so it is a number."),('skills = ["Python", "Django", "HTML"]',"A `list`: ordered items inside square brackets."),('profile = {"name": name, ...}',"A `dict` that groups the three values under keys, like a form with labelled fields."),("print(type(skills))","`type()` tells you what kind of value something is."),("print(len(skills))","`len()` counts the items. The list has 3.")]),
  dict(title="Mutable vs immutable", code=r'''skills = ["Python", "Django"]
skills.append("HTML")      # lists can change
print(skills)

point = (3, 4)
try:
    point[0] = 10          # tuples cannot
except TypeError:
    print("Tuples are immutable")''', output="['Python', 'Django', 'HTML']\nTuples are immutable",
   lines=[('skills.append("HTML")',"Adds a new item to the end of the same list. Lists are mutable, so this is allowed."),("point = (3, 4)","A tuple: like a list that is locked after creation."),("point[0] = 10","Python refuses, and raises a `TypeError`."),("except TypeError:","We catch that error so the program continues and prints a message.")]),
  dict(title="== vs is, and shared lists", code=r'''a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)    # same values?
print(a is b)    # same object?

c = a            # c points to the SAME list
c.append(4)
print(a)''', output="True\nFalse\n[1, 2, 3, 4]",
   lines=[("print(a == b)","`==` compares **values**. Both lists contain 1, 2, 3, so `True`."),("print(a is b)","`is` compares **identity**: are they the very same object in memory? No, they are two separate lists, so `False`."),("c = a","This does **not** copy the list. It gives the same list a second name."),("c.append(4)","Changing the list through `c`..."),("print(a)","...also shows up through `a`, because there is only one list.")])],
 mistakes=["Using `is` to compare values. Use `==` for values and `is` only for checks like `x is None`.","Thinking `c = a` makes a copy. For a real copy use `a.copy()` or `a[:]`.","Using a list when you need to look things up by name. A dictionary is the right tool."],
 use="List for ordered, changeable collections. Tuple for fixed groups (like coordinates). Set to remove duplicates or test membership fast. Dict to look values up by key.",
 qa=[("Difference between list and tuple?","A list is mutable (can be changed), a tuple is immutable."),("How are Python variables typed?","Dynamically: the type is assigned at runtime from the value."),("What's the difference between `is` and `==`?","`==` compares values. `is` compares identity (the memory location)."),("What happens when you do `a = b = [1,2,3]`?","Both names point to the same list in memory, so changing one changes the other.")],
 tryit=dict(task="Create a `profile` dictionary with `name`, `role` and a `skills` list. Add one more skill with `append`, then print every skill on its own line.", hint="Use `profile[\"skills\"].append(...)`, then loop with `for skill in profile[\"skills\"]:`.", solution=r'''profile = {
    "name": "Your Name",
    "role": "Python Developer",
    "skills": ["Python", "Django", "HTML", "CSS"]
}
profile["skills"].append("AJAX")
for skill in profile["skills"]:
    print(skill)''', output="Python\nDjango\nHTML\nCSS\nAJAX"),
 related=["arrays-strings-01","arrays-strings-02"])

add(id="if-elif-else", section=2, title="Decisions: if, elif, else", time="8 min",
 summary="Make your program choose between paths based on a condition.",
 what="A **conditional statement** runs a block of code only when a condition is true. `if` checks the first condition, `elif` (else-if) checks more, and `else` catches everything left.",
 why="Almost every real program has to decide something: is the user old enough, is the password right, is the number positive. Conditions are the decision-making part of every interview problem.",
 simple="Think of a traffic light. **If** it is green, go. **Else if** it is yellow, slow down. **Else** (red), stop. Only *one* of the three things happens.",
 tech="Python evaluates conditions top to bottom and runs the first block whose condition is truthy, then skips the rest. Blocks are defined by **indentation** (usually 4 spaces), not braces.",
 blocks=[
  dict(title="Positive, zero or negative", code=r'''x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")''', output="Positive",
   lines=[("if x > 0:","Check the first condition. `10 > 0` is true."),('    print("Positive")',"The indented line belongs to the `if`. It runs, and Python skips the `elif` and `else`."),("elif x == 0:","Only checked if the `if` was false. Notice `==` (compare), not `=` (assign)."),("else:","The fallback when nothing above was true.")]),
  dict(title="A real-life check, and the one-line version", code=r'''age = 18
if age >= 18:
    print("Eligible to apply for this job")
else:
    print("Not eligible yet")

status = "Adult" if age >= 18 else "Minor"
print(status)''', output="Eligible to apply for this job\nAdult",
   lines=[("if age >= 18:","`>=` means greater than or equal to. 18 qualifies."),('status = "Adult" if age >= 18 else "Minor"',"The **ternary** form: `value_if_true if condition else value_if_false`. It chooses a value in one line.")])],
 mistakes=["Writing `=` instead of `==` inside a condition.","Wrong indentation: lines that should be inside the `if` but are not indented.","Forgetting the colon `:` at the end of the `if`, `elif` and `else` lines."],
 use="Use `if/elif/else` whenever the next step depends on a value. Use the one-line ternary only for simple choices, since long ones become hard to read.",
 qa=[("Can you write a one-line if-else in Python?",'Yes: `status = "Adult" if age >= 18 else "Minor"`.'),("How does Python know which lines belong to an if block?","By indentation. Python has no curly braces; the indented lines are the block.")],
 tryit=dict(task="Given `n = 7`, print `Even` or `Odd` using a one-line ternary.", hint="`n % 2 == 0` is true for even numbers. `%` gives the remainder.", solution=r'''n = 7
print("Even" if n % 2 == 0 else "Odd")''', output="Odd"),
 related=["recursion-math-01"])

add(id="loops-range", section=2, title="Loops: for, while & range()", time="12 min",
 summary="Repeat work without repeating code.",
 what="A **loop** runs the same block of code many times. `for` walks through a collection (list, string, range). `while` keeps going as long as a condition stays true.",
 why="Computers are good at repetition. Summing numbers, searching a list, printing a pattern and sorting all depend on loops, which is why most DSA programs start with one.",
 simple="`for` is like a teacher calling every student on the attendance list, one by one, until the list ends. `while` is like filling a bucket: keep pouring *while* it isn't full. You may not know in advance how many pours it takes.",
 tech="`for x in iterable` pulls items one at a time until the iterable is exhausted. `while cond` re-checks the condition before each pass, so you must change something inside the loop or it never ends. `range(start, stop, step)` produces numbers from `start` up to, but not including, `stop`.",
 blocks=[
  dict(title="for loop over a list", code=r'''skills = ["Python", "Django", "HTML"]
for skill in skills:
    print("I know", skill)''', output="I know Python\nI know Django\nI know HTML",
   lines=[("for skill in skills:","Take the items of `skills` one at a time and call the current one `skill`."),('    print("I know", skill)',"Runs once per item: three items, three lines.")]),
  dict(title="while loop", code=r'''count = 1
while count <= 5:
    print("Count:", count)
    count += 1''', output="Count: 1\nCount: 2\nCount: 3\nCount: 4\nCount: 5",
   lines=[("count = 1","Starting value."),("while count <= 5:","Before every pass, Python checks this. When it becomes false, the loop stops."),("count += 1","Shorthand for `count = count + 1`. Without this line, the condition would never become false and the loop would run forever.")]),
  dict(title="range() in three flavours", code=r'''for i in range(1, 6):
    print(i, end=" ")
print()
print(list(range(0, 10, 2)))
print(list(range(5, 0, -1)))''', output="1 2 3 4 5 \n[0, 2, 4, 6, 8]\n[5, 4, 3, 2, 1]",
   lines=[("range(1, 6)","Starts at 1 and stops **before** 6, giving 1, 2, 3, 4, 5."),('print(i, end=" ")',"`end=\" \"` keeps the output on one line instead of starting a new line each time."),("range(0, 10, 2)","The third number is the **step**: 0, 2, 4, 6, 8."),("range(5, 0, -1)","A negative step counts down.")])],
 mistakes=["Expecting `range(1, 6)` to include 6. The end is always excluded.","Forgetting to update the variable in a `while` loop, which creates an infinite loop (press Ctrl+C to stop it).","Changing a list while looping over it. Loop over a copy instead."],
 use="Use `for` when you know what you are looping over. Use `while` when you loop until something happens (a condition becomes false).",
 qa=[("When would you use while instead of for?","When you don't know in advance how many times to repeat and the loop depends on a condition."),("What does range(0, 10, 2) produce?","0, 2, 4, 6, 8. The step is 2 and the end value 10 is excluded.")],
 tryit=dict(task="Print the multiplication table of 5 from 5 × 1 to 5 × 10, in the form `5 x 3 = 15`.", hint="Loop `i` over `range(1, 11)` and print an f-string.", solution=r'''for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")''', output="5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50"),
 related=["patterns-01","arrays-strings-01"])

add(id="loop-control", section=2, title="break, continue, pass, for…else & nested loops", time="14 min",
 summary="Control exactly how a loop runs, and write the classic prime-number check.",
 what="`break` leaves the loop immediately. `continue` skips the rest of the current pass. `pass` does nothing (a placeholder). A loop can also have an `else` that runs only if it was **not** stopped by `break`. A loop inside a loop is a **nested loop**.",
 why="Real searches stop as soon as they find the answer (`break`). Real filters skip unwanted items (`continue`). Nested loops are the engine behind patterns, matrices and many sorting algorithms.",
 simple="You are looking for your keys in a row of drawers. **break**: you find them in drawer 3, you stop searching. **continue**: drawer 2 is locked, skip it and go on. **for…else**: after opening *every* drawer without finding them, you say *\"not here\"*. That is the `else`.",
 tech="`for … else`: the `else` block runs when the loop finishes normally, meaning it was never exited via `break`. For nested loops the inner loop completes fully for every single pass of the outer loop, so 3 × 2 passes means 6 inner iterations.",
 blocks=[
  dict(title="continue and break", code=r'''for i in range(5):
    if i == 2:
        continue      # skip 2
    elif i == 4:
        break         # stop at 4
    print(i)''', output="0\n1\n3",
   lines=[("if i == 2:","When `i` is 2..."),("continue","...jump straight to the next pass, so 2 is never printed."),("elif i == 4:","When `i` reaches 4..."),("break","...leave the loop completely. 4 is never printed either.")]),
  dict(title="for…else and the prime check", code=r'''num = 7
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")''', output="Prime",
   lines=[("for i in range(2, num):","Try every possible divisor from 2 up to 6."),("if num % i == 0:","If `i` divides `num` with no remainder, `num` has a factor other than 1 and itself."),("break","Found a divisor, so no need to keep checking."),("else:","Attached to the `for`, not to the `if`. It runs only when the loop ends without `break`, meaning no divisor was found, so the number is prime.")]),
  dict(title="Nested loops", code=r'''for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")''', output="i=1, j=1\ni=1, j=2\ni=2, j=1\ni=2, j=2\ni=3, j=1\ni=3, j=2",
   lines=[("for i in range(1, 4):","Outer loop: runs for i = 1, 2, 3."),("for j in range(1, 3):","Inner loop: restarts and runs fully (j = 1, 2) for **each** value of `i`."),('print(f"i={i}, j={j}")',"3 outer × 2 inner = 6 lines. The same idea draws every pattern in the Pattern Printing programs.")])],
 mistakes=["Putting the `else` under the `if` instead of lined up with the `for` when you mean for…else.","Using `break` inside the inner loop and expecting it to end the outer loop too. It only leaves the inner one.","Using `pass` and thinking it skips an iteration. That is `continue`; `pass` does nothing at all."],
 use="Use `break` for early exit once you've found what you need, `continue` to ignore unwanted items, `for…else` for \"search finished without finding it\", and nested loops for 2-D structures and patterns.",
 qa=[("Difference between break and continue?","`break` exits the loop immediately. `continue` skips the current iteration and moves to the next."),("How does for…else work?","The `else` runs only if the loop completed normally, that is, without hitting `break`."),("Write code to check if a number is prime.","Loop `i` from 2 to `num-1`; if `num % i == 0` print \"Not Prime\" and `break`; use `else` on the loop to print \"Prime\" (see the lesson)."),("What does pass do?","Nothing. It's a placeholder where Python needs a statement but you have nothing to write yet.")],
 tryit=dict(task="Print all even numbers from 1 to 20 on one line. Count how many are divisible by 4. Then print how many there were, or `No match found` if none.", hint="Use `i % 2 == 0` for even and `i % 4 == 0` for divisible by 4. Keep a `count` variable that goes up by 1.", solution=r'''count = 0
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
        if i % 4 == 0:
            count += 1
if count == 0:
    print("\nNo match found")
else:
    print(f"\n{count} numbers divisible by 4")''', output="2 4 6 8 10 12 14 16 18 20 \n5 numbers divisible by 4"),
 related=["arrays-strings-10","patterns-01","patterns-05"])
