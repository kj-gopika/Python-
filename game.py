import random
path="C:\Users\HP\Documents\list_of_words.txt"

l=[]
with open(path) as f:
    content=f.read().split('\n')
f.close   
d=len(content)
for i in range(0,d):
    if(len(content[i])>=0):
        l.append(content[i])

#print l 
d=len(content)


word=l[random.randint(0,d-2)]

print word
length=len(word)
print ('No of letters: '+ str(length))
shuffle=list(word)
random.shuffle(shuffle)

chances=len(word)-2
tries=0

c1=random.randint(0,len(word))
c2=random.randint(0,len(word))

hint=""
for i in range(0,len(word)):
    if i==c1 or i==c2:
        hint=hint+word[i]
    else:
        hint=hint+"*"
print hint

'''
for i in range(0,length-2):
    if(chances>0):
        j=raw_input('Enter letter: ')
        if(word[i]==j):
            hint[i]=j
        chances=chances-1   
    else:
        break    
    print hint    
if tries==chances:
    print "The answer was "+word'''
#word="applebird"
lword=word.lower()
word1=list(lword)
 
#x="a**l*****"
l=list(hint)
length=len(hint)
c=length-2
#print 'You have ' + str(c)+' chances left'
flag=False
 
while c>0 and flag==False:
    print ('No of chances left: '+str(c))
    print (''.join(l))
    c=c-1
    op=str(raw_input('Enter char: '))
    for j in range(0,length):
        if(word1[j]==op):
            l[j]=op
    if(l==word1):
        print ('You guessed right!')
        print word
        flag=True
       
       
if(flag==False):
    print ('Oops!')
    print ('The word is ' + word)
