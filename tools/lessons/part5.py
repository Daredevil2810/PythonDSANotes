# Section 8: Matplotlib for Charts (original lessons, own examples).
# plot=True blocks are run by build_lessons.py, which saves the chart as an image and shows it under the code.
# Outputs marked AUTO are filled in from a real run. Every block is self-contained so learners can copy any block alone.
from part1 import add
from part3 import AUTO

# ---------------------------------------------------------------- 1
add(id="matplotlib-first-plot", section=8, lib="matplotlib", title="Your first chart with Matplotlib", time="8 min",
 summary="Install Matplotlib, draw a line chart in three lines, and learn how x and y values turn into a picture.",
 what="**Matplotlib** is Python's most popular library for drawing charts. You use its `pyplot` module, normally imported as `plt`, to turn lists of numbers into line charts, bar charts, scatter plots and more.",
 why="Numbers in a table are hard to read. A chart shows a trend, a spike or a pattern in a second. Matplotlib is also the engine behind many other tools (Pandas plotting, Seaborn), so learning it first makes the rest easier.",
 simple="Think of graph paper. You give Matplotlib the positions along the bottom (the x values) and the heights (the y values). It puts a dot at every pair and joins the dots with a line.",
 tech="`plt.plot(x, y)` creates a line plot for the current figure and `plt.show()` displays it. The x and y sequences must have the same length. If you pass only one sequence, Matplotlib treats it as the y values and uses `0, 1, 2, ...` for x.",
 steps=["Install Matplotlib once with `pip`.", "Import `matplotlib.pyplot` as `plt`.", "Call `plt.plot(x, y)` with two lists of the same length.", "Call `plt.show()` to display the chart.", "Pass a third argument such as `'o'` to draw dots only."],
 blocks=[
  dict(title="Install and import", plain=True, noRun=True, code='''pip install matplotlib      # run once, in your terminal

import matplotlib.pyplot as plt   # at the top of every script''',
   lines=[("pip install matplotlib", "Downloads Matplotlib from PyPI. Run it in your terminal one time, not inside a Python file."),
          ("import matplotlib.pyplot as plt", "Loads the plotting module. `plt` is the short name everyone uses.")]),
  dict(title="A line chart in three lines", plot=True, alt="Line chart of steps in thousands for days 1 to 7, rising from 4 to 10 with small dips.", code=r'''import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
steps = [4, 6, 5, 8, 7, 9, 10]

plt.plot(days, steps)
plt.show()''', output=AUTO,
   lines=[("days = [1, 2, 3, 4, 5, 6, 7]", "The x values, placed along the bottom of the chart."),
          ("steps = [4, 6, 5, 8, 7, 9, 10]", "The y values, the height at each x. There must be exactly as many as x values."),
          ("plt.plot(days, steps)", "Prepares a line through the points (1, 4), (2, 6), (3, 5) and so on."),
          ("plt.show()", "Displays the chart. Nothing appears on screen until you call this.")]),
  dict(title="Only y values: x is filled in for you", plot=True, alt="Line chart of four values with x positions 0, 1, 2 and 3 added automatically.", code=r'''import matplotlib.pyplot as plt

plt.plot([3, 8, 5, 10])
plt.show()''', output=AUTO,
   lines=[("plt.plot([3, 8, 5, 10])", "With one list, Matplotlib treats it as the y values and uses the positions 0, 1, 2, 3 for x. That is why the x axis starts at 0."),
          ("plt.show()", "Draws the chart.")]),
  dict(title="Dots instead of a line", plot=True, alt="Scatter of five blue dots without any connecting line.", code=r'''import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 7, 6]

plt.plot(x, y, 'o')
plt.show()''', output=AUTO,
   lines=[("plt.plot(x, y, 'o')", "The third argument is a format string. `'o'` means *draw a round marker at every point and no line*."),
          ("plt.show()", "Displays the dots.")]),
 ],
 mistakes=["Giving x and y lists of different lengths. Matplotlib raises a `ValueError` about shapes.",
           "Forgetting `plt.show()` in a script. The code runs but no window appears.",
           "Naming your own file `matplotlib.py` or `pyplot.py`. Python then imports your file instead of the library and everything breaks.",
           "Expecting the x axis to start at 1 when you pass only y values. It starts at 0."],
 use="Use a line chart when order matters, for example values over time: daily steps, monthly sales, temperature across a week.",
 qa=[("What is Matplotlib?", "A Python library for creating static charts. Its `pyplot` module gives a simple, MATLAB-like way to draw them."),
     ("What does `plt.plot(y)` do when you give only one list?", "It uses the list as the y values and sets x to 0, 1, 2, and so on."),
     ("What does `plt.show()` do?", "It displays the figure you have prepared. Without it, a script will not open the chart."),
     ("What does the format string `'o'` mean?", "Draw circle markers only, with no connecting line.")],
 tryit=dict(task="Plot the squares of the numbers 1 to 5. Use `[1, 2, 3, 4, 5]` for x and the squares for y.",
            hint="The y values are 1, 4, 9, 16 and 25. Pass x first and y second to `plt.plot`, then call `plt.show()`.",
            plot=True, alt="Line chart curving upward through the points for the squares 1, 4, 9, 16 and 25.",
            solution=r'''import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.show()''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 2
add(id="matplotlib-labels-titles", section=8, lib="matplotlib", title="Titles, labels, legends and grids", time="9 min",
 summary="Turn a bare chart into one that explains itself, with a title, axis labels, a legend and a grid.",
 what="A chart without labels is a puzzle. Matplotlib lets you add a **title**, **axis labels**, a **legend** (a key that names each line) and a **grid** with one function call each.",
 why="People often see your chart without you there to explain it, for example in a report or a LinkedIn post. Labels say what is measured and in which units, so the picture can be understood on its own.",
 simple="Think of a map without a legend. You see colours and lines but cannot tell what they mean. Titles, labels and a legend are the key that makes the map readable.",
 tech="`plt.title()`, `plt.xlabel()` and `plt.ylabel()` set the text. To get a legend, give each plot call a `label='...'` and then call `plt.legend()`. `plt.grid(True)` adds grid lines. Several `plt.plot()` calls before one `plt.show()` draw on the same chart.",
 steps=["Draw your data with `plt.plot(...)`.", "Add `plt.title('...')` for the overall message.", "Add `plt.xlabel()` and `plt.ylabel()`, including units.", "Give each line `label='...'` and call `plt.legend()`.", "Add `plt.grid(True)` if it helps people read values."],
 blocks=[
  dict(title="Title and axis labels", plot=True, alt="Line chart titled Daily steps with the x axis labelled Day and the y axis labelled Steps in thousands.", code=r'''import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
steps = [4, 6, 5, 8, 7, 9, 10]

plt.plot(days, steps)
plt.title('Daily steps')
plt.xlabel('Day')
plt.ylabel('Steps (thousands)')
plt.show()''', output=AUTO,
   lines=[("plt.title('Daily steps')", "Adds the title above the chart. Say what the chart shows."),
          ("plt.xlabel('Day')", "Names the horizontal axis."),
          ("plt.ylabel('Steps (thousands)')", "Names the vertical axis. Putting the unit in brackets saves guessing.")]),
  dict(title="Two lines, a legend and a grid", plot=True, alt="Two lines for this week and last week across seven days, with a legend in the corner and a light grid.", code=r'''import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
this_week = [4, 6, 5, 8, 7, 9, 10]
last_week = [3, 4, 6, 5, 6, 7, 8]

plt.plot(days, this_week, label='This week')
plt.plot(days, last_week, label='Last week')
plt.title('Steps compared')
plt.xlabel('Day')
plt.ylabel('Steps (thousands)')
plt.legend()
plt.grid(True)
plt.show()''', output=AUTO,
   lines=[("plt.plot(days, this_week, label='This week')", "Draws the first line and gives it a name for the legend."),
          ("plt.plot(days, last_week, label='Last week')", "A second `plot` call before `show()` draws on the same chart. Matplotlib picks a different colour automatically."),
          ("plt.legend()", "Builds the legend from the labels. It does nothing if no line has a label."),
          ("plt.grid(True)", "Adds grid lines that make it easier to read the values.")]),
  dict(title="Position and size", plot=True, alt="Chart with a larger title and the legend placed in the upper left corner.", code=r'''import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
a = [2, 4, 5, 8]
b = [1, 3, 6, 7]

plt.plot(x, a, label='Team A')
plt.plot(x, b, label='Team B')
plt.title('Points per round', fontsize=16)
plt.legend(loc='upper left')
plt.show()''', output=AUTO,
   lines=[("fontsize=16", "Makes the title text bigger. Most text functions accept `fontsize`."),
          ("plt.legend(loc='upper left')", "Moves the legend. Other places include `'lower right'` and `'center'`. The default `'best'` lets Matplotlib choose the emptiest corner.")]),
 ],
 mistakes=["Calling `plt.legend()` without giving any line a `label`. The legend is empty or missing.",
           "Leaving out units in the axis labels, so nobody knows if the numbers are minutes or kilometres.",
           "Putting `plt.show()` between the plot calls. After `show()` the chart is finished and later calls start a new one.",
           "Using a vague title such as `Graph`. Say what the chart tells the reader."],
 use="Use titles and labels on every chart you share. Use a legend whenever more than one line or colour appears, and a grid when readers need to read off approximate values.",
 qa=[("How do you add a legend to a Matplotlib plot?", "Pass `label='...'` to each plot call and then call `plt.legend()`."),
     ("How do you draw two lines on one chart?", "Call `plt.plot()` twice before calling `plt.show()`."),
     ("How do you move the legend?", "Use the `loc` argument, for example `plt.legend(loc='upper left')`."),
     ("What are `plt.xlabel` and `plt.ylabel` for?", "They name the x axis and the y axis, ideally with units.")],
 tryit=dict(task="Plot `[10, 20, 15, 30]` against `[1, 2, 3, 4]`. Add the title `Sales`, the x label `Month` and the y label `Units`, and turn the grid on.",
            hint="Use `plt.title`, `plt.xlabel`, `plt.ylabel` and `plt.grid(True)` before `plt.show()`.",
            plot=True, alt="Line chart titled Sales with Month on the x axis, Units on the y axis and grid lines.",
            solution=r'''import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [10, 20, 15, 30])
plt.title('Sales')
plt.xlabel('Month')
plt.ylabel('Units')
plt.grid(True)
plt.show()''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 3
add(id="matplotlib-line-styles", section=8, lib="matplotlib", title="Markers, colours and line styles", time="9 min",
 summary="Change how a line looks: add markers, pick colours, switch to dashed lines and set the thickness.",
 what="You can control the look of every line: the **marker** drawn at each point, the **colour**, the **line style** (solid, dashed, dotted) and the **thickness**.",
 why="Styling is not decoration. When two lines are printed in black and white, or seen by colour-blind readers, different markers and dashes keep them apart. A few well-chosen styles also make important data stand out.",
 simple="Think of highlighting pens. You can choose a pen colour, a thick or thin tip and even draw dashes. Matplotlib has the same choices, only you name them in code.",
 tech="Style options can be given as keyword arguments (`marker`, `color`, `linestyle`, `linewidth`, `markersize`) or packed into a **format string** such as `'o--r'` (circle markers, dashed line, red) as the third argument of `plot`. Colours can be names (`'green'`), short codes (`'g'`) or hex codes (`'#ff7f0e'`).",
 steps=["Add `marker='o'` to show a dot at every data point.", "Choose a colour with `color='...'`.", "Choose a style with `linestyle='--'` or `':'`.", "Control thickness with `linewidth` and `markersize`.", "Use a format string like `'s:g'` as a shortcut."],
 table=dict(head=["Marker", "Shape", "Line style", "Look", "Colour code", "Colour"],
            rows=[["'o'", "Circle", "'-'", "Solid line", "'r'", "Red"],
                  ["'s'", "Square", "'--'", "Dashed line", "'g'", "Green"],
                  ["'^'", "Triangle up", "':'", "Dotted line", "'b'", "Blue"],
                  ["'*'", "Star", "'-.'", "Dash and dot", "'k'", "Black"]]),
 blocks=[
  dict(title="Markers and line style with keywords", plot=True, alt="Line chart with square markers at each point drawn as a dashed green line.", code=r'''import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 5, 4, 8, 7]

plt.plot(x, y, marker='s', linestyle='--', color='green')
plt.show()''', output=AUTO,
   lines=[("marker='s'", "Draws a square at each data point."),
          ("linestyle='--'", "Makes the connecting line dashed."),
          ("color='green'", "Sets the colour by name.")]),
  dict(title="Thickness, size and hex colours", plot=True, alt="Thick orange line with large circle markers on five points.", code=r'''import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 5, 4, 8, 7]

plt.plot(x, y, marker='o', markersize=10,
         linewidth=4, color='#ff7f0e')
plt.show()''', output=AUTO,
   lines=[("markersize=10", "Makes each marker larger."),
          ("linewidth=4", "Makes the line thicker."),
          ("color='#ff7f0e'", "A hex colour code. Any hex colour from a design tool works here.")]),
  dict(title="Shortcut format strings", plot=True, alt="Three lines drawn in different styles: red dashed with circles, green dotted with squares and blue solid with triangles.", code=r'''import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

plt.plot(x, [1, 2, 3, 4], 'o--r', label='Red dashed')
plt.plot(x, [2, 3, 4, 5], 's:g', label='Green dotted')
plt.plot(x, [3, 4, 5, 6], '^-b', label='Blue solid')
plt.legend()
plt.show()''', output=AUTO,
   lines=[("'o--r'", "Reads as marker `o`, line style `--`, colour `r`. The order is marker, line, colour."),
          ("'s:g'", "Square markers, dotted line, green."),
          ("'^-b'", "Triangle markers, solid line, blue."),
          ("plt.legend()", "The `label` on each line is used to build the legend.")]),
 ],
 mistakes=["Putting a colour code in the wrong place in a format string, for example `'ro--'` works but `'o--rx'` does not make sense.",
           "Using `plt.plot(x, y, 'o', linestyle='-')` and being surprised by the clash. Keyword arguments override the format string.",
           "Choosing colours that look alike. Combine colour with marker or line style so lines stay distinct in print.",
           "Misspelling a name such as `colour='red'`. Matplotlib uses the American spelling `color`."],
 use="Use markers when there are only a few points and each one matters. Use different line styles when charts will be printed in black and white. Keep decoration modest so the data stays the star.",
 qa=[("What does the format string `'o--r'` mean?", "Circle markers, a dashed line and red colour."),
     ("How do you make a line thicker?", "Use the `linewidth` argument, for example `linewidth=3`."),
     ("How can you give a colour in Matplotlib?", "By name (`'green'`), by a one-letter code (`'g'`) or by a hex code (`'#2ca02c'`)."),
     ("Why use different line styles as well as different colours?", "So the lines can still be told apart in black-and-white print or by readers who cannot distinguish the colours.")],
 tryit=dict(task="Plot `[2, 4, 3, 6]` against `[1, 2, 3, 4]` using star markers, a dotted line and the colour red. Use the format-string shortcut.",
            hint="Marker first, then line style, then colour: `'*:r'`.",
            plot=True, alt="Red dotted line with star markers through four points.",
            solution=r'''import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2, 4, 3, 6], '*:r')
plt.show()''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 4
add(id="matplotlib-bar-charts", section=8, lib="matplotlib", title="Bar charts: compare categories", time="9 min",
 summary="Draw vertical and horizontal bar charts, colour the bars and print the value on top of each one.",
 what="A **bar chart** shows one bar per category, and the bar's length shows the value. It is the standard way to compare things such as sales per city or marks per subject.",
 why="A line chart suggests that points are connected in order, which makes no sense for cities or subjects. Bars treat each category as a separate item and make the biggest and smallest obvious at a glance.",
 simple="Think of a row of glass tubes filled with water. Each tube is one category, and the water level is its value. You can compare them without reading a single number.",
 tech="`plt.bar(categories, values)` draws vertical bars and `plt.barh(categories, values)` draws horizontal ones. The `color` argument accepts one colour or a list with one colour per bar. `plt.bar_label(bars)` prints each bar's value on the chart.",
 steps=["Prepare a list of category names and a list of values.", "Call `plt.bar(names, values)`.", "Use `color=[...]` for a colour per bar.", "Use `plt.barh` when names are long.", "Add `plt.bar_label(bars)` to show the numbers."],
 blocks=[
  dict(title="A basic bar chart", plot=True, alt="Vertical bars showing sales of 1350 for Pune, 850 for Delhi and 300 for Mumbai.", code=r'''import matplotlib.pyplot as plt

cities = ['Pune', 'Delhi', 'Mumbai']
sales = [1350, 850, 300]

plt.bar(cities, sales)
plt.title('Sales by city')
plt.ylabel('Sales')
plt.show()''', output=AUTO,
   lines=[("plt.bar(cities, sales)", "One bar per city. The first list gives the labels and the second gives the heights."),
          ("plt.title('Sales by city')", "A title that says what is compared."),
          ("plt.ylabel('Sales')", "Labels the vertical axis. The categories along the bottom speak for themselves.")]),
  dict(title="Horizontal bars with your own colours", plot=True, alt="Horizontal bars for four subjects in different colours, with Maths the longest.", code=r'''import matplotlib.pyplot as plt

subjects = ['Maths', 'Science', 'English', 'History']
marks = [88, 76, 69, 54]
colours = ['#2563eb', '#0d9488', '#f59e0b', '#ef4444']

plt.barh(subjects, marks, color=colours)
plt.xlabel('Marks')
plt.show()''', output=AUTO,
   lines=[("plt.barh(subjects, marks, color=colours)", "`barh` draws horizontal bars. Handy when category names are long and would collide along the bottom."),
          ("color=colours", "A list with one colour for each bar, in the same order."),
          ("plt.xlabel('Marks')", "On a horizontal chart the values run along x, so the label goes on the x axis.")]),
  dict(title="Show the value on each bar", plot=True, alt="Vertical bars for three cities with the value printed above each bar.", code=r'''import matplotlib.pyplot as plt

cities = ['Pune', 'Delhi', 'Mumbai']
sales = [1350, 850, 300]

bars = plt.bar(cities, sales, color='#0d9488', width=0.5)
plt.bar_label(bars)
plt.ylim(0, 1600)
plt.show()''', output=AUTO,
   lines=[("bars = plt.bar(...)", "`bar` returns the bars it drew. We keep them so we can label them."),
          ("width=0.5", "Makes each bar narrower. The default width is 0.8."),
          ("plt.bar_label(bars)", "Prints the value above every bar."),
          ("plt.ylim(0, 1600)", "Sets the y range so the biggest label has room above its bar.")]),
 ],
 mistakes=["Using a line chart for categories. Lines imply a connection between neighbours.",
           "Starting the y axis above zero. Bars are compared by length, so cutting the axis exaggerates differences.",
           "Mixing up `bar` and `barh`. On a horizontal chart the value axis is x, not y.",
           "Giving `color` a list of the wrong length. It needs one colour for each bar."],
 use="Use bar charts to compare separate categories: sales by city, marks by subject, votes by option. Sort the bars from largest to smallest when the order is not important.",
 qa=[("When do you use a bar chart instead of a line chart?", "When the x values are separate categories, not an ordered sequence such as time."),
     ("How do you draw horizontal bars?", "Use `plt.barh(names, values)`."),
     ("How do you show each bar's value on the chart?", "Keep the result of `plt.bar` and pass it to `plt.bar_label`."),
     ("Why should bar charts start at zero?", "Bars encode value by length, so a cut axis makes small differences look huge.")],
 tryit=dict(task="Draw a bar chart of fruit sold: apples 40, bananas 25, mangoes 60. Give it the title `Fruit sold` and show the value on each bar.",
            hint="Keep the result of `plt.bar(...)` in a variable and pass it to `plt.bar_label`.",
            plot=True, alt="Three bars for apples, bananas and mangoes with their values printed on top and the title Fruit sold.",
            solution=r'''import matplotlib.pyplot as plt

fruit = ['Apples', 'Bananas', 'Mangoes']
sold = [40, 25, 60]
bars = plt.bar(fruit, sold)
plt.bar_label(bars)
plt.title('Fruit sold')
plt.show()''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 5
add(id="matplotlib-scatter", section=8, lib="matplotlib", title="Scatter plots: find relationships", time="10 min",
 summary="Plot pairs of values as dots to see whether two things move together, and add colour and size to show more.",
 what="A **scatter plot** draws one dot for every pair of values: one value sets the dot's position across, the other sets its height. The shape of the dots shows how the two values relate.",
 why="Does more study time mean higher marks? Do expensive items sell less? A scatter plot answers questions like these by eye, and it is often the first chart you draw when exploring data. It is the picture behind the correlation number you may have met in Pandas.",
 simple="Imagine a teacher sticking a dot on a wall chart for each student: how many hours they studied across the bottom and their mark up the side. If the dots form a rising band, studying and marks go together.",
 tech="`plt.scatter(x, y)` draws unconnected dots. Extra arguments change them: `s` for size, `c` for colour (a single colour, or a list of numbers mapped through a **colormap** `cmap`), and `alpha` for transparency between 0 and 1. `plt.colorbar()` adds a key for the colour scale.",
 steps=["Prepare two lists of equal length: x values and y values.", "Call `plt.scatter(x, y)`.", "Use `alpha` when dots overlap.", "Use `s` and `c` to show a third or fourth value.", "Add `plt.colorbar()` if colour carries meaning."],
 blocks=[
  dict(title="Hours studied against marks", plot=True, alt="Scatter plot of study hours against marks with dots rising steadily from lower left to upper right.", code=r'''import matplotlib.pyplot as plt

hours = [1, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8]
marks = [35, 42, 48, 50, 58, 62, 65, 72, 80, 88]

plt.scatter(hours, marks)
plt.title('Study time and marks')
plt.xlabel('Hours studied')
plt.ylabel('Marks')
plt.show()''', output=AUTO,
   lines=[("plt.scatter(hours, marks)", "One dot per student. Each dot sits at (hours, marks)."),
          ("plt.title(...) and the two labels", "Always say what the two axes measure, with units where possible."),
          ("What the picture shows", "The dots climb from bottom left to top right: more hours go with higher marks.")]),
  dict(title="Colour and size", plot=True, alt="Scatter plot with larger purple dots, semi-transparent, for study hours against marks.", code=r'''import matplotlib.pyplot as plt

hours = [1, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8]
marks = [35, 42, 48, 50, 58, 62, 65, 72, 80, 88]

plt.scatter(hours, marks, s=120, color='#7c3aed', alpha=0.6)
plt.show()''', output=AUTO,
   lines=[("s=120", "Dot size. Bigger numbers make bigger dots."),
          ("color='#7c3aed'", "A single colour for all dots."),
          ("alpha=0.6", "Transparency from 0 (invisible) to 1 (solid). Overlapping dots show up as darker areas.")]),
  dict(title="Let colour show a third value", plot=True, alt="Scatter plot where each dot is coloured by sleep hours, with a colour bar on the right labelled Hours of sleep.", code=r'''import matplotlib.pyplot as plt

hours = [1, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8]
marks = [35, 42, 48, 50, 58, 62, 65, 72, 80, 88]
sleep = [5, 6, 5, 7, 6, 8, 7, 8, 7, 8]

plt.scatter(hours, marks, c=sleep, cmap='viridis', s=100)
plt.colorbar(label='Hours of sleep')
plt.xlabel('Hours studied')
plt.ylabel('Marks')
plt.show()''', output=AUTO,
   lines=[("c=sleep", "Passing numbers to `c` colours each dot according to its value."),
          ("cmap='viridis'", "The colormap decides which colours the numbers map to. `viridis` stays readable for most colour-blind readers."),
          ("plt.colorbar(label='Hours of sleep')", "Adds the scale bar so people can decode the colours.")]),
 ],
 mistakes=["Joining scatter points with a line. If the order of the points does not matter, use `scatter`, not `plot`.",
           "Reading a pattern as proof of cause. Dots that rise together show a relationship, not that one thing causes the other.",
           "Forgetting `alpha` when many dots overlap, so you cannot see where they are dense.",
           "Passing x and y of different lengths, which raises a `ValueError`."],
 use="Use scatter plots to explore the relationship between two numeric columns, to spot clusters, and to spot outliers: dots far away from all the others.",
 qa=[("What is a scatter plot used for?", "To see the relationship between two numeric variables, spot clusters and find outliers."),
     ("What does the `alpha` argument do?", "It sets transparency from 0 to 1, so overlapping dots are easier to see."),
     ("How do you colour dots by a third variable?", "Pass the values to `c`, choose a `cmap`, and add `plt.colorbar()`."),
     ("Is a rising scatter pattern proof that one variable causes the other?", "No. It only shows that they move together.")],
 tryit=dict(task="Plot these points as a scatter: x = `[1, 2, 3, 4, 5]`, y = `[10, 8, 6, 4, 2]`. Make the dots red, size 80, and label the axes `x` and `y`.",
            hint="Use `plt.scatter(x, y, s=80, color='red')`, then `plt.xlabel` and `plt.ylabel`.",
            plot=True, alt="Five red dots falling in a straight line from upper left to lower right, with axes labelled x and y.",
            solution=r'''import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
plt.scatter(x, y, s=80, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.show()''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 6
add(id="matplotlib-histogram", section=8, lib="matplotlib", title="Histograms: see how values are spread", time="10 min",
 summary="Group numbers into ranges called bins and draw how many fall in each, to see the shape of your data.",
 what="A **histogram** counts how many values fall into each range (called a **bin**) and draws one bar per range. It shows how your data is spread out: where most values sit, and whether there are unusual ones.",
 why="Averages hide the shape of data. A class average of 60 could mean everyone scored near 60, or half scored 30 and half scored 90. A histogram shows which one it is.",
 simple="Imagine sorting exam papers into piles: 0 to 40, 40 to 60, 60 to 80 and 80 to 100. You then look at how tall each pile is. A histogram is a picture of those piles.",
 tech="`plt.hist(data, bins=...)` splits the range of the data into bins and draws a bar for the count in each. `bins` can be a number (how many equal-width bins) or a list of **edges**. Unlike a bar chart, the x axis is a continuous number line and the bars touch. `np.histogram` returns the same counts as numbers.",
 steps=["Collect your numbers in one list.", "Call `plt.hist(data)`.", "Choose `bins` as a number or as a list of edges.", "Add `edgecolor` so neighbouring bars are separated.", "Compare counts with `np.histogram` if you need exact numbers."],
 blocks=[
  dict(title="A basic histogram", plot=True, alt="Histogram of 30 exam marks with five bars, the tallest in the 60 to 70 range.", code=r'''import matplotlib.pyplot as plt

marks = [35, 42, 48, 50, 52, 55, 56, 58, 60, 61,
         62, 63, 64, 65, 66, 67, 68, 70, 71, 72,
         74, 75, 78, 80, 82, 85, 88, 90, 93, 97]

plt.hist(marks, bins=5, edgecolor='white')
plt.title('Exam marks')
plt.xlabel('Marks')
plt.ylabel('Number of students')
plt.show()''', output=AUTO,
   lines=[("marks = [...]", "Thirty marks. Unlike a bar chart, a histogram takes the **raw values**, not counts."),
          ("bins=5", "Split the range of marks into five equal-width bins."),
          ("edgecolor='white'", "Draws a thin white line around each bar so bars are easy to tell apart."),
          ("plt.ylabel('Number of students')", "The height of each bar is a count of students, so say so.")]),
  dict(title="Choose the bins yourself", plot=True, alt="Histogram with four bars for the ranges 0 to 40, 40 to 60, 60 to 80 and 80 to 100.", code=r'''import matplotlib.pyplot as plt

marks = [35, 42, 48, 50, 52, 55, 56, 58, 60, 61,
         62, 63, 64, 65, 66, 67, 68, 70, 71, 72,
         74, 75, 78, 80, 82, 85, 88, 90, 93, 97]

plt.hist(marks, bins=[0, 40, 60, 80, 100], edgecolor='white', color='#0d9488')
plt.xlabel('Marks')
plt.ylabel('Number of students')
plt.show()''', output=AUTO,
   lines=[("bins=[0, 40, 60, 80, 100]", "A list gives the **edges** of the bins: 0 to 40, 40 to 60, 60 to 80 and 80 to 100. The widths can differ."),
          ("color='#0d9488'", "Sets the bar colour.")]),
  dict(title="Get the counts as numbers", code=r'''import numpy as np

marks = [35, 42, 48, 50, 52, 55, 56, 58, 60, 61,
         62, 63, 64, 65, 66, 67, 68, 70, 71, 72,
         74, 75, 78, 80, 82, 85, 88, 90, 93, 97]

counts, edges = np.histogram(marks, bins=[0, 40, 60, 80, 100])
print(counts)
print(edges)
print(counts.sum() == len(marks))''', output=AUTO,
   lines=[("np.histogram(marks, bins=[...])", "Does the same counting as `plt.hist` but returns numbers instead of drawing."),
          ("counts", "How many marks fall in each bin."),
          ("edges", "The bin edges you passed in."),
          ("counts.sum() == len(marks)", "Every mark lands in exactly one bin, so the counts add back up to 30.")]),
 ],
 mistakes=["Using a bar chart when you have raw numbers. A histogram does the counting for you.",
           "Choosing too few or too many bins. Too few hides the shape; too many makes a jagged mess. Try a few values.",
           "Forgetting that a value on a bin edge goes into the upper bin, except for the very last bin which includes its right edge.",
           "Not labelling the y axis. Readers must know whether bars show counts or percentages."],
 use="Use a histogram to see the distribution of one numeric column: marks, ages, delivery times, prices. It is a standard first step in data cleaning, because outliers show up as lonely bars.",
 qa=[("What is the difference between a bar chart and a histogram?", "A bar chart compares separate categories. A histogram groups continuous numbers into ranges and counts how many fall in each."),
     ("What are bins?", "The ranges the data is divided into. Each bar of a histogram represents one bin."),
     ("How do you set custom bin edges?", "Pass a list to `bins`, for example `bins=[0, 40, 60, 80, 100]`."),
     ("How do you get the bin counts without drawing?", "Use `np.histogram(data, bins=...)`, which returns the counts and the edges.")],
 tryit=dict(task="Draw a histogram of `ages = [12, 15, 15, 16, 18, 21, 22, 22, 25, 30, 31, 45]` with bins `[10, 20, 30, 50]`, and give it the x label `Age`.",
            hint="Pass the list of edges to `bins=`. Add `edgecolor='white'` for a cleaner look.",
            plot=True, alt="Histogram of ages with three bars for the ranges 10 to 20, 20 to 30 and 30 to 50, with the x axis labelled Age.",
            solution=r'''import matplotlib.pyplot as plt

ages = [12, 15, 15, 16, 18, 21, 22, 22, 25, 30, 31, 45]
plt.hist(ages, bins=[10, 20, 30, 50], edgecolor='white')
plt.xlabel('Age')
plt.show()''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 7
add(id="matplotlib-pie-charts", section=8, lib="matplotlib", title="Pie charts: parts of a whole", time="8 min",
 summary="Draw a pie chart, print percentages on the slices, pull a slice out and keep it readable.",
 what="A **pie chart** shows how a total is split into parts. Each slice is one part, and its angle is proportional to its share of the whole.",
 why="When the question is *what share of the total is each part?*, a pie answers it quickly: the biggest slice is the biggest part. It is common in budgets, survey results and market-share summaries.",
 simple="Think of a pizza cut into slices of different sizes. You immediately see who got the biggest slice. A pie chart is that pizza, drawn from your numbers.",
 tech="`plt.pie(values, labels=names)` draws the chart. `autopct='%1.1f%%'` prints each slice's percentage (the format means *one decimal place, then a percent sign*). `explode=[...]` pulls slices out, `startangle` rotates the start, and `plt.axis('equal')` keeps the pie round.",
 steps=["Prepare the values and their names.", "Call `plt.pie(values, labels=names)`.", "Add `autopct` to show percentages.", "Use `explode` to emphasise one slice.", "Keep the number of slices small."],
 blocks=[
  dict(title="A basic pie chart", plot=True, alt="Pie chart of monthly spending split into rent, food, travel and savings with a label beside each slice.", code=r'''import matplotlib.pyplot as plt

spend = [12000, 6000, 3000, 9000]
names = ['Rent', 'Food', 'Travel', 'Savings']

plt.pie(spend, labels=names)
plt.show()''', output=AUTO,
   lines=[("spend = [...]", "The amounts. Matplotlib works out each share from the total, so you do not need to convert to percentages."),
          ("labels=names", "Writes a name beside each slice, in the same order as the values.")]),
  dict(title="Percentages, colours and a slice pulled out", plot=True, alt="Pie chart with percentages on each slice, custom colours and the Savings slice pulled out.", code=r'''import matplotlib.pyplot as plt

spend = [12000, 6000, 3000, 9000]
names = ['Rent', 'Food', 'Travel', 'Savings']
colours = ['#2563eb', '#f59e0b', '#ef4444', '#0d9488']

plt.pie(spend, labels=names, colors=colours,
        autopct='%1.1f%%', startangle=90,
        explode=[0, 0, 0, 0.1])
plt.title('Where my money goes')
plt.show()''', output=AUTO,
   lines=[("colors=colours", "One colour per slice. This argument is spelled `colors` in `pie`."),
          ("autopct='%1.1f%%'", "Prints each slice's share with one decimal place. The doubled `%%` produces a single `%` sign."),
          ("startangle=90", "Starts the first slice at the top instead of the right."),
          ("explode=[0, 0, 0, 0.1]", "Moves slices away from the centre. Here only the last slice, Savings, is pulled out.")]),
  dict(title="A legend instead of labels", plot=True, alt="Pie chart with percentages and a legend listing the four categories at the side.", code=r'''import matplotlib.pyplot as plt

spend = [12000, 6000, 3000, 9000]
names = ['Rent', 'Food', 'Travel', 'Savings']

plt.pie(spend, autopct='%1.0f%%')
plt.legend(names, loc='center left', bbox_to_anchor=(1, 0.5))
plt.axis('equal')
plt.show()''', output=AUTO,
   lines=[("plt.pie(spend, autopct='%1.0f%%')", "No `labels` here, so the slices stay uncluttered. `1.0f` shows whole percentages."),
          ("plt.legend(names, loc=..., bbox_to_anchor=(1, 0.5))", "Puts a legend to the right of the pie instead of writing names on it."),
          ("plt.axis('equal')", "Makes the x and y scales equal, so the pie stays a circle.")]),
 ],
 mistakes=["Using a pie with many slices. Past five or six, a bar chart is much easier to read.",
           "Using a pie for values that are not parts of one whole, such as temperatures in different cities.",
           "Passing negative values. Pie slices must be zero or more.",
           "Giving `labels` or `explode` lists of a different length than the values."],
 use="Use a pie chart only when you want to show shares of a single total with a handful of parts. If you need to compare sizes precisely, use a bar chart.",
 qa=[("How do you show percentages on a pie chart?", "Use `autopct`, for example `autopct='%1.1f%%'`."),
     ("What does `explode` do?", "It pulls slices away from the centre by a fraction of the radius, to emphasise them."),
     ("When is a pie chart a poor choice?", "When there are many categories or when the parts do not add up to a meaningful whole. A bar chart is clearer."),
     ("Why use `plt.axis('equal')`?", "It keeps the chart perfectly round instead of stretched into an oval.")],
 tryit=dict(task="Draw a pie chart of study time: Python 5, Maths 3, English 2 (hours). Show percentages with one decimal place and start the first slice at the top.",
            hint="Use `autopct='%1.1f%%'` and `startangle=90`, with `labels=` for the names.",
            plot=True, alt="Pie chart with three labelled slices for Python, Maths and English showing percentages 50.0, 30.0 and 20.0.",
            solution=r'''import matplotlib.pyplot as plt

hours = [5, 3, 2]
subjects = ['Python', 'Maths', 'English']
plt.pie(hours, labels=subjects, autopct='%1.1f%%', startangle=90)
plt.show()''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 8
add(id="matplotlib-subplots-save", section=8, lib="matplotlib", title="Subplots and saving charts", time="11 min",
 summary="Put several charts in one figure, meet the figure/axes way of working, and save your chart as an image file.",
 what="A **subplot** is one small chart inside a bigger picture. `plt.subplots()` creates the whole picture (the **figure**) and the chart areas inside it (the **axes**), so you can place several charts side by side. `savefig` writes the result to an image file.",
 why="Dashboards, reports and LinkedIn posts rarely use one chart alone. Putting related charts next to each other lets people compare them. Saving as a file lets you drop the chart into a document, a website or a post.",
 simple="Think of a photo frame with four windows. The frame is the **figure** and each window is an **axes** where you put one picture. You decorate each window separately, then hang the whole frame on the wall.",
 tech="`fig, axs = plt.subplots(rows, cols, figsize=(w, h))` returns a figure and an array of axes. You draw with methods on an axes (`ax.plot`, `ax.bar`) and style it with `ax.set_title`, `ax.set_xlabel`, `ax.set_ylabel`. `fig.tight_layout()` prevents overlaps. `plt.savefig('name.png', dpi=200)` writes the figure to a file; call it **before** `plt.show()`.",
 steps=["Create the grid with `fig, axs = plt.subplots(1, 2, figsize=(9, 3.5))`.", "Draw on each axes, for example `axs[0].plot(...)`.", "Style each axes with `set_title` and the label methods.", "Call `fig.tight_layout()` so nothing overlaps.", "Save with `plt.savefig(...)` and then show."],
 blocks=[
  dict(title="Two charts side by side", plot=True, alt="Two charts side by side: a line chart of weekly steps on the left and a bar chart of sales by city on the right.", code=r'''import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(9, 3.5))

axs[0].plot([1, 2, 3, 4, 5], [4, 6, 5, 8, 7])
axs[0].set_title('Steps')

axs[1].bar(['Pune', 'Delhi', 'Mumbai'], [1350, 850, 300])
axs[1].set_title('Sales')

fig.tight_layout()
plt.show()''', output=AUTO,
   lines=[("plt.subplots(1, 2, figsize=(9, 3.5))", "Creates one figure with 1 row and 2 columns of charts. `figsize` is the width and height in inches."),
          ("axs[0].plot(...)", "Draws on the left chart. With a single row, `axs` is a simple list of two axes."),
          ("axs[0].set_title('Steps')", "On an axes object the method is `set_title`, not `title`."),
          ("axs[1].bar(...)", "A completely different type of chart on the right."),
          ("fig.tight_layout()", "Adjusts the spacing so titles and labels do not overlap.")]),
  dict(title="A 2 by 2 grid", plot=True, alt="A 2 by 2 grid of four small charts: a line chart, a bar chart, a scatter plot and a histogram, under the overall title Four ways to look at data.", code=r'''import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(8, 6))
fig.suptitle('Four ways to look at data')

axs[0, 0].plot([1, 2, 3, 4], [2, 4, 3, 6])
axs[0, 0].set_title('Line')

axs[0, 1].bar(['A', 'B', 'C'], [5, 9, 3])
axs[0, 1].set_title('Bar')

axs[1, 0].scatter([1, 2, 3, 4, 5], [2, 3, 5, 4, 6])
axs[1, 0].set_title('Scatter')

axs[1, 1].hist([1, 2, 2, 3, 3, 3, 4, 4, 5], bins=5)
axs[1, 1].set_title('Histogram')

fig.tight_layout()
plt.show()''', output=AUTO,
   lines=[("plt.subplots(2, 2, ...)", "A grid with 2 rows and 2 columns. Now `axs` is two-dimensional, so you pick a chart with `axs[row, col]`."),
          ("fig.suptitle(...)", "A title for the whole figure, above all the charts."),
          ("axs[0, 0] ... axs[1, 1]", "The four windows: top left, top right, bottom left and bottom right."),
          ("fig.tight_layout()", "Keeps the four titles and labels from running into each other.")]),
  dict(title="Save the chart to a file", code=r'''import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [2, 4, 3])
plt.title('Saved chart')
plt.savefig('chart.png', dpi=150, bbox_inches='tight')

print(os.path.exists('chart.png'))
print(os.path.getsize('chart.png') > 0)''', output=AUTO,
   lines=[("matplotlib.use('Agg')", "Switches to a backend that draws to files and opens no window. This is useful on servers and for scripts that only save images. On your own computer you can leave it out."),
          ("plt.savefig('chart.png', dpi=150, bbox_inches='tight')", "Writes the chart to `chart.png`. `dpi` sets the sharpness and `bbox_inches='tight'` trims extra white space."),
          ("os.path.exists('chart.png')", "Confirms the file now exists."),
          ("os.path.getsize('chart.png') > 0", "And that it is not empty.")]),
 ],
 mistakes=["Calling `plt.savefig` *after* `plt.show()`. Once the window is closed the figure is cleared and you save a blank image.",
           "Using `axs[0]` on a 2-D grid, or `axs[0, 0]` on a single row. Check the shape you asked for.",
           "Mixing `plt.title` with axes objects. On an axes it is `ax.set_title`, `ax.set_xlabel` and `ax.set_ylabel`.",
           "Forgetting `tight_layout()` and ending up with overlapping labels."],
 use="Use subplots to compare related charts in one picture, and `savefig` whenever the chart has to leave your script: a report, a slide, a website or a post.",
 qa=[("What is the difference between a figure and an axes?", "The figure is the whole canvas. An axes is one chart area on it, with its own x and y axis."),
     ("How do you create a 2 by 3 grid of charts?", "`fig, axs = plt.subplots(2, 3)`."),
     ("How do you save a chart as an image?", "`plt.savefig('name.png')`, called before `plt.show()`."),
     ("What does `tight_layout` do?", "It adjusts the spacing between subplots so labels and titles do not overlap.")],
 tryit=dict(task="Create a figure with two charts side by side: on the left a line plot of `[1, 2, 3]` against `[1, 4, 9]`, on the right a bar chart of `['A', 'B']` with values `[3, 5]`. Give each chart a title.",
            hint="Use `fig, axs = plt.subplots(1, 2)`, draw on `axs[0]` and `axs[1]`, and use `set_title`.",
            plot=True, alt="Two small charts side by side: a rising line chart on the left titled Line and a two-bar chart on the right titled Bars.",
            solution=r'''import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2)
axs[0].plot([1, 2, 3], [1, 4, 9])
axs[0].set_title('Line')
axs[1].bar(['A', 'B'], [3, 5])
axs[1].set_title('Bars')
fig.tight_layout()
plt.show()''', output=AUTO),
 related=[])
