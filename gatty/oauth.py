# coding=utf-8
import os
import pkg_resources

#you'll need to change this based on your personal, own oauth shiznit
CLIENT_ID = "713269907379-4crgrrvelpq9f44d3u4pmntkokr70h6k.apps.googleusercontent.com"

# you'll need the secret file and the credentials.json
def secret_file_name():
	global CLIENT_ID
	return "%s%s%s" % ("client_secret_", CLIENT_ID, ".json")

# this requires setup
# TODO: add the setup steps from the Assistant SDK tutorial into setup
# TODO: add setup :^)
def check_for_credfiles() -> bool:
	basedir = pkg_resources.resource_filename("gatty", ".")
	oadir = os.path.join(basedir, "data", "oauth")
	
	try:
		fd = os.open("%s/%s" % (oadir, secret_file_name()), os.O_RDONLY)
		os.close(fd)
		fd = os.open("%s/%s" % (oadir, "credentials.json"), os.O_RDONLY)
		os.close(fd)
	except OSError:
		return False
	
	return True
