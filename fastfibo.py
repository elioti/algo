def fast(n):
    if n == 1:
        return 0, 1
    m = n//2
    hprv, hcur = fast(m)
    prev = hprv*hprv + hcur* hcur
    curr = hcur*(2*hprv + hcur)
    next  = prev + curr
    if n%2 == 0:
        return prev, curr
    else:
        return curr, next

a = fast(10)
print(a)