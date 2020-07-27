import os
import time
import click
import mac_say


# Setting Up Some Default Variables
name         = "unknown beauty"
time_left    = 60
phase1_time  = 5
phase2_time  = 5
passed_time  = 0 
session_time = 60

# As the "time" module uses seconds, we convert the user input given from minutes to seconds.
def input_to_minutes(user_input):
	user_input = round(user_input * 60)
	return user_input

# Some Custom print statements
def print_progress(split,total):

	percent = round((split/total)*100)
	print("")

	if percent == 100:
		print(f'████████████████████ {percent} %')

	elif percent >= 90:
		print(f'██████████████████-- {percent} %')

	elif percent >= 80:
		print(f'████████████████---- {percent} %')

	elif percent >= 70:
		print(f'██████████████------ {percent} %')

	elif percent >= 60:
		print(f'████████████-------- {percent} %')

	elif percent >= 50:
		print(f'██████████---------- {percent} %')

	elif percent >= 40:
		print(f'████████------------ {percent} %')

	elif percent >= 30:
		print(f'██████-------------- {percent} %')

	elif percent >= 20:
		print(f'████---------------- {percent} %')

	elif percent >= 10:
		print(f'██------------------ {percent} %')

	elif percent >=9:
		print(f'██------------------ {percent} %')

	elif percent <= 5:
		print(f'█------------------- {percent} %')

def print_status_bar():
	print_progress(passed_time,session_time)
	print("")

def print_motus():
	os.system('clear')
	print (" ""  ")
	print ("*   *")
	print ("  i  ")
	print (" ___/")
	print ("     ")


# Making Motus Talk Via Apples Text To Speak Engine
def say(utterance_section_1,utterance_section_2 = " ",utterance_section_3 = " "):

	full_utterance = str(utterance_section_1)+str(f' {utterance_section_2}')+str(f' {utterance_section_3}')
	print_motus()
	print(f'Motus: {full_utterance}')
	mac_say.say(full_utterance)

# Interaction 
def welcome():

	print_motus()
	say ("Bleep Bloop. Welcome.")
	menu()

def menu():

	print_motus()
	say ("What's the plan? ")
	print("(q) Quick Session ")
	print("(c) Custom Session ")
	print("(h) help ")
	print("(e) exit ")

	user_input = click.getchar()

	if user_input == 'c':
		say("Okay, let's do a custom session.")
		custom_session()

	elif user_input == 'q':
		say("Wonderful. Let's start learning!")
		run_session()

	elif user_input == 'h':
		help()

	elif user_input == 'e':
		say("ciao!")
		exit()

	else: 
		menu()

def setup_session_time(): 						

	say("How much time you got today for your session?")
	global session_time
	session_time = (input("Session time in Minutes: "))

	try:	
		session_time = input_to_minutes(float(session_time))
		say("Okay.")

	except ValueError:
		say("Please enter a Number, for example 5.")
		setup_session_time()

def setup_phase1():
	say("How long should your first phase be?")

	global phase1_time
	phase1_time = input ("Phase 1 in Minutes: ")

	try:	
		phase1_time = input_to_minutes(float(phase1_time))
		say("Cool.")

	except ValueError:
		say("Please enter a Number, for example 5.")
		setup_phase1()

def setup_phase2():
	say("And how long should the second phase be?")

	global phase2_time
	phase2_time = input ("Phase 2 in Minutes: ")

	try:	
		phase2_time = input_to_minutes(float(phase2_time))
		say("Okay.")
		say("I am ready like fresh cake in the oven.")

	except ValueError:
		say("Please enter a Number, for example 5.")
		setup_phase2()

	check_user_input()

def check_user_input(): 

	# Motus prints out the user input to check if all inputs are correct.

	say("Please check, if i understood you right!")
	print("")
	print(f'Total learning time: {(round(session_time/60))} min')
	print(f'Length of phase 1:   {(round(phase1_time/60))} min')
	print(f'Length of phase 2:   {(round(phase2_time/60))} min')
	print("\n Press any key to continue or press (t) to try again.")

	user_input = click.getchar()

	if user_input == 't':
		custom_session()

	else:
		return

	say("Groovy! Let's go!")

def run_session():

	global passed_time
	global time_left

	passed_time = 0

	while session_time > passed_time:

		say("Phase 1! Good Luck ! :) ")
		print_status_bar()

		time.sleep(phase1_time)

		passed_time += phase1_time
		time_left = float(session_time) - passed_time

		if float(session_time) > passed_time:

			say("Phase 2! Yalla")
			print_status_bar()
			time.sleep(phase2_time)
			passed_time += phase2_time
			time_left = float(session_time) - passed_time

	finish()

def custom_session():
	setup_session_time()
	setup_phase1()
	setup_phase2()
	run_session()

def help():

	say ("Oops. Sorry for being rude.")
	say ("I forgot you are new here.")
	say ("Let me introduce myself.")
	say ("I am Motus, a super-smart super-computer \n hyper-learning giga-assistant.")
	say("What's YOUR name?")

	global name
	
	name = input("Enter your Name or press RETURN to start. ")
	if name == "":
		name = "Unknown Beauty"

	say("Hello",name,"! :)")
	say("So, my job is to help you stay motivated while learning. Just tell me how your learning rhythm works - and i will help you, stiking to your plans.")
	say("That's how it works:")
	say("You can use standard or custom sessions.")
	say("Standard sessions are sessions of 60 minutes with two different phases.")
	say("Let's say you want to learn some flash cards.")
	say("In the first phase, you write your cards.")
	say("Then you switch to the second phase, where you try to learn and remember the cards.")
	say("Each phase is 5 minutes long, and i will remind you when to switch between them.")
	say("clever, isn't it?")
	say("And if you prefere a different rhythm, you should try setting up your own personal custom session. ")
	say("By the way: You can also use one of the phases to relax.")
	say("Well, i guess that's it.")
	say("Now, let's start learning!")
	
	menu()

def finish():
	say("Good Work! :) that's it for today. Have a nice day! ")


# Finally, we run Motus. 

welcome()


