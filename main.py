mouvement = 0
gaz = 0
steam = 0
humidite = 0
temperature = 0
bluetooth.start_uart_service()

def on_forever():
    global temperature, humidite, steam, gaz, mouvement
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P5, True, False, True)
    temperature = dht11_dht22.read_data(dataType.TEMPERATURE)
    humidite = dht11_dht22.read_data(dataType.HUMIDITY)
    steam = pins.analog_read_pin(AnalogReadWritePin.P0)
    gaz = pins.digital_read_pin(DigitalPin.P1)
    mouvement = pins.digital_read_pin(DigitalPin.P15)
    basic.pause(5000)
    bluetooth.uart_write_line("" + str(temperature) + ";" + str(humidite) + ";" + str(mouvement) + ";" + str(steam) + ";" + str(gaz))
    basic.pause(5000)
basic.forever(on_forever)
