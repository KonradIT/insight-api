### Gets X number of images from InSight Mars Lander from NASA.gov

### Args:
### n = number of images starting from the current one backwards
### out = output directory

import argparse

from InSight import InSightAPI

InSightMission = InSightAPI()

parser = argparse.ArgumentParser()
parser.add_argument("--number", "-n",type=int)
parser.add_argument('--output', "-o")
args = parser.parse_args()

json_request = InSightMission.make_request()
all_images = InSightMission.get_count(json_request)
print(all_images)
print(args.number)
images = InSightMission.get_images(json_request, args.number)
InSightMission.download_image(images, args.output)
