#ReadTxt_demo.py

def readTxt(filePath):
    fo = open(filePath,'r')
    lines = fo.readlines()
    for data in lines:
        name, pwd = data.split(',')

    return name,pwd

filePath = 'userInfo.txt'
re_name,re_pwd = readTxt(filePath)

if __name__=="__main__":
    pass