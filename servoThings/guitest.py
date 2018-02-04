#!/usr/bin/python

from Tkinter import *
from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
# pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096


def setServoPulse(channel, pulse):
    # initializes the frequencies and currents for the servo
    pulseLength = 1000000                   # 1,000,000 us per second
    pulseLength /= 60                       # 60 Hz
    print "%d us per period" % pulseLength
    pulseLength /= 4096                     # 12 bits of resolution
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)


pwm.setPWMFreq(60)  # Set frequency to 60 Hz


def moveServos():
    # Change speed of continuous servo on channel O
    pwm.setPWM(0, 0, servoMin)
    pwm.setPWM(2, 0, servoMin)
    time.sleep(1)
    pwm.setPWM(0, 0, 375)
    pwm.setPWM(2, 0, 375)
    time.sleep(1)
    pwm.setPWM(0, 0, servoMax)
    pwm.setPWM(2, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(0, 0, servoMin)
    pwm.setPWM(2, 0, servoMin)
    time.sleep(1)


root = Tk()
root.wm_title("Window Title")
root.config(background="#FFFFFF")

usedFrame = Frame(root, width=800, height=600)
usedFrame.grid(row=0, column=0, padx=10, pady=2)


def hello():
    moveServos()


buttonMove1 = Button(usedFrame, text="Routine 1", command=hello)
buttonMove1.grid(row=0, column=0, padx=10, pady=2)

root.mainloop()
