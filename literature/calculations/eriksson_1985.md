IEEE Power Engineering Society
i~~~
-
Power System Relaying
Committee

424 IEEE Transactions on Power Apparatus and Systems, Vol. PAS-104, No. 2, February 1985
AN ACCURATE FAULTLOCATOR WITH COMPENSATION FORAPPARENTREACTANCE
INTHE FAULT RESISTANCE RESULTING FROM REMOTE-ENDINFEED
Leif Eriksson, Murari MohanSaha, Member, IEEE G. D. Rockefeller, Fellow, IEEE
ASEA AB, Vasteras, Sweden ASEA AB, Vasteras, Sweden Rockefeller Associates, Inc.
Morris Plains, New Jersey
This novel approach is accomplished by using a complete
network model, where the infeed from the network beyond
the remote end point isrigorously taken into consideration.
Abstract - A microprocessor based fault locator is
described, which uses novel compensation techniques to Pre-fault load-current samples are stored and used for
improve accuracy. It displays the distance to the fault in compensation to eliminate a substantial effect on accuracy.
percent of transmission line length, for facilitating repair Also, representative values for the source impedances are
and restoration following a permanent fault. Also, it stored to compensate for variations in impedance angles.
pinpoints weak spots following transient faults. This novel approach is described as well as the system
design andperformance.
This new method for fault location on electric power
transmission lines uses recorded phase currents and voltages PURPOSE FOR FAULT LOCATORS
at the near end. The main feature of the method is that it
considers the influence of the remote-end infeed of the Even where helicopters are immediately available for
transmission line by using a complete network model. patrol following unsuccessful reclosing, fault locators
perform a valuable service. Trouble cannot always be found
with a routine patrol with no indication of where the fault
A microprocessor filters the ac currents and voltages occurred. For example, tree growth could reduce
from the protective relaying instrument transformers to clearances, resulting in a flashover during severe conductor
extract the fundamental components of the signals. It then sagging. By the time the patrol arrives, the conductors have
computes the distance to the fault point, compensating for cooled, increasing the clearance to the tree. The weak spot
the apparent reactance in the fault resistance resulting is not obvious.
from load current and the variations in impedance angles in
the power-system network. The importance of fault locators is more obvious
where foot patrols are relied upon, particularly on long
The design has undergone field tests and evaluation. lines, in rough terrain. Also, locators can help where
The outcome of the field tests is presented and has maintenance jurisdiction is divided between different
confirmed the validity of the concept of the fault locator, companies or divisions within a company.
showing anaccurate display ofthe distance to fault.
Fault locators are valuable even where the line has
INTRODUCTION been restored either automatically or non-automatically. In
this category are faults caused by cranes swinging into the
Distance relays for transmission-line protection line, brushfires, damaged insulators and vandalism. The
provide some indication of the general area where a fault locator allows rapid arrival at the site before the evidence
occurred, but theyare not designed to pinpoint the location. is removed or the "trailbecomes cold"?. Also, the knowledge
Since pRower circuit breakers are only installed at the that repeat faults are occurring in the same area can be
terminals, it is immaterial where the line faulted for valuable in detecting the cause. Weak spots that are not
isolating the flashover. However, with immediate obvious may be found because a more thorough inspection
knowledge of the location, the nature (type and measuring can be focussed in the limited area defined by the fault
data) of the fault can be determined quickly, facilitating locator.
repair and restoration. A locator is also useful for transient
faults, pointing to a weak spot that is threatening further FAULT LOCATION FUNDAMENTALS
trouble.
The fault location computations determine the
Various methods were developed during the recent apparent fault impedance with novel compensation for the
years to detect the location of fault on a transmission line. fault resistance drop, eliminating the errors inherent in
They are mostly based on analog techniquest2]. Some fault conventional reactance-type measurements. For a fault-
locator designs are inservice which are reliable in detecting protection relay these errors are tolerable because a safety
permanent faults. New methods and systems of fault margin is inserted in its setting. However, for the fault
locationbasedonboth analog and digital techniques seem to locator a more precise measurement is quite desirable. The
offer good prospects to obtain a precise location of Appendix derives the equation for the apparent impedance
transient faults also. The method reported in [ii is an seen by a reactance-type measurement. Figs. Al and A2
approximate method. The method of fault location illustrate the apparent reactance effect in the fault-
technique described here seems more advantageous, since it resistance term.
takes into consideration the effects ofboth endsof the line.
Fig. 1 shows the connection of the fault locator at
84 SM 624-3 A paper recomnended and approved station A. Using the ac quantities available at station A, it
by the IEEE Power System Relaying Committee of the is not possible to determine the total fault current IF unless
IEEE Pow'er Engineering Society for presentation at p and ZSB are known; conventional devices tolerate the
the IEEE/PES 1984 Summer Meeting, Seattle, errors resulting from the infeed current IB flowing through
Washington, July 15 - 20, 1984. Manuscript sub- the fault resistance RF, out ofphase with respect to IA.
mitted August 30, 1984; made available for print-
ing May 4, 1984. In the method reported in Reference 1, the current
distribution factors for the parts of the network, located on
either side of the fault point, are assumed to have the same
arguments, or else it is assumed that the difference between
the arguments is known and constant along the line segment
0018-9510/85/0002-0424$01.00(1985 IEEE

425
L- L1 1I UAE (UA)L L ( bIL UFE
'LD
IF
UA
77+7
(UlA), UF
UA.E UB3E
Fig. 1 Power system one-line diagram with fault.
in question. This simplified assumption can give rise to
substantial errors in the calculated fault distance. The
difference between the two arguments mentioned generally
varies with the distance to the fault.
The fault locator program described here utilizes
representative values of the source impedances to
determine a correct description of the network. The value Fig. 2 Prefault conditions.
of RF is unknown; however, it is not needed - only the
angle ofIFRF, the faultpoint voltage, is used.
The other key aspect of this locator's algorithm is its (UlA)F PZIL (1-P)ZlL
use of pre-fault current memory to determine the change in
line current caused by the fault: the actual fault current
minus the prefault value. Eq. (A9) from the appendix,
repeated here as Eq. (1) states that the station A voltage is
the sum of the drops in the line to the fault point plus the
faultpoint voltage:
UlA = '1A PZlL + I1FRF (1)
Eq. (1) is written for a3-phase fault, using the positive
sequence notations. Eq. (2) expresses the same concept in
general terms applicable to any fault:
UA = IA PZL + IFRF (2)
To consider load current effects, the actual voltages
and currents can be considered to be composed of the
prefault values plus the changes caused by the fault. The
appendix discusses this concept. The load currents are
generated in Fig. 2 by the angular difference between the
source voltages. Voltage UF exists at the fault point prior to
the fault and is the driving voltage in Fig. 3 producing the
changes caused by the fault.
From Fig. 3, the change in positive-sequence current
in the line at A, AI1A, is related to the total positive-
sequence current by the current distribution factor DiA:
Fig. 3 Faulted network (Thevenin equivalent).
AI1A = DlA IlF (3)
Writing a similar, butgeneral expression: processing of the zero-sequence components to obtain rF.
Fig. 4 shows the current relations in the fault for an SLG
IFA = DAIF (4) fault:
where IFA is the current change produced by the fault, 33 = F = I2F = IOF (5)
equal to the actual fault current less the prefault current.
The expression for IFA varies with the fault type; Table I
defines these. Changes in phase currents are used except Eliminating the zero-sequence current IOF
for single-line-ground faults. The latter use the change in IF 3/2 ( IlF + 12F)
faulted phase current less the zero sequence current IOA. =
The zero-sequence current is extracted because the zero- AI'A +AI2A
sequence distribution factor DOA is not known as reliably DiA (6)
as the positive-sequence factor DiA. The 3/2 factor in
Table I provides heavier weighting to compensate for the
I-amoval of the zero-sequence current.
The distribution factors for the positive- and negative-
The IFA expression for a single-line-ground (SLG) fault sequence currents may be assumed, with great accuracy, to
will now be derived with the objective of eliminating the be equal(i.e., DIA = D2A).

426
|     |     |     |     |     |     | The | complex | expression |     | of Eq. | (14) | contains | the unknowns |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ------ | ---- | -------- | ------------ | --- |
p
IF IF = 3/2(I1F + 12F) and RF. However, Eq. (14) be separated into two
can
|     |     |     |                 |        |     | simultaneous |          | equations, |           | one        | real            | and one     | imaginary. | By         |
| --- | --- | --- | --------------- | ------ | --- | ------------ | -------- | ---------- | --------- | ---------- | --------------- | ----------- | ---------- | ---------- |
|     |     |     |                 |        |     | eliminating  |          | RF,        | a single  | expression |                 | results     | with       | the single |
|     |     |     |                 |        |     | unknown      |          | p. This    | is solved | by         | the             | program,    | using      | the peak   |
|     |     |     |                 |        |     | values       | and      | their      | phase     | position,  |                 | taken' from | the        | Fourier    |
|     |     |     | r, Ip 'F1/2(11F | + I2F) |     |              |          |            |           |            |                 |             |            |            |
|     |     |     |                 |        |     | analysis     | routine  |            | which     | yields     | the fundamental |             | components | of         |
|     |     |     |                 |        |     | the          | signals. |            |           |            |                 |             |            |            |
IIF + r2F
-I-.
|     |     |      |     |     |     | Fig.         | 5 provides |             | an alternative  |           | view         | of how     | the fault | locator           |
| --- | --- | ---- | --- | --- | --- | ------------ | ---------- | ----------- | --------------- | --------- | ------------ | ---------- | --------- | ----------------- |
|     |     |      |     |     |     | determines   |            | p without   | requiring       |           | the scalar   | value      | of        | the fault-        |
|     |     |      |     |     |     | p o i        | nt v o l   | t ag e . Fi | g . 5 i s       | tr i      | a n g ula t  | ion p ro b | l e m t o | d e t e r m i n e |
|     | I2F | = 3F |     |     |     |              |            |             |                 | a         |              |            |           |                   |
|     |     |      |     |     |     | t h e        | int e r    | s e c t ion | p o in t F      | , kn o w  | i n g U A    | an d I A   | b y m e   | a s u r e m e n t |
|     |     |      |     |     |     | and          | computing  |             | aD and          | aL.       | While        | the        | computer  | is not            |
|     |     |      |     |     |     | specifically |            | using       | this algorithm, |           | nevertheless |            | the       | conclusions       |
|     |     |      |     |     |     | reached      |            | using the   | concept         | of        | Fig. 5       | are valid: | viz.      | that the          |
|     |     |      |     |     |     | magnitude    |            | ofIFRF      | is not          | required, | butonly      |            | its angle | aD.               |
IF
i1F
= 3r
|            |                    |             |                            |     |        |     |     |     |     |     | Intersection | computed |     |     |
| ---------- | ------------------ | ----------- | -------------------------- | --- | ------ | --- | --- | --- | --- | --- | ------------ | -------- | --- | --- |
| Fig.       | 4 Currentrelations |             | for asingle-line-to-ground |     | fault. |     |     |     |     |     |              |          |     |     |
| At station | A                  | in theline: |                            |     |        |     |     |     |     |     |              |          |     |     |
,s_
| AIA | =AIIA | +A12A | + AIOA |     |     |     |     | 4   |     |     |     |     |     |     |
| --- | ----- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(7)
| or AI1A+ |     | AI2A=AIA-AIOA |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(8)
IA
| Neglecting |     | pre-faultzero-sequence | current: |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IA;
|           |     |     |         |     |     |     |     |     | Measured: |     |     | UA  |     |     |
| --------- | --- | --- | ------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
| AIlA+AI2A |     | =   | AIA-IOA |     |     |     |     |     |           |     |     |     |     |     |
(9)
|     |     |     |     |     |     |     |     |     | Computed: |     |     | aL  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
aD;
Eq. (9) in (6):
|     |     |      |      |     |     |     | Fig. |     | Fault-resistance-drop |     |     | compensation. |     |     |
| --- | --- | ---- | ---- | --- | --- | --- | ---- | --- | --------------------- | --- | --- | ------------- | --- | --- |
|     |     | I IA | ~IOA |     |     |     |      | 5   |                       |     |     |               |     |     |
T32
|     |     | IA  |     |     | (10) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F 3/2
|         |      |       |     |     |     | ParallelLine |     | Cases |     |     |     |     |     |     |
| ------- | ---- | ----- | --- | --- | --- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
| Let IFA | =3/2 | (A4lA |     |     |     |              |     |       |     |     |     |     |     |     |
-IOA)
|            |     |            |                          |     | (11) |         | The | locator       |     | be finished  |     | with modified |                   | algotithm   |
| ---------- | --- | ---------- | ------------------------ | --- | ---- | ------- | --- | ------------- | --- | ------------ | --- | ------------- | ----------------- | ----------- |
|            |     |            |                          |     |      |         |     |               | can |              |     | a             |                   |             |
|            |     |            |                          |     |      | for     | a   | parallel-line |     | application. |     | The           | positive-sequence |             |
| Thegeneral |     | expression | ofEq. (2) canberewritten |     |      |         |     |               |     |              |     |               |                   |             |
|            |     |            |                          | as: |      | network |     | is completely |     | described    | by  | re-defining   |                   | equation 13 |
I
as:
| UA  | IA  | PZL+ | jA) RF |     |      |     |     |       |       |         |       |       |     |       |
| --- | --- | ---- | ------ | --- | ---- | --- | --- | ----- | ----- | ------- | ----- | ----- | --- | ----- |
|     |     |      |        |     | (12) |     | DA  | (1-P) | (ZSA  | + ZSB   | + ZL) | + ZSB |     | (13A) |
|     |     |      |        |     |      |     |     |       | 2 ZSA | + 2 ZSB | + ZL  |       |     |       |
From Fig. 1:
|     |     |             |         |     |      |          | E q           | . ( 1 3A   | ) a s s u m | e s an    | i d e nt i c | al p a ra ll | e l l in       | e . U s e o f      |
| --- | --- | ----------- | ------- | --- | ---- | -------- | ------------- | ---------- | ----------- | --------- | ------------ | ------------ | -------------- | ------------------ |
| DA- | (   | 1 - P) Z L  | + Z S   |     |      |          |               |            |             |           |              |              |                |                    |
|     |     |             |         |     |      | the      | eq u          | a ti o n w | il l i m p  | r o ve ac | c u r a c    | y wi t h t   | h e pa r       | a l lel l in e i n |
|     |     | Z S A + Z L | + Z SB' |     |      |          |               |            |             |           |              |              |                |                    |
|     |     |             |         |     | (13) | service. |               |            |             |           |              |              |                |                    |
|     |     |             |         |     |      |          | Zero-sequence |            |             | mutual    | coupling     |              | be compensated |                    |
can
Substituting Eq. (13) in(12) and rearranging, yields: for by interconnecting two fault locators With a fault
.
|     |     |     |     |     |     | locator |     | on the | parallel | line | its residual | current |     | reading can |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------ | -------- | ---- | ------------ | ------- | --- | ----------- |
p-p K1 + K2 K3 RF = 0 be input to its companion locator via the local printer loop
input
|     |     |     |     |     | (14) | circuit; |     | the mutual | resistance |     | and | reactance | are | as  |
| --- | --- | --- | --- | --- | ---- | -------- | --- | ---------- | ---------- | --- | --- | --------- | --- | --- |
additionalsettingparameters.
where:
ALGORITHMS
pre-fault
KI _ UA +1+ ZSB (15) The fault location algorithm uses the and
| K2  | IAZL  |     |     |     |     | fault        | currents |     | and     | voltages  | at  | thei         | end | of the    |
| --- | ----- | --- | --- | --- | --- | ------------ | -------- | --- | ------- | --------- | --- | ------------ | --- | --------- |
|     |       |     | ZL  |     |     |              |          |     |         |           |     | near         |     |           |
|     |       |     |     |     |     | transmission |          |     | line to | determine |     | the distance |     | to fault. |
|     | K2- U | A   |     |     |     |              |          |     |         |           |     |              |     |           |
Z SB C u r r e n t v o l ta g e sa m p le s a r e c o n t i n uo u sl y m e a s u r ed .
|     | IA  | Z L | ' Z |     | (16) |     |             | a nd    |            |          |           |                |          |                  |
| --- | --- | --- | --- | --- | ---- | --- | ----------- | ------- | ---------- | -------- | --------- | -------------- | -------- | ---------------- |
|     |     |     |     |     |      | F   | o l l o w i | ng a si | gn a l f r | om t h e | li ne p r | ot e c t i o n | a t t he | i n s t a nt i t |
I F A initiates breaker tripping,current and voltage' samples for
ZSA+ Z SB si x c y c l e s f r o z en until the completion of the distance-
| K3= | I   | A Z L | +1) |     | (17) |     |              | a r e    |              |     |     |     |     |     |
| --- | --- | ----- | --- | --- | ---- | --- | ------------ | -------- | ------------ | --- | --- | --- | --- | --- |
|     |     |       | Z L |     |      | t   | o -f a u l t | c om p u | ta t i o n . |     |     |     |     |     |

427
TABLE I QUANTITIES PROCESSED FOR
VARIOUS FAULT TYPES
Type
of
Fault UA IA IPA
RN URA IRA + KN X INA 3/2 (AIRA-I0A)
SN USA ISA + KN X INA 3/2 (AISA -IOA)
TN UTA IrA + KN X INA 3/2 (AITA - IOA)
RST
RS URA - USA IRA -ISA AIRSA
RSN
ST USA - UTA ISA - ITA AISTA
STrN
TR UTA - URA ITA -IRA AITRA
TRN
The program then determines the loop of analog data The program selects 24 samples from the two periods
(currents and voltages) on which to base the computation. spanned by SL1 to SF1 in Fig. 6, where SFI is the third
For example, the RS loop is selected if the R and S phase sample following the fault point. For the fault data, 24
selectors operate. Table I shows the normal loop selection. samples immediately following SF1 in Fig. 6 are selected.
For double-line-ground faults only, a phase-to-ground loop
may be selected instead of the normal phase-phase loop, if The pre-fault and fault currents and voltages on all
desired. Table II shows the loop options. The program next phases are filtered by Fourier analysis to yield the
determines the fault inception point within the 6 cycle data, fundamental component. The selected loop quantities are
looking at the selected loop aC quantities, choosing the then processed for the distance-to-fault determination,
current(s) first. If necessary, the voltage(s) is also while the complete set is available for printing for user
processed to find the fault inception point. analysis.
Reading 24 samples apart are compared for a The fundamental components are determined by
significant change, starting with oldest samples. The multiplying each sample by the appropriate instantaneous.
required threshold for the current change is adaptive, sine value and integrating over a full period, then repeating
depending on the prefault current level. The voltage the process by multiplying by cosine values. The result
threshold is fixed. If no change is found, a one sample provides the scalar value and argument for each acquantity.
advance occurs and the procedure is repeated. The Fourier filtering effectively attenuates the dc offset
component and power system harmonics plus CCVT
transients and CT saturation distortion.
TABLE II LOOP SELECTION FOR DOUBLE-
The program uses the peak and angle outputs from the
LINE-TO-GROUND FAULTS filtering routine to compute the distance to the fault.
Phase LOOPSelected
Input Normal Cyclic Acyclic
RSN RS SN RN
STN ST TN TN
TRN TR RN RN
If unable to find the fault-inceptionpoint, the program
reverts to a "'slow start" algorithm, which eliminates the
load-current compensation. This would occur for a switch-
into-the-fault case or a time delay trip for an end-zone Pre-fault Relay time CB time
fault, where in such cases no prefault samples are available.
Memory capacity
In both cases, there would be no load flow to compensate,
because at the time of tripping the far end of the line would
be open. Faulted phase information
When a two-phase loop is selected (e.g. R and S foran
RSN selector input), two different fault inception points will
Fig. 6 Samples are selected from twoperiods
generally occur; the program selects the latter of the two before and after fault inception point Fp
fault points.

428
|     |     |     |          |     |     |     | initiating     | test programs | to  | the memoryand |     | for | resetting | the |
| --- | --- | --- | -------- | --- | --- | --- | -------------- | ------------- | --- | ------------- | --- | --- | --------- | --- |
|     |     |     | HARDWARE |     |     |     | LED indicator. |               |     |               |     |     |           |     |
Fig. 7 shows the main elements of the hardware. The Table III shows the parameters to be set by the
user.
digital inputs consist of the start signal from the line See GLOSSARY OF SYMBOLS. Parameters 1 to 4 are the
| protection | relay | breaker-trip | output | and | the phases | R, S, T |                 |      |       |            |            |     |     |        |
| ---------- | ----- | ------------ | ------ | --- | ---------- | ------- | --------------- | ---- | ----- | ---------- | ---------- | --- | --- | ------ |
|            |       |              |        |     |            |         | line constants; | 5 to | 8 are | the source | constants. |     | The | source |
(i.e., A, B, C) and ground phase selection outputs from the impedances will change with conditions,
|     |     |     |     |     |     |     |     |     |     |     | system |     |     | so a |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ---- |
line protection or from the integral phase underimpedance representative value is selected. The inclusion of the
source
and ground overcurrent phase-selector units. The start impedances in the fault location algorithm is novel
a
input initiates adista-nce-to-fault computation. approach, which allows compensation for different
|     |     |     |     |     |     |     | impedance | angles in | thepower | system | network. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | -------- | ------ | -------- | --- | --- | --- |
Inputsinals from: The parameters set with the help of thumbwheels.
are
|     |     |     |     |     |     |     | A pushbutton | operation |     | initiates | EPROM |     | (electrically |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | --------- | ----- | --- | ------------- | --- |
an
|     |     |     |     |     |     |     | programmable | read-only |     | memory, | 22 Kbytes | used) | burn-in. |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | ------- | --------- | ----- | -------- | --- |
Line protection:
Measuring transformers: The digits of parameter No. 9 determine four different
|     |     |     |     |     |     |     | itemslisted | inTableII. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
Phase
|     |     | Currents | Voltages |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Start selection
|     |     |     |     |     |     |     | TABLEm: | SETTING& |     | PROGRAMMINGPARAMETERS |         |           |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --------------------- | ------- | --------- | --- | --- |
|     |     |     |     |     |     |     | 1. RlL  |          | 7.  | RlSB                  |         |           |     |     |
|     |     |     |     |     |     |     | 2. X1L  |          | 8.  | XlSB                  |         |           |     |     |
|     |     |     |     |     |     |     | 3. ROL  |          | 9.  | Type                  | ofphase | selection |     |     |
-
|     |     |     |     |     |     |     |     |     |     | (Normal, |     | cyclic, | acyclic) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | -------- | --- |
XOL
|     |     |     |     |     |     |     | 4.  |     |     | - CT | polarity |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- | --- | --- |
Printout(A,B,C)
-
|     |     |     |     |     |     |     | 5. RlSA |     |     | Linenumber |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ---------- | --- | --- | --- | --- |
-
6. XlSA
DESIGN
|     |     |     |     |     |     |     | Fig.      | 8 shows      | the fault | locator  | assembly |       | with  | phase  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --------- | -------- | -------- | ----- | ----- | ------ |
|     |     |     |     |     |     |     | selector  | and printer, | which     | is       | suitable | for   | 19"   | rack   |
|     |     |     |     |     |     |     | mounting. | The assembly |           | consists | of test  | unit, | power | supply |
u n i t ,
Fig. Hardware configuration. t r an s f o r me r u n it a n d m e a su r i n g s h un t un i t, w h i c h a r e
7 d i r e ct l y m o u n t e d t o a n d h e l d t o g e th e r b y t w o a p p a ra t u s
|     |     |     |     |     |     |     | bars. The     | remaining | plug-in  | units | are   | connected  |     | to a    |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | -------- | ----- | ----- | ---------- | --- | ------- |
|     |     |     |     |     |     |     | mother-board, | fed       | from the | shunt | unit. | The bottom |     | half of |
The 3-phase currents and voltages enter through input the assembly consists of the fault-type selection
transformers which provide galvanic isolation from the underimpedance and ground overcurrent units and the
| instrument | transformers, |        |              |                 |            |     | printer. |     |     |     |     |     |     |     |
| ---------- | ------------- | ------ | ------------ | --------------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
|            |               |        | as well      | as transforming | thesignals |     |          |     |     |     |     |     |     |     |
| to level   | suitable      | to the | electronics. | A screen        | between    | the |          |     |     |     |     |     |     |     |
a
| windings | minimizes | common-mode |     | surge | coupling. | The |     |        |        |                   |     |             |     |     |
| -------- | --------- | ----------- | --- | ----- | --------- | --- | --- | ------ | ------ | ----------------- | --- | ----------- | --- | --- |
|          |           |             |     |       |           |     | The | result | of the | distance-to-fault |     | calculation |     | is  |
analog signals feed through low-pass filter for signal shown the LED indicator. Fig. 9 shows example of
|     |     |     |     |     |     |     | on  |     |     |     |     | an  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
conditioning, using a 500 Hz cut-off frequency. The filter output results from the printer. The relative distance to
outputs
are switched in sequence by the multiplexer and fed fault is expressed in percentage of the line length. "Phase =
| into the | hold circuit | in  | preparation | for | conversion | to a |               |       |        |        |      |           |           |     |
| -------- | ------------ | --- | ----------- | --- | ---------- | ---- | ------------- | ----- | ------ | ------ | ---- | --------- | --------- | --- |
|          |              |     |             |     |            |      | RN" indicates | A and | ground | inputs | from | the phase | selectors |     |
digital value proportional to the instantaneous value of the (i.e., phase R to N fault). "LOOP RN" indicates
|     |     |     |     |     |     |     | a   |     |     |     | =   |     | that | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
ac wave. Both the digitized signals and the relay input computer processed phase A to ground voltage and phase A
status are stored in a 6-cycle circular file in the memory and residual currents to determine the fault location. The
| with the        | aid            | of       | the microprocessor |         |           |        |               |               |       |                 |        |           |     |       |
| --------------- | -------------- | -------- | ------------------ | ------- | --------- | ------ | ------------- | ------------- | ----- | --------------- | ------ | --------- | --- | ----- |
|                 |                |          |                    |         | (MC       | 6803   | computed      | r.m.s. values | of    | the fundamental |        | component |     | of ac |
| microprocessor, | 8              | bit, 814 | ns memory          | cycle). |           |        |               |               |       |                 |        |           |     |       |
|                 |                |          |                    |         |           |        | signals in    | polar form    | prior | to and          | during | the fault | are | also  |
|                 |                |          |                    |         |           |        | shown in Fig. | 9.            |       |                 |        |           |     |       |
| The             | microprocessor |          | processes          | the     | measuring | values |               |               |       |                 |        |           |     |       |
according to the fault location algorithm and presents the DESIGN TESTS
| distance | to fault | inpercentage | of  | the line | length on | the LED |     |     |     |     |     |     |     |     |
| -------- | -------- | ------------ | --- | -------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
indicator or remote connected equipment (printer, Model-line tests performed six fault locator
|     |     |     |     |     |     |     |     |     | were |     | on  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
telemeter, etc.). The microprocessor continuously executes units at the factory under dynamic conditions. A 100 km,
a monitoring routine. If the computer fails to periodically 170 kV line was modelled using CT's and PT's or a CCVT
output an "'all's well" signal, a peripheral circuit operates an modeL The line impedances referred to 380'V were: ZJL =
| alarm relay. | During |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
normal service, a pushbutton is used for 2.2 + j 17.0 and ZOL = 16.4 + j 68.0 ohms. The ohmic values

429
Line number 1
Relative distance to
fault p= 75%
Phase= RN, Loop= RN
IR = AMPL. = 002,213 A
ARG. = 028,4 DEG.
IS = AMPL. = 000,292 A
ARG. = 308,7 DEG
IT = AMPL. = 000,831 A
ARG. = 212,0 DEG
IRS = AMPL. = 000,519 A
ARG. = 103,1 DEG
IS0 = AMPL. = 000,514 A > Pre-fault
ARG. = 343,3 DEG.
ITO = AMPL. = 000,524 A
ARG. = 223,1 DEG.
Fig. 8 Fault locatorassembly with IN = AMPL. = 001,475 A
phaseselector and printer. ARG. = 015,1 DEG.
UR = AMPL. = 052,157 V
ARG. = 093,0 DEG.
stated below are also referred to 380 V, the primary of the US = AMPL. = 062,611 V
system simulator. Faults were applied with varying ARG. = 332,9 DEG.
incidence angles. Three series of tests were conducted. UT = AMPL. = 063,192 V
ARG. = 210,5 DEG.
Series No. 1 tests were run with zero fault resistance URO= AMPL. = 063,510 V
s a e f w e r n r e t r d o r t o m e i r r n s g a 5 r . t w u t e e n o d S r e 4 e w l r 0 i o i a t l e o d e h s h s m s c N 5 s u o 0 t r ; . r h % e a t 3 n n h t e t l , 2 e o e s a e % r t d x r s , o p c o r o w f h s r i e t t w t c e h e h k d e r e f e p d a l o u i l f w l n e o t e e s r s r s r e e t e r f t s h r t r i a o i o s n r n m t s g a 4 . r n s e % c t S s e a e u t r o l i v i f t o a e i n r s t n i h g A a e N ; t f o i r l . t o i o h n n m 2 e s e U U T SO O= = A A A A A R M R R M G P G G P . L . . L . . = = = = = 0 2 3 0 0 1 6 3 9 6 1 1 3 2 3 , , , , , 9 7 0 7 67 7 D D D 2 4 E E E V V G G G . . . Pre-fault
variations in source impedance from set values; errors were
less than 2 % of the line setting. Source A was varied from
2 a 1 to A 32 ra o te h d ms b , as B e. from 6 to 23 ohms. All ohmic values are on Fig. 9 Printer output
The locator was also run through the normal test
( s c f s e a o u r s n r t i t g e r e s o r ) l i a s t c e p e i p s r l t c t i s u e : e i s d t t s a ) t 4 s o a - i n 8 m d p u k r l t o V a h t t e e f i c a n I t s g E i t C ve t i 2 r n 5 a d r 5 n u e s - c l i 4 a t e y i n s 1 v t , e M t H i e i z n s n c , t t l e u p 2 r d e . r i 5 r u n p k g S t V i E o d N t n i 3 e s s s 6 t t 1 u . i 5 r n 0 b 3 an t c h ( e e a T P l 2) o e o c x w a a e t s r o A r P C w o o s a w . t s e ag r o i e n n d & st t a h f l L a e l i u e l g d d t h e t s a t c t e r C s i o N t b . o e r d w t a a h n s f w d a e u s c l T t o t e n x d l C a u o a s c c r a t r t - o e o l d N r l . e t j w o o n i A n M t s e l u f x y b a i u c b a l o y s t
shown in Fig. 10.
FIELD RESULTS
1) Two prototype units were installed for
c ev o a m l p u o a n t e io n n t i f n ai S lu w r e e d s is h h ave uti b l e it e i n es e . xpe N r o ie m n i c s e o d per O a n t e io o n f s th o e r N Ca W rrollton ( T L I ewisville) Highlands
prototypes was installed on the 30th ofJune 1982, on a 138kV
76 km, 130 kV transmission line between Nybro and
Vaxjo, on theSydkraft transmission system in southern
Sweden.
On July 2nd 1982 , adisturbance wasdetected on
the line between Nybro and Vaxjo. The fault locator
display showed 89 % (corresponding to 67.6 km). The
type of fault that was printed out was a single-phase Source: 34 aQ Source:
ground fault on phase T. An aerial inspection of the 0.48 aa 11.3 /82 6.9 Z9
transmission line was made on July 6th 1982 and the 1.4 /82 19.8 ZI.
point of disturbance was found inphase T atadistance
of 67.0 km from Nybro. The flashover occurred from
conductor to arcing horns, across a tower insulator Imp. in% on100 MVA base
string. The distance to fault, calculated by the fault
locator deviated from the actual distance to fault by
less than 1 %. Load current was 238A and the
calculated fault resistance was 7.2 ohms. The Fig. 10 Staged faults were applied atTI(Lewisville).
parameter settings matched those existing in the
network at the time of the fault
S fa w u e l d t is h T a h h s e S o t c o a c t t h u e e r r r P e o d p w r o e o n t r o t t t h y r a p a t e ns li m w n i a e s . s si i o n n st l a i l n l e e . d o H n ow a ev 4 e 0 r 0 , k n V o i N N n o o t r r e t t n h h t w w T i e e o h n s s e t t r t e o C C a a i e r s r s r r o t o l m i l l m u l t a t t o t u o n e n al - t - h c T e o I H u i p p ( g l e L h i e r l n w f a g i o n s r d v s o m i v l a l e n l e r c i ) n e e. 5 l 9 o in f I e t % t w h w i e a o t s f h fa t t t u h h h l e e e t

