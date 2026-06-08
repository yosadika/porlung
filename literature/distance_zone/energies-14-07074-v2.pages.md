# Page index: energies-14-07074-v2.pdf

Source PDF: energies-14-07074-v2.pdf

Search this file to find a topic, then open the source PDF at the indicated PDF page.

## PDF page 1

energies
Article
Dynamic Quadrilateral Characteristic-Based Distance Relays
for Transmission Lines Equipped with TCSC
Ghada M. Abo-Hamad 1 , Doaa Khalil Ibrahim 1 , Essam Aboul Zahab 1 and Ahmed F. Zobaa 2,*
1 Department of Electrical Power Engineering, Faculty of Engineering, Cairo University, Giza 12613, Egypt;
dody_benhamed@yahoo.com (G.M.A.-H.); doaakhalil73@eng.cu.edu.eg (D.K.I.);
zahab0@eng.cu.edu.eg (E.A.Z.)
2 College of Engineering, Design and Physical Sciences, Brunel University London, Uxbridge UB8 3PH, UK
* Correspondence: azobaa@ieee.org
Abstract: A two-fold adaptive dynamic quadrilateral relay is developed in this research for pro-
tecting Thyristor-Controlled Series Compensator (TCSC)-compensated transmission lines (TLs). By
investigating a new tilt angle and modifying the Takagi method to recognize the fault zone identifier,
the proposed relay adapts its reactive reach and resistive reach separately and independently. The
investigated tilt angle and identified fault zone use the TCSC reactance to compensate its effect
on the TL parameters and system homogeneity. Excessive tests are simulated by MATLAB on the
non-homogenous network, IEEE-9 bus system and further tests are carried out on IEEE-39 bus
system in order to generalize and validate the efficiency of the proposed approach. The designed
trip boundaries are able to detect wide range of resistive faults under all TCSC modes of operations.
The proposed approach is easy to implement as there no need for data synchronization or a high
(cid:1)(cid:2)(cid:3)(cid:1)(cid:4)(cid:5)(cid:6)(cid:7)(cid:8)(cid:1) level of computation and filtration. Moreover, the proposed adaptive dynamic relay can be applied
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:6)(cid:7)
for non-homogeneity systems and short as well as long TLs which are either TCSC-compensated or
-uncompensated TLs.
Citation: Abo-Hamad, G.M.;
Ibrahim, D.K.; Aboul Zahab, E.;
Zobaa, A.F. Dynamic Quadrilateral Keywords: distance relay; fault resistance; quadrilateral characteristic; resistance and reactance
Characteristic-Based Distance Relays elements; Thyristor Controlled Series Compensator (TCSC)
for Transmission Lines Equipped
with TCSC. Energies 2021, 14, 7074.
https://doi.org/10.3390/en14217074
1. Introduction
Academic Editor: Andrea Mariscotti
The value of fault resistance inserted by short circuits has a significant impact on the
performance of distance relaying devices protecting transmission lines (TLs). Therefore, it
Received: 29 September 2021
becomes a challenge to choose the appropriate characteristic to cover all protection require-
Accepted: 25 October 2021
ment issues. The reactance relays are not affected by the line resistance, but, unfortunately,
Published: 28 October 2021
the reactance relay is non-directional relay, and it is impossible to add a directional element
to it, as in such case the relay will operate under normal operating conditions if the system
Publisher’s Note: MDPI stays neutral
operates at or around a unity power factor. For this purpose, the reactance relay with
with regard to jurisdictional claims in
directional features is modified into the Mho or admittance characteristic [1]. Although the
published maps and institutional affil-
Mho relay is preferable in the protection of TLs, as it has inherently directional features,
iations.
its characteristics are still restricted under high fault resistance conditions. On the other
hand, the key advantages of the quadrilateral relay are the trip coverage area for grounded
resistive faults and the “reach” of the resistance and reactance elements which can be
independently controlled; however, it is affected by the system non-homogeneity [2].
Copyright: © 2021 by the authors.
FACTS (Flexible Alternating Current Transmission System) devices are one of the
Licensee MDPI, Basel, Switzerland.
magic solutions installed in the electrical grid to enhance controllability of the network.
This article is an open access article
FACTS controllers can be categorized into series-connected controllers, shunt-connected
distributed under the terms and
controllers, series–series connected controllers, and series–shunt connected controllers [3].
conditions of the Creative Commons
Series compensation (SC) is the most common technique used in TLs, as it not only im-
Attribution (CC BY) license (https://
proves system transient stability, controls voltage and power flow, but also increases power
creativecommons.org/licenses/by/
4.0/). transferring capacity, and decreases losses [4]. A Thyristor-Controlled Series Compensator
Energies 2021, 14, 7074. https://doi.org/10.3390/en14217074 https://www.mdpi.com/journal/energies

## PDF page 2

Energies 2021, 14, 7074 2 of 23
(TCSC) provides better control over fixed SC for a TL power flow. However, unfortunately
the integration of TCSC in TL affects its protection ability significantly due to the abrupt
line parameters changes. This will lead to defects in the apparent impedance measured by
the distance relays that cause overreaching/underreaching of the relays.
The research studies of [5,6] have considered the effect of FACTS as well as TCSC on
the quadrilateral relay. In [5], the impedance measured by the relay is evaluated considering
TCSC at the near end of the TL. Nonetheless, the homogeneity of the system, fault types,
fault location, and TCSC modelling are not considered in this evaluation. The impact of
series-distributed FACTS on the tilt angle setting of the quadrilateral characteristic and how
it may affect the coverage of fault resistance by overreaching/underreaching are discussed
in [5].
Other published efforts in [7–9] have presented the factors that should be considered in
designing the setting of the quadrilateral relay to eliminate the errors due to fault conditions.
In [7], the influence of the fault resistance and tilt angle on the quadrilateral characteristic
equations is presented. The considerations of the phase and ground elements for the
phase comparator quadrilateral relay are proposed in [8]. The influence of phase angle
errors on the polarizing signal of zone-1 quadrilateral distance elements is introduced
in [9]. The study demonstrated the reactive reach setting limit for a given maximum
expected polarization phase angle which, beyond the resistive reach, may lose security for
resistive faults.
In [10–12], the resistive reach is adapted based on the measured impedance by the
relay and circuit theory approach. By using the impedance measurements from two-line
ends, the fault resistance is calculated from a second order equation in [10]. The validation
results for this scheme are obtained for zone-1 only so, the results for back-up protection
zones and under communication failure are unclear. A standalone adaptive distance
protection is also proposed in [10], where the fault resistance is calculated by the slope
tracker method considering constant X/R ratio not only for the primary protected line
but also for the adjacent line, which may be an inappropriate method for interconnected
TLs. Furthermore, the results show the limitation of fault resistance coverage up to 50 Ω
in zone-1 and up to 20 Ω for back-up zones of protection. The four boundary lines of a
numerical quadrilateral characteristic are obtained in [12] by computer simulation under
different changes in system configuration. However, that study does not describe the
methodology followed to adapt the reaches of the characteristics; moreover, the simplicity
of the radial system used in the simulation may reduce the accuracy of results, especially
as the results are limited to the primary zone of protection. Despite of the simplicity of this
technique, the unfaithful model of the FACTS device or the approximate data infeed to
the relay, affected by the TL parameters, may introduce error into the apparent impedance
calculations.
The third zone setting of a quadrilateral relay is adapted in [13] by using the variation
mode decomposition approach to decompose the local end current signal into different
modes. The apparent impedance and energy index that are calculated from the signal
extracted from the third mode are used to detect the third zone’s symmetrical and asym-
metrical faults. Generally, the multi-filtering techniques are performed with high sampling
rates and the extra calculation burden on the relay is significant.
Furthermore, the construction of tripping boundaries of the adaptive quadrilateral
relay by the optimization technique is developed in [14–17]. By considering the probabilistic
behaviour of the random variables that affect the apparent impedance seen by the relays,
optimal settings of quadrilateral relay zones are developed in [14]. Unfortunately, this
approach will be affected by the selected weight used for the constraints that may increase
the reach of protection zones or loss of selectivity. Constructing the boundary of the first
distance protection zone for SC-TL with an optimization-based algorithm is introduced
in [15]. The reach of the protection zone can be maximized by solving a number of scaled
optimization problems in order to construct a tripping boundary. For that algorithm, the
selective weights of the fault resistance bounds are obtained from the historical data and the

## PDF page 3

Energies 2021, 14, 7074 3 of 23
reactance of SC is assumed to be available all time. Additionally, the scaled optimization
problems rely on some assumptions such as recognizing the grid parameters that affect
the algorithm robustness significantly. In [16], a multi-objective optimization problem,
solved by the sine–cosine algorithm to obtain the reach setting of the quadrilateral relay, is
proposed. The lack of the details used to set the parameters of the methodology according
to the application limits of distance protection relays to TLs is a key disadvantage of
this approach.
A genetic algorithm for determining the reach settings of the quadrilateral distance
protection element of mutually coupled TLs is also illustrated in [17]. The algorithm uses
different faulty system conditions affecting the measured impedance as the variable input.
However, there is no information about fault resistance estimation and the method is only
simulated for the primary protected zone. There is no doubt that the higher computational
times for the number of iterations and the accuracy of the results that rely on the data
required from the system make the choice of optimization techniques challenging.
Generally, the application of different nature-inspired metaheuristics is prevalent
in different design optimization missions. However, all of the optimization algorithms
are dependent on parameters that are significantly affected by the question of the best
values or settings and how to tune these parameters to achieve the best performance; in
particular, there is no unified mathematical definition of robustness. Moreover, the selection
of the appropriate nature-inspired metaheuristic and the benchmarking are also an open
challenging problem, due to the “no free lunch” theorem of mathematical optimization [18].
The communication-based scheme is another philosophy used in protective relaying
to meet the TLs’ requirements, as proposed in [19–21]. An adaptive relay setting algorithm
for a series-compensated line with a capacitor protected by Metal Oxide Varistors (MOV)
is proposed in [19]. It computes the seen impedance by considering the local and remote
end relays’ active power, voltage and current. The series compensation model and the
restriction of the fault resistance coverage area to only 10 Ω may weaken the scheme
performance. Another solution for setting the adaptive quadrilateral relay, protecting TL-
possessing series capacitor protected by MOV, is demonstrated in [20]. The seen impedance
is computed from the local information available at the relay. The unknown fault resistance
value can be compensated by using the superposition principle on the obtained active
power from both ends of TL at the fault instant. However, the study has approximated the
SC with the MOV model of linear impedance, which may affect the accuracy of the results.
A modified transfer trip scheme is developed in [21] to eliminate the overreach problem
facing the distance relay under SC without any guarantee of the scheme’s effectiveness
in the case of fault resistance and communication failure. There is no doubt that the cost,
speed and reliability of the communication systems are vital factors that must be considered
before implementing communication-based schemes. Moreover, synchronized data-based
schemes overburden the relays, and communication failure may lead to complete failure
of relays.
Another category of adaptive relays uses the concept of reducing the zone-1 setting
and delaying zone-2 as per the fault conditions [22–25]. Switching off zone-1 and increasing
the zone-2 time to alleviate SC effect of TLs is presented in [22]. An adaptive relay for
SC-TL is also suggested in [23], where the reach of an instantaneous zone-1 is reduced to
67% of TL length and another delayed zone-1 is reconstructed after two cycles from the
fault inception approach. For TCSC-compensated TL, the idea of reducing the zone-1 reach
setting and delaying zone-2, to improve the conventional relay, is introduced in [24,25].
The validation results in the last two schemes ignore the fault resistance effect. Above all,
the intrinsic demerits of this concept are the delayed fault clearance time, the high-speed
TL parameters’ estimation requirement, alongside the need for efficient modelling of the
compensated device.
Generally, the chronological trend of research studies obviously shows the increas-
ing concern of research for more and more improved protection schemes for TCSC-
compensated TLs. For this reason, in this paper, an adaptive dynamic quadrilateral relay

## PDF page 4

Energies 2021, 14, 7074 4 of 23
compatible with the compensated TCSC interconnected with TLs is proposed. The main
objective of this scheme is to adapt the reactive and resistive reach of the setting based
on the circuit theory and the impedance measured by the relay. The quadrilateral charac-
teristic dynamically moves upward/downward reliant on the TCSC mode of operation
and the tilt angle, moving the right side depending on the existence of fault resistance.
The proposed approach is extensively evaluated by using the Matlab simulator program
for TCSC-compensated interconnected TL systems under high fault resistance in both the
inductive and capacitive TCSC modes of operation. For the purpose of generalizing the
methodology, the tests are applied on non-homogeneous TL systems, which are long TLs of
the IEEE-9 bus system and repeated on short TLs of the IEEE-39 bus network. Additionally,
the results are compared with respect to the latest research studies.
Therefore, the contribution of this paper can be summarized as follows:
(cid:110) An adaptive dynamic quadrilateral distance relay is proposed to accurately detect the
high resistive faults under TCSC-compensated TLs.
(cid:110) A new tilt angle estimation is investigated which uses TCSC reactance to compensate
for the non-homogeneity effect due to the presence of TCSC in the faulted loop.
(cid:110) The proposed method applies the modified Takagi method to propose the fault zone
identified, which is used to adapt the resistive reach.
(cid:110) The adaptation of the relay setting reaches for TCSC-compensated TLs is based on the
local data estimated at the relay terminal and two values of RMS current and firing
angle transmitted from the TCSC substation, upon a fault-starting recognition signal
occurring.
(cid:110) Finally, the proposed approach is easily implemented as it can be applied by modify-
ing the conventional relay algorithm without any high level of filtrations or excessive
computational tools.
The remainder of the paper is arranged as follows: in Section 2, the TCSC effect on
the distance relay, and the practical modelling of its impedance are briefly presented. The
proposed methodology is fully described in Section 3. The scheme validation and achieved
results on both IEEE-tested systems are illustrated in detail in Section 4. The discussion of
the advantages of the proposed adaptive relay compared with other relays and conclusions
are summarized in Sections 5 and 6, respectively.
2. Thyristor-Controlled Series Compensator (TCSC)
As is known, TCSC provides better control over TL power flow than fixed SC, so the
paper will focus on identifying and mitigating the effect of TCSC on TL distance protection.
The TCSC characteristic and its operational mode are very well explained in [26,27].
For faulty conditions, TCSC controller system reacts rapidly to take preventive measures
and TCSC operates under different modes depending on the fault type. For different fault
scenarios, Table 1 summarizes the protection performance under different TCSC operation
modes [28].
Table 1. Distance relays performance for TCSC-compensated TLs under faulty conditions.
TCSC Mode Fault Conditions Distance Relay Behaviour
Bypass mode Excessive high fault current Underreach
Circuit breaker bypass The fault is not cleared in the instantaneous tripping zone Slight underreach in some cases
Capacitive mode without MOV High impedance fault Overreach
Capacitive mode with MOV High fault current Slight overreach
Blocking mode Transient fault Overreach
When a fault occurs close to TCSC, the high fault current is enough to conduct the
MOV. Therefore, the equivalent capacitive reactance of TCSC decreases due to MOV. As a
result, the possibility of experiencing voltage and current inversion is quite low during the
fault. In addition, TCSC could be changed from the capacitive mode into the bypass mode

