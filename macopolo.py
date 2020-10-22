#a = []
for i in range(3,10000):
#    a.append(i)
#    print(i)
    if i%3==0 and i%5==0:
        print('makopolo')
    elif i%3==0:
        print('mako')
    elif i%5==0:
        print('polo')
    else:
        print(i)