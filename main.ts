function giroAleatorio () {
    if (Math.randomBoolean()) {
        maqueen.motorStop(maqueen.Motors.M1)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    } else {
        maqueen.motorStop(maqueen.Motors.M2)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    }
    basic.pause(randint(500, 2000))
}
function medirDistancia () {
    distancia = maqueen.Ultrasonic(PingUnit.Centimeters)
    if (distancia == 0) {
        distancia = 400
    }
    return distancia
}
let distancia = 0
basic.pause(2000)
let velocidad = 180
let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
basic.forever(function () {
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, velocidad)
    if (medirDistancia() < 25) {
        giroAleatorio()
    }
})
control.inBackground(function () {
    while (true) {
        strip.showColor(neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        basic.showIcon(IconNames.Heart)
        basic.pause(100)
        basic.showIcon(IconNames.SmallHeart)
        basic.pause(100)
    }
})
