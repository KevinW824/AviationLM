# Aerospace Standard Electronic Flight Instrument System (Efis) Displays

## Rationale

Historically, FAA Technical Standard Orders (TSOs) and associated industry Minimum Operational Performance Specifications (MOPS) were developed to address sensor and indicator requirements for single functions, such as airspeed, altitude, or fuel flow.  In contrast, modern Electronic Flight Instrument System (EFIS) displays normally present indications for multiple functions, but do not normally include the sensor. Until now, a MOPS did not exist to address the operational/functional requirements for such an EFIS display.   
Requirements for this type of EFIS typically consist of a few requirements for each function, drawn from many TSOs and associated MOPS.   As a result, TSO applications for EFIS displays have multiple deviations to many TSOs and may include incomplete TSO authorizations.  This document is intended to facilitate EFIS TSO authorizations by addressing only the EFIS display requirements for a broad set of aircraft functions. This document provides criteria for EFIS displays that are intended for use in the flight deck by the flight crew in aircraft to include, but not limited to, Title 14 CFR Part 23, 25, 27, and 29. 

 
__________________________________________________________________________________________________________________________________________ SAE Technical Standards Board Rules provide that: "This report is published by SAE to advance the state of technical and engineering sciences. The use of this report is entirely voluntary, and its applicability and suitability for any particular use, including any patent infringement arising therefrom, is the sole responsibility of the user." All rights reserved. No part of this publication may be reproduced, stored in a retrieval system or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of SAE. 

TO PLACE A DOCUMENT ORDER: 
Tel:        877-606-7323 (inside USA and Canada) 
 
Tel:        +1 724-776-4970 (outside USA) 
 
Fax:       724-776-0790 
 SAE values your input. To provide feedback on this Technical Report, please visit http://www.sae.org/technical/standards/AS6296 
Email:    CustomerService@sae.org http://www.sae.org 

## Table Of Contents

| 1.     | SCOPE                                                   |    5  |
|--------|---------------------------------------------------------|-------|
|        |                                                         |       |
| 2.     | REFERENCES                                              |    6  |
| 2.1    | Applicable Documents 6                                  |       |
| 2.1.1  | SAE Publications                                        |    6  |
| 2.1.2  | Code of Federal Regulations (CFR) 7                     |       |
| 2.1.3  | RTCA/EUROCAE Publications 7                             |       |
| 2.2    | Related Informational Publications 8                    |       |
| 2.2.1  | SAE Publications                                        |    8  |
| 2.2.2  | FAA Reference Documents 9                               |       |
| 2.2.3  | RTCA/EUROCAE Publications 11                            |       |
| 2.3    | Definitions 11                                          |       |
|        |                                                         |       |
| 3.     | GENERAL STANDARDS                                       |   11  |
| 3.1    | Material 11                                             |       |
| 3.1.1  | Workmanship 12                                          |       |
| 3.2    | Compatibility of Components 12                          |       |
| 3.3    | Equipment Functions and Mechanical Operations 12        |       |
| 3.4    | Interchangeability 12                                   |       |
| 3.5    | Operation and Accessibility of Controls 12              |       |
| 3.6    | Self-Test Capability                                    |   12  |
| 3.7    | Effect of Tests 12                                      |       |
| 3.8    | Malfunctions and Failure Indications                    |   13  |
| 3.8.1  | Malfunction Indication 13                               |       |
| 3.8.2  | Power Failure Indication 13                             |       |
| 3.8.3  | Fail Safe Provision 13                                  |       |
| 3.9    | Multiple Mode Indications 13                            |       |
| 3.10   | Source Selection 13                                     |       |
| 3.11   | Display 13                                              |       |
| 3.11.1 | Multi-Page Display Capability 13                        |       |
| 3.11.2 | Discernibility 14                                       |       |
| 3.11.3 | Critical Information 14                                 |       |
| 3.11.4 | Information Limit Indication 14                         |       |
| 3.11.5 | Scale Indications 14                                    |       |
| 3.11.6 | Ambiguity 14                                            |       |
| 3.11.7 | Symbology 14                                            |       |
| 3.12   | Display Latency                                         |   14  |
| 3.13   | Orientation                                             |   15  |
| 3.14   | Identification 15                                       |       |
| 3.14.1 | Declaration of EFIS Functions 15                        |       |
|        |                                                         |       |
| 4.     | MINIMUM PERFORMANCE STANDARDS UNDER STANDARD CONDITIONS |   15  |
| 4.1    | Flight Instrument Functions                             |   16  |
| 4.1.1  | Airspeed 16                                             |       |
| 4.1.2  | Vertical Velocity (Rate of Climb) 17                    |       |
| 4.1.3  | Altimeter 18                                            |       |
| 4.1.4  | Attitude (Bank and Pitch) 21                            |       |
| 4.1.5  | Direction Indicator 22                                  |       |
| 4.1.6  | Maximum Allowable Airspeed                              |   23  |
| 4.1.7  | Mach 23                                                 |       |
| 4.1.8  | Turn and Slip                                           |   24  |
| 4.1.9  | Airborne Low-Range Radio Altimeter 24                   |       |
| 4.1.10 | Automatic Flight Guidance and Control System 25         |       |
| 4.2    | Navigation and Communication Functions 25               |       |
| 4.2.1  | Very High Frequency Omnidirectional Range (VOR) 25      |       |
| 4.2.2  | Distance Measuring Equipment (DME)                      |   26  |
| 4.2.3  | Localizer                                               |   27  |
| 4.2.4  | Glideslope 28                                           |       |
4.2.5 
Marker Beacon 
............................................................................................................................................ 29 
4.2.6 
Automatic Direction Finding (ADF) ............................................................................................................. 29 
4.2.7 
Stand-Alone Airborne Navigation Equipment Using the Global Positioning System Augmented  
 
by the Satellite Based Augmentation System (GPS/SBAS) ....................................................................... 30 
4.2.8 
Flight Management System using Multi-sensor Inputs ............................................................................... 35 
4.2.9 
Microwave Landing System (MLS) ............................................................................................................. 41 
4.2.10 
VHF Radio 
................................................................................................................................................... 42 
4.2.11 
HF Radio ..................................................................................................................................................... 43 
4.3 
Engine and Fuel Management Functions ................................................................................................... 44 
4.3.1 
Temperature 
................................................................................................................................................ 44 
4.3.2 
Fuel Flow 
..................................................................................................................................................... 44 
4.3.3 
Manifold Pressure ....................................................................................................................................... 45 
4.3.4 
Fuel, Oil, and Hydraulic Pressure ............................................................................................................... 46 
4.3.5 
Tachometer ................................................................................................................................................. 46 
4.3.6 
Fuel and Oil Quantity .................................................................................................................................. 46 
4.4 
Weather Surveillance and Avoidance Functions ........................................................................................ 47 
4.4.1 
Windshear Warning and Escape Guidance 
................................................................................................ 47 
4.4.2 
Weather and Ground Mapping Radar 
......................................................................................................... 48 
4.4.3 
Airborne Passive Thunderstorm Detection ................................................................................................. 51 
4.4.4 
Optional Display Equipment for Weather and Ground Mapping Radar Indicators ..................................... 52 
4.5 
Terrain Surveillance and Avoidance Functions .......................................................................................... 53 
4.5.1 
Terrain Awareness and Ground Proximity 
.................................................................................................. 53 
4.5.2 
Helicopter TAWS 
......................................................................................................................................... 55 
4.6 
Traffic Surveillance and Avoidance Functions 
............................................................................................ 56 
4.6.1 
Traffic Collision Avoidance System (TCAS I and II) ................................................................................... 56 
4.6.2 
Traffic Advisory System .............................................................................................................................. 61 5. 
MINIMUM PERFORMANCE STANDARDS UNDER ENVIRONMENTAL CONDITIONS 
.......................... 64 
5.1 
Additional Functional Requirements under Environmental Conditions 
....................................................... 65 
5.1.1 
Airspeed Performance ................................................................................................................................ 65 
5.1.2 
Vertical Speed Performance ....................................................................................................................... 65 
5.1.3 
Manifold Pressure Performance ................................................................................................................. 65 
5.1.4 
Tachometer Performance ........................................................................................................................... 65 
5.1.5 
Automatic Flight Guidance and Control System ......................................................................................... 65 6. 
GLOSSARY OF TERMS 
............................................................................................................................. 74 
6.1 
Words and Phrases 
..................................................................................................................................... 74 
6.2 
Abbreviations .............................................................................................................................................. 75 7. 
NOTES 
........................................................................................................................................................ 83 
7.1 
Revision Indicator 
........................................................................................................................................ 83 
 
APPENDIX A  DECLARATION OF EFIS DISPLAY FUNCTIONS ..................................................................................... 84 APPENDIX B 
AIR SPEED SCALE ERROR PERFORMANCE OVER TEMPERATURE ENVIRONMENT ..................... 91 
 
Figure 1  
Electronic Flight Instrument System (EFIS) functions covered by this MOPS ............................................. 5 
Figure 2  
RA pitch cues on a PFD 
.............................................................................................................................. 60 
Figure 3  
Declaration of electronic flight instrument functions selected from AS6296 
............................................... 86 
Figure 4  
Example - Declaration of electronic flight instrument functions selected from AS6296 ............................. 88 
Figure 5  
Declaration of electronic flight instrument error contribution 
....................................................................... 90 Table 1  
Airspeed scale error system tolerance 
........................................................................................................ 17 
Table 2 
Vertical speed scale error tolerance ........................................................................................................... 18 
Table 3  
Cold temperature correction - altitude correction chart 
............................................................................... 19 
Table 4  
Scale and hysteresis errors for increasing and decreasing altitude (at ambient room temperature) ......... 20 
Table 5 
Barometric setting mechanism 
.................................................................................................................... 21 
Table 6  
Radio altitude scale error tolerance ............................................................................................................ 25 
Table 7 
Standard SBAS function labels 
................................................................................................................... 31 
Table 8  
Non-numeric display requirements ............................................................................................................. 32 
Table 9  
Non-numeric display requirements (modes) 
............................................................................................... 33 
Table 10  
MLS channels and frequencies 
................................................................................................................... 42 
Table 11  
Frequency channel spacing and channel identification .............................................................................. 43 
Table 12  
Classification by temperature accuracies ................................................................................................... 44 
Table 13  
Standard set of visual and aural terrain alerts ............................................................................................ 54 
Table 14  
Displayed aircraft symbols (examples) ....................................................................................................... 61 
Table 15 
Performance required during environmental conditions ............................................................................. 66 
Table 16 
Performance required during environmental conditions ............................................................................. 69 
Table 17 
Performance required during environmental conditions ............................................................................. 72 
Table B1  
Air speed scale error performance over temperature environment ............................................................ 91 

## 1. Scope

This SAE Aerospace Standard (AS) specifies minimum performance standards for Electronic Flight Information System (EFIS) displays that are head-down and intended for use in the flight deck by the flight crew in all 14 CFR Part 23, 25, 27, and 29 aircraft. This document is expected to be used by multiple regulatory agencies as the basic requirement for a technical standard order for EFIS displays. The requirements and recommendations in this document are intended to apply to, but are not limited to, the following types of display functions: 

 
Primary Flight and Primary Navigation displays, including vertical situation and horizontal situation functions. 
 
Displays that provide flight crew alerts, which may include engine instrument, aircraft systems information/control. 
 
Control displays including communication, navigation and system control displays. 
 
Information displays, which may include navigation displays used for situation awareness only, supplemental data, and maintenance and documentation displays. 
 
Display Systems including a Display Unit (display) and a symbol generator. 
The display functions herein were based on the *display aspects* of functions covered by previous TSOs that included an end-to-end system, including sensors. This document does not address video display terminals or video monitors without the means to generate symbols. The symbol generating function may be contained within the display or may be external to the display unit and part of the display system. This document is not intended to address the display of single function equipment (e.g., airspeed).  Two functions are required as a minimum. This document does not address the sensors or computational engines (e.g., TAWs computer, navigation computer, or TCAS processor) that transmit their data to the EFIS display.  
Functions that are not covered in this document include: Overspeed Warning; Air Traffic Control Radar Beacon System (ATCRBS)/Mode Select (Mode S); Automatic Dependent Surveillance - Broadcast (ADS-B); Traffic Information System - Broadcast (TIS-B); Electronic Map Display; Synthetic Vision; Enhanced Vision; Head-Up Displays (HUD); and Head Worn Displays (HWD). This document does address the following types of control functions: 

 
Control functions related to the data presented on the EFIS display(s).  
 
Control means that are integrated into the displays. 
NOTE: This document is expected to be used for a technical standard order for EFIS displays. This document does not 
address the hardware, physical, or optical (ocular) requirements of the EFIS displays.  Those requirements are addressed in AS8034B. This document is subject to change to keep pace with experience and technical advances.  
 
Many functions often included in an EFIS in existing systems were considered for this MOPS. In general, the functions that were not included here were excluded because it was too complicated to extract and separate the 
display requirements from the sensor requirements.  In other cases, the display requirements in the original MOPS were too extensive to add to this document without essentially replicating the original MOPS. Applicants will need to apply separately for approval for those functions.  

## 2. References

The documents listed in 2.1 are those referenced within various parts of this document as guidance or direction. The documents listed in 2.2 are provided for informational purposes only and do not form a part of the requirements of this document. 

## 2.1 Applicable Documents

The following publications form a part of this document only to the extent that they are explicitly invoked by the requirements within this Aerospace Standard (AS). The latest issue of all SAE International publications shall apply except in cases where referring documents call out specific versions. In the event of conflict between these documents and this standard, the contents of this standard shall govern. 

## 2.1.1 Sae Publications

Available from SAE International, 400 Commonwealth Drive, Warrendale, PA 15096-0001, Tel: 877-606-7323 (inside USA and Canada) or +1 724-776-4970 (outside USA), www.sae.org.  

| AIR1093    | Numeral, Letter and Symbol Dimensions for Aircraft Instrument Displays                            |
|------------|---------------------------------------------------------------------------------------------------|
| ARP4102/7  | Electronic Displays                                                                               |
| ARP4761    | Guidelines and Methods for Conducting the Safety Assessment Process on Civil Airborne Systems and |
| Equipment  |                                                                                                   |
| ARP5289    | Electronic Aeronautical Symbols                                                                   |
| ARP5621    | Electronic Display of Aeronautical Information (Charts)                                           |
| AS8034B    | Minimum Performance Standard for Airborne Multipurpose Electronic Displays                        |
|            |                                                                                                   |
|            |                                                                                                   |

## 2.1.2 Code Of Federal Regulations (Cfr)

Copies of 14 CFR parts 21 and 45 are available from the Superintendent of Documents, U.S. Government Printing Office (GPO), P.O. Box 979050, St. Louis, MO 63197, Tel: (202) 512-1800, fax (202) 512-2250. You can also order copies online at www.access.gpo.gov. Select "Access," then "Online Bookstore." Select "Aviation," then "Code of Federal Regulations. Copies also available digitally at no cost from the GPO's Electronic Code of Federal Regulations website, at: http://www.ecfr.gov/cgi-bin/text-idx?&c=ecfr&tpl=/ecfrbrowse/Title14/14tab_02.tpl, or from the FAA's Regulatory and Guidance Library (RGL), at http://rgl.faa.gov/Regulatory_and_Guidance_Library/rgFinalRule.nsf/MainFrame?OpenFrameset. Title 14, CFR Part 21, Certification Procedures for Products and Parts, and particularly, Subpart O, Technical Standard Order Approvals Title 14, CFR Part 45, Identification and Registration Marking, and particularly, Subpart B, Marking of Products and Articles, section §45.15. 

## 2.1.3 Rtca/Eurocae Publications

Available from RTCA, Inc., 1150 18th Street, NW, Suite 910, Washington, DC 20036, Tel: 202-833-9339, www.rtca.org. Order EUROCAE documents from EUROCAE, 102 rue Etienne Dolet, 92240 Malakoff France. Telephone 33 (0) 1 4092 7930, fax 33 (0) 1 4655 6265. You can also order from the EUROCAE Internet website at www.eurocae.net. 

DO-143 
Minimum Performance Standards - Airborne Radio Marker Receiving Equipment Operating on 75 MHz 
DO-161A 
Minimum Performance Standards - Airborne Ground Proximity Warning Equipment 
DO-163 
Minimum Performance Standards - Airborne High Frequency Radio Communications Transmitting and Receiving Equipment Operating Within the Radio-Frequency Range 1.5 - 30 MHz 
DO-173 
Minimum Operational Performance Standards for Airborne Weather and Ground Mapping Pulsed Radars 
DO-174 
Minimum Operational Performance Standards for Optional Equipment Which Displays Non-Radar-Derived Data on Weather and Ground Mapping Radar Indicators  
DO-177 
Minimum Operational Performance Standards for Microwave Landing System (MLS) Airborne Receiving Equipment 
DO-179 
Minimum Operational Performance Standards for Automatic Direction Finding (ADF) Equipment    
DO-185B 
Minimum Operational Performance Standards for Traffic Alert and Collision Avoidance Systems II (TCAS II) 
DO-186B 
Minimum Operational Performance Standards for Airborne Radio Communications Equipment Operating Within the Radio Frequency Range 117.975-137.000 MHz 
DO-189 
Minimum Operational Performance Standards for Airborne Distance Measuring Equipment (DME) Operating within the Radio Frequency Range of 960-1215 MHz 
DO-191 
Minimum Operational Performance Standards for Airborne Thunderstorm Detection Equipment 
DO-192 
Minimum Operational Performance Standards for Airborne ILS Glide Slope Receiving Equipment Operating Within the Radio Frequency Range of 328.6-335.4 Megahertz 
 
 
DO-195 
Minimum Operational Performance Standards for Airborne ILS Localizer Receiving Equipment Operating within the Radio Frequency Range of 108-112 Megahertz 
DO-196 
Minimum Operational Performance Standards for Airborne VOR Receiving Equipment Operating Within the Radio Frequency Range of 108- 117.95 Megahertz  
DO-197A 
Minimum Operational Performance Standards for an Active Traffic Alert and Collision Avoidance System I (Active TCAS I) 
DO-220 
Minimum Operational Performance Standards (mops) For Airborne Weather Radar with Forward-looking Windshear Detection Capability   
DO-229D 
Minimum Operational Performance Standards for Global Positioning System/Wide Area Augmentation System Airborne Equipment 
DO-257A 
Minimum Operational Performance Standards for the Depiction of Navigational Information on Electronic Maps 
DO-267A 
Minimum Aviation System Performance Standards (MASPS) for Flight Information Services-Broadcast (FIS-B) Data Link  
DO-283A 
Minimum Operational Performance Standards for Required Navigation Performance for Area Navigation 
DO-309 
Minimum Operational Performance Standards (MOPS) for Helicopter Terrain Awareness and Warning System (HTAWS) Airborne Equipment 
DO-325 
Minimum Operational Performance Standards (MOPS) for Automatic Flight Guidance and Control Systems and Equipment 
DO-334 
Minimum Operational Performance Standards (MOPS) for Strapdown Attitude and Heading Reference Systems (AHRS) 
ED-30 
Minimum Performance Standards for Airborne Low-Range Radio (Radar) Altimeter Equipment 

## 2.2 Related Informational Publications

The following publications are provided for information purposes only and are not a required part of this SAE Aerospace Technical Report. 

## 2.2.1 Sae Publications

Available from SAE International, 400 Commonwealth Drive, Warrendale, PA 15096-0001, Tel: 877-606-7323 (inside USA and Canada) or +1 724-776-4970 (outside USA), www.sae.org.  

AS392 
Altimeter, Pressure Actuated Sensitive Type 
AS396 
Bank and Pitch Instruments (Indicating Stabilized Type) (Gyroscopic Horizon, Attitude Gyro) 
AS404 
Electric Tachometer: Magnetic Drag (Indicator & Generator) 
AS405 
Fuel and Oil Quantity Instruments 
AS407 
Fuel Flowmeters 
AS408 
Pressure Instruments - Fuel, Oil and Hydraulic (Reciprocating Engine Powered Aircraft) 
 
 
AS8001 
Minimum Performance Standard for Bank & Pitch Instruments 
AS8004 
Minimum Performance Standard for Turn and Slip Instrument 
AS8005 
Minimum Performance Standard Temperature Instruments 
AS8009B 
Pressure Altimeter Systems 
AS8013  
Minimum Performance Standard for Direction Instrument, Magnetic (Gyroscopically Stabilized) 
AS8016  
Vertical Velocity Instrument (Rate-of-Climb) 
AS8018 
Minimum Performance Standard for Mach Meters 
AS8019 
Airspeed Instruments 
AS8021 
Minimum Performance Standard for Direction Instrument, Non-Magnetic (Gyroscopically Stabilized) 
AS8042  
Manifold Pressure Instruments 
2.2.2 
FAA Reference Documents 
2.2.2.1 
Advisory Circulars and Orders 
AC 20-41A 
Substitute Technical Standard Order (TSO) Aircraft Equipment 
AC 21-43A 
Production Under 14 CFR Part 21, Subparts F, G, K, and O 
AC 20-175  
Controls for Flight Deck Systems  
AC 25-11B 
Electronic Flight Displays (Note: In the EASA system, AMC 25-11 is technically similar). 
2.2.2.2 
FAA Orders 
8120.22 
Production Approval Procedures 
8150.1C 
Technical Standard Order Program 
2.2.2.3 
FAA Technical Standard Orders 
A current list of Technical Standard Orders (TSOs) and advisory circulars can be found on the FAA Internet website Regulatory and Guidance Library (RGL) at http://rgl.faa.gov.  

TSO-C2d 
Airspeed Instruments 
TSO-C3e 
Turn and Slip Instrument 
TSO-C4c 
Bank and Pitch Instruments 
TSO-C5f  
Direction Instrument, Non-Magnetic 
TSO-C6e 
Direction Instrument, Magnetic (Gyroscopically Stabilized) 
TSO-C8e 
Vertical Velocity Instruments 
TSO-C10b 
Altimeter, Pressure Actuated, Sensitive Type 
 
 
TSO-C34e 
ILS Glide Slope Receiving Equipment Operating Within the Radio       Frequency Range of 328.6-335.4 
TSO-C35d 
Airborne Radio Marker Receiving Equipment (a.k.a. Radio Marker Beacon) 
TSO-C36e 
Airborne ILS Localizer Receiving Equipment Operating within the Radio Frequency Range of 108-112 (a.k.a. ILS Localizer) 
TSO-C40c 
VOR Receiving Equipment Operating Within the Radio Frequency Range of 108-117.95 Megahertz (MHz) 
TSO-C41d 
Automatic Direction Finding (ADF) Equipment 
TSO-C43c 
Temperature Instruments 
TSO-C44c 
Fuel Flowmeters 
TSO-C45b 
Manifold Pressure Instruments 
TSO-C46a 
Maximum Allowable Airspeed Indicator Systems 
TSO-C47a 
Fuel, Oil, and Hydraulic Pressure Instruments 
TSO-C49b 
Electric Tachometer: Magnetic Drag (Indicator and Generator) 
TSO-C55a 
Fuel and Oil Quantity Instruments 
TSO-C63d  
Airborne Weather Radar Equipment (a.k.a. Predictive Windshear) 
TSO-C66c 
Distance Measuring Equipment (DME) Operating Within the Radio Frequency Range of 960-1215 Megahertz 
TSO-C87a 
Airborne Low-Range Radio Altimeter 
TSO-C92c 
Airborne Ground Proximity Warning Equipment (a.k.a. Ground Proximity Warning Systems or GPWS) 
TSO-C95a 
Mach Meters 
TSO-C104 
Microwave Landing System (MLS) Airborne Receiving Equipment 
TSO-C105 
Optional Display Equipment for Weather and Ground Mapping Radar Indicators 
TSO-C106 
Air Data Computer 
TSO-C110a 
Airborne Passive Thunderstorm Detection Equipment 
TSO-C113a 
Airborne Multipurpose Electronic Displays 
TSO-C115c 
Flight Management System (FMS) Using Multi-Sensor Inputs 
TSO-C117a 
Airborne Windshear Warning and Escape Guidance Systems for Transport Airplanes (a.k.a. Reactive Windshear) 

TSO-C118a  
Traffic Alert and Collision Avoidance System (TCAS) Airborne Equipment, TCAS I 

