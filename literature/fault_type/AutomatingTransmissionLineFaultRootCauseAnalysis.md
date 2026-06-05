This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPWRD.2015.2503478, IEEE
Transactions on Power Delivery
Paper TPWRD-00902-2015 1
Automating Transmission Line Fault Root
Cause Analysis
UJ Minnaar*, F Nicolls**, and CT Gaunt**, Member, IEEE
*Eskom Holdings, South Africa, ** Department of Electrical Engineering, University of Cape Town, South Africa
 the basis that they will be exposed to similar conditions, and
improvements can be made to reduce the effects of the
Abstract— This research demonstrates that transmission line prevalent causes of faults. For example, from the start of a
faults can be classified automatically according to their project, bird guards might be adopted or clearances increased
underlying cause, and lays a foundation for operational to minimize bird streamer faults.
classification of transmission line faults in system control centres. In a typical scenario, once a fault has occurred, an operational
The transmission line fault waveforms are characterised by
crew is dispatched to patrol the line, identify the fault and
instantaneous symmetrical component analysis to describe the
conduct corrective work. Automatic classification can provide
transient and steady state fault conditions. Using a large fault
information for dispatchers to help teams to be appropriately
record and waveform database, classification features based on
equipped and prepared to look for characteristic fault signs.
the waveform and external environmental characteristics have
been identified to develop single-nearest-neighbour classifiers Where lines are not allowed to be returned to service without a
that identify the underlying cause of transmission line faults, and complete line inspection to resolve uncertainty about the cause
good classification accuracy has been achieved. of a fault and concerns about equipment damage, early
identification of the fault cause could allow a line to be
Index Terms— power system operations, transmission line restored more quickly [4].
faults, fault causes, nearest neighbor classifier, pattern The causes of faults are not always correctly identified as field
recognition
services staff may give vague descriptions or lack knowledge
about the fault mechanisms [5]. Thus, the aim of the present
research is to establish an operational basis for classifying
I. INTRODUCTION
faults according to their underlying cause. The contributions
M ODERN society depends on electricity supplies that are of this work are: a) the development of waveform features to
reliable [1] and compatible with the needs of equipment characterise faults across multiple voltage levels, at specific
connected by utility customers [2]. Supply interruptions time intervals from fault initiation and according to the
and voltage dips are the two most common events affecting influence of the fault flashover mechanism; b) the ranking and
customers and have the largest financial impact on them. They selection of contextual and waveform features for identifying
disrupt commercial activities and manufacturing processes, the causes of transmission line waveforms; c) the successful
resulting in decreased output and profitability [3]. Faults on classification of transmission line faults by Single Nearest
transmission lines are a root cause of both interruptions and Neighbor classification, and d) showing that transmission line
voltage dips [2]. faults can be classified using either combined contextual and
The focus of this paper is on the classification of transmission waveform features or only contextual features.
line faults, according to the underlying cause, to meet the
requirements for transmission systems control and operations. II. LITERATURE REVIEW
The classification of faults plays a role in both the design and
A. Waveform Characterization for Event Classification
operational management of networks. Incorrect classification
leads to uncertainty and error in developing ways to improve Characterizing event waveforms (e.g. voltage dips) is used to
network reliability performance. The benefits of correct fault reduce data, interpret and characterize events for analysis and
cause identification are a) reduced wasteful expenditure on management of power quality [6]. Methods include the ABC
inappropriate corrective measures, b) lower fault frequencies classification [7] and the South African NRS048-2 voltage dip
as the causes of faults are addressed, and c) automatic fault characterization [8]. The requirement is to describe events
identification for immediate operational responses to faults. with a limited number of parameters [9].
Accurate identification of fault causes informs the design and Characterization is also conducted for automatic classification
parameter selection of new lines (insulator selection, tower of disturbances [10] with the aim being ‘to find common
design, footing resistance) and identifies poorly performing features that are likely related to specific underlying causes in
lines for implementing mitigating improvements. The design power systems’ [11]. Various signal processing techniques,
of new networks close to existing networks is often done on including root mean square (rms), Fourier and wavelet
transforms [12], have been used to extract features and
characterize events. They include finding the fundamental
voltages and currents and harmonics, detecting transition
0885-8977 (c) 2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPWRD.2015.2503478, IEEE
Transactions on Power Delivery
Paper TPWRD-00902-2015 2
points in waveforms, waveform segmentation and feature on the existing work by establishing a basis for classifying
extraction [13]. transmission system faults.
Most studies base event classification on the disturbance type
e.g. dips, transient and swells [13]. While this work is relevant III. CHARACTERISING TRANSMISSION LINE FAULTS
for developing methods, its practical application is limited
A. Data Set
[10], since many studies with a shortage of data use synthetic
data, leading to results with limited applicability to real-world The transmission system of South Africa’s electricity utility
scenarios [10]. Eskom comprises over 28 000 km of lines operated at voltages
Characterizing events according to their underlying causes is of 132, 220, 275, 400 and 765 kV, of which the bulk are
of more practical benefit, as described above, but limited work 400 kV and 275 kV lines. Records from 78 digital fault
has been published. Classification of faults according to recorders (primarily SIMEAS-R and Siemens P513 devices)
causes internal to the power system (e.g. transformer on the Eskom transmission network at 220kV, 275kV and
energizing, load changes and motor starting) has been 400kV over 13 years to 2008 were available for 2672
explored by rms and Kalman filtering [14]. transmission line faults. Current and voltage waveforms are
Characterization and analysis of external faults based on the sampled at 2500 Hz.
voltage and current waveforms has been investigated for Fault measurement records were checked to ensure they
lightning, tree and animal contact, and cable faults [15]. provided adequate pre-fault data and measurements from all
Waveform characterization features were obtained from voltage and current channels. The fault measurement records
voltage and current waveforms recorded at distribution were matched using time, date and line on which the fault
substations (12.47 kV) for 180 events, and included maximum occurred to a database of 11573 faults developed by Minnaar
zero sequence current and voltage, fault inception phase angle et al. for the same transmission system [26]. This database of
(FIPA), maximum change of current and voltage magnitudes fault measurements is linked to the underlying fault cause as
(phase and neutral), and maximum arc voltage. well as contextual information i.e. GIS data, line parameters
and lightning density. This database addresses key concerns
B. Classification of Power System Events
raised by Gu and Styvaktakis [13]: each characterized
Pattern recognition is the science of information procedures waveform is associated with a fault cause that makes this a
for classifying, describing and labelling measurements [16]. A suitable dataset for conducting feature selection and
pattern recognition system includes stages of sensing, data classification according to underlying causes; and the large
pre-processing, feature extraction and classification [17]. data set, entirely based on measurements from an operational
Work towards developing pattern recognition techniques for transmission system, addresses the limitations of many studies
recognition of power system events includes identifying the with too little data.
faulted phases e.g. single-phase-to-ground fault or phase-to- The original waveform data from digital fault recorders is
phase [18] and fault location [19]. Such studies use simulated stored in the IEEE C37.111 Common Format for Transient
and measured data from fault recorders on power systems. Data Exchange (COMTRADE). Each file represents a unique
Less work has been done to identify the underlying causes of fault event measurement. The following data are available:
events [13]. One study uses the CN2 induction algorithm to sampling rate; start date and time; faulted phase; distance-to-
determine rules to classify four causes of distribution network fault; red, white and blue phase and neutral currents and
faults (lightning, tree, cable and animal) [15]. The CN2 rule voltages; number of samples; and timestamp data. The data
induction algorithm induces an ordered list of classification was imported and stored in a Matlab structure. An array of
rules from a set of classified observations [15]. This is an structures, compiled with each individual measurement being
approach which is suitable for fault root cause identification a unique structure (file name is associated for identification),
where sufficient measurements with classifications are enables bulk signal processing of waveform data by repeating
available. the same calculations inside a loop to obtain the desired
Approaches to identifying animal-caused faults on distribution characteristics. A symmetrical sequence component
systems according to their root causes have included discrete transformation was implemented in the Matlab Simulink
wavelet transforms in combination with artificial immune environment, built around the discrete 3-phase sequence
systems [20], Bayesian networks [21], artificial neural [22] analysis block. The code to calculate waveform characteristics
and fuzzy systems [23]. Artificial neural networks (ANN) and utilizes structure arrays in Matlab, so as to make possible the
linear regression have been used to classify tree- and animal- bulk signal processing necessary for 2672 waveforms. The
caused faults based on distribution utility outage data [4]. Simulink model is then called from inside a ‘for’ loop to
Other methods applied to automatically diagnose the root calculate the necessary parameters for each individual
cause of faults include support vector machines [24], expert measurement, which in turn is stored inside a second structure
systems for classifying events from measurements i.e. voltage array. The outputs of the Simulink model are discrete
step change, transformer energizing [14], as well as linear waveforms of magnitudes and phase angles for the positive,
discriminant analysis [25]. Most studies have focused on negative and zero sequence current and voltages. Sequence
distribution networks, with few aimed at root cause component currents and voltages are output in complex format
identification for transmission lines [24]. Such studies develop and the rates of change for voltage and current sequence
the theory and use of pattern recognition for identifying the components are also exported. These are used to calculate a
causes of faults and power quality problems. This paper builds range of values for feature extraction and fault cause
classification.
0885-8977 (c) 2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPWRD.2015.2503478, IEEE
Transactions on Power Delivery
| Paper TPWRD-00902-2015  |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 3   |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

