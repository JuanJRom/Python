# Function for sort a list

letters = ['e', 'f', 'g', 'b', 'a', 'c', 'd']
numbers = [9, 7, 2, 5, 4, 3, 8, 6, 1]


def mysort(n):
    for i in range(1, len(n)):
        for j in range(len(n) - i):
            if n[j + 1] < n[j]:
                n[j + 1], n[j] = n[j], n[j + 1]  # I learned this in class today,
    return n                                     # is very useful for not use variable aux


print(letters)
mysort(letters)
print(letters)
print(numbers)
mysort(numbers)
print(numbers)
