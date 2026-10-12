# Section 6: Pandas for Data Analysis (original lessons, own examples).
# Outputs marked "AUTO" are filled in by build_lessons.py from a real run, so they can never be wrong.
# Every code block is self-contained (it imports what it needs) so learners can copy and run any block alone.
from part1 import add

AUTO = "AUTO"

# ---------------------------------------------------------------- 1
add(id="pandas-series", section=6, lib="pandas", title="Pandas Series: labelled 1-D data", time="8 min",
 summary="Meet Pandas and its simplest building block, the Series: one column of data with a label on every value.",
 what="**Pandas** is a Python library for working with tables of data: loading them, cleaning them and answering questions about them. Its simplest object is the **Series**: one column of values where every value also carries a **label** (called the index).",
 why="Real data rarely arrives as a tidy Python list. It arrives as marks registers, sales sheets and sensor logs. Pandas lets you ask *what is the average?* or *which entry is the highest?* in one line, with no loop. A Series is the piece every bigger Pandas object is built from, so understanding it makes everything else easier.",
 simple="Think of one column in your class marks register. Each mark sits next to a student's name. The marks are the **values**, the names are the **labels**, and the whole column is a **Series**.",
 tech="A Series is a one-dimensional array (backed by NumPy) with an **index** and a single **dtype**. Operations such as `+`, `>` and `.mean()` work on the whole Series at once (this is called *vectorised*) and line up values by their index labels.",
 steps=["Install Pandas once with `pip`.", "Import it with the usual alias `pd`.", "Build a Series from a list or a dictionary.", "Read values by label (`s[\"Ravi\"]`) or by position (`s.iloc[0]`).", "Use methods like `mean()` and comparisons to analyse the whole Series."],
 blocks=[
  dict(title="Install and import", plain=True, noRun=True, code='''pip install pandas      # run once, in your terminal

import pandas as pd     # at the top of every script''',
   lines=[("pip install pandas", "Downloads Pandas from PyPI. Run it in your terminal one time, not inside a Python file."),
          ("import pandas as pd", "Loads the library. `pd` is the short name everyone uses, so your code looks like code in tutorials and jobs.")]),
  dict(title="Create a Series from a list", code=r'''import pandas as pd

marks = pd.Series([78, 90, 66])
print(marks)
print(marks.dtype)''', output=AUTO,
   lines=[("marks = pd.Series([78, 90, 66])", "Builds a Series from a list. With no labels given, Pandas numbers the values 0, 1, 2."),
          ("print(marks)", "Shows the labels on the left, the values on the right and the dtype at the bottom."),
          ("print(marks.dtype)", "Shows the data type of the values. All values in a Series share one dtype.")]),
  dict(title="Give it your own labels", code=r'''import pandas as pd

marks = pd.Series([78, 90, 66], index=["Asha", "Ravi", "Meena"])
print(marks)
print("Ravi:", marks["Ravi"])
print("First by position:", marks.iloc[0])
print("Average:", marks.mean())''', output=AUTO,
   lines=[("index=[\"Asha\", \"Ravi\", \"Meena\"]", "Replaces the default 0, 1, 2 with names. You need one label per value."),
          ("marks[\"Ravi\"]", "Reads a value by its label."),
          ("marks.iloc[0]", "Reads a value by its position. `iloc` always counts from 0, whatever the labels are."),
          ("marks.mean()", "Averages the whole Series in one call, with no loop.")]),
  dict(title="Build one from a dictionary and filter it", code=r'''import pandas as pd

steps = {"Mon": 4200, "Tue": 8100, "Wed": 6500, "Thu": 9300}
s = pd.Series(steps)
print(s[s > 6000])
print(pd.Series(steps, index=["Mon", "Thu"]))''', output=AUTO,
   lines=[("s = pd.Series(steps)", "Dictionary keys become the labels and the dictionary values become the data."),
          ("s[s > 6000]", "`s > 6000` gives a True/False value for every item. Using that inside `[]` keeps only the True ones."),
          ("pd.Series(steps, index=[\"Mon\", \"Thu\"])", "Passing `index` picks only those keys from the dictionary.")]),
 ],
 mistakes=["Writing `pd.series(...)` with a small `s`. The class is `pd.Series`.",
           "Treating the index as positions. `marks[0]` asks for a *label* called 0 (newer Pandas raises a `KeyError`). Use `marks.iloc[0]` for the first item.",
           "Assuming labels are unique. They don't have to be, which can give surprising results when you select by label."],
 use="Use a Series when you have one list of related values that deserve labels, or when you pull a single column out of a bigger table.",
 qa=[("What is a Pandas Series?", "A one-dimensional labelled array: a sequence of values of one dtype plus an index of labels."),
     ("How is a Series different from a Python list?", "A Series has labels, holds a single dtype and supports whole-column operations like `s * 2` or `s.mean()` without a loop. A list can mix types and needs a loop for the same work."),
     ("How do you select by label and by position?", "By label: `s[\"Ravi\"]` or `s.loc[\"Ravi\"]`. By position: `s.iloc[0]`."),
     ("What happens when you create a Series from a dictionary?", "The keys become the index labels and the values become the data.")],
 tryit=dict(task="Create a Series of daily study hours for Mon, Tue and Wed with the values 2, 3 and 1.5. Print the Series, then print the total hours using `sum()`.",
            hint="Pass a list of numbers and `index=[...]`, then call `.sum()` on the Series.",
            solution=r'''import pandas as pd

hours = pd.Series([2, 3, 1.5], index=["Mon", "Tue", "Wed"])
print(hours)
print("Total:", hours.sum())''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 2
add(id="pandas-dataframe", section=6, lib="pandas", title="Pandas DataFrame: tables in Python", time="10 min",
 summary="Create a table, pick out columns and rows, and add a new column calculated from the others.",
 what="A **DataFrame** is a table with rows and columns. Each column is a Series, and all the columns share the same row labels (the index).",
 why="Almost every real dataset is a table: students and marks, orders and prices, dates and temperatures. A DataFrame lets you slice, calculate and summarise that table with a few short lines instead of nested loops.",
 simple="Picture a spreadsheet or your school register: headings across the top and one row per student. A DataFrame is that sheet living inside Python, where you can ask questions about it with code.",
 tech="A DataFrame is a two-dimensional, size-mutable table of labelled columns that can hold different dtypes. Selecting one column returns a Series; selecting several returns a smaller DataFrame. `.loc` selects by label and `.iloc` by integer position.",
 table=dict(head=["You want", "Write", "You get"], rows=[
   ["One column", "df[\"maths\"]", "A Series"],
   ["Several columns", "df[[\"name\", \"maths\"]]", "A DataFrame"],
   ["One row by label", "df.loc[1]", "A Series"],
   ["One row by position", "df.iloc[1]", "A Series"],
   ["Several rows", "df.loc[[0, 2]]", "A DataFrame"]]),
 steps=["Put each column's values in a list and collect the lists in a dictionary.", "Pass the dictionary to `pd.DataFrame()`.", "Select columns with `df[\"col\"]` or `df[[\"a\", \"b\"]]`.", "Select rows with `.loc` (labels) or `.iloc` (positions).", "Create a new column by assigning to a new name."],
 blocks=[
  dict(title="Create a DataFrame from a dictionary", code=r'''import pandas as pd

data = {
    "name": ["Asha", "Ravi", "Meena", "Kabir"],
    "maths": [78, 90, 66, 84],
    "science": [82, 75, 70, 91],
}
df = pd.DataFrame(data)
print(df)
print("Shape:", df.shape)''', output=AUTO,
   lines=[("data = { ... }", "Each key is a column heading and each list holds that column's values. All lists must be the same length."),
          ("df = pd.DataFrame(data)", "Turns the dictionary into a table. The row labels 0, 1, 2, 3 are added automatically."),
          ("df.shape", "A tuple of (number of rows, number of columns).")]),
  dict(title="Pick columns", code=r'''import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "Kabir"],
    "maths": [78, 90, 66, 84],
    "science": [82, 75, 70, 91],
})
print(df["maths"])
print(df[["name", "maths"]])''', output=AUTO,
   lines=[("df[\"maths\"]", "One column name in single brackets gives a Series."),
          ("df[[\"name\", \"maths\"]]", "A list of names in double brackets gives a smaller DataFrame. The outer brackets select, the inner brackets make the list.")]),
  dict(title="Pick rows with loc and iloc", code=r'''import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "Kabir"],
    "maths": [78, 90, 66, 84],
})
print(df.loc[0])
print(df.iloc[1])
print(df.loc[[0, 2]])
print(df.loc[1, "name"])''', output=AUTO,
   lines=[("df.loc[0]", "Row labelled 0, returned as a Series whose labels are the column names."),
          ("df.iloc[1]", "The second row by position. Here the label and the position happen to match."),
          ("df.loc[[0, 2]]", "A list of labels returns those rows as a DataFrame."),
          ("df.loc[1, \"name\"]", "Row label first, column label second, which gives a single value.")]),
  dict(title="Use a named index and add a column", code=r'''import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "Kabir"],
    "maths": [78, 90, 66, 84],
    "science": [82, 75, 70, 91],
})
df = df.set_index("name")
df["total"] = df["maths"] + df["science"]
print(df)
print(df.loc["Ravi"])''', output=AUTO,
   lines=[("df.set_index(\"name\")", "Makes the `name` column the row labels. It returns a new DataFrame, so we assign it back to `df`."),
          ("df[\"total\"] = df[\"maths\"] + df[\"science\"]", "Adds two columns row by row and stores the result in a new column called `total`."),
          ("df.loc[\"Ravi\"]", "Rows are now found by name instead of by 0, 1, 2.")]),
 ],
 mistakes=["Using `df[\"name\", \"maths\"]` for two columns. Use double brackets: `df[[\"name\", \"maths\"]]`.",
           "Mixing up `.loc` (labels) and `.iloc` (positions). After `set_index`, the label `\"Ravi\"` and the position `1` are different things.",
           "Expecting `df.loc[0:2]` to stop before 2. With `.loc` the end label is **included**; with `.iloc` the end position is excluded."],
 use="Use a DataFrame whenever your data has several related columns: any CSV, spreadsheet or database table you want to analyse.",
 qa=[("What is the difference between a Series and a DataFrame?", "A Series is one labelled column. A DataFrame is a table of several columns that share one index."),
     ("What is the difference between loc and iloc?", "`loc` selects by label (row and column names). `iloc` selects by integer position."),
     ("How do you add a new column?", "Assign to a new column name, for example `df[\"total\"] = df[\"maths\"] + df[\"science\"]`. The calculation runs for every row."),
     ("How do you select more than one column?", "Pass a list of names: `df[[\"name\", \"maths\"]]`.")],
 tryit=dict(task="Create a DataFrame with 3 products: pen (price 10, qty 5), book (price 120, qty 2) and bag (price 450, qty 1). Add a `revenue` column equal to `price * qty` and print the DataFrame.",
            hint="Use a dictionary with `item`, `price` and `qty` lists, then assign `df[\"revenue\"] = df[\"price\"] * df[\"qty\"]`.",
            solution=r'''import pandas as pd

