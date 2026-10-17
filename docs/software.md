# Software

## Fail-safe design

The float switch and the micro:bit are a single point of failure: if the program hangs while the pump is running, the pot overflows. Consider:

Software limits: a maximum run time per cycle, a minimum soak time between waterings (the soil takes time to respond), and a daily volume cap.
A hardware enable: a logic-level N-MOSFET (not an IRF520) switching the pump’s 12 V, driven by a separate GPIO. That way a hung micro:bit can’t leave the pump running.

A drip tray under the pot, and ideally an independent overflow check.
Wire the float switch fail-safe: switch to GND with the internal pull-up enabled, so water present = LOW and a broken wire reads as “empty” and stops the pump. Add 100 nF and a software debounce. Your idea of using the micro:bit’s internal pull-up is right, so no separate 3.3 V is needed for it.

## No Float Switch

If I change to a larger reservoir but without floating switch, it should be able to detect it and still works

## Calibration and software

Soil sensor: record readings in dry air and in water, then set your dry threshold in between, with hysteresis.
Pump: measure ml/s at a few duty cycles, since the duty-to-flow relationship won’t be linear. Remember that duty below 10% does nothing. At low speed it will also be much quieter than the 63-70 dB rating suggests for full speed.
