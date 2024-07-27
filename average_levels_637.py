class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root):
        # BFS
        results = []
        curr_level = [root]
        while curr_level:
            result, curr_level = averageLevel(curr_level)
            results.append(result)
        return results

def averageLevel(nodes):
    result = []
    next_level = []
    while nodes:
        node = nodes.pop()
        if node is None:
            continue
        result.append(node.val)
        next_level.extend([node.left, node.right])
    return (sum(result)/len(result) if result else 0), next_level


tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(averageOfLevels(tree))