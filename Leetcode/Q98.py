class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def divideConquer(root, lower, upper):
            if not root:
                return True

            return root.val < upper and root.val > lower and \
                divideConquer(root.left, lower, root.val) and \
                divideConquer(root.right, root.val, upper)

        lower, upper = float('-inf'), float('inf')
        return divideConquer(root, lower, upper)
