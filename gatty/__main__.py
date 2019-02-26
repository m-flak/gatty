# coding=utf-8

import sys
import gatty
import gatty.oauth

if gatty.oauth.check_for_credfiles() is not True:
	print("Please follow the Google Assistant SDK Tutorial before attempting to use this program.")
	print("ENSURE YOU HAVE BOTH CLIENT_SECRET_xxx.JSON AND CREDENTIALS.JSON")
	sys.exit(1)

print("Welcome to gatty {}!!!".format(gatty.__version__))