B.  Identifying the start and end of a fault  be considered together, 2) maximum changes of current were
The features during a fault are required for characterization,  used  to  identify  the  influence  of  the  fault  flashover
mechanism, and 3) the magnitude of characteristics at specific
making the identification of the start and end of a fault an
|     |     |     |     |     |     |     | time  | intervals  | from  | the  | start  | of  the  | fault  | were  compared,  |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ----- | ---- | ------ | -------- | ------ | ---------------- | --- |
important consideration. The three pre-fault (normal steady
state operation), fault and interruption stages of measurement  characterizing the development of the fault.
are illustrated for a single-phase-to-ground fault in Fig. 1. The  The following fault features were extracted.

| start  and  | end  of  the  | fault  | are  identified  |     | using  | sequence  |     |                 |     |     |     |     |     |     |     |
| ----------- | ------------- | ------ | ---------------- | --- | ------ | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
|             |               |        |                  |     |        |           | 1)  | Faulted Phases  |     |     |     |     |     |     |     |
components derived from the rms profiles.
The relevance of the faulted-phases feature is based on the
|     |     |     |     |     |     |     | hypothesis  |     | that  | the  physical  |     | flashover  | mechanism  |     | is  a  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | -------------- | --- | ---------- | ---------- | --- | ------ |
consequence of the underlying fault cause. The relationship is
illustrated in Table 1, where the faulted phases (L) or ground
(G) according to underlying cause are shown for the 220kV,
275kV and 400kV networks. More than 90% of all faults on
the South African transmission network between 1995 and
2008 were single-phase-to-ground faults and pollution-caused
faults are almost exclusively single-phase-ground-faults.

TABLE I
FAULTED PHASES ACCORDING TO UNDERLYING CAUSE
|     |     |     |     |     |     |     | Faulted  | Bird      |       |       |            |      |        |            |        |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | ----- | ---------- | ---- | ------ | ---------- | ------ |
|     |     |     |     |     |     |     | Phases   | streamer  |       | Fire  | Lightning  |      | Other  | Pollution  | Total  |
|     |     |     |     |     |     |     |   L-G    |           | 1070  | 453   |            | 534  | 261    | 122        | 2440   |
Fig. 1: Stages of a fault measurement – voltage and current  L-L-G  15  33  66  8  1  123
|     |     |     |     |     |     |     | L-L  |     |     | 25  |     | 1   | 2   |     | 28  |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
The beginning of the fault is identified by a detection index  L-L-L    30  4  32  4    70
(𝑑𝐼), similar to that used for segmentation of rms voltage  L-L-L-G  4  3  3  1    11
|               |        |        |     |                  |     |          | Total  |     | 1119  | 518  |     | 636  | 276  |   123  | 2672  |
| ------------- | ------ | ------ | --- | ---------------- | --- | -------- | ------ | --- | ----- | ---- | --- | ---- | ---- | ------ | ----- |
| measurements  | [14],  | based  | on  | the  difference  |     | between  |        |     |       |      |     |      |      |        |       |

consecutive values of the positive sequence current:
|     |     |     |     |     |     |     | 2)  | Maximum Change of Current (∆𝐼 |     |     |     |     |     |     | )   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
                 𝑑𝐼 =𝐼 −𝐼                (1)  𝑚𝑎𝑥0 ,∆𝐼 𝑚𝑎𝑥1 ,∆𝐼 𝑚𝑎𝑥2
