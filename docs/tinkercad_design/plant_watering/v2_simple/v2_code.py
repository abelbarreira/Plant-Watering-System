# ====================================================================
#  Plant watering - micro:bit V2 (Tinkercad Python)            v3
#  Builds on v2_code.py: calibration, hysteresis, cooldown, retry limit
# ====================================================================
#  Wiring:  P2 <- soil sensor SIG      P8 -> 100 ohm -> MOSFET gate
#
#  How it decides
#    1. Soil moisture is turned into a percentage using your calibration.
#    2. "Dry" starts at DRY_PERCENT or less. It must be dry on
#       DRY_CONFIRM_COUNT readings in a row (ignores single glitches).
#    3. The pump then runs for PUMP_RUN_SECONDS (~500 ml), but only if
#       tank_has_water() is True (float switch goes there later).
#    4. After a run there is a COOLDOWN_MIN wait so the water can soak in.
#    5. If the soil is still dry after MAX_DOSES doses in a row (it never
#       reached WET_PERCENT), the system locks out and shows a skull:
#       something is wrong (empty tank, pump, hose, sensor).
#       Reaching WET_PERCENT, or pressing A+B, clears the lock-out.
#       The gap between DRY_PERCENT and WET_PERCENT is the hysteresis.
#
#  Buttons:  A = show raw soil value (for calibration)
#            B = show soil percent
#            A+B = emergency stop (pump stays off for ABORT_HOLD_MIN),
#                  or clears a lock-out when pressed while idle
#
#  Display:  happy = soil ok     sad = dry, waiting     target = pumping
#            no = dry but no water in tank     skull = locked out
# ====================================================================

TEST_MODE = True  # True: fast timings + live readings. False: real use.

# ---------------- Pins ----------------
PIN_SOIL = AnalogPin.P2
PIN_PUMP = DigitalPin.P8

# ---------------- Soil calibration ----------------
# Press A with the sensor dry, then wet, and enter the two raw values.
# Any order works (a real SEN0308 will probably read HIGHER when dry,
# so DRY would be the bigger number there).
SOIL_RAW_DRY = 0  # raw value when dry   (simulator placeholder)
SOIL_RAW_WET = 800  # raw value when wet   (simulator placeholder)

DRY_PERCENT = 30  # at or below this = needs water
WET_PERCENT = 60  # at or above this = recovered (hysteresis)

# ---------------- Pump and timing ----------------
PUMP_RUN_SECONDS = 8 if TEST_MODE else 30  # measure with a jug for ~500 ml
COOLDOWN_MIN = 1 if TEST_MODE else 30
ABORT_HOLD_MIN = 5 if TEST_MODE else 60  # pause after an A+B emergency stop
CHECK_INTERVAL_MS = 2000 if TEST_MODE else 10000
DRY_CONFIRM_COUNT = 2 if TEST_MODE else 3
MAX_DOSES = 3  # doses in a row without the soil recovering

# ---------------- State ----------------
dry_count = 0
doses_without_recovery = 0
next_allowed_ms = 0
locked_out = False
abort_requested = False


# ---------------- Pump ----------------
def pump_start():
    pins.digital_write_pin(PIN_PUMP, 1)


def pump_stop():
    pins.digital_write_pin(PIN_PUMP, 0)


# ---------------- Water tank (placeholder) ----------------
def tank_has_water():
    # TODO: float switch goes here later. Return True = enough water.
    return True


# ---------------- Soil sensor ----------------
def soil_raw():
    total = 0
    for i in range(10):
        total += pins.analog_read_pin(PIN_SOIL)
        basic.pause(5)
    return total / 10


def soil_percent(raw):
    span = SOIL_RAW_WET - SOIL_RAW_DRY
    if span == 0:
        return 0
    pct = (raw - SOIL_RAW_DRY) * 100 / span
    return max(0, min(100, pct))


# ---------------- Watering cycle ----------------
def water_plant():
    global abort_requested, next_allowed_ms, dry_count
    global doses_without_recovery, locked_out
    abort_requested = False
    start = input.running_time()
    basic.show_icon(IconNames.TARGET, 100)
    pump_start()
    while input.running_time() - start < PUMP_RUN_SECONDS * 1000:
        basic.pause(200)
        if abort_requested:
            break
        if not tank_has_water():
            break
    pump_stop()
    dry_count = 0
    if abort_requested:
        # Stopped by hand: stay off for a long while, don't count as a dose
        next_allowed_ms = input.running_time() + ABORT_HOLD_MIN * 60000
    else:
        next_allowed_ms = input.running_time() + COOLDOWN_MIN * 60000
        doses_without_recovery += 1
        if doses_without_recovery >= MAX_DOSES:
            locked_out = True


# ---------------- Buttons ----------------
def on_button_a():
    basic.show_number(Math.round(soil_raw()))


def on_button_b():
    basic.show_number(Math.round(soil_percent(soil_raw())))


def on_button_ab():
    global abort_requested, locked_out, doses_without_recovery
    abort_requested = True
    pump_stop()
    locked_out = False
    doses_without_recovery = 0


input.on_button_pressed(Button.A, on_button_a)
input.on_button_pressed(Button.B, on_button_b)
input.on_button_pressed(Button.AB, on_button_ab)


# ---------------- Main loop ----------------
def on_forever():
    global dry_count, doses_without_recovery, locked_out
    now = input.running_time()
    raw = soil_raw()
    pct = soil_percent(raw)

    if TEST_MODE:
        basic.show_string("S" + str(Math.round(raw)) + " " + str(Math.round(pct)) + "%")

    # Upper threshold: soil recovered, so reset the retry counter
    if pct >= WET_PERCENT:
        doses_without_recovery = 0
        locked_out = False

    # Lower threshold: count consecutive dry readings
    if pct <= DRY_PERCENT:
        dry_count += 1
    else:
        dry_count = 0

    if locked_out:
        basic.show_icon(IconNames.SKULL, 1000)
    elif dry_count >= DRY_CONFIRM_COUNT and now >= next_allowed_ms:
        if tank_has_water():
            water_plant()
        else:
            basic.show_icon(IconNames.NO, 1000)
    elif pct <= DRY_PERCENT:
        basic.show_icon(IconNames.SAD, 1000)
    else:
        basic.show_icon(IconNames.HAPPY, 1000)

    basic.pause(CHECK_INTERVAL_MS)


# Safe start-up state: pump off
pump_stop()
basic.forever(on_forever)
