1828 L Street, NW, Suite 805 
Washington, DC 20036-5133, USA 

# Minimum Aviation System Performance Standards (Masps) For Flight Information Services-Broadcast (Fis-B) Data Link Revision A

 
This page intentionally left blank. 

Copies of this document may be obtained from 
 
RTCA, Inc. 

1828 L Street, NW, Suite 805 
Washington, DC  20036-5133 USA 
 
Telephone:  202-833-9339 
Facsimile:  202-833-9434 
Internet:  www.rtca.org 
 
Please call RTCA for price and ordering information. 

This page intentionally left blank. 

 

## Foreword

 
The original report (DO-267) was prepared by Special Committee 195 (SC-195) and approved by the RTCA Program Management Committee (PMC) on March 27, 2001.  Revision A of DO-267 was prepared by SC-195 and approved by the PMC on April 29, 2004.  Appendices D, F and I are normative appendices. RTCA, Incorporated is a not-for-profit corporation formed to advance the art and science of aviation and aviation electronic systems for the benefit of the public.  The organization functions as a Federal Advisory Committee and develops consensus-based recommendations on contemporary aviation issues. RTCA's objectives include but are not limited to: 
a. coalescing aviation system user and provider technical requirements in a manner that helps government and industry meet their mutual objectives and responsibilities; 

b. analyzing and recommending solutions to the system technical issues that aviation faces as it 
continues to pursue increased safety, system capacity and efficiency; 
c. developing consensus on the application of pertinent technology to fulfill user and provider 
requirements, including development of minimum operational performance standards for electronic 
systems and equipment that support aviation; and 
d. assisting in developing the appropriate technical material upon which positions for the International 
Civil Aviation Organization and the International Telecommunication Union and other appropriate 
international organizations can be based. 
 The organization's recommendations are often used as a basis for government and private sector decisions as well as the foundation for many Federal Aviation Administration Technical Standard Orders. Since RTCA is not an official agency of the United States Government, its recommendations may not be regarded as statements of official government policy unless so enunciated by the U.S. government organization or agency have statutory jurisdiction over any matters to which the recommendations relate. 

This page intentionally left blank. 

EXECUTIVE SUMMARY This document contains Minimum Aviation System Performance Standards (MASPS) for Flight Information Services-Broadcast (FIS-B), an automated, digital data link system.  The FIS-B system will provide timely access to data link updates of non-control, advisory information needed by pilots to operate safely and efficiently in the National Airspace System and in international airspace. The format of this document generally follows that of an RTCA Minimum Operational Performance Specification (MOPS).  However, a traditional MOPS is not appropriate for FIS-B since this document establishes system performance rather than requirements for specific equipment.  This MASPS supports interoperability between providers of ground and airborne FIS processing systems by defining a broadcast protocol that may be used in any broadcast medium (i.e., VHF, satellite).  The MASPS also provides design guidelines and recommended standards for airborne processing and display of FIS products. 

 
The FIS-B broadcast network organization described in the MASPS consists of a physical layer, an International Standards Organization (ISO) standard-based Data Link Services (DLS) layer, a Network layer, an FIS-B Application Service Element (ASE), and an FIS-B Application.  The physical layer is supplied by the manufacture with all the other layers and/or elements defined in the MASPS. The FIS-B Application Service Element (ASE), noted above, provides connectionless unacknowledged protocol services to include support for the segmentation (and reassembly) of large data files into Application Protocol Data Units (APDUs).  Segmenting large application data files into smaller APDUs reduces the amount of data lost due to any data link impairments.  The MASPS also establishes a publicly accessible FIS-B Product Registry that facilitates coordination and publication of specifications for APDU Payload encoding of new FIS products. The MASPS guidance for airborne processing and display of FIS products is applicable to any display of FIS information in the flight deck (or cockpit).  It is anticipated that most avionics that process and display FIS products will be approved using existing type certification or supplemental type certification processes such as TSO C113, Airborne Multipurpose Electronic Displays.  Consequently, this document only contains guidance that is unique to FIS-B and independent of other functions that are governed by other directives such as terrain and obstacles, and traffic. As the National Airspace System (NAS) evolves and the concepts of Free Flight are implemented, the requirement for use of FIS products and services may change from being advisory in nature to being required for safety of flight.  Any such required use will require a revised definition of the operating environment outlined in this MASPS to include the associated application of Required Communications Performance (RCP) criteria.  The introduction of such RCP criteria will require changes to this MASPS, especially to Section 2.0, System Performance Specifications, and Section 4.0, Procedures for Performance Requirement Verification. 

This page intentionally left blank. 

## 1 Purpose And Scope 1.1 Introduction

This document contains Minimum Aviation System Performance Standards (MASPS) for Flight Information Services-Broadcast (FIS-B), an automated, digital data link system. The FIS-B system will provide timely access to data link updates of non-control, advisory information needed by pilots to operate safely and efficiently in the National Airspace System and in international airspace.  FIS-B services will provide FIS information to pilots such as weather graphics and text, Special Use Airspace (SUA) information, and Notices to Airmen (NOTAMs).  This document provides a broadcast protocol for use in any broadcast medium. These specific system performance standards and equipment characteristics should be useful to designers, manufacturers, installers, and users of FIS-B data link systems. Functional specifications are used where possible so that implementers may have flexibility in developing FIS-B data link systems.  Designing to these standards is one means of assuring that the system and equipment will perform their intended functions satisfactorily under all conditions normally encountered in routine aeronautical operations.  Any regulatory application of this document is the sole responsibility of appropriate governmental agencies. The format of this document generally follows that of an RTCA Minimum Operational Performance Specification (MOPS).  However, a traditional MOPS is not appropriate for FIS-B, since this document establishes system performance rather than requirements for specific equipment.  This MASPS defines a broadcast protocol that supports interoperability between providers of ground and airborne FIS processing systems and provides design guidelines and recommended standards for airborne processing and display of FIS products. 

Section 1 of this document provides information on purpose and scope needed to understand the rationale for system and equipment characteristics, standards, and performance requirements stated in the remaining sections.  It describes typical system applications and operational goals, and establishes the basis for the standards and performance requirements stated in Sections 1 and3, and Appendices D and F. 

Section 2 contains the minimum system performance standards for FIS-B data link systems. Section 3 contains the minimum performance standards for each subsystem/function that is a required element of the minimum system performance in Section 1.  Section 3.1 
defines the FIS-B network interface and Section 3.8 provides guidelines and recommended standards for airborne processing and display of FIS products. 

Section 4 describes a set of minimum system test procedures to verify system performance compliance (e.g., end-to-end performance verification) and that subsystem performance meets the minimum performance requirements in Sections 1 and 3, and normative Appendices D, F and I. 

Appendix A contains a list of acronyms and abbreviations. 

Appendix B contains a glossary of terms. 

Appendix C contains a list of references. 

Appendix D is a normative appendix that describes the format for the Application Protocol Data Unit (APDU).   
Appendix E describes the FIS-B Product Registry, a publicly accessible source for listing the Product Identifiers contained in an APDU Header (see Appendix D) along with the specifications for encoding the FIS-B Product Files contained in the Payload portion of the APDU. 

Appendix F is a normative appendix that describes exceptions to the FIS-B Interface as specified in Section 3.0. 

Appendix G describes the test data sets used to verify FIS-B system performance as specified in Section 4.0. 

Appendix H provides supporting background on ground-based and airborne weather radar systems that was used in determining the recommended color presentations for display of FIS precipitation products in the cockpit as listed in Table 3-2. 

Appendix I is a normative appendix that provides supporting background on general design considerations for cockpit displays of layered graphics and text; and was used in determining the recommended guidelines for the integrated display formats as outlined in Section 3.8.3. 

Appendix J provides supporting background on the National Convective Weather Forecast (NCWF) that was used in determining the recommended color presentations for the display of NCWF products in the cockpit as listed in Table 3-2. 

Appendix K contains the binary coding for the 6-bit Data Link Applications Coding 
(DLAC) alphabet described in Section 3.8.1.6. 

The word "subsystem" as used in this document includes all components that make up a major independent, necessary and essential functional part of the system so that the system can properly perform its intended function(s). 

## 1.2 System Overview

An operational FIS-B system architecture includes the five processes or functions illustrated in Figure 1-1.  These are:  

1. collection of FIS source information from various sources; 2. processing and formatting the data where appropriate into FIS-B products;  
3. processing (and segmenting) FIS-B products into APDUs for data link transmission; 
4. broadcasting the digitally-coded data into coverage volumes in the airspace; and 
5. receiving, decoding and displaying the data by avionics onboard the aircraft for the 
pilot's review or other applications.   
Figure 1-1 illustrates the FIS-B architecture from a protocol stack view.  Both the hardware/processing view and protocol stack views are intended to be notional, that is, they do not place requirements on specific ground or avionics implementations.  For example, the MASPS Data Link Service layer described in this document may be created in either Step 2 or Step 3. 

While the five processes illustrated in Figure 1-1 describe a complete end-to-end system, this MASPS focuses on the interoperability between point B and C and at point D.  
Requirements are established on the Data Link Layer protocol that links the infrastructure of Steps 1, 2, and 3 with the on-board display and processor of Step 5.  Additional requirements are established to ensure consistency of presentation at the pilot interface, point D in Figure 1-1.  Establishing the operational specifications for the airborne component inherently places requirements on the ground-based processing components in Steps 1, 2, and 3.  It is assumed that these steps will be specified and performed in a manner appropriate for anticipated FIS-B applications. FIS-B data link systems use a one-way broadcast protocol.  It is "one-way" in the sense that information flows only from the server to the receiving aircraft without the need for the aircraft to request information from the server, nor to acknowledge receipt.  It is typically "non-addressed" in the sense that information provided by the server is not addressed to a specific aircraft, but is rather intended for the benefit of any suitably equipped aircraft that may be in the coverage volume.  These characteristics make the broadcast protocol well suited to provide information that is of interest to a large portion of the aircraft in the coverage volume.  In addition, the simplicity of the protocol translates into lower costs for both avionics and ground infrastructure. 

Referring to Step 4 of Figure 1-1, the basic concept is that servers will repetitively broadcast a wide assortment of FIS data into their radio frequency coverage volumes. The servers cannot know if all the aircraft receiving the broadcast captured all the data without error, or would they know when additional aircraft enter the coverage volume and are in need of information.  The key to the operational effectiveness of FIS-B is to ensure that the scope of the product list and the repetition intervals of the products are suited to the needs of the users in the broadcast coverage volume. In describing the primary functions of the FIS-B avionics, it is helpful to group them into continuous and discrete functions.  When within the coverage volume, FIS-B avionics would be expected to monitor the FIS-B frequency (or frequencies) to receive, decode, and store data as the broadcast server issues them.  The FIS-B avionics would also be expected to automatically manage the contents of an onboard FIS database in which the received data are stored.  Such management functions would include sorting the data for later retrieval by the pilot or other applications, purging old information that no longer applies and passing information directly to the pilot.  It is assumed that these functions would operate more-or-less continuously in the background without any need for direct pilot management. The more discrete functions of the FIS-B avionics are those associated with the interaction between the database and the pilot (through some form of I/O device) or another application.  They are discrete in the sense that they are usually prompted by an action of the pilot (or application).  An example is a pilot-initiated query of the database to obtain the latest surface observation for an airport of interest.  Another example would be the query of the database by an application to portray weather graphics on a moving map display. 

## 1.3 Operational Applications

The goal of FIS-B data link systems is to provide weather and other non-control flight advisory information to pilots in a manner that will enhance their awareness of the flight conditions and enable better strategic route planning consistent with guidance provided by Federal Aviation Regulations and corporate policy.  The information provided through FIS-B will be advisory in nature, and considered non-binding advice provided to assist in the safe and legal conduct of a flight operations.  With this information, general aviation pilots and air carrier flight crews will be better able to assess the need to consider alternative route and altitude selection. At present when adverse weather conditions are present, the VHF radio frequencies designed to facilitate the exchange of weather and flight data information become saturated to the point that near real-time exchange of information is troublesome.  It is envisioned that FIS products will be continuously received and stored to be readily available as needed, or when requested by the pilot.  
Implementation of an FIS-B data link system is not intended to replace existing voice networks, Flight Service Station (FSS) services, or usurp any joint duties or responsibilities required by part 121 operators.  Loss or non-receipt of FIS-B service would have no regulatory impact.  
FIS products are to be used only for advisory and strategic/planning purposes and not for crew alerting.  This is due to the fact that FIS products may have significant latency between the observation of a weather phenomenon, the issuance of a forecast, or the change in airspace status; and the display of that information in the cockpit.  In addition, because their update rates are relatively low, FIS products should not be used for tactical maneuvering of the aircraft, and should not be the sole basis for immediate corrective action by the pilot.  FIS products are intended to enable pilots to determine if action should be taken well before it is required, and should be used in conjunction with other information sources to support in-flight decisions. It is expected that FIS-B will offer operational advantages to all types of airspace users.  
For part 121 airline operations, the ability of flight crews to access information in-flight previously available only during pre-flight will greatly enhance the collaborative decision making process of pilot-in-command and aircraft dispatcher. The general aviation (GA) community will benefit from FIS-B by having better in-flight access to information on weather phenomena that may pose a danger to the flight.  
Presently, many GA flights are unnecessarily curtailed, cancelled, or terminated early simply because the pilot does not have practical in-flight access to weather and NAS 
status information to ensure that risks to the flight remain low or minimal.  In addition, because many GA flights are single-pilot operations, FIS-B will enable GA pilots to gain a more comprehensive weather picture than currently obtainable via voice radio, thereby enabling better in-flight strategic decision-making.  Finally, with the creation of Temporary Flight Restrictions (TFRs) becoming more prevalent due to national security concerns, FIS-B offers another means to increase the GA pilot's awareness of the status of airspace. 

## 1.4 Future Applications

As the National Airspace System (NAS) evolves and the concepts of Free Flight are implemented, the requirement for use of FIS products and services may change from being advisory in nature to being required for safety of flight.  Any such required use will require a revised definition of the operating environment to include the associated application of Required Communications Performance (RCP) criteria as outlined in AC 20-140.  The introduction of such RCP criteria will require changes to this MASPS, especially to Section 2.0, System Performance Specifications, and Section 4.0, Procedures for Performance Requirement Verification. 

## 1.5 Scope And Objectives

Total system performance standards are dependent on many variables in both the ground and airborne infrastructures and are beyond the scope of this MASPS.  Establishing the minimum standards for media-independent broadcast of FIS will support interoperability between providers of ground and airborne processing systems.  Further, establishing methods to avoid presenting misleading information to pilots and to provide acceptable standards for cockpit presentations of FIS products will support certification, training and safety objectives. Some specific objectives of this MASPS are: 

a. Establish standards for digital data link broadcast communications, independent of 
the radio frequency (RF) spectrum.  
b. Provide flexibility in data format structure to accommodate evolving technologies in 
data sources and data processing techniques. 
c. Provide capabilities to ensure integrity of data transmissions. 
d. Support interoperability between providers of ground and airborne processing 
systems, that is, between points B and C of Figure 1-1. 
e. Assure the maximum possible consistency in product set, pilot presentation, that is, at 
point D in Figure 1-1. 
f. Establish standards for cockpit presentation of FIS products independent of other 
functions such as terrain and obstacles, and traffic that are governed by other directives. 

## Notes:

1) The guidance in Section 2 and Section 3.8 is not exhaustive relative to all FIS 
products.  The absence of guidance does not imply that further requirements may not emerge.  For example, ongoing research and development will contribute to the basis for further FIS product definitions (e.g., product animations or "looping" are 
current topics of intensive prototyping and human factors investigations). 
2) When FIS products are integrated into multi-purpose flight deck displays such as 
those generally found on air carriers, it is understood that the FIS-B information may need to be altered to maintain consistency with other conventions and requirements, the design philosophy of the flight deck, the display context, and the intended task.  
Section 3.8.3 provides guidelines on integrated displays combining layers of FIS 
products (text and graphic).  Manufacturers should follow those guidelines to the maximum extent practical.  These guidelines support displaying FIS information on multi-function displays that provide supplementary situation awareness information such as GPS moving map display.  This also supports flight crew members in correlating the FIS-B information with information used in other venues such as industry aeronautical educational information, service provider weather information, or to aid in achieving convention commonality with other aircraft installations. 
3) For Part 121 operations, the flight deck integrator should consider the following 
issues: 
a. Overlaying FIS-B latent weather products on real-time moving map displays with 
proper design rigor and usability testing. 
b. Providing ownship position, route of flight and other navigation information to 
be integrated with FIS-B product displays with proper failure analyses and operational mitigation procedures 
c. Pilot "notification" algorithms for SIGMET and AIRMET reports coordinated 
with crew "alerting" design within the flight deck into which it would be installed 
d. Review color standards to be appropriate for all operations. e. Review human factors and validation testing criteria. 
f. 
Review the applicability of automatic decluttering and presentation of multiple 
information types on a single display. 

## 1.6 Assumptions

For the purposes of this document, the following assumptions are made: 

a. FIS-B will be a non-control advisory service; the service will provide advice and 
information to assist in the safe conduct of flight. 
b. FIS-B will be used for strategic/planning purposes. c. FIS-B may be available in more than one radio frequency (RF) spectrum and by more 
than one data link. 
d. When appropriate, FIS-B broadcasts of FIS products will be repeated to allow 
opportunities for error correction by the receiving system. 
e. FIS-B broadcasts of FIS products will be updated and repeated on a cycle appropriate 
to the currency of each product. 
f. FIS-B data link systems may use aircraft avionics subsystems (e.g., VHF digital link 
[VDL] radios and Multifunction Displays [MFDs]) that will comply with existing standards published under separate RTCA MOPS and other standards. 
g. Combining FIS-B data with navigational data such as aircraft position, or 
surveillance data such as traffic information, if performed, will be a function of the user avionics. 

## 1.7 Verification Procedures

Given the architecture of FIS-B data link systems, a primary test consideration is the assurance that interactions between the airborne and ground subsystems are tested.  The focus of this MASPS is the specification of the standards and system requirements for two major functions/subsystems in implementing FIS-B: 

a. The communications format for encoding, decoding, and broadcasting Application 
Protocol Data Units (APDUs); and 
b. The minimum criteria for cockpit displays and presentations of FIS data link products 
and services. 
The test and verification procedures specified in Section 4.0 will address the above two major functions/subsystems and the ground-based functions/subsystems necessary to support FIS-B ground processing/broadcast management.  They are intended to be used as recommended means of demonstrating compliance with the minimum acceptable performance parameters.  Although specific test or verification procedures are cited, it is recognized that other methods may be preferred.  These alternate procedures may be used if they provide at least equivalent information.  In such cases, the procedures cited herein should be used as one criterion in evaluating the acceptability of the alternate procedures. Testing and the associated verification and validation are required only for products sent across the applicant's data link. 

## Notes:

1. The FIS-B ground equipment may require approval by appropriate FAA ground 
organizations (e.g., Airway Facilities) but that approval process and verification procedures are beyond the scope of this document. 
2. Also, regarding the verification of cockpit displays, it is strongly recommended that 
human factor evaluations be conducted with pilots of all categories of the end-user population to ensure safe operation of the FIS displays.  These evaluations should encompass issues of workload, accessibility, ease of operation, usefulness, 
interpretation of data, and effect on performance of other piloting tasks  (e.g., does it 
distract the pilot from primary flight responsibilities?).  Medium fidelity simulations 
and/or actual airplane tests are recommended for the piloted evaluations.  These 
would include scenarios that fully exercise the displays, as well as the performance of other flight deck responsibilities. 

## 1.8 Definition Of Terms

A glossary of terms used in this document may be found in Appendix B. 

## 2 System Performance Specification

The system performance standards are defined in this document. 

## 2.1 Airborne Equipment General Requirements

The airborne equipment required for receiving and displaying FIS products are defined in the following general performance standards.  

## 2.1.1 Equipment Compliance

FIS-B equipment, as defined in this document and operating within the context of Section 
1.3, have been determined to have failure conditions classified to at least a "minor" 
hazard classification, per established regulatory guidance.  Hardware and software design assurance should be developed according to regulatory guidance for at least a "minor" 
failure mode classification.  The FIS-B equipment manufacturer is highly encouraged to contact their regulatory authority for FIS-B equipment installation guidance. 

Note:  FIS-B airborne equipment manufacturers should be aware that regulatory 
authorities have identified a future need for onboard recording of data link communication for those aircraft required to have an onboard recorder as defined in the operating rules.  Regulatory authorities have noted data link 
communication reports that are presented to the flight crew are considered essential to accident and incident investigators for reconstruction of cockpit dynamics, ascertaining actual report content, and determination of resultant flight crew action.  In addition, ICAO is planning to implement a recommended practice to record data link communication by January 1, 2005.  For planning 
purposes, the FIS-B airborne equipment manufacturer should take this note into 
consideration during FIS-B equipment development.  FIS-B equipment 
manufacturers are encouraged to contact their local regulatory authority for a 
definitive statement regarding the status of this rule-making effort. 

## 2.1.2 Priority Service

The FIS-B equipment shall be designed to incorporate the ability for the flight crew to disable the FIS-B function (other than via circuit breaker).  When the FIS-B airborne capability is installed on common subnet/application process/displays, the FIS-B function shall not degrade the required performance of other higher priority, more safety critical Communication/Navigation/Surveillance (CNS) applications. 

## 2.1.3 Interoperability

This document specifies standards that will support application interoperability between FIS-B systems at point B and C of Figure 1-1, and will support common presentation features at point D of Figure 1-1.  All products that are broadcast shall use the standard application layer protocol and format as specified in 2.2.12 and 2.2.13. 

## 2.1.4 Abstract Syntax Notation (Asn) Reference

Abstract Syntax Notation version one (ASN.1) encoding and decoding of FIS products contained in this document shall be done in accordance with the International Organization for Standards ISO/IEC 8824-1: 1995 Information Technology - Abstract Syntax Notation One (ASN.1): Specification of Basic Notation.  The bit-wise formatting of FIS products encoded with ASN.1 shall be in accordance with ISO/IEC 8825-2: 1996 
Information Technology - ASN.1 encoding rules - Part 2: Specification of Packed Encoding Rules (PER).  The "non-aligned, non-canonical" form of PER shall be used as referenced in Appendix C. 

## 2.2 Fis-B Functional Requirements

The FIS-B system functional requirements are defined below. 

## 2.2.1 Lossless Compression

Data contents of all FIS-B Product Files shall be transferred by a lossless and transparent process from the broadcast transmitter through the data link medium to the FIS-B airborne system and its display.  If any data compression method is used, it shall be lossless compression.  

## 2.2.2 Lossless Display Of The Most Intense Or Severe Condition

The display of the most intense or severe condition (e.g., weather severity level) shall not be understated regardless of projection, scaling, or any other types of processing.  This requirement applies to both ground and airborne processing of area coverage data, such as NEXRAD radar images.  For example, the displayed geographical area over the earth's surface devoted to the depiction of the most severe level within an image should not decrease following all system processing.  In addition, the location of weather area depictions should remain constant in absolute and relative terms. When a graphical icon (e.g., a cylindrical or polygonal prism used to indicate a restricted air-space) is generated as a component of an FIS product, that icon will incorporate the entire region of impacted air-space.  The overstatement of the impacted air-space due to the construction of the graphical icon should be minimized to the extent practical.  (For example, depicting a complex air-space shape by its enclosing cylinder or polygonal prism is considered appropriate for FIS-B applications.) 

## 2.2.3 Verification Of Data Link Integrity

The system shall verify the data integrity of all data using the frame check sequence defined in Section 3.4.  Data found to be in error shall be discarded. 

## 2.2.4 Positive Indication Of Missing Data

The system shall not in any way misrepresent any FIS/weather information that is known to be corrupted or missing and shall display such data in a unique format insuring positive/unambiguous indication and location of the corrupted or missing data. 

## 2.2.5 Indication Associated With The Loss Of Data Link

The airborne unit shall incorporate an indication when no data has been received over the communications link for 15 minutes. 

## 2.2.6 Product Type Indication

Each display shall incorporate an indication of the type of product that is being displayed. For example, weather product types, including observations and forecasts. 

## 2.2.7 Product Age Indication

Each display of FIS products shall incorporate an indication of the date and time at which the product was generated.  Weather product age guidelines are defined in Section 
3.8.1.2. 

## 2.2.8 Product Validity Indication

The display of any product with a specified valid time or time interval shall incorporate an indication of that valid time or time interval.   

## 2.2.9 Standard Display Scheme For Weather Data

Each display of weather data should use consistent visual schemes, including color, to represent different weather conditions.  These visual schemes are described in Section 
3.8.2. 

## 2.2.10 Product Geographic Location

All data transmitted over the FIS-B network requiring registration with specific geographic locations shall contain earth location/navigation information to facilitate its use and display in the aircraft.  All position data encoded using latitude/longitude shall be referenced to the World Geodetic System 1984 (WGS-84) or NAD 83 datum. 

Note: 
The FAA uses the NAD-83 datum to represent navigational data, NEXRAD, and 
the locations of the weather reporting stations.  Aircraft GPS systems use WGS- 84 as the datum.  NAD-83 varies very slightly from WGS-84 in the flattening factor for the reference ellipsoid.  Position differences between the two data are typically in the centimeter/millimeter range.  The National Weather Service Rapid Update Cycle (RUC) model uses a different datum.  

## 2.2.11 Fis-B Content

The FIS-B system shall only provide current FIS products.  Whenever new and/or amended observations, forecasts, or other aeronautical information are received into the FIS-B network, they shall be incorporated into the next transmission of that product.   

## 2.2.11.1 Composite/Mosaic Products

Composite/mosaic products shall only include current individual reports as indicated below: 

a. Graphical map displays of METARs shall only include individual reports with a 
date/time that is no more than 75 minutes prior to the cut-off date/time of the graphical map display. 
b. Mosaic precipitation maps based on Next Generation Weather Radar (NEXRAD) 
shall only include single-site NEXRAD reports with a date/time that is no more than 10 minutes prior to the cut-off date/time of the NEXRAD mosaic. 

## 2.2.11.2 Product Discard

FIS data should be discarded (Step 2 of Figure 1-1) when either a newer version is received, or the expiration time is exceeded except as defined in 2.2.11.2.1 below. 

## 2.2.11.2.1 Weather Product Discard

For weather products as defined in this document, the following guidelines apply: 

a. Observations (e.g., METAR, special surface observation [SPECI], and PIREP): when 
a maximum of 120 minutes old. 
b. Forecasts: when no longer valid. c. Composite/Mosaic Products: 75 minutes after product creation cut-off date/time. 
Note: 
Weather Product Age and valid time guidelines are defined in Section 3.8.1.2. 

## 2.2.12 Application Service Element

All data transmitted over the FIS-B network shall use the Application Service Element 
(ASE) as defined in Section 3.6.  The ASE is independent of the physical medium over which the broadcast is transmitted.  Included in the ASE is the ability to assemble an FIS- B Product File from multiple transmissions of an identical report, replacing corrupted reports from prior transmissions with ones from a current transmission.  The ASE also assembles a large FIS-B Product File from many independent broadcast transmissions 
(per Section 3.6.2). 

## 2.2.13 Application Protocol Data Unit (Apdu) Header

All data transmitted over the FIS-B network shall use the APDU Header as defined in Appendix D.  The APDU Header is independent of the physical medium over which the APDU is transmitted. 

## 3 Subsystem/Function Performance Requirements

The following sections describe the Subsystem Performance under Standard Operational Conditions for the FIS-B Network Interface (3.1) and the Design Guidelines and Recommended Standards for Airborne Processing and Display of FIS (3.8). 

## 3.1 Fis-B Network Interface

The broadcast data link described in the following Sections 3.2-3.7 includes an FIS-B 
ASE that provides connectionless unacknowledged protocol services.  The ASE supports efficiency in spectrum use since there is no need to perform connection services, request information, or acknowledge receipt of information. The lack of an acknowledgment that a report has been received, however, causes a broadcast data link system to be considered less reliable.  To significantly improve the reliability of the FIS-B unacknowledged broadcast system, the ASE described in Section 
3.6 supports multiple broadcast transmissions of the same report. 

