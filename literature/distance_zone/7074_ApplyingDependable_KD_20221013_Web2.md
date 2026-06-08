Applying Dependable and Secure Protection
With Quadrilateral Distance Elements
Kanchanrao Dase, Armando Guzmán, Steven Chase, and Brian Smyth
Schweitzer Engineering Laboratories, Inc.
Presented at the
77th Annual Conference for Protective Relay Engineers at Texas A&M
College Station, Texas
March 26–28, 2024
Original release October 2022

1
Applying Dependable and Secure Protection With
Quadrilateral Distance Elements
Kanchanrao Dase, Armando Guzmán, Steven Chase, and Brian Smyth, Schweitzer Engineering Laboratories, Inc.
|              | Abstract—This  |     | paper  analyzes     | factors    |     | affecting  | the  |     |     |     |
| ------------ | -------------- | --- | ------------------- | ---------- | --- | ---------- | ---- | --- | --- | --- |
| performance  |                | of  | current  polarized  | reactance  |     | elements   | and  |     |     |     |
provides guidelines to ensure the security of Zone 1 quadrilateral
| distance  |     | elements.  | Network  | nonhomogeneity,  |     | instrument  |     |     |     |     |
| --------- | --- | ---------- | -------- | ---------------- | --- | ----------- | --- | --- | --- | --- |
transformer errors, line charging currents, line transpositions,
| zero-sequence  |     | mutual  | coupling,  | and  | unbalanced  | operating  |     |     |     |     |
| -------------- | --- | ------- | ---------- | ---- | ----------- | ---------- | --- | --- | --- | --- |
conditions affect the performance of current polarized reactance
elements. This paper evaluates each of these factors in detail and
determines an overall tilt angle for the Zone 1 reactance element.
Using this tilt angle for a given right resistance blinder setting
| ensures   | security  |               | of  Zone 1  | quadrilateral    | distance  | elements,        |     |     |     |     |
| --------- | --------- | ------------- | ----------- | ---------------- | --------- | ---------------- | --- | --- | --- | --- |
| assuming  |           | the  correct  | operation   | of  directional  |           | and  fault-type  |     |     |     |     |
identification logics. This paper demonstrates how lowering the
right resistance blinder setting value reduces the necessary tilt for
the reactance element characteristic. This demonstration will
assist relay engineers to determine settings based on expected
values of fault resistances over the length of the protected zone.
This paper analyzes reactance elements polarized with negative-
sequence, zero-sequence, and loop currents.
|     |     |     | I.  INTRODUCTION  |     |     |     |     |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Distance relays are typically used to protect power lines.
They provide primary protection for in-line faults –without

communications channels– and backup protection for out-of-
section  faults.  In  1928,  Warrington  designed  an  Fig. 1.  Operating characteristic of the reactance relay designed by
Warrington.
electromechanical reactance relay that included two reactance
elements supervised by an admittance (mho) element [1]. Fig. 1  Warrington assumed the error in the reactance component
|     |     |     |     |     |     |     | (X ) introduced by the fault resistance (R |     | ) was negligible.  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | ------------------ | --- |
shows the operating characteristic of this relay in the impedance  ER F
plane. This relay has three operating zones for line protection:  Therefore, he used horizontal lines to represent the R F  values
•  for different fault locations, as shown in Fig. 1. There are many
Zone 1 (reactance), the reach of which is set to less
|     |                            |     |     |                 |     |     | fault conditions in which X |  may be significant. For example,  |     |     |
| --- | -------------------------- | --- | --- | --------------- | --- | --- | --------------------------- | ---------------------------------- | --- | --- |
|     | than the line impedance (Z |     |     | ) and provides  |     |     |                             | ER                                 |     |     |
1L
instantaneous protection for in-line faults.  a resistive single-line-to-ground (SLG) fault at the end of the
|     |                                                          |     |     |     |     |     | line with the remote terminal open may have a significant X |     |     | ,   |
| --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- |
|     | •  Zone 2 (reactance), the reach of which is set beyond  |     |     |     |     |     |                                                             |     |     | ER  |
the line impedance and provides primary protection  as illustrated in Fig. 2. The apparent impedance (Z APP ) in this
|     |                                                     |     |     |     |     |     | example is given by (1), where X |     |  is Im[R  / (1 + k | )]. In  |
| --- | --------------------------------------------------- | --- | --- | --- | --- | --- | -------------------------------- | --- | ------------------ | ------- |
|     | for in-line faults that are not seen in Zone 1 and  |     |     |     |     |     |                                  |     | ER F               | 0       |
backup protection for external faults.  general, k 0  is not a real number; therefore, Im[R F  / (1 + k 0 )] is
|     |                                                        |     |     |     |     |     | not zero. In Fig. 2, the angle of k |      |  is negative.  |      |
| --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | ----------------------------------- | ---- | -------------- | ---- |
|     | •  Zone 3 (mho), the reach of which is set beyond the  |     |     |     |     |     |                                     |      | 0              |      |
|     | Zone 2 reach, supervises Zones 1 and 2, and provides   |     |     |     |     |     |                                     |      | R              |      |
|     |                                                        |     |     |     |     |     |                                     | Z =Z | + F            | (1)  |
APP 1L
|     | backup protection for external faults.  |     |     |     |     |     |     |     | 1+k |     |
| --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
where:
−Z
Z 0L 1L
k =  is the zero-sequence compensation
0 3•Ζ
1L
factor.
Z  is the positive-sequence line impedance.
1L
Z 0L  is the zero-sequence line impedance.

2
|     |     |     |     | counterclockwise  |     | for  | different  | loading  | conditions,  |     | which  |
| --- | --- | --- | --- | ----------------- | --- | ---- | ---------- | -------- | ------------ | --- | ------ |
results in element over- or underreach [5]1.
Let us demonstrate how the polarizing quantity affects the
reach of the reactance element by considering a fault at a
distance m per unit (pu) from the relay, as shown in Fig. 4.

