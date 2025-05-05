1140 Connecticut Avenue, NW, Suite 1020 
Washington, DC  20036-4008 USA 
MINIMUM OPERATIONAL PERFORMANCE 
STANDARDS FOR AERONAUTICAL MOBILE 
HIGH FREQUENCY DATA LINK (HFDL) 
Copies of this document may be obtained from RTCA, Inc. 

1140 Connecticut Avenue, NW, Suite 1020 
Washington, DC 20036-4008 USA 
 
Telephone:  202-833-9339 
Facsimile:  202-833-9434 
Internet:  www.rtca.org Please call RTCA for price and ordering information. 

 

FOREWORD 
This report was prepared by Special Committee 188 (SC-188) and approved by the RTCA Program Management Committee (PMC) on December 14, 2000. RTCA, Incorporated is not-for-profit corporation formed to advance the art and science of aviation and aviation electronic systems for the benefit of the public.  The organization functions as a Federal Advisory Committee and develops consensus-based recommendations on contemporary aviation issues.  RTCA's objectives include but are not limited to: 
- 
coalescing aviation system user and provider technical requirements in a manner that helps government and industry meet their mutual objectives and responsibilities; 
 
- 
analyzing and recommending solutions to the system technical issues that aviation faces as it continues to pursue increased safety, system capacity and efficiency; 
 
- 
developing consensus on the application of pertinent technology to fulfill user and provider requirements, including development of minimum operational performance standards for electronic systems and equipment that support aviation; and 
 
- 
assisting in developing the appropriate technical material upon which positions for the International Civil Aviation Organization and the International Telecommunications Union and other appropriate international organizations can be based. The organization's recommendations are often used as the basis for government and private sector decisions as well as the foundation for many Federal Aviation Administration Technical Standard Orders. Since RTCA is not an official agency of the United States Government, its recommendations may not be regarded as statements of official government policy unless so enunciated by the U.S. government organization or agency having statutory jurisdiction over any matters to which the recommendations relate. 
This page intentionally left blank. 

## 1 Purpose And Scope

1.1 
Introduction These standards specify system characteristics that should be useful to designers, manufacturers, installers and users of the HF Data Link systems and equipment. 

 
Compliance with these standards is recommended as one means of assuring that the HF Data Link avionics will perform its intended function(s) satisfactorily under all conditions normally encountered in routine aeronautical operations.  Any regulatory application of this document is the sole responsibility of appropriate governmental agencies. 

 
This document encompasses standards and descriptions of a system configuration including Ground Subnetworks; HF Data Link Subnetworks, of which the Aircraft is one part; and Aircraft Subnetworks.  However, the specified Minimum Operational Performance Standards in this document address only the aircraft HF Data Link Subnetwork function. 

 
The MOPS covers typical HF Data Link avionics requirements and tests for the aircraft avionics.  It includes the purpose, scope and equipment performance requirements; recommended bench tests and other performance verification procedures; and installedequipment tests and operational performance characteristics. The High Frequency Data Link (HFDL) functions operate in the aeronautical frequency bands 2
-30 MHz. The transceiver must be capable of being tuned in integral multiples of 1 kHz to support the HF Data Link function and use the class of emission 2K80J2DEN. 

 
Section 1.0 of this document provides general information needed to understand the rationale for HF Data Link equipment and system characteristics and requirements stated in the remaining sections.  It describes typical applications and operational goals as envisioned by the members of Special Committee 188 and establishes the basis for the standards stated in Sections 2.0 through 3.0.  Definitions and assumptions essential to proper understanding of this document are also provided in this section, while a more extensive glossary appears as Appendix A. 

 
Section 2.0 contains the minimum performance standards for the aircraft HF Data Link function.  These standards specify the required performance under standard and environmental conditions.  Also included are recommended bench test procedures necessary to demonstrate equipment and network compliance with the stated minimum requirements. 

 
Section 3.0 describes the performance required of the installed aircraft avionics equipment.  Tests specifically for the installed equipment are included when performance cannot be adequately determined through bench testing. 

 
Section 4.0 describes the operational performance characteristics for equipment installations and for network operation and defines conditions that will assure the equipment user that operations can be conducted safely and reliably in the expected operational environment. 

The following list summarizes the industry standard documents and their specific versions referenced within this MOPS: 
 
Reference Document Name 
Version RTCA DO-160D 
July 27, 1997 
RTCA DO-163 
March 19, 1976 
RTCA DO-178B 
December 1, 1992 
RTCA DO-210D 
April 19, 2000 
RTCA DO-215A 
February 21, 1995 
RTCA DO-238 
April 2, 1997 
ARINC Characteristic 753-2 
February 20, 1998 
ISO-8208 (English) 
Release 2* 
HFDL SARPs 
 
Annex 10, Chapter 3, Amendment 74 
ICAO Manual for High Frequency Data Link First Edition 2000, Doc 9741-AN/962** 
May 2000 
ITU Appendix 27 AER 2 AC 20-140 
August 16, 1999 
 
 
Note:  
* Includes Amendment 1.  ** Within this document the abbreviation "ICAO 
SARPs Technical Specifications" will be used. 
In the event of any conflict between documents, this MOPS shall take precedence. 
 
Document references within this MOPS are used to assure common requirements between various documents to minimize the risk of conflict, and to reduce the complexity of this document.  The user of this MOPS should keep in mind that the referenced documents may, or may not, contain actual references to HF Data Link and therefore some editorial translations may be necessary.   
 
As used in this document, the term "aircraft avionics" includes all components and units necessary for the aircraft system to communicate through a High Frequency Ground Station for data services.  The aircraft avionics comprises multiple components, including antennas, couplers, and modulators/demodulators (MODEMs).  A particular aircraft avionics will not necessarily include all components or units referred to herein but will perform all required functions. 
 
The guidelines contained in RTCA/DO-178B, Software Considerations in Airborne Systems and Equipment Certification, should be considered with respect to aircraft HF Data Link software packages.  Users should also consult FAA Advisory Circular AC 20- 140, *Guidelines for Design Approval Aircraft Data Communications Systems*, dated 8/16/99. 

## 1.2 System Overview The High Frequency Data Link Provides Worldwide Communications Directly Between

aircraft subnetworks and ground subnetworks via high frequency radio and HF ground stations.  HF will support both data link and voice communications between aircraft users and ground-based users such as Air Route Traffic Control Centers (ARTCCs) and aircraft operating authorities (airlines).  Communication services accommodated by HF 
Data Link functions include two categories: Air Traffic Services (ATS), and Aeronautical Operational Control (AOC).  This document concentrates on these two categories as they pertain to safety and regularity of flight. 

1.2.1 
HF Data Link Architecture The overall HF Data Link system will provide both analog voice and packet-mode data exchanges between ground-based users and airborne users via high frequency radio channels.  The architecture defines system characteristics that are needed to assure a minimum worldwide air-ground communications Interoperability.  This has been accomplished for packet data services to be used by the international civil aviation community through specifying the International Standardization Organization's (ISO) Open Systems Interconnection (OSI) model.  HF Data Link data services will conform to guidelines for the Aeronautical Telecommunications Network (ATN). 

 
All voice transmissions will be analog single sideband for use within the aircraft and in the terrestrial subnetworks. 

1.2.2 
Communications Characteristics HF Data Link will operate in frequency bands allocated by the International Telecommunications Union (ITU) for Aeronautical Mobile (Route) Service (AM(R)S) in accordance with Appendix 27/AER 2. 

 
The channel access protocol to be used in the HF Data Link system is a combination of Frequency Division Multiple Access (FDMA) and Time Division Multiple Access (TDMA).  The TDMA slots are assigned by the ground station on a dynamic basis using a combination of reservation, polling and random access assignments.  A number of frequencies (channels) are available for HF Data Link users.  Each of the active frequencies is divided into frames with 13 slots.  The frame duration is 32 seconds and the slot duration is 2.461538 seconds. 

 
The first slot of each frame is reserved for use by the ground station to broadcast link management data in squitter packets.  The remaining slots may be designated either as uplink slots, downlink slots reserved for specific aircraft, or as downlink random access slots for use by all aircraft on a contention basis.  The assignment of slots to uplinks and downlinks for the upcoming frame is broadcast in the squitter.  Each squitter also contains the actual frame duration and number of slots as well as data which identify the active frequencies at the ground station and the IDs and active frequencies of up to two neighboring HF ground stations providing coverage in the same general area.  The squitters also contain acknowledgments to all downlinks received in the previous frame and channel loading data.  The channel loading data consists of projected slot availability for next two frames and the number of aircraft logged on the ground station. 

 
Universal signal formats and RF channel formats permit any aircraft to communicate with any ground station operating in the HF Data Link system.  Several different data rates are available for use in order to accommodate different propagation and service requirements. 

1.2.3 
Ground Equipment Requirements Ground equipment is required for HF voice and data service organizations to provide communications service between the aircraft and land-based end users.  The equipment must conform to standards used in conjunction with the airborne equipment to provide for the integrity, reliability and timeliness required for aeronautical communications associated with safety and regularity of flight.  These characteristics are described in regard only to their service requirements in the ICAO SARPs. 

1.2.4 
HF Data Link Requirements In order to provide worldwide coverage with adequate backup capability, a number of aeronautical ground stations will be required for HF Data Link.  Requirements for the high availability and integrity necessary for safety-related aeronautical mobile services are described in the ICAO SARPs. 

1.2.5 
Service Providers Service providers oversee the management of, access to, and international registration of the High Frequency radio frequencies and terrestrial networks under their control.  In the HF Data Link system, they must guarantee ground station performance, accept priority rules for allocation of resources and supply acceptable system monitoring and control. Also, voice and data connections to on-board subnetworks as well as ground subnetworks serving Air Traffic Control (ATC), airlines and others should be provided. 

1.2.6 
Communications Protocols For High Frequency Data Link communications to be effective between many aircraft belonging to different users and various ground end-systems, a single set of transmission protocols is defined. 

 
Packet data protocols are based on OSI models with capabilities to interface with various network protocols without regard to the implementation of the subnetworks and physical media through which the messages pass.  Messages traverse hierarchical protocol "layers."  Each layer in an originating subnetwork performs a function paralleled at the destination subnetwork's peer layer.  Possible differences in communicating systems are masked by these standard interfaces, permitting simplified and reliable systems interconnection. 

 
Each layer incorporates well-defined operations designed to optimize control and information flow across the layer boundaries.  To carry out its function, each layer may add protocol control information fields to the service-data-unit supplied by the layer above. However, each layer leaves the control information added by previous layers intact, treating it as data to be passed on unaltered. 

 
The OSI Reference Model defines seven such functional layers with responsibilities ranging from control of data transfer on the physical media (radio, wire, fiber, etc.) to control of the application user interface.  The seven layers are named: (1) Physical, (2) Link, (3) Network, (4) Transport, (5) Session, (6) Presentation, and (7) Application.  The aircraft avionics and its counterpart of the ground station implement either the lowest two or the lowest three layers of the OSI model to provide packet-mode data services.  This document defines the aircraft avionics requirements and tests. 

 
The system requirements contained in Section 2.0 of this document support packet-mode communications reflected by the OSI.  Two modes of operation are permitted.  These modes are referred to as Data-2 and Data-3, to be consistent with existing industry standards (see RTCA/DO-210D).  Data-2 operation provides transparent data communications by enveloping the packets received from a higher-layer entity (HLE) without using internal network layer protocols.  Data-3 operation provides to the user a packet-switched subnetwork that implements the lowest three layers of the OSI model (physical, link and network) and is accessed using a standard interface defined in Reference Document "ISO-8208 (English), Release 2, Including Amendment 1." 

1.3 
Operational Applications Many applications for High Frequency Data Link are potentially available.  However, HF Data Link when operating on AM(R)S frequencies will only support applications for ATS and AOC in accordance with Appendix 27 AER 2 to the ITU Radio Regulations. 
1.3.1 
Air Traffic Services (ATS) Air Traffic Services (ATS) include Air Traffic Control (ATC), the Flight Information Service, the Alerting Service, and Automatic Dependent Surveillance-Addressed (ADS- A).  High Frequency Data Link will provide an important new capability for ATS and AOC voice and data applications. 
1.3.1.1 
Air Traffic Control (ATC) Air Traffic Control applications anticipated to be supported by data links such as VDL, SATCOM, Mode-S, and HF Data Link are listed below: 
 
 
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
Predeparture Clearance Delivery 
 
i.  
Transfer of Communication 
  
 
j.  
Frequency Change 
 
k.  
Aircraft Estimated Trajectory 
 
l.  
Aircraft Estimated Trajectory (FMC/AERA Exchange) 
 
m. 
 
Arrival Identification and State 
 
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
(4) In-Flight Emergency, Safety 
 
(5) Military Interception Procedures 
 
(6) Out of Conformance Check 
 
(7) TCAS Sensitivity 
 
(8) VFR Terminal Area (including Class C Airspace) Access 
 
(9) Hijack 


(10) In-Flight Emergency, Medical
 
 
1.3.1.2 
Flight Information Services (FIS) Flight Information Services (FIS) provided over a data link will use information from weather communications processors that provide alphanumeric and graphical weather data.  FIS will also access data from terminal area equipment such as Terminal Doppler Weather Radar, Low Level Wind Shear Alert System, Airport Traffic Information System Workstation, and Automated Surface/Weather Observation Systems.  Data will also be accessed from national systems to include the Weather Message Switching Center, and the Centralized NOTAM Service Processor.  HF Data Link is an important transmission service for these applications. 
 
The following service applications eventually may use a data link such as VDL, SATCOM, Mode-S, and HF Data Link: 
 
 a. 
Weather Reporting Applications 
 
 (1) Hazardous Weather Advisory (2) Surface Observations (3) Radar Summary (4) Pilot Reports (PIREPs) (5) Terminal Forecast (6) Winds Aloft Forecast (7) Aviation Route Forecast (8) Notice to Airmen (NOTAM) (9) Hazardous Weather Graphic Map (10) Current Air Observations (PIREPs and Winds Aloft downlinked by the 
aircrew) 
 b. 
Terminal Area Applications 
 
 (1) Airport Traffic Information Service (ATIS) 
 (2) Current Position Information/Verification (3) Surface Winds (4) Traffic Information (5) Wind Shear Alert 
c. 
Airport Applications 
 
 (1) Control of Runway Lights (2) Runway Assignments (3) Local Landing Clearance (4) Parallel Runway Monitoring (5) Sequence to Land (6) Flow Management Advisory (7) Surface Traffic Monitoring and Control 
 
1.3.1.3 
Alerting Services The objective of the Alerting Service is to notify appropriate organizations regarding aircraft in need of search and rescue, and to aid and assist such organizations as required. 
1.3.1.4 
Automatic Dependent Surveillance-Addressed (ADS-A) Automatic Dependent Surveillance (ADS-A) is an important new ATC procedure based on the periodic reporting from aircraft of position, altitude and time derived from very accurate, high-integrity on-board navigation data (e.g., GPS).  The initial use of ADS is being planned for oceanic areas; future ADS-A operation is foreseen for domestic operations as well as oceanic and remote areas.  ADS-A messages will support both ATS and AOC requirements.  These messages will be transmitted over a data link to user facilities at specific intervals, as negotiated or upon request. 
1.3.2 
Aeronautical Operational Control (AOC) Like ATS, Aeronautical Operational Control (AOC) is a safety service defined in ICAO Annex 6, Part I, which gives the right and duty to exercise authority over the initiation, continuation, diversion or termination of a flight in the interest of the safety of an aircraft, and the regularity and efficiency of flight. 
 
In addition to packet data communications, data file transfers to support AOC needs such as data base updates, software changes, graphics, and facsimile may be accommodated by HF Data Link. 
1.3.2.1 
AOC Functions AOC functions may directly accommodate dispatch and flight operations department 
functions, or may interface with other departments such as Engineering, Maintenance and Scheduling, in exercising or coordinating related functions.  Some examples of AOC functions are: 
 
 a. 
Exceptional situation handling (aircraft/flight emergencies, hijack, etc.) 
 b. 
Flight planning 
 c. 
Weather information 
 d. 
Airports/airways operational information (NOTAMs), etc. 
 e. 
Movement control (flight departure, arrival, delay and diversion) 
 f. 
Cockpit crew flight times/scheduling 
 g. 
Aircraft engine monitoring 
 h. 
In-Flight maintenance problem reporting and solving 
 i. 
Fuel consumption and requirements 
 j. 
Aircraft scheduling (for particular flights) 
 k. 
Schedule modifications (changes or cancellation of flights), etc. 
 
These AOC functions operate via air-ground voice and data communications either through the cockpit crew or directly with airborne sensors or systems; e.g., Flight Management Systems (FMS), or Digital Flight Data Acquisition Units (DFDAU). Functions served would include FMS Operational Data Base update on flight plans, load and balance, weather, pre-departure clearances, etc.; and DFDAU recording of and reporting on engine health monitoring, fuel flow/status requirements, etc. 
1.3.2.2 
Operations Services Aeronautical Operational Control uses data communications efficiently to operate flight programs supporting accurate and timely information, coordinating activities in the interests of passenger, baggage, cargo and mail; and to enhance flight safety, punctuality, and cost reduction.  HF Data Link will support AOC functions by providing worldwide, continuous services. 
 
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
Aircraft engine monitoring 
 
1.4 
Operational Goals Four basic airspace environments are defined to provide background for HF Data Link goals: 
 
a. 

Oceanic/continental en route airspace with low traffic density (includes low-altitude, offshore and remote areas) 
b. 

Oceanic airspace with high-density traffic c. 

Domestic airspace with high-density traffic d. 

Terminal areas with high-density traffic 
 
These environments differ in data and voice traffic volumes, urgency of access, requirements for end-to-end delays and established capabilities.  HF Data Link will provide greater reliability and integrated services in airspace where they are effectively implemented. 

1.4.1 
Global Coverage The ultimate goal of HF Data Link is to provide the aviation community with worldwide, high-quality safety (ATS/AOC) communication services, and increased coverage for the polar areas. 

1.4.2 
Compatibility and Interoperability HF Data Link must be compatible and interoperable with external systems for all levels of users.  This requires implementation of well-defined gateways and peer-to-peer protocols. Therefore, HF Data Link must provide standard end-user subnetwork interfaces among airborne systems and associated terrestrial systems on a global basis.  For packet data transmissions, HF Data Link will implement the OSI Reference Model and will ultimately be integrated in the Aeronautical Telecommunications Network (ATN). 

 
HF Data Link routing and a ddressing schemes must be compatible worldwide.  The twenty-four (24) bit International Civil Aviation Organization (ICAO) standard address will be the basic address used throughout HF Data Link to ensure compatibility between organizations and systems. The aircraft avionics provides the chosen ground station with its own identification in the form of the 24-bit ICAO aircraft identification code. 

 
When the ATN is operational, HF Data Link will be interoperable with the Aeronautical Telecommunications Network which is also supported by Very High Frequency (VHF), Aeronautical Mobile Satellite Communications (AMSC), and Mode Select (Mode-S) data links and will use procedures compatible with these systems. 

1.4.3 
End-to-End Service Criteria The criteria for HF Data Link service provided among end users of the system are to be contained in the ICAO SARPs. 

The criteria addressed in these documents comprise the following: 
 
a. 
Overall service requirements, to ensure that technical characteristics and system integrity are consistent with the needs of safety communications, 
including those cases where other traffic may also be present. b. 
Overall availability requirements, to ensure the certainty and continuity required for safety communications. c. 
Other functional requirements necessary for safety services, including: (1) preemption control, to ensure that safety services have sufficient system 
resources available to them to meet their needs. (2) priority control, to permit higher-priority communications to proceed in 
preference over lower-priority communications. 
(3) automatic handover of HF Data Link aircraft communications between 
service providers, and ground stations. 
 
(4) a log-on scheme for aircraft avionics to/from the HF Data Link system 
that is identical for all service providers. (5) common procedures for establishment of ATS connections. d. 
To obtain the benefits envisioned by CNS/ATM concepts, it will generally be necessary for aircraft to achieve appropriate performance related to communications, navigation, and surveillance (CNS). 
 

## 1.5 Assumptions And Postulated Environment To Provide Guidance And Background For The Development Of Specific Operational Requirements By Users, The Year 2010 Airspace System Environment Was Postulated And Certain Assumptions Made Regarding That Future Environment. 1.5.1 Coverage Hf Data Link Communications Coverage Depends On The Location Of The Hf Data Link Ground Stations In Relation To The User Aircraft.  Present Hf Data Link Ground Stations Whose Locations Are Specifically Optimized For Maritime Traffic Are Being Upgraded Specifically For Hf Data Link. These Locations Provide Useful Hf Data Link Coverage Over Virtually All Of The Globe. 1.5.2 Data Versus Voice Communications Although Voice Communications Will Be Used For The Foreseeable Future, As The Capacity And Precision Capabilities Of Aeronautical Data Links Become More Apparent, Routine Air-Ground-Air Communications Will Evolve Toward Being Computer-To-Computer.  Pilots And

controllers will use digital data for many purposes, but will continue to use voice communication for non-routine and unanticipated needs. 

1.5.3 
Safety Safety communications, by ICAO and International Telecommunication Union (ITU) regulations, are assured of always having the highest priority and are accorded special measures for protection from interference.  A system supporting safety communications has appropriate priority and preemption control mechanisms embodied in all elements comprising the system. 

 
With the increasing use of data, voice operation will likely diminish.  Voice will always be available for use in emergency and other urgent ATS situations.  HF Data Link safety services include ATS, which will extend current ATC services, and AOC, which will provide carriers with communications to enhance safety and regularity-of-flight operations.  The initial application of HF Data Link in oceanic areas will provide improved communications, and surveillance procedures.  Among other benefits, this will lead to improved safety. 

1.5.4 
Priority, Precedence and Preemption The HF Data Link system, including the airborne avionics and other subsystems, must have means for effecting the priority structure necessary for Aeronautical Mobile (Route) Service safety communications.  This includes the mechanisms for controlling the precedence of both safety and non-safety messages, for the preemption of system resources as needed to support safety services and to provide for the added measure of protection to be accorded the safety services. 