The ASE also provides for the segmentation of a FIS-B Product File into APDUs and reassembly of APDUs into an FIS-B Product File.  Segmenting large application data files into smaller APDUs reduces the amount of data potentially lost due to link impairments.  The size of the APDU is determined by making a trade-off between a small APDU to minimize the amount of data lost due to link impairments and a large APDU to minimize the overhead associated with the APDU Header.  

## 3.2 Fis-B Broadcast Network Organization

Figure 3-1 provides the organization for the FIS-B network interface, when viewed at points B and C in Figure 1-1.  The broadcast network organization consists of a manufacturer supplied physical layer, an International Standards Organization (ISO) 
standard-based Data Link Services (DLS) Layer, a Network Layer, a FIS-B ASE, and a FIS-B Application Layer that are specified by this document and the manufacturer.   

 
FIS-B Application Layer 
Section 3.7 
FIS-B ASE 
Section 3.6 
Network Layer 
Section 3.5 
Data Link Services (frame layer) 
Section 3.4 
Manufacturer Supplied Physical Layer 
Section 3.3 

## 3.3 Physical Layer

The requirements for the physical layer are outside the scope of this document.  It is assumed that the manufacturer will specify the requirements for the physical layer, which should be derived from an industry standard. 

## 3.4 Data Link Services Layer (Dls)

The main services for the DLS are frame processing, source broadcast station identification, broadcast addressing, and error detection. 

## 3.4.1 General Requirements

FIS-B frames shall conform to the ISO standard High-level Data Link Control (HDLC) 
protocol as described in ISO/IEC specifications 3309 and 4335.  Exceptions to strict compliance with ISO 3309 are outlined in Appendix F.  The overall format of the FIS-B 
frame is shown in Figure 3-2. 

FCS 
Section 
Flag 
Section 
 
Flag 
Section 
Address 
Section 3.4.4 
Link Control
Section 3.4.5 
Information Field 
Section 3.4.6 
3.4.7 
3.4.2 
3.4.2 
1 octet 
1-4 or 8 octets 
1 octet 
N (Media Dependent) 
2 octets 
1 octet 

## 3.4.2 Flag Field

The FIS-B frame starts and ends with a "Flag" octet, which is used for framing.  The flag octets shall have the value 01111110 binary, as specified by the ISO 3309 HDLC standard.  

## 3.4.3 Data Transparency Processing

ISO 3309 specifies two alternative procedures for ensuring data transparency (i.e., dealing with occurrences of the flag octet (see 3.4.2 above) within the frame).  The first alternative is designed for synchronous transmission (as a string of bits), while the second alternative is designed for asynchronous transmission (as a string of 8-bit octets). 

## 3.4.3.1 Synchronous Transparency Processing

If the FIS-B frame processing is using synchronous (i.e., bit-serial) transmission, the standard HDLC zero-insertion protocols (often called "bit-stuffing") for synchronous transmission (as specified in ISO 3309 Section 4.5.1) shall be followed to insure that the 
"flag" bit pattern does not occur within the frame itself.  The frame generator processing will examine the frame contents between the two flag octets and will insert a "0" bit after all sequences of 5 contiguous "1" bits.  The frame receiver processing will examine the frame content and will discard any "0" which directly follows 5 contiguous "1" bits. 

## 3.4.3.2 Asynchronous Transparency Processing

If the FIS-B frame processing is using asynchronous (i.e., octet-serial) transmission, the standard "control-octet transparency" protocols for asynchronous transmission (as specified in ISO 3309 Section 4.5.2.2) shall be followed to insure that the "flag" octet does not occur within the frame itself.  The bit pattern of the "control escape octet" is shown below (the low-order bit of the octet is transmitted/received first). 

Bit position in the octet: 1 2 3 4 5 6 7 8 

 
 
 
1 0 1 1 1 1 1 0 
 
