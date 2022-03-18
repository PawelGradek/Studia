def tone(x, y):
    fbz = []
    for i in range(x, y):
        if i % 3 == 0 and i % 5 == 0:
            i = 'foobar'
            fbz.append(i)
        elif i % 3 == 0:
            i = 'foo'
            fbz.append(i)
        elif i % 5 == 0:
            i = 'bar'
            fbz.append(i)
        else:
            fbz.append(i)

    return fbz

print(tone(1, 16))