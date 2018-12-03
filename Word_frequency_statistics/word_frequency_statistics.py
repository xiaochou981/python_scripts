import os
from functools import reduce

# Search all files in target path
def getfiles(path):
    if not path:
        raise Exception("path error! input path not correct.")
    
    files = os.listdir(path)
    result = []
    for file in files:
        if file.split(".")[-1] == "txt":
            result.append(file)
    
    return result


def Formatword(word):
    result = []
    if not word:
        return result
        
    while not word[0].isalpha():
        word = word[1:]
        if not word:
            return result
    while not word[-1].isalpha():
        word = word[:-1]
        if not word:
            return result
            
    start = 0
    for index in range(len(word)):
        if not word[index].isalpha():
            result.append(word[start:index])
            start = index + 1
    if not result:
        result.append(word)
    return result

#read file and return the word list
def readfiles(filename):
    file = open(filename, "r")
    word_list = []
    frequece_list = []
    for line in file.readlines():
        words = map(Formatword, line.split(" "))
        for word in words:
            if word in word_list:
                index = word_list.index(word)
                frequece_list[index] = frequece_list[index] + 1
            else:
                word_list.append(word)
                frequece_list.append(1)
    
    if len(frequece_list) != len(word_list):
        raise Exception("read files proccess error.")
    
    file.close()
    result = []
    [result.append((x, y)) for x in frequece_list for y in word_list]
        
    return result


#read the word list to get the frequece
def MergeFrequency(list1, list2):
    word1,num1=zip(*list1)
    merge_list = []
    
    #将list2中的word加入到merge_list
    for word,num in list2:
        if not word in word1:
            merge_list.append((word,num))
        else:
            index = word1.index(word)
            merge_list.append((word,num+num1[index]))
    
    #将list1中没有统计到merge_list的word加入
    word2,num2=zip(*list2)        
    for word,num in list1:
        if not word in word2:
            merge_list.append((word,num))
            
    return merge_list


#sort the list and print the output
def SetOutput(result):
    #sort them from most to least
    sorted_list = sorted(result, key=lambda word:word[1],reverse=True)
    #print them
    for word in iter(sorted_list):
        print(word)
        
        
if __name__=="__main__":
    path=__file__
    files = getfiles(os.getcwd())
    wordlists = map(readfiles, files)
    result = reduce(MergeFrequency, list(wordlists))
    SetOutput(result)