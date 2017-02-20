[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

```java
// Time: O(n)
// Space: O(size of char set)
// Runtime: 5ms
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        final int SIZE = 256;
        int[] lastOccurence = new int[SIZE];
        for (int i = 0; i < SIZE; i++) { lastOccurence[i] = -1; }

        int leftBoundary = -1;
        int maxLen = 0;
        int idx = 0;
        for (char c : s.toCharArray()) {
            int lastIdx = lastOccurence[c];
            if (lastIdx > leftBoundary) {
                leftBoundary = lastIdx;
            }
            int len = idx - leftBoundary;
            if (len > maxLen) {
                maxLen = len;
            }
            lastOccurence[c] = idx;
            idx++;
        }
        return maxLen;
    }
}
```

Corner cases:
- first occurence: so the `lastOccurence` need have a default value `-1`
- repetition inside 2 duplicated char ('abba'): the `leftBoundary` is always the left boundary of last repetition.
