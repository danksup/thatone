def simple_word_match_algorithm(word, target):
    score = 0

    for i in word:
        if i in target:
            score += 0.1
        else:
            score -= 0.08
    
    delta_len = abs(len(word) - len(target))

    if word == target:
        score += 100
    elif len(word) is not len(target):
        score -= delta_len * 0.05
    else:
        score += 0.1
    return score

def suggest_word(word, word_dict):
    best_score = 0
    best_match = None

    for i in word_dict:
        score = simple_word_match_algorithm(word, i)
        print(f'{score} for {word} to {i}')
        if score > best_score:
            best_score = score
            best_match = i

    if best_score >= 0.3:
        return best_match, best_score
    else:
        return 'no word matches', best_score

def divider():
    print(f'{'-'*50}divider{'-'*50}')


word_dict = ['apple', 'banana', 'orange', 'angel']


print(suggest_word('ananaa', word_dict))
divider()
print(suggest_word('appel', word_dict))
divider()
print(suggest_word('range', word_dict))
divider()
print(suggest_word('angel', word_dict))
divider()
print(suggest_word('ange', word_dict))
