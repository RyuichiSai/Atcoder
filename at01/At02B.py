m = int(input())

km = m/1000
vv = 0

if km < 0.1:
    vv = 0
elif km <= 5:
    vv = km*10
elif km <= 30:
    vv = km+50
elif km <= 70:
    vv = (km-30)/5+80
elif km > 70:
    vv = 89

print('{:0>2}'.format(int(vv)))