TSO-C119d  
Traffic Alert and Collision Avoidance System (TCAS) Airborne Equipment, TCAS II with Hybrid Surveillance TCAS II  
 
 
TSO-C146d 
Stand-alone Airborne Navigation Equipment Using the Global Positioning System Augmented by the Satellite Based Augmentation System WAAS 
TSO-C147a  
Traffic Advisory System (TAS) Airborne Equipment  
TSO-C151c  
Terrain Awareness and Warning System (TAWS) 
TSO-C157a  
Aircraft Flight Information Services-Broadcast (FIS-B) Data Link Systems and Equipment FIS-B 
TSO-C165a  
Electronic Map Display Equipment for Graphical Depiction of Aircraft Position Moving Maps 
TSO-C169a 
VHF Radio Communications Transceiver Equipment Operating Within Radio Frequency Range 117.975 to 137.000 Megahertz 
TSO-C170 
High Frequency (HF) Radio Communications Transceiver Equipment Operating Within the Radio Frequency Range 1.5 to 30 Megahertz 
TSO-C194 
Helicopter Terrain Awareness and Warning System (HTAWS) 
TSO-C198 
Automatic Flight Guidance and Control System (AFGCS) Equipment 
TSO-C201  
Attitude and Heading Reference Systems (AHRS)  

## 2.2.3 Rtca/Eurocae Publications

The RTCA documents referenced here may be purchased from RTCA, Inc., 1150 18th Street NW, Suite 910, Washington, DC 20036, Tel: 202-833-9339, www.rtca.org. 

DO-256 
Minimum Human Factors Standards for Air Traffic Services Provided Via Data Communications Utilizing the ATN, Builds I and IA 
ED-38 
Minimum Performance Specification for Airborne Weather, Ground Mapping and Assisted Approach Pulse Radars (Including Surface-Based Transponder Beacon System Characteristics) 

## 2.3 Definitions

Definitions used in this document shall be as noted in the Glossary of Terms defined in Section 6. The word "shall" is used to express an essential requirement where compliance is mandatory. 

The word "should" is used to express a recommendation. Deviation from the specified recommendation shall require justification. The use of the word warning(s) in this document could mean a warning, caution, or advisory level alert.  A warning is a condition that requires immediate flightcrew awareness and immediate flightcrew response.  A caution is a condition that requires immediate flightcrew awareness and subsequent flightcrew response.  An advisory is a condition that requires flightcrew awareness and may require subsequent flightcrew response. 

## 3. General Standards 3.1 Material

Material shall be of a quality that experience and/or tests have demonstrated to be suitable and dependable for use in aircraft instruments. 

 

## 3.1.1 Workmanship

Workmanship shall be consistent with high quality aircraft electromechanical and electronic instrument manufacturing practices. 

## 3.2 Compatibility Of Components

If an EFIS component is individually acceptable but requires calibration adjustments or matching to other components in the aircraft for proper operation, it shall be identified in a manner that will ensure performance to the requirements of this document. 

## 3.3 Equipment Functions And Mechanical Operations

The EFIS shall operate electrically and mechanically. 

## 3.4 Interchangeability

Display system components that are identified with the same manufactured part number shall be completely interchangeable. 

## 3.5 Operation And Accessibility Of Controls

Controls that are not normally adjustable in flight shall not be readily accessible to flight personnel when the instrument is installed in accordance with the instrument manufacturer's instructions. Controls intended for use on the EFIS during flight shall be designed to minimize errors. No combinations or sequences of these controls shall result in a condition that will be detrimental to the continued performance of the equipment. The display controls intended for flight operations shall not require the simultaneous use of more than one hand. Minimizing pilot workload should be considered when designing EFIS controls. The layering of information should not hinder the pilot in identifying the location of the desired control. Controls shall provide feedback when operated. Feedback can include one or more auditory cues, tactile cues, or visual cues. When a control occurs in multiple places (for example, a "Return" control on multiple pages of a flight management function), the control label location on all pages should be consistent across all occurrences. If a control is provided to perform multiple functions, the functionality shall be clearly distinguished.  There should be a clear indication when any control is in an altered state and not the default (e.g., if a knob is pulled out and then functions differently when rotated). 

## 3.6 Self-Test Capability

If the equipment contains integral arrangements to permit pre-flight and/or in-flight self-test checks on the operation of the equipment in combination with other aircraft sub-systems, such tests shall not adversely affect any associated subsystem. 

In-flight, self-test activation features shall include a means to alert the pilot or appropriate flight crew member of this mode of operation. 

## 3.7 Effect Of Tests

Unless otherwise stated, the application of all prescribed in service testing shall not produce a subsequent condition that would be detrimental to the continued performance of the EFIS. 


## 3.8 Malfunctions And Failure Indications 3.8.1 Malfunction Indication

Means shall be provided to indicate malfunctions, loss of functions, degradations, or failures to the appropriate crew member.  A blank display or an "X" across the display are examples of an acceptable means of indicating failure.  

## 3.8.2 Power Failure Indication

Means shall be provided to indicate when electrical power (voltage and/or current of all required phases) is not sufficient for proper operation of display and/or display system.  A blank display is an example of an acceptable means of indicating failure.  

## 3.8.3 Fail Safe Provision

No single failure or malfunction of the display system shall introduce unsafe conditions to interconnected equipment. Unsafe conditions of the display system results from failures, malfunctions, external events, errors, or combinations thereof.  
A Failure Modes and Effects Analysis (FMEA) should be performed to identify, isolate, and mitigate individual failures of the display. This is needed for a System Safety Assessment (SSA) for an aircraft airworthiness determination. ARP4761 Table 1 shows the failure condition severity as related to probability objectives and assurance levels for components and systems in aircraft.  

## 3.9 Multiple Mode Indications

When a display and/or display system has more than one mode, each mode of operation shall be indicated on the display, including any armed modes, transitions, and reversions. Selector switch position is not an acceptable means of indication. One example of an acceptable exception is the depiction of the Horizontal Situation Indicator (HSI)-Full Compass versus Arc mode, which does not require a mode indication. NOTE: For the purposes of this document, a mode is not a function. Examples of modes on a display include heading-up versus track up (i.e., flight path is on top) or north up (magnetic north is shown on top).  A mode could also be an alternate display format, such as a normal or primary mode versus a reversionary mode. 

## 3.10 Source Selection

Where multiple system configurations and more than one sensor input are available for source selection, the switching configuration by annunciation or by selector switch position should be readily visible, readable, and should not be misleading.  
If information from more than one navigation source can be presented, the selected navigation source should be continuously indicated. If multiple navigation sources can be presented simultaneously, the display should indicate unambiguously what information is provided by each source.   

## 3.11 Display

The information being displayed should conform to the applicable requirements in Section 4 of this document. 

## 3.11.1 Multi-Page Display Capability

Similar data and control markings should be consistent across pages (e.g., lat/long should be displayed in the same format on all pages where it appears). Lines of text shall be broken only at spaces or other natural delimiters. 

 

## 3.11.2 Discernibility

Task essential information allows the flightcrew to accomplishment all tasks required to safely perform the equipment's intended function.  Appropriate means shall be incorporated to prevent obscuration or confusion of task essential information.  Task essential information shall be identified and defined.  
Alerts and symbols shall be distinctive and readily discernible from one another.  Fields that are editable, selectable, or require operator entry should be clearly denoted. 

## 3.11.3 Critical Information

Means shall be provided to prevent the removal of information deemed critical to safe aircraft operation. 

## 3.11.4 Information Limit Indication

A means shall be provided to identify when critical displayed information exceeds display format functional limits.   

## 3.11.5 Scale Indications

The display scaling, graduations, and numeration shall be appropriate for the level of reading accuracy and dynamic range required (e.g., familiar units of measure are not as significant as the values and may be a smaller font, but shall be discernible). The display should indicate if display items are not drawn to scale (e.g., TAWS displays). The minimum dimensions of characters, numerals, and symbols used on the EFIS display should meet the requirements of AIR1093. 

## 3.11.6 Ambiguity

Appropriate means shall be used to prevent ambiguous indications within the operating range of the display system.  

## 3.11.7 Symbology

Displays should use characteristics and symbols that follow commonly accepted aviation practices.  The potential for misinterpreting symbols should be minimized.  Guidelines for electronic display symbology are provided in ARP4102-7. Symbols used for one purpose on published charts should not be used for another purpose on the EFIS display.  Reference ARP5621.  

## 3.12 Display Latency

The maximum amount of latency induced by the display system shall be appropriate to the priority of the function displayed, and shall not cause flight crew misinterpretation or lead to an unsafe condition. The display update rate should be sufficient to preclude objectionable motion artifacts that could be misleading or distracting. Examples of maximum latency for specific functions are as follows: 

a. Aircraft position data update, 1 second; b. Initial response to operator control input, 300 ms; 
c. Airspeed, altitude, attitude data update, 100 ms; d. Cursor or softkey response, 80 ms. 

## 3.13 Orientation

Displayed labels should be oriented to facilitate readability. For example, the labels should continuously maintain an upright orientation or align with an associated symbol (e.g., a runway, an airway, or a cardinal position on a compass). Images should be oriented in such a way that their presentation is easily interpreted.  

## 3.14 Identification

The information in a. through d. shall be legible and permanently marked on the equipment or nameplate attached thereto. If the information in e. and f. are provided, permanently marked it on the equipment or nameplate or in the installation manual.  

a. Manufacturer's part number. b. Manufacturer's serial number or date of manufacture or both. c. Manufacturer's name, trademark, symbol, or other approved identification. 
d. "See Installation Manual (IM) for Declared EFIS Functions", or equivalent, on the primary (most prominent) component 
of the EFIS.   
e. Name of equipment. f. 
"AS6296" or equivalent approval identification such as TSO marking. 

## 3.14.1 Declaration Of Efis Functions

For each EFIS function listed in 4.1.1 through 4.6.2 of this document, the equipment manufacturer shall select the particular functions (and classes, as applicable) that are included in the EFIS. The EFIS functions and applicable classes thus determined shall be tabulated on the "Declaration of Electronic Flight Instrument System (EFIS) Functions" form, in accordance with the guidelines in Appendix A. The completed Declaration of EFIS Functions Form shall be included in the installation manual and maintenance instructions. 

## 4. Minimum Performance Standards Under Standard Conditions

The subsections below group individual EFIS functions into broad categories: Flight Instrument Functions, Navigation and Communication Functions, Engine and Fuel Management Functions, Weather Surveillance and Avoidance Functions, Terrain Surveillance and Avoidance Functions, and Traffic Surveillance and Avoidance Functions. This grouping is for convenience only, and does not imply that all functions within a group are required for any given EFIS. 

Where appropriate, each function below addresses the accuracy (allowable error) requirements for that function.  In some cases, only a system-level error budget is provided.  In other cases, the allowable EFIS contribution to the total error is provided.   
In this document, the term "Displayed Error" is used when the accuracy value or error tolerance is intended to represent only the error contributed by the EFIS (see Section 6). It is recognized that many EFIS implementations receive digital data that directly represents the value to be displayed, with little or no EFIS processing required.  In this document, the term "Display-Ready Data" (see Section 6) is used to describe this case.  In other implementations, the EFIS may need to determine the displayed value based upon received analog sensor data, or upon multiple inputs that shall be processed together to determine the displayed value. 

 

## 4.1 Flight Instrument Functions 4.1.1 Airspeed 4.1.1.1 Indicating Means

The airspeed shall be indicated by means of a pointer, dial, tape, drum, digital numeric readout, other type of moving element, or any combination thereof. Unless otherwise specified, relative motion of the index with respect to the scale (either the index or the scale may be the moving element) shall be clockwise, up, or to the right for increasing airspeed.  

## 4.1.1.2 Graduations

The graduations shall be arranged to provide the maximum readability consistent with the accuracy of the EFIS display. Graduations shall be as follows 

a. The first graduation shall be at the lowest usable airspeed of the EFIS display, as specified by the manufacturer. 
b. From the 10 knot, 10 mph, or 20 km/h graduation nearest to the first graduation and continuing to 250 knots, 250 mph, 
or 400 km/h, graduations shall be separated by no greater than 20 knots, 20 mph, or 40 km/h.  If minor graduations are used, they shall be half the value of the major graduations.  If digital numeric readout is not used, then scale marking increments of 5 knots, 5 mph, or 10 km/h shall be used. 
c. Over 250 knots, 250 mph, or 400 km/h, graduations shall be at least every 50 knots, 50 mph, or 100 km/h. 

## 4.1.1.3 Numerals

The display shall include sufficient numerals positioned to permit quick and positive identification of each graduation. Numerals shall distinctly indicate the graduations to which each applies. When digital numeric readouts are used in conjunction with scales, they should be located close enough to the scale to ensure proper association, yet not detract from the interpretation of the graphic or the readout. 

## 4.1.1.4 Identification

The word AIRSPEED or IAS shall be marked on the dial. This marking may be omitted if the airspeed indication is a part of a "basic T" configuration.  If the units of measure are other than knots or mach, the units of measure shall be labeled. 

## 4.1.1.5 Limits

The indicating means shall be limited in such a way that the moving element will not move more than (a) 10 degrees for circular display or (b) 0.25 inch (6 mm) for linear displays beyond the greatest or least graduation in both increasing and decreasing directions. 

For circular displays, positive means shall be taken so that no ambiguity will exist when the indicator is at the maximum or minimum position, including the maximum over-travel of 10 degrees. If a digital display is used, a positive indication shall be provided on the display when the airspeed exceeds the calibrated range. 

## 4.1.1.6 Accuracy

If the airspeed data for the display is Display-Ready Data, then the displayed error shall not exceed ±1 knot or equivalent. If the airspeed data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS.  The error contributed by the EFIS shall not exceed the error in Table 1.  The displayed error shall be documented in the installation manual. 

 
NOTE: The scale error in Table 1 is defined for a system, including the sensor(s). This gives the EFIS manufacturer flexibility to define the displayed error introduced by the EFIS itself, without the sensors.   
In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

|                |           | Room Ambient    | Room Ambient    | Room Ambient    |
|----------------|-----------|-----------------|-----------------|-----------------|
| Airspeed       | Tolerance | Tolerance       | Airspeed        | Tolerance       |
| (knots or mph) | (knots)   | (mph)           |                 | (km/hour)       |
| 20             | 5         | 5               |                 | 40              |
| 30             | 5         | 5               |                 | 60              |
| 40             | 5         | 5               |                 | 80              |
| 50             | 5         | 5               |                 | 100             |
| 60             | 5         | 5               |                 | 120             |
| 70             | 4         | 4               |                 | 140             |
| 80             | 4         | 4               |                 | 160             |
| 90             | 4         | 4               |                 | 180             |
| 100            | 3         | 3               |                 | 200             |
| 120            | 3         | 3               |                 | 250             |
| 140            | 3         | 3               |                 | 300             |
| 160            | 3         | 3               |                 | 350             |
| 180            | 5         | 3               |                 | 400             |
| 200            | 5         | 6               |                 | 450             |
| 220            | 5         | 6               |                 | 500             |
| 250            | 5         | 6               |                 | 600             |
| 300            | 5         | 6               |                 | 700             |
| 350            | 5         | 6               |                 | 800             |
| 400            | 8         | 6               |                 | 900             |
| 450            | 8         | 9               |                 | 1000            |
| 500            | 8         | 9               |                 | 1100            |
| 550            | 8         | 9               |                 | 1200            |
| 600            | 10        | 9               |                 | 1300            |
| 650            | 10        | 9               |                 |                 |
| 700            | 10        | 12              |                 |                 |

NOTE: System tolerances include the contributions of the sensor and the EFIS. 

## 4.1.1.7 Smoothing

The indication of airspeed shall be smooth and free from irregular motion (e.g., jitter, jerkiness, or ratcheting effects) as the differential pressure or its electrical equivalent is increased and decreased smoothly. 

## 4.1.2 Vertical Velocity (Rate Of Climb) 4.1.2.1 Indicating Means

The vertical velocity shall be indicated by means of a pointer, dial tape, drum, or other type of moving element, or by a digital display with appropriate direction indication. Relative motion of the index with respect to the scale, or of the direction indicator (either the index or the scale may be the moving element) shall be clockwise, up, or to the right for ascending vertical velocity. 

 

## 4.1.2.2 Limits

When the indication is pegged at its maximum rate indication, the direction of that indication, whether ascending or descending, shall be clear and unambiguous. If a digital numeric readout is used, a positive indication shall be provided on the display when the vertical velocity of the aircraft exceeds the readout capability.  

## 4.1.2.3 Accuracy

The manufacturer shall determine the maximum error contributed by the EFIS. The displayed error shall not exceed the error in Table 2. The displayed error shall be documented in the installation manual. NOTE: The scale error in Table 2 is defined for a display *system*, including the sensor(s). This gives the EFIS manufacturer flexibility to define the displayed error introduced by the EFIS.   
In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

| Standard       | Standard      | Test Rate    | Test Rate    |
|----------------|---------------|--------------|--------------|
| Altitude Test  | Altitude Test | Ascent and   | Ascent and   |
| Interval       | Interval      | Descent      | Descent      |
| (Feet)         | (Meters)      | (ft/min)     | (m/min)      |
| 2000 to 2500   | 600 to 750    | 500          | 150          |
| 2000 to 3000   | 600 to 900    | 1000         | 305          |
| 2000 to 4000   | 600 to 1200   | 2000         | 610          |
| 2000 to 5000   | 600 to 1500   | 3000         | 915          |
| 2000 to 6000   | 600 to 1800   | 4000         | 1220         |
| 2000 to 7000   | 600 to 2400   | 5000         | 1525         |
| 15000 to 17000 | 4500 to 5200  | 2000         | 610          |
| 15000 to 19000 | 4500 to 5800  | 4000         | 1220         |
| 28000 to 30000 | 8550 to 9150  | 2000         | 610          |
| 28000 to 32000 | 8550 to 9800  | 4000         | 1220         |

 

## 4.1.2.4 Smoothing

The indication of vertical velocity shall be smooth and free from irregular motion (e.g., jitter, jerkiness, or ratcheting effects) 
as the static pressure or its electrical equivalent is increased and decreased smoothly over the full range of operation. 

## 4.1.3 Altimeter 4.1.3.1 Indicating Means

Altitude shall be indicated in feet or meters as required, by means of one or more pointers, dials, tapes, drums, digital readouts, or any combination thereof. Relative motion of the index with respect to the scale (either the index or the scale may be the moving element) shall be clockwise, up, or to the right for increasing altitude. In the case of counters, drums, or tapes, the higher number shall be above the lower. 

## 4.1.3.2 Identification

The word ALTITUDE or ALT shall be marked on the dial. The altitude range shall be shown on the dial. This marking may be omitted if the altitude indication is a part of a "basic T" configuration.  If the unit of measure is other than feet, the unit of measure shall be labeled. 


## 4.1.3.3 Altitude Range

The minimum calibrated altitude (at a 29.92 in Hg/1013.2 mb barometric setting) shall be -1000 feet (-300 m). The maximum shall be as specified by the manufacturer and documented in the equipment manual(s).   

## 4.1.3.4 Barometric Setting System

The display of barometric setting shall permit the altimeter to be set to any ambient barometric pressure throughout a minimum range of 27.50 to 31.50 in Hg (931.3 to 1066.7 mb). A feature shall be provided that will prevent incorrect indication if attempts are made to operate the barometric setting adjustment beyond the design range specified for the instrument. If a knob is used for control, the barometric setting number shall increase with a clockwise motion of the knob.  

## 4.1.3.5 Multiple Mode Indications (Altimeter)

An EFIS that is intended for operation in more than one altimeter mode shall meet the requirements of this document in each mode. The "normal" mode shall be as specified by the manufacturer. Means shall be provided to indicate when in other than the "normal" mode. If the EFIS is provided with an automatic static source correction function, positive indication shall be given when it is not in use. 

## 4.1.3.6 Static Source Error Correction

When the EFIS implements an altitude correction mechanism that is unique to a particular aircraft, the aircraft type and model number for which the EFIS has been created and performs its intended function shall be documented in the manual(s). 

## 4.1.3.7 Cold Temperature Corrections

When an altimeter indication employs automatic cold temperature corrections, it shall use corrections given in Table 3. The EFIS display shall provide a clear indication to the pilot when the cold temperature corrections are being automatically applied. If the altimeter indication normally provides automatic cold temperature correction and cannot compute the correction, positive indication shall be given that corrections are not being performed. 

Height Above Airport* in Feet 
 
200  300  400  500  600  700  800  900  1000  1500  2000  3000  4000  5000  
+10 
10 
10 
10 
10 
20 
20 
20 
20 
20 
30 
40 
60 
80 
90 
0°  
20  
20  
30  
30  
40  
40  
50  
50  
60  
90  
120  
170  
230  
280  
-10°  
20  
30  
40  
50  
60  
70  
80  
90  
100  
150  
200  
290  
390  
490  
-20°  
30  
50  
60  
70  
90  100  120  130  
140  
210  
280  
420  
570  
710  
-30°  
40  
60  
80  100  120  140  150  170  
190  
280  
380  
570  
760  
950  
-40°  
50  
80  100  120  150  170  190  220  
240  
360  
480  
720  
970  1210  
Reported Temp °C 
-50°  
60 
90 
120 
150 
180 
210 
240 
270 
300 
450 
590 
890 
1190 
1500 

* This is normally the destination airport's elevation. NOTE: Values are to be added to published altitudes. 


                                           

## 4.1.3.8 Graduations

Markings shall be provided at intervals not exceeding 20 feet of altitude with major markings at 100 foot intervals. ARP4102-7 Appendix A, items 39 and 40 provide an acceptable alternative means. For indicating an ascent in altitude when using a dial, the sensitive pointer shall move in a clockwise direction completing one revolution (360 degrees) for each 1000 feet of altitude change. A means shall be provided for showing the multiples of 1000 feet. 

## 4.1.3.9 Accuracy

When provided with Display-Ready Data, the EFIS shall not contribute more than 20 feet error to the displayed altitude. If the altitude data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS.  The error contributed by the EFIS shall not exceed the error in Table 4, except as outlined in the paragraphs below.  The displayed error shall be documented in the installation manual. Examples of non-Display-Ready Data include barometric correction, static source error correction, and cold temperature correction. NOTE: The scale error in Table 4 is defined for a system, including the sensor(s). This gives the EFIS manufacturer flexibility to define the displayed error introduced by the EFIS itself, without the sensors. .  

## 4.1.3.9.1 Scale And Hysteresis Error

The instrument shall meet the tolerance specified in Table 4, which includes the following conditions:  

1. Decreasing and increasing pressure for the test pressure ranges specified in Table 4, or 2. These pressures plus the static defect correction pressures (if specified) for the applicable aircraft as supplied by the 
airframe manufacturer. 

## 4.1.3.9.2 Static Source Correction

Where a static source correction means is in operation, the scale error tolerance shall be that shown in Table 4, increased by an amount of 10% of the static source error plus 10 feet (3 m). In all cases, the EFIS shall be tested to confirm that it does not exceed the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

|       |        | Test Pressure Altitude    | Tolerance    |
|-------|--------|---------------------------|--------------|
| Feet  | Meters |                           |              |
| -1000 | -300   | ±20                       | ±9           |
| 0     | 0      | ±20                       | ±9           |
| 2000  | 300    | ±20                       | ±9           |
| 2000  | 600    | ±30                       | ±9           |
| 3000  | 900    | ±30                       | ±9           |
| 4000  | 1200   | ±35                       | ±9           |
| 5000  | 1500   | ±35                       | ±9           |
| 10000 | 3000   | ±80                       | ±15          |
| 20000 | 6000   | ±130                      | ±20          |
| 30000 | 9000   | ±180                      | ±35          |
| 40000 | 12000  | ±230                      | ±45          |
| 50000 | 15000  | ±280                      | ±55          |

NOTE: System tolerances include the contributions of the sensor and the EFIS. 


## 4.1.3.10 Barometric Setting Scale

If the EFIS performs barometric correction, the pressure-to-altitude coordination shall meet the requirements of Table 5 - Barometric setting mechanism. 

|       |      |       | Barometric Pressure Scale    | Correct Difference    | Baro-Setting Tolerance    |
|-------|------|-------|------------------------------|-----------------------|---------------------------|
| in Hg | mb   | Feet  | Meters                       | Feet                  | Meters                    |
| 22.0  | 745  | -8266 | -2520                        | ±40                   | ±12                       |
| 23.27 | 788  | -6794 | -2071                        | ±35                   | ±11                       |
| 23.92 | 810  | -6065 | -1830                        | ±35                   | ±11                       |
| 24.98 | 846  | -4907 | -1496                        | ±30                   | ±9.0                      |
| 25.98 | 880  | -3850 | -1173                        | ±30                   | ±9.0                      |
| 26.99 | 914  | -2825 | -861                         | ±25                   | ±7.5                      |
| 27.55 | 933  | -2265 | -691                         | ±25                   | ±7.5                      |
| 28.20 | 955  | -1630 | -497                         | ±25                   | ±7.5                      |
| 28.58 | 968  | -1264 | -385                         | ±25                   | ±7.5                      |
| 28.94 | 980  | -920  | -280                         | ±25                   | ±7.5                      |
| 29.91 | 1013 | -10   | -3                           | ±25                   | ±7.5                      |
| 30.15 | 1021 | 211   | 64                           | ±25                   | ±7.5                      |
| 30.77 | 1042 | 776   | 237                          | ±25                   | ±7.5                      |
| 30.98 | 1049 | 965   | 294                          | ±25                   | ±7.5                      |

