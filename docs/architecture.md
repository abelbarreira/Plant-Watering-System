# Architecture

## Phase 1

### Hardware

                 ┌────────────────────┐
                 │     micro:bit V2   │
                 │                    │
 SEN0308 ───────►│ ADC                │
                 │                    │
 Float switch ──►│ GPIO               │
                 │                    │
                 │             GPIO ──┼────► MOSFET ──► Pump
                 │                    │
                 └────────────────────┘

### Software

                 ┌──────────────┐
                 │    START     │
                 └──────┬───────┘
                        ↓
                 Read soil moisture
                        ↓
                 Check sensor valid?
                   /           \
                 NO             YES
                 ↓               ↓
              FAULT        Check water level
                                  ↓
                           Water available?
                            /          \
                          NO            YES
                          ↓              ↓
                        FAULT       Need water?
                                      /    \
                                    NO      YES
                                    ↓        ↓
                                  WAIT    PUMP
                                             ↓
                                          SETTLE
                                             ↓
                                        READ AGAIN

## Pump

                 5 L reservoir
                      │
                      ▼
                      │
                4×6 mm BPT
                      │
              ┌─────────────────────┐
              │  BP200              │
              │ 12 V BLDC brushless │
              │ B46 BPT             │
              │ 4×6 mm              │
              └───────┬─────────────┘
                      │
                4×6 mm BPT
                      │
                      L-Shape Connector
                      │
                      │         4×6 silicone
                     Y1
                    /  \        4×6 silicone
                   /    \
                D1      Y2
                       /  \     4×6 silicone
                      /    \
                     D2    D3


## Power

                    230 V AC
                       │
                       ▼
              ┌─────────────────┐
              │  12 V DC PSU    │
              │   ~2–3 A        │
              └────────┬────────┘
                       │
                ┌──────┴───────┐
                │              │
                ▼              ▼
           12 V → BP200    12 V → 5 V
                              DC/DC
                                │
                                ▼
                         ┌─────────────────┐
                         │  BBC micro:bit  │
                         │       V2        │
                         └────────┬────────┘
                                  │
                         Kitronik 5601B
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
         Soil sensor         Float switch        Pump control
         SEN0308              0307103              MOSFET/
                                                   driver

12 V PSU GND
     │
     ├──── BP200 GND
     │
     ├──── buck converter GND
     │
     └──── micro:bit/control GND


https://www.ebay.com/itm/135179147711

              Mean Well 12 V / 3 A
                       │
                 5.5 × 2.1 mm
                       │
                       ▼
             ┌──────────────────┐
             │   THIS eBay PCB  │
             │                  │
             │  12V ────────────┼──► BP200
             │   5V ────────────┼──► micro:bit
             │ 3.3V ────────────┼──► sensors
             │  GND ────────────┼──► common GND
             └──────────────────┘

## MOSFET & Resitors