|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Waveform Characterization of Animal Contact,
Tree Contact, and Lightning Induced Faults
Saurabh Kulkarni, Duehee Lee, Alicia J. Allen, Surya Santoso, Thomas A. Short
  proposed in [6] for fault classification. The method used in [7]
Abstract—In this paper signal processing tools are used to  uses rough-cloud theory to tackle the problem of abundance
uncover common and unique characteristics of faults resulting
and uncertainty of PQ data. Furthermore, a comparison of
from animal contacts, tree contacts and lightning.  For each fault  deterministic and statistical fault classification techniques is
| type a large number of voltage and current waveform data sets  |     |     |     |     |     |     |     | presented in [8].   |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
measured  at  monitoring  stations  on  distribution  systems  are    On the contrary to the above discussion, not much work has
analyzed.  The characteristics include but are not limited to the
been done in waveform characterization of fault events, which
| presence  | of  impulse-like  | oscillations,  |     | the  | number  | of  | phases  |     |     |     |     |     |     |     |     |
| --------- | ----------------- | -------------- | --- | ---- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
is the first step towards root-cause analysis. The goal of this
involved, the duration of fault event, the phase angle, the time of
day, the spectral content in the time-frequency and time-scale  paper is to utilize the waveform characteristics of fault events
domains, the rate of rise of voltage or current, and the arc  to  distinguish  between  different fault  types.  The  approach
| voltage.  | An  individual  | characteristic  |     | alone  | is  | insufficient  | to  |     |     |     |     |     |     |     |     |
| --------- | --------------- | --------------- | --- | ------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
taken is to identify, extract and analyze characteristics of fault
provide an estimate of the fault type. However, by combining
events based on their waveforms. These characteristic can be
common and unique characteristics extracted from a fault event,
common to many faults types or unique (differentiating) to a
it may be possible to estimate the fault type accurately.
  particular fault type. A number of characteristics are explored
in this paper, namely, time of occurrence of fault, number of
Index Terms—Diagnosis (fault), power distribution faults, power
quality, power system monitoring, power system lightning effects,  affected  phases,  fault  phase  angle,  time  duration  of  fault,
vegetation, animals, wavelet transforms  frequency content, and arc voltage. Some the characteristics
like the number of affected phases and time duration of fault
I.  INTRODUCTION
|     |     |     |     |     |     |     |     | are  common  | to  | all  fault  | types.  | On  | the  other  | hand,  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | ------- | --- | ----------- | ------ | ---- |
POWER quality or PQ disturbances on distribution lines are  characteristics like time of occurrence and arc voltage can be
caused by a number of factors [1] and can be internal or  effectively employed to distinguish between fault types. The
external.  Internal events are primarily the result of equipment  main contribution of this paper is that it provides a set of
characteristics that can be extracted from any voltage and
| malfunction  | or  failure,  | while  | external  |     | disturbances  |     | occur  |     |     |     |     |     |     |     |     |
| ------------ | ------------- | ------ | --------- | --- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
mainly due to animal and bird contacts, tree contacts, vehicle  current  waveforms  obtained  from  a  PQ  monitor.  A
accidents as well as natural phenomena like lightning. The  combination  of  these  characteristics,  rather  than  any  one
power quality monitoring stations that detect the deviations  individual characteristic, can be used to uniquely identify the
caused by these events store a snapshot of the voltage and  root-cause of the PQ events.
current  waveforms.    This  captured  data  possesses  a  large  The introduction to the paper was provided in Section I.
amount of information that can be analyzed to identify the  The PQ data used in this paper is described in Section II.
root-cause of the disturbance.    Sections III to VIII describe the characteristic signatures based
  A significant amount of work has been carried out in the  on, time stamp, fault insertion angle, number of phases, time
areas  of  fault  diagnosis,  root-cause  identification  and  duration, wavelet transforms and arc voltage, respectively.
automatic classification of power quality disturbance events.  The conclusion is presented in section IX.
| The  use  | of  wavelet  | domain  |     | analysis  | for  | fault  | cause  |     |     |     |     |     |     |     |     |
| --------- | ------------ | ------- | --- | --------- | ---- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
identification is proposed in [2]. In addition, a number of  II.  DATA SOURCE FOR POWER QUALITY DISTURBANCES
| artificial  | neural  network  |     | based  | fault-cause  |     | identification  |     |            |           |     |           |            |           |       |     |
| ----------- | ---------------- | --- | ------ | ------------ | --- | --------------- | --- | ---------- | --------- | --- | --------- | ---------- | --------- | ----- | --- |
|             |                  |     |        |              |     |                 |     | The  data  | analyzed  |     | in  this  | paper  is  | obtained  | from  | PQ  |
methodologies have been traditionally discussed in literature
monitoring stations located in an electric supply utility in the
[3]. For example, in [4] supervised clustering based neural
|     |     |     |     |     |     |     |     | Northeastern  | part  | of  the  | United  | States.  | The  | utility  | has  a  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | -------- | ------- | -------- | ---- | -------- | ------- |
networks are used to distinguish between faults and system
|     |     |     |     |     |     |     |     | network  | consisting  | of  | overhead  | power  | lines  | and  | also  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | --------- | ------ | ------ | ---- | ----- |
conditions that appear like faults. A power distribution fault
underground cables. The PQ data set has 143 tree contact
| cause  classifier  | developed  |     | in  [5]  | makes  | use  | of  logistic  |     |     |     |     |     |     |     |     |     |
| ------------------ | ---------- | --- | -------- | ------ | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
regression and artificial neural networks. A hybrid wavelet  cases, 66 animal contact cases and 28 lightning-induced cases.
|         |                  |         |          |     |        |           |     | Lightning-induced  |     | cases  | refer  | to  all  | the  events  | that  | had  |
| ------- | ---------------- | ------- | -------- | --- | ------ | --------- | --- | ------------------ | --- | ------ | ------ | -------- | ------------ | ----- | ---- |
| domain  | and  artificial  | neural  | network  |     | based  | approach  | is  |                    |     |        |        |          |              |       |      |
lightning as the primary cause and not necessarily a direct
                                                            lightning strike. The cause of the fault is identified by the
 S. Kulkarni, D. Lee, A. Allen and S. Santoso are with The Department  utility after conducting a physical survey of the fault site. The
