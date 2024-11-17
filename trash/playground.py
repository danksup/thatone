doller = ['apple', 'apricot', 'banana', 'bayam']
def startwith(x):
    met_x = []
    if not doller:
        print('nothing to show')
    else:
        for i in doller:
            if i.startswith(x):
                met_x.append(i)
        if not met_x:
            return print(f'no element starts with {x} ')
        for number, item in enumerate(met_x):
            print(f'{number + 1}.', item)

print(startwith('b'))