from time import sleep
import pyautogui as p

x = 0

sleep(3)

p.typewrite("2\n")
sleep(0.5)
p.typewrite("001\n")
sleep(0.5)
p.typewrite("002\n")
sleep(0.5)

while x < 7:
	sleep(0.1)

	p.typewrite("001\n")
	sleep(1)
	p.typewrite("12.7245\n")
	sleep(1)
	p.typewrite("y\n")
	sleep(1)
	p.typewrite("001\n")
	sleep(1)
	p.typewrite("12.7245\n")
	sleep(1)
	p.typewrite("y\n")
	sleep(1)
	p.typewrite("002\n")
	sleep(1)
	p.typewrite("13.48721\n")
	sleep(1)
	p.typewrite("y\n")
	sleep(1)
	p.typewrite("002\n")
	sleep(1)
	p.typewrite("13.48721\n")
	sleep(1)
	p.typewrite("n\n")
	sleep(1)

	x += 1