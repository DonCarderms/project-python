n = int(input('Número?'))

if n > 5:
    print(n, ' é maior do que 5')
    if n > 100:
        print(n, 'é grande')
        if n > 1000:
            print(n, 'é muito grande')
elif n > 2:
    print(n, 'é maior do que 2')
else:
    print(n)
