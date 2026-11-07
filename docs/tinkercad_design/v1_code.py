# ====================================================================
#  One-plant automatic watering  -  BBC micro:bit V2  (Tinkercad Python)
# ====================================================================
#  Wiring (from schematics_v1.pdf)
#    P0  <- HC-SR04 ECHO          (digital input)
#    P1  -> HC-SR04 TRIG          (digital output)
#    P2  <- SEN0308 SIG           (analog input)
#    P8  -> 100 ohm -> MOSFET gate (10k pull-down) -> pump (low-side)
#
#  Behaviour
#    * Pump is OFF at power-up and stays off until the soil has been
#      confirmed dry on several readings in a row AND the reservoir
#      has enough water.
#    * Pump runs for a fixed time (PUMP_RUN_SECONDS ~ 500 ml) and is
#      cut early if the reservoir drops below the minimum level, if
#      the distance reading is invalid, or if A+B is pressed.
#    * After every run there is a cool-down so water can soak in
#      before the soil is judged again (prevents over-watering).
#
#  Buttons (handy for calibration)
#    A   = show raw soil reading        B   = show water distance (cm)
#    A+B = emergency stop of the pump
# ====================================================================

# ---------------- Pins ----------------
PIN_ECHO = DigitalPin.P0
PIN_TRIG = DigitalPin.P1
PIN_SOIL = AnalogPin.P2
PIN_PUMP = DigitalPin.P8

# ---------------- Settings (CALIBRATE THESE) ----------------
# Soil: read raw values with button A, once with the probe in air /
# bone-dry soil and once in a glass of water, then enter them here.
# The maths works whichever way round the numbers go.
SOIL_RAW_DRY = 800        # raw reading when completely dry   (placeholder)
SOIL_RAW_WET = 400        # raw reading when fully wet        (placeholder)
SOIL_DRY_PERCENT = 35     # at or below this % the plant needs water

# Reservoir: distance from sensor (top of tank) down to the water.
# Larger distance = less water. Fill the tank to the lowest level you
# still accept (one 500 ml dose + a little reserve), press B, and
# type the distance you see here.
LOW_WATER_CM = 15         # farther than this = "not enough water" (placeholder)

# Pump: time it with a measuring jug until it delivers ~500 ml.
PUMP_RUN_SECONDS = 30     # placeholder - set from your own test

# Timing
CHECK_INTERVAL_MS = 10000 # how often the soil is sampled
DRY_CONFIRM_COUNT = 3     # consecutive dry readings needed to start
TANK_CHECK_MS = 2000      # tank re-check interval while pumping
COOLDOWN_MIN = 30         # minimum wait after a run before the next one

# ---------------- State ----------------
dry_count = 0
next_allowed_ms = 0
abort_requested = False


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
        basic.pause(10)
    return total / 10


def soil_percent(raw):
    pct = (raw - SOIL_RAW_DRY) * 100 / (SOIL_RAW_WET - SOIL_RAW_DRY)
    return max(0, min(100, pct))


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
    us = pins.pulse_in(PIN_ECHO, PulseValue.HIGH, 25000)   # 25 ms ~ 4 m
    if us <= 0:
        return -1
    return us / 58


def distance_cm():
    # Median of 5 readings; -1 if fewer than 3 were valid.
    readings = []
    for i in range(5):
        d = measure_once_cm()
        if d > 0:
            readings.append(d)
        basic.pause(60)
    n = len(readings)
    if n < 3:
        return -1
    for i in range(n):                      # tiny insertion-style sort
        for j in range(n - 1 - i):
            if readings[j] > readings[j + 1]:
                tmp = readings[j]
                readings[j] = readings[j + 1]
                readings[j + 1] = tmp
    return readings[Math.idiv(n, 2)]


def tank_has_water():
    d = distance_cm()
    if d < 0:
        return False        # fail-safe: no valid reading = do not pump
    return d <= LOW_WATER_CM


# ---------------- Watering cycle ----------------
def water_plant():
    global abort_requested, next_allowed_ms, dry_count
    abort_requested = False
    start = input.running_time()
    last_tank_check = start
    basic.show_icon(IconNames.TARGET, 100)
    pump_start()
    while input.running_time() - start < PUMP_RUN_SECONDS * 1000:
        basic.pause(200)
        if abort_requested:
            break
        if input.running_time() - last_tank_check >= TANK_CHECK_MS:
            last_tank_check = input.running_time()
            if not tank_has_water():
                break
    pump_stop()
    dry_count = 0
    next_allowed_ms = input.running_time() + COOLDOWN_MIN * 60000


# ---------------- Buttons ----------------
def on_button_a():
    basic.show_number(Math.round(soil_raw()))


def on_button_b():
    d = distance_cm()
    if d < 0:
        basic.show_string("?")
    else:
        basic.show_number(Math.round(d))


def on_button_ab():
    global abort_requested
    abort_requested = True
    pump_stop()


input.on_button_pressed(Button.A, on_button_a)
input.on_button_pressed(Button.B, on_button_b)
input.on_button_pressed(Button.AB, on_button_ab)


# ---------------- Main loop ----------------
def on_forever():
    global dry_count
    pump_stop()                             # pump is only ever on inside water_plant()
    now = input.running_time()
    pct = soil_percent(soil_raw())

    if pct <= SOIL_DRY_PERCENT:
        dry_count += 1
    else:
        dry_count = 0

    if dry_count >= DRY_CONFIRM_COUNT and now >= next_allowed_ms:
        if tank_has_water():
            water_plant()
        else:
            basic.show_icon(IconNames.NO, 1000)       # dry, but tank is low
    elif pct <= SOIL_DRY_PERCENT:
        basic.show_icon(IconNames.SAD, 1000)          # dry, waiting / cooling down
    else:
        basic.show_icon(IconNames.HAPPY, 1000)        # soil is fine

    basic.pause(CHECK_INTERVAL_MS)


# Safe start-up state: pump off, trigger low
pump_stop()
pins.digital_write_pin(PIN_TRIG, 0)
basic.forever(on_forever)


# ---------------------------------------------------------------------
# FALLBACK: if Tinkercad does not accept pins.pulse_in, keep the trigger
# part of measure_once_cm() and replace everything from the
# "us = pins.pulse_in(...)" line to the end of the function with:
#
#   timeout = input.running_time_micros() + 25000
#   while pins.digital_read_pin(PIN_ECHO) == 0:
#       if input.running_time_micros() > timeout:
#           return -1
#   t_start = input.running_time_micros()
#   while pins.digital_read_pin(PIN_ECHO) == 1:
#       if input.running_time_micros() > timeout:
#           return -1
#   return (input.running_time_micros() - t_start) / 58
# ---------------------------------------------------------------------
