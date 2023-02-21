# Python sample to demonstrate command line arguments

import sys
import datetime

runTime = datetime.datetime.now()
print("Time run:", runTime)

# total arguments
n = len(sys.argv)
print("Total arguments passed: ", n)

# display name of script
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

# add numbers
sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])

print("\nSum of all numbers:", sum)
