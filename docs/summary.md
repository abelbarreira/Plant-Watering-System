# Prompt

I'm working in a embedded automatic watering system designed to keep a large indoor plant watered safely and reliably while unattended.

The idea is to use following controller:

- BBC micro:bit V2 [BOARD]
    Ref: https://tech.microbit.org/hardware/edge-connector/#pins-and-signals
    The micro:bit itself still needs its battery power supply (I dont want to use its normal USB to power it)

- Edge Connector Kitronik 5601B
    https://dk.rs-online.com/web/p/bbc-micro-bit-add-ons/2048218
    BBC micro:bit V2: Compatible
    Ref: docs/shopping/06_edge_connector/Kitronik 5601B.pdf

With following architecture

- Kamoer Brushless Peristaltic Pump KHM3-2-12B3N40 with following:
        2-12B 12V DC Brushless motor (2000h)
        Tube Neoprene, #40 4.0mm x 7.2mmm (1000h)
            Level One (12V, 0.8A): 640ml/min, 70dB, 12W
            Level Two (12V, 0.5A):  74ml/min, 63dB,  6W
        PWM speed regulation
            0 to 5V voltage speed regulation
            Freq: 10Khz to 30Kzh
            Duty Cycle:
                0% to  10%: motor don't run         -> 0.0V to 0.5V
                11% to 100%: speed regulation range -> 0.6V to 5.0V
        Cabling
            UL1332 material PTFE, all of them 24AWG
            Yellow  FG    Signal feedback
            Red     Vcc   Positive pole of power supply
            White   SP    Speed Port
            Black   GND   Negative pole of power supply
            Green   F/R   Revsering Port
        Ref: https://www.alibaba.com/product-detail/Kamoer-KHM-High-precision-DC-Motor_60772709984.html?spm=a2700.shop_index.82.7.6f7f2624Rd2Gss
        Ref: docs/shopping/01_pumps/Kamoer/KHM3.pdf

    - Peristaltic Pump Neoprene Tube 4mm x 7.2mm
        https://www.alibaba.com/product-detail/LEIRONG-High-Quality-Silicone-Gel-Lab_1601402851177.html
        23.73 kr

    - Barbed Connector Straight
        https://www.aliexpress.com/item/1005002078165227.html?spm=a2g0o.cart.0.0.4d2738daZgdWmu&mp=1
        5pcs

    - Y Shape Barbed Connector
        https://www.aliexpress.com/item/1005001723872123.html?spm=a2g0o.cart.0.0.4d2738daZgdWmu&mp=1&pdp_npi=6%40dis%21DKK%21DKK+17.66%21DKK+17.66%21%21DKK+17.66%21%21%21%4021613bf617916483589333481e0d07%2112000017348573469%21ct%21DK%212244227893%21%211%210%21
        5 pcs

    - Silicone Rubber Tube
        https://www.aliexpress.com/item/1005010025288570.html?spm=a2g0o.cart.0.0.4d2738daZgdWmu&mp=1&pdp_npi=6%40dis%21DKK%21DKK+32.99%21DKK+32.99%21%21DKK+32.99%21%21%21%4021613bf617916483589333481e0d07%2112000050871269538%21ct%21DK%212244227893%21%211%210%21
        2 meters

    - Dripper Adjustable 4/7mm
        https://www.aliexpress.com/item/1005006194343223.html?spm=a2g0o.cart.0.0.7d6938daZgnfnC&mp=1&pdp_npi=6%40dis%21DKK%21DKK+15.33%21DKK+15.33%21%21DKK+15.33%21%21%21%4021613bf617916505425451479e0d07%2112000036215781345%21ct%21DK%212244227893%21%211%210%21
        20 pcs

- Soil-Moisture Sensor DFRobot SEN0308
    Ref: https://dk.rs-online.com/web/p/sensor-udvikling/2049905
    Ref: docs/shopping/02_soil_moisture_sensor/DFRobot SEN0308.pdf

