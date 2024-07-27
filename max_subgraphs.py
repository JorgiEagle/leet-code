"""
Given two integers, numNodes and numEdges
Return the minimum size of the maximal complete subgraph of a graph formed of the given number of nodes and edges.

A subgraph is one where every element in the subgraph connects to every other element

e.g. 

1 - 2 - 3 
Contains 2 subgraphs of size 2: [1, 2] and [2, 3]

Thus the minimum size of these is 2

Consider 4, 6

1 - 2 - 3
|   | /
4 - 5

Has several subgraphs: [1, 2], [2, 3], [2, 3, 5], etc

The answer is 3. Since this is minimum possible maximal subgraph
"""

# A complete graph has n*(n-1) / 2 edges

# If num edges equals to this, then the maximal subgraph is n

def maximal_subgraphs(numNodes, numEdges):
    index = 1
    while numEdges > 0:
        index += 1
        numEdges -= numNodes - 1
        numNodes -= 1
    return index

print(maximal_subgraphs(3, 2))
print(maximal_subgraphs(3, 3))
print(maximal_subgraphs(4, 3))
print(maximal_subgraphs(4, 4))

        