# IBM ile Kodluyoruz: CyberStart #4 Week-2 Python App 2

# point1 and point2 is a tuple with a form of (x,y)
def euclideanDistance(point1, point2):
    return (((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2)) ** (1/2)

points = [(3,6),(13,15),(24,12),(5,-5),(6,10),(0,14),(30,6),(2,-10),(10,20)]
distances = []

for i in range(len(points)):
    j = i+1
    while j < len(points):
        distances.append(euclideanDistance(points[i], points[j]))
        j +=1


# pretending that the length of points list is atleast 2 so distances list length will be >= 1
minimumDistance = distances[0]

for i in range(1,len(distances)):
    if minimumDistance > distances[i]:
        minimumDistance = distances[i]

print("Minimum distance is: ", minimumDistance)

# We expect the minimum distance to be 5.0 with the points (3,6) and (6,10)
assert minimumDistance == 5.0