1.6 
Overview of Test and Performance Verification Procedures The test and performance verification procedures specified in this document are intended to be used as one means of demonstrating compliance with the performance requirements.  Although specific test and performance verification procedures are cited, it is recognized that other methods may be preferred and may be used if they provide at least equivalent information.  In such cases, the procedures cited should be used as one criterion in evaluating the acceptability of the alternate procedures. 

 
The order of procedures specified suggests that the equipment be subjected to a succession of tests or analyses as it moves from design to design qualification and into operational use. 

 
Four types of procedures are specified in the following Sections. 

1.6.1 
Environmental Tests and Performance Verification Environmental test and/or analysis requirements are specified in Section 2.3.  The procedures and their associated limit requirements are intended to provide a laboratory means of determining the electrical and mechanical performance of the equipment under the environmental conditions expected to be encountered in actual operations. 

 
Unless otherwise specified, the environmental conditions and test procedures contained in RTCA/DO-160D, Environmental Conditions and Test Procedures for Airborne Equipment, will be used to demonstrate equipment compliance. 

1.6.2 
Bench Tests and Performance Verification Bench test and/or analysis procedures are specified in Section 2.4, and provide a laboratory means of demonstrating compliance with the requirements of Section 2.2.  Test results may be used by equipment manufacturers as design guidance for monitoring manufacturing compliance and, in certain cases, for obtaining formal approval of equipment design. 

1.6.3 
Installed Equipment Tests and Performance Verification The installed equipment test and/or analysis procedures and their associated limits are specified in Section 3.0.  Successful completion of bench and environmental test procedures of Section 2 is a precondition to completion of the installed equipment tests.  In certain instances, however, installed equipment tests may be used in lieu of bench test simulation of such factors as power supply characteristics, interference from or to other equipment installed on the aircraft, etc.  Installed-equipment tests are normally performed under two conditions: 
 
a. 

with the aircraft on the ground and using simulated or operational system inputs. 

 
b. 

with the aircraft in flight using operational system inputs appropriate to the equipment under test. 

 
Test results may be used to demonstrate functional performance in the intended operational environment. 

1.6.4 
Operational Tests and Performance Verification Operational tests and/or analyses are specified in Section 4.0.  These test procedures and their associated limits are intended to be conducted by operating personnel as one means of ensuring that the equipment is functioning properly and can be reliably used for its intended function(s).  

## 2 Equipment Performance Requirements And Test Procedures 2.1 General Requirements General Equipment Requirements Need Not Be Tested In The Test Procedure Subsection.  If A Requirement Needs To Be Tested, It Is Not A General Requirement And Is Included In Section 2.2. 2.1.1 Airworthiness The Design And Manufacture Of The Equipment Shall Provide For An Installation That Does Not Impair The Airworthiness Of The Aircraft. 2.1.2 Intended Function The Equipment Shall Perform Its Intended Function, As Defined By The Manufacturer, And Its Proper Use Shall Not Create A Hazard To Users Of The National Airspace System (Nas). 2.1.3 Federal Communications Commissions Rules The Equipment Shall Comply With All Applicable Rules Of The Federal Communication Commission (Fcc).1 2.1.4 Fire Protection All Materials Used Shall Be Self-Extinguishing Except For Small Parts (Such As Knobs, Fasteners, Seals, Grommets And Small Electrical Parts) That Would Not Contribute Significantly To The Propagation Of A Fire. Note: One Means Of Showing Compliance Is Contained In The Federal Aviation Regulations (Far), Part 25, Appendix F. 2.1.5 Operation Of Controls The Operation Of Controls Intended For Use During Flight, In All Possible Combinations And Sequences, Shall Not Result In A Condition Detrimental To The Continued Performance Of The Equipment. Controls Shall Be Designed To Maximize Operational Suitability And Minimize Pilot Workload (See Do-238). Reliance On Pilot Memory For Operational Procedures Shall Be Minimized. 2.1.6 Accessibility Of Controls

Controls that are not normally adjusted in flight shall not be readily accessible to flight personnel. Controls that are normally adjusted in flight shall be readily accessible and properly labeled as to their intended function. The controls shall be operable with the use of only one hand. 

 
2.1.7 
Effects of Tests The equipment shall be designed so that the application of specified test procedures shall not be detrimental to equipment performance following the application of these tests, except as specifically allowed. 

2.1.8 
Performance in a Shared Environment All requirements for data integrity and timing should consider the effect of other active aircraft data links performing transfer operations in both directions at their nominal rates. 

2.2 
Equipment Performance Requirements, Standard Conditions 
The organization of the following requirements has been mapped into a convenient table for the benefit of the user.  References are included for convenience. 

## Equipment Performance Requirements

Data-3 - 2.2.5.2, 2.2.5.4.2 
System Management 
Data 2 - 2.2.5.1, 2.2.5.4.1 
1.  Log-on Request Format - 2.2.6 
1.  Enveloping - 2.2.5.1 2.  Priority - 2.2.2, 2.2.5.3 
1.  8208 Packet Format 2.  SVC's 3.  Priority vs. SVC 
2.  Log-on Status Indication 3.  HFDL Table Updating 
4.  Voice/Data Mode Selection 
      - 2.2.2.1 
DLS  (ICAO) 
RLS  (ICAO) 
1.  LPDU Format 
2.  LPDU MAX Size 
1.  Segment/Reassembly 
2.  LPDU Format 3.  LPDU MAX Size 
4.  ARQ Protocol 
Priority, Precedence, and Preemption - 2.2.2, 2.2.5.3 1.  Preempt Data Transmission - 2.2.2.1 2.  Prioritize MPDU Encapsulation - 2.2.4.6 3.  MPDU Format - 2.2.4.7 TDMA Protocol 
5.  Squitter PDU Format - 2.2.4.5 
1.  Data Rate Communications - 2.2.4.1 2.  Downlink Slot Selection - 2.2.4.2 
3.  MAX MPDU Size & Data Rate 
- 2.2.4.3
4.  Data Rate & Interleaver Selection - 2.2.4.4 HFDL Signal-in-Space - 2.2.3.2 
5.  M-PSK Symbol Scrambling - 2.2.3.2.3.3 
6.  Transmit Pulse Shape Filtering - 2.2.3.2.5 
7.  Packet Error Rate - 2.2.3.3.2 
1.  Prekey - 2.2.3.2.1 2.  Preamble - 2.2.3.2.2 
3.  Forwar
d Error Correction (FEC) - 2.2.3.2.3.1 
4.  Interleaving - 2.2.3.2.3.2 

## Rf

1.  Prekey Transmit Full Power in 200 ms - 2.2.3.2.1 2.  Transmit to Receive Recovery Time - 2.2.3.3.3 3.  Spectrum Control In Data Mode - 2.2.3.2.6 

2.2.1 
Avionics Subsystem Definitions and Overall Requirements The requirements of this document include those that apply generally to the overall airborne avionics, as described below, followed by those that are related to the Transceiver Packet Data Subsystem.  Additional requirements are contained in RTCA DO-163, Minimum Performance Standards - Airborne High Frequency Radio Communications Transmitting and Receiving Equipment Operating within the Radio Frequency Range of 1.5 to 30 Megahertz. 

 
The Transceiver Packet Data Subsystem is defined to include the transmitter, receiver, and Modem.  It interfaces at RF at the antenna port, and with other on-board avionics equipment through an appropriate interface. 

 
2.2.2 
Priority, Precedence and Preemption (Voice/Data) The airborne avionics shall order the precedence of its transmissions in accordance with the requirements and associated priority structures for packet-mode services contained in Section 2.2.5.3. A message priority, when assigned by the initiating user terminal equipment in accordance with Tables 2
-1 shall be (1) made available to the airborne avionics terminal management function and (2) transmitted to the ground station in RLS mode and forwarded to the ground-based network management function. Similarly, the airborne avionics shall be capable of receiving the priority from the ground station and transferring them to the airborne avionics terminal management function. In-process transmissions of lower priority shall be preempted at the earliest opportunity when necessary to support higher-level priority communications in accordance with the same sections, as appropriate. 

 
Note: When packet-mode operations are conducted using Data-2, packet priority, 


precedence and preemption are managed by a higher-layer entity. 

 
The HF Data Link system shall provide the flight crew with absolute control over the mode of operation.  The flight crew shall have the ability to immediately change the operating mode from HF Data Link to HF Voice regardless of data link message status. A selection of Voice Mode, if available, should always interrupt any data mode operations without delay.  For the purposes of this Section, "without delay" means < 500 ms. The immediate mode change to voice operation may happen during the reception of a data message from the ground, or during the transmission of a message to the ground.  It is recognized that in either case, the potential for a lost/delayed message exists. 

2.2.2.1 
Voice/Data Mode Selection There are two basic methods to preempt HF data transmission.  These are crew initiated Voice/Data Mode selection and the transmission of voice communications by a second HF transceiver.  The Voice/Data Mode selection is under the positive control of the flight crew.  The flight crew may select the Voice Mode at anytime using the cockpit HF Voice/Data Control Function.  When the Voice Mode is selected, the transition to voice operation shall be accomplished without delay, see Section 2.2.2. 

## 2.2.2.2 Dual Hf Data Link Installations A Second Preemption Mode Occurs When An Aircraft Is Equipped With A Dual Hf Installation.  It Is Very Common For Such Installations To Employ Only A Single Antenna System.  In This Case, The Equipment Operating In The Data Mode Shall Monitor The Mode Of The Other System. The Data System Shall Also Monitor The Opposite Side Voice System Ptt. If The Data System Detects The Other Side Is In Voice Mode And Is Being Keyed For A Voice Transmission, The Data System Shall, Without Delay, Stop Transmitting.  After The Opposite Side Voice System Returns To The Receive Mode, The Data System Should Inhibit Any Data Transmissions For A Period Of Time Long Enough For The Crew To Hear Any Acknowledgments Or Messages.  The Data Link System Shall Delay Not Less Than 30 Seconds, Or More Than 90 Seconds Before Resuming Normal Data Communications. 2.2.3 Hf Data Link Subnetwork Physical Layer Requirements 2.2.3.1 Signal-In-Space Modulation Definition The Hf Data Link Shall Employ M -Ary Phase Shift Keying (M-Psk) To Modulate A Carrier Centered At The Rf Channel Frequency Plus 1440 Hz.  The Carrier Is Modulated At 1800 Symbols Per Second Plus Or Minus 10 Ppm (I.E. 0.018 Symbols Per Second). However, The User Data Bits (Information Data Rate) Are Transmitted At Selectable Rates Of 300, 600, 1200, And 1800 B/S.  The Signal -In-Space Shall Be As Defined In The Icao Sarps Per Appendix C Of This Document. 2.2.3.2 Signal-In-Space Transmission Requirements 2.2.3.2.1 Prekey Requirement The Main Purpose Of A Prekey Is To Allow A Transmitter To Reach Full Power And The Receiver To Stabilize Any Automatic Gain Control Prior To Data Transmission.  Due To Keying Delays, Transmitter Rise Times, And Receiver Recovery Times In The Hfdl System, Some Prekey May Be Lost.  During The Prekey The Modulator Shall Transmit An Fc + 1440 Hz Tone (Where Fc Is The Selected Ssb Carrier Frequency) With A Constant Phase Modulation Of 180 Degrees.  The Duration Of The Prekey In The Modem Design Shall Be 249 Ms.  The Transmitter Shall Come Up To Full Power (>90%) So As To Provide A Minimum Of 49 Ms Of The Prekey Carrier Output In The Slot.  Refer To The Icao Sarps Per Appendix C Of This Document. 2.2.3.2.2 Preamble Requirement Immediately Following The Prekey, A Synchronization Preamble With Known Data Shall Be Transmitted As Defined In The Icao Sarps Technical Specifications Per Appendix C Of This Document. 2.2.3.2.3 Data Segment Requirement

A data segment shall be created from the user data and trailer bits that include encoder and flush bits as defined in the ICAO SARPs Technical Specifications per Appendix C of this document. 
2.2.3.2.3.1 
Forward Error Correction The data segment shall be encoded using an error-correcting algorithm of rate 1/2 and 1/4 convolutional codes as defined in the ICAO SARPs Technical Specifications per Appendix C of this document. 
2.2.3.2.3.2 
Interleaving Requirement Data interleaving is used to minimize the impact of burst errors on the decoding of the data stream.  The interleaving requirements are in the ICAO SARPs Technical Specifications per Appendix C of this document. 
 
2.2.3.2.3.3 
M-PSK Symbol Scrambling 
M-PSK Symbol Scrambling is used to reduce the likelihood of a short term Direct Current buildup in the transmitted waveform.  The first bit of the interleaver output block is scrambled first and continues on in order to the last scrambled bit transmitted.  Only the information carrying symbols are scrambled as defined in the ICAO SARPs Technical Specifications per Appendix C of this document. 
2.2.3.2.4 
Transmit Slot Time Synchronization The HF Data Link employs a Time Division Multiple Access (TDMA) protocol.  The HF Data Link Ground Station provides the master timing for system synchronization through the timing of the Squitter protocol Data Unit (SPDU).  The slot timing is defined in the ICAO SARPs per Appendix C of this document.  The transmission of the Prekey shall start at the slot beginning, +10 ms as received at the aircraft.  The aircraft HF Data Link system does not compensate for RF propagation path delays. 
2.2.3.2.5 
Transmit Pulse-Shaping Filter Response The transmit pulse-shaping filter responses shall be per the ICAO SARPs per Appendix C of this document. 
Note:  *This requirement may be verified by inspection*. 
2.2.3.2.6 
Spectrum Control in Data Mode While operating in the data mode, the HF Data Link shall continue to meet the spectrum mask defined in DO-163 Transmit Section 2.3 Spectrum Control. This requirement is also the same as the ICAO Annex 10. 
The peak envelope power (Pp) of any emission on any discrete frequency shall be less than the peak envelope power (Pp) of the transmitter, see the ICAO SARPs per  
 
Appendix C of this document, in accordance with the following:  


a.  
On any frequency removed by 1.5 kHz or more up to 4.5 kHz from the SSB assigned frequency: at least 30 dB. 


b.  
On any frequency removed by 4.5 kHz or more up to 7.5 kHz from the SSB assigned frequency: at least 38 dB.  


c.  
On any frequency removed from the SSB assigned frequency by 7.5 kHz or more 43 dB. 


d.  
See Note in Figure 2.2-2. 


2.2.3.2.7 
Transmitter Peak Envelope Power Transmitter peak envelope power shall not exceed 400 watts except as provided for in Appendix S27/62 of the Radio Regulations.  Also see the ICAO SARPs per Appendix C of this document. 

 

2.2.3.3 
Reception Requirements 
Receiver shall perform as defined in the ICAO SARPs per Appendix C of this document. 2.2.3.3.1 
HF Data Link Receiver Sensitivity The HFDL Receiver shall be capable of receiving (i.e. decoding) 90% of HFDL packets 
error-free when the input signal level is 2 µV (-101 dBm) hard or weaker.  See RTCA 
DO-163 Receiver Appendix B, H3, except change 52 ohms to 50 ohms. 
2.2.3.3.2 
Packet Error Rate Performance The Packet Error Rate of the demodulator, including the de-Interleaver, Forward Error Correction decoder and descrambler, shall meet the requirements  for channel rates and conditions as given in the ICAO SARPs per Appendix C of this document. 
 
Note: The phase noise caused by the transmitting path between the analog input 
from the modem and the power output of the transmitter measured at the antenna terminals should not exceed 3 degrees rms. measured in a 500 microsecond sampled interval.  
 
The phase noise caused by the receiving path between the antenna input and the analog output to the modem should not exceed 3 degrees rms. 
measured in a 500 microsecond sampled interval. 
  
2.2.3.3.3 
Transmit to Receive Recovery Time The receiver baseband output amplitude shall recover to 90% of its final value after transmission to provide at least 50 ms of the Prekey from the following slot.  See Section 2.2.3.2.1, and the ICAO SARPs per Appendix C of this document. 
2.2.3.3.4 
Receiver Signal Attenuation 
Receivers, input signals shall be attenuated such that on any frequency between (fc + 350 Hz) and (fc + 2500 Hz): not more than 4 dB below the peak of the desired signal, 
undesired input signals shall be attenuated as defined in the ICAO SARPs per  
 
Appendix C of this document, and in accordance with the following: 


a.  
On any frequency between fc and (fc - 300 Hz), or between (fc + 2900 Hz) and (fc + 3300 Hz):  at least 35 dB below the peak of the desired signal level. 


b.  
On any frequency below (fc - 300 Hz), or above (fc + 3300 Hz):  at least 60 dB 
below the peak of the desired signal level. 


Note: If the transceiver also supports voice operations using common filters, this requirement may be tested in the voice mode and an external data output. 

 
2.2.3.3.5 
Frequency Search Each aircraft station shall search until it detects an operating frequency from among the currently assigned frequencies.  See the ICAO SARPs per Appendix C of this document. 

2.2.4 
HF Data Link Subnetwork Data Link Layer Functions The HF Data Link shall operate on frequencies assigned for AM(R)S use in the HF spectrum.  The system will use TDMA protocols.  The avionics shall utilize the basic frame structure which is 32 seconds and contains 13 slots.  Each slot is approximately 32/13 (2.461538) seconds long.  The first slot is always an uplink slot and contains a ground station squitter.  The avionics shall process and make use of the squitter information concerning the system operations. 

 
The access protocol is defined in the ICAO SARPs Technical Specifications per Appendix C of this document.  Slot and Frame timing are also in the ICAO SARPs Technical Specifications per Appendix C of this document. 

 
 
Note:  These requirements may be verified by inspection and indirectly tested when other requirements of this document are tested. 

 
2.2.4.1 
Data Rate Communications 
 
 
The recommended maximum operating data rates shall be reported to the ground during the Log-on process and continuing throughout the session.  Requirements for this operation are in the ICAO SARPs Technical Specifications per Appendix C of this document. 

 
2.2.4.2 
Selection of Downlink Slot by Aircraft 
 
The ground stations control the use of each time slot through information contained in the squitter.  Downlink slot assignments are made based on a hierarchical structure which advances highest priority traffic.  The aircraft HF Data Link function must select an appropriate downlink slot based upon the information contained in the uplink squitter.  The requirements are in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.3 
Maximum MPDU Size Adjustment The HF Data Link system is designed to support multiple data rates in fixed time slots using either a single or double slot.  To maximize efficiency, the size of the MPDU used shall be adjusted in accordance with the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.4 
Data Rate and Interleaver Selection The selection of the downlink data rate and Interleaver duration shall be based upon the MPDU/SPDU size as defined in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.5 
Squitter PDU Format The Squitter Packet Data Unit (SPDU) is 67 octets in length and is transmitted at 300 b/s by the ground stations.  The avionics shall decode, process, and utilize the information contained within the squitter.  The requirements for the squitter are found in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.5.1 
SPDU ID The SPDU ID is a one octet field and contains information on channel utilization, if the ground station supports ISO-8208 ATN, and pending changes.  See the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.5.2 
Ground Station Address The ground station address is a one-octet field that uniquely identifies the ground station and if it is synchronized to UTC.  See the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.5.3 
Frame ID The Frame ID is a two-octet field that contains a frame index relating to the count from 0000 UTC and a frame offset from 0000 UTC.  The requirements are in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.5.4 
Slot Acknowledgment Codes Thirty-six octets are used by the ground station to broadcast 12 bit acknowledgment fields for the previous 24 non-squitter slots.  See the requirements in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.5.5 
Slot Assignment Codes Twelve octets are used by the ground station to transmit slot assignments for 12 nonsquitter future slots as defined in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.5.6 
Priority Field The priority field is a one-octet field in which four bits are used to indicate the lowest priority message being accepted by the ground station.  See the ICAO SARPs Technical Specifications per Appendix C of this document. 

 
2.2.4.5.7 
Ground Station Active Frequency Field The Ground Station Active Frequency Field utilizes eleven octets that communicate a version number, the frequencies that are active at the ground station, and similar information for two other ground stations.  This requirement is defined in the ICAO SARPs Technical Specifications per Appendix C of this document.  
 
2.2.4.5.8 
Frame Check Sequence 
 
Each squitter makes use of a 16 bit Frame Check Sequence (FCS) to assure the integrity of the SPDU.  The FCS requirement is based on ITU-T and is found in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.5.9 
Flush Field The Flush Field is transmitted by the ground station to assure complete message communication.  The one octet field is defined as eight zeros appended after the FCS field. 

2.2.4.6 
MPDU Packet Encapsulation The Link Layer performs three levels of encapsulation.  User packets, defined as HF Network Protocol Data Units (NPDUs), are first segmented into Basic Data Units (BDUs) when the NPDU is to be delivered using Reliable Link Service (RLS).  Each segment of the NPDU is encapsulated into a Link Protocol Data Unit (LPDU) and then one or more LPDUs are encapsulated into a single Media Access Control (MAC) protocol Data Unit (MPDU) to maximize use of a slot.  The maximum length of an MPDU that occupies a single slot shall be 405 octets for 1800 b/s and for a double slot, 945 octets for 1800 b/s.  The assembly of MPDUs shall meet the priority requirements of Section 2.2.5.3.  The encapsulation requirements are in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.7 
MPDU Format Requirements The HF Data Link System shall format MPDU Headers, Data, and Flush fields as defined in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.7.1 
Mid (MPDU ID) Field The first octet is used to differentiate between MPDUs and SPDUs, uplinks and downlinks, and the number of LPDUs.  The ICAO SARPs Technical Specifications, contains the requirements for the MID per Appendix C of this document. 

2.2.4.7.2 
GS Field The GS field contains a one-octet ground station identification and is defined in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.7.3 
Aircraft Address Field The Aircraft Address Field is a variable length field that contains four basic pieces of data.  These are aircraft alias address, one octet; Reservation Request, one octet; 
acknowledgment field, two octets; and a variable length LPDU size.  The requirements are in  the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.7.4 
FCS (Frame Check Sequence) Each MPDU header makes use of a 16 bit Frame Check Sequence (FCS) to assure the integrity of the MPDU header.  The FCS requirement is based on ITU-T and is found in the ICAO SARPs Technical Specifications per Appendix C of this document. 

