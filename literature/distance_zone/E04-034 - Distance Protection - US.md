Distance Protection

Course No: E04-034
Credit: 4 PDH

Velimir Lackovic, Char. Eng.

Continuing Education and Development, Inc.

P: (877) 322-5800
info@cedengineering.com

www.cedengineering.com

Distance Protection – E04-034

Combination of fast fault clearance, with selective operation of protection elements, is

the  main  objective  for  the  protection  of  electrical  power  systems.  To  fulfill  these

demands, high-speed protection arrangements for electric transmission and distribution

networks  that  are  used  with  the  automatic  reclosure  of  circuit  breakers  are  under

constant research. Distance protection, is a non-unit protection arrangement providing

significant  financial  and  technical  benefits.  Unlike  phase  and  neutral  overcurrent

protection arrangements, the key benefit of distance protection is that the short circuit

current coverage of the protected element is almost autonomous of source impedance

changes. This principle is shown in Figure 1. It can be noted that overcurrent protection

cannot be used satisfactorily.

ZS=10Ω

ZS=10Ω

Z1=4Ω

F1

220 kV

I>>

R1

IF1  =

220X103
√3X(S+4)

= 14113 A - Relay R1 setting > 14113 A

ZS=10Ω

Z1=4Ω

220 kV

F2

I>>

R1

IF2

3

= 220X10
√3X10

= 12702 A - Relay R
1

setting > 12702 A

Figure 1. Benefits of distance over overcurrent protection

(Relay current setting <12702 A and >14113 A. This is not practical; overcurrent
protection relay is not appropriate. Distance or unit protection is preferred).

2

Distance Protection – E04-034

Distance  protection  is  relatively  simple  to  use,  and  it  can  be  quick  in  service  for

short circuits along most of the protected elements. It can also provide primary and

remote back-up functions in a single operating arrangement. It can simply be adjusted

to make a unit protection arrangement when used with a communication link. In this

arrangement, it is eminently applicable for usage with high-speed auto-reclosing for

the protection of major transmission circuits.

DISTANCE RELAY FOUNDATIONS

Since the impedance of a transmission circuit is relative to its length, it is suitable to

use a relay capable of measuring the impedance of a circuit up to a present point

(the reach point). Such protection relays are known as “distance  protection relays”

and only function in case of faults that occur between the location of the protection

relay  and  the  chosen  reach  point.  Therefore,  they  provide  discrimination  for  short

circuits that may occur in different line portions.

The fundamental rule of distance protection includes the division of the voltage at the

relaying point by the measured current. The calculated impedance is equated with the

reach  point  impedance.  When  the  measured  impedance  is  lower  than  the  reach

point impedance, it is presumed that a fault is on the circuits between the relay and

the reach point. The reach point of a protection relay is the point along the transmission

line impedance locus that is crossed by the boundary feature of the protection relay.

Since  this  depends  on  the  ratio  of  voltage  and  current,  and  the  phase  angle

between  them,  it  may  be  shown  on  an  R/X  graph.  The  loci  of  electrical  power

system impedances, as detected by the protection relay during faults, power swings

and load changes, may be shown on the same graph. The service of the protection

relay in the presence of electrical system faults and disturbances may be examined

using this method.

RELAY OPERATION

Distance  protection  relay  operation  is  expressed  in  terms  of  reach exactness  and

operating time. Reach exactness is a comparison between the real ohmic reach of

the protection relay under real circumstances with the protection relay setting value

in ohms. Reach exactness is especially dependent on the level of voltage shown to

the protection relay during the fault period. The impedance measuring methodologies

used in special relay arrangements also have an influence.

3

Distance Protection – E04-034

Functioning  times  can  change  with  short  circuit  current,  short  circuit  position

relative to the protection relay setting, and the point on the voltage wave at which the

short  circuit  happens.  Depending  on  the  measuring  processes  used  in  a  specific

relay  arrangement,  measuring  signal  transient  errors,  such  as  those  made  by

capacitor voltage transformers or saturating CTs, can adversely slow down the relay

function  for  short  circuit  currents  close  to  the  reach  point.  It  is  typical  for

electromechanical and static distance protection relays to claim both maximum and

minimum functioning times. Nevertheless, for modern digital or numerical distance

protection  relays,  the  change  between  them  is  negligible  over  a  wide  range  of

electrical system operating states and fault locations.

ELECTROMECHANICAL/STATIC DISTANCE PROTECTION RELAYS

With electromechanical and static protection relay arrangements, the magnitude of

input  quantities  is  determined  by  both  reach  exactness  and  functioning  time.  It  is

common  to  present  the  data  on  relay  operation  by  voltage/reach  curves,  as

presented  in  Figure  2,  and  the  servicing  time/fault  location  curves  for  different

values  of  electrical  system  impedance  ratios  (S.I.R.s)  as  presented  in  Figure  3,

where:

And

S. I. R =

Zs

ZL

ZS – electrical system source impedance behind the relay points

ZL – electrical line impedance equivalent to protection relay reach setting

4

Distance Protection – E04-034

0

20

40

60

% relay rated voltage - Phase-earth faults

0

20

40

60

80

100

% relay rated voltage - Phase - phase faults

h
c
a
e
r

e
c
n
a
d
e
p
m

I

)
g
n
i
t
t
e
s
1

e
n
o
Z
%

(

h
c
a
e
r

e
c
n
a
d
e
p
m

I

)
g
n
i
t
t
e
s
 1
e
n
o
Z
%

(

105

104

103

102

101

100

99

98

97

105
104
103
102
101
100
99
98
97
96
95

h
c
a
e
r

e
c
n
a
d
e
p
m

I

)
g
n
i
t
t
e
s
 1
e
n
o
Z
%

(

105
104
103
102
101
100
99
98
97
96
95

0

20

40

60

80

100

% relay rated voltage - Three phase and three phase
earth faults

Figure 2. Common impedance reach exactness characteristics for Zone 1

5

Distance Protection – E04-034

)
s
m

(

e
m

i
t
n
o
i
t
a
r
e
p
O

50
45
40
35
30
25
20
15
10
5
0

0

20

40

60

80

100

Fault position (% relay setting) - System impedance ratio 1/1

Min

Max

)
s
m

