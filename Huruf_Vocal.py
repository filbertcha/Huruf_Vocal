vocal = "aiueo"
a = input("ketik bang: ").lower().strip()
for letter in a:
    if letter in vocal :
        a = a.replace(letter,"")
print(a)
