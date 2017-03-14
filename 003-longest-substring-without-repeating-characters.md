[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

idea: Fast and slow pointer. 

We move fast pointer when:

​	the element at fast pointer does not appear at the previous set.

We move slow pointer when:

​	the element at fast pointer appears at the previous set. Then we delete the element at the slow pointer from the set, check if the element at fast pointer still in the set. Keep doing so until the element at fast pointer does not appear, then add this element to the set, move fast.

Use a global max to memorize the longest substring. If it needs to return the string itself instead of the length, use a start and end pointer to return the substring.

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slow, global_max = 0, 0
        unique_char = set()
        
        for fast in range(0, len(s)):
            if s[fast] not in unique_char:
                unique_char.add(s[fast])
                global_max = max(global_max, fast - slow + 1)
            else:
                while s[fast] in unique_char:
                    unique_char.remove(s[slow])
                    slow += 1
                unique_char.add(s[fast])
        
        return global_max 
```



using dict：

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slow, global_max = 0, 0
        unique_char = {}
        
        for fast in range(0, len(s)):
            '''
            if unique_char.get(s[fast], 0) < 1:
                unique_char[s[fast]] = 1
            '''
            if unique_char.setdefault(s[fast], 0) < 1:
                unique_char[s[fast]] += 1
                global_max = max(global_max, fast - slow + 1)
            else:
                unique_char[s[fast]] += 1
                while unique_char[s[fast]] > 1:
                    unique_char[s[slow]] -= 1
                    slow += 1
        
        return global_max  
```

这里不像java一样，map中没有的key也可以直接用。python里如果去调一个没有的key, 会抛出keyError.

另一方面，`if s[fast] in unique_char` 不能用。因为即使快指针指向的元素被删没了，它在dict里的值是0， 上面的表达式也会返回真！

这里出现了get vs setdefault的差异了！！！

评论：

这个题的基本思路是这样：快慢指针。快指针每轮都往前走一次，慢指针只有在出现重复的时候才往前走。用快指针做循环：

- 如果快指针指向的元素不在集合里，把它加上，然后计算一次全局最大值。（注意这里是 `fast - slow + 1`）
- 如果快指针指向的元素在集合里，就要慢指针开始，先删除其所指向的元素，然后增加慢指针。反复做，直到删到快指针的元素不在集合中为止。（就是一直删到和快指针元素重复的元素）。不要忘记再把快指针加回去，要不然就出KeyError






不知道多久之前的答案：

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