Fig. 4.  Two-source power system with a fault at a distance m per unit from
the relay.
|     |     |     |     | The voltage V |     |  at the relay location can be expressed as  |     |     |     |     |     |
| --- | --- | --- | --- | ------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
L
shown in (2).
|     |     |     |     |     |     | =m•Z |     | +I     |      |     |      |
| --- | --- | --- | --- | --- | --- | ---- | --- | ------ | ---- | --- | ---- |
|     |     |     |     |     |     | V    |     | •I     | •R   |     | (2)  |
|     |     |     |     |     |     | L    |     | IL L F | F    |     |      |
Fig. 2.  Apparent impedance Z  for an SLG fault at the end of the line with  Dividing both the sides of (2) by the polarizing current I ,
|                                                    | APP |     |        |                                          |     |         |      |            |     |      | P   |
| -------------------------------------------------- | --- | --- | ------ | ---------------------------------------- | --- | ------- | ---- | ---------- | --- | ---- | --- |
| the remote terminal open and fault resistance R    |     | .   |        |                                          |     |         |      |            |     |      |     |
|                                                    |     | F   |        | and taking imaginary parts, we get (3).  |     |         |      |            |     |      |     |
| Line loading also causes a significant effect on X |     |     |  [2].  |                                          |     |         |      |            |     |      |     |
|                                                    |     |     | ER     |                                          | V  |        | m•Z | •I        | I  | •R  |     |
|                                                    |     |     |        |                                          |     | L =Im |      | 1L L +Im | F   | F    |     |
Fig. 3 illustrates this behavior for an A-phase-to-ground (AG)    Im   (3)
|     |     |     |     |     | I  |     |     | I   |     | I   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fault at the end of the line with outgoing line load. Note the  P   P   P 
clockwise tilt of [I F  • R F  / I L ] with respect to the horizontal  Writing Im[I  • R  / I ] from (3) in polar form results in (4).
|                                            |     |                        |     |     |     | F F  | P   |      |     |     |     |
| ------------------------------------------ | --- | ---------------------- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- |
| representation in Fig. 1. In many cases, R |     |  can have high values  |     |     |     |      |     |      |     |     |     |
|                                            |     | F                      |     | V  |    | m•Z |    | I  |     |     |     |
depending on tower footing resistance or in the absence of  •I •R sin(∠I )
|     |     |     |     | Im L | =Im | 1L  | L + | F F |     | −∠I | (4)  |
| --- | --- | --- | --- | ----- | ----- | --- | ----- | --- | --- | --- | ---- |
F P
shield wires, or because of faults caused by flashover to a tree  I P   I P   I P 
| or brush fires [3]. In Fig. 3, I |  is the total fault current at the  |     |     |     |     |     |     |     |     |     |     |
| -------------------------------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F In (4), Im[V  / I ] is the relay calculated impedance based
L P
| fault location and I | L  is the loop current.  |     |     |                    |     |            |                |                   |     |     |                |
| -------------------- | ------------------------ | --- | --- | ------------------ | --- | ---------- | -------------- | ----------------- | --- | --- | -------------- |
|                      |                          |     |     | on the choice of I |     | P . When I | P  is set to I | L , the term Im[V |     |     | L  / I P ] is  |
referred as the reactance component of the apparent impedance.
|     |     |     |     | If the polarizing quantity angle ( |           |       |                                            | I P ) equals the fault current  |     |     |     |
| --- | --- | --- | --- | ---------------------------------- | --------- | ----- | ------------------------------------------ | ------------------------------- | --- | --- | --- |
|     |     |     |     | angle (                            | I ), sin( | I  –  | I ) is zero and the relay calculated       |                                 |     |     |     |
|     |     |     |     |                                    | F         | F     | P                                          |                                 |     |     |     |
|     |     |     |     | impedance (Im[V                    |           |  / I  | ]), using (4∠), corresponds to the actual  |                                 |     |     |     |
L P
reach im∠pedance ∠(Im[m∠ • Z
|     |     |     |     |                                  |                                                     |                                       |          |  • I  / I ]), resulting in no reach  |                          |            |        |
| --- | --- | --- | --- | -------------------------------- | --------------------------------------------------- | ------------------------------------- | -------- | ------------------------------------ | ------------------------ | ---------- | ------ |
|     |     |     |     |                                  |                                                     |                                       | 1L       | L P                                  |                          |            |        |
|     |     |     |     | errors. When                     |                                                     | I  leads                              | I , sin( | I  –                                 | I ) is negative and the  |            |        |
|     |     |     |     |                                  |                                                     | P                                     | F        | F                                    | P                        |            |        |
|     |     |     |     | relay calculated impedance (Im[V |                                                     |                                       |          | L  / I P ]), using (4), is smaller   |                          |            |        |
|     |     |     |     | than                             | the  ∠correspon∠ding                                |                                       |          | ∠actual∠                             | reach                    | impedance  |        |
|     |     |     |     | (Im[m • Z                        | 1L  • I                                             | L  / I P ]), causing overreach. When  |          |                                      |                          | I P  lags  | I F ,  |
|     |     |     |     | sin( IF –                        | IP) is positive and the relay calculated impedance  |                                       |          |                                      |                          |            |        |
]), using (4), is greater than the correspo∠nding ac∠tual
|     |     |     |     | (Im[V L  / I | P   |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
reac∠h impe∠dance (Im[m • Z
 • I  / I ]), causing underreach. In
|     |     |     |     |     |     |     | 1L  | L P |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
summary, the polarizing quantity leading the fault current
results in overreach, whereas the polarizing quantity lagging the
|     |     |     |     | fault  current  |          | causes     | underreach.  | In            | case  of  | Warrington’s  |        |
| --- | --- | --- | --- | --------------- | -------- | ---------- | ------------ | ------------- | --------- | ------------- | ------ |
|     |     |     |     | reactance       | element  | (Fig. 1),  |              | the  use  of  | phase     | current       | as  a  |
polarizing quantity does not follow the fault current angle. In

fact, the phase current can either lead or lag the fault current
| Fig. 3.  Apparent impedance Z          | APP  for an AG fault at the end of the line with  |     |     |                |     |               |                 |              |            |        |          |
| -------------------------------------- | ------------------------------------------------- | --- | --- | -------------- | --- | ------------- | --------------- | ------------ | ---------- | ------ | -------- |
|                                        |                                                   |     |     | depending      | on  | the  loading  |                 | conditions,  | resulting  |        | in  the  |
| outgoing load and fault resistance R.  | F                                                 |     |     |                |     |               |                 |              |            |        |          |
|                                        |                                                   |     |     | corresponding  |     | over-         | or  underreach  | of           | the        | phase  | current  |
Warrington’s relay uses phase current as the polarizing
polarized reactance element.
quantity for the reactance elements (depicted by horizontal lines
With advancements in electronic circuit technology, the
| limiting  Zones 1  | and  2  in  Fig. 1)  | of  the  ground  | distance  |     |     |     |     |     |     |     |     |
| ------------------ | -------------------- | ---------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
quadrilateral (also known as “polygonal”) characteristic was
elements [4]. The operating characteristic of reactance elements
introduced by some manufacturers. In 1970, the polygonal
| that  use  phase  | current  polarization  | tilts  clockwise  | or  |     |     |     |     |     |     |     |     |
| ----------------- | ---------------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
characteristic was introduced in a three-phase static protective
relay [6]. In 1971, E. Zurowski introduced the quadrilateral

1 This paper refers to the rotation of a vector by a negative angle as
clockwise tilt and by a positive angle rotation as counterclockwise tilt.

3
characteristic in a static protective relay, as described in [7]. In A relay with the loop polarized characteristic, as shown in
these characteristics, the resistive R and reactive X reaches are Fig. 5, underreaches for incoming load when the polarizing
set independently. Fig. 5 shows the quadrilateral characteristic quantity (loop current) lags the fault current and overreaches
with the corresponding resistive and reactance settings, R for outgoing load when the polarizing quantity (loop current)
SET
and X . leads the fault current. Typically, the loop polarized reactance
SET
elements need to have the reactance characteristic tilted
clockwise, e.g., –15 degrees [9], to avoid overreach. However,
in many cases, this tilt angle for the loop polarized reactance
element characteristic may not be sufficient to compensate for
heavy outgoing loading conditions.
Reference [5] describes a quadrilateral characteristic with a
reactance element that uses the residual current (three times the
zero-sequence current, 3 • I ) as the polarizing quantity.
0
Another choice for polarization is the negative-sequence
current (3 • I ). These polarizing quantities have the same angle
2
as the fault current angle for homogenous systems, irrespective
of load flow, theoretically resulting in no under- or overreach.
For nonhomogenous networks, these polarizing quantities need
correction.
This paper analyzes the effects of network nonhomogeneity,
instrument transformer errors, line charging currents, line
transpositions, zero-sequence mutual coupling, and unbalanced
operating conditions on the reactance element characteristics
that use negative-sequence, zero-sequence, and loop current
polarization. The paper focuses on providing guidance on how
to set the Zone 1 distance element to prevent element
Fig. 5. Quadrilateral characteristic in a static protective relay introduced by overreach.
E. Zurowski.
The reactance element of this quadrilateral characteristic II. FACTORS AFFECTING THE SECURITY OF ZONE 1
uses loop current as polarization. The impedance plots in Fig. 6 QUADRILATERAL DISTANCE ELEMENTS
illustrate under- and overreaching conditions of this
Table I summarizes the factors affecting the security of the
quadrilateral characteristic for different R values and loading
F Zone 1 quadrilateral distance elements. These factors are
conditions [2] [8]. The angles mentioned in Fig. 6 are of the
typically compensated by reducing the Zone 1 reach and/or
local voltage source behind the relay in reference to the remote
tilting the Zone 1 reactance characteristic in a clockwise
voltage source angle.
direction. An alternative to clockwise tilting of the reactance
characteristic is to reduce the right resistance blinder reach
setting. The security impact of Factors 1–7 and 9–10 in Table I
on Zone 1 distance elements and the corresponding
compensation through modification of the Zone 1 reach are
explained in [10]. The effect of coupling capacitor voltage
transformer (CCVT) transients (Factor 5 in Table I) may also
be compensated through built-in relay security logic or by
intentionally delaying the Zone 1 element. The Zone 1
overreach concerns, due to zero-sequence mutual coupling
(Factor 9 in Table I), may also be addressed through the
modification of the zero-sequence compensation factor [11]
[12].
This paper focuses on addressing Factors 3, 6, and 8–14
listed in Table I by modifying the tilt of the reactance element,
except in the case of Factor 11 (current transformer [CT]
Fig. 6. Apparent fault impedance for varying fault resistance for incoming
(solid blue and red dash lines) and outgoing (black dash and solid magenta saturation), which is compensated through the reactance
lines) loads. element reach. For reference, Table II summarizes typical
polarizing quantities for different fault types.
Sections III, V, VII, and X use the simulation results based
on the power system shown in Fig. 7. Note that the impedance
values used here are in primary ohms.

4
TABLE II
POLARIZING QUANTITIES FOR VARIOUS FAULT TYPES
Polarizing Quantity
|     |     |     |     |     |     |     | Negative- |     | Zero- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----- | --- | --- | --- |
Fault Type
|     |     |     |     |     |     |     | Sequence  |           | Sequence  | Loop Current  |             |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --------- | ------------- | ----------- | --- |
|     |     |     |     |     |     |     |           | Current   | Current   |               | (IL)        |     |
|     |     |     |     |     |     |     |           | (3 • I2)  | (3 • I0)  |               |             |     |
|     |     |     |     |     |     | AG  |           | 3 • I     | 3 • I     |               | I  + k  • I |     |
|     |     |     |     |     |     |     |           | A2        | 0         |               | A 0         | G   |
Fig. 7.  Power system used in Sections III, V, VII, and X.  BG  3 • I   3 • I  Ib + k • I
|     |     |          |     |     |     |     |     | B2      | 0       |     | 0           | G   |
| --- | --- | -------- | --- | --- | --- | --- | --- | ------- | ------- | --- | ----------- | --- |
|     |     | TABLE I  |     |     |     | CG  |     | 3 • I   | 3 • I   |     | I  + k  • I |     |
|     |     |          |     |     |     |     |     | C2      | 0       |     | C 0         | G   |
FACTORS AFFECTING SECURITY OF ZONE 1
|     |                                  |     |     |     |     | AB or ABG  | 3 • I |  – 3 • I |   –  |     | I  – I |     |
| --- | -------------------------------- | --- | --- | --- | --- | ---------- | ----- | -------- | ---- | --- | ------ | --- |
|     | QUADRILATERAL DISTANCE ELEMENTS  |     |     |     |     |            |       | A2       | B2   |     | A B    |     |
Compensation Modifying  BC or BCG  3 • I B2  – 3 • I C2   –  I B  – I C
Factors Affecting Zone 1  Tilt of  CA or CAG  3 • I C2  – 3 • I A2   –  I C  – I A
|     | Security  | Zone 1 Reach  |     | Reactance  |     |      |     |     |     |          |                |                |
| --- | --------- | ------------- | --- | ---------- | --- | ---- | --- | --- | --- | -------- | -------------- | -------------- |
|     |           |               |     |            |     | ABC  |     | –   | –   | I A  – I | B , I B  – I C | , I C  – I A   |
Element
1.  Line parameters (positive-      III.  CALCULATING THE NONHOMOGENOUS NETWORK
| and zero-sequence  |     |     |     |     |     |     | AND LOAD CORRECTION ANGLE FOR  |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
impedance).
CORRESPONDING POLARIZING QUANTITIES

| 2.  | Infeed and outfeed for  |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tapped or multiterminal  A.  Calculating the Nonhomogenous Network Correction
lines [13].  Angle for Negative-Sequence Current Polarization
3.  Relay steady-state errors.      In general, the nonhomogenous network correction angle for
|     |     | (Magnitude errors)  |     | (Angle errors)  |                                  |     |     |     |                                 |     |     |     |
| --- | --- | ------------------- | --- | --------------- | -------------------------------- | --- | --- | --- | ------------------------------- | --- | --- | --- |
|     |     |                     |     |                 | the negative-sequence network (θ |     |     |     | 2_NW ) is defined as the angle  |     |     |     |
4.  Transient overreach.      difference between the negative-sequence fault current and the
relay measured negative-sequence current. Some relays may

| 5.  | CCVT transients (may also  |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
be compensated through  refer this correction angle as TANG [9].
the security logic in the  For  the  system  shown  in  Fig. 8  and  the  corresponding
relay or by intentionally
negative-sequence network in Fig. 9, (5) provides the negative-
delaying Zone 1).
sequence current nonhomogenous network correction angle.
| 6.  | Voltage transformer (VT)  |     |    |    |     |     |     |     |     |     |     |     |
| --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I 
|     | steady-state magnitude and  | (Magnitude errors)  |     | (Angle errors)  |     |     |     |      |             |     |     |      |
| --- | --------------------------- | ------------------- | --- | --------------- | --- | --- | --- | ---- | ----------- | --- | --- | ---- |
|     |                             |                     |     |                 |     |     |     | θ    | =arg 2F   |     |     | (5)  |
|     | angle errors.               |                     |     |                 |     |     |     | 2_NW |             |     |     |      |
 I 
L
| 7.  | Voltage induction in  |     |    |     |     |     |     |     |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
secondary cables and
ground potential rise.

| 8.  | Network nonhomogeneity  |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and line loading.
|     |     |     |    |    |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
9.  Zero-sequence mutual
coupling (may also be

compensated through
modifying zero-sequence  Fig. 8.  Two-source power system with a single-line configuration.
compensation factor).
| 10.  | CT steady-state magnitude  |                     |    |                |     |     |     |     |     |     |     |     |
| ---- | -------------------------- | ------------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|      | and angle errors.          | (Magnitude errors)  |     | (Angle errors)  |     |     |     |     |     |     |     |     |
| 11.  | CT saturation.             |                     |    |                 |     |     |     |     |     |     |     |     |
| 12.  | Line charging current.     |                     |     |                |     |     |     |     |     |     |     |     |
| 13.  | Untransposed line.         |                     |     |                |     |     |     |     |     |     |     |     |

| 14.  | Unbalanced operating  |     |     |     |     |     |     |     |     |     |     |     |
| ---- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
conditions (may also be
addressed through the
security logic in the relay).
| 15.  | Subharmonic-frequency  |     |    |     |     |     |     |     |     |     |     |     |
| ---- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transient in series-
|     |     |     |     |     | Fig. 9.  | Negative-sequence network for the system shown in Fig. 8.  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
compensated lines [14].

5
Equation (5) is usually defined in terms of
negative-sequence network parameters. For the
negative-sequence network in Fig. 9, (5) can be expressed by
(6).
 Z +Z +Z 
θ =arg 2S 2L 2R  (6)
2_NW_SL  (1−m)•Z
2L
+Z
2R

For Zone 1 elements, the nonhomogenous network
correction angle is typically calculated for a fault at the Zone 1
reach [9]. However, to achieve an adequate negative-sequence
nonhomogenous network angle, consider faults at the Zone 1
reach and at the remote end of the line (m = 1) with a weak Fig. 11. Two-source power system with lines originating from different
source behind the relay and a strong source at the remote end. buses but terminating on a common bus.
Note that (6) is applicable for single-line configurations, not for
Fig. 11 shows the change in the negative-sequence
parallel lines originating from and terminating on a common
nonhomogenous network correction angle for faults at different
bus, as shown in Fig. 10. For such a parallel line configuration
locations over the length of the line for the system shown in
with both lines in service, (7) is used to determine the negative-
Fig. 7. The plots in Fig. 12 are for the relay located at Breaker 1
sequence current nonhomogenous network correction angle.
when either of the following operating conditions occur:
Refer to Appendix A for the derivation of
• Line 1 and Line 2 are in service.
(7).
• Line 1 is in service, and Line 2 is out of service
(Breakers 3 and 4 are open).
Fig. 10. Two-source power system with parallel lines originating from and
terminating on a common bus.
 
(1−m)•(Z +Z +Z )+Z 
θ =−arg 2S 2L R 2R (7)
2_NW_PL   Z  
 2•Z 2S + 2L +Z 2R 
  2  
In parallel line configurations, one of the lines can be out of
service. Therefore, consider the minimum of the
nonhomogenous network correction angles from (6) and (7). If
there is the possibility of a scenario in which the lines originate
from different buses but terminate on a common bus, as shown
in Fig. 11, consider the protected line (Line 1) as a single line Fig. 12. Negative-sequence nonhomogenous network correction angle
of a two-source power system, similar to the one shown in
(θ2_NW ) for faults at different locations over the length of the line for the
system shown in Fig. 7 for the relay located at Breaker 1.
Fig. 8, and use (6) to calculate the single-line nonhomogenous
network correction angle. Note that in this case, the negative-
sequence source impedance at the remote end is not only Z ,
1R
but also involves Z and Z .
1L2 1S2

6
TABLE III  Representing mutual coupling in the zero-sequence network
NEGATIVE-SEQUENCE NONHOMOGENOUS NETWORK CORRECTION ANGLE
can be complicated for multicircuit lines, especially for the ones
(Θ2_NW ) FOR SYSTEM IN FIG. 7 FOR THE RELAYS LOCATED AT BREAKER 1
that do not run along the entire length of the protected line.
θ2_NW  m = 0.8 (pu)  m = 1 (pu)  Therefore,  short-circuit  simulation  tools  are  convenient  to
θ2_NW_SL   calculate  the  zero-sequence  nonhomogenous  network
|     |     |     | –7°  |     | –9°  |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
(Lines 1 and 2 in service)  correction angle, especially at the Zone 1 reach. For line-end
θ2_NW_SL   faults, the zero-sequence network complexity is significantly
(Line 1 in service and Line 2 out  –3°  –10°  reduced. Note the reduced complexity in Fig. 14, which is the
of service)  same as Fig. 13; however, in this case, there is a fault at the
remote end of the line.
Because Zone 1 is an underreaching element, choose the
minimum of the nonhomogenous network angles calculated at
m = 0.8 pu (Zone 1 reach) and m = 1 pu for the single and
parallel line configurations using (6) and (7), respectively.
| Therefore,     | from  | Table III,           | the    | negative-sequence  |        |     |     |     |     |     |     |     |
| -------------- | ----- | -------------------- | ------ | ------------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| nonhomogenous  |       | network  correction  | angle  | for  the           | relay  | at  |     |     |     |     |     |     |
Breaker 1 is –10 degrees. To determine the correction angle for
the relay at Breaker 2, use the same approach described in this
section; however, consider a weak source behind the relay at
Breaker 2 and a strong source at the other end.
B.  Calculating the Nonhomogenous Network Correction
Angle for Zero-Sequence Current Polarization

| Calculate  | the  | zero-sequence  | nonhomogenous  |     | network  |                                                                                 |     |     |     |     |     |     |
| ---------- | ---- | -------------- | -------------- | --- | -------- | ------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|            |      |                |                |     |          | Fig. 14.  Zero-sequence network for a fault at the remote end of the line in a  |     |     |     |     |     |     |
correction angle for a single-line configuration using (8). To  configuration with two mutually coupled lines originating and terminating at
| achieve an adequate correction angle, consider faults at the  |     |     |     |     |     | the same buses.  |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
Zone 1 reach and the remote end of the line (m = 1) with a weak  Equations  (9)  and  (10)  give  the  zero-sequence
source behind the relay and a strong source at the remote end  nonhomogenous network correction angle for faults at the
of the line.
remote end of the protected line, which is mutually coupled
with n other lines. Equation (9) assumes all the n mutually
|     |     | I  |  Z +Z | +Z  |    |     |     |     |     |     |     |     |
| --- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
θ =arg 0F =arg 0S 0L 0R coupled lines originate and terminate at the same buses, where
|   0_NW_SL |     |      |            |     |    | (8)  |     |     |     |     |     |     |
| --------- | --- | ---- | ---------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|           |     | I  |  (1−m)•Z | +Z  |   |      |     |     |     |     |     |     |
0L 0L 0R k = 1 indicates the protected line. Use (10) for mutually coupled
lines that do not originate or terminate at a common bus or are
For mutually coupled line configurations, the zero-sequence
|     |     |     |     |     |     | partly  in  | parallel  | with  the  | protected  | line.  | As  | previously  |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ---------- | ---------- | ------ | --- | ----------- |
line impedance becomes a function of the zero-sequence mutual
|            |           |                |          |          |           | explained,  | merge  | the  parallel  | line  | impedances  |     | with  the  |
| ---------- | --------- | -------------- | -------- | -------- | --------- | ----------- | ------ | -------------- | ----- | ----------- | --- | ---------- |
| impedance  | and  the  | zero-sequence  | current  | of  the  | mutually  |             |        |                |       |             |     |            |
appropriate source impedances for mutually coupled lines with
coupled lines. Fig. 13 shows the change in the zero-sequence
only one common bus. If short-circuit simulation tools are not
impedance of the line due to the current in the parallel circuit
|     |     |     |     |     |     | available,  | use  | (9)  or  (10)  | to  | get  the  | zero-sequence  |     |
| --- | --- | --- | --- | --- | --- | ----------- | ---- | -------------- | --- | --------- | -------------- | --- |
for a fault at a distance m per unit from the relay. In this case,
nonhomogenous network correction angle for faults at m = 1.
the mutually coupled lines originate and terminate at the same
Note that (10) requires the values of the zero-sequence currents
buses.
of the adjacent lines for faults at the remote end of the protected
|     |     |     |     |     |     | line,  along  | with  | the  corresponding  |     | zero-sequence  |     | mutual  |
| --- | --- | --- | --- | --- | --- | ------------- | ----- | ------------------- | --- | -------------- | --- | ------- |
impedance values.
|     |     |     |     |     |     |         |        |       | Z    |    | n     |       |
| --- | --- | --- | --- | --- | --- | ------- | ------ | ------- | ---- | --- | ----- | ------ |
|     |     |     |     |     |     |         |        |  n• Z | + 0L | +Z  | + ∑ Z |       |
|     |     |     |     |     |     |         |        | 0S      |      | 0R | 0M1,k |        |
|     |     |     |     |     |     |         |        |       | n    |    |       |       |
|     |     |     |     |     |     | θ       | | =arg |         |      |     | k =2  |   (9)  |
|     |     |     |     |     |     | 0_NW_PL | m=1    |        |      |     |       |       |
Z
|     |     |     |     |     |     |          |        |      |     | 0R   |     |       |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | --- | ---- | --- | ------ |
|     |     |     |     |     |     |          |        |      |     |      |     |       |
|     |     |     |     |     |     |          |        |      |     |      |     |       |
|     |     |     |     |     |     |          |        |      |     | n I |    |       |
|     |     |     |     |     |     |          |        | Z +Z | +Z  | +∑   | 0Pk |       |
|     |     |     |     |     |     |          |        | 0S    | 0L  | 0R  | Z  | 0M1,k  |
|     |     |     |     |     |     |          |        |      |     | k=2 | I  |       |
|     |     |     |     |     |     | θ        |  =arg |       |     |      | 0L  |  (10)  |
|     |     |     |     |     |     | 0_NW_PL′ |        |      |     |      |     |       |
|     |     |     |     |     |     |          | m=1    |       |     | Z    |     |        |
|     |     |     |     |     |     |          |        |      |     | 0R   |     |       |
|     |     |     |     |     |     |          |        |      |     |      |     |       |
|     |     |     |     |     |     |          |        |      |     |      |     |       |
Fig. 13.  Zero-sequence network for a fault at distance m from the relay in a
configuration with two mutually coupled lines originating and terminating at
the same buses.

7
Fig. 15 shows the change in the zero-sequence C. Calculating the Load Correction Angle for Loop
nonhomogenous network correction angle for different fault Current Polarization
locations over the length of the line for the system shown in As summarized in Table II, the loop currents for different
Fig. 7. The plots in Fig. 15 are for the relay located at Breaker 1 fault types are functions of the phase currents. For resistive
when either of the following conditions occur: faults, the faulted phase current measured by the relay is the
• Line 1 and Line 2 are in service. superposition of the fault and load currents. Therefore, loop
• Line 1 is in service, and Line 2 is out of service currents cannot accurately provide the fault current angle;
(Breakers 3 and 4 are open). therefore, a correction is needed to ensure security of the
reactance element [2]. Equation (11), in general, defines the
loop current correction angle for faults at the remote end of the
protected line. Equation (11) gives the minimum angle
difference between the fault current and the corresponding
fault-type loop current for different fault resistances (in primary
ohms) at the remote end of the line. Short-circuit calculation
tools are convenient to solve (11). To achieve an adequate
correction angle, consider maximum outgoing power flow from
the protective relay point of view for all possible source
impedances.
 I  
θ  =minarg F  ∀ 1≤R <100 (11)
L_LOAD F
m=1  I L  
Fig. 16 shows the angle difference between the fault current
and the loop current for SLG faults at the remote end of the line
with varying fault resistances. The plots in Fig. 16 are for the
system shown in Fig. 7, for the relay located at Breaker 1, when
either of the following conditions occur:
• Line 1 and Line 2 are in service.
Fig. 15. Zero-sequence nonhomogenous network correction angle (θ0_NW ) • Line 1 is in service, and Line 2 is out of service
for different fault locations over the length of the line for the system shown in (Breakers 3 and 4 are open).
Fig. 7, for the relay located at Breaker 1.
Because the faults are simulated at the remote end of the
TABLE IV protected line, when the mutually coupled lines in service
ZERO-SEQUENCE NONHOMOGENOUS NETWORK CORRECTION ANGLE (Θ0_NW )
originate and terminate at the same buses, we use the modified
FOR THE SYSTEM IN FIG. 7, FOR THE RELAY LOCATED AT BREAKER 1
zero-sequence compensation factor in (11) [11].
θ0_NW m = 0.8 (pu) m = 1 (pu)
Z +Z −Z 
θ0_NW_SL –4° –11° k
0L_PL
= 0L 0M 1L  (12)
 3•Z 1L 
θ0_NW_PL –2° –12°
From Fig. 16, we can conclude that the minimum angle
Because Zone 1 is an underreaching element, choose the
difference between the fault current and the corresponding relay
minimum of the nonhomogenous network correction angles,
loop current at Breaker 1 is –34 degrees. Therefore, from (11),
calculated at m = 0.8 pu (Zone 1 reach) and m = 1 pu for single
θ is the loop current correction angle for the relay at
L_LOAD
and mutually coupled lines originating and terminating at the
Breaker 1 for SLG faults. To determine an adequate loop
same buses. Therefore, from Table IV, we can conclude that the
current correction angle for multiphase fault loops, use the same
zero-sequence nonhomogenous network correction angle for
approach described in this section; however, consider
the relay at Breaker 1 is –12 degrees. To determine the
multiphase faults at the remote end of the line. To determine an
correction factor for the relay at Breaker 2, use the same
adequate loop current correction angle for the relay at
approach described previously in this section; however,
Breaker 2, use the same approach described in this section;
consider a weak source behind the relay at Breaker 2 and a
however, consider reversing the power flow in the system, as
strong source at the other end.
shown in Fig. 7, such that the relay at Breaker 2 measures the
maximum outgoing power when faults are simulated at the
remote end of the line.

8
Fig. 18. Negative-sequence network for the system in Fig. 17 for an
unbalanced fault beyond the remote bus.
Fig. 16. Angle difference between the fault current and the corresponding
Fig. 18 shows the negative-sequence network for an
loop current (θL_LOAD ) measured by the relay at Breaker 1 in Fig. 7 for SLG
faults at the remote end of the line. unbalanced fault beyond the remote bus (m = 1.25 pu). Notice
that the remote impedance is modeled as a combination of
IV. CALCULATING THE NEGATIVE- AND ZERO-SEQUENCE impedances, such that the total impedance beyond the remote
NONHOMOGENOUS NETWORK CORRECTION ANGLE bus is still the same as that shown in Fig. 17. Using (6), the
FOR LINES WITH LOW-IMPEDANCE ANGLES negative-sequence correction angle for a fault at m = 1.25 pu
This section explains calculating the nonhomogenous equals –9 degrees, which is lower than the correction angle of
network correction angles for lines with an impedance angle –8 degrees considered for the Zone 1 reactance element.
less than 70 degrees. Low line impedance angles are Because of this angle difference, the Zone 1 quadrilateral
particularly common in underground cables [15]. Fig. 17 shows distance element may overreach for resistive faults beyond the
an example of a subtransmission underground cable of 15 miles remote bus (see Fig. 19). Fig. 19 shows the reactance element
that connects the two sources of the power system. Note that characteristics at Zone 1 reach (Z 1R ) and m = 1.25 pu, with
the impedance values used in this example are in primary ohms. correction angles of –8 degrees and –19 degrees, respectively.
To calculate an adequate nonhomogenous network correction
angle, consider a weak source behind the relay and a strong
source at the remote end. The following example evaluates only
the use of (6) for calculating the negative-sequence
nonhomogeneous correction angle for lines with
low-impedance angles. A similar analysis can be extended by
using (8) for calculating the zero-sequence nonhomogenous
correction angle for lines with low-impedance angles.
Fig. 19. Operating characteristics of reactance elements at Zone 1 reach
(Z ) and m = 1.25 pu for an unbalanced fault at m = 1.25 pu.
1R
In Fig. 19, if the right resistance blinder is set in such a way
that its characteristic falls on the left of the intersection of the
two reactance characteristics, then the Zone 1 element is secure;
otherwise, it is not. However, determining that setting of the
right resistance blinder is not easy. Alternatively, the simplest
Fig. 17. Two-source subtransmission power system with an underground way is to apply a nonhomogenous network correction angle,
cable connecting the two sources. from (13), to the negative-sequence current polarized Zone 1
Using (6) and based on the selected values of source reactance element. The acronym “SL_LZA_NW,” used in (13)
impedances in Fig. 17, the negative-sequence nonhomogenous and (14), stands for a single-line configuration with a low
network correction angle for a fault at the remote bus (m = 1 pu) impedance angle in a nonhomogenous network.
is –8 degrees. Consider using this clockwise tilt for the θ =arg(Z +Z )−88° (13)
2_SL_LZA_NW 2S 2L
negative-sequence polarized Zone 1 reactance element.
Equation (13) is a simplified form of (6), with m = 1 and
assuming that the strongest theoretical possible remote
impedance (e.g., |Z | = 1 mΩ) has a very high impedance
2R
angle (e.g., Z = 88 degrees). These assumptions result in a
2R
higher clockwise tilt angle value compared to the one obtained
from (6); thu∠s, prevent overreach issues like the one illustrated
in Fig. 19. Therefore, for applications with lines having low
negative-sequence impedance angle (less than 70 degrees)

9
consider using (13), instead of (6), to calculate the negative- even a low value of (θ  – θ ) causes a significant
|     |     |     |     |     |     |     |     |     |     | V_ERR | IPOL_ERR |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- |
sequence nonhomogenous correction angle. Similarly, consider  error in the reach of the reactance element. To avoid reactance
using  (14),  instead  of  (8),  to  calculate  the  zero-sequence  element overreach because of instrument transformer angle
nonhomogenous  correction  angle  for  lines  with  low  zero- errors, the reactance element characteristic needs to be tilted
sequence impedance angle (less than 70 degrees).  clockwise by an angle of (θ V_ERR  – θ IPOL_ERR ). The following
|     |     |             |     |        |       |        |       | example  | illustrates  | how  | to  compensate  | reactance  | element  |
| --- | --- | ----------- | --- | ------ | ----- | ------ | ----- | -------- | ------------ | ---- | --------------- | ---------- | -------- |
|     |     | θ           |     | =arg(Z | +Z    | )−88°  | (14)  |          |              |      |                 |            |          |
|     |     | 0_SL_LZA_NW |     |        | 0S 0L |        |       |          |              |      |                 |            |          |
overreach because of instrument transformer angle errors.
|                | Using  (13)  | and      | (14),  | the  negative-  |         | and  zero-sequence  |        |     |     |     |     |     |     |
| -------------- | ------------ | -------- | ------ | --------------- | ------- | ------------------- | ------ | --- | --- | --- | --- | --- | --- |
| nonhomogenous  |              | network  |        | correction      | angles  | for  the            | relay  |     |     |     |     |     |     |
protecting the underground cable in Fig. 17 equal –21 degrees
and –10 degrees, respectively.
V.  CALCULATING THE FAULTED PHASE VOLTAGE AND
POLARIZING QUANTITY ANGLE ERRORS BECAUSE OF VT AND
CT STEADY-STATE ANGLE ERRORS
The errors of the primary and relay instrument transformers
may cause underreach or overreach of the Zone 1 distance
| elements  | [16]  | [17].  | To  | secure  | the  Zone 1  | elements,  | the  |     |     |     |     |     |     |
| --------- | ----- | ------ | --- | ------- | ------------ | ---------- | ---- | --- | --- | --- | --- | --- | --- |
instrument transformer magnitude errors for line-end metallic
| faults  | (R  = 0)  | are  | typically  | compensated  |     | by  reducing  | the  |     |     |     |     |     |     |
| ------- | --------- | ---- | ---------- | ------------ | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- |
F
Zone 1 reach. Equation (15) gives an expression for the error in

| the reactance element reach, Ψ |     |     |     |     |  (in pu), in terms of the  |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
m_IT_ANG
|                                                |           |     |     |     |           |                  |         | Fig. 20.  Effect of increasing the fault resistance (reducing [θV        |     |     |     |  – θIF | ]) on  |
| ---------------------------------------------- | --------- | --- | --- | --- | --------- | ---------------- | ------- | ------------------------------------------------------------------------ | --- | --- | --- | ------ | ------ |
| angle errors of the faulted phase voltage (θ   |           |     |     |     |           | ) and the        |         |                                                                          |     |     |     |        |        |
|                                                |           |     |     |     |           | V_ERR            |         | reactance element overreach for different instrument transformers angle  |     |     |     |        |        |
| polarizing current of the reactance element (θ |           |     |     |     |           |                  | ). The  |                                                                          |     |     |     |        |        |
|                                                |           |     |     |     |           | IPOL_ERR         |         | errors.                                                                  |     |     |     |        |        |
| acronym                                        | “IT_ANG”  |     | in  | Ψ   |   stands  | for  instrument  |         |                                                                          |     |     |     |        |        |
m_IT_ANG For the example system shown in Fig. 7, consider an AG
transformer angle error. Refer to Appendix B for the derivation
|     |     |     |     |     |     |     |     | metallic fault (R |     |  = 0) at the end of the line for a heavy loading  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------------------------------------------- | --- | --- | --- |
F
of (15). In this equation, the VT and CT magnitude errors are
condition and a weak source behind the relay. Table V shows
ignored because these errors are assumed to be compensated by
the phase currents for this fault with and without CT angle
the  Zone 1  reach  setting.  The  polarizing current  angle,  in  errors and the corresponding polarizing quantities derived from
primary amperes, is assumed to be the same as the fault current
the phase currents. We assumed a steady-state CT angle error
| angle. Therefore, θ |     |     |     |  has only CT angle errors. Negative  |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IPOL_ERR of ±2 degrees in each of the phase currents. Note that an angle
| values of Ψ |     |     |  indicate overreach, whereas positive values  |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m_IT_ANG error of ±2 degrees in the phase currents may translate to a
| indicate  | underreach.  |     | Note  | that  | (15)  is  | an  approximate  |     |                                                  |     |     |     |            |     |
| --------- | ------------ | --- | ----- | ----- | --------- | ---------------- | --- | ------------------------------------------------ | --- | --- | --- | ---------- | --- |
|           |              |     |       |       |           |                  |     | higher angle error in the polarizing quantity (θ |     |     |     | ). Taking  |     |
IPOL_ERR
expression and therefore may have numerical errors. However,
|     |     |     |     |     |     |     |     | the values of (θ |     | ) from Table V and assuming –2 degrees  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------------------------------- | --- | --- | --- |
(15) is still valuable for illustrating the effect of instrument  IPOL_ERR
|     |     |     |     |     |     |     |     | of angle error in the faulted phase voltage (θ |     |     |     | ), the total  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | ------------- | --- |
V_ERR
transformer angle errors on reach estimation.
|     |     |     |     |     |     |     |     | angle  error  | (θ V_ERR |  – θ IPOL_ERR | )  affecting  | the  reach  | of  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ------------- | ------------- | ----------- | -------- |

negative-sequence, zero-sequence, and loop current polarized
|     |     |     | (   | )   | (   |     | )   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  Ψ ≈cot θ −θ • θ −θ  (15)  reactance elements equals 0, –7, and –6 degrees, respectively.
|     | m_IT_ANG |     | V   | IF  | V_ERR | IPOL_ERR |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
TABLE V
where:
CURRENT PHASORS AND POLARIZING QUANTITY ANGLE ERRORS FOR A
(θ  – θ ) is the angle difference between the faulted  LINE-END METALLIC AG FAULT IN THE FIG. 7 SYSTEM
|     | V   | IF  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
phase voltage at the relay location and the total fault
|     |                                                     |     |     |     |     |     |     |           |                |              | Phasors With  |            |     |
| --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | -------------- | ------------ | ------------- | ---------- | --- |
|     |                                                     |     |     |     |     |     |     |           | Ideal Phasors  |              |               | θIPOL_ERR  |     |
|     | current.                                            |     |     |     |     |     |     |           |                |              | Angle Errors  |            |     |
|     | θ  is the error in the faulted phase voltage angle  |     |     |     |     |     |     |           |                |              |               |            |     |
|     | V_ERR                                               |     |     |     |     |     |     |  stnerruC | I              |  = 720∠ 49°  | I ʹ = 720 ∠   | 47°        | –   |
|     |                                                     |     |     |     |     |     |     |  esahP    | A              |              | A             |            |     |
because of the primary and relay VTs.
θ  is the error in the polarizing current angle  I B  = 574 ∠–112°  I B ʹ = 574 ∠–110°  –
IPOL_ERR
because of the primary and relay CTs.  I  = 590 ∠–126°  I ʹ = 590 ∠–124°  –
|     |                       |     |      |                                   |     |     |     |                | C             |       | C              |       |      |
| --- | --------------------- | --- | ---- | --------------------------------- | --- | --- | --- | -------------- | ------------- | ----- | -------------- | ----- | ---- |
|     | In (15), the angle (θ |     |  – θ | ) is expected to decrease as the  |     |     |     |                |               |       |                |       |      |
|     |                       |     | V    | IF                                |     |     |     |  gnidnopserroC |               |       |                |       |      |
|     |                       |     |      |                                   |     |     |     |                | 3 • I = 642 ∠ | 101°  | 3 • Iʹ = 632 ∠ | 103°  | –2°  |
fault resistance increases, resulting in increasing overreach or   gniziraloP  seititnauQ 2 2
| underreach depending on the angle error (θ |     |     |     |     |     |  – θ  |          | ).  |               | –    |                | –    |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ----- | -------- | --- | ------------- | ---- | -------------- | ---- | --- |
|                                            |     |     |     |     |     | V_ERR | IPOL_ERR |     |               |      |                |      |     |
|                                            |     |     |     |     |     |       |          |     | 3 • I = 605 ∠ | 99°  | 3 • Iʹ = 578 ∠ | 94°  | 5°  |
Fig. 20 illustrates instances of reactance element overreach for  0 0
| different values of (θ |     |     |       |  – θ     | ). On the abscissa, the  |     |     |     |     | –   |     | –   |     |
| ---------------------- | --- | --- | ----- | -------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|                        |     |     | V_ERR | IPOL_ERR |                          |     |     |     |     |     |     |     |     |
angle (θ  – θ ) is reduced from 90 degrees to 10 degrees,  I  = 1006 ∠ 73°  I ʹ = 1004 ∠ 69°  4°
|     | V   | IF  |     |     |     |     |     |     | L   |     | L   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
indicating an increase in the fault resistance, while the ordinate  – –
shows Ψ  for different values of (θ  – θ ).  In  Table V,  because  the  phase  current  angle  errors
|     | m_IT_ANG |     |     |     |     | V_ERR | IPOL_ERR |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- |
(±2 degrees) were introduced randomly, we cannot rely on the
| Note that for high fault resistances (low values of [θ |     |     |     |     |     |     |  – θ ]),  |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
|                                                        |     |     |     |     |     |     | V IF      |     |     |     |     |     |     |

10
minimum  values  of  the  polarizing  quantity  angle  errors.  following points when using short-circuit programs to evaluate
Therefore, for the example system of Fig. 7 and assuming  the Zone 1 quadrilateral element security for line-end faults that
±2 degrees of steady-state angle error in the CTs and PTs,  cause local CT saturation:
•
consider tilting the negative-sequence, zero-sequence, or loop  Fault resistance affects (θ V  – θ IF ). As the fault
polarized  reactance  element  characteristics  clockwise  by  resistance increases, (θ  – θ ) decreases, and the
|     |     |     |     |     |     |     |     |     | V   | IF  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7 degrees (maximum of |θ  – θ |) to avoid reactance  leading angle (positive value) of θ  because of
|     |     |     | V_ERR IPOL_ERR |     |     |     |     |     |     | IPOL_ERR |     |
| --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | -------- | --- |
element overreach because of instrument transformer angle  CT saturation may cause an increase in Ψ .
m_CT_SAT
| errors.  |     |     |     |     |     |     |     | Metallic faults will most likely cause underreach.  |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
In summary, to avoid reactance element overreach because  •  Loading conditions affect (I ) and (θ ).
|     |     |     |     |     |     |     |     |     |     | L_MAG_ERR | IPOL_ERR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- |
of instrument transformer angle errors, determine (θ )  •  Several factors affect CT saturation, e.g., saturation
IPOL_ERR
for different possible values of the CT angle error in the phase
voltage of the CT, CT burden, fault current,
currents and tilt the reactance element characteristic clockwise  remanence, CT ratio, CT winding resistance [19].
| by the maximum value of (|θ |     |     |  – θ |     | |). Calculate the  |     |     |     |     |     |     |
| --------------------------- | --- | --- | ---- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
V_ERR IPOL_ERR If the CT saturation results in overreach of the reactance
phase currents for a line-end metallic fault (R F  = 0), with heavy  element, the Zone 1 reach may have to be reduced appropriately
line loading and the weakest source behind the relay.
to ensure its security.
VI.  EFFECT OF CT SATURATION ON THE REACTANCE  VII.  CALCULATING THE POLARIZING QUANTITY ANGLE
ELEMENT REACH
ERROR BECAUSE OF LINE CHARGING CURRENT
Ideally, CTs are not expected to saturate for faults at the
This section demonstrates the effect of line charging current
remote end of the line. However, saturation may occur for line- on the negative-sequence, zero-sequence, and loop polarizing
end faults in short lines with strong systems. When a CT
quantities. When the negative- and zero-sequence networks
saturates, the resulting current phasor has a reduced magnitude  have line and source impedance angles close to 90 degrees (i.e.,
and a leading phase angle shift [18]. Typically, the reduction in  greater than 85 degrees), the shunt capacitance currents of
magnitude of the faulted phase current results in underreach of
negative- and zero-sequence networks are either in phase or out
the reactance element. However, the leading phase angle shift  of phase with the negative- and zero-sequence relay currents,
of the faulted phase current may result in a leading or lagging
respectively [20]. Therefore, there is negligible impact on the
phase angle shift of the polarizing quantity, causing the element  angle error between the relay current and the total fault current
to overreach or underreach for resistive faults. Equation (16)  when  compared  to  the  same  network  without  shunt
shows an approximate expression to determine the error in the
capacitances. Typically, the relay negative- and zero-sequence
reactance element reach, Ψ  (in pu), caused by CT  voltages are smaller than the positive-sequence voltage. This
m_CT_SAT
saturation, assuming no error in the faulted phase voltage
makes the shunt charging currents that are directly proportional
magnitude and angle. Refer to Appendix B for the derivation of  to the magnitude of the voltage less significant in the zero- and
| (16). Negative values of Ψ |     |     |  indicate overreach, whereas  |     |     |     |                              |     |     |     |     |
| -------------------------- | --- | --- | ----------------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
|                            |     |     | m_CT_SAT                      |     |     |     | negative-sequence networks.  |     |     |     |     |
positive values indicate underreach.  Consider the example system of Fig. 7, with a metallic AG
|     |     |     |       |      |     |      | fault (R |  = 0) at the end of the line with the weakest source  |     |     |     |
| --- | --- | --- | ----- | ---- | --- | ---- | -------- | ----------------------------------------------------- | --- | --- | --- |
|     |     |     |  (   |      | ) ( | )−1 |          | F                                                     |     |     |     |
| Ψ   |     | ≈I  | 1−cot | θ −θ | • θ |      |          |                                                       |     |     |     |
m_CT_SAT L_MAG_ERR  V IF IPOL_ERR  behind the relay. To avoid the effect of mutual coupling, the
parallel line is kept out of service. Table VI shows the angles of
|     |     |     |     |     |     | (16)  |      |                     |                 |            |             |
| --- | --- | --- | --- | --- | --- | ----- | ---- | ------------------- | --------------- | ---------- | ----------- |
|     |     |     |     |     |     |       | the  | negative-sequence,  | zero-sequence,  | and  loop  | polarizing  |
where:
quantities with respect to the total fault current with and without
|     |     | I   |     |     |     |     | considering  | the  | line  shunt  | capacitances.  | We  used  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ------------ | -------------- | --------- |
L_UNSAT
|     | I   | =   |  is the magnitude of the ratio  |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
L_MAG_ERR I Electromagnetic  Transients  Program  (EMTP)  software  to
L_SAT
model these conditions.
|     | of the unsaturated faulted loop current (I |     |     |     | L_UNSAT ) to the  |     |     |     |           |     |     |
| --- | ------------------------------------------ | --- | --- | --- | ----------------- | --- | --- | --- | --------- | --- | --- |
|     | saturated faulted loop current (I          |     |     | ).  |                   |     |     |     | TABLE VI  |     |     |
L_SAT
NEGATIVE-SEQUENCE, ZERO-SEQUENCE, AND LOOP POLARIZED
(θ V  – θ IF ) is the angle difference between the faulted  CURRENT ANGLES FOR LINE-END FAULT WITH AND WITHOUT
phase voltage at the relay location and the total fault  LINE SHUNT CAPACITANCE
current.
Polarizing
|     | (θ       | ) is the error in the polarizing current angle  |     |     |     |     |     |                 |            |               |     |
| --- | -------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --------------- | ---------- | ------------- | --- |
|     | IPOL_ERR |                                                 |     |     |     |     |     | Quantity Angle  | With Line  | Without Line  |     |
because of CT saturation.
|     |     |     |     |     |     |     | With Respect to  |     | Capacitance  | Capacitance  | (1) – (2)  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | ------------ | ---------- |
Equation (16) is helpful when the user knows (I )  Total Fault  (1)  (2)
L_MAG_ERR
and (θ ) for different values of (θ  – θ ) for line-end  Current Angle
|     | IPOL_ERR |     |     | V   | IF  |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
faults that cause local CT saturation. Note that (16) may not  ∠3 • I – ∠I  8.6°  9.1°  –0.5°
2 F
| hold true for severe CT saturation, resulting in |θ |     |     |     |     |          | | being  |     |              |        |        |        |
| --------------------------------------------------- | --- | --- | --- | --- | -------- | -------- | --- | ------------ | ------ | ------ | ------ |
|                                                     |     |     |     |     | IPOL_ERR |          |     | ∠3 • I – ∠I  | 10.4°  | 10.8°  | –0.4°  |
0 F
greater than 20 degrees because the angle error assumptions
made  in  deriving  (16)  are  no  longer  valid.  However,  the  ∠ ∠ 36.8°  35.8°  1°
|                                                                  |     |           |                |     |                  |      |     | L F     |     |     |     |
| ---------------------------------------------------------------- | --- | --------- | -------------- | --- | ---------------- | ---- | --- | ------- | --- | --- | --- |
| parameters in (16) affecting the error in the reactance element  |     |           |                |     |                  |      |     | I –  I  |     |     |     |
| reach,                                                           | Ψ   | ,  still  | apply.  Based  | on  | (16),  consider  | the  |     |         |     |     |     |
m_CT_SAT

11
Table VI shows that the angles of the zero- and negative- TABLE VII
ERROR IN THE NEGATIVE-SEQUENCE, ZERO-SEQUENCE, AND LOOP
sequence currents for the line model with shunt capacitance are
POLARIZED CURRENT ANGLES BECAUSE OF UNTRANSPOSED (UT) LINE
smaller than the ones for the line without shunt capacitance.
The  smaller  angles  of  these  polarizing  currents  result  in  Fault  Angle Error, in Degrees, for
underreach of the corresponding reactance element. Therefore,    I2_UT  I0_UT  IL_UT
no compensation is needed for the zero- and negative-sequence
|     |     |     |     |     |     |     |     | AG (outgoing power)  |     |     | 1.1  |     | –0.1  | 0.5  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ---- | --- | ----- | ---- | --- |
polarized reactance element for the example system in Fig. 7.
However,  the  loop  current  for  the  line  model  with  shunt  BG (outgoing power)  2.3  –0.8  0.1
| capacitance  | is  | greater  than  | the   | one      | without  | line  | shunt  |                      |     |     |       |     |       |       |     |
| ------------ | --- | -------------- | ----- | -------- | -------- | ----- | ------ | -------------------- | --- | --- | ----- | --- | ----- | ----- | --- |
|              |     |                |       |          |          |       |        | CG (outgoing power)  |     |     | –3.5  |     | 0     | –0.6  |     |
| capacitance  | by  | one degree.    | This  | greater  | angle    | must  | be     |                      |     |     |       |     |       |       |     |
|              |     |                |       |          |          |       |        | AG (incoming power)  |     |     | 2.3   |     | –0.5  | 0.2   |     |
compensated for to avoid overreach by tilting the loop polarized
|     |     |     |     |     |     |     |     | BG (incoming power)  |     |     | –2.3  |     | –0.2  | –0.2  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ----- | --- | ----- | ----- | --- |
reactance element characteristic clockwise by one degree.
|     |     |     |     |     |     |     |     | CG (incoming power)  |     |     | –0.5  |     | –0.5  | 0.0  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ----- | --- | ----- | ---- | --- |
VIII.  CALCULATING THE POLARIZING QUANTITY ANGLE
|     |     |     |     |     |     |     |     | Based  | on  | the  results  | summarized  |     | in  Table VII,  | tilt  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------------- | ----------- | --- | --------------- | ----- | ---- |
ERROR IN LINES WITHOUT TRANSPOSITIONS
negative-sequence reactance element characteristic by at least
This section explains how to estimate the polarizing quantity
2.3 degrees in the clockwise direction to avoid the overreach
| angle  error  | in  | untransposed  | line  | applications.  |     | The  | EMTP  |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | ----- | -------------- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
caused by the untransposed line. The characteristic of the zero-
| simulation  | results,  | shown  | in  this  | section,  | are  | based  | on  a  |     |     |     |     |     |     |     |     |
| ----------- | --------- | ------ | --------- | --------- | ---- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
sequence current polarized reactance element needs no tilt, and
horizontal transmission line configuration (see Fig. 21). We
|     |     |     |     |     |     |     |     | the  loop  | current  | polarized  | reactance  |     | element  | characteristic  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---------- | ---------- | --- | -------- | --------------- | --- |
simulated SLG faults at the remote end of this untransposed line
requires only 0.5 degrees of tilt in the clockwise direction. Note
| in  a  perfectly  |     | homogenous  | system.  | Therefore,  |     | the  | angle  |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----------- | -------- | ----------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
that the results summarized in Table VII are for SLG faults.
difference between the negative- or zero-sequence current and
Therefore, the angle errors are suitable only for the ground
the fault current is the error in the respective polarizing quantity
reactance elements. Use a similar approach to determine the
solely due to the lack of transpositions. Had we considered an
|     |     |     |     |     |     |     |     | angle  errors  |     | for  the  | phase  reactance  |     | elements,  | simulating  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | ----------------- | --- | ---------- | ----------- | --- |
ideally transposed line in a perfectly homogenous system, the
multiphase faults.
| angle  difference  |     | between  | the  | negative-  | or  | zero-sequence  |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | ---- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
current and the fault current would have been zero.
CALCULATING THE POLARIZING QUANTITY ANGLE ERROR
IX.
BECAUSE OF UNBALANCED OPERATING CONDITIONS
|     |     |     |     |     |     |     |     | This  | paper  | defines  | unbalanced  | operating  |     | conditions  | as  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | -------- | ----------- | ---------- | --- | ----------- | --- |
unbalanced loading, open phase caused by a broken conductor
|     |     |     |     |     |     |     |     | or breaker operation,  |     |     | a pole  | open  in  | a parallel  | line, pole  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ------- | --------- | ----------- | ----------- | --- |
discrepancy while clearing multiphase faults, breaker failure, or
|     |     |     |     |     |     |     |     | asymmetrical  |     | series  | capacitor  | switching.  |     | In  general,  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ---------- | ----------- | --- | ------------- | --- |
transmission and distribution networks with single- and three-
pole tripping protection schemes are subjected to unbalanced
operating conditions. Occurrence of a resistive fault under such
conditions corrupts the polarizing current of the reactance
element, resulting in element underreach or overreach. The
following example demonstrates reactance element overreach
|                                                                  |     |     |     |     |     |     |     |   conditions  | because  |     | of  a  resistive  | fault  | in  | an  unbalanced  |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | ----------------- | ------ | --- | --------------- | --- |
| Fig. 21.  Typical 345 kV transmission line tower configuration.  |     |     |     |     |     |     |     | network.      |          |     |                   |        |     |                 |     |
In the Fig. 22 example system, consider a resistive AG fault
To calculate the loop current angle errors in untransposed
line  applications,  use  EMTP  software  and  find  the  angle  at the remote end of the protected line without (Fig. 22 (a)) and
with (Fig. 22 (b)) an open-phase condition. No magnetic mutual
difference between the loop current and the fault current for an
ideally  transposed  line;  then,  subtract  it  from  the  angle  coupling  is  considered  between  the  parallel  lines  and  the
impedance values are in primary ohms. For the AG fault and
difference between the loop current and the fault current for the
|                     |     |     |     |     |     |     |     | the system conditions shown in Fig. 22, (3 • I |     |     |     |     |       | ), (3 • I | ),    |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | ----- | --------- | ----- |
| untransposed line.  |     |     |     |     |     |     |     |                                                |     |     |     |     | 2_FLT |           | 0_FLT |
Table VII  summarizes  the  angle  errors  for  negative- and (I L_FLT ) are the relay measured negative-sequence, zero-
|     |     |     |     |     |     |     |     | sequence,  | and  | loop  | current  phasors,  |     | in  primary  | amperes.  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ----- | ------------------ | --- | ------------ | --------- | --- |
sequence, zero-sequence, and loop polarized currents for SLG
faults at the remote end of the line for outgoing and incoming  Whereas,  (3 • I 2_UB ),  (3 • I 0_UB ),  and  (I L_UB )  are  the  relay
measured primary negative-sequence, zero-sequence, and loop
| loading  | conditions.  | A  positive  |     | angle  error  | means  | that  | the  |     |     |     |     |     |     |     |     |
| -------- | ------------ | ------------ | --- | ------------- | ------ | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
current phasors because of the unbalanced operating condition
| corresponding  |     | polarizing  | quantity  | leads  | the  | fault  | current  |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | --------- | ------ | ---- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(Phase A open in a parallel line) prior to the occurrence of the
phasor, which causes reactance element overreach. A negative
|     |     |     |     |     |     |     |     | fault (Fig. 22 (b)). The value, I |     |     |     | , is the total fault current, in  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --------------------------------- | --- | --- | --- |
angle  error  in  the  polarizing  quantity  indicates  reactance  FLT
element underreach.  primary amperes, and the reference for the other phasors listed
in Table VIII and Table IX. Because the system is homogenous,

12
no tilt is considered for the zero- and negative-sequence current  zero-sequence, and loop current polarized reactance elements
polarized reactance elements. However, to account for outgoing  need an additional tilt of –7, –5, and –3 degrees, respectively,
loading, a tilt of –7 degrees is assumed for the loop polarized  to  avoid  overreach.  However,  this  additional  tilt  may  not
reactance element.  guarantee  addressing  overreach  concerns  caused  by  other
| (a)  |     |     |     | unbalanced operating conditions.  |     |     |     |     |     |
| ---- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
TABLE IX
CURRENT PHASORS FOR THE AG FAULT IN FIG. 22 (B) (WITH PHASE A OPEN
IN THE PARALLEL LINE)
Overrreach (pu) in
|     |     |     |     |         |     | Magnitude    | Angle              |     |     |
| --- | --- | --- | --- | ------- | --- | ------------ | ------------------ | --- | --- |
|     |     |     |     | Phasor  |     |              | the Corresponding  |     |     |
|     |     |     |     |         |     | (A Primary)  | (Deg.)             |     |     |
Reactance Element
|     |     |     |     | 3 • I 0_UB |     | 69   | 35  | –   |     |
| --- | --- | --- | --- | ---------- | --- | ---- | --- | --- | --- |
|     |     |     |     | 3 • I 2_UB |     | 223  | 25  | –   |     |

|      |     |     |     | I     |     | 821  | 26  | –     |     |
| ---- | --- | --- | --- | ----- | --- | ---- | --- | ----- | --- |
| (b)  |     |     |     | L_UB  |     |      |     |       |     |
|      |     |     |     | 3 • I |     | 888  | 7   | 0.23  |     |
2_FLT
|     |     |     |     | 3 • I |     | 615  | 5   | 0.17  |     |
| --- | --- | --- | --- | ----- | --- | ---- | --- | ----- | --- |
0_FLT
|     |     |     |     | I   |     | 1793  | 3   | 0.10  |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- |
L_FLT
(with –7° tilt)
|     |     |     |     | I   |     | 4507  | 0   | –   |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
FLT
One of the ways to prevent overreach for faults during
|     |     |     |     | unbalanced  | operating  | conditions  | is  to  | use  incremental  |     |
| --- | --- | --- | --- | ----------- | ---------- | ----------- | ------- | ----------------- | --- |
quantities in the polarizing currents. The incremental polarizing

quantities are immune to the pre-fault conditions [21]. For the
Fig. 22.  Two-source power system with AG fault at remote end of the line,
fault in Fig. 22 (b) and the phasors shown in Table IX, the
a) without any phase open in the parallel line and b) with Phase A open in the
incremental negative- and zero-sequence polarizing quantities
parallel line.
are defined in (17) and (18).
Table VIII lists the fault current phasors for the AG fault in
|     |     |     |     |     | ∆(3•I | )=3•I |     |     |     |
| --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- |
Fig. 22 (a).  As  expected,  the  negative-  and  zero-sequence    −3•I   (17)
|     |     |     |     |     |     | 2   | 2_FLT | 2_UB |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- |
currents and the loop current with –7 degrees tilt have the same
|     |     |     |     |     | ∆(3•I | )=3•I | −3•I |     | (18)  |
| --- | --- | --- | --- | --- | ----- | ----- | ---- | --- | ----- |
angle as the fault current angle, resulting in no errors in the  0 0_FLT 0_UB
corresponding reactance element reach. Refer to Section I for  The use of these incremental polarizing quantities ensures
an explanation as to the effect of the polarizing current leading
|     |     |     |     | security  | of  the  | corresponding  | reactance  | elements  | during  |
| --- | --- | --- | --- | --------- | -------- | -------------- | ---------- | --------- | ------- |
or lagging the fault current on the reactance element reach.
|     |     |     |     | unbalanced  | conditions.  | However,  | the  main  | challenge  | with  |
| --- | --- | --- | --- | ----------- | ------------ | --------- | ---------- | ---------- | ----- |
incremental quantities is their application over a short data
TABLE VIII
CURRENT PHASORS FOR THE AG FAULT IN FIG. 22 (A) (WITHOUT ANY PHASE  window  and  their  dependency  on  the  pre-fault  current
OPEN IN THE PARALLEL LINE)  (magnitude and angle) that may be prone to change. These
Overreach (pu) in the  limitations can be overcome by implementing a predefined
|     | Magnitude  | Angle  |     |     |     |     |     |     |     |
| --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Phasor  Corresponding  polarizing quantity tilt angle determined by the maximum pre-
|     | (A Primary)  | (Deg.)  |     |     |     |     |     |     |     |
| --- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- |
Reactance Element  fault unbalanced current magnitude and the minimum fault
3 • I   505  0  0  current magnitude for which the quadrilateral distance element
2_FLT
is expected to pick up. Equations (19) and (20) define the
| 3 • I   | 505  | 0   | 0   |     |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
0_FLT
negative- and zero-sequence current tilt angles that ensure
I L_FLT  security of the corresponding reactance elements for faults
| (with –7° tilt)  | 1415  | 0   | 0   |     |     |     |     |     |     |
| ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
during unbalanced operating conditions.
| I FLT   | 4541  | 0   | –   |     |     |     |          |     |     |
| ------- | ----- | --- | --- | --- | --- | --- | -------- | --- | --- |
|         |       |     |     |     |     |     | max 3•I |    |     |
|         |       |     |     |     |     | −1 | 2_UB     |     |     |
Table IX  lists  the  current  phasors  for  the  AG  fault  in    θ =−tan    (19)
|     |     |     |     |     | 2_UB |     | min |    |     |
| --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- |
3•I
Fig. 22 (b). Note that Phase A of the parallel line is open during   2_FLT 
the fault. The negative- and zero-sequence currents and the loop
|     |     |     |     |     |     |     | max |    |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
3•I
current with –7 degrees tilt lead the total fault current phasor by  θ =−tan −1 0_UB 
|     |     |     |     |     | 0_UB |     |     |     | (20)  |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | ----- |
7, 5, and 3 degrees, respectively. The unbalanced condition  min 3•I 
|     |     |     |     |     |     |     |  0_FLT |    |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
(Phase A open in the parallel line) during the fault causes the
polarizing currents to lead the fault current angle, resulting in  Depending on the power system network configurations and
overreach  of  the  corresponding  reactance  elements.  From  unbalanced operating conditions, the tilt angles defined in (19)
and (20) can be significant, i.e., –40 degrees or more. Tilting
Table IX, we can easily conclude that the negative-sequence,
the reactance element characteristic by such a large angle can

