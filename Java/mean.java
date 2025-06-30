
public class mean {
    public static int findAverage(int[] nums) {
        int sum=0;
        for(int i=0;i<nums.length;i++){
            if (i>nums.length){
                break;
            }
            sum+=nums[i];

        }
        return sum/nums.length;
    }
    public static void main(String[] args) {
        int[] nums={71,22,83,40,15};
        System.out.println(findAverage(nums));
        }
    }
