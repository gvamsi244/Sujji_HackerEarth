import re

def print_hi(name):
    print(f'Hi, {name}')

def tokenize_string(S):
    flag=0
    list1 = []
    str =""
    i=-1
    for c in S:
        i+=1
        if(c=='"'):
            flag+=1
        if(flag==0):
            if(c==' '):
                if(str!=''):
                    list1.append(str)
                str=""
            else:
                str+=c
        if(flag==1): #open
            str+=c
        if(flag==2): #closing
            if(i+1<len(S)):
                if(S[i+1]=='"'):
                    str+=c
                    flag=0
                else:
                    str+=c
                    list1.append(str)
                    flag=0
                    str=""
            else:
                str += c
                list1.append(str)
                flag = 0
                str = ""

    if(str!=''):
        list1.append(str)
    for j in list1:
        print(j)

if __name__ == '__main__':
    str = "abc def ghi \"jkl    as\"\"mno pqr\" hihi \"tuv xyz\"  \"aabbcc\""
    #abc def ghi "jkl    as"  "mno pqr" hihi "tuv xyz"  "aabbcc"
    # str3=input()
    tokenize_string(str)
    # print_hi('PyCharm')
    #"abc"
