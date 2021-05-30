class Tree:
    stack = []
    def __init__(self, data):
        self.data = data[0]
        self.extra_info = data[1:]
        self.parrent = None
        self.left = None
        self.right = None
        self.level = 0
        self.height = 0
    
    def bst_insert(self, root):
        if root == None:
            return self
        elif self.data < root.data:
            temp = self.bst_insert(root.left)
            temp.parrent = root
            temp.level = root.level + 1
            root.left = temp
        elif self.data >= root.data:
            temp = self.bst_insert(root.right)
            temp.parrent = root
            temp.level = root.level + 1
            root.right = temp
        
        return root

    def till_none(self, case):
        while True:
            if case == 'l' and self.left != None:
                self = self.left
            elif case == 'r' and self.right != None:
                self = self.right
            else:
                return self


    def avl_rotations(self):
        diff = 0
        if self==None:
            return

        elif self.right!=None and self.left!=None:
            diff = self.left.height - self.right.height
            # print(self.data, " : ", diff)
        elif self.left!=None:
            diff = self.left.height - 0
        elif self.right!=None:
            diff = 0 - self.right.height
    
        if diff > 1:
            # print(self.data, " : ", diff)
            temp_p = self
            
            if self.parrent.left == self:
                self.parrent.left = self.left
            elif self.parrent.right == self:
                self.parrent.right = self.left

            self = self.left
            if self.right != None:
                temp = self.right.till_none('r')
                temp.right = temp_p
                self.right = temp
            else:
                self.right = temp_p

            # print(self.data)

            
        elif diff < -1:
            # print(self.data, " : ", diff)
            temp_p = self
            
            if self.parrent.left == self:
                self.parrent.left = self.right
            elif self.parrent.right == self:
                self.parrent.right = self.right

            self = self.right
            if self.left != None:
                temp = self.left.till_none('l')
                temp.left = temp_p
                self.left = temp
            else:
                self.right = temp_p
                # print(self.left.data)

            # print(self.data)
        
            
    def bst_traversal_dfs(root, exclude):
        if root.left:
            root.left.bst_traversal_dfs(exclude)
        if root.right:
            root.right.bst_traversal_dfs(exclude)
        try:
            if(root.data != exclude): root.stack.append(root.extra_info[1])
        except:
            pass
        return root.stack
        

    def bst_print(root, where):
        print(where, root.data)

    def bst_traversal_pre(root, where=None):
        if root == None:
            return
        else:
            root.height = bst_height(root)
            root.bst_print(where)
            if root.left != None:
                root.left.bst_traversal_pre(where + "left : ")
            if root.right != None:
                root.right.bst_traversal_pre(where + "right : ")

    def bst_traversal_pre_storage_en(root, memo):
        if root == None:
            return memo
        else:
            if root.left != None:
                memo.append(root.left.extra_info[1])
                root.left.bst_traversal_pre_storage_en(memo)
            if root.right != None:
                memo.append(root.right.extra_info[1])
                root.right.bst_traversal_pre_storage_en(memo)

def bst_search(node, obj):
    if node == None:
        return False
    if node.data == obj:
        return node
    if node.data < obj:
        res = bst_search(node.right, obj)
    if node.data > obj:
        res = bst_search(node.left, obj)

    return res

# def bst_lrdiff(node):
#     if node==None:
#         return -1
#     else:
#         lheight = bst_lrdiff(node.left)
#         rheight = bst_lrdiff(node.right)
        
#     return lheight-rheight


def bst_height(node):
    if node==None:
        return -1
    else:
        lheight = bst_height(node.left)
        rheight = bst_height(node.right)
        
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1


def bst_exact_search(tree, to_search, found):
    if tree == None:
        return
    else:
        if tree.left != None:
            if str(tree.left.data).strip().lower() == str(to_search).strip().lower():
                found.append(tree.left.extra_info)
                found[-1].append(tree.left.data)
            
            bst_exact_search(tree.left, to_search, found)

        if tree.right != None:
            if str(tree.right.data).strip().lower() == str(to_search).strip().lower():
                found.append(tree.right.extra_info)
                found[-1].append(tree.right.data)
            
            bst_exact_search(tree.right, to_search, found)

    return found



        
# root = Tree(10)
# node1 = Tree(5)
# node2 = Tree(15)
# root = node1.bst_insert(root)
# root = node2.bst_insert(root)
# node3 = Tree(2)
# node4 = Tree(5)
# root = node3.bst_insert(root)
# root = node4.bst_insert(root)
# node5 = Tree(53)
# node6 = Tree(154)
# root = node5.bst_insert(root)
# root = node6.bst_insert(root)
# node7 = Tree(12)
# node8 = Tree(1)
# root = node7.bst_insert(root)
# root = node8.bst_insert(root)
# node9 = Tree(-1)
# node10 = Tree(-7)
# root = node9.bst_insert(root)
# root = node10.bst_insert(root)

# # root.bst_print("root : ")

# root.bst_traversal_pre("root : ")

# root.bst_traversal_dfs()

# # root.avl_rotations()

# for i in range(0, len(root.stack)):
#     # print(root.stack[i].data, " -")
#     root.stack[i].avl_rotations()

# # print(root.left.right.right.data)

# print(bst_search(root, 154))


# print(root.till_none('r').data)

# root.bst_traversal_pre("root : ")