## PDF page 5

Energies 2021, 14, x FOR PEER REVIEW 5 of 23
Table 1. Distance relays performance for TCSC-compensated TLs under faulty conditions.
TCSC Mode Fault Conditions Distance Relay Behaviour
Bypass mode Excessive high fault current Underreach
The fault is not cleared in the instantaneous
Circuit breaker bypass Slight underreach in some cases
tripping zone
Capacitive mode without MOV High impedance fault Overreach
Capacitive mode with MOV High fault current Slight overreach
Blocking mode Transient fault Overreach
Figure 1 introduces the errors due to presence of TCSC in the fault loop for different
modes of operations by simulating an L-G fault at the 2 s timepoint and changing the
Energies 2021, 14, 7074 5 of 23
firing angle (𝛼) in order to apply different TCSC operating modes.
- For a simulated fault in zone-2 (at 85% of the protected line) and due to the TCSC
impedance, thifet hreelvaeyry ohvigehrfraeualtchcuersr eantnfldo wdsetthercotusg thhTeC SfaCutlot pirnev zenotndea-m1 aigne obfoththe MbOloVckanindgse ries
mode (α = 90°)c aapnadcit coar.pInacthitisivmeo mdeo, tdhee T(αC S=C 7i5m°p)e. dance is a pure inductance. Therefore, the inversion
- On the other h
p
a
h
n
en
d
o
,
m
fo
en
r
o
a
n
s
n
i
e
m
ve
u
r
l
o
a
c
t
c
e
u
d
r s
f
,
a
a
u
n
l
d
t
t
i
h
n
e
z
d
o
is
n
ta
e
n
-
c
1
e
(
r
a
el
t
a
7
y
5
e
%
xp e
o
r
f
i e
t
n
h
c
e
es
p
s
r
li
o
g
t
h
e
t
c
u
t
n
e
d
d
e r
l
-
i
r
n
e
e
a
)
c h
a
i
n
ng
d
[ 25].
Figure 1 introduces the errors due to presence of TCSC in the fault loop for different
due to the TCSC impedance, the relay underreaches and detects the fault in zone-2
modes of operations by simulating an L-G fault at the 2 s timepoint and changing the firing
in both induct
a
iv
ng
e
l e
m(o α)d
i
e
n
(
o
α
rd
=
e r
2
t
5
o
°
a
)
p
a
p
n
ly
d
d
b
if
y
fe
p
re
a
n
s
t
s
T
m
CS
o
C
d
o
e
p
(
e
α
ra
=
ti n
0
g
°)
m
.
odes.
Figure 1. FTighuer ea1p.pTahreeanptp iamrepnteidmapnecdea nucneduenrd eLr-LG-G fafauullttss aatt 22 ssf ofor rd idffiefrfeenrteTnCt STCCoSpCer aotpioenrmatoidoens .modes.
In this study, -TCSFCo rima spimedualantecde fa(u𝑋lt in z)o nme-o2d(aetll8i5n%g oisf tahpe pplrioetdec theedrlein ae)ccaonrdddiunegt otot htehTe CSC
𝑇𝐶𝑆𝐶
impedance, the relay overreaches and detects the fault in zone-1 in both blocking
practical design values, and the equivalent impedance will be the function of line imped-
mode (α = 90◦) and capacitive mode (α = 75◦).
ance (𝑍 ) and the compensation factor (𝜓), as described in [28]:
𝐿 - On the other hand, for a simulated fault in zone-1 (at 75% of the protected line) and
due to the TC𝑋SC imped=an𝜓c.e𝑍, th e relay underreaches and detects the fault in(1z)o ne-2 in
𝑇𝐶𝑆𝐶(𝛼) 𝐿
both inductive mode (α = 25◦) and bypass mode (α = 0◦).
3. Proposed Dynamic QInutahdisrsiltuadteyr, aTlC DSCistimanpceed aRnecela(yX TCSC ) modelling is applied here according to
the practical design values, and the equivalent impedance will be the function of line
The main purpose of this article is to apply an accurate and simple solution for the
impedance (Z ) and the compensation factor (ψ), as described in [28]:
L
problems facing distance quadrilateral relays for TCSC-compensated TLs under high re-
X = ψ.Z (1)
sistance faults. This target can be achieved by introdTCuScCi(nα)g a newL setting approach for both
resistive and reactive reaches of quadrilateral distance relays independently. The dynamic
3. Proposed Dynamic Quadrilateral Distance Relay
updating of both settings will be separately controlled based on the fault resistance occur-
The main purpose of this article is to apply an accurate and simple solution for the
rence and including TCSC impedance in the faulted path. The proposed dynamic quadri-
problems facing distance quadrilateral relays for TCSC-compensated TLs under high
lateral trip boundarreys iwstailnlc beefa dueltssc. rTihbiesdta irnge tthcea nfobleloacwhiienvge dsubbysienctrtoioduncsi.n g a new setting approach for
both resistive and reactive reaches of quadrilateral distance relays independently. The
dynamic updating of both settings will be separately controlled based on the fault resistance
3.1. Preliminary Basic Considerations
occurrence and including TCSC impedance in the faulted path. The proposed dynamic
The quadrilateqruaald driliasttearnalcter ipchbaoruancdtaerryiswtiicll bise ndeostc raib setdrainigthhetffoolrlwowairndg scuhbasreactcitoenrsi.stic such
as the Mho distance elements, as the combination of distance elements can create different
3.1. Preliminary Basic Considerations
The quadrilateral distance characteristic is not a straightforward characteristic such as
the Mho distance elements, as the combination of distance elements can create different
shapes and polygonal characteristics. The quadrilateral characteristic is constructed, as
shown in Figure 2, from the following elements [8]:
• A directional element;

## PDF page 6

Energies 2021, 14, x FOR PEER REVIEW 6 of 23
shapes and polygonal characteristics. The quadrilateral characteristic is constructed, as
shown in Figure 2, from the following elements [8]:
•
A directional element;
•
A reactance element;
•
A right blinder resistance element;
Energies 2021, 14, x FOR PEER REVIE
•
W A left blinder resistance element. 6 of 23
Energies 2021, 14, 7074 6 of 23
The impedance reach of the protected line (𝑍 ) is determined by the reactance el-
(cid:3019)(cid:3046)(cid:3032)(cid:3047)
ement with the tilt angle (𝛤) declining to consider the power flow conditions during re-
shapes and polygonal characteristics. The quadrilateral characteristic is constructed, as
sistive faults. Moreover, the resistive fault coverage is designed by the right resistance
• e sh le o m wAe n nr iet na. cF Ttiah gne uc ree e le e 2lm ,e mfr e oen mnt t w;th h e i f c o h l l l o i w m i i n t g s t e h le e m r e e n v t e s r [ s 8 e ] : f lowing load coverage is the left resistance
• e • lem AAen r di t gi rh aen tcb dtil oi a nn d daeli r reelrec emt s i i o set nnata n; l c e el e e l m em e e n n t t k ; eeps the faults detected in the forward direction only.
•• AAl ereftacbtlainndcee rerleemsisetnatn; ce element.
• A right blinder resistance element;
• A left blinder resistance element.
jX
The impedance reach of the protected line (𝑍 ) is determined by the reactance el-
(cid:3019)(cid:3046)(cid:3032)(cid:3047)
ement with the tilt angle (𝛤) declining to consider the power flow conditions during re-
𝜞
sistive faults. Moreover, the resistive fault coverage is designed by the right resistance
element. The elemOepnetra wtehich limits the reverse flowing load coverage is the left resistance
element and a directional element keeps the faults detected in the forward direction only.
Xset
Restrain
jX
𝜞
Rset
Operate
R
Xset
Restrain
FFiigguurere2 .2Q. Quaudardilraitleartaelrcahl acrhaactrearcistteircitsrtiipc btroiupn bdoaurinesd.aries.
The impedance reach of the protected line (Z ) is determined by the reactance
3.2. Adaptive Reactive Reach Rset
element with the tilt angl
R
e
se
(
tΓ)
declining to consider the power flow conditions during
Prevalent reactive setting design is achieved by considering the appropriate setting
resistive faults. Moreover, the resistive fault coverage is designed by the right resistance
R
eolef mliennet . rTehaectealenmcee nrtewlehviacnhtl itmoi ttshteh eprreovteercsteefldo zwoinnge.l oTaod ocobvteariang ethise tdheesleirfet dre sriestaacnticvee setting
e(l𝑋eme)n tfaonrd raeadcitraecntcioen ealleemleemnetnst, ktheeep rsetahcetfaanucltes ldinetee csteedttiinngth reefaocrhw a(𝑋rd dir)e cstihoanllo nbley .compen-
(cid:3020)(cid:3032)(cid:3047) (cid:3019)(cid:3046)(cid:3032)(cid:3047)
Figure 2. Quadrilateral characteristic trip boundaries.
sated for by TCSC impedance (𝑋 ) as follows:
(cid:3021)(cid:3004)(cid:3020)(cid:3004)((cid:3080))
3.2. Adaptive Reactive Reach
𝑋 = 𝑋 ± 𝑋 (2)
3.2. Adaptive Reactive Reach (cid:3020)(cid:3032)(cid:3047) (cid:3019)(cid:3046)(cid:3032)(cid:3047) (cid:3021)(cid:3004)(cid:3020)(cid:3004)((cid:3080))
Prevalent reactive setting design is achieved by considering the appropriate setting of
line reP N arce o tva n an - l h ceen o tr m erl o eea g vc e atn n ivt e et i o t s y et th s tei y n s pg t r e od m tees s ci tg a en f d f i e zs c oa t n c t eh h .i e eT vo s e e od n b s bt i ay t i i n v co i t t hn y es i o dd f ee t rs h iinr e eg d r t e hr a ee c a t ac a tpi n vp c er e os p e ert l ti e ai m nteg e s( n eX t t , t i w n)g h ich will
Set
fmoofr orlvienaeec dtraoenawccetnaewnlecamer edrnestl eso,vrta hunept rwteoaa ctrthadens c pberaloistneeecdts eeodtnt i zntohgnere ep.a Tochwo (eoXrb tfaloin)w sth hcaeol lndbdeesiticriooemdn spr eednaucsatriitvneedg sftoehtrteib naygs ymmet-
Rset
Tr(C𝑋icSaCl) pi mfhopar esrdee aaoncrtc aegn(rcXoeu enledmeden) rtesa,ss itsfhoteilvl oreew afsca:tualntcse. Tlion ee nsehttainngce r ethaceh r (e𝑋actan) cseh aplel rbfeo rcmomanpceen -for such
(cid:3020)(cid:3032)(cid:3047) TCSC(α) (cid:3019)(cid:3046)(cid:3032)(cid:3047)
csaotnedd iftoior nbsy, TthCeS Cre iamcptaendcaen ceel e(𝑋ment h)a as st ofo lbloew pso: larized by the fault current (𝐼 ). However,
(cid:3021)(cid:3004)(cid:3020)(cid:3004)((cid:3080)) (cid:3033)
X = X ± X (2)
because the fault loop curren𝑋t(cid:3020) (cid:3032)iSs(cid:3047) e t=no𝑋t(cid:3019) m(cid:3046) R (cid:3032)(cid:3047) see±at s𝑋u(cid:3021)r(cid:3004)aT (cid:3020)b(cid:3004) C (lS (cid:3080)eC ), ( tαh) e current at the relay (𝐼 (cid:3014) ) c(2a)n be used
insteNado no-hf o𝐼m. oAgesn tehitey zseyrsote mans da fnfeecgt athtiev see nsseiqtiuveitnyc oefs t hoec cruearc dtaunec et oel efmauelntts,, wsoh icthh ewyi lal re good
Non-hom(cid:3033)ogeneity systems affect the sensitivity of the reactance element, which will
mpm ooo vlvae erd idzo oiwnwgn n wcwha aor r didcs se oso r.r u Tu php wew ana r red dgs sa b btaiavs s eee d ds oeo nqnu t t heh enec p peo o wrweele rary fl f l oco wuwrc rc oeo nnn dtd i(i t t𝐼 i i o(cid:3014) o n(cid:2870) n s )s d diusu rur i i nsn gegd t t h hhe ee a arses y y tm mom mpeoe t tl- -arize the
rrr i iec c aaa lcl ptpah hna acs see e e o olrer g mg r r oeo unu ntn dad efetd derr r e ae sds is ijs tut iv isv eteinf f aga u u tlt lht s se. . TmT o oee ae nsn huh ara nen cdc e e at h tnh egelr ee re aoa cfc t a ttahn n cec e feap pue e rlr fto fco rur m mraraen nnc c ete, f wo fo rhr s is ucuhc c h his known
ca
c
o
o
sn
n
td
d
ili
i
tt
t
i
i
oa
o
nn
n
sg
s
,
,
l te
t
h
h
e(
e
𝛤 r
r
e)
e
a
a
c[
c
t8
t
a
a
]n.
n
c
c
e
e
e
e
l
l
e
e
m
m
e
e
n
n
t
t
h
h
a
a
s
s
t
t
o
o
b
b
e
e
p
p
o
o
la
la
r
r
iz
iz
e
e
d
d
b
b
y
y
t h
th
e
e
f a
fa
u
u
lt
lt
c
c
u
u
r
r
r
r
e
e
n
n
t
t
(
(I 𝐼
f
(cid:3033)))
.
.
H
H
o
o
w
w
e
e
v
v
e
e
r
r
,
,
bbeeccaauu Fsseo et r th h Tee Cf faa Suu Clltt -l c loo ooo mpp pc cue urn rrr see ann tte ti dsis n n Too Lttms m , et eah ase suu rp raa obbllel a e,r ,ti ht z hee e dc cu u nrrre reg enn att ta i a vttte ht hes e er q reeluala eyy n( c (I𝐼 Me(cid:3014) )) c cu car anr n eb n bee tu u iss se eda d l tered to
i
i
in
n
nss
c
tte
l
e
u
aad
d
d
e
oo f
t
f
h
I
e
𝐼 f(cid:3033). .
𝑋
AAss tthhe e
v
zz
a
ee
l
rr
u
oo
e
a
.
a n
T
ndd
h
n
e
n
r
ee
e
gg
f
a
o
atti
r
iv
e
ve
,
e
t
s
h
see
e
qq u
n
ue
e
en
g
ncc
a
ee
t
ss
iv
oo
e
cc c
s
cuu
e
r
q
r d
u
du
e
ue
n
e
c
tto
e
o f
n
faa
e
uu
t
l
w
tltss
o
,, s
r
so
k
o t
o
ht
f
he
t
ey
h
y
e
a ar
T
ree
C
g go
S
oo
C
od
-
d
c ompen-
p
s
po
a
ol
t
al
e
ar
d
rizi z
T
inin
L
gg
a
c ch
t
h o
t
o
h
ici (cid:3021)
e
ce (cid:3004) e s
m
(cid:3020) s. (cid:3004) . T
i
T
d
hh
-
ee
p
n
o
ne
i
eg
n
ga
t
at t
i
ii
s
vv e
i
e
l
s
l
s
u
eeq
s
qu
t
u
r
e
a
enn
t
c
e
ce
d
er re
i
e
n
lla a
F
yy
i
c
g
cu
u
urr
r
rr
e
een n
3
t
.
t ( (I 𝐼 M(cid:3014)2(cid:2870) )) isisu usseeddh heerreet otop poolalarrizizeet hthee
rreeaaccttaanncceee elelemmeenntta afftteerra addjujusstitninggt thheem meeaassuurreedda annggleleo offt htheef faauultltc cuurrrreennt,t,w whhicichhi sisk knnoowwnn
aasst tiilltta annggllee( Γ(𝛤) )[ 8[]8. ].
Bus M Bus N
FFoorrT TCCSSCC-c-coommppeennsasateteddT TLLs,st, htehep oploarlaizreizdedn engeagtiavteivsee qsueqenuceencceu rcruernrteinsta ilste areltderteodi nto-
cilnucdlue dthe e Z t M hX 1 e
T C
𝑋
S(cid:3021)C(cid:3004)
v
(cid:3020)
R
(cid:3004)
a luvae (0 .lu . T 5 e ) h. Z eTr L h 1 e feorXree
T
f
C
,o
S
t
C
rh
1
e
(
e
α
,
)
tnh ( e r e - g 0 an .5 tei ) vg Z ea L t 1 si V evq fe2u se ( e 1 nq - c r u ) e e n Z ne L c 1 te w noertkwo o Z fr N tk 1 h eofT tChSeC T-CcoSmCp-ceonmsapteedn-
TsLataetdt hTeL mati dth-pe ominidt -ispoililnuts tirsa itleludsitnraFteigdu irne F3i.gure 3.
IM 2 If2 F IN 2
Bus M Bus N
Z M1 R (0.5) Z L1 (r-0.5) Z L1 Vf2 (1-r) Z L1 Z N1
Figure 3. Two-source negat X ivTCeSC 1s(αe) quence network.
IM2
If2 F
IN2
FFiigguurree3 3..T Twwoo-s-soouurrcceen neeggaatitvivees seeqquueenncceen neetwtwoorkrk. .

