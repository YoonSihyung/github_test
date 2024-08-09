import sys

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    code = input().rstrip()
    stop = False

    while code:
        if stop:
            break

        if code[0] == '0':
            if len(code) >= 2 and code[1] == '1':
                code = code[2:]
            else:
                print('NO')
                break

        elif code[0] == '1':
            if code[1] != '0' or code[2] != '0':
                print('NO')
                break

            else:
                for i in range(3, len(code)):
                    if code[i] == '1':
                        if len(code) == i+1:
                            code = code[i+1:]
                        elif i+1 < len(code) and code[i+1] == '0':
                            if i+2 < len(code) and code[i+2] == '1':
                                code = code[i+1:]
                                break
                            else:
                                print('NO')
                                stop = True
                                break

    if len(code) == 0:
        print('YES')