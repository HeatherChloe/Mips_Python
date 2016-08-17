
import os.path
import sys
import os
try:
    import shutil
except:
    print("failed to import shutil")
    sys.exit(0)
src_name = "file_in.txt"


print("begin")
##############################################################
##################do sth with file############################
##############################################################
src_name = "file_in.txt"
file_in_path = os.path.abspath(src_name)
path = sys.path[0]
folder_name = 'edited_version'

no_name = path + '\\' + folder_name
if os.path.exists(no_name) == False:
    os.mkdir(os.path.join(path, folder_name))

new_path = path + '\\edited_version'
print(new_path)
shutil.copy(file_in_path, new_path)

#判断是否存在.tmp 存在就删
with_tmp_file = (new_path + '\\' + src_name+ '.tmp')

if os.path.exists(with_tmp_file) == True:
    os.remove(with_tmp_file)

fore_name = new_path + '\\' + src_name
now_name = with_tmp_file
os.rename(fore_name, now_name)

##############################################################
#################done sth with file###########################
##############################################################


temp = 5
fp = None
while temp >0 :
    try:
        fp = open(now_name,'r+')
    except:
        temp -= 1
    finally:
        break
if fp == None:
    sys.exit(0)

opt_list = []
pc_index = []
reg = [0]
mem = {}

####################fore########################
####################fore########################
####################fore########################
#"mmmmm"
#"lllll"
#"11111"
def unsigned(num):
    unsigned_num = num & 0xffffffff
    return unsigned_num

def print_opt_list():
    for i in opt_list:
        print('-------------'+ str(pc_index[opt_list.index(i)]) + '--------------')
        print(i)

def init_nd(nd):
    nd = int(nd)
    if nd < len(reg):
        return
    for i in range(0,nd):
        reg.append('null')
    return reg


def add_to_reg(nt, rt):
    nt = int(nt)
    if nt in range(len(reg)):
        reg[nt] = rt
    elif nt == len(reg):
        reg.append(rt)
    else :
        indx = nt
        indx = int(indx)
        while(reg.index(reg[-1]) != indx):
            reg.append('null')
            indx -= 1
            if reg.index(reg[-1]) == nt - 1:
                break
            reg.append(rt)
    return reg
def add_to_d(nd, rd):
    nd = int(nd)
    if nd in range(main.len(reg)):
        reg[nd] = rd
    elif nd == main.len(reg):
        reg.append(rd)
    else:
        indx = nd
        while(reg.index(reg[-1]) != indx):
            reg.append('null')
            indx -= 1
            if reg.index(reg[-1]) == nd - 1:
                break
            reg.append(rd)
    return reg

def add_to_mem(nd, rd):
    mem[nd] = rd
    return mem

#0b
def rmv(num):
    num = num.replace("0b", "")
    return num
#pc[0,4,8]
def add_to_index():
    if pc_index != []:
        pc_index.append(pc_index[-1]+4)
    else:
        pc_index.append(0)
class I():
    def __init__(self, op, rs, rt, imm16):
        self.op         = op
        self.rs         = rs
        self.rt         = rt
        self.imm16      = imm16

    def get_nt():
        nt = opt[1].replace("$", "").zfill(5)
        return nt
    def get_ns():
        ns = opt[2].replace("$", "").zfill(5)
        return ns
    def getimm():
        imm16 = opt[3].replace("0x", "")
        return imm16
    def ext(imm16):
        imm16 = int(imm16,16)
        imm16 = bin(imm16).replace('b','')
        return imm16
##        for r in imm16:
            #print(imm16)
##            if r != '0':
##               stri = bin(int(r,16)).replace("0b", "").zfill(4)
                #print(r)
                #arr2.append(r)
                #strin = ""
                #strin_fin = ""
                #strin_fin = ''.join(arr2)
##        return r
    def ext_16_str(stri):
        ext_16 = stri.zfill(16)
        return ext_16

class R():
    #add rd, rs, rt
    #op  rs, rt, rd
    def __init__(self, op, rs, rt, rd, shamt):
        self.op         = op
        self.rs         = rs
        self.rt         = rt
        self.rd         = rd
        self.shamt      = shamt
    def get_ns():
        ns = int(opt[2].replace("$", "").zfill(5))
        return ns
    def get_nd():
        nd = int(opt[1].replace("$", "").zfill(5))
        return nd
    def get_nt():
        nt = int(opt[3].replace("$", "").zfill(5))
        return nt
    def get_shamt():
        shamt = int(opt[3].zfill(5))
        return shamt
class J():
    def __init__(self, target):
        self.target = target

################################################
####################func########################
################################################

####################TYPE########################
#####################I##########################
def ori(nt, rs, imm16):
    imm16_n = I.ext(imm16)
    a = rmv(imm16_n)
    rd = "%05d" % (int(rs)|int(a))
    add_to_reg(nt, rd)
    return rd

