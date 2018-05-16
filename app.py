import BlynkLib
import time
import gpiozero as gpio

ledP = gpio.LED(20)

BLYNK_AUTH = '27b431bedee74135811a8063d96dc6fc' #PROJECT
BLYNK_AUTH_APP = '89d6bf2ffc7146d18079ff5e16b180ef' #APP

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

lat = None
lon = None
steps = 0
Value_display = "Nothing"


@blynk.VIRTUAL_READ(10)
def v10_read_handler():
    global Value_display
    blynk.virtual_write(10, Value_display)

@blynk.VIRTUAL_WRITE(11)
def my_write_handler(value):
    global lat,lon,steps, Value_display
    if steps == 0:
        lat = value
        steps = steps + 1
    elif steps == 1:
        lon = value
        steps = steps + 1
    elif steps == 2:
        steps = steps + 1
    elif steps == 3:
        steps = 0
        latlon = (lat, lon)
        print(latlon)
    elif steps == 4:
        steps = 0
        latlon = (lat, lon)
        print(latlon)
        Value_display = 'String 2'
        blynk.sync_all()
        v10_read_handler()
            
    
@blynk.VIRTUAL_WRITE(20)
def my_write_handlers(value):
    print('Current button value: {}'.format(value))
    print(value)
    if value == "1":
        ledP.on()
        #blynk.notify('You pressed the button and I know it')
    else:
        ledP.off()

    
@blynk.VIRTUAL_READ(21)
def v21_read_handler():
    # Display a Gauge
    import random
    rannum = random.randint(1,20)*5
    print(rannum)
    blynk.virtual_write(21, rannum)

    

blynk.run()
