def main(re):
    return re == re[::-1]
re = input('input a word to cheek if it is fliped will it be the same word(like MoM): ')
ans = main(re)

if ans:
    print('yes',re,'can')
else:
    print('no',re,'itcant')