## PDF page 7

Energies 2021, 14, 7074 7 of 23
Considering a line-to-ground (L-G) bolted fault at the reach of zone-1 (r) of a TL with
Z positive sequence line impedance, and where Z and Z are the positive sequence
L1 M1 N1
source impedances at both TL terminals (M and N), the negative sequence of the fault
voltage is thus described as follows:
V = I (Z + (1 − r)Z ) (3)
f 2 N2 N1 L1
(cid:16) (cid:17)
V = I Z + r × Z ± X (4)
f 2 M2 M1 L1 TCSC1(α)
where “1” denotes a positive sequence while “2” denotes a negative sequence.
Knowing that I = I + I and according to Equations (3) and (4), the tilt angle
f 2 M2 N2
(Γ) can be expressed by:
(cid:18) I (cid:19) Z + Z ± X + Z
Γ = arg f 2 = arg( M1 L1 TCSC1(α) N1 ) (5)
I Z + (1 − r)Z
M2 N1 L1
Note that the negative sequence impedance of the source, line and TCSC are similar
to the corresponding positive sequence impedance values.
3.3. Adaptive Resistive Reach
The responsibility of the right resistance element in a quadrilateral distance relay is
the fault resistance coverage. This component of the quadrilateral distance relay will be
dynamically accommodated in the proposed scheme to detect fault resistance as much as
possible, on the condition that:
(cid:110) It is inherently immune in terms of selectivity, in order to operate for faults in an
appropriate desirable zone;
(cid:110) It is inherently immune in terms of security, in order to avoid mal-operation for
external faults or load encroachment scenarios.
To perform adaptively resistive reach setting for each selective protected zone for TLs
possessing TCSC compensation, a set of equations is applied based on apparent impedance
calculated by the relay and circuit theory approach. An adaptive resistive blinder for
ground elements is obtained by defining the fault resistance border (R ) and the shifting
f set
resistive line setting reach (R ) with an R value set by the positive sequence line
Rset f set
impedance angle (θ ).
L
To perform the fault zone identifier subroutine, the modified Takagi principle will ac-
commodate for TCSC-compensated TLs. The modified method that uses the zero-sequence
relay current (I ), instead of the superposition current used in the Takagi method to
M0
discriminate between ground and phase faults and to consider system loading during
grounded faults [29], is developed to include the TCSC impedance effect. In addition, for
non-homogeneous system correction, the investigated tilt angle will be considered for fault
zone identifier (a ), where V is the voltage at terminal M that is equivalent to the relay
Z M
voltage as:
Imag (cid:0) V × (3 I )∗ × e−jΓ(cid:1)
a Z = (cid:16) M (cid:17) M0 (6)
Imag (Z ± X × I × (3 I )∗ × e−jΓ)
L1 TCSC1(α) M M0
where a ≤ 0.8 for faults in zone-1, a ≤ 1.2 for faults in zone-2, and finally a ≤ 2.0 for
Z Z Z
faults in zone-3.
The adaptive ground element reach setting (R ) can be designated by the following
Set
equation, and is based on R that is calculated after the faulted zone is identified, where
f set
Z is the impedance seen by the distance relay,
app
R = R + R (7)
Set Rset f set
(cid:0) (cid:1)
R = Real Z − R (8)
f set app Rset

## PDF page 8

Energies 2021, 14, 7074 8 of 23
It is important to notice that the adaptive setting reach for phase elements can be
Energies 2021, 14, x FOR PEER REVIEaWc hieved by shifting the resistive line reach setting (R Rset ) from zero to the θ L angle (po8s iotfi v2e3
sequence line impedance angle), as the three phase elements are not accountable for any
fault resistance coverage.
The flowchart, displayed in Figure 4, shows the equation flow of the resistive reach
The flowchart, displayed in Figure 4, shows the equation flow of the resistive reach
setting adaptation for the ground distance elements.
setting adaptation for the ground distance elements.
Start
Fault Starting Recognition
Using Zone-4
Fault Zone Identification (aZ)
Using Equation (6)
No
If (aZ) > Threshold
Yes
Faults in Zone-3 Faults in Zone-2 Faults in Zone-1
No
If (aZ) ≤ 2.0
No
If (aZ) ≤ 1.2
No
If (aZ) ≤ 0.8
Yes Yes Yes
If Real (Zapp) ≤ Real Yes If Real (Zapp) Yes If Real (Zapp) Yes
(Zset_3) ≤ Real (Zset_2) ≤ Real (Zset_1)
No No No
Rfset_3 = R (Z e s a e l t ( _ Z 3 a ) pp) – Real K R e e T e s r p i i s p C ti B v o e n o v R u e n e n a d t c a io h r n y o a f l Rfset_2 = R (Z e s a e l t ( _ Z 2 a ) pp) – Real K R e e T e s r p i i s p C ti B v o e n o v R u e n e n a d t c a io h r n y o a f l Rfset_1 = R (Z e s a e l t ( _ Z 1 a ) pp) – Real K R e e T e s r p i i s p C ti B v o e n o v R u e n e n a d t c a io h r n y o a f l
Updating Resistive Reach of Trip Updating Resistive Reach of Trip Updating Resistive Reach of Trip
Boundary for Last Zone of Protection to Boundary for Following Zones of Boundary for ALL Zones of Protection to
Fault Resistance Limit Protection to Fault Resistance Limit Fault Resistance Limit
Rset_1 = 0 Rset_1 = 0 Rset_1 = Real (Zset_1) + Rfset_1
Rset_2 = 0 Rset_2 = Real (Zset_2) + Rfset_2 Rset_2 = Real (Zset_2) + Rfset_2
Rset_3 = Real (Zset_3) + Rfset_3 Rset_3 = Real (Zset_3) + Rfset_3 Rset_3 = Real (Zset_3) + Rfset_3
Figure 4. Proposed approach for adaptive resistive reaches for ground elements, Numbers 1, 2, or 3 denote zones-1,-2, or
Figure 4. Proposed approach for adaptive resistive reaches for ground elements, Numbers 1, 2, or 3 denote zones-1,-2, or -3,
-3, respectively.
respectively.
3.4. General Procedures of the Proposed Scheme
3.4. General Procedures of the Proposed Scheme
To reduce the burden issues on the distance relay, the proposed dynamic quadrilat-
To reduce the burden issues on the distance relay, the proposed dynamic quadrilateral
eral relay adapts its reactive and resistive reaches upon receiving a signal from the fault
relay adapts its reactive and resistive reaches upon receiving a signal from the fault starting
starting recognition subroutine.
recognition subroutine.
The fault starting recognition can be identified by developing zone-4, which has large
The fault starting recognition can be identified by developing zone-4, which has
quadrilateral boundaries. Its resistive reach relies on the minimum load resistance equiv-
large quadrilateral boundaries. Its resistive reach relies on the minimum load resistance
aelqeunitv taol etnhtet omtahxeimmuamxi mpuowmepr otwraenrsfterar ncsafperabcialpitayb tirliatnystmrainttsemd ivttiead thveia pthroetepcrtoetde,c tceodm, cpoemn--
spaetnedsa tTedL T ( L 𝑃 (cid:3040)((cid:3028)P(cid:3051)m )
a x
u)nudnedr emr maxaimximumu mcocmompepnesnastaiotino ndduurirnign gththee TTCCSSCC ccaappaacciittiivvee mmooddee
((𝑋X(cid:3021)T(cid:3004)C(cid:3020)S(cid:3004)C(cid:3040)m(cid:3028)(cid:3051)ax_(cid:3030)_(cid:3028)c(cid:3043)ap ).) .
𝑃 (cid:3040)P(cid:3028)m(cid:3051) a = x = 𝑍 (cid:3013)Z− L 𝑉 𝑋− (cid:3014) (cid:3021) V (cid:3004)X × M (cid:3020)T(cid:3004) (cid:3040) 𝑉 C ×(cid:3015) S(cid:3028)C V (cid:3051)_m N (cid:3030)(cid:3028)ax(cid:3043)_ s ca in p (s𝛿in−(cid:0) δ𝛼−(cid:2923)(cid:2911)α(cid:2934) m_(cid:3030)a(cid:3028)x(cid:3043)_ ) c ap (cid:1) ((99))
wwhheerree 𝑉V(cid:3015)N aanndd 𝛿δ aarree tthhee rreecceeiivviinngg eenndd vvoollttaaggee ssoouurrccee aanndd llooaadd aannggllee,, rreessppeeccttiivveellyy,, aanndd
𝛼α(cid:2923)m(cid:2911)a(cid:2934)x
__(cid:3030)c(cid:3028)a(cid:3043)p
iiss tthhee fifirriinngg aannggllee uunnddeerr mmaaxxiimmuumm ccoommppeennssaattiioonn ffoorr tthhee ccaappaacciittiivvee mmooddee..
TThhuuss,, tthhee rreeaaccttiivvee rreeaacchh ooff zzoonnee--44 ((X𝑋 4(cid:2872)))c caannb beed deeteterrmminineeddf rforommt htheem maxaixmimuumme xepxepcetca--
ttaiotinonof otfh tehree arecaticvteivree arcehacthh atht acat ncaonc coucrcudru driunrginthge thTeC TSCCSinCd iuncdtiuvcetimveo dmeo(dXe
T
(
C
𝑋 S(cid:3021)C(cid:3004)m(cid:3020)(cid:3004)ax(cid:3040)_(cid:3028)in(cid:3051)d_(cid:3036))(cid:3041),(cid:3031)a)s,
as
𝑋
(cid:2872)
X=
4
=𝐼𝑚I𝑎m𝑔a(g 𝑍(
(cid:3013)
Z)
L
+) +𝑋
(cid:3021)
X
(cid:3004)(cid:3020)T(cid:3004)C(cid:3040)S(cid:3028)C(cid:3051)m_(cid:3036)(cid:3041)ax(cid:3031)_ ind (
(
1
1
0
0
)
)
The general procedures of the proposed scheme are briefly summarized in Figure 5,
where:
 Two separate subroutines (based on Sections 3.2 and 3.3) will be in progress to set
both the reactive and resistive reaches of the quadrilateral distance relay

## PDF page 9

