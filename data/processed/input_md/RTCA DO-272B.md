 

## User Requirements For Aerodrome Mapping Information

 
Copies of this document may be obtained from 
 
RTCA, Inc. 

1828 L Street, NW, Suite 805 
Washington, DC 20036 USA 
 
Telephone: 202-833-9339 
Fax: 202-833-9434 
Internet: www.rtca.org 
 
Please call RTCA for price and ordering information. 

## Foreword

 This report was prepared by RTCA Special Committee 217 (SC-217) and EUROCAE Working Group 44 (WG-44) and approved by the RTCA Program Management Committee (PMC) on April 14, 2009. RTCA, Incorporated is a not-for-profit corporation formed to advance the art and science of aviation and aviation electronic systems for the benefit of the public.  The organization functions as a Federal Advisory Committee and develops consensus-based recommendations on contemporary aviation issues. RTCA's objectives include, but are not limited to 

 
coalescing aviation system user and provider technical requirements in a manner that helps government and industry meet their mutual objectives and responsibilities; 
 
 
analyzing and recommending solutions to the system technical issues that aviation faces as it continues to pursue increased safety, system capacity and efficiency; 
 
 
developing consensus on the application of pertinent technology to fulfill user and provider requirements, including development of minimum operational performance standards for electronic systems and equipment that support aviation; and 
 
 
assisting in developing the appropriate technical material upon which positions for the International Civil Aviation Organization and the International Telecommunication Union and other appropriate international organizations can be based. 
 The organization's recommendations are often used as the basis for government and private sector decisions as well as the foundation for many Federal Aviation Administration Technical Standard Orders. Since the RTCA is not an official agency of the United States Government, its recommendations may not be regarded as statements of official government policy unless so enunciated by the U.S. government organization or agency having statutory jurisdiction over any matters to which the recommendations relate. 

This Page Intentionally Left Blank.

## Executive Summary

 Operations at large aerodromes have become a complex combination of many activities being performed by many individuals.  This group of individuals includes pilots, air traffic controllers, apron controllers, surface vehicle operators, construction/maintenance crews, emergency/security personnel, commercial and cargo airline operations personnel, and general and business aviation operations personnel.  All of these individuals must work collaboratively to ensure safe efficient flight operations at the aerodrome. Furthermore, all of these individuals, or *users*, require some knowledge of the aerodrome layout. Traditionally, pilots navigate on the surface based on visual aids such as airfield markings, signs, and lighting, in conjunction with a paper chart of the aerodrome layout.  Radio communications between air traffic control (ATC) and pilots are used to obtain the route to follow while on the surface.  ATC issues route instructions, using explicit phraseology along with unique names of legs along the route.  ATC must remember the routes given to all aircraft, as well as all aircraft locations, so that no one is directed into a potential collision.  If there is a potential for collision, hold-short instructions can be issued over the radio frequency to constrain aircraft movements.  To maintain safe separation, surveillance on the aerodrome surface is performed by the flight crews based primarily on the ―see-and-avoid‖ principle.  Similarly, ATC performs the surveillance task based primarily on visual cues.  Occasionally, both pilots and controllers will use radio communications to confirm positions of relevant traffic.  From this brief description of aircraft movements, it is apparent that both ATC and pilots require geospatial information about the aerodrome layout (e.g. the relative location and orientation of runways, taxiways, and stands). In order to support flight operations at aerodromes, several other activities are required, each performed by separate organizations and/or facilities.  The aerodrome authority is responsible for construction and maintenance of aerodrome resources such as buildings, pavement, markings, and landing systems (e.g., ILS).  They are also responsible for providing emergency response teams such as fire/rescue and aerodrome security in some cases.  Commercial and cargo airline operators perform activities such as apron control, aircraft maintenance and fueling, baggage and cargo handling, catering services, crew and aircraft scheduling, flight planning, and ticketing.  They also manage training activities such as flight simulations to assure pilot currency.  Finally, General Aviation (GA) and Business Aviation operations are typically supported by Fixed Base Operators (FBOs).  FBOs support GA and Business Aviation operations by providing maintenance, fueling, flight planning, and local ground transportation services. As with pilots and controllers, all of these users also require geospatial information. The information contained in this document has been compiled by industry for the purpose of stating surface mapping information requirements for users such as those described above.  The requirements presented are not all-inclusive, but represent those of more immediate concern.  Airworthiness authorities, civil aviation authorities, and the aviation industry urge aerodrome mapping database (AMDB) originators and integrators to use this document when providing those data to system designers and users. In addition, this document provides guidance material on structure of AMDBs.  Based on the availability of standardized current AMDBs, a variety of applications can be envisioned.  Several are described in this document.  This document has been written under the assumption that if all users are using the same AMDB, operations can be improved, and new capabilities can be realized. The document is organized as follows: 

 
Section 1 provides background information with respect to the purpose of  developing AMDB requirements 
 
Section 2 describes aerodrome mapping data considerations that are important when attempting to comply with this document 
 
Section 3 provides general requirements and recommendations for AMDB development 
 
 
Section 0 provides more detailed content requirements and specific numerical requirements 
 
Appendix A provides an overview of the types of applications that may make use of AMDBs 
 
Appendix B is a glossary of relevant terms 
 
Appendix C lists important abbreviations and acronyms 
 
Appendix D may be used as guidance material when creating AMDBs to meet the quality requirements specified in this document 
 
Appendix E lists the membership of the committee that developed this document 

## Revisions To Rtca Do-272A/Eurocae Ed-99A

The following list is a summary of the major changes made to RTCA DO-272A / EUROCAE ED-99A for the DO-272B and ED-99B versions. Editorial errors, mainly reported by the users of the previous version of the document, or found during the update of the document were corrected. The reference list was updated and amended. RTCA DO-291A/EUROCAE ED-119A, Interchange Standards for Terrain, Obstacle, and Aerodrome Mapping Data was added to the reference list and is considered normative for the purposes of data interchange. Clarifications and text enhancements were provided for the following document sections: 

 
Section 2.3.2 Completeness 
 
Section 2.3.3 Connectivity 
 
Section 3.11.2 Aerodrome Structures 
 A capture rule was added to make mandatory/optional requirements explicit: 

 
Section 4.3 Data Elements rule 4.3.0.2 
 Feature overlap, where allowed, was explicitly stated. Geometrical/functional relations and constraints requirements were amended to reflect new features. The connectivity rules were revised. Deleted rules were marked. Numerical requirements were amended to reflect the addition of new AMDB features. No changes were made to the numerical requirements of the existing AMDB features. Definitions, features, attributes, and data content were revised to harmonize with AIXM5 and ARINC816. Following the revision process, changes were made to the Feature Catalogue. A brief summary of these changes follows: 

 
New features were added: Blastpad, Water, Hotspot, Aerodrome Surface Lighting; 
 
A new attribute idnumber was added to all features; 
 
A 
new 
attribute 
restacn 
was 
added 
to 
the 
RunwayElement, 
RunwayIntersection, 
RunwayDisplacedArea, TaxiwayElement, ApronElement, ParkingStandArea, DeicingArea features; 
 
Attribute pcn was inserted in the RunwayDisplacedArea feature; 
 
Attribute papivasi was replaced by attribute vasis for RunwayThreshold feature; 
 
Attribute surftype was changed to gsurftyp for ServiceRoad feature; 
 
Attributes vacc and vres were deleted from the ConstructionArea feature; 
 
Codelists feattype, surftype, gsurftyp, plysttyp, linsttyp, pntsttyp were modified; 
 
Feature attribute definitions were enhanced: vacc, hacc, vres, integr, revdate, acn; 
 
Feature attribute value domains were modified: width, brngtrue, brngmag, idstd; 
 
New attributes required by new features were added (example: idhot for the Hotspot feature.). 
 The membership list was updated and this summary of revisions was included. 

 

## Revisions To Rtca Do-272/Eurocae Ed-99

 
The following list is a summary of the major changes made to RTCA DO-272 / EUROCAE ED-99 for the DO-272A and ED-99A versions.  
A number of editorial errors, mainly reported by the users of the previous version of the document, or found during the update of the document were corrected. The reference list was updated and amended. RTCA DO-291/EUROCAE ED-119, Interchange Standards for Terrain, Obstacle, and Aerodrome Mapping Data was added to the reference list and is considered normative for the purposes of data interchange. The use of EGM-96 as the gravity model for the vertical reference system was changed from a recommendation to a requirement to harmonize with ICAO Standards and Recommended Practices. Several changes were made to accommodate for Amendment 33 of ICAO Annex 15. This includes figures, definitions and numeric values (e.g. obstacle data collection surfaces). The text to describe the severity levels of applications using the data was revised to harmonize with certification standards such as RTCA DO-178B/EUROCAE ED-12B. Database update cycles were revised to accommodate more frequent deliveries of data than the AIRAC cycles. User feedback was added to the list of possible verification and validation methods. Requirements were added that define geometrical relations and constraints. The requirement concerning the overlap of polygon features was changed. Attributes were added to accommodate multi-use surfaces. Requirements and definitions for functional constraints were added to the feature attribute section. Accuracy requirements for *Medium* quality data sets were modified. Appendix E of the previous version was removed. Data capture and content requirements were moved from Appendix E of previous version into Section 4 (Specific Requirements) of this version. Coding information appropriate for the exchange of data was removed and can now be found in RTCA DO- 291/EUROCAE ED-119. As appropriate, definitions and feature or attribute names as well as data content were revised to harmonize with RTCA DO-291/EUROCAE ED-119. Service Roads and Displaced Threshold Areas were added as data elements. Clearways were removed. The Glossary was revised to harmonize with RTCA DO-291/EUROCAE ED-119 and with the latest versions of ICAO annexes. The membership list was updated and this summary of revisions was included. 

## 1 Purpose And Scope 1.1 Introduction

The information contained in this document has been compiled for the purpose of stating aerodrome surface mapping information requirements for aeronautical uses, particularly on-board aircraft.  The term aerodrome is used in this document to include: Aerodromes, Heliports, and Sea-Plane aerodromes.  The requirements are not all-inclusive, but represent those of more immediate concern.  As future applications are developed, more stringent numerical requirements may be needed.  Airworthiness authorities, civil aviation authorities, and the aviation industry urge the aerodrome mapping data originators and integrators to use this information when providing those data to system designers and users. Based on the availability of standardized aerodrome mapping databases (AMDBs), a wide variety of applications can be envisioned (Appendix A). It is important to note that multiple user classes can benefit from using these databases, for example: pilots, controllers, aerodrome managers, and aerodrome emergency/security personnel.  Each of the applications listed below are described in detail in Appendix A. 

 
Chart information Surveillance and runway incursion detection and alerting Route and hold-short display and deviation detection and alerting Display of digital ATIS information Aerodrome surface guidance and navigation Runway operations Aerodrome and airline resource management Training (flight simulation) 
Aerodrome facility and asset management Emergency and security service management Notice To Airmen (NOTAM) and aeronautical data overlays Synthetic vision 

## 1.2 Scope

This document provides minimum requirements and reference material applicable to the content, origination, publication, updating, and enhancement of aerodrome mapping information.  The document also provides guidance to assess compliance and determination of the levels of confidence that need to be reached to support the types of applications listed in Appendix A.  This document should be used to support the development and application of AMDBs.  AMDBs represent a collection of aerodrome information that is organized and arranged for ease of electronic storage and retrieval in systems that support aerodrome surface movements, training, charting, and planning. Appendix A is intended to provide an overview of the types of applications that may make use of AMDBs.  These application categories have been used to generate the requirements stated herein. 

 
The content generated/surveyed within the scope of this document will be interchangeable according to the rules defined in RTCA DO-291A/EUROCAE ED- 119A. 

## 1.2.1 Definition Of Terms

The precise meaning of terms is essential for a clear understanding of spoken or written information.  This understanding is critical in areas where safety is of concern.  Certain terms and expressions used in this document have specific meanings that must not be misconstrued or applied incorrectly.  These terms are defined in a glossary in Appendix B.  Acronyms are described in Appendix C. In addition, the following conventions of requirements documents have been adopted: 

 
The term ―should‖ implies that compliance is not required, but is strongly 
recommended 
 
The term ―shall‖ means that compliance is required 
Requirements are specified in Sections 3 and 4 and are uniquely numbered to support requirements traceability procedures. 

## 1.2.2 Reference Documents

(1) 
RTCA DO-200A/EUROCAE ED-76, Standards for Processing Aeronautical Data 
(2) 
RTCA DO-201A/EUROCAE ED-77, Industry Standards for Aeronautical Information 
(3) 
RTCA DO-276A/EUROCAE ED-98A, User Requirements for Terrain and Obstacle Data 
(4) 
RTCA DO-291A/EUROCAE ED-119A, Interchange Standards for Terrain, Obstacle, and Aerodrome Mapping Data 
(5) 
ICAO Annex 4, International Standards and Recommended Practices - Aeronautical Charts 
(6) 
ICAO Annex 14, International Standards and Recommended Practices - Vol. I Aerodromes and Vol. II Heliports  
(7) 
ICAO Annex 15, International Standards and Recommended Practices - Aeronautical Information Services 
(8) 
ICAO Doc. 9157, *Aerodrome Design Manual* 
(9) 
ICAO Doc. 9674-AN/946, World Geodetic System 1984 (WGS-84) *Manual* 
(10) 
FAA Doc. No. 405, *Standards for Aeronautical Surveys and Related Products*, September, 1996. 

## 1.3 Application Of Standards

As stated in RTCA DO-200A/EUROCAE ED-76, ―the ultimate responsibility of ensuring that data meets the quality for its intended application rests with the end-user of that data.‖ Figure 1-1 depicts the data integration processes that contribute to the development of an AMDB.  Initially, data originators may collect aerodrome mapping data using various technologies (e.g. aerial photography, satellite imagery, or topographical surveys).  The originators may collect data to support non-aeronautical applications; however, any data to be used to support aeronautical applications must meet the requirements defined herein (illustrated as Requirements A in Figure 1-1).  These requirements (see Sections 3 and 0) are not expected to affect existing standards being used for data acquisition.  However, in some cases, because of stringent accuracy and integrity requirements, traditional validation procedures may require modification. 

## Requirements A

REQUIREMENTS A REQUIREMENTS A
Originator 1 Originator 1
Originator 2 Originator 2
Originator n Originator n
(sat, topo surveyor) (sat, topo surveyor) (sat, topo surveyor)
(sat, topo surveyor) (sat, topo surveyor) (sat, topo surveyor)
(sat, topo surveyor) (sat, topo surveyor)
REQUIREMENTS B

## End User Pool

END USER POOL END USER POOL

## Application 1 Application N Aircraft Operators

Aircraft Operators Aircraft Operators

## Aircraft Manufacturers

Aircraft Manufacturers Aircraft Manufacturers

## Figure 1-1 Data Integration Processes

 When using data provided from multiple data originators, data integrator(s) may be responsible for merging all appropriate data sets for two purposes: 

(1) the correlation of multiple data sets representing the same aerodrome area to ensure 
full aerodrome coverage and to ensure the required accuracy and integrity 
(2) the concatenation of the many aerodromes into a consistent, globally-referenced 
database that may also include other data types such as terrain, obstacles, and/or air navigation data 
System designers (e.g. avionics manufacturers) may merge specific data sets provided by multiple data integrators to meet the requirements of a specific application.  Some of these requirements (illustrated as Requirements B in Figure 1-1) are also defined herein. The aim of this document is to define a set of requirements that can be applied along this chain in order to obtain a database commensurate with the criticality of the final application of the data. 

## 1.4 Aerodrome Mapping Information 1.4.1 Introduction

The advent of ground-based applications based on the use of aerodrome surface data and of onboard applications of aerodrome data to support safe, efficient surface movements, has necessitated the development of requirements and reference material applicable to such data. Most of the existing standards and guidance materials are primarily applicable to air navigation data and were not written with aerodrome surface applications in mind. Issues specific to AMDBs include: 

 
Data may be derived from aerial survey and/or engineering drawings that are not traditional sources of aeronautical information 
 
Suppliers of aerodrome mapping data may not be familiar with typical civil aeronautical requirements, standards, and methods 
 
There are many different formats available for aerodrome mapping data (vector, raster, digital elevation models, etc.) 
 
Aerodrome operators seldom publish changes to their aerodrome data within the ICAO-published AIRAC cycles 
This document is intended to cover these specific issues so that the document can be submitted (together with DO-200A/ED-76) to the aviation community as a collection of disciplines necessary to provide assurance that the production of AMDBs meet the high quality required for safe aerodrome surface operations. The starting point for aerodrome information is the data published by States in their Aeronautical Information Publication (AIP) in accordance with ICAO Standards and Recommended Practices (SARPS) (ICAO Annex 15).  However, much of the specific detail required to support the kinds of applications envisaged in Appendix A is not reported on, as it is not necessary for traditional aviation operations.  Therefore, other sources of information for the aerodrome may be necessary for these applications. 

## 1.4.2 Overview Of Trade Practices

The majority of existing AMDBs have been captured and maintained using Geographic Information Systems (GIS). GIS technology has evolved from the Computer-Aided Design (CAD) industry, combining the detailed information available in engineering drawings with a geographic reference system.  A GIS is a computer program that combines geographically referenced digital data with spatial and attribute analysis tools. The strength of a GIS lies in the methods it provides to represent and analyze geographic information. A GIS can include many different types of data including: control networks, vector data, raster grid data, triangulated irregular networks (TINs), 3-D surface representations, remotely sensed data, and other digital source data such as georeferenced drawings or Airport Layout Plans (ALPs) (see Figure 1-2).  Within a GIS, these data sources can be combined, spatially referenced, and analyzed; enabling the user to organize information and answer questions about the spatial relationships between the various thematic layers as well as the attribute characteristics of the features. In addition to the use of GIS technology, AMDBs have also been realized by digitizing paper charts such as airport obstruction charts, utilizing Computer-Aided Design (CAD) tools, and in text or tabular files. 

## 2 Aerodrome Mapping Data Considerations 2.1 Reference System Considerations

Converting AMDB data elements to a common datum is an issue when source data is referenced to different datums and sufficient conversion algorithms do not exist.  Air navigation considerations and the state of the art regarding the use of the Global Navigation Satellite System (GNSS) for instantaneous positioning and navigation, require that the reference frame for AMDBs be based on the theoretical surface and universallypositioned ellipsoid defined as WGS-84 (see Section 3). 

WGS-84 is the required aviation standard for horizontal reference system and Mean Sea Level (MSL) is the required vertical reference system.  MSL elevations can be derived using an appropriate geoid model.  The Earth Gravitational Model (EGM-96) is the required global gravity model.  

 
There are several specific advantages to using the WGS-84 reference ellipsoid: 

 
The use of a unique universally-located reference frame 
 
Consistent with state-of-the-art regarding avionics systems (e.g. GNSS) 
 
Simple transformation formulas from ellipsoid to a cartographic system 
 
Problems related to feature positioning, estimation of angles, distances, areas, etc., due deflection of the vertical are minimal and in certain cases negligible 
 
Conversion of international aerodromes to WGS-84 has been mandated by ICAO 
From an interoperability standpoint, having the data available using a common datum is essential.  Problems may be encountered when dealing with sources that have an unknown datum. Further, on-board sensors and avionics instruments may provide dynamic inputs to aerodrome mapping databases.  These are other sources of information that may need to be converted within the system. It is expected that these datums will be known and the appropriate conversion can be applied. In cases where an AMDB already exists and is based on a different reference system, the data must be transformed to a WGS-84 reference.  This transformation may induce errors.  Therefore, care must be taken to ensure that the conversion process does not impact the integrity of the data and prevent its use in the application for which it was intended. 

## 2.2 Aerodrome Data 2.2.1 Characterization Of Aerodrome Mapping Data

Unlike terrain databases, which are typically represented as grid points with associated elevation data, aerodrome databases are typically constructed from a photogrammetric image that is converted to vectors and assigned themes and attributes using GIS techniques.  This is because many important data elements are features and not just elevations.  These features are more easily characterized by points, lines, and polygons (described in Section 0).  Examples include runway edges, hold points, and stand locations.  In other words, in AMDBs, not only should the aerodrome surface be properly represented (as is done in terrain databases), but also all existing natural or man-made features should be properly characterized. The use of vector-based data has several advantages: 

 
Small data storage requirement 
 
Easy use of a relational data base structure 
 
Easier for updating purposes 
 
No need of feature recognition software 
 
Easy attachment of attributes 
Consequently, it is recommended that vector-based data (points, lines, and polygons) be used for the characterization of aerodrome features in AMDBs.  An alternate approach is to use raster data or imagery.  Using this approach, features are portrayed via contiguous pixels of equal or similar density number.  This less precise approach may be acceptable for some applications. Aerodrome surface data, unlike terrain data, represents regular geometric objects that can be grouped or classified. Examples of classifications are: runways, taxiways, service roads, localizer antennas, glide slope antennas, buildings, radar sites, radio navigation beacon sites, etc.  All of these can be described with their own set of attributes, most of which are related to horizontal positioning, and not elevation.  These attributes combine to provide a set of aerodrome data requirements that are distinguished from those of terrain data.  This distinction must be recognized and preserved, since more attributes will be required to appropriately create the aerodrome images for use by the flight crews. The array of attributes used to describe aerodrome features is not complete. It is imperative, to reduce the cost of systems that use the aerodrome data, to use standard representation classes and attributes.  It is the intent of this document to define these standards (see section 4). 

## 2.2.2 Obstacle And Obstruction Data For The Aerodrome Surface

Obstructions are obstacles that penetrate a defined surface.  In determining obstruction data requirements, certain accuracy parameters are applied to construct buffers around obstacles and estimate whether they penetrate the defined surface.  Depending on the radius specified, unrealistically large, converging or overlapping buffers may be generated, resulting in high false alarm conditions.  Internationally recognized survey standards should be used.  ICAO Annex 14 defines the requirements for identifying obstacle limitation surfaces.  This is similar to the Obstruction Identification Surface (OIS) schema.  Further criteria for evaluating obstacles are contained in Procedures for Air Navigation Services - Aircraft Operations (PANS-OPS).  An equivalent approach to those mentioned above has been taken when considering which aerodrome obstacles should be included in AMDBs and declared to be obstructions (see Section 3).  Finally, the reader may consider ICAO Annex 15 and RTCA DO-276A / EUROCAE ED-98A terminal area obstacle requirements. 

## 2.2.3 Terminal Area Terrain Data

Consideration of terrain on and around the aerodrome is essential to terminal area airspace operations such as approach, departure, and contingency procedure planning.  
Hazards related to terminal area terrain awareness and avoidance have been cited as a major contributing factor in CFIT (controlled flight into terrain) accidents1.  Terrain is also important to surface navigation.  It defines the surface topography of the ground in and around the surface movement areas.  Since terrain data shares a physical boundary with many surface geometric objects on the aerodrome (runways, taxiways, buildings, etc.), it is important that the terrain data be correlated with these other data types.  For further information on terrain data requirements, see RTCA DO-276A/EUROCAE ED- 98A. 

## 2.3 Application Considerations 2.3.1 Correctness

In most cases, the required data quality will depend on the intended use of the data and the system in which the data resides.  One approach to illustrating this concept is to consider multiple levels of data quality that correspond to the application's criticality (or impact on safety).  Consider the following five severity levels caused by a loss of system integrity due to data errors:  

(1) Data errors could cause or contribute to the failure of a system function resulting in a 
catastrophic failure condition.  A catastrophic failure condition would result in multiple fatalities of the occupants, or incapacitation or fatality of a flight crewmember normally associated with the loss of the airplane. For example, the AMDB is used by a system to provide guidance to an automatic landing system.  
(2) Data errors could cause or contribute to failure of a system function resulting in a 
hazardous/severe-major failure condition. A severe-major failure condition means that:  (a) there is a large reduction in safety margins or functional capabilities, or (b) physical distress or higher workload such that the flight crew could not be relied upon to perform their tasks reliably or completely, or (c) adverse affects on people including serious or potentially fatal injuries to a small number of people.  For example, the AMDB is used by a system to provide information to the flight crew to help steer the aircraft within the confines of the runway prior to takeoff in low visibility conditions.      
(3) Data errors could cause or contribute to failure of a system function resulting in a 
major failure condition. A major failure condition means that:  (a) there is a significant reduction in safety margins or functional capabilities, or (b) a significant increase in operator workload or reduction in operator efficiency, or (c) discomfort to people involved, possibly including injuries.  For example, the AMDB is used by a system that provides warning information to the flight crew of a potential hazard on the aerodrome surface. Another example is the use of an AMDB with traffic information for low speed taxi operation of the aircraft in low visibility conditions. Adherence to a speed limit might be required in airport areas such that it prevents the 
flight crews from using the system in high-speed areas or at speeds that may lead to a higher severity level classification.    

(4) Data errors could cause or contribute to failure of a system function resulting in a 
minor failure condition. This condition means that:  (a) there is a slight reduction in safety margins or functional capabilities, or (b) a slight increase in operator workload or reduction in operator efficiency, or (c) inconvenience to other people involved, possibly including injuries.  For example, an AMDB is used by a system to provide information to the flight crew such that they are aware of the area on the aerodrome surface within which the aircraft can maneuver.  It may be used for low speed taxiing in areas where the flight crew are unfamiliar or need more  information than air traffic control has provided to maneuver the aircraft on the aerodrome surface in visual conditions.    
(5) Data errors have *no affect* on safety, that is, failure conditions that would not affect 
the operational capability of the airplane or increase crew workload.  For example, an AMDB is used by a system that does not display ownship position relative to the aerodrome.  The system is used only for planning purposes and there is a back-up means for the flight crew to receive the information.  If the system is unavailable, the flight crews are able to reference paper charts on-board the aircraft to continue the operation.   
Note: The above examples given for each level have not been fully developed for all cases and actual severity levels would be determined at the aircraft level in the functional hazard assessment. 

## 2.3.2 Completeness

The data requirements specified in this document are based on the current and expected aerodrome data needs of the intended applications listed in Annex A.  Only a ―complete‖ set of aerodrome data can ensure that all of the envisioned applications can be implemented by system designers. However, not all applications require a complete set of aerodrome data to enable their intended use. For example, electronic charts used for flight planning may not require centerline data. Completeness is a quality requirement of an AMDB data product. It reflects the degree of conformance of an AMDB instance in relation to the expected AMDB content as specified by the AMDB data product specification. AMDB completeness depends on AMDB features, AMDB feature attributes, and metadata elements. 

Completeness requirements are applicable at the AMDB feature level and metadata level: 
Features listed in the AMDB feature catalogue are mandatory. When an AMDB does not contain a feature instance which exists in the real world, its completeness is affected. However, features instances can only be provided if they exist in the real world. Therefore, AMDBs shall contain an empty class for each nonexistent feature.  
Completeness 
requirements 
are 
applicable 
at 
the 
feature 
attribute 
level:  
Feature attributes are mandatory unless specified otherwise. Each feature attribute shall contain a value. This may be a default value.  
Supplemental (optional) AMDB features and attributes may be provided, if specified according to the provisions of this document. 