|     |     |     | 1(𝑛−1) | 1(𝑛) |     |     |                                                             |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | ---- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |        |      |     |     | The maximum change of current during the initial transient  |     |     |     |     |     |     |     |     |
A threshold set at 12000 kA/sec marks the start of a fault. In
stage, calculated using (2) as the maximum difference between
most records, measurement continues after the protection has
consecutive samples after the fault has triggered, provides a
operated, so post-fault values must be removed. A fault ‘ends’
picture of the dynamic state of the fault. The maximum change
when the 40ms moving average zero sequence current drops
for each positive, negative and zero sequence component is
below 15% of the peak zero sequence current. Both the fault
treated as an individual feature.
start and end thresholds were determined by inspection until
|     |     |     |     |     |     |     |     |               ∆𝐼 |     | =𝑚𝑎𝑥 (𝐼 |     |     | −𝐼 )             (2)  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | --- | --- | --------------------- | --- | --- |
the start point and endpoint of all the fault measurements in  𝑚𝑎𝑥 𝑛+1 𝑛
|     |     |     |     |     |     |     | This  | feature  | is  | chosen  | to  test  | for  | a  relation  | between  | the  |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | ------- | --------- | ---- | ------------ | -------- | ---- |
the dataset were captured.
underlying cause and the rate of rise of fault current during the
| C.  Feature Extraction                                        |     |     |     |     |     |     | initial stages of a fault.   |                                   |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| The waveform features extracted in this research were chosen  |     |     |     |     |     |     |                              |                                   |     |     |     |     |     |     |     |
|                                                               |     |     |     |     |     |     | 3)                           | Maximum Sequence Voltage Ratio (V |     |     |     |     | , V | )   |     |
on the basis of their possible link to one of the root fault  max2 max0
The degree of unbalance [15] during a fault is calculated from
causes and their expected ability to identify a cause. These
features were then tested for statistical significance linking  the maximum negative and zero sequence voltages during a
fault relative to their respective pre-fault values:
them to a cause.
𝑉𝑓𝑎𝑢𝑙𝑡_max _𝑖                (3)
Characterization and analysis of external faults based on the              𝑉 =
𝑟𝑒𝑙_max _𝑖
voltage  and  current  waveforms  has  previously  been  𝑉𝑝𝑟𝑒−𝑓𝑎𝑢𝑙𝑡

| investigated  | for  causes  | such  | as  lightning,  |     | tree  and  | animal  |     |     |     |     |     |     |     |     |     |
| ------------- | ------------ | ----- | --------------- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Where i is either 0 or 2
contact and cable faults [15] and several features considered in

that study were retained, albeit in a modified form. Maximum
|     |     |     |     |     |     |     | 4)  | Sequence Component Currents at ½ and 1 Cycle   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
zero sequence currents and voltages are defined relative to
|     |     |     |     |     |     |     |       (I | , I | , I | , I | ,I  | , I )  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | ------ | --- | --- | --- |
pre-fault levels, enabling measurements at different voltage  0(0.5) 1(0.5) 2(0.5) 0(1)  1(1) 2(1)
|             |                 |     |            |            |           |      | The  | values  | of  | the  positive,  |     | negative  | and  | zero  | sequence  |
| ----------- | --------------- | --- | ---------- | ---------- | --------- | ---- | ---- | ------- | --- | --------------- | --- | --------- | ---- | ----- | --------- |
| levels  to  | be  considered  |     | together,  | including  | relating  | the  |      |         |     |                 |     |           |      |       |           |
component currents, illustrated in Fig. 2 for the zero sequence
maximum values to pre-fault conditions. Factors such as fault
|                    |          |         |       |      |           |            | current component I |     |     | 0 , are measured at ½ cycle and one whole  |     |     |     |     |     |
| ------------------ | -------- | ------- | ----- | ---- | --------- | ---------- | ------------------- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
| level,  pre-fault  | loading  | level,  | type  | and  | location  | of  load,  |                     |     |     |                                            |     |     |     |     |     |
cycle after the fault trigger.
| network  | configuration  | or  | capacitors  | being  | switched  | may  |     |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ----------- | ------ | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
influence the fault waveforms measured on the same line.
Several parameters from the measurement waveforms were
| calculated  | to  test  for  | these  | influences  | using  | the  following  |     |     |     |     |     |     |     |     |     |     |
| ----------- | -------------- | ------ | ----------- | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
strategies: 1) peak/maximum values relative to pre-fault values
enable measurements from different voltage level networks to
0885-8977 (c) 2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPWRD.2015.2503478, IEEE
Transactions on Power Delivery
Paper TPWRD-00902-2015  4

waveform [15]. In particular, it is reported that cable faults
and animal faults have average FIPA values of 93.7ᵒ and 99.3ᵒ
respectively [15].  FIPA is calculated as the time of the trigger
after the last zero-crossing prior to the fault. For multi-phase
faults, FIPA is assumed to be the phase angle closest to the
peak.

8)  Sequence Component Fault Current Time Constant
The Sequence Component Fault Current Time Constant (τ0,
τ1, τ2) is introduced as a waveform feature. It treats the fault
  waveform response in a similar manner to a first order linear
|     | Fig. 2: I |  at ½ and one cycle after fault trigger  |     |     |     |     |     |     |
| --- | --------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
0 time-invariant system. The time constant is calculated as the

time taken from fault trigger to 0.63 of the difference between
5)  Maximum Sequence Current to Pre-Fault Current Ratio  maximum fault current and pre-fault current for each sequence
| (I , I | )   |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- |
1max 0max component, as illustrated in Fig. 3. The time constant for each
Peak values of sequence currents are calculated relative to the
sequence component current is an individual feature that may
pre-fault current levels on the feeder.
|     |     |     |     |     | indicate  | the  dynamic  response  | of  | the  transmission  |
| --- | --- | --- | --- | --- | --------- | ----------------------- | --- | ------------------ |
          𝐼 = 𝐼𝑝𝑒𝑎𝑘 𝑝𝑜𝑠𝑡−𝑓𝑎𝑢𝑙𝑡              (4)  line/network to the fault type.
max _𝑟𝑒𝑙
𝐼𝑝𝑒𝑎𝑘 𝑝𝑟𝑒−𝑓𝑎𝑢𝑙𝑡

This gives an indication of the total state of change in current
| relative  | to  the  | state  of  | the  network/load  | prior  to  | fault  |     |     |     |
| --------- | -------- | ---------- | ------------------ | ---------- | ------ | --- | --- | --- |
occurrence. This relative value of fault current may provide
more information than peak fault current, which is dominated
| by the network parameters.  |     |     | Maximum sequence current is  |     |     |     |     |     |
| --------------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
therefore largely independent of network conditions or fault
cause.

| 6)  Fault Resistance (R |     |                | , R            | )   |     |     |     |     |
| ----------------------- | --- | -------------- | -------------- | --- | --- | --- | --- | --- |
|                         |     | fault_onecycle | fault_twocycle |     |     |     |     |     |
The underlying mechanism by which a fault is formed and the
medium along which fault current moves differs for each of
the major fault causes. Bird streamer fault current flows via