2.2.4.7.5 
Data Field The Data Field contains the user data and is a variable length.  See the ICAO SARPs Technical Specifications per Appendix C of this document. 2.2.4.7.6 
Flush Field The Flush Field is transmitted by the ground station to assure complete message communication.  The one octet field is defined as eight zeros appended after the last LPDU data field. 

2.2.5 
Packet-Mode Data Service Requirement The HF Data Link shall provide for packet-mode data service using Data-2 and Data 3, or Data-3 protocols. 

 
Data-2 is a specific implementation of the HF Data Link system in which the air/ground subnetwork access equipment contains only the physical and link layer functionality. 

 
Data-3 is a specific implementation of the HF Data Link system in which the air/ground subnetwork access equipment contains the physical layer, link-layer and network layer functionality according to ISO terminology. 

2.2.5.1 
Packet-Mode Data-2 Service Requirements An HF transceiver offering packet-mode Data-2 service shall provide a Link Service Interface as a direct access method to the Direct Link Service (DLS) and Reliable Link Service (RLS) link-layer protocols.  See the ICAO SARP per Appendix C of this document, and the RTCA/DO-210D, Section 2.2.7.4.1. Link Service Data Units (LSDUs) are injected or collected at the Link Service Interface in the HFDR. In order to ensure the forward compatibility of the Data-2 architecture with the standard subnetwork architecture (Data-3), the Link Service Interface user shall add a two-octet header to the user's message to form an LSDU before transmission. The user's message may consist of binary data and may contain up to 251 octets using DLS and 422 octets using RLS. The two-octet dedicated header shall be set to the value FFFF hex. Unless provided by the Link Service Interface user, a Q-precedence of seven (7) shall be used for transmission of LSDUs. The Link Service Interface user shall extract a received user message from an LSDU by removing the two-octet header. 

 
All LSDUs passed to the Link Service Interface shall be transmitted to the GS while the HFDR is logged on. If the HFDR is not logged on, any LSDU passed to the HFDR shall be discarded. Conversely, while the HFDR is logged onto a particular ground station, any messages received from the GS shall be forwarded to the Link Service Interface regardless of the availability of the destination avionics equipment. 

2.2.5.2 
Packet-Mode Data-3 Service Requirements Data-3 is the given name for the HF Data Link Subnetwork layer protocol architecture implemented in the HFDR and supporting the Aeronautical Telecommunications Network.  
See the ICAO SARPs Technical Specifications per Appendix C of this document, and RTCA/DO-210D, Section 2.2.7.5.2. 
 
The HF Data Link Subnetwork Layer (SNL) in the avionics shall offer connectionoriented packet data service to the Higher Layer Entities (HLEs) by establishing HF Data Link Subnetwork SVCs, Switched Virtual Circuits, with its peer entity in the GS. The SNL shall offer methods to convert addressing from the HLE to the SNL. 
 
The SNL in the HFDR shall support the following three main functions: a. 
The HF Data Link Subnetwork Dependent (SND) sublayer 
b. 
The HF Data Link Subnetwork Access (SNAc) sublayer 
c. 
The HF Data Link Subnetwork Interworking Function (IWF) 
 
The SND sublayer shall perform the SND protocol between the HFDR and a log-on GS by exchanging Subnetwork Protocol Data Units (SNPDUs). The SNAc sublayer in the HFDR shall perform the ISO-8208 DCE protocol between the HFDR and the connected airborne HLE (DTE). The IWF shall provide the protocol conversion functions and the flow control operation required between the SND and SNAc (ISO-8208) protocols. 
 
Notes: 1. This architecture allows communication between ISO conforming 
 
 
entities 
and 
is 
suitable 
for 
support 
of 
the 
Aeronautical 
Telecommunications 


Network (ATN) higher layer protocols and applications. The role of the ATN is to define an environment within which reliable endto-end data transfer may take place, spanning the envisioned airborne, air/ground, and ground-based data subnetworks, including the HF Data Link Subnetwork, while providing interoperability among those networks. 
The critical emphasis is on end-system data transfer interoperability. In 
the ATN environment, the HF Data Link Subnetwork Layer must support the transparent transfer of Network Protocol Data Units (NPDUs) between adjacent Interworking entities (or HLEs as seen by the DLSNL). This also implies the transparent transfer of global addresses (or NSAPs) and quality of service information (including network priority) as well as user data. 
 
2. Valuable guidance for packet data communications is provided in 
RTCA/DO-205, "Design Guidelines and Recommended Standards to Support Open Systems Interconnection for Aeronautical Mobile Digital Communications"; in particular, Part 1, Section 6.0 "Subnetwork Protocols to Access and Support ATN" discusses ground, airborne and air/ground subnetworks; Part 1 Appendix B gives a summary of the ISO-
8208 packet level Subnetwork Access Protocol (SNAcP). 
 

 
Q-Number 
(1) 
 
SNC Priority in 
CALL_REQUEST/ 
CALL_ACCEPTED 
Packet 
 
SNC Priority in 
INCOMING_CALL/ 
CALL_CONNECTED 
Packet  

2.2.5.3 
Priority, Precedence and Preemption (Data/Data) The order of precedence of transmission of packet-mode data appearing at an HFDR data port shall be as shown in Table 2
-1.  A message is handled in the link layer by segmenting it into one or more Basic Data Units (BDUs) which are encapsulated into Link Protocol Data Units (LPDUs) as defined in the ICAO SARPs and Technical Specifications per Appendix C of this document.  Transmission preemption, if necessary, shall be effected by immediately changing the order of BDU transmission such that the BDUs comprising the higher-priority message are transmitted before lower-priority BDUs.  Preemption of lower-priority messages, if necessary, shall be effected by any means necessary to preserve the higher-priority message. 

 
Since the HF Data Link is intended to provide only ATS and AOC Services on AM(R)S frequencies, the priority parameter should be set at a value no lower than 5, but is controlled by a ground station uplink value.  The ground station will reject messages and ISO-8208 virtual circuits where the priority is less than the priority parameter included in the squitter. 

 
Higher priority messages are included in the MPDU first.  Once the decision for inclusion in the next downlink transmission is made, no substitution is made.  The downlink message is assembled "just-in-time" for transmission and therefore, if interrupted, no useful transmission occurs in the slot.  Rather than interrupt a downlink message in progress, the transmission is finished and the next message with the new and higher priority is assembled first for transmission in the next available slot. 

 
The target and selected values of the priority of data on a connection in the ISO-8208 CALL REQUEST and CALL ACCEPTED packets shall be mapped to the LIDU Q number of the CONNECTION REQUEST and CONNECTION CONFIRM SNPDUs as defined in Table 2
-1.  The LIDU Q number associated with the CONNECTION 
REQUEST and CONNECTION CONFIRM SNPDUs shall be mapped into the target and selected values of the priority of data on a connection in the ISO-8208 INCOMING CALL and CALL CONNECTED packets as defined in Table 2-1. 

 
A Subnetwork Connection (SNC) of the lowest priority shall be cleared as necessary to accept a request for higher priority service. Note: When packet-mode operations are conducted using a Data-2 implementation, priority, precedence and preemption are managed by a higherlayer entity.] 
 
Category of Messages 
 

 Unspecified (ISO-8208 explicit) 255 0 None Reserved 254-15 Invalid/reject Not Applicable 14 14 14 Distress Communications, Urgent Communications, Network/Systems Management. (2) HF Data Link Management Not Applicable 13 Not Applicable 
 
 Reserved 
 
 12 
 
Invalid/reject 
 
 Not Applicable 11 11 11 Flight Safety Messages, Communications Relating to Direction Finding Reserved 10 Invalid/reject Not Applicable Reserved 9 Invalid/reject Not Applicable Meteorological Communications 8 8 8 Flight Regularity Communications 7 7 7 
 
  6 
 
  6 
 
  6 
 
 Aeronautical Information Service Messages (NOTAMs, ATIS, etc.) 5 5 5 Aeronautical Administrative Messages (3) Network/Systems Administration (2) Reserved 4 Invalid/reject Not Applicable 3 3 3 Urgent Priority Administrative and UN Charter Communications (AAC/APC) 2 2 2 High Priority Administrative and State/ Government Communications (AAC/APC) Normal Priority Administrative (AAC/APC) 1 1 1 Low Priority Administrative (AAC/APC) 0 0 None Unspecified None 0 None 
 
Notes:  1. Q-Number refers to the Link-Layer precedence contained in a SU to be 
 
transmitted. 
 
2. Network/System Management and Administration are not categories of 
messages 
but 
are 
used 
by 
ATN 
or 
other 
network 
management/administration. 
 
  
3. SNC Priorities 5 and above can be either ATS or AOC Communications. 
 
4. Priority Level 4 and below shall not be accepted in the HF Data Link 
AM(R)S. 
2.2.5.4 
HF Data Link Subnetwork Requirements In addition to the data link layer requirements specified in this document (which includes the Direct Link Service (DLS) quality of service), the HFDR shall also provide RLS on the HF Data Link Subnetwork.  RLS shall perform Automatic selective Repeat Request (ARQ) functions to supervise the correct reception of each LSDU.  As with Data-3, 

systems employing packet-mode Data-2, the HF Data Link Subnetwork shall use the RLS. 

  
2.2.5.4.1 
Data-2 Requirements 
 
The minimum requirements for Data-2 service are specified in Section 2.2.5.1.   
  
2.2.5.4.2 
Data-3 Requirements 
 
The minimum requirements for Data-3 packet-mode data service are specified in Section 2.2.5.2. 

2.2.5.4.3 
Join and Leave Event Requirements An HFDR employing Data-3 packet-mode data service shall provide Join and Leave event messages to the aircraft routing function to indicate that the air/ground data link is either available or not available, respectively. The Join/Leave messages shall include sufficient information for the routing function to determine the address(es) of the DTE(s) attached to the log-on GS.  See the ICAO SARPs, Section 11.3.4.2. 

 
Note: This may be accomplished, for example, by passing the GS ID from the HFDR 
  
 
to the routing function containing a lookup table for translation to DTE address(es), or by passing the DTE address(es) directly from the HFDR to the routing function. 

 
2.2.6 
Aircraft Log-on Procedure Every aircraft must Log-on with a single ground station in order to perform the data link function.  When logging on, an aircraft will receive a unique Aircraft ID from the ground station which will be used for all additional communications with that ground station.  The log-on shall be transparent to the aircraft crew.  The Log-on procedure is defined in the ICAO SARPs Technical Specifications per Appendix C of this document. 

 

2.2.7 
Recovery from Primary Power Interruption The HFDR equipment shall conform to the following requirements after encountering primary power interruptions from any cause: 
 
a. 
Power interruptions of less than five milliseconds duration shall be indistinguishable from outages in the RF transmission path of equal duration. 
 
b. 
Power interruptions from five to 200 milliseconds duration shall require no more than five seconds recovery time, beginning from when primary power has been restored.  Recovery is defined as automatically returning to the previous operating state (without user intervention) such that data channels resume in the same configuration they were in before the power interruption occurred.  This assumes a received signal with at least the minimum quality characteristics specified in Section 2.2.3.3.1. 
 
Note: In-transit data service packets which have been acknowledged on either the 
 
DTE or DCE interface, but not yet transferred to the opposite interface, may be 
lost. 
Non-HFDR 
higher-layer 
entities that employ end-to-end 
acknowledgment protocols may choose to retransmit such lost data.  Synchronization and RF output power may be lost during the power interruption and recovery time.  There shall be no more than a momentary 
effect on cockpit displays. 
 
2.2.8 
Failure/Status Indication 
 
 
The HFDR equipment shall provide, independent of any operator action, an indication of a failure of HFDR equipment resulting in loss of data communications.  
 
2.3 
Equipment Performance, Environmental Conditions 
 
2.3.1 
General Requirements The environmental tests and their associated performance requirements described in this Section are intended to provide a laboratory means of determining the overall performance characteristics of the equipment under environmental conditions representative of those which may be encountered in actual operations. 

 
Unless otherwise specified, the test procedures applicable to a determination of equipment performance under environmental test conditions are contained in RTCA Document DO- 160D, Environmental Conditions and Test P
rocedures for Airborne Equipment.  
General information regarding the use of the procedures in RTCA/DO-160D is contained in Sections 1.0 through 3.0 of that document.  Also, a method of identifying which environmental tests were conducted and other amplifying information on the conduct of the tests is contained in Appendix A of RTCA/DO-160D. Some of the software implemented performance requirements in Section 2.2 of this MOPS are not required to be qualified to all of the environmental conditions contai ned in RTCA/DO-160D.  Judgment and experience have indicated that these particular performance parameters are not susceptible to certain environmental conditions and that the level of performance specified in Section 2.2 will not be measurably degraded b y exposure to these conditions. 

 
In addition to the exceptions above, certain environmental tests contained in this section are not required for minimum performance equipment unless the manufacturer wishes to qualify the equipment for additional environmental conditions.  If the manufacturer wishes to qualify the equipment to these additional conditions, then these tests shall be performed. 

2.3.2 
Equipment Configurations Specific HFDR performance tests have been included for use in conjunction with the environmental procedures of RTCA/DO-160D.  These tests are a subset of the full HFDR performance tests contained in Section 2.4 of this MOPS.  Normally, a MOPS does not provide specific equipment performance tests to be used in conjunction with the environmental procedures of RTCA/DO-160D.  However, the large number of performance tests in Section 2.4 indicates that a test procedure that includes all of the performance tests combined with the appropriate environmental procedures would be impractical.  The HFDR qualification conforms to RTCA/DO-160D.  RTCA/DO-160D shall be used when running the test sequence. 

2.3.3 
Configuration Control Nominal environment testing, followed by extreme environment testing, shall be conducted on the HFDR with the Operational Flight Program (OFP) software installed according to the correct software version number as specified in the HFDR configuration documentation. 

 
2.3.4 
Specific Environmental Test Conditions The equipment shall be subjected to the test conditions as specified in RTCA/DO-160D, in the sections identified in Table 2
-2 Environmental Conditions.  By performing (and passing) those tests, the corresponding requirements of this standard shall be met. 

2.3.5 
Performance vs. Test Requirements Not all requirements n eed be verified as a function of environment because data has shown that they are not subject to degradation with the environment.  It is sufficient to verify compliance at ambient conditions for many requirements, and their continued compliance is inferred by successfully meeting the requirements in Table 2-2.  It is further defined that unless otherwise noted that to successfully verify compliance to a requirement section implies compliance to all lessor sections. 

 

 
 
Temperature Section 4.5 
2.2.3.2.1 
Minimum Prekey 
X 
2.2.3.2.6 
Spectrum Control in Data Mode 
X 
2.2.3.3.1 
HFDL Receiver Sensitivity 
X 
2.2.3.3.3 
Transmit to Receive Recovery Time 
X 

 
2.4 
Equipment Performance Verification Procedures 
The following procedures provide guidelines for tests to ensure compliance with the MOPS performance requirements.  Except for Section 3.4.5, these are not required for flight tests.  Any reference to "flight tests" in documents referenced herein should be ignored. 
Some of the following tests may require additional test equipment not shown in the test setup figures.  Such equipment may be associated with the interface between the GS Emulator and the transceiver receiver input. 
2.4.1 
Definitions of Terms and Conditions of Test The following are definitions of terms and the conditions under which the tests described in this Section should be conducted. 
 
1. 
Power Input Voltage - Unless otherwise specified, all tests shall be conducted with the power input voltage adjusted to design voltage +2%.  The input voltage shall be measured at the input terminals of the equipment under test. 
 
2. 
Power Input Frequency 
 
a. 
In the case of equipment designed for operation from an AC source of essentially constant frequency (e.g., 400 Hz), the i
nput frequency shall be 
adjusted to design frequency +2%. 
 
b. 
In the case of equipment designed for operation from an AC source of variable frequency (e.g., 300 to 1,000 Hz), unless otherwise specified, tests shall be conducted with the input frequency adjusted to within 5% of a selected frequency and within the range for which the equipment is designed. 
 
3. 
Adjustment of Equipment - The circuits of the equipment under test shall be properly aligned and otherwise adjusted in accordance with the manufacturer's recommended practices prior to application of the specified tests. 
 
4. 
Test Equipment - All equipment used in the performance of the tests should be identified by make, model and serial number where appropriate, and its latest calibration date.  When appropriate, all test equipment calibration standards should be traceable to national and/or international standards. 
 
5. 
Test Instrument Precautions - Due precautions shall be taken during the tests to prevent the introduction of errors resulting from the connection of voltmeters, oscilloscopes and other test instruments across the input and output impedances of the equipment under test. 6. 
Ambient Conditions - Unless otherwise specified, all tests shall be made within the following ambient conditions: 
 
a. 
Temperature: +15 to +35 degrees C (+59 to +95 degrees F) 
b. 
Relative Humidity: Not greater than 85% 
c. 
Ambient Pressure: 84 to 107 kPa (equivalent to +5,000 to -1,500 ft) (+1,525 to -460 m) 
 
When tests are conducted at ambient conditions which differ from the above values, allowances shall be made and the differences recorded. 
 
7. 
Connected Loads - Unless otherwise specified, all tests shall be performed with the equipment connected to loads having the impedance values for which it is designed. 
 
8. 
EMI Testing - Only the transceiver, not the test equipment, need be subjected to the electromagnetic environment as specified in DO-160D. 
 
Note: For specific airframes, the aircraft manufacturer may require the 
 
interconnecting wiring to be included in the specified electromagnetic 
 
environment. 9. 
Warm-up and Stabilization Requirements - Unless otherwise specified, all tests shall be conducted after a minimum equipment warm-up period of not less than five minutes.  In addition, the frequency reference source shall have completed its warm-up cycle, if any, and any power-on self test(s) shall have been completed prior to testing. 
 
10. Special Cooling Requirements - The manufacturer shall specify any special cooling 
requirements for any of the specified tests. 
 
2.4.2 
Required Test Equipment Ground Station Emulator - For the tests described herein, a Ground Station (GS) Emulator is required.  Transceiver functions and characteristics can be verified only when coupled through an RF link with its Ground Station counterpart, each controlling or reacting to various states (or changes of state) of the other. 
 
The Ground Station Emulator is not necessarily a single definable piece of test 
instrumentation, but it will likely comprise an assemblage of test equipment appropriate for a given test procedure capable of providing the functions necessary for that test.  For example, in certain RF tests, the Ground Station Emulator would establish a "link" with the transceiver, providing the properly modulated RF signals with appropriate accuracy and precision.  As another example, the Ground Station Emulator is necessary to verify correct operation of the signaling and communications protocols embodied in the transceiver. 

 
Because there are many ways in which the Ground Station Emulator can be realized, a detailed description is not necessary, or possible, herein.  However, in each procedure involving the Ground Station Emulator, the particular characteristics essential for that procedure are described. 

  
2.4.3 
Detailed Test Procedures 
 
The test procedures set forth below constitute a satisfactory method of determining required performance.  Although specific test procedures are cited, it is recognized that other methods may be preferred.  Such alternate methods may be used if the manufacturer can show that they provide at least equivalent information.  Therefore, the procedures cited herein should be used as one criterion in evaluating the acceptability of the alternate procedures. 

 
For performance verification purposes, this section includes procedures for the Transceiver Subsystem, including the Transmitter as defined in Section 2.2.3.2, and the Receiver as defined in Section 2.2.3.3.  The term HF Data Link Subnetwork Physical Layer is also used for this subsystem in regard to the layered ISO concepts for data communications protocols. 

 
The following receiver-related tests require a Ground Station Emulator and may require additional test equipment not shown in the test figures.  The transceiver frequency, mode, etc. are controlled by commands from the Ground Station Emulator.  The transceiver must be receiving a Squitter before a transceiver transmit signal can be generated while in the packet data mode.   
 
Some of the receiver tests in the following sections require the use of BER measurements as an indication of proper or improper transceiver operation, and some are repeated under various environmental conditions.  At the lower data rates, if post-Viterbi BERs are used the tests could require a considerable amount of test time.  A
s a result, pre-Viterbi channel error rates may be used in many of the Gaussian signal condition tests to greatly reduce the required testing time.  However, before pre-Viterbi BERs can be used they must be characterized by measuring the relationships between pre-Viterbi and post-Viterbi error rates.  The manufacturer will provide a test procedure to accomplish this characterization. 

 
2.4.4 
Priority, Precedence and Preemption Test Requirements 
 
(Sections 2.2.2, 2.2.5.3) 
 
Equipment Required 

 
UUT  
 
 
ISO-8208 Test Set/Protocol Analyzer (2), one designated as Protocol Analyzer Air 
(PAA), one designated as Protocol Analyzer Ground (PAG) 
Remote access equipment to ISO-8208 compatible data port at GS 
or, alternative, Ground Station Emulator 
Appropriate cabling and antenna for access to the HF Data Link Subnetwork, 
or,  alternatively,  
 
Directional Coupler, 30 dB coupling, 150 watts average power rating Test Procedures 
Step 1 - Setup the equipment as shown above in Figure 2.4-1.   
 
 
Step 2 - Set up a virtual circuit connection with a priority of 11 using the procedures in 
Section 2.4.19.3.4 Step 1. 
 
 
Step 3 - Set up a second virtual circuit connection with a priority of 7 using the 
procedures in Section 2.4.19.3.4 Step 1. 
Step 4 - Program the GS Emulator so that no downlink slots are available in future 
TDMA frames until the UUT (AS) is ready. 
Step 5 - Use the PAA (Protocol Analyzer - Air) to send a 128 octet downlink message 
of priority 7. 
Step 6 - Use the PAA to send a second 128 octet downlink message of priority 11. 
Step 7 - Program the GS Emulator so downlink slots are available in the next TDMA 
frame. 
Step 8 - Use the PAG (Protocol Analyzer - Ground) to observe that the downlink priority 
11 message is received before the downlink priority 7 message. 
 
2.4.5 
Voice/Data Mode Selection Test Requirements 
 
(Sections 2.2.2 and 2.2.2.1) 
 
