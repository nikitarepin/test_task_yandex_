a = str(input())
b = str(input())
ot = [''] * len(a)

def f(a,n):
    k = 0
    for i in range(len(a)):
        if n == a[i]:
            k = 1
    if k == 1:
        return True
    else:
        return False

def res(a,b,ot,):
    for j in range(len(a)):
        if a[j] == b[j]:
            a = a.replace(a[j],'1',1)
            ot[j] = 'correct'

    for j in range(len(a)):
        if (a[j] != b[j] and (f(a,b[j]) == True) and ot[j] != 'correct'):
            ot[j] = 'present'
            a = a.replace(b[j],'1',1)

    for j in range(len(a)):
        if (a[j] != b[j] and (f(a,b[j]) == False) and (ot[j] != 'correct' and ot[j] != 'present')):
            ot[j] = 'absent'

    for j in range(len(ot)):
        print(ot[j])

res(a,b,ot)
