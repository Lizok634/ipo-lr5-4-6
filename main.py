f=open('text.txt','r',encoding='utf-8')
text=f.readlines()
f1=open('output.txt','w',encoding='utf-8')
for line in text:
    f1.write(line[::-1])
f.close()
f1.close()
    