430
|     |         |            | line | without |     | compensation |     | for |     |     | (a) |     |     |     |
| --- | ------- | ---------- | ---- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | locator | on         | that |         | any |              |     | the |     |     |     |     |     |     |
|     | mutual  | impedance. |      |         |     |              |     |     |     |     |     |     |     |     |
ItuD
UA;E
|     |            | Five | faults, | two phase-to-phase |               |     | and three  | phase-     |     |     |     |     |     |     |
| --- | ---------- | ---- | ------- | ------------------ | ------------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
|     | to-ground  |      | faults  | were               | placed        | at  | the        | Lewisville |     |     |     |     |     |     |
|     | substation |      | during  |                    | early morning |     | of October | 25th       |     |     |     |     |     |     |
the
|     | 1983.      | The | faults | were | applied | at the    | TI  | (Lewisville) |     |     |     |     |     |     |
| --- | ---------- | --- | ------ | ---- | ------- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
|     | substation |     | where  | both | lines   | loop into | the | substation.  |     |     |     |     |     |     |
UF
|     | The  | actualdistance |     | to    | fault was | 55 % | of the    | line. The |     |     |     |     |     |     |
| --- | ---- | -------------- | --- | ----- | --------- | ---- | --------- | --------- | --- | --- | --- | --- | --- | --- |
|     | load | current        | was | about | 100A.     |      | Estimated | fault     |     |     |     |     |     |     |
for
|     | resistance |          | was 1.6  | ohms       | the | ground    | faults.        |          | l1FDlA' |     |     |     |     |     |
| --- | ---------- | -------- | -------- | ---------- | --- | --------- | -------------- | -------- | ------- | --- | --- | --- | --- | --- |
|     |            | The      | locator  | functioned |     | properly  | for            | all five |         |     |     |     |     |     |
|     | faults.    | The      | highest  | deviation  |     | of the    | results        | between  |         |     |     |     |     |     |
|     | the        | distance | to fault | shown      | on  | the fault | locatordisplay |          |         |     |     |     | (b) |     |
fault
|     | and | the actual | distance |     | to  | was | 3 %. |     |     |      |     |     |     |     |
| --- | --- | ---------- | -------- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |            |          |     |     |     |      |     |     | 12F- | IIF |     |     |     |
) .
|     |     |     | ACCURACY |     | ANALYSIS |     |     |     | 12FD1A |     |     |     |     |     |
| --- | --- | --- | -------- | --- | -------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
12FD1l
A
|         | Results | of           | overall     | accuracy | during  | dynamic |            | model-line   |     |      |     |     |     |     |
| ------- | ------- | ------------ | ----------- | -------- | ------- | ------- | ---------- | ------------ | --- | ---- | --- | --- | --- | --- |
|         |         | described    |             | DESIGN   |         | TESTS.  | This       | section will |     |      |     |     |     |     |
| tests   | are     |              | under       |          |         |         |            |              |     |      |     |     |     |     |
| discuss |         | the accuracy |             | of this  | locator | in      | comparison | with         |     |      |     |     |     |     |
| those   | using   | other        | approaches. |          |         |         |            |              |     | IOOF |     |     |     |     |
fault
|          | The |              | locator | described |              | above | computes | the      |     |     |     |     |     | IA  |
| -------- | --- | ------------ | ------- | --------- | ------------ | ----- | -------- | -------- | --- | --- | --- | --- | --- | --- |
| distance |     | to the fault | point   | by        | compensating |       | for the  | apparent |     |     |     |     |     |     |
[OFDOA
| reactance |            | in the | fault         | resistance | resulting |     | from load | current |     |     |     |     |     |     |
| --------- | ---------- | ------ | ------------- | ---------- | --------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
|           |            |        |               |            |           |     |           |         |     | ,,  |     | Y   |     |     |
| and       | variations | in     | the impedance |            | angles    | in  | the power | system  |     |     |     |     |     |     |
ILJD
| network. |          | However,      | minor | errors      | (see | Fig.     | 11) can   | occur if  |     |     |     |     |     |     |
| -------- | -------- | ------------- | ----- | ----------- | ---- | -------- | --------- | --------- | --- | --- | --- | --- | --- | --- |
| the      | settings |               |       |             |      | These    | errors    | should be |     |     |     |     |     |     |
|          |          | are           | not   | adequate.   |      |          |           |           |     |     |     |     |     |     |
| moderate |          | for practical |       | situations. |      | For one, | the value | of the    |     |     |     |     |     |     |
(c)
| fault        | locators    |           | increases      | with | line                    | length; |          | for these  |     |     |     |     |     |     |
| ------------ | ----------- | --------- | -------------- | ---- | ----------------------- | ------- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
| applications |             | the       | line impedance |      | tends                   | to      | mask the | effect of  |     |     |     |     |     |     |
|              |             | impedance | variations.    |      | Again                   | for     |          |            |     |     |     |     |     |     |
| source       |             |           |                |      |                         |         | longer   | lines, the |     |     |     |     |     |     |
| fault        | resistance, |           | particularly   |      | for single-phase-ground |         |          | faults,    |     |     |     |     |     |     |
IFRF
| becofnes |     | a smaller | percent | of  | the line | impedance. |     |     |     |     |     |     |     |     |
| -------- | --- | --------- | ------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
I
UA
|     |     |     | -   | I   | oo,) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
-I---
IFRF
'.rror
U
|     |     |       |     |     |     | i   |     |     |     |     |     | IA  |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | IAPZL |     | /   |     |     |     |     |     |     |     |     |     |     |
IA
iF
| Fig. | 11:Location |     | error    | resulting | froin | error | in  | comnpuating |                 |             |                          |     |     |            |
| ---- | ----------- | --- | -------- | --------- | ----- | ----- | --- | ----------- | --------------- | ----------- | ------------------------ | --- | --- | ---------- |
|      |             |     |          |           |       |       |     |             | Fig. 12: System | quantities  | for a single-line-ground |     |     | fault with |
|      | arguinent   |     | of iFRF. |           |       |       |     |             |                 |             |                          |     |     |            |
|      |             |     |          |           |       |       |     |             | load            | export from | station                  | A.  |     |            |
The next series of illustrations shows qualitatively the resistance. The total phase current at A is developed in Fig.
fault-resistance infeed effects on two alternative methods 12(b) and is the sum of the currents resulting from the fault
of determining fault location: the reactance and the zero- and driven by UF, and the pre-fault current ILD. Fig. 12(c)
|     |     |     |     |     |     |     |     |     |     | Figs. | 12(a) and | (b) | essentials | for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --- | ---------- | --- |
sequence current-reference techniques. Two examples are extracts from the
|        |     |         |              |     |         |         |     |     | developing | the diagrams | of Figs. | 13  | and 14. |     |
| ------ | --- | ------- | ------------ | --- | ------- | ------- | --- | --- | ---------- | ------------ | -------- | --- | ------- | --- |
| shown: |     | one for | load export; | the | second, | import. |     |     |            | error        |          |     |         |     |
Fig. 12(a) shows the station A line currents out of The reactance type of Fig. 13 uses the same basis of
phase with the total fault currentIF. Stating it another way, measurement as does the conventional reactance relay. The
source B produces out-of-phase infeeds in the fault angular shift of IFRF produces an error which can become

