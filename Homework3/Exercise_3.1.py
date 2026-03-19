# For a given word (you may use your name), print it in squares.
# If word = "Python", then the result is
#+---+---+---+---+---+---+
#| P | y | t | h | o | n |
#+---+---+---+---+---+---+

word = "Patrycja"
letters = list(word) # powstaje lista

table_part = "+---+---+---+---+---+---+---+---+"
table_schema = "|{0:^3}|{1:^3}|{2:^3}|{3:^3}|{4:^3}|{5:^3}|{6:^3}|{7:^3}|"
row = table_schema.format(*letters) # *(gwiazdka) rozpakowuje listę

print(table_part +"\n" + row  + "\n" + table_part)