13
drastically impact its dependability for typical faults (faults  unbalanced  operating  conditions;  however,  the  lower  fault
without unbalanced operating conditions). One way to increase  resistance coverage of the mho element reduces the scheme
security without sacrificing dependability is to set quadrilateral  dependability when the quadrilateral element is disabled.
elements to allow a small amount of pre-fault unbalance by
using a tilt angle smaller than the tilt angles defined by (19) or
(20), e.g., –10 degrees. If the pre-fault unbalanced current
magnitude exceeds the set limit, block the quadrilateral element
| while  having  | the  | corresponding  | mho  | element  | running  | in  |     |     |     |     |     |     |     |
| -------------- | ---- | -------------- | ---- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
parallel. This approach ensures the dependability of the Zone 1
distance elements. Some relays may include similar built-in
logic in the distance elements to ensure Zone 1 security for
faults during unbalanced operating conditions [22].

Fig. 23 shows the proposed logic of a simplified Zone 1
|     |     |     |     |     |     | Fig. 24.  | Simplified Zone 1 phase quadrilateral distance element logic for  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
ground quadrilateral distance element for unbalanced operating
small pre-fault unbalanced current.
conditions, assuming that the reactance element is polarized
with zero-sequence current. Replace the I  terms with I  in  The rising edge of (|3 • V 2 | > 5) in Fig. 24 indicates the
|     |     |     |     | 0   |     | 2          |         |             |         |        |      |      |          |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | ------- | ------ | ---- | ---- | -------- |
|     |     |     |     |     |     | inception  | of  an  | unbalanced  | fault,  | while  | the  | two  | current  |
Fig. 23, if the reactance element uses negative-sequence current
polarization.  The  logic  illustrated  in  Fig. 23,  disables  the  comparators  and  the  timer indicate  a  pre-fault  unbalanced
condition. If a previously balanced system experiences an
Zone 1 quadrilateral element if the pre-fault unbalanced current
unbalanced fault, the rising edge declaration expires before the
| magnitude  | (|3 • I |           | |)  exceeds  | (|3 • I |  • tan(θ | )|).  |     |     |     |     |     |     |     |
| ---------- | ------- | --------- | ------------ | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
|            |         | 0_PRE_FLT |              |         | 0        | UB    |     |     |     |     |     |     |     |
However, a small amount of pre-fault unbalanced current less  two-cycle  pickup  timer  times  out,  and  the  Zone 1  phase
quadrilateral element is not disabled. With an unbalanced pre-
| than or equal to (|3 • I |     |  • tan(θ | )|) is securely compensated for  |     |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | -------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                          |     | 0        | UB                               |     |     |     |     |     |     |     |     |     |     |
by adding a clockwise tilt, (θ ) (e.g., –10 degrees), in the  fault condition, followed by an unbalanced fault, the pickup
UB
timer output is already high when the rising edge declaration
| corresponding  | tilt          | angle    | setting.  When  | (|3 • I | 0_PRE_FLT      | |)  is  |           |         |                |     |          |                |     |
| -------------- | ------------- | -------- | --------------- | ------- | -------------- | ------- | --------- | ------- | -------------- | --- | -------- | -------------- | --- |
|                |               |          |                 |         |                | occurs  | and  the  | Zone 1  | quadrilateral  |     | element  | is  disabled.  |     |
| greater        | than  (|3 • I |  • tan(θ | )|),  the       | Zone 1  | quadrilateral  |         |           |         |                |     |          |                |     |
|                |               | 0        | UB              |         |                |         |           |         |                |     |          |                |     |
Appendix C includes the relay instructions to implement the
distance element is disabled; therefore, the corresponding mho
logic shown in Fig. 24.
element is expected to run in parallel to maintain dependability
of Zone 1 distance elements. Appendix C includes the relay
|     |     |     |     |     |     | X.  DETERMINING THE BEST TILT ANGLE FOR THE ZONE 1  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
instructions to implement the logic shown in Fig. 23.
REACTANCE ELEMENT
This section illustrates calculating the best tilt angle for the
negative-sequence, zero-sequence, and loop current polarized

