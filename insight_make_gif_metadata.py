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
parser.add_argument('--textsize', "-t", help='Text size: default 40', default="40")
args = parser.parse_args()
InSightMission = InSightAPI(af=args.camera, per_page="400")
json_request = InSightMission.make_request()
metadata_images = InSightMission.get_images_metadata(json_request, InSightMission.get_count(json_request))
images = []
metadata = []
filenames = []
for index, image in enumerate(metadata_images):
	images.append(image["url"])
	metadata.append(image["title"])
	filenames.append("images/IMG_" + str(index) + ".png")

metadata.reverse()
if os.path.exists("images"):
	shutil.rmtree("images")
utils.download_image(images, "images/", order="sequential")
for index, i in enumerate(filenames):
	cmd = ["convert",i,"-pointsize",args.textsize,"-fill","white","-undercolor","'#00000080'","-gravity","South","-annotate","+0+5",metadata[index],i]	
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
          
scale = ""
if not args.size == None:
	scale = "-vf scale=" + args.size
p = subprocess.Popen("ffmpeg -y -f image2 -framerate " + args.fps + " -i images/IMG_%d.png " + scale + " " + args.output, shell=True)
out, err = p.communicate()

#shutil.rmtree("images")
