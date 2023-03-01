import random
import math

from datetime import datetime
from operator import itemgetter

# sort list of points
def sortListOfPoints(points):
  sortedPoints = sorted(points, key=itemgetter(0,1))
  return sortedPoints

# calculate euclidean distance
def euclidean_distance(p1, p2):
  return math.sqrt(pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2) + pow((p1[2] - p2[2]), 2))

# brute force
def closestPairBruteForce(thePoints):
  distance = float('inf')
  p = []
  count = 0
  for i in range(len(thePoints)-1):
    for j in range(i+1, len(thePoints)):
      if (thePoints[i] != thePoints[j]):
        temp_distance = euclidean_distance(thePoints[i], thePoints[j])
        count += 1
        if (temp_distance < distance):
          distance = temp_distance
          p.clear()
          p.append(thePoints[i])
          p.append(thePoints[j])

  return distance, p[0], p[1], count

# divide and conquer
def closestPairDnC(thePoints):
  if (len(thePoints) <= 3):
    return closestPairBruteForce(thePoints)
  else:
    ptsCount = len(thePoints)
    pts1 = []
    pts2 = []
    midPts = thePoints[int(ptsCount//2)]
    min_distance = 0
    for i in range(int(ptsCount//2)):
      pts1.append(thePoints[i])
    for i in range(int(ptsCount//2), ptsCount):
      pts2.append(thePoints[i])
    d1, p11, p12, c1 = closestPairDnC(pts1)
    d2, p21, p22, c2 = closestPairDnC(pts2)
    if (d1 < d2):
      min_distance = d1
    else:
      min_distance = d2
    
    greyArea = []
    for i in range(len(thePoints)):
      if ((thePoints[i] != midPts[0]) and (abs(thePoints[i][0] - midPts[0]) < min_distance) and (abs(thePoints[i][1] - midPts[1]) < min_distance)):
        greyArea.append(thePoints[i])
    
    gDist, gp1, gp2, cg = closestPairGreyArea(greyArea, min_distance)
    if (gDist < min_distance):
      return gDist, gp1, gp2, (c1+c2+cg)
    else:
      if (min_distance == d1):
        return d1, p11, p12, (c1+c2+cg)
      else:
        return d2, p21, p22, (c1+c2+cg)

# points in grey area
def closestPairGreyArea(thePoints, dist):
  distance = dist
  p = []
  count = 0
  for i in range(len(thePoints)-1):
    for j in range(i+1, len(thePoints)):
      temp_distance = euclidean_distance(thePoints[i], thePoints[j])
      count += 1
      if (temp_distance < distance):
        distance = temp_distance
        p.clear()
        p.append(thePoints[i])
        p.append(thePoints[j])
  
  if (len(p) == 0):
    return distance, None, None, count
  else:
    return distance, p[0], p[1], count


### MAIN PROGRAM ###
if __name__ == "__main__":
  # input number of points by user
  n = int(input("Jumlah titik yang ingin dibangkitkan: "))

  # generate points
  points = []
  for i in range(n):
    point = []
    for j in range(3):
      point.append(random.randint(0, 100))
    points.append(point)

  print("kumpulan titik yang dihasilkan:")
  # print(points)
  print("")
  sortedPoints = sortListOfPoints(points)
  print("kumpulan titik yang telah diurutkan:")
  # print(sortedPoints)
  print("")

  # find closest pair
  startTime = datetime.now()
  distance, p1, p2, count = closestPairDnC(points)
  finishTime = datetime.now()
  processingTime = finishTime - startTime

  # show result
  print("HASIL PENCARIAN:")
  print("Jarak terdekat: " + str(distance))
  print("Titik terdekat pertama: " + str(p1[0]) + " " + str(p1[1]) + " " + str(p1[2]))
  print("Titik terdekat kedua: " + str(p2[0]) + " " + str(p2[1]) + " " + str(p2[2]))
  print("Banyaknya operasi perhitungan rumus Euclidian: " + str(count))
  print("Waktu pemrosesan: " + str(processingTime.total_seconds()))
  print("(pemrosesan dilakukan menggunakan laptop Lenovo ideapad gaming 3)")