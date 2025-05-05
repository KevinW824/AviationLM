RTCA, Inc. 

1150 18th Street NW, Suite 910 
Washington, DC 20036 
USA 
Minimum Operational Performance Standards for Traffic Alert and Collision Avoidance System II 
(TCAS II) 
 
Version 7.1 
 
Change 2 RTCA DO-185B: Change 2 March 20, 2013 Prepared by: SC-147 
© 2013 RTCA, Inc. 

Copies of this document may be obtained from 
 
RTCA, Inc. 

1150 18th Street, NW, Suite 910 
Washington, DC 20036, USA 
 
Telephone: 202-833-9339 
Facsimile: 202-833-9434 
Internet: www.rtca.org 
 
Please visit the RTCA Online Store for document pricing and ordering information 

## Executive Summary

Change 2 to DO-185B provides for the following five (5) changes: 

1. Improve the efficiency of the TCAS surveillance function so as to reduce utilization of the 1030 
and 1090 MHz channel without reducing the effectiveness of the equipment's collision avoidance function. 
2. Allow TCAS to implement a narrow band Mode S receive function compatible with the 
RTCA/DO-260B ADS-B receiver requirements without negatively impacting the TCAS receiver function. 
3. Update the flight test requirements to add Atlanta as an alternate location for high density Mode S 
flight testing and to modify the combined air and ground density requirement accordingly. 
4. Decrease the TCAS RA broadcast interval from 8 seconds to 1 second to be compatible with the 
intended use of this data by ground controllers. 
5. Clarify the intent of interference limiting by adding text to the requirements and adding a new 
test. 
 
This Page Intentionally Left Blank
--``````,,,``,,`,`,`,,`,,,```-`-`,,`,,`,`,,`---

## Changes To Volume I

(1.1) 
The following changes to §2.2.2, §2.2.3.6.3, §2.2.4.6.2.2.1, §2.2.4.6.2.2.2, §2.4.4 (Tables 2-69 and 2-70), and creation of §2.4.2.1.7.4.4 reduce TCAS 1030 and 1090 MHz channel utilization. Specifically it reduces unnecessary TCAS interrogations when operating on the airport surface. These changes reduce initial TCAS interrogation power by 10 dB when TCAS is powered-on, and ensures that TCAS aircraft on the ground do not interrogate other on-ground TCAS aircraft while maintaining proper NTA3 and NTA6 counts for TCAS aircraft approaching an airport.  The Mode S surveillance volume is also limited to ± 3000 feet while the TCAS unit is operating on the ground.  Any proposed new text will be highlighted in gray while text intended to be deleted will be marked with red strikethrough font. 

## 2.2.2 System Performance

Note: When operating within the maximum aircraft transponder population and electromagnetic interference levels defined in subparagraph 2.2.1.2, TCAS II will provide a level of performance for active surveillance of targets-of-interest that will support the requirements for generation of collision advisory information. 

 
Specifically, TCAS II will generate a surveillance track in range and altitude on a target-of-interest at the range and with the track probability and range accuracy specified below.  This is to ensure that a correct resolution advisory can be issued in time for the pilot to maintain adequate vertical separation at closest-point-ofapproach. 
--``````,,,``,,`,`,`,,`,,,```-`-`,,`,,`,`,,`---

 
TCAS II will also generate, whenever possible, a surveillance track in range and altitude on a target-of-interest at the range and with the track probability and range accuracy specified below such that a correct traffic advisory can be issued as a precursor to the resolution advisory. 
In addition to the surveillance requirements to support generation of resolution and traffic advisories, TCAS II will display the range and, if available, the altitude 
and bearing position information on targets that generate advisories.  The bearing 
position information will be generated according to the accuracy requirement specified below. 
TCAS II will also generate for display, whenever possible, surveillance range, altitude and bearing position information on Mode C and Mode S aircraft that are within the range specified below and within ±10,000 ft altitude relative to TCAS II when airborne, and within ±3,000 ft altitude relative to TCAS II when on the ground. 

## 2.2.3.6.3 Interrogations From Tcas On The Ground

Whenever the TCAS aircraft determines that it is on the ground, TCAS 
interrogations shall be limited by setting the NTA count in the interference limiting inequalities to a value three times the measured value.  This value will ensure that a TCAS operating on the ground does not add unnecessary 
  
  
  
interference by transmitting at power levels greater than is necessary to provide local area surveillance prior to departure.  The modified value of NTA will provide an approximate surveillance range of 3 NM in the highest density terminal areas to support reliable ground TCAS surveillance of local airborne traffic and a 14 NM range in very low density airspace to provide wide area surveillance in the absence of an SSR.  When TCAS transitions from standby to TA or TA/RA mode and the TCAS aircraft determines that it is on the ground, it shall initialize to the maximum allowed airborne interference limiting values, 10 dB attenuation for Mode S interrogations and 7 dB for Mode C interrogations. 

## 2.2.4.6.2.2.1 Squitter Processing

To reduce the number of unnecessary interrogations, no interrogations shall be transmitted to a target if so few squitters and altitude replies are received from it to indicate an unreliable RF link.  Also, the equipment shall not interrogate for acquisition a target whose altitude is determined from DF=0 or DF=4 replies or continue to interrogate for acquisition a target whose altitude is determined by an active interrogation unless the altitude information indicates that it is within ±10,000 ft of own altitude information indicates that it is not within ±10,000 ft of own altitude when own aircraft is airborne or not within ±3,000 ft of own altitude when own aircraft is on the ground.  Targets that are within ±10,000 ft of own altitude when TCAS II is airborne, or within ±3,000 ft of own altitude when TCAS II is on the ground, and that indicate a reliable RF link are called valid targets.  In order to provide timely acquisition of targets that transition the altitude surveillance boundary, the altitude of targets that are indicated to be outside of ±10,000 ft of own altitude when TCAS II is airborne, or outside of ±3,000 ft of own altitude when TCAS II is on the ground, shall continue to be monitored using DF=0 or DF=4 replies or, in the absence of such replies, by interrogating once every 10 seconds. 

## 2.2.4.6.2.2.2 Acquisition

