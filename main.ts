let mouvement = 0
let gaz = 0
let steam = 0
let humidite = 0
let temperature = 0
bluetooth.startUartService()
basic.forever(function () {
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P5,
    true,
    false,
    true
    )
    temperature = dht11_dht22.readData(dataType.temperature)
    humidite = dht11_dht22.readData(dataType.humidity)
    steam = pins.analogReadPin(AnalogReadWritePin.P0)
    gaz = pins.digitalReadPin(DigitalPin.P1)
    mouvement = pins.digitalReadPin(DigitalPin.P15)
    basic.pause(5000)
    bluetooth.uartWriteLine("" + temperature + ";" + humidite + ";" + mouvement + ";" + steam + ";" + gaz)
    basic.pause(5000)
})
