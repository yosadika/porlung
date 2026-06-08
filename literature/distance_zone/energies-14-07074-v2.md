energies
Article
Dynamic Quadrilateral Characteristic-Based Distance Relays
for Transmission Lines Equipped with TCSC
GhadaM.Abo-Hamad1 ,DoaaKhalilIbrahim1 ,EssamAboulZahab1 andAhmedF.Zobaa2,*
1 DepartmentofElectricalPowerEngineering,FacultyofEngineering,CairoUniversity,Giza12613,Egypt;
dody_benhamed@yahoo.com(G.M.A.-H.);doaakhalil73@eng.cu.edu.eg(D.K.I.);
zahab0@eng.cu.edu.eg(E.A.Z.)
2 CollegeofEngineering,DesignandPhysicalSciences,BrunelUniversityLondon,UxbridgeUB83PH,UK
* Correspondence:azobaa@ieee.org
Abstract: Atwo-foldadaptivedynamicquadrilateralrelayisdevelopedinthisresearchforpro-
tectingThyristor-ControlledSeriesCompensator(TCSC)-compensatedtransmissionlines(TLs).By
investigatinganewtiltangleandmodifyingtheTakagimethodtorecognizethefaultzoneidentifier,
theproposedrelayadaptsitsreactivereachandresistivereachseparatelyandindependently.The
investigatedtiltangleandidentifiedfaultzoneusetheTCSCreactancetocompensateitseffect
ontheTLparametersandsystemhomogeneity.ExcessivetestsaresimulatedbyMATLABonthe
non-homogenous network, IEEE-9 bus system and further tests are carried out on IEEE-39 bus
systeminordertogeneralizeandvalidatetheefficiencyoftheproposedapproach. Thedesigned
tripboundariesareabletodetectwiderangeofresistivefaultsunderallTCSCmodesofoperations.
Theproposedapproachiseasytoimplementastherenoneedfordatasynchronizationorahigh
(cid:1)(cid:2)(cid:3)(cid:1)(cid:4)(cid:5)(cid:6)(cid:7)(cid:8)(cid:1) levelofcomputationandfiltration.Moreover,theproposedadaptivedynamicrelaycanbeapplied
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:6)(cid:7)
fornon-homogeneitysystemsandshortaswellaslongTLswhichareeitherTCSC-compensatedor
-uncompensatedTLs.
Citation: Abo-Hamad,G.M.;
Ibrahim,D.K.;AboulZahab,E.;
Zobaa,A.F.DynamicQuadrilateral Keywords: distance relay; fault resistance; quadrilateral characteristic; resistance and reactance
Characteristic-BasedDistanceRelays elements;ThyristorControlledSeriesCompensator(TCSC)
forTransmissionLinesEquipped
withTCSC.Energies2021,14,7074.
https://doi.org/10.3390/en14217074
1. Introduction
AcademicEditor:AndreaMariscotti
Thevalueoffaultresistanceinsertedbyshortcircuitshasasignificantimpactonthe
performanceofdistancerelayingdevicesprotectingtransmissionlines(TLs). Therefore,it
Received:29September2021
becomesachallengetochoosetheappropriatecharacteristictocoverallprotectionrequire-
Accepted:25October2021
mentissues. Thereactancerelaysarenotaffectedbythelineresistance,but,unfortunately,
Published:28October2021
thereactancerelayisnon-directionalrelay,anditisimpossibletoaddadirectionalelement
toit,asinsuchcasetherelaywilloperateundernormaloperatingconditionsifthesystem
Publisher’sNote:MDPIstaysneutral
operates at or around a unity power factor. For this purpose, the reactance relay with
withregardtojurisdictionalclaimsin
directionalfeaturesismodifiedintotheMhooradmittancecharacteristic[1]. Althoughthe
publishedmapsandinstitutionalaffil-
MhorelayispreferableintheprotectionofTLs,asithasinherentlydirectionalfeatures,
iations.
itscharacteristicsarestillrestrictedunderhighfaultresistanceconditions. Ontheother
hand,thekeyadvantagesofthequadrilateralrelayarethetripcoverageareaforgrounded
resistive faults and the “reach” of the resistance and reactance elements which can be
independentlycontrolled;however,itisaffectedbythesystemnon-homogeneity[2].
Copyright: © 2021 by the authors.
FACTS (Flexible Alternating Current Transmission System) devices are one of the
Licensee MDPI, Basel, Switzerland.
magicsolutionsinstalledintheelectricalgridtoenhancecontrollabilityofthenetwork.
This article is an open access article
FACTScontrollerscanbecategorizedintoseries-connectedcontrollers,shunt-connected
distributed under the terms and
controllers,series–seriesconnectedcontrollers,andseries–shuntconnectedcontrollers[3].
conditionsoftheCreativeCommons
Seriescompensation(SC)isthemostcommontechniqueusedinTLs,asitnotonlyim-
Attribution(CCBY)license(https://
provessystemtransientstability,controlsvoltageandpowerflow,butalsoincreasespower
creativecommons.org/licenses/by/
4.0/). transferringcapacity,anddecreaseslosses[4]. AThyristor-ControlledSeriesCompensator
Energies2021,14,7074.https://doi.org/10.3390/en14217074 https://www.mdpi.com/journal/energies

Energies2021,14,7074 2of23
(TCSC)providesbettercontroloverfixedSCforaTLpowerflow. However,unfortunately
theintegrationofTCSCinTLaffectsitsprotectionabilitysignificantlyduetotheabrupt
lineparameterschanges. Thiswillleadtodefectsintheapparentimpedancemeasuredby
thedistancerelaysthatcauseoverreaching/underreachingoftherelays.
Theresearchstudiesof[5,6]haveconsideredtheeffectofFACTSaswellasTCSCon
thequadrilateralrelay.In[5],theimpedancemeasuredbytherelayisevaluatedconsidering
TCSCatthenearendoftheTL.Nonetheless,thehomogeneityofthesystem,faulttypes,
faultlocation,andTCSCmodellingarenotconsideredinthisevaluation. Theimpactof
series-distributedFACTSonthetiltanglesettingofthequadrilateralcharacteristicandhow
itmayaffectthecoverageoffaultresistancebyoverreaching/underreachingarediscussed
in[5].
Otherpublishedeffortsin[7–9]havepresentedthefactorsthatshouldbeconsideredin
designingthesettingofthequadrilateralrelaytoeliminatetheerrorsduetofaultconditions.
In[7],theinfluenceofthefaultresistanceandtiltangleonthequadrilateralcharacteristic
equations is presented. The considerations of the phase and ground elements for the
phasecomparatorquadrilateralrelayareproposedin[8]. Theinfluenceofphaseangle
errors on the polarizing signal of zone-1 quadrilateral distance elements is introduced
in [9]. The study demonstrated the reactive reach setting limit for a given maximum
expectedpolarizationphaseanglewhich,beyondtheresistivereach,maylosesecurityfor
resistivefaults.
In[10–12],theresistivereachisadaptedbasedonthemeasuredimpedancebythe
relayandcircuittheoryapproach. Byusingtheimpedancemeasurementsfromtwo-line
ends,thefaultresistanceiscalculatedfromasecondorderequationin[10]. Thevalidation
resultsforthisschemeareobtainedforzone-1onlyso,theresultsforback-upprotection
zones and under communication failure are unclear. A standalone adaptive distance
protectionisalsoproposedin[10], wherethefaultresistanceiscalculatedbytheslope
tracker method considering constant X/R ratio not only for the primary protected line
butalsofortheadjacentline,whichmaybeaninappropriatemethodforinterconnected
TLs. Furthermore,theresultsshowthelimitationoffaultresistancecoverageupto50Ω
inzone-1andupto20Ωforback-upzonesofprotection. Thefourboundarylinesofa
numericalquadrilateralcharacteristicareobtainedin[12]bycomputersimulationunder
different changes in system configuration. However, that study does not describe the
methodologyfollowedtoadaptthereachesofthecharacteristics;moreover,thesimplicity
oftheradialsystemusedinthesimulationmayreducetheaccuracyofresults,especially
astheresultsarelimitedtotheprimaryzoneofprotection. Despiteofthesimplicityofthis
technique,theunfaithfulmodeloftheFACTSdeviceortheapproximatedatainfeedto
therelay,affectedbytheTLparameters,mayintroduceerrorintotheapparentimpedance
calculations.
Thethirdzonesettingofaquadrilateralrelayisadaptedin[13]byusingthevariation
modedecompositionapproachtodecomposethelocalendcurrentsignalintodifferent
modes. The apparent impedance and energy index that are calculated from the signal
extractedfromthethirdmodeareusedtodetectthethirdzone’ssymmetricalandasym-
metricalfaults. Generally,themulti-filteringtechniquesareperformedwithhighsampling
ratesandtheextracalculationburdenontherelayissignificant.
Furthermore,theconstructionoftrippingboundariesoftheadaptivequadrilateral
relaybytheoptimizationtechniqueisdevelopedin[14–17].Byconsideringtheprobabilistic
behaviouroftherandomvariablesthataffecttheapparentimpedanceseenbytherelays,
optimal settings of quadrilateral relay zones are developed in [14]. Unfortunately, this
approachwillbeaffectedbytheselectedweightusedfortheconstraintsthatmayincrease
thereachofprotectionzonesorlossofselectivity. Constructingtheboundaryofthefirst
distanceprotectionzoneforSC-TLwithanoptimization-basedalgorithmisintroduced
in[15]. Thereachoftheprotectionzonecanbemaximizedbysolvinganumberofscaled
optimizationproblemsinordertoconstructatrippingboundary. Forthatalgorithm,the
selectiveweightsofthefaultresistanceboundsareobtainedfromthehistoricaldataandthe

Energies2021,14,7074 3of23
reactanceofSCisassumedtobeavailablealltime. Additionally,thescaledoptimization
problemsrelyonsomeassumptionssuchasrecognizingthegridparametersthataffect
the algorithm robustness significantly. In [16], a multi-objective optimization problem,
solvedbythesine–cosinealgorithmtoobtainthereachsettingofthequadrilateralrelay,is
proposed. Thelackofthedetailsusedtosettheparametersofthemethodologyaccording
to the application limits of distance protection relays to TLs is a key disadvantage of
thisapproach.
Ageneticalgorithmfordeterminingthereachsettingsofthequadrilateraldistance
protectionelementofmutuallycoupledTLsisalsoillustratedin[17]. Thealgorithmuses
differentfaultysystemconditionsaffectingthemeasuredimpedanceasthevariableinput.
However,thereisnoinformationaboutfaultresistanceestimationandthemethodisonly
simulatedfortheprimaryprotectedzone. Thereisnodoubtthatthehighercomputational
times for the number of iterations and the accuracy of the results that rely on the data
requiredfromthesystemmakethechoiceofoptimizationtechniqueschallenging.
Generally, the application of different nature-inspired metaheuristics is prevalent
indifferentdesignoptimizationmissions. However, alloftheoptimizationalgorithms
are dependent on parameters that are significantly affected by the question of the best
valuesorsettingsandhowtotunetheseparameterstoachievethebestperformance;in
particular,thereisnounifiedmathematicaldefinitionofrobustness.Moreover,theselection
oftheappropriatenature-inspiredmetaheuristicandthebenchmarkingarealsoanopen
challengingproblem,duetothe“nofreelunch”theoremofmathematicaloptimization[18].
Thecommunication-basedschemeisanotherphilosophyusedinprotectiverelaying
tomeettheTLs’requirements,asproposedin[19–21]. Anadaptiverelaysettingalgorithm
foraseries-compensatedlinewithacapacitorprotectedbyMetalOxideVaristors(MOV)
isproposedin[19]. Itcomputestheseenimpedancebyconsideringthelocalandremote
endrelays’activepower, voltageandcurrent. Theseriescompensationmodelandthe
restriction of the fault resistance coverage area to only 10 Ω may weaken the scheme
performance. Anothersolutionforsettingtheadaptivequadrilateralrelay,protectingTL-
possessingseriescapacitorprotectedbyMOV,isdemonstratedin[20]. Theseenimpedance
iscomputedfromthelocalinformationavailableattherelay. Theunknownfaultresistance
value can be compensated by using the superposition principle on the obtained active
powerfrombothendsofTLatthefaultinstant. However,thestudyhasapproximatedthe
SCwiththeMOVmodeloflinearimpedance,whichmayaffecttheaccuracyoftheresults.
Amodifiedtransfertripschemeisdevelopedin[21]toeliminatetheoverreachproblem
facingthedistancerelayunderSCwithoutanyguaranteeofthescheme’seffectiveness
inthecaseoffaultresistanceandcommunicationfailure. Thereisnodoubtthatthecost,
speedandreliabilityofthecommunicationsystemsarevitalfactorsthatmustbeconsidered
beforeimplementingcommunication-basedschemes. Moreover,synchronizeddata-based
schemesoverburdentherelays,andcommunicationfailuremayleadtocompletefailure
ofrelays.
Anothercategoryofadaptiverelaysusestheconceptofreducingthezone-1setting
anddelayingzone-2asperthefaultconditions[22–25].Switchingoffzone-1andincreasing
the zone-2 time to alleviate SC effect of TLs is presented in [22]. An adaptive relay for
SC-TLisalsosuggestedin[23],wherethereachofaninstantaneouszone-1isreducedto
67%ofTLlengthandanotherdelayedzone-1isreconstructedaftertwocyclesfromthe
faultinceptionapproach. ForTCSC-compensatedTL,theideaofreducingthezone-1reach
settinganddelayingzone-2,toimprovetheconventionalrelay,isintroducedin[24,25].
Thevalidationresultsinthelasttwoschemesignorethefaultresistanceeffect. Aboveall,
theintrinsicdemeritsofthisconceptarethedelayedfaultclearancetime,thehigh-speed
TLparameters’estimationrequirement,alongsidetheneedforefficientmodellingofthe
compensateddevice.
Generally,thechronologicaltrendofresearchstudiesobviouslyshowstheincreas-
ing concern of research for more and more improved protection schemes for TCSC-
compensatedTLs. Forthisreason,inthispaper,anadaptivedynamicquadrilateralrelay

