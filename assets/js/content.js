/* Curriculum map: Python modules, the DSA roadmap and the interview libraries. */
window.PYDSA_PYTHON = [
  { id:"basics", n:"01", title:"Python Basics & Data Types", blurb:"What Python is, how it runs your code, and the data types you will use every day.",
    topics:["What Python is","How Python executes code (bytecode + PVM)","int, float, str, bool","list, tuple, set, dict","Mutable vs immutable","type() and len()"] },
  { id:"control-flow", n:"02", title:"Control Flow & Loops", blurb:"Make decisions and repeat work: the logic behind almost every program.",
    topics:["if / elif / else","for loop & range()","while loop","break, continue, pass","for … else","Nested loops"] },
  { id:"functions", n:"03", title:"Functions & Lambda", blurb:"Package logic into reusable pieces, then learn the shortcuts.",
    topics:["def, parameters, return","*args and **kwargs","Scope & the LEGB rule","lambda","map, filter, reduce","Passing functions as values"] },
  { id:"oop", n:"04", title:"Object-Oriented Programming", blurb:"Classes and objects, and why Django (and most big codebases) are built on them.",
    topics:["Class and object","__init__ and self","@classmethod vs @staticmethod","Inheritance & super()","Encapsulation","Polymorphism","Abstraction (abc)"] },
  { id:"files-exceptions", n:"05", title:"Files, Exceptions & Modules", blurb:"Read and write files safely, handle errors, and organise code into modules.",
    topics:["Reading & writing files","Why use with open()","try / except / finally","Multiple exceptions","Modules & packages","import styles"] }
];


window.PYDSA_DSA = [
  { level:0, title:"Programming Logic", blurb:"Build the control-flow and problem-solving habits every DSA topic depends on.", live:true,
    items:[
      {t:"Loops & conditions",u:"dsa-lesson.html?id=programming-logic-loops"},
      {t:"Functions",u:"dsa-lesson.html?id=programming-logic-functions"},
      {t:"Pattern printing",u:"dsa-lesson.html?id=programming-logic-patterns"}
    ] },
  { level:1, title:"Basic DSA", blurb:"Learn the core structures, complexity thinking, lookup, searching and sorting techniques.", live:true,
    items:[
      {t:"Complexity & Big O",u:"dsa-lesson.html?id=complexity-big-o"},
      {t:"Arrays",u:"dsa-lesson.html?id=arrays"},
      {t:"Strings",u:"dsa-lesson.html?id=strings"},
      {t:"Searching",u:"dsa-lesson.html?id=searching"},
      {t:"Sorting",u:"dsa-lesson.html?id=sorting"},
      {t:"Hashing",u:"dsa-lesson.html?id=hashing"}
    ] },
  { level:2, title:"Linear Structures", blurb:"Learn the structures that arrange data one item after another.", live:true,
    items:[
      {t:"Linked List",u:"dsa-lesson.html?id=linked-list"},
      {t:"Stack",u:"dsa-lesson.html?id=stack"},
      {t:"Queue",u:"dsa-lesson.html?id=queue"},
      {t:"Deque",u:"dsa-lesson.html?id=deque"}
    ] },
  { level:3, title:"Problem-Solving Patterns", blurb:"Recognise reusable techniques that solve whole families of interview problems.", live:true,
    items:[
      {t:"Two pointers",u:"dsa-lesson.html?id=two-pointers"},
      {t:"Sliding window",u:"dsa-lesson.html?id=sliding-window"},
      {t:"Prefix sum",u:"dsa-lesson.html?id=prefix-sum"},
      {t:"Binary search patterns",u:"dsa-lesson.html?id=binary-search-patterns"},
      {t:"Recursion",u:"dsa-lesson.html?id=recursion"},
      {t:"Backtracking",u:"dsa-lesson.html?id=backtracking"}
    ] },
  { level:4, title:"Non-linear DSA", blurb:"Move from linear structures to branching and networked data.", live:true,
    items:[
      {t:"Trees — foundations & types",u:"dsa-lesson.html?id=trees"},{t:"Tree program library (14)",u:"dsa-programs.html#Trees"},
      {t:"Binary search tree",u:"dsa-lesson.html?id=binary-search-tree"},{t:"AVL rotation program",u:"dsa-structure-program.html?id=tree-13-avl-rotation"},
      {t:"Heap / priority queue",u:"dsa-lesson.html?id=heap-priority-queue"},
      {t:"Graphs — representation & traversal",u:"dsa-lesson.html?id=graphs"},{t:"Graph program library (17)",u:"dsa-programs.html#Graphs"},
      {t:"Trie",u:"dsa-lesson.html?id=trie"}
    ] },
  { level:5, title:"Advanced Algorithms", blurb:"Learn the major algorithmic ideas used in harder interview and competitive-programming problems.", live:true,
    items:[
      {t:"Greedy",u:"dsa-lesson.html?id=greedy"},
      {t:"Divide & conquer",u:"dsa-lesson.html?id=divide-and-conquer"},
      {t:"Dynamic programming",u:"dsa-lesson.html?id=dynamic-programming"},
      {t:"Bit manipulation",u:"dsa-lesson.html?id=bit-manipulation"},
      {t:"Graph algorithms",u:"dsa-lesson.html?id=graph-algorithms"}
    ] }
];


/* Curated top interview problem path. Reuses the existing coding-problem library. */


window.PYDSA_INTERVIEW = [
  { id:"python-interview", title:"Python Interview Questions", blurb:"Practice Python basics, data structures, functions, OOP, exceptions, files and common interview concepts.", c:"blue", status:"30 questions", u:"python-interview.html" },
  { id:"dsa-interview",    title:"DSA Interview Questions", blurb:"Explain-it-out-loud questions for the DSA concepts already covered on this site.", c:"teal", status:"30 questions", u:"dsa-interview.html" },
  { id:"coding-problems",  title:"Coding Problems (Easy → Hard)", blurb:"Original explanations for the most-asked problems, each linking to practice on LeetCode.", c:"orange", status:"30 problems", u:"coding-problems.html" },
  { id:"patterns",         title:"Problem-Solving Patterns", blurb:"Recognise which pattern a question wants before you start coding.", c:"purple", status:"9 patterns", u:"patterns.html" },
  { id:"django-interview", title:"Django & Web Interview", blurb:"Practice Django, ORM, authentication, REST and web-development interview questions.", c:"blue", status:"30 questions", u:"django-interview.html" },
  { id:"hr",               title:"HR & Behavioural", blurb:"Practise tell-me-about-yourself, projects, teamwork, strengths, weaknesses and career questions.", c:"orange", status:"30 questions", u:"hr-interview.html" }
];
