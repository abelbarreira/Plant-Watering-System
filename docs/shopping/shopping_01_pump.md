# Pump

## Description

I want to buy Peristaltic Pump for watering a plant with clean water
12 V brushless motor
Around ~0.6 A [it can also be more or less than this]
PWM
Five wire PWM/FG interface
Flow: between 140 to 200mL/min [it can also be more or less]
Noise ≤60dB

Tubing: from 3,2mm to 4,6mm internal diameter with life >=1000h (Neoprene or BPT a last choice silicone)
Available in Denmark/EU with documented PWM and FG feedback, with technical documentation
    This is important, that we want to have available PWM and FG feedback, with its technical documentation

Between 200kr and 450kr danish krone

My idea is control it with a BBC micro:bit v2
https://tech.microbit.org/hardware/edgeconnector/#pins-and-signals

Pls find it in places in Denmark only first, then Amazon.de, then Alibaba, the Aliexpress, then eBay etc

Give two or three models you recommend

## Some models

Kamoer KPHM200-12B3
Kamoer KPA200-12B-B16
Simply Pumps PMB200N eBay

## Links

Pump Kamoer KPHM100
https://www.alibaba.com/product-detail/Kamoer-KPHM100-Low-Flow-Brushless-brushed_1600308101707.html?spm=a2700.prosearch.normal_offer.d_title.204f67afquyZlQ&priceId=48ab3c73d2b842229a95e3d30304ca3e

    Pump INTLLAB+12+V+DC+peristaltic+pum
    https://www.ebay.com/itm/317750278753?_skw=INTLLAB+12+V+DC+peristaltic+pump&itmmeta=01M3F56HH32B27VHGQT108V7GS&hash=item49fb647a61:g:dMwAAeSw-4hpYfam&itmprp=enc%3AAQALAAABAGfYFPkwiKCW4ZNSs2u11xCFLzuukr6hIPyXSmP8JyL4XDwFfCJR8jRnxWXkGbVep7Iy6nPW0XrUJKlCsYLcz%2B%2FhHnaUFRuinVSB4Laqed%2FoDxRJcsBNQgF8HR8W6el7ZytcUgYPrej3RGNgshPS56EOts2g%2FcK1t4QOmH4ikliRmiJ9a0HAzaor7Ddiad5B1tSUm3ijtRxgI4tjdXFIf9PzOMPbEw%2BwwALimHcIwNnjvONeXDyxTVNG2acDeV9u26DpcszDp%2BWm2bC94p4VwWlLazkTw%2FYU6sLz4we2WHOTi3FHsV41FUty27yunQHfosI8IhG0InwkKq4IYi5NpQA%3D%7Ctkp%3ABk9SR9yYmuWbaA

## Others

1. Pump → 4×6 mm tubing connection
I don't want to guess this adapter. We should establish the actual KPHM100 outlet/barb specification from the seller/manual first.
    >>>>> THIS ONE
    3 mm ID × 5 mm OD tube → 4 mm ID × 6 mm OD tube barbed reducer

2. Pump electronics
    You'll need a proper low-side MOSFET driver.

    We'll select:
        logic-level N-MOSFET
        flyback diode
        100 Ω gate resistor
        10 kΩ gate pulldown
        fuse
        screw terminals
        suitable wire
        connectors

        Because the KPHM100 HE is the 12 V brushless version, we should verify its actual operating current before choosing the final power supply and protection.

## Oldies

I'm thinking to build this watering system:

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
                D1      D2

Where

Pump
https://www.alibaba.com/product-detail/LRIRONG-BP200-Brushless-Motor-Sanitizer-Detergent_1600440809054.html?spm=a2756.trade-carp.valid-supplier.4.73bd3192irvMXU
LRIRONG BP200 Brushless Motor BP200-B46 12V

4×6 mm BPT is Leirong Pharmed BPT 1 meter
https://www.alibaba.com/product-detail/Leirong-Pharmed-Bpt13-14-19-16_1600516723013.html?spm=a2756.trade-carp.valid-supplier.3.73bd3192irvMXU

which is connected directly to the pump, two part, hafl meter each

Then
https://www.alibaba.com/product-detail/LeiRong-10mm-Plastic-3-Way-Y_1601763205000.html?spm=a2756.trade-carp.valid-supplier.2.73bd3192gf7VK6

Size: 5/32"
For the Y-Shape (x2) and L-Shape connectors (x1)

Then this for the silicon
https://www.alibaba.com/product-detail/LEIRONG-High-Quality-Silicone-Gel-Lab_1600527088464.html?spm=a2756.trade-carp.valid-supplier.5.73bd3192gf7VK6
LEIRONG High Quality Silicone Gel Lab Food Medical Grade Peristaltic Pump Silicone Tube
4x6 mm Silicon Tube

And then this Dripper
https://www.ebay.com/itm/262860481111?var=561859474552

Antelco Ceta Pressure Compensating Dripper Emitter 4L/h 4mm Micro Irrigation PC

