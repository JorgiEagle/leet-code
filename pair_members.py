"""
Given two lists of nodes, n1 and n2, both of length n. Index i represents an edge between the nodes at position i in both lists.
E.g.

n1 = [1, 2, 3]
n2 = [2, 4, 2]

Represents:

1 - 2 - 4
    |
    3

Return the maximum difference of the min and max elements from each graph

e.g. 3

or

n1 = [1, 2, 3]
n2 = [4, 1, 5]

2 - 1 - 4

3 - 5

= 3 (max(3-1, 5-3))
"""