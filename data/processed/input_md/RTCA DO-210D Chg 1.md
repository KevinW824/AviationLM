RTCA, Inc. 

1140 Connecticut Avenue, NW, Suite 1020 
Washington, DC 20036-4008 USA 
 
CHANGE NO. 1 
 
-TO- 
 
RTCA/DO-210D 
 
Minimum Operational Performance Standards for Geosynchronous Orbit Aeronautical Mobile Satellite Services (AMSS) Avionics © RTCA, Inc.  2000 December 14, 2000 
Copies of this document may be obtained from RTCA, Inc. 

1140 Connecticut Avenue, NW, Suite 1020 
Washington, DC  20036-4008 USA 
 
Telephone:  202-833-9339 
Facsimile:  202-833-9434 
Internet:  www.rtca.org Please contact RTCA for price and ordering information. 


DO-210D Change No. 1 
1. 
Page 5, Section 1.2.3.  In the 1st paragraph of text, last sentence, delete the two instances of the word "shall". 
2. 
Page 18.  Add a new Section 2.1.9 and Figure 2-00 as follows: 
2.1.9 
 
Interference Susceptibility 
 
Receivers meeting the requirements of this document operate satisfactorily in the presence of interference at RF levels at the receiver's input port not exceeding the following tabulated levels. The RF levels in the frequency ranges near the SATCOM receive band are also illustrated in 
Figure 2-00. 
 
 
Frequency Range 
 
Maximum Interference Level 
 
 
470 to 1450 MHz 
 
+3 dBm 
 
 
1450 to 1529 MHz 
 
Decreases linearly in decibels 


from +3 dBm at 1450 MHz to –72 dBm at 1529 MHz 
 
 
1529 to 1560 MHz 
 
-163.2 dBm 
 
 
1560 to 1626.5 MHz 
 
Increases linearly in decibels 


from –72 dBm at 1560 MHz 


to +3 dBm at 1626.5 MHz 


1626.5 to 1660.5 MHz 
 
+47.8 dBm 
 
 
1660.5 to 18000 MHz 
 
+3dBm 

 
FIGURE 2-00.   RECEIVER SUSCEPTIBILITY 
 
 
3. 
Page 21, Section 2.2.3.2.1.  Delete the 3rd paragraph of text and insert the following: 
The coverage volume, as declared by the antenna manufacturer, shall comprise not less than 75 percent of the solid angle of the upper hemisphere above five degrees elevation (to the horizon during normal cruise attitude of the aircraft).  This gain value shall include all (1) effects of installation on a surface representative of the mounting surface on which it is intended to operate the antenna, (2) beam-pointing errors within the antenna subsystem including those due to 
implementation of the beam-steering algorithm, and 
 (3) effects of a radome and/or other 
protective surfaces. 


This gain value shall be met while meeting the pattern discrimination requirements in Section 2.2.3.4.1. 
4. 
Page 21, Section 2.2.3.2.2.  Delete the 2nd paragraph and insert the following: 
The coverage volume as declared by the antenna manufacturer shall comprise not less than 85 percent of the solid angle of the upper hemisphere above five degrees elevation.  This gain value shall include all (1) effects of installation on a surface representative of the mounting surface on which it is intended to operate the antenna, and (2) effects of a radome and/or other protective surfaces.  The coverage volume may include a volume corresponding to a cone of 20 degrees half-angle at the aircraft zenith (when in normal cruise attitude) in straight and level flight.  The gain within this cone must not be less than -2 dBic. 
The remaining 15 percent shall be not less than -5 dBic. 
5. 
Page 22, Section 2.2.3.2.3.  Delete the 4th and 5th paragraphs and insert the following: 
 
The coverage volume, as declared by the antenna manufacturer, shall comprise not less than 85 percent of the solid angle of the upper hemisphere above 5 degrees elevation (relative to the horizon during normal cruise attitude of the aircraft).  This gain value shall include all (1) effects of installation on a surface representative of the mounting surface on which it is intended to operate the antenna, (2) beam-pointing errors within the antenna subsystem including those due to implementation of the beam-steering algorithm, and (3) effects of a radome and/or other protective surfaces. The coverage volume may include a volume corresponding to a cone of 20 degrees half-angle at the aircraft zenith in straight and level flight.  The gain within this cone must be not less than 4 dBic. 
6. 
Page 23, Section 2.2.3.4.2.  Delete paragraphs 2.2.3.4.2.1 and 2.2.3.4.2.2 in their entirety and insert the following: 
 
The discrimination requirements in this section shall be independent of the antenna manufacturer's declared coverage volume (as defined in Section 2.2.3.2.3). The radiation pattern shall discriminate by not less than 7 dB between wanted and 85% of 
unwanted satellite positions for all antenna steering angles above 5 degrees elevation.  In addition, the transmit radiation pattern shall be such that the gain in any direction shall not exceed that in the direction of the wanted satellite by more than 5 dB over 95% of the antenna steering angles above 5 degrees elevation. These requirements assume that (1) satellites are in geostationary orbits, (2) unwanted satellites are not less than 80 degrees longitude away from the wanted satellite, and (3) the aircraft is in straight and level flight. 