## 4.1.3.11 Minimum Operating Rate

The altimeter indication shall be capable of a minimum operating rate of 20000 ft/min (6100 m/min). 

## 4.1.3.12 Monitoring Functions

The EFIS display shall provide a means to indicate the loss of a "valid" signal provided by a remote sensor or computer. 

## 4.1.4 Attitude (Bank And Pitch) 4.1.4.1 Indicating Method

The EFIS shall present pitch and roll angles such that over the range of indication the earth horizon appears as viewed by the pilot when looking forward out of the aircraft. 

The design shall provide suitable contrast between sky and ground segments such that pitch up/down are immediately recognizable. Some indication of both sky and ground shall always be visible at extreme attitude.   

## 4.1.4.2 Graduations

The display shall provide a roll attitude index that indicates through 360 degrees with markings at least for 0 degrees and 
30 degrees right and left roll angles. The pitch display shall provide minor graduations every 5 degrees and major graduation lines every 10 degrees between -30 degrees and +50 degrees. This entire range need not be visible at one time. The major graduations shall be marked with their numerical value. 

## 4.1.4.3 Pitch Attitude Reference

A 0 degree pitch reference shall be provided and may be adjustable to accommodate a range of pitch attitude trim.  

## 4.1.4.4 Accuracy

When provided with Display-Ready Data, the EFIS shall not contribute more than a 0.5 degree error to the displayed pitch and roll. If the pitch and roll data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS.  The error contributed by the EFIS shall not exceed a total scale error of 2.5 degrees.  The displayed error shall be documented in the installation manual. NOTE: The total scale error of 2.5 degrees is defined for a display *system*, including the sensor(s). This gives the EFIS 
manufacturer flexibility to define the display tolerance error introduced by the EFIS.  However, the displayed error introduced by the EFIS should still be a small portion of the total system error budget, which has sensors not included here. The EFIS scale error tolerance shall be documented in the installation manual.  
In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.1.5 Direction Indicator 4.1.5.1 Indicating Method

Direction shall be indicated using either of the two following methods: 

1. A rotating dial or dial segment with a fixed datum or lubber line; dial rotation shall be counterclockwise for right turns. 2. A horizontal scale display with fixed datum or lubber line; scale graduations shall move to the left for right turns. 

## 4.1.5.2 Operating Mode

Direction of flight indications may be shown using aircraft heading or ground track. If more than one operating mode is provided, the direction reference shall be clearly indicated to the pilot. In addition, the direction of flight reference may be displayed in various units, such as magnetic north, true north, or grid north reference. The direction reference shall be indicated if more than one method is available.  

## 4.1.5.3 Graduations

The indicator shall provide minor graduation lines at 5 degrees or smaller intervals, with major graduation lines every 10 degrees. Direction numerals shall be provided at 30 degrees, 60 degrees, 120 degrees, 150 degrees, 210 degrees, 240 degrees, 300 degrees, and 330 degrees. The markings at 0 degrees (360 degrees), 90 degrees, 180 degrees, and 270 degrees shall be either numerals or the letters "N", "E", "S", and "W" respectively. It is acceptable to use the hundreds and tens place numerals and drop the ones place (e.g., 33 for 330 degrees).  

## 4.1.5.4 Accuracy

When provided with Display-Ready Data, the EFIS shall not contribute more than a 0.5 degree error to the displayed magnetic heading or ground track.  
If the heading or ground track data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS.  The error contributed by the EFIS shall not exceed a total scale error of 2 degrees.  The displayed error shall be documented in the installation manual. Note: The total scale error of 2 degrees is defined for a display *system*, including the sensor(s). This gives the EFIS manufacturer flexibility to define the display tolerance error introduced by the EFIS.  However, the displayed error introduced by the EFIS should still be a small portion of the total system error budget, which has sensors not included here.  The display scale error tolerance shall be documented in the installation manual.  
In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 


## 4.1.6 Maximum Allowable Airspeed 4.1.6.1 Maximum Allowable Airspeed Indication

The maximum allowable airspeed indication shall show maximum allowable airspeed values. Maximum allowable airspeed shall be displayed in such a manner that the numerical values on the scale increase in a clockwise, left to right, or bottom to top direction. 

## 4.1.6.2 Accuracy

When provided with Display-Ready Data, the EFIS shall not contribute more than one knot error to the displayed maximum allowable airspeed. When provided with Display-Ready Data, the EFIS shall not contribute more than 0.001 mach error to the displayed maximum allowable mach. 

If the maximum allowable airspeed or maximum allowable mach data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS. The displayed error shall be documented in the installation manual. The EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.1.7 Mach

This function provides mach number indication.  

## 4.1.7.1 Indicating Method

Indicators comprising a dial shall be provided with mach number graduations at intervals not to exceed 0.01 with major graduations every 0.05 and with numerical markings at intervals not greater than 0.1.  When a digital numerical readout is employed, the resolution shall be better than or equal to 0.01 mach. 

## 4.1.7.2 Accuracy

When mach is received as Display-Ready Data, the EFIS shall not contribute more than 0.002 mach error to the displayed mach number. If the mach data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS. The displayed error shall be documented in the installation manual. The EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

 

## 4.1.8 Turn And Slip 4.1.8.1 Turn Rate2

The turn rate shall be indicated by a pointer deflecting in the direction of the turn, or by other means equally suitable. If the aircraft is not turning, the pointer shall align with the center tick mark or be removed from view. When displaying rate of turn by means of a pointer on a fixed scale, indices for standard rate (180 degrees/minute) shall be provided. Indices for half standard rate (90 degrees/minute) may be provided. The range of the rate of turn indicator shall be a minimum of ±240 degrees/minute. 

## 4.1.8.2 Standard Turn Bank Angle

When it is displayed, the standard rate bank angle shall be indicated on the roll scale in both directions. 

## 4.1.8.3 Slip/Skid

When it is displayed slip/skid shall be indicated by a figure or object moving with respect to a reference, or by other means equally suitable. A slip is indicated by the ball (or figure or object) on the inside (wing down side) of a turn. A skid is indicated by the ball (or figure or object) on the outside (wing up side) of the turn. If an inclinometer is used, when the indicator is centered, the scale on either side of the indicator shall include the greater of one and half indicator widths or 7 degrees. Typically, 0.1 g laterally is one ball width. It is recognized that different scaling may be required for different applications. The manufacturer shall specify the scaling.  

## 4.1.8.4 Accuracy

The EFIS shall not significantly contribute to the error of Turn Rate or Slip/Skid.  The manufacturer shall define the 95% displayed error in the installation manual. The manufacturer shall provide instructions on determining total installed system error. In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.1.9 Airborne Low-Range Radio Altimeter 4.1.9.1 Accuracy

When provided with Display-Ready Data, the EFIS shall not contribute more than 1 foot error to the displayed radio altitude. 

If the radio altitude data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS.  The error contributed by the EFIS shall not exceed the error in Table 6.  The displayed error shall be documented in the installation manual. The total scale error in Table 6 is defined for a display *system*, including the sensor(s). This gives the EFIS manufacturer flexibility to define the display tolerance error introduced by the EFIS.  However, the displayed error introduced by the EFIS should still be a small portion of the total system error budget, which has sensors not included here.  
In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 


| Height Range                  | Total System Accuracy       |
|-------------------------------|-----------------------------|
| 3 to 100 feet (1 to 30 m)     | ±5 feet (1.5 m)             |
| 100 to 500 feet (30 to 150 m) | ±5% of true height          |
| ±7% of true height            | 500 feet (150 m) to maximum |
| display scale                 |                             |

## 4.1.9.2 Alerts For Airborne Low-Range Radio Altimeter 4.1.9.2.1 Failure Indication

An indication shall be provided when there is a failure of the radio altimeter to accomplish its intended function because of the following conditions:  

1. Loss of power, and  
2. Loss of signal or altitude sensing capability when within the manufacturer's stated operating altitude range. 4.1.9.2.2 
Decision Height 
For use in landing systems, it is strongly recommended that an indication be provided when the decision height is reached. 

## 4.1.10 Automatic Flight Guidance And Control System

This function provides flight guidance indications and autoflight mode indications. The EFIS shall display any annunciations provided to it by flight guidance systems. Scaling and presentation of flight director command bars should ensure that valid steering commands are displayed and that invalid or off-scale steering commands are not displayed. Note: under tests under environmental conditions, the display is not required to operate normally during *abnormal* voltage inputs, but shall not provide misleading information during or after the tests. 

## 4.2 Navigation And Communication Functions 4.2.1 Very High Frequency Omnidirectional Range (Vor) 4.2.1.1 Bearing Accuracy

If the bearing data for the display is Display-Ready Data, the EFIS shall not contribute more than ±0.5 degrees error to the displayed Bearing. If the bearing data for the display is not Display-Ready Data, the manufacturer shall determine the maximum displayed error contributed by the EFIS.  The error contributed by the EFIS shall not exceed 2.7 degrees with probability of 95%. This bearing accuracy requirement applies to any VOR bearing information that is provided for use in aircraft navigation.  The displayed error shall be documented in the installation manual.  
NOTE: This total error is for a display *system*, including the sensor(s). This gives the EFIS manufacturer flexibility to define the display tolerance error introduced by the EFIS.  However, the displayed error introduced by the EFIS should still be a small portion of the total system error budget, which has sensors not included here. 

In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 


## 4.2.1.2 Frequency Display

If tuning of the VOR sensor is a function of this EFIS, the frequency of paired channel or the identification of the navigation facility or facilities in active use shall be displayed or capable of recall at all times during flight. 

## 4.2.1.3 Vor Course Deviation Indication (Cdi)

If a course deviation indication is provided, the following requirements shall be met with valid input signals. 

## 4.2.1.3.1 Vor Course Deviation Sensitivity3

The EFIS shall provide a display for presentation of VOR course deviation magnitude and direction (left/right).  This display output shall have sufficient dynamic range to display course deviation of at least ±10 degrees with a resolution of one degree or better. 

## 4.2.1.3.2 Vor Course Deviation Accuracy

If the VOR Course Deviation data for the display is Display-Ready Data, the EFIS shall not contribute more than a ±0.5 degree error to the displayed VOR course deviation. If the VOR Course Deviation data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS.  The displayed error shall be documented in the installation manual. In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.2.1.3.3 Ambiguity Indication (To-From)

When valid, and at all bearings up to ±75 degrees from the selected radial, the inbound/outbound (i.e., "TO" or "FROM") shall be clearly indicated.  

## 4.2.1.4 Warnings

The VOR Bearing and, if provided, the Course Deviation Indication, shall be removed or placed in a warning condition when the VOR Bearing is not valid. 

## 4.2.2 Distance Measuring Equipment (Dme)

This function provides DME range and associated indications. 

## 4.2.2.1 Display Parameters4

The EFIS should display unambiguous information to the flight crew. As a minimum, displays should provide distance information, warning indications and channel selection. As an alternative, the source of channel selection may be displayed. 

## 4.2.2.1.1 Dme Source Or Channel Indication

When DME sources or channels are paired with multiple navigation sources, the EFIS shall display the DME source or channel associated with the currently selected navigation source. 


## 4.2.2.1.2 Dme Range

The EFIS display shall indicate the currently selected DME range (distance). The EFIS shall indicate when the DME distance reported is not associated with the currently selected navigation source (DME HOLD). 

## 4.2.2.2 Dme Alerts 4.2.2.2.1 Dme Warning Indication5

The EFIS display shall provide a warning, such as a flag, when the DME equipment indicates that DME distance is not valid. 

## 4.2.2.3 Accuracy

The EFIS shall not significantly contribute to the DME range error.  The manufacturer shall define the 95% error in the installation manual.  The manufacturer shall provide instructions on determining total installed system error.   
The EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.2.3 Localizer 4.2.3.1 Localizer Display Parameters

The Localizer display parameters include the Localizer Deviation Indicator, and may include the localizer displayed frequency. 

## 4.2.3.2 Localizer Frequency

If tuning of the localizer receiver is a function of this EFIS, the frequency of paired channel or the identification of the navigation facility or facilities in active use shall be displayed or capable of recall at all times during flight. 

## 4.2.3.3 Localizer Deviation Indicator

The following requirements shall be met with valid input signals: The localizer deviation indicator shall present localizer deviation magnitude and direction. The displayed localizer deviation indicator shall have a sufficient dynamic range to display at least 0.155 depth of deviation modulation (ddm) left or right of center with a resolution of 0.016 ddm or better. 

NOTE: The localizer function shall detect a back course approach condition.  When a back course approach is detected, the localizer polarity shall be reversed.  

                                           

## 4.2.3.4 Accuracy

When provided with Display-Ready Data, the EFIS shall not contribute more than 0.008 ddm error to the displayed localizer deviation. If the localizer deviation data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS. The displayed error shall be documented in the installation manual. Over the deflection range from zero to 0.093 ddm, in no case shall the error be greater than 10% of the deviation produced by a 0.175 ddm input. NOTE: The error listed here - for an EFIS without Display-Ready Data - is for an *end-to-end system*, including sensors. 

This gives the EFIS display manufacturer flexibility to define the displayed error introduced by the display.  
In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.2.3.5 Localizer Alerts

The Localizer indication shall be removed or placed in a warning condition when the Localizer is not valid.  

## 4.2.4 Glideslope

The Glideslope function presents an indication of ILS Glideslope deviation, and may present an indication of the ILS paired channel frequency.  

## 4.2.4.1 Display Parameters For The Glideslope Function 4.2.4.1.1 Frequency Display

If tuning of the glideslope receiver is a function of this EFIS, the frequency of paired channel or the identification of the navigation facility or facilities in active use shall be displayed or capable of recall at all times during flight. 

## 4.2.4.1.2 Glideslope Deviation Indication

If a Glideslope Deviation indication is provided, the following requirements shall be met with valid input signals.  

## 4.2.4.1.2.1 Deviation Sensitivity6

The equipment shall provide a display for presentation of glideslope deviation magnitude and direction of deviation. This output shall have sufficient dynamic range to display 0.175 ddm above or below center with a resolution of 0.016 ddm or better. 

## 4.2.4.1.2.2 Deflection Response7

When the ddm of a standard glide slope test signal is abruptly changed from zero to any value less than ±0.175 ddm, the pointer shall reach 67% of its ultimate deflection within 2 seconds and pointer overshoot shall not exceed 5%. 

## 4.2.4.1.2.3 Glideslope Warnings

The Glideslope Deviation indication shall be removed or placed in a warning condition when the Glideslope is not valid.  
NOTE: Glideslope deviation is not valid in back course. 


## 4.2.4.1.2.4 Accuracy

When provided with Display-Ready Data, the EFIS shall not contribute more than 0.008 ddm error to the displayed glideslope deviation. If the Glideslope deviation data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS.  The error shall be no greater than 10% of the deviation produced by a 0.175 ddm input over the range of 0.0 to 0.091 ddm.  The display indication or electrical output shall be monotonic when the input difference in depth of modulation is varied over a range from 0.0 ddm to 0.800 ddm. The displayed error shall be documented in the installation manual.8 

NOTE: This error is defined for a display *system*, including the sensor(s). This gives the EFIS manufacturer flexibility to 
define the display tolerance error introduced by the EFIS.  However, the displayed error introduced by the EFIS should still be a small portion of the total system error budget, which has sensors not included here.    
The EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.2.5 Marker Beacon

This function provides display of marker beacons. For each of the three Marker Beacons, the Outer Marker Beacon annunciation shall be blue or cyan and labeled "O" or "OM", the Middle Marker Beacon annunciation shall be amber (or yellow or light brown) and labeled "M" or "MM", and the Inner Marker Beacon Annunciation shall be white and labeled "I" or "IM". 

## 4.2.6 Automatic Direction Finding (Adf)

This function provides display of ADF bearing and associated information. If tuning of the ADF is a function of this EFIS, then the frequency or the identification of the navigation facility or facilities in active use shall be displayed or capable of recall at all times during flight. 

## 4.2.6.1 Display Parameters

The EFIS shall display the ADF Bearing.  

## 4.2.6.2 Accuracy

When provided with Display-Ready Data, the EFIS shall not contribute more than ±0.5 degrees error to the displayed ADF bearing. 

If the ADF bearing data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS. This gives the EFIS manufacturer flexibility to define the display tolerance error introduced by the EFIS.  However, the displayed error introduced by the EFIS should still be a small portion of the total system error budget, which has sensors not included here. The displayed error shall be documented in the installation manual. In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 


## 4.2.7 Stand-Alone Airborne Navigation Equipment Using The Global Positioning System Augmented By The Satellite Based Augmentation System (Gps/Sbas) 4.2.7.1 Functionality

This function accepts a desired flight path and provides deviation commands keyed to that path on the EFIS display. Pilots use these deviations and SBAS displays to guide the aircraft. 

## 4.2.7.2 Color 9

No more than five colors should be used for display of SBAS information.  When color is used to distinguish between functions and indications, red shall not be used other than for warning indications (conditions that require immediate flightcrew awareness and immediate flightcrew response).  Amber (yellow) shall be reserved for caution indicators.  Blue should be avoided because it is difficult for the human eye to bring blue symbols into focus and to distinguish the color from yellow when the symbols are small.  

## 4.2.7.3 Alphanumerics10

Information critical to determining aircraft location and closure rate on the active waypoint, the waypoint name, and the desired track should be differentiated from other information, and located in a consistent manner (including order and position).  The initial approach, final approach, missed approach and missed approach holding waypoints shall be labeled clearly when used as part of an approach procedure.  If space limitations require the use of abbreviations, see 6.2 (this is a list of "Acronyms and Initialisms"). 

## 4.2.7.4 Selectable Navigation Display11

It is permitted to use a selectable display, in lieu of continuous display, for certain primary navigation display parameters.  If a selectable display is used for this purpose, reconfiguring the EFIS display to access the primary navigation information shall require no more than two operator actions. 

## 4.2.7.5 Bearing Labels12

All bearing data fields shall be labeled as "°" to the right of the bearing value.  All true bearing data fields shall be labeled as "°T" or "T" to the right of the bearing value. This applies to all courses, tracks, and bearings. 

## 4.2.7.6 Annunciations13

Warnings, annunciations, and messages not critical to the safety of instrument approaches or missed approaches should be suppressed during those phases of terminal operations. 

## 4.2.7.7 Messages14

If messages are displayed on the EFIS, messages should be grouped by urgency level and listed chronologically within each group.  All current messages shall be retrievable.  An indication shall be provided to identify new messages.  The EFIS 
display should also indicate when there are current messages. 

 

## 4.2.7.8 Set Of Standard Function Labels15

If a function is implemented as a discrete action, the EFIS display shall use the labels or messages in Table 7. Except for waypoint identifiers, these abbreviations shall not be used to represent a different term. 

| Function/Annunciation                      | Label/Message    |
|--------------------------------------------|------------------|
| Access to primary navigation display       |                  |
| NAV or MAP                                 |                  |
| [1]                                        |                  |
|                                            |                  |
| Indication that there is a message         | Message (MSG, M) |
| Indication of loss of integrity monitoring | LOI              |
| "Loss of Integrity - Cross Check Nav."     |                  |
| Indication of impending turn               |                  |
| WPT (flashing)                             |                  |
| [2]                                        |                  |
| ,                                          |                  |
|                                            |                  |
| or                                         |                  |
| "Turn to [next heading] in [distance] nm"  |                  |
| Indication of start of turn                |                  |
| WPT (continuously lit, not flashing)       |                  |
| [2]                                        |                  |
| , or                                       |                  |
| "Turn to [next heading] now"               |                  |

[1] If the primary navigation information is integrated on the same display as a moving map, the 
term "MAP" can be used. 
[2] This can be used to indicate other conditions (e.g., waypoint alerting). 

## 4.2.7.9 Channel Selection

If channel selection is performed through the EFIS, the five (5) digit channel selection shall be available for display. 

## 4.2.7.10 To/From Course Selection 16

The EFIS display shall provide an indication of whether the SBAS sensor is in "TO" or "FROM" operation. 

## 4.2.7.11 Fly-By Turn Indications17

The EFIS display shall provide an indication at the start of a defined turn as provided by the SBAS sensor to indicate to the pilot that the turn has begun. The EFIS display shall provide an indication prior to the start of a defined turn as provided by the SBAS sensor, to indicate to the pilot that a turn is anticipated.  
The EFIS display shall provide an indication of the desired course of the next active leg as provided by the SBAS sensor. 

NOTE: These requirements may be satisfied through the use of a moving map display if it is the primary navigation display 
and it provides adequate representation of the turn to ensure that the turn is initiated at the correct point. 

## 4.2.7.12 Parallel Offsets18

The parallel offset is defined as a route that is alongside, but offset from, the original active route.  The basis of the offset path is the original flight plan leg(s) and one or more offset reference points as computed by the SBAS sensor. When provided by the SBAS sensor, the fact that the EFIS is operating in offset mode shall be clearly indicated to the flight crew.  When in offset mode, the EFIS display shall provide reference parameters (e.g., cross-track deviation, distance-togo, time-to-go) relative to the offset path and offset reference points. An annunciation shall be given to the flight crew prior to the end of the offset path as provided by the SBAS sensor.  

## 4.2.7.13 Primary Navigation Display19

At a minimum, the non-numeric cross-track deviation shall be continuously displayed. At a minimum, the following navigation parameters shall be displayed, either continuously or on a selectable display: 

a. Active waypoint distance or estimated time en route to the active waypoint b. Active waypoint name c. Active waypoint bearing d. Desired track and actual track) or track angle error e. Indication of navigation "TO" or "FROM" the active waypoint 
Distance, bearing, desired track, actual track, and track angle error shall be distinguishable. 

## 4.2.7.14 Deviation Display Characteristics20

The EFIS display shall provide a non-numeric display of cross-track deviation. If LNAV/VNAV or LPV is provided, the EFIS display shall provide a non-numeric display of vertical deviation. Lateral and vertical non-numeric deviation displays shall have the following characteristics shown in Tables 8 and 9. 

| Characteristic/Attribute                      | Requirement (% of Full-Scale)    |
|-----------------------------------------------|----------------------------------|
| Readability                                   |                                  |
| [1]                                           |                                  |
|                                               | 10%                              |
| Minimum Discernible Movement                  | x2%                              |
| Displayed Error: Accuracy of Centered Display | 3%                               |
| Displayed Error: Linearity of Display         | 5%                               |