df = pd.DataFrame({
    "item": ["pen", "book", "bag"],
    "price": [10, 120, 450],
    "qty": [5, 2, 1],
})
df["revenue"] = df["price"] * df["qty"]
print(df)''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 3
add(id="pandas-read-files", section=6, lib="pandas", title="Read and save CSV and JSON files", time="9 min",
 summary="Load data from files into a DataFrame, pick only the columns you need and save your results back to disk.",
 what="Pandas can load a file into a DataFrame with a single function call: `read_csv()` for comma-separated text files and `read_json()` for JSON. `to_csv()` goes the other way and saves a DataFrame to a file.",
 why="Your data almost always lives in a file or an export, not in your code. Loading and saving is the first and last step of nearly every data task.",
 simple="A CSV file is a notebook where each line is one row and commas separate the columns. `read_csv()` is a helper that reads the whole notebook and hands you a neat table.",
 tech="`read_csv(path)` parses delimited text into a DataFrame, inferring dtypes from the values. `read_json(path)` expects JSON that looks like a list of records or a dictionary of columns. `to_csv(path, index=False)` writes the table out without the row labels.",
 steps=["Have the file in the folder you run your script from (or give the full path).", "Call `pd.read_csv(\"file.csv\")` or `pd.read_json(\"file.json\")`.", "Check the result with `print(df)` or `df.head()`.", "Clean or add columns as needed.", "Save with `df.to_csv(\"out.csv\", index=False)`."],
 blocks=[
  dict(title="Create a small CSV to practise with", code=r'''csv_text = """item,price,qty
pen,10,5
notebook,45,3
bag,450,1
marker,30,4
"""

with open("shop.csv", "w") as f:
    f.write(csv_text)

print("shop.csv created")''', output=AUTO,
   lines=[("csv_text = \"\"\"...\"\"\"", "A multi-line string. The first line holds the column names; every other line is one row."),
          ("with open(\"shop.csv\", \"w\") as f:", "Opens (and creates) the file for writing, then closes it automatically."),
          ("f.write(csv_text)", "Saves the text into the file. The next blocks read this file.")]),
  dict(title="Read the CSV", code=r'''import pandas as pd

df = pd.read_csv("shop.csv")
print(df)
print(df.head(2))''', output=AUTO,
   lines=[("pd.read_csv(\"shop.csv\")", "Reads the file. The first line becomes the column names and Pandas works out each column's type."),
          ("df.head(2)", "Shows only the first 2 rows. Handy for peeking at big files.")]),
  dict(title="Choose columns and an index", code=r'''import pandas as pd

small = pd.read_csv("shop.csv", usecols=["item", "price"])
print(small)

by_item = pd.read_csv("shop.csv", index_col="item")
print(by_item.loc["bag"])''', output=AUTO,
   lines=[("usecols=[\"item\", \"price\"]", "Loads only the listed columns, which is quicker and tidier for wide files."),
          ("index_col=\"item\"", "Uses that column as the row labels instead of 0, 1, 2."),
          ("by_item.loc[\"bag\"]", "Because `item` is the index, we can find a row by its item name.")]),
  dict(title="Read a JSON file", code=r'''import pandas as pd

json_text = '[{"item": "pen", "price": 10}, {"item": "bag", "price": 450}]'
with open("shop.json", "w") as f:
    f.write(json_text)

df = pd.read_json("shop.json")
print(df)''', output=AUTO,
   lines=[("json_text = '[{...}, {...}]'", "JSON as a list of objects. Each object becomes one row, and its keys become the column names."),
          ("pd.read_json(\"shop.json\")", "Loads that file into a DataFrame. Because JSON objects look like Python dictionaries, this feels like `pd.DataFrame(list_of_dicts)`.")]),
  dict(title="Save a result with to_csv", code=r'''import pandas as pd

df = pd.read_csv("shop.csv")
df["total"] = df["price"] * df["qty"]
df.to_csv("shop_totals.csv", index=False)

print(open("shop_totals.csv").read())''', output=AUTO,
   lines=[("df[\"total\"] = df[\"price\"] * df[\"qty\"]", "Calculates a new column for every row."),
          ("df.to_csv(\"shop_totals.csv\", index=False)", "Writes the table to a new file. `index=False` leaves out the 0, 1, 2 row labels."),
          ("print(open(...).read())", "Reads the saved file back as plain text so you can see exactly what was written.")]),
 ],
 mistakes=["Getting `FileNotFoundError`. Python looks in the folder you *run* the script from, not the folder where you saved it. Check the path.",
           "Forgetting `index=False` in `to_csv()`. The saved file then gets an extra unnamed column of row numbers.",
           "Assuming a printed big DataFrame shows everything. Pandas hides the middle rows with `...`; use `df.to_string()` to print them all."],
 use="Use `read_csv()` for spreadsheets exported as CSV and `read_json()` for data from web APIs. Use `to_csv()` to share cleaned data or feed it into another tool.",
 qa=[("What does read_csv() return?", "A DataFrame built from the file. The first row is used as the column names by default."),
     ("How do you read only some columns?", "Pass `usecols=[\"col1\", \"col2\"]` to `read_csv()`."),
     ("Why use index=False when saving?", "Otherwise Pandas writes the row labels as an extra first column, and reading the file back creates an unwanted `Unnamed: 0` column."),
     ("What if the file uses semicolons instead of commas?", "Tell Pandas with `sep=\";\"`, for example `pd.read_csv(\"file.csv\", sep=\";\")`.")],
 tryit=dict(task="Write a CSV with the text `name,marks`, then `Asha,78`, `Ravi,90`, `Meena,66` (one per line) into a file called `marks.csv`. Read it with Pandas and print the average of the `marks` column.",
            hint="Write the text with `open(..., \"w\")`, then `pd.read_csv(\"marks.csv\")` and `df[\"marks\"].mean()`.",
            solution=r'''import pandas as pd

with open("marks.csv", "w") as f:
    f.write("name,marks\nAsha,78\nRavi,90\nMeena,66\n")

df = pd.read_csv("marks.csv")
print(df["marks"].mean())''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 4
add(id="pandas-explore-filter", section=6, lib="pandas", title="Explore, sort and filter data", time="10 min",
 summary="Get a quick overview of a DataFrame, then sort it and pull out only the rows that match a rule.",
 what="Before analysing anything, you look at the data: its size, columns, types and basic statistics. After that you **sort** rows and **filter** them, which means keeping only the rows where a condition is true.",
 why="Real files are messy and large. A fast overview shows you what you are dealing with, and filtering lets you answer questions like *who scored above 80?* without writing a loop.",
 simple="When someone hands you a thick register, you flip to the first and last pages, check how many columns it has, then underline the rows that matter. `head()`, `info()` and filtering are those three moves.",
 tech="`head()`/`tail()` show the first or last rows. `info()` lists columns, non-null counts and dtypes. `describe()` summarises numeric columns. A condition like `df[\"marks\"] >= 80` produces a Boolean Series, and passing it to `df[...]` keeps only the True rows (Boolean masking).",
 steps=["Peek with `head()` and `tail()`, and check `shape`.", "Check types and gaps with `info()`.", "Get statistics with `describe()`.", "Sort with `sort_values()`.", "Filter with a condition inside `df[...]`, joining conditions with `&` or `|`."],
 blocks=[
  dict(title="Peek at the data", code=r'''import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "Kabir", "Isha", "Dev", "Nina", "Omar"],
    "section": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "marks": [78, 90, 66, 84, 91, 55, 73, 84],
})
print(df.head(3))
print(df.tail(2))
print(df.shape)
print(list(df.columns))''', output=AUTO,
   lines=[("df.head(3)", "First 3 rows. With no number, `head()` shows 5."),
          ("df.tail(2)", "Last 2 rows."),
          ("df.shape", "(rows, columns)."),
          ("list(df.columns)", "The column names as a normal Python list.")]),
  dict(title="Types and statistics", code=r'''import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "Kabir", "Isha", "Dev", "Nina", "Omar"],
    "section": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "marks": [78, 90, 66, 84, 91, 55, 73, 84],
})
df.info(memory_usage=False)
print(df.describe())''', output=AUTO,
   lines=[("df.info(memory_usage=False)", "Prints the number of rows, each column's name, how many values are not missing and its dtype. (Text columns show as `str` in Pandas 3 and `object` in older versions.) `memory_usage=False` just hides the memory line."),
          ("df.describe()", "Count, mean, standard deviation, minimum, quartiles and maximum for every numeric column.")]),
  dict(title="Sort and filter", code=r'''import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "Kabir", "Isha", "Dev", "Nina", "Omar"],
    "section": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "marks": [78, 90, 66, 84, 91, 55, 73, 84],
})
print(df.sort_values("marks", ascending=False).head(3))
print(df[df["marks"] >= 80])
print(df[(df["section"] == "A") & (df["marks"] > 70)])''', output=AUTO,
   lines=[("df.sort_values(\"marks\", ascending=False)", "Sorts by marks from high to low. It returns a new DataFrame and leaves `df` as it was."),
          (".head(3)", "Keeps the top 3 of the sorted result."),
          ("df[df[\"marks\"] >= 80]", "The inner part is a True/False column; the outer `df[...]` keeps rows where it is True."),
          ("(df[\"section\"] == \"A\") & (df[\"marks\"] > 70)", "Both conditions must be true. Use `&` for *and*, `|` for *or*, and wrap each condition in parentheses.")]),
  dict(title="Count and list values", code=r'''import pandas as pd

