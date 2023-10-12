#include <stdio.h>

int Binary_Search(int *array,int start, int end, int target,int direction)
{
	while(start <= end)
	{
		int middle = (start+end)/2;
		if(array[middle] == target) return middle;
		else if(direction == -1)
		{
			if(array[middle] > target) end = middle-1;
			else start = middle+1;
		}
		else{
			if(array[middle] < target) end = middle-1;
			else start = middle+1;
		}
	}
	return -1;
}
int main()
{
	int size,start,end,middle,target;
	printf("Enter the size of the mountain array: ");
	scanf("%d",&size);
	int array[size];
	printf("Enter the elements of the mountain array:\n");
	for(int i = 0; i < size; i++)
	{
		scanf("%d",&array[i]);
	}
	printf("Enter the element to be searched: ");
	scanf("%d",&target);
	start = 0;
	end = size-1;
	while(start <= end)
	{
		middle = (start+end)/2;
		if(array[middle] > array[middle+1]) end = middle-1;
		else start = middle+1;
	}
	printf("%d,{%d}",middle,array[middle]);
	
		int min_index = Binary_Search(array,0,middle,target,-1);
		if(min_index == -1) min_index = Binary_Search(array,middle,size-1,target,0);
		printf("The minimum index of %d is ==> %d\n",target,min_index);
	
}