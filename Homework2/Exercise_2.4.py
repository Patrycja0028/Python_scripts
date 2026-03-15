# (a) Find Unicode code points (int) for all characters of your name.
# Example: "Andrzej" --> [65, 110, 100, 114, 122, 101, 106]

name = "Patrycja"
codes = [ord(c) for c in name]

print(codes) # [80, 97, 116, 114, 121, 99, 106, 97]


#(b) Prepare the periodic table (ten elements) as a list
#pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), ...].
#Use pt to print a table (3 right + 20 left + 6 center + 10 right)
#+---+--------------------+------+----------+
#|No.|Name (en)           |Symbol|Weight (u)|
#+---+--------------------+------+----------+
#|  1|Hydrogen            |  H   |         1|
#|  2|Helium              |  He  |         4|
#|   | ...                |      |          |
#+---+--------------------+------+----------+
#Hint: use the for loop:
#for (n, name, symbol, weight) in pt:
#    # use variables (n, name, symbol, weight) to create a proper line

pt = [
    (1, "Hydrogen", "H", 1),
    (2, "Helium", "He", 4),
    (3, "Lithium", "Li", 7),
    (4, "Beryllium", "Be", 9),
    (5, "Boron", "B", 11),
    (6, "Carbon", "C", 12),
    (7, "Nitrogen", "N", 14),
    (8, "Oxygen", "O", 16),
    (9, "Fluorine", "F", 19),
    (10, "Neon", "Ne", 20),
]

print("+---+--------------------+------+----------+")
print("|No.|Name (en)           |Symbol|Weight (u)|")
print("+---+--------------------+------+----------+")

for (n, name, symbol, weight) in pt:
    print(f"|{n:>3}|{name:<20}|{symbol:^6}|{weight:>10}|")

print("+---+--------------------+------+----------+")