7. 
Page 29, Section 2.2.4.1.7.1.  Delete the existing one sentence of text and insert the following: 
 
The receiver shall tune within the frequency range 1530-1559 MHz in 2.5 kHz increments. 
NOTE: The channel center frequencies near the allocated band boundaries are restricted to 
contain the sideband energy within the allocated bands.  The center frequencies of high data rate channels are spaced farther from band boundaries than low data rate channels. The ranges of the transmit channel center frequencies for some channel rates are given in the following table. Channel Modulation 
 
Carrier Tuning Ranges (MHz) 
   Rate    
     Type      
 
(Tuning Increment = 2.5 kHz) 
 
0.60 kbps 
A-BPSK 
 
1530.0025 to 1558.9975 
1.20 kbps 
A-BPSK 
 
1530.0025 to 1558.9975 
8.4 kbps 
A-QPSK 
 
1530.0050 to 1558.9950 
10.5 kbps 
A-QPSK 
 
1530.0075 to 1558.9925 
21.0 kbps 
A-QPSK 
 
1530.0125 to 1558.9875 
 
NOTE: While the lower edge of the assigned frequency band in the space-to-earth (AES 
receive) direction is 1525 MHz, the lower edge frequency of the operational band is limited to 1530 MHz.  See Section 2.2.4.2.10.1, Note 2. 
8. 
Page 29, Section 2.2.4.1.7.2.  The equation dividing line should be centered (moved to the right). 
9. 
Page 30, Section 2.2.4.1.11.1.  In the 1st line, the hyphen in "P-channel" should not be underlined. 
10. 
Page 32, Section 2.2.4.1.12.1.1.  In the table, there are two misalignments of text in the third row of the column headers:  "Present" should be aligned under "Rician Fading", and "(Hz)" should be aligned under "Fading Bandwidth". 
11. 
Page 33, Section 2.2.4.2.1.  In the table, there is a misalignment of "47.6 ppm" in the 10.5 kbps row - it should be aligned under the "Channel Rate Tolerances" column. 
12. 
Page 35, Section 2.2.4.2.5.  Delete the table and Table Notes in the entirety and insert the following. (The Notes beginning at the bottom of the page, following the Table Notes, are to be retained.) 
 
Composite Harmonic, Discrete Spurious and Noise Density Levels 
 
Frequency (MHz) 
 
Power Density 
0.01 to 15251 
-135 dBc/4 kHz 
1525 to 1559 
-203 dBc/ 4kHz 
1559 to 1585 
-155 dBc/MHz 
1585 to 1605 
-143 dBc/MHz 
1605 to 1610 
-117 dBc/MHz 
1610 to 1610.6 
  -95 dBc/MHz 
1610.6 to 1613.8 
  -80 dBW/MHz5,7 
1613.8 to 1614 
  -95 dBc/MHz 
1614 to 1626.5 
  -70 dBc/4 kHz 
1626.5 to 1660 
  -70 dBc/4 kHz2,3,4,5,6 
1660 to 1660.5 
-49.5 dBW/20 kHz2,3,4,5,6,7 
1660.5 to 1670 
-49.5 dBW/20 kHz4,5,7 
1670 to 1735 
  -60 dBc/4 kHz 
1735 to 12000 
-105 dBc/4 kHz 
12000 to 18000 
  -70 dBc/4 kHz 
 
TABLE NOTES: 1. AMSS operations are permitted in the MMS (maritime) band which has been extended to 
include 1525-1530 MHz. 
 
2. Within the transmit band, excluding the frequency band within ±35 kHz of the carrier. 
 
3. The –55 dBc/4kHz spectrum level in this table is equivalent to –55 - 10 log10(4000/SR) dBe 
(relative to the maximum envelope) under the definitions in Section 2.2.4.2.16. 4. For wide band spurious the limit is –39.5 dBW/MHz. 
5. This level is not applicable for intermodulation products. 6. The upper limit for the excess power for any narrow-band spurious emission (excluding 
intermodulation products) within a 30 kHz measurement bandwidth shall be 10 dB above the power limit in this table. 7. Note that the power density is expressed in terms of absolute power (dBW) in some 
instances, and in terms relative to carrier power (dBc) in other instances. 
 
 
13. 
Page 36, Section 2.2.4.2.6, table of "Maximum Intermodulation Product Levels".  Delete the table contents in their entirety, and replace with the following: 
 
 
Frequency (MHz) 
 
 IM Level 
 
Below 1610  
<-70  dBc 
 
1610 to 1614 
-64  dBc 
 
1614 to 1671.25 
-24  dBc 
 
1671.25 to 1711 
-29  dBc 
 
1711 to 1735 
-34  dBc 
 
