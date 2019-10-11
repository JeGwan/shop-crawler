# -*- coding: utf-8 -*-
def getFileList():
    import os
    return os.listdir('./KEYWORD')

def getSetFromFile(path):
    keywords = set()
    f = open(path,"r")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "": continue
        keywords.add(line)
    f.close()
    return keywords

def setNewKeywords(newKeywords):
    oldKeywords = getSetFromFile("./KEYWORD/total.txt")
    print("new 키워드:",newKeywords.__len__())
    print("old 키워드:",oldKeywords.__len__())
    newKeywords -= oldKeywords
    print("net 키워드:",newKeywords.__len__())
    f = open("./KEYWORD/total.txt","a")
    for keyword in newKeywords:
        f.write(keyword+"\n")
    f.close()

def getDaumResult(keyword):
    import requests
    from bs4 import BeautifulSoup
    url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q='+keyword 
    soup = requests.get(url)
    soup = BeautifulSoup(soup.content, 'html.parser')
    soup = soup.findAll(attrs={"data-idx":True})
    results = set()
    for data in soup:
        data = data.find(attrs={"class":"fn_tit"})
        if data:
            results.add(data.text)
    return results

def isFile(path):
    import os
    return os.path.isfile(path)

def getOldData(keyword):
    path = "./DB/"+keyword+".txt"
    if isFile(path) :
        oldData = getSetFromFile(path)
    else:
        f = open(path,"w")
        f.close()
        oldData = set()
    return oldData

def updateData(keyword, newData):
    f = open("./DB/"+keyword+".txt","a")
    for data in newData:
        f.write(data+"\n")
    f.close()

def timeStamp():
    from datetime import datetime
    return str(datetime.now())[:-7]

def getLastErrorFileName():
    import os
    errors = list(os.listdir("./ERROR"))
    if (errors.__len__() == 0):
        print("에러 파일이 없음")
        exit()
    errors.sort()
    return errors.pop()
