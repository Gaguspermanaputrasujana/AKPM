#baca dari sumber/ file
from tkinter import N


with open("test.txt") as f:
    lines=f.read()
    print(lines) 
print(lines)

#tulis ke file
with open("text.txt",'w') as g:
    g.write(lines)
    g.write(lines)

print('finished')
n=2
print(n)