[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## idea: Fast and slow pointer. 

基本思路：快指针一直向前走，当发现有重复的时候，移动慢指针。在这个过程中，需要用一个map来记录 frequency or index。

使用map时，key 是 input sting 中的 char，value有两种不同的用法：一种是存放每个char出现的频次，一种是存放每个char最后出现的位置。

## 第一种方法存频次:

We move fast pointer when:

​	the element at fast pointer does not appear at the previous set.

We move slow pointer when:

​	the element at fast pointer appears at the previous set. Then we delete the element at the slow pointer from the set, check if the element at fast pointer still in the set. Keep doing so until the element at fast pointer does not appear, then add this element to the set, move fast.

Use a global max to memorize the longest substring. If it needs to return the string itself instead of the length, use a start and end pointer to return the substring.

这种方式的优点是可以灵活地控制每个字符出现的次数（例如本题要求distinct，每个字符出现的次数就是1，如果要求2次3次都可以改）

我原以为这种方法有一个优点是可以打印出相应的子串（本题中没有要求，但是只要依次打印出value = 1 的 key，就是substring with distinct chars），但后来一想map中的次序是 not garantee的，所以这个优点是不存在的，打印子串还是得靠 fast - slow的部分。

缺点是当需要移动 slow 指针时，必须要一个一个删除 map 中的 key （这里并不是真的删掉key，而是把其对应的 value 减到 0），直到删到重复的那个 key 为止。参考代码如下：

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
            # without duplication
            if unique_char.setdefault(s[fast], 0) < 1:
                unique_char[s[fast]] += 1
                global_max = max(global_max, fast - slow + 1)
            # with duplication
            else:
                unique_char[s[fast]] += 1
                while unique_char[s[fast]] > 1:
                    unique_char[s[slow]] -= 1
                    slow += 1
        
        return global_max  
```



此外，由于本题是要求distinct char，用一个set来存也是完全可以的，这里的set就代表着当前循环下的 substring with distinct character. set 比 map更简洁，但只适用于只需判断有和没有的情况，参考代码如下：

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
            # without dup
            if s[fast] not in unique_char:
                unique_char.add(s[fast])
                global_max = max(global_max, fast - slow + 1)
            # with dup
            else:
                while s[fast] in unique_char:
                    unique_char.remove(s[slow])
                    slow += 1
                unique_char.add(s[fast])
        
        return global_max 
```



## 第二种方法是用 map 记录每个 char 最后出现的位置

这种方式更好一些.此时这个map代表的并不是distinct char，而是之前见过的 char。这里要想清楚，当存的value不一样时，整个map 的意义都变了。（另外，这时 distinct char 是 fast - slow 的区域）这种方法的优点是，当出现重复的时候，不需要一个一个地去删 key，只需要更新一下该字符最后出现的位置就可以了。这种思路下，移动慢指针的条件是：map 中有这个 char，而且这个 char 最后出现的位置比slow还大。参考代码如下：

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """      
        slow, global_max = 0, 0
        visited = {}
        
        for fast in range(0, len(s)):
            if s[fast] in visited:
                slow = max(slow, visited[s[fast]] + 1)
            visited[s[fast]] = fast
            global_max = max(global_max, fast - slow + 1)
        
        return global_max
```



以下是个人未整理的其他笔记：

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
