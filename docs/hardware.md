
# Hardware

## Controller

[BBC micro:bit v2 Go Bundle](https://tech.microbit.org/hardware/2-0-revision/)

### Soil-moisture sensor

- Capacitive
- Sensor VCC ── 3.3 V
- Sensor GND ── GND
- Sensor AO  ── ADC input
- Avoid Poisoning the pant

### Small water pump & power supply

For one plant, a small 5 V or 6 V DC peristaltic pump is a particularly nice option.

A peristaltic pump

50 mL/s
  100 ms → 5 mL
  1 s    → 50 mL
  2 s    → 100 mL

### MOSFET driver

A transistor/MOSFET stage to connect GPIO to the pump

### Water-level sensor

A simple water-level sensor.
