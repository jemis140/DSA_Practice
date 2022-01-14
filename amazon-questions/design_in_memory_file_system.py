# Design a data structure that simulates an in-memory file system.

# Implement the FileSystem class:

# FileSystem() Initializes the object of the system.
# List<String> ls(String path)
# If path is a file path, returns a list that only contains this file's name.
# If path is a directory path, returns the list of file and directory names in this directory.
# The answer should in lexicographic order.
# void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
# void addContentToFile(String filePath, String content)
# If filePath does not exist, creates that file containing given content.
# If filePath already exists, appends the given content to original content.
# String readContentFromFile(String filePath) Returns the content in the file at filePath.

class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.content = ""


class FileSystem(object):

    def __init__(self):
        self.root = Node()

    def find(self, path):
      # start with root node
        curr = self.root
        # if length is one that's mean "/" return root
        if len(path) == 1:
            return self.root
        # for each dir go to the child
        for word in path.split("/")[1:]:
            curr = curr.child[word]
        return curr

    def ls(self, path):
      # reach to the node
        curr = self.find(path)
        # if it's file return content inside of it
        if curr.content:
            return [path.split("/")[-1]]
        # return list of dirs and files
        return sorted(curr.child.keys())

    def mkdir(self, path):
        # reach to the path only
        self.find(path)

    def addContentToFile(self, filePath, content):
      # reach to the node
        curr = self.find(filePath)
        curr.content += content

    def readContentFromFile(self, filePath):
      # reach to the node
        curr = self.find(filePath)
        return curr.content
