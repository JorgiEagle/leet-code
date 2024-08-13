class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(tuple([self.val, self.left, self.right]))

    
    def __repr__(self) -> str:
        return str(tuple([self.val, self.left, self.right]))


def increasingBST(root: TreeNode) -> TreeNode:
        # DFS
        while root.left:
            new_root = root.left
            new_parent = root.left
            while new_parent.right is not None:
                new_parent = new_parent.right
            new_parent.right = root
            root = new_root

        curr = root
        while curr.right:
            while curr.right.left is not None:
                new_parent = curr.right.left
                while new_parent.right is not None:
                    new_parent = new_parent.right
                new_parent.right = curr.right
                curr.right = new_parent
            curr = curr.right
        return root
            
            
        


inp = [5,3,6,2,4,None,8,1,None,None,None,7,9]
nodes = [TreeNode(x) if x else None for x in inp]
off_set = 0
for node_index in range(len(nodes)):
    if nodes[node_index] is None:
        off_set += 1
        continue
    try:
        nodes[node_index].left = nodes[((node_index-off_set)*2)+1]
        nodes[node_index].right = nodes[((node_index-off_set)*2)+2]
    except IndexError:
        continue


root = nodes[0]

print(increasingBST(root))

