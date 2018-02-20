"""
BogoSort.py
The worst sort ever written
by Dylan Hamer
"""

import random
import time

"""Check if array is sorted"""
def sorted(array):
  sorted = True
  for index, item in enumerate(array[:-1]):
    if not item < array[index+1]:
      sorted = False
  return sorted

"""Make a random array for testing"""
def generateArray(size):
  newArray = []
  for index in range(size):
    newArray.append(random.randint(0,256))
  return newArray
  
"""Randomise the order of the array"""
def shuffle(array):
  print("Shuffling...")
  originalArray = array[:]
  shuffledArray = []
  for item in array:
    randomIndex = random.randint(0, len(originalArray)-1)
    shuffledArray.append(originalArray.pop(randomIndex))
  return shuffledArray

"""Sort an array in the worst way possible"""
def sort(array):
  while not sorted(array):
    array = shuffle(array[:])
  return array
  
"""Calculate the time taken to do the sort"""
def calculateTimeTaken(startTime, endTime):
  epochTaken = endTime - startTime
  timeStructure = time.localtime(epochTaken)
  hours, minutes, seconds = timeStructure.tm_hour, timeStructure.tm_min, timeStructure.tm_sec
  print("{} {} {}".format(hours,minutes,seconds))
  return hours, minutes, seconds
  
"""Main function, sort a generated list using a bogo sort"""
def main():
  oldTime = time.time()
  array = generateArray(2)
  sortedArray = sort(array[:])
  newTime = time.time()
  hoursTaken, minutesTaken, secondsTaken = calculateTimeTaken(oldTime, newTime)
  print("Sorted the array!")
  print("Original: {}".format(array))
  print("Sorted: {}".format(sortedArray))
  print("Time taken: {} hours, {} minutes and {} seconds".format(hoursTaken, minutesTaken, secondsTaken))

main()
    
    