1735 to 18000 
<-70  dBc 
14. 
Page 36, Section 2.2.4.2.6 (at bottom of the page).  Delete the sentence beginning with "The transceiver shall not transmit on a newly-assigned frequency..." in its entirety,  and replace with: 
 
In multi-channel operation, the spacing between RF carriers that are operating simultaneously shall not exceed 10.75 MHz. 
15. 
Page 37, in Section 2.2.4.2.6 (at top of the page), immediately following "*NOTES:*".  Add the following note: 
 
 
0. The immediately preceding requirement ensures that neither 3rd nor 5th order 
intermodulation products can occur below 1610 MHz. 
16. 
Page 37, Section 2.2.4.2.8, 1st paragraph of text.  The 2nd line of text has an unwanted hanging indent. 
17. 
Page 37, Section 2.2.4.2.8, 1st paragraph of text.  At end of the second line of text following the words "under the stated conditions" and before the colon, insert the phrase "(see also Section 2.2.2)". 
18. 
Page 38, in Section 2.2.4.2.10.1.  In the Note (second block of text), add "1" following the word "*NOTE*", so as to read "*NOTE 1:*". 
19. 
Page 39, in Section 2.2.4.2.10.1.  Delete the existing table in its entirety and insert the following: 
 
Channel  
Modulation 
 
Carrier Tuning Ranges (MHz) 
   Rate    
 
     Type      
 
(Tuning Increment = 2.5 kHz) 0.60 kbps 
 
A-BPSK 
 
1631.5075 to 1660.4925 
1.20 kbps 
 
A-BPSK 
 
1631.5075 to 1660.4925 
8.4   kbps 
 
A-QPSK 
 
1631.5100 to 1660.4900 
10.5 kbps 
 
A-QPSK 
 
1631.5125 to 1660.4875 
21.0 kbps 
 
A-QPSK 
 
1631.5175 to 1660.4825 

20. 
Page 39, in Section 2.2.4.2.10.1.  In the Note following the table, add "2" following the word "*NOTE:*", so as to read "*NOTE 2:*". 
21. 
Page 39, in Section 2.2.4.2.10.1.  Following "*NOTE 2:*" and its text as changed above, add the following: 
 
NOTE 3: While the lower edge of the assigned frequency band in the earth-to-space (AES 
transmit) direction is 1626.5 MHz, the lower edge frequency of the operational band is limited to 1631.5 MHz due to frequency management constraints necessary for protection of other services (e.g., GNSS).  This limit corresponds with the paired space-to-earth (AES receive) lower band edge frequency of 1530 MHz (see Section 2.2.4.1.7).  Consequently, performance requirements and their verification are limited to the operational frequencies contained in the above table. 
22. 
Page 39, Section 2.2.4.2.10.2.  The equation dividing line should be centered (moved to the right). 
23. 
Page 44, Section 2.2.6.  In the first list for Reference Document "A", for the last entry "Figure 46" the version number "1.45" should be aligned to the 3rd column. 
24. 
Page 54, Section 2.2.7.4.2.  Under the Reference Document "A", Appendix 3 list, in the row for "3.4", remove the underline from the hyphen in "T-Channel". 
25. 
Page 61, in Section 2.2.7.5.2.1.  Following the existing two Notes, insert the following new Note: 
 
 
3. 
Receipt of a request for any optional facility not specified above and not implemented shall result in the connection being cleared, indicating diagnostic code 65 (facility code not allowed). 
26. 
Page 61, Section 2.2.7.5.2.3, 2nd paragraph.  In the 1st sentence, delete the words "facility registration protocols (if used)". 
27. 
Page 65, Table 2-4.  In the 1st column, 3rd row (including header) starting with "Any packet, except...", 
delete the words ", REGISTRATION (if supported)". 
28. 
Page 65, Table 2-4.  In the 1st column, 5th row (including header) starting with "RESTART REQUEST, 
RESTART CONFIRMATION...", delete entire entry and replace with the following: 
 
RESTART REQUEST or RESTART CONFIRMATION Packet with a Logical Channel identifier not = 0. 
 
29. 
Page 65, Table 2-4.  In the 3rd ("r2") column, 7th row (including header) starting with "Packets 
having a Packet Type Identifier shorter than...",  following the existing entries, add "(See Note 3)". 
30. 
Page 65, Table 2-4.  In the 4th ("r3") column, 10th row (including header) starting with "RESTART 
REQUEST OR RESTART CONFIRMATION Packet... ",  following the existing entries, add "(See Note 3)". 
31. 
Page 65, Table 2-4.  In the 1st column, 10th row (including header; last row on the page), change "OR" to 
"or" (lower case). 
32. 
Page 66, Table 2-4 (continued).  Delete the 2
nd and 3
rd rows, both starting with "REGISTRATION 
REQUEST Packets...". 
33. 
Page 66, Table 2-4 (continued).  In the 3rd ("r2") column of the last row (identified in the left column as 
"Call Setup, Call Clearing, DATA..."), following the existing entries, add "(See Note 3)". 
34. 
Page 66, in the Notes.  Delete the text of Note 1 in its entirety, and replace with the following: 
 