of Electrical and Computer Engineering at The University of Texas at Austin.
cause of the fault is assumed as a fact throughout the paper.
T. Short is with the Electric Power Research Institute (EPRI), Burnt Hills,
|     |     |     |     |     |     |     |     | The  PQ  | monitor  | waveforms  | at  | various  | voltage  | levels  | are  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---------- | --- | -------- | -------- | ------- | ---- |
NY.

978-1-4244-6551-4/10/$26.00 ©2010 IEEE

|     |     |     |     |     |     |     |     |     |     | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sampled at the rate of 128 samples per cycle. Generally, the  a  large  presence  of  nocturnal  animals,  the  graph  will  be
sampling window contains 10 cycles with the fundamental  opposite to Fig. 2. 64% of the tree contact cases occur during
frequency of 60 Hz. The PQ data is analyzed based on the  the day, while three quarters of the lightning induced events
characteristic signatures explained in the following sections.   occur after the sun has set.
III.  CHARACTERISTIC SIGNATURE: TIME STAMP  IV.  CHARACTERISTIC SIGNATURE: FAULT INSERTION ANGLE
The  first  signature  is  based  on  the  time  stamp  of  the  Fault insertion angle can be defined as the angle of the
disturbance. Even though this is not an electrical quantity, it  normal sine wave at the disturbance initiation point. Initially,
provides  vital  clues  considering  that  power  quality  it  was  construed  that  the  tree  contact  and  animal  contact
disturbances are influenced by the weather conditions seasonal  triggered events would start around the peak of the sine wave
as the voltage gradient between the animal/tree branch and the
and diurnal cycles.  For example, lightning is associated with
thunderstorms  which  generally  occur  in  late  spring  and  power line is highest at the peak.  Fig. 3 and Fig. 4 show an
animal contact and tree contact event, respectively, occurring
summer.  Animal and bird contacts associated with power
near the positive peak of the sine wave. For the animal contact
lines are more common during the migratory season. A similar
case the fault occurs in phase A, while in the tree contact case
analysis for animal contact events was presented in [9]. Based
phase B is affected. The inception of the fault is characterized
on the month of occurrence, events are classified into four
by a sudden sag in the voltage and a corresponding rise in the
types; Summer (June-August), Fall (September- November),
current of the same phase above the normal operating value.
Winter (December-February) and Spring (March -May). Fig. 1
However, it was found that some lightning induced events
shows this normalized seasonal classification.
also occur at the peak of the sine wave as shown in Fig. 5.  In
100.00 this case the fault inception is at the negative peak of the
85.71
|     | 80.00 |     |     |     |     | voltage waveform and phase C is affected.   |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- |
65.73
| stnevE fo % |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
60.00
42.42
|     | 40.00 |               |     |        |     |     | 20  |         |     |     |
| --- | ----- | ------------- | --- | ------ | --- | --- | --- | ------- | --- | --- |
|     |       | 24.24  21.21  |     | 24.48  |     |     |     | Voltage |     | Va  |
10
|     | 20.00 | 12.12  |       |       | 10.71  |       |      | peak |     | Vb  |
| --- | ----- | ------ | ----- | ----- | ------ | ----- | ---- | ---- | --- | --- |
|     |       |        | 5.59  | 4.20  | 3.57   | 0.50  |      |      |     |     |
|     |       |        |       |       |        |       | Vk 0 |      |     | Vc  |
0.00
-10
|     |     | Animal Contact | Tree Contact |     | Lightning |     |     |     |     |     |
| --- | --- | -------------- | ------------ | --- | --------- | --- | --- | --- | --- | --- |
-20
|     | Spring | Summer |     | Fall | Winter |     | 0   | 0.05 | 0.1 0.15 | 0.2 |
| --- | ------ | ------ | --- | ---- | ------ | --- | --- | ---- | -------- | --- |
time(s)
|     |     |     |     |     |     |     | 5   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 1.  Normalized Seasonal Distribution of Animal Contact, Tree Contact  Fault Ia
inception
| and Lightning Events  |     |     |     |     |     |     |     |     |     | Ib  |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ic
Ak 0
| About  | 85%  | of  lightning  |     | induced  | disturbances  | occur  in  |     |     |     |     |
| ------ | ---- | -------------- | --- | -------- | ------------- | ---------- | --- | --- | --- | --- |
summer, which happens to be the time of the year when
-5
thunderstorms are common.  On the contrary, 65% tree contact  0 0.05 0.1 0.15 0.2