the  liquid  streamer,  while  fault  currents  due  to  fires  are  Fig. 3: Sequence Component Fault Current Time Constant
| conducted via air and smoke particles. The resistivities of  |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
these  mediums  differ  significantly.  Similar  to  sequence  Table  III  shows  the  mean  (µ)  and  standard  deviation  (σ)
currents, the fault resistance is calculated one and two cycles  values  of  the  Sequence  Component  Fault  Current  Time
after the initiation of the fault (and denoted as   and  Constants in milliseconds [28]. These values are very similar
Rfault_onecycle
) to account for the dynamic nature of faults. The  across sequences phases; however they differ across system
Rfault_twocycle
line resistance from the point of measurement to the fault is  voltage levels. These results are indicative of most of the
based on the fault impedance values used for the protection  waveform characteristics extracted, illustrating the effect of
settings for each line. The equations used to calculate fault  the system rating on the magnitudes and changes in voltages
resistance are based on the fault calculations according to  and currents in response to faults. The voltage of the system
Glover and Sarma [27]. The area of high impedance faults and  on which a fault occurs should be included as a feature to
the modelling of fault arcs, while worthy of investigation, are  analyze measurement data.
TABLE III
not dealt with in this paper. Table II shows the mean (µ) and
standard deviation (σ) values of the Fault Resistance in ohms.   POSITIVE, NEGATIVE AND ZERO SEQUENCE FAULT CURRENT
TIME CONSTANT STATISTICS

|     |     |                   | TABLE II  |        |                        | 220kV  | 275kV        | 400kV                |
| --- | --- | ----------------- | --------- | ------ | ---------------------- | ------ | ------------ | -------------------- |
|     |     | FAULT RESISTANCE  |           |        | Characteristic         | µ      | σ  µ         | σ  µ  σ              |
|     |     |                   |           |        | Positive current Time  | 12.81  | 1.48  26.85  | 70.01  22.72  71.41  |
|     |     | 220kV             | 275kV     | 400kV  |                        |        |              |                      |
Constant (τ1)
Characteristic  µ  σ  µ  σ  µ  σ  Negative current Time  12.85  1.61  25.92  70.21  21.80  76.20
Constant (τ2)
| Rfault_onecycle  |     | 20.30  14.73  | 36.23  148.70  | 41.99  | 118.06                 |        |              |                      |
| ---------------- | --- | ------------- | -------------- | ------ | ---------------------- | ------ | ------------ | -------------------- |
|                  |     |               |                |        | Zero current Time      | 13.46  | 7.14  22.31  | 46.26  20.27  63.65  |
| Rfault_twocycle  |     | 17.94  13.55  | 31.69  130.15  | 37.88  | 124.74  Constant (τ0)  |        |              |                      |

D.  Statistical Significance of Waveform Features
7)  Fault Inception Phase Angle (FIPA)
Analysing the waveform feature data by fault cause indicates
Fault inception phase angle (FIPA) was considered in case the
|     |     |     |     |     | that  the  fault  | cause  influences  | the  majority  | of  them.  The  |
| --- | --- | --- | --- | --- | ----------------- | ------------------ | -------------- | --------------- |
large dataset could give a clear indication of the relationship
statistical significance (to the 0.05 level) of the causes (bird
between fault types and fault peak. Its inclusion is based on
streamer, fire, lightning, pollution and other) on single-phase-
statistical data presented by Barrera et al. that certain fault
|         |              |            |               |            | to-ground  | faults  occurring  | on  220kV,  275kV  | and  400kV  |
| ------- | ------------ | ---------- | ------------- | ---------- | ---------- | ------------------ | ------------------ | ----------- |
| causes  | have  fault  | inception  | angles  near  | the  peak  | of  the    |                    |                    |             |
networks, representing more than 90% of all faults, was tested
0885-8977 (c) 2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPWRD.2015.2503478, IEEE
Transactions on Power Delivery
Paper TPWRD-00902-2015  5

| by analysis of variance (ANOVA), for which results are given  |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in  Table  IV  (‘yes’  indicates  statistically  significant).  The
TABLE V
differences across voltage levels for all the waveform features
FEATURES RANKED BY F-STATISTIC
| are  statistically  |     | significant,  | with  the  | exception  | of  FIPA,  |     |     |     |     |     |
| ------------------- | --- | ------------- | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- |
Type of
F- Overall
indicating  that  fault  causes  may  be  differentiated  by  a  Feature
|     |     |     |     |     |     |     | Feature  |     |     | statistic  Rank  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---------------- |
combination of these features.
|     |     |     |     |     |     |     |     | Hour  | Contextual  | 90.90  1  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --------- |

|     |     |     |     |     |     |     |     | Region  | Contextual  | 33.09  2  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --------- |
TABLE IV
|     |     |     |     |     |     |     |     | Month  | Contextual  | 32.16  3  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --------- |
 STATISTICAL SIGNIFICANCE OF CAUSES INFLUENCING
|     |     |     |     |     |     |     | Nominal Voltage  |     | Contextual  | 29.22  4  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | --------- |
WAVEFORM FEATURES
|          |                                    |                            |                 |         |        | Average ground flash density (Ng)  |                 |           | Contextual  | 25.45  5  |
| -------- | ---------------------------------- | -------------------------- | --------------- | ------- | ------ | ---------------------------------- | --------------- | --------- | ----------- | --------- |
| FEATURE  |                                    |                            | 400kV           | 275 kV  | 220kV  |                                    |                 |           |             |           |
|          |                                    |                            |                 |         |        |                                    |                 | I 2(0.5)  | Waveform    | 16.06  6  |
| ∆I       | max1 , ∆I max2                     | , Rfault_onecycle,         |                 |         |        |                                    |                 |           |             |           |
|          |                                    |                            |                 |         |        |                                    |                 | τ1        | Waveform    | 11.98  7  |
|          | Rfault_twocycle                    |                            | yes             | yes     | yes    |                                    |                 |           |             |           |
|          |                                    |                            |                 |         |        |                                    | Faulted Phases  |           | Waveform    | 11.58  8  |
| ∆𝐼       | 𝑚𝑎𝑥0 , I 1(0.5)                    | , I 1(1) , I 0(1) , I 1max | , I 0max   yes  | no      | yes    |                                    |                 |           |             |           |
|          |                                    |                            |                 |         |        |                                    |                 | V         | Waveform    | 10.44  9  |
|          | V                                  | , V                        |                 |         |        |                                    |                 | max2      |             |           |
|          |                                    | max2 max0                  | yes             | no      | no     |                                    |                 | τ2        | Waveform    | 9.97  10  |
| I 2(0.5) | , Pos. current Time Constant (τ1)  |                            | yes             | yes     | no     |                                    |                 |           |             |           |