- Float Switch RS PRO Vertical
    Ref: https://dk.rs-online.com/web/p/niveausensorer-niveauswitche/0307103
    Ref: docs/shopping/04_float_switch/RS PRO_vertical.pdf

    The micro:bit V2 powers the circuit using its internal 3.3 V pull-up resistor. The float switch itself needs no separate power supply.

The idea is following:

    SEN0308 is connected to the BOARD.
    Once it indicates the soil is dry then the BOARD activate the PUMP to provide water to the plant.
    I want to fully control the speed of the PUMP (use its PWM speed regulation and its FG Signal feedback)
    If the float sensor indicates there is no enough water in the reservoir to the BOARD then the BOARD stop the PUMP.
    The initial idea is to have a solderless environment
    The idea is to keep the full environment (electronics, cabling, power supply, wiring etc etc) as much as simple as possible
    I want only one source of power supply, I mean, besides the Power Supply (MEAN WELL AC/DC-adapter) I dont want to connect the micro:bit from its battery pack.

The Power Supply will be like this

- MEAN WELL AC/DC-adapter GST60A12-P1J (12V, 5A) 60W
    Mean Well GST60A12-P1J High Efficiency 60W 12V Single Output Power Supply Adapter Industrial Office Equipment 5A Current Desktop
    https://www.alibaba.com/product-detail/Mean-Well-GST60A12-P1J-High-Efficiency_1601225815189.html?spm=a2700.prosearch.normal_offer.d_title.569b67aftPmmW0&selectedCarrierCode=SEMI_MANAGED_STANDARD%40%40STANDARD&priceId=d50579caadad4899ae610087a391e2a9

    EU Plug Ac Power Cord for Computer C13 Cable 3 Pin Connector Wire Harness Powercon 3 Pin Wire Connector
    https://www.alibaba.com/product-detail/EU-Plug-Ac-Power-Cord-for_62095368508.html?spm=a2700.prosearch.normal_offer.d_title.6b6867afkDX9E5&priceId=ae8952d4ef804dc0b8e99f2915d5fde2
    10kr

- Having this FEMALE jack version (a 5.5×2.1 socket → screw terminals)
https://www.aliexpress.com/item/1005010133352189.html?spm=a2g0o.productlist.main.4.55a1239aKgHr3x&aem_p4p_detail=202610101459307708909935760280001915735&algo_pvid=ca40a13d-c0a6-4096-b714-9810195fc4b7&algo_exp_id=ca40a13d-c0a6-4096-b714-9810195fc4b7-3&pdp_ext_f=%7B%22order%22%3A%2275%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21DKK%219.90%219.90%21%21%219.69%219.69%21%402103810f17916695705034317e0f47%2112000051258110222%21sea%21DK%212244227893%21ABX%211%210%21n_tag%3A-29910%3Bd%3Accaae3c5%3Bm03_new_user%3A-29895&curPageLogUid=vf7zXReKppMG&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005010133352189%7C_p_origin_prod%3A&search_p4p_id=202610101459307708909935760280001915735_1
    5.5mm X 2.1mm 12V DC Power Supply Screw Plug Connector 5.5X2.1mm Female
    Universal 12V DC Compatibility
    Pump will be connected from here directly

- And then this LM2596 Multi Channel Switching Power Supply 3.3V/5V/12V/ADJ Adjustable Voltage Output Power Supply Module
https://www.aliexpress.com/item/1005009488854963.html?spm=a2g0o.productlist.main.2.2c2c3d776mKsJJ&algo_pvid=159efc78-0402-4cf7-b437-689c2defeffb&algo_exp_id=159efc78-0402-4cf7-b437-689c2defeffb-1&pdp_ext_f=%7B%22order%22%3A%2262%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21DKK%2134.22%2134.22%21%21%215.00%215.00%21%400b88ab8a17916699777091466e107e%2112000049261753253%21sea%21DK%212244227893%21ABX%211%210%21n_tag%3A-29910%3Bd%3Accaae3c5%3Bm03_new_user%3A-29895&curPageLogUid=sYec7Ws8rGA1&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009488854963%7C_p_origin_prod%3A
    Multi-Output Voltage Flexibility The LM2596 module delivers adjustable output voltages including 3.3V, 5V, 12V, and ADJ
    Wide Input Voltage Range Designed to operate with a supply voltage from 5V to 40V
    High Current Output Capacity With a maximum dissipation power of 3A
    micro:bit V2 will be connected to here 3.3v output

