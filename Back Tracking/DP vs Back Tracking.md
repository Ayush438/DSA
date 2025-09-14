Backtracking = try all possibilities, prune invalid ones, and backtrack when stuck.

1. Exploration-based: It systematically generates all valid solutions.
2. Brute-force with pruning: It doesn’t remember past results → can repeat work.
3. Use case: Problems where we must generate all solutions or search paths.
   
Example: Generate Parentheses (n=3)
We build strings by placing '(' or ')' as long as they remain valid:
a. Start: ""
b. Add '(' → "("
c. Add '(' → "(("
d. Add ')' → "(()" … etc.
Backtracking explores all paths until it finds all 5 valid solutions.


---------------------------------------------------------------------------------------------------
Dynamic Programming (DP): store results of overlapping subproblems so we don’t recompute them.

1. Optimization-based: Typically used to compute the best value (min, max, count).
2. Memory-based: Saves intermediate results in a table (top-down with memoization or bottom-up with tabulation).
3. Use case: Problems with overlapping subproblems + optimal substructure.
Example: Unique Paths with Obstacles

At each cell (i, j), the number of paths = sum of paths from top and left:
