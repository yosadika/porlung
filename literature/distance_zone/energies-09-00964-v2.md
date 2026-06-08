energies
Article
Novel Auto-Reclosing Blocking Method for
Combined Overhead-Cable Lines in Power Networks
RicardoGranizoArrabé1,*,CarlosAntonioPlateroGaona1,FernandoÁlvarezGómez2
andEmilioRebolloLópez1
1 DepartmentofElectricalEngineering,ETSIngenierosIndustriales,TechnicalUniversityofMadrid,
C/JoséGutierrezAbascal,2,28006Madrid,Spain;carlosantonio.platero@upm.es(C.A.P.G.);
emilio.rebollo.lopez@gmail.com(E.R.L.)
2 DepartmentofElectricalEngineering,ETSIngenieríayDiseñoIndustrial,TechnicalUniversityofMadrid,
C/RondadeValencia,3,28012Madrid,Spain;fernando.alvarez@upm.es
* Correspondence:ricardo.granizo@upm.es;Tel.:+34-91-336-6842
AcademicEditor:MiguelCastilla
Received:25June2016;Accepted:15November2016;Published:17November2016
Abstract: Thispaperpresentsanovelauto-reclosingblockingmethodforcombinedoverhead-cable
lines in power distribution networks that are solidly or impedance grounded, with distribution
transformersinadeltaconnectionintheirhigh-voltagesides. Themaincontributionofthisnew
technique is that it can detect whether a ground fault has been produced at the overhead line
side or at the cable line side, thus improving the performance of the auto-reclosing functionality.
Thislocalizationtechniqueisbasedonthemeasurementsandanalysisoftheargumentdifferences
between the load currents in the active conductors of the cable and the currents in the shields at
thecableendwherethetransformersindeltaconnectionareinstalled,includingawaveletanalysis.
Thistechniquehasbeenverifiedthroughcomputersimulationsandexperimentallaboratorytests.
Keywords: groundfaults;protection;distributionprotections;electricaldistributionnetworks
1. Introduction
Powersystemsuseprotectiondevicestodetectandcleardifferenttypesofshortcircuits,overloads
and,ingeneral,abnormalworkingconditionsorfaultsituationsthatmightbedangeroustothefacilities
andthestabilityoftheelectricalpowersystem. Mostfaultsinpowerdistributionnetworksarelocated
inthelinesthosethattakeplaceinthemachinery,switchgearandmeasurementdevicesinstalledatthe
mainsubstations. Somedistributionlineshavetwodifferentparts:thecablelinesideandtheoverhead
lineside[1]. Protectionrelayshavetheresponsibilitytoclearfaultsthathappenintheirprotection
zonesandforthatpurpose,acloseandquiteapproximatelocationofthegroundfaultinelectrical
powersystemsisrequiredforprotectionsystems[2]. Overheadprotectionsystemshavedifferent
workingprinciplestocableprotectionsystems[3]. Atanydistributionline,theprotectionsystemmust
guaranteethepowersupplyinthemostreliableway. Forthatpurpose,therearemanyprotection
functionsimplementedtoclearupalltypesofpossiblefaultsandkeepthegridasstableaspossible.
Powerdistributionnetworksnormallyhavevoltagelevelsupto45kValthoughinsomecountriesin
Europetheirvoltagelevelscanreachupto150kV[4]. Ifthereisagroundfault,athree-phasetripping
orderwillbegiventoclearit,andalossofpowerdemandresults[5].Itisextremelyimportanttoknow
themaximumreclosingtime[6,7]torecoverpowersupplyandkeepthesystemasstableaspossible.
Whenadistributionlineisformedbycableandoverheadsections(Figure1),faultsinthecable
linesidecauseirreparabledamagebecausetheinsulationofthecablehasbeenpartiallyortotally
deteriorated: thisisthereasonwhyreclosingattemptsarenotallowed. Faultsattheoverheadline
sidearenormallyproducedbylightningstrikes[8]. Ontheotherhand,faultsintheoverheadlineside
Energies2016,9,964;doi:10.3390/en9110964 www.mdpi.com/journal/energies

EEnneerrggiieess 22001166,,9 9,,9 96644 22 ooff 2201
side are normally produced by lightning strikes [8]. On the other hand, faults in the overhead line
psiedrme ipterremcloits irnegclwosiitnhgo uwtriitshko,ubte craisuks,e btheceaauisrei ntshuel aatiior ninissunolartmioanl lyisr encoorvmeraeldlyi nreacofevwermedi lliinse cao nfedws
amnidlliaslemcoonstdosn aensde caolmndositf othneer eseicsomndu tiuf athlcearep aisc imtivuetucaolu cpalpinagcittiovoe tchoeurplilninegs. to other lines.
Overhead
Line - 1
(Rt)
Overhead
Distribution
Line - 2
Substation - A
(Rt)
Transition
(Zta) Station End
Substation - B
Overhead
Line - n (1)
(Rsa)
(Rt) (Rt) (2)
(2) (Rsb)
Figure1. Powerdistributionnetworkwithtransitioncable-overheadline. (1)Activeconductorof
Figure 1. Power distribution network with transition cable-overhead line. (1) Active conductor of
p p o o w w e e r r c c a a b b l l e e s s ; ; ( ( 2 2 ) ) S S h h i i e e l l d d s s o o f f t t h h e e p p o o w w e e r r c c a a b b l l e e ; ; ( ( R Rt t ) ) T T o o w w e e r r g g r r o o u u n n d d r r e e s s is is t t a a n n c c e e ; ; ( ( R Rs s a a ) ) G G r r o o u u n n d d r r e e s s i i s s t t a a n n c c e e o o f f
d d i i s s t t r r i i b b u u t t i i o o n n s s u u b b s s t t a a t t i i o o n n - - A A ; ; ( ( R Rssbb) ) G G r ro o u u n n d d r r e e s s i i s s t t a a n n c c e e o o f f e e n n d d s s u u b b s s t t a a t t i i o o n n - - B B ; ; ( ( Z Zt t a a) ) G G r r o o u u n n d d i i n n g g i i m m p p e e d d a a n n c c e e . .
IInn FFiigguurree 11,, tthhee eeaarrtthhiinngg ooff tthhee ccaabbllee sshhiieellddss aatt tthhee ttrraannssiittiioonn ssttaattiioonn iiss ccoonnnneecctteedd ttoo ooff tthhee
ccoorrrreessppoonnddiinngg ttoowweerr,,w whhoosseee eaarrtthhiinnggr reessisisttaanncceev vaalulueei sisr reepprreesseenntetedda assR R
t
.t. SSuubbssttaattiioonnss AA aanndd BB hhaavvee
tthheeiirr rreessppeeccttiivvee ggrroouunnddiinngg rreessiissttaanncceess RR ssaa aanndd RR ssbb.. TThhee eeaarrtthhiinngg rreessiissttaanncceess RR tt aatt eevveerryy ttoowweerr hhaavvee
nnoorrmmaallllyy sslliigghhttllyy ddiiffffeerreenntt vvaalluueess..
IIff aaf afuaultlot coccucrusrast taht etchaeb lcealbilnee lsiindee asindde isanclde airse dclueapr,eadp ouspt,- rae cploossitn-greocrldoseirnogn othrdeefra uolntc othned iftaiounlt
wcoilnldbietiaonn uwnislul cbcee sasnfu ulnresculcocseinssgfuml arneeculovseirn.gA mlsoa,ntehuevgerri.d Awlsioll, htahvee gtroidw withilslt ahnadvea tnoe wwiftahuslttacnodn da intieown
afanudltb ecoanbdleittiooncl eaanrdi tbuep aabglaei nto. Bcelesiadre itth uepse atwgaoind. isBaedsvidaen ttahgeesseo tfwuon sduicscaedsvsfaunltraegcelso soinf gumnsauncecuevssefrusl,
arnecoltohseirngis mthaenfeauctveorfsc, raenatoitnhgers iigsn tihfiec afnatcta nodf cerxetaetninsigv esidganmifiacgaenti nanthde ecxatbelnes,ibveei ndgamthaegme oinst tphreo bcaabbllee,
cboeninsegq tuheen mceostot phraovbeabtoler ecopnlasceequiteennctei rteol yh.aTvhe itsoc rirecpulamcest iatn ecnetiwreillyl.k Teehpis tchiercduimstsrtiabnucteio wnilliln keeoepu tthoef
odridsterribfuotrioanl olninget imouet wohfi leortdheerc afbolre ias rleopnlga cetidm.eT hwehreilfeo reth,eth ecadbilsec riims irneaptiloacnedof. tThheefraeufoltrein, tthhee
odvisecrrhiemaidnastiidoen oorf itnheth feaulilnt eins itdhee iosveesrsheenatdia slidtoe aolrlo iwn tthoe plirnoete scitdioen isa ensdsetnhteiaclo tnot arollloswy sttoe mprototescetinodn
aanredc tlohsei ncognotrrodle sry[s9t]e.mC utor rseenntdly ,at rheecrleosairnegd oirffdeerre n[9t]p. Croutrercetniotnlyc, rtihteerreia atroe rdeimffeorveentf rpormotesectrivoinc ecraitleinriea
wtoi trhemagorvoeu fnrodmfa suelrt.vice a line with a ground fault.
TThhiiss pprreesseennttss aa tteecchhnniiqquuee ththaat tddeetetermrmininese swwhehreer ethteh egrgoruonudn dfaufaltu lhtahs atsakteank epnlapcela cine ainn
aonveorvheerahde-acda-bclaeb lleinlein ceocnosnidseidrienrgin ga agrgoruonudnidnign gmmetehthoodd mmoostsltyly uusseedd iinn ppoowweerr ddiissttrriibbuuttiioonn nneettwwoorrkkss
wwiitthh tthhee oovveerrhheeaadd ssiiddee ssuubbssttaattiioonnss ssoolliiddllyy ggrroouunnddeedd,, oorr tthhrroouugghh ggrroouunnddiinngg iimmppeeddaannccee wwiitthh llooww
oohhmmiicc vvaalluuee.. AAtt tthhee ccaabbllee eenndd ssiiddee,, tthhee ssyysstteemm iiss uunnggrroouunnddeedd wwiitthh ppoowweerr ttrraannssffoorrmmeerrss iinn aa ddeellttaa
ccoonnnneeccttiioonn iinn tthheeiirr pprriimmaarryy ssiiddee.. TThhee mmooddeellss uusseedd ffoollllooww tthhee iimmppeeddaannccee ccaallccuullaattiioonn ddeessccrriibbeedd iinn tthhee
ssttaannddaarrdd EENN6600990099--33 [[1100]]..
WWeefi rfisrtspt repsreenstenatb raie fborvieefr voivewervoifelwin eopfr olitnecet iopnrotteecchtnioiqnu etes.chSenciqtiuoens2. dSeescctrioibne s2t hdeefoscrrmibuelsa titohne
ufosremdufolartmioond uesliendg ftohre mcaobdleelsi.nSge tchtieo nca3bliensc.l uSdecetsiotnh e3i minpcleuddaensc tehseo ifmcapbeldeasnacneds goef ncearballese qaunadt igoennsefroarl
sehqiuealdtiocnosn nfeocrt iosnhsi.elTdh ecno,nSneeccttiioonns4. dTethaeilns, thSeecptrioinnc ip4l esdeotfaitlhse pthreo popsreindciapuletos -reocf lotshine gpbrloopckoisnegd
mauettoh-oredcltoescihnngi qbuleo.ckSiencgt iomne5thaonda ltyezcehsnitqhuees. oSftewctaioren si5m aunlaatlyiozness otfheth esooftpwearareti osnimoufltahteiopnrso pofo stehde
mopeethraotdio,na nodf Stheec tipornop6opsreeds emntesththode,r easnudl tsSeocftieoxnp e6r ipmreesnetnatlsf atuhelt rteessutsltcsa rorfi eedxpoeurtiminenthtael lafabuolrta tteosrtys.
Fcianrarilelyd, Soeuctti oinn 7thcoe nlcalbuodreastowriyt.h Fthineamllya,i nSceocntitornib u7t icoonnscolufdthees pwroitpho stehde temchainni qcuoen.tributions of the
proposed technique.

EEnneerrggiieess 22001166,, 99,, 996644 33 ooff 2210
2. State-of-the-Art
2. State-of-the-Art
There are two main protection relays that incorporate the auto-reclosing facility in power
distriTbhuetiroena nreettwwoorkms: adinistparnoctee catniodn grreoluanyds tfhauatlt idnciroercptioornaatel otvheercauurtroe-nret cplorositnegctifoanc irlietlyayisn. Ipno wtheisr
sdeicsttiroibnu, tbiootnh nteectwhnoirqkuse:sd airseta pnrceeseanntdedg.r oundfaultdirectionalovercurrentprotectionrelays. Inthis
section,bothtechniquesarepresented.
2.1. Distance Protection (ANSI 21)
2.1. DistanceProtection(ANSI21)
This protection responds to the impedance value measured between the relay and the fault
This protection responds to the impedance value measured between the relay and the fault
location [11–13]. As the impedance of any line is fairly constant, such protection relays work with the
location[11–13]. Astheimpedanceofanylineisfairlyconstant,suchprotectionrelaysworkwiththe
impedance value of the line. Its application requires consideration of several very important factors:
impedancevalueoftheline. Itsapplicationrequiresconsiderationofseveralveryimportantfactors:
 The resistance of the arc [14].
• Theresistanceofthearc[14].
 The different contributions to the short circuit current from the ends of the line.
• Thedifferentcontributionstotheshortcircuitcurrentfromtheendsoftheline.
 The effect of non-transposition of the conductors.
 • T T h h e e e e f f f f e e c c t t o o f f n ze o r n o - t s r e a q n u sp en o c s e it i m on ut o u f a t l h i e m c p o e n d d a u n c c t e o r i s n . parallel lines.
• Theeffectofzerosequencemutualimpedanceinparallellines.
Among the most interesting features from the point of view of their application are:
Amongthemostinterestingfeaturesfromthepointofviewoftheirapplicationare:
 The reduction of the clearing times of faults.
• Thereductionoftheclearingtimesoffaults.
 An easier coordination with other protections.
 • A Th n e e l a a s c i k e r o c f o s o e r n d s i i n ti a v t i i t o y n to w p it o h w o e th r e s r w p in ro g t s e c o t r i o p n e s n . dulums in the network.
• Thelackofsensitivitytopowerswingsorpendulumsinthenetwork.
The locus of the action limit of the protection is the impedance seen by it. As this impedance is a
Thelocusoftheactionlimitoftheprotectionistheimpedanceseenbyit. Asthisimpedanceis
complex number with a real part (resistance) and an imaginary part (reactance), it can be perfectly
acomplexnumberwitharealpart(resistance)andanimaginarypart(reactance),itcanbeperfectly
represented in R-X diagrams. Therefore, the tripping characteristic of the distance relay can be
represented in R-X diagrams. Therefore, the tripping characteristic of the distance relay can be
superimposed on an R-X diagram to the impedance seen by the same at fault condition, power
superimposedonanR-Xdiagramtotheimpedanceseenbythesameatfaultcondition,powerswings
swings or heavy loads, and thus be able to verify the performance of the protection. Figure 2 shows a
orheavyloads,andthusbeabletoverifytheperformanceoftheprotection. Figure2showsatypical
typical setting of distance protection in a distribution line with line impedance ZL with three
settingofdistanceprotectioninadistributionlinewithlineimpedanceZ withthreeimpedancesteps:
impedance steps: ZA, ZB and ZC. The tripping times for such zones are tAL, tB, tC with tA < tB < tC.
Z ,Z andZ . Thetrippingtimesforsuchzonesaret ,t ,t witht <t <t .
A B C A B C A B C
(a) (b)
X ZL X ZL
Zone C
Zone A R Zone B
Zone B Zone A
Zone C R
(c)
X ZL
(d)
Zone C X ZL
Zone B Zone C
Zone B
ZZoonnee AA
Zone A
R
R
Figure 2. Types of impedance relay characteristics with three zone settings: (a) Impedance relay;
Figure 2. Types of impedance relay characteristics with three zone settings: (a) Impedance relay;
(b)Mhorelay;(c)Reactancerelay;(d)Quadrilateralrelay.
(b) Mho relay; (c) Reactance relay; (d) Quadrilateral relay.

