# Explain the results.
x = 5                             
x == 5 and 3 + 8   # 11          ## TRUE  and 11 -> python zwraca ostatnią wartość
x == 4 and 3 + 8   # False       ## FALSE and 11 -> działanie programu zatrzymuje się na FALSE i zwraca taką wartość logiczną
3 + 8 and x == 5   # True        ## 11 and TRUE -> python zwraca ostatnią wartość
3 + 8 and x == 4   # False       ## x == 4 daje wartość logiczną FALSE

isinstance(True, int)    # True      ## funkcja isinstance() sprawdza czy obiekt jest danego typu
                                     ## wartości logiczne mają typ bool, który jest podtypem inta, zatem otrzymujemy wartość logiczną TRUE
isinstance(True, bool)   # True      ## wartości logiczne mają typ bool, zatem TRUE
