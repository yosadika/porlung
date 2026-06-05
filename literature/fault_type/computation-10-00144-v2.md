computation
Article
A Review and Taxonomy on Fault Analysis in Transmission
Power Systems
YaserAlMtawa1,* ,AnwarHaque2andTalalHalabi3
1 DepartmentofAppliedComputerScience,TheUniversityofWinnipeg,Winnipeg,MBR3B2E9,Canada
2 DepartmentofComputerScience,WesternUniversity,London,ONN6A5B7,Canada
3 DepartmentofComputerScienceandSoftwareEngineering,LavalUniversity,Québec,QCG1V0A6,Canada
* Correspondence:y.almtawa@uwinnipeg.ca
Abstract: Enhancing resiliency in a power grid system is one of the core mandates of electrical
distributioncompaniestoprovidehigh-levelservice.Thepowerresiliencyresearchcommunityhas
proposednumerousschemes,todetect,classify,andlocalizefaultevents. However,theliterature
stilllacksacomprehensivetaxonomyoftheseschemeswhichcanhelpadvancefutureresearch.
Thisstudyaimstoprovideacompactyetcomprehensivereviewofthestate-of-the-artsolutions
tofaultanalysisintransmissionpowersystems. Wediscussfaulttypesandseveralfault-analysis
methodologiesadoptedbyrelevantresearchworks,proposeanovelframeworktoclassifythese
works,andhighlighttheirstrengthsandlimitations.Weanticipatethatthisbriefreviewwouldbe
helpfulasaliteraturereviewandbenefittheresearchcommunityinchoosingsuitabletechniquesfor
faultanalysis.
Keywords: power system; smart grid; fault analysis; fault identification; fault detection; fault
localization
Citation:AlMtawa,Y.;Haque,A.; 1. Introduction
Halabi,T.AReviewandTaxonomy
Electricpowersystemshaveevolvedoverdecadesfromsynchronousmachinesto
onFaultAnalysisinTransmission
renewableenergysourcesforgeneratingelectricity. However,thepowergrid’soperation
PowerSystems.Computation2022,10,
hasalwaysbeenchallengingbecauseofextremeoperationalandenvironmentalconditions.
144. https://doi.org/10.3390/
In this section, we address the need for power system fault analysis and provide the
computation10090144
contributionsandstructureofthispaper.
AcademicEditor:DemosT.Tsahalis
1.1. Background
Received:16June2022
Powertransmissionisthefirststeptotransportingthebulkofpowerfromapower
Accepted:18August2022
generatortothelastmileofapowergrid. Thetransmissionsystemincludesmanyfun-
Published:24August2022
damentalcomponentssuchasstep-upandstep-downtransformers,powerlines,towers,
Publisher’sNote:MDPIstaysneutral
switches,relays,andreclosers. Figure1showsdifferentsubsystemsofapowergridsystem.
withregardtojurisdictionalclaimsin
Thissystemissusceptibletomanychallenges,suchaspowerlossthatchangestothermal
publishedmapsandinstitutionalaffil-
energyduetoconductorresistance(I2R),whereIisthecurrentandRistheresistance. That
iations.
is why the voltage is increased to minimize the resistive loss. Another challenge is the
skineffect,wherecurrentflowsalongtheoutersurface/skinofthecableduetoahighfre-
quency. Thismeansthatthecurrentflowsthroughaverysmallportionoftheconductor’s
cross-section,therebyincreasingtheresistance. Thesechallengesandenvironmentalfactors
Copyright: © 2022 by the authors.
Licensee MDPI, Basel, Switzerland. suchasstorms,heavyfreezingrains,andwildhabitatactivitiescontributetotransmission
This article is an open access article elementfaults. Thesecouldheavilyimpactcustomers,suchastherecenthistoricblackouts
distributed under the terms and that hit Texas, USA, in 2021 due to a severe winter storm. Hurricane Sandy is another
conditionsoftheCreativeCommons examplethathittheUSAin2012,causingawiderangeofdamage,hundredsofcasualties,
Attribution(CCBY)license(https:// andthousandsofdisplacedresidentsinthegreatNewYorkarea[1].
creativecommons.org/licenses/by/
4.0/).
Computation2022,10,144.https://doi.org/10.3390/computation10090144 https://www.mdpi.com/journal/computation

Computation 2022, 10, 144 2 of 20
hundreds of casualties, and thousands of displaced residents in the great New York area
[1].
The most recent review in this field [2] described different techniques investigated
by several researchers for detecting, classifying, and localizing transmission faults. How-
ever, it lacks a clear classification scheme and only provides a comparative analysis for
fault localization proposals. In [3], the authors employed fault-analysis methods to clas-
sify a limited number of relevant previous works. Other studies and surveys classified the
Computation2022,10,144 works differently, e.g., according to their computational intelligence features [4] as p2roofm19-
inent, hybrid, or modern [5].
Distribution System
Power Storage
Wind Power
Farm
Pole
Pole
Solar Power Farm
Transformer
Tower
Power Generation Plant
Generation System Transmission System
Figure 1. A schematic of a Power Grid System, where the gray-shaded part represents the trans-
Figure1.AschematicofaPowerGridSystem,wherethegray-shadedpartrepresentsthetransmis-
mission system.
sionsystem.
1.2. Contribution of the Paper
Themostrecentreviewinthisfield[2]describeddifferenttechniquesinvestigatedby
severOalurre sceoanrtcrhibeurstifoonrsd reetleacttivineg t,oc tlahses rifeycienngt, raensdealroccha wlizoinrkg itnr athnesm fiieslsdi ocnanfa buel tssu.mHmowareivzeerd,
iatsl afockllsowasc:l earclassificationschemeandonlyprovidesacomparativeanalysisforfault
lo cali
U
za
n
t
l
i
i
o
k
n
e
p
o
r
t
o
h
p
er
o s
s
a
u
l
r
s
v
.
e
I
y
n
s
[
,
3
t
]
h
,
i
t
s
h
s
e
tu
au
d
t
y
h o
p
r
r
s
ov
e
i
m
de
p
s
l o
a
y e
d
d
ee
f
p
a
e
u
r
l t
i
-
n
a
s
n
i
a
g
l
h
y
t
s i
i
s
nt
m
o
e
t
t
h
h
e
o
c
d
o
s
m
to
pr
c
e
la
h
s
e
s
n
if
s
y
iv
a
e
limitednumberofrelevantpreviousworks. Otherstudiesandsurveysclassifiedtheworks
and most recent state-of-the-art techniques for academic and industrial research com-
differently, e.g.,accordingtotheircomputationalintelligencefeatures[4]asprominent,
munities;
hybrid,ormodern[5].
 We highlight the key challenges presented in the recent literature and summarize the
related research work in terms of their strengths, weaknesses, and gaps;
1.2. ContributionofthePaper
 We provide a novel classification scheme to classify relevant fault-analysis tech-
Ourcontributionsrelativetotherecentresearchworkinthefieldcanbesummarized
niques according to the method used and the target task (i.e., detection, classification,
asfollows:
or localization).
• Unlikeothersurveys,thisstudyprovidesadeeperinsightintothecomprehensiveand
1.3. Rmeovsietwre Mcenetthsotdaotelo-ogfy- the-arttechniquesforacademicandindustrialresearchcommunities;
• Wehighlightthekeychallengespresentedintherecentliteratureandsummarizethe
In Figure 2, we present a flowchart to provide a visual connection of the different
relatedresearchworkintermsoftheirstrengths,weaknesses,andgaps;
components of our methodology. While each component is described in detail in the sub-
• We provide a novel classification scheme to classify relevant fault-analysis tech-
sequent sections, this flowchart shows our review methodology as a whole, emphasizing
niquesaccordingtothemethodusedandthetargettask(i.e.,detection,classification,
the integration between its components.
orlocalization).
1.3. ReviewMethodology
In Figure 2, we present a flowchart to provide a visual connection of the different
components of our methodology. While each component is described in detail in the
subsequentsections,thisflowchartshowsourreviewmethodologyasawhole,emphasizing
theintegrationbetweenitscomponents.

CCoommppuuttaattiioonn 22002222,, 1100,, 114444 33 ooff 1290
Methodology
Introduction
Background
Contributions of the Paper
Challenges
Classification of Faults in Transmission Systems (Transient vs. Permanent)
Steps of Fault-Monitoring Systems
Classification of Faults Based on Used Method
Surveying Relevant Articles in Fault Analysis
Summary Table of Surveyed Works
Discussions: Strengths, Weakness, and Gaps of Different Techniques
Figure 2. The process flow of our review methodology.
Figure2.Theprocessflowofourreviewmethodology.
11..44.. TThhee PPaappeerr OOuuttlliinnee
TThhee ssttrruuccttuurree ooff tthhisisp paappeerri sisa sasf oflollolwows:sS: eScetciotinon2 2p rporvoivdiedseas cal acslsaisfiscifaitciaotnioonf ofaf uflatuslitns
aint raa tnrasmnsimssiisosniosny ssytesmte.mF. aFualutlat naanlaylsyissiste tcehchnniqiquuesesa arered disisccuusssseeddi ninS Seeccttiioonn 33;; aa ssuummmmaarryy
ooff tthheessee tteecchhnniiqquueess bbaasseedd oonn tthhee mmeetthhoodd uusseedd ffoorr ffaauulltt aannaallyyssiiss aanndd ssoommee kkeeyy ppooiinnttss iiss
pprroovviiddeedd iinn SSeeccttiioonn 44.. FFiinnaallllyy,, wwee ccoonncclluuddee tthhee ppaappeerr iinn SSeeccttiioonn 55..
2. FaultClassificationandMonitoring
2. Fault Classification and Monitoring
A transmission power system encounters different types of faults, classified into
A transmission power system encounters different types of faults, classified into tran-
transientandintransient,asshowninFigure3. Theformerisnotusuallyvisibletopower
sient and intransient, as shown in Figure 3. The former is not usually visible to power
techniciansandisdifficulttolocate;thepowercangoofftemporarilyandthenberestored.
technicians and is difficult to locate; the power can go off temporarily and then be re-
Examples of transient faults are temporary contact of a tree to any transmission phase,
stored. Examples of transient faults are temporary contact of a tree to any transmission
animals like birds contacting power lines, lightning strikes affecting the transmission
phase, animals like birds contacting power lines, lightning strikes affecting the transmis-
system,andphasesclashingduetostorms. Thelattertype,i.e.,intransient,ispermanent
sion system, and phases clashing due to storms. The latter type, i.e., intransient, is perma-
untilpowerengineersfixit. Itcanbeeitheropenorshortcircuited[6,7].
nent until power engineers fix it. It can be either open or short circuited [6,7].
Incontrasttoshort-circuitfaults, open-circuitfaultsoccurwhenoneormorelines
In contrast to short-circuit faults, open-circuit faults occur when one or more lines
malfunctionorbreakwithoutmakingcontactwithanyexternalobjectsorground. This
malfunction or break without making contact with any external objects or ground. This
faultproducesaveryhighvoltageinsomepartsofthetransmissionsystem,causingvoltage
fault produces a very high voltage in some parts of the transmission system, causing volt-
instability,whichmaydevelopintoshort-circuitfaultsandposeadangertohumansand
age instability, which may develop into short-circuit faults and pose a danger to humans
animals[8].
and animals [8].
Ontheotherhand,short-circuitfaultsresultfromabnormalcontactoflowimpedance
On the other hand, short-circuit faults result from abnormal contact of low imped-
betweentwopartiesofdifferentpotentialsduetorandomandunpredictableeventssuch
ance between two parties of different potentials due to random and unpredictable events
assevereweatherconditions,animals,supply/demandunbalancing,andaging. Conse-
such as severe weather conditions, animals, supply/demand unbalancing, and aging. Con-
quently,powerreturnstothesourceanddoesnotreachthedistributionsystem,causing
sequently, power returns to the source and does not reach the distribution system, causing
ahighcurrenttoflowthroughthetransmissionsystemtoanobject/ground,damaging
a high current to flow through the transmission system to an object/ground, damaging the
theequipment. Therefore,transmissionpowerfaultscanbefurtherclassifiedintophase
equipment. Therefore, transmission power faults can be further classified into phase faults
faultsorgroundfaults. Phasefaultreferstothecasewhenpowerlinescontacteachother
or ground faults. Phase fault refers to the case when power lines contact each other or

