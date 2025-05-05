RTCA, Inc. 

1150 18th Street, NW, Suite 910 
Washington D.C. 20036 

# Minimum Operational Performance Standards (Mops) For Traffic Alert And Collision Avoidance System Ii (Tcas Ii) Hybrid Surveillance Change 1

 Prepared by: SC-147 
RTCA DO-300A  Change 1 December 15, 2015 
© 2015, RTCA, Inc. 

 
Copies of this document may be obtained from RTCA, Inc. 

1150 18th Street, NW, Suite 910 
Washington, DC 20036-4001, USA 
Telephone: 202-833-9339 
Facsimile: 202-833-9434 
Internet: www.rtca.org Please visit the RTCA Online Store for document pricing and ordering information. 

## Foreword



This report was prepared by Special Committee 147 (SC-147) and approved by the RTCA Program Management Committee (PMC) on December 15, 2015. RTCA, Incorporated is a not-for-profit corporation formed to advance the art and science of aviation and aviation electronic systems for the benefit of the public.  The organization functions as a Federal Advisory Committee and develops consensus-based recommendations on contemporary aviation issues. RTCA's objectives include, but are not limited to: 

 
Coalescing aviation system user and provider technical requirements in a manner that helps government and industry meet their mutual objectives and responsibilities; 
 
Analyzing and recommending solutions to the system technical issues that aviation faces as it continues to pursue increased safety, system capacity and efficiency; 
 
Developing consensus on the application of pertinent technology to fulfill user and provider requirements, including development of minimum operational performance standards for electronic systems and equipment that support aviation; and 
 
Assisting in developing the appropriate technical material upon which positions for the International Civil Aviation Organization and the International Telecommunication Union and other appropriate international organizations can be based. 
The organization's recommendations are often used as the basis for government and private sector decisions as well as the foundation for many Federal Aviation Administration Technical Standard Orders and several Advisory Circulars. Since RTCA is not an official agency of the United States Government, its recommendations may not be regarded as statements of official government policy unless so enunciated by the United States Government organization or agency having statutory jurisdiction over any matters to which the recommendations relate. 

## "Disclaimer"

 
This publication is based on material submitted by various participants during the SC approval process. Neither the SC nor RTCA has made any determination whether these materials could be subject to valid claims of patent, copyright or other proprietary rights by third parties, and no representation or warranty, expressed or implied is made in this regard.  Any use of or reliance on this document shall constitute an acceptance thereof "as is" and be subject to this disclaimer."     

## Executive Summary

 Change 1 to DO-300A provides additional requirements to help prevent spurious Resolution Advisories during transitions from passive to active surveillance.   The change includes: 

1. New requirements which ensure that there is no "residue" from ADS-B surveillance when a track 
transitions from passive to active surveillance. 
2. An optional requirement allowing a system to be designed to only perform hybrid surveillance for 
an intruder whose ADS-B OUT version is greater than or equal to 2. 
3. Appendix G is added demonstrating that the safety analysis in Appendix D still applies.  It 
documents that a TA and an RA will still be generated at the same time as a TCAS II system which does not use the hybrid surveillance techniques of this specification.  
4. Adopt the text from FAA TSO-C119d Appendix 2.  That appendix was created in response to 
comments received during the public comment phase for TSO-C119d.  FAA disposition of certain comments received during that review period necessitated creation of Appendix 2 to affect changes to certain sections of DO-300A. 

## Changes To Do-300A

 
(1.1) 
The changes to §2.2.6.2, §2.4.2.7, and §2.4.3 ensure that TCAS systems with hybrid surveillance will not generate spurious RAs as a result of ADS-B behavior (jumps, noise, offset) when 
transitioning from passive to active surveillance.   Any proposed new text will be highlighted in 
gray while text intended to be deleted will be marked with red strikethrough font.   Note: for section 2.4.3, only the updated table row is included in this change document. 

## 2.2.6.2 Active Surveillance Requirements

Established Mode S tracks under active surveillance **shall** be maintained as specified in Ref. A, §2.2.4.6.2.2.3 (Maintenance of Established Tracks).  

Note: The intent of this section is to establish that active Mode S tracking is performed 
as per Ref. A through the exclusive use of Mode S replies, not through the use of 
range and bearing derived from extended squitter (DF=17) reports.    
Note: Since there can be a significant offset (bias) between the calculated range 
derived from the Airborne Position Message and the measured range from interrogations, even for reports that meet the validation criteria, and since the calculated range may have a larger variance than the measured range, depending on the source of the position data, it is important not to mix these two sources of data in order to avoid problems with the tracked range and range 
rate.   
Note: Care should be taken to avoid large range rate transients when a track 
transitions from active to passive surveillance or vice versa.  One way to avoid a range rate transient during transitions between active and passive surveillance and vice versa would be to coast the range rate until both the position report used for the previous track update and the current position report are of the same 
type.   
If a track under active surveillance satisfies the modified hybrid surveillance criteria of §2.2.7.1.2, but has not been given a validation test as specified in §2.2.6.1.2, then each active interrogation required in Ref. A, §2.2.4.6.2.2.3 (Maintenance of Established Tracks) **shall** also be used as a validation interrogation as specified in §2.2.6.3, and any reply **shall** be subjected to the validation test. If the validation test succeeds, the track transitions to hybrid surveillance. 

Mode S surveillance **shall** be performed in such a way that a track **shall** not be dropped for a nominal transition from passive to active surveillance.  A nominal transition is defined as one in which qualification, validation, or revalidation tests passed successfully.  
Therefore, the range correlation window used during this transition **shall** be at least as large as the revalidation window.  