|     | I   | , I , I   |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
2(1) 0(0.5) 2max no  no  yes  From a full ranking [28], Table V lists the top ten features and
FIPA  no  no  no  gives a clear picture of the relevance of each for distinguishing
Negative current Time Constant (τ2),
faults according to cause. The waveform features with the
| Zero current Time Constant (τ0)  |     |     | no  | yes  | no  |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
highest F-statistic scores are the maximum negative sequence
current (half cycle) and the positive sequence time constant
IV.  FAULT-ROOT IDENTIFICATION BASED ON PATTERN
|     |     |     |     |     |     | labelled I | 2(0.5) |  and τ1 respectively. Both provide a measure of  |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | ------------------------------------------------ | --- | --- |
RECOGNITION
the dynamic response to an event on a transmission line,
This section explores the classification of transmission line  relating to the rate at which sequence currents rise to peak
faults according to underlying cause using pattern recognition
fault current. Table V indicates that three individual contextual
techniques. The individual relevance of features is determined
features related to time of occurrence and geographic location
with  respect  to  the  four  major  causes  identified  and  of a fault are highly relevant to identifying its underlying
classification is treated as a multiclass problem. Features are  cause. This result is consistent with the success achieved using
ranked according to their relevance in separating fault causes
|     |     |     |     |     |     | only  | contextual  | features  | for  classifying  | animal-  and  tree- |
| --- | --- | --- | --- | --- | --- | ----- | ----------- | --------- | ----------------- | ------------------- |
and classifiers are built by nested subsets. The full feature set  caused faults on distribution systems [24]. The ranking also
consists of 7 contextual features (environmental, climatic and  gives insight into the relative strength of using the contextual
| diurnal)  | and  | 21  waveform  | features  (shown  |     | in  Table  IV,  |     |     |     |     |     |
| --------- | ---- | ------------- | ----------------- | --- | --------------- | --- | --- | --- | --- | --- |
and waveform features to identify fault causes.
including system voltage).
B.  Classification by Nested Subsets
A key finding is that the fault frequencies have statistically
significant differences with respect to time-of-day, season, and  The  classification  problem  for  transmission  line  faults  is
climate as represented by rainfall area in South Africa. The  defined here as a multiclass problem with five classes. A
differences are not uniform across the voltage levels; hence  multiclass classifier is a function F:X →Y which maps an
voltage level is also a feature. The contextual feature set also  instance x into a label F(x) [30].
introduces  other  features  considered  relevant.  Thus  the  There are two common approaches to generating F. The first
is to construct it through a combination of binary classes, e.g.
contextual features describing fault occurrence are hour of
day,  month  of  year,  rainfall  area,  voltage  level,  line  GIS  logistic regression or support vector machines; and the second
number, Eskom transmission grid region and the lightning  (used in this study) is to generate F directly e.g. naïve Bayes
or nearest neighbor (NN) algorithms. The 1-NN classifier is
ground flash density [26].
In  this  study,  feature  selection  was  used  first  to  improve  proposed for identifying the underlying cause of transmission
| understanding and interpretability of the data and secondly to  |     |     |     |     |     | line faults.   |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
identify features for building good classifiers for transmission  The 1-NN rule is a suitable benchmark for other classifiers as
line  fault  causes.  Feature  ranking  and  classification  was  it  requires  no  user-specified  parameters,  making  it
considered for three scenarios, using: a) only the contextual  implementation  independent,  and  provides  reasonable
feature set, because earlier analysis had shown statistically  classification performance in most applications [31]. Building
a series of 1-NN classifiers determines the underlying cause of
significant differences in fault frequencies by time of day,
climate and season; b) only the waveform feature set; and c)  faults. An advantage of 1-NN classification is its conceptual
combined  waveform  and  contextual  feature  sets.  Feature  simplicity and ease of implementation [32].
The 1-NN classifiers comprise five classes, one for each major
selection and classification was implemented in the Matlab
toolbox PRTOOLS [29].  fault cause: birds, fire, lightning, pollution, and other. The
classifier finds the nearest point in the training set to the
A.  Feature Ranking
unclassified point and assigns it to the corresponding label.
| Feature  | ranking  | according  | to  the  F-statistic  |     | derived  with  |          |            |           |                          |               |
| -------- | -------- | ---------- | --------------------- | --- | -------------- | -------- | ---------- | --------- | ------------------------ | ------------- |
|          |          |            |                       |     |                | Feature  | selection  | for  the  | initial  classification  | is  done  by  |
ANOVA provides a measure of variance due to each feature  building  nested  subsets  of  features  of  increasing  size.
and a basis for building classifiers.  Classifier building starts with a subset of one feature (the

highest F-statistic) and features of decreasing F-statistic are
0885-8977 (c) 2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPWRD.2015.2503478, IEEE
Transactions on Power Delivery
Paper TPWRD-00902-2015 6
progressively added. For example, using Table V, the first (Note: the F-statistic used in ANOVA and the F-measure are
subset comprises the feature ranked 1 and the second subset two independent measures defined and used in different
the features ranked 1 and 2. ways). In this study, the measures used to assess classifier
A classifier is trained using a training set of two thirds of the performance are overall classification Accuracy and the F-
data and performance is evaluated using the test set of the measure for each fault cause.
remaining third of the data. The entire data set is randomly
D. Overall Classification Accuracy
split 30 times into the training and test sets, and the trained
classifier evaluated against each test set to reduce variance The overall classification accuracy rates indicate that
from the classification results. Evaluating the classifier in this classification accuracy up to 90% is achieved when using only
manner provides enough test data for the faults causes that the five highest ranked contextual features.
occur rarely i.e. other- and pollution-caused faults. Fig. 4 illustrates overall classification accuracy for contextual,
Classification is conducted according to the three scenarios: waveform and all features. The features are added according
using only contextual features, only waveform features, and to the respective decreasing rankings shown in Table IV for
the combined feature set. Two combining rules are waveform and contextual features and then according to the
implemented for classification using all the features. The first combining rules defined. For example, for ACC_All_rule1 all
(Rule 1) combines waveform and contextual feature sets by 21 features of Table IV are added according to Rule 1.
relevance using the overall ranking as indicated in Table IV;
the second (Rule 2) combines the waveform and contextual 1
feature sets by adding (in order of decreasing relevance) a
0.9
feature from each set, starting with the contextual set. Once all
the contextual features are added, the remaining waveform 0.8
features are added to form additional subsets.
0.7
C. Assessing Classifier Performance
0.6
Many classifier’s performance measures are based on the
confusion matrix. A 2x2 confusion matrix for a 2-class 0.5
classifier (Yes/No) and a test dataset is shown in Table VI
0.4
[33].
TABLE VI:
Fig. 4: Classification Accuracy
CONFUSION MATRIX
Class Predicted Positive Predicted Negative
Reasonably good classification performance can be achieved
Actual Positive True Positive (TP) False Negative (FN)
using only waveform features; the best accuracy achieved is
Actual Negative False Positive (FP) True Negative (TN) 0.801 using the seven highest ranked features. It does not
match the performance achieved using only contextual
features or combined contextual and measurement features.
The most common performance measure calculated from this
matrix is Accuracy (Acc), which is the proportion of the total E. Classification Performance using Waveform Features
number of predictions that were correct:
Figure 5 illustrates the classification success by F-measure for
each of the major fault causes, adding features according to
𝑇𝑁+𝑃𝑁
𝐴𝑐𝑐 = (5) decreasing F-statistic. Scores above 0.75 are achieved using
𝑇𝑃+𝐹𝑁+𝐹𝑃+𝑇𝑁
only the two highest ranked features for bird, fire and
lightning caused faults. The F-measure for pollution-caused
An acceptable Accuracy rate for practical classification may
faults is generally lower than the first three classes, but it
be set at 80%. However, Accuracy is an insufficient
needs to be considered that pollution is a highly imbalanced
performance measure in applications with imbalanced data
set (pollution faults represent only a small portion of the total
sets (i.e. one class represents only a small portion of the total
data). The performance of the ‘other’ class of faults is the
data) because a classifier ignoring the presence of the minority
poorest for most feature sets and depends on an appropriate
class will show good performance. The fault performance of
feature set being selected to achieve reasonable performance.
the transmission system is unbalanced across the four major
fault causes.
Alternative measures for classifying unbalanced datasets
include Precision (the percentage of correct positive
predictions), Recall (the percentage of true positive cases
correctly identified), and the F-measure [34], which is the
harmonic mean of Precision and Recall given by
2×𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛×𝑅𝑒𝑐𝑎𝑙𝑙
𝐹−𝑚𝑒𝑎𝑠𝑢𝑟𝑒 = (6)
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙
0885-8977 (c) 2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
)ccA(
ycaruccA
1 3 5 7 9 11 31 51 71 91 12 32 52 72
All_rule1 (28)
All_rule2 (28)
Contextual (7)
Waveform (21)
Number of features

This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPWRD.2015.2503478, IEEE
Transactions on Power Delivery
Paper TPWRD-00902-2015 7
Fig. 5: F-measure using waveform features Fig. 7: F-measure using waveform and contextual features
combined by rule 2
F. Classification Performance using Contextual Features
The classification performance achieved using contextual TABLE VII:
features is significantly better once five or more features are CLASSIFICATION PERFORMANCE
used (with features added by decreasing F-statistic) to build Classifier
the 1-NN classifier. F-measure scores above 0.8 are achieved
for all classes of faults with bird streamers having the highest
score of 0.917, as illustrated in Fig. 6.
Fig. 6: F-measure using contextual features
G. Classification Performance using Combined Features
Combining the waveform and contextual features does not
improve the classification over that achieved by using only
contextual features. Fig. 7 shows the F-measure performance
achieved using combining-rule 2.
The best classification accuracy of 0.86 is achieved using six
features (the top three ranked from the waveform and
contextual sets): Hour, Negative sequence current (half cycle
after fault initiation), Region, Positive sequence fault current
time constant, Month and Faulted Phases. The best
performance achieved with the 1-NN classifier is compared
with the classification performance of several common
classifiers with feature selection conducted by sequential
forward (SFS) and sequential backwards (SBS) wrapper
selection based on best performance for a particular classifier.
The classifiers used for the comparison are radial basis neural
network, decision tree and naïve Bayes classifiers.
0885-8977 (c) 2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
noisiceD
eert
noisiceD
eert
larueN
krowteN
larueN
krowteN
seyaB
evïaN
reifissalc
seyaB
evïaN
reifissalc
NN-1
gninibmoc(
)2
elur
Selection
SFS SBS SFS SBS SFS SBS
detseN stesbus
0.85
0.8
0.75
0.7
0.65
0.6
ACC 0.74 0.73 0.74 0.74 0.74 0.74 0.86
F-measure 0.78 0.77 0.78 0.78 0.80 0.78 0.89
Birds
F-measure 0.82 0.81 0.81 0.81 0.78 0.80 0.88
Fire
F-measure 0.67 0.65 0.67 0.73 0.68 0.68 0.84
Lightning
F-measure 0.31 0.00 0.30 0.28 0.29 0.34 0.75
Pollution
F-measure 0.17 0.20 0.16 0.15 0.14 0.15 0.74
Other
The comparative analysis of classification results shown in
Table VII demonstrates that the best performance achieved
with the 1-NN classifier is between 12-14% higher than
achieved with any of the other classifiers using either forward
or backward selection. The 1-NN classifier is also shown to
have considerably better classification performance when
considering the minority causes (Pollution and Other causes).
V. IMPLICATIONS OF RESULTS
Classifiers developed using only the contextual features
demonstrate the highest level of balanced classification
performance (F-measure=90%). The relevance of this is that
in instances where no physical evidence of the fault is present
and operators assign fault causes based on contextual
information (e.g. a fault during a thunderstorm may not be due
to lightning but is often classified as such [15]), the practice
overlaps directly with the best classification performance.
However, the lower classification accuracies achieved with
waveform features may be relevant when they point to results
differing from those indicated by the contextual features.
Using only waveform features to build a classifier produces
reasonable success levels, even with only the single most
erusaem-F
1 3 5 7 9 11 31 51 71 91 12
Birds
Fire
Lightning
Pollution
Other
Number of features
1.0
0.8
0.6
0.4
0.2
0.0
1 2 3 4 5 6 7
erusaem-F
1
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
Birds
Fire
Lightning
Pollution
Other
Number of features
erusaeM-F
1 2 3 4 5 6 7 8 9 01 11 21 31 41 51 61 71 81 91 02 12 22 32 42 52 62 72 82
Birds
Fire
Lightning
Pollution
Other
Number of features

This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPWRD.2015.2503478, IEEE
Transactions on Power Delivery
| Paper TPWRD-00902-2015  |     |     |     |     |     |     |     |     |     |     |     |     | 8   |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| relevant  | feature.  | While  | this  is  | an  important  |     | finding  for  |     |     |     |     |     |     |     |
| --------- | --------- | ------ | --------- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Waveform
| identifying  | and  | using  | fault  waveform  |     | features  | for  fault  |     |     |     |     |     |     |     |
| ------------ | ---- | ------ | ---------------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Measurement
identification, the classification performance achieved may be
inadequate for practical applications. An acceptable level of
accuracy (80%) is achieved with only contextual features and
by combining contextual and waveform features.
Waveform
| The  concern  | with  | classifying  | faults  | using  | only  | contextual  |     |     |     |     |     |     |     |
| ------------- | ----- | ------------ | ------- | ------ | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
database
features is that actual measurements or observation of the

event are not considered. In practice, physical observations,
| e.g.  flashover          |     | markings  | on  towers,  |     | are  important  | for  |     |                  |     |     |     |     |     |
| ------------------------ | --- | --------- | ------------ | --- | --------------- | ---- | --- | ---------------- | --- | --- | --- | --- | --- |
| confirming fault cause.  |     |           |              |     |                 |      |     | Post-processing  |     |     |     |     |     |
and
The results of automatically classifying faults according to
cause  demonstrate  the  suitability  of  pattern  recognition  characterization
| techniques     | (particularly  |     | 1-NN         | classifiers)  | for     | practical    |     |     |     |     |     |     |     |
| -------------- | -------------- | --- | ------------ | ------------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| applications.  | Classifying    |     | the  causes  | of            | faults  | within  the  |     |     |     |     |     |     |     |
operational timeframe applicable in a control center has the
|            |              |      |                   |         |               |             |     | Waveform  |     |     | Contextual  |     |     |
| ---------- | ------------ | ---- | ----------------- | ------- | ------------- | ----------- | --- | --------- | --- | --- | ----------- | --- | --- |
| potential  | to  improve  |      | transmission      | system  | reliability.  | The         |     |           |     |     |             |     |     |
|            |              |      |                   |         |               |             |     | features  |     |     | features    |     |     |
| relevant   | timeframe    | has  | been  identified  |         | as  less      | than  five  |     |           |     |     |             |     |     |
|            |              |      |                   |         |               |             |     | database  |     |     | database    |     |     |
minutes [35]. This work lays the foundation for implementing
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
automatic classification of transmission line faults within the
operational requirements of a transmission system, following
| the  structure  | shown  |     | in  Fig.  | 8.  The  | following  | are  the  |     |     |     |     |     |     |     |
| --------------- | ------ | --- | --------- | -------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
requirements for implementing real-time classification:
| a)  Knowledge  |     | of  | the  power  | system  | network,  | its  |     |     |     |     |     |     |     |
| -------------- | --- | --- | ----------- | ------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Combined
parameters, external geography and climate play a key  features
role  in  identifying  fault  causes.  These  contextual  database
features should be tabulated in a dataset that can be

