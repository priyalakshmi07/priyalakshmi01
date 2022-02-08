
M = []
trace = 0
row_repeat = 0
col_repeat = 0
increment = 0

TestCases = int(input())
case = 1

for j in range(TestCases):
    row = int(input())
    for i in range(row):
        row_list= list(map(int, input().split()))
        M.append(row_list)

        trace = trace + row_list[increment]#to calculate diagonal
        increment = increment + 1

        if row_list[0] in row_list[1:]:#row repeat
            row_repeat = row_repeat + 1

    for z in range(row):
        col_list = [k[z] for k in M]

        if M[-1][z] in col_list[:-1]:#col repeat
            col_repeat = col_repeat + 1

    print(f"Case #{case}:", trace, row_repeat, col_repeat)
    case = case + 1

    trace = 0
    increment = 0
    row_repeat = 0
    col_repeat = 0
    M.clear()