time(s)
events occur during fall when the wind is generally stronger  Fig. 3.  Animal Contact Event Occurring at Voltage Peak
and the trees are losing their leaves.  Animal contact events
are spread nearly evenly in spring and fall, with a majority
|                                  |     |     |     |     |     |     | 20  |         |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
| (42.42%), occurring in summer.   |     |     |     |     |     |     |     | Voltage |     | Va  |
10
|     |         |        |     |     |     |     |      | peak |     | Vb  |
| --- | ------- | ------ | --- | --- | --- | --- | ---- | ---- | --- | --- |
|     | 100.00  | 88.03  |     |     |     |     |      |      |     |     |
|     |         |        |     |     |     |     | Vk 0 |      |     | Vc  |
75.00
| stnevE fo % |     |     |     | 64.37 |     |     |     |     |     |     |
| ----------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
-10
|     | 50.00  |     |     |       |     |     | -20 |      |          |     |
| --- | ------ | --- | --- | ----- | --- | --- | --- | ---- | -------- | --- |
|     |        |     |     | 35.66 |     |     | 0   | 0.05 | 0.1 0.15 | 0.2 |
26.61
time(s)
|     |       | 12.12          |              |     |           |     | 10  |           |     |     |
| --- | ----- | -------------- | ------------ | --- | --------- | --- | --- | --------- | --- | --- |
|     |       |                |              |     |           |     |     | Fault     |     | Ia  |
|     | 0.00  |                |              |     |           |     | 5   |           |     |     |
|     |       |                |              |     |           |     |     | inception |     | Ib  |
|     |       | Animal Contact | Tree Contact |     | Lightning |     |     |           |     | Ic  |
Ak 0
|     |     |     |     | Daytime | Night time |     |     |     |     |     |
| --- | --- | --- | --- | ------- | ---------- | --- | --- | --- | --- | --- |
|     |     |     |     |         |            |     | -5  |     |     |     |
Fig. 2.  Normalized Classification of Animal Contact, Tree Contact and
-10
| Lightning Events based on time of day  |     |     |     |     |     |     | 0   | 0.05 | 0.1 0.15 | 0.2 |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- |
|                                        |     |     |     |     |     |     |     |      | time(s)  |     |
Fig. 4.  Tree Contact Event Occurring at Voltage Peak
Based on the time of day, events are classified as shown in
Fig. 2. The disturbances between 6:00 am and 7:00 pm are
categorized as ‘daytime’ events while ‘night time’ events are
those that occur between 7:00 pm and 6:00 am. Nearly 90% of
the animal contact triggered events occur during the daytime.
This number is influenced by the kind of animals present in
the geographical region of the utility. If a particular utility has

|     |     |     |     |     |     |     |     |     |     |     | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLE II
|     | 20  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
NUMBER OF AFFECTED PHASES
Va
10
Vb
|     |     |     |     |     |     | Vc  | Event  |     | Single phase  | Multiphase faults  | Total  |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------------- | ------------------ | ------ |
Vk 0
|     |     |         |     |     |     |     |                 |     | faults       |             | cases  |
| --- | --- | ------- | --- | --- | --- | --- | --------------- | --- | ------------ | ----------- | ------ |
|     | -10 | Voltage |     |     |     |     |                 |     |              |             |        |
|     |     |         |     |     |     |     | Animal Contact  |     | 53 (86.88%)  | 8 (13.12%)  | 61     |
|     |     | peak    |     |     |     |     |                 |     |              |             |        |
-20
0 0.05 0.1 0.15 0.2 Tree Contact  66 (73.33%)  24 (26.67%)  90
|     |     |     |     | time(s) |     |     |                    |     |             |              |     |
| --- | --- | --- | --- | ------- | --- | --- | ------------------ | --- | ----------- | ------------ | --- |
|     | 10  |     |     |         |     |     |                    |     |             |              |     |
|     |     |     |     |         |     |     | Lightning Induced  |     | 8 (42.10%)  | 11 (57.90%)  | 19  |
Ia
5
|     |      |     |     |     |     | Ib  |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Ak 0 |     |     |     |     | Ic  |     |     |     |     |     |
As many as 53 out of 61 animal contact events and 66 out
|     | -5  | Fault  |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of 90 tree contact events, i.e. more than 70%, are single phase
inception
-10   faults.  On the other hand, roughly 60% lightning induced
|     | 0   | 0.05 |     | 0.1 | 0.15 | 0.2 |     |     |     |     |     |
| --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
time(s)   events are multiphase.  As in the case of the fault insertion
Fig. 5.  Lightning Induced Event Occurring at Voltage Peak
angle, the number of phases involved is not a characteristic
signature of any particular event. Further research needs to be
The fault insertion angle results for a total of 170 cases are
conducted in order to better utilize this feature.
summarized in Table I, while 67 cases were found to be
ambiguous.  Ambiguous cases are mostly those in which the
VI.  CHARACTERISTIC SIGNATURE: TIME DURATION
| waveforms  |     | obtained  | from  | PQ  monitoring  | station  |     | do  not  |     |     |     |     |
| ---------- | --- | --------- | ----- | --------------- | -------- | --- | -------- | --- | --- | --- | --- |
contain the required prefault data.  If the fault insertion angle  Characteristically  lightning  induced  events  are  high-
is between 15° of the positive or negative peak (±90°) of the  frequency  transients  having  higher  energy  content  as
sine wave, the event is said to have an inception at the peak.   compared to contact triggered events.  The AC resistance and
All other events have an off-peak fault insertion angle.   line  impedance  of  an  overhead  conductor  is  directly
  proportional  to  increasing  frequency  [10].  This  increased
TABLE I
opposition to the flow of higher frequency currents makes
FAULT INSERTION ANGLE
high frequency transients like lightning die down faster as
compared to relatively lower frequency transients like those
|     | Event  | Insertion angle  |     | Off-peak Insertion  |     | Total  |     |     |     |     |     |
| --- | ------ | ---------------- | --- | ------------------- | --- | ------ | --- | --- | --- | --- | --- |
around peak  angle    cases  due to tree/animal contact triggered disturbances. However,
Animal Contact  43 (70.5%)  18 (29.5%)  61  this may not always be the case as seen in Fig. 5 where the
  lightning-induced fault in phase C lasts for several cycles. Fig.
