/* Dynamic Programming learning content. */
(function () {
  const L = window.PYDSA_PROGRAM_LESSONS;
  const add = (id, data) => { L[id] = data; };
  const common = (concept, what, why, approach, dryRun, lineByLine, complexity, mistakes, useWhen, avoidWhen, interview, practice) => ({ concept, what, why, example: '', approach, dryRun, lineByLine, complexity, mistakes, useWhen, avoidWhen, interview, practice });

  add('dynamic-programming-01', common(
    'Bottom-up dynamic programming for Fibonacci',
    'Build the Fibonacci sequence from the smallest known answers instead of recursively recomputing the same values.',
    'Fibonacci is the simplest example of overlapping subproblems. It shows how a DP table can turn repeated recursive work into a single forward pass.',
    ['Define dp[i] as the ith Fibonacci number.', 'Set dp[0] = 0 and dp[1] = 1.', 'For every later position, use dp[i] = dp[i-1] + dp[i-2].', 'Return the completed sequence.'],
    [['dp[0], dp[1]', '[0, 1]'], ['i = 2', 'dp[2] = 1'], ['i = 3', 'dp[3] = 2'], ['i = 4', 'dp[4] = 3'], ['i = 5', 'dp[5] = 5']],
    [['dp = [0] * n', 'Creates storage for every Fibonacci state.'], ['dp[0], dp[1] = 0, 1', 'Sets the two base cases.'], ['for i in range(2, n)', 'Builds states from left to right.'], ['dp[i] = dp[i-1] + dp[i-2]', 'Uses the two previously solved states.'], ['return dp', 'Returns the sequence stored in the table.']],
    { time: 'O(n)', space: 'O(n)' },
    ['For n = 0, the table should be handled before accessing dp[1].', 'Do not confuse the Fibonacci index with the number of terms requested.', 'The full table is unnecessary if only the final Fibonacci value is needed.'],
    'Use it when you need the sequence or want the clearest introduction to bottom-up DP.',
    'If only one Fibonacci value is required and memory matters, keep only the previous two values.',
    ['What are the states in this DP?', 'Why is this O(n) instead of exponential?', 'How can the space be reduced to O(1)?'],
    ['Rewrite it using only two variables.', 'Write a top-down memoized version.', 'Compare recursive, memoized, and tabulated Fibonacci.']
  ));

  add('dynamic-programming-02', common(
    'Longest Common Subsequence (LCS)',
    'Find the length of the longest sequence that appears in both strings in the same relative order, without requiring the characters to be adjacent.',
    'LCS teaches a classic two-dimensional DP state: each cell summarizes the best answer for prefixes of the two strings.',
    ['Let dp[i][j] represent the LCS length for X[:i] and Y[:j].', 'If the current characters match, extend the diagonal answer.', 'Otherwise choose the better answer from dropping one character from either string.', 'The bottom-right cell contains the final answer.'],
    [['X = AGGTAB, Y = GXTXAYB', 'We compare prefixes of both strings.'], ['G matches G', 'Take the diagonal value + 1.'], ['Different characters', 'Take max(top, left).'], ['Final cell', 'LCS length = 4']],
    [['dp = [[0] * (n+1) ...]', 'Creates a table with an extra zero row and column for empty prefixes.'], ['if X[i-1] == Y[j-1]', 'Checks whether the newest characters match.'], ['1 + dp[i-1][j-1]', 'Extends the matching subsequence.'], ['max(dp[i-1][j], dp[i][j-1])', 'Chooses the better result when characters differ.'], ['return dp[m][n]', 'Reads the answer for the complete strings.']],
    { time: 'O(mn)', space: 'O(mn)' },
    ['LCS is not the same as longest common substring; characters do not need to be adjacent.', 'The DP indexes refer to prefixes, so use i-1 and j-1 for string characters.', 'Returning the length is simpler than reconstructing the actual subsequence.'],
    'Use it for sequence comparison, diff-like tasks, and as a foundation for other string DP problems.',
    'For very large strings, a full matrix may be too memory-heavy; space-optimized variants are possible when only the length is needed.',
    ['What does dp[i][j] mean?', 'Why do we use the diagonal when characters match?', 'How would you reconstruct the actual LCS?'],
    ['Implement LCS with recursion + memoization.', 'Reconstruct one actual LCS.', 'Compare LCS with longest common substring.']
  ));

  add('dynamic-programming-03', common(
    '0/1 Knapsack',
    'Choose items with weights and values to maximize total value without exceeding a capacity, where each item can be chosen at most once.',
    'Knapsack is a core decision-DP problem. Each item creates a choice: take it or leave it.',
    ['Let dp[i][w] be the best value using the first i items with capacity w.', 'If the current item is too heavy, skip it.', 'Otherwise compare taking it with skipping it.', 'The final cell gives the maximum value for all items and full capacity.'],
    [['Capacity 50', 'Items: (60,10), (100,20), (120,30).'], ['First two items', 'Taking both gives value 160 at weight 30.'], ['Add 120', 'All three weigh 60, so they cannot all fit.'], ['Best', 'Items 100 + 120 fit at weight 50 → value 220.']],
    [['dp = [[0] * (W+1) ...]', 'Creates states for each item count and capacity.'], ['weights[i-1] <= w', 'Checks whether the current item fits.'], ['values[i-1] + dp[i-1][w-weight]', 'Value when the item is taken.'], ['dp[i-1][w]', 'Value when the item is skipped.'], ['max(...)', 'Chooses the better decision.']],
    { time: 'O(nW)', space: 'O(nW)' },
    ['0/1 means each item is used at most once.', 'Do not accidentally use dp[i] when the recurrence requires the previous item row.', 'Capacity W is part of the state, so the complexity depends on W.'],
    'Use it when each item creates a take/skip decision under a capacity or budget constraint.',
    'Do not use it when items can be taken unlimited times without adapting the recurrence; that is a different knapsack variant.',
    ['Why is this called 0/1?', 'What changes for unbounded knapsack?', 'How can space be reduced to O(W)?'],
    ['Implement the one-dimensional DP version.', 'Reconstruct which items were selected.', 'Solve a subset-sum decision problem.']
  ));

  add('dynamic-programming-04', common(
    'Minimum Coin Change',
    'Find the minimum number of coins needed to make a target amount when each coin denomination can be reused.',
    'This demonstrates a one-dimensional DP where each amount depends on smaller amounts already solved.',
    ['Let dp[x] be the minimum coins needed to make amount x.', 'Set dp[0] = 0 because no coins are needed for zero.', 'For each coin, update reachable amounts using 1 + dp[amount - coin].', 'If the target remains unreachable, return -1.'],
    [['Amount 0', 'dp[0] = 0'], ['Coin 5', 'dp[5] can become 1'], ['Amount 10', 'dp[10] can become dp[5] + 1 = 2'], ['Amount 11', '5 + 5 + 1 → 3 coins']],
    [['dp = [inf] * (V+1)', 'Starts every nonzero amount as unreachable.'], ['dp[0] = 0', 'Sets the base case.'], ['dp[i - coin]', 'Looks at the smaller amount left after taking a coin.'], ['1 + dp[i-coin]', 'Adds the current coin to that solution.'], ['return -1 if ...', 'Reports impossible targets.']],
    { time: 'O(kV)', space: 'O(V)' },
    ['Do not initialize every amount to 0; that would falsely make unreachable states look optimal.', 'This program allows unlimited use of each coin.', 'Coin-change greedy choices do not always produce the minimum number of coins.'],
    'Use DP when denominations do not guarantee a greedy solution.',
    'For special coin systems where a proven greedy strategy works, DP may be unnecessary.',
    ['Why does greedy fail for some coin systems?', 'What does dp[x] represent?', 'How would you reconstruct the actual coins used?'],
    ['Return the selected coins, not only the count.', 'Solve the version where each coin can be used once.', 'Count the number of ways to make the amount.']
  ));

  add('dynamic-programming-05', common(
    "Kadane's Algorithm for Maximum Subarray Sum",
    'Find the largest possible sum of a contiguous subarray.',
    'Kadane’s algorithm is a compact DP recurrence: at each position, decide whether the best subarray ending here should start fresh or extend the previous one.',
    ['max_current means the best sum of a subarray ending at the current index.', 'Either start with arr[i] or extend max_current + arr[i].', 'max_global stores the best ending sum seen anywhere.', 'The global maximum is the answer.'],
    [['[-2]', 'current = -2, global = -2'], ['1', 'max(1, -2+1) = 1'], ['-3', 'max(-3, 1-3) = -2'], ['4,-1,2,1', 'Best ending sum grows to 6'], ['Result', 'Maximum subarray sum = 6']],
    [['max_current = arr[0]', 'Starts the best subarray ending at index 0.'], ['max(arr[i], max_current + arr[i])', 'Chooses a new subarray or extends the old one.'], ['max_global = max(...)', 'Preserves the best sum found anywhere.']],
    { time: 'O(n)', space: 'O(1)' },
    ['Do not initialize the answer to 0 if all values may be negative.', 'The subarray must be contiguous.', 'Do not confuse maximum sum with maximum subsequence sum.'],
    'Use it when you need the maximum sum of a contiguous range in one pass.',
    'If you need the actual subarray, keep start/end indexes in addition to the sums.',
    ['Why does Kadane’s algorithm work?', 'What happens when all numbers are negative?', 'How do you return the actual subarray?'],
    ['Return the start and end indexes.', 'Find the minimum subarray sum.', 'Adapt it to the circular maximum subarray problem.']
  ));

  add('dynamic-programming-06', common(
    'Edit Distance / Levenshtein Distance',
    'Find the minimum number of insertions, deletions, and substitutions needed to transform one string into another.',
    'Edit distance combines several choices into one DP state and is widely useful for string comparison, spell checking, and fuzzy matching.',
    ['Let dp[i][j] be the edit distance between the first i characters of str1 and first j characters of str2.', 'Matching characters need no new operation.', 'For different characters, choose insert, delete, or replace with the smallest cost.', 'The final cell is the minimum edit distance.'],
    [['kitten → sitting', 'Compare prefixes.'], ['k → s', 'Replace k with s: cost 1.'], ['kitten → sitten', 'One replacement.'], ['sitten → sittin → sitting', 'Two insert/replace operations more.'], ['Result', 'Distance = 3']],
    [['dp[i][0] = i', 'Turning i characters into an empty string needs i deletions.'], ['dp[0][j] = j', 'Turning empty into j characters needs j insertions.'], ['str1[i-1] == str2[j-1]', 'Matching characters carry the diagonal cost forward.'], ['1 + min(...)', 'Chooses insert, delete, or replace.']],
    { time: 'O(mn)', space: 'O(mn)' },
    ['Initialize the first row and column correctly.', 'Insert, delete, and replace are different operations.', 'Do not use substring matching logic; edit distance allows modifications.'],
    'Use it for approximate string comparison and transformation-cost problems.',
    'A full matrix may be unnecessary when only the distance is needed and memory is constrained.',
    ['What do the three neighboring cells represent?', 'Why is replacement based on the diagonal?', 'How can space be reduced to O(n)?'],
    ['Reconstruct the sequence of edits.', 'Implement a two-row space-optimized version.', 'Compare two filenames and report their edit distance.']
  ));

  add('dynamic-programming-07', common(
    'Longest Increasing Subsequence (LIS)',
    'Find the length of the longest subsequence whose values are strictly increasing.',
    'LIS teaches one-dimensional DP where the state describes the best increasing subsequence that ends at a particular position.',
    ['Set dp[i] to 1 because every element alone forms an increasing subsequence.', 'For each earlier j, check whether arr[j] < arr[i].', 'If so, arr[i] can extend the subsequence ending at j.', 'The largest dp value is the LIS length.'],
    [['10', 'dp[0] = 1'], ['22', '22 can extend 10 → dp[1] = 2'], ['33', 'Can extend 10 and 22 → dp[3] = 3'], ['50', 'Can extend the best earlier sequence → dp = 4'], ['60', 'Final LIS length = 5']],
    [['dp = [1] * n', 'Every element starts as a length-one subsequence.'], ['for j in range(i)', 'Checks earlier possible predecessors.'], ['if arr[i] > arr[j]', 'Ensures the sequence remains increasing.'], ['dp[i] = max(dp[i], dp[j] + 1)', 'Extends the best sequence ending at j.'], ['return max(dp)', 'Finds the best ending position.']],
    { time: 'O(n²)', space: 'O(n)' },
    ['A subsequence does not need to be contiguous.', 'Strictly increasing means equal values cannot extend the sequence.', 'The quadratic DP is not the fastest known LIS solution, but it is easier to learn first.'],
    'Use this version when clarity is more important than the advanced O(n log n) optimization.',
    'For very large arrays, learn the patience-sorting/binary-search based O(n log n) solution.',
    ['What does dp[i] represent?', 'Why can’t we sort the array first?', 'How does the O(n log n) LIS approach differ?'],
    ['Reconstruct the actual subsequence.', 'Implement LIS in O(n log n).', 'Find the longest non-decreasing subsequence.']
  ));

  add('dynamic-programming-08', common(
    'Maximum Product Subarray',
    'Find the contiguous subarray with the largest product, including cases where negative numbers change the sign of the product.',
    'Unlike maximum-sum problems, a negative number can turn the smallest negative product into the largest positive product. That means one state is not enough.',
    ['Track both the maximum and minimum product ending at the current position.', 'When the current number is negative, swap those two states before updating.', 'Use the current value alone or extend either previous product.', 'Keep the best maximum seen globally.'],
    [['2', 'max = 2, min = 2'], ['3', 'max = 6, min = 3'], ['-2', 'Negative flips the roles → max = -2, min = -12'], ['4', 'max = 4, min = -48'], ['Result', 'Maximum product = 6']],
    [['max_ending, min_ending', 'Keep both extremes because a future negative value can flip them.'], ['if arr[i] < 0: swap', 'A negative multiplier reverses which extreme can become largest.'], ['max(arr[i], arr[i] * max_ending)', 'Choose a new subarray or extend the previous maximum.'], ['min(arr[i], arr[i] * min_ending)', 'Do the same for the minimum.'], ['max_so_far = max(...)', 'Track the best product overall.']],
    { time: 'O(n)', space: 'O(1)' },
    ['Tracking only the maximum fails when negatives appear.', 'Do not forget zero resets the useful product chain.', 'The subarray must be contiguous.'],
    'Use it for contiguous-product optimization where negative values are possible.',
    'For problems without negative values, the simpler positive-product reasoning may be enough.',
    ['Why do we need both max and min?', 'What does a negative number do to the two states?', 'How does zero affect the recurrence?'],
    ['Return the actual maximum-product subarray.', 'Compare this with Kadane’s algorithm.', 'Handle an array containing only zeros and negatives.']
  ));

  add('dynamic-programming-09', common(
    'Minimum Path Sum in a Matrix',
    'Find the minimum sum from the top-left to the bottom-right of a grid when movement is allowed right or down.',
    'This is a clean two-dimensional DP example: the best path to a cell must come from the best path to the cell above or to the left.',
    ['Let dp[i][j] be the minimum cost to reach cell (i,j).', 'Initialize the first row and column because they have only one possible direction.', 'For every other cell, add its value to min(top, left).', 'The bottom-right cell is the minimum path sum.'],
    [['Start', 'dp[0][0] = 1'], ['First row', '1 → 4 → 5'], ['First column', '1 → 2 → 6'], ['Center 5', '5 + min(4,2) = 7'], ['End', 'Minimum path sum = 7']],
    [['dp[0][0] = grid[0][0]', 'Sets the starting cost.'], ['First row/column loops', 'Build states with their only available predecessor.'], ['min(dp[i-1][j], dp[i][j-1])', 'Chooses the cheaper predecessor.'], ['+ grid[i][j]', 'Adds the current cell cost.'], ['return dp[m-1][n-1]', 'Returns the cheapest cost to the destination.']],
    { time: 'O(mn)', space: 'O(mn)' },
    ['Only right and down moves are allowed in this recurrence.', 'Do not forget first-row and first-column initialization.', 'The path sum includes the starting and ending cells.'],
    'Use this pattern for grid problems where each cell depends on a small set of previous cells.',
    'If movement can go in arbitrary directions, this simple DP recurrence may no longer be valid.',
    ['Why can each cell depend only on top and left?', 'How can the matrix be updated in place?', 'How would you reconstruct the path?'],
    ['Return the actual minimum path.', 'Implement O(n) space.', 'Solve the version with obstacles.']
  ));

  add('dynamic-programming-10', common(
    'Maximum Path Sum in a Matrix',
    'Find the maximum sum from the top-left to the bottom-right of a grid when movement is allowed right or down.',
    'It is the same grid-DP structure as minimum path sum, but the optimization direction changes from min to max.',
    ['Let dp[i][j] be the maximum sum reaching cell (i,j).', 'Initialize the first row and column using their only predecessor.', 'For each inner cell, add its value to max(top, left).', 'Return the bottom-right state.'],
    [['Start', 'dp[0][0] = 1'], ['First row', '1 → 4 → 5'], ['First column', '1 → 2 → 6'], ['Center 5', '5 + max(4,2) = 9'], ['End', 'Maximum path sum = 12']],
    [['dp[0][0] = grid[0][0]', 'Sets the starting state.'], ['First row/column loops', 'Handle cells with only one predecessor.'], ['max(dp[i-1][j], dp[i][j-1])', 'Chooses the more valuable predecessor.'], ['+ grid[i][j]', 'Adds the current cell value.'], ['return dp[m-1][n-1]', 'Returns the best possible path sum.']],
    { time: 'O(mn)', space: 'O(mn)' },
    ['Do not accidentally use min when the problem asks for maximum.', 'Movement restrictions are part of the recurrence.', 'If negative values are allowed, do not initialize unreachable states as zero without considering the effect.'],
    'Use it for grid optimization problems with acyclic movement such as right/down paths.',
    'If movement creates cycles or allows arbitrary directions, a different algorithm may be required.',
    ['How is this different from minimum path sum?', 'Why does the recurrence work?', 'How can space be reduced?'],
    ['Reconstruct the maximum path.', 'Write a one-dimensional DP version.', 'Compare the minimum and maximum path implementations side by side.']
  ));

  // Mark the DP family so the renderer can optionally style it in future batches.
  window.PYDSA_DP_LESSONS_READY = true;
})();
