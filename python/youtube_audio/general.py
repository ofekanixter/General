import os

SHARPS="################################\n"

def deleteFile(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file {path} does not exist: ".format(path))

def str_list(l, newLine=True):
    s=""
    for i in l:
        if newLine:
            s=s+i+"\n"
        else:
            s=s+i
    return s[:-1] if  newLine else s

def print_msg(msg,sharps=False,strartLine=False,endLine=False):
    if(sharps):
        if (strartLine):
            print("\n"+SHARPS+msg+"\n"+SHARPS)
        else:
            print(SHARPS+msg+"\n"+SHARPS)
    else:
        if (strartLine and endLine):
            print("\n"+msg+"\n")
        elif(strartLine):
            print("\n"+msg)
        elif(endLine):
            print(msg+"\n")
        else:
            print(msg)