Tree Contact  66 (73.33%)  24 (26.67%)  90  6 shows a tree contact event in which the fault in phase A is

temporary and has duration of just one cycle, because the tree
| Lightning Induced  |     | 16 (84.21%)  |     | 3 (15.79%)  |     | 19  |     |     |     |     |     |
| ------------------ | --- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
branch initiating the fault burns and falls to the ground, before

any protective device operates.
About 70% of the animal and tree contact events have the
fault insertion angle near the peak. However, it is observed
|     |     |     |     |     |     |     |     | 20  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that roughly 85% of lightning induced events also started near  Va
10
the voltage peak. This is because the cases analyzed in this  Vb
|        |      |                    |     |             |          |     |         | Vk 0 |     |     | Vc  |
| ------ | ---- | ------------------ | --- | ----------- | -------- | --- | ------- | ---- | --- | --- | --- |
| paper  | are  | lightning-induced  |     | faults  as  | opposed  | to  | direct  |      |     |     |     |
-10
lightning stroke events which can occur at any phase angle.
| Hence,  | the  | breakdown  | point  | for  lightning-induced  |     |     | events,  | -20   |      |          |     |
| ------- | ---- | ---------- | ------ | ----------------------- | --- | --- | -------- | ----- | ---- | -------- | --- |
|         |      |            |        |                         |     |     |          | 0     | 0.05 | 0.1 0.15 | 0.2 |
unlike direct strikes, is also the voltage peak. Thus, being  time(s)
|            |         |      |       |                    |        |       |      | 10  |     |     |     |
| ---------- | ------- | ---- | ----- | ------------------ | ------ | ----- | ---- | --- | --- | --- | --- |
| initiated  | around  | the  | peak  | of  a  sinusoidal  | wave,  | with  | the  |     |     |     |     |
Ia
available data set, does not seem to be a very unique feature of  5 Ib
| any particular group.    |     |     |     |     |     |     |     | Ak  |     |     | Ic  |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
V.  CHARACTERISTIC SIGNATURE: NUMBER OF PHASES
-5
|     |     |     |     |     |     |     |     | 0   | 0.05 | 0.1 0.15 | 0.2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- |
A  fault  can  affect  one,  two,  or  all  three  phases  of  a  time(s)
distribution feeder.  The number of phases involved in the  Fig. 6.  Tree Contact Event Lasting for One Cycle
fault depends on the cause of the fault. Generally, animal and
From the above examples it is clear that the time duration
tree contacts tend to affect only one phase and hence these
of the fault cannot be recognized as a unique characteristic of
| events  | are  | single  line  | to  | ground  faults.  | On  | the  contrary,  |     |     |     |     |     |
| ------- | ---- | ------------- | --- | ---------------- | --- | --------------- | --- | --- | --- | --- | --- |
any particular event. The duration of the fault is determined by
lightning has the likelihood of affecting all three phases of the
the operation of the overcurrent protective device interrupting
power line. The number of faulted phases is found out for all
the fault, rather than the cause itself.
| the  | 170  cases  | and  | the  results  | are  given  | in  | Table  | II.  A  |     |     |     |     |
| ---- | ----------- | ---- | ------------- | ----------- | --- | ------ | ------- | --- | --- | --- | --- |
disturbance affecting only one phase is called a single phase
VII.  CHARACTERISTIC SIGNATURE: WAVELET TRANSFORMS
fault, while if two or three phases are affected the event is
categorized as a multi-phase fault.    A lightning event can have one or more current pulses or
  strokes. The current stroke penetrates into the power system at
the strike point and may be followed by one or more strokes.

