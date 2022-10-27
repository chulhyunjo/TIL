n = int(input())
maxD = list(map(int, input().split()))
minD = maxD[:]

for i in range(n - 1):
    x, y, z = map(int, input().split())

    nx = min(minD[0], minD[1]) + x
    ny = min(minD[0], minD[1], minD[2]) + y
    nz = min(minD[1], minD[2]) + z
    minD = [nx, ny, nz]

    nx = max(maxD[0], maxD[1]) + x
    ny = max(maxD[0], maxD[1], maxD[2]) + y
    nz = max(maxD[1], maxD[2]) + z
    maxD = [nx,ny,nz]

print(max(maxD), min(minD))
