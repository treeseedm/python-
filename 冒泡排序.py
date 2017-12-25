name = [1,4,5,7,2,6,9]
for num in range(1,len(name)):
	hasOrder = 1
	for index in range(len(name)-num):
    		if name[index]>name[index+1]:
        		temp = name[index]
        		name[index] = name[index+1]
            	name[index+1]=temp
            	hasorder=0