def addiu(nt, ns, imm16):
    imm16_n  = rmv(I.ext(imm16))
    rd       = int(reg[int(ns)]) + int(imm16_n)
    add_to_reg(nt, rd)
    return rd

def sw(nt, ns, imm16):
    nt = int(nt)
    ns = int(ns)
    imm16_n = int(rmv(I.ext(imm16)))
    
    mem_key = int(int(reg[ns]) + imm16_n)
    print(mem_key)
    mem_val = int(reg[nt])
    mem[mem_key] = mem_val
    
    print(mem)
    return mem_val

#    mem[reg[ns]+imm16] = reg[nt]

##def lw(nt, ns, imm16):
##    nt = int(nt)
##    ns = int(ns)
##    imm16_n = int(rmv(I.ext(imm16)))
##    print(imm16_n)
##    print(int(reg[ns]))
##    print(int(reg[ns]) + imm16_n)
##    rt = mem[int(reg[ns]) + imm16_n]
##    add_to_reg(nt, rt)
##    return rt

#    reg[nt] = mem[reg[ns]+imm16]
#def beq:
####################TYPE########################
#####################R##########################
def add(nd, ns, nt):
    rd = int(reg[ns]) + int(reg[nt])
    add_to_reg(nd, rd)
    return rd

def addu(nd, ns, nt):
    rd = unsigned(int(reg[ns])) + unsigned(int(reg[nt]))
    add_to_reg(nd, rd)
    return rd

def sub(nd, ns, nt):
    rd = int(reg[ns]) - int(reg[nt])
    add_to_reg(nd, rd)
    return rd

def subu(nd, ns, nt):
    rd = unsigned(int(reg[ns])) - unsigned(int(reg[nt]))
    add_to_reg(nd, rd)
    return rd

def slt(nd, ns, nt):
    tmp = int(reg[ns]) - int(reg[nt])
    if tmp < 0:
        rd = 1
    else:
        rd = 0
    add_to_reg(nd, rd)
    return rd

def sltu(nd, ns, nt):
    tmp = unsigned(int(reg[ns])) - unsigned(int(reg[nt]))
    if tmp < 0:
        rd = 1
    else:
        rd = 0
    add_to_reg(nd, rd)
    return rd

def sll(nd, nt, shamt):
    rd = rmv(bin(reg[nt] << shamt)).zfill(32)
    add_to_reg(rd)
    return rd

def srl(nd, nt, shamt):
    rd = rmv(bin(reg[nt] >> shamt)).zfill(32)
    add_to_reg(rd)
    return rd

##def sra(nd , nt, shamt):
##    shamt = int(shamt)
##    nt = int(nt)
##    print(nt)
##    print(reg[rt])
##    rd = bin(reg[nt] >> shamt)
##    if bin(reg[nt])[0] == 1:
##        rd = rd.rjust(32, [1])
##    else:
##        rd = rd.zfill(32)
##    add_to_reg(rd)
##    return rd

#rt左移shamt的位数 存在rd里


####################TYPE########################
#####################J##########################


#def j(target):
#

####################main########################
####################main########################
####################main########################
for line in fp:
    L = []
    n = []
    count = 0
    if 'main' not in line:
        count += 1
    elif 'main' in line:
        if line.split(':')[0] == 'main':
            stri = line[5:-1]
            stri = ' '.join(stri.split())
            L = stri.split(' ')
            string = L[1].split(',')
            l = []
            l = string
            l.insert(0,L[0])
            add_to_index()
            opt_list.append(l)
            del l
            l = []
            for line in fp.readlines()[count:]:
                lin = str(line).lstrip()
                lin = lin.replace('\n', '')
                lin = ' '.join(lin.split())


                if not line.split():
                    continue
                elif lin[0] == '#':
                    continue


                else:
                    n = lin.split(' ')
                    st = n[1].split(',')
                    l = st
                    #print(l)
                    l.insert(0, n[0])
                    #print(l)

                    add_to_index()
                    opt_list.append(l)
                    del l
                    l = []

                #if lin.staregwith('#')or not line.split():
                    #continue



    for opt in opt_list:
        print(opt)
        if opt[0]       == 'ori':
            op          = '001101'
            ns          = I.get_ns()
            imm16       = I.getimm()
            nt          = I.get_nt()
            ext         = I.ext_16_str(I.ext(imm16))
            init_nd(nt)
            rt          = ori(nt, ns, imm16)
            nt          = rmv(bin(int(nt))).zfill(5)
            ns          = rmv(bin(int(ns))).zfill(5)
            print("#32'b" + op + "_" + ns + "_" + nt + "_" + '_'.join(ext[i:i + 4] for i in range(0, len(ext),4)))
            print(reg)
            print("--------------------------")


        if opt[0] == 'addiu':
            op          = '000000'
            ns          = I.get_ns()
            rs          = int(reg[int(ns)])
            nt          = I.get_nt()
            imm16       = I.getimm()
            rt          = addiu(nt, ns, imm16)
            #ext         = I.ext_16_str(rmv(I.ext_16_str(I.ext(imm16))))
            ext         = I.ext_16_str(I.ext(imm16))
            init_nd(nt)
            nt          = rmv(bin(int(nt)))
            ns          = rmv(bin(int(ns)))
            #print(l)
            print("#32'b" + op + "_" + str(ns).zfill(5) + "_" + str(nt).zfill(5) + "_" + '_'.join(ext[i:i+4] for i in range(0, len(ext),4)))
            print(reg)
            print("--------------------------")


        if opt[0] == 'add':
            op    = '00000'
            func  = '100000'
            shamt = '00000'
            ns    = R.get_ns()
            nt    = R.get_nt()
            nd    = R.get_nd()
            rd    = add(nd, ns, nt)
            init_nd(nd)
            print(l)
            ns = rmv(bin(int(ns)))
            nt = rmv(bin(int(nt)))
            nd = rmv(bin(int(nd)))
            print("#32'b" + op +'_'+ str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5)+ '_' + shamt + '_' +func)
