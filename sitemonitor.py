from bs4 import BeautifulSoup

import requests

import time

import difflib

url = raw_input("Enter website to monitor: ")

t = int(raw_input("Wait time: "))

while True:
	r1  = requests.get(url)
	data1 = r1.text
	soup1 = BeautifulSoup(data1, "html.parser")
	r1.cookies['example_cookie_name']

	time.sleep(t)

	r2  = requests.get(url)
	data2 = r2.text
	soup2 = BeautifulSoup(data2, "html.parser")
	r2.cookies['example_cookie_name']

	if soup1 == soup2:
		print("No change")
	else:
		l1 = str(soup1).split(' ')
		l2 = str(soup2).split(' ')
		d = difflib.Differ();
		dif = list(d.compare(l1, l2));
		print("Change!")
