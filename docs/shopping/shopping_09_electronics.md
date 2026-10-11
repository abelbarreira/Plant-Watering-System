# Electronics

## BSS138 4-channel logic level converter module

BSS138 4-channel logic level converter module with the pin headers already soldered
    https://www.aliexpress.com/item/1005011941808159.html?spm=a2g0o.cart.0.0.7f4c38dax5J3uc&mp=1

    The module has LV and HV supply pins plus several channels. Connect it like this:
        LV to 3.3 V and HV to 5 V (from the LM2596 outputs).
        GND to common ground.
        Micro:bit P2 goes to an LV channel, and the matching HV channel goes to the pump’s SP wire.

    Bi-directional I2C Logic Level Converter This 4-channel converter supports bidirectional signal translation between 5V and 3.3V systems, ideal for seamless communication in mixed-voltage environments.
    Compatible with Popular Microcontrollers Designed for use with Arduino, Raspberry Pi, ESP32, STM32, and other I2C-based devices, ensuring reliable integration across various DIY projects.
    Uses High-Quality BSS138 Transistors Built with BSS138 MOSFETs for fast switching, low power consumption, and stable performance during signal level conversion.
    Plug-and-Play Module Design The compact module-type design allows for easy connection and integration into circuits without soldering, perfect for quick prototyping.
    Available in Multiple Quantities Choose from 1pc, 3pcs, or 5pcs per pack, offering flexibility for individual use or bulk projects requiring multiple converters.
    Brand-Free, New Condition This new product comes with no brand name, ensuring cost-effective access to reliable logic level conversion functionality.
    Origin: Mainland China, Sold by Piece Manufactured in Mainland China, this item is sold as 1 piece per pack, making it simple to order and manage for small-scale or large-scale DIY needs.

    Yes, one 4-channel BSS138 module can handle SP and FG at the same time.

## AMS1117-3.3 LDO Linear Regulator Board 800mA
    https://www.aliexpress.com/item/1005012337015319.html?spm=a2g0o.productlist.main.1.30976963LfH014&algo_pvid=61d74167-3024-47e4-9e6d-d0ff546d7bc5&algo_exp_id=61d74167-3024-47e4-9e6d-d0ff546d7bc5-0&pdp_ext_f=%7B%22order%22%3A%2240%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21DKK%2110.57%2110.44%21%21%2110.35%2110.22%21%402103810f17917352285972930e1054%2112000058136450929%21sea%21DK%212244227893%21ABX%211%210%21n_tag%3A-29910%3Bd%3Accaae3c5%3Bm03_new_user%3A-29895&curPageLogUid=5XrF4n0r3Lp2&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005012337015319%7C_p_origin_prod%3A

    High-efficiency 3.3V power regulation This AMS1117-3.3 LDO Linear Regulator Board delivers stable 3.3V output with up to 800mA current capacity, ideal for low-noise power supply in sensitive electronic projects.

    For the soil moisture sensor to the board

    Only add it if the soil readings stay noisy with the 3.3 V LM2596 channel plus the capacitors.

## Resitors

Some 100 kΩ for the pull-down on SP line or even FG line if needed
Some 2.2 kΩ pull-down on the LV side

## Capacitors

Get one 100 µF electrolytic (16 V or higher) and one 100 nF ceramic.
A bulk capacitor (470-1000 µF, 25 V)
100 nF

## Dupont Jumpers

Female-to-female Dupont jumper wires for the connections to the BSS138 module and the AMS1117.
Female-to-male Dupont jumpers or a small breadboard for the sensor and float switch wires. The DFRobot SEN0308 comes with a cable, so check what connector it ends in.
Wago lever connectors or screw-terminal blocks for the pump’s bare wires and the 12 V jack. The 5601B has no terminals for those.

    About screw-terminal blocks
    20pcs High-Quality Terminal Blocks This pack includes 20 pieces of KF301-2P terminal blocks, ideal for reliable electrical connections in various wiring applications. Perfect for both DIY and industrial use.
    5.08mm Pitch for Precision Fit Designed with a 5.08mm pitch, these terminal blocks ensure accurate alignment and secure connections. The consistent spacing supports easy installation and stable performance.
    Splice Type for Easy Wiring As a splice terminal block, this product enables seamless wire joining without soldering. It’s ideal for quick, efficient, and secure electrical splicing in control circuits.
    CE Certified for Safety Compliance Certified with CE, this terminal block meets European safety standards. It ensures reliable performance and compliance with low-voltage regulations for safe operation.
    Low Voltage Compatible – 50Vac / 75Vdc Rated for low voltage applications , it’s suitable for control circuits and automation systems requiring safe, stable power handling.

> Search for this    2.54 mm pitch


## PENDINGS

5. Protection on the 12 V side
A fuse (2 A fast-blow or a resettable PTC), a TVS diode (SMBJ15A) and a bulk capacitor (470-1000 µF, 25 V) near the pump.
A reverse-polarity diode (or a P-MOSFET). The screw-terminal jack makes miswiring easy, so confirm the centre-positive polarity.
Wire gauge of at least 22 AWG for the 12 V runs, and ferrules for the screw terminals.

6. Fail-safe design

The float switch and the micro:bit are a single point of failure: if the program hangs while the pump is running, the pot overflows. Consider:

Software limits: a maximum run time per cycle, a minimum soak time between waterings (the soil takes time to respond), and a daily volume cap.
A hardware enable: a logic-level N-MOSFET (not an IRF520) switching the pump’s 12 V, driven by a separate GPIO. That way a hung micro:bit can’t leave the pump running.
A drip tray under the pot, and ideally an independent overflow check.
Wire the float switch fail-safe: switch to GND with the internal pull-up enabled, so water present = LOW and a broken wire reads as “empty” and stops the pump. Add 100 nF and a software debounce. Your idea of using the micro:bit’s internal pull-up is right, so no separate 3.3 V is needed for it.

7. Mechanical items
Barbed fittings or clamps for the 4.0 × 7.2 mm tubing, an intake filter or weight in the reservoir, and a drip nozzle or spray-free outlet.
An enclosure that keeps electronics away from water, with strain relief on cables.
Optionally, tie F/R to GND (or per the datasheet) to fix the direction, or give it a GPIO through a shifter if you want a short reverse to avoid drips.

8. Calibration and software
Soil sensor: record readings in dry air and in water, then set your dry threshold in between, with hysteresis.
Pump: measure ml/s at a few duty cycles, since the duty-to-flow relationship won’t be linear. Remember that duty below 10% does nothing. At low speed it will also be much quieter than the 63-70 dB rating suggests for full speed.
