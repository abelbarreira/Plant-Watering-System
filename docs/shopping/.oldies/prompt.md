The pump is this one

LRIRONG BP200-B46 Brushless Peristaltic Pump 12V
https://cdn.shopify.com/s/files/1/0605/2787/0173/files/BP200_Brushless_motorperistaltic_pump.pdf?v=1763430294

https://cdn.shopify.com/s/files/1/0605/2787/0173/files/BP200_Mini_Peristaltic_Pump-Data_Sheet.pdf?v=1772780959

Pls chekc this table in here

https://www.alibaba.com/product-detail/LRIRONG-BP200-Brushless-Motor-Sanitizer-Detergent_1600440809054.html?spm=a2756.trade-carp.valid-supplier.4.73bd3192irvMXU

 Choose  peristaltic pump
Tube Materials
Silicone tube
BPT
Tube Species
S30
S46
B30
B46
ID×OD
3X5
4X6
3X5
4X6
Flow rate
ml/min
12V/0.8A
110
220
100
190
24V/0.4A
110
220
100
190
Suggested working conditions: Ambient temperature 0-50℃, relative humidity <80%. The above data are all obtained from tests in LEIRONG's laboratory and are for reference only.

Pls analyse in details its specifications about Voltags, Ampares, Calbing, etc



And also check this about our Power Supply for the Pump and the board directly, and the common ground:

https://www.ebay.com/itm/335477433062?var=544917445886
DC-DC 12V TO 3.3V 5V 12V Step Down Power Supply Module Multi Output Voltage New

It is this:
Features
High stability, high cost performance, support 100-240V voltage input, 12V1A output
Double panel design
Beautiful and elegant layout
Input and output use multiple pins, easy to use and connect
Widely used in communication equipment, industrial control motherboards, toys, models, home appliances, car power, etc.
Specification
Module.
One input: DC 6V-12 (input voltage must be more than 1V higher than the voltage to be output)
Three outputs: 3V (±0.2 error),
5.0V(0.2 error)
Current: 800MA (load current must not exceed 800MA),
Input: 12V (12V direct to output)
Double panel design, beautiful and elegant layout;
Input and output use multiple pins, easy to use and connect;
With power indicator (red)
PCB board size:59.5MM*26.5MM
DC interface: 5.5*2.1MM
Adapter.
Voltage input: support 100-240V
Output: 12V 1A
Module List
1 x Module
Module+Adapter List
1 x Module
1 x Adapter

And knowing the micro:bit V2 is giving
https://tech.microbit.org/hardware/edgeconnector/#pins-and-signals

Pls check all the voltages and ampares and those electric things for the GPIOs pins in the V2 we might need


I want for you to be 100% in which specific diode and MOSFET I need, ok, and solve al the questions we have, for exmaple about those PSU

By the way , micro:bit V2  said 3v instad of 3.3v but the "DC-DC 12V TO 3.3V 5V 12V Step Down Power Supply Module Multi Output Voltage New" said 3.3v is there any issue on it?

Checkh the currents as well

and give me one or two spcefic and commoon models of diode and MOSFET I can buy pls


found this

    12V brushless motor 0.6A → B46 → 190 mL/min.

BOARD
    The published specification says approximately:

    Input: 6–12 V
    3.3 V output
    5 V output
    12 V pass-through
    maximum load around 800 mA on the regulated low-voltage outputs
    5.5 × 2.1 mm input
    AMS1117-type linear regulators are used on these versions.

    Therefore I would not use that little PCB as the main high-current distribution point for the pump.

    Take the pump's 12 V directly from the PSU.

