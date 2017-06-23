[51. N-Queens](https://leetcode.com/problems/n-queens/)

经典的NP-hard题，指数级的复杂度，需要用递归思想来解决子问题，DFS经典题目。

这类比较复杂的递归问题，首先要画好递归树，要点在于递归树有几层，每层有几个分支。对于n * n大小的棋盘，要循环递归处理子问题，每一层递归来处理一行，所以一共有n层树，每一行都有n种可能的位置，所以每一层都有n个分支。这个递归树就是有n层，每层有n个叉的树。但是并不是每条路径都是合法的，每递归一次，要检查当前路径是否合法，所以真实复杂度要比 O(n^n) 小。

用一个一维数组来存皇后的位置，数组的index表示行数，值表示列数。比如 `queens = [1,3,5,7]` 就表示当前情况下，在第一行的第2个位置，第二行的第四个位置，第三行的第六个位置和第四行的第八个位置分别有皇后。从0开始，一行一行地往里添加新的，每添加新的一行，皇后都有可能有n个位置，用一个循环来考虑这n个位置，每添加一个新的位置时，判断当面情况是否合法，如果合法就递归到下一行，直到全部合法。

全部合法时，当前数组queens就代表了一种合法的情况，长度为n，代表有n个皇后分别在n行里处在合法的位置上。把这个数组加到最后结果中去，然后返回空，代表了这条路已经走完了。当不合法时，这个DFS helper function在循环里就直接走死了，什么都不用返回。

判断合不合法时，条件是行，列，斜不能有其他皇后。由于我们用一维数组，保证了每行只有一个皇后，所以只需要判断列和斜。列的话比较简单，就是当前的列数没有在之前出现过，也就是说每列只能有一个皇后。关键在于斜，一个普通的方法是检查当前皇后位置和之前所有行里的皇后位置的行列之差的绝对值不相等就可以，这个非常好理解，但是需要循环一遍之前所有行里的皇后，时间复杂度为O(n)。还有一种巧妙的办法，用一个数组存之前所有行里皇后的行列差与和，判断条件是新皇后的行列差与和不与之前数组里的值相等，这个方法时间是O(n)，空间为O(n)，而且不太好理解。画个图就能看得比较清楚了，`/` 这个方向上，行列坐标是一加一减，如果往上走，行减1列加1，如果往下走，行加1列减1，所以行列坐标总和是一定的。 `\` 这个方向上，行列坐标是同加同减。往上走，行列分别减1，往下走，行列分别加1，所以行列坐标之差是一定的。



代码参考 discussion里的就非常简洁了  

```python
def solveNQueens(self, n):
    def DFS(queens, xy_45, xy_135):
        # when reach the end and get a legal result
        row = len(queens)
        if row == n:
            result.append(queens)
            return None
        # recurse to the next row
        for column in range(n):
            # check: same column? same 45 degree line? same 135 degree line?
            if column not in queens and row + column not in xy_45 and row - column not in xy_135:
                DFS(queens + [column], xy_45 + [row + column], xy_135 + [row - column])

                result = []
                DFS([], [], [])
                return [["." * i + "Q" + "." * (n - i - 1) for i in solution] for solution in result]
```

参考 [leetcode discussion:](https://discuss.leetcode.com/topic/20217/fast-short-and-easy-to-understand-python-solution-11-lines-76ms)

关键点是O(1) 的检查方法

In this problem, whenever a location `(x, y`) is occupied, any other locations `(p, q )` where `p + q == x + y` or `p - q == x - y` would be invalid. We can use this information to keep track of the indicators (`xy_dif` and `xy_sum` ) of the invalid positions and then call DFS recursively with valid positions only. 

```python
def solveNQueens(self, n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
```



参考 [code ganker](http://blog.csdn.net/linhuanmars/article/details/20667175)

N皇后问题是非常经典的问题了，记得当时搞竞赛第一道递归的题目就是N皇后。因为这个问题是典型的[NP问题](http://en.wikipedia.org/wiki/NP_(complexity))，所以在时间复杂度上就不用纠结了，肯定是指数量级的。下面我们来介绍这个题的基本思路。
主要思想就是一句话：用一个循环递归处理子问题。这个问题中，在每一层递归函数中，我们用一个循环把一个皇后填入对应行的某一列中，如果当前棋盘合法，我们就递归处理先一行，找到正确的棋盘我们就存储到结果集里面。
这种题目都是使用这个套路，就是用一个循环去枚举当前所有情况，然后把元素加入，递归，再把元素移除，这道题目中不用移除的原因是我们用一个一维数组去存皇后在对应行的哪一列，因为一行只能有一个皇后，如果二维数组，那么就需要把那一行那一列在递归结束后设回没有皇后，所以道理是一样的。
这道题最后一个细节就是怎么实现检查当前棋盘合法性的问题，因为除了刚加进来的那个皇后，前面都是合法的，我们只需要检查当前行和前面行是否冲突即可。检查是否同列很简单，检查对角线就是行的差和列的差的绝对值不要相等就可以。代码如下：

```java
public ArrayList<String[]> solveNQueens(int n) {  
    ArrayList<String[]> res = new ArrayList<String[]>();  
    helper(n,0,new int[n], res);  
    return res;  
}  
private void helper(int n, int row, int[] columnForRow, ArrayList<String[]> res)  
{  
    if(row == n)  
    {  
        String[] item = new String[n];  
        for(int i=0;i<n;i++)  
        {  
            StringBuilder strRow = new StringBuilder();  
            for(int j=0;j<n;j++)  
            {  
                if(columnForRow[i]==j)  
                    strRow.append('Q');  
                else  
                    strRow.append('.');  
            }  
            item[i] = strRow.toString();  
        }  
        res.add(item);  
        return;  
    }  
    for(int i=0;i<n;i++)  
    {  
        columnForRow[row] = i;  
        if(check(row,columnForRow))  
        {  
            helper(n,row+1,columnForRow,res);  
        }  
    }  
}  
private boolean check(int row, int[] columnForRow)  
{  
    for(int i=0;i<row;i++)  
    {  
        if(columnForRow[row]==columnForRow[i] || Math.abs(columnForRow[row]-columnForRow[i])==row-i)  
            return false;  
    }  
    return true;  
}  
```

基本上大部分NP问题的求解都是用这个方式，比如[Sudoku Solver](http://blog.csdn.net/linhuanmars/article/details/20748761)，[Combination Sum](http://blog.csdn.net/linhuanmars/article/details/20828631)，[Combinations](http://blog.csdn.net/linhuanmars/article/details/21260217)，[Permutations，](http://blog.csdn.net/linhuanmars/article/details/21569031)[Word Break II](http://blog.csdn.net/linhuanmars/article/details/22452163)，[Palindrome Partitioning](http://blog.csdn.net/linhuanmars/article/details/22777711)等