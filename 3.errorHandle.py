# -*- coding: utf-8 -*-
import winners
# 1 : ./KEYWORD/total.txt 의 키워드를 가져온다.
keywords = winners.getSetFromFile("./ERROR/"+winners.getLastErrorFileName())
# 2 : 루프로 돌리면서 없는 것을 업체명으로 추가한다.
timeStamp = winners.timeStamp()
results = open("./RESULT/"+timeStamp+" 결과.txt","w")
errors = []
for index,keyword in enumerate(keywords):
    newData = winners.getDaumResult(keyword)
    oldData = winners.getOldData(keyword)
    print(index+1,".",keyword,"-",list(newData))
    # oldData 는 있는데 newData 가 비어있을 경우 에러처리
    if(newData.__len__() == 0 and oldData.__len__() != 0):
        errors.append(keyword)
    newData -= oldData
    winners.updateData(keyword,newData)
    if newData.__len__() :
        print("\t신규:",list(newData))
        results.write(keyword+":\n\t"+str(newData)+"\n")
results.close()
if(errors.__len__()>0):
    f = open("./ERROR/"+timeStamp+" 에러.txt","w")
    f.write("\n".join(errors))
    f.close()