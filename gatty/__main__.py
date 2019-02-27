# coding=utf-8

import re
import sys

from prompt_toolkit import PromptSession
from google.assistant.library import Assistant

import gatty
import gatty.oauth
import gatty.goog

if gatty.oauth.check_for_credfiles() is not True:
	print("Please follow the Google Assistant SDK Tutorial before attempting to use this program.")
	print("ENSURE YOU HAVE BOTH CLIENT_SECRET_xxx.JSON AND CREDENTIALS.JSON")
	sys.exit(1)

special_exit = "exit - exits"

print("Welcome to gatty {}!!!".format(gatty.__version__))
print("The following commands are special:\n\t\t{}\n\t\t".format(special_exit))

gatty.goog.probe_google()

session = PromptSession(message="Say something: ")

with Assistant(gatty.oauth.produce_credentials(), gatty.oauth.api_ids()[1]) as google:
	something = ""
	
	while re.fullmatch("^exit$", something, re.M | re.I) is None:
		something = session.prompt()
		response = google.send_text_query(something)

sys.exit(0)
