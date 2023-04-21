def dfs(graph, start_node):
    visit = []
    stack = [start_node]

    while stack:
        top = stack.pop()
        if top not in visit:
            visit.append(top)
            stack.extend(graph[top])

    return visit

def solution(n, computers):
    routes = {}

    for i, computer in enumerate(computers):
        for j, c in enumerate(computer):
            if i!=j and c==1:
                routes[i] = routes.get(i, []) + [j]
    print(routes)
    print([dfs(routes, n) for n in routes])
    paths = map(sorted,[dfs(routes, n) for n in routes])

    return len({''.join(map(str,path)) for path in paths})

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


