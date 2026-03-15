# Create a dict for conversion of roman numerals/strings (I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M) to arabic numbers. Use different methods. 

# method 1

roman = {
    "I":1,
    "IV":4,
    "V":5,
    "IX":9,
    "X":10,
    "XL":40,
    "L":50,
    "XC":90,
    "C":100,
    "CD":400,
    "D":500,
    "CM":900,
    "M":1000
}

print(roman["X"]) # 10


# method 2

keys = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
values = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

roman = dict(zip(keys, values))
roman # {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

# method 3

roman = {k:v for k,v in zip(keys,values)}
roman # {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
