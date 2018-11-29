### Gets X number of images from InSight Mars Lander from NASA.gov

### Args:
### n = number of images starting from the current one backwards
### out = output directory

import argparse
import subprocess

from insightmars import InSightAPI, utils

parser = argparse.ArgumentParser()
parser.add_argument('--fps', "-f", help='GIF speed', required=True)
parser.add_argument('--output', "-o", help='Output gif name', required=True)
parser.add_argument('--size', "-s", help='Output gif size (WxH)')
parser.add_argument('--camera', "-c", help='Camera: icc / idc', default="idc")
args = parser.parse_args()
InSightMission = InSightAPI(af=args.camera)
json_request = InSightMission.make_request()
images = InSightMission.get_all(json_request)
utils.download_image(images, "images/", "sequential")
scale = ""
if not args.size == None:
	scale = "-vf scale=" + args.size
subprocess.Popen("ffmpeg -y -f image2 -framerate " + args.fps + " -i images/IMG_%d.png " + scale + " " + args.output, shell=True)
