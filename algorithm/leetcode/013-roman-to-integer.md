[13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

```javascript
var romanToInt = function(s) {
//学会怎么处理减的情况，IV = 4, VI = 6
  var hash = {};
  hash["I"] = 1;
  hash["X"] = 10;
  hash["C"] = 100;
  hash["M"] = 1000;
  hash["V"] = 5;
  hash["L"] = 50;
  hash["D"] = 500;
  
  var sum = 0;
  
  for (var i = 0; i < s.length; i++) {
      var curr = hash[s[i]];
    
    //处理好corner case，这是我永远的伤痛！
      var next = i === s.length - 1 ? 0 : hash[s[i+1]];
      
      if (next > curr) {
          sum += next - curr;
          //这里不要忘记加指针，因为已经处理过下一位了
          i++;
      } else {
          sum += curr;
      }
  }
  return sum;
};
```



The trick is that the last letter is always added. Except the last one, if one letter is less than its latter one, this letter is subtracted.

```python
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
```



评论：

伤痛就是不想是回忆，但又不得不面对