Equipment Required UUT Power Attenuator, 80 dB, 200 watt average power RF Signal Generator, HP8640 or equivalent Oscilloscope Voice/Data Switch, Manufacturer supplied Test Procedures Connect the equipment as shown below: 

Generator
Power
Attenuator
UUT

Data Scope Trigger Set up the equipment to operate in the data mode.  Set the RF signal generator to operate on the voice frequency.  Trigger the scope on the data to voice switch transition. Observe the receiver Audio output to determine that the receiver is back in the voice mode.  Measure the time between the switch transition and the UUT output audio appearing.  Record the switching time.  Ensure the UUT meets the requirement of Sections 2.2.2 and 2.2.2.1. 2.4.6 
Dual HF Data Link Installation Test Requirements 
 
(Section 2.2.2.2) 
 
Equipment Required 
 
UUT Power Attenuator, 80 dB, 200 watt average power Diode Detector HP 8471D or equivalent Oscilloscope PTT Switch Message Source, ISO-8208 Protocol Analyzer, or equivalent Setup the equipment as shown above.  Allow the UUT to Log-on to a ground emulator. Input data to the UUT from the Message Source.  While data is being transmitted by the UUT press the PTT switch and observe the time it takes for the RF within the data packet to be turned off.  Record the switching time.  Open the PTT and observe the time before RF again appears.  Ensure the UUT meets the requirement of Section 2.2.2.2. 2.4.7 
Signal-In-Space Test Requirements 
 
(Sections 2.2.3.1, 2.2.3.2.1, 2.2.3.2.2, and 2.2.3.2.3 and subsections, 2.2.3.2.5) 


This test requires access to a test point to monitor the output bits of the HF signal-inspace modulator prior to the Square Root Raised Cosine pulse shaping filter. For digitally implemented transmit pulse shaping filters, analysis of the digital filter coefficients may replace direct measurement. 

 
Equipment Required Logic Analyzer with printer Defined Packet (Test Sequence) MPDU 
 
Digital Oscilloscope 
 
DSP Emulator capable of starting / stopping the Digital Signal Processor, and reading the memory addressable by the Digital Signal Processor Audio Spectrum Analyzer Ground Station Emulator 



Alternate Procedure 1: 
Connect the logic analyzer as shown in Figure 2.4-4(A) to the test points in the UUT to store the states of data.  Cause the transceiver to transmit known MPDU data messages (see Section 2.4.20) at the desired data rate and interleaver duration.  Use the logic analyzer and printer to record the transmitted bits. 
 
 
Compare the following: 
1. 
Contents and length of Prekey sequence with those specified in Section 2.2.3.2.1. 


2. 
Contents (bit sequence) of preamble with those specified in Section 2.2.3.2.2. 


3. 
Transmission of encoded, interleaved, and scrambled MPDU data in frames of 30 MPSK symbols followed by 15 BPSK known probe symbols as specified in Section 2.2.3.2.3.  


4. 
Contents (MPSK symbol sequence) of encoded, interleaved, and scrambled data carrying MPSK symbols with an independent analysis of correct sequence per specifications in Sections 2.2.3.2.3.1, 2.2.3.2.3.2, and 2.2.3.2.3.3. 
Repeat the above procedure at all data rates and interleaver duration. 
Alternate Procedure 2: 
Connect the logic analyzer as shown in Figure 2.4-4(B) to audio test output of the UUT. Cause the transceiver to transmit known MPDU data messages (see Section 2.4.20) at the desired data rate and interleaver duration.  Use the audio spectrum analyzer and Digital Oscilloscope to record the audio output. 
Compare the following: 
1. 
The tone characteristics can be compared against the Defined Results by examining 
the frequency on a digital oscilloscope.  The modulation characteristics can be compared by examining the audio out on a spectrum analyzer. 


2. 
The bit pattern contents of the preamble may be compared by examining the address space of the DSP processor. 


3. 
The symbol period can be measured by examining the minimum between the phase changes on an oscilloscope.  The bit pattern of the prekey will be examined by analysis.  The bit pattern contents of the data and probe can be compared by examining the address space of the DSP processor. 


4. 
Contents (MPSK symbol sequence) of encoded, interleaved, and scrambled data carrying MPSK symbols with an independent analysis of correct sequence per specifications in Sections 2.2.3.2.3.1, 2.2.3.2.3.2, and 2.2.3.2.3.3. 
Repeat the above procedure at all data rates and interleaver duration. 
Note:   This is an ambient condition bench test only. 
 

## 2.4.8 Transmit Pulse Shaping Filter And Spectrum Control Test Requirements (Sections 2.2.3.2.5, 2.2.3.2.6)

 
The Transmit Pulse Shaping Filter requirement may be verified either by direct measurement or by analysis if the pulse shaping filter is implemented digitally.  For measurement of the spectrum emissions and for a direct measurement of the pulse shaping filter spectrum, connect the equipment as shown in Figure 2.4-5. 
Using the Ground Station Emulator, cause the UUT to complete a Log-on sequence. Enter a script to the Ground Station Emulator which will cause the UUT to transmit. Capture the RF output on a Spectrum Analyzer.  Compare the spectrum shape within 3 kHz bandwidth of the square-root raised cosine spectrum requirement and compare the out-of-band spectrum emissions to the RTCA DO-163 described limits. 
Note:   *This is an ambient condition bench test only.* 2.4.9 
Prekey Time Test Procedure 
 
(Section 2.2.3.2.1) 
Power Attenuator, 80 dB, 200 watt average power Directional Coupler, 50 dB coupling Connect the equipment as shown in Figure 2.4-6. 
Step 1 - Establish communications between the UUT and the ground station emulator.      


Step 2 - Set the oscilloscope for a DC coupled input and a sweep time of 100 ms.            
Trigger using 20% pre-trigger.  
 
 
Step 3 - Set up the oscilloscope to use external trigger from the HFDL frame sync from 
the Ground Station Emulator. 


Step 4 - Select and send a downlink message from the message source.   


Step 5 - Capture the transmission period on the oscilloscope.    


Step 6 - Verify that the length of the prekey is in accordance with Section 2.2.3.2.1. 2.4.10 
Packet Error Rate Test Requirements 
 
(Section 2.2.3.3.2) 
 
These tests require use of an HF Channel simulator and an HF Data Link Ground Station Emulator (GSE).  The HF Channel Simulator may interface to the HF Data Link Airborne equipment at RF or baseband frequency, i.e. audio.  The tests require the use of Packet Error Rate (PER) measurements as an indication of proper or improper transceiver operation. 
 
 
Note:   To satisfactorily complete this procedure will require that the system phase 
noise limits are not exceeded. 

Equipment Required 
 
High Power Attenuator(s) (120 dB total attenuation) with 200 watts average power rating High Frequency Ground Station Emulator consisting of HF Data Link signal
-in-space encoder (modulator) and HF transceiver HF Channel simulator, RF or Baseband, capable of simulating multipath delays of up to 4 
ms with complex Gaussian fading statistics with up to 2 Hz Doppler Spread plus additive Gaussian noise Packet Error Rate measurement system 
 
DSP emulator 
 

## Test Procedures

 
Connect the equipment as shown in Figure 2.4-7.  Ensure that High Frequency Ground Station Emulator and HF Data Link Airborne equipment are tuned to the same test frequency.  Set HF Channel simulator to simulate two paths of equal strength with 4 ms of delay between each path, and 1 Hz Doppler Spread for each path, with additive Gaussian at a signal-to-noise ratio (in 3 kHz) equal to the target SNR specified in Section 2.2.3.3.2 for the selected data rate.  Cause the High Frequency Ground Station Emulator to transmit message (MPDU) of size and contents known to PER measurement system to be transmitted at the selected Data Rate and 1.8 second Interleaver duration.  Use PER 
measurement system to determine whether the MPDU was received or not and if received whether it has any errors.  Repeat until 1000 messages have been transmitted. Determine ratio of messages received with errors or not received to total number of messages transmitted. 

 
 
The IF signal provided to the function generator can be generated using a pre-recorded IF transmission.  This allows a repeatable input stream to be used when evaluating the PER. 

 
 
The PER is determined by the DSP receive algorithms.  The PER measurement results can be accessed using a DSP emulator to access the memory space addressable by the DSP processor. 

 
Repeat the above PER measurement for all available transceiver data rates.  Verify that all data rates meet requirements. 

 
If the actual PER is very close to the specified value, several PER measurements at the same data rate may be averaged. 

 
Note:  This is an ambient-condition bench test only; so an open unit with access to a test point is acceptable. 

 
2.4.11 
Transmit to Receive Recovery Time Test Procedure 
 
(Section 2.2.3.3.3) 
 
Equipment Required 
 
UUT Power Attenuator, 80 dB, 200 watt average power Directional Coupler, 50 dB coupling Digital Oscilloscope Ground Station Emulator 
 
Test Procedures 
 
Connect the equipment as shown Figure 2.4-8.  Allow the UUT to log in to the Ground Station Emulator.  Set up the digital oscilloscope to use external trigger from the HFDL frame sync from the Ground Station Emulator.  Set up the GSE to transmit an uplink packet immediately following a downlink from the UUT at -67 dBm.  Measure the recovered audio on the oscilloscope in the slot immediately following the UUT transmit slot.  Ensure that the UUT meets requirements and record actual amount of Prekey is received. 2.4.12 
Data Rate Communications Test Requirements 
 
(Section 2.2.4.1) 
Setup the equipment as shown above with the step attenuator setting of 50 dB. Use the PC to program each of the Squitter fields defined in Section 2.2.4.5.  Select an appropriate G
round Station Emulator frequency and initiate SPDU transmission to allow the HF Data Link to Log-on to the Ground Station Emulator.  Set the Ground Station Emulator and/or PC to display the contents of every downlink.  Verify that the maximum uplink data rate recommended by the UUT is 1800 b/s. Increase the step attenuator setting and input data to the UUT from the Message Generator to cause the UUT to transmit a downlink MPDU.  Repeat until the maximum data rate recommended is 1200 b/s, 600 b/s and 300 b/s as required per Section 2.2.4.1. 

 

2.4.13 
Selection of Downlink Slot by Aircraft Requirements 
 
(Section 2.2.4.2) 
 
Equipment Required 
 
 
Ground Station Emulator Power Attenuator, 80 dB, 200 watt average power Message Source, ISO-8208 Protocol Analyzer, or equivalent PC  
 
Protocol Analyzer - Avionics Specific; e.g. ARINC 429 
 
UUT 

Setup the equipment as shown in Figure 2.4-10. Use the PC to program each of the Squitter fields defined in Section 2.2.4.5.  Select an appropriate Ground Station Emulator frequency and initiate SPDU transmission to allow the HF Data Link to Log-on to the Ground Station Emulator. Use the PC to program the Ground Station Emulator to designate a number of slots as Random Access slots and assign one or no slots to the UUT to enable or disable slot acknowledgment depending on the outcome desired.  Input data to the UUT from the Message Source to cause the UUT to transmit a downlink MPDU.  Verify that the downlink is transmitted in a slot selected according to the requirements specified in Section 2.2.4.2. Repeat several times, each time changing the slot assignments or enabling/disabling slot acknowledgments, until testing of all requirements is covered. 

 

## 2.4.13.1 Transmit Slot Time Synchronization (Section 2.2.3.2.4) Test Procedures Time Slot Synchronization May Be Determined While Conducting The Slot Selection Test, 2.4.13.  Using The Test Setup In 2.4.13, Verify That The Uut Transmits W Ithin The Slot Boundaries As Defined In Section 2.2.3.2.4. 2.4.14 Maximum Mpdu Size Adjustment Test Requirements (Sections 2.2.4.3, 2.2.4.4) Equipment Required

  
 
UUT 
 
Ground Station Emulator 
 
Test Procedures 
Setup the equipment as shown in Figure 2.4-11.  Run script tests on the ground station emulator which address the requirements stated in Sections 2.2.4.3 and 2.2.4.4. 2.4.15 
Data Rate and Interleaver Selection Test Requirements 
 
(Sections 2.2.4.4 and 2.2.4.5) 
 
Equipment Required 
 
Ground Station Emulator. Emulator Power Attenuator, 80 dB, 200 watt average power Message Source, ISO-8208 Protocol Analyzer, or equivalent PC Protocol Analyzer - Avionics Specific; e.g. ARINC 429 
  
UUT 
 
 Setup the equipment as shown in Figure 2.4-12. Use the PC to program each of the Squitter fields defined in Section 2.2.4.5.  Select an appropriate Ground Station Emulator frequency and initiate SPDU transmission to allow the HF Data Link to Log-on to the Ground Station Emulator. 1.  
Use the PC to program the maximum downlink data rate recommended by the Ground Station Emulator to 1800 b/s.  Input data to the UUT from the Message Source to cause the UUT to transmit a downlink MPDU at 300 b/s using a single slot per the requirements specified in Section 2.2.4.4. Repeat step 1 using enough data from the Message Source to cause the UUT to transmit a downlink MPDU using a single slot at the higher data rates of 600, 1200 and 1800 b/s. 2. 

Use the PC to change the maximum downlink data rate recommended by the Ground Station Emulator to 1200 b/s. Input enough data to the UUT from the Message Source to cause the UUT to transmit a downlink MPDU at 1200 b/s using a double slot per the requirements specified in Section 2.2.4.4. Repeat above changing the maximum downlink data rate recommended by the Ground Station Emulator to 600 and 300 b/s. Input enough data from the Message Source to cause the UUT to transmit a downlink MPDU at 600 and 300 b/s, respectively, using a double slot. 

| 2.4.16                                                    | Squitter SPDU Format Test Requirements    |
|-----------------------------------------------------------|-------------------------------------------|
|                                                           | (Sections 2.2.4.5 and subsections )       |
|                                                           |                                           |
| Equipment Required                                        |                                           |
|                                                           |                                           |
|                                                           | Ground Station Emulator                   |
| Power Attenuator, 80 dB, 200 watt average power           |                                           |
| Message Source, ISO-8208 Protocol Analyzer, or equivalent |                                           |
| PC                                                        |                                           |
| Protocol Analyzer - Avionics Specific; e.g. ARINC 429     |                                           |
|                                                           | UUT                                       |
|                                                           |                                           |
| Test Procedures                                           |                                           |
|                                                           |                                           |
Setup the equipment as shown in Figure 2.4-13.  Use the PC to program each of the Squitter fields defined in Section 2.2.4.5.  Select an appropriate Ground Station Emulator frequency and initiate SPDU transmission to allow the HF Data Link to Log-on to the Ground Station Emulator.  Verify that the UUT Logs On. Use the PC to change the modifiable fields in the SPDU one field at a time.  Verify that the UUT reacts according to the requirements in Section 2.2.4.5 and subsections. 
2.4.17 
MPDU Packet Encapsulation Test Requirements 
 
(Sections 2.2.2, 2.2.4.6, 2.2.4.7 and subsections) 
 
Equipment Required 


Ground Station Emulator Power Attenuator, 80 dB to 150 dB, 120 W average power Message Source, ISO-8208 Protocol Analyzer, or equivalent PC  
Protocol Analyzer - Avionics Specific; e.g. ARINC 429  
 
UUT 
S O U R C E
Attenuator
P C
G S
Emulator

 Setup the equipment as shown in Figure 2.4-14. Use the PC to program each of the Squitter fields defined in Section 2.2.4.5.  Select an appropriate Ground Station Emulator frequency and initiate SPDU transmission to allow the UUT to Log-on to the Ground Station Emulator.  Verify that the UUT Logs On. Use the PC to change the slot assignments fields in the SPDU to uplinks to prevent any downlink transmissions from the UUT until ready. Input data of different priorities to the UUT from the Message Source. Use the PC to change the slot assignment field in the SPDU to uplinks to cause the UUT to transmit a downlink MPDU.  Display or store the downlink MPDU contents in the PC. Analyze the received MPDU packet contents for compliance with the requirements in Sections 2.2.2, 2.2.4.6, 2.2.4.7 and subsections. 2.4.18 
MPDU Format Test Requirements 
 
(Sections 2.2.4.5 and 2.2.4.7, and its subsections ) 
Equipment Required 

 
Ground Station Emulator 
Power Attenuator, 80 dB, 120 W average power Message Source, ISO-8208 Protocol Analyzer, or equivalent PC Protocol Analyzer - Avionics Specific; e.g. ARINC 429 UUT 
Test Procedures 
Power
U U T
M E S S A G E
S O U R C E
Attenuator
R F
P C
G S
Emulator
ISO 8208
A N A L Y Z E R Setup the equipment as shown in Figure 2.4-15. Use the PC to program each of the Squitter fields defined in Section 2.2.4.5.  Select an appropriate Ground Station Emulator frequency and initiate SPDU transmission to allow the UUT to Log-on to the Ground Station Emulator.  Verify that the UUT Logs On. Input data to the UUT from the Message Source to cause the UUT to transmit a downlink MPDU.  Display or store the downlink MPDU contents in the PC. Analyze the received MPDU packet contents for compliance with the requirements in Section 2.2.4.7 and subsections. 
2.4.19 
Packet Mode Data Services Test Requirements 
 
(Sections 2.2.5, 2.2.5.1, 2.2.5.2, 2.2.5.3, 2.2.5.4, 2.2.5.4.1, 2.2.5.4.2, 2.2.5.4.3) 
 
Equipment Required ISO-8208 Test Set/Protocol Analyzer (2), one designated as Protocol Analyzer Air 
(PAA), one designated as Protocol Analyzer Ground (PAG) 
Remote access equipment to ISO-8208 compatible data port at GS or, alternative, GS 
Emulator 
Appropriate cabling and antenna for access to the HF Data Link Subnetwork, or, 
alternatively,  
        Directional Coupler, 30 dB coupling, 150 watts average power rating High Power RF Load, 50 ohms, minimum 150 watts average power rating 
2.4.19.1 
Data 3/ATN/ISO-8208 Interfaces 
(Sections 2.2.5.2, 2.2.5.4.2) 
 
 
The  requirements established in 2.2.5.2, 2.2.5.4.2 concern the implementation of an ISO- 8208 compatible Data Circuit-terminating Equipment (DCE) interface on the digital side of the AS.  To verify the proper functionality of that interface, it is necessary to issue certain commands and analyze certain responses from both a simulated Data Terminal  

Equipment (DTE) external to the AS and from a corresponding simulated DTE external to the GS.  One means of verifying compliance would be to probe the radio-frequency emissions of the AS , back out the satellite-network signal-in-space, Layer 1 and Layer 2 and possible HF Data Link Subnetwork Dependent Protocols, and confirm transmission of the proper DCE-DCE message traffic.  This approach requires the ability to simulate the signal processing of the entire satellite network, including its ground terminals and gateways to the public and private networks.  This is a complex and expensive process. The same information can be obtained, however, by using the satellite network directly, and examining the data at the output of the GS.  The potential exists to remotely access this information so that the entire testing is performed in a closed loop from a single location, as shown in Figure 2.4-16. 

Note: Use of the Active HF Data Link Sub-Network for performance testing is subject to the restrictions identified in Section 2.4.2 of this document. 

 

## 2.4.19.1.1 Join And Leave Requirements (Section 2.2.5.4.3) Verify That A Join Event Message In Accordance With Section 2.2.5.4.3 Is Transmitted To The Routing Function Upon Determination Of Availability Of The Air/Ground Data Link. Similarly, Verify That A Leave Event Message Is Transmitted Upon Determination Of Non-Availability Of The Air/Ground Data Link. 2.4.19.1.2 Data 3 Mapping For Priority, Precedence And Preemption (Section 2.2.5.3) This Test Should Be Performed After Verifying Data 3 State Machine Operability In Accordance With 2.4.19.2 Below.

2.4.19.1.3 
Data 2 Transfer 
 
(Section 2.2.5.1) 
Equipment Required 


Ground Station Emulator.  This device is capable of emulating the behavior of a ground 
station.  This should be script driven to allow specific patterns of behavior to be repeated for each test.  This device should be capable of describing the behavior of the UUT so as to allow determination of pass / fail for each of the MOPS test for which it is used.  
 
Protocol Analyzer (Air) - Avionics Specific; i.e. CMU/MU Message Generator 
 
Protocol Analyzer (Ground) - Service Provider Specific; e.g. ARINC ACARS Host 
 
 
Test Procedure 
 
 
See Figure 2.4-16 for Test Setup. 
  
 
Air-to-Ground Data Transfer 
 
 
With the UUT logged-on send test data sequence of variable lengths and contents from the airborne message source. 
 
Verify that the UUT is able to transfer data between an airborne message source and the Ground Station Emulator in an air-to-ground direction. User messages should be correctly received by the Ground Station Emulator. 
 
Ground-to-Air Data Transfer With the UUT logged-on send test data sequence of variable lengths and contents from the ground message source. 

 
 
Verify that the UUT is able to transfer data between a ground message source at the Ground Station Emulator and the UUT in the ground-to-air direction. 

 
User-messages should be correctly received by the UUT. 

2.4.19.2 
HF Data Link Subnetwork  
 
2.4.19.2.1 
HF Data Link Subnetwork Dependent Protocol (Section 2.2.5.4) 
Experimental verification that the requirements of Section 2.2.5.4 have been met could require an inordinate amount of test time, due to the extremely small packet error rates permitted.  Therefore, compliance these requirements may be demonstrated by analysis or simulation of the protocols involved in reliable packet transmission. 

2.4.19.3 
Avionics Subnetwork Interface (Section 2.2.5) Equipment Required ISO-8208 Test Set/Protocol Analyzer (2), one designated as Protocol Analyzer Air 
(PAA), one designated as Protocol Analyzer Ground (PAG) 
Remote access equipment to ISO-8208 compatible data port at GS 
or, alternative, GS Emulator 
Appropriate cabling and antenna for access to the HF Data Link Subnetwork, 
or,  alternatively, Directional Coupler, 30 dB coupling, 20 watts average power rating 
 
High Power RF Load, 50 ohms, minimum 20 watts average power rating 
 