Note: The purpose of this requirement is to ensure that implementations of TCAS with 
passive surveillance do not drop and restart tracks or change track numbers on the same aircraft during normal transitions between passive and active 
surveillance.   
When transitioning a track from 'not Normal' (e.g. 5s update interval or passive surveillance)  to 'Normal' Surveillance Mode the Mode S Surveillance **shall** identify an intruder track as being in 'not Normal' Surveillance Mode until two active range measurements have been provided to the CAS logic tracker.  This will ensure that CAS does not use ADS-B passive position data for threat calculations. This requirement will prevent unnecessary advisories resulting from a passive to active surveillance transition.  Initial implementations of hybrid surveillance were susceptible to transients during the transition and generated unnecessary advisories. An equipment manufacturer may implement an alternate method of ensuring that ADS-B data does not impact the Collision Avoidance Logic in order to meet the above objective. 

The maximum delay from the time it is determined that an aircraft (that was passively tracked) has entered the active surveillance region to the time a track with active reply data is provided to the CAS subsystem **shall** not be more than 3 surveillance update intervals.  This requirement applies only to surveillance conditions where nominal active surveillance link margins exist. When a track transitions to active surveillance and active data does not correlate with both the predicted range and the predicted altitude of the track (previously updated with passive data), the track **shall** be dropped and a new track established based only on active data.  Only one track **shall** be presented to the CAS subsystem at any time for a given Mode S address.   A new track in this case implies a new track number so that all trackers are reset.  In this condition, under nominal link margin conditions, the timing requirements of the previous paragraph apply. Table 1 below illustrates the intent of these requirements with a scenario. 

| T                               | Surveillance Event      |
|---------------------------------|-------------------------|
| <0                              | Track outside active    |
| surveillance region;            |                         |
| tracked passively               |                         |
| SURVNO = X                      |                         |
| SURV_MODE = REDUCED             |                         |
| RFLG = TRUE                     |                         |
| Range derived from passive data |                         |
| SURVNO = X                      |                         |
| SURV_MODE = REDUCED             |                         |
| RFLG = FALSE                    |                         |
|                                 |                         |
| 0                               | Track within the active |
| surveillance region.            |                         |
| Active reply does not           |                         |
| correlate to predicted range    |                         |
| because of large difference     |                         |
| between active and passive      |                         |
| data.                           |                         |
| SURVNO = X                      |                         |
| SURV_MODE = REDUCED             |                         |
| RFLG = FALSE                    |                         |
|                                 |                         |
| 1                               | Active reply does not   |
| correlate to predicted range    |                         |
| because of large difference     |                         |
| between active and passive      |                         |
| data.                           |                         |
 
Although it did not correlate, active reply data is saved to restart the track. 
Although it did not correlate, active reply data is saved to restart the track. 
SURVNO = Y SURV_MODE = NORMAL RFLG = TRUE 
2 
Active reply does not correlate to predicted range because of large difference between active and passive 
data. 
 
Because the track did not correlate again, the existing track is dropped and a new 
track is presented to 
CAS logic using the saved reply data.  The reply data must meet the requirements of Ref. A for initializing a Mode S track. 

Note: The purpose of this requirement is to minimize the delay in generating an 
established active track in a case where an aircraft track that was being updated with passive data meets the criteria where it is required to be updated with active 
data (e.g. within the active surveillance region or failed validation).  Consider the case where the error is sufficiently large that the range correlation criteria for the track fails and the CAS logic will be presented with a coast (S.RFLG = FALSE).  In this case the Surveillance Mode will continue to be marked as not Normal (e.g. Reduced).  This requirement guarantees (under nominal link margin conditions) that the maximum time delay in transitioning to active 
surveillance and establishing is 3 surveillance update intervals.   

## 2.4.2.7 Verification Of Requirements Related To Transitions Between Passive And Active Surveillance Test 6 (Threat Calculations At Hybrid To Active Surveillance Transition)

This test verifies that ADS-B data does not have an impact on intruder range and range rate utilized by the TCAS Collision Avoidance System (CAS) especially at the time of transition from passive to active surveillance and SURV_MODE = Reduced to SURV_MODE = Normal  The test simulates both active and passive (ADS-B) data such that the passive range data is slightly different than the active range data.  TAU values calculated by the CAS are observed to ensure they are based on active range measurements. 

 
Scenario Description The test scenario consists of a single intruder reporting both active and passive range. The intruder's passive range is 100 - 250 meters greater than the active range.  The intruder converges from > 15 nmi at a rate of -360 kts.  As the intruder range decreases the TCAS will transition the intruder from passive to active surveillance and SURV_MODE = Normal  Tau values will be examined at this transition to ensure there are no anomalies (range/range rate inconsistencies). The scenario can be run as given above if at the time of transition to active surveillance the intruder is also marked as SURV_MODE = Normal.    If this is not the case the scenario must be constructed to force a transition to Normal 1 Hz active interrogation rate at the same time that it transitions from passive to active surveillance. 

 
This scenario is specifically designed to test a system that tracks in 'normal' surveillance at the transition from 'passive' to 'active'.  If a manufacturer's implementation is such that the transition from 'passive' to 'active' surveillance always happens prior to the transition to 'normal' surveillance (meeting the requirement that at least two active range measurements are provided to the CAS logic at transition to Normal)  it is acceptable to demonstrate through this test and/or other test/analysis that CAS threat calculations are not impacted by 'passive' range data since the CAS Tau values will not be calculated until the track  SURV_MODE = Normal. TCAS Aircraft Barometric Altitude 
= 20,000 ft 

