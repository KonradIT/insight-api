## Util library

import os
import requests
import logging
### download_image(self, array, out="images")
### array = array of urils
### out = directory for storing images
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
def download_image(array, out="images", order=None):
	if order == "sequential":
		array.reverse()
	if out.endswith("/"):
		out = out[:-1]
	if not os.path.exists(out):
		os.makedirs(out)
	for index, image in enumerate(array):
		logging.info("Downloading %s" % image)
		r = requests.get(image, allow_redirects=True)
		if order == "sequential":
			filename = "IMG_" + str(index) + ".png"
		elif order == "sol":
			filename = "SOL_" + image.split("sol/")[1].split("/")[0] + ".png"
		else:
			filename = image.rsplit('/', 1)[1]
		open(out + "/" + filename, "wb").write(r.content)