2.4.19.3.1 
ISO-8208 Protocol (Section 2.2.5) This section defines a succession of test procedures for a comprehensive logical state test for ISO-8208 DCE.  The tests are defined using the configuration illustrated in Figure 2.4-16.  For all test procedures, the transceiver is logged on to the GS.  The AS and the Protocol Analyzer (Air) exchange ISO-8208 packets, the AS and GS communicate via the satellite sub-network, and the GS and Protocol Analyzer (Ground) communicate via ISO-8208 packets.  Packet content will be monitored at both ends to confirm proper state transitions. The Use of ISO-8208 Default Parameters Unless otherwise specified, this procedure assumes that relevant parameters of the DTE/DCE interface are set to their standard default values as defined in ISO-8208. Note: These include, for example, packet sizes, flow control window sizes, timers 
and retry counters. Maintaining Flow Control Unless otherwise specified, the tester shall ensure that flow control is maintained across the transceiver/HLE interface through the use of RECEIVE READY packets, or DATA packets with updated PR/PS Subfields. Network Conditions Unless otherwise specified, the following test procedures assume that only one DTE will be connected to the transceiver during a given test.  Failure to observe this precaution may cause test results to differ from the expected values. Standard Test Signals The network protocol selected for the transceiver/HLE interface is ISO Standard 8208. 
Note: The manufacturer is free to choose the appropriate physical data bus for 
connection between the transceiver and the HLE.  Characteristics such as amplitude, timing, and waveform shapes of test signals applied to the transceiver shall be consistent with the standards definition of the selected 
data bus.  Moreover, the manufacturer should adhere to system impedance requirements of the appropriate standards whether the equipment under test has power applied or not, or is in an active or quiescent state (i.e., standby). 
 
General Characteristics - Transceiver/HLE Test Signals 
 
a. 
 Data Formats - Data transmitted across this interface shall be in packets  
 
 conforming to ISO Standard 8208. 
 
b. 
 Electrical Characteristics - Test signals on this interface shall be consistent with      

the appropriate standards for the connecting data bus. 
 
c. 
ISO-8208 Channel Assignments - The test procedures in this MOPS use 12 ISO 8208 channels in the range 2805 through 2816.  This assignment of channels is introduced as a documentation aid.  The manufacturer is free to choose any block of 12 ISO-8208 channels in the range 2565 through 2816 in a particular transceiver implementation. d. 
Data Content - The test equipment shall be capable of generating or accepting messages with the following content: packet fields such as sequence numbers, addresses, packet types or any other control fields shall be capable of being loaded with any combination of ones and zeros, including all ones and all zeros.  Data fields within the packets shall be capable of being loaded with any combination of ones and zeros, including all ones and all zeros. Message Validation The test equipment shall provide a means of validating the information content of any message received from the AS.  This requirement applies to either the AS /HLE interface or the GS/DTE interface. 
 
2.4.19.3.2 
Channel State Test Procedures (Section 2.2.5) 
 
The channel state test procedures are designed to test the restart, call setup and clearing, reset, interrupt, flow control and data transfer state tables of the transceiver.  The tests are divided into two subgroups: the Normal State Test Procedures and the Error Recovery State Test Procedures. 
 
Unless otherwise indicated, the tests all occur on one logical channel. 
2.4.19.3.3 
Normal State Test Procedures (Section 2.2.5) 
 
These procedures are designed to test the transceiver actions when receiving the logically correct ISO-8208 packets, from either interface, for the state of the logical channel.  A series of packets will be transferred across the transceiver interfaces to stimulate the logical states.  packets generated using the Protocol Analyzer (Ground) will arrive at the AS via the HF Data Link Subnetwork Protocol Data Units using the HF Data Link Subnetwork Dependent Protocol (SNDP).  Failure of these tests could be indicative of a failure to fully comply with the SNDP. 

2.4.19.3.4 
Call Setup and Clearing States (Section 2.2.5) Steps 1-3 must be performed sequentially. Step 1 - Virtual Call Setup from HLE Program the PAA to send an CALL REQUEST packet to the transceiver.  The use of NSAP addressing is optional.  Invoke the Expedited Data Negotiation Facility in the Optional ITU-T-specified DTE Facilities Field.  Use PAG to return a CALL ACCEPTED packet for the corresponding channel.  Use the PAA to verify that the AS generates the corresponding CALL CONNECTED packet with the correct fields. Step 2 - Data Transmission Program the PAA to send two DATA packets to the AS on the open channel.  Set the M-bit to zero on each of these DATA packets.   Maintain flow control for the channel, i.e. the PS Subfields for the first and second packet should be zero and one, respectively. Use a 32-bit User Data Field, and fill the Fields with alternate one-zero patterns. Verify that the DATA packets received in the proper order at the PAG.  After both DATA packets are accepted by the AS , verify that the AS sends a RECEIVE READY packet to the PAA. Step 3 - Clear Request Procedures from HLE Program the PAA to send a CLEAR REQUEST packet on the open channel to the AS. Verify that the AS returns a CLEAR CONFIRMATION packet to the HLE and sends a corresponding CLEAR INDICATION packet to the PAG.  Use the PAG to return a CLEAR CONFIRMATION packet.  Verify that there is no output on the transceiver/HLE interface. Steps 4-6 must be performed sequentially. Step 4 - Virtual Call Setup from PAG Program the PAG to send an CALL REQUEST packet to the AS.  The use of NSAP addressing is optional.  Invoke the Expedited Data Negotiation Facility in the Optional CCITT-specified DTE Facilities Field.  Use PAA to return a CALL ACCEPTED packet for the corresponding channel.  Use the PAG to verify that the AS generates the corresponding CALL CONNECTED packet with the correct fields. Step 5 - Data Transfer from the PAG Program the PAG to send two DATA packets to the AS on the open channel.  Set the M-bit to zero on each of these DATA packets.   Maintain flow control for the channel, i.e. the PS Subfields for the first and second packet should be zero and one, respectively. Use a 32-bit User Data Field, and fill the Fields with alternate one-zero patterns. Verify that the DATA packets received in the proper order at the PAA.  After both DATA packets are accepted by the AS, verify that the AS sends a RECEIVE READY packet to the PAG. Step 6 - Ground DTE Requests to Clear the Channel Program the PAG to send a CLEAR REQUEST packet on the open channel to the AS. Verify that the AS returns a CLEAR CONFIRMATION packet to the PAG and sends a corresponding CLEAR INDICATION packet to the PAA.  Use the PAA to return a CLEAR CONFIRMATION packet.  Verify that there is no output on the PAG interface. Steps 7-12 can be performed in any order, if desired. Step 7 - HLE Aborts a Call Request Program the PAA to send a CALL REQUEST packet to the transceiver.  Use the PAG to verify that the CALL REQUEST packet is output to the ground DTE.  Have the PAA send a CLEAR REQUEST packet for that channel to the transceiver.  Use the PAA to verify that the AS returns a CLEAR CONFIRMATION packet to the HLE.  Use the PAG to verify the Clearing and Diagnostic Cause Fields in the corresponding CLEAR INDICATION packet and to return a CLEAR CONFIRMATION packet.  Verify that there is no corresponding output at the transceiver/HLE interface. Step 8 - GS Aborts a Call Request Program the PAG to send a CALL REQUEST packet to the AS.  Use the PAA to verify that the CALL REQUEST packet is output from the AS.  Have the PAG send a CLEAR REQUEST packet for that channel to the transceiver.  Use the PAG to verify that the AS returns a CLEAR CONFIRMATION packet to GS.  Use the PAA to verify the Clearing and Diagnostic Cause Fields in the corresponding CLEAR INDICATION packet and to return a CLEAR CONFIRMATION packet.  Verify that there is no corresponding output at the PAG. Step 9 - GS rejects a Call Request Program the PAA to send a CALL REQUEST  Packet.  Use the PAG to verify that a CALL REQUEST packet is produced by the GS, and to return a CLEAR REQUEST packet the GS.  Verify that the GS returns a CLEAR CONFIRMATION packet to the PAG.  Use the PAA to verify that the CLEAR INDICATION packet is output from AS, and to send a CLEAR CONFIRMATION packet back to the GS.  Verify that there is no corresponding output to the PAG. 

Step 10 - HLE Rejects a Call Request 
 
Program the PAG to send a CALL REQUEST  Packet.  Use the PAA to verify that a CALL REQUEST packet is produced by the transceiver, and to return a CLEAR 
REQUEST packet to transceiver.  Verify that the AS returns a CLEAR CONFIRMATION packet to the HLE.  Use the PAG to verify that the CLEAR INDICATION packet is output from the ground entity, and to send a CLEAR CONFIRMATION packet back to the AS.  Verify that there is no corresponding output to the PAA. 

 
Step 11 - CLEAR REQUEST packet for a Channel in the Ready State (p1)  
 
Program the PAA to send a CLEAR REQUEST packet to the transceiver.  Verify that the AS returns a CLEAR CONFIRMATION packet. 

 
Step 12 - Call Collision Program the PAG to send a CALL REQUEST packet to the AS.  Verify that the AS forwards an INCOMING CALL packet to the HLE.  Program the PAA to return a CALL REQUEST packet to the AS with the same channel number.  Verify that the AS forwards a CLEAR INDICATION packet to the PAG   Packet, followed by a CALL REQUEST packet to the PAG. 

 
Step 13 - Clear Channels Perform the procedures in Step 3, to clear the channels used in Step 12. At this point, there are no active communications channels. 2.4.19.3.5 
Restart Request States (Section 2.2.5) Steps 1 and 2 must be performed sequentially. Step 1 - DTE Restart Procedures Perform the procedure in Section 2.4.19.3.4, Call Setup and Clearing States Step 1 to open two channels.  Program the PAA to send a RESTART REQUEST packet to the AS.  Verify the RESTART CONFIRMATION packet is returned from the AS to the PAA.  Use the PAG to verify that the AS sends a CLEAR INDICATION  Packet to the GS for each channel not in the p1 State.  Program the PAG to send the corresponding CLEAR CONFIRMATION packet to the AS.  Verify that there is no corresponding output at the PAA. 

 
At this point, the channels have been cleared. Step 2 - DCE Restart Procedures Without changing the system state from that produced in Step 1, program the PAA to send a RESTART CONFIRMATION packet to the AS.  Use the PAA to verify that the AS will return a RESTART INDICATION packet to the HLE with diagnostic code set to 17.  Program the PAA to return a RESTART CONFIRMATION packet to the transceiver.  Verify that there is no corresponding output at the AS interfaces. Step 2 is a *negative* test, i.e., it assures robust operation in the face of an unexpected input during a restart operation. 

2.4.19.3.6 
Reset States (Section 2.2.5) Step 1 - Reset Procedures by HLE Perform the procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 1 and Step 2.  Program the PAA to send a RESET REQUEST packet on the open channel to the transceiver.  Verify that the AS returns a RESET CONFIRMATION packet to the HLE.  Use the PAG to verify that the RESET INDICATION packet sent from the AS contains the appropriate Resetting and Diagnostic Cause Fields.  Program the PAG to send RESET CONFIRM packet.  Verify that there is no corresponding output at the transceiver/HLE interface. Step 2 - Reserved Step 2 is not used at this time. Step 3 - Reset Procedure from GS. Perform the procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 1 and Step 2.  Program the PAG to send a RESET REQUEST packet on the open channel to the transceiver.  Verify that the GS returns a RESET CONFIRMATION packet to the PAG.  Use the PAA to verify that the RESET INDICATION packet sent from the GS contains the appropriate Resetting and Diagnostic Cause Fields.  Program the PAA to send RESET CONFIRM packet.  Verify that there is no corresponding output at the transceiver/HLE interface. Step 4 - Reset Request from GS.  HLE responds with a RESET REQUEST packet. Program the PAG to send a RESET REQUEST  Packet on the open channel to the AS. Verify that the AS returns a RESET CONFIRM packet to the PAG and transmits the corresponding RESET INDICATION packet with the appropriate Diagnostic and Resetting Fields to the HLE.  Use the PAA to return a RESET REQUEST packet to the AS.  Use the PAG to verify that there is no corresponding output at the GS/DTE interface. Step 4 is a *negative* test, in that it tests an *incorrect* response of RESET REQUEST from the PAA. 

Step 5 - Clear Opened Channel Perform the clear request procedure in Perform the procedure in Section 2.4.19.3.4, Call Setup and Clearing States Step 3. 

 
2.4.19.3.7 
Interrupt Transfer States (Section 2.2.5) Steps 1-4 must be performed sequentially. Step 1 - Virtual Call Setup Perform the call setup procedure in Section 2.4.19.3.4, Call Setup and Clearing States Call Setup and Clearing States, Step 1. Step 2 - Interrupt packet from the HLE Program the PAA to send a DATA packet to the AS.  Set M-bit to one.  User Data Field contains 128 octets, the value of each byte increments from 0 to 127.  Program the PAA to send an INTERRUPT packet with a 32-bit User Data Field containing a bit pattern of alternating one's and zero's, and another DATA packet with M-bit set to zero.  Use the PAG to verify that the corresponding INTERRUPT DATA packet is not the last packet sent from the AS.  Also, verify content and length of the User Data Fields.  Use the PAG to send an INTERRUPT CONFIRMATION packet.  Verify the INTERRUPT CONFIRMATION packet at the PAA. Step 3 - Interrupt packet from the GS. Program the PAG to transmit the following packets to the transceiver: a DATA packet with M
-bit set to one and L*SNDP*   octets of User Data, an INTERRUPT DATA packet with 32 octets of User Data, and a second DATA packet that has the M-bit set to zero. Use the PAA to verify that the AS forwards the corresponding ISO-8208 INTERRUPT packet followed by the ISO-8208 M-bit sequence.  Program the PAA to return an INTERRUPT CONFIRMATION packet to the AS.  Verify the corresponding INTERRUPT CONFIRMATION packet at the PAG. Step 4 - Clear Opened Channel Perform the procedure in Section 2.4.19.3.4, Call Setup and Clearing States Step 3 to clear the open channel. 

2.4.19.3.8 
Error Recovery Procedures (Section 2.2.5) The Error Recovery State Test Procedures are designed to test the capability of the AS to recover from erroneous packets received over the transceiver/HLE or transceiver/GS interface.  A series of ISO-8208 packets will be transferred across the AS boundaries to stimulate the logical states.  Unless otherwise noted, all tests occur on a single logical channel. 

2.4.19.3.9 
DCE Call Setup and Clearing States (Section 2.2.5) Step 1 - Ready State (p1) This test verifies the DCE p1 State. a. 
Program the PAA to send a CALL ACCEPTED packet to the AS.  Verify that the AS returns to the HLE a CLEAR INDICATION packet with diagnostic code set to 20.  Program the PAA to return a CLEAR CONFIRMATION packet to the AS. Verify there is no corresponding output on the PAG. b. 
Perform the procedure in Step 1a replacing the CALL ACCEPTED packet sent to the AS with each of the following packets: RESET REQUEST, CLEAR CONFIRMATION, RESET CONFIRMATION, DATA, INTERRUPT, RECEIVE READY and RECEIVE NOT READY.  Verify the results as in Step 1a. c. 
Program the PAA to send a RESTART REQUEST packet to the AS with channel number not equal to zero.  Verify that the AS sends a CLEAR INDICATION packet to the HLE with diagnostic code set to 41.  Program the PAA to return a CLEAR CONFIRMATION packet to the AS.  Verify that there is no corresponding output on the PAG. d. 
Perform the procedure in Step 1a, replacing the CALL ACCEPTED packet sent to the AS with an ISO-8208 packet having a packet type identifier shorter than one byte.  Verify that the diagnostic code is set to 38 in the CLEAR INDICATION packet. 
 
 
e. 
Perform the procedure in Step 1a, replacing the CALL ACCEPTED packet sent to the AS with an ISO-8208 packet having a packet type identifier which is undefined or not supported.  Verify that the AS returns a CLEAR INDICATION packet with diagnostic code set to 33. Step 2 - DTE Call Request State (p2) This test verifies the DCE p2 State. a. 
 Program the PAA to send a CALL REQUEST packet to the AS.  Use the PAG to 
verify that the AS sends a INCOMING CALL  Packet to the PAG. b. 
Program the PAA to send a RESET REQUEST packet on the same channel to the AS.  Verify that the AS generates a CLEAR INDICATION packet to the PAA and a CLEAR INDICATION packet to the PAG with diagnostic codes set to 21. Program the PAA to return a CLEAR CONFIRMATION packet and the PAG to return a CLEAR CONFIRMATION packet to the AS. c. 
Perform the procedures in Steps 2a and 2b, replacing the RESET REQUEST packet sent to the AS in procedure 2b with each of the following ISO-8208 packets: 
CALL REQUEST, CALL ACCEPTED, CLEAR CONFIRMATION, DATA, INTERRUPT, RECEIVE READY and RECEIVE NOT READY.  The Logical Channel Number should remain the same for all test packets.  Verify the results as in Step 2b. 


d. 
Perform the procedures in Steps 2a and 2b, replacing the RESET REQUEST packet sent to the AS in procedure 2b with an ISO-8208 packet having a packet type identifier shorter than one byte.  Verify that the diagnostic code is set to 38 in the CLEAR INDICATION packets. e. 
Perform the procedures Steps 2a and 2b, replacing the RESET REQUEST packet sent to the AS in procedure 2b with an ISO-8208 packet having a packet type identifier which is undefined or not supported.  Verify that the diagnostic code is set to 33 in the CLEAR INDICATION packets. f. 
Perform the procedures in Steps 2a and 2b, replacing the RESET REQUEST packet sent to the AS in procedure 2b with an RESTART REQUEST packet or a RESTART CONFIRMATION packet with a logical channel number not equal to zero.  Verify that the diagnostic code is set to 41 in the CLEAR INDICATION packets. Step 3 - DCE Call Request State (p3) This test verifies the DCE p3 State. a. 
Program the PAG to send CALL REQUEST packet to the AS.  Verify the 
 
INCOMING CALL packet. b. 
Program the PAA to send a RESET REQUEST packet on the same channel to the AS.  Verify that the AS sends a CLEAR INDICATION packet to the HLE and a CLEAR INDICATION packet to the PAG with diagnostic codes set to 22. Program the PAA to send a CLEAR CONFIRMATION packet to the transceiver, and program the PAG to send a CLEAR CONFIRMATION packet to the AS. Verify that there is no corresponding output at the PAA  or  PAG. c. 
Perform the procedures in Steps 3a and 3b five times.  For each iteration replace the RESET REQUEST packet sent to the AS in Step 3b with one of the following packets: CLEAR CONFIRMATION, DATA, RECEIVE READY, RECEIVE NOT READY and INTERRUPT.  Verify the results as in Step 3b. d. 
Perform the procedures in Steps 3a and 3b, replacing the RESET REQUEST packet sent to the AS in Step 3b with an ISO-8208 packet having a packet Type Identifier shorter than one byte.  Verify that the diagnostic code is set to 38. e. 
Perform the procedures in Steps 3a and 3b, replacing the RESET REQUEST packet sent to the AS in Step 3b with an ISO-8208 packet having a packet Type Identifier which is undefined or not supported.  Verify that the diagnostic code is set to 33. 
 
f. 
Perform the procedures in Steps 3a and 3b, replacing the RESET REQUEST packet sent to the AS in Step 3b with a RESTART REQUEST packet with the logical channel identifier not equal to zero.  Verify that the diagnostic code is set to 41. 
 
Step 4 - Data Transfer State (p4) This test verifies the DCE p4 State. a. 
Perform the procedure in Section 2.4.19.3.4, Call Setup and Clearing States Call  
 
Setup and Clearing States, Step 1. b. 
Program the PAA to send a CALL REQUEST packet on the open channel to the AS.  Verify that the AS sends a CLEAR INDICATION packet and a CLEAR INDICATION packets to the PAA and PAG with diagnostic codes set to 23.  Bit eight of the Clearing Cause Field should be set to zero because the error originated at the DTE/DCE interface.  Program the PAA to return a CLEAR CONFIRMATION packet, and program the PAG to send a CLEAR INDICATION to the transceiver.  Verify that neither confirmation appears in the other interface. c. 
Perform the procedures in Steps 4a and Step 4b two times.  For the first iteration replace the CALL REQUEST packet sent to the AS with a CALL ACCEPTED packet.  For the second iteration, replace the CALL REQUEST packet sent to the AS with a CLEAR CONFIRMATION packet.  Verify the results as in Step 4b. Step 5 - Call Collision State (p5) The error recovery procedure for the Call Collision (p5) State is transitory and therefore is not tested. Step 6 - Clear Request by DTE State (p6) The error recovery procedure for the Clear Request by DTE (p6) State is transitory and therefore is not tested. Step 7 - DCE Clear to DTE State (p7) This test verifies the DCE p7 State. 
 
 
a. 
Perform the call setup procedure in Step 2a. b. 
Program the PAA to send a RESET REQUEST packet on the same channel to the AS.  Verify that the AS generates a CLEAR INDICATION packets to the PAA and PAG.  Both packets should have the  with diagnostic code set to 21. 


c. 
Program the PAA to send a CALL ACCEPTED packet to the AS.  Verify that the  
 
packet is discarded. 
 
d. 
Perform the procedure in Step 7c five times.  For each iteration, replace the CALL ACCEPTED packet sent to the AS with one of the following packets:  DATA, INTERRUPT, RECEIVE READY, RECEIVE NOT READY and RESET REQUEST.  Verify that the packets are discarded. e. 
Perform the procedure in Step 7c, replacing the CALL ACCEPTED packet sent to the AS with an ISO-8208 packet having a packet Type Identifier which is undefined or not supported. f. 
Perform the procedure in Step 7c, replacing the CALL ACCEPTED packet sent to the AS with an ISO-8208 packet having a packet Type Identifier shorter than one byte. g. 
Program the PAA to send a CLEAR CONFIRMATION packet to the AS.  
Program  
the PAG to return a CLEAR CONFIRMATION packet to the AS.  Verify that there is no corresponding output at that AS interfaces. 
 
