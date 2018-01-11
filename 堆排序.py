#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#交换
def swap(array,i,j):
	temp=array[i];
	array[i]=array[j];
	array[j]=temp;
#调整堆，输入数组，与长度
def heapify(array,pNode,sortLength):
	print(sortLength);
	length=sortLength;
	while True:
		maxNode=pNode;
		lNode=2*pNode+1;
		rNode=2*(pNode+1);
		if lNode<length and array[lNode]>array[maxNode]:
			maxNode=lNode
		if rNode<length and array[rNode]>array[maxNode]:
			maxNode=rNode;
		if maxNode!=pNode:
			swap(array,maxNode,pNode);
			pNode=maxNode;
		else:
			break;
#构建最大堆
def buildMaxHeap(array,length):
	parent=length//2-1;
	for i in range(parent,-1,-1):
		heapify(array,i,len(array)-1);
#堆排序
def sortHeap(array):
	buildMaxHeap(array,len(array));
	length=len(array);
	for k in range(length-1,-1,-1):
		swap(array,0,k);
		heapify(array,0,k);
array=[4,3,6,7,1,8,0,34,2,34];
sortHeap(array);
print(array);
