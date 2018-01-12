#!/usr/bin/env python

try:
	import coinbase
except ImportError:
	exit("Please install coinbase package")

import configparser
config = configparser.ConfigParser()
config.read('config.ini')