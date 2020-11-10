def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False


fruit = ['banana', 'grape', 'apple', 'plam']
print(fruit)
frut = input('input to see if it exists: ')

if search(fruit, frut):
    print("fruit is found")
else:
    print("fruiit does not found")