Zone 1 reactance elements for the example system described in
Fig. 23.  Simplified Zone 1 ground quadrilateral distance element logic to
prevent overreach for faults during unbalanced operating condition.  Fig. 7. Table X lists the tilt angle compensation needed for each
of the factors affecting the security of the Zone 1 reactance
If the reactance elements use loop current polarization,
|     |     |     |     |     |     | elements.  | For  simplicity,  |     | the  Zone 1  | quadrilateral  |     | distance  |     |
| --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | ------------ | -------------- | --- | --------- | --- |
follow the approach described in Section III.C with various
elements are assumed to be configured with the proposed
unbalanced operating system contingencies to determine the
|     |     |     |     |     |     | unbalanced  | operating  | condition  |     | logic  | described  | in  | Fig. 24.  |
| --- | --- | --- | --- | --- | --- | ----------- | ---------- | ---------- | --- | ------ | ---------- | --- | --------- |
required tilt to secure the reactance element for faults during
|     |     |     |     |     |     | Therefore,  | no  tilt  | angle  | compensation  |     | is  considered  |     | for  |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ------ | ------------- | --- | --------------- | --- | ---- |
unbalanced operating conditions. An incremental ground loop
unbalanced operating conditions in Table X.
polarizing current is the summation of the incremental phase
All of the compensating tilt angles shown in Table X for
current and incremental ground current multiplied by the zero-
|                                 |     |     |                               |     |     | negative-sequence,  |     | zero-sequence,  |     | and  | loop  | polarizing  |     |
| ------------------------------- | --- | --- | ----------------------------- | --- | --- | ------------------- | --- | --------------- | --- | ---- | ----- | ----------- | --- |
| sequence compensation factor (k |     |     | ). The incremental phase and  |     |     |                     |     |                 |     |      |       |             |     |
0 quantities are calculated for line-end faults. For faults at the
ground currents follow the fault current angle; however, the
|            |                                               |     |     |     |     | Zone 1  | reach,  the  | required  | clockwise  |     | tilt  of  | the  reactance  |     |
| ---------- | --------------------------------------------- | --- | --- | --- | --- | ------- | ------------ | --------- | ---------- | --- | --------- | --------------- | --- |
| angle of k |  added to the incremental ground current may  |     |     |     |     |         |              |           |            |     |           |                 |     |
0 characteristic is smaller than the total clockwise tilt of the
| introduce  | significant  | difference  | between  | the  | angles  | of  the  |     |     |     |     |     |     |     |
| ---------- | ------------ | ----------- | -------- | ---- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
reactance characteristic needed for faults at the end of the line.
incremental loop current and total fault current. Therefore, the
|     |     |     |     |     |     | This  angle  | difference  |     | is  illustrated  |     | in  Fig. 25,  |     | where  |
| --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | ---------------- | --- | ------------- | --- | ------ |
use of incremental loop polarizing currents might work well for
|     |     |     |     |     |     | | < |θ   | |. In Fig. 25, Z |     |  is the positive-sequence line  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     | |θ T_Z1R | T_Z1L            |     | 1R                              |     |     |     |     |
the phase loops; however, using them for the ground loops may
|     |     |     |     |     |     | impedance corresponding to the Zone 1 reach, θ |     |     |     |     |     |     |  is the  |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- |
result  in  overreach  when  the  angle  of  the  zero-sequence  Z1L
|     |     |     |     |     |     | positive-sequence line impedance angle, θ |     |     |     |     |  is the total tilt  |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | ------------------- | --- | --- |
T_Z1L
| compensation factor (k |     | 0 ) is positive.  |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
angle of the reactance characteristic for faults at the end of the
Use the logic shown in Fig. 24 to disable the Zone 1 phase
|     |     |     |     |     |     | line and including the outgoing load effect, θ |     |     |     |     |     |  is the total  |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- |
quadrilateral distance element, even for the slightest pre-fault  T_Z1R
|                                     |     |     |              |                      |     | tilt angle for faults at the Zone 1 reach, and R |     |     |     |     | SET |  is the user- |     |
| ----------------------------------- | --- | --- | ------------ | -------------------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | ------------- | --- |
| unbalanced current given by (|3 • I |     |     | 0 | + |3 • I | 2 | > 0.05 • INOM),  |     |                                                  |     |     |     |     |     |               |     |
defined right resistance blinder setting.
| while  having  | the  | corresponding  | mho  | element  | running  | in  |     |     |     |     |     |     |     |
| -------------- | ---- | -------------- | ---- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
parallel to maintain Zone 1 dependability. Comparing this logic
to the logic shown in Fig. 23, we conclude that the logic in
Fig. 24 does not need any additional tilt to compensate for

