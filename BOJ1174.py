n = int(input())

decrease = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result_idx = 0
result = 0

while len(decrease) != 0:
    pop_num = decrease.pop(0)
    result_idx += 1
    result = pop_num
    
    if result_idx == n:
        break
    
    for r in range(0, pop_num % 10):
        decrease.append(10 * pop_num + r)
    
if result_idx < n:
    print(-1)

elif result_idx == n:
    print(result)