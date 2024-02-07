def permutation(word):
    if len(word) == 1:
        return [word]
    
    perms = permutation(word[1:])
    char = word[0]
    res = []

    for per in perms:
        for i in range(len(per)+1):
            res.append(per[:i] + char + per[i:])
    
    return res

wrd = input()
print(permutation(wrd))