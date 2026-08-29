# Source: index.html link "Decisions &amp; Functions Example" (pythontutor.com)
#Fall+2013+Final+Exam,+5

def+kuwae(+inLst+):
++++tot+=+1
++++for+item+in+inLst:
++++++++tot+=+tot+*+item
++++return+tot

def+foo(+inLst+):
++++if+(+inLst[-1]+>+inLst[0]+):
++++++++return+kuwae(+inLst+)
++++else:
++++++++return+-1
++++++++
foo(+[2,+4,+6,+8]+)

foo(+[4002,+328,+457,+1]+)
