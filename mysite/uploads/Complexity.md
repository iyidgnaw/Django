# Complexity
## Big-o Notation Definition
Let n be the size of program's input and T(n) be a function.
- Formal:
O(f(n)) is the set of all functions T(n) that satisfy:  
There exist positive constants C and N such that for all n >= N, T(n) <= Cf(n)
the highlighted code from specific programming language.
- Big-o notation doesn't care about constants factors.
- Big-o is Upper bound only.
- Suppose we have a more complex instance: n^3 + n^2 +n,
n^3 will be the dominant part of the whole algorithm. Big-o notation is usually used to indicate the dominating (fastest growing )term.

| Big-o| Common Name|
|---|---|---|---|---|
| O(1)  | constant  |
| O(log n)  | logorithmic  |
| O(n^0.5)  | root-n  |
| O(n)  | linear  |
| O(nlog n)  |   |
| O(n^2)  | quadratic  |
| O(n^3)  | cubic  |
| O(2^n)  | exponential  |