NOTES: 
1. 
The AES Subnetwork has no restart states.  Receipt of a RESTART REQUEST causes the DCE to respond with a RESTART CONFIRMATION.  The RESTART REQUEST packet is forwarded to the SSNIW, which responds by executing a connection release procedure for each VC associated with the DTE/DCE interface (reference Figure 2-2). This is the equivalent of the originating DTE separately issuing a CLEAR REQUEST for each VC; i.e., the equivalent of a RESTART REQUEST. 
35. 
Page 66, in the Notes.  Delete the text of Note 2 in its entirety, and replace with "(Reserved)". 
36. 
Page 66, in the Notes.  Delete the text of Note 5 in its entirety, and replace with the following: 
 
 
5. 
The DCE, upon entering the r3 state, checks for the completion of r2 processing.  If the 
r3 state is entered via the r2 state, the DCE discards the received packet and indicates a restart by transmitting to the DTE a RESTART INDICATION, with the cause "Local procedure error" and the appropriate diagnostic code.  If the r3 state is not entered via the r2 state, the DCE performs all of the actions normally performed when entering r2 and issues a RESTART INDICATION to the DTE, and sends a RESTART REQUEST to the SSNIW. 
37. 
Page 67, Table 2-5.  In the 1st column, 4th row  (starting with "RESTART REQUEST OR RESTART 
CONFIRMATION Packet...") delete the existing entry in its entirety and replace with: RESTART REQUEST or RESTART CONFIRMATION Packet with Logical Channel Identifier not = 0. 
38. 
Page 69, Table 2-6.  In 1st column, 4th row, delete the existing entry in its entirety and replace with: 
 
RESTART REQUEST or RESTART CONFIRMATION Packet with Logical Channel Identifier not = 0. 
39. 
Page 69, Table 2-6.  Delete the last row (starting with "REJECT...") in its entirety. 
 
 
40. 
Pages 71-72, Table 2-8.  Make the following changes to the lower ("g1" & "g2") half of Table 2-8 and its notes: 
 
a. In the "DCE FLOW CONTROL TRANSFER STATES" header column, delete "(See Notes 1, 3 
and 4)" in its entirety and replace with: 
 
 
(See Notes 1, 2 and 3) 
 
b. In the 2nd row,  delete the entry "RR, RNR, or REJECT..." in its entirety and replace with: 
 
 
RR or RNR packet with an invalid PR 
 
c. Delete the entire 5th row (beginning with "REJECT packet with a valid PR (optional)"). 
41. 
Page 72, in the Notes to Table 2-8, make the following changes: 
 
a. In Note 1.  Delete the comma following "RR"; insert the word "and"; and delete the subsequent 
words "*, and REJECT*". b. In Note 5.  Delete the word "octal" and replace with "octet". 
c. In Note 6, 5th line.  After the opening parenthesis, delete the symbol "#" that immediately 
precedes the number "0". 
 
d. In Note 7, 1st line.  Delete the comma following "RR"; insert the word "or"; and delete the 
subsequent words "*or REJECT*". e. In Note 7, last line.  Change "*Note 5*" to read "*Note 4*". 
42. 
Page 78, in Section 2.2.8.1.  At the end of the 2nd paragraph, in the parenthetical reference, delete 
"2.2.4.2.8" and replace with "2.2.2". 
 
43. 
Page 117, in Section 2.4.4.1.  Delete Item i. in its entirety, and replace with the following: 
 
i. 
Test Frequencies - Unless otherwise specified, the following tests shall be conducted at the following frequencies: 
 
Test Frequency  
 
    Receive    
 
   Transmit 
 
Lower Band-Edge 
 
1530.5  MHz 
 
1632.0  MHz 
 
 
Mid-Band 
 
 
1544.5  MHz 
 
1646.0  MHz 
 
 
Upper Band-Edge 
 
1558.5  MHz 
 
1660.0  MHz 
44. 
Page 142, in Section 2.4.4.3.6.  Delete Steps 4 through 8 in their entirety, and replace with the following: 
 
Step 4. 
Turn on the first channel unit again so that both units are operating.  This establishes an operating condition with two active transmit carriers operating at maximum output power, each 3 dB below the maximum single carrier output power.  Use the spectrum analyzer to measure the intermodulation products resulting from the two signals with the measured single carrier power level as a reference. Step 5. 
Repeat Steps 1 through 4 for reduced commanded output levels in 5 dB steps to 15 dB below maximum allowable output. Step 6. 
Repeat Steps 1 through 5 for channel frequency separations of 100 kHz and 10 kHz and 
at the other transmit test frequencies specified in Section 2.4.4.1, Item i., at all three 
frequency separations. Step 7. 
Repeat Steps 1 through 5 with one carrier tuned to 1660.4 MHz and the other carrier tuned to the lowest frequency that can be transmitted within the constraint of Section 2.2.4.2.6 for simultaneously operating RF carriers. Step 8. 
Repeat Steps 1 through 4 with a carrier spacing that would exceed the spacing between simultaneously operating RF carriers defined in Section 2.2.4.2.6.  Verify that the 
transceiver meets the requirement. 
45. 
Page 168, in the Section 2.4.6.3 header.  Delete the parenthetical reference "(Section 2.2.6)" and replace with "(Section 2.2.6-A-5.6.2)". 
46. 
Page 196.  Immediately preceding Section 2.4.7.3.4, add a new Section 2.4.7.3.3.6 as follows: 
 