Energies 2021, 14, 7074 9 of 23
Energies 2021, 14, x FOR PEER REVIEW The general procedures of the proposed scheme are briefly summarized in Figu9 roef 52,3
where:
(cid:110) Two separate subroutines (based on Sections 3.2 and 3.3) will be in progress to set both
tihnedreepaecntidveenatnlyd arse ssoisotinv easr eaa lcahuenscohfinthge sqigunaadlr iisla itneirtaial tdeids tfarnocme rtehlea yfaiunldt esptaerntidnegn rtleycoags-
snoiotinona sstaalgaeu. nching signal is initiated from the fault starting recognition stage.
(cid:110) TTCCSSCC zzoonnee iiddeennttiifificcaattiioonn ssttaaggee iiss ssiimmppllyy aacchhiieevveedd aass aapppplliieedd iinn [[3300]],, bbaasseedd oonn ssuubb--
ttrraaccttiinngg tthhee TTCCSSCC tteerrmmiinnaall RRMMSSc cuurrrreenntta attt thheet tiimmeeo offf faauulltts sttaarrttininggr reeccooggnnitiitoionnf rforomm
tthhee ccoorrrreessppoonnddiinngg RRMMSS lliinnee ccuurrrreenntt mmeeaassuurreedda attt thheer reelalayyt teerrmmininaal.l.
Fault Starting Recognition jX
using Zone-4
Zone-4
Zone-3
Zone-2
Zone-1
R
TCSC Zone
Identification
Apparent
Impedance
Updating
analysis
Tilt angle( 𝜞)
by Equation (5)
Updating Resistive Reach Updating Reactive Reach
by Equation (7) by Equation (2)
jX jX
XTCSC_Inductive
XTCSC_Capacitive
RRset Rfset XRset
R
R
Protection Setting For Each Analyzed Zone
Zone-1 jX
Zone-2
XTCSC_Inductive
Zone-3
XTCSC_Capacitive
Rfset
R
Figure 5. General procedures of the proposed scheme.
Figure 5. General procedures of the proposed scheme.
TThhisis pprrooppoosseedd qquuaaddrriillaatteerraall cchhaarraaccteterirsitsitci crerlealya yapapprporaocahc chanca bne bapepalpiepdl ifeodr afnory nanoyn-
nhoonm-hoogmenoegoeunse osyusstseyms t(eams w(aisll wbeil lshboewshno lwatnerl ainte trhien ttehsetetde sstyesdtesmysst)e,m ass )w, aesll wase lTlCasSCT-CcSoCm--
cpoemnpsaetnesda tTeLdsT uLnsduenr dheigrhh ifgahulfta ruelstisrteasnisctea.n Tche.e Tschheesmche eims seeiqsuseenqtuiaeln; ttihaul;st, hauftse,ra tfhteer ftahuelt
fastualrttsintagr triencgorgenciotigonni tiiso nacihsiaecvheide,v tewd,ot sweopasreaptaer sautebsruoubrtionuetsin wesilwl pilrlopcreoecde etod utopduaptdea bteotbho tthhe
trheearcetiavcet iavneda nredsirsetsiivset isveettsientgtisn fgosr feoarceha zchonzeo. nTeh. uTsh, uths,et sheettsientgtisn ogfs zoofnzeo-n1 eo-f1 tohfet hreelareyl aayre
computed first, followed by the settings of zone-2, and then the settings of zone-3 are de-
termined.

## PDF page 10

Energies 2021, 14, x FOR PEER REVIEW 10 of 23
Energies 2021, 14, 7074 This approach will be applied independently for both Ground and P10haofs2e3 distance re-
lay elements; the only difference between them is that the adaptation of the resistive reach
in the phase element can be achieved by shifting the resistive line reach setting (𝑅 ) by
(cid:3019)(cid:3046)(cid:3032)(cid:3047)
cahreacnogminpgu ttehdefi r sbt,yf othlloew veadlubey othfe psoesttiitnivgse osfezqouneen-2c,ea nlidneth iemn ptheedsaenttcineg asnogf lzeo n(𝜃e-3).a re
(cid:3013)
determined.
This approach will be applied independently for both Ground and Phase distance relay
4. Proposed Scheme Validation
elements; the only difference between them is that the adaptation of the resistive reach
4in.1t.h Te epshteadse Seylesmtemenst can be achieved by shifting the resistive line reach setting (R ) by
Rset
changing the by the value of positive sequence line impedance angle (θ ).
The investigated methodology is tested on several faultyL cases generated on TCSC-
c4o. PmroppeonsseadteSdch TeLmse tVharloiduagtiho nthe Matlab simulation program by varying the fault locations,
T4.C1.STCes tmedoSdyest, eamnsd fault resistance value on an IEEE-9 bus small power system network that
has lTohnegi nTvLesst.i gFauterdthmeremthoodreo,l otghye istetsetsste adroen rseepveearatel dfa uolnty acnas eIsEgEeEn e3r9a-tebduso nsyTsCtSeCm-, as a large
ncoemtwpoenrska tseydstTeLms twhriotuhg shhtohretM TaLtsla, bins iomrudlearti oton vpraolgidraamte baynvda rgyeinngertahleizfaeu tlht elo pcartoiopnoss, ed scheme.
TCSCImt modues, ta nbde fpaoulitnrteesdis toaunct ethvaaltu, eino neaacnhIE oEfE t-h9eb utws som sailml puolwateerds ynsetetmwonertkws,o rthk eth naet twork lines
has long TLs. Furthermore, the tests are repeated on an IEEE 39-bus system, as a large
have different line parameters that significantly affect system homogeneity, in addition to
network system with short TLs, in order to validate and generalize the proposed scheme.
the fact that the TCSC impedance will affect the protected line parameters, which have
It must be pointed out that, in each of the two simulated networks, the network lines
been carefully considered in the adaptive proposed scheme.
have different line parameters that significantly affect system homogeneity, in addition to
the fact that the TCSC impedance will affect the protected line parameters, which have
4b.e2e.n Rceasrueflutsll yofc tohnes iIdEeEreEd-9in Btuhes aSdyasptetmive proposed scheme.
As described in [30], this 60 Hz test system consists of three machines connected to a
4.2. Results of the IEEE-9 Bus System
ring system of nine buses operating at 230 kV through step up transformers of 13.8 kV/230
As described in [30], this 60 Hz test system consists of three machines connected
kV. Each line section is 100 km in length. The loads are added at three locations at different
to a ring system of nine buses operating at 230 kV through step up transformers of
b13u.8seksV. T/C23S0Ck iVs. cEoanchnelcinteeds,e actsi osnhoisw1n0 0ink mFiginurlee n6g, taht. thTeh emlioda-dpsoairnet aodf dthede laitnteh breeetween buses
9lo caantido n6s wat hdiilfefe rtehnet bpursoeps.oTseCdS Cdiessciognnneedc terdel,aays sihso lwoncaitneFdi gautr eb6u,sa t9t.h Tehmei dp-rpootienct toefd zones are
the line between buses 9 and 6 while the proposed designed relay is located at bus 9. The
sequentially considered at 80% of the protected line for zone-1, while zone-2 and zone-3
protected zones are sequentially considered at 80% of the protected line for zone-1, while
are extended to 100% of the same line and 20% of the adjacent line, and 100% of the same
zone-2 and zone-3 are extended to 100% of the same line and 20% of the adjacent line, and
protected line and 100% adjacent line, respectively.
100% of the same protected line and 100% adjacent line, respectively.
G2 G3
G1
Figure 6. IEEE-9 bus system equipped with TCSC.
The evaluation divides the tests into five categories to assess the different fault sce-
narios and evaluate the dependability of each design setting compared with the conven-
tional quadrilateral setting.
 Bolted faults without TCSC;
 Adaptive reactive setting while TCSC is included and without fault resistance;
TCSC
7 8 9
Load A
100 MW
192 MVA, 2 35 MVAR 128 MVA,
13.8 kV 13.8/230 kV 13.8/230 kV 13.8 kV
T2 R1 T3
3
I C
L
100 km
I
C
5 R2 6 Ls Th1
Load B I TCR Th2
125 MW
50 MVAR Load C
90 MW
4 30 MVAR
13.8/230 kV T1
1
247 MVA,
13.8 kV
Figure 6. IEEE-9 bus system equipped with TCSC.

## PDF page 11

Energies 2021, 14, 7074 11 of 23
Energies 2021, 14, x FOR PEER REVIEW 11 of 23
The evaluation divides the tests into five categories to assess the different fault scenar-
ios and evaluate the dependability of each design setting compared with the conventional
▪ Aqudaadpritliavteer arlesseitsttinivge. setting for faults before TCSC;
▪ Adaptive resistive setting for faults after TCSC;
(cid:110) Bolted faults without TCSC;
▪ E(cid:110) valuAadtainptgiv tehree apctriovpe osestetidng swchheilme TeC aStC thisei ntcwluod eednadnsd owf iTthLo.u t fault resistance;
(cid:110) Adaptive resistive setting for faults before TCSC;
4.2.1. (cid:110)Bolt A ed d a F p a ti u v l e ts re w sis i t t i h ve ou se t t t T in C g S fo C r f aults after TCSC;
(cid:110) Evaluating the proposed scheme at the two ends of TL.
For selectivity and effectiveness issues, the proposed scheme is evaluated under
bolted4. 2g.1r.oBuonltded faFauullttss awliothnogu tTTLC SaCt different fault locations for instantaneous and back-up
zones of pFroor tseelcetcitoivnit ywainthdoefufetc TtivCeSnCes.s i ssues, the proposed scheme is evaluated under bolted
ground faults along TL at different fault locations for instantaneous and back-up zones of
The trajectory impedances of the proposed scheme (the solid black characteristic) and
protection without TCSC.
the conventional relay (the dashed red characteristic) are addressed in Figure 7 for the
The trajectory impedances of the proposed scheme (the solid black characteristic)
boltedan Ld-Gth efacounltv eant t2io.n0a2l5r esl auyn(dtheer ddaisfhfeerdernetd lcohcaartaicotenrsis otinc) TarLe taod dcroevsseerd ailnl Fthigeu zreo7nefosr of protec-
tion wthiethbooultet dTLC-SGCfa. uAltsa sth2o.0w25ns iunn dthere dfiifgfeurreen,t tlohcea tpiornospoonseTdL tsochcoevmere a(lbl lthaeckz)o nceosinocf ides with
protection without TCSC. As shown in the figure, the proposed scheme (black) coincides
the conventional one (red) as there is no need for any adaptive reaches under plain fault
with the conventional one (red) as there is no need for any adaptive reaches under plain
conditions, which reduces the computational burden of the relay.
fault conditions, which reduces the computational burden of the relay.
(a) (b)
Figure 7. IFmigpuered7a.nImcep etrdaajneccettorrayje cftoorry bfoorltbeodlte Ld-LG-G ffaauullttss aat t2 .202.052s5. (as). F(aau) ltFsabueflotsre btheefomried -tphoein mt oifdth-pe opriontte cotefd thlinee ;p(rbo) tfeauctltesd line; (b)
faults aftera ftthere tmheimd-idp-opionint tooff tthhee pprrootetcetcetdeldin lei.ne.
4.2.2. Adaptive Reactive Setting While TCSC Is Included and without Fault Resistance
4.2.2. Adaptive Reactive Setting While TCSC Is Included and without Fault Resistance
As discussed, the adaptive reactive setting will be only applied in the case that TCSC
Aissi ndciluscduedssinedth, ethfaeu lateddalpootipv.eT hreuas,cftoirvbeo slteetdtifnaugl tws bilelf obree ToCnSlyC ,atphepTliCeSdC iind etnhteifi ccaatsieon that TCSC
is inclzuondeeids iinna ctthivea tfeadu, latneddt hloeorepfo. rTe hthuesa,d faoprt ibveolstcehdem fae udlotess bneotfoprreoc TeeCdS. ACc, ctohrdei nTgClyS, Cth eidentifica-
settings of all zones are matched with the conventional characteristic settings (dashed red
tion zone is inactivated, and therefore the adaptive scheme does not proceed. Accord-
characteristic) as in case (a) of Figure 7.
ingly, the settings of all zones are matched with the conventional characteristic settings
To evaluate changing of the reactive setting reach adaptively, many cases of bolted
(dashed red characteristic) as in case (a) of Figure 7.
ground faults are applied after TCSC under different TCSC modes of operation. The worst
Tcaos eesvfaolrutahteef ocuhramngodinegs ooffo tpheera rtieoancitnivaell szeotnteins gar ereaadcdhr eassdeadphteivreefloyr, amssaenssym ceansteosf of bolted
grounthde fsacuheltms ea.re applied after TCSC under different TCSC modes of operation. The worst
cases (cid:110)for tFhoer fcoauparc mitivoedaensd obfl oocpkeinragtTioCnS Cino paellr aztoionne, sth aeraep apdardernet simsepde dhaenrcee ftorarj eacstosreyssfomr ent of the
2L-G bolted faults at 85% and 125% of the protected line from the tested relay ®is
scheme.
presented in Figure 8. As displayed, the conventional distance relay overreaches
▪ For capacitive and blocking TCSC operation, the apparent impedance trajectory for
2L-G bolted faults at 85% and 125% of the protected line from the tested relay ® is
presented in Figure 8. As displayed, the conventional distance relay overreaches in
both modes of operation and detects zone-2 faults (at 85%) and zone-3 faults (at
125%) incorrectly as zone-1 faults. Meanwhile, the proposed adaptive quadrilateral
distance relay (the solid black characteristic) succeeded in detecting such faults in
their corresponding zones of protection by reducing the reactive reach by the TCSC
reactance value.
▪ For the inductive and bypass modes, Figure 9 demonstrates the trajectory impedance
for the bolted 3L-G fault performed at 75% and 110% of the protected line near the
end edges of zone-1 and zone-2, respectively. As shown in the figure, the proposed

## PDF page 12

Energies 2021, 14, 7074 12 of 23
in both modes of operation and detects zone-2 faults (at 85%) and zone-3 faults (at
125%) incorrectly as zone-1 faults. Meanwhile, the proposed adaptive quadrilateral
distance relay (the solid black characteristic) succeeded in detecting such faults in
their corresponding zones of protection by reducing the reactive reach by the TCSC
Energies 2021, 14, x FOR PEER REVIEW 12 of 23
reactance value.
(cid:110) For the inductive and bypass modes, Figure 9 demonstrates the trajectory impedance
for the bolted 3L-G fault performed at 75% and 110% of the protected line near the end
edges of zone-1 and zone-2, respectively. As shown in the figure, the proposed scheme
scheme correctly detected the faults occurring in zone-1 (at 75%) and zone-2 (at 110%)
correctly detected the faults occurring in zone-1 (at 75%) and zone-2 (at 110%) for
for bobothth mmooddeesso foTfC TSCCSoCpe roaptieonra, wtihoinle, mwahl-iolpee rmataioln-os pocecruartrieodnwsi tohctchue rcroendve nwtiiotnha lthe conven-
tionasle stteinttgisntghsa ttehxapte reixenpceertireicnkcyeu tnrdicekrryea uchnindgeirnrebaocthhciansges i.n both cases.
(a) (b)
(c) (d)
Figure 8. ImFipguedrea8n. cIme ptreadjaenccteotrryaj efcotor rtyhfeo r2tLhe-G2L f-aGuflatu altta 2t .20.0 ss.. ((aa)) AAtt8 85%5%of othfe tlhinee luinned eur ncadpearc ictiavpe amcoidtiev;e(b m) aot d12e5;% (bo)f tahte 125% of the
line under clianpe aucnidteivr cea mpaocidtivee; (mco) daet; 8(c5)%at 8o5f% thoef tlhienlein uenudndeerr bblloocckkininggm modoed; (ed;) (adt )1 2a5t% 1o2f5t%he olifn ethuen dlienr eb luocnkdinegrm bolodec.king mode.
(a) (b)