(

e
m

i
t
n
o
i
t
a
r
e
p
O

50
45
40
35
30
25
20
15
10
5
0

0

20

40

60

80

100

Fault position (% relay setting) - System impedance ratio
30/1

Min

Max

Figure 3. Common functioning time characteristics for Zone 1 line-line faults

Instead, the  above data  is  mixed with a  family  of contour  curves,  where  the  short

circuit  current  location,  given  as  a  percentage  of  the  protection  relay  setting,  is

presented against the source to line impedance ratio, as shown in Figure 4.

6

Distance Protection – E04-034

1.2

1

0.8

0.6

0.4

0.2

)
L
Z

0
0.01

1.2

1

0.8

0.6

0.4

0.2

)
L
Z

0
0.01

g
n
i
t
t
e
s
y
a
l
e
r

.

.

u
p
(
n
o
i
t
i
s
o
p
t
l
u
a
F

g
n
i
t
t
e
 s
y
a
l
e
r

.

.

u
p
(
n
o
i
t
i
s
o
p
t
l
u
a
F

0.1

1
ZS/ZL or S.I.R.

10

100

9 ms

13 ms

Boundary

0.1

1
ZS/ZL or S.I.R.

10

100

15 ms

20 ms

Boundary

Figure 4. Common function-time contours (a) Zone 1 line-line fault: minimum

performance times (b) Zone 1 line-line fault: maximum performance times

DIGITAL/NUMERICAL DISTANCE PROTECTION RELAYS

Digital/Numerical distance protection relays usually have more coherent performance

times. The best transmission-class protection relays can reach sub-cycle functioning,

and the available digital filtering processes guarantee optimum service under adverse

waveform circumstances or boundary fault conditions.

RELATIONSHIP BETWEEN RELAY VOLTAGE AND ZS/ZL RATIO

A unique, generic, and an equivalent circuit, as presented in Figure 5, may correspond
to any

7

Distance Protection – E04-034

short circuit current condition in a three-phase electrical power system. The voltage V

enforced  to  the  impedance  loop  is  the  open  circuit  voltage  of  the  electrical  power

system. Point R corresponds to the relay position; IR and VR are the current and voltage

sensed by the relay.

The  impedances  Zs and  ZL are  depicted  as  source  and  transmission  line  impedances

due to their location relative to the relay. Source impedance Zs is a quantity of the short

circuit  current  at  the  relaying  location.  For  short  circuit  currents  involving  ground,  it

depends on the technique of electrical system grounding behind the relaying location.

Line impedance ZL is a quantity of the impedance of the protected region. The voltage

VR utilized  to  the  protection  relay  is  IRZL.  The  short  circuit  current  at  the  reach  point,

may be conveyed in terms of source to transmission line impedance ratio ZS/ZL using

the following equation:

Where

Hence,

Or

VR = IRZL

IR =

 V
ZS + ZL

VR =

ZL  V

ZS + ZL

VR = V/ (1 + (ZS/ZL))

(1)

Source

Line

ZS

V

IR

VR

ZL

8

Distance Protection – E04-034

100

90

80

70

60

50

40

30

20

)
e
g
a
t
l
o
v

10

)
d
e
t
a
r

%

