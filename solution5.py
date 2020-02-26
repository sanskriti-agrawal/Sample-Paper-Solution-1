l=list(map(int,input().split(" "))
c=list()
for i in l:
	f=1
	while i!=0:
		f=f*i
		i=i-1
	c.append(f)
print(c)
