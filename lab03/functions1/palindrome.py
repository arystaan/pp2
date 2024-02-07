def check(phrase):
    for i in range(len(phrase)//2):
        if phrase[i] != phrase[-i-1]:
            return False
    return True

phr = input()
print(check(phr))