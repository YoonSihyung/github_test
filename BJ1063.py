import sys
input = sys.stdin.readline

king, stone, moves = input().split()
row = ['1', '2', '3', '4', '5', '6', '7', '8']
column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ckid, rkid = column.index(king[0]), row.index(king[1])
csid, rsid = column.index(stone[0]), row.index(stone[1])

def out(cid, rid, command):
    if 'R' in command:
        if cid == 7:
            return True
    elif 'L' in command:
        if cid == 0:
            return True

    if 'T' in command:
        if rid == 7:
            return True
    elif 'B' in command:
        if rid == 0:
            return True

    return False

def move(cid, rid, command):
    ncid, nrid = cid, rid

    if 'R' in command:
        ncid += 1
    elif 'L' in command:
        ncid -= 1

    if 'T' in command:
        nrid += 1
    elif 'B' in command:
        nrid -= 1

    return (ncid, nrid)

def catch(ckid, rkid, csid, rsid, command):
    tmp_id = move(ckid, rkid, command)

    if tmp_id == (csid, rsid):
        return True
    else:
        return False

for _ in range(int(moves)):
    command = input()

    if out(ckid, rkid, command):
        continue

    if catch(ckid, rkid, csid, rsid, command):
        if out(csid, rsid, command):
            continue
        else:
            ckid, rkid = move(ckid, rkid, command)
            csid, rsid = move(csid, rsid, command)
    else:
        ckid, rkid = move(ckid, rkid, command)

print(column[ckid]+row[rkid])
print(column[csid]+row[rsid])