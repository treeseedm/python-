sort=[4,2,5,1,3];
for index in range(1,len(sort)):
	t=sort[index];
	j=index-1;
	while j>=0 and t<sort[j]:
		sort[j+1]=sort[j];
		j=j-1;
	sort[j+1]=t;
	
print sort;
		