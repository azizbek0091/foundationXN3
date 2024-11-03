import os; os.system("cls")

file = open("3-misol.txt", "rt")

qancha = 0
gap = file.readline()
print(gap)

for i in gap:
    if (i.isalpha()):
        qancha += 1

print(f"Lotin harfi {qancha} ta")
file.close()