[1] Readability refers to the ability to determine the magnitude of a deviation (as a percentage of full-scale deflection. 

 

Full-Scale Deflection[1] 
Navigation Mode 
(Nominal) 
En Route 
2 Nautical Miles (NM)  
Terminal 
1 NM 
LNAV or LNAV/VNAV Approach 
Angular/Linear 
LPV or LP Approach 
Angular/Linear  

[1] The full-scale deflection or scale factor for display of Non-Numeric Cross-Track Deviation may be 
provided by the SBAS sensor. 

## 4.2.7.15 Displayed Data Update Rate 21

The EFIS display shall update non-numeric deviation data at a rate of 5 Hz or more.   

## 4.2.7.16 Active Waypoint Distance Display22

When in "TO" operation, the distance to the active waypoint shall be displayed.  When in "FROM" operation, the distance from the active waypoint shall be displayed.  The distance shall be displayed with a resolution of 0.1 NM up to a range of 99.9 NM from the waypoint, and 1 NM between 100 and 9999 NM. NOTE: A moving map may obviate the need for a numerical display. 

## 4.2.7.17 Active Waypoint Bearing Display23

The EFIS display shall provide the capability to display bearing "TO" the active waypoint. The EFIS may provide the capability to display the bearing "FROM" the active waypoint.  If this capability is provided, there shall be an indication of whether the displayed bearing is "TO" the waypoint or "FROM" the waypoint.  The bearing shall be displayed with a resolution of one degree.  The EFIS display shall be capable of displaying the bearing in true or magnetic bearing as selected. NOTE: A moving map may obviate the need for a numerical display. 

## 4.2.7.18 Caution Associated With Loss Of Navigation24

If provided by the EFIS system, the EFIS shall continuously provide a caution, independent of any operator action that indicates the loss of navigation capability.  This caution may be implemented by an annunciation on the primary navigation display.  The conditions for the loss of navigation caution are provided by the SBAS sensor. 

The total system latency for display of loss of navigation caution is defined in RTCA/DO-229D.  No more than a maximum latency of 200 msec should be allocated to the EFIS. NOTE: A loss of navigation alert does not require removal of navigation information from the navigation display.  

Consideration should be given to continued display of navigation information concurrent with the failure/status 
annunciation when conditions warrant. 

## 4.2.7.19 Caution Associated With Loss Of Integrity Monitoring25

The EFIS display shall provide a loss of integrity monitoring caution. The conditions for loss of integrity monitoring caution are provided by the SBAS sensor. The loss of integrity monitoring caution should not result in the removal of navigation information from the navigation display. Example implementations that satisfy this requirement include a pop-up message at the onset of this condition ("Loss of Integrity - Crosscheck Nav") and another message when monitoring is restored ("Integrity Restored - Normal Ops"). The first message may be accompanied by a unique and continuous annunciator ("LOI") that turns on when there is no integrity monitoring and turns off when integrity monitoring is restored.  Alternative implementations of the caution annunciation may be employed. The total system latency for display of loss of integrity monitoring caution is defined in RTCA/DO-229D.  No more than a maximum latency of 200 msec should be allocated to the EFIS. 

## 4.2.7.20 Navigation Mode Display26

The EFIS shall display the current navigation mode as provided by the SBAS sensor upon user request.  Navigation modes are: En Route, Terminal, LNAV Approach, LNAV/VNAV Approach, LPV Approach or LP Approach. 

## 4.2.7.21 Numeric Cross-Track Deviation27

The EFIS shall provide a display of numeric cross-track deviation as provided by the SBAS sensor. The range of the display shall be at least ±20 NM (left and right).  The EFIS display shall provide a resolution of 0.1 NM for deviations up to 9.9 NM, and a resolution of 1 NM for deviations greater than 9.9 NM. 

## 4.2.7.22 Missed Approach Waypoint Distance Display28

The distance to the missed approach waypoint (MAWP) shall be available for display as provided by the SBAS sensor.  The distance shall be displayed with a resolution of 0.1 NM up to a range of 99.9 NM.  Design consideration should be given to avoid confusion between the waypoint distance display and the MAWP distance display. Note: If a moving map is provided, the map may obviate the need for a numerical output. 

## 4.2.7.23 Missed Approach Waypoint Bearing Display29

The bearing to the missed approach waypoint (MAWP) shall be available for display as provided by the SBAS sensor.  The bearing shall be displayed with a resolution of one degree. The EFIS shall be capable of displaying the bearing in true or magnetic bearing as selected.  Note: If a moving map is provided, the map may obviate the need for a numerical output. 

## 4.2.7.24 Missed Approach Waypoint/Ltp/Ftp Distance Display30

If LNAV/VNAV or LP/LPV is provided, the distance to the LTP/FTP shall be available for display as provided by the SBAS sensor.  The distance shall be displayed with a resolution of 0.1 NM up to a range of 99.9 NM.  Note: If a moving map is provided, the map may obviate the need for a numerical output. Note: Design consideration should be given to avoid confusion between the waypoint distance display and the MAWP/LTP/FTP distance display. 


## 4.2.7.25 Missed Approach Waypoint/Ltp/Ftp Bearing Display31

If LNAV/VNAV or LP/LPV is provided, the bearing to the LTP/FTP shall be available for display as provided by the SBAS sensor.  The displayed bearing shall have a resolution of 1 degree. The EFIS shall be capable of displaying the bearing in true or magnetic bearing as selected. Note: If a moving map is provided, the map may obviate the need for a numerical output. 

## 4.2.7.26 Low Altitude Alert32

If LNAV/VNAV or LPV is provided, the EFIS shall display a low altitude alert as provided by the SBAS sensor. Low altitude alert is not required if a TAWS function (e.g., TSO-C151) is provided. 

## 4.2.7.27 Alerting Scheme33

Vertical and lateral integrity flags shall be out of view under normal (non-alerting) operation. 

## 4.2.7.28 Advisory Of Lnav/Vnav Availability34

If LNAV/VNAV is provided, the EFIS display shall indicate if LNAV/VNAV is not available as provided by the SBAS sensor. 

## 4.2.7.29 Landing Threshold Point/Fictitious Threshold Point Distance Display35

If LP/LPV is provided, the distance to LTP/FTP shall be displayed whenever the EFIS is outputting valid lateral deviations. The distance to LTP/FTP is provided by the SBAS sensor. The distance shall be displayed with a resolution of 0.1 NM up to a range of 99.9 NM from the waypoint. NOTE: If a moving map is provided, the map may obviate the need for a numerical output. 

## 4.2.8 Flight Management System Using Multi-Sensor Inputs

It is acknowledged that some designs will only include the EFIS portion while others will provide solutions of EFIS integrated with a control unit, e.g., a Multifunction Control Display Unit (MCDU) or Control Display Unit (CDU).  

## In The Latter Case, It Is Recommended To Seek An Approval Under Tso-C115C.

For EFIS-only designs, the EFIS shall comply with the requirements of this section.  

## 4.2.8.1 Requirements Related To Electronic Map Display

If the EFIS includes Flight Management System (FMS) and Electronic Map Display (EMD) capability, the requirements in this section supersede the related requirements from TSO-C165a and RTCA/DO-257a documents.  If the EFIS includes EMD, but does NOT include FMS, applicants will need to apply for TSO-C165a approval for the EMD separately. If an EMD is included in order to provide course guidance to satisfy the RNP RNAV, it shall meet the minimum standards defined in DO-283A Appendix K.  The appropriate requirements in that RNP MOPS shall also apply to the EMD when it is used to satisfy the RNP display and systems alerting functions. 


## 4.2.8.1.1 Symbology

The display of navigation information shall not be overwritten by lower priority information. It shall always be possible to view navigation information. This may be achieved by manual de-selection of other data. The definition of navigation information can be found in RTCA/DO-283A, Appendix K, Section 1.1.  

## 4.2.8.1.2 Path Depiction

Fixes within a flight plan shall be represented by four-point star symbols. Examples of acceptable symbols for fixes can be found in RTCA/DO-283A, Figure K-2, and in ARP4102-7B or ARP5289. If RNAV is provided, then the EFIS shall be capable of depicting all RNP RNAV leg types, including initial fix (IF), track-tofix (TF), radius-to-fix (RF), fix-to-altitude (FA), direct-to-fix (DF), course-to-fix (CF), and holding legs. The definitions for these leg types can be found in RTCA/DO-283A Appendix D. Straight and curved lines shall be used to indicate the defined path between their associated fixes and any other flight path segments as appropriate. If RNP is provided, then the RNP path depiction shall be a scaled representation of the defined path over the ground. 

The display error is assumed to be negligible. Therefore, if RNAV approval is sought for the EFIS, the ownship symbol and each fix and each point of the defined path on the display shall be positioned such that placement errors are less than 0.013 inches on each map scale, or 3% of the RNP RNAV type in effect, whichever is greater. Note: This requirement corresponds to a visual arc of about 2 minutes for a typical cockpit viewing distance, which corresponds to the human threshold of position discernibility and to the typical pixel of off-the-shelf LCD displays. Upon pilot selection, the EFIS should provide the capability to display current and any portion of upcoming flight plan legs and fixes. 

## 4.2.8.1.3 Offset Requirements

The following requirements apply when an offset is selected: 

1. fixes for a flight plan shall always be shown at their actual geographic positions rather than being displaced by the value 
of the offset; 
2. the appearance of a potential offset, active offset, and defined path of the flight plan shall each be distinguishable from 
each other. 
NOTE: The representation of the defined offset path fulfills the requirements for both indicating that an offset is in effect 
and that the end of an offset is impending (reference DO-283A section 2.2.2.7). 

## 4.2.8.1.4 Holding Pattern

The EFIS shall be capable of representing the holding pattern as a symbol or path that indicates the position, orientation, and turn direction. 

The EFIS should be capable of showing the straight and curved segments of the hold scaled according to the selected map range. 

NOTE: A depiction of the path is preferred when the map scale would make it easy to interpret. If the entry and exit paths are available to the EFIS, then they shall be depicted. 

 

## 4.2.8.1.5 Track, Track Angle, And Next Fix

The following information shall be continuously available for pilot selection: 

- 
desired track 
- 
track angle 
- 
bearing and distance to next fix 
NOTE: It is acceptable to switch between a numeric and non-numeric representation of this information to satisfy the above 
requirement across all conditions. 
A non-numeric representation of track angle or track angle error shall include: 

- 
graduation marks for compass bearings at least every 10 degrees 
- 
labels for graduation marks at least every 30 degrees 
- 
a range sufficient to show at least two graduation labels at all times 
- 
distinct markings for desired track and track angle 
NOTE: If the EFIS is to be used to satisfy requirements for the display of track angle and track angle error, then it may be 
necessary to provide graduation marks every 5 degrees combined with major graduation marks every 10 degrees in order to meet resolution requirements in this document. 

## 4.2.8.1.6 Display Of Desired Track

The EFIS shall provide a numeric display of desired track with a resolution of 1 degree or better.  

## 4.2.8.1.7 Display Of Track Angle

The EFIS shall provide a display of track angle with a resolution of 1 degree or better. The EFIS should provide a display of track angle error with a resolution of 1 degree or better.  

## 4.2.8.1.8 Failure Indication

A failure of the map display shall be continuously evident from the EFIS display itself (e.g., a flag or removal of the map) for as long as the failure condition exists. 

The display of such a continuous failure indication on the EFIS display should not interfere with other functioning information on the display. An alert shall be displayed if updating of the map on the EFIS is lost. 

## 4.2.8.1.9 Layers And De-Cluttering

Any navigation information within the EFIS selected map range shall only be removed from the display by crew action. NOTE: This does not preclude the use of automatic decluttering of information that is not navigation information. 

 
 
The EFIS shall be capable of indicating the current level of declutter. 

NOTE: One way to satisfy this requirement is to annunciate what layers are displayed. "Layers" include categories of 
information such as airports, VORs, etc. 
NOTE: The level of declutter may be on the display or its associated control panel if one exists. 

## 4.2.8.1.10 Range

The minimum map range shall be 10 NM or less. The maximum map range shall be 160 NM or more. NOTE: A maximum range of 640 NM is desirable for use on oceanic routes. 

NOTE: For RNP based operations where RNP < 1 NM, and depending on the physical size of the map display, it may be 
necessary to provide for a map range of 5 NM or less to assure acceptable resolution for evaluating path deviation and path keeping awareness. 
When the map display on the EFIS is the only non-numeric source for cross-track deviation, the map scaling shall meet the requirements of RTCA/DO-283A section 2.2.4.1.2. 

NOTE: It should be recognized that this is not the optimal configuration because broader situation awareness benefits of 
the map display will be compromised. Therefore, it is strongly encouraged that the required non-numeric crosstrack deviation display be separate from the traditional map display. 
When the ownship symbol is fixed (e.g., track-up mode), the EFIS display should show the map scale information with reference marks and labels relative to the ownship symbol (examples provided in RTCA/DO-283A, Figure K-3). When the ownship symbol is fixed, the EFIS should provide capability to display the area completely around the ownship position such that some area behind the aircraft is visible. 

## 4.2.8.2 Horizontal Navigation Requirements 4.2.8.2.1 Flight Plans

The EFIS shall provide the capability for the crew to review flight plans. The displayed guidance shall not be affected until the modification(s) to a flight plan is/are activated. The EFIS display shall indicate to the crew any flight plan discontinuities.  

## 4.2.8.2.2 Display Of Parallel Offsets

The parallel offset path shall be located along the lines drawn parallel to the host route at the desired offset distance, intersected by the line that bisects the track change angle. An exception to this occurs if there is a route discontinuity (or end of route). In this case, the offset reference point shall be located abeam of the original flight plan waypoint at the offset distance.  

## 4.2.8.2.3 Display Of Rnp Value

If RNP is provided, the EFIS shall provide the capability to readily distinguish a RNP value manually entered by the flight crew or automatically provided via the navigation database.  

## 4.2.8.2.4 Indication Of Fix/Leg Sequencing

The EFIS display shall indicate to the crew an impending flight plan leg change.  

## 4.2.8.2.5 Non-Numeric Display Of Cross-Track Deviation

If the EFIS provides non-numeric display of cross-track deviation, the EFIS shall also display the non-numeric scale sensitivity, i.e., full scale deflection. Transitions in scale sensitivity shall be accomplished smoothly and shall be annunciated. The display shall be scaled based on the currently selected RNP type, as defined in RTCA/DO-283A Table 2-2.   

NOTE: For display formats employing the traditional two dots of deviation either side of a centered deviation indication, the 
display should be scaled to meet the full scale deflection indicated in RTCA/DO-283A Table 2-2 when aligned at the second dot of deviation. 
If the EFIS provides the non-numeric display of cross-track deviation, the EFIS shall continuously provide a display meeting the characteristics (full scale deviation, readability, minimum discernible movement, accuracy of centered display, and linearity) per RTCA/DO-283A Table 2-3. 

## 4.2.8.2.6 To-From Indication

If appropriate, the EFIS shall provide a continuous display showing whether the aircraft is behind or ahead of the active fix relative to an imaginary line perpendicular to the defined path and passing through the active fix. 

NOTE: A To-From indication may be desired during the transition to the RNP RNAV operational environment. It may also 
be desirable in installation where a moving map display is not provided, to provide adequate situational awareness, for example during holding patterns and off-path vectoring situations. 

## 4.2.8.2.7 Display Of Fix Identification

Provisions shall be made to display the identification of the active fix, the next fix in the flight plan, and the destination. These fix identifications need not be displayed simultaneously.  

NOTE: When an offset is active, the EFIS may display the identifier of original fixes. Because offsets are the result of pilot 
action, the pilot should be aware that tactical data (e.g., distance-to-go, ETA, etc.) are related to the offset path and not to the original path.  

## 4.2.8.2.8 Display Of Ground Speed

The EFIS shall provide a display of groundspeed with a minimum resolution of 1 knot.  

## 4.2.8.2.9 Indicating And Alerting

If RNAV/RNP is provided, then the EFIS shall display indications and alerts from the navigation system per RTCA/DO-283A 
section 2.2.4.11. 

## 4.2.8.2.10 Display Of Estimate Of Position Uncertainty (Epu) Value

The equipment shall provide a display of the current estimated position uncertainty (EPU) in nautical miles.  The resolution for displayed EPU shall be 0.01 NM or better. If RNAV/RNP is provided and the EFIS display meets requirements of 0 (nonnumerical display of cross-track deviation), then the EFIS shall display the scaled EPU value computed by the navigation system. The displayed EPU shall be scaled such that the containment alert occurs no later than when the displayed EPU value exceeds the RNP RNAV type in effect. 

## 4.2.8.3 Vertical Navigation Requirements

If vertical navigation is displayed on the EFIS, then the following requirements apply: 
 

## 4.2.8.3.1 Direct-To Path Guidance

The EFIS shall support the guidance generated by the navigation system to fly a path from the current position to a vertically constrained fix. NOTE: The navigation system can generate guidance cues to be displayed for the flight crew to fly the computed path (e.g., display of Vertical Speed Required or display of computed Flight Path Angle). 

## 4.2.8.3.2 Display Of Primary Flight Information

The EFIS shall display present airspeed, vertical speed, altitude, attitude, and heading, respectively, per 4.1.1, 4.1.2, 4.1.3, 4.1.4, and 4.1.5 of this MOPS. 

## 4.2.8.3.3 Display Of Vertical Deviations

The EFIS display shall depict deviation from the desired vertical path provided by the navigation system. The EFIS display shall provide a numeric display of vertical path steering error. The vertical path steering error shall be displayed with a resolution of not less than 10 feet. The non-numeric vertical deviation information shall use full-scale deflection suitable to the operation and consistent with the accuracy requirements in DO-283A section H.2.1. The non-numeric vertical deviation value shall be annunciated or available for display to the flight crew. NOTE: Angular deviation indications may be unsuitable for VNAV operations for long leg lengths. Non-numeric vertical deviation information shall be displayed during all phases of flight operations where there is a defined path. Displayed vertical deviation information shall be clear and unambiguous. The vertical deviation information may also be displayed numerically, in addition to, but not in lieu of, the non-numeric depiction.  

NOTE: The preferred location of the vertical deviation information is on either the primary flight display (PFD) or the attitude 
director indicator (ADI). It may be acceptable to provide this information on the navigation display (ND) or horizontal situation indicator (HSI). Presentation of this information solely on the control display unit (CDU) may not be acceptable. The location of numeric vertical deviation information should be consistent with its intended function during vertical navigation operations.  

## 4.2.8.3.4 Display Of Altitude Predictions

The EFIS shall be capable of displaying altitude prediction for the active fix as provided by the navigation system. The capability to display altitude predictions for other fixes in the flight plan is recommended. 

## 4.2.8.3.5 Indication Of Transitions To/From Level Flight

The EFIS shall be capable of displaying a transition to/from level flight. 

NOTE: It is intended that a system capable of performing a vertical transition provide an indication of the impending 
maneuver along with a requirement for timely flight crew acknowledgment of the maneuver prior to conducting it. Flight crew use of a separate altitude preselector for both altitude selection and subsequent acknowledgement is 
one method that has been used. 

## 4.2.8.3.6 Display Of Altitude Restrictions

The EFIS shall be capable of displaying altitude restrictions associated with flight plan fixes. If there is a flight path angle defined in the database for any leg of an approach procedure, the EFIS shall display the flight path angle for that leg. 

 

## 4.2.8.3.7 Visual Indication Of Vertical Crossing

The EFIS shall be capable of displaying a visual indication (e.g., top-of descent, turn anticipation cues, etc.) of impending vertical fix crossing as provided by the navigation system.   

## 4.2.9 Microwave Landing System (Mls)

The MLS function presents an indication from a ground-based time reference scanning beam Microwave Landing System.    

## 4.2.9.1 Display Parameters For The Mls Function 4.2.9.1.1 Course Deviation Display

The following course deviation display requirements shall be met with valid input signals.  

## 4.2.9.1.1.1 Deflection Range36

The course deviation pointer shall deflect at least ⅝ inch along its scale when the deviation equals full-scale value. 

## 4.2.9.1.1.2 Deflection Direction37

When the measured angle is algebraically greater than the reference angle, the deviation pointer shall deflect to the RIGHT (approach azimuth) or DOWN (elevation). 

## 4.2.9.1.1.3 Deflection Linearity38

Over the deflection range from zero to full scale, the deflection shall be within 10% of being proportional to the course deviation from centerline or within 2.6% of the full-scale value, whichever is greater. If the course deviation pointer data for the display is not Display-Ready Data, the manufacturer shall determine the maximum error contributed by the EFIS. The displayed error shall be documented in the installation manual. In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.2.9.1.1.4 Deflection Response39

When the azimuth or elevation angle is stepped by 0.2 degree, the visual output shall reach 67% of its ultimate values within 2.0 seconds.  

## 4.2.9.1.2 Selected Channel Display

If the EFIS is being used as a MLS controller, then a visual display of the selected MLS channel shall be provided. 


## 4.2.9.2 Mls Controllers40

If the EFIS is being used as a MLS controller, then the channel selection shall be made from the range of channels/frequencies in Table 9.  To save space, only the beginning six and the last five pairings of channels and associated frequencies are listed for the entire range of channels and frequencies. To determine other pairings, the nominal center frequencies of the MLS angle and data signals are separated by 300 kHz. (The ICAO assigned channel numbers are included for information only.) 

| Channel    | Frequency    |
|------------|--------------|
| 500        | 5031.0       |
| 501        | 5031.3       |
| 502        | 5031.6       |
| 503        | 5031.9       |
| 504        | 5032.2       |
| 505        | 5032.5       |
| ….         | ….           |
| 695        | 5089.5       |
| 696        | 5089.8       |
| 697        | 5090.1       |
| 698        | 5090.4       |
| 699        | 5090.7       |

## 4.2.9.3 Mls Warnings

The EFIS shall display clearly discernible warnings (e.g., a flag) produced by the MLS to warn the pilot of improper or unreliable guidance. 

## 4.2.10 Vhf Radio

This function displays VHF Radio Channel information. The VHF communications equipment utilizes amplitude modulation and operates on assigned channels spaced 25 and/or 8.33 kHz apart within the radio-frequency range 117.975 to 137.000 MHz. NOTE: The above operational frequency range limitations may not apply to all receiver transmitters and their associated display. For some applications the receiver transmitter may be capable of tuning channels outside of these limits. 

This function shall meet either or both the 8.33 or 25 kHz channel separations identified in TSO-C169a, paragraphs 3(b) and 3(c). 


                                           
 

## 4.2.10.1 Display Parameters For Vhf Radio Function 4.2.10.1.1 Channel Labeling/Identification41

When the equipment displays channel information, the equipment shall display Channel Identifiers for the currently tuned channel in accordance with the frequency-channel pairing plan shown in Table 11. The channel identification used within this radio-frequency range is based on the following frequency-channel pairing plan, which allows unique identification of the 8.33 kHz channels. 

|          | Frequency    | Channel Spacing        |
|----------|--------------|------------------------|
| (MHz)    | (kHz)        | Channel Identification |
| 118.0000 | 25/50        | 118.000                |
| 118.0000 | 8.33         | 118.005                |
| 118.0083 | 8.33         | 118.010                |
| 118.0167 | 8.33         | 118.0l5                |
| 118.0250 | 25           | 118.025                |
| 118.0250 | 8.33         | 118.030                |
| 118.0333 | 8.33         | 118.035                |
| 118.0417 | 8.33         | 118.040                |
| 118.0500 | 25/50        | 118.050                |
| 118.0500 | 8.33         | 118.055                |
| 118.0583 | 8.33         | 118.060                |
| 118.0667 | 8.33         | 118.065                |
| 118.0750 | 25           | 118.075                |
| 118.0750 | 8.33         | 118.080                |
| 118.0833 | 8.33         | 118.085                |
| 118.0917 | 8.33         | 118.090                |
| 118.1000 | 25/50        | 118.100                |
| etc.     |              |                        |

## 4.2.10.1.2 Display Of Channels Other Than The Currently Tuned Channel

When the equipment displays any channel information other than the currently tuned channel, the presentation format shall clearly distinguish the currently tuned channel from any other channel displayed. NOTE: "Channels other than currently tuned channel" may include standby, emergency, or other pre-selected channel information. 

## 4.2.11 Hf Radio

This function displays HF Radio Channel information. 

## 4.2.11.1 Display Parameters For Hf Radio Function 4.2.11.1.1 Channel Identifiers

When the equipment displays channel information, the equipment shall display the frequency of the currently tuned channel. 

## 4.2.11.1.2 Display Of Channel Identifiers Other Than The Currently Tuned Channel

When the equipment displays any channel information other than the currently tuned channel, the presentation format shall clearly distinguish the currently tuned channel from any other channel displayed. 

NOTE: "Channels other than currently tuned channel" may include standby, emergency, or other pre-selected channel 
information. 

## 4.3 Engine And Fuel Management Functions 4.3.1 Temperature

Indications beyond the normal range shall not be displayed in a manner interpretable as an on-scale reading or as an offscale reading in the wrong direction. If applicable, relative motion of the index with respect to the scale (either the index or the scale may be the moving element) shall be clockwise, up, or to the right for increasing temperature. 

Sufficient numerals and graduations shall be provided to positively and quickly identify temperature indications. The label "°C", "°F", "°K", "C", "F", or "K", as appropriate, shall be displayed. 

## 4.3.1.1 Accuracy

The manufacturer shall determine the maximum displayed error contributed by the EFIS, and shall classify the resulting EFIS displayed error as defined in Table 12.  The displayed error shall be documented in the installation manual. NOTE: The error tolerances listed in Table 12 are defined for a display system, including the sensor(s). This gives the EFIS 
manufacturer flexibility to define the displayed error introduced by the display.   
In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. In the event that a non-uniform tolerance is required, compliance is demonstrated if the error at any calibration point does not exceed the value appropriate for that point. 

|          |                          | Class I                          | Class II    | Class III              |
|----------|--------------------------|----------------------------------|-------------|------------------------|
| Class Ia | ±0.1% of indicated range | Class IIa ±1% of indicated range | Class IIIa  | ±2% of indicated range |
| Class Ib | ±0.2% of indicated range |                                  |             | Class IIIb             |
| Class Ic | ±0.5% of indicated range |                                  |             | Class IIIc             |

## 4.3.1.2 Marking

The manufacturer shall indicate the applicable class, accuracy, and operating range on the Declaration of EFIS Functions Form, and shall include the form in the installation manual. 

## 4.3.2 Fuel Flow 4.3.2.1 Indicating Method 4.3.2.1.1 Type I (Rate Of Flow)

Indicate rate of flow with a rotating pointer with fixed graduated dial, counter type indication, or bar graphs.  Clockwise pointer motion shall indicate increasing rate of flow. If bar graphs are used, scale shall be marked beside the bar graph (increasing flow rates increase the size/length of the bar). 


## 4.3.2.1.2 Type Ii (Totalizer)

A counter shall be employed to indicate either the fuel consumed or quantity remaining. A means shall be provided to initialize or reset the fuel consumed or quantity remaining indications. Major graduations shall be used at intervals not to exceed 10% full scale unless accompanied by a digital readout. If a digital readout is not provided, then sufficient numerals shall be marked to identify positively and quickly all graduations. Numerals shall distinctly indicate the graduations to which each applies. Units of measure shall be displayed on the indication.  

## 4.3.3 Manifold Pressure 4.3.3.1 Indicating Means

The functions shall be indicated by means of one or more pointers, dials, tapes, drums, digital displays or other devices. 

Unless otherwise specified, relative motion of the index with respect to the scale when moving elements are employed (either the index or the scale may be the moving element) shall be clockwise, up or to the right for increasing values.  When the EFIS displays manifold pressure for more than one engine, then the pointers or other indicating means shall be clearly identified (for example, as 1 and 2 or left and right). 

## 4.3.3.2 Graduations

The graduations shall be arranged to provide the maximum degree of readability consistent with the accuracy of manifold pressure indication. 

## 4.3.3.3 Numerals

The display shall include sufficient numerals to permit quick and positive identification of each significant graduation. 

## 4.3.3.4 Ambiguity

Appropriate means shall be provided to prevent ambiguous indications within the extremes of the operating range.  

## 4.3.3.5 Accuracy

The EFIS shall not contribute more 0.2 inch (0.5 cm) Hg error to the displayed pressure. The EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.3.3.6 Identification

The manifold pressure indication shall be marked with MANIFOLD PRESSURE, MANIF PRESS, MAN, MAP, or any other unambiguous abbreviation.   

## 4.3.3.7 Units Of Measure

The units of measure (in Hg abs or cm Hg abs) shall be clearly legible.  

## 4.3.3.8 Damping

If the damping is done on the display, then the time for the indicator to traverse the interval from full scale to zero shall be within 1.0 to 3.0 seconds. 

 

## 4.3.4 Fuel, Oil, And Hydraulic Pressure 4.3.4.1 Indicating Means

The pressure shall be indicated by means of a visual display such as pointer(s) moving over a fixed dial, digital counter, etc. The graduations shall be arranged to provide the maximum readability consistent with the accuracy. The display shall include sufficient numerals to permit quick and positive identification of each graduation.  Numerals shall distinctly indicate the graduation to which each applies. 

## 4.3.4.2 Accuracy

The EFIS shall not contribute more than ±0.75% of the full scale value to the displayed pressure (displayed error). The EFIS shall be tested to confirm that it meets the appropriate displayed error. The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.3.5 Tachometer 4.3.5.1 Indicating Means

Indication: Engine speed shall be indicated by means of one or more moving pointers or dials. Relative movement of the pointer with respect to the dial shall be clockwise for increasing revolutions per minute (RPM). Graduations: All graduations shall be multiples of 10 RPM. The increment between graduations shall not exceed 2.5% of full scale, above 600 RPM unless accompanied by a digital readout. Numerals: Sufficient numerals shall be marked to identify positively and quickly all graduations. 

## 4.3.5.2 Accuracy

The manufacturer shall determine the maximum error contributed by the EFIS.  The displayed error shall not exceed the following: Scale error tolerance at room temperature: 25 RPM over the range of indicated speed between 600 and 2800 RPM; 40 RPM over the range of indicated speed between 3000 and 4500 RPM. The displayed error shall be documented in the installation manual.  
NOTE: The errors defined above are for a display system, including the sensor(s). This gives the EFIS manufacturer flexibility to define the displayed error introduced by the display.   
In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.3.6 Fuel And Oil Quantity 4.3.6.1 Indicating Means

The quantity shall be indicated by means of a pointer and/or by means of a digital readout. Graduations: The intervals employed shall be determined by the capacity of the tank and the scale length in order to have a scale having sufficient graduations and numerals for easy reading without overcrowding. 

 
 
Numerals: Sufficient numerals shall be marked to identify positively and quickly all graduations. Numerals shall distinctly indicate the graduations to which each applies. Mark the indication with the word "Fuel Quantity" or "Oil Quantity" or an equivalent unambiguous abbreviation (e.g., Fuel Qty), whichever is applicable.  The inscription "lbs." or "gals." or equivalent shall be displayed. 

## 4.3.6.2 Speed Of Response (Damping)

The indicator shall register from empty to full or vice versa in less than 30 seconds but more than 5 seconds. 

## 4.3.6.3 Accuracy

The manufacturer shall determine the maximum error contributed by the EFIS.  The displayed error at room temperature shall not exceed the following: The percent of error at any point in the scale shall not exceed 3% of full scale indications for fuel gauges and 6% for oil gauges. 

The displayed error shall be documented in the installation manual. NOTE: The errors defined above are for a display system, including the sensor(s). This gives the EFIS manufacturer flexibility to define the displayed error introduced by the display.   

## 4.4 Weather Surveillance And Avoidance Functions

In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.4.1 Windshear Warning And Escape Guidance 4.4.1.1 Windshear Caution Alert

The EFIS shall provide an annunciation of increasing performance shear (updraft, increasing headwind, or decreasing tailwind) as indicated by the windshear sensor. This caution alert shall display or provide an appropriate output for display of an amber caution annunciation labeled "windshear" dedicated for this purpose. The visual alert should remain at least until the threshold windshear condition no longer exists or a minimum of 3 seconds, whichever is greater. 

## 4.4.1.2 Windshear Warning Alert

A windshear warning alert shall provide an annunciation of decreasing performance shear (downdraft, decreasing headwind, or increasing tailwind) as indicated by the windshear sensor. 

This warning alert shall display or provide an appropriate output for display of a red warning annunciation labeled "windshear" dedicated for this purpose. The visual alert should remain at least until the threshold windshear condition no longer exists or a minimum of 3 seconds, whichever is greater. 

## 4.4.1.3 Windshear Escape Guidance

Flight guidance command information shall be provided for presentation on the primary flight display/attitude direction indicator (PFD/ADI). Flight guidance displays that command flight path and pitch attitude should be limited to an angle-of-attack equivalent to onset of stall warning or maximum pitch command of 27 degrees, whichever is less. 

 
Flight guidance commands and any auto recovery mode (if included) may be automatically activated concurrent with or after the windshear warning alert occurs or may be manually selected. If manual selection is utilized, it shall only be via the takeoff-go around (TOGA) switch or equivalent means (i.e., a function of throttle position, other engine parameters, etc.).  
Manual deselection of windshear flight guidance and any auto recovery mode (if included) shall be possible by means other than the TOGA switches. Systems incorporating automatic reversion of flight guidance commands from windshear escape guidance to another flight guidance mode should provide a smooth transition between modes. Flight guidance commands shall not be removed from the flight guidance display until either manually deselected or until the aircraft, following exit of the warning conditions, has maintained a positive rate of climb and speed above 1.3 Vs1 for at least 30 seconds. 

## 4.4.2 Weather And Ground Mapping Radar 4.4.2.1 Display Parameters For Weather And Ground Mapping Radar

This function displays weather and ground mapping radar imagery relative to the aircraft position, range scale, and range markers.  This function may also display related symbology and text. 

## 4.4.2.2 Size Of Display

The maximum trace length shall be at least two inches for the "dead-ahead" indication, and at least 1 and 1/2 inches for indications at the +40 degrees and -40 degrees from dead-ahead. If multiple compass formats are available on the display, all formats shall be sized sufficiently to be used for their intended function. At least one of the display formats shall meet the maximum trace length requirement. The apparent spot size shall be sufficiently small to permit the dead-ahead trace to be resolved into at least 50 equal increments. 

## 4.4.2.3 Indicator Legibility

The indicator shall be useable from a high level of incident illumination to total darkness. It should be noted that levels up to 20000 lux are frequently encountered. A control may be provided for adjustment of brightness. The displayed image shall have adequate resolution and uniformity of brightness and color. 

## 4.4.2.4 Azimuth 4.4.2.4.1 Area Scan And Display

The equipment shall be capable of displaying at least that sector that is within ±40 degrees of the dead-ahead position, excluding that portion of the sector that is limited by the minimum detection range specified in 4.4.2.8. 

## 4.4.2.5 Bearing Accuracy

The manufacturer shall determine the maximum displayed error contributed by the EFIS.  The error contributed by the EFIS 
shall not exceed the following: 
With zero pitch-and-roll signals applied to the scanner, the indicator sweep line shall indicate the angular position of the antenna beam center to within ±3 degrees.42 
 
                                            

NOTE: The error defined above is for a display *system*, including the sensor(s). This gives the EFIS manufacturer flexibility 
to define the displayed error introduced by the display.  However, the displayed error introduced by the EFIS should still be a small portion of the total system error budget, which has sensors not included here. The displayed error shall be documented in the installation manual. 
In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.4.2.6 Range 4.4.2.6.1 Indicator Range Scale43

At least one range scale shall display a maximum range of between 100 and 250% of the system design range.  If the maximum displayed range is more than 75 nautical miles, there shall be at least one additional scale that displays a range of not more than 60 nautical miles. 

## 4.4.2.6.2 Range Markers44

Any range scale capable of displaying the maximum range for which the system is designed shall have at least two range markers.  Other range scales shall be provided with at least one range marker. If multiple compass formats are available on the display, all formats shall provide sufficient range indications to be used for their intended function. At least one of the display formats shall meet the range marker requirement. 

## 4.4.2.7 Indicated Distance Accuracy

The error in the indicated distance, measured at the pulse edge, shall not exceed 5% of the selected range or 1/2 NM, whichever is greater.45 The manufacturer shall determine the maximum error contributed by the EFIS.  The error contributed by the EFIS shall not exceed the error listed above.  The displayed error shall be documented in the installation manual.  

NOTE: The error listed above is defined for a display *system*, including the sensor(s). This gives the EFIS manufacturer 
flexibility to define the displayed error introduced by the EFIS.  Although the manufacturer has the flexibility to define the displayed error introduced by the EFIS, it should still be a small portion of the system error budget.   
In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 

## 4.4.2.8 Minimum Detection Range

The display shall be capable of depicting data as close as the greater of 1/2 NM or 5% of the selected range. 

## 4.4.2.9 Performance Index

Horizontal scans shall be displayed at a least every 10 seconds. 

 

## 4.4.2.10 Symbol Size46

Graphic display symbols, other than lines or line segments, shall be at least 0.10 inch x 0.10 inch and shall be unambiguous so as to avoid misinterpretation. 

## 4.4.2.11 Symbol Overlap47

Overlap of symbols, excluding symbol to line or line to line overlap, should not result in the loss of primary auxiliary data. Primary auxiliary data is data that the equipment designer has defined as having priority over data being displayed. 

## 4.4.2.12 Radar Referenced Data48

The position of any symbol or line when referenced to the weather radar indicators range and azimuth marks shall be accurate to ±8% of the selected radar range and +5 degrees in azimuth. 

## 4.4.2.13 Non-Radar Referenced Data49

The position of any symbol or line when referenced to its associated scale or reference point shall be accurate to ±2% of the full scale value. 

## 4.4.2.14 Character Size50

Alphanumeric characters shall be at least 0.070 inch x 0.070 inch. 

## 4.4.2.15 Character Overlap51

In no case should the character or its position cause erroneous interpretation of the data. 

## 4.4.2.16 Angular Accuracy

If the angular data for the display is Display-ready Data, the displayed error shall not exceed ±2%. If the angular data for the display is not Display-ready data, any numerical readout of data shall be accurate to ±5%. The displayed error shall be documented in the installation manual. NOTE: The non-Display-ready condition above is defined for a display *system*, including the sensor(s). This gives the EFIS 
manufacturer flexibility to define the displayed error introduced by the display. Although the manufacturer has the flexibility to define the displayed error introduced by the EFIS, it should still be a small portion of the system error budget. 

In all cases, the EFIS shall be tested to confirm that it meets the appropriate displayed error.  The EFIS shall be tested with inputs to the EFIS increased and decreased over the full range of operation. 


                                           

## 4.4.2.17 Alerts For Weather And Ground Mapping Radar 4.4.2.17.1 Windshear Alerts

Windshear alerts and failure indications provided by the radar shall be displayed. 

## 4.4.2.17.2 Weather Target Alert

An alert shall be incorporated to advise the aircrew of new weather target acquisition within ±10 degrees of the aircraft heading. This alert shall operate between maximum range and one third of maximum range. A weather target is a cloud or storm cell which has dangerously high turbulence within it.  

## 4.4.2.18 Controls For Weather And Ground Mapping Radar

If the EFIS provides the controls for weather and mapping radar, then the following requirements are applicable: 

## 4.4.2.18.1 Receiver Gain Control52

The EFIS shall provide controls for manual and/or automatic adjustment of the receiver gain for optimum system performance. 

## 4.4.2.18.2 Beam Tilting53

 The EFIS shall provide the ability to adjust the beam tilt ±10 degrees. 

## 4.4.2.18.3 Mode Selection54

The EFIS shall provide a means for selection of data and each available mode of operation for the optional equipment. NOTE: Sub-mode controls such as page or line advance shall be classified as being grouped within the mode control for selection of page mode. 

## 4.4.3 Airborne Passive Thunderstorm Detection

This function displays thunderstorm electrical discharge events relative to the aircraft position.  

## 4.4.3.1 Display Parameters For Airborne Passive Thunderstorm Detection 4.4.3.1.1 Azimuth 4.4.3.1.1.1 Area Scan And Display55

The display shall have the capability of indicating electrical discharge patterns over the forward 120-degree sector relative to aircraft heading. The azimuth may be limited to the forward 90-degree sector when heading reference inputs are used to correct displayed data as the aircraft turns. 

 
                                            
 

## 4.4.3.1.1.2 Azimuth Markers56

There shall be the capability to display azimuth markers at 30 degrees either side relative to the aircraft heading. 

## 4.4.3.1.2 Range 4.4.3.1.2.1 Indicator Range Scale57

The maximum displayed range shall be at least 100 nautical miles. 

## 4.4.3.1.2.2 Range Markers58

A linear range scale capable of displaying the maximum range for which the system is designed shall be provided with at least two range markers. All other range scales shall be provided with at least one range marker. The range shall increase from the minimum to full scale of the selected range. 

If multiple compass formats are available on the display, all formats shall provide sufficient range indications, and at least one of the display formats shall meet the range marker requirement. 

## 4.4.3.1.3 Display Data Obsolescence59

A means shall be provided to distinguish or remove old data. Old data shall not be retained longer than 4 minutes. 

## 4.4.3.2 Controls For Airborne Passive Thunderstorm Detection

If the EFIS provides the controls for airborne passive thunderstorm detection, then the following requirements are applicable: 

## 4.4.3.2.1 Mode Selection 4.4.3.2.1.1 Clear Mode60

The EFIS shall provide a means to manually clear the display of data. 

## 4.4.3.2.1.2 Self-Test Mode61

The EFIS shall include a self-test feature to verify operation of the system. 

## 4.4.4 Optional Display Equipment For Weather And Ground Mapping Radar Indicators

This function displays weather and ground mapping radar returns, beacon returns and beacon location and identification relative to the aircraft position. 


## 4.4.4.1 Display Parameters For Weather And Ground Mapping (Assisted Approach) Radar 4.4.4.1.1 Azimuth

A minimum of three azimuth markers shall be provided. One of the three azimuth markers shall mark the dead ahead direction. 

## 4.4.4.1.2 Beacon Operation

The EFIS shall be able to display and select primary radar returns, or beacon returns, or both and discriminate between beacon and primary targets.  

## 4.4.4.2 Alerts For Assisted Approach Radar

4.4.4.3 
Controls for Assisted Approach Radar 

## 4.4.4.3.1 Azimuth Markers

The EFIS shall enable the aircrew to display or suppress the range and azimuth markers. 

## 4.4.4.3.2 Beacon Operation

If provided by the radar system, the EFIS shall enable the aircrew to display the selected beacon for special identification.   

## 4.5 Terrain Surveillance And Avoidance Functions 4.5.1 Terrain Awareness And Ground Proximity

Terrain Awareness and Warning System (TAWS) and Ground Proximity Warning System (GPWS) intend to provide the flight crew with terrain awareness as well as aural and visual alerts on a display to help prevent an inadvertent controlled flight into terrain (CFIT) event. For each of the TAWS and GPWS functions defined, both aural and visual alerts are required and shall be provided in a manner that indicates it is a single event. The aural alert identifies the reason for the alert. TSO-C151c defines two classes of equipment: class A includes TAWS and GPWS that include a display system, while class B equipment shall only be capable of driving a terrain display function but the terrain display is not required. NOTE: This document includes limited information regarding the aural alerts because in some cases they have to occur simultaneously with the visual alert.  This document does not provide the aural requirements.  The aural alert information is provided for context when designing the visual alerts. 

4.5.1.1 
Terrain Awareness Display  
When implementing a terrain awareness display, provided with the appropriate signals from the terrain sensor, the EFIS shall be capable of displaying the following terrain-related information:      
The terrain shall be depicted relative to the airplane's position such that the pilot can estimate the relative bearing to the terrain of interest. 

The terrain shall be depicted relative to the airplane's position such that the pilot may estimate the distance to the terrain of interest. 

The terrain depicted shall be oriented to either the heading or the track of the airplane. In addition, a north-up orientation may be added as a selectable format. 

 
Variations in terrain elevation shall be depicted relative to the airplane's current or projected elevation (above and below) and be visually distinct. Terrain that is more than 2000 feet below the airplane's elevation can be excluded. Terrain that generates alerts shall be displayed in a manner to distinguish it from non-hazardous terrain. Terrain alerts shall be consistent with the caution and warning alert level. 

## 4.5.1.2 Terrain Alerting Display

When implementing a terrain display, provided with the appropriate signals from the terrain sensor, the visual display of terrain alerting information shall be immediately and continuously displayed by the EFIS until the situation is resolved or no longer valid. The TAWS sensor typically provides aural alerts to the aircraft intercom system and provides signals to the EFIS for display of associated visual alerts.  The EFIS should provide the TAWS visual alerts in a manner that clearly indicates to the flight crew that they represent a single event with the accompanying aural alert.  If the EFIS is providing the aural alert, it shall be coordinated with the visual alert.   
The TAWS display is required to provide visual alerts for each of the alert conditions listed in Table 13 as commanded by the sensor.   

## 4.5.1.3 Ground Proximity Visual Warnings

The EFIS should provide the GPWS visual alerts in a manner that clearly indicates to the flight crew that they represent a single event with the accompanying aural alert.  If the EFIS is providing the aural alert, it shall be coordinated with the visual alert.   

| Alert Condition                            |
|--------------------------------------------|
| Visual Alert                               |
| Amber text message that is obvious,        |
| concise, and shall be consistent with the  |
| aural message.                             |
| FLTA Functions                             |
| Reduced Required Terrain                   |
| Clearance and Imminent                     |
| Impact with Terrain                        |
| Class A & Class B                          |
| Aural Alerts                               |
| Minimum selectable voice alerts:           |
| "Caution, Terrain; Caution, Terrain"       |
| and                                        |
| "Terrain Ahead; Terrain Ahead"             |
| Premature Descent Alert                    |
| (PDA)                                      |
| Class A & Class B                          |
| Visual Alert                               |
| Amber text message that is obvious,        |
| concise, and shall be consistent with the  |
| aural message.                             |
| Aural Alert                                |
| "Too Low Terrain"                          |
| Visual Alert                               |
| Amber text message that is obvious,        |
| concise, and shall be consistent with the  |
| aural message.                             |
| Ground Proximity                           |
| Envelope 1, 2, or 3                        |
| Excessive Descent Rate                     |
| Mode 1                                     |
| Class A & Class B                          |
| Aural Alert                                |
| "Sink Rate"                                |
| Ground Proximity Excessive                 |
| Closure Rate (Flaps not in                 |
| Landing Configuration)                     |
| Mode 2A Class A                            |
| Visual Alert                               |
| Amber text message that is obvious,        |
| concise, and shall be consistent with the  |
| aural message.                             |
| Aural Alert                                |
| "Terrain, Terrain"                         |
| Ground Proximity Excessive                 |
| Closure Rate (Landing                      |
| Configuration) Mode 2B                     |
| Class A                                    |
| Visual Alert                               |
| Amber text message that is obvious,        |
| concise, and shall be consistent with the  |
| aural message.                             |
| Visual Alert                               |
| Red text message that is obvious, concise  |
| and shall be consistent with the aural     |
| message.                                   |
| Aural Alerts                               |
| Minimum selectable voice alerts: "Terrain, |
| Terrain; Pull-Up, Pull-Up"                 |
| and                                        |
| "Terrain                                   |
| Ahead, Pull-Up; Terrain Ahead, Pull-Up"    |
| Visual Alert                               |
| None Required                              |
| Aural Alert                                |
| None Required                              |
| Visual Alert                               |
| Red text message that is obvious, concise, |
| and shall be consistent with the Aural     |
| message.                                   |
| Aural Alert                                |
| "Pull-Up"                                  |
| Visual Alert                               |
| Red text message that is obvious, concise, |
| and shall be consistent with the aural     |
| message.                                   |
| Aural Alert                                |
| "Pull-Up"                                  |
| Visual Alert                               |
| Red text message that is obvious, concise, |
| and shall be consistent with the aural     |
| message for gear up.                       |
| Alert Condition                           |
|-------------------------------------------|
| Aural Alert                               |
| "Terrain, Terrain"                        |
| Aural Alert                               |
| "Pull-Up"—for gear up                     |
| None Required—for gear down               |
| Visual Alert                              |
| None Required                             |
| Ground Proximity Altitude                 |
| Loss after Takeoff                        |
| Mode 3                                    |
| Class A & Class B                         |
| Visual Alert                              |
| Amber text message that is obvious,       |
| concise, and shall be consistent with the |
| aural message.                            |
| Aural Alerts                              |
| "Don't Sink"                              |
| and                                       |
| "Too Low Terrain"                         |
| Aural Alert                               |
| None Required                             |
| Visual Alert                              |
| None Required                             |
| Visual Alert                              |
| Amber text message that is obvious,       |
| concise, and shall be consistent with the |
| aural message.                            |
| Ground Proximity Envelope                 |
| 1 (Gear and/or flaps other                |
| than landing configuration)               |
| Mode 4                                    |
| Class A                                   |
| Aural Alerts                              |
| "Too Low Terrain"                         |
| and                                       |
| "Too Low Gear"                            |
| Aural Alert                               |
| None Required                             |
| Visual Alert                              |
| None Required                             |
| Visual Alert                              |
| Amber text message that is obvious,       |
| concise, and shall be consistent with the |
| aural message.                            |
| Ground Proximity Envelope                 |
| 2 Insufficient Terrain                    |
| Clearance (Gear and/or                    |
| flaps other than landing                  |
| configuration) Mode 4                     |
| Class A                                   |
| Aural Alert                               |
| None Required                             |
| Aural Alerts                              |
| "Too Low Terrain"                         |
| and                                       |
| "Too Low                                  |
| Flaps"                                    |
| Visual Alert                              |
| None Required                             |
| Visual Alert                              |
| Amber text message that is obvious,       |
| concise, and shall be consistent with the |
| aural message.                            |
| Ground Proximity Envelope                 |
| 3 Insufficient Terrain                    |
| Clearance (Gear and/or                    |
| flaps other than landing                  |
| configuration) Mode 4                     |
| Class A                                   |
| Aural Alert                               |
| "Too Low Terrain"                         |
| Aural Alert                               |
| None Required                             |
| Visual Alert                              |
| None Required                             |
| Ground Proximity Excessive                |
| Glideslope or Glidepath                   |
| Deviation Mode 5                          |
| Class A                                   |
| Visual Alert                              |
| Amber text message that is obvious,       |
| concise, and shall be consistent with the |
| aural message.                            |
| Aural Alert                               |
| "Glideslope" or "Glidepath"               |
| Aural Alert                               |
| None Required                             |

## 4.5.2 Helicopter Taws

Helicopter Terrain Awareness and Warning Systems (HTAWS) are to provide terrain and obstacle aural and visual alerts and reduce the risk of helicopters flying into terrain and obstacles. 

NOTE: This document includes limited information regarding the aural alerts because in some cases they have to occur simultaneously with the visual alert.  This document does not provide the aural requirements.  The aural alert information is provided for context when designing the visual alerts. 

## 4.5.2.1 Terrain And Obstacle Data Depiction

When implementing an HTAWS display provided with the appropriate signals from the HTAWS sensor, the EFIS shall be capable of displaying the terrain and obstacle-related information in accordance with the requirements of RTCA/DO-309, section 2.2.1.1 (Data Depiction). 

## 4.5.2.2 Auto Display Function

The EFIS shall support a HTAWS auto display function in accordance with the requirements of RTCA/DO-309, section 2.2.1.2 (Auto Display). 


## 4.5.2.3 Visual Terrain And Obstacle Alerting

The EFIS shall display HTAWS terrain and obstacle alerting in accordance with the requirements of RTCA/DO-309, section 2.2.2.2 (Visual Alerts), paragraphs (d), (e) and (f). 

## 4.5.2.4 Alert Envelope - Reduced Protection Mode

If the HTAWS sensor provides a "Reduced Protection Mode", the EFIS shall comply with the requirements of RTCA/DO- 309, section 2.2.2.4 (Envelope), paragraph (g). 

## 4.5.2.5 Status Indications

The EFIS shall be capable of indicating the HTAWS status in accordance with the requirements of RTCA/DO-309, section 2.2.6 (Status), paragraphs (a) and (b). 

## 4.6 Traffic Surveillance And Avoidance Functions 4.6.1 Traffic Collision Avoidance System (Tcas I And Ii)

For the purposes of this document, an EFIS is expected to display the presence and relative location of intruder aircraft, or simply a "visual annunciation" of a Traffic Advisory (TA). This document does not provide the aural requirements or warnings. The EFIS displays information provided to it without further manipulation as to criticality or priority. 

## 4.6.1.1 Traffic Alert And Collision Avoidance System (Tcas) Airborne Equipment, Tcas I 4.6.1.1.1 Traffic Advisory Criteria

The EFIS shall display advisories against nearby aircraft. The advisory shall provide the crew with the intruder's range, bearing, and for altitude reporting intruders, relative altitude and vertical speed. The EFIS shall provide three levels of advisories: Other Traffic, Proximate Advisories (PA), and Traffic Advisories (TA). 

## 4.6.1.1.2 Display Overload

If the number of targets exceeds the display capability, excess targets shall be deleted in order, beginning with the lowest priority. 

## 4.6.1.2 Traffic Alert And Collision Avoidance System (Tcas) Airborne Equipment, Tcas Ii

In order to meet this MOPS for TCAS II, the EFIS shall also meet the display requirements herein for TAS and TCAS I. 

## 4.6.1.2.1 Resolution Advisory (Ra) Displays62

The Resolution Advisory (RA) display provides guidance on the vertical speed or pitch angle to be flown, and the range of vertical speeds or pitch angles to be avoided, to attain or maintain the desired vertical miss distance from an aircraft causing an RA. RA guidance information to be displayed is provided by a TCAS II sensor. The EFIS shall provide a RA display in one of three implementations: Arc VSI; Integrated Tape VSI on the PFD; or Pitch Cues on the PFD. The EFIS may also provide optional flight director guidance. 


                                           

## 4.6.1.2.1.1 Ra/Vsi (Arc Vsi) 63

This implementation shall indicate the vertical speeds to be flown and avoided using a series of red, green, and black arcs displayed around the periphery of the VSI. 

NOTE: The term "black arcs" refers to the area of the VSI scale, usually the background of the scale, which is not illuminated 
by the lighted red and green arcs. 
The scale of the VSI shall have sufficient range to display the required red and green arcs for all RAs that can be generated by the collision avoidance logic. This will require a range of ±6000 fpm. 

NOTE: If the VSI does not have a range of ±6000 fpm, a means shall be provided to display all corrective and preventive 
RAs, as well as the own aircraft's actual vertical speed. 
a. Red Arcs64 
The red arcs on the RA/VSI shall indicate the vertical speed range as provided by the TCAS II sensor. The red arcs 
shall have the capability of displaying a resolution no larger than 500 fpm for "maintain rate" RAs issued by the TCAS 
II sensor. If the display is capable of displaying a finer resolution, it shall be used. The red arcs shall be able to accurately 
depict all TCAS II "vertical speed limit" (VSL) RAs. The red arcs shall be readily discernible and distinguishable. The 
length of the red arc shall be adjusted as appropriate when the RA is strengthened or weakened, as provided by the TCAS II sensor. 
b. Green Arcs65 
A green "fly-to" arc shall be used to provide a target vertical speed whenever a change in the existing vertical speed is desired or when an existing vertical speed (not less than 1500 fpm) shall be maintained. Thus, a green arc shall be displayed for all RAs, except initial preventive RAs. 
 
NOTE: Maintain rate RAs are classified as corrective RAs 
 
The nominal size of the green arc shall be approximately that defined by the distance between the 1500 and 2000 fpm marks on the VSI scale. The size of the green arc shall remain constant no matter where the arc is placed on the display, with the exception of the multi-aircraft encounter described below. 
 
The green arc shall be readily discernible and distinguishable. In addition, the green arc shall either be wider than the red arc or offset from the red arc to assist in visually differentiating between the red and the green arcs. 
 
The green arc shall remain displayed for the entire duration of the RA. Its position shall move to the appropriate position when an RA is strengthened or weakened, as provided by the TCAS II sensor. 

## C. Black Arcs66

 
The portions of the VSI scale not covered by either a red or a green arc shall remain black. 

## D. Multi-Aircraft Encounter67

 
For the special situation where a multi-aircraft encounter results in an RA where neither a climb nor descent is permitted, a green arc shall be displayed from approximately -250 to +250 fpm. The remainder of the VSI scale shall be illuminated with red arcs. 

## 

e. VSI Characteristics68 
NOTE: It is recommended that inertial quickening of the vertical speed function be provided. 
f. 
Lighting Control69 
 
The lighting intensity of the red and green arcs shall either be automatic or connected to an adjustable lighting control for other similar alerting indicators.  

## 4.6.1.2.1.2 Ra/Vsi (Integrated Tape Vsi On The Pfd)70

This implementation shall indicate the vertical speeds to be flown and avoided using series of red, green, and black zones displayed within the vertical speed tape portion of the PFD. 

## Notes:

1. The requirements of this subparagraph only apply when the sole means of displaying RA guidance information is shown 
on an Integrated Tape VSI on the PFD. 
2. The term "black zones" refers to the area of the VSI scale, usually the background of the scale, which is not covered by 
either a red or a green zone. a. Red Zone71 
The red zone on the RA/VSI shall indicate the vertical speed range as provided by the TCAS II sensor. The red zone shall be readily discernible and distinguishable. The length (height) of the red zone shall be adjusted as appropriate when the RA is strengthened or weakened, as provided by the TCAS II sensor. 
b. Green Zone72 
A green "fly-to" zone shall be used to provide a target vertical speed whenever a change in the existing vertical speed is desired and when an existing vertical speed (not less than 1500 fpm) shall be maintained. Thus, a green zone shall be displayed for all RAs, except initial preventive RAs. 
 
NOTE: Maintain rate RAs are classified as corrective RAs 
 
The nominal size of the green zone shall be approximately that defined by the distance between the 1500 and 2000 fpm marks on the VSI scale. The size of the green zone shall remain constant no matter where the arc is placed on the display, with the exception of the multi-aircraft encounter described below. 
 
The green zone shall be readily discernible and distinguishable. In addition, the green zone shall either be wider than the red zone to assist in visually differentiating between the red and the green zones. 
 
The green zone shall remain displayed for the entire duration of the RA. Its position shall move to the appropriate position when an RA is strengthened or weakened, as provided by the TCAS II sensor. 
 
 
c. Black Zones73 
The portions of the VSI scale not covered by either a red or a green zone shall remain black. 
d. Multi-Aircraft Encounter74 
For the special situation where a multi-aircraft encounter results in an RA where neither a climb nor descent is permitted, a green zone shall be displayed from approximately -250 to +250 fpm. The remainder of the VSI scale shall be illuminated with red zones. 
 
NOTE: When the RA is corrective, it is also acceptable to allow a nominal length green arc beginning at 0 fpm in 
the corrective sense. 
e. VSI Characteristics75 
NOTE: It is recommended that inertial quickening of the vertical speed function be provided. 
f. 
VSI Scale76 
 
The scale of the VSI tape shall have sufficient range to display the required red and green zones for all RAs that can be generated by the TCAS II sensor. This will require a range of ±6000 fpm. 
g. Lighting Control77 
The lighting intensity of the red and green arcs shall either be automatic or connected to an adjustable lighting control for other similar alerting indicators.  

## 4.6.1.2.1.3 Pitch Cues On The Pfd78

This implementation shall indicate the pitch angles to be flown and avoided while responding to an RA using the symbology as follows. A representation of a typical pitch cue implementation on the PFD is shown in Figure 2. 

NOTE 1:  The requirements of this subparagraph are applicable whenever pitch cues are used to provide RA guidance 
information. This subparagraph does not require the implementation of pitch cues for RA guidance on all PFDs. 
NOTE 2:  In this document, the term "PFD" refers to the display used to show the aircraft's relationship to the horizon. The 
requirements for a PFD are also applicable to similar types of displays that may be referred to by different nomenclature. 
 
 
# 

## A. No-Fly Pitch Angles80

 
A red trapezoid overlaying the other information on the PFD shall indicate the range of pitch angles, as provided by the TCAS II sensor. When the trapezoid is displayed, the other information shown on the PFD shall remain readily discernible and readable. The trapezoid shall begin at the bottom of the PFD and extend upward to the desired pitch angle for up sense RAs; for down sense RAs, the trapezoid shall begin at the top of the PFD and extend downwards to the desired pitch angle. The closed end of the trapezoid shall correspond to the pitch angle that will provide the vertical speed desired by the TCAS II sensor. 
 
NOTE 1: The use of a trapezoid in this subparagraph is not intended to preclude the use of other geometric shapes, e.g., a rectangle, to depict the pitch angles to be avoided to attain or maintain the TCAS-desired vertical miss distance. If other geometric shapes are used to display TCAS RA guidance, the requirements shown here for trapezoids shall be met. 
 
The red trapezoid shall remain displayed for the entire duration of the RA. It shall move as appropriate when an RA is strengthened or weakened, as provided by the TCAS II sensor. The symbology used in the TCAS trapezoid shall be readily discernible and distinguishable from any other information displayed on the PFD. 
 
NOTE 2: The use of a green "fly-to" target is permitted to provide a target pitch angle whenever a change in the existing 
vertical speed is desired. If implemented, a green band or box shall be displayed at the top (up sense RA) or bottom 
(down sense RA) of the red trapezoid for all RAs except initial preventive RAs. If implemented, the green pitch target shall be readily discernible and distinguishable, and shall remain displayed for the entire duration of the RA. It shall 
move to the appropriate position when an RA is strengthened or weakened, as provided by the TCAS II sensor. 

## B. Mode Annunciation81

 
When an RA is to be displayed as provided by the TCAS II sensor, a written annunciation of "TCAS", "TFC", or "TRAFFIC", written in red, shall be displayed. The exact implementation of the annunciation shall be compatible with 
the implementation of other mode annunciations. 

## B. Multi-Aircraft Encounters82

 
For the special situation where a multi-aircraft encounter results in an RA where neither a climb nor descent is permitted, two red trapezoids shall be simultaneously displayed. One shall begin at the top of the PFD and extend downwards to the pitch angle that will result in level flight, while the other shall begin at the bottom of the PFD and extend upwards to the pitch angle that will result in level flight. There shall be sufficient room left between the two trapezoids to permit the own aircraft reference on the PFD to fit between the two trapezoids. 

## 4.6.1.2.1.4 Flight Director Guidance83

Flight director guidance may be provided to aid in following RAs. If a flight director RA mode is made available, the mode change shall be pilot selectable and a suitable mode annunciation shall be displayed. Flight director guidance may be used to assist in returning to the flight path and altitude being maintained prior to the display of a corrective RA. Provisions should be included to inhibit an RA recovery mode if, at the initiation of a corrective RA, the flight director was in the Glide Slope capture mode. 

## 4.6.2 Traffic Advisory System 4.6.2.1 Pilot Advisory Functions

A sample interface between Active TAS and the pilot is shown in Table 14. It is acceptable for the TAS system to use shape as the only discriminator for traffic threat levels and ownship. This will allow the use of a monochrome display representation of the TCAS symbology. It is also acceptable to provide a blinking TA symbol to allow further discrimination of the traffic alert symbol. 

Arrow indicates that the target is climbing ↑ or descending ↓ at a rate of at least 500 fpm. Relative altitude is displayed in the proximity of the aircraft symbol in hundreds of feet. A "+" preceding the relative altitude indicates the target is above you and a "-" indicates it is below you. 

Unfilled white diamond.  Non-threatening traffic without altitude reporting.  If altitude reporting, the altitude data will be displayed. 
 
+07 
Solid White diamond.  Proximity traffic 700 feet above.  Non-threatening, altitude reporting traffic within 1200 feet vertically and 6nm horizontally.  Aircraft without altitude reporting will be assumed to be co-altitude and will be displayed as a solid diamond when within 6nm even though they may not be within 1200 feet vertically. 
 
      ↓  
Solid yellow circle.  "TA", 300 feet below and descending with a rate of at least 500 fpm. 
-03  
Own-ship.  Airplane symbol in white just below the center of display (center of the 
surveillance area).   
 

(Compass Arc)  This arc is repeater of the Captain's compass. 

 
                                            

## 4.6.2.2 Active Tcas Pilot Interface

1. A traffic display shall be provided to indicate the presence and location of intruder aircraft. The traffic display may be 
combined with other aircraft displays. The traffic display shall provide the crew with the intruder's range, bearing, and, 
for altitude reporting intruders, relative altitude and vertical trend. 
2. Two levels of intruder aircraft shall be displayed; those causing a TA, and other traffic. Other traffic is defined as any 
traffic within the selected display range and not a TA.   
 
NOTE:  The use of TCAS threat levels as defined in DO-197A is an acceptable alternative to the requirements defined 
in this section. 
3. As a minimum, the traffic display shall depict the following information to aid in the visual acquisition of traffic and assist 
in determining the relative importance of each aircraft shown: In addition, the use of TCAS symbology with a monochrome display is also an acceptable means of depicting traffic information. 
 
NOTE:  TCAS I symbology as defined in FAA Memorandum titled Interim Guidance for Airworthiness Approval and 
Operational Use of Traffic Alert and Collision Avoidance System (TCAS I) dated June 16, 1995 is an acceptable alternative to the symbology requirements defined in this section. In addition, the use of TCAS symbology with a monochrome display is also an acceptable means of depicting traffic information. 
a. Symbolic differentiation among traffic of different relative importance. TA, other traffic (see h, i, j, k, and l below). b. Bearing c. Relative altitude (for altitude reporting aircraft only) 
1) 
Above or below own aircraft (+ and - signs).   
2) 
Numerical value 
d. Vertical trend of intruder aircraft (for altitude reporting aircraft only). e. Range. The selected range shall be depicted. f. 
The display shall contain a symbol to represent own aircraft. The symbol shall be different from those used to indicate TA and other traffic. The display shall be oriented such that own aircraft heading is always up (12 o'clock). 
g. A range ring shall be placed at a range of 2 NM from own aircraft symbol when a display range of 10 NM or less is 
selected. The ring shall have discrete markings at each of the twelve clock positions. The markings shall be of a 
size and shape that does not clutter the display. Note: Range rings for TCAS II displays covered by 4.6.1.2. 
h. Symbol fill shall be used to discriminate traffic by threat levels. i. 
The symbol for a TA is a filled rectangle, diamond or circle, and, when appropriate, a data field and vertical trend arrow as described in m. and n. below. 
j. 
The symbol for other traffic shall be an open or filled rectangle or diamond, and, when appropriate, a data field and 
vertical trend arrow as described in m. below. 

k. Overlapping traffic symbols should be displayed with the appropriate information overlapped. The highest priority 
traffic symbol should appear on top of other traffic symbols. Although this will be determined by the TCAS device performing the calculations, the priority order is: 1) 
Traffic Advisories (TA) traffic in order of increasing tau (i.e., the time to closest approach and the time to the same altitude), and   
2) 
Other Traffic (OT) in order of increasing range. 
 