## PDF page 13

Energies 2021, 14, x FOR PEER REVIEW 12 of 23
scheme correctly detected the faults occurring in zone-1 (at 75%) and zone-2 (at 110%)
for both modes of TCSC operation, while mal-operations occurred with the conven-
tional settings that experience tricky underreaching in both cases.
(a) (b)
(c) (d)
Figure 8E.n Iemrgiepse20d2a1,n1c4,e7 0t7r4ajectory for the 2L-G fault at 2.0 s. (a) At 85% of the line under capacitive mode; (b) a1t3 1o2f 523% of the
line under capacitive mode; (c) at 85% of the line under blocking mode; (d) at 125% of the line under blocking mode.
Energies 2021, 14, x FOR PEER REVIEW 13 of 23
(a) (b)
(c) (d)
Figure 9. ImFpiegduraen9c. eIm trpaejdeacntcoertyra fjeocrto trhyefo 3rLth-eG3 Lfa-Gulfta ualtt a2t.02.20525 ss.. ((aa)) aatt7 75%5%of othfe tlhinee luinndee ur ninddeurct iivnedmuocdtiev; (eb )mato1d1e0%; (bof)t haet 110% of the
line under inlidneuuctnidveer imndoudcteiv; e(cm) oadte 7; (5c%) a to7f5 %thoef ltihneeli nuenudnedre rbbyyppaassssm modoed;e(d; )(dat)1 a10t %11o0f %the olifn tehuen dlienreb yupnadssemr obdyep. ass mode.
4.2.3. Adaptive Resistive Setting for Faults before TCSC
4.2.3. Adaptive Resistive Setting for Faults before TCSC
For evaluating the effectiveness of updated resistive scheme, a set of different resistive
FoL-rG efvaaulltusa(wtiinthg5 t0hΩe, e1f0f0eΩct,i2v0e0nΩe,sasn odf2 5u0pΩdafatueldt r erseissitasnticve)ew secrheeimmpele, ma esnetet doefv deriyfferent resis-
10% of the protected line before TCSC in either the capacitive or inductive mode.
tive L-G faults (with 50 Ω, 100 Ω, 200 Ω, and 250 Ω fault resistance) were implemented
As illustrated in Figure 10, the conventional relay (the dashed red characteristic) lost
every
i
1
ts
0%
se le
o
c
f
t i
t
v
h
it
e
y
p
fo
r
r
o
a
te
ll
c
f
t
a
e
u
d
lt s
li
w
n
i
e
t h
b
r
e
e
f
s
o
is
r
t
e
a n
T
c
C
e 5
S
0
CΩ in
w
e
h
i
i
t
c
h
h
e
o
r
c c
t
u
h
r
e
r e
c
d
a
a
p
t
a
z
c
o
i
n
ti
e
v
-1
e
,
o
an
r
d
in
fa
d
ls
u
e
c
ly
tive mode.
Adse itlelcutesdtrtahteemdi ninz oFnige-u3.reF u1r0th, etrhmeo creo,nthveencotniovnenatli orneallarye l(atyhwe adsausnhaebdle rtoedde ctehcat rtahecteristic) lost
its selercemtivaiintiyn gfofaru latsllu fnaduerlt1s0 0w Ω i,th20 0re Ω s,isantadn2c5e0 Ω 50. O Ωn twhehciocnhtr aorcy,ctuherrperdop aoste zdoscnhee-m1e, (athned falsely de-
solid black characteristic) superiorly adapted its resistive blinder to sufficient reach based
tected them in zone-3. Furthermore, the conventional relay was unable to detect the re-
on the fault location and fault resistance value in all cases. However, TCSC is inserted in
maining faults under 100 Ω, 200 Ω, and 250 Ω. On the contrary, the proposed scheme (the
TL but, as these faults are before TCSC, the reactive reach kept its setting the same as the
solid bcloancvke ncthioanraal cretelaryi.stic) superiorly adapted its resistive blinder to sufficient reach based
on the fault location and fault resistance value in all cases. However, TCSC is inserted in
TL but, as these faults are before TCSC, the reactive reach kept its setting the same as the
conventional relay.
As described before, the fault resistance border (𝑅 ) is determined using Equation
𝑓𝑠𝑒𝑡
(8), and therefore the new updated resistive setting will be directly identified according
to the fault resistance. As shown in Figure 10, when the fault occurs in zone-1 (as an in-
stantaneous protected zone), the trip boundaries of three zones of protection will be adap-
tively changed by updating their resistive reach.
(a) (b) (c) (d)
(e) (f) (g) (h)

## PDF page 14

Energies 2021, 14, x FOR PEER REVIEW 13 of 23
(c) (d)
Figure 9. Impedance trajectory for the 3L-G fault at 2.025 s. (a) at 75% of the line under inductive mode; (b) at 110% of the
line under inductive mode; (c) at 75% of the line under bypass mode; (d) at 110% of the line under bypass mode.
4.2.3. Adaptive Resistive Setting for Faults before TCSC
For evaluating the effectiveness of updated resistive scheme, a set of different resis-
tive L-G faults (with 50 Ω, 100 Ω, 200 Ω, and 250 Ω fault resistance) were implemented
every 10% of the protected line before TCSC in either the capacitive or inductive mode.
As illustrated in Figure 10, the conventional relay (the dashed red characteristic) lost
its selectivity for all faults with resistance 50 Ω which occurred at zone-1, and falsely de-
tected them in zone-3. Furthermore, the conventional relay was unable to detect the re-
maining faults under 100 Ω, 200 Ω, and 250 Ω. On the contrary, the proposed scheme (the
solid black characteristic) superiorly adapted its resistive blinder to sufficient reach based
on the fault location and fault resistance value in all cases. However, TCSC is inserted in
TL but, as these faults are before TCSC, the reactive reach kept its setting the same as the
conventional relay.
As described before, the fault resistance border (𝑅 ) is determined using Equation
𝑓𝑠𝑒𝑡
(8), and therefore the new updated resistive setting will be directly identified according
to the fault resistance. As shown in Figure 10, when the fault occurs in zone-1 (as an in-
Energies 2021, 14, 7074 14 of 23
stantaneous protected zone), the trip boundaries of three zones of protection will be adap-
tively changed by updating their resistive reach.
(a) (b) (c) (d)
Energies 2021, 14, x FOR PEER REVIEW 14 of 23
(e) (f) (g) (h)
(i) (j) (k) (l)
(m) (n) (o) (p)
FFigiguurere1 100. .I mImppeeddaanncceet rtraajejecctotorryyf oforrt htheeL L-G-Gf afauultlta at t2 .20.20255s .s.( a(a) )A At t1 01%0%a nanddR 𝑅
f
𝑓= =5 050Ω Ω; (;b ()ba) ta1t 01%0%a nadndR
f
𝑅 𝑓= 1=0 100Ω0 Ω; (;c )(ca)t a1t0 %
a 1 n 0 d % R an = d 2 𝑅 0𝑓0 Ω= ; 2 ( 0 d 0 ) Ω at ; ( 1 d 0 ) % at a n 10 d % R an = d 2 𝑅 5𝑓0 Ω= ; 2 ( 5 e 0 ) Ω at ; 2 (e 0 ) % at a n 20 d % R an = d 5 𝑅 0𝑓Ω = ; ( 5 f 0 ) a Ω t ; 2 ( 0 f) % at a n 20 d % R an = d 1 0 𝑅 0𝑓 Ω= ; 1 ( 0 g 0 ) Ω at ; 2 (g 0% ) a a t n 2 d 0% R an = d 2 0 𝑅 0𝑓 Ω;
f f f f f
(h = ) 2 a 0 t 0 2 Ω 0% ; (h a ) n a d t R 20% = a 2 n 5 d 0 Ω𝑅 𝑓; ( = i) 2 a 5 t 0 3 Ω 0% ; (i a ) n a d t 3 R 0% = an 50 d Ω𝑅 𝑓; (j = ) 5 a 0 t Ω 30 ; % (j) a a n t d 30 R % = an 1 d 0 0 𝑅Ω𝑓 ; = ( 1 k 0 ) 0 a Ω t 3 ; 0 ( % k) a a n t d 30 R % a = nd 20 𝑅 0𝑓Ω = ; ( 2 l 0 ) 0 a Ω t 3 ; 0 (l % ) a a t n d
f f f f
30% and 𝑅 = 250 Ω; (m) at 40% and 𝑅 = 50 Ω; (n) at 40% and 𝑅 = 100 Ω; (o) at 40% and 𝑅 = 200 Ω; (p) at 40% and 𝑅
R = 250 Ω;𝑓(m) at 40% and R = 50 Ω; 𝑓(n) at 40% and R = 100 Ω𝑓; (o) at 40% and R = 200 Ω𝑓 ; (p) at 40% and R = 250 𝑓Ω.
=f 250 Ω. f f f f
As described before, the fault resistance border (R ) is determined using Equation (8),
f set
4.2.4. Adaptive Resistive Setting for Faults after TCSC
and therefore the new updated resistive setting will be directly identified according to the
faultTrehsei sptaenrfcoer.mAasnscheo owf nthine Fpirgouproes1e0d, wdyhneanmthice qfauualdt roiclacuterrsailn rezloanye -c1an(a bs ea ncoinmsptaanrteadn etoo us
pthreo tceocntevdenztoionnea),l trheelatyri wp ibthou finxdeadr ciehsaorafcttherreisetizco sneetstinofgsp rboyt eacptpiolyninwgi lal bseeta odf arpestiivsteilvye cfhauanltgs ed
bafyteurp TdCatSiCng utnhdeeirr rtehseis tfiovuer rdeaifcfher. ent modes of operation at different critical locations,
where the conventional relay may lose its selectivity-relaying function by underreach-
4in.2g./4o.vAerdraepactihviengR seisgisntiifviceaSnetltyti ndguefo tro Fthaeu letxsiastfetenrceT CofS TCCSC reactance in the faulted loop.
Figures 11–14 illustrate the correctness of the dynamically updated settings (the solid
The performance of the proposed dynamic quadrilateral relay can be compared to
t b h la e ck co c n h v a e ra n c t t i e o r n is a t l ic r ) e f l o a r y L w -G it h fau fi l x ts e d at c 2 h .0 a 2 r 5 a c s t w er i i t s h t ic 𝑅 𝑓s e = t t 5 i 0 n g Ω s , 1 b 0 y 0 a Ω p , p a l n y d in 2 g 00 a Ω se a t t o lo f c r a e ti s o is n t s i ve
85% and 125% under the blocking mode and capacitive TCSC modes, respectively. In ad-
faults after TCSC under the four different modes of operation at different critical locations,
dition, the same faults are simulated with similar fault conditions but at 75% and 110% of
where the conventional relay may lose its selectivity-relaying function by underreach-
the line under the inductive and bypass TCSC modes of operation, respectively. On con-
ing/overreaching significantly due to the existence of TCSC reactance in the faulted loop.
trary, the conventional fixed characteristic settings (the dashed red characteristic) com-
Figures 11–14 illustrate the correctness of the dynamically updated settings (the solid
b
p
l
l
a
e
c
te
k
ly
c h
fa
a
i
r
l
a
e
c
d
t e
to
ri s
d
t
e
ic
t
)
ec
f
t
o r
su
L
c
-
h
G
f
f
a
a
u
u
lt
l
s
ts
d
a
u
t
e
2
t
.0
o
2
b
5
o
s
th
w
t
i
h
th
e e
R
ffe
=
ct
5
s
0
ofΩ f
,
a
1
u
0
lt
0
rΩes
,
is
a
t
n
a
d
nc
2
e
0
a
0
nΩd t
a
h
t
e
l o
e
c
x
a
is
ti
t
o
-
ns
f
ence of TCSC in the fault loop.
85% and 125% under the blocking mode and capacitive TCSC modes, respectively. In
It is also worth clarifying here that the scenario of the resistive faults with TCSC in-
addition, the same faults are simulated with similar fault conditions but at 75% and
cluded in the faulted loop is different from the cases for faults without TCSC. Although
110% of the line under the inductive and bypass TCSC modes of operation, respectively.
TCSC has only inductance behaviour, but it affects the resistive reach unless its negative
impact is compensated for by tile angle, as discussed in Equation (5) and considered in
the fault zone identifier by modifying the Takagi method in Equation (6) to determine the
fault resistance border. Otherwise, the 𝑅
𝑓
term will be a complex value and adds an ad-
ditional reactance value to the fault. Additionally, if the proposed adaptive dynamic set-
ting scheme only adapts the resistive reach without adapting the reactive reach, the relay
will falsely detect the resistive fault due to underreach or overreach depending on TCSC
operational mode. Accordingly, it is concluded that the proposed dynamic setting scheme
is essential for such cases.

## PDF page 15

