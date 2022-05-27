graph={'A':['B','C','D'],'B':['E'],'C':['E','D'],'D':[],'E':[]}
visisted=set()

def dfs(visited,graph,root):
    if root not in visisted:
        print(root)
        visisted.add(root)
        for j in graph[root]:
            dfs(visisted,graph,j)
dfs(visisted,graph,'A')