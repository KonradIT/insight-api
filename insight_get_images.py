### Gets X number of images from InSight Mars Lander from NASA.gov

### Args:
### n = number of images starting from the current one backwards
### out = output directory

import argparse

from insightmars import InSightAPI, utils
InSightMission = InSightAPI(per_page="400")

parser = argparse.ArgumentParser()
parser.add_argument("--number", "-n",type=int, help='Number of images to download', required=True)
parser.add_argument('--output', "-o", help='Output directory', required=True)
parser.add_argument('--sort', "-s", help='Sort by: sol / sequential', type=str)
args = parser.parse_args()

json_request = InSightMission.make_request()
all_images = InSightMission.get_count(json_request)
print("InSight Photo Downloader")
print("Number of images available: %d" % all_images)
print("Number of images to download: %d" % args.number)
images = InSightMission.get_images(json_request, args.number)
utils.download_image(images, args.output, args.sort)
