# Python code
#
PIN_ECHO = DigitalPin.P0
PIN_TRIG = DigitalPin.P1
PIN_SOIL = AnalogPin.P2
PIN_PUMP = DigitalPin.P8

LOW_WATER_CM = 15  # farther than this = "not enough water"


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


# ---------------- Ultrasonic sensor ----------------
def wait_us(duration):
    t0 = input.running_time_micros()
    while input.running_time_micros() - t0 < duration:
        pass


def measure_once_cm():
    # 10 us trigger pulse, then time the echo. Returns -1 if no echo.
    pins.digital_write_pin(PIN_TRIG, 0)
    wait_us(4)
    pins.digital_write_pin(PIN_TRIG, 1)
    wait_us(12)
    pins.digital_write_pin(PIN_TRIG, 0)
    us = pins.pulse_in(PIN_ECHO, PulseValue.HIGH)
    if us <= 0:
        return -1
    return us / 58


# ---------------- Main loop ----------------
def on_forever():
    raw = soil_raw()
    basic.show_number(Math.round(raw))

    # cm = measure_once_cm()
    # basic.show_number(Math.round(cm))

    if raw <= 50:
        pump_start()
    else:
        pump_stop()


# Safe start-up state: pump off
pump_stop()
basic.forever(on_forever)
