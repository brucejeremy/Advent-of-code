import os
import sys
sys.path.append( os.path.join( os.getcwd(), '..', '..') )
from speed import timer_func
###################################################################

class directory:

    def __init__(self):
        self.curr = []
        self.dir = {'/': {} }
        self.folders = {'/': 0}

    def cd(self, level):
        if level == '..':
            self.curr = self.curr[:-1]
        else:
            self.curr.append(level)
    
    def ls(self, contents):
        curr_folder = self.dir
        for folder in self.curr:
            curr_folder = curr_folder[folder]
        size = 0
        for item in contents:
            if item[0] == 'dir':
                self.folders[f'{"/".join(self.curr)}/{item[1]}'] = 0
                curr_folder[item[1]] = {}
            else:
                curr_folder[item[1]] = int(item[0])
                size += int(item[0])
        # Update folder sizes
        for idx in range(len(self.curr)):
            path = self.curr if idx == 0 else self.curr[:-idx]
            self.folders[f'{"/".join(path)}'] += size

directory = directory()

def build_directory():
    with open('cmds.txt', 'r') as data:

        in_ls = False
        ls_contents = []
        for line in data.readlines():
            parts = line.strip().split(' ')
            if parts[0] == '$':
                if in_ls:
                    directory.ls(ls_contents)
                    ls_contents = []
                    in_ls = False
                if parts[1] == 'ls':
                    in_ls = True
                else:
                    directory.cd(parts[2])
            else:
                ls_contents.append(parts)
        if in_ls:
            directory.ls(ls_contents)


@timer_func
def first_star(): 
    build_directory()

    MAX_SIZE = 100_000
    total_size = 0
    for _, size in directory.folders.items():
        if size <= MAX_SIZE:
            total_size += size

    return f'1. The total size of all folders <= 100,000 is {total_size}'

@timer_func
def second_star():
    
    space_to_delete = 30_000_000 - (70_000_000 - directory.folders['/'])

    del_folder = ''
    del_size = 70_000_000
    for folder, size in directory.folders.items():
        if size - space_to_delete > 0 and size < del_size:
            del_size = size
            del_folder = folder

    return f'2. The total size of the smallest directory to delete ({del_folder}) is {del_size}'

if __name__ == '__main__':
    first_star()
    second_star()