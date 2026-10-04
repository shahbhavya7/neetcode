class Solution:   
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterOfBinaryTree = 0
        
        def height(node: Optional[TreeNode]) -> int: 
            # just calculate the current diameter inside the height function as height already has length of left and right subtree, 
            # so we can calculate the diameter at that node
            if node is None:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            self.diameterOfBinaryTree = max(self.diameterOfBinaryTree, left_height + right_height)
            
            return max(left_height, right_height) + 1
        height(root)
        
        return self.diameterOfBinaryTree