CComompuptuattaitoino n2022022,2 1,01,0 1,4144 4 4 o4f o2f01 9
anorotahneort ohberjeoctb jbeuctt bnuott nthoet gthreougnrodu. nIfd t.hIef ftahuelfta auflftecatfsfe acltls tahlrleteh preheapsehsa eseqsueaqlluya, ltlhye, tfhaeulfta uisl t
syismsmymetmrice t(rLicLL(L).L OL)t.hOertwheisrew, iist eis, iatsiysmasmyemtrmice (tLriLc)(. LOLn). tOhen otthheeor thhaenrdh, aan gdr,oaugnrdo ufanudlt foacu-lt
cuorcsc uwrshewnh aennya ntryantrsamnissmsiiosnsi opnhapshea csoenctoancttas ctthset hgeroguronudn. dS.o,S oit, iist iesitehitehre ornoen elinlien etot oththe e
ggrorouunndd (L(LGG),) ,twtwoo lilninees stoto ththee ggrorouunndd (L(LLLGG),) ,oor rththrereee lilnineess (L(LLLLLGG) )[9[9].] .
Transmission
Line Fault
Classification
Transient Intransient
Faults Faults
Tree temporary
contact Open Circuit Short Circuit
Animal
contact
One Open Two Open Three Open
Phase Phases Phases
Lightining
Storm leads to
Phases Fault Ground Fault
phases’ clash
Symmetrical Asymmetrical LG LLG LLLG
LLL LL
FiFgiugurer e3.3 C.Clalsassisfiificactaitoinon ofo ffafuaultlst sinin oovverehrheaedad trtarnansmsmisissisoionn lilninese.s .
PPoowwere rggrirdids saraer ehhigighhlyly frfaraggiliel esysystsetmems,s ,aanndd mmaannyy fafactcotorsr simimppaactc tththee ppeerfroformrmaanncec e
anandd quqaulaitlyit oyf osefrsveircve.i cTeh.erTehfoerree,f oitr ies, imitpiseriamtipveer taot ievmebteode fmaublet dresfialuielntcrye sainlide nsceylf-ahnedalisnegl f-
phroecaelisnsgesp irno cpeoswseesri gnrpidosw teor pgrroidmspttolyp lroocmatpet ltyhelo fcaautletst,h reefpaauilrt sth,reemp,a airntdh erems,toarned threes ptoorweethr e
seprovwiceer [s1e0r]v. iOcene[1 o0f] .thOen peilolafrtsh eofp riellsairliseonft rseyssitleiemnst sisy shtaevminsgi sdhaatav ianbgoudta tdaifafberoeuntt dsiyfsfeteremn t
cosymspteomnecnotms, pporonceenstssi,npgr iot,c easnsdin dgraitw, ainngd adnr ainwstianngtaanneionussta pnitcatnuereo uosf tphiecitru sretaotef. tUhenifrorsttuat-e.
nUatnelfyo,r tluegnaacteyl yp,olewgearc ygrpidosw learckg rbidosthl aac krebaol-tthimaer emale-atismueremmeeanstu orfe mtheenirt sotfatthee airndst aat edairnedct a
wdaiyre tcot awsaseystso thases peassratmheeptearrsa omf eat eproswoefra gproidw seyrsgterimd ssuyscthe mas saucctihvea scuacrrtievnet,c vuorrlteangte,,v pohltaasg-e,
phasors,etc. However,deployingsensorsenableslegacypowergridsystemstocopewith
ors, etc. However, deploying sensors enables legacy power grid systems to cope with this
thisdrawbackandactproactivelyratherthanreactivelytopreventfaults. Furthermore,the
drawback and act proactively rather than reactively to prevent faults. Furthermore, the
powerinatransmissionlinecanflowineitherdirectionaccordingtotheloadatthetwo
power in a transmission line can flow in either direction according to the load at the two
ends,andhencetheinformationfromtheendpointsoftransmissionlinesisnecessaryto
ends, and hence the information from the endpoints of transmission lines is necessary to
developaholisticpictureofthestateofatransmissionsystem.
develop a holistic picture of the state of a transmission system.
Historically,thetopologyofatransmissionsystemhasbeenusedalongsideelectricity
Historically, the topology of a transmission system has been used alongside electric-
lawstoestimatevariouspowerparameters,suchasvoltagevaluesatseveralinterconnec-
ity laws to estimate various power parameters, such as voltage values at several intercon-
tionpointsofthepowersystem. Thecontrolcentercalculatestheseparameterreadingsto
nection points of the power system. The control center calculates these parameter readings
generateapartialpictureofthesystem’sstate. Asaresult,faultscanbedetected. However,
to generate a partial picture of the system’s state. As a result, faults can be detected. How-
the fault itself can’t be accurately localized using minimal measurements. It is usually
ever, the fault itself can’t be accurately localized using minimal measurements. It is usu-
spottedandinspectedvisually,whichistime-consuming[11].
ally spotted and inspected visually, which is time-consuming [11].
Intheearly1980s,relayswereusedtodetectandlocalizefaultsinpowertransmission
In the early 1980s, relays were used to detect and localize faults in power transmis-
lines. Onceafaultoccurs,twosurgesofpoweraregeneratedbythatfault. Thesesurges
sion lines. Once a fault occurs, two surges of power are generated by that fault. These
flow to relays placed at the two ends of the power line. Thus, a fault is detected. The
surges flow to relays placed at the two ends of the power line. Thus, a fault is detected.
timedifferencebetweenreceivingthesesurgesismeasuredtocalculatethefaultlocation.
The time difference between receiving these surges is measured to calculate the fault lo-
Thismethodissimpleandeasytoapply,usingawavelettransformtosignals[12]. Still,
cation. This method is simple and easy to apply, using a wavelet transform to signals [12].
itsuffersfromdrawbackssuchaslocalizationinaccuracyduetothelackofcapturingan

Computation 2022, 10, 144 5 of 20
Computation2022,10,144 5of19
Still, it suffers from drawbacks such as localization inaccuracy due to the lack of capturing
an accurate measurement of the time difference between the two surges, given that the
accuratemeasurementofthetimedifferencebetweenthetwosurges,giventhatthesignals
s t i r g a n v a e l l s a t t ra th v e el s a p t e t e h d e o s f p l e i e g d h t o ( f i . l e ig ., h 3 t × (i.e 1 . 0 , 83 m × 1 / 0 s 8 ) . m In /s d ). e I e n d d , e a e s d l , i g a h s t li d g r h if t t d i r n if t t i m in e ti d m if e f e d r i e f n fe c r e e w nc i e ll
will significantly impact the localization of the fault place. For instance, 1 µs (microsec-
significantlyimpactthelocalizationofthefaultplace. Forinstance, 1µs(microsecond)
ond) of time difference drifts the estimated location of the fault by 300 m. Recent research
oftimedifferencedriftstheestimatedlocationofthefaultby300m. Recentresearchhas
has overcome the inaccuracy of the wavelet transform by combining it with other tools
overcometheinaccuracyofthewavelettransformbycombiningitwithothertoolssuchas
such as entropy-based methods to identify different faults’ time-frequency characteristics.
entropy-basedmethodstoidentifydifferentfaults’time-frequencycharacteristics. Hence,
Hence, it accurately and quickly determines the fault type or disturbances with sufficient
itaccuratelyandquicklydeterminesthefaulttypeordisturbanceswithsufficientnoise
ntooliesrea tnocleer[a1n3c].e [13].
FFaauulltt--mmoonniittoorriinngg ssyysstteemmss uussuuaallllyy ttaarrggeett tthhrreeee ttaasskkss:: ddeetteeccttiioonn,, iiddeennttiifificcaattioionno orrc clalasss-i-
sfiifciactaitoinon,a, nanddlo lcoaclailziaztaitoino,na, sass hsohwownnin inF iFgiugruere4 .4.
Fault Detection of
Phase 1
Fault Detection of
Classification Localization
Phase 2
Fault Detection of
Phase 3
FFiigguurree 44.. SStteeppss iinn ffaauulltt--mmoonniittoorriinngg ssyysstteemmss.. AAnnyy ccoommbbiinnaattiioonn ooff ffaauullttss iinn lliinnee pphhaasseess ccoouulldd eexxiisstt..
Faultdetectionreferstotheprocessthatshowsinstabilityinthetransmissionsystem
Fault detection refers to the process that shows instability in the transmission system
anddependsoncollectingdifferentsystemstatemeasurementssuchasvoltage,current,
and depends on collecting different system state measurements such as voltage, current,
andphases’differences. Themeasurementsfromallphasescanindicatewhetherornot
and phases’ differences. The measurements from all phases can indicate whether or not
there is a fault in a power system. The second step is responsible for classifying and
there is a fault in a power system. The second step is responsible for classifying and iden-
identifyingfaulttypes. Monitoringofalltransmissionlinesallowsbetteridentificationof
tifying fault types. Monitoring of all transmission lines allows better identification of fault
faulttypes. Thisstepiscriticalfortechnicalstafftounderstandtheissuestheyaredealing
types. This step is critical for technical staff to understand the issues they are dealing with
withandtogatherallofthenecessaryequipmenttosolvethem.
and to gather all of the necessary equipment to solve them.
The last step is localizing the fault, which refers to the process that ends up find-
The last step is localizing the fault, which refers to the process that ends up find-
ing/locatingthefaultplace. Faultlocalizationutilizesthemeasurementsfromthedetection
ing/locating the fault place. Fault localization utilizes the measurements from the detec-
steptolocatefaultsaccurately.
tion step to locate faults accurately.
3. FaultAnalysisTechniques
3. Fault Analysis Techniques
Thispaperprovidesanovelclassificationschemetoclassifyfaultanalysistechniques
This paper provides a novel classification scheme to classify fault analysis techniques
bythemethodsusedandtheirtasks(i.e.,detection,identification,andlocalization).Figure5
by the methods used and their tasks (i.e., detection, identification, and localization). Fig-
showstheclassificationoffaultanalysistechniquesbythemethodsused. Atechniquecan
ure 5 shows the classification of fault analysis techniques by the methods used. A tech-
eitheruseconventionalormodernapproachestoanalyzefaults.
niqueA cafanu elitthiserte umsep ocoranrvyeniftiiotnisalc loera mreoddaefrtner abprperaokaecrhreesc tloo sainnaglyazned fiasualtsp.e rmanentfault
otherwise [14]. A permanent fault requires power technicians to locate and repair the
faultedlinesectiontorestorepowerservice. Inconventionalmethods,protectiverelays,
placed at both ends of a transmission line, sense the fault immediately and isolate the
faultedlinebyopeningtheassociatedcircuitbreakers[15]. Distancerelaysarefastand
reliablewaystolocatethefaultarea. However,theyfallshortofprovidingaccuratefault
localization. Inaddition,itisdifficulttoidentifyandclassifyfaultsusingrelays,triggering
theneedforothertechniquestoovercomethisdrawback.
A wavelet-based technique is effective for analyzing transient power faults. It is
mainlyeffectiveforfaultdetectionandlocalization[16–20]. Improvingfaultdetectionand
locationaccuracycanbeachievedbyusingthemaximumwaveletcoefficients(WCs)ofthe
frequencyandvoltagesignalsunderfaultdisturbanceandinvestigatingtherelationship
betweentheWCsandpowervariation. Faultdetection,identification,andlocationusu-
allyneedtobesolvedasaunifiedprobleminpowersystems. However,mostmethods
discussed in previous literature focus on one or two aspects and cannot solve all three