## 2.3.3 Connectivity

For applications that require fully connected topologies, additional content may be required to identify interconnection points and to account for areas where there are no visual markings. For example, painted stand guidance lines from apron taxilines to stand taxilines may not exist. Data providers are not required to fill these gaps in order to meet the minimum requirements specified in this document. As a result, a fully connected topology may not be provided/available. 

## 2.4 Types Of Errors

Errors in AMDBs can be classified into three types: Random Errors, Blunders, and Systematic Errors.  These are defined in Appendix D.  With respect to data acquisition for AMDBs, statistical methods should be applied in order to assess the random errors. Digital filters, based on statistical principles should be designed in order to locate and eliminate blunders. There are, in surveying sciences, highly efficient techniques for this purpose. With respect to systematic errors, deterministic procedures should be adopted to correct the observations or taken into consideration in the derived statistics.  Each data acquisition method or data to be acquired may have its own systematic effect or bias included in the value of the statistics itself.  To eliminate it there are two recommended approaches: 

 
The use of an appropriate mathematical model that describes the systematic effect (e.g. earth curvature, refraction, etc.) 
 
The use of extended models to account for a combination of systematic effects of known sources and quasi-random effects that are difficult to model.  A typical example is the auto-calibration used in photogrammetric aero-triangulation. 
Geospatial databases are three-dimensional, expressing features in two spaces: horizontal and vertical.  Two dimensions, latitude and longitude, are used to express the horizontal space location, while the elevation is used to express the vertical space location.  When considering mapping data, the general error types described above take three basic forms of errors in the final product.  The three forms of errors in these databases are: (a) incorrect horizontal location for an elevation value, (b) incorrect elevation for a horizontal location, or (c) both.  These types of errors are the most important consideration when using the data.  The three types of errors may be indistinguishable when the data is used; however, there are certain traits of these errors: 

 
Groups of data may share a common error, such as a translation error in which a geographic region or feature is displaced.  In AMDBs, latitude/longitude errors are generally of more interest than elevation errors because data changes predominantly in the horizontal space (i.e. aerodromes are relatively flat).  These location errors are generally a fundamental attribute of a dataset, and are a result of the measurement techniques used when the data is taken (i.e. a Systematic Error).  DO-201A/ED-77 describes the convention that is required by the aviation industry to minimize the 
effects of this type of systematic error.  In general, it states that measurements and calculations should be carried to at least one more decimal place than will be required in the final value. 

 
Elevation errors may vary in an indistinguishable manner (i.e. a *Random Error*). This is another basic attribute of datasets, and is usually a function of the measurement equipment. 
 
Individual errors (i.e. *Blunders*) may exist in the dataset as evidenced by ―spikes‖ in the data.  These individual anomalies are, in general, easier to recognize than the systematic errors discussed above.  Software in the user system may perform simple analyses to determine if the rate of change of data is higher than expected, thus sifting out these anomalous data points. 

## 2.4.1 Effect Of Errors On System Integrity

System integrity is related to AMDB errors in that integrity can be compromised if errors in the database exist and cannot be detected by the operational system.  In a typical avionics system, techniques to boost system integrity are as follows: 

 
A thorough analysis, called a *Functional Hazard Assessment (FHA),* is performed on the system to determine the failure modes that contribute to undesired top-level events.  The integrity of the system cannot be understood until this analysis is completed.  Using the output of the FHA, the system can be designed to eliminate or mitigate the effects of the failures contributing to the top-level events.  Using architectural techniques such as system redundancy, perhaps even using dissimilar implementations, can increase system integrity.  In general, redundancy allows comparison of system outputs and allows detection of system failure.  Use of dissimilar implementations ensures that one implementation does not have a systemic flaw/error that could adversely affect integrity. 
 
The addition of monitoring and built-in-test equipment (BITE) functions allows detection of system failures.  The effect of monitoring/BITE is to lower the probability of undetected failure/error, which in turn will increase system integrity. 
The techniques listed above are not intended to be comprehensive.  The intent is to highlight that AMDBs may contain undetectable errors, and these types of errors must be considered in the design of the system that uses an AMDB and the allowed operational uses of the system. 

## 2.4.2 Errors That Affect The Confidence Level Of A Database

Point estimation is the estimation of the mean, variance, and covariance of a random variable from sample data.  Questions that arise are - how good is the estimation and how much can it be relied on?  A simple answer is not possible because sampling never leads to the true, theoretical distribution or its parameters.  It is only possible to estimate a probability that the true value of the parameter in question is within a certain interval around the estimate.  This probability is called the *Confidence Level*, conventionally required to be 90%, 95%, or 99%, depending on how the data is to be used.  Further, the confidence level of an AMDB is directly related to the lowest confidence level for any existing random variable in the database.  Any type of error may affect the confidence level of the database, but systematic and blunder errors will have a larger impact. Therefore, to achieve high confidence levels, it becomes critical to locate and eliminate these systematic and blunder-type errors if at all possible before the data become available to the end users. 

## 2.4.3 Accuracy And Precision

For the purposes of this document, accuracy is defined as the degree of conformance between the estimated or measured value and the true value. Precision is defined as the smallest difference that can be reliably distinguished by a measurement process.  The main difference between precision and accuracy lies in the possible presence of bias or 
―systematic error‖.  Although precision includes only random effects, accuracy comprises both random and systematic effects.  Both terms are used often with the same meaning. This is because in surveying practice, in the majority of cases, the true value is not known and only a most probable value is estimated via random sample measurement procedures. All observed (random variables) or derived statistics should be qualified through their corresponding accuracy parameters such as mean, variance, standard deviation, and covariance. 

## 2.4.4 Resolution

There are many definitions for the term resolution.  The ICAO definition given in Appendix B of this document is used in Section 4 with respect to AMDB resolution requirements.  This definition states that resolution is the number of units or digits to which a measured or calculated value is expressed and used.   However, other more specific definitions are used in surveying science and particularly in the field of image processing.  Examples include:  spatial resolution, spectral resolution, radiometric resolution, and temporal resolution.  These are also defined in Appendix B and further described in Appendix D.  It is important to note that for AMDBs, not all aerodrome features need to be measured or specified to the same resolution. 

## 2.4.5 Timeliness Effects And Currency Errors

One of the most important attributes of a database is its currency.  This informs the user of the date of its latest update or the effective date of the data.  This information needs to be available at any time to the user.  Aerodromes are frequently undergoing construction activities.  However, changes that occur between update cycles will not be considered to be available as part of the AMDB until the subsequent update.  In the interim, this data may be provided to users via a Notice to Airmen (NOTAM) or other means if appropriate. For some applications, aerodrome, terrain, and obstacle databases must be integrated. This integration of data is typically accomplished by layering of the various information sources into an information hierarchy that supports the application and associated display processing.  The data that contributes to these layers is subject to varying levels of change, which in turn suggests that the data will be updated at different times, or in cycles of differing length.  This inconsistency may result in unexpected database errors that can be difficult to detect by the system designer or the end user.  For this reason, database suppliers and integrators are required to provide documentation on their timeliness and update process (see Section 3.7). 

## 2.4.6 Semantic Errors

These are generally considered blunder errors.  Examples include errors due to the misidentification of an object (e.g. a tower for a mast, a tree for a pole, a road for a railroad); errors due to misclassification of a theme (e.g. sand for clay); and errors due to incorrect attachment of attributes (e.g. length for width).  These blunder errors will affect the consistency and the reliability of the AMDB.  Consistency checks are recommended once the initial database is produced and again on each update. 

This Page Intentionally Left Blank 

## 3 General Requirements

In addition to the following requirements, those described in DO-200A/ED-76 and DO- 291A/ED-119A are applicable. 

## 3.1 Position Data

3.1.1 
The horizontal reference for all position data shall be the WGS-84 ellipsoid. 
3.1.2 
All aerodrome mapping data that includes horizontal position information shall be described in units of latitude/longitude for the purpose of data interchange. 
3.1.3 
It is expected that for many applications, implementation may include conversion to a local coordinate system (e.g. Cartesian) along with at least one geodetic reference point. Data quality shall be preserved when performing coordinate system conversion. 
3.1.4 
For all aerodrome mapping data that requires a vertical component, the vertical reference shall be orthometric height (referenced to MSL) for the purpose of data interchange. 
Orthometric height can be derived using WGS-84 ellipsoidal heights and an appropriate geoid undulation.  Geoid undulation shall be derived using the Earth Gravitational Model of 1996 (EGM-96) or its later realizations. If EGM-96 is not used, the geoid model used to derive orthometric height shall be provided (See ICAO Annex 15, Chapter 3). 

3.1.5 
The metric system shall be used for all linear measurements (e.g., runway length). 

## 3.2 Data Acquisition

Any method is acceptable for capturing aerodrome mapping data subject to the information requirements specified in this document.  Examples include:  aerial photogrammetry, satellite photogrammetry, field surveying, and digitizing existing charts.   

3.2.1 
A description of the process used to acquire aerodrome mapping data shall be provided. This shall be consistent with DO-200A/ED-76 and DO-291A/ED-119A. 

## 3.3 Data Merging

3.3.1 
In order to maintain quality where multiple data sets are merged to create a complete AMDB, each individual data set shall be geo-referenced to the WGS-84 ellipsoid (horizontal) and orthometric height (vertical). 
To avoid potential mismatch problems resulting from different features or themes being captured by different methods and/or originated from different sources, it is recommended that digital graphical editing procedures be used to align and/or match the shifted features using as reference the feature(s) that was geo-referenced with the highest accuracy. The data merging process should not alter the information provided by States without prior coordination with the State authority. 

## 3.4 Data Conversion

3.4.1 
Data sets may be converted to WGS-84 latitude/longitude (horizontal) and orthometric height (vertical); however, the original data, prior to conversion, shall meet the quality 
standards described in this document. 
3.4.2 
Algorithms used to convert data to WGS-84 (horizontal) and orthometric height (vertical) shall not degrade the data quality below levels described in this document. 

## 3.5 Data Source Identification

3.5.1 
The data originator shall identify the source of any aerodrome mapping data provided to the user. 

## 3.6 Data Traceability

Traceability is the ability to track the history, application, or location of an entity by means of recorded identifications.  More specifically, it is the degree to which a system or data product can provide a record of the changes made to that product and thereby enable an audit trail to be followed from the end user to the data originator. 

3.6.1 
The source data originator shall produce adequate information such that the traceability of an AMDB can be maintained according to the above definition and in accordance with DO-200A/ED-76.  Traditionally, a survey report generated by an accredited surveyor will contain sufficient information.  If this type of survey report is generated, the data originators shall release this report on request. 
3.6.2 
The data handler, manipulator, integrator, and/or provider shall produce adequate information such that the traceability of an AMDB can be maintained according to the above definition and in accordance with DO-200A/ED-76.  Typically, this can be accomplished with the provision of an appropriate meta-data record or attribute for each contextual data subset as described in Section 0. 

## 3.7 Database Update Cycles And Timeliness

3.7.1 
Timeliness refers to updating AMDBs to account for errors that have been uncovered as well as to change appropriate data (e.g. due to construction activities).  Aerodrome data shall be updated in accordance with the AIRAC cycle schedule.  The AMDB may be updated more frequently than the standard AIRAC cycle schedule.  Changes that occur between AIRAC cycle updates may be provided by NOTAM, data link, or an equivalent method depending on the operational use of the data. 
3.7.2 
Given that the data has been correctly published or otherwise made available by the data originator, the data integrator shall issue the updated database no later than the next AIRAC date.  In addition, the integrator shall provide a list of changes that have occurred since the previous issuance. 
3.7.3 
Database updates shall be provided, at a minimum, for a complete, contextual AMDB sub-class (see Section 0).  For example, if changes to runway markings are performed on the database, it is then the responsibility of the data handler to provide to its data consumers, at a minimum, the complete runway marking database contextual sub-class.  
The database handler or integrator has the option of providing a complete, updated AMDB or just the sub-class. 

## 3.8 Processing, Handling, And Distribution Of Aeronautical Data

It is essential that the integrity of aeronautical database products, as set forth in this document, be preserved during all phases of transfer, distribution, dissemination, or otherwise handling of the data.  This applies equally to individual data elements as well as to the overall AMDB. 

3.8.1    
DO-200A/ED-76 shall be applied with respect to the handling and processing of AMDBs. 
3.8.2 
DO-291A/ED-119A shall be applied with respect to the interchange of AMDBs. 

## 3.9 Verification And Validation

3.9.1 
Sufficient verification and validation of all data shall be performed such that the quality of the data is assured in accordance with DO-200A/ED-76. 
Additional validation may also be necessary for the benefit of suppliers and airworthiness authorities addressing certification of equipment or equipment components relying on the use of AMDBs because: 

 
AMDBs involve complex technology, that is rapidly evolving 
 
The safety assessment may depend directly on a statement as to the overall quality of the AMDB 
 
Some aerodrome surface movement issues are not addressed by current airworthiness documents or guidance materials 
3.9.2 
In addition to the methods that are described in DO200A/ED-76; adequate documentation of the measurement and mathematical transformation stages shall be available for demonstration that the database has sufficient overall quality.  However, other methods may be employed to make the demonstration.   
The following techniques should be considered for the quality demonstration: 

 
Measurement of a sample of the database points with an independent measurement system.  For example, the use of GPS equipment at specific points to compare to the same points in a database that was created by photogrammetric methods.  The overall integrity of the database can be estimated to arbitrary levels of confidence depending on the number of samples that are checked: more samples give better confidence. 
 
Comparison of the target database to other recorded data such as certified record drawings and airport layout plans.  In every case of comparison against other data, the vertical and horizontal references datums for the two data sets should also be compared. 
 
User feedback (e.g. pilot feedback through airline operations) could be a valuable validation method to verify the consistency, currency, and completeness of the database. 
 
Demonstration by actual use of the database including simulation, driving routes on the aerodrome, or flight test. 
The combination of the validation techniques used needs to produce evidence that an appropriate subset of the data has been validated; meaning the subset of the database upon which the validation is performed is a representative sample of the aerodrome area covered by the database. 

## 3.10 Supplier Qualifications

3.10.1 
Suppliers shall provide sufficient quality information with the aerodrome mapping data for the end user to verify and validate that the data is suitable for its intended use.  
Certification/accreditation of suppliers should consider demonstrating compliance with existing ICAO SARPS, civil aviation authority guidance material, other guidance material, and relevant ISO quality management standards. 

## 3.11 Data Element Extent And Boundary Definition

A complete AMDB is composed of a variety of thematic data elements including, but not limited to, vertical objects, runways, taxiways, and building geometry.  The methods employed to collect and handle each data type may differ widely.  For example, vertical object data may be obtained using traditional ground-based aerodrome surveys.  In addition to collection methods, the data types pose different hazards, risks, and informational opportunities to surface and terminal-area navigation applications. Therefore, the spatial or surveyed extent of the AMDB is defined on an element-byelement basis.  Practical methods of data collection employed by industry (vis. a vis. aerodrome surveyors and GIS specialists) are also considered when defining the AMDB extent.  Note: specific requirements for aerodrome mapping terrain data are described in RTCADO-276A/EUROCAE ED-98A. 

## 3.11.1 Vertical Objects

Requirements regarding the collection of vertical objects are given in ICAO Annex 15 through terrain/obstacle data collection surfaces. Applications requiring *Fine* quality data (see Section 0) require many elements in the movement area be surveyed to sub-meter accuracy.  Initially, these high-accuracy survey requirements will be imposed upon a region in and around the movement areas.  Rationale for the vertical extent boundary is driven by three considerations:  1) wing-tip and airframe clearance requirements, 2) airground (landing) and ground-air (takeoff) proximity operations, and 3) helicopter maneuvering operations. 

3.11.1.1 
When surveying vertical objects, the horizontal spatial extent to be surveyed shall include the aerodrome surface movement area plus a buffer of 50 meters (Figure 3-1 and Figure 3-2), or the minimum separation distances specified in ICAO Document 9157, whichever is greater. 
3.11.1.2 
When surveying vertical objects from a runway, the horizontal spatial extent to be surveyed shall cover the area that extends from the edge(s) of the runway(s) to 90m from the runway centerline(s). 
3.11.1.3 
All vertical objects and terrain in the horizontal spatial extent region that extend more than 0.5 meters above the horizontal plane passing through the nearest point on the aerodrome surface movement area may be hazardous for surface movement and shall, therefore, be surveyed (Figure 3-2). 
3.11.1.4 
Control towers shall always be captured regardless of the location on the aerodrome. 
 

## 3.11.2 Aerodrome Structures

Aerodrome structures is a general term used to describe the aerodrome terminal, tower, hangars, and other miscellaneous buildings on the aerodrome surface.  Based on the geometric complexity of these objects, they are not traditionally surveyed, or in some cases, only the corners are surveyed.  Future applications, particularly those with regard to efficiency and routing applications, will require detailed models of these geometric elements.  Therefore, the following requirement is asserted: 

3.11.2.1 
Aerodrome structures shall be modeled with a two-dimensional or three-dimensional bounding polygon. The feature attribute ―elev‖ shall indicate the highest point on the building extent. An example is shown in Figure 3-3. Towers and antennas protruding from the top of the building shall be captured as vertical objects. 
 
This Page Intentionally Left Blank 

## 4 Specific Requirements

This section provides specific requirements for AMDB content, capture rules, relationships, and quality. 

## 4.1 Geometry 4.1.1 Geometrical Primitives

4.1.1.1 
For the purpose of this document, geometries shall be described by points, lines, and polygons. 
4.1.1.2 
Geometrical representations shall ensure compliance with accuracy requirements (e.g. for a curve represented by a line, the density of the points shall be sufficient to meet the accuracy requirement of the feature). 
 
A point is the smallest unit of geometry and has no spatial extent. Points are described by two-dimensional (2-D) or three-dimensional (3-D) coordinates. 
 
A line consists of a connected sequence of points. Start- and end-points of a line are referred to as start- and end-node. Connecting points that are in between start- and endnodes are referred to as vertices. A start-node and an end-node define a line's directionality. A connection between a node and a vertex or between vertices is a straight line.  
A polygon is a surface described by a closed line (i.e. a line whose start-node and endnode are coincident). The closed line forms the outer edge of the surface. The inside of the polygon is defined by the left side in the order of vertices. The symbols listed in Table 4-1 are used to represent the three geometrical primitives. The symbols shown in Table 4-2 are used to represent the applicable geometric relationships. These representations do not imply any additional constraint requirements on the level of the geometry itself. Recommended geometrical constraints are listed in Table 4.3 and Section 4.1.2.11. 

## 4.1.2 Geometrical Constraints

Geometrical constraints ensure connectivity between features on a spatial level. Compliance to geometrical constraints leads to graphical consistency of AMDB features with respect to the spatial connections observed in the real world. Generic geometrical constraints are applicable to all AMDB features of each geometry base type i.e. point, line, or polygon. 

| Symbol    |
|-----------|
|           |
| Point     |
|           |
| Line      |
| Polygon   |
|           |
|           |
| Symbol               | Geometries           |
|----------------------|----------------------|
| Relationship         |                      |
| Description          |                      |
| … is located at the  |                      |
| Point -              |                      |
| Polygon              | edge of …            |
|                      |                      |
| Point -              |                      |
| Polygon              |                      |
| … is contained in …  |                      |
|                      |                      |
|                      |                      |
| Point - Line         | … is located on …    |
|                      |                      |
| Line - Point         | … ends at …          |
| Line - Line          | … crosses …          |
|                      |                      |
| Line - Line          |                      |
| … starts/ends at the |                      |
| edge of …            |                      |
|                      |                      |
|                      |                      |
| Line - Line          | …. is connected to … |
|                      |                      |
| Line - Line          | …. overlaps …        |
| Symbol               | Geometries       |
|----------------------|------------------|
| Relationship         |                  |
| Description          |                  |
| Line - Line          | …is attached to… |
|                      |                  |
| Line -               |                  |
| Polygon              |                  |
| … is contained in …  |                  |
|                      |                  |
| Line - Polygon       |                  |
| … intersects         | …                |
|                      |                  |
|                      |                  |
| Line - Polygon       | … crosses …      |
|                      |                  |
|                      |                  |
| … starts/ends at the |                  |
| Line -               |                  |
| Polygon              | edge of ...      |
|                      |                  |
| Line -               |                  |
| Polygon              |                  |
| … is attached to …   |                  |
|                      |                  |
| Polygon -            |                  |
| Polygon              |                  |
| … is contained in …  |                  |
|                      |                  |
| Polygon -            |                  |
| Polygon              |                  |
| … overlaps …         |                  |
|                      |                  |
| Polygon -            |                  |
| Polygon              |                  |
| … is attached to …   |                  |
|                      |                  |

4.1.2.1 
Features that are attached to each other shall share all mutually co-incident vertices. This 
shall be applied for features of the same feature class and for features of different feature classes. Examples are given in Figure 4-1. In Figure 4-1, the square symbols indicate start- and end-nodes. The triangle symbols indicate vertices between start- and endnodes. 
4.1.2.2 
Polygon features that are attached to each other and line features that are connected to each other and that have the same characteristics shall be represented by a unique object as long as not specified differently in this section of the document.  
4.1.2.3 
For connected lines (e.g. taxi-lines), the end-node of the first line and the start-node of the next line shall have identical (coincident) coordinates (see Figure 4-2). This shall be applied for features of the same feature class (e.g. TaxiwayGuidanceLines) and for features of different feature classes (e.g. TaxiGuidanceLine - RunwayExitLine). 
4.1.2.4 
No two line features shall overlap. 
4.1.2.5 
Any line feature that intersects with a polygonal feature shall include a vertex at the intersection point. See Figure 4-3. 

## Figure 4-3 Line Feature Intersecting Polygonal Feature

 4.1.2.6 
Geospatial locations of the start-node and end-node of a series of lines that form a polygon shall be identical (coincident). 
4.1.2.7 
All polygons shall be captured in a counter clockwise order. See Figure 4-4.  
 

## Figure 4-4 Ordering Of Polygon Vertices

 

4.1.2.8 
Polygons of the same feature class shall not overlap or be contained within each other. 
4.1.2.9 
Polygons of different feature classes shall not overlap with or be contained within other polygons 
except 
for 
RunwayMarkings, 
FrequencyAreas, 
ConstructionAreas, 
TouchDownLiftOffArea, FinalApproachAndTakeOffArea, Deicing Area, Hotspot, and 
Service Roads. 
4.1.2.10 
No curves, parameterized curves, and/or polygons that overlap themselves shall be used. 
Table 4-3 gives an overview of the recommended spatial connections between AMDB objects. Geometrical connections are only applicable if both connected objects exist in the AMDB and if the geometrical connections are observable in the real world. Rules are included in this document if they apply to the majority of feature connections in the real world. These rules are those expressed via the black cells in Table 4-3. The number in each black cell is a reference to the associated rule described further in this section. All potential geometrical connections are defined as equivalence relationships. Consequently, Table 4-3 is symmetrical. The feature names given in Table 4-3 are defined in Section 4.3. Note: optional features are not included in Table 4-3 

4.1.2.11 
 
The following rules for feature-specific geometrical constraints apply: 
 
A **RunwayIntersection** feature should be attached to all corresponding RunwayElement features (Rule 1). 

A **RunwayDisplacedArea** feature should be attached to the corresponding RunwayElement feature (Rule 2). A **RunwayShoulder** feature should be attached to the corresponding **RunwayElement** feature and/or **RunwayIntersection** feature and/or **RunwayDisplacedArea** feature and/or **Stopway** feature and/or **RunwayShoulder** feature and/or **RunwayMarking** feature and/or **Blastpad** feature (Rule 3). A **Stopway** feature should be attached to the corresponding **RunwayElement** feature or RunwayIntersection feature or **RunwayDisplacedArea** feature (Rule 4). A **RunwayMarking** feature should be contained in a **RunwayElement** feature and/or a RunwayDisplacedArea feature and/or a **Stopway** feature and/or a RunwayIntersection feature and/or **Blastpad** feature (Rule 5). A **TaxiwayElement** feature adjacent to a RunwayElement should be attached to the corresponding **RunwayElement** feature (Rule 6). A **RunwayMarking** feature which composes the runway designation (e.g. 0, 4, 6, 8, and 9 numbers) shall be attached to other **RunwayMarking** features that compose the same runway designation (Rule 7). See Figure 4-5. 

## Figure 4-5 Example Geometries For "0" Runway Marking

A **RunwayDisplacedArea** feature should be attached to an adjacent **TaxiwayElement** 
feature (Rule 8). 

A **LandAndHoldShortOperationLocation** feature should start and end at the edge of the corresponding **RunwayElement** feature (Rule 9). An **ArrestingGearLocation** feature should cross the corresponding **RunwayElement** feature and/or **RunwayDisplacedArea** feature and/or **Stopway** feature (Rule 10). A **PaintedCenterline** feature should cross all corresponding **RunwayElement** features and/or **RunwayIntersection** features (Rule 11). A **PaintedCenterline** feature should start/end at the edge of a corresponding RunwayDisplacedArea feature and/or the corresponding **Stopway** feature (Rule 12). A Runway**Exitline** feature should intersect the corresponding **RunwayElement** feature and/or **RunwayDisplacedArea** feature (Rule 13). 

A **RunwayThreshold** feature should be located at the edge of the corresponding RunwayElement feature and/or **RunwayDisplacedArea** feature and/or **Stopway** feature 
(Rule 14). 

A **TaxiwayElement** feature should be attached to all corresponding TaxiwayElement features (Rule 15). 

A **TaxiwayShoulder** feature should be attached to all corresponding TaxiwayElement features (Rule 16). 

An **ApronElement** feature should be attached to all corresponding TaxiwayElement features (Rule 17). 

A **ParkingStandArea** feature should be attached to all corresponding TaxiwayElement features (Rule 18). 

A **DeicingArea** feature should be attached to all adjacent **TaxiwayElement** features 
(Rule 19). 

A **TaxiwayGuidanceLine** feature should be contained in the corresponding TaxiwayElement feature (Rule 20). 

A 
TaxiwayIntersectionMarking feature should intersect the corresponding TaxiwayElement feature (Rule 21). A **TaxiwayHoldingPosition** feature should be attached to the corresponding TaxiwayElement feature and not intersect the corresponding **TaxiwayElement** feature 
(Rule 22). 

A **RunwayExitLine** feature should intersect the corresponding **TaxiwayElement** feature 
(Rule 23). 

A **StandGuidanceLine** feature should intersect the corresponding TaxiwayElement feature (Rule 24).  
A **TaxiwayShoulder** feature should be attached to all corresponding TaxiwayShoulder features (Rule 25). 

An **ApronElement** feature should be attached to all corresponding ApronElement features (Rule 26). 

A **ParkingStandArea** feature should be attached to all corresponding ApronElement features (Rule 27). 

A **DeicingArea** feature should be attached to all adjacent **ApronElement** features (Rule 
28). 

