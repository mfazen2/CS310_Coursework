import os
import string
def file_read(file_name):
    L=[]
    D = {}
    try:
        chars = '!\"#$%&\'()*+,/:;<>?@[\]^`{|}~'
        f = open(file_name)
        while True:
            temp = str(f.readline().replace(" ",""))
            temp = temp.replace("\n","")
            temp = temp.replace("\t","")
            if len(temp) == 0: break
            if temp[0] == "=": return None
            if "=" not in temp: 
                f.close() 
                return None
            if "==" in temp: 
                f.close()
                return None
            for ch in temp:
                if ch in chars:
                    return None
            L = temp.split("=")
            if len(L) == 0: break
            L[1] = (L[1].replace(" ",""))
            L[0] = (L[0].replace(" ",""))
            if "." in L[1]: L[1] = float(L[1])
            else: L[1] = int(L[1])
            D[L[0]] = L[1]
        return D
    except IOError or SyntaxError:
        f.close()
        return None
def file_write(file_name,var_dict,overwrite=False):
    L = str(string.punctuation)
    L = L.replace("_","")
    L2 = string.ascii_letters + "_" + string.digits
    try:
        if (os.path.isfile(file_name) and overwrite == False): return None 
        f = open(file_name,'w')
        for pair in var_dict:
            if pair[0] not in L2: 
                os.remove(file_name)
                return None
            for ch in pair: 
                if ch in L: 
                    os.remove(file_name)
                    return None
            pair = pair.replace("\t","")
            pair = pair.replace(" ","")
            f.write(pair+" = "+str(var_dict.get(pair))+"\n")
    except IOError:
        os.remove(file_name)
        return None
    return True
