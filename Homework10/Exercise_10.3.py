# Create pd.DataFrame for the periodic table (ten elements). Column names are Name, Symbol, Weight. index starts from 1 for hydrogen. 

# import pandas as pd

data = {
    "Name": [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"
    ],
    "Symbol": [
        "H", "He", "Li", "Be", "B",
        "C", "N", "O", "F", "Ne"
    ],
    "Weight": [
        1.008, 4.0026, 6.94, 9.0122, 10.81,
        12.011, 14.007, 15.999, 18.998, 20.180
    ]
}
data
# {'Name': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon'],
#  'Symbol': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne'],
#  'Weight': [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.18]}

df = pd.DataFrame(data, index=range(1, 11))

print(df)
#          Name Symbol   Weight
# 1    Hydrogen      H   1.0080
# 2      Helium     He   4.0026
# 3     Lithium     Li   6.9400
# 4   Beryllium     Be   9.0122
# 5       Boron      B  10.8100
# 6      Carbon      C  12.0110
# 7    Nitrogen      N  14.0070
# 8      Oxygen      O  15.9990
# 9    Fluorine      F  18.9980
# 10       Neon     Ne  20.1800
