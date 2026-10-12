# Section 7: NumPy for Fast Numerical Work (original lessons, own examples).
# Outputs marked AUTO are filled in by build_lessons.py from a real run, so they can never be wrong.
# Every code block is self-contained (it imports what it needs) so learners can copy and run any block alone.
from part1 import add
from part3 import AUTO

# ---------------------------------------------------------------- 1
add(id="numpy-arrays-intro", section=7, lib="numpy", title="NumPy arrays: fast lists of numbers", time="8 min",
 summary="Meet NumPy and its array, and see why `array * 2` behaves very differently from `list * 2`.",
 what="**NumPy** (short for *Numerical Python*) is a library for working with numbers in bulk. Its main object is the **array** (type name `ndarray`): a grid of values where every value has the same type.",
 why="Python lists are flexible, but doing maths on thousands of numbers with a loop is slow and wordy. NumPy does the same work in one line and much faster. It is also the base that Pandas, Matplotlib and most machine-learning libraries are built on, so you will meet it everywhere in data work.",
 simple="A Python list is like a drawer where you can throw in a pen, a key and a coin. A NumPy array is like an egg tray: every cell holds the same kind of thing, in a fixed order. Because everything is the same, NumPy can handle the whole tray in one move instead of one egg at a time.",
 tech="An `ndarray` stores elements of one **dtype** in a single block of memory, and its maths runs in compiled C code. Operations such as `+`, `*` and `>` are **vectorised**: they apply to every element at once, with no Python loop. The size of an array is fixed when it is created.",
 steps=["Install NumPy once with `pip`.", "Import it with the usual alias `np`.", "Turn a list into an array with `np.array()`.", "Use operators on the whole array: `arr * 2`, `arr + 10`.", "Check `arr.dtype` to see which type NumPy chose."],
 blocks=[
  dict(title="Install and import", plain=True, noRun=True, code='''pip install numpy      # run once, in your terminal

import numpy as np     # at the top of every script''',
   lines=[("pip install numpy", "Downloads NumPy from PyPI. Run it in your terminal one time, not inside a Python file."),
          ("import numpy as np", "Loads the library. `np` is the short name used everywhere, so your code looks familiar to other developers.")]),
  dict(title="Your first array", code=r'''import numpy as np

marks = np.array([72, 85, 90, 64])
print(marks)
print(type(marks))
print(marks.dtype)''', output=AUTO,
   lines=[("marks = np.array([72, 85, 90, 64])", "Converts a normal list into a NumPy array."),
          ("print(marks)", "Arrays print without commas, which is a quick way to tell them apart from lists."),
          ("print(type(marks))", "Shows `numpy.ndarray`, the array class."),
          ("print(marks.dtype)", "Shows the type NumPy chose for the values. Whole numbers become an integer type.")]),
  dict(title="List vs array: same symbol, different job", code=r'''import numpy as np

as_list = [1, 2, 3]
as_array = np.array([1, 2, 3])

print(as_list * 2)
print(as_array * 2)
print(as_array + 10)
print(as_array * as_array)''', output=AUTO,
   lines=[("as_list * 2", "For a list, `*` means *repeat the list*, so you get six items."),
          ("as_array * 2", "For an array, `*` means *multiply every number*."),
          ("as_array + 10", "Adds 10 to each element, with no loop."),
          ("as_array * as_array", "Two arrays of the same size are combined position by position: 1*1, 2*2, 3*3.")]),
  dict(title="One type for the whole array", code=r'''import numpy as np

a = np.array([1, 2, 3])
b = np.array([1, 2.5, 3])
c = np.array([1, 2, 'x'])

print(a.dtype)
print(b.dtype)
print(c.dtype)
print(b)''', output=AUTO,
   lines=[("a = np.array([1, 2, 3])", "All whole numbers, so the array holds integers."),
          ("b = np.array([1, 2.5, 3])", "One decimal number is enough to turn the entire array into decimals. The `1` becomes `1.0`."),
          ("c = np.array([1, 2, 'x'])", "Adding a piece of text turns everything into text, which stops you doing maths on it. The dtype `<U21` means *text of up to 21 characters*.")]),
 ],
 mistakes=["Expecting a list's behaviour: `arr * 2` multiplies the numbers, it does not repeat the array.",
           "Mixing text into a numeric array. NumPy quietly converts every value to text and your maths stops working.",
           "Trying to add an item with `append` like on a list. Arrays have a fixed size; you build a new array instead.",
           "Writing `import numpy` and then using `np.array`. If you drop `as np`, the name `np` does not exist."],
 use="Use NumPy whenever you have many numbers to process together: marks, sensor readings, prices, pixels of an image, or the input to a data-science model.",
 qa=[("What is NumPy?", "A Python library for fast numerical work. Its core object is `ndarray`, a fixed-size grid of values that all share one dtype."),
     ("Why is NumPy faster than a list?", "The values sit together in one block of memory and the maths runs in compiled C code over the whole array, so there is no slow Python loop."),
     ("What does `arr * 2` do compared with `my_list * 2`?", "On an array it doubles every number. On a list it repeats the list twice."),
     ("What happens if you mix integers and decimals in one array?", "NumPy upcasts everything to one common type, so the integers become floats.")],
 tryit=dict(task="Make an array from `[5, 10, 15]`. Multiply it by 2, add 1 to the result, and print the final array.",
            hint="Use `np.array([...])`, then do the maths on the array directly: `arr * 2 + 1`.",
            solution=r'''import numpy as np

arr = np.array([5, 10, 15])
print(arr * 2 + 1)''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 2
add(id="numpy-create-arrays", section=7, lib="numpy", title="Create arrays: zeros, ones, arange, linspace", time="9 min",
 summary="Build arrays without typing every number: starter grids, number ranges and evenly spaced points.",
 what="NumPy has ready-made functions that **create arrays for you**: grids full of zeros or ones, a range of numbers, or evenly spaced points between two values.",
 why="Typing a hundred numbers by hand is silly. You usually need an empty grid to fill later, a counter from 0 to 99, or 50 points along an axis for a graph. These functions give you that in one line.",
 simple="Think of buying ready-made stationery. `zeros` is a blank notebook, `ones` is a notebook with a 1 on every line, `arange` is a numbered ticket roll, and `linspace` is a ruler with marks at equal gaps.",
 tech="`np.zeros(shape)`, `np.ones(shape)` and `np.full(shape, value)` take a **shape**. `np.arange(start, stop, step)` works like `range()` but returns an array and allows decimal steps. `np.linspace(start, stop, count)` returns exactly `count` points and **includes** the end value.",
 steps=["For a 1-D array, pass a single number as the shape: `np.zeros(4)`.", "For a table, pass a tuple: `np.zeros((2, 3))` means 2 rows, 3 columns.", "Use `arange` when you know the step size.", "Use `linspace` when you know how many points you want.", "Use `np.eye(n)` for an n by n identity grid."],
 blocks=[
  dict(title="Grids filled with a value", code=r'''import numpy as np

print(np.zeros(4))
print(np.ones((2, 3)))
print(np.full((2, 2), 7))
print(np.eye(3))''', output=AUTO,
   lines=[("np.zeros(4)", "Four zeros in a row. NumPy makes them decimals (`0.`) unless you ask for another type."),
          ("np.ones((2, 3))", "A grid with 2 rows and 3 columns, all ones. The shape goes inside its own brackets, as a tuple."),
          ("np.full((2, 2), 7)", "A 2 by 2 grid where every cell is 7."),
          ("np.eye(3)", "A 3 by 3 identity grid: ones on the diagonal and zeros elsewhere. Used a lot in linear algebra.")]),
  dict(title="Number ranges with arange", code=r'''import numpy as np

print(np.arange(5))
print(np.arange(2, 11, 2))
print(np.arange(0, 1, 0.25))
print(np.arange(10, 0, -3))''', output=AUTO,
   lines=[("np.arange(5)", "Counts from 0 up to, but not including, 5."),
          ("np.arange(2, 11, 2)", "Starts at 2, stops before 11, steps by 2: the even numbers up to 10."),
          ("np.arange(0, 1, 0.25)", "Unlike `range()`, `arange` can step by decimals."),
          ("np.arange(10, 0, -3)", "A negative step counts downwards.")]),
  dict(title="Evenly spaced points with linspace", code=r'''import numpy as np

x = np.linspace(0, 1, 5)
print(x)
print(len(x))
print(np.linspace(10, 20, 3))''', output=AUTO,
   lines=[("np.linspace(0, 1, 5)", "Gives 5 points from 0 to 1, with equal gaps. The end value `1` is included."),
          ("len(x)", "You asked for 5 points, so you get exactly 5. This is the main difference from `arange`."),
          ("np.linspace(10, 20, 3)", "Three points between 10 and 20: the two ends and the middle.")]),
  dict(title="A table from nested lists", code=r'''import numpy as np

table = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(table)
print(table.shape)''', output=AUTO,
   lines=[("np.array([[1, 2, 3], [4, 5, 6]])", "A list of lists becomes a 2-D array. Each inner list is one row, and all rows must be the same length."),
          ("table.shape", "Shows `(2, 3)`: 2 rows and 3 columns.")]),
 ],
 mistakes=["Writing `np.zeros(2, 3)`. The shape must be one tuple: `np.zeros((2, 3))`.",
           "Forgetting that `arange(1, 5)` stops before 5, so 5 is not in the result.",
           "Using `arange` with decimal steps and expecting an exact length. Rounding can change the count, so use `linspace` when the number of points matters.",
           "Building a table from rows of different lengths. NumPy cannot make a proper grid from them."],
 use="Use `zeros` or `ones` to prepare a grid you will fill, `arange` for counters and index lists, and `linspace` for points along an axis, for example before plotting a curve.",
 qa=[("What is the difference between `arange` and `linspace`?", "`arange` is controlled by a step size and excludes the stop value. `linspace` is controlled by how many points you want and includes the end value."),
     ("How do you create a 3 by 4 array of zeros?", "`np.zeros((3, 4))`, with the shape given as a tuple."),
     ("What does `np.full((2, 2), 9)` return?", "A 2 by 2 array where every value is 9."),
     ("Why does `np.zeros(3)` print `0.` instead of `0`?", "The default dtype is float, so the zeros are decimal numbers. Pass `dtype=int` to get integers.")],
 tryit=dict(task="Create an array holding 10, 20, 30, ..., 100 using `arange`, then print it and print how many values it has.",
            hint="The stop value is exclusive, so use 101 as the stop and 10 as the step.",
            solution=r'''import numpy as np

nums = np.arange(10, 101, 10)
print(nums)
print(len(nums))''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 3
add(id="numpy-indexing-slicing", section=7, lib="numpy", title="Indexing and slicing arrays", time="11 min",
 summary="Pick out single values, rows, columns and blocks from an array, and learn why a slice is a view, not a copy.",
 what="**Indexing** picks one value from an array by its position. **Slicing** picks a range of values using `start:stop:step`. In a 2-D array you give one position (or range) per dimension, separated by a comma.",
 why="Almost every data task starts with *give me this row* or *give me the last column*. Clear indexing lets you grab exactly the data you need without loops.",
 simple="Picture a cinema seating chart. A single seat is `[row, seat]`. A whole row is `[row, :]`. A whole column of seats is `[:, seat]`. The colon means *all of them*.",
 tech="Indexing starts at 0 and negative numbers count from the end. For a 2-D array, `a[r, c]` selects one cell. A slice such as `a[1:3]` returns a **view** that shares memory with the original array, so changing the view changes the original unless you call `.copy()`.",
 steps=["Use `a[i]` for one item; the first item is `a[0]`.", "Use `a[-1]` for the last item.", "Use `a[start:stop:step]` for a range; `stop` is not included.", "In 2-D use `a[row, col]`; a colon `:` means *everything* in that direction.", "Call `.copy()` when you need a slice that is independent."],
 blocks=[
  dict(title="One-dimensional arrays", code=r'''import numpy as np

a = np.array([10, 20, 30, 40, 50, 60])
print(a[0])
print(a[-1])
print(a[1:4])
print(a[::2])
print(a[::-1])''', output=AUTO,
   lines=[("a[0]", "The first item, because counting starts at 0."),
          ("a[-1]", "The last item. `-1` means one from the end."),
          ("a[1:4]", "Items at positions 1, 2 and 3. Position 4 is the stop, so it is excluded."),
          ("a[::2]", "Every second item from start to end."),
          ("a[::-1]", "A negative step walks backwards, so this reverses the array.")]),
  dict(title="Two-dimensional arrays", code=r'''import numpy as np

m = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print(m[1, 2])
print(m[0])
print(m[:, 1])
print(m[0:2, 1:3])
print(m[-1, -1])''', output=AUTO,
   lines=[("m[1, 2]", "Row 1, column 2: the value 7."),
          ("m[0]", "With only one position you get the whole first row."),
          ("m[:, 1]", "All rows, column 1: the second column."),
          ("m[0:2, 1:3]", "Rows 0 and 1, columns 1 and 2: a 2 by 2 block from the top middle."),
          ("m[-1, -1]", "The bottom-right corner.")]),
  dict(title="Changing values, and views versus copies", code=r'''import numpy as np

a = np.array([1, 2, 3, 4, 5])

a[0] = 100
print(a)

part = a[1:4]
part[0] = 999
print(a)

safe = a[1:4].copy()
safe[0] = -1
print(a)
print(safe)''', output=AUTO,
   lines=[("a[0] = 100", "Assigning to an index changes that value in place."),
          ("part = a[1:4]", "A slice does not copy the data. `part` is a window onto the same memory as `a`."),
          ("part[0] = 999", "Changing the window changes the original array too, as the second print shows."),
          ("a[1:4].copy()", "`.copy()` makes independent data, so changing `safe` leaves `a` untouched.")]),
 ],
 mistakes=["Expecting a slice to be a separate copy. Edits made through a slice also change the original array.",
           "Forgetting that the stop index is excluded, so `a[1:4]` has three items, not four.",
           "Using `m[0][1]` out of habit from lists. It works, but `m[0, 1]` is clearer and faster for arrays.",
           "Going outside the array: `a[10]` on a six-item array raises an `IndexError`."],
 use="Use indexing and slicing to pull rows, columns or blocks out of data: the first three students, the last column of results, or one corner of an image.",
 qa=[("What does `a[:, 2]` return for a 2-D array?", "Every row of column 2, in other words the third column."),
     ("Is a NumPy slice a copy or a view?", "A view. It shares memory with the original array, so edits show up in both. Use `.copy()` to get independent data."),
     ("How do you reverse a 1-D array?", "`a[::-1]`."),
     ("What is the difference between `m[0]` and `m[:, 0]`?", "`m[0]` is the first row. `m[:, 0]` is the first column.")],
 tryit=dict(task="Given the 3 by 3 array below, print its middle row and then its last column.\n`g = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`",
            hint="The middle row is `g[1]`. For the last column use a colon for all rows and `-1` for the column: `g[:, -1]`.",
            solution=r'''import numpy as np

g = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(g[1])
print(g[:, -1])''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 4
add(id="numpy-shape-reshape", section=7, lib="numpy", title="Shape, reshape and transpose", time="10 min",
 summary="Read the shape of an array and re-arrange the same numbers into rows and columns without changing the data.",
 what="The **shape** of an array tells you how many items it has in each direction, for example `(3, 4)` means 3 rows and 4 columns. **Reshaping** rearranges the same numbers into a different shape.",
 why="Data often arrives in the wrong layout: a long flat list that should be a table, or rows that should be columns. Machine-learning code is also very strict about shapes. Knowing how to read and change them avoids the most common NumPy errors.",
 simple="Imagine twelve chairs. You can set them in one long line, in 3 rows of 4, or in 4 rows of 3. The chairs never change, only how you arrange them. That is reshaping.",
 tech="`arr.shape` is a tuple of dimension sizes, `arr.ndim` is the number of dimensions and `arr.size` is the total item count. `reshape` returns an array with the same items in a new shape; the product of the new shape must equal `size`. Passing `-1` for one dimension lets NumPy work it out. `.T` swaps rows and columns.",
 steps=["Check `arr.shape` first, whenever something looks wrong.", "Make sure the new shape multiplies out to the same total.", "Use `-1` for the one dimension you want NumPy to calculate.", "Use `.T` to flip rows and columns.", "Use `ravel()` to flatten everything back into one row."],
 blocks=[
  dict(title="Reading the shape", code=r'''import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.shape)
print(a.ndim)
print(a.size)''', output=AUTO,
   lines=[("a.shape", "A tuple: 2 rows, 3 columns."),
          ("a.ndim", "The number of dimensions. A table has 2."),
          ("a.size", "The total number of items: 2 * 3 = 6.")]),
  dict(title="Reshape", code=r'''import numpy as np

flat = np.arange(12)
print(flat)

print(flat.reshape(3, 4))
print(flat.reshape(4, 3))
print(flat.reshape(2, -1))''', output=AUTO,
   lines=[("flat = np.arange(12)", "Twelve numbers in one flat row, 0 to 11."),
          ("flat.reshape(3, 4)", "The same twelve numbers laid out as 3 rows of 4. `flat` itself is unchanged."),
          ("flat.reshape(4, 3)", "Another valid layout: 4 rows of 3."),
          ("flat.reshape(2, -1)", "You asked for 2 rows. NumPy sees that 12 / 2 = 6 and fills in the `-1` with 6 columns.")]),
  dict(title="Transpose and flatten", code=r'''import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.T)
print(a.T.shape)
print(a.ravel())''', output=AUTO,
   lines=[("a.T", "Transpose: rows become columns and columns become rows."),
          ("a.T.shape", "The shape flips from `(2, 3)` to `(3, 2)`."),
          ("a.ravel()", "Flattens the array into one dimension, reading row by row.")]),
  dict(title="When the numbers do not fit", code=r'''import numpy as np

flat = np.arange(12)
try:
    flat.reshape(5, 3)
except ValueError as e:
    print("Error:", e)''', output=AUTO,
   lines=[("flat.reshape(5, 3)", "5 * 3 = 15, but the array only has 12 items, so NumPy refuses."),
          ("except ValueError as e", "Reshape problems raise a `ValueError`. Here we catch it and print the message, which says exactly what did not fit.")]),
 ],
 mistakes=["Asking for a shape whose total differs from `size`. Always check `rows * columns == size`.",
           "Using more than one `-1` in a reshape. NumPy can only work out one unknown.",
           "Thinking `reshape` changes the original array. It returns a new view; assign it to a variable to keep it.",
           "Confusing `(3,)` and `(3, 1)`. The first is a flat list of 3, the second is a column with 3 rows, and they behave differently in maths."],
 use="Use `reshape` to turn flat data into a table (or the reverse), and `.T` when your data has rows and columns the wrong way round for a function.",
 qa=[("What does `shape` return?", "A tuple with the size of each dimension, for example `(3, 4)`."),
     ("What does `reshape(2, -1)` mean?", "Make 2 rows and let NumPy calculate the number of columns from the total size."),
     ("What is the difference between `reshape` and `resize`?", "`reshape` keeps the same items and requires the total to match. `resize` can change the total size by repeating or cutting values."),
     ("What does `.T` do?", "It transposes an array: rows become columns and columns become rows.")],
 tryit=dict(task="Create the numbers 1 to 6 with `arange`, reshape them into 2 rows and 3 columns, and print the array and its transpose.",
            hint="`np.arange(1, 7)` gives 1 to 6. Then `.reshape(2, 3)`, and `.T` for the transpose.",
            solution=r'''import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print(a)
print(a.T)''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 5
add(id="numpy-math-aggregates", section=7, lib="numpy", title="Array maths and summaries: sum, mean, max, axis", time="11 min",
 summary="Do maths on a whole array at once, then summarise it by overall, by column and by row.",
 what="NumPy lets you do arithmetic on entire arrays (**vectorised maths**) and summarise them with functions like `sum()`, `mean()`, `max()` and `std()`. A summary can cover the whole array or run along one **axis**.",
 why="Questions like *what is the class average?* or *which test was hardest?* are everyday data work. NumPy answers them without a single loop, and the axis idea carries straight over to Pandas.",
 simple="You have a marks sheet: one row per student, one column per test. The average of a column tells you how hard that test was. The average of a row tells you how one student did overall. The axis just says *down the columns* or *across the rows*.",
 tech="Operators work element by element. Aggregation methods collapse an array: with no `axis` they return one number; `axis=0` collapses the **rows** (one result per column); `axis=1` collapses the **columns** (one result per row). `argmax` and `argmin` return the **position** of the largest and smallest values.",
 steps=["Use operators and functions like `+`, `**2` and `np.sqrt` on whole arrays.", "Call `sum`, `mean`, `min`, `max`, `std` for a quick summary.", "Add `axis=0` for results per column.", "Add `axis=1` for results per row.", "Use `argmax` to find where the biggest value sits."],
 blocks=[
  dict(title="Maths on whole arrays", code=r'''import numpy as np

prices = np.array([100, 250, 80])
qty = np.array([2, 1, 5])

print(prices * qty)
print(prices * 1.18)
print(prices ** 2)
print(np.sqrt(np.array([4, 9, 16])))''', output=AUTO,
   lines=[("prices * qty", "Multiplies position by position: 100*2, 250*1, 80*5. This is the line total of each item."),
          ("prices * 1.18", "A single number is applied to every element, for example adding 18% tax."),
          ("prices ** 2", "Squares every price."),
          ("np.sqrt(...)", "NumPy functions such as `sqrt` also work on each element.")]),
  dict(title="Summaries of one array", code=r'''import numpy as np

marks = np.array([72, 85, 90, 64, 78])

print(marks.sum())
print(marks.mean())
print(marks.max(), marks.min())
print(round(marks.std(), 2))
print(np.median(marks))
print(marks.argmax())''', output=AUTO,
   lines=[("marks.sum()", "Total of all values."),
          ("marks.mean()", "The average."),
          ("marks.max(), marks.min()", "Highest and lowest values."),
          ("round(marks.std(), 2)", "Standard deviation: how spread out the marks are. Rounded to two decimals to keep it tidy."),
          ("np.median(marks)", "The middle value after sorting."),
          ("marks.argmax()", "The **position** of the highest mark, not the mark itself. Position 2 holds 90.")]),
  dict(title="Rows, columns and axis", code=r'''import numpy as np

# rows = students, columns = tests
scores = np.array([[70, 80, 90],
                   [60, 75, 65],
                   [88, 92, 79]])

print(scores.mean())
print(scores.mean(axis=0))
print(scores.mean(axis=1))
print(scores.max(axis=0))
print(scores.cumsum(axis=1))''', output=AUTO,
   lines=[("scores.mean()", "No axis: the average of all nine numbers."),
          ("scores.mean(axis=0)", "`axis=0` runs down the rows, giving one average **per column** (per test)."),
          ("scores.mean(axis=1)", "`axis=1` runs across the columns, giving one average **per row** (per student)."),
          ("scores.max(axis=0)", "The best score in each test."),
          ("scores.cumsum(axis=1)", "Running total along each row, so you see each student's marks adding up.")]),
 ],
 mistakes=["Mixing up the axes. Remember: `axis=0` gives one answer per column, `axis=1` gives one answer per row.",
           "Reading `argmax()` as the biggest value. It returns the index of the biggest value.",
           "Using Python's built-in `sum()` on a 2-D array. It adds the rows together and returns an array of column totals, not one number. Use `arr.sum()` or `np.sum(arr)` instead.",
           "Combining arrays of different lengths, for example 3 prices with 4 quantities, which raises a `ValueError`."],
 use="Use array maths and aggregates for totals, averages, spread and best/worst values on any numeric data, and `axis` whenever your data is a table.",
 qa=[("What does `axis=0` mean in `arr.sum(axis=0)`?", "The sum runs down the rows, so you get one result for each column."),
     ("What is the difference between `max()` and `argmax()`?", "`max()` returns the largest value. `argmax()` returns the position of that value."),
     ("What does vectorised mean?", "An operation is applied to every element of the array at once, without writing a Python loop."),
     ("How do you get the average of each row in a 2-D array?", "`arr.mean(axis=1)`.")],
 tryit=dict(task="For `s = np.array([[10, 20], [30, 40], [50, 60]])` print the sum of each column and then the mean of each row.",
            hint="Columns use `axis=0` and rows use `axis=1`: `s.sum(axis=0)` and `s.mean(axis=1)`.",
            solution=r'''import numpy as np

s = np.array([[10, 20], [30, 40], [50, 60]])
print(s.sum(axis=0))
print(s.mean(axis=1))''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 6
add(id="numpy-broadcasting", section=7, lib="numpy", title="Broadcasting: maths between different shapes", time="10 min",
 summary="See how NumPy combines arrays of different shapes, such as a table plus a single row, without copying data.",
 what="**Broadcasting** is NumPy's rule for doing maths between arrays of *different* shapes. A smaller array is stretched, in effect, to match the bigger one.",
 why="You constantly need things like *add 5 bonus marks to every student* or *subtract each column's average*. Broadcasting lets you write that directly instead of building big repeated arrays or looping. It is also behind many mysterious shape errors, so it is worth understanding.",
 simple="You have a table of marks and one extra row of bonus marks, one bonus per subject. Broadcasting is like photocopying that single bonus row down the page so each student's row gets the same bonus added, but without really making the copies.",
 tech="NumPy compares the two shapes from the **last dimension backwards**. Two dimensions are compatible when they are **equal** or one of them is **1**. A dimension of size 1 is stretched to match the other. If any pair is incompatible, NumPy raises a `ValueError`.",
 steps=["Write out both shapes, lined up from the right.", "For each pair, check: are they equal, or is one of them 1?", "If every pair passes, the smaller array is stretched to fit.", "If one pair fails, you get a shape error.", "Fix it with `reshape`, or by adding a dimension with `[:, np.newaxis]`."],
 blocks=[
  dict(title="A single number against an array", code=r'''import numpy as np

marks = np.array([[60, 70],
                  [80, 90]])
print(marks + 5)
print(marks * 2)''', output=AUTO,
   lines=[("marks + 5", "A single number has no dimensions, so it is stretched to every cell."),
          ("marks * 2", "The same idea works for any operator.")]),
  dict(title="A table plus one row", code=r'''import numpy as np

marks = np.array([[60, 70, 80],
                  [50, 65, 75]])   # shape (2, 3)
bonus = np.array([5, 0, 10])      # shape (3,)

print(marks.shape, bonus.shape)
print(marks + bonus)''', output=AUTO,
   lines=[("marks ... shape (2, 3)", "Two students, three subjects."),
          ("bonus ... shape (3,)", "One bonus per subject."),
          ("marks + bonus", "Lining the shapes up from the right: 3 and 3 match, and the missing first dimension of `bonus` is stretched across both rows. Every student gets the same per-subject bonus.")]),
  dict(title="A column against a row", code=r'''import numpy as np

rows = np.array([[1], [2], [3]])    # shape (3, 1)
cols = np.array([10, 20, 30, 40])   # shape (4,)

print(rows + cols)
print((rows + cols).shape)''', output=AUTO,
   lines=[("rows ... shape (3, 1)", "A column with three rows."),
          ("cols ... shape (4,)", "A single row of four values."),
          ("rows + cols", "The `1` in the first shape stretches to 4 and the missing dimension in the second stretches to 3. The result is a 3 by 4 table of every row value added to every column value.")]),
  dict(title="When broadcasting fails", code=r'''import numpy as np

a = np.ones((2, 3))
b = np.ones((2,))

try:
    print(a + b)
except ValueError as e:
    print("Error:", e)

print(a + b[:, np.newaxis])''', output=AUTO,
   lines=[("a + b", "Shapes `(2, 3)` and `(2,)`: comparing from the right, 3 and 2 are neither equal nor 1, so NumPy refuses."),
          ("except ValueError as e", "Catches the error so we can print its message."),
          ("b[:, np.newaxis]", "Turns `b` into a column of shape `(2, 1)`. Now the pairs are 3 vs 1 and 2 vs 2, which is allowed, and the sum works.")]),
 ],
 mistakes=["Not checking `.shape` when you get a broadcasting error. Print both shapes first.",
           "Assuming `(3,)` is a column. It is a flat row; a column is `(3, 1)`.",
           "Relying on broadcasting silently when you meant two arrays to be the same shape; you can get a result with the wrong meaning and no error.",
           "Trying to broadcast shapes like `(2, 3)` and `(2,)`. Add a dimension with `np.newaxis` or `reshape(2, 1)`."],
 use="Use broadcasting to apply one value or one row/column of values to a whole table, for example scaling, adding bonuses, or subtracting each column's average.",
 qa=[("What is broadcasting in NumPy?", "The rule that lets NumPy do arithmetic on arrays of different shapes by stretching the smaller one to match the larger, without actually copying the data."),
     ("When are two shapes compatible for broadcasting?", "Compared from the last dimension backwards, each pair of sizes must be equal or one of them must be 1."),
     ("What does `np.newaxis` do?", "It adds a new dimension of size 1, for example turning a shape `(3,)` into `(3, 1)`."),
     ("Why does adding shapes `(2, 3)` and `(2,)` fail?", "Comparing from the right, 3 and 2 are different and neither is 1.")],
 tryit=dict(task="Subtract each column's average from the table `t = np.array([[2, 4], [4, 8], [6, 12]])` and print the result.",
            hint="`t.mean(axis=0)` is one average per column, shape `(2,)`. Subtract it from `t` directly.",
            solution=r'''import numpy as np

t = np.array([[2, 4], [4, 8], [6, 12]])
print(t - t.mean(axis=0))''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 7
add(id="numpy-filter-where", section=7, lib="numpy", title="Filter arrays with conditions and np.where", time="10 min",
 summary="Pick values that match a rule, count them, change them, and label them with np.where.",
 what="A **boolean mask** is an array of True/False values made by a comparison such as `marks > 50`. Using it inside `[]` keeps only the matching values. `np.where()` is a one-line *if-else* for a whole array.",
 why="Real questions have conditions: *who passed?*, *which readings are too high?*, *give grace marks to anyone below 40*. Masks answer all of these without loops.",
 simple="Imagine holding a sieve over a bowl of marks. The condition `> 50` is the sieve. Everything that passes through is kept, everything else stays behind. The True/False list is just a record of which marks passed the sieve.",
 tech="A comparison on an array returns a boolean array of the same shape. `arr[mask]` returns only the elements where the mask is True (as a new 1-D array). Combine conditions with `&` (and), `|` (or) and `~` (not), **each condition in its own brackets**. `np.where(cond, a, b)` picks from `a` where the condition is True and from `b` otherwise.",
 steps=["Write a comparison: `marks >= 40`.", "Use it as a mask: `marks[marks >= 40]`.", "Combine rules with `&`, `|`, `~` and brackets.", "Count matches with `mask.sum()`, since True counts as 1.", "Use `np.where` to choose between two values for every element."],
 blocks=[
  dict(title="Masks and filtering", code=r'''import numpy as np

marks = np.array([35, 82, 47, 91, 28, 66])

mask = marks >= 40
print(mask)
print(marks[mask])
print(marks[marks > 80])
print(mask.sum())''', output=AUTO,
   lines=[("mask = marks >= 40", "A True/False value for every mark."),
          ("marks[mask]", "Keeps only the marks where the mask is True."),
          ("marks[marks > 80]", "You can skip the variable and put the condition straight inside the brackets."),
          ("mask.sum()", "True counts as 1 and False as 0, so the sum is how many students passed.")]),
  dict(title="Combining conditions", code=r'''import numpy as np

marks = np.array([35, 82, 47, 91, 28, 66])

print(marks[(marks >= 40) & (marks < 80)])
print(marks[(marks < 30) | (marks > 90)])
print(marks[~(marks >= 40)])''', output=AUTO,
   lines=[("(marks >= 40) & (marks < 80)", "Both rules must be true. Use `&`, not the word `and`, and keep each rule in brackets."),
          ("(marks < 30) | (marks > 90)", "Either rule may be true. `|` means *or*."),
          ("~(marks >= 40)", "`~` flips True and False, so this keeps the marks that failed.")]),
  dict(title="np.where: label every value", code=r'''import numpy as np

marks = np.array([35, 82, 47, 91, 28, 66])

print(np.where(marks >= 40, 'Pass', 'Fail'))
print(np.where(marks >= 40, marks, 0))
print(np.where(marks < 40))''', output=AUTO,
   lines=[("np.where(marks >= 40, 'Pass', 'Fail')", "For each mark, give `'Pass'` where the condition is True and `'Fail'` where it is False."),
          ("np.where(marks >= 40, marks, 0)", "Keep the mark if it passed, otherwise use 0. The result has the same length as the input."),
          ("np.where(marks < 40)", "With only a condition, it returns the **positions** where the condition is True, wrapped in a tuple. Here, positions 0 and 4.")]),
  dict(title="Changing values with a mask", code=r'''import numpy as np

marks = np.array([35, 82, 47, 91, 28, 66])
marks[marks < 40] = 40
print(marks)

ids = np.array([10, 20, 30, 40, 50])
print(ids[[0, 2, 4]])''', output=AUTO,
   lines=[("marks[marks < 40] = 40", "Assigns 40 to every position the mask selects. A quick way to give minimum or grace marks."),
          ("ids[[0, 2, 4]]", "Passing a list of positions picks exactly those items, in that order. This is called fancy indexing.")]),
 ],
 mistakes=["Using `and` / `or` instead of `&` / `|`. Python's keywords fail on arrays with an *ambiguous truth value* error.",
           "Forgetting the brackets: `marks > 40 & marks < 80` is evaluated in the wrong order. Write `(marks > 40) & (marks < 80)`.",
           "Expecting `arr[mask]` to change `arr`. It returns a new array; assign to `arr[mask] = ...` to change the original.",
           "Forgetting that `np.where(condition)` with one argument gives positions, not values."],
 use="Use masks to filter, count or fix values that meet a rule, and `np.where` when every element needs one of two outcomes, such as a Pass/Fail label or a cleaned value.",
 qa=[("How do you select all values greater than 50 from an array `a`?", "`a[a > 50]`."),
     ("Why do you need brackets around each condition when combining with `&`?", "`&` has higher priority than comparison operators, so without brackets Python evaluates the wrong parts first."),
     ("What does `np.where(cond, x, y)` do?", "It returns an array that takes values from `x` where `cond` is True and from `y` where it is False."),
     ("How can you count how many values match a condition?", "Sum the mask: `(a > 50).sum()`, because True counts as 1.")],
 tryit=dict(task="For `temps = np.array([22, 35, 18, 41, 30])`, print how many readings are above 30, and print the array with every reading above 30 replaced by 30.",
            hint="Count with `(temps > 30).sum()`. For the cap use `np.where(temps > 30, 30, temps)`.",
            solution=r'''import numpy as np

temps = np.array([22, 35, 18, 41, 30])
print((temps > 30).sum())
print(np.where(temps > 30, 30, temps))''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 8
add(id="numpy-random", section=7, lib="numpy", title="Random numbers and simulations", time="9 min",
 summary="Generate random numbers the modern way, make them repeatable with a seed, and run a small dice simulation.",
 what="NumPy can generate **random numbers** in bulk. You create a random **generator** with `np.random.default_rng()`, then ask it for integers, decimals, or random picks from a list.",
 why="Random numbers are used to test ideas without real data, to shuffle data, to split data into training and test sets, and to simulate things like dice or coin tosses to see what usually happens.",
 simple="Think of a dice-rolling machine. You tell it how many dice to roll and it hands you all the results at once. A **seed** is like setting the machine to the same starting position every time, so it rolls the same sequence and your experiment can be repeated.",
 tech="`rng = np.random.default_rng(seed)` creates a generator. `rng.integers(low, high, size)` gives integers from `low` up to **but not including** `high`. `rng.random(size)` gives decimals from 0 up to 1. `rng.choice(items, size)` picks from a list. The same seed gives the same numbers, but the exact values can differ between NumPy versions, so rely on shapes and ranges, not specific numbers.",
 steps=["Create a generator: `rng = np.random.default_rng(42)`.", "Ask for numbers with `rng.integers`, `rng.random` or `rng.choice`.", "Pass `size` to get many values at once.", "Use the same seed whenever you need a repeatable result.", "Check the shape, min and max of the result to confirm it looks right."],
 blocks=[
  dict(title="A generator with a seed", code=r'''import numpy as np

rng = np.random.default_rng(42)
print(rng.integers(1, 7, size=5))
print(rng.random(3))

rng2 = np.random.default_rng(42)
print(rng2.integers(1, 7, size=5))''', output=AUTO,
   lines=[("np.random.default_rng(42)", "Creates a random generator. `42` is the seed, any number will do."),
          ("rng.integers(1, 7, size=5)", "Five dice rolls. The top value 7 is excluded, so you get 1 to 6."),
          ("rng.random(3)", "Three random decimals between 0 and 1."),
          ("np.random.default_rng(42) again", "A new generator with the same seed starts from the same point, so it gives the same dice rolls as the first one. The exact numbers can differ on another NumPy version.")]),
  dict(title="Random picks and shuffling", code=r'''import numpy as np

rng = np.random.default_rng(7)
names = np.array(['Asha', 'Ravi', 'Meena', 'Kabir', 'Isha'])

print(len(rng.choice(names, size=2, replace=False)))
shuffled = rng.permutation(names)
print(len(shuffled), sorted(shuffled) == sorted(names))''', output=AUTO,
   lines=[("rng.choice(names, size=2, replace=False)", "Picks 2 different names. `replace=False` means a name cannot be picked twice."),
          ("rng.permutation(names)", "Returns a shuffled copy and leaves the original alone."),
          ("sorted(shuffled) == sorted(names)", "Shuffling only reorders: the same names are still there, so this prints True.")]),
  dict(title="Simulate 1,000 dice rolls", code=r'''import numpy as np

rng = np.random.default_rng(1)
rolls = rng.integers(1, 7, size=1000)

print(rolls.shape)
print(rolls.min(), rolls.max())
print(3.3 < rolls.mean() < 3.7)
print(np.bincount(rolls)[1:].sum())''', output=AUTO,
   lines=[("rng.integers(1, 7, size=1000)", "A thousand rolls of one die in a single line."),
          ("rolls.min(), rolls.max()", "Always 1 and 6 here, a good sanity check on the range."),
          ("3.3 < rolls.mean() < 3.7", "A fair die averages 3.5, and 1,000 rolls land close to that, so this is True."),
          ("np.bincount(rolls)[1:].sum()", "`bincount` counts how many times each number appears. Slicing from 1 drops the unused zero slot, and the counts add back up to 1000.")]),
 ],
 mistakes=["Writing `rng.integers(1, 6)` and expecting a 6 to appear. The upper limit is excluded; use 7 for a six-sided die.",
           "Expecting a different answer on each run while using a fixed seed. A seed makes results repeat on purpose.",
           "Leaving out the seed in tests or tutorials, so nobody can reproduce your numbers.",
           "Printing results and comparing exact numbers across machines. Check shapes, ranges and averages instead."],
 use="Use random numbers to create practice data, shuffle or sample a list, split data into train and test parts, and simulate games or experiments.",
 qa=[("What is a random seed?", "A starting value for the generator. The same seed always produces the same sequence, which makes experiments repeatable."),
     ("What range does `rng.integers(1, 7)` return?", "Whole numbers from 1 to 6. The upper limit is exclusive."),
     ("How do you pick items without repeats?", "`rng.choice(items, size=n, replace=False)`."),
     ("Why is `default_rng` preferred over `np.random.seed`?", "`default_rng` gives each generator its own state, which is cleaner, safer and the approach NumPy recommends for new code.")],
 tryit=dict(task="Using `np.random.default_rng(5)`, simulate 100 coin tosses where 0 is tails and 1 is heads. Print the shape of the result and whether every value is either 0 or 1.",
            hint="Use `rng.integers(0, 2, size=100)`. Check with `np.isin(tosses, [0, 1]).all()`.",
            solution=r'''import numpy as np

rng = np.random.default_rng(5)
tosses = rng.integers(0, 2, size=100)
print(tosses.shape)
print(np.isin(tosses, [0, 1]).all())''', output=AUTO),
 related=[])