Computation2022,10,144 6of19
problemssimultaneously. Itcanbeforeseenthatamultifunctionalapproach,whichcan
Computation 2022, 10, 144 6 of 20
achievefaultdetection,identification,andlocalization,hasthepotentialforawiderange
ofapplicationsinpowersystems.
Classification
Transmission
Line Fault
Techniques by
Tool Used
Conventional
Modern Tools
Tools
Relays Control Theory Artificial Communication
Intelligence (AI) Network
Switches
Wavelet Fuzzy Logic Boolean Logic GSM WSNs
Probabilistic Methods Evolutionary Neural
for Uncertain Reasoning Computation Network
Hidden Bayesian Genetic
Kalman Filter Shallow Deep
Markov Network Algorithms
Learning Learning
Process
Statistical Learning
Methods
Decision Support Vector
Tree Machine
FFigiguurer e5.5 C.Clalsassisfiificactaitoinon oof ffafuaultl tananalaylysissi stetcehchnniqiquuese sbbaasesded oonn ththee mmeeththoodd uusesedd. .
AT .faTuaklta igsi teetmalp.o[2r1a]ryd eifv eitl oisp ecdleaanreedq aufatteiro nbrbeaaskeedr ornectlhoesienlgec atrnicda lise qau paetiromnasnoefntth efaluolotp
oftohremrwediseb y[1a4]s.i nAg lpe-eprmhaasneetnot gfraouultn drerqeusiirsetisv epofawueltr, utescihnngicoinalnys thtoe wlocaavteel eatnrdea rdeipnagisr ftrhoem
faounleteedn dlinoef tsheecttiroann stom riesssitoonrel ipnoew. Tehr esyerlvocicael.i zIend cfoanuvltesnitnioantarla mnsemthisosdios,n plrinoetebcytivseep raerlaatyisn,g
ptlhaececdir caut ibtointhto etnwdos eoqfu aiv atrlaennstmciirscsuiiotns: loinnee,p sreionrset oththee ffaauulltt iamnmdtehdeiaottehlyer adnudr iinsgoltahtee ftahuel t.
faEualctehdo lfinthe ebsye goipveensinagn tehqeu aastisoonciaatbeodu ctitrhcueict ubrrreeanktearsn d[1t5h].e Dvioslttaangcee. rOelnaytsh earoet hfaesrt haanndd ,
remlioadbleer nwtaeycsh tnoi qlouceastec athneb feaucllat sasriefiae.d Hionwtoevcoenr,t rthoelyth feaollr ysh,Aorrtt iofif cpiarolvInidteinllgig aecnccuera(AteI )f,aaunltd
communicationnetworks.
localization. In addition, it is difficult to identify and classify faults using relays, triggering
the need for other techniques to overcome this drawback.
3.1. ControlTheory
A wavelet-based technique is effective for analyzing transient power faults. It is
Controltheoryreferstothefieldfocusingoncontrollingdynamicsystemsandensuring
mainly effective for fault detection and localization [16–20]. Improving fault detection and
the stability of the operating systems without delay. Next, we discuss fuzzy logic and
location accuracy can be achieved by using the maximum wavelet coefficients (WCs) of
Booleanlogicaswell-knownmethodsincontroltheory.
the frequency and voltage signals under fault disturbance and investigating the relation-
ship between the WCs and power variation. Fault detection, identification, and location
3.1.1. FuzzyLogic
usually need to be solved as a unified problem in power systems. However, most methods
Fuzzylogic(FL)isanextensionofamultivaluedlogicalsystem. Thiscontroltheory
discussed in previous literature focus on one or two aspects and cannot solve all three
classfollowsanintuitiveapproachwithlesscomplexity[22]. Thetruthvariablesarereal
problems simultaneously. It can be foreseen that a multifunctional approach, which can
valuesbetween0and1,where0meansveryfalseand1meansverytrue. FLcanmodel
achieve fault detection, identification, and localization, has the potential for a wide range
nonlinear functions and simplify the control of dynamic systems. Natural languages,
of applications in power systems.
controlsystems,andclusteringinnetworksaresomeoftheapplicationsofFL.FLhasalso
T.Takagi et al. [21] developed an equation based on the electrical equations of the
beenusedinpowersystemsforcontrolandanalysis[23–26]. Forinstance,theimpactofthe
loop formed by a single-phase to ground resistive fault, using only the wavelet readings
lightningstrikeonafaultlocationinatransmissionpowersystemwasdeterminedusing
from one end of the transmission line. They localized faults in a transmission line by sep-
FL[27]. TheauthorsfoundthattherateoffalseormissedalarmsisminimalfortheFL
arating the circuit into two equivalent circuits: one prior to the fault and the other during
method,whileFL-basedandSCADAmethodshavecomparableperformanceforlightning
the fault. Each of these gives an equation about the current and the voltage. On the other
strike trips, and the correlations of 100 km line trips are equivalent for the conducted
hand, modern techniques can be classified into control theory, Artificial Intelligence (AI),
experimentthroughoutthetimeinterval.
and communication networks.
Theauthorsin[28]usedafuzzyinferencesystemtodetect,classify,andlocalizeafault
sectionincombinedtransmissionlinesandundergroundpowercables. Theirapproach
3.1. Control Theory
depends on ten adaptive networks based on a fuzzy inference system (ANFIS), using
Control theory refers to the field focusing on controlling dynamic systems and en-
suring the stability of the operating systems without delay. Next, we discuss fuzzy logic
and Boolean logic as well-known methods in control theory.

Computation2022,10,144 7of19
post-faultvoltageandcurrentmeasurements. ANFIS1isusedtoclassifythefaulttype.
Thefundamentalfrequencyamplitudeofthethree-phasecurrentsplustheneutralcurrent
will be the input for ANFIS2. The output has the formats A, B, C, and G, representing
thethreephasesandtheground. AnyoutputA,B,orCcloseto1referstoafaultinthat
phase. Similarly,ifGclosesto1,thefaultinvolvestheground. Thefourshort-circuitfault
types,namelyLL,LLL,LLG,andLG,canbeoverheadorunderground. Thus,theeight
ANFISs are trained for each type to locate the faulty section. To classify overhead and
undergroundfaults,sampledvalues(withinonecycle)ofapost-faultpeakcanbeused
toestimatetheinputsofANFISTheauthorstestedtheirproposedalgorithmtoensure
accuracy,conductingseveralscenariosincludingshort-circuitfaulttypes,faultinception
angles,andimpedances. Themaximumlocationerrorofafaultysectionisbelow0.07%.
However, consideringtheseparametersincreasesthecomplexityandlearningtimefor
differenttrainingsets.
3.1.2. BooleanLogic
Booleanlogicissimplerthanfuzzylogicasthevariableshavetruthvaluesoftrue
or false. It provides only a binary value representation: 0 for false and 1 for true. This
representationisdifferentfromfuzzylogic,wherevaluescanbeanyrealvaluebetween
0 and 1, and is also different from ordinary algebra, where the variables can have any
numerical value [29]. The three main operators in Boolean logic are conjunction (∧),
disjunction (∨), and negation (¬). Boolean logic played a significant role in the digital
revolution,especiallyindigitalcircuitdesignandinformationcommunication. Boolean
logicapplicationssuchaserrorpropagationmodelingandcomputationalgeometryare
appliedtoapproximatelyamolecularsurfacearea[30]. Booleanlogicwasimplementedin
powersystemsanalysisalongwithothermethodstodiagnosefaults[31].
3.2. ArtificialIntelligence
Next,wediscussAI-basedtechniques,includingprobabilisticmethodsforuncertain
reasoning,evolutionarycomputation,statisticallearningmethods,andneuralnetworks.
3.2.1. ProbabilisticMethodsforUncertainReasoning
Therearemanyprobabilisticmethodsforuncertainreasoningandincludethehid-
denMarkovmodel(HMM),Bayesiannetworks,andKalmanfilter. HMMisastatistical
methodbasedontheMarkovprocesswithhiddenstates. UsingHMM,researchersseek
torecoverthesequenceofhidden(unobserved)statesfromtheobservedgenerateddata.
TherearemanyapplicationsofHMM,suchasspeechrecognition,proteinstructurepre-
diction, genome-sequence analysis, and image classification [32]. HMM has been used
recentlyinthefaultdiagnosisofpowersystems,forexample,todetectpowerfaultsthat
lead to islanding in a smart grid [33,34]. In [35], the authors formulate the problem of
detectingatransmissionlinefaultusingHMM.Theyproducedaprobabilisticestimation
of the transmission line status using inference and particle filtering. This approach is
robusttomeasurementerrorsofphasormeasurementunits(PMU).TheproposedHMM-
basedalgorithmsoutperformotheralgorithmsfornoiselevelsof0.1,0.15,and0.2with
detection percentages of 99, 95, and 91, respectively. However, using HMM has two
drawbacks: the expensive computational complexity and the high amount of memory
required,posingascalabilityissue. Althoughthisapproachclaimstoreducecomputational
complexity,itisclearthatthereisatradeoffbetweencomputationalcomplexityandfault
detectionaccuracy.
Similarly,Bayesiannetworks(BNs)havebeenusedsuccessfullytocreateconsistent
probabilisticrepresentationsofuncertainreasoninginmanyfields,suchasaudio-visual
speechrecognition,medicaldiagnosisfrompartiallycorrectdata,biologicalinteractions,
andmanyothers[36]. BNsalsolocatefaultsintransmissionpowersystems[37,38]. Fault
diagnosisBN-basedmodelscanworkwithuncertainorincompletedatarelatedtoapower
faultanalysissystem[39]. In[39],theinitialparametersoftheBNdependonhistorical

Computation2022,10,144 8of19
inputsfromdomainexperts, whicharefurtherrefinedusinganerrorbackpropagation.
Theproposedsystemusesthefollowingevaluationcriteria: (1)ifthefaultbeliefdegreeof
anelementis>0.7,thiselementisfaulty;(2)ifthedegreeofanelementisintherangeof
[0.15–0.7]inclusive,thiselementmaybefaulty;and(3)ifthedegreeofanelementis<0.15,
thiselementisnormal. Thisapproachisefficient,scalable,andindependentofnetwork
topology;hence,itcanbeappliedtoanylarge-scaletransmissionpowersystem. However,
therearesomeconcernsregardingthecomputationalcostofrunningthisapproach.
On the other hand, the Kalman filter (KF) is an optimal estimation algorithm for
variablesofinterestthatcannotbedirectlymeasured. Italsoassessesthestateofthesystem
fromindirectandnoisymeasurements. KFisusedinmanyways,suchasspacecraftto
estimatetheiraltitudeandlocalizeobjectssuchasmobilerobotsanddriverlessvehicles[40].
Inmanydomains,KFhasalsobeenadoptedinmanyresearchstudiesconcerningpower
systems[41–43]. Recently,Netoetal.[44]presentedaKF-basedsolutiontolocatefaultsin
transmissionlineswheremagneticfieldsproducedbycurrentsignalsaremeasuredusing
magneto-resistivesensorsinstalledattransmissionlineterminals. Theproposedsolution
uses the extended KF (EKF) to process these measurements and employs a travelling
wave approach to localize the fault. The proposed algorithm performs approximately
250multiplicationsand400additionsforanewsampleprovidedbythesensors.
Consequently, accuracy is limited by the sampling frequency. The minimum and
maximumlocalizationerrorsoftheproposedsolutionare0mand107m,withanaverage
faultlocationof26mandastandarddeviationof16m,faultresistanceof229Ωandafault
inceptionangleof245◦. Furthermore,thisapproachrequireshighlysynchronizedclocksto
Computation 2022, 10, 144 calculatethetravellingwavetimeandachieveaccuratelocalization.9 of 20
3.2.2. ArtificialNeuralNetworks
detecting a fault, the output is binary, indicating whether there is a fault or not, while
Anartificialneuralnetwork(ANN)isapowerfultoolthathasbeenusedforalong
classifying the fault type requires more outputs. On the other hand, a fault location can be
timeinmanyapplicationsspanningpatternrecognition,featureextraction,noisereduction,
referred to using distance measurements from a specific line terminal or a block/section
whearne dthpe rfeadulitc htiaosn o.cAcunrreAdN. TNhei sfotrrmaeinr eredq,uuirseus aolnlyly ionnae osuutppeurtv, wisheidle mthae nlanteterr (meaacyh setofinputsis
requaisrseo mciualttiepdle wouittphutths teo dideesnirtiefyd toheu ftapuultt )b,lobcyk/fseecetdioinn.g itwithmanyinputexamples. Oncethe
AANNNN icsansu bfefi ecitiheenrt lsyhatlrloawin oerd d,eietpc.a Mnossot lfvaueltd ainffaelyresins ttetcehsntisqcueens aforlilooswt ah sahnaltlhowos eitwastrained
learwniintgh a.pIptrcoaanche [v46e,n47]g. eSneveerraalli rzeesetahrechl epaaprnerisn hgavbey epmrpolodyuecdi nAgNNso flourt fiaounlts atnoalnyseiws datathathave
in the power grid [48–51]. A feed-forward 3-layer ANN has been designed to estimate the
notbeenpartofthetrainingphase[45]. Figure6showsthesimplestformof1-perceptron
resistance and location of a faulty 3-phase transmission line using voltage and current
ANN,whereX andW representtheinputandweight,respectively. Sigmaisthelearning
readings of a single teirminal [5i2]. Similar to Takagi’s method [21], Ref. [52] it requires the
functionfollowedbytheactivationfunction, whichendswiththeoutput. ANN-based
voltage and current parameters prior to and during the fault. Each value of these two
paratemcehtenrisq huaess twfoor pfaarutsl:t ryeatlr aannds mimiasgsiinoanryl.i nThese tcoatanl hnuamndbeler oofn inepourtsm foor rAeNsNte piss 1o5,f faultdiagnosis.
wheIrne oththe enruwmoberrd so,f AhiNddNen-b naosdeeds ties c8h, n11iq, uore s12d feotre cwt,eackla, smsiefdyi,uomr, loorc astlrioznegt hsoeufracue lt. Fordetecting
impaedfaanuclet,, rtehsepeocutitvpeluyt. Tishbe ionuatrpyu,tsin adreic tahtei nfaguwlt hreestihsteanrcteh eanred itshea ffaauultl tloocratnioont ,inw hileclassifying
terms of distance from the used terminal of the transmission line. The result shows the
thefaulttyperequiresmoreoutputs. Ontheotherhand,afaultlocationcanbereferred
high performance of this technique with 1% precision for the fault location and 3% for the
to using distance measurements from a specific line terminal or a block/section where
fault resistance. Although this result outperforms the conventional methods, it is unclear
thefaulthasoccurred. Theformerrequiresonlyoneoutput,whilethelattermayrequire
whether or not the technique in [52] will hold for high values of resistive fault with
chanmguesl tiinp sloeuorucet pimuptsedtaonicdee. ntifythefaultblock/section.
x1
w1
x2
w2
∑ Activation Function
Output
Inputs
wn
xn
FiguFrieg 6u. r1e-p6e.rc1e-pptreornce ApNtrNo.n ANN.
On the other hand, deep learning is a relatively new dimension in ANN, with the
most recent breakthrough in 2006. Deep learning enables unsupervised feature learning,
pattern analysis, and classification. The fundamental principles of deep learning can be
summarized as follows [53]: (1) Unsupervised learning is used to pre-train each layer; (2)
unsupervised training of one layer at a time, on top of the previously trained ones, where
the representation learned at each level is the input for the next layer; and (3) supervised
training used to fine-tune all the layers (in addition to one or more additional layers ded-
icated to producing predictions). Recently, attention has been drawn to applying deep
learning to fault diagnosis in a power transmission system [54–57]. In [49], the authors
developed a technique based on deep learning where data is extracted from a power sys-
tem control center and preprocessed before the deep learning network training. Then
auto-encoders are used to process the data, and hidden features are evaluated to conclude
the existence of the fault. If a fault is detected, the second step is to classify the fault type,
where trained stacked auto-encoders are used for training a deep learning network. For
proper parameter setting, the diagnosis accuracy rate is more than 80%. This means the
number of hidden layers and epochs influences the accuracy rate of diagnosis. For exam-
ple, large numbers of hidden-layer units and epochs might enhance the accuracy, but
would also cost more time for training, influencing on-the-fly fault diagnosis.