When a valid acquisition reply is received, the VS field in the reply shall be used to determine whether the aircraft is on the ground as described in 2.2.4.6.1.3. Mode S aircraft that are determined to be on the ground according to the VS field shall be monitored either passively with replies (DF=0 or DF=4) or squitters (CA field of DF=11 or 17).  replies or by actively interrogating.  In the absence of passive monitoring, an active interrogation once every five surveillance update intervals **shall** be used to monitor the air/ground status as long as the aircraft remains on the ground and continues to transmit squitters.  In addition, if own aircraft is airborne and at or below 2000 feet AGL, the range of Mode S aircraft that are determined to be both on the ground, according to the VS field, and TCAS-equipped, according to the TCAS Broadcast Interrogations, shall be measured by using the an active interrogation once every five surveillance update intervals.  Monitored information shall not be made available to the CAS logic. 

## 2.4.4 Cross-Reference Of Requirements And Associated Tests

Add the following rows to Table 2-69: 

| Tests                 | Requirements          |
|-----------------------|-----------------------|
| 2.2.3.6.1             | Interference Limiting |
| Formulas              |                       |
| 2.4.2.1.7.4.4         | Mode S Surveillance   |
| Special Functionality |                       |
| Test                  |                       |
| 2.2.3.6.3             | Interrogations From   |
| TCAS On The Ground    |                       |
| 2.2.4.6.2.2.1         | Squitter Processing   |
| 2.2.4.6.2.2.2         | Acquisition           |

Add the following rows to Table 2-70: 

| Requirements          | Tests                       |
|-----------------------|-----------------------------|
| 2.2.3.6.1             | Interference Limiting       |
| Formulas              |                             |
| 2.4.2.1.7.4.4         | Mode S Surveillance         |
| Special Functionality |                             |
| Test                  |                             |
| 2.2.3.6.3             | Interrogations From TCAS On |
| The Ground            |                             |
| 2.2.4.6.2.2.1         | Squitter Processing         |
| 2.2.4.6.2.2.2         | Acquisition                 |


## 2.4.2.1.7.4.4 Surveillance Special Functionality Test

This test will verify that TCAS is designed to: 

a. Initialize interference limiting at 10dB power attenuation for Mode S 
surveillance and 7dB for Mode C surveillance when powered on while on the ground, §2.2.3.6.3 
b. Limit acquisition of targets to those within an altitude of +/- 3000 feet 
relative to TCAS when operating on the ground,  §2.2.4.6.2.2.1 and §2.2.4.6.2.2.2 
c. Properly interrogate TCAS targets on the ground when own aircraft is 
airborne and at or below 2000 feet AGL and set NTA3 and NTA6 appropriately, §2.2.3.6.1 and §2.2.4.6.2.2.2 

## Inputs

TCAS Aircraft 


Altitude / Radio Altitude 
= 0 ft at T=0 seconds 
Altitude Rate 
 
  
= 0 FPM at T=0 seconds 


= 1000 FPM at T=45 seconds (gradual acceleration to 1000 
FPM permitted) 
On Ground 
= TCAS on ground at T=0 seconds 
In Air 
= TCAS in-air after T=45 seconds 
Sensitivity Level Selection 
= Set to standby before T=0, 
 
Set to TA/RA (Automatic) at T=0. 
 
Intruder Aircraft 1 


Equipage 
 
= TCAS II 
Altitude 
 
= 0 ft 
Altitude Rate 
  
= 0 FPM 
Range  
  
= 0.2 NM at T=0 seconds 
Relative Speed   
= 0 kt at T=0 seconds 


= 200 kt at T=45 Seconds 
 
Intruder Aircraft 2-6 


Equipage 
 
= Mode S 
Altitude 
 
= 500 - 4500 ft in 1000 ft increments 
Altitude Rate 
  
= 0 FPM 
Range  
  
= 15 NM 
Squitter Power  
= -68 dBm 
Relative Speed   
= 0 kt 


 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

Conditions TCAS initialized and operating at T=0 seconds. Scenario Description TCAS initializes to 10dB attenuation on interrogation power and squitter reception sensitivity. Success: 
TCAS does not send acquisition interrogations to targets 2-4 until T=17 seconds and should send acquisition interrogations no later than T=33 seconds.  Verify that the Mode C interrogation sequence power/steps has been reduced by 7dB at the start of the test.  Verify that by T=81, the Mode C interrogation sequence 
power/steps has been restore to full power. 

 TCAS does not interrogate targets for acquisition outside +/- 3000 ft of own altitude when on the ground. Success: 
TCAS does not send acquisition interrogations to targets 5-6 before T=45 seconds. 

TCAS properly interrogates TCAS targets on the airport surface and sets NTA3 and NTA6 appropriately. 
| Success:                                                         |
|------------------------------------------------------------------|
| before T=45 seconds (because own aircraft is on the ground).     |
| NTA6=0 from T=0 to 44 seconds; NTA6=1 from T=45 to 152           |
| seconds; NTA6=0 after T=153 seconds. NTA3=0 from T=0 to          |
| 44 seconds; NTA3=1 from T=45 to 98 seconds; NTA3=0 after         |
| T=99 seconds. Range monitoring interrogations to target 1 shall  |
| not be sent after T=165 seconds.  The NTA numbers expected       |
| above can transition up to 5 seconds later than specified above. |

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

(1.2) 
The following changes to §2.2.4.4.1.1and §2.4.2.1.2.1.1 allow implementation of a narrow band (± 1 MHz) receiver to accommodate a shared TCAS/ADS-B receiver compatible with RTCA/DO-260B without degradation of required TCAS surveillance performance.  Any proposed new text will be highlighted in gray while text intended to be deleted will be marked with red strikethrough font. 

## 2.2.4.4.1 Receiver Sensitivity And Bandwidth 2.2.4.4.1.1 In-Band Acceptance

Given a valid transponder reply signal in the absence of interference or overloads, the minimum trigger level (MTL) is defined as the minimum input power level that results in a 90% ratio of decoded to received replies. 

 
a. The MTL for ATCRBS signals over the frequency range of 1087 to 1093 
MHz shall be -74 dBm ±2 dB. 
 
The MTL for Mode S signals over the frequency range of 1089 to 1091 MHz shall be -74 dBm ±2 dB. Note: This provides adequate link margin for reliable detection of near-coaltitude aircraft in level flight at a range of 14 NM. Note: To accommodate a shared TCAS/ADS-B receiver, a narrow band (1089 to 
1091 MHz) receiver for Mode S signals is acceptable. 
 
b. For an input signal power level of -78 dBm or less, no more than 10% of 
ATCRBS and Mode S signals shall be decoded. 
 
c. The decoding ratio shall be at least 99% for ATCRBS and Mode S signals 
between MTL +3dB and -21 dBm 

