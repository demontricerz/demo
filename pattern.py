n=int(input())
st="123456789abcdefghijklmnopqrstuvwxyz"
step=0
for i in range(1,n+1):
	print(" "*(n-i)+st[step:step+(i*2-1)]+(st*int(((i*2-1)-(35-step))/35))+(st[:(step+(i*2-1))%35] if((step+(i*2-1))>35) else "")+(" "*(n-i)))
	step=(step+(i*2-1))%35
for i in range(n-1,0,-1):
	print(" "*(n-i)+st[step:step+(i*2-1)]+(st*int(((i*2-1)-(35-step))/35))+(st[:(step+(i*2-1))%35] if((step+(i*2-1))>35) else "")+(" "*(n-i)))
	step=(step+(i*2-1))%35