| Radio Altitude       |  >2500 ft           |
|----------------------|---------------------|
|                      |                     |
| Intruder Aircraft #1 |                     |
| Version              |                     |
| Altitude             |                     |
| Altitude Rate        |                     |
| Range (active)       | = 10 NM             |
| Range (passive)      | = 15.05 to 15.13 NM |
| Range Rate           |                     |

 
Success Criteria Demonstrate that at the update interval that the intruder transitions from passive to active surveillance and from SURV_MODE = reduced to SURV_MODE = normal that the transitions does not result in erroneous threat logic calculations.  Specifically, check that the ITF.TRTRU (in the CAS logic) at transition to SURV_MODE = Normal are within 5 
seconds of a track that had been exclusively tracked in active surveillance.  (i.e. the 'True Tau' values utilized in the CAS logic are not affected by the passive range measurements.).   The ITF.TRTRU values in the table can used for the comparison as they were calculated using "perfect" range and range rate values. 

 
Note:  This is determined by comparing the actual 'True Tau' values calculated by the CAS logic with the 'True Tau' values calculated using the active range values of the simulated intruder during the surveillance transitions from 'passive to active' and 'reduced to normal' as shown in the following table.    'True Tau' values calculated by the CAS logic should be within +/- 5 second. 

True Tau 
(ITF.TRTRU) 
Active Range 
R/-0.1 
 
9.2 
92 
 
9.1 
91 
 
9.0 
90 
Transition to 'active'  
8.9 
89 
 
8.8 
88 
 
8.7 
87 
 
8.6 
86 
 
8.5 
85 
 
8.4 
84 
 
8.3 
83 
 
8.2 
82 
 
8.1 
81 
 
8 
80 
 
7.9 
79 
 
7.8 
78 
 
7.7 
77 
 
7.6 
76 
 
7.5 
75 
 
7.4 
74 
 
7.3 
73 
 
7.2 
72 
 
7.1 
71 
 
7 
70 
 
6.9 
69 

 

## 2.4.3 Cross-Reference Of Requirements And Associated Tests

| Requirement                     |
|---------------------------------|
| §2.2.6.2 Active Surveillance    |
| Requirements                    |
| §2.4.2.7 Verification of        |
| Requirements Related to         |
| Transitions between Passive and |
| Active Surveillance             |
| Test 1 - Intruder 1             |
| Test 2 - Intruder 3             |
| Test 6                          |
|                                 |

(1.2) The changes to §2.2.7.1 and §2.4.2.1.2  allows a system to be designed to only perform hybrid 
surveillance for an intruder whose ADS-B OUT version is greater than or equal to 2 excluding 
version 0 and 1.  Any proposed new text will be highlighted in gray while text intended to be 
deleted will be marked with red strikethrough font.    

## 2.2.7.1 Conditions For Hybrid Surveillance

An established Mode S track will enter the hybrid surveillance state if: 

a) It is in active surveillance state, satisfies the modified hybrid threat criteria 
specified in §2.2.7.1.2, and passes one or two successive validation tests as specified in §2.2.6.1.2. 
b) It is in extended hybrid surveillance state, but the conditions for extended hybrid 
surveillance in §2.2.5.2 (own aircraft and intruder report quality, power level) are no longer satisfied, as specified in §2.2.7.1.3. 
The system may be designed to only perform hybrid surveillance for an intruder whose ADS-B Version Number ≥ 2. 

See section 2.2.9 on requirements related to decoding Version Number. 

## 2.4.2.1.2 Intruder Aircraft

All the tests specify a range and relative velocity of intruder aircraft with respect to own aircraft.  The equipment manufacturer may select what relative azimuth the intruder is with respect to own aircraft. 

Set up a nominal difference between all passive and active data so that the correct data source (active or passive) is output or provided to the CAS logic to be verified.  The suggested difference is: 

 
in altitude: 25 ft when quantization is 25 ft. 
 
in range:   100 ft. 
 

|                      | Altitude Q    |                                  |     | = 25 ft    |
|----------------------|---------------|----------------------------------|-----|------------|
| CC                   |               |                                  |     | = true     |
| Reply/Squitter Power | = -50 dBm     |                                  |     |            |
| Reply/Squitter Power |               | = -70 dBm (for version ≥2 ADS-B) |     |            |

 
Note: It is acceptable to set the signal level of version ≥2 ADS-B to below the TCAS 
minimum threshold for up to 10 seconds before the start of the test (T=0) to allow the track to be acquired passively before TCAS. 
 
Active Interrogation Reply (DF=0) Always available per the intruder set-up in each test scenario.   Formatted per Ref. D. Active Squitter (DF=11) 
--`````,,,,,,,,`,``,,`,,`,```,`-`-`,,`,,`,`,,`---
 
Always available per the intruder set-up in each test scenario.  Formatted per Ref. D. 

Long Active Interrogation Reply (DF=16) Always available per the intruder set-up in each test scenario.  Formatted per Ref. D. 

Used to support the crosslink interrogation. Airborne Position Message (DF=17) All intruders, unless otherwise stated, should transmit their Airborne Position Message as required by Ref. C and per the specific field settings defined. 

The intruder **shall** transmit DF=17 airborne position squitters at a nominal rate of 2/sec when TCAS is in squitter listening mode.  These squitters alternate their CPR Format 0, 1, 0, 1,,,,, with respective even, odd position encoding. The following provide the standard data content for Airborne Position Messages. CA (6-8)  
 
 
=5 (airborne) 