Computation2022,10,144 9of19
ANNcanbeeithershallowordeep. Mostfaultanalysistechniquesfollowashallow
learningapproach[46,47]. SeveralresearchpapershaveemployedANNforfaultanalysis
in thepower grid[48–51]. A feed-forward 3-layerANN has beendesigned toestimate
theresistanceandlocationofafaulty3-phasetransmissionlineusingvoltageandcurrent
readings of a single terminal [52]. Similar to Takagi’s method [21], Ref. [52] it requires
the voltage and current parameters prior to and during the fault. Each value of these
twoparametershastwoparts: realandimaginary. ThetotalnumberofinputsforANN
is15,wherethenumberofhiddennodesis8,11,or12forweak,medium,orstrongsource
impedance, respectively. The outputs are the fault resistance and the fault location in
termsofdistancefromtheusedterminalofthetransmissionline. Theresultshowsthe
highperformanceofthistechniquewith1%precisionforthefaultlocationand3%forthe
faultresistance. Althoughthisresultoutperformstheconventionalmethods,itisunclear
whetherornotthetechniquein[52]willholdforhighvaluesofresistivefaultwithchanges
insourceimpedance.
On the other hand, deep learning is a relatively new dimension in ANN, with the
mostrecentbreakthroughin2006. Deeplearningenablesunsupervisedfeaturelearning,
pattern analysis, and classification. The fundamental principles of deep learning can
besummarizedasfollows[53]: (1)Unsupervisedlearningisusedtopre-traineachlayer;
(2)unsupervisedtrainingofonelayeratatime,ontopofthepreviouslytrainedones,where
therepresentationlearnedateachlevelistheinputforthenextlayer;and(3)supervised
training used to fine-tune all the layers (in addition to one or more additional layers
dedicatedtoproducingpredictions). Recently,attentionhasbeendrawntoapplyingdeep
learningtofaultdiagnosisinapowertransmissionsystem[54–57]. In[49], theauthors
developed a technique based on deep learning where data is extracted from a power
systemcontrolcenterandpreprocessedbeforethedeeplearningnetworktraining. Then
auto-encodersareusedtoprocessthedata,andhiddenfeaturesareevaluatedtoconclude
theexistenceofthefault. Ifafaultisdetected,thesecondstepistoclassifythefaulttype,
wheretrainedstackedauto-encodersareusedfortrainingadeeplearningnetwork. For
properparametersetting,thediagnosisaccuracyrateismorethan80%. Thismeansthe
numberofhiddenlayersandepochsinfluencestheaccuracyrateofdiagnosis. Forexample,
largenumbersofhidden-layerunitsandepochsmightenhancetheaccuracy,butwould
alsocostmoretimefortraining,influencingon-the-flyfaultdiagnosis.
FeatureExtraction
Featureextractionisamajorstepforfaultanalysisinpowergrids,withoutwhichmost
fault-analysismethodsmaynotbesetupcorrectly. AI-basedtechniquesusetheextracted
featuresfortrainingAImodels. Inpowergridanalysis,currentandvoltagemeasurements
are usually collected in samples and forwarded to a feature extraction technique. The
extractedfeaturesarethenusedtodetect,classify,andlocatefaults. Forexample,frequency
measurements could be collected and decomposed in a time-frequency form to extract
time-frequencyfeatures. Theextractedfeaturescanthenbeusedbyclusteringtechniques
topartitionthepowergridanddeterminethefaultlocation[58]. Thescopeofthistopicis
largeanddiverse,andwehighlighteditssignificanceandapplicationmultipletimesin
thetext.
3.2.3. EvolutionaryComputation
Evolutionarycomputationisafieldbasedontrial-and-errorwithstochasticoptimiza-
tion. Perhaps,geneticalgorithms(GA)arethemostcommonclassinthelargercategoryof
evolutionarycomputation. Theyareinspiredbynaturalselectiontheory[59],involvingthe
followingsteps:
(1) Aninitializedpopulationofpotentialsolutionsisrandomlygenerated;
(2) Thefitnessfunctionisevaluated;
(3) Ifitsatisfiestheoptimization/terminationcriteriaorconstraints,thebestoutputis
generated;otherwisetheprocessisterminated;

Computation2022,10,144 10of19
(4) The population is subjected to natural selection in order to select the best-fitting
parentsforbreeding;
(5) Tocreateanewgeneration,geneticoperatorssuchascrossoverandmutationareused;
(6) Gotostepnumber(2).
Crossover or recombination combines two or more parts of candidate solutions to
breed a new one. On the other hand, mutation performs local modifications to a solu-
tion [60]. The last two steps, selection and generation, are iteratively run until the best
candidatesolutionisselected.
ResearchershaveemployedGAstoanalyzefaults[61,62]andsolveotherproblems
inpowergrids,suchasmanagingmicrogridenergy[63]andachievinganoptimaldesign
ofdistributionpowerlines[64]. GAcanbeemployedtolocatefaultsintransmissionlines
using the data from the two-terminal transmission line [65]. The authors in [65] utilize
adistributedtime-domainmodelofapowertransmissionlinetoderiveafaultlocation
formula. Theobjectivefunctionreflectstherelationshipbetweenthederivedvoltagesfrom
bothterminals. Therefore,thegoaloftheproposedGAistominimizethelocationerrorby
collectingsynchronousmeasurementsofpost-faultvoltageandcurrentfromthetwoends
oftheline. Forafaulthappening100kmfromtheSterminal,theproposedGApresentsa
faultdistanceof99.882kmfromtheSterminal,whichisveryclosetotheactualfaultpoint
(i.e.,−0.118%erroroffaultlocation).
3.2.4. StatisticalLearningMethods
Statisticallearningmethodsincludedecisiontree(DT)andsupportvectormachine
(SVM).DTisagraphwithnocycles,acommonlyusedpredictivestatisticalmodel,espe-
ciallyforclassifications[66]. Itcontainsdecisionsandpossibleoutcomes. Safetyevaluation
andclassifiersonprivatedatabasesaresomeapplicationsofDTs[67]. ADT-basedmethod
hasbeendevelopedtoclassifyafaulttypeinasingle-circuittransmissionline[68]. TheDT
istrainedusingtheoddharmonics(uptothe19th)ofthemeasuredsignals. Althoughthe
resultispromising,withaclassificationaccuracyofacycle’squarter,thereliabilityisan
issueasthetraininginputscouldbeerroneous. Furthermore,DTmethodsusuallypose
computationalcomplexity,whichhasnotbeenincludedin[68].
Likewise,SVMisaclassificationtechniquethatbelongstostatisticallearningtheory.
One of the most effective linear classifiers uses kernel tricks to create a nonlinear clas-
sifier [69]. It is a supervised learning method to train machines to learn independently
withoutexplicitstaticprogramminginstructions. ApplicationsofSVMcovermanyfields
suchasmedicinetoclassify,forinstance,cancertissue,financialforecasting,andtextclassi-
fication[70],amongmanyothers. ResearchershaveusedSVMsuccessfullyinfaultanalysis
inpowersystems[71–75]. SVMcanalsobeusedtolocalizefaultsinpowertransmission
systemswithhighaccuracy(upto99%)[76].
3.3. CommunicationNetworks
3.3.1. GlobalSystemforMobileCommunications(GSM)
GSMisatelecommunicationstandarddevelopedbytheEuropeanTelecommunication
StandardInstitute(ETSI).Itisconsideredthesecondgeneration(2G)ofcellularnetworks
used by mobile devices [77]. GSM has been used in power fault analysis [78,79]. For
instance,in[79],atechniquehasbeenproposedtodetectandclassifyafaultytransmission
line. Theproposedsystemconsistsofprotectiveequipmentsuchasrelays,switchbreakers,
reclosers, voltage sensors, an 8-bit microcontroller, a GSM module, and a LED display.
Sincethemicro-controllerworksona5Vvoltagelevelandserialcommunicationwiththe
computersystemworksona12Vvoltagelevel,aMAX232ICisusedtoboostthesignal
from5Vto12V.Thesensedfaultsignalisdeliveredtothemicrocontrollertoanalyzethe
characteristicsofthesignalintermsofcurrentandvoltagereadings. Themicrocontroller
willdetectandclassifythefaultonceitoccurs. GSMwillbeusedtosendamessagetothe
personinchargeofanyexistingfault. Finally,themicrocontrollersendsasignaltorelays
andswitchbreakerstoisolatethefaultysection.