14
TABLE X  Use the corresponding Equations (21), (22), or (23) to
FACTORS AFFECTING THE SECURITY OF THE ZONE 1 REACTANCE ELEMENTS
determine the best tilt angles for the negative-sequence, zero-
AND CORRESPONDING TILT ANGLE COMPENSATION FOR THE FIG. 7 EXAMPLE
|     |     |     |     | sequence,  | and  | loop  | current  | polarized  | Zone 1  | reactance  |     |
| --- | --- | --- | --- | ---------- | ---- | ----- | -------- | ---------- | ------- | ---------- | --- |
SYSTEM
elements. Set the tilt angle setting meant for ground and phase
| Factors  | Tilt Angle Compensation for Reactance  |     |     |     |     |     |     |     |     |     |     |
| -------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reactance loops to the corresponding best tilt angle. In [9], set
| Affecting Zone 1  | Elements Polarized With  |     |     |     |     |     |     |     |     |     |     |
| ----------------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the TANG setting to the corresponding best tilt angle.
Reactance
|          | Negative- | Zero-     | Loop     |     |     |        |         |        |      |     |       |
| -------- | --------- | --------- | -------- | --- | --- | ------ | ------- | ------ | ---- | --- | ----- |
| Element  |           |           |          |     | θ   |        | =θ      | −θ     | +θ   |     | (21)  |
|          | Sequence  | Sequence  | Current  |     |     | 2_BEST | 2_T_Z1R | L_LOAD | 2_NW |     |       |
Security
|                 | Current   | Current   |              |     |     |        |         |         |      |     |       |
| --------------- | --------- | --------- | ------------ | --- | --- | ------ | ------- | ------- | ---- | --- | ----- |
|                 |           |           |              |     | θ   |        | =θ      | −θ      | +θ   |     | (22)  |
|                 |           |           |              |     |     | 0_BEST | 0_T_Z1R | L_LOAD  | 0_NW |     |       |
| Network         | –10°      | –12°      | (Tilt angle  |     |     |        |         |         |      |     |       |
| nonhomogeneity  |           | (θ0_NW )  | included in  |     |     |        | θ       | =θ      |      |     | (23)  |
|                 | (θ2_NW )  |           |              |     |     |        | L_BEST  | L_T_Z1R |      |     |       |
maximum
|     |     |     | outgoing load  | where:  |     |     |     |     |     |     |     |
| --- | --- | --- | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
factor)
|     |     |     |     |     |     |     | q  | −Im(Z | )  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
[k]
| Maximum outgoing  | NA  | NA  | –34°        | θ         |     | =tan−1 |       | 1R    |    |     |     |
| ----------------- | --- | --- | ----------- | --------- | --- | ------- | ----- | ----- | --- | --- | --- |
|                   |     |     |             | [k]_T_Z1R |     |         |       | −Re(Z | )  |     |     |
| load (without     |     |     | (θL_LOAD )  |           |     |         |  p   |       |     |     |     |
|                   |     |     |             |           |     |         |  [k] | 1R    |    |     |     |
unbalanced
| operating  |     |     |     | [k]={0,2,L}  |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
conditions)
|                      |              |              |              |     |      |       | (         | )     |           |        |     |
| -------------------- | ------------ | ------------ | ------------ | --- | ---- | ----- | --------- | ----- | --------- | ------ | --- |
|                      |              |              |              |     | Im(Z | )−tan | θ         |       | •Re(Z )+R | •tan(θ | )   |
| VT and CT (steady    | –7°          | –7°          | –7°          |     |      | 1L    | [k]_T_Z1L |       | 1L        | SET    | Z1L |
| state angle errors)  |              |              |              | p   | =    |       |           |       |           |        |     |
|                      | (θ2_VT_CT )  | (θ0_VT_CT )  | (θL_VT_CT )  | [k] |      |       |           |       | (         | )      |     |
|                      |              |              |              |     |      |       | tan(θ     | )−tan | θ         |        |     |
|                      |              |              |              |     |      |       |           | Z1L   | [k]_T_Z1L |        |     |
| Line charging        | 0°           | 0°           | –1°          |     |      |       |           |       |           |        |     |
current  (θ2_LCC )  (θ0_LCC )  (θL_LCC )  =tan(θ )•p −R •tan(θ )
|                    |      |      |     | q   | [k] | Z1L | [k] | SET | Z1L |     |      |
| ------------------ | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| Untransposed line  | –2°  | –1°  | 0°  |     |     |     |     |     |     |     |      |
|                    |      |      |     | θ   |     | =θ  | +θ  | +θ  | +θ  |     | +θ   |
(θ2_UNTR )  (θ0_UNTR )  (θL_UNTR )  [k]_T_Z1L L_LOAD [k]_VT_CT [k]_LCC [k]_UNTR [k]_UB
Unbalanced  0°  0°  0°  θ   contains  θ   which  also  includes  network
|            |           |           |           | [k]_T_Z1L |     |     | L_LOAD |     |     |     |     |
| ---------- | --------- | --------- | --------- | --------- | --- | --- | ------ | --- | --- | --- | --- |
| operating  | (θ2_UB )  | (θ2_UB )  | (θL_UB )  |           |     |     |        |     |     |     |     |
nonhomogeneity compensation for both negative-sequence and
conditions*
|     |     |     |     | zero-sequence  |     | polarizing  |     | quantities.  | Therefore,  | θ   |     |
| --- | --- | --- | --- | -------------- | --- | ----------- | --- | ------------ | ----------- | --- | --- |
[k]_T_Z1R
Total Tilt  –19°  –20°  –42°  (derived from θ ) requires further modifications in order
[k]_T_Z1L
* Zone 1 quadrilateral distance elements are assumed to be disabled for  to  properly  compensate  the  negative-sequence  or
unbalanced operating conditions based on the logic described in Fig. 24.  zero-sequence  polarizing  quantities  individually.  Equations
Therefore, no tilt angle compensation is needed for any of the polarizing
|     |     |     |     | (21)  and  | (22)  | add  | the  | corresponding  | θ 2_NW |   and  | θ 0_NW   |
| --- | --- | --- | --- | ---------- | ----- | ---- | ---- | -------------- | ------ | ------ | -------- |
quantities for unbalanced operating conditions.
|     |     |     |     | nonhomogeneity compensation angles and subtract θ |     |     |     |     |     |     |  in  |
| --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
L_LOAD
both equations due to the insensitivity of negative-sequence and
zero-sequence currents to load flow.
For the Fig. 7 example system, Fig. 26 shows the plots of the
best tilt angles for the negative-sequence, zero-sequence, and
loop current polarized Zone 1 reactance elements for different
|     |     |     |     | values of R | SET |  obtained from (21), (22), and (23), respectively.  |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
As expected, the best tilt angles in Fig. 26 approach the
|     |     |     |     | corresponding total tilt angles of Table X as the value of R |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
SET
|     |     |     |     | increases. Fig. 26 illustrates that, as R |     |     |     |     |  increases, the required  |     |     |
| --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | ------------------------- | --- | --- |
SET
clockwise tilt angle to keep the reactance element secure also
increases. This observation is important because selecting the
appropriate current polarized clockwise tilt angle from Fig. 26
affects the fault resistance coverage.