| AA (9-32)                                                                       |                                                |     |
|---------------------------------------------------------------------------------|------------------------------------------------|-----|
| ME                                                                              |                                                |     |
| -                                                                               |                                                |     |
| Type Code (33-37)                                                               | = 9                                            |     |
| -                                                                               |                                                |     |
| Surv Status (38-39)                                                             | = 0                                            |     |
| -                                                                               |                                                |     |
| Single Ant (40)                                                                 |                                                | = 0 |
| -                                                                               |                                                |     |
| Altitude (41-52)                                                                | = value specified in test, encoding per Ref. C |     |
| -                                                                               |                                                |     |
| Time (53)                                                                       |                                                | = 1 |
| -                                                                               |                                                |     |
| CPR Format (54)                                                                 | = 0/1 alternating with even/odd encoding       |     |
| -                                                                               |                                                |     |
| Encoded Latitude (55-71) = Value determined from test own lat, lon, and range   |                                                |     |
| to intruder                                                                     |                                                |     |
| -                                                                               |                                                |     |
| Encoded Long (72-88)   = Value determined from test own lat, lon, and range  to |                                                |     |
| intruder                                                                        |                                                |     |

 
Airborne Velocity Message All intruders, unless otherwise stated, should transmit their Airborne Velocity Message per the required encoding and rate as required by Ref. C.  This section defines example settings for subfields settings defined in this section.   All values are encoded per Ref. C. CA (6-8)  
 
 
= 5 (airborne) 

| AA (9-32)                |     |     | = intruder's address      |
|--------------------------|-----|-----|---------------------------|
| ME                       |     |     |                           |
| -                        |     |     |                           |
| Type Code (33-37)        |     |     |                           |
| -                        |     |     |                           |
| Subtype (38-40)          |     |     |                           |
| -                        |     |     |                           |
| Intent Change Flag (41)  |     |     | = 0                       |
| -                        |     |     |                           |
| IFR Capability Flag (42) |     |     | = 1                       |
| -                        |     |     |                           |
| NAC                      |     |     |                           |
| v                        |     |     |                           |
| (43-45)                  |     |     |                           |
| -                        |     |     |                           |
| E/W Direction Bit (46)   |     |     | = value specified in test |
| -                        |     |     |                           |
| E/W Velocity (47-56)     |     |     | = value specified in test |
| -                        |     |     |                           |
| N/S Direction Bit (57)   |     |     | = value specified in test |
| -                        |     |     |                           |
| N/S Velocity (58-67)     |     |     |                           |
| -                        |     |     |                           |
| Vert Rate Source (68)    |     |     | = 1                       |
| -                        |     |     |                           |
| Vert Rate Sign (69)      |     |     |                           |
| -                        |     |     |                           |
| Vert Rate (70-78)        |     |     |                           |
|                                                   |     |    | -   |     |
|---------------------------------------------------|-----|----|-----|-----|
| Reserved (79-80)                                  |     |    |     | = 0 |
| -                                                 |     |    |     |     |
| Difference from Barometric Altitude Sign (81) = 0 |     |    |     |     |
| -                                                 |     |    |     |     |
| Difference from Barometric Altitude (82-88)       | = 0 |    |     |     |

 
Flight Identification Message All intruders, unless otherwise stated, should transmit their Flight Identification Message per the required encoding and rate as required by Ref. C and per the subfield settings defined in this section.   The equipment manufacturer may specify Ident Chars (41-88) that allow the test aircraft to be individually identified.  All values are encoded per Ref. C. CA (6-8)  
 
 
= 5 (airborne) 
AA (9-32)  
 
 
= intruder's address  
ME 

|                                |    |     | -   |                          |
|--------------------------------|----|-----|-----|--------------------------|
| Type Code (33-37)              |    |     |     | = 4                      |
| -                              |    |     |     |                          |
| ADS-B Emitter Category (38-40) |    | = 0 |     |                          |
| -                              |    |     |     |                          |
| Ident Char #1 (41-46)          |    |     |     | = manufacturer specified |
| -                              |    |     |     |                          |
| Ident Char #2 (47-52)          |    |     |     | = manufacturer specified |
| -                              |    |     |     |                          |
| Ident Char #3 (53-58)          |    |     |     | = manufacturer specified |
| -                              |    |     |     |                          |
| Ident Char #4 (59-64)          |    |     |     | = manufacturer specified |
| -                              |    |     |     |                          |
| Ident Char #5 (65-70)          |    |     |     | = manufacturer specified |
| -                              |    |     |     |                          |
| Ident Char #6 (71-76)          |    |     |     | = manufacturer specified |
| -                              |    |     |     |                          |
| Ident Char #7 (77-82)          |    |     |     | = manufacturer specified |
| -                              |    |     |     |                          |
| Ident Char #8 (83-88)          |    |     |     | = manufacturer specified |

 
Note: Squitter Bit field numbering.  All the bit field numbering identified in this tests is referenced to the entire DF=17 message and not the ME field numbering.   

For intruders that are identified in the test sections to be ADS-B Version Number ≥2 targets the Target State and Status Message and the Aircraft Operational Status Message should be transmitted, otherwise these messages should not be transmitted (this identifies them as version=0 intruders). Target State and Status Message When specified in the test, ADS-B version 2 intruders should transmit their Target State and Status Message per the required encoding and rate as required by Ref. C and per the subfield settings defined in this section.  All values are encoded per Ref. C.  Only the subfields applicable to passive surveillance are defined for this message. CA (6-8)  
 
 
= 5 (airborne) 
AA (9-32)  
 
 
= intruder's address  
ME 
- 
NACp (72-75)  
= 7 
- 
SIL (77-79) 
  
= 3 
 
Aircraft Operational Status Message When specified in the test, ADS-B version 2 intruders should transmit their Aircraft Operational Status Message per the required encoding and rate as required per Ref. C and 
--`````,,,,,,,,`,``,,`,,`,```,`-`-`,,`,,`,`,,`---
 
 
per the subfield settings defined in this section.  All values are encoded per Ref. C.  Only the subfields applicable to passive surveillance are defined for this message. 

 

