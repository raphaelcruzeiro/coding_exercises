class TreeNode(object):
    def __init__(self):
        self.val = None
        self.right = None
        self.left = None
        self.flat = None

    def append(self, n):
        if self.val is None:
            self.val = n
            return
        if self.val < n:
            if self.right is None:
                self.right = TreeNode()
            self.right.append(n)
        else:
            if self.left is None:
                self.left = TreeNode()
            self.left.append(n)

    def __contains__(self, arg):
        # arg "in" self
        if arg == self.val:
            return True
        if arg < self.val:
            nextnode = self.left
        else:
            nextnode = self.right
        if nextnode is None:
            return False
        return nextnode.__contains__(arg) #return arg in nextnode

    def __iter__(self):
        return self

    def __next__(self):
        if self.flat is None:
            self.flat = []
            self.i = 0

            def append_inorder(node, l):
                if node:
                    append_inorder(node.left, l)
                    l.append(node.val)
                    append_inorder(node.right, l)

            append_inorder(self, self.flat)

        if self.i > len(self.flat) - 1:
            raise StopIteration

        val = self.flat[self.i]
        self.i += 1
        return val


t = TreeNode()

t.append(4)
t.append(2)
t.append(5)
t.append(8)
t.append(1)
t.append(12)

for n in t: print(n)