2.4.7.3.3.6 
Response to Requests for Non-Supported Facilities 
 
 
This test verifies the transceiver's ability to clear a call request containing an ISO 8208 optional facility that is not supported by the transceiver. 
Step 1 - Call Request from the Test Set 
 
 
Program the test set to send a CALL REQUEST Packet to the transceiver with the Facility Code field encoded for a facility code that is not supported by the transceiver, with the Facility Parameter field encoded as appropriate for the selected facility. 
Step 2 - Virtual Call cleared by transceiver 
 
 
Use the test set to verify that the transceiver clears the Virtual Call by sending a CLEAR CONFIRMATION Packet with a diagnostic code 65 (facility code not allowed). 
47. 
Page 200, Section 2.4.7.4.  In the header and in the 1st sentence of text, delete "Section 2.2.7.5.3" and 
replace with "Section 2.2.7.6". 
48. 
Page 200, Section 2.4.8.  Under "Measurement Procedure", in the 3rd paragraph of text, 2nd line, delete 
'Document "B", V1.20' and replace with: 
 
Document "D" Annex 1 Section 10. 
49. 
Page 201, in Section 2.4.8.  In the list of references under "Reference Document "D" Annex 1 Section 6", add "1.22" (under the "Version" column) in the row "6.3.2.2  CM111 Test Cases". 
50. 
Page 202, in Section 2.4.8.  Immediately before the entry for "10.1", delete the row starting with "6.3.2.2".  (This row is a duplicate and out-of-sequence instance of the entry referencing 6.3.2.2.) 
51. 
Page 202, in Section 2.4.8.  In the list of references under "Reference Document "D" Annex 1 Section 6", segregate the nine line entries beginning with "10.1" through "10.3.2.1", and precede them with their own underlined sub-title "
Reference Document "D" Annex 1 Section 10:".  (Use vertical leading 
consistent with that done elsewhere for such reference lists in this section.) 
52. 
Page 202, in Section 2.4.8.  In the listing subtitled "Reference Document "D" Annex 2 Section 5", underline the sub-title, and change "Annex 2" to "Annex 3". 
53. 
Page 203, in Section 2.4.8.  In the caption for Table 2-20, delete the parenthetical phrase, "(9.6 kbps Vocoder)". 
54. 
Page 214, in Section 3.4.5.  Delete the underlines from the hyphens in line 3.3  "Log-On" and line 3.4  "P- Channel". 
 
 
55. 
Page 219, in the membership list.  Correct the misalignments in the two instances of "CTA, Inc." (for T. Dehel). 
56. 
Appendix C (indicated pages).  Make the following changes: 
 
a. Page 1.  For the "PERFORMANCE" column reference to "2.2.1", delete the "VERIFICATION" 
column references and replace with "2.4.5, 2.4.7.3.3.5, 2.4.8.1". 
 
b. Page 1.  For the "PERFORMANCE" column reference to "2.2.2", change the "VERIFICATION" 
reference from "2.4.8.1" to "2.4.4.3.8". 
 
c. Page 1.  For the "PERFORMANCE" column reference to "2.2.2.1", delete "2.4.8.1" from the 
"VERIFICATION" column. 
 
d. Page 3.  For the "PERFORMANCE" column reference to "2.2.4.2.4", add "2.4.4.3.4" in the 
"VERIFICATION" column. 
 
e. Page 3.  For the "PERFORMANCE" column reference to "2.4.4.3.4", delete the entire row. 
 
f. 
Page 5.  For the "PERFORMANCE" column reference to "2.2.6-A-5.6.2", add "2.4.6.3" as an additional "VERIFICATION" reference. 
 
g. Page 9. For the "PERFORMANCE" column reference to "2.2.7.5.2.1", add "Tested throughout 2.4.7, 
including 2.4.7.3.2.1, 2.4.7.3.2.2, 2.4.7.3.3.1, 2.4.7.3.3.2, 2.4.7.3.3.3, 2.4.7.3.3.4" in the "VERIFICATION" column. 
 
h. Page 10.  For the "PERFORMANCE" column, delete the entry "2.2.7.5.3" and replace with "2.2.7.6". 
 
