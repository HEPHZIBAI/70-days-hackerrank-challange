'''https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/vacant-room-position'''





def find_most_vacant_neighbor_room(buildings):
    r = 5
    c = 5
    vacant_found = False

    for i in range(r):
        if 0 in buildings[i]:
            vacant_found = True
            break

    if not vacant_found:
        return -1

    max_vacant_neighbors = -1
    most_vacant_room = (-1, -1)

    for i in range(r):
        for j in range(c):
            if buildings[i][j] == 1:
                vacant_neighbors = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < r and 0 <= nj < c and buildings[ni][nj] == 0:
                            vacant_neighbors += 1

                if vacant_neighbors > max_vacant_neighbors:
                    max_vacant_neighbors = vacant_neighbors
                    most_vacant_room = (i, j)

    return most_vacant_room

# Test the function with the given sample inputs

buildings1 = []
for i in range(5):
    a=list(map(int,input().split()))
    buildings1.append(a)
hh=find_most_vacant_neighbor_room(buildings1)
if(hh==-1):
    print("-1")
else:
    for i in hh:
        print(i,end=" ")