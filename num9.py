def main():
    ar = []
    i1 = input('input an array: ')
    ar.append(i1)
    l = len(i1)
    if l < 3:
        print('insert more than 3numbers.pls try again')
        main()
    elif l >= 1:
        p = i1[0]
        f = i1[3]
        print('the first number = ',p)
        print('the last number = ',f)
        sumi = p + f
        i1 = int(sumi)
        print('the sum =',sumi)
main()