Energies 2021, 14, 7074 15 of 23
On contrary, the conventional fixed characteristic settings (the dashed red characteristic)
EEEnnneeerrrgggiiieeesss 222000222111,,, 111444,,, xxx FFFOOORRR PPPEEEEEERRR RRREEEVVVIIIEEEWWW 111555 ooofff 222333
completely failed to detect such faults due to both the effects of fault resistance and the
existence of TCSC in the fault loop.
(((aaa))) (((bbb))) (((ccc)))
FFFiiigggFuuuirrrgeeeu 1r11e111...1 A1AA.pppAppppaaaprrreaeenrnnetttn iiitmmmimppppeeededddaaaannnncccceeee llllooooccccuuuussss ffffoooorrrr tttthhhheeeeL LLL-G---GGGf a fffuaaaluuutlllattt t aaa2ttt. 02222...5000222s555a tsss 8 aaa5ttt% 8885o55%f%%t h oooefff ltitthnhheeee ullliiinnnndeeee uruuntnnhdddeeeeTrrr C ttthShhCeee TbTTlCCCoScSSkCCCi n bbbglllooomcccokkkdiiinnneg.gg ( mamm)oooWdddieeet.h.. (((aaa)))
WWWiiitttRhhhf 𝑅𝑅=𝑅
𝑓𝑓𝑓
5 0=== Ω555000; (ΩΩΩb);;; (w((bbbi)))t hwwwRiiitttf hhh= 𝑅𝑅𝑅1
𝑓𝑓𝑓
0 0=== Ω 1110;000(00c Ω)ΩΩw;;; (i((ctcch))) wwwRi
f
iittth=hh 2𝑅𝑅𝑅0
𝑓𝑓𝑓
0 Ω=== 2.22000000 ΩΩΩ...
(((aaa))) (((bbb))) (((ccc)))
FFFiiigggFuuuirrrgeeeu 111re222...1 AAA2.pppApppaaaprrrpeeeannnrttte iniimmmt pippmeeedddpaeaandnncacceene cllloeoocccluuouscss u fffosoorrrf o ttthrhheeeth LLLe---GLGG- Gfffaaauuufallltutt alaatttt a 222t...0002222.05552 ss5s aaasttt a 111t22215552%%%5% ooofffo tttfhhhteeeh lelliiinnnlieeen ueuunnnudddneeedrrre trtthhhteeeh eTTTCTCCCSSSCCCSC cccaaacpppapaaacacciiictttiiiitvvviveee e mmmmooooddddeeee... .(((aaa)))
WWWiiit(tthahh) 𝑅W𝑅𝑅 𝑓𝑓𝑓 i t=h== 55R5000 f ΩΩΩ=;;;5 (((0bbbΩ))) www; (iiibttth)hh w 𝑅𝑅𝑅i𝑓𝑓𝑓 th ===R 111 f 000=000 1ΩΩΩ0;0;; (((Ωccc))); www(ciii)ttthwhh i𝑅𝑅𝑅th𝑓𝑓𝑓 R=== f 222=0000002 0ΩΩΩ0...Ω .
(((aaa))) (((bbb))) (((ccc)))
FFFiiigggFuuuirrrgeeeu 1r11e333...1 A3AA.pppAppppaaaprrreaeenrnnetttn iiitmmmimppppeeededddaaaannnncccceeee llllooooccccuuuussss ffffoooorrrr tttthhhheeeeL LLL-G---GGGf a fffuaaaluuutlllattt t aaa2ttt. 02222...0500222s555a tsss 7 aaa5ttt% 7775o55%%f%t h oooefff lttithnhheeee ullliiinnnndeeee uruuntnnhdddeeeeTrrr C ttthhShCeee TTTinCCCdSSSuCCCct iiiivnnnedddmuuucccotttdiiivvve.eee ( mamm)oooWdddieeeth... (((aaa)))
WWWiiitttRhhhf 𝑅𝑅𝑅=
𝑓𝑓𝑓
5 0=== Ω 555000; (ΩΩΩb);;; (w((bbbi)))t hwwwRiiitttfhhh = 𝑅𝑅𝑅1
𝑓𝑓𝑓
0 0=== Ω 111000; 0(00c Ω)ΩΩw;;; (i((ctcch))) wwwRifiittth=hh 2𝑅𝑅𝑅0
𝑓𝑓𝑓
0 Ω === 2.22000000 ΩΩΩ...
It is also worth clarifying here that the scenario of the resistive faults with TCSC
included in the faulted loop is different from the cases for faults without TCSC. Although
TCSC has only inductance behaviour, but it affects the resistive reach unless its negative
impact is compensated for by tile angle, as discussed in Equation (5) and considered in the
fault zone identifier by modifying the Takagi method in Equation (6) to determine the fault
resistance border. Otherwise, the R term will be a complex value and adds an additional
f
reactance value to the fault. Additionally, if the proposed adaptive dynamic setting scheme
only adapts the resistive reach without adapting the reactive reach, the relay will falsely
detect the resistive fault due to underreach or overreach depending on TCSC operational
(((aaa))) (((bbb))) (((ccc)))
FFFiiiggguuurrreee 111444... AAAppppppaaarrreeennnttt iiimmmpppeeedddaaannnccceee lllooocccuuusss fffooorrr ttthhheee LLL---GGG fffaaauuulllttt aaattt 222...000222555 sss aaattt 111111000%%% ooofff ttthhheee llliiinnneee uuunnndddeeerrr ttthhheee TTTCCCSSSCCC bbbyyypppaaassssss mmmooodddeee... (((aaa))) WWWiiittthhh
𝑅𝑅𝑅
𝑓𝑓𝑓
=== 555000 ΩΩΩ;;; (((bbb))) wwwiiittthhh 𝑅𝑅𝑅
𝑓𝑓𝑓
=== 111000000 ΩΩΩ;;; (((ccc))) wwwiiittthhh 𝑅𝑅𝑅
𝑓𝑓𝑓
=== 222000000 ΩΩΩ...

## PDF page 16

Energies 2021, 14, x FOR PEER REVIEW 15 of 23
(a) (b) (c)
Figure 11. Apparent impedance locus for the L-G fault at 2.025 s at 85% of the line under the TCSC blocking mode. (a)
With 𝑅 = 50 Ω; (b) with 𝑅 = 100 Ω; (c) with 𝑅 = 200 Ω.
𝑓 𝑓 𝑓
(a) (b) (c)
Figure 12. Apparent impedance locus for the L-G fault at 2.025 s at 125% of the line under the TCSC capacitive mode. (a)
With 𝑅 = 50 Ω; (b) with 𝑅 = 100 Ω; (c) with 𝑅 = 200 Ω.
𝑓 𝑓 𝑓
Energies 2021, 14, 7074 16 of 23
(a) (b) (c)
Figure 13. Apparent impedance locus for the L-G fault at 2.025 s at 75% of the line under the TCSC inductive mode. (a)
mode. Accordingly, it is concluded that the proposed dynamic setting scheme is essential
With 𝑅 = 50 Ω; (b) with 𝑅 = 100 Ω; (c) with 𝑅 = 200 Ω.
𝑓 𝑓 for such cases. 𝑓
(a) (b) (c)
Energies 2021, 14, x FOR PEER REVIEW 16 of 23
FigFuigreu r1e4.1 A4.pAppapreanretn itmimpepdeadnacnec elolocucuss foforr tthhee LL--GG ffaauulltt aatt 22..002255 ss aatt 111100%%o offt htheel ilnineeu unndderetrh teheT CTSCCSCby bpyapssasms omdoe.d(ea.) (Wa)i tWh ith
𝑅 𝑓 R=f 5=0 5Ω0; Ω(b; )( bw)iwthi th𝑅 𝑓 R f= =10100 0ΩΩ; (;c()c )wwitihth 𝑅R 𝑓f == 220000 ΩΩ..
4.2.5. Evaluating the Proposed Scheme at the Two Ends of TL
4.2.5. Evaluating the Proposed Scheme at the Two Ends of TL
An L-G fault is simulated under the capacitive TCSC mode at 2.015 s with a large 𝑅
An L-G fault is simulated under the capacitive TCSC mode at 2.015 s with a large R𝑓
f
o
o
f
f
1
1
5
5
0
0
ΩΩ
a
a
t
t
t
t
h
h
e
e
lo
lo
c
c
a
a
ti
t
o
io
n
n
o
o
f
f
8 5
8
%
5%
f r
f
o
r
m
om
th
t
e
h
fi
e
r
f
s
i
t
rs
r
t
e l
r
a
e
y
la
R
y
1
R
(i
1
n
(
i
i
t
n
s z
it
o
s
n
z
e
o
-2
n
)
e
,
-
w
2)
h
,
i
w
ch
h
a
ic
ls
h
o
a
m
ls
e
o
a n
m
s
e
t
a
h
n
a
s
t
that the fault is 15% from the opposite relay R2 (in its zone-1).
the fault is 15% from the opposite relay R2 (in its zone-1).
Upon implementing the proposed scheme in both relays (R1 and R2), Figure 15 illus-
Upon implementing the proposed scheme in both relays (R1 and R2), Figure 15
tirlalutesstr tahtee setfhfeecteifvfeecnteivsse noef sths eoifr tdhyeniradmyincaalmlyi cuaplldyautepdd saetettdinsgest t(ibnlgasck(b sloalcikd)s ocolimd)pcaormedp wariethd
twheit hcotnhveecnotniovneanlt icohnaarlacchtearriastcitce rsiestttiicnsgest t(irnegds d(areshdedda)s whehdic)hw fhaiilcehdf taoil eddetteoctd tehtiesc ftatuhlits ffraoumlt
bfrootmh ebnodtsh. e nds.
(a) (b)
(c) (d)
FFiigguurree 1155.. AAnn LL--GG ffaauulltt uunnddeerr tthhee ccaappaacciittiivvee TTCCSSCC mmooddee aatt 22..001155 ss wwiitthh 𝑅R 𝑓f == 115500 Ω Ω aatt tthhee llooccaattiioonn ooff 8855%% ffrroomm tthhee ffiirrsstt
rreellaayy RR11.. ((aa)) CChhaarraacctteerriissttiiccss ooff tthhee ffiirrsstt eenndd rreellaayy RR11;; ((bb)) cchhaarraacctteerriissttiiccss ooff tthhee sseeccoonndd eenndd rreellaayy RR22;; ((cc)) ffaauulltt ddeetteeccttiioonn ooff tthhee
ffiirrsstt eenndd rreellaayy RR11;; ((dd)) ffaauulltt ddeetteeccttiioonn ooff tthhee sseeccoonndd eenndd rreellaayy RR22..
AAss iiss ccleleaarrlyly sshhoowwnn, ,ththe epprorpoposoesde ddydnyanmamici rcerlaeyla Ry1R c1ocrroercrtelcyt ldyedteectteecdt etdhet hfaeuflat uinlt iitns
zitosnzeo-2n (ed-2et(edcteetdec itte adt 2it.0a2t524 .s0)2 b5y4 asd) abpytiandga bpottinhg rebsoistthivree asinsdti vreeaactnivder reeaaccthiv seo rietsa ctrhipspoinitgs
ttirmipep winags tdimeleayweads bdye ltahyee zdobnye-t2h etimzoen de-e2latyim, we hdielela tyh, ew phrioleptohseedp rdoypnoasmedicd ryenlaaym aict Rre2l asyuca-t
ceeded in detecting the same fault in its zone-1 (detecting it at 2.025 s) by adapting only
its resistive reach without adapting its reactive reach, as TCSC is not included in its faulted
path and thus it trips instantaneously.
4.3. Further Evaluation on a Larger Test System—IEEE-39 Bus System
In order to validate the proposed scheme on a larger test system, the methodology
was widely examined on the modified 60 Hz IEEE-39 bus New England system, as shown
in Figure 16 [31]. In the modified 39-bus system, TCSC is placed at the mid-point of the
line between buses 28 and 29.

## PDF page 17

Energies 2021, 14, 7074 17 of 23
R2 succeeded in detecting the same fault in its zone-1 (detecting it at 2.025 s) by adapting
only its resistive reach without adapting its reactive reach, as TCSC is not included in its
faulted path and thus it trips instantaneously.
4.3. Further Evaluation on a Larger Test System—IEEE-39 Bus System
In order to validate the proposed scheme on a larger test system, the methodology
was widely examined on the modified 60 Hz IEEE-39 bus New England system, as shown
Energies 2021, 14, x FOR PEER REVIEW 17 of 23
in Figure 16 [31]. In the modified 39-bus system, TCSC is placed at the mid-point of the
line between buses 28 and 29.
IL C
IC
Ls Th1
G8 ITCR Th2
G10
37 R1
TCSC
30 1 km 29
25 26 28
2 38
27
1
G1 24 G9
18
39 17 G6
35
3 16
15 21 22
4
14
5 6 12 19 23
7 13 20 33 36
11
8 10 34 G4 G7 345 kV
9 230 kV
31 32 G5 22 kV
G2
G3
Figure 16. Schematic diagram of the IEEE 39-bus New England system compensated for by TCSC.
Figure 16. Schematic diagram of the IEEE 39-bus New England system compensated for by TCSC.
It is to be noted that the TCSC compensation provided in the 39-bus test system is
It is to be noted that the TCSC compensation provided in the 39-bus test system is
exactly the same as that discussed for the IEEE-9 bus power system in the earlier section.
exactly the same as that discussed for the IEEE-9 bus power system in the earlier section.
The proposed distance relay R1, placed at bus-29 for protecting lines 28–29, is considered
Tfhoer pperorfpoormseadn cdeisetvaanlcuea trieolna.yA Rs1e, tpolaf creesdi satitv beugsr-o2u9n fdoerd pfraoutletcstainreg alpinpelise 2d8o–n29d,i ifsfe croenntsidered
folorc pateiorfnosr, maftaenrcteh eeTvCaSluCaltoiocant.i oAn, isnetb ootfh rtehseisctaipvaec igtirvoeuannddeidnd fuacutilvtse maroed easpopflioepde roatnio dn,ifferent
lowciathtiodnifsfe, raefnttefra uthlter eTsCistSaCn cleo, ctoateivoanl,u ainte bthoethp rtohpeo sceadpraecliatyivpee rafnordm ianndceucatnidved ymnaomdeicsa lolyf opera-
updating the resistive and reactive reaches under either the capacitive or inductive TCSC
tion, with different fault resistance, to evaluate the proposed relay performance and dy-
modes of operation.
namically updating the resistive and reactive reaches under either the capacitive or induc-
Figure 17 demonstrates the trajectory impedance for L-G faults at the end of zone-1 of
tive TCSC modes of operation.
the tested relay (at 75%) with R = 50 Ω and 100 Ω, and also at the end of zone-2 (at 110%)
f
with
F
R
igu
=
re
5 0
17Ω d
u
e
n
m
de
o
r
n
t
s
h
t
e
ra
T
t
C
es
S C
th
i
e
n d
tr
u
a
c
je
ti
c
v
t
e
or
m
y
o
i
d
m
e.
p
T
e
h
d
e
an
fi
c
g
e
u r
f
e
or
h i
L
g
-
h
G
li g
f
h
a
t
u
s
lt
th
s
e
a
p
t
e
th
rf
e
o r
e
m
nd
an
o
ce
f zone-1
f
o o f f th th e e t p e r s o te p d o s r e e d la r y el a ( y at w 7 i 5 th % d ) y w n i a t m h ic 𝑅 a𝑓l ly= u 5 p 0 d Ω at e a d nd se t 1 t 0 in 0 g Ω s ( , t h a e nd so a li l d so b l a a t c k th c e h a e r n a d ct e o r f i s z ti o c n ) e-2 (at
1v10er%su) swthitehc o𝑅n𝑓v e=n 5ti0o nΩa lurneldaeyrw thiteh TthCeSfiCx eidndchuacrtaivctee rmistoidc e(t.h Tehdea sfhigeudrree dhicghhalriagchtetrsi stthice) .perfor-
mTahnecaec hoife vthede prersoupltossceodn firremlaeyd wthieths udcycensasmoficthalelyp ruoppodsaetdedsc sheetmtiengins d(ethteec tsionglidal lbflaauclkts charac-
teristic) versus the conventional relay with the fixed characteristic (the dashed red char-
acteristic). The achieved results confirmed the success of the proposed scheme in detecting
all faults with a high degree of selectivity. As is clearly shown, the faults at 75% are de-
tected correctly in zone-1, either with 50 Ω fault resistance (case-a) or 100 Ω fault resistance
(case-b); in addition, the fault at 110% of the line is detected properly in zone-2 (case-c)
due to the zone identification method, while the fixed conventional setting completely
failed to detect such faults.
Under the TCSC capacitive mode, the impedance trajectory for 2L-G faults in zone-2
and zone-3 is illustrated in Figure 18. For cases a and b, the faults occurred at 85% of the
line with 𝑅 = 50 Ω and 100 Ω, while in case c, the fault was simulated at the beginning of
𝑓
zone-3 (at 125%) with 𝑅 = 50 Ω. As is obviously revealed, the conventional relay lost its
𝑓
selectivity in all examined cases. In fact, the conventional relay erroneously underreaches
in case a as the fault is detected in zone-3 and, on the other hand, it incorrectly overreaches
for the fault in zone-3 as illustrated in case c. In addition, it failed to detect the fault in case