i. 
Page 11.  For the "PERFORMANCE" column reference to "2.2.8.1", add "2.4.8.1" in the "VERIFICATION" column. 
57. 
At end of the DO-210D document, insert a new Appendix D, as attached hereto. 58. 
At end of the DO-210D document, insert a new Appendix E, as attached hereto. 
 
 
A P P E N D I X  D 
Recommendations for Non-Safety SATCOM Systems This Page Intentionally Left Blank Recommendations for Non-Safety SATCOM Systems 
 
This appendix provides guidance on the applicability of the MOPS requirements to AMSS avionics equipment that do not provide AMS(R)S (safety services). This is intended to include all avionics equipment that provide only non-safety AMSS services, whether via satellite systems otherwise in compliance with these MOPS or not.  Even though such avionics equipment might not utilize the RF or electrical signal characteristics and functionality required by these MOPS, the necessity of protecting other CNS systems on-board the same aircraft and within the same airspace, as well as the possible provision of AMS(R)S by terminals operating within the same satellite subnetwork, make it desirable that all non-safety-only AMSS equipment be held to a subset of the minimum standards established for AMS(R)S. Table D-1 specifies which sections of the MOPS should apply to non-safety-only AMSS avionics equipment. Sections are not listed beyond the fifth level of numbering (lower-level sections have been deleted for brevity).  In cases where a higher-level requirement applies to non-safety AMSS, it is to be understood that all lower-level unlisted requirements also apply to non-safety AMSS; conversely, where a higher-level requirement does not apply to non-safety AMSS, then it is to be understood that no lower-level unlisted requirements apply.  In cases where some lower-level requirements apply to non-safety AMSS and some do not, those which do apply are explicitly listed, and those which do not apply are omitted for brevity. Manufacturers of non-safety AMSS equipment are urged to consider all of the antenna (Section 2.2.3), receiver (Section 2.2.4.1) and transmitter (Section 2.2.4.2) requirements as guidance in their design. 

PROVIDE NO SAFETY SERVICES MOPS Section 

 MOPS Section Title 
Apply 
to 
Non-Safety AMSS Comments 
1.0 
PURPOSE AND SCOPE  
N/A 
Section 1 contains no requirements 
N/A 
Sections containing no requirements are listed as not applicable ("N/A") 
2.0 
EQUIPMENT PERFORMANCE REQUIREMENTS AND TEST PROCEDURES 
2.1 
General Requirements 
N/A 
 
2.1.1 
Airworthiness 
YES 
 
2.1.2 
Intended Function 
YES 
 
2.1.3 
Federal Communications Commissions Rules 
YES 
 
2.1.4 
Fire Protection 
YES 
 
2.1.5 
Operation of Controls 
YES 
 
2.1.6 
Accessibility of Controls 
YES 
 
2.1.7 
Effects of Tests 
YES 
 
2.2 
Equipment Performance Requirements - Standard Conditions 
N/A 
 
2.2.3 
Antenna Subsystem Requirements 
N/A 
 
2.2.3.1 
General 
N/A 
 
2.2.3.13 
Radiated Antenna Intermodulation Products 
YES 
 
2.2.4 
Satellite Subnetwork Physical Layer Requirements 
N/A MOPS Section MOPS Section Title 
Apply 
to 
Non-Safety AMSS Comments 
2.2.4.2 
Transmitter Requirements 
N/A 
 
2.2.4.2.5 
Harmonics, Discrete Spurious and Noise Density 
YES 
 
2.2.4.2.6 
Intermodulation Products 
YES 
 
2.2.4.2.7 
Carrier Off Level 
YES 
 
2.3 
Equipment Performance - Environmental Conditions 
YES 
The sections marked "YES" above that appear in Table 2-15 should meet DO- 160C 
requirements 
to 
ensure 
that 
interference to safety services do not occur under the specified environmental conditions. 
2.3.1 
General Requirements 
YES 
 
2.3.2 
Equipment Configurations 
YES 
 
2.3.3 
Configuration Control 
YES 
 
2.3.4 
Specific Environmental Test Conditions 
YES 
 
2.4 
Equipment Performance Verification Procedures 
PARTIAL 
Reference Appendix C for the sections marked "YES" above for applicable subsections of Section 2.4. 
3.0 
INSTALLED EQUIPMENT PERFORMANCE 
N/A 
 
3.1 
Equipment Installation 
N/A 
 
3.1.2 
Aircraft Environment 
YES 
 
3.1.5 
Failure Protection 
YES 
 
3.1.6 
Interface Interference Effects 
YES 
 
3.1.7 
Aircraft Power Source 
YES 
 
3.2 
Installed Equipment Performance Requirements 
YES 
For the Radiated Antenna Intermodulation Products 
in 
AMS(R)S 
Bands, 
the 
requirements should apply with the AMSS-only equipment as the source and the AMS(R)S system as the victim.  The 
complementary requirement need not apply. 
3.3 
Conditions of Test 
YES 
 
3.3.1 
Power Input 
YES 
 
3.3.2 
Environment 
YES 
 
