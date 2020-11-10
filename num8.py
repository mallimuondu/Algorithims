def main():
    ar = []
    i1 = input('input a numer to find the first element: ')
    ar.append(i1)
    l = len(i1)
    if l < 3:
        print('insert more than 3numbers.pls try again')
        main()
    elif l >= 1:
        p = i1[2]
        print('the third number = ',p)
main()