A **VerticalPolygonStructure** feature should be attached to the corresponding ApronElement features (Rule 29). A **TaxiwayGuidanceLine** feature should be contained in the corresponding ApronElement features (Rule 30). 

A **StandGuidanceLine** feature should be contained in the corresponding ApronElement feature (Rule 31). 

A **ParkingStandLocation** feature should be contained in the corresponding ApronElement feature (Rule 32). 

A 
ParkingStandArea feature should be attached to all corresponding ParkingStandArea features (Rule 33). 

A 
StandGuidanceLine feature should intersect with the corresponding ParkingStandArea feature (Rule 34). A **ParkingStandLocation** feature should be contained in the corresponding ParkingStandArea feature (Rule 35). 

A **DeicingArea** feature should be attached to all corresponding **DeicingArea** features 
(Rule 36). 

A **TaxiwayGuidanceLine** feature should intersect the corresponding DeicingArea feature (Rule 37). 

A **StandGuidanceLine** feature should intersect with the corresponding DeicingArea feature (Rule 38). 

A **ParkingStandLocation** feature should be contained in the corresponding DeicingArea feature (Rule 39). A **TouchDownLiftOffArea** feature should be contained in the corresponding FinalApproachAndTakeOffArea feature (Rule 40). A **HelipadThreshold** feature should be located at the edge of the corresponding FinalApproachAndTakeOffArea. feature (Rule 41). A **HelipadThreshold** feature should be located at the edge of the corresponding TouchDownLiftOffArea feature (Rule 42). An **ArrestingGearLocation** feature should cross a **PaintedCenterline** feature (Rule 43). A **LandAndHoldShortOperationLocation** feature should cross a **PaintedCenterline** 
feature (Rule 44). 

A **RunwayExitLine** feature should start/end at the edge of a **PaintedCenterline** feature 
(Rule 45). 

A **PaintedCenterline** feature should end at a **RunwayThreshold** feature (Rule 46). A **TaxiwayIntersectionMarking** feature should cross a **TaxiwayGuidanceline** feature 
(Rule 47). A 
TaxiwayGuidanceline feature should start/end at the edge of a TaxiwayHoldingPosition feature (Rule 48). 

A 
RunwayExitLine feature should be connected to a corresponding TaxiwayGuidanceline feature (Rule 49). 

A 
StandGuidanceLine feature should be connected to a corresponding TaxiwayGuidanceline feature (Rule 50). A **RunwayExitLine** feature should start/end at the edge of a **TaxiwayHoldingPosition** 
feature (Rule 51). 

A **StandGuidanceLine** feature should end at a **ParkingStandLocation** feature (Rule 
52). 

A **Blastpad** feature should be attached to the corresponding **RunwayElement** feature or RunwayIntersection feature or **Stopway** feature or **RunwayDisplacedArea** feature 
(Rule 53). 

## 4.2 Attributes 4.2.1 Completeness

4.2.1.1 
For each feature, all of the attributes defined in Section 4.3 shall be provided.  If a particular attribute is ―null,‖ ―unknown,‖ ―not entered,‖ or ―not applicable‖, it shall be listed as such.  

## 4.2.2 Attribute Names

4.2.2.1 
All attribute names shall be constrained as follows: no duplicate names, only lower-case letters from ASCII code, and maximum eight letters. 

## 4.2.3 Supplemental Features And Their Attribution

Supplemental features are features that may be provided in an AMDB that are beyond the minimum set defined in this document. For supplemental features, the following types of information should be provided: name, description, survey method, geometry type, and attribute list. For a supplemental feature, those attributes which are generic to all features should be provided. These include, for example, feattype, idarpt, idnumber, source, integr and revdate. In addition, similar attributes for similar features should be provided. These include, for example, vacc, hacc, vres, hres. For each attribute, a name and description should be provided.  

## 4.2.4 Supplemental Attributes For Feature Catalogue

Supplemental attributes are attributes that may be provided in an AMDB that are beyond the defined set for the features in this document. 

## 4.2.5 Feature Attribute Functional Requirements

Functional constraints shall be used to ensure connectivity between features on a functional level (e.g. runway elements linked with the corresponding runway threshold).  
Specific functional constraint requirements follow. 

4.2.5.1 
Each AMDB feature shall provide the identical **idarpt (**Aerodrome Reference Point) 
object identifier value. 
4.2.5.2 
Every entity of an AMDB feature type shall have an equal feattype value. 
4.2.5.3 
All AMDB features shall be located within 20 km of the Aerodrome Reference Point. 
4.2.5.4 
Table 4-4 describes all functional connections that shall be applied for AMDB objects. The number in the black cells references an associated rule described later in this section. All functional connections are defined as equivalence relationships. Consequently, Table 4-4 is symmetrical. 
4.2.5.5 
The object identifier attributes shall be encoded according to the rules of the EUROCAE ED-119A/RTCA DO-291A feature catalogue. 
 
Note: optional features are not included in Table 4-4 
4.2.5.6 
The following rules for feature-specific functional constraints apply: 
 
 
Each **RunwayElement** feature's attribute **idrwy** shall provide the **idrwy** object 
identifier value corresponding to the name of the real world runway (Rule 1). 
 
Each **RunwayIntersection** feature's attribute **idrwi** shall provide an **idrwi** object 
identifier value that corresponds to the names of the real world intersection runways (idrwy) (Rule 2). 
 
Each **RunwayShoulder** feature's attribute **idrwy** shall provide the **idrwy** object 
identifier value of the real world runway (Rule 3). 
 
Each **RunwayMarking** feature's attribute **idrwy** shall provide the **idrwy** object 
identifier value of the real world runway (Rule 4). 
 
If the **LandAndHoldShortOperationLocation** feature protects a runway, the value of a **LandAndHoldShortOperationLocation** feature's attribute idp shall be identical to the **idrwy** object identifier value of the protected real world runway (Rule 
5). 
 
The value of a **TaxiwayHoldingPosition** feature's attribute idp shall be identical to the **idrwy** object identifier value of the protected real world runway (Rule 6). 
 
Each **RunwayDisplacedArea** feature's attribute **idthr** shall provide the **idthr** object identifier value of the operationally corresponding **RunwayThreshold** (Rule 7). 
 
Each **Stopway** feature's attribute **idthr** shall provide the **idthr** object identifier value of the operationally corresponding **RunwayThreshold** (Rule 8). 
 
Each **TaxiwayElement** feature's attribute **idlin** shall provide the **idlin** object 
identifier value corresponding to the name of the real world taxiway (Rule 9). 
 
The value of a **TaxiwayGuidanceLine** feature's attribute **idlin** shall be identical to the value of the corresponding **TaxiwayElement** feature's attribute **idlin** (Rule 10).  
 
The value of a **TaxiwayIntersectionMarking** feature's attribute **idlin** shall be identical to the value of the corresponding **TaxiwayElement** feature's attribute **idlin** 
(Rule 11). 
 
The value of a **TaxiwayHoldingPosition** feature's attribute **idlin** shall be identical to the value of the corresponding **TaxiwayElement** feature's attribute **idlin** (Rule 12). 
 
Each **ParkingStandArea** feature's attribute **idstd** shall provide an **idstd** object identifier value that holds the **idstd** object identifier values of all corresponding ParkingStandLocations (Rule 13). 
 
Each **FinalApproachAndTakeOff** feature's attribute **idrwy** shall provide the **idrwy** object identifier value of the corresponding **TouchDownAndLiftOff** (Rule 14). 
 
Each **FinalApproachAndTakeOff** feature's attribute **idrwy** shall provide the **idthr** object identifier value of the corresponding **HelipadThreshold** (Rule 15). 
 
The value of an **ArrestingGearLocation** feature's attribute **idthr** shall be identical to the value of its operationally corresponding **RunwayThresholds** feature's attribute idthr (Rule 16). 
The value of a **PaintedCenterline** feature's attribute **idrwy** shall be identical to the value of the corresponding real world runway. (Rule 17). 

 
The value of a **LandAndHoldShortOperationLocation** feature's attribute **idthr** 
shall be identical to the value of the operationally corresponding **RunwayThresholds** feature's attribute **idthr** (Rule 18). 
 
The value of a **RunwayExitLine** feature's attribute **idlin** shall be identical to the value of every connecting **TaxiwayGuidanceLine** feature's attribute **idlin**, in case they are located on the same corresponding **TaxiwayElement** or if multiple adjacent TaxiwayElements share the same attribute's value **idlin** (Rule 19). 
 
Deleted rule 20. 
 
Deleted rule 21. 
 
Each **StandGuidanceLine** feature's attribute **idstd** shall provide object identifier values for all corresponding **ParkingStandLocations** (Rule 22). 
The value of a **ParkingStandArea** feature's attribute **idapron** shall be identical to the value of the operationally corresponding **ApronElement** feature's attribute idapron (Rule 23). The value of a **TaxiwayElement** feature's attribute **idapron** shall be identical to the value of the operationally corresponding **ApronElement** feature's attribute idapron (Rule 24). The value of a **ParkingStandArea** feature's attribute **idapron** shall be identical to the value of the operationally corresponding **TaxiwayElement** feature's attribute idapron (Rule 25). The value of a **DeicingArea** feature's attribute **idbase** shall be identical to the value of the underlying **ApronElement** feature's attribute **idapron** (Rule 26). The value of a **DeicingArea** feature's attribute **idbase** shall be identical to the value of the underlying **TaxiwayElement** feature's attribute **idlin** (Rule 27). The value of a **DeicingArea** feature's attribute **idbase** shall be identical to the value of the underlying **ParkingStandArea** feature's attribute **idstd** (Rule 28). 

Deleted rule 29. 

Each **Blastpad** feature's attribute **idthr** shall provide the **idthr** object identifier value of the operationally corresponding **RunwayThreshold** (Rule 30). In some particular cases, functional connections may not be complete regarding certain real world constraints (e.g. missing paint), therefore, these connections may not be applicable and mandatory to all functions using this data. 

 

## 4.3 Data Elements

 
For the purposes of this document, data elements have been listed by class.  The nine classes are runways, helipads, taxiways, aprons, vertical structures, construction areas, water, surface lighting and quality data.  Each class requires that different objects be captured in the AMDB. Supplemental data classes that have not been specified but may be useful to some applications include, for example, INS/VOR checkpoints, noise abatement zones, special use areas, signage, and aerodrome boundaries. 

4.3.0.1  
AMDB features and attributes shall be encoded according the rules of the EUROCAE ED-119A/RTCA DO-291A feature catalogue. 
4.3.0.2 
AMDB features and attributes shall be mandatory if not otherwise stated. 

## 4.3.1 Runways

An overview of runway data elements is shown in Figure 4-6. 

 

## 4.3.1.1 Runway Elements

Definition: 
Part of a runway. 
Description: 
A runway element may consist of one or more polygons not defined as other portions of the runway class (e.g. stopway) 
4.3.1.1.1 
Data Capture Rule:  
All runway elements shall be individual objects in the database.   

The runway element is delimited by the outer edge of the white runway edge painting. 

4.3.1.1.2 
Runway elements shall include any portion of a runway not otherwise identified as an intersection, threshold, marking, centerline, LAHSO location, arresting gear location, shoulder, stopway, displaced area, or exit line.  
 
Feature Name:  
RunwayElement 
Geometry: 
 
Polygon 
Attributes: 
(1) 
feattype  
Runway feature type identifier 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idrwy  
Object identifier 
(5) 
vacc  
 
Vertical accuracy as a Linear Error Probability (LEP) 
(6) 
hacc  
Horizontal accuracy as a Circular Error Probability (CEP) 
(7) 
vres  
 
Vertical resolution of coordinates 
(8) 
hres  
 
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr 
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
 
Last revision date of data 
(12) 
pcn  
A number expressing the bearing strength of a pavement for 
unrestricted operations. If multiple pcn's exist for a given 
feature, the lowest value (i.e. most restricted) shall be provided. 
(13) 
restacn 
Usage restriction (prohibited) for  specified aircraft type according to ICAO-ACN (Aircraft classification number). Encoding: Aircraft type according ICAO-ACN (Aircraft classification number). If there is more than one aircraft-type 
restriction, the different types should be divided by a ".". Example: 747-400 and A 380 at one location: B744.A380 
(14) 
width   
Minimal width of the feature 
(15) 
length   
Length of feature 
(16) 
surftype 
Predominant surface type 

## 4.3.1.2 Runway Intersections

Definition: 
Intersecting area shared by two or more runways. 
Description: 
The runway intersection feature is the common area of intersecting runways. 
Data Capture Rule:  
The runway intersection polygon is delimited by the outer edge of the white runway edge painting or surface edge if no marking is present, excluding runway shoulders.  
4.3.1.2.1 
When two or more runways intersect, the intersection shall be kept as an individual object in the database.  
4.3.1.2.2 
All runway intersections shall be captured as individual objects. 
Feature Name:  
RunwayIntersection 
Geometry: 
 
Polygon 
Attributes: 
(1) 
feattype 
 
Runway intersection feature type identifier 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt 
ICAO aerodrome location indicator 
(4) 
idrwi 
 
Object identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
 
Vertical resolution of coordinates 
(8) 
hres  
 
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
 
Last revision date of data 
(12) 
pcn  
A number expressing the bearing strength of a pavement for unrestricted operations. If multiple pcn's exist for a given feature, the lowest value (i.e. most restricted) shall be provided. 
(13) 
restacn 
Usage restriction (prohibited) for  specified aircraft type according to ICAO-ACN (Aircraft classification number). Encoding: Aircraft type according ICAO-ACN (Aircraft classification number). If there is more than one aircraft-type restriction, the different types should be divided by a ".". Example: 747-400 and A 380 at one location: B744.A380 
(14) 
surftype 
Predominant surface type 

## 4.3.1.3 Runway Thresholds

| Definition:    |
|----------------|
| for landing.   |

Description: 
See definition: ICAO Annex 14, Chapter 1 
4.3.1.3.1 
Data Capture Rule:  
All runway thresholds shall be individual objects in the database.  
4.3.1.3.2 
All runway information that is related to a landing direction shall be attached to the corresponding threshold.   
4.3.1.3.3 
The threshold points shall be captured in three dimensions and located according ICAO Doc 9674 (WGS84)-Manual, Chapter 5.  
Feature Name:  
RunwayThreshold 
Geometry: 
 
Point 
Attributes: 
(1) 
feattype  
feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idthr 
 
Object identifier 
(5) 
status 
State of feature exceeding one or more AIRAC cycles (e.g. runway 25 closed)  
(6) 
vacc  
 
Vertical accuracy as a LEP 
(7) 
hacc 
Horizontal accuracy as a CEP 
(8) 
vres  
 
Vertical resolution of coordinates 
(9) 
hres  
 
Horizontal resolution of coordinates 
(10) 
source 
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(11) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(12) 
revdate  
 
Last revision date of data 
(13) 
tdze  
Touchdown zone elevation (ICAO Annex 14, Chapter 1.1) 
(14) 
tdzslope  
Touchdown zone longitudinal slope  (slope of 1/3 of the runway length from threshold or first 3000 feet for runways longer than 9000 feet)  
(15) 
brngtrue  
True runway bearing  (ICAO Annex 14, Chapter 3.1.12) 
(16) 
brngmag  
Magnetic runway bearing  valid at the day of data generation 
(17) 
rwyslope  
Runway slope  
(18) 
tora  
Takeoff run available (ICAO Annex 14, Chapter 1.1)  
(19) 
toda 
Takeoff distance available (ICAO Annex 14, Chapter 1.1)  
(20) 
asda  
Accelerate-stop distance available. (ICAO Annex 14, Chapter 1.1)  
(21) 
lda  
Landing distance available (ICAO Annex 14, Chapter 1.1)  
(22) 
vasis 
Vertical guidance lighting system available . 
(23) 
cat  
Type and Category of precision approach guidance system available 
(24) 
ellipse 
Height above/below the WGS-84 ellipsoid at the threshold position.  
(25) 
geound 
Geoidal undulation of threshold in reference to EGM 96 
(26) 
thrtype  
Type of threshold (e.g. displaced) 

## 4.3.1.4 Runway Markings

Definition: 
A symbol or group of symbols displayed on the surface of the runway in order to convey aeronautical information. 

| Description:                                           |
|--------------------------------------------------------|
| runway centerline marking, threshold marking, traverse |

stripes, touchdown zone marking, and runway side stripe marking. See definition: ICAO Annex 14, Chapter 1.1 

4.3.1.4.1 
Data Capture Rule:  
The outline of markings painted on runways shall be 
individual objects in the database.   
Use outer edges of contours of white markings painted on runway. The runway marking feature consists of multiple polygons forming the overall runway marking.  

Feature Name:  
RunwayMarking 
Geometry: 
 
Polygon 
Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idrwy  
Object identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
 
Vertical resolution of coordinates 
(8) 
hres  
 
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
 
Last revision date of data 

## 4.3.1.5 Painted Centerlines

Definition: 
Continuous line captured along the painted line in the center of a runway connecting the two thresholds. 
Description: 

4.3.1.5.1 
Data Capture Rule:  
 All centerlines shall be individual objects in the database.  
 
The centerline should provide data in all three dimensions. 
The line representing the centerline feature should be located in the center of the real-world centerline. 

Feature Name:  
PaintedCenterline 
Geometry: 
 
Line 
Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idrwy  
Object Identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
 
Vertical resolution of coordinates 
(8) 
hres  
 
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
 
Last revision date of data 

## 4.3.1.6 Land And Hold Short Operations (Lahso) Locations

Definition: 
Location of marking used for Land and Hold Short Operations  (LAHSO). 

Description: 
These runway operations include landing and holding short of an intersecting runway, an intersecting taxiway, or on some other designated point on a runway other than an intersecting runway or taxiway.  
 

4.3.1.6.1 
Data Capture Rule:  
All LAHSO locations shall be individual objects in the database.   
4.3.1.6.2 
The lines shall be captured along the outer edge (away from intersecting runway/taxiway) of the LAHSO line as painted on the runway or marked by other means (e.g. lighting). 
Feature Name:  
LandAndHoldShortOperationLocation 
Geometry: 
 
Line 
Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idthr 
 
Object identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
 
Vertical resolution of coordinates 
(8) 
hres  
 
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
idp  
Object identifier of runway or taxiway being protected 

## 4.3.1.7 Arresting Gear Locations

Definition: 
Location of the arresting gear cable across the runway. 
Description: 
Generally consists of pendant cables supported over the runway surface by rubber ―doughnuts‖. Although most devices are located in the overrun areas, a few of these arresting systems have cables stretched over the operational areas  near the ends of a runway. See Figure 4-7. 

## 

 4.3.1.7.1 
Data Capture Rule:  
All arresting gear locations shall be individual objects in the database.   
4.3.1.7.2 
The line shall connect the two fixed points of any arresting gear cables on each side of a runway. 
Feature Name:  
ArrestingGearLocation 
Geometry: 
 
Line 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idthr 
 
Object identifier 
(5) 
status  
State of feature exceeding one or more AIRAC cycles 
(6) 
vacc  
Vertical accuracy as a LEP 
(7) 
hacc  
Horizontal accuracy as a CEP 
(8) 
vres  
Vertical resolution of coordinates 
(9) 
hres  
Horizontal resolution of coordinates 
(10) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(11) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(12) 
revdate  
Last revision date of data 

## 4.3.1.8 Runway Shoulders

| Definition:                                                  |
|--------------------------------------------------------------|
| prepared as to provide a transition between the pavement and |
| the adjacent surface.                                        |

Description: 
See definition: ICAO Annex 14, Chapter 1.1 
4.3.1.8.1 
Data Capture Rule:  
All runway shoulders shall be individual objects in the database.  

The runway shoulder should exclude the white runway edge painting. It typically consists of multiple polygons forming the overall shoulder on each side of the runway.  

Feature Name:  
RunwayShoulder 
Geometry: 
Polygon.  
Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idrwy  
Object Identifier 
(5) 
status 
State of feature exceeding one or more AIRAC cycles 
(6) 
vacc  
Vertical accuracy as a LEP 
(7) 
hacc  
Horizontal accuracy as a CEP 
(8) 
vres  
Vertical resolution of coordinates 
(9) 
hres  
Horizontal resolution of coordinates 
(10) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(11) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(12) 
revdate  
Last revision date of data 
(13) 
gsurftyp 
Generic surface type (e.g. concrete) 

## 4.3.1.9 Stopways

Definition: 
A defined rectangular area on the ground at the end of takeoff run available prepared as a suitable area in which an aircraft can be stopped in the case of an abandoned takeoff Description: 
See definition: ICAO Annex 14, Chapter 1.1 

4.3.1.9.1 
Data Capture Rule:  
Each stopway of a runway shall be an individual object in the database.  
If a painted line separates a shoulder from the stopway then the shoulder should be part of the stopway polygon. Note: Stopway shoulders do not exist.  
Feature Name:  
Stopway Geometry: 
 
Polygon Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idthr 
 
Object identifier 
(5) 
status  
State of feature exceeding one or more AIRAC cycles 
(6) 
vacc  
Vertical accuracy as a LEP 
(7) 
hacc   
Horizontal accuracy as a CEP 
(8) 
vres  
Vertical resolution of coordinates 
(9) 
hres  
Horizontal resolution of coordinates 
(10) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(11) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(12) 
revdate  
Last revision date of data 
(13) 
surftype 
Predominant surface type 

## 4.3.1.10 Runway Displaced Areas

Definition: 
That portion of a runway between the beginning of the runway and the displaced threshold. 

Description: 

4.3.1.10.1 
Data Capture Rule:  
Each runway displaced area shall be an individual object in the database.   
4.3.1.10.2 
A runway displaced area shall not include the runway shoulders.  
Feature Name:  
RunwayDisplacedArea 
 
Geometry: 
 
Polygon 
Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idthr  
 
Object identifier 
(5) 
status  
State of feature exceeding one or more AIRAC cycles 
(6) 
vacc  
Vertical accuracy as a LEP 
(7) 
hacc  
Horizontal accuracy as a CEP 
(8) 
vres  
Vertical resolution of coordinates 
(9) 
hres  
Horizontal resolution of coordinates 
(10) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(11) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(12) 
revdate  
Last revision date of data 
(13) 
pcn 
A number expressing the bearing strength of a pavement for 
unrestricted operations. If multiple pcn's exist for a given 
feature, the lowest value (i.e. most restricted) shall be provided. 
(14) 
restacn 
Usage restriction (prohibited) for  specified aircraft type according to ICAO-ACN (Aircraft classification number). Encoding: Aircraft type according ICAO-ACN (Aircraft classification number). If there is more than one aircraft-type restriction, the different types should be divided by a ".". Example: 747-400 and A 380 at one location: B744.A380 
(15) 
surftype  
Predominant surface type 

## 4.3.1.11 Blastpad

| Definition:                                                    | Specially prepared surface placed adjacent to the end of a    |
|----------------------------------------------------------------|---------------------------------------------------------------|
| runway to eliminate the erosive effect of the high wind forces |                                                               |
| produced by airplanes at the beginning of their takeoff roll.  |                                                               |
| Description:                                                   | Areas in extension of runways or stopways. These areas are    |
| usually covered by chevrons. Blastpads may not be used for     |                                                               |
| taxiing, landing or takeoff. (Ref. FAA AC150/5300-18A)         |                                                               |

 
Data Capture Rule:  
Use the outer edge of the blastpad surface.  
Feature Name:  
Blastpad 
Geometry: 
 
Polygon 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idthr 
 
Object identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
 
Horizontal accuracy as a CEP 
(7) 
vres  
 
Vertical resolution of coordinates 
(8) 
hres  
 
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 

## 4.3.1.12 Runway Exit Lines

| Definition:    | Guidance line painted on the runway exit.                     |
|----------------|---------------------------------------------------------------|
| Description:   | Painted line leading from the runway to a taxiway to exit the |
| runway.        |                                                               |

4.3.1.12.1 
Data Capture Rule:  
Runway exit lines shall be individual objects in the database and shall start/end at the first intersection of the exit line with any other taxiway guidance line at the edge of the Taxiway Holdingposition. 

The endpoint of the runway exit line should be the startpoint of a connecting taxiline. 

Feature Name:  
RunwayExitLine 
Geometry: 
 
Line 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idlin 
 
Object identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 
(9) 
source  
  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
status  
State of feature exceeding one or more AIRAC cycles 
(13) 
color  
Color specifying the color of the taxiline  
(14) 
style  
Style specifying the line property of the taxiline (e.g. dashed or solid) 
(15) 
direc  
Directionality of corresponding taxiway 

## 4.3.2 Helipads

As shown in Figure 4-8, helipad information consists of the final approach and takeoff area (FATO), the touchdown/lift-off area (TLOF), and the helipad threshold location (ICAO Doc 9674 WGS84-Manual, Chapter 5 Attachment C). A helipad can consist of multiple polygons. 

## 4.3.2.1 Final Approach And Take Off Areas (Fatos)

| Definition:    | The beginning of that portion of the helipad that is available    |
|----------------|-------------------------------------------------------------------|
| for landing.   |                                                                   |
| Description:   | See definition: ICAO Doc 9674 WGS84-Manual, Chapter 5             |
| Attachment C   |                                                                   |

4.3.2.1.1 
Data Capture Rule:  
Final approach and takeoff areas (FATO) shall be included as individual objects in the database.  

The outer edge of the white FATO-marking should be used to represent the FATO. 

In case of an overlap of the FATO with another feature (eg. 

TLOF, Taxiway Element), overlapping of both polygons is allowed. 

Feature Name:  
FinalApproachAndTakeOffArea 
Geometry: 
 
Polygon.  
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO Aerodrome/Heliport identifier 
(4) 
idrwy  
Object identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
 
Vertical resolution of coordinates 
(8) 
hres  
 
Horizontal resolution of coordinates 
(9) 
source  
 
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
surftype 
Predominant surface type 

## 4.3.2.2 Touchdown/Lift-Off Areas (Tlofs)

| Definition:                                             | A load bearing area on which a helicopter may touchdown or    |
|---------------------------------------------------------|---------------------------------------------------------------|
| liftoff.                                                |                                                               |
| Description:                                            | See Definition: ICAO Doc 9674 WGS84-Manual, Chapter 5         |
| Attachment C. This is the touchdown/liftoff area of the |                                                               |
| helipad as specified by the marking.                    |                                                               |

4.3.2.2.1 
Data Capture Rule:  
Touchdown/lift-off areas (TLOF) shall be included as individual objects in the database.   

The outer edges of the white TLOF-markings should be used to represent the TLOF. 

In case of an overlap of the TLOF with another feature (eg. FATO, Taxiway Element), overlapping of both polygons is allowed. 

| Feature Name:     | TouchDownLiftOffArea    |
|-------------------|-------------------------|
| Geometry:         | Polygon                 |

Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO Aerodrome/Heliport identifier 
(4) 
idrwy  
Object identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
surftype 
Predominant surface type 

## 4.3.2.3 Helipad Thresholds

| Definition:    | Threshold of a helipad.                               |
|----------------|-------------------------------------------------------|
| Description:   | See Definition: ICAO Doc 9674 WGS84-Manual, Chapter 5 |
| Attachment C   |                                                       |

