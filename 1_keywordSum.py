# -*- coding: utf-8 -*-
import winners

# 0. KEYWORD 폴더 내의 모든 txt파일 리스트 불러오기
fileList = winners.getFileList()
# 1. fileList의 파일을 하나씩 열어서 set으로 준비하기
newKeywords = set()
for fileName in fileList:
    newKeywords.update(winners.getSetFromFile("./KEYWORD/"+fileName))
# 2. 기존에 있던 키워드 디비에 병합시킴
winners.setNewKeywords(newKeywords)