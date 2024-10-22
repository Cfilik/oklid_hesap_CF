points=[(6,9),(1,4),(10,14),(5,11)]
distances=[]
 
def euclideanDistance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5
   
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
       
print(min(distances))