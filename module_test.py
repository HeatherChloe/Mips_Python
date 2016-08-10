##def to_unsigned(num):
##    unsigned_num = num & 0xffffffff
##        return unsigned_num


##NUM = to_unsigned(-1)
##print(NUM)
import os.path
import sys
src_name = "file_in.txt"
file_in_path = os.path.abspath(src_name)
print(file_in_path)
path = sys.path[0]
print(path)
folder_name = 'edited_version'
os.mkdir(os.path.join(path, folder_name))
