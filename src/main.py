import random
import math
import time

from operator import itemgetter

# mengurutkan kumpulan titik
def sortListOfPoints(points):
  sortedPoints = sorted(points, key=itemgetter(0,1))
  return sortedPoints

# divide and conquer
def closestPairDnC(thePoints):
  if (len(thePoints) == 2):
    distance = math.sqrt(pow((thePoints[0][0] - thePoints[1][0]), 2) + pow((thePoints[0][1] - thePoints[1][1]), 2) + pow((thePoints[0][2] - thePoints[1][2]), 2))
    return distance, thePoints[0], thePoints[1]
  else:
    ptsCount = len(thePoints)
    pts1 = []
    pts2 = []
    for i in range(int(ptsCount//2)):
      pts1.append(thePoints[i])
    for i in range(int(ptsCount//2), ptsCount):
      pts2.append(thePoints[i])
    d1, p11, p12 = closestPairDnC(pts1)
    d2, p21, p22 = closestPairDnC(pts2)
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
      point.append(random.randint(0, 10))
    points.append(point)

  print("kumpulan titik yang dihasilkan:")
  print(points)
  print("")
  sortedPoints = sortListOfPoints(points)
  print("kumpulan titik yang telah diurutkan:")
  print(sortedPoints)
  print("")

  # mencari dua buah titik yang memiliki jarak terdekat
  startTime = time.time()
  distance, p1, p2 = closestPairDnC(points)
  finishTime = time.time()
  processingTime = finishTime - startTime

  # menampilkan hasil
  print("Jarak terdekat: " + str(distance))
  print("Titik pertama: " + str(p1[0]) + " " + str(p1[1]) + " " + str(p1[2]))
  print("Titik kedua: " + str(p2[0]) + " " + str(p2[1]) + " " + str(p2[2]))
  print("Waktu pemrosesan: " + str(processingTime))