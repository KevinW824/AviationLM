
## 

# Minimum Operational Performance Standards For Geosynchronous Orbit Aeronautical Mobile Satellite Services (Amss) Avionics

## 

 

 
                                  This Page Intentionally Left Blank 
                                                      

RTCA, Incorporated 
1140 Connecticut Avenue, N. W., Suite 1020 
Washington, DC  20036 

# Minimum Operational Performance Standards For Geosynchronous Orbit Aeronautical Mobile Satellite Services (Amss) Avionics



Prepared by SC-165 


©2000, RTCA, Inc. 



Copies of this document may be obtained from 
 
RTCA, Inc. 

1140 Connecticut Avenue, Northwest, Suite 1020 
Washington, D. C.  20036-4001  U.S.A. 

 
telephone:  202-833-9339 
facsimile:  202-833-9439 
Please contact RTCA for price and ordering information. 



This document was prepared by RTCA Special Committee 165 (SC-165).  It 
was approved by the RTCA Program Management Committee on April 19, 2000. 
 
 
RTCA, Inc., is an association of aeronautical organizations of the United States 
from both government and industry.  Dedicated to the advancement of aeronautics, RTCA seeks sound technical solutions to problems involving the application of electronics and telecommunications to aeronautical operations.  Its objective is the resolution of such problems by mutual agreement of its member organizations. The findings of RTCA are in the nature of recommendations to all organizations concerned.  As RTCA is not an official agency of the United States government, its recommendations may not be regarded as statements of official government policy unless so enunciated by the U.S. government organization or agency having statutory jurisdiction over any matters to which the recommendations relate. 

## Proprietary Disclaimer

 
This publication makes references to written material or systems that are protected by copyrights and/or patents.  RTCA offers no opinion on the validity of the proprietary claims of the specified holder(s) of copyrights and/or patents; neither does RTCA endorse or warrant the product of specific manufacturers or holders of copyrights and/or patents.  RTCA has no economic stake in the use of any proprietary product. 

 
This Page Intentionally Left Blank 

## Table Of Figures

Figure 1-1 
AMSS End-to-End System Model 
....................................................................................   2 
Figure 2-0 
AES Per-Carrier Transmit Spectrum ...............................................................................  41 
Figure 2-1 
Satellite Subnetwork Architecture (Airborne Side) ........................................................  47 
Figure 2-2 
Relationship Between Packets and SNPDUs (Example of Events)  (A) 
.........................  58 
Figure 2-3 
Relationship Between Packets and SNPDUs (Example of Events)  (B) .........................  59 
Figure 2-4 
[Reserved] 
........................................................................................................................  60 
Figure 2-5 
DCE Substate Hierarchy 
..................................................................................................  61 
Figure 2-6 
Cockpit Protocol Interworking -- Air-to-Ground Call Establishment .............................  79 
Figure 2-7 
Cockpit Protocol Interworking -- Ground-to-Air Call Establishment .............................  80 
Figure 2-8 
Cockpit Protocol Interworking -- Air-Initiated Call Clearing .........................................  81 
Figure 2-9 
Cockpit Protocol Interworking -- Ground-Initiated Call Clearing ..................................  82 
Figure 2-10 
Gain and Coverage, Axial Ratio, Pattern Discrim., Phase Discontinuity, C/M 
 
Discrim. -- Sections 2.4.3.3.1, 2.4.3.3.2, 2.4.3.3.3, 2.4.3.3.5, 2.4.3.3.10 ........................  94 
Figure 2-11 
Noise Temperature (Antenna Gain and Coverage) -- Section 2.4.3.3.1.3 
.......................  97 
Figure 2-12 
Voltage Standing Wave Ratio (VSWR) -- Section 2.4.3.3.4 
.......................................... 104 
Figure 2-13 
Antenna Switching Time -- Section 2.4.3.3.6 
................................................................. 105 
Figure 2-14 
Beam Switching Time -- Section 2.4.3.3.7 
..................................................................... 106 
Figure 2-15 
Pointing Response Time -- Section 2.4.3.3.8 ................................................................. 107 
Figure 2-16 
Power Handling -- Section 2.4.3.3.9 
............................................................................... 108 
Figure 2-17 
Antenna Intermodulation in the Receive Band -- Section 2.4.3.3.11 ............................. 113 
Figure 2-17a 
Radiated Antenna Intermodulation Products -- Section 2.4.3.3.12 ................................ 115 
Figure 2-18 
Pre-Viterbi P-Ch Char., BER Perf., Cct-mode Voice, Maint. Bit Sync, C-Ch BER Meas./Acc. -- Sections 2.4.4.2.1, 2.4.4.2.8, 2.4.4.2.10, 2.4.4.2.13, 2.4.4.2.14 ............... 119 
Figure 2-19 
Sensitivity and Desired Signal Dynamic Range -- Sections 2.4.4.2.2 and 2.4.4.2.5 ...... 121 
Figure 2-20 
Image/Spur. Resp. Rej. / Rej. of Signals Outside AES Rcv Band -- Section 2.4.4.2.3 .. 122 
Figure 2-21 
Receiver Linearity -- Section 2.4.4.2.4 
........................................................................... 126 
Figure 2-22 
Receiver Tuning -- Section 2.4.4.2.6  ............................................................................. 127 
Figure 2-23 
Capture Range and Doppler Rate -- Section 2.4.4.2.7 
.................................................... 129 
Figure 2-24 
Time to Acquire Superframe Lock -- Section 2.4.4.2.9 ................................................. 131 
Figure 2-25 
C-channel Bit Timing Recovery and Frame Lock Acquisition & False Frame Lock -- Sections 2.4.4.2.11, 2.4.4.2.12  
....................................................................................... 133 
Figure 2-26 
Channel Rates and Tolerance -- Section 2.4.4.3.1 
.......................................................... 137 
Figure 2-27 
Output Power, Adjustment, and Stability -- Sections 2.4.4.3.2, 2.4.4.3.3, 2.4.4.3.4 
...... 138 
Figure 2-28 
Harmonics, Spurious, and Noise -- Section 2.4.4.3.5 
..................................................... 141 
Figure 2-29 
Intermodulation Products -- Section 2.4.4.3.6 ................................................................ 143 
Figure 2-30 
Carrier off Level -- Section 2.4.4.3.7 
.............................................................................. 144 
Figure 2-31 
Transmitter Muting and Signal Spectrum -- Sections 2.4.4.3.8 and 2.4.4.3.16  
............. 145 
Figure 2-32 
Load Vswr Capability -- Section 2.4.4.3.9 ..................................................................... 146 
Figure 2-33 
Tuning Range & Channel Incrs, Frequency Acc, Doppler Corr, Doppler Rate 
 
Capability -- Sections 2.4.4.3.10, 2.4.4.3.13, 2.4.4.3.14, 2.4.4.3.15............................... 148 
Figure 2-34 
Tuning Stabilization Time -- Section  2.4.4.3.11 ........................................................... 150 
Figure 2-35 
Phase Noise -- Section 2.4.4.3.12 ................................................................................... 151 
Figure 2-36 
Transmit Pulse Shaping Filter Response - Section 2.4.4.3.17 
........................................ 156 
Figure 2-37 
SSN Data Link Layer & Pkt-mode Data Svc Tests -- Sec 2.4.5, 2.4.6, 2.4.7, 2.4.8 
....... 158 
Figure 2-38 
VCTS Test Configuration - Section 2.4.8 ...................................................................... 201 
Figure B-1 
An Example of an AES Receive Chain 
............................................................................ B-1 

## 1.0 Purpose And Scope 1.1 Introduction

 
This document contains minimum operational performance standards (MOPS) for Aeronautical Mobile Satellite Services (AMSS) operating in the frequency bands 1.5 and 1.6 GHz.  These standards specify system characteristics that should be useful to designers, manufacturers, installers and users of the AMSS system and equipment. 

Compliance with these standards is recommended as one means of assuring that the AMSS will perform its intended function(s) satisfactorily under all conditions normally encountered in routine aeronautical operations.  Any regulatory application of this document is the sole responsibility of appropriate governmental agencies. 

 
This document encompasses standards and descriptions of a system configuration including Ground Subnetworks; AMSS Satellite Subnetworks, of which the Aircraft Earth Station (AES) is one part; and Aircraft Subnetworks.  However, the specified Minimum Operational Performance Standards in this document address only the AES portion of the Satellite Subnetwork. 
 
The MOPS covers typical AMSS avionics requirements and tests for the AES.  It includes the purpose, scope and equipment performance requirements; recommended bench tests and other performance verification procedures; and installed-equipment tests and operational performance characteristics.  A companion document, RTCA DO-215A, Guidance on AMSS End-to-End System Performance and Verification Requirements, covers transmission characteristics for end-to-end AMSS service criteria of the network(s), including the remaining portions of the satellite subnetwork (the Ground Earth Stations (GES) and the satellite transponders), the Avionics Subnetworks interfacing with the AES and Ground Subnetworks that interface with the GES (see Figure 1-1). 

 
Section 1.0 of this document provides information needed to understand the rationale for AMSS equipment and system characteristics and requirements stated in the remaining sections.  It describes typical applications and operational goals as envisioned by the members of Special Committee 165 and establishes the basis for the standards stated in Sections 2.0 through 3.0.  Definitions and assumptions essential to proper understanding of this document are also provided in this section, while a more extensive glossary appears as Appendix A. 

 
Section 2.0 contains the minimum performance standards for the AES.  These standards specify the required performance under standard and environmental conditions.  Also included are recommended bench test procedures necessary to demonstrate equipment and network compliance with the stated minimum requirements. 

## 

 
Section 3.0 describes the performance required of the installed AES equipment.  Tests specifically for the installed equipment are included when performance cannot be adequately determined through bench testing. 
Section 4.0 describes the operational performance characteristics for equipment installations and for network operation and defines conditions that will assure the equipment user that operations can be conducted safely and reliably in the expected operational environment. 
The following list summarizes the industry standard documents and their specific versions referenced within this MOPS: 
 

|     |     |     | Reference Document Name       |     | Version    | Reference Name    |
|-----|-----|-----|-------------------------------|-----|------------|-------------------|
|     |     |     |                               |     |            |                   |
|     |     |     | Inmarsat SDM Module 1         |     |            | 1.42              |
|     |     |     | Inmarsat SDM Module 2         |     |            | 1.16              |
|     |     |     | Inmarsat SDM Module 5         |     |            | 3.0               |
|     |     |     | Inmarsat SDM Module 6         |     |            | 1.19              |
|     |     |     | ISO 8208 (English)            |     |            |                   |
|     |     |     | Inmarsat SDM Module 0         |     |            | 2.2               |
|     |     |     | Inmarsat SDM Module 5, Part 2 | 1.0 |            | "G"               |



* Includes Amendment 1. 
 
NOTE: 
These version numbers apply unless indicated otherwise. 

 
All of the documents in the list above fall under the proprietary disclaimer note at the beginning of this document. 

 
In the event of any conflict between documents, this MOPS shall take precedence. 
 
As used in this document, the term "AES" includes all components and units necessary for the aircraft system to communicate through a satellite.  The AES comprises multiple components, including antennas, high power amplifiers (HPAs), voice coders/decoders (CODECs) and modulators/demodulators (MODEMs).  A particular AES will not necessarily include all components or units referred to herein but will perform all required functions. 

The guidelines contained in RTCA/DO-178B, Software Considerations in Airborne Systems and Equipment Certification, should be considered with respect to aircraft AMSS software packages. 

## 1.2 System Overview

 
The AMSS provides worldwide communications directly between aircraft subnetworks and ground subnetworks via aeronautical mobile satellites and their ground earth stations. AMSS will support both data and voice communications between aircraft users and ground-based users such as Air Route Traffic Control Centers (ARTCCs) and aircraft operating authorities (airlines).  Communication services accommodated by AMSS functions include four categories:  Air Traffic Services (ATS), Aeronautical Operational Control (AOC), Aeronautical Administrative Communications (AAC) and Aeronautical Passenger Communications (APC).  This document concentrates on the first two categories as they pertain to safety and regularity of flight. 

## 1.2.1 Amss Architecture

 
The overall AMSS system will provide circuit-mode data and voice as well as packet-mode data exchanges between ground-based users and airborne users via satellite relay.  The architecture defines system characteristics that are needed to assure a minimum worldwide satellite air-ground communications interoperability.  This has been accomplished for 
packet data services to be used by the international civil aviation community through specifying the International Standardization Organization's (ISO) Open Systems Interconnection (OSI) model.  It is anticipated that AMSS data services will conform in the future with guidelines for the Aeronautical Telecommunications Network (ATN). 

 
Initially, all voice transmissions will be digitized at the earth stations (aircraft and ground) for satellite transmission and converted back to analog for use within the aircraft and in the terrestrial subnetworks.  In the future, direct digital transmission through the avionics and ground subnetworks to the user terminus may be employed where practical. 

## 1.2.2 Communications Characteristics

 
AMSS will operate in frequency bands allocated for satellite-to-aircraft and aircraft-tosatellite communications as well as the bands for "feeder" links between the satellite and GES.  AMSS uses both Frequency Division Multiple Access (FDMA) and Time Division Multiple Access (TDMA) techniques. 

Four radio frequency (RF) channel types have been defined which will accommodate all foreseen traffic types.  The "forward" direction means from the GES to the AES, while "return" direction means the AES to GES. The baseline RF channel types are: 

 
a. 
P-channel:  Packet mode Time Division Multiplex (TDM) channel, used in the forward direction to carry signaling and user data.  Transmission is continuous from each GES. 
b. 
R-channel:  Random access ("slotted Aloha") channel, used in burst mode in the return direction to carry the initial signaling data of a transaction, typically request signals, and some short-length packet-mode user data. 
c. 
T-channel:  TDMA channel, used in the return direction to carry packet-mode data. An "on-demand" time allocation scheme is used to optimize efficiency and is arbitrated by one GES to which the AES is logged-on. 
d. 
C-channel:  Circuit-mode channel, used in both forward and return directions for voice, voice/data, and data-only channels.  The use of the channel is controlled by assignment and release signaling at the start and end of each transaction.  The forward C-channel conserves satellite power by operating in a voice-actuated mode, while the return C-channel is continuously powered when operational.  When used for voice, these channels also may carry multiplexed data for signaling and for future ATC and AOC traffic. 
Universal signal formats and RF channel formats permit any aircraft to communicate with any GES operating in the AMSS system.  Several different data rates are available for user choice in order to accommodate different installations and service requirements. 
Two modulation waveforms for the signals-in-space are defined:  Aviation Binary Phase Shift Keying (A-BPSK) is used for RF channel data rates of up to and including 2,400 bits per second (bps), and Aviation Quaternary Phase Shift Keying (A-QPSK) is used for RF 
channel data rates above 2,400 bps.  (The term "aviation" designates agreed-upon high efficiency filter masks for the modulation.) 

## 1.2.3 Operational Service Levels

 
The levels of service available through the AMSS Satellite Subsystem are determined primarily by the equipage of corresponding AESs and GESs.  The ICAO AMSS Standards And Recommended Practices (SARPs) define four levels of system capability based on AES characteristics, requiring that one or more GESs in the system have the capabilities of operating compatibly with AESs.  All AESs, as a minimum, shall have a Level 1 capability and shall continuously monitor a P channel after log-on to a GES. 

 
Level 1  AESs provide basic packet-mode data communications and are capable of: 
 
a. 
reception on a P channel at channel rates of 600 or 1200 bps; and 
 
b. 
transmission on a T channel or an R channel at channel rates of 600 or 1200 bps (with 2400 bps as an additional recommended rate; simultaneous R- and T- channel transmission is not required). 
Level 2  AESs have the capabilities of Level 1 systems and additionally for: 


a. 
reception on a P channel at a channel rate of 10,500 bps (with 4800 bps as an additional recommended rate); and 
 
b. 
transmission on a T channel and an R channel at the channel rate of 10,500 bps (simultaneous R- and T-channel transmission is not required). 
 
Level 3  AESs have the capabilities of a Level 2 system and additionally the capability of reception and transmission on one C-channel pair at a channel rate of 8,400 or 21,000 bps (with 10,500 bps as an additional recommended rate).  Simultaneous C-channel operation with either the R or T channel is not required, and simultaneous R- and T-channel transmission is not required, nor the support of both 21,000 and 8,400 bps C-channels in the one AES. 

 
Level 4  AESs have the capabilities of a Level 3 system and additionally the capability for simultaneous operation on one or more C-channel pairs and transmission on an R channel and a T channel.  Simultaneous R- and T-channel transmission is not required; however, it is recommended that the AES have such capability whenever the C-channel operation is not in use. 
 
 
NOTE: 
An AES with Level 4 capability provides digitized voice capability on the C- channel(s) simultaneously with packet-mode capability on either the R- or T- channel and the P-channel, using two or more receive and two or more transmit 
channels. 
This MOPS covers and requires provision and verification of the minimum performance and test requirements for Level 1. 
 
Minimum performance and test and verification requirements are also included in this MOPS for: 

 
 
a. 
Optional use of the Level 2, 3 or 4 10.5 kbps channel rates for packet-mode data; 
 
b. 
Optional use of the Level 3 or Level 4 8.4 kbps and/or 21.0 kbps channel rate for circuit-mode voice services. 
 
 
NOTES: 1. 
To satisfy SARPs voice channel access delay requirements, provision and test of the 10.5 kbps channel-rate packet-mode data capability is required for equipment providing Level 3 or Level 4 voice capability for safety 
services. 


2. 
The optional 2400 and 4800 bps channel rates are neither covered nor 
required in this MOPS for any level. 
A description of the INMARSAT AES classes may be found in Reference Document "B", Section 2.1.3. 

## 1.2.4 Ground Equipment Requirements

 
Ground equipment is required for satellite system service organizations to provide communications service between the aircraft and land-based end users.  The equipment must conform to standards used in conjunction with the airborne equipment to provide for the integrity, reliability and timeliness required for aeronautical communications associated with safety and regularity of flight.  These characteristics are described in regard only to their service requirements in the RTCA document, Guidance on AMSS End-to-End System Performance and Verification Requirements (DO-215A). 

## 1.2.5 Satellite Requirements

 
In order to provide worldwide coverage with adequate backup capability, a number of satellites will be required for AMSS.  The satellites use linear, frequency-translating, nonprocessing repeaters (transponders) to provide communications capacity.  Requirements for the high availability and integrity necessary for safety-related mobile satellite services are described in the RTCA document, Guidance on AMSS End-to-End System Performance and Verification Requirements (DO-215A). 

## 1.2.6 Service Providers

 
Service providers oversee the management of and access to the satellites and terrestrial networks under their control.  In the AMSS system, they must guarantee transponder performance, accept priority rules for allocation of satellite power and supply acceptable system monitoring and control.  Also, voice and data connections to on-board subnetworks as well as ground subnetworks serving Air Traffic Control (ATC), airlines and others should be provided. 

## 1.2.7 Communication Protocols

 
 
For satellite communications to be effective between many aircraft belonging to different users and various ground end-systems, a single set of transmission protocols is defined. 
Packet data protocols are based on universally-accepted and proven OSI models with capabilities to interface with various network protocols without regard to the implementation of the subnetworks and physical media through which the messages pass. Messages traverse hierarchical protocol "layers."  Each layer in an originating subnetwork performs a function paralleled at the destination subnetwork's peer layer.  Possible differences in communicating systems are masked by these standard interfaces, permitting simplified and reliable interconnection of those systems. 
Each layer incorporates well-defined operations designed to optimize control and information flow across the layer boundaries.  To carry out its function, each layer may add protocol control information fields to the service-data-unit supplied by the layer above. However, each layer leaves the control information added by previous layers intact, treating it as data to be passed on unaltered. 
The OSI Reference Model defines seven such functional layers with responsibilities ranging from control of data transfer on the physical media (radio, wire, fiber, etc.) to control of the application user interface.  The seven layers are named: Physical, Data Link, Network, Transport, Session, Presentation and Application.  The AES and its counterpart on the ground (GES) implement either the lowest two or the lowest three layers of the OSI model to provide packet-mode data services.  This document defines the AES requirements and tests. 
The system requirements contained in Section 2.0 of this document support packet-mode communications reflected by the OSI.  Two modes of operation are permitted.  These modes are referred to as Data-2 and Data-3, to be consistent with existing industry standards (see Reference Document "F").  Data-2 operation provides transparent data communications by enveloping the packets received from a higher-layer entity (HLE) without using internal network layer protocols.  Data-3 operation provides to the user a packet-switched subnetwork that implements the lowest three layers of the OSI model (physical, data link and network) and is accessed using a standard interface defined in Reference Document "E". 

## 1.3 Operational Applications

 
Many applications for AMSS are potentially available; however, cost or other factors may limit users' access to all such applications (e.g., voice as well as data).  While applications for service categories will evolve with time, this document defines standards to support minimum implementations of all currently foreseen applications for ATS and AOC. 
 

## 1.3.1 Air Traffic Services (Ats)

 
Air Traffic Services (ATS) include Air Traffic Control (ATC), the Flight Information Service and the Alerting Service.  AMS(R)S will provide an important new capability for ATS and AOC voice and data applications. 

## 1.3.1.1 Air Traffic Control (Atc)

 
Within the U.S.A., ATC will use the FAA Host Computer at the ARTCCs and eventually the Advanced Automation System (AAS) with its Area Control Computer Complex (ACCC) and its Automated En-Route Air Traffic Control (AERA) software as well as Tower Control Computer Complexes (TCCC). 

 
Air Traffic Control applications anticipated to be supported by data links by 1996 and beyond are listed below: 
 
 a. 
Assignment/Confirmation of Assigned Altitude 

b. 
Automated Airspace Alert 

c. 
Clearance Delivery 

d. 
Designated Traffic Report 

e. 
En-route Metering Advisory 

f. 
In-Flight Plan Filing and Amendment 

g. 
Minimum Safe Altitude 

h. 
Pre-departure Clearance Delivery 

i. 
Transfer of Communication 

j. 
Frequency Change 

k. 
Aircraft Estimated Trajectory 

l. 
Aircraft Estimated Trajectory (FMC/AERA Exchange) 

m. Arrival Identification and State 

n. 
Tactical Maneuver (FMC/AERA Exchange) 

o. 
TCAS/AERA Interface Message 

p. 
Trial Plan Probe 

q. 
Visual Flight Rule Flight Plan Activation/Following 

r. 
Local Landing Clearance 

s. 
Sequence to Land 

t. 
Situation Alerts: 

(1) ATC Contact Alert 

(2) Automatic, Ground Initiated Hazardous Weather 

(3) Emergency Landing Vectors 

(4) In-Flight Emergency; Safety 

(5) Military Interception Procedures 

(6) Out of Conformance Check 

(7) TCAS Sensitivity 

(8) VFR Terminal Area (including ARSA) Access 

(9) Hijack 


(10) In-Flight Emergency, Medical. 
 

## 1.3.1.2 Flight Information Services (Fis)

 
Flight Information Services (FIS) provided over a data link will use information from weather communications processors that provide alphanumeric and graphical weather data. FIS will also access data from terminal area equipment such as Terminal Doppler Weather Radar, Low Level Wind Shear Alert System, Airport Traffic Information System Workstation, and Automated Surface/Weather Observation Systems.  Data will also be accessed from national systems to include the Weather Message Switching Center, and the Centralized NOTAM Service Processor.  AMSS is an important transmission service for these applications. 

 
The following service applications eventually may use a data link: 
 
 a. 
Weather Reporting Applications 

(1) Hazardous Weather Advisory 

(2) Surface Observations 

(3) Radar Summary 

(4) Pilot Reports (PIREPs) 

(5) Terminal Forecast 

(6) Winds Aloft Forecast 

(7) Aviation Route Forecast 

(8) Notice to Airmen (NOTAM) 

(9) Hazardous Weather Graphic Map 


(10) Current Air Observations (PIREPS and Winds Aloft downlinked by 
the aircrew) 
 
 b. 
Terminal Area Applications 

(1) Airport Traffic Information Service (ATIS) 

(2) Current Position Information/Verification 

(3) Surface Winds 

(4) Traffic Information 

(5) Wind Shear Alert 
 
 c. 
Airport Applications 

(1) Control of Runway Lights 

(2) Runway Assignments 

(3) Local Landing Clearance 

(4) Parallel Runway Monitoring 

(5) Sequence to Land 

(6) Flow Management Advisory 

(7) Surface Traffic Monitoring and Control. 
 

## 1.3.1.3 Alerting Service

 
The objective of the Alerting Service is to notify appropriate organizations regarding aircraft in need of search and rescue, and to aid and assist such organizations as required. 

## 1.3.1.4 Automatic Dependent Surveillance (Ads)

 
Automatic Dependent Surveillance (ADS) is an important new ATC procedure based on the periodic reporting from aircraft of position, altitude and time derived from very accurate, high-integrity on-board navigation data (e.g., GPS).  The initial use of ADS is being planned for oceanic areas; future ADS operation is foreseen for domestic operations as well as oceanic and remote areas.  ADS messages will support both ATS and AOC requirements.  These messages will be transmitted over a data link via AMS(R)S or other media to user facilities at specific intervals, as negotiated or upon request. 

## 1.3.2 Aeronautical Operational Control (Aoc)

 
Like ATS, Aeronautical Operational Control (AOC) is a safety service defined in ICAO Annex 6, Part I, which gives the right and duty to exercise authority over the initiation, continuation, diversion or termination of a flight in the interest of the safety of aircraft, and the regularity and efficiency of a flight. 

In addition to packet data communications, data file transfers to support AOC needs such as data base updates, software changes, graphics, and facsimile will be accommodated by AMSS. 

## 1.3.2.1 Aoc Functions

 
AOC functions may directly accommodate dispatch and flight operations department functions, or may interface with other departments such as Engineering, Maintenance and Scheduling, in exercising or coordinating related functions.  Some examples of AOC functions are: 


a. 
Exceptional situation handling (aircraft/flight emergencies, hijack, etc.) 

b. 
Flight planning 

c. 
Weather information 

d. 
Airports/airways operational information (NOTAMS), etc. 

e. 
Movement control (flight departure, arrival, delay and diversion) 

f. 
Cockpit crew flight times/scheduling 

g. 
Aircraft engine monitoring 

h. 
In-flight maintenance problem reporting and solving 

i. 
Fuel consumption and requirements 

j. 
Aircraft scheduling (for particular flights) 

k. 
Schedule modifications (changes or cancellation of flights), etc. 
 
Systems (FMS), Digital Flight Data Acquisition Units (DFDAU).  Functions served would 
include FMS Operational Data Base update on flight plans, load and balance, weather, predeparture clearances, etc.; and DFDAU recording of and reporting on engine health monitoring, fuel flow/status requirements, etc. 

## 1.3.2.2 Operations Services

 
Aeronautical Operational Control uses data communications efficiently to operate flight programs supporting accurate and timely information, coordinating activities in the interests of passenger, baggage, cargo and mail; and to enhance flight safety, punctuality, and cost reduction.  AMSS will support AOC functions by providing worldwide, continuous services. 

 
Automated operations centers may have computer-based applications supporting: 
 
a. 
Schedule planning and adjustment 
 
 
b. 
Movement messages 
 
 
c. 
Aircraft assignment and reassignment 
 
 
d. 
Maintenance scheduling 
 
 
e. 
Crew control 
 
 
f. 
Weather monitoring 
 
 
g. 
Punctuality and regularity displays 
 
 
h. 
Reservations, departure control and maintenance systems 
 
 
i. 
Fuel monitoring 
 
 
j. 
Flight progress information systems 
 
 
k. 
Crew and aircraft flight-time/block-time accumulation 
 
 
l. 
Aircraft engine monitoring. 

## 1.3.3 Non-Safety Services 1.3.3.1 Aeronautical Administrative Communications (Aac)

 
AAC is a non-safety-related service that includes cabin provisioning and inventory, seat assignments, passenger travel arrangements, and baggage and parcel tracing. 

## 1.3.3.2 Aeronautical Passenger Communications (Apc)

 
APC is a non-safety-related service that includes voice telephone service for crew and passengers to connect with ground-based networks worldwide.  Data communications services also have been envisioned, including stock and commodity price quotes, current events, news, weather, and entertainment. 

## 1.4 Operational Goals

 
Four basic airspace environments are defined to provide background for AMSS goals: 
 
a. 
Oceanic/continental en route airspace with low traffic density (includes lowaltitude, offshore and remote areas). 


b. 
Continental airspace with high-density traffic. 
 
c. 
Oceanic airspace with high-density traffic. 
 
d. 
Terminal areas with high-density traffic. 
 
These environments differ in data and voice traffic volumes, urgency of access, requirements for end-to-end delays and established capabilities.  AMSS will provide greater reliability and integrated services in airspaces where they are effectively implemented. 

## 1.4.1 Global Coverage

 
The ultimate goal of AMSS is to provide the civil aviation community with worldwide, high-quality safety (ATS/AOC) and non-safety (AAC/APC) communication services from ground level to 21,350 meters (70,000 feet) and increased coverage for the polar areas. 

## 1.4.2 Compatibility And Interoperability

 
AMSS must be compatible and interoperable with external systems for all levels of users. This requires implementation of well-defined gateways and peer-to-peer protocols; therefore, AMSS must provide standard end-user subnetwork interfaces among satellite systems and associated terrestrial systems on a global basis.  For packet data transmissions, AMSS will implement the OSI Reference Model and will ultimately be integrated in the ATN. 

AMSS routing and addressing schemes must be compatible worldwide.  The twenty-four (24) bit International Civil Aviation Organization (ICAO) standard address will be implemented throughout AMSS to ensure compatibility between organizations and systems. The AES provides the chosen GES with its own identification in the form of the 24-bit ICAO aircraft identification code. 

When the ATN is operational, AMSS will be interoperable with Very High Frequency (VHF) and Mode Select (Mode-S) data links and will use procedures compatible with these systems. 

## 1.4.3 End-To-End Service Criteria

 
The criteria for AMSS service provided among end users of the system are contained in the RTCA document, Guidance on AMSS End-to-End System Performance and Verification Requirements (DO-215A). The criteria addressed in that document comprise the following. 
 
a. 
Overall service requirements, to ensure that technical characteristics and system integrity are consistent with the needs of safety communications, including those cases where other traffic may also be present. 
 
b. 
Overall availability requirements, to ensure the certainty and continuity required for safety communications. 
 
 
c. 
Other functional requirements necessary for safety services, including: 


(1) preemption control, to ensure that safety services have sufficient system 
resources available to them to meet their needs. 
 
 
(2) priority control, to permit higher-priority communications to proceed in 
preference over lower-priority communications. 
 
 
(3) automatic handover of AMSS aircraft communications between service 
providers, GESs, satellites and spot beams. 
 
 
(4) a log-in/log-out scheme for AES to/from the AMSS system that is identical 
for all combinations of satellites and service providers. 
 
 
(5) common procedures for establishment of ATS connections. 

## 1.5 Assumptions And Postulated Environment

 
To provide guidance and background for the development of specific operational requirements by users, the year 2010 airspace system environment was postulated and certain assumptions made regarding that future environment. 

## 1.5.1 Coverage

 
AMSS communications coverage depends on the location of the satellites in relation to the user aircraft.  Present satellites whose locations are specifically optimized for maritime traffic are being upgraded specifically for AMSS. These locations provide useful AMSS coverage over most of the globe except at the highest latitudes and, in some areas, provide dual-satellite coverage. 

## 1.5.2 Data And Voice Communications

 
Although voice communications will be used for the foreseeable future, as the capacity and precision capabilities of aeronautical data links become more apparent, routine air-groundair communications will evolve toward being computer-to-computer and, for many purposes, will be preferred.  Pilots and controllers will use digital data for many purposes but will continue to use voice communication for non-routine and unanticipated needs. 

 
Because of the beyond-line-of-sight and early cost characteristics of AMSS, initial use of satellite communications for ATS and AOC purposes has been concentrated in aircraft flying oceanic and remote-area routes.  As AMSS is the first such air/ground communications medium to support data, major advantage has been taken of that capability to make major strides in the advancement of data communications in ATS applications.  Simultaneously, the improved voice communications capability of AMSS, as compared with HF radio, has enhanced AOC usage and has enabled direct controller/pilot voice communications where previously not practicable in low-density airspace.  With continuing improvements in AMSS characteristics, and refinements of acceptance criteria for digital voice and data communications, it is expected that the applications of AMSS to ATS and AOC will expand. 

## 1.5.3 Safety

 
Safety communications, by ICAO and International Telecommunication Union (ITU) regulations, are assured of always having the highest priority and are accorded special measures for protection from interference.  A system supporting safety communications has appropriate priority and preemption control mechanisms embodied in all elements comprising the system. 
With the increasing use of data, voice operation will diminish, but it will always be available for use in emergency and other non-routine ATS situations.  AMSS safety services include ATS, which will extend current ATC services, and AOC, which will provide carriers with communications to enhance safety and regularity-of-flight operations. The initial application of AMSS in oceanic areas will provide improved communications, surveillance and procedures.  Among other benefits, this will lead to improved safety. 

## 1.5.4 Priority, Precedence And Preemption

 
The AMSS system, including AES and other subsystems, must have means for effecting the priority structure necessary for Aeronautical Mobile Satellite (Route) Service (AMS(R)S) safety services.  This includes the mechanisms for controlling the precedence of both safety and non-safety messages, for the preemption of system resources as needed to support AMS(R)S safety services and to provide for the added measure of protection to be accorded the safety services.  

## 1.5.5 Vocoder Qualifications

 
Through evaluations by the U.K. CAA (in 1988), the 9.6 kbps vocoder was deemed suitable for ATC operations in a non-dense airspace environment.  The 4.8 kbps vocoder was qualified (in August 1997) by direct comparative tests between mean opinion score and intelligibility of the original 9.6 kbps vocoder and the 4.8 kbps vocoder.  Based on the results of the 1997 tests, the 4.8 kbps vocoder was judged as statistically equivalent to the 9.6 kbps vocoder, and is thus suitable for operations in the same environment. 
 
NOTE: No conclusion was reached on the use of the 4.8 kbps vocoder in propeller 
aircraft, noting that: 
(1) the FAA Technical Center found that the speech signal-to-propeller-noise ratio used in the 1997 tests was inappropriately low; and 
 
 
(2) mitigating techniques (e.g., a noise-canceling microphone) were not used in 
the 1997 tests. 
 

## 1.6 Overview Of Test And Performance Verification Procedures

 
The test and performance verification procedures specified in this document are intended to be used as one means of demonstrating compliance with the performance requirements. Although specific test and performance verification procedures are cited, it is recognized that other methods may be preferred and may be used if they provide at least equivalent information.  In such cases, the procedures cited should be used as one criterion in evaluating the acceptability of the alternate procedures. 

 
The order of procedures specified suggests that the equipment be subjected to a succession of tests or analyses as it moves from design to design qualification and into operational use. 
Four types of procedures are specified in the following Sections. 

## 1.6.1 Environmental Tests And Performance Verification

 
Environmental test and/or analysis requirements are specified in Section 2.3.  The procedures and their associated limit requirements are intended to provide a laboratory means of determining the electrical and mechanical performance of the equipment under the environmental conditions expected to be encountered in actual operations. 
Unless otherwise specified, the environmental conditions and test procedures contained in RTCA/DO-160C, *Environmental Conditions and Test Procedures for Airborne Equipment*, will be used to demonstrate equipment compliance. 

## 1.6.2 Bench Tests And Performance Verification

 
Bench test and/or analysis procedures are specified in Section 2.4, and provide a laboratory means of demonstrating compliance with the requirements of Section 2.2.  Test results may be used by equipment manufacturers as design guidance for monitoring manufacturing compliance and, in certain cases, for obtaining formal approval of equipment design. 

## 1.6.3 Installed Equipment Tests And Performance Verification

 
The installed equipment test and/or analysis procedures and their associated limits are specified in Section 3.0.  Successful completion of bench and environmental test procedures is a precondition to completion of the installed equipment tests.  In certain instances, however, installed equipment tests may be used in lieu of bench test simulation of such factors as power supply characteristics, interference from or to other equipment installed on the aircraft, etc.  Installed-equipment tests are normally performed under two conditions: 

 
 
a. 
with the aircraft on the ground and using simulated or operational system inputs; 
 
b. 
with the aircraft in flight using operational system inputs appropriate to the equipment under test. 
 
 
Test results may be used to demonstrate functional performance in the intended operational environment. 

## 1.6.4 Operational Tests And Performance Verification

 
Operational tests and/or analyses are specified in Section 4.0.  These test procedures and their associated limits are intended to be conducted by operating personnel as one means of ensuring that the equipment is functioning properly and can be reliably used for its intended function(s). 

## 2.0 Equipment Performance Requirements And Test Procedures 2.1 General Requirements 2.1.1 Airworthiness

 
The design and manufacture of the equipment shall provide for an installation that does not impair the airworthiness of the aircraft. 

## 2.1.2 Intended Function

 
The equipment shall perform its intended function, as defined by the manufacturer, and its proper use shall not create a hazard to users of the NAS. 

## 2.1.3 Federal Communications Commission Rules

 
The equipment shall comply with all applicable rules of the Federal Communication Commission (FCC).1 

## 2.1.4 Fire Protection

 
All materials used shall be self-extinguishing except for small parts (such as knobs, fasteners, seals, grommets and small electrical parts) that would not contribute significantly to the propagation of a fire. 
 
 
NOTE: 
One means of showing compliance is contained in the Federal Aviation Regulations (FAR), Part 25, Appendix F. 

## 2.1.5 Operation Of Controls

 
The operation of controls intended for use during flight, in all possible combinations and sequences, shall not result in a condition detrimental to the continued performance of the equipment. Controls shall be designed to maximize operational suitability and minimize pilot workload. Reliance on pilot memory for operational procedures shall be minimized. 

## 2.1.6 Accessibility Of Controls

 
Controls that are not normally adjusted in flight shall not be readily accessible to flight personnel. Controls that are normally adjusted in flight shall be readily accessible and properly labeled as to their intended function. The controls shall be operable with the use of only one hand. 
 

## 2.1.7 Effects Of Tests

 
The equipment shall be designed so that the application of specified test procedures shall 
not be detrimental to equipment performance following the application of these tests, except as specifically allowed. 

## 2.1.8 Performance In A Shared Environment

 
All requirements for data integrity and timing should consider the effect of other active aircraft data links performing transfer operations in both directions at their nominal rates. 
It is strongly recommended that the AES receiver design take into account the existence and/or probable deployment of other mobile communications systems operating in the L- band. Because the power flux densities (both composite and per carrier) of such systems in the proximity of the AES may be very much higher than the power flux density of the wanted Aeronautical carriers, particular attention needs to be paid to the dynamic range of the AES receiver (to avoid saturation and consequent intermodulation products in the Aeronautical band), and to the provision of as much selectivity as possible, as near to the input port as possible in the receiver down-conversion process. 

## 2.2 Equipment Performance Requirements  **Standard Conditions**

Section 2.4 contains verification requirements and procedures for the performance requirements which follow.  Refer to Appendix C for a list which indexes all performance requirements sections and their corresponding verification requirements/procedures sections. 

## 2.2.1 Priority, Precedence And Preemption

 
The AES shall order the precedence of its transmissions in accordance with the requirements and associated priority structures for packet-mode and circuit-mode services contained in Sections 2.2.7.3 and 2.2.8.1, respectively. A message or call priority, when assigned by the initiating user terminal equipment in accordance with Tables 2-1 and 2-14, shall be 1) made available to the AES terminal management function and 2) transmitted to the GES and forwarded to the ground-based network management function. Similarly, the AES shall be capable of receiving the priority from the GES providing them to the AES terminal management function. 



In-process transmissions of lower priority shall be preempted immediately when necessary to support higher-level priority communications in accordance with the same sections, as appropriate. 
 
 
NOTE: 
When packet-mode operations are conducted using Data-2, packet priority, 
precedence and preemption are managed by a higher-layer entity. 
 

## 2.2.2 Aes Subsystem Definitions And Overall Requirements

 
The requirements of this document include those which apply generally to the overall AES, as described below, followed by those that are divided between the Antenna Subsystem and the Transceiver Subsystem. 

 
The Antenna Subsystem is defined to include those RF components from the physical aperture of the antenna(s) to a single antenna port where the interconnecting cable to the transceiver is to be attached; and related ancillary components; e.g., beam-steering units and RF relays, if present. 
The Transceiver Subsystem is defined to include the transmitter, receiver, and diplexer/LNA, if used. It interfaces at RF at the antenna port where it connects to the interconnecting cable, and with other on-board avionics equipment. 
Requirements for the Transceiver Subsystem are further divided into receiver Sections (2.2.4.1) and transmitter Sections (2.2.4.2). 
All AESs, as a minimum, shall have a Level 1 capability and shall continuously monitor the P channel after log-on to the GES, as defined in Section 1.2.3. 

## 2.2.2.1 Aes Effective Isotropic Radiated Power (Eirp) And Figure-Of-Merit

 
The AES system design parameters shall be selected to achieve the following Effective Isotropic Radiated Power (EIRP) (at full-rated AES output power) and Figure-of-Merit Gain/Temperature (G/T) minimum values.  For the high gain antenna (HGA) or intermediate gain antenna (IGA), this specification corresponds to the main beam for any pointing angle. 

 
Low Gain 
Intermediate Gain  
High Gain 
 
EIRP 
13.5 dBW 
12.5 dBW 
25.5 dBW 
 
G/T 
-26  dB/K 
-19   dB/K 
-13   dB/K 

 
Note 1: 
The G/T for an LGA can be as low as -28 dB/K for elevations greater than 70 
degrees. 
 
 
Note 2: 
The low gain antenna (LGA) G/T requirement is degraded by 1 dB to allow for 
increased-noise temperature because of its antenna pattern. 
The above values of G/T shall be achieved under the following conditions: 
a. 
A reference sky temperature of 100 K. 
b. 
Satellite elevation angles greater than or equal to five degrees, within the coverage volume of the aircraft antenna. 
c. 
Residual antenna pointing errors (including the effects of errors introduced by the antenna beam steering system). 
 
d. 
A reference temperature of 290 K. 
 
 
e.  
The transmitter power amplifier output at the maximum average RF power rating of the antenna. 


NOTE: 
The term "maximum average RF power rating" is defined as the maximum 
transmitter output power that the antenna subsystem is rated to accept. 
f. 
Include the loss and noise temperature contribution of a radome, where a radome is fitted. 
g. 
The operational RF environment, e.g., when the receive antenna is illuminated in its operating range (Section 2.2.4.1.7) by a total RF flux density of -100 dBW/m2. 
h. 
The RF cable connecting the antenna to the AES input is a 50 ohm coaxial cable with a maximum loss of 0.3 dB. 
Different values apply to systems operating with an LGA versus systems operating with an IGA or HGA.  These performance characteristics are met by virtue of the antenna specifications given in Section 2.2.3 and the receiver and transmitter specifications given in Sections 2.2.4.1 and 2.2.4.2, respectively. 

## 2.2.3 Antenna Subsystem Requirements

 
Antenna subsystems that have more than one antenna may have the performance specifications measured at more than one input/output port. 

## 2.2.3.1 General

 
These testable requirements apply to the high gain, intermediate gain, and low gain antenna subsystems.  These requirements are also to be met over the operating temperature range (per RTCA/DO-160C) of the AES antenna subsystem. 

## 2.2.3.1.1 Frequency Range

 
These requirements are to be met over the receive frequency range of 1530 to 1559 MHz and the transmit frequency range of 1626.5 to 1660.5 MHz. 

## 2.2.3.1.2 Polarization

 
The antennas shall be nominally right-hand (clockwise) circularly polarized (RHCP) in both the transmit and receive bands in accordance with the definition of International Radio Consultative Committee (CCIR) Recommendation 573 (i.e., an elliptically or circularly polarized wave in which the electric field vector, observed in any fixed plane that is normal to the direction of propagation while looking in the direction of propagation, rotates with time in a right-hand or clockwise direction). 

## 2.2.3.2 Antenna Gain And Coverage Volume 2.2.3.2.1 High Gain Antenna

 
The high-gain antenna subsystem gain, with reference to a right-hand circularly polarized isotropic source, shall be not less than +12 dBic over the complete coverage volume of the antenna subsystem.  The maximum gain shall not exceed +17 dBic. 

The antenna subsystem shall be capable of operation in a full-duplex mode.  The beam position control algorithm shall be independent of carrier frequency.  The antenna subsystem shall report its gain to the transceiver in the commanded direction with a resolution of 1 dB for AES transmit power control. 

 
The coverage volume, as declared by the antenna manufacturer, shall comprise not less than 75 percent of the solid angle of the upper hemisphere above five degrees elevation (to the horizon during normal cruise attitude of the aircraft).  The declared coverage volume shall include all effects of: (1) installation on a surface representative of the mounting surface on which it is intended to operate the antenna, (2) beam-pointing errors within the antenna subsystem including those due to implementation of the beam-steering algorithm, (3) effects of a radome and/or other protective surfaces, and (4) pattern discrimination. 
The remaining 25 percent shall be not less than 0 dBic. 
NOTE:   
Operation of an HGA as a low-gain antenna outside of the HGA's declared coverage volume necessitates compliance with this requirement.  It is intended that an AES operating at 600 and/or 1200 bps not be inhibited due to the gain or discrimination characteristics of an HGA. 
If it can be shown that the +12 dBic gain threshold is not a limiting factor, then the requirements of this section may defer to those of Section 2.2.2.1. 

## 2.2.3.2.2 Low Gain Antenna

 
The low-gain antenna subsystem gain, with reference to a right-hand circularly polarized isotropic source, shall be not less than 0 dBic when measured at the single antenna port over the complete coverage volume of the antenna, except as described below.  The maximum gain shall not exceed +5 dBic. 

 
The coverage volume as declared by the antenna manufacturer shall comprise not less than 85 percent of the solid angle of the upper hemisphere above five degrees elevation.  The declared coverage volume shall include all effects of:  (1) installation on a surface representative of the mounting surface on which it is intended to operate the antenna and (2) a radome and/or other protective surfaces.  The coverage volume may include a volume corresponding to a cone of 20 degrees half-angle at the aircraft zenith (when in normal cruise attitude) in straight and level flight.  The gain within this cone shall be not less than - 2 dBic.  The remaining 15 percent of the declared coverage volume shall be not less than - 5 dBic. 
 
 
If it can be shown that the 0 dBic gain threshold is not a limiting factor, then the requirements of this section may defer to those of Section 2.2.2.1.  

## 2.2.3.2.3 Intermediate Gain Antenna

The intermediate gain antenna subsystem gain, with reference to a right hand circularly polarized isotropic source, shall be not less than 6 dBic when measured at a single antenna port over the coverage volume of the antenna, except as described below.  The maximum gain shall not exceed 12 dBic. The antenna subsystem shall be capable of operation in full duplex mode.  The beam position control algorithm shall be independent of carrier frequency. The gain of the antenna subsystem in the commanded direction shall be reported to, or stored in, the transceiver.  The resolution of the antenna gain word shall be at least 1 dB for AES transmit power control. The coverage volume, as declared by the antenna manufacturer, shall comprise not less than 85 percent of the solid angle of the upper hemisphere above 5 degrees elevation (relative to the horizon during normal cruise attitude of the aircraft).  The declared coverage volume shall include all effects of:  (1) installation on a surface representative of the mounting surface on which it is intended to operate the antenna, (2) beam-pointing errors within the antenna subsystem including those due to implementation of the beamsteering algorithm, and (3) a radome and/or other protective surfaces. The declared coverage volume may include a volume corresponding to a cone of 20 degrees half-angle at the aircraft zenith in straight and level flight.  The gain within this cone must be not less than 4 dBic. The antenna gain shall be not less than 0 dBic for 99% of the solid angle above 5 degrees elevations. NOTE 1: 
Operation of an IGA as a low gain antenna outside of the IGA's declared coverage volume necessitates compliance with this requirement.  It is intended that an AES operating at 600 and/or 1200 bps not be inhibited due to gain characteristics of an IGA. 

 
NOTE 2: 
To the maximum extent possible, the antenna gain should be not less than 6 
dBic over 100% of the solid angle above 5 degrees elevation. 
 
If it can be shown that the +6 dBic gain threshold is not a limiting factor, then all the requirements of this section may defer to those of Section 2.2.2.1. 

## 2.2.3.3 Axial Ratio 2.2.3.3.1 High Gain And Intermediate Gain Antenna

 
The AES antenna shall either have an axial ratio not exceeding 6 dB over the declared coverage volume, or else shall have sufficient gain to compensate for excess polarization losses caused by an axial ratio greater than 6 dB.  To calculate the gain compensation required, the satellite antenna axial ratio is assumed to be 2.5 dB with the major axes of the polarization ellipses orthogonal. 

## 2.2.3.3.2 Low Gain Antenna

 
The AES antenna shall either have an axial ratio not exceeding 6 dB for elevations from 45º to 90º and not exceeding 20 dB over the remainder of the declared coverage volume, or else shall have sufficient gain to compensate for excess polarization losses caused by greater axial ratios in the respective regions of the coverage volume.  To calculate the gain compensation required, the satellite antenna axial ratio is assumed to be 2.5 dB with the major axes of the polarization ellipses orthogonal. 

 
 
NOTE: 
The AES antenna axial ratio should not exceed 6 dB. 

## 2.2.3.4 Pattern Discrimination 2.2.3.4.1 High Gain Antenna

 
The radiation pattern shall discriminate by not less than 13 dB between wanted and unwanted satellite positions over the declared coverage volume and not less than 5 dB outside the declared coverage volume. This assumes that:  (1) satellites are in geostationary orbit, (2) unwanted satellites are not less than 45 degrees longitude away from the wanted satellite, and (3) the aircraft is in a straight and level attitude. 

 
 
NOTE: 
See Note of Section 2.2.3.2.1.  

## 2.2.3.4.2 Intermediate Gain Antenna 2.2.3.4.2.1 Intermediate Gain Antenna -- Pattern Discrimination

 
The radiation pattern shall discriminate by not less than 7 dB between wanted and 85% of unwanted satellite positions for all antenna steering angles above 5 degrees elevation. This assumes that (1) satellites are in geostationary orbits, (2) unwanted satellites are not less than 80 degrees longitude away from the wanted satellite, and (3) the aircraft is in straight and level flight. 

## 

This requirement shall be independent of the coverage volume declared by the antenna manufacturer described in Section 2.2.3.2.3.  

## 2.2.3.4.2.2 Intermediate Gain Antenna -- Eirp Discrimination

Within the transmit frequency range described in Section 2.2.3.1.1, the radiation pattern shall be such that the EIRP gain in any direction shall not exceed that in the direction of the wanted satellite by more than 5 dB over 95% of the antenna steering angles above 5 degrees elevation. 

## 2.2.3.5 Voltage Standing Wave Ratio (Vswr)

 
When measured at the single RF port of the antenna, the Voltage Standing Wave Ratio (VSWR) shall not exceed 1.5:1 when correctly mated with the appropriate connector for any selected beam.  The nominal characteristic impedance shall be 50 ohms. 

## 2.2.3.6 Phase Discontinuity 2.2.3.6.1 High Gain Antenna

 
When switching adjacent beams in a switched beam antenna, the signal phase, over the receive and transmit frequency ranges shall not change by more than: 
a. 
Eight degrees for a minimum of 90 percent of all combinations of adjacent beams. 
b. 
12 degrees for a minimum of 99 percent of all combinations of adjacent beams. 
c. 
For multiple array antennas, this specification applies only to individual array performance, not the combined system. 
 
 
NOTE: 
Adjacent beams are defined as beams which have the minimum spatial 
separation in a given direction and whose corresponding phase shifter states differ for at least one element.  

## 2.2.3.6.2 Intermediate Gain Antenna

 
When switching adjacent beams in a switched beam antenna, the signal phase, of the receive and transmit frequency ranges, shall not change by more than 30 degrees for a minimum of 99% of all combinations of adjacent beams. 

 
For multiple array antennas, this specification applies only to individual array performance, not the combined system. 

 
 NOTE: 
Adjacent beams are defined as beams which have the minimum spatial separation in a given direction and whose corresponding phase shifter states differ for at least one element. 

 

## 2.2.3.7 Antenna Switching Time

 
Where more than one antenna is used to meet the coverage requirements, the signal shall be 
interrupted by no more than 40 milliseconds (ms) when switching between antennas. 

## 2.2.3.8 Beam Switching Time

 
For a switched-beam antenna, the signal shall be interrupted for no longer than 50 microseconds when switching between any adjacent beams within the same array. 

## 2.2.3.9 Pointing Response Time

 
The antenna shall point to the commanded direction to within 0.5 dB of its final gain value within six seconds from any initial condition. 
 
 
NOTE: 
For an electronically steered antenna, this requirement may be demonstrated 
through analysis. 

## 2.2.3.10 Power Handling

 
The antenna shall operate within all single-carrier specifications with the carrier having power equal to the maximum average RF power rating of the antenna in the transmit band at maximum operational altitude. 

 
 
NOTES: 1. 
The term "maximum average RF power rating" is defined as the maximum transmitter output power that the antenna subsystem is rated to accept. 
 
 
2. 
There may be in excess of 200 W peak envelope power when multiple 
carriers are used. 

## 2.2.3.11 Carrier To Multipath Discrimination -- High Gain Antenna And Intermediate Gain Antenna

 
With the aircraft in horizontal flight over sea in median sea condition (see note below), the AES antenna shall attenuate the reflected signal from the sea surface relative to the main signal in the direction of the satellite, so as to achieve a minimum C/M of 10 dB at 5o elevation and 12 dB at 20o elevation. 

 
 
NOTE: 
The C/M over median sea (C/Mmed) is defined on the basis of the C/M for rough 
sea (C/Mrough corresponding to sea states with Beaufort Number 3 or higher) and on the C/M for smooth sea (C/Msmooth corresponding to the sea state with Beaufort Number 0), by C/Mmed = (0.3 x C/Msmooth) + (0.7 x C/Mrough) (all values in 
dB). 

## 2.2.3.12 Antenna Intermodulation In The Receive Band

 
For multicarrier operation, when operating with two unmodulated carriers 4 MHz apart anywhere within the transmit frequency band specified in Section 2.2.3.1.1 and each one 
having half the maximum multicarrier average RF power rating of the antenna, the antenna shall not generate intermodulation products in the receive band greater than -162 dBW. 

 
 
NOTE: 
For carriers 10 MHz apart, the antenna should not generate intermodulation 
products in the receive band greater than -164 dBW. 

## 2.2.3.13 Radiated Antenna Intermodulation Products

 
For multi-carrier operation, when operating with two unmodulated carriers anywhere within the transmit frequency band specified in Section 2.2.3.1.1 and each having half the maximum multi-carrier average RF power rating of the antenna, the antenna subsystem shall not radiate internally generated intermodulation products in a direction toward a likely location(s) of a GNSS antenna(s) on the same aircraft so as to cause a power level exceeding -115 dBm for any discrete seventh- and higher-order product, referenced to the GNSS antenna port.  In this condition, the GNSS antenna is taken to be a quarter-wave monopole antenna matched to its load, and the isolation between the AES antenna port and the GNSS antenna port is taken to be 40 dB. 

 
 
NOTE: 
The term "maximum multicarrier average RF power rating" is defined as the maximum multicarrier average RF power for which the AES antenna subsystem 
is qualified to all other requirements in this document. 

## 2.2.4 Satellite Subnetwork Physical Layer Requirements 2.2.4.1 Receiver Requirements

 
For the purposes of this section, the receiver is composed of all the AES equipment's RF receiving systems and circuits and digital signal processing circuits from the AES antenna port (L-band) to the physical layer output to the link layer.  The antenna coaxial cable between the antenna and receiver is not included.  The characteristics of the cable are specified in Section 2.2.2.1 (h).  These requirements shall be met over the receive frequency range of Section 2.2.4.1.7. 

## 2.2.4.1.1 Channel Rates

 
The channel rates for the various receive channel types shall be as follows: 


Channel Rates  
 
Receiver Channel  
   Channel 


    (kbps)  


Types 
 
 
Spacing (kHz) 
  0.6 
P (Data) 
   5 
 
  1.2 
P (Data) 
   5 
 
10.5 
P (Data) 
10/7.5 
 
  8.4 
C (Voice) 
  7.5 
 
21.0 
C (Voice) 
 17.5 
 

## 2.2.4.1.2 Receiver Sensitivity

 
The following maximum signal levels from a modulated signal source at room temperature 
(25 C) for the channel rates shown shall produce the required Bit Error Rate (BER) or better: 



Maximum Signal Power to 
 
Channel Rate/  

     Produce BER = 10-5 or Better 
 
Modulation 


Ambient Temp.  
Ambient Temp. 
 
(kbps) 


25 C 
 
 
70 C 
0.6 A-BPSK 

  -140.2 dBm 
 
  -139.9 dBm 
 
1.2 A-BPSK 

  -137.1 dBm 
 
  -136.8 dBm 
 
10.5 A-QPSK (7.5 kHz spacing)  

  -128.8 dBm 
 
  -128.5 dBm 
 
10.5 A-QPSK (10 kHz spacing)  

  -129.2 dBm 
 
  -128.9 dBm 


Maximum Signal Power to 
 
Channel Rate/  

      Produce BER = 10-3 or Better: 
 
Modulation 


Ambient Temp.  
Ambient Temp. 
 
(kbps) 

      25 C  
 
      70 C 
8.4 A-QPSK 

 -130.9 dBm 
 
  -130.6 dBm 
 
21.0 A-QPSK  

 -127.9 dBm 
 
  -127.6 dBm 

 
NOTE: 
With a signal source at room temperature (25 C = 298 K), the system under test has the following noise temperature and noise power density (N0): 


   System Under Test  
  Noise Power 


Receiver Temp.  
Max Noise Temperature 
  Density (N0) 


T  25 C  

 451 K 
 
 
-172.1 dBm/Hz 


25 C < T  

 483 K 
 
 
-171.8 dBm/Hz 

## 2.2.4.1.2.1 Adjacent Channel Rejection

 
The receiver sensitivity requirements of Section 2.2.4.1.2 shall be met in the presence of two similar adjacent interfering carriers, each of 5 dB higher power than the wanted carrier, one on either side of the wanted carrier and at their nominal channel separation from it. 

## 2.2.4.1.2.2 Isolation From Transmitter

 
The receiver sensitivity specifications of Section 2.2.4.1.2 shall be met while the transmitter is operating at its maximum rated average output power. 
 

## 2.2.4.1.2.3 Phase Noise

 
The receiver sensitivity specifications of Section 2.2.4.1.2 shall be met with phase noise on 
the desired test signal as shown in Figure 1 of Reference Document "B". 

## 2.2.4.1.2.4 Combined Performance

 
It shall be shown, either by test or by analysis, that the receiver sensitivity specified in Section 2.2.4.1.2 is met when all of the conditions in Sections 2.2.4.1.2.1 through 2.2.4.1.2.3 are applied concurrently. 

## 2.2.4.1.3 Rejection Of Signals In The Aes Receive Band

 
The performance defined in Section 2.2.4.1.2 shall be achieved when a CW interfering signal is present at the AES receiver input at a level of -72 dBm at any frequency in the range 1530 to 1559 MHz, excluding the desired signal by + 1 MHz. 

## 2.2.4.1.4 Rejection Of Signals Outside The Aes Receive Band

 
The performance defined in Section 2.2.4.1.2 shall be achieved when a CW interfering signal is present at the AES receiver input at a level of +3 dBm at any frequency in the ranges 470 to 1450 MHz and 1660.5 to 18000 MHz; and at amplitudes decreasing linearly in decibels from +3 dBm at 1450 MHz to -72 dBm at 1530 MHz and increasing linearly in decibels from -72 dBm at 1559 MHz to +3 dBm at 1626.5 MHz. 

 
 
NOTE: 
The range 1626.5 to 1660.5 MHz is covered in Section 2.2.4.1.2.2. 

## 2.2.4.1.5 Receiver Linearity

 
The receiver sensitivity requirements of Section 2.2.4.1.2 shall be met while wide band noise is applied over the entire receive band as defined in Section 2.2.4.1.7.1 except for a notch in the noise spectrum in which a desired test channel can be operated. 

 
The power level of the wideband noise spectrum applied to the AES receiver shall be equivalent to the power delivered to the AES by an antenna subjected to a power flux density of -100 dBW/m2 distributed uniformly over the entire receive band defined in Section 2.2.4.1.7.1.  The noise level applied to the transceiver input port shall be as follows for either a High Gain Antenna (HGA), Intermediate Gain Antenna (IGA) or a Low Gain Antenna (LGA), depending upon which system the receiver will use in operation.  The 
added noise density from a LGA (0 dBic gain) is N0 = -170.8 dBm/Hz, the noise density from an IGA (6 dBic gain) is N0 = -164.8 dBm/Hz and the noise density from a HGA (12 dBic gain) is N0 = -158.8 dBm/Hz at the AES receiver input (taking 0.3 dB antenna cable 
loss into account). 

## 2.2.4.1.6 Desired Signal Dynamic Range

 
The P-channel receiver shall be capable of operating with signal levels from the maximum levels given in Section 2.2.4.1.2 to 22 dB above these levels. 
 
The C-channel receiver shall be capable of operating with signal levels from the maximum levels given in Section 2.2.4.1.2 to 15 dB above these levels. 

## 2.2.4.1.7 Receiver Tuning 2.2.4.1.7.1 Tuning Range And Channel Increments

 
The receiver shall tune within the frequency range 1530-1559 MHz in 2.5 kHz increments. 

## 2.2.4.1.7.2 Channel Numbering

 
The receiver shall be tuned to channels by commands based on the channel number CRx, derived as follows: 


frequency of reception (MHz) - 1510.0 


CRx =  

 0.0025 

## 2.2.4.1.8 Capture Range

 
The receiver shall be capable of acquiring and maintaining a lock to signals with a frequency offset from nominal of +2.180 kHz, minimum. 
 
 
NOTE: 
It may be required that Doppler correction be functionally disabled during Tuning Range & Channel Spacing and possibly other requirements testing. 

## 2.2.4.1.9 Doppler Rate

 
The receiver shall be capable of acquiring and maintaining performance per Section 2.2.4.1.11.1 with a frequency change rate of 30 Hz/s within the entire range of Doppler correction and meeting the requirements of Section 2.2.4.1.8 and if C-channel equipped, Section 2.2.4.1.12.1. 

## 2.2.4.1.10 Phase Discontinuity

 
The receiver shall be capable of maintaining performance per the Gaussian test conditions of Sections 2.2.4.1.11.1 and 2.2.4.1.12.1 with a 12-degree, except 30 degrees for IGA systems, phase discontinuity occurring once per second (reference Section 2.2.3.6). 

 

## Note: Performance Of Iga Channels Is Enhanced By The Channel Format Used. 2.2.4.1.11 P-Channel Configuration And Receiver Requirements

 
The P-channel configuration and receiver requirements shall be the minima specified for the AES in Reference Document "A", Section 3.1, Section 3.3.1, and Section 3.4, including all referenced tables, figures, annexes and appendices applicable to the AES.  These are identified in the following listing. 
 
 
Reference Document "A", Section 3.0: 



3.1  
Channel Configuration - General 
 
 
3.3.1  
P-Channel Characteristics 


Scrambler 


Forward Error Correction (FEC) Encoder 


Interleaver 


Timing (Unique Word) 


Modulator 
 
 
3.3.1.1 
P-Channel Frame Duration 
 
 
3.3.1.2 
P-Channel Frame Format 
 
 
3.3.1.3 
NOT APPLICABLE (Low-Power P-Channel) 
 
 
3.4  
Interleaver 

## 2.2.4.1.11.1 Bit Error Rate Performance

 
The Bit Error Rate (BER) of the P-channel demodulator, including the de-interleaver, Forward Error Correction decoder and descrambler, shall be not greater than 10-5 for the channel rates and conditions specified below.  The BER performance shall be achieved in the presence of channel degradations as specified in Sections 2.2.4.1.2.1 and 2.2.4.1.2.3; also, in the presence of a received-clock offset of one part in 106; and, for the Additive White Gaussian Noise (AWGN) channel conditions, with the phase discontinuity specified in Section 2.2.4.1.10. 

## 

 
Bit Error Rate Performance 
 
Channel 
Rician 
Fading 
C/N0 
Rate/Modulation 
Bandwidth 
(dBHz) 
Fading 
C/M (dB) 
(kbps) 
(Hz) 
0.6 A-BPSK 
31.9 
NO 
Infinity 
N/A 
 
32.9 
YES 
12 
20, 60 and 100 
 
35.0 
YES 
7 
20, 60 and 100 
1.2 A-BPSK 
35.0 
NO 
Infinity 
N/A 
 
36.0 
YES 
12 
20, 60 and 100 
 
38.1 
YES 
7 
20, 60 and 100 
10.5 A-QPSK 
43.3 
NO 
Infinity 
N/A 
(7.5 kHz spacing) 
44.7 
YES 
12 
20, 60 and 100 
 
46.0 
YES 
10 
20, 60 and 100 
10.5 A-QPSK 
42.9 
NO 
Infinity 
N/A 
(10 kHz spacing) 
44.3 
YES 
12 
20, 60 and 100 
 
45.6 
YES 
10 
20, 60 and 100 

## 2.2.4.1.11.2 Time To Acquire Superframe Lock

 
Following receipt of a tuning command, the P-channel demodulator shall achieve superframe lock within the period of time and under Gaussian channel conditions and the conditions specified below, with a probability of at least 99%.  The AES shall provide external indications of superframe lock suitable for measuring the acquisition time. 

 

|                   | Time to Acquire Superframe Lock    |
|-------------------|------------------------------------|
|                   |                                    |
| C/N               |                                    |
| 0                 |                                    |
|                   |                                    |
| (dBHz)            |                                    |
| Channel Rate/     |                                    |
| Modulation        |                                    |
| (kbps)            |                                    |
| Frequency         |                                    |
| Offset            |                                    |
| (Hz)              |                                    |
| Time to           |                                    |
| Acquire           |                                    |
| Super             |                                    |
| Frame Lock        |                                    |
| 0.6  A-BPSK       | 10 sec                             |
|                  |                                    |
| 2180              |                                    |
| 1.2  A-BPSK       | 10 sec                             |
|                  |                                    |
| 2180              |                                    |
| 10 sec            | 43.3                               |
|                  |                                    |
| 2180              |                                    |
| 10.5  A-QPSK      |                                    |
| (7.5 kHz spacing) |                                    |
| 10 sec            | 42.9                               |
|                  |                                    |
| 2180              |                                    |
| 10.5  A-QPSK      |                                    |
| (10 kHz spacing)  |                                    |

## 2.2.4.1.12 C-Channel Configuration And Receiver Requirements

 
The C-channel configuration and receiver requirements (including those in common with the transmitter) shall be the minima specified for the AES in Reference Document "A", Sections 3.1, 3.2 and 3.4, including all referenced tables, figures, annexes and appendices applicable to the AES.  These are identified in the following listing. 

 
 
Reference Document "A", Section 3.0: 
 
3.1  
Channel Configuration - General 
 
 
3.2  
C-Channel Configuration 
 
 
3.2.1  
C-Channel Modulation 
 
 
3.2.2  
C-Channel Frame 
 
 
3.2.3  
Scrambler 
 
 
3.2.4  
FEC Coding 
 
 
3.2.5  
Bit Interleaving 
 
 
3.2.6  
Sub-band Signaling Channel 
 
 
3.2.7  
Preamble Structure 
 
 
3.4  
Interleaver 
 

## 2.2.4.1.12.1 Bit Error Rate Requirements 2.2.4.1.12.1.1 Circuit-Mode Voice Requirements

 
The BER, as measured at the C-channel demodulator, Forward Error Correction (FEC) decoder and de-interleaver, where present, shall not be greater than 10-3 for channel rates and modulations as follows. 



C-channel BER Performance 


 Channel Rate/  
FEC  
 C/N0  
Rician 
C/M  
Fading 
 
 
Modulation Rate 
Rate  
(dBHz) 
Fading 
(dB)  
Bandwidth 

      (kbps)  


Present 
 
 
(Hz) 
 
8.4 A-QPSK 
 
2/3  
41.7  
No  
Inf.  
N/A 


43.9  
Yes  
12  
20, 60 and 100 


46.2  
Yes  
10  
20, 60 and 100 
 
21.0 A-QPSK 
 
1/2  
44.2  
No  
Inf.  
N/A 


46.0  
Yes  
12  
20, 60 and 100 


48.6  
Yes  
10  
20, 60 and 100 

 
The above BER performance shall be achieved in the presence of channel degradations as specified in Sections 2.2.4.1.2.1 and 2.2.4.1.2.3; also, in the presence of a received clock offset of one part in 106; and, for the Gaussian channel conditions, with the phase discontinuity specified in Section 2.2.4.1.10. 

## 2.2.4.1.12.2 Bit-Timing Recovery - Frequency Uncertainty

 
The C-channel demodulator shall be capable of receiving carrier bursts with a burst-toburst uncertainty of 30 Hz plus any uncertainty caused by uncompensated Doppler shift due to aircraft motion. 

## 2.2.4.1.12.3 Frame Lock Acquisition And False Frame Lock Probabilities

 
Under the conditions of (1) a Gaussian channel, (2) phase noise per Figure 1 of Reference Document "B", (3) a burst-to-burst frequency uncertainty of 30 Hz, and (4) the presence of two similar adjacent interfering carriers, each 5 dB higher than the wanted carrier, one on either side of the wanted carrier and at their nominal channel separation from it, the following probabilities exist. 
a. 
The probability of failure to acquire frame lock on the first Unique Word shall be less than: 
 
1 in 103 for 8.4 kbps at C/N0=43.3 dBHz.  
 
 
1 in 103 for 21.0 kbps at C/N0=43.2 dBHz.  
 
 
1 in 104 for 21.0 kbps at C/N0=44.4 dBHz. 
 
 
b. 
The probability of false frame lock shall be less than: 
 
1 in 104 for 8.4 kbps at C/N0=43.3 dBHz.  
 
 
1 in 105 for 21.0 kbps at C/N0=43.2 dBHz. 
c. 
Should frame lock be lost, it shall be re-acquired within 3.0 seconds, at a C/N0 = 43.2 
dBHz for the 21.0 kbps channel rate. 

## 2.2.4.1.12.4 Maintaining Bit Synchronization

 
The C-channel demodulator shall maintain bit synchronization in a Gaussian channel at a C/N0=43.2 dBHz for a 21 kbps channel rate and at a C/N0=39.2 dBHz for a 8.4 kbps channel rate. 

## 2.2.4.1.12.5 Channel Bit Error Rate (Ber) Measurement And Accuracy

 
The average channel BER (before decoding) shall be measured by a built-in BER counter. The reported value is the average number of bit errors, rounded to the next higher integer, occurring in 2560 received channel bits. The estimation shall be derived using at least 21,000 received channel bits or the BER report shall be indicated as being "*invalid*". 



NOTE: 
The channel BER estimation is used for forward link power control and signal 
degradation measurements. 

## 2.2.4.2 Transmitter Requirements

 
For the purposes of this section, the transmitter is composed of all the AES equipment's RF systems and circuits between the baseband input and the output port to the antenna subsystem (L-band).  The antenna coaxial cable is not included.  This cable is specified in Section 2.2.2.1 h.  These requirements shall be met over the transmit frequency range of Section 2.2.4.2.10. 

## 2.2.4.2.1 Channel Rates And Tolerances

 
The channel rates for the various transmit channel types shall be as follows: 

 Transmit Channel Types and Rates 

 
    Channel Rates 
Channel Types  
 
Channel   
Channel Rate 
 
         (kbps) 
 
From Aircraft 
 
 
Spacing 
 
Tolerances 
 
0.6  
 
R, T (Data) 
 
 
2.5 kHz 
 
100.0 ppm 
 
 
1.2  
 
R, T (Data) 
 
 
2.5 kHz 
 
100.0 ppm 
 
 
8.4  
 
C (Voice)  
 
 
5    kHz 
 
59.5 ppm 
 
 
10.5  
 
R, T (Data) 
 
    
10/7.5 kHz 
47.6 ppm 
 
 
21.0  
 
C (Voice)  
 
 
17.5 kHz  
47.6 ppm 
 

 
NOTE: 
The channel rate tolerance should be achieved without requiring manual adjustment more often than once per six months, although automatic 
adjustments may be made as required. 

## 2.2.4.2.2 Output Power

 
When commanded to maximum output with one or more unmodulated carriers, the total transmitter maximum average output power shall be 24 watts minimum and no more than 60 watts into a 50 + j0 ohm load.  When in multi-carrier operation, the transmitter's total average output power shall not exceed a level at which the intermodulation product contribution exceeds the values of Section 2.2.4.2.6. 

 
NOTES: 
1. 
The minimum transmitter output power of 24 Watts (13.8 dBW) specified in this 
section satisfies the Aero-H system requirement for a minimum EIRP of 25.5 dBW (specified in Section 2.2.2.1) when the maximum antenna RF cable loss (0.3 dB) specified in Section 2.2.2.1 (h) and the minimum High Gain Antenna (HGA) gain (12 dBic) specified in Section 2.2.3.2.1 are taken into account. 
 
2. 
The minimum transmitter output power of 24 Watts (13.8 dBW) specified in this 
section satisfies the Aero-L system requirement for a minimum EIRP of 13.5 dBW (specified in Section 2.2.2.1) when the maximum antenna RF cable loss (0.3 dB) specified in Section 2.2.2.1 (h) and the minimum Low Gain Antenna (LGA) gain (0 dBic) specified in Section 2.2.3.2.2 are taken into account. 
 
3. 
The maximum transmitter output power of 60 Watts (17.8 dBW) reflects the case of an 
HPA as specified in ARINC Characteristic 741 that is outputting the maximum allowed output power of 80 Watts (19.0 dBW) with an assumed minimum combined RF cable and diplexer loss of 1.25 dB. 

## 2.2.4.2.3 Output Power Adjustment

 
When using a linear high power amplifier, the transmitter output power shall be adjustable by command to reduce output power by at least 30 dB in a minimum of 30 steps.  A minimum of 15 steps, resulting in at least 15 dB reduction, shall be applicable to carriers on an individual basis. 
When using a non-linear (Class C) high power amplifier, the transmitter output power shall be adjustable by command to reduce output power by at least 15 dB in a minimum of 15 steps. 
Each power reduction step shall be 1 dB nominal, 0.5 dB minimum to 1.5 dB maximum. 
The output power shall be adjusted inversely as a function of the reported gain of a high gain antenna as specified in Section 2.2.3.2.1. 
 

## 2.2.4.2.4 Output Power Stability

 
The transmitter output power per carrier shall not vary from the value resulting from the GES-originated EIRP command and reported antenna gain by more than 1 dB.  For R and T channels, this stability shall be maintained until log-off or loss of the P data channel (Pd); 
for C-channels, this stability shall be maintained for 30 minutes. 

## 2.2.4.2.5 Harmonics, Discrete Spurious And Noise Density

 
While transmitting a single modulated signal at the maximum-rated average output power at any frequency per Section 2.2.4.2.10, the composite harmonic, discrete spurious and noise density (including phase noise), at the transmitter output shall not exceed the following; 

## Composite Harmonic, Discrete Spurious And Noise Density Levels



Frequency (MHz) 
 
 
Power Density 


0.01 to 15251 


- 135 dBc/4 kHz 


1525 to 1559 


- 203 dBc/4 kHz 


1559 to 1585 


- 155 dBc/1 MHz 


1585 to 1605 


- 143 dBc/1 MHz 


1605 to 1610 


- 117 dBc/1 MHz 


1610 to 1614 


-  95 dBc/1 MHz 


1614 to 1660 


-  55 dBc/4 kHz2, 3 


1660 to 1670 


-  55 dBc/20 kHz2, 3 


1670 to 1735 


-  55 dBc/4 kHz 


1735 to 12000  
 
 
- 105 dBc/4 kHz 


12000 to 18000  
 
 
-  70 dBc/4 kHz 



TABLE NOTES: 
 
1. 
AMSS operations are permitted in the MMS (maritime) band which 
has been extended to include 1525-1530 MHz. 
2. 
Within the transmit band, excluding the frequency band within + 35 kHz of the carrier. 
3. 
The -55 dBc/4kHz spectrum level in this table is equivalent to -55 - 10 
log10(4000/SR) dBe (relative to the maximum envelope) under the 
definitions in Section 2.2.4.2.16. 
NOTES: 
1. 
The band 1559 to 1610 MHz is allocated to the Aeronautical Radionavigation Service (ARNS) and Radionavigation Satellite Service (RNSS), and is currently utilized by GPS, GLONASS and 
related augmentation systems, along with guard bands at the edges. Future systems developing in these services (e.g., other ARNS/RNSS systems, augmentation systems) may require the establishment of more stringent protection levels. 

 
2. 
Protection levels required for (and from) other developing aeronautical CNS systems (e.g., next-generation AMS(R)S) have not yet been determined, but are likely to be more stringent. 
3. 
The Radio Astronomy (RA) Service operates in the frequency bands 1610.6-1613.8 MHz and 1660.0-1670.0 MHz.  The composite harmonic, discrete spurious and noise density levels listed above are, alone, insufficient to protect the RA Service to the requirements of ITU RA.769-1. 

## 2.2.4.2.6 Intermodulation Products

 
In systems having multi-carrier capability, while transmitting two equal unmodulated carriers, with total power level up to the Maximum Allowable Multi-carrier Average Output Power of the transmitter, the power level of each intermodulation product shall not exceed the following: 


  Maximum Intermodulation Product Levels 
 
Frequency (MHz) 
 
3rd/5th Order 
 
7th and Higher Orders 
 
below 15251 

N/A  


-114  dBc 
 
 
1525 to 1559 

N/A  


-154  dBc 
 
 
1559 to 1585 

N/A  


-134  dBc 
 
 
1585 to 1605 

N/A  


-117  dBc 
 
 
1605 to 1610 

N/A  


- 91  dBc 
 
 
1610 to 1614 

-64  dBc  
 
 
- 72  dBc 
 
 
1614 to 1691 

-24  dBc  
 
 
- 32  dBc 
 
 
1691 to 1711 

-24  dBc  
 
 
- 29  dBc 
 
 
1711 to 1735 

N/A  


- 34  dBc 
 
 
1735 to 12000  

N/A  


- 84  dBc 
 
 
12000 to 18000  

N/A  


- 84  dBc 



TABLE NOTE: 
 
1. 
AMSS operations are permitted in the MMS (maritime) band which has been extended to include 1525-1530 MHz. 
The transceiver shall not transmit on a newly-assigned frequency that would produce a fifth-order intermodulation product at a frequency below 1610.0 MHz. 
 

## Notes:

 
1. 
The Ground Earth Station (GES) should not assign to an AES any 
combination of frequencies which would cause the AES to inhibit transmission. 
2. 
The band 1559 to 1610 MHz is allocated to the Aeronautical Radionavigation Service (ARNS) and Radionavigation Satellite Service (RNSS), and is currently utilized by GPS, GLONASS and related augmentation systems, along with guard bands at the edges. Future systems developing in these services (e.g., other ARNS/RNSS systems, augmentation systems) may require the establishment of more stringent protection levels. 
 
 
3. 
Protection levels required for (and from) other developing aeronautical CNS systems (e.g., next-generation AMS(R)S) have not yet been determined, but are likely to be more stringent. 
4. 
The Radio Astronomy (RA) Service operates in the frequency bands 1610.6-1613.8 MHz and 1660.0-1670.0 MHz.  The composite harmonic, discrete spurious and noise density levels listed above are, alone, insufficient to protect the RA Service to the requirements of ITU RA.769-1. 

## 2.2.4.2.7 Carrier Off Level

 
The transmitter output power when all carriers are commanded off shall be less than -41.5 dBW. 

## 2.2.4.2.8 Transmitter/Channel Muting

 
An AES shall mute either specific channels (in the case of multiple channel capability) or 
the entire transmitter, as specified below, under the stated conditions:  

 
a. 
Oscillator out-of-lock: An AES shall not transmit in the case of an out-of-lock condition in any oscillator in the transmit path. 
b. 
Loss of GES control: An AES shall not transmit in the following conditions: 
 
i. 
On an R-channel unless it is frame locked on a received P-channel. Frame lock shall be declared when the position within the frame is known. The false frame lock probability shall be less than 10-5. Loss of frame lock shall be declared when, after being successfully frame locked to a P-channel, N or more successive incorrect unique words are detected, where N is 4 for 600 bps, 8 for 1200 bps, and 16 for all other P-channel bit rates. 
 
 
ii. 
On a T-channel unless it is superframe locked on a received P-channel. Superframe lock shall be declared when frame lock is declared and the frame number is known. 
 
iii. 
On a C-channel unless it is successfully receiving the corresponding ground-toair C-channel with a bit error rate less than 10-3, with no interval of more than 40 seconds in which this rate is exceeded. 
 
 
NOTE: 
A minimum system configuration with C-channel capability consists of at least two independent receivers for the P- and C-channels, as specified in Section 1.2.3 for Levels 3 and 4.  The P-channel is of course necessary for initiation of the C-channel; subsequent normal control of the C-channel is performed by the GES via sub-band signaling on the C-channel.  The requirement in (iii) above, which does not require any muting of a C-channel due to any loss of the P-
channel, is intended to allow an existing C-channel to continue to operate in the event of a temporary fade of the P-channel up to the point in time when the C- channel is either intentionally terminated or until the ground-to-air C-channel itself is lost, thus avoiding unnecessary interruptions to C-channel operations. However, it is not intended to allow single receiver-channel configurations 
which provide C-channel capabilities. 

## 2.2.4.2.9 Load Vswr Capability

 
When the transmitter is terminated in a load with a VSWR of 2:1 at any reflection coefficient phase angle and then commanded to output full-rated power in single-carrier mode, the measured power shall not be lower than 0.9 dB below full-rated power measured with the transmitter terminated in a matched resistive load. The transmitter also shall be capable of continuously withstanding, without damage, a load with an infinite VSWR at any phase angle. 

## 2.2.4.2.10 Transmitter Tuning 2.2.4.2.10.1 Tuning Range And Channel Increments

 
The transmitter shall tune within the frequency range per the following table in 2.5 kHz increments and shall not tune to frequencies outside this band. 
 
 
NOTE: 
The channel center frequencies near the allocated band boundaries are restricted to contain the sideband energy within the allocated bands when the maximum Doppler correction is applied.  The center frequencies of high data rate channels are spaced farther from band boundaries than low data rate 
channels. 
The ranges of the transmit channel center frequencies for some channel rates and a maximum Doppler correction of 2 kHz are given in the following table. 

  Transmit Channel Center Frequencies and Tuning Ranges 



Channel 
 
Modulation 
Carrier Tuning Ranges (MHz) 


Rate  
 
Type  
 
(Tuning Increment = 2.5 kHz) 
 
 
0.60 kbps  
A-BPSK  
1626.5075 to 1660.4925 


1.20 kbps  
A-BPSK  
1626.5075 to 1660.4925 


8.4 kbps 
 
A-QPSK  
1626.5100 to 1660.4900 


10.5 kbps  
A-QPSK  
1626.5125 to 1660.4875 


21.0 kbps  
A-QPSK  
1626.5175 to 1660.4825 

 
 
NOTE: 
The band edge channel assignments provide guard bands which take into account Doppler shifts due to aircraft motion, transmit frequency shifts due to AES Doppler corrections, transmit spectrum width and transmit frequency 
tolerance to avoid interference to radio services outside the allocated AMSS frequency band.  The Doppler contributions added to the guard bands protect 
ground-based services from AES Doppler shifted emissions. 

## 2.2.4.2.10.2 Channel Numbering

 
The transmitter shall be tuned to channels by commands based on the channel number CTx, derived as follows: 


 frequency of transmission (MHz)  1611.5 


CTx = 
 

  0.0025 
After log-on, the AES shall transmit only on the channels assigned by the GES. 

## 2.2.4.2.11 Tuning Stabilization Time

 
The receiver and transmitter synthesizer stabilization times must be small enough for the 
Pd/R-channel assignment response time requirements to be met, as specified in Reference 
Document "B", Section 6.5.1. 
 
 
NOTE: 
For the receiver synthesizer stabilization time to be verified as well as the transmitter settling time, a receiver channel re-assignment must also be made 
while performing this test. 

## 2.2.4.2.12 Phase Noise

 
The continuous power density spectrum resulting from phase noise induced on an unmodulated carrier shall not exceed the spectrum envelope given in Figure 2 of Reference Document "B".  Where discrete spectral components exist, the sum of the discrete phase noise components and continuous spectral component averaged over a bandwidth of 10 Hz on either side of the discrete component shall not exceed the phase noise mask. 
 

## 2.2.4.2.13 Frequency Accuracy

 
The maximum contribution of the AES frequency reference to the frequency error shall not exceed 320 Hz. 

 
 
NOTE: 
When the transmit Doppler correction is derived from a measured received signal Doppler shift, a transceiver reference oscillator frequency tolerance of one part in 107 is required. 

## 2.2.4.2.14 Doppler Correction

 
The transmit frequency shall be compensated in accordance with the measured receive frequency offset, or by other means.  When the offset measurement method is used, the transmit offset must be of the opposite sense and approximately 1.064 times greater than the measured receiver offset. 

 
Accuracy of Doppler compensation shall be such that the transmitted signal has the following properties. 
a. 
Total RSS error from nominal frequency shall not exceed 335 Hz.  (This assumes zero error for the received GES signal and includes the AES transmit/receive frequency reference error and the AES Automatic Frequency Compensation (AFC) residual errors.  See Reference Document "A", Table 8.0.2.) 
b. 
The average residual Doppler rate of change (which will be seen by the satellite) shall not exceed 15 Hz/sec. 
The Doppler adjustment resolution shall not exceed 10 Hz. 

## 2.2.4.2.15 Doppler Rate Capability

 
The transmitter shall maintain the frequency accuracy specified in Sections 2.2.4.2.13 and 2.2.4.2.14 for all rates of change of the received signal specified in Section 2.2.4.1.9 or equivalent changes in the range rate of change. 

## 2.2.4.2.16 Signal Spectrum

 
While transmitting a single modulated signal at the rated output power of the transmitter, the transmitted signal power spectrum levels at the transmitter output terminal shall be no greater than the values given below: 



Spectrum Level Relative to 


Frequency Offset 
 
 
Maximum Envelope Level (dBe) 
 
 
0.75 x SR 

  0 


1.40 x SR 


- 20 


2.95 x SR 


- 40 


35 kHz  


- 40 


 
 
 
where: 
SR = Symbol Rate 


SR = 1 x Channel rate for A-BPSK 


SR = 1/2 x Channel rate for A-QPSK 


SR = 1/(log2 M) x Channel rate, 


where M = number of states for 


other digital modulations. 
 
The measurement resolution bandwidth should be approximately 0.1 x SR. The envelope level listed in the table is the relative amplitude as measured in the resolution bandwidth as a function of the frequency offset from the carrier frequency. The maximum level which is the reference for the dBe criteria will occur at the carrier frequency.  The envelope level limits at the frequency offsets that are between the values shown above are in Figure 2-0. 

 

## 2.2.4.2.17 R- And T-Channel Configuration And Transmitter Requirements

 
The R- and T-channel configuration and transmitter requirements shall be the minima specified for the AES in Reference Document "A", Sections 3.1, 3.3.2, 3.4 and Appendix 6; and Reference Document "B" Section 4.2.3, including all referenced tables, figures, annexes and appendices applicable to the AES.  These are identified in the following listings. 

 
 
Reference Document "A", Section 3.0 (Channel Configuration): 



Version 
 
 
3.1  
Channel Configuration -- General 
 
1.45 
 
 
3.3.2  
Return Link Burst Mode Data Channels 
1.45 
 
 
3.3.2.1 
T-Channel Format 


1.45 
 
 
3.3.2.2 
R-Channel Format 


1.45 
 
 
3.3.2.3 
R- and T-Channel Transmit Operations 
1.45 
 
 
3.3.2.4 
R- and T-Channel Transmit Timing 
 
1.45 
 
 
3.4  
Interleaver  


1.45 

 
 
Reference Document "A", Appendix 6.0 (Channel Timing Relationships): 
 
Figure AP6-1: Timing Relationships Between P- and R-Channels 
 
 
Figure AP6-2: Timing Relationships Between P- and T-Channels 
 
Reference Document "B", Section 4.0 (Channel Unit Requirements): 
 
4.2.3.1  R-Channel Burst Timing 
 
 
4.2.3.2  T-Channel Burst Timing 

## 2.2.4.2.17.1 Transmit Pulse-Shaping Filter Response

 
The transmit pulse-shaping filter responses (amplitude and phase) shall not exceed the limits of the envelopes given in Reference Document "B", Figures 3, 4 and 5. 

## 2.2.4.2.18 C-Channel Transmitter Requirements

 
Refer to Section 2.2.4.1.12 for C-channel transmitter requirements that are in common with those for the C-channel receiver.  Only requirements that are peculiar to the C-channel transmitter are included in the following Section. 

## 2.2.4.2.18.1 Transmit Pulse-Shaping Filter Response

 
The A-QPSK transmit pulse-shaping filter response (amplitude and phase) shall not exceed the limits of the envelopes given in Reference Document "B", Figures 4 and 5. 
 

## 2.2.5 Satellite Subnetwork Data Link Layer Functions

 
The minimum satellite data link layer requirements shall be the minima specified for the AES in Reference Document "A", Section 4.0, and Reference Document "B", Section 6.0, including all referenced tables, figures, annexes and appendices applicable to the AES. These are identified in the following listings. 

 
 
Reference Document "A", Section 4.0 (Link Layer Formats and Protocols): 
 
4.1  
General Link Layer Formats and Protocols 
 
 
4.2  
Basic Signal Unit Concepts 
 
 
4.3  
Link Layer Services (Direct Link Service (DLS) and Reliable Link Service (RLS)) 
 
 
4.3.1  
Link Layer Functional Description 
 
 
4.3.2  
Transmission Sequence 
 
 
4.3.3  
R-Channel Retransmission Randomization 
 
 
4.3.4  
Link Reference Number 
 
 
4.3.5  
Reference Number Assignment Algorithm 
 
 
4.3.6  
Link Interface Data Unit (LIDU) 
 
Reference Document "A", General: 
 
Signal Format Figures S0 through S37  
 
 
Annex 1 (Information Element Coding) 
 
 
Annex 2 (Timers) 
 
For all figures (including Specification and Description Language (SDL) and Signal Units (SUs)) associated with the above requirements, see the cross-reference in Reference Document "B", Annex 1. 

 
 
NOTE: 
Message-type codes defined in Reference Document "A", Annex 1, that are not mandatory for the MOPS and not supported by an AES shall be considered as 
RESERVED. 
 
Reference Document "B", Section 6.0 (Access Control Requirements): 
 
6.1  
Access Control Requirements -- General 
 
 
6.2  
Signaling Channels 
 
 
6.3.1  
Channel Configuration Requirements 
 
 
6.3.2  
Channel Setting 
 
 
6.4  
AES Access Control -- General Requirements 
 
 
6.5  
AES System Response Requirements 
 
 
6.5.1  
Pd/R-Channel Assignment Response Time Requirements 
 
 
6.5.2  
P- to R-Channel Turnaround Timing Requirements 
 
 
6.5.3  
Multiple SUs Transmission Requirement 
 
 
6.6  
Mandatory Minimum AES Buffer Size Requirements 
 
 
Reference Document "B", Annex 1 (Module 1 Cross Reference Tables): 

 
 
Table CR4.1 
Packet Mode Data Services 
 
 
NOTE: 
Satellite data link layer requirements that are specific to packet-mode data 
services are among the subjects of Section 2.2.7 of this document. 

## 2.2.6 Satellite Subnetwork Management Requirements

 
The minimum requirements for AES satellite subnetwork operational management and control shall be the minima specified for the AES in Reference Document "A", Section 5.0, and Reference Document "B", Section 7.0, including all referenced tables, figures, annexes and appendices applicable to the AES.  These are identified in the following listings. 

 
 
Reference Document "A", Section 5.0 (AES Management): 



Version 
 
 
5.1  
AES Management -- General 


1.44 
 
 
5.2  
System Log-On/Log-Off 
 
 
5.2.1  
NOT APPLICABLE (Introductory Only) 
 
 
5.2.2  
(Search Mode) 
 
 
5.2.3  
(System Table Version Check)  


1.44 
 
 
5.2.4  
(Pd-Channel/Spot Beam Selection) 


1.44 
 
 
5.2.5  
(Log-On Initiation) 


1.45 
 
 
5.2.6  
(Log-On Information) 
 
 
5.2.7  
(Optional flight ID Log-On Information) 
 
 
5.2.8  
(Log-On/Log-Off Sequences) 


1.45 
 
 
5.2.9  
(Log-On Confirm) 


1.45 
 
 
5.2.10 
(Log-On Handover) 
 
 
5.2.11 
AES System Table Broadcast 
 
 
5.2.11.1 
(PARTIAL and COMPLETE Sequences) 


1.44 
 
 
5.2.11.2 
(Version Check and Selection of Update Method)  
 
 
1.44 
 
 
5.2.12 
NOT APPLICABLE (Optional Double Receiver) 
 
 
5.2.13 
NOT APPLICABLE (GES Requirements) 
 
 
5.2.13.1 
NOT APPLICABLE (GES Requirement) 
 
 
5.2.13.2 
NOT APPLICABLE (GES Requirement) 
 
 
5.2.13.3 
(Log-on reject) 
 
 
5.2.13.4 
NOT APPLICABLE (GES Requirement) 
 
 
5.2.13.5 
NOT APPLICABLE (GES Requirement) 
 
 
5.2.13.6 
NOT APPLICABLE (GES Requirement) 
 
 
5.2.14 
(AES Log-Off) 
 
 
5.2.15 
(Log-On Verification (Direct and Indirect/Prompt)) 
 
 
5.2.16 
NOT APPLICABLE (GES Requirements) 
 
 
5.2.17 
(Log Control/Data Channel Reassignment) 
 
 
5.2.18 
(Pd-Channel Degradation/Handover/Initialization) 
 
 
5.3  
Handover Procedures  


1.44 
 
 
5.3.1  
Fully Automatic Handover 
 
 
5.3.2  
Manually Initiated GES-to-GES Handover 
|    |    |                                                      |                                         |                                                         |      |     |     | 5.3.3     | Manually Initiated Satellite-to-Satellite Handover    |
|----|----|------------------------------------------------------|-----------------------------------------|---------------------------------------------------------|------|-----|-----|-----------|-------------------------------------------------------|
|    |    | 5.3.4                                                | Spot Beam-to-Spot Beam Handover         |                                                         |      |     |     |           | 1.44                                                  |
|    |    | 5.3.4.1                                              | (Fully Automatic)                       |                                                         |      |     |     |           |                                                       |
|    |    | 5.3.5                                                | NOT APPLICABLE (GES Requirements)       |                                                         |      |     |     |           |                                                       |
|    |    | 5.4                                                  | NOT APPLICABLE (GES Requirements)       |                                                         |      |     |     |           |                                                       |
|    |    | 5.5                                                  | Tables at AES                           |                                                         |      |     |     |           |                                                       |
|    |    | 5.5.1                                                | System Table Category                   |                                                         |      |     |     |           |                                                       |
|    |    | 5.5.2                                                | Log-On Confirm category                 |                                                         |      |     |     |           |                                                       |
|    |    | 5.5.3                                                | Service Capabilities Dependent Category |                                                         |      |     |     |           |                                                       |
|    |    | 5.5.4                                                | Owner/Operator Requirements Category    |                                                         |      |     |     | 1.44      |                                                       |
|    |    | 5.5.5                                                | Spot Beam Map Category                  |                                                         |      |     |     |           |                                                       |
|    |    | 5.6                                                  | System Broadcasts                       |                                                         |      |     |     |           |                                                       |
|    |    | 5.6.1                                                | (Optional) Universal Time               |                                                         |      |     |     |           |                                                       |
|    |    | 5.6.2                                                | Selective Release                       |                                                         |      |     |     |           |                                                       |
|    |    | 5.6.3                                                | (Optional) GES Specific Data Broadcast  |                                                         |      |     |     | 1.44      |                                                       |
|    |    |                                                      |                                         | (SUs are considered reserved even if this option is not |      |     |     |           |                                                       |
|    |    |                                                      |                                         | implemented.)                                           |      |     |     |           |                                                       |
|    |    | Figure 46 AES System Log-On and Handover Process ALO |                                         |                                                         | 1.45 |     |     |           |                                                       |

 
For all figures (including SDL and SUs) associated with the above requirements, see the cross-reference in Reference Document "B", Annex 1, "Network Management Cross- Reference with Figures," and, "Network Management Cross-Reference with Signal Units." 

 
 
Reference Document "B", Section 7.0 (Satellite Network Management Requirements): 


Version 
 
 
7.3  
Timing Requirements 
 
 
7.3.1  
P-Channel Quality Monitoring 
 
 
7.3.3  
Selective Release (See the Note below.) 
 
 
7.4  
AES Table Requirements 
 
 
7.4.1  
System Table Requirements 
 
 
7.4.2  
Log Status and Service Capability Tables Requirements 
 
 
7.4.3  
Owner/Operator Table Requirements  


1.18 
 
 
7.4.4  
Spot Beam Map Requirements  


1.18 
 
 
7.5  
NOT APPLICABLE (System Data/Maintenance Interface Requirements) 

 
NOTES: 
1. 
Selective Release is the only currently defined mechanism available for channel clearing.  One or more additional mechanisms may be defined in the future to assure appropriate clearing of spectrum if necessary for protection of the AMS(R)S. 
 
 
2. 
AESs commonly have a programmable Owner Requirements Table by which the preference for selection of certain systems, satellites, and/or GESs can be exercised. There are several criteria by which preferential selection for log-in can be made; e.g., service provider identity, cost.  If this capability were misused (e.g., to exclude particular systems, satellites, or GESs) safety could be derogated. 
 

## 2.2.7 Packet-Mode Data Service Requirements

 
The AES shall provide for packet-mode data service using Data-2, Data-3, or both protocols. 

 
Data-2 is a specific implementation of the AMSS system in which the air/ground subnetwork access equipment (e.g., the ARINC 741 SDU) contains only the physical and link layer functionality. 
Data-3 is a specific implementation of the AMSS system in which the air/ground subnetwork access equipment (SDU) contains the physical layer, link-layer and network layer functionality according to ISO terminology. 

## 2.2.7.1 Packet-Mode Data-2 Service Requirements

 
An AES offering packet-mode Data-2 service shall provide a Link Service Interface as a direct access method to the Reliable Link Service (RLS) link-layer protocols. 
 
Link Service Data Units (LSDUs) are injected or collected at the Link Service Interface in the AES. In order to ensure the forward compatibility of the Data-2 architecture with the standard subnetwork architecture (Data-3), the Link Service Interface user shall add a twooctet header to the user's message to form an LSDU before transmission. The user's message may consist of binary data and may contain up to 504 octets. The two-octet dedicated header shall be set to the value FFFF hex. Unless provided by the Link Service Interface user, a Q-precedence of seven (7) shall be used for transmission of LSDUs. The Link Service Interface user shall extract a received user message from an LSDU by removing the two-octet header. 

 
All LSDUs passed to the Link Service Interface shall be transmitted to the GES while the AES is logged on. If the AES is not logged on, any LSDU passed to the AES shall be discarded. Conversely, while the AES is logged onto a particular GES, any messages received from the GES shall be forwarded to the Link Service Interface regardless of the availability of the destination avionics equipment. 
 
 
NOTE: 
On the ground, a separate Switched Virtual Circuit (SVC) is established for each AES between the GES and a predefined SubNetwork Point of Attachment (SNPA) DTE using X.25/X.75 protocol. The terrestrial SVC is established by the GES when an AES is logged onto the GES and is cleared when the AES is 
logged off of the GES. 

## 2.2.7.2 Packet-Mode Data-3 Service Requirements

 
Data-3 is the given name for the satellite subnetwork layer protocol architecture implemented in the AES. 
The Satellite Subnetwork Layer (SSNL) in the AES shall offer connection-oriented packet data service to the Higher Layer Entities (HLEs) by establishing satellite subnetwork SVCs 
with its peer entity in the GES. It also shall offer methods to convert addressing from the HLE to the SSNL.  (Figure 2-1 refers.) 

 
The SSNL in the AES shall support the following three main functions: 
 
 
a. 
The Satellite Subnetwork Dependent (SSND) sublayer 


b. 
The Satellite Subnetwork Access (SSNAc) sublayer 


c. 
The Satellite Subnetwork InterWorking Function (IWF). 
 
The SSND sublayer shall perform the SSND protocol between the AES and a log-on GES as defined in Reference Document "A" Section 7 by exchanging SubNetwork Protocol Data Units (SNPDUs). The SSNAc sublayer in the AES shall perform the ISO 8208 DCE protocol between the AES and the connected airborne HLE (DTE). The IWF shall provide the protocol conversion functions and the flow control operation required between the SSND and SSNAc (ISO 8208) protocols. 

 
NOTES: 1. 
This architecture allows communication between ISO conforming entities and it is suitable for support of the Aeronautical Telecommunications 
Network (ATN) higher layer protocols and applications. 


The role of the ATN is to define an environment within which reliable endto-end data transfer may take place, spanning the envisioned airborne, air/ground, and ground-based data subnetworks, including the satellite subnetwork, while providing interoperability among those networks. The critical emphasis is on end-system data transfer interoperability. In the ATN environment, the Satellite Subnetwork Layer must support the transparent transfer of Network Protocol Data Units (NPDUs) between adjacent interworking entities (or HLEs as seen by the SSNL). This also implies the transparent transfer of global addresses (or NSAPs) and of 
quality of service information (including network priority) as well as of user data. 
 
 
2. 
Valuable guidance for packet data communications is provided in RTCA/DO-205, "Design Guidelines and Recommended Standards to Support Open Systems Interconnection for Aeronautical Mobile Digital Communications"; in particular, Part 1, Section 6.0 "Subnetwork Protocols to Access and Support ATN" discusses ground, airborne and air/ground subnetworks; Part 1 Appendix B gives a summary of the ISO 8208 packet level Subnetwork Access Protocol (SNAcP) (see Section 
2.2.7.5). 

## 2.2.7.3 Priority, Precedence And Preemption

 
The order of precedence of transmission of packet-mode data appearing at an AES data port shall be as shown in Table 2-1.  A message is handled in the link layer by segmenting it into one or more SUs.  Transmission preemption, if necessary, shall be effected by immediately changing the order of SU transmission such that the SUs comprising the higher-priority message are transmitted before lower-priority SUs.  Preemption of lowerpriority messages, if necessary, shall be effected by any means necessary to preserve the higher-priority message(s), e.g., the overwriting of buffers.  

 
The target and selected values of the priority of data on a connection in the ISO 8208 CALL REQUEST and CALL ACCEPTED packets shall be mapped to the LIDU Q number of the CONNECTION REQUEST and CONNECTION CONFIRM SNPDUs as defined in Table 2-1. 

|                                            | SNC Priority in    |
|--------------------------------------------|--------------------|
| CALL_REQUEST/                              |                    |
| Category of Messages                       |                    |
| CALL_ACCEPTED                              |                    |
|                                            |                    |
| Packet                                     |                    |
| 4,  5                                      |                    |
| SAFETY PACKET-MODE DATA COMMUNICATIONS     |                    |
| 14                                         | 14                 |
| Network/Systems Management                 |                    |
| 2                                          |                    |
|                                            |                    |
| Reserved                                   | 13                 |
| 7                                          |                    |
| Not Applicable                             |                    |
| Reserved                                   | 12                 |
| 7                                          |                    |
|                                            | Not Applicable     |
| 11                                         | 11                 |
| Relating to Direction Finding              |                    |
| Reserved                                   | 10                 |
| 7                                          |                    |
|                                            | Not Applicable     |
| Reserved                                   | 9                  |
| 7                                          |                    |
|                                            | Not Applicable     |
| Meteorological Communications              | 8                  |
| Flight Regularity Communications           | 7                  |
| 6                                          | 6                  |
| Messages (NOTAMs, ATIS, etc.)              |                    |
| 5                                          | 5                  |
| 3                                          |                    |
|                                            |                    |
| Network/Systems Administration             |                    |
| 2                                          |                    |
|                                            |                    |
| NON-SAFETY PACKET-MODE DATA COMMUNICATIONS |                    |
| Unspecified (ISO 8208 explicit)            | 255                |
| 6                                          |                    |
|                                            |                    |
| Reserved (ISO 8208 explicit)               | 254-15             |
| 7                                          |                    |
|                                            | Not Applicable     |
| Reserved                                   | 4                  |
| 7                                          |                    |
|                                            | Not Applicable     |
| 3                                          | 3                  |
| Charter Communications (AAC/APC)           |                    |
| 2                                          | 2                  |
| Government Communications (AAC/APC)        |                    |
| Normal Priority Administrative (AAC/APC)   | 1                  |
| Low Priority Administrative (AAC/APC)      | 0                  |
| 6                                          |                    |
|                                            |                    |
| Not specified                              | None               |
| 6                                          |                    |
| 0                                          | None               |
| 6                                          |                    |
|                                            |                    |

 

Notes: 1. Q-Number refers to the Link-Layer precedence contained in an SU to be transmitted. 
2. Network/System Management and Administration are not categories of end-use messages but are used by ATN or 
other network management/administration functions. 
 
3. SNC Priorities 5 and above can be either ATS or AOC Communications. 
 
4. Priority levels at the ISO-8208 interface to the AMSS Subnetwork are mapped to equivalent ATN priority levels 
by the ATN Subnetwork Dependent Convergence Function (SNDCF) contained in external ATN facilities. 
 
5. ISO 8208 priorities range from 0 (lowest priority) to 14 (highest priority).  The value 255 (all ones) explicitly 
indicates "unspecified".  All other values (i.e., 15 through 254) are reserved. 
 
6. "None" means that the optional ISO 8208 Priority Facility was not invoked in the received CALL_REQUEST or 
CALL_ACCEPTED packets, and/or is not invoked in the forwarded INCOMING_CALL or CALL_CONNECTED packets.  (The AMSS does not forward a Priority Facility for the cases of explicitly requested priorities 0 and 255.) 
 
7. Any call attempted at an invalid priority is rejected (specifically, the SNC is cleared). 

 
SNC Priority in 
Q-Number 1 
INCOMING_CALL/ 
CALL_CONNECTED 
Packet 4,  5 

 
 
The LIDU Q number associated with the CONNECTION REQUEST and CONNECTION 
CONFIRM SNPDUs shall be mapped into the target and selected values of the priority of data on a connection in the ISO 8208 INCOMING CALL and CALL CONNECTED packets as defined in Table 2-1. 

 
A Subnetwork Connection (SNC) of the lowest priority shall be cleared as necessary to accept a request for higher priority service. 
 
 
NOTE: 
When packet-mode operations are conducted using a Data-2 implementation, 
priority, precedence and preemption are managed by a higher-layer entity. 

## 2.2.7.4 Satellite Subnetwork Requirements

 
In addition to the satellite data link layer requirements (foundation protocol) specified in Section 2.2.5 of this document (which includes the Direct Link Service (DLS) quality of service), the AES shall also provide RLS on the satellite subnetwork.  RLS shall perform Automatic selective Repeat Request (ARQ) functions to supervise the correct reception of each LSDU.  As with Data-3, systems employing packet-mode Data-2 on the satellite subnetwork shall use the RLS. 

## 2.2.7.4.1 Data-2 Aes Requirements

 
The minimum requirements for Data-2 service on the satellite subnetwork shall be the minima specified for the AES in Reference Document "A", Section 7.0 and Appendix 3, and in Reference Document "B", Section 9.0, including all referenced tables, figures, annexes and appendices.  These are identified in the following listings. 

 
 
Reference Document "A", Section 7.0 (Data Communication Services): 
 
7.1.1  
Data System Architecture (Layers 1 and 2 Only) 
 
 
7.1.2  
Link Layer Structure 
 
 
7.1.3  
NOT APPLICABLE (Satellite Subnetwork Layer Structure) 
 
 
7.1.4  
NOT APPLICABLE (Subnetwork Services) 
 
 
7.1.5  
NOT APPLICABLE (Satellite Subnetwork Primitives) 
 
 
7.1.6  
NOT APPLICABLE (SNPDU) 
 
 
7.1.7  
NOT APPLICABLE (Logical Channel Number) 
 
 
7.2  
Link Layer Protocol Description 
 
 
7.2.1  
P-Channel Protocol 
 
 
7.2.1.1 
General 
 
 
7.2.1.2 
No Errors 
 
 
7.2.1.3 
Acknowledgement Lost 
 
 
7.2.1.4 
SU-Set Lost 
 
 
7.2.1.5 
SU-Set Errored 
 
 
7.2.1.6 
Retransmission Errored 
 
 
7.2.1.7 
Flow Control 
 
 
7.2.2  
R-Channel Protocol 
 
7.2.2.1 
General 
 
 
7.2.2.2 
No Errors 
 
 
7.2.2.3 
SU-Set or Acknowledgement Lost 
 
 
7.2.2.4 
SU-Set Partial Loss 
 
 
7.2.2.5 
Retransmission Errored 
 
 
7.2.2.6 
Flow Control 
 
 
7.2.3  
T-Channel Protocol 
 
 
7.2.3.1 
General 
 
 
7.2.3.2 
No Errors 
 
 
7.2.3.3 
Acknowledgement Lost 
 
 
7.2.3.4 
SU-Set Partial Loss 
 
 
7.2.3.5 
SU-Set Complete Loss 
 
 
7.2.3.6 
Flow Control 
 
 
7.2.4  
Link Management Functions 
 
 
7.2.4.1 
Resource Management Functions 
 
 
7.2.4.1.1 T-Channel Reservation Protocol 
 
 
7.2.4.1.2 Access Request 
 
 
7.2.4.1.3 Assignment 
 
 
7.2.4.1.4 Additional T-Channel Assignments 
 
 
7.2.4.1.5 Reservation Synchronization 
 
 
7.2.4.1.6 NOT APPLICABLE (Time Allocation Algorithms) 
 
 
7.2.4.2 
Channel Unit Control 
 
 
7.2.5  
Link Layer Recovery During AES Management Operation 
 
Reference Document "A", Appendix 3 (T-Channel Protocol Description): 
 
1 
 
Introduction 
 
 
2 
 
Link Protocol Data Units (LPDUs) 
 
 
3 
 
LSDU Transmission Protocol 
 
 
3.1  
T-Channel Queuing Unit Block (TQU) 
 
 
3.1.1  
TQU Process Description 
 
 
3.1.2  
TTXPROC (Q, MT) 
 
 
3.2  
T-Channel Transmit Block (TTP) & (Shared) R/T Transmitter Block 
 
 
3.2.1  
TTP Process Description 
 
 
3.2.2  
TXSU(N) 
 
 
3.2.3  
RTSW Process Description 
 
 
3.3  
NOT APPLICABLE (T-Channel Message Assembler Block (TMA)) 
 
 
3.4  
NOT APPLICABLE (T-Channel Acknowledge Block (TAK)) 
 
 
4 
 
Reservation Protocol 
 
 
4.1  
T-Channel Request Generator Block (TRG) 
 
 
4.1.1  
TRG Process Description 
 
 
4.1.2  
REQPROC Process Description 
 
 
4.1.3  
TREQPROC Process Description 
 
 
4.1.4  
RREQPROC Process Description 
 
 
4.1.5  
RFCPROC Process Description 
 
 
4.2  
T-Channel Reservation Handler Block (TRH) 
 
 
4.2.1  
TRH Process Description 
 
 
4.3  
NOT APPLICABLE (T-Channel Reservation Synchronizer Block (TRS) 
 
 
4.4  
NOT APPLICABLE (T-Channel Manager Block (TCM)) 
For all figures (including SDL and SUs) associated with the above requirements, see the cross-reference in Reference Document "B", Annex 1. 
 
Reference Document "B", Section 9.0 (Packet Mode Data Service Requirements): 
 
9.3.2  
Physical and Link Layer Requirements 
 
 
9.4.1.1 
Pd/T-Channel Slot Assignment Response Time Requirements 
 
 
9.4.1.2 
R/T-Channel Switch-Over Timing Requirements 
 
 
9.4.1.3 
T/R-Channel Switch-Over Timing Requirements 
 
 
9.5.1  
AES Link Layer Buffer Size Requirements 

## 2.2.7.4.2 Data-3 Aes Requirements

 
The minimum requirements for Data-3 packet-mode data service on the satellite subnetwork shall be the minima specified for the AES in Reference Document "A", Section 7.0 and Appendices 3 and 7, and in Reference Document "B", Section 9.0, including all referenced tables, figures, annexes and appendices applicable to the AES.  These are identified in the following listings. 

 
 
Reference Document "A", Section 7.0 (Data Communication Services): 
 
7.1  
General 
 
 
7.1.1  
Data System Architecture 
 
 
7.1.2  
Link Layer Structure 
 
 
7.1.3  
Satellite Subnetwork Layer Structure 
 
 
7.1.4  
Subnetwork Services 
 
 
7.1.4.1 
Subnetwork Service Features 
 
 
7.1.5  
Satellite Subnetwork Primitives 
 
 
7.1.6  
Subnetwork Protocol Data Unit (SNPDU) 
 
 
7.1.7  
Logical Channel Number 
 
 
7.2  
Link Layer Protocol Description 
 
 
7.2.1  
P-Channel Protocol 
 
 
7.2.1.1 
General 
 
 
7.2.1.2 
No Errors 
 
 
7.2.1.3 
Acknowledgement Lost 

|     |     | 7.2.1.4    | SU-Set Lost                    |
|-----|-----|------------|--------------------------------|
|     |     | 7.2.1.5    | SU-Set Errored                 |
|     |     | 7.2.1.6    | Retransmission Errored         |
|     |     | 7.2.1.7    | Flow Control                   |
|     |     | 7.2.2      | R-Channel Protocol             |
|     |     | 7.2.2.1    | General                        |
|     |     | 7.2.2.2    | No Errors                      |
|     |     | 7.2.2.3    | SU-Set or Acknowledgement Lost |
|     |     | 7.2.2.4    | SU-Set Partial Loss            |
|     |     | 7.2.2.5                                              | Retransmission Errored                               |
|-----|-----|------------------------------------------------------|------------------------------------------------------|
|     |     | 7.2.2.6                                              | Flow Control                                         |
|     |     | 7.2.3                                                | T-Channel Protocol                                   |
|     |     | 7.2.3.1                                              | General                                              |
|     |     | 7.2.3.2                                              | No Errors                                            |
|     |     | 7.2.3.3                                              | Acknowledgement Lost                                 |
|     |     | 7.2.3.4                                              | SU-Set Partial Loss                                  |
|     |     | 7.2.3.5                                              | SU-Set Complete Loss                                 |
|     |     | 7.2.3.6                                              | Flow Control                                         |
|     |     | 7.2.4                                                | Link Management Functions                            |
|     |     | 7.2.4.1                                              | Resource Management Functions                        |
|     |     | 7.2.4.1.1                                            | T-Channel Reservation Protocol                       |
|     |     | 7.2.4.1.2                                            | Access Request                                       |
|     |     | 7.2.4.1.3                                            | Assignment                                           |
|     |     | 7.2.4.1.4                                            | Additional T-Channel Assignments                     |
|     |     | 7.2.4.1.5                                            | Reservation Synchronization                          |
|     |     | 7.2.4.1.6                                            | NOT APPLICABLE (Time Allocation Algorithms)          |
|     |     | 7.2.4.2                                              | Channel Unit Control                                 |
|     |     | 7.2.5                                                | Link Layer Recovery During AES Management Operation  |
|     |     | 7.3                                                  | SSND Sublayer Protocol Description                   |
|     |     | 7.3.1                                                | Connection Establishment Procedure                   |
|     |     | 7.3.1.1                                              | Procedure for Originating SSND                       |
|     |     | 7.3.1.2                                              | Procedure for Receiving SSND                         |
|     |     | 7.3.2                                                | Connection Release Procedure                         |
|     |     | 7.3.2.1                                              | Procedure for Originating SSND                       |
|     |     | 7.3.2.2                                              | Procedure for Receiving SSND                         |
|     |     | 7.3.2.3                                              | SSND-Initiated Release                               |
|     |     | 7.3.3                                                | Data Transfer and Expedited Data Transfer Procedures |
|     |     | 7.3.3.1                                              | Data Transfer Procedure                              |
|     |     | 7.3.3.3                                              | Flow Control Procedure                               |
|     |     | 7.3.3.4                                              | Expedited Data Transfer Procedure                    |
|     |     | 7.3.3.4.1                                            | Procedure for Originating SSND                       |
|     |     | 7.3.3.4.2                                            | Procedure for Receiving SSND                         |
|     |     | 7.3.4                                                | Reset Procedure                                      |
|     |     | 7.3.4.1                                              | Procedure for Originating SSND                       |
|     |     | 7.3.4.2                                              | Procedure for Receiving SSND                         |
|     |     | 7.3.5                                                | Error Procedure                                      |
|     |     | 7.3.5.1                                              | Error Handling                                       |
|     |     | 7.3.5.1.1                                            | Log-On Renewal/AES Log-Off                           |
|     |     | 7.3.5.1.2                                            | Transmission Error                                   |
|     |     | 7.3.5.1.2.1 Receiving SSND Sublayer Error Recovery   |                                                      |
|     |     | 7.3.5.1.2.2 Originating SSND Sublayer Error Recovery |                                                      |
|     |     | 7.3.5.1.3                                            | Protocol Error                                       |
|     |     | 7.3.6                                                | SNPDU -- Primitive Construction Rules                |
|     |     | 7.3.6.1                                              | SNPDU -- General Construction Rules                  |
|     |     | 7.3.6.2                                              | DTE Addresses                                        |
|     |     | 7.3.6.2.1                                            | DTE Address Format and Characteristics               |
|     |     | 7.3.6.2.2                                            | DTE Address Processing                               |

 
 
7.3.6.2.3 
DTE Address Compression and Expansion 
 
 
7.3.6.3 
Network Service Access Point (NSAP) Addresses 
 
 
7.3.6.3.1 
NSAP Address Format and Characteristic 
 
 
7.3.6.3.2 
NSAP Address Processing 
 
 
7.3.6.4 
SNS User Data 
 
 
7.3.6.5 
Receipt Confirmation Selection 
 
 
7.3.6.6 
SNC Priority 
 
 
7.3.6.7 
Throughput Class Negotiation 
 
 
7.3.6.7.1 
Throughput 
 
 
7.3.6.7.2 
AES Actions 
 
 
7.3.6.7.3 
NOT APPLICABLE (GES Actions) 
 
 
7.3.6.8 
Transit Delay 
 
 
7.3.6.9 
Expedited Data Negotiation 
 
 
7.3.6.10 
Combined Establishment/Release Selection 
 
 
7.3.6.11 
Fast Select Selection 

## Reference Document "A", Appendix 3 (T-Channel Protocol Description):

 
 
1 
 
Introduction 
 
 
2 
 
Link Protocol Data Units (LPDUs) 
 
 
3 
 
LSDU Transmission Protocol 
 
 
3.1  
T-Channel Queuing Unit Block (TQU) 
 
 
3.1.1  
TQU Process Description 
 
 
3.1.2  
TTXPROC (Q, MT) 
 
 
3.2  
T-Channel Transmit Block (TTP) & (Shared) R/T Transmitter Block 
 
 
3.2.1  
TTP Process Description 
 
 
3.2.2  
TXSU(N) 
 
 
3.2.3  
RTSW Process Description 
 
 
3.3  
NOT APPLICABLE (T-Channel Message Assembler Block (TMA)) 
 
 
3.4  
NOT APPLICABLE (T-Channel Acknowledge Block (TAK)) 
 
 
4 
 
Reservation Protocol 
 
 
4.1   
T-Channel Request Generator Block (TRG) 
 
 
4.1.1  
TRG Process Description 
 
 
4.1.2  
REQPROC Process Description 
 
 
4.1.3  
TREQPROC Process Description 
 
 
4.1.4  
RREQPROC Process Description 
 
 
4.1.5  
RFCPROC Process Description 
 
 
4.2  
T-Channel Reservation Handler Block (TRH) 
 
 
4.2.1  
TRH Process Description 
 
 
4.3  
NOT APPLICABLE (T-Channel Reservation Sync Block (TRS) 
 
 
4.4  
NOT APPLICABLE (T-Channel Manager Block (TCM)) 
 
 
Reference Document "A", Appendix 7 (Addressing Plans For Packet-Mode Data Service): 


1.1  
DTE Addressing Plan -- Introduction 
 
 
1.2  
DTE Address Characteristics 
 
 
1.3  
Address Format Selection 
 
 
1.4  
DTE Address Format 
 
 
1.4.1  
X.121 DTE Address Format 
 
 
1.4.1.1 
AES DTE Addresses 
 
 
1.4.1.2 
Public-Switched Packet Data Network (PSPDN) DTE Addresses 
 
 
1.4.2  
ATN DTE Address Format 
 
 
1.5  
Addressing Plan Administration 
 
Reference Document "A", Appendix 10 (ISO 8208 Interworking Function): 


NOTE: 
The AES-relevant portions of the sections listed below are applicable as noted, including the numbered but untitled 
Sections not explicitly listed. 
 
1 
 
Introduction (all subsections) 
 
 
2 
 
Architecture (all subsections) 
 
 
3 
 
Logical Channels (all subsections) 
 
 
4 
 
ISO 8208 IWF Operations (title only) 
 
 
4.1  
IWF Activation and Restart Procedures (title only) 
 
 
4.1.1  
AES IWF Inactive State (all subsections) 
 
 
4.1.2  
NOT APPLICABLE (GES IWF Inactive State) 
 
 
4.1.3  
Procedure at Log-on (4.1.3.1, 4.1.3.3) 
 
 
4.1.4  
Procedure at Log-off (4.1.4.1, 4.1.4.3, 4.1.4.4) 
 
 
4.1.5  
Restart Procedure (all subsections) 
 
 
4.2  
Connection Establishment Procedure (title only) 
 
 
4.2.1  
(IWF in Active State) 
 
 
4.2.2  
IWF Procedure -- Call Initiated by the Local DTE (all subsections) 
 
 
4.2.3  
IWF Procedure -- Call Initiated by the Remote DTE (all subsections) 
 
 
4.3  
Connection Release Procedure (title only) 
 
 
4.3.1  
IWF Procedure -- Call Cleared by the Local DTE/DCE (all subsections) 
 
 
4.3.2  
IWF Procedure -- Call Cleared by the Remote DTE/DCE (all subsections) 
 
 
4.4  
Data Transfer and Expedited Data Transfer Procedures (title only) 
 
 
4.4.1  
Data Transfer Procedure (all subsections) 
 
 
4.4.2  
NOT APPLICABLE (Receipt Confirmation Procedure) 
 
 
4.4.3  
Interrupt Procedure (Expedited Data Transfer Procedure) (all subsections) 
 
 
4.5  
Reset Procedure (all subsections) 
 
 
4.6  
Flow Control (all subsections) 
 
 
4.7  
SN-Primitive Construction Rules 
 
 
4.7.1  
(SN-Primitives/Parameters and Packets/Fields Relationships) 
 
 
4.7.2  
(General Transparent Mapping of Packet Fields to SN-Primitive Parameters) 
 
 
4.7.3  
DTE Addresses (all subsections) 
 
 
4.7.4  
NOT APPLICABLE (Receipt Confirmation Selection) 
 
 
4.7.5  
Expedited Data Selection (all subsections) 
 
 
4.7.6  
Throughput QOS Parameters (all subsections) 
 
 
4.7.7  
SNS-User Data during Connection Establishment/Release Phase (all 
subsections) 
 
 
4.7.8  
Mapping of Cause/Diagnostic Fields to Originator/Reason Parameters 
 
 
4.7.9  
Fast Select Control (all subsections) 
 
 
4.7.10 
Data Qualifier 
 
 
4.8  
Packet Construction Rules (title only) 
 
 
4.8.1  
(General Transparent Mapping of SN-Primitive Parameters to Packet Fields) 
 
 
4.8.2  
DTE Addresses (all subsections) 
 
 
4.8.3  
NOT APPLICABLE (Bit 7 in the GFI of Call Setup Packets) 
 
 
4.8.4  
Expedited Data Negotiation (all subsections) 
 
 
4.8.5  
TCN and MTCN (Throughput Class Negotiation and Minimum TCN) (all subsections) 
 
 
4.8.6  
Call/Called and Clear User Data (all subsections) 
 
 
4.8.7  
Mapping of Originator/Reason Parameters to Cause /Diagnostic fields (all subsections) 
 
 
4.8.8  
Fast Select (all subsections) 
 
 
4.8.9  
Priority (all subsections) 
 
 
4.8.10 
Data Qualifier (all subsections) 
 
 
Table 1 
Relationships Between SN-Primitives/Parameters and Packets/Fields 
 
 
Table 2.1 Actions taken by the IWF when in receipt of a Packet according to its 
Current State 
 
 
Table 2.2 Actions taken by the IWF when in receipt of a Primitive according to its 
Current State 
 
 
Figure 1 
IWF State Transition Diagram 
 
Reference Document "B", Section 9.0 (Packet Mode Data Service Requirements) 
 
9.3  
Packet-Mode Data Service Interface Requirements 
 
 
9.3.1  
Subnetwork Access Requirements 
 
 
9.3.2  
Physical and Link Layer Requirements 
 
 
9.4  
Packet-Mode Data Service Timing Requirements 
 
 
9.4.1  
Link Layer Timing Requirements 
 
 
9.4.1.1 
Pd/T-Channel Slot Assignment Response Time Requirements 
 
 
9.4.1.2 
R/T-Channel Switch-Over Timing Requirements 
 
 
9.4.1.3 
T/R-Channel Switch-Over Timing Requirements 
 
 
9.5.1  
AES Link Layer Buffer Size Requirements 
 
 
9.5.2  
AES Subnetwork Layer Buffer Size Requirements 

## 2.2.7.5 Avionics Subnetwork Interface Requirements

 
An AES employing packet-mode Data-3 service shall have the Packet Layer Protocol (PLP) interface specified in detail in Reference Document "E" (ISO 8208) for use with an HLE in an avionics subnetwork connected to the satellite subnetwork.  Section 2.2.7.5.2.1 details the ISO 8208 protocol implementation conformance. 

 
 
HLEs communicate with the SSND sublayer by means of a DTE/Data Circuit-terminating (or Communication) Equipment (DCE) interface.  The DTE contains the SSNAc functions (DTE part).  One or more DTE/DCE interfaces are provided as logical entities within the AES.  Each DTE/DCE interface is configured to connect to not more than one DTE.  That part of the AES that manages the user interface contains the DCE (reference Section 2.2.7.5.2.3). 

 
 
NOTE: 
The HLE (in addition to the incorporation of the SSNAc function) will also support additional functions.  As a minimum, the DTE incorporates an internetwork function and may also incorporate transport, session, presentation 
and application functions. 
 
The satellite subnetwork acts as a relay between the HLE and its peer(s) on the ground. The need to send user information to or receive user information from the ground is not determined in any way by the AES but by the HLEs. 

Figures 2-2 and 2-3 show the required relationships between the ISO 8208 Packets and the Subnetwork Protocol Data Units (SNPDUs) which are exchanged across the satellite link through a selected number of cases.  

 
The operation of the AES as specified in this standard assumes that the HLE does the following. 

 
a. 
Supports the operations of the DTE as specified in Reference Document "E". 
b. 
Is able to initiate, accept and terminate calls via the interface. 
c. 
Is prepared to accept error messages from the AES. 
d. 
Monitors the AES operation in case of unrecoverable error conditions and reinitializes the AES as necessary. 


FIGURE 2-4.  [RESERVED] 

## 2.2.7.5.1 Physical And Data Link Layer Requirements At The Physical And Data Link Layer Of The Hle/Aes Connection:

 
a. 
The interface shall be "bit-oriented," i.e., there shall be no restrictions on the sequence, order or pattern of the bits transferred within a packet between the HLE and the AES. 
b. 
The interface shall support the transfer of variable length network layer packets, containing an integer number of octets. 


c. 
The data link layer shall provide an undetected bit error rate consistent with the satellite subsystem performance requirements, reference RTCA DO-215A, Section 3.2.1.1.2. 

## 2.2.7.5.2 Data-3 Subnetwork Access Protocol Requirements 2.2.7.5.2.1 Iso 8208 Protocol Implementation Conformance

 
The interface between the HLE and the AES shall conform to Reference Document "E" with the following characteristics.  It shall provide for the following. 
 
 
a. 
A User Data Field (in the CALL REQUEST, DATA, CLEAR REQUEST and CALL 
ACCEPTED packets) of up to 128 bytes. 
b. 
Expedited Data Delivery, i.e., the use of INTERRUPT packets with a User Data Field of up to 32 bytes. 
c. 
Called and Calling Address Extension Facilities. 
d. 
Fast Select. 
e. 
Fast Select Acceptance. 
f. 
Throughput Class Negotiation. 
g. 
Transit Delay Selection and Indication. 
 
 
h. 
Default maximum user data field length of 128 bytes in DATA packets. 
i. 
Priority (of data on a connection). 
 
 
NOTES: 1. 
End-to-end data delivery confirmation service is not supported.  The D-bit shall be transmitted as a zero. 
 
 
2. 
Additional ISO 8208 facilities may be found necessary in the future.  These may include Minimum Throughput Class Negotiation and End-to-End 
Transit Delay Negotiation. 

## 2.2.7.5.2.2 [Reserved] 2.2.7.5.2.3 Aes Dce Operation

 
The DCE process within the AES shall function as a peer process to the DTE.  The DCE shall support the operations of the DTE with the facilities specified in Section 2.2.7.5.2.1. 
The following requirements do not include those relating to format definitions, diagnostic and cause codes, facility registration protocols (if used) and flow control on the ISO 8208 interface.  The specifications and definitions in Reference Document "E" shall apply for these cases. 

## 2.2.7.5.2.3.1 State Transitions

The DCE is defined as a state machine.  An ISO 8208 packet received from the DTE can cause state transitions, as can a packet received from the SSNIW sublayer entity.  The next state transition (if any) that occurs when the DCE receives a packet from the DTE is specified by Tables 2-3 through 2-8.  These tables are organized according to the substate hierarchy illustrated in Figure 2-5. 



r1 
 
r2 
 
r3 
 
 
p1  
p2  
p3  
p4  
p5  
p6  
p7 


d1  
d2  
d3 
g1  
g2  
f1 
 
f2 
 
i1 
 
i2 
 
j1 
 
j2 



Upon receiving a packet, the Action is classified as normal or erroneous under the entry "A =".  Normal actions, if not defined in the table itself, are defined via a parenthetical reference {e.g., (4.2)} to Reference Document "E".  The resulting state is shown under the entry "S =". 

 
State Definition 
Action When Entering State 
DCE State r1 
PACKET LAYER READY 
All SVCs are returned to the p1 State (see p1 State READY explanation), and all PVCs are returned to the d1 (FLOW CONTROL READY) State. r2 
DTE RESTART REQUEST 
The DCE returns each SVC to the p1 State (see p1 State explanation) and issues a RESTART CONFIRMATION to the DTE. r3 
DCE RESTART INDICATION 
The DCE returns each SVC to the p1 State (see p1 State explanation) and issues a RESTART INDICATION to the DTE. p1 
READY 
Release all resources assigned to SVC channel.  The correspondence between the DTE/DCE channel and the AES SSND/GES SSND channel is no longer in effect.  Note that the AES SSND/GES SSND channel may not yet be in the p1 State. p2 
DTE CALL REQUEST 
Determine if sufficient resources exist to support request; if so, allocate resources and forward ISO 8208 packet to SSNIW; if not, enter DCE CLEAR INDICATION to DTE State (p7).  Determination of resources and allocation is as defined in Reference Document "E". p3 
DCE INCOMING CALL 
Determine if sufficient resources exist to support request; if so, allocate resources and forward ISO 8208 packet to DTE; if not, send a CLEAR REQUEST packet to the SSNIW.  Determination of resources and allocation is as defined in Reference Document "E". No Action. p4 
DATA TRANSFER p5 
CALL COLLISION 
Send a CLEAR REQUEST packet to the SSNIW, corresponding to the incoming call (the DTE in its Call Collision State ignores the incoming call), and proceed with the DTE Call request. p6 
DTE CLEAR REQUEST 
Release all resources assigned to SVC channel.  Send an ISO 8208 CLEAR CONFIRMATION packet to the DTE and enter p1 State. Forward ISO 8208 CLEAR INDICATION packet to DTE. p7 
DCE CLEAR INDICATION TO DTE 
(continued) 

## 

 
State Definition 
 
Action When Entering State 
 
DCE State d1 No Action. FLOW CONTROL READY d2 RESET REQUEST BY DTE Remove DATA packets transmitted to DTE from window; discard any DATA packets that represent DTE partially transmitted M-bit sequences and discard INTERRUPT and INTERRUPT CONFIRMATION packets awaiting transfer to the DTE; reset all window counters to zero.  Send RESET CONFIRMATION packet to DTE.  Return channel to d1 State. d3 RESET INDICATION BY DCE to DTE Remove DATA packets transmitted to DTE from window; discard any DATA packets that represent partially transmitted M-bit sequences and discard INTERRUPT and INTERRUPT CONFIRMATION packets awaiting transfer to the DTE; reset all window counters to zero.  Forward RESET INDICATION packet to DTE. i1 No Action. DTE INTERRUPT READY i2 Forward INTERRUPT packet received from DTE to SSNIW. DTE INTERRUPT SENT j1 No Action. DCE INTERRUPT READY j2 Forward INTERRUPT packet received from SSNIW to DTE. DCE INTERRUPT SENT f1 No Action. DCE RECEIVE READY f2 No Action. DCE RECEIVE NOT READY g1 No Action. DTE RECEIVE READY g2 No Action. DTE RECEIVE NOT READY 

 
NOTE: 
State nomenclature in this table may differ from that used in Reference Doc "E" (ISO 8208). 

 



Received from DTE 
DCE Special Cases 
Any State Any Packet less than two bytes in length A = DIAG D = 38 Any Packet with an invalid General Format Identifier A = DIAG D = 40 Any Packet with unassigned Logical Channel Identifier A = DIAG D = 36 See Table 2-4 Any Packet with a valid General Format Identifier and an assigned Logical Channel Identifier (includes a Logical Channel Identifier of 0) 

 
If a state transition is specified, the actions taken shall be as specified in Tables 2-3 through 2-8.  In addition, the actions specified for transition to that state shall be performed as specified in Table 2-2. 

 

NOTE: 
        The state tables for the DCE and the state tables defined in Reference 
        Document "A" for the SSND are defined so that the AES functions can operate 
        simultaneously.  While asynchronous operation is a suitable implementation 
        strategy, it is not a requirement for the AES operations. 

## 2.2.7.5.2.3.2 Disposition Of Packets

Tables 2-3 through 2-8 also specify the disposition of the received packet.  When a packet is received from the DTE, the expressions in parentheses in Tables 2-3 though 2-8 specify whether the packet shall be forwarded or not forwarded to the SSNIW.  If no remark in parentheses is listed or listed as "not forwarded," then the packet shall be discarded. The ISO 8208 DCE shall either forward or not forward a packet from the SSNIW to the DTE in a manner that is compatible with ISO 8208. 

|                                               |                                        |
|-----------------------------------------------|----------------------------------------|
|                                               | DCE RESTART STATES (SEE NOTES 6 AND 7) |
| PACKET RECEIVED FROM DTE                      |                                        |
|                                               |                                        |
| PACKET LAYER                                  |                                        |
| READY                                         |                                        |
| (See Note 1)                                  |                                        |
|                                               | r1                                     |
|                                               |                                        |
| See Table 2-5                                 |                                        |
|                                               |                                        |
| Packets having a Packet Type Identifier       |                                        |
| shorter than one byte with assigned logical   |                                        |
| channel identifier (not = 0)                  |                                        |
|                                               |                                        |
| A = DIAG                                      |                                        |
| D = 36                                        |                                        |
|                                               |                                        |
| Any Packet, except RESTART,                   |                                        |
| REGISTRATION (if supported) with a            |                                        |
| logical channel identifier of 0               |                                        |
|                                               |                                        |
| See Table 2-5                                 |                                        |
|                                               |                                        |
| Packet with a Packet Type identifier that is  |                                        |
| undefined or not supported by DCE, and        |                                        |
| with assigned logical channel identifier (not |                                        |
| = 0)                                          |                                        |
|                                               |                                        |
| See Table 2-5                                 |                                        |
|                                               |                                        |
| RESTART REQUEST, RESTART                      |                                        |
| CONFIRMATION or REGISTRATION (if              |                                        |
| supported) packet with a Logical Channel      |                                        |
| Identifier not = 0                            |                                        |
|                                               |                                        |
| RESTART REQUEST                               |                                        |
|                                               |                                        |
| A = NORMAL                                    |                                        |
| (4.2) (Forward)                               |                                        |
| S = r2                                        |                                        |
|                                               |                                        |
| A = DIAG                                      |                                        |
| D = 38                                        |                                        |
|                                               |                                        |
| Packets having a Packet Type Identifier       |                                        |
| shorter than one byte and a Logical Channel   |                                        |
| Identifier equal to 0                         |                                        |
|                                               |                                        |
| A = DIAG                                      |                                        |
| D = 33                                        |                                        |
|                                               |                                        |
| Packets with a Packet Type Identifier that is |                                        |
| undefined or not supported by DCE and a       |                                        |
| Logical Channel Identifier equal to 0         |                                        |
|                                               |                                        |
| RESTART CONFIRMATION                          |                                        |
|                                               |                                        |
| A = ERROR                                     |                                        |
| S = r3                                        |                                        |
| D = 17                                        |                                        |
| (See Note 8)                                  |                                        |
|                                               |                                        |
| RESTART REQUEST OR RESTART                    |                                        |
| CONFIRMATION Packet with format error         |                                        |
|                                               |                                        |
| A = DIAG                                      |                                        |
| D = 38, 39, 81 or                             |                                        |
| 82                                            |                                        |
|                                               |                                        |
|                                               | (continued)                            |
|                                               |                                        |
|                                               |                                        |
| DTE RESTART                                   |                                        |
| REQUEST                                       |                                        |
| (See Note 4)                                  |                                        |
|                                               | r2                                     |
|                                               |                                        |
| DCE RESTART                                   |                                        |
| INDICATION                                    |                                        |
| (See Note 5)                                  |                                        |
|                                               | r3                                     |
|                                               |                                        |
| A = DISCARD                                   |                                        |
|                                               |                                        |
| A = ERROR                                     |                                        |
| S = r3                                        |                                        |
| D = 38                                        |                                        |
| (See Note 3)                                  |                                        |
|                                               |                                        |
| A = DIAG                                      |                                        |
| D = 36                                        |                                        |
|                                               |                                        |
| A = DIAG                                      |                                        |
| D = 36                                        |                                        |
|                                               |                                        |
| A = DISCARD                                   |                                        |
|                                               |                                        |
| A = ERROR                                     |                                        |
| S = r3                                        |                                        |
| D = 33                                        |                                        |
| (See Note 3)                                  |                                        |
|                                               |                                        |
| A = DISCARD                                   |                                        |
|                                               |                                        |
| A = ERROR                                     |                                        |
| S = r3                                        |                                        |
| D = 41                                        |                                        |
| (See Note 3)                                  |                                        |
|                                               |                                        |
| A = DISCARD                                   |                                        |
|                                               |                                        |
| A = NORMAL                                    |                                        |
| (4.3)                                         |                                        |
| S = r1                                        |                                        |
|                                               |                                        |
| A = DISCARD                                   |                                        |
|                                               |                                        |
| A = ERROR                                     |                                        |
| S = r3                                        |                                        |
| D = 38                                        |                                        |
|                                               |                                        |
| A = DISCARD                                   |                                        |
|                                               |                                        |
| A = ERROR                                     |                                        |
| S = r3                                        |                                        |
| D = 33                                        |                                        |
| (See Note 3)                                  |                                        |
|                                               |                                        |
| A = NORMAL                                    |                                        |
| (4.4)                                         |                                        |
| S = r1                                        |                                        |
|                                               |                                        |
| A = ERROR                                     |                                        |
| S = r3                                        |                                        |
| D = 18                                        |                                        |
| (See Note 3)                                  |                                        |
|                                               |                                        |
| A = DISCARD                                   |                                        |
|                                               |                                        |
| A = ERROR                                     |                                        |
| D = 38, 39, 81 or                             |                                        |
| 82                                            |                                        | 
DCE RESTART STATES (See Notes 6 and 7) 
PACKET RECEIVED FROM DTE 
 
PACKET LAYER READY (See Note 1) 
r1 
 
DTE RESTART REQUEST (See Note 4) 
r2 
 
DCE RESTART INDICATION (See Note 5) 
r3 REGISTRATION REQUEST Packets (See Note 2) A = NORMAL (13.1) A = NORMAL (13.1) A = NORMAL (13.1) REGISTRATION REQUEST Packets with a format error (See Note 2) A = DIAG D = 38, 39 or 82 A = ERROR D = 38, 39 OR 82 A = ERROR S = r3 D = 38, 39 or 82 (See Note 3) See Table 2-5 A = DISCARD Call Setup, Call Clearing, DATA, Interrupt, Flow Control or RESET Packet A = ERROR S = r3 D = 18 

 
NOTES: 1. 
The AES Subnetwork has no restart states.  Receipt of a RESTART REQUEST causes the DCE to respond with a RESTART CONFIRMATION.  The RESTART REQUEST packet is forwarded to the SSNIW, which issues a CLEAR request for all SVCs associated with the DTE/DCE interface. 
 
 
2. 
The use of the registration facility is optional on the DTE/DCE interface. 
 
 
3. 
The received packet is not forwarded to the SSNIW. 
 
 
4. 
If the DCE enters the r3 state, then the RESTART CONFIRMATION is not sent. 
 
 
5. 
The DCE upon entering the r3 state checks for the completion of r2 processing and issues an ISO 8208 RESTART INDICATION packet to the DTE, when the r3 state is entered via the r2 state.  If the r3 state is not entered via the r2 state, the DCE performs all of the actions normally performed when entering r2 and issues an ISO 8208 RESTART 
INDICATION to the DTE, and sends a RESTART REQUEST to the SSNIW. 
 
 
6. 
Table entries are defined as follows: A = Action to be taken, S = State to be entered, D = Diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that the received packet is to be cleared from the AES buffers. 
 
 
7. 
The number in the parentheses below an "A = NORMAL" table entry is the Section number in Reference Document "E".  The DCE shall take the same actions as the ones taken by the DTE, acting as a DCE, to perform nominal processing on the received packet. If no Section number is referenced, the normal processing is defined in the table entry. 
8. 
The error procedures consist of entering the r3 state, and sending a RESTART INDICATION to the DTE. 

 
DCE CALL SETUP AND CLEARING STATES (See Notes 5 and 6) 
Packet Received from DTE READY p1 DTE CALL REQUEST p2 DCE INCOMING CALL p3 DATA TRANSFER p4 CALL COLLISION p5; See Notes 1 and 4 DTE CLEAR REQUEST p6 DCE CLEAR INDICATION to DTE p7 See Table 2-6 A = DISCARD Packet having a Packet Type Identifier shorter than one byte A = ERROR S = p7 D = 38 A = ERROR S = p7 D = 38 See Note 2 A = ERROR S = p7 D = 38 See Note 2 A = ERROR S = p7 D = 38 See Note 2 A = ERROR S = p7 D = 38 See Note 2 See Table 2-6 A = DISCARD Packet having a Packet Type 
Identifier that is undefined or not supported by DCE A = ERROR 
S = p7 D = 33 A = ERROR 
S = p7 D = 33 See Note 2 A = ERROR 
S = p7 D = 33 See Note 2 A = ERROR 
S = p7 D = 33 See Note 2 A = ERROR 
S = p7 D = 33 See Note 2 See Table 2-6 A = DISCARD A = ERROR S = p7 D = 41 RESTART REQUEST, RESTART CONFIRMATION or REGISTRATION Packet with Logical Channel Identifier not = 0 A = ERROR S = p7 D = 41 See Note 2 A = ERROR S = p7 D = 41 See Note 2 A = ERROR S = p7 D = 41 See Note 2 A = ERROR S = p7 D = 41 See Note 2 CALL REQUEST A = DISCARD A = NORMAL (5.2.5) S = p5 A = ERROR S = p7 D = 21 See Note 2 A = ERROR S = p7 D = 23 See Note 2 A = ERROR S = p7 D = 24 See Note 2 A = ERROR S = p7 D = 25 See Note 2 A = NORMAL (5.2.2) S = p2 (Forward) see Note 7 A = DISCARD CALL ACCEPTED (See Note 7) A = ERROR S = p7 D = 20 A = ERROR S = p7 D = 21 See Note 2 A = ERROR S = p7 D = 23 See Note 2 A = ERROR S = p7 D = 25 See Note 2 A = ERROR S = p7 D = 24 See Notes 2 and 4 A = NORMAL (5.2.4) S = p4 (Fwrd)/ A = ERROR S = p7; D = 42 Notes 2 and 3 A = DISCARD CLEAR REQUEST (See Note 7) A = NORMAL (5.5.2) S = p6 A = NORMAL (5.5.2) S = p6 
(Forward) A = NORMAL (5.5.2) S = p6 
(Forward) A = NORMAL (5.5.2) S = p6 
(Forward) A = NORMAL (5.5.2) S = p6 
(Forward) A = NORMAL (5.5.4) S = p1 
(do not forward) 
(continued) 

## 

|                                  |                                                        |
|----------------------------------|--------------------------------------------------------|
|                                  | DCE CALL SETUP AND CLEARING STATES (See Notes 5 and 6) |
| Packet Received from DTE         |                                                        |
|                                  |                                                        |
| DCE INCOMING                     |                                                        |
| CALL                             |                                                        |
| p3                               |                                                        |
|                                  |                                                        |
| READY                            |                                                        |
|                                  |                                                        |
|                                  |                                                        |
| p1                               |                                                        |
|                                  |                                                        |
| DTE CALL                         |                                                        |
| REQUEST                          |                                                        |
|                                  |                                                        |
| p2                               |                                                        |
|                                  |                                                        |
| DATA                             |                                                        |
| TRANSFER                         |                                                        |
|                                  |                                                        |
| p4                               |                                                        |
|                                  |                                                        |
| CALL                             |                                                        |
| COLLISION                        |                                                        |
| p5; See Notes 1                  |                                                        |
| and 4                            |                                                        |
|                                  |                                                        |
| DTE CLEAR                        |                                                        |
| REQUEST                          |                                                        |
|                                  |                                                        |
| p6                               |                                                        |
|                                  |                                                        |
| DCE CLEAR                        |                                                        |
| INDICATION to                    |                                                        |
| DTE                              |                                                        |
| p7                               |                                                        |
|                                  |                                                        |
| CLEAR CONFIRMATION               |                                                        |
| (See Note 7)                     |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 20                           |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 21                           |                                                        |
| See Note 2                       |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 22                           |                                                        |
| See Note 2                       |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 23                           |                                                        |
| See Note 2                       |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 24                           |                                                        |
| See Note 2                       |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 25                           |                                                        |
| See Note 2                       |                                                        |
|                                  |                                                        |
| A = NORMAL                       |                                                        |
| (5.5.4)                          |                                                        |
| S = p1                           |                                                        |
| (do not forward)                 |                                                        |
|                                  |                                                        |
| See Table 2-6                    |                                                        |
|                                  |                                                        |
| A = DISCARD                      |                                                        |
|                                  |                                                        |
| DATA, Interrupt, Flow Control or |                                                        |
| Reset Packets                    |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 20                           |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 21; Note 2                   |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 22; Note 2                   |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 24; Note 2                   |                                                        |
|                                  |                                                        |
| A = ERROR                        |                                                        |
| S = p7                           |                                                        |
| D = 25; Note 2                   |                                                        |

## 

NOTES: 1. On entering the p5 state, the DCE cancels the outgoing call to the DTE, issuing a CLEAR REQUEST to the SSNIW (no CLEAR INDICATION 

is issued) and responds to incoming DTE call as appropriate with a CLEAR INDICATION or CALL CONNECTED packet. 
2. The error procedure consists of performing the actions specified when entering the p7 state (including sending a CLEAR INDICATION Packet 
to the DTE) and additionally sending a CLEAR REQUEST Packet to the SSNIW. 
3. The use of Fast Select Facility with restriction on response prohibits the DTE from sending a CALL ACCEPTED packet. 
4. The DTE in the event of a Call Collision must discard the CALL INDICATION packet received from the DCE. 
5. Table entries are defined as follows: A = Action to be taken, S = the State to be entered, D = Diagnostic code to be used in packets generated 
as a result of this action, DISCARD indicates that the received packet is to be cleared from the AES buffers. 
6. The number in parentheses below an "A = NORMAL" table entry is the Section number in Reference Document "E".  The DCE shall take the 
same actions as the ones taken by the DTE, acting as a DCE, to perform normal processing on the received packet.  If no Section number is referenced, the normal processing is defined in the table entry. 
7. If the packet is acceptable to the state of the logical channel (i.e., Action = Normal), but contains a format error or is otherwise unacceptable, 
then the DCE shall initiate a connection release procedure (diagnostic codes that may apply include 34, 38, 39, 65, 66, 67, 68, 69, 73, 77 and 
82).  If such an error is detected in states p1 or p7, the DCE does not send a CLEAR REQUEST packet to the SSNIW. 
 

|                                  |                                      |
|----------------------------------|--------------------------------------|
|                                  | DCE RESET STATES (See Notes 2 and 3) |
| Packet Received from DTE         |                                      |
|                                  |                                      |
| FLOW CONTROL READY               |                                      |
| d1                               |                                      |
|                                  |                                      |
| Packet with a Packet Type        |                                      |
| Identifier Shorter than one byte |                                      |
|                                  |                                      |
| A = ERROR                        |                                      |
| S = d3                           |                                      |
| D = 38                           |                                      |
| (See Note 1)                     |                                      |
|                                  |                                      |
| Packet with a Packet Type        |                                      |
| Identifier that is undefined or  |                                      |
| not supported by DCE             |                                      |
|                                  |                                      |
| A = ERROR                        |                                      |
| S = d3                           |                                      |
| D = 33                           |                                      |
| (See Note 1)                     |                                      |
|                                  |                                      |
| A = ERROR                        |                                      |
| S = d3                           |                                      |
| D = 41                           |                                      |
| (See Note 1)                     |                                      |
|                                  |                                      |
| RESTART REQUEST,                 |                                      |
| RESTART CONFIRMATION,            |                                      |
| or REGISTRATION (if              |                                      |
| supported) packet with Logical   |                                      |
| Channel Identifier not = 0       |                                      |
|                                  |                                      |
| RESET REQUEST                    |                                      |
|                                  |                                      |
| A = NORMAL                       |                                      |
| (8.2)                            |                                      |
| S = d2                           |                                      |
| (Forward)                        |                                      |
| (See Note 4)                     |                                      |
|                                  |                                      |
| RESET CONFIRMATION               |                                      |
|                                  |                                      |
| A = ERROR                        |                                      |
| S = d3                           |                                      |
| D = 27                           |                                      |
| (See Notes 1 and 4)              |                                      |
|                                  |                                      |
| see Table 2-7                    |                                      |
|                                  |                                      |
| A = NORMAL                       |                                      |
| (8.4)                            |                                      |
| S = d1                           |                                      |
| (Do not forward)                 |                                      |
|                                  |                                      |
| INTERRUPT OR                     |                                      |
| INTERRUPT                        |                                      |
| CONFIRMATION Packet              |                                      |
|                                  |                                      |
| DATA or Flow Control Packet      |                                      |
|                                  |                                      |
| See Table 2-8                    |                                      |
|                                  |                                      |
| REJECT supported but not         |                                      |
| subscribed to (optional)         |                                      |
|                                  |                                      |
| A = ERROR                        |                                      |
| S = d3                           |                                      |
| D = 37                           |                                      |
| (See Note 1)                     |                                      |

 
NOTES: 1. The error procedure consists of performing the specified actions when entering the d3 state (which includes forwarding a 

RESET INDICATION packet to the DTE) and sending a RESET REQUEST packet to the SSNIW. 
 
 
2. Table entries are defined as follows: A = Action to be taken, S = the State to be entered, D = the Diagnostic code to be used 
in packets generated as a result of this action, DISCARD indicates that the received packet is to be cleared from the AES buffers. 
 
 
3. The number in parentheses below an "A=NORMAL" table entry is the Section number in Reference Document "E".  The 
DCE shall take the same actions as the ones taken by the DTE to perform normal processing on the received packet. If no Section is referenced, the normal processing is defined in the table entry. 
 
 
4. If the packet is acceptable to the state of the logical channel (i.e., Action = Normal), but contains a format error, then the 
DCE shall initiate a connection reset procedure (diagnostic codes that may apply include 38, 39, 81 and 82).



RESET REQUEST by DTE 
RESET INDICATION by 
 
DCE to DTE 
d2 
d3 A = DISCARD A = ERROR S = d3 D = 38 (See Note 1) A = DISCARD A = ERROR S = d3 D = 33 
(See Note 1) A = DISCARD A = ERROR S = d3 D = 41 (See Note 1) A = DISCARD A = NORMAL (8.3) S = d1 (Do not forward) A = ERROR S = d3 D = 28 (See Note 1) A = DISCARD A = ERROR S = d3 D = 28 (See Note 1) A = DISCARD A = ERROR S = d3 D = 28 
(See Note 1) A = DISCARD A = ERROR S = d3 D = 37 (See Note 1) 
|                          |                    |
|--------------------------|--------------------|
| Packet Received From DTE |                    |
| DTE INTERRUPT READY      | DTE INTERRUPT SENT |
| i1                       | i2                 |
|                          |                    |
| INTERRUPT                |                    |
| (See Note 1)             |                    |
|                          |                    |
| A = NORMAL               |                    |
| (6.8.2)                  |                    |
| S = i2                   |                    |
| (Forward)                |                    |
|                          |                    |
| A = ERROR                |                    |
| S = d3                   |                    |
| D = 44                   |                    |
| (See Note 4)             |                    |
|                          |                                                                                                 |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Packet Received From DTE |                                                                                                 |
| DCE INTERRUPT READY      | DCE INTERRUPT SENT                                                                              |
| j1                       | j2                                                                                              |
|                          |                                                                                                 |
| INTERRUPT                |                                                                                                 |
| CONFIRMATION             |                                                                                                 |
| (See Note 1)             |                                                                                                 |
|                          |                                                                                                 |
| A = ERROR                |                                                                                                 |
| S = d3                   |                                                                                                 |
| D = 43                   |                                                                                                 |
| (See Note 4)             |                                                                                                 |
|                          |                                                                                                 |
| A = NORMAL               |                                                                                                 |
| (6.8.3)                  |                                                                                                 |
| S = j1                   |                                                                                                 |
| (Forward)                |                                                                                                 |
|                          |                                                                                                 |
| NOTES:                   | 1. If the packet is acceptable to the state of the logical channel (i.e., Action = Normal), but |

contains a format error, then the error procedure applies (See Note 4). 

 
2. Table entries are defined as follows: A = Action to be taken, S = the State to be entered, D 

= the Diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that the received packet is to be cleared from the AES buffers. 
 
3. The number in parentheses below an "A=NORMAL" table entry is the Section number in 
Reference Document "E".  The DCE shall take the same actions as the ones taken by the DTE to perform normal processing on the received packet. If no Section is referenced, the normal processing is defined in the table entry. 
4. The error procedure consists of performing the specified actions when entering the d3 
state (which includes forwarding a RESET INDICATION packet to the DTE) and sending a RESET REQUEST packet to the SSNIW. 

 
DCE FLOW CONTROL TRANSFER STATES 
(See Notes 1, 2 and 3) 
Packet Received From DTE 
 
 
DCE RECEIVE READY 
DCE RECEIVE NOT READY 
f1 
f2 DATA packet with invalid PR A=ERROR S=d3 D=2 (See Note 4) A=ERROR S=d3 D=2 (See Note 4) DATA packet with valid PR but invalid PS 
or User Data Field with improper format A=DISCARD 
 (Process PR data) A=ERROR 
 S=d3 
 D=(See Note 5) (See Note 4) A=DISCARD (Process PR data) DATA packet with valid PR but with M-bit set to 1 and the D-bit set to 0 when the User Data Field is partially full, or the D- bit set to 1 A=ERROR S=d3 D=165 or 166 (See Note 4) DATA packet with valid PR, PS and User Data Field with proper-Format A=NORMAL (Forward) A=DISCARD (Process PR data) (See Note 6) 
 
DCE FLOW CONTROL TRANSFER STATES 
(See Notes 1, 3 and 4) 
Packet Received From DTE 
 
 
DTE RECEIVE READY 
DTE RECEIVE NOT READY 
g1 
g2 RR, RNR, or REJECT packet with an invalid PR A=ERROR S=d3 D=2 (See Note 4) A=ERROR S=d3 D=2 (See Note 4) RR packet with a valid PR (See Note 7) A=NORMAL (7.1.5) A=NORMAL (7.1.5) S=g1 RNR packet with a valid PR (See Note 7) A=NORMAL (7.1.6) A=NORMAL (7.1.6) S=g2 REJECT packet with a valid PR (optional) (See Note 7) A=NORMAL (13.4.2) A=NORMAL (13.4.2) S=g1 
 

## Table 2-8.  Dte Effect On Flow Control Transfer States (Continued)

NOTES: 
1. 
The RR, RNR, and REJECT procedures are a local DTE/DCE matter and the 
corresponding packets are not forwarded to the SSNIW. 
 
 
2. 
Table entries are defined as follows: A = Action to be taken, S = the State to be 
entered, D = the Diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that the received packet is to be cleared from the AES buffers. 
3. 
The number in parentheses below an "A=NORMAL" table entry is the Section 
number in Reference Document "E".  The DCE shall take the same actions as the ones taken by the DTE to perform normal processing on the received packet. If no Section is referenced, the normal processing is defined in the table entry. 
4. 
The error procedure consists of performing the specified actions when entering the 
d3 state (which includes forwarding a RESET INDICATION packet to the DTE) and sending a RESET REQUEST packet to the SSNIW. 
5. 
The diagnostic codes are as follows: D=1 for invalid PS; D=39 for a User Data 
Field greater than 128 Bytes; D=82 for a User Data Field not octal aligned. 
6. 
If possible, the DCE should process these packets normally.  On the other hand, the 
DCE may define an internal mechanism to indicate that valid DATA packets have been discarded during a receive-not-ready condition.  In this case, when the receive-not-ready condition clears, the DCE should reset the logical channel, forwarding both a RESET INDICATION packet to the DTE (D = #0, no additional information) and a RESET REQUEST packet to the SSNIW. 
7. 
For RR, RNR or REJECT packets, the presence of one or more octets beyond the 
third octet is considered an error.  Although a valid P(R) may be accepted to update the status of outstanding DATA packets, the DCE shall invoke the ERROR 
procedure, as defined in Note 5 (with D = 39). 
 
Table 2-10.   [Reserved] 
 
Table 2-11.   [Reserved] 
 
Table 2-12.   [Reserved] 
 

## 2.2.7.5.2.3.3 Diagnostic And Cause Codes

 
 
The tables for certain conditions indicate a diagnostic code that is to be included in the packet that is generated when entering the state indicated.  The term "D =" defines the diagnostic code.  When "A = DIAG" appears in a table entry, the action taken is to generate an ISO 8208 DIAGNOSTIC packet and transfer it to the DTE; the diagnostic code indicated defines the entry in the diagnostic field of the packet.  Bit 8 of the cause field of any packet type is always set to 0, indicating that the condition was recognized by the ISO 8208 interface. 

## 2.2.7.5.2.3.4 Dce Timer

 
Under certain circumstances, the DTE must respond to a packet issued from the DCE within a given time. 
Table 2-13 covers these circumstances and the actions that the DCE shall initiate upon the expiration of that time. 

## 2.2.7.6 Join And Leave Event Requirements

 
An AES employing Data-3 packet-mode data service shall provide Join and Leave event messages to the aircraft routing function to indicate that the air/ground data link is either available or not available, respectively. The Join/Leave messages shall include sufficient information for the routing function to determine the address(es) of the DTE(s) attached to the log-on GES. 

 
 
NOTE: 
This may be accomplished, for example, by passing the GES/satellite ID from the AES to the routing function containing a lookup table for translation to DTE address(es), or by passing the DTE address(es) directly from the AES to the routing function. 

## 

|                         | Start Event    |               | Normally    |         |
|-------------------------|----------------|---------------|-------------|---------|
| Design                  |                | terminated by |             | expires |
| Time                    |                |               |             |         |
| Limit                   |                |               |             |         |
| Value                   |                |               |             |         |
| tN10                    | 60 sec         | DCE issues a  |             |         |
| RESTART                 |                |               |             |         |
| INDICATION              |                |               |             |         |
| packet                  |                |               |             |         |
| Reception of RESTART    |                |               |             |         |
| CONFIRMATION or         |                |               |             |         |
| RESTART REQUEST         |                |               |             |         |
| packet                  |                |               |             |         |
| DCE enters the r1 state |                |               |             |         |
| and may issue           |                |               |             |         |
| DIAGNOSTIC packet       |                |               |             |         |
| (D=#52)                 |                |               |             |         |
| tN11                    | 180 sec        | DCE issues an |             |         |
| INCOMING CALL           |                |               |             |         |
| packet                  |                |               |             |         |
| Reception of CALL       |                |               |             |         |
| ACCEPTED or CLEAR       |                |               |             |         |
| REQUEST or CALL         |                |               |             |         |
| REQUEST packet          |                |               |             |         |
| DCE enters the p7 state |                |               |             |         |
| signaling a CLEAR       |                |               |             |         |
| INDICATION packet       |                |               |             |         |
| (D=#49) (see note)      |                |               |             |         |
| Receipt of RESET        |                |               |             |         |
| CONFIRMATION or         |                |               |             |         |
| RESET REQUEST packet    |                |               |             |         |
| tN12                    | 60 sec         | DCE issues a  |             |         |
| RESET                   |                |               |             |         |
| INDICATION              |                |               |             |         |
| packet                  |                |               |             |         |
| DCE enters the p7 state |                |               |             |         |
| signaling a CLEAR       |                |               |             |         |
| INDICATION packet       |                |               |             |         |
| (D=#51) (see note)      |                |               |             |         |
| Reception of a CLEAR    |                |               |             |         |
| CONFIRMATION or         |                |               |             |         |
| CLEAR REQUEST packet    |                |               |             |         |
| tN13                    | 60 sec         | DCE issues a  |             |         |
| CLEAR                   |                |               |             |         |
| INDICATION              |                |               |             |         |
| packet                  |                |               |             |         |
| DCE enters the p1 state |                |               |             |         |
| and may issue a         |                |               |             |         |
| DIAGNOSTIC packet       |                |               |             |         |
| (D=#50)                 |                |               |             |         |

 
 
NOTE: The clear is extended to the satellite subnetwork; i.e., the DCE shall issue a CLEAR 
REQUEST packet to the SSNIW. 

## 2.2.8 Circuit-Mode Service Requirements (Optional)

 
Circuit-mode voice and/or data are optional services which may be provided by the AES. The AES may provide voice communications capability to the cockpit and/or the passenger cabin areas.  Circuit-mode voice shall be provided in AESs fitted with ICAO AMSS SARPs service Levels 3 and 4 (see Section 1.2.3).  Circuit-mode data service, which provides a basic data channel to support a variety of communication applications that require the allocation of dedicated channel capacity for the duration of a call (such as interactive or bulk data, encrypted voice/data and facsimile), may optionally be provided in AESs fitted for the same service levels. 
The minimum requirements for circuit-mode voice service on the satellite subnetwork, if such service is provided by an AES, shall be the minima specified for the AES in Reference Document "A", Section 6.0 and Appendices 4 and 5; in Reference Document "B", Section 10.0 and Annex 2; and in Reference Documents "C" and "G", including all referenced tables, figures, annexes and appendices applicable to the AES.  These are identified in the following listings. 
 
The requirements of the preceding paragraph mandate the use of specific proprietary vocoders.  Alternative vocoder implementations may be used if and only if they demonstrate equivalent performance and interoperability.  "Equivalent performance" of an alternative vocoder is defined as demonstrated performance which is statistically equivalent to that of the standard vocoder described in this MOPS.  The alternative vocoder shall demonstrate this performance when interoperating with itself, the specified vocoder, and all other vocoders operating at the same bit-rate and approved for AMS(R)S operation under this MOPS. 

## Reference Document "A", Section 6.0 (Telephone Services):



Version 
 
 
6 
 
Telephone Services 
 
 
6.1  
General 
 
 
6.1.1  
Quality Objectives 
 
 
6.1.2  
NOT APPLICABLE (Network Coordination Station (NCS) 
Function) 
 
 
6.1.3  
Ground-to-Air Calls 
 
 
6.1.4  
Air-to-Ground Calls 
 
 
6.1.5  
NOT APPLICABLE (Passenger Telephony Operation) 
 
 
6.1.6  
Crew Voice Operation 
 
 
6.3  
Long-Term Channel Management 
 
 
6.4  
Short-Term Channel Management 
 
 
6.5  
Call Setup, Air-to-Ground 
 
 
6.5.1  
Channel and Power Availability Check 


1.45 
 
 
6.5.2  
Call Setup Events -- Description and Sequence 
 
 
6.5.2.1 
(Initial Request) 
 
 
6.5.2.2 
("Other" GES Call Transactions) 
 
 
6.5.2.3 
(Channel Allotment) 
 
 
6.5.2.4 
(Channel Assignment) 
 
 
6.5.2.5 
("Other" GES Channel Assignment) 
 
 
6.5.3  
Call Setup to "Other" GES 
 
 
6.5.4  
NOT APPLICABLE (GES Call Setup Decision Criteria) 
 
 
6.5.5  
Call Termination Events -- Description and Sequence 
 
 
6.6  
Call Setup, Ground-to-Air 
 
 
6.6.1  
Channel and Power Availability Checks 


1.45 
 
 
6.6.2  
Call Setup Events -- Description and Sequence 
 
 
6.6.2.1 
(Call Announcement) 
 
 
6.6.2.2 
(Signaling Sequences) 
 
 
6.6.2.3 
NOT APPLICABLE (GES Processes) 
 
 
6.6.3  
NOT APPLICABLE (GES Call Setup Decision Criteria) 
 
 
6.6.4  
Call Termination Events -- Description and Sequence 
 
 
6.7  
Power Control 
 
 
6.7.1  
Power Control Management 


1.45 
 
 
6.7.2  
AES and GES Requirements for Measuring BER 
 
 
6.7.3  
NOT APPLICABLE (GES Process/Power Control Decision 
Table) 
|                  |     | 6.7.4     | NOT APPLICABLE (GES Process/Power Control Operation    |
|------------------|-----|-----------|--------------------------------------------------------|
| -- Forward Link) |     |           |                                                        |
|                  |     | 6.7.5     | Power Control Operation -- Return Link                 |
|                  |     | 6.7.7     | NOT APPLICABLE (GES Power Management Mechanism)        |
|                  |     | 6.8       | Interworking with Telephone Networks                   |
|                  |     | 6.9       | Voice Coding                                           |
|                  |     | 6.9.1     | Voice Coding at 9.6 kbit/s and 4.8 kbit/s              |
|                  |     | 6.9.1.1   | Coding Algorithm                                       |
|                  |     | 6.9.1.2   | NOT APPLICABLE (Speech Detection Function)             |
|                  |     | 6.9.1.3   | Noise Insertion                                        |
|                  |     | 6.10      | NOT APPLICABLE (Multiplexed Voice Channels)            |
|                  |     | 6.11      | NOT APPLICABLE (Supplementary Signaling Capability)    |

 
For all figures (including SDL and SUs) associated with the above requirements, see the cross-reference in Reference Document "B", Annex 1. 

## Reference Document "A", Appendix 5.0 (Aeronautical Numbering And Addressing):

 
 
1 
 
Public Correspondence Numbering Plan Introduction 
 
 
2 
 
Numbering Considerations 
 
 
2.1  
AES Identification Scheme 
 
 
2.2  
International Public Network Numbering Plan 
 
 
2.3  
INMARSAT Aero Mobile Numbering Scheme 
 
 
3 
 
INMARSAT Mobile Number Format 
 
 
4 
 
Numbering Plan Administration 

 
 
Reference Document "B", Section 10.0 (Circuit-Mode Service Requirements): 



Version 
 
 
10.2.1  
Circuit-Mode Telephony Service Requirements 
 
 
10.3.1  
NOT APPLICABLE (Example of Circuit-Mode Service 


Interface Signaling Requirements) 
 
 
10.4.1  
C-Channel Assignment Response Time Requirements 
 
 
10.4.2  
C-Channel Release Response Time Requirements 
 
 
10.4.3  
C-Channel Acknowledgement Response Time Requirements 
 
 
10.4.4  
EIRP Adjustment 
 
 
10.4.5  
Voice/Circuit-Mode Data Delay  


1.19 
 
 
10.5   
AES Buffer Size Requirement Circuit-Mode Services 
Signaling 

 
Reference Document "B" Section 12 CODEC Technical Parameters: 



Version 
 
 
12.2.1 
Frequency Response and Gain (Decoder) 


1.20 
 
 
12.2.2 
Spectral Distortion (Decoder) 


1.20 
 
 
12.2.3 
Delay (Decoder) 


1.20 
 
 
12.2.4 
Noise and Crosstalk  


1.20 
 
 
12.3.1 
Frequency Response and Gain (Encoder) 


1.20 
 
 
12.3.2.1 
Non Random Signal  


1.20 
 
 
12.3.2.2 
Random Signal  


1.20 
 
 
12.3.3 
Delay (Encoder) 


1.20 
 
 
12.3.4 
Noise and Crosstalk  


1.20 
 
 
12.3.5 
Voiced/Unvoiced Errors 


1.20 

 
 
Reference Document "B", Annex 1 (Module 1 Cross Reference Tables) 
 
Table CR5.1 
Circuit Mode Services 
 
Reference Document "B", Annex 2 (End-to-End Voice Interface Specification [for BTRL 9.6 kbps Speech Codec]): 
 
I 
 
Overall Telephony Baseband Requirements 

|     |     | II    |     | Attenuation/Frequency Response                      |
|-----|-----|-------|-----|-----------------------------------------------------|
|     |     | III   |     | Total Distortion, Including Quantization Distortion |
|     |     | IV    |     | Idle Channel Noise                                  |
|     |     | V     |     | Spurious In-Band Signals                            |

 
 
VI 
 
Spurious Out-of-Band Signals 
 
 
VII  
Amplitude Jitter 
 
 
VIII  
Phase Jitter 
 
Reference Document "C": 
 
Preface 
 

|                                        |     |   1  |     | General (Section 1.1 only)                                   |
|----------------------------------------|-----|------|-----|--------------------------------------------------------------|
|                                        |     |   2  |     | General Introduction to Multipulse-Excited Linear Predictive |
| Coding (LPC)  (including all Sections) |     |      |     |                                                              |
|                                        |     |   3  |     | Multipulse-Excited LPC Encoding (including all Sections)     |
|                                        |     |   4  |     | Parameter Transmission (including all Sections)              |
|                                        |     |   5  |     | The Decoder (including all Sections)                         |

 
 
Reference Document "G": 

 
 
Preface 
AMBE High Level Vocoder Description 
 
 
1.1  
Scope 
 
 
1.2  
Introduction 
 
 
1.3  
Multi-Band Excitation Speech Model 
 
 
1.4  
Speech Coder - Overview 
 
 
1.5  
Aero Speech Coder - Advanced Features 
 
 
1.6  
Speech Input/Output Requirements 
 
 
1.7  
Vocoder Implementation 

## 2.2.8.1 Priority, Precedence And Preemption

Signaling and system management actions for circuit-mode calls in either the airoriginated or ground-originated direction shall be queued and processed within the AES in an order corresponding to each call's Circuit-mode Priority as listed in Table 2-14, with the lower Circuit-mode Priority numbers having the higher precedence.  The lowest priority in-progress call shall be interrupted immediately if necessary to make AES resources (e.g., HPA power, channel unit, vocoder) available for a higher-priority call of Circuit-mode Priority 1, 2, or 3, of either air or ground origination.  If the new groundoriginated call has the same or lower priority as the lowest-priority call in progress, then the AES shall indicate "busy" to the GES. 

If AES resources are not available for a voice call of circuit-mode priority 1, 2, or 3, due to queued or ongoing packet-mode traffic of packet-mode Priority (Q Number) less than the Q Number corresponding to the circuit-mode call priority listed in Table 2-14, and the AES resources could be made available by interrupting that Packet-mode traffic or suspending its processing, then those resources shall be immediately cleared and made available for the call and its associated signaling.  Such preemption shall not apply to the sole, primary packet-mode data channel unit controlling the AES.  (See also Section 2.2.4.2.8.) 

 

## Table 2-14.   Circuit-Mode Priority Structure

| Application (Voice/Data)            | Circuit-   |
|-------------------------------------|------------|
| Mode                                |            |
| Priority                            |            |
| Packet Data                         |            |
| Mapping                             |            |
| (see Note)                          |            |
| Q-Number                            |            |
| (Link Layer                         |            |
| Precedence)                         |            |
| Distress, Urgency                   | 1          |
| Direction Finding, Flight Safety    | 2          |
| Other Safety & Regularity of Flight | 3          |
| 4                                   | 3, 2, 1, 0 |
| & Public Communications             |            |

 
NOTE: 
 
Packet data mapping shows the priority relationship if packet data 
(refer to Table 2-1) is used on a circuit mode channel. 

## 2.2.8.2 Cockpit Services Interworking Requirements

 
The AES shall implement procedures for interworking between the cockpit (e.g., Control/Display Unit (CDU) and "call lamp/chime" and "microphone switch" discretes where used) and the satellite subnetwork protocol, as required, for the provision of cockpit voice service.   The basic interworking  procedures between the AES and the cockpit audio control system (Audio Management (or Control) Panel (AMP or ACP)) are shown in Figures 2-6 through 2-9.  Although the figures show steady call lamps and singlestroke chimes, flashing lamps and/or multistroke chimes may optionally be used. 

## 2.2.8.2.1 Call Establishment -- Air To Ground

 
A call may be initiated via a CDU by means of manufacturer-specific user menus.  Call initiation may also optionally require activation of the microphone switch. 
 
 
The cockpit enters the conversation mode by activating the microphone switch.  This is normally done after the call has been connected and annunciated but may optionally occur as part of the call initiation phase as stated above. 
 
  

## 2.2.8.2.2 Call Establishment -- Ground To Air

 
Ground-to-air calls are handled largely by the AMP with little involvement of the CDU. However, the AES may provide call progress information to the CDU (e.g., priority, etc.). 
Receipt of the Call Announcement SU triggers the interworking process at the AES.  The AES determines if the call is for the cockpit by analysis of the called-terminal information element within the signal unit.  A called-terminal value of zero indicates that no routing information is present and that the call should be routed according to priority (e.g., non-
public correspondence calls to the cockpit AMS, public correspondence calls either rejected or routed to cabin telephone).  The lamp/chime annunciation occurs once as soon as the satellite voice channel has been assigned and its continuity verified. 


 
The cockpit activates the microphone switch to the "on" state to indicate answer of the incoming call; this may optionally be signaled from the CDU.  The AES recognizes the answer signal and sends the Connect SU to the GES. 
Call lights and chimes should be inhibited during take-off and landing flight phases. 

## 2.2.8.2.3 Call Termination

 
For air-initiated call clearing, the cockpit indicates the end of call by use of an End Call control on the CDU.  The end of call may optionally be indicated by the microphone switch.  The AES disconnects the voice channel and sends a series of channel release signal units to the GES to clear the satellite channel. 
For ground-initiated call clearing, a channel release signal unit from the satellite channel causes the AES to disconnect the voice channel.  If a microphone switch (latched for the duration of the call) has been optionally used for call initiation and answering, it must be switched off before the call lamp can be extinguished. 

## 2.2.8.2.3.1 Call Termination By Cross Talk Detection

 
An AES shall always compare the AES ID and Application Reference Number fields in the received sub-band SUs (excluding fill-in SUs) against the expected values. The expected values are established during the call set-up phase. In the event of either or both received values being different from the expected ones, the AES shall immediately clear the call and shall immediately inhibit the C-channel transmitter until the call is fully cleared unilaterally by the AES. 
2.2.9 
Recovery from Primary Power Interruption 
The AES equipment shall conform to the following requirements after encountering primary power interruptions from any cause. 
 
a. 
Power interruptions of less than five milliseconds duration shall be indistinguishable from outages in the RF transmission path of equal duration. 
 
b. 
Power interruptions from five to 200 milliseconds duration shall require no more than five seconds recovery time, beginning from when primary power has been restored.  Recovery is defined as automatically returning to the previous operating state (without user intervention) such that voice and data channels 
resume in the same configuration they were in before the power interruption occurred.  This assumes a P-channel signal with at least the minimum quality characteristics specified in Section 2.2.4.1.2. 

 
 
NOTE: 
In-transit data service packets which have been acknowledged on either the DTE or DCE interface, but not yet transferred to the opposite interface, may be lost.  Non-AES higher-layer entities that employ end-to-end acknowledgement protocols may choose to retransmit such lost data.  Synchronization and RF output power may be lost during the power interruption and recovery time.  
There shall be no more than a momentary effect on cockpit displays. 

## 2.2.10 Failure/Status Indication

 
The AES equipment shall provide, independent of any operator action, an indication of: 
 
a. 
Failure of AES equipment resulting in loss of data communications. 
 
b. 
Failure of AES equipment resulting in loss of voice communications. 

## 2.3 Equipment Performance -- Environmental Conditions 2.3.1 General Requirements

 
The environmental tests and their associated performance requirements described in this Section are intended to provide a laboratory means of determining the electrical and mechanical performance of the equipment under environmental conditions representative of those that may be encountered in actual aircraft operations. 

 
Unless otherwise specified, the test procedures applicable to a determination of equipment performance under environmental test conditions are contained in RTCA Document DO- 160C, *Environmental Conditions and Test Procedures for Airborne Equipment*.  General information regarding the use of the procedures in RTCA/DO-160C is contained in Sections 1.0 through 3.0 of that document.  Also, a method of identifying which environmental tests were conducted and other amplifying information on the conduct of the tests is contained in Appendix A of RTCA/DO-160C. 
Some of the minimum performance requirements in Section 2.2 of this MOPS are not required to be qualified to all of the conditions contained in RTCA/DO-160C.  Judgment and experience have indicated that these particular performance parameters are not susceptible to certain environmental conditions and that the level of performance specified in Section 2.2 will not be measurably degraded by exposure to these conditions. 
Certain environmental tests contained in this Section are identified by the phrase "when required."  These tests need not be performed unless the manufacturer wishes to qualify the equipment for that particular environmental condition.  If the equipment is to be qualified to a particular environmental condition, then these "when required" tests shall be performed. 

## 2.3.2 Equipment Configurations

 
 
This MOPS contains provisions to subject different AES configurations to environmental qualification.  Specific AES performance tests have been included for use in conjunction with the environmental procedures of RTCA/DO-160C.  These tests are a subset of the full AES performance tests contained in Section 2.4 of this MOPS.  Normally, a MOPS does not provide specific equipment performance tests to be used in conjunction with the environmental procedures of RTCA/DO-160C.  However, the large number of performance tests in Section 2.4 indicates that a test procedure that includes all of the performance tests combined with the appropriate environmental procedures would be impractical.  The AES qualification conforms to RTCA/DO-160C.  RTCA/DO-160C shall be used when running the test sequence. 

## 2.3.3 Configuration Control

 
Nominal environment testing, followed by extreme environment testing, shall be conducted on the AES with the Operational Flight Program (OFP) installed according to the correct software version number as specified in the AES configuration documentation. 
 
Table 2-15 is a compliance matrix that cross-references the RTCA/DO-160C environmental test requirements with the performance requirements.  

## 2.3.4 Specific Environmental Test Conditions

 
The equipment shall be subjected to the test conditions as specified in RTCA/DO-160C, in the sections identified in Table 2-15, the conformance matrix. By performing (and passing) those tests, the corresponding requirements of this standard shall be met. 



Num eric entrie s in the tables are refere nces to both the RTC
A/D
O-
160C 
sectio n as well as to a specif ic note.  
An X 
desig nates an  
pli ca bl e R
T
C
A/
D
O-
16
0C 
se cti on
; 
ref er to se cti on lis tin g for sp eci fic no tes
. 

ap A
nt en na Su bs yst e m 
 
 
a.  

## Cti On Function

 
Se
2.

2
.

3
.

7
A
n t e n n a
 
S
w i t c h i n g
 
T
i m e
(
1
)
(
1
)
(
1
)
2.

2.

3.

2 
2
.

3
.

8
B
e a m
 
S
w i t c h i n g
 
T
i m e
(
1
)
(
1
)
(
1
)
(
1
2.

2.

2. 2. 2. 2.

## 

 
b.  Receiver Subsystem 
 
RTCA/DO-160C SECTION 
 
Section 
Function 
4 
5 
6 
7 
8 
15 16 17 18 19 20 21 22 2.2.4.1.2 
Receiver Sensitivity 
X 
- 
X 
- 
X 
- 
- 
- 
- 
- 
X 
- 
X 
 
2.2.4.1.3 
Image and Spur. Response Rejection 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.4 
Rej. of Signal Outside Rcv Band 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.5 
Receiver Linearity 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.6 
Desired Signal Dynamic Range 
X 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.7.1 
Tuning Range and Chnl Increments  
X 
- 
X 
- 
- 
- 
- 
- 
X 
X 
X 
- 
- 
 
2.2.4.1.7.2 
Channel Numbering 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.8 
Capture Range 
X 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.9 
Doppler Rate 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.11.1 
BER Performance (P-Channel) 
(19) - 
- 
- (19) - (21) - 
- 
- 
- 
- 
- 
 
2.2.4.1.11.2 
Time to Acquire Superframe Lock 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.12.1 
BER Requirements (C-Channel) 
(19) - 
- 
- (19) - (21) - 
- 
- 
- 
- 
- 
 
2.2.4.1.12.2 
Bit Timing Recovery 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.12.3 
Frame Lock Acquisition, Probability 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.12.4 
Maintaining Bit Synchronization 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 
2.2.4.1.12.5 
Channel BER Measure. Accuracy 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
c.  Transmitter Subsystem 
 
RTCA/DO-160C SECTION 
 
Section 
Function 
4 
5 
6 
7 
8 
15 16 17 18 19 20 21 22 2.2.4.2.1 
Channel Rates and Tolerances 
(18) - 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
2.2.4.2.2 
Output Power 
X 
- 
X 
- 
- 
X 
X 
X 
X 
X 
X 
- 
X 
2.2.4.2.3 
Output Power Adjustment 
X 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
2.2.4.2.4 
Output Power Stability 
X 
X 
- (17) - 
- 
X 
- 
- 
- 
- 
- 
- 
2.2.4.2.5 
Harmonics, Spur., and Noise Density 
(18) - 
X 
- 
X 
- 
- 
- 
- 
- 
- 
- 
X 
2.2.4.2.6 
Intermodulation Products 
(18) - 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
2.2.4.2.7 
Carrier Off Level 
X 
- 
X 
- 
- 
- 
- 
X 
X 
X 
X 
- 
X 
2.2.4.2.8 
Transmitter/Channel Muting 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
2.2.4.2.9 
Load VSWR Capability 
(18) - 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
2.2.4.2.10.1 
Tuning Range and Chnl Increments 
(18) - 
X 
- 
- 
- 
- 
X 
X 
X 
X 
- 
- 
2.2.4.2.10.2 
Channel Numbering 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
2.2.4.2.11 
Tuning Stabilization Time 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
2.2.4.2.12 
Phase Noise 
(18) - 
- 
- 
X 
- (20) - 
X 
X 
- 
- 
X 
2.2.4.2.13 
Frequency Accuracy 
(18) X 
X 
- 
X 
- 
X 
- 
- 
- 
- 
- 
- 
2.2.4.2.14 
Doppler Correction 
- 
- 
- 
- 
- 
- 
- 
X 
X 
X 
X 
- 
- 
2.2.4.2.15 
Doppler Rate Capability 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
2.2.4.2.16 
Signal Spectrum 
(18) - 
- 
- 
X 
- 
- 
- 
X 
X 
X 
- 
X 
2.2.4.2.17.1 
Pulse-Shaping Filter Resp. (R/T-Chnl) 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
2.2.4.2.18.1 
Pulse-Shaping Filter Resp. (C-Chnl) 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
 

(continued) 

## Table 2-15.   Performance *Versus* **Test Requirement Matrix**  (Continued) Do-160C Sections Applicable To The Aes: 4.0 Temperature And Altitude (See Note 1)

4.5.1 
Ground Survival Low Temperature Test and Operating Temperature Test 
4.5.2 
Ground Survival High Temperature Test and Short-Term Operating High Temperature Test 
4.5.3 
Operating High Temperature Test 
4.5.4 
In-flight Loss of Cooling Test (See Note 16) 
4.6.1 
Altitude Test (See Note 18) 
4.6.2 
Decompression Test (See Note 3) 
4.6.3 
Overpressure Test (See Note 3) 
5.0 
Temperature Variation 
6.0 
Humidity 
7.0 
Shock 
7.2 
Operational Shock (See Note 17) 
7.3 
Crash Safety Test (See Note 4) 
8.0 
Vibration 
9.0 
Explosion Proofness (See Note 3) 
10.0 
Waterproofness (See Note 3) 
10.3.1 
Drip Proof Test (See Note 3) 
10.3.2 
Spray Proof Test (See Notes 3, 5) 
10.3.3 
Continuous Stream Test (See Notes 3, 5) 
11.0 
Fluids Susceptibility (See Notes 3, 6) 
11.4.1 
Spray Test (See Note 3) 
11.4.2 
Immersion Test (See Note 3) 
12.0 
Sand and Dust (See Note 3) 
13.0 
Fungus Resistance (See Note 3) 
14.0 
Salt Spray (See Note 3) 
15.0 
Magnetic Affect 
16.5.1 
Normal Operating Conditions (AC) (See Notes 7, 12, 13) 
16.5.2 
Normal Operating Conditions (DC) (See Notes 7, 12, 13) 
16.5.3 
Abnormal Operating Conditions (AC) (See Notes 7, 12) 
16.5.4 
Abnormal Operating Conditions (DC) (See Notes 7, 8, 12) 
17.0 
Voltage Spikes (See Note 9) 
17.3 
Category A 
17.4 
Category B 
17.4.1 
Intermittent Transients 
17.4.2 
Repetitive Transients 
18.0 
Audio Frequency Conducted Susceptibility - Power Inputs 
19.0 
Induced Signal Susceptibility 
20.0 
Radio Frequency Susceptibility (Radiated and Conducted) (See Notes 10, 11) 
21.0 
Emission of Radio Frequency Energy 
22.0 
Lightning Induced Transient Susceptibility (See Note 14) 
23.0 
Direct Lightning Strike (See Note 15) 
24.0 
Icing Conditions 

## Table 2-15.   Performance Versus Test Requirement Matrix  (Continued)

 NOTES: 
1. 
Due to the difficulties in performing radiating measurements while changing the 
environmental conditions of the antenna, acceptable alternative test procedures may be implemented.  Portions of the antenna subsystem may be measured over the operating environmental conditions range.  The measurement data thus obtained may be used in an analysis to show that the specified antenna performance can be achieved under all operating environmental conditions. This analysis shall include the effects of materials and construction of the individual radiating elements and account for the effects of beam pointing errors versus environmental conditions on other specification requirements within the declared coverage volume. 
2. 
Performance parameters of the antenna subsystem will not be measured during these environmental tests.  These environmental tests are for survivability and apply only to equipment which is mounted on the outside of the aircraft. 
3. 
These tests are not listed for the receiver and transmitter subsystems and need not be performed unless the manufacturer wishes to qualify the equipment for the particular environmental condition. 
4. 
The application of the Crash Safety Shock test may result in damage to the equipment under test.  Therefore, this test may be conducted after the other tests have been completed. In this case, Section 2.1.7, "Effects of Test" does not apply. 
5. 
This test shall be conducted with the spray directed perpendicular to the equipment. 
6. 
Applicable requirements: 
 
a. 
At the end of the 24-hour exposure period, the equipment shall function. 
 
b. 
Following the two-hour operation period at ambient temperature after the 160-hour exposure period at elevated temperature, the performance requirements shall be met. 
7. 
The appropriate test will depend upon whether the equipment is AC or DC powered. 
8. 
The application of the Low Voltage Conditions (DC) (Category B equipment) test may result in damage to the equipment under test.  Therefore, this test may be conducted after the other tests have been completed.  Section 2.1.7, "Effects of Test," does not apply. 
9. 
Select Category A (high degree of protection against voltage spikes required) or Category B (lower standard of protection acceptable) as applicable for the equipment under test. 
10. Excluding frequency to which receiver is tuned and the response within its resonant pass 
band. 

## Table 2-15.   Performance Versus Test Requirement Matrix  (Continued) Notes:  (Continued) 11. Equipment Is Not Required To Meet Performance Specifications During The Application Of

HIRF, (Category U, 20 v/m).  The equipment must meet all requirements following the application. 
12. Meet requirements of DO-160C except as noted by Section 2.2.9. 
13. Phase Noise (Section 2.2.4.2.12) performed under normal conditions only. 
14. Equipment is not required to meet performance specifications during the period of 
application of the Lightning Induced Transient test, but must meet all requirements following the test. 
15. Not required for AMSS. 
16. Applicable to equipment requiring cooling.  Modify test length to three hours.  Verify no 
smoke or fire; compliance to performance specifications not required. 
17. During operational shock testing, measure maximum output stability only. 
18. Altitude tests, 4.6.1, not applicable;  not applicable to receiver tests. 
19. Gaussian only; not multipath. 
20. Steady state conditions only (16.5.1.1 and 16.5.3.1, or 16.5.2.1 and 16.5.4.1, as applicable). 
21. Notes 19 and 20 apply. 

## 2.4 Equipment Performance Verification Procedures

 
The following procedures provide guidelines for tests to ensure compliance with the MOPS 
performance requirements.  Alternative procedures or analyses providing equivalent performance documentation may be used, and if so they shall be accompanied with detailed documentation of the method used.  Therefore, the procedures cited herein should be used as one criterion in evaluating acceptability of the alternate procedures. 

 
Except for Section 3.4.5, these are not required flight tests.  Any reference to "flight tests" in documents referenced herein should be ignored. 
The transceiver frequency, power, and certain other functional parameters are controlled by commands over a P channel received by the transceiver in the 1.5 GHz band from a GES Emulator.  The transceiver must be receiving this P channel before a transceiver transmit signal can be generated. 
For performance verification, this document divides the transceiver into two parts: the Antenna Subsystem (Section 2.4.3), and the Transceiver Subsystem (Section 2.4.4); the latter of which includes the Receiver as defined by Section 2.2.4.1 and the Transmitter as defined by Section 2.2.4.2. 
Some of the following tests may require additional test equipment not shown in the test setup figures.  Such equipment would be associated with the interface between the GES Emulator and the transceiver receiver input. 

## 2.4.1 Special Cooling Requirements

 
The manufacturer shall specify any special cooling requirements for any of the specified tests. 

## 2.4.2 Warm-Up And Stabilization Requirements

 
Unless otherwise specified, all tests shall be conducted after a minimum equipment warmup period of not less than five minutes.  In addition, the frequency reference source shall have completed its warm-up cycle, if any, and any power-on self test(s) shall have been completed prior to testing. 

## 2.4.3 Antenna Subsystem Test Requirements

 
The following tests, or equivalent, are designed to verify that the Antenna Subsystem meets the specifications stated in Section 2.2.3 for both low gain and high gain antennas. 

## 2.4.3.1 Test Conditions 2.4.3.1.1 Antenna Under Test

 
The Antenna Subsystem under test shall include any beam steering unit, control unit or other electronics considered part of the installed Antenna Subsystem but not the LNA/diplexer.  If a radome forms part of the antenna, this shall also be installed during the measurements.  The antenna test installation shall also include any adapter plates, where used, or other hardware used to interface the antenna to the fuselage in a flight installation. 

 
In the case of multiple antenna installations which are normally located at different areas of the aircraft (e.g. two side-mounted antennas), one antenna may be tested at a time.  The overall coverage may then be calculated as noted in section 3.0, (INSTALLED EQUIPMENT PERFORMANCE), taking into account the locations and angular displacement of the antennas on the aircraft. 

## 2.4.3.1.2 Test Frequencies

 
Antenna Subsystem measurements shall be performed at a minimum of six frequencies: 

|     |     |     | Test Frequency     |     |    Receive     |            |   Transmit    |
|-----|-----|-----|--------------------|-----|----------------|------------|---------------|
|     |     |     |                    |     |                |            |               |
|     |     |     | Lower Band-Edge    |     | 1530.0 MHz     |            | 1626.5 MHz    |
|     |     |     | Mid-Band           |     |                | 1545.0 MHz |               |
|     |     |     | Upper Band-Edge    |     | 1559.0 MHz     |            | 1660.5 MHz    |

 
These represent the Lower and Upper Band-Edge and Mid-Band test frequencies of the receive and transmit bands.  Frequency accuracy shall be within +/- 0.5 MHz. 

## 2.4.3.2 Required Test Equipment 2.4.3.2.1 Standard Test Equipment

 
Testing shall be performed in accordance with the Institute of Electrical and Electronics Engineers (IEEE) Std 169, 1983.  It is suggested that an antenna test range with a minimum path length of 14 meters (40 ft) be used having a reflectivity level less than or equal to -25 dB within a quiet zone containing the antenna under test and ground plane.  "Compact ranges" and/or near-field probing techniques may also be employed if analysis shows that an equivalent accuracy may be obtained. 

 
Other items of standard test equipment are: 

- Range instrumentation including a 2-axis (minimum) positioner, positioner 
controller, L-band transmitter, receiver, pattern recorder and polarization measurement instrumentation. 


- Reference RHCP or linearly-polarized, standard-gain antenna, with gain 
calibration traceable to National Institute for Standards and Technology (NIST) or other national standards. 
 
Components of the receive and transmit systems are necessary to perform system level verifications in conjunction with the antenna system verifications.  These include, but are not limited to, the following components or their equivalent: 



- LNA 


- Diplexer 


- High Power Amplifier 


- High Power Relay, if used. 

## 2.4.3.2.2 Special Test Equipment

 
Antenna Ground Plane: An antenna ground plane shall be used to simulate the conductive mounting surface on the intended aircraft.  The ground plane shall extend at least 0.5 m beyond any active portion of the antenna under test, and extend beyond any radome employed.  The ground plane should be curved to simulate the radius of curvature of the portion of the aircraft in which it is intended  to mount the antenna.  Where the antenna is to be installed on an aircraft with a radius of curvature which differs by more than 20% from that used in the antenna tests, or the ground plane differs from the specified size, validity of the results shall be justified by analysis and/or measurement. 

Antenna Test Set: This unit shall convert the antenna position outputs into the format normally used to steer the antenna under "open-loop" steering conditions.  Thus, as the antenna is rotated on the positioner, the correct beam direction shall be selected to keep the beam aligned with the source.  A "composite" radiation pattern will result. 

 
 
NOTE: 
The advantages of this form of measurement are that it enables composite gain plots to be obtained automatically, and that the final gain plots will include the same errors due to beam selection, misalignment, hysteresis, etc., as would be experienced in an installed airborne system. 
Where closed-loop steering is used, the gain plots shall be corrected by analysis and/or measurement to include these additional errors. 
The beam-steering conditions during the pattern and VSWR testing of the antenna shall recognize the independence from carrier frequency as required in this full-duplex operation. 

## 2.4.3.3 Detailed Performance Verification Procedures 2.4.3.3.1 Antenna Gain And Coverage Volume (Section 2.2.3.2) 2.4.3.3.1.1 High-Gain Antenna (Sections 2.2.3.1.2 And 2.2.3.2.1) Or Intermediate Gain Antenna (Section 2.2.3.2.3)

 
Equipment Required 
Antenna Measurement Range - refer also to Section 2.4.3.2.1. 
 
Antenna Ground Plane - refer to Section 2.4.3.2.2. 
 
Antenna Test Set - refer to Section 2.4.3.2.2. 
 
Diplexer/LNA. 
 
Antenna-Diplexer/LNA interconnect coaxial cable with 0.3 dB insertion loss. 
Measurement Requirements 
 
With the equipment set up as in Figure 2-10, measure the antenna gain Ga with a RHCP 
source, or equivalent, of axial ratio not greater than 1.1 referenced to true RHCP isotropic gain, by substituting the calibrated standard gain antenna.  Obtain the antenna gain values for a minimum of 5000 points evenly distributed in solid angle throughout a region corresponding to the upper hemisphere above the aircraft, excluding the lowest 5 degrees above the horizon. 

 
 
NOTE: 
These are not necessarily beam-pointing directions, but are points in space 
selected for this measurement. 
The declared coverage volume shall contain only points which are within the minimum and maximum gain as specified in Section 2.2.3.2.1. 
 
 
NOTE: 
Coverage volume includes factors in addition to gain. 

## 2.4.3.3.1.2 Low-Gain Antenna (Sections 2.2.3.1.2 And 2.2.3.2.2)

 
Equipment Required 
Antenna Measurement Range - refer to Section 2.4.3.2.1. 
 
Antenna Ground Plane - refer to Section 2.4.3.2.2. 
 
Antenna Test Set - refer to Section 2.4.3.2.2. 
 
Diplexer/LNA. 
 
Antenna-Diplexer/LNA interconnect coaxial cable with 0.3 dB insertion loss. 

 
NOTE: 
For a low-gain antenna which is purely passive, there is no requirement for the antenna test set and associated electronics. 
Measurement Requirements 
 
With the equipment set up as in Figure 2-10, measure the antenna gain Ga with a RHCP 
source, or equivalent, of axial ratio not greater than 1.1 referenced to true RHCP isotropic gain, by substituting the calibrated standard gain antenna.  Obtain the antenna gain values for a minimum of 3000 points that are evenly distributed in solid angle throughout a region corresponding to the upper hemisphere above the aircraft, excluding the lowest 5 degrees above the horizon. 

 
 
NOTE: 
These are not necessarily beam-pointing directions, but are selected points in 
space for this measurement. 
The declared coverage volume shall contain only points which are  within the minimum and maximum gain as specified in Section 2.2.3.2.2. 
 
 
NOTE: 
Coverage volume includes factors in addition to gain. 

## 2.4.3.3.1.3 Antenna Gain-To-Noise Temperature Ratio (Section 2.2.2.1)

 
CAUTION: 
THIS TEST REQUIRES CLEAR-SKY RADIATION OF RF ENERGY AND MAY REQUIRE AUTHORIZATION FROM GOVERNMENT AGENCIES AND RELEVANT SATELLITE OPERATORS. 

The antenna gain and coverage volume requirements for either high- or low-gain antennas are to be satisfied by demonstrating that the overall AES system G/T requirement of Section 2.2.2.1 over the coverage volume as defined in Section 2.2.3.2.1 is met.  In order to specify this in terms of antenna G/T at the single RF port of the antenna, it is necessary to assign a value for the noise temperature of the receiver subsystem at this port.  This value is 185.77 K and is derived from receiver subsystem testable requirements and installation requirements, as detailed in Appendix B. 

In this G/T test, first the antenna noise temperature is measured within 1 MHz of the Lower, Mid-Band, and Upper Band-Edge Receiver Test Frequencies given in Section 2.4.3.1.2.  Then the receive band G/T is calculated using these temperatures together with the antenna gain values measured per the procedures in Sections 2.4.3.3.1.1 and 2.4.3.3.1.2. 

 
Equipment Required 
Antenna Ground Plane - refer to Section 2.4.3.2.2. 
 
Diplexer/LNA. 
 
Antenna-Diplexer/LNA interconnect coaxial cable with 0.3 dB maximum loss. 
 
Noise Figure Meter (HP 8970B or equivalent). 
 
Noise Source (HP 346C or equivalent). 
 
Test Cable, loss 0.3 dB or less. 
 
RF Power Source (capable of maximum RF power for this test). 

## Measurement Requirements

 
The objective is to simulate as far as is practicable the sky noise environment experienced in operating conditions.  The following conditions shall apply when performing antenna noise temperature measurements: 

 
 
a. 
The antenna is viewing a clear-sky condition, with a site that offers minimum obstruction of sky visibility over the upper hemisphere; 
 
b. 
If a radome is to be installed as part of the antenna, it is installed during the measurements; 
 
c. 
The antenna is mounted on the ground plane and positioned relative to the Earth in a manner that simulates nominally horizontal level aircraft flight; 
 
d. 
The ambient temperature is in the range 290 + 30 K, where (0 C = 273.16 K); and 
 
e. 
The Noise Source and Noise Figure Meter are operating within the temperature range for which their calibration is valid. 
Measurement Procedure 
Step 1: 
As shown in Figure 2-11, connect the HP346C Noise Source to the (test equipment) Diplexer/LNA cable input using the Test Cable, connect the Diplexer/LNA output to the HP8970B Noise Figure Meter, and record the ambient temperature at the antenna, load, and noise source, TC.  If the RF Source is used for a diplexer transmit load, assure that it remains turned off during this test. 
Step 2: 
Preset the HP8970B by pressing the "Preset" button. 
Step 3: 
Press "Increment" three times to increase the averaging from one sample to eight samples for smoothing.  Press "Frequency" and enter the Lower Band-Edge receive test frequency by pressing "1530" on the numeric keypad followed by "Enter".  Press "1.0" followed by the special function key "SP" to set up the test for measurement without an external oscillator. 
Step 4: 
Press "14.4 SP" to turn on the noise source, and "62 SP" and "72 SP" to hold the RF and IF attenuators during the measurement. 
 
 
Record the value displayed on the far-right display, which is proportional to 
power in decibels.  This value is PH. 

                       To measure PH and PC: ┌──────────────┐    ┌──────────────┐    ┌────────┐    ┌─────────────┐ │    Noise     │    │ Diplexer/LNA │    │ Cable  │    │    Noise    │  
     │    Figure    ├<───┤ Rcv      Ant ├<───│ 0.3 dB ├<───┤    Source   │ │    Meter     │    │        Xmt   │    │max loss│    │             │ └──────┬───────┘    └──────────┬───┘    └────────┘    └──────┬──────┘ │                       ^                             ^ │            ┌──────────┴───┐                         │ │            │   RF Power   │                         │ │            │ Source (Off) │                         │ │            │   or Load    │                         │ │            └──────────────┘                         │ │                                                     │ └─────────────────────────────────────────────────────┘ ----------------------------------------------------------------------------- 
                        To measure PA: ┌──────────────┐    ┌──────────────┐    ┌────────┐    ┌─────────────┐ │    Noise     │    │ Diplexer/LNA │    │ Cable  │    │   Antenna   │ │   Figure     ├<───┤ Rcv      Ant ├<───┤ 0.3 dB ├<───┤    Under    │ │    Meter     │    │        Xmt   │    │max loss│    │     Test    │ └──────────────┘    └─────────┬────┘    └────────┘    └─────────────┘ ^ ┌─────────┴────┐ │   RF Power   │ │    Source    │ │     (On)     │ └──────────────┘ 
NOTE:   Transmissions must be made only in accordance with 

 
              applicable Government regulations 

 

## Figure 2-11.  Noise Temperature (Antenna Gain And Coverage) -- Section 2.4.3.3.1.3



Press "14.3 SP" to turn off the noise source.  Record the value for coldsource power, which is PC.  Calculate 


(1) 
Y1 = PH - PC. 


Convert this dB value to a numerical factor and record it for use in equation (6). 
  
 
 
Disconnect the HP346C Noise Source and attach the antenna output (for a low-gain antenna) or output of the single RF port of the Antenna Subsystem (for a high-gain or intermediate-gain antenna) to the Diplexer/LNA. 
  
 
 
Connect the RF power source to the transmit port of the Diplexer/LNA. Ensure that the source is tuned either to the Mid-Band transmit frequency per Section 2.4.3.1.2 or such frequency as may be coordinated with authorities and 
operators, and that there is a CW power level at the single RF port of the antenna in accordance with Section 2.2.4.2.2. 


 
 
 
For the HGA or IGA, measurements shall be made for beam selections corresponding to all combinations of: 

 
 
 
- 
azimuth angles of 45º, 90º, and 135º. 
 
  
 
 
- 
elevation angles from 5º to 90º elevation in steps no greater than 5º 

 
 
 
Note:  These measurements approximate the worst case system noise 
temperatures. 

 
 
 
For the LGA, repeated measurements may be made to average-out measurement noise. 

 
 
 
Record the value on the far-right display on the Noise Figure meter for each 
measurement.  These values are defined as PA.  From these values, calculate 

 


(2) 
Y2 = PC - PA. 

 
 
 
Convert this dB value to a numerical factor and record it for use in equation (7). 

 
 
 
Repeat Steps 1 and 4 to obtain PH, PC, and PA at the nearest 1 MHz increment 
to the Mid-Band and Upper Band-Edge receive test frequencies. 

 
 
 
In the following analysis, the test receiver noise temperature and the antenna noise temperature are calculated from the basic definitions of the "Y" factors: 

 


(3) 
Y1 = (TH + TR)/(TC + TR) 

 


(4) 
Y2 = (TC + TR)/(TA + TR) 

 
 
 
Calculate the system noise temperature in the following manner.  Use the 
recorded ambient temperature for TC.  Find the value for TH using: 
 
 
(5) 
TH = To[10ENR/10 - 1] 

 
 
where T0 is 290K and ENR is the Excess Noise Ratio of the noise 
source. 

 
 
 
Calculate the test receiver noise temperature TR referred to its input, derived 
from Equation (3), as follows: 

 


(6) 
TR = (TH - Y1TC)/(Y1 - 1) 

 
 
 
Calculate the antenna noise temperature TA1, derived from Equation (4), as 
follows: 
 
  


(7) 
TA1 = [TC + TR(1 - Y2)]/Y2 
 
 
Step 5: 
For the HGA or IGA, TA1 shall be corrected for temperature by calculating the 
internal dissipation loss of the antenna by means of the expression: 


(8) 
L = (TC - TSKY)/(TC - TA1) 

 


where: 


L represents the (unmeasurable) internal dissipation loss of the HGA or IGA, as a value > 1. 

 


TSKY is the external noise temperature, assumed to be 100K for this 
calculation. 

 


TA1 values are obtained from Equation (7). 

 
 
 
From these values for L, corrected values of TA1 may be obtained by using a value of 290K for TC and substituting these values into Equation (9): 

 


(9) 
TA2 = TSKY/L + 290(1 - 1/L) 

 


where TA2 are temperature-corrected values for the corresponding TA1 
values. 


Step 6: 
For the HGA or IGA, the values obtained for TA2 in Step 5 for all azimuth 
angles and frequencies shall be used to derive the coefficients for a single 
third-order function of TA versus the sine of the elevation angle thus: 


(10) TA3 = X0 + X1sin() + X2sin2() + X3sin3() 


where  = elevation angle. 


A least-squares analysis shall be used to derive these coefficients. 


Step 7: 
The AES system gain-to-noise temperature ratio (G/T)AES is determined from 
four elements:  the transceiver sensitivity as verified to the requirements of Section 2.2.4.1.2, expressed as effective noise temperature (see Note in Section 2.2.4.1.2); the antenna gain as verified to the requirements of Section 2.2.3.2; the antenna noise temperature as determined in Step 6 above; and the loss of the antenna RF coaxial cable (Section 2.2.2.1, Item "h"). 


(G/T)AES is calculated as: 
 
 
(11) (G/T)${}_{\rm Al(s)}$(dB) = G${}_{\rm A}$(dB) - 10${}^{\circ}$LOG${}_{\rm J0}$[T${}_{\rm A}$ + T${}_{\rm J}$(L${}_{\rm d}$ - 1) + L${}_{\rm J}$T${}_{\rm R}$]


where: 


GA is the Antenna Subsystem gain (from Section 2.4.3.3.1); 


TA is the noise temperature of the antenna, either TA3 from Step 6 above for an HGA or IGA, or the single averaged value of TA1 obtained in Step 
4 for an LGA; 


TR is the noise temperature of the Transceiver Subsystem from Section 
2.4.4.2.2 and the Note in that section, which indicates that TR  should be 
limited to TR < 451 - 298 = 153 K.  TR = 153 K should be used for this 
calculation; 


TI is the temperature of the antenna cable, 290 K should be assumed for 
this calculation; 


LI is the loss of the antenna cable, assumed to be 0.3 dB for this 
calculation, as a numerical quantity: 


LI = 10[Loss(in dB)/10] 


See Appendix B for further development of G and T parameters. 


For the HGA or IGA, the values for GA and TA to be used are the gain values from Section 2.4.3.3.1 at the single RF port of the antenna for GA, and the TA3 
values at the corresponding elevation angles from the temperature-corrected curve of Step 6 for all points. 


For the LGA, the single averaged value for TA1 obtained in Step 4 should be 
used. 


Step 8: 
Verify that the values of (G/T)AES obtained from this procedure meet the 
requirements of Section 2.2.2.1. 

## 2.4.3.3.2 Axial Ratio (Section 2.2.3.3) 2.4.3.3.2.1 High-Gain Or Intermediate Gain Antenna (Section 2.2.3.3.1)

 
Equipment Required 
Antenna Measurement Range - refer to Section 2.4.3.2.1. 
 
Antenna Ground Plane - refer to Section 2.4.3.2.2. 
 
Antenna Test Set - refer to Section 2.4.3.2.2. 
Measurement Requirements 
 
Connect the equipment as shown in Figure 2-11.  Measure the axial ratio for each of the points designated during the tests in Section 2.4.3.3.1.1.  Points where the values do not exceed the requirement of Section 2.2.3.3.1 are eligible for inclusion in coverage volume. 

 
Measured pointing directions where the axial ratio exceeds the requirement may be included in coverage volume if the measured gain (Gmeas) in that direction exceeds the minimum value per Section 2.2.3.2.1 (Greqd) by at least a compensating amount (Gcomp) per the table below.  Points which should not be excluded from coverage volume because of axial ratio are those where: 



Gmeas  Greqd + Gcomp  (in dB) 

 
                          NOTE: 
                                            
                                                    This compensation is presented in the following tables based on 
                                                    calculations using the Friis power transmission formula, while assuming 
                                                    that both AES and satellite antennas are nominally RHC polarized, as 
                                                    follows:  



Gc = 20log10[(r0 + r1)/(r1 + 1)] - 20log10 [(r0 + r2)/(r2 + 1)] 


where: 


r0  is the satellite antenna axial ratio 


r1 is the AES antenna reference axial ratio, and 


r2 is the AES antenna actual (voltage) axial ratio 
 
Using this Friis formula for RHCP, the reference axial ratio for high-gain antennas (per Section 2.2.3.3.1, 6 dB, a factor of 1.995), and a satellite antenna axial ratio worst-case assumption of 2.5 dB (a factor of 1.334), the Gcomp values for high-gain antennas corresponding to the measured axial ratio values are: 



AES RHCP Axial Ratio 
      Gain Compensation, Gcomp 


6.0 dB 


0.00 dB 


7.0 dB 


0.07 dB 


8.0 dB 


0.13 dB 


9.0 dB 


0.19 dB 


10.0 dB 


0.25 dB 


11.0 dB 


0.30 dB 


12.0 dB 


0.35 dB 


13.0 dB 


0.40 dB 


14.0 dB 


0.45 dB 


15.0 dB 


0.49 dB 


20.0 dB 


0.66 dB 


100.0 dB  


0.92 dB 

 
 
NOTE: 
As an example, if axial ratio at a point is 13 dB and the gain at that point is 12.40 dB or greater, that point should not be excluded from coverage volume 
because of axial ratio. 

## 2.4.3.3.2.2 Low-Gain Antenna (Section 2.2.3.3.2) Equipment Required

 
Antenna Measurement Range - refer to Section 2.4.3.2.1. 
 
Antenna Ground Plane - refer to Section 2.4.3.2.2. 
 
Antenna Test Set - refer to Section 2.4.3.2.2. 
 
 
NOTE: 
For a low-gain antenna which is purely passive, there is no requirement for the antenna test set and associated electronics. 

 
Measurement Requirements 
 
Connect the equipment as shown in Figure 2-11.  Measure the axial ratio for each of the points designated during the tests in Section 2.4.3.3.1.2.  Points where the values do not exceed the requirement of Section 2.2.3.3.2 are eligible for inclusion in coverage volume. 

Measured pointing directions where the axial ratio exceeds the requirement may be included in coverage volume if the measured gain (Gmeas) in that direction exceeds the minimum value per Section 2.2.3.2.2 (Greqd) by at least a compensating amount (Gcomp) per the table below.  Points which should not be excluded from coverage volume because of axial ratio are those where: 



Gmeas  Greqd + Gcomp  (in dB) 
 
Using the Friis formula for RHCP (per Note, Section 2.4.3.3.2.1) the reference axial ratio for low-gain antennas (per Section 2.2.3.3.2, 20 dB, a factor of 10.000), and a satellite antenna axial ratio worst-case assumption of 2.5 dB (a factor of 1.334), the Gcomp values for low-gain antennas corresponding to the measured axial ratio values are: 



AES RHCP Axial Ratio 
Gain Compensation, Gcomp 

 20.0 dB  


0.00 dB 

 21.0 dB  


0.03 dB 

 22.0 dB  


0.05 dB 

 23.0 dB  


0.07 dB 

 24.0 dB  


0.09 dB 

 25.0 dB  


0.11 dB 

 30.0 dB  


0.17 dB 

 35.0 dB  


0.21 dB 

 40.0 dB  


0.23 dB 

 45.0 dB  


0.24 dB 

 50.0 dB  


0.25 dB 

100.0 dB  


0.26 dB 
 

 
NOTE: 
As an example, if the axial ratio at a point is 25 dB and the gain at that point is 0.11 dB or greater, that point should not be excluded from coverage volume 
because of axial ratio. 

## 2.4.3.3.3 Pattern Discrimination - High Gain Antenna (Section 2.2.3.4.1) Or Intermediate Gainantenna (Sections 2.2.3.4.2.1 And 2.2.3.4.2.2)

 
Equipment Required 
Antenna Measurement Range - refer to Section 2.4.3.2.1. 
 
Antenna Ground Plane - refer to Section 2.4.3.2.2. 
 
Antenna Test Set - refer to Section 2.4.3.2.2. 
Measurement Requirements 
 
Connect the equipment as shown in Figure 2-10.  Choose and measure the patterns of a minimum of 10 beams, five evenly distributed over the declared coverage and five at the expected worst-case discrimination points as identified by the manufacturer through simulation or measurement.  Sufficient points over the antenna pattern shall be obtained to determine that the requirements are satisfied. 

## 2.4.3.3.4 Voltage Standing Wave Ratio (Section 2.2.3.5)

 
Equipment Required 
Ground Plane - refer to Section 2.4.3.2.2. 
 
Automatic Network Analyzer (Hewlett-Packard 8753, 8720, 8510, or equivalent). 
 
Antenna Test Set (needed for High Gain or Intermediate Gain Antennas only). 
Measurement Requirements 
 
Connect the equipment as shown in Figure 2-12.  For all antennas, measure the VSWR at the single RF port of the antenna subsystem.  For high-gain or intermediate-gain antennas, measure the VSWR for a minimum of 10 beams evenly distributed over the declared coverage. 

 
Precautions should be taken to reduce the effects of nearby reflections on the VSWR measurements. 
 

 
                 Antenna Under Test                             
               ┌───────────────────┐        Ground Plane       
     ══════════╧══╤══════╤═════════╧════════════════════════      
                  └─┬──┬─┘                                        
                    ^  │                                          
                    │  │ <──── RF Cable                   
                    │  │                                          
                    │  │   ┌────────────┐    ┌───────────┐        
                    │  │   │ Automatic  │    │    Pen    │        
                    │  └─>─┤  Network   ├──>─┤  Plotter  │        
                    │      │  Analyzer  │    │ (optional)│        
                    │      └────────────┘    └───────────┘        
     Control ─────> │                                             
     Cable          │                                             
                    │                                             
            ┌───────┴───────┐                                     
            │    Antenna    │                                     
            │   Test Set    │      <-  HGA or IGA only            
            └───────────────┘                                     
 

## Figure 2-12.  Voltage Standing Wave Ratio (Vswr) -- Section 2.4.3.3.4 2.4.3.3.5 Phase Discontinuity - High Gain Antenna (Section 2.2.3.6.1) Or Intermediate Gain Antenna (Section 2.2.3.6.2)

 
Equipment Required 
Antenna Measurement Range - refer to Section 2.4.3.2.1. 
 
Antenna Ground Plane - refer to Section 2.4.3.2.2. 
 
Antenna Test Set - refer to Section 2.4.3.2.2. 
Measurement Requirements 
 
Connect the equipment as shown in Figure 2-10.  In a beam-switched antenna, position the antenna at a switchover point (the point where at least one phase shifter changes state) between two adjacent beams.  Measure the phase difference by switching between these two beams and recording the difference in phase of the carrier.  Compliance to the requirement may be demonstrated by analysis which is verified by measured data. 

## 2.4.3.3.6 Antenna Switching Time (Multiple Antennas) (Section 2.2.3.7)

 
Equipment Required 

 
Signal source. 
 
Detector(s). 
 
Switch driver. 
 
Storage oscilloscope (Tektronix 2232 or equivalent). 

## Measurement Requirements

 
Connect the equipment as shown in Figure 2-13.  Apply a test signal to the common RF terminal of the switching device.  Monitor the signal at all output terminals on a storage oscilloscope.  The antenna switching time is the elapsed time from a steady state at one output terminal to a steady state at another output terminal.  All possible switch combinations shall be verified. 

 
                     common 
                    terminal 
      ┌──────────────┐     ┌──────────────┐    ┌──────────┐ 
      │   Signal     │     │  RF Switch   │    │ Switch   │ 
      │   Source     ├────>┤  under test  ├<───┤ Driver   │ 
      └──────────────┘     │              │    └──────────┘ 
                           └───┬──────┬───┘ 
                               │      │ output 
                               │      │ terminals 
                               v      v 
                           ┌───┴──────┴───┐ 
                           │   Storage    │ 
                           │ Oscilloscope │ 
                           └──────────────┘ 
 

## Figure 2-13.  Antenna Switching Time -- Section 2.4.3.3.6 2.4.3.3.7 Beam Switching Time (Section 2.2.3.8) Equipment Required

 
Antenna Test Set - refer to Section 2.4.3.2.2. 
 
L-band signal generator. 
 
Storage oscilloscope. 
 
L-band RF detector. 
 
Source antenna. 
Measurement Requirements 
 
Connect the equipment as shown in Figure 2-14.  Measure the duration of the RF signal outage at the mid-band frequencies for transmit and receive when the antenna is switched between adjacent beams.  Where it can be justified by measurement or analysis, the switching time of only the phase-shifter portions of the antenna may be measured. 

 

 
       ┌───────────┐       ┌───────────┐                 
       │ Source    │       │  Antenna  │   ┌───────────┐ 
       │ Antenna   ├<─────>┤ under test├──>┤  Detector │ 
       └─────┬─────┘       └─────┬─────┘   └─────┬─────┘ 
             ^                   ^               │        
             │                   │               v         
       ┌─────┴─────┐       ┌─────┴─────┐   ┌─────┴────────┐  
       │  Signal   │       │  Antenna  │   │ Oscilloscope │  
       │ Generator │       │ Test Set  │   │              │  
       └───────────┘       └─────┬─────┘   └─────┬────────┘  
                                 │   trigger     ^        
                                 └───────────────┘ 
 

## Figure 2-14.  Beam Switching Time -- Section 2.4.3.3.7 2.4.3.3.8 Pointing Response Time - (Section 2.2.3.9) Equipment Required

 
Antenna Test Set - refer to Section 2.4.3.2.2. 
 
Source Antenna. 
 
Signal Generator (Fluke 6082A or equivalent). 
 
Spectrum Analyzer (HP 8566B or equivalent). 
Measurement Requirements 
 
Connect the equipment as shown in Figure 2-15.  Adjust the antenna under test to an elevation angle equal to the lowest angle within the coverage volume, and the combination of antennas for maximum coupling.  Set the spectrum analyzer to the Mid-Band receive frequency in the zero frequency span mode.  With the signal generator operating on the Mid-Band receive frequency, adjust the generator output and the spectrum analyzer to provide a convenient display on the spectrum analyzer.  Record the analyzer amplitude value for reference. 

 
Adjust the antenna under test so the azimuth pointing direction is reversed, + 10 degrees, and the elevation is at 90 degrees.  Set the spectrum analyzer to triggered mode.  Command the Antenna Test Set to return to the initial position, triggering the spectrum analyzer sweep.  Measure the time from the command to the point where the receiver signal amplitude meets the requirements of Section 2.2.3.9. 

 
       ┌───────────┐       ┌───────────┐           
       │ Source    │       │  Antenna  │           
       │ Antenna   ├<─────>┤ under test├─────────┐ 
       └─────┬─────┘       └─────┬─────┘         │ 
             ^                   ^               │ 
             │                   │               v 
       ┌─────┴─────┐       ┌─────┴─────┐   ┌─────┴───────┐ 
       │  Signal   │       │  Antenna  │   │  Spectrum   │ 
       │ Generator │       │ Test Set  │   │  Analyzer   │ 
       └───────────┘       └─────┬─────┘   └─────┬───────┘ 
                                 │   trigger     ^         
                                 └───────────────┘         
 

## Figure 2-15.  Pointing Response Time -- Section 2.4.3.3.8 2.4.3.3.9 Power Handling (Section 2.2.3.10) Equipment Required

 
Environmental chamber. 
 
Vacuum pump/vacuum gauge. 
 
RF absorber panels. 
 
Dual directional coupler (NARDA Model 3022 or equivalent). 
 
RF attenuator (NARDA 757C-20 or equivalent). 
 
Dual RF power meter (HP 438). 
 
Antenna Test Set - refer to Section 2.4.3.2.2. 
 
RF Power Source. 
Measurement Requirements 
 
Connect the equipment as shown in Figure 2-16.  The environmental chamber should be pumped down to and maintained at or above the maximum pressure altitude found in DO- 160C at ambient temperature.  After the environment has stabilized, apply an RF signal as specified in Section 2.2.3.10 for a minimum of one hour. Environmental Chamber               ┌──────────┐ ┌───────────────────────────────────┐    │ Pressure │ │                                   ╞════╡  Gauge   │       
              │                                   │    └──────────┘ │      Antenna Under Test           │ │     ┌──────────────────────┐      │ │  ═══╧══╤═══════════════╤═══╧════  │ < Ground Plane │        └─┬─────┬───────┘          │ │          ^     │ ┌───────────┐    │ │          │     └─┤  Dir'l    ├────┼───<───┐ │  ║       │       │ Coupler   │    │       │ │  ║       │       └─┬───────┬─┘    │       │ └──╫───────┼─────────┼───────┼──────┘       │ ┌─────╨────┐  │         v       v              │ │          │  │         │  ┌────┴────┐         │ 
           │  Vacuum  │  │         │  │  Atten  │         │ │   Pump   │  │         │  │  20 dB  │         │ │          │  │         │  └────┬────┘         │ └──────────┘  │         │       v              │ │      ┌──┴───────┴──┐     ┌─────┴──────┐ │      │ Dual Power  │     │  RF source │ Control ─────> │      │   Meter     │     │            │ Cable          │      └─────────────┘     └────────────┘ │ ┌───────┴───────┐ │    Antenna    │ │   Test Set    │      <-  HGA or IGA only └───────────────┘ Caution: 
Radiation from this test setup may pose a safety hazard, and 

 
              should be conducted so as to avoid harmful interference. 

 

 
NOTES: 1. 
The incident and reflected power at the antenna input should be monitored 
for the duration of the power handling test.  Note any changes. 


2. 
This is an altitude test only. 

 
Turn off the signal and remove the antenna from the environmental chamber.  Measure the gain performance in an anechoic chamber or equivalent at ambient temperature and altitude to verify continued compliance to the requirements of Section 2.2.3.2 and the VSWR requirements of Section 2.2.3.5. 

## 2.4.3.3.10 Carrier/Multipath Discrimination - Hga And Iga (Section 2.2.3.11)

 
Equipment Required 
Antenna Measurement Range - refer to Section 2.4.3.2.1. 
 
Antenna Ground Plane - refer to Section 2.4.3.2.2. 
 
Antenna Test Set - refer to Section 2.4.3.2.2. 

Diplexer/LNA. 

 
Antenna-Diplexer/LNA interconnect coaxial cable with 0.3 dB insertion loss. 

 
 
Measurement Requirements 
 
Carrier/multipath (C/M) discrimination performance is measured for two specific antenna beam-pointing elevation angles -- 5 degrees and 20 degrees.  Pattern measurements are made from which: 

 
 
- 
C/M (smooth sea) is calculated for the specific specular point pattern measurement by using an equation; 
 
- 
C/M (rough sea) is calculated by integration using the pattern measurements and multipath power densities. 
 
- 
C/M (median sea) is calculated as the weighted average of C/M (smooth sea) and C/M (rough sea). 
 
Connect the equipment as shown in Figure 2-10.  This test shall be conducted at the Lower and Upper Band-Edge and Mid-Band test frequencies of the receive and transmit bands. The antenna gain measurements required for this test should be conducted according to the procedure in Section 2.4.3.3.1.1. 

For a beam-pointing direction at elevation angle, b = 5 and azimuth angle, b = 0, measure the elevation cuts for horizontal and vertical polarizations (Gh(,b,b) and Gv(,b,b) respectively) in the elevation range from b to -45.  Measure the circular polarization gain at b (Gc(b,b)). 

 
C/M for Smooth Sea: Calculate the smooth-sea carrier-to-multipath ratio by: 
 
$$C/M_{\mathrm{\tiny~smooth}}\left(\,\theta_{b}\,,\phi_{b}\,\right)=\frac{\Gamma\left(\,\theta_{b}\,\right)x\,G_{c}\left(\,\theta_{b}\,,\phi_{b}\,\right)}{G_{b}\left(\,\text{-}\,\theta_{b}\,,\theta_{b}\,,\phi_{b}\,\right)x\,\big|\,k_{h}\left(\,\theta_{b}\,\right)\big|^{2}+G_{v}\left(\,\text{-}\,\theta_{b}\,,\theta_{b}\,,\phi_{b}\,\right)x\,\big|\,k_{v}\left(\,\theta_{b}\,\right)\big|^{2}}$$
 
where: 
(b)  
 
is 1.59 for 5 and 1.07 for 20. 
Gc(b,b)  
is the power gain for circular polarization at b elevation. 
Gh(-b,b,b) 
is the power gain for horizontal polarization at -b elevation when the 
beam is pointed to (b,b). 
Gv(-b,b,b) 
is the power gain for vertical polarization at -b elevation when the beam is 
pointed to (b,b). 
 

|                       | |k   |
|-----------------------|------|
| h                     |      |
| (                     |      |
|                      |      |
| b                     |      |
| )|                    |      |
|                      |      |
| b                     |      |
|                       |      |
| incidence (0.983 at 5 |      |
|                      |      |
| and 0.932 at 20       |      |
|                      |      |
| elevation).           |      |
|                       |      |
|                       | |k   |
| v                     |      |
| (                     |      |
|                      |      |
| b                     |      |
| )|                    |      |
|                      |      |
| b                     |      |
|                       |      |
| incidence (0.15 at 5  |      |
|                      |      |
| and 0.55 at 20        |      |
|                      |      |
| elevation).           |      |

 
If performance for the smooth sea case meets the requirement of Section 2.2.3.11, further testing is not required. 
 
The C/M computation in the rough sea case is based on Table 2-16, which gives the scatter power densities for elevation angles of 10 and 20.  The densities at 10 elevation angle shall be used for the computation of C/M at 5 elevation, i.e., Dh(,10)  Dh(,5) and Dv(,10)  Dv(,5). 

## 

| MULTIPATH    | HORIZ POL    | HORIZ POL    | VERT POL    | VERT POL    |
|--------------|--------------|--------------|-------------|-------------|
| INCIDENCE    | DENSITY      | DENSITY      | DENSITY     | DENSITY     |
| ANGLE        |              |              |             |             |
| @            |              |              |             |             |
|             |              |              |             |             |
| b            |              |              |             |             |
| = 10         |              |              |             |             |
|             |              |              |             |             |
|              | @            |              |             |             |
|             |              |              |             |             |
| b            |              |              |             |             |
| = 20         |              |              |             |             |
|             |              |              |             |             |
|              | @            |              |             |             |
|             |              |              |             |             |
| b            |              |              |             |             |
| = 10         |              |              |             |             |
|             |              |              |             |             |
|              | @            |              |             |             |
|             |              |              |             |             |
| b            |              |              |             |             |
| = 20         |              |              |             |             |
|             |              |              |             |             |
|              |              |              |             |             |
| ( -          |              |              |             |             |
|             |              |              |             |             |
| in deg)      | ELEVATION    | ELEVATION    | ELEVATION   | ELEVATION   |
| (D           |              |              |             |             |
| h            |              |              |             |             |
| (            |              |              |             |             |
|             |              |              |             |             |
| ,            |              |              |             |             |
|             |              |              |             |             |
| b            |              |              |             |             |
| ) in         | (D           |              |             |             |
| h            |              |              |             |             |
| (            |              |              |             |             |
|             |              |              |             |             |
| ,            |              |              |             |             |
|             |              |              |             |             |
| b            |              |              |             |             |
| ) in         | (D           |              |             |             |
| v            |              |              |             |             |
| (            |              |              |             |             |
|             |              |              |             |             |
| ,            |              |              |             |             |
|             |              |              |             |             |
| b            |              |              |             |             |
| ) in         | (D           |              |             |             |
| v            |              |              |             |             |
| (            |              |              |             |             |
|             |              |              |             |             |
| ,            |              |              |             |             |
|             |              |              |             |             |
| b            |              |              |             |             |
| ) in         |              |              |             |             |
| deg          |              |              |             |             |
| -1           |              |              |             |             |
| )            | deg          |              |             |             |
| -1           |              |              |             |             |
| )            | deg          |              |             |             |
| -1           |              |              |             |             |
| )            | deg          |              |             |             |
| -1           |              |              |             |             |
| )            |              |              |             |             |
|              | 0            |              | 45.0        |             |
|              | 5            |              | 33.0        |             |
|              | 10           |              | 24.0        |             |
|              | 15           |              | 18.0        |             |
|              | 20           |              | 16.5        |             |
|              | 25           |              | 10.0        |             |
|              | 30           |              | 4.0         |             |
|              | 35           |              | 1.5         |             |
|              | 40           |              | 1.0         |             |
|              | 45           |              | 0.0         |             |

 
C/M for Rough Sea: The carrier to multipath ratio for rough sea, C/Mrough can be calculated by the following method for a pointing elevation angle b: 

 
Step 1: 
Calculate the horizontal and vertical multipath components by 
$M_{h}(\,\theta_{b},\phi_{b}\,)=\Delta\theta\,x\sum_{\theta=45^{\circ}}^{0^{\circ}}D_{h}(\,\theta\,,\theta_{b}\,)\,x\,G_{h}(\,\theta\,,\theta_{b}\,,\phi_{b}\,)\,x\,W_{n}(\,\theta\,)$
 
and 

$M_{v}(\,\theta_{b},\phi_{b}\,)=\Delta\theta\,x\sum_{\theta=-\delta v}^{\theta^{\prime}}D_{v}(\,\theta\,,\theta_{b}\,)\,x\,G_{v}(\,\theta\,,\theta_{b}\,,\phi_{b}\,)\,x\,W_{n}(\,\theta\,)$
 
where: 
 
Mh is the horizontal multipath component for the antenna under test 
 
Mv  is the vertical multipath component for the antenna under test 
 
 
is the elevation angle 
 
 
is the elevation angle step (5 for Table 2-16). 
 
Dh(,b) is the horizontally polarized reflected power density, as given in Table 2-16. 
 
Dv(,b) is the vertically polarized reflected power density, as given in Table 2-16. 
 
Gh(,b,b) is the horizontal polarization gain, as measured. 
 
Gv(,b,b) is the vertical polarization gain, as measured. 
 
Wn() 
are the Trapezoidal Rule weights: 


Wn() = 0.5 at =0 and -45; Wn() =1, otherwise. 
Step 2: 
Calculate the roll-off improvement factor relative to the omnidirectional 
reference by: 
b omni b b c ) (     x     x   )    , (   G   =   )    , (   I           b b       )    , (   M   +   )    , (   M b b v b b h


where: 


I(b,b) 
 
is the roll-off improvement factor 


omni(b) 
 
is the Standard summation for the omni-directional antenna.  74.18 at 5 and 97.60 at 20 elevation respectively. 


Gc(b,b) is the RHCP antenna gain. 
Step 3: 
Calculate C/M for the antenna under test by: 
$C/M_{\rm rough}$ ( $\theta_{b},\phi_{b}$) = 10 $x$ log( $I$ ($\theta_{b},\phi_{b}$)) + 11.72
 
C/M for median sea:  Calculate the median C/M for the (worst case) smooth and rough seas by: 
$$C/\,M_{\,\,m e d i a n}=0.3x C/\,M_{\,\,s m o o t h}+0.7x C/\,M_{\,\,r o u g h}$$
 
Step 4: 
Repeat Steps 1 to 3 for azimuth angles, b, of 22.5, 45, ... 180. 
Step 5: 
Repeat measurements for smooth sea, rough sea and median sea C/M for 
elevation angle b of 20. 

## 2.4.3.3.11 Antenna Intermodulation In The Receive Band (Section 2.2.3.12) Equipment Required

 
Two frequency synthesizers (HP 8665A, option 004 or equivalent). 
 
Directional coupler, 30 dB coupling, 60 watts or greater average power rating (NARDA 
Model 3002-30 or equivalent). 
 
Attenuator, 20 dB (NARDA Model 757C-20 or equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics, 
Inc. Model T-1005 or equivalent). 
 
Two RF Power Amplifiers, 1626.5 to 1660.5 MHz (ARINC 741 HPA or equivalent). 
 
Diplexer/LNA (ARINC 741 Diplexer/LNA or equivalent). 
 
Two Spectrum Analyzers (HP 8563A or equivalent). 
 
RF Anechoic Chamber. 
Measurement Requirements 
 
Connect the equipment as shown in Figure 2-17, follow the steps below for each of 10 different beams (or pointing directions in case of mechanical antennas) within the declared service coverage: 

 
For N = 0 to 7, generate an unmodulated carrier at f1 = 1627.0 + 4xN at a power level equal 
to 3 dB below the maximum multi-carrier average RF power rating of the antenna referred to its input. 
Generate an unmodulated carrier at f2 = 1631.0 + 4xN at a power level equal to 3 dB below 
the maximum multi-carrier average RF power rating of the antenna referred to its input. 
 
 ┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐ │ Anechoic              │ │ Chamber               │                                            
   │                       │ │     ┌────────────┐    │                     ┌────────┐     ┌──────┐ │     │  Antenna   │    │                     │  RF    │     │ Synth│ │     │ Under Test │    │                     │  Power ├─<───┤      │ │     └────┬───────┘    │                     │  Amp   │     │  f1  │ │          │            │                     └────┬───┘     └──────┘ └──────────┼────────────┘                          │ ┌────────┘                                       │ │                                                │ │     ┌───────────────────┐                      │ │     │   Diplexer/LNA    │                      v │     │   (Test Eqpt)     │     ┌───────┐     ┌──┴────┐    ┌──────┐ 
     │     │                   │     │ Dir'l │     │ Quad  │    │  50  │ └───<─┤Ant.          Xmt  ├─<───┤ Cplr  ├─<───┤ Cplr  ├──>─│  Ohm │ │Port          Port │     │ 30 dB │     │ 3 dB  │    │ Load │ │       Rcv         │     └───┬───┘     └───┬───┘    └──────┘ │       Port        │         │             ^ └─────────┬─────────┘         │             │ │                   │             │ │                   v             │ │              ┌────┴──┐     ┌────┴───┐    ┌──────┐ │              │ Att'n │     │  RF    │    │Synth │ │              │       │     │  Power ├─<──│      │ │              │ 20 dB │     │  Amp   │    │ f2   │ │              └───┬───┘     └────────┘    └──────┘ v                  v ┌──────┴─────┐      ┌─────┴──────┐ │  Spectrum  │      │  Spectrum  │ │  Analyzer  │      │  Analyzer  │ └────────────┘      └────────────┘ 

## Figure 2-17.  Antenna Intermodulation In The Receive Band -- Section 2.4.3.3.11

 
For M = 0 to 7, measure the power level of the intermodulation product at the output of the LNA with the spectrum analyzer and refer it back to the LNA input at frx = 1559.0 - 4M. 

 
Repeat the tests for all combinations of values of M and N.  The power levels measured shall not exceed values of Section 2.2.3.12. 

## 2.4.3.3.12 Radiated Antenna Intermodulation Products (Section 2.2.3.13) Equipment Required

 
 
Two frequency synthesizers (HP 8665A, option 004 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts or greater average power rating (NARDA 
Model 3002-30 or equivalent). 
 
Attenuator, 20 dB (NARDA Model 757C-20 or equivalent). 
 
High Power Load, 50 Ohms, 60 Watts or greater average power rating (RLC Electronics, 
Inc. Model T-1005 or equivalent). 
 
Two RF Power Amplifiers, 1626.5 MHz to 1660.5 MHz, (ARINC 741 HPA or equivalent). 

 
Two Spectrum Analyzers (HP 8563A or equivalent). 
 
RF Anechoic Chamber. 
 
Matched quarter wave GNSS monopole at 1610 MHz (VSWR < 1.5:1). 
 
Antenna Test Set (refer to Section 2.4.3.2.2). 
 
Ground Plane compliant with Section 2.4.3.2.2 and with provisions to mount the GNSS 
monopole at least 5 feet away from the Antenna Under Test (AUT). 
 
GNSS pass-band filter with < 1 dB insertion loss at 1610 MHz and >65 dB isolation from 
1638.5 MHz to 1660.5 MHz. 
 
GNSS amplifier, 1610 MHz, with gain > 50 dB and NF < 1.3 dB. 
Measurement Requirements 
Connect the equipment as shown in Figure 2-17A, follow the steps below. 
1) 
Mount the Antenna Under Test (AUT) and the GNSS monopole on the ground plane. 
2) 
With the AUT elevation angle set to 5 degrees, steer the AUT in the direction of the GNSS antenna. 
3) 
Use a spectrum analyzer to measure the isolation, in dB, between the two antenna 
(ANTISOdB) at 1610 MHz. 
4) 
Set RF synthesizer 1 (f1) to 1638.5 MHz. 
5) 
The radiated IM is to be measured for 40 different antenna beam locations, equally spaced in solid angle in the region defined by an elevation angle greater than or equal to 20 degrees.  Steer the antenna to each of the 40 beam locations and perform the following steps 6-10. 
 
6) 
The RF Synthesizer number 2 (f2) frequency is defined by the following: 
 
$\int_{2}(\text{MHz})=\frac{(\text{N}+\text{I})\times\text{f}_{1}-2\times(1610)}{\text{N}-\text{I}}$


for N = 7 to 11, where N is the IM order. 
 
Set the RF synthesizer number 2 (f2) for N = 7. 

 
7) 
Set the RF power amplifiers to an output power 3 dB below the maximum multicarrier RF power rating of the antenna referred to its input. 
8) 
Measure the IM product level in dBm at the GNSS spectrum analyzer at 1610 MHz 
and refer it back to the GNSS antenna output port (IMGNSSdBm). 
 
9) 
Normalize the IM product level to a 40 dB antenna isolation by performing the following calculation: 
 
 
IMLEVEL = IMGNSSdBm - 40 dB + ANTISOdB 
10) Repeat steps 6 to 9 for N = 9 and 11. 
11) With the antenna elevation angle set to 5 degrees, repeat steps 6-10 with the antenna 
steered in the direction of the GNSS antenna. 
12) Determine that the IM product levels determined in step 9 (IMLEVEL) do not exceed 
the values of Section 2.2.3.13. 

## 2.4.4 Transceiver Subsystem (Satellite Subnetwork Physical Layer) Performance Verification Requirements

 
For performance verification purposes, this section includes procedures for the Transceiver Subsystem, including the Transmitter as defined in Section 2.2.4.2, and the Receiver as defined in Section 2.2.4.1.  The term Satellite Subnetwork Physical Layer is also used for this subsystem in regard to the layered ISO concepts for data communications protocols. 

## 2.4.4.1 Definitions Of Terms And Conditions Of Test

 
The following are definitions of terms and the conditions under which the tests described in this Section should be conducted. 
a. 
Power Input Voltage - Unless otherwise specified, all tests shall be conducted with the power input voltage adjusted to design voltage +2%.  The power input voltage shall be measured at the input terminals of the equipment under test. 
b. 
Power Input Frequency 
 
(1) In the case of equipment designed for operation from an AC source of 
essentially constant frequency (e.g., 400 Hz), the input frequency shall be adjusted to design frequency +2%. 
 
(2) In the case of equipment designed for operation from an AC source of variable 
frequency (e.g., 300 to 1,000 Hz), unless otherwise specified, tests shall be conducted with the input frequency adjusted to within 5% of a selected frequency and within the range for which the equipment is designed. 
c. 
Adjustment of Equipment - The circuits of the equipment under test shall be properly aligned and otherwise adjusted in accordance with the manufacturer's recommended practices prior to application of the specified tests. 
d. 
Test Equipment - All equipment used in the performance of the tests should be identified by make, model and serial number where appropriate, and its latest 
calibration date.  When appropriate, all test equipment calibration standards should be traceable to national and/or international standards. 

 
 
e. 
GES Emulator - For the tests described herein, a GES Emulator is required. transceiver functions and characteristics can be verified only when the AES is coupled through an RF link with its GES counterpart, each controlling or reacting to various states (or changes of state) of the other. 
 
The GES Emulator is not necessarily a single definable piece of test instrumentation, but it will likely comprise an assemblage of test equipment appropriate for a given test procedure capable of providing the functions necessary for that test.  For example, in certain RF tests, the GES Emulator would establish a "link" with the transceiver, providing the properly-modulated RF signals with appropriate accuracy and precision. As another example, the GES Emulator is necessary to verify correct operation of the signaling and communications protocols embodied in the transceiver. 
 
Because there are many ways in which the GES Emulator can be realized, a detailed description is not necessary herein.  However, in each procedure involving the GES Emulator, the particular characteristics essential for that procedure are described. 
f. 
Test Instrument Precautions - Due precautions shall be taken during the tests to prevent the introduction of errors resulting from the connection of voltmeters, oscilloscopes and other test instruments across the input and output impedances of the equipment under test. 
g. 
Ambient Conditions - Unless otherwise specified, all tests shall be made with ambient conditions as specified in DO-160C, para. 3.4. 
h. 
Connected Loads - Unless otherwise specified, all tests shall be performed with the equipment connected to loads having the impedance values for which it is designed. 
i. 
Test Frequencies - Unless otherwise specified, the following tests shall be conducted at the following frequencies: 


Test Frequency  
 
    Receive  
   Transmit 



Lower Band-Edge 
 
1530.5 MHz 
1627.0 MHz 


Mid-Band  
 
 
1544.5 MHz 
1643.5 MHz 


Upper Band-Edge 
 
1558.5 MHz 
1660.0 MHz 

 
j. 
EMI Testing - Only the transceiver in Figure 2-18 (not the test equipment) need be subjected to the electromagnetic environment as specified in Table 2-15.  For the antenna subsystem, a matched load should be connected, and the antenna performance verified to requirements after application of HIRF. 
 
 
NOTE: 
For specific airframes, the aircraft manufacturer may require the interconnecting wiring to be included in the specified electromagnetic 
environment. 

## 2.4.4.2 Detailed Test Procedures - Receiver

 
 
The following receiver-related tests require a GES Emulator and may require additional test equipment not shown in the test figures.  The transceiver frequency, power, etc. are controlled by commands from the GES Emulator.  The transceiver must be receiving a P channel before a transceiver transmit signal can be generated.  In addition, transmitter Doppler correction may be determined by offsets on the received frequencies generated by the GES Emulator. 

Some of the receiver tests in the following sections require the use of BER measurements as an indication of proper or improper transceiver operation, and some are repeated under various environmental conditions.  At the lower data rates, if post-Viterbi BERs are used the tests could require a considerable amount of test time.  As a result, pre-Viterbi channel error rates may be used in many of the Gaussian signal condition tests to greatly reduce the required testing time.  However, before pre-Viterbi BERs can be used they must be characterized by measuring the relationships between pre-Viterbi and post-Viterbi error rates.  The following procedure provides information supporting this use of pre-Viterbi data. 

## 2.4.4.2.1 Pre-Viterbi P-Channel Ber Characterization

 
Equipment Required 
BER Test Set. 
 
Directional Coupler, 30 dB Coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 
 
Noise and Interference Test Set (HP 3708A or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
Connect the equipment as shown in Figure 2-18.  Command the GES Emulator to provide a P-channel test signal at the highest available BPSK channel rate on a mid-band test frequency channel at a level into the transceiver of -120 dBm.  Command the transceiver to receive this test signal.  Adjust the noise and interference test set for the C/N0 given in Section 2.2.4.1.11.1 for Gaussian noise at the channel rate under test.  Measure and record both the pre-Viterbi and post-Viterbi BER results. ┌─────────────────┐ │   Noise and     │ │  Interference   │ │    Test Set     │ 
                               └────┬────────┬───┘ │        ^ v        │ ┌──────────────┐       ┌────┴────────┴───┐ │     BER      │       │      GES        │ │   Test Set   ├──────>┤    Emulator     │ │              │       │                 │ └──────┬───────┘       └────────┬────────┘ ^                        ^ │                        │ │                        v ┌──────┴───────┐       ┌────────┴────────┐      ┌──────────┐  
        │ XCVR         │       │   Directional   │      │   High   │ │         Ant. ├<─────>┤     Coupler     ├─────>┤   Power  │ │         Port │       │      30 dB      │      │   Load   │ └──────────────┘       └─────────────────┘      └──────────┘ 

 
The observation or gating time shall include a minimum of 100 post-Viterbi errors or 107 received bits within the period, whichever comes first.  Enough pre-Viterbi measurements shall be recorded throughout the post-Viterbi measurement period to determine a valid average pre-Viterbi BER corresponding to the measured post-Viterbi BER.  The recorded BER shall be the average of several measurements. 
Reduce the C/N0 of the test signal by 0.5 dB and repeat the above measurements. 
Reduce the C/N0 of the test signal by another 0.5 dB and repeat the above measurements. 
A plot of measured BERs versus the C/N0 levels should show the relationship between preand post-Viterbi BERs.  The curves should follow typical curves for the two types of BERs.  
Additional testing may be required at higher or lower C/N0 levels to adequately determine 
the curves.  Perform additional testing as required. 
 
 
NOTE: 
The relationship of pre-Viterbi to post-Viterbi BER should be independent of channel rate (bandwidth), so testing at additional rates is not necessary. 
If the actual BER is very close to the specified value, several BER measurements may be averaged.  At least 10 million bits must be observed for BER = 10-5 tests and 100,000 bits for BER = 10-3 to achieve a nominal 100 bits in error.  Also note that these are data bits, not symbols. 

## 2.4.4.2.2 Sensitivity (Section 2.2.4.1.2)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 
rating (NARDA Model 3022 or equivalent). 
 
Precision Calibrated Attenuator, 20 dB (NARDA Model 757C-20 or equivalent). 
 
Dual Power Meter (HP 438A or equivalent). 
 
Power Sensor, -30 to +20 dBm, 0.1 MHz - 4.2 GHz (HP 8482A or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 50 + j0 ohms, 60 watts or greater average power rating (RLC Electronics 
Inc. Model T-1005, or equivalent). 
 
BER Test Set. 
 
GES Emulator. 
Measurement Procedure 
 
 
NOTE: 
The GES Emulator must be capable of generating the required test signal modulated by the data stream from the BER tester.  The precision of the modulation and channel filtering is similar to the requirements of the transceiver transmit modems.  The required precision of the level adjustment for the minimum input signal power is + 0.1 dB to be maintained for the period of the BER measurement.  Considering the very low signal levels required and the small tolerance allowed, measures should be taken to avoid possible leakage problems from the test signal generator. 
 
Connect the equipment as shown in Figure 2-19.  The channel rates and the required BERs and test signal levels are listed in Section 2.2.4.1.2.  The sensitivity of the transceiver will first be measured at ambient temperature.  Command the transceiver to receive a signal using one of the channel units, operating at one of the available channel rates, and on a channel frequency near the center of the receive band. 

 
Adjust the test signal level at the antenna port to the Maximum Input Signal Power as listed (Section 2.2.4.1.2) for that channel rate and expected BER. 
The GES Emulator also must simulate the required adjacent channel signals, configured as the same channel type as the test channel, but modulated by a different data stream than that used by the test channel.  The phase noise as specified in Figure 1 of Reference Document "B" must also be generated by the GES Emulator. 
Command the transceiver to transmit a test signal on a test channel.  Using the BER tester, verify the transceiver sensitivity on a received channel.  Repeat at the remaining received test frequencies. 
Repeat the steps of the above Section at the lowest A-BPSK channel rate and at one A- QPSK channel rate, and test all rates at one test frequency as a minimum. 
 ┌─────────────┐    ┌─────────────┐ │    BER      │    │    GES      │ │    Test     ├───>┤  Emulator   │ │    Set      │    │             │ 
    └──────┬──────┘    └──────┬──────┘ ^                  ^ │                  v ┌──────┴──────┐    ┌──────┴──────┐     ┌─────────────┐   ┌─────────┐ │ XCVR        │    │ Directional │     │ Directional │   │  High   │ │         Ant.├<──>┤  Coupler    ├────>┤  Coupler    ├──>┤  Power  │ │         port│    │   30 dB     │     │   20 dB     │   │  Load   │ └─────────────┘    └─────────────┘     └────┬────────┘   └─────────┘ │ │ │ v 
     ┌─────────────┐    ┌─────────────┐    ┌────┴────────┐ │   Power     │    │   Power     │    │   20 dB     │ │   Meter     ├<───┤   Sensor    ├<───┤  Attenuator │ │             │    │             │    │             │ └─────────────┘    └─────────────┘    └─────────────┘ 

## 2.4.4.2.2 And 2.4.4.2.5 2.4.4.2.3 Rejection Of Signals Within And Outside The Transceiver Receive Band (Sections 2.2.4.1.3 And 2.2.4.1.4)

 
Equipment Required 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
Synthesized Sweep Signal Generator, 470 to 2000 MHz frequency range (HP 8644B, 
option 002, or equivalent). 
 
Synthesized Sweep Signal Generator, 2 to 18 GHz frequency range (HP 83751B or 
equivalent). 
 
Directional Coupler, 10 dB coupling (NARDA Model 3002-10 or equivalent). 
 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 
 
Spectrum Analyzer (HP 8566B or equivalent). 
Measurement Procedure 
 
This is a two-part test.  In Part One, analysis and a swept frequency search is performed to identify potential analog image and spurious response frequencies and possible digitally induced aliases.  The second part evaluates the degradation to a desired signal channel due to CW interference signals on the image and spurious frequencies found in Part One of the test and by analysis.  The degradation is evaluated in terms of loss of superframe lock. 

 
 
NOTE: 
Loss of lock is used as the criterion rather than superframe acquisition because loss of in-progress communications appears to be more critical than inability to 
initially acquire a channel. 
 ┌─────────────┐    ┌───────────┐ │    Signal   │    │    GES    │ │  Generator  │    │  Emulator │ │             │    │           │  
                       └──────┬──────┘    └───┬───────┘ │               ^ │               │ │               │ v               v ┌─────────────┐     ┌──┴────────┐   ┌──┴───────┐   ┌───────────┐ │  XCVR       │     │   Dir.    │   │   Dir.   │   │   High    │ │         Ant.├<───>┤ Coupler   ├<─>┤  Coupler │──>┤   Power   │ │         port│     │  10 dB    │   │  30 dB   │   │   Load    │ │             │     └───────────┘   └──────────┘   └───────────┘ └──┬───────┬──┘ │       v                                                       
          │       └────────  loss-of-lock indication (Part 2) │ │ v Pre-A/D output (Part 1) ┌──┴────────┐ │ Spectrum  │ │ Analyzer  │ │           │ └───────────┘ 

## Image And Spurious Response Rejection And Rejection Of Signals Outside The Aes Receive Band -- Section 2.4.4.2.3

 
Prior to the start of the test, analyze the transceiver under test to determine required input test frequencies.  All IF and reference frequencies used within the transceiver must be known.  Using these frequencies, calculate all frequencies within the ranges specified in Sections 2.2.4.1.3 and 2.2.4.1.4 which possibly will produce image or spurious signals. The calculations should include image frequencies and mixer harmonic intermodulation distortions which are capable of producing IF frequencies used within the transceiver, or sub-harmonics of these IF frequencies, and such frequencies that may lead to digital aliasing problems or other spurious responses. 



Part One of this test may be performed with unit(s) open for access in accordance with the following special requirement. 

 
Special Transceiver Requirements: 
 
 
NOTE: 
In order to perform this test, an analog signal must be available prior to the 
A/D converter of the channel unit under test. 
 
Part One: 
 
Connect the equipment as shown in Figure 2-20, using a sweep generator in the "signal generator" position.  With the sweep generator turned off, set the GES Emulator to provide an unmodulated test signal at the Mid-Band test frequency at the Maximum Signal Power Level into the transceiver as specified in Section 2.2.4.1.2 
for a P channel.  Command the transceiver to receive this signal.  Set the spectrum analyzer sweep to zero span.  Set the spectrum analyzer resolution bandwidth and video bandwidth each to 100 Hz.  Tune the spectrum analyzer frequency for maximum response to the test signal, and note the level of this response.  Command off the GES Emulator test signal.  Assure that the signal-to-noise ratio observed on the spectrum analyzer is at least 12 dB.  Reduce the spectrum analyzer resolution bandwidth and video bandwidth if needed to obtain this signal-to-noise ratio. 

 
 
Turn on the sweep generator.  Adjust its output to produce signal levels into the transceiver as specified for each of the frequency ranges in Sections 2.2.4.1.3 and 2.2.4.1.4.  Sweep the frequency over the ranges specified in Sections 2.2.4.1.3 and 2.2.4.1.4.  Identify and record any frequency which produces an observable undesired output. 
 
Part Two: 
 
If the unit was opened for Part One of this test, disconnect the tap into the analog receiver chain and close the unit.  Command the GES Emulator test signal to the Mid- Band receive test frequency, to modulate as a P channel, and to produce the Maximum Signal Power Level specified in Section 2.2.4.1.2.  With the synthesizer in the "Signal Generator" position shown in Figure 2-20, place a CW signal with a level as specified in Sections 2.2.4.1.3 and 2.2.4.1.4 at each frequency, one at a time in sequence, as found either in Part One of this test or by analysis. Observe whether superframe lock is lost, which is an indication of test failure. 
 
Repeat these tests at the Upper and Lower Band-Edge receive test frequencies and verify operation to specification. 

## 2.4.4.2.4 Receiver Linearity (Section 2.2.4.1.5)

 
Equipment Required (see Figure 2-21) 
 
1 
Noise Source (Noise Com NC1107A or equivalent) 
 
 
2 
Filter, Low Pass, Passive, 17 MHz cutoff 
 
 
3 
Attenuator, 2 dB (HP 8494A or equivalent) 
 
 
4A 
Filter, Active High Pass, cutoff 50 kHz,  
 
 
4B 
Signal Combiner (HP 11636A or equivalent) 
 
 
4C 
Two 5 Volt Variable DC Power Supplies (HP 6825A or equivalent) 
 
 
4D 
Two 400:1 Voltage Dividers (Input 20,000 Ohms; Output 50 Ohms) 
 
 
5 
Signal Generator, 220 MHz, (HP 8644 or equivalent) 
 
 
6 
Quadrature Signal Splitter (Narda Hybrid 4029B or equivalent) 
 
 
7 
Phase Shifter (ARRA 3428A or equivalent) 
 
 
8 
Three Mixers (Watkins-Johnson N2EC or equivalent) 
 
 
9 
Signal Combiner (Anzac TU50 or equivalent) 
 
 
10 
Amplifier, 220 MHz, 14 dB gain 
 
 
11 
Attenuator, 10 dB (HP 8495A or equivalent) 
 
 
12 
Filter, Low Pass, cutoff 550 MHz (Microphase LP500 or equivalent) 
 
 
13 
Signal Generator, 1324.5 MHz (HP 8644A or equivalent) 
 
 
14 
Attenuator, variable (HP 8494A or equivalent) 
 
 
15 
Directional Coupler, 20 dB (Narda 3002-20 or equivalent) 
 
 
16 
Directional Coupler, 30 dB (Narda 3002-30 or equivalent) 
 
 
17 
High Power Load (RLC Electronics T-1005 or equivalent) 
 
 
18 
GES Emulator 
 
 
19 
BER Test Set 
 
 
20 
Amplifier, 1500-1600 MHz, 15 dB gain 
 
 
21 
Spectrum Analyzer (HP 8566B or equivalent) 
Measurement Procedure 
 
 
NOTES: 1. The depth of the notch in the generated noise spectrum to be added to the 
receive channel must be at least 40 dB prior to attenuation and addition to the receive channel in order to meet the test conditions.  When attenuated to 
the operating level for the test, the generated noise in the notch will be well below the thermal noise (i.e., "kTB" noise) at the transceiver receiver input. The width of the notch at the -30 dB points in the spectral response should be wide enough to accommodate the modulation spectrum of the channel 
under test, but should not exceed 110 kHz. 


2. Referring to Figure 2-21, Item 7 and both Items 4C should be adjusted to 
minimize (null) the residual carrier leakage at the center of the notch in the noise spectrum as observed on Item 21 (Spectrum Analyzer) by temporarily connecting the RF coaxial cable from the Mixer, Item 8C, to the Spectrum Analyzer, Item 21.  (Reconnect the coaxial cable to the Attenuator, Item 14, to continue the test procedure after these carrier leakage adjustments are complete).  This carrier leakage is due to imperfect balance in the doublesideband modulating mixer (Item 8B).  These adjustments are interactive and may require repeated iterations of the adjustments to achieve the lowest possible residual carrier level.  The residual carrier level should be no greater than -150 dBm at the antenna port of the transceiver under test.  The residual carrier level can best be observed and measured by the spectrum analyzer (Item 21) and the residual carrier level at the antenna port of the 
transceiver may then be determined by calculation, taking into account the 
gain of Item 20, the attenuation of Items 14 and 15, and any associated RF cable losses.  The residual carrier frequency should not coincide with a test P-channel or C- channel frequency during the test; i.e., the residual carrier should appear as a weak off-channel signal during the test.  This can be achieved by locating the residual carrier at the Mid-Band test frequency and locating test channels 25 kHz above and/or below the Mid-Band (residual carrier) frequency.  The notch extends 50 kHz above and below the residual carrier, allowing room for test channels on either side, or both sides, of the 
center of the notch. 
Connect the equipment as shown in Figure 2-21.  Command the transceiver to receive a P channel at 25 kHz either above or below the Mid-Band receiver test frequency.  Command the GES Emulator test signal to the same test frequency.  Set up the notched noise test set to produce the required noise spectrum power level with its notch centered at the Mid-Band 
test frequency; i.e., located to encompass the test channel frequency.  Verify performance as specified in Section 2.2.4.1.5. 



NOTE: 
For multi-channel transceivers, both a P channel and a C channel may be positioned within the notch, each located 25 kHz away from, and on opposite sides of, the Mid-Band receiver test frequency, so that performance of the C channel may be measured while the P channel maintains system control/-
management functions. 

## 2.4.4.2.5 Desired Signal Dynamic Range (Section 2.2.4.1.6)

 
Equipment Required 
BER Test Set. 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 60 watts or greater average power rating (RLC Electronics Inc.  Model 
T-1005, or equivalent). 
 
Noise And Interference Test Set (HP 3708A or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
 
NOTE: 
This test must be performed for each available channel rate and C/N0 level 
specified in Section 2.2.4.1.2  The previous Sensitivity test of Section 2.4.4.2.2 tested the performance at minimum signal levels.  This section repeats the test at maximum expected signal levels. 
Connect the equipment as shown in Figure 2-19.  Command the GES Emulator to provide a test signal at one of the available channel rates near the Mid-Band test frequency and adjust the level for maximum as specified in Section 2.2.4.1.6 for the channel rate under test. Command the transceiver to receive this test signal.  The resulting BER should be below the value specified in Section 2.2.4.1.2 for the channel rate under test.  The pre-Viterbi BER may be used as desired to reduce test durations per Sections 2.4.4.2 and 2.4.4.2.1. 
 
 
NOTE: 
The reported BER should be the average of several measurements.  The observation or gating time should be such that a minimum of 100 post-Viterbi errors or 107 received bits, whichever occurs first, may be observed within the period at the measured BER. 


Repeat until all the available channel rates for the transceiver under test have been tested. 
 ┌─────────────┐ │    GES      │ │  Emulator   │ 
                                    │             │ └──┬──────────┘ ^ │ ┌──────────────────┐          v │                  │       ┌──┴──────────┐     ┌─────────┐ │      XCVR        │       │ Directional │     │  High   │ │              Ant.├<─────>┤  Coupler    ├────>┤  Power  │ │              port│       │   30 dB     │     │  Load   │ │                  │       └─────────────┘     └─────────┘ └──────┬───────────┘ │ 
                │ v superframe lock indication 

## Figure 2-22.   Receiver Tuning -- Section 2.4.4.2.6 2.4.4.2.6 Receiver Tuning (Section 2.2.4.1.7)

 
Equipment Required 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
Connect the equipment as shown in Figure 2-22.  With a channel unit set up for one of the available channel rates, command the transceiver to receive on 1530.0025 MHz, 1545.0025 MHz, 1545.0050 MHz, 1545.0075 MHz, 1546.000 MHz, and 1558.9975 MHz.  Prior to giving the transceiver channel change command, set the GES Emulator to provide a suitable test signal on each channel.  Then send the command and observe that the transceiver provides a superframe lock indication.  The results will indicate operation at the band edges, and will demonstrate the specified 2.5 kHz channel spacing. 

## 2.4.4.2.7 Capture Range And Doppler Rate (Section 2.2.4.1.8 And 2.2.4.1.9)

 
Equipment Required 

 
Pulsed Microwave Frequency Counter, better than 1 X 108 measurement accuracy (HP 
5361A, option 010, or equivalent). 
 
Dual Trace Storage Oscilloscope (Tektronix 2232 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
Noise and Interference Test Set. 

 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 

 
GES Emulator. 
 
 
NOTE: 
A pulsed counter is not required for this test.  It is required for some of the 
similar tests in the transmitter section.  For that reason it is also specified here. 
Measurement Procedure 
 
 
NOTE: 
The GES Emulator is required to generate test signals simulating frequency offsets on the received signals. 
 
 
Considering actual operating conditions and the two channel unit types to be tested, two types of test signals are required.  A receiver P channel must be able 
to operate as a single receive channel.  A continuous control P-channel receiver signal must be present while testing a receiver C channel.  This P-channel signal must have the same Doppler simulation as the tested C channel. 
 
 
The GES Emulator also must be capable of simulating the normal Doppler offset by tuning each side of normal center frequency by the maximum specified in Section 2.2.4.1.8.  The offset should be adjustable in steps of 1 Hz or less, and must be phase-continuous.  The maximum rate of change of Doppler as specified in Section 2.2.4.1.9 must also be simulated by the GES Emulator. 
 
 
The GES Emulator must have the capability to gate on and off the simulated test signal for the receiver channel under test. 
Capture Range Test 
 
Connect the equipment as shown in Figure 2-23.  Command the GES Emulator control P- channel to the center of the selected receive channel (an exact multiple of 2.5 kHz).  This may be done by direct frequency adjustment if adequate precision is available from the GES Emulator, or by frequency measurement by the frequency counter with adjustments of the frequency.  The accuracy should be on the order of a part in 108 or better in order to maximize the available error allowed the transceiver system.  Set the C/N0 as specified in Section 2.2.4.1.8.  
The P channel should be modulated with a normal P-channel test signal.  The C-channel modulation should be modified to include a new preamble at the beginning of each gating period, as described in the notes following this procedure. 

 
The transceiver superframe lock indicator is fed to the vertical input of the scope.  The GES test signal sweep markers are fed to the scope trigger input.  Adjust the scope sweep to give an appropriate sweep time for observation. 
Adjust the GES test signal levels to -120 dBm at the transceiver antenna port.  Adjust the GES Emulator to provide a maximum positive Doppler offset on the test signals as specified in Section 2.2.4.1.8.  Command the transceiver receiver to tune to a channel not currently in use.  Assure that the transceiver has re-channeled.  Then command the receiver 
 ┌────────────────┐ │    Noise and   │ │  Interference  │ 
                             │    Test Set    │ └───┬───────┬────┘ │       │ ┌─────────────┐      ┌──┴───────┴──┐     ┌─────────────┐ │             │      │    GES      │     │  Frequency  │ │ Oscilloscope├<─────┤  Emulator   ├────>┤   Counter   │ │             │      │             │     │             │ └──────┬──────┘      └──────┬──────┘     └─────────────┘ ^ superframe         ^ │   lock             │ │ indication         │ ┌──────┴────────┐           v                            
         │               │        ┌──┴──────────┐     ┌────────┐ │   XCVR        │        │ Directional │     │  High  │ │           Ant.├<──────>┤   Coupler   ├────>┤  Power │ │           port│        │    30 dB    │     │  Load  │ │               │        └─────────────┘     └────────┘ └───────────────┘ 

## Figure 2-23.   Capture Range And Doppler Rate -- Section 2.4.4.2.7

to return to the original test channel frequency.  After a period of time the frame lock indicator should indicate superframe lock. 

 
Repeat the test with a maximum negative Doppler offset. 
Doppler Rate Test 
 
This test determines that frame lock occurs at the extremes of Doppler offsets and Doppler rates.  Choose an appropriate sweep segment and marker (test signal gate) position as described in the notes following this test.  Start the swept Doppler simulation and note the performance of the frame lock indicator for each gate period. 



Repeat the Capture Range and Doppler Rate tests for the remaining channel rates for the channel unit under test.  Verify operation within specification. 


NOTE: 
These tests and the following transmitter Doppler related tests require careful control of the frequencies of the GES Emulator test signals.  The GES receiver test frequency accuracy should have an insignificant effect on these measurements, and therefore must be accurate to at least an order of magnitude better than the required accuracy of the transceiver clock. 
 
 
The Doppler offset and Doppler rate can be simulated by phase-coherently sweeping both the control P channel and the test-channel signals through the range of center frequency, plus or minus maximum Doppler offset, at a sweep rate equal to the maximum Doppler rate of change.  Either single or multiple markers may be generated at a known frequency or frequencies. 


The resulting marker pulses at the chosen marker frequencies can be fed to a variable gate timer which is used to generate a signal gating pulse. 
 
 
For a normal C-channel operation, the preamble is only transmitted when a new burst is initiated.  This new burst must be simulated by the mechanism used to gate the C-channel carrier on and off, for bit sync and frame lock to occur for each gate interval. 
 
 
The actual gate length requirements are different for a P channel and for a C channel.  Suitable gating times should be chosen. 

## 2.4.4.2.8 Bit Error Rate Performance And Phase Discontinuity (Sections 2.2.4.1.10 And 2.2.4.1.11.1)

 
Equipment Required 
BER Test Set. 
 
Directional Coupler, 30 dB Coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 
 
Noise and Interference Test Set (HP 3708A or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
 
NOTE: 
The Phase Discontinuity requirement of Section 2.2.4.1.10 is tested in this procedure by including the signal degradation as described in that section. 
 
Similarly to the previous data rate tests, the pre-Viterbi BER characterization results from Section 2.4.4.2.1 may be used for the Gaussian (no Rician fading) portion of the test, while post-Viterbi BER must be used for the multipath portions. 

 
Connect the equipment as shown in Figure 2-18.  Adjust the GES Emulator to provide a 600 bps, P-channel test signal on a channel near the Mid-Band frequency and at a level of - 120 dBm at the transceiver.  Command the transceiver to receive this test signal.  Adjust the 
noise and interference test set to provide a C/N0 given in Section 2.2.4.1.11.1 for Gaussian 
noise at 600 bps.  Adjust the GES Emulator to provide the signal degradations specified in Section 2.2.4.1.11.1.  Measure and record the BER. 
Using the post-Viterbi BER, repeat the preceding for each of the multipath conditions at 600 bps in Section 2.2.4.1.11.1. 
Repeat the preceding for the conditions given in Section 2.2.4.1.11.1 for 1200 bps and for 10.5 kbps. 
 
 
NOTE: 
The reported BER should be the average of several measurements.  The observation or gating time should be such that a minimum of 100 post-Viterbi 
 ┌─────────────┐ │ Noise and   │ │ Interference│ 
                                     │ Test Set    │ └─┬─────────┬─┘ v         ^ ┌──────────────┐            ┌─┴─────────┴─┐ │   Digital    │            │    GES      │ ┌─>┤ Oscilloscope ├<───────────┤  Emulator   │ │  │              │            │             │ │  └──────────────┘            └──────┬──────┘ │ - lock indication                   ^ │                                     │ │  ┌───────────────┐                  v │  │               │            ┌─────┴───────┐     ┌───────────┐ 
      │  │   XCVR        │            │ Directional │     │   High    │ └──┤           Ant.├<──────────>┤   Coupler   │────>┤   Power   │ │           port│            │   30 dB     │     │   Load    │ │               │            └─────────────┘     └───────────┘ └───────────────┘ 

## Figure 2-24.   Time To Acquire Superframe Lock -- Section 2.4.4.2.9

errors or 107 received bits, whichever occurs first, may be observed within the period at the measured BER. 

## 2.4.4.2.9 Time To Acquire Superframe Lock (Section 2.2.4.1.11.2)

 
Equipment Required 
Directional Coupler, 30 dB Coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 
 
Noise and Interference Test Set (HP 3708A or equivalent). 
 
Digital Oscilloscope (Lecroy 9420 or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
Connect the equipment as shown in Figure 2-24.  Command the GES Emulator to provide a 600 bps, P-channel test signal on a channel near the Mid-Band test frequency at a level of - 120 dBm at the transceiver.  Command the transceiver to receive this test signal.  Adjust the noise and interference test set for a C/N0 given in Section 2.2.4.1.11.2 for Gaussian (no Rician fading) noise at 600 bps. 

 
Turn off the GES Emulator test signal.  Offset the GES Emulator test frequency by an amount equal to the maximum positive initial frequency offset given in Section 2.2.4.1.11.2.  Command the GES Emulator to transmit a test signal at the offset frequency. Verify that the time between the start of transmission and the transition of the superframe 
lock indicator does not exceed the value given in Section 2.2.4.1.11.2 for the test conditions measured to within  0.5 seconds. 

 
 
Repeat this step with the GES Emulator test frequency offset by the maximum negative initial frequency offset given in Section 2.2.4.1.11.2.  Repeat the test for the positive and negative minimum initial frequency offset given in Section 2.2.4.1.11.2. 
Repeat the procedure for channel rates of 1200 bps and 10.5 kbps. 

## 2.4.4.2.10 Circuit-Mode Voice Requirements (Section 2.2.4.1.12.1.1)

 
Equipment Required 
BER Test Set. 
 
Directional Coupler, 30 dB Coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 
 
Noise and Interference Test Set (HP 3708A or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
Connect the equipment as shown in Figure 2-18.  Command the GES Emulator to provide a 21 kbps C-channel test signal on the Mid-Band test frequency and at a level into the transceiver of -120 dBm.  Command the transceiver to receive this test signal.   Adjust the noise and interference test set for the C/N0 given in Section 2.2.4.1.12.1.1 for Gaussian noise at 21 kbps.  Adjust the GES Emulator to provide the signal degradations specified in Section 2.2.4.1.12.1.1.  Measure and record the BER to verify operation to 2.2.4.1.12.1.1. 

 
Repeat the preceding for each of the multipath (Rician fading) conditions at 21 kbps given in Section 2.2.4.1.12.1.1. 
 
 
NOTE: 
The reported BER should be the average of several measurements.  The 
observations or gating time should be such that a minimum of 100 post-Viterbi 
errors or 105 received bits, whichever occurs first, may be measured within the period. 

## 2.4.4.2.11 C-Channel Bit-Timing Recovery (Frequency Uncertainty) (Section 2.2.4.1.12.2)

 
Equipment Required 
Directional Coupler, 30 dB Coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 
 
Noise and Interference Test Set (HP 3708A or equivalent). 
 
Oscilloscope (Tektronix 2232 or equivalent). 
 
GES Emulator. 
 
 ┌─────────────┐ │ Noise and   │ │ Interference│ │ Test Set    │ 
                                          └─┬─────────┬─┘ v         ^ ┌──────────────┐  frame sync    ┌─┴─────────┴─┐ │   Digital    │  indication    │    GES      │ ┌─>┤ Oscilloscope ├<───────────────┤  Emulator   │ │  │              │                │             │ │  └──────────────┘                └──────┬──────┘ │ -- frame lock                           ^ │    indication                           │ │  ┌───────────────┐                      v │  │               │               ┌──────┴──────┐   ┌──────────┐ │  │               │               │ Directional │   │  High    │ 
       └──┤  XCVR     Ant.├<─────────────>┤   Coupler   ├──>┤  Power   │ │           port│               │    30 dB    │   │  Load    │ │               │               └─────────────┘   └──────────┘ └───────────────┘ 

## 

 
Measurement Procedure 
 
 
NOTE: 
For this test the GES Emulator must be capable of generating a single C- channel frame burst with only one preamble and one unique word.  Alternate bursts must be offset by the frequency shifts specified in Section 2.2.4.1.12.2.  A frame sync pulse coincident with the last bit of the test burst unique word must be available from the GES Emulator.  A similar frame lock pulse must be 
available from the transceiver under test. 
Connect the equipment as shown in Figure 2-25. 
Adjust the GES Emulator to provide a 21 kbps C-channel test signal on a channel near the center of the receive band and at a level of -120 dBm at the transceiver.  Command the transceiver to receive this test signal.  Connect the frame sync indication from the GES Emulator test channel to the scope sync input and one of the scope vertical channels. Connect the frame lock indication from the transceiver channel under test to the other scope vertical channel.  Adjust the scope sweep rate for a suitable value. 
Adjust the noise and interference test set for a C/N0 three to six dB higher than that given in 
Section 2.2.4.1.12.1 for 21 kbps for Gaussian (no Rician fading) conditions.  This should provide an error-free signal to be used for determining normal operation and delays of the transceiver frame sync.  Observe the position (time delay) of the transceiver frame lock indication in relation to the GES Emulator frame sync indication.  All valid frame sync indications for the 21 kbps tests must be at this delay position in relation to the GES sync indication within a maximum tolerance of + one channel-rate bit period.  If no transceiver frame lock occurs or a false lock indication results from a GES frame sync indication, a frame lock failure has occurred. 
 
Adjust the noise and interference test set for the C/N0 specified for 21 kbps in Section 
2.2.4.1.12.1 for Gaussian (no Rician fading) conditions.  Adjust the GES Emulator to 
provide the signal degradations as specified in Section 2.2.4.1.12.2.  For each test burst, note whether the transceiver produces a corresponding valid burst sync indication. Continue the test for sufficient bursts to verify that operation meets specifications. 

## 2.4.4.2.12 Frame Lock Acquisition And False Frame Lock Probabilities (Section 2.2.4.1.12.3) Equipment Required

 
Directional Coupler, 30 dB Coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 
 
Noise and Interference Test Set (HP 3708A or equivalent). 
 
Oscilloscope (Tektronix 2232 or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
 
NOTE: 
For this test the GES Emulator must be capable of automatically generating a single C-channel frame burst with only one preamble and one unique word followed by a data sequence and postamble.  A frame sync indication coincident with the last bit of the test burst unique word must be available from the GES Emulator.  A similar frame lock indication must be available from the transceiver under test. 
Connect the equipment as shown in Figure 2-25.  Adjust the GES Emulator to provide a 21 kbps C-channel test signal on a channel near the center of the receive band at a level into the transceiver of -120 dBm.  Command the transceiver to receive this test signal.  Adjust the GES Emulator to provide the signal degradations as specified in Section 2.2.4.1.12.3. Connect the frame sync indication from the GES Emulator test channel to the scope sync input and one of the scope vertical channels.  Connect the frame lock indication from the transceiver channel under test to the other scope vertical channel.  Adjust the scope sweep rate for a suitable value to display at least one 0.5 second frame period. 
Adjust the noise and interference test set for a C/N0 three to six dB higher than that given in 
Section 2.2.4.1.12.3 for 21 kbps.  This should provide error-free signals for determining normal operation and timing.  Observe the position (time delay) of the transceiver frame lock indication in relation to the GES Emulator frame sync indication.  All valid frame sync indications for the 21 kbps tests must be at this delay position in relation to the GES sync indication within a maximum tolerance of + one channel-rate bit period.  If no transceiver frame lock occurs or a false lock indication results from a GES frame sync indication, a frame lock failure has occurred. 
Adjust the noise and interference test set for the C/N0 specified for 21 kbps in Section 
2.2.4.1.12.3.  For each test burst, note whether the transceiver produces a corresponding 
valid frame lock indication.  Continue the test for sufficient bursts to verify operation to specifications regarding the required probability. 

## 2.4.4.2.13 Maintaining Bit Synchronization (Section 2.2.4.1.12.4)

 
Equipment Required 
BER Test Set. 
 
Directional Coupler, 30 dB Coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 
 
Noise and Interference Test Set (HP 3708A or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
Connect the equipment as shown in Figure 2-18.  Adjust the GES Emulator to provide a 21 kbps C-channel test signal on a channel near the center of the receive band at a level into the transceiver of -120 dBm.  Command the transceiver to receive this test signal.  Adjust the noise and interference test set for a C/N0 given in Section 2.2.4.1.12.4 for 21 kbps. 

Use the GES Emulator frame sync indication to gate the BER Test Set measurement interval, giving a 0.5 sec gating period.  Monitor the resulting errors in each 0.5 second period. 

Because the C/N0 is reduced from the value specified in that section, the error count may be approximately 10 to 20 times worse than would result from the BER value given in Section 2.2.4.1.12.1.1.  Loss of bit timing sync would be indicated by 0.5 second error counts on the order of 1000 or more. 

 
 
NOTE: 
No specification is given indicating the measurement period required to verify normal operation.  A period of 5 minutes should be adequate. 

## 2.4.4.2.14 C-Channel Ber Measurement And Accuracy (Section 2.2.4.1.12.5)

 
Equipment Required 
BER Test Set. 
 
Directional Coupler, 30 dB Coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load (RLC Electronics Inc. Model T-1005, or equivalent). 
 
Noise and Interference Test Set (HP 3708A or equivalent). 
 
GES Emulator. 
 

## Measurement Procedure

 
 
NOTE: 
For this test the BER Test Set must have the capability of introducing precisely 
controlled errors within the data stream.  The errors should be evenly distributed in time through the data stream. 
Connect the equipment as shown in Figure 2-18.  Adjust the GES Emulator to provide a 21 kbps C-channel test signal on a Mid-Band frequency at a level of -120 dBm into the transceiver.  Command the transceiver to receive this test signal.  Adjust the noise and 
interference test set for a C/N0 at 10 dB above the level specified in Section 2.2.4.1.12.1.1 
for Gaussian (no Rician fading) noise at 21 kbps.  Adjust the test setup to provide a channel error rate at any value within one of the five threshold ranges as specified in Reference Document "A", Section 6.7.3.  Record both the source BER and the estimated channel BER as reported by the transceiver. 
Reference Document "A", Section 6.7.2 describes the relationship between the measured and reported channel error rate, and an actual error rate as set by the BER tester.  The number of errors reported over at least 21,000 bits shall be within + 8 of the number of errors transmitted by the BER tester. 
Repeat the above test until all five of the threshold ranges specified in Reference Document "A", Section 6.7.3 have been tested. 

## 2.4.4.3 Detailed Test Procedures - Transmitter 2.4.4.3.1 Channel Rates And Tolerance (Section 2.2.4.2.1)

 
Equipment Required 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent. 
 
High Power Load, 50 Ohms, 60 watts or greater average power rating (RLC Electronics 
Inc. Model T-1005 or equivalent). 
 
Time-Interval Counter (HP 5370B or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
Connect the equipment as shown in Figure 2-26.  Cause the transceiver to transmit a modulated carrier at one of the channel rates specified in Section 2.2.4.2.1 on the Mid-Band test frequency.  Measure the transceiver channel rate using the Time-Interval Counter. 

  
                                Demodulated XCVR Data 
                                       | 
                      ┌─────────────┐  v   ┌─────────────┐ 
                      │    GES      ├─────>│Time Interval│ 
                      │  Emulator   │      │  Counter    │ 
                      └────┬────────┘      └─────────────┘ 
                           ^                               
                           │                               
                           v                               
    ┌────────────┐   ┌─────┴────────┐      ┌────────┐      
    │            │   │ Directional  │      │  High  │      
    │ AES    Ant.├<─>┤   Coupler    ├─────>┤  Power │      
    │        port│   │    30 dB     │      │  Load  │      
    └────────────┘   └──────────────┘      └────────┘      
                                                           

## Figure 2-26.   Channel Rates And Tolerance -- Section 2.4.4.3.1

 
Repeat the above measurement for all the available transceiver channel rates, except that where the same reference clock is used for all channel rates only the highest channel rate need be tested. 

 
Verify that all channel rates meet requirements. 

## 2.4.4.3.2 Output Power (Section 2.2.4.2.2)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 
rating (NARDA Model 3022 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Two Precision Calibrated Attenuators, 20 dB (NARDA 757C-20 or equivalent). 
 
Dual Power Meter (HP 438A or equivalent). 
 
Two Power Sensors, -30 to +20 dBm, 0.1 MHz - 4.2 GHz (HP 8482A or equivalent). 
 
GES Emulator. 
 
 
NOTE: 
This and following tests can be conducted with a single power meter and with two single calibrated directional couplers, but the convenience and additional accuracy of a complete dual system is highly desirable, especially for the Load VSWR Capability test.  For that reason, components for a dual system are 
specified for all of the tests requiring power measurements. 
Measurement Procedure 
Connect the equipment as shown in Figure 2-27.  Command the transceiver to output a single carrier at maximum average power, at the Mid-Band test frequency.  Measure the incident power out of the transmitter. 
 ┌──────────────┐ │     GES      │ │   Emulator   │ │              │ 
                         └───┬──────────┘ ^ │ v ┌──────────────┐    ┌───┴──────────┐    ┌───────────────┐  ┌──────┐ │              │    │  Directional │    │   20 dB Dual  │  │ High │ │ XCVR     Ant.├<──>┤   Coupler    ├───>┤  Directional  ├─>┤ Power│ │          Port│    │    30 dB     │    │    Coupler    │  │ Load │ └──────────────┘    └──────────────┘    └───┬───────┬───┘  └──────┘ v       v ┌───────┴─┐   ┌─┴───────┐ │  Atten. │   │  Atten. │ 
                                         │  20 dB  │   │  20 dB  │ └────┬────┘   └────┬────┘ v             v ┌────┴────┐   ┌────┴────┐ │  Power  │   │  Power  │ │  Sensor │   │  Sensor │ └──────┬──┘   └──┬──────┘ v         v ┌──┴─────────┴──┐ │  Dual Power   │ │     Meter     │ └───────────────┘ 

 
Repeat the above measurements at the Upper and Lower Band-Edge test frequencies. 
For a multichannel transceiver, cause it to transmit its maximum number of carriers evenly spaced across the transmit band.  Measure the average power out of the transceiver and verify performance to specifications. 
 
 
NOTE: 
The number of intermodulation products will increase as the number of carriers 
increases. 

## 2.4.4.3.3 Output Power Adjustment (Section 2.2.4.2.3)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 
rating (NARDA Model 3022 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Two Precision Calibrated Attenuators, 20 dB (NARDA 757C-20 or  equivalent). 
 
Dual Power Meter (HP 438A or equivalent). 
 
Two Power Sensors, -30 to +20 dBm, 0.1 MHz - 4.2 GHz (HP 8482A or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
Connect the equipment as shown in Figure 2-27.  Command the transceiver transmitter to output a single carrier at the Mid-Band test frequency at maximum average rated power with the reported antenna gain set to the lowest value per Section 2.2.3.2.1.  Measure the average power out of the transmitter.  Command the transceiver to reduce its output power level through the specified steps and range (Section 2.2.4.2.3) and verify that the transmitter power output at each step is within tolerance. 

 
If the channel units in a multichannel transceiver are dissimilar in design, each type shall be tested separately. 
 
Using the GES Emulator, command the transceiver to operate at maximum rated average power and adjust the reported antenna gain from the lowest to the highest of the antenna gain range per Section 2.2.3.2.1.  Measure the average rated output power at each step. 

## 2.4.4.3.4 Output Power Stability (Section 2.2.4.2.4)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 
rating (NARDA Model 3022 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Two Precision Calibrated Attenuators, 20 dB (NARDA 757C-20 or equivalent). 
 
Dual Power Meter (HP 438A or equivalent). 
 
Two Power Sensors, -30 to +20 dBm (HP 8482A or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
Connect the equipment as shown in Figure 2-27.  Command the transceiver transmitter to output a single carrier at a frequency near the center of the transmit band.  Command the transceiver to transmit maximum average rated power.  Measure the average power out of the transmitter.  Monitor the power output for the time period specified in Section 2.2.4.2.4. 

 
 
NOTE: 
For lower data rate R or T channels, the format will have to be modified, either in software or hardware, so as to generate a continuous transmission rather than bursts.  In effect, this will be similar to a P-channel operation. 
Command the transceiver to reduce its power level in steps of 10 dB through the available range as specified in Section 2.2.4.2.3 and measure the transmitter power output at each 
step.  Monitor the power output at each step for a minimum time period as specified in Section 2.2.4.2.4 (not applicable to shock tests, as indicated in Table 2-15). 

## 2.4.4.3.5 Harmonics, Spurious, And Noise (Section 2.2.4.2.5) Equipment Required

 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 
rating (NARDA Model 3022 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
Attenuator, 30 dB attenuation, 0 - 6 GHz, 60 watts or greater average power (NARDA 
Model 769-30, or equivalent). 
 
Precision Calibrated Attenuator, 20 dB (NARDA 757C-20 or equivalent). 
 
Dual Power Meter (HP 438A or equivalent). 
 
Power Sensor, -30 to +20 dBm (HP 8482A or equivalent). 
 
High-Power Directional Coupler, 40 dB coupling, 2 - 18 GHz, 60 watts or greater average 
power (NARDA Model 27000-40 or equivalent). 
 
Spectrum Analyzer, 100 Hz - 18 GHz (HP 8566B or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
 
NOTE: 
The two measurement frequency ranges and test positions are required because no directional coupler will cover 10 kHz to 18 GHz, and the specified power attenuator which covers dc on the low end, is only rated to a 6 GHz upper frequency. 
Connect the equipment as shown in Figure 2-28 with the spectrum analyzer connected to Test Position #1.  Command the transceiver transmitter to output a single modulated carrier at maximum rated average power level at the Mid-Band test frequency. 
Measure the power out of the 20 dB attenuator.  Using the known loss of the 20 dB attenuator, the Dual Directional Coupler coupling factor, and the measured insertion loss of the three couplers, calculate the power at the transceiver output.  The carrier level as measured by the power meter, and translated to the transceiver output, will serve as a transceiver output reference level. 
With the transmitter operating at the power level above, use the spectrum analyzer to measure the composite harmonic, spurious and noise output of the transmitter over the frequency range of 4 GHz to 18 GHz. 
 
 
NOTE: 
The specification is in terms of a 4 kHz band (resolution bandwidth).  The recommended spectrum analyzer (and others for which characteristics are known) does not have a 4 kHz measurement bandwidth, so noise measurements must be corrected for bandwidth.  The closest available bandwidth is 3 kHz.  
The bandwidth correction is to be added to the measurement; and is 10 log10 
                     Test Position #1 ┌─────────────┐         ┌─────────────┐ │  Spectrum   │         │    GES      │        
                      │  Analyzer   │         │  Emulator   │ │             │         │             │ └──────┬──────┘         └──┬──────────┘ ^                   ^ │                   │ │                   v ┌─────────────┐     ┌──┴──────────┐     ┌──┴──────────┐ │             │     │    40 dB    │     │    30 dB    │ │  XCVR   Ant.├<───>┤ Directional ├<───>┤ Directional ├─────┐ │         port│     │   Coupler   │     │   Coupler   │     │ └─────────────┘     └─────────────┘     └─────────────┘     │ │  
                                                                  │ ┌───────────────────────────────────────────────────────────┘ │ │   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │   │    20 dB    │    │    30 dB    │    │  Spectrum   │ └──>┤ Directional ├───>┤ High Power  ├───>┤  Analyzer   │ │   Coupler   │    │ Attenuator  │    │             │ └──┬──────────┘    └─────────────┘    └─────────────┘ │                                 Test Position #2 │ │    ┌─────────────┐    ┌─────────────┐    ┌──────────┐ │    │  Precision  │    │  Power      │    │  Power   │ └───>┤  Attenuator ├───>┤  Sensor     ├───>┤  Meter   │ │    20 dB    │    │             │    │          │ └─────────────┘    └─────────────┘    └──────────┘ 

## Figure 2-28.   Harmonics, Spurious, And Noise -- Section 2.4.4.3.5

(4000/BWmeas), where BWmeas is the analyzer bandwidth (in Hz) used for the measurement. 

 
Move the spectrum analyzer to Test Position #2.  Use the spectrum analyzer to measure the composite harmonic, spurious and noise output of the transmitter over the frequency range of 10 kHz to 4 GHz, while transmitting full power as above. 
Repeat the above measurements at the Upper and Lower Band-Edge test frequencies. 

## 2.4.4.3.6 Intermodulation Products (Section 2.2.4.2.6)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 

rating (NARDA Model 3022 or equivalent). 

 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Precision Calibrated Attenuator, 20 dB (NARDA 757C-20 or equivalent). 
 
Dual Power Meter (HP 438A or equivalent). 
 
Power Sensor, -30 to +20 dBm, 0.1 MHz - 4.2 GHz (HP 8482A or equivalent). 
 
Single Directional Coupler, 20 dB coupling, 1-2 GHz (NARDA Model 4012C-20 or 
equivalent). 
 
Spectrum Analyzer, 100 Hz - 18 GHz (HP 8566B or equivalent). 
 
GES Emulator. 
Measurement Procedure 
This test applies only to multichannel transceivers. 
Step 1. 
After connecting the equipment as shown in Figure 2-29, command the transceiver to output a single unmodulated carrier at maximum allowable multicarrier average power level at the Mid-Band test frequency. 
Step 2. 
Reduce the power output of the channel unit by 3 dB at the transmitter output as measured by the power meter. 
Step 3. 
Turn off this carrier and select another channel unit at a frequency separated from the first frequency by approximately 1 MHz.  Adjust the new channel unit output level to be the same as with the first channel. 
Step 4. 
Turn on the first channel unit again so that both units are operating.  Use the spectrum analyzer to measure the intermodulation products resulting from the two signals with the measured single carrier power level as a reference. 
Step 5. 
Repeat Steps 1 through 5 for reduced commanded output levels in 5 dB steps to 15 dB below maximum allowable output. 
Step 6. 
Repeat Steps 1 through 4 for channel frequency separations of 100 kHz and 10 kHz and at the transmit test frequencies specified in Section 2.4.4.1, Item i, at all three frequency separations. 
Step 7. 
Repeat Steps 1 through 5 with one carrier tuned to 1660.4 MHz and the other carrier tuned to the lowest frequency that can be transmitted within the constraint of Section 2.2.4.2.6 for transmitting on newly-assigned frequencies, as implemented in the unit under test. 
Step 8. 
Repeat Steps 1 through 4 with a carrier spacing that would produce a fifth order intermodulation product that falls below the frequency defined in Section 2.2.4.2.6 as the limit on fifth-order products.  Verify that the transceiver meets the requirement. 
 ┌─────────────┐ │    GES      │ │  Emulator   │ │             │                                      
                     └──┬──────────┘ ^ │ v ┌─────────────┐   ┌──┴──────────┐    ┌──────────────┐    ┌────────┐ │             │   │ Directional │    │ Directional  │    │  High  │ │  XCVR   Ant.├<─>┤  Coupler    ├───>┤   Coupler    ├───>┤  Power │ │         port│   │   30 dB     │    │    20 dB     │    │  Load  │ └─────────────┘   └─────────────┘    └──┬───────────┘    └────────┘ │ │ ┌─────────────────────────┘                              
                 │ │   ┌─────────────┐      ┌─────────┐    ┌───────────┐ │   │ Directional │      │  Atten. │    │  Power    │ └──>┤   Coupler   ├─────>┤         ├───>┤  Sensor   │ │    20 dB    │      │  20 dB  │    │           │ └──┬──────────┘      └─────────┘    └─────┬─────┘ │                                      │ v                                      v ┌────┴─────┐                          ┌─────┴─────┐ │ Spectrum │                          │  Power    │ │ Analyzer │                          │  Meter    │ │          │                          │           │ └──────────┘                          └───────────┘ 

## 2.4.4.3.7 Carrier Off Level (Section 2.2.4.2.7)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 
rating (NARDA Model 3022 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 

 
Precision Calibrated Attenuator, 30 dB (NARDA 757C-30 or equivalent).  
 
Spectrum Analyzer, 100 Hz - 18 GHz (HP 8566B or equivalent). 
 
GES Emulator. 
Measurement Procedure 
Connect the equipment as shown in Figure 2-30.  Command the transceiver transmitter to output a single unmodulated carrier at maximum rated average power, and at the Mid-Band test frequency.  Measure the level of the carrier with the spectrum analyzer. 
 ┌───────────┐ │    GES    │ │  Emulator │ │           │ 
                       └──┬────────┘ ^ │ v ┌─────────────┐   ┌──┴──────────┐   ┌─────────────┐    ┌─────────┐ │             │   │ Directional │   │ Directional │    │  High   │ │  XCVR   Ant.├<─>┤   Coupler   ├──>┤  Coupler    ├───>┤  Power  │ │         port│   │    30 dB    │   │   20 dB     │    │  Load   │ └─────────────┘   └─────────────┘   └───┬─────────┘    └─────────┘ │ v ┌─────┴─────┐ 
                                       │           │ │   Atten.  │ │   30 dB   │ └─────┬─────┘ v │               ┌───────────┐ │               │ Spectrum  │ └──────────────>┤ Analyzer  │ │           │ └───────────┘ 

## Figure 2-30.   Carrier Off Level -- Section 2.4.4.3.7

 
Assure that the transmitter is commanded off, and then use the spectrum analyzer to verify that there is no output power level in the transmit band above the level specified in Section 2.2.4.2.7. 

## 2.4.4.3.8 Transmitter Muting (Section 2.2.4.2.8) Equipment Required

 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 

rating (NARDA Model 3022 or equivalent). 

 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 

equivalent). 

 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Precision Calibrated Attenuator, 20 dB (NARDA 757C-20 or equivalent). 
 
Spectrum Analyzer (HP 8566B or equivalent) 
 
GES Emulator. 
Measurement Procedure 
 
 
NOTE: 
For this test, a superframe lock indication must be available from the transceiver. 
 
 ┌───────────┐ │   GES     │ │ Emulator  │ └──┬────────┘ 
                          ^ │ v ┌─────────────┐   ┌──┴─────────┐   ┌────────────┐    ┌─────────┐ │             │   │ Directional│   │ Directional│    │  High   │ │  XCVR   Ant.├<─>┤  Coupler   ├──>┤  Coupler   ├───>┤  Power  │ │         port│   │   30 dB    │   │   20 dB    │    │  Load   │ └──────┬──────┘   └────────────┘   └────────────┘    └─────────┘ │                             │ │                             v │                       ┌─────┴─────┐ v                       │           │                         
        superframe                  │   Atten.  │ lock indication               │   20 dB   │ └─────┬─────┘ v ┌─────┴─────┐ │  Spectrum │ │  Analyzer │ │           │ └───────────┘ 

## Figure 2-31. Transmitter Muting And Signal Spectrum -- Sections 2.4.4.3.8 And 2.4.4.3.16

 
Connect the equipment as shown in Figure 2-31.  Adjust the GES Emulator to provide a 
Psmc channel test signal at the Mid-Band test frequency at a level of -120 dBm into the transceiver.  Command the transceiver to receive this Psmc signal.  Observe the presence of 
superframe lock indication from the transceiver.  Cause the transceiver to transmit a signal on the Mid-Band test frequency.  Adjust the spectrum analyzer to display this transmit 
signal.  Reduce the Psmc signal level until superframe lock indication loss is verified and 
observe that the transmit signal is shut off.  Attempt to cause all equipped channels in a multichannel transceiver to transmit.  Observe the transceiver output with the spectrum analyzer to verify the performance conforms to specifications. 

## 2.4.4.3.9 Load Vswr Capability (Section 2.2.4.2.9)

 
Equipment Required 
Directional Coupler, 30 dB coupling, 60 watts average power rating (NARDA Model 3002-
30 or equivalent). 
 
Dual Directional Coupler, 20 dB coupling, 60 watts or greater average power rating 
(NARDA Model 3022 or equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Dual Power Meter (HP 438A or equivalent). 
 
Two Power Sensors, -30 to +20 dBm, 0.1 MHz - 4.2 GHz (HP 8482A or equivalent). 
 
Two Precision Calibrated Attenuators, 20 dB (NARDA 757C-20 or equivalent). 
 ┌─────────────┐ │    GES      │ │  Emulator   │ └──────┬──────┘ 
                                             ^ │ v ┌───────────────┐     ┌──────┴──────┐ │               │     │ Directional │ │   XCVR    Ant.├<───>┤  Coupler    ├─────┐ │           port│     │    30 dB    │     │ └───────────────┘     └─────────────┘     │ │ ┌────────────────────────────────────────────────┘ │     ┌───────────────────┐ │     │        20 dB      │ 
         └────>┤ Dual Dir. Coupler ├──────────────────────┐ │ Inc.          Ref.│                      │ └─┬───────────────┬─┘                      │ │               │                        │ v               v                        v ┌─────┴─────┐   ┌─────┴─────┐            ┌─────┴─────┐ │   Atten.  │   │   Atten.  │            │   Atten.  │ │   20 dB   │   │   20 dB   │            │           │ │           │   │           │            │ See Note* │ └─────┬─────┘   └─────┬─────┘            └─────┬─────┘ v               v                        v ┌─────┴─────┐   ┌─────┴─────┐            ┌─────┴─────┐ │   Power   │   │   Power   │            │   Phase   │ │   Sensor  │   │   Sensor  │            │  Shifter  │ └─────┬─────┘   └─────┬─────┘            └─────┬─────┘ v               v                        v ┌─────┴───────────────┴─────┐        ┌─────────┴──────────┐ │                           │        │       Switch       │ │     Dual Power Meter      │        └───┬─────────────┬──┘ │                           │            │     OR      │ └───────────────────────────┘            v             v Coaxial        50 Ohm Short          Load * Note:  Select attenuator and cable losses to result in 2:1 VSWR with the coaxial short. 

## 

 
Phase Shifter, 360-degree minimum phase variation at 1.6 GHz, 60 watts minimum power 
rating (SAGE Model 6702-5 or equivalent). 
 
Coaxial short, Type N (HP 11511A, or equivalent). 
 
See Figure 2-32 for additional equipment required. 
Measurement Procedure 
Connect the equipment as shown in Figure 2-32, with the 50-ohm high power load connected to the phase shifter and the high power attenuators in place.  Set the phase shifter to minimum available phase.  Command the transceiver to transmit maximum average rated output power at the Mid-Band test frequency (Section 2.4.4.1).  Record the forward and 
reflected power indications from the two power meters corrected for the coupler and attenuator factors. 

 
 
The total average output power delivered to the load is the difference between the forward power and the reflected power (the reflected power should be negligible with the high power load connected).  Record the total average output power as the 1:1 VSWR load performance reference to be used in the following tests. 
Remove the carrier, replace the power load with a coaxial short.  Assure the phase shifter is at minimum available phase shift.  Again cause the transceiver to transmit the single carrier at maximum average rated output power on the Mid-Band test frequency. 
Record the power indicated on each of the power meters.  To verify that the load VSWR is 
2:1, the return loss should be 9.5 + 0.5 dB, i.e., 10 log10(Pfwd/Pref) = 9.5 + 0.5 dB.  If 
necessary, change the attenuator and/or the cable losses interconnecting the path from the directional coupler to the coaxial short to produce the required 2:1 load VSWR.  The total average output power (in watts) is the difference between the two power meter readings (in watts).  The change in the total average output power between the test with the 1:1 VSWR load and the test with the 2:1 VSWR load shall meet the requirements of Section 2.2.4.2.9. 
Continue to transmit the single carrier at maximum average rated power on the Mid-Band test frequency as before, and adjust the phase shifter continuously through a minimum of one-half wavelength of phase shift and record the lowest total average output power obtained.  The lowest total average output power obtained over all phase angles with the 2:1 VSWR load shall meet the requirements of Section 2.2.4.2.9. 
Remove the carrier and connect the phase shifter (terminated with the coaxial short) directly to the directional coupler (30 dB) as shown in Figure 2-32.  This presents an infinite VSWR to the transceiver antenna port (except for the remaining cable and equipment losses).  Command the transceiver to return to maximum average rated output power as before.  Adjust the phase shifter continuously through a minimum of one-half wavelength of phase shift. 
Then, remove the carrier, reconnect the test setup with the high power load and power attenuators in place (1:1 VSWR) as shown in Figure 2-32, set the phase shifter to minimum available phase shift, cause the transceiver to transmit the single carrier once again at maximum average rated output power at the Mid-Band test frequency, and measure the total average output power.  Verify that the total average output power meets the requirements. 
 
 
NOTE: 
 
The transceiver may not output significant power under the high VSWR condition, since it is only required to survive and is not required to operate under such a condition. 
Repeat the test at the Upper and Lower Band-Edge test frequencies as specified in Section 2.4.4.1. 
 
 ┌─────────────┐       counting gate trigger │    GES      │    (for Doppler rate capability) │   Emulator  ├─────────────────┬────────────────┐ │             │                 v                │ 
                      └──┬───────┬──┘         ┌───────┴──────┐         │ low level ^       │ high level │  Frequency   │         │ │       └───────────>┤   Counter    │         │ v                    └──────────────┘         │ ┌─────────────┐    ┌──┴──────────┐   ┌──────────────┐   ┌─────────┐ │ │             │    │ Directional │   │ Directional  │   │  High   │ │ │  XCVR   Ant.├<──>┤  Coupler    ├──>┤    Coupler   ├──>┤  Power  │ │ │         Port│    │   30 dB     │   │     20 dB    │   │  Load   │ │ └─────────────┘    └─────────────┘   └──┬───────────┘   └─────────┘ │ │                           │ v                           │ 
                                     ┌─────┴─────┐                     │ │           │                     │ │  Atten.   │                     │ │           │                     │ └─────┬─────┘                     │ v                           │ ┌───────┴───────┐                   │ │  Frequency    │                   │ │   Counter     ├─<─────────────────┘ │               │ └───────────────┘ 

## Tuning Range & Channel Incrs, Frequency Acc, Doppler Corr, Doppler Rate Capability -- Sections 2.4.4.3.10, 2.4.4.3.13, 2.4.4.3.14, 2.4.4.3.15 2.4.4.3.10 Tuning Range And Channel Increments And Channel Numbering (Sections 2.2.4.2.10.1 And 2.2.4.2.10.2)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 

rating (NARDA Model 3022 or equivalent). 

 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 

equivalent). 

 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Precision Calibrated Attenuator, 20 dB (NARDA 757C-20 or equivalent). 
 
Microwave Frequency Counter, better than 1 X 10-8 measurement accuracy (HP 5361A, 
option 010) 
 
GES Emulator. 
Measurement Procedure 
Connect the equipment as shown in Figure 2-33.  The table in Section 2.2.4.2.10.1 shows required channel center frequency ranges for each of the different channel rates. 
 
 
With a channel unit set up for one of the available channel rates, command the transmit channel, through the GES Emulator, to transmit at 1626.5000 MHz.  Repeat for 1660.5000 MHz.  Observe the response of the transceiver to these commands.  No carrier should be generated as a result of these commands. 

 
Next, to test proper operation of the allowed band-edge frequencies for all channel rates as listed in Section 2.2.4.2.10.1, at each commanded frequency record the resulting output frequency. 
Observing an output frequency, change the channel number by one and observe a change of output frequency by 2.5 kHz in the correct direction, within test equipment tolerances. Observe the resultant output frequency and verify that the channel number corresponds with the equation in Section 2.2.4.2.10.2. 

## 2.4.4.3.11 Tuning Stabilization Time (Section 2.2.4.2.11) Equipment Required



Dual Trace Storage Oscilloscope (Tektronix 2232 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
Attenuator, 20 dB. (NARDA Model 757C-20 or equivalent) 
 
High Power Attenuator, 30 dB attenuation, 60 watts or greater average power (NARDA 
Model 769-30 or equivalent) 
 
Pulsed Microwave Frequency Counter (HP 5361A or equivalent) 
 
GES Emulator. 
Measurement Procedure 
 
 
NOTE: 
The GES Emulator software must be capable of proper message units, and must have the capability for two P channels. 
 
 
Connect the equipment as shown in Figure 2-34. 
 
Set up the GES Emulator to transmit two P channels on two different channel frequencies and using the same slot timing.  Synchronize the scope with this slot timing signal, or with a superframe sync signal.  Connect the pulse out signal from the counter to the other oscilloscope channel.  This pulse is coincident with the detected burst.  The counter arming signal enables the counter to measure the frequency of a particular burst or series of bursts. 

 
Set up the first P channel to transmit an appropriate System Table (i.e., one showing the 
first P channel's own frequency as a GES Psmc frequency and also supplying the corresponding Rsmc frequency).  Set up the second P channel to continuously transmit Fill-in SUs (S23).  Command the transceiver to log on using the Rsmc frequency corresponding to 
the first P channel.  On receiving the Log-on Request (S1) sent by the transceiver, cause the GES Emulator to send, on the first P channel, one sequence of Log-on confirm (S2), P- channel assignment (S8), and R-channel assignment (S8A) containing the frequency of the 
second P-channel test signal (Pd) and the corresponding Rd frequency.  The frequency 

                   
                  Slot timing for sync 

          ┌─────────────┐       ┌─────────────┐ │             │       │    GES      │ ┌──>┤ Oscilloscope├<──────┤  Emulator   │                          
      │   │             │       │             │ │   └─────────────┘       └──────┬──────┘ │                                ^ │                                │ │                                │ │   ┌───────────────┐            v │   │               │      ┌─────┴───────┐     ┌─────────────┐ │   │   XCVR        │      │ Directional │     │   30 dB     │ │   │           Ant.├<────>┤  Coupler    ├────>┤ High Power  ├───┐ │   │           port│      │    30 dB    │     │  Attenuator │   │ │   │               │      └─────────────┘     └─────────────┘   │ 
      │   └───────────────┘                                            │ │                                                                │ │                                                                │ │                        ┌─────────────┐     ┌─────────────┐     │ │  Detected R-ch burst   │   Pulsed    │     │    20 dB    │     │ └────────────────────────┤  Frequency  ├<────┤ Attenuator  ├<────┘ │   Counter   │     │             │ └──────┬──────┘     └─────────────┘ ^ │ │ Arming                                      

## **Figure 2-34.   Tuning Stabilization Time -- Section  2.4.4.3.11**

counter should be armed to measure only the frequency of the R-channel burst on the Rd frequency. 

The above sequence should cause the transceiver receiver to tune to the second GES Emulator P-channel test frequency, resulting in transceiver R-channel transmission on the corresponding Rd frequency (as specified by the appropriate field of S8A).  The R-channel burst (containing one log-on acknowledgement SU, S34) should appear within the R- channel slot specified in Reference Document "B", Section 6.5.1. 

 
The measured Rd frequency should be as commanded by the S8A signal unit, indicating that 
the transceiver receiver and transmitter synthesizer settling times meet requirements. 

## 2.4.4.3.12 Phase Noise (Section 2.2.4.2.12)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 
rating (NARDA Model 3022 or equivalent). 

|                              | Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or      |
|------------------------------|------------------------------------------------------------------------------------------|
| equivalent).                 |                                                                                          |
|                              | High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. |
| Model T-1005 or equivalent). |                                                                                          |
|                              | Attenuator, 12 dB (NARDA 4772-12 or equivalent).                                         |

 ┌──────────────┐ │    GES       │ │  Emulator    │ │              │ 
                     └──────┬───────┘ ^ │ v ┌───────────┐   ┌──────┴───────┐   ┌───────────────┐    ┌────────┐ │  AES      │   │ Directional  │   │  Directional  │    │  High  │ │       Ant.├<─>┤   Coupler    ├──>┤    Coupler    ├───>┤  Power │ │       port│   │    30 dB     │   │     20 dB     │    │  Load  │ └───────────┘   └──────────────┘   └─┬─────────────┘    └────────┘ │ v  
                                    ┌─────┴─────┐ │           │ │  Atten.   │ │           │ └─────┬─────┘ │ v ┌──────┴──────┐ │  Phase      │ │  Noise Meas.│ │  System     │ └─────────────┘ 

## 

 
Phase Noise Measurement System (HP 3048A Phase Noise Measurement  System, option 
002 and 201; HP 98580C System Computer, options 008, 104; and HP 46083A; or equivalent). 
 
GES Emulator. 
Measurement Procedure 
Connect the equipment as shown in Figure 2-35.  Command the transceiver to transmit an unmodulated carrier on the Mid-Band test frequency. 
Measure and record the phase noise amplitude spectrum to verify compliance with requirements. 

## 2.4.4.3.13 Frequency Accuracy (Section 2.2.4.2.13)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power rating (NARDA Model 3022 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. Model T-1005 or equivalent). 
 
Precision Calibrated Attenuator, 20 dB (NARDA 757C-20 or equivalent). 
 
Pulsed Microwave Frequency Counter, better than 1 X 10-8 measurement accuracy (HP 
5361A, option 010) 
 
GES Emulator. 
Measurement Procedure 
Connect the equipment as shown in Figure 2-33.  Command the transceiver to transmit an unmodulated carrier on a Mid-Band test frequency. 
 
For a transceiver which determines necessary transmit Doppler corrections by measuring receive frequency offset, establish a zero Doppler offset (i.e. zero relative velocity) by adjusting the GES Emulator P-channel signal to the center of the receive channel (an exact multiple of 2.5 kHz). 

 
For a transceiver which uses the aircraft navigational data to determine the required offset, equivalent input signals may be derived to establish a zero Doppler offset. 
Measure the frequency of the transceiver transmit carrier and verify operation to specifications. 

## 2.4.4.3.14 Doppler Correction (Section 2.2.4.2.14)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 
rating (NARDA Model 3022 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Precision Calibrated Attenuator, 20 dB (NARDA 757C-20 or equivalent). 
 
Pulsed Microwave Frequency Counter, better than 1 X 10-8 measurement accuracy (HP 
5361A, option 010). 
 
GES Emulator. 
Measurement Procedure 
 
The following test is for a system which measures the receive frequency offset to determine transmitter frequency corrections for Doppler shift.  Equivalent input signals may be derived for a system which uses the aircraft navigational data to determine the required frequency offset. 

 
Connect the equipment as shown in Figure 2-33.  Set the GES Emulator to transmit a P channel on a Mid-Band receive test frequency (Section 2.4.4.1). 
 
 
To determine the resolution of the Doppler correction, adjust the GES Emulator P-channel transmitter frequency 10 Hz below the channel center frequency and measure the resulting transmitter frequency.  Step the GES Emulator transmitter frequency in 1 Hz steps over a range of 21 Hz, measuring the resulting transmitter frequency at each step.  The frequency compensation must be of the opposite sense.  A plot of the transmitter frequency versus the receiver frequency for the 21 steps should show the resolution of the correction. 

Set the GES Emulator to transmit a P channel at the Mid-Band test frequency channel per Section 2.4.4.1 item i.  Set the GES Emulator to receive at the Mid-Band transmit test frequency channel per Section 2.4.4.1, item i.  The ratio of these frequencies is 1.063774684:1. 

 
Command the transceiver to log on and assure its satisfactory completion.  Command the transceiver to transmit a test signal at the Mid-Band test frequency.  The frequencies used must be measured and recorded throughout this test. 
For a system which measures the receive frequency offset to determine the transmit Doppler corrections, cause the GES Emulator to retune this P-channel frequency to the maximum positive Doppler offset as specified in Section 2.2.4.1.8.  Measure and record the transceiver transmit frequency.  Repeat at the most negative Doppler offset.  Analyze the resulting data to determine that the transceiver transmit frequency is within the allowable error value specified in Section 2.2.4.2.14 of the GES transmit frequency multiplied by the above ratio, and in the opposite sense. 
 
 
NOTE: 
For example, for a receive frequency offset of 2180 Hz, the transmit frequency is 
ft = fc - 2319 Hz. 
For a system which uses the aircraft navigational data to determine the required offsets, equivalent input signals may be derived to establish the transmit Doppler corrections. 
 
 
NOTE: 
For example, a relative velocity toward the satellite of 824 knots is equivalent to a received Doppler offset of +2180 Hz at the Mid-Band test frequency.  The corresponding transmit offset is -2319 Hz at the Mid-Band transmit test 
frequency. 

## 2.4.4.3.15 Doppler Rate Capability (Section 2.2.4.2.15)

 
Equipment Required 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 
rating (NARDA Model 3022 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Precision Calibrated Attenuator, 20 dB (NARDA 757C-20 or equivalent). 
 
Gated Microwave Frequency Counter, better than 1 X 10-8 measurement accuracy (HP 
5361A, option 010) 
 
GES Emulator. 

Measurement Procedure The following test is for a transceiver which measures the receive frequency offset to determine the transmit Doppler corrections.  Equivalent input signals may be derived for a transceiver using the aircraft navigational data to determine the required offset. 

Connect the equipment as shown in Figure 2-33.  Set the GES Emulator to operate on a P channel at the Mid-Band test frequency (Section 2.4.4.1).  Cause the transceiver to transmit a continuous signal at the Mid-Band test frequency (Section 2.4.3.1.2).  The output power can be set to any convenient level since this is not important to the measurement, provided the frequency counter has an adequate input level. 

 
Cause the simulated Doppler offset on the GES P-channel frequency to vary at the Doppler 
rate of change specified in Section 2.2.4.1.9 over the range fc - 225 Hz to fc + 225 Hz, where fc is the channel carrier frequency with no Doppler offset.  Record simultaneous, 
synchronized frequency measurements from the two frequency counters for the P-channel frequency and the transmitter frequency for consecutive one-second measurements. 
Repeat the test with the P-channel signal frequency sweeping over a range of 450 Hz which ends at the upper extreme offset specified in Section 2.2.4.1.8. 
Repeat the test with the P-channel signal frequency sweeping over a range of 450 Hz which ends at the lower extreme offset specified in Section 2.2.4.1.8. 
Analyze the data for verification of the frequency accuracy and residual Doppler error rate of change required by Section 2.2.4.2.15. 
 
 
NOTE: 
Known receiver offset frequencies may be indicated by markers from the sweep signal generator.  These marker pulses are used to generate a counter gate to enable a measurement of the resulting transceiver transmitter frequency for these known receiver frequencies.  Enough marker frequencies should be used 
to demonstrate the dynamic Doppler correction characteristics through the 
entire Doppler range. 

## 2.4.4.3.16 Signal Spectrum (Section 2.2.4.2.16) Equipment Required

 
Dual Calibrated Directional Coupler, 20 dB coupling, 60 watts or greater average power 
rating (NARDA Model 3022 or equivalent). 
 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Precision Calibrated Attenuator, 20 dB (NARDA 757C-20 or equivalent). 
 
Spectrum Analyzer, 100 Hz - 18 GHz (HP 8566B or equivalent). 
GES Emulator. 

 
Measurement Procedure 
 
Connect the equipment as shown in Figure 2-31.  For these measurements the transceiver must be transmitting a continuous signal, modulated at the channel rate under test.  Using one of the channel units operating at one of the available channel rates, command the transceiver to transmit a modulated carrier at rated power at the Mid-Band test frequency. 

 
Use the spectrum analyzer to measure the resulting spectrum, which may be very noiselike.  Video averaging may be used in order to make the measurements. 
If all channel unit types are not identical, repeat the tests for each channel unit type at all applicable channel rates. 
 
 
NOTE: 
A pseudo-random binary sequence (PRBS) would be a good choice for the transmitted data.  For a C-channel, this should be easy to create.  For lower data rate R- or T-channels, the format will have to be modified, either in software or hardware, so as to generate a continuous transmission rather than bursts.  In effect, this will be similar to a P-channel operation. 
 
An alternative to continuous transmissions is to place the spectrum analyzer on zero span. Using a suitable frequency step size, such as SR/20 where SR is the Symbol Rate, increment the spectrum analyzer frequency, record and plot the resulting response. 

## 2.4.4.3.17 Transmit Pulse-Shaping Filter Response (Sections 2.2.4.2.17.1 And 2.2.4.2.18.1)

 
Equipment Required 
Directional Coupler, 30 dB coupling, 60 watts average power (NARDA Model 3002-30 or 
equivalent). 
 
High Power Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics Inc. 
Model T-1005 or equivalent). 
 
Signal Analyzer (HP 3561A or equivalent). 
 
GES Emulator. 
Measurement Procedure 
 
 
NOTE: 
This requirement may be verified either by direct measurement or analysis.  For a direct measurement, a signal must be available from the transceiver channel under test from a point within the transmit chain before any signal amplitude compression occurs.  This is an ambient-condition bench test only, so an open unit with access to a test point is acceptable.  For digitally-implemented transmit pulse-shaping filters, analysis may replace direct measurements. 
 ┌──────────────┐ │    GES       │ │  Emulator    │ │              │ 
                          └──┬───────────┘ ^ │ v ┌───────────┐   ┌──┴───────────┐      ┌─────────┐ │           │   │ Directional  │      │  High   │ │ XCVR  Ant.├<─>┤   Coupler    ├─────>┤  Power  │ │       port│   │    30 dB     │      │  Load   │ └───────────┘   └──────────────┘      └─────────┘ │* v                               
          ┌─────┴─────┐ │   Signal  │   * Special test point in transmitter chain -- │  Analyzer │     see Note Section 2.4.4.3.17 │           │ └───────────┘ 

## Figure 2-36.   Transmit Pulse Shaping Filter Response - Section 2.4.4.3.17

 
For verification by a direct measurement, connect the equipment as shown in Figure 2-36. Command the transceiver to transmit a modulated carrier at an A-BPSK or A-QPSK channel rate specified in Section 2.2.4.2.1 on the Mid-Band transmit test frequency (Section 2.4.4.1).  Use the Signal Analyzer to measure the modulated signal. 

 
Repeat this measurement or analysis for all available A-BPSK and A-QPSK channel rates. Verify that the amplitude and phase responses (relative to the carrier center frequency) meet the applicable requirements. 

## 2.4.5 Satellite Subnetwork Data Link Layer Test Requirements (Sections 2.2.5 And 2.2.7)

 
 
NOTE: 
Unlike the other performance verification requirements sections of this 
MOPS, Section 2.4.5 is organized differently from its companion performance requirements Section 2.2.5.  Section 2.2.5 only addresses foundation data link layer 
performance 
requirements 
(upon 
which 
satellite 
subnetwork 
management requirements are added in Section 2.2.6, and Data-2 as well as Data-3 packet-mode data service requirements are added in Section 2.2.7). This section (2.4.5) not only includes the performance verification requirements for Section 2.2.5, but also for the related data link layer requirements for Section 2.2.7 which are specific to Data-2 and Data-3 packet-mode data services.  These two different sets of performance verification requirements are split out in the two parts of Table 2-17, and are signified in the "Reference Document "A"" column headers of the table as 
"(Section 2.2.5)" and "(Section 2.2.7)", respectively. 

## Equipment Required

 
GES Emulator. 
 
8208 Test Set. 
 
Directional Coupler, 30 dB coupling, 60 watts average power rating (NARDA Model 3002-
30 or equivalent). 
 
High Power RF Load, 50 ohms, 60 watts or greater average power rating (RLC Electronics, 
Inc. Model T-1005 or equivalent). 
Measurement Procedure 
Connect the equipment as shown in Figure 2-37.  Refer to Table 2-17 for cross-references between this document and Reference Document "D". 
 
NOTE: 
The absence of entries in the right-hand column may indicate that tests are manufacturerspecific and should be shown by demonstration or analysis; or may simply be related to a high-level statement not intended for testing. 
 Link layer testing is specified in Reference Document "D" Annex 1 Section 4 (Phase 1 tests), including the details in Attachment 1 thereto.  The abstract test descriptions in Attachment 1 comply with the ISO-9646 standardized testing methodology and framework, and are specified using the Tree and Tabular Combined Notation (TTCN) standard test description language.  To take advantage of the standardized link layer detailed test cases, the transceiver must provide the necessary Delayed Echo Application (DEA) software described and referenced below.  The referenced link layer testing includes the following: 
 
4.1  
Assumptions 

 
 
4.2  
Test Suite Structure 
 
 
4.2.1  
Proper Test Cases 
 
 
4.2.2  
Improper Test Cases 
 
 
4.2.3  
Inopportune Test Cases 
 
 
4.2.4  
Mandatory and Optional Tests 
 
 
4.2.5  
Test Case Identifier Number 
 
 
4.3  
Test Suite Requirements 
 
 
4.3.1  
DL1 - Basic DLS Functions on P- and R- Channels 
 
 
4.3.1.1 
(Information only) 
 
 
4.3.1.2 
DL1 Test Cases 
 
 
4.3.2  
DL2 - SU-Set Assembly Functions on the P-Channel 
 
 
4.3.2.1 
(Information only) 
 
 
4.3.2.2 
DL2 Test Cases 
 
 
4.3.3  
DL3 - Priority and Buffering Functions on the R-Channel 
 
 
4.3.3.1 
(Information only) 
 
 
4.3.3.2 
DL3 Test Cases 
 
 
4.3.4  
DL4 - RLS Receive Functions on the P-Channel 
 
 
4.3.4.1 
(Information only) 
 
 
4.3.4.2 
DL4 Test Cases 
 
 
4.3.5  
DL5 - RLS Transmit Functions on the R-Channel 
 
 
4.3.5.1 
(Information only) 
 
 
4.3.5.2 
DL5 Test Cases 

|     |     | 4.3.6     | DL6 - T-Channel Reservation Protocol          |
|-----|-----|-----------|-----------------------------------------------|
|     |     | 4.3.6.1   | (Information only)                            |
|     |     | 4.3.6.2   | DL6 Test Cases                                |
|     |     | 4.3.7     | DL7 - DLS Transmit Functions on the T-Channel |
|     |     | 4.3.7.1   | (Information only)                            |
|     |     | 4.3.7.2   | DL7 Test Cases                                |
|     |     | 4.3.8     | DL8 - RLS Transmit Functions on the T-Channel |
|     |     | 4.3.8.1   | (Information only)                            |
|     |     | 4.3.8.2   | DL8 Test Cases                                |
|     |     | 4.3.9     | DL9 - R-/T-channel LSDU Transmission          |
|     |     | 4.3.9.1   | (Information only)                            |
|     |     | 4.3.9.2   | DL9 Test Cases                                |
|     |     | 4.3.10    | DL10 - Link Layer Timing Requirements         |
|     |     | 4.3.10.1  | (Information only)                            |
|     |     | 4.3.10.2  | DL10 Test Cases                               |

 
 
NOTE: 
Individual test groups are only applicable if the service is supported. ┌────────────────┐           ┌────────────────┐ │                │           │                │ │   ISO 8208*    │           │      GES       │ │   Test Set     ├<─────────>┤   Emulator     │ │                │           │                │ └───────┬────────┘           └────────┬───────┘ ^                             ^ │ Packets *                   │  SNPDUs * v                             v ┌───────┴────────┐           ┌────────┴───────┐ │                │           │                │     ┌────────┐ │   XCVR         │           │  Directional   │     │  High  │ │           Ant  ├<─────────>┤    Coupler     ├────>┤  Power │ │           Port │           │     30 dB      │     │  Load  │ └───────┬────────┘           └────────────────┘     └────────┘ ^ │ 
               v ┌───────┴────────┐ │                │  
* Req'd for 2.4.7 and 2.4.9 only; the XCVR and 
       │   Telephone    │  
  Test Set exchange ISO 8208 packets, while the 
       │   Hand Set #   │  
  XCVR and the GES Emulator exchange SNPDUs. 

       │                │  
# Required for 2.4.8 and 2.4.9 only 
       └────────────────┘ 

| Reference Document                                     |          | Reference                                               |
|--------------------------------------------------------|----------|---------------------------------------------------------|
| Document                                               | "B"      | Reference Document "D"                                  |
| "A"                                                    | Annex 1  |                                                         |
| (Section 2.2.5)                                        |          |                                                         |
| 4.1                                                    | 6.1, 6.4 | Included in most test cases (SU format/ element coding) |
| 4.2                                                    | 6.4      | Included in most test cases (SU format/ element coding) |
| 4.3                                                    | 6.4      | N/A - Definition                                        |
| 4.3.1                                                  | 6.4      | Indirectly through DL1-DL3                              |
| 4.3.2                                                  | 6.4,     |                                                         |
| Annex 1 Table CR4.1                                    |          |                                                         |
| DL1_108, DL1_118, DL2_101, DL2_102 DL2_103,            |          |                                                         |
| DL2_104, DL2_105, DL2_203, DL2_204, DL2_206,           |          |                                                         |
| DL2_301, DL3_101 DL3_102, DL3_103, DL3_104,            |          |                                                         |
| DL4_103, DL5_109, DL7_103, DL7_104, DL7_105,           |          |                                                         |
| DL7_106, DL7_107, DL8_112                              |          |                                                         |
| 4.3.3                                                  | 6.4      | DL5_201, DL5_202, DL5_203, DL5_204, DL6_204,            |
| DL6_209, CM111_201, CM111_202, CM111_203,              |          |                                                         |
| CM111_301, CM111_302, CM213_201                        |          |                                                         |
| 4.3.4                                                  | 6.4,     |                                                         |
| Annex 1 Table CR4.1                                    |          |                                                         |
| DL1_108, DL1_118, DL2_101, DL2_102 DL2_103,            |          |                                                         |
| DL2_104, DL2_105, DL2_203, DL2_204, DL2_206,           |          |                                                         |
| DL2_301, DL3_101 DL3_102, DL3_103, DL3_104,            |          |                                                         |
| DL4_103, DL5_109, DL7_103, DL7_104, DL7_105,           |          |                                                         |
| DL7_106, DL7_107, DL8_112                              |          |                                                         |
| 4.3.5                                                  | 6.4,     |                                                         |
| Annex 1 Table CR4.1                                    |          |                                                         |
| DL1_108, DL1_118, DL2_101, DL2_102 DL2_103,            |          |                                                         |
| DL2_104, DL2_105, DL2_203, DL2_204, DL2_206,           |          |                                                         |
| DL2_301, DL3_101 DL3_102, DL3_103, DL3_104,            |          |                                                         |
| DL4_103, DL5_109, DL7_103, DL7_104, DL7_105,           |          |                                                         |
| DL7_106, DL7_107, DL8_112                              |          |                                                         |
| 4.3.6                                                  | 6.4      | Included in most test cases                             |
|                                                        | 6.2      | Included in relevant test cases  (signaling SUs are     |
| expected on the designated channel)                    |          |                                                         |
|                                                        | 6.3.1    | Included in relevant test cases                         |
| (signaling SUs are expected on the designated channel, |          |                                                         |
| independently from the AES hardware configuration)     |          |                                                         |
|                                                        | 6.3.2    | DL5_201, DL6_119, SNM12_101                             |
|                                                        | 6.5      | N/A - test conditions                                   |
|                                                        | 6.5.1    | Included in most test cases in 2.4.6, Table 2-18        |
|                                                        | 6.5.2    | DL10_101                                                |
|                                                        | 6.5.3    | DL4_204                                                 |
|                                                        | 6.6      | DL3_105, most of DL2_XXX                                |
|                                                        |          |                                                         |
|                                                 | Reference                                    |
|-------------------------------------------------|----------------------------------------------|
| Document                                        |                                              |
| Reference                                       |                                              |
| Document                                        | Reference Document "D"                       |
| "A"                                             | "B"                                          |
| (Section 2.2.7)                                 |                                              |
| 7.1                                             |                                              |
| 7.1.1                                           |                                              |
| 7.1.2                                           |                                              |
|                                                 | DL1_101, DL1_102, DL1_103, DL1_109, DL1_110, |
| DL1_111, DL4 Test Group                         |                                              |
| 7.2.1.1                                         |                                              |
| (Protocol                                       |                                              |
| overview)                                       |                                              |
|                                                 |                                              |
| 7.2.1.2                                         |                                              |
| 7.2.1.3                                         |                                              |
| 7.2.1.4                                         |                                              |
| 7.2.1.5                                         |                                              |
| DL4_206                                         |                                              |
| 7.2.1.6                                         |                                              |
| 7.2.1.7                                         |                                              |
| 7.2.2.1                                         |                                              |
| (Protocol                                       |                                              |
| overview)                                       |                                              |
|                                                 |                                              |
|                                                 | DL1_104, DL1_105, DL1_106, DL1_112, DL1_113, |
| DL1_114, DL1_115, DL1_116, DL1_117, DL3 and     |                                              |
| DL5 Test Groups                                 |                                              |
| 7.2.2.2                                         |                                              |
| 7.2.2.3                                         |                                              |
| 7.2.2.4                                         |                                              |
| 7.2.2.5                                         |                                              |
| 7.2.2.6                                         |                                              |
| For MOPS 2.2.7.4.2:  4.3.3,                     |                                              |
| DL3_101, to DL3_105.                            |                                              |
|                                                 | DL6, DL7 and DL8 Test Groups                 |
| (Protocol                                       |                                              |
| overview)                                       |                                              |
|                                                 |                                              |
| 7.2.3.2                                         |                                              |
| 7.2.3.3                                         |                                              |
| 7.2.3.4                                         |                                              |
| DL8_109, DL8_110                                |                                              |
| 7.2.3.5                                         |                                              |
| 7.2.3.6                                         |                                              |
| For MOPS 2.2.7.4.2:  4.3.8, DL8_101 to DL8_303. |                                              |
|                                                 | N/A                                          |
| (Introduction/                                  |                                              |
| Definition)                                     |                                              |
|                                                 |                                              |
|                                                 | DL6 Test Group and DL8_208, DL8_209          |
| (Protocol                                       |                                              |
| overview)                                       |                                              |
| 7.2.4.1.2                                       |                                              |
| DL6_202, DL6_203, DL6_205, DL6_206, DL6_207     |                                              |
|                                         | Reference                          |
|-----------------------------------------|------------------------------------|
| Document                                |                                    |
| Reference                               |                                    |
| Document                                | Reference Document "D"             |
| "A"                                     | "B"                                |
| (Section 2.2.7)                         |                                    |
|                                         | DL6_110, DL6_111, DL6_208, DL6_209 |
| 7.2.4.1.5                               |                                    |
| 7.2.4.1.4                               |                                    |
| 7.2.4.2                                 |                                    |
| For MOPS 2.2.7.4.2:  4.3.6,             |                                    |
| DL6_101 to DL6_302.                     |                                    |
| 7.2.5                                   |                                    |
| A3 - 3.1                                |                                    |
| DL7_101 to DL7_107,                     |                                    |
| DL8_101 to DL8_303.                     |                                    |
| A3 - 3.1.1                              |                                    |
| DL7_101 to DL7_107,                     |                                    |
| DL8_101  to DL8_303.                    |                                    |
| A3 - 3.1.2                              |                                    |
| DL8_101 to DL8_303.                     |                                    |
| A3 - 3.2                                |                                    |
| DL9_101, DL9_102.                       |                                    |
| A3 - 3.2.1                              |                                    |
| DL8_101 to DL8_303.                     |                                    |
| A3 - 3.2.2                              |                                    |
| DL 9_101, DL9_102                       |                                    |
| A3 - 3.2.3                              |                                    |
| DL9_101, DL9_102.                       |                                    |
| A3 - 4.1                                |                                    |
| DL6_101 to DL6_302.                     |                                    |
| A3 - 4.1.1                              |                                    |
| A3 - 4.1.2                              |                                    |
| A3 - 4.1.3                              |                                    |
| A3 - 4.1.4                              |                                    |
| A3 - 4.1.5                              |                                    |
| A3 - 4.2                                |                                    |
| A3 - 4.2.1                              |                                    |
|                                         | 9.3.2                              |
|                                         | 9.4.1.1                            |
|                                         | 9.4.1.2                            |
|                                         | 9.4.1.3                            |
|                                         | 9.5.1                              |
| DL4_101 to DL4_302, DL5_101 to DL5_302, |                                    |
| DL7_101 to DL7_107, DL8_101 to DL8_303. |                                    |
|                                         | 9.5.2                              |

 
The Delayed Echo Application (DEA) is an optional satellite data link layer application which may be provided in the transceiver (see Reference Document "B" Section 8). Although not mandatory, it permits testing of the transceiver satellite data link protocol by means of a standardized test software.  Test cases are defined between an "upper tester" (DEA software functions built into the transceiver) and a "lower tester" (software functions built into the GES Emulator which provides during test execution total control and observation, remotely from the transceiver satellite link layer under test, using the DEA protocol).  The DEA Protocol (DEAP) enables the lower tester to both "see" the effects of its actions on the upper tester and cause the upper tester to make the Implementation Under Test (IUT) initiate actions.  All tests are initiated by the lower tester. 

The DEAP Data Units (DEAPDUs) are carried as user data in the satellite Link Protocol Data Units (LPDUs, or SUs).  The DEA interfaces to the link layer in the same way as other link service users, using a Link Interface Data Unit (LIDU) for transporting Link Service Data Units (LSDUs) and/or parameters across the interface.  For data communication, the first octets of the LSDU are defined to provide switch capability between the different link service users. 

The minimum requirements for the DEA, if it is provided in the transceiver, shall be the minimums specified in Reference Document "B" Section 8, including all Sections and all referenced figures.  This includes the following: 

 
 
8.1  
(Information only) 
 
 
8.1.1  
Reaction Queue 
 
 
8.1.2  
LIDU Buffer 
 
 
8.2  
Definition of the DEAP 
 
 
8.2.1  
Implicit reactions 
 
 
8.2.2  
Explicit reactions 
 
 
8.2.2.1 
Definition of DEAPDU sent by the Lower Tester 
 
 
8.3  
Processing of valid explicit reaction 
 
 
8.3.1  
Processing an "Execute queue" 
 
 
8.3.2  
Processing a "send data" 
 
 
8.3.2.1 
Delayed reactions 
 
 
8.3.2.2 
Immediate reactions 
 
 
8.4  
Building a reaction 
 
 
8.4.1  
Building the Link Interface control Information  
 
 
8.4.2  
Building User-Data (DEAPDU sent by the DEA)  
 
 
8.4.2.1 
Echo 
 
 
8.4.2.2 
Reporting 

## 2.4.6 Satellite Subnetwork Management Test Requirements (Section 2.2.6)

 
Equipment Required 
GES Emulator. 
 
Directional Coupler, 30 dB coupling, 60 watts average power rating (NARDA Model 3002-
30 or equivalent). 
 
High Power RF Load, 50 ohms, greater than 60 watts average power rating (RLC 
Electronics, Inc. Model T-1005 or equivalent). 
 
 
Measurement Procedure 
Connect the equipment as shown in Figure 2-37.  Refer to Table 2-18 for cross-references between this document and Reference Document "D". 
 
The following three tests are for verification of the performance requirements in Reference Document "A", Section 5.2.13.3 (Section 2.2.6 of this document).  The intent of these tests is to confirm the actions of the AES unit under test in the event that the GES rejects the log-on attempt by the AES due to congestion or due to invalid parameters in the Log-on request.  Three test cases are provided which correspond to each of the GES rejection categories below; permanent unavailability, temporary unavailability, and invalid parameters. 

For each of three test cases, instruct the AES unit under test to attempt log-on to the GES emulator by transmitting a log-on request LIDU using a test setup as illustrated in Figure 2-37.  Program the GES emulator to send a log-on reject LIDU, with the reason code set to the values indicated below, in response to the AES's log-on request LIDU. 

 
1. Permanent Unavailability:  Program the GES emulator to reject the log-on request by 
replying with a log-on reject LIDU with the reason code set to 1.  Observe that the AES will not re-attempt to log-on to this same GES for the duration of the current flight.  Repeat the same case and have the user command a log-on to this GES and observe that the AES will attempt to log-on to the GES.  Repeat the above with the log-on reject reason code set to 8, 9, and 15. 
 
2. Temporary Unavailability:  Program the GES emulator to reject the log-on request by 
replying with a log-on reject LIDU with the reason code set to 0.  Observe that the AES will re-attempt to log-on to the same GES only after trying all other possible GESs in the Satellite region.  Repeat the above with the log-on reject reason code set to 3, 7, and 14. 
 
3. Invalid Parameters:  For this procedure, instruct the AES to send a log-on request 
LIDU with invalid parameters.  Program the GES emulator to reject the log-on request by replying with a log-on reject LIDU with the reason code set to 2.  Observe that the AES will re-attempt log-on to the same GES by sending a log-on request with parameters that are correct.  Repeat the above with the log-on reject reason code set to 5 and 6. 
 
The following two tests are for verification of the performance requirements in Reference Document "A", Section 5.2.14 (Section 2.2.6 of this document).  The intent of these performance verification procedures is to verify both normal and abnormal AES log-off procedures. 

 
1. Normal:  While a call is in progress, manually initiate a log-off of the logged on AES 
unit under test.  Observe that the AES unit under test aborts the call in progress and 
transmits a Log-off Request.  Instruct the GES emulator to respond within tA10 seconds with a log-off acknowledgment.  Confirm that the status of the AES is "logged off". 

 
2. Abnormal:  Manually initiate a log-off of the logged on AES unit under test.  
Program the GES emulator to not respond to the AES.  Verify that the AES waits tA10 seconds and retransmits the Log-off request.  Verify that the AES repeats this procedure four additional times while not receiving a response form the GES.  After the fifth transmission and expiry of the tA10 timer, the AES management considers the AES logged off.  Confirm that the status of the AES is "logged off". 
 
Satellite network management testing is specified in Reference Document "D" Annex 1 Section 5 (Phase 1 tests), including the details in Attachment 2 Section 4, and Annex 3 Section 3 (Phase 2 tests).  The abstract test descriptions in Attachment 2 are in compliance with the ISO-9646 standardized testing methodology and framework, and are specified using the Tree and Tabular Combined Notation (TTCN) standard test description language. Transceivers which do not support spot beam handover are not required to perform test group SNM3; all other test groups are mandatory.  The referenced satellite network management testing includes the following: 

 
Reference Document "D" Annex 1 Section 5: 
 
5.2  
Satellite Network Management Test Suite Structure 
 
 
5.3  
Test Suite Structure 
 
 
5.3.1  
Proper Test Cases 
 
 
5.3.2  
Improper Test Cases 
 
 
5.3.3  
Inopportune Test Cases 
 
 
5.3.4  
Mandatory and Optional Tests 
 
 
5.3.5  
Test Case Identifier Numbers 
 
 
5.4  
Test Suite Requirements 
 
 
5.4.1  
SNM1 - Satellite Selection 
 
 
5.4.1.1 
(Information only) 
 
 
5.4.1.2 
SNM1 Test Cases 
 
 
5.4.2  
SNM2 - System Table Update 
 
 
5.4.2.1 
(Information only) 
 
 
5.4.2.2 
SNM2 Test Cases 
 
 
5.4.3  
SNM3 - Spot Beam Map Update 
 
 
5.4.3.1 
(Information only) 
 
 
5.4.3.2 
SNM3 Test Cases 
 
 
5.4.4  
SNM4 - Selection of Log-on GES 
 
 
5.4.4.1 
(Information only) 
 
 
5.4.4.2 
SNM4 Test Cases 
 
 
5.4.5  
SNM5 - User Commanded Log-on 
 
 
5.4.5.1 
(Information only) 
 
 
5.4.5.2 
SNM5 Test Cases 
 
 
5.4.6  
SNM6 - Automatic Log-on 
 
 
5.4.6.1 
(Information only) 
 
 
5.4.6.2 
SNM6 Test Cases 

|     |     | 5.4.7     | NOT APPLICABLE (SNM7 - Unused)        |
|-----|-----|-----------|---------------------------------------|
|     |     | 5.4.8     | SNM8 - Log-off                        |
|     |     | 5.4.8.1   | (Information only)                    |
|     |     | 5.4.8.2   | SNM8 Test Cases                       |
|     |     | 5.4.9     | SNM9 - Log-on Renewal                 |
|     |     | 5.4.9.1   | (Information only)                    |
|     |     | 5.4.9.2   | SNM9 Test Cases                       |
|     |     | 5.4.10    | SNM10 - Direct Log-on Verification    |
|     |     | 5.4.10.1  | (Information only)                    |
|     |     | 5.4.10.2  | SNM10 Test Cases                      |
|     |     | 5.4.11    | SNM11 - Log-on Prompt                 |
|     |     | 5.4.11.1  | (Information only)                    |
|     |     | 5.4.11.2  | SNM11 Test Cases                      |
|     |     | 5.4.12    | SNM12 - Data Channel Reassignment     |
|     |     | 5.4.12.1  | (Information only)                    |
|     |     | 5.4.12.2  | SNM12 Test Cases                      |
|     |     | 5.4.13    | SNM13 - Broadcast Selective Release   |
|     |     | 5.4.13.1  | (Information only)                    |
|     |     | 5.4.13.2  | SNM13 Test Cases                      |
|     |     | 5.4.14    | SNM14 - Spot Beam Log-On and Handover |
|     |     | 5.4.14.1  | (Information only)                    |
|     |     | 5.4.14.2  | SNM14 Test Cases                      |
|     |     | 5.4.15    | NOT APPLICABLE (SNM15 - Unused)       |
|     |     | 5.4.16    | NOT APPLICABLE (SNM16 - Unused)       |
|     |     | 5.4.17    | SNM17 - Owner/Operator Table          |
|     |     | 5.4.17.1  | (Information only)                    |
|     |     | 5.4.17.2  | SNM17 Test Cases                      |
|     |     | 5.4.18    | SNM18 - Log-on Confirm Table          |
|     |     | 5.4.18.1  | (Information only)                    |
|     |     | 5.4.18.2  | SNM18 Test Cases                      |

 
Reference Document "D" Annex 3 Section 2: 
 
3.1  
Initial Search Test 
 
 
3.2  
Log On Reject Test 
 
 
3.3  
Normal Log-On Test 
 
 
3.4  
P-channel Degradation Test 

| Reference Document "A"    | Reference Document "D"    |
|---------------------------|---------------------------|
| (Section 2.2.6)           |                           |
| Reference                 |                           |
| Document                  | Annex 1                   |
| "B"                       |                           |
| 5.1                       |                           |
| 5.2                       |                           |
| 5.2.2                     |                           |
| SNM6_101                  |                           |
| 5.2.3                     |                           |
| Reference Document "A"              | Reference Document "D"       |
|-------------------------------------|------------------------------|
| (Section 2.2.6)                     |                              |
| Reference                           |                              |
| Document                            | Annex 1                      |
| "B"                                 |                              |
| SNM2_104, SNM2_301, SNM3_101,       |                              |
| SNM3_103, SNM3_105                  |                              |
| 5.2.4                               |                              |
| 5.2.5                               |                              |
| SNM6_101, SNM6_204, SNM6_205        |                              |
| 5.2.6                               |                              |
| e.g. SNM5_101, SNM6_101             |                              |
| 5.2.7                               |                              |
| SNM6_101                            |                              |
| 5.2.8                               |                              |
| 5.2.9                               |                              |
| 5.2.10                              |                              |
| SNM14_106                           |                              |
| 5.2.11                              |                              |
| 5.2.11.1                            |                              |
| SNM2_104                            |                              |
| 5.2.11.2                            |                              |
| SNM3_301                            |                              |
|                                     |                              |
| (see Section 2.4.6)                 |                              |
|                                     | SNM8_101, SNM8_102, SNM8_201 |
| (see Section 2.4.6)                 |                              |
| 5.2.15                              |                              |
| 5.2.17                              |                              |
| 5.2.18                              | 7.3.1                        |
| SNM5_203, SNM6_203, SNM12_204       |                              |
| 5.3  (introduction)                 |                              |
| 5.3.1                               |                              |
| SNM6_202, SNM6_203, SNM12_202.      |                              |
| SNM12_204                           |                              |
|                                     |                              |
| (see Section 2.4.6.1)               |                              |
|                                     |                              |
| (see Section 2.4.6.2)               |                              |
| 5.3.4                               |                              |
| 5.5  (introduction)                 |                              |
| 5.5.1                               | 7.4.1                        |
| SNM2_104, SNM2_301 (Buffer size not |                              |
| tested)                             |                              |
| 5.5.2                               | 7.4.2                        |
| SNM18_104 (Buffer size not tested)  |                              |
| 5.5.3                               | 7.4.2                        |
| 5.5.4                               | 7.4.3                        |
| setup (Buffer size not tested)      |                              |
| Reference Document "A"    | Reference Document "D"    |
|---------------------------|---------------------------|
| (Section 2.2.6)           |                           |
| Reference                 |                           |
| Document                  | Annex 1                   |
| "B"                       |                           |
| 5.5.5                     | 7.4.4                     |
| size not tested)          |                           |
| 5.6  (introduction)       |                           |
| 5.6.1                     |                           |
| 5.6.2                     |                           |
| 5.6.3                     |                           |
|                           | 7.3                       |
|                           | 7.3.1                     |
|                           | 7.3.3                     |
|                           | 7.4                       |

 NOTE: 
The absence of entries in the right-hand column may indicate that tests are manufacturerspecific and should be shown by demonstration or analysis; or may simply be related to a high-level statement not intended for testing.  

## 2.4.6.1 Manually Initiated Ges-To-Ges Handover (Section 2.2.6)

 
 
Cause the AES unit under test to log-on to the GES emulator.  Manually initiate the AES to change its Log-on GES to another GES operating within the same satellite region. Observe that any previously established communication channels are maintained until clearing. 
In the case that the AES can only transmit on one carrier at a time, confirm that a GES- GES handover procedure is initiated only when the AES unit under test is not busy.  In the case that the AES has a multiple channel transmission capability, verify that the handover procedure may proceed (i.e., sends a new Log-on request) even if the AES has some busy C-Channels.  

## 2.4.6.2 User Command Satellite-To-Satellite Handover (Section 2.2.6)

 
 
The intent of the following test procedure is to verify that the AES shall wait a specified period of time prior to performing a satellite-to-satellite handover when connections are established.  First cause the AES unit under test to log-on to the GES emulator. Manually initiate the AES to perform a satellite-to-satellite handover under the following conditions. 
 
i) 
Manually initiate the AES to perform a satellite-to-satellite handover while no calls are ongoing.  Verify that the AES unit under test meets the requirements of Section 2.2.6. 
ii) 
 
Manually initiate the AES to perform a satellite-to-satellite handover while communications are established.  Verify that the AES unit under test will not immediately initiate the handover procedure, however will wait a time supervision period of three minutes (provided all calls are not cleared in that 
time).  Verify that the AES unit under test meets the requirements of Section 2.2.6.  

## 2.4.6.3 Selective Release (Section 2.2.6)

 
 
Using the GES emulator, create and send a Selective Release SU with a designated channel to the Logged-on AES unit under test.  Confirm that the AES ceases transmission on the frequency designated in the Selective Release SU within 4 seconds from the time when the trailing edge of the unique word preceding the frame containing the Selective Release SU is received at the antenna. 

## 2.4.7 Satellite Subnetwork Packet-Mode Data Service Test Requirements (Section 2.2.7)

 
NOTE: 
Section 2.4.5 contains the performance verification requirements for the 
foundation data link layer requirements, and the related data link layer requirements which are specific to Data-2 and Data-3 packet-mode data services.  This section (2.4.7) adds the performance verification requirements for the satellite subnetwork-dependent (SSND) sublayer for Data-3, and for 
the Data-3 service ISO 8208 DCE. 
Equipment Required 
GES Emulator. 
 
Directional Coupler, 30 dB coupling, 60 watts average power rating (NARDA Model 3002-
30 or equivalent). 
 
High Power RF Load, 50 ohms, greater than 60 watts average power rating (RLC 
Electronics, Inc. Model T-1005 or equivalent). 
 
ISO 8208 Test Set (herein referred to as the Test Set), commercially available equipment 
(or equivalent). 
Test Procedures 
Connect the equipment as shown in Figure 2-37.  Perform the tests specified in Sections 2.4.7.1 (Data-2), 2.4.7.2 (Data-3 SSND), 2.4.7.3 (Data-3 ISO 8208 DCE), and 2.4.7.4 (Data-3 Join/Leave Events), as applicable.  For the tests specified in Section 2.4.7.4, depending on the specific transceiver implementation, an appropriate avionics test set may be substituted for the ISO 8208 Test Set.  Refer to Table 2-19 for cross references between this document and Reference Document "D". 
 
 
NOTE: 
The absence of entries in the right-hand column may indicate that tests are manufacturer-specific and should be shown by demonstration or analysis; or may simply be related to a high-level statement not intended for testing. 

| Reference                               | Reference                               | Reference Document "D"                    |
|-----------------------------------------|-----------------------------------------|-------------------------------------------|
| Document "A"                            | Document                                | (Test cases)                              |
| "B"                                     |                                         |                                           |
| 7.1.1                                   |                                         | Indirectly tested through all test suites |
| 7.1.3                                   |                                         | Indirectly tested                         |
| 7.1.4                                   |                                         | Indirectly tested throughout PMTS         |
| 7.1.4.1                                 |                                         | Indirectly tested throughout PMTS         |
| 7.1.5                                   |                                         | Indirectly tested throughout PMTS         |
| 7.1.6                                   |                                         | Tested throughout PMTS                    |
| 7.1.7                                   |                                         | PM19_102, PM19_103, PM1_209, PM2_205      |
| 7.3                                     |                                         | Tested throughout PMTS                    |
| 7.3.1                                   |                                         | 7.3.1.2,                                  |
| PM1_101 to PM1_309                      |                                         |                                           |
| 7.3.1.1                                 |                                         | PM2_102, PM17_106                         |
| 7.3.1.2                                 |                                         | PM1_101, PM1_202, PM1_203, PM1_204,       |
| PM18_101, PM18_102, PM18_103, PM18_105, |                                         |                                           |
| PM18_107, PM18_109, PM18_110, PM18_111, |                                         |                                           |
| PM18_112, PM18_113, PM18_114, PM18_201  |                                         |                                           |
|                                         | Tested throughout PMTS                  | 7.3.2                                     |
| (introduction)                          |                                         |                                           |
|                                         |                                         |                                           |
| 7.3.2.1                                 |                                         | PM5_101, PM5_102, PM17_105                |
| 7.3.2.2                                 |                                         | PM1_102, PM2_101, PM3_101, PM4_101,       |
| PM18_108                                |                                         |                                           |
| 7.3.2.3                                 |                                         | Tested throughout PM1_3XX to PM4_3XX      |
| 7.3.3                                   |                                         |                                           |
| (introduction)                          |                                         |                                           |
|                                         |                                         |                                           |
|                                         | PM1_303 to PM1_309, PM2_302 to PM2_308, |                                           |
| PM3_304 to PM3_310, PM5_302 to PM5_308, |                                         |                                           |
| PM7_101 and PM16 Test Group             |                                         |                                           |
| 7.3.3.1                                 |                                         | PM7_101, PM14_101, PM14_102, PM16_101,    |
| PM16_102, PM17_101                      |                                         |                                           |
| 7.3.3.3                                 |                                         | PM7_103, PM7_104, PM15_102, PM15_301,     |
| PM16_108, PM16_109                      |                                         |                                           |
|                                         | N/A                                     | 7.3.3.4                                   |
| (introduction)                          |                                         |                                           |
|                                         |                                         |                                           |
| Reference                                   | Reference                                        | Reference Document "D"                            |
|---------------------------------------------|--------------------------------------------------|---------------------------------------------------|
| Document "A"                                | Document                                         | (Test cases)                                      |
| "B"                                         |                                                  |                                                   |
| 7.3.3.4.1                                   |                                                  | PM13_101, PM17_103                                |
| 7.3.3.4.2                                   |                                                  | PM10_101, PM15_101                                |
| 7.3.4                                       |                                                  | Tested throughout PM8 Test Group                  |
| 7.3.4.1                                     |                                                  | PM8_101, PM8_102                                  |
| 7.3.4.2                                     |                                                  | PM7_102                                           |
| 7.3.5                                       |                                                  |                                                   |
| (introduction)                              |                                                  |                                                   |
|                                             |                                                  |                                                   |
|                                             | Cause Code and Diagnostic Code tested throughout |                                                   |
| PMTS (invalid and inopportune test cases)   |                                                  |                                                   |
| 7.3.5.1                                     |                                                  | N/A                                               |
| 7.3.5.1.1                                   |                                                  | 7.3.20,                                           |
| PM22_101 to PM22_119                        |                                                  |                                                   |
|                                             | N/A                                              | 7.3.5.1.2                                         |
| (introduction)                              |                                                  |                                                   |
|                                             |                                                  |                                                   |
| 7.3.5.1.2.1                                 |                                                  | PM14_301, PM14_303, PM15_302                      |
| 7.3.5.1.2.2                                 |                                                  | PM17 Test Group                                   |
| 7.3.5.1.3                                   |                                                  | All invalid or inopportune test cases within PMTS |
| 7.3.6                                       |                                                  | N/A                                               |
|                                             | Tested Throughout PM20 and PM21 Test Groups      | 7.3.6.1                                           |
| (introduction)                              |                                                  |                                                   |
|                                             |                                                  |                                                   |
| 7.3.6.2                                     |                                                  | N/A                                               |
| 7.3.6.2.1                                   |                                                  | PM20_102, PM20_103                                |
| 7.3.6.2.2                                   |                                                  | PM2_101, PM2_102, PM17_106, PM1_101,              |
| PM1_202, PM1_203, PM1_204, PM18 Test Group, |                                                  |                                                   |
| PM5_101, PM5_102, PM17_105 and throughout   |                                                  |                                                   |
| PM1_3XX to PM4_3XX                          |                                                  |                                                   |
| 7.3.6.2.3                                   |                                                  | PM20_102, PM20_103, PM21_101, PM21_102            |
| 7.3.6.3                                     |                                                  | N/A                                               |
| 7.3.6.3.1                                   |                                                  | PM20_106, PM20_107                                |
| 7.3.6.3.2                                   |                                                  | PM20_106, PM20_107, PM20_108, PM20_109,           |
| PM21_105, PM21_107, PM21_108                |                                                  |                                                   |
| 7.3.6.4                                     |                                                  | Tested throughout PMTS when SNS-User Data are     |
| Reference                               | Reference    | Reference Document "D"                         |
|-----------------------------------------|--------------|------------------------------------------------|
| Document "A"                            | Document     | (Test cases)                                   |
| "B"                                     |              |                                                |
| transferred in SNPDUs                   |              |                                                |
| 7.3.6.5                                 |              | PM20_110, PM21_109, PM16_103                   |
| 7.3.6.6                                 |              | PM18_115, PM18_116, PM18_117, PM20_111,        |
| PM20_201, PM20_202, PM21_110, PM21_111, |              |                                                |
| PM21_112, PM21_113                      |              |                                                |
| 7.3.6.7                                 |              | N/A                                            |
| 7.3.6.7.1                               |              | PM20_114                                       |
| 7.3.6.7.2                               |              | PM20_114, PM20_115, PM21_115, PM21_116         |
| 7.3.6.8                                 |              | PM20_116, PM20_117, PM20_118, PM21_117,        |
| PM21_118, PM21_119                      |              |                                                |
| 7.3.6.9                                 |              | PM20_119, PM20_120, PM21_120                   |
| 7.3.6.10                                |              | PM20_121, PM21_121                             |
| 7.3.6.11                                |              | PM20_113, PM21_114                             |
| A7 - 1.3                                |              | 7.3.16,                                        |
| PM18_101, PM18_102, PM18_103            |              |                                                |
| A7 - 1.4.1.1                            |              | 7.3.16,                                        |
| PM18_103                                |              |                                                |
| A7 - 1.4.2                              |              | 7.3.16,                                        |
| PM18_103                                |              |                                                |
| A10 - 3                                 |              | 7.3.17,                                        |
| PM19 (all)                              |              |                                                |
| A10 - 4.1.4                             |              | 7.3.20,                                        |
| PM22_112                                |              |                                                |
|                                         | 9.3          | N/A                                            |
|                                         | 9.3.1        | Tested Throughout PM18, PM20, PM21 Test Groups |
|                                         | 9.3.2        | Tested throughout PMTS                         |
|                                         | 9.4          | N/A                                            |
|                                         | 9.4.1.1      | 4.3.10,                                        |
| DL10_102                                |              |                                                |
| Reference                          | Reference    | Reference Document "D"                     |
|------------------------------------|--------------|--------------------------------------------|
| Document "A"                       | Document     | (Test cases)                               |
| "B"                                |              |                                            |
|                                    | 9.4.1.2      | 4.3.10, DL10_103                           |
|                                    | 9.4.1.3      | 4.3.10,                                    |
| DL10_103                           |              |                                            |
|                                    | 9.5.1        |                                            |
| 4.3.3, 4.3.4, 4.3.5, 4.3.7, 4.3.8, |              |                                            |
| DL3_101 to DL3_105,                |              |                                            |
| DL4_101 to DL4_302,                |              |                                            |
| DL5_101 to DL5_302,                |              |                                            |
| DL7_101 to DL7_107,                |              |                                            |
| DL8_101 to DL8_303                 |              |                                            |
|                                    | 9.5.2        | PM19_101 (test partially the requirements) |

## 2.4.7.1 Packet-Mode Data-2 Service Test Requirements (Section 2.2.7)

 
The referenced packet-mode Data-2 service testing includes the following: 
Reference Document "D" Annex 3 Section 4: 
 
4.2  
Data Communications Service 
 
 
4.2.1  
Ground-to-Air Message Transfer Test 
 
 
4.2.2  
Air-to-Ground Short Message Transfer Test 
 
 
4.2.3  
Air-to-Ground Long Message Transfer Test 
 
 
4.2.4  
Air-to-Ground Message Transfer Test 
 
 
4.2.5  
Mixed Air-to-Ground and Ground-to-Air Message Transfer Test 

## 2.4.7.2 Packet-Mode Data-3 Service Ssnd Sublayer Test Requirements (Section 2.2.7)

 
The packet-mode Data-3 service SSND sublayer test requirements are specified in Reference Document "D" Annex 1 Section 7, including the details in Attachment 4 and in Annex 3 Section 4.  The abstract test descriptions in Attachment 4 are in compliance with the ISO-9646 standardized testing methodology and frame work, and are specified using the Tree and Tabular Combined Notation (TTCN) standard test description language.  The referenced packet-mode Data-3 service SSND sublayer testing includes the following: 

 
Reference Document "D" Annex 1 Section 7: 
 
7.1  
Assumptions 
 
 
7.2  
Test Suite Structure 
 
 
7.2.1  
Proper Test Cases 
 
 
7.2.2  
Improper Test Cases 
 
 
7.2.3  
Inopportune Test Cases 
 
 
7.2.4  
Mandatory and Optional Tests 
 
 
7.2.5  
Test Case Reference Numbers 
 
(Required tests) 
 
7.3  
Test Suite Requirements 
 
 
7.3.1  
PM1 - State P1 Ready 
 
 
7.3.1.1 
(Information only) 
 
 
7.3.1.2 
PM1 Test Cases 
 
 
7.3.2  
PM2 - State P2 HLE Call Request 
 
 
7.3.2.1 
(Information only) 
 
 
7.3.2.2 
PM2 Test Cases 
 
 
7.3.3  
PM3 - State P3 Incoming Calls 
 
 
7.3.3.1 
(Information only) 
 
 
7.3.3.2 
PM3 Test Cases 
 
 
7.3.4  
PM4 - State P4 Data Transfer 
 
 
7.3.4.1 
(Information only) 
 
 
7.3.4.2 
PM4 Test Cases 
 
 
7.3.5  
PM5 - State P6 Local Clear Request 
 
 
7.3.5.1 
(Information only) 
 
 
7.3.5.2 
PM5 Test Cases 
 
 
7.3.6  
PM7 - State D1 (within P4) Flow Control 
 
 
7.3.6.1 
(Information only) 
 
 
7.3.6.2 
PM7 Test Cases 
 
 
7.3.7  
PM8 - State D2 (within P4) Local Reset 
 
 
7.3.7.1 
(Information only) 
 
 
7.3.7.2 
PM8 Test Cases 
 
 
7.3.8  
PM10 - State J1 (within D1) No Remote Interrupt Pending 
 
 
7.3.8.1 
(Information only) 
 
 
7.3.8.2 
PM10 Test Cases 
 
 
7.3.9  
PM11 - State J2 (within D1) Remote Interrupt on going 
 
 
7.3.9.1 
(Information only) 
 
 
7.3.9.2 
PM11 Test Cases 
 
 
7.3.10 
PM12 - State I1 (within D1) No Local Interrupt Pending 
 
 
7.3.10.1 
(Information only) 
 
 
7.3.10.2 
PM12 Test Cases 
 
 
7.3.11 
PM13 - State I2 (within D1) Local Interrupt on going 
 
 
7.3.11.1 
(Information only) 
 
 
7.3.11.2 
PM13 Test Cases 
 
 
7.3.12 
PM14 - State G1 (within D1) Flow control ready 
 
 
7.3.12.1 
(Information only) 
 
 
7.3.12.2 
PM14 Test Cases 
 
 
7.3.13 
PM15 - State G2 (within D1) Flow control not ready 
 
 
7.3.13.1 
(Information only) 
 
 
7.3.13.2 
PM15 Test Cases 
 
 
7.3.14 
PM16 - Data Transfer Function 
 
 
7.3.14.1 
(Information only) 
 
 
7.3.14.2 
PM16 Test Cases 
 
 
7.3.15 
PM17 - Timer Tests 
 
 
7.3.15.1 
(Information only) 
 
 
7.3.15.2 
PM17 Test Cases 
 
 
7.3.16 
PM18 - Address & Facility Field Tests 
 
 
7.3.16.1 
(Information only) 
 
 
7.3.16.2 
PM18 Test Cases 
 
 
7.3.17 
PM19 - Multiple Logical Channel Assignment 
 
 
7.3.17.1 
(Information only) 
 
 
7.3.17.2 
PM19 Test Cases 
 
 
7.3.18 
PM20 - SNPDU Construction Rules 
 
 
7.3.18.1 
(Information only) 
 
 
7.3.18.2 
PM20 Test Cases 
 
 
7.3.19 
PM21 - Primitive Parameter Construction Rules 
 
 
7.3.19.1 
(Information only) 
 
 
7.3.19.2 
PM21 Test Cases 
 
Reference Document "D" Annex 3 Section 4: 

 
4.3 
Connection Setup and Clearing 
 
4.3.1 
Ground-to-Air Connection Setup 
 
4.3.2 
Air-to-Ground Connection Setup 
 
4.3.3 
Ground-to-Air Connection Release 
 
4.3.4 
Air-to-Ground Connection Release 
 
4.3.5 
Multiple Connection Setup with a GES 
 
4.3.6 
Log-On Renewal 
 
4.3.7 
Log-Off 
 
4.4 
Data Transfer 
 
4.4.1 
Air-to-Ground Data Transfer Over a Single SVC 
 
4.4.2 
Air-to-Ground Data Transfer Over Multiple SVCs 
 
4.4.3 
Ground-to-Air Data Transfer Over a Single SVC 
 
4.4.4 
Ground-to-Air Data Transfer Over Multiple SVCs 
 
 
4.4.5  
Bi-directional Data Transfer 

## 2.4.7.3 Packet-Mode Data-3 Service Iso 8208 Test Requirements (Section 2.2.7)

 
This section defines a succession of test procedures for a comprehensive logical state test for ISO 8208 DCE.  For all test procedures, the transceiver under test does not include the antennas.  Use the Test Set to perform the HLE functions and the GES Emulator to perform the GES functions.  For all test procedures, the transceiver is logged on to the GES Emulator.  The transceiver and the Test Set exchange ISO 8208 Packets, while the transceiver and the GES Emulator exchange SNPDUs. 

 
The Use of ISO 8208 Default Parameters 
Unless otherwise specified, this procedure assumes that relevant parameters of the DTE/DCE interface are set to their standard default values as defined in ISO 8208. 
 
 
NOTE: 
These include, for example, packet sizes, flow control window sizes, timers and 
retry counters. 

## Maintaining Flow Control

 
Unless otherwise specified, the tester shall ensure that flow control is maintained across the transceiver/HLE interface through the use of RECEIVE READY Packets, or DATA Packets with updated PR/PS Subfields. 

 
Network Conditions 
 
Unless otherwise specified, the following test procedures assume that only one DTE will be connected to the transceiver during a given test.  Failure to observe this precaution may cause test results to differ from the expected values. 

 
Standard Test Signals 
The network protocol selected for the transceiver/HLE interface is ISO Standard 8208. 
 
 
NOTE: 
The manufacturer is free to choose the appropriate physical data bus for connection between the transceiver and the HLE.  Characteristics such as amplitude, timing, and waveform shapes of test signals applied to the transceiver shall be consistent with the standards definition of the selected data bus.  Moreover, the manufacturer should adhere to system impedance requirements of the appropriate standards whether the equipment under test has 
power applied or not, or is in an active or quiescent state (i.e., standby). 
General Characteristics - Transceiver/HLE Test Signals 
 
a. 
Data Formats:  Data transmitted across this interface shall be in Packets conforming to ISO Standard 8208. 
 
b. 
Electrical Characteristics:  Test signals on this interface shall be consistent with the appropriate standards for the connecting data bus. 
 
c. 
ISO 8208 Channel Assignments:   The test procedures in this MOPS use 12 ISO 8208 channels in the range 2805 through 2816.  This assignment of channels is introduced as a documentation aid.  The manufacturer is free to choose any block of 12 ISO 8208 channels in the range 2565 through 2816, in a particular transceiver implementation. 
 
d. 
Data Content:  The test equipment shall be capable of generating or accepting messages with the following content:  Packet fields such as sequence numbers, addresses, packet types or any other control fields shall be capable of being loaded with all ones or zeros or any combinations thereof.  Data fields within the packets shall also be capable of being loaded with all ones or zeros or any combination thereof as specified in the test procedures. 

## Message Validation

 
The test equipment shall provide a means of validating the information content of any message received from the transceiver.  This requirement applies to either the transceiver/GES interface or the transceiver/HLE interface. 

## 2.4.7.3.1 Channel State Test Procedures

 
The channel state test procedures are designed to test the restart, call setup and clearing, reset, interrupt, flow control and data transfer state tables of the transceiver.  The tests are divided into two subgroups: the Normal State Test Procedures and the Error Recovery State Test Procedures. 

 
Unless otherwise indicated, the tests all occur on one logical channel. 

## 2.4.7.3.1.1 Normal State Test Procedures

 
(Section - 2.2.7.5.2.3 - AES DCE Operation) 
 
(Section - 2.2.7.5.2.3.1 - State Transitions) 
 
These procedures are designed to test the transceiver actions when receiving the logically correct ISO 8208 Packets and SSND SNPDUs for the state of the logical channel.  A series of packets and SNPDUs will be transferred across the transceiver interfaces to stimulate the logical states. 

## Call Setup And Clearing States

 
Step 1 - Virtual Call Setup from HLE 
 
Program the test set to send an CALL REQUEST Packet to the transceiver.  The use of NSAP addressing is optional.  Invoke the Expedited Data Negotiation Facility in the Optional CCITT-specified DTE Facilities Field.  Use the GES Emulator to return a CONNECTION CONFIRM SNPDU for the corresponding channel.  Verify that the transceiver generates the corresponding CALL CONNECTED Packet with the correct fields. 
Step 2 - Data Transmission 
 
Program the test set to send two DATA Packets to the transceiver on the open channel.  Each DATA Packet has the M-bit set to zero.  Maintain flow control for the channel, i.e. the PS Subfields for the first and second packet should be zero and one, respectively.  Use a 32-bit User Data Field, and fill the Fields with alternate one-zero patterns. 
 
Verify that the transceiver transmits one DATA SNPDU to the GES for each DATA Packet.  After both DATA Packets are accepted by the transceiver, verify that the transceiver sends a RECEIVE READY Packet to the Test Set. 
 
Step 3 - Clear Request Procedures from HLE 
 
Program the test set to send a CLEAR REQUEST Packet on the open channel to the 
transceiver.  Verify that the transceiver returns a CLEAR CONFIRMATION Packet to the HLE and sends a corresponding CONNECTION RELEASED SNPDU to the GES Emulator.  Use the GES Emulator to return a CONNECTION RELEASE COMPLETE SNPDU.  Verify that there is no output on the transceiver/HLE interface. 
Step 4 - Virtual Call Setup from GES Emulator 
 
This test is covered by test case PM1_101 as conducted in Section 2.4.7.2. 
Step 5 - Data Transfer from the GES Emulator 
 
This test is covered by test case PM7_101 as conducted in Section 2.4.7.2. 
Step 6 - GES Requests to Clear the Channel 
 
This test is covered by test case PM4_101 as conducted in Section 2.4.7.2. 
Step 7 - HLE Aborts a Call Request 
 
 
Program the test set to send a CALL REQUEST Packet to the transceiver.  Use the GES Emulator to verify that the CONNECTION REQUEST SNPDU is sent from the transceiver.  Have the test set send a CLEAR REQUEST Packet for that channel to the transceiver.  Use the test set to verify that the transceiver returns a CLEAR CONFIRMATION Packet to the HLE.  Use the GES Emulator to verify the Clearing and Diagnostic Cause Fields in the corresponding CONNECTION RELEASED SNPDU and to return a CONNECTION RELEASE COMPLETE SNPDU.  Verify that there is no corresponding output at the transceiver/HLE interface. 

 
Step 8 - GES Aborts a Call Request 
 
This test is covered by test case PM3_101 as conducted in Section 2.4.7.2. 
Step 9 - GES rejects a Call Request 
 
This test is covered by test case PM2_101 as conducted in Section 2.4.7.2. 
Step 10 - HLE Rejects a Call Request 
 
Program the GES Emulator to send a CONNECTION REQUEST SNPDU.  Use the test set to verify that a CALL REQUEST Packet is produced by the transceiver, and to return a CLEAR REQUEST Packet to transceiver.  Verify that the transceiver returns a CLEAR CONFIRMATION Packet to the HLE.  Use the GES Emulator to verify that the CONNECTION RELEASED SNPDU is received from the transceiver, 
and to send a CONNECTION RELEASE COMPLETE SNPDU to the transceiver. Verify that there is no corresponding output at the transceiver/HLE interface. 

 
 
Step 11 - CLEAR REQUEST Packet for a Channel in the Ready State (p1) 
 
Program the test set to send a CLEAR REQUEST Packet to the transceiver.  Verify that the transceiver returns a CLEAR CONFIRMATION Packet. 
Step 12 - Call Collision 
 
Program the GES Emulator to send a CONNECTION REQUEST SNPDU to the transceiver.  Verify that the transceiver forwards an INCOMING CALL Packet to the HLE.  Program the Test Set to return a CALL REQUEST Packet to the transceiver with the same channel number.  Verify that the transceiver returns a CONNECTION RELEASED SNPDU and forwards a CONNECTION REQUEST SNPDU to the GES Emulator. 
Step 13 - Clear Channels 
 
Perform the procedures in Step 3, to clear the channels used in Step 12. 
Restart Request States 
Step 1 - DTE Restart Procedures 
 
Perform the procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1 to open two channels.  Program the test set to send a RESTART REQUEST Packet to the transceiver.  Verify the RESTART CONFIRMATION Packet is returned from the transceiver to the HLE.  Use the GES Emulator to verify that the transceiver sends a CONNECTION RELEASED SNPDU to the GES for each channel not in the p1 State.  Program the GES Emulator to send the corresponding CONNECTION RELEASE COMPLETE SNPDUs to the transceiver.  Verify that there is no corresponding output at the transceiver/HLE interface. 
Step 2 - DCE Restart Procedures 
 
Program the test set to send a RESTART CONFIRMATION Packet to the transceiver.  Use the test set to verify that the transceiver will return a RESTART INDICATION Packet to the HLE with diagnostic code set to 17.  Program the test set to return a RESTART CONFIRMATION Packet to the transceiver.  Verify that there is no corresponding output at the transceiver interfaces. 
Reset States 
Step 1 - Reset Procedures by HLE 
 
Perform virtual call setup and data transactions procedures in Section 2.4.7.3.1.1 Call Setup and Clearing States Steps 1 and 2.  Program the test set to send a RESET 
REQUEST Packet on the open channel to the transceiver.  Verify that the transceiver returns a RESET CONFIRMATION Packet to the HLE.  Use the GES Emulator to verify that the RESET SNPDU sent from the transceiver contains the appropriate Resetting and Diagnostic Cause Fields.  Program the GES Emulator to send RESET CONFIRM SNPDU.  Verify that there is no corresponding output at the transceiver/HLE interface. 

 
Step 2 - Reset Procedures by HLE.  GES Responds with a RESET SNPDU 
 
Program the test set to send a RESET REQUEST Packet on the open channel to the transceiver.  Use the test set to verify that the transceiver returns a RESET CONFIRMATION Packet to the HLE.  Use the GES Emulator to verify that the transceiver transmits a RESET SNPDU with the appropriate Resetting and Diagnostic Cause Fields.  Program the GES Emulator to send a RESET SNPDU.  Verify that there is no corresponding output on the transceiver/HLE interface. 
Step 3 - Reset Procedure from GES. 
 
This test is covered by test case PM7_102 as conducted in Section 2.4.7.2. 
Step 4 - Reset Request from GES.  HLE responds with a RESET REQUEST Packet. 
 
Program the GES Emulator to send a RESET SNPDU on the open channel to the transceiver.  Verify that the transceiver returns a RESET CONFIRM SNPDU to the GES Emulator and transmits the corresponding RESET INDICATION Packet with the appropriate Diagnostic and Resetting Fields to the HLE.  Use the test set to return a RESET REQUEST Packet to the transceiver.  Use the GES Emulator to verify that there is no corresponding output at the transceiver/GES interface. 
Step 5 - Clear Opened Channel 
 
Perform the clear request procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3. 
Flow Control Transfer States 
Step 1 - Receive Not Ready Procedure 
 
This test is covered by test case PM7_103 as conducted in Section 2.4.7.2. 
Step 2 - Receive Ready Procedure 
 
This test is covered by test case PM7_104 as conducted in Section 2.4.7.2. 
Step 3 - Reject Procedures 
 
This test is covered by test case PM14_301 as conducted in Section 2.4.7.2. 
 

## Interrupt Transfer States Step 1 - Virtual Call Setup

 
 
Perform the call setup procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1. 
Step 2 - Interrupt Packet from the HLE 
 
Program the test set to send a DATA Packet to the transceiver.  Set M-bit to one. User Data Field contains 128 bytes, the value of each byte increments from 0 to 127. Program the test set to send an INTERRUPT Packet with a 32-bit User Data Field containing a bit pattern of alternating one's and zero's, and another DATA Packet with M-bit set to zero.  Use the GES Emulator to verify that the corresponding INTERRUPT DATA SNPDU is not the last SNPDU sent from the transceiver.  Also, verify content and length of the User Data Fields.  Use the GES Emulator to send a INTERRUPT CONFIRM SNPDU.  Verify the INTERRUPT CONFIRMATION Packet. 
Step 3 - Interrupt Packet from the GES. 
 
Program the GES emulator to transmit the following SNPDUs to the transceiver: a DATA SNPDU with M-bit set to one and 503 bytes of User Data, an INTERRUPT DATA SNPDU with 32 bytes of User Data, and a second DATA SNPDU that has the M-bit set to zero.  Use the Test Set to verify that the transceiver forwards the corresponding ISO 8208 INTERRUPT Packet followed by the ISO 8208 M-bit sequence.  Program the test set to return an INTERRUPT CONFIRMATION Packet to the transceiver.  Verify the corresponding INTERRUPT CONFIRMATION SNPDU. 
Step 4 - Clear Opened Channel 
 
Perform the procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3 to clear the open channel. 

## 2.4.7.3.1.2 Error Recovery Procedures

 
The Error Recovery State Test Procedures are designed to test the capability of the transceiver to recover from erroneous packets received over the transceiver/HLE or transceiver/GES interface.  A series of ISO 8208 Packets and SSND SNPDUs will be transferred across the transceiver boundaries to stimulate the logical states.  Unless otherwise noted, all tests occur on a single logical channel. 

## Dce Call Setup And Clearing States

 
Step 1 - Ready State (p1) 
 
This test verifies the DCE p1 State. 
 
 
a. 
Program the test set to send a CALL ACCEPTED Packet to the transceiver. Verify that the transceiver returns to the HLE a CLEAR INDICATION Packet 
with diagnostic code set to 20.  Program the test set to return a CLEAR CONFIRMATION Packet to the transceiver.  Verify there is no corresponding output on the transceiver/GES interface. 
 
b. 
Perform the procedure in Step 1a replacing the CALL ACCEPTED Packet sent to the transceiver with each of the following Packets: RESET REQUEST, CLEAR CONFIRMATION, RESET CONFIRMATION, DATA, INTERRUPT, RECEIVE READY and RECEIVE NOT READY.  Verify the results as in Step 1a. 
 
c. 
Program the test set to send a RESTART REQUEST Packet to the transceiver with channel number not equal to zero.  Verify that the transceiver sends a CLEAR INDICATION Packet to the HLE with diagnostic code set to 41. Program the Test Set to return a CLEAR CONFIRMATION Packet to the transceiver.  Verify that there is no corresponding output on the transceiver/GES interface. 
 
d. 
Perform the procedure in Step 1a, replacing the CALL ACCEPTED Packet sent to the transceiver with an ISO 8208 Packet having a packet type identifier shorter than one byte.  Verify that the diagnostic code is set to 38 in the CLEAR INDICATION Packet. 


e. 
Perform the procedure in Step 1a, replacing the CALL ACCEPTED Packet sent to the transceiver with an ISO 8208 Packet having a packet type identifier which is undefined or not supported.  Verify that the transceiver returns a CLEAR INDICATION Packet with diagnostic code set to 33. 

## Step 2 - Dte Call Request State (P2)

 
 
This test verifies the DCE p2 State. 
 
a. 
Program the test set to send a CALL REQUEST Packet to the transceiver.  Use the GES Emulator to verify that the transceiver sends a CONNECTION REQUEST SNPDU to the GES Emulator. 
 
b. 
Program the test set to send a RESET REQUEST Packet on the same channel to the transceiver.  Verify that the transceiver generates a CLEAR INDICATION Packet and a CONNECTION RELEASED SNPDU with diagnostic codes set to 21.  Program the test set to return a CLEAR CONFIRMATION Packet and the GES Emulator to return a CONNECTION RELEASE COMPLETE SNPDU to the transceiver. 
 
c. 
Perform the procedures in Steps 2a and 2b, replacing the RESET REQUEST Packet sent to the transceiver in procedure 2b with each of the following ISO 8208 
Packets: 
CALL 
REQUEST, 
CALL 
ACCEPTED, 
CLEAR 
CONFIRMATION, DATA, INTERRUPT, RECEIVE READY and RECEIVE NOT READY.  Verify the results as in Step 2b. 



d. 
Perform the procedures in Steps 2a and 2b, replacing the RESET REQUEST Packet sent to the transceiver in procedure 2b with an ISO 8208 Packet having a packet type identifier shorter than one byte.  Verify that the diagnostic code is set to 38 in the CLEAR INDICATION Packets. 
 
e. 
Perform the procedures Steps 2a and 2b, replacing the RESET REQUEST Packet sent to the transceiver in procedure 2b with an ISO 8208 Packet having a packet type identifier which is undefined or not supported.  Verify that the diagnostic code is set to 33 in the CLEAR INDICATION Packets. 
 
f. 
Perform the procedures in Steps 2a and 2b, replacing the RESET REQUEST Packet sent to the transceiver in procedure 2b with an RESTART REQUEST Packet or a RESTART CONFIRMATION Packet with a logical channel number not equal to zero.  Verify that the diagnostic code is set to 41 in the CLEAR INDICATION Packets. 

## Step 3 - Dce Call Request State (P3)

 
 
This test verifies the DCE p3 State. 
 
a. 
Program the GES Emulator to send CONNECTION REQUEST SNPDU to the transceiver.  Verify the INCOMING CALL Packet. 
 
b. 
Program the test set to send a RESET REQUEST Packet on the same channel to the transceiver.  Verify that the transceiver will send a CLEAR INDICATION Packet to the HLE and a CONNECTION RELEASED SNPDU to the GES Emulator with diagnostic codes set to 22.  Program the test set to send a CLEAR CONFIRMATION Packet to the transceiver, and program the GES Emulator to send a CONNECTION RELEASE COMPLETE SNPDU to the transceiver. Verify that there is no corresponding output at the transceiver/HLE and transceiver/GES interfaces. 
 
c. 
Perform the procedures in Steps 3a and 3b five times.  For each iteration replace the RESET REQUEST Packet sent to the transceiver in Step 3b with one of the following Packets: CLEAR CONFIRMATION, DATA, RECEIVE READY, RECEIVE NOT READY and INTERRUPT.  Verify the results as in Step 3b. 
 
d. 
Perform the procedures in Steps 3a and 3b, replacing the RESET REQUEST Packet sent to the transceiver in Step 3b with an ISO 8208 Packet having a Packet Type Identifier shorter than one byte.  Verify that the diagnostic code is set to 38. 
 
e. 
Perform the procedures in Steps 3a and 3b, replacing the RESET REQUEST Packet sent to the transceiver in Step 3b with an ISO 8208 Packet having a 
Packet Type Identifier which is undefined or not supported.  Verify that the diagnostic code is set to 33. 



f. 
Perform the procedures in Steps 3a and 3b, replacing the RESET REQUEST Packet sent to the transceiver in Step 3b with a RESTART REQUEST Packet with the logical channel identifier not equal to zero.  Verify that the diagnostic code is set to 41. 
Step  4 - Data Transfer State (p4) 
 
This test verifies the DCE p4 State. 
 
a. 
Perform call setup procedure, Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1. 
 
b. 
Program the test set to send a CALL REQUEST Packet on the open channel to the transceiver.  Verify that the transceiver sends a CLEAR INDICATION Packet and a CONNECTION RELEASED SNPDU with diagnostic codes set to 23.  Bit eight of the Clearing Cause Field should be set to zero because the error originated at the DTE/DCE interface.  Program the test set to return a CLEAR CONFIRMATION Packet, and program the GES Emulator to send a CONNECTION RELEASE COMPLETE SNPDU to the transceiver.  Verify that neither confirmation appears in the other interface. 
 
c. 
Perform the procedures in Steps 4a and Step 4b two times.  For the first iteration replace the CALL REQUEST Packet sent to the transceiver with a CALL ACCEPTED Packet.  For the second iteration, replace the CALL REQUEST Packet sent to the transceiver with a CLEAR CONFIRMATION Packet.  Verify the results as in Step 4b. 
Step 5 - Call Collision State (p5) 
 
The error recovery procedure for the Call Collision (p5) State is transitory and therefore is not tested. 
Step 6 - Clear Request by DTE State (p6) 
 
The error recovery procedure for the Clear Request by DTE (p6) State is transitory and therefore is not tested. 
Step 7 - DCE Clear to DTE State (p7) 
 
This test verifies the DCE p7 State. 


a. 
Perform the call setup procedure in Step 2a. 
 
b. 
Program the test set to send a RESET REQUEST Packet on the same channel to the transceiver.  Verify that the transceiver generates a CLEAR INDICATION 
Packet and a CONNECTION RELEASED SNPDU with diagnostic codes set to 21. 



c. 
Program the test set to send a CALL ACCEPTED Packet to the transceiver. Verify that the packet is discarded. 
 
d. 
Perform the procedure in Step 7c five times.  For each iteration, replace the CALL ACCEPTED Packet sent to the transceiver with one of the following Packets:  DATA, INTERRUPT, RECEIVE READY, RECEIVE NOT READY and RESET REQUEST.  Verify that the packets are discarded. 
 
e. 
Perform the procedure in Step 7c, replacing the CALL ACCEPTED Packet sent to the transceiver with an ISO 8208 Packet having a Packet Type Identifier which is undefined or not supported. 
 
f. 
Perform the procedure in Step 7c, replacing the CALL ACCEPTED Packet sent to the transceiver with an ISO 8208 Packet having a Packet Type Identifier shorter than one byte. 
 
g. 
Program the Test Set to send a CLEAR CONFIRMATION Packet to the transceiver.  Program the GES Emulator to return a CONNECTION RELEASE COMPLETE SNPDU to the transceiver.  Verify that there is no corresponding output at that transceiver interfaces. 

## Dce Restart States

 
Step 1 - Packet Level Ready State (r1) 
 
This test verifies the DCE r1 State. 
 
a.  
Program the test set to send a CALL REQUEST Packet to the transceiver with a channel number equal to zero.  Verify that the transceiver sends a DIAGNOSTIC Packet to the HLE with diagnostic code set to 36, and that the Diagnostic Cause Field contains the first three bytes of the CALL REQUEST Packet. 
 
b. 
Program the test set to send a RESTART REQUEST Packet with a format error to the transceiver.  Verify that the transceiver returns a DIAGNOSTIC Packet to the HLE with diagnostic code set to either 38, 39, 81 or 82, and the Diagnostic Cause Field contains the first three bytes of the RESTART REQUEST Packet. 
 
c. 
Program the test set to send a RESTART CONFIRMATION Packet to the transceiver.  Verify that the transceiver returns a RESTART INDICATION Packet to the HLE with diagnostic code set to 17. 
 
d. 
Program the test set to send a RESTART CONFIRMATION Packet to the transceiver.  The transceiver enters the r1 State. 
 

## Step 2 - Dte Restart Request State (R2)

 
 
The DTE Restart Request State (r2) error recovery procedure is transitory and 
therefore is not tested. 
Step 3 - DCE Restart Request State (r3) 
 
This test verifies the DCE r3 State. 
 
a. 
Perform again the procedure in Step 1d.  The transceiver enters the r3 State. 
 
b. 
Perform the procedure in Step 1a. 
 
c. 
Program the test set to send a RESTART REQUEST Packet with format error to the transceiver.  Verify that the transceiver returns a RESTART INDICATION Packet to the HLE with diagnostic code set to either 38, 39, 81, or 82. 
 
d. 
Perform the procedure in Step 1d. 
Step 4 - DCE Special Cases 
 
a. 
Program the test set to send an ISO 8208 Packet to the transceiver that is less than two bytes in length.  Verify that the transceiver returns a DIAGNOSTIC Packet to the HLE with the Diagnostic Code Field set to 38.  Also, verify the Diagnostic Cause Field. 
 
b. 
Program the test set to send a CALL REQUEST Packet to the transceiver with a invalid General Format Identifier Field.  Verify the transceiver returns a DIAGNOSTIC Packet to the HLE with the Diagnostic Code Field set to 40. Also, verify the Diagnostic Cause Field. 
DCE Reset States 
Step 1 - Erroneous ISO 8208 Packets for the Flow Control Ready State (d1) 
 
This test verifies the DCE d1 State. 
 
a. 
Perform the call setup procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1. 
 
b. 
Program the test set to send a RESTART REQUEST Packet to the transceiver with a logical channel identifier unequal to zero on the open channel.  Verify that the transceiver sends a RESET INDICATION Packet to the HLE and a RESET SNPDU to the GES Emulator with diagnostic codes set to 41. 
 
c. 
Program the test set to send a RESET CONFIRMATION Packet and the GES Emulator to send a RESET CONFIRM SNPDU to the transceiver. 


d. 
Perform the procedures in Steps 1b and 1c.  For this iteration, replace the RESTART REQUEST Packet the transceiver in Step 1b with a packet having an invalid Packet Type Identifier shorter than one byte.  Verify that the diagnostic 
codes are set to 38 in the corresponding RESET INDICATION Packet and RESET SNPDU. 
 
e. 
Perform the procedures in Steps 1b and Step 1c.  For this iteration, replace the RESTART REQUEST Packet with a packet having a Packet Type Identifier which is undefined.  Verify that the diagnostic codes are set to 33 in the corresponding RESET INDICATION Packet and RESET SNPDU. 
 
f. 
Perform the Clear Request procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3. 

## Step 2 - Reset Request By Dte (D2)

 
 
The DTE Reset Request (d2) State error recovery procedure is transitory and therefore is not tested. 

## Step 3 - Reset Request By Dce To Dte (D3)

 
 
This test verifies the DCE d3 State. 
 
a. 
Perform the call setup procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1. 
 
b. 
Program the test set to send a RESET CONFIRMATION Packet on the opened channel to the transceiver.  Verify that the transceiver sends a RESET INDICATION Packet to the HLE and a RESET SNPDU to the GES Emulator with diagnostic codes set to 27. 
 
c. 
Program the test set to return an INTERRUPT Packet to the transceiver.  Verify that there is no corresponding output. 
 
d. 
Perform the procedure in Step 3c, replacing the INTERRUPT Packet sent to the transceiver in Step 3c with each of the following ISO 8208 Packets: INTERRUPT CONFIRMATION, RESTART REQUEST with channel number unequal to zero, DATA, RECEIVE READY, RECEIVE NOT READY, REJECT, a packet having a Packet Type Identifier shorter than one byte, and a packet having a Packet Type Identifier which is undefined.  Program the test set to send a RESET CONFIRMATION Packet and the GES Emulator to send a RESET CONFIRM SNPDU to the transceiver.  Verify the results as in 3c. 
 
e. 
Perform the clear request procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3. 
 

## Dce Flow Control Transfer States Step 1 - Dce Receive Ready State (F1)

 
 
This test verifies the DCE f1 State. 
 
a. 
Perform the call setup procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1. 
 
b. 
Program the test set to send a DATA Packet that contains an invalid PS Field. Verify that the transceiver sends a RESET INDICATION Packet to the HLE and a RESET SNPDU to the GES Emulator with diagnostic codes set to one. Program the test set to return a RESET CONFIRMATION Packet to the transceiver and the GES Emulator to return a RESET CONFIRM SNPDU. 
 
c. 
Program the test set to send a DATA Packet to the transceiver that contains an invalid PR.  Verify that the transceiver sends a RESET INDICATION Packet to the HLE and a RESET SNPDU to the GES Emulator, with diagnostic codes set to two. 
 
d. 
Perform the reset confirmation procedure in Step 1b. 
 
e. 
Perform the procedures in Steps 1c and 1d.  Replace the DATA Packet sent to the transceiver in Step 1c with a DATA Packet that has M-bit set to one and a partially full User Data Field.  Verify that the diagnostic codes are equal to 165 or 166. 
 
f. 
Perform the clear request procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3. 

## Step 2 - Dce Receive Not Ready (F2)

 
 
This test verifies the DCE f2 State. 
 
a. 
Perform the call setup procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1. 
 
b. 
Program the GES Emulator to send a FLOW CONTROL (Suspend) SNPDU. 
 
c. 
Program the test set to send DATA Packets to the transceiver until the transceiver returns a RECEIVE NOT READY Packet to the HLE. 
 
d. 
Verify that the transceiver will discard the following ISO 8208 Packets sent from the Test Set: DATA Packet with a valid PR but an invalid PS, a valid DATA Packet and a DATA Packet that has M-bit set to one and a partially full User Data Field. 
 
e. 
Perform the procedure in Step 1c.  Verify the results. 
 
 
f. 
Perform the reset confirmation procedure in Step 1b. 


g. 
Perform the clear request procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3. 

## Step 3 - Dte Receive Ready (G1)

 
 
This test verifies the DTE g1 State. 
 
a. 
Perform the call setup procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1. 
 
b. 
Program the test set to send a RECEIVE READY Packet with a invalid PR Field to the transceiver.  Verify that the transceiver sends a RESET INDICATION Packet to the HLE and a RESET SNPDU to the GES Emulator with diagnostic codes set to two. 
 
c. 
Perform the reset confirmation procedure in Step 1b. 
 
d. 
Perform the procedures in Steps 3b and Step 3c two times.  For the first iteration, replace the RECEIVE READY Packet sent to the transceiver in Step 3b with a RECEIVE NOT READY Packet.  For the second iteration, replace the RECEIVE READY Packet sent to the transceiver in Step 3b with a REJECT Packet.  Verify the results as in 3b. 
 
e. 
Perform the Clear Request procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3. 

## Step 4 - Dte Receive Not Ready (G2)

 
 
This test verifies the DTE g2 State. 
 
a. 
Perform the call setup procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1. 
 
b. 
Program the test set to send a RECEIVE NOT READY Packet to the transceiver. 
 
c. 
Perform the procedures in Steps 3b, 3c, 4b, and 3d. 
 
d. 
Perform the clear request procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3. 
 

## Dce Interrupt Transfer States Step 1 - Dte Interrupt Sent State (I2)

 
 
This test verifies the DCE i2 State. 
 
a.  
Perform the call setup procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1. 
 
b. 
Program the test set to send an INTERRUPT Packet to the transceiver.  Use the GES Emulator to verify that the transceiver sends a INTERRUPT DATA SNPDU to the GES Emulator.  Program the test set to send another INTERRUPT Packet on the same channel to the transceiver. 
 
c. 
Verify that the transceiver sends a RESET SNPDU to the GES Emulator and a RESET INDICATION Packet to the HLE with diagnostic codes set to 44. 
 
d. 
Perform the reset confirmation procedure in Section 2.4.7.3.1.1 Step 1b. 
 
e. 
Perform the procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3 to clear an open channel. 

## Step 2 - Dce Interrupt Ready State (J1)

 
 
This test verifies the DCE j1 State. 
 
a. 
Perform the procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1 to open a channel. 
 
b. 
Program the test set to send an INTERRUPT CONFIRMATION Packet to the transceiver. 
 
c. 
Verify that the transceiver sends a RESET SNPDU to the GES Emulator and a RESET INDICATION Packet to the HLE with diagnostic codes set to 43. 
 
d. 
Perform the reset confirmation procedure in Section 2.4.7.3.1.1 Step 1b. 
 
e. 
Perform the procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3 to clear a channel. 

## 2.4.7.3.2 Multiple Channel Packet Assembly And Disassembly

 
These test procedures are designed to test the transceiver's ability to assemble and disassemble ISO 8208 Packets and SSND SNPDUs.  The tests are divided into two subgroups, M-bit Linking and Multiple Call Clearing. 
 

## 2.4.7.3.2.1 M-Bit Linking

 
The M-bit linking test procedures are designed to verify the transceiver's ability to assemble User Data Fields in 8208 DATA packets into larger SNS-User Data Fields in SSND DATA SNPDUs, and also to disassemble SNS-User Data Fields in SSND DATA SNPDUs into smaller User Data Fields in 8208 DATA packets, using multiple logical channels. 

 
Use the test set to perform the HLE functions, and use the GES Emulator and GES Emulator to perform the GES functions. 

## Step 1 - Virtual Call Setup

 
 
This test opens multiple channels with the transceiver. 
 
a.  
Program the test set to send four CALL REQUEST Packets to the transceiver with the following channel numbers: 2816, 2815, 2814, and 2813.  Use the GES Emulator to verify that the transceiver sends CONNECTION REQUEST SNPDUs with the following channel numbers: 255, 254, 253, and 252. 
 
b. 
Program the GES Emulator to send four CONNECTION CONFIRM SNPDUs to the transceiver.  Verify that the transceiver sends four CALL CONNECTED Packets to the HLE with the following channel numbers: 2816, 2815, 2814, and 2813. 

## Step 2 - M-Bit Linking Data Snpdus From Data Packets

 
 
This test verifies ISO 8208 M-bit sequence to DATA SNPDU assembly procedure in the transceiver. 
 
a.  
Program the test set to send an ISO 8208 M-bit sequence consisting of four DATA Packets each with 128 bytes of data in the User Data field on each opened channel to the transceiver.  Fill the User Data Field with following patterns: 


channel 2816    01010101 


channel 2815    10101010 


channel 2814    11001100 


channel 2813    00110011 
 
b. 
Use the GES Emulator to verify that the transceiver sends a sequence of two DATA SNPDUs to the GES Emulator for each channel.  Verify that each of the first DATA SNPDUs contain 503 bytes of the SNS-User Data Field and has M- bit set to one.  Verify that the second SNPDU for each channel contains nine bytes of the SNS-User Data Field and has M-bit set to zero.  Also verify that the SNS-User Data Field content corresponds with the following SSND channels: 


channel 255    01010101 


channel 254    10101010 


channel 253    11001100 


channel 252    00110011. 
 
 
Step 3 - DATA SNPDUs from the GES 
 
 
This test verifies ISO 8208 Packet assembly procedures in the transceiver. 

 
 
a. 
Program the GES Emulator to send a sequence of two DATA SNPDUs to the transceiver for each opened channel.  The first DATA SNPDU for each channel should have the M-bit set to one.  All DATA SNPDUs in each sequence should contain 503 bytes of the SNS-User Data Field listed below. 


channel 255    01010101 


channel 254    10101010 


channel 253    11001100 


channel 252    00110011 
 
b. 
Verify that the transceiver sends eight DATA Packets on each opened channel to the HLE.  Also verify that the first seven DATA Packets for each channel have the M-bit set to one and contain 128 bytes of User Data Field listed below, and the eighth packet for each channel shall have M-bit set to zero and 110 bytes of user data. 


channel 2816    01010101 


channel 2815    10101010 


channel 2814    11001100 


channel 2813    00110011 

## 2.4.7.3.2.2 Multiple Call Clearing

 
This test verifies the transceiver's ability to clear the multiple channels that were left opened in Section 2.4.7.3.2.1. 

 
 
a. 
Program the test set to send four CLEAR REQUEST Packets to the transceiver on channels 2816, 2815, 2814, and 2813.  Use the GES Emulator to verify that the transceiver sends four CONNECTION RELEASED SNPDUs to the GES Emulator.  Use the test set to verify that the transceiver returns a CLEAR CONFIRMATION Packet to the HLE on each channel (2816, 2815, 2814, and 2813). 
 
b. 
Program the GES Emulator to return four corresponding CONNECTION RELEASE COMPLETE SNPDUs on channels 255, 254, 253, and 252 to the transceiver. 

## 2.4.7.3.3 Call Setup And Maintenance

 
The Call Setup and Maintenance test procedures are designed to test the transceiver's ability to process various requests for Virtual Call Setup.  The tests are divided into five subgroups: Fast Select, Called and Calling Address (NSAP) Extension, Throughput Class Negotiation, Transit Delay Selection and Indication, and Priority. 

## 2.4.7.3.3.1 Fast Select Facilities

 
The Fast Select test procedures are designed to test the transceiver's ability to process and reformat the Fast Select Facility request. 

## Step 1 - Call Request Packet With Fast Select From The Hle

 
 
This test verifies the transceiver's ability to process a Fast Select request. 
 
a. 
Program the test set to send a CALL REQUEST Packet to the transceiver with the Facilities Field containing a Fast Select request with no restriction on response.  Fill the User Data Field with 128 bytes of the bit pattern 01010101. 


b. 
Use the GES Emulator to verify that the transceiver transmits CONNECTION REQUEST SNPDU to the GES without the Fast Select (use not permitted) in the Facilities Field.  Verify the User Data Field for content and length. 
 
c. 
Program the GES Emulator to send a CONNECTION CONFIRM SNPDU to the transceiver.  Fill the User Data Field with 128 bytes of the bit pattern 10101010.  Verify that the transceiver sends the related CALL CONNECTED Packet to the HLE with the correct User Data Field. 
 
d. 
Program the test set to send a DATA Packet to the transceiver with a User Data Field of four bytes.  Verify that the transceiver sends a DATA SNPDU to the GES Emulator. 

## Step 2 - Connection Request Snpdu With Fast Select From The Ges

 
 
This test verifies the transceiver's ability to process a Fast Select request from the GES Emulator. 


a. 
Program the GES Emulator to send a CONNECTION REQUEST SNPDU to the transceiver without the Fast Select (use not permitted) in the Facilities Field. Fill the User Data Field with a line count from 0 to 127.  Use the Test Set to verify the User Data Field for content, order and length in the corresponding INCOMING CALL Packet. 
 
b. 
Program the test set to return a CALL ACCEPTED Packet to the transceiver. Fill the User Data Field with 128 bytes whose value starts at 127 and decrements to zero. 
 
c. 
Use the GES Emulator to verify that the transceiver transmits a CONNECTION CONFIRM SNPDU to the GES.  Also verify that the User Data Field is correct in content and order. 


d. 
Program the GES Emulator to send a DATA SNPDU containing 56 bits of User Data to the transceiver.  Verify that the transceiver sends the corresponding DATA Packet to the Test Set. 

## Step 3 - Clear Request Packet From The Hle

 
 
This test verifies the transceiver's ability to process a CLEAR REQUEST Packet with Fast Select requested. 
 
a. 
Program the test set to send a CLEAR REQUEST Packet to the transceiver on one of the two open channels.  Fill the User Data Field with 128 bytes of the bit pattern 01010101. 
 
b. 
Use the GES Emulator to verify the following:  transceiver transmits a CONNECTION RELEASED SNPDU to the GES and that the User Data Field contains 128 bytes of the bit pattern 01010101.  Verify that the transceiver returns a CLEAR CONFIRMATION Packet to the HLE.  Program the GES Emulator to return a CONNECTION RELEASE COMPLETE SNPDU to the transceiver. 

## Step 4 - Connection Released Snpdu With Fast Select From Ges

 
 
This test verifies the transceiver's ability to process a CONNECTION RELEASED SNPDU with Fast Select requested. 
 
a. 
Program the GES Emulator to send a CONNECTION RELEASED SNPDU to the transceiver on the open channel.  Fill the User Data with 128 bytes of the bit pattern 10101010. 
 
b. 
Use the GES Emulator to verify that the transceiver returns a CONNECTION RELEASE COMPLETE SNPDU to the GES Emulator.  Use the test set to verify the corresponding CLEAR INDICATION Packet to the test set and to return a CLEAR CONFIRMATION Packet to the transceiver. 

## 2.4.7.3.3.2 Called And Calling Address Extension (Nsap) Test

 
The Called and Calling Address Extension (NSAP) tests are designed to test the transceiver's ability to process packets which contain the NSAP addressing scheme. 

 
Step 1 - Call Request from HLE 
 
Program the Test Set to send a CALL REQUEST Packet to the transceiver.  Fill the Facilities Field with the following facilities: Calling Address Extension Facility, and Called Address Extension Facility.  Use the GES Emulator to verify that the transceiver transmits a corresponding CONNECTION REQUEST SNPDU to the GES, and that the NSAP addresses have been transparently transferred. 
 
 
Step 2 - Call Accept from the GES 
 
Program the GES Emulator to return a CONNECTION CONFIRM SNPDU to the 
transceiver without the Responding NSAP Address Field from the request in Step 1. Use the test set to verify that the transceiver transmits the corresponding CALL CONNECTED Packet to the GES Emulator with the same called NSAP address that was in the original CALL REQUEST Packet. 
Step 3 - CALL REQUEST from GES 
 
This test is covered by test case PM18_105 as conducted in Section 2.4.7.2. 
Step 4 - CALL ACCEPT from HLE 
 
This test is covered by test case PM18_105 as conducted in Section 2.4.7.2. 
Step 5 - CALL ACCEPT from HLE - (Different NSAPs) 
 
This test is covered by test case PM20_109 as conducted in Section 2.4.7.2. 
Step 6 - Clear Request Procedures 
 
This test clears the open channel.  Program the Test Set to send a CLEAR REQUEST Packet to the transceiver.  Use the GES Emulator to verify that the transceiver transmits the corresponding CONNECTION RELEASED SNPDU to the GES.  Use the GES Emulator to return the corresponding CONNECTION RELEASE COMPLETE SNPDU to the transceiver.  Verify the corresponding CLEAR CONFIRMATION Packet. 

## 2.4.7.3.3.3 Throughput Class Negotiation Facility

 
This test verifies the transceiver's ability to process a CALL REQUEST Packet and CONNECTION CONFIRM SNPDU with Throughput Class Negotiation Facility. 
Step 1 - Call Request from the Test Set 
 
Program the test set to send a CALL REQUEST Packet to the transceiver with the Facilities Field containing Throughput Class Negotiation facility with requested throughput class of 7 in both directions.  Use the GES Emulator to verify that the transceiver transmits a CONNECTION REQUEST SNPDU to the GES with the same throughput classes in both directions. 
Step 2 - Call Accept from the GES 
 
Program the GES Emulator to send a CONNECTION CONFIRM SNPDU to the transceiver with throughput classes less than or equal to the requested throughput classes.  Verify that the transceiver sends the corresponding CALL CONNECTED Packet to the Test Set with the same throughput classes. 
 
Step 3 - Clear Request from the Test Set 


Perform the procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3 to clear the channel. 

## 2.4.7.3.3.4 Transit Delay Selection And Indication Facility

 
This test verifies the transceiver's ability to process a CALL REQUEST Packet and CONNECTION CONFIRM SNPDU with Transit Delay Selection and Indication Facility. 

 
Step 1 - Call Request from the Test Set 
 
Program the test set to send a CALL REQUEST Packet to the transceiver with the Facilities Field containing the Transit Delay Selection and Indication Facility with a desired delay of 100 ms.  Use the GES Emulator to verify that the transceiver transmits a CONNECTION REQUEST SNPDU to the GES with the same value of delay. 
Step 2 - Call Accept from the GES 
 
Program the GES Emulator to send a CONNECTION CONFIRM SNPDU to the transceiver with the applicable transit delay value of 5 s.  Verify that the transceiver sends the corresponding CALL CONNECTED Packet with the same transit delay value to the test set. 
Step 3 - Clear Request from the Test Set 
 
Perform the procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3 to clear the channel. 

## 2.4.7.3.3.5 Priority Facility

 
The Priority Facility test procedure is designed to test the transceiver's ability to process the Priority facility during connection establishment and to forward a DATA Packet with the agreed upon priority. 

 
Step 1 - Call Request with Distress Priority from the Test Set 
 
Program the test set to send a CALL REQUEST Packet to the transceiver with the Facilities Field containing a Priority facility with a target value of 14 for priority of data on a connection.  Use the GES Emulator to verify that the Data indication LIDU containing the CONNECTION REQUEST SNPDU from the transceiver has Q precedence level of 14. 
 
 
Step 2 - Call Accept from the GES.  GES Responds with the Same Priority. 
 
Program the GES Emulator to send the transceiver a Data request LIDU containing a 
CONNECTION CONFIRM SNPDU with Q precedence level of 14.  Verify that the transceiver sends the corresponding CALL CONNECTED Packet to the test set with the selected value of 14 for priority of data on a connection. 
Step 3 - Data from the Test Set 
 
Program the test set to send a DATA Packet to the transceiver.  Use the GES Emulator to verify that the Data indication LIDU containing the DATA SNPDU received from the transceiver has Q precedence level of 14. 
Step 4 - Clear Request from the Test Set 
 
Perform the procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3 to clear the channel. 
Step 5 - Call Request from the Test Set 
 
Perform the call setup procedure in Step 1 above. 
Step 6 - Call Accept from the GES.  GES Responds with a Lower Priority. 
 
Program the GES Emulator to send to the transceiver a Data request LIDU containing a CONNECTION CONFIRM SNPDU with Q precedence level of 11.  Verify that the transceiver sends the corresponding CALL CONNECTED Packet to the test set with the selected value of 11 for priority of data on a connection. 
Step 7 - Data from the Test Set 
 
Program the test set to send a DATA Packet to the transceiver.  Use the GES Emulator to verify that the Data indication LIDU containing DATA SNPDU received from the transceiver has Q precedence level of 11. 
Step 8 - Clear Request from the Test Set 
 
Perform the procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3 to clear the channel. 

## 2.4.7.3.4 Multiple Channel Transactions

 
The Multiple Channel Transactions test procedures are designed to test the transceiver's ability to process a transaction on one channel while not affecting the operation of the other open channels. 

 

## 2.4.7.3.4.1 Call Request Procedures

 
This test opens multiple channels with the transceiver.  Perform the virtual call setup procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 1 twelve times to open the following ISO 8208 channel numbers: 2816, 2815, 2814, 2813, 2812, 2811, 2810, 2809, 2808, 2807, 2806, and 2805.  Verify that the transceiver selects the following channel numbers: 255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, and 244. 

## 2.4.7.3.4.2 Data Transmission Procedures

 
This test transmits data from the HLE.  Perform the data transmission procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 2 for each open channel.  Verify that all 12 channels are operating. 

## 2.4.7.3.4.3 Clear Request Procedures

 
This test clears opened channels.  Perform the clear request procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3 for channels 2814 and 2809.  Perform the data transmission procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 2 for the remaining 10 channels.  Verify that the clearing procedures did not affect the operation of the other channels by confirming that the transceiver forwards the corresponding DATA SNPDUs to the GES Emulator on all 10 channels. 

## 2.4.7.3.4.4 Reset Request Procedures

 
This test resets channels.  Perform the reset request procedures in Section 2.4.7.3.1.1 Reset States Step 1 for channels 2815, 2811 and 2806.  Perform the data transmission procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 2 for the 10 channels.  Verify that the resetting procedures did not affect the operations of the transceiver by confirming that the transceiver forwards the DATA SNPDUs to the GES Emulator. 

## 2.4.7.3.4.5 Receive Not Ready Status

 
Step 1 - Data Transfer 
 
This test transfers data from the GES Emulator. 
 
a. 
Program the GES Emulator to send two DATA SNPDUs to the transceiver for each open channel, each containing 56 bits of user data.  Set M-bit to zero in both packets.  Verify the corresponding ISO 8208 Packets sent by the transceiver to the test set. 
 
b. 
Program the test set to return RECEIVE READY Packets to the transceiver for all open channels except 2816, 2810 and 2805. 
 
c. 
Perform the procedure in Step 1a for the following SSND channels: 254, 252, 251, 250, 247, 246 and 245.  Verify that the receive not ready conditions on channels 2816, 2810 and 2805 do not affect the operations of the other channels 
by confirming that the transceiver forwards the corresponding DATA Packets to the HLE. 

 
 
Step 2 - Clear Request Procedures 
 
This test clears channels.  Perform the clear request procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3 for channels 2816, 2810 and 2805.  Verify the results. 

## 2.4.7.3.4.6 Error Recovery Procedures Step 1 - Force An Error Condition

 
 
This test forces channels into an error recovery state. 
 
a. 
Program the Test Set to send a CALL REQUEST Packet to the transceiver on channels 2815 and 2807.  Verify that the transceiver returns a CLEAR INDICATION Packet to the HLE on channels 2815 and 2807.  Also verify that the transceiver transmits, on channels 254 and 246, a CONNECTION RELEASED SNPDU to the GES Emulator.  Diagnostic codes should be set to 23. 
 
b. 
Perform the data transmission procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 2 for channels 2813, 2812, 2811, 2808, and 2806.  Verify that the error recovery conditions on channels 2815 and 2807 do not affect the operations of the other open channels by confirming that the transceiver forwards the corresponding DATA SNPDUs to the GES Emulator. 
 
c. 
Program the Test Set to send a CLEAR CONFIRMATION Packet to the transceiver on channels 2815 and 2807.  Program the GES Emulator to respond to the transceiver with a CONNECTION RELEASE COMPLETE SNPDU for channels 254 and 246. 
Step 2 - Clear Open Channels 
 
This test clears open channels.  Perform the clear request procedure in Section 2.4.7.3.1.1 Call Setup and Clearing States Step 3 for channels 2813, 2812, 2811, 2808 and 2806. 

## 2.4.7.3.5 Iso 8208 Dce Timer Test Procedures (Section 2.2.7.5.2.3.4)

 
The DCE Timer test procedures are designed to test the transceiver's ability to perform corrective actions when the ISO 8208 DCE timers tN10 through tN13 expire. 

## 2.4.7.3.5.1 Tn10 Timer Procedure

 
Program the test set to send a RESTART CONFIRMATION Packet to the transceiver. Verify that the transceiver sends a RESTART INDICATION Packet to the HLE.  Wait and 
verify that, within the interval of tN10 to tN10+5 seconds after sending the RESTART INDICATION Packet, the transceiver sends another RESTART INDICATION Packet. 

 
 
NOTE: 
To facilitate the next test, initialize the transceiver by using the test set to return a RESTART CONFIRMATION Packet to the transceiver; there should be no ISO 8208 outputs from the transceiver. 

## 2.4.7.3.5.2 Tn11 Timer Procedure

 
Program the GES Emulator to send a CONNECTION REQUEST SNPDU to the transceiver without starting tN1 (see Reference Document "A", Table 15.1).  Verify that the transceiver sends a corresponding INCOMING CALL Packet to the HLE.  Wait and verify that, within the interval of tN11 to tN11+5 seconds after sending the INCOMING CALL Packet, the transceiver sends a CLEAR INDICATION Packet to the HLE and a CONNECTION RELEASED SNPDU to the GES Emulator. 
 
 
NOTE: 
To facilitate the next test, initialize the transceiver by using the test set to send a CLEAR CONFIRMATION Packet to the transceiver, and use the GES Emulator to send a CONNECTION RELEASE COMPLETE SNPDU to the transceiver; there should be no ISO 8208 outputs at the transceiver/HLE interface and no 
SNPDU outputs at the transceiver/GES Emulator interface. 

## 2.4.7.3.5.3 Tn12 Timer Procedure

 
Perform the call setup procedure in Section 2.4.7.3.1 Call Setup and Clearing States Step 1. Program the GES Emulator to send a RESET SNPDU to the transceiver without starting the timer tN3 (see Reference Document "A", Table 15.1).  Verify that the transceiver sends a corresponding RESET Packet to the HLE.  Wait and verify that, within the interval of tN12 to tN12+5 seconds after sending the RESET packet, the transceiver sends a CLEAR INDICATION Packet to the HLE and a CONNECTION RELEASED SNPDU to the GES Emulator. 
 
 
NOTE: 
To facilitate the next test, initialize the transceiver by using the test set to send a 
CLEAR CONFIRMATION Packet to the transceiver, and use the GES Emulator 
to send a CONNECTION RELEASE COMPLETE SNPDU to the transceiver; there should be no ISO 8208 outputs at the transceiver/HLE interface and no 
SNPDU outputs at the transceiver/GES Emulator interface. 

## 2.4.7.3.5.4 Tn13 Timer Procedure

 
Program the test set to send a CALL ACCEPTED Packet to the transceiver.  Verify that the transceiver returns a CLEAR INDICATION Packet to the HLE.  When the CLEAR INDICATION Packet is received at the test set, program the test set to send a CALL ACCEPTED Packet after a delay of more than tN13 seconds.  Verify that the transceiver returns a CLEAR INDICATION Packet to the HLE. 
 

## 2.4.7.4 Join And Leave Event Test Requirements (Section 2.2.7.5.3)

 
Verify that a Join event message in accordance with Section 2.2.7.5.3 is transmitted to the 
routing function upon determination of availability of the air/ground data link. Similarly, verify that a Leave event message is transmitted upon determination of non-availability of the air/ground data link. 

## 2.4.8 Satellite Subnetwork Circuit-Mode Service Test Requirements (Optional) (Section 2.2.8)

 
Equipment Required 
GES Emulator. 
 
Telephone Handset. 
 
Directional Coupler, 30 dB coupling, 60 watts average power rating (NARDA Model 3002-
30 or equivalent). 
 
High Power RF Load, 50 ohms, greater than 60 watts average power rating (RLC 
Electronics, Inc. Model T-1005 or equivalent). 
 
4.8 kbps Codec Test Set as described in Section 10.1 of Annex 1 to Reference Document 
"D", V1.24 and in Attachment 6 to Annex 1 of Reference Document "D", V1.24 (see 
also "VCTS Addendum" in this section). 
Measurement Procedure 
 
For the 9.6 kbps voice codec, connect the equipment as shown in Figure 2-37; for the 4.8 kbps voice codec, connect the equipment as shown in Figure 2-38.  Refer to Table 2-20 and Table 2-21 for cross-references between this document and Reference Document "D". 

Circuit-mode service testing is specified in Reference Document "D" Annex 1 Section 6 (Phase 1 tests), including the details in Attachment 3, and Annex 3 Section 5 (Phase 2 tests).  The abstract test descriptions in Attachment 3 are in compliance with the ISO-9646 standardized testing methodology and framework, and are specified using the Tree and Tabular Combined Notation (TTCN) standard test description language.  Level 1 and 2 transceivers (which do not provide any circuit-mode services) are not required to perform any of these tests.   

 
Additional verification is provided for the 4.8 kbps voice encoding algorithms in Reference 
Document "B", V1.20.  These tests, through the use of a standardized test setup described 
therein, verify proper implementation of the voice encoding and decoding algorithms.  For further information on the 4.8 kbps Voice Codec Test Set (VCTS), refer to the VCTS Addendum at the end of Section 2.4.8. 
 
The referenced circuit-mode voice service testing includes the following: 
Reference Document "D" Annex 1 Section 6: 



Version 
 
6.1  
Assumptions 
 
6.2  
Test Suite Structure 
 
6.2.1  
Proper Test Cases 
 
6.2.2  
Improper Test Cases 
 
6.2.3  
Inopportune Test Cases 
 
6.2.4  
Mandatory and Optional Tests 
 
6.2.5  
Test Groups and Test Case Reference Numbers 


(Required tests) 
 
6.3  
Test Suite Requirements 
 
6.3.1  
CM110: Air Origination Call - Initial Call Setup 
 
6.3.1.1 
(Information only) 
 
6.3.1.2 
CM110 Test Cases 
 
6.3.2  
CM111: Air Origination Call - Await Channel Assignment 
 
6.3.2.1 
(Information only) 
 
6.3.2.2 
CM111 Test Cases 
 
6.3.3  
CM112: Air Originating Call - Await Connect State 
 
6.3.3.1 
(Information only) 
 
6.3.3.2 
CM112 Test Cases 
 
6.3.4  
Not Applicable (circuit-mode data service) 
 
6.3.5  
Not Applicable (circuit-mode data service) 
|          | 6.3.6                        | Not Applicable (Supplementary Signal)                      |
|----------|------------------------------|------------------------------------------------------------|
|          | 6.3.7                        | CM210: Ground Originating Call - Initial Call Setup        |
|          | 6.3.7.1                      | (Information only)                                         |
|          | 6.3.7.2                      | CM210 Test Cases                                           |
|          | 6.3.8                        | CM211: Ground Originating Call - Channel Allocation        |
|          | 6.3.8.1                      | (Information only)                                         |
|          | 6.3.8.2                      | CM211 Test Cases                                           |
|          | 6.3.9                        | CM212: Ground Originating Call - C-channel Continuity Test |
|          | 6.3.9.1                      | (Information only)                                         |
|          | 6.3.9.2                      | CM212 Test Cases                                           |
|          | 6.3.10                       | CM213: Ground Originating Call - Missing Signal Processing |
|          | 6.3.10.1                     | (Information only)                                         |
|          | 6.3.10.2                     | CM213 Test Cases                                           |
|          | 6.3.11                       | CM214: Ground Originating Call - Wait for Answer           |
|          | 6.3.11.1                     | (Information only)                                         |
|          | 6.3.11.2                     | CM214 Test Cases                                           |
|          | 6.3.12                       | CM215: Ground Originating Call - Await Connect Acknowledge |
|          | 6.3.12.1                     | (Information only)                                         |
|          | 6.3.12.2                     | CM 215 Test Cases                                          |
|          | 6.3.13                       | CM216: Ground Originating Call - The Answered State        |
|          |                              |                                                            |
|          | 6.3.13.1                     | (Information only)                                         |
|          | 6.3.13.2                     | CM216 Test Cases                                           |
|          | 6.3.14                       | Not Applicable (circuit-mode data service)                 |
|          | 6.3.15                       | Not Applicable (circuit-mode data service)                 |
|          | 6.3.16                       | Not Applicable (Supplementary Signal)                      |
| 6.3.2.2  | CM111 Test Cases             |                                                            |
| 10.1     | Codec Test Set               |                                                            |
| 10.2     | Test Suite Structure         |                                                            |
| 10.2.1   | Test Case Identifier Numbers |                                                            |
| 10.2.2   | Test Case Summary            |                                                            |
| 10.3     | Test Suite Requirements      |                                                            |
| 10.3.1   | Decoder Tests                |                                                            |
| 10.3.1.1 | Test Cases                   |                                                            |
| 10.3.2   | Encoder Tests                |                                                            |
| 10.3.2.1 | Test Cases                   |                                                            |

 
Reference Document "D" Annex 2 Section 5: 

 
5.1  
Telephone Communication Service 
 
5.1.1  
Air Originated Successful Telephone Call Test 
 
5.1.2  
Air Originated Unsuccessful Telephone Call Test 
 
5.1.3  
Ground Originated Successful Telephone Call Test 
 
5.1.4  
Ground Originated Unsuccessful Telephone Call Test 
 
5.1.5  
Multiple Simultaneous Telephone Call Test 
 

| Reference                             | Reference    | Reference Document "D"                    |
|---------------------------------------|--------------|-------------------------------------------|
| Document "A"                          | Document "B" | (Test cases)                              |
| 6.1 to 6.1.5                          | 10.2.1       | N/A: No peer-to-peer protocol requirement |
| 6.1.6                                 | 10.2.1,      |                                           |
| Annex 1 Table                         |              |                                           |
| CR5.1                                 |              |                                           |
| CM111_108, CM112_107, CM140_106,      |              |                                           |
| CM211_104, CM212_104, CM213_106,      |              |                                           |
| CM214_107, CM215_106, CM216_105       |              |                                           |
| 6.3 to 6.4                            | 10.2.1       | N/A: No peer-to-peer protocol requirement |
| 6.5                                   | 10.2.1       | Tested throughout CM110, CM111, CM112     |
| Test Groups                           |              |                                           |
| 6.5.1                                 | 10.2.1       | CM110_102, CM111_105, CM111_109           |
| 6.5.2                                 | 10.2.1       | CM110_101, CM111_101, CM111_102,          |
| CM111_103, CM111_104                  |              |                                           |
| 6.5.2.1 to 6.5.3                      |              | N/A                                       |
| 6.5.5                                 | 10.2.1       | CM111_106, CM111_107, CM112_105,          |
| CM212_103, CM213_105, CM214_105,      |              |                                           |
| CM215_103, CM215_105, CM216_101       |              |                                           |
| 6.6                                   | 10.2.1       | Tested throughout CM210, CM211, CM212,    |
| CM213, CM214, CM15, CM216 Test Groups |              |                                           |
| 6.6.1                                 | 10.2.1       | CM211_102, CM213_103, CM213_104,          |
| CM213_204, CM213_205                  |              |                                           |
| 6.6.2                                 |              | N/A                                       |
| 6.6.2.1                               | 10.2.1       | CM210_101, CM210_102, CM211_101,          |
| CM212_101                             |              |                                           |
| 6.6.2.2                               |              | N/A                                       |
| 6.6.4                                 | 10.2.1       | CM111_106, CM112_104, CM212_102,          |
| CM214_103, CM215_104, CM216_102,      |              |                                           |
| CM216_103                             |              |                                           |
| 6.7                                   |              | N/A                                       |
| 6.7.1                                 | 10.2.1       |                                           |
| 6.7.2                                 | 10.2.1       | N/A: No peer-to-peer protocol requirement |
| 6.7.5                                 | 10.2.1       | CM112_106, CM214_102, CM215_102,          |
| CM216_104                             |              |                                           |
| 6.7.6                                 | 10.2.1       | N/A: No peer-to-peer protocol requirement |
| Reference                       | Reference    | Reference Document "D"                    |
|---------------------------------|--------------|-------------------------------------------|
| Document "A"                    | Document "B" | (Test cases)                              |
| 6.8                             |              | N/A                                       |
| 6.9                             | 10.2.1       | N/A                                       |
| 6.9.1                           | 10.2.1       | N/A                                       |
| 6.9.1.1                         | 10.2.1       | N/A: No peer-to-peer protocol requirement |
| 6.9.1.3                         | 10.2.1       | N/A: No peer-to-peer protocol requirement |
| A5 - 2.1                        |              |                                           |
| SNM5_101 to SNM5_305,           |              |                                           |
| SNM6_101 to SNM6_303            |              |                                           |
|                                 | 10.3.1       | All CM tests in 6.3.                      |
|                                 | 10.4.1       | CM111_103                                 |
|                                 | 10.4.2       | CM111_106, CM112_104, CM211_103,          |
| CM212_102, CM212_103, CM214_103 |              |                                           |
|                                 | 10.4.3       | CM130_101                                 |
|                                 | 10.4.4       | CM112_106, CM121_102, CM130_102,          |
| CM140_105                       |              |                                           |
|                                 | 10.4.5       |                                           |
|                                 | 10.5         |                                           |
| PL 6_09                         |              | Annex 2,                                  |
| I through VIII                  |              |                                           |

## 

| Reference                     | Reference    | Reference Document "D"        |
|-------------------------------|--------------|-------------------------------|
| Document "G"                  | Document "B" | Annex 1                       |
| Version 1.20                  |              |                               |
| 1.3                           |              | N/A - Guidance Material       |
| 1.4                           |              | N/A - Guidance Material       |
|                               | 12.2.1       | AME1_101, AME1_113            |
|                               | 12.2.2       | AME1_102, AME1_103, AME1_104, |
| AME1_105, AME1_106, AME1_107, |              |                               |
| AME1_108, AME1_109, AME1_115, |              |                               |
| AME1_116                      |              |                               |
|                               | 12.2.3       | AME1_110                      |
|                               | 12.2.4       | AME1_111, AME1_112            |
| 1.5                           |              | AME1_114                      |
| Reference                     | Reference    | Reference Document "D"          |
|-------------------------------|--------------|---------------------------------|
| Document "G"                  | Document "B" | Annex 1                         |
| Version 1.20                  |              |                                 |
| 1.6                           |              | Tested throughout AME1 and AME2 |
| 1.7                           |              | N/A - Guidance Material         |
|                               | 12.3.1       | AME2_101, AME2_112              |
|                               | 12.3.2.1     | AME2_102, AME2_103, AME2_104,   |
| AME2_105, AME2_106, AME2_107, |              |                                 |
| AME2_114                      |              |                                 |
|                               | 12.3.2.2     | AME2_115                        |
|                               | 12.3.3       | AME2_109                        |
|                               | 12.3.4       | AME2_110, AME2_111              |
|                               | 12.3.5       | AME2_113                        |

 
                          NOTE: 
                                            The absence of entries in the right-hand columns may indicate that tests are 
                                            manufacturer-specific and should be shown by demonstration or analysis; or 
                                            may simply be related to a high-level statement not intended for testing.  

 
VCTS ADDENDUM The Voice Codec Test Set (VCTS) hardware consists of four functional pieces of equipment: 1)  The I/O Interface Unit, which contains the analog and PCM interfaces and the TRL Channel Unit interfaces. 2)  The VCTS software and two IBM PC-compatible DSP boards. 3)  The IBM-PC compatible computer, which runs the software and holds the DSP boards. 4)  The optional TRL Aero-I Ground Data Unit (GDU), which provides an RF interface to the equipment under test if this is needed.  
 
The I/O Interface Unit The I/O Interface Unit connects to the DSP boards in the test computer to the TRL GDU (if used), and the unit under test. It contains interface circuitry to allow several different analog or digital interfaces to be used. It also contains level adjustment capabilities to allow a wide range of analog levels to be accommodated. The analog and digital interfaces to external equipment that are supported include: 2-wire analog (RJ11), 4-wire analog (RCA phono jacks), and digital 16-bit linear, 8-bit -law, and 8-bit A-law. The I/O Interface Unit also contains two digital baseband channel interfaces, both are on RS442, DB-37 serial interface connectors.  The PCM interface is a DB-15 connector, this provides the user with the choice of interfacing at digital baseband, IF or RF.  In case of the IF or RF interface, the TRL GDU (or equivalent) is required. 

There is no test software embedded in the interface unit. The identification of the interface unit is: Inmarsat Mini-M VCTS I/O Interface Unit The Voice Codec Test Set Software This software resides in the PC. The VCTS uses its software and DSP boards, interfaced through the hardware to perform as series of diagnostics on the unit under test.  The tests produce performance measurements such as: frequency response, gain, spectral distortion, period deviation, pitch errors, voiced and unvoiced errors,  idle channel noise, crosstalk, and out-of-band frequency response.  The diagnostic tests are divided into tests on the voice encoder, tests of the voice decoder, tests of an encoder-decoder pair, and tests of the decoder-encoder pair (the baseband tests). During voice encoder tests the computer presents known signals to the speech input of the unit-under-test (UUT).  The computer monitors the channel output of the UUT via the GDU interface. The computer compares the response of the UUT to objective criteria (these are specified in Reference Document "B") to verify the UUTs performance. Similarly, during voice decoder tests the computer presents a known channel bit stream input to the UUT (via the GDU interface).  The computer then monitors the synthesized speech of the UUT and compares the results to the objective performance criteria (these are specified in Reference Document "B") to verify and analyze the UUT's performance. During the encoder-decoder tests, an encoder's digital channel output is connected to a decoder's digital channel input while presenting known speech input to the encoder and monitoring the speech output of the decoder. The channel connection between the encoder and the decoder can be accomplished externally to the VCTS, for example via the GDU IF interface. The decoder's output is then analyzed and compared with the objective performance criteria. During decoder-encoder, or baseband tests, the VCTS will send channel data (via the GDU) into a decoder under test. The speech output of the decoder will be connected to the speech input of an encoder, and the VCTS will monitor and analyze the channel data (via the GDU interface) output from the encoder-under-test. During the VCTS operation, the test operator monitors and controls the diagnostics via a menu- driven graphical user interface. The user interface will permit the operator to perform an individual test, or collections of tests. The test software is available from Digital Voice Systems, Inc., as Version 1.5.  The DSP boards are manufactured by Communications Automation & Control (Part Number: CAC 32C V2).  A test set may use hardware and/or software equivalent to these specific model and version numbers provided that the equivalent hardware and/or software meets the performance and interoperability requirements of Section 2.2.8. 

## The Ibm-Compatible Pc The Minimum Recommended Configuration Of The Pc Is: 33 Mhz 486, 4Mb Memory, 50 Mb Free Hard Disk Space, Two Free 16 Bit Isa Slots (For The Dsp Cards), 640 X 480 Vga Graphics, A 3.5" Floppy Disk Drive, And A Keyboard. Trl Ground Data Unit

 
This piece of equipment is used if the equipment under test requires an IF or RF interface. This unit uses the AES IF/RF output (a standard 8.4 kbps C-channel) and provides the baseband data output as would exist between an GES demodulator and the GES codec.  The TRL GDU model number is ACM 7703I Multirate GDU, or equivalent.  
 
2.4.8.1 
Priority, Precedence and Preemption (Sections 2.2.1 (circuit mode) and 2.2.8.1) a. AMS(R)S Preemption Step 1.  Load the transceiver to its capacity with C-Channel calls (this may be accomplished in a multi-channel transceiver by temporarily disabling some channels). There shall be a minimum of one C-Channel of Circuit-mode Priority Level 4. Step 2.  Using the test set, initiate a call of Circuit-mode Priority Level 3.  At the GES Emulator, verify that a call of the lowest priority has been cleared, and that the new call (of Circuit-mode Priority Level 3) has been established. Step 3.  Repeat Step 1. Step 4.  Using the GES Emulator, initiate a call of Circuit-mode Priority Level 3.  At the test set, verify that a call of the lowest priority has been cleared, and that the new call (of Circuit-mode Priority Level 3) has been established. b. Distress/Urgency Preemption Step 1.  Load the transceiver to its capacity with C-Channel calls (this may be accomplished in a multi-channel transceiver by temporarily disabling some channels). There shall be a minimum of one C-Channel call of Circuit-mode Priority Level 2 and there shall be no calls Circuit-mode Priority Level 4. Step 2.  Using the test set, initiate a call of Circuit-mode Priority Level 1.  At the GES Emulator, verify that a call of the lowest priority has been cleared, and that the new call (of Circuit-mode Priority Level 1) has been established. Step 3.  Repeat Step 1. 

 
Step 4.  Using the GES Emulator, initiate a call of Circuit-mode Priority Level 1.  At the test set, verify that a call of the lowest priority has been cleared, and that the new call (of Circuit-mode Priority Level 1) has been established.  

## 2.4.9 Failure/Status Indication (Section 2.2.10) Equipment Required

 
GES Emulator. 
 
8208 Test Set (as applicable). 
 
Directional Coupler, 30 dB coupling, 60 watts average power rating (NARDA model 3002-
30 or equivalent). 
 
High Power RF Load, 50 ohms, greater than 60 watts average power rating (RLC 
Electronics, Inc. model T-1005 or equivalent). 
 
Telephone Handset (as applicable). 
Note: The format of the Failure/Status Indications are not specified and may vary by 
the intended installation.  Additional test equipment may be necessary to confirm that the correct annunciation is being indicated. Measurement Procedure Connect the equipment as shown in Figure 2-37.  Manually log on to the GES and verify the AES is capable of sending data and placing voice calls as applicable to the AES operational service level.  Confirm that the AES is indicating that SATCOM is capable of Voice and Data communications. Induce failures that prevent SATCOM from supporting voice communications.  Confirm that the AES indicates (without operator action) that SATCOM Voice is not available. Induce failures that prevent SATCOM from supporting data communications.  Confirm that the AES indicates (without operator action) that SATCOM Data is not available. Induce failures that prevent SATCOM from supporting voice and data communications. Confirm that the AES indicates (without operator action) that SATCOM Voice and Data are not available. 

## 3.0 Installed Equipment Performance 3.1 Equipment Installation 3.1.1 Accessibility

 
Controls and monitors provided for in-flight operation shall be readily accessible from the appropriate operator's normal seated position.  The operator/crew member(s) shall have an unobstructed view of the display(s) or controls when in the normal seated position. 

## 3.1.2 Aircraft Environment

 
Equipment shall be compatible with the environmental conditions present in the specific location in the aircraft where the equipment is installed. 

## 3.1.3 Display Visibility

 
All installed system displays shall be readily visible and readable from the operator's/crew member's normal position in all ambient lighting conditions for which system use is required. 

 
 
NOTE: 
Visors, glareshields, or filters may be an acceptable means of obtaining 
daylight visibility. 

## 3.1.4 Inadvertent Turn Off

 
Where controls for transceiver operation are provided, they shall be equipped with adequate protection against inadvertent turn off. 

## 3.1.5 Failure Protection

 
Any failure of the equipment shall not degrade the normal operation of the equipment or systems connected to it.  Likewise, the failure of interfaced equipment shall not degrade normal operation of this equipment. 

## 3.1.6 Interface Interference Effects

 
The equipment shall not be the source of harmful conducted or radiated interference, and shall not be affected by conducted or radiated interference from other equipment or systems installed in the aircraft. 
Adequate protection of on-board GNSS equipment from harmful interference due to AMSS equipment meeting the requirements of Section 2 is based on an average interference power level not exceeding -113.5 dBm referenced to the port of the GNSS antenna, where the spectral width of the interfering signal(s) lies in the range of 10 to 100 kHz. 
 
NOTES: 
1. In a typical installation, this could be achieved if: 

 
 
a) the transceiver meets all requirements of Sections 2.2.3.13, 2.2.4.2.5 
and 2.2.4.2.6; 
 
b) the isolation between AMSS and GNSS antennas is not less than 40 dB; and 
 
c) interfering intermodulation products generated external to the transceiver do not increase the average interference power level referenced to the port of the GNSS antenna by more than 1.5 dB. 
2. Interference problems noted upon installation of this equipment may result 
from such factors as the design characteristics of previously installed 
systems or equipment and the physical installation itself.  It is not intended that the equipment manufacturer design for all installation environments. The installing facility will be responsible for resolving any incompatibility between this equipment and previously installed equipment in the aircraft. 
3. Potential interference harmful to GNSS due to the transceiver is expected 
only in the case of multiple C-channel operations. The spectral width of the interference will fall in the range of 10 to 100 kHz. 

## 3.1.7 Aircraft Power Source

 
The voltage and frequency tolerance characteristics of the equipment shall be compatible with the aircraft power source of appropriate category as specified in RTCA DO-160C. 

## 3.2 Installed Equipment Performance Requirements

 
The installed equipment shall meet the requirements of Section 2.0 in addition to the requirements stated below.  To meet the requirements of this section, test results supplied by the equipment manufacturer may be accepted in lieu of tests performed by the equipment installer. 

 
However, performance characteristics which cannot be tested by the equipment manufacturer shall be tested by the installer.  These include: (1) performance characteristics of equipment required for the transceiver installation that have not been tested or verified by the manufacturer, and (2) interactions with other equipment installed on the aircraft. 

## 3.3 Conditions Of Test

 
The following Sections define conditions under which the tests specified in Section 3.4 shall be conducted. 
 

## 3.3.1 Power Input

 
Tests may be conducted either with the equipment powered by the aircraft's electrical power generation system or by an appropriate external power source connected to the aircraft. 

## 3.3.2 Environment

 
During the tests, the equipment shall not be subjected to environmental conditions that exceed those in RTCA/DO-160C as specified by the equipment manufacturer. 

## 3.3.3 Adjustment Of Equipment

 
Circuits of the equipment under test shall be properly aligned and otherwise adjusted in accordance with the manufacturer's recommended practices prior to application of the specified tests. 

## 3.3.4 Warm-Up Period

 
Unless otherwise specified, tests shall be conducted after a warm-up (stabilization) period of twenty minutes. 

## 3.4 Test Procedures For Installed Equipment Performance

 
The following test procedures provide one means of determining installed equipment performance. Although specific tests procedures are cited, it is recognized that the installing activity may prefer alternate procedures, which may be used if they provide at least equivalent information. In such cases, the procedures cited herein should be used as one criterion in evaluating the acceptability of the alternate procedures. 

## 3.4.1 Conformity Inspection

 
Visually inspect the installed equipment to determine the use of acceptable workmanship and engineering practices.  Verify that proper mechanical and electrical connections have been made and that the equipment has been located and installed in accordance with the manufacturer's recommendations. 

## 3.4.2 Interference Tests

 
Unless otherwise specified, all aircraft electrically-operated equipment and systems shall be on, using the aircraft's electrical power generating equipment before conducting interference tests. 

 
With the transceiver operating, including transmission of messages and voice calls, individually operate each of the other electrically-operated aircraft equipment and systems to determine that no significant conducted or radiated interference exists.  Evaluate all reasonable combinations of control settings and operating modes.  Operate communication and navigation equipment on at a minimum the low, high, and a mid-band, frequencies. 
 
Operate the aircraft controls (e.g., flaps) through their range to activate all associated aircraft systems which may cause electrical power fluctuations. 
 
 
NOTE 1: Some aircraft contain cooling fans to augment airflow under certain low-speed 
conditions.  These fans are activated with flaps extended and low- to midthrottle, and cause aircraft power fluctuations when activated. 
NOTE 2: See Section 3.4.4 for requirements for message generation to operate over the R 
and T channels, and C channel (if installed). 

## 3.4.3 Power Fluctuation Tests (Section 2.2.9)

 
Transceiver aircraft power sources shall be cycled through all normal configurations to verify that the transceiver performance for power interruption recovery during and after power changeover is satisfactory with no discernable abnormal operation (Reference Section 2.2.9). 

 
 
NOTE: 
In-transit data service packets which have been acknowledged on either the DTE or DCE interface, but not yet transferred to the opposite interface, may be lost.  Non-transceiver higher layer entities which employ end-to-end 
acknowledgement protocols may choose to retransmit such lost data. 

## 3.4.4 Ground Test Procedures

 
Perform the ground test portions of tests defined in Sections 2, 3, 4 and 5 of Annex 3 (Phase 2 tests) of Reference Document "D" as follows:   

 
 
Reference Document "D" Annex 3: 
 
Physical Layer Test Group 
 
2.1  
Power Control Testing 
 
 
2.2  
Frequency Accuracy Testing 
 
 
2.3  
Bit Error Rate Performance Testing 
 
 
2.4  
Antenna Intermod Testing (Multicarrier inst. only) 
 
 
2.5  
Service Coverage Test 
 
Satellite Network Management Test Group 
 
3.1  
Initial Search Test 
 
 
3.2  
Log-On Reject Test 
 
 
3.3  
Normal Log-On Test 
 
 
3.5  
Log-On Prompt Test 
 
 
3.6  
Data Channel Reassignment Test 
 
 
3.7  
Selective Channel Release Test 
 
 
Packet-Mode Services Test Group 
 
4.2.1 
Ground-to-Air Message Transfer Test 
4.2.2 
Air-to-Ground Short Message Transfer Test 
4.2.3 
Air-to-Ground Long Message Transfer Test 
4.2.4 
Air-to-Ground Message Transfer Test 
4.2.5 
Mixed Air-to-Ground and Ground-to-Air Message Transfer Test 
4.3.1 
Ground-to-Air Connection Set-up 
4.3.2 
Air-to-Ground Connection Set-up 
4.3.3 
Ground-to-Air Connection Release 
4.3.4 
Air-to-Ground Connection Release 
4.3.5 
Multiple Connection Setup with a GES 
4.3.6 
Log-on Renewal 
4.3.7 
Log-off 
4.4.1 
Air-to-Ground Data Transfer Over a Single SVC 
4.4.2 
Air-to-Ground Data Transfer Over Multiple SVCs 
4.4.3 
Ground-to-Air Data Transfer Over a Single SVC 
4.4.4 
Ground-to-Air Data Transfer Over Multiple SVCs 
4.4.5 
Bi-directional Data Transfer 
 
Circuit-Mode Services Test Group 
 
5.1  
Telephone Communication Service (except that test criteria, Reference Document "D", Annex 3 Section 5.1, do not apply) 
 
 
5.1.1  
Air Originated Successful Telephone Call Test 
 
 
5.1.2  
Air Originated Unsuccessful Telephone Call Test 
 
 
5.1.3  
Ground Originated Successful Telephone Call Test 
 
 
5.1.4  
Ground Originated Unsuccessful Telephone Call Test 
 
 
5.1.5  
Multiple Simultaneous Telephone Call Test 
 
The installer shall verify that voice communications are satisfactory in both directions. 

## 3.4.5 Flight Test Procedures

 
Flight tests of installed systems are desirable to confirm or supplement bench and ground tests of installed performance.  Flight tests may be selected from the following: 
 
Reference Document "D" Annex 3: 
 
Physical Layer Test Group 
 
2.1  
Power Control Testing 
 
 
2.2  
Frequency Accuracy Testing 
 
 
2.5  
Service Coverage Test 


Satellite Network Management Test Group 
 
3.3  
Normal Log-On Test 
 
 
3.4  
P-channel Degradation Test 
 
Packet-Mode Services Test Group 
 
4.2.1 
Ground-to-Air Message Transfer Test 
4.2.2 
Air-to-Ground Short Message Transfer Test 
4.2.3 
Air-to-Ground Long Message Transfer Test 
4.2.4 
Air-to-Ground Message Transfer Test 
4.2.5 
Mixed Air-to-Ground and Ground-to-Air Message Transfer Test 
4.4.1 
Air-to-Ground Data Transfer Over a Single SVC 
4.4.2 
Air-to-Ground Data Transfer Over Multiple SVCs 
4.4.3 
Ground-to-Air Data Transfer Over a Single SVC 
4.4.4  
Ground-to-Air Data Transfer Over Multiple SVCs 
 
Circuit-Mode Services Test Group 
 
5.1  
Telephone Communication Service (except that test criteria, Reference Document "D", Annex 3 Section 5.1, do not apply). 
 
 
5.1.1  
Air-Originated Successful Telephone Call Test 
 
 
5.1.3  
Ground-Originated Successful Telephone Call Test 
 
 
5.1.5  
Multiple Simultaneous Telephone Call Test 
 
Where such capability is installed, the installer shall verify that voice communications are satisfactory in both directions. 

## 3.4.6 Installed Aes System Performance Verification

 
Performance of the installed, total AES, consisting of the Antenna Subsystem and the Transceiver Subsystem, should be verified in accordance with the following procedures. 

## 3.4.6.1 Aes Eirp

 
The AES Effective Isotropic Radiated Power (EIRP) is determined by using the antenna gain as verified to the requirement of Section 2.2.3.2, the transmitter output power as verified to the requirement of Section 2.2.4.2.2, and the loss of the installed coaxial cable which connects the Transceiver Subsystem to the Antenna Subsystem. 
The transmitter output power, Pout, shall be verified by using the actual loss of the system 
components and interconnecting cables as installed on the aircraft. 
The AES EIRP shall be calculated (in dB values) as: 


EIRP = Pout + GA - LI 
 
 
where: 


EIRP is the AES Effective Isotropic Radiated Power, in dBW. 
 
 
Pout is the Transceiver Subsystem full-rated output power, in dBW as verified 
from the installed system (based on Section 2.4.4.3.2). 
 
 
GA is the Antenna Subsystem gain in dBic (from Section 2.4.3.3.1). 
 
 
LI is the cable loss between the Transceiver and Antenna Subsystems, in dB. 

## 3.4.6.2 Aes G/T

 
The AES system gain-to-noise temperature ratio (G/T)AES is determined from three elements: the receiver sensitivity as verified to the requirement of Section 2.2.4.1.2, expressed as effective noise temperature (see Note in Section 2.2.4.1.2); the antenna gain and noise temperature as verified to the requirements of Sections 2.2.3.2 and 2.2.2.1; and the loss of the installed coaxial cable connecting the Transceiver Subsystem to the Antenna Subsystem. 

 
The AES G/T is calculated as: 
$(\frac{G}{T})_{\mbox{\scriptsize\it AES}}(dB)$= $G_{A}(dB)$ - 10* $\mbox{\scriptsize\rm LOG}_{10}\left[\,T_{A}+T_{I}(\,L_{I}-1)+L_{I}\,T_{R}\,\right]$
 
 
where: 
 
 
GA is the Antenna Subsystem gain (from Section 2.4.3.3.1); 
 
 
TA is the noise temperature of the antenna at the single RF port. 
 
 
TR is the noise temperature of the Transceiver Subsystem derived from the 
results of the procedure of Section 2.4.4.2.2 and the Note in Section 2.2.4.1.2.  
The Note in Section 2.2.4.1.2 indicates that TR should be limited to TR < 451 - 
298 = 153 K.  For the calculation, either TR = 153 K or the actual TR may be 
used; 
 
 
TI is the temperature of the installed cable, in K (normally 290 K); 
 
 
LI is the loss of the cable installed between the Transceiver and Antenna 
Subsystems, as a numerical quantity: 
$$L_{I}=10^{\frac{L_{I}\left(in\ dB\right)}{10}}$$. 
 
This formulation assumes that the procedures of Section 2.4.3.3.1 have been employed to determine Antenna Subsystem Gain and Noise Temperature.  If other procedures are used, they shall be justified and validated by the installer as providing equivalent information. 
The Transceiver Subsystem's receiver may be qualified to an effective noise temperature (or equivalent noise figure) lower than the maximum required by Section 2.2.4.1.2; and/or the Antenna Subsystem may be qualified to a G/T greater than the minimum required by Section 2.2.3.2.1.  If the manufacturer warrants this better performance of either component, such value(s) may be used in the above calculation. 

## 3.4.6.3 Aes Coverage Volume (Sections 2.2.3.2 And 2.2.3.3)

 
The AES Coverage Volume is the region over which the installed system simultaneously meets G/T, EIRP (Section 2.2.2.1) and Axial Ratio (Section 2.2.3.2) standards at the test frequencies defined in Section 2.4.3.1.2. 
AES Coverage Volume may be determined by analysis of test results to verify compliance. Data resulting from the preceding tests, Sections 3.4.6.1 and 3.4.6.2, shall be analyzed together with test results from Section 2.4.3.3 to determine the coverage volume of the installed AES system, as defined by Sections 2.2.3.2 and 2.2.3.3. 
G/T is to be determined only at the three Receive test frequencies and EIRP is to be determined only at the three Transmit test frequencies as specified in Section 2.4. 
 

## 4.0 Equipment Operational Performance Characteristics

 
AMSS AES installations are expected to be accomplished in a variety of ways to fit the aircraft equipment and intended usage. This will also be the case with associated cockpit interfaces.  The requirements of this section shall be suitably interpreted for the particular installation under consideration. 

## 4.1 Operational Performance Requirements

 
The following sections identify requirements to ensure the operator that operations can be conducted safely and reliably in the expected operational environment. 

## 4.1.1 Power Input

 
Prior to flight, the primary power must be available for proper operation. 

## 4.1.2 Communications Displays

 
The required display(s) for the selection of various communication modes/functions of operation shall be available for use. 

## 4.1.3 Communications Controls

 
Cockpit control(s) required for proper operation of the equipment shall be available for use. 

## 4.1.4 System  Operational Indication

 
Communication failure or degradation below minimum acceptable performance shall be readily discernible. 

## 4.1.5 Equipment Operating Limitations

 
Equipment operating limitations of the aircraft earth station should be contained in the aircraft flight manual. 

## 4.2 Test Procedures For Operational Performance Requirements

 
Operational equipment tests may be conducted as part of normal preflight tests.  For those tests which can only be run in flight, procedures should be developed to perform these tests as early in the flight as possible to verify that the equipment is performing its intended function(s). 

## 4.2.1 Power Input

 
With the aircraft's electrical power generating system operating, energize the equipment and verify that electrical power is available to the equipment. 
 

## 4.2.2 Communications Displays

 
With the equipment operating, verify that the required display(s) are operational. 

## 4.2.3 Communications Controls

 
The communications control(s) shall be operated, as required, to verify satisfactory equipment response. 

## 4.2.4 System Operational Indication

 
System operational readiness shall be monitored either by means of Built-In-Test- Equipment (BITE) and/or by suitable preflight tests contained in a check list or flight manual.  All equipment failure annunciators shall be tested during preflight tests to verify proper operation. 

## Special Committee 165 Minimum Operational Performance Standards For Aeronautical Mobile Satellite Systems (Amss)

 
SC-165 CHAIRMAN W. S. Dobbs (1988-1991)  


American Airlines 
R. A. Pickens (1991-Present) 


AvCom, Inc., Consultant for FAA 
 
SC-165 SECRETARY J. R. Child (1988-1989) 


CTA, Inc. 
L. W. Patak (1989-1990) 


CTA, Inc. 
F. P. Mackowick (1990-1991) 


CTA, Inc. 
T. Dehel (1991-1993)  


CTA, Inc. 
F. P. Mackowick (1993-Present)  


CTA, Inc./SkyComm, Inc. 
 
RTCA 
Jerry G. Bryant  


RTCA, Inc. 
 
WORKING GROUP 1 -- AMSS Aeronautical Equipment Standards Chairman 
G. A. Cobley 


Rockwell/Collins 
Secretary 
O. K. Nyhus 


Honeywell 
 
WORKING GROUP 2 -- AMSS Applications Chairman 
A. Snively  


American Airlines 
 
WORKING GROUP 3 -- AMSS Systems/Services Performance Criteria Chairman 
R. A. Pickens 


AvCom, Inc. 
Secretary 
L. W. Patak (1989-1990) 
 
CTA, Inc. 
 
F. P. Mackowick (1990-1991) 
CTA, Inc. 
 
T. Dehel (1991-1993)  
CTA, Inc. 
 
F. P. Mackowick (1993-Present) 
SkyComm, Inc.. 
 
WORKING GROUP 4 -- Technical and Editorial Chairman 
D. K. Dement (1988-1995)  
 
Novacom, Inc. 

 
WORKING GROUP 5 -- AMS(R)S Voice Implementation and Utilization Chairman 
P. R. Ryan (1993-1994) 
 
 
Honeywell 
 
P. W. Lemme (1994-1997)  
 
Boeing Vice-Chairman F. P. Mackowick (1994-1997) 
 
SkyComm, Inc. 

Secretary F. P. Mackowick (1993-1994) 
 
CTA Incorporated 
 
D. Reese (1994-Present) 
 
 
Honeywell MEMBERS AND ADVISERS S. Abatut Aerospatiale D. Allcock Canadian Marconi Company W. Aleshire United Air Lines D. S. Anderson NTIA, Department of Commerce M. I. Anderson Boeing Commercial Airplanes P. Anderson Northwest Airlines R. E. Anderson Anderson Associates T. A. Anderson ARINC 
P. H. Arnstein United States Coast Guard R. Aubry SITA 
R. M. Baca Federal Communication Commission S. Bagieu Aerospatiale B. Bailey Canadian Marconi Company F. E. Bannister INMARSAT 
M. Barmat Jansky/Barmat Telecommunications P. M. Bartosch AVEWB 
P. Baton Aeronautical Radio, Inc. 

R. S. Beale Aeronautical Radio, Inc. 

J. L. Begis Telecommunication Systems Engineering A. H. Beining Hughes Aircraft Company H. W. Benningfield Honeywell, Inc. 

J. Bettcher IFALPA 
A. Bikshapathi IBM Corporation K. J. Blake-Roberts Civil Aviation Authority D. G. Blumberg Mill-Com Electronics Corporation L. Bobber Allied Signal/Bendix King C. Bodel The Boeing Company M. I. Borgford Canadian Marconi Company R. L. Bowers Air Transport Association of America R. L. Breitwisch Rockwell International V. S. G. Brennan Civil Air Attache P. D. Britten RACAL Decca Advanced Development D. Brocard Aerospatiale L. Buckwalter Avionics Magazine A. Burgemeister B12 Associates T. Campbell INMARSAT 
J. W. Callahan Locus, Inc. 

O. Carel DNA 

| G. C. Chang    | Federal Aviation Administration    |
|----------------|------------------------------------|
| L. F. Chesto   | Aeronautical Radio, Inc.           |

J. R. Child CTA, Inc. 

K. Chong Boeing G. R. Church Aviation Management J. F. Clark Aeronautical Radio, Inc. 

B. R. Climie Consultant G. A. Cobley Collins Commercial Avionics R. A. Colton Aeronautical Radio, Inc. 

E. F. Corini Computer Technology Association Inc. 

R. J. Cox Ball Communication Systems Division D. B. Cox, Jr. 

DBC Communications, Inc. 

W. Crawford Global-Wulfsberg Systems R. E. Crenshaw Aeronautical Radio, Inc. 

G. Dail Federal Aviation Administration C. W. Davidson Sundstrand Data Control, Inc. 

B. Dawson Sundstrand Data Control. Inc. 

T. R. Degner American Airlines T. Dehel FAA Technical Center D. K. Dement Novacom, Inc. 

K. Dihle Boeing Commercial Airplane Co. 

G. Dimos Mayflower Communications Company C. R. Dobbs TPI 
W. S. Dobbs American Airlines, Inc. 

T. E. Dulin E-Systems Greenville Division P. Ebers Adsystech S. H. Evans E-Systems C. W. Everberg Federal Aviation Administration D. M. Featherstone INMARSAT 
R. E. Fenton Martin Marietta W. Ferzali Mayflower Communications Co., Inc. 

J. Filz Lufthansa German Airlines V. E. Foose Federal Aviation Administration V. Fotheringham Walter Group, Inc. 

S. G. Francisco IBM, Inc. 

F. Francy MITEC, Incorporated W. R. Fried Hughes Aircraft Company J. C. Friesz Ball Communication O. Furuta KDD 
J. Gabbay Satellite Navigation Research M. Gahan CAA Australia L. R. Ganse Trans World Airlines, Inc. 

L. J. Garcia Federal Communications Commission W. B. Garner American Mobile Satellite Corporation E. Genevieve CENA 
C. Gilbert Ball Aerospace D. H. Gorman Civil Aviation Authority 

| B. Gravante     | Mayflower Communications Co., Inc.               |
|-----------------|--------------------------------------------------|
| J. G. Griffiths | Canadian Marconi Company                         |
| G. N. Gromov    | All-Union Scientific Research Institute of Radio |

 
Equipment T. T. Guan CAA Singapore K. Hanneman Bendix/King D. R. Haapala Northwest Airlines R. M. Hambly ARINC 
N. G. Harold Federal Communications Commission C. Hartgroves Racal Avionics, Inc. 

J. Hatlelid Motorola, Inc. 

E. Henry Federal Aviation Administration R. B. Hester Douglas Aircraft Company A. Hickling PRC, Inc. 

R. Hiesler INMARSAT 
R. L. Hinkle NTIA 
R. Hobby Honeywell Communication Flight System Division M. A. Huisjen Ball Aerospace W. Hundley Wilcox Electric, Inc. 

B. T. Hung The MITRE Corporation W. Hunter Bendix King, ATAD 
L. L. James United Airlines J. Jasco IDB Aero-Nautical V. P. Jikharev All-Union Scientific Research Institute of Radio 
 
Equipment D. John INMARSAT 
G. Jones Toyocom Engineering R. Kahane Thomson-CSF 
Y. Kaminsky Federal Aviation Administration T. W. Kennedy The MITRE Corporation D. Killham Rockwell International K. H. King IATA; ARINC/SITA 
K. Kita Toyo Communication Equipment Co. Ltd. 

J. R. Knight Civil Aviation Authority A. Kohli Mayflower Communications Company R. Koll INMARSAT 
C. Korgel Martin Marietta E.F.C. LaBerge AlliedSignal R. A. LaForge Federal Communications  Commission C. L. Lane Honeywell J. V. Langley Civil Aviation Authority C. Laqui The MITRE Corporation Y. C. Lee The MITRE Corporation R. G. Lehman Honeywell, Inc. 

P. W. Lemme Boeing Commercial Airplane Group D. W. Lipke Communications Satellite Corporation J. R. Lohr RTCA, Inc. 

F. L. Lorge Federal Aviation Administration D. Luff Continental Airlines F. P. Mackowick CTA, Inc./SkyComm, Inc. 

V. Maiolla 
ARINC/SITA 

F. Makita Kukusai Denshin Denwa Company, Ltd. 

Y. Malinge Airbus Industrie M. P. Maritan Canadian Marconi Company S. Mathias Systems Control Technology Inc. 

B. Martine STNA 
E. J. Martin Edward J. Martin & Associates C. R. McCleary American Mobile Satellite Corporation K. D. McDonald SAT Tech Systems, Inc. 

T. L. McDonald Rockwell International J. D. McDonnell Douglas Aircraft company A. D. McEachen Aeronautical Radio, Inc. 

R. McIntyre Federal Communications Commission R. A. McKinlay Racal Avionics Limited E. Mega NEC Corporation E. Michaud Univ. of Colorado C. A. Miller Federal Aviation Administration S. Mohanty Aeronautical Radio, Inc. 

H. Montgomery GPS World W. Mosberg Aeronautical Radio, Inc. 

J. A. Moraes INMARSAT 
C. J. Morris MITECH 
R. D. Murad The MITRE Corporation M. Murphy Adsystech T. A. Murphy Boeing Commercial Airlines V. J. Nagowski Aeronautical Radio, Inc. 

H. Nakamura KDD America K. B. Nebbia NTIA 
J. Nemes INMARSAT 
H. J. Y. Ng Federal Communications Commission L. Norrish INMARSAT 
J. W. Nussbaum COMSAT 
O. K. Nyhus Honeywell, Inc. 

N. Oue Toyocom USA, Inc. 

J. M. Padgett Diversified International Science Corporation M. Parkes Civil Air Atttache L. W. Patak CTA, Inc. 

M. B. Perret EUROCAE 
S. N. Piasecki Racal Avionics Inc. 

R. A. Pickens AvCom, Inc., Consultant for FAA 
W. F. Pierzga COMSAT 
M. H. Pinelle SITA 
P. A. Platt Civil Aviation Authority, U.K. 

M. P. Quigley Aeronautical Radio, Inc. 

| G. F. Quinby    | G. F. Quinby Associates    |
|-----------------|----------------------------|
| C. Radcliffe    | Phase Devices Limited      |
| V. A. Rajcsok   | Aeronautical Radio, Inc.   |
| M. B. Rawas     | Beech Aircraft Corporation |
| R. G. Rayman    | Aeronautical Radio, Inc.   |

M. A. Razik E-Systems, Inc. 

E. A. Reed Federal Aviation Administration L. D. Reed Federal Communications Commission D. Reese Honeywell I. R. Reese Boeing Commercial Airplane Company A. Rehmann Federal Aviation Administration K. Reid Mobile Satellite Reports F. Richard SITA 
J. Rigley Transport Canada M. Roberts COM DEV 
M. D. Rockwell Aeronautical Radio, Inc. 

F. L. Rose Federal Communications Commission R. M. Ruana Jeppesen Sanderson, Inc. 

R. A. Rucker The MITRE Corporation B. Ruhl Honeywell W. M. Russell, III 
Air Transport Association of America P. R. Ryan Honeywell M. P. Russo Aeronautical Radio, Inc. 

P. W. Sapp Microcomputer Electronics Corporation W. C. Scales The MITRE Corporation P. Senard STNA 
J. Sengupta INMARSAT 
H. Sheppard Jet Aviation A. P. Sibold Rockwell International T. L. Signore The MITRE Corporation R. Soucy Boeing Commercial Airplane Company G. K. Smith INMARSAT 
A. L. Snively American Airlines B. P. Stapleton Boeing Commercial Airplane Company R. B. Steinacker Trans World Airlines, Inc. 

W. H. Stine, II 
National Business Aircraft Association K. Stinson Rockwell International K. Stover Delta Air Lines R. L. Striegel Air Line Pilots Association T. Studwell Aeronautical Radio, Inc. 

R. L. Swanson Federal Communications Commission W. H. Syblon American Airlines H. Takeda Civil Aviation Bureau D. J. Tangney United Air Lines, Inc. 

T. Tapsell Civil Aviation Authority T. L. Teck Singapore Aviation Academy J. C. Thornton Collins Avionics E. J. Tibbs Aeronautical Radio, Inc. 

R. W. Tibbs The MITRE Corporation R. D. Till Federal Aviation Administration Y. Toshimtsuna Electronic Industrial Association of Japan 

| T. S. Tycz    | Federal Communications Commission    |
|---------------|--------------------------------------|
| S. Urquhart   | Boeing Company                       |

A. Van Breukelen Boeing Commercial Airplanes K. van den Boogaard International Air Transport Association M. Wade Federal Aviation Administration M. C. Waller NASA 
W. C. Wanner Federal Aviation Administration M. Warfield Qantas Airways M. Warnock Delta Airlines D. Weed Federal Aviation Administration W. Weideman E-Systems, Inc. 

T. Wendel Federal Aviation Administration M. Whalen Canadian Astronautics Limited R. A. Wheeldon Boeing Commercial Airplane Company F. C. White Consultant, Honeywell G. M. White Racal Antennas, Ltd. 

C. E. Willson COM DEV 
J. A. Wilson Sundstrand Data Control M. Wolf Federal Communications Commission P. Wood Consultant, Inmarsat, COMSAT and Iridium This Page Intentionally Left Blank

## A P P E N D I X   A

# Glossary And Acronyms

 
This Page Intentionally Left Blank

 

| AAC                   | Aeronautical Administrative Communications                                 |
|-----------------------|----------------------------------------------------------------------------|
| AAS                   | Advanced Automation System                                                 |
| A-BPSK                | Aviation Binary Phase Shift Keying                                         |
| ACCC                  | Area Control Computer Complex                                              |
| ACK                   | Acknowledge Signal                                                         |
| ACKCTL                | Acknowledge Control                                                        |
| ACP                   | Audio Control Panel                                                        |
| ACSE                  | Access Control and Signaling Equipment                                     |
| ACU                   | Antenna Control Unit                                                       |
| ADM                   | Administration Identifier                                                  |
| ADS                   | Automatic Dependent Surveillance                                           |
| ADSU                  | Automatic Dependent Surveillance Unit                                      |
| ADU                   | Auxiliary Data Unit                                                        |
| AEEC                  | Airlines Electronic Engineering Committee                                  |
| AERA                  | Automated En Route Air Traffic Control                                     |
| AES                   | Aircraft Earth Station                                                     |
| AFC                   | Automatic Frequency Compensation                                           |
| AFEPS                 | ACARS Front End Processor System                                           |
| AFI                   | Authority and Format Identifier                                            |
| AGC                   | Automatic Gain Control                                                     |
| AIDS                  | Aircraft Integrated Data System                                            |
| AKA                   | Also Known As                                                              |
| ALLOC'D               | Allocated                                                                  |
| ALLOC'N               | Allocation                                                                 |
| AMBE                  | Advanced Multi-Band Excitation                                             |
| AMP                   | Audio Management Panel                                                     |
| AM/PM                 | Amplitude Modulation-to-Phase Modulation                                   |
| AMSC                  | American Mobile Satellite Corporation                                      |
| AMS(R)S               | Aeronautical Mobile Satellite (Route) Service (an ITU-defined service for  |
| spectrum allocations) |                                                                            |
| AMSS                  | Aeronautical Mobile Satellite Service                                      |
| ANCP                  | Alternate Network Control Point                                            |
| ANCT                  | Aircraft Network Control Terminal                                          |
| ANRS                  | Aeronautical Radio Navigation Service (an ITU-defined service for spectrum |
| allocations)          |                                                                            |
| AOC                   | Aeronautical Operational Control                                           |
| AOR                   | Atlantic Ocean Region                                                      |
| APC                   | Aeronautical Passenger Communications                                      |
| A-QPSK                | Aviation Quaternary Phase Shift Keying                                     |
| ARINC                 | Aeronautical Radio, Inc.                                                   |
| ARNS                  | Aeronautical Radionavigation Service (an ITU-defined service for spectrum  |
| allocations)          |                                                                            |
| ARQ                   | Automatic Repeat Request                                                   |
| ARS                   | Area Selector                                                              |
| ARSA                  | Airport Radar Service Area                                                 |
| ARTCC                 | Air Route Traffic Control Centers                                          |
| ASORRF                | Start of Aircraft Receive Reporting Frame                                  |
| ASORTCF               | Start of Aircraft Receive Terminal Control Frame                           | | ASSOC'D                                                                            | Associated                                                                    |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| ATA                                                                                | Air Transport Association                                                     |
| ATC                                                                                | Air Traffic Control                                                           |
| ATIS                                                                               | Airport Traffic Information Service                                           |
| ATN                                                                                | Aeronautical Telecommunications Network                                       |
| ATS                                                                                | Air Traffic Services                                                          |
| AWGN                                                                               | Additive White Gaussian Noise                                                 |
| Baud                                                                               | Transmission rate unit; 1/minimum time between signal transitions             |
| BAVAIL                                                                             | Flag indicating that TDMA channel reservation is available in < 8 seconds     |
| BCS                                                                                | Block Check Sum                                                               |
| BER                                                                                | Bit Error Rate                                                                |
| BI                                                                                 | Burst Interval                                                                |
| BILL                                                                               | Billing Subsystem                                                             |
| BITE                                                                               | Built-In Test Equipment                                                       |
| BL                                                                                 | Burst Length                                                                  |
| BOS                                                                                | Beginning of Slot                                                             |
| BPS                                                                                | Bits per Second                                                               |
| BPSK                                                                               | Binary Phase Shift Keying                                                     |
| BSU                                                                                | Beam Steering Unit                                                            |
| BTP                                                                                | Burst Time Plan                                                               |
| BUFFER(Q)                                                                          | Temporary buffer for messages for a given precedence (Q) value                |
| C-band                                                                             | The 4/6 GHz bands in the fixed satellite service                              |
| CCIR                                                                               | International Radio Consultative Committee                                    |
| CCITT                                                                              | International Telegraph and Telephone Consultative Committee                  |
| CCS                                                                                | Cabin Communication System                                                    |
| CDU                                                                                | Control Display Unit                                                          |
| CFDIU                                                                              | Central Fault Display Interface Unit                                          |
| CFDS                                                                               | Central Fault Display System                                                  |
| CFNO                                                                               | Current Frame Number                                                          |
| Channel Rate                                                                       | Data rate on the RF channel, fully burdened with all applicable overhead (FEC |
| encoding, dummy bits, unique word, preamble, etc.).  Expressed in bits per second. |                                                                               |
| Equal to the symbol or Baud rate with A-BPSK; equal to twice the symbol or Baud    |                                                                               |
| rate with A-QPSK.                                                                  |                                                                               |
| C/M                                                                                | Carrier to Multipath                                                          |
| CMU                                                                                | Communications Management Unit                                                |
| CNLS                                                                               | Connectionless Service                                                        |
| C/No                                                                               | Carrier-to-noise power-density ratio                                          |
| CNS                                                                                | Communication, Navigation and Surveillance                                    |
| CODEC                                                                              | Coder/Decoder                                                                 |
| COM                                                                                | Combiner (RF power)                                                           |
| CONS                                                                               | Connection-Oriented Network Service                                           |
| CONV                                                                               | Conversion                                                                    |
| CP                                                                                 | Reference number for a telephone call                                         |
| CR                                                                                 | Connection Request                                                            |
| CRC                                                                                | Cyclic Redundancy Check                                                       |
| CRF                                                                                | Connection Refused                                                            |
| CTE                                                                                | Communications Terminal Equipment                                             |
| C-to-L                                                                             | C-band to L-band                                                              | | CVSD          | Continuously Variable Slope Delta modulator             |
|---------------|---------------------------------------------------------|
| CW            | Continuous Wave                                         |
| D-bit         | Delivery Confirmation Bit                               |
| dB            | Decibels -- the logarithm of a number multiplied by ten |
| DAMA          | Demand Assigned Multiple Access                         |
| DCE           | Data Circuit-terminating Equipment/Data Comm Equipment  |
| DEA           | Delayed Echo Application                                |
| DEAP          | Delayed Echo Application Protocol                       |
| DEAPDU        | Delayed Echo Application Protocol Data Unit             |
| DECPSK        | Differentially Encoded Phase Shift Keying               |
| DFDAU         | Digital Flight Data Acquisition Units                   |
| DIP           | Diplexer                                                |
| DITS          | Digital Information Transfer system (ARINC 429)         |
| DLS           | Direct Link Service                                     |
| DMU           | Data Management Unit                                    |
| DPSK          | Differential Phase Shift Keying                         |
| DRT           | Diagnostic Rhyme Test                                   |
| DTE           | Data Terminal Equipment                                 |
| EETDN         | End-to-End Transit Delay Negotiation                    |
| EIRP          | Effective Isotropic Radiated Power                      |
| EOS           | End of Slot                                             |
| ES            | End-System                                              |
| FAA           | Federal Aviation Administration                         |
| FANS          | Future Air Navigation System                            |
| FAR           | Federal Aviation Regulations                            |
| FCC           | Federal Communications Commission                       |
| FDM           | Frequency Division Multiplex                            |
| FDMA          | Frequency Division Multiple Access                      |
| FEC           | Forward Error Correction                                |
| FID           | Format Identifier Field                                 |
| FMC           | Flight Management Computer                              |
| FP            | Frequency Plan                                          |
| FS            | Fast Select                                             |
| FSN           | Frame Sequence Number                                   |
| GDU           | Ground Data Unit                                        |
| GES           | Ground Earth Station                                    |
| GHz           | Gigahertz (1000 MHz)                                    |
| GRP           | Host-Group Identifier                                   |
| GSO           | Geo-Stationary Orbit                                    |
| G/T           | Gain/Temperature                                        |
| h (subscript) | Hexadecimal                                             |
| HF            | High Frequency                                          |
| HGA           | High Gain Antenna                                       |
| HLE           | Higher Layer Entity                                     |
| HPA           | High Power Amplifier                                    |
| HPR           | High Power Relay                                        |
| HST           | Host Identifier                                         |
| IATA          | International Air Transport Association                 | | ICAO                                                       | International Civil Aviation Organization                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------|
| ICD                                                        | International Code Designator                                                         |
| ID                                                         | Identification                                                                        |
| IDI                                                        | Initial Domain Identifier                                                             |
| IFR                                                        | Instrument Flight Rules                                                               |
| IGA                                                        | Intermediate Gain Antenna                                                             |
| IM                                                         | Intermodulation                                                                       |
| INIT                                                       | Initial/Initiate/Initialize                                                           |
| Inbound                                                    | Aircraft-to-Satellite-to-Earth Station direction                                      |
| INMARSAT                                                   | International Maritime Satellite Organization                                         |
| Instance                                                   | Each time a process is invoked, it is called an "instance" of that process.  The same |
| process may have many simultaneous, independent instances. |                                                                                       |
| INT'L                                                      | International                                                                         |
| IOR                                                        | Indian Ocean Region                                                                   |
| IRR                                                        | International Radio Regulations                                                       |
| IS                                                         | Intermediate System                                                                   |
| ISDN                                                       | Integrated Services Data Network                                                      |
| ISO                                                        | International Standardization Organization                                            |
| ISU                                                        | Initial Signal Unit                                                                   |
| ITU                                                        | International Telecommunication Union                                                 |
| IWF                                                        | Interworking Function                                                                 |
| k                                                          | Kilo (1000)                                                                           |
| K                                                          | "Binary" k (2                                                                         |
| 10                                                         |                                                                                       |
| or 1024)                                                   |                                                                                       |
| K                                                          | Kelvin -- a measure of noise temperature                                              |
| kbps                                                       | Kilobits per second                                                                   |
| LCN                                                        | Logical Channel Number                                                                |
| LGA                                                        | Low Gain Antenna                                                                      |
| LHCP                                                       | Left-Hand Circular Polarization                                                       |
| LICI                                                       | Link Interface Control Information (part of an LIDU)                                  |
| LIDU                                                       | Link Interface Data Unit (contains LICI + LSDU(s))                                    |
| LMSS                                                       | Land Mobile Satellite Service                                                         |
| LNA                                                        | Low Noise Amplifier                                                                   |
| LNRES                                                      | Long-term Next Reservation process (SDL Block TRH)                                    |
| LOC                                                        | Location Identifier                                                                   |
| LPC                                                        | Linear Predictive Coding                                                              |
| LPDU                                                       | Link Protocol Data Unit (AKA SU)                                                      |
| LRE                                                        | Low Rate Encoding                                                                     |
| LRU                                                        | Line Replaceable Unit                                                                 |
| LSB                                                        | Least Significant Bit                                                                 |
| LSDU                                                       | Link Service Data Unit (part of an LIDU; contains > one SU)                           |
| LSU                                                        | Lone Signal Unit                                                                      |
| M                                                          | More Data Bit                                                                         |
| MC                                                         | Multiple Carrier                                                                      |
| MC                                                         | Multichannel                                                                          |
| MCCP                                                       | Message Connection Control Part                                                       |
| MCDU                                                       | Multifunction (Multipurpose) Control/Display Unit                                     |
| MESS                                                       | Message                                                                               |
| MESSQ                                                      | Message with that Q value                                                             | | MESS(Q,AES)                        | Message with that Q value from that transceiver                                 |
|------------------------------------|---------------------------------------------------------------------------------|
| MHz                                | Megahertz (10                                                                   |
| 6                                  |                                                                                 |
| Hz)                                |                                                                                 |
| MMSS                               | Maritime Mobile Satellite Service (an ITU-defined service for spectrum          |
| allocations; now subsumed by MSS)) |                                                                                 |
| MODEM                              | Modulator/Demodulator                                                           |
| MOPS                               | Minimum Operational Performance Standards                                       |
| MOS                                | Mean Opinion Score                                                              |
| MP                                 | Reference Number for a message sent on P-channel                                |
| MP(Q)                              | MP for that Q value                                                             |
| MR                                 | Reference number for a message sent on R-channel                                |
| MR(Q)                              | MR for that Q value                                                             |
| MRT                                | Modified Rhyme Test                                                             |
| ms                                 | Milliseconds (10                                                                |
| -3                                 |                                                                                 |
| sec)                               |                                                                                 |
| MSB                                | Most Significant Bit                                                            |
| MSK                                | Minimum Shift Keying                                                            |
| MSS                                | Mobile Satellite Service (an ITU-defined service for spectrum allocations)      |
| MT                                 | Reference number for a message sent on a TDMA channel                           |
| MTBF                               | Mean Time Between Failures                                                      |
| MTCN                               | Minimum Throughput Class Negotiation                                            |
| MTTR                               | Mean Time to Repair                                                             |
| MUX                                | Multiplexer                                                                     |
| N                                  | Number of SUs in burst                                                          |
| NA, N/A                            | Not Available                                                                   |
|                                    | Not Applicable                                                                  |
| NAK                                | Negative Acknowledgement                                                        |
| NAKRES                             | Negative Acknowledgement signal with Reservation                                |
| NAKRES(ISU)                        | T-channel acknowledgement signal indicating error and corresponding reservation |
| NAKRES(SSU)                        | T-channel acknowledgement signal indicating specific SUs in error               |
| NAKRFC                             | T-channel signal for error SUs and delay until RES/NAKRES' arrival              |
| NAS                                | National Airspace System                                                        |
| NBFM                               | Narrow Band Frequency Modulation                                                |
| NC                                 | Network Connection                                                              |
| NCC                                | Network Control Circuit                                                         |
| NCS                                | Network Coordination Station                                                    |
| NCT                                | Network Control Terminals                                                       |
| NIC                                | New Installation Concept (ARINC 600)                                            |
| NOTAM                              | Notice to Airmen                                                                |
| NPCI                               | Network Protocol Control Information                                            |
| NPDU                               | Network Protocol Data Unit                                                      |
| NS                                 | Network Service                                                                 |
| NSAP                               | Network Service Access Point                                                    |
| NSDU                               | Network Service Data Unit                                                       |
| OALP                               | Outgoing Aeronautical Logic Procedures                                          |
| OAPSP                              | Outgoing Aeronautical Physical Signaling Procedures                             |
| OCC                                | Operations Control Center                                                       |
| Octet                              | AKA Byte; not necessarily a numeric field, but merely 8 bits                    |
| OFP                                | Operational Flight Program                                                      |
| ORT                                | Owner Requirements Table                                                        | | OSI                                                                                  | Open Systems Interconnection                                                          |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Outbound                                                                             | Earth Station-to-Satellite-to-Aircraft direction                                      |
| PABX                                                                                 | Private Automatic Branch Exchange                                                     |
| PACK                                                                                 | P-channel Acknowledge Signal                                                          |
| PACKe                                                                                | PACK indicating Specific SUs in error                                                 |
| PACKo                                                                                | PACK indicating no Error                                                              |
| PACKr                                                                                | PACK indicating Message Retransmission                                                |
| PBX                                                                                  | Private Branch Exchange (implied automatic PABX)                                      |
| PCI                                                                                  | Protocol Control Information                                                          |
| PCM                                                                                  | Pulse Code Modulation                                                                 |
| P                                                                                    |                                                                                       |
| d                                                                                    |                                                                                       |
|                                                                                      | P data channel                                                                        |
| PDN                                                                                  | Public Data Network                                                                   |
| PDU                                                                                  | Protocol Data Unit                                                                    |
| PFD                                                                                  | Power Flux Density                                                                    |
| PH                                                                                   | Packet Handler                                                                        |
| Phase 1 tests                                                                        | Laboratory tests performed with a GES simulator.                                      |
| Phase 2 tests                                                                        | Tests of an installed AES which are performed over a real satellite link with an      |
| operational GES.                                                                     |                                                                                       |
| PIAC                                                                                 | Peak Instantaneous Aircraft Count                                                     |
| PIREP                                                                                | Pilot Report                                                                          |
| PLP                                                                                  | Packet Layer Protocol                                                                 |
| PM                                                                                   | Phase Modulation                                                                      |
| PMTS                                                                                 | Packet Mode Test Suite                                                                |
| PN                                                                                   | Pseudo Noise                                                                          |
| POLREQ                                                                               | Poll Request                                                                          |
| POR                                                                                  | Pacific Ocean Region                                                                  |
| POTS                                                                                 | Plain Old Telephone Service                                                           |
| PPM                                                                                  | Parts Per Million                                                                     |
| Precedence                                                                           | An attribute of a message determining its order of service, for example, in a general |
| transmission queue.  A single message having a priority level higher than all others |                                                                                       |
| has precedence over all others for service.  The precedence of multiple messages of  |                                                                                       |
| the same priority level is first-in-first-out (FIFO).                                |                                                                                       |
| Preemption                                                                           | An action taken by the system protocols or management mechanisms to provide           |
| immediate access to system resources for certain uses.  Intra-service preemption     |                                                                                       |
| can be required for certain individual messages within a given service (e.g.,        |                                                                                       |
| AMS(R)S), in accordance with their respective priority levels as defined in that     |                                                                                       |
| service's preemption structure.  Inter-service preemption can be required among      |                                                                                       |
| services to assure that sufficient system resources are available for one or more    |                                                                                       |
| particular service (e.g., AMS(R)S).                                                  |                                                                                       |
| Priority                                                                             | The preference of one message type or category relative to others in defined          |
| circumstances.  The rank ordering of a number of message categories, each            |                                                                                       |
| assigned a unique priority level, can be used as either a precedence structure or a  |                                                                                       |
| preemption structure when contention for limited resources exists.                   |                                                                                       |
| Process                                                                              | A distinct logical structure and series of logical functions forming part of a        |
| communications protocol.  SDL diagrams describe such processes (see "Instance").     |                                                                                       |
| PSK                                                                                  | Phase Shift Keying                                                                    |
| P                                                                                    |                                                                                       |
| smc                                                                                  |                                                                                       |
|                                                                                      | P system management channel                                                           |
| PSPDN                                                                                | Public-Switched Packet Data Network                                                   | | PSTN         | Public-Switched Telephone Network                                      |
|--------------|------------------------------------------------------------------------|
| PTCPROC      | P-channel Transmit Process (Part of PQU Block)                         |
| PTP          | P-channel Transmit Process (Process in PT block)                       |
| PTT          | Post, Telegraph and Telephone (administration)                         |
| PUSH         | Store a value on a stack                                               |
| PVC          | Permanent Virtual Circuit                                              |
| Q            | Precedence value for the number of the queue used for transmission     |
| QISU         | Q value in received Initial Signal Unit                                |
| QSSU         | Q value at the top of a stack of Q values                              |
| QDU          | Quantization Degradation Unit                                          |
| QOS          | Quality of Service                                                     |
| QPSK         | Quaternary Phase Shift Keying                                          |
| QU           | Queuing Unit                                                           |
| QUEUE        | Holding buffer for SUs awaiting transmission                           |
| RACK         | R-channel acknowledge signal                                           |
| RACKe        | RACK indicating no error                                               |
| RACKr        | RACK indicating message retransmission                                 |
| RB           | Reference Burst                                                        |
| RBA          | Reference Burst A                                                      |
| RCORRECTION  | Process in block RAK to request retransmission of a message            |
| R            |                                                                        |
| d            |                                                                        |
|              | R data channel                                                         |
| REPEATREQ(Q) | Process in block PAK to request repeat of message of that Q value      |
| REQ          | Access Request signal (SUs S4A and S4B)                                |
| REQPROC      | Request Process (Block TRG)                                            |
| RES          | Reservation TDMA channel assignment signal (SU S11)                    |
| RET          | Return                                                                 |
| RF           | Radio Frequency                                                        |
| RFC          | Reservation Forthcoming signal                                         |
| RFCPROC      | Reservation Forthcoming Process (Block TRG)                            |
| RFU          | RF Unit                                                                |
| RHCP         | Right-Hand Circular Polarization                                       |
| RLS          | Reliable Link Service                                                  |
| RND(0,x)     | Random integer in the range 0 to x                                     |
| RNSS         | Radionavigation Satellite Service (an ITU-defined service for spectrum |
| allocations) |                                                                        |
| RQA          | Request for Acknowledge signal                                         |
| RQA(Q)       | RQA for that Q value                                                   |
| Rqst         | Request                                                                |
| RQU          | R-channel Queuing Unit                                                 |
| RR           | Repeat Request                                                         |
| RRC          | Root-Raised Cosine                                                     |
| RREQPROC     | R-channel Request Process (Block TRG)                                  |
| RS           | Reed Solomon (code)                                                    |
| RSCMA        | Return Sub-band C-channel Message Assembler                            |
| RSCT         | Return Sub-band C-channel Transmit (Block)                             |
| R            |                                                                        |
| smc          |                                                                        |
|              | R system management channel                                            |
| RTX          | Retransmission message, comprising ISU followed by SSU's               |
| RTX EXPECTED | Flag                                                                   | | RTXPROX(Q,GES)    | R-channel Transmit Process (Part of RQU Block)             |
|-------------------|------------------------------------------------------------|
| RTX(Q)            | RTX for a given precedence value (i.e., Q)                 |
| Rx                | Receive                                                    |
| SARPs             | Standards And Recommended Practices                        |
| SATCOM            | Satellite Communication                                    |
| SBA               | Stand-by Burst Allocation                                  |
| SCPC              | Single Channel Per Carrier                                 |
| SDL               | CCITT Specification and Description Language               |
| SDM               | System Definition Manual                                   |
| SDU               | Satellite Data Unit                                        |
| s (or sec)        | Second(s)                                                  |
| SF                | Super Frame                                                |
| SFE               | Supplier Furnished Equipment                               |
| SFN               | Starting Frame Number                                      |
| SFPROC            | Stored Reservation Synchronization Process (Block TRS)     |
| S-frame           | Super frame                                                |
| SICAS             | SSR Improvements and Collision Avoidance panel             |
| SIG               | (Telephony) Signaling Process                              |
| Slot Synchron     | Timing pulse/signal for start of TDMA channel slot (~8 ms) |
| SMC               | System Management and Communication                        |
| SN                | Subnetwork                                                 |
| SNAcP             | Subnetwork Access Protocol                                 |
| SNC               | Subnetwork Connection                                      |
| SNDC              | Subnetwork Dependent Convergence                           |
| SNICP             | Subnetwork Independent Convergence Protocol                |
| SNPA              | Subnetwork Point of Attachment                             |
| SNPDU             | Subnetwork Protocol Data Unit                              |
| SNRES             | Short-term Next Reservation process (Block TRH)            |
| SOATRF            | Start of Aircraft Transmit Reporting Frame                 |
| SOATTCF           | Start of Aircraft Transmit Terminal Control Frame          |
| SOITDF            | Start of Inbound Transmit Data Frame                       |
| SOITMF            | Start of Inbound Transmit Master Frame                     |
| SORDF             | Start of Receive Data Frame                                |
| SORMF             | Start of Receive Master Frame                              |
| SORSF             | Start of the Receive Super Frame                           |
| SOTSF             | Start of Transmit Super Frame                              |
| SPITE             | Switching Processing Interface Telephony Event             |
| SPL               | Splitter (RF power)                                        |
| SR                | Symbol Rate                                                |
| SSN               | Satellite Subnetwork                                       |
| SSNAc             | Satellite Subnetwork Access                                |
| SNIW              | Sub-Network Inter-Working                                  |
| SSND              | Satellite Subnetwork Dependent                             |
| SSNIW             | Satellite Subnetwork Interworking                          |
| SSNL              | Satellite Subnetwork Layer                                 |
| SSU               | Subsequent Signal Unit                                     |
| Stack             | Last-in, first-out holding buffer                          |
| SU                | Signal Unit                                                |
| SUT            | System Under Test                                            |
|----------------|--------------------------------------------------------------|
| SVC            | Switched Virtual Circuit                                     |
| TACK           | T-channel Acknowledge signal indicating no errors (SU S16C)  |
| TAK            | T-channel Acknowledge                                        |
| TBA            | To Be Announced                                              |
| TBC            | To Be Confirmed                                              |
| TBD            | To Be Defined or Determined                                  |
| TCC            | Terminal Control Circuit                                     |
| TCCCs          | Tower Control Computer Complexes                             |
| TCM            | T-Channel Manager                                            |
| TCN            | Throughput Class Negotiation                                 |
| TCORRECTION    | Q Process for RLS message supervision (Block TAK)            |
| TDM            | Time Division Multiplex                                      |
| TDMA           | Time Division Multiple Access                                |
| TDSAI          | Transit Delay Selection And Indication                       |
| TLV            | Type/Length/Value                                            |
| TMA            | T-channel Message Assembler                                  |
| TPS            | Transport Protocol Selector                                  |
| TQU            | T-channel Queuing Unit                                       |
| TREQPROC       | T-channel Request Process (Block TRG)                        |
| TRG            | T-channel Request Generator                                  |
| TRH            | T-channel Reservation Handler                                |
| TRS            | TDMA Reservation Synchronizer (Block and Process)            |
| TT&C           | Tracking Telemetry and Command                               |
| TTXPROC        | TDMA Channel Transmission Process (Block TQU)                |
| TUP            | Telephone User Part of CCITT Signaling System No. 7          |
| Tx             | Transmit                                                     |
| TXMESSAGE      | Temporary buffer for message to be transmitted               |
| TXMESSAGE      | Signal containing contents of the TXMESSAGE Buffer           |
| TXSU(N)        | Process for transmission of a burst of N SUs (Block TTP)     |
| UD             | User Data                                                    |
| UP             | User Data Process (network layer)                            |
| UW             | Unique Word                                                  |
| VFR            | Visual Flight Rules                                          |
| VHF            | Very High Frequency                                          |
| Vocoder        | Voice Coder/Decoder (sometimes referred to as "voice codec") |
| VSWR           | Voltage Standing Wave Ratio                                  |
| W              | Watts                                                        |
| W/             | With                                                         |
| WARC           | World Administrative Radio Conference (now replaced by WRC)  |
| WRC            | World Radio Conference                                       |
| XCVR           | Transceiver                                                  |
| Xmsn           | Transmission                                                 |
| XMT            | Transmit                                                     |
| Z              |                                                              |
| k              |                                                              |
|                | Randomization index for the k                                |
| th             |                                                              |
| repeat attempt |                                                              |
| Z              |                                                              |
| 0              |                                                              |
|                | Initial value of Z                                           |
| k              |                                                              |
|                |                                                              |

 
This Page Intentionally Left Blank

 
# Aes G/T Derivations

This Page Intentionally Left Blank

## Aes G/T Derivations

 
 
This appendix defines the antenna gain and the various antenna, installation, and receiver noise contributions necessary to satisfy the overall AES G/T (Gain-to-Temperature) requirements stated in Section 2.2.2.1, and supports the test procedure in Section 3.4.6.2. 

The defined point of separation between the Antenna Subsystem and the Transceiver Subsystem is the single RF port of the antenna.  The noise contributions after the Antenna Subsystem will therefore be from: 

 
(1) The RF cable connecting the antenna to the receiver, with 0.3 dB maximum loss, as 
defined in Section 2.2.2.1, item h. 
(2) The transceiver's low-noise amplifier (LNA), where the receiver sensitivity as defined 
in Section 2.2.4.1.2 is dependent on an equivalent noise temperature of 153 K at an ambient temperature of 298 K, i.e., a noise figure of 1.8 dB. 
(3) Elements in a practical system after the receiver LNA; for example, a system where 
an LNA with a 1.8 dB maximum noise figure and 53 dB minimum gain is followed by a cable with 25 dB maximum loss and an RFU maximum noise figure of 10 dB, as illustrated in Figure B-1. 
 
 * ┌───────────┐ * ┌──────┐  ┌──────────────┐   ┌─────────┐  ┌────────────┐ │  Antenna  ├─*─│Cable ├──┤  Diplxr/LNA  ├───┤  Cable  ├──┤  Receiver  │ │ Subsystem │ * │<0.3dB│  │ NF < 1.8 dB  │   │ < 25dB  │  │ NF < 10 dB │ │           │ * │      │  │ Gain > 53 dB │   │         │  │            │ └───────────┘ * └──────┘  └──────────────┘   └─────────┘  └────────────┘ * *  < -----------  Transceiver Subsystem  ---------------> * 

## Figure B-1.  An Example Of An Aes Receive Chain

 
The noise contributions of (3), using Friis's formula for noise from cascaded stages, can be shown to increase the noise figure of the receiver from 1.80 to 1.85 dB. 

 
The overall AES G/T will therefore be: 
$$(\frac{G}{T})_{AES}=\frac{G_{A}}{T_{A}+T_{O}(\;L_{I}\;^{*}\;F_{B}\;-\;1)}$$. 
 
where: 
 
GA is the gain of the antenna at the single RF port, 
 
 
TA is the noise temperature of the antenna at the single RF port, 


T0 is the system reference temperature (nominally 290 K per Section 2.2.2.1.d), 
 
LI is the numerical insertion loss of the interconnecting cable per (1) above, taken as 
0.3 dB, or 1.07152, and 
 
FR is the worst-case noise figure, 1.85 dB or 1.53109. 
 
The expression T0(LI*FR - 1) is the overall noise contribution of the Transceiver Subsystem at the single RF port of the antenna. 

 
Substituting the above values, 
$T_{0}(L_{1}\,^{*}\,F_{R}\,-\,1)=290(1.07152\,^{*}\,1.53109\,-\,1)$

$=185.77$ K 
 
Thus: 
$$(\frac{G}{T})_{AES}=\frac{G_{A}}{T_{A}+185.77}$$. 
 
From Section 2.2.2.1, an AES using a low-gain antenna must meet G/T = -26 dB-K-1, or a numerical value of 0.0025118. 

 
This is satisfied when: 
$$\frac{G_{A}}{T_{A}+I85.77}\geq0.0025118$$. 
 
Thus, 
$T_{A(LGA)}$ = 398.12 $\ast$ 6${}_{A}$ - 185.77
 
or, where GA from Section 2.4.3.3.1.2 is in dB, 

$T_{A(LGA)}\leq398.12\,\,\,\,10\,\,\,\,\,\,10\,\,\,\,\,\,10\,\,\,\,\,\,185.77$
 
Similarly, an AES using a high-gain antenna must meet G/T = -13 dB/K, or a numerical value of 0.050118.  This is satisfied when: 

$$\frac{G_A}{T_A+185.77}\geq0.050118$$. 
Thus: 

$T_{\rm{A}({\rm{R}}{\rm{A}})}$ = 19.953 ${}^{\star}$ = 185.77

${}^{\star}$ = 19.953 ${}^{\star}$ = 185.77
 
or, where GA from Section 2.4.3.3.1.1 is in dB: 

$T_{A(HGA)}\leq19.953\cdot10^{\frac{G_{A}(dB)}{10}}$ - 185.77
 
This Page Intentionally Left Blank 

# A P P E N D I X   C Index Correlating Requirements And Verification Procedures

 
This Page Intentionally Left Blank

## Index Correlating Requirements And Verification Procedures

 This index correlates each numbered performance requirement section (2.2.x) with its corresponding verification requirements/procedures section(s) (2.4.y or other).  The absence of entries in some rows of the Verification column indicates that there is no verification requirement/procedure specified for the corresponding performance requirement.  It is intended that these absent verification requirements/- procedures be included (and indexed) in a future revision to this MOPS. 

 

| PERFORMANCE    | VERIFICATION                                      |
|----------------|---------------------------------------------------|
| 2.2            | Introductory                                      |
| 2.2.1          | 2.4.7.5, 2.4.7.5.1, 2.4.7.5.2, 2.4.7.5.3, 2.4.8.1 |
| 2.2.2          | 2.4.8.1                                           |
| 2.2.2.1        | 2.4.3.3.1.3, 2.4.8.1                              |
| 2.2.3          | Introductory                                      |
| 2.2.3.1        | Definition                                        |
| 2.2.3.1.1      | Definition                                        |
| 2.2.3.1.2      | 2.4.3.3.1.1, 2.4.3.3.1.2                          |
| 2.2.3.2        | 2.4.3.3.1                                         |
| 2.2.3.2.1      | 2.4.3.3.1.1                                       |
| 2.2.3.2.2      | 2.4.3.3.1.2                                       |
| 2.2.3.2.3      | 2.4.3.3.1.1                                       |
| 2.2.3.3        | 2.4.3.3.2                                         |
| 2.2.3.3.1      | 2.4.3.3.2.1                                       |
| 2.2.3.3.2      | 2.4.3.3.2.2                                       |
| 2.2.3.4        | Title Only                                        |
| 2.2.3.4.1      | 2.4.3.3.3                                         |
| 2.2.3.4.2      | Title Only                                        |
| 2.2.3.4.2.1    | 2.4.3.3.3                                         |
| 2.2.3.4.2.2    | 2.4.3.3.3                                         |
| 2.2.3.5        | 2.4.3.3.4                                         |
| 2.2.3.6        | Title Only                                        |
| 2.2.3.6.1      | 2.4.3.3.5                                         |
| 2.2.3.6.2      | 2.4.3.3.5                                         |
| 2.2.3.7        | 2.4.3.3.6                                         |
| 2.2.3.8        | 2.4.3.3.7                                         |
| 2.2.3.9        | 2.4.3.3.8                                         |
| 2.2.3.10       | 2.4.3.3.9                                         |
| 2.2.3.11       | 2.4.3.3.10                                        |
| 2.2.3.12       | 2.4.3.3.11                                        |
| 2.2.3.13       | 2.4.3.3.12                                        |
| 2.2.4          | 2.4.4                                             |
| 2.2.4.1        | Definition                                        |
| 2.2.4.1.1      | Definition                                        |
| 2.2.4.1.2      | 2.4.4.2.1, 2.4.4.2.2                              |
| 2.2.4.1.2.1    | 2.4.4.2.2                                         |
| PERFORMANCE              | VERIFICATION                                                     |
|--------------------------|------------------------------------------------------------------|
| 2.2.4.1.2.2              | 2.4.4.2.2                                                        |
| 2.2.4.1.2.3              | 2.4.4.2.2                                                        |
| 2.2.4.1.2.4              | 2.4.4.2.2                                                        |
| 2.2.4.1.3                | 2.4.4.2.3                                                        |
| 2.2.4.1.4                | 2.4.4.2.3                                                        |
| 2.2.4.1.5                | 2.4.4.2.4                                                        |
| 2.2.4.1.6                | 2.4.4.2.5                                                        |
| 2.2.4.1.7                | 2.4.4.2.6                                                        |
| 2.2.4.1.7.1              | 2.4.4.2.6                                                        |
| 2.2.4.1.7.2              | 2.4.4.2.6                                                        |
| 2.2.4.1.8                | 2.4.4.2.7                                                        |
| 2.2.4.1.9                | 2.4.4.2.7                                                        |
| 2.2.4.1.10               | 2.4.4.2.8                                                        |
| 2.2.4.1.11 - A - 3.1     | Title Only                                                       |
| 2.2.4.1.11 - A - 3.3.1   | (2.4.4.2.2) *                                                    |
| 2.2.4.1.11 - A - 3.3.1.1 | (2.4.4.2.2) *                                                    |
| 2.2.4.1.11 - A - 3.3.1.2 | (2.4.4.2.2) *                                                    |
| 2.2.4.1.11 - A - 3.4     | (2.4.4.2.2) *                                                    |
| 2.2.4.1.11.1             | 2.4.4.2.8                                                        |
| 2.2.4.1.11.2             | 2.4.4.2.9                                                        |
| 2.2.4.1.12 - A - 3.1     | Title Only                                                       |
| 2.2.4.1.12 - A - 3.2     | (2.4.4.2.2) *                                                    |
| 2.2.4.1.12 - A - 3.2.1   | (2.4.4.2.2) *                                                    |
| 2.2.4.1.12 - A - 3.2.2   | (2.4.4.2.2) *                                                    |
| 2.2.4.1.12 - A - 3.2.3   | (2.4.4.2.2) *                                                    |
| 2.2.4.1.12 - A - 3.3.4   | (2.4.4.2.2) *                                                    |
| 2.2.4.1.12 - A - 3.2.5   | (2.4.4.2.2) *                                                    |
|                          | * NOTE:  There are no individual tests that directly verify that |

the AES receiver has correctly implemented the 
specified P-Channel or C-Channel format.  However, 
it would be impossible to have implemented it 
incorrectly, and still achieve an acceptable post-
Viterbi BER performance using a proper GES 
emulator.  For that reason, 2.4.4.2.2 is listed as the 
corresponding verification section.  The verification 
section number is shown in parentheses to indicate 
that the verification is accomplished indirectly. 

| 2.2.4.1.12 - A - 3.2.6    | 2.4.8 Table 2-20    |
|---------------------------|---------------------|
| 2.2.4.1.12 - A - 3.2.7    | (2.4.4.2.12)        |
| 2.2.4.1.12 - A - 3.4      | (2.4.4.2.2)         |
| 2.2.4.1.12.1              | Title Only          |
| 2.2.4.1.12.1.1            | 2.4.4.2.10          |
| 2.2.4.1.12.2              | 2.4.4.2.11          |
| 2.2.4.1.12.3              | 2.4.4.2.12          |

 RTCA, Inc. 2000 

| PERFORMANCE                    | VERIFICATION    |
|--------------------------------|-----------------|
| 2.2.4.1.12.4                   | 2.4.4.2.13      |
| 2.2.4.1.12.5                   | 2.4.4.2.14      |
| 2.2.4.2                        | Definition      |
| 2.2.4.2.1                      | 2.4.4.3.1       |
| 2.2.4.2.2                      | 2.4.4.3.2       |
| 2.2.4.2.3                      | 2.4.4.3.3       |
| 2.2.4.2.4                      |                 |
| 2.4.4.3.4                      |                 |
| 2.2.4.2.5                      | 2.4.4.3.5       |
| 2.2.4.2.6                      | 2.4.4.3.6       |
| 2.2.4.2.7                      | 2.4.4.3.7       |
| 2.2.4.2.8                      | 2.4.4.3.8       |
| 2.2.4.2.9                      | 2.4.4.3.9       |
| 2.2.4.2.10                     | 2.4.4.3.10      |
| 2.2.4.2.10.1                   | 2.4.4.3.10      |
| 2.2.4.2.10.2                   | 2.4.4.3.10      |
| 2.2.4.2.11                     | 2.4.4.3.11      |
| 2.2.4.2.12                     | 2.4.4.3.12      |
| 2.2.4.2.13                     | 2.4.4.3.13      |
| 2.2.4.2.14                     | 2.4.4.3.14      |
| 2.2.4.2.15                     | 2.4.4.3.15      |
| 2.2.4.2.16                     | 2.4.4.3.16      |
| 2.2.4.2.17 - A - 3.1           | Title Only      |
| 2.2.4.2.17 - A - 3.3.2         |                 |
| 2.2.4.2.17 - A - 3.3.2.1       |                 |
| 2.2.4.2.17 - A - 3.3.2.2       |                 |
| 2.2.4.2.17 - A - 3.3.2.3       |                 |
| 2.2.4.2.17 - A - 3.3.2.4       |                 |
| 2.2.4.2.17 - A - 3.4           |                 |
| 2.2.4.2.17 - A - A6 Fig. AP6-1 |                 |
| 2.2.4.2.17 - A - A6 Fig. AP6-2 |                 |
| 2.2.4.2.17 - B - 4.2.3.1       |                 |
| 2.2.4.2.17 - B - 4.2.3.2       |                 |
| 2.2.4.2.17.1                   | 2.4.4.3.17      |
| 2.2.4.2.18                     |                 |
| 2.2.4.2.18.1                   | 2.4.4.3.17      |
| 2.2.5 General                  | 2.4.5 General   |
| 2.2.5 - A - 4.1                |                 |
| 2.4.5 Table 2-17               |                 |
| /                              |                 |
| 1                              |                 |
| 2.2.5 - A - 4.2                |                 |
| 2.4.5 Table 2-17               |                 |
| /                              |                 |
| 1                              |                 |
| 2.2.5 - A - 4.3                |                 |
| 2.4.5 Table 2-17               |                 |
| /                              |                 |
| 1                              |                 |
| 2.2.5 - A - 4.3.1              |                 |
| 2.4.5 Table 2-17               |                 |
| /                              |                 |
| 1                              |                 |
| 2.2.5 - A - 4.3.2              |                 |
| 2.4.5 Table 2-17               |                 |
| /                              |                 |
| 1                              |                 |
| 2.2.5 - A - 4.3.3              |                 |
| 2.4.5 Table 2-17               |                 |
| /                              |                 |
| 1                              |                 |
| PERFORMANCE                                        | VERIFICATION               |
|----------------------------------------------------|----------------------------|
| 2.2.5 - A - 4.3.4                                  |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - A - 4.3.5                                  |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - A - 4.3.6                                  |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - A - S0 through S37                         |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1, 2.4.6 Table 2-18, 2.4.7 Table 2-19, 2.4.8 Table |                            |
| 2-20                                               |                            |
| 2.2.5 - A - Annex 1                                |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1, 2.4.6 Table 2-18, 2.4.7 Table 2-19, 2.4.8 Table |                            |
| 2-20                                               |                            |
| 2.2.5 - A - Annex 2                                |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1, 2.4.6 Table 2-18, 2.4.7 Table 2-19, 2.4.8 Table |                            |
| 2-20                                               |                            |
| 2.2.5 - B - 6.1                                    |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - B - 6.2                                    |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - B - 6.3.1                                  |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - B - 6.3.2                                  |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - B - 6.4                                    |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - B - 6.5                                    |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - B - 6.5.1                                  | 2.4.6 Table 2-18           |
| 2.2.5 - B - 6.5.2                                  |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - B - 6.5.3                                  |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - B - 6.6                                    |                            |
| 2.4.5 Table 2-17                                   |                            |
| /                                                  |                            |
| 1                                                  |                            |
| 2.2.5 - B - Annex 1 Table CR4.1                    | 2.4.5 Table 2-17/1         |
| 2.2.6 General                                      | 2.4.6 General              |
| 2.2.6 - A - 5.1                                    | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2                                    | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.2                                  | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.3                                  | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.4                                  | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.5                                  | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.6                                  | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.7                                  | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.8                                  | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.9                                  | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.10                                 | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.11                                 | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.11.1                               | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.11.2                               | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.13.3                               | 2.4.6                      |
| 2.2.6 - A - 5.2.14                                 | 2.4.6                      |
| 2.2.6 - A - 5.2.15                                 | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.17                                 | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.2.18                                 | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.3                                    | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.3.1                                  | 2.4.6 Table 2-18           |
| 2.2.6 - A - 5.3.2                                  | 2.4.6. Table 2-18, 2.4.6.1 |
| PERFORMANCE             | VERIFICATION                              |
|-------------------------|-------------------------------------------|
| 2.2.6 - A - 5.3.3       | 2.4.6. Table 2-18, 2.4.6.2                |
| 2.2.6 - A - 5.3.4       | 2.4.6 Table 2-18                          |
| 2.2.6 - A - 5.3.4.1     | 2.4.6 Table 2-18                          |
| 2.2.6 - A - 5.5         | Introductory                              |
| 2.2.6 - A - 5.5.1       | 2.4.6 Table 2-18                          |
| 2.2.6 - A - 5.5.2       | 2.4.6 Table 2-18                          |
| 2.2.6 - A - 5.5.3       | 2.4.6 Table 2-18                          |
| 2.2.6 - A - 5.5.4       | 2.4.6 Table 2-18                          |
| 2.2.6 - A - 5.6         | 2.4.6 Table 2-18                          |
| 2.2.6 - A - 5.6.1       | 2.4.6 Table 2-18                          |
| 2.2.6 - A - 5.6.2       | 2.4.6 Table 2-18                          |
| 2.2.6 - A - 5.6.3       | 2.4.6 Table 2-18                          |
| 2.2.6 - B - 7.3         | 2.4.6 Table 2-18                          |
| 2.2.6 - B - 7.3.1       |                                           |
| 2.2.6 - B - 7.3.3       |                                           |
| 2.2.6 - B - 7.4         | 2.4.6 Table 2-18                          |
| 2.2.6 - B - 7.4.1       | 2.4.6 Table 2-18 (Buffer size NOT tested) |
| 2.2.6 - B - 7.4.2       | 2.4.6 Table 2-18 (Buffer size NOT tested) |
| 2.2.6 - B - 7.4.3       | 2.4.6 Table 2-18 (Buffer size NOT tested) |
| 2.2.7 General           | 2.4.7 General                             |
| 2.2.7.1                 | 2.4.7.1                                   |
| 2.2.7.2                 | 2.4.7.2                                   |
| 2.2.7.3                 | 2.4.5, 2.4.7.3.3.5                        |
| 2.2.7.4                 | Introductory                              |
| 2.2.7.4.1 - A - 7.1.1   | 2.4.7 Table 2-19, 2.4.5 Table 2-17/2      |
| 2.2.7.4.1 - A - 7.1.2   | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2     | Title Only                                |
| 2.2.7.4.1 - A - 7.2.1   | Title Only                                |
| 2.2.7.4.1 - A - 7.2.1.1 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.1.2 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.1.3 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.1.4 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.1.5 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.1.6 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.1.7 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.2   | Title Only                                |
| 2.2.7.4.1 - A - 7.2.2.1 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.2.2 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.2.3 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.2.4 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.2.5 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.2.6 | 2.4.5 Table 2-17/2                        |
| 2.2.7.4.1 - A - 7.2.3   | Title Only                                | | PERFORMANCE               | VERIFICATION       |
|---------------------------|--------------------|
| 2.2.7.4.1 - A - 7.2.3.1   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.3.2   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.3.3   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.3.4   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.3.5   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.3.6   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.4     | Title Only         |
| 2.2.7.4.1 - A - 7.2.4.1   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.4.1.1 | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.4.1.2 | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.4.1.3 | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.4.1.4 | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.4.1.5 | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.4.2   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - 7.2.5     | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-1      | Introductory       |
| 2.2.7.4.1 - A - A3-2      | Introductory       |
| 2.2.7.4.1 - A - A3-3      | Introductory       |
| 2.2.7.4.1 - A - A3-3.1    | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-3.1.1  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-3.1.2  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-3.2    | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-3.2.1  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-3.2.2  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-3.2.3  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-4      | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-4.1    | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-4.1.1  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-4.1.2  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-4.1.3  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-4.1.4  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-4.1.5  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-4.2    | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - A - A3-4.2.1  | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - B - 9.3.2     | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - B - 9.4.1.1   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - B - 9.4.1.2   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - B - 9.4.1.3   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.1 - B - 9.5.1     | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.1       | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.1.1     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.1.2     | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.1.3     | 2.4.7 Table 2-19   | | PERFORMANCE               | VERIFICATION       |
|---------------------------|--------------------|
| 2.2.7.4.2 - A - 7.1.4     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.1.4.1   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.1.5     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.1.6     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.1.7     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.2       | Title Only         |
| 2.2.7.4.2 - A - 7.2.1     | Title Only         |
| 2.2.7.4.2 - A - 7.2.1.1   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.1.2   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.1.3   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.1.4   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.1.5   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.1.6   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.1.7   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.2     | Title Only         |
| 2.2.7.4.2 - A - 7.2.2.1   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.2.2   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.2.3   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.2.4   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.2.5   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.2.6   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.3     | Title Only         |
| 2.2.7.4.2 - A - 7.2.3.1   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.3.2   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.3.3   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.3.4   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.3.5   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.3.6   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.4     | Title Only         |
| 2.2.7.4.2 - A - 7.2.4.1   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.4.1.1 | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.4.1.2 | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.4.1.3 | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.4.1.4 | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.4.1.5 | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.4.2   | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - 7.2.5     |                    |
| 2.2.7.4.2 - A - 7.3       | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.1     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.1.1   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.1.2   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.2     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.2.1   | 2.4.7 Table 2-19   | | PERFORMANCE                 | VERIFICATION       |
|-----------------------------|--------------------|
| 2.2.7.4.2 - A - 7.3.2.2     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.2.3     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.3       | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.3.1     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.3.3     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.3.4     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.3.4.1   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.3.4.2   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.4       | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.4.1     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.4.2     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.5       | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.5.1     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.5.1.1   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.5.1.2   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.5.1.2.1 | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.5.1.2.2 | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.5.1.3   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6       | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.1     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.2     | Title Only         |
| 2.2.7.4.2 - A - 7.3.6.2.1   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.2.2   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.2.3   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.3     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.3.1   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.3.2   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.4     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.5     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.6     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.7     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.7.1   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.7.2   | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.8     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.9     | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.10    | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - 7.3.6.11    | 2.4.7 Table 2-19   |
| 2.2.7.4.2 - A - A3-1        | Introductory       |
| 2.2.7.4.2 - A - A3-2        | Introductory       |
| 2.2.7.4.2 - A - A3-3        | Introductory       |
| 2.2.7.4.2 - A - A3-3.1      | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - A3-3.1.1    | 2.4.5 Table 2-17/2 |
| 2.2.7.4.2 - A - A3-3.1.2    | 2.4.5 Table 2-17/2 |
| PERFORMANCE                                                    | VERIFICATION                             |
|----------------------------------------------------------------|------------------------------------------|
| 2.2.7.4.2 - A - A3-3.2                                         | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-3.2.1                                       | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-3.2.2                                       | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-3.2.3                                       | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-4                                           | Introductory                             |
| 2.2.7.4.2 - A - A3-4.1                                         | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-4.1.1                                       | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-4.1.2                                       | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-4.1.3                                       | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-4.1.4                                       | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-4.1.5                                       | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-4.2                                         | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A3-4.2.1                                       | 2.4.5 Table 2-17/2                       |
| 2.2.7.4.2 - A - A7-1.1                                         | Introductory                             |
| 2.2.7.4.2 - A - A7-1.2                                         | Introductory                             |
| 2.2.7.4.2 - A - A7-1.3                                         | 2.4.7 Table 2-19                         |
| 2.2.7.4.2 - A - A7-1.4                                         | Title Only                               |
| 2.2.7.4.2 - A - A7-1.4.1                                       | Title Only                               |
| 2.2.7.4.2 - A - A7-1.4.1.1                                     | 2.4.7 Table 2-19                         |
| 2.2.7.4.2 - A - A7-1.4.1.2                                     | Definition                               |
| 2.2.7.4.2 - A - A7-1.4.2                                       | 2.4.7 Table 2-19                         |
| 2.2.7.4.2 - A - A7-1.5                                         | Definition                               |
| Performance factors are tested throughout 2.4.7 Table 2-19 and |                                          |
| Section 2.4.7.3                                                |                                          |
| 2.2.7.4.2 - A - A10 (all paragraphs                            |                                          |
| and including Tables 1, 2.1, 2.2 and                           |                                          |
| Figure 1)                                                      |                                          |
| 2.2.7.4.2 - B - 9.3                                            | 2.4.7 Table 2-19                         |
| 2.2.7.4.2 - B - 9.3.1                                          | 2.4.7 Table 2-19                         |
| 2.2.7.4.2 - B - 9.3.2                                          | Introductory                             |
| 2.2.7.4.2 - B - 9.4                                            | 2.4.7 Table 2-19                         |
| 2.2.7.4.2 - B - 9.4.1                                          | Title Only                               |
| 2.2.7.4.2 - B - 9.4.1.1                                        | 2.4.7 Table 2-19                         |
| 2.2.7.4.2 - B - 9.4.1.2                                        | 2.4.7 Table 2-19                         |
| 2.2.7.4.2 - B - 9.4.1.3                                        | 2.4.7 Table 2-19                         |
| 2.2.7.4.2 - B - 9.5.1                                          | 2.4.7 Table 2-19                         |
| 2.2.7.4.2 - B - 9.5.2                                          | 2.4.7 Table 2-19 (Only partially tested) |
| 2.2.7.5                                                        | Introductory                             |
| 2.2.7.5.1                                                      | 2.4.7.3                                  |
| 2.2.7.5.2                                                      | Title Only                               |
| 2.2.7.5.2.1                                                    | Tested throughout 2.4.7                  |
| 2.2.7.5.2.2                                                    | Title Only                               |
| 2.2.7.5.2.3                                                    | 2.4.7.3.1.1                              |
| 2.2.7.5.2.3.1 Table 2-2                                        |                                          |
| 2.4.7.3.1.1, 2.4.7.3.1.2                                       |                                          |
| ,                                                              |                                          |
| 2.4.7.3.4.1, 2.4.7.3.4.2, 2.4.7.3.4.3                          |                                          |
| 2.2.7.5.2.3.1 Table 2-3                                        | 2.4.7.3.1.1, 2.4.7.3.1.2                 |
| PERFORMANCE              | VERIFICATION                               |
|--------------------------|--------------------------------------------|
| 2.2.7.5.2.3.1 Table 2-4  | 2.4.7.3.1.1, 2.4.7.3.1.2                   |
| 2.2.7.5.2.3.1 Table 2-5  | 2.4.7.3.1.1,                               |
| 2.4.7.3.4.6              |                                            |
| 2.2.7.5.2.3.1 Table 2-6  | 2.4.7.3.1.1, 2.4.7.3.1.2, 2.4.7.3.4.4      |
| 2.2.7.5.2.3.1 Table 2-7  | 2.4.7.3.1.1, 2.4.7.3.1.2                   |
| 2.2.7.5.2.3.1 Table 2-8  | 2.4.7.3.1.1, 2.4.7.3.1.2, 2.4.7.3.4.5      |
| 2.2.7.5.2.3.1 Table 2-9  | Reserved Table                             |
| 2.2.7.5.2.3.1 Table 2-10 | Reserved Table                             |
| 2.2.7.5.2.3.1 Table 2-11 | Reserved Table                             |
| 2.2.7.5.2.3.1 Table 2-12 | Reserved Table                             |
| 2.2.7.5.2.3.2            |                                            |
| 2.2.7.5.2.3.3            |                                            |
| 2.2.7.5.2.3.4 Table 2-13 | 2.4.7.3.5, 2.4.7.3.5.1 through 2.4.7.3.5.4 |
| 2.2.7.5.3                | 2.4.7.4                                    |
| 2.2.8 General            | 2.4.8 General                              |
| 2.2.8 - A - 6            | Title Only                                 |
| 2.2.8 - A - 6.1          | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.1.1        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.1.3        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.1.4        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.1.6        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.3          | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.4          | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.5          | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.5.1        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.5.2        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.5.2.1      | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.5.2.2      | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.5.2.3      | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.5.2.4      | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.5.2.5      | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.5.3        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.5.5        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.6          | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.6.1        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.6.2        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.6.2.1      | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.6.2.2      | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.6.4        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.7          | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.7.1        |                                            |
| 2.2.8 - A - 6.7.2        | 2.4.8 Table 2-20                           |
| 2.2.8 - A - 6.7.5        | 2.4.8 Table 2-20                           |
| PERFORMANCE                            | VERIFICATION                                   |
|----------------------------------------|------------------------------------------------|
| 2.2.8 - A - 6.8                        | 2.4.8 Table 2-20                               |
| 2.2.8 - A - 6.9                        | 2.4.8 Table 2-20                               |
| 2.2.8 - A - 6.9.1                      | 2.4.8 Table 2-20                               |
| 2.2.8 - A - 6.9.1.1                    | 2.4.8 Table 2-20                               |
| 2.2.8 - A - 6.9.1.3                    | 2.4.8 Table 2-20                               |
| 2.2.8 - A - A5-1                       | Introductory                                   |
| 2.2.8 - A - A5-2                       | Title Only                                     |
| 2.2.8 - A - A5-2.1                     | 2.4.8 Table 2-20                               |
| 2.2.8 - A - A5-2.2                     | Reference only                                 |
| 2.2.8 - A - A5-2.3                     | Reference only                                 |
| 2.2.8 - A - A5-3                       | Reference only                                 |
| 2.2.8 - A - A5-4                       | Reference only                                 |
| 2.2.8 - B - 10.2.1                     | 2.4.8 Table 2-20                               |
| 2.2.8 - B - Annex 1 Table CR5.1        | 2.4.8 Table 2-20                               |
| 2.2.8 - B - 10.3.1                     | 2.4.8 Table 2-20                               |
| 2.2.8 - B - 10.4.1                     | 2.4.8 Table 2-20                               |
| 2.2.8 - B - 10.4.2                     | 2.4.8 Table 2-20                               |
| 2.2.8 - B - 10.4.3                     | 2.4.8 Table 2-20                               |
| 2.2.8 - B - 10.4.4                     | 2.4.8 Table 2-20                               |
| 2.2.8 - B - 10.4.5                     |                                                |
| 2.2.8 - B - 10.5                       |                                                |
| 2.2.8 - B - 12.2.1                     | 2.4.8 Table 2-21                               |
| 2.2.8 - B - 12.2.2                     | 2.4.8 Table 2-21                               |
| 2.2.8 - B - 12.2.3                     | 2.4.8 Table 2-21                               |
| 2.2.8 - B - 12.2.4                     | 2.4.8 Table 2-21                               |
| 2.2.8 - B - 12.3.1                     | 2.4.8 Table 2-21                               |
| 2.2.8 - B - 12.3.2.1                   | 2.4.8 Table 2-21                               |
| 2.2.8 - B - 12.3.2.2                   | 2.4.8 Table 2-21                               |
| 2.2.8 - B - 12.3.3                     | 2.4.8 Table 2-21                               |
| 2.2.8 - B - 12.3.4                     | 2.4.8 Table 2-21                               |
| 2.2.8 - B - 12.3.5                     | 2.4.8 Table 2-21                               |
| 2.2.8 - B - A2 (all sections)          | 2.4.8 Table 2-20                               |
| 2.2.8 - C - (Preface and all sections) | Effectively tested throughout 2.4.8 Table 2-20 |
| 2.2.8 - G - Preface                    | Introductory                                   |
| 2.2.8 - G - 1.1                        | Introductory                                   |
| 2.2.8 - G - 1.2                        | Introductory                                   |
| 2.2.8 - G - 1.3                        | 2.4.8 Table 2-21                               |
| 2.2.8 - G - 1.4                        | 2.4.8 Table 2-21                               |
| 2.2.8 - G - 1.5                        | 2.4.8 Table 2-21                               |
| 2.2.8 - G - 1.6                        | 2.4.8 Table 2-21                               |
| 2.2.8 - G - 1.7                        | 2.4.8 Table 2-21                               |
| 2.2.8.1                                | 2.4.8 Table 2-20                               |
| 2.2.8.2 and all sections               | (installation criteria)                        |
| PERFORMANCE    | VERIFICATION    |
|----------------|-----------------|
| 2.2.9          | 3.4.3           |
| 2.2.10         | 2.4.9           |