linked to fault measurement waveform data.
b)  Appropriate feature extraction from waveform data is
critical. This may be done either on the fault waveform
recorder (or its associated software) or in a centralized  Pattern
Recognition &
database. For faster classification, it is preferable to
conduct post-processing and feature extraction on the  Result Output

fault waveform recorder. Where legacy devices are in
Fig. 8: Structure for operational fault classification
use, without the requisite software or processing power
to conduct post-processing and feature extraction, it is
|     |     |     |     |     |     |     |     |     | VI.  | CONCLUSIONS   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | --- | --- |
recommended that waveforms should be retrieved to a
central database for centralized feature extraction.  It has been shown that both contextual and waveform features
can be identified which have a varying degree of relevance to
c)  Waveform and contextual features should be combined
in  a  single  database  forming  the  platform  for  performing  classification  of  events.  The  accuracy  of
classification.  classification using these features has been demonstrated by
building classifiers using nested subsets. Best classification is

|     |     |     |     |     |     |     | achieved        | using  | only          | contextual  |           | features;  | however  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ------------- | ----------- | --------- | ---------- | -------- |
|     |     |     |     |     |     |     | classification  | in     | this  manner  | does        | not       | make  use  | of  any  |
|     |     |     |     |     |     |     | measurements.   |        | Taking        | waveform    | features  | based      | on       |
measurements into account, classification accuracy of 86% is
|     |     |     |     |     |     |     | achieved  | using      | the  following  | set       | of        | six  contextual  | and    |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --------------- | --------- | --------- | ---------------- | ------ |
|     |     |     |     |     |     |     | waveform  | features:  | Hour,           | Negative  | sequence  | current          | (half  |
cycle after fault initiation), Region, Positive sequence fault
current time constant, Month and Faulted Phases.

