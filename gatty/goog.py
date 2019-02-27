# coding=utf-8

import subprocess

import gatty.oauth

# attempted fix for issue #314
def probe_google():
	our_ids = gatty.oauth.api_ids()
	gad_call = "google-assistant-demo --project-id {} --device-model-id {}".format(our_ids[0], our_ids[1])
	
	subprocess.Popen(gad_call, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	
	return