2.4.19.3.10 
DCE Restart States (Section 2.2.5) Step 1 - Packet Level Ready State (r1) This test verifies the DCE r1 State. a. 
Program the PAA to send a CALL REQUEST packet to the AS with a channel number equal to zero.  Verify that the AS sends a DIAGNOSTIC packet to the PAA with diagnostic code set to 36, and that the Diagnostic Cause Field contains the first three octets of the CALL REQUEST packet. b. 
Program the PAA to send a RESTART REQUEST packet with a format error to the AS.  Verify that the AS returns a DIAGNOSTIC packet to the HLE with diagnostic code set to either 38, 39, 81 or 82, and the Diagnostic Cause Field contains the first three octets of the RESTART REQUEST packet. c. 
Program the PAA to send a RESTART CONFIRMATION packet to the AS.   
 
Verify that the AS returns a RESTART INDICATION packet to the HLE with  
 
 
diagnostic code set to 17. d. 
Program the PAA to send a RESTART CONFIRMATION packet to the AS.  The 
 
 
AS enters the r1 State. Step 2 - DTE Restart Request State (r2) The DTE Restart Request State (r2) error recovery procedure is transitory and therefore is not tested. 
Step 3 - DCE Restart Request State (r3) This test verifies the DCE r3 State. a. 
Perform again the procedure in Step 1d.  The AS enters the r3 State. b. 
Perform the procedure in Step 1a. c.      Program the PAA to send a RESTART REQUEST packet with format error to the  
AS.  Verify that the AS returns a RESTART INDICATION packet to the HLE with diagnostic code set to either 38, 39, 81, or 82. 
d. 
Perform the procedure in Step 1d. Step 4 - DCE Special Cases a. 
Program the PAA to send an ISO-8208 packet to the AS that is less than two octets in length.  Verify that the AS returns a DIAGNOSTIC packet to the PAA with the Diagnostic Code Field set to 38.  Also, verify the Diagnostic Cause Field. b. 
Program the PAA to send a CALL REQUEST packet to the AS with a invalid General Format Identifier Field.  Verify the AS returns a DIAGNOSTIC packet to the HLE with the Diagnostic Code Field set to 40.  Also, verify the Diagnostic Cause Field. 
 
2.4.19.3.11 
DCE Reset States (Section 2.2.5) Step 1 - Erroneous ISO-8208 packets for the Flow Control Ready State (d1) This test verifies the DCE d1 State. a. 
Perform the call setup procedure in Section 2.4.19.3.4, Call Setup and Clearing 
 
States Step 1. b. 
Program the test set to send a RESTART REQUEST packet to the transceiver with a logical channel identifier unequal to zero on the open channel.  Verify that the transceiver sends a RESET INDICATION packet to the HLE and a RESET INDICATION packet to the PAG with diagnostic codes set to 41. c. 
Program the test set to send a RESET CONFIRMATION packet and the PAG to  
 
send a RESET CONFIRMATION packet to the transceiver. d. 
Perform the procedures in Steps 1b and 1c.  For this iteration, replace the RESTART REQUEST packet the transceiver in Step 1b with a packet having an invalid packet Type Identifier shorter than one byte.  Verify that the diagnostic codes are set to 38 in the corresponding RESET CONFIRMATION packets at the HLE and PAG. e. 
Perform the procedures in Steps 1b and Step 1c.  For this iteration, replace the  
RESTART REQUEST packet with a packet having a packet Type Identifier which is undefined.  Verify that the diagnostic codes are set to 33 in the corresponding RESET INDICATION packets sent to the HLE and the PAG. 
 
f. 
Perform the Clear Request procedure in Section 2.4.19.3.4 Call Setup and Clearing  
 
States Step 3. Step 2 - Reset Request by DTE (d2) The DTE Reset Request (d2) State error recovery procedure is transitory and therefore is not tested. Step 3 - Reset Request by DCE to DTE (d3) This test verifies the DCE d3 State. a. 
Perform the call setup procedure in Section 2.4.19.3.4 Call Setup and Clearing  
 
 
States Step 1. b. 
Program the PAA to send a RESET CONFIRMATION packet on the opened channel to the transceiver.  Verify that the transceiver sends a RESET INDICATION packet to the PAA and a RESET CONFIRMATION packet to the PAG with diagnostic codes set to 27. c. 
Program the PAA to return an INTERRUPT packet to the AS.  Verify that there is  
 
no corresponding output. d. 
Perform the procedure in Step 3c, replacing the INTERRUPT packet sent to the AS in Step 3c with each of the following ISO-8208 packets: INTERRUPT CONFIRMATION, RESTART REQUEST with channel number not equal to zero, DATA, RECEIVE READY, RECEIVE NOT READY, REJECT, a packet having a packet Type Identifier shorter than one byte, and a packet having a packet Type Identifier which is undefined.  Program the PAA to send a RESET CONFIRMATION packet and the PAG to send a RESET CONFIRMATION packet to the AS.  Verify the results as in 3c. e. 
Perform the clear request procedure in Section 2.4.19.3.4 Call Setup and Clearing 
 
States Step 3. 
 
2.4.19.3.12 
DCE Flow Control Transfer States (Section 2.2.5) Step 1 - DCE Receive Ready State (f1) This test verifies the DCE f1 State. a. 
Perform the call setup procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 1. b. 
Program the PAA to send a DATA packet that contains an invalid PS Field.  Verify that the AS sends a RESET INDICATION packet to the PAA and a RESET INDICATION packet to the PAG with diagnostic codes set to one.  Program the 
PAA to return a RESET CONFIRMATION packet to the AS and the PAG to return a RESET CONFIRMATION packet. c. 
Program the PAA to send a DATA packet to the AS that contains an invalid PR. Verify that the AS sends a RESET INDICATION packet to the PAA and a RESET INDICATION packet to the PAG, with diagnostic codes set to two. d. 
Perform the reset confirmation procedure in Step 1b. e. 
Perform the procedures in Steps 1c and 1d.  Replace the DATA packet sent to the AS in Step 1c with a DATA packet that has M
-bit set to one and a partially full 
User Data Field.  Verify that the diagnostic codes are equal to 165 or 166. f. 
Perform the clear request procedure in 2.4.19.3.4 Call Setup and Clearing States Step 3. Step 2 - DCE Receive Not Ready (f2) This test verifies the DCE f2 State. a. 
Perform the call setup procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 1. b. 
Program the PAG to send a FLOW CONTROL (Suspend) packet. c. 
Program the PAA to send DATA packets to the AS until the AS returns a RECEIVE NOT READY packet to the HLE. d. 
Verify that the AS will discard the following ISO-8208 packets sent from the PAA: DATA packet with a valid PR but an invalid PS, a valid DATA packet and a DATA packet that has M-bit set to one and a partially full User Data Field. e. 
Perform the procedure in Step 1c.  Verify the results. f. 
Perform the reset confirmation procedure in Step 1b. g. 
Perform the clear request procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3. Step 3 - DTE Receive Ready (g1) This test verifies the DTE g1 State. 
a. 
Perform the call setup procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 1. b. 
Program the PAA to send a RECEIVE READY packet with a invalid PR Field to 
the AS.  Verify that the AS sends a RESET INDICATION packet to the PAA and a RESET INDICATION packet to the PAG with diagnostic codes set to two. c. 
Perform the reset confirmation procedure in Step 1b. d. 
Perform the procedures in Steps 3b and Step 3c two times.  For the first iteration, replace the RECEIVE READY packet sent to the AS in Step 3b with a RECEIVE NOT READY packet.  For the second iteration, replace the RECEIVE READY packet sent to the AS in Step 3b with a REJECT packet.  Verify the results as in 3b. e. 
Perform the Clear Request procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3. 
Step 4 - DTE Receive Not Ready (g2) This test verifies the DTE g2 State. a. 
Perform the call setup procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 1. b. 
Program the PAA to send a RECEIVE NOT READY packet to the AS. c. 
Perform the procedures in Steps 3b, 3c, 4b, and 3d. d. 
Perform the clear request procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3. 
 
2.4.19.3.13 
DCE Interrupt Transfer States (Section 2.2.5) Step 1 - DTE Interrupt Sent State (i2) This test verifies the DCE i2 State. a.  
Perform the call setup procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 1. b. 
Program the PAA to send an INTERRUPT packet to the AS.  Use the PAG to verify that the AS sends a INTERRUPT DATA packet to the PAG.  Program the PAA to send another INTERRUPT packet on the same channel to the AS. c. 
Verify that the AS sends a RESET INDICATION packet to the PAG and a RESET INDICATION packet to the PAA with diagnostic codes set to 44. d. 
Perform the reset confirmation procedure in Section 2.4.19.3.12 Step 1b. e. 
Perform the procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3 to clear an open channel. 
 
Step 2 - DCE Interrupt Ready State (j1) This test verifies the DCE j1 State. a. 
Perform the procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 1 to open a channel. b. 
Program the PAA to send an INTERRUPT CONFIRMATION packet to the AS. c. 
Verify that the AS sends a RESET INDICATION packet to the PAG and a RESET INDICATION packet to the HLE with diagnostic codes set to 43. d. 
Perform the reset confirmation procedure in Section 2.4.19.3.12  Step 1b. e. 
Perform the procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3 to clear a channel. 
 
2.4.19.3.14 
Packet Assembly (Section 2.2.5) The packet assembly test procedures are designed to test the AS's ability to assemble and disassemble ISO-8208 packets.  These tests also verify SNDP operation, since the confirmations are monitored at the far end of the sub-network. The M-bit linking test procedures are designed to verify the AS's ability to combine User Data Fields of packets to form a larger packet and also to determine how the User Data Field of a packet can be subdivided to form smaller packets. Messages will be 138 octets long each containing a unique bit pattern to be sent on separate logical channels. Use the PAA to perform the HLE functions, and use the PAG and PAG to perform the PAG functions. 
 
Step 1 - Virtual Call Setup This test opens multiple channels with the AS. a.  
Program the PAA to send four CALL REQUEST packets to the AS with the following channel numbers: 2816, 2815, 2814, and 2813.  Use the PAG to verify that the PAG receives INCOMING CALL packets with the four distinct logical channel numbers. 
 
b. 
Program the PAG to send four CALL ACCEPTED packets to the AS.  Verify that the AS sends four CALL CONNECTED packets to the PAA with the following channel numbers: 2816, 2815, 2814, and 2813. 
 
Step 2 - M-bit Linking DATA packets from Data packets Step 2 - DATA packets from Data packets 
 
This test verifies proper ordering of messages according to the link layer precedence of the data packets arriving at the AS. 
 
a.  
Program the PAA to send an ISO 8208 M-bit sequence, message, consisting of four 
DATA packets, time sequence in the following order:  2813, 2816, 2815, 2814, each with 128+10 octets of data in the User Data field on each opened channel to the AS. Fill the User Data Field of each message with following patterns: 
 
channel 2816   01010101 


channel 2815   10101010  


channel 2814   11001100  


channel 2813   00110011  
 
 
These packets shall be sent to the AS ISO-8208 interface at the maximum rate supported by the external interface hardware. 
 
 
Note: Like the equivalent tests in DO-210D, this test implicitly assumes that 
the external I/O bandwidth significantly exceeds the HF Data Link network bandwidth available to any single AS for packet data operations.  If such is not the case, priority, precedence and preemption mechanisms must be supplied at the external I/O controller, effectively overriding AS mechanisms.  
  
b. 
Use the PAG to verify that the AS sends data packets awaiting transmission over the HF Data Link in accordance with the data packet precedence with User Data Fields contents as follows. 
 
channel 2813 
00110011 
 
 
channel 2816 
01010101 
 
 
channel 2816 
01010101 
 
 
channel 2815 
10101010 
 
 
channel 2815 
10101010 
 
 
channel 2814 
11001100 
 
 
channel 2814 
11001100 
 
 
channel 2813 
00110011 
 
Verify that each of the first DATA packets contain 128 octets of the User Data Field and has M-bit set to one. Verify that the second packet for each channel contains ten octets 
of the User Data Field and has M
-bit set to zero. Also verify that the User Data Field 
content corresponds with logical channels defined in Step a. 
 
Step 3 - DATA packets from the PAG This test verifies ISO-8208 packet assembly procedures in the AS. a. 
Program the PAG to send a sequence of two DATA packets to the AS for each opened channel.  The first DATA packet for each channel should have the M-bit set to one.  All DATA packets in each sequence should contain 128 octets of the User Data Field listed below. 
 
channel 2816 01010101 
 
 
channel 2815 10101010 
 
 
channel 2814 11001100 
 
 
channel 2813 00110011 
 
b. 
Verify that the AS sends the correct number, n, of packets on each opened channel to the PAA. Also verify that the first *n-1* DATA packets for each channel have the M-bit set to one and contain 128 octets of User Data Field listed below, and the final packet for each channel shall have M
-bit set to zero and remaining octets of user 
data. 


channel 2816  01010101 
 
 
channel 2815  10101010 
 
 
channel 2814  11001100 
 
 
channel 2813  00110011 Step 4 - Clear Channels a. 
Program the PAA to send four CLEAR REQUEST packets to the AS on channels 2816, 2815, 2814, and 2813.  Use the PAG to verify that the AS sends four CLEAR INDICATION packets to the PAG.  Use the PAA to verify that the AS returns a CLEAR CONFIRMATION packet to the HLE on each channel (2816, 2815, 2814, and 2813). b. 
Program the PAG to return four CLEAR CONFIRMATION packets on the corresponding channels to the AS.  Perform the procedure in Section 2.4.19.3.4, Call Setup and Clearing States Step 3 to clear the four open channels. 
 
2.4.19.3.15 
Call Setup and Maintenance (Section 2.2.5) The Call Setup and Maintenance test procedures are designed to test the AS's ability to process various requests for Virtual Call Setup.  The tests are divided into five subgroups: Fast Select, Called and Calling Address (NSAP) Extension, Throughput Class Negotiation, Transit Delay Selection and Indication, and Priority. 
2.4.19.1.16 
Fast Select Facilities (Section 2.2.5) The Fast Select test procedures are designed to test the AS's ability to process the Fast Select Facility request without restrictions.  The ISO-8208 Fast Select Facility with restrictions is not used by ATN. Step 1 - CALL REQUEST packet with Fast Select from the HLE This test verifies the AS's ability to process a Fast Select request from the HLE. a. 
Program the PAA to send a CALL REQUEST packet to the AS with the Facilities Field containing a Fast Select request with no restriction on response.  Fill the User Data Field with 128 octets of the bit pattern 01010101. 


b. 
Use the PAG to verify that the AS transmits the related INCOMING CALL packet to the PAG containing a Fast Select request with no restriction on response.  Verify the User Data Field for content and length as established in Step 1a. 
c. 
Program the PAG to send a CALL ACCEPTED packet to the AS.  Fill the User 
Data Field with 128 octets of the bit pattern 10101010.  Verify that the AS sends the related CALL CONNECTED packet to the PAA with the correct User Data Field. 
 
d. 
Program the PAA to send a DATA packet to the AS with a User Data Field of four octets of 00110011.  Verify that the GES sends the correct DATA packet to the PAG. e. 
Program the PAG to send a DATA packet to the AS with a User Data Field of eight octets of 11110000.  Verify that the AS sends the correct DATA packet to the PAA. f. 
Program the PAA to send a CLEAR REQUEST with a Clear User Data field with 128 octets of the bit pattern 11001100 to the GES.  Verify that the GES generates the associated CLEAR INDICATION containing the proper data. g. 
Program the PAA to send the requisite  CLEAR CONFIRMATION packet is sent to the GES, and verify that CLEAR CONFIRMATION is output from the AS. Step 2 - CALL REQUEST packet with Fast Select from the PAG This test verifies the AS's ability to process a Fast Select request from the PAG. a. 
Program the PAG to send a CALL REQUEST packet to the AS with the Facilities Field containing a Fast Select request with no restriction on response.  Fill the User Data Field with 128 octets of the bit pattern 01010101. b. 
Use the PAA to verify that the AS transmits the related INCOMING CALL packet to the PAA containing a Fast Select request with no restriction on response.  Verify the User Data Field for content and length as established in Step 1a. c. 
Program the PAA to send a CALL ACCEPTED packet to the AS.  Fill the User Data Field with 128 octets of the bit pattern 10101010.  Verify that the AS sends the related CALL CONNECTED packet to the PAG with the correct User Data Field. 
 
d. 
Program the PAG to send a DATA packet to the GES with a User Data Field of four octets of 00110011.  Verify that the AS sends the correct DATA packet to the PAA. e. 
Program the PAA to send a DATA packet to the GES with a User Data Field of eight octets of 11110000.  Verify that the GES sends the correct DATA packet to the PAG. 
 
f. 

Program the PAG to send a CLEAR REQUEST with a Clear User Data field with 128 octets of the bit pattern 11001100 to the AS.  Verify that the AS generates the associated CLEAR INDICATION containing the proper data. 

 
g. 

Program the PAG to send the requisite CLEAR CONFIRMATION packet is sent to the AS, and verify that CLEAR CONFIRMATION is output from the GES. 

 
2.4.19.3.17 
Called and Calling Address Extension (NSAP) Test (Section 2.2.5) The Called and Calling Address Extension (NSAP) tests are d esigned to test the AS's ability to process packets which contain the NSAP addressing scheme. Step 1 - Call Request from PAA Program the PAA to send a CALL REQUEST packet to the AS. Fill the Facilities Field with the following facilities: Calling Address Extension Facility, and Called Address Extension Facility.  Use the PAG to verify that the AS transmits a corresponding CALL INDICATION packet to the PAG, and that the NSAP addresses have been transparently transferred. Step 2 - Call Accept from the PAG Program the PAG to return a CALL ACCEPTED packet to the AS without the Responding NSAP Address Field from the request in Step 1.  Use the PAA to verify that the AS transmits the corresponding CALL CONNECTED packet with the same called NSAP address that was in the original CALL REQUEST packet. Step 3 - Clear Request Procedures This test clears the open channel. Program the PAA to send a CLEAR REQUEST packet to the AS.  Use the PAG to verify that the AS transmits the corresponding CLEAR INDICATION packet t o the PAG.  Use the PAG to return the corresponding CLEAR 
CONFIRMATION 
packet to the AS. 

 
Verify the corresponding CLEAR 
CONFIRMATION packet. Step 4 - CALL REQUEST from PAG Program the PAG to send a CALL REQUEST packet to the AS. Fill the Facilities Field with the following facilities: Calling Address Extension Facility, and Called Address Extension Facility.  Use the PAA to verify that the AS outputs a corresponding CALL INDICATION packet to its HLE, and that the NSAP addresses have been transparently transferred. Step 5 - CALL ACCEPT from PAA Program the PAA to return a CALL ACCEPTED packet to the AS without the Responding NSAP Address Field from the request in Step 1 . Use the PAG to verify that the AS transmits the corresponding CALL CONNECTED packet to the PAG with the same called NSAP address that was in the original CALL REQUEST packet. Step 6 - Clear Request Repeat Step 3 to clear the open channel. Step 7 - CALL ACCEPT from PAA - (Different NSAPs) Repeat Step 4. Program the PAA to return a CALL ACCEPTED packet to the AS with a Responding NSAP Address Field that is different than the request in Step 3.  Use the PAG to verify that the AS transmits the corresponding CALL CONNECTED packet to the PAG with the same called NSAP address generated by the PAA. Step 8 - Clear Request Procedures Repeat Step 3 to clear the open channel. 

2.4.19.3.18 
Throughput Class Negotiation Facility (Section 2.2.5) This test verifies the AS's ability to process a CALL REQUEST packet and CALL CONNECTED packet with Throughput Class Negotiation Facility. Step 1 - Call Request from the PAA Program the PAA to send a CALL REQUEST packet to the AS with the Facilities Field containing Throughput Class Negotiation facility with requested throughput class of 7 in both directions.  Use the PAG to verify that the AS transmits a INCOMING CALL packet to the PAG with the same throughput classes in both directions. Step 2 - Call Accept from the PAG Program the PAG to send a CALL ACCEPTED packet to the AS with throughput classes less than or equal to the requested throughput classes.  Verify that the AS sends the corresponding CALL CONNECTED packet to the PAA with the same throughput classes. Step 3 - Clear Request from the PAA Perform the procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3 to clear the channel. 

2.4.19.3.19 
Transit Delay Selection and Indication Facility (Section 2.2.5) 
 

This test verifies the AS's ability to process a CALL REQUEST packet and CALL CONNECTED packet with Transit Delay Selection and Indication Facility. Step 1 - Call Request from the PAA Program the PAA to send a CALL REQUEST packet to the AS with the Facilities Field containing the Transit Delay Selection and Indication Facility with a desired delay of 100 ms. Use the PAG to verify that the AS transmits a INCOMING CALL packet to the PAG with the same value of delay. Step 2 - Call Accept from the PAG Program the PAG to send a CALL ACCEPTED Packet to the AS with the applicable transit delay value of 5 s.  Verify that the AS sends the corresponding CALL CONNECTED packet with the same transit delay value to the PAA. 
 
Step 3 - Clear Request from the PAA Perform the procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3 to clear the channel. 
2.4.19.3.20 
Priority Facility (Section 2.2.5) The Priority Facility test procedure is designed to test the AS's ability to process the Priority facility during connection establishment and to forward a DATA packet with the agreed upon priority. 
Note: Testing organizations are cautioned that use of the Distress/Urgency 
priority messages must be coordinated in advance with the cognizant aviation authorities and the satellite network operator. If permission to 
operate with Distress/Urgency priority is not granted, the following tests 
may be performed with other target values, as indicated by the parenthetical notations in the following requirements. The manufacturer shall be responsible for demonstrating by other means that priority 14 messages are handled appropriately. 
 
Step 1 - Call Request with Distress Priority from the PAA Program the PAA to send a CALL REQUEST packet to the AS with the Facilities Field containing a Priority facility with a target value of 14 (11)for priority of data on a connection.  Use the PAG to verify that the LIDU containing the INCOMING CALL packet from the AS has priority level of 14. Step 2 - Call Accept from the PAG.  PAG Responds with the Same Priority. 
Program the PAG to send a CALL ACCEPTED packet with priority level of 14 (11). Verify that the AS sends the corresponding CALL CONNECTED packet to the PAA with the selected value of 14 for priority of data on a connection. 
Step 3 - Data from the PAA Program the PAA to send a DATA packet to the AS.  Use the PAG to verify that the DATA packet received from the AS has priority level of 14 (11). Step 4 - Clear Request from the PAA Perform the procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3 to clear the channel. Step 5 - Call Request from the PAA 
 
