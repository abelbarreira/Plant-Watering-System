# ====================================================================
#  One-plant automatic watering  -  BBC micro:bit V2  (Tinkercad Python)   v2
# ====================================================================
#  Wiring
#    P0  <- HC-SR04P ECHO         (digital input)
#    P1  -> HC-SR04P TRIG         (digital output)
#    P2  <- SEN0308 SIG           (analog input)
#    P8  -> 100 ohm -> MOSFET gate (10k pull-down) -> pump (low-side)
#
#  Behaviour
#    * Pump is OFF at power-up and only runs inside water_plant(), after
#      the soil was dry on several readings in a row AND the reservoir
#      has enough water.
#    * Pump runs PUMP_RUN_SECONDS (~500 ml) and is cut early if the
#      reservoir gets too low, the distance reading is invalid, or A+B.
#    * Cool-down after every run so water can soak in.
#
#  Buttons / gestures (for testing and calibration)
#    A      = show raw soil reading
#    B      = show water distance in cm ("?" = no echo received)
#    A+B    = emergency stop
#    SHAKE  = run the pump for 3 s (tests MOSFET / pump wiring only)
#
#  TEST_MODE = True  -> fast timings + live readings scroll every cycle
#  Set TEST_MODE = False once everything is calibrated and working.
# ====================================================================

TEST_MODE = True

# ---------------- Pins ----------------
PIN_ECHO = DigitalPin.P0
PIN_TRIG = DigitalPin.P1
PIN_SOIL = AnalogPin.P2
PIN_PUMP = DigitalPin.P8

# ---------------- Settings (CALIBRATE THESE) ----------------
# Soil: press A with the sensor dry, then wet, and type the two raw
# numbers here. Works whichever way round they are.
SOIL_RAW_DRY = 800        # raw reading when completely dry   (placeholder)
SOIL_RAW_WET = 400        # raw reading when fully wet        (placeholder)
SOIL_DRY_PERCENT = 35     # at or below this % the plant needs water

# Reservoir: distance from sensor down to the water. Larger = emptier.
# Set the lowest acceptable level, press B, type the number here.
LOW_WATER_CM = 15         # farther than this = "not enough water"

# Pump run time for ~500 ml (measure it with a jug on the real build)
PUMP_RUN_SECONDS = 8 if TEST_MODE else 30

# Timing
CHECK_INTERVAL_MS = 2000 if TEST_MODE else 10000
DRY_CONFIRM_COUNT = 2 if TEST_MODE else 3
TANK_CHECK_MS = 2000
COOLDOWN_MIN = 1 if TEST_MODE else 30

# ---------------- State ----------------
dry_count = 0
next_allowed_ms = 0
abort_requested = False
testing_pump = False


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
    readings: List[number] = []
    for i in range(5):
        d = measure_once_cm()
        if d > 0:
            readings.append(d)
        basic.pause(60)
    n = len(readings)
    if n < 3:
        return -1
    for a in range(n):
        for b in range(n - 1 - a):
            if readings[b] > readings[b + 1]:
                tmp = readings[b]
                readings[b] = readings[b + 1]
                readings[b + 1] = tmp
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


# ---------------- Buttons / gestures ----------------
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


def on_shake():
    global testing_pump
    if testing_pump:
        return
    testing_pump = True
    pump_start()
    basic.pause(3000)
    pump_stop()
    testing_pump = False


input.on_button_pressed(Button.A, on_button_a)
input.on_button_pressed(Button.B, on_button_b)
input.on_button_pressed(Button.AB, on_button_ab)
input.on_gesture(Gesture.SHAKE, on_shake)


# ---------------- Main loop ----------------
def on_forever():
    global dry_count
    now = input.running_time()
    raw = soil_raw()
    pct = soil_percent(raw)

    if TEST_MODE:
        d = distance_cm()
        basic.show_string("S" + str(Math.round(raw)) + " " + str(Math.round(pct)) + "% D" + str(Math.round(d)))

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
