
import os, time

sets = 12
reps = 12
interval = 8 #seconds 

os.system("espeak 'Starting in 7 seconds ... Will be doing {} sets'". format(sets))
for s in range(7):
	os.system("espeak '{}'".format(s+1))
	time.sleep(1)

for i in range(sets):
	st = "espeak 'Set {} . '".format(i+1)
	print st
	os.system(st)

	
	for r in range(reps):
		os.system("espeak '{}'".format(r+1))
		time.sleep(interval)

	os.system("espeak 'Completed {}, remaining {}'". format(i+1, sets-(i+1)))
	time.sleep(interval-5)
	if (i == sets-1):
		os.system("espeak 'Complete, you'll rock today! '")
		break
	os.system("espeak 'READY'")


