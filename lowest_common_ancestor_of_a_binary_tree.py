# -*- coding: utf-8

'''
LeetCode 上这题 31 个 case 一直有两个过不了, 肉眼晚上是看不出来了, MARK 一下 改天 debug.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    def mid_travel(node, level):
        if node is None:
            return

        lvl = level + 1

        if node.left:
            mid_travel(node.left, lvl)

        if mid_travel.started and lvl < mid_travel.min_lvl:
            mid_travel.ret = node
            mid_travel.min_lvl = lvl

        if node.val == p.val or node.val == q.val:
            if mid_travel.started:
                raise Exception

            mid_travel.started = True
            mid_travel.min_lvl = lvl
            mid_travel.ret = node

        if node.right:
            mid_travel(node.right, lvl)

    mid_travel.min_lvl = 9999
    mid_travel.started = False
    mid_travel.ret = root

    try:
        mid_travel(root, 0)
    except Exception:
        pass

    return mid_travel.ret


# FIXME, two LeetCode still not passed.