NOTE:  Tau is a time constant, often shown by the lowercase Greek letter τ (tau), representing in this case 
the range to the intruder divided by intruder's rate of closure. 
l. 
A data field shall indicate the relative altitude, if available, of the intruder aircraft and shall consist of two digits indicating the altitude difference in hundreds of feet. For an intruder above own aircraft, the data field shall be preceded by a "+" character. For an intruder below own aircraft, the data field shall be preceded by a "-" character. For co-altitude intruders (intruders at the same altitude), the data field shall contain the digits "00", with no preceding "+" or "-" character. The data field shall be wholly contained within the boundaries of the traffic symbol. For TA 
traffic, (filled symbol), the data characters shall be depicted in a color that contrasts with the filled symbol color. For other traffic, the data field shall be the same color as the symbol. The height of the relative altitude data characters shall be no less than 0.15 inches. 
m. A vertical arrow should be placed to the immediate right of the traffic symbol if the vertical speed of the intruder is 
equal to or greater than 500 fpm, with the arrow pointing up for climbing traffic and down for descending traffic. The color of the arrow shall be the same as the symbol. 
n. Neither a data field nor a vertical arrow shall be associated with a symbol for traffic that is not reporting altitude. o. The display shall be capable of depicting a minimum of three intruder aircraft simultaneously. As a minimum, the 
display shall be capable of displaying aircraft that are within 5 NM of own aircraft. 
p. The display may provide for multiple crew-selectable display ranges. q. When the range of the intruder causing a traffic advisory to be displayed is greater than the maximum range of the 
display, this shall be indicated by placing no less than one quarter of the traffic advisory symbol at the edge of the display at the proper bearing. The data field and vertical trend arrow shall be shown in their normal positions relative to the traffic symbol. 
r. 
The size of the traffic symbol shall be no less than 0.2 inch high. 
4. "No bearing" advisories shall be presented for an intruder generating a TA when the intruder's relative bearing cannot 
be derived. The "no bearing" advisory shall be an alphanumeric display shown in tabular form. The display shall be in 
the form of "TA 3.6 -05 inch, which translates to a TA at 3.6 nautical miles, 500 feet below. "No bearing" TA's against non-altitude reporting intruders shall include the range only, e.g., "TA 2.2 inch, which translates to a non-altitude reporting, no bearing TA at 2.2 nautical miles. The advisory shall be centered on the display below the own aircraft 
symbol. The display shall include provisions to display at least two "no bearing" TA's. 
 