##            print("after_add")
            print(reg)
            print("--------------------------")


        if opt[0] == 'sub':
            op    = '00000'
            shamt = '00000'
            func  = '100010'
            ns    = R.get_ns()
            nt    = R.get_nt()
            nd    = R.get_nd()
            rd    = sub(nd, ns, nt)
            init_nd(nd)
            #print(l)
            ns    = rmv(bin(int(ns)))
            nt    = rmv(bin(int(nt)))
            nd    = rmv(bin(int(nd)))
            print("#32'b" + op +'_'+ str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5)+ '_' + shamt + '_' +func)
            print(reg)
            print("--------------------------")


        if opt[0] == 'subu':
            op    = '000000'
            shamt = '00000'
            func  = '100010'
            ns    = R.get_ns()
            nt    = R.get_nt()
            nd    = R.get_nd()
            rd    = subu(nd, ns, nt)
            init_nd(nd)
            #print(l)
            ns    = rmv(bin(int(ns)))
            nt    = rmv(bin(int(nt)))
            nd    = rmv(bin(int(nd)))
            print("#32'b" + op +'_'+ str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5)+ '_' + shamt + '_' +func)
            print(reg)
            print("--------------------------")


        if opt[0] == 'slt':
            op    = '000000'
            shamt = '00000'
            ns    = R.get_ns()
            nt    = R.get_nt()
            nd    = R.get_nd()
            rd = slt(nd, ns, nt)
            init_nd(nd)
            ns    = rmv(bin(int(ns)))
            nt    = rmv(bin(int(nt)))
            nd    = rmv(bin(int(nd)))
            print("#32'b" + op +'_'+ str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5)+ '_' + shamt + '_' +func)
            print(reg)
            print("--------------------------")


        if opt[0] == 'sltu':
            op    = '000000'
            shamt = '00000'
            ns    = R.get_ns()
            nt    = R.get_nt()
            nd    = R.get_nd()
            rd = slt(nd, ns, nt)
            init_nd(nd)
            ns    = rmv(bin(int(ns)))
            nt    = rmv(bin(int(nt)))
            nd    = rmv(bin(int(nd)))
            print("#32'b" + op +'_'+ str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5)+ '_' + shamt + '_' +func)
            print(reg)
            print("--------------------------")


        if opt[0] == 'sw':
            op = '101011'
            ns = I.get_ns()
            nt = I.get_nt()
            imm16       = I.getimm()
            rt          = sw(nt, ns, imm16)
            ext         = I.ext_16_str(I.ext(imm16))
            #init_nd(nt)
            nt          = rmv(bin(int(nt)))
            ns          = rmv(bin(int(ns)))
            print("#32'b" + op + "_" + str(ns).zfill(5) + "_" + str(nt).zfill(5) + "_" + '_'.join(ext[i:i+4] for i in range(0, len(ext),4)))
            print(reg)
            print("--------------------------")

            
        if opt[0] == 'lw':
            op = '100011'
            ns = I.get_ns()
            nt = I.get_nt()
            imm16       = I.getimm()
            rt          = lw(nt, ns, imm16)
            ext         = I.ext_16_str(I.ext(imm16))
            #init_nd(nt)
            nt          = rmv(bin(int(nt)))
            ns          = rmv(bin(int(ns)))
            #print(l)
            print("#32'b" + op + "_" + str(ns).zfill(5) + "_" + str(nt).zfill(5) + "_" + '_'.join(ext[i:i+4] for i in range(0, len(ext),4)))
            print(reg)
            print("--------------------------")
##        if opt[0] == 'sra':
##            op = '000000'
##            rs = '00111'
##            nd = R.get_nd()
##            nt = R.get_ns()
##            shamt = R.get_shamt()
##            func = '101100'
##            rd = sra(nd, nt, shamt)
##            print("#32'b" + op +'_'+ rs + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5)+ '_' + shamt + '_' +func)

##print_opt_list()
print(mem)
fp.close()
























