
import os, time

sets = 12
reps = 12
interval = 10 #seconds 

def type(exercise, seconds):
	os.system("espeak 'Starting in {} seconds ...' ". format(interval))
	for s in range(interval):
		os.system("espeak '{}'".format(s+1))
		time.sleep(1)

	os.system("espeak 'Do {} for {} seconds' ". format(exercise, seconds))
	time.sleep(seconds)


if __name__ == '__main__' :
	
	type('plank', 120)
	type('push-ups', 60)
	type('abs-and-thighs', 60)
	type('on-your-back-abs', 60)
	type('triangle-abs', 60)	
	type('Squats', 60)
	type('plank', 120)
