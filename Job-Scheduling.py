arr = [['J1', 5, 85], ['J2', 4, 25], ['J3', 3, 16], ['J4', 3, 40], ['J5', 4, 55],
       ['J6', 5, 19], ['J7', 2, 92], ['J8', 3, 80], ['J9', 7, 15]]
print("Following is maximum profit sequence of jobs")

# length of array
n = len(arr)
t = 7

# Sort all jobs according to
# decreasing order of profit
for i in range(n):
   for j in range(n - 1 - i):
     if arr[j][2] < arr[j + 1][2]:
       arr[j], arr[j + 1] = arr[j + 1], arr[j]

# To keep track of free time slots
result = [False] * t

# To store result (Sequence of jobs)
job = ['-1'] * t

# To store profit
sumOfProfit = 0

# Iterate through all given jobs
for i in range(len(arr)):

   # Find a free slot for this job
   # (Note that we start from the
   # last possible slot)
   for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

     # Free slot found
     if result[j] is False:
       result[j] = True
       job[j] = arr[i][0]
       sumOfProfit += arr[i][2]
       break

# print the sequence
print(job)
print(sumOfProfit)