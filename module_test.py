##def to_unsigned(num):
##    unsigned_num = num & 0xffffffff
##        return unsigned_num


##NUM = to_unsigned(-1)
##print(NUM)



##import os.path
##import sys
##import shutil
##src_name = "05136064.txt"
##file_in_path = os.path.abspath(src_name)
##print(file_in_path)
##path = sys.path[0]
##print(path)
##folder_name = 'edited_version'

##no_name = path + folder_name
##if os.path.exists(no_name) == False:
##    os.mkdir(os.path.join(path, folder_name))
##    
##new_path = path + '\edited_version'
##print(new_path)
##shutil.copy(file_in_path, new_path)

#判断是否存在源文件 存在就删
##to_be_deleted_file = new_path + '\\' + src_name+ '.tmp'
##print(to_be_deleted_file)

##if os.path.exists(to_be_deleted_file):
##    os.remove(to_be_deleted_file)
##else:
##    fore_name = new_path + '\\' + src_name
##    now_name = to_be_deleted_file
##    os.rename(fore_name, now_name)