Computation2022,10,144 11of19
3.3.2. WirelessSensorNetworks(WSNs)
A WSN comprises sensor nodes with sensing functionalities to monitor physical
propertiessuchasvoltage,humidity,temperature,pressure,andmovingobjects. Asensor
hasasmallprocessor,abatteryasapowersupply,memory,andashort-rangewireless
transceiver[80]. Thecollectedsenseddataistypicallypropagatedtowardsthebasestation
Computation 2022, 10, x FOR PEER REVIEW 12 of 21
(BS)inamulti-hopfashiontoprovidethewholepictureofthetargetregion/object. For
example, Figure 7 shows a path of sensed data from sensor nodes, aggregated at BS,
thentransmittedtotheend-userviaacommunicationmediumsuchasTCP/IPprotocols
orGPRS.
Communication
Medium
User
Sensor Node
Base Station
FFiigguurree 77.. AAnn iilllluussttrraattiioonn ooff aa ddaattaa ffllooww iinn WWSSNN..
4. SumSinmcaerWy oSfN Tihseo Anenaolfytshise TleeacdhinnigqIuoeTs enablers,researchersoftenusethetermIoTto
indicateWSN[19,81]. WSNshavebeenappliedtosmartbuildings,smartvehicles,health
Table 1 summarizes the fault analysis techniques. In addition to the remarks, the
care,environmentalstudies,security,trackingobjects,andagriculture[80]. Theycanalso
third column denotes whether the corresponding technique employs one terminal or two
playakeyroleinmonitoringthestatusoftransmissionlinesinareal-timemanner[82,83].
transmission line terminals to achieve its objective/task of fault analysis. The following are
Forexample,[82],aWSN-basedsystemhasbeenproposedtomonitorpowertransmission
some key points that we make regarding these techniques: (i) There is an increasing num-
lines. Theproposedsystemcanbedividedintotwosubsystems: Monitoringandoperation.
ber of proposals that employ modern techniques such as ANN and machine learning (ML)
Inthemonitoringsubsystem,heterogeneoussensorswithdifferentvisionandmagnetic
methods. However, even this sophisticated tool can fail to catch some transient events.
inductioncapabilitiesaredeployedontransmissiontowers. Thesesensorscollectdataona
For example, the voltage drop due to a generator’s malfunction or overloading usually
real-timebasisandsendittotheoperationsubsystem. Thecollecteddataistransmitted
impacts the three phases uniformly. ANN is usually trained to detect the abnormal volt-
wirelesslythroughthetransmissionlinewithupto138kVofpower. Thus,thereisnoneed
age and current differences between these phases due to a fault in one or more of them.
forcellularoropticalcommunicationtodeliverthesenseddatatotheoperationsubsystem
Therefore, there is a need for further feature engineering to reflect on special transient
foranalysis. Theresultsaredisplayedthroughagraphicaluserinterface,showingreal-time
events; (ii) sensors are vital devices for data acquisition for almost all modern technolo-
monitoringandfaultdetection. Thedisplayshowscarbonmonoxide(partspermillion),
gies. Thus, cybersecurity is of paramount importance to grid operators. It is critical be-
temperature(Celsius),pressure,spanandstructureimages,andluminosity.
cause cyber attackers could manipulate the readings of voltage and currents to be per-
c4e.iSvuedm ams anroyromfaTl hwehAilne,a ilny sfiascTt,e tchhenreiq ius easn imminent failure (i.e., increase the false nega-
tives) or vice versa. During normal loading, current and voltage measurements collected
Table 1 summarizes the fault analysis techniques. In addition to the remarks, the
by sensors are almost balanced. However, these measurements fluctuated in faulty inci-
third column denotes whether the corresponding technique employs one terminal or
dents, indicating an unbalanced loading state; and (iii) localization-based techniques that
twotransmissionlineterminalstoachieveitsobjective/taskoffaultanalysis.Thefollowing
uatrieliszoem theek teimyep odiinfftesrtehnactew ofe tmraavkeellirnegg asridgninaglst huesusealtleyc hfancieq aucecsu:r(ai)cyT hisesrueeiss daunei ntocr tehaes iinng-
ancucmurbaecryo offp tirmopeo msaelasstuhraetmemenptlso. yFumrothdeerrmnoterech, tneicqhuneisqsuuecsh thaastA coNllNecat npdowmearc-hreinlaeteleda rrenaindg-
i(nMgLs )atm theteh towdos .enHdosw oef vpeorw, eevr elnineths ipsrsoovpidheis mticoartee dactcouorlatcea nfaufalitl lotocaclaiztachtiosno mtheantr iamnpsieedn-t
aenvceen-tbsa.sFeodr teecxhanmiqpulee,st. hevoltagedropduetoagenerator’smalfunctionoroverloading
usuallyimpactsthethreephasesuniformly. ANNisusuallytrainedtodetecttheabnormal
Tvaobltlaeg 1e. aSnudmmcuarrrye noft tdhieff aenreanlycseiss bteecthwneiqeunetsh ceosnecperhnainsegs thdeu emteothaofdasu clotninsidoenreedo rinm thoere suorfvtehyeemd .
works. It illustrates the tasks these techniques perform (i.e., detection, classification, or localization).
The “General Remarks” column shows the advantages/disadvantages of the corresponding tech-
nique, and whether it uses one terminal or two to achieve its tasks.
Fault Analysis Classifica- Locali-
Work Detection General Remarks
Method tion zation
1-terminal; the assumption of the angles’ equal-
Conventional [21] 
ity may lead to erroneous locations

Computation2022,10,144 12of19
Therefore, there is a need for further feature engineering to reflect on special transient
events;(ii)sensorsarevitaldevicesfordataacquisitionforalmostallmoderntechnologies.
Thus, cybersecurityisofparamountimportancetogridoperators. Itiscriticalbecause
cyberattackerscouldmanipulatethereadingsofvoltageandcurrentstobeperceivedas
normalwhile,infact,thereisanimminentfailure(i.e.,increasethefalsenegatives)orvice
versa. Duringnormalloading,currentandvoltagemeasurementscollectedbysensorsare
almostbalanced. However,thesemeasurementsfluctuatedinfaultyincidents,indicating
anunbalancedloadingstate;and(iii)localization-basedtechniquesthatutilizethetime
differenceoftravellingsignalsusuallyfaceaccuracyissuesduetotheinaccuracyoftime
measurements.Furthermore,techniquesthatcollectpower-relatedreadingsatthetwoends
ofpowerlinesprovidemoreaccuratefaultlocalizationthanimpedance-basedtechniques.
Table1. Summaryoftheanalysistechniquesconcerningthemethodsconsideredinthesurveyed
works.Itillustratesthetasksthesetechniquesperform(i.e.,detection,classification,orlocalization).
The“GeneralRemarks”columnshowstheadvantages/disadvantagesofthecorrespondingtechnique,
andwhetheritusesoneterminalortwotoachieveitstasks.
FaultAnalysis
Work Detection Classification Localization GeneralRemarks
Method
[21] (cid:51) 1-terminal;theassumptionoftheangles’
equalitymayleadtoerroneouslocations
[84] (cid:51) 2-terminal;phasormeasurementunits(PMUs);
toleranttotime-synchsignalandPMUlosses
[85] (cid:51) 1-terminal;EHVtransmissionlines;haslow
efficiency—Bettertosynchdatafrombothends
Conventional
Voltagemeasurementsandnetworkbus
[86] (cid:51) (cid:51) admittancematrix;transientstability
assessmentproblem
2-terminalpre-faultandpost-faultofcurrent
[87–89] (cid:51) andvoltage;usingawide-areameasurement
systemtohandlealarge-scaleofdatafor
accuratefaultlocation
1-terminal;detectedusingconventional
[90] (cid:51) discretewavelettransform;moreprominent
thanothervarioustypesofmotherwavelets
1-endmeasurements;usingbothvoltageand
[91] (cid:51) currentsignals;testedona380kVprototype
powersystem;findthefaultlocationsina
Wavelet shorttime
2-terminaltransmissionline;awavelet
[13] (cid:51) entropy-basedmethod;accuratewithafair
degreeofnoisetolerance
2-terminaltransmissionline;GPSforsynch;
[92] (cid:51) (cid:51) (cid:51) efficientapproachwithafair
degreeofaccuracy
Overheadorunderground;localizationby
section;evaluatedunderdifferentfault
[28] (cid:51) (cid:51) (cid:51) locations,inceptionanglesandseveralfault
resistances;accuratebutrequiresmanyANFIS
FuzzyLogic networkstowork
Faultlocationscausedbylightningstrike;
[27] (cid:51) gathercurrentvaluesfromSCADAsystem;
requires216setsofrulestocreatean
expertdatabase

Computation2022,10,144 13of19
Table1.Cont.
FaultAnalysis
|     | Work | Detection | Classification | Localization | GeneralRemarks |
| --- | ---- | --------- | -------------- | ------------ | -------------- |
Method
Hidden
Phasormeasurements;detectfaultsina
| Markov | [33,35] | (cid:51) |     |     |     |
| ------ | ------- | -------- | --- | --- | --- |
shorttime
process
Single-phasegroundingaccidents;“Storm”,
“Aging”,and“Icing”arethemostcritical
(cid:51)
|          | [37] |     |     |     | hazardsofsingle-phasegrounding,          |
| -------- | ---- | --- | --- | --- | ---------------------------------------- |
| Bayesian |      |     |     |     | respectively;however,sensitivityanalysis |
requiresfurthervalidation
Networks
Faultsectionlocalization;feasibleandefficient;
(cid:51)
|     | [39] |     |     |     | however,thelackofpriorknowledgeofthe |
| --- | ---- | --- | --- | --- | ------------------------------------ |
domainexpertsimpactslocationaccuracy
Estimatethepre-andpost-faultstateof
|     | [43] | (cid:51) |     |     |     |
| --- | ---- | -------- | --- | --- | --- |
voltagesandcurrents
2-terminalwithextendedKF;robustnessand
KalmanFilter
|     |     |     |     | (cid:51) | accuracyoflocalizationaresubjecttosampling |
| --- | --- | --- | --- | -------- | ------------------------------------------ |
[44]
frequency;timesynchisrequiredbetween
bothterminals
2-terminal;highdetectionandclassification
|     | [46,47] | (cid:51) | (cid:51) |     |     |
| --- | ------- | -------- | -------- | --- | --- |
accuracy
|     | [52] |     |          | (cid:51) | 1-terminal;smalllocalizationerror(upto5%)   |
| --- | ---- | --- | -------- | -------- | ------------------------------------------- |
|     |      |     | (cid:51) | (cid:51) | 2-terminal;asinglehiddenlayerissufficientto |
[93]
learnandclassifyandlocalizefaults
|     |      | (cid:51) | (cid:51) |     |                                     |
| --- | ---- | -------- | -------- | --- | ----------------------------------- |
|     | [94] |          |          |     | Utilizesamplesofcurrentsandvoltages |
1-terminal;theclassifierissuitedfor
|     | [95] |     | (cid:51) |     |     |
| --- | ---- | --- | -------- | --- | --- |
classifyingfaultsindouble-circuitlines
1-terminalpre-faultandpost-faultdata;
|     |      |     | (cid:51) | (cid:51) |                                          |
| --- | ---- | --- | -------- | -------- | ---------------------------------------- |
|     | [96] |     |          |          | feasibleandtestedagainstdifferenttypesof |
faultsatseveraloperatingconditions
ANN
2-terminal;maximumlocalizationerrorless
|     | [97] |     |     | (cid:51) | than2%;errorcouldbefurtherreducedif |
| --- | ---- | --- | --- | -------- | ----------------------------------- |
longertrainingtimeisapplied(>2.5min)
LG,LL,andLLG;reliableandattractive
|     |      | (cid:51) | (cid:51) |     |                                       |
| --- | ---- | -------- | -------- | --- | ------------------------------------- |
|     | [98] |          |          |     | approachforprotectingrelayingsystemin |
powertransmissionsystems
Deeplearningneuralnetwork:usestacked
auto-encoders(SAE)totrainthedeepmodel;
increasethereliabilityandstabilityofpower
|     |      | (cid:51) | (cid:51) |     |                          |
| --- | ---- | -------- | -------- | --- | ------------------------ |
|     | [49] |          |          |     | systemsand;theaccuracyis |
parameter-dependent—properselectionofthe
numbersofhiddenlayersandepochsisvital
foranaccuracyofaround80%
Pre-faultformaintenancepurposes;efficient
(cid:51)
|     | [59] |     |     |     | methodtosolvecomplexnon-linear |
| --- | ---- | --- | --- | --- | ------------------------------ |
optimizationproblems
Genetic
| Algorithm |     | (cid:51) |     |     | 2-terminaltransmissionline;significant |
| --------- | --- | -------- | --- | --- | -------------------------------------- |
[65]
| (GA) |     |     |     |     | maintenancesavingsofpowersystems |
| ---- | --- | --- | --- | --- | -------------------------------- |
Measurementofshort-circuitcurrentat
|     | [99] |     |     | (cid:51) |     |
| --- | ---- | --- | --- | -------- | --- |
sendingterminal;highdegreeofaccuracy

