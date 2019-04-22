# alist = [54,26,93,17,77,31,44,55,20]
alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]
def foo(a):
    if len(a) <2:
        return a
    i, j = 0, len(a)-1
    x = a[0]
    left = True
    while i < j:
        if left:
            if a[j] >= x:
                j = j -1
            else:
                a[i] = a[j]
                left = False
                i = i+1
        else:
            if a[i] > x:
                a[j] = a[i]
                left = True
                j = j -1
            else:
                i = i + 1
    a[i] = x
    return foo(a[:i]) + [x] + foo(a[i+1:])

june = foo(alist)
print(june)