## 2.4.2.1.2.1 In-Band Acceptance (2.2.4.4.1.1) 2.4.2.1.2.1.1 Ability To Operate Over The Frequency Band 1087 To 1093 Mhz For Atcrbs And 1089 To 1091 Mhz For Mode S Signals.

These tests verify the ability of the TCAS Receiver to operate over the frequency band 1087 to 1093 MHz for ATCRBS signals and also over the frequency band of 1089 to 1091 MHz for Mode S signals. 

If the antenna gain is not as specified in subparagraph 2.2.4.7.2, each of the reply power levels specified in the tests shall be adjusted to compensate for the difference between the specified antenna gain and the actual antenna gain.  For example, if the antenna gain is three dB below the specified value, each of the reply power levels specified in the test shall be lowered by three dB. 

## Mode C Tests (No Change) Mode S Tests Inputs As Described In 2.4.2.1.2 And Supplemented As Follows:

Intruder Aircraft 
Equipage 
 
=  
Mode S 
Squitter Frequency 
 
 
Scenario A 
= 
1087 MHz 1089 MHz 
 
Scenario B 
=  
1093 MHz 1091 MHz 
Squitter Power 
Scenario A 
= 
-72 dBm 
 
Scenario B 
= 
-72 dBm 

Conditions TCAS initiated and operating at T=0 seconds.  The intruder shall transmit a single squitter during the squitter listening period following the completion of each of the first three whisper-shout sequences and then remain silent. Scenario Description A Mode S intruder is at co-altitude with TCAS and transmits three squitters at a time when the TCAS Receiver is in a squitter listening mode. Success:  TCAS transmits an acquisition interrogation addressed to the ICAO aircraft address contained in the AP field of the squitters within one second following the last squitter (all scenarios terminated at T=10 seconds). Required Probability of Success 
(0.9)3 = 0.73 
--``````,,,``,,`,`,`,,`,,,```-`-`,,`,,`,`,,`---

(1.3) 
The following changes in §3.4.4.2 adds Atlanta as an alternate location for high density Mode S 
flight testing and modifies the combined air and ground density requirement accordingly.  Any 
proposed new text will be highlighted in gray while text intended to be deleted will be marked with red strikethrough font. 

## 3.4.4.2.1 Mode S Surveillance Flight Tests

b. Flight testing shall be accomplished in an area of high Mode S density such as 
Atlanta, Chicago or New York.  Previous tests of TCAS have shown that these areas provide the most stressful environment necessary for evaluation of TCAS Mode S surveillance.  For systems exhibiting air and ground densities, combined 
average air and ground densities of 0.1 A/C per NMI2 in Chicago and 0.12 A/C 
per NMI2 in New York occurred.  For systems exhibiting primarily airborne 
densities, maximum averages of 0.044 A/C per NMI2 in Chicago and 0.042 A/C 
per NMI2 in Atlanta occurred.  Chicago has exhibited a combined air and ground 
average density of 0.1 and New York 0.12.  Chicago has exhibited a maximum NTA of 103 and New York 151.  Atlanta has exhibited a maximum NTA of 126, Chicago 113 and New York 181. Either Atlanta, Chicago or New York are considered adequate to test the Mode S surveillance, however, New York due to its lack of Mode C traffic in the test area and its highest exhibited NTA, will provide the most dense Mode S traffic severe combined average density and NTA environment.  The most effective flight paths have proven to be orbital flights of 5 NM radius near the major airport terminal, Hartsfield in Atlanta, JFK in New York and O'Hare in Chicago. 
 

c. The flight test shall be conducted at an altitude less than 10,000 feet during peak 
traffic periods when ground visibility is greater than 10 NM with a ceiling of at least 11,000 feet to ensure the highest peak traffic densities.  Other locations may be proposed by the applicant and will be considered as a suitable alternative to the above areas if the applicant can demonstrate that the TCAS surveillance test was conducted in an environment whose combined or airborne average density of transponder-equipped aircraft equals or exceeds those of Atlanta, New York or Chicago and indicates a continuous minimum NTA count of 75.  Density is defined as the number of other transponder-equipped aircraft within 10 NM of the TCAS test aircraft divided by the area of a circle of 10 NM radius.  Thirtyone real aircraft targets occurring simultaneously within 10 NM of the TCAS test aircraft is equivalent to a density of 0.1 transponder-equipped aircraft per sq. NM.  Alternate locations must also contain a minimum of three civil ATC or military secondary surveillance radars located within 30 NM of the TCAS aircraft in order to provide an interference environment similar to the above areas. 

 
Note: Although Atlanta, New York and Chicago are presently the highest known densities, future development or test flights may define areas of greater density.  If this occurs, for purposes of maximum system stress, the Mode S Surveillance flight should be flown in these newly defined areas. 

--``````,,,``,,`,`,`,,`,,,```-`-`,,`,,`,`,,`---
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

(1.4) 
The following changes to §2.2.3.10.5.1, §2.2.5.4.1, Table 2-62 in §2.4.2.2.2.2, §2.4.2.2.4.1 and §B.2.3 reduce the RA Broadcast interval from 8 seconds to 1 second in order to be compatible with the intended use of this data by ground air traffic control.   Any proposed new text will be 
highlighted in gray while text intended to be deleted will be marked with red strikethrough font. 

## 2.2.3.10.5.1 Ra Broadcast Interrogations

TCAS shall use the long special surveillance interrogation, UF=16, with UDS=49 and a broadcast address (i.e., 24 ONES) to transmit RA Broadcast Interrogations.  RA Broadcast Interrogations shall be transmitted at full power from the bottom antenna at jittered, nominally 81-second, intervals for the period that the RA is active.  Additionally, one interrogation, indicating RA termination, shall be transmitted immediately after the RA is concluded.  The RA Broadcast Interrogation shall include the MU field as specified in 2.2.3.9.3.2.4.3 and shall describe the most recent RA that existed during the preceding 81-second period. Installations using directional antennas shall operate such that complete circular coverage is provided nominally every 8 1 seconds and the same RA sense and strength is broadcast in each direction. 

Note: This allows RA activity to be monitored in areas where Mode S ground 
station surveillance coverage does not exist by using special RA broadcast signal receivers on the ground.  RA broadcasts are normally destined for ground equipment but are defined as uplink transmissions. 

## 2.2.5.4.1 Communication Of Resolution Advisory Information

Note: TCAS communicates its resolution advisory to the pilot of own TCAS 