Perform the call setup procedure in Step 1 above. 
 
Step 6 - Call Accept from the PAG.  PAG Responds with a Lower Priority. 
 
Program the PAG to send to the AS a CALL ACCEPTED packet with priority level of 11 (9).  Verify that the AS sends the corresponding CALL CONNECTED packet to the PAA with the selected value of 11 (9) for priority of data on a connection. 
 
Step 7 - Data from the PAA 
 
Program the PAA to send a DATA packet to the AS.  Use the PAG to verify that the DATA packet received from the AS has priority level of 11(9). 
 
Step 8 - Clear Request from the PAA Perform the procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3 to clear the channel. 
 
2.4.19.3.21 
Multiple Channel Transactions (Section 2.2.5) The Multiple Channel Transactions test procedures are designed to test the AS's ability to process a transaction on one logical channel while not affecting the operation of the other open logical channels.  The test procedures are designed to be conducted in the given sequence. Unexpected or ambiguous test outputs may result from failure to observe the sequence. 
2.4.19.3.22 
Call Request Procedures (Section 2.2.5) This test opens multiple logical channels with the AS.  Perform the virtual call setup procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 1 twelve times to 
open the following ISO-8208 channel numbers: 2816, 2815, 2814, 2813, 2812, 2811, 2810, 2809, 2808, 2807, 2806, and 2805.  Verify that the AS selects the a corresponding set of logical channels.  Record the assignments for later reference. That is, if channel 2816 is assigned AS logical channel 255, record the pair 2816-255. 

 
2.4.19.3.23 
Data Transmission Procedures (Section 2.2.5) This test transmits data from the PAA.  Perform the data transmission procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 2 for each open channel.  Verify that all 12 channels are operating. 

2.4.19.3.24 
Clear Request Procedures (Section 2.2.5) This test clears opened channels.  Perform the clear request procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3 for channels 2814 and 2809.  Perform the data transmission procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 2 for the remaining 10 channels.  Verify that the clearing procedures did not affect the operation o f the other channels by confirming that the AS forwards the corresponding DATA packets to the PAG on all 10 channels. 

2.4.19.3.25 
Reset Request Procedures (Section 2.2.5) This test resets channels.  Perform the reset request procedures in Section 2.4.19.3.3 Reset States Step 1 for channels 2815, 2811 and 2806.  Perform the data transmission procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 2 for the 10 channels. Verify that the resetting procedures did not affect the operations of the AS by confirming that the AS forwards the DATA packets to the PAG. 

2.4.19.3.26 
Receive Not Ready Status (Section 2.2.5) 
 
Note: See the introductory material regarding selection and assignments of ISO 
channels contained in Section 2.4.19.3.1. Step 1 - Data Transfer This test transfers data from the PAG to the AS. a. 

Program the PAG to send two DATA packets to the AS for each open channel, each containing 56 bits of user data.  Set M-bit to zero in both packets.  Verify the corresponding ISO-8208 packets sent by the AS to the PAA. b. 

Program the PAA to return RECEIVE READY packets to the AS for all open channels except 2816, 2810 and 2805. 

 

c. 
Perform the procedure in Step 1a for the following corresponding to channels 2815, 2813, 2812, 2807, 2806, 2805.   Verify that the receive not ready conditions on channels 2816, 2810 and 2805 do not affect the operations of the other channels by confirming that the AS forwards the corresponding DATA packets to the PAA. Step 2 - Clear Request Procedures This test clears channels.  Perform the clear request procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3 for channels 2816, 2810 and 2805.  Repeat step 1c and verify that no data was transmitted to the PAA. 2.4.19.3.27 
Error Recovery Procedures (Section 2.2.5) Step 1 - Force an Error Condition that allows the air/ground link to continue normal 
 
operation (e.g. ISO-8208 protocol violation). This test forces channels into an error recovery state. a. 
Program the PAA to send a CALL REQUEST packet to the AS on channels 2815 and 2807.  Verify that the AS returns a CLEAR INDICATION packet to the PAA on channels 2815 and 2807.  Also verify that the AS transmits, on the logical channels corresponding to 2815 and 2807, a CLEAR INDICATION packet to the PAG.  Diagnostic codes should be set to 23. b. 
Perform the data transmission procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 2 for channels 2813, 2812, 2811, 2808, and 2806.  Verify that the error recovery conditions on channels 2815 and 2807 do not affect the operations of the other open channels by confirming that the AS forwards the corresponding DATA packets to the PAG. Program the PAA to send a CLEAR CONFIRMATION packet to the AS on channels 2815 and 2807.  Program the PAG to respond to the AS with a CLEAR CONFIRMATION packet for logical channels corresponding to 2815 and 2807. Step 2 - Clear Open Channels This test clears open channels.  Perform the clear request procedure in Section 2.4.19.3.4 Call Setup and Clearing States Step 3 for channels 2813, 2812, 2811, 2808 and 2806. 
2.4.19.3.28 
ISO-8208 DCE Timer Test Procedures (Section 2.2.5) The DCE Timer test procedures are designed to test the AS's ability to perform corrective actions when the ISO-8208 DCE timers through tN13 expire. 2.4.19.3.29 
tN10 Timer Procedure (Section 2.2.5) 
 Program the PAG to send a RESTART REQUEST packet to the AS via the subnetwork. Verify that the AS sends a RESTART INDICATION packet to the PAA. Disable any PAA response to this packet.  Wait for an interval of tN10 seconds after sending the RESTART INDICATION.  Use the PAA to send a CALL REQUEST packet to the AS and verify that there is no corresponding response to the PAG. Note: To facilitate the next test, initialize the AS by using the PAA to return a RESTART CONFIRMATION packet to the AS; there should be no ISO-8208 outputs from the AS. 

 
2.4.19.3.30 
tN11 Timer Procedure (Section 2.2.5) 
 
Program the PAG to send a CALL REQUEST packet to the AS.  Verify that the AS sends a corresponding INCOMING CALL packet to the PAA.  Disable any PAA response to this packet.  Wait and verify that within the interval tN11 to tN11+5 seconds after sending the INCOMING CALL packet, the AS sends a CLEAR INDICATION packet to the PAA with D=49. 

 
Note: To facilitate the next test, initialize the AS by using the PAA to send a CLEAR 
CONFIRMATION packet to the AS, and use the PAG to send a CLEAR CONFIRMATION packet to the AS;  there should be no ISO-8208 outputs at the AS/PAA interface and no packet outputs at the AS/PAG interface. 

 
2.4.19.3.31 
tN12 Timer Procedure (Section 2.2.5) Perform the call setup procedure in Section 2.4.3.6.4.2.3.1.1, Step 1. Program the PAG to send a RESET REQUEST packet to the AS. Verify that the AS sends a corresponding RESET INDICATION packet to the PAA. Disable any PAA response to this packet. Wait and verify that within the interval tN12 to tN12+5 seconds after sending the RESET INDICATION packet, the AS sends a CLEAR INDICATION packet to the PAA with D=51. Note: To facilitate the next test, initialize the AS by using the PAA to send a CLEAR 
CONFIRMATION packet to the AS, and use the PAG to send a CLEAR CONFIRMATION packet to the AS; there should be no ISO-8208 outputs at the AS/PAA interface and no packet outputs at the AS/PAG interface. 

 
2.4.19.3.32 
tN13 Timer Procedure (Section 2.2.5) Perform the call setup procedure in Section 2.4.19.3.4, Step 1.  Use the PAG to send a CLEAR REQUEST packet to the AS.  Verify that the AS sends a CLEAR INDICATION packet to the PAA.  Disable any PAA response to this packet.  Wait for the interval tN13 seconds.  Perform the call setup procedure in Section 2.4.19.3.4, Step 1, using the same logical channel number used at the start of this timer test.  Verify that a 

## Corresponding Incoming Call With That Logical Channel Number Is Received At The Pag. 2.4.20 Aircraft Log-On Procedure Test Requirements (Sections 2.2.4.5 And 2.2.6 ) Equipment Required

 
Ground Station Emulator Power Attenuator, 80 dB, 200 watt average power Message Source, ISO-8208 Protocol Analyzer, or equivalent PC  
 
Protocol Analyzer - Avionics Specific; e.g. ARINC 429  
 
UUT 
 
 Setup the equipment as shown in Figure 2.4-17. Use the PC to program each of the Squitter fields defined in Section 2.2.4.5.  Select an appropriate Ground Station Emulator frequency from the HFDL System Table and initiate SPDU transmission to allow the UUT to Log-on to the Ground Station Emulator.  Verify that the UUT Logs On per the requirements in Section 2.2.6. Change the Ground Station frequency to a different frequency on the HFDL System Table.  Verify that the UUT Logs on to the new frequency. 2.4.21 
Recovery from Primary Power Interruption Test Requirements 
 
(Section 2.2.7) 
 
Equipment Required RF signal Generator, HP 8640 or equivalent Oscilloscope Programmable Interruptible Power Supply, HP6834A or equivalent Setup the equipment as shown in Figure 2.4-18.   Monitor the receiver audio on the oscilloscope.  Apply 5 ms power interruptions and observe no dropout of audio.  Apply 200 ms power interruptions and verify that the audio recovers within 5 seconds and verify the data link functions are unaffected. 

2.4.22 
Failure/Status Indication Test Requirements (Section 2.2.8 ) 
Setup the equipment as shown in Figure 2.4-19. With the Ground Station Emulator OFF, use the Protocol Analyzer to verify that the UUT reports HFDL status NOT AVAILABLE. Use the PC to program each of the Squitter fields defined in Section 2.2.4.5.  Select an appropriate Ground Station Emulator frequency from the HFDL System Table and initiate SPDU transmission to allow the UUT to Log-on to the Ground Station Emulator.  Verify that the UUT Logs On and that it reports HFDL status AVAILABLE. Use the Protocol Analyzer to cause the UUT to switch to voice mode and verify that the UUT reports HFDL status NOT AVAILABLE / VOICE MODE. Induce a failure on the UUT and use the Protocol Analyzer to verify that the UUT 
reports HFDL status NOT AVAILABLE / HFDL FAULT. 

2.4.23 
Frequency Search (Section 2.2.3.3.5) 
Equipment Required Ground Station Emulator Power Attenuator, 80 dB, 200 watt average power Message Source, ISO-8208 protocol Analyzer, or equivalent 
 
 
RTCA: Set up the equipment as shown in Figure 2.4-20. Set the GS Emulator to broadcast a valid system table with the frequencies to be used, at least one of which is contained in the UUT table.  When the UUT is initially powered on, observe that it searches for and finds the GS Emulator squitter by observing that the UUT logs on to the GSE.  See 2.4.20. Cause the GS Emulator to change frequencies normally and verify that the UUT changes to the new frequency and logs on to the GS Emulator. Cause the GS Emulator to change frequencies without notice and verify that the UUT finds the new frequency and logs on to the GS Emulator. 

## 3 Installed Equipment Performance

3.1 
Equipment Installation 
 
3.1.1 
Accessibility Controls and monitors provided for in-flight operation shall be readily accessible from the appropriate operator's normal seated position.  The operator/crew member(s) shall have an unobstructed view of the display(s) or controls when in the normal seated position. 

3.1.2 
Aircraft Environment Equipment shall be compatible with the environmental conditions present in the specific location in the aircraft where the equipment is installed. 

3.1.3 
Display Visibility All installed system displays shall be readily visible and readable from the operator's/crew member's normal position in all ambient lighting conditions for which system use is required. 

 
Note: Visors, glareshields, or filters may be an acceptable means of obtaining 
 
daylight visibility. 

 
3.1.4 
Inadvertent Turn-Off Where controls for transceiver operation are provided, they shall be equipped with adequate protection against inadvertent turn off. 

 
3.1.5 
Failure Protection 
 
Any probable failure of the equipment shall not degrade the normal operation of equipment or systems that are connected to it.  Likewise, the failure of interfaced equipment or systems shall not induce failures of this equipment. 

3.1.6 
Interface Interference Effects The equipment shall not be the source of harmful conducted or radiated interference, and shall not be affected by conducted or radiated interference from other equipment or systems installed in the aircraft. 

3.1.7 
Aircraft Power Source The voltage and frequency tolerance characteristics of the equipment shall be compatible with the aircraft power source of appropriate category as specified in RTCA DO-160D. 

3.2 
Installed Equipment Performance Requirements The installed equipment shall meet the requirements of Section 2.0 in addition to the requirements stated below.  To meet the requirements of this section, test results supplied by the equipment manufacturer may be accepted in lieu of tests performed by the equipment installer. 

 
However, performance characteristics which cannot be tested by the equipment manufacturer shall be tested by the installer.  These include: (1) performance characteristics of equipment required for the transceiver installation that have not been tested or verified by the manufacturer, and (2) interactions with other equipment installed on the aircraft. 

3.3 
Conditions of Test The following Sections define conditions under which the tests specified in Section 3.4 shall be conducted. 

3.3.1 
Power Input Tests may be conducted either with the equipment powered by the aircraft's electrical power generation system or by an appropriate external power source connected to the aircraft. 

3.3.2 
Environment During the tests, the equipment shall not be subjected to environmental conditions that exceed those in RTCA/DO-160D as specified by the equipment manufacturer. 

3.3.3 
Adjustment of Equipment Circuits of the equipment under test shall be properly aligned and otherwise adjusted in accordance with the manufacturer's recommended practices prior to application of the specified tests. 

3.3.4 
Warm-up Period Unless otherwise specified, tests shall be conducted after a warm-up (stabilization) period of twenty (20) minutes. 

3.4 
Test Procedures for Installed Equipment Performance The following test procedures provide one means of determining installed equipment performance. Although specific test procedures are cited, it is recognized that the installing activity may prefer alternate procedures, which may be used if they provide at least equivalent information. In such cases, the procedures cited herein should be used as 

one criterion in evaluating the acceptability of the alternate procedures. 
3.4.1 
Conformity Inspection 
 
Visually inspect the installed equipment to determine the use of acceptable workmanship and engineering practices.  Verify that proper mechanical and electrical connections have been made and that the equipment has been located and installed in accordance with the manufacturer's recommendations. 
3.4.2 
Interference Tests Unless otherwise specified, all aircraft electrically-operated equipment and systems shall be on, using the aircraft's electrical power generating equipment before conducting interference tests. 
 
With the transceiver operating, including transmission of messages and voice calls, individually operate each of the other electrically-operated aircraft equipment and systems to determine that no significant conducted or radiated interference exists.  Evaluate all 
reasonable combinations of control settings and operating modes.  Operate communication 
and navigation equipment on at least a low, high, and mid-band, frequency. 
 
Operate the aircraft controls (e.g., flaps) through their range to activate all associated aircraft systems that may cause electrical power fluctuations. 
 
Notes: 1. Some aircraft contain cooling fans to augment airflow under certain low 
 
speed conditions.  These fans are activated with flaps extended and lowto mid-throttle, and cause aircraft power fluctuations when activated. 


2. See Section 3.4.4 for requirements for message generation. 3.4.3 
Power Fluctuation Tests 
 
 (Section 2.2.7) 
 
Transceiver aircraft power sources shall be cycled through all normal configurations to verify that the transceiver performance for power interruption recovery during and after power changeover is satisfactory with no discernible abnormal operation (Reference Section 2.2.7). 
 
Note: In-transit data service packets which have been acknowledged on either the 
DTE or DCE interface, but not yet transferred to the opposite interface, may be lost. Non-transceiver higher layer entities that employ end-to-end 
acknowledgment protocols may choose to retransmit such lost data. 
 
3.4.4 
Ground Test Procedures Perform the ground test portions of tests defined in manufacturer's installation instructions. 
 
3.4.5 
Flight Test Procedures Flight tests of installed systems are desirable to confirm or supplement bench and ground tests of installed performance.  Flight tests may be defined in the manufacturer's installation instructions. 

 
3.4.6 
Installed System Performance Verification Performance of the installed avionics, consisting of the Antenna Subsystem and the Transceiver Subsystem, should be verified in accordance with the system integrator procedures. 

4 
EQUIPMENT OPERATIONAL PERFORMANCE CHARACTERISTICS HF voice/Data Link installations are expected to be accomplished in a variety of ways to fit the aircraft equipment and intended usage. This will also be the case with associated cockpit interfaces.  The requirements of this section shall be suitably interpreted for the particular installation under consideration. 

4.1 
Operational Performance Requirements The following sections identify requirements to ensure the operator that operations can be conducted safely and reliably in the expected operational environment. 

4.1.1 
Power Input Prior to flight, the primary power must be available for proper operation. 

4.1.2 
Communications Displays The required display(s) for the selection of various communication modes/functions of operation shall be available for use. 

4.1.3 
Communications Controls Cockpit control(s) required for proper operation of the equipment shall be available for use. 

4.1.4 
System Operational Indication Communication failure of degradation below minimum acceptable performance shall be readily discernible. 

4.1.5 
Equipment Operating Limitations Equipment operating limitations of the HF Data Link should be contained in the aircraft flight manual. 

4.2 
Test Procedures for Operational Requirements Operational equipment tests may be conducted as part of normal preflight tests.  For those tests that can only be run in flight, procedures should be developed to perform these tests as early in the flight as possible to verify that the equipment is performing its intended function(s). 

4.2.1 
Power Input With the aircraft's electrical power generating system operating, energize the equipment and verify that electrical power is available to the equipment. 

## 4.2.2 Communications Displays With The Equipment Operating, Verify That The Required Display(S) Are Operational. 4.2.3 Communications Controls The Communications Control(S) Shall Be Operated, As Required, To Verify Satisfactory Equipment Response. 4.2.4 System Operational Indication System Operational Readiness Shall Be Monitored Either By Means Of Built-In-Test- Equipment (Bite) And/Or By Suitable Preflight Tests Contained In A Check List Or Flight Manual.  All Equipment Failure Annunciators Shal L Be Tested During Preflight Tests To Verify Proper Operation.

 
MEMBERSHIP 
 
Special Committee 188 
 
High Frequency Data Link 
 
Chairman, SC-188 
Colonel Roger Robichaux 
 
U.S. Air Force  
 
Chairman, SC-188 Working Group 1, MASPS 
Mr. R. Andrew Pickens  
  
AvCom, Inc. Chairman, SC-188 Working Group 2, MOPS 
 
Mr. George Cobley  
  
Rockwell Collins, Inc. 

 
 
Secretary 
 
Mr. Michael D. Rockwell 
  
ARINC Members Mr. Eric Adler Boeing Ms. Terri Anton ARINC 
Mr. Gilbert B. Asher ARINC 
Mr. Melvin Barmat Jansky/Barmat Telecommunications Mr. Scott Beale ARINC 
Mr. Joel Bean LB&M Associates (FAA) 
Mr. Scott Bradfield Rannoch Corporation Mr. Franklin W. Calkins DCS Corporation Dr. George C. Chang Consultant Mr. Mark Clark ARINC 
Mr. Joseph Comeaux Air Line Pilots Association Ms. Suzanne Compton ARINC 
Mr. Neil J. Earnhardt Rockwell Collins, Inc. 

Mr. Brian Gaffney ARINC 
Dr. John M. Goodman TCI/BR Communications Mr. Jim Grace Rockwell Collins, Inc. 

Ms. Nancy Guzak Rockwell Collins, Inc. 

Mr. Frank D. Hasman Federal Aviation Administration Mr. Tom Hauer Rockwell Collins, Inc. 

Mr. Michael Hawthorne Federal Aviation Administration Mr. Elbert J. Henry Federal Aviation Administration Mr. Howard Hess Rockwell Collins, Inc. 

Mr. Anthony P. Holt AlliedSignal Aerospace Co. Inc. 

Mr. Lawrence Ilarregoi Convergent Sciences & Tech Corp. 

Mr. Les James Federal Aviation Administration Mr. Loftur Jonasson Iceland Radio Mr. Arun Katyal TRW, Inc. 

Mr. Paul Kellam MITRE Corporation Mr. Phil LaRocca Federal Aviation Administration Dr. Victor Lebacqz National Aeronautics & Space Administration Mr. Frank P. Mackowick SkyComm, Inc. 

Mr. Alfonso Malaga AlliedSignal Aerospace Co. Inc. 

Mr. Vincent Nguyen Federal Aviation Administration Mr. Timothy J. Pawlowitz Federal Aviation Administration Mr. Claude Pichavant Aerospatiale Matra Airbus Mr. Robert W. Renoud Mr. Rudy Ruana ARINC RTCA, Inc. 

Mr. Walter C. Scales The MITRE Corporation Mr. Herbert W. Schlickenmaier National Aeronautics & Space Administration Mr. David Sim Transport Canada Mr. Bernald S. Smith Soaring Society of America Mr. Robert Stahl The Boeing Company Mr. Dan C. Tootle ARINC 
Mr. Matthew S. Wade Federal Aviation Administration Mr. Terence Wendel Federal Aviation Administration Mr. Ken Wickwire MITRE 
Appendix A 
 
GLOSSARY AND DEFINITIONS OF TERMS 

                         
This page intentionally left blank. 

Appendix A - GLOSSARY AND DEFINITION OF TERMS 
 
