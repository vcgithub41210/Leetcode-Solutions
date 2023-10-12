/**
 * *********************************************************************
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * *********************************************************************
 *
 * int get(MountainArray *, int index);
 * int length(MountainArray *);
 */
int Binary_Search(MountainArray *array,int start, int end, int target,int direction){
	while(start <= end)
	{
		int middle = (start+end)/2;
		if(get(array,middle) == target) return middle;
		else if(direction == -1)
		{
			if(get(array,middle) > target) end = middle-1;
			else start = middle+1;
		}
		else{
			if(get(array,middle) < target) end = middle-1;
			else start = middle+1;
		}
	}
	return -1;
}

int findInMountainArray(int target, MountainArray* mountainArr) {
	int start,end,middle;
  int size  = length(mountainArr);
	start = 0;
	end = size-1;
	while(start <= end)
	{
		middle = (start+end)/2;
		if(get(mountainArr,middle) > get(mountainArr,middle+1))end = middle-1;
		else start = middle+1;
	}
		int min_index = Binary_Search(mountainArr,0,middle,target,-1);
		if(min_index == -1) min_index = Binary_Search(mountainArr,middle,size-1,target,1);
		return min_index;
}