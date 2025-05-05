RTCA, Inc. 

1828 L Street, NW, Suite 805 
Washington, DC 20036 USA 
 
Change No. 3 
 
-to- 
 
RTCA/DO-210D 
MINIMUM OPERATIONAL PERFORMANCE STANDARDS FOR 
GEOSYNCHRONOUS ORBIT AERONAUTICAL MOBILE SATELLITE 
SERVICES (AMSS) AVIONICS ©2006 RTCA, Inc. September 19, 2006 
Copies of this document may be obtained from 
 
RTCA, Inc. 

1828 L Street, NW, Suite 805 
Washington, DC 20036 USA 
 
Telephone:  202-833-9339 
Fax:  202-833-9434 
Internet:  www.rtca.org 
 
Please call RTCA for price and ordering information. 

1. 
Page 7, replace Section 1.3 Operational Applications in its entirety with the following text.  
Retain sections 1.3.1, 1.3.2, 1.3.3 and related subsections without change. 
1.3 
Operational Applications 
 
Many applications for AMSS are potentially available; however, cost or other factors may 
limit users' access to all such applications (e.g., voice as well as data). While applications for 
service categories will evolve with time, this document defines standards to support minimum implementations of all currently foreseen applications for ATS and AOC. Safety services operating with channel types other than those specified in this document are 
expected to be specified by DO-262 and DO-270. 
Since the original publication of this document in 1995, satellite communication technology 
has advanced to the point where a number of services use channel types other than those specified in this document.  This document specifically does not apply to new channel types 
except for the situations in which those channel types share the transmitter capabilities of the "classic" aeronautical channels specified in this document (i.e., P, R, T and C channels).  In 
the condition where transmitter facilities are shared between new channel types and classic 
aeronautical channels, the emissions requirements of this document apply to both sets of channel types. 
 
2. 
Page 19, replace the 3rd and 4th paragraphs of Section 2.2.2 with the following text: 
 
The Transceiver Subsystem is defined to include the transmitter and receiver.  It includes a radio frequency interface at the antenna port, where it connects to the interconnecting cable, 
and baseband interfaces with other on-board avionics equipment.  If a diplexer/LNA is used, 
the transmit filter portion of the diplexer is considered to be part of the transmitter, while the 
receive filter portion of the diplexer and the LNA are considered to be parts of the receiver. The receiver and transmitter are further defined in Sections 2.2.4.1 and 2.2.4.2, with their respective requirements stated in those sections and their subsections. 
 
3. 
Page 35, replace Section 2.2.4.2.5 in its entirety with the following text including the two 
sub-sections: 
2.2.4.2.5 
Harmonics, Discrete Spurious and Noise Density 
 
Transceivers shall meet the Harmonics, Discrete Spurious and Noise Density requirements in either Section 2.2.4.2.5.1 or 2.2.4.2.5.2. 
2.2.4.2.5.1 
Harmonics, Discrete Spurious and Noise Density for Equipment Utilizing 
Intermodulation Frequency Control per Section 2.2.4.2.6.1 
 
For transceivers that meet the requirements in Section 2.2.4.2.6.1 regarding 
frequency selection to control the generation of fifth-order intermodulation products, while transmitting a single modulated signal at the maximum-rated average output power at any frequency per Section 2.2.4.2.10, the composite harmonic, discrete spurious and noise density (including phase noise) at the transmitter output shall not 
exceed the following: 

Composite Harmonic, Discrete Spurious and Noise Density Levels 
 
Frequency (MHz) 
 
Power Density 
  
 
0.01 to 1525 
 
 
-135 dBc/4 kHz 
  
 
1525 to 1559 
 
 
-203 dBc/4 kHz 
  
 
1559 to 1585 
 
 
-155 dBc/MHz 
  
 
1585 to 1605 
 
 
-143 dBc/MHz 
  
 
1605 to 1610 
 
 
-117 dBc/MHz 
  
 
1610 to 1610.6  
 
-95 dBc/MHz 
  
 
1610.6 to 1613.8 
 
-80 dBW/MHz7 
  
 
1613.8 to 1614  
 
-95 dBc/MHz 
  
 
1614 to 1626.5  
 
-70 dBc/4 kHz 
  
 
1626.5 to 1660  
 
-70 dBc/4 kHz2,3,4,6 
  
 
1660 to 1660.5  
 
-49.5 dBW/20 kHz2,4,6,7 

  
 
1660.5 to 1670  
 
-49.5 dBW/20 kHz4,7 
  
 
1670 to 1735 
 
 
-60 dBc/4 kHz 
  
 
1735 to 12000  
 
-105 dBc/4 kHz 
  
 
12000 to 18000  
 
-70 dBc/4 kHz 
 
TABLE NOTES: 
 
1. 
[Deleted.] 
 
