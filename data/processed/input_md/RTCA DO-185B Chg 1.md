 
Minimum Operational Performance Standards for Traffic Alert and Collision Avoidance System II (TCAS II) 
 
Version 7.1 
 
Change 1 
Copies of this document may be obtained from 
 
 
RTCA, Inc. 

1828 L Street, NW, Suite 805 
Washington, DC 20036, USA 
 
Telephone: 202-833-9339 
Facsimile: 202-833-9434 
Internet: www.rtca.org 


Please call RTCA for price and ordering information. 

Executive Summary This Change 1 document specifies a change to the TCAS II requirements contained in RTCA document DO-185B. The rationale for the change is described in change proposal CP123, which was approved by the SC-147 Requirements Working Group. The first part of the change concerns an aspect of the TCAS multiaircraft logic. It affects the 
"middle" aircraft of a multi-threat situation, and removes the feature that would have required a green arc to accompany that aircraft's RA. The second part of the change clarifies the coding of certain bits reporting Hybrid Surveillance capability within the Data Link Capability Report, to be consistent with a change made to DO- 300. Section 1 provides the text changes to Volume I. Section 2 provides changes to the Pseudocode in Volume II, Attachment A. Section 3 provides changes to the state charts in Volume II. Section 4 provides changes to the TSIM data set that is specified for the verification of the TCAS implementation. This material is not part of DO-185B, but is accompanying material distributed by FAA, not by RTCA. 

## This Page Intentionally Left Blank 1  Changes To Volume I The Following Correction Is Needed In Order To More Accurately Describe The Behavior Of The Multi-Aircraft Logic When Own Aircraft Is "Projected In The Middle". 2.2.5.3.3 Multi-Aircraft Logic

Note: 
Special rules are invoked when a TCAS-equipped aircraft is involved in a 
multiple-aircraft encounter.  The pilot of the aircraft with "projected clear 
airspace above" is told to CLIMB, and the pilot of the aircraft with "projected clear airspace below"  is told to DESCEND.  Aircraft "projected in the middle" 
are told to limit their climb and their descent until the aircraft above or below 
are no longer in conflict. 
 
The selection of a positive DESCEND advisory in a multi-aircraft situation is also subject to the performance limitations of the TCAS aircraft when it is near the Descend Inhibit altitude threshold.  In this case, a negative DON'T CLIMB 
will be selected instead of DESCEND. 
 
The multi-aircraft logic has been designed to prevent premature level-off RAs when own is to pass between two threats vertically.  This requires retention of a 
positive RA until certain criteria have been met so that vertical separation is maximized.  The multi-aircraft logic also includes the ability to model and select 
Increase Rate RAs and sense reversals to better resolve situations that are 
deteriorating due to adverse maneuvers by own aircraft or one of the threats.  
(The ability to generate an Increase Rate RA is subject to the INCREASE CLIMB and INCREASE DESCENT inhibit indications and thresholds.)  The logic also 
performs an unbiased evaluation of all new threats to select the optimum RA against all rather than constraining the RA to be selected against the second or third threat by the initial choice against the first. 
 
Following is the change needed to the coding of the data link capability report:    

## 2.2.3.9.3.2.3.2.1 Coding Of Data Link Capability Report - Do-185A,B Systems

Bits 48, 69, 70, 71 and 72 are used to convey TCAS capability information as follows: 
Bit(s) Coding 
48 
0 = TCAS failed or on standby 
 
1 = TCAS operating 
 
 
69 
0 = Hybrid surveillance not operational 
 
1 = Hybrid surveillance fitted and operational 
 
 
70 
0 = TCAS generating TAs only 
 
1 = TCAS generating TAs and RAs 
 
 
72,71 TCAS Version 
0,0 = RTCA DO-185 
 
0,1 = RTCA DO-185A 
 
1,0 = RTCA DO-185B and ED-143 
 
1,1 = Future versions (see registers E516 and E616 in Ref. L) 

 

## 2.2.3.9.3.2.3.2.2 Coding Of Data Link Capability Report - Faa Tso-C119A Systems