- Multimeter ANENG AN8009
    Capacitance Range
    9.99nF/99.99nF/999.9nF/9.99uF/99.99uF/999.9uF/9.999MF
    Voltage Range
    999.9mV/9.999V/99.99V/999.9V
    Current Range
    60mA/600mA/10A
    Resistance Range
    99.99/999.9/9.999k/99.99k/999.9K/999.9M
    Frequency
    99.99Hz/999.9Hz/9.999KHz/99.99KHz/999.9KHz/9.999MHz
    DC/AC Voltage
    9.999mV/99.99mV/999.9mV/9.999V/99.99V/750ACV(999.9DCV)
    DC/AC Current
    999.9mA/9.999A/99.99μA/999.9μA
    Display Type: Digital Display
    Diode Test: Yes
    Continuity: Yes
    Duty Cycle: 1%-99%
    Sample Rate: 3 times per second
    Power: 2 * 1.5V AAA batteries(Not Included)

- BSS138 4-channel logic level converter module with the pin headers already soldered
    https://www.aliexpress.com/item/1005011941808159.html?spm=a2g0o.cart.0.0.7f4c38dax5J3uc&mp=1

    The module has LV and HV supply pins plus several channels. Connect it like this:
        LV to 3.3 V and HV to 5 V (from the LM2596 outputs).
        GND to common ground.
        Micro:bit P2 goes to an LV channel, and the matching HV channel goes to the pump’s SP wire.

    Yes, one 4-channel BSS138 module can handle SP and FG at the same time.
    Wiring
        LV → 3.3 V, HV → 5 V, GND → common ground.
        Channel 1: micro:bit P2 → LV1, HV1 → pump SP.
        Channel 2: pump FG → HV2, LV2 → micro:bit P12.
        Leave the unused channels unconnected.

- AMS1117-3.3 LDO Linear Regulator Board 800mA
    https://www.aliexpress.com/item/1005012337015319.html?spm=a2g0o.productlist.main.1.30976963LfH014&algo_pvid=61d74167-3024-47e4-9e6d-d0ff546d7bc5&algo_exp_id=61d74167-3024-47e4-9e6d-d0ff546d7bc5-0&pdp_ext_f=%7B%22order%22%3A%2240%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21DKK%2110.57%2110.44%21%21%2110.35%2110.22%21%402103810f17917352285972930e1054%2112000058136450929%21sea%21DK%212244227893%21ABX%211%210%21n_tag%3A-29910%3Bd%3Accaae3c5%3Bm03_new_user%3A-29895&curPageLogUid=5XrF4n0r3Lp2&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005012337015319%7C_p_origin_prod%3A

    High-efficiency 3.3V power regulation This AMS1117-3.3 LDO Linear Regulator Board delivers stable 3.3V output with up to 800mA current capacity, ideal for low-noise power supply in sensitive electronic projects.

    For the soil moisture sensor to the board

    Only add it if the soil readings stay noisy with the 3.3 V LM2596 channel plus the capacitors.