Computation2022,10,144 14of19
Table1.Cont.
FaultAnalysis
Work Detection Classification Localization GeneralRemarks
Method
[66] (cid:51) Detectandidentifylinesthatleadto
cascadingfailure
DecisionTree [68] (cid:51) (cid:51) 1-terminal;robustandaccurate
[100] (cid:51) Currentsignalssampledat1920Hz;high
impedancefault
2-terminal;combinedwithGA;thesystem
[69] (cid:51) usesvoltageandcurrentphasorfromPMUto
identifyfaulttypes;uncertainphasorspose
diagnosisinaccuracy
1-terminal;highaccuracywithaverage
SupportVector [76] (cid:51) localizationoflessthan100m(in200km
Machine transmissionline,i.e.,0.05%)andthe
maximumerrorisbelow2km(i.e.,1%)
[101] (cid:51) 1-terminal;340kmlong3-phase
transmissionline
[102] (cid:51) (cid:51) (cid:51) Post-faultcurrentsamplesand
grounddetection
[77] (cid:51) CombinedwiththeInternetofThings(IoT)
[78] (cid:51) 1-terminalpre-faultandpost-faultofcurrent
andvoltage
GSM
Sensedsignalsareforwardedtoa
[79] (cid:51) (cid:51) microcontrollerfordetectionandclassification
offaults;lessaccurateinextreme
weatherconditions
UseIoTdeviceNODEMCU(Esp8266)to
detectvoltagechangeconsideringweather
[19] (cid:51) conditions;worksinareal-timemanner;
reliable,andcanbeusedtolocatefaultylines;
boundedbyWi-Ficommunicationrange
Monitoringpowerlineswithnoopticalcables
WSN orGPRS;Wi-FithroughTCP/IP;high
[82] (cid:51) overheadhandlingandprocessingof
aggregateddatafrommultiplesensorson
operationcenter;electromagneticcompatibility
isachallenge
[83] (cid:51) ZigbeeandGPRS;goodforremoteareas;the
systemhaslowpowerconsumption
Faultanalysistechniquesthatusemoderntoolsaremoreaccurateandreliablethan
theirconventionalcounterparts. Thisisduetothereal-timedatacollectionofthegridstate
andthefastdecision-makingandaction-takinguponanyfailureevent. However,thereare
variationsamongthesemoderntechniquesrelatedtotheirperformanceevaluation,such
asaccuracy. Thisisfurtherassociatedwiththeconductedexperimentandthefeasibilityof
collectingtherequiredexperimentalparameters. Forexample,ANNwasusedin[46]to
detectandidentifyfaulttypes. Theperformanceoftheproposedsolutionhasbeentested
usingameansquareerror(MSE)andconfusionmatrixwithdetectionaccuracynear100%
andaclassificationaccuracyof70%. Bothfaultyvoltageandcurrenthavebeenusedto
feedtheneuralnetwork.
Ontheotherhand, aGAproposalin[59]providesasolutiontodetectfaultylines
andmaintainthembeforehand,savingoverallcosts. Boththeprevioustechniquesseek
to detect faulty power lines proactively. The solutions are trained/implemented using

Computation2022,10,144 15of19
datasetsoffline. TheANN-basedapproachrequiresalargeenoughdatasetfortraining
purposes, while GA-based algorithms can run over a limited dataset. Achieving high
accuracycanbemorechallengingintheGA-basedapproachbecauseitrequiresacareful
designofafitnessfunction.
Furthermore,IoT-basedsolutionscanbeproposedtodetectfaultsinpowerlines[103,104].
Voltagesensorscollectvoltagereadingsfromdifferentphasesofapowerlineandsend
them to a microcontroller [19]. The microcontroller compares voltage readings and a
predefinedreferencevoltagevalue,flaggingafaultifthereisadifferencebetweenthese
values. Inanotherexample,aGSMandIoThybridschemewasproposed[77]todetectand
localizefaultyspots. Thefastdetectionandlocalizationhelptechnicianstorespondquickly
andfixfaultsbeforeimpactingtransformers. TheGSMandIoT-basedtechnologieslack
intelligence. Theirdecision-makingdependsonapredefinedthreshold,acrucialdifference
fromothermoderntechniquessuchasGAandANN,wherethesethresholdsareimplicitly
definedthroughthetraining/learningprocess. EmbeddingintelligenceintoIoTandGSM
isvitalforadaptingtovariousfaultsandpromotinginteroperabilitywithnewlyadded
componentsattheedgeandfogcomputinginfrastructures.
Inthisstudy,weemphasizetheimportanceofreliablemonitoringsystems.Challenges
andissuesexistindeployingpowermonitoringsystemsandoperatingthemcorrectly. We
discussedsomeoftheseissuesinSection3andTable1,whichcanimpacttheoperations
ofthemonitoringsystemsandreducetheaccuracyoffaultdetection,classification,and
localization. Examplesarerelatedtoshort-circuits,weatherconditions,andpowersources
tooperatethemodulesofthemonitoringsystems.
Although the advanced fault analysis techniques developed in recent years have
contributedtomorereliablepowergrids,thereareopportunitiesforfurtherimprovement.
Forexample,futureresearchshouldfocusondesigningafullyautonomousnext-generation
smartgridinwhichagridwillhaveself-recoveryandself-managementmethodsandbe
moredecentralizedtopromotesustainabilityandscalability.
5. Conclusions
This paper provides an insightful study on fault analysis in transmission power
systems. Weprovideanovelcategorizationschemeofrelevantsolutionsandproposals
in fault analysis of transmission systems according to the method used and the target
task, whether it is detection, classification, or localization of faults. As a result of this
categorization,wehaveidentifiedthemainresearchareasrequiredtobridgethegapin
theresearchbody. Wehaveidentifiedgapssuchasthelackofautomationintheproposed
solutions regarding fault analysis and seamless action-taking upon a failure incident.
Furthermore,cascadingfaultsareamajorissueinatransmissionsystem. Currentsolutions
arenotfastenoughforqualitydecision-makingtopreventfaultpropagation.
Thegeneraltrendoffaultanalysistechniquesistorelymoreonsmartdevicestocollect
data about the overall status of the grid’s components. This data enables modernized
methodssuchasML-basedandevolutionarycomputationmethodstodetect,identify,and
localizefaultsaccurately. Onarelatedemergingtopic,thedistributeddetectionofcyber-
physicalattacksonsmartpowergridsisaninterestingfutureresearchdirection. Another
directionisthedecentralizedfuturesmartgrid,inwhichfaultanalysisshouldbemore
localizedtoamicrogridthanthegridasawhole.Leveragingfogandedgecomputingalong
withartificialintelligence(AI)wouldcreateascalableandfastself-recoveringsmartgrid.
AuthorContributions: Conceptualization,Y.A.M.;Formalanalysis,Y.A.M.;Investigation,Y.A.M.
andA.H.;Methodology,Y.A.M.;Resources,A.H.andT.H.;Visualization,T.H.;Writing—original
draft,Y.A.M.;Writing—review&editing,A.H.andT.H.;fundingacquisition,Y.A.M.;Allauthors
havereadandagreedtothepublishedversionofthemanuscript.
Funding:ThisresearchwasfundedbyTheUniversityofWinnipeggrantnumber16662.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

Computation2022,10,144 16of19
References
1. Abramson,D.M.;Redlener,I.HurricaneSandy: LessonsLearned,Again. DisasterMed. PublicHealthPrep. 2012,6,328–329.
[CrossRef][PubMed]
2. Mukherjee,A.;Kundu,P.K.;Das,A.TransmissionLineFaultsinPowerSystemandtheDifferentAlgorithmsforIdentification,
ClassificationandLocalization:ABriefReviewofMethods.J.Inst.Eng.IndiaSer.B2021,102,855–877.[CrossRef]
3. Raza,A.;Benrabah,A.;Alquthami,T.;Akmal,M.AReviewofFaultDiagnosingMethodsinPowerTransmissionSystems.Appl.
Sci.2020,10,1312.[CrossRef]
4. Ferreira,V.H.;Zanghi,R.;Fortes,M.Z.;Sotelo,G.G.;Silva,R.B.M.;Souza,J.C.S.;Guimarães,C.H.C.;Gomes,S.ASurveyon
IntelligentSystemApplicationtoFaultDiagnosisinElectricPowerSystemTransmissionLines.Electr.PowerSyst.Res.2016,136,
135–153.[CrossRef]
5. Prasad,A.;BelwinEdward,J.;Ravi,K.AReviewonFaultClassificationMethodologiesinPowerTransmissionSystems:Part-I.
J.Electr.Syst.Inf.Technol.2018,5,48–60.[CrossRef]
6. Abass,A.Z.;Pavlyuchenko,D.A.;Hussain,Z.S.SurveyaboutImpactVoltageInstabilityandTransientStabilityforaPower
SystemwithanIntegratedSolarCombinedCyclePlantinIraqbyUsingETAP.J.Robot.Control(JRC)2021,2,134–139.[CrossRef]
7. Sun,C.;Wang,X.;Zheng,Y.;Zhang,F.AFrameworkforDynamicPredictionofReliabilityWeaknessesinPowerTransmission
SystemsBasedonImbalancedData.Int.J.Electr.PowerEnergySyst.2020,117,105718.[CrossRef]
8. Yang,J.;Fletcher,J.E.;O’Reilly,J.Short-CircuitandGroundFaultAnalysesandLocationinVSC-BasedDCNetworkCables.IEEE
Trans.Ind.Electron.2012,59,3827–3837.[CrossRef]
9. Guo,C.;Ye,C.;Ding,Y.;Wang,P.AMulti-StateModelforTransmissionSystemResilienceEnhancementAgainstShort-Circuit
FaultsCausedbyExtremeWeatherEvents.IEEETrans.PowerDeliv.2021,36,2374–2385.[CrossRef]
10. AlMtawa,Y.;Haque,A.Clustering-CoefficientBasedResiliencyApproachforSmartGrid. InProceedingsofthe2021IEEE
InternationalWirelessCommunicationsandMobileComputingConference(IWCMC),Harbin,China,28June–2July2021.
11. Abir,S.M.A.A.;Anwar,A.;Choi,J.;Kayes,A.S.M.IoT-EnabledSmartEnergyGrid:ApplicationsandChallenges.IEEEAccess
2021,9,50961–50981.[CrossRef]
12. Parsi,M.;Crossley,P.;Dragotti,P.L.;Cole,D.WaveletBasedFaultLocationonPowerTransmissionLinesUsingReal-World
TravellingWaveData.Electr.PowerSyst.Res.2020,186,106261.[CrossRef]
13. Huang,W.;Luo,G.;Cheng,M.;He,J.;Liu,Z.;Zhao,Y.ProtectionMethodBasedonWaveletEntropyforMMC-HVDCOverhead
TransmissionLines.Energies2021,14,678.[CrossRef]
14. Bragatto,T.;Cerretti,A.;D’Orazio,L.;Gatta,F.M.;Geri,A.;Maccioni,M.ThermalEffectsofGroundFaultsonMVJointsand
Cables.Energies2019,12,3496.[CrossRef]
15. Lee,S.R.;Ko,E.Y.;Lee,J.-J.;Dinh,M.-C.DevelopmentandHILTestingofaProtectionSystemfortheApplicationof154-KVSFCL
inSouthKorea.IEEETrans.Appl.Supercond.2019,29,1–4.[CrossRef]
16. Medeiros,R.P.;Costa,F.B.;Silva,K.M.;Popov,M.;deChavezMuro,J.J.;LimaJunior,J.R.AClarke-Wavelet-BasedTime-Domain
PowerTransformerDifferentialProtection.IEEETrans.PowerDeliv.2021,37,317–328.[CrossRef]
17. Mukherjee,N.;Chattopadhyaya,A.;Chattopadhyay,S.;Sengupta,S.Discrete-Wavelet-TransformandStockwell-Transform-Based
StatisticalParametersEstimationforFaultAnalysisinGrid-ConnectedWindPowerSystem.IEEESyst.J.2020,14,4320–4328.[CrossRef]
18. Vanitha, V.; Hussien, M.G.FrameworkforTransmissionLineFaultDetectioninaFiveBusSystemUsingDiscreteWavelet
Transform.Distrib.Gener.Altern.EnergyJ.2022,525–536.[CrossRef]
19. Namdev,P.P.;Sudhir,M.P.;Shantaram,R.D.;Goutam,M.R.;Shankar,S.V.;Palake,S.A.TransmissionLineFaultDetectionwith
MiniWeatherStationUsingIoT.AsianJ.Converg.Technol.(AJCT)2021,7,130–133.[CrossRef]
20. Kunj,T.;Ansari,M.A.;Vishwakarrma,C.B.TransmissionLineFaultDetectionandClassificationbyUsingWaveletMultiresolu-
tionAnalysis: AReview. InProceedingsofthe2018InternationalConferenceonPowerEnergy,EnvironmentandIntelligent
Control(PEEIC),GreaterNoida,India,13–14April2018;pp.607–612.
21. Takagi,T.; Yamakoshi,Y.; Yamaura,M.; Kondow,R.; Matsushima,T.DevelopmentofaNewTypeFaultLocatorUsingthe
One-TerminalVoltageandCurrentData.IEEETrans.PowerAppar.Syst.1982,101,2892–2898.[CrossRef]
22. Zadeh,L.A.FuzzyLogic.Computer1988,21,83–93.[CrossRef]
23. Bhat,A.U.Q.;Prakash,A.;Tayal,V.K.;Choudekar,P.Three-PhaseFaultAnalysisofDistributedPowerSystemUsingFuzzyLogic
System(FLS).InAdvancesinSmartCommunicationandImagingSystems;Agrawal,R.,KishoreSingh,C.,Goyal,A.,Eds.;Springer:
Singapore,2021;pp.615–624.
24. Jiao,Z.;Wu,R.ANewMethodtoImproveFaultLocationAccuracyinTransmissionLineBasedonFuzzyMulti-SensorData
Fusion.IEEETrans.SmartGrid2019,10,4211–4220.[CrossRef]
25. Soni,A.K.;Yadav,A.FaultDetectionandClassificationofGridConnectedWindFarm(DFIG)UsingFuzzyLogicController.
InProceedingsofthe2021IEEEInternationalPowerandRenewableEnergyConference(IPRECON),Kollam, India, 24–26
September2021;pp.1–6.
26. Ganthia,B.P.;Barik,S.K.FaultAnalysisofPIandFuzzy-Logic-ControlledDFIG-BasedGrid-ConnectedWindEnergyConversion
System.J.Inst.Eng.IndiaSer.B2022,103,415–437.[CrossRef]
27. Petrovic´,I.;Nikolovski,S.;Baghaee,H.R.;Glavaš,H.DeterminingImpactofLightningStrikeLocationonFailuresinTransmission
NetworkElementsUsingFuzzyDecision-Making.IEEESyst.J.2020,14,2665–2675.[CrossRef]

