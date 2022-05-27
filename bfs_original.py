#bfs need is display all adjucent node
#first go to breadth then incease level
#bfs{0,1,2,3,4}
#queue will be use 
#enque at rear position
#deque from front
#we will deque element from left side
import collections
def bfs(graph,root):

    visited=set()
    queue=collections.deque([root])
    
    while queue:
        vertex=queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)

    print(visited)





graph={0:[1,2,3],1:[0,2],2:[0,1,4],3:[0],4:[2]}
bfs(graph,0)