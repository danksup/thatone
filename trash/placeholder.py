from words import *

t1p = tier_1_pos()
t2p = tier_2_pos()
t3p = tier_3_pos()

t1n = tier_1_neg()
t2n = tier_2_neg()
t3n = tier_3_neg()

all_pos = t1p + t2p + t3p
all_neg = t1n + t2n + t3n

all_words = all_pos + all_neg

intensfier = ['fucking', 'bloody', 'hella', 'insanely', 'really', 'exteremely', 'very', 'so']
article = ['a', 'an', 'the']

def IsEmpty(L):
    return L == []

def divider():
    print('-'*50)

def tone(sentence,ignore_intensifier=bool):
    score = 0
    pos_arr = []
    neg_arr = []

    if isinstance(sentence, list):    
        low = sentence
    else:
        low = sentence.split(' ')

    print(low)

    def IsIntensified(n):
        k = (low.index(n) - 1)
        if k >= 0:
            return low[k] in intensfier

    def intensity(i,score):
        n = 0

        if IsIntensified(i) and not ignore_intensifier:
                print(f'{i} is intensified')
                n = score
        else:
            if ignore_intensifier:
                print('intensifier is ignored')
            else:
                print(f'{i} is not intensified')
                n = 0
        return n
    
    def a_noun(n):
        k = (low.index(n) - 1)
        if k >= 0:
            
            return low[k] in article

    for i in low:
        if i in t1p:
            intense = intensity(i, 1)

            pos_arr.append(i)

            if not a_noun(i):
                score += 1 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0

        elif i in t2p:
            intense = intensity(i, 2)

            pos_arr.append(i)
            
            if not a_noun(i):
                score += 2 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0

        elif i in t3p:
            intense = intensity(i, 3)

            pos_arr.append(i)

            if not a_noun(i):
                score += 3 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0

        elif i in t1n:
            intense = intensity(i, 1)

            neg_arr.append(i)

            if not a_noun(i):
                score -= 1 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0

        elif i in t2n:
            intense = intensity(i, 2)

            neg_arr.append(i)
            
            if not a_noun(i):
                score -= 2 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0

        elif i in t3n:
            intense = intensity(i, 3)

            neg_arr.append(i)

            if not a_noun(i):
                score -= 3 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0
    
    if  IsEmpty(pos_arr):
        print('no positive word')
    else:
        print(pos_arr)
    
    if  IsEmpty(neg_arr):
        print('no negative word')
    else:
        print(neg_arr)

    return score

def indicate(sentence, ignore_intensifier=bool):
    score = tone(sentence, ignore_intensifier)

    if score > 0:
        return 'positive', score
    elif score < 0:
        return 'negative', score
    else:
        return 'neutral', 0

    
print(indicate('fucking beautiful fucking horrendous fucking insane fucking ugly fucking love',False))
divider()
print(indicate('you look so beautiful in white', True))
divider()
print(indicate(['i', 'like', 'you']))