431
|     |     |     |     | IFRF-- | 1   |     |     |     |     | (a) |     |     | UF  |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
_-T
Error
LD)
V.5
.?
;<Iq
J,A
(b)
1FD1A
|     |     |     |     |     |     |     |     | IA  |     |     |     |     | I2FPD1A |      |        |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ------ |
|     |     |     |     |     |     |     |     |     |     |     |     |     |         | Y-IL | IOFDOA |
I2FD1A
| Fig. | 13: | Reactance-type |     | error | resulting | from | conditions | in  |     |     |     |     |     |     |     |
| ---- | --- | -------------- | --- | ----- | --------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 12.
ILD
|     |         |     |     |     | IFjRF |     | Error |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Fig. 13 | 1   |     |     |       | j   |       |     |     |     |     |     |     |     |     |
|     | Error   | _   |     |     | UA    |     |       |     |     |     |     |     |     |     |     |
IFRF
IA
UA
|     |      |     |                                      |     | 3IOFDOA         |     |         |     |     |     | 3IOFDOA |     |     |     |     |
| --- | ---- | --- | ------------------------------------ | --- | --------------- | --- | ------- | --- | --- | --- | ------- | --- | --- | --- | --- |
|     | Fig. | 14  | Zero-sequence-current-reference-type |     |                 |     |         |     |     |     |         |     |     |     |     |
|     |      |     | resulting                            |     | from conditions |     | in Fig. | 12. |     |     |         |     |     |     |     |
error
(c)
IA
| significant |           | for       | the fault   | location         | function |           | where         | greater  |     |     |     |     |     |     |     |
| ----------- | --------- | --------- | ----------- | ---------------- | -------- | --------- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| precision   |           | is needed | than        | for a protective |          | relay.    |               |          |     |     |     |     |     |     |     |
|             | The       | type      | shown       | in Fig. 14       | differs  | from      | the reactance |          |     |     |     |     |     |     |     |
| type        | in its    | use       | of residual | current,         | 31OFDOA  |           | = 3I0A        | as the   |     |     |     |     |     |     |     |
| reference   |           | rather    | than        | using 'IA.       | For the  | example   | of            | Fig. 12, |     |     |     |     |     |     |     |
| the         | two       | currents  | 3IOFDOA     | and              | IA are   | nearly    | in            | the same |     |     |     |     |     |     |     |
| phase       | position, |           | the         | in               | Fig. 14  | is almost |               | much     |     |     |     |     | IF  |     |     |
|             |           |           | so          | error            |          |           | as            | as       |     |     |     |     |     |     |     |
the Fig. 13
error.
In Fig. 15(a), Fig. 15: System quantities for single-phase-ground fault
|     |     |     | power | is being | imported |     | to Station | A so |     |     |     | a   |     |     |     |
| --- | --- | --- | ----- | -------- | -------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
ILD is about 1800 from its position in Fig. 12. The fault with load import into stationA.
| currents      |     | here are | identical | to      | those of | Fig. 12; | however, | the       |              |              |     |       |            |     |     |
| ------------- | --- | -------- | --------- | ------- | -------- | -------- | -------- | --------- | ------------ | ------------ | --- | ----- | ---------- | --- | --- |
| superposition |     |          | of load   | current | results  | in       | a        | different |              |              |     |       |            |     |     |
|               |     |          |           |         |          |          |          |           | then faulted | as specified | in  | rable | IV. Method | 1   | has |
magnitude and angle for IA. Compare 16 and 17: the latter zero
|     |     |          |       |         |     |               |     |          | error | because the source |     | impedance | values | were | input, |
| --- | --- | -------- | ----- | ------- | --- | ------------- | --- | -------- | ----- | ------------------ | --- | --------- | ------ | ---- | ------ |
| now | has | a larger | error | because |     | its reference |     | current, |       |                    |     |           |        |      |        |
3IOFDOA, leads theIA position. describing the complete system. Method 4 showssubstantial
|     |     |      |              |        |     |     |                 |     | errors, | although smaller | thanboth  | methods |     | 2 and3. |     |
| --- | --- | ---- | ------------ | ------ | --- | --- | --------------- | --- | ------- | ---------------- | --------- | ------- | --- | ------- | --- |
|     | The | load | compensation | method |     | [1) | will experience |     |         |                  |           |         |     |         |     |
|     |     |      |              |        |     |     |                 |     |         | 3 in Table       | IV yields | greater |     | than    |     |
errors generally less than those shown in Figs. 14 and 17, Case errors cases 1
depending and 2 because the zero-sequence line impedance argument
|     |     | upon | the amount | of  | out-of-phase |     | infeed | into the |     |     |     |     |     |     |     |
| --- | --- | ---- | ---------- | --- | ------------ | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
fault from the far end. This be in the following of 76.7 degrees is lower with respect to the zero-sequence
|     |     |     |     |     | can | seen |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
numerical examples. source impedance argument. The corresponding angle for
|             |       |          |       |              |     |        |           |        | cases    | 1 and 2 is 81.7 | degrees. | Thus, | the zero-sequence |         | out-    |
| ----------- | ----- | -------- | ----- | ------------ | --- | ------ | --------- | ------ | -------- | --------------- | -------- | ----- | ----------------- | ------- | ------- |
|             |       |          |       |              |     |        |           |        | of-phase | infeed is much  | greater  | in    | 3,                | causing | greater |
| Single-Line |       | Examples |       |              |     |        |           |        |          |                 |          |       | case              |         |         |
|             |       |          |       |              |     |        |           |        | errors   | for methods2,   | 3 and4.  |       |                   |         |         |
|             | Table | IV       | shows | the location |     | errors | for three | cases, |          |                 |          |       |                   |         |         |
comparing four computational methods, using an off-line With smaller fault resistances the errors in Table IV
computer simulatation. Table V defines the power system will be correspondingly smaller. On the other hand, lower
| conditions |     |     |     |     |     |     |     |     | voltage | lines |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- |
for two different transmission lines. These were with lower arguments will produce larger