aircraft by means of the RA display and aural annunciation subsystems.  
TCAS also communicates its displayed RA to other TCAS-equipped 
aircraft in replies to coordination messages received from those aircraft.  
(This composite RA information is not used by the other TCAS aircraft 
for any purpose other than an acknowledgment that its intent message 
was received.)  TCAS also communicates its composite resolution 
advisory to a Mode S ground sensor by means of a Resolution Advisories 
Report when so requested by the sensor.  In addition, TCAS periodically 
broadcasts its resolution advisory information (RA Broadcast) for 
reception by ground-based systems that may monitor resolution 
advisories in airspaces not covered by full-capability Mode S ground 
sensors.  The RA Broadcast includes the Mode A identity code and 
Mode C altitude code for own aircraft. 

The RA Broadcast begins when the RA is initially issued and is updated and rebroadcast every 8 cycles thereafter until RA termination.  When the RA display ceases in the cockpit, the RA Terminated (RAT) indicator is set and the most recent RA information is broadcast once in the following cycle. 

The Active Resolution Advisories (ARA) field in the RA Broadcast, coordination reply and RA Report contains detailed information on the 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
sense, strength and classification of the displayed RA.  The Multi-threat Encounter (MTE) flag is also included for use in interpreting the contents of the ARA field, depending on the encounter situation.  The RA Report also includes the Threat Type Indicator (TTI) fields and subfields.  
For Mode S threats, TTI contains the ICAO aircraft address; for ATCRBS threats, TTI contains the relative range, altitude and bearing of the most recent threat. 

## 2.4.2.2.2.2 Description Of The End Of Cycle Data Output File

| Output File       | Conditions For    |
|-------------------|-------------------|
| Output File       |                   |
| Parameter         | Inclusion         |
| Parameter         |                   |
| Values            | In Output File    |
| T                 | Any real          |
| number            |                   |
| Included for each |                   |
| cycle of test     |                   |
| Included for each |                   |
| cycle of test     |                   |
| Broadcast_Cycle   | 1, . . . , 8      |
| 1                 |                   |
| ** Version 7.0 ** | Version           |
| number            |                   |
| Included          |                   |
| periodically for  |                   |
| identification    |                   |
| Alt_Layer         | 1, . . . , 6      |
| cycle of test     |                   |
| Effective_SL      | 1, . . . , 7      |
| cycle of test     |                   |
| Climb_Inhibit     | Inhib,            |
| Not_Inhib         |                   |
| Included for each |                   |
| cycle of test     |                   |
| Combined_Contro   |                   |
| l                 |                   |
| Included for each |                   |
| cycle of test     |                   |
| No_Adv,           |                   |
| Cor_Clm,          |                   |
| Cor_Des,          |                   |
| Preventive,       |                   |
| Clear_Conf        |                   |
| Corrective_Climb  | Y, N              |
| cycle of test     |                   |
| Corrective_Descen |                   |
| d                 |                   |
| Y, N              | Included for each |
| cycle of test     |                   |
| Descend_Inhibit   | Inhib,            |
| Not_Inhib         |                   |
| Included for each |                   |
| cycle of test     |                   |
| Inhib,            |                   |
| Not_Inhib         |                   |
| Included for each |                   |
| cycle of test     |                   |
| Increase_Descend  |                   |
| _                 |                   |
| Inhibit           |                   |
| Switch_Own_Trac   |                   |
| ker               |                   |
| Included for each |                   |
| cycle of test     |                   |
| No_Switch,        |                   |
| One_Report,       |                   |
| Two_Reports       |                   |
| Own_Tracker       | Fine_Tracker,     |
| 100ft_Tracker     |                   |
| Included for each |                   |
| cycle of test     |                   |
| Own_Tracker_Sof   |                   |
| tness             |                   |
| 2, . . . , 10     | Own_Tracker =     |
| Fine_Data_Tracker |                   |
| RA_MODE           | Inhibited,        |
| Enabled           |                   |
| Included for each |                   |
| cycle of test     |                   |
|                   |                   |
| CRS State, Variable    | CRS Variable    |
|------------------------|-----------------|
| or Function            | Values          |
| T                      | Any real number |
| Broadcast_Cycle        | 1, . . . , 8    |
| 1                      |                 |
| None                   | None            |
| Alt_Layer              | Layer_1,        |
| Layer_2,               |                 |
| Layer_3,               |                 |
| Layer_4,               |                 |
| Layer_5, Layer_6       |                 |
| Effective_SL           | 1, . . . , 7    |
| Climb_Inhibit          | Inhibited,      |
| Not_Inhibited          |                 |
| Combined_Control       | No_Advisory,    |
| Corrective_Climb       |                 |
| ,                      |                 |
| Corrective_Desce       |                 |
| nd, Preventive,        |                 |
| Clear_of_Conflict      |                 |
| Corrective_Climb       | Yes, No         |
| Corrective_Descend     | Yes, No         |
| Descend_Inhibit      | Inhibited,          |
|----------------------|---------------------|
| Not_Inhibited        |                     |
| Increase_Descend_Inh |                     |
| ibit                 |                     |
| Inhibited,           |                     |
| Not_Inhibited        |                     |
| Switch_Own_Tracker   | No_Switch,          |
| One_Report,          |                     |
| Two_Reports          |                     |
| Own_Tracker          | Fine_Data_Track     |
| er, 100ft_Tracker    |                     |
| 2, . . . , 10        | Own_Tracker_Softnes |
| s                    |                     |
| RA_Mode              | Inhibited,          |
| Enabled              |                     |

## 2.4.2.2.4.1 Transmission Of Ra Report To Mode S Sensor And Ra Broadcast Interrogation To Other Ground Receivers

This test verifies that TCAS correctly determines the TCAS/transponder system capability (either FAA TSO-C119A or RTCA/DO-185A,B compatibility) based on communication with the on-board Mode S transponder and then reports RA information in the appropriate format.  This test requires that TCAS demonstrate proper operation with both FAA TSO-C119A and RTCA/DO-185A,B compatible transponders. 

This test verifies that the TCAS/transponder system correctly: 
 

a. passes RA information from TCAS to the transponder, 
b. indicates to the ground (DR field in DF=4, DF=5, DF=20, and DF=21 
replies) that it has information awaiting downlink, 
c. transmits this information in DF=20, DF=21 replies, d. retains RA information for 18 ±1 seconds following the end of the RA, e. (for RTCA/DO-185A,B compatible systems) properly indicates the end of 
the RA via the RA Terminated indicator, and 
f. properly transmits RA Broadcast Interrogations at 81-second intervals for the 
period that the RA is active.  The RA Broadcast Interrogations describe the most recent RA that existed during the preceding 81-second period. 