4
The entire flash event occurs in a very short period, usually in
few hundreds of microseconds. Induced voltage and current
transients propagates away from the strike point and are
captured by PQ monitors. Regardless of the location of PQ
monitors, i.e., upstream or downstream from the lightning
current injection, as long as they are located within the
affected area, voltage and current waveforms should be
captured almost simultaneously by all. Lightning induced
waveforms may look quite different depending on the distance
between the strike point and the PQ monitor. PQ monitors
near the strike point are likely to capture high frequency
oscillations at the initiation of the disturbance. While, those at
different voltage levels or some electrical distance apart are Fig. 9. Three-phase Voltage and Current Waveforms of Lightning Event
unlikely to capture these high frequency oscillations, since Captured at 13.8 kV System by Monitor AC-AP
overhead lines and transformers are inductive.
Wavelet transform can be used to analyze and uncover the
Fig. 7 and Fig. 8 show two sets of three-phase voltage and
spectral content in the time-scale domain. In this paper,
current waveforms caused by a lightning stroke on a 161-kV
orthogonal-dyadic wavelet transform is applied [11]. Only one
system at 10:01:22.000. Monitor T, downstream from strike,
phase is analyzed since results from other phases are similar.
did not see the high current, while Monitor W-C, upstream
Voltage waveform is normalized and decomposed into three
from strike, saw it. Appreciable oscillatory transients (2.2
wavelet analysis scales; Scale 1(1920-3840 Hz), Scale 2(960-
kHz) were present during the initiation of the disturbance. Fig.
1920 Hz), Scale 3(480-960 Hz). They represent the time-scale
9 shows a set of waveforms due to the same lightning stroke
energy spectra of the time domain signal.
captured by a PQ monitor at a 13.8-kV system. The voltage
The discrete wavelet transform of the waveform captured
and current waveforms are smooth and do not have an
by Monitor W-C (Fig. 8) is shown in Fig. 10. The wavelet
appreciable oscillatory transient.
transform of the Monitor AC-AP is computed on similar lines.
Trinity 161 - 11/23/2004 10:01:22.000
200000
100000
0
-100000
-200000
400
200
0
-200
-400
0.00 0.05 0.10 0.15 0.20 0.25
Electrotek/EPRI PQView®
Fig. 7. Three-phase Voltage and Current Waveforms of Lightning Event
Captured at 161-kV System. Monitor T Downstream from Lightning Stroke.
Fig. 10. A Three-scale Wavelet Transform of Lightning induced Voltage
Waveform Captured by Monitor W-C (161 kV)
By analyzing the wavelet transforms it was clear that
transients with high frequency contents appear in lower scales
while those with lower frequency content appear in higher
scales. Comparing the square of the transform outputs, on a
scale by scale basis, for the voltage waveform captured by
Monitor W-C, the maximum energy in scale 1, 2, and 3 is
1.7×10-2, 4.3×10-2, and 5.4×10-2 , respectively. In contrast, the
voltage waveform captured by Monitor AC-AP has maximum
Fig. 8. Three-phase Voltage and Current Waveforms of Lightning Event energies in the first two scales as 2.6×10-3 and 7.8×10-4, while
Captured at 161-kV System. Monitor W-C Upstream from Lightning Stroke.
there is no meaningful maximum energy information in the
third scale. These results indicate that lightning induced
waveforms may be identifiable in the wavelet domain if a PQ
monitor is near the strike point. Lightning induced waveforms
captured by remote PQ monitors can be identified indirectly
through the use of time-proximity cross-correlation approach
and other identifying signatures described in this paper.
)V(
egatloV
)A(
tnerruC
Monitor T
Vab Vbc Vca Ia Ib Ic
Time (s)
Weyerhaeuser - Columbus - 11/23/2004 10:01:22.000
200000
100000
0
-100000
-200000
600
400
200
0
-200
-400
0.00 0.02 0.04 0.06 0.08 0.10 0.12
Electrotek/EPRI PQView®
)V(
egatloV
)A(
tnerruC
Albertville City AlbertvillePrimary - 11/23/2004 10:01:22.000
10000
5000
0
-5000
-10000
400
200
0
-200
-400
0.00 0.02 0.04 0.06 0.08 0.10 0.12
Electrotek/EPRI PQView®
Monitor W-C
Vab Vbc Vca Ia Ib Ic
Time (s)
)V(
egatloV
)A(
tnerruC
Monitor AC-AP
Va Vb Vc Ia Ib Ic
Time (s)
1
0.5
0
-0.5
0 0.02 0.04 0.06 0.08 0.1 0.12
Vk
egatlov
0.02
0.01
0 0 0.02 0.04 0.06 0.08 0.1 0.12 0.14
2.egatlov
0.04
0.02
0
0 0.02 0.04 0.06 0.08 0.1 0.12
2.egatlov
0.05
0
0 0.02 0.04 0.06 0.08 0.1 0.12
2.egatlov
Scale 1: 1920 –3840 Hz
Scale 2: 960 -1920 Hz
Scale 3: 480 –960 Hz
time (msec)

|     |     |     |             |     |     |     |     |     |     |     |     |     |     |     | 5   |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | Monitor C-C |     |     |     |     |     |     |     |     |     |     |     |     |
Cullman-Colbert Cullman Primary - 7/7/2005 14:32:56.000
The wavelet transforms for Monitor AC-AP is computed
|     |     | Va  | Vb  | Vc  | Ia Ib | Ic  |     |     |          |         |      |               |           |           |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | -------- | ------- | ---- | ------------- | --------- | --------- | --- |
|     |     |     |     |     |       |     |     | on  | similar  | lines.  | For  | the  voltage  | waveform  | captured  | by  |
100000
Monitor C-C (161 kV), the maximum energy in scale 1, 2, and
)V( egatloV
|     |     |     |     |     |     |     |     |     | 2.1×10-3,  |     | 1.39×10-2,  | 3.3×10-2,  |     |                |       |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | ---------- | --- | -------------- | ----- |
|     |     | 0   |     |     |     |     |     | 3   | is         |     |             | and        |     | respectively.  |   In  |
contrast, in the voltage waveform captured by Monitor AC-
-100000
AP, the maximum energy in each scale is 9.4×10-7, 1.28×10-5,
100 and 1.2×10-4.  Comparing these values to those shown earlier
)A( tnerruC
0 for a lightning event; scale 1 value for a voltage waveform
-100 (captured  at  161  kV)  caused  by  a  lightning  event  is
approximately 10 times higher than that for a tree-contact
0.00 0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 event (captured at 161 kV also).  For scale 2 and 3 values, they
|     |     |     |     | Time (s) |     |     | PQView®  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Electrotek/EPRI are comparable. Using very limited waveform samples, it is
Fig. 11.  Three-phase Voltage and Current Waveforms of Multiple Tree
Contacts Captured at 161-kV System (Monitor C-C)  observed  that  lightning  events  appear  to  possess  higher
  frequency content than tree contact events.  This is reasonable
Tree contact events also have a number of wave shapes and  given the fact that lightning tends to have higher frequency
are dependent on the voltage level where the tree contact
|     |     |     |     |     |     |     |     | due  | to  | the  travelling  |     | wave  phenomena  |     | arising  | from  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---------------- | --- | ---------------- | --- | -------- | ---------- |
occurs. Fig. 11 and Fig. 12 show simultaneous tree contacts  discontinuity  (from  a  piece  of  equipment  to  another)
captured by Monitor C-C (161 kV) and AC-AP (13.8 kV),  encountered during pulse propagation.
respectively.  Unlike tree contacts on distribution lines, they
generally do not result in a permanent fault.  Waveforms
VIII.  CHARACTERISTIC SIGNATURE: ARC VOLTAGE
| captured  |     | at  transmission  |     | system  | level  do  | possess  | more  |     |     |     |     |     |     |     |     |
| --------- | --- | ----------------- | --- | ------- | ---------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
When an object (tree or animal), is about to be in contact
| significant  |     | transients  | than  | those  captured  |     | at  a  distribution  |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | ----- | ---------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with the power lines, there may be an electric arc struck in the
system level. This is because inductive elements (transformers
medium (generally air) between the object and the line [12].
| and  | overhead  | lines)  | of  | the  power  | system  | offer  | higher  |      |                  |     |     |                 |     |                    |      |
| ---- | --------- | ------- | --- | ----------- | ------- | ------ | ------- | ---- | ---------------- | --- | --- | --------------- | --- | ------------------ | ---- |
|      |           |         |     |             |         |        |         | The  | characteristics  |     | of  | the  arc  such  | as  | the  arc  length,  | arc  |
impedance at a higher frequency. The square of the wavelet
impedance and arc voltage hold crucial information about the
transform of voltage waveform captured by Monitor C-C is
cause of the disturbance [13] [14].  Arguably, the arc voltage
shown in Fig. 13. The frequency of the decomposition scale is
is the most important characteristic out of all the above and
the same as the one used for lightning-induced events.
can be used as a signature of the power quality disturbance.

Based on the algorithm proposed in [15] [16], the arc voltage
|     |     | Albertville City AlbertvillePrimary - 7/7/2005 14:32:38.000 |     | Monitor AC-AP |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------------------------------------------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is assumed to be a square wave in phase with the current. The
|     |     | Va  | Vb  | Vc  | Ia Ib | Ic  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10000 algorithm is applicable to single phase faults and it estimates
)V( egatloV 5000 the arc voltage in the affected phase.  It is assumed that the
0
line impedance parameters are unknown.  The single line
-5000
diagram for a faulted circuit can be represented as shown in
-10000
|     |     | 600 |     |     |     |     |     | Fig. 14.  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
400
|     | )A( tnerruC |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
200
0
-200
-400
-600
|     |     | 0.01 | 0.02 0.03 | 0.04 0.05 | 0.06 0.07 | 0.08 0.09 |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --------- | --------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time (s)
|     | Electrotek/EPRI |     |     |     |     | PQView® |     |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 12.  Three-phase Voltage and Current Waveforms of Multiple Tree
Contacts Captured at 13.8-kV System (Monitor AC-AP)

|     | Vk egatlov 1 |     |     |     |     |     |     | Fig. 14.  Circuit for Arc Voltage Estimation  |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | 0            |     |     |     |     |     |     |                                               |     |     |     |     |     |     |     |
-1 The voltage at the PQ monitoring site, V  for the faulted
|     |     | 0 0.01 | 0.02 | 0.03 0.04 0.05 | 0.06 | 0.07 0.08 |     |     |     |     |     |     |     | F   |     |
| --- | --- | ------ | ---- | -------------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
phase can be written as shown in (1). This equation is applied
x 10-3
2 at  every  point  of  the  voltage  and  current  waveform.  The
|     | 2.egatlov |     |     | Scale 1: 1920 –3840 Hz |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     |     |     |     |     |     | overdetermined  |     |     | system  | of  equations  | is  | solved  using  | least  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ------- | -------------- | --- | -------------- | ------ |
0
0 0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 square method to obtain the peak value of the arc voltage, V .
arc
2.egatlov
|     | 0.01  |        |      | Scale 2: 960 -1920 Hz |      |           |     |     |     |     |      | ⎛d I ⎞       |            |     |     |
| --- | ----- | ------ | ---- | --------------------- | ---- | --------- | --- | --- | --- | --- | ---- | ------------ | ---------- | --- | --- |
|     | 0.005 |        |      |                       |      |           |     |     |     | V   | =R×I | +L⎜⎜ F ⎟⎟ +V | arc×sign(I | )   |     |
|     |       |        |      |                       |      |           |     |     |     |     | F    | F            |            | F   | (1) |
|     | 0     |        |      |                       |      |           |     |     |     |     |      | ⎝ d t ⎠      |            |     |     |
|     |       | 0 0.01 | 0.02 | 0.03 0.04 0.05        | 0.06 | 0.07 0.08 |     |     |     |     |      |              |            |     |     |
V   is the fault phase voltage measured at PQ monitoring
|     | 2.egatlov |     |     | Scale 3: 480 –960 Hz |     |     |     |     | F   |     |     |     |     |     |     |
| --- | --------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.02
|     |     |     |     |     |     |     |     |     | site I | is the fault current   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------------------- | --- | --- | --- | --- | --- |
F
0 0 0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 L is the line inductance
|     |     |     |     | time (msec) |     |     |     |     | R is the line resistance   |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
Fig. 13.  Three-scale Wavelet Decomposition of Tree-contact Voltage
V arc  is the peak arc voltage at the fault location
Waveform Captured by Monitor C-C (161 kV)

  6
|     | sign (I | ) = 1 , if I |  > 0 and -1 if I |  ≤ 0        |     |     |     |     |     |     |     |     |
| --- | ------- | ------------ | ---------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |         | F            | F                | F           |     |     |     |     |     |     |     |     |
|     |         |              |                  |             |     |     | 1   |     |     |     |     |     |
eulav sixa-X eht naht ssel stneve fo noitroP
|                                                               | Animal and tree contact triggered events involve physical  |     |     |     |     |     | 0.9 |     |     |     |     |     |
| ------------------------------------------------------------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| contact of an object with power lines and hence tend to have  |                                                            |     |     |     |     |     | 0.8 |     |     |     |     |     |
an arc voltage higher than events induced by lightning strokes.
0.7
Peak arc voltage estimates for animal contact (Fig. 3), tree
0.6
contact (Fig. 4) and lightning induced events (Fig. 5) are
0.5
shown in Fig. 15 , Fig. 16 and Fig. 17, respectively.
0.4
2.5
0.3
|     | 2   |     |     |     |     |     | 0.2 |     |     |     | Animal Contact |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
)Vk( egatloV crA
Cable Failure
|     | 1.5 |     |     |     |     |     | 0.1 |     |     |     | Lightning |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
Tree contact
|     | 1   |     |     |     |     |     | 0 0   | 200 400 600 | 800 | 1000 1200 | 1400 1600 | 1800 2000 |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | --------- | --------- | --------- |
Arc Voltage (V)

0.5 Fig. 18.  Normalized Arc Voltage Distribution for Animal Contact, Tree
Contact and Lightning Events
0
|     | 0   | 0.02 | 0.04 0.06 0.08 | 0.1 0.12 0.14 | 0.16 0.18 0.2 |     |     |     |     |     |     |     |
| --- | --- | ---- | -------------- | ------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
  It is observed that lightning induced events have the least
time(s)
Fig. 15.  Arc Voltage in Phase A for Animal Contact Event shown in Fig. 3
arc voltage among the three categories, while tree contact
events have the highest arc voltage values.  For the most part,
2.5 animal contact events have an arc voltage in between lightning
2 induced and tree contact events.  Compared with these events,
)Vk( egatloV crA cable failure disturbances have much less arc voltage values.
1.5
|     | 1   |     |     |     |     |                                                          |     | IX.  CONCLUSION   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | ----------------- | --- | --- | --- | --- |
|     | 0.5 |     |     |     |     | The information present in the waveforms captured by PQ  |     |                   |     |     |     |     |
monitoring stations was extracted in form of characteristic
0
0 0.02 0.04 0.06 0.08 0.1 0.12 0.14 0.16 0.18 0.2 signatures which can be used for event classification. The
|     |     |     |     | time(s) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 16.  Arc Voltage in Phase B for Tree Contact Event shown in Fig. 4  signatures  analyzed  were  the  time  of  occurrence,  fault
insertion angle, number of affected phases, time duration of
2 fault, wavelet domain analysis and arc voltage. Using the time
stamp, the events were classified according to the season and
1.5
)Vk( egatloV crA also the time of day. Majority of the lightning induced events
occurred in summer while, most of the tree contact events took
1 place in fall. Both the animal and tree contact events were
generally affecting only one phase of the distribution line, and
0.5
these events usually had the fault insertion angle near the peak
0 of the sine wave. The time duration of the fault proved to be
|     | 0   | 0.02 | 0.04 0.06 0.08 | 0.1 0.12 0.14 | 0.16 0.18 0.2 |     |     |     |     |     |     |     |
| --- | --- | ---- | -------------- | ------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
 an inconclusive characteristic.  It was suggested that lightning
time(s)
Fig. 17.  Arc Voltage in Phase C for Lightning Induced Event shown in Fig. 5
events could be distinguishable from tree contact events in the
wavelet domain. Furthermore, lightning induced events had an
The animal and tree contact events have a peak arc voltage
arc voltage that was lower than both the contact events.
that is more than 1 kV, while the lightning induced event has
Through the course of this analysis it was found that no
an arc voltage that remains largely below 1 kV for the fault
|            |     |                |           |                    |             | single  | signature  | can  exclusively  |     | identify  |     | a  given  event.   |
| ---------- | --- | -------------- | --------- | ------------------ | ----------- | ------- | ---------- | ----------------- | --- | --------- | --- | ------------------ |
| duration.  |     | As  mentioned  | earlier,  | the  arc  voltage  | estimation  |         |            |                   |     |           |     |                    |
algorithm is applicable only to single phase faults. In addition,  However, a combination of these signatures can be used to
|     |     |     |     |     |     | uniquely  | characterize  | the  | animal  | contact,  | tree  | contact  and  |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | ---- | ------- | --------- | ----- | ------------- |
only the events that have a stable arc voltage value have been
|     |     |     |     |     |     | lightning  | induced  | events.  |     | Moreover,  |     | several  other  |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | -------- | --- | ---------- | --- | --------------- |
selected for analysis, resulting in a total of 20 animal contact
cases, 24 tree contact cases and 14 lightning induced cases.  characteristics like p.u. voltage drop in the faulted phase can
The  arc  voltage  values  for  these  cases  are  plotted  in  a  be extracted in the future to determine the root-cause of faults.
normalized fashion in Fig. 18. 25 cable failure cases from the  Future work involves quantification of the relevance of these
same PQ data set are included for the purpose of comparison.   characteristics and extraction of patterns to form a rule set.
Such a set of rules can be used to identify causes of unknown
|     |     |     |     |     |     | events.  | The  | development  | of  | a  rule  | based  | classification  |
| --- | --- | --- | --- | --- | --- | -------- | ---- | ------------ | --- | -------- | ------ | --------------- |
methodology for animal contact, tree contact and lightning
induced events is tackled in [17].

7
X. ACKNOWLEDGEMENT
The authors would like to thank utilities in the Northeastern
XII. BIOGRAPHIES
region of the United States for providing power quality Saurabh Kulkarni received his B.S. from the University of Pune, India in
measurement data. 2003 and the M.S. form The Department of Electrical and Computer
Engineering at The University of Texas at Austin in 2009, where he is
currently working towards his doctorate. His research interests are in power
XI. REFERENCES quality for AC and DC systems.
[1] T.A. Short, Electric power distribution handbook. Boca Raton, FL.: CRC Duehee Lee received his B.S. from the POSTECH, Republic of Korea in
Press, 2004.
2004 and M.S. degrees from The Department of Electrical and Computer
[2] S. Santoso, E. J. Powers, W. M. Grady, A. C. Parsons, "Power quality Engineering at The University of Texas at Austin in 2009, where he is
disturbance waveform recognition using wavelet-based neural classifier currently pursuing the Ph.D. degree in energy systems. His research interests
– Part 1: Theoretical foundation," IEEE Transactions on Power Delivery, include nonlinear system identification and power system stability.
vol. 15, no. 1, pp. 222-228, 2000 January.
Alicia J. Allen received the B.S. and M.S. degrees from The Department of
[3] A. K Ghosh, D. L. Lubkeman, "The classification of power system
Electrical and Computer Engineering at The University of Texas at Austin,
disturbance waveforms using a neural network approach," IEEE
where she is currently pursuing the Ph.D. degree in energy systems. Her
Transactions on Power Delivery, vol. 23, no. 1, pp. 109-115, January
research interests include power quality, renewable energy and synchronized
1995.
phasor measurements.
[4] K.L. Butler, J.A. Momoh, D.J Sobajic, "Field studies using a neural-net-
based approach for fault diagnosis in distribution networks," IEE
Surya Santoso (M’96–SM’02) received the M.S.E. and Ph.D. degrees in
Proceedings on Generation, Transmission and Distribution, vol. 144, no.
electrical and computer engineering from the University of Texas at Austin in
5, pp. 429-436, Sept 1997.
1994 and 1996, respectively. From 1997 to 2003, he was a Consulting
[5] L. Xu and Chow Mo-Yuen, "A classification approach for power Engineer with Electrotek Concepts. Currently, he is an Associate Professor in
distribution systems fault cause identification," IEEE Transactions on the Department of Electrical and Computer Engineering at the same
Power Systems, vol. 21, no. 1, pp. 53-60, Feb 2006. university. His research interests include power quality, power systems, and
[6] O. Dag, C. Ucak, "Fault classification for power distribution systems via wind power.
a combined wavelet-neural approach," in International Conference on
Power System Technology, Singapore, 2004, pp. 1309-1314. Thomas A. Short (M’90–SM’98) received the M.S.E.E. degree from
Montana State University, Bozeman, in 1990. He is a Senior Engineer with
[7] Q. Sun, X. Liu, H. Zhang, "Power Distribution Fault Diagnosis Based on
EPRI in an office in Burnt Hills, NY. Before that, he was with Power
Rough-Cloud Sets," in Asia-Pacific Power and Energy Engineering
Technologies, Inc., for ten years. For several utilities, he has performed
Conference, March, 2009, pp. 1-4.
lightning protection, voltage sag, flicker, capacitor application, and load flow
[8] Bollen Math H. J., Gu Irene Y. H., Peter, G. V. Axelberg , and analysis studies and has been involved in several monitoring projects on
Styvaktakis Emmanouil, "Classification of Underlying Causes of Power distribution systems. He authored the Electric Power Distribution Handbook
Quality Disturbances: Deterministic versus Statistical Methods," (CRC Press, 2004). Mr. Short led the development of IEEE Std. 1410-1997,
EURASIP Journal on Advances in Signal Processing, vol. 2007, p. 17, as Chair of the IEEE Working Group on the Lightning Performance of
2007. Distribution Lines. For this effort, he was awarded the 2002 Technical
[9] Chow Mo-yuen, L. S. Taylor, "Analysis and prevention of animal-caused Committee Distinguished Service Award.
faults in power distribution systems," IEEE Transactions on Power
Delivery, vol. 10, no. 2, pp. 995-1001, April 1995.
[10] V. T Morgan, R. D. Findlay, "The effect of frequency on the resistance
and internal inductance of bare ACSR conductors," IEEE Transactions
on Power Delivery, vol. 6, no. 3, pp. 1319-1326, July 1991.
[11] I. Daubechies, "Ten Lectures on Wavelets," in SIAM, Philadelphia,
Pennsylvania, 1992.
[12] B. Koch, P. Christophe, "Arc voltage for arcing faults on 25(28)-kV
cables and splices," IEEE Transactions on Power Delivery, vol. 8, no. 3,
pp. 779-788, July 1993.
[13] R.D. Garzon, High Voltage Circuit Breakers, 2nd ed. June: CRC, 2002.
[14] T. Gammon, J. Matthews, "Conventional and recommended arc power
and energy calculations and arc damage assessment," IEEE Transactions
on Industry Applications, vol. 39, no. 3, pp. 594- 599, June 2003.
[15] Z.M. Radojevic, V.V. Terzija, "Fault Distance Calculation and Arcing
Faults Detection on Overhead Lines Using Single End Data," IET 9th
International Conference on Developments in Power System Protection,
pp. 638-643, Mar 2008.
[16] T A Short, D D Sabin, M F McGranaghan, "Using PQ Monitoring and
Substation Relays for Fault Location on Distribution Systems," in IEEE
Rural Electric Power Conference, 2007.
[17] V. Barrera Nunez, S. Kulkarni, S. Santoso, J. F Melendez, "Feature
Analysis and Clasiification Methodology for Overhead Distribution Fault
Events," submitted to IEEE PES General Meeting , Minneapolis,
Minnesota, 2010 (submitted).