| Bit 48:                                                                 | Bit 48 = 1 indicates that the TCAS/transponder interface is    |
|-------------------------------------------------------------------------|----------------------------------------------------------------|
| operational and that TCAS is reporting RI=2 or 3 for use in the         |                                                                |
| air-to-air Reply Information field (2.2.3.9.3.1.14).                    |                                                                |
|                                                                         |                                                                |
| Bits 69, 70:                                                            | On-Board Resolution Capability Bits - Bits 69 and 70 form a    |
| capability code subfield which indicates aircraft's on-board            |                                                                |
| resolution advisory generation capability.                              |                                                                |
| The codes are:                                                          |                                                                |
| 0 = No on-board resolution advisory generation capability.              |                                                                |
| 1 = An on-board vertical-only resolution advisory generation capability |                                                                |
| exists.                                                                 |                                                                |
| 2 = An on-board vertical and horizontal resolution advisory generation  |                                                                |
| capability exists (not applicable to FAA TSO-C119A systems).            |                                                                |
| 3 = Not assigned.                                                       |                                                                |
|                                                                         |                                                                |
|                                                                         |                                                                |

Following is the change needed to a test procedure, as a result of the change made to section 
2.2.3.9.3.2.3.2.1: 

## 2.4.2.2.5      Tcas Capability Reporting (2.2.3.13.2.2.4 And 2.2.3.13.2.2.1)

 (text omitted) 
When testing with an RTCA/DO-185A,B compatible Mode S transponder: 

Msgs: 
DF=20 with BDS=16, bits 48, 69, 70, 71, 72 = 0xy01 at T=4 and 64
 
DF=21 with BDS=16, bits 48, 69, 70, 71, 72 = 0xy01 at T=9 and 69
 
DF=20 with BDS=16, bits 48, 69, 70, 71, 72 = 1x001 at T=24, 34 
 
DF=21 with BDS=16, bits 48, 69, 70, 71, 72 = 1x001 at T=29, 39 
 
DF=20 with BDS=16, bits 48, 69, 70, 71, 72 = 1x101 at T=44, 54 
 
DF=21 with BDS=16, bits 48, 69, 70, 71, 72 = 1x101 at T=49, 59 
Where x=0 if hybrid surveillance is not operational 
 
x=1 if hybrid surveillance is fitted and operational 
 
y=don't care 
 
This Page Intentionally Left Blank
2  Changes to Pseudocode 
 
The pseudocode changes needed to implement change proposal CP123 follow. Only a single pseudocode program is affected, Set_up_display_outputs (DO-185B, Volume II, Attachment A, pages 8-P16 and 8-
P17). Both the published DO-185B version (BEFORE) and the revised version (AFTER) of both the high-level and low-level pseudocode are shown below. The changes in the AFTER versions are highlighted. In addition to the changes needed to implement the change proposal, it was noted that the published version of the low-level pseudocode is missing a needed "G." reference to the global data structure G, and that is also fixed and highlighted. 

PROCESS Set_up_display_outputs; 
<Determine advisory annunciation precedence> 
 
IF (an RA is to be displayed this cycle) 
 
 
THEN IF (increase rate RA issued) 


THEN CLEAR reversal, maintain rate, and altitude crossing flags; 


IF (increase rate RA was not present last cycle) 


THEN indicate that RA changed to increase rate this cycle; 


ELSE CLEAR indication that increase rate RA was present last cycle; 


IF (RA requires maintenance of rate) 


THEN SET maintain rate indication; 


CLEAR sense reversal indication, if any;  <announce maintain> 


ELSE IF (previous cycle's RA was dual negative AND current RA is 


either single negative or positive) 


THEN CLEAR maintain rate indication; 


IF (sense of previously displayed RA has been reversed) 


THEN CLEAR altitude crossing flag;  <Reversal needs to be  


announced even if the reversed RA is altitude crossing> 


CLEAR maintain rate indication;  <If reversing maintain RA>  


IF (RA is preventive) 
<Initial preventive neg. or VSL RA or weakening> 


<Note:  All positive RAs are now corrective> 


THEN IF (RA is dual negative) <Don't Climb/Don't Descend> 


THEN SET maintain rate indication;  <announce maintain> 


ELSE CLEAR maintain rate indication; 


IF (positive Climb is weakening to negative Don't 


Descend OR (positive Descend is weakening to  


negative Don't Climb AND not in extreme low  


altitude condition))  


THEN indicate that weakened RA is corrective; 


<Results in green "fly-to" arc plus 


corrective aural annunciation for initial 


weakening> 


Set displayed-model-goal rate to 0 fpm;  <RA display device  


will use prescribed vertical rates for neg. & VSL RAs> 


ELSE IF (RA is corrective negative or VSL) 


THEN CLEAR maintain rate indication; 