| Fig. 25.  Tilt angles for faults at the Zone 1 reach (θT_Z1R |     |     | ) and at the end of  |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
the line (θT_Z1L ).

15
Knowledge of the effect of clockwise tilt of the reactance
characteristic on the fault resistance coverage and maximum
fault resistance that a given line may experience is useful in
|     |     |     |     | determining R |     |  and tilt angle settings. Choose an appropriate  |     |     |     |     |     |
| --- | --- | --- | --- | ------------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
SET
|     |     |     |     | R SET  and its corresponding clockwise tilt angle from the best tilt  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
angle plots, such as the ones shown in Fig. 26, derived for that
|     |     |     |     | particular  | line.  | Using  | this  | R SET   with  | the  | corresponding  |     |
| --- | --- | --- | --- | ----------- | ------ | ------ | ----- | ------------- | ---- | -------------- | --- |
clockwise tilt angle for the reactance element characteristic
enhances the resistive coverage and ensures security of the
Zone 1 reactance element.
|     |     |     |     |     |     | XI.  | CONCLUSION  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | --- | --- | --- |
The reactance element defines the reach of the quadrilateral
|     |     |     |     | distance        | element.  | The             | combination  |            | of  reactance  | element   |        |
| --- | --- | --- | --- | --------------- | --------- | --------------- | ------------ | ---------- | -------------- | --------- | ------ |
|     |     |     |     | characteristic  |           | with  adequate  |              | clockwise  | tilt           | and  the  | right  |
resistance blinder ensures security of the Zone 1 quadrilateral
|     |     |     |     | distance  | element  | for  resistive  |     | faults.  | Factors  | like  network  |     |
| --- | --- | --- | --- | --------- | -------- | --------------- | --- | -------- | -------- | -------------- | --- |
nonhomogeneity, line loading, VT and CT steady-state angle
|     |     |     |     | errors,     | line    | charging   | currents,      | untransposed  |             | lines,     | zero- |
| --- | --- | --- | --- | ----------- | ------- | ---------- | -------------- | ------------- | ----------- | ---------- | ----- |
|     |     |     |     |   sequence  | mutual  | coupling,  |                | and           | unbalanced  | operating  |       |
|     |     |     |     | conditions  | may     | result     | in  reactance  |               | element     | overreach  | for   |
Fig. 26.  Best tilt angles for negative-sequence, zero-sequence, and loop
current polarized Zone 1 reactance elements for different values of R  for  resistive faults. Typically, overreach of the Zone 1 reactance
SET
the Fig. 7 example system.  element for resistive line-end faults is compensated through
|     |     |     |     | clockwise  | tilt  | of  the  | reactance  | characteristic.  |     | This  | paper  |
| --- | --- | --- | --- | ---------- | ----- | -------- | ---------- | ---------------- | --- | ----- | ------ |
Fig. 27 illustrates the effect of the clockwise tilt of the
reactance characteristic on the fault resistance coverage. A  describes how to set the tilt angle of the reactance characteristic
to add security to Zone 1 of quadrilateral distance elements
| lower  clockwise  | tilt  of  the  reactance  | characteristic  | (A  in  |     |     |     |     |     |     |     |     |
| ----------------- | ------------------------- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 27) increases fault resistance coverage near the reactance  without sacrificing operating time for resistive faults and a
given right resistance blinder setting.
reach; however, it decreases fault resistance coverage for the
This paper describes conditions and provides equations to
rest of the protected zone. This assessment is true because the
right resistance blinder (R  in Fig. 27) has to be set lower  determine an adequate negative- and zero-sequence network
SET_A
nonhomogenous correction angle. The conditions include faults
for lower clockwise tilt angles. Whereas, a higher clockwise tilt
of the reactance characteristic (in Fig. 27) may have reduced  at the Zone 1 reach and the end of the line with a weak source
impedance behind the relay and the strongest source impedance
fault resistance coverage near the reach; however, it has high
fault resistance coverage for the rest of the protected zone. This  beyond the remote bus.
Mutual coupling does affect the zero-sequence polarizing
| assessment is true because the right resistance blinder (R |     |     | SET_B |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
current angle; however, proper use of the equations provided in
in Fig. 27) can be set higher with higher clockwise tilt angles.
this paper compensates for that effect. Special considerations
|     |     |     |     | are  described  |     | in  this  | paper  | to  determine  |     | nonhomogenous  |     |
| --- | --- | --- | --- | --------------- | --- | --------- | ------ | -------------- | --- | -------------- | --- |
correction angles for lines with impedance angles less than
70 degrees.
Line loading does not affect negative- and zero-sequence
current polarization. However, it has significant impact on loop
current polarization, especially for outgoing loading conditions.
|     |     |     |     | This  paper  | recommends  |        | simulating  |            | line-end  | faults    | with    |
| --- | --- | --- | --- | ------------ | ----------- | ------ | ----------- | ---------- | --------- | --------- | ------- |
|     |     |     |     | maximum      | outgoing    | power  |             | flow  for  | all       | possible  | source  |
impedances and different fault resistances to determine the loop
|     |     |     |     | current  | polarization  | tilt  | angle  | solely  | for  outgoing  |     | loading  |
| --- | --- | --- | --- | -------- | ------------- | ----- | ------ | ------- | -------------- | --- | -------- |
conditions.
This paper provides an equation to calculate the error in the
reactance element reach as a function of VT and CT steady-
state angle errors. This equation shows that for given VT and
CT angle errors, the reach error of the reactance element
increases significantly as the fault resistance increases. This
paper recommends simulating metallic line-end faults with
  heavy loading and the weakest source behind the relay to
