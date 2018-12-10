## NASA InSight Mars Raw Image API

[![PyPI version](https://badge.fury.io/py/insight-api.svg)](https://badge.fury.io/py/insight-api)

![](/header.gif)

Python library to access the raw images and metadata from the InSight Mars mission

Images are from nasa.gov

### Args:

	InSightAPI(order="desc", per_page="100", af="idc")

- per_page = 25 / 50 / 100
- af (camera) = idc / icc
	- idc = Instrument Deployment Camera
	- icc = Instrument Context Camera

### Usage:

	from insightmars import InSightAPI, utils
	InSightMission = InSightAPI()
	
	# Make initial request
    json_request = InSightMission.make_request()
    
    # Get image count
	all_images = InSightMission.get_count(json_request)
	
	# Get x number of image urls (order backwards, from newest to oldest)
	images = InSightMission.get_images(json_request, x)
	
	# Get image metadata:
	metadata = InSightMission.get_metadata(json_request, image_id)
	
	# Get x number of images + meatadata (order backwards, from newest to oldest)
	metadata = InSightMission.get_images_metadata(json_request, x)
	
	# Get all images available:
	images = InSightMission.get_all(json_request)
	
	# Download images:
	utils.download_image(images, "images/", "sequential")
	
	# Get specific sol
	get_sol(data, sol)
	
	# Get sols
	get_sols(data, start_sol, end_sol)
	
### Examples:

- [insight_get_images.py](/insight_get_images.py)

- [insight_make_gif.py](/insight_get_images.py)

- [insight_latest_image.py](/insight_latest_image.py)

- [insight_make_gif_metadata.py](/insight_make_gif_metadata.py)

- [make_graph.py](/make_graph.py)
