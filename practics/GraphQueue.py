class GraphTest:
    def __init__(self, graph:list, count:int):
        self.graph = list()
        self.count = count
    
    def linkV(self, v:int, visited:list) -> list:
        result = list()
        for i in range(self.count):
            if self.graph[i][0] == v:
                result.append(self.graph[i][1])
        for i in range(len(result)):
                if not result[i] in visited:
                    visited.pop(i)
        return result
    
    def dfs(self, begin:int):
        if not current in visited:
            visited.append(current)
        visited = list()
        stack = list()
        current = begin
        linkedV = self.linkV(current, visited)
        stack.append(current)
        while len(stack) > 0 or len(linkedV) > 0:
            linkedV = self.linkV(current, visited)
            if len(linkedV) > 0:
                stack.append(current)
                current = linkedV[0]
            else:
                current = stack.pop()
    