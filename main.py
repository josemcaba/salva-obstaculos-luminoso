def giroAleatorio():
    if Math.random_boolean():
        maqueen.motor_stop(maqueen.Motors.M1)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    else:
        maqueen.motor_stop(maqueen.Motors.M2)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    basic.pause(randint(500, 2000))
def medirDistancia():
    global distancia
    distancia = maqueen.ultrasonic(PingUnit.CENTIMETERS)
    if distancia == 0:
        distancia = 400
    return distancia
distancia = 0
basic.pause(2000)
velocidad = 180
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)

def on_forever():
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, velocidad)
    if medirDistancia() < 20:
        giroAleatorio()
basic.forever(on_forever)

def on_in_background():
    while True:
        strip.show_color(neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        basic.show_icon(IconNames.HEART)
        basic.pause(100)
        basic.show_icon(IconNames.SMALL_HEART)
        basic.pause(100)
control.in_background(on_in_background)
