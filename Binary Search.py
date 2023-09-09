def binary_search(a, start, end, x):
  if(start <= end):
    middle = (start+end)//2
    print("Identified Middle Element")
    if(a[middle] == x):
      print("Identified Target Element Index")
      return middle
      

    if(a[middle] > x):
      print("Using the left part of the Array")
      return binary_search(a, start, middle-1, x)

    if(a[middle] < x):
      print("Using the right part of the Array")
      return binary_search(a, middle+1, end, x)

  return -1 # not found

# Get an Array for searching
a = [int(x) for x in input("Enter list of integers:").split()]
# Sort the array
a.sort()
start = 0
end = len(a)
#x = int(input("Enter target element to search: "))
# Ask user to exit

if __name__ == '__main__':
  print("The array is ", a)
  while True:
    x = input("Enter target element to search or 'quit' to exit: ")
    if x == 'quit': break
    index_result = binary_search(a, start, end, int(x))
    print("The position of the search element", x, " is ",index_result + 1)
  
  #print("The index of the search element", x, "x is ",index_result)