
sortList=[3,4,2,1,8,10]
minIndex=0
k=0
while k<len(sortList)-1:
	minIndex=k
	for i in range(k+1,len(sortList)):
		if sortList[minIndex]>sortList[i]:
			minIndex=i
	#if minIndex!=k:
		#print (minIndex)
		#temp=sortList[minIndex]
		#sortList[minIndex]=sortList[k]
		#sortList[k]=temp
	k=k+1
	#print(minIndex)
	#print(sortList);
#for 循环
for k in range(len(sortList)-1):
	minIndex=k
	for i in range(k+1,len(sortList)):
		if sortList[minIndex]>sortList[i]:
			minIndex=i
			
	if minIndex!=k:
		temp=sortList[k]
		sortList[k]=sortList[minIndex]
		sortList[minIndex]=temp
	print(sortList)