2. 
Within the transmit band, excluding the frequency band within ±35 kHz  of 
 
the carrier. 
 
3. 
The -70 dBc/4kHz spectrum level in this table is equivalent to 
 
-70-10 log10(4000/SR) dBe (relative to the maximum envelope) under the 
 
definitions in Section 2.2.4.2.16. 
 
4. 
For wide band spurious the limit is -39.5 dBW/MHz. 
 
5. 
[Deleted.] 
 
6. 
The upper limit for the excess power for any narrow-band spurious 
 
emission (excluding intermodulation products) within a 30 kHz 
 
measurement bandwidth shall be 10 dB above the power limit in this 
 
table. 
 
7. 
Note that the power density is expressed in terms of absolute power 
 
(dBW) in some instances, and in terms of relative to carrier power (dBc)  in 
 
other instances. 
 
NOTES: 
 
1. 
The band 1559 to 1610 MHz is allocated to the Aeronautical 
 
Radionavigation Service (ARNS) and Radionavigation Satellite Service 
 
(RNSS), and is currently utilized by GPS, GLONASS and related 
 
augmentation systems, along with guard bands at the edges. Future 
 
systems developing in these services (e.g., other ARNS/RNSS systems, 

|                                                                                        | augmentation systems) may require the establishment of more stringent    |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
|                                                                                        | protection levels.                                                       |
|                                                                                        |                                                                          |
| 2.                                                                                     | [Deleted.]                                                               |
|                                                                                        |                                                                          |
| 3.                                                                                     | [Deleted.]                                                               |
|                                                                                        |                                                                          |
| 2.2.4.2.5.2                                                                            | Harmonics, Discrete Spurious and Noise Density for Equipment without     |
| Intermodulation Frequency Control per Section 2.2.4.2.6.1                              |                                                                          |
|                                                                                        |                                                                          |
| Transceivers that do not implement the requirements in Section 2.2.4.2.6.1 regarding   |                                                                          |
| frequency selection to control the generation of fifth-order intermodulation products  |                                                                          |
| shall meet the following composite harmonic, discrete spurious and noise density       |                                                                          |
| requirements.                                                                          |                                                                          |
|                                                                                        |                                                                          |
| While transmitting a single modulated signal at the maximum-rated average output       |                                                                          |
| power at any frequency per Section 2.2.4.2.10, the composite harmonic, discrete        |                                                                          |
| spurious and noise density (including phase noise) at the transmitter output shall not |                                                                          |
| exceed the following:                                                                  |                                                                          |
|                                                                                        |                                                                          |
| Composite Harmonic, Discrete Spurious and Noise Density Levels                         |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        | Power Density                                                            |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
| 7                                                                                      |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
| 2,3,4,6                                                                                |                                                                          |
|                                                                                        |                                                                          |
| 2,4,6,7                                                                                |                                                                          |
|                                                                                        |                                                                          |
| 1660.5 to 1670                                                                         |                                                                          |
| 4,7                                                                                    |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |
| NOTE: All Notes and Table Notes contained in  2.2.4.2.5.1 apply to this section as     |                                                                          |
| well.                                                                                  |                                                                          |
|                                                                                        |                                                                          |
|                                                                                        |                                                                          |

4. 

Page 36, replace Section 2.2.4.2.6 in its entirety with the following text including the three sub-sections: 
2.2.4.2.6 
Intermodulation Products 
 
Transceivers shall meet the Intermodulation Products requirements in either Section 
2.2.4.2.6.1 and Section 2.2.4.2.6.2, or else in Section 2.2.4.2.6.3. 

 
2.2.4.2.6.1  
Frequency Control Limiting Fifth-Order Intermodulation Products Transceivers that implement frequency control algorithms for the control of fifthorder intermodulation products shall base those algorithms on the following values for the lowest frequency, fLIM, at which fifth-order intermodulation products may occur, as appropriate for the intended installation and operation of the transceiver. 

 
Transceiver installation / operation Value for fLIM 
 
 
Transceivers used on aircraft equipped with GLONASS 1605 MHz 
 
 
Transceivers used on aircraft not equipped with GLONASS 1585 MHz Transceivers that implement frequency control algorithms for the control of fifthorder intermodulation products, when operating with one or more active Classic Aero H, H+, I, or L channels, or Non-Classic Channels of any type, shall not transmit on a newly-assigned channel frequency that would produce a fifth-order intermodulation product at a frequency at or below fLIM , as defined in this section. 

2.2.4.2.6.2 
Intermodulation Products for Equipment Utilizing Intermodulation Frequency Control per Section 2.2.4.2.6.1 Transceivers that have multi-carrier capability and that meet the requirements of Section 2.2.4.2.6.1 regarding frequency selection control shall meet the following requirement.  When transmitting two equal amplitude unmodulated carriers with a total combined power level up to the Maximum Allowable Multi-carrier Average Output Power of the transmitter, the power level of each intermodulation product shall not exceed the following: 

