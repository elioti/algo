def subsetsum(x, i, t, ans):
    if t == 0:
        print(ans)
        return True
    if t < 0 or i == 0:
        return False
    have = subsetsum(x, i-1, t-x[i-1], ans+[x[i-1]])  # 判断除去的值是否在子列里 返回true 表明x[i-1]在子列 flase表明递归失败
    out = subsetsum(x, i-1, t, ans)  # 判断递归是否结束 返回false表示结束

    return have or out


list1 = [8, 6,7, 5,3, 10,9]

print(subsetsum(list1, len(list1), 15, []))
