import random
import time
import os
import cProfile
from importlib import reload

#my own library
from basic_word_match_algorithm import *
from tobeornottobe import *


doller = []

valid_commands = ['add', 'lookup', 'search', 'all', 'sort', 'remove', 'pop', 'modify', 'addtemp', 'keluar', 'indicate', 'menu', 'reload','exit']

def suggest_word(word, word_dict):
    best_score = 0
    best_match = None

    for i in word_dict:
        score = simple_word_match_algorithm(word, i)
        if score > best_score:
            best_score = score
            best_match = i

    if best_score >= 0.2:
        return f'invalid menu input. did you mean {best_match}'
    else:
        return 'invalid menu input'

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

def new_all(min, max):
    minint = int(min)
    maxint = int(max)
    length = len(doller)

    if not doller:
        print('nothing to show')
    elif minint < 0 or maxint > length:
        print("range is out of bounds.")
        return
    elif maxint - minint > 500:
        print("can only show up to 500 data.")
        return
    elif minint > maxint:
        print("min val cant be more than max val")
        return
    else:
        for i in range(minint, maxint):
            print(f"{i + 1}. {doller[i]}")

def startwith(x):
    met_x = []
    if not doller:
        print('nothing to show')
    else:
        for i in doller:
            if i.startswith(x):
                met_x.append(i)
        if not met_x:
            print(f'no element starts with {x} ')
        for number, item in enumerate(met_x):
            print(f'{number + 1}.', item)

def orderize():
    if not doller or len(doller) < 1:
        print('nothing to sort')
    else:
        confirmation = input('once executed, it will stay like that. confirm? ')
        if confirmation == 'yes':
            print('sorting....')
            doller.sort()
            print('successfully sorted the array')

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
        os.system('clear')
        print('removing...')
        while doller:
            doller.pop(0)
        os.system('clear')
        print(f'succesfully removed {length} from the array')

def add_temporary_data(n, k):
    vocal = 'aeiou'
    other = 'bcdfghjklmnpqrstvwxyz'
    vocalupper = vocal.upper()
    otherupper = other.upper()

    allcharupper = vocalupper + otherupper

    for _ in range(n):
        char = ''
        for i in range(k):
            if i == 0:
                determiner = random.choice(allcharupper)
                char += determiner
            else:
                if char[0] in vocalupper:
                    if i % 2 == 0:
                        char += random.choice(vocal)
                    else:
                        char += random.choice(other)
                else:
                    if i % 2 == 0:
                        char += random.choice(other)
                    else:
                        char += random.choice(vocal)
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
    info = 'type \'menu\' to list all menus\n'
    menu = input(f'{info}menu: ').lower()
    arg = menu.split()
    try:
        if arg[0] == 'add':
            k = ' '.join(arg[1:]).strip()
            add(k)
        elif arg[0] == 'lookup':
            k = ' '.join(arg[1:]).strip().capitalize()
            lookup(k)
        elif arg[0] == 'search':
            k = ' '.join(arg[1:]).strip()
            search(k)

        elif arg[0] == 'all':
            try:
                if arg[1] == 'startswith':
                    startwith(arg[2])
                else:
                    minint = int(arg[1])
                    maxint = int(arg[2])
                    new_all(minint, maxint)
            except IndexError:
                all()
            except ValueError:
                print("Please enter valid numbers for the range.")

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
                    print(f'from {n}, only {added}({(added/int(n)*100)}%) data were sucessfully added')
                timer()
            except:
                print("Invalid input. Please provide a number.")
        elif arg[0] == 'sort':
            orderize()
        elif arg[0] == 'remove':
            try:
                if arg[1] == "all":
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
        elif menu == 'exit':
            break;
        elif menu =='cprofile':
            cProfile.run('add_temporary_data(1000000, 5)')
        
        elif arg[0] == 'indicate':
            k = arg[1:]
            print(k)
            #print(indicate(k))
        elif menu == 'menu':
            print(', '.join(valid_commands))
        elif menu == 'reload':
           print('to be added')
        else:
            suggested_command = suggest_word(arg[0], valid_commands)
            print(suggested_command)
    except:
        print('an error occuted')

        




