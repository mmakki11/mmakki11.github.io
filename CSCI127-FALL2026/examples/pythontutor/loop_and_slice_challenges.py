# Source: index.html link "Loop &amp; Slice Challenges" (pythontutor.com)
word = "Hunter"
for i in range(2,10,3):
    for c in word:
        print(i,c, end = "")
    print()
    
pali = "a man a plan a canal Panama"
print(pali[0], pali[-1])
print(pali[2:5], pali[-4:-1])

qPop = [152999,284041,469042,1079129,1297634,
    1550849,1809578,1986473,1891325,1951598,
    2229379,2230722]
print("Queens population in 1900:", qPop[0])
print("Since 2000:", qPop[-3:len(qPop)])