df = pd.DataFrame({
    "section": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "marks": [78, 90, 66, 84, 91, 55, 73, 84],
})
print(df["section"].value_counts())
print(df["marks"].nunique())
print(df["marks"].unique())''', output=AUTO,
   lines=[("df[\"section\"].value_counts()", "How many times each value appears."),
          ("df[\"marks\"].nunique()", "How many different values there are."),
          ("df[\"marks\"].unique()", "The distinct values themselves, in order of first appearance.")]),
 ],
 mistakes=["Writing `and` / `or` instead of `&` / `|` in a filter. Python's keywords don't work on whole columns.",
           "Forgetting parentheses: `df[\"a\"] > 1 & df[\"b\"] < 5` is evaluated in the wrong order. Write `(df[\"a\"] > 1) & (df[\"b\"] < 5)`.",
           "Expecting `sort_values()` to change the DataFrame. It returns a sorted copy, so assign it back (`df = df.sort_values(...)`) if you want to keep it."],
 use="Use these steps at the start of any analysis: peek, check types, summarise, then sort and filter to answer specific questions.",
 qa=[("What does df.info() tell you?", "The number of rows, each column's dtype and how many non-null values it has, which is the quickest way to spot missing data."),
     ("How do you filter rows by two conditions?", "Wrap each condition in parentheses and join them with `&` (and) or `|` (or): `df[(df[\"a\"] > 1) & (df[\"b\"] < 5)]`."),
     ("What does describe() show?", "Count, mean, standard deviation, min, quartiles and max for numeric columns."),
     ("How do you sort in descending order?", "`df.sort_values(\"col\", ascending=False)`.")],
 tryit=dict(task="Using a DataFrame with `name` = Asha, Ravi, Meena, Dev and `marks` = 78, 90, 66, 55, print a list of the names of students who scored below 70.",
            hint="Filter with `df[\"marks\"] < 70`, select the `name` column, then call `.tolist()`.",
            solution=r'''import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "Dev"],
    "marks": [78, 90, 66, 55],
})
print(df[df["marks"] < 70]["name"].tolist())''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 5
add(id="pandas-missing-values", section=6, lib="pandas", title="Handle missing values", time="10 min",
 summary="Find empty cells, then either drop those rows or fill the gaps with a sensible value.",
 what="A **missing value** is a cell with no data. Pandas shows it as `NaN` (\"not a number\"), or `NaT` for dates. Cleaning means finding these gaps and deciding what to do with them.",
 why="Empty cells quietly give wrong answers. An average calculated over half-empty data may not describe reality, and some operations fail outright. Handling missing data is one of the most common data-cleaning jobs.",
 simple="Imagine a marks register where two students were absent and nothing was written. You can cross those rows out (**drop**), write 0 (**fill with a value**), or write the class average (**fill with the mean**). Each choice tells a different story, so you pick on purpose.",
 tech="`isna()` returns True for missing cells. `dropna()` returns a copy without rows that have gaps (use `subset=` to look only at some columns). `fillna(value)` returns a copy with the gaps replaced. A column with a missing number is stored as float, because `NaN` is a float.",
 table=dict(head=["Fill with", "Good when", "Code"], rows=[
   ["A fixed value", "A default makes sense (e.g. \"Unknown\")", "fillna(\"Unknown\")"],
   ["Mean", "Numbers are spread fairly evenly", "fillna(df[\"c\"].mean())"],
   ["Median", "A few extreme values would distort the mean", "fillna(df[\"c\"].median())"],
   ["Mode", "The column holds categories", "fillna(df[\"c\"].mode()[0])"]]),
 steps=["Count the gaps with `df.isna().sum()`.", "Decide: remove the rows or fill them.", "To remove: `dropna()` (optionally with `subset`).", "To fill: `fillna()` with a value, mean, median or mode.", "Assign the result back, because both methods return a new DataFrame."],
 blocks=[
  dict(title="Find the gaps", code=r'''import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "Kabir", "Isha"],
    "marks": [78, None, 66, None, 91],
    "city": ["Pune", "Delhi", None, "Pune", "Pune"],
})
print(df)
print(df.isna())
print(df.isna().sum())''', output=AUTO,
   lines=[("None", "Python's \"nothing\" value. Pandas stores it as `NaN` in number columns and as a missing value in text columns."),
          ("df.isna()", "A table of True/False: True wherever a cell is missing."),
          ("df.isna().sum()", "True counts as 1, so summing each column gives the number of gaps per column.")]),
  dict(title="Drop rows with gaps", code=r'''import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "Kabir", "Isha"],
    "marks": [78, None, 66, None, 91],
    "city": ["Pune", "Delhi", None, "Pune", "Pune"],
})
print(df.dropna())
print(df.dropna(subset=["marks"]))
print(len(df))''', output=AUTO,
   lines=[("df.dropna()", "Removes any row that has at least one gap, in any column."),
          ("df.dropna(subset=[\"marks\"])", "Looks only at the `marks` column, so a missing city doesn't remove a row."),
          ("len(df)", "`df` itself still has 5 rows. `dropna()` returned a new DataFrame and left the original alone.")]),
  dict(title="Fill gaps with a value", code=r'''import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "Kabir", "Isha"],
    "marks": [78, None, 66, None, 91],
    "city": ["Pune", "Delhi", None, "Pune", "Pune"],
})
filled = df.fillna({"marks": 0, "city": "Unknown"})
print(filled)''', output=AUTO,
   lines=[("df.fillna({\"marks\": 0, \"city\": \"Unknown\"})", "A dictionary lets each column have its own fill value. Columns not in the dictionary are left alone.")]),
  dict(title="Fill with mean, median or mode", code=r'''import pandas as pd

df = pd.DataFrame({
    "marks": [78, None, 66, None, 91],
    "city": ["Pune", "Delhi", None, "Pune", "Pune"],
})
mean = df["marks"].mean()
median = df["marks"].median()
common_city = df["city"].mode()[0]
print("mean:", mean, "median:", median, "mode:", common_city)

df["marks"] = df["marks"].fillna(mean)
df["city"] = df["city"].fillna(common_city)
print(df)''', output=AUTO,
   lines=[("df[\"marks\"].mean()", "Average of the existing marks. Missing values are skipped automatically."),
          ("df[\"city\"].mode()[0]", "`mode()` returns the most common value(s) as a Series, so `[0]` takes the first one."),
          ("df[\"marks\"] = df[\"marks\"].fillna(mean)", "Fills the gaps and assigns the result back into the column. This is the safe pattern for one column.")]),
 ],
 mistakes=["Using `inplace=True` on a single column, as in `df[\"marks\"].fillna(0, inplace=True)`. In current Pandas this does not change `df`. Assign the result back instead.",
           "Filling with 0 when 0 is a real value. A student who was absent did not necessarily score zero.",
           "Dropping rows blindly. If a third of your rows have a gap somewhere, `dropna()` throws away a third of your data."],
 use="Drop rows when only a few are affected and they aren't important. Fill when you want to keep every row: use the mean or median for numbers and the mode or a label such as \"Unknown\" for categories.",
 qa=[("How do you count missing values in each column?", "`df.isna().sum()`."),
     ("What is the difference between dropna() and fillna()?", "`dropna()` removes rows (or columns) that contain gaps. `fillna()` keeps them and replaces the gaps with a value."),
     ("When would you use the median instead of the mean?", "When a few extreme values would pull the mean away from a typical value, such as incomes or house prices."),
     ("Why does an integer column become float when it has a missing value?", "Because `NaN` is a floating-point value, so the whole column is stored as floats like `78.0`.")],
 tryit=dict(task="A `price` column holds 25, None, 30, None, 28. Fill the gaps with the median price and print the column.",
            hint="Compute `df[\"price\"].median()` first, then `fillna()` with it and assign the result back to the column.",
            solution=r'''import pandas as pd

df = pd.DataFrame({"price": [25, None, 30, None, 28]})
df["price"] = df["price"].fillna(df["price"].median())
print(df["price"])''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 6
add(id="pandas-clean-data", section=6, lib="pandas", title="Fix wrong formats, wrong values and duplicates", time="11 min",
 summary="Convert messy dates, spot and repair impossible values, and remove duplicate rows.",
 what="Besides empty cells, bad data comes in three more forms: values in the **wrong format** (like dates written three different ways), **wrong values** (like a typo that makes a price 4500 instead of 450) and **duplicate rows** (the same record entered twice).",
 why="Mixed formats stop you from sorting or calculating with dates. A single impossible value can wreck an average. Duplicates make totals too big. Fixing these makes every later result trustworthy.",
 simple="Think of tidying a shop's order book: rewrite every date the same way, correct the price someone wrote with an extra zero, and cross out the order that was written down twice.",
 tech="`pd.to_datetime(col, format=\"mixed\", errors=\"coerce\")` parses dates written in different styles and turns unreadable ones into `NaT`. You fix values with a rule such as `df.loc[condition, col] = new_value` or by filtering rows out. `duplicated()` marks repeats and `drop_duplicates()` removes them.",
 steps=["Convert date columns with `to_datetime()`.", "Drop or fill any `NaT` that conversion creates.", "Decide what values are possible, then correct or remove the ones outside that range.", "Check for repeats with `duplicated()`.", "Remove repeats with `drop_duplicates()`."],
 blocks=[
  dict(title="Wrong format: dates", code=r'''import pandas as pd

df = pd.DataFrame({
    "day": ["2025-01-05", "2025/01/06", "07 Jan 2025", "not a date"],
    "sales": [120, 90, 150, 60],
})
df["day"] = pd.to_datetime(df["day"], format="mixed", errors="coerce")
print(df)

df = df.dropna(subset=["day"])
print(df)''', output=AUTO,
   lines=[("format=\"mixed\"", "Lets each value use its own date style. Without it, Pandas guesses one style from the first value and may fail on the rest."),
          ("errors=\"coerce\"", "Instead of crashing on something that isn't a date, put `NaT` (Not a Time) there."),
          ("df.dropna(subset=[\"day\"])", "Removes the row whose date could not be read.")]),
  dict(title="Wrong values: fix or remove", code=r'''import pandas as pd

# 4500 is a typo for 450
df = pd.DataFrame({"item": ["pen", "book", "bag", "ruler"], "price": [10, 120, 4500, 15]})

fixed = df.copy()
fixed.loc[fixed["price"] > 1000, "price"] = 450
print(fixed)

removed = df[df["price"] <= 1000]
print(removed)''', output=AUTO,
   lines=[("fixed = df.copy()", "Makes an independent copy so we can try two fixes on the same data."),
          ("fixed.loc[fixed[\"price\"] > 1000, \"price\"] = 450", "`loc[rows, column] = value` changes only the rows that match the condition."),
          ("df[df[\"price\"] <= 1000]", "The other option: keep only rows with a believable price.")]),
  dict(title="Duplicates", code=r'''import pandas as pd

df = pd.DataFrame({
    "order": [101, 102, 102, 103, 103],
    "item": ["pen", "book", "book", "bag", "bag"],
    "qty": [2, 1, 1, 1, 3],
})
print(df.duplicated())
print(df.drop_duplicates())
print(df.drop_duplicates(subset="order").reset_index(drop=True))''', output=AUTO,
   lines=[("df.duplicated()", "True for a row that exactly repeats an earlier row. The first copy is False."),
          ("df.drop_duplicates()", "Removes rows that are identical in every column. Order 103 stays twice because its quantities differ (1 and 3)."),
          ("subset=\"order\"", "Compares only the `order` column, so each order number is kept once."),
          ("reset_index(drop=True)", "Renumbers the rows 0, 1, 2 after rows were removed, and drops the old numbers.")]),
 ],
 mistakes=["Treating a large value as wrong just because it looks big. First ask whether it is genuinely possible.",
           "Forgetting `errors=\"coerce\"`, so one bad date makes the whole conversion crash.",
           "Removing duplicates across every column when the real key is just one column (like an order number), or the opposite."],
 use="Run these checks right after loading a new dataset and before any analysis. Fix values you are sure about; remove rows when you can't be sure.",
 qa=[("How do you find duplicate rows?", "`df.duplicated()` returns True for each repeat. `df.duplicated().sum()` counts them."),
     ("What is NaT?", "\"Not a Time\": the missing-value marker for dates, like `NaN` for numbers."),
     ("How do you handle wrong values in a big dataset?", "Define a rule for valid values (a range, for example) and either replace or remove everything outside it, rather than editing rows one by one."),
     ("What does the subset argument do in drop_duplicates()?", "It limits the comparison to the listed columns, so rows count as duplicates when those columns match.")],
 tryit=dict(task="A DataFrame has columns `name` and `score` with rows (Asha, 80), (Ravi, 70) and (Asha, 80). Remove the duplicate row and print the result.",
            hint="Call `drop_duplicates()` and print what it returns.",
            solution=r'''import pandas as pd

df = pd.DataFrame({"name": ["Asha", "Ravi", "Asha"], "score": [80, 70, 80]})
print(df.drop_duplicates())''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 7
add(id="pandas-groupby", section=6, lib="pandas", title="Group and summarise data with groupby", time="10 min",
 summary="Split a table into groups, summarise each group (sum, mean, count) and put the answers back together.",
 what="`groupby()` splits a DataFrame into groups that share a value in some column, calculates a summary for each group, and combines the results into one small table.",
 why="Most business questions are about groups: total sales *per city*, average marks *per section*, orders *per month*. Writing this by hand needs loops and dictionaries. `groupby` does it in one line.",
 simple="Imagine a pile of shop bills. You sort them into one tray per city, then add up each tray. Splitting into trays is the **group** step, and adding is the **summary** step.",
 tech="`groupby` follows a *split-apply-combine* pattern. `df.groupby(\"city\")[\"amount\"].sum()` splits by `city`, applies `sum` to `amount` inside each group and combines the results into a Series indexed by city. `agg()` applies several summaries at once.",
 steps=["Choose the column to group by (`\"city\"`).", "Choose the column to summarise (`\"amount\"`).", "Choose the summary: `sum`, `mean`, `count`, `max`, `min`.", "Optionally use `agg()` for several summaries and `sort_values()` to rank them.", "Use `reset_index()` if you want the group labels back as a normal column."],
 blocks=[
  dict(title="Quick summaries of one column", code=r'''import pandas as pd

sales = pd.DataFrame({
    "city": ["Pune", "Delhi", "Pune", "Delhi", "Mumbai", "Pune"],
    "item": ["pen", "pen", "bag", "bag", "pen", "pen"],
    "amount": [200, 150, 900, 700, 300, 250],
})
print("Total:", sales["amount"].sum())
print("Average:", sales["amount"].mean())
print("Largest:", sales["amount"].max())
best = sales["amount"].idxmax()
print("Best row:", best, "->", sales.loc[best, "city"])''', output=AUTO,
   lines=[("sales[\"amount\"].sum()", "Adds up the whole column. `mean`, `max`, `min` and `count` work the same way."),
          ("sales[\"amount\"].idxmax()", "Returns the *label* of the row with the largest value, not the value itself."),
          ("sales.loc[best, \"city\"]", "Uses that label to look up the city on the best row.")]),
  dict(title="Group and summarise", code=r'''import pandas as pd

sales = pd.DataFrame({
    "city": ["Pune", "Delhi", "Pune", "Delhi", "Mumbai", "Pune"],
    "item": ["pen", "pen", "bag", "bag", "pen", "pen"],
    "amount": [200, 150, 900, 700, 300, 250],
})
print(sales.groupby("city")["amount"].sum())
print(sales.groupby("city")["amount"].mean())
print(sales.groupby("city")["amount"].count())''', output=AUTO,
   lines=[("sales.groupby(\"city\")", "Splits the rows into groups, one per city. Nothing is calculated yet."),
          ("[\"amount\"]", "Chooses the column to summarise inside each group."),
          (".sum() / .mean() / .count()", "The summary step. The result is a Series whose labels are the cities.")]),
  dict(title="Several summaries at once", code=r'''import pandas as pd

sales = pd.DataFrame({
    "city": ["Pune", "Delhi", "Pune", "Delhi", "Mumbai", "Pune"],
    "amount": [200, 150, 900, 700, 300, 250],
})
print(sales.groupby("city")["amount"].agg(["sum", "mean", "count"]))

report = sales.groupby("city").agg(total=("amount", "sum"), orders=("amount", "count"))
print(report.sort_values("total", ascending=False))''', output=AUTO,
   lines=[(".agg([\"sum\", \"mean\", \"count\"])", "Runs all three summaries and gives one column for each."),
          ("agg(total=(\"amount\", \"sum\"), orders=(\"amount\", \"count\"))", "Named aggregation: `new_name=(column, summary)`. It lets you choose the column names of the result."),
          ("sort_values(\"total\", ascending=False)", "Ranks the cities from the highest total to the lowest.")]),
  dict(title="Group by two columns", code=r'''import pandas as pd

sales = pd.DataFrame({
    "city": ["Pune", "Delhi", "Pune", "Delhi", "Mumbai", "Pune"],
    "item": ["pen", "pen", "bag", "bag", "pen", "pen"],
    "amount": [200, 150, 900, 700, 300, 250],
})
result = sales.groupby(["city", "item"])["amount"].sum()
print(result)
print(result.reset_index())''', output=AUTO,
   lines=[("groupby([\"city\", \"item\"])", "A list groups by the combination, such as Pune+pen and Pune+bag."),
          ("result.reset_index()", "Turns the group labels back into normal columns, giving a flat table that is easy to save or plot.")]),
 ],
 mistakes=["Forgetting the summary step. `df.groupby(\"city\")` alone only creates a grouping object and calculates nothing.",
           "Expecting the group labels to be a normal column. They become the index unless you call `reset_index()` or pass `as_index=False`.",
           "Not noticing that rows with a missing group value are left out of the result by default."],
 use="Use `groupby` whenever the question contains the word *per* or *by*: sales per city, average per class, count per category.",
 qa=[("What does groupby() do?", "It splits the data into groups by the values of one or more columns, applies a summary to each group and combines the results."),
     ("What does split-apply-combine mean?", "The three steps behind `groupby`: split the rows into groups, apply a function to each group, combine the answers into one result."),
     ("How do you calculate several statistics per group?", "Use `agg`, for example `df.groupby(\"city\")[\"amount\"].agg([\"sum\", \"mean\"])`."),
     ("How do you turn the group labels back into a column?", "Call `reset_index()` on the result, or use `as_index=False` in `groupby`.")],
 tryit=dict(task="Using sales with `item` = pen, pen, bag, bag, pen and `amount` = 200, 150, 900, 700, 300, print the average amount per item.",
            hint="Group by `item`, select `amount` and call `.mean()`.",
            solution=r'''import pandas as pd

sales = pd.DataFrame({
    "item": ["pen", "pen", "bag", "bag", "pen"],
    "amount": [200, 150, 900, 700, 300],
})
print(sales.groupby("item")["amount"].mean())''', output=AUTO),
 related=[])

# ---------------------------------------------------------------- 8
add(id="pandas-correlation", section=6, lib="pandas", title="Correlation: do two columns move together?", time="9 min",
 summary="Measure how strongly two numeric columns are related with `corr()`, and learn how to read the result honestly.",
 what="**Correlation** is a number between -1 and 1 that says how closely two columns move together. Pandas calculates it with `corr()`.",
 why="Before building a model or drawing conclusions, you want to know which columns are related. Do students who study more score higher? Does more screen time go with lower marks? Correlation gives a quick, numeric first answer.",
 simple="If every extra hour of study comes with a few more marks, the two numbers rise together. That is a correlation near +1. If more phone time comes with fewer marks, they move in opposite directions: near -1. If shoe size and marks have nothing to do with each other, it is near 0.",
 tech="`corr()` calculates the Pearson correlation coefficient, which measures **linear** relationships. +1 is a perfect positive line, -1 a perfect negative line and 0 means no linear relationship. Correlation does not prove one thing causes the other.",
 table=dict(head=["Value", "Meaning"], rows=[
   ["close to +1", "Both rise together"],
   ["close to -1", "One rises while the other falls"],
   ["close to 0", "No straight-line relationship"],
   ["above about 0.6 or below -0.6", "A fairly strong relationship (a common rule of thumb, not a law)"]]),
 steps=["Make sure the columns you compare are numeric.", "Use `a.corr(b)` for one pair, or `df.corr(numeric_only=True)` for every pair.", "Read the numbers: sign tells the direction, size tells the strength.", "Remember: a strong correlation is a clue, not proof of cause."],
 blocks=[
  dict(title="Correlation of two columns", code=r'''import pandas as pd

df = pd.DataFrame({
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "marks": [35, 42, 50, 55, 63, 70, 78, 84],
})
print(round(df["hours"].corr(df["marks"]), 3))''', output=AUTO,
   lines=[("df[\"hours\"].corr(df[\"marks\"])", "Correlation between two columns. A value close to 1 means that students who study more tend to score more."),
          ("round(..., 3)", "Rounds to 3 decimal places so the number is easy to read.")]),
  dict(title="The whole correlation table", code=r'''import pandas as pd

df = pd.DataFrame({
    "name": list("abcdefgh"),
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "marks": [35, 42, 50, 55, 63, 70, 78, 84],
    "phone_minutes": [200, 180, 170, 150, 140, 100, 90, 60],
    "shoe_size": [8, 6, 9, 7, 8, 6, 9, 7],
})
print(df.corr(numeric_only=True).round(2))''', output=AUTO,
   lines=[("df.corr(numeric_only=True)", "Calculates every pair of columns. `numeric_only=True` skips the text column `name`; without it, Pandas raises an error."),
          (".round(2)", "Two decimals keep the table readable. The diagonal is always 1, since every column matches itself perfectly.")]),
  dict(title="Find what relates most to marks", code=r'''import pandas as pd

df = pd.DataFrame({
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "marks": [35, 42, 50, 55, 63, 70, 78, 84],
    "phone_minutes": [200, 180, 170, 150, 140, 100, 90, 60],
    "shoe_size": [8, 6, 9, 7, 8, 6, 9, 7],
})
with_marks = df.corr()["marks"].drop("marks")
print(with_marks.round(2).sort_values())
print("Strongest link:", with_marks.abs().idxmax())''', output=AUTO,
   lines=[("df.corr()[\"marks\"]", "From the full table, takes only the column that shows how everything relates to `marks`."),
          (".drop(\"marks\")", "Removes `marks` compared with itself (always 1)."),
          (".abs().idxmax()", "`abs()` ignores the sign so strong negative links count too; `idxmax()` returns the name of the strongest one.")]),
 ],
 mistakes=["Concluding that one thing *causes* the other. Ice-cream sales and sunburn are correlated because of the weather, not because one causes the other.",
           "Running `df.corr()` on a table with text columns. Use `numeric_only=True` (or select numeric columns first).",
           "Trusting a correlation from a handful of rows, or one that comes from a single extreme value. Always look at the data too."],
 use="Use correlation for a quick first look at which numeric columns are related, for example when choosing features for a model or deciding what to chart next.",
 qa=[("What does corr() calculate?", "The Pearson correlation coefficient between numeric columns, from -1 to 1."),
     ("What does a correlation of -0.9 mean?", "A strong negative relationship: when one column goes up, the other tends to go down."),
     ("Does a high correlation mean one column causes the other?", "No. Correlation only says the two move together. Another factor, or chance, might explain it."),
     ("Why does df.corr() fail on a table with text columns?", "Correlation needs numbers. Pass `numeric_only=True` or select the numeric columns first.")],
 tryit=dict(task="Create two columns, `x` = 1, 2, 3, 4, 5 and `y` = 2, 4, 6, 8, 10, and print their correlation. Before you run it, predict the answer.",
            hint="`y` is exactly twice `x`, so it is a perfect straight line. Use `df[\"x\"].corr(df[\"y\"])`.",
            solution=r'''import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]})
print(round(df["x"].corr(df["y"]), 2))''', output=AUTO),
 related=[])