|     |     |     |     |     |     |     | The  highest  | classification  |     | accuracy  | achieved  | using  | only  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------------- | --- | --------- | --------- | ------ | ----- |
waveform features is 80%. This indicates that faults can be
classified for underlying cause using only waveform features
with a reasonable level of success. However this performance
is inferior to classification accuracies achieved when using
waveform features in combination with contextual features.

This research shows that the underlying cause of transmission
|     |     |     |     |     |     |     | line  faults  | can  | be  classified  |     | automatically.  | The  | results  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | --------------- | --- | --------------- | ---- | -------- |
0885-8977 (c) 2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPWRD.2015.2503478, IEEE
Transactions on Power Delivery
Paper TPWRD-00902-2015 9
achieved indicate that the 1-NN classifier is a suitable [17] R Duin, F. Roli,D. De Ridder, “A note on core research issues for
classifier for identifying the causes of transmission line faults statistical pattern recognition”, Pattern Recognition Letters, vol. 23,
no.1, pp. 493-499, Feb.2002
and achieves superior classification in comparison to other
[18] V. Ziolowski, I. da Silva, R. Flauzino, “Automatic identification of
classifiers. This work lays a foundation for operational
faults in power systems using control technique” Proceedings of thee
classification of transmission line faults and the key 16th International Conference on Control Applications. Singapore,
requirements and structure of a fault classification system 2007.
have been developed. [19] J. Mora-Florez, J. Cormane-Angarita, G. Ordonez-Plata, “K-means
algorithm for power quality applications”, Electric Power Systems
Research, vol. 79, no. 5 , pp. 714-721, 2009.
ACKNOWLEDGEMENTS
[20] L. Xu, M. Chow, “Distribution fault diagnosis using a hybrid algorithm
The contribution of fault and measurement data by Eskom of fuzzy classification and artificial immune system”, Proceedings of
Holdings is acknowledged. IEEE PES General Meeting - Conversion and Delivery of Electrical
Energy. Raleigh, 2008
[21] R. Teive, J. Coelho, P. Charles, T. Lange, L. Cimino, “A bayesian
REFERENCES
network approach to fault diagnosis and prognosis in power transmission
[1] L. Alvehag, L. Soder, “A reliability model for distribution systems systems”, Proceedings of the 16th International Conference on
incorporating seasonal variations in severe weather” IEEE Trans. Intelligent System Application to Power System (ISAP). Crete, 2011
Power Delivery, vol. 26, no. 2, pp. 910-919, Apr. 2011. [22] M. Chow, S. Yee, L. Taylor, “Recognizing animal-caused faults in
[2] Cigre, Economic Framework for Power Quality, JWG Cigre-CIRED power systems using artificial neural networks” IEEE Transactions on
C4.107, 2011 Power Delivery, vol. 8, no. 3, pp. 1268-1273, Jul. 1993
[3] A. Chowdhury, D. Koval , “Development of transmission reliability [23] S. Meher, A. Pradhan, “Fuzzy classifiers for power quality event
performance benchmarks” IEEE Trans. Industrial Applications, vol. 36, analysis” Electric Power Systems Research, vol. 80,no.1 , pp. 71-76,
no. 3, pp. 899-903, Jun. 2000. 2010
[4] L. Xu, M. Chow, “A classification approach for power distribution [24] B. Ravikumar, D. Thukaram, D., H. Khincha, “Application of support
systems fault cause identification”, IEEE Trans. Power Systems, vol. 21, vector machines for fault diagnosis in power transmission system”, IET,
no.1, pp. 53-60, Feb. 2006. Generation, Transmission and Distribution, vol. 2. no.1, pp. 119-130,
Jan. 2008
[5] H. Vosloo, “The need for and contents of a life cycle management plan
for Eskom transmission line servitudes”, M.Sc Thesis, Dept. Geography, [25] Y. Cai, M. Chow, “Exploratory analysis of massive data for distribution
Univ. Johannesburg, Gauteng, South Africa, 2005. fault diagnosis in smart grids”, IEEE PES General Meeting. Calgary,
Jul. 2009
[6] Electromagnetic compatibility (EMC) - Part 4-30: Testing and
measurement techniques - Power quality measurement methods, [26] U. Minnaar, C. Gaunt, F. Nicolls, “Characterisation of power system
IEC61000-4-30, 2008. faults on South African transmission power lines” Electric Power
Systems Research, vol. 88, nol.1, pp. 25-32,Jul. 2012
[7] M. Bollen, “Algorithms for characterizing measured three-phase
unbalanced voltage dips”, IEEE Trans. Power Delivery, vol. 18, no. 3, [27] J.D. Glover, M. Sarma , Power System Analysis and Design. Pacific
pp. 937-944, 2003. Grove, Brooks/Cole, 2002.
[8] Electric Supply - Quality of Supply Part 2: voltage [28] U.J. Minnaar, “The Characterisation and Automatic Classification of
characteristics,compatability levels, limits and assessment methods, NRS Transmission line faults according to Underlying Cause” Ph.D.
048-2:2007,2007 Dissertation, Elec. Eng., UCT, Cape Town, South Africa, 2014
[9] R. Koch, A. Botha, P. Johnson, R. McCurrach , R. Ragoonanthun, [29] R. Duin, P. Juszczak, P. Paclik, E. Pekalska, D. De Ridder, D. Tax,
“Developments in voltage dip (sag) characterisation and the application PRTools 4, A Matlab Toolbox for Pattern Recognition. Delft University
to compatibility engineering of utility networks and industrial plants”, of Technology,Delft, 2000.
Proceedings of the 3rd Southern African Power Quality Conference. [30] R. Duda, P. Hart, D. Stork, Pattern Classification. Wiley-Interscience,
Livingston, Zambia Oct. 2001. New York, 2000.
[10] M. Bollen, I. Gu, E. Styvaktakis, “Classification of Underlying Causes [31] A. Jain, R. Duin , J. Mao, “Statistical pattern recognition: a review”,
of Power Quality Disturbances: Deterministic versus Statistical IEEE Transactions on Pattern Analysis and Machine Intelligence, vol.
Methods” EURASIP Journal on Advances in Signal Processsing, vol. 1, 22, no. 1, pp. 4-37,Jan. 2000.
pp. 1-17. Feb. 2007.
[32] V. Garcia, R. Mollineda, J. Sanchez, “On the k-nn performance in a
[11] M. Bollen, I. Gu, S. Santoso, M. Mcgranaghan, P. Crossley, M. Ribeiro, challenging scenario of imbalance and overlapping”, Pattern Analysis
“Bridging the gap between signal and power”, IEEE Signal Processing and Applications, Vol. 11, pp. 269-280,Sept. 2008
Magazine, vol. 26, no. 4, pp. 12-31. Jul. 2009.
[33] M. Kubat, R. Holte, S.Matwin, “Machine learning for the detection of
[12] R. Fernandez, H. Rojas, “An overview of wavelet transform in oil spills in radar images” Machine Learning, vol. 30, no. 1, pp. 195-
application in power systems”, Proceedings of the 14th Power Systems 215, Feb. 1998
Computation Conference, Sevilla, Spain, Jun. 2002.
[34] Y. Nan, K. Chai, W. Lee, H.Chai, H, “Optimizing f-measure: a tale of
[13] I. Gu, E. Styvaktakis, “Bridge the gap: Signal processing for power two approaches” 29th International Conference on Machine Learning.
quality applications”, Electric Power Systems Research, vol. 66, no. 1, Edinburgh, Jun. 2012
pp. 83-96, Jul. 2003
[35] J. Bekker, P. Keller, “Enhancement of an Expert System Philosophy for
[14] E. Styvaktakis, M. Bollen, I. Gu, “Expert system for classification and Automatic Fault Analysis”, 11th Annual Georgia Tech Fault and
analysis of power system events”, IEEE Trans. Power Delivery, vol. 17, Disturbance Analysis Conference, Atlanta, 2002, Available:
no.2, pp. 423-428, Apr. 2002 http://truc.org/media/1292/enhancement-of-an-expert-system-
[15] V. Barrera , J. Melendez, S. Kulkharni, S. Santoso, “Feature analysis and philosophy-for-automatic-fault-analysis.pdf
automatic classification of short circuit faults resulting from external Ulrich Minnaar received the BSc (Eng) in 2001, MSc (Eng)
causes”, European Transactions on Electrical Power, vol.23, no.4, pp.
in 2006 and PhD in 2014. Trevor Gaunt is an Emeritus
510-525, Jan. 2012.
Professor in the Department of Electrical Engineering at the
[16] P. Jonker, R. Duin, D. De Ridder, “Pattern recognition for metal defect
detection” Steel Grips, vol. 1, no.1, pp. 20-23. 2003 University of Cape Town. Fred Nicolls is an Associate
Professor in the Department of Electrical Engineering at the
University of Cape Town.
0885-8977 (c) 2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.