4.3.2.3.1 
Data Capture Rule:  
Helipad thresholds shall be included as individual objects in the database.  

Helipad-thresholds should be surveyed in all three dimensions. 

Feature Name:  
HelipadThreshold 
Geometry: 
 
Point 
Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO Aerodrome/Heliport identifier 
(4) 
idthr 
 
Object identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
status  
State of feature exceeding one or more AIRAC cycles  
(13) 
ellipse 
Height below/above the WGS-84 ellipsoid 
(14) 
geound 
Geoidal undulation of threshold in reference to EGM 96 

## 4.3.3 Taxiways

As shown in Figure 4-9 taxiways include runway exit taxiways and apron taxiways (see definition: ICAO Annex 14, Chapter 1.1). 

## 4.3.3.1 Taxiway Elements

| Definition:                                                    | Part of a taxiway.                                           |
|----------------------------------------------------------------|--------------------------------------------------------------|
| Description:                                                   | Elements of a taxiway include:  taxiway, apron taxiway,      |
| rapid exit taxiway, and aircraft stand taxilane surfaces as    |                                                              |
| defined in ICAO Annex 14.                                      |                                                              |
| 4.3.3.1.1                                                      | Data Capture Rule:                                           |
| be included as individual objects in the database.  Note:      |                                                              |
| Taxiway elements do not include taxiway shoulders and          |                                                              |
| aircraft parking/stand areas.                                  |                                                              |
| 4.3.3.1.2                                                      | Each taxiway element polygon shall describe the surface of a |
| single taxiway.  A single taxiway is an area identified by the |                                                              |
| same name.  A single taxiway shall be split in those areas     |                                                              |
| where two or more taxiway guidance lines lead into each        |                                                              |
| other. A separate taxiway element shall be provided            |                                                              |
| representing the intersection (Figure 4-10).                   |                                                              |

 The taxiway element polygon should be limited by the outer side of the taxiway edge marking. Taxiway holding positions should be coincident with the edges of two adjacent taxiway element polygons. 

4.3.3.1.3  
Taxiway intersection markings shall be coincident with the edges of two adjacent taxiway element polygons if the marking is less than 10m away from the intersection. See Figure 4-11. 
1
2
8
3
9
7
6

## 

Feature Name:  
TaxiwayElement Geometry: 
Polygon Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idlin 
 
Object identifier 
(5) 
idapron 
Name of apron. If the taxiway element is located on an apron, the name of the apron shall be indicated. If the taxiway is not located on an apron, then ‗Not Applicable' shall be indicated. See Figure 4-12. 
(6) 
vacc  
 
Vertical accuracy as a LEP 
(7) 
hacc  
Horizontal accuracy as a CEP 
(8) 
vres  
Vertical resolution of coordinates 
(9) 
hres  
Horizontal resolution of coordinates 
(10) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(11) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(12) 
revdate  
Last revision date of data 
(13) 
gsurftyp 
Generic surface type (e.g. concrete) 
(14) 
bridge 
Taxiway is either an underpass or an overpass 
(15) 
pcn  
A number expressing the bearing strength of a pavement for unrestricted operations. If multiple pcn's exist for a given feature, the lowest should be used. 
(16) 
restacn 
Usage restriction (prohibited) for  specified aircraft type according to ICAO-ACN (Aircraft classification number). Encoding: Aircraft type according ICAO-ACN (Aircraft classification number). If there is more than one aircraft-type restriction, the different types should be divided by a ".". Example: 747-400 and A 380 at one location: B744.A380 
 

## 4.3.3.2 Taxiway Shoulders

Definition: 
An area adjacent to the edge of a taxiway pavement so prepared as to provide a transition between the pavement and the adjacent surface. 
Description: 
Taxiway shoulders are separate from, but connected to, the taxiway edge marking. See definition: ICAO Annex 14, Chapter 1.1 

4.3.3.2.1 
Data Capture Rule:  
Taxiway shoulders shall be included as individual objects in the database.  
The taxiway shoulder polygon should exclude the taxiway edge marking. It can consist of multiple polygons forming the overall taxiway shoulder. 

Feature Name:  
TaxiwayShoulder 
Geometry:   
 
Polygon. 
 
Attributes: 
(1) 
feattype  
Feature type 

