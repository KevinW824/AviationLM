RTCA, Inc. 

1150 18th Street, NW, Suite 910 
Washington, DC 20036-4001 
 USA  

# Minimum Operational Performance Standards (Mops) For Airborne Selective Calling Equipment

RTCA DO-93A 
Prepared by: SC-232 
March 17, 2016 
© 2016 RTCA, Inc. 

Copies of this document may be obtained from RTCA, Inc. 

1150 18th Street, NW, Suite 910 
Washington, DC 20036-4001, USA 
Telephone: 202-833-9339 
Facsimile: 202-833-9434 
Internet: www.rtca.org Please visit the RTCA Online Store for document pricing and ordering information. 

## Foreword

 
This report was prepared by Special Committee 232 (SC-232) and approved by the RTCA Program Management Committee (PMC) on March 17, 2016. RTCA, Incorporated is a not-for-profit corporation formed to advance the art and science of aviation and aviation electronic systems for the benefit of the public. The organization functions as a Federal advisory committee, and develops consensus-based recommendations on contemporary aviation issues. RTCA's objectives include but are not limited to the following: 
 
Coalescing aviation system user and provider technical requirements in a manner that helps government and industry meet their mutual objectives and responsibilities 

 
Analyzing and recommending solutions to the system technical issues that aviation faces as it continues to pursue increased safety, system capacity and efficiency 
 
Developing consensus on the application of pertinent technology to fulfill user and provider requirements, including development of minimum operational performance standards for electronic systems and equipment that support aviation 
 
Assisting in developing the appropriate technical material upon which positions for the International Civil Aviation Organization and the International Telecommunication Union and other appropriate international organizations can be based. 
 The organization's recommendations are often used as the basis for government and private sector decisions as well as the foundation for many Federal Aviation Administration Technical Standard Orders and several advisory circulars. Since RTCA is not an official agency of the United States Government, its recommendations may not be regarded as statements of official government policy unless so enunciated by the U.S. government organization or agency having statutory jurisdiction over any matters to which the recommendations relate. 

## "Disclaimer"

 This publication is based on material submitted by various participants during the SC approval process. Neither the SC nor RTCA has made any determination whether these materials could be subject to valid claims of patent, copyright or other proprietary rights by third parties, and no representation or warranty, expressed or implied is made in this regard.  Any use of or reliance on this document shall constitute an acceptance thereof "as is" and be subject to this disclaimer." 
--`,,,,`````,,`````,`,``,`,,```-`-`,,`,,`,`,,`---

 
This Page Intentionally Left Blank 

 

## Revision History

| Rev Level                      | Description                                         | Date    | Effective Sections      |
|--------------------------------|-----------------------------------------------------|---------|-------------------------|
|                                | *Note - if the affected sections are extensive they |         | *Note - if the affected |
| may be captured in an Appendix | sections are extensive                              |         |                         |
| they may be captured in        |                                                     |         |                         |
| an Appendix                    |                                                     |         |                         |
|                                |                                                     |         |                         |
|                                |                                                     |         |                         |
|                                |                                                     |         |                         |
|                                |                                                     |         |                         |
|                                |                                                     |         |                         |
|                                |                                                     |         |                         |

Key to text in this MOPS drafting guide: - Text in plain format is meant to be retained as part of standard RTCA wording for all MOPS Documents. - Text in Bold Italics is meant to be a place holder for wording to be added by the committee that is appropriate to the specific type of equipment being developed. - Text in plain Italics is meant as notes to the committee to aid in writing the MOPS and should be removed during the writing process. 

 

## 1 Purpose And Scope 1.1 Introduction

This document contains Minimum Operational Performance Standards for Selective Calling (SELCAL) systems installed in all types of aircraft. These standards specify system characteristics that should be useful to designers, manufacturers, installers and users of the equipment. Compliance with these standards is recommended as one means of assuring that the equipment will perform its intended function(s) satisfactorily under all conditions normally encountered in routine aeronautical operation.  Any regulatory application of this document is the sole responsibility of appropriate governmental agencies. 

Section 1 of this document provides information needed to understand the rationale for equipment characteristics and requirements stated in the remaining sections.  It describes typical equipment operations and operation goals, as envisioned by the members of Special Committee SC-232, and establishes the basis for the standards stated in Sections 2 through 3.  Definitions and assumptions essential to proper understanding of this document are also provided in this section. Section 2 contains the Minimum Performance Standards for the equipment.  These standards specify the required performance under standard environmental conditions.  Also included are recommended bench test procedures necessary to demonstrate equipment compliance with the stated minimum requirements. Section 3 describes the performance required of installed equipment.  Tests for the installed equipment are included when performance cannot be adequately determined through bench testing. Section 4 describes the operational performance characteristics for equipment installations and defines conditions that will assure the equipment user that operations can be conducted safely and reliably in the expected operational environment. This document considers an equipment configuration consisting of a SELCAL Unit and VHF and/or HF transceivers.  Operational performance standards for functions or components that refer to equipment capabilities that exceed the stated minimum requirements are identified as optional features.   
The word "equipment" as used in this document includes all components and units necessary for the system to properly perform its intended function(s).  For example, the "equipment" may include a standalone SELCAL decoder or an Audio System with integrated SELCAL functionality. Each design will include both SELCAL decoding and annunciating capabilities as well as a means of configuring the unique SELCAL code for the aircraft. This MOPS applies to a specific defined function.  The equipment may have additional features related to that function for which there are no specified minimum performance requirements. For example, many VHF radios have an active-standby frequency "flip-flop" 
feature for which there are no specified requirements or tests.  Equipment may also have additional functions for which other MOPS or TSOs may be applicable or it may contain additional functions not defined by any MOPS or TSO, in which case non-TSO function guidance may be applicable. If the equipment implementation includes a computer software package, the guidelines contained in RTCA Document No. DO-178C, *(or the most current published revision)* Software Consideration in Airborne Systems and Equipment Certification, should be considered. 

