def main():
    ar = []
    i1 = input('input a numer to find the first element: ')
    ar.append(i1)
    l = len(i1)
    if l < 1:
        print('insert more than 1number.pls try again')
        main()
    elif l >= 1:
        p = i1[0]
        print('the first number = ',p)
main()