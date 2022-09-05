from solution import Node, Solution, buildTree


if __name__ == "__main__":
    nodes = [1,None,3,2,4,None,5,6]
    root = buildTree(nodes)
    output = Solution().levelOrder(root)
    print("Output:", output)

    nodes = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
    root = buildTree(nodes)
    output = Solution().levelOrder(root)
    print("Output:", output)