## Scenario A

The UUT and an unequipped threat are on a horizontal collision course.  The UUT declares a "Descend" advisory and is asked to communicate it to the Mode S ground sensor. 

## Input:

|                                             | UUT: Z                                     | = 12,000 ft    | at T=0         |
|---------------------------------------------|--------------------------------------------|----------------|----------------|
|                                             | ZDOT                                       | = 0 fpm        | from T=0 to 88 |
|                                             | Mode A code = 5134 (octal)                 |                |                |
| Int1:                                       | Equip                                      | = MODE C       |                |
|                                             | R                                          | = 6.2 NM       | at T=0         |
|                                             | RDOT                                       | = -360 knots   | from T=0 to 88 |
|                                             | Z                                          | = 12,200 ft    | from T=0 to 88 |
|                                             | ZDOT                                       | = 0 fpm        | from T=0 to 88 |
|                                             | Msgs                                       | = None         |                |
| MSS: Msgs                                   | = UF=4, with RR=0 from T=0 to 88, every 4s |                |                |
| UF=4, with RR=19 from T=0b to 88b, every 4s |                                            |                |                |

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

## Expected Output:

Display: "Descend" from T=31 to T=65  

Note: If bit 12 in DF=4 (at T=84a) is zero, the MB field in DF=20 (at T=84c) 
should have BDS=48 followed by 48 zeros.  If bit 12 in DF=4 (at T=84a) is one, the MB field in DF=20 (at T=84c) should contain the same information found at T=80c. 
When testing with an FAA TSO-C119A compatible Mode S transponder: 

Msgs: DF=4 with bit 12 cleared at T=0a, 4a, 8a, …, 28a 
DF=4 with bit 12 set at T=32a, 36a, …, 80a 
 
DF=4 with bit 12 cleared at T=84a, 88a 
 
DF=20, in MB: BDS=48 followed by 48 0s at T=0c, 4c, …, 28c 
 
DF=20, in MB: BDS=48, ARA=00000100000000, RAC=0000 at T=32c, 36c, …, 80c 
 
DF=20, in MB: BDS=48, ARA=0, RAC=0 at T=84c, 88c 
 
UF=16, in MU: UDS=49, ARA=11100010000000, RAC=0000, RAT=0, MTE=0, AID=1010010011100, CAC=0011000101010 at T=31, 39, 47, 55, 63       32, … 64, 65 
 
Note: The position of the UF=16 msg relative to the other messages in a 
given one-second interval is not important. 
 
UF=16, in MU: UDS=49, ARA=11100010000000, RAC=0000, RAT=1, MTE=0, AID=1010010011100, CAC=0011000101010 at T=66 
When testing with an RTCA/DO-185A,B compatible Mode S transponder: 

Msgs: DF=4 with bit 12 cleared at T=0a, 4a, 8a, …, 28a 
DF=4 with bit 12 set at T=32a, 36a, …, 80a 
 
DF=4 with bit 12 cleared at T=84a, 88a 
 
DF=20, in MB: BDS=48 followed by 48 0s at T=0c, 4c, …, 28c 
 
DF=20, in MB: BDS=48, ARA=11100010000000, RAC=0000, RAT=0, MTE=0, TTI=2, TIDA=alt, TIDR=rng, TIDB=brg at T=32c, 36c, …, 64c 
 
DF=20, in MB: BDS=48, ARA=11100010000000, RAC=0000, RAT=1, MTE=0, TTI=2, TIDA=alt, TIDR=rng, TIDB=brg at T=68c, 72c, …, 80c 
 
DF=20, in MB: BDS=48, followed by 48 0s at T=84c, 88c 
 
UF=16, in MU: UDS=49, ARA=11100010000000, RAC=0000, RAT=0, MTE=0, AID=1010010011100, CAC=0011000101010, 
AP address*=FFFFFF16 at T=31, 39, 47, 55, 6332, … 64, 65 
 
Note: The position of the UF=16 msg relative to the other messages in a 
given one-second interval is not important. 
  
  

 
UF=16, in MU: UDS=49, ARA=11100010000000, RAC=0000, RAT=1, MTE=0, AID=1010010011100, CAC=0011000101010, 
AP address*=FFFFFF16 at T=66 
 
* i.e., address before parity overlay added and after parity overlay removed 

## Scenario B

The UUT and TCAS II-equipped threat are on a horizontal collision course. The threat declares the conflict and selects a "Descend" advisory. Subsequently, the UUT declares the conflict and selects a "Climb." The test verifies that the proper resolution advisory data is successfully transmitted to the ground sensors. 

## Input:

|    | UUT: Z      | =    | 12,200 ft    | at T=0         |
|----|-------------|------|--------------|----------------|
|    | ZDOT        | =    | 0 fpm        | from T=0 to 90 |
|    | Mode A code | =    | 2760 (octal) |                |

