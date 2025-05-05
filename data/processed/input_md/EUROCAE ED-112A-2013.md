 
MINIMUM OPERATIONAL PERFORMANCE SPECIFICATION FOR 
 
CRASH PROTECTED AIRBORNE RECORDER SYSTEMS 
This document is the exclusive intellectual and commercial property of EUROCAE. 

It is presently commercialised by EUROCAE. 

This electronic copy is delivered to your company/organisation for internal use exclusively. 

In no case it may be re-sold, or hired, lent or exchanged outside your company. 

ED-112A 
September 2013 Supersedes ED-55 (May 1990), ED-56A (December 1993) and ED-112 (August 2003) 

## Minimum Operational Performance Specification For Crash Protected Airborne Recorder Systems

 
This document is the exclusive intellectual and commercial property of EUROCAE. 

It is presently commercialised by EUROCAE. 

This electronic copy is delivered to your company/organisation for internal use exclusively. 

In no case it may be re-sold, or hired, lent or exchanged outside your company. 

ED-112A 
September 2013 Supersedes ED-55 (May 1990), ED-56A (December 1993) and ED-112 (August 2003) 

## Foreword

1. 
This document was prepared by EUROCAE Working Group 90 "Recording for 
ATM", and was accepted by the Council of EUROCAE on 5 September 2013. 
2. 
EUROCAE is an international non-profit making organisation. Membership is open to manufacturers and users in Europe of equipment for aeronautics, trade associations, national civil aviation administrations and non-European organisations. Its work programme is principally directed to the preparation of performance specifications and guidance documents for civil aviation equipment, for adoption and use at European and world-wide levels. 
3. 
The findings of EUROCAE are resolved after discussion among its members and, where appropriate, in collaboration with RTCA Inc, Washington D.C. USA and/or the Society of Automotive Engineers (SAE), Warrendale, PA, USA through their appropriate committees. 
4. 
The ED-112 document superseded two previously published documents; ED-55 
"Minimum Operational Performance Specification for Flight Data Recorder Systems" of May 1990 (including Amendment 1 of Sept 1998) and ED-56A "Minimum Operational Performance Specification for Cockpit Voice Recorder System" of December 1993 (including Amendment 1 of Nov 1997). It contains the complete contents of the earlier documents, including the following updates and amendments 
ƒ 
Harmonisation of the structure of the documents 
ƒ 
Harmonisation of survivability requirements 
ƒ 
Harmonisation of environmental test requirements 
ƒ 
Harmonisation of FDR recording requirement with ICAO Annex 6 
ƒ 
Harmonisation of recording start/stop criteria 
ƒ 
Providing additional guidance for on-aircraft testing of CVR and FDR systems 
ƒ 
Prohibition of magnetic tape, wire and photographic methods of recording 
ƒ 
Removal of the option to record audio data at reduced quality / merged flight crew channels for data older than 30 minutes  
ƒ 
Clarification of requirements for memory segregation 
ƒ 
Changes to performance requirements during start up and power interruptions 
ƒ 
Additional requirements for relative amplitudes of audio signals from multiple sources 
ƒ 
Clarification of some requirements for survivability testing 
 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

5. 
This 
document 
ED-112A 
supersedes 
ED-112 
"Minimum 
Operational 
Performance Specification for Crash-protected Recorder Systems" of March 2003, for new equipment only. It contains the complete contents of the earlier document, including the following significant updates and amendments 
ƒ 
Harmonization with ICAO documents 
ƒ 
Deployable recorders 
ƒ 
Recorder Independent Power Supply and alternate power source 
ƒ 
Recording contents of data link recorder systems 
ƒ 
Changes to parameter lists 
ƒ 
Removal of some exceptions to general requirements for Cockpit Area Microphone and preamplifier qualification in light of the introduction of GSM technology on aircraft 
ƒ 
Modification of references to data frame layout documents 
ƒ 
Beacon attachment crash survival 
ƒ 
Longer duration classes of CVR 
ƒ 
Maintenance guidance for flight recorders 
ƒ 
Crash-protected memory module size 
ƒ 
Start-up and effect of power interruption 
ƒ 
Environmental qualification standard 
6. 
In addition to ED-55 and ED-56A, ED-112 and ED-112A cover the following new areas: 
ƒ 
Requirements for airborne recording of data link information, derived from the document ED-93."MASPS for CNS/ATM Message Recording Systems", with some differences regarding for example the AOC messages that will be recorded on board where practicable within the system architecture. Everywhere in this document the previous ED-112 "CNS/ATM" wording have been replaced by "data link". 
NOTE: 
Document ED-111 defines requirements for ground based recording for data link. 
ƒ 
Requirements for Image Recording 
ƒ 
Requirements for Automatically Deployable Recorders. 
ƒ 
Requirements for Combined Recorders 
ƒ 
Requirements for Recorder Independent Power Supplies 
7. 
This MOPS is arranged in a series of Sections and Parts which allows the selection of the appropriate requirements for any acceptable combination of recording functions within one or more boxes. It is structured such that individual Parts can be revised independently of the others, and without affecting the main body of the document that applies to all Parts. 
8. 
The Performance Specifications detailed in this document are based on the Standards and Recommended Practices (SARPs) published by ICAO in Annex 6 of the Chicago Convention. Account has been taken of regulations issued by various certification authorities together with the advice and recommendations given by accident investigation specialists. The document represents the minimum standards required for the purposes of accident and incident investigation and is expected to become the basis for new equipment and installation standards to be introduced by the certification authorities. 
9. 
EUROCAE performance specifications are recommendations only. EUROCAE is not an official body of the European governments; its recommendations are valid statements of official policy only when adopted by a particular government or conference of governments. 
10. 
Changes and/or amendments to this document will be notified on the EUROCAE website, in the directory called "documents". 
 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

11. 
Copies of this document may be obtained from: 
 
EUROCAE 
102 rue Etienne Dolet 
92240 Malakoff FRANCE 
 
Tel: +33 1 40 92 79 30 
Fax: +33 1 46 55 62 65 
Email: eurocae@eurocae.net  
Web Site: www.eurocae.net 
 

## Section 1 General Background

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter 1-1 Introduction 1-1.1 Purpose And Scope

This document defines the minimum specification to be met for all aircraft required to carry flight recorders which may record flight data; cockpit audio; images and data link digital messages; in a crash survivable recording medium for the purposes of the investigation of an occurrence (accident or incident). It is applicable to on board crashprotected recorders, ancillary equipment and their installation in civil aircraft. 

## 1-1.1.1 General

This document responds to a need for improved recording of vital information needed for aviation safety investigations. With the rapidly advancing technology used in aircraft, the introduction of data link concepts and the feasibility of digital image recordings, EUROCAE recognized the need to revise recorder requirements and to integrate all of the accident investigation recording requirements into one complete, integrated document. This document therefore defines all recording functions (flight data, cockpit voice, images & data link) as individual Parts along with a common section, applicable to all Parts. Parts may be revised independently of each other and independently of the main body of this document. A similar MOPS exists for lightweight flight recording systems.  

## 1-1.1.2 Description Of Content

This document is divided in to five sections, and four parts, as shown in Figure 1-1.1. Section 1 describes typical equipment applications and operational objectives. Background material and accident/incident investigation considerations are included together with a description of the recording systems. Definitions and Abbreviations essential to proper understanding of this document are provided. Section 2 defines the requirements that are common to all crash-protected recording systems. Section 3 defines the requirements that are specific to Deployable Recorders. Section 4 defines the requirements that are specific to Combined Recorders. Section 5 defines the requirements that are specific to Recorder Independent Power Supplies. Part I defines the requirements that are specific to Cockpit Voice Recorder Systems. 

Part II defines the requirements that are specific to Flight Data Recorder Systems. Part III defines the requirements that are specific to Image Recorder Systems. Part IV defines the requirements that are specific to Airborne Data Link Recorder Systems. Table 1-1.1 provides examples of possible recorder unit configurations, and the sections and parts that would be applicable. Table 1-1.2 provides a matrix of recommended combinations of equipment to satisfy aircraft operational rules, based on an assumption that at least two boxes are required if more than one recorder type is required. All flight recording systems shall be designed to meet the criteria of Sections 1 and 2 plus the relevant function specific section(s) and Parts. 

## 1-1.2 Application 1-1.2.1 Voice Recording (Part I Of This Document)

Voice recording shall include voice communications between flight crew members, voice communications between the flight crew and any other station, and the acoustic environment of the cockpit. 

1-1.2.2 
Flight Data Recording (Part II of this document) 
Data recordings shall continuously record parameters required to accurately determine flight path, speed, attitude, engine power, configuration and operation. The specific parameters required will depend upon aircraft complexity, data sources available and on the need to record certain essential parameters. 

1-1.2.3 
Image Recording (Part III of this document) 
Image recording shall include images depicting the ambient conditions in the cockpit; flight crew activity; instruments and control panels. 

1-1.2.4 
Data link Recording (Part IV of this document) 
Data link recording shall record those messages whereby the flight path of the aircraft is authorised, directed or controlled, and which are relayed over a digital data link rather than by voice communication. 

## 1-1.3 Technical Background 1-1.3.1 Combined Recorders

Investigators are opposed to a single combined recorder installed on large aircraft, as defined by regulation, because the loss of such a recorder would result in the complete loss of all information. Combined recorders can now conceivably record data, voice, data link and images, all in one box. Recent accident investigations have highlighted the need to consider two combined recorders, one installed near the cockpit and one installed towards the rear of the aeroplane for redundancy. A forward mounted recorder has the advantage of shorter lines between the cockpit area microphone and boom microphones to the recorder, reducing the chance of the wires being breached during an in-flight fire or break-up. Traditional aft-mounted recorders maximize impact survivability. The use of two redundant, multi-function recorders installed in the forward and tail sections provides operational as well as accident investigation benefits. The redundancy created by using two combined recorders increases the probability of recovering all of the information following an accident. Combined recorders would benefit the airlines by providing commonality of parts and test equipment, reduced technical training, and possible time extensions with respect to the Minimum Equipment List (MEL) because of the redundancy. 

## 1-1.3.2 Audio Recordings Duration

The 30-minute CVR recording capacity was predicated upon the technology available in the early 1960s; this was the amount of tape that could be crash-protected. Investigators are concerned that 30 minutes of recording time is no longer adequate to capture the initiating events and important background information to many accidents. For example, in accidents involving in-flight fire, the initiating events can develop over a period of time longer than 30 minutes. Longer CVR recording capacity also facilitates the investigation of non-catastrophic occurrences, occurrences in which current 30-minute recordings are often overwritten by the time the aircraft has safely stopped on the ground. Current technology easily accommodates increased CVR recording capacity. In fact, the majority of newly manufactured solid-state memory CVRs have a two-hour recording capacity, and there is a worldwide industry move towards two-hour CVRs. Some states have mandated that they be fitted to all aircraft manufactured after 1998 and are over 5700 kg. As a consequence of ICAO now requiring the investigation of serious incidents, the duration of CVR recordings could be extended to 10, 15 or 25 hours. This document adds three new classes of CVR for these durations. 

 

## 1-1.3.3 Alternate Power Source

Power interruptions have resulted in flight recorder information not being captured during the last few seconds to as high as several minutes during recent major aircraft occurrences. This lack of recorded information has hampered the accident investigation. "alternate" means separate from the power source that normally provides power to the CVR.  The use of aeroplane batteries or other power sources are acceptable provided that the requirements above are met and electrical power to essential and critical loads is not jeopardized. It is now feasible to power newtechnology (solid state) Cockpit Voice Recorder (and the cockpit area microphone) and Airborne Image Recorder (and the camera(s)) independently of normal recorder power for a specific period of time in the event that aircraft power sources to the recorder(s) are interrupted or lost. In modern aircraft, flight data and other data from multiple sources are used by the aircraft systems and by the flight crew to operate the aircraft. To record the required parameters, the FDR system monitors the data flowing through data buses. If electrical power to a particular sensor or data bus is lost, FDR information pertaining to that sensor or data bus will no longer be available. In the event of a total loss of electrical power, essentially there would be no data to record. There may be merit in independently powering the FDR and its flight data acquisition unit in order to capture whatever data are available during partial electrical failures. However, as a minimum, the Cockpit Voice Recorder (and its cockpit area microphone) and the Airborne Image Recorder (and its camera(s)) should continue to be powered for short periods regardless of the availability of normal recorder electrical power. This alternate power source would allow the continued recording of the acoustic and image environment of the cockpit, for a specific period. The addition of a requirement and specifications for a 10 minute recorder independent power supply have therefore been introduced in this MOPS, predicated upon at least a two-hour duration audio and image recording. 

## 1-1.3.4 Obsolete Technology

Many operators are voluntarily replacing their old technology (tape) data and voice recorders with modern, solid-state recorders. The use of these new recorders not only serves safety but also benefits operators directly, as they avoid the high costs and technical problems associated with maintaining outdated old-technology recorders. Additionally, existing tape recorders no longer meet the most recent EASA/FAA Technical Standard Orders ((E)TSO) crash-worthiness standards, nor those specified in this MOPS. 

## 1-1.3.5 Use Of Non-Mandatory Fdrs And Other Flight Recorders

FDR early designs were such that it was very cumbersome to download the information for the investigation of minor incidents or for the purpose of monitoring the data on a regular basis for prevention and maintenance purposes, such as Flight Data Analysis Programs. Consequently, manufacturers developed 'Quick Access', 'Direct Access' and 'Maintenance' recorders. These recorders were typically a replaceable media, such as tape cartridge or optical disk, which could be quickly swapped out when the aircraft landed. Over time, these voluntary systems began to record more information than the mandatory system. Accident investigators want to ensure that mandatory systems record as much information as practical. With today's solid state technology, significantly increased capacities, readily available data on the aircraft and affordable ground based wireless download capabilities, an integrated crash-protected flight recording system which satisfies both accident investigators and operator's routine playback needs is highly desirable. It is recommended that industry provide operators with solutions that protect the core mandatory list while allowing for the operator to change the recorded data (e.g.: additional data, sample rates or resolutions) in the crash-protected recording medium without requiring re-certification of the flight recording system. (Refer to EUROCAE ED-12B / RTCA DO-178B Section 2.4) 
As operators begin to use additional data to make operational and maintenance decisions, it is important that these parameters be properly recorded and that accident investigators have the same data set available in the aftermath of an accident. A significant additional benefit to using the data set recorded on the FDR for Flight Data Analysis Programs is that the probability that the FDR will be functional at the time of an accident is improved dramatically. 

## 1-1.3.6 Electronic Documentation Standard

This MOPS also contains reference to an acceptable means to exchange parameter configuration documentation between ground replay stations in order to facilitate timely playback of recorded data in engineering units. 

## 1-1.3.7 Units Of Measurement

The measurements are expressed, where appropriate, in SI units. The approximate equivalent imperial units are given in parenthesis. 

## 1-1.4 Mandating And Recommendation Phrases

a.  
"Shall" The use of the word "Shall" indicates a mandated criterion; i.e. compliance with the particular procedure or specification is mandatory and no alternative may be applied. 

b.  
"Should" The use of the word "Should" (and phrases such as "It is recommended that...", etc.) indicates that although the procedure or criterion is regarded as the preferred option, alternative procedures, specifications or criteria may be applied, provided that the manufacturer, installer or tester can provide information or data to adequately support and justify the alternative. 

## 1-1.5 Common Definitions And Abbreviations

The definitions and abbreviations of ICAO Annex 5, Annex 6 and Annex 10 are applicable. 

## 1-1.5.1 Definition Of Terms

The following definitions are provided for the terms that are used in this document.  

| Accident                                                     | An occurrence associated with the operation of an aircraft    |
|--------------------------------------------------------------|---------------------------------------------------------------|
| which, in the case of a manned aircraft, takes place         |                                                               |
| between the time any person boards the aircraft with the     |                                                               |
| intention of flight until such time as all such persons have |                                                               |
| disembarked, or in the case of an unmanned aircraft,         |                                                               |
| takes place between the time the aircraft is ready to move   |                                                               |
| with the purpose of flight until such time as it comes to    |                                                               |
| rest at the end of the flight and the primary propulsion     |                                                               |
| system is shut down, in which:                               |                                                               |
| a)                                                           | a person is fatally or seriously injured as a result of:      |
| -                                                            |                                                               |

-  
direct contact with any part of the aircraft, including parts which have become detached from the aircraft, or 
-  
direct exposure to jet blast, 
except when the injuries are from natural causes, self-inflicted or inflicted by other persons, or when the injuries are to stowaways hiding outside the areas normally available to the passengers and crew; or 

 
b) 
the aircraft sustains damage or structural failure which: -  
adversely affects the structural strength, 
performance or flight characteristics of the aircraft, and 
-  
would normally require major repair or replacement of the affected component, 
except for engine failure or damage, when the damage is limited to a single engine, (including its cowlings or accessories), to propellers, wing tips, antennas, probes, vanes, tires, brakes, wheels, fairings, panels, landing gear doors, windscreens, the aircraft skin (such as small dents or puncture holes), or for minor damages to main rotor blades, tail rotor blades, landing gear, and those resulting 
from hail or bird strike (including holes in the radome); or 
c) 
the aircraft is missing or is completely inaccessible. 
NOTE 1:  
For statistical uniformity only, an injury resulting in death within thirty days of the date of the accident is classified, by ICAO, as a fatal injury. 
NOTE 2:  
An aircraft is considered to be missing when the official search has been terminated and the wreckage has not been located. 
NOTE 3:  
The type of unmanned aircraft system to be investigated is addressed in 5.1 of ICAO Annex 13. 
NOTE 4:  
Guidance for the determination of aircraft damage can be found in ICAO Annex 13 Attachment G . 

| Aircraft                                                    | Any machine that can derive support in the atmosphere    |
|-------------------------------------------------------------|----------------------------------------------------------|
| from the reactions of the air other than the reactions of   |                                                          |
| the air against the earth's surface.                        |                                                          |
| AOC                                                         | The ICAO definition of Aeronautical Operational Control  |
| (AOC) is communication required for the exercise of         |                                                          |
| authority over the initiation, continuation, diversion or   |                                                          |
| termination of flight for safety, regularity and efficiency |                                                          |
| reasons. (Annex 10, Part III)                               |                                                          |
| NOTE:                                                       |                                                          |
| The airlines use the term Airline Operational               |                                                          |
| Communication (AOC) for this type of                        |                                                          |
| communication. ICAO uses the abbreviation                   |                                                          |
| "AOC" for different purpose. See below. Thi                 | s                                                        |
| document uses the ICAO meanings for these                   |                                                          |
| terms.                                                      |                                                          |
| APC                                                         | Aeronautical Passenger Communication (APC) is data       |
| link communication relating to the non-safety audio and     |                                                          |
| data services to passengers and crew members for            |                                                          |
| personal communication.                                     |                                                          |
| Approval                                                    | An act or instance of expressing a favourable opinion or |
| giving formal or official sanction.                         |                                                          |

ATSC 
The ICAO definition of air traffic service communication (ATSC) is communications related to air traffic services including air traffic control, aeronautical and meteorological information, position reporting and services related to safety and regularity of flight. This communication involves one or more air traffic service administrations. This term is used for purposes of address administration. (Annex 10, Part III) 

| ATC                                                         | Air Traffic Control. In this context, the use of safety-   |
|-------------------------------------------------------------|------------------------------------------------------------|
| related data link communication for the purpose of:         |                                                            |
| a)                                                          | Preventing collisions between aircraft, and on the         |
| manoeuvring                                                 | area                                                       |
| obstructions;                                               |                                                            |
| b)                                                          | Expediting and maintaining an orderly flow of              |
| traffic.                                                    |                                                            |
| ATM                                                         | Air Traffic Management. A system consisting of a ground    |
| and air part, to ensure the efficient and safe movement of  |                                                            |
| aircraft during all phases of operation. The system         |                                                            |
| includes equipment, people and procedures.                  |                                                            |
| ATS                                                         | Air Traffic Services. A generic term meaning variously,    |
| flight information service, alerting service, air traffic   |                                                            |
| advisory service, air traffic control service (area control |                                                            |
| service, approach control service or aerodrome control      |                                                            |
| service).                                                   |                                                            |
| Camera                                                      | Within this document includes thermal imagers, image       |
| sensors and other electronic pick-up devices.               |                                                            |
| Certification                                              | Legal recognition by a Certification Authority that a    |
|------------------------------------------------------------|----------------------------------------------------------|
| product, service, organisation or person complies with the |                                                          |
| applicable requirements. Such certification comprises the  |                                                          |
| activity of technically checking the product, service,     |                                                          |
| organisation or person and the formal recognition of       |                                                          |
| compliance with the applicable requirements by issue of a  |                                                          |
| certificate, licence, approval or other documents as       |                                                          |
| required by national laws and procedures. In particular,   |                                                          |
| certification of a product involves:                       |                                                          |
| a)                                                         | the process of assessing the design of a product to      |
| ensure that it complies with a set of standards            |                                                          |
| applicable to that type of product so as to                |                                                          |
| demonstrate an acceptable level of safety,                 |                                                          |

b) 
the process of assessing an individual product to ensure that it conforms with the certificated type design, 

| c)                                                       | the issue of a certificate required by national laws       |
|----------------------------------------------------------|------------------------------------------------------------|
| to declare that compliance or conformity has been        |                                                            |
| found with applicable standards in accordance with       |                                                            |
| items (a) or (b) above.                                  |                                                            |
| Certification Authority                                  | The organization or person responsible within the state or |
| country concerned with the certification of compliance   |                                                            |
| with applicable requirements.                            |                                                            |
| Channel                                                  | A path that allows a signal to be transmitted or processed |
| in a deterministic manner independently of other signals |                                                            |
|                                                          |                                                             |           |              | CNS    | Communications, Navigation and Surveillance. The way    |
|----------------------------------------------------------|-------------------------------------------------------------|-----------|--------------|--------|---------------------------------------------------------|
| in                                                       | which                                                       | enhanced  | capabilities | of     | satellite-based                                         |
| navigation and digital data link communication systems   |                                                             |           |              |        |                                                         |
| will permit the next generation of ATM systems to        |                                                             |           |              |        |                                                         |
| combine the features of ADS and CPDLC with the           |                                                             |           |              |        |                                                         |
| conventional ATC functions.                              |                                                             |           |              |        |                                                         |
| Cockpit Voice Recorder                                   | A device that uses a combination of microphones and         |           |              |        |                                                         |
| other audio and digital inputs to collect and record the |                                                             |           |              |        |                                                         |
| aural environment of the cockpit and communications to,  |                                                             |           |              |        |                                                         |
| from and between the flight crew members.                |                                                             |           |              |        |                                                         |
| Combined Recorder                                        | A single flight recorder that combines the functions of two |           |              |        |                                                         |
| or more accident recording functions in a single, crash- |                                                             |           |              |        |                                                         |
| protected box.                                           |                                                             |           |              |        |                                                         |
| Correlation                                              | The parallel relationship of two or more corresponding      |           |              |        |                                                         |
| events                                                   |                                                             |           |              |        |                                                         |
| Corrupted Data/Record                                    | Any data item or record which has been altered in a way     |           |              |        |                                                         |
| other than the one intended by design.                   |                                                             |           |              |        |                                                         |
| Crash                                                    | Refer to "Reportable Accident"                              |           |              |        |                                                         |
| The                                                      | protected                                                   | enclosure | containing   | the    | memory                                                  |
| memory module                                            | module(s)                                                   |           |              |        |                                                         |
| Data link                                                   | Aeronautical two-way data communications.                |
|-------------------------------------------------------------|----------------------------------------------------------|
| Deployable Recorder                                         | Any crash-protected recorder (CVR, FDR or other) which   |
| is designed to be automatically separated from the          |                                                          |
| aircraft only in the event of an accident.                  |                                                          |
| Ditching                                                    | Controlled emergency landing on water.                   |
| Down-link                                                   | Transmission from air to ground.                         |
| Download                                                    | Means of copying the digital data (also known as "raw"   |
| data) stored in the crash-protected memory module for       |                                                          |
| replaying at a later time.                                  |                                                          |
| Filtered Flight Data                                        | A flight data signal is filtered when an original sensor |
| signal is changed in any way, other than changes            |                                                          |
| necessary to accomplish analog to digital conversion of     |                                                          |
| the signal; format a digital signal to be DFDR compatible;  |                                                          |
| eliminate a high freqeucny component of a signal outside    |                                                          |
| the operational bandwidth of the sensor.                    |                                                          |
| Flight Crew                                                 | A licensed crew member charged with duties essential to  |
| the operation of an aircraft during a flight duty period.   |                                                          |
| Flight Data Recorder                                        | A device or devices that uses a combination of data      |
| providers to collect and record parameters that reflect the |                                                          |
| state and performance of an aircraft.                       |                                                          |
| Flight Recorder                                             | Any type of recorder installed in the aircraft for the   |
| purpose of complementing accident/incident investigation    |                                                          |
| or flight analysis.                                         |                                                          |
| Flight time                                                 | The total time from the moment an aeroplane first moves  |
| for the purpose of taking off until the moment it finally   |                                                          |
| comes to rest at the end of the flight.                     |                                                          |
| Follow-on Installation                                      | A production series installation performed in accordance |
| with a previously certified configuration (e.g. a follow-on |                                                          |
| from a Type Certificate (TC), Supplemental Type             |                                                          |
| Certificate (STC) or Major Modification).                   |                                                          |
| Image Recorder                                             |
|------------------------------------------------------------|
| and record information that reflects the status of various |
| parts of the aircraft (internal and external).             |

Incident An occurrence, other than an accident, associated with the operation of an aircraft which affects or could affect the safety of operation. 

NOTE:  
The types of incidents which are of main interest to the International Civil Aviation Organization for accident prevention studies are listed in Annex 13 Attachment C. 

| Initial Installation                              | The installation for initial certification of the recording    |
|---------------------------------------------------|----------------------------------------------------------------|
| system.                                           |                                                                |
| Interconnection Harness                           | The electrical wiring that connects one system functional      |
| element to another e.g. between a crash-protected |                                                                |
| memory module and the flight recorder interface   |                                                                |
| electronics.                                      |                                                                |
| Interphone                                                 | An audio system that enables flight crew members to      |
|------------------------------------------------------------|----------------------------------------------------------|
| communicate with each other in the cockpit or with other   |                                                          |
| personnel elsewhere on the aircraft.                       |                                                          |
| Long term RMS                                              | A signal that remains constant for a period of several   |
| seconds                                                    |                                                          |
| Maintenance                                                | The                                                      |
| modification and repair throughout the lifetime of an      |                                                          |
| aircraft needed to ensure that the aircraft remains in     |                                                          |
| compliance with the certificated type design and           |                                                          |
| consistent with a high standard of safety; this includes   |                                                          |
| modifications made mandatory by the authorities.           |                                                          |
| Maintenance                                                | The                                                      |
| modification and repair throughout the lifetime of an      |                                                          |
| aircraft needed to ensure that the aircraft remains in     |                                                          |
| compliance with the certificated type design and           |                                                          |
| consistent with a high standard of safety; this includes   |                                                          |
| modifications made mandatory by the authorities.           |                                                          |
| Memory Device                                              | The smallest separate physical element in which data can |
| be stored and recovered (e.g. chips).                      |                                                          |
| Memory module                                              | The assembly, within the Crash-protected Memory          |
| Module, containing the memory devices used to retain the   |                                                          |
| recorded data.                                             |                                                          |
| Nominal                                                    | Value commonly used and considered between the           |
| minimal and maximal values                                 |                                                          |
| Operating crew                                             | Any person who is on board with the consent of the       |
| operator of the aircraft and has duties in relation to the |                                                          |
| flying or safety of the aircraft.                          |                                                          |
| Operator                                                   | The person for the time being having the management of   |
| that aircraft.                                             |                                                          |
| Partitioning                                             | A technique for providing isolation between independent    |
|----------------------------------------------------------|------------------------------------------------------------|
| functions to prevent interaction in normal operation and |                                                            |
| under fault conditions. Partitioning design considers:   |                                                            |
| a)                                                       | Hardware                                                   |
| devices, I/0 devices, interrupts, and timers,            |                                                            |
| b)                                                       | Control coupling: vulnerability to external access,        |
| c)                                                       | Data coupling: shared or overlaying data, including        |
| stacks and processor registers,                          |                                                            |
| d)                                                       | Failure modes of hardware devices associated with          |
| the protection mechanisms,                               |                                                            |
| e)                                                       | In a CVR system, assurance that the allocation of          |
| channels                                                 | in                                                         |
| deterministic                                            |                                                            |
| Pilot-in-Command                                               | The pilot designated by the operator, or in the case of    |
|----------------------------------------------------------------|------------------------------------------------------------|
| general aviation, the owner, as being in command and           |                                                            |
| charged with the safe conduct of a flight.                     |                                                            |
| Public Address                                                 | A means by which flight crew members can broadcast a       |
| message within the aircraft cabin.                             |                                                            |
| Recording                                                      | The act of making certain data persistent, with a view to  |
| subsequent replay or analysis.                                 |                                                            |
| Replay                                                         | The                                                        |
| situations/scenarios.                                          |                                                            |
| Retrieval                                                      | Retrieval of data from the recording medium for the task   |
| of presenting the data for analysis purposes.                  |                                                            |
| Segregation                                                    | The physical separation of memory devices within a         |
| recorder crash-protected memory module.                        |                                                            |
| Sidetone                                                       | Output audio level control through the transceiver and     |
| interphone (including the sound of the speaker's voice         |                                                            |
| and background noise as picked up by the microphone            |                                                            |
| and received audio) reproduced in the speaker's own            |                                                            |
| head set.                                                      |                                                            |
| Silence editing                                                | Device which purpose is to put a threshold and to          |
| improve detection on silence intervals in a speech signal      |                                                            |
| Simulation                                                     | The use of a laboratory-installed system of avionic        |
| components ('test bench') representative of the aircraft in    |                                                            |
| which the recording system is to be certified. The test        |                                                            |
| bench may be controlled by a computer-based system             |                                                            |
| including analogue and discrete inputs, to create specific     |                                                            |
| operating conditions, such as 90° pitch up, or other           |                                                            |
| conditions that cannot be tested in flight or are difficult to |                                                            |
| test on the aircraft. The test bench should be configured      |                                                            |
| such that the computer or analogue inputs to the system        |                                                            |
| drive the instruments and displays in a way representative     |                                                            |
| of the aircraft. All avionic components installed in the test  |                                                            |
| bench should be either of production standard or               |                                                            |
| representative of the final production configuration.          |                                                            |
| Software                                                       | Computer                                                   |
| documentation and data pertaining to the operation of a        |                                                            |
| computer system.                                               |                                                            |
| Solid State                                                    | An electronic device that is capable of performing a       |
| function                                                       | without                                                    |
| semiconductor material or similar.                             |                                                            |

Sound Pressure Level In decibels (dB), the Sound Pressure Level is 20 times the logarithm to the base 10 of the ratio of the pressure of this sound to the reference pressure. The reference pressure is 20 µPa, and shall be explicitly stated along with the Sound Pressure Level, such as: _dB above 20 µPa. 

Speech Transmission Index  
A method of quantifying the intelligibility of speech with respect to the transmission media and which is based on differences produced by the media to the temporal speech envelope between speaker and listener. 
Stimulation 
The use of test equipment, traceable to a known standard, to induce aircraft systems to produce a specific result. 
Synchronisation 
A technique to align two independent events to a common point in time 
Telephone 
Audio reception (radio or interphone) 
Test 
A means of demonstrating compliance, using a test aircraft 
in 
a 
configuration 
representative 
of 
the 
configuration to be certified, in a ground and/or flight environment; 
Timebase 
A signal which provides the reference time for other recorded signals. 
Timescale 
A defined scale to be used in relation to the timebase signal. 
Up-link 
Transmission from ground to air 
Volume control setting 
Channel gain level or equivalent 

## 1-1.5.2 Abbreviations

| AAC    | Aeronautical Administrative Communication    |
|--------|----------------------------------------------|
| ABS    | Absolute                                     |
| AC     | Alternating Current/Advisory Circular        |
| ACAS   | Airborne Collision and Avoidance System      |
| ACF    | Auditory Correction Factor                   |
| ADS    | Automatic Dependent Surveillance             |
| ADS-B  | Automatic Dependent Surveillance Broadcast   |
| ADS-C  | Automatic Dependent Surveillance-Contract    |
| AF     | Audio Frequency                              |
| AFCS   | Automatic Flight Control System              |
| AFSK   | Audio Frequency-Shift Keying                 |
| AFN    | ATS Facility Notification                    |
| AGC    | Automatic Gain Control                       |
| AIR    | Airborne Image Recorder                      |
| AMF    | Auditory Masking Factor                      |
| ANP    | Actual Navigation Performance                |
| ANSI   | American National Standards Institute        |
| AOC    | Aeronautical Operational Control             |
| APC    | Aeronautical Passenger Communication         |

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

| APU    | Auxiliary Power Unit                    |
|--------|-----------------------------------------|
| ATC    | Air Traffic Control                     |
| ATIS   | Automatic Terminal Information Services |
| ATM      | Air Traffic Management                              |
|----------|-----------------------------------------------------|
| ATN      | Aeronautical Telecommunications Network             |
| ATR      | Air Transport Racking                               |
| ATS      | Air Traffic Services                                |
| ATSC     | Air Traffic Services Communication                  |
| ATSU     | Air Traffic Services Unit                           |
| BITE     | Built-in Test Equipment                             |
| Btu      | British Thermal Units                               |
| C        | Celsius                                             |
| CAS      | Computed Air Speed                                  |
| CM       | Context Management                                  |
| CMU      | Communications Management Unit                      |
| CNS      | Communications, Navigation and Surveillance         |
| CO2      | Carbon Dioxide                                      |
| CPDLC    | Controller / Pilot Data Link Communications         |
| CVR      | Cockpit Voice Recorder                              |
| dB       | Decibels                                            |
| DC       | Direct Current                                      |
| DCL      | Departure Clearance                                 |
| D-FIS    | Digital Flight Information Services                 |
| DL       | Data Link                                           |
| DME      | Distance Measuring Equipment                        |
| EASA     | European Aviation Safety Agency                     |
| EFIS     | Electronic Flight Instrument System                 |
| EGT      | Exhaust Gas Temperature                             |
| EIRP     | Effective Isotropic Radiated Power                  |
| ELT      | Emergency Locator Transmitter                       |
| EPE      | Estimated Position Error                            |
| EPU      | Estimated Position Uncertainty                      |
| EPR      | Engine Pressure Ratio                               |
| EUROCAE  | European Organisation for Civil Aviation Equipment  |
| FANS 1/A | Future Air Navigation Systems for Boeing and Airbus |
| aircraft |                                                     |
| FAA      | Federal Aviation Administration                     |
| FDAU     | Flight Data Acquisition Unit                        |
| FDR      | Flight Data Recorder                                |
| FIS      | Flight Information Services                         |
| FLIREC   | Flight Recorder Panel (of ICAO)                     |
| FRED     | Flight Recorder Electronic Documentation            |
| ft       | Feet                                                |
| g        | Gravitational Acceleration                          |
| GMT      | Greenwich Mean Time                                 |
| GNSS     | Global Navigation Satellite System                  |
| GPS      | Global Positioning System                           |
| HF       | High Frequency (3-30 MHz)                           |
| Hz       | Hertz                                               |
| IAN      | Integrated Approach Navigation                      |
| ICAO     | International Civil Aviation Organization           |

IEC 
International Electrotechnical Commission IFALPA 
International Federation of Air Line Pilots Associations ILS 
Instrument Landing System in Inches IRNAV 
Integrated Area Navigation ISASI 
The International Society of Air Safety Investigators ISO 
International Organization for Standardization kbps Kilobits-per-second kg Kilograms kHz Kilohertz kN 
Kilonewtons kPa Kilopascals kt Knots kW  
Kilowatts L 
Left lb Pounds LE 
Leading Edge lEEE 
Institute of Electrical & Electronic Engineers LRU 
Line Replaceable Unit LSB 
Least Significant Bit LSP 
Least Significant Part m Metres m/s Metres/Second MASPS 
Minimum Aviation System Performance Specification mb Millibars MCTOM 
Maximum Certified Take Off Mass MEL 
Minimum Equipment List MLS 
Microwave Landing System mm Millimetres Mode-S 
Mode Selective MOPS 
Minimum Operational Performance Specification 

| ms     | Milliseconds          |
|--------|-----------------------|
| MSB    | Most Significant Bit  |
| MSP    | Most Significant Part |

MTF 
Modulation Transfer Function N1 
Fan Speed 

N2 
Intermediate/High Pressure Spool Speed 

N3 
High Pressure Spool Speed NAV 
Navigation NF 
Free Power Turbine Speed NG 
Gas Generator Speed NM 
Nautical Miles NP 
Propeller Speed NR 
Rotational Speed OCL 
Oceanic Clearances OEM 
Original Equipment Manufacturer p Parity Pa Pascal PA 
Public Address PLA 
Power Lever Angle PTT 
Push To Talk R 
Right RIPS 
Recorder Independent Power Supply rms Root Mean Square RNP 
Required Navigation Performance RPM 
Revolutions Per Minute RTCA 
RTCA Inc. 

s Seconds SAE 
Society of Automotive Engineers SARPs Standards and Recommended Practices SAS 
Stability Augmentation System SATCOM 
Satellite Communications SDI 
Source Destination Indicator SNR 
Signal-to-Noise-Ratio SOP 
Standard Operating Procedures SPL 
Sound Pressure Level SSCVR 
Solid State Cockpit Voice Recorder SSFDR 
Solid State Flight Data Recorder SSM 
Sign Status Matrix STC 
Supplemental Type Certificate STI 
Speech Transmission Index SYNC 
Synchronise TBD 
To Be Defined TCAS 
Traffic Collision Avoidance System TE 
Trailing Edge THD  
Total Harmonic Distortion TLA 
Thrust Lever Angle TSO 
Technical Standard Order UTC 
Universal Time Co-ordinate V 
Volts VD 
Velocity - Design Diving VHF 
Very High Frequency (30-300 MHz) 
VMO 
Maximum Operating Limit Speed VOR 
VHF Omni-directional Radio Range WG 
Working Group 

## 1-1.6 List Of Reference Documents

EUROCAE ED-12B / RTCA DO-178B - Software Considerations in Airborne Systems and Equipment Certification EUROCAE ED-14G / RTCA DO-160G - Environmental Conditions and Test Procedures for Airborne Equipment EUROCAE ED-55 - Minimum Operational Performance Specification for Flight Data Recorder Systems EUROCAE ED-56A - Minimum Operational Performance Specification for Cockpit Voice Recorder Systems EUROCAE ED-62A - Minimum Operational Performance Specification for Aircraft Emergency Locator Transmitters (406MHz and 121.5 MHz - optional 243 MHz) EUROCAE ED-78A / RTCA DO-264 - Guidance Material for the Establishment of Data Link supported ATS Services EUROCAE ED-80 / RTCA DO-254 - Design Assurance Guidance for Airborne Electronic Hardware EUROCAE ED-93 - Minimum Aviation Systems Performance Specification for CNS/ATM Message Recorder Systems EUROCAE ED-111 - Functional Specifications and Operational Procedures for CNS/ATM Ground Recording EUROCAE ED-112 - Minimum Operational Performance Specification for Crashprotected Airborne Recorder Systems EUROCAE ED-155 - Minimum Operational Performance Specifications for Lightweight Aircraft Recording Systems ICAO International Standards and Recommended Practices - Operation of Aircraft, ANNEX 6, Parts I, II and III ICAO International Standards and Recommended Practices - Aircraft Accident and Incident Investigation, ANNEX 13 ICAO SARPS - CNS/ATM Package 1 "Manual of Technical Provisions for the ATN" - ICAO Doc 9705 - AN956 - 1998 IEC 225 - Octave, Half Octave and Third Octave Band Filters Intended For The Analysis Of Sounds And Vibrations (1966) IEC 651- Sound Level Meters (1979) RTCA DO-204 - Minimum Operational Performance Standards for 406 MHz Emergency Locator Transmitters (ELT) 
RTCA DO-212 - Minimum Operational Performance Standards for Airborne Automatic Dependent Surveillance RTCA DO-214 - Audio Systems Characteristics and Minimum Operational Performance Standards for Aircraft Audio Systems and Equipment. RTCA DO-219 - Minimum Operational Performance Standards for ATC Two-Way Data link Communication 

## 1-1.7 Related Documents

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
ARINC Specification 404A - Air Transport Equipment Cases and Racking ARINC Report 660A, - CNS/ATM Avionics, Functional Allocation and Recommended Architectures ARINC Characteristic 573 - Aircraft Integrated Data System ARINC Specification 647A - Flight Recorder Electronic Documentation ARINC Characteristic 717 - Flight Data Acquisition and Recording System ARINC Characteristic 747 - Flight Data Recorder ARINC Characteristic 757 - Cockpit Voice Recorder ARINC Characteristic 767 - Enhanced Airborne Flight Recorder (EAFR) ARINC Characteristic 777 - Recorder Independent Power Supply EIA RS-232 - Interface between Data Terminal Equipment and Data Communication Equipment employing Serial Binary Data Interchange EIA RS-422A - Electrical Characteristics of Balanced Voltage Digital Interface Circuits IEEE Standard 488 - Standard Interface for Programmable Instrumentation SAE Aerospace Standard AS 8039 - General Aviation Flight Recorder SAE Aerospace Standard AS 8045(A) - Underwater Locating Devices (Acoustic) (Self-powered) 

| Section                                              | Part    |
|------------------------------------------------------|---------|
| Recorder Type                                        |         |
| 1                                                    | 2       |
| CVR only, non-deployable                             | X       |
| CVR combined with data link, non-deployable          | X       |
| CVR combined with data link and FDR, deployable      | X       |
| CVR combined with FDR, non-deployable, internal RIPS | X       |
| Image combined with FDR, non-deployable              | X       |
| CVR combined with FDR and data link, non-deployable  | X       |
| CVR, FDR, data link, and Image, deployable           | X       |
| --```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---   |         |
|                                                      |         |
|                                                      |         |
| Operating Rule Requires    | Recommended Configuration    |
|----------------------------|------------------------------|
| CVR                        | FDR                          |
| Data                       |                              |
| link                       |                              |
|                            |                              |
| AIR                        | 1 box                        |
|                            |                              |
| X                          |                              |
| X                          |                              |
| CVR/                       |                              |
| data link                  |                              |
|                            |                              |
|                            |                              |
| X                          |                              |
| X                          |                              |
| CVR/                       |                              |
| data link                  |                              |
| / AIR                      | 1 CVR/                       |
| data link                  |                              |
| & 1 AIR                    |                              |
|                            |                              |
|                            | X                            |
|                            | X                            |
| FDR/                       |                              |
| data link                  |                              |
|                            |                              |
|                            |                              |
|                            | X                            |
|                            | X                            |
| FDR/                       |                              |
| data link                  |                              |
| / AIR                      | 1 FDR/                       |
| data link                  |                              |
| & 1 AIR                    |                              |
|                            |                              |
| X                          | X                            |
| X                          | X                            |
| X                          | X                            |
| X                          | X                            |
2 CVR/FDR 
or 
1 CVR & 1 FDR 
or 
 
1 CVR/FDR & 1 FDR 
or 
1 CVR/FDR & 1 CVR 
2 CVR/FDR/data link 
or 
1 CVR/data link &  
1 FDR/data link 
or 
1 CVR/data link/FDR &  
 
1 FDR 
or 
1 CVR/data link/FDR &  
1 CVR 
or 
1 CVR/data link & 1 FDR 
2 CVR/FDR/AIR 
1 CVR & 1 FDR & 1 AIR 
or 
or 
1 CVR & 1 FDR/AIR 
2 CVR/FDR & 1 AIR 
or 
or 
1 CVR/AIR & 1 FDR 
2 CVR/AIR & 1 FDR 
or 
or 
1 CVR/AIR & 1 FDR/AIR 
1 CVR & 2 FDR/AIR 
2 CVR/FDR/data link/AIR 
or 
1 CVR/data link 
1 FDR/data link/AIR 
1 CVR/data link 
1 FDR/data link 
or 
1 AIR 
1 CVR/data link/AIR 
or 
1 FDR/data link 
2 CVR/data link/FDR 
or 
1 AIR 
or 
1 CVR/data link/FDR 
2 CVR/data link/AIR 
1 FDR/data link/AIR 
1 FDR/data link 
or 
or 
1 CVR/data link/AIR 
1 CVR/data link 
1 CVR/data link/FDR 
or 
2 FDR/data link/AIR 
1 CVR/data link/AIR 
1 FDR/data link/AIR 

## Section 2 Common Design Specification Chapter 2-1 General 2-1.1 Introduction

This chapter establishes the design considerations and general specifications for the equipment specific to flight recorder systems.  

## 2-1.2 Recorder Technology

The recorder shall use a digital method of recording. Magnetic tape, wire and photographic methods shall not be used. 

## 2-1.2.1 Physical Size

As technology allows for increased miniaturization, manufacturers continue to shrink the crash-protected memory module.  Now, the crash-protected memory module can be very difficult to find in wreckage.  The sum of the height (a), width (b), and depth (c) of the crash-protected memory module shall be 9 inches or greater.  Each of these major dimensions shall be 2 inches or greater.  Here are five examples of a crashprotected memory module and the minimum required dimensions: 
NOTE:   
The dimensions of the crash-protected memory module shall not include the underwater locator beacon (ULB) or its attachment hardware. 

Apply minimum dimensions to the major axis (a), minor axis (b), and length (c) of the crash-protected memory module. 

Height, width, and depth are all equal to the diameter of the sphere which shall be equal to or greater than 3.0 inches because of the, a + b + c >= 9 inches, requirement. 

Dimensions a, b, and c are not necessarily equal. 

Width (a) is the largest width of the crash-protected memory module, depth (b) is the largest depth of the crash-protected memory module and height (c) is the largest height of the crash-protected memory module.  Take each of these major dimensions from the outer surface of the crash-protected memory module.  Do not include any protrusions such as mounting flanges or plates. 

## 2-1.3 Airworthiness And Certification 2-1.3.1 Safety

The flight recorder equipment shall not, under normal or fault conditions, impair the airworthiness of the aircraft in which it is installed. Particular attention shall be directed to the needs of flight critical systems to ensure appropriate physical and electrical segregation of the information sources at the recording system interface. The flight recorder system shall perform its intended function under any foreseeable operating conditions. 

## 2-1.3.2 Maintenance

The maintenance tasks required to ensure the serviceability and continued airworthiness of the flight recorder systems shall be established by the equipment manufacturers and the equipment installers. The maintenance requirements for specific types of flight recorder are discussed in the relevant chapters of this document. 

## 2-1.3.3 Fire Protection

Except for small quantities of materials used for heat insulation or dissipation (such as ablative paints and thermo-chemical compounds) and small parts (such as knobs, fasteners, seals, grommets and small electrical parts) that would not contribute significantly to the propagation of a fire, all materials used shall be self-extinguishing. 

 

## 2-1.3.4 Documents For Certification

In addition to the documents required by the certifying authority (as specified in the applicable equipment certification procedures) the applicant shall provide the following information: 
1. 

Instructions which would enable an accident investigation authority to obtain or manufacture any special tools or interface equipment required for the retrieval of the recorded information, 

2. 
Details of the procedures to be followed for retrieval of the recorded information from an undamaged recorder, 
3. 
Details of the procedures to be followed for retrieval of the recorded information from any memory device used within the crash-protected memory module removed from a crash damaged recorder, 
4. 
Detailed information and/or tools necessary to permit data recovery from individual memory chips (or equivalent). 
5. 
Software documentation, including conversion and logic data for reproduction of 
the original information. 

NOTE: 
        The Certification Authority should involve the relevant accident authority 
        in the assessment of the above documents. The assessment should 
        confirm that suitable equipment and information will be readily available 
        to the accident investigation specialist to allow retrieval of the recorded 
        information in a timely manner. 

The information provided should enable the accident investigators to produce, 
within 24 hours of receipt of an undamaged recording medium, the material 
necessary to support their investigations. 

6. 
Conversion information and logic for translation of the recorded data into the original end user information and message status changes (selections, message entry, message deletion etc.). Further guidance can be found in ARINC Specification 647A FRED. 

## 2-1.4 Controls 2-1.4.1 Operation Of Controls

Controls available to the flight crew, when operated in all possible positions, combinations and sequences, shall not be detrimental to the continued performance of the flight recorder system. 

## 2-1.4.2 Monitoring Of Proper Operation

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
There shall be aural or visual means for pre-flight checking of the recorder(s) for proper recording of the information in the recording medium. The monitor(s) shall operate continuously throughout the flight. However, an indication to the crew of in-flight failure may be suppressed until the aircraft has completed its flight. 

NOTE: 
An acceptable means of compliance would be to provide system status monitor(s) and built-in test functions which would detect and indicate to the flight crew a failure of the flight recorder system due to any of the following: a. 

Loss of system electrical power, 

b. 
Failure of the acquisition and processing equipment, 
c. 
Failure of the recording medium, 
d. 
Failure of the recorder to store the information in the recording medium as shown by checks of the recorded material including, if reasonably practicable, correct correspondence with the inputs, 
e. 
The absence of the recorder and/or the acquisition equipment. 

## 2-1.5 Start And Termination Of Recording

The recorder shall start automatically to record prior to the aircraft moving under its own power and continue to record until the termination of the flight when the aircraft is no longer capable of moving under its own power. In addition, depending on the availability of electrical power, the recorder shall start to record as early as possible during the cockpit checks prior to engine start at the beginning of flight until the cockpit checks immediately following engine shutdown at the end of the flight. A means shall be provided to stop the recorder automatically as soon as possible at the completion of the flight but no later than ten minutes +/- 1 minute after all the engines have stopped operating when the aircraft is on the ground (see 2-5.3.11 for more guidance). 

NOTE 1: 
For helicopters certificated for extended flight over water, a device should be installed external to the recorder to interrupt the electrical supply to the recorder following a ditching. 

NOTE 2: 
For flight recorders with a RIPS installation, the means in the paragraph 
above includes the required alternate power duration (i.e., no cascading effect of two 10 minute intervals). 

## 2-1.6 Normal Operation

When electrical power is applied to the equipment and the start logic is satisfied, the recorder shall commence and continue to store information, in accordance with the requirements of this MOPS. 

## 2-1.7 Bit Error Rate

The bit error rate arising from differences between the input to the recorder and the retrieved data caused by corruption of the data during processing, recording and retrieval shall not exceed one error in 105 bits. In addition, where data compression is used, the word error rate shall not exceed one error in 105 words.  
NOTE: 
This is not applicable to an analogue audio signal that meets the audio quality performance requirements stated in Table I-3.1. 

## 2-1.8 Effects Of Tests

Unless otherwise permitted, the design of the equipment shall be such that, subsequent to the application of the specified performance tests, no condition exists which would be detrimental to the continued performance of the equipment. 

## 2-1.9 Software Management

Where equipment uses digital computer techniques the software practices shall follow the applicable guidelines specified in document EUROCAE ED-12B / RTCA DO-178B or the revision level as agreed with the certification authority. Software for recording functions shall be shown to comply with the guidelines applicable to at least Level D. 

## 2-1.10 Equipment Design Specifications

The design specifications for each recorder type are detailed in Parts I to IV. 

## 2-1.11 Recorder Synchronisation

The replay of a recording made by any required recorder shall be capable of being synchronised in time with any other required recording to within 1 second.  Refer to paragraph2-5.6.5. 
NOTE 1: 
As far as reasonably practicable, all airborne recordings should be related to a single time reference  
NOTE 2: 
Where the system architecture permits, it is recommended that the recordings are capable of being synchronised in time with any other required recording to within 0.25 seconds. 

## 2-1.12 Time Base Characteristics

A stable time base or reference signal shall be provided having an average accuracy of at least 0.1% obtained during information retrieval. 

The recorded time base shall be reproducible with an accuracy of 0.1%, averaged over a period of at least 1 minute. 

## 2-1.13 Means Of Damage Assessment For The Recording Medium

Where the recording medium cannot be readily and reliably inspected, means shall be provided to enable the accident investigator to determine, prior to an attempted replay, if the recording medium has been subjected to an excessive level of heat where the survival of the medium may be in doubt. 

## 2-1.14 Recorded Information And Recording Medium Organisation

The organisation of information in the recording medium shall minimise the loss in the event of memory device failure or damage. If a loss occurs during normal operation, the event should be indicated in the recorder BITE output. The memory devices should be reconfigured automatically, where this is practicable. 

## 2-1.15 Retention Of Recorded Information

Following the removal of electrical power to the recorder, the recording medium shall be capable of retaining the information recorded during the preceding operating time for a period of at least 2 years.  

## 2-1.16 Crash Survival 2-1.16.1 Information Retrieval

The recorder shall be constructed such that the information in the recording medium can be retrieved using specified techniques.  

## 2-1.16.2 Survival Criteria (Fixed Recorders)

a. 
The crash-protected recording medium of the recorder shall be capable of preserving the recorded information when subjected to the three following sequences of tests: i. 
Impact shock, shear and tensile test, penetration resistance, static crush, high temperature fire and fluid immersion, 
ii. 
Impact shock, shear and tensile test, penetration resistance, static crush, low temperature fire and fluid immersion, 
iii. 
Impact shock, shear and tensile test, penetration resistance, static crush, 
deep sea pressure and sea water immersion. 
b. 
A single recorder shall be used for all of the tests required by a given sequence. However, it is not required that a single recorder should survive all sequences of test. 
c. 
The need for repairs to the recording medium as a consequence of the crash survival tests shall be minimised. i. 
Post test sequence i. & iii, it shall be possible to recover the data from the recording medium with only simple repairs such as replacing the interconnection harness to the crash-protected memory module. Resoldering memory devices or ancillary components is not permitted. 
ii. 
Post test sequence ii. (Low temperature fire), removal of individual memory devices to allow information recovery either separately or in combination after re-attachment to the original or replacement crashprotected memory module is permitted. 
d. 
Test procedures are defined in CHAPTER 2-4.  

## 2-1.16.3 Identification

A high proportion of the area of the outer surfaces of the armour which provides the crash protection, and of the outer surfaces of the recorder, shall be coloured bright orange. The outer surfaces of the recorder shall be inscribed with black letters of at least 25 mm in height, the following instruction: 

## Flight Recorder Do Not Open

 Where it is considered impractical to incorporate lettering of this height due to the size of the recorder case, the applicant may propose an alternative height provided that the size is adequate in relation to the size of the unit. The inscription shall be legible after the recorder has been subjected to the tests, with the exception of the fire tests, specified in CHAPTER 2-4. In addition, reflective tape shall be attached to the external surfaces of the recorder to assist its recovery in poor visibility including sea water immersion conditions. 

NOTE: 
Where these methods are not appropriate alternative means should be agreed with the certification authority. 

## 2-1.16.4 Underwater Locator Beacon

For recorders which are fixed in the airframe, provision shall be made for the attachment of an underwater locator beacon. The method of attachment shall ensure that the risk of damage to the beacon and crash-protected memory module will be minimised and that the beacon will not become separated from the crash-protected part of the recorder when subjected to the shear and tensile test specified in CHAPTER 2-4. 

NOTE: 
The required characteristics of the underwater locator beacon are outside the scope of this MOPS. Reference should be made to the applicable equipment standard. Specifications for ULB are contained in SAE 8045A document. 


## Chapter 2-2 Minimum Performance Specification Under Standard Test Conditions

The requirements for minimum performance under standard test conditions are flight recorder specific and are detailed in the relevant function specific Parts. 


## Chapter 2-3 Minimum Performance Specification Under Environmental Test Conditions 2-3.1 Introduction

This chapter specifies environmental test conditions. The equipment shall be tested to demonstrate that it performs its intended function when operated under the environmental conditions to which it has been declared to comply. Additional tests may be required in respect of equipment using new or untried techniques; the extent of such tests shall be agreed between the certification authority and the equipment manufacturer. Further, tables in the function specific Parts detail those environmental tests during which compliance with specific paragraphs of those parts shall be shown. In respect of the various items of equipment of the system, the choice of test classes within each environmental category is left to the discretion of the equipment manufacturer. However, to limit the aircraft location constraints for the crash-protected recorder, it is strongly recommended that it is designed and tested to meet the most severe environmental conditions. For the purposes of these environmental tests, the term 'equipment' shall be interpreted to include the recording equipment together with its accessories such as shock or anti-vibration mounts. It does not include the underwater sonar location beacon or the radio location beacon, since these devices are the subject of other specifications. An analysis may be substituted for a test where its use can be shown to produce equivalent evidence of compliance. 

NOTE: 
Additional tests applicable to crash survival of the recording medium are stated in CHAPTER 2-4 (fixed recorders) and CHAPTER 3-3 (deployable recorders). 

## 2-3.2 Standard Environmental Tests

The equipment shall be tested as defined in EUROCAE ED-14G / RTCA DO-160G "Environmental Conditions and Test Procedures for Airborne Equipment", or the revision level as agreed with the certification authority. The applicable tests shall be as shown in Table 2-3.1, as appropriate for the equipment categories selected by the manufacturer. The term 'As required' means that this test is only necessary if it is required by the selected category. 

For exceptions to these general requirements, refer to Chapter 4 of each function specific Part. 

--```,,`,````,`,,,``,,``

ED-14G/ 
No 
Test 
DO-160G 
Remarks 
Section 
1. 
 
Temperature 
4.0 
 
2. 
 
Altitude 
4.0 
 
3. 
 
Temperature Variations 
5.0 
 
4. 
 
Humidity 
6.0 
 
5. 
 
Operational Shock 
7.0 
 
6. 
 
Crash Safety Shock 
7.0 
 
7. 
 
Vibration 
8.0 
 
8. 
 
Explosion Proofness 
9.0 
As required  
9. 
 
Waterproofness 
10.0 
As required  
10.  
Fluids Susceptibility 
11.0 
As required  
11.  
Sand and Dust 
12.0 
As required  
12.  
Fungus Resistance 
13.0 
As required  
13.  
Salt Spray 
14.0 
As required  
14.  
Magnetic Effect 
15.0 
 
15.  
Power Input 
16.0 
 
16.  
Voltage Spike 
17.0 
 
17.  
AF Conducted Susceptibility 
18.0 
 
18.  
Induced Signal Susceptibility 
19.0  
19.  
RF Susceptibility 
20.0 
 
20.  
RF Emission 
21.0 
 
21.  
Lightning Induced Transient Susceptibility 
22.0 
When selecting the test level category, consideration should be given to the likely use of the recorder in aircraft constructed, entirely or in part, of composite materials. 
22.  
Lightning Direct Effects 
23.0 
As required  
23.  
Icing 
24.0 
As required  
24.  
Electrostatic Discharge 
25.0 

## Chapter 2-4 Test Procedures For Crash Survival (Fixed Recorders) 2-4.1 General

This section specifies crash survival tests to be applied to the crash-protected recorder to demonstrate compliance with paragraph 2-1.16. a. 
Prior to commencement of any crash survival testing, record a known, random digital data test pattern and after the test sequences data shall be readily recoverable, within the maximum data error rate and/or intelligibility defined in the appropriate Function Specific Part. 
b. 
After the test sequences the recording should be replayed to establish that the initial test signal is recoverable. 
c. 
On completion of a crash survival test sequence, the recording medium may be cleaned and dried. Alterations or repairs between tests shall not be made except for the removal from, or the replacement of, the crash-protected memory module or other components within the main recorder assembly as permitted by the test. 
NOTE 1: 
Microscopic examination of the surface characteristics of memory devices is not acceptable as means of data recovery. 

NOTE 2: 
The repair of individual memory devices is not permitted. 

## 2-4.2 Test Procedures 2-4.2.1 Impact Shock

The integrity of the crash-protected recording medium contents is to be validated when subjected to the following impact shock test. a. 

Subject the crash-protected memory module and attached underwater locator beacon or equivalent dummy to an impact shock applied to the most damagevulnerable axis in the most damage vulnerable direction. The energy content of the impact shock shall be equal to or greater than that provided by a half-sine wave shock of 6.5 millisecond duration and a peak acceleration of 33 342 m/s² (3 400  g), as shown in Figure 2-4.1. The waveform shall be such that a peak acceleration of at least 3 400  g is achieved. The shock may be generated by subjecting the recorder to an increasing or decreasing velocity change. 

NOTE: 
The definitions of "most damage-vulnerable axis" and "most damage-vulnerable direction" should not be limited to the three primary axes of the recorder. 

b. 
One acceptable means of compliance is to generate a trapezoidal shock that has an energy content equivalent to that of a half-sine wave as specified in (a) above. 
c. 
It is permissible to perform the impact test on the crash-protected memory module of the recorder only. The tested module may then be installed in the recorder for the remaining sequence of tests. 
d. 
An underwater locator beacon or equivalent dummy shall be attached to the crash-protected memory module utilizing the underwater locator beacon mounting feature.  
 
 
--```,,`,````,`,

NOTE: 
Depending on the design of the recorder, up to two impact shocks may be required; 1) the most damage vulnerable axis of the armour, and 2) the face-on beacon impact. It is permissible to apply only one of these impacts for each test sequence of paragraph 2-1.16.2. For instance, for a particular recorder, sequence 1 (high temperature fire) may be performed 
on the recorder used during the test of the most damage vulnerable axis of the armour, sequence 2 (low temperature fire) may be performed on the recorder used during the test of the face-on beacon impact, and sequence 3 (deep sea immersion) may be performed on the recorder used during the test of the beacon detachment shear and tensile test. 

## 2-4.2.2 Shear And Tensile Test

As shown in Figure 2-4.2, the underwater locator beacon attachment shall be subjected to:  

1. 
a static shear test in each of the beacon lateral and longitudinal axes and,  
2. 
a tensile test in a direction orthogonal to the lateral and longitudinal axes.   
A separate test specimen may be used for each of the three tests i 
Subject the underwater locator beacon attachment feature to a static shear force of 26.689 kN (6 000 lb) applied in the longitudinal direction of the underwater locator beacon mounting feature. In the longitudinal static shear test, the armor shall be held firmly and a shear force applied nearest to the armor, in the longitudinal direction of the mounting feature of the ULB. The force shall be held steady at the target level for 1 minute. At the completion of the test, the beacon shall not become completely separated from the armor and the armor shall not rupture. 
ii 
Subject the underwater locator beacon attachment feature to a static shear force of 26.689 kN (6 000 lb) applied in the lateral direction of the underwater locator beacon mounting feature. In the lateral static shear test, the armor shall be held firmly and a shear force applied nearest to the armor, in the longitudinal direction of the mounting feature of the ULB. The force shall be held steady at the target level for 1 minute.  At the completion of the test, the beacon shall not become completely separated from the armor and the armor shall not rupture. 
iii 
Subject the underwater locator beacon attachment feature to a static tensile force of 26.689 kN (6 000 lb) applied in the direction orthogonal to the lateral and longitudinal axes of the underwater locator beacon mounting feature.  
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

 
In the static tensile test, the armor shall be held firmly and a tensile force applied to the ULB or substitute. The force shall be held steady at the target level for 1 minute.  At the completion of the test, the beacon shall not become completely separated from the armor and the armor shall not rupture. 

## 2-4.2.3 Penetration Resistance

a. 
Subject the recorder to a penetration force produced by a 227 kg (500 lb) weight which is dropped from a height of 3 m (10 ft) to strike the most damagevulnerable face of the recorder crash-protected memory module at the most critical point. The point of contact of the weight shall be a circular steel pin with a diameter of 6.35 mm ± 0.1 mm (0.25 in ±0.004 in). The hardness of the pin material shall be in the range of Rockwell C39 to C45. The longitudinal axis of the weight shall be vertical at the point of impact. The length of the exposed pin shall be 40 mm ± 1 mm (1.57 in ± 0.04 in). Electronic components, external to the crash-protected memory module, may be removed. A suitable test facility is shown in Figure 2-4.3. 
 
b. 
Support the recorder on a bed of sand, 0.5 m (20 in) deep such that it is subjected to the full force of the penetrating pin and not deflected out of its path. The sand shall comply with the specification of Table 2-4.1, or 'MIL-S-17526A 
Class 18', or sand conforming to product specification 'Redhill 65'. The sand 
may be moistened with water with an approximate volume mix ratio of 1 litre of water to each 15 litres of sand. The actual ratio of water to sand is not critical except that too little or too much water will allow the recorder to sink further into the sand and contact the concrete base thus increasing the severity of the test. The depth of sand below the recorder should be 0.5m (20 inches). Small recorders should be firmly mounted at the centre of a square, steel plate having an area of at least 0.06 sq. m (100 sq. in) and a thickness of 6.35 mm (¼ in). 
The purpose of the plate is to provide a standard resistance beneath the recorder and reduce the amount of deflection when the weight strikes. The plate need not be used for recorders with a cross sectional area greater than 0.06 sq. m. 
NOTE 1: 
'Redhill 65' is obtainable from Hepworths Minerals and Chemicals 
Ltd, Quarries Division, Trowers Way, Redhill, Surrey RH1 2LL, England. 
NOTE 2: 
Specification MIL-S-17526A is obtainable from Naval Publications and Forms Centre, 5801 Tabor Avenue, Philadelphia, PA 19120 USA. 
c. 
Assemble the penetrating mass from a weight into which a replaceable, steel, cylindrical pin is inserted. To avoid absorption of the penetrating force by contact of the weight with the sand, the cross-sectional dimension(s) of the weight shall be less than that of the recorder or the plate on which the recorder is mounted, whichever is the greater. The non-penetrating end of the pin should be plain and have the same diameter as the penetrating end. Any retention method is acceptable provided it does not weaken the pin in any way, e.g. a setscrew is acceptable whereas a threaded pin is not. The penetrating end of the pin should be cut straight across and deburred. FIGURE 2-4.4 illustrates a suitable method for the attachment of the pin. 
d. 
A means to raise the weight, such that the tip of the pin is at a height of 3 m 
(10 ft) above the recorder, shall be provided. The weight may be constrained by a suitable guide and safety cage. A rope fuse is an acceptable release mechanism. 
e. 
At the point of impact, the penetrating pin shall be perpendicular to the side of the recorder to be tested. Following impact, should the protective armouring be 
penetrated by the pin, it may be permissible to continue the test sequence provided it can be demonstrated that a longer pin would not have damaged the recording medium. Repairs to the armouring or insulation are not permitted and the pin shall be left embedded in the crash-protected module for subsequent tests. 
f. 
The penetration test may need to be performed on each side of a test specimen 
to determine the most damage-vulnerable point. The pin should be replaced after each test. A single test is then performed on the recorder which is being used for each sequence of certification tests defined in paragraph 2-1.16.2 as applicable. Electronic components external to the crash-protected memory module may be removed. Photographic evidence of satisfactory testing should be obtained for record purposes. 

## 2-4.2.4 Static Crush

a. 
Subject the crash-protected memory module to a static crush force of 22.25 kN (5 000 lb) applied continuously for a test period of five minutes. At least four points on the crash-protected module, irrespective of its shape, shall be tested 
including, where applicable, each of the main diagonals and each of the main faces. 
b. 
The minimum number of tests to be performed will depend on the shape of the crash-protected memory module. Where a spherical shaped module is used, at least four tests will be required. For a cuboid shaped module, a total of seven tests will be required e.g. 3 faces plus 4 diagonals. 
c. 
The static crush test may be performed using a hydraulic press and pressure gauge. 
d. 
It is permissible to remove from the recorder assembly those items which are not crash-protected except the underwater locator beacon and any other heavy duty items attached to the crash-protected module. 
e. 
The recorder may be supported in the press by means of circular resilient pads with a diameter of 5 cm (2 in) and a thickness of 1.25 cm (0.5 in). 
f. 
The crush force shall be adjusted following any initial collapse to restore the required pressure for the full 5 minute period. 

## 2-4.2.5 High Temperature Fire

a. 

Subject the crash-protected memory module or recorder to a fire producing a minimum thermal flux of 158 kW/m2 (50 000 Btu/ft2/hour). The entire external surface area of the crash-protected memory module or recorder shall be exposed to the fire for a continuous period of at least 60 minutes. The flame temperature should be 1 100 degrees C nominal. The turbulence and local flame cooling due to the crash-protected memory module or recorder under test may cause the temperature to vary between 950 degrees C and 1 100 degrees C. However, the minimum thermal flux stated herein shall be maintained for the duration of the test and monitored by suitable instrumentation. Shielding is not permitted. An acceptable method is to subject the crash-protected memory module or recorder to a fire test with flames generated by an arrangement of burners either gas or oil fired. A mix of air and propane gas is the preferred fuel since the mixture burns cleanly and is readily controllable. The mixture is adjusted to obtain a stable flame. If a complete recorder is used, it shall have the test article subjected to the test detailed above in the sequence described in paragraph 2-1.16.2. 

b. 

At the start of the fire tests precondition the recorder to a stable internal temperature equivalent to that reached after operation at ambient pressure and temperature of 25°C ±5°C. Electronic components external to the crashprotected memory module may be removed. 

NOTE: 
As per ED-14G / DO-160G section 2.1, the equipment is considered stabilised when the temperature of the largest internal mass of the equipment does not vary by more than two degrees Celsius per hour. When temperature measurement of the largest internal mass is not practical, the minimum time considered applicable for temperature stabilization is two hours. 

c. 
Where the effectiveness of the fire protection material decreases during normal operation and/or storage of the recorder, precondition the protective material to simulate the effects of ageing e.g. by means of extended pressure and temperature cycles. 
 
d. 
A water calorimeter shall be used to calibrate the burner array before the fire test is performed. The calorimeter shall be of the same overall dimensions as the test item (crash-protected memory module or recorder) to be tested. FIGURE 2-4.5 shows an example of a suitable water calorimeter. 
Where other burner calibration methods are used such as electronic radiometry, the method shall be validated against the calorimeter method. 
e. 
FIGURE 2-4.6 shows an example of a suitable test arrangement using propane gas burners. The calorimeter is supported on steel angle sections approximately 0.5 m (20 inches) above the ground. The water inlet and outlet pipes are passed through an insulating block wall. The purpose of the wall is to reflect heat onto the rear of the calorimeter (or recorder) and to prevent the water pipes from absorbing heat. The short section of pipes between the wall and the calorimeter should be well insulated. 
f. 
The number and capacity of burners, their positions and the gas pressure should be adjusted to ensure the required criteria of flame coverage, thermal flux and nominal flame temperature are met. It is important that the source of 
water for the calorimeter, and the source of fuel for the fire, can maintain the required flow rates for the full test period. The flame temperature should be monitored continuously by thermocouples placed approximately 25 mm (1 inch) from the surface of the crash-protected memory module or recorder at the approximate centre of a minimum of three faces. Burner output should be set by adjusting the individual burner gas valves. 
g. 
The thermal flux (Q) is given by: 
$$\begin{array}{r l r l}{\mathbf{Q}}&{{}={}}&{{\frac{\operatorname{d}\!\mathsf{T}\,\mathbf{x}\,\mathsf{F}\,\mathbf{x}\,\mathsf{S}\mathsf{H}}{\mathbf{A}\,\mathbf{x}\,\mathsf{C}}}}&{}&{{}}&{{\mathsf{W}/\mathsf{m}^{2}}}\end{array}$$
Where 
dT 
=temperature rise in cooling water (°C) 
 
F=flow rate of cooling water (kg/s) 
 
SH=specific heat of cooling water (4187 Joules/kg/°C) 
 
A=surface area of calorimeter (sq. metre) 
 
C 
=Absorption Constant. (A value of 0.5 shall be used) 
h. 
Once the required test conditions have been established, the gas pressure should be noted and the supply shut off at the main valve. The individual burner gas valves should not be touched. 
i. 
The crash-protected memory module or recorder to be tested should be substituted for the calorimeter. Where practicable, the internal temperature of 
the crash-protected memory module should be monitored in order to determine the margin of protection obtained for the particular recording medium. If construction is such that a significant portion of the crash-protected memory module or recorder has been damaged as a result of previous tests and is likely to melt or burn away during the test, the crash-protected memory module or recorder shall be supported in such a way that the crash-protected memory module will be subjected to the full thermal flux for the duration of the test. 
j. 
The fire test is started by turning on the main gas valve. If necessary, this valve should be used to control the gas pressure to the level noted in step h above. Flame temperature, as indicated by the external thermocouples, shall be continuously monitored. A higher temperature than that achieved during the calorimeter test may be observed due to the presence of the crash-protected memory module or recorder. The burner outputs shall not be altered to compensate for this difference. 
k. 
At the end of the test period, the burners should be shut off and the crashprotected memory module or recorder allowed to cool naturally in ambient conditions. It is permissible to remove the recorder from the vicinity of the support arrangement. 
 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## 2-4.2.6 Low Temperature Fire

a. 
Subject the recorder to a temperature of 260°C for 10 hours duration. 
b. 
At the start of the test precondition the recorder to a stable internal temperature equivalent to that reached after operation at ambient pressure and temperature 
of 25°C ±5°C. Refer to note at paragraph 2-4.2.5b. 
c. 
With the equipment non-operating install the recorder in a constant temperature oven, at ambient conditions (25°C ± 5°C). Raise the temperature of the oven at a rate not less than 2°C per minute, to a minimum temperature of 260°C. Maintain a minimum oven temperature of 260°C for at least 10 hours. 
d. 
At the conclusion of the 10 hours exposure period, the recorder may be removed from the oven and allowed to cool naturally. 

## 2-4.2.7 Deep Sea Pressure And Sea Water Immersion

a. 
Unless it can be shown that the recording medium can withstand the conditions associated with deep sea immersion and that it is unlikely to be damaged as a 
consequence of collapse of any protective armour, immerse the recorder in sea water at a pressure of 60 MPa (equivalent to a depth of 6 000 m (20 000 feet) for a period of 30 days. This period may be reduced to 24 hours provided that the methods and materials used to protect the recording medium have been shown to be unaffected by sea water. To avoid damage to the test equipment, this test may be performed using any suitable liquid in the pressure chamber itself together with a means to separate this liquid from the sea water in which the recorder is immersed. 
b. 
Unless it can be shown that the recording medium and the identification required by paragraph 2-1.16.3 are resistant to the corrosive effects of sea water, immerse the recorder in sea water at a depth of 3 m and nominal temperature of +25°C for a period of 30 days. It is permissible to perform this corrosion resistance test on a separate recorder independently of the main sequence of tests except where sea water has been forced into the crashprotected module during the deep sea pressure test. The weight of the recorder may be used as an indicator of this condition. 

## 2-4.2.8 Fluid Immersion

This test is intended to show that the recording medium, in a standalone, environment will not be damaged by immersion in fluids that may be encountered. It is not intended to show that cracked or damaged recording medium will not be damaged further by the fluids. This test may be run as the last test in the suite of tests described in paragraph 2-1.16.2 or as a separate independent test. 

NOTE: 
Typically the recording medium in a solid state recorder is memory chips contained in the crash-protected memory module.  

## 2-4.2.8.1 Test In Sequence

If the recording medium has not been tested for resistance to fluids in a separate test (refer to paragraph 2-4.2.8.2) then immerse the crash-protected memory module used in the tests described in paragraph 2-1.16.2 in the fluids as described in paragraph 2-4.2.8.3. 

## 2-4.2.8.2 Separate Test

The recording medium that is representative of the recording medium used in the crash-protected memory module may be tested in a separate independent test against the fluids in paragraph 2-4.2.8.3. The term "representative recording medium" means this medium shall be directly interchangeable with the medium used during the test (same part number) sequence described in paragraph 2-1.16.2, though it need not be the actual recording medium used in the other tests test sequence. If this separate test of the recording medium is made then the crash-protected memory module need not be tested for fluid immersion. Unless, during separate tests, the recording medium has been shown to be resistant to the fluid, immerse the crash-protected memory module in the fluids as follows: 

## 2-4.2.8.3 Fluids

Immerse the crash-protected memory module in fluids as follows: a. 
The types of fluids shown in Table 2-4.2, which are most likely to cause damage 
to the crash-protected memory module, for a period of at least 48 hours. 
b. 

The types of fire extinguishing agents, currently in use, which are most likely to cause damage to the  crash-protected memory module , for a period of at least 8 hours. 

NOTE: 
Extinguishing agents are described in the "Fire Protection Handbook" 
obtainable from the National Fire Protection Association (International), 60 Batterymarch St., Boston, Mass 02110, USA, or Infonorme London Information, Index House, Ascot, SL5 7EU, England. 

 

| % By Mass    | Particle Size (Micrometers)    |
|--------------|--------------------------------|
|              |                                |
| 1 Max        | Greater than 710               |
| 2 - 4        |                                |
| 10 - 14      |                                |
| 25 - 35      |                                |
| 25 - 35      |                                |
| 15 - 23      |                                |
| 500 - 710    |                                |
| 355 - 500    |                                |
| 250 - 355    |                                |
| 180 - 250    |                                |
| 125 - 180    |                                |
| 4 - 7        | 90 - 125                       |
| 2 Max        | Less Than 90                   |
| FLUID              | DESCRIPTION      | SPECIFICATIONS    |
|--------------------|------------------|-------------------|
| JOINT SERVICES     |                  |                   |
| DESIGNATION        |                  |                   |
| NATO CODE          |                  |                   |
| DERD 2453          |                  |                   |
| Turbine fuel       |                  |                   |
| MIL-T-83133A       | AVTUR/FS11       | F-34              |
| Kerosene Type      |                  |                   |
| (JP-8)             |                  |                   |
| DERD 2452          |                  |                   |
| Turbine Fuel High  |                  |                   |
| MIL-T-5624L        | AVCAT/FS11       | F-44              |
| Flash Type         |                  |                   |
| FUELS              |                  |                   |
| (JP-5)             |                  |                   |
| DERD 2485          |                  |                   |
| Gasoline, Aviation |                  |                   |
| Type 100/130       |                  |                   |
| MIL-G-5572F        |                  |                   |
| AVGAS 100LL        | F-18             |                   |
| Water Methanol     |                  |                   |
| 44%/56%            |                  |                   |
| DERD 2491          | AL-28            | S-1744            |
| Lubricating Oil    | Synthetic        |                   |
| DERD 2499          |                  |                   |
| MIL-L-23699C       |                  |                   |
| OX-27              | 0-156            |                   |
| DTD 585            |                  |                   |
| Mineral Base       | DEF STAN 91-48/1 |                   |
| OM-15              |                  |                   |
| OM-18              |                  |                   |
| H-515              |                  |                   |
| H-520              |                  |                   |
| MIL-H-5606E        |                  |                   |
| Hydraulic Fluids   |                  |                   |
| DTD 900/4881D      |                  |                   |
| Phosphate Ester    |                  |                   |
| Base               |                  |                   |
| (SKYDROL 500B)     |                  |                   |
| OX-20              | ---              |                   |
| Misc. Fluids       | Toilet Flushing  | Formaldehyde Base |

 
Tr = 3.5 ms maximum Td = 3.0 ms minimum Tf = 0 ms minimum A = 3 400 g (33 354 m/s²) minimum 

NOTE 1: 
         The intervals Tr and Tf shall be such that the area under the curve is 
         equal to or greater than that of a half-sine wave shock pulse i.e. Area = 
         (6.5 x 10-3) x 3400/(Pi/2) = 14.069 g-seconds 

NOTE 2: 
In practice, significant ringing of the shock pulse will be observed. Averaging may be applied to establish the effective pulse shape. 

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
 

NOTES: 
a. 
Top removed for clarity 
 
b. 
Material is 1.6 mm mild steel 
 
c. 
Dimensions in millimetres 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter 2-5 Equipment Installation And Installed Performance 2-5.1 Introduction

This chapter specifies installation characteristics and performance with procedures for verifying that performance when the equipment is installed in an aircraft. Installed performance criteria are generally the same as those contained in this section, which were verified through bench and environmental tests. However, certain performance parameters may be affected by the physical installation and can only be confirmed after installation. 

## 2-5.2 General

The Flight Recorder system shall be of a type approved by the relevant certifying authority, and the system so installed that, under normal conditions, it will be operating within the environmental conditions to which the items of equipment comprising the system have been declared to comply. Where the system is connected to mandatory instruments or data sources used for controlling or indicating the flight path of the aeroplane, adequate isolation between the instruments or data sources and the flight recorder system shall be, provided. Particular attention shall be given to ensuring that the segregation required between critical components or systems of the aircraft e.g. powerplant installation segregation, is not violated by the installation of the flight recorder. 

## 2-5.3 Equipment Installation 2-5.3.1 Accessibility

Controls and monitors needed for in-flight operation shall be readily accessible from the operator's normal seated position. Maintenance provisions for equipment adjustments shall not be readily accessible to the flight crew. 

## 2-5.3.2 Aircraft Environment

Equipment shall be compatible with the environmental conditions present in the specific location in the aircraft where the equipment is installed. 

Operation of the equipment shall not be affected by aircraft manoeuvring or changes in attitude encountered in normal flight operations. Operation of the equipment should not be affected by those extreme conditions likely to be encountered during an accident sequence e.g. stall buffet, violent and extreme manoeuvres. 

## 2-5.3.3 Failure Protection

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
Any probable failure of the flight recorder system shall not degrade the normal operation of any other equipment or systems connected to it. The failure of interfacing equipment or systems shall not degrade normal operation or cause a failure of the flight recorder system. 

## 2-5.3.4 Separation Of Mandatory Recorders

Where more than one type of flight recorder system is required, they shall be installed in such a way that a failure within one system does not impair the operation of any of the others. In addition, as far as practicable, each recorder and its associated wiring and accessories should be so installed that a single event is unlikely to result in the failure of more than one recorder. 

 

## 2-5.3.5 Interference Effects

The installed equipment shall not: a. 
be the source of harmful conducted or radiated interference, nor 
b. 
be adversely affected by conducted or radiated interference from other equipment or systems installed in the aircraft. 

NOTE: 
         Electromagnetic compatibility problems noted after installation of the 
         equipment may result from such factors as the design characteristics of 
         previously installed systems or equipment and the physical installation 
         itself. It is not intended that the equipment manufacturer design for all 
         installation environments. The installer will be responsible for resolving 
         any incompatibility between the equipment and previously installed 
         equipment. 

## 2-5.3.6 Stray Magnetic Field

When the cockpit equipment is placed, either in an operating or non-operating state in an area free from local magnetic disturbances, the stray magnetic field of this equipment shall cause not more than a 1 degree deflection of a magnetic compass when the closest edge of the equipment is at a distance of 300 mm from the compass. 

## 2-5.3.7 Insulation Resistance

The insulation resistance between any exposed conducting material of the equipment (non-electrical circuit) and the electrical circuit of this equipment shall be at least 10 Mohms when measured with an applied voltage of at least 50 volts DC. 

## 2-5.3.8 Inadvertent Turnoff

Protection shall be provided, or the installation shall be designed, to prevent the inadvertent turnoff of the equipment. 

## 2-5.3.9 Aircraft Electrical Power Source

Each recorder, whether containing single or multiple recording functions, shall be connected to a power source providing the most reliable electrical power and which has characteristics ensuring proper and reliable recording in the operational environment. When selecting the power source to be used, account should be taken of the requirements for start and termination of recording detailed in paragraph 2-1.5. For those aircraft with more than one reliable power source during normal operation: 

x 
where separate FDR and CVR recorders are provided, those recorders shall be powered from different electrical sources unless it is shown that any single 
electrical failure external to a recorder does not disable both CVR and FDR. 
x 
where the flight data recording function is duplicated in two separate recorders, those flight data recording functions shall be powered by different electrical sources unless it is shown that any single electrical failure external to a recorder does not disable both flight data recording functions. 
x 
where the cockpit audio recording function is duplicated in two separate recorders, those cockpit audio recording functions shall be powered by different electrical sources unless it is shown that any single electrical failure external to a recorder does not disable both cockpit audio recording functions. 
For helicopters, the recorder shall be designed to function normally with voltage and frequency fluctuations arising from main rotor speed variations within the operating limits. 

 

## 2-5.3.10 Alternate Power Source

An alternate power source shall automatically engage and provide a nominal 10 minutes +/- 1 minute of operation whenever aeroplane power to the recorder ceases, either by normal shutdown or by any other loss of power. The alternate power source 
shall power the CVR and its associated cockpit area microphone components. The alternate power source shall be located as close as practicable to the CVR.   
NOTE 1:  
"alternate" means separate from the power source that normally provides power to the CVR.  The use of aeroplane batteries or other power sources are acceptable provided that the requirements above are met 
and electrical power to essential and critical loads is not jeopardized.   
NOTE 2: 
When the CVR function is combined with other recording functions within the same unit, powering the other functions is allowed.  
The recorder independent power supply (RIPS) is a device (separate LRU or Integrated module) capable of providing an alternate power source. The intent of the RIPS is to allow for continued operation for 10 minutes (+/-1 minute) 
applied in all cases when power to the recorder is removed. The RIPS should be located as close to the unit to be powered as practicable, so as to minimise the possibility of the power supplied by the RIPS being interrupted during an accident. A RIPS may or may not be required as part of a system depending on the recording system type, recorder duration, and State's applicable operating rules SECTION 5 defines the RIPS. 

## 2-5.3.11 Recorder Operation

In order to ensure reliable operation, particularly under the abnormal conditions which might precede an accident, the means provided to automatically stop the recorder should rely on more than one device, e.g. engine oil pressure, weight-on-wheels sensor and airspeed sensors. 
NOTE: 
Use of the parking brake as the sole means for control of recorder operation is not recommended since this arrangement will cause interruptions of the recording during normal taxiing operations. 
If the stop and start conditions described in paragraph 2-1.5are such that the recorder could be inadvertently operating during aircraft maintenance, a means of inhibiting the recording shall be provided. 

## 2-5.3.12 Maintenance

An analysis shall be performed by the equipment installer to identify those aspects of the installation where the serviceability could be degraded and remain undetected. The maintenance tasks to be performed shall take account of this analysis by requiring appropriate functional and maintenance checks at suitable intervals. The maintenance tasks associated with each type of flight recorder are defined in the appropriate sections of the document. 

## 2-5.4 Equipment Location 2-5.4.1 Location Of Recorder

Each recorder shall be located and mounted so as to minimise the probability of container rupture resulting from crash impact, and subsequently damage to the record from fire. In meeting this requirement, the recorder shall be located as far aft in the aircraft as practicable. Due consideration should be given to the likely extremes of environment which might arise, including the possibility of damage from uncontained engine failures, sustained baggage fire, and the bursting of fuel tanks together with the needs for maintenance access. The location shall minimise the risk of destruction of the recording medium due to a sustained baggage fire. The probability of damage due to impact with baggage, cargo, aft engines, auxiliary power units and structural collapse shall also be minimised. 

An acceptable location in aeroplanes would be within the aft 15% of the pressurised fuselage and at least 600 mm (24 Inches) above the lower fuselage contour at the aeroplane centreline. In helicopters, a location in the upper section of the rear fuselage/forward tail boom area will normally be acceptable. 

Where duplicate recording systems are installed, the second system shall be installed as close to the cockpit as practicable. Where two or more dissimilar recorders are installed, the possibility of locating the recorders in separate areas should be considered so that the probability of the loss of more than one type of recording is minimised. Where an underwater locator beacon is required to be attached to the recorder, the location of the recorder should ensure that beacon transmissions are not attenuated to an unusable level by sound absorbent structure, e.g. honeycomb materials. If such a location is not possible, then in addition to the beacon on the recorder, a second beacon may need to be attached elsewhere to the aircraft. 

## 2-5.5 Installation Of Recorders 2-5.5.1 Installation Of Fixed Recorders

Adequate maintenance access shall be available. Except where the condition of the underwater locator beacon battery is monitored by the system, access to the battery, for maintenance checks, shall be available without removal of the beacon or the recorder. It should not be necessary for the recorder to be removed to allow access to other components in the same area. Protection may need to be provided to prevent contamination of the recorder by fluids present in the same area. Where practical, recorder equipment should be separated to reduce the risk of damage to more than one system from a common cause or event. 

## 2-5.5.2 Strength Of Installation

The structural provisions within the aircraft for the mounting of the recorder (including its anti-vibration mount where used) should be able to withstand the loads (to be treated as limit loads) resulting from severe vibration or buffet. In addition, the strength of the local attachments shall be able to withstand the crash safety loads prescribed for the aircraft or an ultimate load of at least 100 m/s2 (10  g) acting in any direction, whichever is the greater. 

## 2-5.5.3 Anti-Vibration Mounting

If the recorder is designed to be installed in an anti-vibration mounting, the equipment designer shall specify a suitable mounting which, when installed in the aircraft with the recorder, is able to withstand an ultimate load of at least 100 m/s2 (10 g) in any direction. 

## 2-5.6 Ground Test Procedures 2-5.6.1 Conformity Inspection

a. 
Visually inspect the installed equipment to determine the use of acceptable workmanship and engineering practices. 
b. 
Verify that proper mechanical and electrical connections have been made and that the equipment has been located and installed in accordance with the requirements and the manufacturer's recommendations. 

## 2-5.6.2 Reserved

Reserved 
 

## 2-5.6.3 Interference Effects

In order to demonstrate that 1) the flight recorder does not adversely affect other aircraft equipment and 2) the flight recorder is not adversely affected by other aircraft equipment, the following tests shall be performed. 
a. 
With the equipment energised, individually operate each of the other electrically operated aircraft equipment and systems to determine that no significant levels of conducted or radiated interference exist. 
b. 
Evaluate representative combinations of control settings and operating modes. 
c. 
Operate communications and navigation equipment on the low, high and at least one mid-band frequency. 
d. 
Identify systems or modes of operation that should be evaluated during flight. 
e. 
If appropriate, repeat the tests using emergency power with the aircraft's batteries alone and any standby inverters operating. 

## 2-5.6.4 Power Supply Fluctuations And Protection

a. 
Under normal aircraft conditions, cycle the aircraft engine(s) through all normal power settings and verify the proper operation of the equipment. 
b. 
Isolate the electrical supply to the recording system by means of the protective devices provided (e.g. circuit breakers) and verify that protection.  

## 2-5.6.5 Recorder Synchronisation

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

a. 
Unless compliance has been demonstrated at unit level testing, the aircraft test sequence shall demonstrate compliance with paragraph 2-1.11. 

## Section 3 Deployable Recorders

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter 3-1 General 3-1.1 Introduction

This section details the additional requirements and exceptions that are specific to deployable recorders. The requirements specified in this section shall be met in addition to the requirements of Sections 1 and 2, together with Sections 4 and 5 as applicable, and the appropriate recorder specific parts. A deployable recorder is a recording medium housed in a crash-protected memory module that is automatically deployed (released) from the aircraft at the start of an accident sequence. Its characteristics have the objective of enabling it to land at low speeds clear of the main aircraft wreckage, or, in the event of an over-water accident, its flotation characteristics enable it to float on water. Since the recorder is no longer with the aircraft it should be equipped with a means to locate it. 

This type of recorder is attached to the exterior of the airframe, and under normal conditions, functions in the same manner as a fixed recorder. The Recorder Memory Unit, Beacon Transmitters, Antennas, Battery Pack and the survival packaging for these units are all an integral part of the Automatic Deployable Package. The deployable Package incorporates flight characteristics that enable it to deploy and rapidly establish a flight trajectory that clears the airframe. 

## 3-1.2 Use Of Deployable Recorders

For fixed wing aircraft, it is strongly recommended that deployable recorders may only be used as part of a redundant installation where the recording function(s) provided by the deployable recorder is (are) also provided by a fixed recorder. If two flight recorders are installed on a rotary wing aircraft, it is strongly recommended that one of the recorders be a fixed recorder. If a combination of a deployable recorder and a fixed recorder is used to provide a redundant recorder installation, both recorders shall provide the same recording function(s).  

## 3-1.3 Purpose And Scope

This section defines the minimum specification to be met for Deployable Recorder Systems. It is applicable to any crash-protected recorder that is designed to be deployed, its ancillary equipment and its installation in civil aircraft. 

## 3-1.4 Application

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
Compliance with this section will ensure that deployable systems will perform their function under the conditions encountered in aircraft operations. 

 

## 3-1.5 Airworthiness And Certification 3-1.5.1 Safety

In addition to the safety requirements specified in paragraph 2-1.3.1, the following 
requirements shall apply to all deployable recorders: a. 
The exterior of the equipment shall have no sharp edges or projections that could damage inflatable survivable equipment or injure persons. 
b. 
The overall quantitative probability (per flight hour) of the failure event "noncommanded deployment" shall be <10-7. This probability objective addresses 
such hardware and software components, which contribute directly to the deployment event. 
NOTE:  
The procedures to determine this safety process shall be adapted 
from SAE ARP4761 "Guidelines and Methods for Conducting the 
Safety Assessment Process on Civil Airborne Systems And 
Equipment". 

NOTE: 
         A "non-commanded deployment" is defined as separation of the 
         deployable recorder from the aircraft when the deployment criteria 
         have not been met. 

## 3-1.5.2 Documents For Certification

In addition to the certification documents specified in paragraph 2-1.3.4, the following shall be provided. a. 
Instructions shall be provided for safely removing deployable recorders from the aircraft for maintenance purposes.  
b. 
The transmission frequency and modulation characteristics of the radio location beacon.  

## 3-1.6 Recorder Operation

In addition to the requirements defined in paragraph 2-1.5, the deployable recorder shall not continue to record once it has been deployed. 

## 3-1.6.1 Monitoring Of Deployable Recorder

A visual method to alert the cockpit crew when the deployable recorder is no longer captive to the aircraft shall be provided. The cockpit crew shall have an unobstructed view of the visual indicator when in the normal seated position. The brilliance of any indicator may be adjustable to levels suitable for data interpretation under all cockpit ambient light conditions ranging from total darkness to reflected sunlight. 


## 3-1.7 Deployment Criteria

a. 
The deployable recorder shall deploy upon aircraft impact with the ground or water so that the maximum amount of data is recorded up to the time of the 
crash. 
b. 
The deployable recorder should not deploy in  a non-catastrophic event such as 
a hard landing or tail strike. 
c. 
The deployable recorder may also deploy in a mid-air collision or explosion. 
d. 
Deployment criteria shall be defined by the aircraft manufacturer based on 
operational scenarios of the aircraft. 
e. 
The following factors shall be considered in establishing deployment criteria: 
i. 
Sensor installation (as defined in paragraph 3-4.3) including the number / type of sensors required to positively indicate a crash 
ii. 
Maximum "hard landing" accelerations (exceedance of which indicates a crash) 
f. 
The time from positive indication of a crash until the deployable recorder is released shall not exceed 50 milliseconds. 
g. 
In order to minimize potential safety hazards, the deployment mechanism may be locked while the aircraft is on the ground. There shall be no means for manual deployment. 
The design characteristics of a deployable recorder should result in the recorder landing clear of the aircraft wreckage. The unit shall incorporate flight characteristics that enable it to rapidly establish a flight trajectory that clears the airframe. The unit shall not be given sufficient initial momentum on deployment such that its release could endanger ground support personnel or the aircraft itself. 

## 3-1.7.1 Impact Initiation

Impact detection sensors such as frangible, deformation or micro-electro mechanical systems (MEMS), shall be installed on the aircraft in locations based on structural analysis and review of typical aircraft crash landing orientations and shall deploy the recorder when activated NOTE: 
Impact sensors should be designed such that they will only trigger when the structure has been significantly deformed (representing a catastrophic accident). Negative acceleration sensors ('g' switches) shall not be used as sole means of detection because their response is not considered to be reliable. 

## 3-1.7.2 Water Immersion Initiation

Sensor(s) shall be installed to activate deployment of the recorder at a depth of 3 m or more.  

## 3-1.8 Crash Survival 3-1.8.1 Survival Criteria (Deployable Recorders)

a. 
The crash-protected memory module of the recorder shall be capable of preserving the recorded information when subjected to the four following sequences of tests. The test procedures are defined in paragraph 3-3.2. i. 
Impact shock, penetration resistance, static crush and high temperature fire. 
ii. 
Impact shock, penetration resistance, static crush, low temperature fire and fluid immersion. 
iii. 
Impact shock, beacon transmission and seaworthiness.  
iv. 
Impact shock, penetration resistance, static crush, deep sea pressure and sea water immersion. 
b. 
A single recorder shall be used for all of the tests required by a given sequence. However, it is not required that a single recorder should survive all sequences of test. 
c. 
The need for repairs to the recording medium as a consequence of the crash 
survival tests shall be minimised. i. 
Post-test sequence i, iii and iv it shall be possible to recover the data from the crash-protected memory module with only simple repairs such as replacing the interconnection harness to the crash-protected memory module. Re-soldering memory devices or ancillary components is not permitted. 
ii. 
Post-test sequence ii (Low temperature fire) removal of individual memory devices to allow information recovery either separately or in combination after re-attachment to the original or replacement crashprotected memory module is permitted. 

## 3-1.8.2 Radio Location Beacon

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
All deployable recorders shall be equipped with a Class 1 dual frequency 406 MHz and 121.5 MHz radio location beacon compliant with the requirements of ED-62A instead of the underwater locator beacon and its attachment as specified in paragraph 2-1.16.4. The radio locating device shall be attached to the deployable recorder such that the aerodynamic properties of the recorder are not adversely affected and the risk of damage to, or separation of, the locating device is minimised. In addition to meeting the endurance requirements specified by ED-62A, the 121.5MHz radio shall operate for an additional 102 hours for a total minimum operational duration of 150 hours.  For the operational duration in exceedance of ED-62A (between 48 hours and 150 hours of operation), the minimum Equivalent Isotropic Radiated Power (EIRP) for the 121.5MHz radio shall be 5mW. 

NOTE: 
Other required characteristics of the radio location beacon are outside the scope of this MOPS. Reference should be made to the applicable equipment standard. 

## 3-1.8.3 Identification

The colours should support searching for the recorder on ground, and on water surface. Therefore, whenever possible, very dark colours should be avoided for the outer side of the airfoil (part of the aircraft external skin of the aircraft). The other external surfaces of the unit shall be bright orange.  
The search activities are primarily supported by determination of the position transmitted via the ELT signals. Therefore whatever paint will be applied, it shall not interfere with the transmission of the ELT signal The following instruction shall be inscribed with black letters of at least 25 mm in height on the orange coloured part of the deployable recorder: 

## Flight Recorder Do Not Open 3-1.8.4 Post-Test Identification Requirements

The identification inscription requirements of paragraph 2-1.16.3 shall be legible after the recorder has been subjected to the tests, with the exception of the fire tests, specified in CHAPTER 3-3. 


## Chapter 3-2 Minimum Performance Under Environmental Conditions 3-2.1 Introduction

CHAPTER 2-3 defines the environmental tests to be performed on the recorder system. Deployable recorders shall satisfy the functional requirements as detailed in Chapter 4 of the applicable function specific Part(s). 

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter 3-3 Test Procedures For Crash Survival (Deployable Recorders) 3-3.1 General

This chapter replaces the procedures for crash survival defined in CHAPTER 2-4. This section specifies crash survival tests to be applied to the crash-protected recorder to demonstrate compliance with paragraph 3-1.8. a. 
Prior to commencement of any crash survival testing a known, random digital data test pattern shall be recorded. This test pattern shall be readily recoverable, within the maximum data error rate and/or intelligibility defined in the appropriate Function Specific Part after the test sequences have been performed. 
b. 
After the test sequences the recording should be replayed to establish that the initial test pattern is recoverable. 
c. 
On completion of a crash survival test sequence, the recording medium may be cleaned and dried. Alterations or repairs between tests shall not be made except for the removal from, or the replacement of, the crash-protected memory module or other components within the main recorder assembly as permitted by the test.  
NOTE 1: 
Microscopic examination of the surface characteristics of memory devices is not acceptable as means of data recovery. 
NOTE 2: 
The repair of individual memory devices is not permitted. 

## 3-3.2 Test Procedures 3-3.2.1 Impact Shock

The integrity of the crash-protected recording medium contents and the proper operation of the Radio Location Beacon are to be validated when subjected to the following impact shock test. a. 

Subject the deployable recorder package, to an impact shock applied to the most probable landing attitude in the most damage vulnerable direction. The shock shall be such a level as to simulate a landing velocity of 46.33 m/s (152 ft/s) onto a hard surface such as rock, concrete or steel. 

NOTE: 
The definitions of "landing attitude" and "most damage-vulnerable direction" should not be limited to the three primary axes of the recorder. 

b. 
The deployable recorder containing the protected memory module shall impact or be impacted by a hard surface (50 mm thick steel plate of dimensions greater that the overall dimensions of the recorder) at a minimum impact velocity of 46.33 m/s (152 ft/s). Figure 3-3.1 illustrates an acceptable impact shock test setup for deployable recorders. Figure 3-3.2 illustrates an acceptable method and setup for retrieval of the deployable after impact. The mass of the impact plate shall be greater than 10 times the mass of the deployable recorder and experience no yield when subjected to the impact. 
c. 
Apart from the test sequence specified in paragraph 3-1.8 a iii, electronic components external to the crash-protected memory may be removed and replaced with representative mass models prior to commencing the impact shock test. For test sequence iii, the radio location beacon shall be installed and the test carried out on the complete recorder. 

## 3-3.2.2 Penetration Resistance

Place the deployable recorder on a smooth concrete surface, supported such that lateral deflection is prevented. a. 
An impactor, consisting of a penetrator with a rigidly attached mass of 25 kg 
(55 lbs) is dropped a distance of 15 cm (6 in) on to the deployable recorder.  
b. 
The penetrator shall have a maximum dimension across the surface of protrusion of 0.64 cm by 2.5 cm.  
c. 
The penetrator shall be of Rockwell C40 hardness, so that the shock of impact is absorbed by the deployable unit, not the penetrator. 
d. 
The impactor shall be dropped on to the deployable recorder such that at least half of the penetrator impacts within a 2.5 cm (1 in) radius of the most vulnerable area of the specified surface of the protected memory module. 
e. 
Figure 3-3.3 illustrates an acceptable penetration resistance test set up for deployable recorders. 
f. 
FIGURE 3-3.4 illustrates the penetrator. 
NOTE: 
This test methodology is the same as the penetration test specified for Emergency Locator Transmitters (ELTs) in ED-62A. 

## 3-3.2.3 Static Crush

a. 
Subject the crash-protected memory module to a static crush force of 8.9 kN (2 000 lb) applied continuously for a test period of five minutes. At least four points on the crash-protected module, irrespective of its shape, shall be tested including, where applicable, each of the main diagonals and each of the main faces. 
b. 
The minimum number of tests to be performed will depend on the shape of the crash-protected memory module. Where a spherical-shaped module is used, at least four tests will be required. For a cuboid-shaped module, a total of seven tests will be required e.g. 3 faces plus 4 diagonals. 
c. 
The static crush test may be performed using a hydraulic press and pressure gauge. 
d. 
It is permissible to remove from the recorder assembly those items which are not crash-protected except heavy duty items attached to the crash-protected module. 
e. 
The recorder may be supported in the press by means of circular resilient pads with a diameter of 5 cm (2 in) and a thickness of 1.25 cm (0.5 in). 
f. 
The crush force shall be adjusted following any initial collapse to restore the required pressure for the full 5 minute period.  

## 3-3.2.4 High Temperature Fire

a. 

Subject the crash-protected memory module or recorder to a fire producing a minimum thermal flux of 158 kW/m2 (50 000 Btu/ft2/hour). The entire external surface area of the crash-protected memory module or recorder shall be exposed to the fire for a continuous period of at least 20 minutes. The flame temperature should be 1 100 degrees C nominal. The turbulence and local flame cooling due to the crash-protected memory module or recorder under test may cause the temperature to vary between 950 degrees C and 1 100 degrees C. However, the minimum thermal flux stated herein shall be maintained for the duration of the test and monitored by suitable instrumentation. Shielding is not permitted. An acceptable method is to subject the crash-protected memory module or recorder to a fire test with flames generated by an arrangement of burners either gas or oil fired. A mix of air and propane gas is the preferred fuel since the mixture burns cleanly and is readily controllable. The mixture is adjusted to obtain a stable flame. If a complete recorder is used, it shall have the test article subjected to the test detailed above in the sequence described in paragraph 3-1.8.1. 

b. 

At the start of the fire tests precondition the recorder to a stable internal temperature equivalent to that reached after operation at ambient pressure and temperature of +25°C ±5°C. Electronic components external to the crashprotected memory module may be removed. 

NOTE: 
As per ED-14G / DO-160G section 2.1, the equipment is considered stabilised when the temperature of the largest internal mass of the equipment does not vary by more than two degrees Celsius per hour. When temperature measurement of the largest internal mass is not practical, the minimum time considered applicable for temperature stabilization is two hours. 

c. 
Where the effectiveness of the fire protection material decreases during normal operation and/or storage of the recorder, precondition the protective material to simulate the effects of ageing e.g. by means of extended pressure and temperature cycles. 
d. 
A water calorimeter shall be used to calibrate the burner array before the fire test is performed. The calorimeter shall be of the same overall dimensions as 
the test item (crash-protected memory module or recorder) to be tested. FIGURE 2-4.5 shows an example of a suitable water calorimeter. Where other burner calibration methods are used such as electronic radiometry, the method shall be validated against the calorimeter method. 
e. 
FIGURE 2-4.6 shows an example of a suitable test arrangement using propane gas burners. The calorimeter is supported on steel angle sections approximately 0.5 m (20 inches) above the ground. The water inlet and outlet pipes are passed through an insulating block wall. The purpose of the wall is to reflect heat onto the rear of the calorimeter (or recorder) and to prevent the water pipes from absorbing heat. The short section of pipes between the wall and the calorimeter should be well insulated. 
f. 
The number and capacity of burners, their positions and the gas pressure should be adjusted to ensure the required criteria of flame coverage, thermal flux and nominal flame temperature are met. It is important that the source of water for the calorimeter, and the source of fuel for the fire, can maintain the required flow rates for the full test period. The flame temperature should be monitored continuously by thermocouples placed approximately 25 mm (1 inch) from the surface of the crash-protected memory module or recorder at the approximate centre of a minimum of three faces. Burner output should be set by adjusting the individual burner gas valves. 
g. 
The thermal flux (Q) is given by: 
$$\begin{array}{r l r l}{\mathbf{Q}}&{{}={}}&{{\frac{\operatorname{d}\!\mathsf{T}\,\mathbf{x}\,\mathsf{F}\,\mathbf{x}\,\mathsf{S}\mathsf{H}}{\mathbf{A}\,\mathbf{x}\,\mathsf{C}}}}&{}&{{}}&{\mathsf{W/m}^{2}}\end{array}$$
Where dT 
=temperature rise in cooling water (°C) 

 
F=flow rate of cooling water (kg/s) 
 
SH=specific heat of cooling water (4187 Joules/kg/°C) 
 
A=surface area of calorimeter (sq. metre) 
 
C  
=Absorption Constant. (A value of 0.5 shall be used) 
h. 
Once the required test conditions have been established, the gas pressure should be noted and the supply shut off at the main valve. The individual burner gas valves should not be touched. 
i. 
The crash-protected memory module or recorder to be tested should be substituted for the calorimeter. Where practicable, the internal temperature of the crash-protected memory module should be monitored in order to determine the margin of protection obtained for the particular recording medium. If construction is such that a significant portion of the crash-protected memory module or recorder has been damaged as a result of previous tests and is likely to melt or burn away during the test, the crash-protected memory module or recorder shall be supported in such a way that the crash-protected memory module will be subjected to the full thermal flux for the duration of the test. 
j. 
The fire test is started by turning on the main gas valve. If necessary, this valve should be used to control the gas pressure to the level noted in step h above. Flame temperature, as indicated by the external thermocouples, shall be continuously monitored. A higher temperature than that achieved during the 
calorimeter test may be observed due to the presence of the crash-protected memory module or recorder. The burner outputs shall not be altered to compensate for this difference. 
k. 
At the end of the test period, the burners should be shut off and the crashprotected memory module or recorder allowed to cool naturally in ambient conditions. It is permissible to remove the recorder from the vicinity of the support arrangement. 

## 3-3.2.5 Low Temperature Fire

a. 
Subject the deployable recorder to a temperature of 260°C for 10 hours duration. 
b. 
At the start of the test precondition the recorder to a stable internal temperature 
equivalent to that reached after operation at ambient pressure and temperature of +25°C ±5°C. Refer to note at paragraph 2-4.2.5 b. 
c. 
With the equipment non-operating install the recorder in a constant temperature oven at ambient conditions (25°C ± 5°C). Raise the temperature of the oven at a rate not less than 2°C per minute, to a minimum temperature of 260°C. Maintain a minimum oven temperature of 260°C for at least 10 hours. 
d. 
At the conclusion of the 10 hours exposure period, the recorder may be removed from the oven and allowed to cool naturally. 

## 3-3.2.6 Fluid Immersion

Immerse the crash-protected memory module in fluids as follows: a. 
A selection of the fluids shown in Table 2-4.2, as agreed with the Certification Authority, for a period of at least 48 hours.  
b. 

The types of fire extinguishing agents, currently in use, as agreed with the Certification Authority, for a period of at least 8 hours.  
NOTE: 
Extinguishing agents are described in the "Fire Protection Handbook" 
obtainable from the National Fire Protection Association (International), 60 Batterymarch St., Boston, Mass 02110, USA, or Infonorme London Information, Index House, Ascot, SL5 7EU, England. 

## 3-3.2.7 Beacon Transmission

Place the deployable recorder in a shielded bag and confirm that the beacon transmits on 406 MHz with the required output for at least 24 hours; and that the beacon transmits on 121.5MHz with required power output for at least 150 hours. 

## 3-3.2.8 Seaworthiness

The deployable recorder shall be buoyant and, when floating in fresh water or salt water, shall be self-righting and sufficiently stable to maintain the antenna substantially in its normal operating position and to transmit on its 406 MHz and 121.5 MHz frequencies. Transmission of the ELT frequencies shall be demonstrated by testing in fresh and then salt water and confirming the reception of the 406 MHz Alert frequency via COSPAS SARSAT Satellite, and the 121.5 MHz homing frequency via a SAR Homing receiver.  This test shall be performed in water conditions representative of an open sea state 7 (equivalent to Beaufort Scale force 10). 

 

## 3-3.2.9 Deep Sea Pressure And Sea Water Immersion

a. 
Unless it can be shown that the recording medium can withstand the conditions associated with deep sea immersion and that it is unlikely to be damaged as a consequence of collapse of any protective armour, immerse the recorder in sea 
water at a pressure of 60 MPa (equivalent to a depth of 6 000 m (20 000 feet) for a period of 30 days. This period may be reduced to 24 hours provided that the methods and materials used to protect the recording medium have been shown to be unaffected by sea water. To avoid damage to the test equipment, this test may be performed using any suitable liquid in the pressure chamber itself together with a means to separate this liquid from the sea water in which the recorder is immersed. 
b. 
Unless it can be shown that the recording medium and the identification required by paragraph 2-1.16.3 are resistant to the corrosive effects of sea water, immerse the recorder in sea water at a depth of 3 m and nominal temperature of + 25°C for a period of 30 days. It is permissible to perform this corrosion resistance test on a separate recorder independently of the main 
sequence of tests except where sea water has been forced into the crashprotected module during the deep sea pressure test. The weight of the recorder may be used as an indicator of this condition. 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
 
C40 
hardness Dimension Tolerances - ±0.05 cm (±0.02 in) 

## Chapter 3-4 Equipment Installation And Installed Performance (Deployable Recorders) 3-4.1 Introduction

This chapter specifies installation characteristics and performance with procedures for verifying that performance when the equipment is installed in an aircraft. Installed performance criteria are generally the same as those contained in this section, which were verified through bench and environmental tests. However, certain performance parameters may be affected by the physical installation and can only be confirmed after installation. 

## 3-4.1.1 Aircraft Electrical Power Source

In addition to the requirements of paragraph 2-5.3.9, the electrical supply for the deployment mechanism shall be from a source which provides maximum integrity for system operation under crash conditions including sinking. An independent power source, located immediately adjacent to the deployment mechanism, shall be provided for activation of the mechanism 

## 3-4.2 Equipment Location 3-4.2.1 Location Of Recorder

In addition to the requirements of paragraph 2-5.4.1, each deployable recorder shall be located and mounted so as to minimise hazards resulting from intended or inadvertent deployment of the recorder. The deployment trajectory shall not create a hazard to the aircraft in any flight condition. The location of the deployable recorder on the airframe shall be established in conjunction with the aircraft manufacturer to ensure that the optimum deployment trajectory can be attained and that the deployed recorder clears the airframe. The location should provide optimum survival for the most likely crash cases, i.e. nose down or tail down directions. 

## 3-4.3 Installation Of Deployable Recorders 3-4.3.1 Aeroplane Installations

The following installation requirements shall be met when designing a deployable recorder installation for fixed wing aircraft: 
a. 
The deployable recorder shall be installed such that while it is still captive to the aircraft, the embedded ELT has sufficient visibility of the COSPAS-SARSAT satellite constellation in normal flight attitude. 
b. 
When the design of the airframe dictates that a pressurised structure is cut, the size of the opening shall be limited to the smallest practical size. 
c. 
The deployable package shall separate from the aircraft cleanly without striking any part of the airframe. Proper deployment shall be achieved for the whole flight envelope including a margin outside the normal flight envelope which might be expected during the initial stages of an accident sequence. Similarly, deployment from an aircraft in an unusual attitude should not make the survival of the recorder less likely. In selecting the location of the deployable package, consideration shall be given to antennas or other items protruding from the airframe. The airflow characteristics which may determine the flight path of the deployed recorder shall be analysed. 
d. 
Crash sensors shall be installed and located to detect the earliest indication of a crash in order to provide the highest assurance of survival for the deployable package. The positioning of the sensors should take the shape of the aircraft into account (ref paragraph 3-1.7.1). Negative acceleration sensors ('g' switches) shall not be used as sole means of detection because their response is not considered to be reliable. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

e. 
Crash sensors shall be protected to avoid inadvertent operation during ground activities. 
f. 
Hydrostatic or immersion sensors shall be installed to activate deployment of the recorder at a depth of 3 m or more. 

## 3-4.3.2 Helicopter Installations

The following installation requirements shall be met when designing a deployable recorder installation for helicopters: a. 
The selected location shall provide a recorder trajectory which is clear of the airframe and of the rotors when deployed at any point in the flight envelope. 
b. 
The location should provide optimum survival for the most likely crash cases, i.e. tail down, nose down. 
c. 
Consideration should be given also to avoiding locations near fuel cells. The design of the installation and deployment mechanism shall ensure that the recorder can deploy from a submerged airframe. To assist in the selection of 
this location, the installer should consider: - 
The type of helicopter, e.g. twin main rotor, ducted fan, conventional tail rotor. 
- 
Airflow round the airframe in different flight conditions. 
- 
Direction of rotation of main rotor. 
- 
Position (port or starboard) of tail rotor. 
d. 
It will not be acceptable to mount the recorder on control surfaces or in any areas likely to affect operating or flight characteristics. 
e. 
Crash sensors shall be installed and located so as to detect the earliest indication of a crash and to provide the highest assurance of recorder survival. To avoid false indications, crash sensors should not be located in areas of high vibration (ref paragraph 3-1.7.1). Negative acceleration sensors ('g' switches) shall not be used as sole means of detection because their response is not considered to be reliable. 
f. 
Crash sensors shall be protected to avoid inadvertent operation during ground activities. 
g. 
Hydrostatic deployment shall be demonstrated. 

## Section 4 Combined Recorders Chapter 4-1 Requirements For Combined Recorders 4-1.1 Combined Recorders

Two or more individual recording functions may be combined within a single unit. Each function shall satisfy the requirements of Parts I, II, III and IV of this document, as applicable. 

## 4.1.2 Functional Segregation

Where two or more types of flight recording functions are combined, the recorder shall be designed in such a way that a failure of one function does not impair the operation of any of the others. In addition, as far as practicable, each recorder and its associated wiring and accessories should be so installed that a single event is unlikely to result in the failure of more than one recording function. 

## 4-1.2.1 Recording Medium Segregation And Partitioning

When recording functions are combined in a single recorder, there is concern by investigators that all of the data pertaining to an accident or incident may be lost due to damage to a single memory device. To minimise this risk, the recording mechanism and medium shall be designed such that loss of data from multiple recording functions (e.g.: audio, parameters, etc) cannot result from the loss of a single memory device, with the exception that data link data may be combined with flight crew audio data.  
NOTE: 
Redundant recording or memory segregated as suggested by FIGURE 4-1.1 are acceptable means of compliance. 

## 4-1.2.2 Failure Reporting

When the recording functions are combined, an indication shall be provided to the flight crew of the particular function which has failed. Reporting of the failure via an onboard reporting system may be an acceptable means of determining which individual function of a combination recorder that has failed. The monitor(s) shall operate continuously throughout the flight. However, an indication to the flight crew of in-flight failure may be suppressed until the aircraft has completed its flight. 

NOTE: 
An acceptable means of compliance would be to provide system status monitor(s) and built-in-test functions that would detect and indicate to the flight crew a failure of each portion of the combined recorder. 

## 4-1.2.3 Single Power Supply

When the recording functions are combined in a single recorder, it shall be permissible for the functions to use a single power supply (both aircraft supply and recorder internal supply). 

## 4-1.3 Crosstalk In Combined Recorders 4-1.3.1 Cross-Talk Between Data And Audio Channels

When any digital data signal within the range for which the equipment is designed is applied to the required data recording channel, the level of any cross-talk signal recorded on that part of the recording medium assigned to each of the audio recording channels, shall be at least 34 dB below the levels obtained in paragraph I-3.2.2. 

 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## 4-1.3.2 Testing Of Cross-Talk Between Digital And Audio Channels

a. 

Equipment Required: Data link message transfer simulator  
Audio Signal Generator Audio Power Meter b. 

Measurement Procedure: With the audio input channels set to the signal level in paragraph I-5.2.2 connect the digital data transfer simulator to the data input of the recorder and record the signal for a period of one minute Replay the recording and measure the signal level on the audio channels. Determine the cross-talk level taking account of any imbalance measured in the test of Part I, paragraph I-5.2.2. It shall be verified that the crosstalk levels are within the limits defined in paragraph 4-1.3.1. 

## Section 5 Recorder Independent Power Supply

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter 5-1 Introduction 5-1.1 Purpose And Scope

This part defines the minimum specification to be met by a Recorder Independent Power Supply (RIPS) to support a flight recorder. 

## 5-1.1.1 General

The Section responds to a need to permit some types of flight recorder to continue operation for a period after the aircraft primary power supply has been removed. 

## 5-1.2 Functional Overview

The Recorder Independent Power Supply (RIPS) is an alternate power source that supplies direct current voltage to applicable aircraft recorder(s), for a specified duration whenever the primary aircraft power is removed from the recorder(s). The desired intent is to ensure continued recording following a loss of primary power associated with an aircraft emergency. Since it is impossible to distinguish between normal power shutdown and power removal as a result of an emergency situation, the RIPS will experience frequent operational cycles. In order to minimise the risk of overwriting useful information, a RIPS should not be fitted to a system which has a recording duration of less than two hours. 

## Chapter 5-2 General Design Specification 5-2.1 Introduction

This chapter establishes the minimum operation performance specifications for the equipment comprising the Recorder Independent Power Supply 

## 5-2.1.1 Equipment

a. 
The recorder independent power supply (RIPS) is a device (separate Line Replaceable Unit (LRU) or Integrated module) capable of providing backup power independently of aircraft power busses. 
b. 
The intent of the RIPS is to allow for continued operation for 10 minutes (±1 minute) applied in all cases when aircraft power to the recorder is removed. 
c. 
The RIPS should be located as close to the unit to be powered as practicable, 
so as to minimise the possibility of the power supplied by the RIPS being interrupted during an accident. 

## 5-2.2 Self-Monitoring Of Proper Operation

The RIPS shall be equipped with built-in test equipment (BITE) to determine the state of readiness of the RIPS to perform its function. The RIPS shall detect and report any internal failures, if maintenance is required, and of any conditions affecting the ability of the RIPS to perform its intended function. 

## Chapter 5-3 Minimum Performance Specifications Under Standard Test Conditions 5-3.1 Introduction

This chapter specifies the minimum performance specification of the equipment and the levels to be demonstrated under standard test conditions. For the purposes of this chapter, standard test conditions are defined in documents EUROCAE ED-14G / RTCA DO-160G "Environmental Conditions and Test Procedures for Airborne Equipment" or the revision level as agreed with the certification authority, paragraph 3.4 as: a. 

Temperature 
: +15 to +35°C 

b. 
Relative Humidity : Not greater than 85% 
c. 
Ambient Pressure : 84 to 107 kPa 
In addition to the above, the AC electrical power supply shall be within the limits specified as Normal in Section 16 of ED-14G/DO-160G or the revision level as agreed with the certification authority, the DC electrical power supply shall be within the limits specified as maximum and minimum in Section 16 of ED-14G / DO-160G or the revision level as agreed with the certification authority. The electrical power supply used shall be essentially free from modulation, ripple, interruptions and surges. In the case of equipment designed for operation from an AC power source of variable frequency, unless otherwise specified, tests should be performed at representative input power frequencies with the input frequency adjusted to within 5% of a selected frequency. 

## 5-3.2 Rips Minimum Performance Levels

The RIPS shall be designed to meet and shall be tested to show compliance with the following Minimum Performance Levels. 

NOTE:  
Where these paragraphs state requirements regarding the signal in the recording medium, it should be interpreted as that observed at the output of the data retrieval equipment specified by the equipment manufacturer.  

## 5-3.2.1 Backup Time Tolerance

The tolerance on the time of 10 minutes output shall be ±1 minute. 

## 5-3.2.2 Output Power Availability

The RIPS shall monitor the aircraft power supplied to the recorder. When aircraft power is lost to the recorder, the RIPS shall restore power in less than 50 milliseconds. 

NOTE: 
The RIPS designer may elect to make output power available continuously or only after aircraft power to the recorder has been lost. Either option is acceptable. 

## 5-3.2.3 Recharge Timing

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

a. 
From the time normal aircraft power is available until the unit is capable of providing the full 10 minutes of power shall be no more than 15 minutes. 
b. 
From the time normal aircraft power is available until the unit is capable of providing at least 6 minutes of power shall be no more than 10 minutes. 
c. 
The design of the RIPS shall make it possible to meet this requirement from any charge/discharge state or condition. For example, it shall be possible to replace the RIPS or its energy storage module from storage without any processing of the replacement unit prior to its installation in the aircraft. 

## 5-3.2.4 Output Control

There shall be no external means of inhibiting the output of the RIPS except a direct jumper located in the mating connector. A placard should be affixed to the RIPS notifying personnel that the output power pins may be active even when input power has been removed. 

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter 5-4 Minimum Performance Specifications Under Environmental Test Conditions

CHAPTER 2-3 of this document defines the environmental tests to be performed on the recorder system. Compliance with the applicable performance requirements of this part for RIPS shall be demonstrated as shown in TABLE 5-4.1. 

| 5-3.2.1Backup                                            | 5-3.2.2Output    | 5-3.2.3   | Environment   |
|----------------------------------------------------------|------------------|-----------|---------------|
|                                                          |                  |           |               |
| Test                                                     |                  |           |               |
| Reference                                                | Time Tolerance   | Power     | Recharge      |
| Table 2-3.1                                              | Availability     | Timing    |               |
| Temperature                                              | 1                | R         | R             |
| Altitude                                                 | 2                | R         | R             |
| Temp Variation                                           | 3                | R         |               |
| Humidity                                                 | 4                | R         |               |
| Shock                                                    | 5 and 6          | R         |               |
| Vibration                                                | 7                | R         |               |
| Power Input                                              | 15               | R         | R             |
| Voltage Spike                                            | 16               | R         | R             |
| 17                                                       | R                | R         | R             |
| Susceptibility                                           |                  |           |               |
| Induced Susceptibility                                   | 18               | R         |               |
| RF Susceptibility                                        | 19               | R         | R             |
| Lightning                                                | 21               | R         |               |
| Key: Blank = Manufacturers Discretion, R = Test Required |                  |           |               |
|                                                          |                  |           |               |

## Chapter 5-5 Test Procedures 5-5.1 Introduction

This chapter specifies the standard test procedures for demonstrating compliance with CHAPTER 5-3. Although specific test procedures are cited, it is recognised that they will not apply in all cases and that other methods may be preferred or required. Alternative methods may be used if the manufacturer can show that they provide equivalent certification data. Where a test procedure is not specified for a particular characteristic, the manufacturer may show compliance either by analysis or by devising a test appropriate to the equipment design. 

## 5-5.1.1 Adjustment Of Equipment

The equipment under test shall be properly aligned and adjusted in accordance with the manufacturer's recommendations. 

## 5-5.1.2 Test Instrument Precautions

Precautions shall be taken to prevent the introduction of errors resulting from impedance mismatch and the improper connection of test instruments to the equipment under test. 

5-5.1.3 
Test Conditions 
All tests shall be performed under the conditions defined in paragraph 5-3.1. 

## 5-5.1.4 Connected Loads

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
Unless otherwise specified, all tests shall be performed with the equipment connected to loads having the impedance values for which it is designated. 

## 5-5.1.5 Recording Of Test Results

Except where tests are GO/NO GO in character, the actual numerical values obtained for each of the parameters tested shall be recorded in a qualification test report. 

## 5-5.2 Electrical Test Procedures 5-5.2.1 Backup Time Tolerance (Paragraph 5-3.2.1)

a. 
Operate the RIPS for at least 15 minutes with the simulated aircraft power set to 
the specified low voltage limit.  
b. 
Switch off the simulated aircraft power. Verify that the RIPS power output voltage is as specified by the manufacturer, and remains present for the time defined in paragraph 5-3.2.1. 

## 5-5.2.2 Output Power Availability (Paragraph 5-3.2.2)

a. 
Operate the RIPS with the simulated aircraft power set to the nominal voltage.  
b. 
Switch off the simulated aircraft power. Verify that the RIPS power output voltage reaches the nominal voltage as specified by the manufacturer, within the time defined in paragraph 5-3.2.2.  
NOTE: 
This test may be omitted if the RIPS is a type that provides the output voltage continuously. 


## 5-5.2.3 Recharge Timing (Paragraph 5-3.2.3)

a. 
Make sure that the RIPS is completely discharged. 
b. 
Operate the RIPS with the simulated aircraft power set to the specified low voltage limit for the recharge period defined in paragraph 5-3.2.3a. 
c. 
Switch off the simulated aircraft power. Verify that the RIPS power output voltage is as specified by the manufacturer, and remains present for the time defined in paragraph 5-3.2.3a. 
d. 
Completely discharge the RIPS. 
e. 
Operate the RIPS with the simulated aircraft power set to the specified low voltage limit for the recharge period defined in paragraph 5-3.2.3b. 
f. 
Switch off the simulated aircraft power. Verify that the RIPS power output voltage is as specified by the manufacturer, and remains present for the time defined in paragraph 5-3.2.3b. 

## Chapter 5-6 Equipment Installation And Installed Performance 5-6.1 Introduction

This chapter specifies the aircraft installation. 

## 5-6.2 Equipment Installation

a. 

The RIPS and the recorder to be powered should be located as close as practical so as to minimize the length of the interwiring. 

NOTE: 
The state of the energy storage device technology may require the RIPS to be installed in a pressure and temperature controlled environment. In some installations this may make co-locating the RIPS with the recorder impractical causing the interwiring to be routed through a pressure bulkhead. 

b. 
The RIPS and the recorder should be designed such that no damage to equipment or aircraft or harm to personnel will result from installing or removing the recorder while power is applied (hot-plugging). 
c. 
The RIPS shall satisfy the requirements of paragraphs 2-5.3.2, 2-5.3.3, 2-5.3.5, 2-5.3.6, 2-5.3.8, 2-5.3.9 and 2-5.3.12. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## 5-6.3 Ground Test Procedure

a. 
Apply aircraft power for at least 15 minutes 
b. 
Verify that the recorder is operating 
c. 
Remove aircraft power from the RIPS/recorder (Pull circuit breaker) 
d. 
Verify that the recorder(s) continue to operate for 10 ±1 minutes. 
e. 
Apply aircraft power. 
f. 
Verify that the recorder(s) continues normal operation through aircraft switching transients such as Ground to APU, APU to engine, Ground to engine, engine to APU, APU to ground and engine to Ground. 

## 5-6.4 Flight Test Procedures

There are no flight test procedures associated with the RIPS. 

## Part I Cockpit Voice Recorder System

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter I-1 Introduction I-1.1 Purpose And Scope

This part defines the minimum specification to be met for all aircraft required to carry a Cockpit Voice Recorder system for the purposes of the investigation of a reportable accident or incident. It is applicable to crash-protected audio recorders, ancillary equipment and their installation in civil aircraft. This part shall be read in conjunction with Sections 1 and 2, together with Sections 3, 4 and 5 as applicable. 

## I-1.1.1 Description Of Content

This part is divided into six Chapters and four Annexes. CHAPTER I-1 describes typical equipment applications and operational objectives. 

Background material and accident investigation considerations are included together with a description of the CVR system. CHAPTER I-2 defines the general design specification. CHAPTER I-3 defines the minimum system performance under standard test conditions. CHAPTER I-4 defines the minimum system performance under environmental test conditions. CHAPTER I-5 specifies tests and procedures for determining compliance with the performance requirements and for demonstrating crash survival capability. CHAPTER I-6 defines the installed equipment performance requirements including ground tests and flight tests. The Annexes give additional guidance on replay, signal processing, maintenance practices and the determination of speech transmission index. 

## I-1.2 Application I-1.2.1 Audio Recording

Compliance with this Part will ensure that CVR systems will perform their function under the conditions encountered in aircraft operations. 

## I-1.2.2 Helicopter Rotor Speed Recording

Compliance with the relevant sections of this Part will ensure that ICAO Standards and Recommended Practices applicable to the recording of helicopter rotor rotational speed will be satisfied. 

## I-1.3 Description Of The System I-1.3.1 Equipment

The CVR system may include the following equipment as appropriate to the aircraft: a. 

Cockpit equipment, including controls for test and bulk erase functions, a monitor and failure indication, one or more area microphones and associated preamplifiers, NOTE: 
A control for the test function may be omitted where an automatic test is provided within the system. 

b. 
A crash-protected recorder in which the recording can be synchronised with the other airborne recordings, 
c. 
A means of converting the analogue audio signals to a digital format 
d. 
Audio interface equipment, including microphone/telephone signal summing amplifiers, 
e. 
For a Class 1 CVR, an alternate power source, capable of providing power to the crash-protected recorder and the area microphone(s), as defined in SECTION 5. 
f. 
An interface device suitable for converting a signal representing helicopter main 
rotor rotational speed into a format which can be recorded, 
g. 
A means of converting a synchronization signal to a format which can be recorded. 
h. 
Digital data busses and/or networks providing communications between elements of the system 

## I-1.3.2 Classes Of Voice Recorder

CVRs can be classified in terms of recording duration, number of channels and whether separate from, or combined with, an FDR. It is not within the scope of this document to specify which class of recorder is required to be installed in a particular category of aircraft. Reference needs to be made to the applicable operating regulations. 

For the purpose of this MOPS, six classes of recorder are defined as follows: a. 

EUROCAE Class 1 CVR: A recorder which meets the relevant parts of this MOPS and which is capable of retaining the information recorded during the last 2 hours of its operation. 

b. 
EUROCAE Class 2 CVR: A recorder which meets the relevant parts of this MOPS and which is capable of retaining information recorded during the last 60 minutes of its operation. 
c. 
EUROCAE Class 3 CVR: A recorder which meets the relevant parts of this MOPS and which is capable of retaining information recorded during the last 30 minutes of its operation. 
d. 
EUROCAE Class 4 CVR: A recorder which meets the relevant parts of this MOPS and which is capable of retaining the information recorded during the last 10 hours of its operation. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

e. 
EUROCAE Class 5 CVR: A recorder which meets the relevant parts of this MOPS and which is capable of retaining the information recorded during the last 15 hours of its operation. 
f. 
EUROCAE Class 6 CVR: A recorder which meets the relevant parts of this MOPS and which is capable of retaining the information recorded during the last 25 hours of its operation. 

## I-1.3.3 Operational Considerations

a. 
Objectives Each CVR should be installed so as to provide with reference to a timescale, simultaneous recordings of: i. 
voice communications transmitted from or received in the cockpit by radio, 
ii. 
the aural environment of the cockpit  
iii. 
the audio signals received from each boom and mask microphone in use, without interruption, 
iv. 
voice communications of flight crew members in the cockpit using the aircraft interphone system, 
v. 
voice or audio signals identifying navigation or approach aids, or related to warnings and alerts,  introduced into a headset or speaker, 
vi. 
voice communications of flight crew members in the cockpit using the public address system, if installed, and 
vii. 
for a helicopter not required to be equipped with a flight data recorder, the parameters necessary to determine the rotational speed of the main rotor. 
NOTE 1: 
For helicopters with two or more main rotors, the speed of each rotor should be recorded unless they are incapable of independent rotation. 
NOTE 2: 
Where, in a two flight crew aircraft, additional stations are provided for operating crew, these stations should be included for the 
purposes of this paragraph and may be summed on the third flight crew channel. 
NOTE 3: 
The timescale should be obtained from the source which sends the time signal to the FDR such that both the CVR and the FDR record the same time signal. Where a time signal is not required by the FDR, equivalent means of correlating the FDR and CVR should be provided such that both the CVR and the FDR recordings can be related to the same time base 
b. 
Start and Termination of Recording Recorder operation shall be as defined in paragraph 2-1.5. 
 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter I-2 Cvr Specifications I-2.1 Equipment Design Specifications I-2.1.1 General

This chapter is applicable to the functions of a flight recorder system designed to receive, process, record and preserve audio information in accordance with the requirements of this MOPS. These functions shall be performed reliably even under adverse operating conditions including events leading to an accident. To meet the requirements of different aircraft technologies, the recording system shall be capable of accepting and processing information of the following types: a. 

audio information, 

b. 
helicopter rotor rotational speed in either analogue or digital format (if required), 
c. 
time signals for synchronising the CVR with other flight recording functions, 
This section shall be read in conjunction with Section 2, which defines the requirements that are generic to all flight recorders. 

## I-2.1.2 Recording Techniques

The recorder shall use a digital method of recording and storing the data. 

## I-2.1.3 Digital Recording And Retrieval Characteristics

The recorded information shall be readily retrievable from the recording medium to an industry standard digital format without loss of audio quality, or timing correlation irrespective of the recording format. The recording shall be continuous regardless of input signal level; silence editing shall not be used. The organisation of the recording medium and the recording shall be such that: a. 

for undamaged, fully serviceable recording medium with a normal recording, the recorded information is readily available 

b. 
for damaged or partially failed recording medium, the available information can be retrieved using special techniques, as required. 
c. 
The organization of the recording medium shall contain provisions to detect corruptions in the recording or retrieval, or data losses due to medium management. These provisions could include time stamps, sequence numbers, and block checksums. 

## I-2.1.4 Recorder Synchronisation

The recordings on the CVR shall be synchronised to other airborne recordings as defined in paragraph 2-1.11. 

## I-2.1.5 Recording Capacity And Format

The equipment shall be capable of recording and storing the required information for the period applicable to the class of recorder. The recording of information as separate channels shall be maintained for the entire duration of the recording. 

## I-2.1.6 Means For Replay Of Recorded Information

The means for replaying the recording shall: a. 
require the removal of the recorder from its location in the aircraft, 
b. 
minimise the possibility of unauthorised replay of the recording and 
c. 
not erase, rewrite or alter the recording during replay. 

## I-2.1.7 Bulk Erase

After use of a bulk erase function, the recording shall be modified so that it cannot be retrieved using any and all normal replay or copying techniques. 

An acceptable means of compliance would be for a bulk erase function to delete that information needed to access the recording medium by the normal replay procedure. The probability of inadvertent activation of a bulk erase function shall be minimised both in design of the recorder and by ensuring that the bulk erase function, when installed, is wired so that it requires at least two other sets of logic to be satisfied. Wherever practicable, the parking brake should be one of the sets of logic. In addition, the probability of an inadvertent activation of a bulk erase function during an accident shall also be minimised 

NOTE 1: 
In the event of bulk erasure, non-normal replay or copying techniques may be used by the accident investigation authority to retrieve data, if available, for the purposes of conducting an official investigation. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

NOTE 2: 
Normal replay is data retrieval at the equipment level as used in the laboratories of aircraft constructors and modifiers to support certification of recorder installations. 
NOTE 3: 
Non-normal replay is data retrieval from the recording medium media using special techniques available to the recorder manufacturers and/or accident investigation authorities for dealing with severely damaged recorders. 
NOTE 4: 
It is understood that military organisations may use commercial recorders. In this case, they may have additional security requirements that exempt the recorder from this requirement. Arrangements should be made with the certifying authorities in regard to such exemptions 

## I-2.1.8 Recording And Recording Medium Characteristics

a. 

Recording Delay: Audio Signals The delay in recording the audio signals from the time of reception at the cockpit area microphone to the time of recording on the protected recording medium shall not exceed 50 milliseconds. The delay in recording the flight crew audio signals from the time of reception at the recorder input to the time of recording on the protected recording medium shall not exceed 200 milliseconds. 

b. 

Channel Synchronisation: Audio Signals The recordings for separate channels shall be made such that, when replayed, the relative time between channels can be deduced to better than 4 milliseconds irrespective of recording delay. 

c. 

Memory Segregation The recording mechanism and medium shall be designed such that complete loss of data from both the CAM and the flight crew audio recording channels cannot result from the loss of a single memory device.  
NOTE: 
Redundant recording or memory segregated as suggested by Figure I-2.1 are acceptable means of compliance 

## I-2.1.9 Audio Recording Channels

As a minimum, the recorder shall be capable of accepting audio signals simultaneously on separate channels as follows: 

 
Captain's audio panel; 
 
First Officer's audio panel; 
 
Additional flight crew positions; 
 
Cockpit Area Microphone. 

(Refer to Figure I-2.1). 
NOTE: 
             The number of channels required will depend on the operational 
             requirement for the aircraft in which the recorder is intended to be 
             installed. At least the Captain's audio panel and Cockpit Area Microphone 
             channels will be required. 

## I-2.1.10 Area Microphone Polarity

The area microphone terminals shall be identified indicating which terminal produces a positive-going electrical signal when there is a positive-going pressure wave at the diaphragm. 

## I-2.1.11 Reserved I-2.1.12 Digital Systems Characteristics

In digital systems, overdrive conditions can result in severe distortion if not properly handled. It is desirable to have the digital system handle an overdrive condition in the same way as an analogue system does. The design of a digital system's input stage should limit the maximum and minimum values of the digital word used to represent the input. This ensures that the system response to an input overdrive condition will be in the form of a predictable clipping at the system output. An output overdrive condition can result when multiple inputs are improperly combined. In digital audio systems, output stage overdrives normally occur in the digital signal processor. A processor will need to be able to handle an overdrive condition in the same way as an analogue system. Operation of a digital signal processor in its overflow or saturation mode would require that any overflow will set a value at its largest positive or negative value depending on the direction of the overflow. This prevents errors due to wraparound and yields properly limited inputs and outputs. 

## Chapter I-3 Minimum Performance Specification Under Standard Test Conditions I-3.1 Introduction

This chapter provides the minimum performance specification of the equipment and the levels to be demonstrated under standard test conditions. 

## I-3.1.1 Standard Test Conditions

For the purposes of this chapter, standard test conditions are defined in documents EUROCAE ED-14G / RTCA DO-160G, "Environmental Conditions and Test Procedures for Airborne Equipment" or the revision level as agreed with the certification authority, paragraph 3.4 as: a. 

Temperature 
: +15 to +35°C 

b. 
Relative Humidity : Not greater than 85% 
c. 
Ambient Pressure : 84 to 107 kPa 
In addition to the above, the AC electrical power supply shall be within the limits specified as Normal in section 16. of ED-14G/DO-160G or the revision level as agreed with the certification authority, the DC electrical power supply shall be within the limits specified as maximum and minimum in section 16. of ED-14G/DO-160G or the revision level as agreed with the certification authority. The electrical power supply used shall be essentially free from modulation, ripple, interruptions and surges. In the case of equipment designed for operation from an AC power source of variable frequency, unless otherwise specified, tests should be performed at representative input power frequencies with the input frequency adjusted to within 5% of a selected frequency. In the tests that follow, the Reference Signal is defined as 1 000 Hz signal having an amplitude equal to the maximum level for which the equipment is designed. 

## I-3.2 Recorder Minimum Performance Levels

The recorder shall be tested to show compliance with the following Minimum Performance Levels: 
NOTE: 
Where these paragraphs state requirements regarding the information in the recording medium it should be interpreted as that observed at the output of suitable playback equipment. 

## I-3.2.1 Start-Up And Effects Of Power Interruptions

Following a system electrical power interruption the characteristic of the CVR recorder system (including any dedicated networks, busses etc) shall be as described in the following table. The recorder system consists of the CVR recorder, area mic, CVR control panel and any interconnecting networks, busses etc.  

Recording Requirement 
Power 
Interruption 
Interruption 
Duration 
Initial Power 
Level 
Cold Start 
>2s 
No Power 
Following initial application of power to the recorder system, the system shall be capable 
of recording information in the recording medium as soon as possible but no later than 10s. Any built-in test function shall be 
completed within 60s. 
Warm 
Restart 
Within 
200ms to 2s 
Normal, Abnormal, and 
Emergency 
For interruptions with a duration of 200ms to 2s, the recorder system shall recover and commence storing information, in the recorder medium, as soon as possible but no later than 
500ms after power is restored. Any built-in test 
function shall recover within 5s(1). 
Transient 
0 to 200ms 
Normal 
Interruptions with a duration of 0 to 200ms 
shall have no effect on the recorder system.  
Power Down 
> 200ms 
Normal 
All information available at the start of an interruption together with that available in the following 200ms shall be recorded in the crashprotected recording medium. 

NOTE 1:   
          Any built-in test function may take up to 5s to recover. The recovery 
          period of 5s is intended to permit power-up test and system initialization 
          routines to be performed. It is recommended that such routines should be 
          performed as rapidly as possible to minimize the recovery period. 

## I-3.2.2 Signal Level - Balance Between Audio Channels

When half the Reference Signal Level is applied to all input audio channels, the maximum difference between the signals recovered from any two channels shall be less than 3 dB. 

## I-3.2.3 Audio Frequency Response

a. 
When half the Reference Signal level is applied to the input of the area microphone channel and its frequency is swept continuously at a rate not exceeding 0.1 octaves per second over the range defined in Table I-3.1, the level of the signal recovered from the recording medium shall not vary by more than a total range of 6 dB. 
b. 
In respect of the non-area microphone channels, the above requirement shall be met for a signal frequency range of at least 150 Hz to 3.5 kHz. 
c. 
In respect of the area microphone channel, the above requirement shall be met for a signal frequency range of at least 150 Hz to 6 kHz. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

NOTE 1: 
Synchronisation of the CVR function with other flight recorder functions can be provided by recording, on a non area microphone channel, a time signal on a 4 kHz sub-carrier. Where the frequency response cannot support such a recording and where compatibility with existing installations is to be offered, alternative provisions should be made. 
NOTE 2: 
If any rotor speed recording or timing synchronisation is to be superimposed on an audio channel then it should use frequencies which are outside of the ranges quoted in Table I-3.1 and the frequency response of the recorder should be adjusted to cater for this. 

## I-3.2.4 Quality Index

The quality of the recording shall be established and shall not be less than that corresponding to quality values for Speech Transmission Index as stated in Table I-3.1 
NOTE: 
STI is discussed in ANNEX I-D of this section. 

## I-3.2.5 Audio Noise Level - Signal To No Signal

With no signal applied to any input channel, the reproduced signal shall be below the output level produced by an input Reference Signal by the value defined in Table I-3.1. This requirement shall be met across the frequency band as defined in Table I-3.1 with the input both open and short circuited. The above Signal to No Signal performance shall be met in the presence of out-of-band input signals at the Reference level when tested in accordance with paragraph I-5.2.5. Note that if audio channels are specified with the audio frequency response of the area channel, the area channel out-of-band signal definition shall apply. 

## I-3.2.6 Audio Noise Level - Signal To Noise And Distortion

The reproduced signal to noise and distortion shall be at least the value defined in Table I-3.1 across the frequency band and over the input range of 0 to –20 dB relative to the Reference Signal Level. 

NOTE: 
Overdrive considerations are discussed in paragraph I-2.1.12. 

## I-3.2.7 Cross-Talk Between Audio Channels

When the Reference Signal is applied to any one of the inputs of the required audio recording channel, the level of the signal, recorded on that part of the recording medium assigned to each of the other recording channels, shall be below the level recorded on the intended channel by at least the amount defined in Table I-3.1. 

## I-3.3 Area Microphone And Preamplifier

The microphone sensitivity and output impedance are not controlled by this document. These values should be chosen for compatibility with the microphone preamplifier and the combination specified together as a complete unit. 

## I-3.3.1 Frequency Response - Area Microphone

The output level of the microphone shall not vary more than 10 dB (total spread) over the frequency range of 150 Hz to 10 kHz. This requirement shall be met over a sound pressure input range of 60 dB to 94 dB above 20 µPa. 

## I-3.3.2 Harmonic Distortion - Area Microphone

The distortion contributed by the microphone shall be less than 5% at sound pressure levels up to 90 dB above 20 µPa in a free field with a frequency range of 150 Hz to 8 kHz, and less than 10% at 120 dB at 1 000 Hz. 

## I-3.3.3 Polar Response - Area Microphone

When measured in a free field, the ratio of front response to the response at r 60 degrees shall fall within a r 6 dB range. 

The best microphone response pattern will be dictated by the location of the microphone in the cockpit and the need to detect pertinent airframe, power plant, avionics and pilots activity sounds while rejecting airflow and other extraneous sounds or structural vibrations.  The use of windscreens and isolation devices may also be necessary to ensure that ventilation airflow or airframe vibrations do not saturate the microphone input. 

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## I-3.3.4 Frequency Response - Microphone Preamplifier

The output level of the microphone preamplifier shall not vary more than 6 dB (total spread) when the frequency of an input signal is varied over the range of at least 150 Hz to 10 kHz and its level is held constant. 

When an input signal of constant level is varied outside the declared frequency range, the output level of the microphone preamplifier shall decrease continuously. 

## I-3.3.5 Harmonic Distortion - Area Microphone Pre-Amplifier

The total harmonic distortion of the output signal shall not exceed 5% for input signals within the range 150 Hz to 8 kHz. This requirement shall be met for input signals up to the level produced by the microphone for which the equipment is designed, when it is exposed to a sound pressure level of 120 dB above 20 µPa. 

## I-3.3.6 Signal To Noise Ratio - Area Microphone Preamplifier

The level of any noise at the output of the preamplifier shall be as least 48 dB below the level of an output signal corresponding to the maximum input signal. 

## I-3.3.7 Output Level - Microphone Preamplifier

A means shall be provided for the installer to accommodate different attenuation levels for noisy cockpit environments. This attenuation should be applied before the range compression required below. At an attenuation setting of 0 dB, when the input level of the preamplifier signal corresponds to a sound pressure level at the microphone of 120 dB above 20 µPa, the output shall not exceed the maximum input level for which the recorder is designed. At an attenuation setting of 0 dB, when the input level corresponds to a sound pressure level of 70 dB above 20 µPa, the output level shall be no more than 25 dB below the maximum level for which the recorder is designed. 

## For The Cockpit Voice Recorder

| Paragraph       | I-3.2.3    | I-3.2.4     | I-3.2.5        | I-3.2.6         | I-3.2.7         |
|-----------------|------------|-------------|----------------|-----------------|-----------------|
| Channel         | Frequency  | STI Quality | Signal to No   | Signal to Noise | Audio Crosstalk |
| Response        | Index      | Signal      | and Distortion |                 |                 |
| 150 to 6 000 Hz | 0.85       | 48 dB       | 24 dB          | 40 dB           | Cockpit Area    |
| Microphone      |            |             |                |                 |                 |
| 150 to 3 500 Hz | 0.75       | 48 dB       | 24 dB          | 40 dB           | Non Area        |
| Microphone      |            |             |                |                 |                 |
|                 |            |             |                |                 |                 |
|                 |            |             |                |                 |                 |

## Chapter I-4 Minimum Performance Under Environmental Conditions I-4.1 Introduction

CHAPTER 2-3 of this document defines the environmental tests to be performed on the recorder system. Compliance with the applicable performance requirements of this part for the Cockpit Voice Recorder shall be demonstrated as shown in Table I-4.1. Compliance with the applicable performance requirements of this part for the Cockpit Area Microphone and Preamplifier shall be demonstrated as shown in Table I-4.2. 

## I-4.2 Exceptions To General Requirements

The following exceptions to the general requirements defined in paragraph 2-3.2 apply for cockpit audio recording systems. 

## I-4.2.1 Af Conducted Susceptibility (Test 17)

The area microphone pre-amplifier signal to noise ratio specified in paragraph I-3.3.6 may be reduced to 35 dB under this environmental test condition. 

## I-4.2.2 Induced Signal Susceptibility (Test 18)

1. 
The area microphone pre-amplifier signal to noise ratio specified in paragraph I-3.3.6 may be reduced to 35 dB under this environmental test condition. 
2. 
For the area microphone, the induced signal level shall not exceed a level 
equivalent to an applied sound pressure level of 50 dB above 20 PPa. 

## I-4.2.3 Rf Susceptibility (Test 19)

1. 
The area microphone pre-amplifier Signal to No-Signal ratio specified in Part I may be reduced to 35 dB under this environmental condition. 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

MOPS PARAGRAH NUMBER 
Test 
2-1.6 
2-1.7 
2-1.12 
I-3.2.2 
I-3.2.3 
I-3.2.4 
I-3.2.5 
I-3.2.6 
I-3.2.7 
4-1.3.1 
ENVIRONMENT 
Reference 
Table 2-3.1 
NORMAL 
BIT ERROR 
Time Base 
Frequency 
Noise/ 
Audio Cross 
Data 
OPERATION 
RATE  
Stability 
Channel 
Balance 
Response 
Quality Index 
Signal/ 
Noise 
Distortion 
talk 
Crosstalk 
Temperature 
1 
R 
 
R 
R 
R 
R 
R 
R 
R 
R 
Altitude 
2 
R 
 
R 
R 
R 
R 
R 
R 
R 
R 
Temp Variation 
3 
R 
 
R 


R 
R 
 
 
Humidity 
4 
R 


R 
R 
 
 
Shock 
5 and 6 
R 
R 
R 


Vibration 
7 
R/E 
R 


Power Input 
15 
R 


Voltage Spike 
16 
R 


AF Susceptibility 
17 
R 


R 
 
 
Induced 
Susceptibility 
18 
R 


R 
 
 
RF 
Susceptibility 
19 
R 


R/E 
 
 
Lightning 
21 
R 


Blank = Manufacturer's Discretion E = Exceptions apply R = Test Required 

## Cockpit Area Microphone And Preamplifier

MOPS PARAGRAPH NUMBER 
ENVIRONMENT 
Test Reference 
I-3.3.1 
I-3.3.2 
I-3.3.4 
I-3.3.5 
I-3.3.6 
I-3.3.7 
Table 2-3.1 
Mic Response 
Mic Distortion 
Preamp Response 
Preamp Distortion 
Preamp Noise 
Preamp Level 
Temperature 
1 
R 
R 
R 
R 
R 
R 
Altitude 
2 
R 
R 
R 
R 
R 
R 
Temp Variation 
3 
 
R 
 
R 
R 
 
Humidity 
4 
R 
 
 
R 
R 
R 
Shock 
5 and 6 
R 


Vibration 
7 


Power Input 
15 


Voltage Spike 
16 


AF Susceptibility 
17 


R/E 
 
Induced Susceptibility 
18 
R/E 


R/E 
 
RF Susceptibility 
19 
R/E 


R/E 
 
Lightning 
21 


Key: Blank = Manufacturer's Discretion E = Exceptions apply R = Test Required 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter I-5 Test Procedures I-5.1 Introduction

This chapter specifies the standard test procedures for demonstrating compliance with CHAPTER I-3. Although specific test procedures are cited, it is recognised that they will not apply in all cases and that other methods may be preferred or required. Alternative methods may be used if the manufacturer can show that they provide equivalent certification data. Where a test procedure is not specified for a particular performance parameter, the manufacturer may show compliance either by analysis or by devising a test appropriate to the equipment design. 

## I-5.1.1 Adjustment Of Equipment

The equipment under test shall be properly aligned and adjusted in accordance with the manufacturer's recommendations. 

## I-5.1.2 Test Instrument Precautions

Precautions shall be taken to prevent the introduction of errors resulting from impedance mismatch and the improper connection of test instruments to the equipment under test. 

## I-5.1.3 Test Conditions

Unless otherwise stated, the test procedures of this chapter apply to systems with analogue inputs and analogue outputs. Where parts of the system use digital processing, the test procedures assume that interface conversion equipment appropriate to the recovery of the recorded information and which match the performance characteristics of the system to be certified, are used. All tests shall be performed under the conditions defined in paragraph I-3.1. 

## I-5.1.4 Connected Loads

Unless otherwise specified, all tests shall be performed with the equipment connected to loads having the impedance values for which it is designed. 

## I-5.1.6 Warm-Up Period

Unless otherwise specified, all tests shall be performed after a warm-up (stabilisation) 
period of not less than 5 minutes and not more than 15 minutes. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## I-5.1.6 Recording Of Test Results

Except where tests are GO/NO GO in character, the actual numerical values obtained for each of the parameters tested shall be recorded in a qualification test report. 

## I-5.2 Electrical Test Procedures I-5.2.1 Time Base Stability (Paragraph 2-1.12)

a. 
Equipment Required: 
High stability audio signal generator. Start-stop frequency event counter with presettable gate time. 
b. 

Measurement Procedure: Connect the signal generator to one channel of the recorder under test and record a 1 kHz time base signal for a period of at least one minute. Replay the recording and, with the aid of the event counter set to a gate time of 10 seconds and adjusted to trigger correctly on a falling edge or rising edge of the replay signal, count the number of events. 

TimeBase Error % = 100 x abs[number of event counts - 10 000]
Repeat this measurement six times and determine the time base stability by averaging the results. 

## I-5.2.2 Signal Level - Balance Between Audio Channels (Paragraph I-3.2.2)

a. 

Equipment Required Audio signal generator Attenuator Audio power meter b. 

Measurement Procedure: Connect and adjust the audio signal generator output to obtain half the reference signal level at each input of the recorder under test, and record this signal for a period of one minute. Replay the recording. Choose a reference channel, and connect its output via the attenuator to the audio power meter. Adjust the attenuator to obtain a convenient reference level and note the setting. Repeat the procedure for each of the other audio channels. The balance between channels is determined by comparing the attenuator settings. If the audio recording function is provided in a combined recorder, note test results for use in test 4-1.3.2. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## I-5.2.3 Audio Frequency Response (Paragraph I-3.2.3)

a. 

Equipment Required Sweep frequency audio signal generator Audio power meter Frequency counter b. 

Measurement Procedure Connect the audio signal generator to one channel of the recorder under test and adjust its output to obtain a signal which continuously sweeps over the frequency range defined for this channel. Adjust the sweep frequency rate to 0.1 octave per second. Set the level to half the reference signal level at equipment input. Record this signal. Replay the recording and measure the output level and frequency. Determine the level variation over the frequency band. Repeat the test with the input signal adjusted as appropriate to the channel under test. Where the recorded signal is reprocessed after a 30 minute period, recheck the output level and frequency, then determine the level variation over the frequency band for this condition. 


## I-5.2.4 Quality Index (Paragraph I-3.2.4)

This section describes a method of measuring the STI by directly generating and measuring the prescribed modulations. Other methods of making the measurement can be used provided that they are shown to be theoretically equivalent and to yield similar results (refer to ANNEX I-D). a. 

Equipment Required A signal generator and analyser as described in ANNEX I-D. The specification of the generator is given in paragraph I-D.3 and illustrated in Figure I-D.1. The specification of the analyser is given in paragraph I-D.4 and illustrated in Figure I-D.2. 

b. 

Measurement Procedure for Speech Transmission Index Filter speech weighted noise into seven octave bands to produce carriers that can be 100% amplitude modulated by the signals specified in paragraph I-D.3.4. Select each of the three modulation signals in turn to each octave band modulator. As one signal is applied to a given modulator, attenuate by 6 dB each of the other two modulation signals and sum their result to give a signal with the same peak value as the first signal. Apply this signal to all six remaining modulators. A total of 21 separate test conditions is thus defined. Combine the modulated octave band signals, and adjust the peak output level to half the Reference Signal level. Apply this signal to the channel of the recorder under test. Record each test condition for at least 30 seconds. Replay each recorded test condition in turn and measure the output of the octave band filter for that test condition using a square law detector. Determine the mean amplitude for the octave band by measuring the timeaveraged output of the detector. Select the output of each narrow bandpass filter in turn and measure the time-averaged magnitude of the modulation frequency. Calculate the modulation index from the measurements of octave bank amplitude and modulation frequency magnitude. When this has been done for all 21 test conditions, calculate the STI using the procedure given in paragraph I-D.4.5. 

## I-5.2.5 Audio Noise Level - Signal To No Signal (Paragraph I-3.2.5)

a. 
Equipment Required Audio Signal Generator A-weighted Filter IEC 651(1979) 
3rd Octave Filters IEC 225 (1966) Audio Power Meter 
b. 

Measurement Procedure: Operate the recorder and apply the Reference Signal to each recording channel for 30 seconds. Replay the recordings and measure the output levels using the audio power meter. Operate the recorder for 30 seconds for each of the following five different input conditions - open, shorted and with three separate out-of-band signals applied. For the out-of-band tests, connect the signal generator to each channel of the recorder under test and set the input signal to the Reference Signal Level. Select, in turn, frequencies of 8 kHz, 10 kHz and 12.5 kHz for the area microphone channel, and 5 kHz, 6.3 kHz and 8 kHz for the other audio channels. Replay the recordings measuring the A-weighted noise level in 3rd octave bands. Table I-5.1 and Table I-5.2 are examples for entering this data for the area microphone and audio channels respectively. Enter the calculated ratio in dB of the output for the reference signal input relative to the output for zero input.  Record the lowest value in the last row of the table.  This value should be greater than the specification given in Table I-3.1. 


## I-5.2.6 Audio Noise Level - Signal To Noise And Distortion (Paragraph I-3.2.6)

a. 
Equipment Required Attenuator 
Band pass filter Distortion meter 
b. 

Measurement Procedure: Connect the recorder via an attenuator to the signal source of the distortion meter and record signals at 3rd octave intervals over the band varying the level from the Reference Level to –20 dB in 5 dB steps. Replay the recordings and measure total harmonic distortion plus noise for each test condition. Table I-5.3 and Table I-5.4 are examples of tables for entering this data for the area microphone and audio channels respectively. Optionally, the measurement may be made after passing the replayed signal through a bandpass filter of 150 Hz to 3.5 kHz (audio channel) or 150 Hz to 6 kHz (area microphone channel). Enter the distortion plus noise as a power ratio, expressed in dB. Record the lowest value in the last row of the table. This value should be greater than the specification found in Table I-3.1. 

## I-5.2.7 Cross-Talk Between Audio Channels (Paragraph I-3.2.7)

a. 
Equipment Required Audio signal generator Audio Power meter 
b. 

Measurement Procedure: With the other input channels appropriately loaded, connect the signal generator to one channel of the recorder under test and adjust its output to the reference signal level. Record this signal for a period of one minute. Replay the recording and measure the signal level on each output channel. Repeat the test in turn for each input channel. Determine the cross-talk level for each channel for each test condition. 

## I-5.2.8 Frequency Response - (Microphone Only) (Paragraph I-3.3.1)

a. 
Equipment Required Voltmeter or Level Recorder Audio Amplifier Sweep Frequency Audio Signal Generator 
Anechoic Chamber 
b. 

Measurement Procedure: Set up and calibrate the equipment in the anechoic chamber in accordance with the manufacturer's instructions. Set the output frequency to 1 kHz and the sound pressure level to 94 dB above 20 PPa at the measurement position. 

Connect the microphone to be tested, loaded in accordance with manufacturer's recommendation, to the audio amplifier. Monitor the output of the amplifier with the voltmeter or level recorder. Position the microphone at the calibrated reference position. Operate a level recorder in tandem with the sweep frequency signal generator and derive a frequency response curve automatically over the range 150 Hz to 10 kHz or manually by adjusting the signal generator to frequencies of 150 Hz, 200 Hz, 350 Hz, 500 Hz, 600 Hz, 1 kHz, 1.5 kHz, 2 kHz, 3 kHz, 4 kHz, 5 kHz, 8 kHz, 10 kHz, reading the output on the voltmeter for each frequency. Verify that the output level remains within a 10 dB range between 150 Hz to 10 kHz. 

Repeat the test at a Sound Pressure Level of 60 dB above 20 PPa. 

## I-5.2.9 Harmonic Distortion (Microphone Only) (Paragraph I-3.3.2)

a. 

Equipment Required Audio signal generator Voltmeter Audio amplifier Anechoic chamber Distortion meter b. 

Measurement Procedure: Set up and calibrate the equipment in the anechoic chamber in accordance with the manufacturer's instructions. Set the output frequency to 1 kHz and the sound pressure level to 120 dB above 20 PPa at the measurement position. 

Connect the microphone to be tested, loaded in accordance with the manufacturer's recommendations, to the audio amplifier. Monitor the output of the amplifier with the voltmeter and distortion meter. Position the microphone at the calibrated reference position and measure the distortion level. Reduce the sound pressure level to 90 dB above 20 PPa and slowly adjust the signal generator from 150 Hz to 8 kHz and observe on the voltmeter the frequency at which maximum output from the microphone under test occurs. Note the distortion produced at this frequency. 

Repeat the test at a Sound Pressure Level of 90 dB above 20 PPa. 

## I-5.2.10 Polar Response - Area Microphone (Paragraph I-3.3.3)

a. 

Equipment Required: Audio Signal Generator Power amplifier and Loudspeaker Voltmeter b. 

Measurement Procedure: Either in a large anechoic studio or an open space free of reflecting objects, direct a high level, 1 kHz sound towards the microphone under test. The microphone should be positioned approximately 2 metres from the loudspeaker and the level set to avoid system overloading. Rotate the microphone and determine the polar response by measuring its output. 

## I-5.2.11 Frequency Response - (Pre-Amplifier Only) (Paragraph I-3.3.4)

a. 

Equipment Required: Audio power meter Audio signal generator Oscilloscope 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
b. 

Measurement Procedure: Apply a 1 kHz tone to the preamplifier input to produce half the rated output level. Maintain this input level constant and vary the frequency through the test frequency range and determine the maximum and minimum output levels. Simultaneously, use an oscilloscope to ensure there are no parasitic oscillations during the sweep. Calculate the dB difference between the two levels. Reduce the input level to produce one tenth the rated output level and repeat the measurement. At no time during this test shall the system be in an output limiting state. If limiting occurs, drop the input level below limiting and repeat the test. The test frequency sweep rate shall be limited to ensure that high Q system response will not be missed. 

## I-5.2.12 Harmonic Distortion - (Pre-Amplifier Only) (Paragraph I-3.3.5)

a. 
Equipment Required: Audio signal generator 
Audio power meter Distortion meter 
b. 

Measurement Procedure: Apply a signal corresponding to the level produced by the microphone for which the equipment is designed, when it is exposed to a sound pressure level of 
120 dB above 20PPa. Slowly adjust the signal frequency from 150 Hz to 8 kHz and observe on the audio power meter when maximum output from preamplifier under test occurs. Note the distortion level and frequency. 

## I-5.2.13 Signal To Noise Ratio - (Pre-Amplifier Only) (Paragraph I-3.3.6)

a. 
Equipment Required: 
Audio signal generator Audio power meter 
b. 

Measurement Procedure: Apply a signal with a frequency of 1 kHz and level corresponding to the maximum rated input signal. Read the output level on power meter. Disconnect the input signal and load the input with the manufacturer's recommended source impedance. Read the noise level on the power meter and determine the signal to noise ratio. 

## I-5.2.14 Output Level - (Pre-Amplifier Only) (Paragraph I-3.3.7)

a. 
Equipment Required: Audio signal generator Audio power meter 
b. 

Measurement Procedure: Apply an input signal with a frequency of 1 kHz and level corresponding to the level produced by the microphone for which the equipment is designed, when it is exposed to a sound pressure level of 120 dB above 20 PPa. Read the output level on the power meter. Repeat the measurement for an input level corresponding to 70 dB above 
20 PPa. 

## I-5.2.15 Bit Error Rate (Paragraph 2-1.7)

It shall be verified that the bit error rate arising from differences between the input to the recorder and the retrieved data caused by corruption of the data during processing, recording and retrieval does not exceed the specification in paragraph 2- 1.7. a. 

Equipment Required: Basic simulation of start/stop conditions Readout Tool 

b. 
Measurement Procedure: i. 
Apply power to the recording system,  
ii. 
Set the starting conditions to true, 
iii. 
Continue recording for duration as specified in paragraph I-1.3.2, 
iv. 
Set the stop conditions to true,  
v. 
Readout the recorded data, 
vi. 
Verify bit errors or discontinuities in recovered data are within allowance of paragraph 2-1.7. 
 

 
 
Output A-Weighted Level relative to Reference Level (dB) 
Centre Frequency 
of 3rd Octave Band 
Open 
Shorted 
Out of Band @ Reference Level 


8 000 Hz 
10 000 Hz 
12 500 Hz 
200 


250 


315 


400 


500 


630 


800 


1 000 


1 250 


1 600 


2 000 


2 500 


3 150 


4 000 


5 000 


MINIMUM SIGNAL TO NO SIGNAL RATIO = 
 
 
Output A-weighted Level relative to reference level (dB) 
Centre Frequency 
Open 
Shorted 
Out of Band @ Reference Level 
of 3rd Octave Band 


5 000 Hz 
6 300 Hz 
8 000 Hz 
200 


250 


315 


400 


500 


630 


800 


1 000 


| 1 250                               |     |     |     |     |     |
|-------------------------------------|-----|-----|-----|-----|-----|
| 1 600                               |     |     |     |     |     |
| 2 000                               |     |     |     |     |     |
| 2 500                               |     |     |     |     |     |
| 3 150                               |     |     |     |     |     |
| MINIMUM SIGNAL TO NO SIGNAL RATIO = |     |     |     |     |     |
CAM Channel 
Ref. Level  
 
 
INPUT RELATIVE TO REFERENCE LEVEL 
Frequency 
0 dB 
-5 dB 
-10 dB 
-15 dB 
-20 dB 
150 Hz 


200 Hz 


250 Hz 


--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
315 Hz 


400 Hz 


500 Hz 


630 Hz 


800 Hz 


1 000 Hz 


1 250 Hz 


1 600 Hz 


2 000 Hz 


2 500 Hz 


3 150 Hz 


4 000 Hz 


5 000 Hz 


6 000 Hz 


MINIMUM SIGNAL TO NOISE AND DISTORTION RATIO = 

 

 
INPUT RELATIVE TO REFERENCE LEVEL 
Frequency 
0 dB 
-5 dB 
-10 dB 
-15 dB 
-20 dB 
150 Hz 


200 Hz 


250 Hz 


315 Hz 


400 Hz 


500 Hz 


630 Hz 


800 Hz 


1 000 Hz 


1 250 Hz 


1 600 Hz 


2 000 Hz 


2 500 Hz 


3 500 Hz 


MINIMUM SIGNAL TO NOISE AND DISTORTION RATIO = 

## Chapter I-6 Equipment Installation And Installed Performance I-6.1 Introduction

This chapter specifies installation characteristics and performance with procedures for verifying that performance when the equipment is installed in an aircraft. Installed performance criteria are generally the same as those contained in this section, which were verified through bench and environmental tests. However, certain performance parameters may be affected by the physical installation and can only be confirmed after installation. 

## I-6.1.1 Interface Design

a. 
Figure I-6.1 of this chapter illustrates a possible CVR system configuration for 
commercial air transport aircraft and large general aviation aircraft. 
b. 
Figure I-6.2 illustrates a possible configuration using a combined flight data and audio recorder for small aircraft. 
c. 
Impedance and signal levels shall be such that a satisfactory recording is obtained without unwanted coupling between the audio system microphone and telephone circuits. With all telephone inputs set to provide maximum signal to the audio but not selected to be active on the audio control panel, and with a long term rms input to the microphone, the input level at the CVR should be the long term rms level. 
d. 
Hot mic, interphone, and radio reception With high volume control settings, the relative levels of the microphone and telephone signals shall be such that, at the summing point, the microphone signal exceeds the level of its corresponding sidetone signal on a high percentage of occasions. With an input signal to the microphone equivalent to a moderate speech level (note 1) and with input to the radio reception equivalent to a strong reception signal (note 2), when volume control settings are high (note 3), the level of the recorded microphone signal (hot mic included), shall be greater than the radio reception signal level on the majority of occasion whether interphone is in use or not. 
NOTE 1: 
According to ARINC Characteristic 538B and D0-214 definitions, a moderate speech level (or average speech level) could be 
considered with SPL (Sound Pressure Level) of 98 dB (re: 20 μPa), 
which is around 65 mV ±3 dB. 
NOTE 2: 
According to ARINC Characteristic 716 definition, transceiver nominal output level could be considered as a strong level for 2.5V 
(10 mW on 600Ω). 
NOTE 3: 
High volume control settings could be considered with a value greater than 65%. 

e. 

Hot mic, radio transmission, and interphone (when PTT is activated) The phase of any sidetone signal measured at the summing point should be within 50 degrees of the corresponding microphone signal. Where sidetone phase is uncontrolled, it is permissible for the sidetone signal to the summing point to be attenuated during radio transmissions or when interphone is selected (PTT activated). A sufficient attenuation factor will be applied in order to avoid signal cancellation effect greater than 3 dB. 

f. 
In reference to paragraphs d and e above, the "hot mic" microphone signal shall not be attenuated. 
g. 
To maintain continuous microphone recordings by the CVR during periods when radio transmitters or interphone are not selected, an energising supply shall be provided for carbon or simulated carbon microphones. This supply may be derived from the electrical supply to the summing amplifier but shall be 
interrupted if and when the microphone is energised by a radio transmitter of the interphone system. 
h. 
Transients caused by microphone switching should be suppressed to avoid blocking of any recording channel.  
i. 
The characteristics of the source and of the recording format shall be such that rotor speed within the range of at least 80% of Minimum Rotor Rotational Speed to 110% of Maximum Rotor Rotational Speed can be deduced with an accuracy of + or - 2%. Where rotor speed is periodically sampled, the maximum interval between samples shall not exceed 0.5 seconds. 

## I-6.1.2 Recorder Operation

The recorder system shall be equipped with a means to automatically start it before the aircraft moves under its own power. An acceptable means would be the detection of engine oil pressure. If required, an acceptable means of manually starting the recorder system prior to engine start (for the purpose of recording the pre-flight cockpit checks) include: a. 

pressing the CVR test button, 

b. 
operating some device early in the check list procedures. 
Once manually started, the recorder should latch to that condition until the shutdown logic is satisfied. In order to ensure reliable operation, particularly under the abnormal conditions which might precede an accident, the means provided to automatically stop the recorder should rely on more than one device, e.g. engine oil pressure, weight-on-wheels sensor and airspeed sensors. 

NOTE: 
Use of the parking brake as the sole means for control of recorder operation is not recommended since this arrangement will cause interruptions of the recording during normal taxiing operations. 

If required by operational rules, acceptable means of stopping the recorder after an accident include: i. 

detection of loss of oil pressure on all engines together with loss of airspeed. 

ii. 
airframe crash sensors, 
iii. 
water immersion sensors e.g. to detect ditching of a helicopter. 
Negative acceleration sensors ('g' switches) shall not be used as sole means of detection because their response is not considered to be reliable. 

## I-6.1.3 Bulk Erase Interlocks

Where provision is made in the cockpit for bulk erasure of the recording by the flight crew, the function shall be inhibited to prevent inadvertent or untimely erasure whilst the aircraft is capable of moving under its own power. Acceptable means of inhibiting the function include interlocks with: a. 

the parking brake and weight-on-wheels sensor, 

b. 
the main cabin door position sensor and weight-on-wheels sensor, 
c. 
In the case of a helicopter, the rotor brake and weight-on-wheels sensor. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## I-6.1.4 Quality Of Recording

For each newly installed system, the quality of the recording shall be established by analysis of information recorded on the ground and in flight. The relevant accident investigation authority shall be invited by the Certification Authority to participate in the assessment of new systems. 

 

## I-6.1.5 Cvr Systems Audio Delays

Flight crew audio channels shall be compliant with DO-214 for absolute delay. Any individual delay shall be such that it shall not compromise the channels synchronization requirement defined in I-2.1.8b. 

The delay in recording the flight crew audio signals from the time of reception at the microphones to the time of recording on the protected recording medium shall not exceed 250 milliseconds. 

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## I-6.2 Equipment Location I-6.2.1 Area Microphone Location

Particular attention shall be given by installers to the location of the area microphone. 
To aid in voice and sound discrimination, general rules for optimum performance are: a. 
Position the microphone for recording general cockpit sounds, voice communications originating at the 
pilot and 
co-pilot stations, voice 
communications of other flight crew members in the cockpit when directed to those stations, and for helicopters, transmission gearbox sounds. In certain cases, it may be necessary to install an additional area microphone in order to obtain adequate recordings of cockpit and/or transmission gearbox sounds. 
b. 
Correct phasing of microphones needs to be observed. Refer to paragraph I-2.1.10. 
c. 
Position the microphone to minimize noise from vents, fans, windshield wipers and other undesirable acoustic noise generators. Additionally, to minimise airstream noise, the installer should consider isolation of the microphone from 
structure connected to the aircraft skin. 
d. 
Position the microphone away from cockpit loudspeakers. 
e. 
Position the microphone such that it cannot be obstructed by loose articles e.g. navigation charts. 
f. 
Position the microphone such that it is unlikely to be damaged during crew entry to, or exit from the cockpit. 
g. 
Do not install the microphone on the lower centre console except where a second microphone is installed elsewhere. 

## I-6.3 Flight Test Procedures I-6.3.1 General

a. 
This section provides guidance for flight testing prototype installations in both aeroplanes and helicopters. It may need to be adapted to suit the particular installation being tested and to comply with operating regulations. 
b. 
Each newly installed CVR shall be flight tested and the recording, so obtained, to be evaluated to show adequate recording quality during all normal regimes of flight including taxiing, take-off, cruise, approach and landing. For helicopters, hover and autorotation should be included. 
c. 
Since the duration of the recording may be limited, the test flight should be carefully planned. The CVR circuit breaker can be tripped between each test 
phase and at the end of the landing run if the flight time is likely to exceed the recording duration limit. 
d. 
Systems which generate sounds in the cockpit and which might not otherwise be used during the test flight should be operated with appropriate announcements by the flight crew. 
e. 
To enable proper analysis of the recording, it is essential that adequate commentary on the flight is provided, e.g. flight crew actions, altitudes and speeds. Each test should be clearly announced and the flight crew member identified, e.g. "Co-pilot testing oxygen mask microphone with interphone off". 
f. 
The replay and evaluation shall be performed by a replay centre acceptable to the Certification Authority. Refer to ANNEX I-A. 

## I-6.3.2 Prior To Engine Start

a. 
Check that the CVR is operating. 
b. 
Press the ERASE button (if fitted). 
c. 
Confirm CVR Serviceability e.g. by pressing the CVR TEST button. 
d. 
Select BOOM microphone and interphone ON at all flight crew stations. 
e. 
Identify each flight crew member, the aircraft type and registration, date and time. 
f. 
Call out the location of the area microphone e.g. centre pedestal, overhead panel, glareshield. 

## I-6.3.3 Engine Start

a. 
(Helicopters only). During rotor spin-up, call out rotor speed at 50%, 80% and 100%. 
b. 
Make a test announcement from each flight crew station in turn using the boom 
microphones 
with 
interphone 
selected 
'ON' 
followed 
by 
a 
second 
announcement with the interphone OFF, i.e. "hot microphone" function. 
c. 
Repeat paragraph I-6.3.3b. using the oxygen mask microphone. 
d. 
(Aeroplanes only). Announce and test the stall warning stick shaker (if fitted). 
e. 
(Helicopters only). Close the cockpit windows. 

## I-6.3.4 Take-Off

a. 
With headsets on and boom microphones in position for use, record a normal take-off and initial climb. 
b. 
Announce landing gear and flap selections and propeller settings (where applicable). 

## I-6.3.5 Cruise

a. 
With interphone OFF at all stations, announce and activate aural warnings. 
b. 
(Aeroplanes only). Where regulations permit, accelerate to, and announce VMO. Continue until the overspeed warning sounds. Reduce speed as required. 
c. 
Perform a VHF test transmission from each pilot's station using boom microphones. (VHF audio should be selected OFF at all other flight crew stations). 
d. 
Perform a VHF test transmission from each pilot's station using hand-held microphone and the cockpit loudspeakers. (VHF audio should be selected OFF 
at all other flight crew stations). 
e. 
Perform a test transmission from each pilot's station using HF (if fitted) and boom microphones. (HF audio should be selected OFF at all other flight crew stations). 
f. 
Perform test broadcasts from the cockpit and the cabin using the passenger address system. 
g. 
(Helicopters only) Call out rotor RPM. 
h. 
Announce and open the cockpit-cabin door. Announce and close the door after approximately 10 seconds. 
i. 
Where permitted, announce and open the cockpit windows. Announce and close the windows after approximately 10 seconds. 
j. 
Where available, acknowledge verbally, a digital message received via the digital data link system. 

## I-6.3.6 Helicopter Auto-Rotation And Hover

a. 
At a safe altitude, perform an auto-rotation descent with power recovery. 
b. 
Announce and hover for approximately 20 seconds. 

## I-6.3.7 Landing

a. 
Record final approach and landing including ILS and Marker audio identification. Announce landing gear and flap selection and other actions. 
b. 
At end of landing run call out the time. 
c. 
Select BOOM microphone and interphone ON at all flight crew stations and announce "End of Audio Recorder Test". 
d. 
DO NOT ERASE (if fitted). 
e. 
Remove aircraft power from the CVR system. 
 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Annex I-A Post Flight Evaluation Of Recordings I-A.1 Introduction

I-A.1.1 
Following the flight testing of each new CVR installation, the recording so obtained shall be evaluated to confirm adequate quality. Similarly, it will be necessary to evaluate recordings obtained on a sampling basis from in-service flying or following cockpit modification, which may change the audio environment to ensure that quality is maintained. 
I-A.1.2 
It is recommended that the replay equipment be located in a clean, quiet area which is separated from other work areas sufficiently to ensure the privacy of recordings and to protect other staff from exposure to irritating noise. Access to the replay equipment should be restricted to authorised personnel only. 
I-A.1.3 
Provision shall be made for the secure storage of CVR recording media and any 
copies made. 
I-A.1.4 
The replay and evaluation of recordings shall be performed by personnel with adequate knowledge of CVR systems and aircraft operations, and who have appropriate experience of the techniques used to evaluate recordings. 
NOTE 1: 
Accident investigation authorities may be able to provide demonstrations which would assist the training of personnel. 
NOTE 2: 
Where possible, replay personnel should be given the opportunity to accompany the flight crew on a CVR test flight in order to become familiar with the test procedure. 
I-A.1.5 
A test report and certification in a format acceptable to the Certification Authority will be required to record the observations made from evaluation of the recording. 

## I-A.2 Replay Equipment

I-A.2.1 
Experience has shown that a multi-channel replay method re-creates the flight conditions with a measure of realism which assists subjective evaluation of the recording. For this reason, the evaluation of recordings from new CVR installations should involve replay on equipment capable of multi-channel reproduction. 
I-A.2.2 
The recording should be copied to a multi-track instrumentation quality audio recording for qualitative and quantitative evaluation and to provide evidence of recording quality. 
I-A.2.3 
An oscilloscope may be required to check recorded signal levels. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

I-A.2.4 
For CVRs removed from helicopters, the replay equipment will need filters and decoders for retrieval of the rotor speed data and where applicable the public address signals. To enable rotor speed to be correlated with announcements by the flight crew, the replay equipment shall be able to output the audio and data channels simultaneously. 
 

## I-A.3 Recording Evaluation

I-A.3.1 
The recording on each channel shall be checked to confirm that the required input sources are connected to the CVR system, and that recorded levels and signal quality are acceptable. 
I-A.3.2 
In general, the proper recording level will be confirmed using the oscilloscope to show that the full recording dynamic range has been achieved without excessive clipping of peak signals. A check should be made to confirm that adequate signal to noise ratios exist for all significant input signals, and that signal levels are reasonably balanced between the channels. Signal quality may be confirmed during subjective listening checks and by ensuring that the recording is free from electrical interference and from the effects of vibration. The presence of cockpit sounds, crew speech and audible warnings should be confirmed on the area microphone channel. Extracts of the recording should be either photographed from the oscilloscope, or printed on strip paper as further evidence of recording quality. 
NOTE 1: 
A low level of 400 Hz interference may be tolerated since it provides a 
crude but useful timebase for accident investigation. 
NOTE 2: 
Momentary recording disturbances of a minor nature, caused by vibration, can be tolerated during take-off and landing whilst the aircraft is on the runway. 
NOTE 3: 
To avoid signal cancellation effects, and to ensure that incoming radio messages do not mask flight crew speech, with a moderate speech level (refer to paragraph I-6.1.1) levels of telephone signals, at high volume control settings (greater than 65%), should be preset lower than the CVR hot-mic signal level. 
I-A.3.4 
For combined CVR and FDR systems, flight data recordings may be verified by correlating data values against announcements made by the flight crew, and by ensuring that the parameter range and resolution available are sufficient to meet the specified range/accuracy requirements. 
NOTE: 
Further verification of data accuracy may be required by the certification authority. This aspect of data verification is the subject of Part II of this document. 

## I-A.4 Test Report

I-A.4.1 
A suitable report is shown in Table I-A.1. The report may be supplemented by photographic or printed evidence obtained from selected extracts of the recording. 
I-A.4.2 
The spaces on the report, as applicable, should be annotated with brief comments on the replay signal quality. 

| ABC AVIONICS     |
|------------------|
| Municipal Road   |
| TOONVILLE        |
COCKPIT VOICE RECORDER - FLIGHT TEST EVALUATION AIRCRAFT TYPE:  ...................... REGN:  ........................................ OPERATOR:  
.................................. 
 
CVR TYPE:  
................................. SERIAL NO:  
................................ FLIGHT NO:  
................................... 
 
RECORDING QUALITY CHECK 
INPUT CHANNEL 
1 
2 
3 
4 
FUNCTION 


MICROPHONES 


HOT-MIC BOOM 


HOT-MIC MASK 


HOT-MIC LEVELS 


TELEPHONES / PA 


RADIO RECEPTION 


RADIO SIDETONE 


INTERPHONE 


PUBLIC ADDRESS 


WARNINGS 


SIGNAL LEVEL 


AREA MIC 


COCKPIT SOUNDS 

 


WARNINGS 

 


SIGNAL LEVEL 


ROTOR SPEED 


RANGE 

 


RESOLUTION 

 


SIGNAL LEVEL 

 


TIME SIGNAL 


................................................................................................................................................ 

 
Certified that the above mentioned recording has been evaluated in accordance with the terms of the contract/order applicable thereto and the requirements of the Certification Authority relating to the evaluation of such recordings. 

 
.......................................................................DATE:  
................................................................. 

for and on behalf of ABC Avionics Organisation Approval Reference ..........................................................  

## Annex I-B Speech Encoding Considerations I-B.1 General

Speech encoding methods fall generally into two categories, waveform coders which attempt to exploit redundancy in the audio waveform and source modelled coders which assume that the audio is produced by human vocal tracts which can be modelled. There is a large variation of features for specific methods from both categories and, consequently, their performance. The following paragraphs discuss the considerations which are important to the fidelity of the recording. These considerations are not all inclusive and are not intended to limit the application of new technology or techniques. Specific encoding methods should be evaluated on their ability to satisfy the requirements of this document. 

## I-B.2 Information Retrieval

All forms of encoding should be readily reversible so that as much information as possible can be recovered from an incomplete or corrupted recording. Methods which require large, complete, error free records of encoded data in order to successfully reconstruct the information should be avoided. 

## I-B.3 Effect Of Noise And Non-Speech Audio

The selection of an encoding method should take account of the fact that all the recorded channels are likely to have considerable levels of noise and non-speech audio information (sounds). The performance of the recording system should be compatible with these sounds. The sounds should be reproduced with as much fidelity as possible. For this reason waveform coders are in general preferable to source modelled coders. 

## I-B.4 Determination Of Recording Medium Capacity

If variable rate encoding is used, the required duration of the recording shall be demonstrated for all foreseeable input conditions. That is to say, full recording time is met when the maximum expected amount of radio communications, crew conversations and cockpit noise is recorded. Careful attention shall be given to time correlation between channels. 


## Annex I-C Maintenance Practices I-C.1 General

The maintenance tasks required to ensure the continued serviceability of the installed CVR system will depend on the extent of monitoring built into the CVR system. The installer shall perform an analysis of the CVR system to identify those parts of system which, if defective, would not be readily apparent to the flight crew or maintenance personnel. Appropriate inspections and functional checks, together with the intervals at which these would need to be performed, need to be established as indicated by the analysis. The specified checks need to include verification of system performance, where appropriate. A flight recording should be replayed at specified intervals to reveal defective equipment and to indicate essential maintenance actions. Where a replay evaluation indicates an aircraft system defect, appropriate corrective action shall be initiated. Any inspection or test requirements specified by equipment manufacturers shall be observed, e.g. battery checks of the underwater locator beacon. Maintenance and flight crew procedures should emphasise the need to preserve the recording following a reportable occurrence. 

## I-C.2 Recording Evaluation

An in-flight recording should be replayed and assessed for quality. ANNEX I-A provides guidance for the evaluation of such recordings. Cockpit Voice recorder systems should be considered unserviceable if the recording duration is less than required, if there is a period of poor quality audio or unintelligible audio/sounds. 

## I-C.3 Primary Maintenance Tasks

Table I-C.1 shows the primary maintenance tasks for the installed CVR system. Inspection periods should be established on the basis of the CVR system analysis discussed in paragraph I-C.1. 

 

| Item                                   | Equipment                          | Task                               | Maximum Interval    |
|----------------------------------------|------------------------------------|------------------------------------|---------------------|
| Operational                            |                                    |                                    |                     |
| Check                                  |                                    |                                    |                     |
| Daily (pre-flight and/or               |                                    |                                    |                     |
| post-flight)                           |                                    |                                    |                     |
| 1                                      | Cockpit Voice                      |                                    |                     |
| Recorder                               |                                    |                                    |                     |
| System                                 |                                    |                                    |                     |
| Confirm serviceability using TEST      |                                    |                                    |                     |
| function on CVR controller or Check    |                                    |                                    |                     |
| 'no                                    | -                                  | fail' indication for built in test |                     |
| Not exceeding 6                        |                                    |                                    |                     |
| months elapsed time                    |                                    |                                    |                     |
| 2                                      | Check/                             |                                    |                     |
| Functional                             |                                    |                                    |                     |
| Test                                   |                                    |                                    |                     |
| Inspect Installation. Confirm, by      |                                    |                                    |                     |
| means of the CVR Controller monitor    |                                    |                                    |                     |
| jack, proper recording on each audio   |                                    |                                    |                     |
| channel from area microphone(s),       |                                    |                                    |                     |
| receiver audio, sidetone, interphone,  |                                    |                                    |                     |
| public address (if recorded) and boom  |                                    |                                    |                     |
| micropho                               | ne (including 'hot mic'            |                                    |                     |
| function, i.e. interphone OFF).        |                                    |                                    |                     |
| Confirm proper functioning of the      |                                    |                                    |                     |
| inhibit logic for the bulk erase.      |                                    |                                    |                     |
|                                        |                                    |                                    |                     |
| Check/Replay Not exceeding interval    | 3                                  | Cockpit Voice                      |                     |
| Recorder                               | stated by the vendor               |                                    |                     |
| Remove recorders for inspection and    |                                    |                                    |                     |
| test as required by the Component      |                                    |                                    |                     |
| Maintenance Manual.                    |                                    |                                    |                     |
| NOTE:                                  |                                    | The recording stored on            |                     |
| the media prior to the                 |                                    |                                    |                     |
| removal                                | should                             | be                                 |                     |
| evaluated.                             |                                    |                                    |                     |
| Not exceeding 24                       |                                    |                                    |                     |
| months elapsed time                    |                                    |                                    |                     |
| Confirm proper sensor function. Test   |                                    |                                    |                     |
| may be performed in-situ if practical. |                                    |                                    |                     |
| 4                                      | Ditching                           |                                    |                     |
| Sensor                                 |                                    |                                    |                     |
| (Helicopter)                           |                                    |                                    |                     |
| Check/                                 |                                    |                                    |                     |
| Functional                             |                                    |                                    |                     |
| Test                                   |                                    |                                    |                     |
| 5                                      | Crash Sensor                       |                                    |                     |
| (where fitted)                         |                                    |                                    |                     |
| As stated by vendor                    | Comply with instructions issued by |                                    |                     |
| vendor                                 |                                    |                                    |                     |
| Check/                                 |                                    |                                    |                     |
| Functional                             |                                    |                                    |                     |
| Test                                   |                                    |                                    |                     |
| 6                                      | Underwater                         |                                    |                     |
| Locator Beacon                         |                                    |                                    |                     |
| As stated by vendor                    | Comply with instructions issued by |                                    |                     |
| vendor                                 |                                    |                                    |                     |
| Check/                                 |                                    |                                    |                     |
| Functional                             |                                    |                                    |                     |
| Test                                   |                                    |                                    |                     |
| 7                                      | Cockpit Voice                      |                                    |                     |
| Recorder                               |                                    |                                    |                     |
| Remove CVR immediately post-flight.    |                                    |                                    |                     |
| Replay and evaluate the quality of the |                                    |                                    |                     |
| in-flight recording.                   |                                    |                                    |                     |
| Check in                               |                                    |                                    |                     |
| accordance                             |                                    |                                    |                     |
| with criteria                          |                                    |                                    |                     |
| and                                    |                                    |                                    |                     |
| procedures                             |                                    |                                    |                     |
| agreed with                            |                                    |                                    |                     |
| the Regulatory                         |                                    |                                    |                     |
| Authority                              |                                    |                                    |                     |
| One year, or up to a                   |                                    |                                    |                     |
| maximum of two years                   |                                    |                                    |                     |
| if approval from the                   |                                    |                                    |                     |
| appropriate regulatory                 |                                    |                                    |                     |
| authority has been                     |                                    |                                    |                     |
| obtained for CVR                       |                                    |                                    |                     |
| systems that have a                    |                                    |                                    |                     |
| demonstrated high                      |                                    |                                    |                     |
| integrity of                           |                                    |                                    |                     |
| serviceability self-                   |                                    |                                    |                     |
| monitoring                             |                                    |                                    |                     |
|                                        |                                    |                                    |                     |

## Annex I-D Speech Transmission Index I-D.1 Introduction

The aim of including a Quality Index measurement in this MOPS is to ensure that a minimum standard of speech intelligibility is achieved by recording systems.  

## I-D.2 Speech Transmission Index

Speech Transmission Index is a method of quantifying the intelligibility of speech with respect to a transmission medium. STI is based on the implication that the temporal speech envelope at the listener replicates the speech envelope at the speaker's mouth. The test signal consists of a noise carrier having a speech shaped spectrum with sinusoidal intensity modulation. Intelligibility can be quantified in terms of the changes in the modulation envelope due to the transmission path, taking account of interfering noise, echoes or reverberation. This is expressed as a modulation reduction factor or Modulation Transfer Function (MTF). This phenomenon presents itself as a reduction of signal to noise ratio irrespective of its cause. The full STI method uses 14 modulation frequencies in 7 octave bands resulting in 98 data points. It has been demonstrated (reference I-D.4.7a) that when these measurements are combined, very good correlation with accepted subjective intelligibility measurements can be achieved, for example scores from phoneticallybalanced word tests. The need for such a large number of data points to measure STI is due to the effects of time domain distortions such as reverberation and echoes. In these cases the MTF may be strongly dependent on modulation frequency. These distortions are not characteristic of recording systems, so the method described here, and in the test procedure given in the MOPS (paragraph I-5.2.4), uses a subset of the 14 modulation frequencies. Only 3 modulation frequencies are used to cover the range. This technique reduces complexity where time domain distortions are not present and has been validated (reference I-D.4.7a). The MTFs for each octave band are weighted and combined to produce an index in which a value of 1.0 represents perfect speech intelligibility. The subjective ratings corresponding to ranges of STI values are presented in Table I-D.1. 

STI Subjective Ratings 
0.10 - 0.30 
BAD 
0.30 - 0.45 
POOR 
0.45 - 0.60 
FAIR 
0.60 - 0.75 
GOOD 
0.75 - 0.99 
EXCELLENT 

## I-D.3 Specification For The Sti Signal Generator (Refer To Figure I-D.1)

I-D.3.1 
Gaussian Noise Generator Power spectral density flat within ± 0.1 dB from 80 Hz to 12 kHz, averaged over the 
measurement period. 
I-D.3.2 
Speech Weighting Filter 2-pole low-pass filter with poles at: 225 Hz, 1667 Hz, and Attenuation A, defined as: 
A (f) = 10log${}_{10}$ (1 + $\frac{\mbox{f}^{2}}{4.957\ \mbox{x}\ 10^{4}}$ + $\frac{\mbox{f}^{4}}{1.401\ \mbox{x}\ 10^{11}}$ ) dB
 
Tolerance ± 0.5 dB. 

I-D.3.3 
Octave Band Filters ANSI S1.11-1986 defined 2/3 octave band filters, Order 5, Type 1-D. Centre 
frequencies 125 Hz, 250 Hz, 500 Hz, 1 kHz, 2 kHz, 4 kHz, 8 kHz. 
I-D.3.4 
Modulating Signal Generator Three selectable modulating signals (0.8 Hz, 3.15 Hz, 10 Hz). Three 6 dB attenuators and a signal combiner. Amplitude match ± 0.1 dB. 

I-D.3.5 
Modulators Frequency response over each octave band ± 0.1 dB. Gain match ± 0.1 dB. 
I-D.3.6 
Summing Amplifier Gain adjusted to give total output power - 6 dB relative to CVR Reference Signal level, measured over the band from 80 Hz to 12 kHz. 

## I-D.4 Specification For The Sti Analyser

I-D.4.1 
Octave Band Filters ANSI S1.11-1986 defined 2/3 octave band filters, Order 5, Type 1-D. Centre frequencies 125 Hz, 250 Hz, 500 Hz, 1 kHz, 2 kHz, 4 kHz, 8 kHz. 
I-D.4.2 
Square Law Detector Frequency response 80 Hz to 12 kHz, ± 0.1 dB. 
I-D.4.3 
Modulation Filters 
ANSI S1.11-1986 defined 1/3 octave band filters, Order 5, Type 1-D. Centre frequencies 0.8 Hz, 3.15 Hz, 10 Hz. 
I-D.4.4 
Averaging Meter Frequency response dc to 25 kHz, ± 0.1 dB. Converts input, x, to absolute value,[x], and takes an unweighted average over the measurement interval. The interval shall be sufficient to make a measurement with an accuracy better than 2 %. 

I-D.4.5 
Calculation Method 
For kth octave band, 

1. 
Mean intensity (measured),  
Ik 

2. 
Modulation indices (measured), 
mk,Fi 

3. 
Mean intensity of (k-1)th band, 
Ik-1 

 
(Note: Io = O) 
4. 
Auditory Masking Factor, 
AMF 
 
(Note: Constant = 0.0003) 
5. 
Apparent Masking intensity, 
IAM,k = Ik-1 . AMF 
6. 
Auditory Correction Factor, 
ACFk = Ik / (Ik + IAM,k) 
7. 
Corrected modulation indices, 
m'k,Fi = ACFk . m k,Fi 
8. 
Effective Signal-to-Noise Ratio, 
 
SNR k,Fi = 10 . log10[m'k,Fi / (1 - m'k,Fi)] db 
 
0< m'k,Fi <1 
9. 
Transmission Index, 
 
TIk,Fi = (SNRk,Fi + 12)/18 
 
0< TI k,Fi <1 
10. 
Combine the Transmission Indices for each modulation frequency, Fi, 
3
 

¦
Fi K, K
TI
3
1
TI
 
1
i
 

11. 
Combine TIk's from each octave band in a weighted sum, 
$${\mathsf{S T I}}=\sum_{\mathsf{K}=1}^{7}\left(W_{\mathsf{K}}\ \cdot\ T\,|_{\mathsf{K}}\right)$$

|    |            | Weighting factors,    |
|----|------------|-----------------------|
|    | W1 = 0.129 | W5 = 0.186            |
|    | W2 = 0.143 | W6 = 0.171            |
|    | W3 = 0.114 | W7 = 0.143            |
|    | W4 = 0.114 |                       |

I-D.4.6 
Alternative Measurement Methods Alternative methods of making the STI measurement can be used providing they are shown to be theoretically equivalent and to yield similar results. Reference to the relevant documents is given in paragraph I-D.4.7. 

I-D.4.7 
References a. 
H.J.M. Steeneken and T. Houtgast, "A physical method for measuring speech transmission quality", J. Acoust. Soc. Amer. vol 67 (1980) pp 318. 
b. 
D. Rife and J. Vanderkooy, "Transfer function measurement with maximum length sequences", J. Audio Engr. Soc. (JAES) vol 37 (1989) pp 419. 
c. 
R.H. Campbell, "Analog Tape Recorder Analysis Using MLSSA", Bang- Campbell Associates, Massachusetts 02543-0047, USA. 
d. 
D. Rife, "MLSSA reference manual version 7.0", DRA Laboratories (1991), 24 Halifax Court, Sterling Virginia, USA, 22170. 
e. 
ANSI S1.11-1986 Specification for Octave-Band and Fractional-Octave-Band Analogue and Digital Filters. 

## Part Ii Flight Data Recorder Systems

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter Ii-1 Introduction Ii-1.1 Purpose And Scope Ii-1.1.1 General

This part defines the minimum specification to be met for all aircraft required to carry a Flight Data Recorder system for the purposes of the investigation of a reportable accident or incident. It is applicable to crash-protected recorders, ancillary equipment and their installation in civil aircraft. This part shall be read in conjunction with Sections 1 and 2, together with Sections 3, 4 and 5 as applicable. 

## Ii-1.1.2 Description Of Content

This part is divided into six Chapters and four Annexes. 

CHAPTER II-1 describes typical equipment applications and operational objectives. Background material and accident investigation considerations are included together with a description of the FDR system. CHAPTER II-2 defines the general design specification. CHAPTER II-3 defines the minimum system performance under standard test conditions. CHAPTER II-4 defines the minimum system performance under environmental test conditions. CHAPTER II-5 specifies tests and procedures for determining compliance with the performance requirements and for demonstrating crash survival capability. CHAPTER II-6 defines the installed equipment performance requirements including ground tests and flight tests. Annexes provide details of parameters to be recorded and give additional guidance on maintenance practices, data compression techniques and electronic documentation standards. 

## Ii-1.2 Application Ii-1.2.1 Flight Data Recording

Compliance with this Part will ensure that FDR systems will perform their function under the conditions encountered in aircraft operations. 

## Ii-1.3 Description Of System Ii-1.3.1 Equipment

The FDR system may include the following items of equipment as appropriate to the aircraft. a. 
Equipment necessary to: i. 
acquire and process analogue and digital sensor signals;  
ii. 
store the recorded data in crash survivable recording medium; and 
iii. 
when necessary, support dedicated sensors. 
b. 
Digital data busses and/or networks providing communications between elements of the system 
 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Ii-1.3.2 Classes Of Flight Data Recorder

The classes of flight data recorders specified in this section are based upon the number and type of defined parameters to be recorded and the required recording duration. The number and type of parameters to be recorded is also specified within the operational rules of each ICAO member state, as is the required recording duration. This being so, all recommendations within this section relating to classes of recorder should be checked against the appropriate operational rule. Whilst the operational rule always takes precedence over a EUROCAE MOPS, if the requirements it specifies are less stringent than those specified here, the aims and needs of accident/incident investigation will be better served if the recorder is designed to meet this section. For the purpose of this MOPS, flight data recorders are classified as follows. These classes of recorder correspond with one or more types as defined in ICAO Annex 6 as shown. a. 

EUROCAE FDR Class A: 
A non-deployable recorder which is capable of retaining the data recorded during at least the last 25 hours of its operation. This recorder type shall have sufficient recording medium capacity for the parameters defined in ANNEX II-A Table II-A.1 (Aeroplanes) of this MOPS i.e. equivalent to an ICAO Type Ia recorder. 

b. 

EUROCAE FDR Class B: A non-deployable recorder which is capable of retaining the data recorded during at least the last 10 hours of its operation. This recorder type shall have sufficient recording medium capacity for the parameters defined in ANNEX II-A Table II-A.2 (Helicopters) of this MOPS i.e. equivalent to an ICAO Type IVa recorder 

c. 
EUROCAE FDR Class C: 
The requirement for this class of recorder has been deleted 
d. 

EUROCAE FDR Class D: Deployable recorders equivalent to the Class B recorders. The installation of this type of recorder is restricted. Refer to SECTION 3 (DEPLOYABLE RECORDERS). 

e. 
EUROCAE FDR Class E: The requirement for this class of recorder has been deleted 
f. 

EUROCAE FDR Class F: 
Deployable recorders equivalent to the Class A recorder. The installation of this type of recorder is restricted. Refer to SECTION 3 (DEPLOYABLE 
RECORDERS). 

NOTE: 
         Each recorder, irrespective of its class, should have spare capacity or 
         provision for additional recording medium capacity to accommodate the 
         additional parameters that may be required by specific operating 
         conditions or additions to operational rules. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Ii-1.3.3 Operational Considerations

a. 
Objectives The general objectives to be met by flight recorder systems in aircraft are stated in ICAO Annex 6, Parts I, II and III. Seven types of recorder are defined by 
ICAO which relate to their operational use as follows: i. 
ICAO Type I: A recorder for use in aeroplanes over 27 000 kg MCTOM and which is capable of retaining the data recorded during the last 25 hours of its operation. A Type I recorder shall record the parameters required to determine accurately the aeroplane flight path, speed, attitude, engine power, configuration and operation. 
ii. 
ICAO Type  IA: A recorder for use in aeroplanes over 5 700 kg MCTOM and which is capable of retaining the data recorded during the last 25 hours of its operation. A type IA recorder shall record the parameters required to determine accurately the aeroplane flight path, speed, attitude, engine power, configuration and operation. 
iii. 
ICAO Type II: A recorder for use in aeroplanes over 5 700 kg and up to and including 27 000 kg MCTOM and which is capable of retaining the data recorded during the last 25 hours of its operation. A Type II recorder shall record the parameters required to determine accurately the aeroplane flight path, speed, attitude, engine power and configuration of lift and drag devices, 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

iv. 
ICAO Type IIA: A recorder for use in multi-engine turbine power aeroplanes of 5 700 kg MCTOM or less and which has the same objectives as the Type II except that the recording duration is 30 minutes. In addition to this 30 minutes of recording duration, the recorder shall retain sufficient data from the preceding take-off for the purposes of calibration, 
v. 
ICAO Type IV: A recorder for use in helicopters over 7 000 kg MCTOM and which is capable of retaining the data recorded during the last 10 hours of its operation. A Type IV recorder shall record the parameters required to determine accurately the helicopter flight path, speed, attitude, engine power and operation, 
vi. 
ICAO Type IVA: A recorder for use in helicopters over 3 180 kg MCTOM and which is capable of retaining the data recorded during the last 10 hours of its operation. A type IVA recorder shall record the parameters required to determine accurately the helicopter flight path, speed, 
attitude, engine power, configuration and operation. 
vii. 
ICAO Type V: A recorder for use in helicopters over 3 180 kg and up to and including 7 000 kg MCTOM and which is capable of retaining the data recorded during the last 10 hours of its operation. A Type V recorder shall record the parameters required to determine accurately the helicopter flight path, speed, attitude, engine power. 
In addition to the general objectives described above, flight recorders shall be constructed, located and installed so as to provide maximum protection for the recordings in order that the recorded data may be preserved, recovered and transcribed. 

## B. Start And Termination Of Recording Recorder Operation Shall Be As Defined In Paragraph 2-1.5. Chapter Ii-2 Fdr Specification Ii-2.1 Equipment Design Specifications Ii-2.1.1 General

This section is applicable to the functions of a flight recorder system designed to receive, process, record and preserve flight data in accordance with the requirements of this MOPS. These functions shall be performed reliably even under adverse operating conditions including events leading to an accident. To meet the requirements of different aircraft technologies, the recording system shall be capable of accepting and processing information of the following types: a. 

Flight data parameters as defined by this section of the MOPS in ANNEX II-A;  

b. 
Time signals for synchronising the flight data with other flight recording 
functions, 
This section shall be read in conjunction with Section 2, which defines the requirements that are generic to all flight recorders. The FDR system shall perform its intended function under all foreseeable operating conditions. 

## Ii-2.1.2 Self-Monitoring Of Proper Operation

a. 
Means shall be provided, as far as is practicable, to detect the loss of the data from sensors connected to the flight data recorder and causing a fault indication. 
b. 
When the FDR system provides an excitation voltage for dedicated FDR sensors, a means of detecting and reporting when this signal is not available shall be provided. 
NOTE 1: 
Except where sensor unserviceability would be detectable by other means, a flight recorder maintenance indicator should be set. 
NOTE 2: 
Where sensor data is not monitored and where the sensor unserviceability would remain undetected or would not be evident to the flight crew, a maintenance task should be specified to check, at appropriate intervals, that the sensor is operating within its specified limits and that data is being supplied to the recorder. 
NOTE 3: 
Except where the overall performance of the recorder would be adversely affected, data from a defective sensor should continue to be recorded. 

## Ii-2.1.3 Recorder Synchronisation

The recordings on the FDR shall be synchronised to other airborne recordings as defined in paragraph 2-1.11.  

## Ii-2.1.4 Recording Technology

a. 
The flight recorder shall use a digital method of recording and storing the data and a method of readily retrieving that data from the recording medium. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

b. 
The method of retrieval shall not alter, or re-write, the data in the recording medium. 
c. 
The recording medium shall be physically segregated in such a way that the non-availability of a single memory device does not lead to the loss of more than 16 seconds of contiguous data. 
NOTE: 
Redundant recording is an acceptable means of compliance. 

## Ii-2.1.5 Start And Termination Of Recording

Recorder operation shall be as defined in paragraph 2-1.5. 

## Ii-2.1.6 Data To Be Recorded

a. 
Data shall be recorded within the range, resolution, accuracy and sampling intervals specified in ANNEX II-A,  
b. 
Any novel or unique design or operational characteristics of the aircraft shall be 
evaluated to determine if any dedicated parameters should be recorded in addition to or in place of existing requirements.  
c. 
The flight recorder shall use a digital method of recording and storing the data and a method of readily retrieving that data from the recording medium. 
d. 
Data shall be obtained from sources within the aircraft which provide the most accurate and reliable information under both static and dynamic conditions. 

## Ii-2.1.7 Erasure Of Recorded Data

a. 

Except for the overwriting of the oldest data by new information, no means for the erasure of the record shall be provided in the recorder.  
NOTE: 
It is understood that military organisations may use commercial recorders. In this case, they may have additional security requirements that exempt the recorder from this requirement. Arrangements should be made with the certifying authorities in regard to such exemptions 

b. 
It is recommended that appropriate procedures are used to avoid the overwriting of data during aircraft maintenance following a reportable incident or accident.  

## Ii-2.1.8 Quality And Reliability Of Recording

a. 
For each newly installed system, the reliability of the system and quality of recorded data shall be established by analysis of data recorded on the ground and in flight.  
b. 
It is recommended that the relevant accident investigation authority should be invited by the certifying authority to participate in the assessment of new systems and the quality of the recorded data particularly where novel features exist (refer to paragraph II-2.1.6b). 

## Ii-2.1.9 Recording Capacity And Format

The equipment shall be capable of recording in digital format the data parameters specified in ANNEX II-A of this section as applicable to the particular class of recorder. Refer also to ANNEX II-C paragraph 6. 

## Ii-2.1.10 Means Of Functional Test

A means shall be provided for checking the recorder system for proper operation as required by the paragraph II-2.1.2 of this part and 2-4.2.1 of SECTION 2 (Generic Flight Recorder Requirements). 

## Ii-2.1.11 Means For Copying Recorded Data

Means shall be provided within the recording system to enable the aircraft operator to copy recorded data. The means for copying the data shall be readily accessible and shall not require the removal of the recorder from its location in the aircraft. Recorded data shall not be erased, re-written or altered during the process of copying. It is not required that the normal parameter recording function should continue during the process of copying.  

## Ii-2.1.12 Flight Crew Interface

Means should be provided to enable the flight crew to insert an event mark on the recording. 

 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Ii-2.1.13 Acceleration Sensors

For aircraft where the recording interval of acceleration parameters is equal to or longer than 0.125 s, the damping factor of the acceleration sensors shall be not less than 0.7 of critical damping and the total error in following a single triangular input of 
0.5 second duration or greater, shall be no more than 10% of the acceleration. The input/output ratio shall not vary by more than ± 3 dB when the sensor is subjected to a sinusoidal acceleration input within the range of 0-4 Hz. Above 4 Hz, the output signal shall decrease at not less than 6 dB per octave. For aircraft where the recording interval of acceleration parameters is shorter than 0.125 s, the damping factor of the acceleration sensors shall be not less than 0.7 of critical damping and the total error in following a single triangular input of 0.25 second duration or greater, shall be no more than 10% of the acceleration. The input/output ratio shall not vary by more than ± 3 dB when the sensor is subjected to a sinusoidal acceleration input within the range of 0-8 Hz. Above 8 Hz, the output signal shall decrease at not less than 6 dB per octave. Some of the attenuation shall be provided in the mechanical design of the sensor in order to avoid saturation by noise or high frequency inputs. Attenuation wholly provided by electrical filtering is not acceptable.  

## Ii-2.1.14 Recorder System Requirements

II-2.1.14.1 
Segregation of Mandatory, Non-Mandatory FDRs and Other Flight Recorders Where, in addition to the mandatory crash-protected recorder, a non-mandatory recorder is installed for maintenance or other purposes, the functions of the recorders shall be segregated in such a way that failures within the non-mandatory system do not affect the mandatory system.  
NOTE: 
It is permissible for both recorders to obtain their data from common sensors and a common data input buffer. However, software for the processing of parameters recorded by the mandatory flight data recorder should be segregated from the software for the processing of parameters for the maintenance recorder. This segregation will allow airlines to modify the software for maintenance recording functions without incurring re-certification effort for the mandatory recording functions. 

II-2.1.15 
Data Sampling, Recording and Retrieval Characteristics 
II-2.1.15.1 
General The flight recorder shall use a digital method of recording and storing the data and a method of readily retrieving that data from the recording medium without loss of parameter accuracy, resolution, samples or timing correlation. 

II-2.1.15.2 
Data Sampling Successive recorded values of each parameter shall be derived from new readings obtained from the input interface of the flight recorder system. The interval between these readings shall be that specified in the parameter tables within a tolerance of 1/64th of a second. Irrespective of parameter, successive readings of a parameter shall be recoverable in the sequence in which they were made. Where an input parameter has not been updated at the input interface since the previous reading, an indication of this should be recorded. 

II-2.1.15.3 
Data Measurement Range The measurement range for each parameter shall comply with at least the range defined in the tables of ANNEX II-A, Where a parameter changes its value over its full range within one sample period, the recorded values shall meet the specified resolution and other parameter recording requirements. Refer also to paragraph II-A.7. 

 

II-2.1.15.4 
Data Accuracy, Resolution and Timing a. 
Data shall be recorded so as to meet the accuracy, sampling rate, resolution and timing requirements as defined in the tables of ANNEX II-A. (Refer also to paragraphs 2-1.7 and II-3.2.2). 
b. 
Where data compression methods are used, parameter resolution and sampling rates shall be maintained irrespective of the values and variations of other parameters. 
c. 

Data shall be recorded so that relative timings between parameters can be deduced within a tolerance of 0.25 seconds (Refer also to paragraph II-6.2.3). 

NOTE: 
This tolerance should refer to the timing of actual events not acquisition time. 

## Chapter Ii-3 Minimum Performance Specification Under Standard Test Conditions Ii-3.1 Introduction

This chapter provides the minimum performance specification of the equipment and the levels to be demonstrated under standard test conditions. For the purposes of this chapter, standard test conditions are defined in documents EUROCAE ED-14G / RTCA DO-160G. "Environmental Conditions and Test Procedures for Airborne Equipment" or the revision level as agreed with the certification authority, paragraph 3.4 as: a. 

TEMPERATURE 
+15 to +35°C 

| b.    | RELATIVE HUMIDITY    | Not greater than 85%    |
|-------|----------------------|-------------------------|
| c.    | AMBIENT PRESSURE     | 84 to 107 kPa           |

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
In addition to the above, the AC electrical power supply should be within the limits specified as Normal in Section 16 of ED-14G / DO-160G or the revision level as agreed with the certification authority, and essentially free from modulation, ripple, interruptions and surges; the DC electrical supply should be within the limits specified as maximum and minimum in Section 16 of ED-14G / DO-160G or the revision level as agreed with the certification authority. Reference should be made also to CHAPTER II-4 for details of the tests to be performed under environmental test conditions. 

## Ii-3.2 Recorder Minimum Performance Levels

The recorder shall be designed to meet and be tested to show compliance with the following Minimum Performance Levels. 

NOTE: 
Where these paragraphs state requirements regarding the signal in the recording medium, it should be interpreted as that observed at the output of the data retrieval equipment specified by the equipment manufacturer. 

## Ii-3.2.1 Start-Up And Effects Of Power Interruptions

Following a system electrical power interruption the characteristic of the FDR recorder system shall be as described in the following table.  

 
Recording Requirement 
Power Interruption 
Interruption Duration 
Initial Power Level 
Cold Start 
>2s 
No Power 
Following initial application of power to the recorder system, the system shall be capable of recording information in the recording medium as soon as possible but no later than 10s. Any built-in test 
function shall be completed within 60s.  
Warm 
Restart 
Within 
200ms to 2s 
Normal, Abnormal, and 
Emergency 
For interruptions with a duration of 200ms to 2s, the recorder system shall recover and commence storing information, in the recorder medium, as soon as possible but no later than 500ms after power is restored. Any built-in test function shall 
recover within 10s [2].  
Transient 
0 to 200ms 
Normal 
Interruptions with a duration of 0 to 200ms shall have no effect on the recorder 
system. 

 The recording of data shall commence irrespective of the status of any data frame synchronization. The recorder shall be ready within the specified interval to record all parameters regardless of their availability. 

NOTE 1: 
 Where data compression is used, it is permissible to commence data recording with uncompressed data pending recovery of the compression algorithm, provided that recovery of all the data can be demonstrated. 

NOTE 2:   
Any built-in test function may take up to 10s to recover. The recovery period of 10s is intended to permit power-up test and system initialization routines to be performed. It is recommended that such routines should be performed as rapidly as possible to minimize the recovery period. 

## Ii-3.2.2 Recording Delay

The delay between the completion of the data acquisition process and the recording of the resulting data in the non-volatile crash-protected recording medium shall not exceed 0.5 seconds.  
NOTE: 
It is important to preserve all available data. For this reason, any delay should be minimised.  

## Ii-3.2.3 Data Retrieval

The organisation of the recording medium and the data record shall be such that: a. 
for an undamaged, fully serviceable recording medium with a normal recording, the data is readily retrievable. 
b. 
for an undamaged, fully serviceable recording medium with a corrupted record, the data can be retrieved, using special techniques if needed, for the periods i. 
ending one second maximum prior to the period of corruption and 
ii. 
commencing one second maximum after the period of corruption 
c. 
for a damaged or partially failed recording medium the available data can be retrieved (refer also to paragraph II-2.1.4) using special techniques if needed. 

## Minimum Performance Specification Under Environmental Test Conditions Ii-4.1 Introduction

Chapter 2-3 of this document defines the environmental tests to be performed on the recorder system. Compliance with the applicable performance requirements of this part for the Flight Data Recording System shall be demonstrated as shown in Table II-4.1. 

## Ii-4.2 Exceptions To General Requirements

There are no exceptions to the general requirements defined in paragraph 2-3.2 for parameter recording systems. 

MOPS PARAGRAPH NUMBER 
2-1.6 
2-1.7 
2-1.12 
II-3.2.1 
II-3.2.2 
ENVIRONMENT 
Test Reference 
Table 2-3.1 
NORMAL 
Power 
Recording 
OPERATION 
Bit Error Rate 
Timebase 
Stability 
Interruptions 
Delay 
Temperature 
1 
R 
 
R 
R 
R 
Altitude 
2 
R 
 
R 
R 
R 
Temp Variation 
3 
R 


Humidity 
4 
R 


Shock 
5 and 6 
R 
R 


Vibration 
7 
R/E 
R 


Power Input 
15 
R 


Voltage Spike 
16 
R 


AF Susceptibility 
17 
R 


Induced Susceptibility 
18 
R 


RF Susceptibility 
19 
R 


Lightning 
21 
R 


Key: Blank = Manufacturer's Discretion R = Test Required 
 

## Chapter Ii-5 Test Procedures Ii-5.1 Introduction

This chapter specifies the test procedures for demonstrating compliance with the requirements for data recovery, specified in CHAPTER II-3. Although specific test procedures are cited, it is recognised that they will not apply in all cases and that other methods may be preferred or required. Alternative methods may be used if the manufacturer can show that they provide equivalent certification data. 

## Ii-5.1.1 Adjustment Of Equipment

The equipment under test shall be properly aligned and adjusted in accordance with the manufacturer's recommendations. 

II-5.1.2 
Test Instrument Precautions 
Precautions shall be taken to prevent the introduction of errors resulting from impedance mismatch and the improper connection of test instruments to the equipment under test. 

II-5.1.3 
Test Conditions 
Where parts of the system use digital processing, the test procedures assume that interface conversion equipment appropriate to the recovery of the recorded information and which match the performance characteristics of the system to be certified, are used.  

II-5.1.4 
Warm-Up Period 
Unless otherwise specified, all tests shall be performed after a warm-up (stabilization) period of not less than 5 minutes and not more than 15 minutes. 

## Ii-5.1.5 Recording Of Test Results

The actual numerical values obtained for each of the parameters tested shall be recorded in a qualification test report. 

## Ii-5.2 Data Recovery Testing Ii-5.2.1 Scope

This chapter describes test methods which provide an acceptable means, but not the only means, of compliance with the requirements of paragraph II-3.2.3. Success criteria for the tests are given in paragraph II-3.2.3. 

## Ii-5.2.2 Background

Paragraph II-3.2.3 covers data retrieval, with or without data corruptions due to crash damage or other sources. The probability of achieving the required retrieval capability is affected by the recording medium organisation, the download or recovery process, and the use of data compression. Regardless of the source of the data corruption, it shall be possible to recover data preceding and following the corruption within the window defined in paragraph II-3.2.3. This test procedure assumes the use of ARINC 717 or similar data stream. Recorders using other data types can modify this procedure as necessary to demonstrate the same objectives. In the following test cases, certain operations may be combined as long as it can be shown that the test cases do not interfere with each other. 

 
The Data Stream tests require a controllable data source that can start, stop, and corrupt the data stream at specific repeatable points. A realistic data stream should be constructed in which the parameter dynamics are typical of the intended application and there is sufficient changing data to unambiguously identify the position in the stream. 

## Ii-5.2.3 Data Stream Startup

Apply power to the recorder, and after several seconds start the data stream at various points in the frame, including: 
 
within a sync word 

 
less than one word before a sync word 
Record at least 10 seconds of data after starting the stream. Then download the recorded data and show that data words can be recovered and interpreted up to the window defined in paragraph II-3.2.3b(ii). 

## Ii-5.2.4 Data Stream Stop

Begin recording a valid data stream, and after at least 10 seconds stop the data stream at various points in the frame, including: 
 
within a sync word 

 
less than one word before a sync word 
Then download the recorded data and show that data words can be recovered and interpreted up to the window defined in paragraph II-3.2.3b(i). 

## Ii-5.2.5 Data Stream Bit Dropout

Begin recording a valid data stream, and after at least 10 seconds introduce a bit dropout in the data stream at various points in the frame, including: 

 
within a sync word 
 
less than one word before a sync word 
Record at least 10 seconds of data after the dropout. Then download the recorded data and show that data words can be recovered and interpreted up to the window defined in paragraph II-3.2.3b(i) and (ii). 

## Ii-5.2.6 Data Stream Bit Error

Begin recording a valid data stream, and after at least 10 seconds introduce a bit error in the data stream at various points in the frame, including: 

 
within each sync word 
Record at least 10 seconds of data after the bit error. Then download the recorded data and show that data words can be recovered and interpreted up to the window defined in paragraph II-3.2.3b(i) and (ii). 

## Ii-5.2.7 File Corruption - Modified Word

After recording a valid data stream for at least 30 minutes, download an image of the recorded data. Then, before post processing the data file for interpretation, modify a word in the file at various critical points, including: 

 
sync words or frame headers 
 
file structures such as directories or page tables 
Then show that data words can be recovered by normal or special techniques up to the window defined in paragraph II-3.2.3b(i) and (ii). 


## Ii-5.2.8 File Corruption - Deleted Block

After recording a valid data stream for at least 30 minutes, download an image of the recorded data. Then, before post processing the data file for interpretation, delete a block of at least 512 words from the file at various critical points, including: 

 
sync words or frame headers 
 
file structures such as directories or page tables 
Then show that data words can be recovered by normal or special techniques up to the window defined in paragraph II-3.2.3b(i) and (ii). 

## Ii-5.2.9 Data Stream Interruption

After recording a valid data stream for at least 10 seconds, interrupt the data stream at various points in the frame, including: 

 
within a sync word 
 
less than one word before a sync word 
Resume the data stream after durations of: 
 
100 milliseconds 
 
900 milliseconds 
 
1100 milliseconds 
 
65 seconds 
Record at least 10 seconds of data after the resumption of the data stream. Then download the recorded data and show that the start time and duration of the interruption can be derived as in paragraph II-3.2.3. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter Ii-6 Equipment Installation And Installed Performance Ii-6.1 Introduction

This chapter specifies: - 

 
the FDR system specific installation characteristics and performance  
 
the procedures for verifying that performance when the system is installed in an aircraft. 
Installed performance criteria are generally the same as those contained in this part, which were verified through bench and environmental tests. However, certain performance parameters may be affected by the physical installation and can only be confirmed after installation. 

Typical flight recorder systems are illustrated in Figure II-6.1 and Figure II-6.2. 

## Ii-6.2 Equipment Installation Ii-6.2.1 Altitude And Airspeed Sensors

It is permissible to derive altitude and airspeed data from either of the pilots' instrument systems provided that the operation and integrity of the pilots' instruments are not impaired. Long extensions to the pitot-static system should be avoided. Where data for the flight recorder is derived from a separate pitot-static system, this system shall have accuracy equivalent to the pilots' systems over the full flight envelope of the aircraft. 

## Ii-6.2.2 Acceleration Sensors

Acceleration data shall be obtained from sensors which are rigidly attached, and located longitudinally either (i) in helicopters, within the approved centre of gravity limits, or (ii) in aeroplanes, within a distance forward or aft of the centre of gravity limits that does not exceed 25% of the aeroplane mean aerodynamic chord.  
NOTE: 
The acceleration sensors should be so mounted that they are not affected significantly by structural modes or vibration.  
The use of alternative sources of acceleration data, e.g. Inertial Reference Units, is not recommended particularly where the units are located outside the prescribed limits. Translation of such parameters involves many variables in a complex calculation where the algorithm depends on the location of the inertial reference unit relative to the particular aircraft centre of gravity. It would be difficult, if not impossible, to verify the algorithm for the accident environment. Furthermore, equipment interchangeability would be adversely affected. 

## Ii-6.2.3 Choice Of Sensors And Data Sources

As far as practicable, the flight recorder system should be connected to data sources within the aircraft such that: a. 
any data transport delay between the sensor and the recorder system i. 
is minimised (ideally to less than 0.25 seconds) and 
ii. 
can be deduced with reasonable certainty 
b. 
data, appropriate to each required parameter is supplied to the recorder system at a rate sufficient to prevent the data sample from being recorded more than once for that parameter (rate sufficient to meet the required sampling rate and avoid stale data) 
c. 
relative timings between all parameters, irrespective of their sources, can be deduced to within a tolerance of 0.25 seconds. 
Pre-existing on-board sensors should be used wherever possible, provided that their accuracy and resolution meet the requirements of ANNEX II-A. 

## Ii-6.3 Installation Calibration And Correlation Tests Ii-6.3.1 General

Proper functioning of a newly installed flight recorder system may be determined by a combination of ground and flight tests. The objectives of the flight test are to determine, where appropriate, the correlation between recorded data and cockpit displays and to demonstrate proper functioning of the system in the airborne environment. A schedule of tests should be prepared by the equipment installer. For the prototype installation, a comprehensive programme of tests should be performed, as described in paragraph II-6.3.4. For follow-on series installations, a limited flight test and data examination may suffice. 

## Ii-6.3.2 Installation Tests

Installation tests shall comprise ground and/or flight tests and will vary in extent dependent upon whether the installation is classed as initial or follow-on. Generally, each parameter shall be tested over its entire range of operation, the number of test points being dependent on the data source and how the source (data) is processed. The minimum number of test points is defined below. Required test points for a given parameter may be obtained by simulation, stimulation, ground test, flight test or a combination of these methods 

## Ii-6.3.3 Flight Testing

The flight test of the prototype installation should be planned to cover the full flight envelope. The schedule of tests should take account of the ground tests performed and include, where practicable, the following as appropriate to the aircraft and recorder system: a. 

Instrument readings and recordings made at intervals during the flight for the purpose of determining data correlation. 

b. 
Functioning of equipment and systems in all modes and over their full ranges to generate the various discretes and variable parameters to be recorded. 
c. 
Electrical power system switching to demonstrate recorder tolerance to transients and power interrupts. 
d. 
Operation of radio transmitters and heavy duty electrical equipment to demonstrate recorder immunity to interference. 
e. 
Flight into turbulence, manoeuvres to buffet and stalls to demonstrate recorder tolerance to vibration and acceleration. 

## Ii-6.3.4 Initial Fdr System Installation Ii-6.3.4.1 Ground Tests

The following tests shall be performed for certification of an initial FDR system installation. a. 
Insert definitive Documentary Data through the Flight Data Entry Panel, if installed, (or equivalent device, e.g.: flight-deck clock suitably configured and wired or an event marker switch) to identify commencement of tests. 
b. 
With the FDR system operating, perform a calibration check of all parameters and discretes. All sensors or transducers should be exercised over their effective range and all discretes exercised through their 'off'/'on' states. Specific test points should be recorded to enable replay to confirm values. 
c. 
Sensors which may not be practical to exercise or stimulate for the purpose of calibration tests (e.g. fuel flow, torque, EPR) may be simulated by appropriate test equipment. 
d. 
Each calibration point should be predetermined and tabulated on a calibration record sheet. The calculated value in bits for each calibration point should be shown on the record sheet and the test operator should enter the value indicated on the test set. A typical example of an entry on the calibration record is shown in Table II-6.1. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

e. 
Where the output of a sensor is indicated on flight-deck instruments and/or displays, the correlation between the indicated value and the predetermined calibration point should be established. 
f. 
Where a sensor output does not provide a flight-deck indication or where it 
results in an indication with resolution too low for correlation, (e.g. position of flight control surfaces, spoilers, airbrakes) angle-measuring devices such as clinometers should be used to set predetermined test points required for calibration. 
g. 
The number of correlation or test points for non-linear parameters shall be sufficient to precisely define the relationship between the recorded value and measured value over the full operating range of the parameter within the accuracy required by Table II-A.1 or Table II-A.2. The correlation between recorded and measured values for linear parameters can be established with three test points, one at the mid or null point and the others at each end point of the operating range. Test points should include upper, transition and lower values (e.g. left, zero and right lateral deviation) and should confirm test points 
denoting to, from, north, south, east, west, plus, minus, etc. For parameters derived from flight-deck controls having discrete detent positions (e.g. throttles, flaps), each detented position should be tested. 
h. 
Upon completion of ground test calibration and correlation testing, the FDR should be removed from the aircraft for data analysis. Alternatively, a suitable copy tape or download of the recording(s) should be obtained from the FDR in situ for subsequent playback assessment. 
i. 
To facilitate the assessment of all recorded data, the block of time allocated to ground testing may be suitably time-marked on the FDR such that the identification and assessment of the ground test data may be made later during the flight test data playback assessment. 

## Ii-6.3.4.2 Flight Tests

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
The flight test shall be performed after the ground test and while it should be of minimal duration, should nevertheless be of sufficient length to determine if there has been any degradation of the recorded data when compared with the ground correlation and calibration data and to validate all parameters that can only be exercised during the aircraft's in-flight (dynamic) condition. The certification flight test of the initial FDR installation shall include specific test points of all parameters and should cover a range of altitudes including maximum certificated altitude of the aircraft. The test schedule should include the following where practical with all test points registered by means of a suitable event marker: a. 

Instrument and/or electronic display readings and recordings made at intervals during the flight for the purpose of determining data correlation of the required parameters. 

b. 
Unless conducted through the ground test segment, functioning of the equipment and systems in all modes and over their full ranges to generate the various discretes and variable parameters to be recorded. 
c. 
Unless conducted through ground testing, electrical power switching to demonstrate FDR system tolerance to transients and power interruptions 
d. 
Operation of radio transmitters and electrical equipment (e.g. pumps, solenoids, motors, fans) to demonstrate FDR system immunity to electromagnetic interference. 
e. 
For non-solid state recorders, implementation of a flight profile to demonstrate FDR system tolerance to vibration and acceleration. 
f. 
At completion of testing, the FDR should be removed from the aircraft for playback assessment. Alternatively, a suitable copy tape or download of the recording(s) should be obtained from the FDR in situ for subsequent playback assessment. 
g. 
For the assessment the recorded data shall be converted to engineering units using the information contained in the certification document specified in 2-1.3.4(5). The assessment shall then be carried out using this engineering units data. 

## Ii-6.3.5 Follow-On Fdr System Installations Ii-6.3.5.1 Ground Tests

The following tests shall be performed for certification of follow-on installations of an FDR system: a. 
lnsert definitive Documentary Data through the Flight Data Entry Panel, if installed, (or equivalent device, e.g. flight-deck clock suitably configured and wired or an event marker switch) to identify commencement of tests. 
b. 
With the FDR system operating, perform a check of each parameter to obtain sufficient calibration and correlation data to demonstrate that the system performance conforms to that of the initial installation. It is acceptable to monitor 
and record a reduced number of parameter test points. For data derived from a digital bus, a minimum of two test points is required. For data derived from analogue sources, a minimum of three test points is required, typically to record extreme values and transition points and test points denoting to, from, north, south, east, west, plus, minus, etc. 
II-6.3.5.2 
Flight Tests 
Flight testing is not required for follow-on FDR installations. 

## Ii-6.3.6 Additional Parameters And Discretes

a. 
If new parameters or discrete signals are added to an existing FDR system, recertification testing is required. If the existing system can accommodate the change(s) without modification to FDR system components (e.g. if Flight Data Acquisition Unit (FDAU) software changes are not required), confirmation of satisfactory performance should be established by means of ground and flight 
testing of the *additional* FDR system inputs only, followed by a playback 
assessment in accordance with paragraph II-6.3.4f. If the new parameters or discretes are derived from existing aircraft systems and require additional wiring or modifications to existing cable assemblies, a test programme should be conducted to ensure that Electromagnetic Compatibility is maintained. 
NOTE: 
An assessment should be conducted to determine the need for retesting of existing FDR parameters to confirm continued 
acceptability. 
b. 
Where significant architectural and/or software changes result from the requirement to augment the list of parameters and/or discrete inputs to an FDR system, a re-certification of the system will be necessary with ground testing of all parameters and discretes required as for an initial installation as described in paragraph II-6.3.4.1. 
NOTE: 
The need for a flight test should also be assessed. 

## Ii-6.3.7 Documentation

a. 
A report prepared to comply with the requirements shall describe the FDR system installation and the equipment installed and shall contain a record of the results of all ground and flight tests, including calibrations and correlations. A copy of the actual ground and flight test data shall be retained by the installer and operator. 
b. 
For each follow-on installation, a copy of all ground calibration and correlation data shall be retained by the installer and operator. 
c. 
Any processing time delays between the FDR acquisition system input and FDR recording output shall be documented. 
d. 
To aid in the playback and analysis of the recorded data, the following information should also be documented and made available in electronic format: The following documentation fields are based on the ARINC 573/717 standards. 
When other standards are used an equivalent level of documentation shall be provided. 

 
Bits per Second 
 
Record Stream Format (e.g. ARINC 573, ARINC 717) 
 
Parameter Name 
 
Number of Bits Comprising Parameter (including sign bit) 
 
Location of Bits (bit(s) / word number / subframe / superframe as appropriate) 
 
Superframe Cycle Counter Name (if applicable) 
 
Superframe Cycle Counter Value (if applicable) 
 
Signed Parameter? (Yes/No) 
 
Location of Sign Bit (bit / word number / subframe / superframe as appropriate) 
 
Recording Range in engineering units 
 
Polynomial Coefficients for Parameter engineering unit conversion 
 
Look Up Table in tabular format (raw value versus engineering unit value) for parameters that do not have an equation 
 
Predefined Equation (e.g. ARINC synchro) 
 
Conversion Description  
 
Units (e.g. degrees, feet, knots) 
 
Parameter Sign Convention (e.g. positive values = aircraft nose-up) 
 
Discrete Interpretation (e.g. 1 = Engaged, 0 = Disengaged) 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
PITCH ATTITUDE: NUMBER 013: RATE 16 

| SELECTED CAL. POINT    | -10° DN    | -5° DN    | 0°      | +5° UP    | +10° UP    |
|------------------------|------------|-----------|---------|-----------|------------|
| REQUIRED VALUE         | 655-665    | 673-683   | 689-699 | 703-713   | 716-726    |
| TEST SET READING       |            |           |         |           |            |

## Annex Ii-A Definition Of Parameters To Be Recorded Ii-A.1 Parameter Tables

Table II-A.1 and Table II-A.2 provide details of parameter characteristics appropriate to flight recorders as defined in paragraph II-1.3.1. a. 
The parameter tables are based on those given in ICAO Annex 6. Parts I, II and III. Where possible, to aid comparison, the order of parameters within the tables corresponds with the ICAO tables.  
b. 
The choice of recorder class and the parameters to be recorded is the prerogative of the responsible regulatory agency. 
c. 
As installed in Table II-A.1 and Table II-A.2 means that when a parameter is used by the aircraft's systems, or required to operate the aircraft, the recording requirements shall meet but need not exceed the requirements for the operation 
of the aircraft. In cases where the aircraft systems do not use the data operationally, as installed means that the recording requirements should be the same as the actual sensor characteristics, as far as practicable. 
d. 
In order to accommodate variations in aircraft complexity certain parameters have been denoted with an asterisk. Parameters without an * shall be recorded regardless of aeroplane complexity. Those parameters designated by an * shall be recorded if an information source for the parameter is used by aircraft systems and/or flight crew to operate the aircraft. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

e. 
Where spare capacity exists, manufacturers and operators should be encouraged to use the space to increase sampling rates and/or resolution and/or to record additional parameters for operational use. Where practicable, spare input ports to the acquisition system should also be mapped to the data frame. 
f. 
The recommended characteristics reflect needs identified by accident investigators, but may not be practicable without significant modifications to existing designs. In addition recommended characteristics should meet but need not exceed the requirements for the operation of the aircraft.  

## Ii-A.2 Recording Format

When creating a data frame the following points should be considered: a. 
Certain parameters need to be recorded at equal time intervals to aid computer 
processing during accident analysis e.g. accelerations, attitude.  
b. 
Related parameters such as helicopter cyclic, collective and tail rotor positions should be stored in adjacent word locations. 
c. 
Engine related parameters should be recorded so as to provide continuity of data samples from each engine during the data frame period. Where recording capacity allows a significant number of engine parameters to be recorded, these should be arranged in groups to provide a snapshot of engine condition.  
d. 
Care shall be taken to avoid discrete word constructs which might be interpreted as synchronisation word values.  
e. 
If a parameter requires recording in two or more locations in an FDR frame or sub-frame to obtain the necessary range and resolution then care shall be taken to ensure that the derivation of its engineering value from the raw data is achieved without ambiguity. All constituent words shall be taken from the same sample of the source data, and should be recorded in the same sub-frame, with the least significant word being recorded earliest in the sub-frame. The transfer function, in terms of a mathematical equation shall be unique. 

## Ii-A.3 Recording Multi-Word Parameters

When splitting the value of a parameter is necessary, implementation of either one of the two options presented below will ensure proper reconstitution of original data. 1. 

If the original value of the parameter is split into two or more constituent words using a single acquisition and buffering of the data (allowing mapping of data into different words from a single sample), then all constituent words shall be recorded at the same rate as required for the parameter (e.g. pressure altitude recorded once per second). If parameter is divided into two words, both words shall be recorded at the required interval. The sample time for all constituent words shall be the same as the sample time of the original value of the parameter. For example, an 18-bit word (e.g. Longitude) could be divided into two parts as shown below (with and without overlap bits); both parts shall be recorded at the required parameter rate and their respective sample time shall be identical. 

| Sign                                                                        |   90 |   45 |   22.5 | 11.25 5.625 2.8125 1.406 0.703 0.352 0.176 0.088 0.044 0.022 0.011 0.0055 0.0027 0.0014   |
|-----------------------------------------------------------------------------|------|------|--------|-------------------------------------------------------------------------------------------|
| Bit weighting                                                               |      |      |        |                                                                                           |
| 18 bit longitude parameter                                                  |      |      |        |                                                                                           |
| Most Significant Word                                                       |      |      |        |                                                                                           |
| Sign                                                                        |   90 |   45 |   22.5 | 11.25 5.625 2.8125 1.406 0.703 0.352 0.176 0.088                                          |
| Least Significant Word                                                      |      |      |        |                                                                                           |
| 2.8125 1.406 0.703 0.352 0.176 0.088 0.044 0.022 0.011 0.0055 0.0027 0.0014 |      |      |        |                                                                                           |
| Overlapping Recording                                                       |      |      |        |                                                                                           |
| Sign                                                                        |   90 |   45 |   22.5 | 11.25 5.625                                                                               |
| Most Significant Word                                                       |      |      |        |                                                                                           |
| 2.8125 1.406 0.703 0.352 0.176 0.088 0.044 0.022 0.011 0.0055 0.0027 0.0014 |      |      |        |                                                                                           |
| Least Significant Word                                                      |      |      |        |                                                                                           |
| Non-Overlapping Recording                                                   |      |      |        |                                                                                           |

 

## Figure Ii-A.1: Eample Of Multi-Word Parameter

2. 
If buffering of the original parameter value is not possible or practical (e.g. coarse and fine signals available from transducers), then the most significant and least significant parts shall meet the following criteria: 
a) 
the resolution of the most significant part is at least 4 times lower than the maximum range of the least significant part and  
b) 
the maximum possible change in value of the original parameter (worse case scenario) over a time period equal to the recording rate of the most significant part, shall be less than the ¼ of the range of the least significant part (controls the required recording frequency of the most significant part and allows for occasional dropouts) 
c) 
the maximum possible change in value of the original parameter (worse case scenario) between two consecutive samples of the least significant part shall be less than ½ of the recording range of the least significant part 
Option 1 above is the preferred choice. For either option, where practicable, the least significant part should utilize all 12-bits of its assigned word and where practicable, the least significant and most significant parts should be sampled consecutively. 


## Ii-A.4 Recording Signed Parameters From Arinc 429 Words

II-A.4.1 
There are examples where the range of a parameter in the standard ARINC 429 format far exceeds that needed for normal operations. Some bits at the most significant end can be discarded. If the parameter is signed (i.e. can take positive and 
negative values), a common practice is to extract the sign bit and the required value bits and join them together, with the sign at the most significant position. This is not only unnecessarily complicated but leads to confusing behaviour if the chosen range is exceeded. As an example, consider pitch attitude, represented in the standard angular form with bit 29 as the sign, and to be recorded as a 12-bit word.  
II-A.4.2 
As an illustration, suppose that a range of ± 45 degrees is sufficient. A 12-bit word could be formed from bit 29 and bits 26 to 16, and provided the parameter remains within normal limits this will be quite satisfactory. But in two's complement notation the sign bit is repeated down into all value bits higher than those needed to represent the current parameter value. Thus it is possible, as an alternative method, to take bits 27 to 16 only using bit 27 as a sign bit and ignore bit 29. For pitch angles smaller than 45 degrees, in either sense, the form of the recorded word will be exactly the same as the form provided by the first method.  
II-A.4.3 
Now consider the overflow case. Suppose the angle increases to exactly +45 degrees. Using the first method, bits 26 to 16 will go to zero; bit 29 (the sign) will remain at zero. So the recorded word will be zero, and the displayed readout value will jump from maximum positive to mid-range. As the parameter value continues to increase, the (false) positive readout value will increase also. 
II-A.4.4 
Using the alternative method, when overflow occurs, bits 26 to 16 will go to zero and bit 27 will go to one. The recorded word will jump from the maximum positive value to the maximum negative value, and as the angle continues to increase the (false) negative readout value will decrease in magnitude. This is full-range positive-tonegative wraparound, and in cases of rapidly changing value is less likely to be misunderstood than a half-range jump. This alternative method of sign bit usage is preferred to the first method described.  

## Ii-A.5 Asymmetrically Signed Parameters

Signed parameters have been discussed in paragraph A-II.4 but with some parameters the signed ranges are asymmetric. There may be a large positive range but only a small negative range, e.g. altitude. If the value is treated as a simple two's 
complement signed number, such as would be extracted from an ARINC 429 word, nearly half the range will be wasted on impossible negative values which is wasteful of recording medium space. There are two ways of avoiding this: a. 
Add an offset equal to the maximum negative value before recording the parameter. This is then subtracted on data retrieval. The recorded value will then be unsigned. As an example, consider radio altitude; the range is from -20 to about +2600 feet. If a two's complement representation is used, a 12-bit word will give -2048 to +2047 ft for a count of 0 to 4095 at 1 ft resolution per count which is inadequate for the range required. With an offset added, zero could represent -20 ft. and the full range is easily accommodated with no loss of resolution. 
b. 
Record the signed parameter unchanged, but on data retrieval assume that values near the top of the recording range are negative. Using the radio altitude example again, the value can be tested against a suitable constant, say 4 000; if it is greater, subtract 4096. This gives a range of –95 to +4 000 feet at 1 ft resolution. 

## Ii-A.6 Parameter Characteristics

II-A.6.1 
Air Data and inertial data Altitude, airspeed and other air data parameters shall be obtained from the air data system used for the operation of the aircraft. Altitude, airspeed, pitch angle and roll angle displayed on each flight crew member primary flight displays shall be recorded. 

II-A.6.2 
Flight Control Systems It will be necessary to record, for each axis, both the pilot input and the control surface movements. Where the input controls for each pilot can be operated independently, both inputs shall be recorded. It is not required that all the input and surface movement parameters for a particular axis should be recorded at the specified sampling interval; the parameters, considered in combination, should satisfy the sampling interval requirement. In certain cases, a shorter sampling interval might be appropriate in order to provide a sufficient number of samples of the pilots' input controls. Interleaving shall not be permitted to meet the recording interval requirement. 

NOTE:  
The certifying authorities are likely to require at least 2 samples per second for each axis of each input control, although higher sampling rates may be deemed necessary to satisfy the requirements of any unique or novel systems.  
II-A.6.3 
Approach Aids It is not intended that data from multiple approach aid systems (such as ILS and MLS) should be recorded at the same time. The approach aid in use should be recorded. 

## Ii-A.6.4 Parameters Related To Electronic Displays Parameters Specific To Electronic Displays Are Included In Table Ii-A.1 And Table Ii-A.2.

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Ii-A.7 Recording Range

Reference in Table II-A.1 and Table II-A.2 to the term "full range" is to be interpreted as the operational range of the parameter appropriate to the aircraft in question (e.g. the total angular movement of a control surface) irrespective of the range available from the associated transducer or the magnitude of the word on a data-bus. A margin for abnormal conditions may need to be provided, e.g. excess speed. Refer also to paragraph II-2.1.15.3. 


## Ii-A.8 Recording Interval

The figure given for each parameter in Table II-A.1 and Table II-A.2 is the maximum time interval in seconds between two consecutive readings. The requirements relating to time correlation between sampling and recording are specified in paragraphs  
II-6.2.3, II-2.1.15.2, and II-2.1.15.4.c. 

## Ii-A.9 Recording Accuracy

The measurement accuracy for each parameter under static conditions shall be at least the accuracy in Table II-A.1 and Table II-A.2. Refer also to paragraph II-2.1.15.4. 

NOTE:  
For the purpose of understanding: 

x 
Static condition for a given parameter means that this parameter is experiencing no variation. 
x 
Normal dynamic condition for a given parameter means that this parameter is experiencing variation at a rate usually encountered 
during dynamic flight phases of normal operation (such as take-off, 
landing, go-around, normal turn, etc.) 
x 
Extremely dynamic condition for a given parameter means that this parameter is experiencing change at the maximum rate attainable, including the maximum rate of reversal. 
In this context, the term 'recording accuracy' refers to the correctness of the recorded data in relation to the physical value. The parameter accuracy applies only to the sensor through the recorded data and does not apply to items upstream of the sensor. In addition, the recording system from the sensor output through the recorded data shall contribute no more than half of the values stated in the accuracy column of the relevant parameter. When the sensor is provided for the sole purpose of producing a data source to the flight recorder system (e.g. tri-axial accelerometer) the accuracy referenced in the relevant parameter table will apply. When the data source used by the flight recorder system, also provides data to the aircraft's systems for the purpose of operating the aircraft, the required accuracy will default to the aircraft system (excluding the FDR system) with the most stringent accuracy requirement. Data shall be obtained from sources within the aircraft, which provide the most accurate and reliable information under both static and normal dynamic conditions. 

NOTE:  
The recorded information may be more accurate than the information displayed to the flight crew, which is displayed in real-time and is sometimes filtered in order to improve readability. In that case, this should be mentioned in the related parameter documentation.  
Filtering shall be avoided for parameters representing primary flight control positions and forces, position of the power levers and positions of primary flight surfaces, unless it can be demonstrated that: 

x 
the recorded values meet the accuracy requirements in extremely dynamic conditions, in spite of the filtering; or 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

x 
original sensor signal values can be reconstructed from filtered data recorded in extremely dynamic conditions, and this reconstructed values meet the accuracy requirements (see tables II-A.1 and II-A.2). The original sensor values shall be retrievable by applying a unique algorithm to the filtered values. This algorithm shall be a permanent part of the aircraft specific FDR system documentation package.  
NOTE 1:  
A definition of filtering is given in 1-1.5.1 
NOTE 2:  
An original sensor signal is the direct electronic output from a sensor or a system that accepts multiple sensor inputs.  
When the accuracy is given as a percentage, the percentage will apply to the operational range of the parameter as opposed to the full range of the sensor, which typically exceeds the operational range of the parameter. 


## Ii-A.10 Documentary Parameters

Provision may need to be made for the recording of documentary parameters which might be needed as an aid to data retrieval, conversion and analysis. For example, it might be necessary to include in the recording, parameters to identify airframe and system configuration including the software standard associated with data acquisition.  

## Ii-A.11 Recording Resolution

The resolution required for each parameter is listed in tables II-A-1 and II-A-2. Resolution typically refers to the value of the Least Significant Bit (LSB) as recorded by the system. This minimum resolution is what has been deemed sufficient to recreate the parameter across the required range using the available bits of the data word. The resolution should be such that it does not compromise the accuracy of the parameter (resolution should be an order of magnitude better than the required parameter accuracy). 

| Minimum Recording                                | Maximum recording                        |
|--------------------------------------------------|------------------------------------------|
| Recording Accuracy                               | Recording Resolution                     |
| N°                                               | Parameter                                |
| (refer to para II-A.9)                           | (refer to para II-A.11)                  |
| Remarks                                          |                                          |
| (refer to para II-A.7)                           | (refer to para II-A.8)                   |
| 1a                                               | Time                                     |
| r                                                |                                          |
| 0.125% per hour                                  |                                          |
| 1 second                                         | (a) UTC time preferred where available.  |
| or                                               |                                          |
| 1b                                               | Relative Time Count                      |
| r                                                |                                          |
| 0.125% per hour                                  |                                          |
|                                                  | (b) Counter increments each 4 seconds of |
| system operation.                                |                                          |
| 1c                                               | GPS Time Sync                            |
| are synchronised to GPS time                     |                                          |
| 1                                                | ±100 ft to ±700 ft                       |
| Refer to Table II-A.3                            |                                          |
| 2                                                | Pressure Altitude                        |
| maximum                                          |                                          |
| certificated altitude                            |                                          |
| of aircraft + 5 000 ft                           |                                          |
| 3                                                | Indicated Airspeed                       |
| r                                                |                                          |
| 5%                                               |                                          |
| 1 kt (0.5 kt                                     |                                          |
| recommended)                                     |                                          |
| or                                               |                                          |
| Calibrated Airspeed                              |                                          |
| 50 kt or minimum                                 |                                          |
| value from installed                             |                                          |
| pitot static system to                           |                                          |
| Max V                                            |                                          |
| S0                                               |                                          |
|                                                  |                                          |
|                                                  | Max V                                    |
| S0                                               |                                          |
| to 1.2 V                                         |                                          |
| D                                                |                                          |
|                                                  |                                          |
| r                                                |                                          |
| 3%                                               |                                          |
|                                                  |                                          |
| 4                                                | Heading                                  |
| (Primary flight crew reference)                  |                                          |
| 1                                                |                                          |
| r                                                |                                          |
| 2 degrees                                        |                                          |
| 0.5 degrees                                      | When true or magnetic heading can be     |
| selected as the primary heading reference, a     |                                          |
| discrete indicating selection shall be recorded. |                                          |
| and discrete 'true' or                           |                                          |
| 'mag'                                            |                                          |
| 0.004 g                                          |                                          |
| recommended)                                     |                                          |
| r                                                |                                          |
| 0.09 g excluding a                               |                                          |
| datum error of                                   |                                          |
| r                                                |                                          |
| 0.45 g                                           |                                          |
| 6                                                | Pitch Attitude                           |
| r                                                |                                          |
| 90 degrees                                       |                                          |
| 0.25                                             |                                          |
| r                                                |                                          |
| 2 degrees                                        |                                          |
| 0.5 degree                                       |                                          |
| Accuracy will apply only within                  |                                          |
| r                                                |                                          |
| 75° range                                        |                                          |
| Refer to paragraph II-A.6.1                      |                                          |

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

| 7                                                 | Roll Attitude                                  |
|---------------------------------------------------|------------------------------------------------|
| r                                                 |                                                |
| 180 degrees                                       |                                                |
| 0.25                                              |                                                |
| r                                                 |                                                |
| 2 degrees                                         |                                                |
| 0.5 degree                                        | For a new aircraft type, an analysis should be |
| performed by the aircraft manufacturer in         |                                                |
| order to assess if a shorter sampling interval is |                                                |
| necessary to capture quick attitude variations    |                                                |
| in a dynamic sequence.                            |                                                |
| Refer to paragraph II-A.6.1                       |                                                |
| 8                                                 | Manual Radio Transmission Keying               |
| and CVR/FDR synchronization                       |                                                |
| reference                                         |                                                |
| Discrete(s)                                       | 1                                              |
| discrete acceptable for all transmissions         |                                                |
| provided the CVR/FDR system complies with         |                                                |
| paragraph 2-1.11 of Section 2 (including          |                                                |
| ATC/SATCOM communications)                        |                                                |
|                                  |                                       | Minimum Recording    | Maximum recording    |
|----------------------------------|---------------------------------------|----------------------|----------------------|
| N°                               | Parameter                             | Range                | interval in seconds  |
| (refer to para II-A.7)           | (refer to para II-A.8)                |                      |                      |
| 9                                | Engine Thrust/power                   | Full range           | Each engine each     |
| second                           |                                       |                      |                      |
| 9a                               |                                       |                      |                      |
|                                  |                                       |                      |                      |
| Parameters required to determine |                                       |                      |                      |
| Propulsive Thrust/Power on each  |                                       |                      |                      |
| engine                           |                                       |                      |                      |
| 9b                               | Cockpit thrust / Power lever position | Full range           | Each lever each 0.5  |
| second                           |                                       |                      |                      |
| 10 *                             | Flaps                                 |                      | 2                    |
|                                  |                                       |                      |                      |
| 10a                              | Trailing edge flap position           | Full range or each   |                      |
| discrete position                |                                       |                      |                      |
| 10b                              | Cockpit control selection             |                      |                      |
| 11 *                             | Slats                                 |                      | 1                    |
|                                  |                                       |                      |                      |
| 11a                              | Leading edge flap (slat) position     | Full range or each   |                      |
| discrete position                |                                       |                      |                      |
| 11b                              | Cockpit control selection             |                      |                      |

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

| 12 *                                         | Thrust reverse status            | Turbo-jet - stowed,    |
|----------------------------------------------|----------------------------------|------------------------|
| in transit, reverse                          |                                  |                        |
| Each reverser each                           |                                  |                        |
| second                                       |                                  |                        |
|                                              |                                  | Turboprop - reverse    |
|                                              |                                  |                        |
|                                              | Turbo-prop - 1 discrete.         |                        |
| 13 *                                         | Ground spoiler and speed brake   | Full range or each     |
| discrete position                            |                                  |                        |
| 13a                                          | Ground Spoiler position          |                        |
| 0.5                                          |                                  |                        |
| r                                            |                                  |                        |
| 2% unless higher                             |                                  |                        |
| accuracy uniquely                            |                                  |                        |
| required                                     |                                  |                        |
| 13b                                          | Ground Spoiler selection         |                        |
| 13c                                          | Speed brake position             |                        |
| 13d                                          | Speed brake selection            |                        |
| 2                                            |                                  |                        |
| r                                            |                                  |                        |
| 2°C                                          |                                  |                        |
| 0.3°C                                        |                                  | 14                     |
| available sensor                             |                                  |                        |
| range                                        |                                  |                        |
| 15 *                                         | Autopilot/Autothrottle/AFCS mode |                        |
| and engagement status                        |                                  |                        |
| A suitable                                   |                                  |                        |
| combination of                               |                                  |                        |
| discretes                                    |                                  |                        |
| 1                                            | -                                | -                      |
| engaged and which primary modes are          |                                  |                        |
| controlling the flight path and speed of the |                                  |                        |
| aircraft                                     |                                  |                        |
| Recording Accuracy                            | Recording Resolution                           |
|-----------------------------------------------|------------------------------------------------|
| (refer to para II-A.9)                        | (refer to para II-A.11)                        |
| Remarks                                       |                                                |
| As installed                                  | 0.2% of full range                             |
| 1                                             |                                                |
| or                                            |                                                |
| Torque/Np as appropriate to the particular    |                                                |
| engine shall be recorded to determine power   |                                                |
| in both normal and reverse thrust. A margin   |                                                |
| for possible overspeed should be provided.    |                                                |
| 2% of full range or the                       |                                                |
| resolution required to                        |                                                |
| operate the aircraft                          |                                                |
| r                                             |                                                |
| 2% or sufficient to                           |                                                |
| determine any gated                           |                                                |
| position                                      |                                                |
|                                               |                                                |
| Parameter 9b shall be recorded for            |                                                |
| aeroplanes with non-mechanically linked       |                                                |
| cockpit-engine controls, otherwise            |                                                |
| recommended.                                  |                                                |
|                                               | Flap position and cockpit control, may each be |
| sampled at 4 second intervals so as to give a |                                                |
| data point each 2 seconds.                    |                                                |
| 0.5% of full range or                         |                                                |
| the resolution required                       |                                                |
| to operate the aircraft                       |                                                |
| r                                             |                                                |
| 3 degrees or as                               |                                                |
| pilot's indicator and                         |                                                |
| sufficient to determine                       |                                                |
| each discrete position                        |                                                |
|                                               | Left and right sides, or flap and cockpit      |
| control, may each be sampled at 2 second      |                                                |
| intervals so as to give a data point each     |                                                |
| second.                                       |                                                |
| 0.5% of full range or                         |                                                |
| the resolution required                       |                                                |
| to operate the aircraft                       |                                                |
| r                                             |                                                |
| 3 degrees or as                               |                                                |
| pilot's indicator and                         |                                                |
| sufficient to determine                       |                                                |
| each discrete position                        |                                                |
| -                                             | -                                              |
| be determined.                                |                                                |
|                                               |                                                |
| 0.2% of full range                            |                                                |
| Sufficient to determine use of the cockpit    |                                                |
| selector and the subsequent activation and    |                                                |
| positions of the surfaces.                    |                                                |
| 0.2% of full range                            |                                                |
|                                    |                                 | Minimum Recording    | Maximum recording    |
|------------------------------------|---------------------------------|----------------------|----------------------|
| N°                                 | Parameter                       | Range                | interval in seconds  |
| (refer to para II-A.7)             | (refer to para II-A.8)          |                      |                      |
| 16                                 | Longitudinal Acceleration (Body |                      |                      |
| axis)                              |                                 |                      |                      |
| r                                  |                                 |                      |                      |
| 1 g                                |                                 |                      |                      |
| 0.125 (0.0625                      |                                 |                      |                      |
| recommended)                       |                                 |                      |                      |
| 17                                 | Lateral Acceleration            |                      |                      |
| r                                  |                                 |                      |                      |
| 1 g                                |                                 |                      |                      |
| 0.125 (0.0625                      |                                 |                      |                      |
| recommended)                       |                                 |                      |                      |
| 18                                 | Primary Flight Control surface  | Full range           | (0.0625              |
| recommended)                       |                                 |                      |                      |
|                                    | and                             |                      |                      |
| Primary Flight Control pilot input | Full range                      |                      |                      |
|                                    |                                 |                      |                      |
| 18a                                | pitch axis                      | 0.125                |                      |
| 18b                                | roll axis                       | 0.125                |                      |
| 18c                                | yaw axis                        | 0.125                |                      |
| 19                                 | Pitch trim surface position     | Full range           | 1                    |
| r                                  |                                 |                      |                      |
| 3% unless higher                   |                                 |                      |                      |
| accuracy uniquely                  |                                 |                      |                      |
| required                           |                                 |                      |                      |
| 20 *                 | Radio Altitude               | - 20 ft to + 2500 ft    |   1  |
|----------------------|------------------------------|-------------------------|------|
| r                    |                              |                         |      |
| 2 ft or              |                              |                         |      |
| r                    |                              |                         |      |
| 3%                   |                              |                         |      |
| whichever is greater |                              |                         |      |
| below 500 ft and     |                              |                         |      |
| r                    |                              |                         |      |
| 5%                   |                              |                         |      |
| above 500 ft         |                              |                         |      |
| recommended          |                              |                         |      |
| 21 *                 | Vertical Beam deviation      |                         |   1  |
| 21a                  | ILS/GPS/GLS Glide Path       |                         |      |
| 21b                  | MLS Elevation                |                         |      |
| ±0.8 DDM or          |                              |                         |      |
| available sensor     |                              |                         |      |
| range as installed   |                              |                         |      |
| 21c                  | IRNAV/IAN Vertical Deviation |                         |      |
| 22 *                 | Horizontal Beam deviation    |                         |   1  |
| 22a                  | ILS/GPS/GLS Localizer        |                         |      |
| 22b                  | MLS Azimuth                  |                         |      |
| ±0.4 DDM or          |                              |                         |      |
| available sensor     |                              |                         |      |
| range as installed   |                              |                         |      |
| 22c                  | IRNAV/IAN Lateral Deviation  |                         |      |
|                      |                              |                         |      |
| 23                   | Marker beacon passage        | Discrete(s)             |   1  |
| Recording Accuracy                              | Recording Resolution         |
|-------------------------------------------------|------------------------------|
| (refer to para II-A.9)                          | (refer to para II-A.11)      |
| Remarks                                         |                              |
| 0.004 g                                         |                              |
| datum error of ±0.05 g                          |                              |
| 0.004 g                                         |                              |
| datum error of ±0.05 g                          |                              |
| 0.2% of full range or                           |                              |
| as installed                                    |                              |
| For multiple or split surfaces, a suitable      |                              |
| combination of inputs is acceptable in lieu of  |                              |
| recording each surface separately.              |                              |
| r                                               |                              |
| 2 degrees unless                                |                              |
| higher accuracy                                 |                              |
| uniquely required                               |                              |
| 0.2% of full range or                           |                              |
| as installed                                    |                              |
|                                                 |                              |
| For aeroplanes that have a flight control break |                              |
| away capability that allows either pilot to     |                              |
| operate the controls independently, record      |                              |
| both control inputs. The control inputs may be  |                              |
| sampled alternately to produce the sampling     |                              |
| interval                                        |                              |
| 0.3% of full range or                           |                              |
| as installed                                    |                              |
| Where dual surfaces are provided it is          |                              |
| permissible to record each surface alternately. |                              |
| 1 ft below 500 ft. 1 ft +                       |                              |
| 0.5% of full range                              |                              |
| above 500 ft                                    |                              |
| For autoland/category 3 operations, each        |                              |
| radio altimeter should be recorded, but         |                              |
| arranged so that at least one is recorded each  |                              |
| second. Radio Altitude can go negative          |                              |
| depending aircraft attitude and sensor          |                              |
| calibration                                     |                              |
| 0.3% of full range                              | Refer to paragraph II-A.6.3. |
| r                                               |                              |
| 3% recommended                                  |                              |
| For autoland/category 3 operations, each        |                              |
| system should be recorded but arranged so       |                              |
| that at least one is recorded each second       |                              |
|                                                 |                              |
| 0.3% of full range                              | Refer to paragraph II-A.6.3. |
| r                                               |                              |
| 3% recommended                                  |                              |
| For autoland/category 3 operations, each        |                              |
| system should be recorded but arranged so       |                              |
| that at least one is recorded each second.      |                              |
| Minimum Recording                              | Maximum recording        |
|------------------------------------------------|--------------------------|
| Recording Accuracy                             | Recording Resolution     |
| N°                                             | Parameter                |
| (refer to para II-A.9)                         | (refer to para II-A.11)  |
| Remarks                                        |                          |
| (refer to para II-A.7)                         | (refer to para II-A.8)   |
| 24                                             | Warnings                 |
| warning. The master warning and each 'red'     |                          |
| warning that can not be determined from other  |                          |
| parameters or from the cockpit voice recorder  |                          |
| shall be recorded. In addition each smoke      |                          |
| warning from others compartments such as:      |                          |
| lavatories, crew rest areas, etc. should be    |                          |
| recorded.                                      |                          |
| 25                                             | Each Navigation Receiver |
| Frequency Selection                            |                          |
| Sufficient to                                  |                          |
| determine selected                             |                          |
| frequency                                      |                          |
| 4                                              | As installed             |
| acceptable. The frequency to be recorded       |                          |
| should be that associated with the information |                          |
| displayed to the pilot.                        |                          |
| 26 *                                           | DME 1 and 2 Distances    |
|                                                |                          |
| (GLS)                                          |                          |
| As installed                                   |                          |
|                                                |                          |
| As installed                                   |                          |
| (IRNAV/IAN)                                    |                          |
| 27                                             | Air - ground status      |
| landing gear if installed                      |                          |
|                                                | (0.25 recommended)       |
| A suitable                                     |                          |
| combination of                                 |                          |
| discretes                                      |                          |
|                                                |                          |
| 28 *                                           | GPWS/TAWS/GCAS status    |
| 28a                                            |                          |
| Discretes                                      | 1                        |
| recorder capacity is limited in which case a   |                          |
| single discrete for all modes is acceptable    |                          |
| Selection of terrain display mode              |                          |
| including pop-up display status                |                          |

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

| 28b                                              | Terrain alerts, both cautions and    |
|--------------------------------------------------|--------------------------------------|
| warnings, and advisories                         |                                      |
| 28c                                              | On/off switch position               |
| 29 *                                             | Angle of attack                      |
| may be recorded at 1 second intervals so as      |                                      |
| to give a data point each half second. If the    |                                      |
| aircraft is equipped with a suitable data source |                                      |
| for this parameter the data shall be recorded    |                                      |
| 30 *                                             | Low pressure warning                 |
| 30a                                              | Hydraulic pressure                   |
| Discrete(s) or                                   |                                      |
| available sensor                                 |                                      |
| range                                            |                                      |
| 30b                                              | Pneumatic pressure                   |
| Minimum Recording                             | Maximum recording                                |
|-----------------------------------------------|--------------------------------------------------|
| Recording Accuracy                            | Recording Resolution                             |
| N°                                            | Parameter                                        |
| (refer to para II-A.9)                        | (refer to para II-A.11)                          |
| Remarks                                       |                                                  |
| (refer to para II-A.7)                        | (refer to para II-A.8)                           |
| 1 kt                                          |                                                  |
| obtained from the                             |                                                  |
| most accurate system                          |                                                  |
| 32 *                                          | Landing gear                                     |
| 32a                                           | Landing gear position                            |
| -                                             | -                                                |
| recorded to determine in transit, down and    |                                                  |
| lock, up and lock, as installed.              |                                                  |
| 32b                                           | Gear selector position                           |
| 33 *                                          | Navigation Data                                  |
|                                               |                                                  |
| Data should be                                |                                                  |
| obtained from the                             |                                                  |
| most accurate system                          |                                                  |
| as installed                                  |                                                  |
|                                               | The sampling timings of Wind speed and Wind      |
| Direction parameters should be sampled as     |                                                  |
| close as possible in time so that they can be |                                                  |
| correlated."                                  |                                                  |
| 33a                                           | Drift Angle                                      |
| 33b                                           | Wind Speed                                       |
| 33c                                           | Wind Direction                                   |
| 33d                                           | Latitude/Longitude                               |
| 33e                                           | GPS Correction in use                            |
| GPS correction. Actual correction data        |                                                  |
| recorded on ground                            |                                                  |
| 34 *                                          | Brakes                                           |
| r                                             |                                                  |
| 5 %                                           |                                                  |
| 2% of full range                              | To determine braking effort applied by pilots or |
| by autobrakes                                 |                                                  |
|                                               |                                                  |
| brake range                                   |                                                  |
|                                               |                                                  |
| range                                         |                                                  |

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

|                                                 |                                         | Minimum Recording    | Maximum recording       |
|-------------------------------------------------|-----------------------------------------|----------------------|-------------------------|
| N°                                              | Parameter                               | Range                | interval in seconds     |
| (refer to para II-A.7)                          | (refer to para II-A.8)                  |                      |                         |
| 35 *                                            | Additional Engine Parameters            | As installed         | Each Engine             |
| 35a                                             | EPR                                     | Each second          |                         |
| 35b                                             |                                         |                      |                         |
| 35c                                             |                                         |                      |                         |
| 35d                                             |                                         |                      |                         |
| 35e                                             |                                         |                      |                         |
| N                                               |                                         |                      |                         |
| 1                                               |                                         |                      |                         |
| indicated vibration level                       |                                         |                      |                         |
|                                                 |                                         |                      |                         |
| N                                               |                                         |                      |                         |
| 2                                               |                                         |                      |                         |
| EGT                                             |                                         |                      |                         |
| 35f                                             | fuel flow                               |                      |                         |
| 35g                                             |                                         |                      |                         |
| 35h                                             |                                         |                      |                         |
| 35i                                             |                                         |                      |                         |
| fuel cut-off lever position                     |                                         |                      |                         |
|                                                 |                                         |                      |                         |
| N                                               |                                         |                      |                         |
| 3                                               |                                         |                      |                         |
| engine fuel metering valve position             |                                         |                      |                         |
|                                                 |                                         |                      |                         |
| 36 *                                            | TCAS/ACAS (Traffic Alert and            |                      |                         |
| Collision Avoidance System)                     |                                         |                      |                         |
| Discretes                                       | 1                                       | As installed         |                         |
| recorded to determine sensitivity level and the |                                         |                      |                         |
| status of system, Combined Control, Vertical    |                                         |                      |                         |
| Control, Up Advisory, and Down Advisory (ref.   |                                         |                      |                         |
| ARINC).                                         |                                         |                      |                         |
| 37 *                                            | Windshear Warning                       | Discrete             | 1                       |
| 38 *                                            | Selected Barometric setting             |                      |                         |
| 38a                                             | Pilot                                   |                      |                         |
| As installed                                    | 64                                      | As installed         | 0.1 mb/0.01 in-Hg       |
| seconds is recommended. To be recorded for      |                                         |                      |                         |
| aeroplanes where electronic displays are fitted |                                         |                      |                         |
| 38b                                             | First Officer                           |                      |                         |
| 39 *                                            | Selected Altitude (All pilot selectable |                      |                         |
| modes of operation)                             |                                         |                      |                         |
| As installed                                    | 1                                       | As installed         | Sufficient to determine |
| flight crew selection                           |                                         |                      |                         |
| 40 *                                            | Selected Speed (All pilot selectable    |                      |                         |
| modes of operation)                             |                                         |                      |                         |
| As installed                                    | 1                                       | As installed         | Sufficient to determine |
| flight crew selection                           |                                         |                      |                         |
| 41 *                                            | Selected Mach (All pilot selectable     |                      |                         |
| modes of operation)                             |                                         |                      |                         |
| As installed                                    | 1                                       | As installed         | Sufficient to determine |
| flight crew selection                           |                                         |                      |                         |
| 42 *                                            | Selected Vertical Speed (All pilot      |                      |                         |
| selectable modes of operation)                  |                                         |                      |                         |
| As installed                                    | 1                                       | As installed         | Sufficient to determine |
| flight crew selection                           |                                         |                      |                         |
| 43 *                                            | Selected Heading (All pilot             |                      |                         |
| selectable modes of operation)                  |                                         |                      |                         |
| As installed                                    | 1                                       | As installed         | Sufficient to determine |
| flight crew selection                           |                                         |                      |                         |
|                                                 |                                         |                      |                         |
|                                                 |                                         |                      |                         |
| Recording Accuracy                          | Recording Resolution    |
|---------------------------------------------|-------------------------|
| (refer to para II-A.9)                      | (refer to para II-A.11) |
| Remarks                                     |                         |
| As installed                                | 2% of full range        |
| source for this parameter the data shall be |                         |
| recorded, if not already recorded in        |                         |
| parameters 9a or 9b                         |                         |
To be recorded for aeroplanes where electronic displays are fitted To be recorded for aeroplanes where electronic displays are fitted To be recorded for aeroplanes where electronic displays are fitted To be recorded for aeroplanes where electronic displays are fitted To be recorded for aeroplanes where electronic displays are fitted 
| Minimum Recording                                  | Maximum recording                    |
|----------------------------------------------------|--------------------------------------|
| Recording Accuracy                                 | Recording Resolution                 |
| N°                                                 | Parameter                            |
| (refer to para II-A.9)                             | (refer to para II-A.11)              |
| Remarks                                            |                                      |
| (refer to para II-A.7)                             | (refer to para II-A.8)               |
| 44 *                                               | Selected Flight Path (All pilot      |
| selectable modes of operation)                     |                                      |
|                                                    | 1                                    |
| electronic displays are fitted                     |                                      |
| 44a                                                | Course/DSTRK                         |
| 44b                                                | Path Angle                           |
| 44c                                                | Final Approach Path (IRNAV/IAN)      |
| identify the unique final approach path            |                                      |
| 45 *                                               | Selected Decision Height             |
| flight crew selection                              |                                      |
| To be recorded for aeroplanes where                |                                      |
| electronic displays are fitted                     |                                      |
| 46 *                                               | EFIS Display Format                  |
| 46a                                                | Pilot                                |
| Discrete(s)                                        | 4                                    |
| status e.g. off, normal, fail, composite, sector,  |                                      |
| plan, rose, nav aids, wxr, range, copy.            |                                      |
| 46b                                                | First Officer                        |
| 47 *                                               | Multi-function/Engine/Alerts Display |
| format                                             |                                      |
| Discrete(s)                                        | 4                                    |
| status e.g. off, normal, fail and the identity of  |                                      |
| display pages for emergency procedures,            |                                      |
| check lists. Information in checklists and         |                                      |
| procedures need not be recorded.                   |                                      |
| 48 *                                               | AC Electrical Bus Status             |
| 49 *                                               | DC Electrical Bus status             |
| 50 *                                               | Engine Bleed Valve Position          |
| determine the configuration of engine bleed        |                                      |
| valve                                              |                                      |
| 51 *                                               | APU Bleed Valve Position             |
| 52 *                                               | Computer Failure                     |
| 53 *                                               | Engine Thrust Command                |
| 54 *                                               | Engine Thrust Target                 |
| 55 *                                               | Computed Centre of Gravity           |
| 56 *                                               | Fuel Quantity in CG Trim Tank        |
| --```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`--- |                                      |
| 57 *                                               | Head up Display in use               |
| 58 *                                               | Para Visual Display on               |
| Minimum Recording                                 | Maximum recording                              |
|---------------------------------------------------|------------------------------------------------|
| Recording Accuracy                                | Recording Resolution                           |
| N°                                                | Parameter                                      |
| (refer to para II-A.9)                            | (refer to para II-A.11)                        |
| Remarks                                           |                                                |
| (refer to para II-A.7)                            | (refer to para II-A.8)                         |
| 59 *                                              | Operational Stall protection, Stick            |
| shaker and pusher activation                      |                                                |
| As installed                                      | 1                                              |
| determine activation                              |                                                |
| 60 *                                              | Primary Navigation System                      |
| Reference                                         |                                                |
| As installed                                      | 4                                              |
| determine the Primary Navigation System           |                                                |
| reference if more than one is available.          |                                                |
| GNSS, INS, VOR/DME, MLS, Loran                    |                                                |
| C, Localizer Glideslope                           |                                                |
| 61 *                                              | Ice Detection                                  |
| determine the status of each sensor               |                                                |
| As installed                                      | 1                                              |
| vibration                                         |                                                |
| As installed                                      | 1                                              |
| temperature                                       |                                                |
| As installed                                      | 1                                              |
| pressure low                                      |                                                |
| As installed                                      | 1                                              |
| speed                                             |                                                |
| 0.3% of full range                                |                                                |
| r                                                 |                                                |
| 3% Unless Higher                                  |                                                |
| Accuracy Uniquely                                 |                                                |
| Required                                          |                                                |
| 0.3% of full range                                |                                                |
| r                                                 |                                                |
| 3% Unless Higher                                  |                                                |
| Accuracy Uniquely                                 |                                                |
| Required                                          |                                                |
| 68 *                                              | Yaw or sideslip angle                          |
| r                                                 |                                                |
| 5%                                                |                                                |
| 0.5°                                              | For a new aircraft type, an analysis should be |
| performed by the aircraft manufacturer in         |                                                |
| order to assess if a shorter sampling interval is |                                                |
| necessary to capture quick attitude variations    |                                                |
| in a dynamic sequence.                            |                                                |
| Discretes                                         | 4                                              |
| selection                                         |                                                |
| 70 *                                              | Hydraulic Pressure (each system)               |
| r                                                 |                                                |
| 5%                                                |                                                |
| 100 psi                                           |                                                |
| 71 *                                              | Loss of cabin pressure                         |
| Minimum Recording                               | Maximum recording                       |
|-------------------------------------------------|-----------------------------------------|
| Recording Accuracy                              | Recording Resolution                    |
| N°                                              | Parameter                               |
| (refer to para II-A.9)                          | (refer to para II-A.11)                 |
| Remarks                                         |                                         |
| (refer to para II-A.7)                          | (refer to para II-A.8)                  |
| 72 *                                            | Cockpit trim control input position     |
| r                                               |                                         |
| 5%                                              |                                         |
| 0.2% of full range or                           |                                         |
| as installed                                    |                                         |
| Pitch                                           |                                         |
| When mechanical means for control inputs are    |                                         |
| not available cockpit display trim positions or |                                         |
| trim command should be recorded                 |                                         |
| 73 *                                            | Cockpit trim control input position     |
| r                                               |                                         |
| 5%                                              |                                         |
| 0.2% of full range or                           |                                         |
| as installed                                    |                                         |
| Roll                                            |                                         |
| When mechanical means for control inputs are    |                                         |
| not available cockpit display trim positions or |                                         |
| trim command should be recorded                 |                                         |
| 74 *                                            | Cockpit trim control input position     |
| r                                               |                                         |
| 5%                                              |                                         |
| 0.2% of full range or                           |                                         |
| as installed                                    |                                         |
| Yaw                                             |                                         |
| When mechanical means for control inputs are    |                                         |
| not available cockpit display trim positions or |                                         |
| trim command should be recorded                 |                                         |
| 75                                              | All cockpit flight control input forces |
| r                                               |                                         |
| 5%                                              |                                         |
|                                                 |                                         |
| 0.2% of full range or                           |                                         |
| as installed                                    |                                         |
| For fly-by-wire flight control systems, where   |                                         |
| control surface position is a function of the   |                                         |
| displacement of the control input device only,  |                                         |
| not necessary to record this parameter.         |                                         |
| 75a                                             | Control wheel - cockpit input forces    |
| r                                               |                                         |
| (±70 lbf)                                       |                                         |
|                                                 |                                         |
|                                                 |                                         |
|                                                 |                                         |
| r                                               |                                         |
| 378 N (± 85 lbf)                                |                                         |
|                                                 |                                         |
|                                                 |                                         |
|                                                 | 75b                                     |
| forces                                          |                                         |
| 75c                                             | Rudder pedal - cockpit input forces     |
| r                                               |                                         |
| 734 N (±165 lbf)                                |                                         |
|                                                 |                                         |
|                                                 |                                         |
|                                                 |                                         |
| 76 *                                            | Event Marker                            |
|                                                 |                                         |
|                                                 | From cockpit Switch                     |
| 77 *                                            | Date                                    |
|                                                 |                                         |
|                                                 |                                         |
| 78*                                             | ANP or EPE or EPU                       |
|                                                 |                                         |
|                                                 | Only required in data link environment. |
| Recording requirement is TBD                    |                                         |
| 1                                               | (refer to para II-A.3)                  |
| 40 000 ft                                       |                                         |
| recommended)                                    |                                         |
| 80*                                             | Aircraft computed weight                |
|                                                 |                                         |
| 1% of full range                                |                                         |
| 81*                                             |                                         |
|                                                 |                                         |
| 81a                                             | Full range                              |
|                                                 |                                         |
| 81b                                             | Full range                              |
|                                                 |                                         |
| 81c                                             | Right flight director pitch command     |
| 81d                                             | Right flight director roll command      |
|                                                 |                                         |
| Minimum Recording      | Maximum recording       |
|------------------------|-------------------------|
| Recording Accuracy     | Recording Resolution    |
| N°                     | Parameter               |
| (refer to para II-A.9) | (refer to para II-A.11) |
| Remarks                |                         |
| (refer to para II-A.7) | (refer to para II-A.8)  |
| 16 feet/min            |                         |
| feet/min               |                         |
| recommended)           |                         |
|                        |                         |
|                        |                         |
Maximum recording 
Recording Accuracy  
Recording Resolution 
interval in seconds 
N° 
Parameter 
Minimum Recording Range 
(refer to para II-A.7)  
(refer to para II-A.9)  
(refer to para II-A.11)  
REMARKS 
(refer to para II-A.8) 
1a or 
Time 
24 hours 
4 
± 0.125% per hour 
1 second 
(a) UTC time preferred where available. 
1b 
Relative Time Count 
0 to 4095 
4 
± 0.125% per hour 
 
(b) Counter increments every 4 seconds of system operation. 
5 ft 
Refer to paragraph II-A.6.1. 
1 
± 100 ft to ± 700 ft Refer to Table II-A.3 
2 
Pressure Altitude 
-1 000 ft to maximum certificated altitude of aircraft +5 000 ft 
1 
± 3% 
1 kt 
Refer to paragraph II-A.6.1. 
3 
Indicated Airspeed 
As the installed Pilot display measuring system 
4 
Heading 
360 degrees 
0.25 
± 2 degrees 
0.5 degree 
 
0.004 g 
 
5 
Normal Acceleration 
-3 g to +6 g 
0.125 
r0.09 g excluding a datum error of ±0.45 g 
6 
Pitch Attitude 
± 90 degrees 
0.25 
± 2 degrees 
0.5 degree 
 
7 
Roll Attitude 
± 180 degrees 
0.25 
± 2 degrees 
0.5 degree 
For a new aircraft type, an analysis should be performed by the aircraft manufacturer in order to assess if a shorter sampling interval is necessary to capture quick attitude variations in a dynamic sequence. 
8 
Manual Radio Transmission Keying and CVR/FDR synchronization reference 
Discrete(s) 
1 
- 
- 
Preferably each flight crew member but one discrete acceptable for all transmissions provided the system complies with paragraph 2-1.11 of Section 2 (including ATC/SATCOM communications) 
9 
Power on each engine 
Full range 
Each engine each second 
0-130% 
9a 
Free Power Turbine Speed 
(NF) 
As installed 
0.1% of full range 
Sufficient parameters e.g. Power Turbine Speed and engine torque should be recorded to enable engine power to be determined. A margin for possible overspeed should be provided. 
9b 
Engine Torque 
Full range 0-130% 
9c 
Engine Gas Generator Speed (Ng) 
2% of full range 
 
9d 
Cockpit Power Control position 
Full range or each discrete position 
Each control each 0.5 second 
± 2% or sufficient to determine any gated position 
10 10a 
Rotor Main rotor speed 50 to 130% 0.5 2% 0.3% of full range . 
10b 
Rotor brake 
Discrete 
1 
 
 
Where available 
Maximum recording 
Recording Accuracy  
Recording Resolution 
interval in seconds 
N° 
Parameter 
Minimum Recording Range 
(refer to para II-A.7)  
(refer to para II-A.9)  
(refer to para II-A.11)  
REMARKS 
(refer to para II-A.8) 
11 
Primary Flight Controls - Pilot input and/or* control output position 
0.5% of operating range 
11b 
Longitudinal cyclic pitch 
0.125 
11a 
Collective pitch 
Full range 
0.125 
± 3% unless higher accuracy is uniquely required 
 
(0.0625 recommended) 
 
 
* For helicopters that can demonstrate the capability of deriving either the control input or control movement (one from the other) for all modes of operation and flight regimes, the 'or' applies. For helicopters with non-mechanical control systems the 'and' applies. Refer to paragraph II-A.6.2. 
11c 
Lateral cyclic pitch 
0.125 
11d 
Tail rotor pedal 
0.125 
11e 
Controllable stabilator 
0.125 
11f 
Hydraulic selection 
Discrete(s) 
1 
- 
- 
12 
Hydraulics low pressure 
Discrete(s) 
1 
- 
- 
Each essential system should be recorded. 
2 
± 2°C 
0.3°C 
 
13 
Outside Air Temperature 
-50° to +90°C or available sensor range 
14 * 
AFCS mode and engagement status 
A suitable combination of discretes 
1 
- 
- 
Discretes should show which systems are engaged and which primary modes are controlling the flight path of the helicopter 
Discrete 
1 
- 
- 
 
15 * 
Stability augmentation system engagement 
16 * 
Main gearbox oil pressure 
As installed  
1 
As installed 
6.895 kN/m² (1 psi) 
 
17 * 
Gearbox oil temperature 
As installed 
2 
As installed 
1°C 


17a 
Main gearbox oil temperature 


17b 
Intermediate gearbox oil temperature 


17c 
Tail rotor gearbox oil temperature 
18 
Yaw rate 
± 400 degrees/second 
0.25 
± 1% 
2 degrees per second 
An equivalent yaw acceleration is an acceptable alternative. 
19 * 
Indicated sling load force 
0 to 200% of maximum certified load 
0.5 
± 3% of maximum certified load 
0.5% for maximum certified load 
With reasonable practicability if sling load indicator is installed. 
0.004 g 
 
20 
Longitudinal Acceleration (body axis) 
± 1 g 
0.25 
±0.015 g excluding a datum error of ±0.05 g 
0.004 g 
 
21 
Lateral Acceleration 
± 1 g 
0.25 
±0.015 g excluding a datum error of ±0.05 g 
Maximum recording 
Recording Accuracy  
Recording Resolution 
interval in seconds 
N° 
Parameter 
Minimum Recording Range 
(refer to para II-A.7)  
(refer to para II-A.9)  
(refer to para II-A.11)  
REMARKS 
(refer to para II-A.8) 
Radio Altitude can go negative depending aircraft attitude and sensor calibration 
1 ft below 500 ft, 1 ft + 0.5% of full range above 500 ft 
22 * 
Radio Altitude 
-20 ft to +2 500 ft 
0.25 
± 2 ft or ± 3% whichever is greater below 500 ft and ± 5% above 500 ft recommended 
0.3% of full range 
Refer to paragraph II-A.6.3. 
23 * 
Vertical beam deviation  
 
1 
As installed ± 3% recommended 


23a 
ILS/GPS Glide Path 
± 0.22 DDM or available sensor range as installed 
23b 
MLS Elevation 
+0.9 to +30 degrees 


0.3% of full range 
Refer to paragraph II-A.6.3. 
24 * 
Horizontal beam deviation 
 
1 
As installed. ± 3% recommended 


24a 
ILS/GPS Localizer 
± 0.22 DDM or available sensor 
range as installed 
24b 
MLS Azimuth 
± 62 degrees 


25 
Marker beacon passage 
Discrete 
1 
- 
- 
One discrete is acceptable for all markers. 
26 
Warnings 
Discretes 
1 
- 
- 
A discrete shall be recorded for the master warning, gearbox low oil pressure and SAS failure. Other 'red' warnings should be recorded where the warning condition cannot be determined from other parameters or from the cockpit voice recorder. 
27 
Each Navigation Receiver Frequency Selection 
Sufficient to determine selected frequency 
4 
As installed 
- 
An offset value or channel counter would be acceptable. The frequency to be recorded should be that associated with the information displayed to the pilot. 
28 * 
DME 1 and 2 Distances 
0-200 NM 
4 
As installed 
1 NM 
A sampling interval of 64 seconds is acceptable where other navigation parameters are recorded. 
 
 
29a 
Drift Angle 
 
4 
0.1 degree 
 
29 * 
Navigation Data 
As installed 
 
Data should be obtained from the most accurate system as installed 
29b 
Wind Speed 
 
4 
1 knot 
 
29c 
Wind Direction 
 
4 
1 degree 
 
29d 
Latitude/Longitude 
 
1 
0.0002 degree 
 
Maximum recording 
Recording Accuracy  
Recording Resolution 
interval in seconds 
N° 
Parameter 
Minimum Recording Range 
(refer to para II-A.7)  
(refer to para II-A.9)  
(refer to para II-A.11)  
REMARKS 
(refer to para II-A.8) 
Discrete(s) 
4 
- 
- 
Where installed. 
30 * 
Landing gear or gear selector position 
As installed 
1 
As installed 
 
 
31 * 
Engine exhaust gas temperature (T4) 
As installed 
4 


32 * 
Turbine inlet temperature (TIT/ITT) 
33 * 
Fuel contents 
As installed 
4 
As installed 
 
 
34 * 
Altitude rate 
As installed 
0.125 (0.0625 recommened) 
As installed 
 
Only necessary when available from cockpit instruments 
35 * 
Ice detection 
As installed 
4 
As installed 
 
A suitable combination of discretes to determine the status of each sensor 
As installed 
- 
As installed 
- 
 
36 * 36a 36b 36c 36d 36e 
Helicopter Health and Usage Monitor System (HUMS) Engine data Chip detectors Track timing Exceedance discretes Broadband average engine vibration 
37 
Engine control modes 
Discrete 
1 
As installed 
 
 
As installed  
64 
As installed 
0.1 mb/0.01 in-Hg 
Where practicable, a sampling interval of 4 seconds is recommended. To be recorded for helicopters where electronic displays are fitted 
38 * 38a 38b 
Selected Barometric setting Pilot First Officer 
As installed  
1 
As installed 
Sufficient to determine flight crew selection  
To be recorded for helicopters where electronic displays are fitted 
39 * 
Selected Altitude (All pilot selectable modes of operation) 
As installed  
1 
As installed 
Sufficient to determine flight crew selection 
To be recorded for helicopters where electronic displays are fitted 
40 * 
Selected Speed (All pilot selectable modes of operation) 
As installed 
1 
As installed 
Sufficient to determine flight crew selection 
To be recorded for helicopters where electronic displays are fitted 
41 * 
Selected Mach (All pilot selectable modes of operation) 
Maximum recording 
interval in seconds 
N° 
Parameter 
Minimum Recording Range 
(refer to para II-A.7)  
(refer to para II-A.8) 
As installed 
1 
As installed 
Sufficient to determine flight crew selection 
42 * 
Selected Vertical Speed (All pilot selectable modes of operation) 
As installed 
1 
As installed 
Sufficient to determine flight crew selection 
43 * 
Selected Heading (All pilot selectable modes of operation) 
 
1 
As installed 
 
To be recorded for helicopters where electronic displays are fitted 
44 * 
Selected Flight Path (All pilot selectable modes of operation) 
45 * 
Selected Decision Height 
As installed 
64 
As installed 
Sufficient to determine flight crew selection 
Discrete(s) 
4 
As installed 
- 
Discretes should show the display system 
status e.g. off, normal, fail, composite, sector, plan, rose, nav aids, wxr, range, copy. 
46 * 
46a 46b 
EFIS Display Format 
Pilot First Officer 
47 * 
Multi-function/Engine/Alerts Display format 
Discrete(s) 
4 
As installed 
- 
Discretes should show the display system status e.g. off, normal, fail and the identity of display pages for emergency procedures, check lists. Information in checklists and procedures need not be recorded. 
48 * 
Event Marker 
Discrete 
1 
 
 
From cockpit Switch 
GPWS/TAWS/GCAS status 
49* 49a 
Discretes 
1 
- 
- 
A suitable combination of discretes unless recorder capacity is limited in which case a single discrete for all modes is acceptable 
Selection of terrain display mode including pop-up display status 


49b 
Terrain alerts, both cautions and warnings, and advisories 
49c 
On/off switch position 


50* 
TCAS/ACAS (Traffic Alert and Collision Avoidance System) 
Discretes 
1 
As installed 
 
A suitable combination of discretes should be recorded to determine sensitivity level and the status of system, Combined Control, Vertical Control, Up Advisory, and Down Advisory (ref. ARINC). 
| Recording Accuracy                              | Recording Resolution    |
|-------------------------------------------------|-------------------------|
| (refer to para II-A.9)                          | (refer to para II-A.11) |
| REMARKS                                         |                         |
| To be recorded for helicopters where electronic |                         |
| displays are fitted                             |                         |
| To be recorded for helicopters where electronic |                         |
| displays are fitted                             |                         |
| To be recorded for helicopters where electronic |                         |
| displays are fitted                             |                         |
Maximum recording 
Recording Accuracy  
Recording Resolution 
interval in seconds 
N° 
Parameter 
Minimum Recording Range 
(refer to para II-A.7)  
(refer to para II-A.9)  
(refer to para II-A.11)  
REMARKS 
(refer to para II-A.8) 
 
0.125 (0.0625 recommended) 
51* 
Primary Flight Controls - Pilot input and/or* control output forces 
 
 
* For helicopters that can demonstrate the capability of deriving either the control input or control movement (one from the other) for all modes of operation and flight regimes, the 'or' applies. For helicopters with non-mechanical control systems the 'and' applies. Refer to paragraph II-A.6.2. 
0.5% of operating range  
51a 
Collective pitch forces 
Full range 
0.125 
± 3% unless higher accuracy is uniquely required 
 
0.125 


51b 
Longitudinal cyclic pitch forces 
51c 
Lateral cyclic pitch forces 
 
0.125 


51d 
Tail rotor pedal forces 
 
0.125 


52* 
Computed Centre of Gravity As installed 
64 
As installed 
1% of full range 
 
53* 
Helicopter computed weight As installed 
64 
As installed 
1% of full range 
 
 
|                 |       | Standard    | Equivalent Pressure Mercury    | Tolerance, Feet Plus or Minus    |
|-----------------|-------|-------------|--------------------------------|----------------------------------|
| Altitude (feet) | mm Hg | In Hg       | Room Temperature               | Low Temperature                  |
| -1 000          | 787.9 | 31.02       | 100                            | 150                              |
| -500            | 773.8 | 30.47       | 100                            | ---                              |
| 0               | 760.0 | 29.92       | 100                            | 150                              |
| 500             | 746.4 | 29.39       | 100                            | ---                              |
| 1 000           | 732.9 | 28.86       | 100                            | ---                              |
| 1 500           | 719.7 | 28.33       | 100                            | ---                              |
| 2 000           | 706.6 | 27.82       | 100                            | ---                              |
| 3 000           | 681.1 | 26.81       | 125                            | ---                              |
| 4 000           | 656.3 | 25.84       | 150                            | 210                              |
| 6 000           | 609.0 | 23.98       | 150                            | 250                              |
| 8 000           | 564.4 | 22.22       | 150                            | ---                              |
| 10 000          | 522.6 | 20.58       | 150                            | ---                              |
| 12 000          | 483.3 | 19.03       | 180                            | 350                              |
| 14 000          | 446.4 | 17.57       | 210                            | ---                              |
| 16 000          | 411.8 | 16.21       | 240                            | ---                              |
| 18 000          | 379.4 | 14.94       | 270                            | 450                              |
| 20 000          | 349.1 | 13.75       | 300                            | ---                              |
| 22 000          | 320.8 | 12.63       | 335                            | ---                              |
| 25 000          | 281.9 | 11.10       | 375                            | 560                              |
| 30 000          | 225.6 | 8.88        | 450                            | 600                              |
| 35 000          | 178.7 | 7.04        | 525                            | 730                              |
| 40 000          | 140.7 | 5.54        | 600                            | 800                              |
| 50 000          | 87.3  | 3.44        | 700                            | ---                              |
|                 |       |             |                                |                                  |
|                 |       |             |                                |                                  |

## Annex Ii-B Maintenance Practices Ii-B.1 General

II-B.1.1 
The maintenance practices contained in this annex are intended to ensure continued serviceability of flight data recorder systems and are intended as guidance for OEMs and flight data recorder system STC applicants in the creation of maintenance practices for their systems.   
II-B.1.2 
The maintenance tasks required to ensure the continued serviceability of the installed flight data recorder system will depend on the extent of the monitoring built into the recorder and its sensors. The system installer shall perform an analysis of the system to identify those parameters or parts of the system which are not monitored by any other airborne system and which, if defective, would not be readily apparent to the flight crew or maintenance personnel. Appropriate inspections and functional checks, 
together with the intervals at which these would need to be performed, shall be established as indicated by the analysis. These inspections and functional checks will include a validation of the whole measuring and processing channel from the sensor input through to re-conversion (to engineering units) of the recorded data. 
NOTE:  
In the analysis the following causes of improper operation of a parameter should be taken into account:  
x 
The dismantling and/or reassembling of some part of an aircraft may affect the adjustment of a sensor,  
x 
Any change to the interconnectivity between sensor and sampling equipment which may affect an analogue signal provided by the sensor (e.g. feeding the sensor output to other equipment),  
x 
The characteristics of some sensors and transducers are susceptible to drift. 
The analysis performed by the system installer will dictate which parameters should be verified using a correlation check. Attention should be given to the source and nature of the recorded signal, whether analogue or digital. Signals from a digital data bus (e.g. ARINC 429) that are identical to the signals utilized for the operation of the aircraft need not be verified via a correlation check; a reasonableness check that these digital signals are properly recorded will suffice. All other signals (analogue or digital) should be verified via a correlation check. A calibration check is required when the absolute accuracy of the recorded information is suspect or when the rigging of the sensor is disturbed. A scheduled calibration check is needed only for those parameters that are not identical to signals utilized for the operation of the aircraft and for which the accuracy cannot be established by a correlation check (for example, acceleration parameters when coming from a sensor dedicated to the FDR). A report on the analysis of the system should be prepared by the system installer and shall specify which check is appropriate for each of the recorded parameters (reasonableness, correlation, or calibration check). Refer to Table II-B.1 for an example of the differences between the three checks. The analysis report shall be made available to the operator for maintenance action purposes.  When a report is not prepared or not available, as a minimum, the maintenance procedures shall specify that a correlation check be carried out for all mandatory parameters in accordance with intervals in Table II-B.2. Correlation Check: The process of comparing data recorded by the flight data recorder against the corresponding data derived from flight instruments, indicators or the expected values obtained during specified portion(s) of a flight profile or during ground checks which are conducted for that purpose. Calibration: The process of establishing the relationship between the recorded raw data by the flight data recorder and the actual physical measurements of a parameter for the purpose of converting raw data to engineering units. 

Calibration Check: A check to determine the accuracy of a recorded parameter relative to a standard. Reasonableness Check: A subjective, qualitative evaluation requiring technical judgement of the recordings from a complete flight.  
NOTE:  
A reasonableness check is not a correlation check because quantitative assessment of some parameters may not be possible in terms of both magnitude and accuracy in the time domain, by inspecting data alone. A correlation check does not ensure the absolute accuracy of a recorded parameter whereas a calibration check does. 

|                                                      | Parameter: Pressure Altitude                       |
|------------------------------------------------------|----------------------------------------------------|
| Reasonableness check                                 |                                                    |
|                                                      |                                                    |
| Check that the pressure altitude values:             |                                                    |
|                                                      |                                                    |
| x                                                    |                                                    |
|                                                      | Correspond roughly to the airport altitude when on |
| ground                                               |                                                    |
|                                                      |                                                    |
| x                                                    |                                                    |
|                                                      | Increase when expected (climb phase after weight   |
| on wheel is released)                                |                                                    |
|                                                      |                                                    |
| x                                                    |                                                    |
|                                                      | Have values during the cruise phase consistent     |
| with the normal aircraft altitude and the operator   |                                                    |
| SOP (e.g. between 27000 and 45000 feet for a         |                                                    |
| turbo-jet)                                           |                                                    |
|                                                      |                                                    |
| Correlation check                                    |                                                    |
|                                                      |                                                    |
| x                                                    |                                                    |
|                                                      | Check that the pressure altitude value when on     |
| ground corresponds accurately to the airport         |                                                    |
| altitude corrected from the local QNH.               |                                                    |
| x                                                    |                                                    |
|                                                      | Check that the sequence of cruise values           |
| corresponds accurately to the flight level history   |                                                    |
| recorded by the crew for a given flight.             |                                                    |
|                                                      |                                                    |
| The difference between the FDR values and the values |                                                    |
| recorded or computed by an independent means for     |                                                    |
| comparison should not exceed the values specified by |                                                    |
| Table II-A.3.                                        |                                                    |
|                                                      |                                                    |
| Calibration check                                    |                                                    |
| x                                                    |                                                    |
|                                                      | Submit the static probe to various calibrated      |
| pressures which corresponds to a pressure altitude   |                                                    |
| ranging from the minimum to the highest altitude     |                                                    |
| attainable by the aircraft, with a 5000 ft step.     |                                                    |
x 
Check that the difference between the simulated pressure altitude and the recorded pressure altitude does not exceed the values specified by 
Table II-A.3. 

 
II-B.1.3 
The maintenance procedures shall specify that, when a reasonableness, correlation or calibration check is performed at the specified intervals of Table II-B.2, a copy of the complete/full download of the recordings shall be made. A whole flight should be transcribed graphically such that all parameter samples can be resolved. All mandatory parameters recorded should be expressed in engineering units. Inspection of parameters should reveal defects or noise in the measuring and processing chains and indicate necessary maintenance actions. When applicable, each mandatory parameter should be checked for different values of its operational range. For this purpose, some parameters should be inspected at different flight phases. The operator shall retain the most recent copy of the complete download. 
II-B.1.4 
Maintenance procedures shall specify that sensor calibration data be retained by the aircraft operator and be available when required by the accident investigation authorities. 
II-B.1.5 
Maintenance procedures shall take account of any inspection or test requirements specified by equipment manufacturers (e.g. battery checks of the underwater locator beacon). 
II-B.1.6 
Maintenance and flight crew procedures should emphasise the need to preserve the 
recording following a reportable occurrence. 
II-B.1.7 
Flight data recorder systems should be considered unserviceable if the recording duration is less than required, if there is a significant period of poor quality data or if one or more of the mandatory parameters is not recorded correctly. 

## Ii-B.2 Typical Maintenance Tasks

Table II-B.2 shows the primary maintenance tasks for the installed flight data recorder system. Inspection periods should be established on the basis of the system analysis referred to in paragraph II-B.1.2. 

|                                                    |                                                                             | ITEM                                                                       | INTERVAL                                                      | TASK              |
|----------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------|-------------------|
| Flight                                             | Data                                                                        | Recorder                                                                   | Pre-flight                                                    | Check for no-fail |
| System                                             |                                                                             |                                                                            |                                                               |                   |
|                                                    | One year, or up to a maximum of two                                         |                                                                            |                                                               |                   |
| years if approval from the appropriate             |                                                                             |                                                                            |                                                               |                   |
| regulatory authority has been obtained             |                                                                             |                                                                            |                                                               |                   |
| for                                                | FDR                                                                         | systems                                                                    | that                                                          | have              |
| demonstrated                                       | high                                                                        | integrity                                                                  | of                                                            |                   |
| serviceability self-monitoring                     |                                                                             |                                                                            |                                                               |                   |
|                                                    |                                                                             |                                                                            |                                                               |                   |
| Download and analyse at least a whole              |                                                                             |                                                                            |                                                               |                   |
| flight recording. Perform a correlation            |                                                                             |                                                                            |                                                               |                   |
| check, a reasonableness check, or a                |                                                                             |                                                                            |                                                               |                   |
| combination of both based on the                   |                                                                             |                                                                            |                                                               |                   |
| analysis described in II-B.1.2. When the           |                                                                             |                                                                            |                                                               |                   |
| analysis report is not prepared or not             |                                                                             |                                                                            |                                                               |                   |
| available, as a minimum, a correlation             |                                                                             |                                                                            |                                                               |                   |
| check shall be executed. Check all                 |                                                                             |                                                                            |                                                               |                   |
| mandatory parameters. When either                  |                                                                             |                                                                            |                                                               |                   |
| check indicates an anomaly, corrective             |                                                                             |                                                                            |                                                               |                   |
| action shall be initiated.                         |                                                                             |                                                                            |                                                               |                   |
| Perform scheduled calibration check for            |                                                                             |                                                                            |                                                               |                   |
| the                                                | mandatory                                                                   | parameters                                                                 | as                                                            |                   |
|                                                    | At intervals determined by the analysis                                     |                                                                            |                                                               |                   |
| of the system (refer to paragraph II-              |                                                                             |                                                                            |                                                               |                   |
| B.1.2) or at a minimum of 15000 hours              |                                                                             |                                                                            |                                                               |                   |
| or 60 months, whichever comes first.               |                                                                             |                                                                            |                                                               |                   |
| determined by the analysis of the                  |                                                                             |                                                                            |                                                               |                   |
| system for which the accuracy cannot               |                                                                             |                                                                            |                                                               |                   |
| be established by other means (refer to            |                                                                             |                                                                            |                                                               |                   |
| paragraph II-B.1.2).  When the check               |                                                                             |                                                                            |                                                               |                   |
| indicates an anomaly, corrective action            |                                                                             |                                                                            |                                                               |                   |
| shall be initiated.                                |                                                                             |                                                                            |                                                               |                   |
| Flight Data Recorder                               | As specified by equipment manufacturer. Remove recorders for bench check in |                                                                            |                                                               |                   |
| accordance                                         | with                                                                        | m                                                                          | anufacturer's                                                 |                   |
| instructions.                                      |                                                                             |                                                                            |                                                               |                   |
| --```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`--- |                                                                             |                                                                            |                                                               |                   |
|                                                    | As specified by equipment manufacturer. Remove for check of crash/ fire     |                                                                            |                                                               |                   |
| protection features                                |                                                                             |                                                                            |                                                               |                   |
| Accelerometers                                     | or                                                                          | FDR                                                                        | As specified by equipment manufacturer. Test for calibration. |                   |
| dedicated sensors                                  |                                                                             |                                                                            |                                                               |                   |
| Underwater                                         | locator/Radio                                                               | As specified by equipment manufacturer. Check serviceability of beacon and |                                                               |                   |
| Location Beacons                                   | battery.                                                                    |                                                                            |                                                               |                   |
|                                                    |                                                                             |                                                                            |                                                               |                   |

## Annex Ii-C Data Compression Ii-C.1 General

Data compression is used in order that the recording medium capacity requirement of a recorder may be reduced. For accident data recorders, compression techniques should be carefully designed so that discontinuities of the data stream or data corruption do not prevent retrieval of the data from the recording medium. It should be noted that it is relatively straightforward in existing magnetic tape recorders to retrieve data terminating immediately prior to a period of corruption and recommencing immediately after the period of corruption. For recorders with solid-state memory, with or without data compression, the objective should be to achieve an equivalent level of data retrieval. The following guidelines supplement CHAPTER II-3 and cover some of the features that an acceptable form of data compression would incorporate. 

These features are not all inclusive and are not intended to limit the application of new technology or techniques. The following paragraphs illustrate the type of features which are important to the retrieval of accident data. Specific data compression methods shall be evaluated on their ability to meet the intent of these key features. 

## Ii-C.2 Data Retrieval

All forms of data compression should be fully reversible. For reconstituted (or decompressed) data, it shall be demonstrated that there is no degradation or loss of accuracy, resolution, sample rates or timing correlation of the data when compared to the original input data. 

## Ii-C.3 Compression Characteristics

The following are considered to be desirable features of any compression technique. 

II-C.3.1 
Synchronisation A unique synchronisation bit pattern should be recorded at intervals not exceeding 4 seconds. 
II-C.3.2 
Reference Condition Where a compression technique records a variation from a reference condition, that reference condition should be recorded at pre-determined intervals of 300 seconds or less and within 16 seconds of recovery from each power interruption (refer also to paragraph II-3.2.1). Reference conditions should define the actual data value with full resolution and accuracy. 

II-C.3.3 
Variable Length Frame Synchronisation When variable length frames are used, a technique should be employed which provides a positive indication of each frame length e.g. a count of the number of bits between synchronisation patterns. 

II-C.3.4 
Data and Recording Medium Organisation To comply with paragraph II-2.1.4c the organisation of the data in the recording medium shall minimise the loss of data in the event of memory device failure or damage. Should this loss occur during normal operation, the event should be indicated in the recorder BITE output. The memory devices should be reconfigured automatically where this is practicable. 


## Ii-C.4 Data Compression Of Discrete Parameters

There are various means of data compression; many of them using the principle that a new value of each parameter will be recorded only when there is a significant change. The definition of a significant change varies between parameters; if the threshold is taken as zero counts, any change at all will cause a new value to be recorded, and the data will be fully recoverable. Clearly this will be the case with discrete words, but for some parameters a fairly large threshold which takes account of the required resolution will not cause any important loss of information. If the traditional approach is retained, that is to use 10-bit words with a pair of discrete values in the least significant positions, the data compression technique can be applied to the full 12 bit word only if a threshold of zero is used. Otherwise, changes in the discrete states will be lost. This means that the 10-bit parameter value will have also a zero threshold, which may be inappropriate. Alternatively, the data compression algorithms may distinguish between different word lengths, but this will make them more complex. A possible solution is to put the discretes at the most significant end of the word; then any discrete change will be seen as a large value change, and any suitable threshold can be chosen for the 10 bit word. In a software-controlled system there is no need to retain 10 and 12-bit words: it is reasonable to use as many bits as necessary for the required resolution and fill the top positions with discretes. 

## Ii-C.5 Effect Of Defective Sensors

The compression algorithm will become Inefficient when a defective sensor (e.g. a worn position transducer) generates a noisy signal. Recording of the particular parameter will require additional recording medium thus reducing the total recording time available. The possibility of noisy signals should be taken into account when the recording medium size is determined. 

## Ii-C.6 Determination Of Recording Capacity Requirements

When using data compression, the required capacity, of the recording medium for a given recording duration, is a function of the total number of parameters, their characteristics and the flight environment. Since these factors will be unknown until a system is defined and installed in an aircraft, the equipment manufacturer will be unable to declare compliance with the recording duration requirement, e.g. 10 hours or 25 hours. At the time of equipment certification (e.g. TSO), the equipment manufacturer will be able to estimate the recording capacity required on the basis of laboratory tests using suitable specimen data sets. This estimate can be used as a declaration to the certifying authority to obtain a conditional certification for the equipment. Following installation of the equipment in an aircraft, it will be necessary to verify that the required recording duration is achieved for the particular set of parameters recorded. This verification will require a series of flights to be made and the recordings to be checked. The certifying authority may permit these verification flights to be performed by the airline during normal revenue service. Subsequent to any revision to the recorded parameters definition, e.g. addition of nonmandatory parameters by the airline, further validation flights will be necessary to ensure compliance with the minimum recording duration requirements. In some cases, it may be acceptable to obtain unrestricted equipment certification by demonstrating adequate recording duration in the laboratory, using suitable data sets provided that the data sets fully represent both the parameter characteristics (e.g. range, sampling rates, resolution) and the flight characteristics of the aircraft in which the recorder will be installed. Further flight testing may be unnecessary. 


## Ii-C.7 Effect Of Defective Memory Devices

If the recorder is fully operational, then retrieved data shall meet the applicable parameter requirements for accuracy, resolution, sample rates, error rates and timing correlation when compared with the identical input data to the recorder. 

If the recorder has a single defective memory device (including the most critical device), then the comments in paragraph II-2.1.4c shall apply and the unaffected data shall meet the applicable parameter requirements for accuracy, resolution, sample rates, error rates and timing correlation when compared with the identical input data to the recorder. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Annex Ii-D Electronic Documentation Standard Ii-D.1 Background

Because FDR system documentation is necessary for the recovery of FDR information, the progress of an investigation can be significantly hindered if there are any delays in recovering the recorded information. This will not only delay determination of the cause, but also slow down the identification of critical safety issues. FDR system documentation is currently maintained in a variety of electronic and hard copy formats that are often incomplete or difficult to interpret. This problem has been compounded in recent years as the number of parameters for newly manufactured aircraft has risen from hundreds to more than a thousand. 

## Ii-D.2 Requirements

A standard for the documentation of flight recorder systems shall be used. The documentation for this standard shall: a. 
exist in an electronic format that is readily accessible and capable of presentation in a printed or screen-readable form. Sufficient information on the standard shall be made available so that replay system developers can incorporate an import function in to their own systems. 
b. 
be capable of being updated by the operator. 
NOTE: 
This documentation is not meant to replace the system descriptions that manufacturers currently produce. These normally contain much greater information about the system that is of use to investigators. 
In addition, for aircraft with a recording system architecture that readily supports file transfer protocols, the documentation shall be stored in the FDR crash-protected recording medium and automatically refreshed as needed. The file may be compressed using an industry standard lossless algorithm. The documentation shall be stored in a memory space segregated from those allocated for recording. For aircraft with a recording system architecture that does not support file transfer protocols, the same documentation shall be provided to the aircraft accident investigative body of the country in which the aircraft is registered. 

## Ii-D.3 Requirement For Fdr System Documentation Standard

An Electronic Documentation Standard (EDS) shall be used to store the definition of the data to be recorded by the FDR into the crash-protected recording medium. The EDS shall fulfil the following characteristics: a. 

The standard shall have a General Public License policy i.e. shall be available to everyone without patent, copyright or intellectual property issues. 

b. 
To allow complete and thorough description of the data recorded on the FDR the standard shall describe a generic database structure, which includes facilities to describe complex system data without the need to provide auxiliary data (graphics, descriptions) separately from the data recorded in crashprotected recording medium. 
c. 
The standard shall include means to allow configuration control of recording format history, recording form and recording data. 
Refer also to paragraph II-6.3.7.d. 

 

## Ii-D.4 Example Of An Electronic Documentation Standard

The ARINC 647A FRED (Flight Recorder Electronic Documentation) format qualifies as an international standard for documenting the content and format of information retained in FDRs. The FRED format 647A is a standard for the documentation that a ground station needs to recover the data. The ARINC FRED format 647A - Flight Recorder Electronic Documentation has been designed and developed to provide a standardized format for maintaining and conveying FDR system documentation. This standard format supersedes an older electronic format, the Flight Recorder Configuration Standard, Document TP13140E.  

## Part Iii Image Recorder Systems Chapter Iii-1 Introduction Iii-1.1 Purpose

This part defines the minimum specification to be met for all aircraft required to carry an Image Recording System for the purposes of the investigation of a reportable accident, or incident. It is applicable to crash-protected recorders, ancillary equipment and their installation in civil aircraft. This part shall be read in conjunction with Sections 1 and 2, together with Sections 3, 4 and 5 as applicable. 

## Iii-1.1.1 Description Of Content

This Part is divided into 6 Chapters. CHAPTER III-1 describes the typical equipment application and operational objectives of airborne image recording systems. CHAPTER III-2 establishes the minimum system performance requirements for the image recording systems. CHAPTER III-3 defines the minimum performance specification of the equipment and the levels to be demonstrated under standard test conditions. CHAPTER III-4 defines the minimum performance specification of the equipment and the levels to be demonstrated under environmental test conditions. CHAPTER III-5 specifies tests and procedures for determining compliance with the performance requirements and for demonstrating crash survival capability. CHAPTER III-6 defines the installation characteristics and performance with procedures for verifying that performance when installed in an aircraft. 

## Iii-1.2 Scope

Accident investigators have recognised for many years that recorded 'images' of the cockpit environment were needed to augment existing data and audio recordings. However, it has only recently become economically realistic to record cockpit images in a crash-protected recording medium. Therefore, supplementing existing data and audio recorder information with an image recording of the cockpit environment is the next logical step in the evolution of flight recorder systems. The combination of audio, data and cockpit image recordings will provide air safety investigators with the necessary information to better define the facts, conditions and circumstances of an occurrence, and to broaden the scope of the vitally important human factor aspects of investigations. Additionally, image recordings can capture other cockpit information that would otherwise be impractical or impossible to record. Flight Data Recorders (FDR) and Cockpit Voice Recorders (CVR) have provided accident investigators with detailed information on aircraft performance, operation of aircraft systems and to a limited degree flight crew activity. Vital information regarding the cockpit environment, non-verbal flight crew communications, flight crew workload, instrument display selections and status has not been available on traditional data and audio recorders. This has limited the scope of many investigations, but more importantly, has hindered the identification of safety issues and consequently the corrective action needed to prevent future occurrences. In several high profile accident investigations, despite the availability of state of the art flight data and cockpit voice recorder systems, the official findings of the investigation have generated considerable controversial debate reducing the time and energy that could have been better used on safety improvements. Accident investigators believe that image recording in the cockpit will substantially assist in confirming findings thereby allowing government and industry to focus on important safety issues rather than prolonged debate of the basic factual information. 

 
A general view of the cockpit area and instrument and control panel displays would enhance the understanding of an occurrence by providing valuable insight into the cockpit environment, serviceability of displays and instruments, flight crew activity, and the human/machine interface. 

Some operators have installed video cameras for operational purposes. These systems can provide the flight crew with images such as the external views of the undercarriage area, wings and engines, or internal views of cargo and cabin areas. Since these video images have the potential of influencing critical operational decisions, the images presented to the flight crew should be stored in crash-protected recording medium to facilitate accident investigation. Cameras installed for such purposes do not need to meet the requirements of this specification. In some instances it will be practical to use image recordings of sufficient resolution to record information that is not readily available to the FDR or CVR (e.g. secondary displays, flight crew selections, data link messages or weather radar). However, it is always preferable to record parametric data explicitly on the FDR rather than use an image recording, as FDRs provide a more accurate and useable recording. The use of image recordings is considered an acceptable means of compliance when it is the only practical means of recording explicit parametric data that would otherwise not be available to the FDR or CVR. Use of image recordings to capture data link messages is permissible. Therefore, the fundamental need for image recording for accident investigation is to augment existing flight and audio data by capturing images of the cockpit to better understand the cockpit environment, flight crew interactions and the overall human/machine interface. An additional benefit is the ability to capture information that is otherwise impractical to explicitly record on an FDR or CVR. In some older or smaller aircraft, where either no data recorders are required or equipping the aircraft with sensors to capture explicit parametric data could be prohibitively expensive, an image recorder could provide a low cost solution. This would be the only acceptable instance where the image recorder would be the primary source of parametric data. 

## Iii-1.3 Application Iii-1.3.1 Image Recording

Compliance with this Part will ensure that Airborne Image Recording systems will perform their function under the conditions encountered in aircraft operations. 

## Iii-1.4 Description Of System Iii-1.4.1 Equipment

The word "equipment" as used in this document includes all components and units on the aircraft necessary for the Image recording system to properly perform its intended functions. The equipment may include: a. 

Single or multiple Cameras/Image Sources 

b. 
Image communication network 
c. 
Image processing unit 
d. 
Crash-protected Image recording unit 
It should not be inferred from this example that each recording equipment design will necessarily include all the foregoing components or units. This will depend on the specific design chosen by the manufacturer. 


## Iii-1.4.2 Classes Of Recorder

For the purposes of this MOPS, Image Recorders are classified by "Class" as follows.  

## Table Iii-1: Classes Of Recorder

| 1.1.1.1.1.1.1                                                       | Class                                                                   | Image Recording System Purpose                      |
|---------------------------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------|
| A                                                                   | Required to capture data supplemental to conventional flight recorders. |                                                     |
| For example, to capture cockpit Human Factors, movements etc.       |                                                                         |                                                     |
| B                                                                   | Would satisfy data link Message Display Recording.                      |                                                     |
| C                                                                   | As a means for recording flight data where it is not practical or       |                                                     |
| prohibitively expensive to record on an FDR, or where an FDR is not |                                                                         |                                                     |
| required.                                                           |                                                                         |                                                     |
| D                                                                   | Required to capture Heads Up Display.                                   |                                                     |
| E                                                                   | Required to capture Other Camera Images presented to the Flight         |                                                     |
| Crew                                                                |                                                                         |                                                     |
| For example                                                         | -                                                                       | To capture cargo or cabin views, as selected in the |
| cockpit, which may be achieved by directly recording the images     |                                                                         |                                                     |
| presented to the flight crew, or indirectly using a camera.         |                                                                         |                                                     |

It may be that one camera can satisfy several requirements or that several cameras are necessary to satisfy one requirement. Except for Class E, where multiple sources are used to provide a certain class of recorded information, the images shall be recorded so that relative timings between them can be deduced within a tolerance of 0.25 second.  
NOTE: 
For the type D HUD recorder the display is usually collimated to infinity and the camera should be focussed similarly. 

## Iii-1.4.3 Operational Considerations

a. 

Objectives The following coverage areas are not necessarily related to the number of cameras required to obtain the information. It may be that one camera can satisfy several requirements or that several cameras are necessary to satisfy one requirement. Each aircraft will need to be assessed on an individual basis to identify the need for an appropriate number of dedicated image sensors to sufficiently capture the information described in sub-paragraphs i and ii. A coverage area is intended to reflect the field of view required to be captured by single or multiple image sensors. These coverage areas are further defined in paragraph III-1.4.1. 

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

| i.                                              | General Cockpit Area                              |
|-------------------------------------------------|---------------------------------------------------|
| Coverage areas                                  |                                                   |
|                                                 | All flight crew stations work areas including     |
| instruments and controls                        |                                                   |
| Purpose                                         |                                                   |
|                                                 |                                                   |
|                                                 | Ambient conditions in the cockpit (smoke, fire,   |
| lighting, etc.);                                |                                                   |
|                                                 | General flight crew activities such as use of     |
| checklists, charts, etc, and health and well-   |                                                   |
| being of flight crew;                           |                                                   |
|                                                 | Non-verbal communications (hand signals,          |
| pointing, etc.);                                |                                                   |
|                                                 | Cockpit selections within flight crew reach while |
| seated at duty station  (switch/throttle/flight |                                                   |
| controls, etc).                                 |                                                   |
| Resolution                                      |                                                   |
|                                                 |                                                   |
| displays and ambient conditions;                |                                                   |
| Frame Recording Rate                            |                                                   |
| Sufficient to determine significant flight crew |                                                   |
| actions.                                        |                                                   |
| Colour                                          |                                                   |
|                                                 |                                                   |
| ii.                                             | Instruments and Control Panels:                   |
| Coverage Area                                   |                                                   |
|                                                 | Forward Instrument Panel, Overhead Panel,         |
| Centre Pedestal and video displays presented    |                                                   |
| to the flight crew (where installed).           |                                                   |
| Purpose                                         |                                                   |
|                                                 |                                                   |
|                                                  | Information (including flight crew selections) not    |
|--------------------------------------------------|-------------------------------------------------------|
| explicitly recorded on the Flight Data Recorder; |                                                       |
|                                                  | Status of instrument displays and display             |
| modes (blank screen, partial display, automatic  |                                                       |
| display mode changes, etc.);                     |                                                       |
| Resolution                                       |                                                       |
|                                                  |                                                       |
|                                                  | Determine                                             |
| operational mode of the displays                 |                                                       |
|                                                  | Determine parameter values whose recording            |
| requirements can only be met by image            |                                                       |
| recording.                                       |                                                       |
| Frame Recording Rate                             |                                                       |
| The Update Rate will be per paragraph III-2.2.8. |                                                       |
| Colour                                           |                                                       |
|                                                  |                                                       |
|                                                  |                                                       |

b. 

Flight Crew Privacy Issues Misuse and privacy issues with respect to recorded voices, images and to some extent data, remain of significant concern to the aviation community. Use of audio and image recordings for reasons other than aviation safety, can do a disservice to the community as well as harm individuals. When taken out of context, images of the cockpit have the potential to mislead inexperienced people by virtue of their readily understandable format. They will also tend to have a high media appeal for sensationalist purposes and higher potential to be viewed out of context, all of which can be detrimental to an investigation and the parties involved. Privacy issues generally increase in sensitivity when information contains personal and/or emotional elements. This is the primary reason why audio recordings are considered privileged by most investigation authorities and international standards.  
It is the intent of investigators to obtain information with respect to flight crew interaction, the human/machine interface and information that is otherwise impractical to record on the FDR. It is therefore not necessary to record the total image of the flight crew. While accident investigators recognise and share the privacy and misuse concerns, the need to record the image of the general cockpit environment is nonetheless considered fundamental. In order to prevent unauthorised access to image recordings, gain further acceptance by the aviation community, and minimise the potential for misuse, it is required that: a. 

Recorded images may be used only for accident investigation purposes and shall not be publicly disclosed. To ensure that the AIR is not used for purposes other than investigation, the investigative authority shall retain custody of the AIR recording; 

b. 
Provisions shall be made for a flight crew operated post flight bulk erase function. Playback of image recordings by unauthorised persons shall be inhibited through the use of suitable protection mechanisms (refer to paragraph III-2.2.7). 
c. 
Start and Termination of Recording Recorder operation shall be as defined in paragraph 2-1.5. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter Iii-2 General Design Specification Iii-2.1 General Iii-2.1.1 General

This chapter is applicable to the functions of a flight recorder system designed to receive, process, record and preserve image information in accordance with the requirements of this MOPS. These functions shall be performed reliably even under adverse operating conditions including events leading to an accident. This section shall be read in conjunction with Section 2, which defines the requirements that are generic to all flight recorders. 

## Iii-2.2 Image Recorder Iii-2.2.1 General

The Image Recording System shall not, under normal or fault conditions, impair the airworthiness of the aircraft in which it is installed. Except for small parts that would not contribute significantly to the propagation of a fire, all materials used shall be self-extinguishing. The operation of Image Recording System controls intended for use during flight, in all possible positions, combinations and sequences, shall not result in a condition whose presence or continuation would be detrimental to the continued performance of the equipment. Controls that are not intended to be adjusted in flight shall not be readily accessible to flight personnel.  

## Iii-2.2.2 Recording Techniques

The recorder shall use a digital method of recording and storing the data. 

## Iii-2.2.3 Digital Recording And Retrieval Characteristics

The recorded information shall be readily retrievable from the memory to an industry standard digital format without loss of quality, or timing correlation irrespective of the recording format. The organisation of the memory and the recording shall be such that: 
a. 

for undamaged, fully serviceable memory with a normal recording, the recorded information is readily available 

b. 
for damaged or partially failed memory, the available information can be retrieved using special techniques, as required. 
c. 
The organization of the memory shall contain provisions to detect corruptions in the recording or retrieval, or data losses due to medium management. These provisions could include time stamps, sequence numbers, and block checksums. 

## Iii-2.2.4 Recorder Synchronisation

The recordings on the Image Recorder shall be synchronised to other airborne recordings as defined in paragraph 2-1.11. 

## Iii-2.2.5 Recording Capacity And Format

The equipment shall be capable of recording and storing the required information for the period applicable to the class of recorder. 

 

## Iii-2.2.6 Image Compression

Image Compression techniques may be used to minimise the amount of recording medium dedicated to Image recording. The loss of one image (frame or equivalent) shall not result in the loss of adjacent images. 

It shall be possible to reconstruct the images from the information stored in the crashprotected medium. Under normal replay conditions the images shall be available both as a real time flow of images, and one image at a time. The Image compression techniques may generate limited artefacts or loss of details. These shall not preclude the overall system from meeting the requirements of paragraphs III-1.4.3a i and III-1.4.3a ii. 

## Iii-2.2.7 Image Security/Encryption

One suitable means of compliance to address the privacy and security concerns in paragraph III-1.4.3b is the provision of a dual password/encryption key protection capability for Image Playback Systems such that both passwords are required to playback a recording.  Official investigation authorities may have access to specialised playback capability that does not require the use of these Passwords/Encryption keys. 

NOTE: 
It is envisioned that the passwords will be delegated to the airline and its pilot representative. 

## Iii-2.2.8 Minimum Required Update Rates

Images from each sensor(s), as installed, shall be updated with the following rates as a minimum: 

Minimum Update Rate 
Information 
 
Recording Period 
Class 
Description 
 
 
A 
General Cockpit View 
4 per second 
 
B 
CPDLC Message Display 
1 per second 
 
C 
Cockpit Displays 
4 per second 
 
D 
HUD Display 
4 per second 
 
E 
Other 
Camera 
Images 
 
when presented to the flight crew  
1 per second, or the rate provided to the flight crew, whichever is lower  

## Iii-2.2.9 Privacy Of Recorded Images

To respect flight crew privacy, cockpit area views shall be designed as far as practical to exclude the head and shoulders of flight crew members whilst seated in their normal operating positions.  

## Iii-2.2.10 Means Of Replay

The means of replay, which will be provided by the manufacturer, shall produce image data in an industry standard format. If the data has been encrypted it shall be decrypted. Replaying of the recording shall not damage, alter or erase the recording. Replaying or downloading of the recorded images shall require the removal of the recorder from its location in the aircraft. The documentation necessary to reproduce the images shall be made available. 

 

## Iii-2.2.11 Bulk Erase

After use of a bulk erase function, the recording shall be modified so that it cannot be retrieved using any and all normal replay (refer to note 2) or copying techniques. For a solid-state memory, an acceptable means of compliance would be for a bulk erase function to delete that information needed to access the memory by the normal replay procedure. The probability of inadvertent activation of a bulk erase function shall be minimised both in design of the recorder and by ensuring that the bulk erase function, when installed, is wired so that it requires at least two other sets of logic to be satisfied. Wherever practicable, the parking brake should be one of the sets of logic. In addition, the probability of an inadvertent activation of a bulk erase function during an accident shall also be minimised. 

NOTE 1: 
In the event of bulk erasure, non-normal replay or copying techniques may be used by the accident investigation authority to retrieve data, if available, for the purposes of conducting an official investigation. 

NOTE 2: 
Normal replay is data retrieval at the equipment level as used in the laboratories of aircraft constructors and modifiers to support certification of recorder installations. 
NOTE 3: 
Non-normal replay is data retrieval from the recording medium media using special techniques available to the recorder manufacturers and/or accident investigation authorities for dealing with severely damaged recorders. 
NOTE 4: 
It is understood that military organisations may use commercial recorders. In this case, they may have additional security requirements that exempt the recorder from this requirement. Arrangements should be made with the certifying authorities in regard to such exemptions 

## Iii-2.2.12 Maintenance Access

The installed system shall allow a loopback real time monitor function for test purposes and alignment. 

NOTE: 
The current image(s) from the system may be displayed on command. This should not allow the display of recorded images. 

## Iii-2.3 Camera Specifications Iii-2.3.1 General

There shall be no requirements for flight crew intervention during normal operation. 

## Iii-2.3.2 Beating Effects

For those Image Recording Systems where data is to be retrieved from electronic Instrument Displays, beating effects should be minimised. 

## Iii-2.3.3 Optical Characteristics

III-2.3.3.1 
Spatial Resolution 
Spatial resolution of the images shall be verified by differentiation of resolution lines presented for the appropriate information class. For Class A, B and C images, the resolution as shown in Table III-3.1 should be used. 

III-2.3.3.2 
Depth of field 
Depth of field shall be sufficient for the Class of Image Recording as shown in Table III-3.1. 

NOTE: 
For a Class B or C Recorder, the required depth of field shall encompass the instrument panel from furthest instruments to nearest instruments. For a Class A Recorder, the required depth of field should be as large as possible to accurately focus all movement in the cockpit.  

III-2.3.3.3 
Field of View 
Field of View shall be sufficient for the Class of Image Recording as shown in Table III-3.1.  

III-2.3.3.4 
Contrast 
The level of contrast shall be adequate to differentiate between the lines presented on the Test Chart as appropriate for the Class of Image Recording as shown in Table III-3.1. 

III-2.3.3.5 
Distortion 
Distortion of the Image shall be minimised in order to allow for differentiation between the lines presented on the Test Chart as appropriate for the Class of Image Recording as shown in Table III-3.1. 

III-2.3.3.6 
Digital Artefacts 
The level of artefacts introduced by the digitisation and compression systems shall not compromise the required resolution of the Image System as shown in Table III-3.1. 

## Iii-2.3.4 Spectral Bandwidth

The objective of the General Cockpit View or Instrument panels is to faithfully record the cockpit environment as experienced by or presented to the flight crew. The wavelengths of light sensed should be conformed to the spectral sensitivity of the human eye as closely as practicable.  
NOTE: 
The eye is generally taken to have a range from 410 nm to 710 nm (at these wavelengths the eye is approximately 1/400 as sensitive as at 560 nm, which is the most sensitive wavelength) 

## Iii-2.3.5 Lighting And Sensitivity

The Image sensor shall not require supplemental lighting during normal operation. The cockpit Image System shall be capable of operating in lighting conditions from 86 000 lux (full sun) to an illumination of 1.0 lux, by automatic means, and for Class B & C Image Systems shall be capable of resolving data from instruments with a luminance of 1.71 +/- 0.85 nits.  

## Iii-2.3.6 Dynamic Range

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
The image sensor shall accommodate a dynamic range of lighting of at least 10:1 between the brightest and darkest elements in a single image while providing the resolution, contrast, and depth of colour performance specified herein. 

## Iii-2.3.7 Depth Of Colour

Where a colour image is required, the depth of colour shall be no less than 256 colours, distributed across the visual bandwidth. 

## Iii-2.3.8 Electrical Interfaces

The interface shall be an accepted industry standard and non-proprietary. 

## Iii-2.4 Recorder Specifications Iii-2.4.1 Recording Duration

The duration is defined by regulation or operational requirements. Where an image recorder is used in lieu of a DLR or FDR application its duration shall be that of the DLR or FDR requirement.   

## Iii-2.4.2 Recording Medium Segregation And Partitioning

Recording medium shall be segregated such that the failure of a single memory device does not lead to the loss of more than 16 seconds of contiguous images. 

## Iii-2.4.3 Databus Selection

The databus interface chosen for the recorder shall, as a minimum, support the amount and frequency of Images required to be recorded in accordance with design requirements of these MOPS. 

## Iii-2.4.4 Recording Delay

The delay between the completion of the acquisition of the image at the image sensor, and the time the image is presented to the input of the recorder shall not exceed 2 seconds. The delay in recording the data, from the time that the image is presented at the input of the recorder to the time this data is stored in the crash-protected medium, shall be minimised, and shall not exceed 1 second. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter Iii-3 Minimum Performance Specifications Under Standard Test Conditions Iii-3.1 Introduction

This chapter specifies the minimum performance specification of the equipment and the levels to be demonstrated under standard test conditions. For the purposes of this chapter, standard test conditions are defined in documents EUROCAE ED-14G / RTCA DO-160G "Environmental Conditions and Test Procedures for Airborne Equipment" or the revision level as agreed with the certification authority, paragraph 3.4 as: Temperature 
+15 to +35°C 

| Relative Humidity    | Not greater than 85%      |
|----------------------|---------------------------|
| Ambient Pressure     | 84 to 107 kPa             |
| Lighting Level       | Between 100 and 1 000 lux |

In addition to the above; the AC electrical power supply shall be within the limits specified as Normal in section 16 of ED-14G/DO-160G or the revision level as agreed with the certification authority; the DC electrical power supply shall be within the limits specified as maximum and minimum in section 16 of ED-14G/DO-160G, or the revision level as agreed with the certification authority. The electrical power supply used shall be essentially free from modulation, ripple, interruptions and surges. In the case of equipment designed for operation from an AC power source of variable frequency, unless otherwise specified, tests should be performed at representative input power frequencies with the input frequency adjusted to within 5% of a selected frequency. 

## Iii-3.2 Equipment Minimum Performance Levels

The equipment shall be designed to meet and shall be tested to show compliance with the following Minimum Performance Levels. 

NOTE: 
Where these paragraphs state requirements regarding the signal in the recording medium, it should be interpreted as that observed at the output of the playback equipment specified by the equipment manufacturer.  

## Iii-3.2.1 Recovered Image Quality

The recovered image shall conform to Table III-3.1. 

## Iii-3.2.2 Start-Up And Effects Of Power Interruptions

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
Following a system electrical power interruption the characteristics of the Image recorder system (including any equipment identified in section III-1.4.1) shall be as described in the following table.  These characteristics are applicable to each class of image recorder: A, B, C, D and E. The table clarifies the performance requirements for tests under EUROCAE ED-14G / RTCA DO-160G section 16.  

Recording Requirement 
Power 
Interruption 
Interruption 
Duration 
Initial Power 
Level 
Cold Start 
>2s 
No Power 
Following initial application of power to the recorder system, the system shall be capable of recording information in the recording medium as soon as possible 
but no later than 10s. For systems with multiple image 
sources it is permissible to increase this time to a 
maximum of 20s. Any built-in test function shall be completed within 60s. 
Warm Restart  
Within 200ms 
to 2s 
 
Normal, Abnormal, and 
Emergency 
For interruptions with a duration of 200ms to 2s, the recorder system shall recover and commence storing information, in the recorder medium, as soon as possible but no later than 2s after power is restored. Any built-in 
test function shall recover within 5s(1). 
Recorder and NON- Camera 
Electronics 
Warm Restart  
Within 10ms 
to 2s 
 
For interruptions with a duration of 10ms to 2s, images shall be available at the output of the camera as soon as 
possible but no later than 2s after power is restored. 
Normal, Abnormal, and 
Emergency 
Camera 
Electronics 
Transient 
0 to 200ms 
Normal 
Interruptions with a duration of 0 to 200ms shall have no 
effect on the recorder system. Recorder and NON- Camera 
Electronics 
Transient 
0 to 10ms 
Normal 
Interruptions with a duration of 0 to 10ms shall have no 
effect on the camera. Camera 
Electronics 

NOTE 1:  
Any built-in test function may take up to 5s to recover. The recovery period of 5s is intended to permit power-up test and system initialization 
routines to be performed. It is recommended that such routines should be 
performed as rapidly as possible to minimize the recovery period. 
 

Image Recorder 
Resolution 
Field of View 
Sensitivity 
Contrast / Grey Scale 
Distortion & Artefacts 
Class (per paragraph 
III-1.4.1) 
A 
Sufficient to distinguish 
Full width of front 
5mm resolution bars 
instrument panel 
Full resolution at 1 lux 
256 colours 
Meet Required 
resolution 
as per test chart 
B 
It shall be possible to 
visually differentiate 
between 3mm display 
Face of display 
Distinguish between 
panel numeric (for 
"5" and "6" at 1.7 nits 
256 colours 
Meet Required 
resolution 
example "5" and "6") 
on an image. 
C 
It shall be possible to 
visually differentiate 
between 4mm display 
Full width of front 
Distinguish between 
panel numeric (for 
instrument panel 
"5" and "6" at 1.7 nits 
256 colours 
Meet Required 
resolution 
example "5" and "6") 
on an image. 
D 
As provided by system 
As provided by system 
As provided by system 
As provided by system 
Meet Required 
resolution 
E 
As provided by system 
As provided by system 
As provided by system 
As provided by system 
Meet Required 
resolution 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter Iii-4 Minimum Performance Specifications Under Environmental Test Conditions Iii-4.1 Introduction

CHAPTER 2-3 defines the environmental tests to be performed on the recorder system. Compliance with the applicable performance requirements of this part for the Airborne Image Recording System shall be demonstrated as shown in Table III-4.1. 

## Iii-4.2 Additional Requirements Iii-4.2.1 Vibration

In addition to the vibration tests defined by EUROCAE ED-14G / RTCA DO-160G, the camera shall perform the following. The camera shall be able to meet the resolution requirements defined in paragraph III-2.3.3.1III-2.3.3.1III-2.3.3.1III-2.3.3.1III-2.3.3.1, under the following conditions: EUROCAE ED-14G / RTCA DO-160G Section 8, test level B2, less 3dB, extended to 5 Hz. The Power Spectral Density (PSD) shall be constant between 5 Hz and 10 Hz using lighting level as close to 100 lux as practicable. 

## Iii-4.2.2 Light Levels

The camera shall satisfy the requirements of paragraph III-5.2.1 with lighting levels as specified below: a. 

Quality Index Chart Illuminated at 86 000 lux (measured incident at the Chart) 

b. 
Quality Index Chart Illuminated at 1 lux (measured incident at the Chart) 

## Iii-4.3 Exceptions To General Requirements

There are no exceptions to the general requirements defined in paragraph 2-3.2 for Image recording systems. 

MOPS PARAGRAPH NUMBER 
2-1.6 
2-1.7 
III-2.3.3.1 
III-3.2.1 
III-2.3.3.4 
III-2.3.3.5  
Environment 
Test Reference 
and III-2.3.3.6 
III-2.2.8 
NORMAL 
BIT ERROR 
Distortion / 
OPERATION  
RATE  
Resolution 
Sensitivity 
Contrast / 
Grey Scale 
Artefacts 
Update Rate 
Temperature 
Table 2-3.1 Item 1 
R 
 
R 
R 
R 
R 
R 
Altitude 
Table 2-3.1 Item 2 
R 
 
R 
R 


Temp Variation 
Table 2-3.1 Item 3 
R 
 
R 
R 


Humidity 
Table 2-3.1 Item 4 
R 
 
R 
 
 
R 
R 
Shock 
Table 2-3.1 Items 5 and 6 
R 
R 


R 
Vibration (Survival) 
Table 2-3.1 Item 7 
R 
R 


R 
Magnetic Effect 
Table 2-3.1 Item 15 
R 


Voltage Spike 
Table 2-3.1 Item 16 
R 
 
R 
 
 
R 
 
Power Input 
Table 2-3.1 Item 17 
R 
 
R 


AF Susceptibility 
Table 2-3.1 Item 18 
R 
 
R 
 
 
R 
 
Induced Susceptibility 
Table 2-3.1 Item 18 
R 
 
R 
 
 
R 
 
RF Susceptibility 
Table 2-3.1 Item 19 
R 
 
R 
 
 
R 
 
Lightning 
Table 2-3.1 Item 21 
R 
 
R 


Vibration 
Para III-4.2.1 
R 
 
R 
R 


High Lighting Level 
Para III-4.2.2 a 
R 
 
R 
R 
R 
 
 
Low Lighting Level 
Para III-4.2.2 b 
R 
 
R 
R 
R 
 
 
Key  
Blank = Manufacturer's Discretion                            R = Test Required 
 

## Chapter Iii-5 Test Procedures Iii-5.1 Introduction

This chapter specifies the standard test procedures for demonstrating compliance with CHAPTER III-2, and CHAPTER III-3. Although specific test procedures are cited, it is recognised that they will not apply in all cases and that other methods may be preferred or required. Alternative methods may be used if the manufacturer can show that they provide equivalent certification data. Where a test procedure is not specified for a particular performance parameter, the manufacturer may show compliance either by analysis or by devising a test appropriate to the equipment design. 

## Iii-5.1.1 Adjustment Of Equipment

The equipment under test shall be properly aligned and adjusted in accordance with the manufacturer's recommendations. 

## Iii-5.1.2 Test Instrument Precautions

Precautions shall be taken to prevent the introduction of errors resulting from impedance mismatch and the improper connection of test instruments to the equipment under test. 

## Iii-5.1.3 Test Conditions

Unless otherwise stated, the test procedures of this chapter apply to systems with analogue inputs and analogue outputs. Where parts of the system use digital processing, the test procedures assume that interface conversion equipment appropriate to the recovery of the recorded information and which match the performance characteristics of the system to be certified, are used. All tests shall be performed under the conditions defined in paragraph III-3.1.  

## Iii-5.1.4 Connected Loads

Unless otherwise specified, all tests shall be performed with the equipment connected to loads having the impedance values for which it is designed. 

## Iii-5.1.5 Warm-Up Period

Unless otherwise specified, all tests shall be performed after a warm-up (stabilisation) 
period of not less than 5 minutes and not more than 15 minutes. 

## Iii-5.1.6 Recording Of Test Results

Except where tests are GO/NO GO in character (e.g. the determination of whether or not mechanical devices function correctly) the actual numerical values obtained for each of the parameters tested shall be recorded in a qualification test report. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Iii-5.2 Electrical Test Procedures Iii-5.2.1 Recovered Image Quality

The quality of the Recovered Image shall be established and shall not be less than that corresponding to the values of "quality index pattern" as stated below. The overall system quality can be assessed by imaging a reference test pattern. This test pattern shall have the following attributes which are met by the test chart shown in Figure III-5.1: 

 
Horizontal lines with separation ranging from 5 mm to 1 mm spacing. 
 
Vertical lines with separation ranging from 5 mm to 1 mm spacing. 
 
Colour blocks with 8 typical cockpit colours (red, green, blue, magenta, cyan, yellow, black and white). 
 
Text (Compatible with Class C image) 
 
Industry Standard preferred 
This pattern, which will be 0.3 m x 0.225 m, should be placed in the 4 corners and the centre of the image area which typically measures 2 m (horizontal) by 1.6 m (vertical) minimum, as shown in Figure III-5.2. Alternative dimensions may be used, but should be representative of the dimensions and format of the cockpit in which the equipment is to be installed. The background of the image area shall be patterned to represent a typical cockpit. It shall be possible to distinguish the lines at the required separation level after imaging and reproducing the image with the system under test under standard lighting conditions (100 - 1 000 lux). Other lighting conditions will be verified in separate tests. 

NOTE: 
Figure III-5.1 requires full colour reproduction, which is not possible within this document.  

## Iii-5.2.2 Start Of Recording

The Equipment shall be switched on, and the time until the first image is successfully recorded shall be noted. This shall conform to the timings given in paragraph III-3.2.2.  

## Iii-5.2.3 Update Rate

The Equipment shall be set to operate, viewing a scene representative of an aircraft cockpit. The Equipment shall be allowed to stabilise for a period of 5 minutes. The Equipment shall then be operated over a period of one minute, and the number of picture frames recorded shall be recorded. A frame rate per second shall be calculated, and conformity with the required Update Rate for the Image Recording system shall be established. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter Iii-6 Equipment Installation And Installed Performance Iii-6.1 Introduction

This chapter specifies installation characteristics and performance with procedures for verifying that performance when the equipment is installed in an aircraft. Installed performance criteria are generally the same as those contained in CHAPTER III-3, which were verified through bench and environmental tests. However, certain performance parameters may be affected by the physical installation and can only be confirmed after installation. 

## Iii-6.2 Equipment Installation Iii-6.2.1 Accessibility

a. 
Maintenance provisions for equipment adjustments shall not be readily accessible to the flight crew. 
b. 
Any Bulk Erase control shall be available in the cockpit. 

## Iii-6.2.2 Aircraft Environment

Equipment shall be compatible with the environmental conditions present in the specific location in the aircraft where the equipment is installed. Operation of the equipment shall not be affected by aircraft manoeuvring or changes in attitude encountered in normal flight operations. Operation of the equipment should not be affected by those extreme conditions likely to, be encountered during an accident sequence e.g. stall buffet, violent and extreme manoeuvres, however under these conditions picture quality may be degraded. Based on the expected displacement of the camera relative to the scene being viewed, it is recommended that the camera is mounted sufficiently rigid to avoid resonances below 50 Hz. 

## Iii-6.2.3 Failure Protection

a. 
Any failure of the Image Recorder system shall not degrade the normal operation of any other equipment or systems connected to it. 
b. 
The failure of interfacing equipment or systems shall not degrade normal operation of the Image Recorder system. 

## Iii-6.2.4 Interference Effects

The installed equipment shall not: a. 
be the source of harmful conducted or radiated interference, nor 
b. 
be adversely affected by conducted or radiated interference from other equipment or systems installed in the aircraft. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

NOTE: 
          Electromagnetic compatibility problems noted after installation of the 
          equipment may result from such factors as the design characteristics of 
          previously installed systems or equipment and the physical installation 
          itself. It is not intended that the equipment manufacturer design for all 
          installation environments. The installer will be responsible for resolving 
          any incompatibility between the equipment and previously installed 
          equipment. 

## Iii-6.2.5 Insulation Resistance

The insulation resistance between any exposed conducting material of the cockpit equipment (non-electrical circuit) and the electrical circuit of this equipment shall be at least 10 Mohms when measured with an applied voltage of at least 50 volts DC. 

## Iii-6.2.6 Recorder Operation

The recorder shall be equipped with a means to automatically start it before the aircraft moves under its own power. An acceptable means would be the detection of engine oil pressure. 

If required, an acceptable means of manually starting the recorder prior to engine start (for the purpose of recording the pre-flight cockpit checks) include: a. 

pressing the AIR test button, 

b. 
operating some device early in the check list procedures. 
Once manually started, the recorder should latch to that condition until the shutdown logic is satisfied. In order to ensure reliable operation, particularly under the abnormal conditions which might precede an accident, the means provided to automatically stop the recorder should rely on more than one device, e.g. engine oil pressure, weight-on-wheels sensor and airspeed sensors. 

NOTE: 
Use of the parking brake as the sole means for control of recorder operation is not recommended since this arrangement will cause interruptions of the recording during normal taxiing operations. 

If required by operational rules an acceptable means of stopping the recorder after an accident include: i. 

detection of loss of oil pressure on all engines together with loss of airspeed. 

ii. 
airframe crash sensors, 
iii. 
water immersion sensors e.g. to detect ditching of a helicopter. 
Negative acceleration sensors ('g' switches) shall not be used as sole means of detection because their response is not considered to be reliable. 

## Iii-6.2.7 Bulk Erase Interlocks

Where provision is made in the cockpit for bulk erasure of the recording by the flight crew, the function shall be inhibited to prevent inadvertent or untimely erasure whilst the aircraft is capable of moving under its own power. Acceptable means of inhibiting the function include interlocks with: a. 

the parking brake and weight-on-wheels sensor,  

b. 
the main cabin door position sensor and weight-on-wheels sensor, 
c. 
In the case of a helicopter, the rotor brake.  

## Iii-6.2.8 Quality Of Recovered Image

For each newly installed system, the quality of the recovered image shall be established by analysis of data recorded on the ground and in flight. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Iii-6.2.9 Maintenance

An analysis shall be performed by the equipment installer to identify those aspects of the installation where the serviceability could be degraded and remain undetected. The maintenance tasks to be performed shall take account of this analysis by requiring appropriate functional and maintenance checks at suitable intervals. 


## Iii-6.3 Ground Test Procedures Iii-6.3.1 Equipment Function

Vary all controls of the equipment through their full range to determine that the equipment is operating according to the manufacturer's instructions and that each control performs its intended function. 

## Iii-6.3.2 Interference Effects

With the equipment energised, individually operate each of the other electrically operated aircraft equipment and systems to determine that no significant levels of conducted or radiated interference exist. Evaluate all combinations of control settings and operating modes. Operate communication and navigation equipment on the low, high and at least one mid-band frequency. Identify systems or modes of operation that should be evaluated during flight. 

If appropriate, repeat the tests using emergency power with the aircraft's batteries alone and any standby inverters operating. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Iii-6.3.3 Power Supply Fluctuations And Protection

Verify equipment operation from available aircraft power sources, including normal generator switching. 

## Iii-6.4 Flight Test Procedures Iii-6.4.1 General

This section provides guidance for flight testing prototype installations both aeroplanes and helicopters. It may need to be adapted to suit the particular installation being tested and to comply with operating regulations. Each newly installed Image Recording System will need to be flight tested and the recording so obtained, to be evaluated to show adequate recording quality during all normal regimes of flight including taxiing, take-off, cruise, approach and landing. For helicopters, hover and autorotation should be included. Since the duration of the recording may be limited, the test flight should be carefully planned. The Image Recorder circuit breaker can be tripped between each test phase and at the end of the landing run if the flight time is likely to exceed the recording duration limit. The replay and evaluation will need to be performed by a replay centre acceptable to the Certification Authority. 


## Annex Iii-A Post Flight Evaluation Of Recordings Iii-A.1 Introduction

III-A.1.1 
Following the flight testing of each new AIR installation, the recording so obtained shall be evaluated to confirm adequate quality. Similarly, it will be necessary to evaluate recordings obtained on a sampling basis from in-service flying or following cockpit modification, which may change the image environment to ensure that quality is maintained. 
IIII-A.1.2 
It is recommended that the replay equipment be located in a clean, quiet area which is separated from other work areas sufficiently to ensure the privacy of recordings. Access to the replay equipment should be restricted to authorised personnel only. 
III-A.1.3 
Provision shall be made for the secure storage of AIR recording media and any copies made. 
III-A.1.4 
The replay and evaluation of recordings shall be performed by personnel with adequate knowledge of AIR systems and aircraft operations, and who have appropriate experience of the techniques used to evaluate recordings. 
NOTE 1: 
Accident investigation authorities may be able to provide demonstrations which would assist the training of personnel. 
NOTE 2: 
Where possible, replay personnel should be given the opportunity to accompany the flight crew on an AIR test flight in order to become familiar with the test procedure. 
III-A.1.5 
A test report and certification in a format acceptable to the Certification Authority will be required to record the observations made from evaluation of the recording. 

## Iii-A.2 Replay Equipment

The evaluation of recordings from new AIR installations should involve replay on equipment capable of not degrading the images. 

## Iii-A.3 Recording Evaluation

III-A.3.1 
The recording shall be checked to confirm that the required input sources are connected to the AIR system, and that image quality is acceptable and by ensuring that the resolution available is sufficient to meet the specified resolution requirements. 
III-A.3.2 
For combined recorders with AIR function, image recordings may be verified by correlating data values against announcements made by the flight crew. 

## Iii-A.4 Test Report

III-A.4.1 
A suitable report is shown in TABLE III-A.1. The report may be supplemented by photographic or printed evidence obtained from selected extracts of the recording. 
III-A.4.2 
The spaces on the report, as applicable, should be annotated with brief comments on the replay signal quality. 
 
ABC AVIONICS  
CERTIFICATE NO  
 
Municipal Road TOONVILLE 

## Test Certificate

AIRCRAFT IMAGE RECORDER - FLIGHT TEST EVALUATION AIRCRAFT TYPE:  ...................... REGN:  ........................................ OPERATOR:  
.................................. 

 

| CVR TYPE:     |  SERIAL NO:     |  FLIGHT NO:     |     |     |
|---------------|-----------------|-----------------|-----|-----|

 

## Image Recording Quality Check

Spatial resolution 
"Good" or "Not good" 
Field of view 
"Good" or "Not good" 
Camera sensitivity  
"Good" or "Not good" 
Contrast 
"Good" or "Not good" 
Distortion 
"Good" or "Not good" 
Digital artefacts 
"Good" or "Not good" 

 REMARKS:  
................................................................................................................................................ Certified that the above mentioned recording has been evaluated in accordance with the terms of the contract/order applicable thereto and the requirements of the Certification Authority relating to the evaluation of such recordings. SIGNED:  
.......................................................................DATE:  
................................................................. 

 
for and on behalf of ABC Avionics Organisation Approval Reference ..........................................................  
 

## Annex Iii-B Maintenance Practices Iii-B.1 General

The maintenance tasks required to ensure the continued serviceability of the installed AIR system will depend on the extent of monitoring built into the AIR system. The installer shall perform an analysis of the AIR system to identify those parts of system which, if defective, would not be readily apparent to the flight crew or maintenance personnel. Appropriate inspections and functional checks, together with the intervals at which these would need to be performed, need to be established as indicated by the analysis. The specified checks need to include verification of system performance, where appropriate. 

A flight recording should be replayed at specified intervals to reveal defective equipment and to indicate essential maintenance actions. Where a replay evaluation indicates an aircraft system defect, appropriate corrective action shall be initiated. Any inspection or test requirements specified by equipment manufacturers shall be observed, e.g. battery checks of the underwater locator beacon. Maintenance and flight crew procedures should emphasise the need to preserve the recording following a reported occurrence. 

## Iii-B.2 Recording Evaluation

An in-flight recording should be replayed and assessed for quality.  Annex III-A provides guidance for the evaluation of such recordings. Aircraft image recorder systems should be considered unserviceable if the recording duration is less than required, if there is a period of poor quality images. 

## Iii-B.3 Primary Maintenance Tasks

Table III-B.1 shows the primary maintenance tasks for the installed AIR system. Inspection periods should be established on the basis of the AIR system analysis discussed in paragraph III-B.1. 

| Item                                     | Equipment                          | Task                               | Maximum Interval    |
|------------------------------------------|------------------------------------|------------------------------------|---------------------|
| Operational                              |                                    |                                    |                     |
| Check                                    |                                    |                                    |                     |
| Daily (pre-flight and/or                 |                                    |                                    |                     |
| post-flight)                             |                                    |                                    |                     |
| 1                                        | Aircraft Image                     |                                    |                     |
| Recorder                                 |                                    |                                    |                     |
| System                                   |                                    |                                    |                     |
| Confirm serviceability using TEST        |                                    |                                    |                     |
| function on AIR controller or Check      |                                    |                                    |                     |
| 'no                                      | -                                  | fail' indication for built in test |                     |
| Not exceeding 6                          |                                    |                                    |                     |
| months elapsed time                      |                                    |                                    |                     |
| 2                                        | Check/                             |                                    |                     |
| Functional                               |                                    |                                    |                     |
| Test                                     |                                    |                                    |                     |
| Inspect Installation. Confirm proper     |                                    |                                    |                     |
| functioning of the inhibit logic for the |                                    |                                    |                     |
| bulk erase.                              |                                    |                                    |                     |
|                                          |                                    |                                    |                     |
| Check/Replay Not exceeding interval      | 3                                  | Aircraft Image                     |                     |
| Recorder                                 | stated by the vendor               |                                    |                     |
| Remove recorders for inspection and      |                                    |                                    |                     |
| test as required by the Component        |                                    |                                    |                     |
| Maintenance Manual.                      |                                    |                                    |                     |
| NOTE:                                    |                                    | The recording stored on            |                     |
| the media prior to the                   |                                    |                                    |                     |
| removal                                  | should                             | be                                 |                     |
| evaluated.                               |                                    |                                    |                     |
| Not exceeding 24                         |                                    |                                    |                     |
| months elapsed time                      |                                    |                                    |                     |
| Confirm proper sensor function. Test     |                                    |                                    |                     |
| may be performed in-situ if practical.   |                                    |                                    |                     |
| 4                                        | Ditching                           |                                    |                     |
| Sensor                                   |                                    |                                    |                     |
| (Helicopter)                             |                                    |                                    |                     |
| Check/                                   |                                    |                                    |                     |
| Functional                               |                                    |                                    |                     |
| Test                                     |                                    |                                    |                     |
| 5                                        | Crash Sensor                       |                                    |                     |
| (where fitted)                           |                                    |                                    |                     |
| As stated by vendor                      | Comply with instructions issued by |                                    |                     |
| vendor                                   |                                    |                                    |                     |
| Check/                                   |                                    |                                    |                     |
| Functional                               |                                    |                                    |                     |
| Test                                     |                                    |                                    |                     |
| 6                                        | Underwater                         |                                    |                     |
| Locator Beacon                           |                                    |                                    |                     |
| As stated by vendor                      | Comply with instructions issued by |                                    |                     |
| vendor                                   |                                    |                                    |                     |
| Check/                                   |                                    |                                    |                     |
| Functional                               |                                    |                                    |                     |
| Test                                     |                                    |                                    |                     |
| 7                                        | Aircraft Image                     |                                    |                     |
| Recorder                                 |                                    |                                    |                     |
| Remove AIR immediately post-flight.      |                                    |                                    |                     |
| Replay and evaluate the quality of the   |                                    |                                    |                     |
| in-flight recording.                     |                                    |                                    |                     |
| Check in                                 |                                    |                                    |                     |
| accordance                               |                                    |                                    |                     |
| with criteria                            |                                    |                                    |                     |
| and                                      |                                    |                                    |                     |
| procedures                               |                                    |                                    |                     |
| agreed with                              |                                    |                                    |                     |
| the Regulatory                           |                                    |                                    |                     |
| Authority                                |                                    |                                    |                     |
| One year, or up to a                     |                                    |                                    |                     |
| maximum of two years                     |                                    |                                    |                     |
| if approval from the                     |                                    |                                    |                     |
| appropriate regulatory                   |                                    |                                    |                     |
| authority has been                       |                                    |                                    |                     |
| obtained for AIR                         |                                    |                                    |                     |
| systems that have a                      |                                    |                                    |                     |
| demonstrated high                        |                                    |                                    |                     |
| integrity of                             |                                    |                                    |                     |
| serviceability self-                     |                                    |                                    |                     |
| monitoring                               |                                    |                                    |                     |
|                                          |                                    |                                    |                     |

## Part Iv Data Link Recorder Systems

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Chapter Iv-1 Introduction Iv-1.1 Purpose And Scope

This part defines the minimum specification to be met for all aircraft required to carry a data link recorder system for the purposes of the investigation of a reportable accident or incident. It is applicable to crash-protected recorders, ancillary equipment and their installation in civil aircraft. This part shall be read in conjunction with Sections 1 and 2, together with Sections 3, 4 and 5 as applicable. 

## Iv-1.1.1 General

This part responds to a need for improved crash-protected recorders to serve the vital role that accident and incident investigation plays in promoting aviation safety. 

It is intended to define the design and performance specifications for a unit capable of storing airborne digital messages, as well as providing design and performance specifications that will apply to the systems that will provide data to the airborne recording units. The purpose of this Part is to establish a basis for the approval of flight recorders capable of recording digital messages that are transmitted to and from the aircraft and their effects on the cockpit/flight crew interaction. 

## Iv-1.1.2 Description Of Content

This part is divided into 6 Chapters and 2 Annexes. CHAPTER IV-1 describes the typical equipment application and operational objectives from the data link recording. CHAPTER IV-2 establishes the minimum system performance requirements for the digital communication recording system. CHAPTER IV-3 defines the minimum performance specification of the equipment and the levels to be demonstrated under standard test conditions. CHAPTER IV-4 defines the minimum performance specification of the equipment and the levels to be demonstrated under environmental test conditions. Additional tests may be required for equipment using new techniques. The extent of such tests shall be agreed between the certification authority and the equipment manufacturer. 

CHAPTER IV-5 specifies tests and procedures for determining compliance with the performance requirements and for demonstrating crash survival capability. CHAPTER IV-6 defines the installation characteristics and performance with procedures for verifying that performance when installed in an aircraft. The Annexes give additional guidance on system architecture and provide details of the parameters to be recorded. 

## Iv-1.2 Application Iv-1.2.1 Data Link Recording

Compliance with this Part will ensure that data link Communication Recording systems will perform their primary function under the conditions encountered in aircraft operations. 

 

## Iv-1.3 Technical Background Iv-1.3.1 System Reliability

The viability of an aircraft type is seriously threatened when the cause of an accident involving the type cannot be determined in the recovery of recorders from crash sites and in the subsequent analysis of the recordings. Close attention should be given therefore, to the reliability of the recording function. This consideration applies both to maintenance tasks and to recorder and installation design. For maintenance tasks refer also to ANNEX IV-B. 

## Iv-1.4 Description Of The System Iv-1.4.1 Equipment

The data link recorder system shall include the following items as appropriate for the aircraft: a. 
A crash-protected recorder in which the recording can be synchronised with the other airborne recordings. 
b. 
Digital interface equipment suitable for converting a data link message into a format which is to be recorded. 
c. 
Digital data busses and/or networks providing communications between elements of the system. 

## Chapter Iv-2 Data Link Recorder Specification Iv-2.1 Equipment Design Specifications Iv-2.1.1 General

This chapter establishes the minimum operation performance specifications for the equipment comprising the data link Communication Recorder System. The data link recording system shall be designed to receive, process, store and enable the retrieval of data link information transmitted to and from the aircraft in accordance with the requirements of this chapter. The requirements for digital communications that may be recorded both on board the aircraft and on the ground are summarised as follows. For complete text of the overall systems requirements and message types to be recorded refer to Minimum Aviation System Performance Specification for CNS/ATM Recorder Systems (ED-93): a. 

All communications to and from the flight crew shall be recorded on the aircraft in order to develop a thorough understanding of the working environment of the cockpit. This is of fundamental importance to accident investigation. 

b. 
In the same way that traditional audio recording has enabled investigators to determine if radio communications systems were overall functioning as required, the airborne recording of digital communications will help to determine the end-to-end functioning of the data link system. 
c. 
Increased reliance will be placed on digital messaging to ensure safe operation in an environment where separations will be significantly reduced and profiles flown will be assumed to be much more precise. Much of this information may not involve the flight crew or controller and messages may be addressed directly to and from the aircraft's systems. The recording of such information will prove valuable. 
d. 
Ground based recording will involve many stations and locations around the world. An effective means of ensuring that the information is readily available to an accident investigation is to record as much of it, as practical on board the aircraft. 
e. 
Recording on the ground is required in order to correlate the transmitted and received messages and to investigate periods beyond the duration of the airborne recording. Part of this reason is to be able to understand the role of air 
traffic control in the occurrence, and to be able to understand the interactions between ground stations, other aircraft, and other agencies. 
To meet the operational goals, there are two main issues each of which require consideration in terms of both airborne and ground recording: a. 
Recording of digital communications to and from the flight crew. This includes those messages that would have traditionally been passed by voice means. 
b. 
Other data link messages that are transmitted to and from the aircraft for the purposes of weather information, navigation and surveillance (For example differential GPS requiring position correction), and advanced TCAS that may require communication from aircraft to aircraft. 

## Iv-2.1.2 Recording Technique

The recorder shall use a digital method of recording and storing the data. Where data compression is used it shall be fully reversible. For reconstituted (or decompressed) data, it shall be demonstrated that there is no degradation or loss of messages or timing correlation of the data when compared to the original input data. 

## Iv-2.1.3 Digital Recording And Retrieval Characteristics

The data link message information shall be readily retrievable from the recording medium and reconstructed completely without loss of data content or timing correlation irrespective of the recording format. 

Recording medium organisation and records shall be such that: a. 

for an undamaged, fully serviceable recording medium with a normal recording, the recorded information is readily retrievable, 

b. 
for a damaged or partially failed recording medium, the available information can be retrieved using special techniques, as required. 

## Iv-2.1.4 Recorder Synchronisation

The recordings on the data link recorder shall be synchronised to other airborne recordings as defined in paragraph 2-1.11. 

## Iv-2.1.5 Start And Termination Of Recording

Recorder operation shall be as defined in paragraph 2-1.5. 

## Iv-2.1.6 Data To Be Recorded Iv-2.1.6.1 Data Link Applications And Services To Record

If the aircraft flight path is authorised, directed or controlled by data link messages, then all data link messages, both up-links (to the aircraft) and down-links (from the aircraft), the time they are displayed to the flight crew, and their data link response shall be recorded on the aircraft in order to determine an accurate sequence of events for the aircraft and cockpit operation. AOC/AAC datalink services, Navigation and surveillance parameters should be recorded if data link message transfer is a feature of the system architecture - refer to ANNEX IV-A for message type details required to be recorded. Message recording and associated timing shall apply to the recording requirements of: a. 

Flight crew communication as defined in ED-93 paragraph 2.3.2.1 

b. 
Navigation as defined in ED-93 paragraph 2.3.2.3 
c. 
Surveillance as defined in ED-93 paragraph 2.3.2.5 
NOTE: 
In order to minimise recording medium utilisation, data link messages may be recorded on an interrupt basis, i.e. as the message occurs. 

The recording of digital messages may be made in one or more airborne recorders. The data link message shall be recorded on the aircraft, whether generated automatically or manually, and shall be independent of the media transmission method (VHF, Satcom, HF, Mode S or other). 

## Iv-2.1.6.2 Content Of Recordings

Sufficient information shall be recorded to enable the following to be determined: a. 
The content of ALL messages generated and received by the flight crew. 
b. 
The message priority (if any) 
c. 
The number of messages in any available queue 
d. 
The display status of each message 
Clarification of "Message priority": Being able to determine message priority means - if a message has an associated priority that may have an effect upon the order of or method of its display or transmission, then the existence of such a priority should be determinable from the recorded information. 

 
Clarification of "Available queues": Being able to determine the number of messages in available queues means - as far as practical given by the architecture of the system the recorded information should be sufficient to determine at any given time, how many messages may have been received at the aircraft, but not displayed to the flight crew. Conversely, it should be determinable how many messages the flight crew has generated which have not yet been sent to the ground. Clarification of "Display Status": The recording of message display status means - as far as practical given the architecture of the system, information concerning the state of flight crew selection of the messages should be recorded. Current states may include new arrival, open, acceptance, rejection of messages, etc. 

IV-2.1.6.3 
Timestamp It shall be possible to determine time information associated with each data link message, with a minimum resolution of 1 second. The time information shall include Hours/Minutes/Seconds/Day/Month and should include Year, if available.  
NOTE: 
The reason for the inclusion of date within the timestamp is that, since a 
data link message may be recorded on interrupt basis, there may be information from more than a single 24-hour period within the recorder and the date will provide information to determine which is most recent. 
The following timing information associated with the digital messages shall, as far as practical given the architecture of the system, be capable of being determined from the airborne-based recordings: a. 

The time each message was generated (i.e. when "send" was selected) 

b. 
The time any message was available to be displayed by the flight crew 
c. 
The time each message was actually displayed or recalled from a queue 
d. 
The time of each status change 
Clarification of "Time stamp": The recording of time stamps means - the recorded information associated with each message should be sufficient to determine the time the message was recorded. This can be accomplished either by recording an explicit time identifier with each message or by recording in such a manner that the relative time can be referenced to a timeline with an absolute time basis. Clarification of "Status change": The recording of message status change means - as far as practical given the architecture of the system, information concerning the flight crew interaction with the messages should be recorded. Interactions include acknowledgement of messages, recall of messages, WILCO of messages, etc. 

## Iv-2.1.7 Recording Capacity And Duration

The recorder shall have adequate capacity to record all required data link messages during the most recent time period at least equal to the recording duration required for the CVR.  
NOTE 1: 
Future technology may require alternate bus transfer speeds and larger recording medium capacity. This should be taken into account in the design of the recorder system. 
NOTE 2: 
As the data link message recording is an event type recording (opposed to sequence method as is the case for the audio recorder system), there is no fixed relationship between the recording medium capacity and the duration of the recording.  
However in some circumstances, the data link message traffic may exceed the limit defined, and consequently the recording duration may be insufficient regarding the recording medium size defined. Paragraph IV-3.2.6 gives a standard method to calculate the amount of recording medium required. Memory chip or recording capacity failure during normal recording shall be tolerated until the total recording medium capacity falls below the required duration. When the recording capacity threshold is crossed a BIT fault should be recorded in recording medium, but the recorder should continue to record until power is removed.  
In addition any mismatches between the rate of the input port, the actual input rate from the CMU/ATSU, and the size of the recording medium module should be detected by the recorder and a BIT fault recorded. 

## Iv-2.1.8 Data Burst Throughput

The recorder should be capable of processing and recording a high speed burst of digital data at the maximum rate of the interface employed in the digital communication system design which shall have no adverse effect on the performance of the recorder. (Refer to paragraph IV-3.2.7.) 

## Iv-2.1.9 Databus Selection

The databus interface chosen for the recorder shall, as a minimum, support the amount and frequency of digital message traffic required to be recorded in accordance with design requirements of this MOPS. 

## Iv-2.1.10 Recording Format

Each message shall be recorded in a format that is easily identified and decodeable by the recorder manufacturer and accident investigators. All data, including element identifiers (such as priority, message number etc.) or equivalent shall be recorded. (Refer to paragraph IV-2.1.6). It shall be possible to determine the entire message or partial message from multiple elements stored in the crash-protected medium. 

## Iv-2.1.11 Means For Replay Of The Recorded Information

The means for replaying the data message recording shall: 

a. 
Minimise the possibility of unauthorised replay of the recording 
b. 
Not erase, rewrite or alter the recording during replay 

## Iv-2.1.12 Erasure Of Recorded Data

Except for the overwriting of the oldest data by new information, no means for the erasure of the record shall be provided in the recorder.  
NOTE: 
It is understood that military organisations may use commercial recorders. In this case, they may have additional security requirements that exempt the recorder from this requirement. Arrangements should be made with the certifying authorities in regard to such exemptions 

## Iv-2.1.13 Recording And Recording Medium Characteristics Iv-2.1.13.1 Time Base Characteristics

A stable time base or reference signal shall be provided. 

## Iv-2.1.13.2 Recording Delay

The delay in recording the data, from the time that it is presented at the input of the recorder to the time this data is stored in the crash-protected medium, should be minimised. (Refer to paragraph IV-3.2.4) 
 

## Iv-2.2 Crash Survival Iv-2.2.1 Data Retrieval Characteristics

A means shall be provided to retrieve and decode the recorded data link messages and timestamps. A method of rapid retrieval of the data should not alter, degrade or overwrite the data in the recording medium. The data shall be readily retrievable from the recording medium without loss of quality or timing correlation irrespective of the recording medium. It shall be possible to recover the digital messages in the same chronological order in which they occurred. 

## Iv-2.2.2 Data Retrieval

The organisation of the recording medium and the recording shall be such that: a. 
for an undamaged, fully serviceable recording medium with a normal recording, 
the recorded information is readily retrievable, 
b. 
for a damaged or partially failed recording medium, the available information can be retrieved using special techniques, as required. 

## Iv-2.2.3 Downloading Of Crash-Protected Recording Medium

It shall be possible to download the data link message data from the crash-protected medium, while the recorder is installed on the aircraft. Recorded digital messages shall not be erased, re-written or altered during the process of downloading. It is not required that the normal message recording function continues during the process of downloading. 

## Chapter Iv-3 Minimum Performance Specifications Under Standard Test Conditions Iv-3.1 Introduction

This chapter specifies the minimum performance specification of the equipment and the levels to be demonstrated under standard test conditions. For the purposes of this chapter, standard test conditions are defined in documents EUROCAE ED-14G / RTCA DO-160G "Environmental Conditions and Test Procedures for Airborne Equipment" or the revision level as agreed with the certification authority, paragraph 3.4 as: a. 

Temperature 
: +15 to +35°C 

b. 
Relative Humidity 
: Not greater than 85% 
c. 
Ambient Pressure 
: 84 to 107 kPa 
In addition to the above; the AC electrical power supply shall be within the limits specified as Normal in Section 16 of ED-14G / DO-160G or the revision level as agreed with the certification authority, the DC electrical power supply shall be within the limits specified as maximum and minimum in Section 16 of ED-14G / DO-160G or the revision level as agreed with the certification authority. The electrical power supply used shall be essentially free from modulation, ripple, interruptions and surges. In the case of equipment designed for operation from an AC power source of variable frequency, unless otherwise specified, tests should be performed at representative input power frequencies with the input frequency adjusted to within 5% of a selected frequency. 

## Iv-3.2 Recorder Minimum Performance Levels

The recorder shall be designed to meet and shall be tested to show compliance with the following Minimum Performance Levels. 

NOTE: 
Where these paragraphs state requirements regarding the signal in the recording medium, it should be interpreted as that observed at the output of the data retrieval equipment specified by the equipment manufacturer.  

## Iv-3.2.1 Start Up And Effects Of Power Interruptions

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
Following a system electrical power interruption the characteristics of the data link recorder system (including any dedicated networks, busses etc) shall be as described in the following table.  

| Recording Requirement                             | Power    |
|---------------------------------------------------|----------|
| Interruption                                      |          |
|                                                   |          |
| Interruption                                      |          |
| Duration                                          |          |
|                                                   |          |
| Initial Power                                     |          |
| Level                                             |          |
|                                                   |          |
| Cold Start                                        |          |
|                                                   |          |
| >2s                                               |          |
|                                                   |          |
| No Power                                          |          |
|                                                   |          |
| Following initial application of power to the     |          |
| recorder system, the system shall be capable of   |          |
| recording information in the recording medium     |          |
| as soon as possible but no later than 10s. Any    |          |
| built-in test function shall be completed within  |          |
| 60s.                                              |          |
|                                                   |          |
| For interruptions with a duration of 200ms to 2s, |          |
| the                                               | recorder |
| Warm                                              |          |
| Restart                                           |          |
|                                                   |          |
| Within 200ms                                      |          |
| to 2s                                             |          |
|                                                   |          |
| Normal,                                           |          |
| Abnormal,                                         |          |
| and                                               |          |
| Emergency                                         |          |
|                                                   |          |
| commence storing information, in the recorder     |          |
| medium, as soon as possible but no later than     |          |
| 500ms after power is restored. Any built-in test  |          |
| function shall recover within 5s(2).              |          |
|                                                   |          |
| Transient                                         |          |
|                                                   |          |
| 0 to 200ms                                        |          |
|                                                   |          |
| Normal                                            |          |
|                                                   |          |
| Interruptions with a duration of 0 to 200ms shall |          |
| have no effect on the recorder system.            |          |
|                                                   |          |
| Power Down                                        |          |
|                                                   |          |
| > 200ms                                           |          |
|                                                   |          |
| Normal                                            |          |
|                                                   |          |
| All information available at the start of an      |          |
| interruption together with that available in the  |          |
| following 200ms shall be recorded in the crash-   |          |
| protected recording medium.                       |          |
|                                                   |          |

NOTE 1: 
The recording of data should commence immediately when data is available. 
NOTE 2: 
Any built-in test function may take up to 5s to recover. The recovery period of 5s is intended to permit power-up test and system initialization routines to be performed. It is recommended that such routines should be performed as rapidly as possible to minimize the recovery period. 
NOTE 3: 
No constraint is intended to be placed on maintenance actions associated with setting the initial configuration status of the system following equipment replacement. 

## Iv-3.2.2 Standard Message

A standard message is defined as 103 ASCII characters (or equivalent) of payload at the input to the recorder. Protocol or overhead required to identify the message during playback shall also be processed and stored. An example of required header/protocol information is the time stamp added to the message prior to it being sent to the recorder. 

## Iv-3.2.3 Recording Delay

For a standard message (as defined in paragraph IV-3.2.2) the delay in recording the data, from the time of reception of the complete message at the recording device to the time of recording in the crash-protected medium, shall not exceed 250 milliseconds. 
NOTE 1: 
For a message with a larger payload than the standard message or a burst of messages the delay may exceed the limit of 250 milliseconds. 
NOTE 2: 
It is important to preserve all available data. For this reason, any delay should be minimised. Where buffer devices are used, it is strongly recommended that non-volatile devices are used and that they are located within the crash-protected module. 
 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Iv-3.2.4 System Applications Delays

For a standard message (as defined in paragraph IV-3.2.2), the delay between the message being recognized as data to be recorded and the last bit being presented at the recording device shall not exceed 2 seconds. 

In any case, for a message of any length, the delay between the message being recognized as data to be recorded and the first bit being presented at the recording device shall not exceed 2 seconds. 

## Iv-3.2.5 Synchronisation Of Audio And Digital Message Recordings

The recordings on the data link recorder shall be synchronised to other airborne recordings as defined in paragraph 2-1.11 

## Iv-3.2.6 Recording Capacity

The recorder shall, as a minimum, provide sufficient capacity to store 5 standard messages per minute and each followed by an acknowledgement message of 28 characters (in addition to any protocol overhead as required to meet this specification), 
for a duration as specified in paragraph 2-1.11.  
NOTE 1: 
This requirement is derived from a perceived maximum of current CPDLC traffic and message sizes. It is based on the assumption that 60 percent of the recording capacity will be used for CPDLC messages, and the remaining 40 percent for other types of messages.  
NOTE 2: 
Today's definition of data link architectures do not provide enough 
information on the amount of anticipated or typical data flow and as such it is suggested that sufficient reserve shall be provided for system growth. 
NOTE 3: 
In order to minimise recording medium utilisation and to optimise recording medium capacity, data link messages may be recorded on an interrupt basis, i.e. as the message occurs. 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Iv-3.2.7 Short-Term Maximum Throughput

The recorder shall continue to operate in accordance with the other requirements of this chapter when it receives a burst of six consecutive message pairs at the interface's maximum possible input data transfer rate, with an interval of one minute between such bursts. These message pairs shall be as defined in paragraph IV-3.2.6 (Recording Capacity).  

## Chapter Iv-4 Minimum Performance Specifications Under Environmental Test Conditions Iv-4.1 Introduction

CHAPTER 2-3 of this document defines the environmental tests to be performed on the recorder system. Compliance with the applicable performance requirements of this part for data link Recorder shall be demonstrated as shown in Table VI-1.. 

## Iv-4.2 Exceptions To General Requirements

There are no exceptions to the general requirements defined in paragraph 2-3.2 for data link recording systems. 

 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

|                                                             |              |          | ENVIRONMENT    |         | MOPS PARAGRAPH NUMBER    |
|-------------------------------------------------------------|--------------|----------|----------------|---------|--------------------------|
| 2-1.6                                                       | IV-3.2.1     | IV-3.2.3 | IV-3.2.4       | 4-1.3.2 | 2-1.12                   |
| System                                                      |              |          |                |         |                          |
| NORMAL                                                      | Power        |          |                |         |                          |
| Applications                                                | Cross-Talk   |          |                |         |                          |
| Timebase                                                    |              |          |                |         |                          |
| OPERATION                                                   | Interruption |          |                |         |                          |
| Recording Delay                                             |              |          |                |         |                          |
| Characteristics                                             |              |          |                |         |                          |
| Delay                                                       |              |          |                |         |                          |
| Temperature                                                 | 1            | R        | R              | R       |                          |
| Altitude                                                    | 2            | R        |                |         |                          |
| Temp Variation                                              | 3            | R        |                |         |                          |
|                                                             |              |          |                |         |                          |
| Humidity                                                    | 4            | R        |                |         |                          |
| Shock                                                       | 5 and 6      | R        |                |         |                          |
| Vibration                                                   | 7            | R/E      |                |         |                          |
| Power Input                                                 | 15           | R        |                |         |                          |
| Voltage Spike                                               | 16           | R        |                |         |                          |
| AF Susceptibility                                           | 17           | R        |                |         |                          |
| Induced                                                     |              |          |                |         |                          |
| Susceptibility                                              |              |          |                |         |                          |
| 18                                                          |              |          |                |         |                          |
| R                                                           |              |          |                |         |                          |
| RF Susceptibility                                           | 19           | R        |                |         |                          |
| Lightning                                                   | 21           | R        |                |         |                          |
|                                                             | Key          |          |                |         |                          |
| Blank = Manufacturer's                                      |              |          |                |         |                          |
| Discretion      E = Exceptions apply      R = Test Required |              |          |                |         |                          |
|                                                             |              |          |                |         |                          |

## Chapter Iv-5 Test Procedures Iv-5.1 Introduction

This chapter specifies the standard test procedures for demonstrating compliance with CHAPTER IV-3. Although specific test procedures are cited, it is recognised that they will not apply in all cases and that other methods may be preferred or required. Alternative methods may be used if the manufacturer can show that they provide equivalent certification data. Where a test procedure is not specified for a particular characteristic, the manufacturer may show compliance either by analysis or by devising a test appropriate to the equipment design. The verification procedure of On Board Recording Performance shall test that the data link data defined in this document is recorded correctly on board and can be retrieved to the requirements of this specification. 

## Iv-5.1.1 Adjustment Of Equipment

The equipment under test shall be properly aligned and adjusted in accordance with the manufacturer's recommendations. 

## Iv-5.1.2 Test Instrument Precautions

Precautions shall be taken to prevent the introduction of errors resulting from impedance mismatch and the improper connection of test instruments to the equipment under test. 

## Iv-5.1.3 Test Conditions

Unless otherwise stated, the test procedures of this chapter apply to systems with digital processing inputs and digital processing outputs. Where parts of the system use analogue processing, the test procedure assumes that conversion equipment appropriate to the recorded information and which match the performance characteristics of the system to be certified are used. All tests shall be performed under the conditions defined in paragraph IV-3.1. 

## Iv-5.1.4 Connected Loads

Unless otherwise specified, all tests shall be performed with the equipment connected to loads having the impedance values for which it is designated. 

## Iv-5.1.5 Recording Of Test Results

Except where tests are GO/NO GO in character the actual numerical values obtained for each of the parameters tested shall be recorded in a qualification test report. 

## Iv-5.2 Electrical Test Procedures Iv-5.2.1 Continuity Of Recording (Paragraph Iv-2.1.5)

It shall be verified, that all data link messages will be recorded continuously since the electrical power is applied to the system and the start logic is satisfied. a. 
Equipment Required: Data link message transfer simulation Basic simulation of start/stop conditions Readout Tool 
b. 
Measurement Procedure: i. 
Apply power to the recording system,  
ii. 
Set the starting conditions to true,  
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

iii. 
Start the message transfers simulation, 
iv. 
Record for the duration as defined in paragraph IV-2.1.7 
v. 
Set the stop conditions to true,  
vi. 
Readout the recorded data,  
vii. 
Compare the recorded data with the data simulated. 
All simulated data shall be recorded completely between Start/Stop conditions. 

## Iv-5.2.2 Effects Of Power Interruptions (Paragraph Iv-3.2.1)

It shall be verified that the requirements according to effects on power interruptions defined under paragraph IV-3.2.1are fulfilled. a. 
Equipment Required: Power Interrupt Generator Data link message transfer simulation Basic simulation of start/stop conditions Readout Tool 
b. 
Measurement Procedure: 
i. 
Power Interrupt of 200 milliseconds under normal power level A. 
Apply power to the recording system,  
B. 
Set the starting conditions to true,  
C. 
Start the message transfer simulation,  
D. 
Perform power interrupt of 200 milliseconds 
E. 
Set the stop conditions to true,  
F. 
Readout the recorded data,  
G. 
Compare the recorded data with the data simulated. 
The data recorded shall be identical with the data simulated. 

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

ii. 
Power Interrupt of more than 200 milliseconds under abnormal and emergency power level A. 
Equip abnormal or emergency power to the recording system,  
B. 
Set the starting conditions to true,  
C. 
Start the message transfer simulation,  
D. 
Perform power interrupt of more than 200 milliseconds 
E. 
Set the stop conditions to true,  
F. 
Readout the recorded data,  
The data recorded shall be identical with the data simulated. The system shall recover and commence storing information within 250 milliseconds after the power is restored. The data recorded before the power interrupt and 250 milliseconds after power recovery shall be identical with the data simulated.  

## Iv-5.2.3 Test Of Delays (Paragraph Iv-3.2.3)

a. 
Equipment Required: Data link message transfer simulation Basic simulation of starting conditions Readout Tool Logic Analyser or equivalent time measurement equipment 
b. 
Measurement Procedure: The delay between the recorder input and recording shall be tested. i. 
Apply power to the recording system,  
ii. 
Set the starting conditions to true,  
iii. 
Start the message transfer simulation with a standard message (as defined in paragraph IV-3.2.2.  
iv. 
Measure time between the complete reception of the message at the recording device and the recording in the crash-protected recording medium for each character by use of the logic analyser 
v. 
Set the stop conditions to true. 
It shall be verified that the maximum time delay between the complete reception of the message at the recording device and the recording of the message in the crashprotected medium does not exceed the figure as defined in paragraph IV-3.2.3. 

## Iv-5.2.4 System Applications Delay (Paragraph Iv-3.2.4)

NOTE: 
         This test is applicable to the airborne data link system and is outside this 
         scope of this chapter. Consequently, it will be implemented at the system 
         level only. 

## Iv-5.2.5 Recording Duration / Capacity (Paragraph Iv-3.2.6)

It shall be verified that the recording medium capacity is sufficient to store the digital messages specified in paragraph IV-3.2.6. Subsequent playback of messages shall verify that the full test format was recorded. a. 
Equipment Required: 
Data link message transfer simulator Basic simulation of start/stop conditions Readout Tool 
b. 
Measurement Procedure: i. 
Apply power to the recording system, 
ii. 
Set up the message simulator in accordance with the scenario as specified in paragraph IV-3.2.6. 
iii. 
Set the starting conditions to true,  
iv. 
Start the message transfers simulator, 
v. 
Continue simulation for duration as specified in paragraph IV-2.1.7 
vi. 
Set the stop conditions to true,  
vii. 
Readout the recorded data,  
viii. 
Compare the recorded data with the data simulated. 
It shall be verified that all simulated data has been recorded. 

## Iv-5.2.6 Short Term Maximum Throughput (Paragraph Iv-3.2.7)

It shall be verified that when a burst of data messages at the maximum burst throughput of paragraph IV-3.2.7 rate is sent to the recorder, all messages can be recovered as specified in paragraph IV-3.2.7. 
a. 
Equipment Required: Data link message transfer simulator Basic simulation of start/stop conditions Readout Tool 
b. 
Measurement Procedure Apply power to the recording system, i. 
Set simulator for the maximum message transfer rate  
ii. 
Set the starting conditions to true,  
iii. 
Start the message transfers simulator, 
iv. 
Continue simulation for the period of time specified in paragraph IV-3.2.7 
v. 
Set the stop conditions to true,  
vi. 
Readout the recorded data,  
vii. 
Compare the recorded data with the data simulated. 
It shall be verified that all simulated data shall be recorded completely between Start/Stop conditions. 

## Iv-5.2.7 Bit Error Rate (Paragraph 2-1.7)

It shall be verified that the bit error rate arising from differences between the input and 
the retrieved data caused by corruption of the data during processing, recording and retrieval does not exceed the specification in paragraph 2-1.7. a. 
Equipment Required: Data link message transfer simulator Basic simulation of start/stop conditions Readout Tool 
b. 
Measurement Procedure: i. 
Apply power to the recording system, 
ii. 
Set up the message simulator to generate test data 
iii. 
Set the starting conditions to true, 
iv. 
Start the message transfers simulation, 
v. 
Continue simulation for duration as specified in paragraph IV-2.1.7  
vi. 
Set the stop conditions to true, 
vii. 
Readout the recorded data, 
viii. 
Verify bit errors in recovered data are within allowance of paragraph 2-1.7. 
All simulated data shall be recorded completely between Start/Stop conditions. 

## Iv-5.2.8 Time Base Characteristics (Paragraph 2-1.12)

It shall be verified that the time base used in the recording of the digital messages is stable to the specification of paragraph 2-1.12. a. 
Equipment Required: Data link message transfer simulator Basic simulation of start/stop conditions Readout Tool 
b. 
Measurement Procedure: i. 
Apply power to the recording system, 
ii. 
Set up the message simulator to generate accurately timed message intervals  
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

iii. 
Set the starting conditions to true,  
iv. 
Start the message transfers simulation, 
v. 
Continue simulation for duration as specified in paragraph IV-2.1.7 
vi. 
Set the stop conditions to true,  
vii. 
Readout the recorded data,  
viii. 
Verify all recovered messages meet the overall time base stability characteristics specified in paragraph 2-1.12. 
It shall be verified that all simulated data shall be recorded completely between Start/Stop conditions. 

## Iv-5.2.9 Monitoring Of Proper Operation

It shall be verified that the aural or visual means of pre-flight checking works as specified to ensure the digital message recorder is functioning correctly. a. 

Equipment Required: Data link message transfer simulator Basic simulation of start/stop conditions Readout Tool 

b. 
Measurement Procedure: The following events shall lead to aural or visual indications: i. 
loss of system electrical power, Test sequence:  shut down system electrical power 
 
recorder system shall produce failure indication output 
ii. 
failure of the digital interface within the recorder, Test sequence:  simulate failure of the digital interface 
recorder system shall produce failure indication output 
iii. 
failure of the recording medium, Test sequence:  simulate failure in the recording medium 
recorder system shall produce failure indication output 
iv. 
failure of the recorder to store the information in the recording medium as shown by checks of the recording, Test sequence:  simulate failure in recording medium 
recorder system shall produce failure indication output 
v. 
removal of the recorder or any other item of this equipment from the aircraft. Test sequence:  remove recorder, run recording system without recorder 
recorder system shall produce failure indication output 
To prove the correct indication in the a/c cockpit the tests have to be repeated under real a/c conditions.  

## Iv-5.2.10 Data Retrieval Characteristics (Paragraph Iv-2.2.1)

a. 
Equipment Required: Data link message transfer simulation Basic simulation of start/stop conditions Readout Tool Data analysis tool and software (replay equipment) 
b. 
Measurement Procedure: i. 
Apply power to the recording system,  
ii. 
Set the starting conditions to true,  
iii. 
Start the message transfers simulation,  
iv. 
Set the stop conditions to true,  
v. 
Readout the recorded data,  
vi. 
Compare the recorded data with the simulated data. 
vii. 
Repeat this procedure  
Check that all recorded data of an undamaged, fully serviceable recording medium can be retrieved. Check that for an undamaged, fully serviceable recording medium with a corrupted record all data can be retrieved, including the corrupted record. Check that the data is not altered, degraded or overwritten after the first download. Check that the chronological order of the messages is maintained during replay. 

--```,,`,````,`,,,``,,```,,

## Chapter Iv-6 Equipment Installation And Installed Performance Iv-6.1 Introduction

The purpose of this chapter is to test the installed Airborne system with all message types employed in Communications, Navigation, and Surveillance. Installed performance criteria are generally the same as those contained in CHAPTER IV-3, which were verified through bench and environmental tests. However, certain performance parameters may be affected by the physical installation and can only be confirmed after installation. Following the testing of each new data link Recorder System installation, the recording so obtained shall be evaluated to confirm adequate message recording accuracy and synchronisation with other recording devices both on the aircraft and on the Ground.  
Similarly it will be necessary to evaluate recording obtained from in-service flying to ensure this accuracy is maintained and the system has sufficient capacity to preserve all messages received over the required recording duration. 

NOTE: 
The Recording Performance Test can be conducted in a laboratory environment and/or in the real aircraft environment 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
The purpose of this section is to test the installed Airborne system with all message types employed in Communications, Navigation, and Surveillance. An analysis shall be performed by the equipment installer to identify the "subsystems" where the serviceability or accuracy could be degraded and remain undetected. Maintenance tasks shall take account of this analysis by requiring the appropriate calibration checks at suitable intervals. During introduction to service of a new component in the airborne data link system, in order to test the correct operation of the overall recording system, a scenario has to be developed. In the course of the scenario, one or more procedures, involving the flight crew of an aircraft, a ground station such as an ATC centre (or a simulation thereof) should be exercised. There may be benefit in performing the test twice, once with an ATM centre and once with a non-ATM centre. A complete test scenario consists of three test domains a. 

Aircraft Recording Domain 

b. 
Ground Recording Domain (or simulation) 
c. 
Correlation of Recording Domains (overall end-to end) 

NOTE: 
         It shall not be required to test the data link technology itself. The data link 
         establishment, test and approval are described in the EUROCAE 
         document ED-78A / RTCA document DO-264. The test procedures shall 
         focus on the data link overall recording system comprising on board 
         recording, ground recording and correlation of both recording domains.  

NOTE: 
The Recording Performance Test can be conducted in a laboratory environment and/or in the real aircraft environment. 

The verification of a communication data recording shall be done in order to correlate the message flows between both parts. 

ƒ 
on the aircraft and  
ƒ 
simultaneously on the Ground 
It shall be verified that 

ƒ 
the actual or deduced message content for airborne recording is correct (through comparison with ground recordings or equivalent means) 
ƒ 
a synchronisation with a common time base is possible  
ƒ 
the reconstitution of message sequences in the scenario is possible  

## Note: Standardisation Of Recording Formats May Make Automatic Correlation Of These Messages Possible.

A test procedure shall include following activities: 
a. 
send messages (different types) from the Ground equipment to the aircraft and vice versa 
b. 
perform the communication on the aircraft and on the Ground (both digital message generation and voice commenting) in order to be able to correlate voice and data communication 
c. 
retrieve the data after the test from the aircraft recording system on ground 
d. 
check airborne recording (e.g. through the ground recording) and confirm the integrity of on board data 

NOTE: 
        It is recommended that anyone operating an aircraft equipped with the 
        data link technology shall have the possibility to obtain an audit to recover 
        data link messages from their network provider. The operator may ensure 
        this by requesting a data recovery of all available data link messages for 
        a single randomly selected flight. The recommended frequency is once 
        per year. This procedure will ensure to identify any deficiencies in the 
        service provider's capabilities. 

## Iv-6.2 Equipment Installation Iv-6.2.1 Interface Design

Reserved. 

## Iv-6.3 Ground Test Procedures Iv-6.3.1 General

This section provides guidance for ground testing the initial installation of a unique system in aeroplanes. It may need to be adapted to suit the particular installation being tested and to comply with operating regulations. Each unique recorder system shall be ground tested and the recording so obtained, shall be evaluated to show adequate recording quality during all test conditions. The replay and evaluation shall be performed by a replay centre acceptable to the Certification Authority.  

## Iv-6.3.2 Downlink (From Aircraft)

a. 
Send a standard message (as defined in paragraph IV-3.2.2) to an ATC centre. 
b. 
Note content of message and time message was sent. 
c. 
With an available selection of several messages on the Data Entry Panel, select the messages randomly (i.e. Read, Skip, Delete, Store, Recall etc.). 
d. 
Note message selected, activity, and time when selected. 
e. 
Verify the airborne recording meets requirements of paragraphs IV-3.2.3 and IV-3.2.4. 
f. 
Verify airborne and ground recording message content, and time stamps correspond to those noted in b) and d). 
g. 
Repeat a) through f) using a non-ATC centre. 

## Iv-6.3.3 Uplink (To Aircraft)

a. 
Send a standard message (as defined in paragraph IV-3.2.2) to the aircraft from an ATC centre 
b. 
Note content of message and time message was sent 
c. 
On the aircraft using the Data Entry Panel select the message uplinked to the aircraft (i.e. Read, Skip, Delete, Store, Recall etc.). 
d. 
Note message selected, content, activity, and time when selected. 
e. 
Verify the airborne recording meets requirements of paragraphs IV-3.2.3 and 
IV-3.2.4. 
f. 
Verify airborne and ground recording message content, and time stamps correspond to those noted in b) and d). 
g. 
Repeat a) through f) using a non-ATC centre. 

## Iv-6.3.4 Conformity Inspection

a. 
Visually inspect the installed equipment to determine the use of acceptable workmanship and engineering practices. 
b. 
Verify that proper mechanical and electrical connections have been made and that the equipment has been located and installed in accordance with the requirements and the manufacturer's recommendations. 

## Iv-6.3.5 Equipment Function

Vary all controls of the equipment through their full range to determine that the equipment is operating according to the manufacturer's instructions and that each control performs its intended function. 

## Iv-6.3.6 Interference Effects

a. 
With the recording equipment in normal and standby operation, operate other electrically operated aircraft equipment and systems to determine that no significant levels of conducted or radiated interference exist. 
b. 
Evaluate all combinations of control settings and operating modes. 
c. 
Operate communication and navigation equipment on the low, high and at least one mid-band frequency. 
d. 
Identify systems or modes of operation that should be evaluated during flight. 
e. 
If appropriate, repeat the tests using emergency power with the aircraft's batteries alone and any standby inverters operating. 

## Iv-6.3.7 Power Supply Fluctuations And Protection

a. 
Under normal aircraft conditions, cycle the aircraft engine(s) through all normal power settings and verify the proper operation of the equipment. 
b. 
Isolate the electrical supply to the recording system by means of the protective devices provided (e.g. circuit breakers) and verify that the equipment is off. 

## Iv-6.4 Flight Test Procedures

This procedure assumes that a complete system test of the data link aircraft installation has been successfully conducted. If an on-board printer is available, print all Uplinks and Downlinks for correlation and verification with the Crash Recording records. If the requirements have been successfully demonstrated during ground testing a flight test may not be necessary 

## Iv-6.4.1 General

a. 
This section provides guidance for flight testing the initial installation of a unique system in aeroplanes. It may need to be adapted to suit the particular installation being tested and to comply with operating regulations. 
b. 
Each unique recorder system shall be flight tested and the recording so obtained shall be evaluated to show adequate recording quality during all normal regimes of flight including taxiing, take-off, cruise, approach and landing. 
c. 
The replay and evaluation shall be performed by a replay centre acceptable to the Certification Authority.  

## Iv-6.4.2 Downlink (From Aircraft)

a. 
Send a standard message (as defined in paragraph IV-3.2.2) to an ATC centre. 
b. 
Note content of message and time message was sent. 
c. 
With an available selection of several messages on the Data Entry Panel, select the messages randomly (i.e. Read, Skip, Delete, Store, Recall etc.). 
d. 
Note message selected, activity, and time when selected. 
e. 
Verify the airborne recording meets requirements of paragraphs IV-3.2.3 and IV-3.2.4. 
f. 
Verify airborne and ground recording message content, and time stamps correspond to those noted in b) and d) 
g. 
Repeat a) through f) using a non-ATC centre. 

## Iv-6.4.3 Uplink (To Aircraft)

a. 
Send a standard message (as defined in paragraph IV-3.2.2) to the aircraft from an ATC centre 
b. 
Note content of message and time message was sent 
c. 
On the aircraft using the Data Entry Panel select the message uplinked to the aircraft (i.e. Read, Skip, Delete, Store, Recall etc.). 
d. 
Note message selected, content, activity, and time when selected. 
e. 
Verify the airborne recording meets requirements of paragraphs IV-3.2.3 and IV-3.2.4. 
f. 
Verify airborne and ground recording message content, and time stamps correspond to those noted in b) and d). 
g. 
Repeat a) through f) using a non-ATC centre. 

## Iv-6.5 Post Flight Evaluation Of Recordings Iv-6.5.1 Introduction

Following the flight testing of each new recorder system installation, the recording so obtained shall be evaluated to confirm adequate quality. 

## Iv-6.5.2 Replay Equipment

Means should be provided to retrieve and decode recorded messages obtained via a digital data link. Similarly a means to retrieve timing signals should be provided. 

## Iv-6.5.3 Recording Evaluation

Proper recording of a data link message should be verified and correlated to announcements recorded by the flight crew. 

## Iv-6.5.4 Verification Of Ground Recording Performance

The Verification of Ground Recording Performance is out of the scope of this document. 

## Iv-6.5.5 Test Report

The report may be supplemented by printing evidence obtained from selected extracts of the recording. The spaces on the report should, as applicable, be annotated with brief comments on the replay signal quality. 

 
 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## Annex Iv-A Data Link Recording Table Iv-A.1 Data To Be Recorded

The material in Annex IV-A and the Table IV-A.1 is to be considered as guidance material only and as a means of compliance with the MASPS ED-93. Table IV-A.1 lists the function and states if the appropriate data shall be recorded. The minimum list of applications and services to be recorded is provided by IV-2.1.6.1. The content of messages are required by paragraph IV-2.1.6.1.  

## Table Iv-A.1: Data Link Recording Requirements

| Item                                                     | Air Traffic      | Air Traffic Service Description    | Recording                                                   |
|----------------------------------------------------------|------------------|------------------------------------|-------------------------------------------------------------|
| No.                                                      | Service Type     | content                            |                                                             |
| C                                                        | 1                | Data link Initiation               | This includes any applications used to logon to or initiate |
| data link service. In FANS-1/A and ATN, these are ATS    |                  |                                    |                                                             |
| Facilities Notification (AFN) and Context Management     |                  |                                    |                                                             |
| (CM) respectively.                                       |                  |                                    |                                                             |
| 2                                                        | Controller/Pilot | C                                  |                                                             |
| Communication                                            |                  |                                    |                                                             |
| This includes any application used to exchange requests, |                  |                                    |                                                             |
| clearances, instructions and reports between the flight  |                  |                                    |                                                             |
| crew and controllers on the ground. In FANS-1/A and ATN, |                  |                                    |                                                             |
| this includes the CPDLC application.                     |                  |                                    |                                                             |
| It also includes applications used for the exchange of   |                  |                                    |                                                             |
| oceanic (OCL) and departure clearances (DCL) as well as  |                  |                                    |                                                             |
| data link delivery of taxi clearances.                   |                  |                                    |                                                             |
| 3                                                        | Addressed        | C                                  |                                                             |
| Surveillance                                             |                  |                                    |                                                             |
This includes any surveillance application in which the ground sets up contracts for delivery of surveillance data. In FANS-1/A and ATN, this includes the Automatic Dependent Surveillance (ADS-C) application. Where parametric data are reported within the message they shall be recorded unless data from the same source are recorded on the FDR. 
C 
4 
Flight Information 
This includes any service used for delivery of flight information (endorsed by Air Traffic Service Providers, not via AOC) to specific aircraft. In ATN, this includes the FIS application (D-OTIS, which provides D-METAR, D-ATIS, D-NOTAM and other textual data link services). 
5 
Aircraft Broadcast 
M * 
Surveillance 
This includes Elementary and Enhanced Surveillance Systems, as well as ADS-B output data. Where parametric data sent by the aeroplane are reported within the message they shall be recorded unless data from the same source are recorded on the FDR. 
6 
Aeronautical 
M * 
Operational 
Control Data 
This includes any messages transmitting or receiving data used for AOC purposes (per the ICAO definition, refer paragraph 1.1.5.1).  

## Note: C: Complete Contents Recorded

M: 
Information that enables correlation to any associated records stored separately from the aeroplane. 
*: 
 Applications to be recorded only as far as is practicable given the architecture 
of the system. 

## Annex Iv-B Maintenance Practices Iv-B.1 General

The maintenance practices contained in this annex are intended to ensure continued serviceability of DLR systems and are intended as guidance for OEMs and DLR system STC applicants in the creation of maintenance practices for their systems. The maintenance tasks required to ensure the continued serviceability of the installed DLR system will depend on the extent of monitoring built into the DLR system. The installer shall perform an analysis of the DLR system to identify those parts of system which, if defective, would not be readily apparent to the flight crew or maintenance personnel. Appropriate inspections and functional checks, together with the intervals at which these would need to be performed, need to be established as indicated by the analysis. 

The specified checks need to include verification of system performance, where appropriate. Maintenance procedures should emphasise the need to preserve the recording following a reported incident. The equipment needs to include a continuous and exhaustive monitoring of the data link recording function (e.g. by continuous BITE) that provides failure messages to the aircraft maintenance system or to the cockpit information system (usually warning display). If such a monitoring cannot be implemented, then a data link recording download and analysis shall be performed at intervals of no greater than two years, or up to a maximum of four years if approval from the appropriate regulatory authority has been obtained at the time of certification of the type for DLR systems that have a demonstrated high integrity of serviceability self-monitoring. Any inspection or test requirements specified by equipment manufacturers shall be observed, e.g. battery checks of the underwater location beacon. 

## Iv-B.2 Recording Evaluation

An in-flight recording should be replayed and assessed for integrity. Paragraph IV-6.5 provides guidance for the evaluation of such recordings. Data link recorder systems should be considered unserviceable if the recording duration is less than required, if one or more messages are corrupted or not recorded. 

## Iv-B.3 Primary Maintenance Tasks

Table IV-B.1 shows the primary maintenance tasks for the installed DLR system. Inspection periods should be established on the basis of the DLR system analysis discussed in paragraph IV-B.1. 

| Item                                    | Equipment                          | Task                                | Maximum Interval    | Interpretation    |
|-----------------------------------------|------------------------------------|-------------------------------------|---------------------|-------------------|
| Confirm correct recording of digital    |                                    |                                     |                     |                   |
| data link messages:                     |                                    |                                     |                     |                   |
| 1                                       | DLR System                         | Check in                            |                     |                   |
| accordance                              |                                    |                                     |                     |                   |
| with criteria                           |                                    |                                     |                     |                   |
| and                                     |                                    |                                     |                     |                   |
| procedures                              |                                    |                                     |                     |                   |
| agreed with                             |                                    |                                     |                     |                   |
| the Regulatory                          |                                    |                                     |                     |                   |
| Authority                               |                                    |                                     |                     |                   |
| Two years, or up to a                   |                                    |                                     |                     |                   |
| maximum of four                         |                                    |                                     |                     |                   |
| years if approval from                  |                                    |                                     |                     |                   |
| the appropriate                         |                                    |                                     |                     |                   |
| regulatory authority                    |                                    |                                     |                     |                   |
| has been obtained for                   |                                    |                                     |                     |                   |
| DLR systems that                        |                                    |                                     |                     |                   |
| have a demonstrated                     |                                    |                                     |                     |                   |
| high integrity of                       |                                    |                                     |                     |                   |
| serviceability self-                    |                                    |                                     |                     |                   |
| monitoring                              |                                    |                                     |                     |                   |
| Within the last 90 minutes of a         |                                    |                                     |                     |                   |
| designated flight, have the flight crew |                                    |                                     |                     |                   |
| speak out at least three data link      |                                    |                                     |                     |                   |
| messages sent and at least three data   |                                    |                                     |                     |                   |
| link messages received. After the       |                                    |                                     |                     |                   |
| flight, read out the DLR and the CVR    |                                    |                                     |                     |                   |
| and check that the recorded data link   |                                    |                                     |                     |                   |
| messages are consistent with the        |                                    |                                     |                     |                   |
| CVR recording.                          |                                    |                                     |                     |                   |
| 2                                       | DLR                                | Check/Replay Not exceeding interval |                     |                   |
| stated by the vendor                    |                                    |                                     |                     |                   |
| Remove recorders for inspection and     |                                    |                                     |                     |                   |
| test as required by the Component       |                                    |                                     |                     |                   |
| Maintenance Manual.                     |                                    |                                     |                     |                   |
| NOTE:                                   |                                    | The recording stored on             |                     |                   |
| the media prior to the                  |                                    |                                     |                     |                   |
| removal                                 | should                             | be                                  |                     |                   |
| evaluated.                              |                                    |                                     |                     |                   |
| Not exceeding 24                        |                                    |                                     |                     |                   |
| months elapsed time                     |                                    |                                     |                     |                   |
| Confirm proper sensor function. Test    |                                    |                                     |                     |                   |
| may be performed in-situ if practical.  |                                    |                                     |                     |                   |
| 3                                       | Ditching                           |                                     |                     |                   |
| Sensor                                  |                                    |                                     |                     |                   |
| (Helicopter)                            |                                    |                                     |                     |                   |
| Check/                                  |                                    |                                     |                     |                   |
| Functional                              |                                    |                                     |                     |                   |
| Test                                    |                                    |                                     |                     |                   |
| 4                                       | Crash Sensor                       |                                     |                     |                   |
| (where fitted)                          |                                    |                                     |                     |                   |
| As stated by vendor                     | Comply with instructions issued by |                                     |                     |                   |
| vendor                                  |                                    |                                     |                     |                   |
| Check/                                  |                                    |                                     |                     |                   |
| Functional                              |                                    |                                     |                     |                   |
| Test                                    |                                    |                                     |                     |                   |
| 7                                       | Underwater                         |                                     |                     |                   |
| Locator Beacon                          |                                    |                                     |                     |                   |
| As stated by vendor                     | Comply with instructions issued by |                                     |                     |                   |
| vendor                                  |                                    |                                     |                     |                   |
| Check/                                  |                                    |                                     |                     |                   |
| Functional                              |                                    |                                     |                     |                   |
| Test                                    |                                    |                                     |                     |                   |
|                                         |                                    |                                     |                     |                   |
|                                         |                                    |                                     |                     |                   |

--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---

## List Of Members Of Eurocae Wg-90 Chairman

PLANTIN DE HUGUES 
Philippe  
Bureau d'Enquêtes et d'Analyses (BEA) 

## Secretary

WEISS 
Jennifer L-3 Communications 
 

## Members

AIGOIN 
Guillaume EASA 
ALLEN 
Jonathan FedEx ANDERS 
Peter AIRBUS 
BERECZ 
Endre L-3 Communications BITTERLI 
Daniel Dassault Aviation BLAU 
Georges BFU 
BOAKES 
Steve GE Aviation Systems BORSARI 
Gregory FAA 
BOULANGER 
Chantal L-3 Communications BOWLES 
Gregory GAMA 
BUTTRICK 
Scott BayFirst Solutions LLC 
CALLE 
Ricardo Airbus military CASH 
Jim NTSB 
CHADLI 
Mohammed DGAC 
COLIN 
Michel AIRBUS 
CUSHMAN 
Anna FAA 
DALMOLIN 
Fabien CTS 
DARBY 
Bob Eurocontrol DE KOCK 
André ICAO 
DORAN 
Frank L-3 Communications ELLIOTT 
Jim GE Aviation Systems EPHRAIM 
Piet GE Aviation Systems FORTUNATO 
Tom Deloitte GIVINS 
Ted TSB 
GREWE 
Reinhold Cassidian HAREMZA 
Harry EASA 
HARPER 
Roger HONEYWELL 
HORNE 
Mike A.D. Aerospace Ltd HOWE-RYBERG 
Sandy HONEYWELL 
JAMES 
Richard AAIB 
KAUFMANN 
Ari DRS Technologies KELL 
kenneth ATSB  
KOLEV 
Denis RNC-Avionic KRAMAR 
Peter TSB 
LAM 
Sunny HKCAA 
LE BERRE 
Aude BEA 
LOZANO 
JuanCarlos IFALPA 
MALAGA 
Pedro Airbus military MARTINEC 
Dan ARINC 
NAHAPETIAN 
Armen Teledyne Controls NEEB 
Volkmar AIRBUS 
OSHLOPOV 
Dimitry RNC-Avionic PEREZ REDONDO 
Almudena Fomento PETERSON  
William GE Aviation Systems PITSCHEIDER 
Armin Eurocopter Germany POLITIS 
Elias  
NRC  
PRIVITERA 
Darren Flight Data Systems RIDGELY 
Tim Boeing ROE 
John Agusta/Westland ROHRBAUGH 
Nathan FAA 
SALDANA 
Daniel Airbus Military SCHICK 
Arthur Cassidian SCHMUTZ 
Tom L-3 Communications SEBAN 
Henri Eurocopter SHAVER 
Tim FAA 
SHEEHAN 
Stephen TSA 
SHOCRON CROITORU 
Ariel SEPLA 
SHU 
Ping CAST 
SMITH 
Everett Spiegare STEVENS 
Thomas L-3 Communications SWANSON 
Robert FedEx TAYLOR 
Stuart HR Smith group of companies TERRY 
Malcolm IFALPA 
THOMPSON 
Michael HONEYWELL 
TRIBHUVAN 
Pinaki GE Aviation Systems VAN DEN HEUVEL 
Blake DRS Technologies VERNA 
Brian FAA 
WAI 
George  
HKCAA 
WANG 
Peng CAAC 
WANKE 
Nickolas Flight Data Systems WEED 
Mike L-3 Communications WHITE 
Todd L-3 Communications WILLIS 
Geoffrey Penny & Giles ZAYKO 
Sergey MAK 
ZDUNICH 
Patrick NRC  

## Improvement Suggestion Form

[   ] 
Documentation error (Format, punctuation, spelling) 

[   ] 
Content error 
[   ] 
Enhancement or refinement 
--```,,`,````,`,,,``,,```,,,``,`-`-`,,`,,`,`,,`---
Rationale (Describe the error or justification for enhancement): Proposed change (Attach marked-up text or proposed rewrite): Please provide any general comments for improvement of this document:   

## Return Completed Form To:

EUROCAE Attention: Secretariat General 
102 rue Etienne Dolet 92240 Malakoff - France Email: eurocae@eurocae.net Fax: +33 (0) 1 40 92 79 30 