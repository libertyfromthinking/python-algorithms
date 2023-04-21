def solution(tickets):
    route = {}
    stack = ['ICN']
    visit = []

    for t in tickets:
        route[t[0]] = route.get(t[0],[]) + [t[1]]

    while stack:
        node = stack[-1]
        if node not in route or len(route[node])==0:
            visit.append(stack.pop())
        else:
            stack.append(route[node].pop())
    visit.reverse()
    return visit


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# 현재 공항에서 갈 수 있는 모든 공항을 큐에 삽입
# 기존의 리스트에서는 삭제
#

