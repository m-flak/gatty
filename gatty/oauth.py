# coding=utf-8
import os
import pkg_resources
import google.oauth2.credentials as goocred

#you'll need to change this based on your personal, own oauth shiznit
CLIENT_ID = "713269907379-4crgrrvelpq9f44d3u4pmntkokr70h6k.apps.googleusercontent.com"

#i'm sure this'll need to be different as well
PROJECT_ID = "gatty-aff42"
MODEL_ID = "gatty-aff42-laptop-eosr6x"
INSTANCE_ID = "Laptop"

# you'll need the secret file and the credentials.json
def secret_file_name():
	global CLIENT_ID
	return "%s%s%s" % ("client_secret_", CLIENT_ID, ".json")

def get_dirs() -> tuple:
	basedir = pkg_resources.resource_filename("gatty", ".")
	return basedir, os.path.join(basedir, "data", "oauth")

# this requires setup
# TODO: add the setup steps from the Assistant SDK tutorial into setup
# TODO: add setup :^)
def check_for_credfiles() -> bool:
	basedir, oadir = get_dirs()
	
	try:
		fd = os.open("%s/%s" % (oadir, secret_file_name()), os.O_RDONLY)
		os.close(fd)
		fd = os.open("%s/%s" % (oadir, "credentials.json"), os.O_RDONLY)
		os.close(fd)
	except OSError:
		return False
	
	return True

def api_ids() -> tuple:
	global PROJECT_ID
	global MODEL_ID
	global INSTANCE_ID
	return PROJECT_ID, MODEL_ID, INSTANCE_ID

def produce_credentials():
	json_creds = os.path.join(get_dirs()[1], "credentials.json")
	
	credentials = goocred.Credentials.from_authorized_user_file(json_creds)
	
	return credentials
