//requirements: ArrayList, List interfaces
import java.util.ArrayList;
import java.util.List;

class KthLargest {
    int num_k;
    List <Integer> array = new ArrayList<>();

    public KthLargest(int k, int[] nums) {
        Arrays.sort(nums);
        try{

            for (int i = nums.length-1; i >= nums.length-k;i--){
                this.array.add(nums[i]);
            }
        }
        catch(Exception e){
        }
        this.num_k = k;  
    }
    
    public int add(int val) {
        this.array.add(val); 
        this.array.sort((a,b)->{return -1*a.compareTo(b);});
        return this.array.get(num_k-1);
    }
}
