class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> my_dict = new HashMap<>();

        for(int i=0; i < nums.length; i++){
            int difference = target - nums[i];
            if (my_dict.containsKey(difference)){
                return new int[] {my_dict.get(difference), i};
            }
            my_dict.put(nums[i], i);
        }
        return new int[0]; 
    }
}

// my_dict = {}
//         for i in range(len(nums)):
//             difference = target - nums[i]
//             if difference in my_dict:
//                 return [my_dict[difference], i]
//             my_dict[nums[i]] = i