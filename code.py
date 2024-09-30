import math
from math import floor

# username - alonbeck1
# id1      - 318441599
# name1    - Alon Beck
# id2      - 319144283
# name2    - Aya Schechner

import printer

"""A class representing a node in an AVL tree"""

class AVLNode(object):
    """Constructor, you are allowed to add more fields.

        @type value: str
        @param value: data of your node
        """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0
        self.bf = 0

    """returns the size
        @rtype: Int
        @returns: returns the size of the sub-tree of the node, including the node
        Time Complexity: O(1)
        """

    def getSize(self):  # returns number of nodes in the tree
        return self.size

    """returns the left child
    
        @rtype: AVLNode
        @returns: the left child of self, None if there is no left child
        Time Complexity: O(1)
        """

    def getLeft(self):  # returns the left son of self
        if self.left.isRealNode():
            return self.left
        return self.left

    """returns the right child

        @rtype: AVLNode
        @returns: the right child of self, None if there is no right child
        Time Complexity: O(1)
        """

    def getRight(self):     # returns the right son of self
        if self.right.isRealNode():
            return self.right
        return self.right

    """returns the parent 

        @rtype: AVLNode
        @returns: the parent of self, None if there is no parent
        Time Complexity: O(1)
        """

    def getParent(self):    # returns the parent of self if there is one
        if self.parent == None:
            return None
        if self.parent.isRealNode():
            return self.parent
        return None

    """return the value

        @rtype: str
        @returns: the value of self, None if the node is virtual
        Time Complexity: O(1)
        """

    def getValue(self):     # returns the value of self
        if self.isRealNode():
            return self.value
        return None

    """returns the height

        @rtype: int
        @returns: the height of self, -1 if the node is virtual
        Time Complexity: O(1)
        """

    def getHeight(self):    # returns the height of self
        return self.height

    """sets left child

        @type node: AVLNode
        @param node: a node
        Time Complexity: O(1)
        """

    def setLeft(self, node):    # setting the left son of self
        self.left = node
        return None

    """sets right child

        @type node: AVLNode
        @param node: a node
        Time Complexity: O(1)
        """

    def setRight(self, node):   # setting the right son of self
        self.right = node
        return None

    """sets parent

        @type node: AVLNode
        @param node: a node
        Time Complexity: O(1)
        """

    def setParent(self, node):  # setting the parent of self
        self.parent = node
        return None

    """sets value

        @type value: str
        @param value: data
        Time Complexity: O(1)
        """

    def setValue(self, value):  # setting the value of self
        self.value = value
        return None

    """sets the balance factor of the node

        @type h: int
        @param h: the height
        Time Complexity: O(1)
        """

    def setHeight(self, h):     # setting the height of self
        self.height = h
        return None

    """returns whether self is not a virtual node 

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        Time Complexity: O(1)
        """

    def isRealNode(self):  # checking whether the node is virtual or not
        return self.height != -1

    """calculating the number of nodes in self's sub-tree, self included
        
        Time Complexity: O(1)
        """

    def calcSize(self):  # calculating the number of nodes in the sub-tree of self, self included
        return self.left.size + self.right.size + 1

    """rotating to the right side 

        @rtype: None
        @returns: None. changing the pointers inside the tree
        Time Complexity: O(1)
        """

    def rightrot(self, other):  # rotating to the right side (self is the upper node...)
        self.left = other.right
        self.left.parent = self
        other.right = self
        other.parent = self.parent
        if other.parent != None:   # changing the father pointer (first checking on which side of the father...)
            if other.parent.right == self:
                other.parent.right = other
            else:
                other.parent.left = other
        self.parent = other
        self.height = max(self.right.height, self.left.height) + 1   # updating the fields from her on
        other.height = max(other.right.height, other.left.height) + 1
        self.size = 1 + self.right.size + self.left.size
        other.size = 1 + other.left.size + other.right.size
        self.bf = self.left.height - self.right.height
        other.bf = (other.left.height) - (other.right.height)
        return None

    """rotating to the left side 

        @rtype: None
        @returns: None. changing the pointers inside the tree
        Time Complexity: O(1)
        """

    def leftrot(self, other):  # rotating to the right side (self is the upper node...)
        self.right = other.left
        self.right.parent = self
        other.left = self
        other.parent = self.parent
        if other.parent != None:   # changing the father pointer (first checking on which side of the father...)
             if other.parent.left == self:
                 other.parent.left = other
             else:
                other.parent.right = other
        self.parent = other
        self.height = max(self.right.height, self.left.height) + 1  # updating the fields from her on
        other.height = max(other.right.height, other.left.height) + 1
        self.size = 1 + self.right.size + self.left.size
        other.size = 1 + other.left.size + other.right.size
        self.bf = self.left.height - self.right.height
        other.bf = (other.left.height) - (other.right.height)
        return None

    """returns the node's successor

        @rtype: node
        @returns: the successor of self, or self if no successor.
        Time Complexity:O(log(n))
        """

    def successor(self):
        if self.right.isRealNode():  # if the node has right son, return the node on the bottom left of the sons subtree
            return self.right.minimum()
        parent = self.parent
        right = self
        while parent != None and right == parent.right:  # if there is no right child, go up until the first turn right
            right = parent
            parent = right.parent
        return parent

    """returns the node's predecessor

        @rtype: node
        @returns: the predecessor of self, or self if no predecessor.
        Time Complexity:O(log(n))
        """

    def predecessor(self):
        if self.left.isRealNode():  # if the node has left son return the node on the bottom right of the sons subtree
            return self.left.maximum()
        parent = self.parent
        left = self
        while parent != None and left == parent.left:   # if there is no left son, go up until the first turn left
            left = parent
            parent = left.parent
        return parent

    """returns the minimum node of self's subtree

        @rtype: node
        @returns: the minimum node self's subtree.
        Time Complexity:O(log(n))
        """

    def minimum(self):
        curr = self
        while curr.left.isRealNode():
            curr = curr.left
        return curr

    """returns the maximum node of self's subtree

        @rtype: node
        @returns: the maximum node of the current node's subtree.
        Time Complexity:O(log(n))
        """

    def maximum(self):
        curr = self
        if curr.right != None:
            while curr.right.isRealNode():
                curr = curr.right
        return curr


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.size = 0  # denote self.size = n
        self.root = None
        self.max = None
        self.min = None

    # add your fields here

    """returns whether the list is empty

        @rtype: bool
        @returns: True if the list is empty, False otherwise
        Time Complexity: O(1)
        """

    def empty(self):
        return self.size == 0

    """retrieves the value of the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: index in the list
        @rtype: str
        @returns: the the value of the i'th item in the list
        Time Complexity:O(log(n))
        """

    def retrieve(self, i):
        if i < 0:
            return None
        if i > self.size - 1:
            return None
        else:
            new_node = self.treeSelect(i+1)     # returning the node which there are i nodes ranked lower then it
            return new_node.value

    """ insert help function 
    
        Time Complexity:O(log(n))
        """

    def insert_last(self, node):  # inserting to the bottom right side of the tree
        self.max.right = node
        node.parent = self.max
        self.size += 1
        self.max = node
        x = self.fixtree(node)  # going over the tree to update fields and rotate if needed
        return x

    """ insert help function 
    
        Time Complexity:O(log(n))
        """

    def insert_first(self, node):   # inserting to the bottom left side of the tree
        a = self.min.value
        self.min.left = node
        node.parent = self.min
        self.min = node
        self.size += 1
        x = self.fixtree(node)  # going over the tree to update fields and rotate if needed
        return x

    """ insert help function 

        Time Complexity:O(1)
        """

    def insert_root(self, node):    # inserting the first node to the tree
        self.root = node
        self.min = node
        self.max = node
        self.size += 1
        return 0

    """ insert help function 

        Time Complexity:O(log(n))
        """

    def insert_left(self, father, node):  # inserting to the left side of hte current (i))th node
        father.left = node
        node.parent = father
        self.size += 1
        x = self.fixtree(node)  # going over the tree to update fields and rotate if needed
        return x

    """ insert help function 

        Time Complexity:O(log(n))
        """

    def insert_right(self, father, node):    # inserting to the right side of the current (i-1)th node
        father.right = node
        node.parent = father
        self.size += 1
        x = self.fixtree(node)  # going over the tree to update fields and rotate if needed
        return x

    """going over the route from node to root to fix fields (if needed)
        
        Time Complexity:O(log(n))
        """

    def fixtree(self, node):     # fixing size, height, bf fields of the nodes on the trail from the root to the node
        son = node
        father = node.parent
        while father != None:  # "traveling" on the route from "node" to the root to update fields if needed
            father.height = max(father.left.height, father.right.height) + 1
            father.bf = (father.left.height) - (father.right.height)
            father.size = father.left.size + father.right.size + 1
            father = father.parent
            son = son.parent
        y = self.rotations(node)
        return y

    """going over the route from node to root to fix fields (if needed) after rotations

        Time Complexity:O(log(n))
        """

    def fixafterrot(self, node):    # fixing size, height, bf fields of the nodes on the trail from the root to the node after rotation
        son = node
        father = node.parent
        while father != None:   # "traveling" on the route from "node" to the root to update fields if needed
            father.height = max(father.left.height, father.right.height) + 1
            father.bf = (father.left.height) - (father.right.height)
            father.size = father.left.size + father.right.size + 1
            father = father.parent
            son = son.parent
        return None

    """going over the route from node to root looking for rotations needed

        Time Complexity:O(log(n))
        """

    def rotations(self, node):  # going over the trail from the node to the rot looking for "avl-criminals"
        rotnum = 0
        son = node
        father = node.parent
        while father != None:
            if father.right == son:
                if (father.bf == -2) and (son.bf == -1):
                    if self.root == father:
                        self.root = son
                    father.leftrot(son)     # rotating the problematic nodes
                    self.fixafterrot(father)     # fixing after rotation
                    rotnum += 1
                    return 1
                elif (father.bf == -2) and (son.bf == 1):
                    sonleft = son.left
                    if self.root == father:
                        self.root = sonleft
                    son.rightrot(son.left)      # rotating the problematic nodes
                    father.leftrot(sonleft)     # rotating the problematic nodes
                    self.fixafterrot(father)    # fixing after rotation
                    rotnum += 2
                    return rotnum
            elif father.left == son:
                if (father.bf == 2) and (son.bf == 1):
                    if self.root == father:
                        self.root = son
                    father.rightrot(son)    # rotating the problematic nodes
                    self.fixafterrot(father)    # fixing after rotation
                    rotnum += 1
                    return rotnum
                elif (father.bf == 2) and (son.bf == -1):
                    sonright = son.right
                    if self.root == father:
                        self.root = sonright
                    son.leftrot(son.right)  # rotating the problematic nodes
                    father.rightrot(sonright)   # rotating the problematic nodes
                    self.fixafterrot(father)    # fixing after rotation
                    rotnum += 2
                    return rotnum
            father = father.parent
            son = son.parent
        return rotnum

    """inserts val at position i in the list

        @type i: int
        @pre: 0 <= i <= self.length()
        @param i: The intended index in the list to which we insert val
        @type val: str
        @param val: the value we inserts
        @rtype: list
        @returns: the number of re-balancing operation due to AVL rebalancing
        Time Complexity:O(log(n))
        """

    def insert(self, i, val):
        new_node = AVLNode(val)
        new_node.left = AVLNode(None)
        new_node.left.parent = new_node
        new_node.right = AVLNode(None)
        new_node.right.parent = new_node
        new_node.height += 1
        new_node.size += 1
        if self.size == 0:  # if the tree is empty...
            x = self.insert_root(new_node)
            return x
        if i == self.size:  # if we want to insert the node to the bottom right side of the tree
            x = self.insert_last(new_node)
            return x
        if i == 0:          # if we want to insert the node to the bottom left side of the tree
            x = self.insert_first(new_node)
            return x
        else:
            helpnode = self.treeSelect(i+1)     # searching for the current (i)th node
            if helpnode.left.height == -1:
                x = self.insert_left(helpnode, new_node)    # inserting to the left side of help node
                return x
            else:
                helpnodepre = helpnode.predecessor()    # searching for predecessor incase there is a right son
                x = self.insert_right(helpnodepre, new_node)    # inserting to the right side of predecessor
                return x

    """changing pointers to go over a node in order to remove it from the tree
      
        @type node, changeNode: AVLNode
        Time Complexity: O(1)
        """

    def bypass(self, node, changeNode):
        changeNode.parent = node.parent
        if node.parent.left == node:  # node is a left child
            node.parent.left = changeNode
        else:  # node is a right child
            node.parent.right = changeNode
        return None

    """double rotating two nodes 
       
        @param father, son: AVLNode
        @param side: str
        Time Complexity: O(1)
        """

    def doubleRotation(self, father, son, side):
        if side == 'right':
            AVLNode.leftrot(son, son.right)
            AVLNode.rightrot(father, father.left)
        else:  # side is left
            AVLNode.rightrot(son, son.left)
            AVLNode.leftrot(father, father.right)
        if self.root == father:
            self.root = father.parent
        return None

    """rotating two nodes 
        
        @param father, son: AVLNode
        @param side: str
        Time Complexity: O(1)
        """

    def singleRotation(self, father, son, side):
        if side == 'left':
            AVLNode.rightrot(father, son)
        else:  # side is right
            AVLNode.leftrot(father, son)
        if self.root == father:
            self.root = son
        return None

    """deletes the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: The intended index in the list to be deleted
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        Time Complexity: O(log(n))
        """

    def delete(self, i):
        delNode = AVLTreeList.treeSelect(self, i + 1)
        if delNode is None:  # ith index isn't in the list
            return -1
        virtualNode = AVLNode(None)
        father = delNode.parent
        isRoot = False
        isMax = False
        isMin = False
        if delNode == self.root:
            isRoot = True
        if delNode == self.max:
            isMax = True
        if delNode == self.min:
            isMin = True

        if (not delNode.left.isRealNode()) and (not delNode.right.isRealNode()):  # deleted node is a leaf
            if not isRoot:  # deleted node is not the root
                if isMax:
                    self.max = delNode.parent
                if isMin:
                    self.min = delNode.parent
                AVLTreeList.bypass(self, delNode, virtualNode)
            else:  # deleted node is the root
                self.root = None  # the tree is empty now
                self.min = None
                self.max = None

        elif delNode.left.isRealNode() and not delNode.right.isRealNode():  # deleted node has only left child
            if not isRoot:  # deleted node is not the root
                AVLTreeList.bypass(self, delNode, delNode.left)  # bypass the deleted node
                if isMax:
                    self.max = delNode.left
            else:  # deleted node is the root
                delNode.left.parent = None  # make deleted node's child the root
                self.root = delNode.left
                self.max = self.root  # deleted node is the root + has only left child -> it's the maximum

        elif delNode.right.isRealNode() and not delNode.left.isRealNode():  # deleted node has only right child
            if not isRoot:
                AVLTreeList.bypass(self, delNode, delNode.right)  # bypass the deleted node
                if isMin:
                    self.min = delNode.right
            else:  # deleted node is the root
                delNode.right.parent = None  # make deleted node's child the root
                self.root = delNode.right
                self.min = self.root  # deleted node is the root + has only right child -> it's the minimum

        else:  # deleted node has two children
            success = delNode.successor()  # successor is a leaf or has only right child (prove in class)
            father = success.parent
            if father == delNode:
                father = success
            if success.right.isRealNode():  # successor has a right child
                AVLTreeList.bypass(self, success, success.right)
            else:  # successor is a leaf
                AVLTreeList.bypass(self, success, virtualNode)
            # replacing the deleted node with the successor:
            if not isRoot:  # deleted node isn't the root
                AVLTreeList.bypass(self, delNode, success)
            else:  # deleted node is the root
                success.parent = None
                self.root = success
            delNode.right.parent = success  # update deleted node's children's parent
            delNode.left.parent = success
            success.left = delNode.left  # update successor's children
            success.right = delNode.right

        rotNum = 0
        while father is not None:  # updating size and rotating
            father.size = AVLNode.calcSize(father)
            bf = father.left.height - father.right.height
            father.bf = bf
            father.height = max(father.left.height, father.right.height) + 1
            if bf == 2:
                leftSon = father.left
                if leftSon.isRealNode():
                    sonBf = leftSon.bf
                    if sonBf == 0 or sonBf == 1:
                        self.singleRotation(father, leftSon, 'left')
                        father = leftSon
                        rotNum += 1
                    else:  # sonBf == -1
                        self.doubleRotation(father, leftSon, 'right')
                        father = leftSon.right
                        rotNum += 2

            elif bf == -2:
                rightSon = father.right
                if rightSon.isRealNode():
                    sonBf = rightSon.left.height - rightSon.right.height
                    if sonBf == 0 or sonBf == -1:
                        self.singleRotation(father, rightSon, 'right')
                        father = rightSon
                        rotNum += 1
                    else:  # sonBf == 1
                        self.doubleRotation(father, rightSon, 'left')
                        father = rightSon.left
                        rotNum += 2
            # elif (bf == 0 or bf == 1 or bf == -1) continue to update size and check parent's bf
            father = father.parent
        self.size -= 1
        return rotNum

    """returns the value of the first item in the list

        @rtype: str
        @returns: the value of the first item, None if the list is empty
        Time Complexity:O(1)
        """

    def first(self):
        if self.size == 0:
            return None
        else:
            return self.min.value

    """returns the value of the last item in the list

        @rtype: str
        @returns: the value of the last item, None if the list is empty
        Time Complexity:O(1)
        """

    def last(self):
        if self.size == 0:
            return None
        else:
            return self.max.value

    """returns an array representing list 

        @rtype: list
        @returns: a list of strings representing the data structure
        Time Complexity:O(n)
        """

    def listToArray(self):
        if self.size == 0:
            new_array1 = []
            return new_array1
        new_array2 = [0 for i in range(self.size)]   # initializing the array to the correct size
        currnode = self.min
        for i in range(self.size):
            new_array2[i] = currnode.value
            currnode = currnode.successor()     # going over the tree inorder to make the array
        return new_array2

    """returns the size of the list 

        @rtype: int
        @returns: the size of the list
        Time Complexity:O(1)
        """

    def length(self):
        return self.size

    """sort the info values of the list

        @rtype: list
        @returns: an AVLTreeList where the values are sorted by the info of the original list.
        Time Complexity:O(nlog(n))
        """

    def sort(self):
        if self.size == 0:
            newavltree = AVLTreeList()
            return newavltree
        helparray = self.listToArray()
        newavltree = AVLTreeList()
        for i in range(self.size):      # going over the array and making AVLNode for each index
            pp = helparray[i]
            new_node = AVLNode(helparray[i])
            new_node.left = AVLNode(None)
            new_node.left.parent = new_node
            new_node.right = AVLNode(None)
            new_node.right.parent = new_node
            new_node.height += 1
            new_node.size += 1
            if i == 0:
                x = newavltree.insert_root(new_node)
            else:
                d = new_node.value
                a = newavltree.root
                currval = a.value
                isitreal = a.isRealNode()
                if new_node.value == None:
                    newavltree.insert_first(new_node)
                else:
                    while a.isRealNode() == True:  # inserting to tree as if it was a BST
                        if a.value == new_node.value:   # adding this case because lists can have two similar values
                            if not a.right.isRealNode():
                                if newavltree.min == a:
                                    newavltree.min = new_node
                                    x = newavltree.insert_right(a, newavltree)
                                else:
                                    if newavltree.max == a:
                                        newavltree.max == new_node
                                        x = newavltree.insert_right(a, newavltree)
                                    else:
                                        x = newavltree.insert_right(a, newavltree)
                                break
                            elif a.right.isRealNode():
                                b = a.successor()
                                if newavltree.min == b:
                                    newavltree.min = new_node
                                    x = newavltree.insert_left(b, new_node)
                                else:
                                    if newavltree.max == b:
                                        newavltree.max = new_node
                                        x = newavltree.insert_left(b, new_node)
                                    else:
                                        x = newavltree.insert_left(b, new_node)
                                break
                        elif (a.value == None) and (a.isRealNode):
                            a = a.right
                        elif  a.value > new_node.value:
                            a = a.left
                        elif  a.value < new_node.value:
                            a = a.right
                    c = a.parent
                    if c.left == a:
                        if newavltree.min == c:
                            newavltree.min = new_node
                        newavltree.insert_left(c, new_node)
                    elif c.right == a:
                        if newavltree.max == c:
                            newavltree.max = new_node
                        newavltree.insert_right(c, new_node)
                newavltree.fixtree(a)   # fixing the tree after each insertion to keep it an AVL
        return newavltree

    """permute the info values of the list 

        @rtype: list
        @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
        Time Complexity:O(n)
        """

    def permutation(self):
        import random
        if self.size == 0:
            newavltree = AVLTreeList()
            return newavltree
        if self.size == 1:  # if the tree has only one node then returning the tree itself
            a = self.retrieve(0)
            newavltree = AVLTreeList()
            newavltree.insert(0, a.val)
            return newavltree
        if self.size == 2:  # if the tree has only 2 nodes then randomly making a permutation of it
            a = self.retrieve(0)
            b = self.retrieve(1)
            x = random.randint(0,1)
            newavltree = AVLTreeList()
            newavltree.insert(0, a.val)
            newavltree.insert(x, b.val)
            return newavltree
        helparray = self.listToArray()
        helparray2 = self.listToArray()
        for i in range(self.size):  # making helparray2 (a permutation of helarray) using helparray
            x = random.randint(i, self.size-1)
            b = x
            AVLTreeList.swap(helparray2, i, x)  # swapping between the index values
        y = math.floor(self.size/2)     # looking for the middle of the array
        a1 = 0 #saving pointers from here on to the places where we want to slice the array instead of actual slicing
        a2 = y-1
        b1 = y+1
        b2 = len(helparray2)-1
        newavltree = AVLTreeList()
        newnode = AVLNode(helparray2[y])    # making the middle of the array the new AVL's root
        newavltree.root = newnode
        newavltree.size += 1
        newavltree.min = newnode
        newavltree.max = newnode
        a = AVLTreeList.creatAvlTreeRec(helparray2,a1, a2)  # recursively making the left sub AVL tree
        b = AVLTreeList.creatAvlTreeRec(helparray2, b1, b2)  # recursively making the right sub AVL tree
        newavltree.root.left = a.root  # from here on "connecting" the two sub trees to the root, and fixing fields values
        a.root.parent = newavltree.root
        newavltree.root.right = b.root
        b.root.parent = newavltree.root
        newavltree.root.height = max(a.root.height, b.root.height) + 1
        newavltree.root.bf = a.root.height - b.root.height
        newavltree.root.size = a.size + b.size + 1
        newavltree.size = a.size + b.size + 1
        newavltree.min = a.min
        newavltree.max = b.max
        return newavltree

    """help function

        Time Complexity:O(n)
        """

    def creatAvlTreeRec(lst, firstnode, secondnode):
        curravltree = AVLTreeList()
        y = math.floor((secondnode-firstnode+1)/2)
        if secondnode-firstnode+1 > 3:  # if the current list size is bigger then 3, keep going with the recurrsive calls
            newnode = AVLNode(lst[y])
            a1 = 0  # saving pointers from here on to the places where we want to slice the array instead of actual slicing
            a2 = y-1
            b1 = y+1
            b2 = secondnode
            curravltree.root = newnode
            a = AVLTreeList.creatAvlTreeRec(lst, a1, a2)  # recursively making the left sub AVL tree
            b = AVLTreeList.creatAvlTreeRec(lst, b1, b2)  # recursively making the right sub AVL tree
            curravltree.root.left = a.root  # from here on "connecting" the two sub trees to the root, and fixing fields values
            a.root.parent = curravltree.root
            curravltree.root.right = b.root
            b.root.parent = curravltree.root
            curravltree.root.height = max(a.root.height, b.root.height) + 1
            curravltree.root.bf = a.root.height - b.root.height
            curravltree.root.size = a.size + b.size + 1
            curravltree.min = a.min
            curravltree.max = b.max
            curravltree.size = a.size + b.size + 1
            return curravltree
        if secondnode-firstnode+1 == 3:  # else, change pointers and fields and return the tree
            curravltree.root = AVLNode(lst[firstnode+1])
            a = AVLNode(lst[firstnode])
            a.left = AVLNode(None)
            a.right = AVLNode(None)
            a.height += 1
            a.size += 1
            b = AVLNode(lst[secondnode])
            b.left = AVLNode(None)
            b.right = AVLNode(None)
            b.size += 1
            b.height += 1
            curravltree.root.left = a
            curravltree.root.right = b
            b.parent = curravltree.root
            a.parent = curravltree.root
            curravltree.root.size = 3
            curravltree.root.height = 1
            curravltree.size = 3
            curravltree.min = a
            curravltree.min = b
            return curravltree
        if secondnode-firstnode+1 == 1:  # else, change pointers and fields and return the tree
            curravltree = AVLTreeList()
            a = AVLNode(lst[firstnode])
            a.right = AVLNode(None)
            a.left = AVLNode(None)
            a.size += 1
            a.height += 1
            curravltree.root = a
            curravltree.min = a
            curravltree.max = a
            curravltree.size = 1
            return curravltree
        if secondnode-firstnode+1 == 2:  # else, change pointers and fields and return the tree
            a = AVLNode(lst[firstnode])
            a.left = AVLNode(None)
            a.right = AVLNode(None)
            a.size += 1
            a.height += 1
            b = AVLNode(lst[secondnode])
            b.right = AVLNode(None)
            b.size += 2
            b.height += 2
            b.bf = 1
            b.left = a
            a.parent = b
            curravltree.root = b
            curravltree.min = a
            curravltree.max = b
            curravltree.size = 2
            return curravltree

    """swapping indexes in array 

        @rtype: list
        @returns: list in which two indexes "switched" values
        Time Complexity:O(1)
        """

    def swap(self, i, j):  # swapping between values randomly
        a = self[i]
        b = self[j]
        self[i] = b
        self[j] = a

    """concatenates lst to self

        @type lst: AVLTreeList
        @param lst: a list to be concatenated after self
        @rtype: int
        @returns: the absolute value of the difference between the height of the AVL trees joined
        Time Complexity: O(log(n)) - the size of the two trees sizes combined
        """

    def concat(self, lst):
        if lst.size == 0 and self.size == 0:
            return 0
        if lst.size == 0:
            return abs(self.root.height)
        if self.size == 0:
            self.root = lst.root
            self.size = lst.size
            self.min = lst.min
            self.max = lst.max
            return abs(self.root.height)
        firstreeheight = self.root.height
        secondtreeheight = lst.root.height
        helpnode = AVLNode("no way there is another node with this value")  # making connecting node
        c = helpnode  # making pointer to connecting node in order to be able to delete it later on
        if firstreeheight > secondtreeheight:
            a = self.max
            while a.height < secondtreeheight:  # looking for the first node with matching/bigger height
                a = a.parent
            if a == self.root:
                a.parent = helpnode  # from here on fixing values and updating pointers
                helpnode.left = a
                helpnode.right = lst.root
                lst.root.parent = helpnode
                self.root.parent = helpnode
                self.root = helpnode
                helpnode.size = helpnode.left.size + helpnode.right.size + 1
                helpnode.height = max(helpnode.left.height, helpnode.right.height) + 1
                helpnode.bf = helpnode.left.height - helpnode.right.height
                self.size += 1 + lst.size
                self.max = lst.max
                x = self.fixtree(c)     # fixing the tree
                d = self.treeRank(c)  # looking for the helping node index
                f = self.retrieve(d-1)
                self.delete(d - 1)  # deleting the helping node
                return abs(firstreeheight - secondtreeheight)
            a.parent.right = helpnode
            helpnode.left = a
            helpnode.right = lst.root
            helpnode.parent = a.parent
            a.parent = helpnode
            lst.root.parent = helpnode
            helpnode.size = a.size + lst.root.size + 1
            helpnode.height = max(a.height, lst.root.height) +1
            helpnode.bf = helpnode.left.height - helpnode.right.height
            self.size += lst.size + 1
            self.max = lst.max
            x = self.fixtree(c)     # fixing the tree
            d = self.treeRank(c)    # looking for the helping nodes index
            self.delete(d-1)    # deleting the helping node from the tree
            return abs(firstreeheight-secondtreeheight)
        elif secondtreeheight > firstreeheight:     # doing the exact same thing replacing "roles" of the trees
            a = lst.min
            while a.height < firstreeheight:
                a = a.parent
            if a == lst.root:
                a.parent = helpnode
                helpnode.right = a
                helpnode.left = self.root
                self.root.parent = helpnode
                self.root = helpnode
                helpnode.size = helpnode.left.size + helpnode.right.size
                helpnode.height = max(helpnode.left.height, helpnode.right.height) + 1
                helpnode.bf = helpnode.left.height - helpnode.right.height
                self.size += 1 + lst.size
                self.max = lst.max
                x = self.fixtree(c)     # fixing the tree after concatenating
                d = self.treeRank(c)    # looking dor the helping nodes index
                self.delete(d - 1)  # deleting the helping node from the tree
                return abs(firstreeheight - secondtreeheight)
            a.parent.left = helpnode
            helpnode.left = self.root
            helpnode.right = a
            helpnode.parent = a.parent
            a.parent = helpnode
            self.root.parent = helpnode
            helpnode.size = a.size + self.root.size + 1
            helpnode.height = max(a.height, self.root.height) + 1
            helpnode.bf = helpnode.left.height - helpnode.right.height
            self.size += lst.size + 1
            self.max = lst.max
            self.root = lst.root
            x = self.fixtree(c)     # fixing the tree after concatenating
            d = self.treeRank(c)  # looking for the helping nodes index
            self.delete(d-1)    # deleting the helping node from the tree
            return abs(firstreeheight-secondtreeheight)
        if firstreeheight == secondtreeheight:  # in this case no need to fix the tree after concatenating!!
            helpnode.left = self.root
            helpnode.right = lst.root
            helpnode.size = self.size + lst.size + 1
            helpnode.height = max(self.root.height, lst.root.height) + 1
            helpnode.bf = helpnode.left.height - helpnode.right.height
            self.root = helpnode
            self.size += lst.size + 1
            self.max = lst.max
            d = self.treeRank(c)    # looking for the helping nodes index
            self.delete(d-1)    # deleting the helping node from the tree
            return 0

    """searches for a *value* in the list

        @type val: str
        @param val: a value to be searched
        @rtype: int
        @returns: the first index that contains val, -1 if not found.
        Time Complexity:O(n)
        """

    def search(self, val):
        if self.size == 0:
            return -1
        i = 0
        currnode = self.min
        if currnode.value == val:  # returning the first index if we found the node at the beginning
            return 0
        else:
            i += 1
            while currnode.successor() != None:
                currnode = currnode.successor()  # going inorder looking for the value
                if currnode.value == val:
                    return i
                i += 1
        return -1

    """returns the root of the tree representing the list

        @rtype: AVLNode
        @returns: the root, None if the list is empty
        Time Complexity:O(1)
        """

    def getRoot(self):
        if self.size == 0:
            return None
        else:
            return self.root

    """returns the rank of the selected node

        @type node: AVLNode
        @param node: a node to get it's rank
        @rtype: int
        @returns: the rank of the given node
        Time Complexity: O(log(n))
        """

    def treeRank(self, node):
        cnt = node.left.size + 1
        curr = node
        while curr != None:
            if curr.parent != None:
                 if curr == curr.parent.right:  # curr is a right son
                    cnt += curr.parent.left.size + 1  # add the current node's left subtree size + 1
                    curr = curr.parent  # go up
                 else:
                     curr = curr.parent     # go up
            else:
                return cnt
        return cnt

    """returns the element with rank i

        @type i: int
        @param i: the rank of the returned element
        @rtype: AVLNode
        @returns: the element with rank i, or None if the rank does not exist.
        Time Complexity: O(log(n))
        """

    def treeSelect(self, i):
        if i > self.size or i <= 0:  # check if the rank exist
            return None
        return AVLTreeList.treeSelectRec(self.root, i)

    """ recursive function for treeSelect
    
        Time Complexity: O(log(n))
        """
    
    def treeSelectRec(node, i):
        indx = node.left.size + 1
        if i == indx:  # the root is the required element
            return node
        elif i < indx:  # the required element is in the left subtree
            return AVLTreeList.treeSelectRec(node.left, i)
        else:  # the required element is in the right subtree
            return AVLTreeList.treeSelectRec(node.right, i - indx)

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printer.printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out
