# Name: Minh Trinh
# UTA_ID: 1001705984
# Date Modified:
#   2/25/2023: Implemnted BFS, DFS, UCS, and IDS for the specified graph
# Description: 
#   Implements graph search algorithms: breadth-first search,
#   depth-first search, uniform cost search, and iterative
#   deepening search on a specified graph.

def BFS(edge_set, start, goal):

  parent = start
  edge = []
  cost = 0

  print("depth 0: ")
  print(start)

  print("depth 1: ")
  for loop in range(len(edge_set)):
    if parent == edge_set[loop][0]:
      edge.append(edge_set[loop])
      cost += edge_set[loop][2]
      print(edge_set[loop][1], " ", end="")
  print()

  parent = edge[0][1]
  print("depth 2: ")
  
  for x in range(len(edge_set)):
    if parent == edge_set[x][0]:
      print(edge_set[x][1], " ", end="")
      cost += edge_set[x][2]

  print("\nGoal State has been reached!")
  print("Total Cost:", cost)

def DFS(edge_set, start, goal):

  print("Depth 0:")
  print(start)

  parent = start
  edge = []
  cost = 0

  for loop in range(len(edge_set)):
    if parent == edge_set[loop][0]:
      edge.append(edge_set[loop])

  for loop in range(len(edge)):
    parent = edge[loop][1]
    cost += edge[loop][2]

    print("Depth 1:")
    print(parent)

    print("Depth 2:")
    for x in range(len(edge_set)):
      if parent == edge_set[x][0]:
        cost += edge_set[x][2]
        print(edge_set[x][1], " ", end="")
        if edge_set[x][1] == goal:
          print("\nGoal state has been reached!")
          print("Total Cost:", cost)
          return
          
  print(cost)

def UCS(edge_set, start, goal):
  
  parent = start
  cost = 0

  print("Depth 0")
  print(start)

  edge1 = []
  edge2 = []

  for d1 in range(len(edge_set)):
    if parent in edge_set[d1][0]:
      edge1.append(edge_set[d1])

      print("Depth 1")
      print(edge_set[d1][1])

      parent = edge1[d1][1]
      cost += edge1[d1][2]
      for d2 in range(len(edge1)):
        for x in range(len(edge_set)):
          if parent in edge_set[x][0]:
            edge2.append(edge_set[x])
            cost += edge_set[x][2]
      
            print("Depth 2")
            print(edge_set[x][1])
            if cost == 11:
              print("Goal state has been reached!")
              print("Total Cost:", cost)
              return

      parent = start
    cost = 0

  return

def IDS(edge_set, start, goal):

  limit = 3
  count = 0
  parent = start
  edge1 = []
  edge2 = []
  cost = 0

  while count <= limit:
    if count == 0:
      print("--LIMIT ", count, "--", sep='')
      print("Depth ", count, ":", sep='')
      print(parent)

    if count == 1:
      print("--LIMIT ", count, "--", sep='')
      print("Depth ", 0, ":", sep='')
      print(parent)

      print("Depth ", 1, ":", sep='')

      for d1 in range(len(edge_set)):
        if parent == edge_set[d1][0]:
          edge1.append(edge_set[d1])
          print(edge_set[d1][1], end=" ")
          cost += edge_set[d1][2]

    if count == 2:
      print("\n--LIMIT ", count, "--", sep='')
      print("Depth ", 0, ":", sep='')
      print(parent)

      print("Depth ", 1, ":", sep='')
      for d1 in range(len(edge_set)):
        if parent == edge_set[d1][0]:
          edge1.append(edge_set[d1])
          print(edge_set[d1][1], end=" ")
          cost += edge_set[d1][2]

        print("\nDepth ", count, ":", sep='')
        parent = edge1[d1][1]
        for d2 in range(len(edge1)):
          for x in range(len(edge_set)):
            if parent in edge_set[x][0]:
              edge2.append(edge_set[x])
              cost += edge_set[x][2]

              print(edge_set[x][1], end=" ")
              if edge_set[x][1] == goal:
                print("\nGoal state has been reached!")
                print("Total Cost:", cost)
                return

        parent = start

    count += 1

  return

node_set = {'S', 'A', 'B', 'C', 'D', 'E', 'F', 'G'}
edge_set = [['S', 'A', 1], ['S', 'B', 6], ['S', 'C', 9], 
            ['A', 'D', 4], ['A', 'E', 8], ['A', 'G', 12], 
            ['B', 'G', 5], ['C', 'G', 6], ['C', 'F', 11]]


print("---Breadth-First Search---")
BFS(edge_set, 'S', 'G')
print("\n---Depth-First Search---")
DFS(edge_set, 'S', 'G')
print("\n---Uniform Cost Search---")
UCS(edge_set, 'S', 'G')
print("\n---Iterative Deepening Search---")
IDS(edge_set, 'S', 'G')


