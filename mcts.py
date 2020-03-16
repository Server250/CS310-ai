import math
import sys

def ucb1(avVal, pVisits, totalVisits) -> float:
	return avVal+(2*(math.sqrt(math.log(pVisits)/(totalVisits))))
	


if __name__ == "__main__":
	if (len(sys.argv)>=4):
		print(ucb1(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])))