AAC 
Airline Administrative Communications 
AC 
Alternating Current 
ACARS 
Aircraft Communications, Addressing and Reporting System 
ADS 
Automatic Dependent Surveillance 
AERA 
Air Traffic Service Operational Requirements for Automated En Route ATC Version 1 (AERA 1) 
AM(R)S 
Aeronautical Mobile (Route) Service 
AOC 
Airline Operational Control 
APC 
Aircraft Passenger Communications 
ARINC 
Aeronautical Radio, Inc. 
AS 
Aircraft Station 
ATC 
Air Traffic Control 
ATIS 
Automatic Terminal Information Service 
ATM 
Air Traffic Management 
ATN 
Aeronautical Telecommunications Network 
ATS 
Air Traffic Services 
b/s 
bits per second 
BDU 
Basic Data Unit 
BER 
Bit Error Rate 
BPSK 
Binary Phase Shift Keying 
C 
Celsius 
CMU 
Communications Management Unit (character oriented [ACARS] and bit oriented [ATN]) 
CNS 
Communications/Navigation/Surveillance 
Data Link 
A system that allows the exchange of digital data over a communications network 
Data-2 
A Data Link implementation for the enveloping of user data with a unique Initial Protocol 
Identifier of FFh 
Data-3 
A Data Link implementation for the transmission of user data using ISO-8208 protocol 
dB 
Decibel 
dBm 
Decibels referenced to 1 milliwatt 
DC 
Direct Current 
DCE 
Data Communications Equipment 
DFDAU 
Digital Flight Data Acquisition Unit 
DLS 
Direct Link Service 
DSP 
Digital Signal Processor 
DTE 
Data Terminal Equipment 
EMI 
Electromagnetic Interference 
F 
Fahrenheit 
fc 
Frequency of a Carrier 
FCS 
Frame Check Sequence (usually a cyclic redundancy code) 
FDMA 
Frequency Division Multiple Access 
FIS 
Flight Information Service 
FMC 
Flight Management Computer 

 

Full Power 
The operating power level that is defined as the usual maximum operating level
 
Gaussian 
A symmetric, bell-shaped probability curve 
GPS 
Global Positioning System 
GS 
Ground Station 
GSE 
Ground Station Emulator 
 
HF 
High Frequency (3 to 30 MHz) 
HFDR 
HF Data Radio 
HFDL 
High Frequency Data Link 
HLE 
Higher Layer Entity 
Hz 
Hertz (measure of frequency) 
ICAO 
International Civil Aviation Organization  
ID 
Identification 
ISO 
International Standards Organization 
ITU 
International Telecommunications Union 
IWF 
Interworking Function 
kHz 
Kilo Hertz (1,000 times frequency) 
kPa 
Kilo Pascals (1,000 times unit of pressure; Newtons per square meter) 
LIDU 
Link Interface Data Unit 
LPDU 
Link Protocol Data Unit 
LSDU 
Link Service Data Unit 
M-ary 
M dimensional array 
MHz 
Mega Hertz (1,000,000 times frequency) 
MID 
First octet of the downlink MPDU header 
Mode-S 
Mode Select - A transponder format to allow discrete interrogation and data link capability 
MOPS 
Minimum Operational Performance Standard 
MPDU 
Media access control Protocol Data Unit 
M-PSK 
M-ary Phase Shift Keying 
ms 
Milli second (1/1000 second) 
MU 
Management Unit (character oriented ACARS) 
Network 
A collection of interconnected devices for the purpose of exchanging data 
NOTAM 
Notice To Airmen 
NPDU 
Network Protocol Data Unit 
NSAP 
Network Service Access Point 
OSI 
Open System Interconnect 
PAA 
Protocol Analyzer - Airborne 
PAG 
Protocol Analyzer - Ground 
PDU 
Protocol Data Unit 
PER 
Packet Error Rate 
PIREP 
Pilot Report 
Precedence 
Mechanization for the execution of relative priority 
Priority 
Relative ordering of importance 
Pp 
Peak Envelop Power (PEP) 
ppm 
parts per million 
PTT 
Push-To-Talk 
Q Number 
Link Layer identification of priority 
RF 
Radio Frequency 
RLS 
Reliable Link Service 
RTCA 
RTCA, Inc.  
rms 
Root Mean Square 
SARPs 
Standards And Recommended Practices (developed by ICAO) 
SATCOM 
Satellite Communication 
SNAc 
SubNetwork Access 
SNC 
SubNetwork Connection 
SND 
SubNetwork Dependent Sublayer 
SNL 
Subnetwork Layer (a part of Network Layer) 
SNR 
Signal to Noise Ratio 
SNPDU 
SubNetwork Protocol Data Unit 
SPDU 
Squitter Protocol Data Unit 
Squitter 
The repetitive transmission of basic system information and time synchronization  
SSB 
Single Sideband 
SU 
Signal Unit 
Subnetwork 
See Network 
SVC 
Switched Virtual Circuit 
TCAS 
Traffic alert Collision Avoidance System 
TDMA 
Time Division Multiple Access 
Transceiver 
All of the elements between the ISO-8208 input/output port and the common receiver and transmitter RF connection 
UTC 
Universal Coordinated Time 
UUT 
Unit Under Test 
VFR 
Visual Flight Rules 
Viterbi 
A data decoder implementation 
W 
Watt 
Definitions 
 
GSE 
Ground Station Emulator.  This device is capable of emulating the behavior of a ground station.  This should be script driven to allow specific patterns of behavior to be repeated for each test.  This device should be capable of describing the behavior of the UUT so as to allow determination of pass/fail for each test for which it is used. 
 
HF Data Link 
A packet data communications system operating in the High Frequency radio spectrum. 
 
Preemption 
The termination of one communication before completion in preference to another. 
 
Terrestrial Network 
A collection of devices on the ground for the purpose of exchanging data. 
 

 
UUT  
Unit Under Test. This is a full up HFDR/HFDU.  It may be modified to operate at low power.  This modification allows equivalent tests since the signal-inspace wave form characteristics are not under test.  The tests of Section 2.4 are designed to insure that the operation of the Data Link Layer protocol is compliant with the MOPS specifications. 

## 

 
 
This page intentionally left blank. 

## Appendix B Requirements/Test Coverage Matrix

 
This page intentionally left blank.

Appendix B - REQUIREMENTS/TEST COVERAGE MATRIX Requirement 
Test Section(s) 
 
2.2     Equipment Performance Requirements, Standard Conditions 
NA 
2.2.1     
Avionics Subsystem Definitions and Overall Requirements 
NA 
2.2.2     
Voice/Data Mode Selection 
2.4.5 
2.2.2.2    Dual HF Data Link Installations 
2.4.6 
2.2.3     
HF Data Link Subnetwork Physical Layer Requirements 
NA 
2.2.3.1    Signal-In-Space Modulation Definition 
2.4.7 
2.2.3.2    Signal-In-Space Transmission Requirements 
NA 
2.2.3.2.1   Prekey Requirement 
2.4.7, 2.4.9 
2.2.3.2.2   Preamble Requirement 
2.4.7 
2.2.3.2.3   Data Segment Requirement 
2.4.7 
2.2.3.2.3.1  Forward Error Correction 
2.4.7 
2.2.3.2.3.2  Interleaving Requirement 
2.4.7 
2.2.3.2.3.3  M-PSK Symbol Scrambling 
2.4.7 
2.2.3.2.4   Transmit Slot Time Synchronization 
2.4.13.1 
2.2.3.2.5   Transmit Pulse-Shaping Filter Response 
2.4.7, 2.4.8 
2.2.3.2.6   Spectrum Control in Data Mode 
2.4.8 
2.2.3.2.7   Transmitter Peak Power 
See DO-163 
2.2.3.3    Reception Requirements 
NA 
2.2.3.3.1   HF Data Link Receiver Sensitivity 
See DO-163 
2.2.3.3.2   Packet Error Rate Performance 
2.4.10 
2.2.3.3.3   Transmit to Receive Recovery Time 
2.4.11 
2.2.3.3.4   Receiver Signal Attenuation 
See DO-163 
2.2.3.3.5   Frequency Search 
2.4.23 
2.2.4     
HF Data Link Subnetwork Data Link Layer Functions 
NA 
2.2.4.1    Data Rate Communications 
2.4.12 
2.2.4.2    Selection of Downlink Slot by Aircraft 
2.4.13 
2.2.4.3    Maximum MPDU Size Adjustment 
2.4.14 
2.2.4.4    Data Rate and Interleaver Selection 
2.4.14, 2.4.15 
2.2.4.5    Squitter PDU Format 
2.4.16 
2.2.4.5.1   SPDU ID 
2.4.16 
2.2.4.5.2   Ground Station Address 
2.4.16 
2.2.4.5.3   Frame ID 
2.4.16 
2.2.4.5.4   Slot Acknowledgment Codes 
2.4.16 
2.2.4.5.5   Slot Assignment Codes 
2.4.16 
2.2.4.5.6   Priority Field 
2.4.16 
2.2.4.5.7   Ground Station Active Frequency Field 
2.4.16 
2.2.4.5.8   Frame Check Sequence 
2.4.16 
2.2.4.5.9   Flush Field 
2.4.16 
2.2.4.6    MPDU Packet Encapsulation 
2.4.17 
2.2.4.7    MPDU Format Requirements 
2.4.17, 2.4.18 
2.2.4.7.1   Mid (MPDU ID) Field 
2.4.17, 2.4.18 
2.2.4.7.2   GS Field 
2.4.17, 2.4.18 
2.2.4.7.3   Aircraft Address Field 
2.4.17, 2.4.18 
| 2.2.4.7.4   FCS (Frame Check Sequence)             | 2.4.17, 2.4.18                           |
|----------------------------------------------------|------------------------------------------|
| 2.2.4.7.5   Data Field                             | 2.4.17, 2.4.18                           |
| 2.2.4.7.6   Flush Field                            | 2.4.17, 2.4.18                           |
| 2.2.5                                              | Packet-Mode Data Service Requirement     |
| 2.2.5.1    Packet-Mode Data-2 Service Requirements | 2.4.19, 2.4.19.1.3                       |
| 2.2.5.2    Packet-Mode Data-3 Service Requirements | 2.4.19, 2.4.19.1                         |
| 2.2.5.3    Priority, Precedence and Preemption     | 2.4.4, 2.4.19, 2.4.19.1.2                |
| 2.2.5.4    HF Data Link Subnetwork Requirements    | 2.4.19, 2.4.19.2.1                       |
| 2.2.5.4.1   Data-2 Requirements                    | 2.4.19                                   |
| 2.2.5.4.2   Data-3 Requirements                    | 2.4.19, 2.4.19.1                         |
| 2.2.5.4.3   Join and Leave Event Requirements      | 2.4.19, 2.4.19.1.1                       |
| 2.2.6                                              | Aircraft Log-on Procedure                |
| 2.2.7                                              | Recovery from Primary Power Interruption |
| 2.2.8                                              | Failure/Status Indication                | Test Section(s) 
Requirement 2.4  
 
 
Equipment Performance Verification Procedures 
NA 
2.4.1 

Definitions of Terms and Conditions of Test 
NA 
2.4.2 

Required Test Equipment 
NA 
2.4.3 

Detailed Test Procedures 
NA 
2.4.4 

Priority, Precedence and Preemption Test Requirements 
2.2.2, 2.2.5.3 
2.4.5 

Voice/Data Mode Selection Test Requirements 
2.2.2, 2.2.2.1 
2.4.6 

Dual HF Data Link Installation Test Requirements 
2.2.2.2 
2.4.7 

Signal-In-Space Test Requirements 
2.2.3.1, 2.2.3.2.1, 2.2.3.2.2, 2.2.3.2.3 and subsections, 2.2.3.2.5 
2.4.8 
   
 Transmit Pulse Shaping Filter Test Requirements 
2.2.3.2.5, 2.2.3.2.6 
2.4.9 

Prekey Time Test Procedure 
2.2.3.2.1 
2.4.10  
 
Packet Error Rate Test Requirements 
2.2.3.3.2 
2.4.11  
 
Transmit to Receive Recovery Time Test Procedure 
2.2.3.3.3 
2.4.12  
 
Data Rate Communications Test Requirements 
2.2.4.1 
2.4.13  
 
Selection of Downlink Slot by Aircraft Requirements 
2.2.4.2 
2.4.13.1 
 
Transmit Slot Time Synchronization 
2.2.3.2.4 
2.4.14  
 
Maximum MPDU Size Adjustment Test Requirements 
2.2.4.3, 2.2.4.4 
2.4.15  
 
Data Rate and Interleaver Selection Test Requirements 
2.2.4.4 
2.4.16  
 
Squitter SPDU Format Test Requirements 
2.2.4.5, 2.2.4.51, 2.2.4.5.2, 2.2.4.5.3, 2.2.4.5.4, 2.2.4.5.5, 2.2.4.5.6, 2.2.4.5.7, 2.2.4.5.8, 2.2.4.5.9 
2.4.17  
 
MPDU Packet Encapsulation Test Requirements 
2.2.2, 2.2.4.6, 2.2.4.7, 2.2.4.7.1, 2.2.4.7.2, 2.2.4.7.3, 2.2.4.7.4, 2.2.4.7.5, 2.2.4.7.6 
2.4.18  
 
MPDU Format Test Requirements 
2.2.4.7, 2.2.4.7.1, 2.2.4.7.2, 2.2.4.7.3, 2.2.4.7.4, 2.2.4.7.5, 2.2.4.7.6 
2.4.19  
 
Packet Mode Data Services Test Requirements 
2.2.5, 2.2.5.1, 2.2.5.2, 2.2.5.3, 2.2.5.4, 2.2.5.4.1, 2.2.5.4.2, 2.2.5.4.3 
2.4.19.1 
 
Data 3/ATN/ISO-8208 Interfaces 
2.2.5.2, 2.2.5.4.2 
2.4.19.1.1  
Join and Leave Requirements 
2.2.5.4.3 
2.4.19.1.2  
Data 3 Mapping for Priority, Precedence and Preemption 
2.2.5.3 
2.4.19.1.3  
Data 2 
2.2.5.1 
2.4.19.2 
 
HF Data Link Subnetwork 
NA 
2.4.19.2.1  
HF Data Link Subnetwork Dependent Protocol 
2.2.5.4 
 
2.4.19.3 
 
Avionics Subnetwork Interface 
2.2.5 
2.4.19.3.1  
ISO-8208 Protocol 
2.2.5 
| 2.4.19.3.2     | Channel State Test Procedures                    | 2.2.5                                                      |
|----------------|--------------------------------------------------|------------------------------------------------------------|
|                |                                                  |                                                            |
| 2.4.19.3.3     | Normal State Test Procedures                     | 2.2.5                                                      |
| 2.4.19.3.4     | Call Setup and Clearing States                   | 2.2.5                                                      |
| 2.4.19.3.5     | Restart Request States                           | 2.2.5                                                      |
| 2.4.19.3.6     | Reset States                                     | 2.2.5                                                      |
| 2.4.19.3.7     | Interrupt Transfer States                        | 2.2.5                                                      |
| 2.4.19.3.8     | Error Recovery Procedures                        | 2.2.5                                                      |
| 2.4.19.3.9     | DCE Call Setup and Clearing States               | 2.2.5                                                      |
| 2.4.19.3.10    | DCE Restart States                               | 2.2.5                                                      |
| 2.4.19.3.11    | DCE Reset States                                 | 2.2.5                                                      |
| 2.4.19.3.12    | DCE Flow Control Transfer States                 | 2.2.5                                                      |
| 2.4.19.3.13    | DCE Interrupt Transfer States                    | 2.2.5                                                      |
| 2.4.19.3.14    | Packet Assembly                                  | 2.2.5                                                      |
| 2.4.19.3.15    | Call Setup and Maintenance                       | 2.2.5                                                      |
| 2.4.19.1.16    | Fast Select Facilities                           | 2.2.5                                                      |
| 2.4.19.3.17    | Called and Calling Address Extension (NSAP) Test | 2.2.5                                                      |
| 2.4.19.3.18    | Throughput Class Negotiation Facility            | 2.2.5                                                      |
| 2.4.19.3.19    | Transit Delay Selection and Indication Facility  | 2.2.5                                                      |
| 2.4.19.3.20    | Priority Facility                                | 2.2.5                                                      |
| 2.4.19.3.21    | Multiple Channel Transactions                    | 2.2.5                                                      |
| 2.4.19.3.22    | Call Request Procedures                          | 2.2.5                                                      |
| 2.4.19.3.23    | Data Transmission Procedures                     | 2.2.5                                                      |
| 2.4.19.2.24    | Clear Request Procedures                         | 2.2.5                                                      |
| 2.4.19.3.25    | Reset Request Procedures                         | 2.2.5                                                      |
| 2.4.19.3.26    | Receive Not Ready Status                         | 2.2.5                                                      |
| 2.4.19.3.27    | Error Recovery Procedures                        | 2.2.5                                                      |
| 2.4.19.3.28    | ISO-8208 DCE Timer Test Procedures               | 2.2.5                                                      |
| 2.4.19.3.29    | tN10 Timer Procedure                             | 2.2.5                                                      |
| 2.4.19.3.30    | tN11 Timer Procedure                             | 2.2.5                                                      |
| 2.4.19.3.31    | tN12 Timer Procedure                             | 2.2.5                                                      |
| 2.4.19.3.32    | tN13 Timer Procedure                             | 2.2.5                                                      |
| 2.4.20         |                                                  | Aircraft Log-on Procedure Test Requirements                |
| 2.4.21         |                                                  | Recovery from Primary Power Interruption Test Requirements |
| 2.4.22         |                                                  | Failure/Status Indication Test Requirements                |
| 2.4.23         | Frequency Search                                 | 2.2.3.3.5                                                  |
|                |                                                  |                                                            |
|                |                                                  |                                                            |

 
Appendix C 
 
ICAO REQUIREMENTS REFERENCE TABLE 
This page intentionally left blank. 

Appendix C - ICAO REQUIREMENTS REFERENCE TABLE 
 
MOPS Section 
No. 
Paragraph Title 
ICAO SARPs 
Chapter 11 
Section No. 
ICAO Manual 
On HF Data 
Link  
Section No. 
2.2.3.1 
Signal-In-Space Modulation Definition 
11.3.1.5 
 
2.2.3.2.1 
Prekey Requirement 
11.3.2.3 
P2 - 2.2.2.1.2 
2.2.3.2.2 
Preamble Requirement 
 
P2 - 2.2.2.1.3 
2.2.3.2.3 
Data Segment Requirement 
 
P2 - 2.2.2.1.4, 2.2.2.2.1 
2.2.3.2.3.1 
Forward Error Correction 
 
P2 - 2.2.2.3 
2.2.3.2.3.2 
Interleaving Requirement 
 
P2 - 2.2.2.4 
2.2.3.2.3.3 
M-PSK Symbol Scrambling 
 
P2 - 2.2.2.6 
2.2.3.2.4 
Transmit Slot Time Synchronization 
11.3.2.3 
 
2.2.3.2.5 
Transmit Pulse-Shaping Filter Response 
11.3.1.5.2 
 
2.2.3.2.6 
Spectrum Control in Data Mode 
11.3.1.11 
 
2.2.3.2.7 
Transmitter Peak Envelope Power 
11.3.1.12.2 
 
2.2.3.3 
Reception Requirements 
11.3.2.4 
P2 - 2.2.3 
2.2.3.3.2 
Packet Error Rate Performance 
11.2.6.1, 11.3.2.4.5 
 
2.2.3.3.3 
Transmit to Receive Recovery Time 
11.3.2.2.1 
 
2.2.3.3.4 
Receiver Signal Attenuation 
11.3.1.13 
 
2.2.3.3.5 
Frequency Search 
11.3.2.4.1 
P1 - 1.3.3.2, P2 - 3.2.3.1.1, Att. 2 
2.2.4 
HF Data Link Subnetwork Data Link Layer Functions 
11.3.3 
 
2.2.4.1 
Data Rate Communications 
 
P2-3.2.2.4, 3.2.3.3 
2.2.4.2 
Selection of Downlink Slot by Aircraft 
11.3.2.3.1 
P2 - 3.2.1, Att. 2 
2.2.4.3 
Maximum MPDU Size Adjustment 
 
P2 - 3.1.1.2, Att. 2 
2.2.4.4 
Data Rate and Interleaver Selection 
 
P1 - 1.3.5, P2 - 2.2.2.4 
2.2.4.5 
Data Rate and Interleaver Selection 
 
P1 - 1.3.5, P2 - 2.2.2.4 
2.2.4.5.1 
SPDU ID 
 
P2 - Fig. II-A1-5, Att. 2 
2.2.4.5.2 
Ground Station Address 
 
P2 - Att. 1, Att. 2 
2.2.4.5.3 
Frame ID 
 
P2 - Att. 2 
2.2.4.5.4 
Slot Acknowledgment Codes 
 
P2 - 3.1.3.3.6, Att. 1, Att. 2 
2.2.4.5.5 
Slot Assignment Codes 
 
P2 - 3.2.1.1.1, 3.2.1.2 
2.2.4.5.6 
Priority Field 
11.3.3.2 
P2 - 3.1.2, Att. 1, Att. 2 
2.2.4.5.7 
Ground Station Active Frequency Field 
 
P2 - Att. 1, Att. 2 
2.2.4.5.8 
Frame Check Sequence 
 
P2 - Att. 2 
MOPS Section 
No. 
Paragraph Title 
ICAO SARPs 
Chapter 11 
Section No. 
ICAO Manual 
On HF Data 
Link  
Section No. 
2.2.4.6 
MPDU Packet Encapsulation 
 
P2 - 3.1.1 
2.2.4.7 
MPDU Format Requirements 
 
P2 - Att. 2 
2.2.4.7.1 
Mid (MPDU ID) Field 
 
P2 - Att. 1, Att 2 
2.2.4.7.2 
GS Field 
 
P2 - Att. 1, Att.2 
2.2.4.7.3 
Aircraft Address Field 
 
P2 - Att. 1 
2.2.4.7.4 
FCS (Frame Check Sequence) 
 
P2 - Att. 1,  Att. 2 
2.2.4.7.5 
Data Field 
 
P2 - Att. 1 
2.2.5.1 
Packet-Mode Data-2 Service Requirements 
11.3.3.3 
P2 - 3.1.1, 3.1.3.3.20 
2.2.5.2 
Packet-Mode Data-3 Service Requirements 
11.3.3.3, 11.3.4.1 
P2 - 3.1.1, 3.1.3 
2.2.5.3 
Priority, Precedence and Preemption (Data/Data) 
11.3.3.2 
P2 - 3.1.2 
2.2.5.4.3 
Join and Leave Event Requirements 
11.3.4.2 
 
2.2.6 
Aircraft Log-on Procedure 
11.3.3.2 
P1 - 1.3.3, P2 - 3.2.2.1, 3.2.3.1, 5.1.1.2, 5.1.1.2.2 

 
Note: Users should recognize that not all possible references have been included. 