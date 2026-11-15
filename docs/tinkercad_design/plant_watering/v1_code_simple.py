# Python code
#
PIN_ECHO = DigitalPin.P0
PIN_TRIG = DigitalPin.P1
PIN_SOIL = AnalogPin.P2
PIN_PUMP = DigitalPin.P8


# ---------------- Pump ----------------
def pump_start():
    pins.digital_write_pin(PIN_PUMP, 1)


def pump_stop():
    pins.digital_write_pin(PIN_PUMP, 0)


# ---------------- Soil sensor ----------------
def soil_raw():
    total = 0
    for i in range(10):
        total += pins.analog_read_pin(PIN_SOIL)
        basic.pause(5)
    return total / 10


# ---------------- Main loop ----------------
def on_forever():
    raw = soil_raw()
    basic.show_number(Math.round(raw))

    if raw <= 50:
        pump_start()
    else:
        pump_stop()


# Safe start-up state: pump off
pump_stop()
basic.forever(on_forever)
