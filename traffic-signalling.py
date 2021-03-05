import numpy as np
import sys

# D: the duration of the simulation, in seconds
# I: the number of intersections (with IDs from 0 to I -1 )
# S: the number of streets
# V: the numbers of cars
# F: the bonus points for each car that reaches its destination before time D .

# Comment this line if you are about to submit
#try:
#	sys.stdin = open("hashcode.in", "r")
#except:
#	pass

filename="hashcode.in"

with open(filename, mode="r") as f:
	duration, n_intersections, n_streets, n_cars, bonus_points =  list(map(int, f.readline().strip().split()))

	for line in f:
		parts = line.split()
		elif isinstance(parts[1],int): # streets
			inters1 = int(parts[0])
			inters2 = int(parts[1])
			street_name = parts[2]
			street_length = int(parts[3])
		elif isinstance(parts[0],int): # car route
			car_movements = int(parts[0])
			streets = parts[1:]