| CA (6-8)                     |     |     | = 5 (airborne)       |
|------------------------------|-----|-----|----------------------|
| AA (9-32)                    |     |     | = intruder's address |
| ME                           |     |     |                      |
| -                            |     |     |                      |
| ADS-B Version Number (73-75) | = 2 |     |                      |
| -                            |     |     |                      |
| NACp (77-80)                 |     |     | = 7                  |
| -                            |     |     |                      |
| SIL (83-84)                  |     |     |                      |
| -                            |     |     |                      |
| SDA (63-64)                  |     |     |                      |

If the system implements the optional requirement of section 2.2.7.1 requiring ADS-B Version Number >= 2 to qualify for hybrid surveillance then the tests of this MOPS shall be modified in the following way: 
 

- 
All ADS-B out equipped intruders for which the ADS-B Version Number is NOT specified (i.e. were intended to have a default version number of 0) shall be setup to broadcast an ADS-B Version >= 2 and their power level shall be set to - 50 dBm. 
(1.3) 
Appendix G is added demonstrating that the safety analysis in Appendix D still applies.  It documents that a TA and an RA will still be generated at the same time as a TCAS II system which does not use the hybrid surveillance techniques of this specification. New text is 
highlighted in gray while text to be deleted will be marked with red strikethrough font. 

## Appendix G Analysin And Information Supporting Change 1

