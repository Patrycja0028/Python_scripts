#Reversing a part of a list in place, reverse_range(L, left, right), the right index is included. Write iterative and recursive versions.

## Example.
#L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#reverse_range(L, 3, 6)   # index 6 is included!
#print(L)   # [0, 1, 2, 6, 5, 4, 3, 7, 8, 9]   # the list L changed
## The numbers outside the range are intact.

def reverse_range(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def reverse_range_recursive(L, left, right):
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    reverse_range_recursive(L, left + 1, right - 1)
