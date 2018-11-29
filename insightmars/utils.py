## Util library

import os
import requests

### download_image(self, array, out="images")
### array = array of urils
### out = directory for storing images
def download_image(array, out="images", order=None):
	if out.endswith("/"):
		out = out[:-1]
	if not os.path.exists(out):
		os.makedirs(out)
	for index, image in enumerate(array):
		print("Downloading %s" % image)
		r = requests.get(image, allow_redirects=True)
		if order == "sequential":
			filename = "IMG_" + str(index) + ".png"
		elif order == "sol":
			filename = "SOL_" + image.split("sol/")[1].split("/")[0] + ".png"
		else:
			filename = image.rsplit('/', 1)[1]
		open(out + "/" + filename, "wb").write(r.content)
