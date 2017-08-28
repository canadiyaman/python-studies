#!/usr/bin/env python3


#Implement a group_by_owners function that:

#Accepts a dictionary containing the file owner name for each file name.
#Returns a dictionary containing a list of file names for each owner name, in any order.
#For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.





class FileOwners:

    @staticmethod
    def group_by_owners(files):
        owners = {}
        for file in files.keys():
            owner = files[file]
            if owner in owners:
                owners[owner].append(file)
            else:
                owners[owner] = [file]

        return owners

if __name__ == '__main__':
    files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
    print(FileOwners.group_by_owners(files))