NOTE: For Pilot Advisory Functions with an Active *TCAS I* Pilot Interface only, a visual "Traffic" annunciation shall be 
provided for the duration of the TA. 

## 4.6.2.3 Traffic Advisory Criteria

The EFIS shall display two levels of TAS advisories - Other Traffic (OT), and Traffic Advisories (TA) - as provided by TAS equipment. Other traffic is defined as any traffic within the selected display range that is not a TA. TAs are issued based either on tau, i.e., the time to closest approach and the time to co-altitude, or on proximity to an intruder aircraft. The range tau is defined as the range divided by range rate and the vertical tau is defined as the relative altitude divided by the altitude rate. 

 

## 4.6.2.4 Display Overload

If the number of targets exceeds the display capability, excess targets shall be deleted in the following order:  

1. Other traffic (OT) beginning with the intruder at the greatest range. 2. Traffic Advisories (TAs) beginning with the intruder having the largest tau, i.e., the longest time to closest approach and 
time to the same altitude. Once a TA has been generated against an intruder, it cannot be removed as a TA until the TA criteria are no longer satisfied even though it may be dropped from the display. 

## 5. Minimum Performance Standards Under Environmental Conditions

The environmental tests and performance requirements described therein are intended to provide a laboratory means of determining the overall performance characteristics of the EFIS under conditions representative of those that may be encountered in actual operations.  To demonstrate compliance with this document, the performance requirements in Tables 15, 16, and 17 shall be met for the environmental conditions as outlined in 5.4 through 5.30 of AS8034B.  Compliance may be demonstrated by testing, analysis, or combination thereof.  After all environmental tests have been performed; the EFIS 
shall display information with contents as specified by the applicable requirements in Section 4 of this document. The EFIS shall perform the intended functions. As noted in AS8034B, some of the environmental tests contained need not be performed unless the manufacturer wishes to qualify the equipment for the particular environmental condition. These tests are identified in AS8034B by the phrase "when required." If the manufacturer wishes to qualify the equipment to these additional environmental conditions, then these "when required" tests will be performed. In addition, the requirements in 5.1 shall be met for the applicable declared functions under this aerospace standard. This is in addition to the requirements noted in AS8034B, and those of 3.4. The tables below, titled "Performance Required during Environmental Conditions", indicate additional specific performance under environmental conditions that shall be met for the functions selected for the EFIS. These have been taken from existing stand-alone TSOs, and are limited to those pertaining to display aspects. When the DO-160 section states "when required" for a test and that test has been determined to be required for the EFIS being qualified, then any performance required under an environmental condition shall be met. For simplicity, if there were no specific *additional* performance requirements for the display aspects of an existing TSO functionality, rather than having columns entirely of "N/A" or "None", those functions were not included in the tables.  Also, the tables of "Performance Required during Environmental Conditions" do not cover performance required *after* exposure to certain environmental conditions.  

## Post-Test Operational Requirements Post 4.6 Altitude Test Requirements: "Fuel, Oil, And Hydraulic Pressure" Requires The Unit To Pass 4.3.4.2 Accuracy Within 1 Hour Of Test. Post 6.0 Humidity Test Requirements: "Electric Tachometer: Magnetic Drag" Requires The Unit To Pass 4.3.5.2 Accuracy (Post Test).

Post 8.0 Vibration Test requirements: 
"Electric Tachometer: Magnetic Drag" requires the unit to pass 4.3.5.2 Accuracy (post test) 

## 5.1 Additional Functional Requirements Under Environmental Conditions 5.1.1 Airspeed Performance 5.1.1.1 Operation Under Power Input Variations:

The airspeed indication shall operate, although degradation of performance is permissible. 

## 5.1.1.2 Airspeed Performance Under Environments

When subjected to the following environmental tests the airspeed shall meet the following performance requirements as specified in the table below. Temperature Low/High (DO-160 Section 4.0) and Temperature Variation (DO-160 Section 5.0) environments shall allow an additional tolerance of 3 knots (3.5 mph to 6 km/h) for all points in Table 1. NOTE 1: See Appendix B for an example of the analysis for an EFIS compliant with inputs from an Air Data Computer 
(ADC) that is certified to TSO-C106/AS8002A. The example shows the system level analysis needed to satisfy the scale error requirement for the EFIS TSO.  In this case, the installation manual would call out the EFIS is compliant with ADCs that meet accuracy of TSO-C106/AS8002A or better. 

## 5.1.2 Vertical Speed Performance 5.1.2.1 Vertical Speed Performance Under Power Input Variations:

The vertical speed indication shall operate electrically and mechanically and degradation of performance is permissible. 

## 5.1.2.2 Vertical Speed Performance Under Environments

When subjected to the following environmental tests the vertical speed shall meet the following performance requirements as specified in Table 16: The following Windshear performance requirements shall be met for the environmental conditions required by AS8034B. Windshear Caution Alert as defined in 4.4.1.1 Windshear Warning Alert as defined in 4.4.1.2 Windshear Escape Guidance as defined in 4.4.1.3 

## 5.1.3 Manifold Pressure Performance

The EFIS shall not contribute more 0.4 inches (1.0 cm) Hg error to the displayed pressure during the Low Temperature and High Temperature tests. The EFIS shall not contribute more 0.4 inches (1.0 cm) Hg error to the displayed pressure during the Altitude test.   

## 5.1.4 Tachometer Performance

The change in indication from the reading obtained at room temperature shall not exceed one percent of full scale under low temperature and high temperature environmental conditions.  After exposure to the humidity test, the change in reading between this test and the original displayed error at room temperature test shall not exceed 10 RPM. 

## 5.1.5 Automatic Flight Guidance And Control System

The display is not required to operate normally during *abnormal* voltage inputs, but shall not provide misleading information during or after the tests. 

 

