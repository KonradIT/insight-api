from insightmars import InSightAPI, utils

InSightMission = InSightAPI()
json_request = InSightMission.make_request()
utils.download_image(InSightMission.get_latest(json_request))