--``````,,,``,,`,`,`,,`,,,```-`-`,,`,,`,`,,`---

| Int1:                                       | Equip    | =                                        | TCAS II                             |                 |
|---------------------------------------------|----------|------------------------------------------|-------------------------------------|-----------------|
|                                             | R        | =                                        | 6.2 NM                              | at T=0          |
|                                             | RDOT     | =                                        | -360 knots                          | from T=0 to 90  |
|                                             | Z        | =                                        | 12,000 ft                           | from T=0 to  90 |
|                                             | ZDOT     | =                                        | 0 fpm                               | from T=0 to 90  |
|                                             | Msgs     | =                                        | UF=16, in MU: UDS=48, MTB=0, CVC=0, |                 |
| VRC=1, CHC=0, HRC=0, VSB=14, MID=2 from     |          |                                          |                                     |                 |
| T=26 to 60                                  |          |                                          |                                     |                 |
| MSS: Msgs                                   | =        | UF=4, with RR=0 from T=0 to 88, every 4s |                                     |                 |
| UF=4, with RR=19 from T=0b to 88b, every 4s |          |                                          |                                     |                 |

## Expected Output:

Display:  "Climb" from T=30 to 64 
Note: If bit 12 in DF=4 (at T=84a) is zero, the MB field in DF=20 (at T=84c) 

should have BDS=48 followed by 48 zeros.  If bit 12 in DF=4 (at T=84a) is one, the MB field in DF=20 (at T=84c) should contain the same information found at T=80c. 
When testing with an FAA TSO-C119A compatible Mode S transponder: 

Msgs: DF=4, with bit 12 cleared at T=0a, 4a, 8a, …, 28a 
DF=4, with bit 12 set at T=32a, 36a, …, 80a 
 
DF=4, with bit 12 cleared at T=84a, 88a 
 
DF=20, in MB: BDS=48 followed by 48 0s at T=0c, 4c, …, 24c 
 
DF=20, in MB: BDS=48, ARA=00000000000000, RAC=X000, at T=28c      (X=don't care) 
 
DF=20, in MB: BDS=48, ARA=10000000000000, RAC=1000, at T=32c, 36c, …, 80c 
 
DF=20, in MB: BDS=48 followed by 48 0s at T=84c, 88c 
 
UF=16, in MU: UDS=49, ARA=11000010000000, RAC=1000, RAT=0, MTE=0, AID=0101110110000, CAC=1001000101010 at T=30, 38, 46, 54, 6231, … 63, 64  
 
Note: The position of the UF=16 msg relative to the other messages in 
a given one-second interval is not important. 
 
UF=16, in MU: UDS=49, ARA=11000010000000, RAC=1000, RAT=1, MTE=0, AID=0101110110000, CAC=1001000101010 at T=65 
When testing with an RTCA/DO-185A,B compatible Mode S transponder: 

Msgs: DF=4, with bit 12 cleared at T=0a, 4a, 8a, …, 28a 
DF=4, with bit 12 set at T=32a, 36a, …, 80a 
 
DF=4, with bit 12 cleared at T=84a, 88a 
 
DF=20, in MB: BDS=48 followed by 48 0s at T=0c, 4c, …, 24c 
 
DF=20, in MB: BDS=48, ARA=00000000000000, RAC=X000, RAT=0, MTE=0, TTI=0, TID=0 at T=28c     (X=don't care) 
 
DF=20, in MB: BDS=48, ARA=11000010000000, RAC=1000, RAT=0, MTE=0, TTI=1, TID=2 at T=32c, 36c, …, 64c 
 
DF=20, in MB: BDS=48, ARA=11000010000000, RAC=1000, RAT=1, MTE=0, TTI=1, TID=2 at T=68c, 72c, …, 80c 
 
DF=20, in MB: BDS=48 followed by 48 0s at T=84c, 88c 
 
UF=16, in MU: UDS=49, ARA=11000010000000, RAC=1000, RAT=0, MTE=0, AID=0101110110000, CAC=1001000101010, 
AP address*=FFFFFF16 at T=30, 38, 46, 54, 6231, … 63, 64  
 
Note: The position of the UF=16 msg relative to the other messages in 
a given one-second interval is not important. 
 
UF=16, in MU: UDS=49, ARA=11000010000000, RAC=1000, RAT=1, MTE=0, AID=0101110110000, CAC=1001000101010 
AP address*=FFFFFF16 at T=65 
 
* i.e., address before parity overlay added and after parity overlay removed 

## B.2.3 Ra Broadcast Interrogation Messages

UF=16 interrogations are also used to transmit RA Broadcast Interrogation Messages.  These interrogations are transmitted every 8 1 seconds by a TCAS processor for the period that an RA is active.  This allows RA activity to be monitored in areas where Mode S ground station surveillance coverage does not exist by using special RA broadcast signal receivers on the ground.  RA Broadcast Interrogations are defined as uplink transmissions but are normally destined for ground equipment.  In the RA Broadcast Interrogation, the 56-bit message field describes the most recent RA that existed during the preceding 8 1 second period. The message field also includes the most recent Mode A and Mode C codes transmitted by the associated Mode S transponder. 

(1.5) The following changes to §2.2.3.6.1, §2.4.4 (Tables 2-69 and 2-70), and creation of the new test 
in §2.4.2.1.7.4.5 insure that interference algorithms limit maximum power and minimum sensitivity, but do not limit the number of interrogations in any surveillance cycle for intruders in the communication range defined by those limits.  Any proposed new text will be highlighted in 
gray while text intended to be deleted will be marked with red strikethrough font. 

## 2.2.3.6.1 Interference Limiting Formulas

Notes: 3. 
The three interference limiting inequalities are designed to check if the current Mode C and Mode S surveillance are aligned with the goals of the TCAS contribution to the communication environment as a system, 
which are stated in note 2 above. The inequalities are not meant to restrict individual interrogations, but rather modify Mode C and Mode S surveillance parameters so that the inequalities can be satisfied in the future. The procedures in §2.2.3.6.1 describe how to modify Mode C and Mode S surveillance for interference limiting. 
 

## 2.4.4 Cross-Reference Of Requirements And Associated Tests

Add the following rows to Table 2-69: 

| Tests                   | Requirements              |
|-------------------------|---------------------------|
| 2.4.2.1.7.4.5           | Interference Limiting and |
| Required Interrogations |                           |
| 2.2.3.6.2               | Interference Limiting     |
| Procedures              |                           |

 Add the following rows to Table 2-70: 

Requirements 
Tests 

--``````,,,``,,`,`,`,,`,,,```-`-`,,`,,`,`,,`---

| 2.2.3.6.2               | Interference Limiting     |
|-------------------------|---------------------------|
| Procedures              |                           |
| 2.4.2.1.7.4.5           | Interference Limiting and |
| Required Interrogations |                           |

## 2.4.2.1.7.4.5 Interference Limiting And Required Interrogations

This test will verify that TCAS is designed to send interrogations as required in §2.2.4.6 while in maximum interference limiting. Inputs and Conditions Create an aircraft environment that will cause TCAS to enter the maximum interference limiting, 10dB for Mode S. This shall be done by having a sufficiently high NTA count, sufficient Mode C traffic to require a high resolution whisper shout sequence in all four antenna quadrants, and multiple Mode S targets in communication range. 

## Scenario Description Tcas Must Be Airborne For This Test. Tcas Will Follow The Interference Limiting Procedures Until 10Db Of Mode S Interrogation Power And Receiver Sensitivity Attenuation Is Reached. The Conditions Below Must Then Be Met. Success: The Power Sum For The Left Hand Side Of Interference Limiting Inequality 1 Consistently Exceeds The Right Hand Side Determined By Nta. All Targets Within Communication Range Are Interrogated And Tracked As Required In §2.2.4.6 2 Changes To Pseudocode

