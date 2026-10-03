# Automatic Plant Watering System 🌱

An embedded automatic watering system designed to keep a large indoor pothos plant watered safely and reliably while unattended.

The project is built as a real embedded system rather than a simple timer: watering decisions are based on soil moisture, with safety limits and room for future monitoring and remote control.

## Project Goals

- Automatically maintain suitable soil moisture.
- Use controlled water pulses rather than continuous pumping.
- Detect low water level in the reservoir.
- Keep the system safe if a sensor, pump, or network fails.
- Run reliably for extended periods.
- Eventually provide Wi-Fi/MQTT monitoring and control.

## Hardware

Initial controller:

- BBC micro:bit V2
- DFRobot SEN0308 capacitive soil-moisture sensor
- Peristaltic water pump
- Water reservoir (~5 L)
- Float switch for low-water detection
- MOSFET pump driver + flyback diode
- Drip irrigation tubing
- 2–3 watering points around the plant
- Transparent electronics enclosure
- [0.96" I²C OLED (SSD1306)](https://www.mouser.com/datasheet/2/1398/Soldered_333099-3395096.pdf)
- Jumper wires
- 5 V power supply

The system will later use a Microchip RNWF02 Wi-Fi module for network connectivity.

## Development Plan

### Phase 1 — Local Automatic Watering

Focus on making the watering system reliable **without Wi-Fi**.

The micro:bit will:

1. Read the soil-moisture sensor.
2. Determine whether watering is required.
3. Check the reservoir level.
4. Run the pump for a controlled period.
5. Wait for the water to distribute through the soil.
6. Measure the soil again.
7. Repeat only when necessary.

Safety features will include:

- Maximum pump runtime
- Low-water protection
- Sensor validity checks
- Watchdog/recovery handling
- Controlled watering intervals
- Sensor calibration

### Phase 2 — Wi-Fi & Remote Monitoring

After the local system is stable, add:

- Microchip RNWF02 Wi-Fi module
- MQTT communication
- Remote telemetry
- Remote status monitoring
- Remote watering commands
- Alerts for low water / faults
- Automatic operation continuing even when Wi-Fi or the Internet is unavailable

The network connection will **not*- be responsible for the core watering safety logic. Local control must always remain autonomous.

## Repository Structure

```text
plant-watering/
├── README.md
├── docs/
│   ├── hardware.md
│   ├── wiring.md
│   └── calibration.md
├── phase1/
│   └── ...
└── phase2/
    └── ...
```

## Philosophy

> **Local control first. Connectivity second.**

The plant should remain safely watered even if Wi-Fi, MQTT, or the Internet is unavailable.

The project will be developed incrementally, starting with a simple and testable local watering controller and gradually adding connectivity and remote management.
