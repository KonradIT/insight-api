### Gets X number of images from InSight Mars Lander from NASA.gov

### Args:
### n = number of images starting from the current one backwards
### out = output directory

import argparse
import subprocess
import os
import signal
import time
import shutil

from insightmars import InSightAPI, utils

parser = argparse.ArgumentParser()
parser.add_argument('--fps', "-f", help='GIF speed', required=True)
parser.add_argument('--output', "-o", help='Output gif name', required=True)
parser.add_argument('--size', "-s", help='Output gif size (WxH)')
parser.add_argument('--camera', "-c", help='Camera: icc / idc', default="idc")
parser.add_argument('--sol', "-d", help='Sol (00 / 00 - 01)', default="all")
args = parser.parse_args()
InSightMission = InSightAPI(af=args.camera, per_page="400")
json_request = InSightMission.make_request()

images = []	
if args.sol == "all":
	images = InSightMission.get_all(json_request)
elif "-" in args.sol:
	start_sol = int(args.sol.split(" - ")[0])
	end_sol = int(args.sol.split(" - ")[1])
	images = InSightMission.get_sols(json_request, start_sol, end_sol)
else:
	images = InSightMission.get_sol(json_request, int(args.sol))

if os.path.exists("images"):
	shutil.rmtree("images")

utils.download_image(images, "images/", "sequential")
scale = ""
if not args.size == None:
	scale = "-vf scale=" + args.size
p = subprocess.Popen("ffmpeg -y -f image2 -framerate " + args.fps + " -i images/IMG_%d.png " + scale + " " + args.output, shell=True)
out, err = p.communicate()