(2.1) 
The following changes to Attachment A of Volume 2 reduce the RA broadcast inteval from 8 seconds to 1 second to be compatible with the intended use of this data by ground controllers. Any proposed new text will be highlighted in gray while text intended to be deleted will be marked with red strikethrough font. 

## Volume 2 Attachment A

NAME  
 
 
SECTION 
CONTEXT 

      NOMINAL 


(STRUCTURE GROUP) 
 
       VALUE 
PR_NOISE 
4 
TRACKVAR.horizontal 
 
PREVINCREASE 
2 
G.display 
 
PREVIOUS_RZ 
2 
ITF.position 
 
PREVMTE 
2 
G.broadcast 
 
PREVRA 
2 
G.broadcast 
 
PROCNOIVAR 
2 
P.mdf 
2.56 ft2/sec4 
PROJ_ZINT 
6 
RESVAR.modeling 
 
PROJ_ZINT 
7 
DISPVAR.crossing_RA 
 
PROX_TEST 
7 
TRAFVAR.flags 
 
PROXA 
2 
P.traffic 
1200 ft 
PROXR 
2 
P.traffic 
6 nmi 
PRV_AID 
2 
BRDCST_DATA.final_broadcast 
 
PRV_ARA 
2 
BRDCST_DATA.final_broadcast 
 
PRV_CAC 
2 
BRDCST_DATA.final_broadcast 
 
PRV_MTE 
2 
BRDCST_DATA.final_broadcast 
 
PRV_RAC 
2 
BRDCST_DATA.final_broadcast 
 
PRXHITA 
7 
TRAFVAR.flags 
 
PTABLEH(0:63) 
2 
P.coordination 
See Table 3-3 
PTABLEV(0:15) 
2 
P.coordination 
See Table 3-2 
Q 
2 
N.general 
 
QSIGN 
4 
TRACKVAR.vertical 
 

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

| QUANT    |   4  | TRACKVAR.vertical    |       |
|----------|------|----------------------|-------|
| QUIKREAC |   2  | P.model              | 2.5 s |
| R        |   2  | ITF.position         |       |
| RA(14)   |   2  | G.resolution         |       |
| RABRDCST |   2  | P.delay              | 8     |
|          |      |                      |       |
|          |      |                      |       |
|          |      |                      |       |

## Changes To State Charts

(3.1) 
The following changes to §1.3.8, Figure 2-3 in §2.1, Note after Figure 2-22 in §2.1.13, CAS Functions 4.61 and 4.86 reduce the RA broadcast inteval from 8 seconds to 1 second to be compatible with the intended use of this data by ground controllers.  Any proposed new text will be highlighted in gray while text intended to be deleted will be marked with red strikethrough font. 

## 1.3.8 Interface:  Ra_Broadcast_Message

 
Source:  CAS 

 
Destination:  TCAS_Transmitter 

 
Trigger Event:  Send_RA_Messagee-C4 

 
Condition: 

|                      |          |     |   OR  |
|----------------------|----------|-----|-------|
|                      |          |     |       |
| Composite_RA         |          |     |       |
| s-111                |          |     |       |
|                      | in state | RA  |       |
|                      |          |     |       |
| T                    |          |     |       |
|                      |          |     |       |
| F                    |          |     |       |
| AND                  |          |     |       |
| PREV(Broadcast_Cycle |          |     |       |
| s-141                |          |     |       |
| )                    | in state |     |     8 |
|                      |          |     |       |
| T                    |          |     |       |
|                      |          |     |       |
| ˜                    |          |     |       |
|                      |          |     |       |
|                      |          |     |       |
| PREV(Composite_RA    |          |     |       |
| s-111                |          |     |       |
| )                    | in state | RA  |       |
|                      |          |     |       |
| ˜                    |          |     |       |
|                      |          |     |       |
|                      |          |     |       |
| T                    |          |     |       |

 
Output Action:  SEND(RA_Broadcast_Message(ARA, VRAC, HRAC, RAT, MTE, Own_Mode_A_Addressv-56, CAC)) 

 
Assignments:  None 

 
Abbreviations: 

 
ARA = 

Version_7_ARAf-587 
if Composite_RAs-111 **in state**  RA 
Otherwise 
PREV(Version_7_ARAf-587) 

VRAC = 

Vertical_RACv-68 
if Composite_RAs-111 **in state**  RA 
Otherwise 

PREV(Vertical_RACv-68) 
 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

HRAC = 
Horizontal_RACv-70 
if Composite_RAs-111 **in state**  RA 
Otherwise 
PREV(Horizontal_RACv-70) 

MTE = 