432
Error
- -- Eror
UA
-..;0Fig.
uAUA 16
Error
Fig. 16: Reactance-type error resulting from conditiorns in FiY. 1.7 Zero-sequence-current-reference-type
Fig. 15. error resulting from conditions in Fig. 15.
TABLE IV COMPARISON OF FAULT LOCATOR ERRORS FOR THE APPLICATIONS IN TABLE V
CALCULATED RESULTS
Power Fault Fault RF Method 1 Method 2 Method 3 Method4
Case System Locator Point Ohms p Error p Error p Error p Error
At:
1 Ashe-Marion Ashe 0.9 50 0.9 0 0.87 -3.1 0.62 -28.4 0.88 -1.9
2 Ashe-Marion Ashe 0.9 100 0.9 0 0.86 -4.5 0.54 -36.7 0.87 -2.7
3 Stenkullen- Sten- 0.8 125 0.8 0 0.72 -7.9 0.39 -41.0 0.76 -4.2
Borgvik
kullen
Method 1 As described in this paper.
Method 2 Zero-sequence-current-reference type(see Fig. 14)
KN as defined in the Glossary
Method3 Reactance type(see Fig. 13)
KN as defined in the Glossary.
Method4 Load compensated 1].
Errors are in percentage of total length of line.
errors where the remote source argument is higher, such as 0.1-20 times rated; voltage, 0.01-1.5 rated. It is available
would be the case near agenerating station. with 1, 2 and 5 A ratings, withstanding 3 times rated current
continuously.
Parallel-Line Examples
It is designed for use with the relaying instrument
Table VI shows computer-simulation results for two transformers and introduces a burden of 1 VA per phase at
parallel-line cases. In both instances the parallel line is rated voltage or current.
identical to its companion listed in Table V. The errors in
Table VI for method 1 would occur if parallel-line The unit is designed and tested just as if it were a
compensation were not included. With both the positive - protective relay.
and zero-sequence effects included in the- algorithms, the
computed errors were zero. The uncompensated errors for Operating temperature range is0 to 550 C.
the Lieto-Forsa application are greaterbecause of the lower
line arguments compared to the Ashe-Marion lines. The It requires 1.5 cycles of fault dturation for an accurate
parallel-line effect uipon accuracy will be the greatest for measurement.
far-end faults, because these produce . the maximum
parallel-line current. It is not necessary to apply one locator at each line
terminal. Four units can share one optionalprinter.
APPLICATION CONSIDERATIONS The distance to the fault can be remotely logged using
the built-in telemetering outputs from the locator.
The unit is suitable for use with lines or sources with
secondary impedances in the range of 0-1000 ohms based on
a A CT (0-200 ohms for 5 A CT's). Signal current range is

433
TABLE V SYSTEM DESCRIPTIONS FOR TABLE VI FAULT LOCATOR ERRORS (METHOD 1)
EXAMPLES IN TABLES IV ANDVI F-OR PARALLEL LINE APPLICATIONS
WITHOUT COMPENSATION
Ashe- Stenkullen- Lieto-
Marion Borgvik Forsa Fault locator installed at Ashe and Lieto.
(USA) (SWEDEN) (FINLAND)
Fault R - Ashe Lieto
Location O§ms Marion Forsa
Voltage -kV 525 400 110
Z1SA a m r a g g . . 17. 9 6 0 21. 9 3 0 5. 8 8 5 ZOM mag - - 332.1 75.8
ZOSA 'nag. 6.2 24.4 70 arg. - - 73.6 73.5
ZlSB a m r a g g . . 42. 90 2 25. 9 6 0 8 1 5 5 ILD mag - - 1165 240
JB arg. 90 90 85 arg. _ - -37.8 4.3
ZOSB 'mag. 29.5 27.8 130
arg. 90 -90 80
ZiL mag. 118.5 53.5 27.6 PercentError:
arg. 87.0 86.4 73.7
0.3 50 0.1
ZOL mag. 463.0 247.6 108.7 0.3 100 0.1
arg. 81.7 76.7 74.3
0.4 4.3 0.4
UAE mag. 320.4 225.2 63.5
0.4 20 0.4
arg. -17.0 O 0
0.8 50 3.2
UBE mag. 334.9 240.2 63.5
0.8 100 2.9
arg. -67.0 -29.4 -15
0.8 4.3 15.8
ILD mag. 1555 1184
arg. -37.0 -5.7
Impedances in ohms REFERENCES
Voltages inkV
Currents in A 1) T. Takagi, Y. Yamakoshi. M. Yamaura, R.
Arguments in degrees Kondow, T. Matsushima: "Development of a new
type fault locator using the one-terminalvoltage
and current datat", IEEE Trans., VOL. PAS-101,
No. 8, August 1982, pp 2892-2898.
SUMMARY 2) M. Souillard, Ph. Sarquiz, L. Mouton:
"Development of measurement principles and of
1 The fault locator displays the percent the technology of protection systems and fault
distance to the fault, using novel compensation location systems for three-phase transmission
techniques for the errors resulting from remote- lines", CIGRE No. 34-02, August 1974.
end source infeed into the fault resistance. This
is accomplished by using a.complete network
modeL.
GLOSSARY OF SYMBOLS
2 Compensation for fault-resistance voltage
drop utilizes prefault current and representative aD angle of fault resistance drop, IFRF, with reference
to UA
values for source resistance and reactance. The
inclusion of source impedances is a novel
aE angle between generated voltages UAE and UBE
approach which provides improved accurancy.
3 The microprocessor-based system is aF angle of total fault current, with reference to UF
designed and built to protective-relaying
standards, including all surge withstand aL argument of line impedance
requirements.
aR angular error in computing IFRF
4 It is suitable for use with the relaying
DA general expression for current distribution factor at
instrument transformers, introducing negligible
station A.
burden.
DiA, D2A, DOA
5 Extensive software filtering minimizes the positive-, negative- and zero-sequence current
effects of power-system and instrument- distribution factor in line at station A
transformer transients.
IA, IB line current on faulted phase(s) at station A and B,
6 The microprocessor monitors itself and respectively. General, i.e. not referring to a
built-in functional-test facilities can pinpoint a specific symmetrical component sequence
particular chip or analog-system failure.
11A totalpositive-sequence current in line at station A.
7 The locator can function either with the
line-relay phase selectors or with the optional AIIAA11B
built-in relay units. positive-sequence current change as a result of
fault, in line at station A andB, respectively
8 Only one end of the line needs to be
equipped. IF total fault current