Energies2021,14,7074 4of23
compatiblewiththecompensatedTCSCinterconnectedwithTLsisproposed. Themain
objectiveofthisschemeistoadaptthereactiveandresistivereachofthesettingbased
onthecircuittheoryandtheimpedancemeasuredbytherelay. Thequadrilateralcharac-
teristicdynamicallymovesupward/downwardreliantontheTCSCmodeofoperation
and the tilt angle, moving the right side depending on the existence of fault resistance.
TheproposedapproachisextensivelyevaluatedbyusingtheMatlabsimulatorprogram
forTCSC-compensatedinterconnectedTLsystemsunderhighfaultresistanceinboththe
inductiveandcapacitiveTCSCmodesofoperation. Forthepurposeofgeneralizingthe
methodology,thetestsareappliedonnon-homogeneousTLsystems,whicharelongTLsof
theIEEE-9bussystemandrepeatedonshortTLsoftheIEEE-39busnetwork. Additionally,
theresultsarecomparedwithrespecttothelatestresearchstudies.
Therefore,thecontributionofthispapercanbesummarizedasfollows:
(cid:110) Anadaptivedynamicquadrilateraldistancerelayisproposedtoaccuratelydetectthe
highresistivefaultsunderTCSC-compensatedTLs.
(cid:110) AnewtiltangleestimationisinvestigatedwhichusesTCSCreactancetocompensate
forthenon-homogeneityeffectduetothepresenceofTCSCinthefaultedloop.
(cid:110) TheproposedmethodappliesthemodifiedTakagimethodtoproposethefaultzone
identified,whichisusedtoadapttheresistivereach.
(cid:110) TheadaptationoftherelaysettingreachesforTCSC-compensatedTLsisbasedonthe
localdataestimatedattherelayterminalandtwovaluesofRMScurrentandfiring
angletransmittedfromtheTCSCsubstation,uponafault-startingrecognitionsignal
occurring.
(cid:110) Finally,theproposedapproachiseasilyimplementedasitcanbeappliedbymodify-
ingtheconventionalrelayalgorithmwithoutanyhighleveloffiltrationsorexcessive
computationaltools.
Theremainderofthepaperisarrangedasfollows: inSection2,theTCSCeffecton
thedistancerelay,andthepracticalmodellingofitsimpedancearebrieflypresented. The
proposedmethodologyisfullydescribedinSection3. Theschemevalidationandachieved
resultsonbothIEEE-testedsystemsareillustratedindetailinSection4. Thediscussionof
theadvantagesoftheproposedadaptiverelaycomparedwithotherrelaysandconclusions
aresummarizedinSections5and6,respectively.
2. Thyristor-ControlledSeriesCompensator(TCSC)
Asisknown,TCSCprovidesbettercontroloverTLpowerflowthanfixedSC,sothe
paperwillfocusonidentifyingandmitigatingtheeffectofTCSConTLdistanceprotection.
TheTCSCcharacteristicanditsoperationalmodeareverywellexplainedin[26,27].
Forfaultyconditions,TCSCcontrollersystemreactsrapidlytotakepreventivemeasures
andTCSCoperatesunderdifferentmodesdependingonthefaulttype. Fordifferentfault
scenarios,Table1summarizestheprotectionperformanceunderdifferentTCSCoperation
modes[28].
Table1.DistancerelaysperformanceforTCSC-compensatedTLsunderfaultyconditions.
TCSCMode FaultConditions DistanceRelayBehaviour
Bypassmode Excessivehighfaultcurrent Underreach
Circuitbreakerbypass Thefaultisnotclearedintheinstantaneoustrippingzone Slightunderreachinsomecases
CapacitivemodewithoutMOV Highimpedancefault Overreach
CapacitivemodewithMOV Highfaultcurrent Slightoverreach
Blockingmode Transientfault Overreach
WhenafaultoccursclosetoTCSC,thehighfaultcurrentisenoughtoconductthe
MOV.Therefore,theequivalentcapacitivereactanceofTCSCdecreasesduetoMOV.Asa
result,thepossibilityofexperiencingvoltageandcurrentinversionisquitelowduringthe
fault. Inaddition,TCSCcouldbechangedfromthecapacitivemodeintothebypassmode

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
Energies2021,14,7074 5of23
firing angle (𝛼) in order to apply different TCSC operating modes.
- For a simulated fault in zone-2 (at 85% of the protected line) and due to the TCSC
impedance, thifet hreelvaeyry ohvigehrfraeualtchcuersr eantnfldo wdsetthercotusg thhTeC SfaCutlot pirnev zenotndea-m1 aigne obfoththe MbOloVckanindgse ries
mode (α = 90°)c aapnadcit coar.pInacthitisivmeo mdeo,tdhee T(αC S=C 7i5m°p)e. danceisapureinductance. Therefore,theinversion
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
Figure1introducestheerrorsduetopresenceofTCSCinthefaultloopfordifferent
due to the TCSC impedance, the relay underreaches and detects the fault in zone-2
modesofoperationsbysimulatinganL-Gfaultatthe2stimepointandchangingthefiring
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
Figure 1. FTighuer ea1p.pTahreeanptp iamrepnteidmapnecdea nucneduenrd eLr-LG-G fafauullttss aatt 22 ssf oforrd idffiefrfeenrteTnCt STCCoSpCer aotpioenrmatoidoens .modes.
In this study, -TCSFCo rimaspimedualantecde fa(u𝑋ltinz)o nme-o2d(aetll8i5n%g oisf tahpepplrioetdec theedrlein ae)ccaonrdddiunegt otot htehTe CSC
𝑇𝐶𝑆𝐶
impedance, the relay overreaches and detects the fault in zone-1 in both blocking
practical design values, and the equivalent impedance will be the function of line imped-
mode(α=90◦)andcapacitivemode(α=75◦).
ance (𝑍 ) and the compensation factor (𝜓), as described in [28]:
𝐿 - Ontheotherhand,forasimulatedfaultinzone-1(at75%oftheprotectedline)and
duetotheTC𝑋SCimped=an𝜓c.e𝑍,th erelayunderreachesanddetectsthefaultin(1z)o ne-2in
𝑇𝐶𝑆𝐶(𝛼) 𝐿
bothinductivemode(α=25◦)andbypassmode(α=0◦).
3. Proposed Dynamic QInutahdisrsiltuadteyr,aTlC DSCistimanpceed aRnecela(yX TCSC ) modelling is applied here according to
the practical design values, and the equivalent impedance will be the function of line
The main purpose of this article is to apply an accurate and simple solution for the
impedance(Z )andthecompensationfactor(ψ),asdescribedin[28]:
L
problems facing distance quadrilateral relays for TCSC-compensated TLs under high re-
X = ψ.Z (1)
sistance faults. This target can be achieved by introdTCuScCi(nα)g a newL setting approach for both
resistive and reactive reaches of quadrilateral distance relays independently. The dynamic
3. ProposedDynamicQuadrilateralDistanceRelay
updating of both settings will be separately controlled based on the fault resistance occur-
Themainpurposeofthisarticleistoapplyanaccurateandsimplesolutionforthe
rence and including TCSC impedance in the faulted path. The proposed dynamic quadri-
problems facing distance quadrilateral relays for TCSC-compensated TLs under high
lateral trip boundarreys iwstailnlc beefa dueltssc.rTihbiesdta irnge tthcea nfobleloacwhiienvge dsubbysienctrtoioduncsi.n ganewsettingapproachfor
both resistive and reactive reaches of quadrilateral distance relays independently. The
dynamicupdatingofbothsettingswillbeseparatelycontrolledbasedonthefaultresistance
3.1. Preliminary Basic Considerations
occurrenceandincludingTCSCimpedanceinthefaultedpath. Theproposeddynamic
The quadrilateqruaald driliasttearnalcter ipchbaoruancdtaerryiswtiicll bise ndeostc raib setdrainigthhetffoolrlwowairndg scuhbasreactcitoenrsi.stic such
as the Mho distance elements, as the combination of distance elements can create different
3.1. PreliminaryBasicConsiderations
Thequadrilateraldistancecharacteristicisnotastraightforwardcharacteristicsuchas
theMhodistanceelements,asthecombinationofdistanceelementscancreatedifferent
shapesandpolygonalcharacteristics. Thequadrilateralcharacteristicisconstructed,as
showninFigure2,fromthefollowingelements[8]:
• Adirectionalelement;

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
Energies2021,14,7074 6of23
The impedance reach of the protected line (𝑍 ) is determined by the reactance el-
(cid:3019)(cid:3046)(cid:3032)(cid:3047)
ement with the tilt angle (𝛤) declining to consider the power flow conditions during re-
shapes and polygonal characteristics. The quadrilateral characteristic is constructed, as
sistive faults. Moreover, the resistive fault coverage is designed by the right resistance
• e sh le o m wAe n nr iet na. cF Ttiah gne uc ree e le e 2lm ,e mfr e oen mnt t w;th h e i f c o h l l l o i w m i i n t g s t e h le e m r e e n v t e s r [ s 8 e ] : f lowing load coverage is the left resistance
• e • lem AAen r di t gi rh aen tcb dtil oi a nn d daeli r reelrec emt s i i o set nnata n; l c e el e e l m em e e n n t t k ; eeps the faults detected in the forward direction only.
•• AAl ereftacbtlainndcee rerleemsisetnatn; ceelement.
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
resistivefaults. Moreover,theresistivefaultcoverageisdesignedbytherightresistance
R
eolef mliennet .rTehaectealenmcee nrtewlehviacnhtl itmoi ttshteh eprreovteercsteefldo zwoinnge.l oTaod ocobvteariang ethise tdheesleirfetdre sriestaacnticvee setting
e(l𝑋eme)n tfaonrd raeadcitraecntcioen ealleemleemnetnst, ktheeep rsetahcetfaanucltes ldinetee csteedttiinngth reefaocrhw a(𝑋rddir)e cstihoanllo nbley .compen-
(cid:3020)(cid:3032)(cid:3047) (cid:3019)(cid:3046)(cid:3032)(cid:3047)
Figure 2. Quadrilateral characteristic trip boundaries.
sated for by TCSC impedance (𝑋 ) as follows:
(cid:3021)(cid:3004)(cid:3020)(cid:3004)((cid:3080))
3.2. AdaptiveReactiveReach
𝑋 = 𝑋 ±𝑋 (2)
3.2. Adaptive Reactive Reach (cid:3020)(cid:3032)(cid:3047) (cid:3019)(cid:3046)(cid:3032)(cid:3047) (cid:3021)(cid:3004)(cid:3020)(cid:3004)((cid:3080))
Prevalentreactivesettingdesignisachievedbyconsideringtheappropriatesettingof
linereP N arce o tva n an - l h ceen o tr m erl o eea g vc e atn n ivt e et i o t s y et th s tei y n s pg t r e od m tees s ci tg a en f d f i e zs c oa t n c t eh h .i e eT vo s e e od n b s bt i ay t i i n v co i t t hn y es i o dd f ee t rs h iinr e eg d r t e hr a ee c a t ac a tpi n vp c er e os p e ert l ti e ai m nteg e s( n eX t t , t i w n)g h ich will
Set
fmoofr orlvienaeec dtraoenawccetnaewnlecamer edrnestl eso,vrta hunept rwteoaa ctrthadens c pberaloistneeecdts eeodtnt i zntohgnere ep.a Tochwo (eoXrb tfaloin)w sth hcaeol lndbdeesiticriooemdn spr eednaucsatriitvneedg sftoehtrteib naygs ymmet-
Rset
Tr(C𝑋icSaCl) pi mfhopar esrdee aaoncrtc aegn(rcXoeu enledmeden) rtesa,ss itsfhoteilvl oreew afsca:tualntcse. Tlion ee nsehttainngce r ethaceh r (e𝑋actan) cseh aplel rbfeo rcmomanpceen -for such
(cid:3020)(cid:3032)(cid:3047) TCSC(α) (cid:3019)(cid:3046)(cid:3032)(cid:3047)
csaotnedd iftoior nbsy, TthCeS Cre iamcptaendcaen ceel e(𝑋ment h)a as st ofo lbloew pso: larized by the fault current (𝐼 ). However,
(cid:3021)(cid:3004)(cid:3020)(cid:3004)((cid:3080)) (cid:3033)
X = X ±X (2)
because the fault loop curren𝑋t(cid:3020) (cid:3032)iSs(cid:3047) e t=no𝑋t(cid:3019) m(cid:3046) R (cid:3032)(cid:3047) see±ats𝑋u(cid:3021)r(cid:3004)aT (cid:3020)b(cid:3004) C (lS (cid:3080)eC ), ( tαh)e current at the relay (𝐼 (cid:3014) ) c(2a)n be used
insteNado no-hf o𝐼m. oAgesn tehitey zseyrsote mans da fnfeecgt athtiev see nsseiqtiuveitnyc oefs t hoec cruearc dtaunec et oel efmauelntts,, wsoh icthh ewyi lal re good
Non-hom(cid:3033)ogeneitysystemsaffectthesensitivityofthereactanceelement,whichwill
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
aasst tiilltta annggllee( Γ(𝛤))[ 8[]8.].
Bus M Bus N
FFoorrT TCCSSCC-c-coommppeennsasateteddT TLLs,st, htehep oploarlaizreizdedn engeagtiavteivsee qsueqenuceencceu rcruernrteinsta ilste areltderteodi nto-
cilnucdluedthe e Z t M hX 1 e
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
TsLataetdt hTeL mati dth-pe ominidt-ispoililnuts tirsa itleludsitnraFteigdu irne F3i.gure 3.
IM 2 If2 F IN 2
Bus M Bus N
Z M1 R (0.5) Z L1 (r-0.5) Z L1 Vf2 (1-r) Z L1 Z N1
Figure 3. Two-source negat X ivTCeSC 1s(αe)quence network.
IM2
If2 F
IN2
FFiigguurree3 3..T Twwoo-s-soouurrcceen neeggaatitvivees seeqquueenncceen neetwtwoorkrk..

