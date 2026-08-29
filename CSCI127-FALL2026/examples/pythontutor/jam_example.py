# Source: index.html link "Jam Example" (pythontutor.com)
def+prob4():
++++verse+=+"jam+tomorrow+and+jam+yesterday,"
++++print("The+rule+is,")
++++c+=+mystery(verse)
++++w+=+enigma(verse,c)
++++print(c,w)
def+mystery(v):
++++print(v)
++++c+=+v.count("jam")
++++return(c)
def+enigma(v,c):
++++print("but+never",+v[-1])
++++for+i+in+range(c):
++++++++print("jam")
++++return("day.")
prob4()
