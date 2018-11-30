from insightmars import InSightAPI, utils
import os
import time

#import twutils
import logging

InSightMission = InSightAPI()
json_request = InSightMission.make_request()

if not os.path.exists("images"):
	os.makedirs("images")
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
while True:
	time.sleep(5) #1800 = 30min
	if len(os.listdir('images')) == 0:
		logging.info("populating 1st img")
		utils.download_image(InSightMission.get_latest(json_request))
	current_imageid = InSightMission.get_images_metadata(json_request, 1)[0]["imageid"]
	if not os.listdir('images')[0].replace(".PNG", "") == current_imageid:
		logging.info("downloading new img + tweeting it.....")
		utils.download_image(InSightMission.get_latest(json_request))
		#tweet
		cmd = ["python","tweet.py",current_imageid + ".PNG"]
		subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