The frame transmitter processing will examine the frame contents between the two flag octets (after completion of the FCS calculation (see 3.4.7 below) and will perform the following procedure whenever a flag octet or control escape octet is detected in the data: 

(1) Complement the 6th bit of the octet 
(2) Insert a control escape octet immediately preceding the octet modified in Step (1) 
above. 
The frame receiver processing will examine the frame contents between the two flag octets and will perform the following procedure prior to the calculation of the Frame Check Sequence (FCS) (see 3.4.7 below).  When a control escape octet is detected in the frame contents: 

(3) Discard the control escape octet 
(4) Restore the immediately following octet by complementing its 6th bit. 
These procedures ensure that the flag octet pattern will not be detected within the data of the FIS-B frame when asynchronous transmission is being used. 

## 3.4.4 Address Field

FIS-B frame addressing shall be in either ISO 3309 format or exceptions as outlined in Appendix F.  The following subparagraph describes an ISO 3309 Minimum Addressing format.  In either case, the source address field of the FIS-B frame shall be available to the APDU decoding process. 

## 3.4.4.1 Minimum Addressing

The Minimum Addressing format shall completely suppress the Destination Address subfield.  The Source Address sub-field shall be used to designate the source of the broadcast frame.  The Source Address sub-field shall contain the vendor identification code whose value shall be in the range 1-254.  At the vendor's option, 1 to 3 additional source address octets beyond the vendor identification code may be included in the source address to provide additional ground-station identification or other vendor-specific information.  In accordance with ISO 3309, the upper 7 bits of each source address octet shall be used for user application.  The low-order, 'E', bit of each source address shall be used to indicate field extensibility.  If the 'E' bit of an octet is set to 1, the source address field shall end with that octet.  When the 'E' bit of an octet is cleared to 0, the source address field shall include further octets.  The 7 user-specifiable bits of each source address octet in the frame shall be concatenated to form the complete source address value. 

## Notes:

1. ISO 3309 requires that the high-order octet of the source address (might be the only 
octet) cannot have the value of zero or 255.  
2. For those sources of FIS-B requiring only identification of the "provider" in the 
source address field, one octet of source address is sufficient to specify up to 126 
"providers." If identification of the broadcast origin is required in the source 
address field, two octets of source addressing yields 16,128 "site" identifiers. 

## 3.4.5 Link Control Field

The Link Control field of all FIS-B frames shall contain the 8-bit value 11000000, indicating that the frame is an Unnumbered Information (i.e., broadcast) frame as specified in ISO/IEC 4335, Section 7.3.2.  Link Control Field bits are transmitted from left-to right, as indicated in Figure 3-3. 

## 3.4.6 Information Field

The information field shall contain a complete FIS-B APDU.  If the FIS-B UI frame fails the error detection test described in Section 3.4.7, the information field contained in that frame shall be discarded. 

Note: 
The information field always contains a complete APDU because reassembly 
cannot be performed on partial APDUs.  A maximum length specification from 
the provider is desirable to allow for sizing of avionics buffers. 

## 3.4.7 Frame Check Sequence (Fcs)

The APDU shall be verified by means of the two-octet Frame Check Sequence specified in ISO 3309, Section 4.6.2. 

## 3.5 Network Layer

Provision shall be made for a simplified network layer consisting of only sub network protocol identification as further defined in Section E.2, "FIS-B Product Identifier."  The initial field of the APDU, termed the Subnetwork Access Protocol (SNAcP) field 
(Section D.1) is used for this purpose.  No other network layer functions are performed.  

## 3.6 Application Service Element

The FIS-B ASE segments on the ground and reassembles in the air, large data units (files) for an FIS-B application product.  A description of the ASE segmentation and reassembly services is given in Section 3.6.2.  The ASE also provides application product filtering and data conversion services as specified in Section 3.6.3.  These services are described in an abstract manner and do not imply any particular implementation.  An overview of the FIS-B data flow is shown in Figure 3-4.  

## 3.6.1 Application Protocol Data Unit (Apdu)

APDUs are the smallest incremental units of data conveyed to the airborne FIS-B 
Application Layer.  APDUs are inherently of one of two types depending on the application and the system design: 

a. *Independent* in that receipt of a single APDU of that type will result in some data that 
can be accessed by the pilot independent of any that precede or follow it. 
b. *Linked* in that receipt of an APDU of this type is part of a larger sequence of APDUs, 
and may not be accessible to the pilot until others in the sequence of APDUs are received and converted to a Product File. 
The APDU shall consist of a Header and a Payload.  The specific format for the APDU 
Header shall be as provided in Appendix D.  The specification for the Payload is given in the FIS-B Product Registry (see Appendix E for information on the FIS-B Product Registry).  The Payload contains all or segmented portions of an FIS-B Product File as described in Section 3.6.2.2. 

## 3.6.1.1 Apdu Header

Note: 
The Header is described in Appendix D. 

## 3.6.2 Segmentation Into Apdus And Reassembly

This network capability will allow the segmenting of large FIS-B Product Files from the network user for transmission from ground to air.  Reassembly of the large FIS-B Product Files will be performed at the receiving end of the broadcast network. 

## 3.6.2.1 Apdu Length

The total length of the APDU in octets is the sum of the fixed Header lengths defined by this document and the manufacturer-defined Payload length.  There is no requirement for the length of the total APDU.  The APDU shall be contained in the information field of an UI frame.  There is no need for an APDU length requirement because the APDU is 
"framed" in the DLS sublayer.   
Note:  The length of the APDU is constrained by manufacturer and industry requirements.  For example, the VDL SARPs Section 6.4.4.1.1 states that the minimum transmission length that a receiver will be capable of demodulating without degradation of bit error rate is 131,071 bits.  

## 3.6.2.2 Segmentation Of Product File Into Linked Apdus

The Processing and APDU Generation function (refer to Figure 1-1) shall perform segmentation when the size of an FIS-B Product File is greater than the maximum APDU 
Payload defined.  Segmentation consists of composing two or more APDUs from the Product File.  All of the APDU Header information, with the exception of the APDU 
Number (Section D.5.2), is duplicated in each linked APDU.  
The user data encapsulated within the Product File shall be divided such that the linked APDUs satisfy the size requirement for the Payload.  Linked APDUs shall be identified as being from the same initial Product File by means of the APDU Header, with the exception of the APDU Number, which is different for each linked APDU. Each APDU shall be included in the information field of an ISO High-level Data Link Control (HDLC) UI frame.  Only one complete APDU shall be included in an HDLC UI frame.  This is because frames containing errors will be rejected at the frame layer. When a frame is dropped at the link layer, a single APDU will be lost and, if retransmitted, could potentially be recovered by the ASE.  The ASE will not be able to recover partial APDUs. 

The frame check sequence (FCS) defined in section 3.4.7 provides for integrity checking of each APDU received - it does not provide for end-to-end integrity checking when a Product File is segmented into multiple APDUs.  In addition to the integrity check provided to individual APDUs, a sequence of linked APDUs should also employ an integrity check across the entire assembled payload.  This applies to both textual and graphic products. 

## Notes:

1. Any missing APDUs in the linked sequence will result in an invalid Product File 2. Compression techniques used with Product Files requiring linked APDUs may 
incorporate acceptable integrity checks.  For text products the 32-bit Adler checksum 
used in the ZLIB technique (Appendix D.2.2.5) or equivalent, is acceptable.  For nontext (i.e., graphical) products, the PNG and MNG graphical compression methods 
(see Appendix D.2.2.5) incorporate a 32-bit Adler checksum integrity check function 
that is acceptable.  The Weather Huffman graphical compression method (see 
Appendix D.2.2.4) also incorporates an acceptable end-to-end integrity check 
function as part of its design. 

## 3.6.2.3 Reassembly Of Linked Apdus To Form An Fis-B Product File

The re-assembly function shall reconstruct the Product File from the linked APDUs generated by the segmentation function performed on the Product File.  The re-assembly function shall be performed on APDUs with the same APDU Header, with the exception of the APDU Number, which is different for each APDU containing a segment of a Product File. 

In the receiver, the APDU Header information shall be used to reassemble the Payload from each APDU of a sequence to form the FIS-B Product File as shown in Figure 3-5. 

Separate APDU sequences are maintained for each Product and ground station combination for which linked APDUs are transmitted.  If, after the application service has received the last APDU of the FIS-B Product File, there are APDUs missing, then the application service shall do one of the following:  

a. discard the sequence,  
b. pass the sequence on to the application with missing APDUs, or c. wait for the missing APDU(s) to be retransmitted.  
In the case of segmented textual Product Files, missing APDUs that are unavailable from retransmission shall result in discard of the entire Product File.  APDUs that are still under the control of the re-assembly function shall be discarded when an APDU is received for the same product with more recent time data (a more recent version of the same product). 

## Notes:

1. The application service can replace the missing APDUs from a subsequent 
retransmission of the Product File.  Replacing missing APDUs with APDUs from a retransmission of a Product File improves the reliability of a broadcast link because, in general, the probability is low for there to be an error in the same APDU from two separate transmissions of the same Product File.  The actual probability of an error occurring in two APDU transmissions separated in time is dependent on the error characteristics of the channel and the size of the APDU. 
2. It is possible for the ASE to pass graphical application product data to an 
application even though some of the independent APDUs contained in the file are missing because there are some graphical weather applications that can be viewed 
despite missing data.  If the missing graphical APDUs are subsequently received, it is permissible to pass them to the application. 

## 3.6.3 Application File Selection And Conversion

The ASE may choose to discard APDUs based on data contained in the APDU Header field.  The ASE can discard an APDU if any of the following situations are encountered: 

a. An APDU is received, but due to processing limitations, it cannot be processed. 
b. An APDU is received whose header or payload cannot be analyzed. c. An APDU is received that contains an unsupported option. 
Data uncompression and geographic reference conversions are performed on the application data contained in the Payload field by the ASE.  The APDU Header fields are passed, as needed to the FIS-B application with the FIS-B Product File. 

## 3.7 Fis-B Application Layer

The FIS-B Product Identifiers and the Payload specifications for each FIS-B Product File are contained in the FIS-B Product Registry (see Appendix E for information on the FIS-
B Product Registry). 

## 3.8 Design Guidelines & Recommended Standards For Airborne Processing & Display Of Fis Products

This guidance is applicable to any cockpit display of FIS information in the flight deck/cockpit.  It is anticipated that most avionics for the airborne processing and display of FIS products will be approved using existing type certification or supplemental type certification processes such as the current version of TSO C113, Airborne Multipurpose Electronic Displays.  Consequently, this document only contains guidance for airborne processing and display of information that is unique to FIS-B and independent of other functions such as terrain and obstacles, and traffic that are governed by other directives. 

Notes:  

1. The guidance in this section is not exhaustive relative to all FIS products.  The 
absence of guidance does not imply that further requirements may not emerge.  For 
example, ongoing research and development will contribute to the basis for further FIS product definitions (e.g., product animations or "looping" are current topics of intensive prototyping and human factors investigations). 
2. When FIS products are integrated into multi-purpose flight deck displays of the type 
now generally found on air carrier aircraft, it is understood that the FIS information may need to be altered to maintain consistency with other conventions and requirements, the design philosophy of the flight deck, the display context, and the 
intended task.  Section 3.8.3 provides guidelines on integrated displays combining 
layers of FIS products (text and graphic).  Manufacturers should follow these 
guidelines to the maximum extent practical.  These guidelines support displaying FIS 
information on multi-function displays that provide supplementary situation 
awareness information such as GPS moving map display.  This supports flight crew 
members in correlating the FIS information with information used in other venues such as industry aeronautical educational information, service provider weather 
information, or to aid in achieving convention commonality with other aircraft installations. 

The following standards and practices contain general design guidance for avionics displays and should be used in the design and approval of FIS-B processing and display subsystems. 

a. RTCA 216-96:  Human Engineering Recommendations for Data Link Systems 
b. SAE 
Aerospace 
Recommended 
Practice 
ARP4032: 
Human 
Engineering 
Considerations in the Application of Color to Electronic Aircraft Displays 
c. SAE Aerospace Minimum Performance Standard AS8034: Minimum Performance 
Standard for Airborne Multipurpose Displays 
d. SAE Aerospace Recommended Practice ARP5364: Human Factors Criteria for the 
Design of Multifunction Displays for Civil Aviation 
e. AC 23.1309.1C: Equipment, Systems, and Installation in Part 23 Airplane (latest 
revision) 
f. AC 23.1311-1: Installation of Electronic Display Instrument Systems in Part 23 
Airplanes, (latest revision) 
g. AC 25-11:  Transport Category Airplane Electronic Display Systems h. AC 25-1309A: "System Design and Analysis" i. 
AC 120-76A: Guidelines for the Certification, Airworthiness, and Operational Approval of Electronic Flight Bag Computing Devices 
j. 
TSO C113: Airborne Multipurpose Electronic Displays 
k. TSO C165: Electronic Map Display Equipment for Graphical Depiction of Aircraft 
Position 

## 3.8.1 Airborne Processing And Display

The following minimum requirements and guidelines are provided to establish standard methods and practices in processing and displaying FIS products.  In the cockpit environment, the information being conveyed by any FIS product should be quickly discernable by the pilots.  Five key elements that shall be intuitive and easy to interpret in every FIS product are: 

a. the information contained in the product (3.8.1.1); 
b. the currency or age of the product (3.8.1.2); 
c. the method for displaying/decoding the product (3.8.1.3); 
d. the location/mapping of the product (3.8.1.5); and 
e. a positive, unambiguous indication of any missing data within the product (3.8.1.4). 
Any FIS information beyond the required key elements listed in Section 3.8.1 that is presented on the FIS cockpit display shall not interfere with the readability of those key elements. 

## 3.8.1.1 Product Title

Each display page providing FIS information shall clearly indicate to the pilot the information displayed, and weather-related pages shall distinguish between weather observations and forecast information. 

## 3.8.1.2 Product Age

A means for the pilot to determine the age of the product shall be included on each page or each data set.  

a. **Integrated Product:**  Data formats consisting of overlays of dissimilar data sets with 
different generation and/or valid times shall include a means for the pilot to 
determine the age of each of the data sets. 
b. **Sequential or Looping Product:**  If a sequential data set is replayed, there shall be 
an indication of the age of each data set in the sequence during replay. 

## 3.8.1.2.1 Weather Product Age

The method for determining the currency or age of FIS weather applications is based on the product date/time(s) for the specific weather product.  The product date/time(s) will depend on the type of product as described below and shown in Table 3-2.  Any specific product times should be expressed in Coordinated Universal Time (UTC) (Zulu) time. 

a. **Observations.**  For individual observations, the date/time that the specific data is 
observed is the product date/time.  The observation date/time shall be indicated on all 
displays of individual observation reports or subelements of those reports (e.g., METARs, SPECIs, PIREPs and individual NEXRAD reports). 
b. **Forecasts.**  For most forecast products, there are two separate, but necessary product 
date/times: the date/time that the overall forecast product was issued; and the valid forecast time or times (e.g., the start and stop times of a Terminal Area Forecast). Both the issue date/time and the valid forecast time(s) shall be indicated on all 
displays of individual forecast products. 
Note:  Forecast products include NOWCASTS as well as aviation advisories and 
warnings such as SIGMETs and AIRMETs.  NOWCASTS are weather products, which generally include short-term predictive descriptions of weather conditions, 
based on inputs from multiple weather data sources. 
c. **Composite/Mosaic Products.**  (Section 2.2.11).  This category of product is based 
on a summary or composite presentation of multiple individual observations (or forecasts).  The date/time that the last individual report was incorporated (the cut-off date/time) into the product is the product date/time.  Indication of product age should be readily apparent to the pilot such that the pilot will not need to calculate the 
product's age based on its date/time. 
d. **Incremental Display Update of NEXRAD Graphics (Single Site or Mosaic)**.  If 
the cockpit display of NEXRAD Graphics is updated in an incremental fashion, the 
following guidelines apply.  As APDUs with new data (later observation time for single sites, or cut-off time for mosaics) are received, they are integrated directly into the cockpit display, replacing that incremental portion of the display contained in that APDU. 

1. The product time displayed shall be the time of the oldest source product (time 
observed for single site or cut-off time for mosaic) that contributes to the displayed image. 
2. The time span between the oldest and newest source product contributing to the 
displayed image shall not exceed 10 minutes.  Portions of the image that exceed this 10 minute requirement shall be depicted as missing data (see Section 
3.8.1.4). 
3. This incremental display technique should not be used as the basis for a 
Sequential or Looping Product (See Section 3.8.1.2). 

## Notes:

1. The source products for this NEXRAD cockpit display could be either single site 
NEXRAD observations or NEXRAD mosaics products (e.g., base reflectivity).  This guidance seeks to limit the maximum age difference of the data contained in these 
displays. 
2. If the source product is a mosaic, the total time difference of the data contained in the 
displayed product could be 20 minutes. 

Display Time Indications (Date/Time and/or Age of Data) 
Type of FIS 
Product 
Time 
Observed 
Time 
Issued 
Valid 
Stop/Start 
Cut-Off 
Time (last 
data entry) 
 Oldest Time 
Observed 
(Single Site) or 
Cut-Off Time 
(Mosaic) 
Individual Reports / Observations 
X 


Forecasts 
/ 
Advisories/ Nowcasts 
 
X 
X 
 
 
Composite / Mosaic Observations 


X 
 
Incremental NEXRAD Update 


X 
 

## 3.8.1.3 Product Legend

The meaning of the color-coding and symbology for any FIS product display shall be available to the pilot on a legend.  That legend should be accessible via no more than a single operator action. The legend may optionally describe FIS/weather data set characteristics such as the following: 

a. Maximum update interval for incorporating new data into the product(s). 
b. Maximum retransmission interval for initiating a broadcast/transmission of the 
product(s). 
c. The source of the product or specific production algorithm for weather products (e.g., 
FAA, NWS, private vendor, etc). 
d. Confidence level for weather product when available with corresponding legend 
(e.g., 10 on a scale of 1-10). 
e. Notification criteria for weather information. 

## 3.8.1.4 Missing Data

Graphical display presentations shall show a positive and unambiguous indication and location of data that is known to be corrupted or missing.  Examples include: 

a. Indicating those areas of missing coverage within the region displayed that are 
beyond the approximate limits of weather radar coverage, if known and available. 
b. Indicating radar sites and lightning sensors that are not reporting within the region 
displayed. 
c. Indicating areas of missing data within the region displayed due to lost data packets 
or APDUs, not available when decoding or reassembling the display presentation. 

## 3.8.1.5 Product Mapping Or Location

Graphical displays shall clearly indicate the geographic area covered, and, when applicable, the vertical height(s) for the product (e.g., 3000 ft, 3000-5000 ft, ABV 12,000 
ft). 

a. The display may incorporate Range Rings (e.g., 50 NM, 100 NM) that clearly 
indicate the location represented at the center of the rings, or the aircraft's position relative to the center of the rings. 
b. The FIS/weather information display may also indicate the location of the own-ship 
aircraft on the map and the flight plan or route of flight. 

## 3.8.1.6 Text Product Format Criteria

Character Sets.  FIS textual products are formed as a variable-length sequence of fixedlength elements (termed "characters"), drawn from a predefined collection (termed "character set").  Two character sets are defined for FIS-B transmission of textual products.  One of the following character sets shall be used. 

a. **ASCII.**  The ASCII character set (WMO Telegraph Alphabet Number 5) is assumed 
unless otherwise specified in the product description.  Each FIS textual ASCII character occupies 8 bits (with the high-order bit cleared to zero) which provides byte 
alignment for each character.  The ISO specification for ASN.1 using PER encoding 
(International Alphabet Number 5 - See Appendix C for reference) may be used to 
generate an equivalent character representation for FIS textual products. 
b. **DLAC.**  The DLAC 6-bit character set (Data Link Applications Coding) is an 
alternative character set, described in Appendix K.  An example of use is the 
"Generic Textual Data Product, Type II (DLAC)," Payload Encoding 5.8 described 
in the FIS-B Product Registry (See Appendix E; or access at: http://fpr.tc.faa.gov). 
Control Functions.  FIS textual reports may use special "control functions" to support product display formatting or to delimit individual reports within a given APDU payload. There are characters within each of the character sets defined above (ASCII or DLAC) to indicate these functions. 

End-of-Line.  FIS textual reports will consist of sequences of characters taken from one of the defined character sets above.  A single report shall consist of one or more logical text lines, each line separated using the End-of-Line sequence from the selected character set.  Separate carriage return and line feed characters are used in the ASCII character set and just the CRLF character is used in the DLAC character set to denote End-of-Line. 

Record-Separator.  When multiple FIS textual reports are grouped into an APDU 
Payload, each single report shall be separated using the Record-Separator from the selected character set. 

Line Break.  The line break is assumed at the end of each FIS textual report, thus there is no need to use an End-of-Line sequence prior to a Record-Separator. 

Last Report.  The last FIS textual report in an APDU payload is terminated with an ASCII End-of-Text character or a DLAC End-of-Line sequence rather than a Record-
Separator. 

## 3.8.1.7 Text Product Display Features

Text should follow the general guidelines for multi-function displays (MFD) with respect to size, ease of reading, etc. 

a. **Text Case.**  Upper case text should be used for captions, headings, titles, and coded 
information (e.g., ICAO-formatted METARs).  Mixed case should be used when 
presenting continuous textual information (i.e., sentences, and paragraphs) because it 
is read faster than upper case. 
b. **Text Breaks or Hyphenation.**  Lines of text should be broken only at spaces or 
other natural delimiters for coded products, such as METARs and TAFs, to prevent 
ambiguous interpretation.  Line breaks shall not occur in numerical values containing 
spaces.  For example, visibility is often stated in main and fractional portions with an 
intervening space.  These values shall always remain together on the same line of the display. 
1. Text other than coded information (e.g., plain language forecasts) may be broken 
at the end of a display line using hyphenation between syllables in words. 
2. Where multiple textual reports are combined into an APDU payload, the text 
should be broken at the boundary between products and a prominent indication 
should be provided on the display to separate the products. 
c. **ICAO or Equivalent Display.**  Textual weather reports (e.g., METARs, TAFs) and 
NOTAMs shall either be displayed in their original ICAO format as modified by the 
reporting States or in alternate formats that represent the original content.  If the 
integrity of the original text cannot be demonstrated using the alternate formats, the original report shall be available for display in its unaltered ICAO format. 

Note:  The ICAO formats for METAR and TAF reports are defined in Annex 3 with 
differences filed by the reporting States as contained in appendices 4 and 5.  The 
ICAO formats for NOTAMs are defined in Annex 15.  

## 3.8.1.8 Data Blocks

There may be objects on the display or a portion of the display that have other useful information associated with them. The following guidelines apply to the depiction of data blocks: 

a. There should be a clear and consistent indication or documentation of which portions 
of the display contain additional information (associated data blocks).   
b. There should be a clear and unambiguous indication of the symbol or display region 
with which the data block is associated. 
c. There should be a means of quickly eliminating the data block if it is obscuring other 
information. 

## 3.8.1.9 Symbols

Symbols may be used to graphically represent operations, processes, and data as well as to exercise display control.  Symbols should be recognizable from a normal viewing distance as defined in ARP4102/7.  Symbols should be consistent across applications and operations as well as aviation weather standards, e.g., wind barbs. 

## 3.8.1.10 Combined Graphical And Textual Displays

When product reports comprise both graphical and textual records, a means shall be provided for the pilot to associate both records and, at a minimum, access and display the textual component of the report. 

## 3.8.1.11 Multiple Page Displays

When the FIS product presentation requires more than one page for display, an indication should be prominently displayed on each page that a next or previous page exists.  Only one action should be required to scroll to the next or previous display page of a multipage FIS product presentation. 

## 3.8.1.12 General Display Features

An indication should be given that the system is processing information (e.g., when a composite product is requested for display).  The indication should be continuous, so that any interruption of processing is recognizable to the user. A means to notify the pilot of AIRMETs, SIGMETs and convective SIGMETs received during flight may also be available through the weather display. The FIS display pages (e.g., location of titles, specification of valid times, use of color and symbols, etc.) should be consistent to reduce training requirements, workload, and errors. 

The pilot shall have the capability to de-clutter the display relative to FIS information. 

## 3.8.2 Use Of Color, Textures And Symbols

The use of color in FIS displays is recommended, but is not required. 

## 3.8.2.1 Color Philosophy In Fis Graphics

The color philosophy for FIS graphics is based on the Operational Applications as described in Section 1.3.  It is understood that there are limited number of options manufacturers will have with regard to display graphics, therefore it is expected that there may be some reuse of the same or similar display methodologies in multiple display contexts. 

a. Information displayed for purposes of FIS shall enable the crew to clearly identify the 
content as being an FIS product, which is for information purposes only.  The use of 
display graphics should be applied consistently with the guidance described in this 
section. 
b. Within the FIS context, FIS products may use the green-yellow-red-magenta color 
scheme to represent increasing intensity or severity of condition.  The use of these 
colors should be applied consistently within FIS products (see Sections 3.8.2.1.1 and 
3.8.2.1.2). 
c. To ensure compatibility between the FIS context and other contexts, such as crew 
alerting, higher priority information contained within a crew alerting display shall not 
be superceded by FIS information as described in Section 3.8.3. 
For FIS products including weather information, a consistent color philosophy should be used throughout the display (across applications) which is appropriate in the context of the information being displayed.  To the greatest extend practical, colors should be in harmony with other sources of similar information, and maintain consistency with legacy weather graphics and systems, and flight deck design.  A limited number of colors should be used in a cockpit display to minimize pilot interpretation workload. 

FIS products are to be used for advisory and strategic/planning purposes and not for crew alerting.  This is due to the fact that FIS products may have significant latency between the observations of a weather phenomenon, the issuance of a forecast, or the change in airspace status; and the display of that information in the cockpit.  In addition, because their update rates are low, FIS products should not be used for tactical maneuvering of the aircraft, and should not be the sole basis for immediate corrective action by the pilot.  
FIS products are intended to enable pilots to determine if action should be taken well before it is required, and should be used in conjunction with other information sources to support in-flight decisions.  

## 3.8.2.1.1 Fis Graphics - Weather

Single Weather Phenomenon.  For FIS products depicting a single weather phenomenon with increasing levels of intensity or severity (e.g., turbulence, convection, icing, ceilings, visibility, and surface temperature and winds), a color scale of greenyellow-red-magenta may be used to indicate the increasing intensity (or severity) of condition.  

Note:  A subset or a superset of the above color scale may be used.  For graphical 
depictions of a single weather phenomenon the use of red or magenta should be 
reserved for intensities that represent the most intense or severe conditions.  It should be noted that what constitutes a severe condition for a given flight is a 
function of many factors including the type of aircraft; optional airborne equipment; the type of flight operation; the training level and certification of the 
flight crew; and the flight policies of the operator.  For example, while widespread low ceilings and visibility rarely pose a severe condition to part 121 (scheduled air carrier) operations, such conditions represent a serious threat to 
pilots who are constrained to flight in visual meteorological conditions due to either equipment or training/certification limitations.  
Multiple Weather Phenomena.  It is recognized that color may also be used to depict different meteorological conditions and may not be limited to describing the intensity or severity of a particular condition.   An example is an integrated display that depicts regions or areas of icing, turbulence, and convection simultaneously. 

a. In the case of combining multiple weather phenomena on a single display, there shall 
be a consistent approach for depicting various weather phenomena.  
b. There shall be a clear differentiation between the weather phenomena.  Color is one 
technique to differentiate between the weather phenomena; the use of symbology is 
another technique (e.g., 'X' to denote lightning strikes). 
c. When color is used, its application should follow the guidelines in Section 3.8.3, and 
restrict the use of the color red to weather phenomena representing a potential hazard 
to flight operations. 

## 3.8.2.1.2 Fis Graphics - Airspace

Red may be used to depict airspace in which some or all flight operations are prohibited, subjecting transgressors to intercept and shoot-down policies.  These would include airspace placed under temporary flight restriction (TFR) and prohibited areas (PA). 

## 3.8.2.2 Color & Symbol Characterization Chart

To provide standardization when displaying weather phenomena, the table below provides definitions for weather conditions, sample display colors, and in some cases, sample display characters or symbols.  The weather condition definitions are based on well established and recognized conventions.  This table is not an exhaustive list of all FIS weather products. 

Note: 
For the Precipitation Products, see Appendix H (Section H.12 and Table H-5) for 
the basic radar intensity levels (dBZ) associated with VIP 1 - VIP 6.  The VIP 1 - VIP 6 were selected as the Weather Condition definition to provide close correlation between displays of FIS Precipitation Products and installed airborne weather radar systems.  There may be some small variations (e.g., 1-2 
dBZ) in the "VIP" quantization levels (dBZ) of Precipitation Products (e.g., NEXRAD mosaics) from different sources; such variations are acceptable. 

| Weather Conditions                                                        | Color                            | Character/Symbol    | Reference    |
|---------------------------------------------------------------------------|----------------------------------|---------------------|--------------|
| Precipitation Products                                                    |                                  |                     |              |
| 1                                                                         |                                  |                     |              |
| (derived in part from radar)                                              |                                  |                     |              |
| No weather                                                                | Display background (distinct     |                     |              |
| from radar intensity colors)                                              |                                  |                     |              |
| None                                                                      |                                  |                     |              |
|                                                                           |                                  |                     |              |
| Missing Data                                                              | Distinctive color or texture not |                     |              |
| used for background or other                                              |                                  |                     |              |
| display elements                                                          |                                  |                     |              |
| Distinctive character                                                     |                                  |                     |              |
| or texture not used for                                                   |                                  |                     |              |
| other display elements                                                    |                                  |                     |              |
| VIP1: up to 30 dBZ                                                        |                                  |                     |              |
| 2                                                                         |                                  |                     |              |
|                                                                           |                                  |                     |              |
| Green                                                                     | "L"    optional                  | AC 25-11            |              |
| VIP2: >30 -                                                               |                                  |                     |              |
| ≤                                                                         |                                  |                     |              |
| 40 dBZ                                                                    |                                  |                     |              |
| Amber or yellow                                                           | "M"   optional                   | AC 25-11            |              |
| VIP3 (or greater): >40 dBZ (>40 -                                         |                                  |                     |              |
| ≤                                                                         |                                  |                     |              |
| 45                                                                        |                                  |                     |              |
| dBZ if optional VIP levels used)                                          |                                  |                     |              |
| Red                                                                       | "H"    optional                  | AC 25-11            |              |
| (optional)VIP4: >45 -                                                     |                                  |                     |              |
| ≤                                                                         |                                  |                     |              |
| 50                                                                        |                                  |                     |              |
| Red                                                                       |                                  |                     |              |
| 3                                                                         |                                  |                     |              |
|                                                                           |                                  |                     |              |
| (optional) VIP5: >50 - 54 dBZ                                             | Magenta                          |                     | AC 25-11     |
| (optional)VIP6:                                                           |                                  |                     |              |
| ≥                                                                         |                                  |                     |              |
| 55 dBZ                                                                    |                                  |                     |              |
| Magenta                                                                   |                                  |                     |              |
| 3                                                                         |                                  |                     |              |
|                                                                           |                                  |                     |              |
| Snow or frozen precip                                                     | Blue                             |                     |              |
| 4                                                                         |                                  |                     |              |
|                                                                           | "S"                              |                     |              |
| Mixed or unknown precip                                                   | Pink                             |                     |              |
| 4                                                                         |                                  |                     |              |
|                                                                           |                                  |                     |              |
| (optional) Storm information, eg, echo                                    |                                  |                     |              |
| tops, storm velocity                                                      |                                  |                     |              |
| Light gray or white                                                       |                                  |                     |              |
|                                                                           |                                  |                     |              |
| Lightning                                                                 |                                  |                     |              |
| White or high intensity yellow                                            |                                  |                     |              |
| "X" or "Z" or "+" or                                                      |                                  |                     |              |
| "."                                                                       |                                  |                     |              |
|                                                                           |                                  |                     |              |
|                                                                           |                                  |                     |              |
| National Convective Weather Forecast (NCWF)                               |                                  |                     |              |
| 5                                                                         |                                  |                     |              |
|                                                                           |                                  |                     |              |
| NCWF Hazard Levels:                                                       |                                  |                     | AIM Ch 7     |
| Current Convection                                                        |                                  |                     | "            |
| 1                                                                         | Green                            |                     | "            |
|                                                                           |                                  |                     |              |
| 2                                                                         | Amber or yellow                  |                     | "            |
|                                                                           |                                  |                     |              |
| 3                                                                         | Red                              |                     | "            |
|                                                                           |                                  |                     |              |
| 4                                                                         | Red                              |                     |              |
| 3                                                                         |                                  |                     |              |
|                                                                           |                                  | "                   |              |
|                                                                           |                                  |                     |              |
| 5                                                                         | Magenta                          |                     | "            |
|                                                                           |                                  |                     |              |
| 6                                                                         | Magenta                          |                     |              |
| 3                                                                         |                                  |                     |              |
|                                                                           |                                  | "                   |              |
|                                                                           |                                  |                     |              |
| Forecast (1 Hr)                                                           |                                  |                     |              |
| ≥                                                                         |                                  |                     |              |
| Hazard Level 3                                                            |                                  |                     |              |
| Cyan                                                                      |                                  | "                   |              |
|                                                                           |                                  |                     |              |
|                                                                           |                                  |                     |              |
| Graphical Representations of Point Observations of Ceiling and Visibility |                                  |                     |              |
| 6                                                                         |                                  |                     |              |
|                                                                           |                                  |                     |              |
| (optional) Visual Flight Rules (VFR)                                      | Sky blue or green                |                     | AIM Ch 7     |
| Marginal Visual Flight Rules (MVFR)                                       | Green                            |                     | "            |
| Instrument Flight Rules (IFR)                                             | Amber or yellow                  |                     | "            |
| Low Instrument Flight Rules (LIFR)                                        | Red or Magenta                   |                     | "            |
| (optional) Less Than CAT 1                                                | Magenta                          |                     | "            |
|                                                                           |                                  |                     |              |

## 3.8.3 Integrated Display Formats Combining Layers Of Fis Graphics And Text

The following guidelines are provided for presentation of FIS graphics and text in integrated cockpit displays that combine FIS information with navigation and other information. 

                                                     
 

a. In integrated display formats that combine weather and navigation information, the 
current position of the aircraft with respect to its planned flight route should not be 
obscured by FIS data symbols.  The use of red or magenta to depict the most intense or severe FIS conditions on a multi-function display shall not degrade their use in other graphics with crew alerting functions, such as TCAS, TAWS and surface 
movement alerts as described by their respective regulatory documents.  Information 
should be prioritized in accordance with its criticality.  Lower priority information, 
such as FIS products, shall not mask higher priority information, such as alerts or annunciations. 
b. Information displayed in textual form such as METARs, TAFs, and NOTAMs should 
not be overlaid on a map display except to amplify or explain concisely the meaning of a graphical feature.  These products can be provided on a separate page or screen region, since they are generally referred to by the pilot when needed and not monitored on a continuous basis. 
c. If a display system incorporates a decision support function, and if the decision 
support function determines that a particular non-FIS event requires immediate pilot attention, the display of FIS information shall not adversely impact crew alerting. 
Note:  One means of accomplishing this is to suppress the display of the FIS product and 
declutter the screen.  In this case, the pilot should be made aware that the display of FIS data is suppressed and that the non-FIS event needs immediate attention. The FIS product may not be restored to the display until either the pilot positively acknowledges the non-FIS event , or the event ceases to exist and disappears. 
d. A method to turn on and off individual layers of information should be available to 
the pilot. 
e. An indication of current displayed layers should be available to the pilot. 
f. When multiple categories of information are combined, an unambiguous method of 
differentiating between them should be provided. 
This page intentionally left blank. 

## 4 Procedures For Performance Requirement Verification

This section describes an acceptable means of showing compliance to the system and subsystem performance requirements in Sections 2 and 3, and Appendices D and F of this document as necessary.  Since the FIS-B performance requirements in this MASPS are medium independent, the communications interface and radio frequency (RF) segment are not included in this section.  It is anticipated that those segments will comply with existing or proposed standards.  Further, it is anticipated that avionics that will be certified for the airborne processing and display of FIS products will use existing type certification or supplemental type certification processes.  Thus, the focus of this section will be on the performance requirement verification of FIS-B functionality. 

A combination of analysis, inspection, demonstration and test as defined below is sufficient to substantiate compliance to the functionality requirements of this document. Flight demonstrations may not be required since the communications interface and RF segment will be verified separately.  The validation/verification process should take into account the assumptions given in Section 1.6 along with such factors as the intended use. 

The tests provide a means to verify functionality in FIS-B frame and APDU header processing, and FIS-B display conformance. 

## 4.1 Assumptions

The procedures were developed under the following assumptions: Testing and the associated verification and validation are required only for products sent across the FIS-B data link system(s) supported by the manufacturer.  Not all FIS-B 
Product Files contained in the FIS-B Product Registry (see Appendix E) will be included in the transmissions of a specific FIS-B broadcast system.  There is no requirement for testing or compliance associated with FIS products that are not supported by the manufacturer's system. Test procedures in this section will not exhaustively test all of the performance requirements in this MASPS document.  The Section 4.0 procedures provide test coverage for only the MASPS requirements that are practical to test given the fact that this MASPS addresses only a limited product set.  It is expected that the manufacturer would determine the method of verification of performance requirements outside the scope of these test procedures. It is expected that manufacturers with different implementations will use a source data set of their choosing to construct test inputs to show compliance with the MASPS requirements.  Determination of whether the pass/fail criterion has been successfully met at the output is generally accomplished by inspection of the display.  There may be other means for determining pass/fail success, such as analysis of the output data. 

Hardware access points for inserting test data and sampling output data are not specified but left to the discretion of the manufacturer, dependent upon the manufacturer's unique hardware configuration. 

## 4.2 Verification

Figure 4-1 below provides an overview of the system. 

One or more of the analysis, inspection, demonstration, and test methods, which are defined as follows, shall be used to verify requirements: 
Analysis - Verification by technical/mathematical evaluation using mathematical representations (i.e., models, simulation, algorithms), charts, graphs, drawings, and representative data.  One means of analysis could be a pixel-by-pixel comparison of the output-decoded product with the original data set. 

Inspection - Verification by visual examination or observation using representative documentation to compare appropriate characteristics with specific requirements. 

Demonstration - Verification by operation, movement or adjustment using qualitative criteria rather than measuring instruments and quantitative data to assure performance of functions and capabilities. 

Test - Verification by examination or trial under appropriate conditions using measuring instruments that yield analytical data for use in comparing measured performance against specific requirements. The test procedures set forth below constitute a satisfactory method of determining FIS-B performance.  Although specific test procedures are cited, it is recognized that other methods may be preferred.  Such alternate methods may be used if the applicant can show they provide at least equivalent information or verification.  Therefore, the procedures cited herein should be used as one criterion in evaluating the acceptability of the alternate procedures. 

## 4.2.1 Equipment Configuration

The equipment configuration is at the vendor's discretion and is expected to include system components as shown in Figure 4-1.  Tests in Section 4.3 are considered "bench tests" whereas tests in Section 4.4 are appropriate as bench tests or installed equipment tests. 

## 4.2.2 Sequence Of Verification

Table 4-1 and Table 4-2 propose the sequence in which verification tests are performed.  
However, other test sequences are acceptable and may improve testing efficiency or convenience. 

## 4.2.3 Standard Test Data

A representative FIS-B test data set will be data frames in binary form, under configuration control, for insertion at a point determined by the vendor to exercise the functionality being verified.  The test data set will also contain the original binary source data for comparison with the decoded and reassembled output product.  Appendix G contains a description of an example test data set for representative textual (e.g., METAR) and graphical (e.g., NEXRAD) reports that vendors may choose to use.  The functionality being verified is specified in Table 4-1 and Table 4-2.  The test data set will include reports containing errors to verify appropriate system responses.  The test data set will be used to demonstrate that the system can display the five key elements (Section 
3.8.1) 
of information: 
product type, report currency/age, the method of displaying/decoding the report, the location/mapping of the product, and a positive, unambiguous indication of any missing report data.  It is not intended that this data set support all possible conditions or types of errors.  The input reports will be uncompressed but could be used to demonstrate compression techniques as well as other options by changes to the APDU Header. 

## 4.3 Fis-B Frame And Apdu Header Processing

The FIS-B Frame and APDU Header Processing subsystems as described in Section 1.2 
(Figure 1-1, Steps 2 and 3) shall meet the functional requirements outlined in Section 2 
(beginning with 2.2), Section 3 (with any exceptions as contained in Appendix F), and Appendix D.  The presence of a legible (familiar characters arranged to represent common words, abbreviations, terms or other information), intact (coherent, whole) display (as compared with the source data/image) is considered evidence, where indicated in Table 4-1 and Table 4-2, that these functions are performed satisfactorily.  For example, display of mirror (reversed) images of the original product is not acceptable. FIS products contained in the test data sets will use the application layer protocol and APDU Header and meet the functional requirements as outlined in Sections 2 and 3.  The following table provides the minimum requirements for FIS-B cockpit avionics processing.  
The items tabulated below are associated with requirements contained in this document. Recommendations contained in this document may require additional verification beyond the scope of this section.  There is not one-to-one mapping of an item to a single requirement.  Each of the items may contain one or more individual requirements.  

| Pass / Fail Criteria     | Data Set                |
|--------------------------|-------------------------|
| Test                     |                         |
| Paragraph                |                         |
| Description              |                         |
| Requirement              |                         |
| Reference                |                         |
|                          |                         |
| Verification             |                         |
| Method                   |                         |
| A = Analysis             |                         |
| I = Inspection           |                         |
| D = Demo                 |                         |
| T = Test                 |                         |
|                          |                         |
| 2.2.1                    |                         |
|                          | A                       |
| transfer or compression. |                         |
| Graphical                |                         |
| test pattern             |                         |
| 4.3.2.1                  |                         |
| 2                        |                         |
| .                        |                         |
| Lossless process,        |                         |
| lossless                 |                         |
| compression              |                         |
| 2.2.3                    |                         |
| ,                        |                         |
| 3.4.7                    |                         |
|                          |                         |
| D                        | Data with errors are    |
| discarded                |                         |
| Textual test             |                         |
| reports                  |                         |
| 4.3.2.2                  |                         |
| 2                        |                         |
| .                        |                         |
| Verify data link         |                         |
| integrity (Frame         |                         |
| Check Sequence),         |                         |
| discard data with        |                         |
| errors                   |                         |
| Graphical                |                         |
| test pattern             |                         |
| 4.3.2.2                  |                         |
| 4                        |                         |
| .                        |                         |
|                          |                         |
| Frame Format             |                         |
| Processing,              |                         |
| Addressing, Control      |                         |
| 3.4.1                    | ,                       |
| 3.4.2                    |                         |
|                          |                         |
| 3.4.4                    |                         |
| ,                        |                         |
| 3.4.5                    |                         |
|                          |                         |
| D                        |                         |
|                          |                         |
| The FIS-B type data      |                         |
| displayed verifies the   |                         |
| Frame Format, its        |                         |
| processing, direct       |                         |
| addressing and control   |                         |
| are correct and in order |                         |
| within the FIS-B         |                         |
| Application              |                         |
| 4.3.2.2                  |                         |
| 4                        | .                       |
| Information Field        | 3.4.6                   |
| test pattern             |                         |
| Graphical                |                         |
| test pattern             |                         |
| 4.3.2.2                  |                         |
| 5                        | .                       |
| Network Layer            | 3.5                     |
| displayed verifies the   |                         |
| Network Layer identifier |                         |
| used was of type FIS-B   |                         |
| Application from the     |                         |
| APDU Header              |                         |
| 4.3.2.2                  |                         |
| 6                        | .                       |
| ASE for FIS-B            |                         |
| applications             |                         |
| 3.6                      | ,                       |
| 2.2.12                   |                         |
| D                        | Legible, intact display |
| test pattern             |                         |
| 4.3.2.2                  |                         |
| 7                        | .                       |
| APDU Format              | 2.2.13                  |
| 3.6.1                    | ,                       |
| Appendix                 | D                       |
|                          |                         |
| D                        | Legible, intact display |
| reports  &               |                         |
| graphical                |                         |
| test pattern             |                         |
| 3.6.2                    |                         |
| ,                        |                         |
| D.5                      |                         |
|                          |                         |
| D                        | Legible, intact display |
| test pattern             |                         |
| 4.3.2.2                  |                         |
| 8                        |                         |
| .                        |                         |
| Segmentation,            |                         |
| division among           |                         |
| linked APDUs and         |                         |
| reassembly               |                         |
| 4.3.2.2                  |                         |
| 10                       | .                       |
| APDU Payload             |                         |
| Encoding                 |                         |
| 3.8.1                    | ,                       |
| D.5                      |                         |
| D                        | Legible, intact display |
| reports &                |                         |
| graphical                |                         |
| test pattern             |                         |

## 4.3.1 Conditions Of Test/Test Objectives

The objectives of these tests are to verify that the communications format for encoding, decoding and broadcasting APDUs is consistent and accurate and that the cockpit avionics processing faithfully reassembles APDUs and assures the data integrity as outlined in this document.  It is not required, or necessarily desirable, that these tests be conducted in aircraft.  Only processing functions will be tested. 

## 4.3.2 Detailed Test And Demonstration Procedures

These procedures are developed to test individual performance requirements and, in many instances, are grouped with similar procedures to facilitate the verification process. 

## 4.3.2.1 Lossless Process, Lossless Compression Test Procedures

These test procedures will verify data are not lost from either transfer or compression. 

1. Insert the standard graphical test data set and view the graphical test pattern. 
2. By analysis, verify that the decoded APDU data matches the input source data set 
exactly, showing that data are not lost from either the transfer of the data or from any compression employed. 

## 4.3.2.2 Fis-B Frame And Apdu Header Processing Test Procedures

These test procedures verify requirements imposed in Sections 2.2 and 3.1, as shown in Table 4-1. 

1. Insert the standard textual test report.  Bits have been altered (after FIS-B frame 
checksum computation) to create an error and corrupt the data. 
2. Verify data with errors are discarded.  The indication of missing data on the 
display verifies that data with errors are discarded. 
3. Insert the standard graphical test data set. 4. Verify the legible, intact display, indicating a proper FIS-B frame information 
field with complete APDU.  Otherwise, no product display will be shown. 
5. Verify the graphical test data are displayed, indicating proper formatting and 
identification of the Network Identifier within the ADPU header, as being of type 
FIS-B Application.  Otherwise, no product display will be shown. 
6. Verify the five (as applicable for this display) key elements are displayed to show 
the proper use of the Application Service Element functions of the FIS-B system.  
Otherwise, no product display will be shown. 
7. Verify the five (as applicable for this display) key elements are displayed to 
indicate the proper processing of APDUs.  Otherwise, no product display will be shown. 
8. Verify the five (as applicable for this display) key elements are displayed to 
validate proper segmentation, division and reassembly of APDUs.  Otherwise, no product display will be shown. 
9. Insert the standard textual test data set and view the text reports. 10. Verify the five (as applicable for this display) key elements are displayed to 
signify the proper processing of the APDU Payload.  Otherwise, no product display will be shown. 

## 4.4 Fis-B Display Conformance

The cockpit display of FIS products shall meet the applicable functional requirements as described in Sections 2 and 3 and Appendix D of this document, and summarized below. 

The items tabulated below are associated with requirements contained in this document. Recommendations contained in this document may require additional verification beyond the scope of this section.  There is not one to one mapping of an item to a single requirement.  Each of the items may contain one or more individual requirements. 

| Pass / Fail Criteria    | Data Set             |
|-------------------------|----------------------|
| Test                    |                      |
| Paragraph               |                      |
| Description             |                      |
| Requirement             |                      |
| Reference               |                      |
| Verification            |                      |
| Method                  |                      |
| A = Analysis            |                      |
| I = Inspection          |                      |
| D = Demo                |                      |
| T = Test                |                      |
|                         |                      |
| Graphical test          |                      |
| pattern                 |                      |
| 2.2.2                   |                      |
| Verify max weather      |                      |
| severity is not         |                      |
| lost/understated        |                      |
| 4.4.2.1                 |                      |
| 2                       |                      |
| .                       |                      |
|                         |                      |
| Weather                 |                      |
| severity not to         |                      |
| be understated          |                      |
| Graphical test          |                      |
| pattern                 |                      |
| 4.4.2.1                 |                      |
| 3                       |                      |
| .                       |                      |
|                         |                      |
| Indication of           |                      |
| Loss of Data            |                      |
| Link                    |                      |
| 2.2.5                   |                      |
| Display indicates data  |                      |
| link lost 15 minutes    |                      |
| after disabling the     |                      |
| data stream             |                      |
| Only applicable         |                      |
| to overlays or          |                      |
| sequential data         |                      |
| 4.4.2.1                 |                      |
| 4                       |                      |
| .                       |                      |
|                         |                      |
| Age of data             |                      |
| overlays and            |                      |
| sequential data         |                      |
| sets                    |                      |
| 3.8.1.2                 |                      |
| Displays with           |                      |
| overlays or sequential  |                      |
| data sets show          |                      |
| indication of age of    |                      |
| each data set           |                      |
| 3.8.1.2                 |                      |
|                         | D                    |
| Issue date/time         |                      |
| shown on displays of    |                      |
| individual forecasts    |                      |
| Only applicable         |                      |
| to forecast test        |                      |
| reports                 |                      |
| 4.4.2.1                 |                      |
| 5                       |                      |
| .                       |                      |
|                         |                      |
| Age of data -           |                      |
| Forecasts               |                      |
| generation/issu         |                      |
| e date/time(s)          |                      |
| Only applicable         |                      |
| to forecast test        |                      |
| reports                 |                      |
| 4.4.2.1                 |                      |
| 6                       |                      |
| .                       |                      |
|                         |                      |
| Age of Data             |                      |
| Forecasts               |                      |
| Valid Time or           |                      |
| Time Interval           |                      |
| 2.2.8                   | ,                    |
| 3.8.1.2                 |                      |
|                         |                      |
| D                       | Valid time and time  |
| interval are shown      |                      |
| for forecast            |                      |
| products with a         |                      |
| valid time and time     |                      |
| interval                |                      |
| Graphical test          |                      |
| pattern                 |                      |
| 4.4.2.1                 |                      |
| 7                       |                      |
| .                       |                      |
|                         |                      |
| Age of data             |                      |
| Composite or            |                      |
| Mosaic                  |                      |
| Products Cut-           |                      |
| off time                |                      |
| 2.2.7                   |                      |
| ,                       |                      |
| 3.8.1.2                 |                      |
|                         |                      |
| D                       | Cut-off date/time is |
| indicated on all        |                      |
| displays of             |                      |
| composite/mosaic        |                      |
| products                |                      |
| Graphical test          |                      |
| pattern                 |                      |
| 4.4.2.1                 |                      |
| 8                       |                      |
| .                       |                      |
|                         |                      |
| Legend /                |                      |
| Decoding Key            |                      |
| 3.8.1.3                 |                      |
| coding and              |                      |
| symbology               |                      |
| available to the        |                      |
| pilot on a legend.      |                      |
| Graphical test          |                      |
| pattern                 |                      |
| 4.4.2.1                 |                      |
| 9                       |                      |
| .                       |                      |
| Geographic              |                      |
| area                    |                      |
| 2.2.10                  |                      |
|                         | D                    |
| All displays contain    |                      |
| earth                   |                      |
| location/navigation     |                      |
| information             |                      |
| Pass / Fail Criteria    | Data Set     |
|-------------------------|--------------|
| Test                    |              |
| Paragraph               |              |
| Description             |              |
| Requirement             |              |
| Reference               |              |
| Verification            |              |
| Method                  |              |
| A = Analysis            |              |
| I = Inspection          |              |
| D = Demo                |              |
| T = Test                |              |
|                         |              |
| 4.4.2.1                 |              |
| 10                      |              |
| .                       |              |
|                         |              |
| Geographic              |              |
| area and                |              |
| altitude                |              |
| coverage                |              |
| Graphical test          |              |
| pattern  not            |              |
| applicable to           |              |
| vertical height         |              |
| test                    |              |
| 2.2.10                  |              |
|                         |              |
| 3.8.1.5                 |              |
|                         |              |
| D                       |              |
| Graphical displays      |              |
| clearly indicate        |              |
| geographic area         |              |
| covered and, when       |              |
| applicable, the         |              |
| vertical height(s) for  |              |
| the product             |              |
| Graphical test          |              |
| pattern                 |              |
| 4.4.2.1                 |              |
| 11                      |              |
| .                       |              |
|                         |              |
| Readability of          |              |
| key elements            |              |
| 3.8.1                   |              |
| Key elements are not    |              |
| obscured by other FIS   |              |
| information             |              |
| Graphical test          |              |
| pattern                 |              |
| 4.4.2.1                 |              |
| 12                      |              |
| .                       |              |
|                         |              |
| Type of Product         |              |
| 2.2.6                   | ,            |
| 3.8.1.1                 |              |
|                         |              |
| D                       |              |
| Each display page       |              |
| shows the type of the   |              |
| product being           |              |
| displayed               |              |
| Graphical test          |              |
| pattern                 |              |
| 4.4.2.1                 |              |
| 14                      |              |
| .                       |              |
|                         |              |
| Indication of           |              |
| corrupted,              |              |
| missing data            |              |
| 2.2.4                   | ,            |
| 3.8.1.4                 |              |
|                         |              |
| D                       |              |
| Unique format used      |              |
| to positively locate    |              |
| and indicate            |              |
| corrupted/missing       |              |
| data or missing radar   |              |
| site                    |              |
| Graphical test          |              |
| pattern                 |              |
| 4.4.2.1                 |              |
| 16                      |              |
| .                       |              |
|                         |              |
| Indication of           |              |
| corrupted,              |              |
| missing data            |              |
| 2.2.4                   | ,            |
| 3.8.1.4                 |              |
|                         |              |
| D                       |              |
| Unique format used      |              |
| to positively locate    |              |
| and indicate            |              |
| corrupted/missing       |              |
| data                    |              |
| Textual test            |              |
| reports                 |              |
| 4.4.2.1                 |              |
| 18                      |              |
| .                       |              |
| Age of                  |              |
| weather data;           |              |
| Observations            |              |
| 2.2.7                   |              |
| ,                       |              |
| 3.8.1.2.1               |              |
|                         |              |
| D                       |              |
| Date/time is shown      |              |
| for each                |              |
| METAR/SPECI             |              |
| observation shown on    |              |
| display                 |              |
| Textual test            |              |
| reports                 |              |
| 4.4.2.1                 |              |
| 19                      |              |
| .                       |              |
| Report display          |              |
| format                  |              |
| 3.8.1.6                 |              |
| ,                       |              |
| 3.8.1.7                 |              |
|                         |              |
| D                       |              |
| Text displayed in       |              |
| ICAO or equivalent      |              |
| format                  |              |
| 3.8.1.6                 |              |
| ,                       |              |
| 3.8.1.7                 |              |
|                         |              |
| D                       |              |
| Text is accurately      |              |
| decoded                 |              |
| Textual test            |              |
| reports                 |              |
| 4.4.2.1                 |              |
| 20                      |              |
| .                       |              |
| ASCII or                |              |
| DLAC                    |              |
| character set           |              |
| Combined                |              |
| Graphical and           |              |
| Textual reports         |              |
| 3.8.1.10                |              |
|                         | D            |
| Text component of       |              |
| report is accurately    |              |
| displayed               |              |
| 4.4.2.1                 |              |
| 22                      |              |
| .                       |              |
| Combined                |              |
| Graphical and           |              |
| Textual                 |              |
| Display                 |              |

## 4.4.1 Conditions Of Test Procedures/Test Objectives

The objectives of these tests are to verify that the display of FIS products meets the minimum standards of this document.  These tests are to be conducted in a controlled, ground environment and only processing functions will be tested.  Standardized FIS-B 
test stimuli will be used to simulate live data except where live data are required to verify the function. 

## 4.4.2 Detailed Test Procedures

These procedures are developed to test individual performance requirements and, in many instances, are grouped with similar procedures to facilitate the verification process. 

## 4.4.2.1 Faithful Display Of Data Test Procedures

These procedures will verify that the weather severity is not understated (depictions of most severe weather not lost when resolution is decreased) and the age of data, legend/decoding key and indication of missing data are properly displayed. 

1. Insert the graphical test data set and view the graphical pattern on the airborne 
display. 
2. Beginning with the display set on minimum scale/highest resolution (if such a 
selection exists), observe regions with most severe weather characteristics.  Next, 
zoom to or select the maximum scale/lowest resolution and verify that the most 
severe weather on the test display is not degraded or understated due to changes in scale.  This test is not applicable if scale is not adjustable on the display. 
3. Verify that 15 minutes after disabling the signal input to the physical media 
receiver, the lack of data is detected and an indication is provided on the display unit that the data link has been lost. 
4. For those products with data overlays or sequential data sets, verify the display 
shows an indication of age of each data set. 
5. Verify that issue date/time(s) are indicated on all displays of individual forecast 
products. 
6. Verify that valid time or time interval is indicated on all displays of individual 
forecast products. 
7. Verify that a cut-off date/time is indicated on all displays of composite/mosaic 
products. 
8. Verify that the meaning of color-coding and symbology is available to the pilot 
on a legend, accessible via no more than a single operator action. 
9. Verify that each display contains service volume coverage represented by the 
data. 
10. Verify that, for graphical displays, the geographical area covered is clearly 
indicated and, when part of the specified product, the vertical heights for the product are indicated (e.g., 3000 ft, 3000-5000 ft, ABV 12,000 ft). 
11. Verify that no FIS information (besides/beyond the five key elements) that is 
presented interferes with or obscures the readability of those key elements. 
12. Verify that the type of product is clearly indicated on each display. 
13. Insert the standard graphical test data set.  A missing radar site has been 
simulated. 
14. Verify that any data known to be missing or radar sites not reporting are 
indicated on the display. 
15. Insert the standard graphical test data set.  Bits have been altered (after FIS-B 
frame checksum computation) to create an error and corrupt the data. 
16. Verify corrupted/missing data are identified and located on the display. 
17. Insert the standard Textual test data set and view the text products. 
18. Verify that the date/time for each textual report is indicated on the display 
showing the age of the data. 
19. Verify that textual reports in the appropriate ICAO format or equivalent, alternate 
format are displayed accurately. 
20. Verify that the character set used, it is decoded correctly. 
21. Insert the standard test data set of combined graphical and textual reports. 
22. Verify that the textual component of the report can be accessed and accurately 
displayed. 
MEMBERSHIP 
Chairman Mr. Steve Henely Rockwell Collins 
 
Designated Federal Official Mr. Rick Heuwinkel Federal Aviation Administration 
 
Secretary Mr. Roy Strasser AvMet Applications International, LLC Members Ms. Kathy Abbott Federal Aviation Administration Mr. Moin Abulhosn Federal Aviation Administration Mr. Robert Anoll Federal Aviation Administration Mr. Larry Bachman The John Hopkins University Mr. Kirk Baker Federal Aviation Administration Mr. Steve Boyer Technology Service Corporation Mr. Andrew Broom General Aviation Manufacturers Association Mr. Jennifer Burt National Aeronautics & Space Administration Mr. Michael Castle John Hopkins University Mr. Jim Chamberlain National Aeronautics & Space Administration Mr. Ernie R. Dash Raytheon Systems Company Mr. Archie Dillard Federal Aviation Administration Ms. Colleen Donovan Federal Aviation Administration Ms Fonda Dowl Federal Aviation Administration Mr. Art Ercolani Honeywell International, Inc. 

Ms. Thea Feyereisen Honeywell International, Inc. 

Mr. Paul Fiduccia Small Aircraft Manufacturers Association Mr. Bill Flathers Aircraft Owners and Pilots Association Ms. JoAnn Ford Federal Aviation Administration Mr. Gregory Frye Federal Aviation Administration Mr. David Goehler Jeppesen Mr. John Gordon Federal Aviation Administration Mr. Robert Grappel MIT Lincoln Laboratory Mr. Loran Haworth Federal Aviation Administration Mr. Damon Hill WSI Corporation Mr. Keith Hoffler WSI Corporation Mr. Al Homans ARINC Incorporated Mr. Thomas Hutchins Federal Aviation Administration Mr. Mike Ingram Avidyne Corporation Mr. Richard Jinkins Rockwell Collins, Inc Mr. Fred Johnson Federal Aviation Administration Mr. Clyde Jones Federal Aviation Administration Mr. Jon Johnson National Aeronautics & Space Administration Ms. Kathleen Kearns SITA 
Mr. Randy Kenagy Aircraft Owners and Pilots Association Mr. Todd Kilbourne Trios Associates, Inc. 

Mr. Richard King Honeywell International, Inc. 

Mr. Chuck LaBerge Honeywell International, Inc. 

Ms. Brooke Lang Trios Associates, Inc. 

Ms. Mary Lapis Rockwell Collins, Inc. 

Mr. Terrence Leier Rockwell Collins, Inc. 

Mr. Tenny Lindholm National Center for Atmospheric Research Mr. Gary Livack Federal Aviation Administration Mr. David Lotterer Regional Airline Association Mr. Delbert Mann Federal Aviation Administration Mr. Donald Marsh Honeywell International, Inc. 

Mr. Simon Matthews Avidyne Corporation Mr. Kevin Mattison Federal Aviation Administration Ms. Kerryaine Mazziotti Federal Aviation Administration Dr. Raymon McAdaragh Federal Aviation Administration Mr. George McClain United States Air Force Mr. Thomas McFall American Airlines Ms. Starr McGettigan Federal Aviation Administration Mr. James McKie Air Transport Association of America Ms. Priscilla Merritt-Stephenson Federal Aviation Administration Mr. Chris Moody MITRE Corporation/CAASD 
Mr. Alfred Moosakhanian Federal Aviation Administration Mr. Tom Mosher Garmin AT, Inc Mr. Thomas Mulkerin Mulkerin Associates Inc. 

Mr. Peter Muraca Federal Aviation Administration Mr. Robert Myers The Boeing Company Mr. Kevin O'Toole United States Air Force Mr. Richard Olson Federal Aviation Administration Mr. Dave Pace Federal Aviation Administration Mr. William Petruzel Federal Aviation Administration Mr. Mark Phaneuf AvMet Applications International, LLC 
Mr. William Phaneuf Air Line Pilots Association Mr. Dino Piccione Federal Aviation Administration Ms. Jennifer Rezeppa Technology Service Corporation Mr. Alan Robinson United States Air Force Mr. David Robinson Federal Aviation Administration Mr. Rudolph Ruana RTCA, Inc. 

Mr. William Russell Russell Systems Ms. Sandra Schmidt Federal Aviation Administration Mr. Russ Sinclair Harris Corporation Mr. Peter Skaves Federal Aviation Administration Mr. Daniel Stapleton MITRE Corporation/CAASD 
Mr. Robert Strain MITRE Corporation/CAASD 
Mr. Paul Stringer Trios Associates, Inc. 

Mr. Terry Stubblefield Federal Aviation Administration Mr. Ralph Thompson International Air Transport Association Mr. Brian Toohey AirCell, Inc. 

Mr. Matthew Tucker National Air Traffic Controllers Association Mr. Stephen Van Trees Federal Aviation Administration Ms. Trish Ververs Honeywell International, Inc. 

Mr. Matthew Wade Federal Aviation Administration Mr. Robert Witulski ARINC Incorporated 
 

## Appendix A Acronyms And Abbreviations

This page intentionally left blank. 

## Appendix A Acronyms And Abbreviations

AC 
FAA Advisory Circular 
ACARS 
Aircraft Communications, Addressing and Reporting System.  Air-ground alphanumeric data link. 
AIRMET 
Airmen's Meteorological Information.  In-flight weather advisory issued only to amend the area forecast.  Concerns weather of less severity than SIGMETs. 
AOA 
ACARS Over AVLC 
APDU 
Application Protocol Data Unit 
ASE 
Application Service Element 
ASN.1 
Abstract Syntax Notation, version one 
ATC 
Air Traffic Control 
ATIS 
Airport Terminal Information Service 
AVLC 
Aviation VHF Link Control 
AWW 
Severe Weather Forecast Alert 
BMS 
Bit Map Section 
CDM 
Collaborative Decision Making 
CONUS 
Continental United States 
CRLF 
Carriage Return Line Feed 
CSC 
Common Signaling Channel 
CSMA 
Carrier Sense Multiple Access 
D-ATIS 
Digital Airport Terminal Information Service 
DLS 
Data Link Services 
FCS 
Frame Check Sequence 
FIS 
Flight Information Services 
FIS-B 
Flight Information Services - Broadcast 
FISDL 
Flight Information Service Data Link 
GDS 
Grid Description Section 
GIF 
Graphics Interchange Format 
GPS 
Global Positioning System 
GRIB 
GRIdded Binary 
GSIF 
Ground Station Identification Frame 
GWS 
Graphical Weather Service 
HDLC 
High-level Data Link Control  
HFDL 
High Frequency Data Link 
ICAO 
International Civil Aviation Organization 
IEC 
International Electrotechnical Commission 
IFR 
Instrument Flight Rules 
IPI 
Initial Protocol Identifier 
ISO 
International Standards Organization 
JPEG 
Joint Photographic Experts Group 
LIFR 
Low Instrument Flight Rules 
LME 
Link Management Entity 
MASPS 
Minimum Aviation System Performance Standards 
METAR 
Aviation Routine Weather Report.  An international weather-reporting format. 
MFD 
Multi-Function Display 
MNG 
Multiple-image Network Graphics  
MOPS 
Minimum Operational Performance Standards 
MVFR 
Marginal Visual Flight Rules 
NCEP 
National Centers for Environmental Prediction 
NEXRAD  
Next Generation Weather Radar 
NLDN 
National Lightning Detection Network 
NOAA   
National Oceanic and Atmospheric Administration 
NOTAM  
Notice to Airmen 
NSME 
Network System Management Entity 
NWS 
National Weather Service 
OSI 
Open Systems Interconnection 
PDS 
Product Definition Section 
PER 
Packed Encoding Rules (ASN.1) 
PIREPs 
Pilot Weather Reports 
PNG 
Portable Network Graphics format 
RF 
Radio Frequency 
RFC 
Request For Comment 
RUC 
Rapid Update Cycle 
RVR  
Runway Visual Range.  Visibility values measured by transmissometers mounted on towers along the runway. 
SARPs  
Standards and Recommended Practices (ICAO). 
SATCOM  
Satellite Communications 
SATCOM DL 
SATCOM data link 
SIGMET 
Significant Meteorological Advisory.  Weather advisory issued concerning weather significant to the safety of all aircraft such as severe and extreme turbulence or severe 
icing. 
SNAcP 
SubNetwork Access Protocol 
SPECI  
Special Surface Observation 
SPI 
Subsequent Protocol Identifier 
SUA  
Special Use Airspace, including restricted and prohibited airspace and military 
operations areas (MOAs) 
TAF  
Terminal Aerodrome Forecasts  
TIFF 
Tagged Image File Format 
UAT 
Universal Access Transceiver 
UI 
Unnumbered Information 
UTC 
Coordinated Universal Time 
VDL 
VHF Digital Link 
VDLM2 
VHF Digital Link Mode 2 
VDR 
VHF Digital Radio 
VFR 
Visual Flight Rules 
VHF 
Very High Frequency (30-300 MHz) 
VIP 
Video Integrated Processor 
VME 
VDL Management Entity 
W3C 
World Wide Web Consortium 
WH 
Weather-Huffman 
WMO 
World Meteorological Organization 
WSR  
Weather Surveillance Radar 
 

## Appendix B Glossary Of Terms

This page intentionally left blank. 

## Appendix B Glossary Of Terms

This appendix provides definitions of terms that are used in defining and testing data link systems.  Some terms in this glossary are unique to flight information systems or system features not addressed by this document and included for compatibility with related documents. 

 
Aeronautical Telecommunication Network (ATN): An inter-network architecture that allows ground, air-ground and avionic subnetworks to inter-operate by adopting common interface services and protocols based on the ISO Open Systems Interconnection (OSI) reference model. 

Aircraft Address: A unique combination of 24 bits available for assignment to an aircraft for the purpose of air-ground communications, navigation, and surveillance. 

APDU Payload (also Payload): The Payload contains all or segmented portions of an FIS-B Product File. 

 
Bit Error Rate: The number of bit errors in a sample divided by the total number of bits in the sample, generally averaged over many samples. 

Broadcast: A non-directed transmission intended to be received by all stations. 

 
DBZ: Ten (10) times the log base ten (10) of the effective radar reflectivity. 

 
Decision Support Function: At the highest level, a decision support function applies intelligence or logic to transform data into information for the pilot (or, in general, end user) to facilitate fast and accurate decision making.  A simple decision support function might be an annunciator that is intended to direct pilot attention to a particular situation.  A more complex decision support function might include prioritization of multi-function displays, annunciation, and/or steering guidance to avoid a hazard such as traffic or terrain. 

Field: A field is an element of a Record or Report in which one piece of information is stored.  A field is the smallest, most basic data element transmitted. 

FIS: Non-control, advisory information needed by pilots to operate safely and efficiently in the National Airspace System and in international airspace.  FIS includes such information (or products) as weather graphics and text, Special Use Airspace (SUA) information, and Notices to Airmen (NOTAMs). 

FIS-B (also FIS-B system): Means of disseminating FIS via a broadcast (a non-directed transmission intended to be received by all stations) as described in Steps 1-5 of the FIS-B Data Link System (Section 
1.2, Figure 1-1). 

 
FIS Product (also FIS-B Product):  FIS information generated and displayed for cockpit applications as described in Steps 2 and 5 of the FIS-B Data Link System (Section 1.2, Figure 1-1). 

 
FIS-B Product File (also Product File):  The basis for the FIS product intended for cockpit presentation.  
The Product File is formatted as described in the FIS-B Product Registry (see Appendix E) and generated during Step 3 of the FIS-B Data Link System (Section 1.2, Figure 1-1). 

 
FIS-B Product Registry: A publicly accessible source for listing the Product Identifiers (see Section D.2.1) contained in an APDU Header along with the description of the APDU Payload encoding for the associated FIS-B Product Files (see Appendix E).  Also provides a listing of the FIS-B data link networks that are using the APDU format, and the application procedures for requesting additions or updates to the FIS-B Product Registry. 

 
 
Frame: The link layer frame is composed of a sequence of address, control, frame check sequence, and information fields, bracketed by opening and closing flag sequences.  A valid frame is at least eight octets in length and contains an address field (8 octets), a link control field (1 octet) and a frame check sequence for error detection (2 octets).  A frame may or may not include a variable length information field. 

 
Link Layer: The layer that lies immediately above the physical layer in the OSI protocol model.  The link layer provides for the reliable transfer of information across the physical media.  It is subdivided into the media access and control sublayer. 

Media Access Control (MAC): The sublayer that acquires the data path. 

 
Multicast: A directed transmission intended to be received by a specific set of stations. 

 
Nibble: Four (4) bit data value. 

 
Physical Layer: The lowest layer in the OSI protocol model.  The physical layer is concerned with the transmission of binary information over the physical medium. 

 
Point-to-Point: Pertaining or relating to the interconnection of two devices, particularly end-user instruments.  A communication path of service intended to connect two discrete end-users. 

Radome: Radar dome. 

 
Record: A record is part of a collection of related items in a report or an alternate means of conveying a report or portions thereof. 

Report: A report is an instance of a single FIS product.  An APDU may contain one or more reports of a particular FIS product. 

 
RFC: Stands for Request for Comment.  Approved RFCs are documented technical consensus available at the Internet Engineering Task Force (IETF) web site.  Web site link: http://www.ietf.org/.  RFCs are not technical standards. 

Unicast: A directed transmission to a single station. 

 
VDL Station: A VDL-capable entity.  A VDL station may be either an aircraft or a ground station.  A 
VDL station is a physical entity that transmits and receives frames over the air-ground interface and comprises, at a minimum: a physical layer, MAC sublayer, and a unique link layer address. 

Winds Aloft: Wind speed at a designated altitude, in knots. 

 
Wind Speed: The speed at which the wind is blowing, measured in knots. 

 
World Wide Web Consortium: An International organization whose goals are the furthering of consensus on world wide web technical recommendations. 

## Appendix C List Of References

This page intentionally left blank. 

## Appendix C List Of References

The following standards and practices are referenced herewith and are useful as guidance in the design and certification of FIS. 

1. AC 23.1309.1C: Equipment, Systems, and Installation in Part 23 Airplane  (latest revision). 

2. AC 23.1311-1A: Installation of Electronic Displays in Part 23 Airplanes, March 1999. 3. AC 25.11 "Transport Category Airplane Electronic Display Systems, AMS "Guidelines for Using 
Color to Depict Meteorological Information: IIPS Subcommittee for Color Guidelines"." 
4. AC 25.1309-1A: "System Design and Analysis." 5. AC 00-45E: "Aviation Weather Services." 6. AC 120-76A: Guidelines for the Certification, Airworthiness, and Operational Approval of Electronic 
Flight Bag Computing Devices 
7. ICAO Annex 3, Meteorological Service for International Air Navigation, 14th edition, July 2001. 
8. ICAO Annex 10, Volume III, Part 1 Digital Data Communications Systems, section 8.6.2.4 Character 
Structure on Data Links, Table 8-2 International Alphabet No. 5 (IA-5) (international reference 
version). 
9. Broadcast Address Encoding of the VDL Mode 2 SARPs. 10. "Department of Defense Joint Technical Architecture," Version 3.0, dated November 15, 1999. 
11. DOT project report ATC-261. 
12. GeoTIFF Format Specification Rev 1.0. 
13. "Human Factors Considerations in the Design and Evaluations of Electronic Flight Bags (EFBs)", 
Version 1: Basic Functions, Chandra and Mangold, USDOT/Volpe, September 2000. 
14. ICAO, Amendment 72 to the International Standards and Recommended Practices, Aeronautical 
Telecommunications, Annex 10 to the Convention on International Civil Aviation, Volume III Part I 
Digital Data Communications Systems, November 6, 1997. 
15. ICAO Annex 15, "Aeronautical Information Services, 10th edition, July 1997. 
16. International Organization for Standardization/International Electrotechnical Commission, ISO/IEC 
3309, 
Information 
technology⎯Telecommunication 
and 
information 
exchange 
between 
systems⎯High-level data link control (HDLC) procedures⎯Frame structure, 1991. 
17. International Organization for Standardization, ISO 4335, Information processing systems⎯Data 
communication⎯High-level data link control elements of procedures, 1987. 
18. International Organization for Standards [ISO/IEC 8824-1: 1995 Information Technology - Abstract 
Syntax Notation One (ASN.1): Specification of Basic Notation.] [ISO/IEC 8825-2: 1996 Information 
Technology - ASN.1 encoding rules - Part 2: Specification of Packed Encoding Rules (PER).]. 
19. ISO/IEC TR 9577 Technical Report - Information Technology - Protocol Identification in the 
Network Layer. 
20. ISO Open Systems Interconnection (OSI) reference model. 
21. Minimum Operational Performance Standards for ATC Two-Way Data Link Communications, 
RTCA/DO-219, August 27, 1993 by RTCA Special Committee 169. 
22. MNG (Multiple-image Network Graphics) Format, Version 1.0; January 31, 2001. 
23. "PNG (Portable Network Graphics) Specification," Version 1.0, W3C Recommendation; October 
01,1996. 
24. RFC 1950: "ZLIB Compressed Data Format Specification version 3.3", Deutsch, P. and J-L. Gailly; 
May 22, 1996. 
25. RFC 1951: "DEFLATE Compressed Data Format Specification version 1.3", Deutsch, P.: May 1996. 
26. RFC 2083: "PNG (Portable Network Graphics) Specification version 1.0"; March 1997. 
27. RTCA 216-96:  Human Engineering Recommendations for Data Link Systems. 
28. RTCA DO-224A, Signal-in-Space Minimum Aviation System Performance Standards (MASPS) for 
Advanced VHF Digital Data Communications Including Compatibility with Digital Voice Techniques, September 13, 2000. 
29. RTCA/SAE Aerospace Recommended Practice ARP4791: Human Engineering Guidance for Data 
Link Systems. 
30. SAE Aerospace Minimum Performance Standard AS8034: Minimum Performance Standard for 
Airborne Multipurpose Displays. 
31. SAE Aerospace Recommended Practice ARP4032: Human Engineering Considerations in the 
Application of Color to Electronic Aircraft Displays. 
32. SAE Aerospace Recommended Practice ARP5364: Human Factors Considerations for the Design of 
Multifunction Displays for Civil Aircraft; March 27, 2003. 
33. SAE Aerospace Recommended Practice ARP5898: Human Interface Criteria for Flight Deck Surface 
Operations Displays; December 19, 2002. 
34. Software Considerations & Airborne Systems & Equipment Certification, RTCA/DO-178B, 
December 1, 1992 by RTCA Special Committee 167. 
35. Tanenbaum, Andrew S., *Computer Networks*, Prentice Hall, 1988. 
36. TSO C113: Airborne Multipurpose Electronic Displays. 
37. US Geological Survey Professional Paper 1395: *Map projections - A working manual*, by John P. 
Snyder. 
38. World Meteorological Organization, 1988: *Manual on Codes, Volume 1*.  (WMO Publ. No. 306), 
WMO, Geneva, Switzerland. 

## Appendix D Apdu Format (Normative)

This page intentionally left blank. 

## Appendix D Apdu Format (Normative)

This appendix describes the Application Protocol Data Unit (APDU).  The APDU Header fields contain all of the information necessary for the receiving end of the network to process, store, and display a FIS-B Product File.  The application service may choose to discard a Product File based on information contained in the APDU Header fields (and, possibly, on the Address Fields of the Frame containing the APDU).  Product Files that are too large for transmission in a single APDU may be segmented into multiple APDUs.  In this event, the Segmentation Flag is set to indicate use of the Segmentation Data field, and Product File segments (or APDU Payloads) are individually numbered and sequenced. 

 
The APDU structure shall begin with an APDU Header consisting of data fields as shown in Table D-1.  
FIS-B Product Identifier, Product Descriptor, Segmentation Flag, APDU Header Time, and an optional Segmentation Data Block.  Figure D-9 provides a graphic outline of all the header fields. The APDU Header shall be encoded and decoded in ASN.1 or an equivalent means that provides bit-wise formatting identical to ASN.1.  ASN.1 encoding and decoding shall be in accordance with the International Organization for Standards ISO/IEC 8824-1: 1995 Information Technology - Abstract Syntax Notation One (ASN.1): Specification of Basic Notation.  FIS products encoded with ASN.1 shall be done so in accordance with ISO/IEC 8825-2: 1996 Information Technology - ASN.1 encoding rules - Part 2: Specification of Packed Encoding Rules (PER).  The "non-aligned, non-canonical" form of PER 
shall be used as referenced in Appendix C.  Table D-14 contains an Abstract Syntax Notation version one 
(ASN.1) representation of the APDU Header. 

APDU 

| APDU Header (Appendix               | D                                  | )       | APDU Payload (Appendix    | E                                |
|-------------------------------------|------------------------------------|---------|---------------------------|----------------------------------|
|                                     |                                    |         |                           |                                  |
| Table D-1  FIS-B APDU Header Format |                                    |         |                           |                                  |
| Field                               | Number of bits                     |         |                           |                                  |
| Document                            |                                    |         |                           |                                  |
| Section                             |                                    |         |                           |                                  |
| Identifier                          | 16 bits (two bytes, 0xFF and 0xFE) | Section | D.1                       |                                  |
| 14 - 42 bits                        | Section                            | D.2     |                           | Product Descriptor fields (Note: |
| Field size will vary based on the   |                                    |         |                           |                                  |
| options included.)                  |                                    |         |                           |                                  |
| Segmentation Flag                   | 1 bit                              | Section | D.3                       |                                  |
| Header Time                         | 22 - 37 bits                       | Section | D.4                       |                                  |
| Time Option Bits                    | 2 bits                             |         |                           |                                  |
| Date (optional)                     | 9 bits (if included)               |         |                           |                                  |
| Month of year                       | 4 bits                             |         |                           |                                  |
| Day of Month                        | 5 bits                             |         |                           |                                  |
| UTC Time Hours                      | 5 bits                             |         |                           |                                  |
| Time Minutes                        | 6 bits                             |         |                           |                                  |
| Time Seconds (optional)             | 6 bits (if included)               |         |                           |                                  |
| Segmentation                        | Data                               | Block   |                           |                                  |
| (optional)                          |                                    |         |                           |                                  |
| 24 bits total (if included)         | Section                            | D.5     |                           |                                  |
| Product File Length                 | 12 bits                            |         |                           |                                  |
| Number                              | 12 bits                            |         |                           |                                  |
| Zero Padding Bits                   | 0-7 bits to force octet-alignment  | Section | D.6                       |                                  |

## D.1 Subnetwork Access Protocol Identification

The Subnetwork Access Protocol (SNAcP) field is composed of two bytes used to uniquely identify FIS products in accordance with the recommendations of ISO/IEC TR 9577.  These bytes facilitate subnetwork access protocol (SNAcP) identification in the event of multiple concurrent subnetwork use (i.e., FIS-B along with HFDL, SATCOM 
 
DL, VDL, or ACARS).  The bit definition shall be 0xFF (termed the Initial Protocol Identifier, or IPI) and 0xFE (termed the Subsequent Protocol Identifier, or SPI) respectively, or 11111111 11111110.  

Note:  The IPI byte encoding of all-ones (0xFF) is reserved by ISO/IEC TR 9577 to 
allow for the specification of additional subnetwork protocols beyond those 
explicitly defined in the ISO document.  When this form of IPI encoding is employed, a second byte (the SPI) is used to specify the actual subnetwork protocol in use.  The "ACARS Over AVLC" (AOA) subnetwork protocol (used to provide backwards compatibility for ACARS applications to operate over VDL) 
currently specifies the SPI encoding of 0xFF.  FIS-B has selected the SPI encoding of 0xFE (11111110) to avoid conflict with AOA and to require a 
minimum of regulatory co-ordination. 

## D.2 Product Descriptor Fields

The Product Descriptor identifies the broadcast application (i.e., the particular FIS-B Product File), the optional Applications Methods (compression and geographic reference), the optional Geographic Locator, and contains the Provider-Specific Flag Bit associated with the Product File, as shown in Table D-2. 

The Application Methods Flag Bit shall be set to 1 if the optional Applications Methods fields are to be included.  The Applications Methods Flag Bit shall be cleared to 0 if the Applications Methods fields are to be omitted.  (Since the Applications Methods to be used can be uniquely identified by the Product Identifier itself for a significant number of FIS products, these FIS products may save 8 bits of APDU Header overhead by omitting the Application Methods fields entirely as opposed to using the "none" codings for Compression and Geographic Reference). The Geographic Locator Flag Bit identifies whether the optional Geographic Locator is included - see Section D.2.4 for details. 

The Provider-Specific Flag Bit in the FIS-B Product Descriptor (see Table D-2) is reserved as a special indicator flag that may be utilized for a provider-specific function. Some example applications of the Provider-Specific Flag Bit include: 

a. Indicating that the APDU payload is encrypted 
b. Marking the APDU as a system test-report 
If the Provider-Specific Flag Bit is set to one in the APDU, the FIS-B avionics will determine the proper processing for the APDU based on the provider of the particular APDU.  The determination of the APDU provider might be performed by examination of the Address Field of the APDU (see Section 3.4.4 and Appendix F), or by an alternative means.  The Provider-Specific Flag Bit should be cleared to zero unless some providerspecific usage is intended.  

|                                        |                      | Field    | Number of bits    | Document Section    |
|----------------------------------------|----------------------|----------|-------------------|---------------------|
| Application Methods Flag Bit           | 1 bit                | Section  | D.2               |                     |
| Geographic Locator Flag Bit            | 1 bit                | Section  | D.2.4             |                     |
| Provider-Specific Flag Bit             | 1 bit                | Section  | D.2               |                     |
| Product Identifier                     | 11 bits              | Section  | D.2.1             |                     |
| Application Methods (optional)         | 8 bits (if present)  | Section  | D.2               |                     |
| Compression Method                     | 4 bits               | Section  | D.2.2             |                     |
| Geographic Reference Method            | 4 bits               | Section  | D.2.3             |                     |
| Geographic Locator (region) (optional) | 20 bits (if present) | Section  | D.2.4             |                     |

 
                          Note: 
                                       The criteria for determining whether an application parameter is contained in 
                                       the Product Descriptor field or the Payload field relates to the operation 
                                       performed on the bits contained in the Payload.  If the operation is required to 
                                       convert the Payload to bits of information, then the application qualifier needs to 
                                       be described in the Product Descriptor.  If the parameter is not needed for such a 
                                       conversion, then it can be contained in the Payload.  For example, the 
                                       compression method needs to be known in order for the bits contained in the 
                                       Payload to be converted to a usable form. 

## D.2.1 Product Identifier

The Product Identifier describes to the avionics receiver the FIS product contained in the Payload field of the APDU.  The FIS-B Product Registry (see Appendix E) lists the Product Identifiers together with the associated FIS-B Product File that it supports.  The FIS-B Product Registry also describes the content and format of the data in each FIS-B Product File. It is desirable to standardize some product specifications, as contained herein, so avionics manufacturers do not have to develop software for multiple product specifications. Further, good system design practice dictates that FIS-B Product File specifications should allow for future growth and evolution.  It should be noted there is no requirement for each ground station to broadcast every one of the products listed in the FIS-B Product Registry and avionics manufacturers are not required to decode or accept all of the Product File specifications. In some cases, an FIS-B Product File may be based on a proprietary product.  For such products, a Product Identifier will be assigned and the FIS-B Product Registry will provide the reference source for obtaining information on the encoding/decoding details for the FIS-B Product File. 

## D.2.2 Compression Method

This field tells the receiver which compression method will be used by the APDU.  A 
number of compression methods are possible but the methods listed in Table D-3 should be used in order to reduce the number and simplify the decompression process in the aircraft avionics. 

Field Value Compression Method 
Document Section and Reference Document 
0 
None 
N/A 
1 
Run Length Encoding 1 
Section D.2.2.1 
2 
Run Length Encoding 2  
Section D.2.2.2 
3 
DEFLATE 
Section D.2.2.3 
RFC 1951 
4 
WH method of data compression of weather images Section D.2.2.4 
DOT project report ATC-261
5 
Portable Network Graphics (PNG) format  
Section D.2.2.5 
RFC 2083 
6 
Multiple-Image Network Graphic (MNG) format 
Section D.2.2.5 
7-15 
Reserved 

## D.2.2.1 Run Length Encoding Compression Method 1

The format of the run length encoding allows runs of up to 65,536 pixels of the color or data codes 0 to 255 to be encoded.  Runs are encoded with a varying number of bytes depending on the length of the run.  Data code values are encoded as 2 separate nibbles (4 
bits) with the high nibble being set in a special flag byte and the low nibble being sent with each run. Runs of 1 to 13 pixels are encoded in a single byte with the lower 4 bits being the low nibble of the data code and the higher 4 bits being the length of the run minus 1 (0x0 to 0xC). Runs of 14 to 256 pixels are encoded in 2 bytes.  The first byte contains the flag 0xE or 
14 in the high nibble, and the low nibble of the data in the lower 4 bits.  This byte is followed by one byte with the length of the run minus 1 (0x0D to 0xFF hex). Runs of 257 to 65,536 pixels are encoded in 3 bytes.  The first byte contains the flag 0xD or 13 in the high nibble, and the low nibble of the data code in the lower 4 bits.  The byte is followed by 2 bytes with the length of the run minus 1 (0x0100 to 0xFFFF hex). 

At the beginning of a line segment, the high nibble of the data is assumed to be zero.  
This value is changed with a special flag byte.  The high nibble of the flag byte contains the value 0xF or 15.  The lower 4 bits of the byte contain the high nibble of the color value.  The value of the high nibble should be carried over to the next 1 or more runs. The value is only changed when a new flag byte for the high nibble color or end of the line is encountered. With the encoding, it is possible for the flag sequence '0x00 0xF0' to appear as data.  
'0x00 0xF0' is defined as a control sequence.  To prevent a misinterpretation of the data as a flag sequence, a control byte of 0x00 is placed as the next byte after the sequence. This indicates that the proceeding 2 bytes are data, and should not be interpreted as the start of a new segment. 

Example (see Table D-4):  0xD0 0x0105 0xF1 0x01 0x12 0xE3 0x20 0x00 0xF0 0x00 
0xD0 0x0F00 

0xD0  0x0105 Run of 262 bytes of color code 0 
0xF1 
flag byte to change the high nibble of the color code to 0x1 
0x01 
Run of 1 byte of color 17 
0x12 
Run of 2 bytes of color 18 
0xE3  0x20 
Run of 33 bytes of color 19 
0x00 
Run of 1 byte of color 16 
0xF0 
flag byte to change the high nibble of the color to 0x0 
0x00 
stuff byte to indicate previous 2 bytes are data 
0xD0 0x0F00 
Run of 3841 bytes of color 0  (0x00) 

## D.2.2.2 Run Length Encoding Compression Method 2

A scheme known as "run length encoding" can be used to compress raster format images.  
Starting at the upper left corner of a raster image and going across a row, data bins having the same data value are counted until the data value changes.  The count is called a "run". The data value is called the "color".  The current run/color pair is then stored and a new run is started.  A scheme using 4 bits for the run value and 4 bits for the color value is used in WSR-88D products (e.g., Composite Reflectivity).  Hence a maximum run of 15 data bins is possible and data values in the range 0 to 15 are supported.  Each run/color pair occupies a single byte.  Also, a new run/color combination is started each time that a run value reaches 15 even if the data level (color) did not change, unless the packing descriptor is greater than 2. The packing descriptor in the NEXRAD product is normally set to 2.  Larger values result in the run length being multiplied by the packing descriptor (minus 1). 

Each row is processed individually.  Once a row is completed then the next row is processed.  The number of bytes of data in the current row is stored in the two bytes preceding the actual run/color data for the current row.  If the end of a row is reached with an odd number of run/color combinations then an additional byte (value of zero) is added so that the next row will start on an even 16-bit boundary.  Although the run length encoded format will not result in the smallest possible file size, it is still effective and it is a very efficient format for display since little processing is needed at that stage. 

Table D-5 and Table D-6 are excerpts from the WSR-88D RPG to Associated PUP 
Interface Control Document showing the raster Data Packet format that uses Run Length Encoding.  Each line in this excerpt represents a 16-bit word.  The National Mosaic products produced by Unisys are formatted using the same scheme. 

| MSB                         |                |         |                |
|-----------------------------|----------------|---------|----------------|
| Packing Descriptor          |                |         |                |
| Number Of Bytes In This Row |                |         |                |
| RUN (0)                     | COLOR CODE (0) | RUN (1) | COLOR CODE (1) |
|                             |                |         |                |
|                             |                |         |                |
| Repeat For Each             |                |         |                |
| Row                         |                |         |                |
| RUN (2)                     | COLOR CODE (2) | RUN (3) | COLOR CODE (3) |
| ·                           |                |         |                |
|                             |                |         |                |
| ·                           | ·              | ·       |                |
| ·                           |                |         |                |
|                             |                |         |                |
| ·                           | ·              | ·       |                |
| RUN (N)                     | COLOR CODE (N) | 0000    | 0000           |


 
Field name 
 
Type 
 
Units 
 
Range 
Precision/ 
Accuracy 
 
Remarks 
Packing Descriptor 
INT*2 
N/A 
2 
N/A 
Defines packing format 2 
Number of Bytes in This Row 
INT*2 
N/A 
2 to 920 
1 
Number of bytes in this row 
not including self 
Run (0) 
4 Bit INT  
N/A 
0 to 15 
1 
4-bit run code 
Color Code (90) 
4 Bit INT  
N/A 
0 to 15 
1 
4-bit color level 

## D.2.2.3 Deflate Compression Method

DEFLATE is a lossless compressed data format that compresses data using a combination of the LZ77 algorithm and Huffman coding, with efficiency comparable to the best currently available general-purpose compression methods.  The data can be produced or consumed, even for an arbitrarily long sequentially presented input data stream, using only a priority-bounded amount of intermediate storage.  The format can be implemented readily in a manner not covered by patents.  Specifications for DEFLATE can be found in RFC 1951 - DEFLATE Compressed Data Format Specification, May 1996. 

## D.2.2.4 Weather-Huffman (Wh) Method Of Data Compression Of Weather Images

MIT Lincoln Laboratory developed the WH compression algorithm as an optimal mechanism for the transfer of graphical precipitation maps via a bandwidth-restricted data link.  The WH algorithm combines a number of standard graphical compression techniques including Huffman-coding, Hilbert-scan, run length encoding, etc. together with many special-case mechanisms to achieve better compression performance than any other existing compression algorithm.  Documentation about the WH algorithm may be found in Reference (1) at the end of this section along with the Reference (2) source for obtaining license for the operational software and software documentation for the WH 
algorithm (encoder and decoder). The WH algorithm encoder takes as its input a square matrix of pixels whose dimension is a power-of-two and where each pixel contains a weather-level encoding.  The current software implementation assumes a 256-by-256 pixel-input weather map where each pixel encodes weather levels 0-7 (Note: the WH algorithm can be extended to larger input maps or more weather levels per pixel).  The WH algorithm encoder output is an encoded bit-string and the bit count.  The WH algorithm decoder performs the reverse process, converting its input bit-string into a pixel matrix. The WH algorithm is unique in that it can be operated in either lossless or lossy modes.  
The WH algorithm encoder accepts a bit limit parameter; the encoded output will use only this many bits while minimizing image distortion.  If the bit limit is set to "infinity" (more than the number of bits in the uncompressed input), then the WH algorithm will be lossless (although the exact degree of compression will vary with the complexity of the input data).  Some examples of the lossless operation of the WH algorithm may be found in Reference (1).  Reference (1) provides details of the extent of the compression that can be obtained using this method.  Lossless compression of up to 11:1 was obtained in these specially chosen cases of very severe weather.  The WH algorithm could have even higher compression on less-severe weather inputs. It should be noted that the encoded bit-string produced by the WH algorithm encoder is monolithic.  The weather map cannot be decoded unless the entire encoded bit-string is complete and uncorrupted.  The WH algorithm decoder is quite effective at detecting corrupted input, but missing or corrupted data cannot be corrected. References: 
(1) "The Weather-Huffman Method of Data Compression of Weather Images," J. Gertz, October 31, 1997, Project Report ATC-261 (2) MIT Technology Licensing Office, Massachusetts Institute of Technology, Room NE25-230, Five Cambridge Center, Kendall Square, Cambridge, MA. 

Note:  Although this is not required, the use of the WH algorithm requires a license. 

## D.2.2.5 Png And Mng Image Formats

The PNG or Portable Network Graphics standard is an extensible file format for the lossless, portable, well-compressed storage of raster images.  PNG utilizes the highly effective ZLIB compression algorithm, a direct extension of the DEFLATE algorithm.  
PNG provides a patent-free replacement for GIF and can also replace many common uses of TIFF.  Indexed or palette color (normally used for NEXRAD weather images), grayscale (normally used for satellite weather images), and true color images (normally used for photographic images, not weather), are supported.  Sample depths range from 1 to 16 bits.  PNG is robust, providing both full file integrity checking and simple detection of common transmission errors.  Also, PNG can store gamma and chromaticity data for improved color matching on heterogeneous platforms although these elements are not required.  PNG has been identified as the standard lossless still-image interchange format for DOD networks as a W3C Recommendation within the document, "Department of Defense Joint Technical Architecture," Version 3.0 dated Nov. 15, 1999. For more information on the PNG format, consult RFC-2083 ("PNG (Portable Network Graphics) Specification," Version 1.0, W3C Recommendation October 01, 1996), which is found on the website of the Internet Engineering Task Force (IETF), http://www.ietf.org. 

For more information on the ZLIB compression format, consult the standard document RFC-1950 Deutsch, P. and J-L. Gailly, "ZLIB Compressed Data Format Specification version 3.3," Aladdin Enterprises, May 1996, and the website of the Internet Engineering Task Force (IETF), http://www.ietf.org. 

MNG, or Multiple-Image Network Graphics is an animation graphics standard that utilizes a set of either PNG or JPEG images, and is thus either lossless or lossy dependent upon the underlying image format.  MNG permits the precisely controlled sequential display of the image sets.  When used with PNG images all the requirements and feature of the PNG format are incorporated for the individual images.  A delta image compression capability permits very efficient compression of multiple images.  MNG is fully compatible with PNG, utilizing PNG images as its basis. For more technical information, consult "MNG (Multiple-image Network Graphics) 
Format, Version 1.0; January 31, 2001 and the website, http://www.libpng.org/pub/mng/. 

## D.2.3 Geographic Reference Method Or File Format

Graphical weather will be created as bit maps representing some portion of the surface of the earth as a flat surface.  These bit maps are created according to mathematical formulae that we refer to as the map projection (or geographic reference/geo-referencing) 
method.  Each bit map is comprised of a grid of x-y coordinates.  In order to display the weather maps on the aircraft, the means by which the weather map grid was created needs to be understood.  The geographic reference method shall be described in sufficient detail so that any avionics supplier can navigate through the uplinked dataset grid and extract the portion relevant to current display settings.  This field tells the receiver which geographic reference method was used to create the data matrix in the application file; 
see Table D-7 for a listing of the Field Values.  Although other methods exist, a limit should be imposed to contain memory and processing requirements on aircraft avionics. The following assumptions apply: 

a. As part of the FIS-B Product File, the ground station provider may transmit 
geographic parameters with each broadcast to alleviate the need for an on-board 
database, or may substitute a scheme requiring an airborne database. 
b. X increases easterly for all projections. c. Y increases northerly for all projections. 
d. Earth assumed spherical with radius 6367.47 km = 3438 NM. 

| Field Value    | Geographic Reference Method or File Format    | Document Section    |
|----------------|-----------------------------------------------|---------------------|
| 0              | N/A                                           |                     |
| 1              | Cylindrical Equidistant                       | D.2.3.1             |
| 2              | Lambertian                                    | D.2.3.2             |
| 3              | Polar Stereographic                           | D.2.3.3             |
| 4              | GeoTIFF file format                           | D.2.3.4             |
| 5              | Global Block Representation                   | D.2.3.5             |
| 6-15           | Reserved                                      |                     |
|                |                                               |                     |

 
                          Note: 
                                       These map projections conform to the "US Geological Survey Professional 
                                       Paper 1395: Map projections - A working manual," by John P. Snyder.  Even if 
                                       the same geo-referencing algorithm is used then the projected area may be 
                                       different if a different datum is used. 

## D.2.3.1 Cylindrical Equidistant

The cylindrical equidistant method has been in use at least since 100 AD; making it one of the oldest, as well as one of the simplest, map projections.  In this projection a portion of the earth's spherical surface is projected onto a cylinder that is tangent to the earth at the standard parallel, often the equator.  The cylinder is oriented parallel to the standard meridian.  Straight lines represent the poles, not a point.  See P 91 of the US Geological Survey (USGS) working manual by Snyder for the equations that describe the projection.  
An ANS.1 representation of this geo-referencing method is presented in Table D-8.  The Cylindrical Equidistant projection is characterized by the following: 

a. Meridians and parallels are equidistant straight lines, intersecting at right angles. 
b. North/south resolution is constant (independent of latitude). 
c. East/west resolution depends on latitude.  Scale is fixed (scale error is 0) on standard 
parallel. 
d. Assume standard parallel is southern boundary. e. Also known as Equirectangular projection. 

## D.2.3.2 Lambertian

This geo-referencing method, developed by Johann Lambert in 1772, projects a portion of the earth's surface onto a portion of a cone slicing through the earth's sphere between two parallels.  On those two parallels, scale error is 0.  A point at which meridians converge represents the pole that is in the same hemisphere as the standard parallels.  An ANS.1 representation of this geo-referencing method is presented in Table D-9.  The Lambertian projection is characterized by the following: 

a. Lambert conformal secant conic projection.  (Note: it is conformal, meaning relative 
local angles about every point are correct.) 
b. Parallels are unequally spaced arcs of concentric circles. c. Meridians are equally spaced radii of concentric circles; they intersect parallels at 
right angles. 
d. Scale is true along two standard parallels. e. Used for maps of countries and regions with predominant east-west expanse, also for 
1:1,000,000 regional and 1:500,000 sectional aeronautical charts. 

## D.2.3.3 Polar Stereographic

In this projection, the plane of projection is tangent to the earth at the north or South Pole.  
The point of projection is from the opposite pole (lines diverge from the South Pole onto plane at North Pole).  The plane may be a secant plane that cuts through the earth at a  
particular latitude.  An ANS.1 representation of this geo-referencing method is presented in Table D-10.  The Polar Stereographic projection is characterized by the following: 

a. Azimuthal and conformal 
b. Central meridian are straight lines c. It has a polar aspect, not equatorial or oblique stereographic 
d. All meridians on polar aspect are straight lines; all other meridians and parallels are 
arcs 
e. Scale increases away from the center of the projection 
f. The scale is true at 60 degrees latitude  (central scale factor Ko = 0.933) 
g. A rectangular grid is transmitted h. A spherical datum is specified 

Cylindrical_equidistant::= SEQUENCE 
 
{ 
 
standard_parallel, 
 
standard_meridian, 
 
scale_on_std_parallel, 

 
scale_on_std_meridian, 
 
N_points_X, 
 
N_points_Y, 
 
Western_boundary, 
 
Eastern_boundary  OPTIONAL, 
 
Southern_boundary OPTIONAL, 
 
Northern_boundary OPTIONAL 

 
} 

standard_parallel ::= Latitude_hundredths 
-- latitude given of scale, assumed to be bottom row, called φ1 in Snyder standard_meridian ::= Longitude_hundredths, λo  in Snyder 
-- center of projection  (east/west) Western_boundary ::= Longitude_hundredths Eastern_boundary ::= Longitude_hundredths Southern_boundary ::= Latitude_hundredths Northern_boundary ::= Latitude_hundredths Latitude_hundredths::=INTEGER(-9000 .. 9000) -- Latitude in degrees/hundredths of degrees Longitude_hundredths::=INTEGER(-18000 .. +18000) --Longitude in degrees/hundredths of degrees N_pts_X ::= INTEGER(0..8191) N_pts_Y ::= INTEGER(0..8191) scale_on_std_parallel::=   INTEGER(1..16384) --scale on X axis in m, k in Snyder scale_on_std_meridian::= INTEGER(1..16384) --scale on Y axis in m, h in Snyder Example: 
Standard_meridian  = -95.00 degrees 

 
Standard_parallel = 20.00 degrees 
 
Scale_on_std_parallel = 2 km, decreasing northerly 
 
Scale_on_std_meridian = 2 km 
 
N_pts_X = 3661 
 
N_pts_Y = 1837 
 
Western_boundary  = -130.00 degrees 
 
Eastern_boundary   =   -60.00 degrees 
 
Southern_boundary =    20.00 degrees 
 
Northern_boundary =    53.00 degrees 
Lambert_conic::= SEQUENCE 
{ standard_parallel_N, standard_parallel_S, central_meridian, scale_on_std_parallel_N, scale_on_std_parallel_S, N_points_X, N_points_Y, Origin_latitude, Origin_longitude, False_easting OPTIONAL, False_northing  OPTIONAL 
} 
standard_parallel_N ::= Latitude_hundredths 
--northern true scale latitude, φ2 
standard_parallel_S::= Latitude_hundredths 
--southern true scale latitude, φ1   in Snyder central_meridian ::= Longitude_hundredths 
-- center of projection (east/west), Y axisλo origin_latitude ::= Latitude_hundredths 
--origin of projection (north/south) , φo Northern_boundary ::= Latitude_hundredths 
 
Latitude_hundredths::=INTEGER(-9000 .. 9000) -- Latitude in degrees/hundredths of degrees Longitude_hundredths::=INTEGER(-18000 .. +18000) --Longitude in degrees/hundredths of degrees N_pts_X ::= INTEGER(0..8191) --number of points on x axis (number of elements/line) N_pts_Y ::=INTEGER(0..8191) -- number of points on y axis (number of lines/image) scale_on_std_parallel::= INTEGER(1..16383) --scale on std parallel in m, k scale_on_std_meridian::= INTEGER(1..16383) --scale on std meridian in m, h False_easting ::= INTEGER(0..8191) --shift of X axis in meters * 100 False_northing ::=INTEGER(0..8191) --shift of Y axis in meters * 100 -- If Standard_parallel_N = Standard_parallel_S then the projection is on a tangent cone. 

Polar_Stereographic::=SEQUENCE 
{ hemisphere, 
N_pts_X, N_pts_Y, Latitude_upper_left, Longitude_upper_left, Straight_vertical_longitude, Grid_resolution, False_easting 
OPTIONAL, 

False_northing OPTIONAL } 
hemisphere::=BOOLEAN 
--1 if north pole, 0 if south pole N_pts_X::=INTEGER(0..8191) 
--number of points along x axis N_pts_Y::=INTEGER(0..8191) --number of points along y axis straight_vertical_longitude::=INTEGER(-180..180) --longitude in degrees to be oriented straight up from the north or south pole Y increases  
 --vertically along this axis,  λo. 

Latitude_upper_left::=Latitude_hundredths -- Latitude of upper left corner of grid in .01 degrees Longitude_upper_left::=Longitude_hundredths -- Longitude of upper left corner of grid in .01 degrees Latitude_hundredths::=INTEGER(-9000 .. 9000) -- Latitude in degrees/hundredths of degrees Longitude_hundredths::=INTEGER(-18000 .. +18000) --Longitude in degrees/hundredths of degrees Grid_resolution::=INTEGER(0..8191) -- resolution of grid element in meters (dx, dy same) determined by central scale factor, radius, k False_easting ::= INTEGER(0..8191) --offset of X axis (lower left corner of grid) in meters * 100 False_northing ::=INTEGER(0..8191) --offset of Y axis (lower left corner of grid) in meters * 100 

## D.2.3.4 Geotiff File Format

GeoTIFF is a means of adding geo-referencing information to files stored in Aldus- Adobe's public domain Tagged-Image File Format (TIFF).  The GeoTIFF Format Specification Rev 1.0 states "The GeoTIFF spec defines a set of TIFF tags provided to describe all 'Cartographic' information associated with TIFF imagery that originates from satellite imaging systems, scanned aerial photography, scanned maps, digital elevation models, or as a result of geographic analyses.  Its aim is to allow means for tying a raster image to a known model space or map projection, and for describing those projections." As TIFF provides for compression, files that use the GeoTIFF structure should indicate "no compression" in the header, to indicate that no compression other than TIFF is used in generating the file. 

GeoTIFF 
Format Specification Rev 
1.0 
can be found at http://home.earthlink.net/~ritter/geotiff/spec/geotiffhome.html. 

## D.2.3.5 Global Block Representation

This geo reference method is based on a global grid of blocks and bins.  It was developed to support uplink of a common base image product from multiple origins simultaneously in a globally seamless manner with independent APDUs.  This approach includes a specific form of data compression.  Therefore this method does not require a separate compression method callout. 

## D.2.3.5.1 The Use Of "Bins" And "Blocks"

This geo reference approach employs a global grid of "bins" which represent the smallest granularity of uplink image data to be rendered on the cockpit display.  For purposes of bandwidth efficient transmission, bins are run length encoded.  To simplify and optimize run length encoding, bins are grouped into "blocks". The coordinate system for bins is oriented to the axes of latitude and longitude.  The relationship between bins and blocks are shown in Figure D-1.  In the latitude axis, bins always have a dimension of 1 arc minute or 1 nmi.  In the longitude axis bin, width is constant in minutes, which results in a variable distance proportional to the cosine of its latitude.  In order to prevent unnecessary over-sampling of image data at high latitude, the longitudinal bin width is increased from 1.5 minutes below 60 degrees, to 3 minutes above 60 degrees.  These bin dimensions are designed to match the maximum resolution of the NEXRAD sensor as closely as possible, on average. 

## D.2.3.5.2 Global Block Numbering Plan D.2.3.5.2.1 Grid Layout

The origin of the block numbering system is at the prime meridian and the equator. Numbering is symmetric about the equator; northern and southern hemispheres are distinguished with a sign bit.  Positive block numbering begins with the block just east and north of the prime meridian and equator (block number 0).  Block numbers increment in an easterly direction until the entire "ring" of blocks is closed back at the prime meridian.  Each ring will consist of 450 blocks below 60 degrees latitude, and 225 blocks above 60 degrees.  Block numbers continue to increment in each successive ring in the direction of the poles.  Note that above latitude 60 degrees, only even block numbers are assigned.  This is to maintain a globally consistent relationship of 48 minutes of longitude per block increment.  See Figure D-2 for a graphic representation of the assignment of block numbers. 

## D.2.3.5.2.2 The Block Reference Indicator

Three bytes are used to encode the Block Reference Indicator as depicted in Figure D-3 
below.  The Block Reference Indicator contains an Element Identifier bit, the hemisphere bit, and the Block Number. 

Bit Number
Byte #
7
6
5
4
3
2
1
0
Element Identifier
N/S
0
Spare
Block Number (MSb )
Block Number
1
2
Block Number
(LSb )
 

Element Identifier: This indicates the type of image data element that is represented relative to the block location identified.  The data elements are one of two types:  
Run Length Encoded Element: the encoded information associated with the Block number provided is a run length encoding of all bins within the identified block.  The Element Identifier bit will take on the value of 1. 

Empty Element: the encoded information represents multiple empty blocks with the identified block number as a reference point.  The Element Identifier bit will take on the value of 0. 

Hemisphere N/S: For blocks in the Northern Hemisphere this bit will be set to 0.  For blocks in the Southern Hemisphere this block will be set to 1. 

Encoding of the Block Number: Twenty-one bits are required to uniquely identify all blocks on the globe with the numbering plan defined above.  However, 23 bits are reserved resulting in 2 spare bits.  This could allow for future capability to increase product resolution. 

## D.2.3.5.3 Run Length Encoding Of Cells Within The Block

Creating "runs" of bins of identical intensity (or reflectivity) within a single Block forms a Run Length Encoded Element.  A run is represented by 1 byte as shown in Figure D-4.  
Run length encoding always begins in the northwest corner of the block in a west-to-east and then north-to-south raster style.  The maximum run allowed is 32 bins.  Encoding this maximum amount can be represented in only five bits if one considers that every run is greater than or equal to one.  We therefore subtract the value of 1 from this maximum amount yielding an adjusted maximum value of 31, which can be delivered in 5 bits. Runs may span rows of bins within the block.  A maximum of 8 levels of intensity can be conveyed. 

Figure D-5 shows a block containing 12 runs of varying intensities.  The run length encoding information for this block is contained in Table D-11 below.  The total number of bins encoded per block will always be 128.  In the worst case—minimum compression—scenario there would be 128 runs of length 1 bin each. 

|   Run Length  |   Intensity  |   Cumulative Bins  | Encoded Run (binary)    |
|---------------|--------------|--------------------|-------------------------|
|            9  |           0  |                 9  | 01000 000               |
|           15  |           1  |                24  | 01110 001               |
|            7  |           2  |                31  | 00110 010               |
|            1  |           3  |                32  | 00000 011               |
|            8  |           0  |                40  | 00111 000               |
|           18  |           1  |                58  | 10001 001               |
|            6  |           2  |                64  | 00101 010               |
|            6  |           0  |                70  | 00101 000               |
|           32  |           1  |               102  | 11111 001               |
|           26  |           1  |               128  | 11001 010               |

The complete encoding of a Run Length Encoded Element is shown in Figure D-6.  Note that there is no explicit length field since the receiving application interprets each successive byte as an encoded run until all 128 bins of the Block are accounted for. 

Bytes are transmitted in sequence beginning with byte 0.  Within each byte, bits are transmitted in sequence beginning with bit 0. 

## D.2.3.5.4 The "Empty" Element

Most uplink images of any size will almost always contain large areas void of detectable precipitation (or other product).  Unfortunately, the run encoding on a bin basis described above will not fully exploit this fact and would result in inefficient bandwidth use for these large areas void of weather.  This is because with this approach even "empty" 
blocks would require a precipitation block with 4 runs each.  We can do much better for the special case of empty blocks with a special "Empty" Element encoding.  The Empty Element uses a bitmap encoding of all empty blocks that are contained in a row of blocks. The Block Number encoded in the Block Reference Indicator identifies the Starting Block Number (i.e., the first empty block) within a row of blocks.  Figure D-7 below shows the format. 

 
Bytes are transmitted in sequence beginning with byte 0.  Within each byte, bits are transmitted in sequence beginning with bit 0. 

## D.2.3.5.4.1 Length And Bitmap Bytes

Bitmap bytes begin at byte #3 and extend to the end of the Empty Element as shown in Figure D-8.  There are a total of L additional bytes in the bitmap, per the Bitmap Length 
 
field in byte #3.  Starting at byte #3 the bitmap bytes are denoted as bb0, bb1, ..., bbL-1, and bbL in Figure D-8 below. 

 

| bb0                      | bb1      | bb2      | bbL-1    |      bbL | Byte #   |
|--------------------------|----------|----------|----------|----------|----------|
| * * * *                  |          |          |          |          |          |
| LLLL                     |          |          |          |          |          |
| ********                 | ******** | ******** | ******** |          |          |
| 76543210                 | 76543210 | 76543210 | 76543210 | 76543210 | Bit #    |
| L = Length bits          |          |          |          |          |          |
| * = Bitmap bits          |          |          |          |          |          |
|                          |          |          |          |          |          |
| Figure D-8  Bitmap Bytes |          |          |          |          |          |

Length:  In bitmap byte 0 (bb0) bits 0-3 represent L in Figure D-8, the number of bitmap bytes to follow.  Given L, the number of bit-mapped Blocks is equal to the number of bits in L bytes plus the number of bitmap bits in bb0. 

 
Equation #1 Number of bit-mapped Blocks = (8 * L) + 4 
 
Since the Block identified in the Block Reference Indicator is always the first empty Block in a row of Blocks, the number of potential empty Blocks in the row is equal to the number of bit-mapped Blocks plus one (the first Block). 

 
Equation #2 Number of potential empty Blocks = (8 * L) + 4 + 1 
 
Since the length field is four bits, the maximum value for L is binary 1111 or decimal 15. Substituting in eq#2, we get the maximum row size that can potentially be encoded: (8 * 15) + 4 + 1 = 125 blocks.  This allows a single Empty Element to span an area of 4 nmi in "height" by over 3000 nmi in "width". 

Bitmap:  The value of the bits in the bitmap bytes determines the "emptiness" of the block it represents.  The block is empty when the bit is set to 1.  Each block represented by a zero will also be conveyed in a separate Run Length Encoded Element. 

## D.2.3.5.4.2 Mapping Bits To Blocks

The emptiness of the blocks following the Starting Block Number is determined from the bit locations shown in Table D-12 below.  The bitmap bits are set according to the emptiness of the blocks following the Starting Block Number.  When this mapping is viewed in an octal format a pattern emerges showing the correlation between block number offset and bitmap location. 

| Byte                 | Bit Location    |
|----------------------|-----------------|
| Block Number (octal) |                 |
| bb0                  | bit 4           |
|                      | bit 5           |
|                      | bit 6           |
|                      | bit 7           |
| bb1                  | bit 0           |
|                      | bit 1           |
|                      | bit 2           |
|                      | bit 3           |
|                      | bit 4           |
|                      | bit 5           |
|                      | bit 6           |
|                      | bit 7           |
| bb2                  | bit 0           |
|                      | bit 1           |
|                      | bit 2           |
|                      | bit 3           |
|                      | bit 4           |
|                      | bit 5           |
|                      | bit 6           |
|                      | bit 7           |
| -                    | -               |
| -                    | -               |
| bbL                  | bit 0           |
| BN + L*08 + -03      |                 |
|                      | bit 1           |
|                      | bit 2           |
|                      | bit 3           |
|                      | bit 4           |
|                      | bit 5           |
|                      | bit 6           |
|                      | bit 7           |

## D.2.3.5.4.3 Prime Meridian Case

When a row of blocks spanning the Prime Meridian is encoded by the ground system, Empty Element encoding will include all blocks of the row on both sides of the Prime Meridian.  Avionics processing needs to account for this case and properly identify the block numbers on the East Side of the meridian using modulo arithmetic. 

## D.2.3.5.5 Apdu Payload Format For Graphical Image

The Run Length Encoded and Empty elements of the image product as shown in Figure D-6 and Figure D-7 respectively are in a form ready for mapping directly into the APDU 
Payload.  Each APDU will contain one Payload field.  Within a Payload field, any number of either element types can appear in any order and in any combination, subject only to the maximum burst length limitations of the physical media to be used.  Bit and byte transmission order is as described with the encoding description of each element. 

## D.2.4 Geographic Locator

The Geographic Locator shall be included in the FIS-B Product Descriptor if the Geographic Locator Flag Bit is set to 1.  It shall be omitted from the FIS-B Product Descriptor if the Geographic Locator Bit is cleared to 0.  The purpose of the Geographic Locator is to allow FIS-B applications to filter out Products that are not of interest due to their area of coverage.  For example: an aircraft flying from New York to Washington, DC might not care about SIGMET information from Chicago. The Geographic Locator defines "rectilinear" regions on the Earth's surface.  The Geographic Locator shall be defined in terms of an origin corner point (given in latitude and longitude) and a distance (southward and eastward) from that corner point.  For purposes of the Geographic Locator coding, the Earth's surface shall be subdivided into "patches" each 2 degrees of latitude/longitude on a side (approximately 120 nautical miles square at the Equator).  There are 90 latitude steps from 0 degrees latitude (North Pole) to 180 degrees (South Pole).  There are 180 longitude steps from 0 degrees 
(Greenwich) to 360 degrees (eastward).  Hence: 7 bits are used for the origin latitude code and 8 bits for the origin longitude code.  The 5-bit "extent" coding is given in 2- degree steps along the latitude and longitude sides of the rectilinear region.  Hence, the Geographic Locator can indicate distances from 100 to 3200 nautical miles southward and eastward with respect to the origin corner point.  

## D.3 Segmentation Flag

The Segmentation Flag indicates whether the optional Segmentation Data Block is present (bit=1) or omitted (bit=0).  Product Files that are too large for transmission in a single APDU are segmented into multiple APDUs.  In this event, the Segmentation Flag is set to indicate use of the Segmentation Data field, and Product File segments are individually numbered and sequenced. 

## D.4 Apdu Header Time

APDU Header Time is a time reference used to aid in the reassembly of Product Files from independent or linked APDUs.  The APDU Header Time may be the specific time the APDU(s) are created/generated, or it may be some other time established by the FIS-
B provider such as the date/time of the Product File as outlined in Section 3.8.1.2.  Note that the APDU Header Time shall be the same/identical for all linked APDUs. 

## D.4.1 Time Options

Table D-13 provides the option states.  If they are not needed, days and seconds fields are eliminated from the header bit overhead. 

Time Seconds (6 bits) 
Options 
Day of Month 
(5 bits) and Month of year (4 bits) 
00 
Omitted 
Omitted 
01 
Omitted 
Included 
10 
Included 
Omitted 
11 
Included 
Included 

## D.4.2 Month Of Year & Day Of Month (Optional)

The Month of Year field shall give the month of the year in Coordinated Universal Time 
(UTC) (Zulu) time.  The Day of Month field shall give the day in Coordinated Universal Time (UTC) (Zulu) time when the APDU was formatted.  

## D.4.3 Time Hours

The Time Hours field shall give the hour in UTC (Zulu) time.  The Time Hours field remains constant for all APDUs contained in a Product File. 

## D.4.4 Time Minutes

The Time Minute field shall give the minute in UTC (Zulu) time.  The Time Minutes field remains constant for all APDUs contained in a Product File. 

## D.4.5 Time Seconds (Optional)

The Time Seconds field shall give the seconds in UTC (Zulu) time.  The Time Seconds field remains constant for all APDUs contained in a Product File. 

## D.5 Segmentation Data Block

The Segmentation Data Block shall be included in the APDU Header if the Segmentation Flag Bit is set to 1.  It shall be omitted if the Segmentation Flag Bit is cleared to 0.  The purpose of the Segmentation Data Block is to provide information for the re-assembly of an FIS-B Product File that has been segmented into multiple APDUs.  Those FIS-B 
Product Files conveyed by independent APDUs will not use the Segmentation Block mechanism.  The Segmentation Data Block (if present) shall consist of two components, the Product File Length field and the APDU Number field. 

## D.5.1 Product File Length Field

The Product File Length field indicates the number of linked APDUs contained in the FIS-B Product File identified by the Product Descriptor.  The Product File Length field remains constant for all APDUs contained in a Product File. 

## D.5.2 Apdu Number Field

The APDU Number field identifies a specific APDU in a series of linked APDUs.  The APDU Number field increments upward for each transmitted APDU of a Product File. For example, if the Product File Length field is eight and the APDU Number field is three, then the APDU is the third of eight total APDUs contained in the Product File.  

## D.6 Zero Padding

The APDU Header shall be padded with up to 7 zero-valued padding bits in order to make the APDU Header align with the nearest byte boundary (i.e., to make the total number of bits in the APDU Header a multiple of eight).  The number of padding bits (if any) required for a given APDU will vary depending on the particular choice of APDU Header options selected. 

## D.7 Apdu Payload

The APDU Payload contains all or segmented portions of an FIS-B Product File.  The service provider determines the size and format of the Payload.  The data contained in the Payload shall be consistent with the FIS-B Product File specification identified in the APDU Header (D.2 - Product Descriptor) and referenced in the FIS-B Product Registry 
(see Appendix E). 

The Payload data may be further decomposed into reports, records and fields.  To foster consistent terminology among FIS-B Product File specifications, the definition of these entities is provided below as guidance to the developers of these specifications. 

## D.7.1 Report

A report is an instance of a single FIS product.  An APDU may contain one or more reports of a particular FIS product.  For example, a METAR report may be the observation from a ground station or a D-ATIS for an airport.  Each of these reports is instances of the METAR/SPECI product and NOTAMs product, respectively. 

## D.7.2 Record

A record is part of a collection of related items in a report or an alternate means of conveying a report or portions thereof.  In cases where a report is fully represented by a collection of fields, the use of a record does not apply.  Records are exemplified by either representing a report using one of several character sets available (ASCII or DLAC), using ASN-1 to encode the report content or conveying parts of the report using graphical parameters. 

## D.7.3 Field

A field is an element of a Record or Report in which one piece of information is stored. A field is the smallest, most basic data element transmitted.  Fields contain data items found in reports or records such as: location identifier, temperature, block number, latitude, altitude, etc. 

Product Descriptor (14, 22, 34 or 42 bits)
S f l a g
FIS-B APDU ID
(16 bits)
App. Method (Optional)
T
Opt
2
bits
Mth. of
Yr(Opt.
4 bits)
Product ID
(11 bits)
Geographic Locator
(Optional, 20 bits)
A f
G f
P f
Comp.
(4 bits)
Geo Ref
(4 bits)
1
1 1 1 1 1 1
1
1
1 1 1 1 1 0
1
Compression Method (Opt.)
Day of Month (Opt.)
Month of Year (Opt.)
Bit ID
Bit ID
Bit ID
Field
Value
Day
Field
Value
Month
Field
Value
Description
4
3
2
1
5
4
3
2
1
4
3
2
1
Unused
0
0
0
0
0
0
0
0
0
0
0
None
0
0
0
0
0
Unused
0
0
0
0
1
1
1
0
0
0
1
1
Run Length Encoding 1
0
0
0
1
1
1
0
0
0
1
0
2
2
0
0
1
0
2
Run Length Encoding 2
0
0
1
0
2
2
0
0
0
1
1
3
3
0
0
1
1
3
3
0
0
1
1
3
Deflate
0
0
1
0
0
4
4
0
1
0
0
4
4
0
1
0
0
4
Weather Huffman Method
0
0
1
0
1
5
5
0
1
0
1
5
5
0
1
0
1
5
PNG
0
0
1
1
0
6
6
0
1
1
0
6
6
0
1
1
0
6
MNG
0
0
1
1
1
7
7
0
1
1
1
7
7
7-15
Reserved
0
1
0
0
0
8
8
1
0
0
0
8
8
0
1
0
0
1
9
9
1
0
0
1
9
9
0
1
0
1
0
10
10
Geo. Reference Method (Opt.)
1
0
1
0
10
10
0
1
0
1
1
11
11
1
0
1
1
11
11
0
1
1
0
0
12
12
1
1
0
0
12
12
Bit ID
0
1
1
0
1
13
13
Field
Value
1
1
0
1
13
Unused
Description
0
1
1
1
0
14
14
1
1
1
0
14
Unused
4
3
2
1
0
1
1
1
1
15
15
1
1
1
1
15
Unused
1
0
0
0
0
16
16

Discrete List

|   1 |   0 |   0 |   0 |   1 |
|-----|-----|-----|-----|-----|
|   0 |   0 |   0 |   1 |   1 |

Cylindrical Equidistant

|   1 |   0 |   0 |   1 |   0 |
|-----|-----|-----|-----|-----|
|   0 |   0 |   1 |   0 |   2 |

Lambertian

|   1 |   0 |   0 |   1 |   1 |
|-----|-----|-----|-----|-----|
|   0 |   0 |   1 |   1 |   3 |

Polar Stereographic

|   1 |   0 |   1 |   0 |   0 |
|-----|-----|-----|-----|-----|
|   0 |   1 |   0 |   0 |   4 |

GeoTIFF File Format

|   1 |   0 |   1 |   0 |   1 |
|-----|-----|-----|-----|-----|
|   0 |   1 |   0 |   1 |   5 |

Single Text File

|   1 |
|-----|
|   0 |

1
   1
      0
            6

Multiple Text Products File

|   1 |   0 |   1 |   1 |   1 |   23 |   23 |
|-----|-----|-----|-----|-----|------|------|
|   1 |   1 |   0 |   0 |   0 |   24 |   24 |

   1
      1
         1
0
               7
                       Global Block Representation

| 1    | 1        |   0 |   0 |   1 |   25 |   25 |
|------|----------|-----|-----|-----|------|------|
| 8-15 | Reserved |     |     |     |      |      |
| 1    | 1        |   0 |   1 |   0 |   26 |   26 |
| 1    | 1        |   0 |   1 |   1 |   27 |   27 |

Option Flags

| 1                             | 1                      | 1                     |   0 |   0 |   28 |   28 |
|-------------------------------|------------------------|-----------------------|-----|-----|------|------|
| 1                             | 1                      | 1                     |   0 |   1 |   29 |   29 |
| 1                             | 1                      | 1                     |   1 |   0 |   30 |   30 |
| Flag Name                     |                        |                       |     |     |      |      |
| Bit                           |                        |                       |     |     |      |      |
| Value                         |                        |                       |     |     |      |      |
| Description                   |                        |                       |     |     |      |      |
| 1                             | 1                      | 1                     |   1 |   1 |   31 |   31 |
| Application Method            | 0                      | Method Fields omitted |     |     |      |      |
| 1                             | Method Fields included |                       |     |     |      |      |
| Geographic Locator            | 0                      | Geo Loc Field omitted |     |     |      |      |
| 1                             | Geo Loc Field included |                       |     |     |      |      |
| Provider-Specific Flag Bit    |                        |                       |     |     |      |      |
| Geographic Locator (Optional) |                        |                       |     |     |      |      |
| 0                             | Provider Specific      |                       |     |     |      |      |
| 1                             | Provider Specific      |                       |     |     |      |      |
| Lat                           | Long                   | Extent                |     |     |      |      |
| Segmentation                  | 0                      | Seg Fields omitted    |     |     |      |      |
| 1                             | Seg Field included     |                       |     |     |      |      |
| 8                             | 2                      | 1                     |   5 |   3 |    6 |    5 |
| 0                             |                        |                       |     |     |      |      |
| Day of Month and Month of     |                        |                       |     |     |      |      |
| Year omitted                  |                        |                       |     |     |      |      |
| Time Flag #1                  |                        |                       |     |     |      |      |
| Day of Month and Month of     |                        |                       |     |     |      |      |
| Year included                 |                        |                       |     |     |      |      |
| 0-180, N-S, 2 deg res         | 0-360, W-E, 2 deg res  |                       |     |     |      |      |
| S and E,                      |                        |                       |     |     |      |      |
| 2 deg. res                    |                        |                       |     |     |      |      |
| 1                             |                        |                       |     |     |      |      |
| Time Flag #2                  | 0                      | Seconds omitted       |     |     |      |      |
| 1                             | Seconds included       |                       |     |     |      |      |

Note: See Appendix E (FIS-B Product Registry) for source of listing of specific Product Identifier assignments.

|  APDU Header Time (13 or 28 bits)   |   Segmentation Data Block (Optional 24 bits) |
|-------------------------------------|----------------------------------------------|
| Zero Pad                            |                                              |
| (0 - 7 bits A/R)                    |                                              |
| Day of                              |                                              |
| Mth(Opt 5                           |                                              |
| bits)                               |                                              |
| Hours                               |                                              |
| (5 bits)                            |                                              |
| Minutes                             |                                              |
| (6 bits)                            |                                              |
| Seconds                             |                                              |
| (Opt. 6 bits)                       |                                              |
| Product File Length                 |                                              |
| (12 bits)                           |                                              |
| APDU Number                         |                                              |
| (12 bits)                           |                                              |
| 0 0 0 0 0                           |                                            0 |
| Minutes /                           |                                              |
| Seconds  (Opt.)                     |                                              |
| Minutes /                           |                                              |
| Seconds cont. (Opt.)                |                                              |
| Hours                               |                                              |
| Bit ID                              |                                              |
| Field                               |                                              |
| Value                               |                                              |
| Bit ID                              |                                              |
| Time                                |                                              |
| Bit ID                              |                                              |
| Field                               |                                              |
| Value                               |                                              |
| Min. /                              |                                              |
| Sec.                                |                                              |
| Field                               |                                              |
| Value                               |                                              |
| Min. /                              |                                              |
| Sec.                                |                                              |
| 5                                   |                                            4 |
| 6                                   |                                            5 |
| 5                                   |                                            4 |
| 0                                   |                                            0 |
| 0                                   |                                            0 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            0 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            0 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            0 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            0 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            0 |
| 1                                   |                                            0 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 0                                   |                                            0 |
| 1                                   |                                            0 |
| 1                                   |                                            1 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 1                                   |                                            1 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 1                                   |                                            1 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 1                                   |                                            1 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 1                                   |                                            1 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 1                                   |                                            1 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 1                                   |                                            1 |
| 0                                   |                                            1 |
| 1                                   |                                            0 |
| 1                                   |                                            1 |
| 0                                   |                                            1 |
| 1                                   |                                            1 |

24 - 31 Unused

| 0               |   1 |   1 |   0 |   0 |   0 |   24 |   24 |
|-----------------|-----|-----|-----|-----|-----|------|------|
| 1               |   1 |   1 |   0 |   0 |   1 |   57 |   57 |
| 0               |   1 |   1 |   0 |   0 |   1 |   25 |   25 |
| 1               |   1 |   1 |   0 |   1 |   0 |   58 |   58 |
| 0               |   1 |   1 |   0 |   1 |   0 |   26 |   26 |
| 1               |   1 |   1 |   0 |   1 |   1 |   59 |   59 |
| 0               |   1 |   1 |   0 |   1 |   1 |   27 |   27 |
| 60 - 63 Unused  |     |     |     |     |     |      |      |
| 0               |   1 |   1 |   1 |   0 |   0 |   28 |   28 |
| 0               |   1 |   1 |   1 |   0 |   1 |   29 |   29 |
| 0               |   1 |   1 |   1 |   1 |   0 |   30 |   30 |
| 0               |   1 |   1 |   1 |   1 |   1 |   31 |   31 |
| Continued above |     |     |     |     |     |      |      |

## Table D-14  Asn.1 Representation Of The Apdu

FisBAPDUFormat DEFINITIONS AUTOMATIC TAGS ::= BEGIN 
 
FisBAPDU ::= SEQUENCE { 
protocolIdentifier BIT STRING DEFAULT '1111111111111110', 
 
APDUHeader, -- Application data is an arbitrary-length string of bits -- Data is aligned on an octet boundary by padding the APDU header EncodedAPDUData 
} APDUData ::= BIT STRING EncodedAPDUData ::= TYPE-IDENTIFIER.&Type( APDUData) APDUHeader ::= SEQUENCE { 
ProductDescriptor, 
 
APDUHeaderTime, 
 
SegmentationData OPTIONAL 
} ProductDescriptor ::= SEQUENCE { 
 
 
providerFlag BOOLEAN, -- Product identifier values are defined in the FIS-B Product Registry (Appendix E) 
productIdentifier INTEGER (0..2047), ApplicationMethods OPTIONAL, 
 
GeoLocator OPTIONAL 
} 
APDUHeaderTime ::= SEQUENCE { 
MonthDay  OPTIONAL, 
 
uTCHours INTEGER (0..23), 
 
minutes INTEGER (0..59), 
 
seconds INTEGER (0..59) OPTIONAL 
} MonthDay ::= SEQUENCE { 
monthofYear INTEGER (0..12),  --note: code 0 reserved 
 
dayofMonth INTEGER (0..31) 
--note: code 0 reserved 
} 
 

 
ApplicationMethods ::= SEQUENCE { -- Application compression methods are defined in Table D-3 
compressionMethod INTEGER (0..15), 
 
-- Application geographic reference methods are defined in Table D-7 
geographicReferenceMethod INTEGER (0..15) 
} SegmentationData ::= SEQUENCE { -- Number of APDUs contained in application data file 
productFileLength INTEGER (0..4095), -- Identifier number for particular APDU in application data file 
aPDUNumber INTEGER (0..4095) 
} -- Earth's surface is subdivided into "patches" 2 degrees (~120 Nmi) on a side -- Latitude from 0 (north) to 180 (south) ==> 90 steps -- Longitude from 0 (Greenwich) to 360 ==> 180 steps -- Geographic reference origin is "northwest corner" of "patch" -- Extent (distance southward/eastward) is: (n+1) * 2 degrees -- Hence, a Geo-locator can cover a region from ~ 120 to 3800 nautical miles on a side GeoLocator ::= SEQUENCE { 
cornerLatitude INTEGER (0..90), 
 
cornerLongitude INTEGER (0..180), 
 
extent INTEGER (0..31) 
} END 
 
This page intentionally left blank. 

 

## Appendix E Fis-B Product Registry

This page intentionally left blank. 

## Appendix E Fis-B Product Registry

This appendix provides background on the FIS-B Product Registry.  The FIS-B Product Registry provides a publicly accessible source for listing the Product Identifiers contained in an APDU Header along with the description of the APDU Payload encoding for the associated FIS-B Product Files. 

The APDU is comprised of two elements; the APDU Header followed by the APDU Payload.  The APDU Header fields contain information necessary for the receiving avionics to process, store, and display an FIS-B Product File contained in the APDU Payload.  The APDU Payload fields contain all or segmented portions of an FIS-B Product File. This FIS-B Product Registry may be used by any data link communications service that employs the APDU format specified in this MASPS.  The FIS-B Product Registry contains the following key items: 

a. Product Identifier listing.  The Product Identifiers are a data field in the Product 
Descriptor Field in the APDU Header (see Section D.2.1); 
b. APDU Payload encoding (or reference source for propriety products) for the 
associated FIS-B Product Files (see Section D.7);  
c. FIS-B data link listing of all registered networks that are using the APDU format;  
d. Application procedures for requesting additions or updates to the FIS-B Product 
Registry. 

## E.1 Fis-B Product Registry Control

The FAA through the Aerospace Weather Policy and Standards Staff and the William J. Hughes Technical Center (WJHTC) Weather Processors and Sensors Group are responsible for maintaining the FIS-B Product Registry.  All requests for assignment of an FIS-B Product Identifier or for including APDU Payload encoding specifications for new FIS-B Product Files in the registry should be submitted as outlined below in Section E.4. 

The FIS-B Product Registry is maintained as a website and may be accessed using the following URL:  http://fpr.tc.faa.gov.  During the initial website access, user registration will be accomplished and a User Name and Password established for full access to the FIS-B Product Registry. Correspondence may be addressed to the following address: Federal Aviation Administration Federal Aviation Administration Aerospace Weather Policy and Standards Staff William J. Hughes Technical Center 
(FIS-B Product Registry) 
Weather Processors and Sensors Group 
800 Independence Avenue, SW 
(FIS-B Product Registry) 
Washington DC, 20591 
Atlantic City International Airport Atlantic City, NJ 08405 
E.2 
FIS-B Product Identifier The Product Identifier is an 11 bit field with field values from "0" to "2047" which describes to the avionics receiver the FIS-B Product contained in the Payload field of the APDU (see Section D.2.1).  The FIS-B Product Registry lists the Product Identifiers together with the products supported as a separate page on the website.  The content and format of the data fields in the specific FIS-B Product Files are described in the APDU 
Payload section of the website. 

## E.3 Apdu Payload

The APDU Payload field includes all or segmented portions of an FIS-B Product File. The Product Registry includes the minimum specifications for encoding/decoding the FIS-B Product Files, or the reference source for proprietary or developmental products. Two types of FIS-B Product Files are listed in the Product Registry:  Operational Products and Developmental Products.  To be accepted for listing in the Product Registry, a proposed FIS-B Product File needs to meet the definition as either an Operational Product (E.3.1) or Developmental Product (E.3.2). 

## E.3.1 Operational Products

These Product Files represent FIS Products that are intended and ready for operational use on an operational FIS-B data link system.  For all Operational Products, a Product Identifier will be assigned and information on encoding/decoding the product file (or reference source for proprietary products) included in the Product Registry.  Once a Product Identifier has been assigned, it will remain valid even if it is no longer being actively used. Operational products may include provisions for future version changes.  When version management is planned, the procedures for including the new version specifications in the FIS Product Registry apply (See Section E.4.3.1).  In this case, the same Product Identifier will be used.  Each successive version may add features that cannot be processed by previous versions.  However, if the new version is not backward compatible with the basic features of the initial version, then a new Product Identifier shall be assigned. 

## Notes:

1. Some projected FIS Products were assigned Product Identifier numbers in the initial 
RTCA DO-267, March 27, 2001.  Those assignments and all pre-existing Product Identifier uses, prior to the issuance of RTCA DO-267 Revision A will remain valid. 
2. No more than ten (10) Product Identifiers may be assigned to any FIS-B data link 
system that requests assignment of an operational Product Identifier for transmission of proprietary FIS Products.  With the advice and consent of the requesting FIS-B data link service provider, Product Identifier numbers assigned to proprietary products may be reassigned when no longer in use. 
The Product Registry will initially include the Operational Product types listed below.  It is anticipated that additional types may be included as new products and/or new (and improved) encoding techniques are developed. 

a. Textual Products 
b. Graphical Products c. Gridded Products 
d. Generic Products 

## E. Proprietary Products F. System Information Products E.3.2 Developmental Products

These Product Files represent FIS Products that are in an evolutionary (development or experimental) stage, and are not ready for operational use.  Access to these products will be limited to the participants in the associated research and development activity.  For all Developmental Products, a Product Identifier will be assigned and information on the reference source for participating in the R&D activity included in the FIS-B Product Registry.  The Product Identifier assignment will be temporary for thirty-six (36) month increments (renewable). 

Note: 
One Product Identifier number will be assigned per FIS-B data link system for 
such testing and development.  These Product Identifier numbers may be reassigned when no longer in use. 

## E.4 Fis-B Product Registry Application

An application for User Registration or additions or updates to the FIS-B Product Registry should be submitted to the WJHTC Weather Processors and Sensors Group using the online application on the FIS-B Product Registry website (see Section E.1).  
Follow the procedures outlined in the following sections. 

## E.4.1 User Registration

All individuals and/or organizations that desire access to the FIS-B Product Registry may do so by supplying contact information and establishing a username and password. 

## E.4.2 Fis-B Data Link Network Registration

All FIS-B Data Link Networks which are using the FIS-B APDU format specified in this MASPS are encouraged to register that use in the FIS-B Product Registry.  This will provide cross-reference information for coordinating any future changes or updates to the MASPS, especially the FIS-B Product Registry. 

## E.4.3 Fis-B Product File Registration

An application for including a new APDU Payload encoding of an FIS-B Product File in the FIS-B Product Registry is accomplished by completing the FIS-B Product Registry Application form which is available on the Product Registry website. 

## E.4.3.1 Operational Products

Upon receipt of the application, the steps outlined below will be followed: 

a. The application information will be posted to the FIS-B Product Registry website and 
advertised to all registered FIS-B Product Registry users within 30 days after receipt of the application.  The WJHTC Weather Processors and Sensors Group will coordinate with the applicant to clarify any unclear or incomplete items in the 
application. 
b. A 90-day comment period will be established for receipt of any comments and/or 
recommendations for changes/edits to the proposed APDU Payload encoding of an FIS-B Product File.  Those comments will remain posted on the website for 30 days 
beyond the comment period. 
c. The WJHTC Weather Processors and Sensors Group will coordinate with the 
applicant to insure they have received all comments submitted.  The applicant will 
accept or reject the comments as appropriate and submit (within 60 days) the final FIS-B Product File for posting to the APDU Payload encoding section of the FIS-B Product Registry along with the rationale for accepting or rejecting the comments received.  Any resulting issues or actions will be coordinated with the FAA 
Aerospace Weather Policy and Standards Staff. 
d. The final registration will be posted to the website and disseminated via email to all 
registered FIS-B Product Registry users.  That registration will include assignment of 
an appropriate Product Identifier.  The applicant's rationale for accepting or rejecting 
any comments received will also be posted to the website for 30 days. 

## Notes:

1. All FIS-B data link networks are encouraged to use the existing FIS-B Product Files 
to the maximum extent possible.  This will minimize the need for maintaining multiple 
software processing applications. 
2. For Proprietary Products, only the last step above (Step d) applies; the first three 
steps (a-c) are omitted. 

## E.4.3.2 Developmental Products

Upon receipt of the application, the steps outlined below will be followed: 

a. The FIS-B Product File will be added to the FIS-B Product Registry as a thirty-six 
(36) month temporary assignment.  That registration will also include assignment of an appropriate Product Identifier. 
b. The registration will be posted to the website and disseminate via email to all 
registered FIS-B Product Registry users. 

## Appendix F Exceptions To Strict Compliance With Iso 3309 (Normative)

This page intentionally left blank. 

## Appendix F Exceptions To Strict Compliance With Iso 3309 (Normative)

Strict compliance with all the provisions of ISO 3309 may not be appropriate for some implementations.  
Exceptions to strict compliance with ISO 3309 are outlined below. 

## F.1 Vdl Mode 2 Unnumbered Information Link Layer Frame Format

|                    | First Bit Transmitted    |
|--------------------|--------------------------|
| Bit   Number       |                          |
| ↓                  |                          |
|                    |                          |
|                    |                          |
| Description        | Octet No. 8              |
| Flag               | 0                        |
| 1                  | d                        |
| 22                 |                          |
| d                  |                          |
| 23                 |                          |
| d                  |                          |
| 24                 |                          |
| d                  |                          |
| 25                 |                          |
| D                  |                          |
| 26                 |                          |
| d                  |                          |
| 27                 |                          |
| A/G                | 0                        |
| 2                  | d                        |
| 15                 |                          |
|                    |                          |
| 21                 |                          |
| 0                  |                          |
| 3                  | d                        |
| 8                  |                          |
|                    |                          |
| 14                 |                          |
| 0                  |                          |
| Destination        |                          |
| Address            |                          |
| Field              |                          |
| 4                  | d                        |
| 1                  |                          |
|                    |                          |
| 7                  |                          |
| 0                  |                          |
| 5                  | s                        |
| 22                 |                          |
| s                  |                          |
| 23                 |                          |
| s                  |                          |
| 24                 |                          |
| s                  |                          |
| 25                 |                          |
| S                  |                          |
| 26                 |                          |
| s                  |                          |
| 27                 |                          |
| C/R                | 0                        |
| 6                  | s                        |
| 15                 |                          |
|                    |                          |
| 21                 |                          |
| 0                  |                          |
| 7                  | s                        |
| 8                  |                          |
|                    |                          |
| 14                 |                          |
| 0                  |                          |
| Source             |                          |
| Address            |                          |
| Field              |                          |
| 8                  | s                        |
| 1                  |                          |
|                    |                          |
| 7                  |                          |
| 1                  |                          |
| Link Control Field | 9                        |
| Information        |                          |
| Field              |                          |
| N-2                | FIS-B                    |
| A P D U            |                          |
| N-1                | fcs                      |
| 9                  |                          |
|                    |                          |
| 16                 |                          |
| Frame Check        |                          |
| Sequence           |                          |
| N                  | fcs                      |
| 1                  |                          |
|                    |                          |
| 8                  |                          |
| Flag               | N+1                      |

 
Note:  ISO 3309 states that a transmitter may include more than one frame in a single physical layer transmission, with a single flag separating each frame. 

## F.1.1 Flag

Flag is a unique HDLC bit sequence to delimit the start and end of each APDU 
transported by the data link layer.  FIS-B frames shall be delimited by this unique sequence of bits by setting the Flag octet to '01111110' binary. 

## F.1.2 Destination Address Field

The Destination Address Field is a 28-bit field comprised of a 24-bit Aircraft Specific Address field (d1 through d24), a 3-bit Address Type field (d25 through d27), and a 1-bit Air/Ground (A/G) Transmitter field.  The nominal broadcast destination address encoding is taken from Table 6-8, Broadcast Address Encoding, of the VDL Mode 2 SARPs.  The nominal broadcast destination is all aircraft and assumes all ones in the specific destination address field.  In the future, use of aircraft specific destination addressing (unicast) within the specific destination address field is not precluded. 

## F.1.2.1 Aircraft Specific Address

This 24-bit address (d1 through d24) shall be set to all ones (1s) for FIS-B frames to denote a broadcast destination address as encoded in Table 6-8 of the VDL Mode 2 SARPs.  Future implementations will support aircraft specific addressing (unicast) 
utilizing 24-bit aircraft addressing. 

## F.1.2.2 Address Type

This 3-bit type field (d25 through d27) shall be set to '100' binary to signify "ALL 
AIRCRAFT" type.  It is expected that this destination type field will remain constant for all broadcast UI frames.  Future implementations will support an appropriate address type field for aircraft specific addressing.  

## F.1.2.3 A/G Transmitter

This bit represents the location of the transmitting station as being either airborne or on the ground, as defined is Section 6.5.3.3.3.1 of the VDL Mode 2 SARPs.  This bit shall be set to '1' for FIS-B, since the transmitting station is on the ground. 

## F.1.3 Source Address Field

The Source Address Field is a 28-bit field comprised of a 24-bit Ground Specific Address field (s1 through s24), a 3-bit Address Type field (s25 through s27), and a 1-bit Command/Response (C/R) bit.  This address field is described in detail in the Section 
6.5.3.3.3 through Section 6.5.3.3.3.7 in the VDL Mode 2 SARPs. 

## F.1.3.1 Broadcast Source Address

This 24-bit address (s1 through s24) shall be the ICAO delegated ground address. 

## F.1.3.2 Address Type

This 3-bit type field (s25 through s27) shall be set to '101' binary to signify "ICAO 
DELEGATED ADDRESS" type.  Its encoding is taken from Table 6-7, Address Type Field Encoding, of the VDL Mode 2 SARPs.  It is expected that this field will change depending on the source of the broadcast UI frames. 

## F.1.3.3 C/R Bit

The Command-Response (C/R) bit shall be set to '0' to indicate that the UI frame is a command.  The C/R bit is described in Section 6.5.3.3.3.2 of the VDL Mode 2 SARPs. 

## F.1.4 Link Control Field

This field indicates the purpose of the frame.  It shall be set to '00000011' binary to represent the UI command as detailed in Section 7.3 of ISO 4335.  This binary setting includes the Poll/Final (P/F) bit, which is described in Section 6.5.3.7 of the VDL Mode 
2 SARPs and Section 6.2.3 of ISO 4335.  All commands, other than the UI command require a response.  The AVLC commands and responses are detailed in Table 6-9 of the VDL Mode 2 SARPs. 

## F.1.5 Information Field

This field shall be used to transfer FIS-B APDUs.  The requirements for the information field are given in the FIS-B ASE format specification. 

## F.1.6 Frame Check Sequence

FIS-B shall contain a 16-bit frame checking sequence as described in ISO 3309, Section 4.6 and Annex A. 

## F.2 Universal Access Transceiver (Uat) Data Link Services

The UAT datalink is specifically designed to support only connectionless data communication.  Therefore, the data link service (DLS) for UAT implementations of FIS- B has a more limited set of minimum requirements than is described in Section 3.4 of this document (ISO 3309).   
The following material serves to set minimum requirements for the DLS functionality for FIS-B services over the UAT datalink.  In the UAT architecture, there is no requirement to employ the same DLS formats between the local segments (i.e., the links marked "B" 
and "C" of Figure 1-1) and the DLS used on the RF segment (i.e., shown as "Step 4" on Figure 1-1).  Therefore DLS requirements are discussed separately for each segment. 

## F.2.1 Rf Segment

The UAT datalink RF segment allows for multiple types of Information Frames to support various applications.  FIS-B is one of the intended applications.  All of the initial applications of FIS-B over UAT require only the most rudimentary of data link services. As other applications are developed that have more sophisticated data link service requirements, they can be easily be incorporated by defining Information Frame formats for those purposes.  The frame structure and formats are documented in RTCA DO- 282A.   

Note: 
In the UAT system, Information Frames are conveyed by UAT Ground Uplink 
messages.  In addition to Information Frames, a UAT Ground Uplink message 
will include a UAT-specific header (See RTCA DO-282A). 
Specific functional requirements of the DLS for the RF segment are listed below: 

## F.2.1.1 Data Transparency

The UAT data link service shall provide for data transparency (e.g., the communication of arbitrary binary frame data).   
Note: 
UAT employs a length indicator field as opposed to employing delimiter "flags" 
as described in Section 3.4.3 

## F.2.1.2 Addressing

The UAT data link service shall provide the Source Address subfield, if required by the specific FIS-B service being provided.  The initial applications of FIS-B service do not require the Source Address subfield. 

Since the UAT datalink is intended for connectionless broadcasts only, there is no requirement for a Destination Address subfield. 

## F.2.1.3 Integrity Of Frame Data

Integrity at least equivalent to the FCS field as described in Section 3.4.7 shall be provided. 

Note: Integrity of frame data is verified as prescribed in RTCA DO-282A. 

## F.2.2 Local Segments

Local segments may employ DLS frame formats and protocols different from that used over the RF segment if it provides performance consistent with the requirements of F.2.1 
above. 

Note: 
RTCA DO-282A contains requirements for "report generation" on receipt of 
each message containing FIS Information Frames.  The report format includes additional overhead that helps distinguish FIS information from surveillance information and includes a precise time of message reception. 
 

## Test Data Set Description

This page intentionally left blank. 

## Appendix G Test Data Set Description

This section provides recommendations for test data sets for the purpose of manufacturer or applicant system test and verification.  The data sets should consist of normal text data and graphical data, as well as variants containing errors.  The text data sets should consist of three parts: (1) original text report(s), 
(2) source text data binary stream, and (3) data in FIS-B frame format carrying the APDU.  The graphical test data sets should also consist of three parts: (1) original image (picture), (2) source graphical data binary stream and (3) data in FIS-B frame format carrying the APDU.  The original data (text or image) will be used for a detailed comparison with the text (or image) reassembled from the APDUs to verify there are no unacceptable aspects of the displayed output, such as incorrect colors, mirror images, missing or added data when the product was correctly received, etc. 

Note: 
Data sets containing proprietary encoding should make provision for decoding by any regulatory authority examining the data for approval. 

Construction of the FIS-B frame format carrying the APDU Header and APDU Payload should be generally compliant with the recommendations of this document. Each data set will be used to demonstrate at least one pass/fail criteria.  There will not be data sets without pass/fail criteria or pass/fail criteria without data sets. 

## G.1 Text Data Set

METAR data sets.  General characteristics: A total of 30 textual reports (15 METAR and 15 SPECI) as a minimum. 

## G.1.1 Unaltered Data Set

A representative unaltered METAR/SPECI set.  The intent of this data set is a baseline verification of FIS-B text product processing capability.  Error conditions have not been addressed in this set.  Multiple products should be used in preparation of this set to force product segmentation and thus multiple linked APDUs. The data set provided should separately includes all FIS-B "long" link layer format, "short" link layer format and APDU overhead, as they would be received by the avionics.  
Different encoding will be necessary for the "short" link layer format.  No physical layer encoding is necessary. Properly functioning avionics should be capable of data recovery, decode, and reassembly of linked APDUs following transmission.  A byte level comparison should reveal a one-to-one match of transmitted to recovered data. 

## G.1.2 Altered Data Set

METAR test set with one header altered following computation of the Frame Check Sequence (corrupted APDU).  The intent of this data set is to verify that data with errors are discarded. 

## G.2 Graphical Text Pattern

Graphical test pattern (NEXRAD image).  General characteristics: Graphical image with 4-level (4 colors) minimum and a mosaic (composed of more than one radar sites' image data). 

## G.2.1 Unaltered Image

A representative, unaltered NEXRAD image.  The intent of this data set is a baseline verification of FIS-B graphical processing capability.  Error conditions have not been addressed in this set.  A NEXRAD mosaic image should be used in preparation of this set to force product segmentation and thus multiple linked APDUs.  

## G.2.2 Missing Data

NEXRAD image with at least one radar sites' data missing.  The intent of this data set is to verify that the processing function correctly deals with a missing radar site image data. 

## G.2.3 Altered Data Set

NEXRAD image with one header altered following computation of the Frame Check Sequence (corrupted APDU).  The intent of this data set is to verify that the resultant missing data (rejected APDU) are properly identified and located on the image, or the entire image is rejected as appropriate, dependent upon system processing. 

## Appendix H Radar Color Consistency

This page intentionally left blank. 

## Appendix H Radar Color Consistency

This appendix provides background on ground-based and airborne weather radar systems.  It was developed by Special Committee 195, Working Group 1 and was used in determining the recommended color presentations for display of FIS precipitation products based on NEXRAD data as listed in Table 3-
2, Section 3.8.2. 

H.1 
Color Consistency Between Ground-based and Airborne Weather Radars There is a desire to achieve consistency in color assignment between NEXRAD  (WSR- 88D), airborne weather radars, and air traffic control weather radars (ASR-9).  Currently the output of these radars is described by varying schemes.  In this paper we will review a little of how weather radars produce their output image indicating received signal strength, which indirectly indicates precipitation rate.  We will look at the differences in propagation and reflectivity in the three spectrum bands used by weather radars, and also consider differences in environment.  We will look at the differences in quantization schemes. 

## H.2 Radar Basics

RADARs (radio detection and ranging) transmit a burst of energy in a pulse of short duration, typically 1.6 microseconds for NEXRAD radar.  The antenna focuses the energy into a slender conical beam whose beamwidth varies with the frequency of the transmitted radiation and the size of the antenna.  At the end of the transmitted pulse, the radar switches into receiving mode to "listen" to returned energy.  Targets intercepting the radar beam (precipitation and other objects) cause scattering of the beam, some of which is backscattered (reflected back) to the radar.  The returned signal is amplified, processed, colorized, and displayed on a screen.  At the end of the "listening period", the radar transmits another pulse and the process is repeated. The radar equation for a discrete target with backscatter cross section b
σ  is: 

$$P_{r}=P_{t}G^{2}\lambda^{2}l^{2}\sigma_{b}f^{4}(\theta,\varphi)/\bigl(4\pi\bigr)^{3}R^{4}$$
Where r P  is the received power for one pulse 

 
Pt is transmitted power in one pulse 
 
G is antenna gain  (relative to isotropic) along the beam axis 
 
λ is wavelength of the radar energy 
 
l is the one-way path loss due to attenuation  (absorption and forward scattering) 
 
f2(ϕ,θ) is the normalized  antenna power gain pattern 
 
R is the range to the target 
The receiving and transmitting antennas are assumed to be the same.  From this equation, one can work backwards to determine b
σ , the scattering cross section of the target.  The backscatter cross section of a volume of targets can be related to the rainfall rate, so we can create an image that estimates the amount of rain occurring in specific volumes as a function of range, bearing, and tilt from the aircraft.   
There are many known constants in the equation, such as the transmitted power in each pulse, and the gain of the antenna pattern (which can be measured).  Wavelength is a known constant, and we can measure range to the target based on the time it took for the echo to return to the radar.  (See discussion of range-normalization.) The unknowns in the equation, then, are the path losses, the scattering cross section, and the extent to which the target fills the antenna beam.  There are other unknowns arising from non-ideal conditions such as the presence of side lobes, the absorption & scattering in the radome, anomalous propagation, etc. The beamwidth partially determines the spatial resolution of the radar.  The other dimension of the pulse volume is determined by the pulse width.  The sampling volume of a "pencil-beam" radar is a portion of a spherical shell, θ degrees across and one pulsewidth thick.  If it's an X-band radar with a 3-degree antenna beamwidth, the beam is approximately 0.5 NM (3000 ft) across at 10 NM from the radar, and widens at the same rate (about a 19:1 ratio).  So 100 NM away from the radar, the smallest resolution element is about 5 NM in diameter, and 200 miles away the beam subtends an area approximately 10 NM across.  The thickness of the spherical shell is determined by the pulsewidth.  For NEXRAD radar the pulse width is 1.6 microsecond, therefore the sampling volume is about 1600 ft thick. Within that sampling volume, target returns are averaged together, and individual target characteristics cannot be distinguished.  A small, highly reflective target may return the same amount of energy as a large, less reflective target, so they would appear the same. 

## H.3 Range-Normalization

Because the pulse volume expands as it moves away from the radar, the energy per unit volume decreases.  Thus, the strength of the returned signal is typically weaker from distant targets than from nearby ones.  The returned signal is, therefore, range-normalized to eliminate this effect.  The range-normalized returned signal strength is then converted to an equivalent radar reflectivity factor, or "reflectivity," Z. Returned signal strength relates to the size, type, and concentration (number per unit volume within the pulse volume) of targets within the pulse volume.  Types of targets include, liquid drops (rain, drizzle, cloud drops), ice (crystals and hail), ice coated with water, insects, birds, aircraft, skyscrapers, mountains, motor vehicles (usually affecting only the lowest elevation angle scan), etc., with different scattering "efficiencies."  The skyscrapers, mountains, and other non-meteorological targets represent "clutter", with those attached to the surface typically called ground clutter.  Only one measurement of total returned power is obtained per pulse volume, representing the combined effects of all targets.  Because there are three factors that affect the returned power, and only one measured value, it is not possible to unambiguously estimate precipitation rate from radar reflectivity values. 7  
A fair amount of ground clutter can be differentiated from other returns on the basis of its Doppler shift, or in the case of fixed ground-based radar like NEXRAD, by its constancy. 

## H.4 Spectrum

The electromagnetic spectrum has alphabetic labels applied to certain microwave regions. Weather radars operate in S, C, or X bands.  These are defined as: 

| S band     | 2– 4       |
|------------|------------|
| C band     | 4 - 8  GHz |
| X band     | 8-12.5 GHz |

Airborne radars are usually X-band radars, with wavelengths of 3.2 cm.  The antenna power gain pattern is limited by the size of the antenna and is typically a slender, diverging beam of 3 degrees for an air-transport size (28-inch) antenna. There are some airborne C-band radars with wavelength = 5 cm.  For an antenna of the same size (28 inches), the beamwidth is 4.7 degrees. NEXRAD radars (WSR-88D radars) are S-band radars, with wavelengths of about 10 cm.  
Their large antenna allows them to focus radiation into a narrower beam about 1 degree wide.   
The ASR-9 radars are fan-beam radars, not pencil-beam radars.  The fan beam extends vertically, and they are scanned horizontally. 

## H.5 Backscatter

Reflection of radar energy from a volume filled with raindrops is approximated by the backscatter cross section of that volume.  The backscatter cross section of a single water drop, assuming its diameter is small compared to wavelength  (i.e., diameter less than 2 mm for X-band, 6 mm for NEXRAD), is  

$$\sigma_{b}=\left(\pi^{5}/\lambda^{4}\right)\!\!\left|K_{w}\right|^{2}D^{6}$$
This is called the Rayleigh approximation, and holds for small scatterers, D < λ/16.  
Basically it says that for a given spectral band, backscatter is proportional to the sixth power of the diameter of the raindrop.  
2
W
K
, a magnitude related to the complex refractive index of water, is about 0.92 for the wavelengths of interest, and is pretty much independent of temperature so long as the droplet is still water.  For ice spheres, 
2
W
K
 is 
0.18, much less reflective than similar sized water droplet, and is also independent of temperature and wavelength, so long as the droplet stays frozen. 

Note:  At shorter wavelengths, like X band, the scattering is much stronger. 

## H.6 Losses Due To Attenuation

Rain attenuates the radar energy by scattering energy away from the receiver and by absorbing some of the radar energy.  The amount of attenuation depends on temperature, the rainfall rate, and the wavelength of the radar used.  Figure H-1 (from Doviak and Zrnic)8 shows the attenuation of radar energy due to rainfall rate  (the ordinate is expressed as dB/km).  This plot is defined for a temperature of 18° C.  The temperature adjustment factor for S-band radars is C(T) = 2 exp(0.035T).  For shorter wavelength radars the temperature correction factor is dependent on rainfall rate. 

 
We can observe from this plot that attenuation increases exponentially with rainfall rate, and the attenuation is less with longer wavelength radars.  In fact, at 50dBZ, the rate of 
(one-way) attenuation is approximately 0.01 dB/km at λ =10cm, 0.1 dB/km at λ =5 cm, and 1 dB/km at   λ = 3.2 cm.  This explains why weather radars trade off resolution for storm penetration.  (Shorter wavelengths provide better resolution (smaller beamwidth) for a given antenna size, but the energy is lost at a much higher rate.)  At fairly high rainfall rates, S-band radars have one hundred times less attenuation than most airborne radars (and usually higher transmitted powers, as well). Cloud droplets can absorb a significant amount of energy.  These droplets can be very small (diameters less than 100 microns) and they do not always backscatter enough energy to be detected, but they still absorb energy.  If the droplets are very small then absorption depends on the amount of liquid water in the cloud volume  (measured in g/m3).  This attenuation will result in underestimates of rain in distant storms viewed though clouds.  The underestimate cannot be corrected because it is undetectable.  For a radar with  λ  = 10 cm, the attenuation might be 0.9 dB for 2-way propagation through 50 
km of clouds with 1g/m3 of liquid water along the path.   

## H.7 What Is A Dbz?

In the discussion above, σb is the backscatter value for one drop.  Weather radars encounter a wide distribution of droplet sizes within a very large pulse volume.  The summation of all the backscatters within the volume, normalized per unit volume, is the averaged reflectivity of that volume, written as η instead of σb . 

For short wavelength radars measuring thunderstorm precipitation, the size of the raindrops relative to wavelength often falls outside of the Rayleigh region D< λ/16.  So it is common to write 

$$\eta=\left(\pi^{5}/\lambda^{4}\right)K_{W}\left|^{2}Z_{e}\right.\ \ \mathrm{instead\of}\ \ \eta=\left(\pi^{5}/\lambda^{4}\right)K_{W}\left|^{2}\frac{1}{\Delta V}\sum_{i}D_{i}^{6}\right.$$
where Ze is the effective reflectivity in units of mm6/mm3 .  (Recall that reflectivity is proportional to the sixth power of raindrop diameter in mm, volume in cubic millimeters.)  Recall also that Kw varies by less than 2% with temperature and wavelength, but does depend strongly on whether precipitation is frozen or liquid.  This expression is found to be adequate where radar frequency is below 10 GHz. 

Because the values of Ze commonly encountered span many orders of magnitude, radar meteorologists use a log scale, where dBZ is defined as 10 log10 Ze.  Precipitation in regions of heavy rainfall and hail can exceed 60 dBZ. A reflectivity of 50 dBZ represents a range-normalized returned signal 1000 times stronger than one with a reflectivity of 20 dBZ.  The reflectivity is then used to estimate precipitation rate.9 
There is another form of the radar equation for the volume scatters, in which average received power is proportional to Ze .  The form of this equation is given below.  For derivation, see Doviak and Zrnic, p 5810 

$$\overline{{{P}}}=\frac{\pi^{5}10^{-17}\,P G^{2}l^{2}l_{r}\tau\theta_{1}^{2}\big|K_{w}\big|^{2}Z_{e}}{6.75x2^{14}\big(\ln2\big)R^{2}\lambda^{2}}$$
 
In this form, P  is in mW, θ is in degrees, Ze is in mm6/mm3 , τ (the pulsewidth) is in microseconds, transmitted power Pt is in Watts, R is in km, and  λ is in cm. 

## H.8 What Is The Relationship Between Dbz And Rainfall Rate?

The exact relationship between reflectivity Z and rainfall rate R depends on the drop-size distribution within the sampling volume.  Marshall and Palmer11 developed the most commonly used expression: 

$$Z=200R^{1.6}$$
where Z is the volume reflectivity Ze  in mm 6/mm3, and  R the rainfall rate, is in mm/hr.  
When characterizing snow, there are three expressions for Z as a function of R, depending on whether the snow is single crystals or aggregate snowflakes, or a generalpurpose snow.  The average expression for all snow is: 

$$Z=1000R^{1.6}$$
where R is millimeters of water per hour  (not mm of snow).  Note that this volume backscattering coefficient is about 5 times larger than the one given above for rain; 
however recall that Kw for ice is ¼ of Kw for liquid water.  So the two factors approximately cancel out, and the volume backscattering coefficient of dry snow is approximately equal to that of rain for the same precipitation (in water) rate.  Note that the range of snow precipitation rates is lower than that for rain because snowflakes fall at a much lower velocity than raindrops. 

## H.9 Current Quantization Standards

A/C 25-11 lists the quantization standards for airborne radar returns and the colors that should be applied; see Table H-1: 

| Reflectivity in dBZ    | Rainfall rate    | Color         |
|------------------------|------------------|---------------|
| 0-20                   |                  | Black  (none) |
| 20 - 30                | 1-4 mm/hr        | Green         |
| 30-40                  | 4-12 mm/hr       | Yellow        |
| 40-50                  | 12-50 mm/hr      | Red           |
| 50 +                   | >50 mm/hr        | Magenta       |
| Red                    |                  |               |

 
Pilots receive advice from ATC terminal area controllers regarding storm activity on the basis of ASR-9 radars, which report intensities based on VIP level (video integrator processor).  En-route controllers use different terminology, namely:   

 
 
Light to moderate 
30-41 dBZ 
(corresponds to VIP 2) 
 
Moderate to heavy 
41-50 dBZ 
(corresponds to VIP 3 & 4) 
 
Heavy to extreme 
>50 dBZ 
(corresponds to VIP 5&6) 
VIP level 
Gray shade14 
Echo Intensity 
dBZ15 
Rainfall rate 
stratiform16 
Rainfall rate 
convective17 
1 
Gray 
Weak 
<30 
< 2.54mm/hr 
< 0.1 in/hr 
< 5 mm/hr 
< 0.2 in/hr 
2 
White 
Moderate 
30-41 
2.54 - 12.7 mm/hr 
0.1 - 0.5  in/hr 
5.0 - 28 mm/hr 0.2 - 1.1 in/hr 
3 
Black 
Strong 
41-46 
12.7-25.4 mm/hr 
0.5-1.0  in/hr 
28 - 56 mm/hr 1.1 - 2.2 in/hr 
4 
Gray 
very strong 
46-50 
 
56 - 114 mm/hr 
2.2-4.5  in/hr 
5 
White 
Intense 
50-57 
 
114 - 180 mm/hr 
4.5-7.1  in/hr 
6 
Black 
Extreme 
>57 
 
>180 mm/hr 
>7.1 in/hr 

 
NEXRAD (WSR-88D) is reported either in 16 levels of 5 dBZ each (from less than 5 
dBZ to greater than 75 dBZ) or as VIP levels.  Table H-2 indicates the dBZ returns associated with various forms of precipitation. 

| dBZ                | WSR-88D Standard   |
|--------------------|--------------------|
| 19                 |                    |
|                    | Stratiform         |
| precipitation      |                    |
| 20                 |                    |
|                    |                    |
| Convective         |                    |
| precipitation      |                    |
| 21                 |                    |
|                    |                    |
| Snow               |                    |
| 22                 |                    |
|                    |                    |
| <15                | <0.20 mm/hr        |
| <0.008 "/hr        |                    |
| <0.31 mm/hr        |                    |
| <0.01 "/hr         |                    |
| 0.15 mm/hr         |                    |
| < 0.006 "/hr       |                    |
| < 0.12 mm/hr       |                    |
| < 0.005 "/hr       |                    |
| 15 - 30            | 0.20 - 2.36 mm/hr  |
| 0.008- 0.09''/hr   |                    |
| 0.32 - 2.73        |                    |
| 0.01 - 0.10        |                    |
| 0.16 - 1.58        |                    |
| 0.006- 0.06        |                    |
| 0.13 - 0.70        |                    |
| 0.005- 0.02        |                    |
| 30 - 40            | 2.36 - 12.23 mm/hr |
| 0.09 -  0.48       |                    |
| 2.73 - 11.53       |                    |
| 0.11 -  0.45       |                    |
| 1.59 - 7.36        |                    |
| 0.06 - 0.29        |                    |
| 0.71 - 2.23        |                    |
| 0.03 - 0.08        |                    |
| 40- 45             | 12.24- 27.85       |
| 0.48 - 1.09        |                    |
| 11.53- 23.67       |                    |
| 0.45 - 0.93        |                    |
| 7.37- 15.87        |                    |
| 0.29-  0.62        |                    |
| 2.24- 3.97         |                    |
| 0.09 - 0.15        |                    |
| 45 - 50            | 27.86- 63.39       |
| 1.10 - 2.49        |                    |
| 23.68- 48.62       |                    |
| 0.93 - 1.91        |                    |
| 15.87- 34.19       |                    |
| 0.63 - 1.34        |                    |
| 3.98 - 7.07        |                    |
| 0.16 - 0.27        |                    |
| 50 - 55            | 63.40-144.27       |
| 2.50 - 5.68        |                    |
| 48.62- 99.85       |                    |
| 1.91 - 3.93        |                    |
| 34.20- 73.68       |                    |
| 1.35 - 2.90        |                    |
| 7.07- 12.57        |                    |
| 0.28 - 0.49        |                    |
| 55 or more >144.28 |                    |
| >5.68              |                    |
| >99.85             |                    |
| >3.93              |                    |
| >73.68             |                    |
| >2.9               |                    |
| >12.57             |                    |
| >0.50              |                    |

 
 
12 Bob Grappel, Lincoln Labs, personal communication, Nov 1999. 13 NWS Training Manual for Radar Specialists, presented by Archie Trammel, supplemental information to course 
22 Sept 99. 

14 Refers to PPI display.  White and black are reversed on WBRR displays. 

Table H-3 compares the VIP levels to the 16-level NEXRAD and the airborne weather radar levels. 

Table H-4 is the result of a comparison of WSR 57/74 radar values to NEXRAD 
returns.23 

NWS "VIP Level" 
WSR- 57S/74C (dBZ) 
WSR-88D (NEXRAD) Level 
NEXRAD Precip mode (dBZ) 
Airborne Radar Intensity (dBZ) 
Airborne Radar Display Color 
0 
< 10 
0 - 2 
0 - 15 
 
 
1 
~ 18*-30 3 - 5 
15 - 30 
 20-30 
 Green 
2 
30 - 41 
6 - 7 
30 - 40 
 30-40 
 Yellow 
3 
41 - 46 
8 
40 - 45 
>40 
 Red 
4 
46 - 50 
9 
45 - 50 
>40  
 Red 
5 
50 - 56 
10 
50 - 55 
>50  
Red 
or 
magenta 
6 
>= 57 
11 
55 - 60 
>50  
Red 
or 
magenta 
 
 
12 
60 - 65 


13 
65 - 70 


14 
70 - 75 


15 
>= 75 

 
Note:  The lower threshold for Level 1 on WSR 57/74 radars is variable, depending on analog threshold setting and target proximity. 

## H.10 Observed Data

Evidence indicates that ASR-9, WSR-57, and WSR-88D returns are consistent on the ground.  A comparison of X-band or C-band airborne radar to WSR-88D is not currently available.  Given the spectral differences, the antenna lobe differences, and the differences in backscattering models and attenuation just discussed, however, it's not clear that a storm that measures 20 dBZ on a NEXRAD would also measure at 20 dBZ on an X-band radar. There is also a difference in the field of regard of the two radars.  We should not expect airborne weather radar to show exactly the same precipitation pattern as the ground-based radar.  The NEXRAD images being uplinked are base reflectivity images for the most part, taken from the lowest scan angle.  Airborne weather radars may be flying at 30,000 ft and their radar beam scans a completely different part of the storm.  Base reflectivity NEXRAD (assuming 1.5 degree max elevation, 230 Km range) scans a volume whose vertical extent ends a little less than 30,000 ft. above the elevation of the radar site, but for the first 100 Km the vertical extent of the scanned volume is below 10,000 ft. The aircraft radar operates in a significantly different temperature environment, in a different spectral band, with much higher losses.  The plane of the radar beam may be looking at frozen precipitation within the cloud.  Or the plane may be looking at the early stages of a very severe storm, in which heavy concentrations of hydrometeors are present in the cloud at high altitudes, but no precipitation has fallen to the ground yet. 

## H.11 Operational Considerations

What are the important operational considerations?  We are trying to portray storms in a manner that will encourage avoidance of dangerous conditions, not provide guidance for penetration. It would be prudent to establish levels that have a service history, and that pilots are accustomed to.  The VIP levels have a very long history, and many general aviation pilots have a sense of the hazard posed by VIP levels already.  For example, a pilot may feel comfortable flying into VIP level 1, and may or may not fly into VIP level 2 precipitation.  This implies that uplinked weather would gain more immediate acceptance if its color codes reflected the current VIP levels in some way, and that the color codes should clearly distinguish VIP level 1, 2, and 3. 

Air transport pilots have known for years that their weather radars do not exactly match the VIP levels.  However, given the radically different nature of the two radars and the operating environment in which they are used, "consistency" is perhaps a theoretical goal.  Knowing that the X-band radars suffer from higher path loss, it would seem ill advised to de-rate their color scale so that 30 - 40 dBZ would be colored as green. About 20 years ago, United Airlines asked for their C-band radar color assignments to be changed so that 30-40 was green, 40 - 50 was yellow, and 50+ was red.  This resulted in flights passing through severe convective activity.  In the end, the colors were changed back to the A/C 25-11 standard, but not before the pilot's union was involved. The W.J. Hughes Technical Center advised that the colors used for NEXRAD color coding (also, ITWS, OASIS, etc.) found in FCMH11c-1991 were generated by Unisys as default values and DO NOT constitute a standard.  In daily practice, that color mapping is often altered by meteorologists to suit their preferences. 

## H.12 Conclusions & Recommendations

It should be clear that measuring rainfall with radar is not an exact science but rather an exercise in mathematical modeling.  The same radar color can mean different atmospheric conditions.  (Latitude alone can play an important role in interpretation.) The general aviation user community already has a standard in place with a long service history, the VIP levels.  The community should strive for color levels that meaningfully indicate hazard to the user community.  Assuming that NEXRAD radar returns do indeed correlate well with the radar returns used as the basis for VIP levels, the NEXRAD 
quantizations already fall into the VIP levels fairly directly, as shown in Table H-4 
columns 2 & 4.  (After the discussion above, the community should not demur over a 1-2 
dBZ discrepancy.)  
VIP level 1 is trace precipitation, but is still shown on weather radars for several reasons.  
One important reason is that in freezing conditions, VIP level 1 precipitation may be freezing rain, an aviation hazard.  Another reason for displaying level 1 precipitation is that some patterns in the low-intensity returns can indicate hail or turbulence (e.g., hooks, fingers, scalloped edges). 

VIP level 2 may indicate thunderstorm activity, and is treated with caution by pilots, so it is reasonable to assign a cautionary color such as yellow to it. VIP level 4 is mentioned in the Aeronautical Information Manual (AIM) as an indicator of severe thunderstorm activity.  In the current standards it is subsumed into the red level  
(40-50 dBZ) but it might optionally be shown as a darker shade of red. 

Table H-5 shows the recommended colors, including optional colors, discussed by the working group.  Note that these are similar to A/C 25-11 colors, and the assignment of yellow is 5 dBZ more conservative than NEXRAD.  The assignment of red is 10 dBZ more conservative than NEXRAD.  VIP level 4 may optionally be displayed as dark red. It is worth noting that on many weather radars, green, yellow, and red are all dark green, dark yellow, and dark red, but there is no ambiguity, as these displays do not display more than 4 levels of weather.  
Table H-5 shows the correspondence of VIP dBZ levels (column 2) to the 16-level NEXRAD intensities (column 8).  There is no more than one or two dB of difference between the boundaries of the VIP levels and the 5 dBZ bounds of the 16-level NEXRAD.  This is little enough difference that it can be ignored.  VIP level four can be shown in dark red. 

NWS "VIP 
Radar 
Recommended 
Optional 
Airborne 
Airborne 
NEXRAD 
NEXRAD 
WSR-88D 
Level" 
Intensity 
Display 
colors24 
Radar 
Radar 
Precip 
Display 
(NEXRAD) 
(dBZ) 
Color24 
Intensity 
Display 
mode 
Color 
16- Level 
Recommended 
controller 
description 
(dBZ) 
Color 
(dBZ) 
0 
<20 
None 
 
<20 
None 
 
0 - 15 
Blue 
0 - 2 
0 
<20 
None 
 
<20 
None 
"Light" 
15 - 20 
Lt. Grn 
3 
1 
20-30 
Green 
 
20-30 
Green 
"Light" 
20 - 30 
Med Grn 
4-5 
2 
>30-40 
Yellow 
 
30-40 
Yellow
"Moderate" 
30 - 40 
Drk. Grn 
6-7 
3 
>40-45 
Red 
 
40-45 
Red 
"Heavy" 
40 - 45 
Amber 
8 
High-
4 
>45 - 50 
Red 
45-50 
Red 
"Heavy 4" 
45 - 50 
Orange 
9 
contrast 
Red 
5 
>50 - 54 
Red 
Magenta
50-55 
Red or 
Magenta
"Heavy 5" 
50 - 55 
Lt. Red 
10 
Magenta 
or High-
>55 
Red or 
6 
≥55 
Red 
Magenta
"Heavy 6" 
55 - 60 
Red 
11 
contrast 
Magenta


≥60 
Red 
White 
60 - 65 
Drk. Red 
12 


65 - 70 
Magenta 
13 
70 - 75 
Purple 
14 
>= 75 
White 
15 

 
The discrepancy between ground-based radar seen by controllers and flight service station specialists and airborne radar might best be handled by appropriate terminology on the part of the controllers.  Dr. Ray McAdaragh, an FAA Human Factors/Weather official, noted that controllers or flight service station specialists should never describe the weather by the colors on their screen.  Instead, he has promoted the idea that they can describe VIP levels (if they know them), or use standard (recommended) descriptors such as those listed in Table H-5 above (Recommended controller description): 
These standards (Recommended controller description) were developed through an FAA 
sponsored User Needs Analysis (UNA).  The UNA was based on operational information provided by representatives from organizations such as Allied Pilots Association and the Aircraft Owners and Pilots Association.  For example, airliners do not generally operate in areas with precipitation levels greater than 40 dBZ, and general aviation pilots do not generally operate in areas with precipitation levels above 30 dBZ.  The FAA UNA team came to consensus on the fact that there are basically three relevant ranges of dBZ levels: Light (10-30 dBZ), Moderate (>30-40 dBZ), and Heavy (>40 dBZ).  For further definition, the team also agreed that Automated Flight Service Stations (i.e, Flight Watch), National Weather Service, and dispatchers (not ATC) could issue sub-levels of the Heavy range.  The breakpoints for the Heavy dBZ range sub-levels were determined to be Heavy 4 (>45-50 dBZ), Heavy 5 (>50-55 dBZ) and Heavy 6 (>55 dBZ). In summary, the Recommended controller descriptions are: 
Light:  
>10 dBZ to <30 dBZ 
Moderate: 
>30 dBZ to <40 dBZ 
Heavy:  
>40 dBZ 
Heavy sub-levels: Heavy 4: 
>45 dBZ to <50 dBZ 
Heavy 5: 
>50 dBZ to <55 dBZ 
Heavy 6: 
>55 dBZ 
 
This page intentionally left blank.

## Appendix I Display Of Layered Graphics And Text (Normative)

This page intentionally left blank.

## Appendix I Display Of Layered Graphics And Text (Normative)

This appendix provides background information on concepts and issues impacting cockpit displays that integrate various categories of information to include FIS data link products as covered by this MASPS.  
It was developed by Special Committee 195, Working Group 1 and was used in determining the recommendations for "Integrated display formats combining layers of FIS graphics and Text," as listed in Section 3.8.3. Displays for flight information services can take many forms, depending on the stage of evolution, options provided by the vendor, equipage, degree of integration with and capabilities of installed flight management systems, and the availability of information.  Most importantly, specifications on the layering of diverse categories of cockpit information shall take into account the criticality of each category and/or severity level of information considering the particular circumstances of the current phase of flight, and cockpit design philosophy.  This appendix does not attempt to provide *specific* guidance on layering of categories of cockpit information that can be applied in all situations.  Instead, this appendix offers general design considerations for vendor displays that should guide the certification process for the initial FIS-B offerings.  As the industry gains experience in integrating the new FIS information categories described in this MASPS, this guidance can be expanded to include specifications as they evolve and as the vendors add more capabilities during the phased introduction of FIS products and display functionality. We can expect the following categories of information on cockpit displays; the non-FIS information is governed by other regulatory documents and normally takes precedence over FIS data link information which is advisory as described in Section 1: 
Non-FIS Information: 
a. Cockpit Display of Traffic Information (CDTI), graphical and textual. 

b. Terrain and obstacle depiction and ground proximity warning/alerting, graphical and 
textual. 
c. Decision support, graphical and textual. 
FIS Information 
a. Weather information, graphical and textual. 
b. Other NAS status information such as NOTAMs, graphical and textual. 
In addition, we can expect the above informational products to be overlaid on a graphical depiction of the current flight profile and navigation situation, either on a north-up, moving map display or a track-up, horizontal situation display, both including varying levels of graphical information for geo-reference. Clearly, the cockpit display has the potential for a high degree of clutter, especially in critical flight situations where terrain, traffic, precise navigation, and weather are all factors at the same time and require the pilot's attention for safe continued flight.  The question becomes which categories or levels of severity of information deserve priority over others in the current flight situation.  The answer to this question drives the specification of display functionality, display concept, colors, characteristics of display automation, and system interface with the pilot.  In critical flight situations, the pilot may not be expected to make priority decisions him/herself when interacting with the system. An auto-declutter feature may be appropriate when the aircraft is in a hazardous state.  An indication of the information contained in each layer should be available to the pilot.  A method to turn on and off individual layers should be available to the pilot. 

 
The most important layer of display information, in all cases, should be the current navigation situation and current position of the aircraft with planned flight route.  The ownship information should be on top of the other data formats.  The flight plan should also be on top except when some high-priority text information might be obscured.  As a minimum, a planview should be provided. 

In general, long-range textual information such as METARs, TAFs, and NOTAMs should not be overlaid on a planview or vertical profile display.  These products can be provided on a separate page or in a separate screen area, since they are generally referred to by the pilot when needed and not monitored on a continuous basis.  Where possible, an effort should be made to inhibit textual labels from writing on top of one another. Existing guidance on display design provides information on the use of color and contrast to discriminate between high interest and low interest features within the same category of information (for example, terrain), and to focus attention on critical features.  Less guidance is provided to differentiate different categories of information when these categories needs to be presented simultaneously.  For example, the same color set with varying intensities, contrasts, or textures to convey criticality can be re-used within different categories of information (for weather or for terrain or traffic) all of the time.  More care is needed with a color set (such as red/yellow/green) to specify criticality across all categories of information.  The meaning of such a simultaneous presentation could be enhanced if categories of information are further differentiated by the use of unique graphics or other easily differentiable icons. The use of this display paradigm necessarily requires the implementation of decision support algorithms that ensure unambiguous guidance to the pilot in all situations.  Certification criteria shall be specified and evaluated to ensure conflicting hazard avoidance guidance is never provided to the pilot in any flight situations.  In general, this display paradigm will provide the most effective cockpit display of FIS products, but it also adds complexity to system development and verification. Finally, a question arises as to how to control which categories of information are available for selection at any particular time by the pilot.  Again, it is impossible to specify display options in general guidance. For most flight situations, it may be appropriate to permit the display of all categories of information, allowing the pilot to make his/her own display decisions.  As the decision support function of the cockpit display system determines that a particular category of information emerges as a dominant category, it may be appropriate to inhibit those categories that are not critical.  In this case, the pilot should be made aware that options are being inhibited and that the dominant category of FIS information needs immediate attention.  In the worst case scenario, where traffic, weather, terrain, and precise navigation all need pilot attention simultaneously, a design scheme that inhibits all extraneous information except precise decision guidance that deals with the most critical hazards is needed.  Look-ahead decision guidance should be considered to prevent a situation where hazard categories have to be dealt with simultaneously. To summarize: 
a. The current navigation situation and current position of the aircraft with respect to its planned flight route should not be obscured by FIS data symbols. 

b. The prioritization rules for layering of information may consider not only category 
(e.g., terrain, weather, traffic), but also severity of phenomena. 
c. Information displayed in textual form such as METARs, TAFs, and NOTAMs should 
not be overlaid on a map display except to amplify or explain concisely the meaning of a graphical feature.  These products can be provided on a separate page or screen region, since they are generally referred to by the pilot when needed and not monitored on a continuous basis. 
d. If a display system incorporates a decision support function, and if the decision 
support function determines that a particular hazard requires immediate pilot 
attention, the display of FIS information that is not critical may be inhibited.  In this case, the pilot should be made aware that the display of FIS information data is being inhibited and that the dominant hazard needs immediate attention. 

e. A method to turn on and off individual layers of information should be available to 
the pilot. 
f. An indication of current displayed layers should be available to the pilot. g. If the traditional use of red, yellow and green is maintained to prioritize threats, then 
when multiple categories of information are combined (weather, traffic, terrain), 
some unambiguous method should be employed to differentiate between these categories.  Different weather phenomena (such as icing, turbulence, precipitation) should not be displayed simultaneously if this display paradigm is used. 
 
This page intentionally left blank.

## Appendix J National Convective Weather Forecast (Ncwf)

This page intentionally left blank.

## Appendix J National Convective Weather Forecast (Ncwf)

The National Convective Weather Forecast (NCWF) is an operational aviation weather product that is produced by the National Weather Service Aviation Weather Center (AWC).  The NCWF product is automatically generated and updated every five (5) minutes.  The NCWF is actually composed of two component products: 

a. the first is a graphic depiction of current convection which combines convection 
detected through: 
1. WSR-88D (NEXRAD) national radar and echo top mosaics; and 
2. cloud-to-ground lightning; and 
b. the second is a graphic depiction of one (1) hour extrapolated forecasts of significant 
current convection. 
The NCWF hazard levels are depicted based on a six (6) level intensity scale as shown in Table J-1 
below.  The six (6) hazard levels fundamentally correspond to the conventional weather radar VIP levels, which are discussed in Appendix H.  In the NCWF, however, the intensity of the NEXRAD radar returns is calibrated in terms of Vertically Integrated Liquid (VIL), which is measured in liquid water content 
(kg/m2).  The magnitude of VIL relates to the strength of updraft in the convective cells and is an indicator of storm severity.  The lightning data supplements the NEXRAD data, filling in holes in NEXRAD coverage during radar outages or in Western US data void regions.  The number of lightning strokes within 8 km of a gridpoint in 10 minutes is used as a proxy for intensity.  At any grid point, the higher of radar or lightning levels is used. The NCWF displays one (1) hour forecasts of cells (regions) with equal to or greater than hazard level 3; 
the NCWF forecast does not distinguish among level 3 through level 6.  The NCWF hazard level 3 
corresponds (approximately) to the current airborne weather radar hazard level 3. 

 

NCWF 
Hazard Levels 
Approximate Correlations 
Ltg. Rate 
Reflectivity 
 
VIL 
(kg/m2) 
(/10 min) 
Effect 
Airborne 
Radar 
(dBZ) 
VIP 
Level 4 Very 
5-6 
12 + 
15 + 
Severe Turbulence, 
Lightning Hail likely 
Hazardous 
50 + 
5 - 6 
Level 3 
4 
6.9 - 12.0 
6 - 14 
Possible Severe Turbulence, 
Lightning 
Hazardous 
45 - 49 
4 
Level 3 
3 
3.5 - 6.9 
3 - 5 
Possible Severe Turbulence, 
Lightning 
Hazardous 
40 - 44 
3 
Level 1-2 weak-
1-2 
0 - 3.5 
NA 
Light to Mod. Turbulence, 
Possible Lightning 
moderate 
0 - 39 
1 - 2 

 
The correlations in Table J-1 above are the basis for the color recommendations included in Section 3.8.2, Table 3-2.  The NCWF hazard levels were mapped to the Precipitation Product VIP levels and color recommendations.  With this mapping, the cockpit display of NEXRAD Precipitation Products and the NCWF will be correlated. It should be noted that research on refining the NCWF forecast algorithms as well as increasing the resolution of the NCWF detection is continuing.  That research may result in changes to Table J-1 to the specific VIL and lightning strike correlations for determining individual hazard levels, but the correlation of the NCWF six (6) hazard levels to the VIP levels and airborne radar will remain unchanged.  Thus the color-coding recommendations in Section 3.8.2, Table 3-2 should not be impacted by such changes. Additional background on the NCWF products is available in the AIM Section 7-1 and the AWC website 
( http://aviationweather.noaa.gov). 

This page intentionally left blank. 

## Appendix K Data Link Applications Coding (Dlac) 6-Bit Alphabet

The following table provides the binary coding for the 6-bit DLAC alphabet: 

| Bit Encoding                           | Character                              | Bit Encoding    | Character                 |
|----------------------------------------|----------------------------------------|-----------------|---------------------------|
| 000000                                 | ETX                                    | 100000          | SP                        |
| 000001                                 | A                                      | 100001          | !                         |
| 000010                                 | B                                      | 100010          | "                         |
| 000011                                 | C                                      | 100011          | #                         |
| 000100                                 | D                                      | 100100          | CS                        |
| 000101                                 | E                                      | 100101          | %                         |
| 000110                                 | F                                      | 100110          | &                         |
| 000111                                 | G                                      | 100111          | '                         |
| 001000                                 | H                                      | 101000          | (                         |
| 001001                                 | I                                      | 101001          | )                         |
| 001010                                 | J                                      | 101010          | *                         |
| 001011                                 | K                                      | 101011          | +                         |
| 001100                                 | L                                      | 101100          | ,                         |
| 001101                                 | M                                      | 101101          | -                         |
| 001110                                 | N                                      | 101110          | .                         |
| 001111                                 | O                                      | 101111          | /                         |
| 010000                                 | P                                      | 110000          | 0                         |
| 010001                                 | Q                                      | 110001          | 1                         |
| 010010                                 | R                                      | 110010          | 2                         |
| 010011                                 | S                                      | 110011          | 3                         |
| 010100                                 | T                                      | 110100          | 4                         |
| 010101                                 | U                                      | 110101          | 5                         |
| 010110                                 | V                                      | 110110          | 6                         |
| 010111                                 | W                                      | 110111          | 7                         |
| 011000                                 | X                                      | 111000          | 8                         |
| 011001                                 | Y                                      | 111001          | 9                         |
| 011010                                 | Z                                      | 111010          | :                         |
| 011011                                 | NC                                     | 111011          | ;                         |
| 011100                                 | TAB                                    | 111100          | <                         |
| 011101                                 | RS                                     | 111101          | =                         |
| 011110                                 | CRLF                                   | 111110          | >                         |
| 011111                                 | CC                                     | 111111          | ?                         |
| Notes:                                 |                                        |                 |                           |
| SP       =                             | Space                                  | CS    =         | Currency Symbol (e.g., $) |
| ETX    =                               | End of Text marker                     | NC    =         | Null Character            |
| CC      =                              | "Change-Cipher" indicator (note that   |                 |                           |
| FIS does not Incorporate the DLAC      |                                        |                 |                           |
| "cipher-coding" algorithms, treat as a |                                        |                 |                           |
| null character)                        |                                        |                 |                           |
| TAB =                                  | Tabulator (the binary value of the six |                 |                           |
| bits following the TAB character       |                                        |                 |                           |
| define the number of blank characters  |                                        |                 |                           |
| [1-64] to be inserted)                 |                                        |                 |                           |
| CRLF =                                 | Carriage Return/Line Feed (also the    |                 |                           |
| end-of-line function)                  |                                        |                 |                           |
| RS    =                                | Record Separator                       |                 |                           |

This page intentionally left blank. 