# 学习笔记week04

```
二分查找的前提
1.目标函数具有单调性
2.存在上下界
3.能够通过索引访问
```

```
#dfs模板 python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
			
# bfs模板 Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([root]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.append(nodes)
	# other processing work 
	...
```

