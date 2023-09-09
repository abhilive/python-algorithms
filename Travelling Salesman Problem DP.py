MAX = 999999

def TSP(mask, pos, graph, dp,n, visited):
	if mask == visited:
		return graph[pos][0]
	if dp[mask][pos] != -1:
		return dp[mask][pos]
	
	ans = MAX 
	for city in range(0, n):
		if ((mask & (1 << city)) == 0):
			new = graph[pos][city] + TSP(mask|(1<<city),city, graph, dp, n, visited)
			ans = min(ans, new)
	
	dp[mask][pos]=ans
	return dp[mask][pos]




graph = [[0, 10, 15, 20], [10, 0, 35, 25],
		[15, 35, 0, 30], [20, 25, 30, 0]]
n = 4
visited = (1 << n) - 1
r,c=16,4
dp=[[-1 for j in range(c)]for i in range(r)]
for i in range(0, (1<<n)):
	for j in range(0, n):
		dp[i][j] = -1

print(TSP(1, 0,graph, dp, n, visited))