## 1.2 System Overview The Purpose Of Selcal Is To Permit The Selective Calling Of Individual Aircraft Using Common Hf And Vhf Radio Communications Paths.

The elements comprising the overall SELCAL system are as follows: 

(a)  Ground selective calling encoder (b)  Ground-to-air transmitter (HF or VHF) 
 
(c)  Airborne receiver (HF or VHF) (d)  Airborne selective calling decoder (e)  Means of annunciation 
 
Items (b) and (c) comprise the typical communication paths. Item (a) is the ground portion of the SELCAL coding device which supplies coded information to the ground-based transmitter, Item (b). Item (d) is the airborne SELCAL function that operates with existing communications receivers on the aircraft, Item (c), to permit decoding of the ground-to-air signals for annunciation (e). The form of annunciation (e) should be chosen to suit the operational requirements of the user, and must contain visual and audible annunciating devices. Items (d) and (e) may be integrated into the aircraft audio system. Item (d) may also be integrated into Item (c). 

1.2.1 
Document Hierarchy The following documents contain additional guidance regarding SELCAL functionality. In case of conflict, this document, DO-93A, will take precedence. Additional documents in order of precedence: ICAO Annex 10  International Standards and Recommended Practices -Aeronautical Telecommunications. ARINC Characteristic 714A    Mark 4 Airborne SELCAL 
1.3 
Intended Function Selective calling of an aircraft is accomplished as follows: Each aircraft capable of SELCAL operation is assigned an identifying four-character alphanumeric code. The ground communicator selects the proper code. The ground transmitter is then modulated by this coded audio signal. The airborne receiver demodulates the RF signal and the coded audio signal is applied to the SELCAL decoder. The decoder is designed so that it will respond only to the code for which it is configured. It rejects all other codes. Upon receipt of an acceptable coded signal, the decoder actuates both a visual and an audible indicator which, at the user's option, may be a lamp, a bell, a chime, or any combination of such crew alerting devices. The pilot, having been alerted, may clear the alert and answer the call by communicating with the ground station. The airborne SELCAL decoder must be capable of being configured to interpret the code that is assigned to the aircraft. The airborne receiver and decoder functions must be capable of receiving and interpreting the correct code and rejecting all other codes in the presence of random noise and interference. 

 
A positive calling should be presented to the flight crew by means of a suitable aural and visual signaling device such as a chime or lamp. SELCAL has a functional hazard classification of minor. Loss or malfunction of SELCAL 
operation will result in increased pilot workload. 

## 1.4 Operational Goals

The SELCAL system serves as a one-way ground-to-air paging service. The system is designed to alleviate the pilot workload of continuous monitoring of VHF/HF radio communications and instead notify the flight crew when ground contact is requested. The ground system transmits a unique code by sending two consecutive pulses of 1.0 ± 0.25 seconds duration, separated by an interval of 0.2 ± 0.1 seconds. Each pulse consists of the sum of two simultaneously occurring tones. The call consists of one transmission without repetition. An example of a transmitted code (AC-BD) is shown in Figure 1-1. 

The transmitted signal is received by one of the aircraft radios and passed to the SELCAL decoder. If the decoded signal matches the unique code for the aircraft, the SELCAL decoder will provide a visual and aural alert for the associated radio channel. The airborne receiver and decoder functions must be capable of receiving and identifying the correct code in the presence of random noise, distortion and RF propagation effects, as defined later in this document, and rejecting all other codes. The SELCAL system is expected to operate successfully under all RF channel conditions that support voice communication. In practice, SELCAL notification often operates successfully in conditions where voice communications are difficult or ineffective. 

SELCAL codes consist of 4 unique tone designators, each corresponding to an audio frequency from Table 1 below (ex. AC-BD): 

Designator 
Audio Frequency 
(Hz) 
A 
312.6 
B 
346.7 
C 
384.6 
D 
426.6 
E 
473.2 
F 
524.8 
G 
582.1 
H 
645.7 
J 
716.1 
K 
794.3 
L 
881.0 
M 
977.2 
P 
1083.9 
Q 
1202.3 
R 
1333.5 
S 
1479.1 
T 
329.2 
U 
365.2 
V 
405.0 
W 
449.3 
X 
498.3 
Y 
552.7 
Z 
613.1 
1 
680.0 
2 
754.2 
3 
836.6 
4 
927.9 
5 
1029.2 
6 
1141.6 
7 
1266.2 
8 
1404.4 
9 
1557.8 

## 1.5 Assumptions

Ground Station transmitters will fully comply with the ICAO Annex 10 specifications. 

The SELCAL decoder utilizes a non-squelched radio output, with no Audio Gain Control, as the audio source for detection. 

## 1.6 Test Procedures

