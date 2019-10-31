wordsFreqDict = {
    "hello": 56,
    "zat" : 23 ,
    "at" : 23 ,
    "gt" : 23 ,
    "test" : 43,
    "this" : 43
    }

# Create a list of tuples sorted by value field and then key
listofTuples = sorted(wordsFreqDict.items(),  key=lambda x: (x[1], x[0]))
 
# Iterate over the sorted sequence
for elem in listofTuples :
    print(elem)


