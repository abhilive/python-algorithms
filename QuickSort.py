
# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


# data = [-2, 0, 50]

# taking multiple inputs at a time

userInput = input("Enter multiple values : ")
print("You entered: " + userInput)

intArray, strArray = [], []

for data in userInput.split():
  print(data)
  try:
    val = int(data)
    print("Input is an integer number.")
    print("Input number is: ", val)
    intArray.append(val)
    continue;
  except ValueError:
    try:
      val = str(data)
      print("Input is a string.")
      print("Input string is: ", val)
      strArray.append(val)
      continue;
    except ValueError:
      print("Entry is neither integer nor string type.")

print("Unsorted Array (Integer)")
print(intArray)

print("Unsorted Array (String)")
print(strArray)

sizeOfStrArr = len(strArray)
print (sizeOfStrArr)
quickSort(strArray, 0, sizeOfStrArr - 1)

sizeOfIntArr = len(intArray)
print (sizeOfIntArr)
quickSort(intArray, 0, sizeOfIntArr - 1)

print('Sorted Array in Ascending Order:')
print(intArray + strArray)

# intData = [int(x) for x in input("Enter multiple values(int): ").split()]
# print("intData: ", intData)

# strData = [str(x) for x in input("Enter multiple values(str): ").split()]
# print("strData: ", strData)

# print("Unsorted Array (String)")
# print(data)

# size = len(data)
# print (size)
# quickSort(data, 0, size - 1)

# print('Sorted Array in Ascending Order:')
# print(data)