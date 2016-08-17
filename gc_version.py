import os
import sys
import re
import shutil

usage = """Usage:
    cpu_comp file1 [file2...]"""
argv = sys.argv
argv = [ "", "file_in.txt" ]
if __name__ == "__main__":
    print(os.path.abspath('.')+'\\edited_version')
    if len(argv) == 1:
        print(usage)
    else:
        print("run in console")
        for filename in argv[1:]:
            print(filename)
            if os.path.exists(filename):
                pass
            else:
                print("file("+filename+") doesn't exist")
                continue