Set displayed-model-goal rate to 0 fpm; 


CLEAR clear of conflict flag; 
 
 
ELSE CLEAR maintain rate indication;  <no RA is to be displayed this cycle> 


Set displayed-model-goal rate to 0 fpm; 


IF (an altitude-reporting threat became non-altitude-reporting during preceding RA) 


THEN CLEAR track drop and clear of conflict flags; 


ELSE IF (a threat's track was dropped during preceding RA) 


THEN CLEAR clear of conflict flag; 
 
PERFORM Load_display_and_aural_info; <Load display information to be sent to the RA display, 


TA display and aural annunciation subsystem.> 
END Set_up_display_outputs;  
  
PROCESS Set_up_display_outputs; 
<Determine advisory annunciation precedence> 
 
IF (an RA is to be displayed this cycle) 
 
 
THEN IF (increase rate RA issued) 


THEN CLEAR reversal, maintain rate, and altitude crossing flags; 


IF (increase rate RA was not present last cycle) 


THEN indicate that RA changed to increase rate this cycle; 


ELSE CLEAR indication that increase rate RA was present last cycle; 


IF (RA requires maintenance of rate) 


THEN SET maintain rate indication; 


CLEAR sense reversal indication, if any;  <announce maintain> 


ELSE IF (previous cycle's RA was dual negative AND current RA is 


either single negative or positive) 


THEN CLEAR maintain rate indication; 


IF (sense of previously displayed RA has been reversed) 


THEN CLEAR altitude crossing flag;  <Reversal needs to be  


announced even if the reversed RA is altitude crossing> 


CLEAR maintain rate indication;  <If reversing maintain RA>  


IF (RA is preventive) 
<Initial preventive neg. or VSL RA or weakening> 


<Note:  All positive RAs are now corrective> 


THEN IF (RA is dual negative) <Don't Climb/Don't Descend> 


THEN SET maintain rate indication;  <announce maintain> 


ELSE CLEAR maintain rate indication; 


IF ((positive Climb is weakening to negative Don't 


Descend OR (positive Descend is weakening to  


negative Don't Climb AND not weakening due  


to extreme low altitude condition)) AND not  


weakening due to multiaircraft "sandwich"  


encounter with both up-sense and down-sense  


VSLs) 


THEN indicate that weakened RA is corrective; 


<Results in green "fly-to" arc plus 


corrective aural annunciation for initial 


weakening> 


Set displayed-model-goal rate to 0 fpm;  <RA display device  


will use prescribed vertical rates for neg. & VSL RAs> 


ELSE IF (RA is corrective negative or VSL) 


THEN CLEAR maintain rate indication; 


Set displayed-model-goal rate to 0 fpm; 


CLEAR clear of conflict flag; 
 
 
ELSE CLEAR maintain rate indication;  <no RA is to be displayed this cycle> 


Set displayed-model-goal rate to 0 fpm; 


IF (an altitude-reporting threat became non-altitude-reporting during preceding RA) 


THEN CLEAR track drop and clear of conflict flags; 


ELSE IF (a threat's track was dropped during preceding RA) 


THEN CLEAR clear of conflict flag; 
 
PERFORM Load_display_and_aural_info; <Load display information to be sent to the RA display, 


TA display and aural annunciation subsystem.> 
END Set_up_display_outputs;  
 
PROCESS Set_up_display_outputs; 
IF (any bit in G.RA(1–10)EQ $TRUE) 
 
 
THEN IF (G.ANYINCREASE EQ $TRUE) 


THEN CLEAR G.ANYREVERSE, G.MAINTAIN, G.ANYCROSS; 


IF (G.PREVINCREASE EQ $FALSE) 


THEN SET G.ANYCORCHANG, G.PREVINCREASE; 


ELSE CLEAR G.PREVINCREASE; 


IF ((G.RA(1) EQ $TRUE AND G.ZDMODEL GT P.CLMRT AND  


G.ZDOWN GT P.CLMRT) OR (G.RA(6) EQ $TRUE AND 


G.ZDMODEL LT P.DESRT AND G.ZDOWN LT P.DESRT)) 


THEN SET G.MAINTAIN; 


CLEAR G.ANYREVERSE; 


ELSE IF ((G.CLSTROLD EQ 4 AND G.DESTROLD EQ 4) AND 


(G.CLSTRONG EQ 0 OR G.DESTRONG EQ 0)) 


THEN CLEAR G.MAINTAIN; 


IF (G.ANYREVERSE EQ $TRUE) 


THEN CLEAR G.ANYCROSS; 


CLEAR G.MAINTAIN; 


IF (G.CORRECTIVE_CLM EQ $FALSE AND  


G.CORRECTIVE_DES EQ $FALSE)  


THEN IF (G.RA(2) EQ $TRUE AND G.RA(7) EQ $TRUE)  


THEN SET G.MAINTAIN; 


ELSE CLEAR G.MAINTAIN; 


IF (G.CLSTRONG EQ 4 AND  


G.CLSTROLD EQ 8) 


THEN SET G.CORRECTIVE_CLM,  


G.ANYPRECOR; 


ELSE IF (G.DESTRONG EQ 4 AND  


G.DESTROLD EQ 8 AND  


G.EXTALT EQ $FALSE) 


THEN SET CORRECTIVE_DES, 


G.ANYPRECOR; 


G.ZDMODEL = 0; 


ELSE IF (G.RA(1 and 6) EQ $FALSE) 


THEN CLEAR G.MAINTAIN; 


G.ZDMODEL = 0; 


CLEAR G.ALLCLEAR; 
 
 
ELSE CLEAR G.MAINTAIN, G.ANYINCREASE; 


G.ZDMODEL = 0; 


IF (ANYALTLOST EQ $TRUE) 


THEN CLEAR ANYTRACKDROP, G.ALLCLEAR; 


ELSE IF (ANYTRACKDROP EQ $TRUE) 


THEN CLEAR G.ALLCLEAR; 
 
PERFORM Load_display_and_aural_info; 
 
END Set_up_display_outputs; 
 
 
PROCESS Set_up_display_outputs; 
IF (any bit in G.RA(1–10)EQ $TRUE) 
 
 
THEN IF (G.ANYINCREASE EQ $TRUE) 


THEN CLEAR G.ANYREVERSE, G.MAINTAIN, G.ANYCROSS; 


IF (G.PREVINCREASE EQ $FALSE) 


THEN SET G.ANYCORCHANG, G.PREVINCREASE; 


ELSE CLEAR G.PREVINCREASE; 


IF ((G.RA(1) EQ $TRUE AND G.ZDMODEL GT P.CLMRT AND  


G.ZDOWN GT P.CLMRT) OR (G.RA(6) EQ $TRUE AND 


G.ZDMODEL LT P.DESRT AND G.ZDOWN LT P.DESRT)) 


THEN SET G.MAINTAIN; 


CLEAR G.ANYREVERSE; 


ELSE IF ((G.CLSTROLD EQ 4 AND G.DESTROLD EQ 4) AND 


(G.CLSTRONG EQ 0 OR G.DESTRONG EQ 0)) 


THEN CLEAR G.MAINTAIN; 


IF (G.ANYREVERSE EQ $TRUE) 


THEN CLEAR G.ANYCROSS; 


CLEAR G.MAINTAIN; 


IF (G.CORRECTIVE_CLM EQ $FALSE AND  


G.CORRECTIVE_DES EQ $FALSE)  


THEN IF (G.RA(2) EQ $TRUE AND G.RA(7) EQ $TRUE)  


THEN SET G.MAINTAIN; 


ELSE CLEAR G.MAINTAIN; 


IF (G.CLSTRONG EQ 4 AND  


G.CLSTROLD EQ 8 AND 


G.DESTRONG EQ 0) 


THEN SET G.CORRECTIVE_CLM,  


G.ANYPRECOR; 


ELSE IF (G.DESTRONG EQ 4 AND  


G.DESTROLD EQ 8 AND 


G.CLSTRONG EQ 0 AND  


G.EXTALT EQ $FALSE) 


THEN SET G.CORRECTIVE_DES, 


G.ANYPRECOR; 


G.ZDMODEL = 0; 


ELSE IF (G.RA(1 and 6) EQ $FALSE) 


THEN CLEAR G.MAINTAIN; 


G.ZDMODEL = 0; 


CLEAR G.ALLCLEAR; 
 
 
ELSE CLEAR G.MAINTAIN, G.ANYINCREASE; 


G.ZDMODEL = 0; 


IF (ANYALTLOST EQ $TRUE) 


THEN CLEAR ANYTRACKDROP, G.ALLCLEAR; 


ELSE IF (ANYTRACKDROP EQ $TRUE) 


THEN CLEAR G.ALLCLEAR; 
 
PERFORM Load_display_and_aural_info; 
 
END Set_up_display_outputs;
Following is the pseudocode change to the routine Send_owndata_to_trans that refers to the coding of the hybrid surveillance capability in the Data Link Capability Report. 

PROCESS Send_owndata_to_trans; 
<Set up fields for SLC Update messages and data link capability report to transponder:> 
 
OWNDATA_TO_TRANS.SL = G.INDEX; <Indicate current sensitivity level> 
CLEAR OWNDATA_TO_TRANS.BIT_69;  

 
 
<This bit must be set to 1 if hybrid surveillance is fitted and operational> 
IF (G.INDEX GE 2 AND G.INDEX LE 7 AND G.OPFLG EQ $TRUE)  
 
 
THEN SET OWNDATA_TO_TRANS.BIT_48; 
 
 
ELSE CLEAR OWNDATA_TO_TRANS.BIT_48; 


IF (G.OPFLG EQ $TRUE) 


THEN SET OWNDATA_TO_TRANS.BIT_70; 


ELSE CLEAR OWNDATA_TO_TRANS.BIT_70; 
IF (G.RAMODE EQ $TRUE) 
 
 
THEN OWNDATA_TO_TRANS.RI = 3; <Onboard TCAS with vertical-only RA 

capability> 


SET OWNDATA_TO_TRANS.BIT_70; 
 
 
ELSE  IF (G.TAMODE EQ $TRUE) 


THEN OWNDATA_TO_TRANS.RI = 2; <Onboard TCAS with RA 

capability inhibited> 


CLEAR OWNDATA_TO_TRANS.BIT_70; 


ELSE  OWNDATA_TO_TRANS.RI = 0; <No onboard TCAS> 


OWNDATA_TO_TRANS.VI = 1; 
 
CLEAR OWNDATA_TO_TRANS.BIT_71; 
SET OWNDATA_TO_TRANS.BIT_72; 
Send SLC Update message (i.e., SL, RI and VI) to transponder; 
 
IF (G.TRANSVI EQ 1) 
 
 
THEN send data link capability report (i.e., BIT_48, BIT_69, BIT_70, BIT_71, and  


BIT_72) to transponder; 
 
END Send_owndata_to_trans; _____________TRACKING LOW-LEVEL LOGIC___________________ 
This Page Intentionally Left Blank 

## 

3  Changes to State Charts There are two transition tables that need to be updated to match the Multiaircraft changes in the pseudocode. These are the Yes to No transition tables for the Corrective_Climb and the Corrective_Descend states on pages 125 and 127, respectively, of DO-185B Volume II. The original DO-
185B form of those two transition tables are shown next, followed by the revised versions of those two tables with the changes highlighted. Note that in addition to the changes made to match the proposed pseudocode change, the subscript page references for the functions Climb_Goal and Descend_Goal are changed because the values printed in DO-185B are incorrect. 

 
Location:  Advisory_Statuss-261  Corrective_Climbs-123  
Trigger Event:  Composite_RA_Evaluated_Evente-C2 

Condition: 
 
OR 
 
Climb_RA_Weakenedm-374  
T
 T  . 
 
Climb_Goalf-410 = 0 ft/min 
F
 T  . 
 
Own_Tracked_Alt_Ratef-564 > Climb_Goalf-410  
T
 .  . 
AND Own_Tracked_Alt_Ratef-564 > –300 ft/min(HYSTERCOR) 
.  T  . 
 
Own_Tracked_Alt_Ratef-564  300 ft/min(HYSTERCOR) 
.  T  . 
 
Descend_Goalf-411 = 0 ft/min 
.  T  . 
 
Not_Meeting_Descend_Goalm-411  
.  .  T 

Output Action: Corrective_Climb_Evaluated_Evente-C2 

Notes: 
1. 
Description:  Transition out of corrective climb occurs for a weakened climb RA 
condition when either the own aircraft altitude rate exceeds a non-zero climb goal or the aircraft is considered level (i.e., within hysteresis) for a zero climb and 
descend goal.  This transition also occurs whenever the aircraft is not meeting the 
current descend goal. 
 
2. 
Pseudocode Reference:  Corrective_preventive_test. 
 

Transition(s): 

Location:  Advisory_Statuss-261  Corrective_Descends-229 
Trigger Event:  Corrective_Climb_Evaluated_Evente-C2 

Condition: 
 
  OR 
 
Descend_RA_Weakenedm-378 
T
 T  .  T
 
Descend_Goalf-411 = 0 ft/min 
F
 T  .  T
 
Own_Tracked_Alt_Ratef-564 < Descend_Goalf-411 
T
 .  .  . 
 
Own_Tracked_Alt_Ratef-564 < 300 ft/min(HYSTERCOR) 
.  T  .  T
 AND Own_Tracked_Alt_Ratef-564  300 ft/min(HYSTERCOR) 
.  T  .  . 
 
Climb_Goalf-410 = 0 ft/min 
.  T  .  . 
 
Not_Meeting_Climb_Goalm-410 
.  .  T  . 
 
Extreme_Alt_Checkm-378 
.  .  .  T
 
Multiple_Threatsm-403  
.  .  .  F
Output Action:  Corrective_Descend_Evaluated_Evente-C2 
Notes: 
1. 
Description:  Transition out of corrective descend occurs for a weakened descend 
RA condition when (1) the own aircraft altitude rate is less than a non-zero descend goal, or (2) the aircraft is considered level (i.e., within hysteresis) for a zero climb and descend goal, or (3) the aircraft is not meeting the current climb 
goal, or (4) a descend RA is weakened to a zero climb rate goal under extreme 
low altitude against a single threat aircraft. 

 
2. 
Pseudocode Reference:  Corrective_preventive_test, Set_up_display_outputs, 
Extreme_altitude_check. 
 
Location:  Advisory_Statuss-261  Corrective_Climbs-123  
Trigger Event:  Composite_RA_Evaluated_Evente-C2 

Condition: 
 
OR 
 
Climb_RA_Weakenedm-374  
T
 T  .  T
 
Climb_Goalf-467 = 0 ft/min 
F
 T  .  T
 
Own_Tracked_Alt_Ratef-564 > Climb_Goalf-467  
T
 .  .  . 
AND Own_Tracked_Alt_Ratef-564 > –300 ft/min(HYSTERCOR) 
.  T  .  T
 
Own_Tracked_Alt_Ratef-564  300 ft/min(HYSTERCOR) 
.  T  .  . 
 
Descend_Goalf-473 = 0 ft/min 
.  T  .  . 
 
Not_Meeting_Descend_Goalm-411  
.  .  T  . 
 
Descend_Goal f-473 < 100,000 ft/min(HUGE) 
.  .  .  T

Output Action: Corrective_Climb_Evaluated_Evente-C2 

Notes: 
1. 
Description:  Transition out of corrective climb occurs for a weakened climb RA 
condition when either the own aircraft altitude rate exceeds a non-zero climb goal or the aircraft is considered level (i.e., within hysteresis) for a zero climb and 
descend goal.  This transition also occurs whenever the aircraft is not meeting the 
current descend goal or there is a simultaneous opposite-sense VSL due to a multiaircraft encounter. 
 
2. 
Pseudocode Reference:  Corrective_preventive_test, Set_up_display_outputs. 
 

 
Transition(s): 

Location:  Advisory_Statuss-261  Corrective_Descends-229 
Trigger Event:  Corrective_Climb_Evaluated_Evente-C2 

Condition: 
 
  OR 
 
Descend_RA_Weakenedm-378 
T
 T  .  T
T
 
Descend_Goalf-473 = 0 ft/min 
F
 T  .  T
T
 
Own_Tracked_Alt_Ratef-564 < Descend_Goalf-473 
T
 .  .  . 
. 
 
Own_Tracked_Alt_Ratef-564 < 300 ft/min(HYSTERCOR) 
.  T  .  T
T
 AND Own_Tracked_Alt_Ratef-564  300 ft/min(HYSTERCOR) 
.  T  .  . 
. 
 
Climb_Goalf-467 = 0 ft/min 
.  T  .  . 
. 
 
Not_Meeting_Climb_Goalm-410 
.  .  T  . 
. 
 
Extreme_Alt_Checkm-378 
.  .  .  T
. 
 
Multiple_Threatsm-403  
.  .  .  F
. 
 
Climb_Goalf-467 > 100,000 ft/min(HUGE) 
.  .  .  . 
T
Output Action:  Corrective_Descend_Evaluated_Evente-C2 
Notes: 
1. 
Description:  Transition out of corrective descend occurs for a weakened descend 
RA condition when (1) the own aircraft altitude rate is less than a non-zero descend goal, or (2) the aircraft is considered level (i.e., within hysteresis) for a zero climb and descend goal, or (3) the aircraft is not meeting the current climb goal, or (4) a descend RA is weakened to a zero climb rate goal under extreme low altitude against a single threat aircraft, or (5) there is a simultaneous opposite-sense VSL due to a multiaircraft encounter. 

 
2. 
Pseudocode Reference:  Corrective_preventive_test, Set_up_display_outputs, 
Extreme_altitude_check. 
 
The following output interface change, section 1.3.10 of DO-185B Volume II, corrects the Hybrid Surveillance capability reporting within the Data Link Capability Report. 

Output Interfaces                                              Data_Link_Capability_Report 
__________________________________________________________________ 
1.3.10  Interface:  Data_Link_Capability_Report 
 
Source:  CAS 
 
Destination:  Mode_S_Transponder 
 
Trigger Event:  Effective_SL_Evaluated_Evente-C2 
 
Condition: 
 
Mode_S_Versionv-55 = Version_7 
 
if (Effective_SLs-97 **in one of** {2,3,4,5,6,7} and TCAS_Operational_Statusv-42 = Operational) 
 
Assignments:  None 
 
Output Action:  SEND(Data_Link_Capability_Report(BIT48, BIT69, BIT70, BIT71, BIT72) 
 
Abbreviations: 
 
TCAS_Operational_Statusv-42 = Operational) 
 
BIT69 = 0   ***** This bit must be set to 1 if hybrid surveillance is fitted and operational***** 
 

Notes: 
1. 
Description:  The data link capability report is sent to the Mode S transponder for 
downlink to a ground station receiver. 
 
2. 
Pseudocode Reference:  Send_owndata_to_trans.
This Page Intentionally Left Blank

## 4  Changes To Tsim This Material Is Not Part Of Do-185B. It Is Accompanying Material Distributed By Faa, Not By Rtca. Certain Files That Are Compiled Into The Tsim Simulation Program Or That Provide Input Data To That Program Must Be Modified To Reflect The Changes To Both The Pseudocode And The Statecharts. The Necessary Changes Are Indicated Below. The Headings Are The Names Of The Files That Must Be Modified. 4.1 Trans7.Dat

[Corrective_Climb, Yes -> No] Base_Number = 2.1.11.2 Trigger = Composite_RA_Evaluated_Event Output = Corrective_Climb_Evaluated_Event !Climb_RA_Weakened;                    T  T  .  T Climb_Goal = 0;                        F  T  .  T Descend_Goal = 0;                      .  T  .  . Own_Tracked_Alt_Rate > Climb_Goal;     T  .  .  . Own_Tracked_Alt_Rate > 0 - HYSTERCOR;  .  T  .  T Own_Tracked_Alt_Rate <= HYSTERCOR;     .  T  .  . !Not_Meeting_Descend_Goal;             .  .  T  . Descend_Goal < HUGE;                   .  .  .  T *** The row above and new column is added by Hui Men (JHU/APL) 2008.12.12 IP-15 … [Corrective_Descend, Yes -> No] Base_Number = 2.1.11.3 Trigger = Corrective_Climb_Evaluated_Event Output = Corrective_Descend_Evaluated_Event *** Begin:  Hui Men (JHU/APL) 2007.08.27 CP116 
!Descend_RA_Weakened;                  T  T  .  T  T 
Descend_Goal = 0;                      F  T  .  T  T 
Climb_Goal = 0;                        .  T  .  .  . Own_Tracked_Alt_Rate < Descend_Goal;   T  .  .  .  . Own_Tracked_Alt_Rate < HYSTERCOR;      .  T  .  T  T Own_Tracked_Alt_Rate >= 0 - HYSTERCOR; .  T  .  .  . !Not_Meeting_Climb_Goal;               .  .  T  .  . !Extreme_Alt_Check;                    .  .  .  T  . Multiple_Threats;                      .  .  .  F  . *** End:  Hui Men (JHU/APL) 2007.08.27 CP116 Climb_Goal > 0 - HUGE;                 .  .  .  .  T *** The above row and new column is added by Hui Men (JHU/APL)2008.12.12 for IP-15 
Line 946 
&& g_disp_else->de_strong == 0  

      // added by Hui Men (JHU/APL) on 2008.12.12 for IP-15  
 
Line 961 
&& g_disp_else->cl_strong == 0 

// added by Hui Men (JHU/APL) on 2008.12.12 for IP-15 
 