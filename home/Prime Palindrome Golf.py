def g(n):
    while 1:
        n+=1;if `n`==`n`[::-1] and not [x for x in range(2,n) if n%x==0]:return n

