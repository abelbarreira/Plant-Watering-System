# Automatic watering system – diagrams

Zoom 1500 px

Scroll inside each diagram to pan. Use the slider to enlarge it. To save as PNG/SVG, paste the Mermaid code into mermaid.live and use Actions → Download.

## A. Power distribution and signal wiring

```mermaid
flowchart TB
  AC["230 V outletRCD protected"] --> CORD["Certified C13 mains cord"] --> PSU["MEAN WELL GST60A12-P1J12 V 5 A"]
  PSU --> JACK["5.5x2.1 female jackscrew terminalsverify polarity with multimeter"]
  JACK -->|"+12 V"| F1["F1 2 A slow-blow fuse"] --> SW1["SW1 power switchSPST 3 A or more"] --> W12["Wago 3P no.1+12V_SW"]
  JACK -->|"GND"| WG["Wago 3P no.2GND_PWR"]

  subgraph BUCK["LM2596 module - tune and measure BEFORE connecting loads"]
    VINP["VIN+"]
    VINN["VIN-"]
    V5["OUT 5 V"]
    V33["OUT 3.3 Vplus 100 uF and 100 nF"]
    GL["OUT GND = GND_LOGICbreadboard blue rail"]
  end
  W12 --> VINP
  WG --> VINN

  subgraph PSTAGE["Pump power stage - OFF by default"]
    Q1["Q1 IRF9540N P-MOSFETSource=+12V_SW Drain=PUMP_V"]
    R1["R1 10kgate to source = pull-up"]
    R2["R2 100R gate series"]
    Q2["Q2 PN2222Collector to R2, Emitter to GND_LOGIC"]
    R3["R3 1k base"]
    R4["R4 10k base to GND_LOGICpull-down"]
  end
  W12 -->|"Source"| Q1
  W12 --> R1 -->|"Gate"| Q1
  Q1 -->|"Gate"| R2 --> Q2
  P16 --> R3 --> Q2
  R4 --- Q2
  Q2 -->|"Emitter"| GL

  PUMP["Kamoer KHM3-2-12B3N40Red Vcc, Black GNDWhite SP, Yellow FG, Green F/RC1 100-470 uF across Vcc and GND"]
  Q1 -->|"Drain = PUMP_V to Red"| PUMP
  WG -->|"Black GND"| PUMP
  PUMP -->|"Green F/R: fixed per datasheet,never floating"| WG

  subgraph LSH["BSS138 4-channel level shifter"]
    LV["LV pin"]
    HV["HV pin"]
    LG["GND"]
    CH1["CH1: LV1 to HV1"]
    CH2["CH2: LV2 to HV2"]
    R5["R5 1k LV1 to GND_LOGICidle LOW so SP = 0 V"]
  end
  V33 --> LV
  V5 --> HV
  GL --> LG
  CH1 --- R5
  HV -.-> CH1
  CH1 -->|"HV1 to White SP"| PUMP
  PUMP -->|"Yellow FG to HV2"| CH2

  subgraph MB["micro:bit V2 on Kitronik 5601B edge connector"]
    MB3V["3V pin - USB UNPLUGGED"]
    MBGND["GND pin"]
    P2["P2 PWM 20 kHz"]
    P14["P14 FG input"]
    P16["P16 pump enable"]
    P0["P0 analog in"]
    P8["P8 float input"]
  end
  V33 --> MB3V
  GL --> MBGND
  P2 --> CH1
  CH2 -->|"LV2"| P14

  subgraph SENS["Sensors"]
    SEN["SEN0308VCC 3.3 V, GND, AOUT"]
    FLT["RS PRO float switchclosed = water OK"]
    PU["R6 10k pull-up to 3.3 VC2 100 nF to GND at pin"]
  end
  V33 --> SEN
  GL --> SEN
  SEN -->|"AOUT"| P0
  V33 --> PU --> P8
  FLT -->|"one wire"| P8
  FLT -->|"other wire"| GL
```

## B. Hydraulics: one reservoir, one plant, two drippers

```mermaid
flowchart LR
  subgraph RES["Opaque reservoir 5-10 L with lid"]
    INTAKE["Intake tube endweighted, with strainer"]
    FLOAT["Float switchmounted ABOVE intake level"]
  end
  INTAKE -->|"silicone tube 4/7"| B1["Straight barb 1"]
  B1 --> PT["Pump-head tubeneoprene 4 x 7.2inside Kamoer KHM3"]
  PT --> B2["Straight barb 2"]
  B2 -->|"silicone tube"| FIL["Optional inline filter"]
  FIL --> Y["Y barbed connector"]
  Y -->|"branch A"| D1["Dripper A adjustable"]
  Y -->|"branch B"| D2["Dripper B adjustable"]
  D1 --> PLANT["Plant pot soil"]
  D2 --> PLANT
  SOIL["SEN0308 probebetween both drippers,electronics above soil line"] -.-> PLANT
  PLANT --> TRAY["Drip tray"]
  FLOAT -.->|"wires to P8 and GND"| MCU["micro:bit"]
  SOIL -.->|"wire to P0"| MCU
```