3.3.3 
Adjustment of Equipment 
YES 
 
3.3.4 
Warm-up Period 
YES 
 
3.4 
Test Procedures for Installed Equipment Performance 
YES 
 
3.4.1 
Conformity Inspection 
YES 
 
3.4.2 
Interference Tests 
YES 

 
A P P E N D I X  E 
Diplexer Historical Development and Performance Characteristics This Page Intentionally Left Blank Diplexer Historical Development and Performance Characteristics The transmitter Harmonics, Spurious, and Noise (HSN) and the Intermodulation (IM) Product requirements in Section 2.2.4.2.5 and Section 2.2.4.2.6 of this MOPS are predicated on performance characteristics of the transmit filter in the diplexer that is used in the ARINC Characteristic 741 AES system configuration and the HSN and IM levels allowed to be generated in the signal generation and amplification processes. Since the first versions of DO-210 and ARINC Characteristic 741, several different diplexer specifications have been developed.  There are currently four versions of diplexer filter specifications which were pertinent to the deliberations of SC-165 WG-1 and the AEEC Air/Ground Communications Systems (AGCS) Subcommittee.  These are known as "Type A", "Modified Type A", "Type B" and "Type C" (previously called by the nickname "Jane"). These different diplexer designs were developed to meet changing requirements to protect services outside the Inmarsat SATCOM transmit band, 1626.5 to 1660.5 MHz.  The services to be protected have included GPS, GLONASS, Radio Astronomy, and Iridium. The original diplexer design was the Type A model and it offered sufficient protection only to GPS.  The Modified Type A diplexer design was developed to give more protection to GLONASS as well as protecting GPS. At about the same time that the Modified Type A diplexer specification was being developed, there was concern about protection for the TFTS system.  TFTS operates in the spectrum above the SATCOM transmit band.  The "Type B" diplexer design specification was developed for ARINC Characteristic 741 to offer protection to GPS, GLONASS and TFTS.  The "Type B" diplexer specifications were not involved in derivation of the specifications in the MOPS. The "Type C" diplexer specification was developed to provide additional protection for AMS(R)S services operating in the 1610 MHz to 1626.5 MHz bands.  It does not address TFTS.  In particular it was developed to provide an additional 10 dB of protection for the Iridium system at 1624.5 MHz.  Along with the "Type C" diplexer design, a pre-HPA filter was designed to further reduce the broadband noise and spurious signals in the Iridium frequency band generated prior to the HPA in the AES system. The Type A and modified Type A diplexers are currently available.  The Type A diplexer is by far the more prevalent in aircraft installations.  The "Type B" diplexer, the pre-HPA filter, and the "Type C" diplexer have not been commercially developed or qualified.  It is expected that these devices will not be qualified until after the ongoing deliberations within the ITU and ETSI have been completed. The "Type C" diplexer can be used in conjunction with the pre-HPA filter to provide additional HSN outof-band filtering.  The pre-HPA filter does not provide significant additional attenuation of any intermodulation products because those products primarily originate in the HPA which follows the pre- HPA filter in the system configuration. The development of characteristics of the "Type C" diplexer took due account of ITU Study Group 8 activity post WRC2000.  The applicability of this diplexer, and whether it is needed to adequately protect all NGSS systems below 1626.5 MHz, is currently unknown. The following Type A and Modified Type A diplexer characteristics are taken from ARINC Characteristic 741 Part 1 Supplement 10, Section 2.2.4.3.  The HSN and IM characteristics of the other AES 

transceiver system components (i.e., SDU/RFU), as taken from ARINC Characteristic 741 Part 1, follow the diplexer characteristics tables. 
Type A Diplexer - For Protection of GPS Only 
 
Transmit Port-to-Antenna Port The path from the transmit port to the antenna port should have the following characteristics: 
 
Frequency (MHz) 
 
Rejection 
 
      0.0 to 1525.0 
 
>   80  dB 
 
1525.0 to 1559.0 
 
> 120  dB 
 
1559.0 to 1565.0 
 
>   80  dB 
 
1565.0 to 1585.0 
 
> 100  dB 
 
1585.0 to 1605.0 
 
>   50  dB 
 
1605.0 to 1610.0 
 
>   30  dB 
 
1610.0 to 1626.5 
 
Decreases 
 
1626.5 to 1660.5 
 
Insertion loss < 0.8  dB 
 
1660.5 to 1735.0 
 
Increases 
 
1735.0 to 12000 .0 
 
>   50  dB 
 
12000.0 to 18000.0 
 
>   15  dB 
 
Modified Type A Diplexer - For Protection of GPS and GLONASS Transmit Port-to-Antenna Port 
The path from the transmit port to the antenna port should have the following characteristics: 
 
Frequency (MHz) 
 
Rejection 
 
      0.0 to 1525.0 
 
>   80  dB 
 
1525.0 to 1559.0 
 
> 120  dB 
 
1559.0 to 1585.0 
 
> 100  dB 
 
1585.0 to 1605.0 
 
