import java.util.HashMap;

class Solution {
    public void binaryConversion(HashMap<Integer,Integer> memo,int number){
        int value = 1;
        int temp = number;
        while(temp != 1){
            if(temp%2 == 1) value += 1;
            temp = temp/2;
        }
        memo.put(number,value); 
    }
    public int[] sortByBits(int[] arr) {
        HashMap<Integer,Integer> memo = new HashMap();
        memo.put(0,0);
        int length = arr.length;
        for(int i = 1; i < length; i++){
            int min = arr[i];
            int j = i-1;
            while(j>=0 && arr[j]>min){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = min;
        }
        for(int i = 0;i < length;i++){
            if(arr[i] != 0) binaryConversion(memo,arr[i]);
        }
        for(int i = 1; i < length;i++){
            int min = arr[i];
            int min_bit_count = memo.get(min);
            int j = i-1;
            while(j >= 0 && memo.get(arr[j]) > min_bit_count){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = min;
        }
        return arr;
    }
}