434
IFA change in line current at station A, as a result of ZOSA, s Z e O qu S e B nce source impedance at station A zer a o n - d B,
fault. General - see Table I for specific definition
respectively
depending upon fault type
ZlL, ZOL positive-
IlF, I2FY IOF
and zero-sequence line impedance
positive-, negative- and zero-sequence currents in
fault
ZSA, ZSB source
impedance behind station A and B, respectively.
ILD load current in line General, i.e. not referring to a specific
symmetricalcomponent sequence
INA residualcurrent(3 IOA) in the line at station A
ZL total line impedance. General, ie. not referring
'OA zero-sequence line current atstationA toa specific symmetricalcomponent sequence
ZOM
IRA, ISA, ITA mutual impedance of line for the zero-sequence
current in line at station A, phases R, S and T, network
respectively
APPENDIX
AIRA, etc.-total current minus pre-fault current, in
the line atstationA, phase R Apparent Impedance for Three Phase Fault
KN Z3L ZlL The apparent impedance seen by a conventional
reactance relay or fault locator will be derivei for a 3-
phase fault, including load current effects.
N ground, whenreferring to fault type
Load current flow in the line will be developed by
p proportion of the total line from station A (fault phase angle'aE between two sources, per Fig. 2. Shunt
locator location) to the fault capacitances'and reactances willbe neglected.
R, S, Tpower system phases(alternative: The derivation willuse the superposition principle with
A,B,C) Thevenin's theorem, where the total voltage and current at
any point in the network Is the sum of the prefault values
RlL, ROL positive-and zero-sequence line plus those produced by short circuiting the voltage sources
resistances and inserting UF, the open-circuit voltage at the fault point,
as shown 'in Fig. 3. The polarity of' UF in the equivalent
RlSA, RlSB positive-sequence source resist- circuit of Fig. 3 is such as to cancel the pre-fault voltage
anceatstationA andB, respectively except for the fault resistance drop. For the 3-phase fault
case, the negative- and zero-sequence voltage drops are
RF fault resistance zero.
UA, UB voltageon faultedphase(s) at station The positive direction of the load current ILD is
A and B, respectively. General, i.e. not arbitrarily chosen asshown in Fig. 2.-
referring to a specific symmetrical component
The positive-sequence prefault voltage at stationA is:
UAE, UBE sourcevoltagebehind equivalent (UIA) L = UAE -ILD ZiSA
impedance at stationA andB, respectively
- UF + ILD pZlL (Al)
UlA actualpositive-sequence voltage at stationA
(U1A)F
The positive-sequence change in voltage atA
positive-sequence change in voltage at station A produced by the fault is:
resulting from fault
(UlA) F = - DiA IlF ZJSA
(UlA)L, (U1B)L
p t o io s n it A iv a e n - d se B q , ue r n e c s e pec v t o i l v t e a l g y e prior to fault at sta- = DIA 11F PZlL + '1F RF - UF (A2)
UF voltage at faultpointprior to fault The actualvoltage at A is:
URA, USA, UTA UJA = (UJA) L + (UlA) F
voltage to ground at station A, phases R, S and
T, respectively = UF + ILD P ZJL + DlA I'F PZlL
+ IlF RF - UF
XlL, XOL
positive-and zero-sequence line reactance
ILD PZiL+ (DiA PZiL + RF) IlF
(A3)
XlSA, XtSJ3
positive-sequence source reactance at station A
andB, respectively The actualcurrent in the line at A is:
ZA apparent impedance on the line atstationA IJA = ILD + AIJA
ZJSA, ZlSB positive-sequence source impedance = ILD+ DlA IJF (A4)
at station A andB, respectively

