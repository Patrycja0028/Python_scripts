# # Find and explain the results.
t = (2, 4)                  
print(t[2])                    # IndexError: tuple index out of range
                               # obiekt ma tylko indeksy 0 i 1
t.append(6)                    # AttributeError: 'tuple' object has no attribute 'append'
                               # tuple są obiektami niezmienialnymi - nie można dołączyć elementu
a, b = t ; print(a, b)         # 2 4
                               # działa - tzw. unpacking tupli, przypisanie kolejnych jej elementów do nowych zmiennych
