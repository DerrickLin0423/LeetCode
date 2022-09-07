from solution import TreeNode, Solution


if __name__ == "__main__":
    # nodes = [1,null,0,0,1]
    root = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
    output = Solution().pruneTree(root)
    print("Output:", output)

    # nodes = [1,0,1,0,0,0,1]
    root = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1)))
    output = Solution().pruneTree(root)
    print("Output:", output)
    
    # nodes = [1,1,0,1,1,0,1,0]
    root = TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(0)), TreeNode(1)), TreeNode(0, TreeNode(0), TreeNode(1)))
    output = Solution().pruneTree(root)
    print("Output:", output)