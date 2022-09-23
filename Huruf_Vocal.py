tu = "aiueo"
hi = input("ketik bang: ").lower().strip()
for letter in hi:
    if letter in tu:
        hi = hi.replace(letter,"")
print(hi)
