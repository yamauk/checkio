def golf(n):
    while 1:
        n+=1
        if str(n)==str(n)[::-1] and not [x for x in range(2,n) if n%x==0]:
            return n

