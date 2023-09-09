from typing import DefaultDict
INT_MAX = 2147483647
tsp = [[-1, 10, 15, 20], [10, -1, 35, 25], [15, 35, -1, 30], [20, 25, 30, -1]]
sm = 0
counter = 0
j = 0
i = 0
mn = INT_MAX
visitedRouteList = DefaultDict(int)

visitedRouteList[0] = 1
route = [0] * len(tsp)
while i < len(tsp) and j < len(tsp[i]):
   if counter >= len(tsp[i]) - 1:
      break
   if j != i and (visitedRouteList[j] == 0):
      if tsp[i][j] < mn:
         mn = tsp[i][j]
         route[counter] = j + 1
   j += 1
   if j == len(tsp[i]):
      sm += mn
      mn = INT_MAX
      visitedRouteList[route[counter] - 1] = 1
      j = 0
      i = route[counter] - 1
      counter += 1

i = route[counter - 1] - 1
for j in range(len(tsp)):
   if (i != j) and tsp[i][j] < mn:
      mn = tsp[i][j]
      route[counter] = j + 1
sm += mn
print("Minimum Cost is :", sm)