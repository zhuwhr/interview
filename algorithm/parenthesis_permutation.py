def parenthesis_permutation(n):
    res = []
    def dfs(n, left=0, right=0, temp=[]):
        if left == n and right == n:
            res.append(''.join(temp))
            return
        if left < n:
            temp.append('(')
            dfs(n, left + 1, right, temp)
            temp.pop()
        if right < left:
            temp.append(')')
            dfs(n, left, right + 1, temp)
            temp.pop()
    dfs(n)
    return res

if __name__ == '__main__':
    print(parenthesis_permutation(4))
