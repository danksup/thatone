import random
import time
import os


doller = []

def add(k):
    if k not in doller:
        doller.append(k)
        print(k + ' is added')
    else:
        if k in doller:
            print(f'unsuccessful. {k} is already in the array')

def lookup(k):
    try:
        print(f'{k} is in {doller.index(k) + 1} of the array') 
    except:
        print(f'{k} is not in the array')

def search(k):
    try:
        if not doller:
            print('nothing to search')
        elif int(k) > len(doller):
            print(f'try 1-{len(doller)}')
        else:
            l = int(k)-1
            print(f'index {k} is occupied by {doller[l]}')
    except:
        print(f'either input is invalid(input only int) or another problem occured')

def all():
    # print(', '.join(doller))
    if not doller:
        print('array is empty')
    else:
        for i, j in enumerate(doller):
            print(f'{i + 1}.',j)
    
def remove(n):
    try:
        doller.pop(doller.index(n))
        print(f'{k} is sucessfully removed from the array')
    except:
        print(f'either {k} is not in the array or another problem occured')

def remove_all():
    if not doller:
        print('nothing to remove')
    else:
        length = len(doller)
        print('removing...')
        while doller:
            doller.pop(0)
        print(f'succesfully removed {length} from the array')

def add_temporary_data(n,k):
    vocal = 'aeiou'
    other = 'bcdfghjklmnpqrstvwxyz'
    for _ in range(n):
        char = ''
        for i in range(k):
            if i % 2 == 0:
                char += random.choice(vocal)
            else:
                char += random.choice(other)
        add(char)

def pop_(n):
    try:
        if not doller:
            print('nothing to pop')
        elif int(n) > len(doller):
            print(f'try 1-{len(doller)}')
        else:
            l = int(n) - 1
            print(f'index {int(n)} ({doller[l]}) is successfully removed')
            doller.pop(l)
    except ValueError:
        print('only input int')
        
def modify(j, newchar):
    try:
        int_j = int(j)
        if not doller:
            print('nothing to modify')
        if int_j > len(doller):
            print(f'try 1-{len(doller)}')
        if newchar in doller:
            print(f'unsuccessful modification. {newchar} is already in the array')
        else:   
            l = int_j -1
            print(f'succesfully modified {doller[l]} into {newchar}')
            doller[l] = newchar
    except:
        if not doller:
            print('nothing to modify')
        elif j not in doller:
            print(f'{j} is not in the array')
        elif newchar in doller:
            print(f'unsuccessful modification. {newchar} is already in the array')
        else:   
            try:
                indexed = doller.index(j)
                print(f'succesfully modified {doller[indexed]} into {newchar}')
                doller[indexed] = newchar
            except:
                print('an error occured')

def timer():
    end_time=time.time()
    seconds = end_time - start_time
    print(f'took {int(seconds)}s to execute')
    
        
while True:
    menu = input('menu: ').lower()
    arg = menu.split()

    if arg[0] == 'add':
        k = ' '.join(arg[1:]).strip()
        add(k)
    elif arg[0] == 'lookup':
        k = ' '.join(arg[1:]).strip()
        lookup(k)
    elif arg[0] == 'search':
        k = ' '.join(arg[1:]).strip()
        search(k)
    elif menu == 'all':
        all()
    elif menu.startswith('addtemp'):
        start_time = time.time()
        len_arr_old = len(doller)
        try:
            n = arg[1]
            k = arg[2]
            add_temporary_data(int(n), int(k))
            len_arr_new = len(doller)
            delta_arr = abs(len_arr_old-len_arr_new)
            unsuccessful = abs(int(n) - delta_arr)
            added = int(n) - unsuccessful
            if added == int(n):
                print('all data are unique')
            else:
                print(f'from {n}, only {added} data were sucessfully added')
            timer()
        except:
         print("Invalid input. Please provide a number.")
    elif arg[0] == 'remove':
        try:
            if arg[1] == "all":
                os.system('clear')
                remove_all()
            else:
                k = ' '.join(arg[1:]).strip()
                remove(k)
        except:
            print('error')
    elif arg[0] == 'pop':
        k = ' '.join(arg[1:]).strip()
        pop_(k)
    elif arg[0] == 'modify':
         index = ' '.join(arg[1:2]).strip()
         modifier = ' '.join(arg[2:]).strip()
         modify(index, modifier)
    elif menu == 'keluar':
        break;
    else:
        #if makes sense:
        print('invalid menu input. do you mean (to be implemented)')
        #else:
        #print(invalid menu input)
        