(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 

(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
status  
State of feature exceeding one or more AIRAC cycles 
(5) 
vacc  
Vertical accuracy as a LEP 
(6) 
hacc  
 
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 

(9) 
source   
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 

(11) 
revdate  
Last revision date of data 
(12) 
gsurftyp 
Generic surface type (e.g. concrete) 

## 4.3.3.3 Taxiway Guidance Lines

Definition: 
Guidance line painted on a taxiway. 

Description: 
Taxiway guidance lines (taxilines) are referred to in ICAO Doc. 9157 as taxiway centerlines. See definition: ICAO Annex 14, Chapter 5.2.8 
4.3.3.3.1 
Data Capture Rule:  
Guidance lines painted on a taxiway shall be included as individual objects in the database.   
4.3.3.3.2 
Each taxiway guidance taxiline object in the database shall be a continuous line sharing the start or end node of at least two connecting taxiway guidance taxiline objects except if one or both ends represent the end of the painted taxiline.   
4.3.3.3.3 
Taxiway guidance lines shall exclude exit lines and aircraft stand guidance taxilines.  
4.3.3.3.4 
For connecting taxilines, the endpoint of one of the taxiline objects shall be the starting point of the next one as shown in Figure 4-13. 
 

Feature Name:  
TaxiwayGuidanceLine 
Geometry: 
Line 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idlin 
 
Object identifier 
(5) 
status  
State of feature exceeding one or more AIRAC cycles 
(6) 
vacc  
Vertical accuracy as a LEP 
(7) 
hacc  
Horizontal accuracy as a CEP 
(8) 
vres  
Vertical resolution of coordinates 
(9) 
hres  
Horizontal resolution of coordinates 
(10) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(11) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(12) 
revdate  
Last revision date of data 
(13) 
wingspan 
Maximum wingspan on taxiway 
(14) 
maxspeed 
Maximum speed on taxiway 
(15) 
color  
Color specifying the color of the taxiline 
(16) 
style  
Style specifying the line property of the taxiway guidance line (e.g. dashed or solid) 
(17) 
direc  
Directionality of taxiline (one-way or two-way) 

## 4.3.3.4 Taxiway Intersection Markings

| Definition:    | Taxiway intersection marking painted across a taxiway.    |
|----------------|-----------------------------------------------------------|
| Description:   | See definition: ICAO Annex 14, Chapter 5.2.10             |

4.3.3.4.1 
Data Capture Rule:  
Taxi intersection markings shall be individual objects in the database.   
4.3.3.4.2 
The line shall be located in the center of the painted ground marking. 
Feature Name:  
TaxiwayIntersectionMarking 
Geometry: 
Line 
Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idlin 
 
Object Identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 
(9) 
source  
 
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 

## 4.3.3.5 Taxiway Holding Positions

Definition: 
Taxiway holding position painted across a taxiway. 
Description: 
See definition of Runway holding position in ICAO Annex 14 
4.3.3.5.1 
Data Capture Rule:  
Taxiway holding positions shall be included as individual objects in the database.   
4.3.3.5.2 
The line shall be located at the outer edge of the painted ground marking away from the corresponding runway. 
Feature Name:  
TaxiwayHoldingPosition 
Geometry: 
Line 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idlin 
 
Object Identifier 
(5) 
catstop   
Low Visibility Operation Category of  Holding Position 
(6) 
status  
State of feature exceeding one or more AIRAC cycles 
(7) 
vacc  
Vertical accuracy as a LEP 
(8) 
hacc  
Horizontal accuracy as a CEP 
(9) 
vres  
Vertical resolution of coordinates 
(10) 
hres  
Horizontal resolution of coordinates 
(11) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(12) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(13) 
revdate  
Last revision date of data 
(14) 
idp 
Object identifier of runway or taxiway being protected 

## 4.3.3.6 Frequency Areas

Definition: 
Designated part of a surface movement area where a specific frequency is required by air traffic control or ground control. 
Description: 
One or more polygons that represent the region in which a specific frequency is to be used.  
 
4.3.3.6.1 
Data Capture Rule:  
Polygons representing designated areas on the surface where a specific frequency is required by ATC or ground control shall be individual objects in the database.  If there is only one frequency area for the aerodrome, the polygon shall cover the total aerodrome area as defined in Section 3.11.1. See Figure 4-14. 
In case of an overlap of the Frequency Area with another feature, overlapping of both polygons is allowed. 


Feature Name:  
FrequencyArea 
Geometry: 
 
Polygon 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt 
ICAO aerodrome location indicator 
(4) 
hacc  
Horizontal accuracy as a CEP 
(5) 
hres  
Horizontal resolution of coordinates 
(6) 
source  
 
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(7) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(8) 
revdate  
Last revision date of data 
(9) 
frq  
Primary frequency used on frequency area 
(10) 
station  
Service or station assigned to primary frequency (e.g. ATC Tower, Ground Control) 

## 4.3.4 Aprons

The Apron as defined in ICAO Annex 14, Chapter 1.1 is an aggregate of the features Apron Element, Parking Stand Area, and those Taxiway Elements that are located within the defined Apron Area. See Figure 4-15. 

## 4.3.4.1 Apron Elements

Definition: 
The remaining parts of a defined apron area that are not covered by Parking Stand Area features or Taxiway Element 
features. 
Description: 
The apron may consist of multiple apron elements.  
4.3.4.1.1 
Data Capture Rule:  
Aircraft accessible apron areas that are not aircraft stands, aircraft stand taxilanes, or apron taxiways shall be individual objects in the database. This includes turn-around areas near the end of runways and fillets designed to accommodate wide turns. See Figure 4-16. 

## 

Feature Name:  
ApronElement 
Geometry: 
 
Polygon 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
status  
State of feature exceeding one or more AIRAC cycles 
(5) 
vacc  
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
 
Vertical resolution of coordinates 
(8) 
hres  
 
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
pcn  
A number expressing the bearing strength of a pavement for unrestricted operations.. If multiple pcn's exist for a given feature, the lowest should be used. 
(13) 
restacn 
Usage restriction (prohibited) for  specified aircraft type according to ICAO-ACN (Aircraft classification number). Encoding: Aircraft type according ICAO-ACN (Aircraft classification number). If there is more than one aircraft-type restriction, the different types should be divided by a ".". Example: 747-400 and A 380 at one location: B744.A380 
(14) 
gsurftyp 
Generic surface type (e.g. concrete) 
(15) 
idapron  
Name of apron 

## 4.3.4.2 Stand Guidance Lines

| Definition:                      |
|----------------------------------|
| be used for parking an aircraft. |

Description: 
All painted taxilines covering a parking stand area are regarded as stand guidance lines. There may be several stand guidance taxilines leading to an aircraft stand to accommodate different aircraft types. 
4.3.4.2.1 
Data Capture Rule:  
All stand guidance lines shall be individual objects in the database.  
4.3.4.2.2 
To ensure connectivity, the startpoint of a stand guidance taxiline shall be the endpoint of the connecting taxiway guidance line (only if applicable).  
Feature Name:  
StandGuidanceLine 
Geometry: 
 
Line 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt 
ICAO aerodrome location indicator 
(4) 
idstd 
Object identifier 
(5) 
vacc  
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
color  
Color specifying the color of the stand guidance line 
(13) 
style  
Style specifying the line property of the stand guidance line (e.g. dashed or solid) 
(14) 
direc  
Directionality of stand guidance line 
(15) 
wingspan  
Maximum wingspan on stand 
(16) 
status  
State of feature exceeding one or more AIRAC cycles 

## 4.3.4.3 Parking Stand Locations

Definition: 
Location of an aircraft stand. 

Description: 
As shown in Figure 4-17, a single parking stand location may accommodate different aircraft types (e.g. for B-747, A-340). In addition, there may be multiple parking stand locations within one parking stand area. 

4.3.4.3.1 
Data Capture Rule:  
Painted parking stand locations on the stand guidance line shall be individual objects in the database.  
4.3.4.3.2 
The parking stand location shall be located on the Stand guidance line at the location indicating the position to stop for a specific aircraft type. 
Feature Name:  
ParkingStandLocation 

| Geometry:    |     | Point    |
|--------------|-----|----------|

Attributes: 
(1) 
feattype  
Feature type 

(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 

(3) 
idarpt 
ICAO aerodrome location indicator 
(4) 
idstd 
Object identifier 
(5) 
vacc  
Vertical accuracy as a LEP  
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
acn  
Park stand location's feasibility for specific aircraft type 
according to ICAO-ACN (Aircraft Classification Number) 

## 4.3.4.4 Parking Stand Areas

Definition: 
A designated area on an apron intended to be used for parking an aircraft.  

Description: 
Parking Stand Areas are operational areas near parking stands locations denoted by painted markings. 
4.3.4.4.1 
Data Capture Rule:  
All Parking Stand Areas shall be individual objects in the database.  
If marked, a parking stand area polygon shall be captured that coincides with the painted markings. If not marked, a polygon shall be captured that considers published restrictions (e.g. wingspan limits). 

Feature Name:  
ParkingStandArea 
Geometry: 
 
Polygon 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idstd  
 
Object identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
pcn  
A number expressing the bearing strength of a pavement for unrestricted operations.. If multiple pcn's exist for a given feature, the lowest should be used. 
(13) 
restacn 
Usage restriction (prohibited) for  specified aircraft type according to ICAO-ACN (Aircraft classification number). Encoding: Aircraft type according ICAO-ACN (Aircraft classification number). If there is more than one aircraft-type 
restriction, the different types should be divided by a ".". Example: 747-400 and A 380 at one location: B744.A380 
(14) 
gsurftyp 
Generic surface type (e.g. concrete) 
(15) 
jetway 
Availability of jetway 
(16) 
fuel 
Types of fuel available 
(17) 
towing 
Availability of towing service 
(18) 
docking 
Availability of docking station system 
(19) 
gndpower 
Availability of ground power 
(20) 
idapron 
Name of underlying apron. See Figure 4-12. 

## 4.3.4.5 Deicing Areas

Definition: 
An area comprising an inner area for the parking of an airplane to receive de-icing treatment and an outer area for the maneuvering of two or more mobile de-icing equipment. 
Description: 
See definition: ICAO Annex 14, Chapter 1.1 The deicing area feature polygon contains the marked deicing area on the apron surface. 
4.3.4.5.1 
Data Capture Rule:  
Designated aircraft deicing areas shall be individual objects in the database. 
 
 
In case of an overlap of the Deicing Area with another feature (eg. Taxiway Element), overlapping of both polygons is allowed.  
Feature Name:  
DeicingArea 
Geometry: 
 
Polygon 

## Attributes:

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
status 
State of feature exceeding one or more AIRAC cycles 
(5) 
vacc  
Vertical accuracy as a LEP 
(6) 
hacc   
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 

(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
restacn 
Usage restriction (prohibited) for  specified aircraft type according to ICAO-ACN (Aircraft classification number). Encoding: Aircraft type according ICAO-ACN (Aircraft classification number). If there is more than one aircraft-type restriction, the different types should be divided by a ".". Example: 747-400 and A 380 at one location: B744.A380 
(13) 
gsurftyp 
Generic surface type (e.g. concrete) 
(14) 
idbase 
Identifier of underlying Taxiway Element (idlin), Parking Stand Area (idstd), or Apron Element (idapron). If the deicing area overlaps another feature, this shall be indicated. If the deicing area does not overlap another feature, then ‗No overlap' shall be indicated. See Figure 4-18. 
(15) 
ident 
Name of Deicing Area. See Figure 4-18. 

## 4.3.4.6 Service Roads

Definition: 
Part of aerodrome surface used by service vehicles. 
Description: 
A Service Road may consist of one or more polygons. Service roads can exist both inside and outside of the aerodrome movement area. 
4.3.4.6.1 
Data Capture Rule:  
Those parts of service roads that are located within an area that extends from the edge(s) of the runway(s) to 90m from the runway centerline(s) and for all other parts of the aerodrome movement area(s), 50m from the edge(s) of the defined area(s) shall be captured. The capture of service roads outside the regions described above (including in the movement area) and inside the aerodrome boundary is optional. 
4.3.4.6.2  
 
In case the user chooses to capture the optional Service Roads within the movement area, the overlapping area shall be captured as a unique element to both classes. Both polygons shall be of identical shape. See Figure 4-19. 
 

Feature Name:  
ServiceRoad 
Geometry: 
 
Polygon 
Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
vacc  
 
Vertical accuracy as a LEP 
(5) 
hacc  
Horizontal accuracy as a CEP 
(6) 
vres  
Vertical resolution of coordinates 
(7) 
hres  
Horizontal resolution of coordinates 
(8) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(9) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(10) 
revdate  
Last revision date of data 
(11) 
gsurftyp 
Predominant surface type 
(12) 
featbase 
Identification of the feature type affected by the road. If the service road overlaps another feature, this shall be indicated. 
If the service road does not overlap another feature, then ‗No 
overlap' shall be indicated. 
(13) 
idbase 
Identifier of underlying Taxiway Element (idlin), Parking Stand Area (idstd), or Apron element (idapron). If the service road overlaps another feature, this shall be indicated. If the service road does not overlap another feature, then ‗No overlap' shall be indicated. 

## 4.3.4.7 Aerodrome Reference Points

Definition: 
The designated geographical location of an aerodrome. 

Description: 
See Definition: ICAO Annex 14, Chapter 1.1 

4.3.4.7.1 
Data Capture Rule:  
The designated geographic location of an aerodrome as published in the AIP shall be an individual object in the database. 
Feature Name:  
AerodromeReferencePoint 
Geometry: 
 
Point 

## Attributes:

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
iata 
 
IATA aerodrome location indicator 
(5) 
name 
 
Name of aerodrome  
(6) 
vacc  
 
Vertical accuracy as a LEP 
(7) 
hacc  
Horizontal accuracy as a CEP 
(8) 
vres  
Vertical resolution of coordinates 
(9) 
hres  
Horizontal resolution of coordinates 
(10) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(11) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(12) 
revdate  
Last revision date of data 
(13) 
elev 
 
Provides elevation of the airport. 
 

## 4.3.5 Vertical Structures

Vertical structures include point, line, and polygon structures. Point structures have a radius indicating any associated structures such as guywires. See Figure 4-20. 

(a)
(b)

(a)
                                                                       (b)
(a)
                                                                       (b) (a)
                                                                       (b) (a)
                                                                       (b)
(a)
                                                                       (b)

Polygon Structure Line Structure Radius Radius Radius Point Structure

## 4.3.5.1 Vertical Polygonal Structures

| Definition:                                                   | Polygonal structure of a defined vertical extent that is located    |
|---------------------------------------------------------------|---------------------------------------------------------------------|
| within an area that extends from the edge(s) of the runway(s) |                                                                     |
| to 90m from the runway centerline(s) and for all other parts  |                                                                     |
| of the aerodrome movement area(s), 50m from the edge(s) of    |                                                                     |
| the defined area(s).                                          |                                                                     |
| Description:                                                  | All polygonal structures (e.g. buildings) whose maximum             |
| height exceeds the defined vertical limit. See Section 3.11.  |                                                                     |

4.3.5.1.1 
Data Capture Rule:  
All Vertical Polygon Structures shall be individual objects in the database.  

In the horizontal plane, a structure that has a complex real world shape may be decomposed into multiple polygons. In the vertical plane, all polygons should have a height attribute indicating the highest point of the corresponding real-world object.  

Feature Name:  
VerticalPolygonalStructure 
Geometry: 
 
Polygon 
Attributes: 
(1) 
feattype  
Feature type 

(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 

(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
plysttyp  
Polygonal structure type 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 

(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 

(11) 
revdate  
Last revision date of data 
(12) 
height  
Maximum height of top of vertical structure 
(13) 
elev  
Maximum elevation of top of vertical structure (Orthometric elevation) 
(14) 
material  
Predominant surface material of the vertical structure 
(15) 
ident 
Name/Identifier of vertical polygon structure  

## 4.3.5.2 Vertical Point Structures

Definition: 
Point structure of a defined vertical extent that is located within an area that extends from the edge(s) of the runway(s) to 90m from the runway centerline(s) and for all other parts of the aerodrome movement area(s), 50m from the edge(s) of the defined area(s). 
Description: 
All point structures (e.g. radio towers) whose maximum height exceeds the defined vertical limit. See Section 3.11. 
4.3.5.2.1 
Data Capture Rule:  
All Vertical Point Structures shall be individual objects in the database.  

In the horizontal plane, the vertical point object should be located in the center of the corresponding real-world object. In the vertical plane, it should be located on the highest point of the real-world object. 

Feature Name:  
VerticalPointStructure 
Geometry: 
 
Point 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
pntsttyp 
 
Vertical Point Object feature type identifier 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
marking  
Obstacle marking in conformance with ICAO Annex 14, Chapter 6.2 
(13) 
lighting  
Obstacle lighting in conformance with ICAO Annex 14, Chapter 6.2 
(14) 
radius  
Radius of circle around center of obstacle including body of obstacle and associated structures such as guywires 
(15) 
height  
Maximum height of top of vertical structure 
(16) 
elev  
Maximum elevation of top of vertical structure (Orthometric elevation) 
(17) 
material  
Predominant surface material of the vertical structure 

## 4.3.5.3 Vertical Line Structures

Definition: 
Line structure of a defined vertical extent that is located within an area that extends from the edge(s) of the runway(s) to 90m from the runway centerline(s) and for all other parts of the aerodrome movement area(s), 50m from the edge(s) of the defined area(s). 

Description: 
All line structures (e.g. power lines) whose maximum height exceeds the defined vertical limit. See Section 3.11. 
4.3.5.3.1 
Data Capture Rule:  
All Vertical Line Structures shall be individual objects in the database.  
In the horizontal plane, the vertical line object should be located in the center of the corresponding real-world object. In the vertical plane, it should be located on the highest point of the real-world object. 

Feature Name:  
VerticalLineStructure 
Geometry: 
 
Line 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
linsttyp  
Vertical Line Object feature type identifier  
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 
(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(11) 
revdate  
Last revision date of data 
(12) 
marking  
Obstacle marking in conformance with ICAO Annex 14, Chapter 6.2 
(13) 
lighting  
Obstacle lighting in conformance with ICAO Annex 14, Chapter 6.2 
(14) 
height  
Maximum height of top of vertical structure 
(15) 
elev  
Maximum elevation of top of vertical structure (Orthometric elevation) 
(16) 
material  
Predominant surface material of the vertical structure 

## 4.3.6 Construction Areas

Definition: 
Part of a movement area under construction. 

Description: 
The construction area feature is that part of the aircraft surface movement area under construction, including runways, taxiways, apron, aircraft parking stands, and deicing areas. 
4.3.6.1 
Data Capture Rule: 
Aircraft movement areas under construction shall be individual objects in the database. See Section 3.7.  
Feature Name:  
ConstructionArea 
Geometry: 
 
Polygon 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
hacc  
Horizontal accuracy as a CEP 
(5) 
hres  
Horizontal resolution of coordinates 
(6) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(7) 
integr  
Integrity of data in the aeronautical data processing chain 
from data origination process to present data manipulation process 
(8) 
revdate  
Last revision date of data 
(9) 
pstdate  
Planned construction start date 
(10) 
pendate  
Planned construction end date 
(11) 
piocdate  
Planned initial operational date (inc commission date) 

## 4.3.7 Water

Definition: 
Water bodies close to the movement zone. 
Description: 
All water courses located within a buffer 200m from the edge of the aircraft movement zone (taxiways, stopways, fato, apron, parking stand area, deicing area), and major water courses located within a buffer 5km from the edge of the aircraft movement zone. 
 
Data Capture Rule: 
Use the outer edges of the water surface at high tide. 
4.3.7.1  
Capture all water located within an area that extends 200m from the edge of the aerodrome movement area(s).  If a portion of a water object is within this area, the entire water object shall be captured (it should not be clipped at 200m beyond the movement area). 
4.3.7.2  
For objects whose surface area is greater than 0.5 square kilometers, capture water located within an area that can extend up to 5.0 kilometers from the edge of the aerodrome movement area(s).  These water objects shall be captured out to the resulting rectangular aerodrome boundary. 
The total extend of the boundary could vary based on a data provider's source data, but should include a portion of large bodies of water outside of the movement area.  The 5.0km limit is designed to prevent unnecessarily vast amounts of water data from being captured and yield more predictable and consistent results. For example, Figure 4-21 depicts an airport near an ocean. The inner dashed line indicates the 200m buffer around the movement area, and the outer dashed line indicates the 5.0 km buffer around the movement area. 

Feature Name:  
Water 
Geometry: 
 
Polygon 
Attributes: 
(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
vacc  
 
Vertical accuracy as a LEP 
(5) 
hacc  
Horizontal accuracy as a CEP 
(6) 
vres  
Vertical resolution of coordinates 
(7) 
hres  
Horizontal resolution of coordinates 
(8) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(9) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(10) 
revdate  
Last revision date of data 

## 4.3.8 Hotspot

Definition: 
A location on an aerodrome movement area with a history or potential risk of collision or runway incursion, and where heightened attention by pilots/drivers is necessary. (ICAO Annex 4)Description: 
Hotspots are designated positions on 
the airport surface where runway/taxiway incursions have historically taken place and may take place in the future. A hotspot is an occurrence in the airport movement environment involving an aircraft, vehicle, person, or object on the ground that creates a collision hazard or results in a loss of required separation with an aircraft taking off, intending to take off, landing, or intending to land. 

 
Data Capture Rule: 
The hotspot polygon should be placed around the intersection of the affected features, which may include taxiways, runways and stopways. 
In case of an overlap of the Hotspot with another feature (eg. Runway Element, Taxiway Element), overlapping of both polygons is allowed.  

Feature Name:   
Hotspot 
Geometry: 
 
Polygon 
Attributes: 

(1) 
feattype  
Feature type 
(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 
(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idhot 
 
Hotspot feature identifier 

(5) 
hacc  
Horizontal accuracy as a CEP 
(6) 
hres  
Horizontal resolution of coordinates 
(7) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(8) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 
(9) 
revdate  
Last revision date of data 

## 4.3.9 (Optional) Aerodrome Surface Lighting

| Definition:                                            | Lighting within a movement area.                            |
|--------------------------------------------------------|-------------------------------------------------------------|
| Description:                                           | Individual airport surface lights that are located within a |
| buffer 90m from runway centerline and 50m from edge of |                                                             |
| aircraft movement zone.                                |                                                             |

4.3.9.1 
Data Capture Rule: 
Capture the center of the light. 
Feature Name:  
AerodromeSurfaceLighting 
Geometry: 
 
Point 
Attributes: 
(1) 
feattype  
Feature type 

(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 

(3) 
idarpt  
ICAO aerodrome location indicator 

(4) 
vacc  
 
Vertical accuracy as a LEP 

(5) 
hacc  
Horizontal accuracy as a CEP 
(6) 
vres  
Vertical resolution of coordinates 
(7) 
hres  
Horizontal resolution of coordinates 

(8) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(9) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 

(10) 
revdate  
Last revision date of data 
(11) 
status 
State of feature exceeding one or more AIRAC cycles 

## 4.3.10 Quality Data

The following data elements are needed to support quality assurance. 

## 4.3.10.1 Survey Control Points

Definition: 
A monumented survey control point. 
Description: 
See Definition: ICAO Doc 9674 WGS84 Manual, Chapter 5.2.5. In the US, these are known as PACS. 
4.3.10.1.1 
Data Capture Rule:  
Locations of monumented survey control points at the aerodrome shall be individual objects in the database.  

The marked position of a survey control point should be captured. 

Feature Name:  
SurveyControlPoint 
Geometry: 
 
Point 
Attributes: 
(1) 
feattype  
Feature type 

(2) 
idnumber 
Special unique identifier permanently assigned to a feature by the data provider 

(3) 
idarpt  
ICAO aerodrome location indicator 
(4) 
idsurv  
Object identifier. Name/number of survey control point 
(5) 
vacc  
 
Vertical accuracy as a LEP 
(6) 
hacc  
Horizontal accuracy as a CEP 
(7) 
vres  
Vertical resolution of coordinates 
(8) 
hres  
Horizontal resolution of coordinates 

(9) 
source  
Name of entity or organization that supplied data according to RTCA DO-200A/EUROCAE ED-76 
(10) 
integr  
Integrity of data in the aeronautical data processing chain from data origination process to present data manipulation process 

(11) 
revdate  
Last revision date of data 

(12) 
coord  
Published reference coordinates (x/y/z or lat/long/elevation) of survey point as provided by authorized survey institution. This information is expressed in the complete resolution of the original surveyed values. 

(13) 
hdatum 
Full name of horizontal datum of reference coordinates 
(14) 
vdatum 
Name of vertical datum of reference coordinates 
(15) 
spheroid  
Spheroid of reference coordinate 
(16) 
project  
Full name of projection of reference coordinates 

## 4.4 Quality 4.4.1 Accuracy

Accuracy requirements are specified according to three categories: Fine, *Medium*, and Coarse.  These categories are defined in Section 4.4.4. 

4.4.1.1 
Aerodrome mapping data accuracy shall meet a confidence level of 95% for *Fine* and 90% for Medium or *Coarse* quality categories.  Further, there may be data elements at specific aerodromes that are deemed critical in terms of operational safety by system designers.  For these elements, sufficient validation may be necessary to ensure that the stated accuracy is not only at the required confidence level, but also bounded to a prescribed worst-case inaccuracy.  Aerodrome mapping geometry data shall meet the accuracy requirements listed in Tables 4-5 through 4-8.  The accuracy requirement listed for a particular data element applies to all position coordinates that constitute that data element. 
4.4.1.2 
As stated in 4.4.1.1, in order to bound the error for certain elements, an additional accuracy value has been defined.  The *Max Error* column of Tables 4-5 through 4-8 refers to maximum acceptable error.  Most of the Max Error numbers represent approximately a six standard deviation value for a normal distribution.  This value shall not be exceeded for the elements specified.  This limit shall be applied only to Fine category data. 
Positional accuracies are relative to a positional datum.  It is recommended that accuracies be relative to the WGS-84 reference network at the aerodrome. In the U.S., these are referred to as Primary Aerodrome Control Sites (PACS) (FAA doc. 405). 

4.4.1.3 
For any data element that requires multiple vertices, the number of vertices shall be sufficient to maintain the required horizontal and vertical accuracy as well as to distinguish any points where multiple elements intersect. 

## 4.4.2 Resolution

4.4.2.1 
Resolution shall be sufficient to guarantee both the horizontal and the vertical accuracy requirements listed in Tables 4-5 through 4-8. These represent the minimum resolution required.  The definition in Appendix B for resolution shall be used with respect to Tables 4-5 through 4-8. 

## 4.4.3 Integrity

For the purposes of this document, integrity classification is consistent with ICAO's WGS-84 Manual. 

(1) Critical data - there is a high probability when using corrupted critical data that 
the continued safe operation of an aircraft would be severely at risk with potential 
for catastrophe.  Required level of data integrity is 10-8 or better. 
(2) Essential data - there is a low probability when using corrupted essential data that 
the continued safe operation of an aircraft would be severely at risk with potential 
for catastrophe.  Required level of data integrity is 10-5 or better. 
(3) Routine data - there is a very low probability when using corrupted routine data 
that the continued safe operation of an aircraft would be severely at risk with the 
potential for catastrophe. Required level of data integrity is 10-3 or better. 
4.4.3.1 
Data originators and integrators shall ensure that the integrity of aerodrome data is maintained throughout the data process from survey/origin to the end user. 
4.4.3.2 
Because required data integrity depends to a large degree on the intended functional use of the data not all data elements have an assigned integrity. However they must be categorized as either routine, essential or critical, as indicated above. 
4.4.3.3 
For those data elements that are already required to support air navigation2, integrity 
requirements from those documents shall be used and are re-stated in Tables 4-5 through 4-8. 

## 4.4.4 Numerical Requirements

Tables 4-5 through 4-8 list data quality requirements for three categories of AMDB data: *Coarse, Medium,* and *Fine*. Coarse data information requirements would be the minimum acceptable data quality. Coarse quality data may support only a few of the applications described in Appendix A for a given aerodrome such as electronic charting.  This data would generally support criteria for VFR and special-night VFR (helicopter) operations, primarily at GA uncontrolled aerodromes.  It is expected that data meeting coarse requirements may be obtained from a single source (e.g. imagery or CAD drawings). Medium data information requirements would support most of the aviation applications described in Appendix A for a given aerodrome including the cockpit display of traffic information (CDTI).  This data may support non-precision approach capability (e.g. VOR, NDB, and GNSS approaches).  Medium data requirements may be met using imagery from commercial space systems or aircraft without ground control utilizing overlapping imagery; and/or through photogrammetric analysis utilizing a stereoscopic model. Fine data information requirements would support all aviation applications described in Appendix A for a given aerodrome including low visibility surface navigation. This data would support all-weather flight operations including conditions when Category I, II, or III precision approaches are being flown.  The most stringent approach criteria at the aerodrome will generally establish a need for Fine survey data.  Acquiring this class of data would probably require ground control points (surveys) and the use of photogrammetric techniques in conjunction with imagery. 

4.4.4.1 
The Data Derivation column in Tables 4-5 through 4-8 refers to either Surveyed (S), Calculated (C), or *as charted*.  If available, a surveyed value shall be used instead of a calculated or *as charted* value. 
4.4.4.2 
In Tables 4-5 through 4-8, the three columns under Fine, *Medium*, and *Coarse*, list requirements for accuracy (A), resolution (R), and integrity (I), respectively.  As 
stated previously, integrity requirements, either critical (C), essential (E), or routine (R), are listed only for those elements already required for air navigation.  For these elements, the quality requirements are simply copied from the relevant ICAO documents to show consistency. 

Data Element 
Data 
Derivation 
Fine 
Medium 
Coarse 
Max 
  
  
A 
R 
I 
A 
R 
I 
A 
R 
I 
  
Runway element 
S 
1 
0.1 
C 
5 
0.1 
- 
30 
1 
- 
- 
Runway intersection 
S 
1 
0.1 
C 
5 
0.1 
- 
30 
1 
- 
- 
Runway threshold 
S 
1 
0.1 
C 
5 
0.1 
- 
NS 
NS 
- 
3 
Painted centerline 
S 
0.5 
0.01 
C 
5 
0.1 
- 
NS 
NS 
- 
2 
LAHSO 
S 
1 
0.1 
R 
5 
0.1 
- 
NS 
NS 
- 
3 
Arresting gear location 
S 
1 
0.1 
- 
5 
0.1 
- 
30 
1 
- 
- 
Runway shoulder 
S 
1 
0.1 
- 
5 
0.1 
- 
30 
1 
- 
- 
Stopway 
S 
1 
0.1 
- 
5 
0.1 
- 
30 
1 
- 
- 
Runway displaced area 
S 
1 
0.1 
C 
5 
0.1 
- 
30 
1 
- 
- 
Runway marking 
as charted 
NS 
NS 
- 
NS 
NS 
- 
NS 
NS 
- 
- 
FATO 
S 
1 
0.1 
C 
5 
0.1 
- 
5 
0.1 
- 
- 
TLOF 
S 
1 
0.1 
C 
5 
0.1 
- 
5 
0.1 
- 
- 
Helipad threshold 
S 
1 
0.1 
C 
5 
0.1 
- 
NS 
NS 
- 
- 
Taxiway element 
S 
1 
0.1 
- 
5 
0.1 
- 
5 
0.1 
- 
- 
Taxiway shoulder 
S 
1 
0.1 
- 
5 
0.1 
- 
5 
0.1 
- 
- 
Taxiway guidance line 
S 
0.5 
0.01 
C 
5 
0.1 
- 
NS 
NS 
- 
2 
Taxiway intersection marking 
S 
0.5 
0.01 
C 
5 
0.1 
- 
NS 
NS 
- 
- 
Taxiway holding position 
S 
1 
0.1 
- 
5 
0.1 
- 
NS 
NS 
- 
3 
Runway exit line 
S 
0.5 
0.01 
C 
5 
0.1 
- 
NS 
NS 
- 
2 
Frequency area 
C 
NS 
NS 
- 
NS 
NS 
- 
NS 
NS 
- 
- 
Apron 
S 
1 
0.1 
- 
5 
0.1 
- 
30 
1 
- 
- 
Stand guidance line  
S 
0.5 
0.01 
E 
5 
0.1 
- 
NS 
NS 
- 
2 
Parking stand location  
S 
0.5 
0.01 
E 
5 
0.1 
- 
30 
1 
- 
2 
Parking stand area  
C 
1 
0.1 
- 
5 
0.1 
- 
30 
1 
- 
- 
Deicing area  
S 
1 
0.1 
- 
5 
0.1 
- 
30 
1 
- 
- 
Vertical polygonal objects 
S 
0.5 
0.1 
E 
5 
0.1 
- 
30 
1 
- 
- 
Vertical point objects 
S 
0.5 
0.1 
E 
5 
0.1 
- 
30 
1 
- 
- 
Vertical line objects 
S 
0.5 
0.1 
E 
5 
0.1 
- 
30 
1 
- 
- 
Construction area 
S 
1 
0.1 
- 
5 
0.1 
- 
5 
0.1 
- 
- 
Aerodrome reference point 
C 
30 
1 
R 
30 
1 
R 
30 
1 
R 
- 
Survey control point 
S 
0.5 
0.01 
E 
0.5 
0.01 
E 
NS 
NS 
- 
- 
Service road 
S 
1 
0.1 
- 
5 
0.1 
- 
30 
1 
- 
- 
Water 
S 
NS 
NS 
- 
NS 
NS 
- 
NS 
NS 
- 
- 
Aerodrome surface lighting 
S 
1 
0.1 
- 
NS 
NS 
- 
NS 
NS 
- 
- 
Blastpad 
S 
1 
0.1 
- 
5 
0.1 
- 
30 
1 
- 
- 
Hotspot 
C 
NS 
NS 
- 
NS 
NS 
- 
NS 
NS 
- 
- 
 
Error 

(All values in meters; NS denotes not specified) 

Max
Fine
Medium
Coarse
Data Element
Data
Derivation
Error
A
R
I
A
R
I
A
R
I
Runway threshold (non-precision)
S
0.5
0.1
E
NS
NS
-
NS
NS
-
3
Runway threshold (precision)
S
0.25
0.01
C
NS
NS
-
NS
NS
-
-
Painted centerline
S
1
0.1
-
NS
NS
-
NS
NS
-
6
Helipad threshold
S
0.5
0.1
C
NS
NS
-
NS
NS
-
-
Survey control point
S
0.25
0.01
E
NS
NS
-
NS
NS
-
-
Threshold elevation (non-precision)
S
0.5
0.1
E
NS
NS
-
NS
NS
-
3
Threshold elevation (precision)
S
0.25
0.01
C
NS
NS
-
NS
NS
-
-
Max height of vertical object
C
1
0.1
E
1
0.1
-
NS
NS
-
-
Max elevation of vertical object
S
1
0.1
E
1
0.1
-
NS
NS
-
-
Touchdown zone elevation
S
1
0.1
-
1
0.1
-
NS
NS
-
-
Max
Fine
Medium
Coarse
Data Element
Data
Derivation
Error
A
R
I
A
R
I
A
R
I
True runway bearing
C
0.01°
0.01°
R
0.5°
0.01°
-
1.5°
0.1°
-
-
Magnetic runway bearing
S
0.01°
0.01°
R
0.5°
0.01°
-
1.5°
0.1°
-
-

(All values in meters unless otherwise stated; NS denotes not specified) 

 
Max
Fine
Medium
Coarse
Data Element
Data
Derivation
Error
A
R
I
A
R
I
A
R
I
Width of runway
C
0.5
0.01
R
1
0.1
-
5
0.1
-
-
Length of runway
C
1
0.1
C
5
0.1
-
30
1
-
-
Touchdown zone longitudinal slope
C
0.1% 0.01%
-
NS
NS
-
NS
NS
-
-
Runway slope
C
0.1% 0.01%
-
NS
NS
-
NS
NS
-
-
Take-off run available
C
1
0.1
E
5
0.1
-
30
1
-
-
Take-off distance available
C
1
0.1
E
5
0.1
-
30
1
-
-
Accelerating-stop-distance avail.
C
1
0.1
E
5
0.1
-
30
1
-
-
Landing distance available
C
1
0.1
C
5
0.1
-
30
1
-
-
Radius about center of obstacle
S
1
0.1
-
5
0.1
-
30
1
-
-
Max height of point structure
C
1
0.1
-
5
0.1
-
30
1
-
-

## A Applications Of Aerodrome Mapping Databases A.1 Introduction

This appendix provides an overview of the types of applications that may make use of aerodrome mapping databases.  These application categories have been used to generate the requirements for the content, origination, publication, updating, and enhancement of the aerodrome mapping data that have been included in the main body of this document. Many of the applications described herein are intended primarily to improve the user's situational awareness (SA) and/or to supplement surface navigation, thereby increasing safety margins and operational efficiency.  Because the human factors term ―Situational Awareness‖ (SA) is somewhat vague, more specific operational benefits will be listed for each application.  All of these specific benefits can be considered as contributing to overall improved SA for the user (e.g., pilots, controllers, aerodrome planners, and managers).  Below is a definition of SA. 

Definition:  Situational Awareness (SA) is the perception of elements in the environment, the comprehension of their meaning, and the projection of their status into the near future3. 

For pilots, the notional concept is that situational awareness includes three fundamental elements:  factors affecting the pilot's physical and emotional state; factors affecting the aircraft and its airworthiness; and last, all factors *external* to the aircraft.  These external factors include situational awareness of where you are with respect to terrain and obstacle hazards, adverse weather, traffic, and wake vortex hazards. This appendix consists of the following sections:  Section A.2 provides background information with respect to relevant ICAO, EUROCAE, and RTCA activities.  Section A.2 also provides an overview of aerodrome surface operations.  Section A.3 consists of a summary table listing the applications to be discussed.  Sections A.4 through Section A.15 provide brief descriptions of twelve potential applications of aerodrome mapping databases.  Each of these sections describes the operational concept and the potential benefits that can be achieved.  Finally, Section A.16 briefly introduces a technology that has the potential to implement many of the applications of AMDBs. 

## A.2 Background A.2.1 Related Icao, Eurocae, And Rtca Activities

ICAO and EUROCAE have defined operational requirements for Advanced Surface Movement Guidance and Control Systems (A-SMGCS)4,5 that specify what is required to support safe, orderly, and expeditious movement of aircraft and vehicles at aerodromes under all visibility conditions, traffic densities, and aerodrome layouts.  These requirements were written to ensure standardization and safety with respect to global interoperability. 

Specific recommendations are made by ICAO for improving aerodrome surface operations.  Some of these are listed below.  

 
Improved means of providing situational awareness information to pilots, controllers and vehicle operators 
 
Clearly defined roles and responsibilities that eliminate procedural ambiguities that lead to operational errors and deviations 
 
Improved guidance and procedures should be in place to allow safe operations regardless of visibility, traffic density, and aerodrome layout 
 
Conflict prediction and/or detection, analysis, and resolution should be provided 
 
All users should be provided with the same level of service while operating on the aerodrome surface 
 
A standardized aerodrome mapping database, available to all aerodrome users, would allow implementation of many of these recommendations as will be described in later sections. The ICAO A-SMGCS document forecasts that the projected growth in flight operations will lead to increased surface congestion and system delay unless new techniques (e.g., technologies) are available to ATC to reduce workload.  In addition, apron controllers and flight dispatch services will require greater sharing of information to manage the availability of stands and parking areas.  Finally, for pilots, supplemental guidance information will be required, particularly under low visibility conditions, to avoid increasing workload as the traffic volume grows. RTCA has published DO-247 ―The Role of GNSS in Supporting Aerodrome Surface Operations6.‖  Although this document is intended to further develop the performance standards applicable to GNSS equipment for use on the aerodrome surface, it also suggests that GNSS-derived information (i.e., position, velocity, and time) combined with a suitable aerodrome database and display can be used to provide pilots and vehicle drivers with situational awareness and electronic guidance. 

RTCA's Special Committee 186 has drafted ―Operational Concepts, Procedures, and Information Requirements for the Cockpit Display of Traffic Information (CDTI) 
Applications7.‖  One of the applications included is ―aerodrome surface CDTI to improve pilot situational awareness.‖  This application requires an aerodrome mapping database, for the overlay of surveillance data, to achieve maximum potential. 

## A.2.2 Overview Of Aerodrome Surface Operations

Traditionally, pilots have relied on visual aids such as airfield markings (e.g., painted centerlines), signs, and lighting, in conjunction with a paper chart of the aerodrome to navigate from point to point on the aerodrome surface.  Radio communication with air traffic control (ATC) is used by pilots to obtain the route to follow while on the surface.  
As a rule, a ―ground‖ controller will issue route instructions to pilots using explicit instructions and a strict protocol (i.e., phraseology) so that there is no misunderstanding of voice communications exchanged over the radio channel.  The pilot must then memorize this route (or write it down), re-state it to the controller for confirmation, and then follow the signs and markings to the destination while avoiding other surface traffic and obstructions.  Meanwhile, the ground controller must remember the routes given to all aircraft, as well as all aircraft locations, so that no one is directed into a potential collision.  If there is a potential for collision, hold in position and/or hold-short instructions can be issued over the radio frequency to further constrain aircraft movements. Surveillance on the aerodrome surface is performed by the flight crews based primarily on the ―see and be seen‖ principle to maintain safe separation.  Similarly, ATC performs the surveillance task based primarily on visual cues.  Occasionally, both pilots and controllers will use radio communications to confirm positions of relevant traffic (e.g., ―Delta 635, say your position‖).  While the Traffic Alerting and Collision Avoidance System (TCAS) provides traffic advisories to flight crews in flight, it is not intended for use on the aerodrome surface.  The Aerodrome Surface Detection Equipment (ASDE-3) radar is used in the U. S. to provide secondary surveillance data to the ATC tower; however, it is currently only scheduled to be deployed at 34 U. S. aerodromes.  ASDE-X, a follow-on airport surveillance system, is intended for deployment at an additional 25 towered airports. These traditional procedures have worked well as aerodrome surface has not been congested and visibility is usually good.  However, as traffic volume has increased, the surface is becoming more and more congested, even in clear weather, and there is a need to perform more operations in low visibility and at night to meet an ever increasing demand leading to increasingly complex, large aerodrome layouts. In order to support flight operations at aerodromes, several other activities are required, each of which are performed by separate organizations or facilities.  These include: 

(1) Aerodrome operations.  The aerodrome authority is responsible for construction and 
maintenance of aerodrome resources such as buildings, pavement, lighting, markings, and landing systems (e.g., ILS).  They are also responsible for providing emergency response teams such as fire/rescue and aerodrome security in some cases. 
(2) Commercial/Cargo airline operations.  These include a wide variety of activities such 
as apron control, aircraft maintenance/fueling, baggage/cargo handling, catering services, crew and aircraft scheduling, flight planning, and ticketing.  These also include training activities such as flight simulations to maintain pilot currency. 
(3) General Aviation (GA) and Business Aviation operations.  In the U. S., these 
operations are typically supported by Fixed Base Operators (FBOs).  FBOs support GA and business aviation operations by providing maintenance, fueling, flight 
planning, and local ground transportation services.  FBOs are typically located away from the commercial concourse/stand areas while still having access to active taxiways and runways. 

These three general classes of aerodrome activities, in conjunction with pilot and ATC activities, represent aerodrome surface operations at the larger aerodrome facilities.  At smaller aerodrome facilities, only a subset of these activities is necessary to support surface operations. 

## A.3 List Of Applications

Based on the availability of a standardized aerodrome mapping database, a wide variety of applications can be envisioned.  Twelve are described in this document.  These applications are listed below and separated by user class.  Note that several of the applications can be used by multiple user classes.  Each application is described in greater detail in Sections A.4 through A.15. 

## Pilots

Section A.4 
Chart information 
Section A.5 
Surveillance and conflict/runway incursion detection/alerting 
Section A.6 
Route/hold-short depiction and deviation detection/alerting 
Section A.7 
Depiction of digital ATIS information 
Section A.8 
Aerodrome surface guidance/navigation 
Section A.13 
Runway operations 
Section A.14 
Notices to Airmen (NOTAMs) and Aeronautical Data Overlays 
Section A.16 
Synthetic vision 
Air Traffic Controllers Sections A.4, A.5, and A.6 Airline, Cargo, GA, and Business Aviation Operations Sections A.4, A.5, A.6, and A.7 

Section A.9 
Resource management 
Section A.10 
Training and High Fidelity Simulation  
Vehicle Operators Sections A.4, A.5, A.6, A.7, A.8, A.10, A.14, and A.16 Aerodrome Operations 

Section A.11 
Aerodrome facility management 
Section A.12 
Emergency and security service management 
Section A.15 
Aerodrome Asset Management 
 

## A.4 Charting Information A.4.1 Operational Concept

For pilots, a graphical depiction of the aerodrome site (including airfield movement/nonmovement areas) is essential to safe and efficient navigation.  Currently, this graphical depiction is provided to flight crews by way of paper charts.  An alternate or supplemental means, of graphically depicting aerodromes is by way of a flight deck electronic display.  This would provide a tool for pilots to visualize their physical environment while on the aerodrome surface, or while planning an arrival to a specific aerodrome.  This tool could also provide access to aerodrome-specific data that are also included in paper charts such as frequencies, operational constraints, and local procedures.  In addition, such a display system could make use of a spatial database that included themes, or layers, that would allow pilots to assimilate specific displayed information types with the out-the-window scenes.  These themes can include: 

 
Runways 
Taxiways 
Aprons 
Shoulders 
Service Roads 
Stands 
Hold Lines/Points 
Paint Features 
Jetways 
Pavement Segments 
Centerlines 
Contour Lines 
Hydrography 
Building/Structures 
Fences 
Radar Sites 
Elevation Models 
Signage 
Lighting 
SMGCS Plans 
Obstacles 
Navigation Points 
Survey Control Points 
Concourses 
Highways 
Primary Roads 
Secondary Roads 
Land Use 
De-Icing Pads 
Land Fills 
 

The above table presents a list of terrestrial physical features that can be surveyed and stored in a database.  The database may also support multiple spatial models, or polygonal zones.  Polygonal zones are 2-D and/or 3-D shapes used to provide spatial cueing or visualization of data by way of illustration.  A list of themes that support various modeling constructs is presented in the following table: 

| Noise Contours      | Incursion Zones       | Movement Areas        |
|---------------------|-----------------------|-----------------------|
| Airspace Cylinders  | Ground Water Models   | De-Ice Solvent Plumes |
| Bird Strike Areas   | ILS Hold Segments     | Tower Field of View   |
| Approach/Departure  | Obstacle buffer zones | Emergency Response    |
| Time/Distance Zones | Corridors             |                       |

 
This application of aerodrome databases does not require any interfaces to real-time data and could operate on a ―stand-alone‖ basis in the flight deck. 

## A.4.2 Benefits

In addition to the graphical depiction of the aerodrome layout, spatial and tabular information included in the database could be utilized as a source of Aerodrome/Facility Directory data, NOTAM data, communications frequencies, procedures, and other textual annotation information overlaid on graphics/maps that have customarily been included in the charts/manuals.  Information could be made available in electronic format eliminating the need for paper copies of maps and charts in most instances.  For pilots, this would reduce cockpit clutter and workload during surface operations and ease flight planning activities. This electronic charting information may also be used by other aerodrome users to support: 

 
Aerodrome operations and facilities management 
 
Planning, e.g., environmental, noise, construction, etc. 
 
Leases, pavement utilization, utilities, snow removal, etc. 
 
Airline/Cargo/GA resource management 
 
ATC and apron control, routing, dispatch, and decision support tools 
 
Efficient routing of aircraft and vehicles; conflict detection and alerting 
 
Emergency response and security operations 
 
Finally, database chart information, developed in electronic form and distributed on electronic media and/or via network (or the world-wide web) connectivity, can be maintained and disseminated in an efficient, cost-effective manner to the pilot/user community. 

 

## A.5 Surveillance And Conflict (Runway Incursion) Detection And Alerting A.5.1 Operational Concept

In today's environment, flight crews maintain traffic awareness on the surface by way of frequent visual scans and, in some cases, radio communications with air traffic control (ATC) to obtain traffic advisories.  Except for a few rare runway/taxiway geometries (obtuse-angled intersections) and high-workload situations, this method of surveillance is adequate during VMC.  However, as weather conditions deteriorate (i.e., IMC), at night, or under high workload conditions, maintaining awareness of traffic on the surface can become increasingly difficult.  In these types of situations, uncertainties can arise that, in the best case, reduce flow rates, and in the worst case, increase the likelihood of a runway incursion and/or surface accident. Real-time aerodrome surface surveillance data is available via ASDE-3 radar at certain U. S. aerodromes.  This ground-based surveillance data has been provided to ATC to supplement visual acquisition.  Used in conjunction with an automation system, ASDE-3 can detect potential hazardous situations on the aerodrome surface.  This automation is called the Aerodrome Movement Area Safety System (AMASS).  AMASS provides ATC 
with alerts and warnings of unsafe traffic conditions.  Both systems, ASDE-3 and AMASS, utilize an aerodrome mapping database.  The database is used by the ASDE- 3/AMASS to depict the locations of traffic with respect to runway/taxiway edges and to detect runway incursions.  This database is not standardized and its format is proprietary in nature.  Further, the database does not lend itself to reuse by other user classes as it uses the radar's polar coordinate system (range, azimuth), which is relative to the ASDE- 3's rotating radar antenna location. 

## Figure A-3 Aerodrome Movement Area Safety System (Amass) Display8

With the advent of ADS-B and TIS-B data link services, surveillance data will become available to non-ATC users (e.g., pilots) throughout all phases of flight, including aerodrome surface operations, and even at non-towered aerodromes.  Users of this surveillance data, along with an accurate, complete, aerodrome mapping database, can then be provided with a supplemental means of observing traffic positions on the aerodrome surface in any visibility condition on a graphical display; much like the ATC use of ASDE-3/AMASS.  This overlay of traffic data onto a graphical depiction of the aerodrome will allow the user to determine ownship location as well as the relative location, velocity, identity, and intent of all aircraft/vehicles on the movement area (see Figure A-4 through Figure A-8 of this Appendix).  This application has been identified in the MASPS for ADS-B and has been demonstrated in flight on transport-category aircraft at major aerodrome facilities910. 

21-23, 1998. 
 
 
Runway incursions and potential surface collisions can be detected and presented in the cockpit using a graphical depiction of the aerodrome once surveillance data and an aerodrome mapping database are available.  Once detected, alerts can be issued to either ATC (via data link) or directly to the flight crew.  This detection and alerting can be functionally similar to the approach taken by AMASS and/or TCAS.  This runway incursion alerting concept has undergone flight simulation testing at NASA and flight testing at the Dallas-Ft. Worth International Airport12. 

## A.5.2 Benefits

For pilots, access to a Cockpit Display of Traffic Information (CDTI) during surface operations at controlled and uncontrolled aerodromes can increase traffic awareness while decreasing the uncertainties associated with available visual cues and radio communications13.  This increased awareness can: 
                                                     
 

 
Reduce the likelihood of runway incursions and surface accidents 
 
Reduce the likelihood of navigation errors on the surface 
 
Enable tighter separations on the surface and higher taxi speeds 
 
Enable strategic planning to avoid departure queues 
 
Enable strategic planning by choosing an optimum runway exit 
 
Reduce the amount of radio communications required 
 
Further, in extremely low visibility conditions (e.g., Category III-B and III-C), surface CDTI can become an enabling technology.  Despite the fact that autoland and HUD systems allow Category III-B landings, these operations are not permitted at VMC flow rates, in large part, because flight crews cannot safely perform ―see-and-avoid‖ while moving on the aerodrome surface.  A surface CDTI capability would be critical in enabling higher capacity IMC flow rates on the aerodrome surface. Finally, it should be noted that, frequently, ATC surface guidance is provided to flight crews relative to other surface vehicles.  For example, ―Delta 625, follow company traffic‖ or ―American 833, follow the 737 to your left.‖  A surface CDTI capability would support adherence to these types of instructions in limited visibility as well as reduce uncertainties that may occur when these types of instructions are issued in VMC. As mentioned earlier, ATC can also benefit from the use of aerodrome mapping databases to depict the geographic locations of aerodrome surface traffic.  This is being implemented at major U. S. aerodromes by the ASDE-3 radar system.  ASDE-3 is used as a supplemental means of surveillance for controllers working in the tower.  It is used more extensively as weather conditions deteriorate.  AMASS works in conjunction with the ASDE-3 radar to provide controllers with automatic alerts and warnings of runway incursions and other potentially hazardous situations.  The combination of ASDE- 3/AMASS is an entirely passive system that does not require any equipage on vehicles or aircraft. Airline, cargo, GA, and business aviation operations centers could also benefit from realtime surveillance data depicted on a graphical aerodrome mapping database.  This capability would enable operations that are more efficient.  For example, apron controllers can make more informed decisions about controlling the movement of aircraft and vehicles in the apron areas to avoid conflicts and to reduce delays.  In addition, scheduling and managing service vehicle operations (e.g., fuel, baggage, etc.) can be improved by tracking the location of vehicle and aircraft locations. As with pilots, the primary benefit to vehicle operators of a display of traffic information superimposed onto an aerodrome mapping database is to reduce the likelihood of runway incursions or surface accidents.  Low-cost prototype systems have been tested on vehicle platforms (e.g., emergency vehicles) that have shown the potential for this application14.  
Fire and rescue vehicles in particular can benefit significantly from this technology.  This application would allow them to accurately discern the location of accidents and choose the fastest route to the scene avoiding other surface traffic. 

## A.6 Route And Hold-Short Depiction And Deviation Detection And Alerting A.6.1 Operational Concept

In today's aerodrome environment, both departure and arrival taxi routes are provided by ATC to the flight deck by way of VHF voice radio communication.  All taxi route instructions are ―read-back‖ by the responsible flight deck crewmember to ATC as a way of confirming the instruction.  Similarly, hold-short instructions may be issued by ATC to constrain aircraft movements to avoid surface collisions, runway incursions, or ILS interference.  In the flight deck, taxi routes are memorized (and sometimes written down). Subsequently, the pilots follow relevant signage to reach the destination stand or runway. For arrivals, taxi routes are typically requested by the flight deck after clearing the arrival runway.  For departures, taxi routes are typically requested just prior to entering the movement area (on departure from the ramp/apron). For this application, taxi routes would be depicted on a graphical display of the aerodrome layout.  There are several ways in which this route could be represented (Figure A-9 and Figure A-10).   Figure A-9 depicts the taxi route as a magenta line similar to the way in which it is done on navigation displays in flight.  Figure A-9 also depicts a method of graphically representing hold-short instructions.  Red bars at ATC- designated hold points would also be displayed on the aerodrome map.  These bars are removed once ATC has cleared the aircraft to continue taxi.  These methods have been flight tested and shown to be effective.  Taxi routes and hold-short locations either can be transmitted to the aircraft, stored in a database onboard the aircraft using a standard naming convention, or entered by the crew. 

 

## A.6.2 Benefits

A graphic depiction of taxi route and hold-short locations has been shown to reduce the likelihood of pilots making navigation errors (i.e., wrong turns or runway incursions) on the aerodrome surface, while at the same time enabling an increase in taxi speed15.  This is primarily because uncertainties associated with both the visual aids (i.e., signage) and radio communications are significantly reduced.  Another contributing factor to this benefit is that the graphic depiction of taxi route and hold-short locations is a more natural representation than a series of alpha-numeric symbols that are either memorized or written down. Depending on the implementation of this application, other operational benefits are achievable.  If taxi route and hold-short locations are data linked to the flight deck via CPDLC, the probability of miscommunication and/or misunderstanding over the voice channel can be reduced.  The CPDLC instructions would serve as a reinforcement for voice communications.  This would also reduce the amount of voice traffic on the radio channel as the number of ―say agains‖ and progressive taxi instructions to pilots unfamiliar with the aerodrome would be reduced.  On the other hand, if taxi routes were entered in the flight deck (or chosen from a menu of standard routes) by the crew after receipt via radio, the operational benefits would still be achievable; as well as removing the workload of ―writing‖ and/or memorizing taxi routes and/or hold-short locations. Finally, by knowing the assigned taxi route, hold-short locations, and one's ownship position, it becomes possible to monitor route conformance during the surface operation. Deviations from route, or moving beyond a hold point, can be detected and alerts can be sent to the crew, ATC, or even other aircraft that may be impacted.  Advisories can be generated that would return the aircraft to its route in a direct safe manner. 

## A.7 Depiction Of Digital Atis Information A.7.1 Operational Concept

Listed below is a typical message received in the flight deck via the Automatic Terminal Information Service (ATIS).  ATIS messages are either pre-recorded and replayed over a radio frequency, or encoded and transmitted digitally to equipped aircraft (D-ATIS). 

ORD ATIS INFO G 1556Z. 18011KT 10SM OVC200 29/21 A2986. ARR EXP VECTORS ILS RWY 14R APCH. ILS RWY 22R ARCH. LAND AND HOLD SHORT OPERATIONS ARE IN EFFECT. RWY 14R ARR PLAN TO H/S OF RWY 27L, 9 THSD 8 HND FT AVBL. DEPS EXP RWYS 22L, 27L. NOTAMS... RWY 18, 36 CLSD, RWY 14L, 32R CLSD. TWY M CLSD BTN TW M4 AND TW M6; TWY P CLSD BTN RWY 4L AND TWY P1; TWY V2 CLSD; TWY U CLSD; TWY M5 CLSD. PILOTS USE CTN FOR BIRD ACTIVITY IN THE VICINITY OF THE ARPT. WHEN READY TO TAXI CONTACT GND METERING ON FREQ 121.67. ...ADVS YOU HAVE INFO G. 

 
The information ―Golf‖ above for Chicago's O'Hare International Airport (KORD) at 15:56 will improve the situational awareness in the flight deck once the message has been read, translated, and assimilated.  Much of this information could also be presented to the crew as a graphical display overlay that utilizes an aerodrome mapping database and an interface to the digital ATIS receiver.  Features of this graphical display could be specifically tailored to ATIS-type messages that are related to geographic information, for example: 

 
Active arrival and departure runways outlined or shaded uniquely 
 
Active ―land and hold short‖ locations depicted 
 
Closed runway or taxiway segments can be uniquely depicted 
 
Areas of potential bird strikes can be uniquely depicted 

## A.7.2 Benefits

The display described above would primarily benefit flight crews by improving situational awareness with respect to the current aerodrome configuration, conditions, and recent NOTAMs.  This approach would also reduce the likelihood of misreading the ATIS text or misunderstanding the recorded ATIS issued over the radio.  Finally, if the system were designed to automatically receive and display the ATIS information, it is more likely that the crew would be aware of the most recent ATIS update. It should be noted that a similar display resource could also benefit ATC (e.g., a graphical user interface could be used to generate ATIS information) and the operations facilities (e.g., a tool to aid in flight planning/scheduling as well as aircraft/vehicle servicing). 

## A.8 Aerodrome Surface Guidance And Navigation A.8.1 Operational Concept

One of the anticipated applications of GNSS is aircraft navigation on the aerodrome surface.  With the advent of GNSS augmentation systems16, technology will soon be available to enable aircraft to obtain accurate position information while operating on the aerodrome surface.  Standards are under development by both ICAO4 and RTCA6 in this area.  Further, proposed Required Navigation Performance (RNP) requirements have been developed by NASA for surface movement17.  Despite the capability of technology 
(i.e., GNSS) to perform the navigation function (i.e., determining position and velocity), there must be a means by which this position is relayed to the flight crew so that they can safely steer the aircraft from the current position to the desired destination.  One approach is by presenting current position to the pilot relative to geographic locations stored in an aerodrome mapping database (see Figure A-4 through Figure A-12 of this Appendix). These geographic references can be centerlines, guidance lines, runway/taxiway edges, painted markings, and/or obstructions.  Using GNSS, an accurate database, and a display, the flight crew can determine, in real-time, both lateral and longitudinal track deviations (independent of visual aids). In Figure A-4 through Figure A-12, the result of the navigation function is presented to the flight crew with respect to a virtual depiction of the runway/taxiway centerlines and/or edges.  This approach is sometimes referred to as a form of *Synthetic Vision*. Figure A-4 through Figure A-10 and Figure A-12 use a head-down display device, while Figure A-11 uses a head-up display (HUD) device.  The centerline and/or edge locations are stored in an aerodrome mapping database.  These display concepts are the result of flight simulation and flight test research activities that have demonstrated an approach to low visibility aerodrome surface guidance/navigation using GNSS and an aerodrome mapping database9, 12, 15. 

In most visibility conditions, surface navigation display functions, like the ones mentioned above, would be intended to supplement visual cues.  Visual aids such as airfield signs, painted markings, and lights would continue to be used as the primary method of guidance/navigation.  This supplemental information would be used by the crew as needed to reduce any uncertainties associated with guidance presented by the visual aids (e.g., indeterminate sign direction arrows, missing centerline paint, etc.). 

In extremely low visibility conditions or at aerodromes not equipped with sufficient visual aids, surface navigation displays (like the ones pictured) may be the primary, or sole, means of guidance/navigation.  Currently, for either of these cases, aerodrome operations cease; as there is no means of safe surface navigation. 

## A.8.2 Benefits

For pilots and vehicle operators, depiction of current position on a display (like the ones shown in Figure A-4 through Figure A-12), can result in operational benefits, particularly if current aircraft position is depicted graphically relative to geographic data.  This function provides benefits similar to those provided by Navigation Displays (NDs) that are currently being used in the flight regimes.  Access to this display during the surface operation (and prior to landing) can increase spatial awareness while decreasing uncertainties associated with available visual aids.  This increased awareness can 

 
reduce the likelihood of runway incursions and surface accidents 
 
reduce the likelihood of navigation errors on the surface 
 
enable higher roll-out, turn-off, and taxi speeds 
 
reduce the amount of radio communications required 
 
Further, as weather conditions deteriorate, these benefits become more pronounced.  In extremely low visibility conditions, this guidance/navigation tool can become an enabling technology.  Despite the fact that autoland and HUD systems allow Category III-B landings, these operations are not permitted at VMC flow rates, in large part, because flight crews cannot safely navigate while moving on the aerodrome surface.  A surface navigation function that supplements visual aids would be essential in enabling ―0/0‖ 
flight operations as well as higher capacity IMC flow rates on the aerodrome surface. 

## A.9 Resource Management A.9.1 Operational Concept

Commercial airlines, cargo airlines, and the Fixed Base Operators (FBO) who manage GA and business aviation operations, are responsible for many resources on and about the aerodrome vicinity.  Examples of these resources include: 

 
Aircraft 
 
Service vehicles 
 
Maintenance hangars 
 
Simulation facilities 
 
Apron control operations facilities 
 
Operations control centers 
 
An accurate, complete, aerodrome GIS database and associated toolset can be made available to airport operations control centers, apron control operations facilities, and maintenance facilities to improve operational efficiency.  Further, efficiency models can be developed, using ad hoc analysis or real-time methods, that maximize procedural efficiencies associated with crew bus dispatch, aircraft/vehicle routing, and asset management. A graphical depiction of aerodrome surface features, obstacles, and/or movement boundaries along with information on resource status/location can be combined in a GIS layered database that can be accessed by appropriate personnel.  Networked terminals providing access to this database can be located based on the needs of a specific airline/FBO.  In addition to aerodrome mapping information, this database can include the following types of information layers relevant to resource management: 

(1) Service facility information (2) General and business aviation maintenance areas (3) Asset identification, status, and inventory 
(4) Cargo maintenance areas (5) Parking/stand assignments and status 
(6) Airline maintenance (7) Apron route planning (8) Crew scheduling and dispatch information 
An example is the Surface Movement System (SMS) that integrates airline schedules, stand information, flight plans, radar feeds, and runway configuration (departure splits and landing direction) to improve coordination and planning of the ground aerodrome traffic operation.  The integrated information is then re-transmitted over the networked system and shared between the Air Traffic Control Supervisors, Aerodrome Managers/Operators, Air Traffic Controllers, Airline Operators, and Apron Operators at the aerodrome.  For aerodrome mapping databases (AMDBs) to be of use to SMS, the following data elements are required:  apron centerlines, apron edges, stand centerlines, stand locations, aircraft that a particular stand can handle, and stands associated with a particular apron.  Accurate standardized AMDBs would allow SMS to be more easily configured, ported, and customized to any given aerodrome surface environment. 

## A.9.2 Benefits

A spatial aerodrome surface database and an associated toolset can support varied needs of Commercial/Cargo/GA/Business aviation operators.  It addresses the need for a component-based system that can enable more efficient monitoring and movement of resources.  These resources include: aircraft, service vehicles, equipment, and crew. Valuable commodities can also be more efficiently managed including passengers, baggage, and cargo.  Tracking and identification of physical resources can also be managed using a GIS system and its associated database. 

## A.10 Training And High Fidelity Simulation A.10.1 Operational Concept

Flight simulators are used in all phases of advanced flight training/education; including pilot type ratings and regularly scheduled mission rehearsals.  Flight simulators are classified into four different quality levels (JAR-STD 1A): A, B, C, and D.  All levels require a database (JAR-STD 1A, AMC STD1A.030 paragraph 2.3) that includes: 

 
General aerodrome outline 
 
All runways 
 
Glide slope transmitter position for all runways 
 
Position of the glide slope receivers for all runway 
 
Type of approach lighting system for all runways 
 
In addition, level D certified visual systems (JAR-STD 1A, AMC STD1A.030 paragraph 2.3) require sufficient scene content to recognize: 

 
Aerodrome features 
 
Terrain with major terrain features 
 
Major landmarks around the aerodrome 
 
Far beyond these requirements, state-of-the-art flight simulator databases also have: 

 
Taxiway outlines 
 
Taxiway markings 
 
Taxiway signs 
 
Apron markings 
 
Parking positions 
 
Aerodrome buildings 
 
Gates and jetways 
 
Current training simulation systems only provide relative positions. With the introduction of new aviation procedures such as GNSS approaches, all simulation aerodrome databases will need to be geo-referenced to precise absolute three-dimensional positions. WGS84 geo-referencing is required to be GNSS compliant.  The simulator integration of Terrain Awareness Warning Systems (TAWS) requires terrain and obstacle information in the vicinity of the aerodrome.  For simulation purposes, precise aerodrome data is needed after integrating next-generation navigation displays with moving map taxiguidance functionality. For realistic training, all geo-spatial information stored within each individual aircraft system (e.g., TAWS, FMS, ND, etc.) will have to match the database stored in the simulator's visual database.  The only common reference system that these distinct systems share is an absolute positioning system based on geo-coordinates. 

## A.10.2 Benefits

All simulator database vendors can use geo-referenced aerodrome databases as the basis for future simulator visual databases.  Currently, they replace all available databases to make them compliant with geo-referenced GNSS approach procedure requirements.  Cost can be significantly reduced by the availability of aerodrome databases.  Even current geo-referenced databases used in simulators can be enriched with additional more precise geo-information. Problems with an insufficient matching of moving map guidance displays and algorithms such as those employed by TAWS can be avoided if the databases used to generate visual scenes in simulators are consistent with (if not identical) to those used onboard aircraft. 

## A.11 Aerodrome Facility Management A.11.1 Operational Concept

There are six primary categories of activities that come within the scope of aerodrome facility management: 

 
Planning 
 
Airfield design 
 
Facility design 
 
Construction 
 
Environmental 
 
Administration 
Each of these activities can benefit from the availability of an aerodrome database.  To ensure consistency across the applications, a Geographic Information System (GIS) layered database structure with attribute data can be utilized.  Every aerodrome implementation will be unique.  It is anticipated that the primary repository for this database will be some form of an Aerodrome Operational Control Center (OCC). Secondary repositories, with full functionality, may be located at Maintenance Control Centers (MCCs), Aerodrome Engineering Centers (AECs), and Movement Area Control Centers (MACCs). 

The current problem at most aerodromes is the establishment of ―data islands‖ within each aerodrome organization.  Consequently, the practice has been to develop databases for a specific need.  The result has been duplicated databases with inconsistent key fields and an environment where no standards exist.  Many aerodrome departments use incompatible vendor-specific formats that lead to inefficiencies and low performance, as well as high costs and low quality.  Storing data in a GIS database structure can result in tremendous efficiencies being realized. 

## A.11.1.1 Planning

Capacity, land use, noise, and environmental management are all issues facing the aviation industry.  The planning process is integral to developing and maintaining aerodromes and resolving issues relating to technical and legislative changes that affect the individual aerodrome, and the industry as a whole.  Planning databases may contain layered information that would be resident in an enterprise database schema. 

## A.11.1.2 Airfield Design

Heavier aircraft and increased operations are producing a strain on airfields worldwide. Aerodromes are quickly approaching capacity, while runway, taxiway, and apron availability is becoming severely limited.  Pavement at many aerodromes is far beyond its useful life and is failing.  In addition, recent changes to airfield signage requirements have resulted in a need to install new signs at aerodromes.  Aerodrome design database information must account for present and future needs.  In order to meet these requirements, the data must be retrievable in such a way that it can be used by consultants, planners, and designers to develop three-dimensional simulations of the aerodrome.  These simulations will allow multiple alternative schemes to be assessed before any one scheme is adopted. 

## A.11.1.3 Facility Design

Roadways, buildings, mechanical, electrical, and plumbing systems are special issues that arise when facilities are located on aerodromes.  Facility design database information should include the requirements for safety, airspace restrictions, operational issues, noise abatement issues, environmental issues, and revenue-generation issues such as terminal space leasing to tenants. 

## A.11.1.4 Construction

Construction personnel, managers, and inspectors require specific information when operating in an aerodrome environment.  Databases are required to understand individual airfield operations, government regulations, aerodrome safety requirements for construction, and coordination of construction activities. Construction management services on aerodrome projects may require information on special phasing considerations to prevent operational interruptions.  To reduce administrative burdens and related costs incurred by aerodromes and aerodrome planning boards, cooperation between planner, designer, contractor, construction manager, and the aerodrome administration are critical for both large and small projects. 

## A.11.1.5 Environmental

Virtually every aerodrome project has a critical need to identify and define environmental issues and solutions that provide for a realistic design and implementation plan.  Issues of concern to aerodrome operators include performing environmental evaluations of facilities, providing training for personnel, administering environmental programs, and developing environmental manuals. 

## A.11.1.6 Administrative

Aerodrome planning boards have requirements for familiarity with the policies, procedures, and internal structures of each aerodrome, and the sources that fund work to be performed at each aerodrome.  To that end, each aerodrome must maintain close relationships with the national aviation authorities, and must have a thorough understanding of any plan to develop and expand aerodromes.  The information maintained in databases assists the aerodrome staff in preparing development strategies for aerodrome improvements. 

## A.11.2 Benefits

The benefits for aerodrome facility management are categorized as: 

 
Reduced staff time for analysis 
 
Quick response to questions 
 
Ability to address complex issues 
 
Ability to provide better information to the decision makers 
 
Reduced cost to develop applications 
 
Creation of a basic framework to administer geospatial data 
 
The use of consistent, standardized data results in the creation of an efficient data warehouse for the aerodrome organization.  The data warehouse concept results in beneficial data management and analysis technology and techniques.  The data are used to enhance the value of the aerodrome's data by replication, and it becomes more than just data, it becomes a set of tools.  The initial creation of a data warehouse requires a commitment of resources.  However, the payback to the aerodrome organization can be realized in multiple efficiencies. Another benefit of such a database is the capability of data to retain its natural spatial information.  For example, data can be visualized as in the real world and thus, can create a common language for the aerodrome organization to use.  In addition, spatial queries will serve to broaden the information that is available, and users will want to use the system because it is user-friendly and intuitive. Some of the benefits of standard data are: 

 
Ease of processing and integrating data into various applications 
 
Longevity given to the data 
 
Assistance given in maintaining links to the legacy systems 
 
Ensured compatibility between systems 
 
Cooperation facilitated between database application developers 
 
Opening to additional external sources of data 
 

## A.12 Emergency And Security Services Management A.12.1 Operational Concept

A critical need exists to integrate the system designs of the adverse weather navigation systems being developed for aerodromes.  Systems are being developed for both aircraft and aerodrome ground vehicles (e.g., emergency and security vehicles).  The problems and requirements related to central control and safe operation during simultaneous surface movement of a mixed vehicle fleet are broad in scope.  Challenges exist under normal and emergency conditions that require all vehicles be controlled, monitored, and managed by a central control function.  All aerodrome surface vehicles (i.e., aircraft and vehicles) must use common guidance reference data having a specific accuracy to prevent potential problems that would be associated with uncoordinated activities during adverse weather conditions.  It becomes essential that cost-effective and dependable methods and designs be developed that will ensure safe operation of a mixed fleet consisting of aircraft and ground vehicles when operated simultaneously during adverse weather conditions. Driven by the need to respond quickly to accidents or security breeches occurring in poor visibility conditions, ground vehicles can be outfitted with equipment to improve response capabilities.  The capabilities provided can enable the Aerodrome Rescue and Fire Fighting (ARFF) operations centers and the fire fighters themselves to more quickly locate a fire/crash sight during the times of adverse visibility (i.e., at night and/or during poor weather conditions).  Security operations centers and the associated personnel and vehicles have similar needs when responding to a site where there is a potential security threat. 

Using a Primary Base Station (PBS) located in an aerodrome Operations Communications Center (OCC), coordination and management of emergency and security services can be performed.  These services include: 

 
Tracking vehicle location and identity 
 
Maintaining/distributing checklists and procedures 
 
Monitoring vehicle status 
 
Acquiring aircraft data 
 
Acquiring incident status data 
 
Acquiring hazardous material information 
 
Enabling/disabling alarm functions 
 
Dispatching emergency/security resource 
 
The PBS display can be supported by a GIS map database of the aerodrome and surrounding area to include the Aerodrome Emergency Plan (AEP) area; typically a five mile radius from the end of each runway.  Further, the map database can be layered with the option of displaying any combination of informational layers available to either the control center or the vehicle. 

## A.12.2 Benefits

Emergency and security vehicles outfitted with equipment and aerodrome surface databases as described will be able to respond even faster and with more situational awareness particularly in poor visibility conditions.  OCCs will be able to work more efficiently to control and monitor movements to ensure conflict avoidance and rapid response.  The use of common guidance information, having a high degree of integrity, can prevent potential problems that would be associated with uncoordinated activities during adverse weather conditions.  Development of aerodrome surface databases used to support simultaneous surface movement of  mixed vehicle and aircraft fleets can increase safety margins and performance.  Emergency and security operators using aerodrome databases and associated displays (Figure A-13) can also: 

 
Reduce operator workload 
 
Increase coordination/dispatch capabilities 
 
Enable clear, unambiguous communication of information  
 
Enable drivers to travel the most direct routes to a prescribed destination (e.g., fire 
location) quickly and safely regardless of visibility 

## A.13 Runway Operations A.13.1 Operational Concept

Using a robust position sensor (e.g., augmented GNSS), a display (either auditory or graphical), and an adequate aerodrome database, guidance can be provided in real-time to pilots so that they can effectively manage aircraft energy and location during takeoff and during landing roll-out and turn-off from the runway. During takeoff, access to sufficient runway information can allow a guidance profile to be generated based on conditions that may be changing dynamically.  This guidance can be provided on either the PFD, ND, HUD, or any other available display in the flight deck.  Further, important situational information could be provided, such as where on the runway the aircraft is projected to reach specific V speeds and where the flight crew would need to consider a departure-abort.  Finally, alerts could be generated to warn the pilot if there is insufficient runway remaining to either perform a departure-abort or to lift-off. Similarly, during the last stages of landing (e.g., the flare) and during landing roll-out and runway exit, sufficient runway information could enable guidance profiles to be generated to aid the pilot's decision making in these critical stages.  This guidance could be tailored to provide several functions: 

 
Warning if landing fast or long 
 
Guidance to optimal touchdown point 
 
Flare guidance 
 
Optimal guidance to desired exit 
 
Runway remaining guidance 
 
Warning of potential overrun 
 
Deceleration guidance to ensure passenger comfort and reduce brake wear 
 
Finally, in conditions of low visibility or at night, this application could help the pilot ensure that he is maintaining an appropriate track, both laterally and longitudinally, during takeoff roll, landing roll-out, and normal taxi.  In conditions of good visibility, this is done using visual references such as center lines/lights, runway edge lines/lights, and runway remaining signs.  An aerodrome moving map could be used to prevent runway excursions, whereby the landing gear exits the runway or taxiway, leading to aircraft shutdown, and tow. A great deal of research has been done involving these applications at various research centers.  For example, NASA has developed a Takeoff Performance Monitoring System (TOPMS) and a Roll-out Turn-off (ROTO) guidance system.  Both of these conceptual systems were designed to provide many of the functionalities described above. 

## A.13.2 Benefits

Potential benefits of this application for takeoffs include: 

 
Reduced number of departure-aborts 
 
Reduced likelihood of takeoff accidents 
 
Optimized aircraft performance during departure roll 
 
Improved fuel efficiency Potential benefits of this application for arrivals include: 
 
Reduced number of overruns 
 
Reduced number of go-arounds 
 
Reduced/predictable roll-out times in any visibility or weather condition 
 
Reduced brake wear 
 
Optimized aircraft performance 
 
Fewer runway excursions 
 

## A.14 Notice To Airmen (Notam) And Aeronautical Data Overlays A.14.1 Operational Concept

Aeronautical data overlays, including aerodrome NOTAMs, are one kind of advisory information that could be disseminated to flight crews using a Flight Information Services - Broadcast (FIS-B) data link system.  FIS-B is an emerging data link concept (with several implementations underway) that is intended to provide weather and other flight advisory information to pilots in a way that will enhance their awareness of the flight situation and enable better strategic decision-making.  The information provided through FIS-B will be advisory in nature, and is considered non-binding advice and information provided to assist in the safe conduct of a flight.  With this information, pilots will be better able to assess potential hazards as well as make better decisions that will improve operational safety and efficiency. At present when the weather deteriorates, voice radio calls from pilots to air traffic controllers or to flight service station specialists requesting FIS-B kinds of information become more necessary and more frequent.  This clogs voice radio frequencies just when the demand for the data is the highest.  It is envisioned that FIS digital broadcast data will be continuously received and stored to be readily available as needed or requested by the pilot. 

Implementation of an FIS-B data link system is not intended to replace existing voice radio FIS services.  Loss or non-receipt of FIS-B data link services would not be considered flight critical.  In the initial implementation, it is anticipated that FIS-B data link services will be used primarily to supplement or complement established sources of weather and operational information, including receipt of an integrated aeronautical information package prior to departure.  Existing sources such as the Flight Service Station network, ATC facilities, and/or the corporate/airline dispatchers, would still be available to provide timely data. In the end state, FIS-B services will assist both individual pilot and collaborative decision making (CDM) processes. As envisioned, graphical or other display of NOTAM information can be facilitated by the Aerodrome Mapping Database (AMDB).  A comprehensive AMDB will include all the required ―raw materials‖ for depiction of graphical NOTAMs, such as runways, taxiways, and aerodrome structures.  The NOTAM and aeronautical data overlay concept is an operational concept as to how graphical NOTAMs / aeronautical data could work with the AMDB.  In the envisioned application, the graphical display of the data can be described as overlay graphics referenced to and correlated with AMDB objects.  For example, a runway closure could be depicted as a graphical overlay of the runway object stored in the AMDB.  An example is given below. 

## A.14.2 Benefits

The anticipated benefits of this concept are as follows: 

 
Better and more efficiently communicated information 
 
―One-stop‖ shopping for information 
 
Enhanced situational awareness 
 
Less reliance on today's dispatch release form 
 
Less concern that inaccurate, incomplete, or out-dated information was being made available 
 
En route updates would be updated by FIS data link, and provided as textual and as graphical overlay products 
 
Near instantaneous dissemination of SUA and aerodrome-related NOTAM's and related information 
 
Reduced communications costs because of use of a public use, not dedicated, land line system 
 
Less data entry delay because other parties other than the source originator would be eliminated from the process of data entry and verification.  The originator would enter time-perishable data directly into the system, with little if any delays 
 

## 

List of selected NOTAMs that could be graphically displayed using an AMDB 
NOTAM 
Attribute Specification 
Closed runways 
Object name (runway), closed, reason, surface referencing polygon 
Closed taxiways 
Object name (taxiway), closed, reason, 
surface referencing polygon 
Designated construction areas 
Object name, reason, surface bounding 
polygon, hours of construction activity 
Temporary grass cutting, snow plowing operations, agricultural activity / areas Clutter/contamination on specified runways and taxiways Lighting equipage and status (VASI, PAPI, ALSF-2, etc) Signage (e. g., missing, blownover, obscured, etc) Runway and taxiway markings (e.g., worn, missing, snow covered, etc) Areas of low-braking effectiveness Engine maintenance run-up areas and heading alignments Location of FBOs on aerodrome with available parking highlighted (general aviation parking/refueling areas) 

## 

 
Object name, closed, reason, surface referencing polygon, time started, time ended Object name, reason, amount, surface 
bounding polygon 
Object name (light), location, status 
Object name (signage), location, status 
Object name (runway), surface type, surface condition, paint, status, surface 
referencing polygon 
Object name(designated area on apron)), 
special comments, referencing polygon 
Object name (designated area on aerodrome), heading alignment required, special comments, referencing polygon Object name (surface non movement area), special comments, surface referencing polygon 
Designated customs clearing parking areas 
Object name (designated surface non movement area), special comments (e.g., hours of operation; alternative parking area after hours),  surface referencing 
polygon 
Communication frequencies 
Object (active aerodrome surface communication frequencies), description, referencing polygon 
Gate/apron closures 
Object name (gate/apron), closed, reason, 
surface referencing polygon 

## A.15 Aerodrome Asset Management On The Aerodrome Surface Using Hand-Held Computers A.15.1 Operation Concept

In today's busy aerodrome environment, aircraft frequently arrive at an aerodrome only to find that they must wait for an available gate or, wait for a ramp agent to reposition the ramp-way to the aircraft.  Additionally, service vehicles (such as refueling trucks); often spend extra time searching for parked aircraft, especially at night, often without any mechanical or electronic means to assist them. At very busy aerodromes, surface movement delays often produce ripple effects that extend well beyond the ramp area and into the aerodrome surface movement.  For instance, surface and ―push-back‖ delays directly affect departure timing.  Oceanic flight ―slot times‖ at track entry fixes are very sensitive to these delays.  Missing a departure slot can easily delay the takeoff of a flight for several hours. Sometimes delays can affect safety.  For example, sequencing to de-icing areas, and subsequent ―hold-over‖ times prior to takeoff, are all subject to critical timing and scheduling to minimize delay.  It is in this operational context that airline, aerodrome staff, and air traffic managers must have a common, shared, situational awareness. In the following concept of operations, appropriate personnel would be equipped with a small hand-held computer device.  Each computer would have a flash card for wireless communication via TCP / IP with a local, Intranet-based, aerodrome information system. Each computer would also have a small database that would contain aerodrome slot information, and would receive on-line flight plan data from ICAO FPL, DEP, DLA, CNL and CNG messages, as well as actual data from departure and arrival movement or ACARS messages.  A simple installed software application would convert flight plan information into intuitive graphics.  This software would create and position special color-coded icons on the display (see Figure A-15).  These depictions would be displayed in a time-line based manner. In the depiction, below, the ―beginning‖ and ―end‖ of the orange shape represent the arrival and departure aerodrome slot times.  The dark blue shapes depict the estimated out, off, on, and in times (i.e., off-block, takeoff, landing and in-block times) as well as the estimated turn-around times between two flight segments.  The green shapes would be resized depending on the actual times while the vertical magenta line would show the current local time.  ADS-B and TIS-B data would provide this information, including providing accurate surface movement predictions.  Differences between the assigned aerodrome slots and the planned / actual times would also be graphically depicted.  The user could zoom the map, and scroll the picture for better visualization of a specific aircraft or vehicle.  The aircraft's identification and current position would be depicted and electronically transferred (by use of ADS-B or other data link) to the aerodrome information system, which would then re-broadcast it. Each computer would have a GPS flash card, allowing aerodrome management to know where all surface vehicles are, assuming that there is GPS line-of-sight coverage. A GSM flash card could provide each device with access to the local aerodrome map data base or to other aerodrome information systems.  This same concept could include aerodrome refueling, baggage, and servicing vehicles.  Graphical ATIS and graphical NOTAM ―overlay‖ information could also be displayed on these small screens to assist ground personnel. These devices would be equipped with tactile displays.  Ramp agents and others could then use these input devices to enter ―operational events‖ (such as the beginning and end of servicing) by simply touching the buttons on the screen with a stylus or finger.   
 

## A.15.2 Benefits

This application could reduce surface movement delays, thereby enhancing airline and facility operational efficiency.  Collectively, these applications would assist airline employees in better synchronizing work tasks with aircraft arrival and departure schedules.  Dispatchers and ramp controllers would know the precise location of all aircraft and their status.  Gate agents would know exactly when an aircraft would arrive at a stand / gate.  Refuelling vehicles, service vehicles, and emergency response vehicles could easily locate a specific aircraft (especially if it was remote parked). 

## A.16 Synthetic Vision A.16.1 Operational Concept

An aircraft's ability to conduct flight operations at aerodromes is dependent upon a number of factors.  Among these, reduced visibility is a significant factor.  As weather and visibility conditions deteriorate, it is increasingly difficult to conduct flight operations in the same manner and at the same rate as in visual metrological conditions.  
While today's technology provides solutions to many of the problems caused by low visibility, the potential now exists to provide information well beyond what the pilot is able to see even on a clear day.  The operational concept is to create a virtual visual environment that all but eliminates reduced visibility as a significant factor in flight operations, and enhancing what the pilot can see even in the best of visibility conditions19.  A virtual visual environment can be described in terms of its components and the operational flight phases it supports. 

With respect to aerodrome operations, the synthetic vision ―virtual visual environment‖ is composed of three components:  an enhanced intuitive view of the aerodrome environment, conflict detection and display, and precision navigation guidance.  The intuitive view is derived from an aerodrome mapping database with multi-system information superimposed or overlaid.  This information is comprised of tactical information typically found on a primary flight display as well as strategic information typically found on a navigation display.  Since cluttered displays are undesirable, pilots will need the ability to choose certain features so that the system and its displays will be able to present an intuitive and simple-to-comprehend visual depiction. Many of the applications already listed in this appendix have already been demonstrated in the operational environment using synthetic vision technology including: 

 
Surveillance and conflict (runway incursion) detection and alerting 
 
Route and hold-short depiction and deviation detection and alerting 
 
Depiction of digital ATIS information 
 
Aerodrome surface guidance/navigation 
 
Runway operations 
 
The reader is referred to the sections of this appendix that describe these applications in greater detail for sample synthetic vision display formats. 

## A.16.2 Benefits

Current technology systems allow flight crews to perform ―all-visibility‖ en route flight operations as well as low-visibility approaches and landings to appropriately equipped runways.  Synthetic vision systems have the potential to go beyond this present capability, and to extend it to include all-weather surface operations.  Such an expanded capability will enhance safety and provide operational benefits.  Some synthetic vision systems are expected to emulate day visual flight operations at night and in limited visibility conditions.  Others will provide visual cues commensurate with an ego-centered VMC view from the cockpit.  Using synthetic vision systems, the overall accident rate and hull loss rate is expected to become that of day visual flight operations.  Some of the expected safety benefits with respect to aerodrome operations include:  runway incursion risk reduction, improved pilot situational awareness, improved non-normal situation response, and improved compliance with air traffic clearances and instructions.  Potential capacity and efficiency benefits have also been identified, including reduced arrival and departure minimums, inclusion of additional multi-runway operations, and greater aerodrome access. 

## B Glossary Accuracy

A degree of conformance between the estimated or measured value and the true value.  Note: for measured positional data, the accuracy is normally expressed in terms of a distance from a stated position within which there is a defined confidence of the true position falling.  [ICAO Annex 14]  Note: relative accuracy is defined with reference to a geodetic datum. 

## Aerodrome (Airport)

A defined area on land or water (including any buildings, installations, and equipment) intended to be used either wholly or in part for the arrival, departure, and surface movement of aircraft.  [ICAO Annex 14] 

## Aircraft Stand

A designated area on an apron intended to be used for parking an aircraft.  [ICAO Annex 14] 

## Aerodrome Elevation

The elevation of the highest point of the landing area.  [ICAO Annex 14] 

## Aerodrome Mapping Database (Amdb)

One or more files containing information in a digital form that represent selected aerodrome features.  This data includes geo-spatial data and metadata over a defined area.  The files have a defined structure to permit an AMDB management system and other applications to make revisions that include additions, deletions, or modifications. 

Aeronautical Data  
Data used for aeronautical applications such as navigation, flight planning, flight simulators, terrain awareness, and other purposes, which comprises navigation data, terrain, and obstacle data.  [DO-200A/ED-76] 

## Aeronautical Database

Any data that is stored electronically in a system that supports airborne or ground based aeronautical applications.  An Aeronautical Database may be updated at regular intervals. [DO-200A/ED-76] 

## Aeronautical Data Preparation Agency

An agency, public or private, other than an originator and/or publisher of government source documents, who compiles official government document information into charts or electronic formats for computer-based systems. [DO-201A/ED-77] 

## Aeronautical Information Publication (Aip)

A publication issued by or with the authority of a State and containing aeronautical information of a lasting character essential to air navigation. [ICAO Annex 15] 

## Aeronautical Information Regulation And Control (Airac)

A regulated system aimed at advanced notification based on common effective dates of circumstances that necessitate significant changes in operating practices. [ICAO Annex 15] 

## Aerodrome Reference Point (Arp)

The designated geographical location of an aerodrome.  [ICAO Annex 4] 

## Aerodrome Surface Movement Area

That part of an aerodrome (aerodrome) that is to be used for the takeoff, landing, and taxiing of aircraft.  This includes runways, taxiways, and apron areas. 

## Altitude

The vertical distance of a level, a point, or an object considered as a point, measured from mean sea level (MSL). [ICAO Annex 4] 

## Approved Source

An approved source is: 

 
a State that provides aerodrome mapping data with sufficient information so that the end-user can check that those data are suitable for its own application. 
 
a supplier accredited against this standard and the DO-200A/ED-76 by an appropriate organization. 

## Apron

A defined area, on a land aerodrome, intended to accommodate aircraft for purposes of loading or unloading passengers, mail or cargo, fuelling, parking, or maintenance. [ICAO Annex 14] 

## Arresting Gear Location

Location of the arresting gear cable across the runway. 

## Assemble (Merge)

A process of merging aeronautical information from multiple sources into a database and establishing a baseline for subsequent processing.  The assemble phase includes checking the data and ensuring that detected errors and omissions are rectified. [ICAO Annex 15] 

## Blastpad

Specially prepared surface placed adjacent to the end of a runway to eliminate the erosive effect of the high wind forces produced by airplanes at the beginning of their takeoff roll. 

## Blunder Errors

From the statistical point of view, blunders or mistakes are observations that cannot be considered as belonging to the same sample from the distribution in question. They should not be used with other observations. They should be located and eliminated. 

## Circular Error Probability (Cep)

CEP refers to the radius of a circle within which a stated percentage of measurements for a given point will fall. For example, if the horizontal accuracy of a surveyed point is stated as 1 m with 90% CEP, then 90% of measurements of this point will fall within a circle of radius 1 m. The true position is then estimated to lie at the center of this circle. Note: for GPS, CEP is usually stated at 50%. 

## Completeness

The primary quality parameter describing the degree of conformance of a subset of data compared to its nominal ground with respect to the presence of objects, associations instances, and property instances. 

## Computer-Based Systems

Systems operating from pre-assembled aeronautical databases. Systems include, but are not limited to, Area Navigation Systems, Flight Management Systems, Flight Planning Systems, Flight Simulators, Computer Modeling, and Design Systems. [RTCA DO-201A/EUROCAE ED-77] 

## Confidence

Meta-quality element describing the correctness of quality information. 

## Confidence Level

The probability that the true value of a parameter is within a certain interval around the estimate of its value.  The interval is usually referred to as the accuracy of the estimate. 

## Construction Area

Part of a movement area under construction. 

## Correct Data

Data meeting stated quality requirements. [DO-201A/ED-77] 

## Corruption

A change to previously correct data introduced during processing, storage, or transmission, which causes the data to no longer be correct. [DO-200A/ED-76] 

## Database

One or more files of data so structured that appropriate applications may draw from the files and update them.  This primarily refers to data stored electronically and accessed by computer rather than in files of physical records.  [ICAO Annex 15] 

## Data Element

A term used to describe any component of an AMDB. For example: a feature, an attribute, an object, an entity, or a value. 

## Data Quality

A degree or level of confidence that the data provided meets the requirements of the data user in terms of accuracy, resolution, and integrity.  [ICAO Annex 15] 

## Datum

A point, line, surface, or set of values used as a reference.  A geodetic datum is a set of constants specifying the coordinate system and reference used for geodetic control (i.e. for calculating coordinates of points on the earth).  At least eight constants are needed to form a complete datum: three to specify the location of the origin of the coordinate system; three to specify the orientation of the coordinate system; and two to specify the dimensions of the reference ellipsoid.  [FAA doc. 405] Any quantity or set of quantities that may serve as a reference or basis for the calculation of other quantites. [ISO 19104] 

## Deficiency

The aeronautical data process is not adequate to ensure that data quality requirements are satisfied. [DO-200A/ED-76] 

## De-Icing Pad

An area comprising an inner area for the parking of an airplane to receive de-icing treatment and an outer area for the maneuvering of two or more mobile de-icing equipment.  [ICAO Annex 14] 

## Displaced Threshold

A threshold not located at the extremity of a runway.  [ICAO Annex 14] 

## Distribution (Paper)

The process of disseminating documents containing formatted aeronautical data in various media, including the shipping and loading of a database into the target system for application. [DO-201A/ED-77] 

## Distribution (Data)

The process of duplication of formatted aeronautical data into a database and the shipping and loading of the database into the target system for application. Distribution is usually achieved by transferring the data from one medium to another, with each transfer being verified. [DO-200A/ED-76] 

## Draping

Digital overlaying of one spatial dataset onto another, where both datasets have been georectified (digitally matched) to the same coordinate system and map projection. Particularly useful in 3D visualizations of spatial data.  Example:  draping a satellite image over terrain data and creating a fly-through visualization in motion. 

## Elevation

The vertical distance of a point or a level, on or affixed to the surface of the earth, measured from mean sea level (MSL). [ICAO Annex 4] 

## Ellipsoid Height (Geodetic Height)

The height related to the reference ellipsoid, measured along the ellipsoidal outer normal through the point in question. [ICAO Annex 14]. 

## End User

See User. 

## Enterprise Data

Common data used by multiple users but stored at a single location. 

## Feature

Abstraction of real-world phenomena. [ISO 19101] Note: a feature may occur as a type or an instance. Feature type or feature instance should be used when only one is meant. 

## Final Approach And Takeoff Area (Fato)

A defined area over which the final phase of the approach maneuver to hover or landing is completed or from which the takeoff maneuver is commenced. 

## Format

The process of translating, arranging, packing, and compressing a selected set of data for distribution to a specific target system. [DO-200A/ED-76] 

## Frequency Area

Designated part of a surface movement area where a specific frequency is required by air traffic control or ground control. 

## Geodetic Datum

A minimum set of parameters required to define location and orientation of the local reference system with respect to the global reference system/frame.  [ICAO Annex 14] 

## Geodetic Distance

The shortest distance between any two points on a mathematically defined ellipsoidal surface. [ICAO Annex 15] 

## Geographic Coordinates

The values of latitude, longitude, and height that define the position of a point on the surface of the Earth with respect to a reference datum. 

## Geoid

The equipotential surface in the gravity field of the Earth that coincides with the undisturbed mean sea level (MSL) extended continuously through the continents. Note:  the geoïd is irregular in shape because of local gravitational disturbances (wind tides, salinity, current, etc.) and the direction of gravity is perpendicular to the geoid at every point.  [ICAO Annex 14] 

## Geoid Undulation (Geoid Height)

The distance of the geoïd above (positive) or below (negative) the mathematical reference ellipsoid.  Note: with respect to the WGS-84 defined ellipsoid, the difference between the WGS-84 ellipsoidal height and orthometric height represents WGS-84 geoïd undulation.  [ICAO Annex 14] 

## Global Navigation Satellite System (Gnss)

The GNSS is a world-wide position and time determination system, that includes one or more satellite constellations, aircraft receivers, and system integrity monitoring, augmented as necessary to support the required navigation performance for the actual phase of operation. [ICAO Doc 9524] 

## Helipad

A small designated area, usually with a prepared surface, on a heliport, aerodrome, landing/takeoff area, apron area, or movement area used for takeoff, landing, or parking of helicopters.  [FAA doc. 405] 

## Heliport

An aerodrome or a defined area on a structure intended to be used wholly or in part for the arrival, departure, and surface movement of helicopters.  [ICAO Annex 14] 

## Hotspot

A location on an aerodrome movement area with a history or potential risk of collision or runway incursion, and where heightened attention by pilots/drivers is necessary. [ICAO Annex 4] 

## Imagery

The product of photography or advanced imaging sensors.  Can be produced via either aerial or satellite fly-overs. 

## Integrity Of Aeronautical Data

A degree of assurance that an aeronautical data and its value have not been lost or altered since the data origination or authorized amendment. [ICAO Annex 14] 

## Land And Hold Short Operations (Lahso) Location

Marking used for Land and Hold Short Operations (LAHSO). 

## Linear Error Probability (Lep)

LEP refers to a linear magnitude within which a stated percentage of measurements for a given point will fall. For example, if the vertical accuracy of a surveyed point is stated as 1 m with 90% LEP, then 90% of measurements of the height of this point will fall along a vertical line of length 1 m. The true position is then estimated to lie at the center of this vertical line. Note: LEP is the one-dimensional form of CEP. 

## Maneuvering Area

That part of an aerodrome to be used for the takeoff, landing and taxiing of aircraft, excluding aprons. [ICAO Annex 14] 

## Marking

A symbol or group of symbols displayed on the surface of the movement area in order to convey aeronautical information. 

## Mean Sea Level (Msl)

The average location of the interface between the ocean and the atmosphere, over a period of time sufficiently long so that all random and periodic variations of short duration average to zero.  [FAA doc. 405] 

## Metadata

Data about data. [ISO 19115] Note : data that describes and documents data.  

## Movement Area

That part of an aerodrome to be used for the takeoff, landing and taxiing of aircraft, consisting of the maneuvering area and the apron(s). 

## Multi-Ring Polygon

One or more polygons located inside another polygon that excludes the area of the inner polygons (e.g. doughnut, figure eight) 

## Notice To Airmen (Notam)

A notice distributed by means of telecommunication containing information concerning the establishment, condition, or change in any aeronautical facility, service, procedure, or hazard, the timely knowledge of which is essential to personnel concerned with flight operations.  [ICAO Annex 15] 

## Obstacle

All fixed (whether temporary or permanent) and mobile objects, or parts thereof, that are located on an area intended for the surface movement of aircraft or that extend above a defined surface intended to protect aircraft in flight.  [ICAO Annex 14] 

## Obstruction

Any object that penetrates an obstruction identification surface.  Note that this is considered a subset of the ―Obstacle‖ definition, Note (2) please refer to section 6.3 for a discussion of Special Cases.   [FAA doc. 405] 

## Obstruction Identification Surface

Any imaginary surface authorized by the FAA to identify obstructions.  [FAA doc. 405] 

## Originator (Data)

The first organization in the aeronautical data chain that accepts responsibility for the data. For example, a State or DO-200A/ED-76-compliant organization. [DO- 200A/ED-76] 
 

## Orthometric Height (Or Elevation)

Height of a point related to the geoid, generally presented as an MSL elevation. [ICAO Annex 14] 

## Painted Centerline

Continuous line along the painted line in the center of a runway connecting the two thresholds.  

## Pavement Classification Number (Pcn)

A number expressing the bearing strength of a pavement for unrestricted operations. [ICAO Annex 14] 

## Position (Geographical)

Set of coordinates (latitude, longitude) referenced to the mathematical reference ellipsoid that define the position of a point on the surface of the Earth. [ICAO Annex 15] 

## Precision

The smallest difference that can be reliably distinguished by a measurement process. Note:  in reference to geodetic surveys, precision is a degree of refinement in performance of an operation or a degree of perfection in the instruments and methods used when making measurements.  [ICAO Annex 15] 

## Quality

Totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs.  Note: entity is an element that can be individually described and considered.  (ISO 8402) [ICAO Annex 15] 

## Quality Assurance

All the planned and systematic activities implemented within the quality system, and demonstrated as needed, to provide adequate confidence that an entity will fulfill requirements for quality.  (ISO 8402) [ICAO Annex 15] 

## Radiometric Resolution

The capability of a sensor to discriminate levels or intensity of spectral radiance.  In the analogue systems such as photography, the radiometric resolution is measured based on the number of gray levels that can be obtained.  In opto-electronic systems, the radiance is recorded in an array of cells. A digit is assigned to each cell proportional to the received level of energy. This is done by an analog to digital converter in the platform.  Generally, in modern sensors the range is between zero radiance into the sensor and 255 at saturation response of the detector. 

 

## Ramp

See Apron. 

## Random Errors

Random errors of observations refer to the basic inherent property that estimates of a random variable do not agree, in general, with its expectation. 

## Reference Ellipsoid

A geometric figure comprising one component of a geodetic datum, usually determined by rotating an ellipse about its shorter (polar) axis, and used as a surface of reference for geodetic surveys.  The reference ellipsoid closely approximates the dimensions of the geoid, with certain ellipsoids fitting the geoid more closely for various areas of the earth.  Elevations derived directly from satellite observations are relative to the ellipsoid and are called ellipsoid heights.  [FAA doc. 405] 

## Repeatability

The level to which a measurement, when repeated, will agree with the previous value.  The consistency of results provides a measure of the degree of repeatability, though not necessarily its accuracy. In determining the consistency, the precision of the repeated measurements are taken into account). [DO-201A/ED-77] 

## Resolution

A number of units or digits to which a measured or calculated value is expressed and used. [ICAO Annex 15] 

## Runway

A defined rectangular area on a land aerodrome prepared for the landing and takeoff of aircraft.  [ICAO Annex 14] 

## Runway Exit Line

Guidance line painted on the runway exit. 

## Runway Displaced Area

That portion of a runway between the beginning of the runway and the displaced threshold. 

## Runway-End Safety Area (Resa)

An area symmetrical about the extended runway centerline and adjacent to the end of the strip primarily intended to reduce the risk of damage to an airplane undershooting or overrunning the runway.  [ICAO Annex 14] 
 

## Runway-Holding Position

A designed position intended to protect a runway, an obstacle limitation surface, or an ILS/MLS critical/sensitive area at which taxiing aircraft and vehicles shall stop and hold, unless otherwise authorized by the aerodrome control tower.  [ICAO Annex 14] 

## Runway Intersection

Intersecting area of two or more runways. 

## Situational Awareness

The perception of elements in the environment, the comprehension of their meaning, and the projection of their status into the near future.  [Endsley, 1990]  For example, for pilots, the elements of the environment include, but are not limited to, the crew, passengers, aircraft systems, time, position, weather, traffic, and ATC constraints. 

## Seaplane Landing Area (Sla)

A defined area on water at an aerodrome prescribed for the landing and takeoff of seaplanes. 

## Seaplane Landing Lane (Sll)

A defined path on water at an aerodrome prescribed for the landing and takeoff run of seaplanes along its entire length. 

## Service Road

Part of aerodrome surface that shall be used only by service vehicles and is not considered as surface movement areas for aircraft. 

## Shoulder

An area adjacent to the edge of a pavement so prepared as to provide a transition between the pavement and the adjacent surface. 

## Spatial Resolution

The capacity of the system (lens, sensor, emulsion, electronic components, etc.) to define the smallest possible object in the image. Historically, this has been measured as the number of lines pair per millimeter that can be resolved in a photograph of a bar chart. This is the so-called Analogue Resolution.  For the modern photogrammetric cameras equipped with Forward Motion Compensation (FMC) devices and photogrammetric Panchromatic Black and White emulsions, the resolution could (depending on contrast) be 40 to 80 lp/mm (line pairs per millimeter). 

 

## Spectral Resolution

The capability of a sensor to discriminate the detected radiance in different intervals of wavelengths of the electromagnetic spectrum.  Hence, the spectral resolution is determined by the number of bands that a particular sensor is capable to capture and by the corresponding spectral bandwidth. 

## Stand

See Aircraft Stand. 

## State

A term referring to an internationally recognized geographic entity that provides Aeronautical Information Service. [ICAO Doc 7300] 

## Stopway

A defined rectangular area on the ground at the end of takeoff run available prepared as a suitable area in which an aircraft can be stopped in the case of an abandoned takeoff.  [ICAO Annex 4] 

## Surface Lighting

Lighting within a movement area. 

## Survey Control Point

A monumented survey control point. 

## Systematic Errors

Systematic errors affect all repeated observations in the same way. Systematic errors are often referred to as bias errors. These effects can be minimized via instrument calibration and/or the use of the appropriate math model.   

## Taxiway

A defined path on a land aerodrome established for the taxiing of aircraft and intended to provide a link between one part of the aerodrome and another, including: a.) Aircraft stand taxilane. A portion of an apron designed as a taxiway and intended to provide access to aircraft stands only. b.) Apron taxiway. A portion of a taxiway system located on an apron and intended to provide a through taxiway route across the apron. c.) Rapid exit taxiway. A taxiway connected to a runway at an acute angle and designed to allow landing airplanes to turn off at higher speeds than are achieved on other exit taxiways thereby minimizing runway occupancy times. 

## Taxiway Guidance Line

Guidance line painted on a taxiway. 

## Taxiway Holding Position

A designated position at which taxiing aircraft and vehicles shall stop and hold position, unless otherwise authorized by the aerodrome control tower.  

## Taxiway Intersection

A junction of two or more taxiways. 

## Taxiway Intersection Marking

Taxiway intersection marking painted across a taxiway. 

## Temporal Resolution

The periodicity through which a sensor can acquire a new image of the same spot of the earth's surface.  

## Terrain

The surface of the Earth containing naturally occurring features such as mountains, hills, ridges, valleys, bodies of water, permanent ice and snow, and excluding obstacles. Note.— In practical terms, depending on the method of data collection used, terrain represents the continuous surface that exists at the bare Earth, the top of the canopy or something in-between, also known as ―first reflective surface‖. 

 
Threshold The beginning of that portion of the runway that is available for landing.  [ICAO Annex 14] 

## Touchdown Zone (Tdz)

The portion of a runway, beyond the threshold, where it is intended landing airplanes first contact the runway.  [ICAO Annex 4] 

## Touchdown And Lift-Off (Tlof) Area

A load bearing area on which a helicopter may touchdown or lift-off. 

## Traceability

Ability to trace the history, application, or location of an entity by means of recorded identifications. (ISO 8402) [ICAO Annex 15] 

## User Of Aeronautical Data

The group or organization using the system that contains the delivered aeronautical data on an operational basis, such as the airline operator. (Note, the user may also be referred to as the ―end user‖). [DO-201A/ED-77] 

## Validation

Confirmation by examination and provision of objective evidence that the particular requirements for a specific intended use are fulfilled.  (ISO 8402) [ICAO Annex 15] 

## Verification

Confirmation by examination and provision of objective evidence that specified requirements have been fulfilled.  Objective evidence is information that can be proved true, based on facts obtained through observation, measurement, test, or other means. (ISO8402) [ICAO Annex 15] The activity whereby the value currently accorded to a data element is checked against the value originally supplied. [DO-200A/ED-76] 

## Vertical Line Structure

Line structure of a defined vertical extend that is located within an area that extends from the edge(s) of the runway(s) to 90m from the runway centerline(s) and for all other parts of the aerodrome movement area(s), 50m from the edge(s) of the defined area(s). 

## Vertical Point Structure

Point structure of a defined vertical extend that is located within an area that extends from the edge(s) of the runway(s) to 90m from the runway centerline(s) and for all other parts of the aerodrome movement area(s), 50m from the edge(s) of the defined area(s). 

## Vertical Polygonal Structure

Polygonal structure of a defined vertical extend that is located within an area that extends from the edge(s) of the runway(s) to 90m from the runway centerline(s) and for all other parts of the aerodrome movement area(s), 50m from the edge(s) of the defined area(s). 

## C Abbrevations And Acronyms

| ACARS    | Aircraft Communications Addressing and Reporting System         |
|----------|-----------------------------------------------------------------|
| ADS-B    | Automatic Dependent Surveillance - Broadcast                    |
| AIP      | Aeronautical Information Publication                            |
| AIRAC    | Aeronautical Information Regulation and Control                 |
| AIS      | Aeronautical Information Service                                |
| AIXM     | Aeronautical Information Exchange Model                         |
| ALP      | Airport Layout Plan                                             |
| ALSF-2   | High Intensity Approach Lighting with Sequenced Flashing Lights |
| AMDB     | Aerodrome Mapping Database                                      |
| ARINC    | Aeronautical Radio Incorporated                                 |
| ARP      | Aerodrome Reference Point                                       |
| A-SMGCS  | Advanced Surface Movement Guidance and Control System           |
| ASCII    | American Standard Code for Information Interchange              |
| ATC      | Air Traffic Control                                             |
| ATIS     | Automatic Terminal Information Service                          |
| BITE     | Built-in Test Equipment                                         |
| CAA      | Civil Aviation Authority                                        |
| CAD      | Computer-Aided Design                                           |
| CEP      | Circular Error Probability                                      |
| CFIT     | Controlled Flight Into Terrain                                  |
| CNG      | Change                                                          |
| CNL      | Cancel                                                          |
| CPDLC    | Controller-Pilot Data Link Communications                       |
| DEP      | Departure                                                       |
| DLA      | Delay                                                           |
| ETRF     | European Terrestrial Reference Frame                            |
| EUROCAE  | European Organization for Civil Aviation Equipment              |
| FAA      | Federal Aviation Administration                                 |
| FAR      | FAA Aviation Regulation                                         |
| FATO     | Final Approach and Takeoff areas                                |
| FHA      | Functional Hazards Assessment                                   |
| FPL      | Filed Flight Plan                                               |
| GIS      | Geographic Information System                                   |
| GNSS     | Global Navigation Satellite System                              |
| ICAO     | International Civil Aviation Organization                       |
| ILS      | Instrument Landing System                                       |
| IMC      | Instrument Meteorological Conditions                            |
| INS      | Inertial Navigation System                                      |
| JAA      | Joint Aviation Authority                                        |
| LAAS     | Local Area Augmentation System                                  |
| LAHSO    | Land and Hold Short Operations                                  |
| LEP      | Linear Error Probability                                        |
| MSL      | Mean Sea Level                                                  |
| NOTAM    | Notice to Airmen                                                |
| NA       | Not Applicable                                                  |
| NM       | Nautical mile                                                   |
| NS       | Not Specified                                                   |
| OIS      | Obstruction Identification Surface                              |
| PANS-OPS    | Procedures for Air Navigation Services - Aircraft Operations    |
|-------------|-----------------------------------------------------------------|
| PCN         | Pavement Classification Number                                  |
| PDF         | Probability Density Function                                    |
| RNP         | Required Navigation Performance                                 |
| RTCA        | RTCA, Incorporated                                              |
| SA          | Situational Awareness                                           |
| SAE         | Society of Automotive Engineers                                 |
| SARPs       | Standards and Recommended Practices (ICAO)                      |
| TCAS        | Traffic Alerting and Collision Avoidance System                 |
| TCP/IP      | Transmission Control Protocol/Internet Protocol                 |
| TIN         | Triangular Irregular Network                                    |
| TIS-B       | Traffic Information Service - Broadcast                         |
| TLOF        | Touchdown Liftoff areas                                         |
| UDDF        | Universal Data Distribution Format                              |
| VFR         | Visual Flight Rules                                             |
| VMC         | Visual Meteorological Conditions                                |
| VOR         | Very High Frequency Omni-directional Radio Range                |
| WGS84       | World Geodetic System 1984                                      |

## D Aerodrome Mapping Data Considerations D.1 Reference System Considerations

D.1.1 
Due to aerial navigation considerations and the state of the art regarding the use of the Global Positioning System (GPS) for instantaneous positioning and navigation, the Reference Frame of the AMDB shall be based on the theoretical surface and universally positioned ellipsoid, WGS-84. See Section 3. 
D.1.2 
In all those cases where an aerodrome map or database already exists and it is based on a different reference system, shall be transformed to the WGS-84 environment. See Section 3.  In this sense, the user may choose different approaches, among them the use of the *Unabridged Modelenskii Series* or the *Rigorous Solution* that is based on a seven-parameter three-dimensional transformation. This contemplates three shifts of the center of the old to the new ellipsoid, three rotations, or attitude of the old to the new ellipsoid and one scale factor relating possible local deformations of the old system. 
If the user decides to apply the *Rigorous Solution* this should contemplate the local geoid undulations during the computations of the Cartesian coordinate system. 

## D.2 Errors

Modern information theory regards the observations as signals, the statistical properties of which are classified as having deterministic and stochastic components. This philosophy regards errors as properties of observations. Nevertheless, the classical theory considers errors as being of three types, namely: Random Errors, Systematic Errors and Blunders. 

## D.3 Random Errors

When talking of observational errors or random errors of observations, we refer to the basic inherent property that estimates of a random variable x do not agree, in general, with its expectation. Thus, an observational error may in this context be defined as: 

$v_{I}=x_{I}$ - $\mu_{x}$,

_with $x_{I}$= estimate I of the random variable $x$_

$\tau$= population mean. (also for sample mean).

## D.4 Systematic Errors

The effects of systematic errors can be minimized via instrument calibration and/or the use of an appropriate mathematical model. From the statistical point of view, it should be noted that *Systematic Errors* will affect all repeated observations in the same way. So they cannot be discovered by repetition of observations. An elimination of systematic errors can only be accomplished by the use of the appropriate mathematical model. Thus, a triangle on the Earth's surface may be treated by one of the three functional models: plane, spherical, or ellipsoidal. The choice of one over the others will result in different values of systematic errors. 

## D.5 Blunders

From the statistical point of view blunders, or mistakes, are observations that cannot be considered as belonging to the same sample from the distribution in question. 

Therefore, they should not be used with other observations, and should be located and eliminated. In the advanced surveying practice statistical procedures, digital filters, etc. exist that are capable of locating and eliminating these errors. 

## D.6 Error Assessment

With regard to the treatment to be given to the above types of errors during aerodrome data acquisition for AMDB generation purposes, statistical methods should be applied in order to assess the random errors. Digital filters based on statistical principles should be designed in order to locate and eliminate blunders. The surveying sciences have developed highly effective techniques for this purpose. Statistical test based on a corresponding probability density function of the measured or derived statistic, pre-adjustment data-snooping strategies, and simultaneous adjustment with robust estimators are advised for this purpose. With regard to systematic errors, deterministic procedures should be adopted to correct the observations or they should be taken into consideration in the derived statistics. Each data acquisition method or data to be acquired has its own systematic effect or bias included in the value of the statistics themselves. To eliminate systematic errors, there are two main approaches: 

(1) use of the appropriate mathematical model that describes the systematic effect 
(e.g. Earth curvature, refraction, etc.); 
(2) use of extended functional models to account for a combination of systematic 
effects of known sources and quasi-random effects that are difficult to model. A typical case is the auto-calibration (or additional parameters) used in Photogrammetric Aero-Triangulation. 
Either approach should be followed as necessary and according to the method and statistics involved. 

## D.7 Confidence Level Of A Database

There are mainly two methods of estimation that hold four important criteria consistent, unbiased, efficient, and *sufficient*. They are the method of Maximum Likelihood and the method of Least Squares. The Maximum Likelihood method requires knowledge of the distribution from which the observations come for the purpose of parameter estimation. On the other hand, the method of Maximum Likelihood is more laborious from the computational point of view.  In the case of normal distributions, the *Method of Least Squares* will give identical results to those of the *Method of Maximum Likelihood*. With linear functions, the estimated parameters (in particular the estimated expectations) are consistent, unbiased, efficient, sufficient, and have the minimum variance property, especially when there is not systematic effects in the observations. Due to all above reasons, the method of Least Squares is recommended as the estimation method to use during all survey operations leading to an AMDB. 

The estimation of means, variance, and covariance of random variables from sample data is referred to as *point estimation*, because it results in one value for each parameter in question. By contrast, to point estimation, establishing confidence interval from sampling is referred to as *interval estimation.*  After having performed a point estimation - for instance, having estimated the coordinates of one point - the question remains: 
How good is my estimation and how much can be relied on? 

A simple answer is not possible because sampling never leads to the true theoretical distribution or its parameters. It is only possible to estimate probabilities with which the true value of the parameter in question is likely to be within a certain interval around the estimate. Such probability can be determined if we know the distribution function f(x) of the random variable. 

$$P(x_{1}<x<x_{2})=\int_{x_{1}}^{x}$$

By analogy, the probability statement for a confidence interval of the parameter s, the estimate of which is $\hat{\mathbf{s}}$ is

$$P(s_{1}<s<s_{2})=\ I\ -\.$$

(1 - $\alpha$) is called the Confidence Level, conventionally taken to be 90%, 95%, or 99%.

The values s1 and s2 are the lower and the upper confidence limits for the parameter s. 

The above equation defines the confidence interval for the parameters as the interval around the estimate ŝ, such that the probability that this interval includes the 
(unknown) true value of the parameter is (1-). The probability that the true value of the parameter does not fall in a given interval is the value 
. The width of the confidence interval decreases as the degree of freedom increases and as the level of probability associated with it decreases. Based on the above definitions we can conclude that the confidence level of a geospatial database is directly related with the lowest confidence level of existing random variables in the database. From the statistical point of view, any sort of error will affect the confidence level of the database, with a greater emphasis on the systematic and blunder errors.  Methods to use to locate and eliminate these two types of errors have been outlined above. 

## D.8 Accuracy And Precision

 Precision may be defined as the degree of conformity among a set of observations of the same random variable. The spread (or dispersion) of the probability distribution is an indication of the precision. Therefore in the figure above (2) is least precise and (3) is most precise. Accuracy may be defined as the extent to which an estimate approaches its parameter 
(in conventional terms, it is considered as the degree of closeness to the ―true‖ value). 

In the figure above, both (1) and (2) are equally accurate but neither is as precise as 
(3). By contrast, (3) is least accurate, although is the most precise. 

The main difference between precision and accuracy lies in the possible presence of bias or ―systematic error.‖ Although precision includes only random effects, accuracy comprises both random and systematic effects.  Both terms are used often with the same meaning. This is because in surveying practice, in the majority of the cases, the true value is not known and only a most probable value of the population mean can be estimated via random sample measurement procedures.  For the purpose of this paper both terms will have the same meaning and relate to the definition of precision. This concept is per se emphasized by the fact that geospatial data in the AMDB should be free of systematic effects (see above definition of accuracy). Further, all observed (random variable) or derived statistics should be qualified through its corresponding accuracy parameters such as variance, standard deviation, and covariance. A measure for accuracy proposed by Gauss is the ―mean square error‖ (MSE) given by: 
MSE = m² = E[(ŝ - E(ŝ))2], which it can be shown to reduce to: 

$$\mathrm{MSE}=\mathrm{m}^{2}=\sigma_{\mathrm{i}}^{2}+\left(\mathrm{bias}\right)^{2}$$

## D.9 Resolution

In relation with this subject, there are two possible definitions or approaches to resolution. One is according to the RTCA/ICAO philosophy whose definition is in the Glossary of this document, and the second follows surveying science concepts and particularly the field of image processing. Within this context, the following definitions are valid: SPATIAL RESOLUTION is the capacity of the system (lens, sensor, emulsion, electronic components, etc.) to define the smallest possible object in the image. Historically, this has been measured as the number of lines pair per millimeter that can be resolved in a photograph of a bar chart. This is the also called Analogue Resolution. For the modern photogrammetric cameras equipped with Forward Motion Compensation (FMC) devices and photogrammetric Panchromatic Black and White emulsions, this resolution can (depending on contrast) be 40 to 80 lp/mm (line pairs per millimeter).  In the case of space scanner sensors mounted on satellite platforms, they record the incident radiation at a series of scan lines at approximately right angles to the flight direction of the platform. Within each scan line there is a set of recorded values called the picture elements or pixels, with each pixel being the same size as the IFOV (Instantaneous Field of View). The pixel is thus the measure of the spatial resolution limit of the scanner data. SPECTRAL RESOLUTION is the capability of a sensor to discriminate the detected radiance in different intervals of wave lengths of the electromagnetic spectrum. Hence, the spectral resolution is determined by the number of bands that a particular sensor is capable to capture and by the corresponding spectral bandwidth.  In general, a sensor will be more useful with more bands and with narrow spectral bands. The photographic systems have spectral bands covering from the panchromatic Black & White (B/W), the B/W infrared, to the natural color or color infrared. The electrooptic sensors typically have larger spectral resolution. For example, Spot imagery has three bands, the NOAA-AVHRR has five, and the Landsat TM has seven. RADIOMETRIC RESOLUTION is the capability of the sensor to discriminate levels or intensity of spectral radiance. In analogue systems such as photography, the radiometric resolution is measured based on the number of gray levels that can be obtained. In opto-electronic systems, the radiance is recorded in an array of cells. A digit is assigned to each cell proportional to the received level of energy. This is done by an analogue to digital converter in the platform. Generally, in the modern sensors the range is between 0 (zero) radiance into the sensor and 255 at saturation response of the detector. TEMPORAL RESOLUTION is the rate at which a sensor can acquire a new image of the same spot of the earth's surface. This depends on the altitude of the orbit and on the aperture angle of observation. When utilizing aerial photogrammetric means to capture aerodrome data, the system resolution (i.e., combination of the optical resolution of the objective lens of the camera and resolving power of the emulsion) should be chosen based on the smallest feature that needs to be captured at the flying scale. If using satellite imagery, the selection of the bands to be used should be governed by the data elements to be captured and the size of the features to be mapped in order to derive the required spatial resolution of the imagery. 

## D.10 References For Appendix D

W. Baarda, Statistical Concepts in Geodesy. Netherlands Geodetic Commission. Publications on Geodesy. New Series, Vol. 2, No. 4, Delft, 1967. W. Baarda, Statistics. A Compass for the Land Surveyor. Netherlands Geodetic Commission. Publications on Geodesy. New Series, Vol. 2, No. 4, Delft, 1967. W. Baarda, A testing Procedure to use in Geodetic Networks. Netherlands Geodetic Commission. Publications on Geodesy. New Series, Vol. 2, No. 5, Delft, 1968. G. Konecny, Photogrammetrie. Walter de Gruyter. Berlin. 1984 K. McCoy, Resource Management Information System. Taylor and Francis, 1995. E. Mikhail, Observations and Least Squares. IEP A Dun-Donnelley Publisher, New York 1976. C. Pinillas, Elementos de Teledetección. RA-MA Editorial. Madrid. Spain, 1995. P. Wolf, Elements of Photogrammetry. McGraw-Hill, Inc. New York, USA. 1976. International Standards Organization, Central Secretariat.  ISO 19115, Geographic Information - Metadata.  Geneva, Switzerland:  ISO Central Secretariat, 2003. International Standards Organization, Central Secretariat.  ISO 19121, Geographic Information - Imagery and Gridded Data.  Geneva, Switzerland:  ISO Central Secretariat.  2003. 

## E Membership List

This document was written by a joint committee consisting of RTCA Special Committee 217 (SC- 217) and EUROCAE Working Group 44 (WG-44). 

Revision ‗B' contributors: 

| Chairs                   |                                       |
|--------------------------|---------------------------------------|
| Stephane Dubet           | Service de l'Information Aeronautique |
| Jim Terpstra             | Jeppesen                              |
|                          |                                       |
| Secretary                |                                       |
| Jens Schiefele, PhD      | Jeppesen                              |
|                          |                                       |
| Members                  |                                       |
| André Bourdais           | Airbus Industrie                      |
| Mike Burski              | FAA                                   |
| Dejan Damjanovic         | GeoEye                                |
| Britta Eilmus            | TU-Darmstadt                          |
| Brian Gilbert            | Rockwell Collins                      |
| Juliana Goh, PhD         | Boeing Commercial Airplane            |
| Allan Hart               | Honeywell                             |
| Lisa Haskell             | Jeppesen                              |
| John Kasten              | Jeppesen                              |
| Lyle Kendall             | Honeywell                             |
| Gary Livack              | FAA                                   |
| Brad Miller              | FAA                                   |
| Andre Nathaus            | TU-Darmstadt                          |
| Andreas Paul             | Lufthansa Systems FlightNav Inc.      |
| Tsvetan Penev            | TU-Darmstadt                          |
| Eduard Porosnicu         | Eurocontrol                           |
| Christian Pschierer, PhD | Jeppesen                              |
| Eric Rakotoarisoa        | Thales Aerospace                      |
| Brian Shaflik            | Boeing Commercial Airplane            |
| Ralf Sieprath            | Avitech AG                            |
| Sam Van der Stricht      | Eurocontrol                           |
| Scott Wilson             | Eurocontrol                           |

 Revision ‗A' contributors: 

| Chairs          |                                       |
|-----------------|---------------------------------------|
| Stephane Dubet  | Service de l'Information Aeronautique |
| Jim Terpstra    | Jeppesen                              |
|                 |                                       |
| Secretary       |                                       |
| Tom Evans       | NASA                                  |
|                 |                                       |
| Members         |                                       |
| Andre Bourdais  | Airbus Industrie                      |
| Stephane Dupont | ISTAR                                 |
| Christine Ellis     | Honeywell                               |
|---------------------|-----------------------------------------|
| Skip Ellis          | National Geospatial-Intelligence Agency |
| Gail Evans          | METI                                    |
| Edward Falkov, PhD  | FGUP GosNII AS                          |
| Fabien Fetzmann     | Airbus Industrie                        |
| Mike Fox            | Jeppesen                                |
| Axel Friedrich      | Lufthansa - Systems FlightNav           |
| Charisse Green      | FAA                                     |
| Duncan Howland      | Jeppesen                                |
| Scott Jerdan        | FAA NACO                                |
| John Kasten         | Jeppesen                                |
| Rob Kudlinski       | NASA                                    |
| Sergey Laletin      | FGUP GosNII AS                          |
| Marc Launer         | Jeppesen                                |
| Kevin Little        | Intermap Technologies Inc.              |
| Gary Livack         | FAA                                     |
| Sheila Mariano      | FAA                                     |
| John Moore          | FAA NACO                                |
| Randy Murphy        | Grafton Technologies                    |
| Steve Muth          | METI                                    |
| Aleksander Pavlovic | ICAO                                    |
| Jens Schiefele, PhD | Jeppesen                                |
| Ralf Sieprath       | Avitech                                 |
| Bernald Smith       | SSA and FAI                             |
| Ken Staub           | Trios Associates                        |
| Frederic Thomas     | Thales Avionics                         |
| David Toland        | METI                                    |
| Sam Van der Stricht | EUROCONTROL                             |
| Felicia Wescott     | Titan Systems                           |
| David Williams      | Evans & Sutherland                      |
| Lisa Wynn           | Jeppesen                                |
| Steve Young, PhD    | NASA                                    |

 DO-272/ED-99 contributors: 

| Chairs               |                           |
|----------------------|---------------------------|
| Philippe Caisso      | STNA                      |
| Jim Terpstra         | Jeppesen                  |
|                      |                           |
| Secretary            |                           |
| Jeff Cooper          | Allied Pilots Association |
|                      |                           |
| Members              |                           |
| Nasos Apostolopoulos | Jeppesen                  |
| Jean Baron           | DGAC/SFACT/N/ST/A         |
| Ron Birk             | Intermap Technologies     |
| Nigel Blackwell      | BAE Systems               |
| Del Croom            | NASA                      |
| Dejan Damjanovic     | Jeppesen                  |
| Milen Denchev        | EUROCONTROL               |

Stephane Dubet Service de l'Information David M. Dudish FAA NACO 
William E. Fowler III 
Delta Air Lines Michael Fox Jeppesen Silvia Freeman National Imagery & Mapping Agency Axel Friedrich Darmstadt University of Technology Tony Henley BAE Systems Avionics Jack Izatt BAE Systems Scott Jerdan FAA NACO 
Walter Johnson Rockwell Collins Flight Dynamics Brad Kearse NOS / NGS 
Randy Kenagy AOPA 
Rob Kudlinski NASA 
Norman LeFevre FAA 
Gerard Lepere Thomson-CSF Sextant Mike Lissone Stasys Limited Gary Livack FAA 
Bill Lugsch Jeppesen Kevin McKinney Evans & Sutherland Hugues Meunier Thomson-CSF Sextant Florence Munoz EADS 
Chris Parrish NOS / NGS 
Ricardo Passini, PhD 
BAE Systems/ADR Marconi Aleksandar Pavlovic ICAO 
Ken Reid EUROCONTROL 
Pedro Rivas ALPA 
Rudy Ruana RTCA 
Jens Schiefele, PhD 
Darmstadt University of Technology Ed Schuster Jeppesen Richard Simon FAA 
Donald W. Smith National Imagery & Mapping Agency Bernald S. Smith Soaring Society of America Bruce V. Smith, PhD 
Rockwell Collins Christine Stahl Honeywell Chris Stassen BAE Systems Canada Ken Staub Trios Associates Peter Stephenson EUROCONTROL 
Ron Strathmann FAA NACO 
John Synnott IATA 
Harro Von Viebahn Diehl Avionik Systeme Mike Warren Rockwell Collins Flight Dynamics John Wilde Stasys Limited Blake Wilson Honeywell Steve Young NASA 
Steve Zellers Rockwell Collins 

 
                                  This Page Intentionally Left Blank 
                                                      

