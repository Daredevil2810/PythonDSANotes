window.PYDSA_DSA_STRUCTURE_PROGRAMS = [
  {
    "id": "tree-01-binary-tree",
    "category": "Trees",
    "title": "Build a Binary Tree",
    "difficulty": "easy",
    "concept": "A binary tree gives each node at most a left and a right child.",
    "why": "It is the base representation for traversals, BSTs, heaps, expression trees, and recursive tree problems.",
    "approach": "Binary trees are about shape first; ordering comes later.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\nroot = Node(1, Node(2), Node(3))\nroot.left.left = Node(4)\nprint(root.value, root.left.value, root.right.value)",
    "output": "1 2 3",
    "lines": [
      [
        "self.left = left",
        "Stores the left child."
      ],
      [
        "self.right = right",
        "Stores the right child."
      ]
    ],
    "dryRun": "1 is the root; 2 and 3 are its children; 4 is below 2.",
    "complexity": "O(1) per link; O(n) space for n nodes.",
    "mistakes": [
      "Assuming every binary tree is a BST.",
      "Dereferencing a missing child."
    ],
    "useWhen": "Use for any hierarchy where a node has at most two children.",
    "interview": [
      [
        "Binary tree vs BST?",
        "A BST adds an ordering rule; a binary tree does not."
      ]
    ],
    "practice": "Build a six-node tree by hand."
  },
  {
    "id": "tree-02-preorder",
    "category": "Trees",
    "title": "Preorder Traversal",
    "difficulty": "easy",
    "concept": "Preorder is root → left → right.",
    "why": "It is useful when a parent must be processed before descendants and for serialization patterns.",
    "approach": "Remember: root, left, right.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef preorder(node):\n    if not node: return\n    print(node.value, end=\" \")\n    preorder(node.left)\n    preorder(node.right)\n\nroot = Node(1, Node(2), Node(3))\npreorder(root)",
    "output": "1 2 3 ",
    "lines": [
      [
        "print(node.value, end=\" \")",
        "Processes the root first."
      ],
      [
        "preorder(node.left)",
        "Then visits the whole left subtree."
      ]
    ],
    "dryRun": "Visit 1, then 2, then return and visit 3.",
    "complexity": "O(n) time; O(h) recursion space.",
    "mistakes": [
      "Missing the base case.",
      "Putting the print after recursive calls."
    ],
    "useWhen": "Use for root-before-children processing.",
    "interview": [
      [
        "Root-left-right is which traversal?",
        "Preorder."
      ]
    ],
    "practice": "Write iterative preorder using a stack."
  },
  {
    "id": "tree-03-inorder",
    "category": "Trees",
    "title": "Inorder Traversal",
    "difficulty": "easy",
    "concept": "Inorder is left → root → right.",
    "why": "For a BST, inorder returns values in sorted order.",
    "approach": "Think: left, root, right.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef inorder(node):\n    if not node: return\n    inorder(node.left)\n    print(node.value, end=\" \")\n    inorder(node.right)\n\nroot = Node(2, Node(1), Node(3))\ninorder(root)",
    "output": "1 2 3 ",
    "lines": [
      [
        "inorder(node.left)",
        "Finishes the left subtree first."
      ],
      [
        "print(node.value, end=\" \")",
        "Processes the root between both subtrees."
      ]
    ],
    "dryRun": "1 prints before 2, and 3 prints after 2.",
    "complexity": "O(n) time; O(h) recursion space.",
    "mistakes": [
      "Assuming inorder is sorted for every binary tree."
    ],
    "useWhen": "Use for sorted traversal of a BST.",
    "interview": [
      [
        "Why is BST inorder sorted?",
        "BST ordering puts smaller values left and larger values right."
      ]
    ],
    "practice": "Return the inorder values as a list."
  },
  {
    "id": "tree-04-postorder",
    "category": "Trees",
    "title": "Postorder Traversal",
    "difficulty": "easy",
    "concept": "Postorder is left → right → root.",
    "why": "It is useful when children must be processed before their parent.",
    "approach": "Children first, parent last.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef postorder(node):\n    if not node: return\n    postorder(node.left)\n    postorder(node.right)\n    print(node.value, end=\" \")\n\nroot = Node(1, Node(2), Node(3))\npostorder(root)",
    "output": "2 3 1 ",
    "lines": [
      [
        "postorder(node.right)",
        "Processes the right subtree before the parent."
      ],
      [
        "print(node.value, end=\" \")",
        "Processes the parent last."
      ]
    ],
    "dryRun": "2 and 3 are processed before 1.",
    "complexity": "O(n) time; O(h) recursion space.",
    "mistakes": [
      "Processing the root too early."
    ],
    "useWhen": "Use for bottom-up calculations and expression trees.",
    "interview": [
      [
        "Left-right-root is which traversal?",
        "Postorder."
      ]
    ],
    "practice": "Compute subtree sizes using postorder."
  },
  {
    "id": "tree-05-level-order",
    "category": "Trees",
    "title": "Level Order Traversal",
    "difficulty": "easy",
    "concept": "Level order is tree BFS: process nodes by depth using a queue.",
    "why": "It is the natural technique for level-based questions and minimum depth.",
    "approach": "Tree BFS = queue + levels.",
    "code": "from collections import deque\n\nclass Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\n\ndef level_order(root):\n    if not root: return []\n    q = deque([root]); result=[]\n    while q:\n        node=q.popleft(); result.append(node.value)\n        if node.left: q.append(node.left)\n        if node.right: q.append(node.right)\n    return result\n\nroot=Node(1,Node(2),Node(3,Node(4),Node(5)))\nprint(level_order(root))",
    "output": "[1, 2, 3, 4, 5]",
    "lines": [
      [
        "q.popleft()",
        "Takes the oldest pending node."
      ],
      [
        "q.append(node.left)",
        "Schedules the next level."
      ]
    ],
    "dryRun": "1 is processed, then 2 and 3, then 4 and 5.",
    "complexity": "O(n) time; O(w) space where w is maximum width.",
    "mistakes": [
      "Using pop(0) on a list."
    ],
    "useWhen": "Use for levels, minimum depth, and nearest-by-distance tree problems.",
    "interview": [
      [
        "Which structure powers level order?",
        "A queue."
      ]
    ],
    "practice": "Return a list for each level."
  },
  {
    "id": "tree-06-height",
    "category": "Trees",
    "title": "Maximum Depth / Height",
    "difficulty": "easy",
    "concept": "Maximum depth is one plus the deeper child depth, with empty tree depth 0.",
    "why": "Height is used by balance, diameter, recursion, and complexity reasoning.",
    "approach": "State your height convention explicitly.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef height(node):\n    if not node: return 0\n    return 1 + max(height(node.left), height(node.right))\n\nroot=Node(1,Node(2),Node(3,Node(4)))\nprint(height(root))",
    "output": "3",
    "lines": [
      [
        "return 1 + max(...)",
        "Adds the current node to the deeper child path."
      ]
    ],
    "dryRun": "The longest path is 1 → 3 → 4, so height is 3.",
    "complexity": "O(n) time; O(h) recursion space.",
    "mistakes": [
      "Mixing edge-count and node-count definitions."
    ],
    "useWhen": "Use for depth, balance, diameter, and tree height questions.",
    "interview": [
      [
        "Depth vs height?",
        "Depth measures down from the root; height measures down from a node to its deepest descendant."
      ]
    ],
    "practice": "Rewrite it to count edges instead."
  },
  {
    "id": "tree-07-leaf-count",
    "category": "Trees",
    "title": "Count Leaf Nodes",
    "difficulty": "easy",
    "concept": "A leaf has no left and no right child.",
    "why": "It is a simple example of recursive structural decomposition.",
    "approach": "Base case + combine is the recurring tree pattern.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef leaves(node):\n    if not node: return 0\n    if not node.left and not node.right: return 1\n    return leaves(node.left)+leaves(node.right)\n\nroot=Node(1,Node(2),Node(3,Node(4),Node(5)))\nprint(leaves(root))",
    "output": "3",
    "lines": [
      [
        "if not node.left and not node.right",
        "Identifies a leaf."
      ],
      [
        "return leaves(node.left)+leaves(node.right)",
        "Combines both subtree counts."
      ]
    ],
    "dryRun": "Leaves are 2, 4, and 5.",
    "complexity": "O(n) time; O(h) space.",
    "mistakes": [
      "Counting internal nodes as leaves."
    ],
    "useWhen": "Use when a question asks about terminal nodes.",
    "interview": [
      [
        "What is a leaf?",
        "A node with no children."
      ]
    ],
    "practice": "Count internal nodes."
  },
  {
    "id": "tree-08-diameter",
    "category": "Trees",
    "title": "Binary Tree Diameter",
    "difficulty": "medium",
    "concept": "The diameter is the longest path between two nodes; here it is measured in edges.",
    "why": "It is a classic example of returning subtree height while updating a global answer.",
    "approach": "This is postorder tree DP.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef diameter(root):\n    best=0\n    def height(node):\n        nonlocal best\n        if not node: return 0\n        left=height(node.left); right=height(node.right)\n        best=max(best,left+right)\n        return 1+max(left,right)\n    height(root)\n    return best\n\nroot=Node(1,Node(2,Node(4),Node(5)),Node(3))\nprint(diameter(root))",
    "output": "3",
    "lines": [
      [
        "best=max(best,left+right)",
        "Checks a path passing through the current node."
      ],
      [
        "return 1+max(left,right)",
        "Returns height to the parent."
      ]
    ],
    "dryRun": "At node 1, the longest path is 4 → 2 → 1 → 3: three edges.",
    "complexity": "O(n) time; O(h) space.",
    "mistakes": [
      "Recomputing height for every node, causing O(n²)."
    ],
    "useWhen": "Use for longest-path-in-tree problems.",
    "interview": [
      [
        "Why one DFS?",
        "Height and diameter can be computed together."
      ]
    ],
    "practice": "Return the actual diameter path."
  },
  {
    "id": "tree-09-balanced",
    "category": "Trees",
    "title": "Check Balanced Tree",
    "difficulty": "medium",
    "concept": "A height-balanced binary tree keeps child heights within one at every node.",
    "why": "Balance keeps search-tree height small and is a core invariant in AVL-style trees.",
    "approach": "Sentinel returns let recursion carry multiple kinds of information.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef balanced(root):\n    def h(node):\n        if not node: return 0\n        a=h(node.left)\n        if a==-1: return -1\n        b=h(node.right)\n        if b==-1 or abs(a-b)>1: return -1\n        return 1+max(a,b)\n    return h(root)!=-1\n\nroot=Node(1,Node(2),Node(3,Node(4)))\nprint(balanced(root))",
    "output": "True",
    "lines": [
      [
        "abs(a-b)>1",
        "Checks the balance condition."
      ],
      [
        "h(root)!=-1",
        "Converts the sentinel into a Boolean."
      ]
    ],
    "dryRun": "Each subtree returns its height unless it finds an imbalance, represented by -1.",
    "complexity": "O(n) time; O(h) space.",
    "mistakes": [
      "Recomputing heights separately at every node."
    ],
    "useWhen": "Use when a tree must remain shallow.",
    "interview": [
      [
        "Why does balance matter?",
        "It keeps height near O(log n), improving many operations."
      ]
    ],
    "practice": "Create a clearly unbalanced chain."
  },
  {
    "id": "tree-10-bst-search",
    "category": "Trees",
    "title": "BST Search",
    "difficulty": "easy",
    "concept": "A BST stores smaller values left and larger values right.",
    "why": "The ordering lets each comparison discard one whole subtree.",
    "approach": "Always mention the balance assumption.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef contains(root,target):\n    while root:\n        if root.value==target: return True\n        root=root.left if target<root.value else root.right\n    return False\n\nroot=Node(8,Node(3,Node(1),Node(6)),Node(10))\nprint(contains(root,6))\nprint(contains(root,7))",
    "output": "True\nFalse",
    "lines": [
      [
        "root=root.left if target<root.value else root.right",
        "Chooses the only possible side."
      ]
    ],
    "dryRun": "For 6: left from 8, right from 3, then found. 7 ends at a missing child.",
    "complexity": "O(h); O(log n) when balanced, O(n) when skewed.",
    "mistakes": [
      "Using BST search on an arbitrary binary tree."
    ],
    "useWhen": "Use for ordered dynamic data.",
    "interview": [
      [
        "Why can BST search be O(n)?",
        "A skewed tree can become a chain."
      ]
    ],
    "practice": "Write recursive search."
  },
  {
    "id": "tree-11-bst-insert",
    "category": "Trees",
    "title": "BST Insertion",
    "difficulty": "medium",
    "concept": "BST insertion places a value while preserving the ordering invariant.",
    "why": "It is the fundamental update operation for an ordinary BST.",
    "approach": "Invariant matters more than shape.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef insert(root,value):\n    if not root: return Node(value)\n    if value<root.value: root.left=insert(root.left,value)\n    else: root.right=insert(root.right,value)\n    return root\n\nroot=None\nfor x in [8,3,10,6]: root=insert(root,x)\nprint(root.left.right.value)",
    "output": "6",
    "lines": [
      [
        "if not root",
        "Finds the insertion position."
      ],
      [
        "root.left=insert(root.left,value)",
        "Continues on the smaller side."
      ]
    ],
    "dryRun": "8 becomes root, 3 left, 10 right, and 6 becomes right child of 3.",
    "complexity": "O(h) per insertion.",
    "mistakes": [
      "No duplicate policy.",
      "Assuming insertion balances the tree."
    ],
    "useWhen": "Use to maintain an ordered BST.",
    "interview": [
      [
        "Does ordinary BST insertion guarantee O(log n)?",
        "No. Only a balanced BST guarantees logarithmic height."
      ]
    ],
    "practice": "Implement duplicate rejection."
  },
  {
    "id": "tree-12-bst-delete",
    "category": "Trees",
    "title": "BST Deletion",
    "difficulty": "medium",
    "concept": "BST deletion has leaf, one-child, and two-child cases.",
    "why": "It forces you to preserve the BST invariant during structural changes.",
    "approach": "Draw the three cases before coding.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef delete(root,key):\n    if not root: return None\n    if key<root.value: root.left=delete(root.left,key)\n    elif key>root.value: root.right=delete(root.right,key)\n    else:\n        if not root.left: return root.right\n        if not root.right: return root.left\n        s=root.right\n        while s.left: s=s.left\n        root.value=s.value\n        root.right=delete(root.right,s.value)\n    return root\n\nroot=Node(5,Node(3),Node(8,Node(6),Node(9)))\nroot=delete(root,8)\nprint(root.right.value)",
    "output": "9",
    "lines": [
      [
        "if not root.left: return root.right",
        "Handles zero/one-child cases."
      ],
      [
        "s=root.right",
        "Starts the successor search."
      ],
      [
        "root.value=s.value",
        "Copies the smallest right-subtree value."
      ]
    ],
    "dryRun": "Deleting 8 uses successor 9, then removes the original 9.",
    "complexity": "O(h).",
    "mistakes": [
      "Forgetting the successor must also be removed."
    ],
    "useWhen": "Use for mutable BSTs.",
    "interview": [
      [
        "Why successor?",
        "It is the smallest value larger than the deleted node."
      ]
    ],
    "practice": "Delete a leaf, one-child node, and two-child node."
  },
  {
    "id": "tree-13-avl-rotation",
    "category": "Trees",
    "title": "AVL Rotation — LL Case",
    "difficulty": "hard",
    "concept": "AVL trees rebalance after updates using rotations. This program demonstrates a right rotation for a left-left imbalance.",
    "why": "Balanced height keeps search and updates O(log n).",
    "approach": "Learn rotations as local shape transformations.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\n        self.height = 1\n\ndef h(n): return n.height if n else 0\ndef update(n): n.height=1+max(h(n.left),h(n.right))\ndef rotate_right(y):\n    x=y.left; middle=x.right\n    x.right=y; y.left=middle\n    update(y); update(x)\n    return x\n\ny=Node(30); y.left=Node(20); y.left.left=Node(10)\nupdate(y.left); update(y)\ny=rotate_right(y)\nprint(y.value,y.left.value,y.right.value)",
    "output": "20 10 30",
    "lines": [
      [
        "x=y.left",
        "The left child becomes subtree root."
      ],
      [
        "x.right=y",
        "The old root moves right."
      ]
    ],
    "dryRun": "30-20-10 is left-heavy; one right rotation produces 20 with children 10 and 30.",
    "complexity": "Rotation O(1); AVL operations O(log n).",
    "mistakes": [
      "Wrong rotation direction.",
      "Not updating heights."
    ],
    "useWhen": "Use balanced BST concepts.",
    "interview": [
      [
        "What are the four AVL imbalance cases?",
        "LL, RR, LR, and RL."
      ]
    ],
    "practice": "Implement the mirrored RR rotation."
  },
  {
    "id": "tree-14-serialize",
    "category": "Trees",
    "title": "Serialize & Deserialize Tree",
    "difficulty": "hard",
    "concept": "Serialization stores tree values and null markers so the exact shape can be reconstructed.",
    "why": "It teaches explicit structural representation and appears in interview/system problems.",
    "approach": "Serialization is about preserving structure, not just values.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\ndef serialize(root):\n    out=[]\n    def dfs(n):\n        if not n: out.append('#'); return\n        out.append(str(n.value)); dfs(n.left); dfs(n.right)\n    dfs(root); return ','.join(out)\n\ndef deserialize(data):\n    it=iter(data.split(','))\n    def dfs():\n        x=next(it)\n        if x=='#': return None\n        return Node(int(x),dfs(),dfs())\n    return dfs()\n\nroot=Node(1,Node(2),Node(3))\ns=serialize(root); copy=deserialize(s)\nprint(s,copy.right.value)",
    "output": "1,2,#,#,3,#,# 3",
    "lines": [
      [
        "out.append('#')",
        "Records a missing child."
      ],
      [
        "Node(int(x),dfs(),dfs())",
        "Rebuilds both child positions recursively."
      ]
    ],
    "dryRun": "The preorder stream records every value plus null children, preserving shape.",
    "complexity": "O(n) time; O(n) storage including output.",
    "mistakes": [
      "Omitting null markers."
    ],
    "useWhen": "Use for storage, transfer, caching, and tree reconstruction.",
    "interview": [
      [
        "Why are null markers required?",
        "Values alone do not uniquely identify the tree shape."
      ]
    ],
    "practice": "Support duplicate and negative values."
  },
  {
    "id": "graph-01-adjacency-list",
    "category": "Graphs",
    "title": "Adjacency List",
    "difficulty": "easy",
    "concept": "Store each vertex with its neighbors.",
    "why": "It is the standard sparse-graph representation for BFS and DFS.",
    "approach": "Choose representation before choosing the algorithm.",
    "code": "graph={\"A\":[\"B\",\"C\"],\"B\":[\"A\",\"D\"],\"C\":[\"A\"],\"D\":[\"B\"]}\nfor u in graph: print(u,graph[u])",
    "output": "A ['B', 'C']\nB ['A', 'D']\nC ['A']\nD ['B']",
    "lines": [
      [
        "graph[\"A\"]",
        "Returns A’s neighbors."
      ]
    ],
    "dryRun": "A has edges to B and C; B connects A and D.",
    "complexity": "O(V+E) space.",
    "mistakes": [
      "Forgetting reverse edges in undirected graphs."
    ],
    "useWhen": "Use for sparse graphs and traversals.",
    "interview": [
      [
        "List vs matrix?",
        "List uses O(V+E) space; matrix uses O(V²)."
      ]
    ],
    "practice": "Convert an edge list into a list."
  },
  {
    "id": "graph-02-adjacency-matrix",
    "category": "Graphs",
    "title": "Adjacency Matrix",
    "difficulty": "easy",
    "concept": "Store graph connectivity in a V×V table.",
    "why": "It gives O(1) edge-existence checks and suits dense/small graphs.",
    "approach": "Directed vs undirected changes how edges are inserted.",
    "code": "n=4\nedges=[(0,1),(0,2),(2,3)]\nm=[[0]*n for _ in range(n)]\nfor u,v in edges: m[u][v]=m[v][u]=1\nprint(m[0][2]); print(m[1][3])",
    "output": "1\n0",
    "lines": [
      [
        "m[u][v]=m[v][u]=1",
        "Marks both directions for an undirected edge."
      ]
    ],
    "dryRun": "0-2 exists; 1-3 does not.",
    "complexity": "O(V²) space; O(1) edge lookup.",
    "mistakes": [
      "Using it for a huge sparse graph."
    ],
    "useWhen": "Use when constant edge lookup or density matters.",
    "interview": [
      [
        "When is matrix preferable?",
        "Dense graphs or frequent direct edge queries."
      ]
    ],
    "practice": "Represent a directed matrix without mirroring."
  },
  {
    "id": "graph-03-bfs",
    "category": "Graphs",
    "title": "Breadth-First Search",
    "difficulty": "easy",
    "concept": "BFS explores by distance layers using a queue.",
    "why": "It gives shortest paths in unweighted graphs and supports level-based exploration.",
    "approach": "Queue = breadth.",
    "code": "from collections import deque\ng={\"A\":[\"B\",\"C\"],\"B\":[\"D\"],\"C\":[\"D\"],\"D\":[]}\nq=deque([\"A\"]); seen={\"A\"}; order=[]\nwhile q:\n u=q.popleft(); order.append(u)\n for v in g[u]:\n  if v not in seen: seen.add(v); q.append(v)\nprint(order)",
    "output": "['A', 'B', 'C', 'D']",
    "lines": [
      [
        "q.popleft()",
        "Processes the oldest discovered vertex."
      ],
      [
        "seen.add(v)",
        "Prevents repeated discovery."
      ]
    ],
    "dryRun": "A is layer 0, B/C layer 1, D layer 2.",
    "complexity": "O(V+E) time; O(V) space.",
    "mistakes": [
      "Marking visited too late."
    ],
    "useWhen": "Use for unweighted shortest paths and level exploration.",
    "interview": [
      [
        "Why shortest?",
        "BFS discovers vertices in nondecreasing edge distance."
      ]
    ],
    "practice": "Track parents and reconstruct the path."
  },
  {
    "id": "graph-04-dfs",
    "category": "Graphs",
    "title": "Depth-First Search",
    "difficulty": "easy",
    "concept": "DFS follows one branch deeply before backtracking.",
    "why": "It is the base for components, cycle detection, topological sorting, bridges, and SCCs.",
    "approach": "Stack = depth.",
    "code": "g={\"A\":[\"B\",\"C\"],\"B\":[\"D\"],\"C\":[\"D\"],\"D\":[]}\nseen=set(); order=[]\ndef dfs(u):\n seen.add(u); order.append(u)\n for v in g[u]:\n  if v not in seen: dfs(v)\ndfs(\"A\"); print(order)",
    "output": "['A', 'B', 'D', 'C']",
    "lines": [
      [
        "dfs(v)",
        "Finishes one branch before moving to the next."
      ]
    ],
    "dryRun": "A→B→D, backtrack, then C.",
    "complexity": "O(V+E) time; O(V) space.",
    "mistakes": [
      "No visited set in cyclic graphs.",
      "Recursion depth on huge graphs."
    ],
    "useWhen": "Use for structural graph algorithms.",
    "interview": [
      [
        "BFS vs DFS?",
        "BFS is layer-first; DFS is branch-first."
      ]
    ],
    "practice": "Write iterative DFS."
  },
  {
    "id": "graph-05-components",
    "category": "Graphs",
    "title": "Connected Components",
    "difficulty": "easy",
    "concept": "A component is a maximal reachable group in an undirected graph.",
    "why": "It identifies independent groups or islands.",
    "approach": "The outer loop is essential.",
    "code": "g={1:[2],2:[1],3:[4],4:[3],5:[]}\nseen=set(); count=0\ndef dfs(u):\n seen.add(u)\n for v in g[u]:\n  if v not in seen: dfs(v)\nfor u in g:\n if u not in seen: count+=1; dfs(u)\nprint(count)",
    "output": "3",
    "lines": [
      [
        "if u not in seen",
        "A new traversal means a new component."
      ]
    ],
    "dryRun": "1-2, 3-4, and 5 are three components.",
    "complexity": "O(V+E).",
    "mistakes": [
      "Only starting DFS once."
    ],
    "useWhen": "Use for groups and connectivity.",
    "interview": [
      [
        "How many components?",
        "Start a traversal from every unvisited vertex."
      ]
    ],
    "practice": "Return each component’s members."
  },
  {
    "id": "graph-06-cycle-undirected",
    "category": "Graphs",
    "title": "Cycle Detection — Undirected",
    "difficulty": "medium",
    "concept": "In undirected DFS, a visited neighbor that is not the parent proves a cycle.",
    "why": "It distinguishes trees from cyclic networks.",
    "approach": "Parent tracking is the key.",
    "code": "g={1:[2,3],2:[1,3],3:[1,2]}; seen=set()\ndef cycle(u,p):\n seen.add(u)\n for v in g[u]:\n  if v not in seen:\n   if cycle(v,u): return True\n  elif v!=p: return True\n return False\nprint(cycle(1,-1))",
    "output": "True",
    "lines": [
      [
        "v!=p",
        "Ignores the edge used to enter the current node."
      ]
    ],
    "dryRun": "3 sees already-visited 1, which is not its parent, so a cycle exists.",
    "complexity": "O(V+E).",
    "mistakes": [
      "Using directed-graph cycle logic."
    ],
    "useWhen": "Use to validate undirected trees and networks.",
    "interview": [
      [
        "Tree condition?",
        "Connected + acyclic."
      ]
    ],
    "practice": "Handle disconnected graphs too."
  },
  {
    "id": "graph-07-cycle-directed",
    "category": "Graphs",
    "title": "Cycle Detection — Directed",
    "difficulty": "medium",
    "concept": "In directed DFS, an edge to a currently active node is a cycle.",
    "why": "It is essential for dependency validation.",
    "approach": "Three states: unvisited, visiting, finished.",
    "code": "g={\"A\":[\"B\"],\"B\":[\"C\"],\"C\":[\"A\"]}; state={}\ndef dfs(u):\n state[u]=1\n for v in g[u]:\n  if state.get(v,0)==1: return True\n  if state.get(v,0)==0 and dfs(v): return True\n state[u]=2; return False\nprint(dfs(\"A\"))",
    "output": "True",
    "lines": [
      [
        "state[u]=1",
        "Marks u as active on the recursion path."
      ],
      [
        "state[u]=2",
        "Marks u finished."
      ]
    ],
    "dryRun": "C points back to active A, proving a directed cycle.",
    "complexity": "O(V+E).",
    "mistakes": [
      "Using the undirected parent rule."
    ],
    "useWhen": "Use for prerequisite/dependency cycles.",
    "interview": [
      [
        "What is a DAG?",
        "A directed acyclic graph."
      ]
    ],
    "practice": "Detect a cycle using Kahn’s algorithm."
  },
  {
    "id": "graph-08-bipartite",
    "category": "Graphs",
    "title": "Bipartite Check",
    "difficulty": "medium",
    "concept": "A bipartite graph can be colored with two colors so every edge crosses colors.",
    "why": "It models two-group constraints and conflict graphs.",
    "approach": "Bipartite = two-colorable.",
    "code": "from collections import deque\ng={0:[1,3],1:[0,2],2:[1,3],3:[0,2]}; color={}\nfor s in g:\n if s in color: continue\n color[s]=0; q=deque([s])\n while q:\n  u=q.popleft()\n  for v in g[u]:\n   if v not in color: color[v]=1-color[u]; q.append(v)\n   elif color[v]==color[u]: print(False); raise SystemExit\nprint(True)",
    "output": "True",
    "lines": [
      [
        "color[v]=1-color[u]",
        "Assigns the opposite group."
      ],
      [
        "color[v]==color[u]",
        "Detects a conflict."
      ]
    ],
    "dryRun": "The four-cycle alternates colors 0 and 1, so it is bipartite.",
    "complexity": "O(V+E).",
    "mistakes": [
      "Checking only one component."
    ],
    "useWhen": "Use for two-group constraints and odd-cycle detection.",
    "interview": [
      [
        "What breaks bipartiteness?",
        "An odd-length cycle."
      ]
    ],
    "practice": "Return the two color groups."
  },
  {
    "id": "graph-09-topological",
    "category": "Graphs",
    "title": "Topological Sort — Kahn",
    "difficulty": "medium",
    "concept": "A topological order places every prerequisite before its dependent node.",
    "why": "It models build systems, courses, and dependency graphs.",
    "approach": "Kahn = indegree + queue.",
    "code": "from collections import deque\ng={\"A\":[\"C\"],\"B\":[\"C\"],\"C\":[\"D\"],\"D\":[]}; indeg={u:0 for u in g}\nfor u in g:\n for v in g[u]: indeg[v]+=1\nq=deque([u for u in g if indeg[u]==0]); order=[]\nwhile q:\n u=q.popleft(); order.append(u)\n for v in g[u]:\n  indeg[v]-=1\n  if indeg[v]==0:q.append(v)\nprint(order)",
    "output": "['A', 'B', 'C', 'D']",
    "lines": [
      [
        "indeg[v]+=1",
        "Counts prerequisites."
      ],
      [
        "indeg[v]-=1",
        "Removes a completed prerequisite."
      ]
    ],
    "dryRun": "A and B become ready first; C then D follow.",
    "complexity": "O(V+E).",
    "mistakes": [
      "Using it on cyclic input without checking output size."
    ],
    "useWhen": "Use on DAG dependencies.",
    "interview": [
      [
        "Cycle detection with Kahn?",
        "If fewer than V nodes are output, a cycle exists."
      ]
    ],
    "practice": "Create a cycle and detect it."
  },
  {
    "id": "graph-10-unweighted-shortest",
    "category": "Graphs",
    "title": "Shortest Path — Unweighted",
    "difficulty": "medium",
    "concept": "BFS gives minimum edge count when every edge has equal cost.",
    "why": "It is the correct shortest-path tool for unweighted graphs.",
    "approach": "First discovery is optimal in unweighted BFS.",
    "code": "from collections import deque\ng={\"A\":[\"B\",\"C\"],\"B\":[\"D\"],\"C\":[\"D\"],\"D\":[]}; dist={\"A\":0}; q=deque([\"A\"])\nwhile q:\n u=q.popleft()\n for v in g[u]:\n  if v not in dist: dist[v]=dist[u]+1; q.append(v)\nprint(dist[\"D\"])",
    "output": "2",
    "lines": [
      [
        "dist[v]=dist[u]+1",
        "Adds one edge to the distance."
      ]
    ],
    "dryRun": "D is two edges from A.",
    "complexity": "O(V+E).",
    "mistakes": [
      "Using BFS for weighted edges."
    ],
    "useWhen": "Use for minimum number of edges.",
    "interview": [
      [
        "How reconstruct path?",
        "Store a parent for each first discovery."
      ]
    ],
    "practice": "Print the actual shortest path."
  },
  {
    "id": "graph-11-dijkstra",
    "category": "Graphs",
    "title": "Dijkstra Shortest Path",
    "difficulty": "hard",
    "concept": "Dijkstra finds single-source shortest paths with non-negative edge weights.",
    "why": "It is a standard weighted routing algorithm.",
    "approach": "Dijkstra = greedy relaxation + min-heap.",
    "code": "import heapq\ng={\"A\":[(\"B\",4),(\"C\",1)],\"B\":[(\"D\",1)],\"C\":[(\"B\",2),(\"D\",5)],\"D\":[]}; d={u:float(\"inf\") for u in g}; d[\"A\"]=0; h=[(0,\"A\")]\nwhile h:\n du,u=heapq.heappop(h)\n if du!=d[u]: continue\n for v,w in g[u]:\n  nd=du+w\n  if nd<d[v]: d[v]=nd; heapq.heappush(h,(nd,v))\nprint(d)",
    "output": "{'A': 0, 'B': 3, 'C': 1, 'D': 4}",
    "lines": [
      [
        "nd=du+w",
        "Builds a candidate route."
      ],
      [
        "nd<d[v]",
        "Relaxes the edge."
      ]
    ],
    "dryRun": "A→C→B→D costs 1+2+1=4 to D; B costs 3.",
    "complexity": "O((V+E) log V).",
    "mistakes": [
      "Negative edge weights."
    ],
    "useWhen": "Use for non-negative weighted shortest paths.",
    "interview": [
      [
        "Why not negative edges?",
        "The greedy finalization assumption can fail."
      ]
    ],
    "practice": "Track parents to reconstruct routes."
  },
  {
    "id": "graph-12-bellman-ford",
    "category": "Graphs",
    "title": "Bellman-Ford",
    "difficulty": "hard",
    "concept": "Bellman-Ford handles negative edges and can detect reachable negative cycles.",
    "why": "It is used when Dijkstra’s weight restriction is invalid.",
    "approach": "Repeated edge relaxation is the core.",
    "code": "edges=[(\"A\",\"B\",4),(\"A\",\"C\",5),(\"B\",\"C\",-2),(\"C\",\"D\",3)]; d={\"A\":0,\"B\":float(\"inf\"),\"C\":float(\"inf\"),\"D\":float(\"inf\")}\nfor _ in range(len(d)-1):\n changed=False\n for u,v,w in edges:\n  if d[u]!=float(\"inf\") and d[u]+w<d[v]: d[v]=d[u]+w; changed=True\n if not changed: break\nprint(d)",
    "output": "{'A': 0, 'B': 4, 'C': 2, 'D': 5}",
    "lines": [
      [
        "d[u]+w<d[v]",
        "Relaxes an edge."
      ]
    ],
    "dryRun": "C improves from 5 to 2 through B; D then becomes 5.",
    "complexity": "O(VE) time; O(V) space.",
    "mistakes": [
      "Stopping after one pass."
    ],
    "useWhen": "Use when negative edges may exist.",
    "interview": [
      [
        "Dijkstra vs Bellman-Ford?",
        "Dijkstra is faster but needs non-negative weights; Bellman-Ford is slower but handles negative edges."
      ]
    ],
    "practice": "Add a reachable negative cycle and detect it."
  },
  {
    "id": "graph-13-floyd-warshall",
    "category": "Graphs",
    "title": "Floyd-Warshall",
    "difficulty": "hard",
    "concept": "Floyd-Warshall computes all-pairs shortest paths using DP over intermediate vertices.",
    "why": "It is useful for small dense graphs where every pair matters.",
    "approach": "Three loops; k is the DP layer.",
    "code": "INF=float(\"inf\")\nd=[[0,3,INF],[3,0,1],[INF,1,0]]\nfor k in range(3):\n for i in range(3):\n  for j in range(3): d[i][j]=min(d[i][j],d[i][k]+d[k][j])\nprint(d[0][2])",
    "output": "4",
    "lines": [
      [
        "d[i][k]+d[k][j]",
        "Checks a route through intermediate k."
      ]
    ],
    "dryRun": "0→1→2 costs 3+1=4.",
    "complexity": "O(V³) time; O(V²) space.",
    "mistakes": [
      "Using it for very large sparse graphs."
    ],
    "useWhen": "Use for all-pairs shortest paths on small graphs.",
    "interview": [
      [
        "How is it DP?",
        "k defines which intermediate vertices are allowed."
      ]
    ],
    "practice": "Detect negative cycles with d[i][i] < 0."
  },
  {
    "id": "graph-14-dsu",
    "category": "Graphs",
    "title": "Disjoint Set Union",
    "difficulty": "medium",
    "concept": "DSU maintains disjoint sets with fast find and union using compression and size/rank.",
    "why": "It powers connectivity checks and Kruskal MST.",
    "approach": "DSU = roots + merging sets.",
    "code": "parent=list(range(5)); size=[1]*5\ndef find(x):\n if parent[x]!=x: parent[x]=find(parent[x])\n return parent[x]\ndef union(a,b):\n a,b=find(a),find(b)\n if a==b:return False\n if size[a]<size[b]:a,b=b,a\n parent[b]=a; size[a]+=size[b]; return True\nunion(0,1); union(1,2); print(find(0)==find(2))",
    "output": "True",
    "lines": [
      [
        "parent[x]=find(parent[x])",
        "Path compression flattens the tree."
      ],
      [
        "size[a]+=size[b]",
        "Union by size keeps trees shallow."
      ]
    ],
    "dryRun": "0, 1, and 2 are in one set.",
    "complexity": "Amortized O(alpha(n)) per operation.",
    "mistakes": [
      "Unioning non-root nodes directly."
    ],
    "useWhen": "Use for dynamic connectivity and Kruskal.",
    "interview": [
      [
        "Why path compression?",
        "It makes future finds extremely fast."
      ]
    ],
    "practice": "Use DSU to detect an edge that creates a cycle."
  },
  {
    "id": "graph-15-kruskal",
    "category": "Graphs",
    "title": "Kruskal MST",
    "difficulty": "hard",
    "concept": "Kruskal builds a minimum spanning tree by taking lightest edges that do not create a cycle.",
    "why": "It is a core greedy MST algorithm.",
    "approach": "Kruskal = sort + DSU.",
    "code": "edges=[(1,\"A\",\"B\"),(3,\"B\",\"C\"),(2,\"A\",\"C\"),(4,\"C\",\"D\")]; parent={x:x for x in \"ABCD\"}\ndef find(x):\n while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]\n return x\nmst=[]\nfor w,u,v in sorted(edges):\n a,b=find(u),find(v)\n if a!=b: parent[b]=a; mst.append((u,v,w))\nprint(mst)",
    "output": "[('A', 'B', 1), ('A', 'C', 2), ('C', 'D', 4)]",
    "lines": [
      [
        "sorted(edges)",
        "Processes cheapest edges first."
      ],
      [
        "a!=b",
        "Accepts only edges joining different components."
      ]
    ],
    "dryRun": "Edges 1, 2, and 4 are accepted; the 3 edge would create a cycle.",
    "complexity": "O(E log E) dominated by sorting.",
    "mistakes": [
      "Forgetting MST is for undirected weighted graphs."
    ],
    "useWhen": "Use for minimum spanning trees.",
    "interview": [
      [
        "Why DSU?",
        "It quickly tells whether an edge joins two existing components."
      ]
    ],
    "practice": "Return total MST weight."
  },
  {
    "id": "graph-16-prims",
    "category": "Graphs",
    "title": "Prim MST",
    "difficulty": "hard",
    "concept": "Prim grows an MST by repeatedly taking the cheapest frontier edge.",
    "why": "It is the other major MST technique and pairs naturally with adjacency lists and a heap.",
    "approach": "Same heap idea, different optimization goal.",
    "code": "import heapq\ng={\"A\":[(\"B\",1),(\"C\",2)],\"B\":[(\"A\",1),(\"C\",3)],\"C\":[(\"A\",2),(\"B\",3),(\"D\",4)],\"D\":[(\"C\",4)]}; seen={\"A\"}; h=[(w,\"A\",v) for v,w in g[\"A\"]]; heapq.heapify(h); total=0\nwhile h:\n w,u,v=heapq.heappop(h)\n if v in seen: continue\n seen.add(v); total+=w\n for x,nw in g[v]:\n  if x not in seen: heapq.heappush(h,(nw,v,x))\nprint(total)",
    "output": "7",
    "lines": [
      [
        "heapq.heappop(h)",
        "Chooses the cheapest frontier edge."
      ],
      [
        "if v in seen: continue",
        "Rejects edges into the existing tree."
      ]
    ],
    "dryRun": "Take A-B=1, A-C=2, C-D=4 for total 7.",
    "complexity": "O(E log V).",
    "mistakes": [
      "Confusing Prim with Dijkstra."
    ],
    "useWhen": "Use for MST construction.",
    "interview": [
      [
        "Prim vs Dijkstra?",
        "Prim minimizes total tree connection cost; Dijkstra minimizes source-to-node distances."
      ]
    ],
    "practice": "Return the selected edges."
  },
  {
    "id": "graph-17-scc",
    "category": "Graphs",
    "title": "Strongly Connected Components — Kosaraju",
    "difficulty": "hard",
    "concept": "An SCC is a maximal directed group where every vertex can reach every other.",
    "why": "SCCs expose cyclic dependency groups.",
    "approach": "Kosaraju = DFS order + reverse graph + DFS.",
    "code": "g={0:[1],1:[2],2:[0,3],3:[]}; rev={u:[] for u in g}\nfor u in g:\n for v in g[u]: rev[v].append(u)\nseen=set(); order=[]\ndef d1(u):\n seen.add(u)\n for v in g[u]:\n  if v not in seen:d1(v)\n order.append(u)\nfor u in g:\n if u not in seen:d1(u)\nseen=set(); comps=[]\ndef d2(u,c):\n seen.add(u); c.append(u)\n for v in rev[u]:\n  if v not in seen:d2(v,c)\nfor u in reversed(order):\n if u not in seen:c=[]; d2(u,c); comps.append(c)\nprint(comps)",
    "output": "[[0, 2, 1], [3]]",
    "lines": [
      [
        "order.append(u)",
        "Records finish order."
      ],
      [
        "reversed(order)",
        "Chooses the right roots for the reversed graph."
      ]
    ],
    "dryRun": "0,1,2 form one mutually reachable component; 3 is separate.",
    "complexity": "O(V+E).",
    "mistakes": [
      "Using the original graph in the second pass."
    ],
    "useWhen": "Use for directed connectivity and condensation graphs.",
    "interview": [
      [
        "What is an SCC?",
        "A maximal set with mutual reachability."
      ]
    ],
    "practice": "Study Tarjan as a one-pass alternative."
  },
  {
    "id": "tree-15-full-check",
    "category": "Trees",
    "title": "Check a Full Binary Tree",
    "difficulty": "medium",
    "concept": "A full binary tree has either 0 or 2 children at every node.",
    "why": "Fullness is a structural invariant that appears in tree classification and validation problems.",
    "approach": "Recursively reject a node with exactly one child; leaf nodes and two-child nodes are valid.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\n\ndef is_full(node):\n    if node is None:\n        return True\n    if (node.left is None) != (node.right is None):\n        return False\n    return is_full(node.left) and is_full(node.right)\n\nroot = Node(1, Node(2), Node(3))\nroot.left.left = Node(4)\nroot.left.right = Node(5)\nprint(is_full(root))",
    "output": "True",
    "lines": [
      [
        "if (node.left is None) != (node.right is None):",
        "Detects exactly one child."
      ],
      [
        "return is_full(node.left) and is_full(node.right)",
        "Checks both subtrees recursively."
      ]
    ],
    "dryRun": "Node 1 has two children; node 2 has two children; nodes 3, 4 and 5 are leaves, so every node has 0 or 2 children.",
    "complexity": "O(n) time; O(h) recursion space.",
    "mistakes": [
      "Confusing full with complete.",
      "Checking only the root instead of every node."
    ],
    "useWhen": "Use when a problem explicitly asks whether every internal node has exactly two children.",
    "interview": [
      [
        "What makes a binary tree full?",
        "Every node has either zero or two children."
      ]
    ],
    "practice": "Modify the tree so one node has only a left child and verify the result becomes False."
  },
  {
    "id": "tree-16-perfect-check",
    "category": "Trees",
    "title": "Check a Perfect Binary Tree",
    "difficulty": "medium",
    "concept": "A perfect binary tree has two children at every internal node and all leaves at the same depth.",
    "why": "Perfectness combines a branching rule with a depth rule, making it a useful tree-invariant exercise.",
    "approach": "Find the expected leaf depth from the left edge, then verify every leaf reaches exactly that depth and every internal node has two children.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\n\ndef left_depth(node):\n    depth = 0\n    while node:\n        depth += 1\n        node = node.left\n    return depth\n\ndef check(node, depth, expected):\n    if node is None:\n        return True\n    if node.left is None and node.right is None:\n        return depth == expected\n    if node.left is None or node.right is None:\n        return False\n    return check(node.left, depth + 1, expected) and check(node.right, depth + 1, expected)\n\nroot = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))\nprint(check(root, 1, left_depth(root)))",
    "output": "True",
    "lines": [
      [
        "left_depth(root)",
        "Finds the depth that every leaf should have."
      ],
      [
        "if node.left is None or node.right is None:",
        "Rejects an internal node with only one child."
      ],
      [
        "return depth == expected",
        "Checks the leaf depth invariant."
      ]
    ],
    "dryRun": "The leftmost path has depth 3. Every leaf is at depth 3 and every internal node has two children, so the tree is perfect.",
    "complexity": "O(n) time; O(h) recursion space.",
    "mistakes": [
      "Checking only that the number of nodes is 2^h-1 without validating shape.",
      "Confusing perfect with complete."
    ],
    "useWhen": "Use when both equal leaf depth and two-child structure must hold.",
    "interview": [
      [
        "How is a perfect tree different from a full tree?",
        "A full tree only requires 0 or 2 children; a perfect tree also requires all leaves at the same depth."
      ]
    ],
    "practice": "Remove one leaf and verify the tree is no longer perfect."
  },
  {
    "id": "tree-17-complete-check",
    "category": "Trees",
    "title": "Check a Complete Binary Tree",
    "difficulty": "medium",
    "concept": "A complete binary tree fills every level except possibly the last, and the last level is filled from left to right.",
    "why": "Completeness is the structural property that allows binary heaps to use an array representation efficiently.",
    "approach": "Use level-order traversal. After the first missing child position, every later node must have no children.",
    "code": "from collections import deque\n\nclass Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\n\ndef is_complete(root):\n    if root is None:\n        return True\n    q = deque([root])\n    seen_gap = False\n    while q:\n        node = q.popleft()\n        for child in (node.left, node.right):\n            if child is None:\n                seen_gap = True\n            else:\n                if seen_gap:\n                    return False\n                q.append(child)\n    return True\n\nroot = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6)))\nprint(is_complete(root))",
    "output": "True",
    "lines": [
      [
        "seen_gap = False",
        "Records whether a missing child position has appeared."
      ],
      [
        "if child is None:",
        "A gap in level order has been found."
      ],
      [
        "if seen_gap:",
        "A real child after a gap violates left-to-right filling."
      ]
    ],
    "dryRun": "Level order sees nodes 1, 2, 3, 4, 5, 6. The missing right child of 3 comes after all existing children, so the tree remains complete.",
    "complexity": "O(n) time; O(n) queue space in the widest level.",
    "mistakes": [
      "Checking only node counts.",
      "Forgetting that the final level must be left-aligned.",
      "Confusing complete with perfect."
    ],
    "useWhen": "Use when validating heap-like tree shape or any left-filled binary tree requirement.",
    "interview": [
      [
        "Why are heaps complete binary trees?",
        "Completeness keeps the height logarithmic and lets nodes map naturally to array indices."
      ]
    ],
    "practice": "Add a right child under node 3 while node 2 still has a missing child and observe why the shape fails."
  },
  {
    "id": "tree-18-skewed-check",
    "category": "Trees",
    "title": "Recognize a Skewed Binary Tree",
    "difficulty": "easy",
    "concept": "A skewed binary tree has each node continuing through only one child, making the tree behave like a chain.",
    "why": "Recognizing skewed shape helps explain why an unbalanced BST can degrade from logarithmic height to linear height.",
    "approach": "Walk down the tree and reject any node that has both children. A node with two children is not part of a purely skewed chain.",
    "code": "class Node:\n    def __init__(self, value, left=None, right=None):\n        self.value = value\n        self.left = left\n        self.right = right\n\ndef is_skewed(root):\n    while root:\n        if root.left and root.right:\n            return False\n        root = root.left or root.right\n    return True\n\nroot = Node(1, Node(2, None, Node(3)))\nprint(is_skewed(root))",
    "output": "True",
    "lines": [
      [
        "if root.left and root.right:",
        "A node with two children breaks the skewed-chain shape."
      ],
      [
        "root = root.left or root.right",
        "Moves to the only existing child."
      ]
    ],
    "dryRun": "Node 1 has only a left child; node 2 has only a right child; node 3 is a leaf. The structure is a chain, so it is skewed.",
    "complexity": "O(h) time; O(1) extra space.",
    "mistakes": [
      "Calling every unbalanced tree skewed.",
      "Forgetting that the single-child direction can change."
    ],
    "useWhen": "Use to detect a tree whose nodes each have at most one child along the path.",
    "interview": [
      [
        "Why is a skewed BST slow?",
        "Its height becomes O(n), so search, insertion and deletion can degrade to O(n)."
      ]
    ],
    "practice": "Build a left-skewed tree and confirm the same checker works."
  },
  {
    "id": "graph-18-directed-vs-undirected",
    "category": "Graphs",
    "title": "Model Directed vs Undirected Graphs",
    "difficulty": "easy",
    "concept": "Directed edges have a direction; undirected edges represent a two-way relationship.",
    "why": "Many graph algorithms depend on whether an edge can be traversed in one direction or both.",
    "approach": "For an undirected edge u-v, store both u→v and v→u. For a directed edge u→v, store only u→v.",
    "code": "directed = {\n    'A': ['B'],\n    'B': []\n}\n\nundirected = {\n    'A': ['B'],\n    'B': ['A']\n}\n\nprint(directed['B'])\nprint(undirected['B'])",
    "output": "[]\n['A']",
    "lines": [
      [
        "directed['A'] = ['B']",
        "A can reach B, but the reverse is not implied."
      ],
      [
        "undirected['B'] = ['A']",
        "The reverse relationship is stored explicitly."
      ]
    ],
    "dryRun": "In the directed graph, B has no outgoing edge. In the undirected graph, B can return to A because the connection works both ways.",
    "complexity": "O(V + E) storage for adjacency lists.",
    "mistakes": [
      "Automatically adding reverse edges to a directed graph.",
      "Forgetting both directions in an undirected adjacency list."
    ],
    "useWhen": "Use directed graphs for dependencies, one-way links and prerequisite relationships; use undirected graphs for mutual connections such as two-way roads.",
    "interview": [
      [
        "How do you represent an undirected edge in an adjacency list?",
        "Add each endpoint to the other endpoint's neighbor list."
      ]
    ],
    "practice": "Convert a directed dependency graph into an undirected graph and compare BFS reachability."
  },
  {
    "id": "graph-19-weighted-vs-unweighted",
    "category": "Graphs",
    "title": "Model Weighted vs Unweighted Graphs",
    "difficulty": "easy",
    "concept": "Weighted graphs attach a cost/value to each edge; unweighted graphs treat each edge as equal cost.",
    "why": "The edge information determines whether simple BFS is enough or a weighted shortest-path algorithm is required.",
    "approach": "Store plain neighbors for unweighted graphs and (neighbor, weight) pairs for weighted graphs.",
    "code": "unweighted = {\n    'A': ['B', 'C'],\n    'B': ['A'],\n    'C': ['A']\n}\n\nweighted = {\n    'A': [('B', 5), ('C', 2)],\n    'B': [('A', 5)],\n    'C': [('A', 2)]\n}\n\nprint(weighted['A'][1])",
    "output": "('C', 2)",
    "lines": [
      [
        "weighted['A']",
        "Stores both destination and edge cost."
      ],
      [
        "('C', 2)",
        "Represents an edge from A to C with weight 2."
      ]
    ],
    "dryRun": "The unweighted model only says A connects to B and C. The weighted model additionally says reaching B costs 5 while reaching C costs 2.",
    "complexity": "O(V + E) storage for adjacency lists.",
    "mistakes": [
      "Ignoring weights when the problem asks for minimum cost.",
      "Using Dijkstra when negative edge weights exist."
    ],
    "useWhen": "Use weighted graphs when distance, time, price or another edge-specific cost matters.",
    "interview": [
      [
        "When can BFS solve shortest path?",
        "When every edge has equal cost, such as an unweighted graph."
      ]
    ],
    "practice": "Represent a road map where each edge stores travel time."
  }
];
