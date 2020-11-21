
def charlen(stri):
    dic={}
    for i in stri:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return len(dic)
def distance(s):
    length=len(s)
    if length==0 or length==1:
        print(length)
    maxc=charlen(s)
    m=length+1
    a={}
    start=0
    a[s[start]]=1
    for i in range(1,length):
        if s[i] in a:
            a[s[i]]+=1
        else:
            a[s[i]]=1
        if len(a)==maxc:
            while start<i and a[s[start]]>1:
                a[s[start]]-=1
                start+=1
            if m>i+1-start:
                m=i+1-start
    print(m)
s=str(input())
distance(s)