--`````,,,,,,,,`,``,,`,,`,```,`-`-`,,`,,`,`,,
 
G.1 Introduction This appendix shows that Change 1 to DO-300A prevents spurious RAs during passive to active surveillance transitions and does not impact the safety assumptions described in Appendix D. Specifically, it shows that an RA and TA will still be reported at the same time as a TCAS II system which does not use the hybrid surveillance techniques of this MOPS. 

 
The proposed change to the Hybrid Surveillance MOPS may introduce a delay of 1 second to the time that the collision avoidance logic would begin processing a track as a Normal Surveillance Mode track (under nominal link margin conditions).  The following analysis demonstrates that there is no impact to the time that an RA or TA is annunciated as a result of this change. 

## G.2  Terms

Surveillance Mode - The data field provided as part of each surveillance report provided to the CAS logic.  This field has two values:  Reduced and Normal.  Reduced implies a 5 sec nominal surveillance update rate and Normal implies a 1 sec nominal surveillance update rate for active tracks.  The CAS logic will only generate TAs and RAs for intruders in normal surveillance mode1  In RTCA/DO-185B section 2.2.4.8.1 this  "data field" is referred to as the "Track Update rate" and in the corresponding *pseudocode* as S.SURVMODE. 

## G.3  Observed Issue In The Field

As of early in 2015 approximately 30 different spurious RAs, over a period of 15 months have been reported.   Some of these events are summarized in the Airborne Collision Sub-Group of ICAO Aeronautical Surveillance Panel (ASP) paper:  IP ACSG01-04 - Unexpected RAs in aircraft equipped with TCAS V7.1 and Hybrid surveillance by Philippe Louyot (DSNA).   The purpose of the change to RTCA/DO-300A and EUROCAE ED 221 is to update the specifications in this MOPS in order to prevent these unjustified RAs. Common characteristics of the observed events include: 
- 
Own Aircraft equipped with TCAS V7.1 w/ DO-300 Hybrid Surveillance 

- 
Own and Intruder ADS-B Out equipped 
- 
Both aircraft have similar position source architecture, via a data concentrator, for ADS-B OUT and TCAS use. 
- 
Occur at SL=7  (above FL 200)  
- 
Spurious RA is generated at ranges of 5 - 7 NMI 
- 
Intruder passing behind "own"  

## G.4  Root Cause Of The Spurious Ra

This section outlines the different events which must occur in order for a spurious RA to be generated.   

1.  Transition to Active Surveillance.   A spurious RA cannot occur against an aircraft which is only 
passively tracked.   Therefore a transition to active surveillance is required. "Noise" on received ADS-B OUT messages drives a spike in closure rate which drives the early transition to active surveillance. 
                                                     
 

2. At transition from SurvMode = Reduced and passive surveillance TO SurvMode = Normal and 
active surveillance AND the CAS Logic Tau falls below RA threshold (just once is sufficient). 
The CAS Logic TAU is driven by range (ITF.R) and (ITF.RD).  There is no smoothing of ITF.R 
and ITF.RD at the transition time - so the system is especially susceptible to transients. Additionally the TAUCAP features does not allow TAU to rise - which is also susceptible to transients. 

 
 
Note HMD filter is not active until CAS logic tracker firmness is "high" 
 
3. The track must stay in SurvMode = Normal for >= 3 seconds so that ITF.HIRM can reach a value 
of 3 or greater, which is required for generation of an RA. 
 
4. Active replies must correlate to the existing passive surveillance track - otherwise a new track is 
started - and the CAS logic tracker is reset and the RA is not issued  

## G.5  Proposed Solution

The proposed solution is defined in section 2.2.6.2 of this document and is repeated below. 

 
When transitioning a track from 'Reduced' to 'Normal' Surveillance Mode the Mode S 
Surveillance shall identify an intruder track as being in 'Reduced' Surveillance Mode until two active range measurements have been provided to the CAS logic tracker.  This will ensure that CAS does not use ADS-B passive position data for threat calculations. This requirement will prevent unnecessary advisories resulting from ADS-B to active surveillance transition.  Initial implementations of hybrid surveillance were susceptible to transients during the transition and generated unnecessary advisories.   

## G.6  Effectiveness Of Proposed Solution To Prevent Spurious Ras

The proposed solution ensures that the measured range used to compute the horizontal "tau" values of RTCA/DO-185B specified collision avoidance logic are based exclusively on active surveillance TCAS slant range measurements as is done with a TCAS developed to RTCA/DO185B but without DO-300A specified hybrid surveillance. 

The Table shows how each of the causes or contributing factors of spurious RA are addressed by the proposed change. 

Cause  
How Addressed By Proposed Change 1  
Not addressed directly - solution to cause 2 will prevent spurious RA, even in the case where  an early jump to active surveillance occurs. 
Transition to Active Surveillance early "Noise" on ADS-B OUT drives a spike in closure rate At transition from SurvMode = Reduced and passive surveillance   TO SurvMode = Normal and active surveillance And CAS Logic Tau below RA threshold just once  
2  
There is no smoothing of ITF.R and ITF.RD at transition time - so susceptible to transients  
Proposed change ensures that all the data to compute ITF.R and ITF.RD are from active surveillance. Delaying transition to SurvMode = Normal by 1 second, ensures that the previous S.RR update and current S.RR update are from active TCAS surveillance. At the cycle that SurvMode transitions from 
"Reduced" to "Normal" the filtered range will be set to 
current TCAS active surveillance reply and ITF.RD will be set the difference in the current and previous range (S.RR current - S.RR previous)/time between reports. The above eliminates ADS-B or ADS-B to Active Surveillance induced transients.   
(Note:  The system is still susceptible to active surveillance transients.)  
TAUCAP features does not allow TAU to rise - so susceptible to transients. 

## G.7  Safety Of Proposed Solution To Prevent Spurious Ras

The proposed solution delays the transition to the SURVMODE = Normal by 1 second. This analysis uses, as a starting point, the analysis of appendix D. The focus of the analysis of Appendix D, was to ensure that an RA or TA produced by a system compliant with the hybrid surveillance standards did not delay the issue of a TCAS II RA or TA. The safety study of Appendix D made the following assumptions: 

- 
The transition to Normal Surveillance must be performed 3 seconds before the alert time of a TA and 8 seconds before the required alert time of an RA.  

- 
The slant range acceleration is 1/3 g. 
- 
Intruder ADS-B range position error is 0.2 NMI  
- 
Intruder ADS-B uncompensated position latency of 0.6 seconds 
- 
Own Ship uncompensated position latency of 0.250 seconds 
- 
The range rate error of the passive track is 130 knots (for the TA case) and 145 knots (for the RA case). 
Figure D-3 summarizes the assumptions.  It also illustrates that with these assumptions the alert time of the TAs and RAs are not impacted. 

 
 
"Four curves are shown on a graph of range rate versus range. The curve closest to the lower left of the graph is the range/range rate boundary for issuing a TA at altitude layer 6 and sensitivity level 7. The TA boundaries for lower altitude layers and sensitivity levels would be to the left of that curve, as would the RA boundaries for all altitude layers and sensitivity levels.   … The next curve above and to the right of the TA boundary curve is the locus of points from which an intruder could cross the TA boundary within 3 seconds assuming a range acceleration of 11 ft/s2.  … The curve closest to the upper right of the chart is the passive-to-active surveillance boundary in range and range rate…"2   and is specified by equation 2 of RTCA/DO-300A section 2.2.6.1.4.   "Figure D–3 shows an offset active surveillance boundary curve calculated for a fixed component of range error of 0.2 NM (370 meters), a range-rate-dependent range error that is due to 0.85 seconds of uncompensated latency (being the sum of a worst case uncompensated latency of 0.6 seconds for the intruder and 0.25 seconds for the TCAS aircraft), and a range rate error of 130 knots. The knee in the shifted curve just touches the 3-second time buffer curve at 2.87 NM and -136 kt. Figure D–4 shows the critical region of the chart in greater detail."2 
 
 
Analysis shows that even if the active surveillance boundary were modified to be 59 seconds  to account for the one second delay in transitioning to SUVMODE = NORMAL that the dashed green curve would not "touch" or cross below the dashed purple curve - which represents the 3 second buffer to allow adequate time for a TA.   In fact, even if the surveillance transition tau were changed to 50 seconds the 3 second TA buffer and 8 second RA buffer would be maintained.  Figures G-1 and G-2 are updates to the curves of Figures D-3 and D-4 but with a surveillance tau threshold of 50 seconds.   Figure G-3 is a further scaled in version - so that it is clear that the 3 second boundary is still maintained.  If that is still true for a transition that is 10 seconds late that it is certainly true for 1 second delay in the transition. 

--`````,,,,,,,,`,``,,`,,`,```,`-`-`,,`,,`,`,,`---
As can been seen, the DO-300 active surveillance boundary with assumed errors still does not cross the RA boundary with assumed aircraft acceleration and 8 second buffer. 

 

## G.8  Conclusion

The proposed requirements change will ensure that the CAS logic is not presented with ADS-B induced transients at the time of the transition from passive and reduced surveillance to active and normal surveillance.   Furthermore, although the proposed solution adds a 1 second delay to that transition the RA and TA timing will not be impacted. 

 
G.9   Further Rationale 
 
The comparison of the DO-300A Active Surveillance boundary and the TA Tau boundary at SL=7 are shown below.     Each row of the table is a rearrangement of the equation so that range rate is isolated on the left side.  The reformation of the equations only holds true for closing or negative range rates.  By comparing the last row it can be seen that Surveillance Tau boundary of 60 seconds could be reduced close to 48 and that hybrid boundary would be crossed before the TA boundary.   Although this comparison does not take into account the assumed errors in DO-300A,  it provides additional intuition about the margin that exists between the TA alert boundary and the passive / active surveillance boundary.  

(1.4) 
The changes in this section adopt the text from FAA TSO-C119d Appendix 2.  That appendix was created in response to comments received during the public comment phase for TSO-C119d. FAA disposition of certain comments received during that review period necessitated creation of 
Appendix 2 to affect changes to these sections of DO-300A.  New text is highlighted in gray 
while text to be deleted will be marked with red strikethrough font. 
 
(1.4.1) To ensure proper revalidation when own aircraft is operating on the surface, in the first paragraph 
of RTCA/DO-300A section 2.2.7.5, Revalidation, insert the following new text: 
An established track that is under hybrid surveillance (per §2.2.7.1) **shall** be subject to revalidation.  If a track under hybrid surveillance does not satisfy the first (altitude) condition of 
§2.2.6.1.4, it **shall** be subject to revalidation every 60th surveillance update interval;  if it satisfies the first and second (altitude and range) conditions of 2.2.6.1.4 but not the third (airborne) condition, it shall be subject to revalidation every 10th surveillance update interval;  if it satisfies the first condition of §2.2.6.1.4 but not the second (range) condition, it **shall** be subject to revalidation at intervals calculated according to the following procedure.  The revalidation interval t **shall** be calculated at the time of the initial successful validation and at the time of each successful revalidation.  It **shall** be used as the number of surveillance update intervals until the next revalidation attempt. 

 

(1.4.2) Because there is a requirement specifying creation of information which is never used, in 
--`````,,,,,,,,`,``,,`,,`,```,`-`-`,,`,,`,`,,`---
RTCA/DO-300A section 2.2.11, Interface to the CAS Logic, delete existing text from the first paragraph as follows: Position data for tracks under passive surveillance may be provided to the CAS logic via the 
interface specified in Ref A, §2.2.4.8.1.  If this is done, information **shall** be provided in addition  
to that required  in Ref.  A, §2.2.4.8.l(a) to distinguish a position  report  that resulted from a passive reception of an Airborne Position Message from one that resulted from an active interrogation. 
(1.4.3) Tests 2, 3a and 3b specified in RTCA/DO-300A, section 2.4.2.5, Verification of Acquisition and 
Maintenance of Established Tracks Using Active Surveillance (§2.2.6), do not need to be performed as their expected results are incorrect.  Test coverage of the input conditions associated 
with those tests is provided, in aggregate, by other existing tests in RTCA/DO-300A. 
 
(1.4.4) A new Test 11a is required in addition to the existing Test 11 specified in RTCA/DO-300A, 
section 2.4.2.6, Verification of Maintenance of Established Tracks using Passive Surveillance (§ 2.2.7).  This new test is to verify the revalidation rate when own aircraft is operating on the surface.  Perform this new test in addition to the existing Test 11; the new test does not replace 
Test 11.  Insert the following new text after existing Test 11:  

## Test 11A (Intruder Revalidation Rate When Own Aircraft Is Operating On The Surface 2.2.7.5)

This test verifies the revalidation rate when own aircraft is operating on the surface based on the altitude and range criteria for active tracking (§2.2.7.5).    
 
(The following tests may be performed using ADS-B reports or directly decoded ADS-B messages.  TIS-B and ADS-R data is not permitted.) 
 
Scenario Description 

 
 
Intruder 1 shows that when own aircraft is operating on the airport surface and an intruder is within the altitude and range criteria for active surveillance it will be tracked using hybrid surveillance with a 10 second revalidation rate (§2.2.7.5).  
 
 
Intruder 2 shows that when own aircraft is operating on the airport surface and an intruder is within the altitude but not the range criteria for active surveillance it will be tracked using hybrid surveillance with a variable revalidation rate according to the requirements in (§2.2.7.5). 

 
TCAS Aircraft Altitude  
 
= 0 ft (Ground Level) 
Altitude Rate   
= 0 FPM 
Position 
 
= Sydney 
Radio altitude input 
= 0 ft 
Ground Speed is valid and at 0 knots and TCAS Air/Ground (OOGROUN) indicates on-ground. 
 
Intruder Aircraft #1 Altitude  
 
= 2,000 ft 
Altitude Rate   
= 0 FPM 
Range 
 
= 2 NM 
Relative Speed = 0 kt At T=100 the intruder is terminated. 
 
Intruder Aircraft #2 Altitude  
 
= 2,000 ft 
Altitude Rate   
= 0 FPM 
Range 
 
= 8 NM 

Relative Speed = 0 kt At T=100 the intruder is terminated. 
Success Criteria 
For each intruder: 
The surveillance reports to the CAS logic are present for the duration of the track. Verify that the track is under passive surveillance. 

 
Intruder 1 Verify that revalidation interrogations are transmitted every 10 seconds.  
 
Intruder 2 Verify that revalidation interrogations are transmitted every 30 seconds.  
 
The revalidation rate for each applicable success criteria was identified using the table in §2.2.7.5. If the implementation uses the equation method then the revalidation interval can be longer by up to 10 to 20 seconds.  Care should be taken to verify that the success criteria matches the value expected based on the implementation. 

 

(1.4.5) RTCA/DO-300A removes a provision which allowed for larger range calculation errors above +/- 
60 degrees latitude from DO-300 Section 2.2.7.6 but the associated tests were not updated 
accordingly.  To account for removal of that provision, delete the following text from RTCA/DO-
300A, sections 2.4.2.8, Verification of Error Budget in Computing Slant Range from Passive Data and 2.4.2.10, Verification of DF17 Decoding and insert a clarifying note in Appendix A, 
Conversion of Reported Positions to Slant Range, section A.1, Overview.  TSO-C119d Appendix 
2 section 1.5 inadvertently introduced a unit change for the range tolerance of intruders in the 
Success Criteria of test 2.4.2.10, Verification of DF17 Decoding.  The tolerance is reverted back 
to 145 m (versus the 145 in specified by TSO-C119d, Appendix 2 for that test).   
 
2.4.2.8 Verification of Error Budget in Computing Slant Range from Passive Data 
. 

. 

. If the test method is used to demonstrate compliance to the requirement then this paragraph describes one potential scenario.  Own aircraft and intruder aircraft are traveling towards each other at 600 kt at high latitude (near 60 degrees). If the error between the passive range estimate and active range measurement is less than 145 meters then the intent of the requirement is met. The error in range computation of tests at slower closure rates can be used to extrapolate or predict errors at the 1200 kt closure rate. 2.4.2.10, Verification of DF17 Decoding 
. 

. . Success Criteria All Intruders. For all of the Intruders with Latitudes within ±60 degrees, verify that the range for each intruder is within 145 in m of the calculated range identified in Table 3. For all of the Intruders with Latitudes within ±60 degrees, verify that the bearing for each intruder is within 3 deg of the calculated bearing identified in Table 3. 

Verify that the error in range from the calculated range does not use more of the error budget allowed for range based on the completion of Test §2.4.2.8 (Verification of Error Budget in Computing Slant Range from Passive Data) Test 1. A.1 
Overview 

This appendix provides useful guidance on computing range from own and reported position data.  This appendix does not recommend a particular implementation and should be used for reference only. First, the exact conversion equations from position to slant range are given. The computational requirements for the exact conversion equations are reasonable and could be used as is for modern processors and typical TCAS traffic loads. Second, several approximate conversion equations from position to slant range are presented.  For circumstances where hybrid surveillance is implemented as a software upgrade to existing processors, it may be desirable to use approximations to the conversion equations to reduce the computational requirements.  The errors in the approximate equations are presented and compared to the computational accuracy requirements of §2.2.7.6, which requires a maximum 145 m processing error when calculating slant range. 

Note: The equations in A.2 provide an example of conversion equations which meet the accuracy requirements.  The approximation equations provided in the appendix may not provide the required accuracy. 

 The verification cross reference table is updated below to reflect the changes associated with test changes related to section 1.4 of this change document. New text is highlighted in gray while text to be deleted will be marked with red strikethrough font.  Note: for section 2.4.3, only the updated table rows are included in this change document. 

## 2.4.3 Cross-Reference Of Requirements And Associated Tests

|                                 | Requirement    | Test    | Sub Test    |
|---------------------------------|----------------|---------|-------------|
| Test                            | 3a, 3b,        | 4a, 4b, | §           |
| 2.2.5.2.1                       |                |         |             |
| Extended Hybrid                 |                |         |             |
| Surveillance Traffic Quality    |                |         |             |
| Requirements                    |                |         |             |
| §                               |                |         |             |
| 2.4.2.5                         |                |         |             |
| Verification of                 |                |         |             |
| Acquisition and Maintenance of  |                |         |             |
| Established Tracks using Active |                |         |             |
| Surveillance                    |                |         |             |
| Tests 5, 6, 7, 8, 9             |                | §       |             |
| 2.4.2.6                         |                |         |             |
| Verification of                 |                |         |             |
| Maintenance of Established      |                |         |             |
| Tracks using Passive            |                |         |             |
| Surveillance                    |                |         |             |
| Test 4, 3A                      |                | §       |             |
| 2.4.2.7                         |                |         |             |
| Verification of                 |                |         |             |
| Requirements Related to         |                |         |             |
| Transitions between Passive and |                |         |             |
| Active Surveillance             |                |         |             |
| §                               |                |         |             |
| 2.2.7.2.2.1                     |                |         |             |
| Active to Extended              |                |         |             |
| Hybrid Surveillance Transition  |                |         |             |
|                                 |                |         |             |
| §                               |                |         |             |
| 2.4.2.5                         |                |         |             |
| Verification of                 |                |         |             |
| Acquisition and Maintenance of  |                |         |             |
| Established Tracks Using Active |                |         |             |
| Surveillance                    |                |         |             |
| Test 2                          |                |         |             |
| Test 3a                         |                |         |             |
| Test 3b                         |                |         |             |
| Test 4a                         |                |         |             |
| Test 4b                         |                |         |             |
|                                 |                |         |             |
| Test 1 - All intruders          |                |         |             |
| Test 11, 11a                    |                |         |             |
| Test 14                         |                |         |             |
| §                               |                |         |             |
| 2.2.7.5                         |                |         |             |
| Revalidation                    | §              |         |             |
| 2.4.2.6                         |                |         |             |
| Verification of                 |                |         |             |
| Maintenance of Established      |                |         |             |
| Tracks using Passive            |                |         |             |
| Surveillance                    |                |         |             |
| §                               |                |         |             |
| 2.4.2.7                         |                |         |             |
| Verification of                 |                |         |             |
| Requirements Related to         |                |         |             |
| Transitions between Passive and |                |         |             |
| Active Surveillance             |                |         |             |
| Test 2 - Intruder 3             |                |         |             |
| Test 3 - Intruders 2-6          |                |         |             |
| Test 3A - Intruders 2,3         |                |         |             |
| Test 4 - Intruders 6,7          |                |         |             |

This Page Intentionally Left Blank 
--`````,,,,,,,,`,``,,`,,`,```,`-`-`,,`,,`,`,,`---