The test procedures specified in this document are intended to be used as one means of demonstrating compliance with the performance requirements defined in Section 2.2. Although specific test procedures are cited, it is recognized that other methods may be acceptable.  These alternate procedures may be used if they provide equivalent verification data.  In such cases, the procedures cited herein should be used as one criterion in evaluating the acceptability of the alternate procedures. Users of this document should not infer performance requirements based on Test Procedures. The order of tests specified suggests that the equipment be subjected to a succession of tests as it moves from design, and design qualification, into operational use.  For example, compliance with the requirements of Section 2 shall have been demonstrated as a precondition to satisfactory completion of the installed system tests of Section 3. 

## 

(a) Environmental Tests 
Environmental test requirements are specified in Subsection 2.3.  The procedures and their associated limits are intended to provide a laboratory means of determining the electrical and mechanical performance of the equipment under environmental conditions expected to be encountered in actual operations. Unless otherwise specified, the environmental conditions and test procedures contained in RTCA Document No. DO-160G, Environmental Conditions and Test Procedures for Airborne Equipment, will be used to demonstrate equipment compliance. 

(b) Bench Tests 
Bench test procedures are specified in Subsection 2.4.  These tests provide a laboratory means of demonstrating compliance with the requirements of Subsection 2.2.  Test results may be used by equipment manufacturers as design guidance, for monitoring manufacturing compliance and, in certain cases, for obtaining formal approval of equipment design. 

(c) Installed Equipment Considerations 
Tests for the installed equipment are included when performance cannot be adequately determined through bench testing. The installed equipment test procedures and their associated limits are specified in Section 3.  Although bench and environmental test procedures are not included in the installed equipment test, their successful completion is a precondition to completion of the installed test.  In certain instances, however, installed equipment test may be used in lieu of bench test simulation of such factors as power supply characteristics, interference from or to other equipment installed on the aircraft, etc.  Installed tests are normally performed under two conditions: 

1. With the aircraft on the ground and using simulated or operational system inputs. 2. With the aircraft in flight using operational system inputs appropriate to the 
equipment under test. 
Test results may be used to demonstrate functional performance in the intended operational environment. 

--`,,,,`````,,`````,`,``,`,,```-`-`,,`,,`,`,,`---

(d) Operational Tests 
The operational tests, if required, are specified in Section 4.  These test procedures and their associated limits are intended to be conducted by operating personnel as one means of ensuring that the equipment is functioning properly and can be reliably used for its intended function(s). 

## 1.7 Acronyms, Abbreviations, And Definitions Ac      Advisory Circular Ac      Alternating Current Ansp Air Navigation Service Provider

ASRI     Aviation Spectrum Resources Incorporated ATIS     Automatic Terminal Information Service C       degrees Celsius CFR 
     Code of Federal Regulations 
dB       Decibel DAL     Design Assurance Level ERAM    En Route Automation Modernization F 
       degrees Fahrenheit 
FAA     Federal Aviation Administration FAR 
     Federal Aviation Regulations 
FCC 
     Federal Communications Commission 
HF 
      High Frequency 
Hz       Hertz ICAO     International Civil Aviation Organization IM 
      intermodulation 
ITU      International Telecommunication Union kPa      kilopascal Mark 3    Mark 3 SELCAL System (16 tone, A-S) Mark 4    Mark 4 SELCAL System (32 tone, A-9) MOPS    Minimum Operational Performance Standards RF 
      Radio Frequency 
RMS     Root Mean Square SAE 
     Society of Automotive Engineers 
SELCAL   Selective Calling TSO 
     Technical Standard Orders 
V       volt 
VHF     Very High Frequency 

## 1.8 Anticipated Future Growth

ARINC 714-6 Mark 3 SELCAL system uses a set of 16 audible tones and 10,920 unique SELCAL codes. ARINC 714A Mark 4 SELCAL is capable of decoding up to 215,760 unique SELCAL code identifiers by using a set of 32 audible tones defined herein. Future growth of the SELCAL system is not anticipated. 

## 2 Equipment Performance Requirements And Test Procedures 2.1 General Requirements 2.1.1 Airworthiness

In the design and manufacture of the equipment, the manufacturer shall provide for installation so as not to impair the airworthiness of the aircraft. 

## 2.1.2 Intended Function

The equipment shall perform its intended function(s), as defined by the manufacturer, and its proper use shall not create a hazard to other users of the National Airspace System. 

## 2.1.3 Federal Communications Commission Rules

All equipment shall comply with the applicable rules of the Federal Communications Commission (FCC). 

## 2.1.4 Fire Protection

All materials used shall be self-extinguishing except for small parts (such as knobs, fasteners, seals, grommets and small electrical parts) that would not contribute significantly to the propagation of a fire. Unless compliance with 14 CFR §25.1309(b) is provided by the circuit protective device required by 14 CFR §25.1357(a), electric motors and transformers, including those installed in domestic systems, must have a suitable thermal protection device to prevent overheating under normal operation and failure conditions, if overheating could create a smoke or fire hazard. 

Note: One means of showing compliance is contained in Federal Aviation Regulations 
(FAR), Part 25.853, Appendix F. 

## 2.1.5 Operation Of Controls

The equipment shall be designed so that controls intended for use during flight cannot be operated in any position, combination or sequence that would result in a condition detrimental to the reliability of the equipment or operation of the aircraft. 

