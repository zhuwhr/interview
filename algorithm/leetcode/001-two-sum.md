[1. Two Sum](https://leetcode.com/problems/two-sum/)

## naive solution
```c++
// Time: O(n^2)
// Space: O(1)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        const auto size = nums.size();
        for (int i = 0; i < size - 1; i++) {
            for (int j = i + 1; j < size; j++) {
                if (nums[i] + nums[j] == target) {
                    return vector<int> {i + 1, j + 1};
                }
            }
        }
    }
};
```

## O(n) solution
To decrease the time complexity, could store previous info for further query. Here we could use element's `value` as `index`.
But using array as collection is impractical, just use a Hashmap.

```java
import java.util.HashMap;

// Time: O(n)
// Space: O(n)
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indices = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int value = nums[i];
            int complement = target - value;
            if (indices.containsKey(complement)) {
                return new int[] {indices.get(complement), i+1};
            } else {
                indices.put(value, i+1);
            }
        }
        return null;
    }
}
```

P.S. Using array in Java could beat 99.9% at runtime. But to make it theorically correct u have at least allocate `INT_SIZE`
for the array. And it's not a good practice in engineering.
