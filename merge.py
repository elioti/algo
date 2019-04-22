alist = [54,26,93,17,77,31,44,55,20]

ans = []
def part(a):
    if len(a) >= 2:
        num = len(a)//2
        left = part(a[:num])
        right = part(a[num:])
        return merge(left, right)
    else:
        return a


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] > right[0]:
        return [right[0]] + merge(left, right[1:])
    else:
        return [left[0]] + merge(right, left[1:])

june = part(alist)
print(june)