## 2.1.6 Accessibility Of Controls

Controls that do not require adjustment during flight shall not be readily accessible to flight personnel. 

## 2.1.7 Effects Of Test

The equipment shall be designed so that the application of specified test procedures shall not be detrimental to equipment performance following the application of the tests, except as specifically allowed. 

## 2.1.8 Design Assurance

Design Assurance Levels (DAL) should be adequate to mitigate the failure classification appropriate to the contribution of the equipment to the aircraft level failure in the aircraft in which it is to be installed. Since the SELCAL system has a hazard classification of minor in accordance with Advisory Circular (AC) 25.1309-1A, *System Design and Analysis*, the corresponding design assurance level is D. For integrated SELCAL systems, a higher DAL may apply. 

Designers should apply the guidance specified in Society of Automotive Engineers (SAE) ARP-4754A, DO-178C, and DO-254, where applicable.  

## 2.1.9 Integrated Systems For Systems Where The Selcal Decoder Is Integrated With The Rf Receiver It Is Up To The Equipment Manufacturer To Produce A Modulated Rf Test Signal That Will Provide Equivalent Tone Input Levels To Those Specified In This Document. 2.2 Equipment Performance - Standard Conditions 2.2.1 Sensitivity And Range

The equipment shall provide proper code identification for input signals ranging from a threshold level of 0.1 volt (V) Root Mean Square (RMS) (each tone) across a nominal 10,000 ohms input impedance, to a level 30 Decibel (dB) above this threshold without change of any service adjustment. 

## 2.2.2 Tone Imbalance

Normal operation shall be obtained with amplitudes differing by as much as 12 dB between the two simultaneously transmitted tones in a tone pair. 

## 2.2.3 Harmonic Distortion

Normal operation shall be obtained with tone frequency harmonic distortion up to 15%. 

## 2.2.4 Tone Frequency Tolerance

Operation shall be normal with tone frequencies differing from assigned values by as much as +/- 0.15%. 

## 2.2.5 Noise Performance

The operation shall be normal in an environment containing white noise in the range of 0 to 5000 Hertz (Hz), rolling off at a rate of 6 dB per octave above 5000 Hz, having RMS voltage level of up to 6 dB above the voltage level of the tone having the lower amplitude. 

## 2.2.6 Tone Code Timing Tolerance

The operation shall be normal with tone durations varying by +/-0.25 second from the 1.0 second standard and with pulse spacing varying by +/- 0.1 second from the 0.2 second standard. 

## 2.2.7 False Operation

The unit shall not respond when subjected to the following conditions: 

1. Random noise 2. Codes having tone frequencies 1.65% or more removed from the nominal 
frequencies selected in the unit under test. 

## 2.2.8 False Operation, Extended Duration

The unit shall not respond to random audio (e.g., normal aeronautical radio communications, Automatic Terminal Information Service (ATIS), other speech, or music) applied for an extended period of time. 

## 2.3 Equipment Performance - Environmental Conditions

The environmental tests and performance requirements described in this subsection provide a laboratory means of determining the overall performance characteristics of the equipment under conditions representative of those that may be encountered in actual aeronautical operations.  
Some of the environmental tests contained in this subsection need not be performed unless the manufacturer wishes to qualify the equipment for that particular environmental condition.  These tests are identified by the phrase "When required."  If the manufacturer wishes to qualify the equipment to these additional environmental conditions, then these 
"When required" tests **shall** be performed.  
The test set-up procedures applicable to a determination of equipment performance under environmental test conditions are contained in RTCA Document DO-160G, Environmental Conditions and Test Procedures for Airborne Equipment, December 8, 2010. For each environmental condition section, reference to the applicable DO-160G test is included in square brackets. 

2.3.1 
Temperature Test [DO-160G Section 4.5.1-4.5.4] 
When the equipment is subjected to this test: 

(a)  The standards of paragraphs 2.2.1, 2.2.2, 2.2.4 and 2.2.5 shall be met. 
(b)  All mechanical devices shall operate satisfactorily.  
2.3.2 
Loss of Cooling Test [DO-160G Section 4.5.5] 
When the equipment is subjected to this test, the performance requirements of paragraphs 2.2.1, 2.2.2, 2.2.4 and 2.2.5 shall be met. 

2.3.3 
Altitude Test *[DO-160G Section 4.6.1]* 
When the equipment is subjected to the test, the requirements of paragraphs 2.2.1, 2.2.2, 
2.2.4, and 2.2.5 shall be met. 

2.3.4 
Decompression Test (When required) *[DO-160G Section 4.6.2]* 
When the equipment is subjected to this test, the performance requirements of paragraphs 2.2.1 and 2.2.5 shall be met. 

2.3.5 
Overpressure Test (When required) *[DO-160G Section 4.6.3]* 
After being subjected to Overpressure, the standards of paragraphs 2.2.1, 2.2.2, 2.2.4, and 2.2.5 shall be met. 

2.3.6 
Temperature Variation Test *[DO-160G Section 5]* 
When the equipment is subjected to this test, the standards of paragraphs 2.2.1and 2.2.5 
shall be met. 

2.3.7 
Humidity Test [DO-160G Section 6] 
After being subjected to Humidity, the standards of paragraphs 2.2.1, 2.2.2, 2.2.4 and 2.2.5 shall be met. 