Computation2022,10,144 17of19
28. Sadeh,J.;Afradi,H.ANewandAccurateFaultLocationAlgorithmforCombinedTransmissionLinesUsingAdaptiveNetwork-
BasedFuzzyInferenceSystem.Electr.PowerSyst.Res.2009,79,1538–1545.[CrossRef]
29. Yousuf,H.;Zainal,A.Y.;Alshurideh,M.;Salloum,S.A.ArtificialIntelligenceModelsinPowerSystemAnalysis. InArtificial
IntelligenceforSustainableDevelopment:Theory,PracticeandFutureApplications;Hassanien,A.E.,Bhatnagar,R.,Darwish,A.,Eds.;
SpringerInternationalPublishing:Cham,Switzerland,2021;pp.231–242;ISBN978-3-030-51920-9.
30. LeGrand,S.M.;Merz,K.M.RapidApproximationtoMolecularSurfaceAreaviatheUseofBooleanLogicandLook-upTables.
J.Comput.Chem.1993,14,349–352.[CrossRef]
31. Rivera-Torres,P.J.;LlanesSantiago,O.FaultDetectionandIsolationinSmartGridDevicesUsingProbabilisticBooleanNetworks.In
ComputationalIntelligenceinEmergingTechnologiesforEngineeringApplications;LlanesSantiago,O.,CruzCorona,C.,SilvaNeto,A.J.,
Verdegay,J.L.,Eds.;SpringerInternationalPublishing:Cham,Switzerland,2020;pp.165–185;ISBN978-3-030-34409-2.
32. Li,J.;Najmi,A.;Gray,R.M.ImageClassificationbyaTwo-DimensionalHiddenMarkovModel.IEEETrans.SignalProcess.2000,
48,517–533.[CrossRef]
33. Kumar,D.;Bhowmik,P.S.HiddenMarkovModelBasedIslandingPredictioninSmartGrids.IEEESyst.J.2019,13,4181–4189.[CrossRef]
34. Hasheminejad,S.ANewHigh-Frequency-BasedMethodfortheVeryFastDifferentialProtectionofPowerTransformers.Electr.
PowerSyst.Res.2022,209,108032.[CrossRef]
35. Huang,Q.;Shao,L.;Li,N.DynamicDetectionofTransmissionLineOutagesUsingHiddenMarkovModels.InProceedingsof
the2015AmericanControlConference(ACC),Chicago,IL,USA,1–3July2015;pp.5050–5055.
36. Friedman,N.;Linial,M.;Nachman,I.;Pe’er,D.UsingBayesianNetworkstoAnalyzeExpressionData.J.Comput.Biol.2000,7,
601–620.[CrossRef]
37. Zhang,J.;Bian,H.;Zhao,H.;Wang,X.;Zhang,L.;Bai,Y.BayesianNetwork-BasedRiskAssessmentofSingle-PhaseGrounding
AccidentsofPowerTransmissionLines.Int.J.Environ.Res.PublicHealth2020,17,1841.[CrossRef]
38. Sahu,A.R.;Palei,S.K.FaultAnalysisofDraglineSubsystemUsingBayesianNetworkModel.Reliab. Eng. Syst. Saf.2022,
225,108579. [CrossRef]
39. Yongli,Z.;Limin,H.;Jinling,L.BayesianNetworks-BasedApproachforPowerSystemsFaultDiagnosis.IEEETrans.PowerDeliv.
2006,21,634–639.[CrossRef]
40. Roumeliotis,S.I.;Bekey,G.A.CollectiveLocalization:ADistributedKalmanFilterApproachtoLocalizationofGroupsofMobile
Robots.InProceedingsoftheProceedings2000ICRA.MillenniumConference.IEEEInternationalConferenceonRoboticsand
Automation,SymposiaProceedings(Cat.No.00CH37065).SanFrancisco,CA,USA,24–28April2000;Volume3,pp.2958–2965.
41. Vauhkonen,M.;Karjalainen,P.A.;Kaipio,J.P.AKalmanFilterApproachtoTrackFastImpedanceChangesinElectricalImpedance
Tomography.IEEETrans.Biomed.Eng.1998,45,486–493.[CrossRef][PubMed]
42. Zhao,J.;Netto,M.;Mili,L.ARobustIteratedExtendedKalmanFilterforPowerSystemDynamicStateEstimation.IEEETrans.
PowerSyst.2017,32,3205–3216.[CrossRef]
43. Chowdhury,F.N.;Christensen,J.P.;Aravena,J.L.PowerSystemFaultDetectionandStateEstimationUsingKalmanFilterwith
HypothesisTesting.IEEETrans.PowerDeliv.1991,6,1025–1030.[CrossRef]
44. DeOliveiraNeto,J.A.;Sartori,C.A.F.;Junior,G.M.FaultLocationinOverheadTransmissionLinesBasedonMagneticSignatures
andontheExtendedKalmanFilter.IEEEAccess2021,9,15259–15270.[CrossRef]
45. Chiroma, H.; Abdullahi, U.A.; Abdulhamid, S.M.; Abdulsalam Alarood, A.; Gabralla, L.A.; Rana, N.; Shuib, L.; Targio
Hashem,I.A.;Gbenga,D.E.;Abubakar,A.I.;etal.ProgressonArtificialNeuralNetworksforBigDataAnalytics:ASurvey.IEEE
Access2019,7,70535–70551.[CrossRef]
46. Leh,N.A.M.;Zain,F.M.;Muhammad,Z.;Hamid,S.A.;Rosli,A.D.FaultDetectionMethodUsingANNforPowerTransmission
Line. InProceedingsofthe10thIEEEInternationalConferenceonControlSystem,ComputingandEngineering(ICCSCE),
Penang,Malaysia,21–22August2020;pp.79–84.
47. Fayaz,F.;Pahuja,G.L.ANN-BasedRelayingAlgorithmforProtectionofSVC-CompensatedACTransmissionLineandCriticality
AnalysisofaDigitalRelay.RecentAdv.Comput.Sci.Commun.2020,13,381–393.[CrossRef]
48. Tiwari,S.;Palivela,H.;Kumar,P.ClassificationandIdentificationofPartialOutageinTransmissionLinesUsingDeepLearning.
InRecentInnovationsinComputing;Singh,P.K.,Singh,Y.,Kolekar,M.H.,Kar,A.K.,Gonçalves,P.J.S.,Eds.;Springer:Singapore,
2022;pp.155–167.
49. Wang,Y.;Liu,M.;Bao,Z.DeepLearningNeuralNetworkforPowerSystemFaultDiagnosis.InProceedingsofthe35thChinese
ControlConference(CCC),Chengdu,China,27–29July2016;pp.6678–6683.
50. Hossain,M.;Khan,R.;Islam,N.;Sarker,S.;Fahim,S.;Das,S.DeepLearningTechniquesforTransmissionLineFaultDiagnosis:
A Comparative Evaluation. In Proceedings of the International Conference on Automation, Control and Mechatronics for
Industry4.0(ACMI),Rajshahi,Bangladesh,8–9July2021;pp.1–5.
51. Fahim,S.R.;Sarker,S.K.;Muyeen,S.M.;Das,S.K.;Kamwa,I.ADeepLearningBasedIntelligentApproachinDetectionand
ClassificationofTransmissionLineFaults.Int.J.Electr.PowerEnergySyst.2021,133,107102.[CrossRef]
52. Chen,Z.;Maun,J.C.ArtificialNeuralNetworkApproachtoSingle-EndedFaultLocatorforTransmissionLines. IEEETrans.
PowerSyst.2000,15,370–375.[CrossRef]
53. Hinton,G.E.;Osindero,S.;Teh,Y.-W.AFastLearningAlgorithmforDeepBeliefNets. NeuralComput. 2006,18,1527–1554.
[CrossRef][PubMed]

