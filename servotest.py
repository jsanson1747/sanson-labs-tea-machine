from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import time
kit = ServoKit(channels=16)

##############################################

# Continuous Servos

LEFT_LIMIT_SWITCH_PIN = 16  # BCM pin 16
RIGHT_LIMIT_SWITCH_PIN = 20  # BCM pin 20

GPIO.setmode(GPIO.BCM)
# Configure as input with internal pull-up resistor
GPIO.setup(LEFT_LIMIT_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_LIMIT_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

kit.continuous_servo[0].throttle = -1
kit.continuous_servo[1].throttle = -1

try:
    while True:
        isLeftHomed = False
        isRightHomed = False
        time.sleep(1)
        
        if GPIO.input(LEFT_LIMIT_SWITCH_PIN) == GPIO.LOW:
            print("Left Limit switch pressed!")
            kit.continuous_servo[0].throttle = None
            kit.continuous_servo[1].throttle = None
            isLeftHomed = True
            
        if GPIO.input(RIGHT_LIMIT_SWITCH_PIN) == GPIO.LOW:
            print("Right limit switch pressed!")
            kit.continuous_servo[0].throttle = None
            kit.continuous_servo[1].throttle = None
            isRightHomed = True
        if isLeftHomed and isRightHomed:
            break
except KeyboardInterrupt:
    kit.continuous_servo[0].throttle = None
    kit.continuous_servo[1].throttle = None
    GPIO.cleanup()

##############################################

# Regular Servo (Dumper Mechanism)

# kit.servo[2].angle = 180

# time.sleep(1)

# kit.servo[2].angle = 0

# time.sleep(1)

# kit.servo[2].angle = 180

##############################################