Maximum Intermodulation Product Levels 
Frequency (MHz) 
IM Level 
Below 1525 
-115 dBc 
1525 to 1559 
-155 dBc 
1559 to 1585 
-135 dBc 
1585 to 1605 
-118 dBc 
1605 to 1610 
-86 dBc 
1610 to 1614 
-64 dBc 
1614 to 1697.5 
-24 dBc 
1697.5 to 1716 
-30 dBc 
1716 to 1735 
-35 dBc 
1735 to 18000 
-85 dBc TABLE NOTE: 1. 
[Deleted.] 
NOTES: 
 
0. 
The requirements in Section 2.2.4.2.6.1 ensure that neither 3rd nor 5th 
 
order intermodulation products can occur below fLIM. 1. 
The Ground Earth Station (GES) should not assign to an AES any 
 
combination of frequencies which would cause the AES to inhibit 
 
transmission. 2. 
The band 1559 to 1610 MHz is allocated to the Aeronautical 
 
Radionavigation Service (ARNS) and Radionavigation Satellite Service 
 
(RNSS) and is currently utilized by the GPS, GLONASS and related 
 
augmentation systems, along with guard bands at the edges.  Future 
 
systems developing in these services (e.g., other ARNS/RNSS systems, 
 
augmentation systems) may require the establishment of more stringent 
 
protection levels. 
 
3. 
[Deleted.] 
 
4. 
[Deleted.] 
 
 
2.2.4.2.6.3 
Intermodulation Products for Equipment without Intermodulation Frequency 
Control per Section 2.2.4.2.6.1 Transceivers that have multi-carrier capability and that do not meet the requirements 
of Section 2.2.4.2.6.1 regarding frequency selection control shall meet the following 
requirement. 

When transmitting two equal amplitude unmodulated carriers with a total combined 
power level up to the Maximum Allowable Multi-carrier Average Output Power of 
the transmitter, the power level of each intermodulation product shall not exceed the following: 
 
Maximum Intermodulation Product Levels 
 
Frequency (MHz) 
IM Level 
Below 1525 
-110 dBc 
1525 to 1559 
-144 dBc 
1559 to 1585 
-135 dBc 
1585 to 1605 
-119 dBc 
1605 to 1610 
-86 dBc 
1610 to 1614 
-64 dBc 
1614 to 1620 
-44 dBc 
1620 to 1625.5 
-34 dBc 
1625.5 to 1728.5 
-24 dBc 
1728.5 to 1735 
-30 dBc 
1735 to 1762.5 
-80 dBc 
1762.5 to 18000 
-85 dBc 
 
NOTE: Notes 1 through 4 of Section 2.2.4.2.6.2 apply to this section. 
5. 
Page 142, in Section 2.4.4.3.6, replace the existing words:  "Measurement Procedure" with 
"Measurement Procedure for Section 2.2.4.2.6.2". Replace the sentence "This test applies only to multichannel transceivers." with the sentence "This test applies only to multichannel transceivers that utilize frequency control per Section 
2.2.4.2.6.1.". In the existing "Step 5" replace "Repeat steps 1 through 5" with "Repeat steps 1 through 4". In the existing "Step 6" replace "Repeat steps 1 through 4" with "Repeat steps 1 through 5". Following the existing "Step 8" add the following: 
Measurement Procedure for Section 2.2.4.2.6.3 This test applies only to multichannel transceivers without frequency control per Section 2.2.4.2.6.1. 
Step 1. After connecting the equipment as shown in Figure 2-29, command the transceiver to 
output a single unmodulated carrier at maximum allowable multi-carrier average power level at the Mid-Band test frequency. 
 
Step 2. Reduce the power output of the channel unit by 3 dB at the transmitter output as 
measured by the power meter. 
 

Step 3. Turn off this carrier and select another channel unit at a frequency separated from the 
first frequency at approximately 1 MHz.  Adjust the new channel unit output level to 
be the same as with the first channel. 
 
Step 4. Turn on the first channel unit again so that both units are operating.  Use the 
spectrum analyzer to measure the intermodulation products resulting from the two signals with the measured single carrier power level as a reference. 
 
Step 5. Repeat Steps 1 through 4 for reduced commanded output levels in 5 dB steps to 15 
dB below maximum allowable output. 
 
Step 6. Repeat Steps 1 through 5 for channel frequency separations of 100 kHz and 10 kHz 
and at the transmit test frequencies specified in Section 2.4.4.1, Item i, at all three 
frequency separations. 
 
Step 7. Repeat Steps 1 through 5 with one carrier tuned to the highest frequency at which the 
transceiver is capable of operating and the other carrier tuned to the lowest frequency at which the transceiver is capable of operating. 
 
 