435
| From | (A3) | and (A4): |     |     |     |     |     |     |     |     |         |     |     |
| ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
|      |      |           |     |     |     |     |     |     | jXA |     | UIAA ZA |     |     |
= RA + jXA
|     | ZA = | UlA/IlA |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
B
|     |     |            |              | IlF)      | 11F  |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | ------------ | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | P ZlL (ILD | + DlA        |           | + RF |     |     |     |     |     |     |     |     |
|     |     |            | ILD          | + DiA IlF |      |     |     |     |     |     |     |     |     |
|     | =   | P ZlL +    | RF ( ILIIF)A |           |      |     |     |     |     |     |     |     |     |
l
|     |     |     |     | RF  |     |     |     |     |     |     | =LDO |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
=PZlL+
|     |     |     | DlA |     |     |     |      |     |     |     | _%.. Increasing |     | RF  |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --------------- | --- | --- |
|     |     |     | +   | ~fl |     |     | (A5) |     |     |     |                 |     |     |
IJF
ILDVO
| From | Fig. | 3:  |     |     |     |     |     |     |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
UF
|       | IJF | RF +   | DiA (P | ZlL + ZiSA) |     |     |      |     |     |      |     |     |     |
| ----- | --- | ------ | ------ | ----------- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
|       |     |        |        |             |     |     | (A6) |     |     | pZlL |     |     |     |
|       |     | (1     | P) ZlL | + ZlSB      |     |     |      |     |     |      |     | RA  |     |
| where | DlA | = ZlSA | + ZlL  | + ZlSB      |     |     |      |     |     |      |     |     |     |
(A?)
A
| Eq. | (A6) in(A5): |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RF
|     | ZA = PZlL | +   |     |          |     |       |       |      |                 |            |     |     |     |
| --- | --------- | --- | --- | -------- | --- | ----- | ----- | ---- | --------------- | ---------- | --- | --- | --- |
|     |           |     |     |          |     |       |       | Fig. | Al: Appai-kriit | i,npedaiee | ZA. |     |     |
|     |           |     | DlA |          | DlA | (PZlL | ZlSA) |      |                 |            |     |     |     |
|     |           |     |     | + ILD RF | +   |       | +     |      |                 |            |     |     |     |
UF
|     |     |     |     |     |     |     | (A8) |     |     |     |     | ,pparent |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | -------- | --- |
eactance
rop
|           | Eq. (A8) | is           | a quadratic | in     | p, the          | unknown | fault      |     |     |     |     |     |     |
| --------- | -------- | ------------ | ----------- | ------ | --------------- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
| location. | RF       | is also      | unknown.    |        |                 |         |            |     | N   |     |     |     |     |
|           | Note     | that the     | argument    | for    | the RF term     | is      | influenced |     |     |     |     |     |     |
| byboth    | the      | load current | angle       | andby  | the impedances. |         |            |     |     |     |     |     |     |
|           | For      | long line    | and         | fault  |                 |         |            |     |     |     |     |     |     |
|           | a        |              |             | a near | station         | B, DlA  | in Eq.     |     |     |     |     |     |     |
(A?) approaches:
'lA
ZiSB
Di = --
|     | Assuming | that     | ZlSB      |              |          |     |           |          |         |         |                    |        |          |
| --- | -------- | -------- | --------- | ------------ | -------- | --- | --------- | -------- | ------- | ------- | ------------------ | ------ | -------- |
|     |          |          |           | has a larger | argument |     | than ZlL, |          |         |         |                    |        |          |
| DlA | willhave | positive | argument. |              |          |     |           |          |         |         |                    |        |          |
|     |          |          |           |              |          |     |           | Fig. A2: | Phasers | showing | apparent reactance | effect | in fault |
point
potentiaL
|     | Neglecting | loadcurrent, |     | Eq. | (A8) reduces | to: |     |     |     |     |     |     |     |
| --- | ---------- | ------------ | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
RF
|     | ZA  | = P | ZJL+ | DA  |     |     |     |        |           |            |             |       |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | ------ | --------- | ---------- | ----------- | ----- | --- |
|     |     |     |      |     |     |     |     | import | condition | at station | A (UAE lags | UBE), |     |
the error
willbe positive.
|         | This is                | plotted | in Fig.  |         |          |                 |         |     |     |     |     |     |     |
| ------- | ---------------------- | ------- | -------- | ------- | -------- | --------------- | ------- | --- | --- | --- | --- | --- | --- |
|         |                        |         |          | Al with | the      | locus for       | varying |     |     |     |     |     |     |
| RF; the | curve                  | with    | the load | effect  |          |                 |         |     |     |     |     |     |     |
|         |                        |         |          |         | included | is alsoplotted. |         |     |     |     |     |     |     |
|         | The apparent-reactance |         |          | effect  | can      | also be         | seen on |     |     |     |     |     |     |
a
| phasor | diagram | such | as  | Fig. A2, | with the | current | plotted |     |     |     |     |     |     |
| ------ | ------- | ---- | --- | -------- | -------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
horizontally
as the reference.
|     | Fig. A2 | canbe          | derived  | by rearranging |            | Eq.(A3): |       |     |     |     |     |     |     |
| --- | ------- | -------------- | -------- | -------------- | ---------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
|     |         | UiA = P        | ZIL (ILD | + DA           | IlF) + IlF | RF       |       |     |     |     |     |     |     |
|     |         | (11A)          | IlF      |                |            |          |       |     |     |     |     |     |     |
|     | =       | P ZiL          | +        | RF             |            | (A9)     |       |     |     |     |     |     |     |
|     | where   | 11A actual     | line     |                |            |          |       |     |     |     |     |     |     |
|     |         | =              |          | current        | at station | A.       |       |     |     |     |     |     |     |
|     | Thus,   | a conventional |          | reactance      | distance   |          | relay |     |     |     |     |     |     |
or
| fault       | locator  | using               | the same | principle    | is         | subject | to an  |     |     |     |     |     |     |
| ----------- | -------- | ------------------- | -------- | ------------ | ---------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
| error       | because  | of                  | fault    | resistance,  | load       | current | and    |     |     |     |     |     |     |
| differences |          | in system-impedance |          |              |            |         |        |     |     |     |     |     |     |
|             |          |                     |          |              | arguments. | The     | error  |     |     |     |     |     |     |
| shown       | in Figs. | Al                  | and      | A2 negative; | however,   |         |        |     |     |     |     |     |     |
|             |          |                     |          | is           |            |         | for an |     |     |     |     |     |     |

436
Discussion A computer simulation on a400 kV, 150 km linewith a shunt load
|                                               |     |     |     |     |     |                  |     | appliedatStationAoftheproportionsstatedbyMr. |                |     |     |     | Crockettproduc- |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ---------------- | --- | -------------------------------------------- | -------------- | --- | --- | --- | --------------- | --- | --- |
| J.M.Crockett(WestinghouseCanadaInc.,Hamilton, |     |     |     |     |     | Ontario,Canada): |     |                                              |                |     |     |     |                 |     |     |
|                                               |     |     |     |     |     |                  |     | ed                                           | these results: |     |     |     |                 |     |     |
Theauthorshaveoutlinedaninterestingconceptinfaultlocatordesign
| but some | additional | information |     | would be | useful. |     |     |     |     |     |     |     |     |     |     |
| -------- | ---------- | ----------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Source
ThederivationoftheequivalentsourceimpedancesZ1SAandZ1SN
|                   |     |           |         |         |                |     |        |      | Fault |     | Rf   | Impedange |       |     | Error |
| ----------------- | --- | --------- | ------- | ------- | -------------- | --- | ------ | ---- | ----- | --- | ---- | --------- | ----- | --- | ----- |
| could bedescribed |     | ingreater | detail. | Itwould | appearthatthey |     | arenot |      |       |     |      |           |       |     |       |
|                   |     |           |         |         |                |     |        | Case | Point |     | Ohms | Scalar    | Angle |     | wo    |
actualsourceimpedancesbutbasedonasystemreductiontoatwoline
|     |     |     |     |     |     |     |     | 1   | 0.5 |     | 20  | 23  | 90  |     | 1-  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
machineequivalentandthenthedeltastarconversionoftheequivalent 2 0.5 20 22.9 85.2 0
| parallel line                                | and                                                  | source impedances. |     | Ifthe resulting |                        | mutual | branch | is  |     |     |     |      |      |     |     |
| -------------------------------------------- | ---------------------------------------------------- | ------------------ | --- | --------------- | ---------------------- | ------ | ------ | --- | --- | --- | --- | ---- | ---- | --- | --- |
|                                              |                                                      |                    |     |                 |                        |        |        | 3   | 0.5 |     | 100 | 23   | 90   |     | 3   |
| eliminated,                                  | positivesequencesourceimpedancesresultwhichyieldcor- |                    |     |                 |                        |        |        |     |     |     |     |      |      |     |     |
|                                              |                                                      |                    |     |                 |                        |        |        | 4   | 0.5 |     | 100 | 22.9 | 85.2 |     | 0   |
| rectdistributionfactorsforallfaultlocations. |                                                      |                    |     |                 | Isthistheapproachused? |        |        |     |     |     |     |      |      |     |     |
|                                              |                                                      |                    |     |                 |                        |        |        | 5   | 0.8 |     | 100 | 23   | 90   |     | 4   |
Itisnotexactinthezerosequencenetworkifmutualcouplingisinvolved.
|     |     |     |     |     |     |     |     | 6   | 0.8 |     | 100 | 22.9 | 85.2 |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- |
Thepositivesequenceequivalentisnotpreciselyrigorousifshuntloads
| atthelineterminalsareignoredorvariable, |               |          |     | andthedegreeofprecision |           |      |        |                                                       |            |                    |     |       |                  |     |        |
| --------------------------------------- | ------------- | -------- | --- | ----------------------- | --------- | ---- | ------ | ----------------------------------------------------- | ---------- | ------------------ | --- | ----- | ---------------- | --- | ------ |
|                                         |               |          |     |                         |           |      |        | All                                                   | six faults | werephasetoground. |     | Cases | 2, 4and6havezero |     | error, |
| as regards                              | fault locator | accuracy |     | may be very             | important | even | though |                                                       |            |                    |     |       |                  |     |        |
|                                         |               |          |     |                         |           |      |        | becausetheloadimpedancehasbeenrigorouslyaccommodated. |            |                    |     |       |                  |     | Cases  |
theresultingsourceimpedanceargumentvariationislessthan3degrees.
3and5representextremeconditions,with100ohmsoffaultresistance,
| As anexample |     | oferrors, | consider | sourceto | line | impedance | ratio in |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | -------- | -------- | ---- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
theorderof0.5,shuntloadsintheorderof12ormoretimesthesource particularly case 5 where the fault is near the far end. By choosing a
representativevaluefortheloadimpedancesvariationsinthisvaluewill
| impedance, | asubstantialphaseshiftbetween |     |     |     | sources, | ahighresistance |     |      |           |               |     |     |     |     |     |
| ---------- | ----------------------------- | --- | --- | --- | -------- | --------------- | --- | ---- | --------- | ------------- | --- | --- | --- | --- | --- |
|            |                               |     |     |     |          |                 |     | have | a limited | error effect. |     |     |     |     |     |
faulttogroundsuchasatree,andafaultlocatoratthepowerreceiving
|                                              |           |                |        |            |                   |       |          |     | The parameters | for this | example   | are:       |     |     |     |
| -------------------------------------------- | --------- | -------------- | ------ | ---------- | ----------------- | ----- | -------- | --- | -------------- | -------- | --------- | ---------- | --- | --- | --- |
| line terminal.                               | I believe | substantial    |        | changes in | measured          | fault | location |     |                |          |           |            |     |     |     |
|                                              |           |                |        |            |                   |       |          |     |                |          | magnitude | angle-deg. |     |     |     |
| wouldbeobservedastheshuntload,faultlocation, |           |                |        |            | andfaultimpedance |       |          |     |                |          |           |            |     |     |     |
| Would                                        |           |                |        |            |                   |       |          |     | ZISA           |          |           | 23         |     |     | 90  |
| vary.                                        | the       | authors        | agree? |            |                   |       |          |     | ZOSA           |          |           | 23         |     |     | 90  |
| Theabilitytolocate                           |           | ahighimpedance |        | faultto    | foliagewould      |       | indeed   |     |                |          |           |            |     |     |     |
|                                              |           |                |        |            |                   |       |          |     | ZSH            |          |           | 276        |     |     | 0   |
| beusefulbuthasthiscapabilitybeendemonstated? |           |                |        |            | Slowrelayingwould |       |          |     |                |          |           |            |     |     |     |
|                                              |           |                |        |            |                   |       |          |     | ZISB           |          |           | 20         |     |     | 90  |
beexpectedforsuchafaultandhenceapparentcurrentandvoltagedevia-
|             |         |      |          |              |     |     |     |     | ZOSB |     |     | 40   |     |     | 90   |
| ----------- | ------- | ---- | -------- | ------------ | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | ---- |
| tions could | be zero | when | the line | was tripped. |     |     |     |     |      |     |     |      |     |     |      |
|             |         |      |          |              |     |     |     |     | ZIL  |     |     | 46.5 |     |     | 84.4 |
Finally,Ibelievethatthepower-sendingterminalisthepreferredfault ZOL 156.7 77.5
| locator position. |          | Would    | the authors | agree?             |     |             |       |     |     |     |     |       |     |     |       |
| ----------------- | -------- | -------- | ----------- | ------------------ | --- | ----------- | ----- | --- | --- | --- | --- | ----- | --- | --- | ----- |
|                   |          |          |             |                    |     |             |       |     | UAE |     |     | 230.9 |     |     | 0     |
|                   |          |          |             |                    |     |             |       |     | ZBE |     |     | 230.9 |     |     | -38.5 |
| Manuscript        | received | August   | 2, 1984.    |                    |     |             |       |     |     |     |     |       |     |     |       |
|                   |          |          |             |                    |     |             |       |     | ILD |     |     | 2312  |     |     | -14.3 |
|                   |          |          |             |                    |     |             |       |     | ZSp |     |     | 22.9  |     |     | 85.2  |
| L. Eriksson,      | M.       | M. Saha, | and         | G. D. Rockefeller: |     | The authors | thank |     |     |     |     |       |     |     |       |
Impedancesareinohms,voltagesinkV,currentsinamperesandangles
Mr. Crockettforhisinterestinthispaperandforhisrelevantcomments
|                |     |            |     |               |      |      |        | indegrees. | ZSFisthepositive-sequenceequivalentoftheparalleledsource |     |     |     |     |     |     |
| -------------- | --- | ---------- | --- | ------------- | ---- | ---- | ------ | ---------- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| and questions. | His | discussion | can | be segregated | into | four | areas: |            |                                                          |     |     |     |     |     |     |
ZSAandloadimpedanceZSH.Notethattheeffectoftheloadimpedance
1. derivationofthecurrentdistributionfactorfortheparallellinecase
atStationAistoshifttheactualsourceanglefrom90deg.to85.2deg.
2. effect of shunt loads for the paralleled equivalent ofthe and load impedances. The
3. availabilityofprefaultcurrentinformation forahigh-impedance source
|     |     |     |     |     |     |     |     | load | has a negligible | effect | on  | the magnitude | ofthis equivalent. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------------- | ------ | --- | ------------- | ------------------ | --- | --- |
fault
3.Ifthenormalhigh-speedprotecitonfailstodetectahigh-resistance
| 4. preferred | spot | for the | locator. |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | ---- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fault,suchasamid-spanflashovertofoliage,twopossibilitiesexistfor
| These | item numbers | will         | be used | below. |     |     |             |     |          |     |     |     |     |     |     |
| ----- | ------------ | ------------ | ------- | ------ | --- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
|       |              | distribution | factor  | stated | in  |     | is rigorous | the | locator: |     |     |     |     |     |     |
1. The current as Eq. 13A a) Thefault-locatorterminalopensfollowingtheremoteterminal.
| assuminganidenticalparallelline. |     |     |     | Itisindependentofanyzero-sequence |     |     |     |        |       |                |                      |     |       |            |     |
| -------------------------------- | --- | --- | --- | --------------------------------- | --- | --- | --- | ------ | ----- | -------------- | -------------------- | --- | ----- | ---------- | --- |
|                                  |     |     |     |                                   |     |     |     | Inthis | case, | thereis noload | currentflowduringthe |     | fault | periodused |     |
effect,includingmutualimpedance,becauseonlythepositive-sequence
bythelocatortocompute.Thus,noerroroccursbecauseofloadcurrent.
| factor is | needed | to derive | the total | fault current | If. |     |     |     |     |     |     |     |     |     |     |
| --------- | ------ | --------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
b) Thefault-locatorterminalopensfirst.Theprefaultdataarenot
Measuredvoltage willcontain anymutualinductionfrom aparallel protectiontrip delayed.
line-thiscanbecompensatedforbyinputtingthezero-sequencemutual available in memoryiftheline is This
|     |     |     |     |     |     |     |     |     | situation | will berecognized |     | bytheprogram | and | an alternative |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------- | --- | ------------ | --- | -------------- | --- |
impedancetothelocatorandprovidingtheprogramwiththemeasured
|               |               |     |                      |     |       |         |      |     | "slowtrip" | routine | is         | processed. | Errors will occur | because | of  |
| ------------- | ------------- | --- | -------------------- | --- | ----- | ------- | ---- | --- | ---------- | ------- | ---------- | ---------- | ----------------- | ------- | --- |
| parallel-line | zero-sequence |     | currentviatheprinter |     | loop, | fromthe | com- |     |            |         |            |            |                   |         |     |
|               |               |     |                      |     |       |         |      |     | the load   | current | component. |            |                   |         |     |
panion locator.
4.Thedirectionofpowerflowisnotofconcerntothefaultlocator,
TheEq. 13Aexpressionisderivedusingadelta-starconversion,where Thatis,thereisnobias
the impedances merged into the equivalent impedances. sinceitsalgorithmeliminatesloadfloweffects.
source are towards installing the locator at the "power sendingterminal" unless
| However,       | theactualsourceimpedances |      |        | areinputjust         |     | as forthesingle |     |                                       |         |        |                  |     |                            |      |      |
| -------------- | ------------------------- | ---- | ------ | -------------------- | --- | --------------- | --- | ------------------------------------- | ------- | ------ | ---------------- | --- | -------------------------- | ---- | ---- |
|                |                           |      |        |                      |     |                 |     | thisdescribesthestrongersourceoffault |         |        |                  |     | current. Thestrongersource |      |      |
| line algorithm | which                     | uses | Eq. 13 | for the distribution |     | factor.         |     |                                       |         |        |                  |     |                            |      |      |
|                |                           |      |        |                      |     |                 |     | installation                          | reduces | errors | becausetheweaker |     | end produces               | less | ofan |
2. Shuntimpedanceeffectsatthetwoendsofthelinecanberigously
|     |     |     |     |     |     |     |     | infeed | effect. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- |
canceledbyincludingtheseimpedancesinthesourceimpedances. This following results Sixphase-
is the for either the single line or the parallel linealgorithm. The 5. The additional field are noteworthy.
case groundfaultsoccurredduringveryhighwindsona400kV, 135kmline.
| loadandsourceimpedances |     |     | aremerelyparalleled. |     | Mr. | Crockettiscor- |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | -------------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thepreciselocationofthesetemporaryfaultsisnotknown.Thelocator
| rectthatchanges                                             |            | inthese, | coupled | with faultresistance, |            | willintroduce |         |          |     |            |            |              |          |       |     |
| ----------------------------------------------------------- | ---------- | -------- | ------- | --------------------- | ---------- | ------------- | ------- | -------- | --- | ---------- | ---------- | ------------ | -------- | ----- | --- |
|                                                             |            |          |         |                       |            |               |         | operated | in  | each case, | indicating | in the range | of 93 to | 990/. |     |
| errors. Themagnitudeoftheloadimpedancewillhavelittleeffect, |            |          |         |                       |            |               | but     |          |     |            |            |              |          |       |     |
| its angular                                                 | difference | compared |         | to the other          | impedances | will          | have an |          |     |            |            |              |          |       |     |
effectastheimpedancevariesfromthenominalvalueusedtodetermine Manuscript received September 4, 1984.
thesourceimpedanceinput.Thefollowingexampleillustratesthiseffect.