string = input()
upp = sum(map(lambda x: x.isupper(), string))
low = sum(map(lambda x: x.islower(), string))
print(f"Upper: {upp} Lower: {low}")