Multiple_Threatsm-403 
if Composite_RAs-111 **in state**  RA 
Otherwise 
PREV(Multiple_Threatsm-403) 

 
--``````,,,``,,`,`,`,,`,,,```-`-`,,`,,`,`,,`---

## 2.1 Own Aircraft Own_Aircraft Input:

Alerter_Data_Available: {True, False}
| Own_Alt_Radio: {-20 ... 2,720}                          | Traffic_Display_Permitted: {True, False}                |
|---------------------------------------------------------|---------------------------------------------------------|
| Ground_Level: Real {Range Unspecified}                  | Aircraft_Altitude_Limit: Real {Range Unspecified}       |
| Own_Alt_Barometric: {-1200 to limit of Altimeter}       | Mode_Selector: {TA/RA, Standby, TA_Only, 3, 4, 5, 6, 7} |
| Config_Climb_Inhibit: {True, False}                     | Own_Corrected_Altitude: Real {Range Unspecified}        |
| Altitude_Climb_Inhib_Active: {True, False}              | Radio_Altimeter_Status: {Valid, Not_Valid}              |
| Increase_Climb_Inhibit_Discrete: {True, False}          | Own_Mode_S_Address: {1 ... (2                           |
| 24                                                      |                                                         |
| - 2)}                                                   |                                                         |
| TCAS_Operational_Status: {Operational, Not_Operational} | Own_Mode_A_Address: {0 ... (2                           |
| 13                                                      |                                                         |
| - 1)}                                                   |                                                         |

## Output:

VSL500, Negative, Positive} Own_Goal_Alt_Rate: {-4,400 ... 4,400}
Corrective_Descend, Preventive, Clear_of_Conflict} 
Vertical_RAC: {None, Dont_Climb, Dont_Descend, Dont_Climb_Dont_Descend} Horizontal_RAC: {None, Dont_Turn_Left,
| Climb_RA: {No_Climb_RA, VSL2000,VSL1000,   | Dont_Turn_Right, Dont_Turn_Left_Dont_Turn_Right}   |
|--------------------------------------------|----------------------------------------------------|
| VSL500, Negative, Positive}                | Crossing_Out: {True, False}                        |

## 2.1.13 Broadcast_Cycle

Note: **Description:** The Broadcast_Cycle state implements a countdown which controls broadcast or RA broadcast message through the TCAS 1030 MHz transmitter whenever a resolution advisory is in progress.  The RA broadcast message is sent from TCAS to the TCAS transmitter when the Broadcast_Cycle state has value 8 1. 

 

## 2.1.13 **Own Aircraft**

| Transition(s):   |     |
|------------------|-----|
| 8                |     |
| o                |     |
|                  |     |
| 7                |     |
|                  |     |
| 7                |     |
| o                |     |
|                  |     |
| 6                |     |
|                  | 6   |
| o                |     |
|                  |     |
| 5                |     |
|                  | 5   |
| o                |     |
|                  |     |
| 4                |     |
|                  | 4   |
| o                |     |
|                  |     |
| 3                |     |
|                  | 3   |
| o                |     |
|                  |     |
| 2                |     |
|                  | 2   |
| o                |     |
|                  |     |
| 1                |     |
|                  | 1   |
| o                |     |
|                  |     |
| 8                |     |
|                  |     |
| 1                |     |
| o                |     |
|                  | 1   |
|                  |     |

Location:  Threats-207  Broadcast_Cycles-141 
Trigger Event:  Composite_RA_Evaluated_Evente-C2 
Condition: 

 
Composite_RAs-111 in state RA 
 T 
Output Action:  None Notes: 
1. 
Description:  Restart the countdown (i.e., transition from 8**1 to** 71) whenever a resolution advisory is in progress.  Cycle through the broadcast counter values when triggered by the Composite_RA_Evaluated event. 
2.  
Pseudocode Reference:  Broadcast. 
Transition(s): 
Any 
o 
81 
Location:  Threats-207  Broadcast_Cycles-141 

Trigger Event:  Composite_RA_Evaluated_Evente-C2 

| Condition:     |          |
|----------------|----------|
|                |          |
| Composite_RA   |          |
| s-111          |          |
|                | in state |
| T              |          |
| Output Action: | None     |
| Notes:         | 1.       |
|                | 2.       |

## 4.61 Function: New_Threat_Type

Return Type:  Enumerated Units:  N/A Range:  {None, ATCRBS, ModeS} Definition: New_Threat_Type = 
­ ° ° ° ®
 
ATCRBS ModeS None PREV(New_Threat_Typef-545) 

if there exists an i such that: 
(Other_Aircrafts-157 [i]  Statuss-261 **in state** New) and (Other_Aircrafts-157 [i]  Other_Capabilityv-164 = ATCRBS) if there exists an i such that: 
(Other_Aircrafts-157 [i]  Statuss-261 **in state** New) and 
(Other_Aircrafts-157 [i]  Other_Capabilityv-164 z ATCRBS) 
 
if (Composite_RAs-111 **in state** No_RA) and (PREV(Broadcast_Cycles-141) in state 8 1) and 
(PREV2(Broadcast_Cycles-141) **in state** 1) Otherwise 

° ° ° ¯
 

Notes: 
1. 
Description:  Returns the secondary surveillance radar (SSR) transmission capability (Mode S or ATCRBS) of a new threat if there is one.  When the Broadcast Cycle Counter has just been reset to 8 1, its highest value (which permits broadcast of a resolution message), but if the composite resolution advisory is in the 'No_RA' state, then the new threat type is set to 'none'. 
  
2. 
Pseudocode Reference:  Broadcast, Store_threat_info. 

## 4.86 Function: Threat_Id

Return Type:  Integer Units:  Dimensionless Range:  {0 ... (224  1)} 
Definition: Threat_ID = 

 
BITS_1_13(Latest_Threatf-536) ˜ 213 + 
if (Composite_RAs-111 **in state** RA) and 
(Other_Aircrafts-157 [Latest_Threatf-536]  
Other_Capabilityv-164 = ATCRBS) 
BITS_14_20(Latest_Threatf-536) ˜ 26 + 
BITS_21_26(Latest_Threatf-536) 
 
Other_Aircrafts-157 [Latest_Threatf-536] 
Other_Mode_S_Addressv-160 ˜ 22 
if (Composite_RAs-111 **in state** RA) and 
(Other_Aircrafts-157 [Latest_Threatf-536]  
Other_Capabilityv-164 z ATCRBS) and 
(Other_Aircrafts-157 [Latest_Threatf-536]  
Statuss-261 **in state** New) 
 
0 
if (Composite_RAs-111 **in state** No_RA) and 
(PREV(Broadcast_Cycles-141) in state 8 1) and 
(PREV2(Broadcast_Cycles-141) **in state** 1) 
 
PREV(Threat_IDf-575) 
Otherwise 

Abbreviations: BITS_1_13(i) = 

| Gillham             |                |
|---------------------|----------------|
| s-157               |                |
| [i]                 |                |
|                     |                |
| Other_Alt           |                |
| v-159               |                |
|                     |                |
| BITS_14_20(i) =     |                |
| Coded               | Other_Aircraft |
| s-157               |                |
| [i]                 |                |
|                     |                |
| Other_Tracked_Range |                |
| f-554               |                |
|                     |                |

BITS_21_26(i) = 

| Coded               | Other_Aircraft   |
|---------------------|------------------|
| s-157               |                  |
| [i]                 |                  |
|                     |                  |
| Other_Bearing       |                  |
| v-                  |                  |
| ­                    |                  |
| ®                   |                  |
| °                   |                  |
| ¯                   |                  |
| °                   |                  |
| 171                 |                  |
|                     |                  |
|                     |                  |
| 0                   |                  |
| if                  | (Other_Aircraft  |
| s-157               |                  |
| [i]                 |                  |
|                     |                  |
|                     |                  |
| Other_Bearing_Valid |                  |
| v-173               |                  |
| = True              |                  |
|                     |                  |
| Otherwise           |                  |
|                     |                  |
|                     |                  |

 
This Page Intentionally Left 
 

## 4 Changes To Tsim

 TSIM has not been updated to generate new output data.  Consequently, the variable Broadcast_Cycle will take on the value of 1 for every cycle, not conforming to values contained on the CD. This discrepancy should be noted as acceptable, so that deviations or further justifications are not needed. 

 
This Page Intentionally Left Blank 