>   88  dB 
 
1605.0 to 1610.0 
 
>   62  dB 
 
1610.0 to 1614.0 
 
>   40  dB 
 
1614.0 to 1626.5 
 
Decreases 
 
1626.5 to 1631.5 
 
Insertion loss < 2.3  dB 
 
1631.5 to 1660.5 
 
Insertion loss < 0.8  dB 
 
1660.5 to 1735.0 
 
Increases 
 
1735.0 to 12000 .0 
 
>   50  dB 
 
12000.0 to 18000.0 
 
>   15  dB 
Type "Type C" Diplexer - For Protection of GNSS and Iridium 
 
Transmit Port-to-Antenna Port 
Frequency (MHz) 
 
Rejection 
 
      0.0 to 1525.0 
 
>   80  dB 
 
1525.0 to 1559.0 
 
> 120  dB 
 
1559.0 to 1585.0 
 
> 100  dB 
 
1585.0 to 1610.0 
 
>   88  dB 
 
1610.0 to 1614.0 
 
>   70  dB 
 
1614.0 to 1624.5 
 
>   10  dB 
 
1624.5 to 1631.5 
 
Decreases 
 
1631.5 to 1640.0 
 
Insertion loss < 1.3  dB 
 
1640.0 to 1658.0 
 
Insertion loss < 0.8  dB 
 
1658.0 to 1660.5 
 
Insertion loss < 0.9  dB 
 
1660.5 to 1670.0 
 
Increases 
 
1670.0 to 1700.0 
 
>   10  dB 
 
1700.0 to 1735.0 
 
>   40  dB 
 
1735.0 to 12000 .0 
 
>   50  dB 
 
12000.0 to 18000.0 
 
>   15  dB 
 
Pre-HPA Filter - For Reduction of Spurious and Noise 
 
 
Frequency (MHz) 
 
Rejection 
 
      0.0 to 1610.0 
 
Not defined 
 
1610.0 to 1614.0 
 
>     5  dB 
 
1614.0 to 1626.5 
 
>   10  dB 
 
1626.5 to 1631.5 
 
Decreases 
 
1631.5 to 1660.5 
 
Don't care 
 
1660.5 to 1665.0 
 
Increases 
 
1665.0 to 1670.0 
 
>     5  dB 
 
1670.0 to 1700.0 
 
>   15  dB 
 
1700.0 to 18000 .0 
 
Not defined 
 
Transmitter Output Characteristics The system RF characteristics are determined by both the diplexer transmit filter and the HSN and IM generated prior to the diplexer in the transmit RF chain. 
From ARINC Characteristic 741, Part 1, Section 2.2.5.1: 
 
Harmonics, Discrete Spurious and Noise 
 
Frequency (MHz) 
 
Power Density 
 
 
0.0 to 1525.0 
 
 
-55  dBc/ 4 kHz 
 
 
1525.0 to 1559.0 
 
-83  dBc/ 4 kHz 
 
 
1559.0 to 1614.0 
 
-55  dBc/ 1 MHz 
 
 
1614.0 to 1660.0 
 
-55  dBc/ 4 kHz* 
 
 
1660.0 to 1670.0 
 
-55  dBc/ 20 kHz 
 
 
1670.0 to 1675.0 
 
-55  dBc/ 1 MHz 
 
 
1675.0 to 18000  
-55  dBc/ 4 kHz 
 
* 
Excluding the carrier frequency ±35 kHz. HPA IM levels taken from the table in ARINC Characteristic 741, Part 1, Section 2.2.5 for a Linear Type 
2 HPA: 
 
 
IM Product Level Limits 
Order 


IM Level 
 
3rd 


-25  dBc 
 
5th 


-25  dBc 
 
7th (carriers spaced 13.5 to 14.5 kHz) 
 
-30  dBc 
 
7th (carriers spaced less than13.5 kHz) 
 
-33  dBc 
 
Greater than 7th and less than 12 GHz 
 
-35  dBc 
 
Greater than 7th and from 12 to 18 GHz 
 
-70  dBc 
Examples HSN Example 


Modified 

Type A 
Frequency (MHz) 
 HPA Output 
 
Diplexer 
       MOPS 
 
1559 to 1585 
 
-55  dBc/MHz 
 
 100  dB 
-155 dBc/MHz 
IM Example - 3rd Order 


Modified 

Type A 
Frequency (MHz) 
HPA Output 
 
Diplexer 
  MOPS 
1610 to 1614 
 
  -25  dBc 
 
  40  dB  
-64  dBc 
IM Example - 7th  Order (Carriers Spaced less than 13.5 kHz) 


Modified 

Type A 
Frequency (MHz) 
HPA Output 
 
Diplexer 
 MOPS  
1610 to 1614 
 
  -33  dBc 
 
  40  dB  
-72  dBc Note that the IM limits in DO-210D give 1 dB margin compared to the ARINC Characteristic 741 HPA and diplexer values. 
 
