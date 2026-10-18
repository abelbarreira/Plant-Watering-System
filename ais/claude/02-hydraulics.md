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
