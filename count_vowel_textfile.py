

wifi=open('Pass.txt','w')
x=input('Type in : ')
wifi.close()
p=open('Pass.txt')
gg=p.read()
count=0
for a in x:
	if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
		count+=1
	
print(count)


wifi.close()