Performance Requirements for These Functions 
Automatic 
Environmental 
Airborne 
Direction 
Test 
Low-Range 
DO-160G/ED-14G 
Radio 
Section 
Altimeter 
Airspeed 
Altimeter 
Equipment 
4.1.1.6 Accuracy   
4.0 Operating Low Temperature Test 
4.2.6.2 Bearing Accuracy 
4.1.9.1 Accuracy 4.1.9.2.1 Failure Indication 
4.1.3.9 Accuracy and AS8009B §5.2 4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate 4.1.3.12 Monitoring functions  
4.1.1.6 Accuracy   
4.0 Operating High Temperature Test 
4.2.6.2 Bearing Accuracy 
4.1.9.1 Accuracy 4.1.9.2.1 Failure Indication 
4.1.3.9 Accuracy and AS8009B §5.2 4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate 4.1.3.12 Monitoring functions  
4.6 Altitude  
Drift and after effect AS8009B §5.3 
4.2.6.2 Bearing Accuracy 
4.1.1.6 Accuracy and 4.1.1.7 Smoothing 
4.1.9.1 Accuracy 4.1.9.2.1 Failure Indication 
4.6 Decompression (When Required) 


4.2.6.2 Bearing Accuracy 


4.2.6.2 Bearing Accuracy 
4.6 Overpressure Tests (When Required)  
 
4.1.1.6 Accuracy   
5.0 Temperature Variation Test  
 
4.2.6.2 Bearing Accuracy 
6.0 
Humidity Test  
4.2.6.2 
Bearing Accuracy 
4.1.9.1 
Accuracy 4.1.9.2.1 Failure Indication 
 
4.1.3.9 Accuracy 
and AS8009B 5.2 4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate 4.1.3.12 Monitoring functions  
7.0 Operational Shocks  
4.2.6.2 Bearing Accuracy 
4.1.9.1 Accuracy 4.1.9.2.1 Failure Indication 
 
4.1.3.9 Accuracy Scale error 4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate 4.1.3.12 Monitoring functions 
8.0 Vibration Tests  
4.1.1.6 Accuracy   
4.2.6.2 Bearing Accuracy 
4.1.9.1 Accuracy 4.1.9.2.1 Failure Indication 
4.1.3.9 Accuracy Scale error 4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate  
Automatic 
Flight 
Guidance 
and Control 
Finding 
System 
Direction 
Direction 
(ADF) 
(AFGCS) 
Instrument, 
Instrument, 
Equipment 
Magnetic 
Non-Magnetic 
Tachometer 
4.1.5.4 Accuracy 
4.1.5.4 Accuracy 
5.1.4 Tachometer Performance under Environments 
4.1.10 Steering commands under Automatic Flight Guidance and Control System 
4.1.5.4 Accuracy 
4.1.5.4 Accuracy 
4.1.10 Steering commands 
5.1.4 Tachometer Performanc e under Environment s 
4.1.5.4 Accuracy 
4.1.5.4 Accuracy 
4.1.10 Steering commands 


4.1.10 Steering commands 


4.1.10 
Steering commands 


4.1.10 Steering commands 
 
4.1.5.4 Accuracy 
4.1.5.4 Accuracy 
4.1.10 Steering commands 
Performance Requirements for These Functions 
Automatic 
Environmental 
Airborne 
Direction 
Test 
Low-Range 
DO-160G/ED-14G 
Radio 
Section 
Altimeter 
Airspeed 
Altimeter 
Equipment 
4.1.3.12 Monitoring functions 


4.1.10 Steering commands 
9.0 Explosive Atmosphere Test (When Required)  


4.2.6.2 Bearing Accuracy 
10.0 Waterproofness Drip Proof Test (When Required)  


4.2.6.2 Bearing Accuracy 
11.0 Fluids Susceptibility Spray Test (When Required)  


4.2.6.2 Bearing Accuracy 
11.0 Fluids Susceptibility Immersion Test (When Required) 


4.2.6.2 Bearing Accuracy 
12.0 Sand and Dust Test (When Required)  


4.2.6.2 Bearing Accuracy 
13.0 Fungus Resistance Tests (When Required) 14.0 Salt Fog Test (When Required)  


4.2.6.2 Bearing Accuracy 
4.1.1.6 Accuracy   
4.2.6.2 Bearing Accuracy 
16.0 Power Input Test Normal Operating Conditions  
4.1.9.1 Accuracy 4.1.9.2.1 Failure Indication 
4.1.3.9 Accuracy Scale error 4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate 4.1.3.12 Monitoring 
functions 
4.2.6.2 Bearing Accuracy 
16.0 Power Input Test Abnormal Operating Conditions  
 
5.1.1.1 Operation Under Power Input Variations 
4.2.6.2 Bearing Accuracy 
17.0 Voltage Spike Test  Category A Test (When Required)  
4.1.9.1 Accuracy 4.1.9.2.1 Failure Indication 
 
4.1.3.9 Accuracy Scale error 4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate 4.1.3.12 Monitoring functions 


4.2.6.2 Bearing Accuracy 
17.0 Voltage Spike Test  Category B Test (When Required)  
4.1.9.1 Accuracy 
4.1.1.6 Accuracy   
4.1.3.9 Accuracy Scale error 
4.2.6.2 Bearing Accuracy 
18.0 Audio Frequency Conducted Susceptibility - 
Automatic 
Flight 
Guidance 
and Control 
Finding 
System 
Direction 
Direction 
(ADF) 
(AFGCS) 
Instrument, 
Instrument, 
Equipment 
Magnetic 
Non-Magnetic 
Tachometer 


4.1.10 Steering commands 


4.1.10 Steering commands 


4.1.10 Steering commands 


4.1.10 Steering commands 


4.1.10 Steering commands 


4.1.10 Steering commands 
 
4.1.5.4 Accuracy 
4.1.5.4 Accuracy 
4.1.10 Steering commands 


4.1.10 Steering commands  


4.1.10 Steering commands 
 
4.1.5.4 Accuracy 
4.1.5.4 Accuracy 
4.1.10 Steering commands 
 
4.1.5.4 Accuracy 
4.1.5.4 Accuracy 
4.1.10 Steering commands 
Performance Requirements for These Functions 
Automatic 
Environmental 
Airborne 
Direction 
Test 
Low-Range 
DO-160G/ED-14G 
Radio 
Section 
Altimeter 
Airspeed 
Altimeter 
Equipment 
Power Inputs (Closed Circuit Test)  
4.1.9.2.1 Failure Indication 
4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate 4.1.3.12 Monitoring functions 
4.1.1.6 Accuracy   
19.0 Induced Signal Susceptibility Test  
4.2.6.2 Bearing Accuracy 
4.1.9.1 Accuracy 4.1.9.2.1 Failure Indication 
4.1.3.9 Accuracy Scale error 4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate 4.1.3.12 Monitoring functions 
4.1.1.6 Accuracy   
4.2.6.2 Bearing Accuracy 
20.0 Radio Frequency Susceptibility Test (Radiated and Conducted)  
4.1.9.1 Accuracy 4.1.9.2.1 Failure Indication 
4.1.3.9 Accuracy Scale error 4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate 4.1.3.12 Monitoring functions 
 
 
4.1.5.4 Accuracy 
21.0 Emission of Radio Frequency Energy Test  
 
 
4.1.3.9 Accuracy Scale error 4.1.3.10 Barometric Setting Scale 4.1.3.11 Minimum operating rate 4.1.3.12 Monitoring functions 


4.1.10 Steering commands 
22.0 Lightning Induced Transient 
Susceptibility  


4.1.10 Steering commands 
23.0 Lightning Direct Effects (When Required) 25.0 Electrostatic Discharge (ESD)  


4.1.10 Steering commands 
Automatic 
Flight 
Guidance 
and Control 
Finding 
System 
Direction 
Direction 
(ADF) 
(AFGCS) 
Instrument, 
Instrument, 
Equipment 
Magnetic 
Non-Magnetic 
Tachometer 
 
4.1.5.4 Accuracy 
4.1.5.4 Accuracy 
4.1.10 Steering commands 
 
4.1.5.4 Accuracy 
4.1.5.4 Accuracy 
4.1.10 Steering commands 
 
4.1.5.4 Accuracy 


Performance Requirements for These Functions 
Flight 
Environmental 
Management 
Fuel, Oil, 
Test 
System (FMS) 
and 
DO-160G/ED-14G 
using multi-
Fuel and Oil 
Hydraulic 
Section 
sensor inputs 
Quantity 
Pressure 
Glideslope 
ILS Localizer 
4.0 Operating Low Temperature Test 


5.1.3 Manifold Pressure Performance under Environments 
4.2.8.2.5 Crosstrack deviation under Non- Numeric Display of Cross-Track Deviation, and failure/status indication under both 4.2.8.2.9 
"Indicating and 
Alerting and 4.2.8.1.8 Failure Indication 
 
4.3.4.2 Accuracy 
4.0 Operating High Temperature Test 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
4.2.4.1.2.1 Glideslope Deviation Sensitivity 4.2.4.1.2.3 Glideslope Warnings 
4.0 In-Flight Loss of Cooling Test  
 
 
4.2.4.1.2.3 Glideslope Warnings. 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
4.6 Altitude  
 
 
4.2.4.1.2.3 Glideslope Warnings. 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
4.6 Decompression (When Required) 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
 
4.2.4.1.2.1 Glideslope Deviation Sensitivity. 4.2.4.1.2.3 Glideslope Warnings. 
4.3.6.3 
Accuracy 
4.6  
Overpressure Tests (When Required)  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
4.2.4.1.2.1 
Glideslope Deviation Sensitivity. 4.2.4.1.2.3 Glideslope Warnings. 
5.0 Temperature Variation Test  
 
 
4.2.4.1.2.3 Glideslope Warnings 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 


6.0 Humidity Test  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
4.3.6.3 Accuracy 
7.0 Operational Shocks  
 
4.2.4.1.2.3 Glideslope Warnings 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 


4.2.8.2.5 Crosstrack deviation 
7.0 Crash Safety Tests 
Manifold 
Max Allowable 
ILS 
Mach 
Pressure 
Airspeed 
Meters 
Instruments 
Indicators 
 
4.1.7.2 Accuracy 
4.1.6.2 Accuracy 
4.2.3.4 Accuracy 4.2.3.5 Localizer Alerts 
5.1.3 Manifold Pressure Performance under Environments 
4.1.7.2 Accuracy 
 
4.1.6.2 Accuracy 
4.2.3.5 Localizer Alerts 
 
4.1.7.2 Accuracy 
4.2.3.5 Localizer Alerts 
5.1.3 Manifold Pressure Performance under Environments 


4.2.3.4 Accuracy 4.2.3.5 Localizer Alerts 
 
 
4.1.7.2 
Accuracy 
4.2.3.4 
Accuracy 4.2.3.5 Localizer Alerts 
 
 
4.1.7.2 Accuracy 
4.2.3.5 Localizer Alerts 
 
 
4.1.7.2 Accuracy 
4.2.3.5 Localizer Alerts 
Performance Requirements for These Functions 
Flight 
Environmental 
Management 
Fuel, Oil, 
Test 
System (FMS) 
and 
DO-160G/ED-14G 
using multi-
Fuel and Oil 
Hydraulic 
Section 
sensor inputs 
Quantity 
Pressure 
Glideslope 
ILS Localizer 
4.2.8.2.9/ 4.2.8.1.8 
Failure/status indication 
8.0 Vibration Tests  
 
 
4.2.4.1.2.3 Glideslope Warnings 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
 
4.2.4.1.2.3 Glideslope Warnings 
9.0 Explosive Atmosphere Test (When Required)  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
 
4.2.4.1.2.3 Glideslope Warnings 
10.0 Waterproofness Drip Proof Test (When Required)  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
 
4.2.4.1.2.3 Glideslope Warnings 
11.0 Fluids Susceptibility Spray Test (When Required)  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
 
4.2.4.1.2.3 Glideslope Warnings 
11.0 Fluids Susceptibility Immersion Test (When Required) 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
 
4.2.4.1.2.3 Glideslope Warnings 
12.0 Sand and Dust Test (When Required)  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
14.0 Salt Fog Test (When Required)  
 
 
4.2.4.1.2.3 Glideslope Warnings 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 
4.2.8.1.8 Failure/status indication 
15.0 Magnetic Effect Test  
 
 
4.2.4.1.2.3 Glideslope Warnings 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
 
4.2.4.1.2.3 Glideslope Warnings 
16.0 Power Input Test Normal Operating Conditions  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
 
4.2.4.1.2.3 Glideslope Warnings 
16.0 Power Input Test Abnormal Operating Conditions  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
 
4.2.4.1.2.3 Glideslope Warnings 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 
17.0 Voltage Spike Test  Category A Test (When Required)  
Manifold 
Max Allowable 
ILS 
Mach 
Pressure 
Airspeed 
Meters 
Instruments 
Indicators 


4.2.3.5 Localizer Alerts  


4.2.3.5 Localizer Alerts 


4.2.3.5 Localizer Alerts 


4.2.3.5 Localizer Alerts 


4.2.3.5 Localizer Alerts 


4.2.3.5 Localizer Alerts 
 
 
4.1.7.2 Accuracy 
4.2.3.5 Localizer Alerts 
 
 
4.1.7.2 Accuracy 
4.2.3.5 Localizer Alerts 
 
 
4.1.7.2 Accuracy 
4.2.3.5 Localizer Alerts 
 
 
4.1.7.2 Accuracy 
4.2.3.5 Localizer Alerts 
 
 
4.1.7.2 Accuracy 
4.2.3.5 Localizer Alerts 
Performance Requirements for These Functions 
Flight 
Environmental 
Management 
Fuel, Oil, 
Test 
System (FMS) 
and 
DO-160G/ED-14G 
using multi-
Fuel and Oil 
Hydraulic 
Section 
sensor inputs 
Quantity 
Pressure 
Glideslope 
ILS Localizer 
Failure/status indication 
 
 
4.2.4.1.2.3 Glideslope Warnings 
17.0 Voltage Spike Test  Category B Test (When Required)  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
 
 
4.2.4.1.2.3 Glideslope Warnings 
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 
18.0 Audio Frequency Conducted Susceptibility - Power Inputs (Closed Circuit Test)  


19.0 Induced Signal Susceptibility Test  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 


20.0 Radio Frequency Susceptibility Test (Radiated and Conducted)  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 


21.0 Emission of Radio Frequency Energy Test  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 


22.0 Lightning Induced Transient Susceptibility  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 Failure/status indication 


23.0 Lightning Direct Effects (When Required)  
4.2.8.2.5 Crosstrack deviation 4.2.8.2.9/ 4.2.8.1.8 
Failure/status indication 
 
Manifold 
Max Allowable 
ILS 
Mach 
Pressure 
Airspeed 
Meters 
Instruments 
Indicators 
 
 
4.1.7.2 Accuracy 
4.2.3.5 Localizer Alerts 
 
 
4.1.7.2 Accuracy 
4.2.3.5 Localizer Alerts 
Performance Requirements for Functions 
Stand-Alone Nav 
Environmental Test 
System using 
DO-160G/ED-14G 
GPS Assisted by 
Temperature 
Section 
SBAS 
Instruments 
Turn and Slip 
 
4.3.1.1 Accuracy  
4.0 Operating Low Temperature Test 
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
 
4.3.1.1 Accuracy 
4.0 Operating High Temperature Test 
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
4.6 Altitude  
 
4.3.1.1 Accuracy 
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
4.6 Decompression (When Required) 


4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  


4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
4.6 Overpressure Tests (When Required) 5.0 Temperature Variation Test  
 
 
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
6.0 Humidity Test  
 
 
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
7.0 Operational Shocks  
 
 
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
8.0 Vibration Tests  
 
4.3.1.1 Accuracy 
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 


4.4.1 Windshear Warning and Escape Guidance 
9.0 Explosive Atmosphere Test (When Required)  
Vertical 
Velocity 
Windshear Warning 
Instruments 
(Rate of 
VOR Receiving 
and Escape Guidance Systems for Transport 
Climb) 
Equipment 
Airplanes 
 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.3.1 VOR Course Deviation Sensitivity 4.2.1.3.3 Ambiguity Indication 4.2.1.4 Warnings 
 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.3.1 VOR Course Deviation Sensitivity 4.2.1.3.3 Ambiguity Indication 4.2.1.4 Warnings 
 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.3.1 VOR Course Deviation Sensitivity 4.2.1.3.3 Ambiguity Indication 4.2.1.4 Warnings 4.4.1 Windshear Warning and Escape Guidance 
4.1.2.3 Accuracy Scale error  
4.4.1 Windshear Warning and Escape Guidance 
4.2.1.1 Bearing Accuracy 4.2.1.3.1 VOR Course Deviation Sensitivity 4.2.1.3.3 Ambiguity Indication 4.2.1.4 Warnings 
 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.3.1 VOR Course Deviation Sensitivity 4.2.1.3.3 Ambiguity Indication 4.2.1.4 Warnings 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
4.4.1 Windshear Warning and Escape Guidance 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
Performance Requirements for Functions 
Stand-Alone Nav 
Environmental Test 
System using 
DO-160G/ED-14G 
GPS Assisted by 
Temperature 
Section 
SBAS 
Instruments 
Turn and Slip 


4.2.1.1 Bearing Accuracy  
4.2.1.4 Warnings  
10.0 Waterproofness 
Drip Proof Test (When Required)  


4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
11.0 Fluids Susceptibility Spray Test (When Required)  


4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
11.0 Fluids Susceptibility Immersion Test (When Required) 


4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
12.0 Sand and Dust Test (When Required)  


4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
13.0 Fungus Resistance Tests (When Required) 14.0 Salt Fog Test (When Required)  


4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
 
4.3.1.1 Accuracy 
16.0 Power Input Test Normal Operating Conditions  
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
 
4.3.1.1 Accuracy 
 
 
4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
16.0 Power Input Test Abnormal Operating Conditions  
 
4.3.1.1 Accuracy 
17.0 Voltage Spike Test Category A Test (When Required)  
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
 
4.3.1.1 Accuracy 
17.0 Voltage Spike Test Category B Test (When Required)  
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
 
4.3.1.1 Accuracy 
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
18.0 Audio Frequency Conducted Susceptibility - Power Inputs (Closed Circuit Test)  
Vertical 
Velocity 
Windshear Warning 
Instruments 
(Rate of 
VOR Receiving 
and Escape Guidance Systems for Transport 
Climb) 
Equipment 
Airplanes 
4.4.1 Windshear Warning and Escape 
Guidance 4.4.1 Windshear Warning and Escape Guidance 4.4.1 Windshear Warning and Escape Guidance 4.4.1 Windshear Warning and Escape Guidance 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
 
 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.4Warnings  
 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
Performance Requirements for Functions 
Vertical 
Stand-Alone Nav 
Velocity 
Windshear Warning 
Environmental Test 
System using 
Instruments 
DO-160G/ED-14G 
GPS Assisted by 
Temperature 
(Rate of 
VOR Receiving 
and Escape Guidance Systems for Transport 
Section 
SBAS 
Instruments 
Turn and Slip 
Climb) 
Equipment 
Airplanes 
 
4.3.1.1 Accuracy 
19.0 Induced Signal 
Susceptibility Test  
4.1.2.3 Accuracy 
Scale error  
4.2.1.1 Bearing Accuracy  
4.2.1.4 Warnings  
4.4.1 Windshear Warning and Escape 
Guidance 
4.1.8.1 Turn Rate 4.1.8.2 Standard 
Turn Bank Angle 4.1.8.3 Slip/Skid 
 
4.3.1.1 Accuracy 
4.1.2.3 Accuracy Scale error  
4.2.1.1 Bearing Accuracy 4.2.1.4 Warnings  
4.4.1 Windshear Warning and Escape Guidance 
4.1.8.1 Turn Rate 4.1.8.2 Standard Turn Bank Angle 4.1.8.3 Slip/Skid 
20.0 Radio Frequency Susceptibility Test (Radiated and Conducted)  


4.1.2.3 Accuracy Scale error  
21.0 Emission of Radio Frequency Energy Test  


22.0 Lightning Induced Transient Susceptibility  


4.4.1 Windshear Warning and Escape Guidance 
23.0 Lightning Direct Effects (When Required) 24.0 Icing (When Required)  


4.4.1 Windshear Warning and Escape Guidance 
25.0 Electrostatic Discharge (ESD)  


4.4.1 Windshear Warning and Escape Guidance 
X-ray Radiation (only for CRTs) 


4.4.1 Windshear Warning and Escape Guidance 
UV Radiation (only for CRTs) 


4.4.1 Windshear Warning and Escape Guidance 

 

## 6. Glossary Of Terms 6.1 Words And Phrases

ACRONYM: An abbreviation, pronounced as a word, which is formed from the initial components of phrases or words or both. ADS-B:  Automatic dependent surveillance - broadcast  
ATCRBS/MODE S:  Air Traffic Control Radar Beacon System/Mode Select BASIC T:  The basic T-configuration is based on a grouping of analog flight instruments in the shape of a capital letter T, and is defined as an arrangement where the top center position, directly in front of the pilot or copilot, is for the "artificial horizon" showing attitude data, with indictors for airspeed and altitude data centered, respectively, directly to the left and right of the attitude data, and with a heading indicator for magnetic direction data located directly below the attitude data. Even when applied to an EFIS display, the basic T information should be displayed continuously under normal (that is, no display system failure) conditions, and the attitude indication should be placed so that the display is unobstructed under all flight conditions. Primary airspeed, altitude, and direction of flight indications should be located adjacent to the primary attitude indication. Information elements placed within, overlaid, or between these indications, such as lateral and vertical deviation, are acceptable when they are relevant to respective airspeed, altitude, or directional indications used for accomplishing the basic flying task, and are shown to not disrupt the normal crosscheck or decrease manual flying performance. 

 
DIGITAL NUMERIC READOUT:  A Digital Numeric Readout, also known as a digital readout, presents data visually to the flight crew expressed as series of numbers (digits). The data presented are values of a physical quantity such as altitude, fuel, voltage, amperage, etc., and may also present information from data or signals generated by things such as a linear encoder or rotary encoder. DISPLAY-READY DATA:  Data received by the EFIS that represents a single parameter, in engineering units (e.g., degrees, feet, knots), and which the EFIS displays as a single parameter. The EFIS performs no calibration or compensation or scaling on this data. Analog data is not considered to be Display-Ready-Data. DISPLAYED ERROR:  The maximum steady-state error contributed by the EFIS, which does not include dynamic effects and the effects of latency.  
ELECTRONIC FLIGHT INSTRUMENT SYSTEM (EFIS):  *As it applies to this document*, an Electronic Flight Instrument System includes the electronic display of functions, the associated processing capability as needed, the controls, if any 
(e.g., luminance/brightness control), but it *excludes sensors*. An EFIS may be integrated into one article, one line replaceable unit (LRU), several components or multiple LRUs, but it does not include the sensors.  
EFIS DISPLAY:  The *electronic display portion* (e.g., an active matrix liquid crystal display, cathode ray tube, etc.) of an Electronic Flight Instrument System. FLIGHT CREW:  Flight Crew refers to a pilot, flight engineer, or flight navigator assigned to duty in an aircraft during flight time (reference 14 CFR Part 1). FUNCTION:  A function is an intended behavior for an EFIS based on a defined set of requirements, regardless of implementation. A list of these functions can be found in Appendix A. INITIALISM:  An abbreviation formed from the first letters of phrases or words or both, pronounced as series of letters. SHALL:  The word "shall" is used to express an essential requirement where compliance is mandatory. SHOULD:  The word "should" is used to express a recommendation. Deviation from the specified recommendation shall require justification SYSTEM:  A system is a combination of inter-related hardware and/or software arranged to perform specific function(s). 

## 6.2 Abbreviations

' (a single right quote mark, or apostrophe):  Feet, Foot (when not part of a word indicating possession or a contraction) AC: Advisory Circular ACK: Acknowledge ACT, ACTV: Active, Activate ADC: Air Data Computer ADF: Automatic Direction Finding ADI: Attitude Director Indicator ADS-B: Automatic Dependent Surveillance - Broadcast AFGS: Automatic Flight Guidance System AHRS: Attitude Heading Reference System AHRU: Attitude Heading Reference Unit 
 
 
AIRB: Airborne ALRT: Alert/Alerting ALT: Altitude AMC: Acceptable Means of Compliance APPR, APR: Approach, Approach Control APT: Airport, Aerodrome ARM: Arm, Armed ARP: Aerospace Recommended Practice AS: Aerospace Standard  
ASA: Aircraft Surveillance Applications ATC: Air Traffic Control ATCRBS: Air Traffic Control Radar Beacon System ATD: Along-Track Distance ATE: Along-Track Error ATK: Along-Track ATN: Air Traffic Network BARO: Barometric setting BRG: Bearing C: Center runway, Centigrade CDI: Course Deviation Indicator CDTI: Cockpit Display of Traffic Information CDU: Control Display Unit CF: Course-to-fix CFR: Code of Federal Regulations CLR: Clear   
CNCL: Cancel CRS: Course CRSR: Cursor DA: Decision Altitude, Drift Angle 
 
