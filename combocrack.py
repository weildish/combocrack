#DECLARING GLOBAL VARIABLES SO THEY CAN BE USED IN THE SUCCESS FUNCTION
global to_address
global from_address
global smtp_server
global smtp_user
global smtp_pass
global first
global last
#EDIT THESE VARIABLES TO SUIT YOUR NEEDS
to_address = "youremail@email.com" #The email address to which you want the safe combination sent
from_address = "fromemail@email.com" #The email address from which you're sending
smtp_server = "smtp.email.com" #The SMTP server you're using-- if you have an account at Gmail, you will probably be able to send using that server and account
smtp_user = "username" #Your SMTP account username
smtp_pass = "Pass1234" #Your SMTP account password
start = 10000 #The beginning of the range of combinations you want to try. Currently only supports between 10000 and 99999
end = 19999 #The end of the range of combinations you want to try. Currently only supports between 10001 and 99999
#######FUNCTIONS#######
def check_combo():
	global combo
	success = False
	attempt = 0
	while (success == False):
		if attempt == 3:
			print "Three attempts made. Rebooting safe PCB..."
			GPIO.output(8, 0)
			time.sleep(5)
			GPIO.output(8, 1)
			print "Reboot complete. Continuing crack."
			attempt = 0
		combo = str(random.randint(first,last))
		with open("combolist.db") as database:
			found = False
			for line in database:
				if re.search(format(combo),line):
					#COMBO TRIED
					print combo+" has already been attempted. Moving on to another combination."
					found = True
			if not found: #Could have shortened this section by using classes. Too late now.
				print "Attempting combination "+combo
				#DEFINE EACH DIGIT OF COMBINATION
				c0 = str(combo)[0]
				c1 = str(combo)[1]
				c2 = str(combo)[2]
				c3 = str(combo)[3]
				c4 = str(combo)[4]
				#FIRST DIGIT ATTEMPT
				print "Attempting first digit: "+c0
				if c0 == "1":
					GPIO.output(2, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(2, 0)
					GPIO.output(24, 0)
				if c0 == "2":
					GPIO.output(3, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(3, 0)
					GPIO.output(10, 0)
				if c0 == "3":
					GPIO.output(4, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(4, 0)
					GPIO.output(9, 0)
				if c0 == "4":
					GPIO.output(14, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(14, 0)
					GPIO.output(24, 0)
				if c0 == "5":
					GPIO.output(15, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(15, 0)
					GPIO.output(10, 0)
				if c0 == "6":
					GPIO.output(18, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(18, 0)
					GPIO.output(9, 0)
				if c0 == "7":
					GPIO.output(17, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(17, 0)
					GPIO.output(24, 0)
				if c0 == "8":
					GPIO.output(27, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(27, 0)
					GPIO.output(10, 0)
				if c0 == "9":
					GPIO.output(22, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(22, 0)
					GPIO.output(9, 0)
				if c0 == "0":
					GPIO.output(23, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(23, 0)
					GPIO.output(10, 0)
				time.sleep(.381)
				#SECOND DIGIT ATTEMPT
				print "Attempting second digit: "+c1
				if c1 == "1":
					GPIO.output(2, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(2, 0)
					GPIO.output(24, 0)
				if c1 == "2":
					GPIO.output(3, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(3, 0)
					GPIO.output(10, 0)
				if c1 == "3":
					GPIO.output(4, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(4, 0)
					GPIO.output(9, 0)
				if c1 == "4":
					GPIO.output(14, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(14, 0)
					GPIO.output(24, 0)
				if c1 == "5":
					GPIO.output(15, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(15, 0)
					GPIO.output(10, 0)
				if c1 == "6":
					GPIO.output(18, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(18, 0)
					GPIO.output(9, 0)
				if c1 == "7":
					GPIO.output(17, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(17, 0)
					GPIO.output(24, 0)
				if c1 == "8":
					GPIO.output(27, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(27, 0)
					GPIO.output(10, 0)
				if c1 == "9":
					GPIO.output(22, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(22, 0)
					GPIO.output(9, 0)
				if c1 == "0":
					GPIO.output(23, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(23, 0)
					GPIO.output(10, 0)
				time.sleep(.381)
				#THIRD DIGIT ATTEMPT
				print "Attempting third digit: "+c2
				if c2 == "1":
					GPIO.output(2, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(2, 0)
					GPIO.output(24, 0)
				if c2 == "2":
					GPIO.output(3, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(3, 0)
					GPIO.output(10, 0)
				if c2 == "3":
					GPIO.output(4, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(4, 0)
					GPIO.output(9, 0)
				if c2 == "4":
					GPIO.output(14, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(14, 0)
					GPIO.output(24, 0)
				if c2 == "5":
					GPIO.output(15, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(15, 0)
					GPIO.output(10, 0)
				if c2 == "6":
					GPIO.output(18, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(18, 0)
					GPIO.output(9, 0)
				if c2 == "7":
					GPIO.output(17, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(17, 0)
					GPIO.output(24, 0)
				if c2 == "8":
					GPIO.output(27, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(27, 0)
					GPIO.output(10, 0)
				if c2 == "9":
					GPIO.output(22, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(22, 0)
					GPIO.output(9, 0)
				if c2 == "0":
					GPIO.output(23, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(23, 0)
					GPIO.output(10, 0)
				time.sleep(.381)
				#FOURTH DIGIT ATTEMPT
				print "Attempting fourth digit: "+c3
				if c3 == "1":
					GPIO.output(2, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(2, 0)
					GPIO.output(24, 0)
				if c3 == "2":
					GPIO.output(3, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(3, 0)
					GPIO.output(10, 0)
				if c3 == "3":
					GPIO.output(4, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(4, 0)
					GPIO.output(9, 0)
				if c3 == "4":
					GPIO.output(14, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(14, 0)
					GPIO.output(24, 0)
				if c3 == "5":
					GPIO.output(15, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(15, 0)
					GPIO.output(10, 0)
				if c3 == "6":
					GPIO.output(18, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(18, 0)
					GPIO.output(9, 0)
				if c3 == "7":
					GPIO.output(17, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(17, 0)
					GPIO.output(24, 0)
				if c3 == "8":
					GPIO.output(27, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(27, 0)
					GPIO.output(10, 0)
				if c3 == "9":
					GPIO.output(22, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(22, 0)
					GPIO.output(9, 0)
				if c3 == "0":
					GPIO.output(23, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(23, 0)
					GPIO.output(10, 0)
				time.sleep(.381)
				#FIFTH DIGIT ATTEMPT
				print "Attempting fifth digit: "+c4
				if c4 == "1":
					GPIO.output(2, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(2, 0)
					GPIO.output(24, 0)
				if c4 == "2":
					GPIO.output(3, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(3, 0)
					GPIO.output(10, 0)
				if c4 == "3":
					GPIO.output(4, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(4, 0)
					GPIO.output(9, 0)
				if c4 == "4":
					GPIO.output(14, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(14, 0)
					GPIO.output(24, 0)
				if c4 == "5":
					GPIO.output(15, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(15, 0)
					GPIO.output(10, 0)
				if c4 == "6":
					GPIO.output(18, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(18, 0)
					GPIO.output(9, 0)
				if c4 == "7":
					GPIO.output(17, 1)
					GPIO.output(24, 1)
					time.sleep(.38)
					GPIO.output(17, 0)
					GPIO.output(24, 0)
				if c4 == "8":
					GPIO.output(27, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(27, 0)
					GPIO.output(10, 0)
				if c4 == "9":
					GPIO.output(22, 1)
					GPIO.output(9, 1)
					time.sleep(.38)
					GPIO.output(22, 0)
					GPIO.output(9, 0)
				if c4 == "0":
					GPIO.output(23, 1)
					GPIO.output(10, 1)
					time.sleep(.38)
					GPIO.output(23, 0)
					GPIO.output(10, 0)
				time.sleep(1.85)
				#CHECK FOR SUCCESS
				with open("combolist.db", "a") as database:
					database.write(combo+"\n")
				print "Checking safe response for successful attempt..."
				time.sleep(.1)
				if GPIO.input(7):
					success = True
					global successcombo
					successcombo = combo
					success_combo()
				else:
					attempt +=1
					print "Sorry. That was not the correct combination. Trying again..."
def success_combo():
	GPIO.cleanup()
	print "Success! Combination has been found!"
	print "Combination is "+combo
	print "Now attempting to email you..."
	import smtplib
	from email.mime.text import MIMEText
	msg = MIMEText("Safe combination has been found! The combination is "+combo+".<br><br>This has been graciously provided by Jordan Spencer Cunningham at <a href='http://nerdology.org'>nerdology.org</a>.<br><br>Sincerely,<br>combocrack.py")
	msg['Subject'] = "Safe Combination Found!"
	msg['From'] = from_address
	msg['To'] = to_address
	send = smtplib.SMTP(smtp_server)
	send.login(smtp_user, smtp_pass)
	send.sendmail(from_address, to_address, msg.as_string())
	send.quit()
	print "Email successfully sent. Congratulations! Your safe is unlocked!"
#######REGULAR OPERATIONS#######
raw_input("Please press enter when you're ready for me to begin.")
import time
import random
import re
import RPi.GPIO as GPIO
#DEFINE GPIO PINS
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT, initial=0) #1 destination
GPIO.setup(3, GPIO.OUT, initial=0) #2 destination     } 1,2,3 all share the same ground-- combine?
GPIO.setup(4, GPIO.OUT, initial=0) #3 destination
GPIO.setup(14, GPIO.OUT, initial=0) #4 destination
GPIO.setup(15, GPIO.OUT, initial=0) #5 destination
GPIO.setup(18, GPIO.OUT, initial=0) #6 destination
GPIO.setup(17, GPIO.OUT, initial=0) #7 destination
GPIO.setup(27, GPIO.OUT, initial=0) #8 destination
GPIO.setup(22, GPIO.OUT, initial=0) #9 destination
GPIO.setup(23, GPIO.OUT, initial=0) #0 destination
#GPIO setup for sources
GPIO.setup(24, GPIO.OUT, initial=0) #1,4,7 source
GPIO.setup(10, GPIO.OUT, initial=0) #2,5,8,0 source
GPIO.setup(9, GPIO.OUT, initial=0) #3,6,9 source
GPIO.setup(8, GPIO.OUT, initial=1) #POWER FOR MAIN BOARD
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #TEST IF SAFE IS UNLOCKED
check_combo()