- 830-hole Breadboard Kit MB-102 for Arduinos UNO R3 Component Package Beginner Starter Kit Boxed
    https://www.alibaba.com/product-detail/830-hole-Breadboard-Kit-MB-102_1601518996653.html
    Component listing: 1pcs Power Supply Module WARNING: Pls. do not use the voltage higher than 9V
        1pcs 830 tie-points Breadboard
        1pcs 65 Jumper Wire
        140pcs Solderless Jumper Wire
        20pcs Female-to-male Dupont Wire
        2pcs Pin header (40pin)
        1pcs Precision Potentiometer
        2pcs Photoresistor
        1pcs Thermistor
        5pcs Diode Rectifier (1N4007)
        5pcs NPN Transistor (PN2222)
        1pcs IC 4N35
        1pcs IC 74HC595
        1pcs Active Buzzer
        1pcs Passive Buzzer
        10pcs Button (small)
        10pcs 22pf Ceramic Capacitor
        10pcs 104 Ceramic Capacitor
        5pcs Electrolytic Capacitor (10UF 50V)
        5pcs Electrolytic Capacitor (100UF 50V)
        10pcs White LED
        10pcs Yellow LED
        10pcs Blue LED
        10pcsGreen LED
        10pcs Red LED
        1pcs RGB LED
        10pcs Resistor (10R)
        10pcs Resistor (100R)
        10pcs Resistor (220R)
        10pcs Resistor (330R)
        10pcs Resistor (1K)
        10pcs Resistor (2K)
        10pcs Resistor (5K1)
        10pcs Resistor (10K)
        10pcs Resistor (100K)
        10pcs Resistor (1M)

- Fuse 2A slow-blow (T), 5 × 20 mm glass cartridge
    Slow Blow Glass Tube Fuse 5x20MM 2a 5PCS
    https://www.aliexpress.com/item/1005009422492983.html?spm=a2g0o.productlist.main.11.6c6bLKnQLKnQ5q&algo_pvid=e2835c82-52c7-4cf1-b7fc-66f59057ffb3&algo_exp_id=e2835c82-52c7-4cf1-b7fc-66f59057ffb3-10&pdp_ext_f=%7B%22order%22%3A%226631%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21DKK%2116.64%2116.64%21%21%212.44%212.44%21%402161390417922690961358527e0e30%2112000049084083664%21sea%21DK%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Accaae3c5%3Bm03_new_user%3A-29895&curPageLogUid=To14C9GaLCQG&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009422492983%7C_p_origin_prod%3A

    RS PRO 2A Patronsikring, Reaktionshastighed: T Glas, 250V ac, 5 x 20 mm
    https://dk.rs-online.com/web/p/finsikringer/0563722

    Protection on the 12 V side

- Holder: 5 × 20 mm fuse holder,  rated ≥ 2 A.
    RS PRO Panelmonteret sikringsholder, 6.3A 5 x 20 mm RS PRO 25V
    https://dk.rs-online.com/web/p/sikringsholdere/0563784?gb=a

- 22 awg silicone wire
    https://www.aliexpress.com/item/1005006106389362.html?spm=a2g0o.productlist.seoads.4.15342772LICaBW&p4p_pvid=202610171406522110340017747260003613995_2
    Buy red, black and one signal colour

- Lever-nut / terminal blocks Wago 221
    https://www.alibaba.com/product-detail/221-Cable-Connector-6mm-4mm-Power_1601383854771.html?spm=a2700.prosearch.normal_offer.d_title.2d1b67afyqpWug&priceId=45360a9c330348cd903afd2c11babdac
    With 1-core cable: buy 2 of 2P and 2 of 3P with

- Infineon Type P-Kanal, MOSFET, 23 A 100 V Forbedring, 3 Ben, TO-220, HEXFET, IRF9540NPBF
    https://dk.rs-online.com/web/p/mosfet/5411225?gb=a
    14 kr

- Clean Water Reservoir (5l or 10l)

Considering all this, I want for you to deeply analyse everything and tell me following, pls

1. Which other hardware or electronics components should I buy, maybe I need some MOSFET, Diodes, etc or whatever you think I need get and it is not in the list
2. Shortly if you thing there are things in the list not needed, pls tell me
3. Provide me a mermaid flow chart with the full wiring from the Power Supply considering all the needed devices to be connected including pull ups, pull downs etc etc
    For example, flow chart with the:
        - Power distribution, Power Switch, Complete Overview
        - About Pump and Tubing assuming there is only one reservoir, and one plant which will receive two drippers
4. Don't worry about the software for the microcontroller for the moment, we will deal with this later