Computation2022,10,144 18of19
54. Ullah, I.; Khan, R.U.; Yang, F.; Wuttisittikulkij, L. Deep Learning Image-Based Defect Detection in High Voltage Electrical
Equipment.Energies2020,13,392.[CrossRef]
55. Tong,L.;Hai,Z.;Xiaoming,Z.;Shidong,Z.;Zheng,Y.;Hongping,Y.;Wei,L.;Zhenliu,Z.MethodofShort-CircuitFaultDiagnosis
inTransmissionLineBasedonDeepLearning.Int.J.Patt.Recogn.Artif.Intell.2022,36,2252009.[CrossRef]
56. Teng,S.;Li,J.;He,S.;Fan,B.;Hu,S.On-LineFaultDiagnosisTechnologyandApplicationBasedonDeepLearningofFault
CharacteristicofPowerGrid.J.Phys.Conf.Ser.2021,2023,012023.[CrossRef]
57. Khodayar,M.;Liu,G.;Wang,J.;Khodayar,M.E.DeepLearninginPowerSystemsResearch:AReview.CSEEJ.PowerEnergySyst.
2021,7,209–220.[CrossRef]
58. Hassani,H.;Razavi-Far,R.;Saif,M.FaultLocationinSmartGridsThroughMulticriteriaAnalysisofGroupDecisionSupport
Systems.IEEETrans.Ind.Inform.2020,16,7318–7327.[CrossRef]
59. Mahdavi,M.;Kheirkhah,A.R.;Macedo,L.H.;Romero,R.AGeneticAlgorithmforTransmissionNetworkExpansionPlanning
ConsideringLineMaintenance.InProceedingsoftheIEEECongressonEvolutionaryComputation(CEC),Glasgow,UK,19–24
July2020;pp.1–6.
60. Sastry,K.;Goldberg,D.E.;Kendall,G.GeneticAlgorithms.InSearchMethodologies;Springer:Boston,MA,USA,2014;pp.93–117;
ISBN978-1-4614-6939-1.
61. Prasad,A.;BelwinEdward,J.;Ravi,K.AReviewonFaultClassificationMethodologiesinPowerTransmissionSystems:Part-II.
J.Electr.Syst.Inf.Technol.2018,5,61–67.[CrossRef]
62. Fahim,S.R.;Sarker,Y.;Islam,O.K.;Sarker,S.K.;Ishraque,M.F.;Das,S.K.AnIntelligentApproachofFaultClassificationand
LocalizationofaPowerTransmissionLine. InProceedingsoftheIEEEInternationalConferenceonPower, Electrical, and
ElectronicsandIndustrialApplications(PEEIACON),Dhaka,Bangladesh,29November–1December2019;pp.53–56.
63. Leonori,S.;Paschero,M.;FrattaleMascioli,F.M.;Rizzi,A.OptimizationStrategiesforMicrogridEnergyManagementSystemsby
GeneticAlgorithms.Appl.SoftComput.2020,86,105903.[CrossRef]
64. Vanderstar,G.;Musilek,P.OptimalDesignofDistributionOverheadPowerlinesUsingGeneticAlgorithms.IEEETrans.Power
Deliv.2021,37,1803–1812.[CrossRef]
65. Davoudi,M.G.;Sadeh,J.;Kamyab,K.TimeDomainFaultLocationonTransmissionLinesUsingGeneticAlgorithm. In
Proceedingsofthe11thInternationalConferenceonEnvironmentandElectricalEngineering,Venice,Italy,18–25May
2012;pp. 1087–1092.
66. Aliyan,E.;Aghamohammadi,M.;Kia,M.;Heidari,A.;Shafie-khah,M.;Catalão,J.P.S.DecisionTreeAnalysistoIdentifyHarmful
ContingenciesandEstimateBlackoutIndicesforPredictingSystemVulnerability.Electr.PowerSyst.Res.2020,178,106036.[CrossRef]
67. Du,W.;Zhan,Z.BuildingDecisionTreeClassifieronPrivateData.InProceedingsoftheIEEEInternationalConferenceonPrivacy,
SecurityandDataMining,MaebashiCity,Japan,9December2002;AustralianComputerSociety,Inc.:Darlinghurst,Australia,2002;
Volume14,pp.1–8.
68. Jamehbozorg,A.;Shahrtash,S.M.ADecision-Tree-BasedMethodforFaultClassificationinSingle-CircuitTransmissionLines.
IEEETrans.PowerDeliv.2010,25,2190–2196.[CrossRef]
69. Wu, X.; Wang, D.; Cao, W.; Ding, M.AGenetic-AlgorithmSupportVectorMachineandD-SEvidenceTheoryBasedFault
DiagnosticModelforTransmissionLine.IEEETrans.PowerSyst.2019,34,4186–4194.[CrossRef]
70. Joachims,T.TextCategorizationwithSupportVectorMachines: LearningwithManyRelevantFeatures. InProceedingsofthe
MachineLearning:ECML-98,Chemnitz,Germany,21–23April1998;Springer:Berlin/Heidelberg,Germany,1998;pp.137–142.
71. Tamrakar,A.K.;Koley,E.ASVMBasedFaultDetectionandSectionIdentificationSchemeforaHybridAC/HVDCTransmission
LinewithWindFarmIntegration.InProceedingsoftheIEEEFirstInternationalConferenceonSmartTechnologiesforPower,
EnergyandControl(STPEC),Nagpur,India,25–26September2020;pp.1–5.
72. Ahmed,Q.;Raza,S.A.;Al-Anazi,D.M.Reliability-BasedFaultAnalysisModelswithIndustrialApplications: ASystematic
LiteratureReview.Qual.Reliab.Eng.Int.2021,37,1307–1333.[CrossRef]
73. Gashteroodkhani,O.A.;Majidi,M.;Etezadi-Amoli,M.;Nematollahi,A.F.;Vahidi,B.AHybridSVM-TTTransform-BasedMethod
forFaultLocationinHybridTransmissionLineswithUndergroundCables.Electr.PowerSyst.Res.2019,170,205–214.[CrossRef]
74. Jain,A.;Archana,T.C.;Sahoo,M.B.K.AMethodologyforFaultDetectionandClassificationUsingPMUMeasurements. In
Proceedingsofthe20thNationalPowerSystemsConference(NPSC),Tiruchirappalli,India,14–16December2018;pp.1–6.
75. Liu,P.;Wang,Z.;Song,Q.;Xu,Y.;Cheng,M.OptimizedSVMandRemedialControlStrategyforCascadedCurrent-Source-
Converters-BasedDualThree-PhasePMSMDrivesSystem.IEEETrans.PowerElectron.2020,35,6153–6164.[CrossRef]
76. Salat,R.;Osowski,S.AccurateFaultLocationinthePowerTransmissionLineUsingSupportVectorMachineApproach.IEEE
Trans.PowerSyst.2004,19,979–986.[CrossRef]
77. Emi,P.S.;Sivasankari,R.;Kumar,P.R.;Prabha,R.;Jayageetha,J.;Karhikeyan,A.FaultDetectioninTransformerUsingGSM
Technology.InProceedingsofthe5thInternationalConferenceonAdvancedComputingCommunicationSystems(ICACCS),
Coimbatore,India,15–16March2019;pp.868–873.
78. Sujatha,M.S.;Kumar,M.V.On-LineMonitoringandAnalysisofFaultsinTransmissionandDistributionLinesUsingGSM.
J.Theor.Appl.Inf.Technol.2011,33,258–265.
79. Gulbhile,P.A.;Rana,J.R.;Deshmukh,B.T.OverheadLineFaultDetectionUsingGSMTechnology.InProceedingsoftheInternational
ConferenceonInnovativeMechanismsforIndustryApplications(ICIMIA),Bengaluru,India,21–23February2017;pp.46–49.

Computation2022,10,144 19of19
80. AlMtawa,Y.;Hassanein,H.;Nasser,N.TheImpactofAnchorMisplacementonSensingCoverage.InProceedingsofthe2016
IEEEWirelessCommunicationsandNetworkingConference,Doha,Qatar,3–6April2016.
81. AlMtawa,Y.;Hassanein,H.S.;Nasser,N.IdentifyingBoundsonSensingCoverageHolesinIoTDeployments.InProceedingsof
the2015IEEEGlobalCommunicationsConference(GLOBECOM),SanDiego,CA,USA,6–10December2015;pp.1–6.
82. Leoni,J.L.;Nogueira,J.M.S.;Campos,M.F.M.;Macedo,D.F.;Salvador,E.M.;Mota,V.F.S.;Resende,D.B.;Silva,V.F.;Correia,L.H.A.;
Vieira,L.F.M.;etal.Real-TimeMonitoringofTransmissionLinesUsingWirelessSensorNetworks.InProceedingsofthe2014
IEEEPESTransmissionDistributionConferenceandExposition—LatinAmerica(PESTD-LA),Medellín, Colombia, 10–13
September2014;pp.1–6.
83. Yang,Y.;Xie,G.;Xu,X.;Jiang,Y.AMonitoringSystemDesigninTransmissionLinesBasedonWirelessSensorNetworks.Energy
Procedia2011,12,192–199.[CrossRef]
84. Azizi,S.;Sanaye-Pasand,M.;Paolone,M.LocatingFaultsonUntransposed,MeshedTransmissionNetworksUsingaLimited
NumberofSynchrophasorMeasurements.IEEETrans.PowerSyst.2016,31,4462–4472.[CrossRef]
85. Ha,H.;Zhang,B.;Lv,Z.ANovelPrincipleofSingle-EndedFaultLocationTechniqueforEHVTransmissionLines.IEEETrans.
PowerDeliv.2003,18,1147–1151.[CrossRef]
86. Das,S.;Singh,S.P.;Panigrahi,B.K.TransmissionLineFaultDetectionandLocationUsingWideAreaMeasurements.Electr.Power
Syst.Res.2017,151,96–105.[CrossRef]
87. Azizi,S.;Sanaye-Pasand,M.AStraightforwardMethodforWide-AreaFaultLocationonTransmissionNetworks.IEEETrans.
PowerDeliv.2015,30,264–272.[CrossRef]
88. Galijasevic,Z.;Abur,A.FaultLocationUsingVoltageMeasurements.IEEETrans.PowerDeliv.2002,17,441–445.[CrossRef]
89. Johns,A.T.;Jamali,S.AccurateFaultLocationTechniqueforPowerTransmissionLines.IEEProc.C1990,137,395–402.[CrossRef]
90. Kim,C.-H.;Kim,H.;Ko,Y.-H.;Byun,S.-H.;Aggarwal,R.K.;Johns,A.T.ANovelFault-DetectionTechniqueofHigh-Impedance
ArcingFaultsinTransmissionLinesUsingtheWaveletTransform.IEEETrans.PowerDeliv.2002,17,921–929.[CrossRef]
91. Ekici,S.;Yildirim,S.;Poyraz,M.ATransmissionLineFaultLocatorBasedonElmanRecurrentNetworks. Appl. SoftComput.
2009,9,341–347.[CrossRef]
92. Shaik,A.G.;Pulipaka,R.R.V.ANewWaveletBasedFaultDetection,ClassificationandLocationinTransmissionLines.Int.J.
Electr.PowerEnergySyst.2015,64,35–40.[CrossRef]
93. Gracia,J.;Mazon,A.J.;Zamora,I.BestANNStructuresforFaultLocationinSingle-andDouble-CircuitTransmissionLines.IEEE
Trans.PowerDeliv.2005,20,2389–2395.[CrossRef]
94. Kezunovic,M.;Rikalo,I.DetectandClassifyFaultsUsingNeuralNets.IEEEComput.Appl.Power1996,9,42–47.[CrossRef]
95. Aggarwal,R.K.;Xuan,Q.Y.;Dunn,R.W.;Johns,A.T.;Bennett,A.ANovelFaultClassificationTechniqueforDouble-CircuitLines
BasedonaCombinedUnsupervised/SupervisedNeuralNetwork.IEEETrans.PowerDeliv.1999,14,1250–1256.[CrossRef]
96. Mahanty,R.N.;Gupta,P.B.D.ApplicationofRBFNeuralNetworktoFaultClassificationandLocationinTransmissionLines.
Transm.Distrib.IEEProc.-Gener.2004,151,201–212.[CrossRef]
97. Mazon,A.J.;Zamora,I.;Miñambres,J.F.;Zorrozua,M.A.;Barandiaran,J.J.;Sagastabeitia,K.ANewApproachtoFaultLocation
inTwo-TerminalTransmissionLinesUsingArtificialNeuralNetworks.Electr.PowerSyst.Res.2000,56,261–266.[CrossRef]
98. Tayeb,E.B.M.;Rhim,O.A.A.A.TransmissionLineFaultsDetection,ClassificationandLocationUsingArtificialNeuralNetwork.
InProceedingsofthe2011InternationalConferenceUtilityExhibitiononPowerandEnergySystems:IssuesandProspectsfor
Asia(ICUE),Pattaya,Thailand,28–30September2011;pp.1–5.
99. El-Naggar,K.M.AGeneticBasedFaultLocationAlgorithmforTransmissionLines. InProceedingsofthe16thInternational
ConferenceandExhibitiononElectricityDistribution,2001.Part1:Contributions.CIRED.,IEEConferencePublicationNo.482.
Amsterdam,TheNetherlands,18–21June2001;Volume3,pp.1–5.
100. Sheng,Y.;Rovnyak,S.M.DecisionTree-BasedMethodologyforHighImpedanceFaultDetection.IEEETrans.PowerDeliv.2004,
19,533–536.[CrossRef]
101. Wang,Z.;Zhao,P.FaultLocationRecognitioninTransmissionLinesBasedonSupportVectorMachines.InProceedingsofthe20092nd
IEEEInternationalConferenceonComputerScienceandInformationTechnology,Beijing,China,8–11August2009;pp.401–404.
102. Dash,P.K.; Samantaray,S.R.; Panda,G.FaultClassificationandSectionIdentificationofanAdvancedSeries-Compensated
TransmissionLineUsingSupportVectorMachine.IEEETrans.PowerDeliv.2007,22,67–73.[CrossRef]
103. Goswami,L.;Agrawal,P.IOTBasedDiagnosingofFaultDetectioninPowerLineTransmissionthroughGOOGLEFirebase
Database. InProceedingsofthe20204thInternationalConferenceonTrendsinElectronicsandInformatics(ICOEI)(48184),
Tirunelveli,India,3–5June2020;pp.415–420.
104. Goswami,L.;Kaushik,M.K.;Sikka,R.;Anand,V.;PrasadSharma,K.;SinghSolanki,M.IOTBasedFaultDetectionofUnderground
CablesthroughNodeMCUModule.InProceedingsofthe2020InternationalConferenceonComputerScience,Engineeringand
Applications(ICCSEA),Gunupur,India,13–14March2020;pp.1–6.