(
R
V
e
g
a
t
l
o
V

0

0.1

1
System impedance ratio ZS/ZL

10

Figure 5. Link between source to transmission line ratio and protection relay voltage

(a) Electrical power system arrangement (b) Change in protection relay voltage with

electrical system source to transmission line impedance ratio

The universal relationship between VR and ZS/ZL, presented in Figure 5, is valid for all

cases of short circuit currents provided  that few elementary rules are kept. These

rules are:

- For  line  faults,  V∆  is  the  line-line  source  voltage  and  ZS/ZL  is  the  positive

sequence  source  to  transmission  line  impedance  ratio.  VR  and  IR  are  the

line-line protection relay voltage and current respectively.

VR = V∆ /(1+ (ZS/ZL))

(2)

- For  ground  short  circuit  currents,  Vl-n is  the  line-neutral  source  voltage  and

ZS/ZL  is  a  composite  ratio  representing  the  positive  and  zero  sequence

impedances.  VR  is  the  line-neutral  protection  relay  voltage  and  IR  is  the

protection relay  current for the faulted line.

V  =
R

Where:

1
2+p

ZS)(
(
ZL    2+q

)+1 V1-n

(3)

9

Distance Protection – E04-034

And

ZS = 2ZS1 + ZS0 = ZS1(2 + p)

ZL = 2ZL1 + ZL0 = ZL1(2+ q)

p =

q =

ZS0
ZS1

ZL0
ZL1

VOLTAGE LIMIT FOR PRECISE REACH POINT MEASUREMENT

The  ability  of  a  distance  protection  relay  to  precisely  assess  the  reach  point  fault

depends  on  the  minimum  voltage  at  the  protection  relay  position.  This  voltage,

which  depends  on  the  protection  relay  arrangement,  can  also  be  expressed  in

terms  of  an  equivalent  maximum  ZS/ZL  or  S.I.R.  Distance  protection  relays  are

made in a specific way that once the reach point voltage standard is reached, any

increase in measuring errors for short circuits closer to the protection relay has no

effect  on

the  protection

relay  performance.  Most  protection

relays  are

manufactured  with  healthy  line  voltage  polarization  and/or  memory  voltage

polarization. The primary use of the protection relay voltage polarization is to ensure

a correct directional response for close-up short circuit currents, both in forward or

reverse directions, where the fault-loop voltage sensed by the protection relay may

be very low.

DISTANCE PROTECTION ZONES

The  careful  choice  of  reach  settings  and  operation  times  for  the  different  zones

allows proper coordination between distance protection relays on an electric power

system. Fundamental distance protection will contain an instantaneous directional

Zone 1 relay protection and one or more time-delayed zones. Common reach and

time settings for a 3-zone distance relay protection are presented in Figure 6. Digital

and numerical distance protection relays may have up to five or six protection zones,

some  are  set  to  sense  in  the  reverse  direction.  The  common  settings  for  three

forward-looking zones of a basic distance relay protection are shown in the following

paragraphs. To find out the settings for a specific protection relay arrangement or a

specific distance tele-protection arrangement that involves end-to-end signaling, the

producer’s suggestions and manuals should be considered.

10

Distance Protection – E04-034

ZONE 1 PROTECTION SETTING

Electromechanical/static protection relays typically have a reach setting of up to 80%

of the protected transmission line impedance for instantaneous Zone 1 protection. For

digital/numerical distance protection relays, settings of up to 85% may be adequate.

The  obtained  15-20%  safety  margin  assures  the  Zone  1  protection  from

overreaching  the  protected  transmission  circuit  due  to  errors  in  the  current  and

voltage transformers, and inaccuracies in transmission line impedance information.

Otherwise,  there  would  be  improper  discrimination  with  fast  functioning  relay

protection  on  the following transmission  line section. Zone 2  of the distance relay

protection has to cover the remaining 15-20% of the transmission line.

ZONE 2 PROTECTION SETTING

To assure complete coverage of the transmission line with provision for the sources

of error already presented in the previous paragraph, the reach protection setting of

the Zone 2 protection needs to be at least 120% of the protected transmission line

impedance.  In  many  cases  it  is  a  typical  practice  to  set  the  Zone  2  reach  to  be

same as the protected transmission line section and +50% of the shortest adjacent

transmission  line.  Where  feasible,  this  assures  that  the  maximum  effective

protection Zone 2 reach does not go beyond the minimum effective protection Zone

1  reach  of  the  adjacent  transmission  line  protection.  This  eliminates  the

requirement  to  grade  the  protection  Zone  2  time  settings  between  upstream  and

downstream  protection  relays.  In  electromechanical  and  static  protection  relays,

Zone 2 protection is given either by different elements or by extending the protection

reach of the Zone 1 devices after a time delay that is started by a fault detector. In

the majority of digital and numerical protection relays, the Zone 2 devices are put in

software.

Zone 2 tripping has to be time-delayed to assure grading with the primary protection

relay  used  in  adjacent  transmission  circuits  that  fall  within  the  Zone  2  protection

reach.  Hence,  full  coverage  of  a  transmission  line  portion  is  achieved,  with  fast

clearance of short circuits in the first 80-85% of the transmission line and reasonably

slower short circuit current clearance in the remaining portions of the transmission

circuit.

11

Distance Protection – E04-034

Time

Source

0

Time

Z3JR

Z3JF

Z2J

Z1J

Y
X

 Z1L

Source

H

J

K

L

Z1H

X
Y

Z1K

Z2K

Z3K

Z3KR

Figure 6. Common time/distance characteristics for three zone distance relay
protection

Zone 1 =80-85% of protected transmission line impedance

Zone 2 (minimum)=120% of protected transmission line

Zone 2 (maximum)<Protected transmission line+50% of shortest second
transmission line

Zone 3F=1.2 (protected transmission line +longest second transmission line)

Zone 3R=20% of protected transmission line

X= Circuit breaker tripping time

Y= Discriminating time

ZONE 3 PROTECTION SETTING

Remote back-up relay protection, for all short circuit currents on adjacent transmission

lines, can be given by a third zone that is time delayed to discriminate with Zone 2 relay

protection  and  the  circuit  breaker  operation  time  for  the  adjacent  transmission  line.

Protection Zone 3 reach should be adjusted to at least 1.2 times the impedance given

to the protection relay for a short circuit at the remote end of the second transmission

line  portion.  On  interconnected  electrical  power  systems,  the  impact  of  short  circuit

current infeed at the remote bus will create a much higher impedance at the protection

relay  than  the  actual  impedance  to  the  short  circuit.  This  has  to  be  considered  when

setting the protection Zone 3. In some electrical systems, differences in the remote bus

infeed  can  prohibit  the  usage  of  remote  back-up  protection  Zone  3.  However,  there

should  not  be  any  problem  on  radial  distribution  electrical  systems  with  single  end

infeed.

12

Distance Protection – E04-034

PROTECTION SETTINGS FOR REVERSE REACH AND OTHER ZONES

Modern digital or numerical protection relays may have extra impedance zones that

can be used to provide extra protection functions. For instance, when the first three

protection zones are set as above, Zone 4 could be used to give back-up protection

for the local bus, by using a reverse reach setting of the order of 25% of the protection

Zone 1 reach. Also, in addition to its forward reach setting, one of the forward-looking

protection zones (usually Zone 3) could be adjusted with a low reverse offset reach

from the origin of the R/X graph. An offset impedance measurement characteristic is

non-directional.  One  benefit  of  a  non-directional  protection  zone  of  impedance

measurement is that it is capable to function for a close-up, zero-impedance short

circuit, where there may be no healthy line or memory voltage signals available to

permit the performance of a directional impedance zone. With the  offset-zone time

delay bypassed, Switch-on-to-Fault’ (SOTF) protection can be used. This is needed

when line voltage transformers give a fast  tripping during inadvertent transmission

line energization with maintenance grounding clamps left in place. Extra impedance

zones  may be  positioned  as  part of  a distance relay protection arrangement used

with a tele-protection signaling medium.

DISTANCE PROTECTION RELAY FEATURES

Some  numerical  relays  measure  the  absolute  fault  impedance,  and  then  check  if

operation is needed according to impedance boundaries predetermined on the R/X

graph. Typical distance and numerical protection relays, that emulate the impedance

elements  of  common  protection  relays,  do  not  measure  absolute  impedance.

These  protection  relays  compare  the  sensed  short  circuit  voltage  with  a  replica

voltage, deduced from the short circuit current and the zone impedance settings, to

check  if  the  short  circuit  is  within  or  out-of-zone.  Distance  protection  relay

impedance  comparators  or  algorithms  which  emulate  typical  comparators  are

organized in line with their polar features, the number of signal inputs they contain,

and the procedure by which signal comparisons are determined. The typical types

compare either the relative amplitude or the phase of two input measures in order

to get performance features that are either straight lines or circles when printed on

an R/X graph.  At  each  stage  of  distance  protection  relay  design,  the

13

Distance Protection – E04-034

features  and  shapes  of  the  impedance  performance  have  been  regulated  by  the

present technology at acceptable costs. Since many typical protection relays are still

in  operation,  and  some  numerical  protection  relays  emulate  the  processes of the

typical protection relays, a brief review of impedance comparators is needed.

AMPLITUDE AND PHASE COMPARISON

Protection relay measuring devices, in which practicality is determined on the basis

of  comparing  two independent measures, are basically either amplitude or phase

comparators.  For  impedance  elements  of  a  distance  protection  relay,  the

measurements compared are the voltage and current sensed by the protection relay.

There  are  different  methodologies  for  completing  the  comparison  based  on  the

used  technology.  They  differ  from  a  balanced  beam  (amplitude  comparison)  and

induction  cup  (phase  comparison)  electromagnetic  protection  relays,  even  from

diode and operational amplifier comparators in static-type distance protection relays,

to digital sequence comparators in digital protection relays and to algorithms used in

numerical protection relays.

Any  method  of  impedance  feature  obtained  with  one  comparator  is  also  obtained

with  another.  The  addition  and  subtraction  of  the  signals  for  one  type  of

comparator provide  the  necessary  signals  to  obtain  a  similar  characteristic  using

the other type. For instance, comparing V and I in an amplitude comparator ends in

a circular impedance characteristic placed at the origin of the R/X graph. If the sum

and difference of V and I are put to the phase comparator, the end result is a similar

characteristic.

PLAIN IMPEDANCE CHARACTERISTIC

The  plain  impedance  characteristic  does  not  take  into  account  the  phase  angle

between the current and the voltage. For this reason, the impedance characteristic

printed  on  an  R/X  graph  is  a  circle  with  its  center  at  the  origin  of  the  coordinates

and  of  radius  similar  to  its  setting  in  ohms.  The  operation  happens  for  all

impedance quantities less than the setting, that is, for all points inside the circle. The

protection relay characteristic, presented in Figure 7, is hence non-directional, and in

this form it would trip for all short circuit currents along the vector AL and for all

14

Distance Protection – E04-034

short  circuits  behind  the  bus  to  an  impedance  AM.  A  is  the  protection  relaying  point,

and RAB is the angle by which the short circuit current lags the protection relay voltage

for a short circuit on the line AB, and RAC is the same leading angle for a short circuit

on line AC. Vector AB displays the impedance in front of the protection relay between

the  point  A  and  the  end  of  line  AB.  Vector  AC  presents  the  impedance  of  line  AC

behind the protection relaying point. AL presents the reach of instantaneous protection

Zone 1, and covers 80% to 85% of the protected transmission line.

Line AC

Line AB

C

B

A

X

Z<

B

Restrai

L

 Operat

Line
Zo
n
e 1

A

R

Line

C

M

Impedance

Figure 7. Plain impedance protection relay characteristic

A protection relay using this characteristic has three important  drawbacks:

-

It  is  non-directional;  it  will  sense  short  circuits  both  in  front  and  behind  the

protection  relaying  point,  and  hence  it  needs  a  directional  device  to  provide  it

with exact discrimination.

15

Distance Protection – E04-034

-

-

It has a non-uniform short circuit resistance coverage.

It is non-resistant to power oscillations and heavy loading of a long transmission

line because of the large area covered by the impedance circle.

Directional control is a basic discrimination measure for a distance protection relay,

which  makes  the  protection  relay  non-responsive  to  short  circuits  outside  the

protected  transmission  line.  This  can  be  received  by  the  addition  of  a  separate

directional  control  device.  The  impedance  characteristic  of  a  directional  control

device  is  a  straight  line  on  the  R/X  graph.  The  mixed  characteristic  of  the

directional  and  impedance  protection  relays  is  the  semi-circle  APLQ  displayed  in

Figure 8.

16

Distance Protection – E04-034

X

B

mpedance
I

element Rz

P

Operates

L

Line AB

Zone
1

A

R

Restrains

Q

IF1

IF2

B

D

A

C

Z<

F

&

&

Trip relay

Combined directional/impedance relay

Directional

element R0

RAZ<

RAD

RAD

RAZ<  -  distance  device  at  A

RAD – directional device at A

 Figure 8. Mixed directional and impedance protection relays (a) Characteristic of

mixed  directional/impedance

relay

(b)  Example  of  directional/Impedance

protection relay (c) Logic for directional and impedance protection devices at A

17

Distance Protection – E04-034

If a short circuit occurs at F near C on the parallel line CD, then the directional unit

RD  at  A  will  hold  due  to  current  IF1.  At  the  same  time,  the  impedance  element  is

retained  by  the  inhibiting  output  of  unit  RD.  If  this  control  is  not  given,  the  under

impedance device could function prior to the tripping of circuit breaker C. The reversal of

the current through the protection relay from IF1 to IF2 while opening C, could end up

in an incorrect operation of the healthy transmission line if the directional element RD

operates before  the  impedance  unit  resets.  Thus,  there  is  a  need  to  address  the

adequate  coordination  of  multiple  protection  relay  elements  to  achieve  a  reliable

performance during evolving fault conditions. In older protection relay arrangements,

this type of problem is typically referred to as one of ‘contact race’.

SELF-POLARISED MHO PROTECTION RELAY

The mho impedance element is typically known as such, since its characteristic is

a  straight  line  on  an  admittance  graph.  It  mixes  the  discriminating  measures  of

both  reach  control  and  directional  control,  therefore  cancelling  the  ‘contact  race’

issues that may be found with separate reach and directional control devices. This

is  accomplished  by  introduction  of  a  polarizing  signal.  Mho  impedance  devices

were  especially attractive due  to  financial reasons where  electromechanical relay

devices were used. Finally, they have been used for many years and their benefits

and  drawbacks  are  well-known.  For  this  reason,  they  are  still  implemented  in  the

algorithms  of  some  numerical  protection  relays.  The  characteristic  of  a  mho

impedance device, when printed on an R/X graph, is a circle whose circumference

passes  through  the  origin,  as  shown  in  Figure  9.  This  shows  that  the  impedance

device is inherently directional and will function only for short circuits in the forward

direction along line AB.

The  impedance  characteristic  is  adapted  by  setting  Zn,  the  impedance  reach,  the

diameter and φ, the angle of displacement of the diameter from the R-axis. Angle φ

is known as the Relay Characteristic Angle (RCA). The relay acts for quantities  of

fault  impedance  ZF  within  its  characteristic.  The  self-polarized  mho characteristic

can be found using a phase comparator circuit which compares input signals S2 and

S1, and performs whenever S2 lags S1 by 90° to 270°, as presented in the voltage

graph of Figure 9.

18

The two input signals are:

Distance Protection – E04-034

S2 = V - IZn

S1 = V

where:

V - fault voltage from VT secondary

I - fault current from CT secondary

Zn - impedance setting of the  zone

X

ZN

V=IZ0

Restrain

V

φ
Zo
ne
1

Operate

B

X

ZN

ZF

φ
ne
Zo
1

Operate

A

Restrain

K

X

B

P

Q

φ

θ

A

K

Restrain

R

R

R

19

Distance Protection – E04-034

AQ – Relay impedance setting

φ – Relay characteristic angle setting

AB – Protected transmission line

PQ – Arc resistance

θ – Line angle

Figure 9. Mho protection relay characteristics (a) Phase comparator inputs (b) Mho

impedance characteristics (c) Increased arc resistance coverage

The characteristic shown in Figure 9 (a) can be translated to the impedance plane of

Figure 9(b) by dividing each voltage by I. The impedance reach changes with short

circuit  angle.  As  the  protected  transmission  line  is  made  up  of  resistance  and

inductance, its short circuit current angle will depend upon the relative quantities of R

and X at the power system operating frequency. Under an arcing fault condition, or

ground fault involving extra resistance, such as tower footing resistance, the value of

the  resistive  element  of  short  circuit  impedance  will  increase  to  change  the

impedance  angle. Thus a protection relay, having a characteristic angle similar  to

the  transmission  line  angle,  will  under-reach  at  resistive  short  circuit  conditions.

Some  engineers  set  the  RCA  less  than  the  transmission  line  angle,  to  accept  a

small  quantity  of  short  circuit  resistance  without  causing  an  under-reach.

Nevertheless,  when  setting  the  protection  relay,  the  difference  between  the  line

angle θ and the protection relay characteristic angle Ø has to be known. The resulting

characteristic  is  presented  in  Figure  9  where  GL  represents  the  length  of  the

protected transmission line. When angle Ø is smaller than θ, the actual quantity of

protected transmission line AB, would be equal to the protection relay setting quantity

AQ  multiplied  by  cos(θ-Ø).  Hence  the  needed  protection  relay  setting  AQ  is

determined by:

AB

AQ =

cos(0 - <p)

Due to the physical nature of an electric arc, there is a non-linear relationship between

the  arc  voltage  and  arc  current,  which  ends  in  a  non-linear  resistance.  Using  the

empirical equation, the estimated quantity of arc resistance can be determined by:

20

Distance Protection – E04-034

Ra =

28710
/1.4

L

(4)

where:

Ra = arc resistance (ohms)

L = length of arc (meters)

I = arc current (A)

When long overhead transmission lines are installed on steel towers with overhead

ground  wires,  the  impact  of  arc  resistance  can  be  neglected.  The  impact  is

predominant on short overhead transmission lines and with short circuit currents below

2000A (i.e. minimum plant condition), or if the protected transmission line is a wood-

pole construction without ground wires. In the second case, the ground short circuit

resistance decreases the effective ground-fault reach of a ‘mho’ protection Zone 1

device to an extent that the majority of short circuits are sensed in Zone 2 time.

This  issue  can  be  solved  by  using  a  protection  relay  with  a  cross-polarized  mho

with  a  polygonal  characteristic.  When  an  electrical  power  system  is  resistance-

grounded, it does not have to be treated in regards to the protection relay settings

other than the effect that a decreased short circuit current may have on the value of

arc  resistance  sensed.  The  grounding  resistance  is  in  the  source  behind  the

protection  relay,  and  only  changes  the  source  angle  and  source  to  transmission

line  impedance  ratio  for  ground  faults.  Hence,  it  would  only  be  considered  when

examining protection relay operations in terms of system impedance ratio.

OFFSET MHO/LENTICULAR CHARACTERISTICS

Under close up short circuit conditions, when the protection relay voltage drops to zero

or near-zero, a protection relay using a self-polarized mho characteristic or any other

shape  of  self-polarized  directional  impedance  characteristic  may  not  function  as

needed.  Processes  of  covering  this  situation  include  the  use  of  non-directional

impedance characteristics, such as offset mho, offset lenticular, or cross-polarized

and memory polarized directional impedance characteristics. If current bias is used,

the mho characteristic is shifted to embrace the origin, so that the measuring device

can  function  for  close-up  short  circuits  in  both  the  forward  and  the  reverse

directions. The offset mho protection relay has two main uses:

21

Distance Protection – E04-034

Zone
3

Zone
2

Zone
1

R

X

X

Busbar zone

J

H

Zone
1

Zone
3

Zone
2

Carrier stop

R

G

K

Carrier start

Figure 10. Common usage for the offset mho protection relay (a) Bus zone back-up

using an offset mho protection relay (b) Carrier starting in distance blocking

arrangements

THIRD PROTECTION ZONE AND BUSBAR BACK-UP PROTECTION ZONE

This  is  applied  in  conjunction  with  mho  measuring  devices  as  a  short  circuit  detector

and/or  protection  Zone  3  measuring  device.  So,  using  the  reverse  reach  set  up  to

extend  into  the  bus  protection  zone,  as  presented  in  Figure  10,  it  will  give  back-up

protection

for  bus  short  circuits.  This  can  be  presented  with  quadrilateral

characteristics. Another  advantage of using the protection Zone 3 is for Switch-on-to-

Fault  (SOTF)  protection,  where  the  protection  Zone  3  time  delay  would  be  bypassed

for a short period, shortly after line switching, to provide a quick clearance for a short

circuit anywhere along the protected transmission  line.

22

Distance Protection – E04-034

CARRIER STARTING DEVICE IN DISTANCE PROTECTION ARRANGEMENTS

WITH CARRIER BLOCKING

If the offset mho device is utilized for starting carrier signaling, it is arranged as in

Figure 10. The carrier is transferred if the short circuit is external to the  protected

transmission line but inside the reach of the offset mho protection relay. This is to

stop  the  accelerated  operation  of  the  second  or  third  zone  protection  relay  at  the

remote station. Transmission is reverted for internal short circuits by the operation

of  local  mho  measuring  devices, which  provide  high-speed  fault clearance  by  the

local and remote end circuit breakers.

USAGE OF LENTICULAR CHARACTERISTIC

There is a possibility that the offset mho protection relay displayed in Figure 11 may

trip under maximum load transfer conditions if protection Zone 3 has a large  reach

setting. A large protection Zone 3 reach may be needed to provide a remote back-up

protection for short circuits on the adjacent circuit. To avert this, a shaped mode of

characteristic may be utilized, where the resistive coverage is limited. With a

‘lenticular’ characteristic, the aspect ratio of the lens (a) is changeable, allowing it to

b

give  maximum  short  circuit  resistance  coverage  under  maximum  load  transfer

conditions.  Figure  11  presents  how  the  lenticular  characteristic  can  allow  greater

degrees  of  transmission  line  loading  than  offset  mho  and  plain  impedance

characteristics. Decrease of load impedance from ZD3 to ZD1 will relate to the same

rise in load current.

23

Distance Protection – E04-034

X

b

Offset Lenticular

characteristic

Offset Mho

characteristic

ZD3

ZD2

a

ZD1

ZC

Load

R

Area

ZA

ZB

Impedance

characteristic

Figure 11. Minimum load impedance allowed with lenticular, offset mho and

impedance protection relays

It  can  be  noted  in  Figure  11  that  the  load  area  is  fixed  according  to  a  minimum

impedance arc, and is limited by straight lines which exhale from the origin, 0. Modem

numerical  protection  relays  usually  do  not  utilize  lenticular  characteristic  shaping,  but

alternatively utilize load encroachment (load blinder) sensing. This makes the full mho

characteristic to be utilized, but with a stopped tripping in the region of the impedance

plane that is frequented by load  (ZA-ZB-ZC-ZD).

FULLY CROSS-POLARISED MHO CHARACTERISTIC

The  previous  paragraph  presented  how  the  non-directional  offset  mho  characteristic

can  inherently  trip  for  close-up  zero  voltage  short  circuits,  where  there  would  be  no

polarizing  voltage  to  grant  operation  of  a  plain  mho  directional  device.  One  way  of

making sure the correct mho device response for zero-voltage short circuits is to add

a  percentage  of  voltage  from  the  healthy  line(s)  to  the  main  polarizing  voltage  as  a

substitute  phase  reference.  This  method  is  known  as  cross-polarizing,  and  it  has  the

benefit of keeping and increasing the directional features of the mho characteristic. By

the  use  of  a  phase  voltage  memory  technique,  that  gives  several  cycles  of  pre-short

circuit  voltage  reference  during  a  short  circuit,  the  cross-polarization  method  is  also

efficient for close-up three-phase short circuits. For this type of short circuit, no  healthy

24

Distance Protection – E04-034

line voltage reference is usable.

Early  memory  system  techniques  were  established  on  tuned,  resonant  circuits,  but

issues occurred in power networks where the power system operating frequency could

change.  Sophisticated  digital  or  numerical  elements  can  provide  a  synchronous  line

reference  for  changes  in  power  system  frequency  before  or  during  a  short  circuit.

Drawback  of  the  self-polarized  plain  mho  impedance  characteristic,  when  used  on

overhead  transmission  circuits  with  large  impedance  angles,  is  that  it  has  a  fixed

coverage  of  arc  or  fault  resistance.  This  issue  is  worsened  in  short  transmission

circuits, since the ohmic setting of protection Zone 1 is low. The degree of the resistive

coverage provided by the mho circle is linked with the forward reach setting. Therefore,

the ending resistive coverage may be too small compared to the anticipated quantities

of  fault  resistance.  One  extra  advantage  of  using  cross-polarization  to  a  mho

impedance  device is  that  its  resistive  coverage  will  be  improved.  This is  presented  in

Figure  12,  where  a  mho  device  has  100%  cross-polarization.  With  cross-polarization

from the healthy line(s) or from a memory system element, the mho resistive expansion

occurs  during  a  balanced  three-line  short  circuit  as  well  as  for  unbalanced  short

circuits.  The  expansion  will  not  occur  under  load  conditions,  when  there  is  no  phase

shift  between  the  measured  voltage  and  the  polarizing  voltage.  The  increase  in

resistive  reach  depends  on  the  ratio  of  source  impedance  to  protection  relay  reach

(impedance) setting, this can be deduced by referring to Figure  13.

X

R

Figure 12. Fully cross-polarized mho relay characteristic with variations of ZS/ZL

ratio

25

Distance Protection – E04-034

Positive current direction for relay

ZS

ZL

Relay

location

IF

Va1

ZS1

ZL1

N1

E1

Va2

ZS2

N2

Mho unit
characteristic
(not-cross-
polarized)

Ia1

Ia2

X

Zn1

ZL1

Zn2

30°

ZS1

F1

F2

ZL2

S2’=ZL1-Zn1

R

S1’=ZL1+Zn2

Mho unit
characteristic
(fully-cross-
polarized)

Figure 13. Diagram of enhancing protection relay resistive coverage for fully cross-

polarized characteristic

It  is  noteworthy  to  emphasize  that  the  evident  extension  of  a  fully  cross-polarized

impedance characteristic into the negative reactance quadrants of Figure 13 does not

mean that there would be trip for reverse short circuits. With cross-polarization, the

26

Distance Protection – E04-034

relay characteristic extends to cover the beginning of the impedance graph for forward

short circuits only. For reverse short circuits, the impact is to omit the beginning of the

impedance graph, ensuring adequate directional responses for close-up forward or

reverse short circuits. Fully cross-polarized characteristics have now been  greatly

replaced,  due  to  the  trend  of  comparators  linked  with  healthy  line  to  trip  under

heavy short circuit circumstances on another line. This is does not have an effect in

a  switched  distance  protection  relay,  where  a  single  comparator  is  linked  to  the

adequate  short  circuit  loop  impedance  by  starting  units  before  measurements.

Nevertheless,  modern  protection

relays  provide

independent

impedance

measurements  for  each  of  the  three  ground-fault  and  three  line-fault  loops.  For

these protection relays, mal-operation of live lines is not desired, particularly when

single-pole tripping is needed for single-line short circuits.

PARTLY CROSS-POLARISED MHO CHARACTERISTIC

When a dependable, independent technique of a faulted line selection is not given,

a  modern  non-switched  distance  protection  relay  may  only  use  a  comparatively

small  percentage  of  cross  polarization.  The  picked  out  level  has  to  be  enough  to

provide  a  dependable  directional  control  in  the  presence  of  CVT  transients  for

close-up  short  circuits,  and  also  achieve  dependable  faulted  line  selection.  By

using  only  partial  cross-polarization,  the  drawback  of  the  fully  cross-polarized

characteristics are avoided,  while  still  keeping  the  benefits.  Figure  14  presents  a

common characteristic that can be found using this method.

27

Distance Protection – E04-034

Shield-shaped characteristic
with 16% square-wave cross
polarization

X

Self-polarized
Mho circle

Fully cross
polarized Mho
circle

Zn

R

Extra resistive
coverage of shield

Conventional 16% partially
cross polarized Mho circle

X

0

1

6

1

2

60

 24

R

Figure 14. Partially cross-polarized characteristic with “shield” shape (a) comparison

of polarized characteristics made for S.I.R.= 6 (b) Resistive enlargement of shaped

partly cross-polarized Mho with increasing values of  S.I.R.

QUADRILATERAL CHARACTERISTIC

This  shape  of  a  polygonal  impedance  characteristic  is  presented  in  Figure  15.  The

characteristic  is  given  with  forward  reach  and  resistive  reach  settings  that  are

independently  changeable.  Hence,  it  gives  a  better  resistive  coverage  than  any  mho-

type  characteristic  for  short  transmission  lines.  This  is  particularly  correct  for  ground

fault  impedance  measurement,  where  the  arc  resistances and  short  circuit  resistance

to  ground  contribute  to  the  greatest  values  of  fault  resistance.  To  avert  significant

28

Distance Protection – E04-034

errors  in  the  protection  zone  reach  precision,  it  is  typical  to  enforce  a  maximum

resistive  reach  in  terms  of  the  protection  zone  impedance  reach.  Suggestions  about

this  can  be  typically  found  in  the  technical  protection  relay  brochures  and  manuals.

Quadrilateral  devices  with  plain  reactance  reach  lines  can bring  in  reach  error  issues

for  resistive  ground  short  circuits,  where  the  angle  of  total  short  circuit  current  differs

from the angle of the current sensed by the protection relay. This will be the situation

where  the  local  and  remote  source  voltage  vectors  are  phase  shifted  with  respect  to

each  other  due  to  pre-short  circuit  power  flow.  This  can  be  resolved  by  choosing  an

option  to  utilize  a  line  current  for  polarization  of  the  reactance  reach  line.  Polygonal

impedance  characteristics  are  greatly  flexible  in  terms  of  short  circuit  impedance

coverage  for  both  line  and  ground  short  circuits.  For  this  reason,  most  digital  and

numerical  protection  distance  relays  give  this  shape  of  characteristic.  An  additional

factor is that extra cost implications of enforcing this characteristic in utilizing discrete

electromechanical  components  or  early  static  protection  relay  technologies  do  not

apply.

X

C

Zone 3

Zone 2

B

Zone 1

Zones 1&2

A

Zone 3

R

RZ1

RZ2

RZ3

Figure 15. Quadrilateral characteristic

PROTECTION AGAINST POWER SWINGS: USE OF THE OHM CHARACTERISTIC

During serious power swing situations in which the power system is unlikely to retrieve,

stability  might  only  be  recovered  if  the  swinging  sources  are  separated.  When  such

situations are discovered, power swing, or out-of-step, tripping relay

29

Distance Protection – E04-034

protection  can  be  used  in  order  to  strategically  divide  a  power  system  at  a  selected

position. Ideally, the division should be made so that the plant capacity and  the loads

on either part of the split are matched.

Generally,  this  disruption  mode  cannot  be  precisely  described  by  typical  distance

protection. As previously noted, it is usually required to keep distance relay protection

schemes  from  tripping  during  stable  or  unstable  power  swings  to  avert  cascade

tripping.  To  start  system  divisions  for  a  prospective  unstable  power  swing,  an  out-of-

step tripping arrangements, using ohm impedance measuring devices, can be used.

Ohm  impedance  characteristics  are  used  along  the  forward  and  reverse  resistance

axes of the R/X graph, and their tripping limits are parallel to the protected transmission

line impedance vector, as presented in Figure 16.

Locus of
power
swing

X

Zone
C

Zone
B

H

Line

impedance

Zone
A

R

G

Out-of-step tripping relay

characteristic

Figure 16. Usage of out-of-step tripping protection relay characteristic

The ohm impedance devices split the R/X impedance graph into three zones; A, B and

C. As  the  impedance  changes  during  a  power  swing,  the  point  presenting  the

impedance shifts along the swing locus, placing the three zones in turn and making the

ohm  elements  to  trip  in  sequence.  When  the  impedance  gets  into  the  third  zone,  the

trip  sequence  is  finished  and  the  circuit  breaker’s  trip  coil  can  be  energized  at  a

favorable  angle  between  power  system  sources  for  arc  interruption  with  little  risk  of

restriking.

30

Distance Protection – E04-034

Only  an  unstable  power  swing  situation  can  make  the  impedance  vector  shift

through the three zones. Hence, other types of system disruptions, such as power

system short circuit conditions, will not end in a protection relay element trip.

OTHER CHARACTERISTICS

The performance time for the algorithm for a typical distance relay protection using

quadrilateral or similar characteristics may end in a long tripping time, perhaps up to

40  ms  in  some  protection  relay  arrangements.  To  get  over  this,  some  numerical

distance protection relays use extra algorithms that can be carried out significantly

quicker. These algorithms are typically based on sensing variations in current and

voltage that are surplus of what is anticipated.

This algorithm senses a short circuit by cross-comparing the measured quantities of

current  and  voltage  with  previously  sampled  quantities.  If  the  variation  between

these samples surpasses a predefined quantity, it is presumed  that a short circuit

is  present.  In  parallel,  the  distance  to  fault  location  is  also  calculated.  Given  the

calculated distance to fault lies within the protection Zone reach of the protection relay,

a trip command is issued. This algorithm can be carried out quicker than the typical

distance algorithm, ending in quicker overall functioning times. Faulted line selection

can  be  carried  out  by  cross-comparing  the  signs  of  the  variations  in  voltage  and

current.  Protection  relays  that  use  these  algorithms  typically  run  both  this  and

distance  protection  algorithms  in  parallel,  as  some  short  circuit  types  (e.g.  high-

resistance short circuits) may not fall within the short circuit detection criteria of the

algorithm.

DISTANCE PROTECTION RELAY USAGE

Discriminating protection zones can be accomplished using distance protection relays

given  that  fault  distance  is  a  simple  function  of  impedance.  While  this  is  true  for

transmission lines, the impedances sensed by a distance protection relay also depend

on the following points:

-

the magnitudes of current and voltage (the protection relay may not see all the

31

Distance Protection – E04-034

current that generates the short circuit voltage)

the fault impedance loop being sensed

the type of short circuit

the short circuit resistance

the symmetry of transmission line impedance

the circuit arrangement (single, double or multi-terminal transmission line)

-

-

-

-

-

It is feasible to eliminate all of the above points for all practical operating situations.

Nevertheless, significant success can be made with an adequate distance protection

relay. This may incorporate protection relay devices or algorithms for starting, distance

sensing and for scheme logic. Different distance protection relay formats exist and

they  depend  on  the  tripping  speed  and  cost  conditions  related  to  the  protection

relaying hardware, software or numerical protection relay processing capacity needed.

The most typical formats are:

-

-

a single sensing device for each line is given, covering all line short circuits

a  more  economical  scheme  is  for  ‘starter’  devices  to  check  the  lines  that

have experienced a short circuit. The starter devices switch a single sensing

device or algorithm to sense the most appropriate short circuit impedance loop.

This is typically referred to as a switched distance protection relay

-

a single set of impedance sensing devices for each impedance loop may have

their reach settings raised from one zone to another. The gain happens after

zone time delays are started by the functioning of  starter devices. This type

of  protection  relay  is  typically  referred  to  as  a  reach  stepped  distance

protection relay

-

each  protection  zone  may  be  given  with  independent  sets  of  impedance

sensing  devices for each  impedance  loop. This  is known  as  a full  distance

32

protection arrangement; capable of providing the greatest performance in terms

of speed and application flexibility

Distance Protection – E04-034

Moreover, relay protection against ground faults may need different characteristics

and/or  settings  than  those  needed  for  line  short  circuits,  resulting  in  additional

elements needed. A total of 18 impedance-sensing devices or algorithms would be

needed  in  a  complete  arrangement  distance  protection  relay  for  a  three  zone

protection  for  all  types  of  short  circuits.  With  electromechanical  or  static

arrangements, each of the sensing devices would have been a separate protection

relay placed in its own enclosing. This is to ensure that the distance protection relay

is comprised of a panel-mounted assembly of the needed protection relays with suited

inter-unit wiring.

Digital/numerical distance protection relays are likely to have all of the above functions

incorporated in software. Starter elements may not be needed. The complete distance

protection  relay  is  placed  in  a  single  enclosure,  making  great  savings  in  space,

wiring  and  dependability,  through  the  enhanced  availability  that  stems  from  the

provision of uninterrupted self-supervision.

STARTERS FOR SWITCHED DISTANCE RELAY PROTECTION

Electromechanical  and  static  distance  protection  relays  do  not  use  separate

impedance-sensing devices per phase. The cost and the final physical size make

this  arrangement

impractical,  except

for

the  most  comprehensive  EHV

transmission  usages.  To  be  more  economical,  only  one  sensing  device  is given,

together with ‘starter’ elements that detect the lines that are short circuited, and switch

the adequate signals to the single measuring function. A distance  protection relay

using  this  method  is  known  as  a  switched  distance  protection  relay.  A  number of

different  modes  of  starters  have  been  utilized,  the  most  typical  is  based  on  over-

current, under-voltage or under-impedance sensing.

Numerical distance protection relays allow direct sensing of the lines involved in a

short circuit. This is known as short circuit line selection, often abbreviated to line

selection.  Several  methods  are  available  for  short  circuit  line  selection,  which

allows the adequate distance-sensing zone to operate. Without line selection, the relay

protection risks having over or under-reach issues, or tripping three-line when single-

33

Distance Protection – E04-034

pole short circuit clearance is needed. Several modes are available for short circuit

phase selection, such as:

- Superimposed  current  comparisons,  cross-comparing  the  change  between

pre-short circuit load, and short circuit current. This allows very quick sensing

of the faulted lines, within several samples of the analogue current inputs

-

-

change in voltage magnitude

change in current magnitude

Numerical  line  selection  is  quicker  than  traditional  starter  methods  utilized  in

electromechanical  or  static  distance  protection  relays.  It  does  not  enforce  a  time

penalty since the line selection and sensing zone algorithms operate in parallel. It

is  feasible  to  make  a  full-arrangement  protection  relay  with  these  numerical

methods. The line selection algorithm gives short circuited line selection, together

with a segregated sensing algorithm for each line-earth and line-to-line short circuit

loop (AN, BN, CN, AB, BC, CA), thus assuring complete-scheme operation.

Nevertheless, there may be cases where a numerical protection relay that mimics

switched  distance  protection  methods  is  needed.  The  reasons  may  be  economic

(less  software  needed),  therefore  cheaper  than  protection  relays  that  contain

complete-arrangement  implementations),  and/or  technical.  Some  instances  may

