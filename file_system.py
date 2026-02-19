class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

class FileSystem:
    def __init__(self):
        self.root = Node("/")

    def mkdir(self, path):
        parts = path.strip("/").split("/")
        current = self.root

        for part in parts:
            if part not in current.children:
                current.children[part] = Node(part)
            current = current.children[part]

    def ls(self, node=None, level=0):
        if node is None:
            node = self.root
        print("  " * level + node.name)
        for child in node.children.values():
            self.ls(child, level + 1)


fs = FileSystem()
fs.mkdir("/home/user/docs")
fs.mkdir("/home/user/images")
fs.ls()
