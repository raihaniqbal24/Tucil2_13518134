import random
import math

from datetime import datetime
from operator import itemgetter

# mengurutkan kumpulan titik
def sortListOfPoints(points):
  sortedPoints = sorted(points, key=itemgetter(0,1))
  return sortedPoints

# brute force
def closestPairBruteForce(thePoints):
  distance = float('inf')
  p = []
  count = 0
  for i in range(len(thePoints)):
    for j in range(len(thePoints)):
      if (thePoints[i] != thePoints[j]):
        temp_distance = math.sqrt(pow((thePoints[i][0] - thePoints[j][0]), 2) + pow((thePoints[i][1] - thePoints[j][1]), 2) + pow((thePoints[i][2] - thePoints[j][2]), 2))
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
    for i in range(int(ptsCount//2)):
      pts1.append(thePoints[i])
    for i in range(int(ptsCount//2), ptsCount):
      pts2.append(thePoints[i])
    d1, p11, p12, c1 = closestPairDnC(pts1)
    d2, p21, p22, c2 = closestPairDnC(pts2)
    if (d1 > d2):
      return d2, p21, p22, c2
    else:
      return d1, p11, p12, c1
    # greyArea = []



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
  startTime = datetime.now()
  distance, p1, p2, count = closestPairDnC(points)
  finishTime = datetime.now()
  processingTime = finishTime - startTime

  # menampilkan hasil
  print("Jarak terdekat: " + str(distance))
  print("Titik pertama: " + str(p1[0]) + " " + str(p1[1]) + " " + str(p1[2]))
  print("Titik kedua: " + str(p2[0]) + " " + str(p2[1]) + " " + str(p2[2]))
  print("Banyaknya operasi perhitungan rumus Euclidian: " + str(count))
  print("Waktu pemrosesan: " + str(processingTime.total_seconds()))