2.3.8 
Operational Shock and Crash Safety Test *[DO-160G Section 7]* 
(a)  Following the application of Operational Shocks, 
 
1. The standards of paragraphs 2.2.1, 2.2.2, and 2.2.5 shall be met. 

2. All mechanical devices shall operate satisfactorily. 

(b) Following the application of the Crash Safety Shocks, the equipment under test shall 
have remained in its mounting, and no parts of the equipment or its mounting shall 
have become detached and free of the equipment. No performance requirements 
apply. 
 

2.3.9 
Vibration Test *[DO-160G Section 8]* 
When the equipment is subjected to this test, the standards of paragraphs 2.2.1 and 2.2.5 
shall be met. 

2.3.10 
Explosion Proofness (When required) *[DO-160G Section 9]* 
No MOPS performance measurement is required during this test. 

2.3.11 
Waterproofness (When required) [DO-160G Section 10] 
After being subjected to Waterproofness, the standards of paragraphs 2.2.1, 2.2.2, 2.2.4, and 2.2.5 shall be met. 

2.3.12 
Fluids Susceptibility (When required) *[DO-160G Section 11]* 
After being subjected to Fluids Susceptibility, the standards of paragraphs 2.2.1, 2.2.2, 2.2.4, and 2.2.5 shall be met. 

2.3.13 
Sand and Dust (When required) *[DO-160G Section 12]* 
After being subjected to Sand and Dust, the standards of paragraphs 2.2.1, 2.2.2, 2.2.4, and 
2.2.5 shall be met. 

2.3.14 
Fungus Resistance (When required) [DO-160G Section 13] 
No MOPS performance measurement is required during this test. 

2.3.15 
Salt Spray (When required) *[DO-160G Section 14]* 
After being subjected to Salt Spray, the standards of paragraphs 2.2.1, 2.2.2, 2.2.4, and 
2.2.5 shall be met. 

2.3.16 
Magnetic Effect Test *[DO-160G Section 15]* 
This test determines the effects of the SELCAL equipment on other aircraft equipment and therefore does not involve the SELCAL performance requirements of this document. 

2.3.17 
Power Input Test *[DO-160G Section 16]* 
When the equipment is subjected to this test, the standards of paragraphs 2.2.1, 2.2.2, 
2.2.4 and 2.2.5 shall be met. 

2.3.18 
Voltage Spike Test *[DO-160G Section 17]* 
(a) Following the Intermittent Transient Test, the performance requirements of paragraphs 
2.2.1, 2.2.2, 2.2.4 and 2.2.5 shall be met. 
(b) During the Repetitive Transient Test, the performance requirements of paragraphs 
2.2.1 and 2.2.7 shall be met. 
2.3.19 
Audio-Frequency Conducted Susceptibility Test *[DO-160G Section 18]* 
When the equipment is subjected to this test, the performance requirements of paragraphs 2.2.5 and 2.2.7 shall be met. 

2.3.20 
Induced Signals Susceptibility Test *[DO-160G Section 19]* 
When the equipment is subjected to this test, the performance requirements of paragraphs 2.2.5 and 2.2.7 shall be met. 

## 2.3.21 Radio Frequency Susceptibility Tests

2.3.21.1 
Conducted Susceptibility Test *[DO-160G Section 20.4]* 
When the equipment is subjected to this test, the performance requirements of paragraphs 
2.2.1, 2.2.5 and 2.2.7 shall be met. 

2.3.21.2 
Radiated Susceptibility Test *[DO-160G Section 20.5 or 20.6]* 
When the equipment is subjected to this test, the performance requirements of paragraphs 2.2.1, 2.2.5 and 2.2.7 shall be met. 

## 2.3.22 Radio Frequency Emissions Tests

2.3.22.1 
Conducted Radio Frequency Emissions Test *[DO-160G Section 21.4]* 
No MOPS performance measurement is required during this test. 
2.3.22.2 
Radiated Radio Frequency Emissions Test *[DO-160G Section 21.5 or 21.6]* 
No MOPS performance measurement is required during this test. 
2.3.23 
Lightning Induced Transient Susceptibility Test (When required) [DO-160G Section 22] 
After being subjected to Lightning Induced Transients, the standards of paragraphs 2.2.1, 2.2.5, and 2.2.7 shall be met. 

2.3.24 
Lightning Direct Effects (When required) *[DO-160G Section 23]* 
After being subjected to Lightning Direct Effects, the standards of paragraphs 2.2.1, 2.2.5, and 2.2.7 shall be met. 

2.3.25 
Icing (When required) *[DO-160G Section 24]* 
After being subjected to Icing, the standards of paragraphs 2.2.1, 2.2.2, 2.2.4 and 2.2.5 shall be met. 

2.3.26 
Electrostatic Discharge Test *[DO-160G Section 25]* 

After being subjected to Electrostatic Discharge, the standards of paragraphs 2.2.1, 2.2.5, 
and 2.2.7 shall be met. 

2.3.27 
Fire, Flammability Test (When required) *[DO-160G Section 26]* 

No MOPS performance measurement is required during this test.  

## 2.4 Equipment Test Procedures 2.4.1 Definitions Of Terms And Conditions Of Test

The following are definitions of terms and the conditions under which the tests described in this subsection should be conducted. 