require  the  numerical  protection  relay  characteristics  to  match  those  of  earlier

generations  established

in  a

transmission  network,

to  help  and  enhance

selectivity.  Such  protection  relays  can  be  used,  often  with  refinements  such  as

multi-sided  polygonal  impedance  characteristics  that  help  avoid  tripping  due  to

heavy load conditions. With electromechanical or static switched distance protection

relays,  a  selection  of  available  starters  is  usually  made.  The  selection  of  starters

depends on power system parameters such as maximum load transfers relative to the

maximum reach needed, and power system grounding schemes.

When  overcurrent  starters  are  utilized,  it  must  be  carefully  assured  that  with

minimum generating plant in operation, the setting of the overcurrent starters is

34

Distance Protection – E04-034

sufficiently  sensitive  to  short  circuits  beyond  the  third  zone.  Moreover,  these

starters  need  a  high  drop-off  to  pick-up  ratio.  This  is  to  assure  that  they  drop  off

under maximum load conditions after a second or third zone short circuit has been

cleared  by  the  first  zone  protection  relay.  Without  these  characteristics,  the

operation  may  end  for  subsequent  short  circuits  in  the  second  or  third  protection

zones.  For  an  acceptable  tripping  of  overcurrent  starters  in  a  switched  distance

protection scheme, the following conditions have to be met:

-

the current setting of the overcurrent starters must not be less than 1.2 times

the maximum full load current of the protected transmission line

-

the power system’s minimum short circuit current, at the Zone 3 reach of the

distance protection relay, must not be less than 1.5 times the setting  of  the

overcurrent starters

In multiple-grounded power systems where the neutrals of all the power transformers

are directly grounded, or in power systems where the short circuit current is less than

the full load current of the protected transmission line, the use overcurrent starters

is  not  feasible.  Under  these  conditions,  under-impedance  starters  are  commonly

used.  The  type  of  under-impedance  starters  used  depends  on  the  maximum

anticipated load current and the minimum load impedance relative to the protection

relay setting  needed to cover short circuits in  Zone  3. This is shown  in  Figure  11

where ZD1, ZD2, and ZD3 are the minimum load impedances allowed when lenticular,

offset mho, and impedance protection relays are utilized.

35

