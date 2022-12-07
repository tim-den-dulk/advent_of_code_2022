import re

from get_inputs import GetInputs

class DirOrFile:
    def __init__(self, name, type, parent, size):
        self.name = name
        self.type = type
        self.parent = parent
        self.size = size
        self.childs = []

    def get_child_dir(self, name):
        for child in self.childs:
            if child.name == name:
                return child
        raise Exception("not found")
    def subdir(self, name):
        childdir = DirOrFile(name, "dir", self, 0)
        self.childs.append(childdir)
        return childdir

    def file(self, name, size):
        childfile = DirOrFile(name, "file", self, size)
        self.childs.append(childfile)
    def filesize(self):
        if self.type == "file":
            return self.size
        if self.type == "dir":
            size = 0
            for child in self.childs:
                size += child.filesize()
            return size

    def __repr__(self):
        if self.type == "dir":
            return "D " + self.name
        if self.type == "file":
            return "F " + self.name


data = GetInputs(7).lines()
basedir = DirOrFile("/","dir", None, 0)
active_dir = basedir
for line in data[1:]:
    if re.match(r"\$ cd \.\.", line):
        active_dir = active_dir.parent
    elif re.match(r"\$ cd", line):
        dir = re.findall(r"\$ cd (.+)", line)
        active_dir = active_dir.get_child_dir(dir[0])
    elif re.match(r"dir", line):
        dir = re.findall(r"dir (.+)", line)
        active_dir.subdir(dir[0])
    elif re.match(r"\d+", line):
        res = re.search(r"(\b[0-9]+\b) (\b.*)", line)
        size = res.group(1)
        filename = res.group(2)
        active_dir.file(filename,int(size))

class Size:
    def __init__(self):
        self.total = 0
        self.sizes = []

    def getsizes(self, dir):
        for child in dir.childs:
            if child.type == "dir":
                if child.filesize() < 100000:
                    print(child.name + " "+ str(child.filesize()))
                    self.total +=child.filesize()
                self.sizes.append(child.filesize())
                self.getsizes(child)


res = Size()
res.getsizes(basedir)
print(res.total)
# pt 2
filesystem = 70000000
space_used = basedir.filesize()
free_space = filesystem-space_used
free_space_needed = 30000000
to_free_up = free_space_needed-free_space
print("to free up: ", to_free_up)
res.sizes.sort()
for dir in res.sizes:
    if dir >= to_free_up:
        print(dir)
        break