(a) Power Input Voltage - Unless otherwise specified, all tests shall be conducted with the 
power input voltage adjusted to design voltage, plus or minus 2%.  The input voltage shall be measured at the input terminals of the equipment under test. 
(b) Power Input Frequency 
1) In the case of equipment designed for operation from an alternating current (AC) 
source of essentially constant frequency (e.g., 400 Hz), the input frequency shall be adjusted to design frequency, plus or minus 2%. 
2) In the case of equipment designed for operation from an AC source of variable 
frequency (e.g., 300 to 1,000 Hz), unless otherwise specified, tests shall be conducted with the input frequency adjusted to within 5% of a selected frequency and within the range for which the equipment is designed. 
(c) Adjustment of Equipment - The circuits of the equipment under test shall be properly 
aligned and otherwise adjusted in accordance with the manufacturer's recommended 
practices prior to application of the specified tests. 
(d) Test Equipment - All equipment used in the performance of the tests should be 
identified by make, model and serial number where appropriate, and its latest calibration date.  When appropriate, all test equipment calibration standards should be traceable to national and/or international standards. 
(e) Test Instrument Precautions - Adequate precautions shall be taken during the test to 
prevent the introduction of errors resulting from the connection of voltmeters, oscilloscopes and other test instruments across the input and output impedances of the equipment under test. 
(f) Ambient Conditions - Unless otherwise specified, all tests shall be made within the 
following ambient conditions: 
1) Temperature: +15 to +35 degrees Celsius (C) (+59 to +95 degrees Fahrenheit (F)). 
2) Relative Humidity: Not greater than 85%. 3) Ambient Pressure: 84 to 107 kilopascal (kPa) (equivalent to +5,000 to –1,500 ft) 
(+1,525 to –460m). 
(g) Warm-up Period - Unless otherwise specified, all tests shall be performed after 
allowing for a warm-up period as specified by the manufacturer. 
(h) Connected Loads - Unless otherwise specified, all tests shall be performed with the 
equipment connected to loads having the impedance values for which it is designed. 
(i) Signal Input Voltage - The "Signal Input Voltage" is defined as the RMS value of the 
voltage (across a nominal 10,000 ohms) of one of the signaling tones. 
(j) Standard SELCAL Test Signal - The standard SELCAL test signal consists of two 
pulses of equal amplitude. Each pulse consists of two simultaneously occurring tones of equal amplitude. Each pulse has a duration of 1.0 +/- 0.25 second and the two pulses are separated by an interval of 0.2 +/- 0.1 second. Refer to Section 1.4. 

## 2.4.2 Detailed Test Procedures

The test procedures set forth below constitute a satisfactory method of determining required performance.  Although specific test procedures are cited, it is recognized that other methods may be preferred.  Such alternate methods may be used if the manufacturer can show that they provide at least equivalent information.   

## 2.4.2.1 Sensitivity And Range (Paragraph 2.2.1)

Equipment Required: 

1. SELCAL tone and signal generator. 2. RMS voltage measurement equipment  
Measurement Procedure: 

1. Apply an input signal of 0.1 volt (V), balanced tones, and check for normal 
operation on representative codes, involving each of the 32 tones. Increase the input signal to 3.2 volts, balanced tones, and repeat the above test. 

## 2.4.2.2 Tone Imbalance (Paragraph 2.2.2)

Equipment Required: 

1. SELCAL tone and signal generator. 2. RMS voltage measurement equipment  
Measurement Procedure: 

1. Apply an imbalanced tone input signal of 0.1 volt and 0.4 volt in both pulses and 
check for normal operation on representative codes involving each of the 32 tones. Increase the imbalanced tone input voltages to 0.8 volt and 3.2 volt and repeat the above test. 
For example, if your representative code is AS-BR, test with the following tone input signal values: 

|        | A     | S     | B     | R     |
|--------|-------|-------|-------|-------|
| Test 1 | 0.1 V | 0.4 V | 0.1 V | 0.4 V |
| Test 2 | 0.4 V | 0.1 V | 0.4 V | 0.1 V |
| Test 3 | 0.8 V | 3.2 V | 0.8 V | 3.2 V |
| Test 4 | 3.2 V | 0.8 V | 3.2 V | 0.8 V |

 

## 2.4.2.3 Harmonic Distortion (Paragraph 2.2.3)

Equipment Required: 

1. Distortion Analyzer 2. SELCAL tone and signal generator. 3. RMS voltage measurement equipment  
Measurement Procedure: 

## 

1. Apply 15% harmonic distortion to each tone in a standard SELCAL Test Signal 
with a level of 0.1 volts into the input of the SELCAL decoder under test. Use the following set of SELCAL codes, which represent the entire SELCAL tone 
frequency range, and check for normal operation: AT-S9, H1-J2, A9-ST.  

## 2.4.2.4 Tone Frequency Tolerance (Paragraph 2.2.4)

Equipment Required: 

1. SELCAL tone and signal generator capable of ±0.15% offset from the standard 
SELCAL tone frequencies. 
2. RMS voltage measurement equipment  
Measurement Procedure:          

1. For each of the 32 tones, vary the frequency by +0.15% and -0.15% and check for 
normal operation at an input signal level of 0.1 volts. 

## 2.4.2.5 Noise Performance (Paragraph 2.2.5)

Equipment Required: 

1. SELCAL tone and signal generator. 2. RMS voltage measurement equipment 3. Noise generator capable of producing "white noise" essentially flat up to 5000 Hz 
then diminishing at a rate of not more than 6 dB per octave. 
Measurement Procedure: 

