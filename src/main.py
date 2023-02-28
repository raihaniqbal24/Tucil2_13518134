import random
import math
import time

# divide and conquer
def closestPair(thePoints):
  if (len(thePoints) == 2):
    distance = math.sqrt(pow((thePoints[0][0] - thePoints[1][0]), 2) + pow((thePoints[0][1] - thePoints[1][1]), 2) + pow((thePoints[0][2] - thePoints[1][2]), 2))
    return distance, thePoints[0], thePoints[1]
  else:
    ptsCount = len(thePoints)
    pts1 = []
    pts2 = []
    for i in range(ptsCount/2):
      pts1.append(thePoints[i])
    for i in range((ptsCount/2)+1, ptsCount):
      pts2.append(thePoints[i])
    d1, p11, p12 = closestPair(pts1)
    d2, p21, p22 = closestPair(pts2)
    if (d1 > d2):
      return d2, p21, p22
    else:
      return d1, p11, p12


if __name__ == "__main__":
  # input jumlah titik oleh pengguna
  n = int(input("Jumlah titik yang ingin dibangkitkan: "))

  # membangkitkan titik-titik
  points = []
  for i in range(n):
    point = []
    for j in range(3):
      point.append(random.randint(0, 100))
    points.append(point)

  print(points)

  # mencari dua buah titik yang memiliki jarak terdekat
  startTime = time.time()
  distance, p1, p2 = closestPair(points)
  finishTime = time.time()
  processingTime = finishTime = startTime

  # menampilkan hasil