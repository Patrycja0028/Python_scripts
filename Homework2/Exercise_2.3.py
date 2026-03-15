# Find the sum 1*1 + 3*3 + 5*5 + ... + 2027*2027 [hint: use sum() and range()]. 

result = sum(i*i for i in range(1, 2028, 2))
print(result) # 1390120654