1. Apply a standard SELCAL Test Signal with an input level of 0.1 volt 
simultaneously with 0.2 volt of constant white noise, and check for normal operation. 

## 2.4.2.6 Tone Code Timing Tolerance (Paragraph 2.2.6)

Equipment Required: 

1. SELCAL tone and signal generator. 2. RMS voltage measurement equipment  
Measurement Procedure: 

1. Adjust the pulse durations to 0.75 second and the pulse amplitude for 0.1 volt. 
Adjust the pulse spacing for 0.3 second. Check for normal operation of the equipment. 
2. Adjust the pulse durations to 1.25 second and the pulse amplitude for 0.1 volt. 
Adjust the pulse spacing for 0.1 second. Check for normal operation of the equipment. 

## 2.4.2.7 False Operation (Paragraph 2.2.7)

Equipment Required: 

1. SELCAL tone and signal generator capable of ±1.65% offset from the standard 
SELCAL tone frequencies. 
2. RMS voltage measurement equipment  
3. Noise generator capable of producing "white noise" essentially flat up to 5000 Hz 
then diminishing at a rate of not more than 6 dB per octave. 
Measurement Procedure: 

1. Set the unit under test to respond to the SELCAL code AT-S9. 
2. Apply a constant white noise input signal with a level of 3.2 volts for a minimum 
of 1 minute under standard conditions and verify that the unit does not respond. (Durations of at least 3 seconds are acceptable while subjected to repetitive environmental tests that include incremental step testing). 
3. Apply a standard SELCAL Test Signal with an input level of 3.2 volts, and verify 
normal operation. Vary the frequency of each of the assigned tones, in turn, by +1.65% and -1.65%, and verify that the unit does not respond.  
4. Repeat step 3 using representative codes involving each of the 32 tones. 

## 2.4.2.8 False Operation, Extended Duration (Paragraph 2.2.8)

Equipment Required: 

1. Non-repetitive, continuous audio source consisting of music or speech (e.g., a 
commercial broadcast receiver or recording) 
2. RMS voltage measurement equipment  
 
Measurement Procedure: 

1. Set the unit under test to respond to the SELCAL code AT-S9. 2. Apply a non-repetitive, continuous audio source with a level of 1 volt for a 
minimum of 10 hours and verify that the unit does not respond.  
3. Repeat step 2 with the following SELCAL codes: H1-J2, A9-ST. 
 

## 3 Manufacturer Considerations For Installed Equipment

This section contains no design requirements. The purpose of this section is to provide useful considerations regarding equipment designed to meet these MOPS when that equipment is installed and used on an aircraft.   
For the most part, installed performance requirements are the same as those contained in Section 2, which were verified through bench and environmental test.  However, certain requirements may be affected by the physical installation (e.g., antenna patterns, receiver sensitivity, etc.) and can only be verified after installation.  The installed performance limits or validation requirements are generally provided in separate installation guidance related to the function(s) provided.  These are often provided in the form of Advisory Circulars (ACs) or their equivalents. Equipment designed to meet these MOPS generally require separate approval for installation and use on an aircraft.  This section is intended to provide some aircraft installation related considerations such that the equipment may also be able to obtain any additional required installation or use approvals when correctly installed in an aircraft. 

## 3.1 Equipment Installation 3.1.1 Accessibility

Controls and monitors provided for in-flight operations shall be readily accessible from the pilot's normal seated position.  The flight crew shall have an unobstructed view of the visual annunciation when in the normal seated position. 

## 3.1.2 Aircraft Environment

Equipment shall be compatible with the environmental condition present in the specific location in the aircraft where the equipment is installed. 

## 3.1.3 Display Visibility

Display intensity shall be suitable for data interpretation under all cockpit ambient light conditions ranging from total darkness to reflected sunlight. 

Note: Visors, glare-shields or filters may be an acceptable means of obtaining daylight 
visibility. 

## 3.1.4 Failure Protection

Any probable failure of the equipment shall not degrade the normal operation of equipment or systems connected to it.  Likewise, the failure of interfaced equipment or systems shall not degrade normal operation of this equipment. 

Note: Systems may have loss of function or malfunction of the MOPS function due to 
failures of required interfaced equipment.  For example, a failure of a radio may degrade normal operation of the SELCAL system.  When a MOPS function is dependent on proper function of interfaced equipment, this should be considered in the aircraft level system safety assessment.  Installation approval may depend on the ability to mitigate probable failures with techniques such as detection and annunciation, redundancy such that the failure is no longer probable, or other aircraft level mitigation techniques. 

## 3.1.5 Interference Effects

The equipment shall not be the source of harmful conducted or radiated interference nor be adversely affected by conducted or radiated interference from other equipment or systems installed in the aircraft. 

Note: Electromagnetic compatibility problems noted after installation of this equipment 
may result from such factors as the design characteristics of previously installed systems or equipment and the physical installation itself.  It is not intended that the equipment manufacturer design for all installation environments.  The installing facility will be responsible for resolving any incompatibility between this equipment and previously installed equipment in the aircraft.  The various factors contributing to the incompatibility shall be considered. 

## 3.1.6 Inadvertent Turnoff

Appropriate protection shall be provided to avoid the inadvertent turnoff of the equipment. 

