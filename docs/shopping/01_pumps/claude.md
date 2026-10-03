I couldn't find a Danish shop selling a pump with your spec (brushless, PWM and FG, documented). The only pumps that match are Kamoer's, which I found on Amazon and Alibaba. I couldn't confirm a live price or stock on Amazon.de for the brushless versions, so check those yourself before ordering.

Recommendations

1. Kamoer KHS, 12V brushless ("12B"), Norprene tube. This is the best match.

The 12V brushless version draws 0.6 A, and its PWM speed control runs at 10-30 kHz with a 5V amplitude, over a 13%-100% speed range.
robu
Norprene tubing is rated for 1000 h or more, while silicone is only 200 h or more. The tube codes are 16 (3.2 × 6.4 mm) and 40 (4 × 7.2 mm). Both inner diameters are inside your 3.2-4.6 mm range.
s3
The datasheet's flow figures are at least 200 mL/min for N16 and at least 260 mL/min for N40, at full speed. PWM can bring either down to your 140-200 mL/min.
s3
Order code KHS-12B-3-N16 (3.2 mm) or KHS-12B-3-N40 (4 mm). I'd take N16: its full-speed flow is closest to your target, so you get finer control.
The datasheet lists the wiring, including a yellow FG signal feedback wire, a red Vcc wire and a white speed-control wire. That covers your documentation requirement.
directindustry

2. Kamoer KPHM400, 12V brushless, BPT tube.

The KPHM400 brushless version has PWM speed regulation, a BPT tube life of 1000 h, and a yellow speed-feedback wire.
media-amazon
It is a bigger pump (400 mL/min class). I couldn't confirm its tube inner diameter, so check that it is 4.6 mm or less before buying.
Treat it as a fallback to the KHS.

Not recommended: the KPHM100 is too slow for you. It delivers 100 mL/min through a 3 × 5 mm BPT tube rated for over 1000 h. The KPHM600 is too big: it uses a 6.4 mm ID tube and draws 1 A.
amazon
amazon

Where to look, in your order
Denmark: I found nothing. It may be worth emailing a distributor such as Elfa Distrelec or RS and asking about Kamoer.
EU: Funduinoshop in Germany stocks Kamoer, but the model I saw was the KCM stepper pump at €50.38, which isn't what you want. Ask them about the KHS brushless.
funduinoshop
Amazon.de: search "Kamoer KHS brushless 12V" and check the listing says "12B" or "brushless". The KHS listing I found on Amazon.com is the brushed version, so be careful not to buy that one.
amazon
Alibaba: Kamoer's official store lists brush and brushless pumps. Ask for the KHS-12B and its datasheet. Expect VAT on import.
alibaba

Prices are unverified. Kamoer's small pumps tend to cost around $25, about 170 kr, so the KHS should fit your 200-450 kr budget, but check at checkout.

Using it with the micro:bit
Power the pump from a separate 12V supply and join the grounds. Never power it from the micro:bit pins.
The pump expects a 5V PWM signal at 10-30 kHz, and the micro:bit outputs 3.3V. Check the datasheet's logic-high threshold, or add a small level shifter or transistor to be safe.
MakeCode's default PWM period is slow. Set it to about 40 µs (25 kHz) with pins.analogSetPeriod.
On the related KPHM600, duty cycles of 0-10% don't turn the motor. Expect something similar here, and keep your duty cycle above about 13%.
amazon
Read FG on a separate pin and count the pulses. Confirm the pulses per revolution and the output type (open-collector or push-pull) in the datasheet.

If you tell me which Amazon.de or Alibaba listing you find, I can check it against your requirements.