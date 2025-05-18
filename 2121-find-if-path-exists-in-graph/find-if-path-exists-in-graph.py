class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
            graph = defaultdict(list)


            for nodeOne, nodeTwo in edges:
                graph[nodeOne].append(nodeTwo)
                graph[nodeTwo].append(nodeOne)
            
    
            def isPathExists_iteration_dfs(start, end):


                visited = set()

                toBevisited = [start]


                while toBevisited:

                    currentNode = toBevisited.pop()

                    if currentNode == end:
                        return True
                    


                    for next_node in graph[currentNode]:
                        if next_node not in visited:
                            visited.add(next_node)
                            toBevisited.append(next_node)
                return False

            def isPathExists_recurrsion_bfs(start, end):


                    visited = set()
                    def isPathExist(current_node):

                        if current_node == end:
                            return True
                        

                        for next_child in graph[current_node]:
                            if next_child not in visited:
                                visited.add(next_child)
                                if isPathExist(next_child):
                                    return True
                        
                        return False
                
                    return isPathExist(start)


            def isPathExisits_iteration_bfs(start, end):
                visited = set()

                toBeVisistedNodes = deque([start])

                while toBeVisistedNodes:

                    for _ in range(len(toBeVisistedNodes)):

                        current_node = toBeVisistedNodes.popleft()

                        if current_node == end:
                            return True

                        for next_child in graph[current_node]:
                            if next_child not in visited:
                                visited.add(next_child)
                                toBeVisistedNodes.append(next_child)
                return False


                
            def isPathExisits_recurrsion_bfs(start, end):
                pass



            # return isPathExists_iteration_dfs(start, end)
            # return isPathExists_recurrsion_bfs(start, end)
            return isPathExisits_iteration_bfs(start, end)


        