## 3.2 Test Procedures For Installed Equipment Performance

Test Procedures for installed equipment are generally contained in separate installation or operational approval guidance such as ACs or their equivalents, with the goal of ensuring that the SELCAL function (visual and aural alerts) is working correctly for each decoding channel under standard conditions. 

--`,,,,`````,,`````,`,``,`,,```-`-`,,`,,`,`,,`---

## 4 Aircraft Operational Performance Characteristics

When equipment is designed and manufactured to meet these MOPS, and it is properly installed in an aircraft in accordance with applicable installation and operational approval guidance and regulations, it is expected that all aircraft level functional and operational performance criteria will be met. 

The equipment when installed contributes to the operation and performance of the MOPS functions at the aircraft level.  Other aircraft-level contributions such as redundant or additional equipment may also be required. The equipment design should consider the types and characteristics of aircraft for which installation of this equipment is intended as well as the MOPS function at an aircraft level, and the equipment should be designed such that the equipment's contribution to aircraft-level operational and functional requirements is adequate. 

## Rtca Special Committee 232 Airborne Selective Calling Equipment

| Chairs           |  Organization                     |
|------------------|-----------------------------------|
| Eric Kehoe       | AvtechTyee, Inc.                  |
| Victor Nagowski  | Aviation Spectrum Resources, Inc. |
| Secretary        |                                   |
|                  |                                   |
| Organization     |                                   |
| Daniel Martinec  | Avutel, Inc.                      |
| Program Director | Organization                      |
| Harold Moses     | RTCA, Inc                         |
| Members          | Orga                              |
| Scott            | Bauler                            |
| Luke             | Bogner                            |
| Rabah            | Bouda                             |
| François         | Courbun                           |
| Benoit           | Gauduin                           |
| Mark             | Goldberg                          |
| Robert           | Holcomb                           |
| Kris             | Hutchison                         |
| Christopher      | Meehan                            |
| Hugues           | Meunier                           |
| Robert           | Miller                            |
| Gregg            | Nesemeier                         |
| Frank            | Orsino                            |
| Greg             | Park                              |
| Mike             | Pham                              |
| David            | Phillips                          |
| Mark             | Prestrude                         |
| Paul             | Prisaznuk                         |
| David            | Robinson                          |
| Andrew           | Roy                               |
| Tim              | Totten                            |
| Ken              | Vander Putten                     |

## Appendix A Implementation Guidance Selcal Code Assignment Guidance

As a result of the SC-232 committee testing of legacy avionics, it was determined that some legacy avionics showed susceptibility to false detection when receiving Mark 4 SELCAL transmissions containing the new lower frequency tones (i.e., designators T through 1). In order to alleviate a potential operational problem, it is suggested that Aviation Spectrum Resources Incorporated (ASRI) as the administrator for the assignment of SELCAL codes, commence with the issuing of new SELCAL codes starting with the new higher frequency tones (i.e., designators 2 through 9). The SC-232 committee reviewed a theoretical analysis of the intermodulation (IM) products that are introduced when the 16 new tones are incorporated into the existing SELCAL system and the potential impacts on legacy systems. The analysis provided the IM products and the probability of false detection associated with each tone pair. While the amplitude of the IM product will be considerably less than the fundamental tone pair, it is still possible for the IM product to have enough amplitude to be detected if the initial signal is strong enough. The results of the analysis indicated that there are 73 tone pairs from the list of Mark 4 tone pairs that generate more IM products that could potentially affect the older 16 tone Mark 3 systems. While the odds of false detection are considered low, by initially excluding these SELCAL codes, it should minimize the risk and have little effect on code assignments due to the large number of codes (215,760) that will be available. It is suggested that ASRI commence with the assignment of SELCAL codes that initially exclude the 73 tone pairs that were identified as a result of the IM assessment. The 73 tone pairs identified in the analysis are included here: AT, AU, AW, AY, A1, A2, A3, BU, BV, BX, BZ, B2, B3, CT, CU, CV, CW, CY, C1, DT, DU, DV, DW, DX, DZ, EU, EV, EW, EX, EY, FT, FV, FW, FX, FZ, GT, GU, GW, GX, G1, HT, HV, HX, HY, H2, JT, JU, JY, JZ, J3, KU, KZ, K1, K4, L1, L2, L5, M2, M3, M6, P3, P4, P7, Q4, Q5, R6, TW, TY, UX, VW, VY, WX, WY The complete analysis will be provided to ASRI which will detail the guidance recommended for initial Mark 4 SELCAL code assignments. 

## Faa En Route Automation Modernization (Eram) Guidance

ASRI worked through the ICAO Communications Panel to implement the SELCAL code pool expansion in order to update the Air Navigation Service Providers (ANSPs) ground systems to support the SELCAL code pool expansion proposal in oceanic and in remote airspace regions. The FAA needs to consider the implications of the SELCAL code pool expansion to the domestic flight planning systems. As a minimum, an assessment of the ERAM system should be conducted in order to determine the SELCAL code pool expansion impact.  

## Airline Ground System Guidance

The airlines will need to evaluate the impact that the SELCAL code pool expansion may have on their ground systems when new aircraft are added to their fleets that support the expanded SELCAL code pool functionality. 

This Page Intentionally Left Blank 
--`,,,,`````,,`````,`,``,`,,```-`-`,,`,,`,`,,`---