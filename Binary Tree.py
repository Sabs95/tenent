# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Node:
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None
def printOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printLevel(root, i)
  
def printLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print (root.data)
    elif level > 1 : 
        printLevel(root.left , level-1) 
        printLevel(root.right , level-1) 
def height(node): 
    if node is None: 
        return 0 
    else :  
        lheight = height(node.left) 
        rheight = height(node.right) 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print ("The binary tree is -")
printOrder(root)