Fig. 27.  Effect of the clockwise tilt of the reactance characteristic on the  determine  an  adequate  clockwise  tilt  angle  required  to
fault resistance coverage.
compensate for VT and CT angle errors. This paper also shows

16
that the polarizing currents may have higher angle errors than    I =I +I   (28)
|     |     |     |     |     |     |     |     |     |     |     | 2S 2L | 2P  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
the steady-state CT angle error in the faulted phase current.
Substituting (27) in (28), we get:
When CT saturation for line-end faults causes overreach, secure
Zone 1 by appropriately reducing its reach.    I =2•I −(1−m)•I   (29)
|     |     |     |     |     |     |     |     |     |     | 2S  | 2L  |     | 2F  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The tilt angle setting needed to compensate for line charging
current and line transpositions can be in the order of a couple
of degrees. This paper defines an approach to determine this
compensation.
Faults during unbalanced operating conditions are probably
rare; however, they can significantly impact the security of the
| current  | polarized  | reactance  | element.  |     | This  paper  | describes  |     |     |     |     |     |     |     |     |     |
| -------- | ---------- | ---------- | --------- | --- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
various approaches to compensate for unbalanced operating
| conditions.  | The  | simplest  | approach  |     | is  to  block  | Zone 1  |     |     |     |     |     |     |     |     |     |
| ------------ | ---- | --------- | --------- | --- | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
quadrilateral elements for faults during unbalanced operating
| conditions,  | while  | having  | the  | corresponding  |     | mho  element  |     |     |     |     |     |     |     |     |     |
| ------------ | ------ | ------- | ---- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
running in parallel.
Lastly, this paper provides an expression to determine the
best tilt angle for a given right resistance blinder setting to

enhance the fault resistance coverage and ensure security of the
Fig. 29.  Star-configuration impedances from the delta-configuration
Zone 1 quadrilateral distance element.
impedances of Fig. 28.
From Fig. 28,
XII.  APPENDIX A
(1−m)•Z
| Deriving Expression for Negative-Sequence  |     |     |     |     |     |     |     |     |     |     |     | 2L  |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+Z
|     |     |     |     |     |     |     |     |     |     |     | 2   |     | 2R  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Nonhomogenous Network Correction Angle for Parallel    I = •I   (30)
|                     |     |     |     |     |     |     |     |     |     | 2S  | Z    |     | 2F  |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
| Line Configuration  |     |     |     |     |     |     |     |     |     |     | 2L   |     |     |     |     |
|                     |     |     |     |     |     |     |     |     |     | Z   | +    | +Z  |     |     |     |
|                     |     |     |     |     |     |     |     |     |     |     | 2S 2 | 2R  |     |     |     |
Fig. 28 shows a negative-sequence network for a fault at
distance  m  from  the  local  terminal  in  a  parallel  line  Equating (29) and (30), and solving for I  / I , results in:
|                 |     |     |     |     |     |     |     |     |      |          |     |       | 2L  | 2F   |       |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- | ----- | --- | ---- | ----- |
| configuration.  |     |     |     |     |     |     |     |     |      | (1−m)•(Z |     |       | )+Z |      |       |
|                 |     |     |     |     |     |     |     |     | I    |          | +Z  | +Z    |     |      |       |
|                 |     |     |     |     |     |     |     |     | 2L = |          | 2S  | 2L    | 2R  | 2R   | (31)  |
|                 |     |     |     |     |     |     |     |     | I    |          |    | Z     |    |      |       |
|                 |     |     |     |     |     |     |     |     | 2F   | 2•Z     | +   | 2L +Z | 2R |      |       |
2S
|     |     |     |     |     |     |     |     |     |     |     |    | 2   |    |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
From(31),
|     |     |     |     |     |     |     |     |     |         |          |     |     |     |     |          |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | --- | --- | --- | --------- |
|     |     |     |     |     |     |     |     |     |         | (1−m)•(Z |     |     |     |     |          |
|     |     |     |     |     |     |     |     | I  |        |           |     | +Z  | +Z  | )+Z |           |
|     |     |     |     |     |     |     |     | 2F  | =−arg |           |     | 2S  | 2L  | 2R  | 2R (32)  |
  arg
|     |     |     |     |     |     |     |           | I  |       |            |      |      | Z                  |     |    |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----- | ----------- | ----- | ---- | ------------------ | ---- | --- |
|     |     |     |     |     |     |     |           | 2L  |      |             | 2• Z | +    | 2L +Z              |      |     |
|     |     |     |     |     |     |     |           |     |       |            |       | 2s   |                    | 2R  |    |
|     |     |     |     |     |     |     |           |     |       |            |      |      | 2                  |     |    |
|     |     |     |     |     |     |     | Equation  |     | (32)  | represents  |       | the  | negative-sequence  |      |     |
nonhomogenous network correction angle for a parallel line

|     |     |     |     |     |     |     | configuration  |     | having  |     | two  lines,  | originating  |     | from  | and  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | --- | ------------ | ------------ | --- | ----- | ---- |
Fig. 28.  Negative-sequence network for a fault at distance m from the relay
terminating on a common bus.
in a parallel line configuration.
Equating negative-sequence voltage drops from the local
|     |     |     |     |     |     |     |     |     |     | XIII.  | APPENDIX B  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | --- | --- | --- |
bus to the remote bus through protected line and parallel line,
| we get:  |     |         |       |          |     |         |     | Deriving an Expression for Error in the Reactance  |     |     |     |     |     |     |     |
| -------- | --- | ------- | ----- | -------- | --- | ------- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|          |     |         |       | −(1−m)•I |     |         |     | Element Reach                                      |     |     |     |     |     |     |     |
|          | I   | •Z =m•I | •Z    |          | •Z  |   (24)  |     |                                                    |     |     |     |     |     |     |     |
|          | 2P  | 2L      | 2L 2L |          | 2R  | 2L      |     |                                                    |     |     |     |     |     |     |     |
Consider a fault at a distance m per unit from the relay, as
| Simplifying (24), we get:  |     |     |     |     |     |     | shown in Fig. 30.  |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
−(1−m)•I
|     |     | I   | =m•I |     |     | (25)  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 2P  | 2L   |     | 2R  |       |     |     |     |     |     |     |     |     |     |
From Fig. 28,
|     |     |     | I =I +I | −I  |     | (26)  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 2R 2P   | 2F  | 2S  |       |     |     |     |     |     |     |     |     |     |
Substituting (26) in (25), results in:

−(1−m)•I
|     |     | I   | =I  |     |     | (27)  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2P 2L 2F Fig. 30.  Two-source power system with a fault at a distance m per unit from
| From Fig. 28,  |     |     |     |     |     |     | the relay.  |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |

17
The voltage V at the relay location can be expressed as: The result of these assumptions is shown in (40).
L
V =m•Z •I +I •R (33) m+δm V +δV Z I
L 1L L F F ≈ L L • 1L • L •
Multiplying both the sides of the previous equation by the m V L Z 1L +δZ 1L I L +δI L
conjugate of the fault current I and taking imaginary parts to ( ) ( )
F 1+cot θ −θ • δθ −δθ
solve for m, we get:
VL P VL P
( ) ( )
1+cot θ +θ −θ • δθ +δθ −δθ
ImV •I *−ImI •R •I * IL Z1L P IL Z1L P
 L F   F F F 
m= (34) (40)
ImZ •I •I *
 L L F  We assume that the loop current angle θ follows the fault
IL
current angle θ . However, even if there is significant
We know, ImI •R •I *=0, IF
 F F F  difference between the two, the term cot(θ IL + θ Z1L – θ P ) •
(δθ + δθ – δθ ) in the denominator of (40) shall be less
IL Z1L P
Im  V L •I F *  than one; therefore, neglecting it, results in:
∴m= (35)
Im

Z
1L
•I
L
•I
F
*

m+δm
≈
V
L
+δV
L •
Z
1L •
I
L •
m V Z +δZ I +δI
In polar form, the previous equation can be written as L 1L 1L L L (41)
( ) 1+cot ( θ −θ ) • ( δθ −δθ )
m=
V
L
•sin θ
VL
−θ
IF
(36)
 VL P VL P 
( )
Z •I •sin θ +θ +θ To get the amount of overreach for a fault at the end of the
1L L Z1L IL IF
line, substitute m = 1 in (41) and substituting θ by θ as
P IF
In (36), θ IF is the fault current angle. Assume the polarizing assumed in (37).
current angle with appropriate tilt (θ ) is same as the fault
P
V +δV Z I 
current angle. Substituting θ IF by θ P in (36), we get  L L • 1L • L •
V •sin ( θ −θ ) δm≈   V L Z 1L +δZ 1L I L +δI L  −1 (42)
m= Z •I L •sin ( θ VL +θ P −θ ) (37)     1+cot ( θ VL −θ IF ) • ( δθ VL −δθ P )   
1L L Z1L IL P
Equation (42) provides an approximate expression for the
The primary and relay CTs introduce magnitude and angle
error in the reactance reach. Negative values of δm indicate
errors in the loop and polarizing currents. Similarly, the primary
overreach, whereas positive values mean underreach.
and relay VTs introduce magnitude and angle errors in the
Assuming negligible error in the magnitudes of the faulted
faulted phase voltage. The line parameters may also be
phase voltage, line impedance, and loop current, the error in the
erroneous. Considering all these errors in (37), results in an
reactance reach in (42) is solely because of VT and CT steady-
error of the reactance reach δ as expressed in (38).
m
state angle errors and is expressed as:
V +δV
m+δm= L L • ( ) ( )
(Z
1L
+δZ
1L
)•(I
L
+δI
L
) δm IT_ANG ≈cot θ VL −θ IF • δθ VL −δθ P (43)
( ) (38)
sin θ +δθ −θ −δθ where:
VL VL P P
sin ( θ +δθ +θ +δθ −θ −δθ ) (θ V – θ P ) is the angle difference between the faulted phase
Z1L Z1L IL IL P P voltage at the relay location and the total fault current, (θ
P
Dividing equation (38) by (37), results in: is assumed to be the total fault current angle, or else
include that error in δθ ).
m+δm V +δV Z •I P
= L L • 1L L • δθ is the error in the faulted phase voltage angle
m (Z +δZ )•(I +δI ) V VL
L 1L L L L because of the primary and relay VTs.
sin ( θ +δθ −θ −δθ ) δθ P is the error in the polarizing current angle because of
VL VL P P
• (39) the primary and relay CTs, or in other words, it is the
( )
sin θ Z1L +δθ Z1L +θ IL +δθ IL −θ P −δθ P angle difference between the relay calculated polarizing
( ) current and total fault current.
sin θ +θ −θ
Z1L IL P Note that (43) is an approximate expression and therefore
( )
sin θ −θ may have numerical errors if the simplifying assumptions made
VL P
in (39) are violated. However, (43) is still valuable for
Simplifying (39) with the following assumptions:
illustrating the effect of instrument transformer angle errors on
• The angle error (δθ + δθ – δθ ) is less than
IL Z1L P reach estimation.
20 degrees; therefore, cos(δθ + δθ – δθ ) ≈ 1, and
IL Z1L P CT saturation results in reduced magnitude and a leading
sin(δθ + δθ – δθ ) ≈ (δθ + δθ – δθ ).
IL Z1L P IL Z1L P phase angle shift of the affected current phasor [18]. Assuming
• Similarly, the angle error (δθ VL – δθ IF ) is less than negligible error in the magnitude and angle of the faulted phase
20 degrees; therefore, cos(δθ VL – δθ IF ) ≈ 1, and voltage and in the magnitude of line impedance, the error in the
sin(δθ – δθ ) ≈ (δθ – δθ ).
VL IF VL IF

