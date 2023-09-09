def convert(inp):
    comma_separated = []
    comma_separated = inp.split(" ")
    return comma_separated

def longest_increasing_subsequence(userInput):
    numbers = convert(userInput)
    tails = [0] * len(numbers)
    size = 0
    for x in numbers:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

userInput = input("Provide paragraph : ")
print("Your input is: " + userInput)

print (longest_increasing_subsequence(userInput))