import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from insightmars import InSightAPI, utils
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--camera', "-c", help='Camera: icc / idc', default="idc")
args = parser.parse_args()

InSightMission = InSightAPI(af=args.camera)
json_request = InSightMission.make_request()
count = InSightMission.get_count(json_request)
metadata = InSightMission.get_images_metadata(json_request, count)


sols=[]
solcount=[]
for i in metadata:
	sols.append(i["sol"])

print(sols)
each_sol = list(set(sols))
for i in each_sol:
	solcount.append(sols.count(i))
print(each_sol)
print(solcount)

x_pos = [i for i, _ in enumerate(each_sol)]

plt.bar(x_pos, solcount, color='red')
plt.xlabel("Sol")
plt.ylabel("Number of Images")
plt.title("Number of Images per Sol")

plt.xticks(x_pos, each_sol)

plt.show()

