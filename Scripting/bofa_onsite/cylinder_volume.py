#cylinder_volume.py

import math
import argparse

def cylinder_volume(rad,h):
	return((math.pi)*(rad**2)*h)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("radius", help = "Enter radius of the cylinder",type = float)
	parser.add_argument("height", help = "Enter height of the cylinder",type = float)
		
	

	args = parser.parse_args()
	result = cylinder_volume(args.radius, args.height)

	print("Volume of the cylinder with radius ", str(args.radius), " and ", str(args.height), " is ", str(result))

if __name__ == '__main__':
	main()