## PDF page 18

Energies 2021, 14, x FOR PEER REVIEW 18 of 23
Energies 2021, 14, 7074 18 of 23
b under the high fault resistance value; on the contrary, the proposed relay tripped cor-
rectly (the solid characteristic) in this case.
As a matter of fact, the achieved results ensure the correct operation of the proposed
with a high degree of selectivity. As is clearly shown, the faults at 75% are detected correctly
scheme, in which the relay adapted its trip boundaries itself in the respective zones under
in zone-1, either with 50 Ω fault resistance (case-a) or 100 Ω fault resistance (case-b); in
TCSC operation, according to the local information at the relay and the received infor-
addition, the fault at 110% of the line is detected properly in zone-2 (case-c) due to the
mation from the TCSC terminal during faulty system conditions that the conventional
zone identification method, while the fixed conventional setting completely failed to detect
Energies 2021, 14, x FOR PEER REVIEW 18 of 23
re
s
la
u
y
ch
is
f a
in
u
c
lt
a
s
p
.
able of handling.
b under the high fault resistance value; on the contrary, the proposed relay tripped cor-
rectly (the solid characteristic) in this case.
As a matter of fact, the achieved results ensure the correct operation of the proposed
scheme, in which the relay adapted its trip boundaries itself in the respective zones under
TCSC operation, according to the local information at the relay and the received infor-
mation from the TCSC terminal during faulty system conditions that the conventional
relay is incapable of handling.
(a) (b) (c)
FigFuirgeu 1re7.1 A7.pAppapreanret nitmimpepdeadnacnec efofor rththee LL--GG ffaauulltt aatt 11..00 ssu unnddeerrt htheeT CTCSCSCin idnudcuticvteivme omdeo.d(ea.) (Aa)t 7A5t% 75a%nd aRnfd= 𝑅5
𝑓
0 Ω = 5; (0b Ω) a; t(b)
at 7755%% aanndd R𝑅 𝑓f == 110000 Ω Ω;;( (cc))a att1 11100%%a nadndR f𝑅= 𝑓 5=0 5 Ω 0 .Ω.
Under the TCSC capacitive mode, the impedance trajectory for 2L-G faults in zone-2
and zone-3 is illustrated in Figure 18. For cases a and b, the faults occurred at 85% of the
line with R = 50 Ω and 100 Ω, while in case c, the fault was simulated at the beginning of
f
zone-3 (at 125%) with R = 50 Ω. As is obviously revealed, the conventional relay lost its
f
selectivity in all examined cases. In fact, the con ventional relay erroneously underreac hes
in case a as the fault is detected in zone-3 and, on the other hand, it incorrectly overreaches
(a) (b) (c)
for the fault in zone-3 as illustrated in case c. In addition, it failed to detect the fault in
Figure 17. Apparent impedanccaes feorb tuhne dLe-Gr tfhaeulht iagth 1.f0a us lut nredseirs ttahne cTeCvSaClu ined; ounctitvhee mcoondter.a (ray), Atht e75p%ro apnods e𝑅d r=e l5a0y Ωtr;i p(bp)e d
𝑓
at 75% and 𝑅 = 100 Ω; (c) at c1o10rr%e catnlyd (t𝑅he =s o5l0i dΩc. haracteristic) in this case.
𝑓 𝑓
(a) (b) (c)
Figure 18. Apparent impedance for the 2L-G fault at 1.0 s under the TCSC capacitive mode. (a) At 85% and 𝑅 = 50 Ω; (b)
𝑓
at 85% and 𝑅 = 100 Ω; (c) at 125% and 𝑅 = 50 Ω.
𝑓 𝑓
5. Features Assessment with Reference to Other Techniques
Multi-fold advantages of the proposed scheme compared to some other published
techniques shall be addressed and discussed in the following section. The key advantages
of the prop osed scheme are addressed in term s of Fault Detection Time, Fault Resi stance
Coverage, and Data Acquisition and Computation Technique.
(a) (b) (c)
FigFuirgeu 1r8e. 1A8.pApparpeanret nimt ipmepdea5 dn. a 1cne. c F efoa foru rtlht t heD e 2e 2Lt L e--Gc G t iff oaa nuu ll Ttt iaa m tt 11e . .00 ss uunnddeerrt htheeT TCCSCSCca cpaapcaitciviteivme omdeo.d(ea.) (Aa)t 8A5t% 85a%nd aRndf = 𝑅5 𝑓 0 Ω = 5; 0(b Ω) a; t(b)
at 8855%% aanndd R𝑅 𝑓f == 110000 Ω Ω;; ((cc))a att1 12255% A %a s na nd th dR e f𝑅 p𝑓 = r 5 o =0 p 5 Ω o 0 s .Ω e . d scheme is used for fault detection in TCSC-compensated TLs, the
performAsanacme astpteeredof ifsa cctr,ittihcealalcyh iimevpeodrrteasnutl. tTs henussu, raessthesescionrgr etchtiso paeprpartiooancho fftohre tphreo fpaousletd de-
5. Features Assessment with Reference to Other Techniques
tescctihoenm teim, ine wshhoicuhldth beer eelvaayluadataepdte bdyi tisntvreipstbigoautnindga rtihese idtseetlefcitniothne trimesep efcotri voenzeo onfe sthuen wdeorrst
Multi-fold advantages of the proposed scheme compared to some other published
caTsCesS Cino zpoenraet-i1o no,na cthcoer IdEinEgEt-o9 tbhuesl oscyasltienmfo.r Tmhaitsio cnasaet tohcecruerlareyda nwdhtehne rLe-cGei vfaeudlitn wfoarms aaptiponlied
t a e t cf 7rho5 nm% iq to uhf ee s th Ts e hC p aSl rCl o b tte eec ramt d edidn r lae iln sds e e ua drti an2 ng.0 d 0f a7 du5 ils ts cy, u wssys h esitd ceh min is ct hoim en df p oiltl eilom onw esn intthe gad st e atcht tet i h oce no .ni n Tvs het ena ntkitoe ny oaf a lz dre verla oan yc t r aiosg s e s s -
o in fi gnt hcvae op l pata rbo glep e oo wfsehit dah n sd𝑅 clh
𝑓
in e =gm .2 e 0 a 0 r Ω e a u d n d d re e s r s t e h d e i T n C t S er C m i s n d o u f c F t a iv u e lt m D o et d e e ct . i A on s T is im re e, v F ea a l u e l d t R in es F is i t g a u n r c e e
Coverage, and Data Acquisition and Computation Technique.
19a, due to the high resistance fault, the current increases and the voltage decreases insig-
5. Features Assessment with Reference to Other Techniques
nificantly and, therefore, it is expected that the conventional fixed setting will underreach
5.1. FauMltu Dltei-tfeocltdionad Tviamnet ages of the proposed scheme compared to some other published
for this fault. On the other hand, Figure 19b validates the timing of different stages of the
techniques shall be addressed and discussed in the following section. The key advantages
propAosse dth de ipstraonpcoes reedla syc,h setmareti nisg ufrsoemd ftohre ffaauulltt dinecteepcttiioonn itnim TeC tSoC th-ceo dmepteecntsioante tdim TeL.s A, tsh ies
of the proposed scheme are addressed in terms of Fault Detection Time, Fault Resistance
pdeermfoornmstarnacteed s,p weehdil eis t hcrei tfiacualllty i nimceppotirotann otc. cTuhruresd, a asts e2s.0s0in7g5 tsh, itsh ea ppproropaocshe dfo rre tlahye cfaourrlet cdtely-
Coverage, and Data Acquisition and Computation Technique.
treecctoiognn itsiemde t hshaot ual dfa buelt ehvaadlu sattaerdte bdy a itn 2v.e0s1t6ig6a sti, nagn dth teh dee itdeecntitoinfi ctaimtioen f oorf oTnCeS oCf tzhoen we owrasst
cases in zone-1 on the IEEE-9 bus system. This case occurred when L-G fault was applied
at 75% of the protected line at 2.0075 s, which is implemented at the instant of zero cross-
ing voltage with 𝑅
𝑓
= 200 Ω under the TCSC inductive mode. As is revealed in Figure
19a, due to the high resistance fault, the current increases and the voltage decreases insig-
nificantly and, therefore, it is expected that the conventional fixed setting will underreach
for this fault. On the other hand, Figure 19b validates the timing of different stages of the
proposed distance relay, starting from the fault inception time to the detection time. As is
demonstrated, while the fault inception occurred at 2.0075 s, the proposed relay correctly
recognised that a fault had started at 2.0166 s, and the identification of TCSC zone was

## PDF page 19

Energies 2021, 14, 7074 19 of 23
5.1. Fault Detection Time
As the proposed scheme is used for fault detection in TCSC-compensated TLs, the
performance speed is critically important. Thus, assessing this approach for the fault
detection time should be evaluated by investigating the detection time for one of the
worst cases in zone-1 on the IEEE-9 bus system. This case occurred when L-G fault was
applied at 75% of the protected line at 2.0075 s, which is implemented at the instant of
zero crossing voltage with R = 200 Ω under the TCSC inductive mode. As is revealed
f
in Figure 19a, due to the high resistance fault, the current increases and the voltage
decreases insignificantly and, therefore, it is expected that the conventional fixed setting
will underreach for this fault. On the other hand, Figure 19b validates the timing of different
Energies 2021, 14, x FOR PEER REVIEWst ages of the proposed distance relay, starting from the fault inception time to1t9h oef d23e tection
time. As is demonstrated, while the fault inception occurred at 2.0075 s, the proposed relay
correctly recognised that a fault had started at 2.0166 s, and the identification of TCSC
azcohnieevewda ast a2c.0h1ie8 vse, dwhatile2 .t0h1e8 fsa,uwlt hzoilneet hweafsa purlotpzeornlye iwdeanstipfireodp aetr lzyonidee-1n taitfi tehde 2a.t0z2o10n5e -s1 at the
ti2m.0e2p1o0i5nts atnimd efpinoailnlyt athned fafiunlat lwlyatsh deeftaeuctletdw faosr dtheet eccotrerdecfto trritph eatc 2o.r0r2e3c5t5t rsi,p wahti2c.h0 2m3e5a5nss, which
thmaet aonnslyt h0.a0t1o6n05ly s 0w.0a1s6 r0e5qusirwedas (0re.9q6u3i cryedcle()0 .f9ro6m3 c tyhcel eti)mfreo omf ftahueltt iinmceepotfiofna.u lt inception.
(a)
(b)
FFigiguurer e191.9 O. nOe noef tohfe twheorwsto crasstesc ainse zsoinne-z1o wneh-e1rew thhee rLe-Gth feauLl-tG is fsaiumlut liastesdim atu 7la5t%ed ofa tth7e5 l%ineo aftt he line
2.0075 s. (a) Measured voltage, current at relay terminal and calculated apparent impedance; (b)
at 2.0075 s. (a) Measured voltage, current at relay terminal and calculated apparent impedance;
timing of different stages of the proposed scheme.
(b) timing of different stages of the proposed scheme.
Besides, the detection time is evaluated for other simulated faults occurring during
capacitive TCSC cases and under high resistance faults of 200 Ω (demonstrated in Figures
11c and 12c). It is found that all these faults are detected within less than one cycle from
fault inception (about 0.75 cycle).
It is worth mentioning that this detection time is estimated for simulated cases but in
real cases it may be longer. In fact, the fault detection time was affected by the Transducer
delay that is used for voltage and current measurements, the Processing time that is re-
quired for converting measured data into phasor information using DFT, and the Commu-
nication delay that depends on the type of commination links as well as, the physical dis-
tance between the TCSC substation and relay. Therefore, for the locality of TCSC in the
opposite end of the relay, the fault detection time may be affected by the communication
latency. However, due the significant and continuous development of communication

## PDF page 20