DB: Database DEL: Delete DEP: Departure, Departure Control DEST: Destination DF: Direct-to-Fix DIR: Direct, Direction direct symbol (D with arrow): Direct-To DIS, DIST: Distance DK, DTK: Desired Track   
DME: Distance Measuring Equipment DOP: Dilution of Precision DR: Dead Reckoning DU: Display Unit E: East EFIS: Electronic Flight Instrument System EMD: Electronic Map Display ENR: En Route ENT: Enter EPU: Estimated Position Uncertainty ESA: Emergency Safe Altitude, En Route Safe Altitude  
ETA: Estimated Time of Arrival ETD: Estimated Time of Departure ETE: Estimated Time En Route EUROCAE: European Organisation for Civil Aviation Equipment EV: Enhanced Visual (Acquisition) 
F: Fahrenheit f, FA, FAWP: Final Approach Waypoint, for waypoint identifiers FA: Fix-to-Altitude FAA: Federal Aviation Administration 
 
FIS: Flight Information Service FL: Flight Level FLTA: Forward Looking Terrain Avoidance FMEA: Failure Modes and Effects Analysis FMS: Flight Management System FPA: Flight Path Angle FPL: Flight Plan FPM: Feet per Minute FPV: Flight Path Vector FR: From FSD: Full-Scale Deflection FT: Foot, Feet FTP: Fictitious Threshold Point GMT: Greenwich Mean Time GNSS: Global Navigation Satellite System GPS: Global Positioning System GPWS: Ground Proximity Warning System GS: Ground Speed h, MH, MAHWP: Missed-Approach Holding Waypoint HAL: Horizontal Alert Limit   
HAT: Height Above Threshold HDG: Heading HF: High Frequency HLD:  Hold, Holding, Holding Pattern   
HPL: Horizontal Protection Level   
HSI: Horizontal Situation Indicator HTAWS: Helicopter Terrain Awareness and Warning System HUL: Horizontal Uncertainty Level 
 
i, IA, IAWP: Initial Approach Waypoint, for waypoint identifiers IAS: Indicated Airspeed ID: Identifier IF: Initial Fix IFR: Instrument Flight Rules ILS: Instrument Landing System IM: Inner Marker IMA: Integrated Modular Avionics INT: Intersection   
ITP: In-Trail Procedures IWP: Intermediate Waypoint KT: Nautical Miles per Hour, Knots L: Left runway L, LFT:  Left LAT: Latitude LCD: Liquid Crystal Display LDA: Localizer-type Directional Aid LNAV: Lateral Navigation LNAV/VNAV, L/V: Lateral Navigation/Vertical Navigation LOC: Localizer   
LOI: Loss of Integrity LON: Longitude LOS: Line of Sight LP: Localizer Performance without Vertical Guidance  
LPV: Localizer Performance with Vertical Guidance LTP: Landing Threshold Point M: Meters m, MA, MAWP: Missed-Approach Waypoint, for waypoint identifiers 
 
M, MAG: Magnetic MAN: Manifold, Manual MANIF: Manifold MAP: Manifold Pressure mB: Millibars MCDU: Multifunction Control Display Unit MDA: Minimum Descent Altitude MEA: Minimum En Route Altitude MM: Middle Marker MMO: Maximum operating limit (Mach) MOA: Military Operating Area MOPS: Minimum Operational Performance Specification MSA: Minimum Safe Altitude msec: Millisecond (one thousandth of a second) MSG: Message MSL: Mean Sea Level N: North ND: Navigation Display NDB: Non-directional Beacon NGSS: Next Generation Satellite Systems nm, NM: Nautical Mile NPA: Non-Precision Approach NRST: Nearest OBS: Omni-Bearing Selector   
OEM: Original Equipment Manufacturer OFST: Offset OM: Outer Marker OROCA: Off Route Obstacle Clearance Altitude 
 
PA: Proximate Advisory, Precision Approach PDA: Premature Descent Alert PFD: Primary Flight Display PPOS, PP: Present Position PRESS: Pressure PROC: Procedure PT: Procedure Turn PTK: Parallel Track R: Right runway  
R, RAD: Radial R, RT: Right R/D: Radial/Distance RAIM: Receiver Autonomous Integrity Monitoring RB: Relative Bearing REV: Reverse, Revision, Revise RF: Radio Frequency, Radius to Fix RNAV: Area Navigation RNG: Range RNP: Required Navigation Performance RPM: Revolutions Per Minute RTE: Route RWY: Runway S: South SA: Selective Availability   
SAS: Stability Augmentation System SBAS: Space Based Augmentation System SEQ: Sequence, Sequencing SET: Setup 
 
SG: Symbol Generator SSA: System Safety Assessment STAR: Standard Terminal Arrival Route SUA: Special Use Airspace SUSP: Suspend SVS: Synthetic Vision System T: True T/F: To/From TA: Traffic Advisory, Transition Altitude   
TAS: True Air Speed or Traffic Advisory System TAWS: Terrain Awareness and Warning TCAS: Traffic Collision Avoidance System TCH: Threshold Crossing Height TEMP: Temperature TERM, TER: Terminal TF: Track-to-Fix TH: True Heading TK, TRK: Track TKE: Track Angle Error TL: Transition Level   
TO: To TOGA: Takeoff/Go-around TSO: Technical Standard Order TSOA: Technical Standard Order Authorization TST: Test   
TTA: Time-to-Alert TWR: Tower UAT: Universal Access Transceiver 
 
UTC: Coordinated Universal Time VAL: Vertical Alert Limit VAR: Variation VECT: Vector VFR: Visual Flight Rules VHF: Very High Frequency VMO: Maximum operating limit speed (in knots) VNAV, VNV: Vertical Navigation VOR: VHF Omni Range VPL: Vertical Protection Level VS: Vertical Speed VSA: Visual Separation on Approach VTE: Vertical Track Error VTF: Vector-to Final VTK: Vertical Track VUL: Vertical Uncertainty Level W: West WAAS: Wide Area Augmentation System WARN, WRN: Warning WGS: World Geodetic System   
WPT: Waypoint XT, XTK: Cross-Track XTE: Cross-Track Error   

## 7. Notes 7.1 Revision Indicator

A change bar (l) located in the left margin is for the convenience of the user in locating areas where technical revisions, not editorial changes, have been made to the previous issue of this document. An (R) symbol to the left of the document title indicates a complete revision of the document, including technical revisions. Change bars and (R) are not used in original publications nor in documents that contain editorial changes only. 

## Appendix A - Declaration Of Efis Display Functions A.1 Introduction And Scope

A need exists to provide a permanent record of the specific AS6296 functions that are included in Electronic Flight Instrument System (EFIS) equipment submitted for Technical Standard Order (TSO) Authorization. This procedure provides for a record (hereafter referred to as the Declaration of EFIS Functions Form) to be included in the equipment data package submitted for TSO authorization and in the installation and maintenance instructions. 

Since it is not envisioned that the Declaration of EFIS Functions Form will be related to a particular equipment by serial number or date of manufacture, association shall be achieved through the equipment type, model, or part number. Manufacturers shall identify the functions included in the equipment. When a function is included, manufacturers shall identify if deviations were obtained.  When a function is incomplete, manufacturers shall identify the applicable requirements. When AS6296 defines more than one class of equipment for a given function, manufacturers should identify the class of their equipment in the appropriate row of the form. 

## A.2 Declaration Of Efis Functions Form

Refer to Figure 3 - Declaration of electronic flight instrument functions selected from AS6296 below. This form identifies the specific equipment type or model to which the list applies. This form provides the necessary information regarding which functions were included in the equipment, and compliance to the relevant detailed requirement sections of AS6296. This form lists the legacy TSOs and Minimum Operational Performance Specification (MOPS) from which the AS6296 requirements were derived, for reference purposes only.  Identify deviations and incomplete functions in the remarks box on the form. An example Declaration of EFIS Functions Form is shown in Figure 4 and has been annotated to illustrate a completed form. The example shown includes functions comprising a hypothetical Primary Flight Display.  Equipment manufacturers should expand on the data included on this form to provide added clarity. 

 
Nomenclature: _____________________________________________________________________ Address: __________________________________________________________________________ 
___________________________________________________________________________________ 
Manufacturer's Specification and/or Other Applicable Specification:  
___________________________________________________________________________________ 
Date of This Declaration: ___________________________________________________________ 
Declaration: 
X = Function not included. C = Function included and meets the requirements of AS6296. D = Function included with approved deviation(s).  
I = Incomplete function included and meets a subset of that function's requirements of AS6296.  

 
Function Name 
AS 6296 Section 
Legacy TSO/MOPS (Reference Only) 
Declaration (X, C, D, or I) 
Airspeed 
4.1.1 
TSO-C2d/AS 8019 
 
Vertical Velocity (Rate of Climb) 
4.1.2 
TSO-C8e/AS 8016A 
Altimeter 
4.1.3 
TSO-C10b/AS 392C/AS 8009B 
Attitude (Bank and Pitch) 
4.1.4 
TSO-C4c/AS 396B/AS 8001 
Direction Indicator 
4.1.5 
TSO-C5f/AS 8021 TSO-C6e/AS 8013A 
Max Allowable Airspeed 
4.1.6 
TSO-C46a/TSO-C46a 
 
Mach 
4.1.7 
TSO-C95a/AS 8018 
 
Turn and Slip 
4.1.8 
TSO-C3e/AS 8004 
 
Airborne Low-Range Radio Altimeter 
4.1.9 
TSO-C87a/ED-30  
 
4.1.10 
TSO-C198/DO-325 
 
Automatic Flight Guidance and Control System 
4.2.1 
TSO-C40c/DO-196 
 
Very High Frequency Omnidirectional Range 
(VOR) Distance Measuring Equipment (DME) 
4.2.2 
TSO-C66c/DO-189 
 
Localizer 
4.2.3 
TSO-C36e/DO-195 
 
Glideslope 
4.2.4 
TSO-C34e/DO-192 
 
Marker Beacon 
4.2.5 
TSO-C35d/DO-143 
 
Automatic Direction Finding (ADF) 
4.2.6 
TSO-C41d/DO-179 
 
4.2.7 
TSO-C146c/DO-229D 
 
Stand-Alone Airborne Navigation Equipment Using the Global Positioning System Augmented By The Satellite Based Augmentation System 
4.2.8 
TSO-C115c/DO-283A 
 
Flight Management System using Multisensor Inputs Microwave Landing System 
4.2.9 
TSO-C104/DO-177 
 
VHF Radio 
4.2.10 
TSO-C169a/DO-186B 
 
HF Radio 
4.2.11 
TSO-C170/DO-163 
 
| Function Name                           | AS 6296                                    |
|-----------------------------------------|--------------------------------------------|
| Section                                 |                                            |
| Legacy TSO/MOPS                         |                                            |
| (Reference Only)                        |                                            |
| Declaration                             |                                            |
| (X, C, D, or                            |                                            |
| I)                                      |                                            |
| Temperature*                            | 4.3.1                                      |
| Fuel Flow*                              | 4.3.2                                      |
| Manifold Pressure                       | 4.3.3                                      |
| Fuel, Oil, and Hydraulic Pressure       | 4.3.4                                      |
| Tachometer                              | 4.3.5                                      |
| Fuel and Oil Quantity                   | 4.3.6                                      |
| Windshear Warning and Escape Guidance   | 4.4.1                                      |
| Weather and Ground Mapping Radar        | 4.4.2                                      |
| Airborne Passive Thunderstorm Detection | 4.4.3                                      |
| 4.4.4                                   | TSO-C105/DO-174                            |
| Ground Mapping Radar Indicators         |                                            |
|                                         | Terrain Awareness and Ground Proximity*    |
| TSO-C151b/TSO-C151b                     |                                            |
| Helicopter TAWS                         | 4.5.2                                      |
|                                         | Traffic Collision Avoidance System (TCAS I |
| and II)                                 |                                            |
| 4.6.1                                   | TSO-C118a/DO-197A                          |
| TSO-C119d/DO-185B                       |                                            |
| modified and DO-300A                    |                                            |
| modified by the TSO                     |                                            |
|                                         | Traffic Advisory System                    |
| modified                                |                                            |

*Include the classes or types in the declaration column of the form above.  The classes for Temperature are in section 4.31. The types for Fuel Flow are in section 4.3.2.  The classes for TAWS are in 4.5.1.   

## Remarks:

 
 
Nomenclature: ____________________ The Best Electronic Flight Instrument _________________ TSO Model/Part No: _______________ Model 1, part number 123456________________________ Manufacturer: _____________________ The Best Instrument Company_______________________ Address: ___________________________123 Outstanding Street_____________________________ 
___________________________________ Our Town, Any State, USA_________________________ 
Manufacturer's Specification and/or Other Applicable Specification:  
____________________________________The Best Instrument Company Spec #1_______________ 
Date of This Declaration: _________________ July 22, 2015_______________________________ 
Declaration: 
X = Function not included. C = Function included and meets the requirements of AS6296. D = Function included with approved deviation(s).  
I = Incomplete function included and meets a subset of that function's requirements of AS6296.  

| Function Name                       | AS 6296             |
|-------------------------------------|---------------------|
| Section                             |                     |
| Legacy TSO/MOPS                     |                     |
| (Reference Only)                    |                     |
| Declaration                         |                     |
| (X, C, D, or                        |                     |
| I)                                  |                     |
| Airspeed                            | 4.1.1               |
| Vertical Velocity (Rate of Climb)   | 4.1.2               |
| C                                   | Altimeter           |
| 8009B                               |                     |
| Attitude (Bank and Pitch)           | 4.1.4               |
| C                                   | Direction Indicator |
| TSO-C6e/AS 8013A                    |                     |
| Max Allowable Airspeed              | 4.1.6               |
| Mach                                | 4.1.7               |
| Turn and Slip                       | 4.1.8               |
| Airborne Low-Range Radio Altimeter  | 4.1.9               |
| 4.1.10                              | TSO-C198/DO-325     |
| System                              |                     |
| 4.2.1                               | TSO-C40c/DO-196     |
| (VOR)                               |                     |
| Distance Measuring Equipment (DME)  | 4.2.2               |
| Localizer                           | 4.2.3               |
| Glideslope                          | 4.2.4               |
| Marker Beacon                       | 4.2.5               |
| Automatic Direction Finding (ADF)   | 4.2.6               |
| 4.2.7                               | TSO-C146c/DO-229D   |
| Using the Global Positioning System |                     |
| Augmented By The Satellite Based    |                     |
| Augmentation System                 |                     |
| 4.2.8                               | TSO-C115c/DO-283A   |
| sensor Inputs                       |                     |
| Microwave Landing System            | 4.2.9               |
| VHF Radio                           | 4.2.10              |
| HF Radio                            | 4.2.11              |
| Temperature*                        | 4.3.1               |
| Function Name                           | AS 6296                                    |
|-----------------------------------------|--------------------------------------------|
| Section                                 |                                            |
| Legacy TSO/MOPS                         |                                            |
| (Reference Only)                        |                                            |
| Declaration                             |                                            |
| (X, C, D, or                            |                                            |
| I)                                      |                                            |
| Fuel Flow*                              | 4.3.2                                      |
| Manifold Pressure                       | 4.3.3                                      |
| Fuel, Oil, and Hydraulic Pressure       | 4.3.4                                      |
| Tachometer                              | 4.3.5                                      |
| Fuel and Oil Quantity                   | 4.3.6                                      |
| Windshear Warning and Escape Guidance   | 4.4.1                                      |
| Weather and Ground Mapping Radar        | 4.4.2                                      |
| Airborne Passive Thunderstorm Detection | 4.4.3                                      |
| 4.4.4                                   | TSO-C105/DO-174                            |
| Ground Mapping Radar Indicators         |                                            |
| Terrain Awareness and Ground Proximity* | 4.5.1                                      |
| TSO-C151b/TSO-C151b                     |                                            |
| C                                       |                                            |
| Class A                                 |                                            |
| Helicopter TAWS                         | 4.5.2                                      |
| C                                       | Traffic Collision Avoidance System (TCAS I |
| and II)                                 |                                            |
| 4.6.1                                   | TSO-C118a/DO-197A                          |
| TSO-C119d/DO-185B                       |                                            |
| modified and DO-300A                    |                                            |
| modified by the TSO                     |                                            |
| X                                       | Traffic Advisory System                    |
| modified                                |                                            |

*   Include the classes or types in the declaration column of the form above.  The classes for Temperature are in section 4.31. The types for Fuel Flow are in section 4.3.2.  The classes for TAWS are in 4.5.1. 

## Remarks:

4.1.4 Attitude (Bank and Pitch), 4.1.4.2 Graduations: Pitch scale minor graduations are provided between -30 Degrees and +30 Degrees. 4.2.8  Flight Management System using Multi-sensor Inputs: Met all the requirements of this section except section 4.2.8.1.4 Holding Pattern. 4.4.1 Windshear Warning and Escape Guidance:  Windshear Warning Alert has been abbreviated to the annunciation "WS" to provide a compact format on the display. 

 

## A.3 Declaration Of Efis Error Contribution

Refer to Figure 5 - Declaration of electronic flight instrument error contribution below. This form summarizes the EFIS error contributions required to be specified by the manufacturer in the equipment installation manual per the detailed requirement sections of AS6296. For each function included in the EFIS, the manufacturer shall provide the error contribution information (including units of measure) to facilitate aircraft installation. A suggested format is depicted in Figure 5.  
 

AS6296 
Maximum 
Displayed 
Function Name 
Section 
Description of Error Parameter 
Error 
 
Airspeed 
4.1.1 
Maximum EFIS error contribution if the airspeed data is not Display-Ready Data 
4.1.2 
Maximum EFIS error contribution 
 
Vertical Velocity (Rate of 
Climb) 
 
Altimeter 
4.1.3 
Maximum EFIS error contribution if the altitude data is not Display-Ready Data 
 
Attitude (Bank and Pitch) 
4.1.4 
Maximum EFIS error contribution if the pitch and roll data is not Display-Ready Data 
 
Direction Indicator 
4.1.5 
Maximum EFIS error contribution if the heading or ground track data are not Display-Ready Data 
 
Max Allowable Airspeed 
4.1.6 
Maximum EFIS error contribution if the maximum allowable airspeed or maximum allowable mach data are not Display-Ready Data 
 
Mach 
4.1.7 
Maximum EFIS error contribution if the mach data is not Display-Ready Data 
Turn and Slip 
4.1.8 
95% displayed error 
Airborne Low-Range Radio Altimeter 
4.1.9 
Maximum EFIS error contribution if the radio altitude data is not Display-Ready Data 
4.1.10 
N/A 
 
Automatic Flight Guidance and Control System 
 
Very High Frequency Omnidirectional Range (VOR) 
4.2.1 
Maximum EFIS error contribution if VOR bearing data is not Display-Ready Data 


Maximum EFIS error contribution if the VOR course deviation data is not Display-Ready Data 
4.2.2 
95% error 
 
Distance Measuring Equipment (DME) 
 
Localizer 
4.2.3 
Maximum EFIS error contribution if the localizer deviation data is not Display- Ready Data 
 
Glideslope 
4.2.4 
Maximum EFIS error contribution if the glideslope deviation data is not Display- Ready Data 
Marker Beacon 
4.2.5 
N/A 
 
AS6296 
Maximum 
Displayed 
Function Name 
Section 
Description of Error Parameter 
Error 
 
Automatic Direction Finding (ADF) 
4.2.6 
Maximum EFIS error contribution if the ADF bearing data is not Display-Ready 
Data 
4.2.7 
N/A 
 
Stand-Alone Airborne Navigation Equipment Using the Global Positioning System Augmented By The Satellite Based Augmentation System 
4.2.8 
N/A 
 
Flight Management System using Multi-sensor Inputs Microwave Landing System 
4.2.9 
N/A 
 
VHF Radio 
4.2.10 
N/A 
 
HF Radio 
4.2.11 
N/A 
 
Temperature 
4.3.1 
Maximum EFIS error contribution 
 
Fuel Flow* 
4.3.2 
N/A 
 
Manifold Pressure  
4.3.3 
N/A 
 
4.3.4 
N/A 
 
Fuel, Oil, and Hydraulic Pressure Tachometer 
4.3.5 
Maximum EFIS error contribution 
 
Fuel and Oil Quantity 
4.3.6 
Maximum EFIS error contribution 
 
4.4.1 
N/A 
 
Windshear Warning and Escape Guidance 
 
Weather and Ground Mapping Radar 
4.4.2 
Maximum EFIS error contribution for bearing  


Maximum EFIS error contribution for range 


Maximum EFIS error contribution for numerical readouts if the data is not Display-Ready Data 
4.4.3 
N/A 
 
Airborne Passive 
Thunderstorm Detection 
4.4.4 
N/A 
 
Optional Display Equipment for Weather and Ground Mapping Radar Indicators 
4.5.1 
N/A 
 
Terrain Awareness and Ground Proximity Helicopter TAWS 
4.5.2 
N/A 
 
4.6.1 
N/A 
 
Traffic Collision Avoidance System (TCAS I and II) Traffic Advisory System 
4.6.2 
N/A 

## Appendix B - Air Speed Scale Error Performance Over Temperature Environment

AS6296 
AS8002A 
Air Speed Instrument 
 
Air Data Computer Tolerance 
Scale Error Tolerance 
EFIS Air Speed Display Scale Error 
Low 
operating 
High Operating 
Room 
Room 
Ambient 
of -20 C 
of +55 C 
Ambient 
Low/High 
Airspeed 
Tolerance 
Tolerance 
Tolerance 
Tolerance 
Operating 
Room Ambient 
Low Operating 
High Operating 
(KTS) 
(KTS) 
(KTS) 
(KTS) 
(KTS) 
(KTS) 
(KTS) 
(KTS) 
(KTS) 
20 
5.000 
6.725 
7.287 
5 
8 
Note 1 
1.275 
0.713 
30 
5.000 
6.725 
7.287 
5 
8 
Note 1 
1.275 
0.713 
40 
5.000 
6.725 
7.287 
5 
8 
Note 1 
1.275 
0.713 
50 
5.000 
6.725 
7.287 
5 
8 
Note 1 
1.275 
0.713 
60 
4.333 
5.828 
6.315 
5 
8 
0.667 
2.172 
1.685 
70 
3.667 
4.932 
5.343 
4 
7 
0.333 
2.068 
1.657 
80 
3.000 
4.035 
4.372 
4 
7 
1.000 
2.965 
2.628 
90 
2.500 
3.363 
3.643 
4 
7 
1.500 
3.638 
3.357 
100 
2.000 
2.690 
2.915 
3 
6 
1.000 
3.310 
3.085 
120 
2.000 
2.690 
2.915 
3 
6 
1.000 
3.310 
3.085 
140 
2.000 
2.690 
2.915 
3 
6 
1.000 
3.310 
3.085 
150 
2.000 
2.690 
2.915 
3 
6 
1.000 
3.310 
3.085 
160 
2.000 
2.690 
2.915 
3 
6 
1.000 
3.310 
3.085 
180 
2.000 
2.690 
2.915 
5 
8 
3.000 
5.310 
5.085 
200 
2.000 
2.690 
2.915 
5 
8 
3.000 
5.310 
5.085 
220 
2.160 
2.905 
3.148 
5 
8 
2.840 
5.095 
4.852 
250 
2.400 
3.228 
3.498 
5 
8 
2.600 
4.772 
4.502 
300 
2.800 
3.766 
4.080 
5 
8 
2.200 
4.234 
3.920 
350 
3.200 
4.304 
4.663 
5 
8 
1.800 
3.696 
3.337 
400 
3.600 
4.842 
5.246 
8 
11 
4.400 
6.158 
5.754 
450 
4.000 
5.380 
5.829 
8 
11 
4.000 
5.620 
5.171 
500 
4.000 
5.380 
5.829 
8 
11 
4.000 
5.620 
5.171 
550 
4.000 
5.380 
5.829 
8 
11 
4.000 
5.620 
5.171 
600 
4.000 
5.380 
5.829 
10 
13 
6.000 
7.620 
7.171 
650 
4.000 
5.380 
5.829 
10 
13 
6.000 
7.620 
7.171 
700 
4.000 
5.380 
5.829 
10 
13 
6.000 
7.620 
7.171 

The above low operating and high operating temperatures were selected to be -20 C and +55 C. This is an example only and may change based on the unit's installation environment. TSO-C106/AS8002 Table 3 was used for Room Ambient Air Data Computer Air Speed Performance Tolerance and 5.3 was used to calculate the Air Data Computer Air Speed Performance tolerances for low and high temperatures. NOTE 1:  
When the Room Ambient Air Data Computer Tolerance is equal to the Room Ambient Air Speed Indicator Scale Error tolerance a Scale Error of less than 0.5 knots should be used to avoid rounding to the next higher digit. 