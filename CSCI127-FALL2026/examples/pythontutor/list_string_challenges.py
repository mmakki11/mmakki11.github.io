# Source: index.html link "List/String Challenges" (pythontutor.com)
sports = ["Field Hockey","Swimming","Water Polo"]
mess = "Qoauxca BrletRce crcx qvBnqa ocUxk"
result = ""
for i in range(len(mess)):
    if i % 3 == 0:
        print(mess[i])
        result = result + mess[i]
print(sports[1], result)
