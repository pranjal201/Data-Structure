
# 841. Keys and Rooms
# There are n rooms labeled from 0 to n - 1 and all the rooms 
# are locked except for room 0. Your goal is to visit all the rooms. 
# However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. 
# Each key has a number on it, denoting which room it unlocks, 
# and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can 
# obtain if you visited room i, return true if you can visit all the rooms,
# or false otherwise.
# rooms = [[1],[2],[3],[]]
# Used stack approach
def canVisitAllRooms(rooms)->bool:
    stack = [0]
    seen_rooms = set(stack)

    while stack:
        idx = stack.pop()
        for j in rooms[idx]:
            if j not in seen_rooms:
                stack.append(j)
                seen_rooms.add(j)
    return len(seen_rooms) == len(rooms)


if __name__ =="__main__":
    rooms =[[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]]
    print(canVisitAllRooms(rooms))

# Time Complexity O(n^2)
# Space Complexity O(n)
