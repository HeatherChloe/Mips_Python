print("begin")
fp = open('file_in.txt','r')
opt_list = []
pc_index = []
rts = [0]
####################fore########################
####################fore########################
####################fore########################
def init_nd(nd):
    
    nd = int(nd)
    
    if nd < len(rts):
        return
    for i in range(0,nd):
        rts.append('null')
    return rts


def add_to_t(nt, rt):
    nt = int(nt)
    if nt in range(len(rts)):
        rts[nt] = rt
    elif nt == len(rts):
        rts.append(rt)
    else :
        indx = nt
        indx = int(indx)
        while(rts.index(rts[-1]) != indx):
            rts.append('null')
            indx -= 1
            if rts.index(rts[-1]) == nt - 1:
                break
            rts.append(rt)
    return rts
def add_to_d(nd, rd):
    nd = int(nd)
    if nd in range(main.len(rts)):
        rts[nd] = rd
    elif nd == main.len(rts):
        rts.append(rd)
    else:
        indx = nd
        while(rts.index(rts[-1]) != indx):
            rts.append('null')
            indx -= 1
            if rts.index(rts[-1]) == nd - 1:
                break
            rts.append(rd)
    return rts
#鍘绘帀0b
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

    def getnt():
        nt = opt[1].replace("$", "").zfill(5)
        return nt
    def getns():
        ns = opt[2].replace("$", "").zfill(5)
        return ns    
    def getimm():
        imm16 = opt[3].replace("0x", "")
        return imm16
    def ext(imm16):
        arr2 = []
        strin_fin = ""
        for r in imm16:
            if r != '0':
                r = bin(int(r,16)).replace("0b", "").zfill(4)
                arr2.append(r)
                #strin = ""
                strin_fin = ""
                strin_fin = ''.join(arr2)
        return strin_fin
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
    def get_ns():
        ns = int(opt[2].replace("$", "").zfill(5))
        return ns
    def get_nd():
        nd = int(opt[1].replace("$", "").zfill(5))
        return nd
    def get_nt():
        nt = int(opt[3].replace("$", "").zfill(5))
        return nt


####################func########################
####################func########################
####################func########################
        #for i in opt_list: read(i)
def ori(nt, rs, imm16):
    imm16_n = I.ext(imm16)
    #print("rs:"+rs)
    a = rmv(imm16_n)
    rd = "%05d" % (int(rs)|int(a))
    add_to_t(nt, rd)
    return rd

def addiu(nt, ns, imm16):
    imm16_n  = rmv(I.ext(imm16))
    rd       = int(rts[ns]) + int(imm16_n)
    add_to_t(nt, rd)
    return rd

def add(nd, ns, nt):
    rd = int(rts[ns]) + int(rts[nt])
    add_to_t(nd, rd)
    return rd
def addu(nd, ns, nt):
    rd = int(rts[ns]) + int(rts[nt])
    add_to_t(nd, rd)
    return rd
def sub(nd, ns, nt):
    rd = int(rts[ns]) - int(rts[nt])
    add_to_t(nd, rd)
    return rd
def subu(nd, ns, nt):
    rd = int(rts[ns]) - int(rts[nt])
    add_to_t(nd, rd)
    return rd
#小于置一 rd = ns-nt 小于0 rd置1
def slt(nd, ns, nt):
    tmp = int(rts[ns]) - int(rts[nt])
    if tmp < 0:
        rd = 1
    else:
        rd = 0
    add_to_t(nd, rd)
    return rd
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
                n = lin.split(' ')
                st = n[1].split(',')
                l = st
                l.insert(0, n[0])
                add_to_index()
                opt_list.append(l)
                del l
                l = []

                
    for opt in opt_list:
        print(opt)
        if opt[0]       == 'ori':
            op          = '001101'
            ns          = I.getns()
            imm16       = I.getimm()
            nt          = I.getnt()
            ext         = I.ext_16_str(I.ext(imm16))
            init_nd(nt)
            rt          = ori(nt, ns, imm16)
            nt          = rmv(bin(int(nt))).zfill(5)
            ns          = rmv(bin(int(ns))).zfill(5)
            #print("#32'b" + op + "_" + ns + "_" + nt + "_" + '_'.join(ext[i:i + 4] for i in range(0, len(ext),4)))
            #print(rts)
        if opt[0] == 'addiu':
            op          = '000000'
            ns          = R.get_ns()
            rs          = rts[ns]
            nt          = I.getnt()
            imm16       = I.getimm()
            rt          = addiu(nt, ns, imm16)
            #ext         = I.ext_16_str(rmv(I.ext_16_str(I.ext(imm16))))
            ext         = I.ext_16_str(I.ext(imm16))
            init_nd(nt)
            nt          = rmv(bin(int(nt)))
            ns          = rmv(bin(int(ns)))
            print(l)
            print("#32'b" + op + "_" + str(ns).zfill(5) + "_" + str(nt).zfill(5) + "_" + '_'.join(ext[i:i+4] for i in range(0, len(ext),4)))
            print(rts)
            
            
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
            print("after_add")
            print(rts)
            
        if opt[0] == 'sub':
            op    = '00000'
            shamt = '00000'
            func  = '100010'
            ns    = R.get_ns()
            nt    = R.get_nt()
            nd    = R.get_nd()
            rd    = sub(nd, ns, nt)
            init_nd(nd)
            print(l)
            ns    = rmv(bin(int(ns)))
            nt    = rmv(bin(int(nt)))
            nd    = rmv(bin(int(nd)))
            print("#32'b" + op +'_'+ str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5)+ '_' + shamt + '_' +func)



        if opt[0] == 'subu':
            op    = '000000'
            shamt = '00000'
            func  = '100010'
            ns    = R.get_ns()
            nt    = R.get_nt()
            nd    = R.get_nd()
            rd    = subu(nd, ns, nt)
            init_nd(nd)
            print(l)
            ns    = rmv(bin(int(ns)))
            nt    = rmv(bin(int(nt)))
            nd    = rmv(bin(int(nd)))
            print("#32'b" + op +'_'+ str(ns).zfill(5) + '_' + str(nt).zfill(5) + '_' + str(nd).zfill(5)+ '_' + shamt + '_' +func)

        #if opt[0] == 'slt'
        #if opt[0] == 'sltu'  
print(pc_index)
print(opt_list)




