18
reactance reach in (42) is solely because of CT saturation and  3.  Relay instructions for the logic described in Fig. 23
is expressed as:  for Zone 1 quadrilateral phase-distance element with
negative-sequence current polarization for the
|        |     |  I    |         |     |     |         |     |     |                                    |     |     |     |     |     |     |
| ------ | --- | ------- | ------- | --- | --- | ------- | ----- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
|        |     | L       | •1−cot | (   | )   | •(δθ ) |       |     | reactance element.                 |     |     |     |     |     |     |
|   δm   | ≈  |         |         | θ   | −θ  |         |  −1  |     |                                    |     |     |     |     |     |     |
| CT_SAT |     | I +δI |        | VL  | IF  | P       |    |     |                                    |     |     |     |     |     |     |
|        |     | L L     |         |     |     |         |       |     | PMV07 := 240.000000 # ENTER CTRW.  |     |     |     |     |     |     |
PSV07 := R_TRIG 3V2FIM > 5.000000 # INDICATES
|     |     |     |     |     |     |     | (44)  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
INCEPTION OF UNBALANCED FAULT.
where:
PSV08 := 3V2FIM > 5.000000 # UNBALANCED FAULT.
δI L  is the error in the loop current magnitude because of  PMV08 := L3I2M * PSV07 / PMV07 + PMV08 * PSV08 #
CT saturation.
PRE-FAULT NEGATIVE SEQ.  CURRENT MAG.
δθ P  is the error in the polarizing current angle because of  PMV09  :=  L3I2FIM  *  0.176327  #  TAN(10  DEG)  =
CT saturation, or in other words, is the angle difference
|     |     |     |     |     |     |     |     |     | 0.176327.  | REMEMBER  |     | TO  ADD  | ADDITIONAL  |     | -10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | -------- | ----------- | --- | ---- |
between the relay calculated polarizing current and the
DEG. CLOCKWISE TILT IN THE TANGP SETTING
total fault current.
FOR THIS LOGIC.
Note (44) may not be accurate for severe CT saturation
PSV09 := PMV09 > PMV08 AND PSV07
conditions because the angle error assumptions made when  PSV10  :=  PSV09  OR  NOT  32QE  #  USE  PSV10  IN
| deriving (42) may get violated. However, the parameters (δI |     |                                                 |     |     |     |     |     | ,   |          |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
|                                                             |     |                                                 |     |     |     |     |     | L   | Z1XPTC.  |     |     |     |     |     |     |
| θ , θ , and δθ                                              |     | ) in (44) affecting the error in the reactance  |     |     |     |     |     |     |          |     |     |     |     |     |     |
VL IF P 4.  Relay instructions for the logic described in Fig. 24
reach because of CT saturation still stand true.
for Zone 1 quadrilateral ground- and phase-distance
element.
|     |     | XIV.  | APPENDIX C  |     |     |     |     |     | PMV10 := LIGFIM + L3I2FIM  |     |     |     |     |     |     |
| --- | --- | ----- | ----------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
Relay Instructions to Implement the Logic Shown in  PMV11 := 0.200000 * 3.000000 * LI1FIM
Fig. 23 and Fig. 24  PMV12 := 0.050000 * 5.000000 # MULTIPLER 5 IS FOR
Note that PMV and PSV used in this section are IEEE 32-bit  5A INOM RELAY. USE 1 for 1A INOM RELAY.
PSV11 := PMV10 > PMV11 AND PMV10 > PMV12
floating-point and Boolean variables, respectively.
1.  Relay instructions for the logic described in Fig. 23  PCT01IN := PSV11 # INPUT TO TIMER PCT01
|     |     |     |     |     |     |     |     |     | PCT01PU  | :=  | 2.000000  | #  TWO  | POWER  | SYSTEM  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------- | ------- | ------ | ------- | --- |
for Zone 1 quadrilateral ground distance element with
CYCLES PICKUP DELAY.
zero-sequence current polarization for the reactance
| element.  |     |     |     |     |     |     |     |     | PCT01DO := 0.000000 # 0 DROP OUT DELAY.  |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
PSV12 := R_TRIG 3V2FIM > 5.000000 # INDICATES
PMV01 := 240.000000 # ENTER CTRW.
PSV01 := R_TRIG 3V2FIM > 5.000000 # INDICATES  INCEPTION OF UNBALANCED FAULT.
PSV13 := 3V2FIM > 5.000000 # UNBALANCED FAULT.
INCEPTION OF UNBALANCED FAULT.
PSV14 := PCT01Q AND PSV12 OR PSV14 AND PSV13
PSV02 := 3V2FIM > 5.000000 # UNBALANCED FAULT.
PMV02 := LIGM * PSV01 / PMV01 + PMV02 * PSV02 #  # USE PSV14 IN Z1XGTC.
|     |     |     |     |     |     |     |     |     | PSV15  :=  | PSV14  | OR  NOT  | 32QE  | #  USE  | PSV16  | IN  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | -------- | ----- | ------- | ------ | --- |
PRE-FAULT GROUND CURRENT MAGNITUDE.
| PMV03      | :=        | LIGFIM  | *  0.176327  |      | #  TAN(10   |     | DEG)  | =   | Z1XPTC.  |     |     |     |     |     |     |
| ---------- | --------- | ------- | ------------ | ---- | ----------- | --- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- |
| 0.176327.  | REMEMBER  |         | TO           | ADD  | ADDITIONAL  |     | -10   |     |          |     |     |     |     |     |     |
REFERENCES
| DEG. CLOCKWISE TILT IN THE TANGG SETTING  |     |     |     |     |     |     |     |      |                                                                        |     | XV.  |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------------------------------------------------------------------- | --- | ---- | --- | --- | --- | --- |
|                                           |     |     |     |     |     |     |     | [1]  | A. R. van C. Warrington, Protective Relays: Their Theory and Practice  |     |      |     |     |     |     |
FOR THIS LOGIC.
Volume One, Chapman and Hall, Ltd., London, 1962.
PSV03 := PMV03 > PMV02 AND PSV02 # USE PSV03
IN Z1XGTC.  [2]  J. B. Roberts, A Guzmán, and E. O. Schweitzer, III, “Z = V/I Does Not
Make a Distance Relay,” proceedings of the 20th Annual Western
2.  Relay instructions for the logic described in Fig. 23
Protective Relay Conference, Spokane, WA, October 1993.
for Zone 1 quadrilateral ground distance element with
|     |     |     |     |     |     |     |     | [3]  | C. Henville and R. Chowdhury, “Coordination of Resistive Reach of  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
negative-sequence current polarization for the  Phase and Ground Distance Elements,” proceedings of the 48th Annual
reactance element.  Western Protective Relay Conference, Spokane, WA, October 2021.
PMV04 := 240.000000 # ENTER CTRW.  [4]  GEI-98339E Directional Ground Distance Relay Instructions, Type
GCXG51A11 & Up, GE Power Management.
PSV04 := R_TRIG 3V2FIM > 5.000000 # INDICATES
|     |     |     |     |     |     |     |     | [5]  | E. O. Schweitzer, III, and J. B. Roberts, “Distance Relay Element  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
INCEPTION OF UNBALANCED FAULT.
Design,” proceedings of the 19th Annual Western Protective Relay
PSV05 := 3V2FIM > 5.000000 # UNBALANCED FAULT.  Conference, Spokane, WA, October 1992.
PMV05 := L3I2M * PSV04 / PMV04 + PMV05 * PSV05 #
|     |     |     |     |     |     |     |     | [6]  | W.  Schossig,  | “Distance  | Protection  |     | From  Protection  | Relays  | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------------- | ---------- | ----------- | --- | ----------------- | ------- | --- |
PRE-FAULT NEGATIVE SEQ. CURRENT MAG.  Multifunctional,” Protection, Automation & Control World, Vol. 04,
Spring 2008, pp. 71–76.
| PMV06  | :=  | L3I2FIM  | *  0.176327  |     | #  TAN(10  |     | DEG)  | =   |     |     |     |     |     |     |     |
| ------ | --- | -------- | ------------ | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
0.176327.  REMEMBER  TO  ADD  ADDITIONAL  -10  [7]  G. Ziegler, Numerical Distance Protection: Principles and Applications,
2nd Edition, Publicis Corporate Publishing, Erlangen, Germany, 2006.
DEG. CLOCKWISE TILT IN THE TANGG SETTING
|     |     |     |     |     |     |     |     | [8]  | F. Calero, A. Guzmán, and G. Benmouyal, “Adaptive Phase and Ground  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
FOR THIS LOGIC.
|     |     |     |     |     |     |     |     |     | Quadrilateral  | Distance  | Elements,”  | proceedings  | of  | the  36th  | Annual  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | ----------- | ------------ | --- | ---------- | ------- |
PSV06 := PMV06 > PMV05 AND PSV05 # USE PSV06  Western Protective Relay Conference, Spokane, WA, October 2009.
IN Z1XGTC.

19
[9] SEL-421-4, -5 Protection, Automation, and Control System Instruction Idaho in power system protection and power system stability. Since 1993, he
Manual. Available: selinc.com. has been with Schweitzer Engineering Laboratories, Inc. in Pullman,
[10] B. Kasztenny, “Settings Considerations for Distance Elements in Line Washington, where he is a distinguished engineer. He holds numerous patents
in power system protection, fault locating, and monitoring. He is a senior
Protection Applications,” proceedings of the 74th Annual Conference for
member of IEEE.
Protective Relay Engineers, College Station, TX, March 2021.
[11] F. Calero, “Mutual Impedance in Parallel Lines – Protective Relaying and
Steven Chase received his bachelor of science degree in electrical engineering
Fault Location Considerations,” proceedings of the 34th Annual Western
from Arizona State University in 2008 and his master of science degree in
Protective Relay Conference, Spokane, WA, October 2007.
electrical engineering in 2009. He worked for two years as a substation design
[12] D. A. Tziouvaras, H. J. Altuve, and F. Calero, “Protecting Mutually intern at Salt River Project, an Arizona water and power utility. He joined
Coupled Transmission Lines: Challenges and Solutions,” proceedings of Schweitzer Engineering Laboratories, Inc. (SEL) in 2010, where he works as a
the 67th Annual Conference for Protective Relay Engineers, College senior power engineer in the research and development division. He is currently
Station, TX, March 2014. a registered PE in the state of Washington.
[13] R. Jimerson, A. Hulen, R. Chowdhury, N. Karnik, and B. Matta,
“Application Considerations for Protecting Three-Terminal Transmission Brian Smyth received a B.S.E.E. and M.S.E.E. from Montana Tech at the
Lines,” proceedings of the 74th Annual Conference for Protective Relay University of Montana in 2006 and 2008, respectively. He joined Montana Tech
Engineers, College Station, TX, March 2021. as a visiting professor in 2008 and taught classes in electrical circuits, electric
[14] H. J. Altuve, J. B. Mooney, and G. E. Alexander, “Advances in Series- machinery, instrumentation and controls, and power system analysis. He joined
Schweitzer Engineering Laboratories, Inc. (SEL) in 2009 as an associate power
Compensated Line Protection,” proceedings of the 35th Annual Western
engineer in the research and development division. Brian is currently a senior
Protective Relay Conference, Spokane, WA, October 2008.
engineer in the transmission department and is the co-inventor of two patents.
[15] J. Vargas, A. Guzmán, and J. Robles, “Underground/Submarine Cable
In addition to working for SEL, Brian joined Montana Tech in 2014 as an
Protection Using a Negative-Sequence Directional Comparison Scheme,” Affiliate Professor, where he teaches courses in power system protection. He
proceedings of the 26th Annual Western Protective Relay Conference, received the Distinguished Alumni award from Montana Tech in 2016 and the
Spokane, WA, October 1999. IEEE Southwest Montana Chapter Engineer of the Year award in 2017. He is
[16] D. Tziouvaras, J. Roberts, G. Benmouyal, and D. Hou, “The Effect of an active IEEE member and a registered professional engineer in the state of
Conventional Instrument Transformer Transients on Numerical Relay Washington.
Elements,” proceedings of the 28th Annual Western Protective Relay
Conference, Spokane, WA, October 2001.
[17] E. O. Schweitzer, III, K. Behrendt, and T. Lee, “Digital Communications
for Power System Protection: Security, Availability, and Speed,”
proceedings of the 25th Annual Western Protective Relay Conference,
Spokane, WA, October 1998.
[18] J. Mooney, “Distance Element Performance Under Conditions of CT
Saturation,” proceedings of the 61st Annual Conference for Protective
Relay Engineers, College Station, TX, April 2008.
[19] R. Chowdhury, D. Finney, N. Fischer, and D. Taylor, “Determining CT
Requirements for Generator and Transformer Protective Relays,”
proceedings of the 46th Annual Western Protective Relay Conference,
Spokane, WA, October 2019.
[20] K. Dase and N. Fischer, “Computationally Efficient Methods for
Improved Double-Ended Transmission Line Fault Locating,”
proceedings of the 45th Annual Western Protective Relay Conference,
Spokane, WA, October 2018.
[21] G. Benmouyal and J. Roberts, “Superimposed Quantities: Their True
Nature and Application in Relays,” proceedings of the 26th Annual
Western Protective Relay Conference, Spokane, WA, October 1999.
[22] SEL-T401L Ultra-High-Speed Line Relay Instruction Manual. Available:
selinc.com.
XVI. BIOGRAPHIES
Kanchanrao Dase received his bachelor of engineering degree in electrical
engineering in 2009 from Sardar Patel College of Engineering, University of
Mumbai, India. He received his master of science degree in electrical
engineering from Michigan Technological University, Houghton, MI, in 2015.
From 2009 to 2014, he was a manager at Reliance Infrastructure Limited with
a substation engineering and commissioning profile. Currently, he is working
with Schweitzer Engineering Laboratories, Inc. (SEL) as a lead power engineer.
His research interests include power system protection, substation automation,
and fault locating. He currently hold five patents in power system protection
and fault locating.
Armando Guzmán (M ’95, SM ’01) received his BSEE with honors from
Guadalajara Autonomous University (UAG), Mexico. He received a diploma
in fiber-optics engineering from Monterrey Institute of Technology and
Advanced Studies (ITESM), Mexico, and his Master of Science and PhD in
electrical engineering and Master of Engineering in computer engineering from
the University of Idaho, USA. He served as regional supervisor of the
© 2022 by Schweitzer Engineering Laboratories, Inc.
Protection Department in the Western Transmission Region of the Federal
All rights reserved.
Electricity Commission (the electrical utility company of Mexico) in
20221013 • TP7074-01
Guadalajara, Mexico for 13 years. He lectured at UAG and the University of