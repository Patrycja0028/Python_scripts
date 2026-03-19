# Make a loop over integer numbers from 1 to 40.
# If x is divided by 5 then print a message 'x is divided by 5'.
# If x is divided by 7 then print a message 'x is divided by 7'.
# If x is divided by 5 and 7 then print a message 'x is divided by 5 and 7'.
# Skip x = 13.
# If x is not divided by 5 and x is not divided by 7 
# then print a message 'x is not important'.
# Prepare two solutions with 'while' and 'for' loops.

# -------------------------------------------------------------------------------------------------------
# while version
# -------------------------------------------------------------------------------------------------------
i = 1

while i < 41:
     if i % 5 == 0:
         if i % 7 == 0:
             print(f"{i} is divided by 5 and 7")
             pass
         else: print(f"{i} is divided by 5")
         pass
     elif i % 7 == 0:
         print(f"{i} is divided by 7")
         pass
     elif i == 13:
         pass
     else: print(f"{i} is not important")
       i = i + 1

# -------------------------------------------------------------------------------------------------------
# for version
# -------------------------------------------------------------------------------------------------------

for i in range(1,41):
     if i % 5 == 0:
         if i % 7 == 0:
             print(f"{i} is divided by 5 and 7")
             pass
         else: print(f"{i} is divided by 5")
         pass
     elif i % 7 == 0:
         print(f"{i} is divided by 7")
         pass
     elif i == 13:
         pass
     else: print(f"{i} is not important")


# 1 is not important
# 2 is not important
# 3 is not important
# 4 is not important
# 5 is divided by 5
# 6 is not important
# 7 is divided by 7
# 8 is not important
# 9 is not important
# 10 is divided by 5
# 11 is not important
# 12 is not important
# 14 is divided by 7
# 15 is divided by 5
# 16 is not important
# 17 is not important
# 18 is not important
# 19 is not important
# 20 is divided by 5
# 21 is divided by 7
# 22 is not important
# 23 is not important
# 24 is not important
# 25 is divided by 5
# 26 is not important
# 27 is not important
# 28 is divided by 7
# 29 is not important
# 30 is divided by 5
# 31 is not important
# 32 is not important
# 33 is not important
# 34 is not important
# 35 is divided by 5 and 7
# 36 is not important
# 37 is not important
# 38 is not important
# 39 is not important
# 40 is divided by 5
