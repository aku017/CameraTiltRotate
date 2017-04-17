from tkinter import *
import RPi.GPIO as GPIO
import time
import picamera

root = Tk()
root.wm_title("Camera Control")

    
def horizMotorLeft():
    GPIO.setmode(GPIO.BOARD)
    pin_number = 11
    GPIO.setup(pin_number, GPIO.OUT)
    freq_hertz = 50
    pwm = GPIO.PWM(pin_number, freq_hertz)
    ms_per_cycle = 1000 / freq_hertz
    positionValue = 1
    #for i in range(1):
    #    positionValueF = positionValue
    duty_cycle_percentage = positionValue * 100 / ms_per_cycle
    #positionValueF -= .1
    pwm.start(duty_cycle_percentage)
    time.sleep(.1)
    pwm.stop()
    GPIO.cleanup()

def horizMotorRight():
    GPIO.setmode(GPIO.BOARD)
    pin_number = 11
    GPIO.setup(pin_number, GPIO.OUT)
    freq_hertz = 50
    pwm = GPIO.PWM(pin_number, freq_hertz)
    ms_per_cycle = 1000 / freq_hertz
    positionValue = 2
    duty_cycle_percentage = positionValue * 100 / ms_per_cycle
    pwm.start(duty_cycle_percentage)
    time.sleep(.1)
    pwm.stop()
    GPIO.cleanup()

def vertMotorUp():
    GPIO.setmode(GPIO.BOARD)
    pin_number = 7
    GPIO.setup(pin_number, GPIO.OUT)
    freq_hertz = 50
    pwm = GPIO.PWM(pin_number, freq_hertz)
    ms_per_cycle = 1000 / freq_hertz
    positionValue = 1
    #for i in range(1):
    #    positionValueF = positionValue
    duty_cycle_percentage = positionValue * 100 / ms_per_cycle
    #positionValueF -= .1
    pwm.start(duty_cycle_percentage)
    time.sleep(.1)
    pwm.stop()
    GPIO.cleanup()

def vertMotorDown():
    GPIO.setmode(GPIO.BOARD)
    pin_number = 7
    GPIO.setup(pin_number, GPIO.OUT)
    freq_hertz = 50
    pwm = GPIO.PWM(pin_number, freq_hertz)
    ms_per_cycle = 1000 / freq_hertz
    positionValue = 2
    duty_cycle_percentage = positionValue * 100 / ms_per_cycle
    pwm.start(duty_cycle_percentage)
    time.sleep(.1)
    pwm.stop()
    GPIO.cleanup()
    
def motorReset():
    GPIO.setmode(GPIO.BOARD)
    pin_number1 = 11
    pin_number2 = 7
    GPIO.setup(pin_number1, GPIO.OUT)
    GPIO.setup(pin_number2, GPIO.OUT)
    freq_hertz = 50
    pwm1 = GPIO.PWM(pin_number1, freq_hertz)
    pwm2 = GPIO.PWM(pin_number2, freq_hertz)
    ms_per_cycle = 1000 / freq_hertz
    positionValue = 1.5
    duty_cycle_percentage = positionValue * 100 / ms_per_cycle
    pwm1.start(duty_cycle_percentage)
    pwm2.start(duty_cycle_percentage)
    time.sleep(.1)
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

def cameraPreview():
    camera = picamera.PiCamera()
    camera.start_preview()
    time.sleep(20)
    camera.stop_preview()
    camera.close()

def cameraOff():
    camera = picamera.PiCamera()
    camera.stop_preview()
    camera.close()

leftFrame = Frame(root, width=800, height=1200)
leftFrame.grid(row=0, column=0, padx=4, pady=8)

Label(leftFrame, text="Camera Control").grid(row=0, column=0, padx=0, pady=0)

#Camera Control Buttons
prompt = Label(root, text="", anchor="w")
prompt.grid(row=0, column=0)

left = Button(leftFrame, text="<", width=10, command = horizMotorLeft)
left.grid(row=2, column=0)

right = Button(leftFrame, text=">", width=10, command = horizMotorRight)
right.grid(row=2, column=2)

up = Button(leftFrame, text="^", width=10, command = vertMotorUp)
up.grid(row=1, column=1)

down = Button(leftFrame, text="v", width=10, command = vertMotorDown)
down.grid(row=3, column=1)

reset = Button(leftFrame, text="Reset", width=10, command = motorReset)
reset.grid(row=2, column=1)

#Camera Video Feed Buttons
camera_label = Label(leftFrame, text="Camera Video", anchor="w")
camera_label.grid(row=4,column=0)

camera_off = Button(leftFrame, text="Stop", width=10, command = cameraOff)
camera_off.grid(row=5,column=1)

camera_record = Button(leftFrame, text="Record", width=10)
camera_record.grid(row=5, column=2)

entry = Entry(leftFrame, width=10)
entry.grid(row=6, column=1)

entry_label = Label(leftFrame, text="Preview Time")#Does not work right now
entry_label.grid(row=6, column=0)

camera_preview = Button(leftFrame, text="Start Preview", width=10, command = cameraPreview)
camera_preview.grid(row=6,column=2)
        
root.mainloop() #start monitoring and updating the GUI
