# -*- coding: utf-8 -*-
# Author: Hao Zhao

"""
树的专有名词：
度数：每个节点所有的子树的个数
层数：树的层数
高度：树的最大层数
树叶或终端节点（叶子节点）：度数为0的节点
非叶子节点:度数不为0的节点

二叉树和一般树的不同之处：
1. 树不可为空集合，但是二叉树可以
2. 树的度数为d>=0；但二叉树的节点度数为0<=d<=2
3. 树的子树之间没有次序关系，二叉树则有

二叉查找树的特点：
1. 可以是空集合，但若不是空集合，树节点上一定要有一个键值
2. 每一个树根的值需要大于左子树的值
3. 每一个树根的值需要小于右子树的值
4. 树的每个节点的值都不相同

二叉树的3种遍历方法：
中序遍历：
1. 遍历左子树
2. 遍历树根
3. 遍历右子树

前序遍历：
1. 遍历树根
2. 遍历左子树
3. 遍历有右子树

后序遍历：
1. 遍历左子树
2. 遍历右子树
3. 遍历树根

应用场景：
1. 算数表达式的二叉运算树

"""

class TreeNode(object):
    """定义二叉树的节点"""
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None

def create_tree(root,value):
    """创建二叉树"""
    # 创建二叉树的节点
    Node = TreeNode()
    Node.data = value
    Node.left = None
    Node.right = None
    # 创建二叉树的树根节点
    if root == None:
        root = Node
        return root
    # 为创建的新节点寻找合适的位置
    else:
        current = root
        while current != None:
            backup = current
            if current.data > value:
                current = current.left
            else:
                current = current.right
        # 插入新节点
        if backup.data > value:
            backup.left = Node
        else:
            backup.right = Node
    # 返回新节点
    return root

def preorder(ptr):
    """前序遍历： 遍历树根->遍历左子树->遍历右子树"""
    if ptr != None:
        print('[%2d]' % ptr.data,end='')
        preorder(ptr.left)
        preorder(ptr.right)


def inorder(ptr):
    """中序遍历：遍历左子树->遍历树根->遍历右子树"""
    if ptr != None:
        inorder(ptr.left)
        print('[%2d]' % ptr.data,end='')
        inorder(ptr.right)

def postorder(ptr):
    """后序遍历：遍历左子树->遍历右子树->遍历树根"""
    if ptr != None:
        postorder(ptr.left)
        postorder(ptr.right)
        print('[%2d]' % ptr.data, end='')

def search(ptr,value):
    """查询二叉树中的节点"""
    i = 1
    while True:
        if ptr == None:
            return None
        if ptr.data == value:
            print("共查找%d次" % i)
            return ptr
        elif ptr.data > value:
            ptr = ptr.left
        else:
            ptr = ptr.right
        i += 1

def delete(ptr,value):
    """
    删除二叉树中的节点：
    1. 删除的节点为叶子节点，只需要将其父节点指向None
    2. 删除的节点只有1棵子树，只需要将其子树节点放到其父节点指针字段
    3. 删除的节点有2棵子树：（都是符合二叉树特性）
        a) 找出中序立即先行者：左子树中最大的值代替删除节点的位置
        b) 找出中序立即后序者：右子树中最小的值代替删除节点的位置
    """
    pass


if __name__ == "__main__":
    data = [7,4,1,5,16,8,11,12,15,9,2]
    ptr = None
    root = None
    for i in range(11):
        # 建立二叉树
        ptr = create_tree(ptr,data[i])

    # 遍历二叉树
    print("前序遍历结果：")
    preorder(ptr)
    print()
    print("中序遍历结果：")
    inorder(ptr)
    print()
    print("后序遍历结果：")
    postorder(ptr)
    print()

    # 查询操作
    value = 11
    if search(ptr,value) != None:
        print("该值找到了！")
    else:
        print("该值找不到！")

    # 插入操作
    addvalue = 11
    if search(ptr,addvalue) != None:
        print("已经存在")
    else:
        ptr = create_tree(ptr,addvalue)