Energies 2021, 14, 7074 20 of 23
Besides, the detection time is evaluated for other simulated faults occurring dur-
ing capacitive TCSC cases and under high resistance faults of 200 Ω (demonstrated in
Figures 11c and 12c). It is found that all these faults are detected within less than one cycle
from fault inception (about 0.75 cycle).
It is worth mentioning that this detection time is estimated for simulated cases but in
real cases it may be longer. In fact, the fault detection time was affected by the Transducer
delay that is used for voltage and current measurements, the Processing time that is required
for converting measured data into phasor information using DFT, and the Communication
delay that depends on the type of commination links as well as, the physical distance
between the TCSC substation and relay. Therefore, for the locality of TCSC in the opposite
end of the relay, the fault detection time may be affected by the communication latency.
However, due the significant and continuous development of communication applications
with high data rates, the 4G wireless broadband becomes 10 times faster than 3G, which
helps in achieving reliable and fast protection schemes as the 4G latency is estimated
as 50 ms [32]. In the near future, 5G will provide a maximal platform for different grid
applications including ultra time-critical applications such as protection schemes [33].
Regarding the comparative study with other published techniques, it is worth men-
tioning that only the scheme introduced in [10] is faster than the proposed scheme but is so
under less fault-resistance coverage. Moreover, the scheme in [10] does not consider the
homogeneity system concerns that may affect the accuracy of its results in such cases.
5.2. Fault Resistance Coverage
According to the obtained results, the large coverage of the trip boundary of the
proposed method due to the fault resistance can be clearly observed. This significant
advantage is due to the development of the modified Takagi method that helps in estimating
the fault zone. Therefore, the fault resistance border can be updated properly. As is
discussed in the results, the fault resistance can be covered up to 250 Ω in zone-1 and 200
Ω in the back-up zones of protection. Although the optimization method used in [15]
introduces good coverage of the resistive fault up to 200 Ω in zone-1, the method is only
applicable for the first zone and the fault is detected after a relatively long iteration time, as
is habitual for optimization methods.
5.3. Data Acquisition and Computation Technique
As described, the proposed technique basically relies on the local data estimated at
the relay terminal and only two values are received from the TCSC substation which are:
the TCSC fault RMS current, to simply inform whether TCSC is included in the faulted
loop or not, and the firing angle that is used in estimating the TCSC impedance. However,
some reported schemes, such as those in [10] and [15], are designed based upon the local
terminal data but they have some limitations, as discussed in Sections 5.1 and 5.2. In
addition, in [22] and [23], the local data are utilized to reduce zone-1 setting and delayed
zone-2, but [22] did not consider the fault resistance in the evaluation, rather than [23],
which is just suggested based on a poor modelling of TCSC that negatively affects the
accuracy of its results.
5.4. Comprehensive Comparative in Terms of Main Features
Table 2 summarizes the comparative study undertaken to highlight the performance
of the proposed method compared with some other techniques used for quadrilateral relay
settings. Therefore, the salient features of the proposed dynamic quadrilateral characteristic-
based adaptive distance relay can be summarized as follows:
Controllability: the reactive and resistive reach can be controlled separately and indepen-
dently. The reactive reach is changed considering the TCSC reactance effect and the system
homogeneity effect, while the resistance is changed considering the fault resistance effect.

## PDF page 21

Energies 2021, 14, 7074 21 of 23
Reliability, as the selectivity feature is obtained by compensating the undesirable effect of
TCSC and fault resistance. Furthermore, the security is obtained by avoiding mal-operation
for any external faults.
Economy, as there is no need for multi-filtration devices with high level of sampling time
and no synchronized data or excessive communications are required to transmit the data
from the remote end.
Inclusivity, as the proposed method can be generalized and applied for any interconnected
long or short TL.
Ease of application, as the method can be applied on the conventional distance relays by
modifying the existing algorithm.
Table 2. Comparison between the proposed dynamic relay and some other methods.
Fault Resistance
Reference Fault Detection Time Data Acquisition Computation Technique
Coverage
[10] — Up to 98 Ω in zone-1 Two-terminal data Communication added
scheme
Within 0.67 cycles Up to 50 Ω in zone-1
[10] without compensation Up to 20 Ω in zone-2 Local data High level of filtration
[15] Within 1.2 s Up to 200 Ω in zone-1 Local data Optimization
[16] Within 1.2 cycles Up to 80 Ω in zone-1 Two-terminal data Optimization
[20] — Up to 150 Ω in zone-1 Two-terminal data Synchronized data scheme
[22] Within 1 cycle — Local data Reducing zone-1 setting
[23] Within 3 cycles Up to 95 Ω zone-1 Local data Reducing zone-1 setting
Within 0.75 cycles and Up to 250 Ω in zone-1
Proposed 0.963 cycles for the worst Up to 200 Ω in zone-2 Local data Apparent resistance and
Scheme case Up to 100 Ω in zone-3 circuit theorem approach
The symbol “—” refers to information not mentioned.
6. Conclusions
The paper introduces a dynamic quadrilateral characteristic-based adaptive distance
relay for TCSC-compensated TLs. The proposed relay adapts both the reactive reach and
resistive reach independently. The reactive reach is adjusted by identifying the presence of
TCSC in the faulted loop to compensate for its effect. Additionally, the calculation of the
tilt angle is investigated to consider the homogeneity of the system due to the load flow
and TCSC effect during high resistance faults. The resistive reach is modified adaptively in
TCSC TLs by estimating the faulted zone through the modified Takagi method.
In order to validate and generalize the proposed dynamic distance relay, it is exten-
sively tested on two simulated IEEE benchmark networks using Maltab, which are the
IEEE-9 bus and New England IEEE-39 bus, to consider both a small grid with long TLs
and a large network with short TLs. The proposed relay is tested on different locations
to cover three zones of protection, different fault resistance values, and different TCSC
modes of operation. According to the obtained results, it can be deduced that the proposed
scheme has conventional functions under normal fault conditions without any burden
on the relay; in addition, it is capable of detecting high resistance faults during the TCSC
inductive and capacitive modes. Additionally, it can alleviate the negative impact of TCSC
underreach/overreach by adapting the reactive setting. Finally, Controllability, Reliability,
Economy, Inclusivity, and Ease of application are considered the salient features of the
proposed dynamic quadrilateral characteristic-based adaptive distance relay.
However, if the system is subject to transient instability such as unstable power swing,
the proposed method should be modified to also consider power swing tripping and
blocking issues based on faults conditions. In addition, validation through real world data

## PDF page 22

Energies 2021, 14, 7074 22 of 23
will be valuable to ensure the leverage of the proposed scheme. Therefore, these issues will
be studied in future publications.
Author Contributions: Conceptualization, D.K.I., E.A.Z.; methodology, G.M.A.-H. and D.K.I.; soft-
ware, G.M.A.-H.; investigation, G.M.A.-H.; writing—original draft preparation, G.M.A.-H. and D.K.I.;
writing—review and editing, D.K.I., E.A.Z., A.F.Z.; supervision, E.A.Z., A.F.Z. All authors have read
and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.
References
1. Bakshi, U.A.; Bakshi, M.V. Protection and Switchgear; Technical Publications Pune: Maharashtra, India, 2008.
2. Joe, M.; Jackie, P. Application Guidelines for Ground Fault Protection. In Proceedings of the 1998 International Conference
Modern Trends in the Protection Schemes of Electric Power Apparatus and Systems, New Delhi, India, 28–30 October 1998.
3. Sauvik, B.; Paresh, K.N. State-Of-The-Art on The Protection of FACTS Compensated High-Voltage Transmission Lines: A review.
IET CEPRI 2018, 3, 21–30.
4. Mathur, R.M.; Rajiv, K.V. Thyristor-Based FACTS Controllers for Electrical Transmission Systems; John Wiley & Sons: Hoboken, NJ,
USA, 2011.
5. Ahad, K.; Shahram, J.; Hossein, S. Distance Relay Over-Reaching in Presence of TCSC on Next Line Considering MOV Operation.
In Proceedings of the 45th International Universities Power Engineering Conference UPEC2010, Cardiff, UK, 31 August–3
September 2010.
6. Beleed, H.; Johnson, B.K.; Hess, H.L. An Examination of the Impact of D-FACTS on the Dynamic Behavior of Mho and
Quadrilateral Ground Distance Elements. In Proceedings of the 2020 IEEE Power & Energy Society Innovative Smart Grid
Technologies Conference (ISGT), Washington, DC, USA, 17–20 February 2020; pp. 1–5. [CrossRef]
7. Holbach, J.; Vadlamani, V.; Lu, Y. Issues and Solutions in Setting a Quadrilateral Distance Characteristic. In Proceedings of the
2008 61st Annual Conference for Protective Relay Engineers, College Station, TX, USA, 1–3 April 2008; pp. 89–104. [CrossRef]
8. Fernando, C.; Armando, G.; Gabriel, B. Adaptive Phase and Ground Quadrilateral Distance Elements; Schweitzer Engineering
Laboratories, Inc.: Pullman, WA, USA, 2017.
9. Bogdan, K. Settings Considerations for Distance Elements in Line Protection Applications. In Proceedings of the 2021 Texas A&M
Conference for Protective Relay, Presented at the 74th Annual Georgia Tech Protective Relaying Conference, College Station, TX,
USA, 28–30 April 2021.
10. Shateri, H.; Jamali, S. Robustness of communication aided distance relay with Quadrilateral characteristic against inter phase
fault resistance. In Proceedings of the 2010 International Conference on Power System Technology, Hangzhou, China, 24–28
October 2010; pp. 1–8. [CrossRef]
11. Patel, U.J.; Chothani, N.G.; Bhatt, P. Adaptive quadrilateral distance relaying scheme for fault impedance compensation. Electr.
Control. Commun. Eng. 2018, 14, 58–70. [CrossRef]
12. Aneesh, S.; Angel, T.S. Quadrilateral Relay Based Distance Protection Scheme for Transmission Lines under Varying System
Conditions. In Proceedings of the 2015 IEEE International Conference on Technological Advancements in Power & Energy,
Kollam, India, 24–26 June 2015. [CrossRef]
13. Venkatanagaraju, K.; Biswal, M.; Bansal, R. Adaptive distance relay algorithm to detect and discriminate third zone faults from
system stressed conditions. Int. J. Electr. Power Energy Syst. 2021, 125, 106497. [CrossRef]
14. Sorrentino, E.; De Andrade, V. Optimal-Probabilistic Method to Compute the Reach Settings of Distance Relays. IEEE Trans.
Power Deliv. 2011, 26, 1522–1529. [CrossRef]
15. Davydova, N.; Shchetinin, D.; Hug, G.; Davvdova, N. Optimization of First Zone Boundary of Adaptive Distance Protection for
Flexible Transmission Lines. In Proceedings of the 2018 Power Systems Computation Conference (PSCC), Dublin, Ireland, 11–15
June 2018. [CrossRef]
16. Shukla, S.K.; Koley, E.; Ghosh, S. A Novel Approach Based on Line Inequality Concept and Sine–Cosine Algorithm for Estimating
Optimal Reach Setting of Quadrilateral Relays. Arab. J. Sci. Eng. 2020, 45, 1499–1511. [CrossRef]
17. Serna, J.D.J.J.; López-Lezama, J.M. Calculation of Distance Protection Settings in Mutually Coupled Transmission Lines: A
Comparative Analysis. Energies 2019, 12, 1290. [CrossRef]
18. Orosz, T.; Rassõlkin, A.; Kallaste, A.; Arsénio, P.; Pánek, D.; Kaska, J.; Karban, P. Robust Design Optimization and Emerging
Technologies for Electrical Machines: Challenges and Open Problems. Appl. Sci. 2020, 10, 6653. [CrossRef]
19. Srivani, S.; Vittal, K.P. Adaptive distance relaying scheme in series compensated transmission lines. In Proceedings of the 2010
Joint International Conference on Power Electronics, Drives and Energy Systems & 2010 Power India, New Delhi, India, 20–23
December 2010; pp. 1–7.
20. Biswal, M.; Pati, B.B.; Pradhan, A.K. Adaptive distance relay setting for series compensated line. Int. J. Electr. Power Energy Syst.
2013, 52, 198–206. [CrossRef]

## PDF page 23

Energies 2021, 14, 7074 23 of 23
21. Achary, K.S.K.; Raja, P. Adaptive design of distance relay for series compensated transmission line. Energy Procedia 2017, 117,
527–534. [CrossRef]
22. Magagula, X.G.; Nicolae, D.V.; Yusuff, A.A. The performance of distance protection relay on series compensated line under fault
conditions. In Proceedings of the AFRICON 2015, Addis Ababa, Ethiopia, 14–17 September 2015; pp. 1–6. [CrossRef]
23. Paladhi, S.; Pradhan, A.K. Adaptive Zone-1 Setting Following Structural and Operational Changes in Power System. IEEE Trans.
Power Deliv. 2017, 33, 560–569. [CrossRef]
24. Seo, W.-S.; Kang, S.-H.; Yoon, Y.-D.; Yoon, J.-S. A Conventional Distance Protection for Series-Compensated Lines Considering
TCSC Protected by a Metal Oxide Varistor. In Proceedings of the 2019 IEEE 8th International Conference on Advanced Power
System Automation and Protection (APAP), Xi’an, China, 21–24 October 2019.
25. Woo, S.S.; Min, S.K.; Sang, H.K.; Jong, S.Y.; Chang, H.H. An Improved Setting Method of the Distance Protective LEDs for
Series-Compensated Transmission Lines Based on A Case Study Approach. Electr. Power Syst. Res. 2020, 188, 106554.
26. Vyas, B.; Maheshwari, R.P.; Das, B. Protection of series compensated transmission line: Issues and state of art. Electr. Power Syst.
Res. 2014, 107, 93–108. [CrossRef]
27. Ordóñez, C.; Gómez-Expósito, A.; Maza-Ortega, J. Series Compensation of Transmission Systems: A Literature Survey. Energies
2021, 14, 1717. [CrossRef]
28. Ibrahim, D.K.; Abo-Hamad, G.M.; Zahab, E.E.-D.M.A.; Zobaa, A.F. Comprehensive Analysis of the Impact of the TCSC on
Distance Relays in Interconnected Transmission Networks. IEEE Access 2020, 8, 228315–228325. [CrossRef]
29. Das, S.; Santoso, S.; Gaikwad, A.; Patel, M. Impedance-based fault location in transmission networks: Theory and application.
IEEE Access 2014, 2, 537–557. [CrossRef]
30. Abo-Hamad, G.; Ibrahim, D.; Zahab, E.A.; Zobaa, A. Adaptive Mho Distance Protection for Interconnected Transmission Lines
Compensated with Thyristor Controlled Series Capacitor. Energies 2021, 14, 2477. [CrossRef]
31. Sahoo, B.; Samantaray, S.R. System Integrity Protection Scheme for Enhancing Backup Protection of Transmission Lines. IEEE
Syst. J. 2021, 15, 4578–4588. [CrossRef]
32. Eissa, M. Developing wide area phase plane primary protection scheme “WA4PS” for complex smart grid system. Int. J. Electr.
Power Energy Syst. 2018, 99, 203–213. [CrossRef]
33. Hovila, P.; Syväluoma, P.; Kokkoniemi-Tarkkanen, H.; Horsmanheimo, S.; Borenius, S.; Li, Z.; Uusitalo, M. 5G networks enabling
new smart grid protection solutions. In Proceedings of the 25th International Conference on Electricity Distribution: CIRED 2019,
Madrid, Spain, 3–6 June 2019; p. 341.
