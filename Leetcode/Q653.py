class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        ht = set()
        def helper(root):
            if root:
                calcValue = k - root.val
                if calcValue in ht:
                    return True
                else:
                    ht.add(root.val)

                return helper(root.left) or helper(root.right)

        return helper(root)