| EnEenrgeriegsie2s0 21061,69,, 99, 69464  |     |     |     |     |     |     |     |     |     | 4 o4fo 2f12 0 |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
| Energies 2016, 9, 964                    |     |     |     |     |     |     |     |     |     | 4 of 21       |
Any small current or voltage transformer error could represent an important increase or
Any small current or voltage transformer error could represent an important increase or
decArenayses mina tllhceu mrreeanstuorredvo ilmtapgeedtraanncsef. oCrmonesreeqruroenrtcloyu, lidf trhepe rfeasuelntt wanasi mpproodrtuacnetdi nvcerreya sceloosred teoc rtehaes e
decrease in the measured impedance. Consequently, if the fault was produced very close to the
intrtahnesimtioena souvreerdheimadp-ceadbalne clein.eC, iot niss enqout eknntolyw,nif inth wehfaicuhl tsiwdea sitp hraosd huacpepdevneedry. Tchloesreeftooret,h iemtpreadnasnitcioe n
transition overhead-cable line, it is not known in which side it has happened. Therefore, impedance
ovperrohteecatdio-cna ibsl enolitn feu,liltyi ssenleocttkivneo two ndiisncrwimhiicnhatsei dwehietthhaesr hthaep pgreonuendd. Tfahuelrte hfoarse h,iampppeendeadn cine pthreo tceacbtiloe n
protection is not fully selective to discriminate whether the ground fault has happened in the cable
isonr oitn futhlely osveelrehcetiavde stiodde.i sIcnr ipmoiwneart edwisthreibthuetirotnh enegtrwoournkds rfaauteldt h4a5s ohra 6p6p kenVe, ddiisntatnhcee cparboleteoctrioinn tihs e
or in the overhead side. In power distribution networks rated 45 or 66 kV, distance protection is
ovmearhinelayd ussiedde w. Ihnepno twhee rsydsitsetmri bisu tsioolnidnlye tgwroourknsderadt.e d45or66kV,distanceprotectionismainlyused
mainly used when the system is solidly grounded.
whenthesystemissolidlygrounded.
2.2. Directional Ground Fault Protection (ANSI 67N)
2.2. Directional Ground Fault Protection (ANSI 67N)
2.2. DirectionalGroundFaultProtection(ANSI67N)
This protection measures the magnitudes of the ground fault current, the residual voltage and  This protection measures the magnitudes of the ground fault current, the residual voltage and
the Tahnigsuplaror tdeciftfieornenmcee abseutrweseetnh ethmeamg.n Iift utdhee sgorfotuhnedg fraouulnt dcufarruelnttc uanrrde ntth,et hreesriedsuidalu avlovltoalgtea gheaavne d
the angular difference between them. If the ground fault current and the residual voltage have
thveaalunegsu loavredr iftfheer esnectetinbget wvaeleunest hpermev.iIofuthsley gsreotu innd tfhaeu lptrcoutrercetinotna nredlathy,e arensdid tuhael avnogltualgaer hdaivffeerveanlcuee s
values over the setting values previously set in the protection relay, and the angular difference
ovbeertwtheeense ttthinemg viasl uinessipdree vthioeu sdliyrescettioinnatlh etrpiproptiencgt ioznonree ladye,fainneddt,h tehaen pgurolatercdtiioffne rreenlcaey bwetiwll eseenntdh eam
between them is inside the directional tripping zone defined, the protection relay will send a
istir tni p isp pidp inein gtg  ho  eo rd rdd eie rr er t  co tto  it  oh tnh eae  cl c itr irr cic upu ipt   tib  nb rgr e aza kok ene rer   odo n nec cfie  n  t teh hde  ,  ttt rhr i pep p ppi nrnog gt   et ici m mtieoe  n  s e ertet    lh haa ays  w  e x xilp pli isr ree dnd .d.   M Mao otrs sit tp  g gpr rio onu ugn nod dr   df a aeu url ttt sos   i itn nh   e
| r   |     |     | i e |   e | e i | i t s | s   | e e |     | f l   |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- |
cisrocsuo li lid itd lby lyr e  gag rko reo uru non dnd ece ded  t hp peo o wtwreipe r r  p idnd igs is tr ttriibmib u uet t iso ioentn  h  nan ese t tew wxopo rir krkes s  d .h hMa a v voe es   ta agn nr o ui i n nnd ddu ufc cat t iui v vletes   ic cnh h asaor r a alic cdt t eleyr r ; ;    grt t hohue e r rne edf f o oer rde e , ,p   ot twh h e ee   r
dicsh aria rba ct cteitoe ri rns t int c  ta n gog lre  sb ehe taw twveee e nan  n  th ene  d  g gur oco utuinvn ded  c  f aha uau lrl tat    cc utuerrr r r;e ntnht  e  ara nenfd do   rr ree e,s iti dhd ueu a acl  h  v vao orlal t acatg gee er, ,i   sa att ti   cw wah hni igc h hle  t tbh hee et   wg r ree eea ant e ets sht
cth rua i s iec  wa n lke  b e tih r f c e t s l t c   g t t  e
grsoe sue n nnsi sdt i v ifvait iuy tyl ti s ic  au a crc hrheie ine vtv eae dnd , d, i s isr n  enso oirdr m muaaa lll y lvy  o1 1l1t0a0 °g°   wew,iai t hth  w  t h hhe ei   cg ghr o otuhu nen d dg  frf aea uau ltl tet    sc ctu usr rer ene n nstit  t  lil eve a aidtdyi n nigsg    at hchhe    ir ree evs sei d ddu u,a aisl    nv ooo l lrt tma g gae el. .l   y
| i t |   s |     | l   |  1   t | t   | r   | r   |     | i t e i | l v a |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | ------- | ----- |
11F0F i◦g ig uwu re rite  3h 3  st  h shh oeo wgw srs  ot   h tuh ene  cd c h hfaaa rur a a clctte tce rur is irs tri tec ic  nt   r ttr ip ilpepap idn inigng  z  gz o otnhn e ee f  f oroer r  ss  is odo lul i i dad lll y yv    g gor rlotoau ugn ned d.e e dFd  i  dgd iui s s trt rer i i b b3u ust t ihi o oon nw    p pso o wtwhe eer r    cs shy yas s trt e eam mcts se. .r   istic
trippingzoneforsolidlygroundeddistributionpowersystems.
IoIo
111100ºº
TTrirpip--ZZoonnee
TTrirpip-Z-Zoonnee
|     |     |     | NNoo-T-Trirpip-Z-Zoonnee |     |     | NNoo--TTrripip--ZZoonnee |     |     |     |     |
| --- | --- | --- | ------------------------ | --- | --- | ------------------------ | --- | --- | --- | --- |
|     |     |     |                          |     |     | UUoo                     |     |     |     |     |
Figure3. Trippingzoneforsolidlygroundedpowerdistributionnetworks. (Uo)Residualvoltage;
F Figi gu ur er e  3  3.  .T  Tr irp ipp p in in gg   z z o on ne e  f o for r s  so ol ild id lyl y  g  g r ro ou u nn d de edd   p p oo ww ee rr   dd iis sttrriibbuuttiioonn  nneettwwoorrkkss..  ((UUoo))  RReessiidduuaall  vvoollttaaggee;;
| (Io ) R e s i d | u a l c u r r | e n t ; ( 1 1 | 0 ◦ ) C h a r | a c t e r i s t i c t r ip | p i n g a | n g le . |     |     |     |     |
| --------------- | ------------- | ------------- | ------------- | -------------------------- | --------- | -------- | --- | --- | --- | --- |
(I(oIo) )R Reseisdiduuaal lc ucurrrerennt;t ;( 1(11100°°) )C Chhaarraaccteterrisistitcic t trripipppiningg a annggllee..
3. 33. .I mImppeeddaanncceess o of fC Caabbleless a anndd G Geenneerraall E Eqquuaattiioonnss f foorr  SShhiieelldd  CCoonnnneeccttiioonnss   ImpedancesofCablesandGeneralEquationsforShieldConnections
TTh T ehhep e pr   o prop ropo pos o essed edd m m m eet e htht o hod odd a a  p app ppl pliie lei s ess tt  o too dd d iissi t str tri rib ibb uuu ttt iio ioo nnn   lllii inn nee ess s  ww wii itt thh h  oo ovv vee err rhh hee eaa add d  aa ann ndd d  cc caa abb bllel e e  ss see ecc cttii too ionn nss,, s  w, w whh heerr eee r   etthh tee h   e
shsihs e hiled ields ldso s fo oft h ft he thec e ac cab abl eles lesa r are c c  o con onn nne nec ect cteet d edd tt  o too ee e aaa rrr tth thh aa a ttt bb boo ott thh h  ee enn ndd dss s  oo off f  tt thh e  cc caa abb bllel e,, , knn noo oww wnn n  aa ass s Siinn ingg gllee l   eBB Boono ndn did igg n   g((SS (BB S)) B..   ).
|     | b   | s a  ree |     |     |     | hee | e   |  kk |  SS | inn |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
NNoNotro at rtnarsanpnsopsspoiotsiisotiitnoionon fo tofh ft ehthceae c bcalaebblselhe s isehhlideielsdldhssa  hshabases  bebneeeeinmn  ipimmleppmlleeemmneteenndttee[d1d 5 [[]11.55F]].o.  FrFoeorxr  aeemxxaapmmlepp,llteeh,, e tthhceoe  mccoopmmosppiootissoiitntiiooonnf  aoonff  y
staaannnydy a srtsdatancnaddbaalredrd fo crcaabmbleele d fiofuormr  m-mveoedldtiauiugmme-a-vvpoopltltlaiagcgaee t iaoapnppsplaliicncaadttiioaonnflssa  taadnnidds p aoa s faflllaaott  fddthiissrppeoeosscaaall b oloeffs  tathhrrereereee  pccraaebbslleeenss t eaadrreei  n
Firgeruepprreeres4es.enntetedd i nin F Figiguurree 4 4. .
ricr i c
rorcoc
|     |     |     | risris |     |     | SSCSCS |     | SSCCSS |     |     |
| --- | --- | --- | ------ | --- | --- | ------ | --- | ------ | --- | --- |
rorsos
tptsps
rS rS
CoCnodnudcutoctror
IsoIslaotlaiotnion
ShSiehlideld
|     |     | ExEtexrtenranl aclo cvoevrer |     |     |     | (b(b)) |     |     |     |     |
| --- | --- | ---------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- |
|     |     | (a()a)                       |     |     |     |        |     |     |     |     |
FiFgFiugigrueurer4e .4 4(. a.( )a(a)C )C aCbaalbeblelce oc cmoompmpoposoistsiitioitoinonna  anandndd( b (b()b)fl ) faflaltatdt  didsisipspopososasala.ll. .( (r(r r iccic)))  IIInnnttteeerrrnnnaaalll  cccooonnnddduuuccctttooorrr  rrraaadddiiiuuusss;; ; (((rrroo occ))   )EEExxxtteetrrennranalla  l
|     |     |     |     |     |     | i   |     |     | c   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cocnoc onu ndd ucotc roto rra r rdar adu disu; ius(r;s  ;  ()r( r Isi)ns )  IenI ntnet errnl n caa ol l  cd coo unn cdd ucr ctsoto hrr  sl shd hi;eie ldd  ;  )((rE r oosx)s) t   eEE xta tee lrrns n haa ill e   lss dhhir iee all ddd i   urr saa ;dd iuu s;; A  (( vrr ses)) r   aAA gvv eee srr haa igg eee ld  ss rhh aii deell idd u
| d cut | i   | i   | t r a | n tuo i e | (lr ; | rxn |     | (ir | s)  | s;  |
| ----- | --- | --- | ----- | --------- | ----- | --- | --- | --- | --- | --- |
|       |     | i s |       |           | o s   |     |     |     | s   |     |
(Sr ar da diDuiusi;s s ; t(  aS(S nCSCc)Se )D  Diesitt saw tane nce cen e b b aee xtwt w seeeo enf n ta  axe xeesc s oo o nf f dt ht hec e tc  coo rnn add nuu dccts too hrr ia  anl n ddd ; s  s thh i iee )lldE d;x ;  (t (te t pprss)n )  Ea Exl xtc tee orr vnn eaa rll  ct c hoo ivv cee krr n  tt ehh sii scc .kknneessss..
| C S ) | b   |     | e h | u o |     | e ( p s |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |

Energies2016,9,964 5of20
3.1. ImpedanceofCableandShields
EnergIiens 2t0h1i6s, 9s, e9c6t4i on, the formulation that evaluates the impedances and self-impedances betw5 eofe 2n1
thedifferentpartsofthecablesislistedandimplementedinMatlabtodevelopthecablemodelsin
S3i.m1. uImlinpkeduansecde oifn Cthabeles iamndu lSahtiieolndss describedinSection5. First,theselfimpedancesoftheconductors
andshieldsareindicated.Then,themutualimpedancesbetweenthemarecalculated.Theirimpedance
In this section, the formulation that evaluates the impedances and self-impedances between the
valuesarecalculatedusingCarson’sequationsconsideringtheeffectofthereturngroundpathforall
different parts of the cables is listed and implemented in Matlab to develop the cable models in
typesofselfandmutualimpedances.
Simulink used in the simulations described in Section 5. First, the self impedances of the conductors
Theselfimpedanceoftheconductoris:
and  shields  are  indicated.  Then,  the  mutual  impedances  between  them  are  calculated.  Their
impedance values are cal cula te d usin g   C a r−so n ´s   e q u a t i o−n s  c o n si d eri ng the effect of the retu rn
| Z = R   | + π | 2 ·1 0 7 ·f + j · 4· | π · 1 0 7 ·l n ( D | / r ) | (1 ) |
| ------- | --- | -------------------- | ------------------ | ----- | ---- |
| C C(ca) |     |                      |                    | e oc  |      |
ground path for all types of self and mutual impedances.
The self impedance of the conductor is:
TheexpressionforthereturngroundpathdistancegivenbyCarsonis:
| ZC = RC(ca) + π2·10−7·f |     |  + j·4    | ·π·10−7·ln(De/roc)  |     | (1)  |
| ----------------------- | --- | --------- | ------------------- | --- | ---- |
|                         |     | (cid:114) | ρ                   |     |      |
e
|     | D   | =1.85· |     |     | (2) |
| --- | --- | ------ | --- | --- | --- |
The expression for the return ground epath distanωce· µgiven by Carson is:
o
ρ
Ontheotherhand,theselfimpedanceofDt h =e 1s.h8i5e·l√di se:   (2)
|     |     | e                             | ω·μo    |     |     |
| --- | --- | ----------------------------- | ------- | --- | --- |
|     |     | 2 − 7·ef s+hji·e4l·dπ ·i1s:0  | −7·ln(D |     |     |
On the other hand, the ZseSl=f iRmSp(cead) +anπc e· 1o0f  th /r ) (3)
|     |                   |                        |                      | e s     |      |
| --- | ----------------- | ---------------------- | -------------------- | ------- | ---- |
| Z   |   = R coS(ncad) + |   π 2· 10 − 7 ·f  +  j | ·4 ·π ·1 0 −7· ln (D | /rsb )  | (3)  |
Themutualimpedancebetw eSe n u c to r “ i ” a n d s hi e ld “ j” caen ewrittenas:
The mutual impedance between conductor “i” and shield “j” can be written as:
|      | =π2·10                                   | −7·f+j·4·π·10 | −7·ln(D |      |      |
| ---- | ---------------------------------------- | ------------- | ------- | ---- | ---- |
| Z CS |                                          |               | e /S    | CS ) | (4)  |
|      | ZCS = π2·10−7·f + j·4·π·10−7·ln(De/SCS)  |               |         |      | (4)  |
Themutualimpedancebetweenanyconductoranditsshieldcanbewrittenas:
The mutual impedance between any conductor and its shield can be written as:
|      | π 2 =·1 π02 | − ·170·f−7+·f j+·4 j··π4··π10·1 | − 07−·7l·lnn((DD |     |         |
| ---- | ----------- | ------------------------------- | ---------------- | --- | ------- |
| Z CS | =ZC S       |                                 | ee//rrss         | ))  | (5()5 ) |
The mutual impedance between shields is given by:
Themutualimpedancebetweenshieldsisgivenby:
|      | ZSS = π2·10−7·f + j·4·π·10−7·ln(De/SSS)  |               |         |      | (6)  |
| ---- | ---------------------------------------- | ------------- | ------- | ---- | ---- |
|      | =π2·10                                   | −7·f+j·4·π·10 | −7·ln(D |      |      |
| Z SS |                                          |               | e /S    | SS ) | (6)  |
33..22.. BBaallaanncceedd SSyysstteemm:: GGeenneerraall EEqquuaattiioonnss ffoorr SSiinnggllee BBoonnddiinngg ((SSBB)) SShhiieelldd CCoonnnneeccttiioonnss
TThhee cciirrccuuiitt uusseedd iinn tthhiiss ssttuuddyy iiss sshhoowwnni innF Fiigguurree5 5a annddc coorrrreessppoonnddsst otoa annS SBBc coonnnneecctitoionn..
Isa
Ia
Isb
Ib
Isc
Ic
U
|     | R1  |     | R2  |     |     |
| --- | --- | --- | --- | --- | --- |

FFiigguurree 5.5S. taSntadnadrdarsdh ieslhdiselcdosn nceocntinoenctfioornS Bfoarp pSlBic aatipopnlsi.c(aIt i,oIn s,.I  ()ICa, uIrbr,e nItc)s inCucorrnednutsc toirns ;c(Io n a,dIu c,toIs r s);
|     |     |     | a b c | s sb | c   |
| --- | --- | --- | ----- | ---- | --- |
C(Iusar,r eIsnb,t sIisnc) sChuierlrdesn;t(sR  in,R s h)iGelrdosu; n(dRr1,e sRis2t)a Gncreosuantdb ortehsiesntadnscoefss hatie bldost;h( Ue)nPdos teonf tisahlidelidffse;r e(nUc)e Pboettweneteianl
1 2
sdhiifefeldretnecrme bineatwlse.en shield terminals.
When the load currents form a three-phase balanced system and only a positive sequence
component exists, the vector sum of the line currents flowing in the conductors is zero. The voltages
induced in the shields have a component due to the flow of current through conductor, and another
due to the currents circulating in the shields. As shown in Figure 5, the shields are grounded at both
ends and the voltages between the two grounding connections are equal to the three shields as:

| Energies2016,9,964 |     |     |     |     |     |     |     |     |     |     |     | 6of20 |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
When the load currents form a three-phase balanced system and only a positive sequence
componentexists,thevectorsumofthelinecurrentsflowingintheconductorsiszero. Thevoltages
inducedintheshieldshaveacomponentduetotheflowofcurrentthroughconductor,andanother
duetothecurrentscirculatingintheshields. AsshowninFigure5,theshieldsaregroundedatboth
endsandthevoltagesbetweenthetwogroundingconnectionsareequaltothethreeshieldsas:
|     |     |     | U=U | +U  | =U +U | =U  | +U  |     |     |     |     | (7) |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 1C  | 1S  | 2C    | 2S  | 3C  | 3S  |     |     |     |     |
Themathematicalmodelsforsuchinducedvoltagesarelistedbelow:
•
Inducedvoltagesinshieldsduetocirculatingcurrentsinconductors:
|     |     |     |      | =L·(Z | ·I        | ·I     |         | ·I   |     |     |     |      |
| --- | --- | --- | ---- | ----- | --------- | ------ | ------- | ---- | --- | --- | --- | ---- |
|     |     |     | U 1C |       | C1S1 1 +Z | C2S1 2 | +Z C3S1 | 3 )  |     |     |     | (8)  |
|     |     |     | U    | =L·(Z | ·I +Z     | ·I     | +Z      | ·I ) |     |     |     | (9)  |
|     |     |     | 2C   |       | C1S2 1    | C2S2 2 | C3S2    | 3    |     |     |     |      |
|     |     |     |      | =L·(Z | ·I        | ·I     |         | ·I   |     |     |     |      |
|     |     |     | U 3C |       | C1S3 1 +Z | C2S3 2 | +Z C3S3 | 3 )  |     |     |     | (10) |
• Inducedvoltagesinshieldsduetocirculatingcurrentsinshields:
|     |     |     | =L·(Z |      | ·I    | ·I      |         | ·I   |     |     |     |      |
| --- | --- | --- | ----- | ---- | ----- | ------- | ------- | ---- | --- | --- | --- | ---- |
|     |     |     | U 1S  | S1S1 | S1 +Z | S2S1 S2 | +Z S3S1 | S3 ) |     |     |     | (11) |
|     |     |     | =L·(Z |      | ·I    | ·I      |         | ·I   |     |     |     |      |
|     |     |     | U 2S  | S1S2 | S1 +Z | S2S2 S2 | +Z S3S2 | S3 ) |     |     |     | (12) |
|     |     |     | =L·(Z |      | ·I    | ·I      |         | ·I   |     |     |     |      |
|     |     |     | U 3S  | S1S3 | S1 +Z | S2S3 S2 | +Z S3S3 | S3 ) |     |     |     | (13) |
Allthepreviousequationscanbeexpressedasamatrixsystem:
|     |     |     |    |    |        |    |       |     |     |     |     |      |
| --- | --- | --- | --- | --- | -------- | --- | ------ | --- | --- | --- | --- | ---- |
|     |     |     | U   |     | U        |     | U      |     |     |     |     |      |
|     |     |     |     | 1   | 1C       |     | 1S     |     |     |     |     |      |
|     |     |     |    |  = |  +    |     |       |     |     |     |     |      |
|     |     |     |  U | 2  |  U 2C  |    | U 2S  |     |     |     |     | (14) |
|     |     |     | U   |     | U        |     | U      |     |     |     |     |      |
|     |     |     |     | 3   | 3C       |     | 3S     |     |     |     |     |      |
where:
|          |       |        |        |    |       |    |        |        |        |    |     |       |
| ---------- | ------ | ------ | ------ | --- | ------- | --- | ------ | ------ | ------ | --- | ---- | ------ |
| U 1        | Z C1S1 | Z C2S1 | Z C3S1 |     | I 1     |     | Z S1S1 | Z S2S1 | Z S3S1 |     | I S1 |        |
|  U  =L· | Z      | Z      | Z      | · | I +L· |     | Z      | Z      | Z      | · | I    |  (15) |
|  2       |  C1S2 | C2S2   | C3S2   |    |  2    |    | S1S2   | S2S2   | S3S2   |    |  S2 |       |
| U          | Z      | Z      | Z      |     | I       |     | Z      | Z      | Z      |     | I    |        |
| 3          | C1S3   | C2S3   | C3S3   |     | 3       |     | S1S3   | S2S3   | S3S3   |     | S3   |        |
4. PrinciplesofNovelAuto-ReclosingBlockingMethodforPowerDistributionNetworks
Thenewmethodpresentedmeasuresthecurrentsatthethreeshieldsofthecablesattheirends
located at the substation side, and the currents in the active part of the three phases of the cable
as indicated in Figure 6. This was studied for solidly or low-value impedance grounded power
distributionnetworkswithdistributiontransformersinadeltaconnectionattheirhigh-voltagesides.
Thismethodisvalidwhenthetransitionoverhead-cableisnotveryfarawayfromthesubstationwhere
themeasurementsofcurrentsinshieldsandconductorsaredone. Weemployatriggersignaltostart
theanalysisandconsideratotaltimesignallengthof40msasapre-triggertimeand40msactivefault
time. Thetriggersignalisprovidedbyanyprotectionrelaywhenagroundfaulthasbeendetected.
Thetimeset40msfortheactivefaulttimeisacceptable,asthegroundfaultsatpowerdistribution
networks are active for longer times and the minimum tripping time for standard overcurrent or
voltagerelaysis30ms. Apartfromthistime,themedium-voltagecircuitbreakeropeningtimesarenot
lessthan40–50ms. Thismeansthat40msasanactivefaulttimeisgoodenough,aswillbeverifiedin
thesimulationandrealtestresults.

Energies 2016, 9, 964 7 of 21
ΔL3S3 for the respective phases and corresponding shields. A second evaluation is developed for the
second decision criteria and to make sure that the right maneuver will be taken up. This second
evaluation is a wavelet analysis of those angular differences. The wavelet analysis uses the discrete
Energiwesa2v01e6le,9t ,t9r6a4nsform (DWT) and only evaluates the high-frequency elements [16–18]. These two 7of20
analyses are now described.
Active
conductors
CT
CT New Auto-Reclosing
Blocking Unit
CT
CT
CT
CT
Cable
Shields
Power
cables
FiguFriegu6r.eC 6u. Crruernretsntosf otfh tehec acbablelessm meeaassuurreedd iinn tthhee aactcitviev ecocnodnudcutocrtso arnsda nthdeitrh sehiiresldhsi.e lds.
4.1. Analysis of Angular Difference Between the Conductor Currents and Respective Shields
Oncethistriggersignalhasbeenacknowledged,thenewmethodinitiatestheproceduretoclassify
This analysis evaluates the angular differences ΔL1S1, ΔL2S2 and ΔL3S3. In normal operation
wherethegroundfaulthashappened,andtakesthedecisionofwhetherornottoblockthereclosing
without ground faults, the currents circulating in staggered cables in the three shields form a
maneuver. With the shields connected in SB disposal, the new method first evaluates the angular
balanced system, and the angular differences between active currents and shield currents have
differencebetweenthecurrentsintheactivepartofthecablesandtheircorrespondingshieldsduring
similar values. Cables in flat disposal have unbalanced currents in the shields, as the distances
atimeof40msprevioustotheacknowledgementofthetrigger,andanother40msaftersuchtrigger
between them are not exactly the same; whereas cables in delta disposal normally have very similar
hasbceuernreanctsk. nAosw a lfeudngcteidon, soof tthhee gtrootuanlde vfaaululta ptoiosintiotinm, teheis p8h0asme-ss.hAieldfu clulrpreenrito adngFuoluarr ideirffterraenncsefso ramre ation
overiancrrueansnedin, gdewcrienadsoedw oor fsttwayo thcey cslaemseo. fTthheeirf ubnehdaavmioer natlalolwfrse, qinu emnocyst tcoasceasl,c tuhlea tleoctahtieonp hoaf steheo f the
respegcrtoiuvnedc ufarurletn tto. bTeh disetaenrmguinleadr.d Tiyffpeirceanl oceveirshheaedre lainfteesr udpe tnoo 3t0e dkmas a∆ndL 1cSab1l,e∆ leLn2gSt2hsa unpd t∆o L1320S03 mfo rthe
respehcativvee bpehena seevsaalunadtecdo rarse as pcaosned sitnugdysh. Hieoldwse.vAers, ethcoisn mdeetvhaoldu caotiuolnd ibsed uesveedl oinp esidmfiolarrt choensfeigcuornadtiodnesc ision
with larger distances.
criteriaandtomakesurethattherightmaneuverwillbetakenup. Thissecondevaluationisawavelet
When the ground fault occurs in the overhead line side, the currents in the shields are due to the
analysisofthoseangulardifferences. Thewaveletanalysisusesthediscretewavelettransform(DWT)
mutual coupling between all conductors and shields. In such ground fault conditions, the angular
andonlyevaluatesthehigh-frequencyelements[16–18]. Thesetwoanalysesarenowdescribed.
difference between them is in the range from 10 to 50°. Practically all ground fault current circulates
from the fault point to the grounding system in the main distribution substation to which the power
4.1. AnalysisofAngularDifferenceBetweentheConductorCurrentsandRespectiveShields
transformer is grounded.
ThisHaonwaleyvseirs, eifv tahleu agtreosunthde faaunlgt uolcacrurdsi finfe trheen cliense ∆siLd1eS, 1g,ro∆uLn2dS f2aualnt dcu∆rrLe3nSt 3c.irIcnulnaotersm fraolmo ptheer ation
withofauutlgt rpoouinntd tofa buolttsh, tehnedsc uorfr ethnet sschiirecldu loaft inthge ipnhsatsaeg gweirtehd ac faabullets. Tinheth sehitehlrde eofs hthieel dcasbfloer wmitah btahlea nced
systegmro,uanndd ftahuelta ancgtsu alas rad girffoeurnedn cfeasulbt ectuwrreeennt dacivtiidveerc. uArtr ethnet seaarnthdinsgh ioefl dsuccuhr rae nshtsiehlda vate bsoimthi lcaarblvea lues.
ends, both fault currents return to the main substation; whereas the currents circulating in the
Cablesinflatdisposalhaveunbalancedcurrentsintheshields,asthedistancesbetweenthemarenot
shields of the phases without any fault keep circulating from one end to the other of the cable. This
exactlythesame;whereascablesindeltadisposalnormallyhaveverysimilarcurrents. Asafunction
circulation process makes ΔL1S1, ΔL2S2 and ΔL3S3 greatly increase and have values well above 50°
ofthegroundfaultposition,thephase-shieldcurrentangulardifferencesareincreased,decreasedor
The threshold to decide whether the auto-reclosing maneuver is blocked has been selected as 50°,
staythesame. Theirbehaviorallows,inmostcases,thelocationofthegroundfaulttobedetermined.
which appears in the algorithm developed for this new application.
Typic aloverheadlinesupto30km andcablelengthsupto1200mhavebeenevaluatedasacasestudy.
However,thismethodcouldbeusedinsimilarconfigurationswithlargerdistances.
Whenthegroundfaultoccursintheoverheadlineside,thecurrentsintheshieldsareduetothe
mutu alcouplingbetweenallconductorsandshields. Insuchgroundfaultconditions,theangular
differencebetweenthemisintherangefrom10to50◦. Practicallyallgroundfaultcurrentcirculates
fromthefaultpointtothegroundingsysteminthemaindistributionsubstationtowhichthepower
transformerisgrounded.
However,ifthegroundfaultoccursinthelineside,groundfaultcurrentcirculatesfromthefault
pointtobothendsoftheshieldofthephasewithafault. Theshieldofthecablewiththegroundfault
actsasagroundfaultcurrentdivider. Attheearthingofsuchashieldatbothcableends,bothfault
currentsreturntothemainsubstation;whereasthecurrentscirculatingintheshieldsofthephases

Energies2016,9,964 8of20
withoutanyfaultkeepcirculatingfromoneendtotheotherofthecable. Thiscirculationprocess
makes∆L1S1, ∆L2S2and∆L3S3greatlyincreaseandhavevalueswellabove50◦ Thethresholdto
decidewhethertheauto-reclosingmaneuverisblockedhasbeenselectedas50◦,whichappearsinthe
algorithmdevelopedforthisnewapplication.
Energies 2016, 9, 964 8 of 21
4.2. WaveletAnalysisoftheAngularDifferenceBetweentheConductorCurrentsandRespectiveShields
4.2. Wavelet Analysis of the Angular Difference Between the Conductor Currents and Respective Shields
Theuseofwaveletanalysisallowsinformationinthetimedomain. Thesignaltobestudiedis
decomposTehdei nustoe odfi fwfearveenltets hanoarltysscisa laelsloowfsw ininfodromwastiofonr inth teheh itgimheer dforemqauine.n Tchiees ,siagnndall oton bgew stiunddioewd issc ales
forthdeelcoowmpfroesqedu einntcoie ds.ifEfelreecnttr ischaolrst igscnaalelss souf cwhinadsocwusr rfeonr ttshaen hdigvhoelrt afrgeeqsuaenrecineso, tafnrede lofrnogm whinadrmowo nics;
theDsisccarleest efoWr athvee lleotwT rfarneqsufoernmcieiss. vEelercytreifcfael cstiigvnea.lIst ssufochrm aus lcautirorennctsa nanbde vworltiattgeens aasref onlolot wfrse:e from
harmonics; the Discrete Wavelet Transform is very effective. Its formulation can be written
as follows: Ψ S,τ(t)=S −1/2·Ψ(t−τ/S);S>0;S(cid:15)R (16)
ΨS,τ(t) = S−1/2·Ψ(t − τ/S); S > 0; S ϵ R (16)
where the mother wavelet Ψ is expanded or contracted by the scale factor S (S−1/2·Ψ(t/S)).
where the mother wavelet Ψ is expanded or contracted by the scale factor S (S−1/2·Ψ(t/S). Such a
Suchamotherwaveletisinverselyproportionaltothefrequencyandisshiftedbytheshiftfactor
mother wavelet is inversely proportional to the frequency and is shifted by the shift factor
τ(Ψ(t−τ))[19]. ThemotherwaveletchosentodeveloptheDWTanalysismusthavegoodfeatures
τ(Ψ(t − τ) [19]. The mother wavelet chosen to develop the DWT analysis must have good features to
to remove harmonics as well as high performance when extracting the main characteristics of the
remove harmonics as well as high performance when extracting the main characteristics of the
studiedsignal. ThereareseveralmotherwaveletssuchasHarr,Daubechies,Biorthogonal,Coiflets,etc.
studied signal. There are several mother wavelets such as Harr, Daubechies, Biorthogonal, Coiflets,
Thenumberofdecompositionstepsischosenfunctionofthesamplingfrequencyoftheoriginalsignal.
etc. The number of decomposition steps is chosen function of the sampling frequency of the original
Thefisrisgtndael.c Tohme pfiorssti tdioecnohmapsotswitioone lheams etwntos :ealemhiegnht-sf: rae qhuigehn-fcryeqeuleemnceyn etle D m1eannt dD1 a alnodw a- flroewq-ufreenqcuyenelceym ent
A
1
. Aesleamfeunnt cAti
1
o. nAos fat hfuenscatimonp loinf gthfer esqaumepnlcinygf sf,rethqueefnrceyq ufs e, nthcye bfraenqdueonfcyD b1aenlde moef nDt
1
i selfesm/2e–nfts /is4 Hz,
wherefs a/2s–tfh s/4e Hfrze,q wuheenrceyasb tahned froeqfuAe1necyle bmanend toifs Af
s1
/ e4l–em0Henzt .isI nfs/t4h–e0 sHezc.o Innd thdee sceocmonpdo dseitcioomn,ptohseitiAon1, ethleem ent
isdecAo1m elpemoseendt iisn dtoecDom
2
peolesmede innttof oDr2 tehleemheingth f-ofrr ethqeu henigchy-fbreaqnuden(cf sy/ b4a–nfds / (8fs/H4–zfs)/8a Hndz) Aan
2
de Ale2m eleenmtefnotr the
low-ffroerq utheen lcoywb-farneqdu(efn
s
/cy8 –b0anHdz ()f.s/8T–h0i sHpzr).o Tcehsiss pisrorceepses aitse rdepuenattieldt huentdile tshiree ddefsrireeqdu ferneqcyuebnacny dbarneadc hed
allowrseathcheerdi gahlltoiwnsfo trhme artiigohnt oinfftohremeavtiaolnu aotfe dthes igevnaallutaotebde seigxntraal cttoe db.eI nexFtirgacutreed.7 ,Inth Feigduerceo m7, ptohes ition
develdoepceodmbpyostihtieonw daevveelleotpterda nbsyf tohrem wcaavnelbete trsaenesnf.orm can be seen.
 f 
LF A  s Hz
i 2i1
A2
LF
A1
 f 
LF HF D  s Hz
i 2i 
 f 
y(x) HF D  s Hz
2 22 
HF D   f s   Hz
1 21 
FiguFriegu7r.eW 7.a Wvealveetlterta tnrasnfosfromrm.F. Frereqquueennccyy bbaannddss rreelalatetedd tot odedceocmopmopsiotisointi ostnepsst.e ps.
TheDTahue bDeachubieesch2iems o2t hmerotwhearv ewleatv,edleBt,2 ,dhBa2s, bhaese nbeseenle csteeledc,teads,i tahs aits ghaoso dgocohda rcahcatrearcistetircisstitcos ctloa ssify
them c a l g as n s i i t f u y d th e e o m ft a h g e n D itud c e o o m f p th o e n D en1 t co [2 m 0 p ] o w n h en e t n [2 th 0] e w g h ro e u n n th d e f g a r u o l u t n is d l f o a c u a l t t e i d s l a o t ca th te e d o a v t e t r h h e e o a v d er o h r e c a a d b o le r side
1
ofthe c l a i b n l e e . s T id h e e o t f h r th e e s h li o n l e d . f T o h r e D thr v es a h lu ol e d c f o o m r D po 1 n v e a n lu t e s c h o a m s p b o e n en en s t e s l h e a c s te b d ee to n 5 s 0 ele to cte b d lo t c o k 5 t 0 h e to a b u l t o o c - k r e t c h l e o sing
auto-reclosing order when i1ts value is higher. The variable W represents its value in the algorithm
orderwhenitsvalueishigher. ThevariableWrepresentsitsvalueinthealgorithm(Figure8).
(Figure 8).
4.3. AlgorithmofNewAuto-ReclosingBlockingMethod
4.3. Algorithm of New Auto-Reclosing Blocking Method
FigurFeig8usrhe o8w shsotwhes athlge oarligtohrmithums eudsetdo tdoe dteertemrminieneth theel oloccaatitoionn ooff tthhee ggrroouunndd ffaauultl tisi.s T.hTeh aenaanlyaslyiss isof
∆L1S1o,f ∆ ΔLL21SS21, aΔnLd2 ∆ S2L 3aSn3d isΔLd3eSv3e liosp deedveinloppaedra lilne lpwariathlleal wwaitvhe ale twaanvaellyets iasntahlaytsiesv tahlauta teevsaltuhaetems atxhiem um
valuemsaoxfimthuemd vBa2l-uceDs 1ofc toheef fidcBi2e-ncDts1 fcoorefsfuicciehnt∆s Lfo1rS 1su,c∆hL Δ2LS12S1a,n ΔdL∆2SL23 aSn3d. ΔTLh3eS3v.a Tluhee svaolfueths eofd tBh2e -cD1
coeffidciBe2n-tcsDa1r ceoaenffaicliyeznetsd a,raen adnathlyezevda,r aianbdl ethWe viasrioabbltea iWne ids .obtained.

Energies2016,9,964 9of20
Energies 2016, 9, 964 9 of 21
Energies 2016, 9, 964 9 of 21
Input Input Input
Input Input Input
Trigger. Trigger. Trigger.
Trigger. Trigger. Trigger.
Trip – L1 Trip – L2 Trip – L3
Trip – L1 Trip – L2 Trip – L3
Analysis
Analysis
+/-40 ms
+/-40 ms
from the
from the
trigger input
trigger input
>50º
> < 5 6 0 0 <º º 60º Rec R lo e s c in lo g sing
An A g n le gle Bloc B k l e o d c . ked.
P
D
hP
i
a
fD
h
f
s
ei
ae
frf
s
e
/
e
Se
nr
h
e
/
c
Si
ne
eh
cs
ldi
e
e
s
ld C a o W C n e a aa fo W f v l i n e y c ea a f s ife lv li e i ys cn et s. i te l s i e s n t . ts WW W < >W 6 5 0 0< > º6 5 0 0 º
ANDAND
F C a S a u id F b lt C e l a S e a a u i t d b lt e l e at
dBd2B-c2D-c1D1
evaelvuaaltuioantion
FFiFgiiguguruerr e8e.8 8A.. AlAglolggrooirtrhiitmthhm mofo otfhft ethh neeen nweew waua atuout-toroe--rcreleocclsolionssigni nbgglob bclolkocicnkkgini nmggem mtheeothtdho.o dd..
55.5. A. AAnnanlaayllsyyisssii sso foo fSf iSSmiimmuluualltaaiottiinoo nnR eRRseeussluutsll ttss
TTThhhee ep prproropopopososeseded da auautuotto or rerececloclolsoisnsinigng gb blobloclokcckinkingin ggm memtehetohthdoo ddw wawsa asssi smsimiumluaultaleatdet eduds uiunssigni ngSgi SmSimuimluinulkilni®nk ki®n® iiann tayap tytiycpapilci caall
pppooowwweerer rd ddisiitssrttirrbiiubbtuuiottiinoo nnn enntewetwtowrokor rkpk rperpseersneestneedtne tdaes da as acasa csaea ssect uassdtueyd. syAt.u nAd eynq. ueqivAuainlveanelteq n“upti iv“”ap mli”eon mdteo“ld pfeoi”lr f lominr oelidsn ewelsa fswo urasse luidns eesd
awsa saw sweulelsl ale sad sp aopswowweree trlr ltaranassnfsopfroomwrmeerresr rtsra artaendtse fd6o6 r6/m260/e2 rk0sV kr,V a2t,0 e2 Md0 VM66AV/ Aw20 iwthki VtDh,y D2n0y1 nMc1oV ncAonnecwnteiiocthnti ogDnroy gunrp1o uacpno dna nndedisc dttriioisbnturitgbioruontui opn
tartanrnadnsfsdofirosmrtmreibresur str iaortanetdet dr2 a02n/00s/.f04o. r4km Vke,V r6s, 360r3a 0kte VkdAV2 Aa0 n/ad0n .d4co kcnoVnn,enc6te3ico0tnio kgnVr Aoguropaun Dpd yDcnoy1n1nn.1 eL1c.o taLiodonsa dignsr oitnhu eptsheDe sdyeins dt1r1iisb.turitLbioounati dosn
tirtnarnatnshfseofsroemrmderiessr tswr iwberueetr ieco ocnnosntirdsaiendrseefrdoe rdum pue ptros t 6ow0 60e0 rk0eV kcAVo nAws iiwdthei trshet adsntadunapdrdato rpd6o p0w0oewrk eVfarAc ftaowcrtsio tfrhrso sfmtrao n0m.d8 a05r .8idn5d piunocdwtuievcret iftvaoec 1tto.o r 1s.
TfTrhohem eg rg0ird.8id 5s csihncehdmeumec teiuv sueesdeto dh 1ah.sa soT nhoeen eog vroeivdrehrsehcahedae dmd iesdtirusitbsreuibdtiuohtniao slnin olenin eweo iwtvhei trahh etaoa tdtaol dtalielsn tlrgeitnbhgu tothifo no24f l i2kn4me k.w mTih.t heT ha“ept io”“t pail”
plpeanraagrmathmeteoetrfesr 2so 4fo ftk htmeh e.o voevTrehhreehaed“a pdlii ”nlienp ewa rwiathmitoheuotteu grtsr gooruofnudtnh wde iwroevi rheera hhveaea vtdeh etl hifneoe lfloowlwloiitnwhgoi nuvgta lvguarelosu:u eRnsd0: R= w0 0 =.i8r 3e01.8 hΩ3a1/v kΩem/tk, hm e,
RfRo1 l1l =o =w 0i.n06.g8678v 7a ΩluΩ/ek/smk:mR, 0 ,L =0L 00 = .8 =30 1.00Ω0.04/08k468m 6H, R/Hk 1 /m=km,0 .,L6 81 L71 =Ω =/L k2 Lm= 2 , L=0 0 .00=0.10030.0810334 883H6 /HHkm//kk, mmC,, 0L C 1 = 0 =4=L. 2 2 44= .2×04 . 01×001 −391 803F−9/H kFm//kk, mm ,,
CCC1 0 1 == =4 C.2C2 42 = × =8 1.808.9−8 99× F ×/1 k01m−09 −,9F C/Fk 1 /mk=m.C .T 2 h=Teh8 e.c8 o9cno×dnud1c0ut−ocrt9o Frt/y pktyemp .eis TisLh AeL-cA5o6-n 5d6w uiwcthtoi trhd itaydmpiaeemtieser tLeΦAr L-AΦ5566L A =w56 i9t=h. 459d .i4am5m mme,t em r,
RΦRLA LL5 AA65 56 = 6 ==0 .069.1.64615 6Ωm Ω/km/mk,m,R I, L m A Iamx 5 a6 = x ==1 9019.96.3915.63 5AΩ A/akn amdn ,dgI e m goe a m x oem=tre1it9cr 9imc.3 em5aAnea danni sddtiasgnteacoenm cGeeM tGrDiMc m=D 2 e=.a5 n23. d5m3is. mtTahn. ecT ehuGen dMuenDrdge=rorg2ur.n5od3u mnd.
cTachbaeblelu eun usdesederd gir soi sRu nRHdHZc1Za 1b2 Ol2eOLu Ls1e 21d/22i/0s2 0Rk VHk VZw1 hw2oOhsoeLs me1 2am/in2a0 infke aVfetuawrteuhsro esaser ema:r aeΦi: nCΦabflCee-aacbotlreue- cro =ere s 1=a3 r.18e32:. Φ8m2 C m a m b , l m e S -c c, o r =S e c 1= =51 013 5.m802m mm2,m m 2,,
S SSs c = s = =1 6 11 56m 0 mm mm2m , 2R,2 R , = S =0 s .01 =.811 886 8Ω mΩ/k m/mk2m, , Φ,R eΦx=te = x0t 3=.1 4 38 .448 .m4Ω mm /k .m m A. ,AcΦa cb e al x eb t ll =ee n 3leg 4nt .4 hg tm fhro mfmr.o m6 A 0 06c – a010b 2–l 0 e102l e0m n0 g wmth a ws f c rao hsm ocshe 6on 0s. 0e T –nh 1. e 2T 0 sh0 hei m eslhdiw se ladss
o cof h ft o htshe e sen es. ec T acb halbe els se hsa i rae erl dec o scnoo nnf ent c hetce etd see din c ia nS b B lSe ,B s w, a hwr e ehreec aroes na t nsh e etch t oee v doevr i h neerSha B de,a ldw in hlein e c reo e ncaos s ind tsh eie rdseo srv pse asr nph ae lena n d lgel tni h ngs et ho c fso 1on 0fs 0 i1 d m0e0. r smTh s.p eTa hne
g legro nrou gun thnd sd r o erf sei 1ss 0itsa 0tnam cne .c eT a t ha tte h tg eh r teo r a utrn nas dnitsr iio etis noi snt t a a ktnaekc s ee asa tat y t pthyi e cpa ticr l aav nla svlu iat e ilou o nef to1 af2 k 1Ω e2s aΩa n t dayn p adt ic taa htl etv hc a ael b ucl eaeb o elf ne1 de2 nsΩdu bsa sun tba d tsita oat ntit o0 h .ne 5 c0Ω a.5. b lΩe.
T
eT
h
nh
e
d e
m
s mu
o
b
d
osd
e
t
l
ae
u
tl i
s
uo
e
sn
d
e0 d
i
.
s
5i s
sΩh
s
o
h.
w
oTwh
n
e n
in
m i n
F
o
i
Fd
g
i
u
egl
r
u
e
ur s
9
ee
.
9d. isshowninFigure9.
Breaker - L: Fault at Overhead Side
Breaker - L: Fault at Overhead Side Breaker - C: Fault at Cable Side Load Voltages
Breaker - C: Fault at Cable Side Voltages Conductor Currents Load Voltages
S R N c U c S 6 = R n N c 6 1 = U c 5 6 k 6 = n V 0 6 6 1 =0 5 k k 6M V 0 V 6 0 V A B C k M AV V A B C A U S T A B C T T ra = = U S T n D 6 2 A B C s T T r y 6 0a f = o n =/ n D 2 M r 16 2 s m 0 y 6 0 fV n o n / k e b a c 2 2 A M r 1 V r m 0 V n k e b a c 2 A V V r - A B C T S I M h uV r b- e e A B C T Is a e Mt h a s - r P u te e io r h V a ee S n I a s a a -m u P s b u b A V b e b c c a c r eh V o e S s I na l a a t t m u a a ts b b V b t g e b c c a c e ioo s e O n ln t t s a a t A B C v A t g e i S o 1 e r O h n u 2 s C A B C v e b A ek u a s S 1 mr r d ta h r u 2 C e t e L b i n o k C u A B a i s n m t nr d t s a e r eA t L i n o C A B in t n s e O R A A B C v d e e r 1O f h R e 2 A B Ce v c d a ke t e m d r 1 f h e 2 L e c C A B i a k t n m d e L C A B ine C s C s C s c c c a a a r r r b b b e e e C l l l e e e e e e p C s C s C n n n o o c c a a a n 1 2 3 1 2 3 r r w b b b e e ti C l l l n e e e e e e p u r n n o g o o n 1 2 3 1 2 u w u ti i s n e u rg o u u i s s s s C C C c c c a a a r r r b b b e e e l l l e e e e e e n n n s s C C C c c 1 2 3 1 2 3 a a a r r b b b e e l l l e e e e e n n 1 2 3 1 2 R C s C s C s d c c c a a a e r r r b b b e e e fe l l l e e e e e e R c n n n C s C s C t d 1 1 2 3 c c 1 2 3 a a a e r r b b b e e fe l l l e e e e e c n n t 1 1 2 3 1 2 s s s C C C c c c a a a r r r e e e b b b e e e l l l e e e n n n s s C C C 1 2 3 1 2 3 c c a a a r r e e b b b e e l l l e e e n n 1 2 1 2 3 V-I A B C T M S h u e re b V a e s s - - t I u A B C a T P M S r t h i e h o V u e r V m a I n e a a b a s o b b e s e B s e l b c c a c - t t n u a a Pt r t g 3 i e h o V e m a I n s a a s T b b e B e b A B C r c c a c n a t n 3 sform A B C n e S b 2 a c r u : V bC - s T I S toa M h u n n t r S i b A B C e b e od 2 a c u s a e nu V Vt b s - a I cB a a - P u s t t T I S i b b o t r o h a M h b e c c a c r u n a t rm i C b A B C e e o s B s a e e n u e V t s - a n r I B a a P r u t t e i b b r o h b n e c c a c n a t m s s B e en L t oa A B C 4 d 0 L 0 o c k u a V L r d r o A e a A B C 4 n d 0 L ts 0 o c k u a V r d r A ents
Substation A A: 3s Ccraebelne s3 connection S sBcreen 3 B: 3 sCcarebelens 3connection S Bscreen 3 U S T T = = 2 6 0 3 / T 0 0 S r . ka T4 Vn = k As 6V f 3 o 0 rm kV e A r: Rt Rt
R1 A: 3 Cables connection SB B: 3 Cables connection SB DynU1T1=20/0.4 kV
R1 Dyn11
Shield Voltages Substation B
A Vabc Shield Voltages Substation B
A Iabc Vabc
B a Iabc Shield Currents Substation B
B b a Shield Currents Substation B
C c b R3
Three-CPhase c R3
V-I MeasuTrhermeee-nPt1hase
V-I Measurement1
FFigiguurere 99. N.Newew auatuot-or-ercelcolsoisnign gblbolcokciknign gmmetehtohdo:d m:omdoedl eimlipmlepmleemnetendte. d.
Figure 9. New auto-reclosing blocking method: model implemented.

Energies2016,9,964 10of20
Energies 2016, 9, 964 10 of 21
Energies 2016, 9, 964 10 of 21
5.1. Angular Difference Analysis in Power Distribution Networks Solidly Grounded at the Overhead Side and
55.1.1..A AnngguulalarrD Diiffffeerreennccee AAnnaallyyssiiss iinn PPoowweerr DDiissttrriibbuuttiioonn NNeettwwoorrkkss SSoolliiddllyy GGrroouunnddeedd aatt tthhee OOvveerrhheeaadd SSidide eaanndd
IsIsoolalatetedda attt thheeC Caabbllee EEnndd SSiiddee
Isolated at the Cable End Side
TThhee aanngguullaarr ddiiffffeerreenncceess ∆ΔLL11SS11,, ∆ΔLL22SS22 aanndd Δ∆LL33SS33 bbeettwweeeenn ccuurrrreenntsts inin ththee sshhieieldlds saanndd inin ththe e
The angular differences ΔL1S1, ΔL2S2 and ΔL3S3 between currents in the shields and in the
aa acc ctit tvi i v vee e pp paa arr rtt t ooo fff t tth hhe ee c cca aab bbl l e eles s s i i n nin a a as s y yss syt t e esm mte mu u n nug gnr r o ogu urnonud d ene d dd ea adt t t t hahte e tc cha aeb b l lce ea s sbi i d dlee e s( ( titdy y p pei i c(cta ayl l pp pio ocw wale epr r ot t r rwa a n nesrs f f otorr ram mne esr rf o i i n nrm d dee erl l t t a ain
dc ceo olntnan nce eoc c t tni i ono n ne)c) taiaon nnd d) as s ono l ldi i d dsl loy yl igdg r rloyo u ugn nrd doeue d dn da aet td t t h haete toho v vee eor rvh hee era ahd de as sdi i d dse ei dh hea ahv v eae vb bee ebe een ne na a l l lal ls sli ism mimu u l lua alt tae etd de dd ddu uur r i irn nigng g n nno oor r m mrma aal l l
oo opp pee errar a atit toi i o onn no fo otf fh t teh hpe e o p pwo oew wre edr ri sdtdri iis sbt tur r i itb biou unt t i i o onn ne t wn n e eot trw wko owr r k kit hw woiui t t hth ogo uruot t u g gnr rdo o u ufan nud dl t f faa anu udl l t t w a ain nthd d itw wai ilt toh hn gi i t t da ailfl ofoen nrg ge n d dti ipf f f foe esr rie etin not tn
ap pto oths s i iet t i i ooo nvn e a art th t teh hae ed o osv vie edr reh h e eaa and dd s sai i d dte eth a aen ncd da a abt tl et t h hse ei d c cea a.b b l lMe e sus i ild dtie ep. . lM Meusuil lmt t i i p pul lle ea ts sii iom mnu usl l asaht t i ioo own n s s ts shh hao otw wth t teh h a act tl at tsh hse ei fic c lcl a aas sts siioi f fni i c c a aot tfi i o othn n e
of the ground faults turns out to be:
gorof uthned gfraouulntsdt ufarunlstso tuutrtnos boeu:t to be:
•   G G Gr r ro o ou u un n nd d d f f af a au u ul l lt t t i i ni n n t t th h he e e o o ov v ve e er r rh h he e ea a ad d d s s si i id d de e e: : : i i i f ff ∆Δ Δ L LL 1 11 S SS 1 11 , ,, Δ Δ ∆L LL 2 22 S SS 2 22 a aa n nn d dd Δ Δ ∆L LL 3 33 S SS 3 33 a aa r rr e ee l ll e ee s ss s ss t tt h hh a aa n nn 5 55 0 00 ° ° ◦, , , n nn o oo r r m rmm a aa l l l ll y yly i i n nin
all phases.
aallllp phhaasseess..
•

 G
G
Gr
r
or
o
ou
u
un
n
nd
d
df
f
af
a
au
u
ult
l
l
t
ti
i
ni
n
nt
t
th
h
he
e
e c
c
ca
a
ab
b
bl
l
le
e
e l
l
li
i
in
n
ne
e
e s
s
si
i
id
d
de
e
e:
:
: i
i
if
f
f a
a
at
t
t l
l
le
e
ea
a
as
s
st
t
t o
o
o
n
nn
e
ee
o
oo
f
ff
Δ Δ∆L
LL
1
11
S
SS
1
11
,
,,
Δ Δ∆L
LL
2
22
S
SS
2
22
o
oo
r
rr
Δ Δ∆L
LL
3
33
S
SS
3
33
i
ii
s
ss
c
cc
l
ll
e
ee
a
aa
r
rr
l
l
y
lyy
o
oo
v
vv
e
ee
r
rr
5
55
0
00
° °◦.
. .
F
F
Fig
i
i
g
gu
u
ur
r
re
e
es
s
s 1
1
10
0
0 a
a
an
n
nd
d
d 1
1
11
1
1 s
s
sh
h
ho
o
ow
w
w h
h
ho
o
ow
w
w t
t
th
h
he
e
e v
v
va
a
ar
r
ri
i
ia
a
at
t
t
i
ii
o
oo
n
nn
s
ss
o
oo
f
ff
Δ Δ∆L
LL
1
11
S
SS
1
11
,
,,
Δ Δ∆L
LL
2
22
S
SS
2
22
a
aa
n
nn
d
dd
Δ Δ∆L
LL
3
33
S
SS
3
33
a
aa
r
rr
e
ee
w
ww
h
hh
e
ee
n
nn
t
t
h
hth
e
ee
p
pp
o
oo
w
ww
e
e
r
er r
distribution network suffers a ground fault in phase L1 at the overhead line side 12 km from the
ddisistrtribibuuttiioonn nneettwwoorrkk ssuuffffeerrss aa ggrroouunndd ffaauulltt iinn pphhaassee LL11 aatt tthhee oovveerrhheeaadd lliinnee ssididee 1122 kkmm frfroomm ththee
transition, and at the cable line side in its central position in t = 200 ms. The overhead line has a total
trtarannssitiitoionn,,a anndda attt thheec caabbllee lliinnee ssiiddee iinn iittss cceennttrraall ppoossiittiioonn iinn tt == 220000 mmss.. TThhee oovveerrhheeaadd lilninee hhaass aa tototatal l
length of 24 km and the cable 600 m.
lelennggththo off2 244k kmma annddt thheec caabbllee 660000 mm..
Ground fault in t=200 ms at the overhead side in phase L1
-
-
6
6
0
0
Ground fault in t=200 ms at the overhead side in phase L1
-65 Angle difference L1-S1
A n gl e
Diff er e n c e
A
n gl e
Diff
er e n c e
C o n d
u ct or-
S
hi el d ( d e gr e e s)
o n d u
ct or- S
hi
el d ( d e gr e e s)
-
-
- - -
-
-
-
- - -
9
8
8 7 7
9
8
8
7 7 6
0
5
0 5 0
0
5
0
5 0 5 A A A A A n n n n n g g g g g l l l l l e e e e e D D d D D i i i i i f f f f f f f f f f e e e e e r r r r r e e e e e n n n n n c c c c c e e e e e L L S L S 1 2 2 3 3 - - - - - S S S L L 1 3 2 3 2 1 1 5 5 , , 6
1
6
1
4
2
4
2
º
,
º
, 2 2 0 0 º º 1 1 5 5 , , 4 4 4 4 º º
C
-95
-95
-
-
1
1
0
00
0
0
0.
.
1
1
5
5
0
0
.
.
2
2 Time (s)
0
0
.
.
2
2
5
5
0
0
.
.
3
3
Time (s)
Figure 10. Angular differences with ground fault at the overhead side in phase L1.
FFiigguurree 1100.. AAnngguullaarr ddiiffffeerreenncceess wwiitthh ggrroouunndd ffaauulltt aatt tthhee oovveerrhheeaadd ssiiddee iinn pphhaassee LL11. .
Ground fault in t=200 ms at the cable side in phase L1
1
1
0
0
0
0
Ground fault in t=200 ms at the cable side in phase L1
Angle Difference L1-S1
A A n n g g l l e e D D i i f f f f e e r r e e n n c c e e L L 2 1 - - S S 2 1 167,95º
A n gl e
Diff er e n c e
A n gl e
Diff er e n c e
P h a s e- S
hi el d ( d e gr e
e
s)
h a s e- S hi
el d ( d e gr e e
s)
-
-
-
-
2
1
2
1
0
0
0
0
0
0
0
0
0
0 A A A n n n g g g l l l e e e D D D i i i f f f f f f e e e r r r e e e n n n c c c e e e L L L 3 2 3 - - - S S S 3 2 3 167,9
7 7
5
3 3
º
, , 3 3 5 5 º º 2 2 3 3 , , 1 1 5 5 º º
P-300
-300
-
-
4
4
0
00
0
0
0.
.
1
1
5
5
0
0
.
.
2
2 Time (s)
0
0
.
.
2
2
5
5
0
0
.
.
3
3
Time (s)
Figure11.AngulardifferenceswithgroundfaultatthecablelinesideinphaseL1.
Figure 11. Angular differences with ground fault at the cable line side in phase L1.
Figure 11. Angular differences with ground fault at the cable line side in phase L1.
CCoonnssiiddeerriinngg ddiissttaanncceess ffrroomm tthhee ttrraannssiittiioonn,, TTaabbllee 11 sshhoowwss tthhee rreessuultlsts oof fththee vvaariraiatitoionn inin Δ ∆ LL1S11S,1 ,
∆ ΔLL22SS2 C 2a o an n nd s d i∆d Δ e LL r 3 i 3 n SS3 g 3 f d frro i o s m t m an oo c nn e ll s yy f 11 ro mm m tt oo th mm e oo tr rr a ee n tt s hh i aa ti nn o n 11 , 00 T kk a mm b l i e inn 1 tt hh s e h e o oo w vvee s r rh t h h ee e aa dd re ll s iin u ne l e t s s si id o d f ee , t , h aan e n d v d a ffr r ro i o a mm ti o 11 n t ot i o n 5 59 Δ 99 L 9 m 1 m S i 1 ni , n
ΔL2S2 and ΔL3S3 from only 1 m to more than 10 km in the overhead line side, and from 1 to 599 m in
ththeec caabblelel ilninees isdide.e.I tItc acnanb ebes eseenenh ohwowth tehev avraiaritaiotinosnos fo ∆ f LΔ1LS11S,1 ∆ , LΔ2LS22Sa2n adn ∆ d LΔ3LS33Sa3r earree dreudceudcewd hwenhetnh e
the cable line side. It can be seen how the variations of ΔL1S1, ΔL2S2 and ΔL3S3 are reduced when
gtrhoeu gnrdoufanudl tfaouccltu orcscautrtsh aet othvee rohveeardheliande lsinidee siadned aanrde avreer yvehriyg hhiwghh ewnhtehne tghreo gurnodunfadu flatuhlat phpaepnpsentsth t e
the ground fault occurs at the overhead line side and are very high when the ground fault happens t
ctahbel ecalibnlee sliindee .side.
the cable line side.

| Energies2016,9,964     |     |     |     |     |     |     |     | 11of20    |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --------- |
| Energies 2016, 9, 964  |     |     |     |     |     |     |     | 11 of 21  |
Table1.Phaseanglevariationwithgroundfaultsattheoverheadandcablelinesides.
Table 1. Phase angle variation with ground faults at the overhead and cable line sides.
| FaultatOverheadLineSide |     |     |     |     |     | FaultatCableLineSide |     |     |
| ----------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- |
Fault at Overhead LFianuel tSiindeP haseL1 Fault at Cable Line FSaiudlet inPhaseL1
|     |     | Fault in Phase L1  |     |     |     |     | Fault in Phase L1  |     |
| --- | --- | ------------------ | --- | --- | --- | --- | ------------------ | --- |
DiDstaisntcaenfcreo mfroTmra nsition VariationinPhaseAngles DDiissttaannccee ffrroommT ransition VariationinPhaseAngles
|             | Variation in Phase Angles  |        |        |       |             | Variation in Phase Angles  |             |        |
| ----------- | -------------------------- | ------ | ------ | ----- | ----------- | -------------------------- | ----------- | ------ |
| Transition  |                            | ∆L1S1  | ∆L2S2  | ∆L3S3 | Transition  |                            | ∆L1S1 ∆L2S2 | ∆L3S3  |
|             | ΔL1S1                      | ΔL2S2  | ΔL3S3  |       |             | ΔL1S1                      | ΔL2S2       | ΔL3S3  |
1 m1 m 15.181°5 .18◦ 101.09.988°  ◦ 1155.2.266° ◦ 1m 73.69° 73.69◦ 168.16628°. 62◦ 24.0243.°0 3◦
  1 m
| 10m   |         | 15.16◦ | 10.99◦          | 15.24◦ | 10m   |         | 73.72◦ 168.65◦ | 24.05◦  |
| ----- | ------- | ------ | --------------- | ------ | ----- | ------- | -------------- | ------- |
| 10 m  | 15.16°  |        | 10.99°  15.24°  |        | 10 m  | 73.72°  | 168.65°        | 24.05°  |
| 100m  |         | 15.17◦ | 11.01◦          | 15.26◦ | 50m   |         | 73.75◦ 168.61◦ | 24.12◦  |
10 1 0 0  m 00   m 15.17 1 ° 5   .18◦ 11 1 . 1 0 .0 1 5 ° ◦ 1 1 5 4 .2 .2 6 7 °◦  50 m 1   00m 73.75°  73.71◦168. 1 6 6 1 8 ° .   52◦24.1 23 2 . ° 7   3◦
100500 0m0 m 15.181°5 .25◦ 111.10.353° ◦ 1145.2.377°◦  100 m3 00m 73.71° 73.35◦168.15627°. 95◦23.7233.°1 5◦
50>0100 ,m00 0m 15.251°5 .44◦ 111.23.230° ◦ 1155.3.674°◦  300 m5 99m 73.35° 67.32◦167.19557°. 11◦23.1275.°6 7◦
>10,000 m  15.44°  12.20°  15.64°  599 m  67.32°  157.11°  27.67°
| FaultatOverheadLineSide              |                            |                        |     |     |                                      | FaultatCableLineSide       |                        |     |
| ------------------------------------ | -------------------------- | ---------------------- | --- | --- | ------------------------------------ | -------------------------- | ---------------------- | --- |
| Fault at Overhead Line Side          |                            |                        |     |     |                                      | Fault at Cable Line Side   |                        |     |
|                                      |                            | FaultinPhaseL2         |     |     |                                      |                            | FaultinPhaseL2         |     |
|                                      |                            | Fault in Phase L2      |     |     |                                      |                            | Fault in Phase L2      |     |
| DiDstaisntcaenfcreo mfroTmra nsition |                            |                        |     |     | DDiissttaannccee ffrroommT ransition |                            |                        |     |
|                                      |                            | VariationinPhaseAngles |     |     |                                      |                            | VariationinPhaseAngles |     |
|                                      | Variation in Phase Angles  |                        |     |     |                                      | Variation in Phase Angles  |                        |     |
| Transition                           |                            | ∆                      | ∆   | ∆   | Transition                           |                            | ∆L1S1ΔL2 ∆             | ∆   |
ΔL1S 1L 1S1 Δ LL2S2S22  Δ LL33SS33  ΔL1S1  SL2 2S2ΔL3 SL33 S3
1 m1 m 15.341°5 .34◦ 151.53.333° ◦ 1100.8.811°◦  1 m  24.02° 24.02◦73.7723°. 72◦1681.6588.°5 8◦
1m
15.351°5 .35◦ ◦ ◦ 24.10° 24.10◦ 73.7703°. 70◦ 1681.6589.°5 9◦
| 10 1m0 m |     |     | 151.53.344°  1100.8.888° |     | 10 m 10m |     |     |     |
| -------- | --- | --- | ------------------------ | --- | -------- | --- | --- | --- |
1001 0m0 m 15.341°5 .34◦ 151.53.333°  ◦ 1100.8.877° ◦ 50 m 50m 23.92° 23.92◦ 73.7713°. 71◦ 1681.6487.°4 7◦

| 1000m |     | 15.37◦ | 15.36◦ | 10.85◦ | 100m |     | 23.85◦ 73.79◦ | 168.42◦ |
| ----- | --- | ------ | ------ | ------ | ---- | --- | ------------- | ------- |
1000 m  15.37°  15.36°  10.85°  100 m  23.85°  73.79°  168.42°
| 5000m |     | 15.48◦ | 15.45◦ | 11.20◦ | 300m |     | 22.99◦ 73.55◦ | 167.65◦ |
| ----- | --- | ------ | ------ | ------ | ---- | --- | ------------- | ------- |
50 > 0 1 0 0   , m 00   0m 15.48 1 ° 5   .67◦ 15 1 . 5 4 .5 5 6 ° ◦ 1 1 1 1 .2 .7 0 2 °◦  300 m 5   99m 22.99°  27.87◦73.5 6 5 7 ° .   51◦167 1 . 5 6 7 5 . ° 5   2◦
>10,000 m  15.67°  15.56°  11.72°  599 m  27.87°  67.51°  157.52°
| FaultatOverheadLineSide      |     |                    |     |     |                | FaultatCableLineSide      |                    |     |
| ---------------------------- | --- | ------------------ | --- | --- | -------------- | ------------------------- | ------------------ | --- |
| Fault at Overhead Line Side  |     |                    |     |     |                | Fault at Cable Line Side  |                    |     |
|                              |     | FaultinPhaseL3     |     |     |                |                           | FaultinPhaseL3     |     |
|                              |     | Fault in Phase L3  |     |     |                |                           | Fault in Phase L3  |     |
| Distance from                |     |                    |     |     | Distance from  |                           |                    |     |
DistancefromTransitionVariaVtairoinat iinon PihnaPseh aAsengAlnegs les DistancefromtransitioVnariatiVoanr iiant iPonhaisneP AhansgeleAsn gles
| Transition  |     |     |     |     | transition  |     |     |     |
| ----------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
ΔL1S∆1L 1S1 Δ∆LL2S2S22  Δ∆LL33SS33  ΔL1S1 ∆L1S1ΔL2∆SL2 2S2ΔL3∆SL33 S3
1 m   11.78 °   .78◦ 15 . 4 1 ° ◦ 1 5 .2 5 °◦  1 m  168.61°   68.61◦24.0 1 °   01◦ 73.3 1 °   1◦
| 1 m |     | 1 1 | 1 5 .4 1 | 1 5 .2 5 | 1m  |     | 1 2 4 | . 73 . 3 |
| --- | --- | --- | -------- | -------- | --- | --- | ----- | -------- |
10 1m0 m 11.791°1 .79◦ 151.54.422° ◦ 1155.2.222°◦  10 m 10m 168.62°1 68.62◦24.0224°. 02◦ 73.7730.°7 0◦
11.771°1 .77◦ 151.54.433° ◦ 1155.2.233°◦  168.51°1 68.51◦23.9223 .92 73.7732.°7 2◦
| 1001 0m0 m |     |     |     |     | 50 m 50m |     |     |     |
| ---------- | --- | --- | --- | --- | -------- | --- | --- | --- |
11.821°1 .82◦ ◦ ◦ 168.40°1 68.40◦ 23.7253°. 75◦ 73.3731.°3 1◦
| 100100 0m0 m |     |        | 151.54.455°  1155.2.255° |        | 100 m1 00m |     |                |        |
| ------------ | --- | ------ | ------------------------ | ------ | ---------- | --- | -------------- | ------ |
|              |     | 12.13◦ | 15.55◦                   | 15.33◦ |            |     | 168.12◦ 23.11◦ | 73.55◦ |
5000 m  5000m 12.13°  15.55°  15.33°  300 m  300m 168.12°  23.11°  73.55°
|          |     | 12.66◦ | 15.73◦ | 15.45◦ |      |     | 157.36◦ 67.78◦ | 68.01◦ |
| -------- | --- | ------ | ------ | ------ | ---- | --- | -------------- | ------ |
| >10,000m |     |        |        |        | 599m |     |                |        |
>10,000 m  12.66°  15.73°  15.45°  599 m  157.36°  67.78°  68.01°
5.25..2W. WavaevleetleAt nAanlaylsyissisin ina aP PowowererD Disisttrriibbuuttiioonn NNeettwwoorrkk SSoolliiddllyy GGrroouunnddeedd aat tththe eOOvevrehrehaeda dLiLnien SeiSdeid aenadn d
IsolatedattheCableEndSide
Isolated at the Cable End Side
ThTehsei msimulualtaiotinonr erseusultlstso offt hthiissc coonnfifigguurraattiioonn iinncclluuddeedd inin TTaabblele 22 shshooww thtahta tthteh aenagnuglaurl adrifdfeifrfeenrceen ce
whwehnetnh tehge rgoruonudndfa fuaultlth haassh haappppeenneedd iinn tthhee oovveerrhheeaadd ssiiddee hhaass ddBB2-2c-DcD1 1coceofefifcfiiecnietns tlsowloewr ethratnh a0n.1,0 .1,
anadnodv eorve1r0 010w0h wenhethne thfaeu flatuislti nist hine tehlein ee lsiindee .siFdieg.u Freigsu1r2esa n1d2 1a3ndsh 1o3w shthoewr etshuel trsesoublttasi noebdtafionredg rfoour nd
fauglrtosuinndp fhaausletsL in1 apthtahsee oLv1 earth tehaed olvinerehseiadde lainned scidaeb laenldin ceasbsleid lienreess spidecet irveseplye.ctively.
Ground fault in t=0.2 s at the overhead side in phase L1
0.2

dB2-cD1 Angle difference Conductor L2/Shield S2
|     | 0.15 |     |     | dB2-cD1 Angle difference Conductor L3/Shield S3 |     |     |     |     |
| --- | ---- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
dB2-cD1 Angle difference Conductor L1/Shield S1
s 0.1
nt
e
ci 0.05
effi
C o 0
1
D
c-0.05
2-
B
d -0.1
-0.15
-0.2
|     |     | 0.1995 | 0.2 |          | 0.2005 | 0.201 | 0.2015 |     |
| --- | --- | ------ | --- | -------- | ------ | ----- | ------ | --- |
|     |     |        |     | Time (s) |        |       |        |     |
FigFuigruer1e2 .12W. aWvealveetldetB d2-B12--c1D-c1Dc1o ecfofiecfifeicnitesnotsf tohf ethane gaunlgaurldairf fdeirfefnerceenscieg nsiaglsnawlsi thwigtrho ugrnodufnadu lftaiunltp ihna se
L1pahtatshee Lo1v aetr htheea dovseirdhee1ad2 ksimdef 1ro2m kmth ferotmra nthsiet itorann.sition.

| Energies2016,9,964     |     |     |     |     | 12of20    |
| ---------------------- | --- | --- | --- | --- | --------- |
| Energies 2016, 9, 964  |     |     |     |     | 12 of 21  |
db2-cD1 Coefficients for ground fault in the the cable side in t=0.2 s in phase L1
150

dB2-cD1-Angle Difference Conductor L2/Shield S2
nt s 100 dB2-cD1-Angle Difference Conductor L1/Shield S1
e
ci dB2-cD1-Angle Difference Conductor L3/Shield S3
effi
o
|     | C   |     |     | 127.3 |     |
| --- | --- | --- | --- | ----- | --- |
1
D
c 50
2-
B
d
0
|     | 0.1 8 0.185 | 0.19     | 0.195 0.2 | 0.205 |     |
| --- | ----------- | -------- | --------- | ----- | --- |
|     |             | Time (s) |           |       |     |
Figure13.WaveletdB2-1-cD1coefficientsoftheangulardifferencesignalswithgroundfaultinphase
Figure 13. Wavelet dB2-1-cD1 coefficients of the angular difference signals with ground fault in
L1atthecablelineside300mfromthetransition. phase L1 at the cable line side 300 m from the transition.
TabTlaebl2e. 2W. aWvaevleetleat naanlaylsyissi:s:s ismimuullaattiioonn rreessuullttss.. GGrroouunndd fafauultlst sata tthteh eovoevrehrehaeda danadn dcabcaleb lleinlei nseidseisd. es.
OvOevrherehaedadli nlienes idsiedes osloidlidlylyg grorouunnddeedd aanndd ccaabbllee lliinnee ssiiddee iissoollaatteedd. .PPhhasaes ecucrurrernetns tmsmeaesuasreudre idn itnhet he
concodnudcutocrtosr(sL (1L,1L, 2L,2L, 3L)3a) nanddi nint htheeirirs shhieiellddss ((SS11,, SS22,, SS33))..
| Fault at Overhead Line Side  |                                          |     | Fault at Cable Line Side  |                                          |     |
| ---------------------------- | ---------------------------------------- | --- | ------------------------- | ---------------------------------------- | --- |
| FaultatOverheadLineSide      |                                          |     | FaultatCableLineSide      |                                          |     |
|                              | Fault in Phase L1                        |     |                           | Fault in Phase L1                        |     |
| Distance from                |                                          |     | Distance from             |                                          |     |
|                              | W (dB2-cD1 Coefficients)  FaultinPhaseL1 |     |                           | W (dB2-cD1 Coefficients)  FaultinPhaseL1 |     |
| Transition                   |                                          |     | Transition                |                                          |     |
DistancefromTransitionΔL1SW1 (dB2-ΔcDL21SC2o effiΔciLe3nSts3)  DistancefromTransitΔioLn1S1 W(dBΔ2L-c2DS21 CoeΔffiLc3ieSn3t s)
1 m  0.006∆8L 1S1 0.∆00L627S 2 0∆.0L036S53  1 m  173.88 ∆L1S10.01∆34L 2S20.0∆09L63 S3
| 10 m  | 0.0039  0.0041  | 0.0041  | 10 m  | 173.89  0.0123  | 0.0097  |
| ----- | --------------- | ------- | ----- | --------------- | ------- |
| 1m    | 0.0068 0.0067   | 0.0065  | 1m    | 173.88 0.0134   | 0.0096  |
1001 m0m  0.00303.0 039 0.00.003084 1 0.00.0003491  50 m 10m 127.32 173.890.01103.0 123 0.0009.040 97
100100 m0m  0.00207.0 033 0.00.002093 8 0.00.0002359  100 m5 0m 127.32 127.320.01109.0 113 0.0009.070 94
500100 0m0 m 0.00109.0 027 0.00.002042 9 0.00.0001295  300 m1 00m 127.31 127.320.01208.0 119 0.0008.090 97
| 5000m | 0.0019 0.0024 | 0.0019 | 300m | 127.31 0.0128 | 0.0089 |
| ----- | ------------- | ------ | ---- | ------------- | ------ |
>10,000 m  0.0014  0.0016  0.0013  599 m  123.67  0.02784  0.0332
| >10,000m                     | 0.0014 0.0016 | 0.0013 | 599m                      | 123.67 0.02784 | 0.0332 |
| ---------------------------- | ------------- | ------ | ------------------------- | -------------- | ------ |
| Fault at Overhead Line Side  |               |        | Fault at Cable Line Side  |                |        |
FaultatOverheadLineSide Fault in Phase L2  FaultatCableLineSide Fault in Phase L2
| Distance from  |                                         |     | Distance from  |                                         |     |
| -------------- | --------------------------------------- | --- | -------------- | --------------------------------------- | --- |
|                | W (dB2-cFDau1l tCionePffhiacsieenLt2s)  |     |                | W (dB2-cDF1a uCloteinffiPchieansetsL) 2 |     |
| Transition     |                                         |     | Transition     |                                         |     |
DistancefromTransitionΔL1SW1 (dB2-ΔcDL21SC2o effiΔciLe3nSts3)  DistancefromTransitΔioLn1S1 W(dBΔ2L-c2DS21 CoeΔffiLc3ieSn3t s)
1 m  0.006∆7 L   1S1 0.∆00 L 6 2 4 S   2 0∆.0 L 0 3 6 S 9 3   1 m  0.0095 ∆L1S1 173.∆90 L   2S2 0.0∆13 L 6 3   S3
| 10 m   | 0.0044  0.0039  | 0.0042  | 10 m  | 0.0098  173.90  | 0.0122  |
| ------ | --------------- | ------- | ----- | --------------- | ------- |
| 1m     | 0.0067 0.0064   | 0.0069  | 1m    | 0.0095 173.90   | 0.0136  |
| 100 m  | 0.0037  0.0031  | 0.0039  | 50 m  | 0.0095  127.30  | 0.0114  |
| 10m    | 0.0044 0.0039   | 0.0042  | 10m   | 0.0098 173.90   | 0.0122  |
1000 m  100m 0.0029  0.0037 0.0022  0.0031 0.0028  0.0039 100 m  50m 0.0098  0.0095 127.30  127.30 0.0120  0.0114
500100 0m0 m 0.00201.0 029 0.00.001072 2 0.00.0002228  300 m1 00m 0.0088 0.0098127.31127 .30 0.010.3001 20
>10,5000000 mm  0.00106.0 021 0.00.001011 7 0.00.0001252  599 m3 00m 0.0333 0.0088123.71027 .310.0207.08123 0
>10,00F0amult at Overhe0a.d00 L16ine S0i.d0e0 11 0.0015 599Fmault at Cable L0i.n03e3 S3ide 123.70 0.02782
FaultatOverheaFdauLlitn ienS Pidhease L3  FaultatCabFleauLlitn ienS Pidhease L3
| Distance from  |                                         |     | Distance from  |                                         |     |
| -------------- | --------------------------------------- | --- | -------------- | --------------------------------------- | --- |
|                | W (dB2-cFDau1l tCionePffhiacsieenLt3s)  |     |                | W (dB2-cDF1a uCloteinffiPchieansetsL) 3 |     |
| Transition     |                                         |     | Transition     |                                         |     |
DistancefromTransition ΔL1S1  ΔL2S2  ΔL3S3  DistancefromTransition ΔL1S1  ΔL2S2  ΔL3S3
|       | W(dB2-cD1Coefficients) |         |       | W(dB2-cD1Coefficients) |         |
| ----- | ---------------------- | ------- | ----- | ---------------------- | ------- |
| 1 m   | 0.0066  0.0064         | 0.0065  | 1 m   | 0.0135  0.0094         | 173.91  |
|       | ∆L1S1 ∆L2S2            | ∆L3S3   |       | ∆L1S1 ∆L2S2            | ∆L3S3   |
| 10 m  | 0.0044  0.0045         | 0.0037  | 10 m  | 0.0121  0.0097         | 173.91  |
100 1mm  0.00307.0 066 0.00.003096 4 0.00.0003605  50 m 1m 0.0113 0.01350.00907.0 094 1271.2739. 91
| 10m | 0.0044 0.0045 | 0.0037 | 10m | 0.0121 0.0097 | 173.91 |
| --- | ------------- | ------ | --- | ------------- | ------ |
1000 m  0.0029  0.0031  0.0024  100 m  0.0121  0.0099  127.29
| 100m | 0.0037 0.0039 | 0.0030 | 50m | 0.0113 0.0097 | 127.29 |
| ---- | ------------- | ------ | --- | ------------- | ------ |
5000 m  0.0023  0.0023  0.0018  300 m  0.0131  0.0087  127.30
| 1000m | 0.0029 0.0031 | 0.0024 | 100m | 0.0121 0.0099 | 127.29 |
| ----- | ------------- | ------ | ---- | ------------- | ------ |
>10,5000000 mm  0.00106.0 023 0.00.001052 3 0.00.0001138  599 m3 00m 0.02783 0.01310.03304.0 087 1271.7271. 30
| >10,000m | 0.0016 0.0015 | 0.0013 | 599m | 0.02783 0.0334 | 127.71 |
| -------- | ------------- | ------ | ---- | -------------- | ------ |
6. Experimental Results
6. ExperimentalResults Different laboratory tests were developed in order to test the validity of the new auto-reclosing
blocking method, and to check the computer simulation results obtained.
Differentlaboratorytestsweredevelopedinordertotestthevalidityofthenewauto-reclosing
blockingmethod,andtocheckthecomputersimulationresultsobtained.

Energies2016,9,964 13of20
Energies 2016, 9, 964 13 of 21
66..11.. EExxppeerriimmeennttaall SSeettuupp
TThhee tteessttss wweerree ccaarrrriieedd oouutt oonn aa ssoolliiddllyy eeaarrtthheedd ssoouurrccee ssuupppplliieedd bbyy aa ppoowweerr ttrraannssffoorrmmeerr rraatteedd
880000 VVAA,,4 0400/0/110000V Vacaca nadndD yDny1nc1o ncnoencntieocntiognro ugpro.uTpw. oTlwinoe mlinoed umleoedmuluel aetmoruslwatiothrse qwuitivha leeqnuticviarlceunitt
“cpiri”cuwite “repiu” swederwe iuthsetdh ewfoitlhlo twhein fgolfleoawtuinregs :feRat=ur8e8s.:4 8R m= Ω88,.L48= m4Ωm, HL a=n 4d mCH= 4anµdF Cea c=h 4c aμpFa ceiatcohr.
Tcahpearceiatolrc.a Tbhleeu rseeadl chaabsleth uesfeodll ohwasi nthgec hfoalrlaocwteirnigst icchsa:rRac=te1r.i8stΩic,s:L R= =2 21.m8 ΩH, aLn d= 2C2= m4H.9 annFdw Cit h= a4.t9o tnaFl
cwaibthle lae ntgotthalo fc3a0b0lem .leTnwgtoho voef rc3u0r0r enmt.p rTowteoc tioonverrecluaryrsenotf typproetMectRioI4n byreWlayoso dowf artdy-pSee gMarReI4u sebdy
aWsodoisdtwurabradn-Sceegr eacroer udseerds taoss dtoisrteutrhbeanvcaelu reescoorfdtheres ctuor rsetonrtes flthoew vianlgueins tohf ethaec tcivuerrceonntsd uflcotworisngan idn tthhee
sahctiievlde scoonfdthuectcoarbsl easn.dA thsee csohniedldtrsa onfs tfhoerm caebrlreast. eAd s8e0c0oVndA ,tr4a0n0s/fo1r0m0Vera rcaatnedd 8D0y0n V1A1,i s40u0s/e1d00to Vsaucp apnldy
dDiyffne1re1n ist luosaedds tion sduepltpalyc odninffeecrteinotn l.oFaidgsu irne d14elstah ocwonsntehcetieoxnp. eFriigmuerne t1a4l ssehtouwpsa tnhde tehxepRerLimCefneatatul rseestuopf
tahnedl itnhee mRLoCdu fleeateumreusl aotfo trhseu lsiende. module emulators used.
FFiigguurree 1144.. EExxppeerriimmeennttaall sseettuupp.. 11: :PPrortoetcetcitoino nrerlealyasy;s 2;:2 A: uAxuilxiialriayr ypopwoewr esruspupplyp;l y3;: 3P:oPwoewr esrupsupplyp; l4y:;
4L:oLaodasd; s5;: 5G:rGoruonudn dfafualut lstwswitcithc;h 6;:6 T:rTarnansfsoformrmeer;r ;77: :PPCC; ;88: :CCaabbleless; ;99: :LLininee mmoodduulleess;; 1100:: RRLLCC ppaarraammeetteerrss
ooff tthhee lliinnee mmoodduulleess ((99)) uusseedd..
Several single ground faults at all phases in lines and cables were carried out in the network
Several single ground faults at all phases in lines and cables were carried out in the network
erected in the laboratory. Tests were developed at 100 V phase-to-phase voltage and load currents of
erectedinthelaboratory. Testsweredevelopedat100Vphase-to-phasevoltageandloadcurrents
less than 1 A with different cosφ values. The positions where the ground faults were developed
oflessthan1Awithdifferentcosφvalues. Thepositionswherethegroundfaultsweredeveloped
(indicated in Figure 15) are represented schematically in Figure 16.
(indicatedinFigure15)arerepresentedschematicallyinFigure16.

Energies2016,9,964 14of20
Energies 2016, 9, 964 14 of 21
Energies 2016, 9, 964 14 of 21
Figure 15. Ground fault positions. A: At the end of the cable; B: Between the first and second sections
FigFuigreur1e5 1.5G. rGoruonudndfa fualutlpt poosistiitoionnss..A A:: AAtt tthhee eenndd ooff tthhee ccaabbllee; ;BB: :BBeetwtweeenen thteh efirfisrts atnadn dsesceocnodn sdecsteioctnios ns
of the cables; C: Between the second and third sections of the cables; D: In the transition at the end of
ofothf ethcea bcalebsle;sC; :CB: eBtewtweeenent hthees eseccoonndda anndd tthhiirrdd sseeccttiioonnss ooff tthhee ccaabbleless; ;DD: :InIn thteh etrtarnasnitsiiotino ant athteth eenedn odf of
the cables; E: Between the first and second trams of the line modules; F: Behind the two line modules.
thethcea bcalebsl;esE;: EB: eBtewtweeenenth tehefi frisrtsta anndds seeccoonndd ttrraammss ooff tthhee lliinnee mmoodduuleless; ;FF: :BBehehinidn dthteh tewtwo loinlein meomdoudleusl.e s.
Figure 16. Ground fault positions: schematic representation.
FiFgiugurere1 166..G Grroouunndd ffaauulltt ppoossiittiioonnss:: sscchheemmaatitcic rereppreresesnentattaitoino.n .
6.2. Angle Analysis of the Experimental Power Distribution.
6.2. Angle Analysis of the Experimental Power Distribution.
6.2. AngleAnalysisoftheExperimentalPowerDistribution
In the experimental circuit test shown in Figure 16, the network is solidly grounded at the
In the experimental circuit test shown in Figure 16, the network is solidly grounded at the
begInintnhinege oxfp ethriem oevnetrahleacdir cluiniet tseidste swhhoewrenasi nthFei gtruarnesf1o6r,mtehre wnheitcwh osrukppisliesos ltihdely logardo uhnasd ead dealttat he
beginning of the overhead line side whereas the transformer which supplies the load has a delta
begcoinnnniencgtioonf itnh eitso hviegrhheera vdollitnagees sididee.w Thheer eaansguthlaer tdriaffnesrfeonrcmese rΔLw1hSi1c,h ΔsLu2pS2p lainesd tΔhLe3lSo3a odbhtaaisneadd inel ta
connection in its higher voltage side. The angular differences ΔL1S1, ΔL2S2 and ΔL3S3 obtained in
conthnee ctetisotsn iinn ai tssyhsitgemhe runvgorlotaugnedseidd ea.t Tthhee caanbgleu llainred siifdfeer eanncde sso∆liLd1lyS 1g,r∆ouLn2dSe2da antd th∆eL o3vSe3rohbeatadi nliende i n
the tests in a system ungrounded at the cable line side and solidly grounded at the overhead line
thesitdees twseirne:a system ungrounded at the cable line side and solidly grounded at the overhead line
side were:
side weGrer:ound fault in overhead side: if the angular difference between the active and respective
 Ground fault in overhead side: if the angular difference between the active and respective
shield of the currents in the phase with a fault is less than 50°.
• Grsohuienldd foafu tlhtei ncuorvreenrhtse aind tshied ep:hiafsteh weiatnhg au flaaurldt iisff leersesn tcheabne 5t0w°e. entheactiveandrespectiveshield
 Ground fault in the cable line side: if the angular difference between the active and respective
 ofGthreoucundrr efanutslt iinn tthhee pchabalsee lwiniet hsiadefa: uifl tthise laensgsuthlaarn d5if0f◦e.rence between the active and respective
shield of the currents in the phase with a fault is clearly over 50°.
• Gr s o h u ie n l d d o fa f u th lt e i c n u t r h re e n c t a s b in le th li e n e ph s a id se e : w if it t h h a e f a a n u g lt u i l s a c r le d a i r f l f y e r o e v n e c r e 5 b 0 e °. t weentheactiveandrespective
shiF
F
ei
i
lg
g
du
u
ro
r
e
e
fs
s
t h1
1
7
7
e a
a
cn
n
ud
d
rr 1
1
e8
8
n ts
s
sh
h
io
o
nw
w
t ht
t
h
h
ee
e
p a
a
hn
n
ag
g
su
u
el
l
a
a
wr
r
id
d
thi
i
f
f
f
f
ae
e
r
r
fe
e
an
n
uc
c
lte
e
ib
b
se
e
ct
t
lw
w
eae
e
re
e
ln
n
y p
p
oh
h
va
a
es
s
re
e
5 a
a
0n
n◦
d
d
. s
s
h
h
i
i
e
e
l
l
d
d
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
s
s
w
w
h
h
e
e
n
n
t
t
h
h
e
e
r
r
e
e
i
i
s
s
a ground fault in phase L1 in the overhead side at fault point E, and at the cable line side in fault
a ground fault in phase L1 in the overhead side at fault point E, and at the cable line side in fault
poFinigt uCr.e Tsh1e7 taensdt r1e8suslhtso winctlhuedaedn giunl aTrabdliefsfe 3re–n5 csehboewt wveaeluneps hoaf sveaarinadtiosnhsie ilnd ΔcuLr1rSe1n, tΔsLw2hSe2n atnhde re
point C. The test results included in Tables 3–5 show values of variations in ΔL1S1, ΔL2S2 and
ΔL3S3 over 50° and below 50° when the ground fault is developed at the overhead line side.
isagroundfaultinphaseL1intheoverheadsideatfaultpointE,andatthecablelinesideinfault
ΔL3S3 over 50° and below 50° when the ground fault is developed at the overhead line side.
pointC.ThetestresultsincludedinTables3–5showvaluesofvariationsin∆L1S1,∆L2S2and∆L3S3
over50◦ andbelow50◦ whenthegroundfaultisdevelopedattheoverheadlineside.

EEnneerrggiieess 22001166,, 99,, 996644 1155 ooff 2210
Energies 2016, 9, 964 15 of 21
Angle change between currents in conductors and shields.
Angle chaGngroeu bnedt wfaeueltn a ct utrhree notvse irnh ecoandd suidceto irns Ean.d shields.
-20 Ground fault at the overhead side in E.
-20
-40
-40 30.8º 27.2º
-60 30.8º 27.2º 32.3º
-60 32.3º
D e
gr e
e s
()º
e
gr e
e s
()º
-
-
1
1
-
-
8
0
8
0
0
0
0
0
D
-120 Angle difference Conductor L1/Shield S1
-120 AAnnggllee ddiiffffeerreennccee CCoonndduuccttoorr LL31//SShhiieelldd SS31
-140 AAnnggllee ddiiffffeerreennccee CCoonndduuccttoorr LL23//SShhiieelldd SS23
-140 Angle difference Conductor L2/Shield S2
-16
0
0
. 2 0.25 0.3 0.35 0.4 0.45 0.5
-16 0 0 . 2 0.25 0.3 Tim0.e3 5(s) 0.4 0.45 0.5
Time (s)
FFiigguurree 1177.. AAnngguullaarr ddiiffffeerreenncceess wwiitthh ggrroouunndd ffaauulltt aatt tthhee oovveerrhheeaadd ssiiddee iinn pphhaassee LL11.. FFaauulltt ppooiinntt EE..
Figure 17. Angular differences with ground fault at the overhead side in phase L1. Fault point E.
Angle difference between currents in conductors and shields
Angle diffweirtehn gcreo buentdw feaeunlt cinu rcraebnltes sinid ceo innd puhcatosres La1nd shields
with ground fault in cable side in phase L1
-50 0.2º
-50 0.2º
-100
9.82º
-100
9.82º
-150 64.89º
D e
gr e
e s
()º
D e gr e
e s
()º
-
-
-
-
-
2
2
2
2
1
5
0
5
0
5
0
0
0
0
0 64.89º
A AA n nn g gg l ll e ee d dd i ii f ff f ff e ee r rr e ee n nn c cc e ee C CC o oo n nn d dd u uu c cc t tt o oo r rr L LL 1 21 / // S SS h hh i ii e ee l ll d dd S SS 1 21
-300 AAnnggllee ddiiffffeerreennccee CCoonndduuccttoorr LL32 // SShhiieelldd SS32
-300 Angle difference Conductor L3 / Shield S3
-350
-350
-400
-4000.1 2 0.14 0.16 0.18 0.2 0.22 0.24 0.26 0.28 0.3
0.1 2 0.14 0.16 0.18 0.2Time (s0).22 0.24 0.26 0.28 0.3
Time (s)
Figure18.AngulardifferenceswithgroundfaultatthecablelinesideinphaseL1.FaultpointC.
Figure 18. Angular differences with ground fault at the cable line side in phase L1. Fault point C.
Figure 18. Angular differences with ground fault at the cable line side in phase L1. Fault point C.
TTaabblleess 33––55 sshhoowwt htheer eresusultlstso off∆ ΔLL1S11S,1∆, ΔL2LS22S2a nadnd∆ LΔ3LS33Si3n ignr oguronudnfdau flatullotc laotcioantisoAns, BA,,C B,, DC,i nDt hine
Tables 3–5 show the results of ΔL1S1, ΔL2S2 and ΔL3S3 in ground fault locations A, B, C, D in
tchaeb lcealbinlee lsinidee s,iadned, ainndl oinca ltoiocantsioEnasn Ed aFnadt Fth aet othvee rohveeardheliande lsinidee s.ide.
the cable line side, and in locations E and F at the overhead line side.
TTaabbllee 33..G Groruounnddf afualutlatt aotv eorvheerahdeaadn dacnadb lcealbinlee sliindee ssiindepsh ainse pLh1a.sVea rLia1t. ioVnairniaptihoans eina npghleasseb eatnwgeleens
Table 3. Ground fault at overhead and cable line sides in phase L1. Variation in phase angles
bcuetrwreenetns icnutrhreenctos nind uthcteo crosnadnudctthoerisr arnedsp tehcetiirv eresshpieecldtisv.e shields.
between currents in the conductors and their respective shields.
Fault at Cable Line Side
FaultatCableLineSide
Fault at Cable Line Side
Fault in Phase L1
FFaauulltt iinn PPhhaasseeL L11
Place of the Fault Variation in Phase Angles
PPllaaccee oofft htheeF aFualutlt VVaarriiaattiioonn iinn PPhhaasseeA Annglgelses
ΔL1S1 ΔL2S2 ΔL3S3
∆ΔLL11SS11 Δ∆LL22SS22 Δ∆LL33SS33
A 66.32° 11.02° 0.33°
A
A
B 66
6
65
6
.3.
.
9
3
23
2◦
°
°
1
1
101
1
..
.
02
0
24
2◦
°
°
0
0
0.
.
.2 3
36
3
3°
◦°
BB 6655.9.933◦° 1100..2244◦° 00..2266◦°
C 64.89° 9.82° 0.20°
CC 6644.8.899 ◦ ° 99..8822 ◦ ° 00..2200◦ °
D
D
6
6
4
4
.2 .2
5
5◦° 9
9.
.
3
3
1
1◦° 0
0
.
.
1
1
8
8
°◦
D 64.25° 9.31° 0.18°
Fault at Overhead Line Side
FaFuaultl taatt OOvveerrhheeaadd LLinineeS Sidiede
Fault in Phase L1
FFaauulltt iinn PPhhaasseeL L11
Place of the Fault Variation in Phase Angles
PPllaaccee oofft htheeF Faualutlt VVaarriiaattiioonn iinn PPhhaasseeA Annglgelses
ΔL1S1 ΔL2S2 ΔL3S3
E ∆Δ 3L0 L1. 1 8SS 01° 1 Δ∆ 32LL .22 3SS 12° 2 Δ 2 ∆ 7 LL. 3 13S 6S° 33
EF
E
32
3
09
0
.8.
.
1
8
02
0◦° °
3
3
312
2
..
.
38
3
16
1◦° °
2
2
26
7
7.
.
.0 1
12
6 6°◦°
FF 2299.1.122◦° 3311..8866◦° 2266..0022◦°

Energies2016,9,964 16of20
Table4.GroundfaultatoverheadandcablelinesidesinphaseL2.Variationinphaseanglesbetween
currentsintheconductorsandtheirrespectiveshields.
FaultatCableLineSide
FaultinPhaseL2
| PlaceoftheFault | VariationinPhaseAngles |        |
| --------------- | ---------------------- | ------ |
|                 | ∆L1S1 ∆L2S2            | ∆L3S3  |
|                 | 0.29◦ 66.45◦           | 12.08◦ |
A
|     | 0.25◦ 65.99◦ | 10.93◦ |
| --- | ------------ | ------ |
B
|     | 0.21◦ 65.02◦ | 9.88◦ |
| --- | ------------ | ----- |
C
|     | 0.16◦ 64.67◦ | 9.33◦ |
| --- | ------------ | ----- |
D
FaultatOverheadLineSide
FaultinPhaseL2
| PlaceoftheFault | VariationinPhaseAngles |        |
| --------------- | ---------------------- | ------ |
|                 | ∆L1S1 ∆L2S2            | ∆L3S3  |
| E               | 1.29◦ 31.78◦           | 16.29◦ |
| F               | 1.11◦ 25.11◦           | 12.11◦ |
Table5.GroundfaultatoverheadandcablelinesidesinphaseL3.Variationinphaseanglesbetween
currentsintheconductorsandtheirrespectiveshields.
FaultatCableLineSide
FaultinPhaseL3
PlaceoftheFault
VariationinPhaseAngles
|     | ∆L1S1 ∆L2S2  | ∆L3S3  |
| --- | ------------ | ------ |
| A   | 12.58◦ 0.30◦ | 67.34◦ |
| B   | 10.13◦ 0.26◦ | 66.86◦ |
| C   | 9.01◦ 0.20◦  | 65.78◦ |
| D   | 8.92◦ 0.18◦  | 64.02◦ |
FaultatOverheadLineSide
FaultinPhaseL3
| PlaceoftheFault | VariationinPhaseAngles |        |
| --------------- | ---------------------- | ------ |
|                 | ∆L1S1 ∆L2S2            | ∆L3S3  |
| E               | 17.34◦ 1.35◦           | 32.45◦ |
| F               | 14.22◦ 1.18◦           | 23.67◦ |
6.3. WaveletAnalysisoftheExperimentalPowerDistributionNetwork
ThecD1coefficientsobtainedfromtheangulardifferencesinthetestsbetweencurrentsinthe
shields and in the active cables in a system that is ungrounded at the cable line side and solidly
groundedattheoverheadlinesidewere:
• Groundfaultinoverheadlineside: ifthecD1coefficientvaluesarelowerthan50inallphases.
• Ground fault in the cable line side: if the cD1 coefficient values are much higher than 50,
i.e.,100ormore.
Figure19showsthedB2-cD1coefficientvaluesoftheangulardifferencebetweenphaseandshield
currentswhenthereisagroundfaultinphaseL1intheoverheadlinesideatfaultpointE.Thesevalues
of the dB2-cD1 coefficients are higher than the values obtained from the simulated case shown in
Figure12. Thisdifferenceisrelatedtothephysicaldisposaloftherealcablesinthelaboratorywhich
arewoundincoilsinsteadofbeenlaidunderthegroundastheywereconsideredinthesimulated
model. Figure20showsatthecablelinesideinfaultpointC.Table6showsthebigdifferencesinthe
valuesofthedB2-cD1coefficientsfromgroundfaultsattheoverheadlinesidetogroundfaultsatthe
cableside.

Energies2016,9,964 17of20
EEnneerrggiieess 22001166,, 99,, 996644 1177 ooff 2211
ddBB22--ccDD11 CCooeeffffiicciieennttss ffoorr ggrroouunndd ffaauulltt iinn pphhaassee LL11 aatt tthhee oovveerrhheeaadd ssiiddee iinn ppoossiittiioonn EE
44
d
B2-c D1
Co
efficie nts
d
B2-c D1
Co
efficie nts
-
-
-
-
4
2
0
2
4
2
0
2 00
4
.
4
.55 ..88
00..0033
d d d d B B B B 2 2 2 2 - - - - c c c c D D D D 1 1 1 1 c c c c o o o o e e e e f f f f f f f f i i i i c c c c i i i i e e e e n n n n t t t t s s s s C C C C o o o o n n n n d d d d u u u u c c c c t t t t o o o o r r r r L L L L 1 2 1 2 / / / / S S S S h h h h i i i i e e e e l l l l d d d d S S S S 1 2 1 2
--66
ddBB22--ccDD11 ccooeeffffiicciieennttss CCoonndduuccttoorr LL33 // SShhiieelldd SS33
00..0 0 88 00..008855 00..0099 TTi 0i 0 mm..00 ee9 9 ( 5( 5 ss)) 00..11 00..110055 00..1111
FigureFFi1igg9uu.rrWee 11a99v.. eWWleaatvvaeelnleeatt laaynnsaailslyyossiifss toohff e tthhaeen aagnnuggluuallraarrd ddifiiffffefeerrreeennnccceeesss wwwiiittthhh aaa ggrgrooruuonnuddn fdfaauuflalttu aalttt ttahhtee toohvveeerrohhveeeaadrdh lleiinnaeed ssilididneee iinns idein
phasepp Lhh 1aa .ss Fee
a
LL u11 l..
t
FF paauo uli ltt
n
pp too Eiinn .tt EE..
ddBB22--ccDD11 CCooeeffffiicciieenntt vvaalluueess ffoorr ggrroouunndd ffaauulltt iinn pphhaassee LL11 aatt tthhee ccaabbllee ssiiddee iinn llooccaattiioonn CC
2200
00
d B b
2-c D 1 C o effici e nt
d B b
2-c D 1 C o effici e nt V al u es V al u es
- - - - 1 1 1 1
- - - - - - - -
2 0
8 6 4 2
2 0
8 6 4 2
0 0
0 0 0 0
0 0
0 0 0 0 114422
d d d d d d B B B B B B
0
2 2 2
0
2 2 2
.
- - -
.8 - - -
8
c c c c c c D D D D D D 1 1 1 1 1 1 C C C C C C o o o o o o e e e e e e f f f f f f f f f f f f i i i i i i e e e e e e n n n n n n t t t t t t e e e e e e s s s s s s C C C C C C o o o o o o n n n n n n d d d d d d u u u u u u c c c c c c t t t t t t o o o o o o
77
r r r r r r
. . 2
L L L
2
L L L 1 2 3 1 2 3 / / / / / / S S S S S S h h h h h h i i i i i i e e e e e e l l l l l l d d d d d d S S S S S S 1 2 3 1 2 3
--114400
--116600
00..1155 00..1166 00..1177 00..1188 00..1199 00..22 00..2211 00..2222
TTiimmee ((ss))
FigureFFi2igg0uu.rrWee 2a20v0..e WWleatavvaeenlleaetlt y aasnniasallyoysfsiitssh ooeff atthnhege uaanlnaggruudllaairfr f dediriffeffneerrceeennsccewess i wtwhiittahh g aar oggurroonuudnndfda fufaaluutllatt taattt h ttheheec accabablbelleel illniinneee s ssiididdeee iininn phase
L1.Fapuphhltaaspseeo LLin11.t. FFCaa.uulltt ppooiinntt CC..
TableTT 6a. abblG lee r6o 6.. u GG nrd roouu fna ndu d lft faaua ult ltt oaa vtt eoo rvv hee err ahh deeaadd a n aa dnndd c acc baabl b ellee l illin inn eee sss iii dddee ess s.. . WW Waavv aee vllee ett l eaa tnn aaaln lyy assil isy s:: s ei e sxx :ppee err xiimm pee enn rti tam all err neess tua ull lttss r.. e sults.
OOvveerrhheeaadd lliinnee ssiiddee ssoolliiddllyy ggrroouunnddeedd aanndd ccaabbllee lliinnee ssiiddee iissoollaatteedd..
Overheadlinesidesolidlygroundedandcablelinesideisolated.
FFaauulltt aatt CCaabbllee LLiinnee SSiiddee FFaauulltt aatt OOvveerrhheeaadd LLiinnee SSiiddee
FaultatCableLineSFF iaa duu elltt iinn PPhhaassee LL11 FaultatOveFF raa huu ellta t diinn
L
PP ihh naa essee
S
LL id11
e
LLooccaattiioonn ooff tthhee FFaauulltt WW ((ddBB22--ccDD11 CCooeeffffiicciieennttss)) LLooccaattiioonn ooff tthhee FFaauulltt WW ((ddBB22--ccDD11 CCooeeffffiicciieennttss))
F ΔΔa LLu 11S lSt 11 i nP ΔΔh LL2 a2S sS2 e2 L1 ΔΔLL33SS33 ΔΔLL11SS11 ΔΔLLF 22a SSu 22 l ti Δ nΔLLP 33S hS3 a3 seL1
LocationoftheFaA B A B u lt W(d1 1 1 1 B5 4 5 4 2 5 2 2 5 . . - . . 2 8 2 8 c4 8 4 8 D 1C2 1 2 1 o. . . . 4 9 4 9 e5 6 5 6 f ficie1 1 n 1 1 8 4 8 4 t. . s . . 2 1 2 1 )9 2 9 2 Locatio E nE oftheFault 44..8800 W( 00d ..00B 332 -cD1 00. C.5500o efficients)
A D
C
D
C ∆
15
L
2
1
.
S
2
1
14
1
1
1 4
3
4
3
2
6
2
6
.
.
.
.
0
5
0
5
1
4
1
4
∆
2
L
.
2
4
S
5
0
0
0
0
.
.
2.
.
8
6
8
6
0
9
0
9
∆
1
L
8
7
4
7
4
3
.
.
.2 .
.
2
7
S2
7 9
1
5
1
5
3 FF 44..6666 ∆L1 00 S ..0 1 022 ∆L 00 2 ..44 S 22 2 ∆L3S3
B FFaauulltt a1 att 4 CC 5a. a 8bb 8llee LLiinnee 1 SS .9iid6 dee 14.12 FFaaE uulltt aatt OOvveerrhheeaadd LLiinn4 ee. 8 SS0 iiddee 0.03 0.50
C 142.01 FFaauu 0llt. t 8 iin0 n PPhhaassee L7 L2. 2 2 1 FFaauulltt iinn PPhhaassee LL22
LL Dooccaattiioonn ooff tthhee FFaauu 1ll 3tt
6
.5WW
4
((ddBB22-0 -cc .DD 6911 CCooeeffffiic4 cii .ee 7nn 5ttss)) LLooccaattiioonn ooff tth Fhee FFaauulltt WW ((ddBB22--4 ccD .D6 116 CCooeeffffiicc0 iie .e0 nn2 ttss)) 0.42
ΔΔLL11SS11 ΔΔLL22SS22 ΔΔLL33SS33 ΔΔLL11SS11 ΔΔLL22SS22 ΔΔLL33SS33
Faul A B At B a tCableLi F n 2 1 2 1a e 0 6 0 6u . . . . S 0 5 0 5l 4 9 4 9t i d in e P 1 1 1 1 5 4h 5 4 4 8 4 8a . . . . 3 2s 3 2 1 2e 1 2 L2 3 2 3 2 . . . . 0 4 0 4 1 2 1 2 EE FaultatO 00 v ..00 e 44 r head 44 F . L .88 a i 88 n u e lt S in id 00. P . e 55 h 99 aseL2
LocationoftheFa D C D C u lt W(dB 9 6 9 6 . . 2 . . 9 8 9 8- 2 2 2 2c D1C 1 1 1 1 4 3 4 3o 3 8 3 8e . . . . 6 0 6 0f 7 8 7 8fi cien 0 0 0 0t . . . . 8 8 s 8 8 9 2 9 2) LocatioFnF oftheFault00..0033 W(44d..77B222 -cD100.C.4488o efficients)
FFaauulltt a∆attL CC1aaSbb1llee LLiinn∆eeL SS2iidSdee2 ∆L3S3 FFaauulltt aatt OOvveerrhheeaadd LL∆iinnLee 1 SSSiid1dee ∆L2S2 ∆L3S3
FFaauulltt iinn PPhhaassee LL33 FFaauulltt iinn PPhhaassee LL33
A 20.04 154.31 3.01
LLooccaattiioonn ooff tthhee FFaauulltt WW ((ddBB22--ccDD11 CCooeeffffiicciieennttss)) LLooccaattiioonn ooff tthEhee FFaauulltt WW ((ddBB22--0ccD.D0114 CCooeeffffiicc4iie.e8nn8ttss)) 0.59
B 16.59 148.22 2.42
ΔΔLL11SS11 ΔΔLL22SS22 ΔΔLL33SS33 ΔΔLL11SS11 ΔΔLL22SS22 ΔΔLL33SS33
C 9.92 143.67 0.89
D A B A B 6.82 2 1 2 1 . . . . 6 4 6 4 6 9 6 9 138. 1 1 1 1 0 9 5 9 5 8 . . . . 4 1 4 1 4 8 4 8 0 1 1 1 1 . 5 4 5 4 8 3 4 3 4 2 . . . . 0 7 0 7 1 8 1 8 EE F 00..4477 0.0 003 ..0044 4 44. . 7.332 44 0.48
Faul
D
C
D
tC a tCableLin0
0
e0
0
.
.
.
.
8
5
8
5
S1
2
1
2
i de 6
3
6
3
.
.
.
.
9
9
9
9
6
7
6
7
1
1
1
1
4
3
4
3
0
4
0
4
.
.
.
.
1
9
1
9
2
6
2
6
FF FaultatO 00 v ..55 e 11 r head 00. L .00 i 22 n eSid 44.. e 1111
FaultinPhaseL3 FaultinPhaseL3
LocationoftheFault W(dB2-cD1Coefficients) LocationoftheFault W(dB2-cD1Coefficients)
∆L1S1 ∆L2S2 ∆L3S3 ∆L1S1 ∆L2S2 ∆L3S3
A 2.66 19.44 153.01
E 0.47 0.04 4.34
B 1.49 15.18 144.78
C 0.81 6.96 140.12
F 0.51 0.02 4.11
D 0.52 3.97 134.96

Energies2016,9,964 18of20
7. ConclusionsandFutureWork
Anewauto-reclosingblockingmethodforcombinedoverhead-cablelinesinpowerdistribution
networks has been presented in this article. This method is applicable when the transition
overhead-cableisclosetothesubstationwherethemeasurementsofcurrentsinshieldsandconductors
aredone.Theshieldsofthecablesaregroundedatbothends.Theproposedgroundfaultauto-reclosing
methodisbasedontwoanalyses. Thefirstevaluatesthedifferencebetweenthecurrentsintheactive
partofthecableandthoseintheshields,whereasthesecondanalysisusesthewaveletDaubechiesdB2
andextractsthecoefficientscD1fromthesamedifferencesusedinthefirstanalysis. Iftheargument
differencesbetweenthecurrentsintheconductorsofthecableandthoseintheshieldshaveaphase
variationjustafteragroundfaultoccurswithhighervaluesthanareferencedifferenceand,atthe
sametime,theDaubechies-cD1coefficientsofsuchdifferenceshavevaluesoverareferencethreshold,
then a ground fault has occurred in the cable line side and the reclosing is blocked. On the other
hand,ifthephasevariationjustafteragroundfaulttakesplacebetweenthecurrentsintheconductor
ofthecableandthoseintheshieldshaslowervaluesthanareferenceargumentdifference,andthe
Daubechies-cD1coefficientsofsuchavariationhaveverysmallvalues,thegroundfaulthasoccurred
attheoverheadlineside,andthereclosingisreleased.
Thesimulationsturnedouttobetotallysatisfactoryandtheexperimentalresultsofthelaboratory
testsshowedthatthelocalizationofthegroundfaultiscorrect. Thisnoveltechniquehasimportant
advantagescomparedtoup-and-runninggroundfaultdetectionsystems:
• Itdiscriminateswhetheragroundfaulthappensattheoverheadlinesideorcablelineside;
• Itdoesnotuseanyvoltagemeasurement;
• Itdoesnotuseanydirectionalcriterion;
• Itdoesnotusetheresidualgroundfaultcurrenttolocalizethegroundfault;
• Itdoesnotconsideranydistancecalculationtolocalizethegroundfault;
• Itdoesnotconsideranydifferentialtrippingcriteriontolocalizethegroundfault.
Theaforementionedadvantagesoftheproposedtechniquemakeiteasiertodeterminewhere
thegroundfaultisand,consequently,toallowtheprotectionrelaytomakethebestpossibleuseof
theauto-reclosingfunctionality. Thestabilityofthegridisalsoimprovedbecausewrongreclosing
commandsarenotsentwhilegroundfaultconditionsareactive.
Acknowledgments:Theauthorswishtothankthereviewersfortheirhelpfulandconstructivecomments.
Author Contributions: Ricardo Granizo Arrabé developed the study and included all the mathematical
formulations of the cables in the simulated models. Carlos Antonio Platero Gaona and Fernando Álvarez
Gómezperformedthelaboratorytestsandcheckedthevalidityofthenewauto-reclosingblockingmethod.Emilio
RebolloLópezrevisedandimprovedtheMatlab-Simulink®model.Alltheauthorscontributedtowritingthis
article,includingtheirconceptualapproachestothesolutionobtained.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
Abbreviations
Thefollowingabbreviationsareusedthroughoutthearticle:
AC AlternatingCurrent
AND LogicalFunction
CT CurrentTransformer
cD DetailCoefficient
DWT DiscreteWaveletTransformation
Dyn1 Delta-StarwithGroundConnectionofPowerTransformer
Dyn11 Delta-StarwithGroundConnectionofDistributionTransformer
dB2 Daubechies2MotherWavelet
GMD GeometricMeanDistance
HF HighFrequency
LF LowFrequency
SB SingleBonding
∆LiSj variationoftheargumentdifferencebetweenthecurrentinphaseiandthatinshieldj

Energies2016,9,964 19of20
IndicesandSets
i Indexofeachconductor
j Indexofeachshield
k Indexofeachlevelofdetailcoefficientsinwaveletanalysis
m Indexofeachlevelofapproximationcoefficientsinwaveletanalysis
Parameters
A,B,C,D,E,F groundfaultsituationinlaboratorytests
Am approximationlevel“m”forwaveletanalysis
C zerosequencecapacitancevalue
0
C directsequencecapacitancevalue
1
C negativesequencecapacitancevalue
2
De equivalentdistanceforgroundreturn
Dm detaillevel“m”ofwaveletanalysis
f frequency
fs samplingfrequency
I groundfaultcurrent
0
I currentinconductor1
1
I currentinconductor2
2
I currentinconductor3
3
j imaginarypartofcomplexvector
L lengthoftheconductor
L1 phaseone
L2 phasetwo
L3 phasethree
L zerosequenceinductancevalue
0
L directsequenceinductancevalue
1
L negativesequenceinductancevalue
2
ln logarithm
R realpartorresistanceofanyimpedance
R resistanceoftheconductorinAC
C(ac)
R zerosequenceresistancevalue
0
R directsequenceresistancevalue
1
roc outerradiusoftheconductor
rs averageradiusoftheshield
R resistanceoftheshieldinAC
S(ac)
R groundresistanceofsubstationA
SA
R groundresistanceofsubstationB
SB
Rt groundresistanceofanytowerofdistributionlines
S1 shieldofconductorinphaseL1
S2 shieldofconductorinphaseL2
S3 shieldofconductorinphaseL3
S distancebetweenaxesofconductorandshield
CS
S distancebetweenaxesofshields
SS
t trippingtimeforimpedancezoneA
A
t trippingtimeforimpedancezoneB
B
t trippingtimeforimpedancezoneC
C
U voltagedifferencebetweenshieldends
U inducedvoltageinshield1ofconductor1duetocirculatingcurrentsinconductors
1C
U inducedvoltageinshield2ofconductor2duetocirculatingcurrentsinconductors
2C
U inducedvoltageinshield3ofconductor3duetocirculatingcurrentsinconductors
3C
U inducedvoltageinshield1ofconductor1duetocirculatingcurrentsinshields
1S
U inducedvoltageinshield2ofconductor2duetocirculatingcurrentsinshields
2S
U inducedvoltageinshield3ofconductor3duetocirculatingcurrentsinshields
3S
U residualvoltage
0
X imaginarypartorreactanceofanyimpedance
Z self-impedanceofaconductor
C
Z mutualimpedancebetweenconductorandshield
CS
Z impedancezoneI
I
Z lineimpedance
L
Z self-impedanceofashield
S
Z mutualimpedancebetweenshields
SS

Energies2016,9,964 20of20
References
1. Tleis,N.PowerSystemsModellingandFaultAnalysis,1sted.;Newnes:Oxford,UK,2008.
2. Saha,M.M.;Izykowsky,J.;Rosolowsky,E.FaultLocationonPowerNetworks;Springer:Berlin,Germany,2009.
3. Horowitz,S.H.;Phadke,A.G.PowerSystemRelaying,3rded.;Wiley:NewYork,NY,USA,2008.
4. L’Abbate,A.;Fulli,G.;Starr,F.;Peteves,S.DistributedPowerGenerationinEurope:TechnicalIssuesforFurther
Integration;JRCEuropeanCommissionScientificandTechnicalReport,EUR23234EN;OfficeforOfficial
PublicationsoftheEuropeanCommunities:Luxembourg,2007.
5. Tamo,T.;Voufo,J.Faultdiagnosisonmediumvoltage(MV)electricpowerdistributionnetworks:Thecase
ofthedownstreamnetworkoftheAES-SONELNgoussosub-station.Energies2009,2,243–257.
6. Li,P.;Zhang,B.H.;Hao,Z.G.;Rao,Y.F.;Wang,Y.T.;Bo,Z.Q.;Klimek,A.;Zhao,Q.;He,W.OptimalReclosing
TimeofTransmissionLinesanditsApplicationinRealPowerSystem.InProceedingsofthe9thInternational
ConferenceonDevelopmentsinPowerSystemProtection,Glasgow,UK,17–20March2008.
7. He,R.W.ANewApproachtotheCalculationofReclosingTimeforAdaptiveAuto-reclosure.InProceedings
ofthe2010Asia-PacificPowerandEnergyEngineeringConference,Chengdu,China,28–31March2010.
8. Zoro,R.;Mefiardhi,R.Lightningperformanceonoverheaddistributionlines: FieldobservationatWest
Java—Indonesia. In Proceedings of the 7th International Power Engineering Conference, Singapore,
29November–2December2005.
9. Yu,Y.Z.; Qin,J.; Li,G.X.; Chen,S.Y.; Li,J.; Chen,Y.Y.ASurveyonFaultLocationMethodsforHybrid
TransmissionLinesConsistingofPowerCablesandOverheadLines.PowerSyst.Technol.2006,30,64–69.
10. StandardCEI_60909-3. Short-CircuitCurrentCalculationinThree-Phasea.c. Systems. Part3. Currents
during Two Separate Simultaneous Single Phase Line-to-Earth Short Circuits and Partial Short-Circuit
CurrentsFlowingthroughEarth.Availableonline:https://webstore.iec.ch/publication/3890(accessedon
17November2016).
11. Radojevic,Z.; Terzija,V.TwoTerminalsNumericalAlgorithmforFaultDistanceCalculationandFault
Analysis. InProceedingsofthe2006IEEEPESPowerSystemsConferenceandExposition,Atlanta,GA,
USA,29October–1November2006.
12. Zhou,Y.;Xu,G.;Chen,Y.FaultLocationinPowerElectricalTractionLineSystem.Energies2012,5,5002–5018.
[CrossRef]
13. Terzija,V.V.;Dobrijevic,D.M.ShortCircuitStudiesinTransmissionNetworksUsingImprovedFaultModel.
InProceedingsoftheIEEELausannePowerTech,Lausanne,Switzerland,1–5July2007.
14. Simón,P.;Garnacho,F.;Moreno,J.;González,A.CálculoyDiseñodeLíneasEléctricasdeAltaTensión;Ibergarceta
Publicaciones,S.L.:Madrid,Spain,2011.
15. Magnago, F.H.; Abur, A. Fault location using wavelets. IEEE Trans. Power Deliv. 1998, 13, 1475–1480.
[CrossRef]
16. Costa,F.B.;Souza,B.A.;Brito,N.S.D.Real-timeclassificationoftransmissionlinefaultsbasedonmaximal
overlapdiscretewavelettransform.InProceedingsofthe2012IEEE/PESTransmissionandDistribution
ConferenceandExposition,Orlando,FL,USA,7–10May2012.
17. Han, J.; Crossley, P.A. Fault location on a mixed overhead and underground transmission feeder
usingamultiple-zonequadrilateralimpedancerelayandadouble-endedtravellingwavefaultlocator.
InProceedingsofthe201412thInternationalConferenceonDevelopmentsinPowerSystemProtection,
Copenhagen,Denmark,31March–3April2014.
18. Huang, J.G.; Hu, X.Y.; Li, X.S.; Hu, H.M.; Lv, Y.P. A Novel Single-Phase Earth Fault Feeder Detection
byTravelingWaveandWavelets. InProceedingsofthe2006InternationalConferenceonPowerSystem
Technology,Chongqing,China,22–26October2006.
19. Martínez,F.; Peris,A.; Rodenas,F.TratamientodeSeñalesDigitalesMedianteWaveletsysuusoconMatlab;
EditorialClubUniversitario:Alicante,Spain,2004.
20. Hong,Y.Y.;Wei,Y.H.;Chang,Y.R.;Lee,Y.D.;Liu,P.W.FaultDetectionandLocationbyStaticSwitchesin
MicrogridsUsingWaveletTransformandAdaptiveNetwork-BasedFuzzyInferenceSystem.Energies2014,
7,2658–2675.[CrossRef]
©2016bytheauthors;licenseeMDPI,Basel,Switzerland. Thisarticleisanopenaccess
articledistributedunderthetermsandconditionsoftheCreativeCommonsAttribution
(CC-BY)license(http://creativecommons.org/licenses/by/4.0/).