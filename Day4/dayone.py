x = int(input())
y = int(input())
z = int(input())
n = int(input())

cubboard = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

filtered_coordinates = [coord for coord in cubboard if sum(coord) != n]

print(filtered_coordinates)