Energies2021,14,7074 7of23
Consideringaline-to-ground(L-G)boltedfaultatthereachofzone-1(r)ofaTLwith
Z positivesequencelineimpedance,andwhereZ andZ arethepositivesequence
| L1  |     |     |     |     |     | M1  | N1  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
source impedances at both TL terminals (M and N), the negative sequence of the fault
voltageisthusdescribedasfollows:
|     |     |     | V   | = I N2 | (Z N1 +(1−r)Z | L1  | )   |     |     | (3) |
| --- | --- | --- | --- | ------ | ------------- | --- | --- | --- | --- | --- |
f2
|     |     |     |     | (cid:16) |      |             | (cid:17) |     |     |     |
| --- | --- | --- | --- | -------- | ---- | ----------- | -------- | --- | --- | --- |
|     |     | V   | = I | Z        | +r×Z | ±X          |          |     |     | (4) |
|     |     | f2  | M2  | M1       |      | L1 TCSC1(α) |          |     |     |     |
where“1”denotesapositivesequencewhile“2”denotesanegativesequence.
Knowingthat I = I +I andaccordingtoEquations(3)and(4),thetiltangle
|     |     | f2  | M2  | N2  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(Γ)canbeexpressedby:
|     |        | (cid:18) | (cid:19) |       | +Z   | ±X          |     | +Z  |     |     |
| --- | ------ | -------- | -------- | ----- | ---- | ----------- | --- | --- | --- | --- |
|     |        |          | I f2     |       | Z M1 | L1 TCSC1(α) |     | N1  |     |     |
|     | Γ =arg |          |          | =arg( |      |             |     | )   |     | (5) |
+(1−r)Z
|     |     |     | I M2 |     |     | Z N1 | L1  |     |     |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- |
Notethatthenegativesequenceimpedanceofthesource,lineandTCSCaresimilar
tothecorrespondingpositivesequenceimpedancevalues.
3.3. AdaptiveResistiveReach
Theresponsibilityoftherightresistanceelementinaquadrilateraldistancerelayis
thefaultresistancecoverage. Thiscomponentofthequadrilateraldistancerelaywillbe
dynamicallyaccommodatedintheproposedschemetodetectfaultresistanceasmuchas
possible,ontheconditionthat:
(cid:110) It is inherently immune in terms of selectivity, in order to operate for faults in an
appropriatedesirablezone;
(cid:110) It is inherently immune in terms of security, in order to avoid mal-operation for
externalfaultsorloadencroachmentscenarios.
ToperformadaptivelyresistivereachsettingforeachselectiveprotectedzoneforTLs
possessingTCSCcompensation,asetofequationsisappliedbasedonapparentimpedance
calculated by the relay and circuit theory approach. An adaptive resistive blinder for
groundelementsisobtainedbydefiningthefaultresistanceborder(R )andtheshifting
fset
resistive line setting reach (R ) with an R value set by the positive sequence line
|                  |     |     | Rset |     | fset |     |     |     |     |     |
| ---------------- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- |
| impedanceangle(θ |     | ).  |      |     |      |     |     |     |     |     |
L
Toperformthefaultzoneidentifiersubroutine,themodifiedTakagiprinciplewillac-
commodateforTCSC-compensatedTLs. Themodifiedmethodthatusesthezero-sequence
relay current (I ), instead of the superposition current used in the Takagi method to
M0
discriminate between ground and phase faults and to consider system loading during
groundedfaults[29],isdevelopedtoincludetheTCSCimpedanceeffect. Inaddition,for
non-homogeneoussystemcorrection,theinvestigatedtiltanglewillbeconsideredforfault
zoneidentifier(a ),whereV isthevoltageatterminal M thatisequivalenttotherelay
|     | Z   |     | M   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
voltageas:
|     |     |      |          | (cid:0)  | ×(3      | )∗×e−jΓ(cid:1) |          |     |     |     |
| --- | --- | ---- | -------- | -------- | -------- | -------------- | -------- | --- | --- | --- |
|     |     |      |          | Imag V   | M        | I M0           |          |     |     |     |
|     | a = |      |          |          |          |                |          |     |     | (6) |
|     | Z   |      | (cid:16) |          | (cid:17) |                | )∗×e−jΓ) |     |     |     |
|     |     | Imag | (Z       | ±X       |          | ×I ×(3         | I        |     |     |     |
|     |     |      | L1       | TCSC1(α) |          | M              | M0       |     |     |     |
wherea ≤0.8forfaultsinzone-1,a ≤1.2forfaultsinzone-2,andfinallya ≤2.0for
| Z   |     |     |     | Z   |     |     |     |     | Z   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
faultsinzone-3.
Theadaptivegroundelementreachsetting(R )canbedesignatedbythefollowing
Set
equation,andisbasedonR thatiscalculatedafterthefaultedzoneisidentified,where
fset
Z istheimpedanceseenbythedistancerelay,
app
|     |     |     |        | R =    | R       | +R      |     |     |     | (7) |
| --- | --- | --- | ------ | ------ | ------- | ------- | --- | --- | --- | --- |
|     |     |     |        | Set    | Rset    | fset    |     |     |     |     |
|     |     |     |        |        | (cid:0) | (cid:1) |     |     |     |     |
|     |     |     | R fset | = Real | Z app   | −R Rset |     |     |     | (8) |

Energies2021,14,7074 8of23
It is important to notice that the adaptive setting reach for phase elements can be
Energies 2021, 14, x FOR PEER REVIEaWc hievedbyshiftingtheresistivelinereachsetting(R )fromzerototheθ angle(po8s iotfi v2e3
Rset L

sequencelineimpedanceangle),asthethreephaseelementsarenotaccountableforany
faultresistancecoverage.
Theflowchart,displayedinFigure4,showstheequationflowoftheresistivereach
The flowchart, displayed in Figure 4, shows the equation flow of the resistive reach
settingadaptationforthegrounddistanceelements.
setting adaptation for the ground distance elements.
Start
Fault Starting Recognition
Using Zone-4
Fault Zone Identification (aZ)
Using Equation (6)
|     |     |     |     |     |     |     | No If  (aZ) >  Threshold |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- |
Yes
|     |                 | Faults in Zone-3 |     |                 | Faults in Zone-2 |     |     |                 | Faults in Zone-1 |     |
| --- | --------------- | ---------------- | --- | --------------- | ---------------- | --- | --- | --------------- | ---------------- | --- |
| No  | If  (aZ) ≤  2.0 |                  |     | If  (aZ) ≤  1.2 |                  |     |     | If  (aZ) ≤  0.8 |                  |     |
|     |                 |                  | No  |                 |                  |     | No  |                 |                  |     |
|     | Yes             |                  |     | Yes             |                  |     |     | Yes             |                  |     |
Yes
If  Real (Zapp) ≤ Real  Yes If  Real (Zapp)  Yes If  Real (Zapp)
|     | (Zset_3) |     |     | ≤ Real (Zset_2) |     |     |     | ≤ Real (Zset_1) |     |     |
| --- | -------- | --- | --- | --------------- | --- | --- | --- | --------------- | --- | --- |
|     | No       |     |     | No              |     |     |     | No              |     |     |
K e e p   C o n v e n t io n a l   K e e p   C o n v e n t io n a l   K e e p   C o n v e n t io n a l
Rfset_3 = R e a l  ( Z a pp) – Real  Rfset_2 = R e a l  ( Z a pp) – Real  Rfset_1 = R e a l  ( Z a pp) – Real
(Z s e t _ 3 ) R e s i s ti v e   R e a c h  o f   (Z s e t _ 2 ) R e s i s ti v e   R e a c h  o f   (Z s e t _ 1 ) R e s i s ti v e   R e a c h  o f
|     |     | T r i p  B o u n d a r y |     |     | T r i p |  B o u n d a r y |     |     | T r i p  B o u n d a r y |     |
| --- | --- | ------------------------ | --- | --- | ------- | ---------------- | --- | --- | ------------------------ | --- |
Updating  Resistive  Reach  of  Trip  Updating  Resistive  Reach  of  Trip  Updating  Resistive  Reach  of  Trip
Boundary for Last Zone of Protection to
|     |     |     | Boundary  | for  Following  | Zones  of  |     | Boundary for ALL Zones of Protection to  |     |     |     |
| --- | --- | --- | --------- | --------------- | ---------- | --- | ---------------------------------------- | --- | --- | --- |
Fault Resistance Limit Protection to Fault Resistance Limit Fault Resistance Limit
| Rset_1 = 0 |     |     | Rset_1 = 0 |     |     |     | Rset_1 = Real (Zset_1) + Rfset_1 |     |     |     |
| ---------- | --- | --- | ---------- | --- | --- | --- | -------------------------------- | --- | --- | --- |
Rset_2 = 0 Rset_2 = Real (Zset_2) + Rfset_2 Rset_2 = Real (Zset_2) + Rfset_2
Rset_3 = Real (Zset_3) + Rfset_3 Rset_3 = Real (Zset_3) + Rfset_3 Rset_3 = Real (Zset_3) + Rfset_3

Figure 4. Proposed approach for adaptive resistive reaches for ground elements, Numbers 1, 2, or 3 denote zones-1,-2, or
Figure4.Proposedapproachforadaptiveresistivereachesforgroundelements,Numbers1,2,or3denotezones-1,-2,or-3,
-3, respectively.
respectively.
3.4. General Procedures of the Proposed Scheme
3.4. GeneralProceduresoftheProposedScheme
To reduce the burden issues on the distance relay, the proposed dynamic quadrilat- Toreducetheburdenissuesonthedistancerelay,theproposeddynamicquadrilateral
eral relay adapts its reactive and resistive reaches upon receiving a signal from the fault
relayadaptsitsreactiveandresistivereachesuponreceivingasignalfromthefaultstarting
starting recognition subroutine.   recognitionsubroutine.
The fault starting recognition can be identified by developing zone-4, which has large
The fault starting recognition can be identified by developing zone-4, which has
quadrilateral boundaries. Its resistive reach relies on the minimum load resistance equiv- largequadrilateralboundaries. Itsresistivereachreliesontheminimumloadresistance
aelqeunitv taol etnhtet omtahxeimmuamxi mpuowmepr otwraenrsfterar ncsafperabcialpitayb tirliatnystmrainttsemd ivttiead thveia pthroetepcrtoetde,c tceodm,cpoemn--
spaetnedsa tTedL T ( L 𝑃 (cid:3040)((cid:3028)P(cid:3051)m )   u)nudnedr emr maxaimximumu mcocmompepnesnastaiotino ndduurirnign gththee TTCCSSCC ccaappaacciittiivvee mmooddee
a x
((𝑋X(cid:3021)T(cid:3004)C(cid:3020)S(cid:3004)C(cid:3040)m(cid:3028)(cid:3051)ax_(cid:3030)_(cid:3028)c(cid:3043)ap
).) .
|     |     |     |     |                                     | 𝑉 (cid:3014) V ×       |   𝑉 ×(cid:3015) V                                                                            |                    |                                                                        |             |         |
| --- | --- | --- | --- | ----------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------- | ------------------ | ---------------------------------------------------------------------- | ----------- | ------- |
|     |     |     |     | 𝑃 =                                 |  =                     | M N                                                                                          | s in (s𝛿in−(cid:0) | δ𝛼−(cid:2923)(cid:2911)α(cid:2934) m_(cid:3030)a(cid:3028)x(cid:3043)_ | )   (cid:1) |         |
|     |     |     |     | (cid:3040)P(cid:3028)m(cid:3051)a x | 𝑍 (cid:3013)Z− 𝑋−      |                                                                                              |                    |                                                                        | c ap        | ((99))  |
|     |     |     |     |                                     | (cid:3021) (cid:3004)X | (cid:3020)T(cid:3004) (cid:3040) S(cid:3028)C (cid:3051)_m (cid:3030)(cid:3028)ax(cid:3043)_ |                    |                                                                        |             |         |
|     |     |     |     |                                     | L                      | C                                                                                            | ca p               |                                                                        |             |         |
wwhheerree 𝑉V(cid:3015)N  aanndd 𝛿δ aarree tthhee rreecceeiivviinngg eenndd vvoollttaaggee ssoouurrccee aanndd llooaadd aannggllee,, rreessppeeccttiivveellyy,, aanndd
𝛼α(cid:2923)m(cid:2911)a(cid:2934)x __(cid:3030)c(cid:3028)a(cid:3043)p  iiss tthhee fifirriinngg aannggllee uunnddeerr mmaaxxiimmuumm ccoommppeennssaattiioonn ffoorr tthhee ccaappaacciittiivvee mmooddee..
TThhuuss,, tthhee rreeaaccttiivvee rreeaacchh ooff zzoonnee--44 ((X𝑋
4(cid:2872)))c caannb beed deeteterrmminineeddf rforommt htheem maxaixmimuumme xepxepcetca--
ttaiotinonof otfh tehree arecaticvteivree arcehacthh athtacat ncaonc coucrcudru driunrginthge thTeC TSCCSinCd iuncdtiuvcetimveo dmeo(dXe  ( 𝑋 S(cid:3021)C(cid:3004)m(cid:3020)(cid:3004)ax(cid:3040)_(cid:3028)in(cid:3051)d_(cid:3036))(cid:3041),(cid:3031)a)s,
T C
as
|     |     |     |     |     | 𝑋 X= =𝐼𝑚I𝑎m𝑔a(g 𝑍( | Z) +)+𝑋      | X (cid:3004)(cid:3020)T(cid:3004)C(cid:3040)S(cid:3028)C(cid:3051)m_(cid:3036)(cid:3041)ax(cid:3031)_ ind |     |     | ( 1 0 )   |
| --- | --- | --- | --- | --- | ------------------ | ------------ | --------------------------------------------------------------------------------------------------------- | --- | --- | --------- |
|     |     |     |     |     | (cid:2872) 4       | (cid:3013) L | (cid:3021)                                                                                                |     |     | ( 1 0 )   |
The general procedures of the proposed scheme are briefly summarized in Figure 5,
where:

Two separate subroutines (based on Sections 3.2 and 3.3) will be in progress to set
both  the  reactive  and  resistive  reaches  of  the  quadrilateral  distance  relay

Energies2021,14,7074 9of23
Energies 2021, 14, x FOR PEER REVIEW ThegeneralproceduresoftheproposedschemearebrieflysummarizedinFigu9 roef 52,3
where:
(cid:110) Twoseparatesubroutines(basedonSections3.2and3.3)willbeinprogresstosetboth
tihnedreepaecntidveenatnlyd arse ssoisotinv easr eaa lcahuenscohfinthge sqigunaadlr iisla itneirtaialtdeids tfarnocme rtehlea yfaiunldt esptaerntidnegn rtleycoags-
snoiotinona sstaalgaeu. nchingsignalisinitiatedfromthefaultstartingrecognitionstage.
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
Figure5.Generalproceduresoftheproposedscheme.
TThhisis pprrooppoosseedd qquuaaddrriillaatteerraall cchhaarraaccteterirsitsitci crerlealya yapapprporaocahc chanca bne bapepalpiepdl ifeodr afnory nanoyn-
nhoonm-hoogmenoegoeunse osyusstseyms t(eams w(aisll wbeil lshboewshno lwatnerl ainte trhien ttehsetetde sstyesdtesmysst)e,m ass )w,aesll wase lTlCasSCT-CcSoCm--
cpoemnpsaetnesda tTeLdsT uLnsduenr dheigrhh ifgahulfta ruelstisrteasnisctea.n Tche.e Tschheesmche eims seeiqsuseenqtuiaeln; ttihaul;st, hauftse,ra tfhteer ftahuelt
fastualrttsintagr triencgorgenciotigonni tiiso nacihsiaecvheide,v tewd,ot sweopasreaptaer sautebsruoubrtionuetsin wesilwl pilrlopcreoecde etod utopduaptdea bteotbho tthhe
trheearcetiavcet iavneda nredsirsetsiivset isveettsientgtisn fgosr feoarceha zchonzeo. nTeh.uTsh, uths,et sheettsientgtisn ogfs zoofnzeo-n1 eo-f1 tohfet hreelareyl aayre
computed first, followed by the settings of zone-2, and then the settings of zone-3 are de-
termined.

Energies 2021, 14, x FOR PEER REVIEW 10 of 23
Energies2021,14,7074 This approach will be applied independently for both Ground and P10haofs2e3 distance re-
lay elements; the only difference between them is that the adaptation of the resistive reach
in the phase element can be achieved by shifting the resistive line reach setting (𝑅 ) by
(cid:3019)(cid:3046)(cid:3032)(cid:3047)
cahreacnogminpgu ttehdefi r sbt,yf othlloew veadlubey othfe psoesttiitnivgse osfezqouneen-2c,ea nlidneth iemnptheedsaenttcineg asnogflzeo n(𝜃e-3).a re
(cid:3013)
determined.
ThisapproachwillbeappliedindependentlyforbothGroundandPhasedistancerelay
4. Proposed Scheme Validation
elements; theonlydifferencebetweenthemisthattheadaptationoftheresistivereach
4in.1t.h Teepshteadse Seylesmtemenst canbeachievedbyshiftingtheresistivelinereachsetting(R )by
Rset
changingthebythevalueofpositivesequencelineimpedanceangle(θ ).
The investigated methodology is tested on several faultyL cases generated on TCSC-
c4o. PmroppeonsseadteSdch TeLmse tVharloiduagtiho nthe Matlab simulation program by varying the fault locations,
T4.C1.STCes tmedoSdyest, eamnsd fault resistance value on an IEEE-9 bus small power system network that
has lTohnegi nTvLesst.i gFauterdthmeremthoodreo,l otghye istetsetsste adroen rseepveearateldfa uolnty acnas eIsEgEeEn e3r9a-tebduso nsyTsCtSeCm-, as a large
ncoemtwpoenrska tseydstTeLms twhriotuhg shhtohretM TaLtsla, bins iomrudlearti oton vpraolgidraamte baynvda rgyeinngertahleizfaeu tlhtelo pcartoiopnoss,ed scheme.
TCSCImt modues,ta nbde fpaoulitnrteesdis toaunct ethvaaltu, eino neaacnhIE oEfE t-h9eb utwssom sailmlpuolwateerds ynsetetmwonertkws,o rthketh naettwork lines
haslongTLs. Furthermore, thetestsarerepeatedonanIEEE39-bussystem, asalarge
have different line parameters that significantly affect system homogeneity, in addition to
networksystemwithshortTLs,inordertovalidateandgeneralizetheproposedscheme.
the fact that the TCSC impedance will affect the protected line parameters, which have
Itmustbepointedoutthat,ineachofthetwosimulatednetworks,thenetworklines
been carefully considered in the adaptive proposed scheme.
havedifferentlineparametersthatsignificantlyaffectsystemhomogeneity,inadditionto
thefactthattheTCSCimpedancewillaffecttheprotectedlineparameters,whichhave
4b.e2e.n Rceasrueflutsll yofc tohnes iIdEeEreEd-9in Btuhes aSdyasptetmive proposedscheme.
As described in [30], this 60 Hz test system consists of three machines connected to a
4.2. ResultsoftheIEEE-9BusSystem
ring system of nine buses operating at 230 kV through step up transformers of 13.8 kV/230
As described in [30], this 60 Hz test system consists of three machines connected
kV. Each line section is 100 km in length. The loads are added at three locations at different
to a ring system of nine buses operating at 230 kV through step up transformers of
b13u.8seksV. T/C23S0Ck iVs. cEoanchnelcinteeds,e actsi osnhoisw1n0 0ink mFiginurlee n6g, taht. thTeh emlioda-dpsoairnet aodf dthede laitnteh breeetween buses
9lo caantido n6s wathdiilfefe rtehnet bpursoeps.oTseCdS Cdiessciognnneedc terdel,aays sihso lwoncaitneFdi gautr eb6u,sa t9t.h Tehmei dp-rpootiencttoefd zones are
thelinebetweenbuses9and6whiletheproposeddesignedrelayislocatedatbus9. The
sequentially considered at 80% of the protected line for zone-1, while zone-2 and zone-3
protectedzonesaresequentiallyconsideredat80%oftheprotectedlineforzone-1,while
are extended to 100% of the same line and 20% of the adjacent line, and 100% of the same
zone-2andzone-3areextendedto100%ofthesamelineand20%oftheadjacentline,and
protected line and 100% adjacent line, respectively.
100%ofthesameprotectedlineand100%adjacentline,respectively.
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
Figure6.IEEE-9bussystemequippedwithTCSC.

Energies2021,14,7074 11of23
Energies 2021, 14, x FOR PEER REVIEW 11 of 23
Theevaluationdividesthetestsintofivecategoriestoassessthedifferentfaultscenar-
iosandevaluatethedependabilityofeachdesignsettingcomparedwiththeconventional
▪ Aqudaadpritliavteer arlesseitsttinivge. setting for faults before TCSC;
▪ Adaptive resistive setting for faults after TCSC;
(cid:110) BoltedfaultswithoutTCSC;
▪ E(cid:110)valuAadtainptgiv tehree apctriovpeosestetidng swchheilmeTeC aStC thisei ntcwluod eednadnsd owf iTthLo.u tfaultresistance;
(cid:110) AdaptiveresistivesettingforfaultsbeforeTCSC;
4.2.1. (cid:110)Bolt A ed d a F p a ti u v l e ts re w sis i t t i h ve ou se t t t T in C g S fo C r f aultsafterTCSC;
(cid:110) EvaluatingtheproposedschemeatthetwoendsofTL.
For selectivity and effectiveness issues, the proposed scheme is evaluated under
bolted4. 2g.1r.oBuonltded faFauullttss awliothnogu tTTLC SaCt different fault locations for instantaneous and back-up
zones of pFroortseelcetcitoivnit ywainthdoefufetc TtivCeSnCes.s i ssues,theproposedschemeisevaluatedunderbolted
groundfaultsalongTLatdifferentfaultlocationsforinstantaneousandback-upzonesof
The trajectory impedances of the proposed scheme (the solid black characteristic) and
protectionwithoutTCSC.
the conventional relay (the dashed red characteristic) are addressed in Figure 7 for the
The trajectory impedances of the proposed scheme (the solid black characteristic)
boltedan Ld-Gth efacounltv eant t2io.n0a2l5r esl auyn(dtheer ddaisfhfeerdernetd lcohcaartaicotenrsis otinc) TarLe taod dcroevsseerd ailnl Fthigeu zreo7nefosr of protec-
tion wthiethbooultet dTLC-SGCfa. uAltsa sth2o.0w25ns iunn dthere dfiifgfeurreen,t tlohcea tpiornospoonseTdL tsochcoevmere a(lbl lthaeckz)o nceosinocfides with
protectionwithoutTCSC.Asshowninthefigure,theproposedscheme(black)coincides
the conventional one (red) as there is no need for any adaptive reaches under plain fault
withtheconventionalone(red)asthereisnoneedforanyadaptivereachesunderplain
conditions, which reduces the computational burden of the relay.
faultconditions,whichreducesthecomputationalburdenoftherelay.
(a) (b)
Figure 7. IFmigpuered7a.nImcep etrdaajneccettorrayje cftoorry bfoorltbeodlte Ld-LG-G ffaauullttss aatt2 .202.052s5. (as). F(aau) ltFsabueflotsre btheefomried -tphoein mtoifdth-peopriontte cotefd thlinee ;p(rbo)tfeauctltesd line; (b)
faults aftera ftthere tmheimd-idp-opionint tooff tthhee pprrootetcetcetdeldin lei.ne.
4.2.2. AdaptiveReactiveSettingWhileTCSCIsIncludedandwithoutFaultResistance
4.2.2. Adaptive Reactive Setting While TCSC Is Included and without Fault Resistance
Asdiscussed,theadaptivereactivesettingwillbeonlyappliedinthecasethatTCSC
Aissi ndciluscduedssinedth, ethfaeu lateddalpootipv.eT hreuas,cftoirvbeo slteetdtifnaugl twsbilelf obree ToCnSlyC ,atphepTliCeSdC iind etnhteifi ccaatsieon that TCSC
is inclzuondeeids iinna ctthivea tfeadu,latneddt hloeorepfo. rTehthuesa,d faoprt ibveolstcehdem faeudlotess bneotfoprreoc TeeCdS. ACc, ctohrdei nTgClyS,Cth eidentifica-
settingsofallzonesarematchedwiththeconventionalcharacteristicsettings(dashedred
tion zone is inactivated, and therefore the adaptive scheme does not proceed. Accord-
characteristic)asincase(a)ofFigure7.
ingly, the settings of all zones are matched with the conventional characteristic settings
Toevaluatechangingofthereactivesettingreachadaptively,manycasesofbolted
(dashed red characteristic) as in case (a) of Figure 7.
groundfaultsareappliedafterTCSCunderdifferentTCSCmodesofoperation. Theworst
Tcaos eesvfaolrutahteef ocuhramngodinegs ooffo tpheera rtieoancitnivaell szeotnteinsgar ereaadcdhr eassdeadphteivreefloyr, amssaenssym ceansteosf of bolted
grounthde fsacuheltms ea.re applied after TCSC under different TCSC modes of operation. The worst
cases (cid:110)for tFhoer fcoauparc mitivoedaensd obfl oocpkeinragtTioCnS Cino paellr aztoionne,sth aeraep apdardernetsimsepde dhaenrcee ftorarj eacstosreyssfomrent of the
2L-Gboltedfaultsat85%and125%oftheprotectedlinefromthetestedrelay®is
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

Energies2021,14,7074 12of23
inbothmodesofoperationanddetectszone-2faults(at85%)andzone-3faults(at
125%)incorrectlyaszone-1faults. Meanwhile,theproposedadaptivequadrilateral
distancerelay(thesolidblackcharacteristic)succeededindetectingsuchfaultsin
theircorrespondingzonesofprotectionbyreducingthereactivereachbytheTCSC
Energies 2021, 14, x FOR PEER REVIEW 12 of 23
reactancevalue.
(cid:110) Fortheinductiveandbypassmodes,Figure9demonstratesthetrajectoryimpedance
forthebolted3L-Gfaultperformedat75%and110%oftheprotectedlineneartheend
edgesofzone-1andzone-2,respectively.Asshowninthefigure,theproposedscheme
scheme correctly detected the faults occurring in zone-1 (at 75%) and zone-2 (at 110%)
correctlydetectedthefaultsoccurringinzone-1(at75%)andzone-2(at110%)for
for bobothth mmooddeesso foTfC TSCCSoCpe roaptieonra,wtihoinle, mwahl-iolpee rmataioln-ospocecruartrieodnwsi tohctchuercroendve nwtiiotnha lthe conven-
tionasle stteinttgisntghsa ttehxapte reixenpceertireicnkcyeu tnrdicekrryea uchnindgeirnrebaocthhciansges i.n both cases.
(a) (b)
(c) (d)
Figure 8. ImFipguedrea8n.cIme ptreadjaenccteotrryaj efcotor rtyhfeo r2tLhe-G2L f-aGuflatu altta 2t.20.0 ss.. ((aa)) AAtt8 85%5%of othfe tlhinee luinned eurncadpearc ictiavpeamcoidtiev;e(b m)aotd12e5;% (bo)f tahte 125% of the
line under clianpeaucnidteivrcea mpaocidtivee; (mco) daet; 8(c5)%at 8o5f% thoef tlhienlein uenudndeerr bblloocckkininggm modoed;(ed;) (adt)1 2a5t% 1o2f5t%he olifn ethuen dlienreb luocnkdinegrm bolodec.king mode.
(a) (b)

| Energies 2021, 14, x FOR PEER REVIEW  |     |     |     |     |     |     | 12 of 23  |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- |

scheme correctly detected the faults occurring in zone-1 (at 75%) and zone-2 (at 110%)
for both modes of TCSC operation, while mal-operations occurred with the conven-
tional settings that experience tricky underreaching in both cases.
|     |     |      |     |     |      |     |     |     |
| --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
|     |     | (a)  |     |     | (b)  |     |     |     |
|     |     |      |     |     |      |     |     |     |
|     |     | (c)  |     |     | (d)  |     |     |     |
Figure 8E.n Iemrgiepse20d2a1,n1c4,e7 0t7r4ajectory for the 2L-G fault at 2.0 s. (a) At 85% of the line under capacitive mode; (b) a1t3 1o2f523% of the
line under capacitive mode; (c) at 85% of the line under blocking mode; (d) at 125% of the line under blocking mode.
| Energies 2021, 14, x FOR PEER REVIEW  |     |     |     |     |     |     | 13 of 23  |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- |

|     |     |      |     |     |      |     |     |     |
| --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
|     |     | (a)  |     |     | (b)  |     |     |     |
|     |     |      |     |     |      |     |     |     |
|     |     | (c)  |     |     | (d)  |     |     |     |
Figure 9. ImFpiegduraen9c.eIm trpaejdeacntcoertyra fjeocrto trhyefo 3rLth-eG3 Lfa-Gulfta ualtt a2t.02.20525 ss.. ((aa)) aatt7 75%5%of othfe tlhinee luinndee urninddeurct iivnedmuocdtiev;(eb )mato1d1e0%; (bof)t haet 110% of the
line under inlidneuuctnidveer imndoudcteiv; e(cm) oadte 7;(5c%)a to7f5 %thoef ltihneeli nuenudnedre rbbyyppaassssm modoed;e(d; )(dat)1 a10t %11o0f%the olifn tehuen dlienreb yupnadssemr obdyep. ass mode.
|     |     | 4.2.3. | AdaptiveResistiveSettingforFaultsbeforeTCSC |     |     |     |     |     |
| --- | --- | ------ | ------------------------------------------- | --- | --- | --- | --- | --- |
4.2.3. Adaptive Resistive Setting for Faults before TCSC
Forevaluatingtheeffectivenessofupdatedresistivescheme,asetofdifferentresistive
FoL-rG efvaaulltusa(wtiinthg5 t0hΩe, e1f0f0eΩct,i2v0e0nΩe,sasn odf2 5u0pΩdafatueldtr erseissitasnticve)ew secrheeimmpele, ma esnetet doefv deriyfferent resis-
tive L-G faults (with 50 Ω, 100 Ω, 200 Ω, and 250 Ω fault resistance) were implemented  10%oftheprotectedlinebeforeTCSCineitherthecapacitiveorinductivemode.
AsillustratedinFigure10,theconventionalrelay(thedashedredcharacteristic)lost
every  1 0%   o f   t h e  p r o te c t e d   li n e   b e f o r e   T C S CΩ in  e i t h e r   t h e   c a p a c i ti v e  o r  in d u c tive mode.
i ts se le c t i v it y fo r a ll f a u lt s w i t h r e s is t a n c e 5 0 w h i c h o c c u r r e d a t z o n e -1 , an d fa ls e ly
Adse itlelcutesdtrtahteemdi ninz oFnige-u3.reF u1r0th, etrhmeo creo,nthveencotniovnenatli orneallarye l(atyhwe adsausnhaebdle rtoedde ctehcatrtahecteristic) lost
|     |     |     |     | Ω Ω | Ω   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
its selercemtivaiintiyn gfofaru latsllu fnaduerlt1s0 0w i,th20 0re s,isantadn2c5e0  50.O Ωn twhehciocnhtr aorcy,ctuherrperdop aoste zdoscnhee-m1e, (athned falsely de-
solidblackcharacteristic)superiorlyadapteditsresistiveblindertosufficientreachbased
tected them in zone-3. Furthermore, the conventional relay was unable to detect the re-
onthefaultlocationandfaultresistancevalueinallcases. However,TCSCisinsertedin
maining faults under 100 Ω, 200 Ω, and 250 Ω. On the contrary, the proposed scheme (the
TLbut,asthesefaultsarebeforeTCSC,thereactivereachkeptitssettingthesameasthe
solid bcloancvke ncthioanraalcretelaryi.stic) superiorly adapted its resistive blinder to sufficient reach based
on the fault location and fault resistance value in all cases. However, TCSC is inserted in
TL but, as these faults are before TCSC, the reactive reach kept its setting the same as the
conventional relay.
As described before, the fault resistance border (𝑅
𝑓𝑠𝑒𝑡 ) is determined using Equation
(8), and therefore the new updated resistive setting will be directly identified according
to the fault resistance. As shown in Figure 10, when the fault occurs in zone-1 (as an in-
stantaneous protected zone), the trip boundaries of three zones of protection will be adap-
tively changed by updating their resistive reach.
|     |      |     |      |     |      |     |      |     |
| --- | ---- | --- | ---- | --- | ---- | --- | ---- | --- |
|     | (a)  |     | (b)  |     | (c)  |     | (d)  |     |
|     |      |     |      |     |      |     |      |     |
|     |      |     |      |     |      |     |      |     |
|     | (e)  |     | (f)  |     | (g)  |     | (h)  |     |

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
Energies2021,14,7074 14of23
stantaneous protected zone), the trip boundaries of three zones of protection will be adap-
tively changed by updating their resistive reach.
(a) (b) (c) (d)
Energies 2021, 14, x FOR PEER REVIEW 14 of 23
(e) (f) (g) (h)
(i) (j) (k) (l)
(m) (n) (o) (p)
FFigiguurere1 100..I mImppeeddaanncceet rtraajejecctotorryyf oforrt htheeL L-G-Gf afauultlta att2 .20.20255s .s.( a(a))A Att1 01%0%a nanddR 𝑅 f𝑓= =5 050Ω Ω;(;b ()ba) ta1t 01%0%a nadndR
f
𝑅 𝑓= 1=0 100Ω0 Ω;(;c )(ca)t a1t0 %
a 1 n 0 d % R an = d 2 𝑅 0𝑓0 Ω= ; 2 ( 0 d 0 ) Ω at ; ( 1 d 0 ) % at a n 10 d % R an = d 2 𝑅 5𝑓0 Ω= ; 2 ( 5 e 0 ) Ω at ; 2 (e 0 ) % at a n 20 d % R an = d 5 𝑅 0𝑓Ω = ; ( 5 f 0 ) a Ω t ; 2 ( 0 f) % at a n 20 d % R an = d 1 0 𝑅 0𝑓 Ω= ; 1 ( 0 g 0 ) Ω at ; 2 (g 0% ) a a t n 2 d 0% R an = d 2 0 𝑅 0𝑓 Ω;
f f f f f
(h = ) 2 a 0 t 0 2 Ω 0% ; (h a ) n a d t R 20% = a 2 n 5 d 0 Ω𝑅 𝑓; ( = i) 2 a 5 t 0 3 Ω 0% ; (i a ) n a d t 3 R 0% = an 50 d Ω𝑅 𝑓; (j = ) 5 a 0 t Ω 30 ; % (j) a a n t d 30 R % = an 1 d 0 0 𝑅Ω𝑓 ; = ( 1 k 0 ) 0 a Ω t3 ; 0 ( % k) a a n t d 30 R % a = nd 20 𝑅 0𝑓Ω = ; ( 2 l 0 ) 0 a Ω t3 ; 0 (l % ) a a t n d
f f f f
30% and 𝑅 = 250 Ω; (m) at 40% and 𝑅 = 50 Ω; (n) at 40% and 𝑅 = 100 Ω; (o) at 40% and 𝑅 = 200 Ω; (p) at 40% and 𝑅
R =250Ω;𝑓(m)at40%andR =50Ω;𝑓(n)at40%andR =100Ω𝑓;(o)at40%andR =200Ω𝑓;(p)at40%andR =250𝑓Ω.
=f 250 Ω. f f f f
Asdescribedbefore,thefaultresistanceborder(R )isdeterminedusingEquation(8),
fset
4.2.4. Adaptive Resistive Setting for Faults after TCSC
andthereforethenewupdatedresistivesettingwillbedirectlyidentifiedaccordingtothe
faultTrehsei sptaenrfcoer.mAasnscheo owf nthine Fpirgouproes1e0d, wdyhneanmthice qfauualdtroiclacuterrsailn rezloanye -c1an(a bsea ncoinmsptaanrteadn etoo us
pthreo tceocntevdenztoionnea),l trheelatyri wpibthou finxdeadr ciehsaorafcttherreisetizco sneetstinofgsp rboyt eacptpiolyninwgi lal bseeta odf arpestiivsteilvye cfhauanltgs ed
bafyteurp TdCatSiCng utnhdeeirr rtehseis tfiovuer rdeaifcfher.ent modes of operation at different critical locations,
where the conventional relay may lose its selectivity-relaying function by underreach-
4in.2g./4o.vAerdraepactihviengR seisgisntiifviceaSnetltyti ndguefo tro Fthaeu letxsiastfetenrceT CofS TCCSC reactance in the faulted loop.
Figures 11–14 illustrate the correctness of the dynamically updated settings (the solid
Theperformanceoftheproposeddynamicquadrilateralrelaycanbecomparedto
t b h la e ck co c n h v a e ra n c t t i e o r n is a t l ic r ) e f l o a r y L w -G it h fau fi l x ts e d at c 2 h .0 a 2 r 5 a c s t w er i i t s h t ic 𝑅 𝑓s e = t t 5 i 0 n g Ω s , 1 b 0 y 0 a Ω p , p a l n y d in 2 g 00 a Ω se a t t o lo f c r a e ti s o is n t s i ve
85% and 125% under the blocking mode and capacitive TCSC modes, respectively. In ad-
faultsafterTCSCunderthefourdifferentmodesofoperationatdifferentcriticallocations,
dition, the same faults are simulated with similar fault conditions but at 75% and 110% of
where the conventional relay may lose its selectivity-relaying function by underreach-
the line under the inductive and bypass TCSC modes of operation, respectively. On con-
ing/overreachingsignificantlyduetotheexistenceofTCSCreactanceinthefaultedloop.
trary, the conventional fixed characteristic settings (the dashed red characteristic) com-
Figures11–14illustratethecorrectnessofthedynamicallyupdatedsettings(thesolid
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
.0 o
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
110%ofthelineundertheinductiveandbypassTCSCmodesofoperation,respectively.
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

| Energies2021,14,7074 |     |     |     |     |     |     |     |     | 15of23 |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
Oncontrary,theconventionalfixedcharacteristicsettings(thedashedredcharacteristic)
EEEnnneeerrrgggiiieeesss   222000222111,,,   111444,,,   xxx   FFFOOORRR   PPPEEEEEERRR   RRREEEVVVIIIEEEWWW    111555   ooofff   222333
    completelyfailedtodetectsuchfaultsduetoboththeeffectsoffaultresistanceandthe
existenceofTCSCinthefaultloop.
|     |     |              |     |     |     |              |     |              |     |
| --- | --- | ------------ | --- | --- | --- | ------------ | --- | ------------ | --- |
|     |     | (((aaa)))    |     |     |     | (((bbb)))    |     | (((ccc)))    |     |
FFFiiigggFuuuirrrgeeeu   1r11e111...1   A1AA.pppAppppaaaprrreaeenrnnetttn   iiitmmmimppppeeededddaaaannnncccceeee   llllooooccccuuuussss   ffffoooorrrr   tttthhhheeeeL   LLL-G---GGGf  a fffuaaaluuutlllattt t  aaa2ttt.   02222...5000222s555a   tsss 8  aaa5ttt%   8885o55%f%%t  h oooefff   ltitthnhheeee   ullliiinnnndeeee   uruuntnnhdddeeeeTrrr C  ttthShhCeee   TbTTlCCCoScSSkCCCi n  bbbglllooomcccokkkdiiinnneg.gg (  mamm)oooWdddieeet.h..   (((aaa)))
| WWWiiitttRhhhf    𝑅𝑅=𝑅 | 5   0===   Ω555000;   (ΩΩΩb);;;   (w((bbbi)))t   hwwwRiiitttf |              | hhh=   𝑅𝑅𝑅1 0   0=== Ω  1110;000(00c   Ω)ΩΩw;;;   (i((ctcch)))   wwwRi |     | iittth=hh   2𝑅𝑅𝑅0 0   Ω===   2.22000000   ΩΩΩ...    |              |     |              |     |
| ---------------------- | ------------------------------------------------------------- | ------------ | ---------------------------------------------------------------------- | --- | --------------------------------------------------- | ------------ | --- | ------------ | --- |
|                        | 𝑓𝑓𝑓                                                           |              | 𝑓𝑓𝑓                                                                    | f   | 𝑓𝑓𝑓                                                 |              |     |              |     |
|                        |                                                               |              |                                                                        |     |                                                     |              |     |              |     |
|                        |                                                               | (((aaa)))    |                                                                        |     |                                                     | (((bbb)))    |     | (((ccc)))    |     |
FFFiiigggFuuuirrrgeeeu   111re222...1   AAA2.pppApppaaaprrrpeeeannnrttte   iniimmmtpippmeeedddpaeaandnncacceene   cllloeoocccluuouscss u  fffosoorrrf o  ttthrhheeeth   LLLe---GLGG-   Gfffaaauuufallltutt   alaatttt  a 222t...0002222.05552   ss5s   aaasttt a  111t22215552%%%5%   ooofffo   tttfhhhteeeh   lelliiinnnlieeen   ueuunnnudddneeedrrre   trtthhhteeeh   eTTTCTCCCSSSCCCSC   cccaaacpppapaaacacciiictttiiiitvvviveee e  mmmmooooddddeeee...   .(((aaa)))
| WWWiiit(tthahh)   𝑅W𝑅𝑅 |    ΩΩΩ=;;;5   (((0bbbΩ)))   www;(iiibttth)hh w  𝑅𝑅𝑅i𝑓𝑓𝑓 |              | 000=000   1ΩΩΩ0;0;;   (((Ωccc)));   www(ciii)ttthwhh   i𝑅𝑅𝑅th𝑓𝑓𝑓 |     |    222=0000002   0ΩΩΩ0...Ω    |              |     |              |     |
| ---------------------- | ------------------------------------------------------- | ------------ | ---------------------------------------------------------------- | --- | ----------------------------- | ------------ | --- | ------------ | --- |
|                        | 𝑓𝑓𝑓 i   t=h==   55R5000 f                               |              | th   ===R   111 f                                                |     |    R=== f                     | .            |     |              |     |
|                        |                                                         |              |                                                                  |     |                               |              |     |              |     |
|                        |                                                         | (((aaa)))    |                                                                  |     |                               | (((bbb)))    |     | (((ccc)))    |     |
FFFiiigggFuuuirrrgeeeu   1r11e333...1   A3AA.pppAppppaaaprrreaeenrnnetttn   iiitmmmimppppeeededddaaaannnncccceeee   llllooooccccuuuussss   ffffoooorrrr   tttthhhheeeeL   LLL-G---GGGf a  fffuaaaluuutlllattt t  aaa2ttt.   02222...0500222s555a   tsss 7  aaa5ttt%   7775o55%%f%t h  oooefff   lttithnhheeee   ullliiinnnndeeee   uruuntnnhdddeeeeTrrr C  ttthhShCeee   TTTinCCCdSSSuCCCct   iiiivnnnedddmuuucccotttdiiivvve.eee (  mamm)oooWdddieeeth...   (((aaa)))
|                       | Ω                                                                            |     | Ω                                                                                |     | Ω                                     |     |     |     |     |
| --------------------- | ---------------------------------------------------------------------------- | --- | -------------------------------------------------------------------------------- | --- | ------------------------------------- | --- | --- | --- | --- |
| WWWiiitttRhhhf   𝑅𝑅𝑅= | 𝑓𝑓𝑓 5   0===    555000;   (ΩΩΩb);;;   (w((bbbi)))t   hwwwRiiitttfhhh =  𝑅𝑅𝑅1 |     | 𝑓𝑓𝑓 0   0===    111000;0(00c   Ω)ΩΩw;;;   (i((ctcch)))   wwwRifiittth=hh   2𝑅𝑅𝑅0 |     | 𝑓𝑓𝑓 0    ===   2.22000000   ΩΩΩ...    |     |     |     |     |
It is also worth clarifying here that the scenario of the resistive faults with TCSC
includedinthefaultedloopisdifferentfromthecasesforfaultswithoutTCSC.Although
TCSChasonlyinductancebehaviour,butitaffectstheresistivereachunlessitsnegative
impactiscompensatedforbytileangle,asdiscussedinEquation(5)andconsideredinthe
faultzoneidentifierbymodifyingtheTakagimethodinEquation(6)todeterminethefault
resistanceborder. Otherwise,theR termwillbeacomplexvalueandaddsanadditional
f
reactancevaluetothefault. Additionally,iftheproposedadaptivedynamicsettingscheme
onlyadaptstheresistivereachwithoutadaptingthereactivereach,therelaywillfalsely
detecttheresistivefaultduetounderreachoroverreachdependingonTCSCoperational
|     |     |              |     |     |     |              |     |              |     |
| --- | --- | ------------ | --- | --- | --- | ------------ | --- | ------------ | --- |
|     |     | (((aaa)))    |     |     |     | (((bbb)))    |     | (((ccc)))    |     |
FFFiiiggguuurrreee   111444...   AAAppppppaaarrreeennnttt   iiimmmpppeeedddaaannnccceee   lllooocccuuusss   fffooorrr   ttthhheee   LLL---GGG   fffaaauuulllttt   aaattt   222...000222555   sss   aaattt   111111000%%%   ooofff   ttthhheee   llliiinnneee   uuunnndddeeerrr   ttthhheee   TTTCCCSSSCCC   bbbyyypppaaassssss   mmmooodddeee...   (((aaa)))   WWWiiittthhh
𝑅𝑅𝑅 𝑓𝑓𝑓    ===   555000   ΩΩΩ;;;   (((bbb)))   wwwiiittthhh   𝑅𝑅𝑅 𝑓𝑓𝑓    ===   111000000   ΩΩΩ;;;   (((ccc)))   wwwiiittthhh   𝑅𝑅𝑅 𝑓𝑓𝑓    ===   222000000   ΩΩΩ...

| Energies 2021, 14, x FOR PEER REVIEW  |     |     |     |     |     | 15 of 23  |
| ------------------------------------- | --- | --- | --- | --- | --- | --------- |

|     |      |     |      |     |      |     |
| --- | ---- | --- | ---- | --- | ---- | --- |
|     | (a)  |     | (b)  |     | (c)  |     |
Figure 11. Apparent impedance locus for the L-G fault at 2.025 s at 85% of the line under the TCSC blocking mode. (a)
| With 𝑅  = 50 Ω; (b) with 𝑅 |  = 100 Ω; (c) with 𝑅 |  = 200 Ω.  |      |     |      |     |
| -------------------------- | -------------------- | ---------- | ---- | --- | ---- | --- |
| 𝑓                          | 𝑓                    | 𝑓          |      |     |      |     |
|                            |                      |            |      |     |      |     |
|                            | (a)                  |            | (b)  |     | (c)  |     |
Figure 12. Apparent impedance locus for the L-G fault at 2.025 s at 125% of the line under the TCSC capacitive mode. (a)
| With 𝑅  = 50 Ω; (b) with 𝑅 |  = 100 Ω; (c) with 𝑅 |  = 200 Ω.  |      |     |      |        |
| -------------------------- | -------------------- | ---------- | ---- | --- | ---- | ------ |
| 𝑓                          | 𝑓                    | 𝑓          |      |     |      |        |
| Energies2021,14,7074       |                      |            |      |     |      | 16of23 |
|                            |                      |            |      |     |      |        |
|                            | (a)                  |            | (b)  |     | (c)  |        |
Figure 13. Apparent impedance locus for the L-G fault at 2.025 s at 75% of the line under the TCSC inductive mode. (a)
mode. Accordingly,itisconcludedthattheproposeddynamicsettingschemeisessential
| With 𝑅  = 50 Ω; (b) with 𝑅            |  = 100 Ω; (c) with 𝑅 |  = 200 Ω.  |      |     |      |           |
| ------------------------------------- | -------------------- | ---------- | ---- | --- | ---- | --------- |
| 𝑓                                     | 𝑓 forsuchcases.      | 𝑓          |      |     |      |           |
|                                       |                      |            |      |     |      |           |
|                                       | (a)                  |            | (b)  |     | (c)  |           |
| Energies 2021, 14, x FOR PEER REVIEW  |                      |            |      |     |      | 16 of 23  |

FigFuigreu r1e4.1 A4.pAppapreanretn itmimpepdeadnacnec elolocucuss foforr tthhee LL--GG ffaauulltt aatt 22..002255 ss aatt 111100%%o offt htheel ilnineeu unndderetrh teheT CTSCCSCby bpyapssasms omdoe.d(ea.) (Wa)i tWhith
𝑅  R=f 5=0 5Ω0; Ω(b;)( bw)iwthi th𝑅 R f= =10100 0ΩΩ; (;c()c )wwitihth 𝑅R 𝑓f == 220000 ΩΩ..
| 𝑓   | 𝑓   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
4.2.5. Evaluating the Proposed Scheme at the Two Ends of TL
4.2.5. EvaluatingtheProposedSchemeattheTwoEndsofTL
An L-G fault is simulated under the capacitive TCSC mode at 2.015 s with a large 𝑅
AnL-GfaultissimulatedunderthecapacitiveTCSCmodeat2.015swithalargeR𝑓
f
o f  1 5 0  ΩΩ  a t  t h e  lo c a t io n  o f   8 5%   f r om  t h e  f i rs t   r e la y  R 1  ( i n   it s  z o n e - 2) ,  w h ic h  a ls o   m e a n s
o f 1 5 0 a t t h e lo c a ti o n o f 8 5 % f r o m th e fi r s t r e l a y R 1 (i n i t s z o n e -2 ) , w h i ch a ls o m e a n s t h a t
that the fault is 15% from the opposite relay R2 (in its zone-1).
thefaultis15%fromtheoppositerelayR2(initszone-1).
Upon implementing the proposed scheme in both relays (R1 and R2), Figure 15 illus-
  Upon implementing the proposed scheme in both relays (R1 and R2), Figure 15
tirlalutesstr tahtee setfhfeecteifvfeecnteivsse noef sthseoifr tdhyeniradmyincaalmlyi cuaplldyautepdd saetettdinsgest t(ibnlgasck(b sloalcikd)s ocolimd)pcaormedp wariethd
twheit hcotnhveecnotniovneanlt icohnaarlacchtearriastcitce rsiestttiicnsgest t(irnegds d(areshdedda)s whehdic)hw fhaiilcehdf taoil eddetteoctd tehtiesc ftatuhlits ffraoumlt
bfrootmh ebnodtsh. e nds.
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
(a)  (b)
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
(c)  (d)
FFiigguurree 1155.. AAnn LL--GG ffaauulltt uunnddeerr tthhee ccaappaacciittiivvee TTCCSSCC mmooddee aatt 22..001155 ss wwiitthh 𝑅R Ω
𝑓f == 115500 Ω  aatt tthhee llooccaattiioonn ooff 8855%% ffrroomm tthhee ffiirrsstt
rreellaayy RR11.. ((aa)) CChhaarraacctteerriissttiiccss ooff tthhee ffiirrsstt eenndd rreellaayy RR11;; ((bb)) cchhaarraacctteerriissttiiccss ooff tthhee sseeccoonndd eenndd rreellaayy RR22;; ((cc)) ffaauulltt ddeetteeccttiioonn ooff tthhee
ffiirrsstt eenndd rreellaayy RR11;; ((dd)) ffaauulltt ddeetteeccttiioonn ooff tthhee sseeccoonndd eenndd rreellaayy RR22..
AAss iiss ccleleaarrlyly sshhoowwnn, ,ththe epprorpoposoesde ddydnyanmamici rcerlaeyla Ry1R c1ocrroercrtelcyt ldyedteectteecdt etdhet hfaeuflat uinlt iitns
zitosnzeo-2n (ed-2et(edcteetdec itte adt 2it.0a2t524 .s0)2 b5y4 asd)abpytiandga bpottinhg rebsoistthivree asinsdti vreeaactnivder reeaaccthiv seo rietsa ctrhipspoinitgs
ttirmipep winags tdimeleayweads bdye ltahyee zdobnye-t2h etimzoen de-e2latyim, wehdielela tyh,ew phrioleptohseedp rdoypnoasmedicd ryenlaaym aict Rre2l asyuca-t
ceeded in detecting the same fault in its zone-1 (detecting it at 2.025 s) by adapting only
its resistive reach without adapting its reactive reach, as TCSC is not included in its faulted
path and thus it trips instantaneously.
4.3. Further Evaluation on a Larger Test System—IEEE-39 Bus System
In order to validate the proposed scheme on a larger test system, the methodology
was widely examined on the modified 60 Hz IEEE-39 bus New England system, as shown
in Figure 16 [31]. In the modified 39-bus system, TCSC is placed at the mid-point of the
line between buses 28 and 29.

Energies2021,14,7074 17of23
R2succeededindetectingthesamefaultinitszone-1(detectingitat2.025s)byadapting
onlyitsresistivereachwithoutadaptingitsreactivereach,asTCSCisnotincludedinits
faultedpathandthusittripsinstantaneously.
4.3. FurtherEvaluationonaLargerTestSystem—IEEE-39BusSystem
Inordertovalidatetheproposedschemeonalargertestsystem,themethodology
waswidelyexaminedonthemodified60HzIEEE-39busNewEnglandsystem,asshown
Energies 2021, 14, x FOR PEER REVIEW 17 of 23
inFigure16[31]. Inthemodified39-bussystem,TCSCisplacedatthemid-pointofthe
linebetweenbuses28and29.
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
Figure16.SchematicdiagramoftheIEEE39-busNewEnglandsystemcompensatedforbyTCSC.
Figure 16. Schematic diagram of the IEEE 39-bus New England system compensated for by TCSC.
ItistobenotedthattheTCSCcompensationprovidedinthe39-bustestsystemis
It is to be noted that the TCSC compensation provided in the 39-bus test system is
exactlythesameasthatdiscussedfortheIEEE-9buspowersystemintheearliersection.
exactly the same as that discussed for the IEEE-9 bus power system in the earlier section.
TheproposeddistancerelayR1,placedatbus-29forprotectinglines28–29,isconsidered
Tfhoer pperorfpoormseadn cdeisetvaanlcuea trieolna.yA Rs1e, tpolafcreesdi satitv beugsr-o2u9n fdoerd pfraoutletcstainreg alpinpelise 2d8o–n29d,i ifsfe croenntsidered
folorc pateiorfnosr,maftaenrcteh eeTvCaSluCaltoiocant.i oAn, isnetb ootfh rtehseisctaipvaec igtirvoeuannddeidnd fuacutilvtse maroed easpopflioepde roatnio dn,ifferent
lowciathtiodnifsfe, raefnttefra uthlter eTsCistSaCn cleo,ctoateivoanl,u ainte bthoethp rtohpeo sceadpraecliatyivpee rafnordm ianndceucatnidved ymnaomdeicsa lolyf opera-
updatingtheresistiveandreactivereachesundereitherthecapacitiveorinductiveTCSC
tion, with different fault resistance, to evaluate the proposed relay performance and dy-
modesofoperation.
namically updating the resistive and reactive reaches under either the capacitive or induc-
Figure17demonstratesthetrajectoryimpedanceforL-Gfaultsattheendofzone-1of
tive TCSC modes of operation.
thetestedrelay(at75%)withR =50Ωand100Ω,andalsoattheendofzone-2(at110%)
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
o o f f th th e e t p e r s o te p d o s r e e d la r y el a ( y at w 7 i 5 th % d ) y w n i a t m h ic 𝑅 a𝑓l ly= u 5 p 0 d Ω at e a d nd se t 1 t 0 in 0 g Ω s( , t h a e nd so a li l d so b l a a t c k th c e h a e r n a d ct e o r f i s z ti o c n ) e-2 (at
1v10er%su) swthitehc o𝑅n𝑓v e=n 5ti0o nΩa lurneldaeyrw thiteh TthCeSfiCx eidndchuacrtaivctee rmistoidce(t.h Tehdea sfhigeudrree dhicghhalriagchtetrsi stthice) .perfor-
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

| Energies 2021, 14, x FOR PEER REVIEW  |     |     |     |     |     |     | 18 of 23  |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --------- |

| Energies2021,14,7074 |     |     |     |     |     |     | 18of23 |
| -------------------- | --- | --- | --- | --- | --- | --- | ------ |
b under the high fault resistance value; on the contrary, the proposed relay tripped cor-
rectly (the solid characteristic) in this case.
As a matter of fact, the achieved results ensure the correct operation of the proposed
withahighdegreeofselectivity.Asisclearlyshown,thefaultsat75%aredetectedcorrectly
scheme, in which the relay adapted its trip boundaries itself in the respective zones under
inzone-1,eitherwith50Ωfaultresistance(case-a)or100Ωfaultresistance(case-b);in
TCSC operation, according to the local information at the relay and the received infor-
addition, thefaultat110%ofthelineisdetectedproperlyinzone-2(case-c)duetothe
mation from the TCSC terminal during faulty system conditions that the conventional
zoneidentificationmethod,whilethefixedconventionalsettingcompletelyfailedtodetect
| Energies 2021, 14, x FOR PEER REVIEW  |     |             |                               |     |     |     | 18 of 23  |
| ------------------------------------- | --- | ----------- | ----------------------------- | --- | --- | --- | --------- |
|                                       |     | re la y  is |   in c a p able of handling.  |     |     |     |           |
|                                       |     | s u ch      | f a u lt s .                  |     |     |     |           |
b under the high fault resistance value; on the contrary, the proposed relay tripped cor-
rectly (the solid characteristic) in this case.
As a matter of fact, the achieved results ensure the correct operation of the proposed
scheme, in which the relay adapted its trip boundaries itself in the respective zones under
TCSC operation, according to the local information at the relay and the received infor-
mation from the TCSC terminal during faulty system conditions that the conventional
relay is incapable of handling.
|     |      |     |     |      |     |      |     |
| --- | ---- | --- | --- | ---- | --- | ---- | --- |
|     | (a)  |     |     | (b)  |     | (c)  |     |
FigFuirgeu 1re7.1 A7.pAppapreanret nitmimpepdeadnacnec efofor rththee LL--GG ffaauulltt aatt 11..00 ssu unnddeerrt htheeT CTCSCSCin idnudcuticvteivme omdeo.d(ea.) (Aa)t 7A5t% 75a%nd aRnfd= 𝑅5 0  Ω = 5;(0b Ω)a; t(b)
𝑓
|                     | Ω                                                  |     | Ω             |     |     |     |     |
| ------------------- | -------------------------------------------------- | --- | ------------- | --- | --- | --- | --- |
| at 7755%% aanndd R𝑅 | 𝑓f == 110000  Ω;;( (cc))a att1 11100%%a nadndR f𝑅= |     |  5=0 5 0 .Ω.  |     |     |     |     |
𝑓
UndertheTCSCcapacitivemode,theimpedancetrajectoryfor2L-Gfaultsinzone-2
andzone-3isillustratedinFigure18. Forcasesaandb,thefaultsoccurredat85%ofthe
linewithR =50Ωand100Ω,whileincasec,thefaultwassimulatedatthebeginningof
f
=50Ω.
zone-3(at125%)withR f Asisobviouslyrevealed,theconventionalrelaylostits
selectivity  inallexaminedcases. Infact,thecon ventionalrelayerroneouslyunderreac hes

(a)  incaseaasthefaultisdetectedinzone-3and,ontheotherhand,itincorrectlyoverreaches (b)  (c)
forthefaultinzone-3asillustratedincasec. Inaddition,itfailedtodetectthefaultin
Figure 17. Apparent impedanccaes feorb tuhne dLe-Gr tfhaeulht iagth 1.f0a us lutnredseirs ttahne cTeCvSaClu ined;ounctitvhee mcoondter.a (ray), Atht e75p%ro apnods e𝑅d r=e l5a0y Ωtr;i p(bp)e d 𝑓
| at 75% and 𝑅 |  = 100 Ω; (c) at c1o10rr%e catnlyd (t𝑅he =s o5l0i dΩc. haracteristic)inthiscase. |     |     |      |     |      |     |
| ------------ | -------------------------------------------------------------------------------- | --- | --- | ---- | --- | ---- | --- |
|              | 𝑓                                                                                |     | 𝑓   |      |     |      |     |
|              |                                                                                  |     |     |      |     |      |     |
|              | (a)                                                                              |     |     | (b)  |     | (c)  |     |
Figure 18. Apparent impedance for the 2L-G fault at 1.0 s under the TCSC capacitive mode. (a) At 85% and 𝑅  = 50 Ω; (b)
𝑓
| at 85% and 𝑅 |  = 100 Ω; (c) at 125% and 𝑅 |     |             |     |     |     |     |
| ------------ | --------------------------- | --- | ----------- | --- | --- | --- | --- |
|              | 𝑓                           |     | 𝑓  = 50 Ω.  |     |     |     |     |
5. Features Assessment with Reference to Other Techniques
Multi-fold advantages of the proposed scheme compared to some other published
techniques shall be addressed and discussed in the following section. The key advantages
of the prop osed scheme are addressed in term s of Fault Detection Time, Fault Resi stance
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Coverage, and Data Acquisition and Computation Technique.
|     | (a)  |     |     | (b)  |     | (c)  |     |
| --- | ---- | --- | --- | ---- | --- | ---- | --- |
Ω
FigFuirgeu 1r8e. 1A8.pApparpeanret nimtipmepdea5 dn. a 1cne. c   F efoa foru rtlht t   heD e 2e 2Lt L e--Gc G t iff oaa nuu  ll Ttt iaa m tt 11e .  .00 ss uunnddeerrt htheeT TCCSCSCca cpaapcaitciviteivme omdeo.d(ea.) (Aa)t 8A5t% 85a%nd aRndf = 𝑅5 0  = 5;0(b Ω)a; t(b)
𝑓
| at 8855%% aanndd R𝑅 | 𝑓f == 110000  Ω Ω;; ((cc))a att1 12255% | %a  | na nd dR f𝑅 =  5 =0  Ω .Ω |     |     |     |     |
| ------------------- | --------------------------------------- | --- | ------------------------- | --- | --- | --- | --- |
|                     |                                         |     |   p𝑓 5 0  .               |     |     |     |     |
A s   th e   r o p o s e d  scheme is used for fault detection in TCSC-compensated TLs, the
performAsanacme astpteeredof ifsa cctr,ittihcealalcyh iimevpeodrrteasnutl. tTshenussu, raessthesescionrgr etchtiso paeprpartiooancho fftohre tphreo fpaousletd de-
5. Features Assessment with Reference to Other Techniques
tescctihoenm teim,ine wshhoicuhldth beer eelvaayluadataepdte bdyi tisntvreipstbigoautnindga rtihese idtseetlefcitniothne trimesep efcotri voenzeo onfe sthuen wdeorrst
Multi-fold advantages of the proposed scheme compared to some other published
caTsCesS Cino zpoenraet-i1o no,na cthcoer IdEinEgEt-o9 tbhuesl oscyasltienmfo.r Tmhaitsio cnasaet tohcecruerlareyda nwdhtehne rLe-cGei vfaeudlitn wfoarms aaptiponlied
t a e t cf 7rho5 nm% iq  to uhf ee  s th  Ts e hC p aSl rCl o  b tte eec  ramt d edidn  r lae iln sds e e  ua drti    an2 ng.0 d 0f a7 du5 ils  ts cy, u  wssys h esitd ceh  min  is  ct   hoim en df p oiltl eilom onw esn intthe gad  st  e atcht  tet i h oce no  .ni   n Tvs het ena   ntkitoe  ny oaf  a  lz dre verla oan  yc t r aiosg s e s s -
o fi  gnt hcvae op  pata rbo glep e oo wfsehit dah  n  sd𝑅 clh e =gm e  a r e  a d d re s s e d   i n  t er m s   o f  F a u lt   D et e ct i on   T im e,  F a u l t  R es is t a n c e
in   l in    .2 0 0  Ω   u n d e r  t h e   T C S C  i n d u c t iv e   m o d e .  A s   is  re v ea l e d   in  F i g u r e
𝑓
Coverage, and Data Acquisition and Computation Technique.
19a, due to the high resistance fault, the current increases and the voltage decreases insig-
5. FeaturesAssessmentwithReferencetoOtherTechniques
nificantly and, therefore, it is expected that the conventional fixed setting will underreach
5.1. FauMltu Dltei-tfeocltdionad Tviamnet agesoftheproposedschemecomparedtosomeotherpublished
for this fault. On the other hand, Figure 19b validates the timing of different stages of the
techniquesshallbeaddressedanddiscussedinthefollowingsection. Thekeyadvantages
propAosse dth de ipstraonpcoes reedla syc,h setmareti nisg  ufrsoemd  ftohre  ffaauulltt  dinecteepcttiioonn  itnim TeC tSoC th-ceo dmepteecntsioante tdim TeL.s A, tsh ies
of the proposed scheme are addressed in terms of Fault Detection Time, Fault Resistance
pdeermfoornmstarnacteed s,p weehdil eis t hcrei tfiacualllty i nimceppotirotann otc. cTuhruresd, a asts e2s.0s0in7g5  tsh, itsh ea ppproropaocshe dfo rre tlahye  cfaourrlet cdtely-
Coverage,andDataAcquisitionandComputationTechnique.
treecctoiognn itsiemde t hshaot ual dfa buelt  ehvaadlu sattaerdte bdy a itn 2v.e0s1t6ig6a sti, nagn dth teh dee itdeecntitoinfi ctaimtioen f oorf  oTnCeS oCf  tzhoen we owrasst
cases in zone-1 on the IEEE-9 bus system. This case occurred when L-G fault was applied
at 75% of the protected line at 2.0075 s, which is implemented at the instant of zero cross-
ing voltage with 𝑅 𝑓 = 200 Ω under the TCSC inductive mode. As is revealed in Figure

19a, due to the high resistance fault, the current increases and the voltage decreases insig-
nificantly and, therefore, it is expected that the conventional fixed setting will underreach
for this fault. On the other hand, Figure 19b validates the timing of different stages of the
proposed distance relay, starting from the fault inception time to the detection time. As is
demonstrated, while the fault inception occurred at 2.0075 s, the proposed relay correctly
recognised that a fault had started at 2.0166 s, and the identification of TCSC zone was

Energies2021,14,7074 19of23
5.1. FaultDetectionTime
AstheproposedschemeisusedforfaultdetectioninTCSC-compensatedTLs,the
performance speed is critically important. Thus, assessing this approach for the fault
detection time should be evaluated by investigating the detection time for one of the
worstcasesinzone-1ontheIEEE-9bussystem. ThiscaseoccurredwhenL-Gfaultwas
appliedat75%oftheprotectedlineat2.0075s, whichisimplementedattheinstantof
zerocrossingvoltagewith R =200ΩundertheTCSCinductivemode. Asisrevealed
f
in Figure 19a, due to the high resistance fault, the current increases and the voltage
decreasesinsignificantlyand,therefore,itisexpectedthattheconventionalfixedsetting
willunderreachforthisfault.Ontheotherhand,Figure19bvalidatesthetimingofdifferent
Energies 2021, 14, x FOR PEER REVIEWst agesoftheproposeddistancerelay,startingfromthefaultinceptiontimeto1t9h oef d23e tection
time. Asisdemonstrated,whilethefaultinceptionoccurredat2.0075s,theproposedrelay
correctly recognised that a fault had started at 2.0166 s, and the identification of TCSC
azcohnieevewda ast a2c.0h1ie8 vse, dwhatile2 .t0h1e8 fsa,uwlt hzoilneet hweafsa purlotpzeornlye iwdeanstipfireodp aetr lzyonidee-1n taitfi tehde 2a.t0z2o10n5e -s1 atthe
ti2m.0e2p1o0i5nts atnimd efpinoailnlyt athned fafiunlat lwlyatsh deeftaeuctletdw faosr dtheet eccotrerdecfto trritph eatc 2o.r0r2e3c5t5t rsi,p wahti2c.h0 2m3e5a5nss, which
thmaet aonnslyt h0.a0t1o6n05ly s 0w.0a1s6 r0e5qusirwedas (0re.9q6u3i cryedcle()0 .f9ro6m3c tyhcel eti)mfreo omf ftahueltt iinmceepotfiofna.u ltinception.
(a)
(b)
FFigiguurer e191.9 O.nOe noef tohfe twheorwsto crasstesc ainse zsoinne-z1o wneh-e1rew thhee rLe-Gth feauLl-tG is fsaiumlutliastesdim atu 7la5t%ed ofa tth7e5 l%ineo aftt heline
2.0075 s. (a) Measured voltage, current at relay terminal and calculated apparent impedance; (b)
at2.0075s. (a)Measuredvoltage, currentatrelayterminalandcalculatedapparentimpedance;
timing of different stages of the proposed scheme.
(b)timingofdifferentstagesoftheproposedscheme.
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

Energies2021,14,7074 20of23
Besides, the detection time is evaluated for other simulated faults occurring dur-
ing capacitive TCSC cases and under high resistance faults of 200 Ω (demonstrated in
Figures11cand12c). Itisfoundthatallthesefaultsaredetectedwithinlessthanonecycle
fromfaultinception(about0.75cycle).
Itisworthmentioningthatthisdetectiontimeisestimatedforsimulatedcasesbutin
realcasesitmaybelonger. Infact,thefaultdetectiontimewasaffectedbytheTransducer
delaythatisusedforvoltageandcurrentmeasurements,theProcessingtimethatisrequired
forconvertingmeasureddataintophasorinformationusingDFT,andtheCommunication
delay that depends on the type of commination links as well as, the physical distance
betweentheTCSCsubstationandrelay. Therefore,forthelocalityofTCSCintheopposite
endoftherelay,thefaultdetectiontimemaybeaffectedbythecommunicationlatency.
However,duethesignificantandcontinuousdevelopmentofcommunicationapplications
withhighdatarates,the4Gwirelessbroadbandbecomes10timesfasterthan3G,which
helps in achieving reliable and fast protection schemes as the 4G latency is estimated
as50ms[32]. Inthenearfuture,5Gwillprovideamaximalplatformfordifferentgrid
applicationsincludingultratime-criticalapplicationssuchasprotectionschemes[33].
Regardingthecomparativestudywithotherpublishedtechniques,itisworthmen-
tioningthatonlytheschemeintroducedin[10]isfasterthantheproposedschemebutisso
underlessfault-resistancecoverage. Moreover,theschemein[10]doesnotconsiderthe
homogeneitysystemconcernsthatmayaffecttheaccuracyofitsresultsinsuchcases.
5.2. FaultResistanceCoverage
According to the obtained results, the large coverage of the trip boundary of the
proposed method due to the fault resistance can be clearly observed. This significant
advantageisduetothedevelopmentofthemodifiedTakagimethodthathelpsinestimating
the fault zone. Therefore, the fault resistance border can be updated properly. As is
discussedintheresults,thefaultresistancecanbecoveredupto250Ωinzone-1and200
Ω in the back-up zones of protection. Although the optimization method used in [15]
introducesgoodcoverageoftheresistivefaultupto200Ωinzone-1,themethodisonly
applicableforthefirstzoneandthefaultisdetectedafterarelativelylongiterationtime,as
ishabitualforoptimizationmethods.
5.3. DataAcquisitionandComputationTechnique
Asdescribed,theproposedtechniquebasicallyreliesonthelocaldataestimatedat
therelayterminalandonlytwovaluesarereceivedfromtheTCSCsubstationwhichare:
theTCSCfaultRMScurrent,tosimplyinformwhetherTCSCisincludedinthefaulted
loopornot,andthefiringanglethatisusedinestimatingtheTCSCimpedance. However,
somereportedschemes,suchasthosein[10]and[15],aredesignedbaseduponthelocal
terminal data but they have some limitations, as discussed in Sections 5.1 and 5.2. In
addition,in[22]and[23],thelocaldataareutilizedtoreducezone-1settinganddelayed
zone-2, but[22]didnotconsiderthefaultresistanceintheevaluation, ratherthan[23],
which is just suggested based on a poor modelling of TCSC that negatively affects the
accuracyofitsresults.
5.4. ComprehensiveComparativeinTermsofMainFeatures
Table2summarizesthecomparativestudyundertakentohighlighttheperformance
oftheproposedmethodcomparedwithsomeothertechniquesusedforquadrilateralrelay
settings.Therefore,thesalientfeaturesoftheproposeddynamicquadrilateralcharacteristic-
basedadaptivedistancerelaycanbesummarizedasfollows:
Controllability: thereactiveandresistivereachcanbecontrolledseparatelyandindepen-
dently. ThereactivereachischangedconsideringtheTCSCreactanceeffectandthesystem
homogeneityeffect,whiletheresistanceischangedconsideringthefaultresistanceeffect.

Energies2021,14,7074 21of23
Reliability,astheselectivityfeatureisobtainedbycompensatingtheundesirableeffectof
TCSCandfaultresistance.Furthermore,thesecurityisobtainedbyavoidingmal-operation
foranyexternalfaults.
Economy,asthereisnoneedformulti-filtrationdeviceswithhighlevelofsamplingtime
andnosynchronizeddataorexcessivecommunicationsarerequiredtotransmitthedata
fromtheremoteend.
Inclusivity,astheproposedmethodcanbegeneralizedandappliedforanyinterconnected
longorshortTL.
Easeofapplication, asthemethodcanbeappliedontheconventionaldistancerelaysby
modifyingtheexistingalgorithm.
Table2.Comparisonbetweentheproposeddynamicrelayandsomeothermethods.
FaultResistance
Reference FaultDetectionTime DataAcquisition ComputationTechnique
Coverage
|      |     | Upto98Ωinzone-1 |                  | Communicationadded |
| ---- | --- | --------------- | ---------------- | ------------------ |
| [10] | —   |                 | Two-terminaldata |                    |
scheme
|      | Within0.67cycles    | Upto50Ωinzone-1  |           |                       |
| ---- | ------------------- | ---------------- | --------- | --------------------- |
| [10] |                     |                  | Localdata | Highleveloffiltration |
|      | withoutcompensation | Upto20Ωinzone-2  |           |                       |
| [15] | Within1.2s          | Upto200Ωinzone-1 | Localdata | Optimization          |
Upto80Ωinzone-1
| [16] | Within1.2cycles |     | Two-terminaldata | Optimization |
| ---- | --------------- | --- | ---------------- | ------------ |
Upto150Ωinzone-1
| [20] | —            |     | Two-terminaldata | Synchronizeddatascheme |
| ---- | ------------ | --- | ---------------- | ---------------------- |
| [22] | Within1cycle | —   | Localdata        | Reducingzone-1setting  |
Upto95Ωzone-1
| [23]     | Within3cycles          |                  | Localdata | Reducingzone-1setting  |
| -------- | ---------------------- | ---------------- | --------- | ---------------------- |
|          | Within0.75cyclesand    | Upto250Ωinzone-1 |           |                        |
| Proposed |                        |                  |           | Apparentresistanceand  |
|          | 0.963cyclesfortheworst | Upto200Ωinzone-2 | Localdata |                        |
| Scheme   |                        |                  |           | circuittheoremapproach |
Upto100Ωinzone-3
case
Thesymbol“—”referstoinformationnotmentioned.
6. Conclusions
Thepaperintroducesadynamicquadrilateralcharacteristic-basedadaptivedistance
relayforTCSC-compensatedTLs. Theproposedrelayadaptsboththereactivereachand
resistivereachindependently. Thereactivereachisadjustedbyidentifyingthepresenceof
TCSCinthefaultedlooptocompensateforitseffect. Additionally,thecalculationofthe
tiltangleisinvestigatedtoconsiderthehomogeneityofthesystemduetotheloadflow
andTCSCeffectduringhighresistancefaults. Theresistivereachismodifiedadaptivelyin
TCSCTLsbyestimatingthefaultedzonethroughthemodifiedTakagimethod.
Inordertovalidateandgeneralizetheproposeddynamicdistancerelay,itisexten-
sivelytestedontwosimulatedIEEEbenchmarknetworksusingMaltab, whicharethe
IEEE-9busandNewEnglandIEEE-39bus,toconsiderbothasmallgridwithlongTLs
andalargenetworkwithshortTLs. Theproposedrelayistestedondifferentlocations
tocoverthreezonesofprotection, differentfaultresistancevalues, anddifferentTCSC
modesofoperation. Accordingtotheobtainedresults,itcanbededucedthattheproposed
scheme has conventional functions under normal fault conditions without any burden
ontherelay;inaddition,itiscapableofdetectinghighresistancefaultsduringtheTCSC
inductiveandcapacitivemodes. Additionally,itcanalleviatethenegativeimpactofTCSC
underreach/overreachbyadaptingthereactivesetting. Finally,Controllability,Reliability,
Economy, Inclusivity, and Ease of application are considered the salient features of the
proposeddynamicquadrilateralcharacteristic-basedadaptivedistancerelay.
However,ifthesystemissubjecttotransientinstabilitysuchasunstablepowerswing,
the proposed method should be modified to also consider power swing tripping and
blockingissuesbasedonfaultsconditions. Inaddition,validationthroughrealworlddata

Energies2021,14,7074 22of23
willbevaluabletoensuretheleverageoftheproposedscheme. Therefore,theseissueswill
bestudiedinfuturepublications.
AuthorContributions:Conceptualization,D.K.I.,E.A.Z.;methodology,G.M.A.-H.andD.K.I.;soft-
ware,G.M.A.-H.;investigation,G.M.A.-H.;writing—originaldraftpreparation,G.M.A.-H.andD.K.I.;
writing—reviewandediting,D.K.I.,E.A.Z.,A.F.Z.;supervision,E.A.Z.,A.F.Z.Allauthorshaveread
andagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Bakshi,U.A.;Bakshi,M.V.ProtectionandSwitchgear;TechnicalPublicationsPune:Maharashtra,India,2008.
2. Joe,M.; Jackie,P.ApplicationGuidelinesforGroundFaultProtection. InProceedingsofthe1998InternationalConference
ModernTrendsintheProtectionSchemesofElectricPowerApparatusandSystems,NewDelhi,India,28–30October1998.
3. Sauvik,B.;Paresh,K.N.State-Of-The-ArtonTheProtectionofFACTSCompensatedHigh-VoltageTransmissionLines:Areview.
IETCEPRI2018,3,21–30.
4. Mathur,R.M.;Rajiv,K.V.Thyristor-BasedFACTSControllersforElectricalTransmissionSystems;JohnWiley&Sons:Hoboken,NJ,
USA,2011.
5. Ahad,K.;Shahram,J.;Hossein,S.DistanceRelayOver-ReachinginPresenceofTCSConNextLineConsideringMOVOperation.
In Proceedings of the 45th International Universities Power Engineering Conference UPEC2010, Cardiff, UK, 31 August–3
September2010.
6. Beleed, H.; Johnson, B.K.; Hess, H.L. An Examination of the Impact of D-FACTS on the Dynamic Behavior of Mho and
QuadrilateralGroundDistanceElements. InProceedingsofthe2020IEEEPower&EnergySocietyInnovativeSmartGrid
TechnologiesConference(ISGT),Washington,DC,USA,17–20February2020;pp.1–5.[CrossRef]
7. Holbach,J.;Vadlamani,V.;Lu,Y.IssuesandSolutionsinSettingaQuadrilateralDistanceCharacteristic.InProceedingsofthe
200861stAnnualConferenceforProtectiveRelayEngineers,CollegeStation,TX,USA,1–3April2008;pp.89–104.[CrossRef]
8. Fernando, C.; Armando, G.; Gabriel, B. Adaptive Phase and Ground Quadrilateral Distance Elements; Schweitzer Engineering
Laboratories,Inc.:Pullman,WA,USA,2017.
9. Bogdan,K.SettingsConsiderationsforDistanceElementsinLineProtectionApplications.InProceedingsofthe2021TexasA&M
ConferenceforProtectiveRelay,Presentedatthe74thAnnualGeorgiaTechProtectiveRelayingConference,CollegeStation,TX,
USA,28–30April2021.
10. Shateri,H.;Jamali,S.RobustnessofcommunicationaideddistancerelaywithQuadrilateralcharacteristicagainstinterphase
faultresistance. InProceedingsofthe2010InternationalConferenceonPowerSystemTechnology,Hangzhou,China,24–28
October2010;pp.1–8.[CrossRef]
11. Patel,U.J.;Chothani,N.G.;Bhatt,P.Adaptivequadrilateraldistancerelayingschemeforfaultimpedancecompensation.Electr.
Control.Commun.Eng.2018,14,58–70.[CrossRef]
12. Aneesh,S.;Angel,T.S.QuadrilateralRelayBasedDistanceProtectionSchemeforTransmissionLinesunderVaryingSystem
Conditions. InProceedingsofthe2015IEEEInternationalConferenceonTechnologicalAdvancementsinPower&Energy,
Kollam,India,24–26June2015.[CrossRef]
13. Venkatanagaraju,K.;Biswal,M.;Bansal,R.Adaptivedistancerelayalgorithmtodetectanddiscriminatethirdzonefaultsfrom
systemstressedconditions.Int.J.Electr.PowerEnergySyst.2021,125,106497.[CrossRef]
14. Sorrentino,E.;DeAndrade,V.Optimal-ProbabilisticMethodtoComputetheReachSettingsofDistanceRelays. IEEETrans.
PowerDeliv.2011,26,1522–1529.[CrossRef]
15. Davydova,N.;Shchetinin,D.;Hug,G.;Davvdova,N.OptimizationofFirstZoneBoundaryofAdaptiveDistanceProtectionfor
FlexibleTransmissionLines.InProceedingsofthe2018PowerSystemsComputationConference(PSCC),Dublin,Ireland,11–15
June2018.[CrossRef]
16. Shukla,S.K.;Koley,E.;Ghosh,S.ANovelApproachBasedonLineInequalityConceptandSine–CosineAlgorithmforEstimating
OptimalReachSettingofQuadrilateralRelays.Arab.J.Sci.Eng.2020,45,1499–1511.[CrossRef]
17. Serna, J.D.J.J.; López-Lezama, J.M.CalculationofDistanceProtectionSettingsinMutuallyCoupledTransmissionLines: A
ComparativeAnalysis.Energies2019,12,1290.[CrossRef]
18. Orosz,T.;Rassõlkin,A.;Kallaste,A.;Arsénio,P.;Pánek,D.;Kaska,J.;Karban,P.RobustDesignOptimizationandEmerging
TechnologiesforElectricalMachines:ChallengesandOpenProblems.Appl.Sci.2020,10,6653.[CrossRef]
19. Srivani,S.;Vittal,K.P.Adaptivedistancerelayingschemeinseriescompensatedtransmissionlines.InProceedingsofthe2010
JointInternationalConferenceonPowerElectronics,DrivesandEnergySystems&2010PowerIndia,NewDelhi,India,20–23
December2010;pp.1–7.
20. Biswal,M.;Pati,B.B.;Pradhan,A.K.Adaptivedistancerelaysettingforseriescompensatedline.Int.J.Electr.PowerEnergySyst.
2013,52,198–206.[CrossRef]

Energies2021,14,7074 23of23
21. Achary,K.S.K.;Raja,P.Adaptivedesignofdistancerelayforseriescompensatedtransmissionline.EnergyProcedia2017,117,
527–534.[CrossRef]
22. Magagula,X.G.;Nicolae,D.V.;Yusuff,A.A.Theperformanceofdistanceprotectionrelayonseriescompensatedlineunderfault
conditions.InProceedingsoftheAFRICON2015,AddisAbaba,Ethiopia,14–17September2015;pp.1–6.[CrossRef]
23. Paladhi,S.;Pradhan,A.K.AdaptiveZone-1SettingFollowingStructuralandOperationalChangesinPowerSystem.IEEETrans.
PowerDeliv.2017,33,560–569.[CrossRef]
24. Seo,W.-S.;Kang,S.-H.;Yoon,Y.-D.;Yoon,J.-S.AConventionalDistanceProtectionforSeries-CompensatedLinesConsidering
TCSCProtectedbyaMetalOxideVaristor.InProceedingsofthe2019IEEE8thInternationalConferenceonAdvancedPower
SystemAutomationandProtection(APAP),Xi’an,China,21–24October2019.
25. Woo,S.S.; Min,S.K.; Sang,H.K.; Jong,S.Y.; Chang,H.H.AnImprovedSettingMethodoftheDistanceProtectiveLEDsfor
Series-CompensatedTransmissionLinesBasedonACaseStudyApproach.Electr.PowerSyst.Res.2020,188,106554.
26. Vyas,B.;Maheshwari,R.P.;Das,B.Protectionofseriescompensatedtransmissionline:Issuesandstateofart.Electr.PowerSyst.
Res.2014,107,93–108.[CrossRef]
27. Ordóñez,C.;Gómez-Expósito,A.;Maza-Ortega,J.SeriesCompensationofTransmissionSystems:ALiteratureSurvey.Energies
2021,14,1717.[CrossRef]
28. Ibrahim,D.K.; Abo-Hamad,G.M.; Zahab,E.E.-D.M.A.; Zobaa,A.F.ComprehensiveAnalysisoftheImpactoftheTCSCon
DistanceRelaysinInterconnectedTransmissionNetworks.IEEEAccess2020,8,228315–228325.[CrossRef]
29. Das,S.;Santoso,S.;Gaikwad,A.;Patel,M.Impedance-basedfaultlocationintransmissionnetworks:Theoryandapplication.
IEEEAccess2014,2,537–557.[CrossRef]
30. Abo-Hamad,G.;Ibrahim,D.;Zahab,E.A.;Zobaa,A.AdaptiveMhoDistanceProtectionforInterconnectedTransmissionLines
CompensatedwithThyristorControlledSeriesCapacitor.Energies2021,14,2477.[CrossRef]
31. Sahoo,B.;Samantaray,S.R.SystemIntegrityProtectionSchemeforEnhancingBackupProtectionofTransmissionLines.IEEE
Syst.J.2021,15,4578–4588.[CrossRef]
32. Eissa,M.Developingwideareaphaseplaneprimaryprotectionscheme“WA4PS”forcomplexsmartgridsystem.Int.J.Electr.
PowerEnergySyst.2018,99,203–213.[CrossRef]
33. Hovila,P.;Syväluoma,P.;Kokkoniemi-Tarkkanen,H.;Horsmanheimo,S.;Borenius,S.;Li,Z.;Uusitalo,M.5Gnetworksenabling
newsmartgridprotectionsolutions.InProceedingsofthe25thInternationalConferenceonElectricityDistribution:CIRED2019,
Madrid,Spain,3–6June2019;p.341.