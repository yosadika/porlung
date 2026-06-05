| COMPUTER |       | RELAYING |
| -------- | ----- | -------- |
| FOR      | POWER | SYSTEMS  |

COMPUTER
RELAYING FOR
POWER SYSTEMS
Second Edition
Arun G. Phadke
UniversityDistinguishedProfessorEmeritus
TheBradleyDepartmentofElectricalandComputerEngineering
VirginiaTech,Blacksburg,Virginia,USA
James S. Thorp
HughP.andEthelC.KelleyProfessorandDepartmentHead
TheBradleyDepartmentofElectricalandComputerEngineering
VirginiaTech,Blacksburg,Virginia,USA
A John Wiley and Sons, Ltd., Publication Research Studies Press Limited

Copyright2009 ResearchStudiesPressLimited,16CoachHouseCloisters,10HitchinStreet,Baldock,
Hertfordshire,SG76AE
Publishedby JohnWiley&SonsLtd,TheAtrium,SouthernGate,Chichester,
WestSussexPO198SQ,England
Telephone(+44)1243779777
Email(forordersandcustomerserviceenquiries):cs-books@wiley.co.uk
VisitourHomePageonwww.wileyeurope.comorwww.wiley.com
ThisWorkisaco-publicationbetweenResearchStudiesPressLimitedandJohnWiley&Sons,Ltd.
Thiseditionfirstpublished2009
Allrightsreserved.Nopartofthispublicationmaybereproduced,storedinaretrievalsystem,ortransmitted,in
anyformorbyanymeans,electronic,mechanical,photocopying,recordingorotherwise,exceptaspermittedby
theUKCopyright,DesignsandPatentsAct1988,withoutthepriorpermissionofthepublisher.
Wileyalsopublishesitsbooksinavarietyofelectronicformats.Somecontentthatappearsinprintmaynotbe
availableinelectronicbooks.
Designationsusedbycompaniestodistinguishtheirproductsareoftenclaimedastrademarks.Allbrandnames
andproductnamesusedinthisbookaretradenames,servicemarks,trademarksorregisteredtrademarksoftheir
respectiveowners.Thepublisherisnotassociatedwithanyproductorvendormentionedinthisbook.This
publicationisdesignedtoprovideaccurateandauthoritativeinformationinregardtothesubjectmattercovered.
Itissoldontheunderstandingthatthepublisherisnotengagedinrenderingprofessionalservices.Ifprofessional
adviceorotherexpertassistanceisrequired,theservicesofacompetentprofessionalshouldbesought.

MATLAB MATLABandanyassociatedtrademarksusedinthisbookaretheregisteredtrademarksofThe
MathWorks,Inc.
LibraryofCongressCataloguing-in-PublicationData:
Phadke,ArunG.
Computerrelayingforpowersystems/ArunG.Phadke. – 2nded.
p.cm.
Includesbibliographicalreferencesandindex.
ISBN978-0-470-05713-1(cloth)
1.Protectiverelays.2.Electricpowersystems–Protection–Dataprocessing.I.Title.
TK2861.P482009
621.31(cid:1)7–dc22
2009022672
AcataloguerecordforthisbookisavailablefromtheBritishLibrary.
ISBN978-0-470-05713-1 (Hbk)
Typesetin11/13TimesbyLaserwordsPrivateLimited,Chennai,India.
PrintedandboundinGreatBritainbyAntonyRoweLtd,Chippenham,Wiltshire

CONTENTS
|     | About         | the Authors   |                 |               |                 |                       | xi   |
| --- | ------------- | ------------- | --------------- | ------------- | --------------- | --------------------- | ---- |
|     | Preface       | to            | the First       | Edition       |                 |                       | xiii |
|     | Preface       | to            | the Second      |               | Edition         |                       | xv   |
|     | Glossary      | of            | Acronyms        |               |                 |                       | xvii |
| 1   | Introduction  |               | to              | computer      | relaying        |                       | 1    |
| 1.1 | Development   |               | of              | computer      | relaying        |                       | 1    |
| 1.2 | Historical    |               | background      |               |                 |                       | 2    |
| 1.3 | Expected      |               | benefits        | of computer   |                 | relaying              | 3    |
|     | 1.3.1         | Cost          |                 |               |                 |                       | 3    |
|     | 1.3.2         | Self-checking |                 |               | and reliability |                       | 4    |
|     | 1.3.3         | System        |                 | integration   | and             | digital environment   | 4    |
|     | 1.3.4         | Functional    |                 | flexibility   |                 | and adaptive relaying | 5    |
| 1.4 | Computer      |               | relay           | architecture  |                 |                       | 6    |
| 1.5 | Analog        | to            | digital         | converters    |                 |                       | 12   |
|     | 1.5.1         | Successive    |                 | approximation |                 | ADC                   | 13   |
|     | 1.5.2         | Delta-sigma   |                 | ADC           |                 |                       | 15   |
| 1.6 | Anti-aliasing |               | filters         |               |                 |                       | 16   |
| 1.7 | Substation    |               | computer        | hierarchy     |                 |                       | 19   |
| 1.8 | Summary       |               |                 |               |                 |                       | 21   |
|     | Problems      |               |                 |               |                 |                       | 21   |
|     | References    |               |                 |               |                 |                       | 22   |
| 2   | Relaying      |               | practices       |               |                 |                       | 25   |
| 2.1 | Introduction  |               | to              | protection    | systems         |                       | 25   |
| 2.2 | Functions     |               | of a protection |               | system          |                       | 26   |
| 2.3 | Protection    |               | of transmission |               | lines           |                       | 30   |
|     | 2.3.1         | Overcurrent   |                 | relays        |                 |                       | 30   |
|     | 2.3.2         | Directional   |                 | relays        |                 |                       | 32   |

vi CONTENTS
|     | 2.3.3        | Distance    |          | relays       |                |              |                     | 35  |
| --- | ------------ | ----------- | -------- | ------------ | -------------- | ------------ | ------------------- | --- |
|     | 2.3.4        | Phasor      |          | diagrams     | and            | R-X diagrams |                     | 38  |
|     | 2.3.5        | Pilot       | relaying |              |                |              |                     | 39  |
| 2.4 | Transformer, |             | reactor  |              | and generator  |              | protection          | 40  |
|     | 2.4.1        | Transformer |          | protection   |                |              |                     | 40  |
|     | 2.4.2        | Reactor     |          | protection   |                |              |                     | 43  |
|     | 2.4.3        | Generator   |          | protection   |                |              |                     | 43  |
| 2.5 | Bus          | protection  |          |              |                |              |                     | 44  |
| 2.6 | Performance  |             | of       | current      | and            | voltage      | transformers        | 45  |
|     | 2.6.1        | Current     |          | transformers |                |              |                     | 45  |
|     | 2.6.2        | Voltage     |          | transformers |                |              |                     | 47  |
|     | 2.6.3        | Electronic  |          | current      |                | and voltage  | transformers        | 48  |
| 2.7 | Summary      |             |          |              |                |              |                     | 51  |
|     | Problems     |             |          |              |                |              |                     | 51  |
|     | References   |             |          |              |                |              |                     | 53  |
| 3   | Mathematical |             |          | basis        | for protective |              | relaying algorithms | 55  |
| 3.1 | Introduction |             |          |              |                |              |                     | 55  |
| 3.2 | Fourier      | series      |          |              |                |              |                     | 55  |
|     | 3.2.1        | Exponential |          | fourier      |                | series       |                     |     |
58
|     | 3.2.2        | Sine         | and     | cosine        | fourier | series           |               | 60  |
| --- | ------------ | ------------ | ------- | ------------- | ------- | ---------------- | ------------- | --- |
|     | 3.2.3        | Phasors      |         |               |         |                  |               | 62  |
| 3.3 | Other        | orthogonal   |         | expansions    |         |                  |               | 62  |
|     | 3.3.1        | Walsh        |         | functions     |         |                  |               | 63  |
| 3.4 | Fourier      | transforms   |         |               |         |                  |               | 63  |
|     | 3.4.1        | Properties   |         | of            | fourier | transforms       |               | 69  |
| 3.5 | Use          | of fourier   |         | transforms    |         |                  |               | 80  |
|     | 3.5.1        | Sampling     |         |               |         |                  |               | 81  |
| 3.6 | Discrete     |              | fourier | transform     |         |                  |               | 83  |
| 3.7 | Introduction |              | to      | probability   |         | and random       | process       | 86  |
|     | 3.7.1        | Random       |         | variables     |         | and probability  | distributions | 86  |
|     | 3.7.2        | Probability  |         | distributions |         | and              | densities     | 87  |
|     | 3.7.3        | Expectation  |         |               |         |                  |               | 89  |
|     | 3.7.4        | Jointly      |         | distributed   |         | random variables |               | 90  |
|     | 3.7.5        | Independence |         |               |         |                  |               | 91  |
|     | 3.7.6        | Linear       |         | estimation    |         |                  |               | 92  |
|     | 3.7.7        | Weighted     |         | least         | squares |                  |               |     |
93
| 3.8  | Random     |           | processes |           |     |           |     | 94  |
| ---- | ---------- | --------- | --------- | --------- | --- | --------- | --- | --- |
|      | 3.8.1      | Filtering |           | of random |     | processes |     | 97  |
| 3.9  | Kalman     |           | filtering |           |     |           |     | 98  |
| 3.10 | Summary    |           |           |           |     |           |     | 103 |
|      | Problems   |           |           |           |     |           |     | 103 |
|      | References |           |           |           |     |           |     | 108 |

| CONTENTS |               |                       |               |               |              |              |           | vii |
| -------- | ------------- | --------------------- | ------------- | ------------- | ------------ | ------------ | --------- | --- |
| 4        | Digital       | filters               |               |               |              |              |           | 109 |
| 4.1      | Introduction  |                       |               |               |              |              |           | 109 |
| 4.2      | Discrete      |                       | time systems  |               |              |              |           | 109 |
|          | 4.2.1         | Operations            |               | on            | discrete     | time         | sequences | 110 |
|          | 4.2.2         | Convolution           |               |               |              |              |           | 110 |
| 4.3      | Discrete      |                       | time systems  |               |              |              |           | 112 |
| 4.4      | Z Transforms  |                       |               |               |              |              |           | 113 |
|          | 4.4.1         | Power                 |               | series        |              |              |           | 113 |
|          | 4.4.2         | Z                     | Transforms    |               |              |              |           | 114 |
|          | 4.4.3         | Inverse               |               | Z transforms  |              |              |           | 115 |
|          | 4.4.4         | Properties            |               | of            | Z transforms |              |           | 116 |
|          | 4.4.5         | Discrete              |               | time          | fourier      | transform    |           | 118 |
| 4.5      | Digital       | filters               |               |               |              |              |           | 119 |
| 4.6      | Windows       |                       | and windowing |               |              |              |           | 121 |
| 4.7      | Linear        | phase                 |               |               |              |              |           | 122 |
| 4.8      | Approximation |                       |               | – filter      | synthesis    |              |           | 124 |
| 4.9      | Wavelets      |                       |               |               |              |              |           | 126 |
| 4.10     | Elements      |                       | of artificial |               | intelligence |              |           | 129 |
|          | 4.10.1        | Artificial            |               | neural        | networks     |              |           | 129 |
|          | 4.10.2        | Decision              |               | trees         |              |              |           | 131 |
|          | 4.10.3        | Agents                |               |               |              |              |           | 132 |
| 4.11     | Conclusion    |                       |               |               |              |              |           | 133 |
|          | Problems      |                       |               |               |              |              |           | 133 |
|          | References    |                       |               |               |              |              |           | 135 |
| 5        | Transmission  |                       |               | line relaying |              |              |           | 137 |
| 5.1      | Introduction  |                       |               |               |              |              |           | 137 |
| 5.2      | Sources       | of                    | error         |               |              |              |           | 142 |
| 5.3      | Relaying      |                       | as parameter  |               | estimation   |              |           | 147 |
|          | 5.3.1         | Curve                 |               | fitting       | algorithms   |              |           | 149 |
|          | 5.3.2         | Fourier               |               | algorithms    |              |              |           | 149 |
|          | 5.3.3         | Fourier               |               | algorithms    |              | with shorter | windows   | 151 |
|          | 5.3.4         | Recursive             |               | forms         |              |              |           | 152 |
|          | 5.3.5         | Walsh                 |               | function      | algorithms   |              |           | 154 |
|          | 5.3.6         | Differential-equation |               |               |              | algorithms   |           | 155 |
|          | 5.3.7         | Kalman                |               | filter        | algorithms   |              |           | 162 |
|          | 5.3.8         | Removal               |               | of the        | DC           | offset       |           |     |
163
| 5.4 | Beyond      | parameter      |           | estimation |          |       |       | 166 |
| --- | ----------- | -------------- | --------- | ---------- | -------- | ----- | ----- | --- |
|     | 5.4.1       | Relay          | programs  |            | based    | upon  | fault |     |
|     |             | classification |           |            |          |       |       | 166 |
| 5.5 | Symmetrical |                | component |            | distance | relay |       | 170 |
|     | 5.5.1       | SCDFT          |           |            |          |       |       | 172 |
|     | 5.5.2       | Transient      |           | monitor    |          |       |       | 174 |

| viii |       |       |     |                      |     |     | CONTENTS |     |
| ---- | ----- | ----- | --- | -------------------- | --- | --- | -------- | --- |
|      | 5.5.3 | Speed |     | reach considerations |     |     |          |     |
176
|     | 5.5.4 | A        | relaying | program      |     |     |     | 180 |
| --- | ----- | -------- | -------- | ------------ | --- | --- | --- | --- |
| 5.6 | Newer | analytic |          | techniques   |     |     |     | 182 |
|     | 5.6.1 | Wavelet  |          | applications |     |     |     |     |
182
|     | 5.6.2        | Agent       | applications     |             |            |          |           | 182 |
| --- | ------------ | ----------- | ---------------- | ----------- | ---------- | -------- | --------- | --- |
| 5.7 | Protection   |             | of series        | compensated |            | lines    |           | 183 |
| 5.8 | Summary      |             |                  |             |            |          |           | 185 |
|     | Problems     |             |                  |             |            |          |           | 185 |
|     | References   |             |                  |             |            |          |           | 186 |
| 6   | Protection   |             | of transformers, |             |            | machines | and buses | 189 |
| 6.1 | Introduction |             |                  |             |            |          |           | 189 |
| 6.2 | Power        | transformer |                  | algorithms  |            |          |           | 190 |
|     | 6.2.1        | Current     |                  | derived     | restraints |          |           | 191 |
|     | 6.2.2        | Voltage     |                  | based       | restraints |          |           | 194 |
|     | 6.2.3        | Flux        | restraint        |             |            |          |           | 195 |
6.2.4 A restraint function based on the gap in inrush current 199
| 6.3 | Generator       |              | protection    |             |               |           |           | 200 |
| --- | --------------- | ------------ | ------------- | ----------- | ------------- | --------- | --------- | --- |
|     | 6.3.1           | Differential |               | protection  |               | of stator | windings  | 200 |
|     | 6.3.2           | Other        | generator     |             | protection    |           | functions | 202 |
|     | 6.3.3           | Sampling     |               | rates       | locked        | to system | frequency | 203 |
| 6.4 | Motor           | protection   |               |             |               |           |           | 204 |
| 6.5 | Digital         | bus          | protection    |             |               |           |           | 204 |
| 6.6 | Summary         |              |               |             |               |           |           | 208 |
|     | Problems        |              |               |             |               |           |           | 209 |
|     | References      |              |               |             |               |           |           | 210 |
| 7   | Hardware        |              | organization  |             | in integrated |           | systems   | 213 |
| 7.1 | The             | nature       | of hardware   |             | issues        |           |           | 213 |
| 7.2 | Computers       |              | for           | relaying    |               |           |           | 214 |
| 7.3 | The             | substation   |               | environment |               |           |           | 216 |
| 7.4 | Industry        |              | environmental |             | standards     |           |           | 217 |
| 7.5 | Countermeasures |              |               | against     | EMI           |           |           | 220 |
| 7.6 | Supplementary   |              |               | equipment   |               |           |           | 222 |
|     | 7.6.1           | Power        |               | supply      |               |           |           | 222 |
|     | 7.6.2           | Auxiliary    |               | relays      |               |           |           | 222 |
|     | 7.6.3           | Test         | switches      |             |               |           |           | 222 |
|     | 7.6.4           | Interface    |               | panel       |               |           |           | 223 |
| 7.7 | Redundancy      |              | and           | backup      |               |           |           | 223 |
| 7.8 | Servicing,      |              | training      | and         | maintenance   |           |           | 225 |
| 7.9 | Summary         |              |               |             |               |           |           | 226 |
|     | References      |              |               |             |               |           |           | 227 |

| CONTENTS |              |          |              |                 |              |               |                    | ix  |
| -------- | ------------ | -------- | ------------ | --------------- | ------------ | ------------- | ------------------ | --- |
| 8        | System       |          | relaying     | and             | control      |               |                    | 229 |
| 8.1      | Introduction |          |              |                 |              |               |                    | 229 |
| 8.2      | Measurement  |          |              | of frequency    |              | and phase     |                    | 230 |
|          | 8.2.1        |          | Least        | squares         | estimation   |               | of f and df/dt     | 232 |
| 8.3      | Sampling     |          | clock        | synchronization |              |               |                    | 233 |
| 8.4      | Application  |          | of           | phasor          | measurements |               | to state           |     |
|          | estimation   |          |              |                 |              |               |                    | 234 |
|          | 8.4.1        |          | WLS          | estimator       | involving    |               | angle measurements | 237 |
|          | 8.4.2        |          | Linear       | state           | estimator    |               |                    | 238 |
|          | 8.4.3        |          | Partitioned  |                 | state        | estimation    |                    | 242 |
|          | 8.4.4        |          | PMU          | locations       |              |               |                    | 244 |
| 8.5      | Phasor       |          | measurements |                 | in           | dynamic       | state estimation   | 245 |
|          | 8.5.1        |          | State        | equation        |              |               |                    | 247 |
| 8.6      | Monitoring   |          |              |                 |              |               |                    | 248 |
|          | 8.6.1        |          | Sequence     | of              | events       | analysis      |                    | 248 |
|          | 8.6.2        |          | Incipient    | fault           | detection    |               |                    | 248 |
|          | 8.6.3        |          | Breaker      | health          | monitoring   |               |                    | 249 |
| 8.7      | Control      |          | applications |                 |              |               |                    | 249 |
| 8.8      | Summary      |          |              |                 |              |               |                    | 250 |
|          | Problems     |          |              |                 |              |               |                    | 250 |
|          | References   |          |              |                 |              |               |                    | 251 |
| 9        | Relaying     |          | applications |                 | of           | traveling     | waves              | 255 |
| 9.1      | Introduction |          |              |                 |              |               |                    | 255 |
| 9.2      | Traveling    |          | waves        | on              | single-phase |               | lines              | 255 |
| 9.3      | Traveling    |          | waves        | on              | three-phase  |               | lines              | 262 |
|          | 9.3.1        |          | Traveling    | waves           |              | due to faults |                    | 265 |
| 9.4      | Directional  |          | wave         | relay           |              |               |                    | 267 |
| 9.5      | Traveling    |          | wave         | distance        |              | relay         |                    | 269 |
| 9.6      | Differential |          | relaying     |                 | with         | phasors       |                    | 272 |
| 9.7      | Traveling    |          | wave         | differential    |              | relays        |                    | 275 |
| 9.8      | Fault        | location |              |                 |              |               |                    | 276 |
|          | 9.8.1        |          | Impedance    |                 | estimation   | based         | fault location     | 276 |
|          | 9.8.2        |          | Fault        | location        | based        | on            | traveling waves    | 278 |
| 9.9      | Other        | recent   |              | developments    |              |               |                    | 279 |
| 9.10     | Summary      |          |              |                 |              |               |                    | 280 |
|          | Problems     |          |              |                 |              |               |                    | 280 |
|          | References   |          |              |                 |              |               |                    | 281 |
| 10       | Wide         | area     | measurement  |                 |              | applications  |                    | 285 |
| 10.1     | Introduction |          |              |                 |              |               |                    | 285 |
| 10.2     | Adaptive     |          | relaying     |                 |              |               |                    | 285 |

| x    |          |      |              |               |                 | CONTENTS     |     |
| ---- | -------- | ---- | ------------ | ------------- | --------------- | ------------ | --- |
| 10.3 | Examples |      | of adaptive  |               | relaying        |              | 286 |
|      | 10.3.1   |      | Transmission |               | line protection |              | 287 |
|      | 10.3.2   |      | Transformer  |               | protection      |              | 288 |
|      | 10.3.3   |      | Reclosing    |               |                 |              | 289 |
| 10.4 | Wide     | area | measurement  |               | systems         | (WAMS)       | 291 |
| 10.5 | WAMS     |      | architecture |               |                 |              | 291 |
| 10.6 | WAMS     |      | based        | protection    | concepts        |              | 292 |
|      | 10.6.1   |      | Adaptive     | dependability |                 | and security | 293 |
10.6.2 Monitoring approach of apparent impedances towards relay
|          |                |        | characteristics |               |             |                | 294 |
| -------- | -------------- | ------ | --------------- | ------------- | ----------- | -------------- | --- |
|          | 10.6.3         |        | WAMS            | based         | out-of-step | relaying       | 295 |
|          | 10.6.4         |        | Supervision     |               | of backup   | zones          | 300 |
|          | 10.6.5         |        | Intelligent     | load          | shedding    |                | 301 |
|          | 10.6.6         |        | Adaptive        | loss-of-field |             |                | 302 |
|          | 10.6.7         |        | Intelligent     | islanding     |             |                | 303 |
|          | 10.6.8         |        | System          | wide          | integration | of SIPS        | 304 |
|          | 10.6.9         |        | Load shedding   |               | and         | restoration    | 304 |
| 10.7     | Summary        |        |                 |               |             |                | 305 |
|          | Problems       |        |                 |               |             |                | 306 |
|          | References     |        |                 |               |             |                | 306 |
| Appendix |                | A      |                 |               |             |                | 309 |
|          | Representative |        |                 | system        | data        |                | 309 |
|          | Transmission   |        | lines           |               |             |                | 309 |
|          | Transformers   |        |                 |               |             |                | 311 |
|          | Generators     |        |                 |               |             |                | 311 |
|          | Power          | system |                 |               |             |                | 311 |
|          | References     |        |                 |               |             |                | 312 |
| Appendix |                | B      |                 |               |             |                | 313 |
|          | Standard       |        | sampling        | rates         |             |                | 313 |
|          | References     |        |                 |               |             |                | 315 |
| Appendix |                | C      |                 |               |             |                | 317 |
|          | Conversion     |        | between         |               | different   | sampling rates | 317 |
|          | References     |        |                 |               |             |                | 320 |
| Appendix |                | D      |                 |               |             |                | 321 |
|          | Standard       |        | for transient   |               | data        | exchange       | 321 |
|          | References     |        |                 |               |             |                | 322 |
| Index    |                |        |                 |               |             |                | 323 |

About the authors
Dr. Arun G. Phadke worked in the Electric Utility industry for 13years before
joining Virginia Tech 1982. He became the American Electric Power Professor of
Electrical Engineering in 1985 and held this title until 2000 when he was recog-
nized as a University Distinguished Professor. He became University Distinguished
Professor Emeritus in 2003, and continues as a Research Faculty member of the
Electrical and Computer Engineering Department of Virginia Tech. Dr. Phadke was
elected a Fellow of IEEE in 1980. He was elected to the National Academy of
Engineering in 1993. He was Editor in Chief of Transactions of IEEE on Power
Delivery. He became the Chairman of the Power System Relaying Committee of
IEEE in 1999–2000. Dr. Phadke received the Herman Halperin award of IEEE in
2000. Dr. Phadke has also been very active in CIGRE. He has been a member of
the Executive Committee of the US National Committee of CIGRE, and was the
Chairman of their Technical Committee. He was previously the Vice President of
USNC-CIGRE and served as Secretary/Treasurer. In 2002 he was elected a ‘Dis-
tinguished Member of CIGRE’ by the Governing Board of CIGRE. Dr. Phadke
was active in CIGRE SC34 for several years, and was the Chairman of some
of their working groups. In 1999 Dr. Phadke joined colleagues from Europe and
Far East in founding the International Institute for Critical Infrastructures (CRIS).
He was the first President of CRIS from 1999–2002, and currently serves on its
Governing Board. Dr. Phadke received the ‘Docteur Honoris Causa’ from Insti-
tute National Polytechnic de Grenoble (INPG) in 2006. Dr. Phadke received the
‘Karapetoff Award’ from the HKN Society, and the ‘Benjamin Franklin Medal’ for
Electrical Engineering in 2008.
Dr. James S. Thorp is the Hugh P. and Ethel C. Kelley Professor of Electri-
cal and Computer Engineering and Department Head of the Bradley Department
of Electrical and Computer Engineering at Virginia Tech. He was the Charles N.
Mellowes Professor in Engineering at Cornell University from 1994–2004. He
obtained the B.E.E. in 1959 and the Ph. D. in 1962 from Cornell University and
was the Director of the Cornell School of Electrical and Computer Engineering
from 1994 to 2001, a Faculty Intern, American Electric Power Service Corporation
in 1976–77 and an Overseas Fellow, Churchill College, Cambridge University in
1988.HehasconsultedforMehtaTechInc.,BaslerElectric,RFLDowtyIndustries,

xii About the authors
American Electric Power Service Corporation, and General Electric. He was an
Alfred P. Sloan Foundation National Scholar and was elected a Fellow of the
IEEE in 1989 and a Member of the National Academy of Engineering in 1996. He
received the2001 PowerEngineering Society CareerServiceaward, the 2006 IEEE
Outstanding Power Engineering Educator Award, and shared the 2007 Benjamin
Franklin Medal with A.G. Phadke.

Preface to the first edition
The concept of using digital computers for relaying originated some 25years ago.
Since then the field has grown rapidly. Computers have undergone a significant
change – they have become more powerful, cheaper, and sturdier. Today computer
relays are preferred for economic as well as technical reasons. These advances
in computer hardware have been accompanied by analytical developments in the
field of relaying. Through the participation of researchers at Universities and indus-
trial organizations, the theory of power system protection has been placed on a
mathematical basis. It is noted that, in most cases, the mathematical investiga-
tions have confirmed the fact that traditional relay designs have been optimum or
near-optimum solutions to the relaying problem. This is reassuring: the theory and
practice of relaying have been reaffirmed simultaneously.
An account of these developments is scattered throughout the technical litera-
ture: Proceedings of various conferences, Transactions of Engineering Societies,
and technical publications of various equipment manufacturers. This book is our
attempt to present a coherent account of the field of computer relaying. We have
been doing activeresearchinthisarea – much of itinclosecollaboration witheach
other – since the mid 1970’s. We have tried to present a balanced view of all the
developments in the field, although it may seem that, at times, we have given a
fuller account of areas in which we ourselves have made contributions. For this
bias – if it is perceived as such by the reader – we seek his indulgence.
The book is intended for graduate students in electric power engineering, for
researchers in the field, or for anyone who wishes to understand this new develop-
ment in the role of a potential user or manufacturer of computer relays. In teaching
a course from this book, we recommend following the order of the material in the
book. Ifacourseontraditionalprotectionisapre-requisitetothiscourse,Chapter 2
may be omitted. The mathematical basis for relaying is contained in Chapter 3, and
is intended for those who are not in an academic environment at present. The
material is essential for gaining an understanding of the reason why a relaying
algorithm works as it does, although how an algorithm works – i.e. its procedural
structure – can be understood without a thorough knowledge of the mathematics.
A reader with such a limited objective may skip the mathematical background, and
go directly to the sections of immediate interest to him.

xiv Preface to the first edition
Our long association with the American Electric Power Service Corporation
(AEP) has been the single most important element in sustaining our interest in
Computer Relaying. The atmosphere in the old Computer Applications Department
in AEP under Tony Gabrielle was particularly well suited for innovative engineer-
ing. He was responsible for starting us on this subject, and for giving much needed
support when practical results seemed to be far into the future. Also present at AEP
was Stan Horowitz, our colleague and teacher, without whose help we would have
lost touch with the reality of relaying as a practical engineering enterprise. Stan
Horowitz, Eric Udren, and Peter McLaren read through the manuscript and offered
many constructive comments. We are grateful for their help. The responsibility for
the book, and for any remaining errors, is of course our own.
We continue to derive great pleasure from working in this field. It is our hope
that, with this book, we may share this enjoyment with the reader.
Arun G. Phadke
Blacksburg
James S. Thorp
Ithaca
1988

Preface to the second edition
The first edition of this book was published in 1988. The intervening two decades
have seen wide-spread acceptance of computer relays by power engineers through-
out the world. In fact, in many countries computer relays are the protective devices
of choice, and one would be hard pressed to find electromechanical or electronic
relays with comparable capabilities. Clearly economics of relay manufacture have
played a major role in making this possible, and the improved performance,
self-checking capabilities, and access to relay settings over communication lines
have been the principal features of this technology which have brought about their
acceptance on such a wide scale.
It has been recognized by most relay designers – and is also the belief of the
authors – that the principles of protection have essentially remained as established
by experience gained over the last century. Computer relays provide essentially
the same capabilities as traditional relays in a more efficient manner. Having said
this, it is also recognized that changes in protection principles have taken place,
solelybecauseofthecapabilitiesofthecomputersandtheavailablecommunication
facilities.Thusadaptive relayingcould not berealizedwithout thisnew technology.
Adaptive relaying, along with the new field of wide area measurements (which
originated in the field of computer relaying) forms a significant part of the present
edition of our book.
A study of published research papers on relaying will show that researchers
continue to investigate the application of newer analytical techniques to the field of
relaying.Wehaveincludedanaccountofseveralsuchtechniquesinthisedition,but
itmustbestatedthatmostofthesetechniqueshavenotseentheirimplementationin
practical relay designs. Perhaps this confirms the authors’ belief that the principles
of protection are essentially dictated by power system phenomena, and the long
established techniques of protection system design are very sound and close to
being optimum. The newer analytical techniques which are being investigated offer
very minor improvements at best, and it remains questionable as to when or for
which applications we will see a clear benefit of these newer analytical techniques.
Our book remains a research text and reference work. As such the problem set
at the end of each chapter is often a statement of research idea. Some problems
are quite complex, and each problem leaves room for individual interpretation and

xvi Preface to the second edition
development. We therefore offer no solutions to these problems and leave their
resolution to the individual initiative of the reader. We are of course interested in
receiving any comments that the users of our book care to make.
The authors have participated with pleasure in project “111”, a Key Research
Project of the North China Electric Power University since its inception in 2008
under the direction of Professor Yang Qixun. In addition to promoting research in
many aspects of computer relaying in which the authors continue to participate, the
facilities provided in Beijing under the auspices of this project for the authors have
facilitated the timely completion of this Second Edition of our book.
We continue to derive great pleasure from working in this field. It is our hope
that, with the second edition of this book, we may share this enjoyment with the
reader.
Arun G. Phadke
Blacksburg
James S. Thorp
Blacksburg
2009

| Glossary | of              |               | acronyms         |                |                  |
| -------- | --------------- | ------------- | ---------------- | -------------- | ---------------- |
| A/D      | Analog          | to Digital    |                  |                |                  |
| ADC      | Analog          | to Digital    | Converter        |                |                  |
| ANN      | Artificial      | Neural        | Network          |                |                  |
| ANSI     | American        | National      | Standards        | Institute      |                  |
| CIGRE    | International   |               | Council          | on Large       | Electric Systems |
| CT       | Current         | Transformer   |                  |                |                  |
| CVT      | Capacitive      | Voltage       | Transformer      |                |                  |
| DFT      | Discrete        | Fourier       | Transform        |                |                  |
| EHV      | Extra High      | Voltage       |                  |                |                  |
| EMI      | Electromagnetic |               | Interference     |                |                  |
| EMTP     | Electromagnetic |               | Transients       | Program        |                  |
| EPRI     | Electric        | Power         | Research         | Institute      |                  |
| EPROM    | Erasable        | Programmable  |                  | Read Only      | Memory           |
| FFT      | Fast Fourier    | Transform     |                  |                |                  |
| GPS      | Global          | Positioning   | System           |                |                  |
| I/O      | Input Output    |               |                  |                |                  |
| IEC      | International   |               | Electrotechnical | Commission     |                  |
| IEEE     | Institute       | of Electronic |                  | and Electrical | Engineers        |
| MOV      | Metal Oxide     |               | Varistors        |                |                  |
| MUX      | Multiplexer     |               |                  |                |                  |
NAVSTAR NAVSTAR is not an acronym. It represents GPS described above.
| PDC  | Phasor       | Data Concentrator |        |             |     |
| ---- | ------------ | ----------------- | ------ | ----------- | --- |
| PMU  | Phasor       | Measurement       |        | Unit        |     |
| PROM | Programmable |                   | Read   | Only Memory |     |
| PT   | Potential    | Transformer       |        |             |     |
| RAM  | Random       | Access            | Memory |             |     |
| RAS  | Remedial     | Action            | Scheme |             |     |

| xviii   |                 |                      |                  | Glossary           | of acronyms |
| ------- | --------------- | -------------------- | ---------------- | ------------------ | ----------- |
| ROM     | Read Only       | Memory               |                  |                    |             |
| S/H     | Sample          | and Hold             |                  |                    |             |
| SCDFT   | Symmetrical     | Component            | Discrete Fourier | Transform          |             |
| SIPS    | System          | Integrity Protection | Scheme           |                    |             |
| SWC     | Surge Withstand | Capability           |                  |                    |             |
| WAMS    | Wide Area       | Measurement          | System           |                    |             |
| WAMPACS | Wide Area       | Measurement,         | Protection       | and Control System |             |
| WLS     | Weighted        | Least Squares        |                  |                    |             |

1
Introduction to computer relaying
1.1 Development of computer relaying
The field of computer relaying started with attempts to investigate whether power
systemrelayingfunctionscouldbeperformedwithadigitalcomputer.Theseinvesti-
gations began in the 1960s, a period during which the digital computer was slowly
and systematically replacing many of the traditional tools of analytical electric
power engineering. The short circuit, load flow, and stability problems – whose
solution was the primary preoccupation of power system planners – had already
been converted to computer programs, replacing the DC boards and the Network
Analyzers. Relaying was thought to be the next promising and exciting field for
computerization. It was clear from the outset that digital computers of that period
couldnothandlethetechnicalneedsofhighspeedrelayingfunctions.Norwasthere
any economic incentive to do so. Computers were orders of magnitude too expen-
sive. Yet, the prospect of developing and examining relaying algorithms looked
attractive to several researchers. Through such essentially academic curiosity this
very fertile field was initiated. The evolution of computers over the intervening
years has been so rapid that algorithmic sophistication demanded by the relaying
programs hasfinallyfound acorrespondence inthespeedand economy of themod-
ern microcomputer; so that at present computer relays offer the best economic and
technical solution to the protection problems – in many instances the only work-
able solution. Indeed, we are at the start of an era in which computer relaying has
become routine, and it has further influenced the development of effective tools for
real-time monitoring and control of power systems.
In this chapter we will briefly review the historical developments in the field of
computer relaying. We will then describe the architecture of a typical computer
based relay. We will also identify the critical hardware components, and discuss the
influence they have on the relaying tasks.
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

2 Introduction to computer relaying
1.2 Historical background
One of the earliest published papers on computer relaying explored the somewhat
curious idea that relaying of all the equipment in a substation would be handled
by a single computer.1 No doubt this was motivated by the fact that computers
were very expensive at that time (1960s), and there could be no conceivable way
in which multiple computers would be economically palatable as a substitute for
conventional relays which were at least one order of magnitude less expensive than
a suitable computer. In addition, the computation speed of contemporary computers
was too slow to handle high speed relaying, while the power consumption of the
computers was too high. In spite of these obvious shortcomings – which reflected
thethencurrentstateofcomputerdevelopment – thereferencecitedaboveexplored
several protection algorithmic details thoroughly, and even today provides a good
initiation to the novice in the complexities of modern relaying practices.
Several other papers were published at approximately the same time, and led to
the algorithmic development for protection of high voltage transmission
lines.2,3
It was recognized early that transmission line protection function (distance relay-
ing in particular) – more than any other – is of greatest interest to relay engineers
because of its widespread use on power systems, its relatively high cost, and its
functional complexity. These early researchers began a study of distance protection
algorithms which continues unabated to this day. These studies have led to impor-
tant new insights into the physical nature of protection processes and the limits to
which they can be pushed. It is quite possible that distance relaying implementa-
tion on computers has been mastered by most researchers by now, and that any
new advances in this field are likely to come from the use of improved computer
hardware to implement the well-understood distance relaying algorithms.
An entirely different approach to distance relaying has been proposed during
recent
years.4,5
Itis generally based upon theutilizationof traveling waves initiated
by a fault to estimate the fault distance. Traveling wave relays require relatively
high frequencies for sampling voltage and current input signals. Although traveling
wave relays have not offered compelling advantages over other relaying principles
in terms of speed and accuracy of performance, they have been applied in a few
instances around the world with satisfactory performance. This technique will be
covered more fullyin Chapter 9; it remains for the present a somewhat infrequently
used relaying application. Fault location algorithms based on traveling waves have
also been developed and there are reports of good experience with these devices.
These too will be covered more fully in Chapter 9.
In addition to the development of distance relaying algorithms, work was begun
earlyonapparatusprotectionusingthedifferentialrelayingprinciple.6–8 Theseearly
references recognize the fact that compared to the line relaying task, differential
relaying algorithms are less demanding of computational power. Harmonic restraint
functionaddssomecomplexitytothetransformerprotectionproblem,andproblems
associatedwithcurrenttransformersaturationorotherinaccuraciescontinuetohave

Expected benefits of computer relaying 3
no easy solutions in computer based protection systems just as in conventional
relays. Nevertheless, with the algorithmic development of distance and differential
relayingprinciples,onecouldsaythattheabilityofcomputerbasedrelaystoprovide
performance at least as good as conventional relays had been established by the
early 1970s.
Verysignificant advances in computer hardware had taken placesince those early
days.Thesize,powerconsumption,andcostofcomputershadgonedownbyorders
of magnitude, while simultaneously the speed of computation increased by several
orders. The appearance of 16 bit (and more recently of 32 bit) microprocessors
and computers based upon them made high speed computer relaying technically
achievable, while at the same time cost of computer based relays began to become
comparable to that of conventional relays. This trend has continued to the present
day – and is bound to persist in the future – although perhaps at not quite as pre-
cipitous a rate. In fact, it appears well established by now that the most economical
and technically superior way to build relay systems of the future (except possibly
for some functionally simple and inexpensive relays) is with digital computers. The
old idea of combining several protection functions in one hardware system1 has
also re-emerged to a certain extent – in the present day multi-function relays.
With reasonable prospects of having affordable computer relays which can be
dedicated to a single protection function, attention soon turned to the opportunities
offered by computer relays to integrate them into a substation-wide, perhaps even a
system-wide, network using high-speed wide-band communication networks. Early
papers on this subject realized several benefits that would flow from this ability of
relays to
communicate.9,10
As will be seen in Chapters 8 and 9 integrated com-
puter systems for substations which handle relaying, monitoring, and control tasks
offer novel opportunities for improving overall system performance by exchanging
critical information between different devices.
1.3 Expected benefits of computer relaying
Itwouldbewelltosummarizetheadvantagesofferedbycomputerrelays,andsome
of the features of this technology which have required new operational considera-
tions. Among the benefits flowing from computer relays are:
1.3.1 Cost
All other things being equal, the cost of a relay is the main consideration in its
acceptability. In the early stages of computer relaying, computer relay costs were
10to20timesgreaterthanthecostofconventionalrelays.Overtheyears,thecostof
digital computers has steadily declined; at the same time their computational power
(measured by instruction execution time and word length) has increased substan-
tially. The cost of conventional (analog) relays has steadily increased over the same
period,primarilybecauseofsomedesignimprovements,butalsobecauseofgeneral

4 Introduction to computer relaying
inflation and a relatively low volume of production and sales. It is estimated that
for equal performance the cost of the most sophisticated digital computer relays
(including software costs) would be about the same as that of conventional relay-
ing systems. Clearly there are some conventional relays – overcurrent relays are an
example – which are so inexpensive that cheaper computer relays to replace them
seem unlikely at present, unless they are a part of a multi-function relay. However,
for major protection systems, the competitive computer relay costs have definitely
become an important consideration.
1.3.2 Self-checking and reliability
A computer relay can be programmed to monitor several of its hardware and soft-
ware subsystems continuously, thus detecting any malfunctions that may occur. It
can be designed to fail in a safe mode – i.e. take itself out of service if a failure
is detected – and send a service request alarm to the system center. This feature of
computer relaysisperhaps themost tellingtechnical argument infavor of computer
relaying. Misoperation of relays is not a frequent occurrence, considering the very
large number of relays in existence on a power system. On the other hand, in most
casesofpower systemcatastrophicfailurestheimmediatecauseoftheescalationof
events that leads to the failure can be traced to relay misoperation. In some cases, it
isamis-applicationofarelaytothegivenprotectiontask,butinamajorityofcases
it is due to a failure of a relay component that leads to its misoperation and the
consequent power system breakdown.11 It is expected that with the self-checking
featureof computer based relays, therelay component failurescanbe detected soon
after they occur, and could be repaired before they have a chance to misoperate. In
this sense, although computer based relays are more complex than electromechani-
cal or solid state relays (and hence potentially more likely to fail), as a system they
have a higher rate of availability. Of course, a relay cannot detect all component
failures – especially those outside the periphery of the relay system.
1.3.3 System integration and digital environment
Digital computers and digital technology have become the basis of most systems in
substations. Measurements, communication, telemetry and control are all computer
based functions. Many of the power transducers (current and voltage transformers)
are in the process of becoming digital systems. Fiber optic links, because of their
immunity to Electromagnetic Interference (EMI), are likely to become the medium
of signal transmission from one point to another in a substation; it is a technology
particularly suited to the digital environment. In substations of the future, com-
puter relays will fit in very naturally. They can accept digital signals obtained from
newer transducers and fiber optic channels, and become integrated with the com-
puter based control and monitoring systems of a substation. As a matter of fact,
without computer relaying, the digital transducers and fiber optic links for signal
transmission would not be viable systems in the substation.

Expected benefits of computer relaying 5
1.3.4 Functional flexibility and adaptive relaying
Since the digital computer can be programmed to perform several functions as long
asithastheinputandoutputsignalsneededforthosefunctions,itisasimplematter
to the relay computer to do many other substation tasks. For example, measuring
and monitoring flows and voltages in transformers and transmission lines, control-
ling the opening and closing of circuit breakers and switches, providing backup for
other devices that have failed, are all functions that can be taken over by the relay
computer. The relaying function calls for intensive computational activity when a
fault occurs on the system. This intense activity at best occupies the relaying com-
puter foraverysmallfractionof itsservicelife – lessthanatenthofapercent.The
relaying computer can thus take over these other tasks at practically no extra cost.
With the programmability and communication capability, the computer based
relay offers yet another possible advantage that is not easily realizable in a conven-
tional system. This is the ability to change relay characteristics (settings) as system
conditions warrant it. More will be said about this aspect (adaptive relaying) in
Chapter 10.
The high expectations for computer relaying have been mostly met in practical
implementations. It is clear that most benefits of computer relaying follow from the
ability of computers to communicate with various levels of a control hierarchy.
Thefullfloweringofcomputerrelayingtechnologythereforehasonlybeenpossible
with the arrival of an extensive communication network that reaches into major
substations. Preferably, the medium of communication would be fiber optic links
with their superior immunity to interference, and the ability to handle high-speed
high-volume data. It appears that the benefits of such a communication network
would flow in many fields, and as more such links become available, the computer
relaysandtheirmeasurementcapabilitiesbecomevaluableintheirownright.Where
extensive communication networks are not available, many of the expected benefits
of computer relaying must remain unrealized.
Other issues which are specific to computer relaying technology should also be
mentioned. It has been noted that digital computer technology has advanced at a
very rapid pace over the last twenty years. This implies that computer hardware has
a relatively short lifespan. The hardware changes significantly every few years, and
thequestionofmaintainabilityofoldhardwarebecomes crucial.Theexistingrelays
have performed well for long periods – some as long as 30 years or more. Such
relays have been maintained over this period. It is difficult to envision a similar
lifespan for computer based equipment. Perhaps a solution lies in the modularity
of computer hardware; computers and peripherals belonging to a single family may
provide a longer service life with replacements of a few modules every few years.
As long as this can be accomplished without extensive changes to the relaying
system, this may be an acceptable compromise for long service life. However,
the implications of rapidly changing computer hardware systems are evident to
manufacturers and users of this technology.

6 Introduction to computer relaying
Software presents problems of its own. Computer programs for relaying applica-
tions (or critical parts of them) are usually written in lower level languages, such
as assembly language. The reason for this is the need to utilize the available time
after the occurrence of a fault as efficiently as possible. Relaying programs tend
to be computation and input-output bound. The higher level languages tend to be
inefficient for time-sensitive applications. It is possible that in time, with computer
instruction times becoming faster, the higher level languages could replace much
of the assembly language programming in relaying computers. The problem with
machinelevellanguagesisthattheyarenottransportablebetweencomputersofdif-
ferent types. Some transportability between different computer models of the same
family may exist, but even here it is generally desirable to develop new software
in order to take advantage of differing capabilities among the different models.
Since software costs are a very significant part of computer relaying development,
non-transferability of software is a significant problem.
In the early period of computer relaying development, there was some concern
about the harsh environment of electric utility substations, in which the relays must
function. Extremes of temperature, humidity, pollution as well as very severe EMI
must be anticipated.
Another concern often raised by users of computer relays can be traced to the
wide range of problems these relays can handle. It is rare to find a computer relay
which does not require very large number of settings before it can be installed and
commissioned. Where the organization using these devices has ample staff dedi-
cated to working with computer relays, handling the complexity of setting these
relays is not a problem. However, where the organization is small and a specialized
staff for these applications cannot be justified, setting of these relays correctly and
maintaining them for future modifications becomes a difficult task. Furthermore,
if relays of different manufacture are in use within a single organization, it may
become necessary to have experts who can deal with devices of different manufac-
ture. Several Working Groups and Technical Committees of the Power Engineering
Society of IEEE have attempted to develop a common user-interface to relays of
different manufacture, but thistask seems tobe too complex and not much progress
has been made in this direction.
1.4 Computer relay architecture
Computer relays consist of subsystems with well defined functions. Although a
specific relay may be different in some of its details, these subsystems are most
likely to be incorporated in its design in some form. Relay subsystems and their
functions will be described next.
The block diagram in Figure 1.1 shows the principal subsystems of a com-
puter relay. The processor is central to its organization. It is responsible for the
execution of relay programs, maintenance of various timing functions, and com-
municating with its peripheral equipment. Several types of memories are shown in

| Computer | relay architecture |              |               |     | 7   |
| -------- | ------------------ | ------------ | ------------- | --- | --- |
|          | FROM               | SUBSTATION   | SWITCH YARD   |     |     |
|          | Currents and       | Contact      | Contact       |     |     |
|          | Voltages           | Inputs (D/I) | Outputs (D/O) |     |     |
(Communications)
|     | Surge   | Surge   | Signal       |     |     |
| --- | ------- | ------- | ------------ | --- | --- |
|     | Filters | Filters | Conditioning |     |     |
Serial
|     | Signal | Signal |     | Port |     |
| --- | ------ | ------ | --- | ---- | --- |
Digital
|     | Conditioning | Conditioning | Output |     |     |
| --- | ------------ | ------------ | ------ | --- | --- |
Sampling
|     | A/D |       | Parallel |     |     |
| --- | --- | ----- | -------- | --- | --- |
|     |     | Clock | Port     |     |     |
Sample/Hold
Processor
Power
Supply
|     |     | ROM/ |       | Mass   |     |
| --- | --- | ---- | ----- | ------ | --- |
|     | RAM |      | EPROM |        |     |
|     |     | PROM |       | Memory |     |
Figure 1.1 Subsystems of a relaying computer. The dashed line at the top indicates the
boundary of the out-door switch yard. All other equipment is inside the control house
Figure 1.1 – each of them serves a specific need. The Random Access Memory
(RAM) holds the input sample data as they are brought in and processed. It may
also be used to buffer data for later storage in a more permanent medium. In addi-
tion, RAM is needed as a scratch pad to be used during relay algorithm execution.
The Read Only Memory (ROM) or Programmable Read Only Memory (PROM) is
used to store the programs permanently. In some cases the programs may execute
directly from the ROM, if its read time is short enough. If this is not the case, the
programsmustbecopiedfromtheROMintotheRAMduringaninitializationstage,
and then the real-time execution would take place from the RAM. The Erasable
PROM (EPROM) is needed for storing certain parameters (such as the relay set-
tings) which may be changed from time to time, but once set must remain fixed,
even if the power supply to the computer is interrupted. Either a core type memory
or an on-board battery backed RAM may be suitable for this function.
A large capacity EPROM is likely to become a desirable feature of a computer
relay. Such a memory would be useful as an archival data storage medium, for
storing fault related data tables, time-tagged event logs, and audit trails of interro-
gations and setting changes made in the relay. The main consideration here is the
cost of such a memory. The memory costs have dropped sufficiently by now so
that archival storage of oscillography and sequence-of-event data on a large scale
| within the | relays has become | possible. |     |     |     |
| ---------- | ----------------- | --------- | --- | --- | --- |
Consider the analog input system next. At the outset it should be pointed out
that Figure 1.1 is based upon using conventional transducers. If electronic CTs and
CVTs are used, the input circuits may be significantly different and data are likely
to be entered directly in the processor memory. The relay inputs are currents and
voltages and digital signals indicating contact status. The analog signals must be

8 Introduction to computer relaying
converted to voltage signals suitable for conversion to digital form. This is done by
the Analog to Digital Converter (ADC). Usually the input to an ADC is restricted
to a full scale value of ±10 volts. The current and voltage signals obtained from
currentandvoltagetransformersecondarywindingsmustbescaledaccordingly.The
largest possible signal levels must be anticipated, and the relation between the rms
(root mean square) value of the signal and its peak must be reckoned with. It is not
necessarytoallowforhighfrequencytransientsinmostcases,astheseareremoved
by anti-aliasing filters which have a low cut-off frequency. An exception to this is
a wave relay, which does use the high frequency (traveling wave) components.
For such relays (to be discussed more fully in Chapter 9), the scaling of signals
must be such that the entire input signal with its largest anticipated high frequency
component must not exceed the ADC input range.
The current inputs must be converted to voltages – for example by resistive
shunts. As the normal current transformer secondary currents may be as high as
hundreds of amperes,shunts ofresistanceof afewmilliohmsareneeded toproduce
the desired voltage for the ADCs. An alternative arrangement would be to use an
auxiliary current transformer to reduce the current to a lower level. However, any
inaccuracies in the auxiliary current transformer would contribute to the total error
oftheconversionprocess, andmustbekeptaslowaspossible. Anauxiliarycurrent
transformer serves another function: that of providing electrical isolation between
themainCTsecondaryandthecomputerinputsystem.Inthiscase,theshuntmaybe
grounded at its midpoint in order to provide a balanced input to following amplifier
and filter stages. These considerations are illustrated in Figure 1.2(a) and (b).
Figure 1.2(c) shows connections to the voltage transformer. A fused circuit is
provided for each instrument or relay, and a similar circuit may be provided for the
computerrelayaswell.Thenormalvoltageatthesecondaryofavoltagetransformer
is 67volts rms for a phase to neutral connection. It can be reduced to the desired
level by a resistive potential divider sized to provide adequate source impedance to
drive the following stages of filters and amplifiers.
Although an auxiliary voltage transformer may be used in this case to provide
additional isolation, it is not a necessity. Digital inputs to the computer relay are
usually contact status, obtained from other relays or subsystems from within the
substation. If the other subsystems are computer based, then these signals can be
input to the computer relay without any special processing. An exception to this
may be an opto-isolation circuit provided to maintain isolation between the two
systems. When the digital inputs are derived from contacts within the yard (or
control house), it is necessary to apply surge filtering and (or) optical isolation in
order to isolate the computer relay from the harsh substation environment. Surge
suppression for analog and digital signals is discussed next.
Suppression of surges from wiring connected to any protection system is a spe-
cialized subject with considerable literature of its
own.12,13
High voltage and high
energy content surges are coupled into the wiring which connects current, volt-
age, and digital inputs to the protection system. The surges are created by faults

Computer relay architecture 9
To Other
Relays &
To Other
Meters
Relays &
Meters
Main Main
CT CT To
To Computer
Computer
Relay
Relay
Aux
CT
(a) (b)
Fuses
To Other
Relays &
Meters
To
Computer
Relay
(c)
Figure 1.2 Scaling of current and voltage signals for input to the relay. (a) Direct con-
nection in the main CT secondary. (b) Use of auxiliary CT. (c) Voltage transformer and
potential divider
and switching operations on the power system, or by certain types of switching
operations within the control house. For example, sparking contacts in inductive
protection and control circuits within the control house have been found to be a
source of very significant disturbances.14 (See Chapter 7 for additional details).
Suppression of these surges requires very careful grounding and shielding of leads
and equipment, as well as low-pass filtering. Nonlinear energy absorbing Metal
Oxide Varistors (MOVs) may also be used. Surge suppression filters are necessary
for input and output wiring, as well as for the power supply leads.12
The ADC and anti-aliasing filter associated with the sampling process will be
considered in greater detail in Sections 1.5 and 1.6. At this stage it is sufficient
to be aware of their function in the overall relaying process. The anti-aliasing
filters are low-pass analog filters designed to suit a specific choice of sampling
rate used. The sampling instants are determined by the sampling clock, which must
produce pulses at a fixed rate. The relationship between the sampling clock and
several of the measurement functions performed by a computer relay is discussed
in Chapters 9 and 10. For the present, it is sufficient to understand that, at each
instant definedbytheclock,aconversion fromtheinstantaneous valueofananalog
input signal (voltage or current) to a digital form is performed by the ADC, and
made available to the processor. Since the relay in general requires several inputs,
several conversionsareperformedat eachsamplinginstant.Itisdesirable(although
not essential) that all signal samples be simultaneous, which means that either the
conversion and transmission to the processor of each sample be very fast, or all
the signals be sampled and held at the same instant for processing by a relatively

| 10     |     |     |        | Introduction | to computer | relaying |
| ------ | --- | --- | ------ | ------------ | ----------- | -------- |
| Analog |     |     | Analog |              |             |          |
S/H
| Inputs |     | A/D | Inputs |     |     |     |
| ------ | --- | --- | ------ | --- | --- | --- |
A/D
| •   |     |     |     | S/H |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     | MUX |     |     | •   | MUX |     |
| •   |     |     |     | •   |     |     |
•
|     |     | Sampling |     | •   |     |     |
| --- | --- | -------- | --- | --- | --- | --- |
|     |     | Clock    |     | S/H |     |     |
Sampling
Clock
|     | (a) |     |     | (b) |     |     |
| --- | --- | --- | --- | --- | --- | --- |
A/D
Analog
Inputs
A/D
• Buffer
•
•
A/D
Sampling
Clock
(c)
Figure 1.3 Multiple signal sampling process and its organization. (a) Single ADC with
multiplexed input. (b) Sample and hold added to each channel. (c) Separate ADC for each
channel
slowconversion-transmissioncycleforeachsample.Thisistypicalofamultiplexed
analog input system. A third option, technically feasible but expensive. is to use
individual ADCs for each input channel. Trends in the ADC development and their
reduced costs seem to point to the use of individual ADCs for each signal to be the
preferred system. These options are illustrated in Figure 1.3.
It is well to consider this need for simultaneity in a little more detail at this point.
Most relay functions require simultaneous measurement of two or more phasor
quantities.
Aswillbe seenin Chapters3and 8, thereference for thesephasors isdetermined
by theinstant at which asample isobtained. Thus ifthe phasors for signals x(t) and
y(t) are computed from their samples beginning at instants t x and t y , the references
for the two phasors will differ from each other by an angle θ, where
2π
|     |     | θ = (t | −t ) radians |     |     |     |
| --- | --- | ------ | ------------ | --- | --- | --- |
|     |     | x      | y            |     |     |     |
T
whereTisthefundamentalfrequencyperiodofthesignal.Ifthedifferencebetween
t x and t y is known, then the phase angle between the two references is also known,
and the two phasors could always be put on a common reference by compensating
for θ. It would thus appear that simultaneous sampling of various input signals is

Computer relay architecture 11
not necessary, as long as thedifference between the twoisknown and compensated
for. On the other hand, all computations become much simpler if θ is zero and no
compensationisneeded.Furthermore,whenneeded,thesamplesofdifferentsignals
could be combined directly (as in the case of a differential relaying application,
where all input current samples of different signals could be added directly to form
samples of the differentialcurrent). Tobe ableto combine the samples directly, it is
essential that the samples be taken simultaneously – and this fact, plus the relative
ease of achieving it, has led to the general practice of simultaneous sampling of all
input signals by each relaying computer. Indeed, there are benefits to be gained by
coherently sampling all the quantities within a station as well as at all the stations
within the system. System-wide synchronization will be considered in Chapters 8,
9 and 10.
Consider the sampling scheme shown in Figure 1.3(a). In the absence of sample-
and-hold circuits, the different signal samples are obtained sequentially, and are
not truly simultaneous. One period of a 60Hz wave is 16.67 milliseconds. This
corresponds to about 21.6 degrees per millisecond. Thus if the entire sampling scan
can be completed in about 10 microseconds, the worst error created by sequential
samplingamountstoabout0.2degree – anegligibleamountoferrorinanyrelaying
application. Indeed, total scan periods of about 50 microseconds could be tolerated.
In fact, a tolerance of 10–50 microseconds provides a good measure for describing
any data samples as being simultaneous.
It should be mentioned that if simultaneous sampling is not possible, and yet it
is needed for a relaying application, one could generate approximate simultaneous
samplesfromnon-simultaneous samples. Supposethat samplesx = {x , x ,...x }
k 1 2 n
are obtained at instants t = {t , t ,...t }, whereas samples at t(cid:1) = t +(cid:1)T are
k 1 2 n k k
needed. If x(t) is assumed to be suitably band-limited, x(cid:1) can be generated by
k
interpolationformulas.Thesimplestprocedurewouldbetouselinearinterpolation:
(cid:1)T
x(cid:1) = x +(x −x )
k k k+1 k t −t
k+1 k
where k = 1,2,...n−1 as shown in Figure 1.4. Higher order polynomials or
spline functions may be used to obtain x(cid:1) from x . Details may be found in any
k k
textbook on numerical methods.15 It should be remembered that, in the context
of relaying applications, any but the simplest linear interpolation formula would
require excessively long real-time computation.
Returning once again to Figure 1.1, digital output from the processor is used to
provide relay output in the form of open or close contacts. A parallel output port of
the processor provides one word (typically two bytes) for these outputs. Each bit
can be used as a source for one contact. The computer output bit is a Transistor to
Transistor Logic (TTL) level signal, and would be optically isolated before driving
a high speed multi-contact relay, or thyristors, which in turn can be used to activate
external devices such as alarms, breaker trip coils, carrier control etc.

12 Introduction to computer relaying
x(t)
∆T
t 1 t′ 1 t 2 t′ 2 t 3 t
Figure 1.4 Interpolation for obtaining synchronous samples. Samples shown with x’s are
to be determined from samples actually obtained, which are shown by o’s
Finally, the power supply is usually a single DC input multiple DC output con-
verter powered by the station battery. The input is generally 125volts DC, and
the output could be 5volts DC and ±15volts DC. Typically the 5 volt supply is
needed topower thelogiccircuits,whilethe15volt supplyisneeded fortheanalog
circuits. The station battery is of course continuously charged from the station AC
service.
1.5 Analog to digital converters
The Analog to Digital Converter (ADC) converts an analog voltage level to its
digital representation. The principal feature of an ADC is its word length expressed
in bits. Ultimately this affects the ability of the ADC to represent the analog sig-
nal with a sufficiently detailed digital representation. Consider an ADC with 12
bit word length – which, along with the 16 bit converter – is the most common
word length in commercially available ADCs of today. Using a two’s complement
notation, the binary number 0111 1111 1111 (7FF in hexadecimal notation) repre-
sents the largest positive number that can be represented by a 12 bit ADC, while
1000 0000 0000 (800 in hexadecimal notation) represents the smallest (negative)
number. In decimal notation, hexadecimal 7FF is equal to (211−1) = 2047, and
hexadecimal 800 is equal to −211 = −2048. Considering that the analog input sig-
nal may range between ±10volts, it is clear that each bit of the 12 bit ADC word
represents 10/2048volts, or 4.883 millivolts. Table 1.1 shows input voltages and
their corresponding converted values in two’s complement and decimal equivalent
for 12 and 16 bit ADCs.
Theequivalentinputchangeforonedigitchangeintheoutput(4.883millivoltsin
case of a 12 bit A/D converter) is an important parameter of the ADC. It describes
the uncertainty in the input signal for a given digital output. Thus an output of
hexadecimal 001 represents any input voltage between 2.442 and 7.352 millivolts.
ThisisthequantizationerroroftheADC.Ingeneral,ifthewordlengthoftheADC

| Analog to digital | converters |     |     | 13  |
| ----------------- | ---------- | --- | --- | --- |
Table 1.1 Two’s complement 12 bit and 16 bit ADC input-outputs. maximum input
| voltage is assumed | to be 10volts |         |             |         |
| ------------------ | ------------- | ------- | ----------- | ------- |
|                    | 12 bit ADC    |         | 16 bit ADC  |         |
| Input Volts        | Hexadecimal   | Decimal | Hexadecimal | Decimal |
| 9.995              | 7FF           | 2047    | 7FFF        | 32767   |
| 5.0                | 400           | 1024    | 4000        | 16384   |
| 3.0                | 266           | 614     | 2666        | 9830    |
| 2.0                | 198           | 408     | 1999        | 6553    |
| 0.0                | 000           | 0       | 0000        | 0       |
| −1.0               | F33           | −205    | FCCB        | −3277   |
| −5.0               | C00           | −1024   | BFFF        | −16384  |
| −10.0              |               | −2048   |             | −32768  |
|                    | 800           |         | 8000        |         |
is N bits, and the maximum input voltage for the ADC is V volts, the quantization
| error q is given | by  |     |     |     |
| ---------------- | --- | --- | --- | --- |
V
q = = 2−NV
2×2N−1
and normalized to the largest possible input voltage of V, the per unit quantization
error is
per unit q = 2−N
clearly, the larger the number of bits in a converter word, the smaller is the quan-
tization error.
Besides the quantization error, the ADC is prone to other errors as well. In order
to understand the source of these errors, it is helpful to examine the principle of
| operation of     | an ADC.       |     |     |     |
| ---------------- | ------------- | --- | --- | --- |
| 1.5.1 Successive | approximation | ADC |     |     |
Acommontypeofanalog-to-digitalconverteristhesuccessiveapproximationADC.
Detailed information about this type of ADC and its design can be found in the
literature.16
The analog signal is amplified through an adjustable gain amplifier,
as shown in Figure 1.5. A Digital to Analog Converter (DAC) converts the digital
numberintheoutputregisteroftheADCtoananalogvalue.Thissignaliscompared
with the input analog signal, and the difference is used to drive up the count in the
ADCoutputregister.WhentheoutputoftheDACiswithinthequantizationrangeof
theanaloginput,theoutputisstable,andistheconvertedvalueoftheanalogsignal.
The amplifier is a source of additional error in the ADC. It may have a DC offset
error as well as a gain error. In addition, the gain may have nonlinearity as well.
The combined effect of all ADC errors is illustrated in Figure 1.6. The offset
error produces a shift in the input-output characteristic, whereas the gain error

14 Introduction to computer relaying
Analog
Inputs
Comparator
Variable Gain Count
Amplifier Up/Down
Circuit
ADC Output
DAC
Register
Output
Figure 1.5 Successive approximation ADC. When the output of the comparator is posi-
tive, the ADC output register is incremented; when negative, it is decremented. When the
comparator output is less than the quantization error, the output is declared valid
Gain
error
Quantization error
Input
tuptuO
Offset
error
Figure 1.6 The effect of gain error, gain nonlinearity, and quantization on total error of
the ADC
produces a change in the slope. The nonlinearity produces a band of uncertainty in
theinput-outputrelationship.Ifthegainerrorandthenonlinearityerrorarebounded
by two straight lines as shown in Figure 1.6, the total error in the ADC for a given
voltage input V is given by ε :
v
ε = K ×FS+K ×V
v 1 2
where FS is the full scale value of the input voltage, and K and K are constants
1 2
depending upon the actual uncertainties of the conversion process.
Itispossibleforthegainsettingtobechangedbetweensamples,althoughatsam-
pling rates corresponding to relaying applications (of the order of 1kHz), dynamic
gain changing would be too time consuming. Consequently, the error model given
above is fairly representative of the ADCs used in relaying applications. It should

| Analog to | digital converters |     |     |     |     | 15  |
| --------- | ------------------ | --- | --- | --- | --- | --- |
alsobeclearthat,whentheinputsignalisasmallfractionofthefullscalevalue,the
first error term is dominant and the error at every sample is likely to be of the same
size. On the other hand, when the input signals approach the full scale, the sec-
ond term may dominate and each sample error may be proportional to its nominal
value.
Thequantizationerrorcomponentofthetotalerrorisarandomprocess,whilethe
remainingerrorcomponentsaredeterministicerrorsdependinguponthegain,offset
and non-linearity errors present at a given moment. If we consider the ensemble of
all operating conditions under which the relay must operate, this too may be treated
as a random process. The error model given for ε above should then be understood
v
to represent the standard deviation σ of the random measurement noise. Such error
v
| models | will be considered |     | in Chapter | 3.  |     |     |
| ------ | ------------------ | --- | ---------- | --- | --- | --- |
| 1.5.2  | Delta-sigma        | ADC |            |     |     |     |
The Delta-Sigma analog-to-digital converter has become the ADC of choice in
recent years.17 These converters use a 1 bit analog to digital converter, thus making
the analog signal processing simple and inexpensive. A very high sampling rate is
used(over-sampling)andthedigitalsignalprocessingisusedtoprovideappropriate
anti-aliasing filters and decimation filters. The digital circuitry in these ADCs are
| more complex, | but | are relatively | inexpensive |     | to manufacture. |     |
| ------------- | --- | -------------- | ----------- | --- | --------------- | --- |
The block diagram of a generic delta-sigma ADC is shown in Figure 1.7(a). The
signal x is obtained by subtracting from the input signal x the output of the 1 bit
1
ADC (y) converted to analog form by the 1 bit Digital-to-Analog Converter. The
y
|     | x   | x 1 | x 2 |     | Digital |     |
| --- | --- | --- | --- | --- | ------- | --- |
Decimation
|     |     | Integrator |     | 1-bit ADC | low-pass |     |
| --- | --- | ---------- | --- | --------- | -------- | --- |
+ Filter
|     |     | −   |     |     | filter |     |
| --- | --- | --- | --- | --- | ------ | --- |
DAC
(a)
Signal of interest
Anti-aliasing
|     |     |     |     | filter cut-off | Shaped noise |     |
| --- | --- | --- | --- | -------------- | ------------ | --- |
edutilpmA
Noise
with over-
sampling
Frequency
(b)
Figure1.7 (a)Blockdiagramofadelta-sigmaanalog-to-digitalconverter.(b)Noisereduc-
| tion in ADC | output | by shaping | the filter | characteristic |     |     |
| ----------- | ------ | ---------- | ---------- | -------------- | --- | --- |

16 Introduction to computer relaying
signal x is integrated to produce the signal x which is fed to the 1 bit ADC.
1 2
The feed-back circuit ensures that the average of the analog input is equal to that
of the converted signal. The output of the 1 bit ADC is a 1 bit data stream clocked
at high frequency (over-sampling). A digital low-pass filter converts the 1 bit data
stream to a multi-bit data stream, which is finally filtered by a decimation filter to
achieve the sampling rate of interest in relaying applications. For example, with an
over-sampling frequency of 40kHz, a decimation filter output at 2kHz could be
obtainedwitha16bitresolution. Theover-samplingreducestheamount of noisein
the frequency band of interest, as it spreads the signal noise equally throughout the
bandwidth corresponding to the over-sampling rate. A further reduction in noise in
the output is achieved by shaping the digital filter characteristic so that the noise is
concentrated at the high end of the spectrum, which in turn is eliminated by the
anti-aliasing filter (Figure 1.7(b)).
1.6 Anti-aliasing filters
Theneedforanti-aliasingfilterswillbeestablishedinChapter3.Forthepresent,we
will accept that these are low-pass filters with a cut-off frequency equal to one-half
thesamplingrateusedbytheADC.Anidealanti-aliasingfiltercharacteristicwitha
cut-off frequency f is shown in Figure 1.8. A practical filter can only approximate
c
this ‘brick-wall’ shape, as shown by the dotted line in Figure 1.8. Next, we will
consider design aspects of practical anti-aliasing filters.
Anti-aliasing filters could be passive, consisting of resistors and capacitors exclu-
sively; or active, utilizing operational amplifiers. As some buffering between the
filtersandtheADCisgenerallynecessary,anoperational amplifierisneededinany
case, and one could use the active filter design which leads to smaller component
sizes. An active filter may also be designed using the monolithic hybrid microelec-
tronic technology providing compact packaging. The transfer function for the filter
in any case is determined from considerations of sharpness of cut-off in the stop
band, and the transient response of the filter.
niaG
f c Frequency
Figure1.8 Idealanti-aliasingfiltercharacteristicforacut-offfrequencyoff .Approximate
c
realizable characteristic shown by the dotted line

Anti-aliasing filters 17
In general, if filters with very sharp cut-off are employed, they produce longer
time delays in their step function response.18 In most applications of computer
relaying, two-stage RC filters are found to provide an acceptable compromise
between sharpness of the cut-off characteristic in the stop band, and the time delay
in their step input response. A second order Butterworth, Chebyshev, or maximally
flat (Bessel) filter may be used to satisfy computer relaying requirements. How-
ever, these filters have a significant overshoot in their step input response. As an
example, we will consider the design of a two-stage RC filter suitable for a sam-
pling process using a sampling rate of 720Hz (12 times the fundamental frequency
for a 60Hz power system). The filter must have a cut-off frequency of 360Hz. We
may further specify a DC gain of unity – which makes either an active or a passive
design possible. An active filter can of course be designed to provide any other
reasonable gain.
Two-stage RC filters are quite popular because of their simplicity, passive com-
ponents, and a reasonable frequency response. They suffer from the disadvantage
that they produce a rounded characteristic at the beginning of the stop band. A
two-stage RC filter achieves a 12db per octave attenuation rate when it is well into
its stop band. Indeed, this is a property of an all-pole second order filter.18 The
transfer function of a two-stage RC filter is given by:
1
H(jω) =
1+jω(R C +R C +R C )−ω2(R C R C )
1 1 2 2 1 2 1 1 2 2
R , C , R , C being the components of two stages. These components must be
1 1 2 2
adjusted to provide the necessary attenuation at a desired cut-off frequency f .
c
Figure 1.9(a) shows a two-stage RC circuit with this transfer function and a cut-off
frequency of 360Hz. The frequency response and step wave response of this filter
are shown in Figures 1.9(b) and (c). As can be seen, the step wave response is
reasonable, producing an essentially correct output in about 0.8 millisecond after
application of the step wave. The phase lag at the fundamental power frequency
(60Hz) is about 11 degrees, which corresponds to a time delay of about 0.7 mil-
lisecond. Considering that this filter has been designed for a sampling frequency of
720Hz,thephasedelayproducedbyitisaboutone-halfthesamplingperiod.Recall
that the sampling period at a sampling frequency of 720Hz is 1.388 milliseconds.
SecondorderChebyshevfiltersproduceasomewhatsteeperinitialcut-offintheir
stop band. However, this is at the expense of a ripple in the pass band. The step
wave response of Butterworth and Chebyshev filters is somewhat poorer, having
a significant overshoot. A comparison of the frequency response and step wave
response of these three second order filters with a cut-off frequency of 360Hz
is shown in Figure 1.10. Figure 1.11 shows an active realization of the two-pole
Butterworth filter of Figure 1.9. Note that there are no inductors in this realization
whereas a passive Butterworth filter must use inductances. This may well be one
of the considerations in the final choice of active or passive filter design.

| 18  |         |         | Introduction | to computer | relaying |
| --- | ------- | ------- | ------------ | ----------- | -------- |
|     | 1.26 KΩ | 2.52 KΩ |              |             |          |
|     | 0.1µF   | 0.1 µF  |              |             |          |
1.0
niaG
|        |     | (a) | 0.7 |     |     |
| ------ | --- | --- | --- | --- | --- |
| tuptuO |     |     | 360 | 720 |     |
1.0
Frequency (Hz)
(b)
|     | 1 2 | 3 4 |     |     |     |
| --- | --- | --- | --- | --- | --- |
Time (msec)
(c)
Figure 1.9 Two-stage RC filter with a cut-off frequency of 360Hz. (a) RC ladder realiza-
| tion. (b) Frequency | response. | (c) Step wave input | response |     |     |
| ------------------- | --------- | ------------------- | -------- | --- | --- |
Chebyshev
Butterworth
|     | 1.0 |     | 1.0 |     |     |
| --- | --- | --- | --- | --- | --- |
RC
RC
Butterworth
Chebyshev
|     |                | 360 720 | 1           | 2   |     |
| --- | -------------- | ------- | ----------- | --- | --- |
|     | Frequency (Hz) |         | Time (msec) |     |     |
|     |                | (a)     | (b)         |     |     |
Figure 1.10 Comparison of second order RC, Butterworth, and Chebyshev filters with a
cut-off frequency of 360Hz. (a) Frequency response. (b) Step wave response
Another consideration in selecting a filter design is the stability of its transfer
function in the presence of variation in component values due to aging and tem-
perature variations. Consider the passive two-stage RC filter of Figure 1.9. Its gain
H(ω):
and phase shift are obtained by taking the magnitude and phase angle of
G(ω)≡|H(ω)|
(cid:1)
1
=
|     | {1−ω2(R | C R C )}2+ω2(R | C +R | C +R C )}2 |     |
| --- | ------- | -------------- | ---- | ---------- | --- |
|     |         | 1 1 2 2        | 1 1  | 2 2 1 2    |     |
φ(ω)≡∠H(ω)
|     |     | (cid:2)    | (cid:3) |     |     |
| --- | --- | ---------- | ------- | --- | --- |
|     |     | ω(R C +R C | +R C )  |     |     |
|     |     | 1 1 2      | 2 1 2   |     |     |
=−arctan
|     |     | 1−ω2(R C | R C ) |     |     |
| --- | --- | -------- | ----- | --- | --- |
1 1 2 2

| Substation | computer | hierarchy |     |     |     |     |     |     |     |     | 19  |
| ---------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
_
+
Figure 1.11 Active circuit realization of a two-pole Butterworth filter with a cut-off fre-
| quency | of 360Hz |     |     |     |     |     |     |     |     |     |     |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
If we consider that all four components used in the passive circuit may vary by
small amounts, the variations in the gain and phase shift are given by
|     |             |     | ∂G  |          | ∂G  |            | ∂G  |            | ∂G       |     |     |
| --- | ----------- | --- | --- | -------- | --- | ---------- | --- | ---------- | -------- | --- | --- |
|     | (cid:1)G(ω) |     | =   | (cid:1)R | +   | (cid:1)R + |     | (cid:1)C + | (cid:1)C |     |     |
|     |             |     | ∂R  | 1        | ∂R  | 2          | ∂C  | 1          | ∂C       | 2   |     |
|     |             |     | 1   |          | 2   |            | 1   |            | 2        |     |     |
|     |             |     | ∂φ  |          | ∂φ  |            | ∂φ  |            | ∂φ       |     |     |
|     | (cid:1)φ(ω) |     | =   | (cid:1)R | +   | (cid:1)R + |     | (cid:1)C + | (cid:1)C |     |     |
|     |             |     |     | 1        |     | 2          |     | 1          |          | 2   |     |
|     |             |     | ∂R  |          | ∂R  |            | ∂C  |            | ∂C       |     |     |
|     |             |     | 1   |          | 2   |            | 1   |            | 2        |     |     |
Taking the partial derivatives at the selected nominal values of R , R , C and C
|           |          |        |          |          |     |          |     |          |     | 1 2 1    | 2   |
| --------- | -------- | ------ | -------- | -------- | --- | -------- | --- | -------- | --- | -------- | --- |
| in Figure | 1.9,     | we get |          |          |     |          |     |          |     |          |     |
|           | (cid:1)G |        | (cid:1)R |          |     | (cid:1)R |     | (cid:1)C |     | (cid:1)C |     |
|           |          | −0.013 |          | 1 −0.013 |     | 2 −0.004 |     | 1 −0.022 |     | 2        |     |
=
|     | G        |         | R        |        |          | R      |          | C      |          | C   |     |
| --- | -------- | ------- | -------- | ------ | -------- | ------ | -------- | ------ | -------- | --- | --- |
|     |          |         |          | 1      |          | 2      |          | 1      |          | 2   |     |
|     | (cid:1)φ |         | (cid:1)R |        | (cid:1)R |        | (cid:1)C |        | (cid:1)C |     |     |
|     |          |         |          | 1      |          | 2      |          | 1      |          | 2   |     |
|     |          | = 0.493 |          | +0.493 |          | +0.242 |          | +0.734 |          |     |     |
φ
|     |     |     | R 1 |     | R   | 2   | C   | 1   |     | C 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Often it is the relative deviation in the phase angle (cid:1)φ/φ at 60Hz due to changes
in resistor and capacitor values which is of greatest concern, since this is greater
in magnitude than the relative deviation in gain (cid:1)G/G. As can be seen from
Problem 1.3, the gain magnitude and phase angle of an active filter are more sen-
sitive to variations in component values as compared to those of a passive filter.
Component variations can be kept small by selecting high precision metal film
| resistors      | and polystyrene |     | or       | polycarbonate |           | capacitors. |     |     |     |     |     |
| -------------- | --------------- | --- | -------- | ------------- | --------- | ----------- | --- | --- | --- | --- | --- |
| 1.7 Substation |                 |     | computer |               | hierarchy |             |     |     |     |     |     |
Let us consider the hierarchy of various relaying and other computers in a substa-
tion. Computer relays are expected to be a part of a system wide protection and
hierarchy.19,20
control computer Functionally the hierarchy structures that are being
planned for implementation may be represented as in Figure 1.12. Relay comput-
ers and their input-output systems are at the lowest level of this hierarchy, and

20 Introduction to computer relaying
Central
Level III Computer
Substation
Level II Host
Relay
Computer
Level I
Input
Output
Figure1.12 Systemwidehierarchicalcomputersystem.Computerrelaysareatthelowest
levelofthehierarchy.Theyarelinkedwithsubstationhostcomputerwhichinturnislinked
with a system center computer
communicate with the switch yard through the relay input and output signals. As
the relay outputs are connected to circuit breakers and could also be connected to
remote controlled switches in the yard, the relay may serve as a conduit for super-
visory control tasks at the substation. The control commands flow from the system
center, through the substation host computer and to the relay computers. All the
relay computers within the station are linked to the substation host computer. This
host acts as adata concentrator for all historical and oscillography records collected
by the relay computers. It – along with all other substation computers – transmits
these data to the system central computer. The substation host computer also pro-
vides an interface between the relay computers and the station operators. Through
this interface the relay settings, calibration, target interrogation, or diagnostic and
maintenance functions can be performed. The substation host computer may also
be used to produce some coordinated sequence-of-events for the substation as an
aid to station maintenance personnel.
The role of the central computer is even less critical in the conventional relaying
process. It initiates various supervisory control commands at the behest of the oper-
ator. It also collects historical data from all the substation computers and creates
oscillography, coordinated sequence of event analyses, and various book-keeping
functions regarding the operations performed at the station. The central computer
will play a more direct role if adaptive relaying becomes accepted by the relay-
ing community. Adaptive relaying principles and their relationship to computer
relaying have been discussed in some recent publications.21–23
The functions of various computers in the system wide computer hierarchy may
be summarized as follows:
Level I: Relaying, input output to the switch yard, measurements, control, diag-
nostics, man-machine interface, communications with level II.

Problems 21
Level II: Man-machine interface, data acquisition and storage, sequence of events
analyses and coordination, assignment for back-up in case of failures, communi-
cation with level I and level III computers.
Level III: Initiate control actions, collect and collate system wide sequence of
eventanalyses,communicationwithlevelII,oscillographyandreportpreparation,
adaptive relaying.
1.8 Summary
In this chapter, we have traced the development of computer relaying. We have
examined the motivation behind this development, and the expectations for systems
of the future. Computer based relays have become the standard of the electric
power industry. Their service record in field installations has been comparable
to that of traditional relays, and in many respects they offer advantages which
are not readily available with traditional relays. Examples of such features are
adaptive relaying (to be considered in Chapter 10), oscillography records saved
for post-mortem analyses, and the ability to address the relays from remote sites
through available communication links. In fact, the communication capability is the
single most valuable asset of computer based relays. Of course, the communication
capability brings with it the concern for security from malicious intervention from
unauthorized persons. As with most computer based systems, this concern can be
alleviated by appropriate fire-walls and other security measures.
In this chapter we have considered in detail the functional block diagram of a
computer relay and its place in the hierarchical system wide computer system. We
have discussed the Analog to Digital conversion process, and the sources of errors
in data conversion. We have also discussed the anti-aliasing filter design, and its
contribution to the overall error in the relay input system. The Problems that follow
further illustrate many of these concepts.
Problems
1.1 A500kVtransmissionlinehasanormalloadcurrentof1000amperesprimary,
and a maximum symmetrical fault current of 30000 amperes. Determine the
CT and CVT ratios and ohmic values of shunts and potential dividers in their
respectivesecondarycircuits.AssumethatafullDCoffsetmayoccurinthefault
current, and allow for a dynamic overvoltage of 20%. Determine the smallest
loadcurrentthattheinputsystemcanreadiftheADCusedisa12bitconverter.
1.2 Consider the non-simultaneous sampling of two input signals. Assume the
differencebetweensamplinginstantsforthetwosignalstobe30%ofthesam-
pling interval. What is the error in the sample of one signal calculated to be
simultaneous with the sample of the other signal using a linear interpolation
formula? Assume that both input signals are of pure fundamental frequency.

| 22  |     |     | Introduction | to computer | relaying |
| --- | --- | --- | ------------ | ----------- | -------- |
Assume suitable sampling rates, and arbitrary placement of sampling instants
| on the waveforms. |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- |
1.3 A phasor is calculated from samples of an input signal taken over one period.
If the samples are obtained with a 12 bit ADC, what is the error in the phasor
computationduetothequantizationerror?Obtainthegreatestupperboundfor
the error in magnitude and phase angle of the phasor. The phasor calculation
is explained in Chapter 3. For the present, assume that the phasor is the same
as the fundamental frequency component calculated by the familiar Fourier
| series formula. |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
1.4 Repeat Problem 1.3 for the errors introduced by an imperfect input amplifier
having an offset error, a gain error, and gain nonlinearity. Assume suitable
| bounds for | these errors. |     |     |     |     |
| ---------- | ------------- | --- | --- | --- | --- |
1.5 Design a third order Butterworth filter with a cut-off frequency of 360Hz.
Plot its transient response to a step input function. Also plot its frequency
| response | for a frequency | range of | DC to 720Hz. |     |     |
| -------- | --------------- | -------- | ------------ | --- | --- |
1.6 Design a two-stage RC filter with a cut-off frequency of 300Hz, and compare
itsfrequencyandstepinputresponsewiththoseofthetwo-stageRCfilterhav-
ing a cut-off frequency of 360Hz. Often a 300Hz cut-off frequency filter may
be used for anti-aliasing purposes where sampling frequency is 720Hz. This
givesbetternoiseimmunitytothefilter,butitisofcoursenotsuitablewhenit
is necessary to calculate the fifth harmonic of the input signal – for example,
| in a transformer | relay. |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- |
1.7 Complete the design of the second order Butterworth filter by finding the
| values of | the components | in Figure | 1.10. |     |            |
| --------- | -------------- | --------- | ----- | --- | ---------- |
| 1.8       |                |           |       |     | (cid:1)G/G |
Verify the expressions for the relative gain and phase angle variations
and(cid:1)φ/φgiveninSection1.6forthetwo-stageRCfilter.Determineageneral
formula, and then substitute the values of the resistors and capacitors from
| Figure 1.8(a). |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
1.9 Derive expressions similar to those in Problem 1.8 for the two-stage Butter-
worth filter, and obtain numerical results for the filter design of Problem 1.5
Verify that, for the same relative variation in component values, the Butter-
worth filter has greater variation in its gain and phase shift when compared
| to the two-stage | RC filter. |     |     |     |     |
| ---------------- | ---------- | --- | --- | --- | --- |
References
[1] Rockefeller,G. D. (1969) Fault protection witha digital computer, IEEE Transactions
onPowerApparatusandSystems(IEEETrans.onPAS),vol.88,no.4,pp.438–461.
[2] MannB.J.andMorrison,I.F.(1971)Digitalcalculationofimpedancefortransmission
line protection, IEEE Trans. on PAS, vol. 90, no. 1, pp. 270–279.

References 23
[3] Poncelet,R.(1972)Theuseofdigitalcomputersfornetworkprotection,CIGRE´ Paper
no. 32-08.
[4] Takagi, T., Baba, J., Uemura K., and Sakaguchi, T. (1977) Fault protection based on
traveling wave theory – Part I: Theory, IEEE Summer Power Meeting, Mexico City,
paper no. A77 750-3.
[5] Dommel, H. W. and Michels, J. M. (1978) High speed relaying using travelling wave
transient analysis, IEEE PES Winter Power Meeting, New York, January 1978, Paper
No. A78 214-9.
[6] Cory B. J. and Moont, J. F. (1970) Application of digital computers to busbar protec-
tion, IEEE Conference on the Application of Computers to Power System Protection
and Metering, Bournemouth, England, May 1970, pp. 201–209.
[7] Sykes, J. A. and Morrison, I. F. (1972) A proposed method of harmonic restraint
differential protection of transformers by digital computers, IEEE Trans. on PAS, vol.
91, no. 3, pp. 1266–1272.
[8] Sachdev, M. S. and Wind, D. W. (1973) Generator differential protection using a
hybrid computer, IEEE Trans. on PAS, vol. 92, no. 6, pp. 2063–2072.
[9] Phadke, A. G., Horowitz, S. H., Thorp, J. S. (1983) Integrated computer system for
protection and control of high voltage substations, CIGRE´ Colloquium, Tokyo, Japan,
November 1983.
[10] Deliyannides J. S. and Udren, E. A. (1985) From concepts to reality: the implemen-
tation of an integrated protection and control system, Developments in Power System
Protection, IEE Conference Publication no. 249, London, April 1985, pp. 24–28.
[11] North American Reliability Council, System Disturbance, 1983, 1984 etc. Research
Park, Terhune Road, Princeton, New Jersey.
[12] Surge Withstand Capability (SWC) Tests for Protective Relays and Relay Systems,
P472/D9, C37.90.1-198x. Draft Document of the Power System Relaying Committee,
June 8, 1987.
[13] Surge Withstand Capability (SWC) Tests, ANSI C37.90a, 1974.
[14] Kotheimer W. C. and Mankoff, L. L. (1977) Electromagnetic interference and solid
state protective relays, IEEE Trans. on PAS, vol. PAS-96, no. 4, pp. 1311–1317.
[15] Henrici, P. (1964) ElementsofNumericalAnalysis, John Wiley & Sons, Ltd.
[16] ProductDataBook, Burr-Brown Research Corporation, 1982, Tucson, Arizona.
[17] Candy, J. C. and Temes, G. C. (1991) Oversampling methods for data conversion,
IEEE Pacific Rim Conference on Communications, Computers and Signal Processing,
May 9–10, 1991.
[18] Chen,Wai-Kai(1986)PassiveandActiveFilters,JohnWiley&Sons,Ltd,Chichester.
[19] Udren,E.A.(1985)Anintegrated,microcomputerbasedsystemforrelayingandcon-
trolofsubstations:designfeaturesandtestingprogram,12thAnnualWesternProtective
Relaying Conference, Spokane, Washington, October 1985.
[20] Phadke, A. G. (Convener), CIGRE´ Working Group 34.02 Final Report, Paris, 1985.
[21] Thorp,J.S.,Phadke,A.G.,Horowitz,S.H.andBegovic,M.M.(1987)Someapplica-
tionsofphasormeasurementstoadaptiveprotection,ProceedingsofPICA,Montreal.
[22] Horowitz, S. H., Phadke, A. G., Thorp, J. S. 1987 Adaptive transmission system
relaying, IEEE PES Summer Power Meeting, San Francisco, 1987.
[23] Phadke, A. G., Thorp, J. S., Horowitz, S. H. (1987) Impact of adaptive protection on
power system control, Proceedings of PSCC, Lisbon.

2
Relaying practices
2.1 Introduction to protection systems
In this chapter we will summarize the operating principles of different types of
relays, and express their operating principles through their performance equations.
The performance equation is a mathematical relationship between the input
quantities of a relay and its output. Generally, the inputs are voltages and
currents – sometimes supplemented by status of some contacts – and the outputs
are status changes (on-off) of the output contacts of the relay. Conventional relay
performance is described in terms of voltage and current phasor inputs, and we will
follow the same practice in this chapter. However, it must be understood that the
phasor concept implies steady-state fundamental frequency sinusoidal waveforms;
while immediately following a fault the currents and voltages of a power system
are rich in transient components of other than fundamental frequency. As will be
seen in the next chapter, the phasor representation of an input quantity can be
defined under these conditions, and this interpretation of the phasor under transient
conditions will be understood in the performance equations derived in this chapter.
It should also be mentioned that the reason for reviewing the performance
equations of conventional relays is to provide a point of reference for computer
relaying development. It will be found that in most instances the conventional
relaying equations provide the ideal method of achieving a protection goal. It is
sound practice to examine ways of implementing conventional relaying principles
in a digital computer before going on to newer developments. In this fashion, it
can be assured that the job of meeting relaying needs – done admirably by most
conventional relays – is also done by the computer relays. Only then can we begin
to explore development of newer relaying principles. Although we will describe
the operating principles of various relays, it should be noted that their application
to power systems is a specialized field, and by and large we will not get into
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

26 Relaying practices
application related matters. For example, we will describe how an overcurrent
relay functions, but we will not describe how a set of overcurrent relays can be
applied for transmission line protection. This is in keeping with our objective of
describing the computer relaying technology, i.e. how computer relays work. For
the most part, their application to solve a specific protection problem is similar
to that of conventional relays. For a complete treatment of traditional relaying
and application practices, the reader is referred to several excellent text books
and reference manuals on protective relaying.1–5 In addition, the IEEE Press has
published an excellent collection of important papers dealing with all aspects of
relaying.6
Earliest relays were electromechanical devices consisting of plungers, balanced-
beams and induction discs or cups. With the exception of the balanced-beam types,
all other electromechanical relays are in use at the present time. Electromechanical
relaysarerobust – bothmechanicallyandfromthepointofviewofelectromagnetic
interference (EMI). Although they can be very fast (quarter cycle operating time),
usually they are slow – their speed of operation is measured in cycles or seconds.
They also require a fairly high amount of energy to operate, thereby necessitating
current and voltage transformers with relatively high volt-ampere capability.
In the late 1950s solid-state relays began to appear. These were designed with
discrete electronic components such as diodes, transistors and operational ampli-
fiers. Early solid-state relays were plagued by failures of components due to EMI,
and by failures brought on by the high failure rate of the early solid state com-
ponents. To a certain extent, some relay engineers still consider solid state relays
to be less reliable than their electromechanical counterparts. However, for most
users solid-state relays became an important element of modern protection system
design. Modern solid state relays are relatively maintenance-free and offer a greater
flexibility as far as protection applications are concerned. Their operating speed
is high – of the order of one cycle or less. On many power systems, the protec-
tion system consisted of a combination of solid state relays and electromechanical
relays – electromechanical relays being more common in simpler applications such
as overcurrent relaying, while solid-state relays dominated in more complex appli-
cations such as pilot relaying or step-distance relaying. In recent years, computer
relayshavesupplantedsolidstateandelectromechanicalrelaysasprotectionsystems
of choice.
2.2 Functions of a protection system
A protection system protects the power system from the deleterious effects of a
sustained fault. A fault (meaning in most cases a short circuit, but more gener-
ally an abnormal system condition) occurs as a random event. If some faulted
power system component (line, bus, transformer, etc.) is not isolated from the sys-
tem quickly, it may lead to power system instability or break-up of the system
through the action of other automatic protective devices. A protection system must

Functions of a protection system 27
CT Breaker
Relay
CVT
Battery
Figure 2.1 Subsystems of a protection system. Besides relays, the protection system con-
sists of transducers, circuit breakers and station battery
therefore remove the faulted element from the rest of the power system as quickly
as possible.
Although a protection system is usually understood to mean relays, it consists
of many other subsystems which contribute to the fault removal process. These
subsystems are identified in Figure 2.1. The circuit breaker actually isolates the
faulted circuit by interrupting the current at or near current zero. A modern Extra
High Voltage (EHV) circuit breaker can interrupt fault currents of the order of
100000 amperes at system voltages of up to 800kV. It can do this as quickly as
the first current zero after the initiation of the fault, although more often it does
so at the second or third current zero. The breaker is operated by energizing its
trip coil from the station battery, and the relay(s) do this job by closing contacts
between the battery and the trip-coil. Very often other relays (reclosing relays) are
used to reclose the circuit breaker after a suitable time interval.
The transducers (current and voltage transformers, or CTs and CVTs) constitute
another major component of the protection system. They are necessary because
the high magnitude currents and voltages of the power system must be reduced to
more manageable levels in order to drive low energy (and hence safe for human
access)devicessuchasrelays.Wewillconsiderthecurrentandvoltagetransformers
in some detail in Section 2.6. For the present, it is sufficient to note that certain
features of the transducers have been standardized. Current transformer secondary
rating has been standardized at 5 amperes or 1ampere, the latter standard being
more common in Europe. (A few other standard ratings also exist but they are
not very common). This implies that the maximum load current in the primary
winding of the current transformer would produce 5 amperes (1ampere) or less
in its secondary winding. This leads to a desired CT winding ratio, which is then
approximated by one of the standard CT ratios available. The voltage transformers
havethesecondarywindingsratedat67voltsphase-to-neutral.Withincertainlimits
(as discussed in Section 2.6), the current and voltage transformers reproduce the
primarycurrentandvoltagewaveformsfaithfullyontheirsecondaryside. Therelay

28 Relaying practices
thus sees a scaled down version of currents and voltages that exist on the power
system.
The last and most important component for our discussion of the protection
system is the relay. This is a device which responds to the condition of its inputs
(voltages, currents, or contact status) in such a manner that it provides appropriate
output signals to trip circuit breakers when input conditions correspond to faults for
which the relay is designed to operate. Relays are the logic elements in the entire
protection system. The design of a relay (whether analog or digital) must be such
that all fault conditions for which it is responsible produce a trip output, while no
other conditions should. Much of this book will be dedicated to design techniques
for relaying algorithms such that these requirements are met.
Thisisagoodpointtodiscusstheconceptofreliabilityasunderstoodinrelaying
literature. To a relay engineer, a reliable relay has two attributes: it is dependable,
and it is secure. Dependability implies that the relay will always operate for con-
ditions for which it is designed to operate. A relay is said to be secure if the
relay will not operate for any other power system disturbance. Of the two attributes
(dependability and security), the latter is more difficult to achieve. Every fault in
the neighborhood of a relay will disturb its input voltages and currents. However,
the relay should disregard those voltage and current conditions that are produced
by faults which are not the responsibility of the relay.
The responsibility for protection of a portion of the power system is defined
by a zone of protection. A zone of protection is a region clearly defined by an
imaginary boundary line on the power system one line diagram. A protection
system – consisting of one or several relays – is made responsible for all faults
occurring within the zone of protection. When such a fault occurs, the protection
system will activate trip coils of circuit breakers thereby isolating the faulty portion
of the power system inside the zone boundary. Usually – though not always – the
zonesofprotectionaredefinedbycircuitbreakers.Ifthezoneofprotectiondoesnot
have a circuit breaker at its boundary, the protection system must trip some remote
circuit breakers (transfer the trip command through a communication channel) to
de-energizethefaultedzone.Figure2.2showsaportionofthepowersystemdivided
into various zones of protection. Zones 1, 2, and 3 are transmission line protection
zones for the various lines. A fault on any of these lines would be detected by their
corresponding protection systems, and trip appropriate breakers at zone boundaries.
Zone 4 is the bus protection zone. Zone 5 is the zone for transformer protection.
Note that there is no circuit breaker at one end of this zone, and consequently
the transformer protection system must trip the breaker at bus A, and through a
communication channel remotely trip the breaker at bus C.
Note also that the zones of protection always overlap. This is in order to ensure
that no portion of the system is left without primary high speed protection (i.e.
there are no blind spots in the protection system). Although overlap is achieved in
Figure 2.2 by including the circuit breaker in each neighboring zone, in reality this
may not be possible under all circumstances. Zone overlap is achieved through the

Functions of a protection system 29
A 2 B
5
1
4
3
C
Figure2.2 Zonesofprotection.Zone2definestheboundaryforprotectionoftransmission
line A-B. Zone 4 defines bus-A protection. Zone 5 is a transformer protection zone
A
A
B B
To A To A
To B (a) To B (b)
Figure2.3 Principleofzoneoverlap.(a)Whencurrenttransformersareavailableoneither
sideofthebreaker.(b)Whenasinglecurrenttransformerwithmultiplesecondarywindings
is available
proper choice of current transformers dedicated toeachprotection system. Consider
the arrangement shown in Figure 2.3(a). A current transformer is assumed to exist
oneithersideofthecircuitbreaker.Inthiscase,theprotectionsystemsoneitherside
of the breaker use current transformers from opposite sides of the circuit breaker.
When current transformers are not available on both sides of the circuit breakers,
an overlap is achieved by using current transformer secondary windings on the far
side as illustrated in Figure 2.3(b). In this case, although there is no blind spot in
relaying,tripping for faults between the circuit breaker and the CT requires special
consideration. It is desirable to keep the region of overlap as small as possible.
Occasionally, a zone will be protected by several protection systems in order
to make sure that failure of the protection system itself will not leave the power
system unprotected. This reinforces the dependability of the overall protection sys-
tem. In such cases, it is desirable to have as much independence between the two
protection systems as possible. It would be prohibitively expensive to duplicate the
circuit breaker, the current transformer, the voltage transformer, or even the station
battery. However, some degree of separateness may be obtained by using differ-
ent secondary windings of a current transformer for the two protection systems,
by using separate fuses in the voltage transformer circuit, by providing separate
trip coils for the circuit breaker, and in exceptional cases by providing separate

30 Relaying practices
batteries for relays and breaker trip circuits. These attempts are made in order to
avoid common failure modes among the different protection systems and thereby
to improve the dependability of the entire protection system.
Almost all the relays in use on power systems may be classified as follows:
1. Magnitude Relays: These relays respond to the magnitude of the input quantity.
Anexampleistheovercurrent relaywhichresponds tochanges inthemagnitude
(either the peak value or the rms value) of the input current.
2. Directional Relays: These relays respond to the phase angle between two AC
inputs. A commonly used directional relay may compare the phase angle of a
current withavoltage. Or, thephase angle of one current may be compared with
that of another current.
3. Ratio Relays: These relays respond to the ratio of two input signals expressed
as phasors. Ratio of two phasors is a complex number, and a ratio relay may
be designed to respond to the magnitude of this complex number or to the
complex number itself. The most common ratio relays are the several versions
of impedance or distance relays.
4. Differential Relays: These relays respond to the magnitude of the algebraic sum
of two or more inputs. In their most common form, the relays respond to the
algebraic sum of currents entering a zone of protection. This algebraic sum may
be made to represent the current in any fault (if it exists) inside the zone of
protection.
5. Pilot Relays: These relays utilize communicated information from remote loca-
tions as an input signal. This type of protection generally communicates the
decision made by a local relay of one of the four types described above to relays
at the remote terminals of a transmission line.
A functional description of input-output relationships of the five relay classes
described above will give us sufficient basis for the design of relays – all else is
applicationof thesedesigns toagivenprotectionproblem. Asfar asdigitalrelaying
is concerned, we may then proceed directly to a discussion of relaying algorithms.
However, we will give a very brief overview of the application of these relays to
system protection problems. As mentioned in Section 2.1, the reader will do well
to refer to several excellent books on application of relays to power systems. The
material in Sections 2.4, 2.5, and 2.6 is offered in order to provide a degree of
continuity in our development, as it is not advisable to develop a theory of relay
algorithm design without some note being taken of the application principles.
2.3 Protection of transmission lines
2.3.1 Overcurrent relays
When a fault occurs on a power system, the fault current is almost always greater
than the pre-fault load current in any power system element. A very simple and

| Protection | of transmission | lines |     | 31  |
| ---------- | --------------- | ----- | --- | --- |
effective relaying principle is that of using the current magnitude as an indicator
of a fault. Overcurrent relays (as such relays are known) can be used to protect
practically any power system element, i.e. transmission lines, transformers, gener-
ators, or motors. We will use a transmission line as an example to illustrate the
application. For a fault within the zone of protection, the fault current is smallest at
the far end of the line and greatest at the relay (breaker) end. It is assumed that the
system is radial – i.e. the source of power is only on the left side in Figure 2.4(a).
If the minimum fault current possible within the zone of protection is greater than
the maximum possible load current, it would be possible to define the operating
| principle | of a relay as | follows: |     |     |
| --------- | ------------- | -------- | --- | --- |
zone,trip
|     |     | |I|≥I fault | in  |     |
| --- | --- | ----------- | --- | --- |
p
|     |     | <I         | zone,do     |       |
| --- | --- | ---------- | ----------- | ----- |
|     |     | p no fault | in not trip | (2.1) |
where I is the current in the relay and I P is a setting described below. Note that
the current magnitude must be derived from an AC waveform which may include
a decaying DC component whose magnitude depends upon the instant of fault
occurrence. Figure 2.4(b) is a sketch of the variation in steady state AC fault
current – (known as the symmetrical fault current) with fault location. The relay
characteristic given by Equation (2.1) is defined in terms of the symmetrical fault
current.
The quantity I is known as the pickup setting of the relay. The above equation
P
describes an ideal relay operating characteristic as shown in Figure 2.5(a). The
relay does not operate (operating time is infinite) as long as the current magnitude
is less than I . If the current magnitude exceeds I , the relay operates taking a time
|     | P   |     | P   |     |
| --- | --- | --- | --- | --- |
T to close its contacts. This type of relay is termed an instantaneous relay. It
min
A
B
R
(a)
|     |     | tnerruC I |     |     |
| --- | --- | --------- | --- | --- |
fault
I
load
|     |     | A   | Location B |     |
| --- | --- | --- | ---------- | --- |
(b)
Figure 2.4 Overcurrent protection of transmission lines. (a) Radial system protection.
| (b) Fault | current magnitude | as a function | of fault location |     |
| --------- | ----------------- | ------------- | ----------------- | --- |

32 Relaying practices
Current
emiT emiT
Time
Dial
T
min
I p Current I p
(a) (b)
Figure 2.5 Overcurrent relay operating time. (a) Instantaneous relay, and (b) Time over-
current relay
is often desirable to have the operating time depend upon the current magnitude:
being smallest when the current is greatest as shown in Figure 2.5(b). Such a
characteristic is known as an inverse-time characteristic and the relay is known as
a time overcurrent relay. In practice, I would be selected to lie between maximum
p
load current and minimum fault current.
A ratio of 3 between I and the minimum fault current is considered desirable
p
for getting a well defined operating time for all faults. There is a great variety
in the shape of the inverse-time characteristic: the shapes are described as being
‘inverse’,‘veryinverse’,and‘extremelyinverse’.Admittedly,theseareratherloose
descriptions and the actual characteristic furnished by the manufacturer must be
used in determining the relay setting. Furthermore, even for a relay of a given type,
the operating time can be moved up (made slower) by turning the ‘time dial’ on
the relay. This is also illustrated in Figure 2.5(b). By convention the lowest time
dial setting (fastest operating time) is generally 1/2, and the slowest setting is 10.
A typical time overcurrent relay characteristic of a commercially available relay is
shown in Figure 2.6. The reader may want to work out some of the problems at the
end of this chapter to gain insight into the application of time overcurrent relays
and relay coordination.
2.3.2 Directional relays
Whenthepowersystemisnotradial(sourceononesideofthelineasinFigure2.4),
an overcurrent relay may not be able to provide adequate protection. Consider the
zoneofprotectionforalinewithsourcesbehindbothendsasshowninFigure2.7(a).
In such a case, depending upon the relative strength of the source on the two sides,
it may be that for a fault such as F (which is within the zone of protection of
1
the transmission line), the current flowing through the relay at B is less than the
current that would flow through the same relay (albeit in a reverse direction) for a
fault at F – which is outside its zone of protection. In such a case, an overcurrent
2
relay set to trip for a fault at F would also trip for a fault at F – an unacceptable
1 2
loss of security. This situation is resolved by providing a ‘directional’ relay at B
(as well as at A) which does not operate when the fault is away from the zone of

Protection of transmission lines 33
10.0
Multiples of pickup setting
sdnoces
ni
emit
gnitarepO
gnittes
laid-emiT
1.0
10
8
6
4
3
2
0.1
1
1/2
1 10 40
Figure 2.6 A typical commercial time overcurrent relay characteristic
A F 1 B F 2
(a)
I Reverse
B fault
E
B
Forward
I
B fault
(b)
Figure 2.7 Line protection for a loop system. Equivalent sources on both ends of the
line contribute current for a fault on the line. (a) System diagram. (b) Voltage and current
phasors

34 Relaying practices
protection, and operates when the fault is in the ‘forward’ direction – i.e. towards
thezoneofprotection.Thesedirectionalrelaysmayusethephaseanglebetweenthe
fault current and some reference quantity (the corresponding voltage, for example)
to determine the direction of the fault. Figure 2.7(b) shows the voltage behind the
fault and the fault current. Assuming that the fault circuit consisting mostly of
transmission lines is almost purely inductive the fault current lags the voltage by
almost 90◦. If theangle betweenthereference phasor (voltage) and thefault current
is θ, then the relay operating principle could be described by
−π ≤ θ ≤ 0,operate
0 ≤ θ ≤ π,block (2.2)
It should be noted that, although the region of operation and blocking takes
up the entire plane (0 ≤ θ ≤ π) in the above definition, the actual angles for a
realistic fault will be around −π/2 for forward faults and around π/2 for reverse
faults. Thus the operating principle could be made more selective by defining zones
around ±π/2. The voltage used as a reference must of course be the voltage that
is driving the fault current. Thus for a phase a to ground fault, the a phase voltage
and current must be used in this comparison. For a phase b-c fault, phase b current
and voltage between phases b and c must be used. Occasionally, a current may be
used as a reference phasor. Consider the transformer connected at the bus where
the line under consideration originates (see Figure 2.8). For a ground fault within
the zone of protection (e.g. at F ), the transformer neutral current and the fault
1
current will be in phase with each other. On the other hand, for a fault such as
at F the faulted phase current flowing through the relay under consideration will
2
reverse, while the transformer neutral current will maintain its direction. Thus the
transformer neutral current provides an effective reference for directional relays.
I
F
F
1
I
n F
2
I
n
I F2 I n I F1
Figure 2.8 Use of transformer neutral current for polarizing a directional relay

Protection of transmission lines 35
The quantity providing the reference is often called a ‘polarizing’ quantity of the
directional relay. The advantage of using current for polarizing is that the relay
may be applicable where only CTs are available. The reader should beware that
in case of an auto-transformer, the neutral current is not always dependable as a
polarizing quantity. Instead, the current in a delta winding (if it is available) is
far more desirable, although even this may be subject to reversals under certain
conditions.
Generally,aprotectionsystemdesignedforphasefaultsisdistinctfromprotection
for ground faults. This is so because (a) ground fault currents are dependent upon
system grounding, and (b) ground faults produce zero-sequence currents whereas
there is very little zero-sequence current during normal operation. Thus the pickup
settings of the ground fault relays can be made more sensitive than those of phase
fault relays. It should be clear that the three phase-to-phase fault relays respond-
ing to the so-called delta currents, viz. (I −I ), (I −I ), (I −I ), are needed
a b b c c a
to protect against all phase-to-phase faults; while a separate relay responding to
the zero sequence current. (I +I +I )/3 is provided for ground fault protection.
a b c
Appropriate polarizing sources must also be provided for each relay if a directional
overcurrentfunctionisneeded.Oftenoneofthephase-to-phaserelaysmaybeomit-
ted, as the remaining two phase-to-phase relays and the zero-sequence current relay
provide adequate protection against all faults.
2.3.3 Distance relays
As mentioned in Section 2.3, the pickup value of an overcurrent relay must be set
between the maximum load current and the minimum fault current experienced by
the relay. In high voltage and extra-high voltage networks, these parameters are
often not well defined, nor are they separated sufficiently from each other to allow
a safe selection for a pickup setting. For such cases, the distance relay furnishes
excellent protection under all circumstances. Consider the transmission line shown
in Figure 2.9(a). Let there be a fault at a fractional distance k from the relay
location. If there is a phase-to-phase fault between phases x and y such that x (cid:6)= y;
and x,y = a,b,c, then it can be shown that6,7
E −E
x y
= kZ (2.3)
1
I −I
x y
where Z is the positive sequence impedance of the entire line. Similarly, for a
1
phase to ground fault on phase x
E
x
= kZ (2.4)
1
I +mI
x 0
m being equal to (Z – Z )/Z , and Z is the zero sequence impedance of the
0 1 1 0
line.8 The ratios of appropriate voltages and currents represent the fraction of line

36 Relaying practices
A F B
V,I k
(a)
X B
k
A R
(b)
Figure 2.9 Distance relaying of high voltage transmission lines. (a) Line with a fault in
the zone of protection. (b) Distance relay characteristic
impedance (positive sequence) at which a fault occurs. The computed ratio can be
compared with the total positive sequence impedance of the zone being protected,
and if smaller, trip output is produced. It must be noted that the ratio of the two
phasors – numerator and denominator in Equations (2.3) and (2.4) being complex
numbers is a complex number. Consequently, the comparison is made in the com-
plex impedance plane as shown in Figure 2.9(b). For faults on the transmission
line, the ratio is a complex number lying on A-B. However, allowing for various
inaccuracies within the transducers and in the relay, as well as due to fault arc
resistance, it becomes necessary to define the fault region in the complex plane as
having a substantial area surrounding the line AB. A rectangle, circle, or a segment
of a circle are all acceptable shapes, and define the zone of protection in the R-X
plane. The circular shape originated with electromechanical relays and has been
carried over in many solid-state relays (and in some computer relays) as well. The
circular zone shown in Figure 2.9(b) belongs to the class of relays known as offset
impedance relays – the center of the circle being offset from the origin. When the
circle passes through the origin as illustrated, the shape is known as a ‘mho’ relay.
Knowing the inaccuracies and fault resistance that must be allowed for, a more
accurate zone shape can be defined so as to occupy a minimum area of the com-
plex R-X plane. The rectangle (or more generally a quadrilateral) enclosing the line
AB is a more appropriate shape for distance relaying, and most computer relays
provide such a shape.
As in the case of overcurrent relays, complete protection with distance relays
involves three phase distance relays (using delta voltages and currents) and three
ground distancerelaystoprotectagainst allpossiblefaults.Sinceovercurrent relays

Protection of transmission lines 37
can be used for ground fault protection effectively (there being no significant
zero-sequence component in load currents), often three phase distance relays and
one ground overcurrent relay provide adequate protection.
Yet another application related subject is the manner in which distance relays
are put to use. The performance of a distance relay near its zone boundaries is not
verypredictablebecauseofvarioustypesoferrorsmentionedearlier.Consequently,
it becomes necessary to use multiple zones of protection to cover the entire line
dependably and securely. Consider the protection of line AB in Figure 2.10(a).
The zone of protection is that shown by a dotted line. However, to be sure of
covering it in the presence of input errors, two zones (Zone 1 and Zone 2) are
used. Zone 1 relay operates instantaneously (no intentional delay – i.e. in about
one to two cycles) while a fault in Zone 2 causes the relay to operate with an added
delay (generally of the order of 20 to 30 cycles). In this fashion, the entire line
is protected even where the zone boundary is not very precisely determined. The
Zone 2 operating delay is to permit other relays such as those belonging to lines
BC and BD to operate for faults within their respective first zones – such as F or
2
F – which may lie in Zone 2 of the relay protecting line AB. Remembering that
3
a similar protection system exists at the B terminal looking towards A, it is clear
that such a line protection scheme would provide high speed protection from both
B
Zone 1
Zone 2 F
X Y 2
C
F
3
A D
Zone 3
(a)
X
D
C
B
A R
(b)
Figure2.10 Stepdistancerelayingofatransmissionline.(a)Transmissionlinesprotected
by distance relays. (b) Three zones of protection

38 Relaying practices
ends against faults in the middle portion of the line (in region XY); while faults
on the line but outside the XY region are cleared instantaneously by the near relay
and with a Zone 2 time delay by the distant relay. In addition to these two zones,
often a third zone (with an additional time delay of the order of one second) is
provided at each end in order to provide remote backup for the protection of the
neighboring circuits. Zone 3 overlaps the longest line connected to the same bus as
the line being protected. The three protection zones are shown in Figure 2.10(b). It
should be noted that often, because of the system load, it is not possible to obtain
a secure Zone 3 setting on high voltage or extra-high voltage networks.
2.3.4 Phasor diagrams and R-X diagrams5
The relay characteristics of Figures 2.9 and 2.10 are in the R-X plane. These
diagrams are generally known as R-X diagrams, and are very useful in determin-
ing response of distance relays for different types of system conditions including
faults, load changes, and power swings. It is well to understand how distance relay
responses in the R-X plane can be derived from the phasor diagrams representing
the current and voltage phasors representing the inputs to a distance relay.
Assume that inputs to the distance relay are voltage and current having phasor
representations E and I. The key concept is that of ‘apparent impedance’ seen by
the relay. Apparent impedance is defined as the ratio of the voltage phasor to the
current phasor:
Z ≡ R+jX = E/I (2.5)
app
Consider the case of the current phasor being (1+j0). In that case, the voltage
phasor becomes equal to the apparent impedance. This concept can be formalized
by a process of rotating the entire E-I phasor diagram until the current phasor
becomes aligned with the real axis, and then changing the length of the phasors
until the current phasor falls becomes 1.0 in length. The process is illustrated in
Figure 2.11(a). The complex plane is now labeled R-X plane, and the apparent
impedance seen by a relay supplied with phasor E and I is as shown.
Figure 2.11(b) illustrates the effect of variations in current magnitude and phase
angle on the R-X diagram. For lagging currents, which correspond to active and
reactive power flowing from the bus into the line (with current and voltage phasor
reference directions as shown) the apparent impedance falls in the first quadrant.
The right half of the R-X plane corresponds to real power flowing into the line,
while the left half corresponds to real power flowing into the bus. Similarly the
upper half of the R-X plane corresponds to reactive power flowing into the line,
while the lower half corresponds to reactive power flowing into the bus. Increasing
current magnitude or decreasing voltage magnitude brings the apparent impedance
closertotheoriginoftheR-Xdiagram.Thisobservationisattheheartofloadability
limits of distance relays. As the apparent impedance approaches the origin of the

| Protection | of transmission | lines |     |     | 39  |
| ---------- | --------------- | ----- | --- | --- | --- |
I
E
E I
|     |     |     | Q into line  | P & Q     |     |
| --- | --- | --- | ------------ | --------- | --- |
|     | X   |     | P into bus   | Into line |     |
Increasing
Current
magnitude
Z app
1.0 R
|     |     |     | P & Q    | P into line  |     |
| --- | --- | --- | -------- | ------------ | --- |
|     |     |     | Into bus | Q into bus   |     |
|     |     | (a) | (b)      |              |     |
Figure 2.11 Apparent impedance seen by a relay energized by E and I phasors. (a) Con-
version of phasor diagram to R-X diagram. (b) Apparent impedance behavior for different
| power system | conditions |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- |
R-X diagram, it may eventually enter a characteristic of a relay located at the line
terminalinquestion.Excursionsbyapparentimpedanceintotherelaycharacteristics
during load changes or power swings have caused unnecessary trips of relays, often
| contributing | to cascading | failures of | the power systems. |     |     |
| ------------ | ------------ | ----------- | ------------------ | --- | --- |
In considering adaptive relaying applications in Chapter 10 we will make use
of these concepts in order to understand the response of distance relays to various
system conditions.
| 2.3.5 | Pilot relaying |     |     |     |     |
| ----- | -------------- | --- | --- | --- | --- |
Pilot relaying is used to protect transmission lines when it is desired that an entire
line (not just the region XY in Figure 2.10) be provided with high speed protection.
This is particularly desirable in an integrated network, where with only the near
breaker opening at high speed in zone 1 time, the delayed tripping of the remote
breaker would be intolerable to the system. In a sense, the power system is so
tightly knit that no fault is a ‘distant’ fault for which slow clearing can be accepted.
Two types of pilot relaying systems are in general use: the directional comparison
system and the phase comparison system. The actual implementation of each of
these systems could lead to additional sub-classifications: for example, permissive
ornon-permissive,overorunder-reaching.2 Thedetailsoftheseschemesarenottoo
importantforthepresentdiscussion – althoughundoubtedlytheymustbetakeninto
accountwhenactualrelayimplementationisconsidered.Thedirectionalcomparison
scheme calls for communicating from one end of a line to the other whether a fault
is in the direction of the zone of protection or in the opposite direction. As far as
the relay itself is concerned, this direction determination is accomplished through a

| 40  |     |     |     | Relaying | practices |
| --- | --- | --- | --- | -------- | --------- |
directional distance calculation. Thus from the point of view of relaying algorithm
| design, no | new concept | is introduced. |     |     |     |
| ---------- | ----------- | -------------- | --- | --- | --- |
A phase comparison system is closely related to the differential protection prin-
ciple. The relative phase angles of currents at the terminals of a line are compared
to determine if the algebraic sum of all currents entering a transmission line can
be non-zero. A true differential relay would require a check of the magnitude of
the algebraic sum as well. However, the communication channel requirements can
be kept at a modest level if only the phase information is exchanged. A segregated
phase comparison scheme applies the phase comparison criterion to each of the
three phase currents, whereas a combined phase comparison system uses a single
ACquantityderivedfromallthreephasecurrentsforthesakeofsuchacomparison.
Clearly in the latter case, the communication channel requirements are substantially
reduced. A phase comparison relaying system is particularly suitable in case of
transmission lines with series capacitor compensation. Also, since the phase com-
parison is made for currents alone, no voltage input is needed for such systems.
On the other hand, directional comparison systems do require voltage inputs since
an impedance calculation is involved. It should be noted that, if the communica-
tion system should fail, the phase comparison scheme becomes totally inoperative,
while the directional comparison system can be designed to provide some distance
relaying functions as a second (additional) protective function.
| 2.4 Transformer,  |     | reactor    | and generator | protection |     |
| ----------------- | --- | ---------- | ------------- | ---------- | --- |
| 2.4.1 Transformer |     | protection |               |            |     |
Small transformers are usually protected by fuses or overcurrent relays. Larger
transformers (2.5 MVA or greater in capacity) are usually protected by percent-
age current differential relays. Consider a two-winding single-phase transformer
illustrated in Figure 2.12. When the transformer is without a fault within the zone
| defined by | the two CTs |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- |
= −I
|     |     |     | I 1 N 1 | 2 N 2 T | (2.6) |
| --- | --- | --- | ------- | ------- | ----- |
1:T
| I   |     |     | I   | 2 I    |     |
| --- | --- | --- | --- | ------ | --- |
|     | 1   |     |     | d      |     |
|     | 1:n |     | 1:n | I = KI |     |
|     | 1   |     | 2   | d r    |     |
|     | i 1 |     | i   |        |     |
2
I d = kI r
|     |     | N :N |     |     |     |
| --- | --- | ---- | --- | --- | --- |
1 2
I
r
(a) (b)
Figure2.12 Percentagedifferentialprotectionofatransformer.(a)Thesingle-phasetrans-
| former. (b) | Slope of the | percentage | differential | characteristic |     |
| ----------- | ------------ | ---------- | ------------ | -------------- | --- |

| Transformer, | reactor | and generator protection |     |     | 41  |
| ------------ | ------- | ------------------------ | --- | --- | --- |
Equation (2.6) is an approximation, because it does not take into account the mag-
netizing current. N and N are the nominal turns of the two windings, and T is the
|     |     | 1 2 |     |     |     |
| --- | --- | --- | --- | --- | --- |
ratio of the tap changer. If the two current transformers have turns ratios of 1:n
1
| and 1:n | , respectively, | then |     |     |     |
| ------- | --------------- | ---- | --- | --- | --- |
2
I =n i
1 1 1
|     |     |     | I =n i |     | (2.7) |
| --- | --- | --- | ------ | --- | ----- |
2 2 2
When the tap changer is at the neutral tap setting (i.e. when T = 1), the CT
secondary currents i and i may be made equal in magnitude by choosing n and
|     |     | 1 2 |     |     | 1   |
| --- | --- | --- | --- | --- | --- |
n such that
2
|     |     |     | N n = N n |     | (2.8) |
| --- | --- | --- | --------- | --- | ----- |
|     |     |     | 1 1 2 2   |     |       |
Since the current transformers are selected from available standard ratio CTs, in
general N n (cid:6)= N n , and i −i (cid:6)= 0 for a transformer without a fault. The tap
|     | 1 1 2 | 2 1 | 2   |     |     |
| --- | ----- | --- | --- | --- | --- |
changer creates an additional disparity between i 1 and i 2 when it deviates from its
nominal value. And finally, the CT errors also make a contribution to the algebraic
| sum of | i and i . In | general then, |                 |     |     |
| ------ | ------------ | ------------- | --------------- | --- | --- |
|        | 1 2          |               |                 |     |     |
|        |              |               | (cid:2) (cid:3) |     |     |
i −i
|     |     |     | 1 2    |     |       |
| --- | --- | --- | ------ | --- | ----- |
|     |     | i   | +i = k |     | (2.9) |
|     |     | 1   | 2 2    |     |       |
or
I = kI
d r
The algebraic sum (i +i ) is the differential current I , and (|i |+|i |)/2 is the
|     |     | 1 2 |     | d 1 | 2   |
| --- | --- | --- | --- | --- | --- |
average value of the two winding currents referred to the CT secondaries. This is
knownastherestrainingcurrentI ,andEquation(2.9)indicatesthat,whenthetrans-
r
formeriswithoutaninternalfault,adifferentialcurrentequaltoktimestherestrain-
ing current may be developed. For the differential relay to refrain from tripping, it
becomes necessary toshapetherelaycharacteristicas showninFigure2.12(b). The
percentage slope K in Figure 2.12(b) is made greater than the k of Equation (2.9),
in order to allow for some safety margin. The constant k has three contributing
factors as shown in the Figure. The smaller the setting K of the relay, the more
sensitive is the relay in detecting small fault currents. Typical settings available for
| percentage | differential | relays are | 10, 20 or 40%. |     |     |
| ---------- | ------------ | ---------- | -------------- | --- | --- |
During energization of a transformer, abnormal currents may flow in the winding
that isbeing energized. These areknown asthemagnetizing inrush currents, caused
by the saturation of the transformer core for portions of a cycle. Typical inrush
currents are shown in Figure 2.13. The inrush may be quite severe if there is
remanence in the core and it is of a polarity which takes the core further into
saturation. As the relationship between the remanence and the flux build up caused
by energization is random, actual inrush obtained during an energization depends
upon chance. However, the fact remains that, during energization, high current

42 Relaying practices
Unfavorable remanence
Favorable remanence
I
1
I
1 No remanence
t
(a) (b)
Figure 2.13 Inrush current during energization of a transformer. The amount of inrush
depends upon the instant of switching and upon the remanence in the core
may flow in the primary of a transformer. This is exactly the condition obtained
when there is an internal fault in the transformer. It is thus necessary to distinguish
between a fault and an inrush transient.
The accepted technique for blocking the trip action of a percentage differential
relay under conditions of inrush isto make use of the high second harmonic current
in the inrush, whereas a fault current is almost purely of fundamental frequency.
Thesecondharmoniccurrent isusedasanother restrainingsignal (inadditiontothe
fundamental frequency restraining current I of Equation (2.9)). In designing a har-
r
monicrestraintpercentagedifferentialrelay,notemustbetakenofotherphenomena
which produce harmonics in the current waveforms.9 For example, an overexcited
transformer has significant fifth harmonic component in its magnetizing current,
and hence it is desirable to create a composite restraint function with 2nd and 5th
harmonics. On the other hand, if one of the CTs saturates during an internal fault,
the resulting third harmonic current in the secondary winding of the saturated CT
should not produce any restraint function.
Although current harmonics furnish a sound means of distinguishing faults from
no-fault conditions, other schemes for achieving the same end result are possible.
Thus a high voltage at the transformer terminal may also be used to indicate that
any differential current present must be due to magnetizing inrush. This, and some
other ideas, will be discussed more fully in Chapter 5.
It should also be noted that some of the most sensitive relays for transformer
protection are not electrical in nature. These are the Sudden Pressure Relay (SPR)
and the Buchholz relay.1
Three phase transformer protection generally follows the principles outlined
above. Incase of a wye-delta transformer, the linecurrents during normal operation
(or, through currents flowing when there is an external fault) on the wye and
the delta sides have a phase difference between them. This must be accounted
for before a differential relay can be connected. This is usually accomplished by
connecting the CTs in a reversed connection: in wye on the delta side of the main

| Transformer, | reactor and generator | protection |     | 43  |
| ------------ | --------------------- | ---------- | --- | --- |
|              |                       | i          | i   |     |
|              |                       | ai         | i A |     |
|              |                       | bi         | i B |     |
|              |                       | c          | C   |     |
Figure 2.14 Wye-delta transformer protection by percentage differential relay. The CT
connections compensate for the phase shift in the main transformer
transformer and in delta on the wye side. This is illustrated in Figure 2.14. The
same effect may be achieved through computation in a computer relay.
| 2.4.2 | Reactor protection |     |     |     |
| ----- | ------------------ | --- | --- | --- |
The main protection for a reactor is similar to generator differential protection,
discussed next. In addition, a turn-to-turn fault in a reactor can be detected by a
| distance | relay connected      | to look into | the reactor. |     |
| -------- | -------------------- | ------------ | ------------ | --- |
| 2.4.3    | Generator protection |              |              |     |
The current transformers used at the two ends (high side and neutral) of a generator
winding are specially matched so as to reduce the disparity in their performance.
Thisispossibleinthecaseofgenerators(andreactors)becausetheprimarycurrents
of the two CTs are identical (as was not the case for a transformer differential
relay). Also no allowance need be made for errors caused by tap changers. Thus, a
generator differential protection relay can be made extremely sensitive. Of course,
there is no need to worry about the magnetizing inrush current.
Another concern in case of generator protection is the rotor heating caused by
unbalanced stator currents. This is usually related to the amount of heating of the
rotor caused by negative sequence current in the stator windings. The negative
| sequence | current relay tests | for the quantity |     |     |
| -------- | ------------------- | ---------------- | --- | --- |
(cid:4)
|     |     | i2dt≥K,trip | alarm, |     |
| --- | --- | ----------- | ------ | --- |
or
2
|     |     | ≤K,no | operation. | (2.10) |
| --- | --- | ----- | ---------- | ------ |
The constant K is usually furnished by the generator manufacturer. Several other
generatorrelayingtasksareclosertobeingcontroltasksinthatoperatorintervention
or automatic control actions (slower than relay responses) are called for. Examples
of these functions are reverse power relay, field ground relay, generator capability
(overload) relay, and out-of-step relays. In Chapter 5 we will consider implemen-
tation of some of these functions with the help of conventional relays described in
Section 2.2.

44 Relaying practices
2.5 Bus protection
A bus, being a power system element that does not extend over long distances
(as transmission lines do), is ideally suited for protection by a differential relay.
Consider a bus and its associated circuits consisting of lines or transformers as
shown in Figure 2.15. The algebraic sum of all the circuit currents must be zero
when there is no bus fault. With all circuit CT ratios being equal, the secondary
currents also add to zero when there is no bus fault. The various CT inaccuracies
require that a percentage differential relay be used, but in this case the percentage
slope can be quite small, as there are no mismatched ratios or tap changers to be
concerned about. And of course, there is no magnetizing inrush phenomenon to
consider.
One area of concern is the saturation of a CT during an external fault. Consider
the fault at F in Figure 2.15. The current in the CT on this feeder is the sum of
all feeder currents, and consequently this CT is in danger of becoming saturated.
A saturated CT produces no secondary current while the CT core is in saturation.10
Typical waveforms of primary current, secondary current and the flux in the CT
corearegiveninFigure2.16.Wheneverthefluxdensitycrossesthesaturationlevel,
F
Figure 2.15 Bus protection with a differential relay. When there is no fault, the algebraic
sum of circuit currents is zero
Secondary current
i,φ
during saturation
φ
Saturation
i
level
t
remanence
Figure 2.16 Primary current, secondary current, and the flux in the core of a CT in
saturation. Remanence may cause saturation to set in earlier and last longer

Performance of current and voltage transformers 45
the secondary current becomes negligible. Under these conditions, the secondary
winding is no longer strongly coupled with the primary winding – the transformer
essentially acts like an air-core device.
A lack of strong coupling implies that the secondary winding presents a very
low impedance to any external circuit connected at its terminals, instead of acting
like a current source of high equivalent impedance. It should be clear that, if the
secondary current in one CT becomes zero for any period during an external fault,
the differential current will be equal to the missing current causing the relay to trip.
IngeneralthecoreofaproperlychosenCTshouldnotsaturatewithin1/2to1cycle
of fault inception. However, often the requirement placed on bus differential relays
is that they should restrain from operating for external faults even if a CT should
saturate in 1/4 cycle or less after the occurrence of a fault. This requirement places
a very confining restriction on a computer based bus differential relay. This subject
will be dealt with in Chapter 6.
However, analog relays have a very ingenious solution to the problem posed by
a saturating CT. Since the saturated CT secondary appears as a low impedance
path in the differential circuit, it is sufficient to make the relay a high-impedance
device. The spurious differential current produced by the saturated CT then flows
through its own secondary winding and by passes the relay having a much higher
impedance. The condition is illustrated in Figure 2.17. The saturation of the CT is
itself responsible for saving a false operation which would have resulted from the
saturation.
2.6 Performance of current and voltage transformers
2.6.1 Current transformers
We have already discussed in Section 2.5 the CT secondary current error caused
by saturation of the CT cores. These are quite substantial – when they occur the
secondary current disappears for a portion of the waveform. However, even when
the CT core is not saturated to such an extent, the secondary current is always
in error due to the small but non-zero magnetizing current required to set up the
R
F High
impedance
relay
Figure 2.17 Effect of saturating CT on a high impedance differential relay. The lower
impedance of the saturated CT secondary bypasses the differential current from the relay

| 46  |     |     |     | Relaying practices |
| --- | --- | --- | --- | ------------------ |
|     | Z   | Z   | V   | Z                  |
|     | l1  | l2  | 2   | l2                 |
I
|     | 1   | V   |       |       |
| --- | --- | --- | ----- | ----- |
|     |     | 2   | Z′ I′ |       |
|     | Z m | Z   | m m   | Z I b |
|     |     | b   |       | b     |
I
m
|     | (a) |     | (b) |     |
| --- | --- | --- | --- | --- |
I
1
V
2
I
b
I′
|     |     | m I |     |     |
| --- | --- | --- | --- | --- |
2
φ
(c)
Figure2.18 (a)Completeequivalentcircuitofacurrenttransformer.(b)Ausefulapprox-
| imation for | practical CTs. | (c) Phasor diagram |     |     |
| ----------- | -------------- | ------------------ | --- | --- |
flux in the core. Consider the equivalent circuit of a current transformer, shown in
Figure 2.18(a). The leakage reactance of primary and secondary windings is gener-
ally negligible in most practical current transformers; hence the equivalent circuit
of Figure 2.18(b) is more appropriate for its analysis. The load (burden) impedance
Z b includes resistance of all the secondary wiring as well as the impedance of all
instruments and relays connected to the CT. The primary current I , the secondary
1
I(cid:1) φ,
current I , the magnetizing current , the core flux and the voltage across the
b m
secondary winding V are shown in the phasor diagram of Figure 2.18(c). Note
2
that, although the phasor diagram is generally used in this analysis, there may be
some harmonics present in the magnetizing current due to the nonlinearity of the
core B-H characteristic. In any case, I differs from I by I(cid:1) , which is therefore the
2 b m
CT error for the primary current and burden impedance shown. It should be clear
that a smaller burden impedance Z causes smaller V and I(cid:1) ; thereby reducing
b 2 m
the CT error. If the magnetizing characteristic of the core is available, the CT error
can be evaluated for any operating conditions of the CT. The CT classifications
(such as 10C400 or 10T400) indicate the upper limit of the CT error as being 10%
when the primary current is 20 times normal and the secondary voltage is less than
or equal to 400volts. The letters C or T in the class designation indicate the type
of CT construction – C type being a better CT than the T type. The CT error is
generally kept low by a proper choice of CT and its connected burden. The only
point of departure for computer relaying is that conceivably the CT error could
be computed and corrected inside the computer relay if the CT characteristic and
burden impedance were given as inputs to the computer relay. This clearly cannot
be done in conventional relays. This idea has not been used in computer relaying
| applications | developed | so far. |     |     |
| ------------ | --------- | ------- | --- | --- |

Performance of current and voltage transformers 47
2.6.2 Voltage transformers
Some voltage transformers, especially those for lower voltage transmission, are
magneticallycoupledpotentialtransformerswithaprimarywindingandasecondary
winding. Such transformers are very accurate, and in general their transformation
errors can be neglected.
Afairlycommon voltagetransformerusesacapacitor voltagedivider network,as
shown in Figure 2.19(a). The voltage divider reduces the line potential to a few kV,
and is further reduced to the standard relaying voltage of 67volts line-to-neutral by
a magnetic core transformer. The capacitive voltage divider presents a capacitive
The´ve´nin impedance as shown in Figure 2.19(b), and in order to eliminate any
phase angle errors due to the load current flowing through the capacitive The´ve´nin
impedance, a tuning inductance L is connected in series with the primary winding.
By making 1/2πf(c +c ) = 2πfL, the phase shift across (c +c ) is exactly can-
1 2 1 2
celed by the phase shift across L at all load currents, and once again the secondary
voltage is in phase with the primary voltage. In general, the steady state error of
the Capacitive Voltage Transformer (CVT) is negligible.
However thetransient response of aCVTisof some concern inrelaydesign. The
equivalent circuit of Figure 2.19(b) can be used to determine the output waveform
acrosstheburdenwhenafaultoccursontheprimarycircuit.Astheprimaryvoltage
changes suddenly from its pre-fault value to its (smaller) post-fault value, the out-
put voltage undergoes a subsidence transient before settling to its final steady state
value. The subsidence transient magnitude depends upon CVT parameters, burden
impedance and power factor, and upon the angle of incidence of the primary fault.
Primary
voltage
C
1
L
C 2 Z b
(a)
L
C 1 +C 2 Z b
(b)
Figure 2.19 (a) Capacitive voltage transformer. (b) Equivalent circuit

48 Relaying practices
V Secondary V Secondary
voltage voltage
t t
Primary Primary
voltage voltage
(a) (b)
Figure 2.20 CVT transient response. (a) Complete primary voltage collapse at voltage
maximum. (b) Voltage collapse at zero voltage. Note that the secondary transient is much
more pronounced in case (b)
Ingeneral,thefaultsoccurring ator near zerovoltage producetheworstsubsidence
transient. Figures 2.20(a) and (b) show samples of CVT response for representative
installations.11 Although omitted from most simulation studies, usually a ferrores-
onance suppression circuit is also present on the CVT secondary side, and does
affect the transient response.
The CVT transient response causes difficulties in those relaying tasks which
require voltage inputs. In particular, faults causing near-complete voltage collapse
create false voltage pictures at the relay input terminals. Special attention should be
given to relay algorithm design in such cases, particularly if severe voltage collapse
may be caused by a fault near a zone boundary. Short transmission lines fed from
weak systems usually constitute difficult relay design problems due to transient
CVT errors.
2.6.3 Electronic current and voltage transformers
Electronic current transformers were discussed in technical literature in the early
1960s, but their practical realization useable in modern power systems became pos-
sibleinthe1980s.Inrecentyearstherehavebeendevelopmentsofelectroniccurrent
and voltage transformers which are promising source of input signals for computer
based relays. We will present a brief account of their principles of operation here
and refer the reader to the references cited above for additional information.
2.6.3.1 Electronic current transformers12
The operating principle of these devices (also known as Magneto-Optic Current
Transformers) is based on Faraday Effect, by which the plane of polarization of
a polarized light beam is deflected by an angle which depends upon the magnetic
field to which the beam is subjected.
The principle of operation of electronic current transformers is shown in
Figure 2.21. A light beam is produced by a LED, and collated by a lens before

Performance of current and voltage transformers 49
Current
carrying
conductor
Polarizer
and beam
splitter
Light beam
from LED
Faraday effect
Lens crystal block
Output
Signalprocessor
Figure 2.21 Schematic of the principle of operation of an electronic current transformer
it passes through a polarizer, where the beam is split into two parts. One part of
the beam goes directly to a detector in the signal processing circuit, while the
second part of the linearly polarized light beam is passed through a special crystal
block with total reflections taking place at its three corners so that the light beam
makes a complete circuit around the conductor through which the current to be
measured is flowing. By Ampere’s law, a complete circuit through the magnetic
field produced by the current leads to a closed path integral of the magnetic field,
which is proportional to the current. The deflection of the plane of polarization
of the light is thus proportional to the instantaneous value of the current. The
beam with deflected plane of polarization is also sent to the signal processor,
where the angle of rotation of the beam as it went through the magnetic field is
measured by comparison with the first half of the beam, and an output voltage
signal proportional to the instantaneous current value is produced. This signal can
then be routed to appropriate application. It should be clear that the voltage signal
is easily handled by computer relays, while traditional relays requiring heavy
current inputs must be supplied through a current amplifier.
2.6.3.2 Electronic voltage transformers13
The electronic voltage transformer is based upon the electro-optic device known as
Pockels cell, and is illustrated in Figure 2.22. A light beam produced by a LED
and collated by a lens, as in the case of the electronic current transformer is passed
through a polarizer and a quarter-wave plate, producing a circularly polarized light
beam. This beam is passed through a Pockels cell which is subjected to an electric
potential field produced by applying a voltage in a direction perpendicular to the
direction of the light beam. The effect of the passage through the electric field on

50 Relaying practices
Voltage
Input from
PT or CVT
Polarizer Analyzer
Light beam
from LED
Lens Quarter
Wave
Pockles
plate
Cell
Output
Signalprocessor
Figure 2.22 Schematic of the principle of operation of an electronic voltage transformer
the light beam is to convert the circularly polarized light beam to an elliptically
polarizedlightbeam,withthedegreeofellipticitybeingproportionaltothestrength
oftheelectricfield.Ananalyzersplitstheellipticallypolarizedbeamintwolinearly
polarized beams, with their planes of polarization perpendicular to each other. The
relative intensity of each of the beams is compared in the signal processor, which
measures the degree of ellipticity which is proportional to the instantaneous electric
field (and by inference the instantaneous value of the applied voltage). As before,
the measurement is converted to a voltage which reproduces the voltage applied
to the Pockels cell.
2.6.3.3 Rogowski coils
Rogowskicoilisahelicalcoilplacedinalooparoundthecurrentcarryingconductor
with a return conductor placed in the center of the helical coil as illustrated in
Figure 2.23. The coil has a non-magnetic core (for example air), and thus has no
saturation effects. The coil has a voltage induced which is proportional to the rate
Current carrying
conductor
Helical coil
Return conductor
Figure 2.23 Schematic of the principle of operation of a Rogowski coil

Problems 51
of change of its flux linkage. Since the flux is proportional to the current in the
conductor in the center, the voltage in the Rogowski coil is proportional to the rate
of change of current. This signal can be processed through an integrator (or first
sampledandthenintegrateddigitally)toprovideasignalproportionaltothecurrent.
Clearly the output of such a system is not suitable for conventional relays which
require large current signals to operate, but is convenient for computer relays.
The return conductor passing through the center of the coil cancels any induced
voltage due to any other interfering magnetic field which may be present. Although
this is not a main-stream current measuring circuit, versions of this design have
been used in integrated sensing and protection applications.14
2.7 Summary
Inthischapter,wehavepresentedaclassificationofrelaytypes,andhavedescribed
theirbehaviorwiththehelpofaninput-outputrelationship.Wehavepointedoutthe
importanceoftheconceptofaphasorduringtheoccurrenceoftransientphenomena.
Wehavegivenashortaccountofsomeoftherelayapplicationconsiderations;how-
ever, we have accepted that a thorough discussion of relay applications is beyond
the scope of this book. Finally, we have pointed out the causes of errors created by
current and voltage transformers. These errors ultimately affect the accuracy with
which a relay can discriminate between faults internal to its zone of protection, and
all other system transients. We have also described electronic current and voltage
transformer principles, which eliminate some of these sources of errors. This very
promising technology is still not in wide use in power systems. In the following
chapter we will begin a discussion of the mathematical basis for relaying algo-
rithms, and then take up an account of relaying algorithms which are in use at the
present time.
Problems
2.1 Fault calculations are usually performed with symmetrical components.
Review the procedure for calculating faults on a three-phase network with the
help of the sequence diagram. Verify that a three-phase fault involves only
the positive sequence network, the phase-to-phase fault involves the positive
and the negative sequence networks, and that all ground faults require the
zero sequence network, as well. Show that the phase-to-ground fault on
phase a is represented by a series connection of the sequence networks at the
point of fault. What would be the corresponding connection for a phase b to
ground fault?
2.2 A radial feeder is connected to a source having an impedance of 0.5 per unit.
Thefeederlengthis10mileswithapositivesequencereactanceof0.7ohmper
mile, and a zero sequence impedance of three times that value. Calculate the

52 Relaying practices
three-phasefaultcurrent,phase-to-phasefaultcurrent,andthephase-to-ground
fault current as a function of the fault location along the feeder. Plot the three
fault current magnitudes as a function of the distance from the sending end.
Assumethatthezerosequence impedanceof thesource isequal toitspositive
sequence impedance.
2.3 The overcurrent relay at bus A in Figure 2.4 is to be coordinated with the
relay to the right of bus B. The time dial setting of the relay at B is 1/2. It
picks up reliably for a minimum fault current of 650 amperes. Assuming a
CT ratio for the relay at bus B of 200:5, what should be the relay tap setting
of this relay if any desirable tap setting could be available? The maximum
fault current for a fault at bus B is 1000 amperes. Determine the time dial
setting, CT ratio and the relay tap setting for the relay at A. Assume the relay
characteristics as shown in Figure 2.6.
2.4 In problem 2.3, what is the safe load current (loadability) that can be carried
by the two relays?
2.5 Consider a three-phase autotransformer. Assume the primary voltage to be
69kV, while the secondary voltage is 345kV. The transformer leakage reac-
tance is 0.1 per unit on its own base. Assume a phase-to-ground fault at
varying distance from the terminals of the transformer (i.e. assume a variable
impedance between the transformer terminals and the fault point). Show that
the current in the neutral of the autotransformer is not always flowing up
the neutral, indicating that this current is an unsuitable polarizing current for
directional ground relaying.
2.6 Using the symmetrical component representation for phase-to-phase and
phase-to-ground faults developed in problem 2.1, show that Equations (2.3)
and (2.4) are valid.
2.7 A ‘mho’ characteristic is a circle passing through the origin in the com-
plex R-X plane. Assuming the diameter of the circle to be (r+jx), derive
an equation for the voltages and currents seen by a relay such that the
voltage-current pairs correspond to points on the relay characteristic.
2.8 A single-phase transformer is rated at 34.5kV primary and 345kV secondary.
The transformer is rated at 50 MVA. Determine the CT ratios to be used for
differential relaying of this transformer. Using standard types of CTs, what
should be the slope of the percentage differential relay if the transformer has
a tap changer with a range of ±6%? Allow for CT errors as well as a safety
margin for security.
2.9 Assume a normal load current flow in a three-phase wye-delta transformer.
Show the connections of a differential relay and the CT secondary wind-
ings so that the differential relay is in balance (i.e. no differential current is

References 53
produced for this condition). Assume suitable transformation ratios for the
| main transformer | and | the current | transformers. |     |     |
| ---------------- | --- | ----------- | ------------- | --- | --- |
2.10 If the B-H curve of the core steel of a transformer consists of a vertical line
when the core is unsaturated, and a line of some finite slope when the core
is saturated, the inrush current is made up of portions of a sinusoid that are
θ < θ < 2π.
| symmetric | around its | peak, and | have | a span of angle | where 0 |
| --------- | ---------- | --------- | ---- | --------------- | ------- |
Determine the harmonic content of such a waveform for a general θ. Confirm
that the second harmonic predominates, and that the harmonic magnitudes go
| to zero | as θ goes to 0 | or 2π. |     |     |     |
| ------- | -------------- | ------ | --- | --- | --- |
2.11 ForaB-Hcurvefor thecoresteel asdescribed inProblem2.10, determinethe
shape of magnetizing current as the transformer is overexcited. Assume that
over-excitation produces a symmetric flux excursion beyond the saturation
level by a factor k, where k is greater than 1. Determine the harmonic content
of the resulting magnetizing current, and show that fifth is the predominant
| harmonic | in this case. |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- |
2.12 Assume the primary voltage of the CVT shown in Figure 2.18 to be 400kV,
and the voltage produced by the capacitive potential divider to be 4kV.
Assume the capacitor C to be 0.1µF. Determine the value of the tuning
2
inductance. If theburden is200ohmsresistive, determinethe subsidence tran-
sient at the burden when the primary voltage collapses to zero at (a) peak of
the voltage wave, and (b) at the zero-crossing of the voltage wave.
References
[1] Mason, C. R. (1956) TheArtandScienceofProtectiveRelaying, John Wiley & Sons,
Ltd.
[2] AppliedProtectiveRelaying, Westinghouse Electric Corporation, 1982.
[3] Van C. Warrington, A. R. (1962, 1969) Protective Relays, Their Theory and Practice,
vol. I, Chapman and Hall, London and John Wiley & Sons Inc. New York, 1962;
vol. II, Chapman and Hall, London and John Wiley & Sons Inc. New York, 1969.
[4] PowerSystemProtection, vols. I, II, III. Edited by Electricity Council. The Institution
| of Electrical | Engineers. |     |     |     |     |
| ------------- | ---------- | --- | --- | --- | --- |
[5] Horowitz, S. H. and Phadke (2008) A.G. PowerSystemRelaying, Third edition, John
| Wiley & | Sons, Ltd. |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- |
[6] Horowitz, S. H. (ed.) (1980) Protective Relaying for Power Systems, IEEE Press,
New York.
[7] Stevenson, Jr., W. D. (1980) Elements of Power System Analysis, Chapter 13,
| McGraw-Hill, | New York. |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
[8] Lewis W. A. and Tippett, L. S. (1947) Fundamental basis for distance relaying on
| 3-phase | systems, AIEE | Transactions, | vol. | 66, pp. 694–708. |     |
| ------- | ------------- | ------------- | ---- | ---------------- | --- |
[9] Einvall,C.H.andLinders,J.R.(1975)Athree-phasedifferentialrelayfortransformer
| protection, | IEEE Trans. | on PAS, | vol. PAS-94, | no. 6. |     |
| ----------- | ----------- | ------- | ------------ | ------ | --- |

54 Relaying practices
[10] IEEE Publication no. 6 CH1130-PWR, Transient Response of Current Transformers,
1976.
[11] Sweetana,A.(1970)Transientresponsecharacteristicsofcapacitancepotentialdevices,
| IEEE Trans.onPAS, |     | Vol. PAS-89, | pp. 1989–1997. |
| ----------------- | --- | ------------ | -------------- |
[12] EmergingTechnologiesWorkingGroupandFiberOpticSensorsWorkingGroup,Opti-
cal current transducers for power systems: a review, IEEE Transactions on Power
| Delivery, | vol. 9, | no. 4, October | 1994, pp. 1778–1788. |
| --------- | ------- | -------------- | -------------------- |
[13] Kanoi M., Takahashi, G., Sato, T. et al. (1986) Optical voltage and current mea-
suring system for electric power systems, IEEE Transactions on Power Delivery,
| vol. PWRD-1, | no. | 1, pp. 91–97. |     |
| ------------ | --- | ------------- | --- |
[14] Ljubomir K. (2002) PCB Rogowski coils benefit relay protection, IEEE Computer
| Applications | in Power, | July | 2002. |
| ------------ | --------- | ---- | ----- |

3
Mathematical basis for protective
relaying algorithms
3.1 Introduction
One of the attractions of the computer relaying area is the rich combination of aca-
demic disciplines upon which it is based. In addition to protective relaying itself,
computer relaying depends on computer engineering for an understanding of hard-
wareselectionandcompromises,oncommunicationsystemsforanunderstandingof
the links between devices, and on elements of digital signal processing and estima-
tion theory in understanding the algorithms. To understand a number of algorithms
it is necessary to understand how the Fourier series and Fourier transform are used
to extract the fundamental frequency component of voltage and current waveforms.
The first few sections of this chapter are devoted to a brief presentation of Fourier
series and transform ideas along with a related expansion of a signal in terms of
Walsh functions. Another important concept in evaluating relay algorithms is that
of estimation. Since unwanted components are generally present in the signals that
are sampled, it is necessary to estimate the parameters of interest (the fundamen-
tal frequency component, for example) by processing a number of samples. The
remaining material in this chapter is concerned with ideas of probability, random
processes, and estimation including the Kalman filter. Our treatment of all of these
subjects is, of necessity, brief. The interested reader is referred to more complete
books on these subjects given as references at the end of the chapter.
3.2 Fourier series
Manyoftheinputsignalssuchasphasevoltagesandcurrentsencounteredinpower
systems are essentially periodic. Ideally the voltages and currents present in the
system in steady state are pure sinusoids at the power system frequency (50 or
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

| 56  |     |     |     | Mathematical | basis for protective | relaying algorithms |     |
| --- | --- | --- | --- | ------------ | -------------------- | ------------------- | --- |
60Hz). Some devices (for example, power transformers, inverters, converters and
loads) create harmonic distortion in the steady state signals. The signals seen by
protective relays also fail to be pure sinusoids. The non-fundamental frequency
content of the voltage and current seen by a relay are not truly periodic but change
in time. The nature of these non-fundamental frequency signals has an important
bearing on the performance of relaying algorithms. The Fourier series provides a
technique for examining these signals and determining their harmonic content.
A signal r(t) is said to be periodic if there is a T such that
|     |     |     | r(t) = | r(t+T); | for all t |     | (3.1) |
| --- | --- | --- | ------ | ------- | --------- | --- | ----- |
If r(t) is periodic and not a constant then let T be the smallest positive value of
0
T for which Equation (3.1) is satisfied. The period T is called the fundamental
0
period of r(t). The need for a concern with the smallest such T is made clear by
considering a sinusoid. If r(t) = sin(ω t) then Equation (3.1) is satisfied for
0
2nπ
1,2,3,...
|     |     | T   | =   | ; n | =   |     | (3.2) |
| --- | --- | --- | --- | --- | --- | --- | ----- |
ω
0
2π/ω
The smallest positive value is, of course, T = . Associated with the funda-
0
| mental period | is a fundamental |     | frequency |     | defined by |     |     |
| ------------- | ---------------- | --- | --------- | --- | ---------- | --- | --- |
2π
|     |     |     |     | ω = |     |     | (3.3) |
| --- | --- | --- | --- | --- | --- | --- | ----- |
0
T
0
| Example | 3.1 |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
If
|               |                |     |     | r(t)=     | ejω 0t  |     |     |
| ------------- | -------------- | --- | --- | --------- | ------- | --- | --- |
| then Equation | (3.1) requires |     |     |           |         |     |     |
|               |                |     |     | ejω (t+T) | =ejω 0t |     |     |
0
|     |     |     | ejω 0t(cid:7)ejω | 0T−1(cid:8)=0;for |     |     |     |
| --- | --- | --- | ---------------- | ----------------- | --- | --- | --- |
all t
|     | ω   | 2nπ; |     |     | ... |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
which implies that 0 T = n = 1, 2, 3, The conclusion is that the funda-
mental period is T = 2π/ω , and the fundamental frequency is ω .
|         | 0   |     | 0   |     |     | 0   |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
| Example | 3.2 |     |     |     |     |     |     |
The real and imaginary parts of Example 3.1, viz. cos(ω t) and sin(ω t), have
|             |          |        |     |                 |           | 0   | 0   |
| ----------- | -------- | ------ | --- | --------------- | --------- | --- | --- |
| fundamental | period T | = 2π/ω |     | and fundamental | frequency | ω . |     |
|             |          | 0      | 0   |                 |           | 0   |     |

| Fourier series |     |     |     |     |     |     | 57  |
| -------------- | --- | --- | --- | --- | --- | --- | --- |
| Example        | 3.3 |     |     |     |     |     |     |
The periodic square wave shown in Figure 3.1 (the dots indicate the signal is
|     |     |     |     |     |     | ω 2π/T |     |
| --- | --- | --- | --- | --- | --- | ------ | --- |
periodic) has fundamental period T and fundamental frequency = .
|     |     |     | 0   |     |     | 0   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- |
r(t)
••••
|     |     | −T     | /2 T | /2 T            | 2T   | t   |     |
| --- | --- | ------ | ---- | --------------- | ---- | --- | --- |
|     |     | 0      |      | 0 0             | 0    |     |     |
|     |     | Figure | 3.1  | Periodic square | wave |     |     |
If r 1 (t) and r 2 (t) are both periodic signals with fundamental periods T 0 and T 1 ,
respectively, then the sum, r (t)+r (t), is not necessarily periodic. Consider
|     |     |     | 1 2    |                 |     |     |     |
| --- | --- | --- | ------ | --------------- | --- | --- | --- |
|     |     |     | r(t) = | sin(t)+sin(πt). |     |     |     |
The fundamental period of sin(t) is 2π while the fundamental period of sin(πt)
|     |     |     |     |     |     | 2πn | π   |
| --- | --- | --- | --- | --- | --- | --- | --- |
is 2. It is not possible to find integers n and m such that 2m = since is
irrational (not the ratio of integers) so that there is no T that satisfies Equation
| (3.1). On | the other | hand if |        |             |     |     |     |
| --------- | --------- | ------- | ------ | ----------- | --- | --- | --- |
|           |           |         | r(t) = | ejω 0t+e2jω | 0t  |     |     |
then the two fundamental periods differ only by a factor of two, i.e. 2π/ω and
0
| π/ω |     |     |     |     |     | 2π/ω |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
. Thus the fundamental period of the sum is the larger, . In fact it is
| 0       |              |            |          |                |          | 0       |     |
| ------- | ------------ | ---------- | -------- | -------------- | -------- | ------- | --- |
| easy to | see that any | finite sum | of the   | form           |          |         |     |
|         | r(t)         | = c +c     | ejω 0t+c | e2jω 0t+c e3jω | 0t+···+c | ejNω 0t |     |
|         |              | 0 1        | 2        | 3              |          | N       |     |
is periodic with fundamental frequency ω . Including both positive and negative
0
| terms in | the sum, |     |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- |
k(cid:5)=N
|     |     |     | r(t)= | c ejkω | 0t  |     | (3.4) |
| --- | --- | --- | ----- | ------ | --- | --- | ----- |
k
k=−N
is also a periodic signal with fundamental frequency ω . The objective of Fourier
0
analysis is to decompose an arbitrary periodic signal into components as in
| Equation | (3.4). |     |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- | --- |

| 58                |         | Mathematical |     | basis for | protective relaying algorithms |     |
| ----------------- | ------- | ------------ | --- | --------- | ------------------------------ | --- |
| 3.2.1 Exponential | fourier | series       |     |           |                                |     |
ω
Given a periodic signal with fundamental frequency the exponential Fourier
0
| series is written as1 |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- |
k(cid:5)=∞
|     |     | r(t)= |     | ejkω 0t |     |       |
| --- | --- | ----- | --- | ------- | --- | ----- |
|     |     |       | c   | k       |     | (3.5) |
k=−∞
The task at hand is to determine the coefficients c k . An important property of the
exponentials makes the calculation a simple process. Note that
(cid:6)
(cid:4)T0
|     |     |       |     | ; =        |     |       |
| --- | --- | ----- | --- | ---------- | --- | ----- |
|     |     | ejmω  | T   | 0 m        | 0   |       |
|     |     | 0t dt | =   |            |     | (3.6) |
|     |     |       | 0;  | m (cid:6)= | 0   |       |
0
The value of the integral is clear for m = 0, while for m (cid:6)= 0
(cid:4)T0
|     |     |     |     | (cid:7) (cid:8)T0 |     |     |
| --- | --- | --- | --- | ----------------- | --- | --- |
1
|     | ejmω | 0t dt = |     | ejmω 0t | = 0 |     |
| --- | ---- | ------- | --- | ------- | --- | --- |
jmω
|     |     |     | 0   | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
0
since ω T = 2π. Equation (3.6) is also true for integration over any period, i.e.
0 0
|     |     |     | τ τ+T |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- |
the integrand could have been from to . To compute the Fourier series
0
coefficients it is only necessary to multiply Equation (3.5) by e−jnω 0t and integrate
over a period:
|     | (cid:4)T0 |     | (cid:4)T0 |     |     |     |
| --- | --------- | --- | --------- | --- | --- | --- |
K(cid:5)=∞
|     | r(t)e−jnω | 0t dt | =   | c ej(k−n)ω | 0tdt | (3.7) |
| --- | --------- | ----- | --- | ---------- | ---- | ----- |
k
|     | 0   |     | 0 K=−∞ |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- |
From Equation (3.6) every term on the right hand side vanishes except the nth,
yielding
(cid:4)T0
|     |     | r(t)e−jnω | 0tdt | = T c |     | (3.8) |
| --- | --- | --------- | ---- | ----- | --- | ----- |
|     |     |           |      | 0 n   |     |       |
0
or
(cid:4)T0
1
|     |     | c = | r(t)ejnω | 0tdt |     | (3.9) |
| --- | --- | --- | -------- | ---- | --- | ----- |
n
T
0
0
Equation(3.9)canbeevaluatedover anyperiodthatisconvenient aswillbeseen
in example to follow.

Fourier series 59
| Example | 3.4 |     |     |
| ------- | --- | --- | --- |
Consider the square wave of Figure 3.1. The nth coefficient is given by
|     |     | T(cid:4) /2 | (cid:2) (cid:3) |
| --- | --- | ----------- | --------------- |
0 T0 /2
|     |     | 1   | e−jnω 0t |
| --- | --- | --- | -------- |
e−jnω 0tdt
|     |     | c = | =      |
| --- | --- | --- | ------ |
|     |     | n T | −jnω T |
0 0 0 0
0
|     |     | (cid:2)        | (cid:3) |
| --- | --- | -------------- | ------- |
|     |     | e−jnω 0T0 /2−1 |         |
=
|     |     | −jnω T |     |
| --- | --- | ------ | --- |
0 0
|     |     | (cid:2) | (cid:3) |
| --- | --- | ------- | ------- |
|     |     | e−jnπ−1 | (−1)n−1 |
|     |     | =       | =       |
|     |     | −jn2π   | −j2nπ   |
1
c = ;n odd
n jnπ
|     |     | c =0; n even,n | (cid:6)= 0 |
| --- | --- | -------------- | ---------- |
n
=1/2
c
0
The coefficient c (the average value of the signal) must frequently be evaluated
0
| separately. | The approximations | formed | by the finite sum |
| ----------- | ------------------ | ------ | ----------------- |
k(cid:5)=N
|     |     | r(t) = | ejkω 0t |
| --- | --- | ------ | ------- |
c k
k=−N
| for N = | 1, 3, and 5 | are shown in Figure | 3.2. |
| ------- | ----------- | ------------------- | ---- |
r(t)
T
0
t
Figure 3.2 Finite Fourier series approximations to the square wave

| 60      |          |        |       |          | Mathematical |     | basis for | protective | relaying | algorithms |
| ------- | -------- | ------ | ----- | -------- | ------------ | --- | --------- | ---------- | -------- | ---------- |
| 3.2.2   | Sine and | cosine |       | fourier  | series       |     |           |            |          |            |
| Through | the use  | of the | Euler | identity |              |     |           |            |          |            |
ejkω
|     |     |     |     | ot = | cos(kω | t)+jsin(kω |     | t)  |     | (3.10) |
| --- | --- | --- | --- | ---- | ------ | ---------- | --- | --- | --- | ------ |
|     |     |     |     |      |        | o          |     | o   |     |        |
it is possible to write the exponential series given in Equation (3.4) in terms of
| sines and | cosines  |     |         |       |          |        |          |          |     |        |
| --------- | -------- | --- | ------- | ----- | -------- | ------ | -------- | -------- | --- | ------ |
|           | (cid:5)∞ |     |         |       | (cid:5)∞ |        | (cid:5)∞ |          |     |        |
|           |          | c   | ejkω ot | = a + | a        | cos(kω | t)+      | b sin(kω | t)  | (3.11) |
|           |          | k   |         | o     | k        |        | o        | k        | o   |        |
|           | k=−∞     |     |         |       | k=1      |        | k=1      |          |     |        |
where
a =c
|           |          |        |     | o      | o   |            |            |     |     |        |
| --------- | -------- | ------ | --- | ------ | --- | ---------- | ---------- | --- | --- | ------ |
|           |          |        |     | a =c   | +c  | k (cid:6)= | 0          |     |     | (3.12) |
|           |          |        |     | k      | k   | −k         |            |     |     |        |
|           |          |        |     | b =j(c | −c  | )k         | (cid:6)= 0 |     |     | (3.13) |
|           |          |        |     | k      | k   | −k         |            |     |     |        |
| Or, using | Equation | (3.9), |     |        |     |            |            |     |     |        |
(cid:4)To
2
|     |     |     |     | a = | r(t)cos(kω |     | t)dt |     |     | (3.14) |
| --- | --- | --- | --- | --- | ---------- | --- | ---- | --- | --- | ------ |
|     |     |     |     | k   |            |     | o    |     |     |        |
|     |     |     |     |     | T o        |     |      |     |     |        |
0
(cid:4)To
2
|     |     |     |     |     | r(t)sin(kω |     | t)dt |     |     |        |
| --- | --- | --- | --- | --- | ---------- | --- | ---- | --- | --- | ------ |
|     |     |     |     | b = |            |     |      |     |     | (3.15) |
|     |     |     |     | k   | T          |     | o    |     |     |        |
o
o
From the results of Problem 3.2, it follows that real and even signals have expan-
sions of the form of Equation (3.11) with only cosine terms, while real and odd
| signals | have such | expansions |     | with | only | sine terms. |     |     |     |     |
| ------- | --------- | ---------- | --- | ---- | ---- | ----------- | --- | --- | --- | --- |
Equations (3.12) and (3.13) result from expanding the kth and −kth terms of the
| exponential    | series | using      | the        | Euler    | expansion |         |           |       |             |     |
| -------------- | ------ | ---------- | ---------- | -------- | --------- | ------- | --------- | ----- | ----------- | --- |
|                | e−jkω  |            |            |          | ejkω      |         |           |       |             |     |
|                | c      | ot+.....+c |            |          | ot =c     | cos(ω   | t)+c      | cos(ω | t)          |     |
|                | −k     |            |            | k        |           | −k      | o         | k     | o           |     |
|                |        |            |            |          |           |         | jsin(ω    | t)+c  | jsinω       |     |
|                |        |            |            |          |           | −c      |           |       | t           |     |
|                |        |            |            |          |           |         | −k        | o     | k o         |     |
| If the Fourier | series |            | is written | as       |           |         |           |       |             |     |
|                | r(t)=c |            | +(c        | ejω ot+c | e−jω      | ot) +(c | e2jω ot+c |       | e2jω ot)... |     |
|                |        | o          | 1          |          | −1        |         | 2         | −2    |             |     |
|                |        |            | +(c ejkω   | ot+c     | e−jkω     | ot)+... |           |       |             |     |
|                |        |            | k          |          | −k        |         |           |       |             |     |

| Fourier     | series |       |        |            |        |           |     |          |        | 61  |
| ----------- | ------ | ----- | ------ | ---------- | ------ | --------- | --- | -------- | ------ | --- |
| the various |        | terms | can be | recognized | as     |           |     |          |        |     |
|             | c      |       |        |            | the dc | component |     | (average | value) |     |
o
|     | (c  | ejω ot+c | e−jω | ot) |                 |     |           |     |           |     |
| --- | --- | -------- | ---- | --- | --------------- | --- | --------- | --- | --------- | --- |
|     |     |          | −1   |     | the fundamental |     | frequency |     | component |     |
1
|     | (c  | ejkω ot+c |     | e−jkω ot) | the kth | harmonic |     |     |     |     |
| --- | --- | --------- | --- | --------- | ------- | -------- | --- | --- | --- | --- |
|     |     | k         | −k  |           |         |          |     |     |     |     |
It is possible to think of the Fourier series expansion as the resolution of a peri-
odic function into its frequency components. The frequencies present in a periodic
function with fundamental frequency ω are: 0(DC),±ω (the first harmonic), 2ω
|     |     |     |     |     |     | o   |     | o   |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
±3ω
(the second harmonic), o (the third harmonic), etc. The coefficient c k then rep-
resents the amount of the signal at the frequency kω . The interpretation of the
o
Fourier series coefficientsas the frequency content of the signal can be summarized
by plotting the magnitudes of the coefficients versus frequency.
| Example | 3.5 |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The half-wave rectified sinusoid shown in Figure 3.3 represents a first approxima-
tion to a current waveform encountered in power transformers under a condition
of magnetizing inrush. The fundamental frequency is ω and the Fourier series
o
| coefficients |     | are given | by  |     | (cid:4) |           |      |     |     |     |
| ------------ | --- | --------- | --- | --- | ------- | --------- | ---- | --- | --- | --- |
|              |     |           |     |     | 1       | To        |      |     |     |     |
|              |     |           |     |     |         | r(t)e−jkω | otdt |     |     |     |
|              |     |           |     | c k | =       |           |      |     |     |     |
T
|     |     |     |     |     | o 0 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r(t)
A
•••
|     |     |     |     |     | π   | 2π  |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | ω   | ω   |     |     |     |     |
|     |     |     |     |     | 0   | 0   |     |     |     |     |
Figure 3.3 Half-wave rectified sine. An approximation to an inrush current
The coefficient c is found to be A/4j while all other odd c are zero and
|     |     |     | 1   |     |     |     |     |     | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A
|       |       |       |           | c   | =           | :         | k even |        |         |     |
| ----- | ----- | ----- | --------- | --- | ----------- | --------- | ------ | ------ | ------- | --- |
|       |       |       |           | k   | π(1−k2)     |           |        |        |         |     |
| Hence | the   | first | few terms | of  | the Fourier | expansion |        | are    |         |     |
|       |       | A     | A         |     | 2A          |           |        | 2A     |         |     |
|       | r(t)= |       | + sin(ω   | t)− |             | cos(2ω    | t)−    | cos(4ω | t)+.... |     |
|       |       | π     |           | o   | 3π          | o         | 15π    |        | o       |     |
2

| 62  |     |     |     | Mathematical |     | basis for protective | relaying | algorithms |
| --- | --- | --- | --- | ------------ | --- | -------------------- | -------- | ---------- |
3.2.3 Phasors
ω
Given a periodic signal with fundamental frequency o , we can compute a fun-
damental frequency phasor from the fundamental term in the Fourier series. If
we adopt the notation that a cosine waveform is the reference signal, that is, the
voltage
√
|     |     |     | v(t) | = 2Vcos(ω |     | t)  |     |     |
| --- | --- | --- | ---- | --------- | --- | --- | --- | --- |
o
| corresponds | to a phasor | V which |     | has angle | 0,  | and the voltage |     |     |
| ----------- | ----------- | ------- | --- | --------- | --- | --------------- | --- | --- |
√
|     |     |     | v(t) = | 2Vcos(ω |     | t+ϕ) |     |     |
| --- | --- | --- | ------ | ------- | --- | ---- | --- | --- |
o
corresponds to a complex phasor, Vejφ , then the fundamental frequency phasor is
directly related to the first exponential Fourier series coefficient:
√ (cid:4)
To
|     |     | Vejϕ |     | 2   | v(t)e−jω |      |     |        |
| --- | --- | ---- | --- | --- | -------- | ---- | --- | ------ |
|     |     |      | =   |     |          | otdt |     | (3.16) |
T
o 0
√
The 2inEquation(3.16)isduetotheconventionthatthemagnitudeofaphasor
is the root-mean-square (rms) value of a sinusoid but can be omitted if a ratio of
voltage and current phasors (an impedance calculation) is to be computed.
| 3.3 Other | orthogonal |     | expansions |     |     |     |     |     |
| --------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- |
The property of the exponentials that made it easy to compute the Fourier series
| coefficients, | viz. |     |     |     |     |     |     |     |
| ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
(cid:4)To
ej(k−m)ω
|     |     |     |     | ot  | dt = 0;k | (cid:6)= m |     | (3.17) |
| --- | --- | --- | --- | --- | -------- | ---------- | --- | ------ |
o
|                   |         |      |                 |     | {ejnω | ot}n 0,±1,±2,... |     |            |
| ----------------- | ------- | ---- | --------------- | --- | ----- | ---------------- | --- | ---------- |
| is a reflectionof | thefact | that | theexponentials |     |       | =                |     | areorthog- |
onaloveraperiod2π/ω .Thereareotherorthogonalperiodicfunctionswhichhave
o
beenappliedindigitalrelaying.Afamilyofcomplexsignals{ϕ (t),n = 1,2,3,...}
n
| are said | to be orthogonal | over | the | interval | 0 ≤ | t ≤ T if |     |     |
| -------- | ---------------- | ---- | --- | -------- | --- | -------- | --- | --- |
(cid:4)T
|     |     |     | ϕ (t)ϕ | ∗ (t)dt | =   | 0;m (cid:6)= n |     | (3.18) |
| --- | --- | --- | ------ | ------- | --- | -------------- | --- | ------ |
|     |     |     | n      | m       |     |                |     |        |
0
If thesignalsarerealthen thecomplex conjugate isunnecessary inEquation(3.18).
The negative sign on m in the exponent of Equation (3.17) is due to the required
conjugate.

| Fourier transforms |                 |     |     | 63  |
| ------------------ | --------------- | --- | --- | --- |
| 3.3.1              | Walsh functions |     |     |     |
The Walsh functions are a set of orthogonal signals on the interval [0,1] which
only take on the values ±1. As such, they seemed appealing for digital implemen-
tation since multiplication by a Walsh function involves only algebraic operations.
Progress in computer hardware has essentially eliminated the need for Walsh func-
tions.
φ =
An expansion of a function f(t) in an arbitrary orthogonal set n (t), n 1, 2,
3,... can be thought of as that of finding coefficients such that
(cid:5)N
|     |     | f(t) = | c ϕ (t) | (3.19) |
| --- | --- | ------ | ------- | ------ |
n n
n=1
Equation (3.19) is only symbolic since the finite summation will not actually equal
f(t) except in exceptional circumstances. However, if Equation (3.19) is multiplied
on both sides by ϕ ∗ (t) and integrated from 0 to T, the orthogonality of the φ
|        | m   |         |     | n   |
| ------ | --- | ------- | --- | --- |
| yields |     | (cid:9) |     |     |
Tϕ ∗ (t)f(t)dt
m
|     |     | c = 0      |     | (3.20) |
| --- | --- | ---------- | --- | ------ |
|     |     | m (cid:9)T |     |        |
ϕ ∗ (t)ϕ (t)dt
m m
0
Equation (3.20) is a generalization of Equation (3.9) for signals other than expo-
nentials. For exponentials the denominator of Equation (3.20) equals T and
o
|     |     | ϕ ∗ (t)= | e−jmω ot |     |
| --- | --- | -------- | -------- | --- |
m
| 3.4 Fourier | transforms |     |     |     |
| ----------- | ---------- | --- | --- | --- |
The technique of representing a signal as a sum of exponentials can be extended
to non-periodic functions through the use of Fourier transforms.2 The transform
pair can be obtained by writing a Fourier series and taking the limit as the period
becomes infinite.3,4 Consider a time limited signal as shown in Figure 3.4, i.e.
|     |     | x(t) = | 0;|t| (cid:12) T |     |
| --- | --- | ------ | ---------------- | --- |
1
| We select | a period T | (cid:13) T and let |     |     |
| --------- | ---------- | ------------------ | --- | --- |
|           | o          | 1                  |     |     |
(cid:5)∞
|     |     | r(t)= | x(t−nT ) | (3.21) |
| --- | --- | ----- | -------- | ------ |
o
n=−∞
toformaperiodicfunctionmadeupofshiftedreplicasofx(t)asshowninFigure3.5.

64 Mathematical basis for protective relaying algorithms
x(t)
−T T t
1 1
Figure 3.4 A time limited function
r(t)
−T − T −T −T + T1 −T 0 T T − T T T + T1 t
0 1 0 0 1 1 0 1 0 0
Figure 3.5 Shifted replicas of x(t)
It can be seen that r(t) is periodic, with fundamental period T and fundamental
0
frequency ω = 2π/T . The Fourier series coefficients are given by
o o
(cid:4)
1 To /2
c = r(t)e−jkω otdt
k
T o −To /2
(cid:4)
1 To /2
c = x(t)e−jkω otdt
k
T o −To /2
As T approaches infinity, r(t) limits to x(t), and r(t) can be written
o
(cid:5)∞
r(t)= c ejkω ot
k
k=−∞
(cid:2) (cid:4) (cid:3)
(cid:5)∞ 1 To /2
r(t)= x(t)e−jkω otdt ejkω ot
k=−∞
T o −To /2
since
1 ω
o
=
T 2π
o
(cid:2)(cid:4) (cid:3)
1 (cid:5)∞ To /2
r(t)= x(t)e−jkω otdt ω ejkω ot
2π
k=−∞
−To /2
o

| Fourier transforms |             |               |              |     | 65  |
| ------------------ | ----------- | ------------- | ------------ | --- | --- |
| If T o is taken    | to infinity | in such a way | that         |     |     |
|                    |             | ω             | → dω,kω → ω, |     |     |
|                    |             | o             | o            |     |     |
|                    |             | limr(t)       | = x(t),      |     |     |
T →∞
| (cid:10)∞ | (cid:9) | o   |     |     |     |
| --------- | ------- | --- | --- | --- | --- |
∞
| and → |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- |
−∞
k=∞
|      |       |         | (cid:2)(cid:4) | (cid:3) |     |
| ---- | ----- | ------- | -------------- | ------- | --- |
| then |       | (cid:4) |                |         |     |
|      |       | 1       | ∞ ∞            |         |     |
|      | x(t)= |         | x(t)e−jωtdt    | ejωtdω  |     |
(3.22)
2π
|     |     | −∞  | −∞  |     |     |
| --- | --- | --- | --- | --- | --- |
(cid:4)
∞
|     |       | 1   | ∧ (ω)ejωwtdω |     |        |
| --- | ----- | --- | ------------ | --- | ------ |
|     | x(t)= |     | X            |     | (3.23) |
2π
−∞
(cid:4)
|     | ∧    | ∞           |     |     |        |
| --- | ---- | ----------- | --- | --- | ------ |
|     | (ω)= | x(t)e−jωtdt |     |     |        |
|     | FX   |             |     |     | (3.24) |
−∞
(cid:4)
1 ∧
|     | F−1x(t)= |     | (ω)ejωtdω |     |        |
| --- | -------- | --- | --------- | --- | ------ |
|     |          |     | X         |     | (3.25) |
2π
Equations (3.24) and (3.25) represent the Fourier transform pair. The connection
∧
between the two functions x(t) and X (ω) in Equations (3.24) and (3.25) is shown
| symbolically | as  |       |         |     |        |
| ------------ | --- | ----- | ------- | --- | ------ |
|              |     | x(t)↔ | I ∧ (ω) |     |        |
|              |     |       | X       |     | (3.26) |
|              | ∧   |       | ∧       |     |        |
Given an x(t) and X (ω), we say x(t) and X (ω) are a Fourier transform pair when
F−1
either or both of F (Equation (3.24)) and (Equation (3.25)) hold.
| Example                | 3.6 |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- |
| If x(t) = e−αtu(t);α>0 |     |     |     |     |     |
(cid:4)
∞
∧
|     |     | (ω)= | x(t)ejωtdt |     |     |
| --- | --- | ---- | ---------- | --- | --- |
X
(cid:4) −∞
|     |     | ∞   |     | 1   |     |
| --- | --- | --- | --- | --- | --- |
e−(α+jω)tdt
|     |     | =   | =   |     |     |
| --- | --- | --- | --- | --- | --- |
α+jω
−∞
| and from | the inversion | integral |     |     |     |
| -------- | ------------- | -------- | --- | --- | --- |
(cid:4)
|     |     |        | 1 ∞ ejωt |     |     |
| --- | --- | ------ | -------- | --- | --- |
|     |     | x(t) = | dω       |     |     |
|     |     |        | 2π α+jω  |     |     |
−∞

| 66      |             |      |       | Mathematical |           | basis for protective | relaying | algorithms |
| ------- | ----------- | ---- | ----- | ------------ | --------- | -------------------- | -------- | ---------- |
| Example | 3.7         |      |       |              |           |                      |          |            |
|         | αtu(t); α>0 |      | ∧ (ω) |              |           |                      |          |            |
| If x(t) | = e         | then | X     | does         | not exist | because x(t)         | → ∞ as   | t → ∞.     |
It is clear that, since the factor e−jωt in the integrand of Equation (3.24) does not
contribute to the convergence of the integral, it is necessary that x(t) at least remain
F−1
| bounded    | as t → ∞        | in order | for       | F &  | to be | defined. |     |     |
| ---------- | --------------- | -------- | --------- | ---- | ----- | -------- | --- | --- |
| Example    | 3.8             |          |           |      |       |          |     |     |
| If x(t) is | the pulse shown |          | in Figure | 3.6, | i.e.  |          |     |     |
|            |                 |          | x(t)=p    | (t)  |       |          |     |     |
(cid:4) a
(cid:11)
|     |     |     | ∧    | a   |         | e−jωt(cid:11) a |     |     |
| --- | --- | --- | ---- | --- | ------- | --------------- | --- | --- |
|     |     |     | (ω)= |     | e−jωtdt | (cid:11)        |     |     |
|     |     | X   |      |     | =       |                 |     |     |
−jω
|     |     |     |     | −a  |     | −a  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
2sin(ωa)
∧
X (ω)=
ω
P (t)
a
1.0
|          |             |           |        | −a           | 0           | a t     |     |     |
| -------- | ----------- | --------- | ------ | ------------ | ----------- | ------- | --- | --- |
|          |             |           | Figure | 3.6          | Rectangular | pulse   |     |     |
| In order | to plot the | transform | it     | is necessary | to          | examine |     |     |
2sin(ωa)
|     |     |     |     |     | ω   | =   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | at  | 0   |     |     |
ω
Using L’Hospital’s rule we evaluate the ratio of the derivatives at ω = 0 to
obtain
|     |     | 2sin(ωa) |     |        | 2acos(ωa) |           |     |     |
| --- | --- | -------- | --- | ------ | --------- | --------- | --- | --- |
|     |     |          |     | |ω=0 = |           | |ω=0 = 2a |     |     |
|     |     |          | ω   |        | 1         |           |     |     |
The transform 2sin (ωa) is plotted in Figure 3.7. Using the notation
sinπx
|     |     |     |     | sinc(x) | =   |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- |
πx

Fourier transforms 67
2a
^ (ω) = 2si nωa
x ω
|     |     |     | −π/a |     | π/a |     |
| --- | --- | --- | ---- | --- | --- | --- |
2π/a
|               | Figure | 3.7 The | Fourier | transform | of the rectangular | pulse |
| ------------- | ------ | ------- | ------- | --------- | ------------------ | ----- |
| the transform | can be | written | as      |           |                    |       |
∧
|     |     |     | (ω) | = 2asinc(aω/π) |     |     |
| --- | --- | --- | --- | -------------- | --- | --- |
X
Theexampleillustratesageneralrule.Ifx(t)istimelimited,theFouriertransform
∧ (ω)
will exist. As in the Fourier series case the transform X is the spectrum of x(t),
| i.e. the frequency | content. |     |     |     |     |     |
| ------------------ | -------- | --- | --- | --- | --- | --- |
| Example            | 3.9      |     |     |     |     |     |
∧
(ω) (ω)
Suppose X = pω as shown in Figure 3.8. If it is thought of as the transfer
0
function of a linear system then the filter would represent an ‘ideal low-pass filter’
sinceallfrequenciesbelowω
arepassedwithoutdistortionwhilefrequenciesabove
o
ω
o are perfectly attenuated. Using the inversion integral (Equation (3.25))
(cid:4)
|     |     |       |     | 1 ∞ ∧     |     |     |
| --- | --- | ----- | --- | --------- | --- | --- |
|     |     | x(t)= |     | (ω)ejωtdω |     |     |
X
2π
−∞
(cid:4)
ω
|     |     |     |     | 1 o ejωtdω |     |     |
| --- | --- | --- | --- | ---------- | --- | --- |
x(t)=
2π
−ω
|     |     |     |     | (cid:11) o |     |     |
| --- | --- | --- | --- | ---------- | --- | --- |
ω
|     |       |       |     | ejωt (cid:11) o   | 2sin(ω t) |     |
| --- | ----- | ----- | --- | ----------------- | --------- | --- |
|     |       |       |     | (cid:11)          | o         |     |
|     |       | x(t)= |     | (cid:11) =        |           |     |
|     |       |       |     | 2πjt              | 2πt       |     |
|     |       |       |     | −ω o              |           |     |
|     |       |       |     | (cid:12) (cid:13) |           |     |
|     | sin(ω | t)    | ω   | ω                 |           |     |
t
| that is, X(t) | =         | o =        | o sinc | o                     |      |     |
| ------------- | --------- | ---------- | ------ | --------------------- | ---- | --- |
|               | πt        |            | π      | π                     |      |     |
| as shown      | in Figure | 3.9. Again | if     | x(t) is band-limited, | i.e. |     |
∧
|          |                   |     | (ω)       | = |ω|         | (cid:12) ω , |     |
| -------- | ----------------- | --- | --------- | ------------- | ------------ | --- |
|          |                   |     | X         | 0 for         | o            |     |
| then the | inverse transform |     | x(t) will | always exist. |              |     |

| 68  |     |     |     | Mathematical |     | basis | for protective | relaying algorithms |
| --- | --- | --- | --- | ------------ | --- | ----- | -------------- | ------------------- |
Pω(ω)
0
1.0
|     |        |     |     | −ω       |          | ω      | ω              |        |
| --- | ------ | --- | --- | -------- | -------- | ------ | -------------- | ------ |
|     |        |     |     | 0        | 0        | 0      |                |        |
|     | Figure | 3.8 | The | transfer | function | of the | ideal low-pass | filter |
ω
|     |     |     |     | sinωt |     | π0  |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
x(t) =
πt
|     |     |     |     |     |     | π   | 2π  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | ω   | ω   | t   |
|     |     |     |     |     |     | 0   | 0   |     |
Figure 3.9 The inverse transform of the ideal low-pass filter shown in Figure 3.8
| Example   | 3.10      |          |            |     |        |         |       |     |
| --------- | --------- | -------- | ---------- | --- | ------ | ------- | ----- | --- |
| If x(t) = | δ(t), the | defining | properties |     | of the | impulse | yield |     |
(cid:4)
∞
|     |     |     | ∧   |       | δ(t)e−jωt |     |     |     |
| --- | --- | --- | --- | ----- | --------- | --- | --- | --- |
|     |     |     | X   | (ω) = |           |     | = 1 |     |
−∞
or
∧
|     |     |     | x(t) |     | δ(t)↔ I |       | (ω) |     |
| --- | --- | --- | ---- | --- | ------- | ----- | --- | --- |
|     |     |     |      | =   |         | 1 = X |     |     |
Theinversioninthispaironlymakessenseinsomegeneralizedcontextbutnonethe-
| less is a transform |      | pair | according | to  | our agreements. |     |     |     |
| ------------------- | ---- | ---- | --------- | --- | --------------- | --- | --- | --- |
| Example             | 3.11 |      |           |     |                 |     |     |     |
∧
| Similarly, | if (ω) | =   | δ(ω)2π |     |     |     |     |     |
| ---------- | ------ | --- | ------ | --- | --- | --- | --- | --- |
X
(cid:4)
1 ∞
|     |     |     | F−1x(t) | =   | 2πδ(ω)ejωtdt |     | =   |     |
| --- | --- | --- | ------- | --- | ------------ | --- | --- | --- |
1
2π
−∞

| Fourier | transforms |     |     |     |     |     |     | 69  |
| ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
and
|     |     |     |      |      | F      | ∧     |     |     |
| --- | --- | --- | ---- | ---- | ------ | ----- | --- | --- |
|     |     |     | x(t) | = 1↔ | 2πδ(ω) | = (ω) |     |     |
X
Wecanconcludefromthelastfourpairsoftransformsthatsharpornarrowsignals
inonedomain(torω)implybroadorspread-outsignalsintheotherdomain.Sharp
edges in time require broad frequency spectra. The examples can also provide a
practical view of the impulse. If we normalize Example 3.9 by 2a we obtain
2sin(ωa)
F
|     |     |     |     | P (t)/2a↔ |     |     |     | (3.27) |
| --- | --- | --- | --- | --------- | --- | --- | --- | ------ |
|     |     |     |     | a         |     | 2aω |     |        |
The time function in Equation (3.37) has unit area being 2a wide and 1/2a tall,
whilethefunction offrequency hasaheight at ω = 0of1.Ifais10−9 sec(roughly
2×10−9
the time it takes light to travel a foot) then the pulse has a duration of
sec and the transform is as shown in Figure 3.8 with the first zero at ω = π×109
radians or a frequency of 500M Hz. Practically speaking, the impulse may be
regarded as an extremely narrow pulse with unit area (the limit of Equation (3.27)
| as ‘a’     | goes | to zero.)       |     |            |     |     |     |     |
| ---------- | ---- | --------------- | --- | ---------- | --- | --- | --- | --- |
| Example    | 3.12 |                 |     |            |     |     |     |     |
| If Example |      | 3.10 is shifted | in  | frequency, |     |     |     |     |
∧
|     |     | (ω) | 2πδ(ω−ω |     | )   |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- |
|     |     | X   | =       |     | o   |     |     |     |
(cid:4)
∞
1
|     |     | x(t) | =   |     | 2πδ(ω−ω | )ejωtdω = | ejω ot |     |
| --- | --- | ---- | --- | --- | ------- | --------- | ------ | --- |
o
2π
−∞
|     |     | ejω ot | ↔ F 2πδ(ω−ω |     | )   |     |     |     |
| --- | --- | ------ | ----------- | --- | --- | --- | --- | --- |
o
| 3.4.1 | Properties | of  | fourier | transforms |     |     |     |     |
| ----- | ---------- | --- | ------- | ---------- | --- | --- | --- | --- |
There are a number of properties of Fourier transforms which are useful in under-
standing the resolution of a signal into its frequency spectrum.
|     |            |           | F ∧ |     |     |     |     |     |
| --- | ---------- | --------- | --- | --- | --- | --- | --- | --- |
| P1) | Linearity: | If x (t)↔ | X   | (ω) |     |     |     |     |
|     |            | 1         | 1   |     |     |     |     |     |
F ∧
| And  | x (t)↔    | X (ω)  |     |       |       |     |     |        |
| ---- | --------- | ------ | --- | ----- | ----- | --- | --- | ------ |
|      | 2         | 2      |     |       |       |     |     |        |
|      |           |        | F   | ∧     | ∧     |     |     |        |
| then | c x (t)+c | x (t)↔ | c X | (ω)+c | X (ω) |     |     | (3.28) |
|      | 1 1       | 2 2    | 1   | 1     | 2 2   |     |     |        |

| 70  |     |     |     | Mathematical |     | basis | for protective | relaying | algorithms |
| --- | --- | --- | --- | ------------ | --- | ----- | -------------- | -------- | ---------- |
It should be observed that Equation (3.28) may involve combining one pair where
F does not actually exist with a second pair where F−1 does not actually exist.
∧
| P2)   |       | x(t)↔ | F   | (ω) |     |     |     |     |     |
| ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Delay | Rule: | If    |     | X   |     |     |     |     |     |
∧
| x(t−t    | )↔ F       | (ω)ejωt1    |     |               |         |               |     |     |        |
| -------- | ---------- | ----------- | --- | ------------- | ------- | ------------- | --- | --- | ------ |
| then     | 1          | X           |     |               |         |               |     |     | (3.29) |
| Equation | (3.29) can | be verified |     | by evaluating |         |               |     |     |        |
|          |            | (cid:4)     |     |               | (cid:4) |               |     |     |        |
|          |            | ∞           |     |               |         | ∞             |     |     |        |
|          |            | x(t−t       |     | )ejωtdt       |         | x(τ)e−jω(τ+t1 | )   | dτ  |        |
|          |            |             |     | 1             | =       |               |     |     |        |
|          |            | −∞          |     |               | −∞      |               |     |     |        |
τ
| letting | = t−t |     | (cid:4) |     |     |     |     |     |     |
| ------- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
|         |       | 1   |         | ∞   |     |     |     |     |     |
∧
|     |     | =e−jωt1 |     | x(τ)e−jωτ |     | dr = | (ω)e−jωt1 |     |     |
| --- | --- | ------- | --- | --------- | --- | ---- | --------- | --- | --- |
X
−∞
| Example | 3.13 |     |     |     |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
If
2sin(ωa)
∧
|     |     |     | x(t) = | P (t), | X (ω) | =   |     |     |     |
| --- | --- | --- | ------ | ------ | ----- | --- | --- | --- | --- |
|     |     |     |        | a      |       | ω   |     |     |     |
then
2sin(ωa)
∧
|     |     | y(t) | = P (t−t | ),  | (ω) | = ejωt1 |     |     |     |
| --- | --- | ---- | -------- | --- | --- | ------- | --- | --- | --- |
|     |     |      | a        | 1   | Y   |         | ω   |     |     |
∧
If the transform is written X (ω) = |Xˆ(ω)|ejθ(ω) where |Xˆ(ω)| is the magnitude, and
∧
| θ(ω) |     |     |     |     |     |     | (ω) | Yˆ(ω), |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
is the phase, the transforms in Example 3.13, X and are seen to
differ only in phase. Further, the phase of y(t) has a special form
∧
|     |     |     |     | ∠ Y (ω)= |     | −ωt |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
1
| as shown | in Figure | 3.10. |     |     |     |       |     |     |     |
| -------- | --------- | ----- | --- | --- | --- | ----- | --- | --- | --- |
|          |           |       |     |     | ∠ Y | ^ (w) |     |     |     |
w
−wt
1
|     | Figure | 3.10 | Linear | phase | associated | with | pure | delay |     |
| --- | ------ | ---- | ------ | ----- | ---------- | ---- | ---- | ----- | --- |

| Fourier transforms |       |               |     |       |     |     |     |     | 71  |
| ------------------ | ----- | ------------- | --- | ----- | --- | --- | --- | --- | --- |
| P3) Frequency      | Shift | or Modulation |     | Rule: |     |     |     |     |     |
If
F ∧
|     |     |     |     | x(t)↔ | X (ω) |     |     |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- |
then
∧
|          |        |                 | x(t)ejω | ot↔        | F (ω−ω |         | )   |     | (3.30) |
| -------- | ------ | --------------- | ------- | ---------- | ------ | ------- | --- | --- | ------ |
|          |        |                 |         |            | X      | o       |     |     |        |
| Equation | (3.30) | can be verified |         | by letting |        |         |     |     |        |
|          |        | y(t)=x(t)ejω    | ot      |            |        |         |     |     |        |
|          |        | (cid:4)         |         |            |        | (cid:4) |     |     |        |
|          |        |                 | ∞       |            |        | ∞       |     |     |        |
∧
|           | Y          | (ω)=  | x(t)ejω | ote−jωtdt | =     |       | x(t)e−j(ω−ω | o )tdt |     |
| --------- | ---------- | ----- | ------- | --------- | ----- | ----- | ----------- | ------ | --- |
|           |            |       | −∞      |           |       | −∞    |             |        |     |
|           | ∧          | ∧     |         |           |       |       |             |        |     |
|           |            | (ω)=X | (ω−ω    | )         |       |       |             |        |     |
|           | Y          |       |         | o         |       |       |             |        |     |
| Example   | 3.14       |       |         |           |       |       |             |        |     |
| If y(t) = | x(t) cos(ω | t) as | shown   | in Figure | 3.11, | using |             |        |     |
o
|     |     |     |        | 1       |     | 1        |     |     |     |
| --- | --- | --- | ------ | ------- | --- | -------- | --- | --- | --- |
|     |     |     |        | x(t)ejω |     | x(t)e−jω |     |     |     |
|     |     |     | y(t) = |         | ot+ |          | ot  |     |     |
|     |     |     |        | 2       |     | 2        |     |     |     |
y(t) = x(t) cos(ω
0 t)
t
|                     |       | Figure   | 3.11  | An        | amplitude | modulated | signal |     |     |
| ------------------- | ----- | -------- | ----- | --------- | --------- | --------- | ------ | --- | --- |
| and the modulation  |       | rule     |       |           |           |           |        |     |     |
|                     |       |          |       | 1         |           | 1         |        |     |     |
|                     |       | ∧ (ω)    |       | ∧ (ω−ω    | )+        | ∧         | (ω+ω   | )   |     |
|                     |       | Y        | =     | X         |           | X         |        |     |     |
|                     |       |          |       | 2         | o         | 2         | o      |     |     |
| The transform       | pairs | are      | shown | in Figure | 3.12      |           |        |     |     |
| P4) Differentiation |       | in Time: |       |           |           |           |        |     |     |
If
F ∧
|     |     |     | x(t)↔ | X (ω) | and x˙(t) | exists |     |     |     |
| --- | --- | --- | ----- | ----- | --------- | ------ | --- | --- | --- |

| 72  | Mathematical | basis for protective | relaying algorithms |
| --- | ------------ | -------------------- | ------------------- |
x(t) A
|     |     | F   | x^(ω) |
| --- | --- | --- | ----- |
ω
t
y(t) = x(t) cos(ω t)
0
|     |     | A/2 x ^ (ω+ω | ) x^(ω−ω ) A/2 |
| --- | --- | ------------ | -------------- |
|     |     | F            | 0 0            |
2 2
|     |     | −ω  | ω ω |
| --- | --- | --- | --- |
|     | t   | 0   |     |
0
Figure 3.12 Modulation
then
|     | F           | ∧     |     |
| --- | ----------- | ----- | --- |
|     | x˙(t)↔ (jω) | X (ω) |     |
and
|     | dn             | ∧   |     |
| --- | -------------- | --- | --- |
|     | x(t)↔ F (jω)nX | (ω) |     |
(3.31)
dtn
Equation (3.31) is obtained directly by differentiating the inversion integral
(cid:4)
∞
1 ∧ (ω)ejωtdω
x(t)= X
2π
(cid:4) −∞
| dx  | 1 ∞  | ∧         |     |
| --- | ---- | --------- | --- |
|     | (jω) | (ω)ejωtdω |     |
| =   |      | X         |     |
dt 2π
−∞
P5) Differentiation in Frequency:
If
|       | ∧     | d ∧      |     |
| ----- | ----- | -------- | --- |
| x(t)↔ | F (ω) | (ω)      |     |
|       | X and | X exists |     |
dω
then
|     | F          | d ∧ |     |
| --- | ---------- | --- | --- |
|     | (−jt)x(t)↔ | (ω) |     |
dω X
| As in P4: | (cid:4) |     |     |
| --------- | ------- | --- | --- |
∞
∧ x(t)e−jωtdt
X (ω)=
−∞
(cid:4)
∧
dX (ω) ∞
(−jt)x(t)e−jωtdt
=
dω
−∞

| Fourier | transforms |     |     |     |     |     |     | 73  |
| ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
In general
|     |     |     |     | dnX ∧ (ω) |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- |
F
|     |     |     |     |     | ↔ (−jt)nx(t) |     |     | (3.32) |
| --- | --- | --- | --- | --- | ------------ | --- | --- | ------ |
dωn
| Even | and Odd | Properties: |     | If x(t) is real |     |     |     |     |
| ---- | ------- | ----------- | --- | --------------- | --- | --- | --- | --- |
(cid:4)
∞
|     |     | ∧       | x(t)e−jωtdt |     |     |     |     |     |
| --- | --- | ------- | ----------- | --- | --- | --- | --- | --- |
|     |     | X (ω) = |             |     |     |     |     |     |
−∞
|     |     | (cid:4)         |          | (cid:4) |               |     |     |     |
| --- | --- | --------------- | -------- | ------- | ------------- | --- | --- | --- |
|     |     | ∞               |          | ∞       |               |     |     |     |
|     |     | x(t)cos(ωt)dt−j |          |         | x(t)sin(ωt)dt |     |     |     |
|     |     | −∞              |          | −∞      |               |     |     |     |
|     |     | (cid:14)        | (cid:15) | (cid:4) |               |     |     |     |
∞
∧
|     |     | Re X (ω) | =   | x(t)cos(ωt)dt | : an even | function | of ω |     |
| --- | --- | -------- | --- | ------------- | --------- | -------- | ---- | --- |
−∞
|     |     | (cid:14) | (cid:15) | (cid:4) |     |     |     |     |
| --- | --- | -------- | -------- | ------- | --- | --- | --- | --- |
∞
∧
|     |     | Im (ω) | =   | x(t)sin(ωt)dt | : an odd | function | of ω |     |
| --- | --- | ------ | --- | ------------- | -------- | -------- | ---- | --- |
X
−∞
∧
P6a): If x(t) is real and even, i.e. x(t) = x(−t), then X (ω) is real and even.
∧
(ω)
P6b): If x(t) is real and odd, i.e. x(t) = −x(−t), then X is pure imaginary and
odd.
| Properties |     | P6a and | P6b follow | from    |     |     |     |     |
| ---------- | --- | ------- | ---------- | ------- | --- | --- | --- | --- |
|            |     | (cid:4) |            | (cid:4) |     |     |     |     |
∞
|     | ∧    |             |     | 0   |            |     |     |     |
| --- | ---- | ----------- | --- | --- | ---------- | --- | --- | --- |
|     | (ω)= | x(t)e−jωtdt |     | =   | x(t)ejωtdt |     |     |     |
X
|     |     | 0            |     | −∞        |     |     |     |     |
| --- | --- | ------------ | --- | --------- | --- | --- | --- | --- |
|     |     | (cid:4)      |     | (cid:4)   |     |     |     |     |
|     |     | ∞            |     | ∞         |     |     |     |     |
|     |     | x(t)e−jωrdt+ |     | x(−τ)ejωτ |     |     |     |     |
|     |     | =            |     |           | dr  |     |     |     |
|     |     | 0            |     | 0         |     |     |     |     |
(cid:4)
∞
[x(t)e−jωt+x(−t)ejωt]dt
=
0
|     |     | (cid:4)                   |     |        | (cid:4)               |      |       |     |
| --- | --- | ------------------------- | --- | ------ | --------------------- | ---- | ----- | --- |
|     |     | ∞                         |     |        | ∞                     |      |       |     |
|     |     | = [x(t)+x(−t)]cos(ωt)dt+j |     |        | [x(−t)−x(t)]sin(ωt)dt |      |       |     |
|     |     | 0                         |     |        | 0                     |      |       |     |
|     |     | ∧                         |     |        | ∧                     |      |       |     |
|     |     | Re{X (ω)}                 |     |        | Im{X (ω)}             |      |       |     |
|     |     | x(t)=                     |     | −x(−t) |                       | x(t) | x(−t) |     |
|     |     | =0 if                     |     |        | = 0 if                | =    |       |     |
∧
| P7) | Time Scaling: | If  | x(t)↔ F | (ω) |     |     |     |     |
| --- | ------------- | --- | ------- | --- | --- | --- | --- | --- |
X
| then |     |     |     |     | (cid:16) (cid:17) |     |     |     |
| ---- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
ω
∧
X
|     |     |     |     | x(at)↔ F | a ;a (cid:12) 0 |     |     | (3.33) |
| --- | --- | --- | --- | -------- | --------------- | --- | --- | ------ |
a

| 74           |          |     |        | Mathematical |         | basis | for | protective | relaying | algorithms |
| ------------ | -------- | --- | ------ | ------------ | ------- | ----- | --- | ---------- | -------- | ---------- |
|              |          |     |        | y(t)         | = x(at) |       |     |            |          |            |
| To establish | Equation |     | (3.33) | let          |         |       |     |            |          |            |
(cid:4)
|     |     | ∧    |     | ∞              |     |     |        |     |     |     |
| --- | --- | ---- | --- | -------------- | --- | --- | ------ | --- | --- | --- |
|     |     | (ω)= |     | x(at)e−jωtdt;τ |     |     |        | τ/a |     |     |
|     |     | Y    |     |                |     |     | = at;t | =   |     |     |
−∞
1
|     |     |     | dt= | dτ  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a
|     |     |        |     | (cid:4) |       | (cid:16) (cid:17) |     | (cid:16) | (cid:17) |     |
| --- | --- | ------ | --- | ------- | ----- | ----------------- | --- | -------- | -------- | --- |
|     |     |        | 1   | ∞       |       | ω                 | 1   | ω        |          |     |
|     |     | ∧      |     |         | −j    | τ                 |     | ∧        |          |     |
|     |     | Y (ω)= |     |         | x(τ)e | a dτ              | =   | X        |          |     |
|     |     |        | a   | −∞      |       |                   | a   | a        |          |     |
Equation (3.33) is another expression of the inherent conservation of time-duration
(a>1)
and bandwidth. If scaling is used to make the time function narrow then the
transform is scaled in the opposite direction and becomes broader.
| Example      | 3.15  |     |               |          |          |     |     |     |     |     |
| ------------ | ----- | --- | ------------- | -------- | -------- | --- | --- | --- | --- | --- |
| The Gaussian | pulse | and | its transform |          |          |     |     |     |     |     |
|              |       |     |               | (cid:18) | (cid:19) |     |     |     |     |     |
2
−1 t
|     |     |     |      | e 2 | τ   | ∧    | − 1ω2τ2 |     |     |        |
| --- | --- | --- | ---- | --- | --- | ---- | ------- | --- | --- | ------ |
|     |     |     | x(t) |     | F   | (ω)= |         |     |     |        |
|     |     |     | =    | √   | ↔ X |      | e 2     |     |     | (3.34) |
2πτ
are shown in Figure 3.13. The transform pair in Equation (3.34) is important in
probabilityandstatistics.Itfurtherillustratesthetimeduration-bandwidthlimitation,
since the width of the time function is proportional to τ while the bandwidth is
1/τ.
| proportional | to  |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
^x(ω)
x(t)
|     |        |      |     | 2τ       |       |     | 2/τ         |           |     |     |
| --- | ------ | ---- | --- | -------- | ----- | --- | ----------- | --------- | --- | --- |
|     |        |      |     |          | t     |     |             |           | ω   |     |
|     | Figure | 3.13 | The | Gaussian | pulse | and | its Fourier | transform |     |     |
P8) Periodic Functions: Using the transforms of the impulse it is possible to
discuss the Fourier transforms of periodic functions for which we previously wrote
| Fourier series. | Recall: |     |     |     |     |     |     |     |     |     |
| --------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F
|     |     |     |     | δ(t)↔ | 1         |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --------- | --- | --- | --- | --- | --- |
|     |     |     |     | 1↔    | F 2πδ(ω)  |     |     |     |     |     |
|     |     |     |     | ejω   | F         |     |     |     |     |     |
|     |     |     |     | ot    | ↔ 2πδ(ω−ω |     | )   |     |     |     |
o

| Fourier | transforms |     |     |     |     |     | 75  |
| ------- | ---------- | --- | --- | --- | --- | --- | --- |
cos(ω
o t):
|     | 1   | [ejω ot+e−jω | F    |         |         |     |     |
| --- | --- | ------------ | ---- | ------- | ------- | --- | --- |
|     |     |              | ot]↔ | π[δ(ω−ω | )+δ(ω+ω | )]  |     |
|     |     |              |      |         | o       | o   |     |
2
sin(ω
o t):
π
|     | 1   | [ejω ot−e−jω | F    |        |         |     |     |
| --- | --- | ------------ | ---- | ------ | ------- | --- | --- |
|     |     |              | ot]↔ | [δ(ω−ω | )−δ(ω+ω | )]  |     |
|     |     |              |      |        | o       | o   |     |
|     | 2j  |              |      | j      |         |     |     |
Fourier series:
|     |      | (cid:5)∞ |           | (cid:5)∞ |        |     |        |
| --- | ---- | -------- | --------- | -------- | ------ | --- | ------ |
|     |      | ejkω     | ot; ∧ (ω) | 2π       | δ(ω−kω | )   |        |
|     |      | c        | R         | =        | c      |     | (3.35) |
|     |      | k        |           |          | k      | o   |        |
|     | k=−∞ |          |           | k=−∞     |        |     |        |
By drawing an impulse of strength c with a height of c , the transform in
|     |     |     |     | k   |     | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Equation(3.35)canbedrawnasinFigure3.14.ThediscretespectruminFigure3.14
isreferredtoasalinespectrum.TheinversionofEquation(3.25)returnstheoriginal
| expression | for the | Fourier series: |     |     |     |     |     |
| ---------- | ------- | --------------- | --- | --- | --- | --- | --- |
(cid:4)
(cid:5)∞
|     |     | 1     | ∞   |     |               |     |     |
| --- | --- | ----- | --- | --- | ------------- | --- | --- |
|     |     | r(t)= | 2π  |     | δ(ω−ω )ejωtdω |     |     |
|     |     |       |     | c k | o             |     |     |
2π
−∞
k=−∞
(cid:5)∞
|     |     | r(t)= | ejkω | ot  |     |     |     |
| --- | --- | ----- | ---- | --- | --- | --- | --- |
c
k
k=−∞
R(ω)
C 0
C
1
C 2
C
3
ω
|     |     | Figure | 3.14 | A line | spectrum |     |     |
| --- | --- | ------ | ---- | ------ | -------- | --- | --- |
P9):TheFouriertransformoftheunitstepshowninFigure3.15mustbeobtained
rathercarefully.Firstlety(t)=sgn(t)andletsgn(t)bethoughtofasthelimitshown
| in Figure | 3.16, i.e. |        |                  |     |            |     |        |
| --------- | ---------- | ------ | ---------------- | --- | ---------- | --- | ------ |
|           |            |        | [e−αtu(t)−u(−t)e |     | αt] sgn(t) |     |        |
|           |            | limα→0 |                  |     | =          |     | (3.36) |
| e−αtu(t)↔ | F          | 1      |                  |     |            |     |        |
Using
jω+α
1
|     |     |     | e−αtu(−t)↔ | F   |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- |
α−jω

| 76  |     |     |     | Mathematical | basis for | protective relaying | algorithms |
| --- | --- | --- | --- | ------------ | --------- | ------------------- | ---------- |
u(t)
1.0
t
|     |     |     | Figure | 3.15 | The unit step |     |     |
| --- | --- | --- | ------ | ---- | ------------- | --- | --- |
1.0
e−αt
t
eαt
−1.0
|     |     | Figure | 3.16    |          |                 |        |     |
| --- | --- | ------ | ------- | -------- | --------------- | ------ | --- |
|     |     |        |         | A signal | which limits to | sgn(t) |     |
|     |     |        | (cid:2) |          | (cid:3)         |        |     |
we obtain
|     |     |         |      | 1    | 1 2 |           |        |
| --- | --- | ------- | ---- | ---- | --- | --------- | ------ |
|     |     | limα→0  |      | −    | = = | F[sgn(t)] |        |
|     |     |         | α+jω | α−jω | jω  |           |        |
|     |     |         | F 2  |      |     |           |        |
|     |     | sgn(t)↔ |      |      |     |           | (3.37) |
jω
It should be noted that the transform pair in Equation (3.37) obeys property P6b
2/jω
| in that | sgn(t) is | odd and | the transform |             | is pure imaginary. |      |        |
| ------- | --------- | ------- | ------------- | ----------- | ------------------ | ---- | ------ |
| The     | transform | of the  | step can      | be obtained | by observing       | that |        |
|         |           |         |               | 1           | 1                  |      |        |
|         |           |         |               | u(t) =      | + sgn(t)           |      | (3.38) |
|         |           |         |               | 2           | 2                  |      |        |
1
|           | u(t)↔ | F   | +πδ(ω) |     |     |     |        |
| --------- | ----- | --- | ------ | --- | --- | --- | ------ |
| and hence |       |     |        |     |     |     | (3.39) |
jω
πδ(ω)
The in Equation (3.39) is due to 1/2 in Equation (3.38). In spite of the
fact that the Laplace transform of the unit step is 1/s the Fourier transform contains
| πδ(ω) |             |             |         | 1/ω.       |            |     |     |
| ----- | ----------- | ----------- | ------- | ---------- | ---------- | --- | --- |
| the   | term        | in addition | to      |            |            |     |     |
| P10)  | Convolution | in          | Time:   |            |            |     |     |
| Given | two signals | with        | Fourier | transforms |            |     |     |
|       |             |             |         | ∧          | ∧          |     |     |
|       |             |             | (t)↔    | F (ω),x    | (t)↔ F (ω) |     |     |
|       |             |             | x 1     | X 1        | 2 X 2      |     |     |

| Fourier    | transforms |             |     |     |            |       |     | 77     |
| ---------- | ---------- | ----------- | --- | --- | ---------- | ----- | --- | ------ |
| and a well | defined    | convolution |     | x 1 | * x 2 then |       |     |        |
|            |            |             |     |     | F ∧        | ∧     |     |        |
|            |            |             |     | x ∗ | x ↔ X      | (ω) X | (ω) | (3.40) |
|            |            |             |     | 1   | 2 1        | 2     |     |        |
Thatis,convolutionintimecorrespondstomultiplicationinthetransformdomain.
Equation (3.40) can be verified by taking the transform of the convolution. Let
|     |     |     | y(t)=x |     | ∗   |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- |
1 x 2
(cid:4)
∞
|     |     |     | y(t)= |     | x (τ)x | (t−τ)dτ |     |     |
| --- | --- | --- | ----- | --- | ------ | ------- | --- | --- |
|     |     |     |       |     | 1      | 2       |     |     |
−∞
|     |     |     | (cid:4) | (cid:2)(cid:4) |     |     | (cid:3) |     |
| --- | --- | --- | ------- | -------------- | --- | --- | ------- | --- |
then
∞ ∞
|     |     | ∧ (ω)= |     |     | (τ)x | (t−τ)dτ | e−jωtdt |     |
| --- | --- | ------ | --- | --- | ---- | ------- | ------- | --- |
|     |     | Y      |     |     | x    |         |         |     |
|     |     |        |     |     | 1 2  |         |         |     |
|     |     |        | −∞  | −∞  |      |         |         |     |
(cid:4)
∞
|     |     | ∧    |     |       | ∧             |     |                |     |
| --- | --- | ---- | --- | ----- | ------------- | --- | -------------- | --- |
|     |     | (ω)= |     | x (τ) | (ω)e−jωtdτ(by |     | delay rule P2) |     |
|     |     | Y    |     | 1     | X 2           |     |                |     |
−∞
|     |     | ∧     | ∧   | ∧   |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     | (ω)=X | (ω) | (ω) |     |     |     |     |
|     |     | Y     | 1   | X 2 |     |     |     |     |
Two examples of convolution given below are particularly interesting.
| Example | 3.16 |     |     |     |     |         |     |     |
| ------- | ---- | --- | --- | --- | --- | ------- | --- | --- |
| Let     |      |     |     |     |     | (cid:4) |     |     |
t
|     |     |     | Y(t)=x(t) |     | ∗ u(t)  | =   | x(τ)dr  |     |
| --- | --- | --- | --------- | --- | ------- | --- | ------- | --- |
|     |     |     |           |     | (cid:2) | −∞  | (cid:3) |     |
1
|     |     |     | ∧ (ω)=X |     | ∧ (ω) πδ(ω)+ |     |     |     |
| --- | --- | --- | ------- | --- | ------------ | --- | --- | --- |
Y
jω
∧
|     |     |     | ∧    |     | X (ω)  |     | ∧   |     |
| --- | --- | --- | ---- | --- | ------ | --- | --- | --- |
|     |     |     | (ω)= |     | +πδ(ω) |     | (0) |     |
|     |     |     | Y    |     |        |     | X   |     |
jω
| Example   | 3.17  |            |     |     |         |     |     |     |
| --------- | ----- | ---------- | --- | --- | ------- | --- | --- | --- |
| If x(t) * | x(−t) | is defined |     |     |         |     |     |     |
| then      |       |            |     |     | (cid:4) |     |     |     |
∞
|     |     | y(t) | = x(t) | ∗ x(−t) | =   | x(τ)x(−t+τ)dτ |     |     |
| --- | --- | ---- | ------ | ------- | --- | ------------- | --- | --- |
−∞

| 78  |     |     |     | Mathematical |     | basis | for protective | relaying | algorithms |
| --- | --- | --- | --- | ------------ | --- | ----- | -------------- | -------- | ---------- |
i.e.
|          |         |         | ∧       | ∧   | ∧     |         |          |     |     |
| -------- | ------- | ------- | ------- | --- | ----- | ------- | -------- | --- | --- |
|          |         |         | (ω)     | =   | (ω) ∗ | (ω) =   | |Xˆ(ω)2| |     |     |
|          |         |         | Y       | X   | X     |         |          |     |     |
| However, | if x(t) | is real |         |     |       |         |          |     |     |
|          |         |         | (cid:4) |     |       | (cid:4) |          |     |     |
|          |         |         | ∞       |     |       | ∞       |          |     |     |
∧
|     | F[x(−t)]= |     |     | x(−t)e−jωtdt |     | =   | x(τ)ejωτ dr = | ∗ (ω) |     |
| --- | --------- | --- | --- | ------------ | --- | --- | ------------- | ----- | --- |
X
|     |     |       | −∞ (cid:4) |                |     | −∞  |     |     |     |
| --- | --- | ----- | ---------- | -------------- | --- | --- | --- | --- | --- |
|     |     |       | 1          | ∞              |     |     |     |     |     |
|     |     | y(t)= |            | |Xˆ(ω)|2ejωtdt |     |     |     |     |     |
2π
−∞
|     |     |     | (cid:4) |     |     | (cid:4) |     |     |     |
| --- | --- | --- | ------- | --- | --- | ------- | --- | --- | --- |
|     |     |     | ∞       |     |     | ∞       |     |     |     |
1
|     |     | y(0)= |     | x2(τ)dτ | =   | |Xˆ(ω)|2dω |     |     |     |
| --- | --- | ----- | --- | ------- | --- | ---------- | --- | --- | --- |
2π
|                  |            |         | −∞         |                  |     | −∞         |     |     |     |
| ---------------- | ---------- | ------- | ---------- | ---------------- | --- | ---------- | --- | --- | --- |
| which is         | Parseval’s | theorem |            | for non-periodic |     | functions. |     |     |     |
| P11) Convolution |            | in      | Frequency: |                  |     |            |     |     |     |
Given
|        |         |     |          |        | ∧     |        | ∧   |     |     |
| ------ | ------- | --- | -------- | ------ | ----- | ------ | --- | --- | --- |
|        |         |     | x        | (t)↔ F | (ω),x | (t)↔ F | (ω) |     |     |
|        |         |     | 1        |        | X 1   | 2      | X 2 |     |     |
| ∧      | ∧       |     |          |        |       |        |     |     |     |
| with X | (ω) ∗ X | (ω) | defined, |        |       |        |     |     |     |
| 1      |         | 2   |          |        |       |        |     |     |     |
then
|     |     |     |      |      | 1   | ∧   | ∧     |     |        |
| --- | --- | --- | ---- | ---- | --- | --- | ----- | --- | ------ |
|     |     |     | (t)x | (t)↔ | F   | (ω) | ∗ (ω) |     |        |
|     |     |     | x    |      |     | X   | X     |     | (3.41) |
|     |     |     | 1    | 2    | 2π  | 1   | 2     |     |        |
Equation (3.41) is dual to Equation (3.40) in that convolution in one domain cor-
responds to multiplication in the other domain. Equation (3.41) can be verified by
taking the inverse transform of the convolution in frequency defined as
(cid:4)
|     |     |     | ∧   | 1   | ∞ ∧ | ∧     |         |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ------- | --- | --- |
|     |     |     | (ω) |     |     | (µ)   | (ω−µ)dµ |     |     |
|     |     |     | Y   | =   | X   | 1 X 2 |         |     |     |
2π
−∞
andusingthemodulationrule,P3,wherethedelayrule,P2,wasusedinestablishing
| Equation  | (3.40).  |        |      |         |     |     |     |     |     |
| --------- | -------- | ------ | ---- | ------- | --- | --- | --- | --- | --- |
| Example   | 3.18     |        |      |         |     |     |     |     |     |
| The ideal | low-pass | filter | from | Example | 3.9 |     |     |     |     |
sin(at)
(ω)↔ F
P
|     |     |     |     |     | a   | πt  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Fourier transforms 79
| generates | the pair |            |           |     |
| --------- | -------- | ---------- | --------- | --- |
|           |          | sin2(at) 1 |           |     |
|           |          | ↔ F        | (ω) ∗ (ω) |     |
P a P a
π2t2 2π
using P11. The transform pair is shown in Figure 3.17. It can be seen that
multiplying time functions increases the bandwidth since the convolution of two
band-limited spectra with bandwidths ω and ω respectively produces a transform
1 2
ω +ω
| with bandwidth | .   |     |     |     |
| -------------- | --- | --- | --- | --- |
|                | 1 2 |     |     |     |
sin2(at)
|     |     |     | 1 pa(ω)* pa(ω) | a   |
| --- | --- | --- | -------------- | --- |
π
|     |     | π2t2 | 2π  |     |
| --- | --- | ---- | --- | --- |
ω
|               |             | t             | −2a               | 2a   |
| ------------- | ----------- | ------------- | ----------------- | ---- |
|               | Figure 3.17 | The transform | pair from Example | 3.18 |
| P12) Symmetry | or Duality: |               |                   |      |
The symmetry property allows us to effectively double the number of transform
pairs at our disposal, in that, for each pair we know, we can find a second pair in
| the following | manner: |     |     |     |
| ------------- | ------- | --- | --- | --- |
If
F
|     |     | f(t)↔ | g(ω) | (3.42) |
| --- | --- | ----- | ---- | ------ |
then
F
|     |     | g(t)↔ | 2πf(−ω) | (3.43) |
| --- | --- | ----- | ------- | ------ |
The notation used in Equations (3.42) and (3.43) is slightly different from that
used previously in order to avoid confusion between the two domains. Here, for
example, the function g(.) is a transform in Equation (3.42) while it is a time
| function in | Equation (3.43). |     |     |     |
| ----------- | ---------------- | --- | --- | --- |
The property can be established through a sequence of changes of variables in
| the transform | equation: | (cid:4) |     |     |
| ------------- | --------- | ------- | --- | --- |
∞
|     |     | g(ω) | f(t)e−jωtdt |     |
| --- | --- | ---- | ----------- | --- |
=
−∞
| or  |     | (cid:4) |     |     |
| --- | --- | ------- | --- | --- |
∞
|     |     | g(z) | f(p)e−jzpdp |     |
| --- | --- | ---- | ----------- | --- |
=
−∞

| 80      |         |     |     | Mathematical | basis for protective | relaying algorithms |
| ------- | ------- | --- | --- | ------------ | -------------------- | ------------------- |
|         | −p = ω, | =   |     |              |                      |                     |
| Now let |         | z t |     |              |                      |                     |
(cid:4)
−∞
|     |     | g(t)= |     | f(−ω)ejtω(−dω) |     |     |
| --- | --- | ----- | --- | -------------- | --- | --- |
∞
(cid:4)
∞
|     |     |     |     | 1 2πf(−ω)ejωtdω |     |     |
| --- | --- | --- | --- | --------------- | --- | --- |
g(t)=
2π
−∞
| Example | 3.19 |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- |
1
| Given | x(t) = |     |     |     |     |     |
| ----- | ------ | --- | --- | --- | --- | --- |
1+t2
| Using duality | if  | we consider |      |         |           |     |
| ------------- | --- | ----------- | ---- | ------- | --------- | --- |
|               |     |             |      | (cid:2) | (cid:3)   |     |
|               |     |             | 1    | 1       | 1 1       |     |
|               |     | g(ω)        | =    | =       | +         |     |
|               |     |             | 1+ω2 |         | 1+jω 1−jω |     |
2
| 1    | ↔ F 1e−|t| |           |          |             |        |     |
| ---- | ---------- | --------- | -------- | ----------- | ------ | --- |
| i.e. |            | then from | symmetry |             |        |     |
| 1+ω2 | 2          |           |          |             |        |     |
|      |            |           |          | 1 F         | πe−|ω| |     |
|      |            | g(t)      | =        | ↔ 2π[f(−ω)] | =      |     |
1+t2
| 3.5 Use | of fourier | transforms |     |     |     |     |
| ------- | ---------- | ---------- | --- | --- | --- | --- |
Fourier transforms are used in a variety of areas ranging from communication sys-
temstooptics.Theimmediateapplicationofinterestinrelayingisinthedescription
of the frequency content of signals and of the effect of filters and algorithms on
those signals. If the box in Figure 3.18 represents a Linear Time Invariant System
| (LTI) then | there | is a function | h(t) | such that |        |     |
| ---------- | ----- | ------------- | ---- | --------- | ------ | --- |
|            |       |               |      | y(t) h(t) | ∗ w(t) |     |
= (3.44)
ω(t)
|     |     |     |     | LTI | y(t) |     |
| --- | --- | --- | --- | --- | ---- | --- |
h(t)
|     |     |     | Figure | 3.18 | LTI system |     |
| --- | --- | --- | ------ | ---- | ---------- | --- |

| Use of fourier | transforms |     |     |       |      |     |     |     |     | 81  |
| -------------- | ---------- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- |
|                |            |     |     | w(t)= | ejωt |     |     |     |     |     |
If the input is of the form then, using ideas from elementary circuit
| analysis, | the output | is  | of the | same | form, | i.e. |     |     |     |     |
| --------- | ---------- | --- | ------ | ---- | ----- | ---- | --- | --- | --- | --- |
∧ (ω)ejωt
|     |     |     |     | y(t) | = H |     |     |     |     | (3.45) |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | ------ |
Taking the Fourier transform of Equation (3.44), it is also clear that
|     |     |     |     | ∧ (ω) | ∧   | (ω) ∧ | (ω) |     |     |        |
| --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | ------ |
|     |     |     |     | Y     | = H | W     |     |     |     | (3.46) |
where
∧
| impulse | response | h(t) | ↔ F | (ω) frequency |     | response. |     |     |     |     |
| ------- | -------- | ---- | --- | ------------- | --- | --------- | --- | --- | --- | --- |
H
In other words, the frequency response of the system determines how the fre-
quency content of the input is passed to the output. It is in this sense that the
function of frequency of Example 3.9 can be considered to be an ideal low-pass
filter.Thefiltersusedinrelayingapplications havebeendiscussed inChapter 1.We
will usethe ideal low-passfilter for convenience indiscussing the ideaof sampling.
3.5.1 Sampling
| Given that | x(t) | is a band-limited |     | signal, | i.e. |     |     |     |     |     |
| ---------- | ---- | ----------------- | --- | ------- | ---- | --- | --- | --- | --- | --- |
∧
|     |     |     |     |     | x(t)↔ F | (ω) |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
X
and
∧
|     |     |     |     | X (ω) | = 0 for | |ω|>ω |     |     |     |     |
| --- | --- | --- | --- | ----- | ------- | ----- | --- | --- | --- | --- |
m
and suppose x(t) were multiplied by the periodic signal shown in Figure 3.19 to
| produce | a new | signal | called | the sampled |     | signal, |     |     |     |     |
| ------- | ----- | ------ | ------ | ----------- | --- | ------- | --- | --- | --- | --- |
k(cid:5)=∞
|     |     | r(t) |     | (t−nT | )    |     | −a>a, |     | >2a |     |
| --- | --- | ---- | --- | ----- | ---- | --- | ----- | --- | --- | --- |
|     |     | =    |     | p     | with | T   |       | or  | T   |     |
|     |     |      |     | a     | o    | o   |       |     | o   |     |
k=−∞
| If the | product | of x(t) | and | r(t) is | formed |          |     |     |     |     |
| ------ | ------- | ------- | --- | ------- | ------ | -------- | --- | --- | --- | --- |
|        |         |         |     |         | z(t)   | x(t)r(t) |     |     |     |     |
=
r(t)
1.0
2a
|     |     |     | −2T | −T     | −aa           | T   | 2T     |     |     |     |
| --- | --- | --- | --- | ------ | ------------- | --- | ------ | --- | --- | --- |
|     |     |     |     | 0      | 0             | 0   |        | 0   |     |     |
|     |     |     |     | Figure | 3.19 Sampling |     | signal |     |     |     |

| 82  |     |     |     | Mathematical |     | basis for | protective | relaying | algorithms |
| --- | --- | --- | --- | ------------ | --- | --------- | ---------- | -------- | ---------- |
z(t) = x(t).r(t)
x(t)
−aa
|     |     |     | −2T    | −T   |         | T 2T   | t   |     |     |
| --- | --- | --- | ------ | ---- | ------- | ------ | --- | --- | --- |
|     |     |     |        | 0 0  |         | 0      | 0   |     |     |
|     |     |     | Figure | 3.20 | Sampled | signal |     |     |     |
^
X (ω)
|     |     |     |        | −ω     | ω            |          | ω   |     |     |
| --- | --- | --- | ------ | ------ | ------------ | -------- | --- | --- | --- |
|     |     |     |        | m      |              | m        |     |     |     |
|     |     |     | Figure | 3.21 A | band-limited | spectrum |     |     |     |
as shown in Figure 3.20 it is possible to recover the signal x(t) from the signal z(t)
| with a filter | if  | the samples | are | close enough | together. |     |     |     |     |
| ------------- | --- | ----------- | --- | ------------ | --------- | --- | --- | --- | --- |
The process is best understood in the frequency domain. If the spectrum of x(t)
is as shown in Figure 3.21 and we form the transform of z(t) using the convolution
| in frequency | rule, | we obtain |     |     |       |     |     |     |     |
| ------------ | ----- | --------- | --- | --- | ----- | --- | --- | --- | --- |
|              |       |           |     |     | ∧     | ∧   |     |     |     |
|              |       |           |     |     | (ω) ∗ | (ω) |     |     |     |
|              |       |           |     | ∧   | X     | R   |     |     |     |
Z (ω) =
2π
|     |     |     |     |     |     |     |     | ω = | 2π/T |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Since r(t) is a periodic function, it has a line spectrum, i.e. with o o
|     |     |      | k(cid:5)=∞ |          | k(cid:5)=∞ |        |     |     |     |
| --- | --- | ---- | ---------- | -------- | ---------- | ------ | --- | --- | --- |
|     |     | r(t) |            | ejkω ot↔ | F 2π       | δ(ω−kω |     | )   |     |
|     |     | =    |            | c k      |            | c k    |     | o   |     |
|     |     |      | k=−∞       |          | k=−∞       |        |     |     |     |
and
k(cid:5)=∞
2π
|     |     | ∧   | (ω) |     | ∧ (ω) | ∗ δ(ω−kω | )   |     |     |
| --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- |
|     |     | Z   | =   |     | c X   |          |     |     |     |
|     |     |     |     | 2π  | k     |          | o   |     |     |
k=−∞
| if we examine |     | the convolution |     | with impulses |     |     |     |     |     |
| ------------- | --- | --------------- | --- | ------------- | --- | --- | --- | --- | --- |
(cid:4)
∞
|     |     | ∧       |        |     |        |     | ∧         |     |     |
| --- | --- | ------- | ------ | --- | ------ | --- | --------- | --- | --- |
|     |     | X (ω) ∗ | δ(ω−kω | ) = | δ(µ−kω | )   | X (ω−µ)dµ |     |     |
|     |     |         |        | o   |        | o   |           |     |     |
−∞
∧
|     |     | =X  | (ω)−kω | )   |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
o
k(cid:5)=∞
|     |     | ∧ (ω)= |     | ∧ (ω−kω | )   |     |     |     |        |
| --- | --- | ------ | --- | ------- | --- | --- | --- | --- | ------ |
|     |     | Z      |     | c X     |     |     |     |     | (3.47) |
|     |     |        |     | k       | o   |     |     |     |        |
k=−∞

| Discrete | fourier | transform |     |     |     |     |     |     | 83  |
| -------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
^
Z (ω)
^
|     | ^            |        |         | c X (ω) |          |       |             |             |     |
| --- | ------------ | ------ | ------- | ------- | -------- | ----- | ----------- | ----------- | --- |
|     | c−1 X (ω + ω | )      |         | 0       |          |       | ^ (ω − ω    | )           |     |
|     |              | 0      |         |         |          |       | c 1 X       | 0           |     |
|     |              |        |         |         |          |       |             | ^ (ω − 2ω ) |     |
|     |              |        |         |         |          |       |             | c 2 X 0     |     |
|     |              | −ω     |         |         |          |       | ω           | 2ω ω        |     |
|     | −ω           | − ω    | 0−ω + ω | −ω      | ω        | ω − ω | 0 ω + ω     | 0           |     |
|     | 0            | m      | 0  m    | m       | m        | 0  m  | 0           | m           |     |
|     |              | Figure | 3.22    | The     | spectrum | of    | the sampled | signal      |     |
∧
Equation(3.47)representsaspectrummadeupofshiftedreplicasofX (ω)asshown
| in Figure | 3.22. | If, as | shown, |     |     |     |     |     |     |
| --------- | ----- | ------ | ------ | --- | --- | --- | --- | --- | --- |
|           |       |        |        | ω   | < ω | −ω  |     |     |     |
|           |       |        |        |     | m   | o   | m   |     |     |
i.e.
ω >2ω
|     |     |     |     |     | o   | m   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
or
|     |     |     |     |     | <   | π/ω |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | To  | m   |     |     |     |
then the spectrum of x(t) can be recovered from z(t) with an ideal low-pass filter
| with a | cut-off | frequency | of  | ω   |     |     |     |     |     |
| ------ | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
m.
|     |     | ω   | 2ω  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The frequency, = , i.e. twice the highest frequency in the band-limited
o m
signal, is the Nyquist sampling frequency. It can be seen from Figure 3.22 that if
the sampling frequency were lower than the Nyquist frequency that there would
X(ω)
be overlap in the shifted replicas of and the output of the low-pass filter
would not be the original signal x(t). This effect is called aliasing. If a signal is
ω
to be sampled at a sampling rate corresponding to the frequency then to avoid
s
aliasing it is necessary to filter the signal to a bandwidth of ω /2. Such a filter is
s
referred to as an anti-aliasing filter (as discussed in Chapter 1).
| 3.6 | Discrete | fourier |     | transform |     |     |     |     |     |
| --- | -------- | ------- | --- | --------- | --- | --- | --- | --- | --- |
Given a continuous signal f(t), if we take N samples of f(t) at intervals of T sec to
form a finite duration discrete time signal as shown in Figure 3.23 with
f[n]=f(nT)
|     |     |     |     |     |     | 0 (cid:17) | n (cid:17) N−1 |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | --- |
N(cid:5)−1
∧
|     |     |     |     | (ω)= | d(nT)e−jωT |     |     |     |        |
| --- | --- | --- | --- | ---- | ---------- | --- | --- | --- | ------ |
|     |     |     | F   |      |            |     |     |     | (3.48) |
n=0
∧
|     |     |     | (ω), |     |     |     |     | ω   |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
then the transform, F is a continuous and periodic function of with a Fourier
series with only a finite number of terms (N) as shown by Equation (3.48).5 The
| time function |     | is described | by  | N numbers, |     | i.e. |     |     |     |
| ------------- | --- | ------------ | --- | ---------- | --- | ---- | --- | --- | --- |
f[0],f[1],f[2],...,f[N−1]

| 84  |     | Mathematical | basis for | protective relaying | algorithms |
| --- | --- | ------------ | --------- | ------------------- | ---------- |
f[n]
f[N-1]
f[0]
t
|     |             | T               | (N-1)T   |             |     |
| --- | ----------- | --------------- | -------- | ----------- | --- |
|     | Figure 3.23 | Finite duration | discrete | time signal |     |
ω
while the function of is continuous. It would be desirable (if possible) to obtain
a finite description of the transform, i.e. N numbers which completely describe the
∧
((cid:3)).
transform, F The key is to consider the periodic extension (see Problem 3.3)
of the time-limited discrete time signal. It can be shown that the discrete Fourier
| transform | pair |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
N(cid:5)−1
|     |       | ∧              | f(nT)e−jkn(cid:3) |     |        |
| --- | ----- | -------------- | ----------------- | --- | ------ |
|     | DFT : | F (k(cid:3) )= |                   | oT  | (3.49) |
o
n=0
N(cid:5)−1
1 ∧
|     | IDFT: | f(nT)= | (k(cid:3) | )ejnk(cid:3) oT | (3.50) |
| --- | ----- | ------ | --------- | --------------- | ------ |
F o
N
k=0
relate a sampled periodic time function (the periodic extension of the signal in
Figure 3.23) and a similar sampled periodic function of ω as shown in Figure 3.24.
There are N samples per period in each domain. In the time domain the samples
are at an interval of T sec and the period is NT sec. In the frequency domain the
|         | 2π/NT         | = (cid:3) |                | 2π/T. |     |
| ------- | ------------- | --------- | -------------- | ----- | --- |
| samples | are spaced at | 0 radians | and the period | is    |     |
A more compact form of Equations (3.49) and (3.50) can be obtained if we let
∧
|     |     | F =F (k(cid:3) ) | f = f(nT) |     |     |
| --- | --- | ---------------- | --------- | --- | --- |
|     |     | k o              | n         |     |     |
2n
|     |     | w=e−j(cid:3) oT | −j  |     |     |
| --- | --- | --------------- | --- | --- | --- |
|     |     | =               | e N |     |     |
^
|     | f[n] |     |     | F (kΩ ) |     |
| --- | ---- | --- | --- | ------- | --- |
0
2π
NT
T
|     |     | t   |     |     | ω   |
| --- | --- | --- | --- | --- | --- |
|     | T   |     |     | Ω   |     |
0
|     | Figure | 3.24 Discrete | Fourier transform | pair |     |
| --- | ------ | ------------- | ----------------- | ---- | --- |

| Discrete fourier | transform |     |     |     |     |     |     | 85  |
| ---------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
then
N(cid:5)−1
wnk
|     |     |     | f   | =   | f   |     |     | (3.51) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ |
|     |     |     |     | k   | n   |     |     |        |
n=0
N(cid:5)−1
1
|     |     |     | f   | =   | F w−nk |     |     | (3.52) |
| --- | --- | --- | --- | --- | ------ | --- | --- | ------ |
|     |     |     |     | n   | k      |     |     |        |
N
k=0
which makes the connection between N numbers in time and N numbers in fre-
quency more obvious. Notice that the difference in sign of the exponents plays the
same role as in the original transform and that the inverse transform has a scale
factor of 1/N rather than 1/2π. Equations (3.51) and (3.52) can also be expressed
| in matrix form | as  |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                |     |    |    |     |     |     |     |     |
F
|     |      |     | o   |     |        |         |        |        |
| --- | ---- | --- | --- | ---- | ------ | ------- | --------- | ------ |
|     |      |    |    |      | ...... |         |           |        |
|     |      |    | F  | w0   | w0     | wo      | f         |        |
|     |      |     | 1   |      |        |         | o         |        |
|     |      |    | ·  |  w0 | 1      | 2 . . . |        |        |
|     |      |    |    |     | w w    |         |   f 1  |        |
|     | [EQ] |    | ·  | =   |        |         |        | (3.53) |
|     |      |    | ·  | w 0  | w 2 w  | 4 . . . |           |        |
·
|     |     |    |    |     |       | ... |       |     |
| --- | --- | --- | --- | --- | ----- | --- | ----- | --- |
|     |     |     | ·   | w0  | w3 w6 |     | f N−1 |     |
F
N−1
In applications other than digital relaying, the fast Fourier transform (FFT) has
become the vehicle of application of the transform techniques developed in the first
part of this chapter. The FFT is in fact not a new transform, but rather a numerical
techniquetomakethecalculationoftheDFTfaster.6 Itisordersofmagnitudefaster
than the calculations implied by (Equation (3.53)) if all the F are desired and if
k
N is large. In relaying applications, however, N is small (from 4 to 20 for most
algorithms) and only a few of the F k are wanted. Generally only the fundamental
frequency component (k = 1) is used in impedance relaying while a few harmonics
(for example, the fundamental, the second, and the fifth) are used in transformer
algorithms. Hence the FFT has found little application in digital relaying.
| If we consider | the | signal |     |     |     |     |     |     |
| -------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
√
|     |     |     | v(t) | = 2V | cos(ωt+φ) |     |     |     |
| --- | --- | --- | ---- | ---- | --------- | --- | --- | --- |
with N samples per period (T = 2π/ω), the calculation in Equation (3.49) yields
N/2
|     |     |     | F   | =   | Vejϕ |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- |
1
2
The fundamental frequency phasor associated with the signal x(t) is then given by
|     |     |     |       |              | (cid:12) | (cid:13) |     |     |
| --- | --- | --- | ----- | ------------ | -------- | -------- | --- | --- |
|     |     |     |       | n=(cid:5)N−1 | 2πn      |          |     |     |
|     |     |     | 2     |              |          | e−j2πn/N |     |     |
|     |     | X   | =     |              | x        |          |     |     |
|     |     |     | 1 2/N |              | Nω       |          |     |     |
n=0

| 86  |     |     | Mathematical |          | basis for | protective relaying | algorithms |
| --- | --- | --- | ------------ | -------- | --------- | ------------------- | ---------- |
|     |     |     | (cid:12)     | (cid:13) |           |                     |            |
or with
2πn
|     |     |     | x =x |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     | n    | Nω  |     |     |     |
n=(cid:5)N−1
2
|     |     |     | X =   |     | x e−j2πn/N |     | (3.54) |
| --- | --- | --- | ----- | --- | ---------- | --- | ------ |
|     |     |     | 1 2/N |     | n          |     |        |
n=0
Equation (3.54) provides the basis of a number of relaying algorithms and will be
| seen again       | in Chapter | 4.  |             |     |        |         |     |
| ---------------- | ---------- | --- | ----------- | --- | ------ | ------- | --- |
| 3.7 Introduction |            | to  | probability | and | random | process |     |
As pointed out in Chapter 1, errors in the analog to digital conversion process can
be thought of as being random. There are additional errors or unmodeled signals
present in most relaying applications as will be discussed in later chapters. These
include signalsnot described bythemodel onwhich thealgorithmisbasedsuch as:
the transient response of the capacitively coupled voltage transformers, harmonics
produced by CT saturation, high frequency signals associated with reflection of
surge waveforms between the bus and the fault, and other system transients caused
by the fault. One valid comparison of algorithms is in terms of their ability to
reject these unwanted signals. If these error signals are considered to be random
processes then techniques of parameter estimation can be used to describe and
evaluate algorithms. This section is concerned with the probability and random
algorithms.7
| processes | underlying | this view | of relaying     |     |               |     |     |
| --------- | ---------- | --------- | --------------- | --- | ------------- | --- | --- |
| 3.7.1     | Random     | variables | and probability |     | distributions |     |     |
Consider an experiment in which a die is thrown and the result recorded. Suppose
the experiment is repeated 600 times. A typical set of results is summarized in
Table 3.1.
|     |     | Table   | 3.1 Results | of  | experiment |     |     |
| --- | --- | ------- | ----------- | --- | ---------- | --- | --- |
|     |     | Outcome |             |     | Number     |     |     |
|     |     |         | 1           |     | 101        |     |     |
|     |     |         | 2           |     | 100        |     |     |
|     |     |         | 3           |     | 95         |     |     |
|     |     |         | 4           |     | 94         |     |     |
|     |     |         | 5           |     | 113        |     |     |
|     |     |         | 6           |     | 97         |     |     |

| Introduction | to probability | and random | process |     | 87  |
| ------------ | -------------- | ---------- | ------- | --- | --- |
If we define the relative frequency of the outcome being a 3, for example, as
|     |     | number | of times a 3 is observed |     |     |
| --- | --- | ------ | ------------------------ | --- | --- |
F3=
|     |     |     | Total number of throws |     |     |
| --- | --- | --- | ---------------------- | --- | --- |
F3=95/600
then, as the number of throws, N, increases, a belief in statistical regularity would
imply that F should limit to a constant. We could define the probability that a 3 is
3
| observed | as that limit, | i.e. |                      |     |     |
| -------- | -------------- | ---- | -------------------- | --- | --- |
|          |                | Pr{a | 3 is observed} = lim | F   |     |
3
For a ‘fair’ die we would expect all of the probabilities to be 1/6. The outcome
of the experiment is then a random variable with six possible values 1, 2, 3, 4, 5,
and 6, and we have assigned a probability to each of the six possible outcomes.
If we imagine a similar but more elaborate experiment we can introduce a more
compact description of the behavior of the random variable. Suppose we throw 15
dice (a real handful) and record the total of the faces showing. The result can vary
from15(all1’s)to90(all6’s).Ifweattempttosummarizetheresultinatablesuch
as Table 3.1 we will need 76 entries (the 76 possible outcomes). A more compact
summary can be given by making 76 bins and counting the number of times the
total lies in each bin. If we present the results in a histogram we get a curve such
as that in Figure 3.25 (drawn for 30 000 trials). Another possible way of displaying
the result is to count the number of outcomes with values less than or equal to each
| value. Such | a cumulative | histogram     | is shown in Figure | 3.26. |     |
| ----------- | ------------ | ------------- | ------------------ | ----- | --- |
| 3.7.2       | Probability  | distributions | and densities      |       |     |
In general, random variables can be described with functions similar to the
cumulative histogram of Figure 3.26. If X denotes the random variable then the
18,000
rebmuN
10,000
|     |     |     | 20 40 60 | 80  |     |
| --- | --- | --- | -------- | --- | --- |
Total
|     |     | Figure | 3.25 Histogram |     |     |
| --- | --- | ------ | -------------- | --- | --- |

| 88  |     |     | Mathematical | basis for protective | relaying | algorithms |
| --- | --- | --- | ------------ | -------------------- | -------- | ---------- |
30,000
rebmuN
20,000
10,000
|     |     |     | 20  | 40 60 80 |     |     |
| --- | --- | --- | --- | -------- | --- | --- |
Total
|     |     | Figure | 3.26 Cumulative | histogram |     |     |
| --- | --- | ------ | --------------- | --------- | --- | --- |
0.8
)x(F
0.4
|     |     |     | 20  | 40 60 80 |     |     |
| --- | --- | --- | --- | -------- | --- | --- |
x
|          |                 | Figure 3.27 | A probability | distribution function |     |        |
| -------- | --------------- | ----------- | ------------- | --------------------- | --- | ------ |
| function | F x (x) defined | as          |               |                       |     |        |
|          |                 |             | F (x) =       | Pr{X ≤ x}             |     | (3.55) |
X
is called the probability distribution function for X. It is clear that F (x) is a mono-
x
tone non-decreasing function of x. The corresponding distribution function for our
| previous      | experiment | is shown    | in Figure 3.27. |     |     |     |
| ------------- | ---------- | ----------- | --------------- | --- | --- | --- |
| If a function | f(x)       | exists such | that            |     |     |     |
(cid:4)
x
|     |     |     | (x)   | f(ξ)dξ |     |        |
| --- | --- | --- | ----- | ------ | --- | ------ |
|     |     |     | F X = |        |     | (3.56) |
−∞
or
dF(x)
f(x) =
dx
then f(x) is referred to as the probability density function for X. It is the existence
of probability distribution functions and density functions which are tractable for
analysis that has made most of the results in modern probability and statistics
possible. Two common densities are the Gaussian density and the uniform density.
| The Gaussian | or  | normal density | is given | by  |     |     |
| ------------ | --- | -------------- | -------- | --- | --- | --- |
1
|     |     |     | f(x) | e−(x−m)2/2σ2 |     |        |
| --- | --- | --- | ---- | ------------ | --- | ------ |
|     |     |     | = √  |              |     | (3.57) |
2πσ

| Introduction | to probability | and random | process | 89  |
| ------------ | -------------- | ---------- | ------- | --- |
|              |                | 0.4        | f(x)    |     |
0.3
0.2
0.1
2 4 6
x
|     |     | Figure | 3.28 Gaussian density |     |
| --- | --- | ------ | --------------------- | --- |
f(x)
1/2
−1
1 x
|     |     | Figure | 3.29 Uniform density |     |
| --- | --- | ------ | -------------------- | --- |
and is shown in Figure 3.28 for an m of 3.0 and a σ of 1.0. A uniform density is
| shown in | Figure 3.29. |     |     |     |
| -------- | ------------ | --- | --- | --- |
3.7.3 Expectation
Given a function, g(x), of the random variable X, the expectation of g(x) is
defined as
(cid:4)∞
|     |     | E{g(x)} | = g(x)f(x)dx | (3.58) |
| --- | --- | ------- | ------------ | ------ |
−∞
In particular, the expected value of powers of x are important in describing
the random variable. The expected value of x is called the mean and is
given by
(cid:4)∞
xf(x)dx
|     |     | x = | E{x} = | (3.59) |
| --- | --- | --- | ------ | ------ |
−∞
For the Gaussian density, x = m (m= 3 in Figure 3.28). The fact that the mean
of the uniform distribution in Figure 3.29 is 0 can be verified by integration.

| 90  |     |     | Mathematical |     | basis for protective | relaying | algorithms |
| --- | --- | --- | ------------ | --- | -------------------- | -------- | ---------- |
The expected value of the square of the difference between x and its mean is
a measure of the width of the density. The variance of the random variable x is
defined as
(cid:4)∞
|     |     | σ2  | = E{x−x)2} | =   | (x−x)2f(x)dx |     | (3.60) |
| --- | --- | --- | ---------- | --- | ------------ | --- | ------ |
−∞
σ
The quantity is referred to as the standard deviation. The standard deviation
for the Gaussian density is, of course, σ. The standard deviation of the Gaussian
one-σ
density in Figure 3.28 is 1. The width of the density at the level is shown in
| Figure 3.28. | Note | that |     |     |     |     |     |
| ------------ | ---- | ---- | --- | --- | --- | --- | --- |
F(m+σ)=e−1/2f(m)
|     |     |     | e−1/2 | =.6075 |     |     |     |
| --- | --- | --- | ----- | ------ | --- | --- | --- |
The variance of the uniform density in Figure 3.30 can be obtained as
|     |     |     | (cid:4)1 |      | (cid:11)       |     |     |
| --- | --- | --- | -------- | ---- | -------------- | --- | --- |
|     |     |     |          |      | 1x3(cid:11) −1 |     |     |
|     |     |     | 1        |      | 1              |     |     |
|     |     |     | σ2       | x2dx | (cid:11)       |     |     |
|     |     |     | =        | =    | (cid:11) =     |     |     |
|     |     |     | 2        |      | 2 3 3          |     |     |
1
−1
| or the standard | deviation           |     | is σ = .57735. |           |     |     |     |
| --------------- | ------------------- | --- | -------------- | --------- | --- | --- | --- |
| 3.7.4           | Jointly distributed |     | random         | variables |     |     |     |
It is common to have more than one source of random error in a given application.
For that reason we must be concerned with jointly distributed random variables.
Because of our intended use of these results we will step directly to a vector valued
| random | variable. Let | X   | be a vector | of n random | variables |     |     |
| ------ | ------------- | --- | ----------- | ----------- | --------- | --- | --- |
(cid:11) (cid:11)
(cid:11) (cid:11)
(cid:11)X (cid:11)
1
(cid:11) (cid:11)
(cid:11)X 2 (cid:11)
(cid:11) . (cid:11)
|     |     |     |     | X = | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
(cid:11) . (cid:11)
(cid:11) (cid:11)
(cid:11) (cid:11)
X n
| with a joint | probability |     | distribution |        |      |     |     |
| ------------ | ----------- | --- | ------------ | ------ | ---- | --- | --- |
|              |             |     | F (x)        | = Pr{X | ≤ x} |     |     |
X
where x is also an n vector. There is also a joint density of the form
∂nF(x)
|     |     |     | f(x) | =   |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
∂x ∂x ...∂x
|     |     |     |     | 1   | 2 n |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

| Introduction | to  | probability | and random | process |     |     |     |     | 91  |
| ------------ | --- | ----------- | ---------- | ------- | --- | --- | --- | --- | --- |
Expectations are computed with repeated integrals in the form
|     |     |         | (cid:4)∞ | (cid:4)∞ | (cid:4)∞ |     |     |     |     |
| --- | --- | ------- | -------- | -------- | -------- | --- | --- | --- | --- |
|     |     | E{g(x)} |          | ...      | g(x)f(x) |     | ... |     |     |
|     |     |         | =        |          |          | dx  | dx  | dx  |     |
|     |     |         |          |          |          | 1   | 2   | n   |     |
|     |     |         | −∞−∞     | −∞       |          |     |     |     |     |
−
In particular, the mean x is a vector and the covariance matrix P is defined as
|     |     |     |     | = E{(x−x)(x−x)T} |     |     |     |     |        |
| --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | ------ |
|     |     |     | P   |                  |     |     |     |     | (3.61) |
where the superscript T denotes the transpose of the vector, i.e. P is a symmetric n
| by n matrix | with |     |     |      |       |      |     |     |     |
| ----------- | ---- | --- | --- | ---- | ----- | ---- | --- | --- | --- |
|             |      |     |     | E{(x | −x)(x | −x)} |     |     |     |
P =
|     |     |     | ij  |     | i i | j i |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The diagonal entries in P are the variances of the individual random variables,
whiletheoff-diagonalentriesareinsomesenseameasureoftheconnectionbetween
the random variables. The form of the density for a Gaussian random variable is
|     |     |     |     | (cid:7) |     |     | (cid:8) |     |     |
| --- | --- | --- | --- | ------- | --- | --- | ------- | --- | --- |
−1(x−m)TP−1(x−m)
exp
|     |     |     | F(x) = | 2       |         |     |     |     | (3.62) |
| --- | --- | --- | ------ | ------- | ------- | --- | --- | --- | ------ |
|     |     |     |        | (2π)n/2 | detP1/2 |     |     |     |        |
−
| Example | 3.20 |     |     |     |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Given two Gaussian random variables with E {X } = 0,E{X } = 0,E{X2} = 5,
|           |     |      |           |     |     | 1   |     | 2   | 1   |
| --------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- |
| E{X2} =3, | and | E {X | X } = −3, |     |     |     |     |     |     |
| 2         |     |      | 1 2       |     |     |     |     |     |     |
then
|     |     |     | (cid:2) | (cid:3) |       | (cid:2) | (cid:3) |     |     |
| --- | --- | --- | ------- | ------- | ----- | ------- | ------- | --- | --- |
|     |     |     |         | 5 −3    |       | 1 3     | 3       |     |     |
|     |     |     | P =     |         | , P−1 | =       |         |     |     |
|     |     |     | −3      | 5       |       | 3       | 5       |     |     |
6
| and |     |     |          |     | (cid:2)   |     |         | (cid:3) |     |
| --- | --- | --- | -------- | --- | --------- | --- | ------- | ------- | --- |
|     |     |     | 1        |     | 1         |     |         |         |     |
|     |     | f(x | ,x ) = √ | exp | − (3x2+6x |     | x +5x2) |         |     |
|     |     | 1   | 2        |     |           | 1   | 1 2     | 2       |     |
|     |     |     | 24π      |     | 12        |     |         |         |     |
3.7.5 Independence
Random variablesaresaidtobe independent iftheir densitiesor distributionsfactor
into a product of densities of distributions. For example X and X are independent
|     |     |     |     |     |     |     | 1   | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
if
|     |     |     | f    | (x ,x ) | = f (x | )f (x | )   |     |     |
| --- | --- | --- | ---- | ------- | ------ | ----- | --- | --- | --- |
|     |     |     | X1X2 | 1 2     | X1     | 1 X2  | 2   |     |     |

| 92  |     |     | Mathematical | basis | for protective | relaying algorithms |
| --- | --- | --- | ------------ | ----- | -------------- | ------------------- |
Since the joint Gaussian density in Equation (3.62) is completely specified by its
mean and covariance matrix, it follows that Gaussian random variables are inde-
pendent if their covariance matrix is diagonal. This is not true of arbitrary densities
| but is one | of the many       | conveniences | of the | Gaussian | density. |     |
| ---------- | ----------------- | ------------ | ------ | -------- | -------- | --- |
| 3.7.6      | Linear estimation |              |        |          |          |     |
As we will see in Chapter 4, many algorithms involve processing a total number
of measurements that exceeds the number of parameters to be determined. In its
simplest form such a problem can be cast as that of solving an ‘overdefined’ set of
| equations | in the form |     |       |     |     |        |
| --------- | ----------- | --- | ----- | --- | --- | ------ |
|           |             |     | A x = | b   |     | (3.63) |
whereAandbareknownandxistobedetermined.Theequationsare‘overdefined’
| if there | are more b’s | than x’s. | As an example   | consider |     |     |
| -------- | ------------ | --------- | --------------- | -------- | --- | --- |
|          |              |          |                |         |    |     |
|          |              |           | (cid:2) (cid:3) | 3/4      |     |     |
1 0
|     |     |     |  x              | (cid:1)(cid:1) |    |     |
| --- | --- | ---- | ---------------- | --------------- | --- | --- |
|     |     | 1 −1 | 1 (cid:1)(cid:1) | = −1/4          |     |     |
x
|     |     |     | 2   | 3/4 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
0 1
Theequalsignisinquotessincethereisnosolutiontotheequation.Thefirstrow
has solution x = 5/4 while the last row gives x = 3/4. Under these conditions
|            | 1      |     |     | 2   |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- |
| the second | row is |     |     |     |     |     |
1/2 = −1/4
A more reasonable approach to the ‘solution’ of an equation such as Equation
| (3.63) is | to recognize | that there | is an error | and write |     |     |
| --------- | ------------ | ---------- | ----------- | --------- | --- | --- |
b = A x+e
where
e = b−Ax
The solution above is one in which e(1) and e(3) are 0 and e(2) is −3/4. In an
attempt to spread the error around a little more we could take as a measure of the
| quality | of the solution | the sum | of the squared | e’s, i.e. |     |     |
| ------- | --------------- | ------- | -------------- | --------- | --- | --- |
eTe=(b−Ax)T(b−Ax)
=(bT−xTAT)(b−A)
|     |     | =xTATA | x−xTATb−bTA |     | x+bTb |     |
| --- | --- | ------ | ----------- | --- | ----- | --- |
(3.64)
eTe
The x that minimizes can be obtained by taking the partial derivatives of
Equation (3.74) with respect to the components of x and equating to zero. The

| Introduction | to probability | and | random | process |     |     |     |     | 93  |
| ------------ | -------------- | --- | ------ | ------- | --- | --- | --- | --- | --- |
result is
∧
|     |     |     |     | = (ATA)−1ATb |     |     |     |     | (3.65) |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --- | ------ |
X
The calculation in Equation (3.65) is sometimes referred to as the pseudo inverse.
A mnemonic for Equation (3.65) is to multiply Equation (3.63) on both sides by
| AT  |               |        |         |     |            |     | (ATA), |      |     |
| --- | ------------- | ------ | ------- | --- | ---------- | --- | ------ | ---- | --- |
| and | then multiply | by the | inverse | of  | the square |     | matrix | i.e. |     |
∧
Ax=b
∧
ATAx=ATb
∧
x=(ATA)−1ATb
For our example
|     |     |      |         |         |    |    |         |         |     |
| --- | --- | ---- | ------- | ------- | --- | --- | ------- | ------- | --- |
|     |     |      | (cid:2) | (cid:3) |     |     | (cid:2) | (cid:3) |     |
|     |     |      |         |         | 1   | 0   |         |         |     |
|     |     |      | 1       | 1 0     |    |    | 2 −1    |         |     |
|     |     | ATA= |         |         | 1   | −1  | =       |         |     |
|     |     |      | 0       | −1 1    |     |     | −1      | 2       |     |
|     |     |      |         |         | 0   | 1   |         |         |     |
|     |     |      | (cid:2) | (cid:3) |     |     |         |         |     |
|     |     |      | 1       | 2 1     |     |     |         |         |     |
(ATA)−1
=
|     |     |      | 3       | 1 2            |     |         |                 |     |     |
| --- | --- | ---- | ------- | -------------- | --- | ------- | --------------- | --- | --- |
|     |     |      | (cid:2) | (cid:3)(cid:2) |     | (cid:3) | (cid:2) (cid:3) |     |     |
|     |     |      | 1       | 1 0            | 5/4 |         | 1               |     |     |
|     |     | ATb= |         |                |     | =       |                 |     |     |
−1/4
|     |     |     | 0       | −1 1    |     |     | 1   |     |     |
| --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- |
|     |     |     |         |         |     |    |    |     |     |
|     |     |     | (cid:2) | (cid:3) |     |     |     |     |     |
1/4
|     |     | ∧   | 1   | ,   | ∧   |    | −1/4  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
|     |     | x=  |     | b−A | x   | =   |        |     |     |
1
−1/4
It is an accident that the errors are of exactly the same magnitude in the example,
but it is reasonable to assume that they will be approximately the same size since
we are minimizing the sum of the squares of all of the errors.
| 3.7.7 | Weighted | least | squares |     |     |     |     |     |     |
| ----- | -------- | ----- | ------- | --- | --- | --- | --- | --- | --- |
Suppose we had a more detailed statistical knowledge of the errors in the equation
|     |     |     |     | b = | A x+e |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
Suppose we knew that e had a zero mean and a covariance matrix
|     |     |     |     | E { e | eT } = | V   |     |     | (3.66) |
| --- | --- | --- | --- | ----- | ------ | --- | --- | --- | ------ |
If e were Gaussian and the covariance matrix, V, were diagonal, the compo-
nents of the error would be independent (but possibly of different sizes). Given a

| 94  |     | Mathematical | basis for protective | relaying algorithms |
| --- | --- | ------------ | -------------------- | ------------------- |
covariance, V, it would make more sense to weight the errors in the minimization,
| i.e. to seek | an x that minimized |     |     |     |
| ------------ | ------------------- | --- | --- | --- |
eTV−1e
| Again, if | V were diagonal |     |     |     |
| --------- | --------------- | --- | --- | --- |
(cid:5) e2(i)
eTV−1e =
V
ii
That is, an error e(i) with a large variance would have a smaller contribution to
the sum than one with a smaller covariance. The solution to the minimization is
given by
∧
(ATV−1A)−1ATV−1b
X = (3.67)
| For the example, | if  |     |     |     |
| ---------------- | --- | --- | --- | --- |
(cid:11) (cid:11)
(cid:11)1 0 0(cid:11)
(cid:11) (cid:11)
|     | V=(cid:11)0 | 1 0(cid:11) |     |     |
| --- | ----------- | ----------- | --- | --- |
0 0 100
|     | (cid:11) | (cid:11) | (cid:11)     | (cid:11)       |
| --- | -------- | -------- | ------------ | -------------- |
|     | (cid:11) | (cid:11) | (cid:11) . 0 | 0 7 4 (cid:11) |
1 . 2 4 2 6
|     | ∧ (cid:11)  | (cid:11) , | ∧ (cid:11) (cid:11)−. | (cid:11)       |
| --- | ----------- | ---------- | --------------------- | -------------- |
|     | x= (cid:11) | (cid:11)   | b−A x = 0             | 0 7 4 (cid:11) |
1 . 4 8 5 3
−.7353
It can be seen that, since the third error is assumed to have a variance 100 times the
other two errors, the estimate xˆ drives the error in the first two components down
to much smaller values than the third. In fact, the first two errors are much smaller
| than they were | when the three | errors were | treated equally. |     |
| -------------- | -------------- | ----------- | ---------------- | --- |
Weightedleastsquaresestimation(Equation(3.67))isusedinpowersystemstatic
state estimation and is an ingredient of many relaying algorithms.
| 3.8 Random | processes |     |     |     |
| ---------- | --------- | --- | --- | --- |
Consideratimefunctionthatdependsononeormorerandomvariables.InChapter4
we will see that the non-fundamental frequency component of the fault waveform
can be modeled as depending on random parameters such as the fault incidence
angle and fault location. Suppose we imagine an ensemble of simultaneous experi-
ments where the random variables are chosen according to their probability laws as
represented in Figure 3.30. Each time function is a sample function of the random
process. If all of the sample functions are examined at a fixed time t, as shown,
i
then the random variable x(t) can be described by a probability density.
i
The joint probability density for x at all times t i is then a description of the
random process. Somewhat more convenient characterizations of the process are
possible if the process is well behaved. For example the mean of the process can
be computed
|     |     | xˆ(t) = | E{x(t)} |     |
| --- | --- | ------- | ------- | --- |

Random processes 95
x (t)
1
x (t)
2
x (t)
n
t
1
| Figure | 3.30 | An ensemble | of experiments |     |
| ------ | ---- | ----------- | -------------- | --- |
and a correlation function defined
|     |     | (t ,t ) = | E{x(t )x(t )} |        |
| --- | --- | --------- | ------------- | ------ |
|     | R   | x 1 2     | 1 2           | (3.68) |
The process is said to be stationary in the wide sense if the mean is constant and
the correlation function depends only on the difference between t and t , i.e.
1 2
|     |     | R (t,t−τ)= | R (τ) | (3.69) |
| --- | --- | ---------- | ----- | ------ |
|     |     | x          | x     |        |
The Fourier transform of the correlation function of a wide sense stationary
random process has a special meaning. Let the power spectrum of the random
process x(t) be defined as
(cid:4)∞
(τ)e−jωtdτ
|     | S (ω)= |     | R   | (3.70) |
| --- | ------ | --- | --- | ------ |
|     | x      |     | x   |        |
−∞
(cid:4)∞
1
|     | (τ)= |     | (ω)ejωτ dω |        |
| --- | ---- | --- | ---------- | ------ |
|     | R x  |     | S x        | (3.71) |
2π
−∞
In other words, the correlation function and the power spectrum are a Fourier
transform pair. The power spectral density is a description of how the energy in
the random process is distributed in frequency. A process that has a power spectral
density that is a constant for all ω is referred to as ‘white noise’ since it contains

| 96  |     |     |     | Mathematical |     | basis for | protective | relaying algorithms |
| --- | --- | --- | --- | ------------ | --- | --------- | ---------- | ------------------- |
|     |     |     |     | R(τ)         |     |           | S(ω)       |                     |
|     |     |     |     | x            |     |           | x          |                     |
|     |     |     |     |              | τ   |           |            | ω                   |
Figure 3.31 A correlation function and power density function
all frequencies. A correlation function and the corresponding power spectrum are
| shown    | in  | Figure 3.31. |         |        |             |     |     |     |
| -------- | --- | ------------ | ------- | ------ | ----------- | --- | --- | --- |
| Example  |     | 3.21         |         |        |             |     |     |     |
| Consider |     | the random   | process | given  | by          |     |     |     |
|          |     |              |         | x(t) = | A cos(ωτ+φ) |     |     |     |
where A is a constant, ω is a uniform random variable in the interval from ω
1
to ω , and ϕ is independent of ω and uniform in 0 to 2π. This is similar to a
2
model of the transient components of voltages and currents in a power network.
Each sample function is a pure cosine with a constant frequency and amplitude.
The expectation in the calculation of the correlation function in Equation (3.69) is
| over | both | ω and ϕ. | That | is, |     |     |     |     |
| ---- | ---- | -------- | ---- | --- | --- | --- | --- | --- |
(cid:4)2π(cid:4)ω
2
1
|     |     | (t ,t ) |      |      | A2cos(ωt | +ϕ)cos(ωt |     | +ϕ)dωdϕ |
| --- | --- | ------- | ---- | ---- | -------- | --------- | --- | ------- |
|     | R x | 1 2 =   |      |      |          | 1         |     | 2       |
|     |     |         | 2π(ω | −ω ) |          |           |     |         |
2 1
0 ω
1
Using
|     |     |           |     | 1         | 1   |          |     |     |
| --- | --- | --------- | --- | --------- | --- | -------- | --- | --- |
|     |     | cos x cos | y=  | cos(x+y)+ |     | cos(x−y) |     |     |
|     |     |           |     | 2         | 2   |          |     |     |
(cid:4)2π(cid:4)ω
2
A2
|     |     | (t    | ,t )= |         |     | cos(ω(t | )+2ϕ)dϕdω |     |
| --- | --- | ----- | ----- | ------- | --- | ------- | --------- | --- |
|     |     | R x 1 | 2     |         |     | 2       | +t 1      |     |
|     |     |       |       | 4π(ω −ω | )   |         |           |     |
|     |     |       |       | 2       | 1   |         |           |     |
0 ω
1
(cid:4)2π(cid:4)ω
2
A2
|     |     |     | +   |         |     | cos(ω(t | −t ))dωdϕ |     |
| --- | --- | --- | --- | ------- | --- | ------- | --------- | --- |
|     |     |     |     |         |     | 2       | 1         |     |
|     |     |     |     | 4π(ω −ω | )   |         |           |     |
|     |     |     |     | 2       | 1   |         |           |     |
0 ω
1
The first integral is zero and the second is a function of the difference, τ = t −t .
2 1
|     |     |     |      |     | (cid:2) |        |      | (cid:3) |
| --- | --- | --- | ---- | --- | ------- | ------ | ---- | ------- |
|     |     |     |      | A2  |         | sinω τ | sinω | τ       |
|     |     |     | (τ)= |     |         | 2 −    | 1    |         |
R x
|     |     |     |     | 2(ω −ω | )   | τ   | τ   |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- |
|     |     |     |     | 2      | 1   |     |     |     |

Random processes 97
| Using | the transform |     | of the | ideal | low-pass |     |     |     |     |
| ----- | ------------- | --- | ------ | ----- | -------- | --- | --- | --- | --- |
πA2
|     |     | (ω)= |     | ;−ω  |     | ω   | −ω ,ω | ω   | ω   |
| --- | --- | ---- | --- | ---- | --- | --- | ----- | --- | --- |
|     |     | S    |     |      | ≤   | ≤   |       | ≤   | ≤   |
|     |     | x    | (ω  | −ω ) | 2   |     | 1     | 1   | 2   |
|     |     |      | 2   | 1    |     |     |       |     |     |
=0;elsewhere.
| The spectrum |     | is shown | in  | Figure | 3.32. |     |     |     |     |
| ------------ | --- | -------- | --- | ------ | ----- | --- | --- | --- | --- |
(ω)
S x
πA2
(ω −ω
)
2 1
|       |           |      |        | ω         |         | ω        | ω   |            |      |
| ----- | --------- | ---- | ------ | --------- | ------- | -------- | --- | ---------- | ---- |
|       |           |      |        | 1         |         | 2        |     |            |      |
|       | Figure    | 3.32 | The    | power     | density | spectrum |     | of Example | 3.20 |
| 3.8.1 | Filtering | of   | random | processes |         |          |     |            |      |
If a wide sense stationary random process x(t) with power density spectrum S (ω)
x
is the input to a filter with transfer function H(ω) as shown in Figure 3.33 then the
y(t)
| output   | is     | also a wide | sense       | stationary |            | random | process | with |        |
| -------- | ------ | ----------- | ----------- | ---------- | ---------- | ------ | ------- | ---- | ------ |
|          |        |             |             | (ω)        | (ω)|H(ω)|2 |        |         |      |        |
|          |        |             |             | S y        | = S x      |        |         |      | (3.72) |
| Equation | (3.72) | can be      | established |            | by writing |        |         |      |        |
(cid:4)∞
|     |     |     |     | y(t) = | x(τ)h(t−τ)dτ |     |     |     |     |
| --- | --- | --- | --- | ------ | ------------ | --- | --- | --- | --- |
−∞
E{y(t)y(t+τ)},
forming and using Fourier transforms. Our particular interest in
H(ω)
the relationship in Equation (3.72) is in terms of the anti-aliasing filter. If is
the transfer function of the anti-aliasing filter and x(t) is the raw (unfiltered) mea-
surement noise then y(t) is the noise seen by the A/D converter. The multiplication
inEquation(3.72)thenaltersthepowerdensityspectrumofthenoise.Forexample,
|     |     |     |     | x(t) |     |     | y(t) |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- |
H(ω)
|     |     |        |      | S(ω)      |     |            | S(ω) |              |     |
| --- | --- | ------ | ---- | --------- | --- | ---------- | ---- | ------------ | --- |
|     |     |        |      | x         |     |            | y    |              |     |
|     |     | Figure | 3.33 | Filtering | of  | the random |      | process x(t) |     |

| 98  |     | Mathematical | basis for protective | relaying | algorithms |
| --- | --- | ------------ | -------------------- | -------- | ---------- |
|     |     |              | ω =                  |          | H(ω)       |
if x(t) has the spectrum shown in Figure 3.32 with 1 0 and the filter is
an ideal low-pass with a cut-off frequency of ω (ω < ω ) then the output power
|     |     |     | 3 3 2 |     |     |
| --- | --- | --- | ----- | --- | --- |
ω
spectrum is also flat but has a cut-off frequency of radians. The impact of
3
anti-aliasing filters on the performance of line relay algorithms will be investigated
| in more    | detail in Chapter | 4.  |     |     |     |
| ---------- | ----------------- | --- | --- | --- | --- |
| 3.9 Kalman | filtering         |     |     |     |     |
The Kalman filter provides a solution to the estimation problem in the context of
an evolution of the parameters to be estimated according to a state equation. It has
been used extensively in estimation problems for dynamic systems.8–10 Its use in
relaying is motivated by the filter’s ability to handle measurements that change in
time. To model the problem so that a Kalman filter may be used it is necessary to
write a state equation for the parameters to be estimated in the form
=φ +(cid:4)
|     |     | x x   | w     |     | (3.73) |
| --- | --- | ----- | ----- | --- | ------ |
|     |     | k+1 k | k k k |     |        |
+ε
|     |     | z =H | x   |     | (3.74) |
| --- | --- | ---- | --- | --- | ------ |
|     |     | k k  | k k |     |        |
whereEquation(3.73)(thestateequation)representstheevolutionoftheparameters
in time and Equation (3.74) represents the measurements. The terms w and ε are
|     |     |     |     | k   | k   |
| --- | --- | --- | --- | --- | --- |
discrete time random processes representing state noise, i.e. random inputs in the
evolution of the parameters, and measurement errors, respectively. Typically w
k
and ε are assumed to be independent of each other and uncorrelated from sample
k
to sample. If w and ε have zero means then it is common to assume that
|     | k   | k         |        |     |        |
| --- | --- | --------- | ------ | --- | ------ |
|     |     | E{w wT}=Q | ;k = j |     | (3.75) |
k j k
=0;k (cid:6)= j
E{ε εT}=R
|     |     |     | ;k = j |     | (3.76) |
| --- | --- | --- | ------ | --- | ------ |
k j k
=0;k (cid:6)= j
The matrices Q and R are the covariance matrices of the random processes and
|             | k         | k             |     |     |     |
| ----------- | --------- | ------------- | --- | --- | --- |
| are allowed | to change | as k changes. |     |     |     |
The matrix ϕ in Equation (3.73) is the state transition matrix. If we imagine
k
| sampling | a pure sinusoid | of the form    |         |     |     |
| -------- | --------------- | -------------- | ------- | --- | --- |
|          |                 | y(t) cos(ωt)+Y | sin(ωt) |     |     |
= Y
|     |     | c   | s   |     |     |
| --- | --- | --- | --- | --- | --- |
ω(cid:1)t ψ
at equal intervals corresponding to = then we could take the state to be
(cid:2) (cid:3)
Y c
x =
k Y
s

| Kalman    | filtering |      |            |         |         |     | 99  |
| --------- | --------- | ---- | ---------- | ------- | ------- | --- | --- |
| and since | the state | does | not change | in time |         |     |     |
|           |           |      |            | (cid:2) | (cid:3) |     |     |
1 0
ϕ
=
0 1
| In this case | H the | measurement |     | matrix would | be  |     |     |
| ------------ | ----- | ----------- | --- | ------------ | --- | --- | --- |
k
|     |     |     | H   | = [cos(kψ) | sin(kψ)] |     |     |
| --- | --- | --- | --- | ---------- | -------- | --- | --- |
k
| A second | possibility | is to | define  | the state as |                |         |     |
| -------- | ----------- | ----- | ------- | ------------ | -------------- | ------- | --- |
|          |             |       | (cid:2) |              | (cid:3)(cid:2) | (cid:3) |     |
|          |             |       |         | coskψ sinkψ  | Y              |         |     |
c
x =
|     |     |     | k   | −sinkψ coskψ | Y   |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | --- |
s
so that
|     |     |     |     | (cid:2) | (cid:3) |     |     |
| --- | --- | --- | --- | ------- | ------- | --- | --- |
|     |     |     |     | cosψ    | sinψ    |     |     |
|     |     |     | ϕ   | =       |         |     |     |
|     |     |     | k   | −sinψ   | cosψ    |     |     |
and
|     |     |     |     | H = [1 | 0]  |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- |
k
The Kalman filter assumes an initial (before the measurements are made) statistical
description of the state x, and recursively (as each measurement becomes available)
updates the estimate of state. The initial assumption about the state is that it is a
random vector independent of the processes w and ε and with a known mean and
k k
covariance matrix, P . The recursive calculation involves computing a gain matrix
0
| K . The | estimate | xˆ is given | by  |     |     |     |     |
| ------- | -------- | ----------- | --- | --- | --- | --- | --- |
k
|     |     | xˆ  | = ϕ | x +K [z | −H ϕ    | xˆ ] | (3.77) |
| --- | --- | --- | --- | ------- | ------- | ---- | ------ |
|     |     | k+1 | k   | k k+1   | k+1 k+1 | k k  |        |
The first term in Equation (3.77) is an update of the old estimate by the state
transition matrix while the second is the gain matrix multiplying the observation
residual. The bracketed term in Equation (3.77) is the difference between the actual
measurement, z , and the predicted value of the measurement, i.e. the residual
k
|     |     |     |     | φ   |     |     | φ   |
| --- | --- | --- | --- | --- | --- | --- | --- |
in predicting the measurement. That is, xˆ is the predicted state and H xˆ
|     |     |     |     | k   | k   |     | k+1 k k |
| --- | --- | --- | --- | --- | --- | --- | ------- |
is the predicted measurement. The computation of the gain matrix K k involves
the computation of two covariance matrices. The first is the covariance of the
one-step prediction denoted P(k+1|k). The second is the covariance of the error
in the estimate at time k, P(k|k). The first step in computing the gain matrix is to
| update the | covariance | for      | the one-step | prediction           |       |          |        |
| ---------- | ---------- | -------- | ------------ | -------------------- | ----- | -------- | ------ |
|            |            | P(k+1|k) |              | = φ P(k|k)φT+(cid:4) | Q     | (cid:4)T | (3.78) |
|            |            |          |              | k                    | k k k | k        |        |

| 100      |            |              |     | Mathematical | basis      | for protective | relaying | algorithms |
| -------- | ---------- | ------------ | --- | ------------ | ---------- | -------------- | -------- | ---------- |
| The gain | matrix can | be computed  |     | as           |            |                |          |            |
|          | K          | = P(k+1|k)HT |     | [H           | P(k+1|k)HT | +R             | ]−1      | (3.79)     |
|          | k+1        |              |     | k+1 k+1      |            | k+1            | k+1      |            |
The matrix that must be inverted in Equation (3.79) is of the dimension of the
measurements which typically is smaller than the number of states. In the line
relaying application, the state dimension is 2 while there is only one measurement.
In order to maintain the recursion an additional calculation is involved. The matrix
P(k+1|k+1) must be formed to be used in the next version of Equation (3.78).
|     |     | P(k+1|k+1) |     |        |           | ]P(k+1|k) |     |        |
| --- | --- | ---------- | --- | ------ | --------- | --------- | --- | ------ |
|     |     |            |     | = [I−K | k+1 H k+1 |           |     | (3.80) |
Alternategainexpressionsarefrequentlyuseful.ManyformsofEquations(3.78),
(3.79) and (3.80) can be obtained using the matrix inversion lemma given in
| Equation | (3.81)         |     |     |                   |     |     |     |        |
| -------- | -------------- | --- | --- | ----------------- | --- | --- | --- | ------ |
|          | (A−1+BTC−1B)−1 |     |     | A−ABT(BABT+C)−1BA |     |     |     |        |
|          |                |     |     | =                 |     |     |     | (3.81) |
If we write Equation (3.79) in a more compact notation as K = PHT(HPHT+R)−1
| and apply | the lemma | as in | Equation | (3.82) |     |     |     |     |
| --------- | --------- | ----- | -------- | ------ | --- | --- | --- | --- |
K=(P−1+HTR−1H)−1(P−1+HTR−1H)PHT(R+HPHT)−1
(3.82)
K=(P−1+HTR−1H)−1(HT+HTR−1HPHT)(R+HPHT)−1
K=(P−1+HTR−1H)−1HTR−1(HPHT+R)(R+HPHT)−1
K=(P−1+HTR−1H)−1HTR−1
Or
|     | K   | = [HT | R       | H +P−1(k+1|k)]−1HT |     |     | R       | (3.83) |
| --- | --- | ----- | ------- | ------------------ | --- | --- | ------- | ------ |
|     | k+1 |       | k+1 k+1 | k+1                |     |     | k+1 k+1 |        |
Substituting Equation (3.79) into Equation (3.80) with the same notation and
| employing | the lemma         | again |     |     |               |     |     |        |
| --------- | ----------------- | ----- | --- | --- | ------------- | --- | --- | ------ |
|           | P−PHT(HPHT+R)−1HP |       |     |     | (P+HTR−1+R)−1 |     |     |        |
|           | P =               |       |     |     | =             |     |     | (3.84) |
| Example   | 3.22              |       |     |     |               |     |     |        |
ItseemsappropriatetogiveacomparisonoftheKalmanestimatesandtheestimates
formed using the DFT algorithms. To do so, however, it is necessary to put the
algorithms on a common basis. The Kalman estimate assumes an initial estimate
and an initial covariance for that estimate, while the DFT algorithm does not.
Equations 3.78–3.80 are not convenient if there is no initial estimate. A form of

| Kalman | filtering |     |     |     |     |     |     |     | 101 |
| ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
theequationswhichisconvenientforthiscaseinvolvestheinverseofthecovariance
matrix P(k|k). If we define the inverse of the covariance matrix as
|     |     |     |     | F = | P(k|k)−1 |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
k
and assume that there is no random input to the system, i.e. Q = 0, then Equations
k
(3.78) and (3.79) can be rewritten in terms of an update of F as
k
|     |     |     |         | ϕ−TF | ϕ−1+HT |     | R−1 |     |        |
| --- | --- | --- | ------- | ---- | ------ | --- | --- | --- | ------ |
|     |     |     | F k+1 = | k    |        |     | H   | k+1 | (3.85) |
|     |     |     |         | k    | k      | k+1 | k+1 |     |        |
The advantage of Equation (3.82) is that F can be taken as zero. The matrix
0
F is referred to as the information matrix and can also be used to compute the
k
gain from
|     |     |     |     |           | = HT | R−1 |     |     |        |
| --- | --- | --- | --- | --------- | ---- | --- | --- | --- | ------ |
|     |     |     | F   | k+1 K k+1 |      |     |     |     | (3.86) |
k+1 k+1
Equation(3.85) makes itclear that,if theinitialF 0 iszero, wemust makeenough
measurements so that F is invertible before the gain matrix can be computed. In
k
the relaying problem, this is a manifestation of the fact that one measurement is
not sufficient to form an estimate of a phasor. If we take the form of the state
equation for the phasor given by ϕ = I and H = [cos(kψ)sin(kψ)], and assume
|      |            |           |         | k           |     | k      |         |     |     |
| ---- | ---------- | --------- | ------- | ----------- | --- | ------ | ------- | --- | --- |
| that | R = I, the | recursion | for the | information |     | matrix | becomes |     |     |
k
|     |       | (cid:2)            |            |     |     |                    |            |         | (cid:3) |
| --- | ----- | ------------------ | ---------- | --- | --- | ------------------ | ---------- | ------- | ------- |
|     |       |                    | cos2(k+1)ψ |     |     | cos(k+1)ψsin(k+1)ψ |            |         |         |
|     | F = F | +                  |            |     |     |                    |            |         |         |
|     | k+1 k | cos(k+1)ψsin(k+1)ψ |            |     |     |                    | sin2(k+1)ψ |         |         |
| or  |       |                    | (cid:2)    |     |     |                    |            | (cid:3) |         |
(cid:5)N
|     |     |     |     | cos2kψ |     | coskψsinkψ |     |     |     |
| --- | --- | --- | --- | ------ | --- | ---------- | --- | --- | --- |
F N =
|     |     |     |     | coskψsinkψ |     | sin2kψ |     |     |     |
| --- | --- | --- | --- | ---------- | --- | ------ | --- | --- | --- |
k=1
ϕ
Under the assumption that k = I, Q k = 0, R k = I, the recursions are
|     |     |     |     | =F−1 | HT  |     |     |     |        |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | ------ |
|     |     |     |     | K k  |     |     |     |     | (3.87) |
k k
|     |     |     |     | F =F | +HT | H   |     |     | (3.88) |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | ------ |
|     |     |     |     | k    | k−1 |     | k   |     |        |
k
| And | using Equation | (3.87) | in Equation |     | (3.77) |     |     |     |     |
| --- | -------------- | ------ | ----------- | --- | ------ | --- | --- | --- | --- |
∧
|     |                | xˆ     | =X     | + F−  | 1 HT    | [z −H | xˆ  | ]   |        |
| --- | -------------- | ------ | ------ | ----- | ------- | ----- | --- | --- | ------ |
|     |                |        | k k−1  |       | k k     | k     | k   | k−1 |        |
|     |                | xˆ     | =F−1[F | −HTH  | ]xˆ     | +HTz  |     | ]   |        |
|     |                |        | k k    | k     | k k     | k−1   | k k |     |        |
| and | using Equation | (3.85) |        |       |         |       |     |     |        |
|     |                |        | xˆ =   | F−1[F | xˆ      | +HTz  | ]   |     | (3.89) |
|     |                |        | k      | k     | k−1 k−1 |       | k k |     |        |

| 102      |        |     |             | Mathematical |       | basis | for      | protective | relaying | algorithms |
| -------- | ------ | --- | ----------- | ------------ | ----- | ----- | -------- | ---------- | -------- | ---------- |
| Equation | (3.89) | can | be repeated | to           | yield |       |          |            |          |            |
|          |        |     | xˆ = F−1[F  | x +HTz       |       | +HTz  | +···+HTz |            | ]        | (3.90)     |
|          |        |     | k           | o o          | 1 1   | 2 2   |          | k          | k        |            |
k
Equation (3.90) shows that if the initial information matrix is zero then the esti-
mate is formed as the weighted sum of the measurements (if F is zero then the
0
first term in the brackets is zero). The bracketed quantity in Equation (3.87) is
|     |     |     |     | (cid:26)(cid:10) |     | (cid:27) |     |     |     |     |
| --- | --- | --- | --- | ---------------- | --- | -------- | --- | --- | --- | --- |
cos(kψ)z
k
(cid:10)
sin(kψ)z
k
In other words, if there is no initial information and the measurement error has a
constant covariance then the Kalman filter estimate is a combination of DFT terms.
| The | particular | combination |     | depends | on the | matrix | F−1. |     |     |     |
| --- | ---------- | ----------- | --- | ------- | ------ | ------ | ---- | --- | --- | --- |
k
Ifthereareanevennumberofsamplesperhalfcycle,atmultiplesofahalfcycle,
ψ = π/2n,N = 2nm, i.e. m = 1 is a half cycle, m = 2 is a full cycle, m = 3 is 3
| half | cycles, | and |     |         |     |     |     |     |         |     |
| ---- | ------- | --- | --- | ------- | --- | --- | --- | --- | ------- | --- |
|      |         |     |     | (cid:2) |     |     |     |     | (cid:3) |     |
(cid:5)N
|     |     |     |     | cos2(kψ) |     | cos(kψ)sin(kψ) |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | -------------- | --- | --- | --- | --- |
=
|     |     | F   | N   | cos(kψ)sin(kψ) |     |     | sin2(kψ) |     |     | (3.91) |
| --- | --- | --- | --- | -------------- | --- | --- | -------- | --- | --- | ------ |
k=1
Then using
|     |     | 1+cos(2u) |     |     | 1−cos(2u) |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --------- | --- | --- | --- | --- | --- |
sin2u
|     | cos2u | =   |     | , sin2u | =   |     | , cosusinu |     | =   |     |
| --- | ----- | --- | --- | ------- | --- | --- | ---------- | --- | --- | --- |
|     |       |     | 2   |         |     | 2   |            |     | 2   |     |
With 2u = 2ψ = π/n and m = 1, N = 2n, the sums in Equation (3.91) involve a
|     | cos(π/n) |     | sin(π/n)     |        |              |           |     |     |     |     |
| --- | -------- | --- | ------------ | ------ | ------------ | --------- | --- | --- | --- | --- |
| sum | of       | or  |              | over a | full period. | Since     |     |     |     |     |
|     |          |     | (cid:5)2n    |        | (cid:5)2n    |           |     |     |     |     |
|     |          |     | cos(kπ/n)=0, |        |              | sin(kπ/n) |     | 0,  |     |     |
=
|     |     |     | k=1 |     | k=1               |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | (cid:12) (cid:13) |     |     |     |     |     |
N
|     |     |     |     | F = |     | I   |     |     |     | (3.92) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
N
2
|     |     |     |     |     |     |    |     |     |    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2(cid:10)nm
|     |     |     |     |     | (cid:12) (cid:13) | cos(kπ/2n)z |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | ----------- | --- | --- | --- | --- |
|     |     |     |     |     |                   |            |     |     | k  |     |
1
|     |     |     |     |      |     |  k = 1     |     |     |    |        |
| --- | --- | --- | --- | ---- | --- | ----------- | --- | --- | --- | ------ |
|     |     |     |     | xˆ = |     |  2(cid:10) |     |     |    | (3.93) |
nm nm
sin(kπ/2n)z
k
k=1
In fact, the Kalman filter estimate exactly corresponds to the Fourier estimates in
these situations.11 The estimates given by Equation (3.90) were first derived in a

| Problems |     |     |     |     |     |     | 103 |
| -------- | --- | --- | --- | --- | --- | --- | --- |
digital relaying context without reference to Kalman filtering. There are seen to be
two possible reasons to use the Kalman filter. They are: the existence of an initial
| estimate, | or non-constant |     | measurement |     | noise. |     |     |
| --------- | --------------- | --- | ----------- | --- | ------ | --- | --- |
3.10 Summary
In this chapter we have presented the background material needed to understand
relaying algorithms. We have examined the Fourier series and Fourier transform as
means of determining the frequency content of signals. In a digital relaying context
the discrete Fourier transform which takes samples of a signal and computes the
various harmonics is of particular importance. The Fourier transform sheds light on
the sampling process and explains the need for anti-aliasing filters.
Ideasofprobabilityandrandomprocessesarerequiredinordertoappreciatehow
various algorithms estimate the parameters of interest in the relaying application.
The view that the solution of an over-defined set of equations is an estimation
problem will be used extensively in Chapter 4. The Kalman filter has also been
applied in distance relaying. Our presentation of the Kalman filter makes it clear
that the primary use of the filter in relaying should be in situations where the mea-
surement noise does not have a constant covariance. When the measurement noise
has a constant covariance and when no prior knowledge of the state is assumed,
then the Kalman filter solution is equivalent to solutions obtained with other tech-
niques.
Problems
3.1 Determine whether each of the following signals is periodic. If so, give the
| fundamental |        | frequency. |           |     |     |     |     |
| ----------- | ------ | ---------- | --------- | --- | --- | --- | --- |
|             |        | ω          |           | 3ω  |     |     |     |
| (a)         | r(t) = | cos        | o t = sin | o t |     |     |     |
2
| (b) | r(t) = | cos πt      | + cos3t |       |     |     |     |
| --- | ------ | ----------- | ------- | ----- | --- | --- | --- |
|     |        | ω           |         | cos6ω |     |     |     |
| (c) | r(t) = | sin         | (t – 3) | +     | t   |     |     |
|     |        |             | o       |       | 4 o |     |     |
|     |        | ejω ot+sinω |         | cos1ω |     |     |     |
| (d) | r(t) = |             |         | o t + | o t |     |     |
2
3.2 Demonstrate the following consequences of Equation (3.9):
| (a) | If r(t) | is real | then | c −k = c | k   |     |     |
| --- | ------- | ------- | ---- | -------- | --- | --- | --- |
| (b) | If r(t) | is even | then | c = c    |     |     |     |
|     |         |         |      | k        | −k  |     |     |
| (c) | If r(t) | is odd  | then | c = −c   |     |     |     |
|     |         |         |      | k        | −k  |     |     |
(d) If r(t)is real and even then c = c = c∗ i.e. all c are pure real
|     |     |     |     |     | k −k | k   |     |
| --- | --- | --- | --- | --- | ---- | --- | --- |
k
(e) If r(t) is real and odd then c = −c = −c∗ i.e. all c are pure
|     |     |     |     |     | k −k | k   | k   |
| --- | --- | --- | --- | --- | ---- | --- | --- |
imaginary

| 104 |     |     |                |     | Mathematical | basis | for protective | relaying algorithms |
| --- | --- | --- | -------------- | --- | ------------ | ----- | -------------- | ------------------- |
| 3.3 | T>0 |     |                |     |              |       |                |                     |
|     | Let | be  | a fixed number |     |              |       |                |                     |
(a) Let x(t) be a signal which is zero for t ≤ 0 and t ≥ T. Show that the
|     | following |     | infinite | sum defines | a periodic |     | signal, | r(t) |
| --- | --------- | --- | -------- | ----------- | ---------- | --- | ------- | ---- |
n(cid:5)=∞
|     |     |     |     |     | r(t) = | x(t−nT) |     |     |
| --- | --- | --- | --- | --- | ------ | ------- | --- | --- |
n=−∞
(b) Let x(t) bea signal which is zero for t ≤ 0 and t ≥ T/2. Construct an even
|     | signal     | r(t)    | such that |            |     |     |     |     |
| --- | ---------- | ------- | --------- | ---------- | --- | --- | --- | --- |
|     | i.         | r(t) is | periodic  |            |     |     |     |     |
|     | ii.        | r(t) =  | x(t) for  | 0 ≤ t ≤    | T/2 |     |     |     |
|     | (c) Repeat | (b)     | for an    | odd signal |     |     |     |     |
3.4 (a) Find the Fourier series coefficients {c } for the signal
k
|     |     |     |     | r(t) | |cos(cid:3)t|;(cid:3)>0 |     | <   | <   |
| --- | --- | --- | --- | ---- | ----------------------- | --- | --- | --- |
|     |     |     |     | =    |                         |     | −∞  | t ∞ |
(b) Write the Fourier series for r(t) in complex exponential form and in sine
|     | and        | cosine | form.      |     |            |          |     |     |
| --- | ---------- | ------ | ---------- | --- | ---------- | -------- | --- | --- |
| 3.5 | Given that | an     | LTI system | has | an impulse | response |     |     |
u(t)e−tcost
h(t) =
|     | Find the | response | of       | the system | to the       | input    |       |     |
| --- | -------- | -------- | -------- | ---------- | ------------ | -------- | ----- | --- |
|     |          |          |          | w(t)       | = sint;−∞    | <        | t < ∞ |     |
| 3.6 | An LTI   | system   | is known | to         | have impulse | response |       |     |
|     |          |          |          |            | h(t)         | u(t)e−4t |       |     |
=
Determinetheresponse,y(t),ofthesystemtotheinputw(t)=ejωt.Sketch
(a)
|     | the | magnitude | of  | the response | as  | a function | of ω. |     |
| --- | --- | --------- | --- | ------------ | --- | ---------- | ----- | --- |
(b) FindtheFourierseriescoefficientsoftheoutputiftheinputisr(t)from3.3
|     | (c) Is the | output | an even | function | of  | time? |     |     |
| --- | ---------- | ------ | ------- | -------- | --- | ----- | --- | --- |
3.7 Letr(t)beaperiodicsignalwithafundamentalperiodT andfundamentalfre-
o
|     |     | ω   | 2π/T |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- |
quency of = Let c denote the kth Fourier series coefficient of r(t).
|     |     | o   |     | o   | k   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Findformulasintermsofc forthekth Fouriercoefficientsd ory(t)where
|     |          |         |       | k   |     |     |     | k   |
| --- | -------- | ------- | ----- | --- | --- | --- | --- | --- |
|     | (a) y(t) | = r(−t) |       |     |     |     |     |     |
|     | (b) y(t) | = r(t   | – t ) |     |     |     |     |     |
1
dr
|     | (c) y(t) | =   | (assuming | r(t) | is differentiable) |     |     |     |
| --- | -------- | --- | --------- | ---- | ------------------ | --- | --- | --- |
dt

| Problems |     |     |     |     |     |     |     |     | 105 |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Xˆ(ω)
| 3.8 | Find the | Fourier | transforms |     | of each | signal | x(t) |     |     |
| --- | -------- | ------- | ---------- | --- | ------- | ------ | ---- | --- | --- |
(cid:14)
|     |          | cost     | |t| ≤ 1        |     |      |     |     |     |     |
| --- | -------- | -------- | -------------- | --- | ---- | --- | --- | --- | --- |
|     | (a) x(t) | =        |                |     |      |     |     |     |     |
|     |          |          | |t| (cid:12) = | (t) |      |     |     |     |     |
|     |          | 0        | 1              | P 1 | cost |     |     |     |     |
|     | x(t)     |          | (t)            |     |      |     |     |     |     |
|     | (b)      | = e−|t|P |                |     |      |     |     |     |     |
1
1
|     | (c) x(t) | = Pa | (t) |     |     |     |     |     |     |
| --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |          | a 2  |     |     |     |     |     |     |     |
3.9 An LTI system designed to ‘smooth’ input signals has the following output
|     | when w(t) | is the | input |     |     |     |     |     |     |
| --- | --------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
t(cid:4)+a/2
|     |     |     | y(t) |     | w(τ)dτ−∞ |     |                       |     |     |
| --- | --- | --- | ---- | --- | -------- | --- | --------------------- | --- | --- |
|     |     |     | =    |     |          |     | (cid:17) t (cid:17) ∞ |     |     |
t−a/2
|      | Find the | frequency  | response | of the | system. |     |     |     |     |
| ---- | -------- | ---------- | -------- | ------ | ------- | --- | --- | --- | --- |
| 3.10 | Consider | the signal |          |        |         |     |     |     |     |
|      |          |            |          | x(t)   |         | < π |     |     |     |
= sint;|t|
0;|t|>π
∧
(ω)
|     | (a) Find | X           | by direct integration |     |     |     |     |     |     |
| --- | -------- | ----------- | --------------------- | --- | --- | --- | --- | --- | --- |
|     | (b) let  | x(t) = sint | pπ (t) where          |     |     |     |     |     |     |
2sinπω
pπ (t)↔ F
ω
∧
|     | Find | (ω) | using the modulation |     | rule. |     |     |     |     |
| --- | ---- | --- | -------------------- | --- | ----- | --- | --- | --- | --- |
X
(cid:16) (cid:17)
1 t2
−
| 3.11 | Let x(t) | = e 2             | T         |         |     |     |          |      |        |
| ---- | -------- | ----------------- | --------- | ------- | --- | --- | -------- | ---- | ------ |
|      |          |                   | ∧         |         | ∧   |     |          |      | ∧      |
|      | (a) Show | that              | d [X (ω)] | = −ωT2X | (ω) | and | conclude | that | X (ω)= |
|      |          | (cid:12) (cid:13) | dω        |         |     |     |          |      |        |
ω2T2
−
|     | Ke        | 2    | for some constant |          | K.   |     |        |     |     |
| --- | --------- | ---- | ----------------- | -------- | ---- | --- | ------ | --- | --- |
|     |           |      | (cid:9)           |          |      |     | √      |     |     |
|     |           |      | ∞                 | √        |      |     |        |     |     |
|     | (b) Given | that | e−τ2 dτ           | = π,show | that | K   | = T 2π |     |     |
−∞
3.12 Recall that given a signal, x(t), we may write x(t) uniquely as the sum of an
|     | even signal | x (t) | and an odd | signal | x (t) |     |     |     |     |
| --- | ----------- | ----- | ---------- | ------ | ----- | --- | --- | --- | --- |
|     |             | e     |            |        | o     |     |     |     |     |
1
|     |     |     | x   | (t)= | [x(t)+x(−t)] |     |     |     |     |
| --- | --- | --- | --- | ---- | ------------ | --- | --- | --- | --- |
e
2
1
|     |     |     | x   | (t)= | [x(t)−x(−t)] |     |     |     |     |
| --- | --- | --- | --- | ---- | ------------ | --- | --- | --- | --- |
o
2

| 106 |     |     |     | Mathematical | basis for | protective | relaying algorithms |
| --- | --- | --- | --- | ------------ | --------- | ---------- | ------------------- |
∧ (ω),
(a) If x(t) is real-valued and has Fourier transform X show that
|     |     |     |     | ∧    | ∧          |     |     |
| --- | --- | --- | --- | ---- | ---------- | --- | --- |
|     |     |     |     | Re{X | (ω)}=X (ω) |     |     |
e
|     |     |     |     | ∧    | ∧        |     |     |
| --- | --- | --- | --- | ---- | -------- | --- | --- |
|     |     |     |     | Im{X | (ω)}=−jX | (ω) |     |
o
(b) Suppose that x(t) is causal, i.e. x(t) = 0 for t< 0. Assume that F−1 exists
|     | ∧       |     | ∧    |           |     |     |     |
| --- | ------- | --- | ---- | --------- | --- | --- | --- |
|     | for (ω) | and | (ω). | Show that |     |     |     |
|     | X e     |     | X o  |           |     |     |     |
(cid:4)∞
|     |     |     |       | 2    | ∧             |     |            |
| --- | --- | --- | ----- | ---- | ------------- | --- | ---------- |
|     |     |     | x(t)= |      | (ω)}cosωtdω;t |     |            |
|     |     |     |       | Re{X |               |     | (cid:12) 0 |
π
0
(cid:4)∞
|     |     |     |       | 2    | ∧           |            |     |
| --- | --- | --- | ----- | ---- | ----------- | ---------- | --- |
|     |     |     | x(t)= | Im{X | (ω)}sinωt;t | (cid:12) 0 |     |
π
0
thatis,acausalsignalmaybedeterminedfromeithertherealorimaginary
|     | part of | its Fourier | transform. |     |     |     |     |
| --- | ------- | ----------- | ---------- | --- | --- | --- | --- |
3.13 Suppose that a certain linear time-invariant system has response
|     |     |     |     | y(t) [6e−4t−6e−5t]u(t) |     |     |     |
| --- | --- | --- | --- | ---------------------- | --- | --- | --- |
=
|     | to the input       |     |          |                          |         |     |     |
| --- | ------------------ | --- | -------- | ------------------------ | ------- | --- | --- |
|     |                    |     |          | w(t) = [3e−5t−2e−4t]u(t) |         |     |     |
|     | Find the frequency |     | response | of the                   | system. |     |     |
3.14 (a) Find the impulse response of the linear time-invariant system whose fre-
|     | quency | response | is  |     |     |     |     |
| --- | ------ | -------- | --- | --- | --- | --- | --- |
∧
|     |     |     | (ω) | = A e−αω2 | e−jωt1;−∞ | (cid:17) ω | (cid:17) ∞ |
| --- | --- | --- | --- | --------- | --------- | ---------- | ---------- |
|     |     |     | H   | o         |           |            |            |
this system might be called an ideal linear phase Gaussian filter.
|     | (b) Is the | system | causal? |     |     |     |     |
| --- | ---------- | ------ | ------- | --- | --- | --- | --- |
3.15 The signal shown in Figure P3.15a has Fourier transform given by
4sin2ω
∧
|     |     |     |     | X (ω) | =   |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     | o     | ω2  |     |     |
without integrating, find the transforms of the following signals:
|     | (a) The signal | shown  | in     | Figure P3.15b |     |     |     |
| --- | -------------- | ------ | ------ | ------------- | --- | --- | --- |
|     | (b) x (t) =    | tx (t) |        |               |     |     |     |
|     | 2              | o      |        |               |     |     |     |
|     | (c) x (t) =    | x (t)  | sinω t |               |     |     |     |
|     | 3              | o      | o      |               |     |     |     |

| Problems |       |     |     |       | 107 |
| -------- | ----- | --- | --- | ----- | --- |
|          | x (t) |     |     | x (t) |     |
|          | 0     |     |     | 1     |     |
2
2
| −2  |     | 2 t −5       | −3 −1               | 1 3  | 5 t |
| --- | --- | ------------ | ------------------- | ---- | --- |
|     | (a) |              |                     | (b)  |     |
|     |     | Figure P3.34 | Signals for Problem | 3.15 |     |
3.16
| Find | the transforms | of  |     |     |     |
| ---- | -------------- | --- | --- | --- | --- |
4sin2t
x(t)
| (a) | =   |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
t2
1
| (b) x(t) | =   | +πδ(t) |     |     |     |
| -------- | --- | ------ | --- | --- | --- |
jt
| 3.17 Suppose | x (t) | and x (t) are | signals such that |     |     |
| ------------ | ----- | ------------- | ----------------- | --- | --- |
|              | 1     | 2             |                   |     |     |
∧
|     |     | (ω)=0 | |ω| ω      |     |     |
| --- | --- | ----- | ---------- | --- | --- |
|     |     | X 1   | (cid:12) 1 |     |     |
∧
|     |     | X (ω)=0 | |ω| (cid:12) ω | (ω (cid:12) ω ) |     |
| --- | --- | ------- | -------------- | --------------- | --- |
|     |     | 2       | 2              | 2 1             |     |
Find the minimum sampling rate necessary to represent y(t) exactly, when
| (a) y(t)= | x   | (t)+x (t) |     |     |     |
| --------- | --- | --------- | --- | --- | --- |
|           | 1   | 2         |     |     |     |
| y(t)=     |     | (t) (t)   |     |     |     |
| (b)       | x   | ∗ x       |     |     |     |
|           | 1   | 2         |     |     |     |
y(t)= (t)x (t)
| (c) | x 1 | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- |
3.18 Recovering an approximation of a signal x(t) from a sampled version may be
viewed as a process of interpolation. That is, given x(nT), −∞ < n < ∞, T
x˜(t)
| fixed, | find an | approximation | to x(t), where |     |     |
| ------ | ------- | ------------- | -------------- | --- | --- |
n(cid:5)=∞
|     |     | x˜(t) | x(nT)h(t−nT) |     |     |
| --- | --- | ----- | ------------ | --- | --- |
=
n=−∞
|     |     | x(t) |     | h(t) |     |
| --- | --- | ---- | --- | ---- | --- |
1
|     |     |     | t −T | T t |     |
| --- | --- | --- | ---- | --- | --- |
|     |     | (a) |      | (b) |     |
Figure P3.35 (a) A signal to be interpolated. (b) h(t) for linear interpolation

| 108 |     | Mathematical | basis for protective | relaying algorithms |
| --- | --- | ------------ | -------------------- | ------------------- |
|     |     |              | as| | → ∞.           |                     |
where h(t) is afunction which goes to zero t Let x(t) beas shown
| in Figure | P3.18a. |     |     |     |
| --------- | ------- | --- | --- | --- |
(a) Sketch the zero-order hold interpolation x˜(t) when h(t) = p (t).
T/2
x˜(t)
(b) Sketch the linear interpolation when h(t) is as shown in P3.18b.
References
[1] Papoulis, A. The FourierIntegralanditsApplication, McGraw-Hill, 1961.
[2] Oppenheim, A.V. and Willsky A.S. (1983) SignalsandSystems, Prentice-Hall.
[3] Lathi, B.P. (1987) SignalsandSystems, Berkeley-Cambridge.
| [4] Papoulis, | A. (1977) SignalAnalysis, | McGraw-Hill. |     |     |
| ------------- | ------------------------- | ------------ | --- | --- |
[5] Rabiner,L.R.andGold,B.(1975)TheoryandApplicationofDigitalSignalProcessing,
McGraw-Hill.
[6] Openheimer,A.V.andSchaefer,R.W.(1975)DigitalSignalProcessing,Prentice-Hall.
[7] Helstrom, C.W. (1984) Probability and Stochastic Processes for Engineers, Macmil-
lian.
[8] Anderson, B.D.O. and Moore, J.B. (1979) OptimalFiltering, Prentice-Hall.
| [9] Gelb, | A. (1974) AppliedOptimalEstimation, |     | MIT Press. |     |
| --------- | ----------------------------------- | --- | ---------- | --- |
[10] Meditch,J.S.(1969)StochasticOptimalLinearEstimationandControl,McGraw-Hill.
[11] Thorp,J.S.,Phadke,A.G.,Horowitz,S.H.andBeehier,J.E.(1979)Limitstoimpedance
| relaying, | IEEE Trans. on PAS, | vol. 98, | no. 1, pp. 246–260. |     |
| --------- | ------------------- | -------- | ------------------- | --- |

4
| Digital | filters |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- |
4.1 Introduction
The material in Chapter 3 concerning Fourier transforms, random processes, and
analog filtersisprimarilycast in continuous time. Much of the subsequent literature
has been focused on the application of techniques from digital signal processing.
This chapter parallels Chapter 3 with an emphasis on some of these topics, includ-
ing: discrete time signals and systems, the design of digital filters and windowing.
The chapter concludes with wavelet transforms, artificial neural networks, and an
introduction to decision trees and agents. Some of the later ideas have yet to be
applied on a large scale but they represent a dramatic shift from the early reluc-
tance to use computers in protection to an embrace of many new approaches to
these problems.
| 4.2 Discrete | time | systems |     |     |     |
| ------------ | ---- | ------- | --- | --- | --- |
The processes and operations that digital relays perform on the samples of voltage
and current can be regarded as manifestations of discrete time systems. To under-
stand such systems we need first to examine the notation and definitions that are
used with discrete time signals. As in Section 3.6, we will use the notation x[n] for
| a function                        | with integer | arguments.  |                   |          |       |
| --------------------------------- | ------------ | ----------- | ----------------- | -------- | ----- |
| Example                           | 4.1          |             |                   |          |       |
| The discrete                      | time step    | and impulse | are given by      |          |       |
|                                   |              |             | (cid:14)          | (cid:15) |       |
|                                   |              |             | 1; n ≥            | 0        |       |
|                                   |              | x[n] = u[n] | =                 |          | (4.1) |
|                                   |              |             | 0; n <            | 0        |       |
| ComputerRelayingforPowerSystems2e |              |             | byA.G.PhadkeandJ. | S.Thorp  |       |
2009JohnWiley&Sons,Ltd

| 110            |                  |     |      |          |          | Digital      | filters |
| -------------- | ---------------- | --- | ---- | -------- | -------- | ------------ | ------- |
|                |                  |     |      |          | (cid:14) | (cid:15)     |         |
|                |                  |     |      |          | 1;       | n = 0        |         |
|                |                  |     | x[n] | = δ[n] = |          |              | (4.2)   |
|                |                  |     |      |          | 0;       | n (cid:6)= 0 |         |
| Note that δ[n] | = u[n]−u[n−1]    |     |      |          |          |              |         |
| A discrete     | time exponential |     | is   |          |          |              |         |
|                |                  |     |      | x[n]     | = zn     |              |         |
0
Where z is any complex number. Then |zn| grows for |z |>1 and decays for
0 0
0
| |z | < 1 and | if  |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- |
0
ej(cid:3)
|     |     |     |     | x[n] | =   |     | (4.3) |
| --- | --- | --- | --- | ---- | --- | --- | ----- |
thenx[n]isadiscretetimesinusoid.Discretetimesignalsarecausaliftheyarezero
for negative arguments, i.e. x[n] = 0, n < 0 and time limited if they are confined
| to an interval,    | i.e. | for some | n <      | n           |           |             |       |
| ------------------ | ---- | -------- | -------- | ----------- | --------- | ----------- | ----- |
|                    |      |          | 1        | 2           |           |             |       |
|                    |      |          |          | <           |           | n>n         |       |
|                    |      |          | x[n] =   | 0 n         | n and     |             | (4.4) |
|                    |      |          |          |             | 1         | 2           |       |
| Just as in Section |      | 3.2, a   | discrete | time signal | is        | periodic if |       |
|                    |      |          |          | x[n] =      | x[n+N]    |             |       |
| for some N.        |      |          |          |             |           |             |       |
| 4.2.1 Operations   |      | on       | discrete | time        | sequences |             |       |
Given any two discrete time sequences x [n] and x [n] the following operations are
|     |     |     |     | 1   |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
defined
|     |     | z[n]=x  | [n]+x | [n] addition   |     |             | (4.5) |
| --- | --- | ------- | ----- | -------------- | --- | ----------- | ----- |
|     |     |         | 1     | 2              |     |             |       |
|     |     | z[n]=cx | [n]   | multiplication |     | by a scalar |       |
1
|     |     | z[n]=x     | [n]x | [n] multiplication |       | of sequences |     |
| --- | --- | ---------- | ---- | ------------------ | ----- | ------------ | --- |
|     |     |            | 1    | 2                  |       |              |     |
|     |     | z[n]=x[n−n |      | 0 ] time           | shift |              |     |
4.2.2 Convolution
An important operation involving two sequences is discrete time convolution
[n]∗x
| x [n] | defined | by  |         |          |        |       |       |
| ----- | ------- | --- | ------- | -------- | ------ | ----- | ----- |
| 1 2   |         |     |         | (cid:5)∞ |        |       |       |
|       |         |     | x [n]∗x | [n] =    | x [k]x | [n−k] | (4.6) |
|       |         |     | 1 2     |          | 1      | 2     |       |
k=−∞

| Discrete time | systems |     |     |     |     |     | 111 |
| ------------- | ------- | --- | --- | --- | --- | --- | --- |
X [k]
2
X 1 [k]
−2 −1
|     |     | 0 1 2 | 3   | k   | 0 1 2 3 | k   |     |
| --- | --- | ----- | --- | --- | ------- | --- | --- |
X [n-k]
2
|     |     | X 1 [k]    |          |                  | n   |     |     |
| --- | --- | ---------- | -------- | ---------------- | --- | --- | --- |
|     |     | −2 −1      | 0 1      | 2                | k   |     |     |
|     |     | Figure 4.1 | Discrete | time convolution |     |     |     |
Equation (4.6) is the discrete equivalent of continuous time operation is
Section 3.5. The terms inside the summation are shown in Figure 4.1. The
sequence x 1 [k] is fixed while the sequence x 2 [n−k] is x 2 [k] time reversed and
| shifted so | the origin      | is at k = n. |           |              |     |     |     |
| ---------- | --------------- | ------------ | --------- | ------------ | --- | --- | --- |
| Example    | 4.2 Convolution | of a         | step with | a step       |     |     |     |
|            |                 | x            | 1 [n]=x   | 2 [n] = u[n] |     |     |     |
(cid:5)∞
u[n]∗u[n]=
u[k]u[n−k]
k=−∞
(cid:5)∞
u[n]∗u[n]=
u[n−k]
k=0
(cid:5)n
|     |     | u[n]∗u[n]= |     | ≥    |     |     |     |
| --- | --- | ---------- | --- | ---- | --- | --- | --- |
|     |     |            |     | 1n 0 |     |     |     |
k=0
|     |     |     | =0  | n < 0 |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- |
u[n]∗u[n]=(n+1)u[n]

| 112 |     |     |      |     |      | Digital | filters |
| --- | --- | --- | ---- | --- | ---- | ------- | ------- |
|     |     |     | x[n] |     | y[n] |         |         |
System
|              |     |              | Figure 4.2 | Discrete | time | system |     |
| ------------ | --- | ------------ | ---------- | -------- | ---- | ------ | --- |
| 4.3 Discrete |     | time systems |            |          |      |        |     |
A discrete time system operates on an input discrete time sequence to produce
another discrete time sequence as an output, as shown in Figure 4.2. The system is
linear if for any pair of inputs y [n] and y [n] with corresponding outputs x [n] and
|     |     |     | 1   | 2   |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
x [n], the input y [n]+y [n] produces the output x [n]+x [n]. Thesystem istime
| 2   |     | 1   | 2   |     |     | 1 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
invariant if for any input y[n] with output x[n], the input y[n−n 0 ] produces the
output x[n−n ]. The system is causal if the output x[n] depends only on the input
0
y[m]form ≤ n.Justasincontinuous time,convolutionwithanimpulsereproduces
| the signal, | i.e. |     |     |     |     |     |     |
| ----------- | ---- | --- | --- | --- | --- | --- | --- |
(cid:5)∞
|     |     | y[n]∗δ[n] | =   | y[k]δ[n−k] |     | = y[n] | (4.7) |
| --- | --- | --------- | --- | ---------- | --- | ------ | ----- |
k=−∞
Combining the facts in the preceding paragraph we can characterize a linear time
invariant system by its response to a unit impulse. If the response of a linear time
δ[n]
invariant system to a unit impulse is h[n] as shown in Figure 4.3 then the
response to any input y[n] is x[n] = y[n]∗h[n]. This can be established by writing
| the input y[n] | as  | a convolution | with | an impulse |     |     |     |
| -------------- | --- | ------------- | ---- | ---------- | --- | --- | --- |
(cid:5)∞
|     |     |     | y[n] | =   | y[k]δ[n−k] |     | (4.8) |
| --- | --- | --- | ---- | --- | ---------- | --- | ----- |
k=−∞
The output x[n] then, using linearity, is the sum of the responses to the shifted
| impulses inside | the | sum | or  |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
(cid:5)∞
|     |     |     | x[n] = |     | y[k]h[n−k] |     | (4.9) |
| --- | --- | --- | ------ | --- | ---------- | --- | ----- |
k=−∞
|     | δ[n] |        | h[n]         |      |         |                  |     |
| --- | ---- | ------ | ------------ | ---- | ------- | ---------------- | --- |
|     |      |        |              | x[n] |         | y[n] = x[n]*h[n] |     |
|     |      | System |              |      | System  |                  |     |
|     |      | Figure | 4.3 Discrete | time | impulse | response         |     |

| Z Transforms |     |     |     | 113 |
| ------------ | --- | --- | --- | --- |
h[n−k]
Note that the time invariance property is used in writing as the response
to δ[n−k].
Discrete time systems fall into two large classes, the first is those in which the
impulse response is limited in duration so that the output only depends on a finite
| number of previous | inputs as | in Equation         | (4.10). |        |
| ------------------ | --------- | ------------------- | ------- | ------ |
|                    | x[n] = a  | y[n]+a y[n−1]+···+a | y[n−k]  | (4.10) |
|                    | 0         | 1                   | k       |        |
The second is those for which the output depends on all previous input values. The
first are designated Finite Impulse Response (FIR) while the second are designated
as Infinite Impulse Response (IIR). If we cast a relaying algorithm as a discrete
time system or a digital filter it will be an FIR filter since the number of past
samples of the input that can be used in making a decision must be finite. We will
encounter IIR filters, however, in examining equivalences between continuous time
| and discrete time | filters. |     |     |     |
| ----------------- | -------- | --- | --- | --- |
| 4.4 Z Transforms  |          |     |     |     |
| 4.4.1 Power       | series   |     |     |     |
Consider a power series of the form of Equation (4.11) where w is a complex
variable.
n(cid:5)=∞
|     |     | f(w) = | c wn | (4.11) |
| --- | --- | ------ | ---- | ------ |
n
n=−∞
The series will converge for some values of w. A simple example is given in
| Equation (4.12). |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
n(cid:5)=N
|     | f(w) = | wn = 1+w+w2+···wN |     | (4.12) |
| --- | ------ | ----------------- | --- | ------ |
n=0
(1+w+w2+···wN)(1−w)=1+w+w2+···wN−(w+w2+···wN+1)
=1−wN+1
or
n(cid:5)=N
1−wN+1
|     | f(w) | = wn | =   | (4.13) |
| --- | ---- | ---- | --- | ------ |
1−w
n=0
Beingafinitesum,theseriesinEquation(4.12)convergesforallw.Theexpression
=
inEquation(4.13)mustbeevaluatedcarefullyatw 1butuseofL’Hospital’srule

| 114 |     |     |     |     |     |     | Digital | filters |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- |
givesf(1) = N+1whichisobviouslycorrect.IfweletN → ∞inEquation(4.13)
it is necessary that |w| < 1 for the series to converge In general the sum in form
of Equation (4.14) converges in a disk given by Equation (4.15) which is referred
| to  | as the | ratio test. |     |     |     |     |     |     |
| --- | ------ | ----------- | --- | --- | --- | --- | --- | --- |
(cid:5)∞
|     |     |     |     |     | f(w)= |     | c wn | (4.14) |
| --- | --- | --- | --- | --- | ----- | --- | ---- | ------ |
n
n=0
|     |     |     |     |     |     |     | (cid:11) (cid:11) |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- |
|     |     |     |     |     |     |     | (cid:11) (cid:11) |     |
c
|     |     |     |     |     | <   | <   | (cid:11) n (cid:11)   |        |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | ------ |
|     |     |     |     |     | |w| | R   | lim (cid:11) (cid:11) | (4.15) |
|     |     |     |     |     |     |     | n→∞ c                 |        |
n+1
If R = 0 the sum does not converge for any value of w. R is called the radius of
convergence.
| Example |     | 4.3 Ratio | tests |     |     |     |     |     |
| ------- | --- | --------- | ----- | --- | --- | --- | --- | --- |
(cid:10)∞
|     | (w) |     |      |     |       | n   |     |     |
| --- | --- | --- | ---- | --- | ----- | --- | --- | --- |
| (a) | f   | =   | nwn; | R   | = lim |     | = 1 |     |
|     | a   |     |      |     |       | n+1 |     |     |
|     |     | n=0 |      |     | n→∞   |     |     |     |
(cid:10)∞
|     | (w)     |       | 1 wn;        |     |             | (n+1)! |     |     |
| --- | ------- | ----- | ------------ | --- | ----------- | ------ | --- | --- |
| (b) | f       | =     |              |     | R = lim     |        | = ∞ |     |
|     | b       |       | n!           |     |             |        | n!  |     |
|     |         | n=0   |              |     | n→∞         |        |     |     |
| In  | fact, f | (w) = | ez converges |     | everywhere. |        |     |     |
b
| 4.4.2 | Z   | Transforms |     |     |     |     |     |     |
| ----- | --- | ---------- | --- | --- | --- | --- | --- | --- |
The z transform is the discrete time equivalent of the Laplace transform and is
| given | by  | Equation | (4.16) | for | the sequence |     | h[n] |     |
| ----- | --- | -------- | ------ | --- | ------------ | --- | ---- | --- |
(cid:5)∞
|     |     |     |     |     | H(z) | =   | h[n]z−n | (4.16) |
| --- | --- | --- | --- | --- | ---- | --- | ------- | ------ |
n=−∞
If the transform exists it is defined in an annual region referred to as the region of
| convergence |     | in  | the z-plane | defined |     | by    |     |        |
| ----------- | --- | --- | ----------- | ------- | --- | ----- | --- | ------ |
|             |     |     |             |         |     | < |z| | <   |        |
|             |     |     |             |         | R   | −     | R + | (4.17) |
= 1/w
Note the negative exponent on z in Equation (4.16). Letting z in the ratio
test in preceding section establishes that R+ comes from the limit as n → ∞ and
| R-  | comes | from | the limit | as n | → −∞. |     |     |     |
| --- | ----- | ---- | --------- | ---- | ----- | --- | --- | --- |

Z Transforms 115
Example 4.4 Z Transforms
(a) The unit step h[n] = 1, n = 0,1,2...(using Equation 4.13 and z = 1/w)
(cid:5)∞
1 z
H(z) = z−n = = ;|z| < 1
1−(1/z) z−1
0
(b) The discrete unit ramp h[n] = nu[n] (differentiating 4.4a with respect to z and
multiplying by −z)
(cid:5)∞
1 z
(cid:5)∞
−z z2
− nz−n−1 = − nz−n = +
z−1 (z−1)2 z−1 (z−1)2
0 0
(cid:5)∞
z
H(z)= nz−n = ;|z| < 1
(z−1)2
0
(c) A sampled exponential h[n] = u[n]e−anT (using Equation (4.13) and zeaT =
(1/w))
(cid:5)∞ (cid:5)∞
zeaT z
H(z) = e−aTnz−n = (e−aTz−1)n = = ;|z| < |e−aT|
zeaT−1 z−e−aT
0 0
If β = e−aT,h[n] = u[n]βn and H(z) = z ;|z| < |β|
z−β
4.4.3 Inverse Z transforms
The inverse z transform is given by Equation 4.18 where the integration is along a
counterclockwise curve in the region of convergence.
(cid:28)
1
h[n] = H(z)zn−1dz (4.18)
2πj
C
Equations (4.16) and (4.18) constitute a z transform pair. The ROC in
Equation (4.17) and the path of integration in Equation (4.18) are an important
part of the relationship.

| 116 |     |     |     |     |     |     |     | Digital | filters |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- |
For rational functions, especially with simple pole, the use of partial fractions
offers a convenient alternative to the integration in Equation (4.18). Given a ratio-
nal function, H(z), with distinct poles and numerator of lower degree than the
| denominator | write | a   | partial fraction | expansion |       | for | H(z)/z |     |        |
| ----------- | ----- | --- | ---------------- | --------- | ----- | --- | ------ | --- | ------ |
|             | H(z)  |     | (cid:5) α        |           |       |     | H(z)   |     |        |
|             |       | =   |                  | k ;       | where | α = | (z−β ) | |   | (4.19) |
|             |       |     | (z−              | β )       |       | k   | k      | z→β |        |
|             |       | z   |                  |           |       |     |        | z k |        |
|             |       |     | k                | k         |       |     |        |     |        |
Repeatedpoles andnumerators of higher order than thedenominator canbeaccom-
modated as in Laplace transforms. The division by z before the partial fraction
| expansion | gives | the desired | form | for     | the expansion |     | of H(z). |     |     |
| --------- | ----- | ----------- | ---- | ------- | ------------- | --- | -------- | --- | --- |
|           |       |             |      | (cid:5) |               |     | (cid:5)  |     |     |
α z
|     |     |     | H(z) |      | k   |        | α βk |     |        |
| --- | --- | --- | ---- | ---- | --- | ------ | ---- | --- | ------ |
|     |     |     | =    |      | ;   | h[n] = |      |     | (4.20) |
|     |     |     |      | (z−β | )   |        | k    |     |        |
k
|                  |     |     |                 | k   |     |     | k   |     |     |
| ---------------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| 4.4.4 Properties |     |     | of Z transforms |     |     |     |     |     |     |
With the notation as in Chapter 3 for Fourier transforms shown in Equation (4.21)
the properties of z transforms have direct counterparts with the properties of the
| Fourier transform |     | in  | Chapter | 3.    |     |      |     |     |        |
| ----------------- | --- | --- | ------- | ----- | --- | ---- | --- | --- | ------ |
|                   |     |     |         |       | z   | H(z) |     |     |        |
|                   |     |     |         | h[n]↔ |     |      |     |     | (4.21) |
P1) Linearity
If
|     |     |     |     | [n]↔ | z   | (z) |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     |     |     | h 1  |     | H 1 |     |     |     |
and
z
|     |     |     |     | h [n]↔ |     | H (z) |     |     |     |
| --- | --- | --- | --- | ------ | --- | ----- | --- | --- | --- |
|     |     |     |     | 2      |     | 2     |     |     |     |
then
|          |          |     |               | [n]↔  | z   | (z)+c | (z)   |     |        |
| -------- | -------- | --- | ------------- | ----- | --- | ----- | ----- | --- | ------ |
|          |          |     | c 1 h 1 [n]+c | 2 h 2 | c   | 1 H 1 | 2 H 2 |     | (4.22) |
| P2) Time | shifting |     |               |       |     |       |       |     |        |
If
|     |     |     |     |        | z   | (z) |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     | h [n]↔ |     | H   |     |     |     |
|     |     |     |     | 1      |     | 1   |     |     |     |
then
|                     |     |     |     |        | z   | z−n0H (z) |     |     |        |
| ------------------- | --- | --- | --- | ------ | --- | --------- | --- | --- | ------ |
|                     |     |     |     | h [n−n | ]↔  |           |     |     | (4.23) |
|                     |     |     |     | 1      | 0   | 1         |     |     |        |
| P3) Differentiation |     | in  | z   |        |     |           |     |     |        |
If
z
|     |     |     |     | h [n]↔ |     | H (z) |     |     |     |
| --- | --- | --- | --- | ------ | --- | ----- | --- | --- | --- |
|     |     |     |     | 1      |     | 1     |     |     |     |

| Z Transforms |     |     |     |     |     | 117 |
| ------------ | --- | --- | --- | --- | --- | --- |
then
z d
|     |     |     | (n−1)h [n−1]↔ | −   | H (z) |     |
| --- | --- | --- | ------------- | --- | ----- | --- |
|     |     |     | 1             |     | 1     |     |
dz
| or from | time shifting |     |     |     |     |     |
| ------- | ------------- | --- | --- | --- | --- | --- |
z d
|     |     |     | nh [n]↔ | −z H (z) |     | (4.24) |
| --- | --- | --- | ------- | -------- | --- | ------ |
|     |     |     | 1       | 1        |     |        |
dz
P4) Convolution
If
z (z)
|     |     |     | h [n]↔ | H   |     |     |
| --- | --- | --- | ------ | --- | --- | --- |
|     |     |     | 1      | 1   |     |     |
and
z (z)
|     |     |     | h [n]↔ | H   |     |     |
| --- | --- | --- | ------ | --- | --- | --- |
|     |     |     | 2      | 2   |     |     |
then
z
|     |     |     | h [n]∗h [n]↔ | H (z)H | (z) | (4.25) |
| --- | --- | --- | ------------ | ------ | --- | ------ |
|     |     |     | 1 2          | 1 2    |     |        |
Note that, since we have established that a linear discrete time system has an
output which is the convolution of its impulse response with the input sequence
property, P4 says the x transform of the output is the product of the z transform of
| the | input and the | z transform | of the impulse | response. |     |     |
| --- | ------------- | ----------- | -------------- | --------- | --- | --- |
z
|     |     | x[n] | = h[n]∗y[n]↔ | H(z)Y(z) | = X(z) | (4.26) |
| --- | --- | ---- | ------------ | -------- | ------ | ------ |
The z transform of the impulse response, H(z), is then the discrete time transfer
function.
Example 4.5 Solution of a constant coefficient difference equation
Property P2 enables the z transform to be used in the solution of constant coef-
ficient difference equations in the same way that Laplace transforms are used to
solve differential equations. The solution of the differential equation is somewhat
more of an accomplishment, as can be seen considering the difference equation in
Equation (4.27) relating the input sequence y[n] and output sequence x[n].
|        | x[n]+(5/4)x[n−1]+(3/8)x[n−2]    |                   |              | = y[n−1]+4y[n−2]  |                  | (4.27) |
| ------ | ------------------------------- | ----------------- | ------------ | ----------------- | ---------------- | ------ |
| Taking | z transforms                    | and               | using P2 and | partial fractions |                  |        |
|        | X(z)+(5/4)z−1X(z)+(3/8)z−2X(z)= |                   |              |                   | z−1Y(z)+4z−2Y(z) |        |
|        | X(z)[1+(5/4)z−1+(3/8)z−2]       |                   |              | = (z−1+4z−2)Y(z)  |                  |        |
|        |                                 |                   | (z+4)Y(z)    | (z+4)Y(z)         |                  |        |
|        | X(z)=                           |                   |              | =                 |                  |        |
|        |                                 | (z2+(5/4)z+(3/8)) |              | (z+1/2)(z+3/4)    |                  |        |

| 118 |     |     |     |     |     |       |     | Digital filters |
| --- | --- | --- | --- | --- | --- | ----- | --- | --------------- |
|     |     |     |     |     |     | x[n]= | ≤   |                 |
If y[n] is a unit step and the initial condition are 0 for n 0
(z+4)
X(z)/z=
(z+1/2)(z+3/4)(z+1)
|     |     |     | −28/3 | 52/7 |     | (40/21) |     |     |
| --- | --- | --- | ----- | ---- | --- | ------- | --- | --- |
X(z)/z=
|     |     |                     |       | +     |                | +   |          |     |
| --- | --- | ------------------- | ----- | ----- | -------------- | --- | -------- | --- |
|     |     |                     | z+1/2 | z+3/4 |                | z−1 |          |     |
|     |     | x[n]=(−28/3)(−1/2)n |       |       | +(52/7)(−3/4)n |     | +(40/21) |     |
For comparison the difference Equation can be simply rewritten as
(−5/4)×[n−1]−(3/8)x[n−2]+u[n−1]+4u[n−2]
|       | x[n]     | =    |         |           |     |     |     |     |
| ----- | -------- | ---- | ------- | --------- | --- | --- | --- | --- |
| 4.4.5 | Discrete | time | fourier | transform |     |     |     |     |
In the special case that the unit circle is in the ROC, the z transform can be used
to create the discrete time Fourier transform by letting z = ej(cid:3) . The relationships
| are | in Equation | (4.28). |     |     |     |     |     |     |
| --- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
(cid:5)∞
|     |     |     |     | Xˆ((cid:3))= | x[n]e−jn(cid:3) |     |     |     |
| --- | --- | --- | --- | ------------ | --------------- | --- | --- | --- |
−∞
(cid:4)π
1
|     |     |     |     | x[n]= | Xˆ((cid:3))ejn(cid:3) | d(cid:3) |     | (4.28) |
| --- | --- | --- | --- | ----- | --------------------- | -------- | --- | ------ |
2πj
−π
If X(z) is the z transform then X(ej(cid:3)) = Xˆ((cid:3)). Note that Xˆ((cid:3)) is periodic with
|     | 2π  |     |     | (cid:3) |     |     |     | 2π. |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- |
period and the integral in can be performed over any interval of The
[−π,π]
interval is chosen only to make the parallel to the Fourier transform in
continuous time. The discrete samples in time have produced a transform which
(cid:3)
is continuous in but periodic. Consider the ideal low-pass filter shown in
Figure 4.4.
H(Ω)
1
|     |     |     |        | −π −π/2      | π/2  | π              | 2π Ω   |     |
| --- | --- | --- | ------ | ------------ | ---- | -------------- | ------ | --- |
|     |     |     | Figure | 4.4 Discrete | time | ideal low-pass | filter |     |

Digital filters 119
| The inverse | discrete | time | Fourier transform |     | is  |     |     |
| ----------- | -------- | ---- | ----------------- | --- | --- | --- | --- |
(cid:4)π/2
|     |      | 1   |                       | ejnπ/2−e−jnπ/2 |      |     | sin(nπ/2) |
| --- | ---- | --- | --------------------- | -------------- | ---- | --- | --------- |
|     |      |     | Xˆ((cid:3))ejn(cid:3) | d(cid:3)       |      |     |           |
|     | x[n] | =   |                       | =              |      | =   |           |
|     |      | 2π  |                       |                | j2nπ |     | nπ        |
−π/2
|     |     |     |     |     |     |     | ωt nπ/2. |
| --- | --- | --- | --- | --- | --- | --- | -------- |
Figures 3.9 and 3.10 are the continuous time equivalents with =
Since the z transform is a subset of the z transform all of the properties of the z
transform including convolution carry over. Hence we can imagine specifying the
behavior of a discrete time system in terms of its frequency response because a
filter with impulse response h[n] will operate on an input y[n] to produce an output
x[n] with
|     |     |     | Xˆ((cid:3)) | = Hˆ((cid:3))Yˆ((cid:3)) |     |     |     |
| --- | --- | --- | ----------- | ------------------------ | --- | --- | --- |
(4.29)
ExceptingthefactthatHˆ((cid:3))isperiodicallthenomenclatureassociatedwithanalog
filtersisappropriatefordigitalfilters,Hˆ((cid:3))canbelow-pass,high-passorband-pass.
Digital filters have pass bands, transition bands, and stop bands.
| 4.5 | Digital | filters |     |     |     |     |     |
| --- | ------- | ------- | --- | --- | --- | --- | --- |
One approach to digital filter design is to make the impulse response of the digital
filter correspond to samples of the analog filter’s impulse response. Such a filter is
referred to as ‘impulse invariant’. Sampling as in Section 3.5 with samples spaced
at T seconds and using an infinite impulse train as the sampling function the
0
transform of the sampled function is given by Equation (4.30).
|     |     |            | (cid:5)∞ |          |     | (cid:5)∞ |          |
| --- | --- | ---------- | -------- | -------- | --- | -------- | -------- |
|     |     |            |          | F        | 1   |          |          |
|     |     | z(t)= x(t) | δ(t−nT   | )↔ Z(ω)= |     | X(ω−kω   | ) (4.30) |
|     |     |            |          | o        |     |          | 0        |
T
|     |     |     | −∞  |     |     | −∞  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
where ω = 2π/T . The function z(t) is a continuous time function made up of
|     | 0   | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
impulses with weights given by the sample of x at nT 0 . Taking the transform of the
| impulses | Z(ω) | is also | given by Equation | (4.31). |     |     |     |
| -------- | ---- | ------- | ----------------- | ------- | --- | --- | --- |
(cid:5)∞
|     |     |     | Z(ω)= | x(nT | )e−jnωT0 |     |     |
| --- | --- | --- | ----- | ---- | -------- | --- | --- |
(4.31)
o
−∞
| Comparing | Equations |     | (4.28) and (4.31) |               |     |     |     |
| --------- | --------- | --- | ----------------- | ------------- | --- | --- | --- |
|           |           |     | Xˆ((cid:3))       | = Z((cid:3)/T | )   |     |     |
0 (4.32)
Xˆ((cid:3))
The periodic function is simply periodic replicas of the original frequency
response. If X(ω) is band limited and T is chosen to satisfy the Nyquist
0

120 Digital filters
criteria then the discrete filter is impulse invariant with the continuous time
filter.
If the analog filter were a second order Butterworth filter, for example, several
difficultiesemerge. Thefrequency response innot band limitedand thereisaliasing
at any reasonable sampling rate and the digital filter is IIR. Compromises can be
made to try to minimize the effects of both of these problems but other approaches
seem needed.
The mapping z = ej(cid:3) limits the complex variable z to the unit circle. It can be
viewed as the mapping z = esT with s = j(cid:3)/T . Other such mappings include the
0
bilinear transformation
2 1−z−1
s = (4.33)
T 1+z−1
0
which has an inverse
1+(T /2)s
0
z = (4.34)
1−(T /2)s
0
For z= ej(cid:3) the pair of equations are given in Equation (4.35)
2 (cid:3) ωT
ω = tan and (cid:3) = 2tan−1 0 (4.35)
T 2 2
0
Given an analog filter with transfer function H (s), the discrete time transfer
a
function is given by Equation (4.36)
(cid:12) (cid:13)
2 1−z−1
H (z) = H (4.36)
d a T1+z−1
Aliasing is eliminated but the mapping distorts the frequency axis which can have
an effect on some designs. The distortion is shown in Figure 4.5
Ω
π
Ω = 2 arctan(ωT /2)
0
ω
Figure 4.5 Frequency distortions in the bilinear transformation

Windows and windowing 121
4.6 Windows and windowing
Windowing is an issue in spectral estimation, that is, estimating the frequency
content of a signal record and in filter design. The FFT introduced in Section 3.6 is
a convenient tool for spectral analysis. Recall: the FFT is an efficient computation
technique for computing the terms in the DFT. The DFT assumes that the signal
record in question is one period of a periodic function and provides a connection
between N samples in time and N complex numbers which describe the harmonic
contentofthesignal.Inpracticalapplications,therecordisunlikelytobeoneperiod
of a periodic signal and the assumption is that the harmonic content found is that
of the periodic extension of the signal record as shown in Figure 4.6. The fact that
the first and last samples are not identical produces a discontinuity in the periodic
extension and alters the frequency content. The sample values of the waveform in
Figure 4.6 are
x=[−0.3647 −0.2147 −0.0647 0.0853 0.2353 0.3853 0.5353 0.6353 0.6203
0.5853 0.4353 0.2353 −0.0647 −0.5647 −1.1647 −1.3147]
The absolute value of the DFT with a rectangular window and with a Hamming
windowareshowninFigure4.7.Itcanbeseenthatthewindowhasgreatlyreduced
the energy in the all the harmonics while increasing the energy at DC. Viewed as a
filter itself,the Hamming window is shown in Figure4.8 compared to therectangu-
lar window. The Hamming response is broader around the fundamental (it does not
rejectthesecondharmonic)butismuchmoreselectiveforhigherfrequencies.There
arealargenumber ofwindowstochoosefrom.Matlaboffers16differentwindows.
NationalInstrumentsoffersanumberinLabView.1 Mostpopular windowshavethe
featuresoftheHammingwindowtovaryingdegrees.Somehavebroadermainlobes
and greater rejection of side lobes. Some have adjustable parameters that control
y[n]
n
…
…
n
Figure 4.6 A signal and its periodic extension

122 Digital filters
TFD
6
5 Rectangular window
4
3
2 Hamming window
1
0
0 2 4 6 8 10 12 14 16
1
x[n]h[n]
0.5
0
−0.5
X[n]
−1
−1.5
0 2 4 6 8 10 12 14 16
Figure 4.7 Effect of a Hamming window
16
14
Rectangular
12
10
8
6 Hamming
4
2
0
0 2 4 6 8 10 12 14 16
Figure 4.8 The Hamming and rectangular window transfer functions
these effects. The choice of a windowing functions is complicated and depends on
the application.
Theexpressionsforthewindowfunctionforthreerepresentativewindowsaregiven
in Table 4.1. The 32 sample windows and the corresponding FFTs are shown in
Figure 4.9.
4.7 Linear phase
One of the features of the windowing functions in the previous section is that they
come in at least one form with linear phase. Linear phase in analog filters is an
unachievable ideal while it is routine in digital filters. The elimination of phase
distortion is important in many applications. An FIR filter with certain symmetries

| Linear phase |     |               |     |     |     |     |     |     | 123 |
| ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| Table        | 4.1 | Three windows |     |     |     |     |     |     |     |
Hamming2
|                   |     |     | (cid:16) (cid:17) |         |     |     |     |     |     |
| ----------------- | --- | --- | ----------------- | ------- | --- | --- | --- | --- | --- |
| w[n]=0.54−0.46cos |     |     | 2π n              | , 0≤n≤N |     |     |     |     |     |
N
2
4-term Blackman-Harris3
|                         |     |     |     | (cid:16) (cid:17) |     | (cid:16) | (cid:17) |     |     |
| ----------------------- | --- | --- | --- | ----------------- | --- | -------- | -------- | --- | --- |
| w[n]=0.35875+0.48829cos |     |     |     | 2π n +0.01168cos  |     | 2π       | 3n       |     |     |
|                         |     |     |     | N                 |     | N        |          |     |     |
|                         | N   | N   |     |                   |     |          |          |     |     |
for − ≤n≤
|     | 2   | 2   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Flat-top4
|        |                      | (cid:16)  | (cid:17) | (cid:16)          | (cid:17) | (cid:16) | (cid:17)  | (cid:16) | (cid:17) |
| ------ | -------------------- | --------- | -------- | ----------------- | -------- | -------- | --------- | -------- | -------- |
| w[n]=α |                      | +α cos 2π | n +α     | cos 2π 2n         | +α cos   | 2π       | 3n +α     | cos 2π   | 4n       |
|        | 0                    | 1 N       |          | 2 N               | 3        | N        | 4         | N        |          |
|        | α=[0.215578−0.416633 |           |          | 0.277263−0.083579 |          |          | 0.006947] |          |          |
where
|     |     |     |     | Window function |     |     | FFT of Window function |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | ---------------------- | --- | --- |
|     |     |     | 1   |                 |     | 1   |                        |     |     |
|     |     |     | 0.8 |                 |     | 0.8 |                        |     |     |
Flattop
|     |     |     | 0.6 |     |     | 0.6 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Blackman-Harris
Hamming
|     |     |            | 0.4    |           |     | 0.4   |      |       |     |
| --- | --- | ---------- | ------ | --------- | --- | ----- | ---- | ----- | --- |
|     |     |            | 0.2    |           |     | 0.2   |      |       |     |
|     |     |            | 0      |           |     | 0     |      |       |     |
|     |     |            | 0      | 10 20     | 30  | 0     | 5    | 10 15 |     |
|     |     | Figure 4.9 | Window | functions | and | their | FFTs |       |     |
has linear phase. Let h[n] be the impulse response of an FIR filter with
Hˆ((cid:3)) H((cid:3))eiθ((cid:3))
|     |     |     |     | =   |     |     |     |     | (4.37) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
H((cid:3))
| with | real | and |     |     |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
< 0,
|     |     | h[n] | = 0 | for n | n   | ≥ N |     |     | (4.38) |
| --- | --- | ---- | --- | ----- | --- | --- | --- | --- | ------ |
If
|     |     |     | h[n] | = h[N−1−n] |          |     |     |     | (4.39) |
| --- | --- | --- | ---- | ---------- | -------- | --- | --- | --- | ------ |
|     |     |     |      | (cid:12)   | (cid:13) |     |     |     |        |
then
N−1
|     |     |     | θ((cid:3))= |     | (cid:3) |     |     |     |        |
| --- | --- | --- | ----------- | --- | ------- | --- | --- | --- | ------ |
|     |     |     |             | −   |         |     |     |     | (4.40) |
2

124 Digital filters
Assume N is even, (a similar development is possible if N is odd) and group the
terms in the sum
N(cid:5)/2−1
Hˆ((cid:3)) = h[n](e−jn(cid:3) +e−j(N−1−n)(cid:3))
0
(cid:12) (cid:13)
N(cid:5)/2−1 (cid:16) (cid:17) (cid:16) (cid:16) (cid:17)(cid:17) (cid:16) (cid:16) (cid:17)(cid:17)
Hˆ((cid:3)) = h[n]e −j N− 2 1 (cid:3) e −j n− N− 2 1 (cid:3) +e −j N−1−n− N− 2 1 (cid:3)
0
(cid:12) (cid:13)
N(cid:5)/2−1 (cid:16) (cid:17) (cid:16) (cid:16) (cid:17)(cid:17) (cid:16) (cid:16) (cid:17)(cid:17)
Hˆ((cid:3)) = h[n]e −j N− 2 1 (cid:3) e −j n− N− 2 1 (cid:3) +e j n− N− 2 1 (cid:3)
0
(cid:12) (cid:12) (cid:13) (cid:13)
(cid:16) (cid:17) N(cid:5)/2−1
Hˆ((cid:3)) = e −j N− 2 1 (cid:3) 2 h[n]cos n− N−1 (cid:3) (4.41)
2
0
For N odd, the upper limit on the sum is (N/2−1). A similar result is obtained
with odd symmetry (a minus sign in Equation 4.38), i.e.,
h[n] = −h[N−1−n] (4.42)
With odd symmetry the cosine terms in the sum in Equation (4.41) are replaced
with sine terms but the angles θ((cid:3)) is the same.
4.8 Approximation – filter synthesis
The design of a digital filter can be initiated by specifying requirements on the
frequency response Hˆ((cid:3)). Generic specifications for a low-pass filter are shown in
Figure 4.10.
1−δ ≤ Hˆ((cid:3)) ≤ 1+δ 0 ≤ (cid:3) ≤ (cid:3)
1 1 p
0 ≤ Hˆ((cid:3)) ≤ δ (cid:3) ≤ (cid:3) ≤ π
2 s
It is expected that the frequency response will have ripples in the pass band and
stop band. One approach would be to window a portion of the impulse response of
the ideal low-pass filter. Let g[n] be given by Equation (4.43)
sin(cid:3) (n−M)
c
g[n] = 0 ≤ n ≤ 2M (4.43)
π(n−M)
Then by windowing g[n] with various windows, different low-pass filters are
obtained. Figure 4.11 shows the frequency response of a 32 (M = 16) sample
version of Equation (4.43) with a cut-off frequency of π/2 along with the effect of

Approximation – filter synthesis 125
1+ δ
1
1− δ
1
Passband
Stopband
Transition
band
δ
2
Ω p Ω s π
Figure 4.10 Magnitude response specifications for a low-pass filter
1.4
1.2 Hamming Truncated sinc g[n]
1 Blackman-Harris
0.8
0.6
Flat top
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6
π
Figure 4.11 Low-pass filters N=32
the Hamming, Flat top, and Blackman-Harris windows. All four filters have linear
phase since they are symmetric.
A more direct approach to digital filter design would be to approach the choice
of the impulse response coefficients as an optimization problem. That is, from the
filter specification in Figure 4.10, for a given stop band and pass band find a set
of filter coefficients of given order to minimize the maximum deviation from 1 in
the pass band and 0 in the stop band. It is even possible to assign different weights
to the two different types of error. The difficulty is that algorithms for minimizing
maximum deviations are more complicated than for many other minimization prob-
lems. The Parks McClellan algorithm uses the Remez exchange algorithm to solve
these problems.5 The function firpm.m in MATLAB is an implementation of that
algorithm. The FFT of the 32d order filter with the indicated pass and stop bands
is shown in Figure 4.12.

126 Digital filters
Filter coefficients
1.4
0.5
0.4 1.2 Frequency
response
0.3 1
0.2 0.8
0.1 0.6 Pass band
Stop band
0 0.4
−0.1 0.2
−0.2 0
0 5 10 15 20 25 30 35 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Figure 4.12 Parks McClellan optimum 32nd order low-pass filter with e=0.0197
4.9 Wavelets
ThewavelettransformisasignalprocessingtoolthathasreplacedtheFouriertrans-
form inmany applications including data compression, Sonar and Radar, communi-
cations and biomedical applications. Considerable overlap exists between wavelets
and the area of filter banks. The wavelet transform is viewed as an improvement
over the Fourier transform because it deals with time-frequency resolution in a dif-
ferent way. The Fourier transform provides a decomposition of a time function into
exponentials,
ejωt
which exist for all time. We should consider the signal that is
processed with the DFT calculations as being extended periodically for all time as
discussed in the previous section. That is, the data window represents one period of
a periodic signal. The sampling rate and the length of the data window determine
the frequency resolution of the calculations. The wavelet transform introduces an
alternative to these limitations.
A windowed Fourier transform can be written as in Equation (4.44)
(cid:4)∞
X(ω,t) = x(τ)h(t−τ)e−jωτ dτ (4.44)
−∞
while the wavelet transform takes the form of Equation (4.45)
(cid:4)∞ (cid:2) (cid:12) (cid:13)(cid:3)
1 τ−t
X(s,t) = x(τ) √ ψ dτ (4.45)
s s
−∞
where s is a scale parameter.
If h(t) has Fourier transform H(ω) then h(t/s) has Fourier transform H(sω). Note
that for a fixed h(t), that a large value of s compresses the transform while small

| Wavelets |     |     |     |     |     |     | 127 |
| -------- | --- | --- | --- | --- | --- | --- | --- |
value of s spreads the transform in frequency. There are a few requirements on a
signal h(t) to be the ‘mother wavelet’ (essentially that h(t) have finite energy and
| be a band-pass | signal). |     |     |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- | --- | --- |
Wavelets are a family of functions obtained from the ‘mother wavelet’, ψ, by
dilating and translating. The discrete version is given by Equation (4.46).
|     |     |     |     |         | (cid:12) (cid:13) |     |     |
| --- | --- | --- | --- | ------- | ----------------- | --- | --- |
|     |     |     |     | (cid:5) | k−nam             |     |     |
1
|     | DWT(x,m,n) |     | =   | √ . | x(k)ψ |     | (4.46) |
| --- | ---------- | --- | --- | --- | ----- | --- | ------ |
am am
k
|     |     |     |     |     | (cid:12) (cid:13) |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | --- |
t−nam
|     |     | ψ   | (t) | a−m .ψ |     |     |        |
| --- | --- | --- | --- | ------ | --- | --- | ------ |
|     |     |     | =   | 2      |     |     | (4.47) |
|     |     |     | mn  |        | am  |     |        |
ψ(t)
Let be a rectangular pulse with one second duration as shown in Figure 4.13.
The functions ψ (t) = ψ(t−n) are shifted (translated) replicas of the one second
0n
pulse. The functions ψ (t) in Equation (4.47), with a = 2, are dilated (have a two
1n
| second duration) | as shown | in  | Figure | 4.13.      |          |     |        |
| ---------------- | -------- | --- | ------ | ---------- | -------- | --- | ------ |
|                  |          |     |        | √ (cid:12) | (cid:13) |     |        |
|                  |          |     |        | 2          | 1        |     |        |
|                  |          | ψ   | (t)=   | ψ          | (t−2n)   |     | (4.48) |
1n
|     |     |     |     | 2   | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Note that the set of functions {ψ (t)} are orthogonal as are the set {ψ (t)}, Th
|     |     |     | 0n  |     |     |     | 1n  |
| --- | --- | --- | --- | --- | --- | --- | --- |
{ψ (t)}
is property is maintained as m increases. The functions have a 2m sec-
mn
ond duration and are orthogonal to each other. If we denote the space spanned by
{ψ (t)} as V then V ⊃ V ⊃ V ···, i.e. V is coarser than V . There are a
| mn  | m   | 0   | 1 20 |     | m+1 | m   |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
number of common mother wavelets both continuous and discrete. The coarseness
mentioned for the rectangular wavelets translates into different frequency resolu-
tion as m changes. Smaller m gives higher frequency resolution. Some rectangular
wavelets and their Fourier transforms are shown in Figure 4.14. Discrete wavelets
include:Daubechies wavelets,Haarwavelets,Mathieuwavelets,Legendrewavelets
| and Villasenor | wavelet. |     |     |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- | --- | --- |
ψ
|     |     | 00  |     | ψ   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
03
1
. . .
0           1    ψ       2            3      ψ     4
|     |     | 10  |     | 11  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
.707 . . .
ψ
20
1/2
|     |     | Figure | 4.13 | Rectangular | wavelets |     |     |
| --- | --- | ------ | ---- | ----------- | -------- | --- | --- |

| 128 |     |     |     |     |     |     | Digital | filters |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- |
|     |     |     |     |     | 6   |     | 6       |         |
4
4
H(f)
2
2
0
0
−2
−2
−4
|     |     |     |         |     | −6      | −4      |           |       |
| --- | --- | --- | ------- | --- | ------- | ------- | --------- | ----- |
|     | B/2 | B   | B/4 B/2 |     | −20 −10 | 0 10 20 | −20 −10 0 | 10 20 |
|     |     |     |         |     | 4       |         | 3         |       |
2
2
1
0
0
−2
−1
|     |     |     |          |     | −4      | −2      |           |       |
| --- | --- | --- | -------- | --- | ------- | ------- | --------- | ----- |
|     |     |     |          |     | −20 −10 | 0 10 20 | −20 −10 0 | 10 20 |
| B/8 | B/4 |     | B/16 B/8 |     |         |         |           |       |
Figure 4.14 Rectangular wavelets and their Fourier transforms
Waveletsarealsorelatedtofilterbanks. Toillustratethis,considerusingwavelets
to compress a discrete waveform. Figure 4.15 shows a filter bank in which the
incoming signal h(k) is split into a high-pass and a low-pass signal at the far left
of the figure. Each half is samples at half the original sampling rate, the half band
(k ).
high-pass signal is sent forward as h and the low-pass signal is split again.
1 1
Consider the sequence x(n) = [−2 −28 −46 −44 −20 12 32 30] with the
low-pass filter being the average of two consecutive signals (x(n)+x(n+1))/2
(x(n)−x(n+1))/2.
| and | the high-pass | filter  | being the         | difference |           |               |            |     |
| --- | ------------- | ------- | ----------------- | ---------- | --------- | ------------- | ---------- | --- |
| The | resulting     | signals | shown in          | Figure     | 4.15 are  |               |            |     |
|     |               |         | h (k ) = [13−1−16 |            | 1],h      | (k )= [7−8.5] |            |     |
|     |               |         | 1 1               |            | 2         | 2             |            |     |
|     |               |         | (k ) [7.75],l     | (k         | ) [−0.75] |               |            |     |
|     |               |         | h =               |            | =         |               |            |     |
|     |               |         | 3 3               | 3          | 3         |               |            |     |
|     |               | h(k)    |                   |            |           |               | h 1 (k 1 ) |     |
|     |               | HPF     | 2                 |            |           |               |            |     |
B
h (k )
|     |     | /2  |     |     |     |     | 2 2    |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- |
|     |     | LPF | 2   | HPF | 2   |     |        |     |
|     |     | B/2 |     | B/4 |     |     | h (k ) |     |
3 3
|     |     |     |     | LPF | 2   | HPF 2 |        |     |
| --- | --- | --- | --- | --- | --- | ----- | ------ | --- |
|     |     |     |     | B/4 |     | B/8   | l (k ) |     |
3 3
LPF 2
B/8
|     |     |     | Figure | 4.15 | Filter | bank |     |     |
| --- | --- | --- | ------ | ---- | ------ | ---- | --- | --- |

Elements of artificial intelligence 129
40
30 Original
20 Compressed
10
0
−10
−20
−30
−40
−50
−60
Figure 4.16 The original and reconstructed compressed waveforms
If we truncate to three levels 0, 8, and 16 (compressing the signal)
h (k ) = [16 0−16 0],h (k ) = [8−8]
1 1 2 2
h (k ) = [8],l (k ) = [0]
3 3 3 3
and reconstruct the original sequence the original and compressed signal are shown
in Figure 4.16.
4.10 Elements of artificial intelligence
SuggestedapplicationofalimitednumberofAIconceptsinprotectionhasemerged
in the literature. It is attractive to imagine some powerful new technique solving
existingprotectionproblems. Twotechniques, ArtificialNeuralNetworks,anddeci-
sion trees, are based on training the relay with simulation and even field data to
differentiate between fault and no fault conditions. The third involves the use of
autonomous software agents distributed through the protection system.
4.10.1 Artificial neural networks
Artificial Neural Networks (ANNs) had their beginning in the ‘perceptron’ which
was designed to recognize patterns.6 In some sense ANNs are modeled after the
structure of the brain.7 The number of papers suggesting relay application has
soared. The attraction is the use of ANNs as pattern recognition devices that can be
trained with data to recognize faults or inrush or other protection effects. The basic
feed forward neural net is composed of layers of neurons as shown in Figure 4.17.
The function F is either a threshold function or a saturating function such as a
symmetric sigmoid function.(ψ in Figure 4.17) The weights w are determined by
i

130 Digital filters
x
1
n
|     |     | w   |     | ϕ wkxk |
| --- | --- | --- | --- | ------ |
1
1
x
2
w 2
|     | x   | w 3 |     | 1− e−x |
| --- | --- | --- | --- | ------ |
3
ϕ =
|     |     | .   |     | 1+ e−x |
| --- | --- | --- | --- | ------ |
.
x
|     | n      | w n  |                   |          |
| --- | ------ | ---- | ----------------- | -------- |
|     | Figure | 4.17 | Artificial Neural | Networks |
training the network. (so called back propagation). The training process is the most
difficult part of the ANN process. Typically simulation data such as that obtained
from EMTP is used to train the ANN. A set of cases to be executed must be
identified along with a proposed structure for the net. The cases include the data
therelaywouldseeandadeclarationthatthedatabelongstofaultcaseoranon-fault
case. The Matlab Neural network toolbox can perform the training but only after a
structure is chosen. A typical structure is shown in Figure 4.17.
The structure required is described in terms of the number if inputs, the number
of hiddenlayers, andthenumber of neurons inthevariouslayers, andtheoutput(s).
Anexamplemightbeanetwith12inputs,anda4,3,1layerstructure.Therewould
be 4×12 plus 4×3 plus 3×1 or 63 weights to be determined. Clearly a lot more
than 63 training cases are needed to learn 63 weights. In addition some cases not
| used for training | are needed | for | testing. |     |
| ----------------- | ---------- | --- | -------- | --- |
Once the weights are learned the designer is frequently asked how the ANN will
perform when some combination of inputs are presented to it. The ability to answer
such questions is very much a function of the breadth of the training sequence. The
| proposed protective | relaying | applications | of ANNs | include: |
| ------------------- | -------- | ------------ | ------- | -------- |
•
| high impedance | fault detection |     |     |     |
| -------------- | --------------- | --- | --- | --- |
•
| transformer | protection |     |     |     |
| ----------- | ---------- | --- | --- | --- |
•
fault classification
•
| fault direction | determination |     |     |     |
| --------------- | ------------- | --- | --- | --- |
•
fault location
| • adaptive reclosing |             |     |     |     |
| -------------------- | ----------- | --- | --- | --- |
| • rotating machinery | protection. |     |     |     |

| Elements | of artificial intelligence |     |     | 131 |
| -------- | -------------------------- | --- | --- | --- |
Inputs Outputs
|     | Input layer |     | Output layer |     |
| --- | ----------- | --- | ------------ | --- |
Hidden
layer
Figure 4.18
Layers
| 4.10.2 | Decision trees |     |     |     |
| ------ | -------------- | --- | --- | --- |
Decision trees are commonly used in data mining and have the advantage of sim-
plicity compared to neural networks. A classification tree is shown in Figure 4.18.
The tree represents a hypothetical experiment formed by the results from 100 tran-
sient stability simulations. Each of the simulations is declared stable or unstable
and a set of prefault measurements (angles, voltages, and flows) are attached to that
result.Thereare50stablecasesand50unstablecasesandeachsetofmeasurements
include 80 measurements. The tree is formed by processing a data set of 100×81
numbers.
|     | (m ,m ,m | ,···,m | ,y) i = 1,2,3,···,100 | (4.49) |
| --- | -------- | ------ | --------------------- | ------ |
|     | i1 i2    | i3 i80 | i                     |        |
They are1or0whilethem areanglesorvoltagesorrealorreactivepower flows.
| i   |     | i   |     |     |
| --- | --- | --- | --- | --- |
ThewhiteboxesinFigure4.19aresplittingnodeswherethevalueofameasurement
is used to branch to the right or the left. The top box uses some measurement, say,
m to divide the 100 cases into 55 on the right and 45 to the left.
ik1
<
|     |     | left if | m N1 |     |
| --- | --- | ------- | ---- | --- |
ik1
>N1
|     |     | right if | m ik1 | (4.50) |
| --- | --- | -------- | ----- | ------ |
Note the 55 to the right are not all stable or unstable, nor are 45 to the left.
Also observe the branching is on a single measurement. There are five additional
splitting nodes, with the number going left and right labeled for each. The
shaded nodes are the terminal nodes and for the example are correct. In large
real problems, there may be a small number of mis-classifications permitted. The
example has far fewer training cases than normally would be used. The actual tree
structure resulted from a training set of 4150 simulation cases which was tested
on an additional 4385 cases with a total error rate less than 1%.

132 Digital filters
Stable
|     |     | 45  | 55       | Unstable |
| --- | --- | --- | -------- | -------- |
|     |     | 30  | 15 10 40 |          |
15 10
|     |     | 20 10 | 10  |     |
| --- | --- | ----- | --- | --- |
15 20
|     |     | Figure | 4.19 A classification | tree |
| --- | --- | ------ | --------------------- | ---- |
Note that the tree has selected six variables out of the 80 measurements to com-
plete the tree. This is frequently the most important feature of the tree. One can
hypothesize that a large number of PMUs are available for the measurements and
thedecision treetrainingalgorithmwillselect thebest locationfor theplacement of
PMUsout of theoriginal offering.Thisisnot thecasefor theANN.If weimagined
80 inputs for the ANN we could hope some of the weights were small enough to
be omitted but it can not be guaranteed. In addition the size of neural net with 80
| inputs would | make | training difficult. |     |     |
| ------------ | ---- | ------------------- | --- | --- |
Experience with both ANNs and decision trees is that they both interpolate well
buthavedifficultyextrapolating.Thatis,ifweimaginethesetofmeasurementsthat
are used to train the ANN or classification tree as a region in measurement space
then a new set of measurements (not used in training) that lies within the training
set is unlikely to cause an error in classification. A new point that is outside the
trainingset,inanysense,hasalargerchanceofbeingmis-classified.Theerrorstend
to occur at the boundaries.8 This means that a great deal of engineering experience
| is required | in selecting | the training | cases. |     |
| ----------- | ------------ | ------------ | ------ | --- |
| 4.10.3      | Agents       |              |        |     |
An agent is a self-contained piece of software that has the properties of autonomy
and interaction. Agents in relays would be capable of autonomously interacting
with each other. It has been proposed that using geographically distributed agents
located in every relay can improve on more traditional isolated component system.
A suggested research area is the use of agent-based backup protection system. The
fact that agent relays would be capable of autonomously interacting witheach other
could make a distributed systems work effectively. This flexibility and autonomy
adds reliability to the protection system because any given agent-based relay can
continue to work properly despite failures in other parts of the protection system.

Problems 133
It is certainly necessary to explore the expected communication traffic patterns in
order to make agents more intelligent and robust towards network conditions. The
object models of multifunctional distance relays in IEC 61850 may provide an
environment for agents. Message structure and strategies for such systems have
been studied in simulation.9–12
4.11 Conclusion
This chapter has continued in the vein of previous chapter with more of the math-
ematical basis for computer relaying. In this chapter there is more emphasis on
digital signal processing. Discrete time signals and systems, the z transform, and
discrete time Fourier transforms have parallels in the material in Chapter 3, while
some of the material in the Section 4.6 through Section 4.10 is unlike Chapter 3.
The concept of windowing and the behavior of various windows is less of an issue
in relaying then in other uses of the measurements that relays make. Synchronized
phasor measurementsinChapter8aresuchanapplication. Thewindowingmaterial
is then the background for some of the signal processing involved in processing
synchronized phasor measurements. Wavelets are, in a sense, a generalization of
Fourier analysis and have found wide application in other fields. Artificial intel-
ligence, including ANNs, decision trees, and agents are concepts that have been
suggested in the literature to improve relaying. The first two involve training the
relay with simulation or field data while the third allows autonomous behavior of
software installed in relays. Both concepts have encountered the kind of resistance
encountered by the first attempts at digital relaying. The relay engineer is reluctant
to accept the possibility of a relay, at some time inthe future, behaving ina manner
that cannot be explained.
Problems
4.1 Given a causal LTI system with input y(t) and output x(t) described by
Y(s)
X(s) =
s2+3s+2
Write a difference Equation for a discrete time system which is impulse
invariant (with a sampling time of T seconds) to the continuous system. i.e.,
h[n] = h (nT)
a
4.2 Find a discrete tine sequence x[n];−∞ < n,< ∞ which has z transform
1
X(z) = ; 0.5 < |z| < 1
z2(z−0.5)(z+1)

134 Digital filters
4.3
Determine, in each case, whether x[n] has a discrete-time Fourier transform,
| X(z), and | if so                       | find it.      |            |          |
| --------- | --------------------------- | ------------- | ---------- | -------- |
| (a) x[n]= | 2nu[n]                      |               |            |          |
| (b) x[n]  | = 2nu[−n]                   |               |            |          |
| (c) x[n]= | 2−nu[n]                     |               |            |          |
| (d) x[n]  | = 2−nu[n]+3nu[−n−1(cid:18)] |               | (cid:19)   |          |
|           | [n]∗x                       |               | 2 n        | e−3nu[n] |
| (e) x[n]= | x 1                         | 2 [n] x 1 [n] | = u[n] x 2 | [n] =    |
3
4.4 A discrete time system is used to model a causal continuous time system
| modeled | by  |     |     |     |
| ------- | --- | --- | --- | --- |
dx(t)
|     |     |     | +0.9x(t) | y(t) |
| --- | --- | --- | -------- | ---- |
=
dt
dx(t)
| By replacing |     | with the forward | difference | approximation |
| ------------ | --- | ---------------- | ---------- | ------------- |
dt
x((n+1)T)−x(nT)
T
(a) Sketch the magnitude of the magnitude of the frequency response of the
| discrete | time | system. |     |     |
| -------- | ---- | ------- | --- | --- |
(b) For T = 10/9 sketch the magnitude of the frequency response of the
| discrete | time | system. |     |     |
| -------- | ---- | ------- | --- | --- |
(c) For what values of T is the discrete time system unstable?
4.5 Find the transfer function for two discrete time systems which simulate the
H(s)
system = 50 both an impulse invariant: system and one obtained
|     |     | (s+w )3 |     |     |
| --- | --- | ------- | --- | --- |
c
| with the | bilinear | transformation. |     |     |
| -------- | -------- | --------------- | --- | --- |
4.6 If the impulse response of a discrete time system is given by
(cid:12) (cid:13)
1 n
|     |     | h[n] | = u[n] |     |
| --- | --- | ---- | ------ | --- |
2
Find the output x[n] if the input is y[n] = u[n]. Use convolution.
4.7 If it exists find the z transform (the function and the ROC) for
(cid:18) (cid:19)
1 n
| (a) x[n]= | u[n] | +u[−n−1]3n |     |     |
| --------- | ---- | ---------- | --- | --- |
3
|     | u[n](3)n+u[−n−1] |     | 1   |     |
| --- | ---------------- | --- | --- | --- |
(b) x[n] =
3n
| (c) x[n]= | 1;  | 0 ≤ n ≤ (N−1) |     |     |
| --------- | --- | ------------- | --- | --- |
| x[n]      | = 0 | elsewhere     |     |     |
(cid:18) (cid:19)
n
| (d) x[n] | = n 1 | u[n+1] |     |     |
| -------- | ----- | ------ | --- | --- |
2

References 135
Pass band
Stop band
Stop band
|     |     |        |     | 2π/8 3π/8 | 5π/8               | 7π/8  | π   |
| --- | --- | ------ | --- | --------- | ------------------ | ----- | --- |
|     |     | Figure |     | P4.20     | Figure for Problem | 4.10. |     |
4.8
|     | Find x[n] | where X(z) | is  | as indicated |       |     |     |
| --- | --------- | ---------- | --- | ------------ | ----- | --- | --- |
|     | X(z)      | z          |     | 0.3          | < <   |     |     |
|     | (a)       | =          | ;   |              | |z| ∞ |     |     |
z2−.5z+.06
|     | X(z) | 4   |     | <     | < 1/4 |     |     |
| --- | ---- | --- | --- | ----- | ----- | --- | --- |
|     | (b)  | =   | ;   | 0 |z| |       |     |     |
z3(4z−1)
|     | (c) X(z) | = z2 | ;   | 1 < | |z| < 2 |     |     |
| --- | -------- | ---- | --- | --- | ------- | --- | --- |
(z−1)(z+2)
| 4.9 | In each                 | case find | the response  |     | to an input y[n] | = u[n] |     |
| --- | ----------------------- | --------- | ------------- | --- | ---------------- | ------ | --- |
|     | (a) x[n]−2x[n−1]+x[n−2] |           |               |     | = y[n]           |        |     |
|     | (b) x[n]−x[n−2]         |           | = y[n]−y[n−1] |     |                  |        |     |
4.10 Use the Matlab function firpm.m to design a 64th order band-pass filter with
|     | the desired | pass band | and | stop | band shown. |     |     |
| --- | ----------- | --------- | --- | ---- | ----------- | --- | --- |
References
[1] http://zone.ni.com/devzone/cda/tut/p/id/4844
[2] Oppenheim, A. V., and R. W. Schafer (1989) Discrete-Time Signal Processing,
| Prentice-Hall, |     | pp. 447–448. |     |     |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- | --- | --- |
[3] Harris, F. J. (1978) On the use of windows for harmonic analysis with the discrete
Fourier transform. Proceedings of the IEEE, vol. 66, pp. 51–84.
[4] D’Antona, G. and Ferrero, A. (2006) DigitalSignalProcessingforMeasurementSys-
| tems, | New | York: Springer |     | Media, | Inc., pp. 70–72. |     |     |
| ----- | --- | -------------- | --- | ------ | ---------------- | --- | --- |
[5] Rabiner, L. R., McClellan, J. H. and Parks, T. W. (1975) FIR digital filter design
techniques using weighted Chebyshev approximations, Proceedings of the IEEE, vol.
| 63, | pp. 595–610. |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- |
[6] Rosenblatt,F.ThePerceptron:Aprobabilisticmodelforinformationstorageandorga-
nizationinthe brain,CornellAeronauticalLaboratory,PsychologicalReview,vol.65,
| no. | 6, pp. | 386–408. |     |     |     |     |     |
| --- | ------ | -------- | --- | --- | --- | --- | --- |
[7] Haykin, S. (1994) NeuralNetworks:AComprehensiveFoundation, Macmillian.
[8] Sheng, Y. and Rovnyak, S. M. (2002) Decision trees and wavelet analysis for power
transformer protection, IEEE Trans. on Power Delivery, vol. 17, no. 2.

136 Digital filters
[9] IEC61850-7-2(2003–2005)Communicationnetworksandsystemsinsubstations,Part
7-2: Basic communication structure for substations and feeder equipment – Abstract
communication service interface (ACSI).
[10] Hopkinson, Wang, X., Giovanini, R., Thorp, J. S. et al. (2006) EPOCHS A plat-
form for agent-based electric power and communication simulation built from
commercialoff-the-shelfcomponents, IEEE Trans. on Power Systems, vol. 21, no. 2,
pp. 548–558.
[11] Apostolov,A.P.(2001)Objectmodelsofmultifunctionaldistancerelays,Proceedings
of the Power Engineering Society Summer Meeting, pp. 1157–1162.
[12] Apostolov,A.P.(2001)Multi-agentsystemsandIEC61850,ProceedingsofthePower
Engineering Society General Meeting, 2001, pp. 1–6.

5
Transmission line relaying
5.1 Introduction
Historically,linerelayingalgorithmsrepresentmostoftheearlyactivityincomputer
relaying. Researchers perceived that line relaying offered the greatest challenge,
alongwiththegreatestpossibilityforimprovedperformance.Inthischapterwewill
examine many of these algorithms and attempt to draw some general conclusions
about the characteristics of several types of algorithms.
Anumberofalgorithmscanberegardedasimpedancecalculationsinthatthefun-
damentalfrequencycomponentsofbothvoltagesandcurrentsareobtainedfromthe
samples.Theratiosofappropriatevoltagesandcurrentsthenprovidetheimpedance
to the fault. The performance of all of these algorithms is dependent on obtaining
accurate estimates of the fundamental frequency components of a signal from a
few samples. Within this class of algorithm both Fourier and curve fitting tech-
niques are used to estimate the fundamental frequency components. If the signal in
question were a pure sinusoid then virtually every algorithm ever suggested would
work perfectly. The distinction between algorithms of this type is in their behavior
when signals other than the fundamental frequency are present in the voltage and
current.
Another type of algorithm is based on a series R-L model of the transmis-
sion line. Rather than using a single frequency model, such as the impedance,
this approach has the apparent advantage of allowing all signals that satisfy the
differential equation to be used in estimating the R and L of the model.
Line relaying algorithms have been compared under the assumption that the cur-
rents and voltages were composed of the fundamental and certain combinations
of harmonics.1 It is our contention that, given all the situations in which a line
relay must operate – i.e. a changing system configuration, variable fault incidence
angle etc. – the non-fundamental frequency components seen by the relay must be
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

| 138 |     |     |     |     |     |     | Transmission | line | relaying |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | -------- |
regarded as a random process. The nature of this random process is then a primary
| issue in evaluating |     | relaying |     | algorithm | performance. |     |     |     |     |
| ------------------- | --- | -------- | --- | --------- | ------------ | --- | --- | --- | --- |
Inthefollowingsectionsthesourcesoferrorinthesignalswillbeinvestigatedand
astatisticaldescriptionoftheerrorswillbepostulated.Foralargeclassofalgorithm
any non-fundamental frequency signal constitutes anerror. Theconnection between
the error model and the algorithm used to estimate the parameters of interest will
be established. Before proceeding, certain notation and concepts common to all
algorithms will be illustrated for a simple example. The following notation will be
| used in discussing |     | all | of the | algorithms: |     |     |     |     |     |
| ------------------ | --- | --- | ------ | ----------- | --- | --- | --- | --- | --- |
y(t) = The instantaneous value of an AC waveform, a voltage or a current
kth
| y = The |     | sample | value | of y(t) |     |     |     |     |     |
| ------- | --- | ------ | ----- | ------- | --- | --- | --- | --- | --- |
k
ω = The fundamental power system frequency in radians per second
o
| (cid:1)t = The | fixed | interval | between |     | samples, | i.e. |     |     |     |
| -------------- | ----- | -------- | ------- | --- | -------- | ---- | --- | --- | --- |
y(k(cid:1)t)
y k =
θ = The fundamental frequency angle between samples, i.e. θ = ω (cid:1)t
o
To illustrate some of the common features of algorithms based on a waveform
| model suppose |     | y(t) is | assumed | to  | be of | the form |         |     |       |
| ------------- | --- | ------- | ------- | --- | ----- | -------- | ------- | --- | ----- |
|               |     |         |         |     |       | ω        | ω       |     |       |
|               |     |         | y(t)    | = Y | c cos | o t+Y s  | sin o t |     | (5.1) |
−(cid:1)t,
where Y c and Y s are real numbers, Further, assume samples are taken at 0,
and (cid:1)t
=y(−(cid:1)t)
y
−1
=y(0)
y
o
|     |     |     |     |     | y =y((cid:1)t) |     |     |     | (5.2) |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | ----- |
1
| The samples | are | related | to  | the amplitudes |      | Y and | Y through       |     |       |
| ----------- | --- | ------- | --- | -------------- | ---- | ----- | --------------- | --- | ----- |
|             |     |         |     |                |      | c     | s               |     |       |
|             |     |         |    |               |     |      |                 |     |       |
|             |     |         |     |                |      |       | (cid:2) (cid:3) |     |       |
|             |     |         | y   |                | cosθ | −sinθ |                 |     |       |
|             |     |         | −1  |                |      |       | Y               |     |       |
|             |     |         |    |               |     |      | c               |     |       |
|             |     |         | y   | =              | 1    | 0     |                 |     | (5.3) |
|             |     |         | o   |                |      |       | Y               |     |       |
|             |     |         | y   |                | cosθ | sinθ  | s               |     |       |
1
where θ is the fundamental frequency angle between samples. It is clear that
two samples are sufficient to determine Y and Y if the signal is described by
|     |     |     |     |     |     | c   | s   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Equation (5.1). For example, Y = y and Y = (y −y cosθ)/sinθ satisfy the last
|     |     |     |     | c   | 0   | s   | 1 0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
two equations in (5.3). The use of three samples is an attempt to provide some
immunity to additional terms (harmonics or random terms) in Equation (5.1). As
such, a least squares solution to Equation (5.3) would seem appropriate. Using

| Introduction |        |     |              |          |     |     |     |     |     | 139 |
| ------------ | ------ | --- | ------------ | -------- | --- | --- | --- | --- | --- | --- |
| Equation     | (3.75) | the | least square | solution |     | is  |     |     |     |     |
 
|     | (cid:2) | (cid:3) | (cid:2) |     |     | (cid:3) (cid:2) |     | (cid:3) |     |     |
| --- | ------- | ------- | ------- | --- | --- | --------------- | --- | ------- | --- | --- |
y
|     | Yˆ  |     | 1+2cos2θ |     |        | −1 cosθ | cosθ   |     | −1  |     |
| --- | --- | --- | -------- | --- | ------ | ------- | ------ | --- | --- | --- |
|     |     | c   |          |     | 0      |         | 1      |     |   |     |
|     |     | =   |          |     |        |         |        |     | y   |     |
|     | Yˆ  |     | 0        |     | 2sin2θ | −sinθ   | 0 sinθ |     | o   |     |
s
y 1
|     |     | (cid:7) |          |     |         | (cid:8) |     |     |     |       |
| --- | --- | ------- | -------- | --- | ------- | ------- | --- | --- | --- | ----- |
|     |     |         | cosθ+y   | +y  | cosθ    |         |     |     |     |       |
|     |     | y 1     |          | −1  |         |         |     |     |     |       |
|     | Yˆ  | =       |          | o   |         |         |     |     |     | (5.4) |
|     | c   |         | 1+2cos2θ |     |         |         |     |     |     |       |
|     |     |         |          |     | (cid:7) | (cid:8) |     |     |     |       |
|     |     |         |          |     | y       | −y      |     |     |     |       |
|     |     |         |          | Yˆ  |         | 1 −1    |     |     |     |       |
|     |     |         |          |     | =       |         |     |     |     | (5.5) |
|     |     |         |          |     | s       | 2sinθ   |     |     |     |       |
A more general solution to Equation (5.3) (not a least square solution) is in the
form
|     |     |     | Y = | Yˆ +c | [y  | −2y cosθ+y | ]   |     |     | (5.6) |
| --- | --- | --- | --- | ----- | --- | ---------- | --- | --- | --- | ----- |
|     |     |     | c   | c     | 1 1 | o          | −1  |     |     |       |
|     |     |     | Y = | Yˆ +c | [y  | −2y cosθ+y | ]   |     |     | (5.7) |
|     |     |     | s   | s     | 2 1 | o          | −1  |     |     |       |
where c and c are arbitrary constants. The bracketed terms in Equations (5.6)
|     | 1   | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and (5.7) are zero if the signal is described by Equation (5.1). Two of the early
algorithms correspond to particular choices of c 1 with c 2 = 0. The Mann-Morrison
| algorithm2 | corresponds |     | to c | = 0 and |     |     |     |     |     |     |
| ---------- | ----------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- |
2
−cosθ
c =
1 1+2cos2θ
| while | the Prodar | 70  | algorithm3 | corresponds |     | to c = | 0 and |     |     |     |
| ----- | ---------- | --- | ---------- | ----------- | --- | ------ | ----- | --- | --- | --- |
2
|     |     |     |     | (cid:2) |     |     | (cid:3) |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | ------- | --- | --- | --- |
cosθ
1
|     |     |     | c   | =   | −   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     |     | sin2θ |     | 1+2cos2θ |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | -------- | --- | --- | --- | --- |
The original versions of both algorithms also are based on the assumption
that θ is small enough so that the small angle assumptions that, cos(θ) ≈ 1 and
sin(θ)
≈ 0 are appropriate and represent approximations of derivative terms from
samples.
In order to examine some general properties of all such algorithms let us take the
version with c and c equal to zero and examine the computation as time passes
|     |     | 1   | 2   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and more samples become available. An algorithm based on the last three samples
| y k−1 , | y k , and | y k+1 , | would have | the   | form   |       |       |     |     |     |
| ------- | --------- | ------- | ---------- | ----- | ------ | ----- | ----- | --- | --- | --- |
|         |           |         |            | [y    | cosθ+y | +y    | cosθ] |     |     |     |
|         |           |         | Yˆ(k)      | = k+1 |        | k k−1 |       |     |     |     |
(5.8)
|     |     |     | c   |     | 1+2cos2θ |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |

| 140 |     |     |       |     |         | Transmission | line | relaying |
| --- | --- | --- | ----- | --- | ------- | ------------ | ---- | -------- |
|     |     |     |       | [y  | −y      | ]            |      |          |
|     |     |     | Yˆ(k) | =   | k+1 k−1 |              |      | (5.9)    |
|     |     |     | s     |     | 2sinθ   |              |      |          |
where the superscript k indicates calculations centered at the kth sample. If y(t)
were a pure sinusoid as in Equation (5.1) then (in fact, for any choice of c and c )
|     |     |     |     |     |     |     |     | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(k)
|     |     |     | Y =Y | cosk   | θ+Y sink | θ   |     | (5.10) |
| --- | --- | --- | ---- | ------ | -------- | --- | --- | ------ |
|     |     |     | c    | c      | s        |     |     |        |
|     |     |     | (k)  |        | θ−Y      | θ   |     |        |
|     |     |     | Y =Y | s cosk | c sink   |     |     | (5.11) |
s
In polar form
(cid:29)
|     |     | (cid:11)             | (cid:11) |          |          |                 |     |        |
| --- | --- | -------------------- | -------- | -------- | -------- | --------------- | --- | ------ |
|     |     | (cid:11) (k)(cid:11) | (Y       | (k))2+(Y | (k))2    |                 |     |        |
|     |     | Y                    | =        |          |          |                 |     | (5.12) |
|     |     |                      |          | c        | s        |                 |     |        |
|     |     |                      |          | (cid:26) | (cid:27) |                 |     |        |
|     |     |                      |          |          |          | (cid:2) (cid:3) |     |        |
(k)
|     |     |      |        | Y   |         | Y     |     |        |
| --- | --- | ---- | ------ | --- | ------- | ----- | --- | ------ |
|     |     | ϕ(k) | =tan−1 | s   | = tan−1 | s −kθ |     | (5.13) |
(k)
|     |     |     |     | Y   |     | Y   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | c   |     | c   |     |     |
It can be seen from Equation (5.13) that the computed phasor has the correct
|     |     |     |     | ϕ(k) |     | θ   |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- |
amplitude but rotates i.e. the angle decreases by the angle at each sample
point Depending on the application, it may be necessary to correct for the rotation.
Iftheratioofvoltageandcurrentphasorsistobeusedforanimpedancecalculation,
| however, | then the | rotation | will cancel |     | in the division. |     |     |     |
| -------- | -------- | -------- | ----------- | --- | ---------------- | --- | --- | --- |
The algorithm described by Equations (5.8) and (5.9) has a datawindow of three
samples, that is, as a new sample becomes available, the oldest of the three sample
values is discarded and the new sample value is included in the calculation. Each
sample is then used in three calculations, once as y , once as y , and once as
|     |     |     |     |     |     | k+1 | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
y . The calculation in Equations (5.8) and (5.9) must then be completed by the
k−1
microprocessor before the next sample is produced. In practice a great deal more
| must actually | be computed |     | as we | will | see later. |     |     |     |
| ------------- | ----------- | --- | ----- | ---- | ---------- | --- | --- | --- |
A moving data window of three samples is shown in Figure 5.1 for an ideal
voltage waveform sampled at 12 samples per cycle. The voltage decreases instan-
taneously at the fault instant. The window labeled W1 contains three samples of
pre-fault data, the windows W2 and W3 contain both pre- and post-fault data, and
the window W4 has only post-fault data. The calculations in Equations (5.8) and
(5.9) will produce the correct phasors in the windows containing pure pre-fault or
post-fault samples. The data in the windows W2 and W3, however, cannot be fitted
to a pure sinusoid and the computed phasor is of little meaning. It can be verified,
however,thatthecomputedphasordoesnotfitthethreesamples.Itshouldbenoted
that a two sample window will always fit the data although the fit to one pre-fault
| and one post-fault |     | sample | is equally | meaningless. |     |     |     |     |
| ------------------ | --- | ------ | ---------- | ------------ | --- | --- | --- | --- |

Introduction 141
W W
3 4
Moving data window
W
2
W
1
Figure 5.1 Moving three sample data window on a voltage waveform. W1 is pre-fault,
W2 and W3 contain both pre-fault and post-fault samples, and W4 is pure post-fault
There are several conclusions that can be drawn from the simple three sample
algorithm and the Figure. The sample time, (cid:1)t, determines the amount of time the
microprocessor has to complete its calculations. The example with 12 samples per
cycle has (cid:1)t = 1.3889msec for a 60Hz system. On a 50Hz system 20 samples
a cycle yields (cid:1)t = 1msec. Existing algorithms use sampling rates from four to
64 samples a cycle. Clearly high sampling rates require more powerful processors
or particularly simple algorithms.
The second issue is that of the length of the data window. Recognizing that the
resultsobtainedwhenthewindowcontainsbothpre-faultandpost-faultsamplesare
unreliable,itseemsreasonabletowaituntiltheresultsarereliable(whenthewindow
contains only post-fault data) before making relaying decisions. It is important that
a technique that senses this transition region be developed. The response of the
example algorithm in this transition region is a function of the parameters c and
1
c in Equations (5.6) and (5.7). Since a longer window takes longer to pass over
2
the fault instant, it is clear that faster decisions can be made by short window
algorithms. Unfortunately, as we will see in Section 5.5, the ability of an algorithm
to reject non-fundamental frequency signals is a function of the length of the data
window. In other words, there is an inherent inverse relationship between relaying
speed and accuracy. While the algorithm represented by Equations (5.8) and (5.9)

| 142 |     |     |     |     |     |     | Transmission | line relaying |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- |
yields the correct phasor if the signal y(t) is given by Equation (5.1), we must
recognize that the signal to be sampled is more accurately given by:
|     |     |     | y(t) = Y cosω | t+Y | sinω | t+ε(t) |     | (5.14) |
| --- | --- | --- | ------------- | --- | ---- | ------ | --- | ------ |
|     |     |     | c             | o   | s    | o      |     |        |
ε(t)
It is the nature of the signal in Equation (5.14) that must be understood in
| order to    | evaluate | line     | relay performance. |     |     |     |     |     |
| ----------- | -------- | -------- | ------------------ | --- | --- | --- | --- | --- |
| 5.2 Sources |          | of error |                    |     |     |     |     |     |
Thepost-faultcurrentandvoltagewaveformsfailtobepurefundamental frequency
sinusoids for a variety of reasons. The most predictable non-fundamental frequency
term is the decaying exponential which can be present in the current waveform.
For the series R-L model of the line shown in Figure 5.2, assuming zero pre-fault
current and a steadystatefault current of the formI cos(ω t−ϕ),the instantaneous
0
| current | for a | fault at time | t is given | by  |     |     |     |     |
| ------- | ----- | ------------- | ---------- | --- | --- | --- | --- | --- |
0
|     |     | i(t) | cos(ω t−ϕ)−[I |     | cos(ω | −ϕ)]e−(t−t0 | )R/L |        |
| --- | --- | ---- | ------------- | --- | ----- | ----------- | ---- | ------ |
|     |     | = I  |               |     |       | t           |      | (5.15) |
|     |     |      | 0             |     | 0     | 0           |      |        |
The second term in Equation (5.15) decays exponentially with the time constant
of the line. This term is the main cause of transient over-reach in high speed relays,
and must be eliminated if computer relaying at fractional cycle speed is to be
achieved. For a typical EHV line the time constant is in the range of 30–50ms.
Theinitialamplitudeoftheexponentialcomponentcanbeaslargeasthepeakofthe
fault current, as shown in Figure 5.3. The situation can be even more complicated
near a large generator. The exponential term is not an error to algorithms based
on a differential equation description of the line, since the exponential satisfies the
differential equation. If the time constant of the line is known, then the decay can
be removed with an external filter or even in software (for algorithms which see
the exponential decay as an error). The dependence of the time constant on fault
resistance makes the removal less effective for high resistance faults.
|     |     |     | i(t) | L   |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- |
R
e(t)
|     |     | Figure | 5.2 Series | R-L model | of a | transmission | line |     |
| --- | --- | ------ | ---------- | --------- | ---- | ------------ | ---- | --- |

Sources of error 143
t t
0
steady state
fault current
Figure 5.3 Fault current. The dashed curve is the steady state fault current
Other non-fundamental frequency terms are not so easy to remove because they
are not so easy to predict. The current and voltage transducers contribute some of
these signals. For example, as shown in Section 2.6, a capacitive coupled voltage
transformer has a transient response to the abrupt change in voltage shown in
Figure 5.1. High frequency signals associated with the reflection of waveforms
between the bus and fault may be present, as will be developed in Chapter 8. The
nonlinear behavior of the fault arc may produce harmonic signals. In addition, as
shown in Section 1.5, the A/D converter contributes errors due the least significant
bit in the conversion and due to timing errors, i.e. the samples are not exactly (cid:1)t
sec appart. Most of these signals have considerable high frequency content and can
be reduced through the use of an anti-aliasing filter.
Since the waveform is being sampled at a rate of f = 1/(cid:1)t Hz the Nyquist sam-
s
plingtheoremfromSection3.5impliesthatthesignalshouldbefilteredwithafilter
havingacut-offfrequencyoff /2toavoidaliasing.AsmentionedinChapter1,such
s
a filter will remove the high frequency error signals described above but will con-
tributea transient response of itsown; also, drift over timeof thecomponent values
in such filters (particularly active realizations of such filters) are sources of error.
Finally, the power system itself is a source of non-fundamental frequency sig-
nals. Consider the single phase model of three lines and two generators shown
in Figure 5.4. It is assumed that the lines are identical but one source is strong
and one is weak. The lines are assumed to be 100 miles of typical 765kV line.
If a fault is applied at 60% of the protected line, the voltage seen by the relay
is shown in Figure 5.5. The smooth curve is the voltage that would result if the
capacitors were removed from Figure 5.5. It can be seen that the inclusion of
the capacitors has produced at least two non-fundamental frequency signals. These
non-fundamentalfrequenciesarenaturalfrequenciesofthesystemwhichareexcited
by the application of the fault. Since the network is fixed if the fault location is

144 Transmission line relaying
L r kL kr
C C kC
protected
zone
Figure 5.4 Single-phase power system model
Voltage in per unit
1.0
−1.0
Time
Figure 5.5 Voltage waveforms for a fault at 60% of the line length
held constant, it follows that the natural frequencies are determined by the fault
location.
Figure 5.6 shows a family of voltage waveforms produced by altering the fault
incidenceangle.Itcanbeseenthatthephaseofthenon-fundamentalfrequencycom-
ponentsisafunctionofthefaultincidenceangle.Asthefaultlocationischangedas
shown in Figure 5.7, the frequency of the non-fundamental frequency components
Voltage in per unit
1.0
−1.0
Time
Figure 5.6 Family of voltage waveforms for faults at 60% of the line length

Sources of error 145
Voltage in per unit
1.0
−1.0
Time
Figure 5.7 Family of voltage waveforms for varying fault locations
changes. A similar effect can be produced by altering the network structure behind
the fault. Experiments on a model power system combining the effect of changing
the structure of the network feeding the fault and the fault type and location have
been reported.4 The conclusion is that an important part of the non-fundamental
frequency signal ε(t) in Equation (5.14), at least for high voltage lines, is due to the
network itself. These signals depend on the fault location and on the nature of the
system feeding the fault and, as such, are not predictable. Example 3.20 provides
a model of such a process. If we model the fault incidence angle as the random
phase and the fault location and network structure as the mechanism producing the
random frequency then we can think of the power spectrum of Example 3.20 as the
power spectrum of the signal in ε(t) in Equation (5.14). It should be recognized that
each realization of such a process is a rather deterministic looking signal, such as
that shown in Figure 5.5. (This is counter intuitive if one expects a realization of a
random process to look noisy.) The randomness is present because, considering the
ensemble of times that the relay is expected to operate, the frequency and phase of
the signal cannot be predicted.
Considering the ε(t) in Equation (5.14) as a random process, it is reasonable
to consider the anti-aliasing filter and the algorithm taken together as filtering the
random process, as in Section 3.8. The frequency response of the algorithm is
then an important part of the filtering process. To obtain the frequency response
of the algorithm we should compute the response of the algorithm (the phasor for
Equations (5.6) and (5.7), for example) when the input signal is of the form
ejωt.
Example 5.1
If y(t) = ejωt
y =
e−jω(cid:1)t
−1
y = 1
o
y =
ejω(cid:1)t
1

146 Transmission line relaying
and Equations (5.4) and (5.5) yield
ejω(cid:1)tcosθ+1+e−jω(cid:1)tcosθ
Yˆ =
c 1+2cos2θ
1+2cosθcosω(cid:1)t
Yˆ =
c 1+2cos2θ
and
ejω(cid:1)t−e−jω(cid:1)t
Yˆ =
s 2sinθ
sinω(cid:1)t
Yˆ =j
s sinθ
Itcanbeseen,for example, that,ify(t) = Re{ejωot} = cosω t,Yˆ = 1,andYˆ = 0.
o c s
In general, if y(t) = Re{ej(ωt+ϕ)} =cos (ωt+ϕ) then
(cid:2) (cid:3)
1+2cosθcosω(cid:1)t
Yˆ = cosϕ
c 1+2cos2θ
(cid:2) (cid:3)
sinω(cid:1)t
Yˆ = sinϕ
s sinθ
(cid:29)
The two bracketed terms are plotted in Figure 5.8 along with (Yˆ2+Yˆ2)/2 (the
c s
magnitude for ϕ = 45◦) for θ = 30◦ (12 samples per cycle). Since two quantities
are being computed, there are two frequency responses. The choice of angle ϕ that
is used in presenting the magnitude is somewhat arbitrary. We will use ϕ = 45◦ for
consistency.
Different frequency responses are obtained for different values of c and c in
1 2
Equations (5.6) and (5.7). The Prodar 70 algorithm was specifically designed to
cos coefficient
2.0
Mann-Morrison
magnitude
magnitude
1.0
sin coefficient
0 60 240 360 Hz
Figure 5.8 Frequency responses of Equations (5.4) and (5.5) along with the Mann-
Morrison algorithm

| Relaying | as parameter | estimation |     |     |     |     | 147 |
| -------- | ------------ | ---------- | --- | --- | --- | --- | --- |
10
6
2
0
|     |     |            |           | 0 120 | 240 360         | Hz                  |     |
| --- | --- | ---------- | --------- | ----- | --------------- | ------------------- | --- |
|     |     | Figure 5.9 | Frequency |       | response of the | Prodar 70 algorithm |     |
reduce low frequency response. The frequency responses of the Mann-Morrison
and the Prodar 70 algorithms at the same sampling rate of 12 samples per cycle are
| shown | in Figure | 5.8 and | Figure | 5.9. |     |     |     |
| ----- | --------- | ------- | ------ | ---- | --- | --- | --- |
The algorithms compared in Figures 5.8 and 5.9 represent three samples at a
rate of 12 samples per cycle, or a quarter of a cycle. As such, they do not reject
non-fundamental frequency components (particularly the third harmonic) as well as
might be necessary in many applications. These algorithms are fast in that the short
windowwillbeentirelyinthepost-faultregionquickly.Wewillseelaterthatlonger
window algorithms have a greater ability to reject non-fundamental frequencies at
the expense of a longer decision time (the longer window takes longer to clear the
instantoffaultinception).Thisisageneralresultwhichwewilldevelopthroughout
this chapter. That is, there is an inherent speed-reach limitation in line relaying
caused by the presence of random signals in the measured voltages and currents.
The reach of the relay (the setting of the boundary of the zone of protection) is
directly related to the accuracy of the estimates formed by the algorithm.
| 5.3 Relaying |     | as  | parameter | estimation |     |     |     |
| ------------ | --- | --- | --------- | ---------- | --- | --- | --- |
IfEquation(5.14)isgeneralizedtoincludeanumberofknownsignalsincludingthe
fundamentalfrequencycomponents,ageneralprobleminestimatingthecoefficients
of the known signals can be posed. The resulting solution encompasses a number
of relaying algorithms. The signal to be sampled is written as
(cid:5)N
|     |     |     |     | y(t) | (t)+ε(t) |     |        |
| --- | --- | --- | --- | ---- | -------- | --- | ------ |
|     |     |     |     | =    | Y n s n  |     | (5.16) |
n=1
or
(cid:5)N
|     |     |     |     | y = | Y s (k(cid:1)t)+ε(t) |     | (5.17) |
| --- | --- | --- | --- | --- | -------------------- | --- | ------ |
|     |     |     |     | k   | n n                  |     |        |
n=1

| 148 |     |     |     |     |     |     | Transmission |     | line relaying |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- |
where the signals s(t) are assumed known but the coefficients Y n are unknown. The
| obvious | choices for | the signals | include: |     |     |     |     |     |     |
| ------- | ----------- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
(cid:15)
(t)= cosω
|     |     | s      |      | t   |              |     |         |     |     |
| --- | --- | ------ | ---- | --- | ------------ | --- | ------- | --- | --- |
|     |     | 1      |      | o   |              |     |         |     |     |
|     |     |        |      |     | the previous |     | example |     |     |
|     |     | s (t)= | sinω | t   |              |     |         |     |     |
|     |     | 2      |      | o   |              |     |         |     |     |
(cid:15)
(t)= cos2ω
|     |     | s      |       | t   |            |          |     |     |     |
| --- | --- | ------ | ----- | --- | ---------- | -------- | --- | --- | --- |
|     |     | 3      |       | o   |            |          |     |     |     |
|     |     |        |       |     | the second | harmonic |     |     |     |
|     |     | s (t)= | sin2ω | t   |            |          |     |     |     |
|     |     | 4      |       | o   |            |          |     |     |     |
(cid:30)
.
|     |     | . . | other harmonics |     |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
e−(R/L)t
| s (t) = | the | exponential |     | offset |     |     |     |     |     |
| ------- | --- | ----------- | --- | ------ | --- | --- | --- | --- | --- |
N
The problem then is to estimate the coefficients Y from the measurements Y .
n k
The least squares technique from Chapter 3 is appropriate if we write
|     |       |    |               |                 |               |   |      |    |      |
| --- | ------- | --- | ------------- | --------------- | ------------- | --- | ----- | --- | ----- |
|     | y       |     | s ((cid:1)t)s | ((cid:1)t)···s  | ((cid:1)t)    |     | Y     |     | ε     |
|     | 1       |     | 1             | 2               | N             |     | 1     |     | 1     |
|     |       |    |               |                 |               |   |      |    |      |
|     | y     | s  | (2(cid:1)t)s  | (2(cid:1)t)···s | (2(cid:1)t) |     | Y    | ε  |      |
|     | 2       |    | 1             | 2               | N             |     | 2     |    | 2     |
|     |       | =   |               |                 |               |   |  + |     |      |
|     |  . .  |    |               | . .             |               |   | . .   |     | . .  |
|     |  .    |    |               | .               |               |   | .    |    | .    |
|     |         |     | (k(cid:1)t)s  | (k(cid:1)t)···s | (k(cid:1)t)   |     |       |     | ε     |
|     | y       | s   |               |                 |               |     | Y     |     |       |
|     | k       |     | 1             | 2               | N             |     | N     |     | k     |
or
Y+ε
|     |     |     |     | y = | S   |     |     |     | (5.18) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
where Equation (5.18) represents k equations in N unknowns. It is clear that k ≥ N
is required in order to estimate all of the N parameters. If the error vector ε is
E{ε}
| assumed | to have zero | mean, | i.e. | =0  | and a | covariance | matrix |     |     |
| ------- | ------------ | ----- | ---- | --- | ----- | ---------- | ------ | --- | --- |
E{εεT}
|     |     |     |     |     | = W |     |     |     | (5.19) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
then the solution from Section 3.7 (Equation (3.77)) is appropriate and yields
|     |     |     | Yˆ = | (STW−1S)−1STW−1y |     |     |     |     |     |
| --- | --- | --- | ---- | ---------------- | --- | --- | --- | --- | --- |
(5.20)
| The estimate | given        | by Equation |        | (5.20) | is unbiased, | i.e.       |     |     |        |
| ------------ | ------------ | ----------- | ------ | ------ | ------------ | ---------- | --- | --- | ------ |
|              |              |             |        | E{Yˆ}  | =E {Y}       |            |     |     | (5.21) |
| and has      | a covariance |             |        |        |              |            |     |     |        |
|              |              | E{(Yˆ       | −Y)(Yˆ | −Y)T}  | =            | (STW−1S)−1 |     |     | (5.22) |

| Relaying | as parameter | estimation |            |     |     |     | 149 |
| -------- | ------------ | ---------- | ---------- | --- | --- | --- | --- |
| 5.3.1    | Curve        | fitting    | algorithms |     |     |     |     |
(5.20)5,6
The algorithms developed along the lines of Equation have assumed, in
essence, that W is a multiple of a unit matrix (the errors are uncorrelated and
independent from sample to sample and have a constant covariance) so that the
| least squares |     | solution is |     |     |            |     |        |
| ------------- | --- | ----------- | --- | --- | ---------- | --- | ------ |
|               |     |             |     | Yˆ  | (STS)−1STy |     |        |
|               |     |             |     | =   |            |     | (5.23) |
The matrix (STS)−1ST can be computed off-line and stored. In fact, only the two
|     |     |     |     |     | cosω | sinω |     |
| --- | --- | --- | --- | --- | ---- | ---- | --- |
rows of the matrix that correspond to 0 t and 0 t are needed for impedance
relaying (the ratio of the fundamental frequency voltage and current is sufficient).
If the DC offset (the exponential decay in the fault current) is included, the matrix
(STS)−1ST isfull,sothatafullsetof2knumbersisneeded.Inadditiontoanumber
of harmonics and the magnitude of the offset, the time constant of the line itself
estimated.5
| has been | included | in the     | parameters |     | to be |     |     |
| -------- | -------- | ---------- | ---------- | --- | ----- | --- | --- |
| 5.3.2    | Fourier  | algorithms |            |     |       |     |     |
If, as in the curve fitting algorithms, W is assumed to be a multiple of a unit matrix
and if the DC offset is removed with an analog filter or with a separate piece of
software (see Section 5.3.8) then Equations (5.20) or (5.23) becomes particularly
(t)}
simple. If only the fundamental and harmonics are included in the signal set {s
n
and an even number of sample panning a full period is used then Equation (5.23)
becomes a rectangular form of the DFT. With K samples per cycle (K/2-1) har-
monics can be computed. Using the orthogonality of the sine and cosine terms, the
| ijth entry | of the | matrix STS | is  |     |     |     |     |
| ---------- | ------ | ---------- | --- | --- | --- | --- | --- |
(cid:5)K
|     |     |     | (STS) | =   | s(k(cid:1)t)s(k(cid:1)t) |     |     |
| --- | --- | --- | ----- | --- | ------------------------ | --- | --- |
|     |     |     |       | ij  | i                        | j   |     |
k=1
|                 |     |           |            | =   | K/2;i         | = j      | (5.24) |
| --------------- | --- | --------- | ---------- | --- | ------------- | -------- | ------ |
|                 |     |           |            | =   | 0; i (cid:6)= | j        |        |
| The fundamental |     | frequency | components |     | are           | given by |        |
(cid:5)K
2
|     |     |     | Yˆ  |     |     | cos(kθ) |        |
| --- | --- | --- | --- | --- | --- | ------- | ------ |
|     |     |     |     | c = |     | y k     | (5.25) |
K
k=1
(cid:5)K
2
|     |     |     | Yˆ  | =   |     | y sin(kθ) | (5.26) |
| --- | --- | --- | --- | --- | --- | --------- | ------ |
|     |     |     |     | s   |     | k         |        |
K
k=1

| 150       |                  |     |     | Transmission | line relaying |
| --------- | ---------------- | --- | --- | ------------ | ------------- |
| while for | the pth harmonic |     |     |              |               |
(cid:5)K
2
|     |     | Yˆ(p) | cos(pkθ) |     |        |
| --- | --- | ----- | -------- | --- | ------ |
|     |     | =     | y        |     | (5.27) |
|     |     | c     | K k      |     |        |
k=1
(cid:5)K
2
|     |     | Yˆ(p) | sin(pkθ) |     |        |
| --- | --- | ----- | -------- | --- | ------ |
|     |     | =     | y        |     | (5.28) |
|     |     | s     | K k      |     |        |
k=1
| θ   | 2π/K. |     |     |     |     |
| --- | ----- | --- | --- | --- | --- |
where = As in the Kalman filter case in Section 3.9 under the assumption
of a constant variance error model and the external removal of the offset, the DFT
is an optimal estimate of the fundamental and of all of the harmonics permitted by
the sampling rate. The estimates of the harmonics given in Equations (5.27) and
(5.28) are not used in line relaying but do play a role in transformer protection, as
| will be | seen in Chapter | 6.  |     |     |     |
| ------- | --------------- | --- | --- | --- | --- |
The concept of the frequency response of algorithms which take real samples
and produce a complex output is subtle. Both Equations (5.25) and (5.26) have
frequency responses shown in Figure 5.10a. Both frequency responses have even
magnitudes (as a function of ω) and odd phases. The cosine channel is superior for
frequencies above the fundamental, while the sine is better below the fundamental.
Both parts are required to compute the complex phasor output. A filter with a real
input but having a complex output would have a frequency response such as shown
1.4
|     | sine | cosine |     |     |     |
| --- | ---- | ------ | --- | --- | --- |
1.2
| 1   |     |     | 1   |     |     |
| --- | --- | --- | --- | --- | --- |
0.9
| 0.8 |     |     | 0.8 |     |     |
| --- | --- | --- | --- | --- | --- |
0.7
| 0.6 |     |     | 0.6 Complex |     |     |
| --- | --- | --- | ----------- | --- | --- |
0.5
Fourier
| 0.4 |     |     | 0.4 |     |     |
| --- | --- | --- | --- | --- | --- |
0.3
| 0.2 |     |     | 0.2 |     |     |
| --- | --- | --- | --- | --- | --- |
0.1
| 0   |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- |
−400 −300 −200 −100 0 100 200 300 400 −400 −300 −200 −100 0 100 200 300 400
|     |     | (a) |     | (b) |     |
| --- | --- | --- | --- | --- | --- |
1
0.9
0.8
0.7 Least squares
0.6
0.5
0.4
0.3
0.2
0.1
| −0 400 | −300 −200 −100 | 0 100 200 300 | 400 |     |     |
| ------ | -------------- | ------------- | --- | --- | --- |
(c)
Figure5.10 Frequencyresponseoffull-cyclealgorithmsat12samplespercycle.(a)Sine
| and Cosine. | (b) Complex | Fourier. (c) Least | squares fitting |     |     |
| ----------- | ----------- | ------------------ | --------------- | --- | --- |

| Relaying | as  | parameter | estimation |     |     |     |     |     |     | 151 |
| -------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
in Figure 5.10b. Note the frequency response does not have an even magnitude
and odd phase. The frequency response of the least squares algorithm is shown in
Figure 5.10c for a sampling rate of 12 samples a cycle. It can be seen that the
Fourier algorithm rejects DC while the least squares algorithm does not. The fitting
algorithm does reject the exponential it was designed to reject, of course, and has
the advantage that no external filtering is required to eliminate the exponential. The
disadvantage is that the computation is quite a bit more complicated. We will see
in a later section that the Fourier algorithm can be made particularly simple by a
suitable choice of the sampling frequency. The additional filtering provided by a
longer window is obvious if Figure 5.10 is compared with Figure 5.8.
| 5.3.3 | Fourier |     | algorithms | with | shorter | windows |     |     |     |     |
| ----- | ------- | --- | ---------- | ---- | ------- | ------- | --- | --- | --- | --- |
If only the fundamental frequency components are included in the signal set {s (t)},
n
the Fourier-like calculations can be carried out for windows of any length. The
|     |     |     |     | (STS) |     |     |     |     | 2×2 |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
difference is that the matrix is no longer diagonal. It is only a matrix,
| however. |                   | Equation | (5.23)         | becomes: |           |                |     |            |         |     |
| -------- | ----------------- | -------- | -------------- | -------- | --------- | -------------- | --- | ---------- | ------- | --- |
|          |                   |         |                |          |           |                |    |           |         |    |
|          | (cid:26) (cid:27) |          | (cid:10)K      |          | (cid:10)K |                | −1  | (cid:10)K  |         |     |
|          |                   |          | cos2(kθ)       |          |           | cos(kθ)sin(kθ) |     |            | cos(kθ) |     |
|          |                   |         |                |          |           |                |    |           | y       |    |
|          | Yˆ                |          |                |          |           |                |     |            | k       |     |
|          | c                 |         | k = 1          |          | k =       | 1              |    |  k =      | 1       |    |
|          |                   | =       | (cid:10)       |          | (cid:10)  |                |    |  (cid:10) |         |    |
|          | Yˆ                |          | K              |          | K         |                |     | K          |         |     |
|          | s                 |          | cos(kθ)sin(kθ) |          |           | sin2(kθ)       |     |            | sin(kθ) |     |
y k
|     |     |     | k=1 |     | k=1 |     |     | k=1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(5.29)
These are the estimates of Section 3.9 obtained from the Kalman filter under
the assumptions of no initial estimate and a constant covariance matrix for the
measurement error. With K = 3 they are a shifted version of Equations (5.4) and
(5.5), and with θ = 2π/K they correspond to the full-cycle Fourier. With an even
number of samples per half-cycle, Equation (5.29) generates the half-cycle Fourier
algorithm.7
(cid:5)K
2
|     |     |     |     | Yˆ  | =   | y cos(kθ) |     |     |     | (5.30) |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ------ |
|     |     |     |     |     | c   | k         |     |     |     |        |
K
k=1
(cid:5)K
2
|     |     |     |     | Yˆ  | =   | y sin(kθ) |     |     |     | (5.31) |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ------ |
|     |     |     |     |     | s   | k         |     |     |     |        |
K
k=1
Thefrequencyresponseofthehalf-cycleFourieralgorithmisshowninFigure5.11.
It can be seen that the shorter window algorithm still rejects the odd harmonics but
has lost the ability to reject even harmonics. The DC response is also poor. The
algorithmwasintendedtobeusedwithanexternalfiltertoeliminatetheexponential
| offset | in the | current. |     |     |     |     |     |     |     |     |
| ------ | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |

| 152 |     |     |     |     |     |     | Transmission | line relaying |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- |
1.0
0.6
0.2
0
|     |     |     |     | 0 120 | 240 | 360 Hz |     |     |
| --- | --- | --- | --- | ----- | --- | ------ | --- | --- |
Figure 5.11 Frequency response of half-cycle Fourier algorithm, 12 samples per cycle
| 5.3.4 Recursive |     | forms |     |     |     |     |     |     |
| --------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
The Fourier calculations in Equations (5.25) and (5.26) or Equations (5.30) and
(5.31) represent more calculations than are actually necessary in practice. In addi-
tion, the computed phasor rotates as in Equation (5.13). If we examine the complex
form for the computation involving samples ending at L and drop the factor of 2/K
in Equations (5.25) and (5.26) or Equations (5.30) and (5.31),
(cid:5)L
|     |     |     | (L) |     | e−j(k+K−L)θ |     |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
|     |     |     | Y   | =   | y           |     |     |     |
k
k=L−K+1
and rotate by an angle of (K−L)θ to keep the result stationary
(cid:5)L
|     |     |     | Y˜(L) | (L) ej(K−L)θ |     |     | e−jkθ |        |
| --- | --- | --- | ----- | ------------ | --- | --- | ----- | ------ |
|     |     |     | =     | Y            | =   | y   |       | (5.32) |
k
k=L−K+1
and
(cid:5)L−1
|     |     |     |     | Y˜(L−1) |     | e−jkθ |     |        |
| --- | --- | --- | --- | ------- | --- | ----- | --- | ------ |
|     |     |     |     |         | = y |       |     | (5.33) |
k
k=L−K
The difference between Equations (5.32) and (5.33) is the last term of (5.32) and
| the first term | of  | Equation | (5.33), | i.e. |       |           |     |     |
| -------------- | --- | -------- | ------- | ---- | ----- | --------- | --- | --- |
|                |     | Y˜(L)    | Y˜(L−1) |      | e−jLθ | e−j(L−K)θ |     |     |
|                |     |          | =       | +[y  | −y    |           | ]   |     |
|                |     |          |         |      | L     | L−K       |     |     |
or
|     |     |     | Y˜(L) = | Y˜(L−1) | +[y −y | ejKθ | ]e−jLθ | (5.34) |
| --- | --- | --- | ------- | ------- | ------ | ---- | ------ | ------ |
|     |     |     |         |         | L      | L−K  |        |        |
Equation (5.34) is valid for any length window (any K). If Kθ is not a multiple of a
half-cycle then the real and imaginary parts of Equation (5.34) must be multiplied

| Relaying | as parameter estimation |     |     | 153 |
| -------- | ----------------------- | --- | --- | --- |
Kθ 2π
by the matrix (STS)−1 to form the estimates. For the full-cycle window, =
| and the | recursive form | of the full-cycle algorithm | becomes  |        |
| ------- | -------------- | --------------------------- | -------- | ------ |
|         | Yˆ(new)        | =Yˆ(old) +[y −y             | ]cos(Lθ) | (5.35) |
old
|     |         | c c new  |          |        |
| --- | ------- | -------- | -------- | ------ |
|     | Yˆ(new) | =Yˆ(old) | ]sin(Lθ) |        |
|     |         | +[y −y   |          | (5.36) |
|     |         | s s new  | old      |        |
where y is the newest sample corresponding to L and y is the oldest sam-
new old
ple corresponding to a full cycle earlier. If the signal is a purely periodic signal
y = y andthephasordoesnotchange.Noticealsothatonlyonemultiplication
new old
and one addition are required to accomplish the update of the real and imaginary
parts of the phasor estimate. The half-cycle versions of Equations (5.35) and (5.36)
| Kθ   | π       |          |          |        |
| ---- | ------- | -------- | -------- | ------ |
| with | = are   |          |          |        |
|      | Yˆ(new) | =Yˆ(old) | ]cos(Lθ) |        |
|      |         | +[y +y   |          | (5.37) |
|      |         | c c new  | old      |        |
Yˆ(new) =Yˆ(old)
|     |     | +[y +y  | ]sin(Lθ) | (5.38) |
| --- | --- | ------- | -------- | ------ |
|     |     | s s new | old      |        |
where y and y are a half cycle apart in Equations (5.37) and (5.38). Again
|     | new old |     |     |     |
| --- | ------- | --- | --- | --- |
=
if y new y (a pure fundamental frequency signal or a signal with only odd
old
harmonics) the phasor is unchanged. The missing factor of 2/K may be included in
| the scaling | of the numbers | in the microprocessor. |     |     |
| ----------- | -------------- | ---------------------- | --- | --- |
AlthoughtherecursiveformsoftheFouriercalculationsareparticularlysimple,it
must be recognized that a large number of currents and voltages must be processed
for full three-phase protection of a transmission line (see Section 5.4). The calcu-
lations can be further simplified by clever choice of the sampling rate. A sampling
rate of four times a cycle would only require the sines and cosines of multiples
of 90◦ (i.e. 0, ±1) and hence make the update a pure addition. Unfortunately this
is a rather slow sampling rate for some applications. If the rate is increased to
eight times a cycle, sines and cosines of multiples of 45◦ are required (0, ±1 and
| √   |     |     | √   |     |
| --- | --- | --- | --- | --- |
± 2/2). At 12 times a cycle, the multipliers are 0, ±1, ±1/2, and 3/2. In each
of the latter cases, the multiplication by an irrational number can be accomplished
externally by an analog voltage divider, or approximated in software by a number
| of shifts | and adds. |     |     |     |
| --------- | --------- | --- | --- | --- |
| Example   | 5.2       |     |     |     |
√
An approximation to 3/2 can be obtained for a 16 bit processor as
√
|     | 3/2 | = 2−1+3×2−3−2−7−2−10−3×2−14 |     |     |
| --- | --- | --------------------------- | --- | --- |
|     |     | 0.8660254 ∼ 0.8660278       |     |     |
=

| 154 |     |     | Transmission | line relaying |
| --- | --- | --- | ------------ | ------------- |
The error of 0.0000024 is less than 2−16. In fact, it is not clear that the first three
or four terms are not adequate. The implementation of the five term approximation
then involves a sequence of shifts and adds and, in one implementation, is done
while the next sample is being converted by the A/D converter.
| 5.3.5 Walsh function | algorithms |     |     |     |
| -------------------- | ---------- | --- | --- | --- |
The Walsh functions have the advantage that all of the multiplications required in
the evaluation of Equation (5.23) are ±1. If we take N = 2n and let
(t) (t)
|     |     | s = w |     | (5.39) |
| --- | --- | ----- | --- | ------ |
|     |     | n n   |     |        |
where the Walsh functions are defined as in Section 3.3, then
|     | (STS)−1 | 2−n |     |        |
| --- | ------- | --- | --- | ------ |
|     |         | = I |     | (5.40) |
(cid:5)2n
1
|     | Yˆ = | y w (kθ) |     | (5.41) |
| --- | ---- | -------- | --- | ------ |
|     | n    | 2n k n   |     |        |
k=1
Example 5.3
ThefirstfourWalshfunctionsareshowninFigure5.12alongwiththesamplevalues
(kθ).
w n An expansion in terms of the first four Walsh functions would involve the
calculations
1
|     | Yˆ  | (y       | )   |     |
| --- | --- | -------- | --- | --- |
|     | 1 = | +y +y +y |     |     |
|     | 4   | 1 2 3    | 4   |     |
1
|     | Yˆ = | (y +y −y −y | )   |     |
| --- | ---- | ----------- | --- | --- |
|     | 2    | 3           | 4   |     |
|     | 4    | 1 2         |     |     |
1
|     | Yˆ = | (y −y −y +y | )   |     |
| --- | ---- | ----------- | --- | --- |
|     | 3    | 1 2 3       | 4   |     |
4
1
|     | Yˆ = | (y −y +y −y | )   |     |
| --- | ---- | ----------- | --- | --- |
|     | 4    | 1 2 3       | 4   |     |
4
The only problem with the Walsh expansion is that explained in Section 3.3.
A large number of Walsh terms must be included in order to obtain an accurate
estimate of the components. The advantage of the simplicity of Equation (5.41)
is counterbalanced by the need for a large number of terms and the need to
convert from Walsh to Fourier. The frequency response of the Walsh algorithm

| Relaying | as parameter | estimation |     |     | 155 |
| -------- | ------------ | ---------- | --- | --- | --- |
W (t)
0
1
W (t)
|     |     | 1   | 1/2 | 1   |     |
| --- | --- | --- | --- | --- | --- |
W (t)
2
|     |     |     | 1/4 | 3/4 |     |
| --- | --- | --- | --- | --- | --- |
1
W (t)
|     |     | 3   | 1/4 1/2 | 3/4 1 |     |
| --- | --- | --- | ------- | ----- | --- |
Figure 5.12 The first four Walsh functions and their sample values
is indistinguishable from the full-cycle Fourier algorithm if a sufficient number of
| Walsh coefficients |                       | are used. |            |     |     |
| ------------------ | --------------------- | --------- | ---------- | --- | --- |
| 5.3.6              | Differential-equation |           | algorithms |     |     |
The differential-equation algorithms represent a second major theme in line relay-
ing. The algorithms described so far in this chapter are based on a description of
the waveforms and are essentially impedance relay algorithms. These algorithms
attempt to estimate the fundamental frequency components of currents and voltages
inordertocomputetheimpedancetothefault.Thedifferential-equationalgorithms,
on the other hand, are based on a model of the system rather than on a model of
the signal. They can still be regarded as parameter estimation, however. If we
take the single-phase model of the faulted line shown in Figure 5.2 and write the
differential-equation relating the voltage and current seen by the relay, we obtain
di(t)
|     |     |     | v(t) i(t)+L |     |        |
| --- | --- | --- | ----------- | --- | ------ |
|     |     |     | = R         |     | (5.42) |
dt
Since both v(t) and i(t) are measured, it seems possible that we can estimate the
parameters R and L and hence the distance to the fault. Since derivatives of mea-
sured quantities are difficult to produce, McInnes and Morrison obtained a more

156 Transmission line relaying
tractable form of Equation (5.42) by integrating the Equation (5.42) over two con-
secutive intervals:8
(cid:4)t1 (cid:4)t1
v(t)dt = R i(t)dt+L[i(t )−i(t )] (5.43)
1 0
t0 t0
(cid:4)t2 (cid:4)t2
v(t)dt = R i(t)dt+L[i(t )−i(t )] (5.44)
2 1
t1 t1
The integrals in Equations (5.43) and (5.44) must be approximated from the sample
values. If the samples are equally spaced at an interval (cid:1)t and the trapezoidal rule
is used for the integrals, viz.
(cid:4)t1
(cid:1)t (cid:1)t
v(t)dt = [v(t )+v(t )] = [v +v ]
1 0 1 2
2 2
t0
then Equations (5.43) and (5.44) can be written for samples at k, k+1, and k+2 as
   
(cid:1)t (cid:26) (cid:27) (cid:1)t
 (i k+1 +i k ) (i k+1 −i k )  R  (v k+1 +v k ) 
 2  =  2 
(cid:1)t (cid:1)t
(i +i ) (i −i ) L (v +v )
k+2 k+1 k+2 k+1 k+2 k+1
2 2
The three samples of current and voltage are sufficient to compute estimates of
R and L as
(cid:2) (cid:3)
(v +v )(i −i )−(v +v )(i −i )
k+1 k k+2 k+1 k+2 k+1 k+1 k
R= (5.45)
(i +i )(i −i )−(i +i )(i −i )
k+1 k k+2 k+1 k+2 k+1 k+1 k
(cid:2) (cid:3)
(cid:1)t (i +i )(v +v )−(i +i )(v +v )
k+1 k k+2 k+1 k+2 k+1 k+1 k
L= (5.46)
2 (i +i )(i −i )−(i +i )(i −i )
k+1 k k+2 k+1 k+2 k+1 k+1 k
Equations (5.45) and (5.46) can be roughly compared with Equations (5.4) and
(5.5), the three sample phasor calculations. Both the current and voltage phasors
must be computed using Equations (5.4) and (5.5) and then a complex division
performedtoobtaintheimpedancetothefault.Equations(5.45)and(5.46)represent
thetotalcomputationinvolvedinprocessingthesixsamples(threecurrentandthree
voltagesamples).Intotal,thesixmultiplicationsandtworealdivisionsinEquations
(5.45) and (5.46) compare favorably with computation of Equations (5.4) and (5.5)
for current and voltage followed by a complex division which would also involve

Relaying as parameter estimation 157
six multiplications and two real divisions in the form
a+jb (ac+bd) (bc−ad)
= +j
c+jd c2+d2 c2+d2
The actual difference in speed would depend on the angle θ in Equations (5.4)
and (5.5).
The algorithm given by Equations (5.45) and (5.46) is the differential-equation
counterpart of the short window algorithm given by Equations (5.6) and (5.7) and
as such is not as selective as longer window algorithms. The extension of the
differential-equation approach to a longer window takes a number of forms. One
approach is to make the intervals [t ,t ] and [t ,t ] in Equations (5.43) and (5.44)
o 1 1 2
longer. It is possible to select the intervals so that certain harmonics are rejected.9
If the intervals contain a number of samples, the trapezoidal approximation to
each of the integrals will contain sums of a number of samples. Another approach
is to do the trapezoidal integration over the interval between adjacent samples and
obtain an over defined set of equations in the form
   
(cid:1)t (cid:1)t
 (i k+1 +i k ) (i k+1 −i k )   (v k+1 +v k ) 
 2    2 
    (cid:1) 2 t (i k+2 +i k+1 ) (i k+2 −i k+1 )      R  =     (cid:1) 2 t (v k+2 +v k+1 )    
  . . . . . .   L   . . .  
   
(cid:1)t (cid:1)t
(i +i ) (i −i ) (v +v )
k+N k+N−1 k+N k+N−1 k+N k+N−1
2 2
The least squares solution of the over defined equations would involve a large
number of multiplications in forming the equivalent of the matrix (STS). To avoid
some of these problems, a technique of using a sequence of estimates, each of
which is obtained from the three-sample algorithm, has been developed.10 Suppose
a region of the R-L plane is chosen to correspond to zone-1 protection of the line.
If the result of the three-point calculation Equations (5.45) and (5.46) lies in the
characteristic, a counter is indexed by one. If the computed values lie outside the
characteristic,thecounterisreducedbyone.Withathresholdoffouronthecounter,
i.e. a trip signal cannot be issued unless the counter is at four, a minimum of six
consecutive samples is required. The window length is thus increased by increasing
the counter threshold.
Although ingenious, the counting schemes are difficult to compare with other
long window algorithms in terms of frequency response. An additional problem in
giving the frequency response of the differential-equation algorithms is that there
are two signals involved, i(t) and v(t). To obtain some comparison, Figure 5.13 is
a frequency response obtained for the average of consecutive three-sample results

| 158 |         |     |            | Transmission | line relaying |
| --- | ------- | --- | ---------- | ------------ | ------------- |
|     | 1.0     |     | 1.0        |              |               |
|     | 0.5     |     | 0.5        |              |               |
|     | 0 0 120 | 240 | 360 Hz 0 0 | 120 240      | 360 Hz        |
|     |         | (a) |            | (b)          |               |
Figure 5.13 Frequency response of the average of consecutive three-sample calculations
for Equations (5.45) and (5.46). (a) One-half cycle window at 12 samples per cycle.
| (b) Full-cycle | window at | 12 samples | per cycle |     |     |
| -------------- | --------- | ---------- | --------- | --- | --- |
of Equations (5.45) and (5.46) spanning half-cycle and full-cycle windows at a
| sampling | rate of 12 samples | per cycle. |     |     |     |
| -------- | ------------------ | ---------- | --- | --- | --- |
In computing Figure 5.13, it was assumed that the current was the true funda-
mental frequency current but that thevoltage signal variedinfrequency. Inessence,
Figure5.13isthefrequencyresponseoftheaveragednumeratorofEquations(5.45)
and (5.46) with the denominator held at the fundamental frequency values. The
frequency response in Figure 5.13 can only roughly be compared with the ear-
lier responses. A different response is produced, for example, if the averaging is
done only for non-overlapping three-sample results. An additional problem with
the concept of frequency response for these algorithms is that as long as v(t) and
i(t) satisfy the differential-equation (no matter what frequencies are present in v(t)
| and i(t)) | then the computed | values                    | of R and L | are correct. |     |
| --------- | ----------------- | ------------------------- | ---------- | ------------ | --- |
| 5.3.6.1   | Error analysis    | for differential-equation |            | algorithms   |     |
The property identified in describing the frequency response of the differential-
equation algorithms, i.e. that the correct R and L are obtained as long as v(t)
and i(t) satisfy the differential equation, is a major strength of these algorithms.
The exponential offset in the current satisfies the equation if the correct values of
R and L are used, so that it need not be removed. We have seen in Section 5.2
that the voltage seen by the relay just after fault inception has non-fundamental
frequency components caused by the power system itself. If the faulted line can
accurately be modeled as a series R-L line, then the current will respond to these
non-fundamental frequency components in the voltage (according to the differential
equation) and no errors in estimating R and L will result. As long as the R-L
representation is correct, then the only sources of error are in the measurement of
v(t) and i(t). Transducer errors, A/D errors, and errors in the anti-aliasing filters
contribute portions of the measured voltage and current which do not satisfy the
differential equation and which will cause errors in the estimates. The frequency

| Relaying | as  | parameter | estimation |     |     |     |     |     |     | 159 |
| -------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
responseinFigure5.13representstheresponseofthealgorithmtosucherrorsignals
in the measured voltage. To examine the effect of such errors in both voltage and
current, let the measured current and voltage be denoted by i m (t) and v m (t) where
(t)=i(t)+ε(t)
|     |     |     |     | i m |            | i   |     |     |     | (5.47) |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ------ |
|     |     |     |     | v   | (t)=v(t)+ε | (t) |     |     |     | (5.48) |
|     |     |     |     | m   |            | v   |     |     |     |        |
and v(t) and i(t) satisfy the differential equation. The current i (t) satisfies the
m
| differential |             | equation |                 |     |              |         |       |       |     |        |
| ------------ | ----------- | -------- | --------------- | --- | ------------ | ------- | ----- | ----- | --- | ------ |
|              |             |          |                 | di  | (t)          |         |       | dε(t) |     |        |
|              |             |          | (t)+L           | m   | v(t)+Rε(t)+L |         |       | i     |     |        |
|              |             |          | Ri              |     | =            |         |       |       |     | (5.49) |
|              |             |          | m               | dt  |              |         | i     | dt    |     |        |
| and          | the current | i m      | (t) and voltage |     | v m (t) are  | related | by:   |       |     |        |
|              |             |          |                 | (t) |              |         | dε(t) |       |     |        |
di
|     |     | i   | (t)+L | m = | v (t)+Rε(t)+L |     |     | i −ε | (t) | (5.50) |
| --- | --- | --- | ----- | --- | ------------- | --- | --- | ---- | --- | ------ |
|     |     | m   |       |     | m             | i   |     |      | v   |        |
|     |     |     |       | dt  |               |     |     | dt   |     |        |
The measured voltage and current then satisfy a differential equation with an error
term which is made up of the voltage error plus a processed current error term. The
latterissimilartotheerrorobtainedattheoutputofamimiccircuitwiththecurrent
error as an input (see Figure 5.16). Figure 5.13 then can finally be interpreted as
the response of the algorithm to the entire error term in Equation (5.50), assuming
that the sum of the last three terms on the right hand side of the equation are
(ωt);
thought of as a signal cos the last three terms in (5.50) also make it clear that
error signals that satisfy the differential equation do not contribute a net error to
| Equation | (5.50). |     |     |     |     |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thereisanadditionalsubtletyinthethree-sampledifferential-equationalgorithm.
The denominator of Equations (5.45) and (5.46) is not a constant but rather a func-
tion of time which has maxima and minima. The denominator can be simplified to
|     | (i        | +i )(i | −i      | )−(i  | +i        | )(i     | −i ) | = −2(i2 | −i i  | )   |
| --- | --------- | ------ | ------- | ----- | --------- | ------- | ---- | ------- | ----- | --- |
|     | k+1       | k      | k+2 k+1 |       | k+2       | k+1 k+1 | k    |         | k+1 k | k+2 |
| If  | we assume | that   |         |       |           |         |      |         |       |     |
|     |           |        |         |       |           |         | R    | (t−t )  |       |     |
|     |           |        |         | cos(ω | t)−Icos(ω | )e−−    |      |         |       |     |
|     |           |        | i = I   |       |           | t       | L    | o       |       |     |
|     |           |        | k+1     |       | o         | o o     |      |         |       |     |
|     |           |        |         | (θ    | 30o)      |         |      |         |       |     |
and use 12 samples per cycle = with a line time constant of 40ms, then
|     |          |       | (cid:2)              |     |     |               |     |     |        | (cid:3) |
| --- | -------- | ----- | -------------------- | --- | --- | ------------- | --- | --- | ------ | ------- |
|     | (cid:18) |       | (cid:19)             |     |     |               |     |     | (t−t   | )       |
|     |          |       |                      |     |     | t+7.41◦)cos(ω |     |     | − R    |         |
|     | 2 i2     | −i i  | = I2 0.5−0.5384cos(ω |     |     |               |     |     | t )e L | o       |
|     | k+1      | k k+2 |                      |     |     | o             |     | o   | o      |         |
The denominator is shown in Figure 5.14 as a function of the time of the kth
sample for the case of maximum offset (ω t = 0). When the denominator is small
0 0

160 Transmissionlinerelaying
0.5 I2
0
t
Figure 5.14 The denominator of Equations (5.45) and (5.46) for maximum offset in the
current
the error terms from Equation (5.50) are amplified. In the limit as the denominator
becomes zero the estimates are unacceptably sensitive to even the smallest error
terms. A counting algorithm will deal with such poor estimates by indexing down
because the estimate is not in the characteristic. The net effect is then only a delay
in issuing the trip signal. Since the denominator is a constant if the offset is absent,
it can be seen that the supposed immunity of the differential-equation algorithms
to offset is a bit of myth.
The preceding has assumed that the actual voltage and current satisfy the
differential equation but that there are errors made in the measurement process. As
seen in Section 5.2, the largest contributions to errors in the waveform algorithms
are non-fundamental frequency signals from the power system itself. If the
differential-equationalgorithmswereimmunetothesesignals,therewouldbemuch
to recommend them. A somewhat more realistic model of the faulted line can be
usedtoinvestigatetheimpactofthesepowersystemsignalsonsuchalgorithms.The
circuitshowninFigure5.15includestheshuntcapacitanceofthetransmissionlineat
therelayterminals.Thevoltagesourcev(t)representsthevoltagesseeninFigure5.5
made up of a fundamental plus non-fundamental components whose frequency and
phase are unpredictable. The current i(t) is the current measured by the relay. The
dv
{ i(t) -C }
dt
i(t)
L
v(t) C
Figure 5.15 A single-phase line model with shunt capacitance

Relaying as parameter estimation 161
actualrelationshipbetweenthemeasuredvoltageandcurrentisgivenby
di(t) dv(t) d2v(t)
v(t) = Ri(t)+L −RC −LC (5.51)
dt dt d2t
If the algorithm of Equations (5.45) and (5.46) is used then the last two terms in
Equation (5.51) must be regarded as error terms. The magnitude of these terms
is a function of fault location and of the frequency of the signals in v(t). The
dependence on fault location is quadratic, reaching a maximum for a fault at the
end of the line. For faults at the far end of a long high-voltage line, these terms can
be quite substantial, especially if high frequencies are included in v(t). On the other
hand, the terms RC and LC are small for close-in faults and on lower voltage lines.
A solution to this problem, of course, is to include the capacitance in the sys-
tem model. This has been proposed and central differences have been used to
approximate the derivatives in Equation (5.51).11 It seems desirable to integrate
Equation (5.51) once to recover some similarity with Equations (5.45) and (5.46).
If this is done and (cid:2) (cid:3)
dv(t) v −v
∼ k k−1
=
dt (cid:1)t
tk
then a more elaborate version of Equations (5.45) and (5.46) can be obtained by
considering four consecutive intervals
 
(cid:1)t −1
  2 (i k+1 +i k ) (i k+1 −i k ) −(v k+1 −v k ) (cid:1)t (v k+1 −2v k +v k−1 )  
  (cid:1)t −1  
  2 (i k+2 +i k+1 ) (i k+2 −i k+1 ) −(v k+2 −v k+1 ) (cid:1)t (v k+2 −2v k+1 +v k )  
  (cid:1)t −1  
 (i +i ) (i −i ) −(v −v ) (v −2v +v )
 2 k+3 k+2 k+3 k+2 k+3 k+2 (cid:1)t k+3 k+2 k+1 
 
(cid:1)t −1
(i +i ) (i −i ) −(v −v ) (v −2v +v )
2 k+4 k+3 k+4 k+3 k+4 k+3 (cid:1)t k+4 k+3 k+2
 
(cid:1)t
(v +v )
 k+1 k 
   2 
R  (cid:1)t 
×    R L C   =     (cid:1) 2 t (v k+2 +v k+1 )    (5.52)
 (v +v )
LC   2 k+3 k+2  
(cid:1)t
(v +v )
k+4 k+3
2
If Equation (5.52) is thought of as a partitioned matrix in the form
(cid:2) (cid:3)(cid:2) (cid:3) (cid:2) (cid:3)
M M p r
11 12 = 1 (5.53)
M M Cp r
21 22 2

| 162 |     |     |     |     |     |     | Transmission |     | line relaying |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- |
p
where is the parameter vector made up of R and L, then the estimate can be
formed by solving the second set of equations and substituting into the first set to
| obtain:11 | (cid:2) | (cid:3) |          |     |          |          |      |          |        |
| --------- | ------- | ------- | -------- | --- | -------- | -------- | ---- | -------- | ------ |
|           |         |         | (cid:16) |     | (cid:17) | (cid:16) |      | (cid:17) |        |
|           |         | Rˆ      |          |     |          | −1       |      |          |        |
|           |         |         |          |     | M−1M     |          | M−1r |          |        |
|           |         | =       | M −M     |     |          | r        | −M   |          | (5.54) |
|           |         | Lˆ      | 11       | 12  | 22 21    | 1        | 12   | 22 2     |        |
Equation(5.54)representsaformidableamountofcomputationgiventhatthematri-
ces involved are formed of measured voltages and currents. It is not clear that the
computationiswarrantedsincethepi-sectionrepresentationisstillanapproximation
| to the transmission |     | line   | model.     |     |     |     |     |     |     |
| ------------------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- |
| 5.3.7 Kalman        |     | filter | algorithms |     |     |     |     |     |     |
In1981, simulation experiments performed ona 345kV lineconnecting agenerator
and a load led to the conclusion that the covariance of the noise in the voltage and
current was not a constant but, rather, decayed in time. If the time constant of the
decayiscomparabletothedecisiontimeoftherelaythentheKalmanfiltersolution
of Section 3.9 is appropriate for the estimation problem. The voltage was modeled
| as in Equations |     | (3.83)  | and (3.84) | with    |         |     |                  |     |        |
| --------------- | --- | ------- | ---------- | ------- | ------- | --- | ---------------- | --- | ------ |
|                 |     | (cid:2) | (cid:3)    | (cid:2) | (cid:3) |     |                  |     |        |
|                 |     | Y       |            | 1       | 0       |     |                  |     |        |
|                 | X   | =       | c ,ϕ       | =       | ,and H  | =   | [cos(kθ)sin(kθ)] |     | (5.55) |
k
|     |     | Y   | s   | 0   | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
while a three-state model was used for the current to account for the offset. In
| particular, | the current |     | was assumed |     | to be described |     | by  |     |     |
| ----------- | ----------- | --- | ----------- | --- | --------------- | --- | --- | --- | --- |
|             |             |     |            |    |                |     |    |     |     |
|             |             |     |             | Y   | 1               | 0   | 0   |     |     |
c
|     |     |     | x =  | Y ,ϕ | =  0 | 1   | 0  |     | (5.56) |
| --- | --- | --- | ----- | ----- | ----- | --- | --- | --- | ------ |
s
e−β(cid:1)t
|     |     |     |     | Y   | 0   | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
and
|     |     |     |     | H = [cos(kθ)sin(kθ)1] |     |     |     |     | (5.57) |
| --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | ------ |
k
In both cases the covariance of the measurement noise was taken to be
e−k(cid:1)t/T
|     |     |     |     | R   | = K |     |     |     | (5.58) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
k
where K was different for voltage and current models and T was one-half the
expected time constant of the protected line. Using the error model given by
Equation (5.58) and a prior estimate for the state, the Kalman filter is required
| as shown | in Section | 3.9. |     |     |     |     |     |     |     |
| -------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
The Kalman-type description has been extended to an 11 state model including
two states for each of the fundamental through the fifth harmonic plus one state for

Relaying as parameter estimation 163
the offset.15 A constant error covariance was assumed, however, so that the only
justification for the Kalman filter as opposed to least squares or Fourier techniques
is the prior estimate. It should be recognized that either Kalman filter approach is a
waveformalgorithm,inthatthefundamentalfrequencyphasorsarebeingestimated.
Exact prior estimates of the fundamental frequency phasors are equivalent to prior
knowledge of the fault location and are not reasonable. Crude prior estimates are
obviously available (for example, the fault is within 1000 miles of the bus) but
such crude estimates will be quickly overcome by the measurements. The Kalman
filter approach cannot be justified simply to include a questionable prior estimate
of the fault location. It must be accepted that the only reason to use the Kalman
filter approach is to account for the time-varying measurement error model given
by Equation (5.58).
In examining the simulation model used to obtain Equation (5.58),12–14 the
absence of any network structure at the source bus is an obvious limitation. The
non-fundamental frequency terms described in Section 5.2 are produced by the net-
work structure. A line connected directly to a high short circuit capacity source
will not see these non-fundamental frequency terms. Other more detailed studies15
and field data16 support the conclusion that, although the error term decays, it does
so at a much slower rate than suggested by Equation (5.58) (for example, see
Figure 5.5). In summary, the Kalman filter approach is an alternate technique for
estimating the fundamental frequency components of voltage and current involving
considerably more computation than the alternatives, which is justified only if the
measurement error covariance decays significantly during the first cycle after the
fault.
5.3.8 Removal of the DC offset
One of the distinctions between the preceding algorithms is the treatment of the
offset in the current. The short window Fourier algorithms in particular require that
theoffsetberemoved prior toprocessing, whilethedifferential-equation algorithms
ideally do not require its elimination. Consider the R-L line model of Figure 5.16.
If the fault occurs at t = 0, while the voltage of the source is
(cid:31)
e(t) = 2 Ecos(ω t+φ) (5.59)
o
the fault current i(t) (assuming no pre-fault current in the circuit) is given by
√ √
2 E 2 E ω Rt
i(t)= (cid:31) cos(ω t+φ−(cid:5))− (cid:31) cos(φ−(cid:5))e o (5.60)
o
(R2+X2) (R2+X2) X
The second term in the expression for i(t) is the decaying DC component. The
traditional method of eliminating the DC component is with the use of a mimic

| 164 |     |     |     |     |     | Transmission | line relaying |
| --- | --- | --- | --- | --- | --- | ------------ | ------------- |
i(t)
e(t)
X
|     |     | e(t) |     | R   |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
v(t)
(a)
i(t)
i(t)
x
v(t)
(c)
r
(b)
Figure 5.16 Generation of exponentially decaying DC offset and its removal. (a) Fault
| circuit. (b) | Mimic | circuit. | (c) Voltage | and current | waveforms |     |     |
| ------------ | ----- | -------- | ----------- | ----------- | --------- | --- | --- |
circuitasshowninFigure5.16(b).ThefaultcurrentI(oritsanaloginthesecondary
winding of a current transformer) is passed through a burden of (r + jx) where
x/r = X/R. In this case, the voltage across the burden (r + jx) is given by
√
(cid:31)
2 E
|     |     | v(t)(cid:31) |     | (r2+x2)cos(ω |     | t+(cid:5)) |     |
| --- | --- | ------------ | --- | ------------ | --- | ---------- | --- |
(5.61)
|     |     |     | (R2+X2) |     |     | o   |     |
| --- | --- | --- | ------- | --- | --- | --- | --- |
This voltage v(t) is proportional to the fault current and is without the DC offset. It
can be used to represent the fault current. The phase angle of v(t) is different from
that of i(t) Indeed, v(t) is in phase with e(t), the voltage that produced the fault
current.
Figure 5.16 (c) shows the waveforms of the currents and voltages associated with
the fault circuit and the mimic circuit. The burden (r + jx) is known as the mimic
impedance, since it mimics the fault path impedance. Such circuits are commonly
| used in analog | and | digital | relays.7 |     |     |     |     |
| -------------- | --- | ------- | -------- | --- | --- | --- | --- |
It should benoted that the r and x of the mimicimpedance must be set to specific
values, whereas the fault circuit X/R may change depending upon network switch-
ing or fault arc resistance. In addition, any noise (or extraneous high frequency
components) present in the current tends to be amplified by the mimic circuit. In
the case of computer relays, the low-pass anti-aliasing filter attenuates a significant
| part of the | noise. |     |     |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- | --- | --- |
As microcomputer capabilities have improved, it has become possible to include
the mimic circuit representation within the microcomputer.17 Consider the samples
|               |             |     | k(cid:1)t, | 1,2,3...}.   |        |       |        |
| ------------- | ----------- | --- | ---------- | ------------ | ------ | ----- | ------ |
| of i(t) taken | at instants |     | {k         | =            | We may | write |        |
|               |             |     |            | γk+Y sinkθ+Y |        | coskθ |        |
|               |             |     | i k = Y    | o s          | c      |       | (5.62) |

| Relaying | as parameter |          | estimation |     |     |     |     |     | 165 |
| -------- | ------------ | -------- | ---------- | --- | --- | --- | --- | --- | --- |
| where,   | from         | Equation | (5.60),    |     |     |     |     |     |     |
√
2 E
|     |     |     | Y   | = −√ |     | cos(φ−(cid:5)) |     |     |     |
| --- | --- | --- | --- | ---- | --- | -------------- | --- | --- | --- |
o
R2+X2
√
2 E
|     |     |     | Y   | = −√ |     | sin(φ−(cid:5)) |     |     | (5.63) |
| --- | --- | --- | --- | ---- | --- | -------------- | --- | --- | ------ |
s
R2+X2
√
2 E
|     |     |     | Y   | = −√ |     | cos(φ−(cid:5)) |     |     |     |
| --- | --- | --- | --- | ---- | --- | -------------- | --- | --- | --- |
c
R2+X2
−θR
γ = e
X
γ
Assuming that the fault circuit X/R is known, in Equation (5.63) is known; and
Equation (5.62) for n samples (n>3) can be written as an over-determined set of
equations:
|     |     |     |    |         |     |     |         |    |     |
| --- | --- | --- | --- | -------- | --- | --- | -------- | --- | --- |
|     |     |     |     | (cid:26) |     |     | (cid:27) |     |     |
i
|     |     |     | 1        |     | γsinθsin2θ..  |     | Y   | o   |        |
| --- | --- | --- | -------- | --- | ------------- | --- | --- | --- | ------ |
|     |     |     |         |    |               |     |    |    |        |
|     |     |     | i = i 2 |  = |               |     | Y   |     | (5.64) |
|     |     |     | .        |     | γ2cosθcos2θ.. |     |     | s   |        |
.
|     |     |     | .   |     |     |     | Y   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c
or,
=
i JY
| from which | the | unknown | vector | Y   | can be | determined: |     |     |     |
| ---------- | --- | ------- | ------ | --- | ------ | ----------- | --- | --- | --- |
(JTJ)−1JTi
|     |     |     |     | Y   | =   |     |     |     | (5.65) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
The constants Y ,Ys,Yc having been found, the samples of v(t) can also be found.
0
| The k’th | sample | of  | v(t) is given | by  |     |     |     |     |     |
| -------- | ------ | --- | ------------- | --- | --- | --- | --- | --- | --- |
√
(cid:31)
|     |     |     |              | 2 E |                  |     |     |     |        |
| --- | --- | --- | ------------ | --- | ---------------- | --- | --- | --- | ------ |
|     |     |     | v = (cid:31) |     | (r2+x2)cos(kθ+ϕ) |     |     |     | (5.66) |
k
(R2+X2)
We may combine Equations (5.65) and (5.66) into a single algorithm for finding v
k
from i k :
|     |     |     | v = G(JTJ)−1JT[i−Y |     |     | (γ,γ2,...)T] |     |     | (5.67) |
| --- | --- | --- | ------------------ | --- | --- | ------------ | --- | --- | ------ |
o
where
|     |     |     |     |    |     |     |     |    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sin(θ+ψ)sin(2θ+ψ)..
|     |     |     | (cid:31)  |    |            |         |     | ..   |        |
| --- | --- | --- | --------- | --- | ---------- | ------- | --- | ----- | ------ |
|     |     |     |           |    | co s(θ+ψ)c | os(2θ+ψ |     | )    |        |
|     |     | G   | = (r2+x2) |     |            |         |     |       | (5.68) |
|     |     |     |           |    | .          | .       |     | . .  |        |
|     |     |     |           |     | .          | .       |     | ..    |        |

166 Transmission line relaying
Withthreedatapoints,Equation(5.67)hasnoredundancy.Withagreaternumberof
data points, the redundancy becomes favorable and the mimic circuit representation
becomeslessimmunetonoise.Thereferencecitedearliergivesexamplesoflabora-
toryexperimentswiththree-pointandsix-pointalgorithms.17 Ithasbeenshownthat
real-time elimination of DC offset by digital techniques is feasible, and produces
results comparable to those obtained with analog mimic circuits.
5.4 Beyond parameter estimation
There is a great deal more involved in a line relay than the estimation of the
parameters. It has been seen in Section 5.3 that all of the line relaying algorithms
can be thought of as attempts to estimate the parameters of the signal or of the
model of the faulted line. Comparisons of relaying algorithms based solely on their
abilitytoestimatetheseparametersarefraughtwithdifficulty.Differentassumptions
aboutthemeasurementerrorsproducedifferentoptimalestimates.Differentnetwork
models used in computer simulations produce different non-fundamental frequency
terms in the post-fault waveforms. Any algorithm can be made to circumvent a
particular deficiency by putting auxiliary features in the total relaying program.
For example, the short window Fourier algorithms are made insensitive to the
offset through the use of an external mimic impedance or its equivalent algorithm.
Comparisons of algorithmswhichdonot recognize theseauxiliaryfeaturescan lead
to absurd results.
A more complete comparison requires an understanding of the total relaying
program. Some of the issues which must be considered beyond the parameter esti-
mation are: determination of the fault type and how the fault type impacts the
parameter estimation; monitoring of the quality of the estimates; and speed-reach
considerations. Each of these issues will be examined in this section in a general
setting. Finally, one particular algorithm will be presented in more detail as an
example.
5.4.1 Relay programs based upon fault classification
The algorithms presented in the preceding sections are essentially single-phase
algorithms. The waveform algorithms are for a single current or voltage and the
differential-equationalgorithmsareforasingle-phaseR-Lmodel.Alinerelayusing
one of these algorithms would protect one terminal of a three-phase transmission
line. If the phases are labeled as a, b, c then there are a total of ten possible faults
that can be seen by the relay. They are
a – ground
b – ground
c – ground

Beyond parameter estimation 167
a – b
a – c
b – c
a – b – ground
a – c – ground
b – c – ground
a – b – c
Since the fault type is not known a-priori the algorithm must process samples of
all the voltages and currents in order to determine the fault type.
Conceptually, the simplest distance relaying algorithm would process six single-
phase distance Equations corresponding to three phase-ground faults and three
phase-phase faults. Early computers – and even modern microprocessors – would
be hard pressed to process all six distance Equations between successive samples.
It may be that the next generation of microprocessors will make such a proce-
dure practical. The overall flow chart of a relay program of this type is shown in
Figure 5.17. When a sample set of voltages and currents are acquired, the fault dis-
tance is estimated by assuming each of the six possible types (see Section 2.3). The
distance may be calculated by phasors or through the corresponding single-phase
differential equation. Once the six distances are computed, each is checked against
the relay characteristic to determine the appropriate relay response. It should be
noted that, for a given fault, only some of the distance calculations will produce
correct fault distances. Thus for a phase a-b fault, block 1 in Figure 5.17 will
produce the correct fault distance, while all other equations will produce distances
which lie outside the relay zones. Similarly, a phase a-b-g fault will produce cor-
rect fault distances in blocks 1, 4 and 5. A three-phase fault will produce correct
distances in all six blocks.
A considerable saving in computation can be achieved by utilizing a first
step which attempts to determine the fault type. This principle is illustrated in
Figure 5.18. In general, only one of the six equations would be processed for any
fault, and considerable computational efficiency would be achieved.
An early classification program used a voltage deviation criterion to classify a
fault.18 Thus, for a phase a-g fault, the voltage of phase a should deviate from its
value one cycle ago. Such a comparison is made, and if it is found to persist (while
other phase voltagesremainundisturbed), an a-g fault isdeclared (seeFigure5.19).
Inorder toguardagainst declaringafaultwhenadatasampleiscorruptedbynoise,
anaccumulatednumberofpointsatwhichthevoltagedifferenceexceedsatolerance
may be compared against a threshold. A count is maintained for each phase, and
if counts of two phases reach the threshold simultaneously, a phase-to-phase fault
is declared. One could supplement a voltage classifier with a similarly designed
current classifier.

| 168 |     |     |     | Transmission | line relaying |
| --- | --- | --- | --- | ------------ | ------------- |
sample ‘k’
|     |     | of e , e  | , e |     |     |
| --- | --- | --------- | --- | --- | --- |
|     |     | a b       | c   |     |     |
|     |     | i , i , i |     |     |     |
|     |     | a b       | c   |     |     |
calculate
|     |     | distance for | 1   |     |     |
| --- | --- | ------------ | --- | --- | --- |
phase fault a-b
|     |     | b-c | 2   |     |     |
| --- | --- | --- | --- | --- | --- |
c-a
3
a-g
4
|     |     | b-g | 5   |     |     |
| --- | --- | --- | --- | --- | --- |
c-g
6
check fault
distance against
zones
provide appropriate
outputs
|     | Figure | 5.17 A simple | relay program |     |     |
| --- | ------ | ------------- | ------------- | --- | --- |
sample ‘k’
fault
type
|     |     | 1 2 | 3 4 | 5 6 |     |
| --- | --- | --- | --- | --- | --- |
process
distance equation ‘k’
|     | Figure 5.18 | A fault classification | relay | program |     |
| --- | ----------- | ---------------------- | ----- | ------- | --- |

| Beyond parameter | estimation |     |     |     |     | 169 |
| ---------------- | ---------- | --- | --- | --- | --- | --- |
Figure 5.19 Voltage waveforms for a voltage classification algorithm
Fault classification schemes based upon voltages and/or currents are used in sev-
eral practical relaying programs. They produce correct fault classification under
most reasonable conditions but do mis-classify in a significant number of cases.
The voltage based classifiers tend to be error-prone when short lines are supplied
from a weak system or when a long line is fed from a strong system. In the former
case all voltages deviate significantly from nominal while in the latter case faults
near a zone boundary produce hardly any voltage deviation in the faulted phase
at the relay location. Current based classifiers are similarly confused when load
currents are significant compared to fault current. Whenever the classification is
uncertain, it must be recognized as such, and all six equations must be processed
| at each sample | time. |     |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- | --- |
Another drawback of the programs using fault classification is that no fault pro-
cessing can be begun until the classification phase is complete. If voltage deviation
countersaretobecheckedagainstthresholds,valuabletimeislostwhilethedistance
calculation(and therelaydecision) isheld inabeyance waitingfor theclassification
step to be completed. This makes for slower relay response time.
Clarke19
For the differential-equation algorithms, the components offer another
possibleapproach.10 TheClarkecomponentswithphasea asreferenceareobtained
| by multiplying | the | phase quantities | by  | the matrix |     |        |
| -------------- | --- | ---------------- | --- | ---------- | --- | ------ |
|                |     |                  |    |            |    |        |
|                |     |                  |     | 1 1        | 1   |        |
|                |     |                  | 1  |            |    |        |
|                |     |                  | T = | 2 −1       | −1  | (5.69) |
|                |     |                  | c   | √          | √   |        |
3
|     |     |     |     | 0 3 | − 3 |     |
| --- | --- | --- | --- | --- | --- | --- |
It can be verified by multiplication that TT T is diagonal but is not normalized so
c c
that it is not a unitary matrix. The components are referred to as zero, alpha, and
| beta components.  | For | example, | for    |       |        |     |
| ----------------- | --- | -------- | ------ | ----- | ------ | --- |
| a phase-to-ground |     | fault    | Iα = 2 | I and | Iβ = 0 |     |
0
| b-c to | ground | fault | Iα = −I |     |     |     |
| ------ | ------ | ----- | ------- | --- | --- | --- |
0
| b-c fault |     |     | Iα = 0 | and I | = 0 |     |
| --------- | --- | --- | ------ | ----- | --- | --- |
0
| 3-phase | fault |     | I 0 = 0 |     |     |     |
| ------- | ----- | --- | ------- | --- | --- | --- |

| 170 |     |     |     |     | Transmission | line relaying |
| --- | --- | --- | --- | --- | ------------ | ------------- |
b c
If the Clarke transformation is also performed with and phases as reference
and if the neutral current I is measured, these conditions can be translated into two
n
| types depending | on  | whether | I is | zero or not. |     |     |
| --------------- | --- | ------- | ---- | ------------ | --- | --- |
n
| If I (cid:6)= 0 | (ground | faults) |     |     |     |     |
| --------------- | ------- | ------- | --- | --- | --- | --- |
n
| I −I              | = 0     |       | a−ground   | fault |     |     |
| ----------------- | ------- | ----- | ---------- | ----- | --- | --- |
| b c               |         |       |            |       |     |     |
| −I                | =       |       | b−ground   |       |     |     |
| I a c             | 0       |       |            | fault |     |     |
| I −I              | = 0     |       | c−ground   | fault |     |     |
| b a               |         |       |            |       |     |     |
| 2 I −I            | −I +I   | = 0   | b-c−ground | fault |     |     |
| a                 | b c     | n     |            |       |     |     |
| 2 I −I            | −I +I   | = 0   | a-c−ground | fault |     |     |
| b                 | a c     | n     |            |       |     |     |
| 2 I −I            | −I +I   | = 0   | a-b−ground | fault |     |     |
| c                 | a b     | n     |            |       |     |     |
| If I n = 0 (phase | faults) |       |            |       |     |     |
| 2 I −I            | −I =    | 0 b-c | fault      |       |     |     |
| a                 | b c     |       |            |       |     |     |
| 2 I −I            | −I =    | 0 a-c | fault      |       |     |     |
| b                 | a c     |       |            |       |     |     |
| 2 I −I            | −I =    | 0 a-b | fault      |       |     |     |
| c                 | a b     |       |            |       |     |     |
If none of the equalities is satisfied for a phase fault, it is assumed that the fault is a
three-phase fault. The nine quantities are actually checked against a small threshold
rather than zero. It can be seen that the fault must be correctly classified in order
to use the correct current and voltage in the algorithm for computing R and L. An
obvious problem is mis-classification or an evolving fault. If some samples have
been processed under the assumption that the fault is a – ground, for example, and
it is recognized that the fault is, in fact, a-b – ground then the counter must be
reset and the processing started over. The net effect is a delay in clearing the fault.
| 5.5 Symmetrical |     | component |     | distance relay |     |     |
| --------------- | --- | --------- | --- | -------------- | --- | --- |
The use of phasor calculations permits the use of symmetrical components in the
detection of fault type. The Symmetrical Component Distance Relay20 overcomes
the uncertainty of the fault classifiers and their attendant delay of response in a neat
manner; the symmetrical component transformation20 applies to phasor quantities
| and with phase | a as | reference | takes | the form |     |     |
| -------------- | ---- | --------- | ----- | -------- | --- | --- |
|                |      |           |       |        |     |     |
1 1 1
|     |     |     |     | 1      |     |        |
| --- | --- | --- | --- | -------- | --- | ------ |
|     |     |     | T   | = 1 α α2 |     | (5.70) |
s
|     |     |     |     | 3 α2 α |     |     |
| --- | --- | --- | --- | ------ | --- | --- |
1
ej2π/3.
| where α is |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- |
The resulting component quantities are referred to as zero, positive, and negative
quantities, denoted by subscripts 0, 1, and 2 respectively. If we consider a fault
at a fraction k of the line length away from the relay with pre-fault load currents

| Symmetrical | component | distance | relay |     |     |     | 171 |
| ----------- | --------- | -------- | ----- | --- | --- | --- | --- |
k
fault
|     | Figure | 5.20 | A fault | at a fraction |     | k of the line length |     |
| --- | ------ | ---- | ------- | ------------- | --- | -------------------- | --- |
of I 0,I , and I as shown in Figure 5.20, then we can define the changes in the
| 1         | 2        |     |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- | --- |
| component | currents | as  |     |     |     |     |     |
(cid:1)I
|     |     |     |     | = I          | −I  |     |        |
| --- | --- | --- | --- | ------------ | --- | --- | ------ |
|     |     |     |     | 0            | 0 0 |     |        |
|     |     |     |     | (cid:1)I = I | −I  |     | (5.71) |
|     |     |     |     | 1            | 1 1 |     |        |
(cid:1)I
|     |     |     |     | = I | −I  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | 2   | 2 2 |     |     |
In fact, only I will be significant in practice. The voltage drops in the line can be
1
defined as
|     |     |     |     | (cid:1)E = (cid:1)I |       |     |        |
| --- | --- | --- | --- | ------------------- | ----- | --- | ------ |
|     |     |     |     | 0                   | 0 Z 0 |     |        |
|     |     |     |     | (cid:1)E = (cid:1)I | Z     |     | (5.72) |
|     |     |     |     | 1                   | 1 1   |     |        |
|     |     |     |     | (cid:1)E = (cid:1)I | Z     |     |        |
|     |     |     |     | 2                   | 2 2   |     |        |
where Z 0 , Z 1 , and Z 2 are the sequence impedances of the entire line. The ratios
E
|     |     |     |     | k =        | 0   |     |     |
| --- | --- | --- | --- | ---------- | --- | --- | --- |
|     |     |     |     | 0 (cid:1)E |     |     |     |
0
E
|     |     |     |     | k =        | 1   |     |     |
| --- | --- | --- | --- | ---------- | --- | --- | --- |
|     |     |     |     | 1 (cid:1)E |     |     |     |
1
(5.73)
E
|     |     |     |     | k =        | 2   |     |     |
| --- | --- | --- | --- | ---------- | --- | --- | --- |
|     |     |     |     | 2 (cid:1)E |     |     |     |
2
Z I
1 1
k l =
(cid:1)E
1
playanimportantroleindeterminingfaultlocationforallfaulttypes.Forexample,a
three-phasefaultwithfaultresistance,R ,wouldinvolveonlythepositivesequence
1f
| network | as shown in | Figure | 5.21.      | The voltage   | equation | is:   |     |
| ------- | ----------- | ------ | ---------- | ------------- | -------- | ----- | --- |
|         |             | 0      | = (cid:1)E | [k −k(1+k)]−R |          | I     |     |
|         |             |        | 1          | 1             | l        | 1f 1f |     |

| 172 |     |     |     |     |     |     | Transmission | line | relaying |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | -------- |
|     |     |     | E   |     | kZ  |     |              |      |          |
|     |     |     |     | 1   |     | 1   |              |      |          |
I
|     |     |     |     |     | 1   |     | R   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1f
|     | Figure | 5.21 | Positive | sequence |     | network | for a three-phase | fault |     |
| --- | ------ | ---- | -------- | -------- | --- | ------- | ----------------- | ----- | --- |
or
|     |     |     |     |     | k   | 1   |     |     |        |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
|     |     |     |     | k   | =   | +ε  |     |     | (5.74) |
r
1+k
l
where
|     |     |     |     |     | −R       | 1f I 1f |     |     |     |
| --- | --- | --- | --- | --- | -------- | ------- | --- | --- | --- |
|     |     |     |     | ε   | =        |         |     |     |     |
|     |     |     |     | r   | (cid:1)E | (1+k)   |     |     |     |
|     |     |     |     |     |          | 1 l     |     |     |     |
By considering all possible fault types a general expression for the fractional dis-
| tance to | the fault | can | be obtained |     | in the     | form      |          |     |        |
| -------- | --------- | --- | ----------- | --- | ---------- | --------- | -------- | --- | ------ |
|          |           |     |             |     |            | k(cid:1)  | k(cid:1) |     |        |
|          |           |     |             |     | k +k       | +k        |          |     |        |
|          |           |     |             | k = | 1          | 2 2 0     | 0        |     | (5.75) |
|          |           |     |             |     | 1+k(cid:1) | +k(cid:1) |          |     |        |
+k
|          |          |     |     |     |     | 0 2 | l   |     |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| k(cid:1) | k(cid:1) |     |     |     |     |     |     |     |     |
where and play something of the role of the nine conditions developed in the
|                  | 0   | 2       |      |     |     |                   |     |     |     |
| ---------------- | --- | ------- | ---- | --- | --- | ----------------- | --- | --- | --- |
| Clarke component |     | case.20 | They | are |     |                   |     |     |     |
|                  |     |         |      |     |     | (cid:11) (cid:11) |     |     |     |
|                  |     |         |      |     |     | (cid:11) (cid:11) |     |     |     |
(cid:1)E
|     |     |     |     |     | k(cid:1) = | (cid:11) 0 (cid:11) |     |     |     |
| --- | --- | --- | --- | --- | ---------- | ------------------- | --- | --- | --- |
|     |     |     |     |     |            | (cid:11) (cid:11)   |     |     |     |
|     |     |     |     |     | 0          | (cid:1)E            |     |     |     |
1
(cid:14)
and
|     |     |     |          |     |     | |(cid:1)E | ∼ | |(cid:1)E | |     |     |
| --- | --- | --- | -------- | --- | --- | ------------- | ----------- | --- | --- |
|     |     |     | k(cid:1) | 1   | if  | 2 =           | 1           |     |     |
=
|     |     |     | 2   | 0   | otherwise |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
Aflowchartforthek calculationisshowninFigure5.22.Theobviousadvantage
of the k calculation is that it is not necessary to determine the fault type before
| meaningful | calculations |     | can | be performed. |     |     |     |     |     |
| ---------- | ------------ | --- | --- | ------------- | --- | --- | --- | --- | --- |
5.5.1 SCDFT
Thecomputationalburdenassociatedwiththecomputationofthesymmetricalcom-
ponents can be greatly reduced by the choice of sampling frequency. If sampling
frequencies that correspond to θ = 30◦,60◦, or 120◦ are used then the discrete
Fourier transform calculation and the symmetrical component calculation can be

| Symmetrical | component |     | distance relay |     |     |     | 173 |
| ----------- | --------- | --- | -------------- | --- | --- | --- | --- |
|             |           |     | k calculation  |     |     |     |     |
1
yes
|     |     |     | ∆E <e |     | k =   0 |     |     |
| --- | --- | --- | ------- | --- | ------- | --- | --- |
|     |     |     | 2 1     |     | 2 ′=    |     |     |
k 2   0
no
′= 1
k
2
no
yes
|     |     |     | ∆E <e |     | k 0 =   0 |     |     |
| --- | --- | --- | ------- | --- | --------- | --- | --- |
|     |     |     | 0 2     |     | ′=        |     |     |
k 0   0
no
′
k 0 , k 0
calculation
no
yes
k ′<e3
0
no
|     |     |     | k ′= 0 |     | k calculation |     |     |
| --- | --- | --- | ------ | --- | ------------- | --- | --- |
|     |     |     | 2      |     | 2             |     |     |
k calculation
|     |     | Figure | 5.22 The | flow | chart for the | k algorithm |     |
| --- | --- | ------ | -------- | ---- | ------------- | ----------- | --- |
effectively combined. Using θ = 30◦, the factor α in Equation (5.70) is seen to be
|            |     | 4×θ     | α2         |     | 8×θ −4×θ.      |           |     |
| ---------- | --- | ------- | ---------- | --- | -------------- | --------- | --- |
| a rotation | by  | and     | a rotation | by  | or             | If we let |     |
|            |     | (cid:1) | (y         | )   |                |           |     |
|            |     | y       | = −y       | for | the full-cycle | algorithm |     |
|            |     | L       | new        | old |                |           |     |
and
|     |     | (cid:1) y | = (y +y | ) for | the half-cycle | algorithm |     |
| --- | --- | --------- | ------- | ----- | -------------- | --------- | --- |
|     |     | L         | new     | old   |                |           |     |
given in Equations (5.35) – (5.38), we can produce the full- or half-cycle versions
of the SCDFT (Symmetrical Component Discrete Fourier transform) with a single
expression.7
|     | ( L +1) | YL +((cid:1)y   | +(cid:1)y | +(cid:1)y | )cos(Lθ) |     |     |
| --- | ------- | --------------- | --------- | --------- | -------- | --- | --- |
|     | Y       | =               | a,L       | b,L       | c,L      |     |     |
|     | O C     | OC              |           |           |          |     |     |
|     | ( L +1) | = YL +((cid:1)y | +(cid:1)y | +(cid:1)y | )sin(Lθ) |     |     |
|     | Y       |                 | a,L       | b,L       | c,L      |     |     |
|     | O S     | OC              |           |           |          |     |     |

| 174 |     |     |     | Transmission | line relaying |
| --- | --- | --- | --- | ------------ | ------------- |
| (   | +1) |     |     |              |               |
Y L = YL +(cid:1)y cos(Lθ)+(cid:1)y cos(L+4)θ+(cid:1)y cos(L−4)θ
| 1   | C 1C | a,L | b,L | c,L |     |
| --- | ---- | --- | --- | --- | --- |
( L +1) +(cid:1)y sin(Lθ)+(cid:1)y sin(L+4)θ+(cid:1)y cos(L−4)θ
| Y   | = YL | a,L | b,L | c,L |     |
| --- | ---- | --- | --- | --- | --- |
| 1   | S 1S |     |     |     |     |
( L +1) YL +(cid:1)y cos(Lθ)+(cid:1)y cos(L−4)θ+(cid:1)y sin(L+4)θ
| Y   | =    | a,L | b,L | c,L |     |
| --- | ---- | --- | --- | --- | --- |
| 2   | C 2C |     |     |     |     |
Y ( L +1) = YL +(cid:1)y sin(Lθ)+(cid:1)y sin(L−4)θ+(cid:1)y cos(L+4)θ
|     |      | a,L | b,L | c,L |     |
| --- | ---- | --- | --- | --- | --- |
| 2   | S 2S |     |     |     |     |
(5.76)
The recursive expressions in Equation (5.76) are off by an additional factor of 1/3
because of the 1/3 in Equation (5.70). This means the half-cycle SCDFT is off
by 1/9 and the full-cycle SCDFT is off by 1/18. For impedance calculations the
constantmultiplierswillcancelinthedivision.Itisonlynecessarytoconsider them
if there is a problem with overflow in the calculations or if metering quantities such
| as power | or voltage | are required. |     |     |     |
| -------- | ---------- | ------------- | --- | --- | --- |
| 5.5.2    | Transient  | monitor       |     |     |     |
When the data window spans the instant of fault inception, as seen in Figure 5.1,
the results obtained from almost any algorithm are unreliable. The difficulty is
that the data contain both pre-fault samples and post-fault samples so that the
fit of the estimate to the data is particularly bad. If the quality of the estimate
could be determined, then the relay could be disabled during this transition. Using
the least squares solution given by Equation (5.23), we can compute the sample
values that would correspond to the estimate. If we denote these as the vector y˜
then
Yˆ S(STS)−1STy
|     |     | y˜ = S | =   |     | (5.77) |
| --- | --- | ------ | --- | --- | ------ |
The vector y˜ represents the reconstruction of the samples from the estimate yˆ, as
shown in Figure 5.23. If y˜ is close to y then the estimate is trustworthy. If not,
{y }
k
~
{y }
k
|     | Figure 5.23 | The actual samples | and the reconstructed | samples |     |
| --- | ----------- | ------------------ | --------------------- | ------- | --- |

| Symmetrical | component | distance | relay |     |     |     |     |     | 175 |
| ----------- | --------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
then it is fair to assume that something such as the pre-fault/post-fault transition is
| involved. | The difference |     | can be formed |                   | as  |     |     |     |        |
| --------- | -------------- | --- | ------------- | ----------------- | --- | --- | --- | --- | ------ |
|           |                |     | r=y˜ −y       | = [S(STS)−1ST−I]y |     |     |     |     | (5.78) |
|           |                |     | r=My          |                   |     |     |     |     | (5.79) |
The residual r can be thought of in much the same way as the observation residual
in the Kalman filter. For the Fourier algorithms the matrix in Equation (5.78) can
| be simplified. | With | six Samples | per   | half-cycle, | for      | example |     |       |     |
| -------------- | ---- | ----------- | ----- | ----------- | -------- | ------- | --- | ----- | --- |
|                |      |            | √     |             |          |         |     | √    |     |
|                |      | 2           | − 3/2 | −1/2        | 0        | 1/2     |     | 3/2   |     |
|                |      |  √         |       | √           |          |         |     |      |     |
|                |      | − 3/2      | 2     | −           | 3/2 −1/2 |         | 0   | 1/2  |     |
|                |      |            |       |             |          |         |     |      |     |
|                |      |             | √     |             | √        |         |     |       |     |
|                |      |  −1/2      | 3/2   |             | 3/2      | −1/2    |     |      |     |
|                | 1    |            | −     |             | 2 −      |         |     | 0    |     |
|                | =    |            |       | √           |          | √       |     |      |     |
|                | M    |            |       |             |          |         |     |      |     |
|                | 3    | 0           | −1/2  | −           | 3/2 2    | −       | 3/2 | −1/2  |     |
|                |      |            |       |             |          |         |     |      |     |
|                |      |            |       |             | √        |         |     | √    |     |
|                |      | 1/2         |       | −1/2        | 3/2      |         |     | 3/2  |     |
|                |      |            | 0     |             | −        |         | 2−  |       |     |
|                |      | √           |       |             |          | √       |     |       |     |
|                |      | 3/2         | 1/2   |             | 0 −1/2   | −       | 3/2 | 2     |     |
It can be shown (Problem 5.5) that the residuals r obey a recursive relationship
k
transient monitor
similar to Equations (5.37) and (5.38). If we define a function as
| the sum | of the absolute |     | values of | the r , | i.e. |     |     |     |     |
| ------- | --------------- | --- | --------- | ------- | ---- | --- | --- | --- | --- |
k
(cid:5)6
|     |     |     |     | t = | |r | |     |     |     | (5.80) |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------ |
k
k=1
thentcanbecomputedwithmuchthesameprocedureasthefundamentalfrequency
components or the symmetrical components. The t function is computed for each
phase current. Figure 5.24 shows the transient monitor for the a phase current
|     |     |     | t pu |     |     | i   | pu  |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |     |     | a    |     |     | a   |     |     |     |
i
|     |     | 15  | t   |     | a   |     | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a
|     |     | 10  |     |     |     |     | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 5   |     |     |     |     | 1   |     |     |
|     |     |     |     | 5   | 10  |     |     |     |     |
Figure 5.24 The transient monitor function for a phase a to ground fault

| 176 |     |     |     |     |     | Transmission | line | relaying |
| --- | --- | --- | --- | --- | --- | ------------ | ---- | -------- |
during a phase a to ground fault. It can be seen that the transient monitor behaves
as desired. The value of t is large while the data window contains both pre-fault
a
and post-fault data and drops when the window contains only post-fault data. If the
transient monitor is large for any phase, the trip signal is inhibited. The transient
monitor may pick up, i.e. exceed some threshold value, for transient events which
are not faults. This is not troublesome since the transient monitor is only a control
parameter which testifies to the purity of the data. However, the threshold value
must be set high enough so that the random signals encountered in the post-fault
| currents | do not inhibit | tripping.      |     |     |     |     |     |     |
| -------- | -------------- | -------------- | --- | --- | --- | --- | --- | --- |
| 5.5.3    | Speed reach    | considerations |     |     |     |     |     |     |
If we examine the performance of the impedance like algorithms by taking the
covariance of the estimate as a measure then Equation (5.22) implies a relationship
between the length of the data window and the estimation error. For a measure-
= σ2
ment error covariance matrix which is a multiple of a unit matrix, W I, the
e
| covariance | of the estimation |     | error is       |     |           |                |     |        |
| ---------- | ----------------- | --- | -------------- | --- | --------- | -------------- | --- | ------ |
|            |                   |     |               |     |           |                |    |        |
|            |                   |     | (cid:10)K      |     | (cid:10)K |                | −1  |        |
|            |                   |     | cos2(kθ)       |     |           | cos(kθ)sin(kθ) |     |        |
|            |                   |     |               |     |           |                |    |        |
|            |                   |     |               |     |           |                |    |        |
| E{(Yˆ      | −Y)(Yˆ −Y)T}      | σ2 | k=1            |     | k=1       |                |     |        |
|            |                   | =   |                |     |           |                |    | (5.81) |
|            |                   | ε   |  (cid:10)K    |     | (cid:10)K |                |    |        |
|            |                   |     | cos(kθ)sin(kθ) |     |           | sin2(kθ)       |     |        |
|            |                   |     | k=1            |     | k=1       |                |     |        |
As in Figure 5.8, two quantities are being estimated, Y and Y . The diagonal
|     |     |     |     |     |     | c   | s   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
entries in the inverse matrix in Equation (5.81) give the variances of each of the
estimation errors while the off-diagonal entries give a cross covariance between
the two. At multiples of a half-cycle the two estimation errors are independent.
| The various | sums are |     |     |     |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- | --- | --- | --- |
(cid:5)K
|     |          |     | (K−1) | cos2Kθ | 1   | cosθ   |     |     |
| --- | -------- | --- | ----- | ------ | --- | ------ | --- | --- |
|     | cos2(kθ) |     |       |        |     | sin2Kθ |     |     |
|     |          |     | =     | +      | +   |        |     |     |
|     |          |     | 2     | 2      | 2   | sinθ   |     |     |
k=1
(cid:5)K
|     |        |     | (K+1) | cos2Kθ | 1      | cosθ |     |        |
| --- | ------ | --- | ----- | ------ | ------ | ---- | --- | ------ |
|     | sin2kθ |     |       |        | sin2Kθ |      |     |        |
|     |        | =   |       | −      | +      |      |     | (5.82) |
|     |        |     | 2     | 2      | 2      | sinθ |     |        |
k=1
|     | (cid:5)K |     |     |     | sin2Kθ | cosθ |     |     |
| --- | -------- | --- | --- | --- | ------ | ---- | --- | --- |
1
|     | cos(kθ)sin(kθ) |     | =   | sin2Kθ+ |     |     |     |     |
| --- | -------------- | --- | --- | ------- | --- | --- | --- | --- |
sinθ
|     |     |     |     | 4   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
k=1
For Kθ a multiple of π the estimation errors are independent and have equal vari-
2σ2/K.
ances of The determinant of the matrix in Equation (5.81) is complicated in
e

| Symmetrical | component | distance | relay |     |     |     |     | 177 |
| ----------- | --------- | -------- | ----- | --- | --- | --- | --- | --- |
general but can be evaluated from the sums in Equation (5.82). If we add the two
variances to obtain a variance for the phasor Yˆ +jYˆ we obtain
|     |     |     |     |     | c   |     | s   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
4σ2
|     |     |     |     | σ2  | = e |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(5.83)
Yˆ K
Before we can reach any firm conclusion about the behavior of the estimation
σ2.
error we must examine the term To clarify the notation let us consider that y
e
represents samples of voltage. If, motivated by Section 5.1, we imagine that the
non-fundamental frequency signals that are being sampled to produce the error
ε
in Equation (5.18) are a wide-sense stationary random process (Section 3.7).
|     |     | ω   | = andω |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- |
Example 3.20, with 1 0 2 very large) with a power density spectrum
| which is | flat at a | level S | , i.e. |     |     |     |     |     |
| -------- | --------- | ------- | ------ | --- | --- | --- | --- | --- |
v
|     |     |     | S(ω) | =   | S for all | ω   |     |     |
| --- | --- | --- | ---- | --- | --------- | --- | --- | --- |
v
then we will have to filter the noise with the anti-aliasing filter before sampling. If
| we assume | an ideal | filter | with a | cut-off | frequency | of  |     |     |
| --------- | -------- | ------ | ------ | ------- | --------- | --- | --- | --- |
πω
|     |     |     |     | ω   | = o |     |     |        |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ |
|     |     |     |     | c   |     |     |     | (5.84) |
8
one-half the sampling frequency where θ = ω (cid:1)t then the noise before sampling
0
has a spectrum
|     |     |     | S (ω) | = S | ;|ω| < | πω /θ |     |     |
| --- | --- | --- | ----- | --- | ------ | ----- | --- | --- |
|     |     |     | s     |     | v      | o     |     |     |
(5.85)
|     |     |     | (ω) | 0;|ω|>πω |     | /θ  |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- |
|     |     |     | S   | =        |     |     |     |     |
|     |     |     | s   |          |     | o   |     |     |
where the sub s denotes sampling. From the definition of the correlation func-
tion (Equation (3.78) and the relationship between the correlation function and the
| spectrum | (Equation | (3.81)) | we obtain |     |     |     |     |     |
| -------- | --------- | ------- | --------- | --- | --- | --- | --- | --- |
π(cid:4)ω /θ
o
|     |     |     |       | 1   |     |     | S ω |        |
| --- | --- | --- | ----- | --- | --- | --- | --- | ------ |
|     |     | σ2  | (0)   |     |     | dω  | v o |        |
|     |     |     | = R v | =   | S   | v = |     | (5.86) |
|     |     | e   |       | 2π  |     |     | θ   |        |
−πω /θ
o
or
ω
|     |     |     |     | 4   | S     | 4 S |     |        |
| --- | --- | --- | --- | --- | ----- | --- | --- | ------ |
|     |     |     | σ2  | =   | v o = | v   |     | (5.87) |
|     |     |     |     | Vˆ  | Kθ    | T   |     |        |
where T is the length of the window in seconds. If the impedance to the fault is
computed as a ratio of estimated voltage to estimate current and we assume that

178 Transmission line relaying
1.0 1.0
one cycle
DATA WINDOW
tinu
rep
σ z
hcaer
tinu
rep
reach
σ
z
Figure5.25 Thevarianceoftheimpedanceestimateandthereachversusthedatawindow
the errors are small then the variance of the impedance error is given by
4(S +S )
σ2 = σ2 +σ2 = v I (5.88)
Zˆ Vˆ ˆI T
Equation (5.88) is valid for T a multiple of a half-cycle of the fundamental fre-
quency.Thecurveofthestandarddeviation(σ )oftheimpedanceestimateobtained
z
from Equation (5.81) is shown in Figure 5.25.
Several interesting observations can be made from Equation (5.88). The first
concerns the sampling rate used in relaying algorithms. The sampling rate does not
appearinEquation(5.88).Thevarianceoftheimpedanceestimateisindependentof
the sampling rate and is inverse to the length of the data window. The explanation
lies with the anti-aliasing filter. At higher sampling frequencies the anti-aliasing
filter has a larger bandwidth and each sample has a larger variance Equation (5.86).
On the other hand, there are more samples in the same time period T and K is
correspondingly larger (see Equation (5.83)). This effect will hold until the sam-
pling frequency is so large that the assumption that the noise before filtering is
white (S(ω) = S for all ω) is invalid. Since the noise is ultimately band-limited,
v
for example, by the transducers, t here are sampling frequencies that are high
enough to exceed the noise bandwidth. Laboratory and simulation results indicate
that sampling frequencies in the kHz range would be required before this effect
would be pronounced.5
There is an additional effect caused by the use of a non-ideal anti-aliasing filter.
The actual anti-aliasing filter (Chapter 1) has a phase shift which translates into
a delay. This delay, for well designed filters, is roughly one sample time. Lower
sampling frequencies mean longer delays introduced by the anti-aliasing filter.
This analysis has been for the Fourier algorithms but is appropriate for all of the
algorithms described inthischapter. A longer window will produce better estimates
forallofthealgorithmtypes.Thecounter schemeusedforthedifferential-Equation
algorithms is an attempt to create a longer window. Higher sampling rates (with the

Symmetrical component distance relay 179
appropriate anti-aliasing filter) produce more noise per sample. In general, indepen-
dent of sampling rate, the variance of the estimated fault location is inverse to the
length of the data window.
The second curve in Figure 5.25 is also an important general result. If we accept
thattheestimatedfaultlocationisarandomvariablewhichhasthecorrectmeanbut
has a probability density with the variance given by Equation (5.88) then we must
accept that there is a probability of false trip or failure to trip. The two situations
are shown in Figure 5.26. In each case the density is drawn with its mean at the
true fault location and the shaded area of the density corresponds to incorrect relay
operation. If the density has tails, as shown in Figure 5.26, then there is no setting
for the relay that can eliminate the failure to trip shown in Figure 5.26(a).
However, if we assume that almost all reasonable densities are concentrated
within ±2.5σ then we can conclude that the maximum relay setting that can safely
be used is 1−2.5σ. This would correspond to better than 99% confidence if the
distribution were Gaussian and would guarantee no failures to trip if the density
were triangular or uniform. The inverse time dependence of the variance of the
estimates translates into the reach curve shown in Figure 5.25.
The implications of the speed-reach relationship are plain and are inherent in
electromechanical relays. Close-in faults may be cleared quickly but faults near the
zone-1 boundary require more processing. While the principle is physically appeal-
ing and is recognized in relaying practice,21 it has an impact on digital schemes
which use a fixed data window for ease of computation. For example, a fixed
one half-cycle algorithm cannot clear a close-in fault as quickly as might be justi-
fied and cannot be set as near the zone-1 boundary as a longer window algorithm.
(a)
actual fault
location
(b) l = 1 actual fault
location
Figure 5.26 Distributions of estimated fault location. (a) Fault within zone-1. (b) Fault
beyond zone-1

| 180 |     |     |     | Transmission | line relaying |
| --- | --- | --- | --- | ------------ | ------------- |
Evidently,whatisneededisanadaptiveschemewhichadjuststhewindowlengthto
the estimated fault location. An accumulator for this purpose has been suggested.22
| 5.5.4 | A relaying | program |     |     |     |
| ----- | ---------- | ------- | --- | --- | --- |
As an example of the additional features that must be included in a complete
line relaying program we will conclude with a description of the Symmetrical
Component Distance Relaying Program (SCDR).7 The flow chart for the program
is shown in Figure 5.27. The program includes the following features:
| 1. Phase       | and Ground | Distance Protection |                 |     |     |
| -------------- | ---------- | ------------------- | --------------- | --- | --- |
| 2. Directional | Comparison | Carrier             | Blocking Scheme |     |     |
3. Three-zone Stepped Dist ace for both Carrier and Time-Delay Backup
| 4. Local             | Breaker Failure | Protection       |           |     |     |
| -------------------- | --------------- | ---------------- | --------- | --- | --- |
| 5. High              | Speed Reclosing | Initiation       |           |     |     |
| 6. Automatic         | Reclosing       | with Synchronism | Check     |     |     |
| 7. Sequence          | of Events       | Recording        |           |     |     |
| 8. Fault             | Classification  |                  |           |     |     |
| 9. Single-Phase-Trip |                 | Output           |           |     |     |
| 10. Memory           | Voltage         | for Three-Phase  | Bus Fault |     |     |
11. Directional Inverse Time Backup for Ground Faults using Ground Current.
The SCDFT, K algorithm, and transient monitor algorithm have been described
earlier in this section. The circuit-breaker failure flag (CBF) is set high following
| a trip command | to the | line breakers. |     |     |     |
| -------------- | ------ | -------------- | --- | --- | --- |
The CBF routine initiates a timer and upon expiration of the time interval checks
the line currents. If the currents are not zero, a CBF trip signal is sent to the
appropriate breakers. The value of k computed by the K routine is checked to see
if it lies in various zones of the relay. A value of k lying in zone-1 or in zone-3
with no carrier received, leads to High Speed Reclose (HSR) output and breaker
tripoutput fromeach isprovided when thetimeexceeds the appropriate timedelay.
The CARRIER START routine is entered and the local carrier transmitter is started
| if k is in | the carrier start | zone. |     |     |     |
| ---------- | ----------------- | ----- | --- | --- | --- |
The Auto Reclose Flag is set high following the BREAKER TRIP routine. The
AR routine which is entered when this flag is high maintains timers and upon
their expiration checks the phase angle between the bus voltage of phase a and
the positive sequence line voltage. If these two voltage are within a preset limit,
Auto-Reclose is initiated. The Single-Phase Tripfeature of the Triproutine uses the
phase angle between the positive and negative sequence currents computed by the
SCDFT. The entire program is repeated at each sample time (12 times a cycle of
| the nominal | fundamental | frequency). |     |     |     |
| ----------- | ----------- | ----------- | --- | --- | --- |
Several additional features of the k calculations are addressed in the problems.
The correct k is obtained even if one of the voltages is missing due to a blown
fuse in a CVT (Problem 5.8). The k maintains its directionality for unbalance

| Symmetrical | component | distance | relay |     |     |     | 181 |
| ----------- | --------- | -------- | ----- | --- | --- | --- | --- |
SCDFT and
|     |     |     |                    |     | I yes |      |     |
| --- | --- | --- | ------------------ | --- | ----- | ---- | --- |
|     |     |     | transient monitor  |     |       | wait |     |
high
program
no
|     |     |        |         | yes | no  |         |     |
| --- | --- | ------ | ------- | --- | --- | ------- | --- |
|     |     | CBF    | CBF     |     | CBF | k       |     |
|     |     | output | routine |     |     | routine |     |
set
|     |     | set | trip    | HSR    | yes | k    |     |
| --- | --- | --- | ------- | ------ | --- | ---- | --- |
|     | CBF |     | routine | output |     | in Z |     |
1
|     |     |     | single |     |     | no  |     |
| --- | --- | --- | ------ | --- | --- | --- | --- |
pole
Set
trip
|     | AR   |     |     |     | yes  |     |     |
| --- | ---- | --- | --- | --- | ---- | --- | --- |
|     | flag |     |     |     | recv | k   |     |
in Z
|     |     |     |     |     | carr. | 3   |     |
| --- | --- | --- | --- | --- | ----- | --- | --- |
yes
Z
3
routine
|     |     |     |     | carrier |     | k   |     |
| --- | --- | --- | --- | ------- | --- | --- | --- |
yes
|     |     |     |     | start   | in start |     |     |
| --- | --- | --- | --- | ------- | -------- | --- | --- |
|     |     |     |     | routine |          | Z   |     |
no
|     |     |     |     | zone 2  | yes  | k   |     |
| --- | --- | --- | --- | ------- | ---- | --- | --- |
|     |     |     |     | routine | in Z |     |     |
2
no
yes
|     |     |     |     | AR      | AR flag |     |     |
| --- | --- | --- | --- | ------- | ------- | --- | --- |
|     |     |     |     | routine |         | set |     |
no
wait
Figure 5.27 The flow chart for the symmetrical component distance relay
faults even if the fault is a so-called bolted fault producing zero bus voltage
| (Problem | 5.9). |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- |
Except for the fact that this program uses the symmetrical component
Equation (5.75) for distance calculations, this could be a relaying program using
any other method for computing the distance to the fault. The complexity of the
program beyond the distance calculation should be borne in mind, as often the

182 Transmission line relaying
impact of an improvement in the distance calculation technique is completely
masked by the larger relaying programs in which the algorithm must be imbedded.
5.6 Newer analytic techniques
Some of the techniques presented in Chapter 4 have been proposed in areas beyond
line protection, such as windowing for PMUs when the system frequency is off
nominal. Wavelets have been suggested for high impedance fault detection, trans-
formerprotection,faultclassification,faultlocation,adaptivereclosing,androtating
machinery protection. As mentioned in the preface, the case for the application of
artificial intelligence to conventional first zone protection has not really been made.
5.6.1 Wavelet applications
An early wavelet application that took advantage of the wavelet’s superior time
frequency resolution was in dealing with the complicated waveforms that are gen-
erated by resonant grounding.23 It is common in Europe to insert a Petersen coil in
the connection of the neutral to ground. When properly tuned this eliminates arcing
grounds. For a single phase fault the signal measured by a zero sequence device
contains significant transient components and only small amounts of the fundamen-
tal frequency contribution, however. The signals are non-stationary short-duration
transients and are difficult to deal with in a Fourier environment. With a carefully
chosen Mother Wavelet it is possible to use the wavelet transform magnitude and
phase to set thresholds to distinguish faults from non faults.
Wavelets have been suggested in the environment of the traveling wave relays of
Chapter 9.24 The issue is determining fault location from observations of the time
of arrival of traveling waves caused by a fault on a transmission line. In Chapter 9,
a discriminant function is presented to solve this problem. Correlation techniques
havealsobeensuggestedforthispurpose. Becausethewavelettransformiscapable
of localizing in both time and frequency it is an attractive option especially with
synchronized sampling at both ends of the line.
Both neural nets and decision trees have been proposed to learn the difference
between a fault and inrush in transformer protection.25 The conventional harmonic
approachtothisproblemispresentedinChapter6.Eventhecombinationofwavelet
analysis and decision trees has been proposed.26 The wavelet coefficients are the
variables in the decision tree construction.
5.6.2 Agent applications
Agents have been proposed for the protection of tapped transmission lines and for a
variety of backup protection
applications.27,28
The issues of communication traffic
patterns and the connection with IEC 61850 and message structure and strategies
for such systems have been studied in simulation.29

Protection of series compensated lines 183
5.7 Protection of series compensated lines
One of the earliest field installations of computer relays dealt with the problem of
protecting a series compensated transmission line.30 In order to improve the power
transfercapabilityof alongdistancetransmissionline,itisoftennecessary toinsert
a three-phase capacitor bank in series with the transmission line. Usually the series
capacitors are inserted at one end of the line, but occasionally they may be installed
in the middle, or even in more than one location. A compensating capacitor having
a reactance equal to the positive sequence reactance of the transmission line is
said to provide 100% compensation, while a capacitor with a smaller reactace, i.e.
with a larger value of capacitance) provides a proportionally smaller compensation.
In most cases, the compensation is smaller than 100%. Consider the compensated
transmission line shown in Figure 5.28(a). As long as the capacitors are in service,
theimpedance seen bydistance relaysatterminal Avariesalong thesegmented line
ABCD as shown in Figure 5.28(b). It is clear that an impedance measured by the
relay at A may not have a one-to-one correspondence with the distance to the fault,
particularly if the distance is primarily determined by the fault reactance X . In
f
some cases it may be that the resistance of the measured impedance is sufficiently
well defined to make the distance calculation based upon the complex impedance
a practical proposition.
The actual fault conditions are likely to be more complex, as the protective gaps
or lightning arresters across the capacitors may flash over for some transmission
line faults. Should this happen, the distance measurement would change suddenly
when the capacitor protection system operates. This is likely to be a single-phase
A B C D
R
(a)
X
B
D
X
f
A R
C
(b)
Figure 5.28 R-X diagram for a series compensated line. (a) One-line diagram.
(b) R-X diagram

| 184 |     |     |     |     |     |     | Transmission | line relaying |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- |
phenomenon, and consequently the fault calculation is further complicated by the
presenceof asimultaneousunbalance: theoriginalfault,andtheshort-circuitacross
one phase of the compensating capacitor. The distance calculated from the terminal
voltage and current is now a very complex function of the distance to the fault, the
amount of series compensation, and the placement of the series compensation. It
should be clear from this discussion that the determination of fault location from
a ratio of fundamental frequency voltage and current at the terminals of a series
| compensated | transmission |     | line | is not | a simple | matter. |     |     |
| ----------- | ------------ | --- | ---- | ------ | -------- | ------- | --- | --- |
Even the calculation of voltage and current phasors is fraught with difficulty in
thiscase.Asmentionedearlier,theusualcaseoflessthan100%seriescompensation
requires that capacitors greater than those required for 100% compensation be con-
nected in series with the transmission line. These capacitors form resonant circuits
with the reactance of the transmission line and of the source system. Consequently
the resonance frequencies of these circuits are smaller than the fundamental power
frequency. These extraneous frequencies – which are seldom sub-multiples of the
power frequency – cause considerable error in small window phasor calculations.
It is necessary to devise algorithms which reject these low frequencies, as well as
those above the fundamental frequency. The reference cited earlier used first and
second derivatives of the current and voltage signals to reject the low frequency
components. Consider an input y(t) having two frequency components:
|     |     |     | y(t) = | a sin | ω t+a | sin | (ω t+ϕ) | (5.89) |
| --- | --- | --- | ------ | ----- | ----- | --- | ------- | ------ |
|     |     |     |        | 1     | 1     | 0   | 0       |        |
where ω is the power frequency, and ω is a frequency considerably smaller than
|                 | 0   |           |            |     | 1            |     |     |     |
| --------------- | --- | --------- | ---------- | --- | ------------ | --- | --- | --- |
| ω . Calculating |     | the first | and second |     | derivatives: |     |     |     |
0
|     |     | y˙(t) | ω    |        | ω     | ω     | (ω t+ϕ) |        |
| --- | --- | ----- | ---- | ------ | ----- | ----- | ------- | ------ |
|     |     |       | = a  | cos    | t+a   |       | cos     | (5.90) |
|     |     |       | 1    | 1      | 1     | 0 0   | 0       |        |
|     |     | y¨(t) | = −a | ω2 sin | ω t−a | ω2sin | (ω t+ϕ) | (5.91) |
|     |     |       | 1    | 1      | 1     | 0 0   | 0       |        |
If ω is much smaller than ω , the first term on the right hand sides of
| 1   |     |     |     | 0   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Equations (5.90) and (5.91) can be neglected, and one can solve for the magnitude
| and phase | angle | of the | fundamental |           | frequency   | component: |     |        |
| --------- | ----- | ------ | ----------- | --------- | ----------- | ---------- | --- | ------ |
|           |       |        |             | a2 = y˙/ω | )2+(y¨/ω2)2 |            |     | (5.92) |
|           |       |        |             | 0         | 0           |            | 0   |        |
|           |       |        | ϕ+ω         | t         | = arctan    | (−y¨/ω     | y˙) | (5.93) |
|           |       |        |             | 0         |             |            | 0   |        |
One could design a least squares solution in the spirit of Chapter 3 with similar
assumptions about the two frequencies. However, as is to be expected, the resulting
| algorithms | are | far more | sensitive | to  | noise |     |     |     |
| ---------- | --- | -------- | --------- | --- | ----- | --- | --- | --- |
Estimation of fault location from terminal voltages and currents of a series com-
pensated transmission line remains a difficult problem. As in traditional relaying,

Problems 185
phase-comparisonrelayingandlongitudinaldifferentialprotectionaretheprotection
schemes of choice for such lines.
5.8 Summary
In this chapter we have examined line relaying algorithms. The interested reader
is referred to other books on the
subject.31,32
We have seen that the fundamen-
tal limitation of all of the various algorithms is the presence of unpredictable
non-fundamental frequency signals in the voltage and current waveforms just after
fault inception. Whether the algorithm is attempting to estimate the fundamental
frequency components of voltage and current to estimate the impedance of using a
series R-L model of the line, these unmodeled signals cause errors in the estimated
fault location. The role of the exponential offset in the fault current is an important
consideration in differentiating between algorithms. If the offset is removed out-
side to the relaying algorithm by analog filtering or a separate subroutine, then the
Fourier type algorithms offer considerable advantages in terms of simplicity and
performance. The differential-equation algorithms do not require that the offset be
removedbutdohavesomeperformancelimitationsforlonghigh-voltagelinesifthe
system structure at the source bus is complicated. If the error terms in the measured
current and voltage are assumed to have a significant variation in their statistical
description during the relaying interval, the Kalman filtering approach may be indi-
cated. The increased computation burden must be considered along with problem
of the need for a more detailed error model.
Additional features of relaying algorithms such as their ability to determine the
fault type should also be considered. The use of Clarke or Symmetrical Compo-
nents provides a technique for determining fault type for the algorithms presented.
The consequence of mis-classification of the fault is an additional consideration in
algorithm selection.
Finally, there is an inherent speed-reach limitation in all distance relaying. Given
the unpredictable nature of the non-fundamental frequency components of the
post-fault current ad voltage, close-in faults may be cleared confidently with short
windowalgorithmsbuttheremovereachoftherelayrequiresalongerdatawindow.
Thedistantreachoffixedwindowdigitalrelayingalgorithmsmustbesetwiththese
limitations in mind. An adaptive speed-reach characteristic is an important feature
of any relaying program.
Problems
5.1 Determine a value of c in Equation (5.6) so that Y = 0 for the third har-
1 c
monic.
5.2 Work out the algorithm suggested by Equation (5.23) if the signal set includes
the three terms s (t) = cos ω t, s (t)= sinω t and s (t) = e−(R/L)t.
1 o 2 o 3

| 186 |     |     |     |     |     |     | Transmission | line relaying |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- |
5.3
Develop a recursive form of a two-cycle Fourier algorithm with a sampling
| rate        | of four | samples    | per | cycle.  |     |               |         |     |
| ----------- | ------- | ---------- | --- | ------- | --- | ------------- | ------- | --- |
| 5.4 Compare |         | the answer | to  | Problem | 5.2 | with Equation | (5.67). |     |
5.5 Show that the components of the residual vector r in Equation (5.79) obey a
recursive relationship similar to Equations (5.37) and (5.38).
5.6 Derive the Symmetrical Component Distance Relay equations.
5.7 Derive distance calculation equations for two lines with mutual coupling.
5.8 Show that the SCDR produces the correct distance calculation even if one of
| the | voltages | is due | to  | a blown | fuse. |     |     |     |
| --- | -------- | ------ | --- | ------- | ----- | --- | --- | --- |
5.9 Show that the SCDR maintains directionality for all unbalanced faults even
| when        | the      | fault is  | a bolted | fault. |       |     |     |     |
| ----------- | -------- | --------- | -------- | ------ | ----- | --- | --- | --- |
| 5.10 Derive | the      | response  | of       | a b-c  | relay |     |     |     |
| (a)         | to an    | a-b fault |          |        |       |     |     |     |
| (b)         | to a b-g | fault.    |          |        |       |     |     |     |
5.11 Calculate the voltage changes in phase a, b, c at the relay location of a line
fed from a source as a function of the Source to Line Impedance Ratio (SIR).
| Assume | suitable |     | X /X | and | neglect | R and C. |     |     |
| ------ | -------- | --- | ---- | --- | ------- | -------- | --- | --- |
|        |          |     | m    | s   |         |          |     |     |
π-section
5.12 Assume a single-phase model of a transmission line. Calculate the
voltage and current transients for a line-end fault. Determine the error in
the differential-equation algorithm if the source is purely inductive. Assume
suitable values for L and C for (a) a long line and (b) a short line.
References
[1] Gilbert,J.C.,Udren,E.A.andSackin,M.(1977)Evaluationofalgorithmsforcomputer
relaying, IEEE Publication no. 77CH1193 PWR, Paper no. A77-520-0, IEEE PES
| Summer | Meeting, |     | Mexico | City, | pp. 1–8. |     |     |     |
| ------ | -------- | --- | ------ | ----- | -------- | --- | --- | --- |
[2] B.J.Mann,andI.F.Morrison(1971)Digitalcalculationofimpedancefortransmission
line protection, IEEE Trans. on PAS, vol. 90, no. 1, pp. 270–279.
[3] Gilchrist,G.B.,RockefellerG.D.andUdren,E.A.(1972)High-speeddistancerelaying
usingadigitalcomputer,PartI:Systemdescription,IEEETrans.onPAS,vol.91,no.3,
pp. 1235–1243.
[4] Thorp,J.S.,Phadke,A.G.,HorowitzS.H.andBeehler,J.E.(1979)Limitstoimpedance
| relaying, | IEEE | Trans. | on  | PAS, vol. | 98, | no. 1, pp. | 246–260. |     |
| --------- | ---- | ------ | --- | --------- | --- | ---------- | -------- | --- |
[5] SachdevM.S.andBaribeau,M.A.(1979)ADigitalcomputerrelayforimpedancepro-
tection of transmission lines, Trans. of Engineering and Operating Division Canadian
| Electrical | Association, |     | vol. | 18, | Part 3, | no. 79-SP-158, | pp. 1–5. |     |
| ---------- | ------------ | --- | ---- | --- | ------- | -------------- | -------- | --- |

References 187
[6] Luckett, R.G., Munday, P.J. and Murray, B.E. (1975) A substation-based computer
for control and protection, Developments in Power System Protection, IEE Confer-
ence Publication No. 125, pp. 252–260.
[7] Phadke, A.G., Hlibka, T., Ibrahim, M. and Adamiak, M.G. (1979) A microprocessor
based symmetrical component distance relay, Proceedings of PICA, Cleveland.
[8] McInnes,A.D.andMorrison,I.F.Realtimecalculationsofresistanceandreactancefor
transmissionlineprotectionbydigitalcomputer(1970)Elec.Eng.Trans.IE,Australia,
vol. EE7, no. 1, pp. 16–23.
[9] Ranjbar, A.M. and Cory, B.J. (1975) An improved method for the digital protection
of high voltage transmission lines, IEEETrans.onPAS, vol. 94, no. 2, pp. 544–550.
[10] Breingan, W.D. Chen, M.M. and Gallen, T.F. (1979) The laboratory investigation of
a digital system for the protection of transmission lines, IEEE Trans. on PAS, vol. 98,
no. 2, pp. 350–368.
[11] Smolinski, W.J. (1980) An algorithm for digital impedance calculation using a single
pi section, IEEE Trans. on PAS, vol. 98, no. 5, pp. 1546–1551, and vol. 99, no. 6,
pp. 2251–2252.
[12] Girgis, A.A. and Brown, R.G. (1981) Application of Kalman filtering in computer
relaying, IEEE Trans. on PAS, vol. 100, no. 7, pp. 3387–3397.
[13] GirgisA.A.andBrown,R.G.(1983)Modelingoffault-inducednoisesignalsforcom-
puter relaying applications, IEEE Trans. on PAS, vol. 102, no. 9, pp. 2834–2841.
[14] Sachdev, M.S., Wood H.C. and Johnson, N.G. (1985) Kalman filtering applied to
power system measurements for relaying, IEEE Trans. on PAS, vol. 104, no. 12,
pp. 3565–3573.
[15] Swift, G.W. (1979) The spectra of fault induced transients, IEEE Trans. on PAS,
vol. 98, no. 3, pp. 940–947.
[16] Phadke, A.G., Hlibka, T., Adamiak, M.G., Ibrahim, M. and Thorp, J.S. (1981) A
microcomputerbasedultra-highspeeddistancerelay:Fieldtests,IEEETrans.onPAS,
vol. 100, no. 4, pp. 2026–2036.
[17] Centeno, V. (1988) Mimic circuit simulation in real time, MS Thesis, Virginia Tech.
[18] Mann B.J. and Morrison, I.F. (1971) Relaying a three-phase transmission line with a
digital computer, IEEE Trans. on PAS, vol. 90, no. 2, pp. 742–750.
[19] Clarke, E. (1943) CircuitAnalysisofA-CPowerSystems, vol. I, John Wiley & Sons,
Inc. New York.
[20] Phadke, A.G., Hlibka T. and Ibrahim, M. (1977) Fundamental basis for dis-
tance relaying with symmetrical components, IEEE Trans. on PAS, vol. 96, no. 2,
pp. 635–646.
[21] AndrichakJ.G.andWilkinson,S.B.(1976)Considerationsofspeed,dependabilityand
security in high speed pilot relaying schemes, Minnesota Power Systems Conference,
October 1976.
[22] UdrenE.A.andSackin,M.(1980)RelayingFeaturesofanIntegratedMicroprocessor-
BasedSubstationControlandProtectionSystem,IEEConferencePublicationno.185,
London, U.K., April 1980, pp. 97–101.
[23] Chaari,O.,Meunier,M.andBrouaye,F. (1996)Wavelets:anew toolfor theresonant
grounded power distribution systems relay, IEEE Transactions in Power Delivery,
vol. 11, no. 3, pp. 1301–1308.

| 188 |     |     | Transmission | line relaying |
| --- | --- | --- | ------------ | ------------- |
[24] Magnago F.H. and Abur, (1998) A. Fault location using wavelets, IEEE Trans on
| Power Delivery, | vol. 13, | no. 4, pp. 1475–1480. |     |     |
| --------------- | -------- | --------------------- | --- | --- |
[25] Nagpal,M.,Sachdev,M.S.,Kao,N.,Wedephol,L.M.(1995)UsingaNeuralNetwork
fortransformerprotection,InternationalConferenceonEnergyManagementandPower
| Delivery, Proceedings | of  | EMPD ’95, pp. 674–679. |     |     |
| --------------------- | --- | ---------------------- | --- | --- |
[26] Sheng, Y. and Rovnyak, S.M. (2002) Decision trees and wavelet analysis for power
transformer protection, IEEE Trans. on Power Delivery, vol. 17, no. 2, pp. 429–433.
[27] Coury, D.V., Thorp, J.S., Hopkinson, K.H. and Birman, K.P. (2002) An agent based
currentdifferentialrelayforusewithautilityInternet,IEEETrans.onPowerDelivery,
| vol. 17, no.1, | pp. 47–53. |     |     |     |
| -------------- | ---------- | --- | --- | --- |
[28] Giovanini, K. Hopkinson, R, Coury, D.V. and Thorp, J.S. (2006) A primary and
backup cooperative protection system based on wide area agents, IEEE Trans. on
| Power Delivery, | vol. 21, | no. 3, pp. 1222–1230. |     |     |
| --------------- | -------- | --------------------- | --- | --- |
[29] Tong, X. Wang, X. and Ding, L. (2008) Study of information model for wide-area
backupprotectionagentinsubstationbasedIEC61850,ThirdInternationalConference
on Electric Utility Deregulation and Restructuring and Power Technologies, 2008.
| Nanjing, China, | pp. 2212–2216. |     |     |     |
| --------------- | -------------- | --- | --- | --- |
[30] Rockefeller,G.D.andUdren,E.A.(1972)High-speeddistancerelayingusingadigital
computer, Part II: Test results, IEEE Trans. on PAS, vol. 91, no. 3, pp. 1244–1252.
[31] JohnsA.T.andSalman,S.K.(1995)DigitalProtectionforPowerSystems,Peregrinus,
Ltd.
[32] Ziegler, B. (1999) NumericalDistanceProtection, Siemens.

6
Protection of transformers,
machines and buses
6.1 Introduction
This chapter is concerned with algorithms for the protection of power transformers,
generators and buses. All of the devices can be protected with algorithms based
upon ideas of differential protection since measurements at all of the terminals
can be made available to the algorithm. Each type of algorithm, however, must
deal with effects which tend to confuse the percentage differential characteristic.
Algorithms for the protection of power transformers must be designed to operate
correctlyinthepresenceofmagnetizinginrush(whichappearstobeaninternalfault
to the percentage differential characteristic) and in the presence of over excitation,
which has a similar effect. Saturation of the current transformers is an additional
issue in power transformer protection and is a fundamental issue in bus protection.
Generator protection usually consists of many tasks that include control functions
as well. Differential protection of generators is usually a straightforward task, since
the current transformers used are matched and sized carefully to produce very little
differential current for external faults. Motor protection also incorporates many
control tasks.
These issues and the conventional solutions to these problems are described
in Chapter 2. In some cases, such as the use of harmonic restraint for dealing
with inrush and over-excitation (Section 2.4), there is an almost direct digital
implementation of a conventional relaying practice. There are, however, subtle
differences in the way analog filters obtain the harmonic content of signals as
opposed to digital techniques. In other cases of conventional relaying practice, such
as high impedance bus protection (Section 2.5), there is no digital implementa-
tion and new digital solutions must be found. For generators, phasor calculation of
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

| 190 |     |     | Protection | of transformers, | machines | and buses |
| --- | --- | --- | ---------- | ---------------- | -------- | --------- |
currents,voltagesandfrequencymeasurementsaresufficienttosatisfyallprotection
needs.
In an integrated digital substation protection system, new solutions to some of
these problems are made possible by an increase in the data that can be used
in decision making. Conventional power transformer protection uses only current
measurements. In an integrated substation it is assumed that all the samples of
voltages and currents will be synchronized so that data can be shared, both for
backupandforimproveddecisionmaking.Theuseofvoltagemeasurementsisthen
possible in transformer protection. In the next section a number of different power
transformeralgorithmswillbedescribed,someofwhichcloselyfollowconventional
approaches and some of which are unconventional in terms of their use of voltage
measurements. The reader is referred to Section 2.4 for the background material on
| transformer | protection. |     |            |     |     |     |
| ----------- | ----------- | --- | ---------- | --- | --- | --- |
| 6.2 Power   | transformer |     | algorithms |     |     |     |
Some version of the percentage differential characteristicis a part of almost all pro-
posed transformer algorithms. The only addition that should be made to Section 2.4
andFigure2.11isthatformulti-windingtransformersthereareanumberofrestraint
currents. If we consider a three-winding transformer as shown in Figure 6.1 with
the current polarities as shown, the trip current is given by
|             |         |             | I = I +I       | +I  |     |     |
| ----------- | ------- | ----------- | -------------- | --- | --- | --- |
|             |         |             | T 1            | 2 3 |     |     |
| while there | are two | restraining | currents given | by  |     |     |
|             |         |             | I = I −I       | −I  |     |     |
|             |         |             | R1 1           | 2 3 |     |     |
and
|     |     |     | I = −I | +I −I |     |     |
| --- | --- | --- | ------ | ----- | --- | --- |
|     |     |     | R2 1   | 2 3   |     |     |
Thesecondrestraintcurrentisnecessarytoprotectthetransformeroperatingwith
the primary breaker open. Although much of the original algorithm development
I
2
I 1
I
3
|     |     | Figure | 6.1 A three-winding | transformer |     |     |
| --- | --- | ------ | ------------------- | ----------- | --- | --- |

Power transformer algorithms 191
hasbeenonasingle-phasebasis,theultimateapplicationisonathree-phasedevice.
Thus, there would be three trip currents (one per phase) and six restraint currents
(two per phase) for a three-phase three-winding transformer.
While the percentage differential characteristic of Figure 2.11 could be applied
to each phase (checking each of the restraint currents against the trip current) on
a per sample basis, it is clear that there are error terms in the samples (as in line
relaying)andthatsomefilteringwouldimproveperformance.Moreimportantly,the
percentage differential characteristic must be inhibited during periods of magnetiz-
inginrushorover-excitation.Thefirstclassoftransformeralgorithmsincludesthose
whichformarestraintforthepercentagedifferentialfromthecurrentmeasurements
themselves.
6.2.1 Current derived restraints
As pointed out in Section 2.4, the presence of second harmonic in the transformer
inrush current and the presence of fifth harmonic in the current that flows under
conditions of over-excitation lead to the principle of harmonic restraint. In analog
relays filters are used to obtain some combination of non-fundamental frequency
components. When the output of these filters is high the relay is restrained. Early
digital versions of the harmonic restraint-percent-differential relay differ in their
technique for obtaining the harmonic content of the currents. Techniques based on
wave shape identification,1 on the use of recursive band-pass digital filters,2 on
cross correlation with sinusoids or square waves,3 on finite impulse response digi-
tal filters,4 on Walsh type transforms,5 least square curve fitting,6 and the discrete
Fourier transform7 have been proposed. The wave shape identification is based
on the observation that under inrush conditions the peaks of the current wave are
either closer together or farther apart than is normal. The remaining algorithms are
allattemptstoobtainsimplecomputationaltechniquesfordeterminingtheharmonic
content of the currents. The concern with computational efficiency is motivated by
thelargenumberofcurrentsthatwouldbeinvolvedforathree-phasemulti-winding
transformer. As was pointed out in Chapter 4, the discrete Fourier transform pro-
duces optimal estimates if a constant error covariance is assumed. The recursive
form of the DFT for fundamental and harmonic frequencies is particularly simple
with an appropriate sampling rate. These recursive DFT calculations were found to
represent the best compromise between speed of calculation and accuracy of the
results.8
The recursive form of the full-cycle Fourier calculation of the nth harmonic (in
complex form – see Equation (4.34)) for samples ending at sample L is given by
2
Y
(L)
= Y
(L−1)
+ [y −y
]e−jnLθ
(6.1)
n n K L L−K
where K(θ)= 2π. Thedifference between Equations (6.1) and (4.34) isthe n in the
exponent and the scaling of 2/K that was omitted in Equation (4.34). That is, the

| 192 |     |     |     | Protection | of  | transformers, | machines | and buses |
| --- | --- | --- | --- | ---------- | --- | ------------- | -------- | --------- |
Table 6.1 One cycle of coefficients for the fundamental, the second harmonic, and the
fifth harmonic with a sampling frequency of 12 samples per cycle
| Harmonic  | 1   | 1   | 1   | 1   | 2 2 2 | 2   | 5 5 | 5 5 |
| --------- | --- | --- | --- | --- | ----- | --- | --- | --- |
| Real      | x   | x   |     |     | x x   |     | x x |     |
| Imaginary |     |     | x   | x   | x     | x   |     | x x |
Channel Gain
| 1.0   | x   |     | x   |     | x x |     | x   | x   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.866 |     | x   |     | x   | x   | x   | x   | x   |
n
| 1   | 1    | 0   | 0    | 0      | 1 0 0 | 0   | 1 0    | 0 0    |
| --- | ---- | --- | ---- | ------ | ----- | --- | ------ | ------ |
| 2   | 0    | 1   | 1/2  | 0 1/2  | 0 0   | 1   | 0 −1   | 1/2 0  |
| 3   | 1/2  | 0   | 0    | 1 −1/2 | 0 0   | 1   | 1/2 0  | 0 −1   |
| 4   | 0    | 0   | 1    | 0 −1   | 0 0   | 0   | 0 0    | 1 0    |
| 5   | −1/2 | 0   | 0    | 1 −1/2 | 0 0   | −1  | −1/2 0 | 0 −1   |
| 6   | 0    | −1  | 1/2  | 0 1/2  | 0 0   | −1  | 0 1    | 1/2 0  |
| 7   | −1   | 0   | 0    | 0      | 1 0 0 | 0   | −1 0   | 0 0    |
| 8   | 0    | −1  | −1/2 | 0 1/2  | 0 0   | 1   | 0 1    | −1/2 0 |
| 9   | −1/2 | 0   | 0 −1 | −1/2   | 0 0   | 1   | −1/2 0 | 0 −1   |
| 10  | 0    | 0   | −1   | 0 −1   | 0 0   | 0   | 0 0    | −1 0   |
| 11  | 1/2  | 0   | 0 −1 | −1/2   | 0 0   | −1  | 1/2 0  | 0 1    |
| 12  | 0    | 1   | −1/2 | 0 1/2  | 0 0   | −1  | 0 −1   | −1/2 0 |
correction term for the nth harmonic is the difference between the newest sample
and the oldest (one cycle old) multiplied by an angle that rotates more rapidly for
| the higher | harmonics. |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
At a sampling rate of 12 samples per cycle the only irrational number involved
√
in the update is 3/2. If this multiplication is accomplished externally by a voltage
divider or in software, as in Example 4.2, then a table of coefficients for the mul-
tiplications in Equation (6.1) can be given in terms of the two channels of data, as
| shown in | Table 6.1. |     |     |     |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Forathree-windingtransformerthefundamental,second,andfifthharmonicmust
becomputedforeachofninephasecurrents.Thereisevidencethatasecurerestraint
function for a three-phase transformer can be formed by combining the harmonics
fromallthreephases.9
Atypicalalgorithmmightthenformtwoharmonicrestraints:
one the sum of the three second harmonic magnitudes, and the second the sum of
the three fifth harmonic magnitudes. Denoting these sums as I and I , the relay
|               |       |             |     |        |     |     | H2 H5 |     |
| ------------- | ----- | ----------- | --- | ------ | --- | --- | ----- | --- |
| is restrained | for a | given phase | if  |        |     |     |       |     |
|               |       |             |     | |I | < | α   |     |       |     |
T
or
|     |     |     | |I  | | < β|I | |   |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- |
|     |     |     |     | T       | R1  |     |     |     |

Power transformer algorithms 193
or
|I | < β|I | (6.2)
T R2
or
|I | < γ|I |
H2 T
or
|I | < δ|I |
H5 T
where α is the threshold value in Figure 2.11, β is the slope of the percentage dif-
ferential characteristic and γ and δ are the percent harmonic restraints. The currents
in Equation (6.2) are the full cycle phasor values computed from Equation (6.1). It
should be noted that the factors affecting the choice of these parameters include not
only the transformer type and steel but also the design of the anti-aliasing filters.
The need for a fifth harmonic implies a sampling frequency of at least 12 samples
per cycle. At that rate, the fifth harmonic is quite close to the anti-aliasing filter
cut-off frequency and may be attenuated by the filter. The parameter γ must be
selected with this effect in mind.
As an example of this type of algorithm, the response of the various restraint
currents for an internal a to ground primary fault are shown in Figure 6.2. The fault
occurred approximately at sample 14. Prior to sample 17, before any phase had
developed a trip signal, the second and fifth harmonic restraints were effective. At
sample 17 the phase a differential indicated a trip but the relay was restrained by
the harmonics. The fifth harmonic drops out at sample 22 and the second harmonic
restraint drops out at sample 27. The trip signal would be issued at sample 27, one
cycle after fault initiation. In general the harmonics develop more rapidly than the
10,000
I
T
I
1,000 R1
I
H2
100
I
H5
14 20 25 Sample
Figure 6.2 The response of the restraint and trip currents to an internal a-ground fault

| 194 |     |     | Protection | of transformers, | machines | and buses |
| --- | --- | --- | ---------- | ---------------- | -------- | --------- |
fundamental during a transient so that the relay is restrained for approximately a
full cycle by the harmonic restraints. In effect the harmonic restraint acts much like
| the transient | monitor | of Chapter | 5.  |     |     |     |
| ------------- | ------- | ---------- | --- | --- | --- | --- |
| 6.2.2 Voltage | based   | restraints |     |     |     |     |
As pointed out in the Introduction, it is reasonable in an integrated substation
protection system to assume that bus voltage measurements would be available for
transformer protection. While the requirement of additional voltage measurements
would increase the cost of a stand-alone transformer protection unit, such voltage
measurements may be obtained quite inexpensively in an integrated system. In fact,
an early solution to the inrush problem used voltage measurements to restrain a
differential.10
percentage The so-called ‘tripping suppressor’ used a voltage relay
to suppress the tripping function if the voltage was high. In its early analog form,
the ‘tripping suppressor’ was found to be slower than harmonic restraint devices.
Since the harmonic restraint algorithm is essentially a one cycle relay and since the
short window line protection algorithms can compute voltage phasors in as little as
a quarter of a cycle, it has been suggested that a digital ‘tripping suppressor’ may
| be faster | than the digital | harmonic | restraint | algorithm.11 |     |     |
| --------- | ---------------- | -------- | --------- | ------------ | --- | --- |
The proposed algorithm used a one-half cycle window for the calculation of
fundamental frequency components of trip and restraint currents and the primary
voltageforeachphase.Itwasdeterminedthatitwasnecessarytoincludeatransient
monitor (Section 4.5) for the voltage signals. Thus for a three-winding transformer,
one trip and two restraint currents, the primary voltage and the transient monitor
value must be updated for each phase. This total of 27 updates of the form of
Equations (4.37) and (4.38) (counting real and imaginary parts for the voltage and
current phasors) compares with 30 such simple updates for the harmonic restraint
algorithm (the fundamental of the tripand two restraint currents and thesecond and
fifth harmonic of one of the restraint currents for each phase). The saving is simply
| that t is | real rather | than complex. |     |     |     |     |
| --------- | ----------- | ------------- | --- | --- | --- | --- |
V
| The relay | is restrained | for a | given phase | if  |     |     |
| --------- | ------------- | ----- | ----------- | --- | --- | --- |
|I | < α
T
or
|     |     |     | |I | < β|I | |   |     |     |
| --- | --- | --- | ---------- | --- | --- | --- |
|     |     |     | T          | R1  |     |     |
or
|     |     |     | |I | < β|I | |   |     | (6.3) |
| --- | --- | --- | ---------- | --- | --- | ----- |
|     |     |     | T          | R2  |     |       |
or
|V|>σ

Power transformer algorithms 195
_
|v|
t
V
13 27 Sample
v
Figure 6.3 Phase c voltage quantities for the voltage restraint algorithm – inrush
or
|t |>ρ
V
The quantities in Equation (6.3) are now half cycle phasor results rather than
the full cycle quantities of Equation (6.2). The first three inequalities in Equation
(6.3) produce the percentage differential characteristic while the last two restrain
if the voltage is high or the transient monitor indicates that the voltage phasor is
unreliable. The transient monitor is necessary since the voltage waveform can be
so distorted that the half cycle phasor for the voltage fails to be large enough.
The voltage quantities for phase c for an inrush case are shown in Figure 6.3. The
serious voltage distortion is due to the inrush. The inrush is sufficient to produce
a current differential trip in phases a and c. For samples 17–23 only the transient
monitorrestrainsphasea,whileatsample27themonitordropsbutthehighvoltage
restrains phase c.
The voltage restraint algorithm is potentially faster than the harmonic restraint
algorithm since it is based on a half cycle computation. It is also somewhat less
complicated to implement on a microprocessor.
6.2.3 Flux restraint
There are other possible uses of measured voltages. It has been suggested that,
using a linear model of the transformer, the measured currents could be used to
computetheterminalvoltages.12 Thecomparisonofthecomputedvoltageswiththe
measuredvoltageswouldthengiveanindicationofwhetherthelinear(unsaturated)

| 196 |     |     | Protection | of  | transformers, | machines | and buses |
| --- | --- | --- | ---------- | --- | ------------- | -------- | --------- |
modelwascorrectorwhethersaturationhadbegun.Anotherpossibilityistousethe
measured voltages and currents to determine the internal flux of the transformer.13
Neglecting the resistance of the winding, the voltage at the terminals of a trans-
former winding, v(t), the current through that winding, i(t), and the flux linkage,
(cid:6)(t)
| of the | transformer are | related |       |             |     |     |     |
| ------ | --------------- | ------- | ----- | ----------- | --- | --- | --- |
|        |                 |         | di(t) | d(cid:6)(t) |     |     |     |
v(t)−L
|     |     |     |     | =   |     |     | (6.4) |
| --- | --- | --- | --- | --- | --- | --- | ----- |
|     |     |     | dt  | dt  |     |     |       |
where L is the leakage inductance of the winding. If Equation (6.4) is integrated
| between sample | times t | and t |     |     |     |     |     |
| -------------- | ------- | ----- | --- | --- | --- | --- | --- |
|                | 1       | 2     |     |     |     |     |     |
(cid:4)t2
|     | (cid:6)(t )−(cid:6)(t | )   | = v(t)dt−L[i(t |     | )−i(t | )]  |     |
| --- | --------------------- | --- | -------------- | --- | ----- | --- | --- |
|     | 2                     | 1   |                |     | 2     | 1   |     |
t1
Using trapezoidal integration as in Equations (4.45) and (4.46) and equally spaced
| samples, we | can write |     |     |     |     |     |     |
| ----------- | --------- | --- | --- | --- | --- | --- | --- |
(cid:1)t
|     | (cid:6)(t ) (cid:6)(t | )+  | [v(t )+v(t | )]−L[i(t | )−i(t | )]  |     |
| --- | --------------------- | --- | ---------- | -------- | ----- | --- | --- |
=
|     | 2   | 1   | 2 2 | 1   | 2   | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
kth.
| or with subscript | k denoting | the |     |     |     |     |     |
| ----------------- | ---------- | --- | --- | --- | --- | --- | --- |
(cid:1)t
|     | (cid:6) | (cid:6) |        |            |        |     |       |
| --- | ------- | ------- | ------ | ---------- | ------ | --- | ----- |
|     | k+1     | = k +   | [v k+1 | +v k ]−L[i | k+1 −i | k ] | (6.5) |
2
The current in Equation (6.5) is the trip current I +I +I for each phase of the
|     |     |     |     |     | 1 2 3 |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- |
three-winding transformer. The voltage in Equation (6.5) is the winding voltage.
In the case of delta windings, the line–line voltages would have to be obtained
from the phase to neutral voltages. Similarly, if the transformer were grounded
through an impedance, it would be necessary to account for the neutral potential.
Equation (6.5) permits the computation of the mutual flux linkage from measured
values of currents and voltages. If the initial flux linkage were known, then at each
sample it would be possible to track the flux-current plot of the transformer. The
i−(cid:6)
plane is shown in Figure 6.4. The open circuit magnetizing curve of the
transformer is shown along with the flux-current curve that would be associated
with an internal fault. It can be seen that the flux-current characteristic can provide
an effective restraint function. If the flux computed from Equation (6.5) and the
measured current (i ,(cid:6) ), lie on the open circuit magnetizing curve, then the relay
k k
(cid:6))
should be restrained. There are distinct regions in the (i, plane corresponding to
fault or no-fault conditions as shown. It should be noted that there are no phasor
calculations involved and that the percentage differential and the flux restraint are

| Power transformer | algorithms |            |     |     | 197 |
| ----------------- | ---------- | ---------- | --- | --- | --- |
|                   |            | Λ no fault |     | Λ   |     |
fault
i i
d d
fault
no fault
|     |     | (a) |     | (b) |     |
| --- | --- | --- | --- | --- | --- |
Figure 6.4 The flux-current plane. (a) Fault and no-fault regions. (b) Effect of unknown
remnant flux
instantaneous. While the simplicity of computation is appealing, some averaging is
clearly called for to provide security. In addition there is a problem in assuming
the initial flux linkage is known. Figure 6.4(b) shows the effect of the unknown
initial flux. Note that it is not possible to discriminate between fault and no-fault
situations in the (i, (cid:6)) plane with an unknown initial flux.
Both problems can be resolved by considering the slope of the flux curve. From
Figure 6.4(b) it can be seen that the open circuit magnetizing is characterized by
differentslopesinthe(i,(cid:6))plane.UsingEquation(6.5),wecanformanexpression
(d(cid:6)/di)
| for the slope |          | as               |            |         |     |
| ------------- | -------- | ---------------- | ---------- | ------- | --- |
|               | (cid:12) | (cid:13)         | (cid:2)    | (cid:3) |     |
|               | d(cid:6) | (cid:6) −(cid:6) | (cid:1)t e | +e      |     |
|               |          | = k              | k−1 = k    | k−1 −L  |     |
(6.6)
|     | di  | i −i    | 2 i | −i  |     |
| --- | --- | ------- | --- | --- | --- |
|     |     | k k k−1 | k   | k−1 |     |
OperationintheunsaturatedregionoftheopencircuitmagnetizingcurveFigure6.4
produces a large value for the slope (d(cid:6)/di) while the fault or no-fault (saturated)
regions have much smaller slopes. It is not possible to distinguish between the
fault or no-fault regions on the basis of the slope but it is not necessary to do
so. During an internal fault the (d(cid:6)/di) samples remain small (the fault region of
(d(cid:6)/di)
Figure 6.4) continuously. During inrush, on the other hand, the samples
alternate between large and small values as the magnetizing curve is traced. Thus
| if we define | a positive | restraint index | k , as follows |     |     |
| ------------ | ---------- | --------------- | -------------- | --- | --- |
r
k = k +1
r r
| if the current | differential | indicates trip |     |     |     |
| -------------- | ------------ | -------------- | --- | --- | --- |

| 198 |     |     | Protection | of transformers, | machines | and buses |
| --- | --- | --- | ---------- | ---------------- | -------- | --------- |
| k   |     |     | k          |                  |          |           |
| r   |     |     | r          |                  |          |           |
i
| 20  | a b |     | 20  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| 10  |     |     | 10  |     |     |     |
|     |     | a   | a   |     |     |     |
b
|     | 10 20 | 30      |     |       |       |         |
| --- | ----- | ------- | --- | ----- | ----- | ------- |
|     |       |         |     | 10 20 | 30 40 |         |
|     |       | samples |     |       |       | samples |
i
a
|     | (a) |     |     | (b) |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Figure 6.5 The behavior of the restraint index. (a) An internal a-b fault. (b) Inrush pro-
| duced following | the removal | of an external | three-phase | fault |     |     |
| --------------- | ----------- | -------------- | ----------- | ----- | --- | --- |
and if
|     | (d(cid:6)/di) | >ζ  |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- |
k
(cid:14)
|     |     |      | >0     | (d(cid:6)/di) | >ζ  |       |
| --- | --- | ---- | ------ | ------------- | --- | ----- |
|     |     | k −1 | if k   | and           |     |       |
|     | k   | = r  | r      |               | k   | (6.7) |
|     |     | r k  | if k = | 0             |     |       |
|     |     | r    | r      |               |     |       |
then k will increase whenever the current differential shows a trip and the flux
r
is not on the steep part of the magnetizing curve. In fact, the index grows almost
monotonicallyforinternalfaultsbutshowsasaw-toothbehaviorfornon-faultcases.
The threshold value ζ simply separates the high and low slopes of the magnetizing
curve.
The behavior of the restraint index for a phase a to b internal fault along with
the phase a differential current are shown in Figure 6.5(a). The hesitation in the
growth of k r for phases a and b indicates that there were points on the fault current
waveform when the transformer was saturated. The restraint index for phases a and
b for an inrush condition along with the phase a are shown in Figure 6.5(b). The
maximum value attained by k r is six. For 21 cases reported in reference 13, six
was the largest value ever encountered. Figure 6.5 is obtained for a sampling rate
of 12 samples per cycle. It is clear that the maximum value of k depends on the
r
sampling rate. The trip decision would be made when k r exceeded some threshold
k . The choice k of illustrates the familiar conflict between the speed and
| rrmax | rrmax |     |     |     |     |     |
| ----- | ----- | --- | --- | --- | --- | --- |
security of any relay. If k is small the relay will be fast but will have some
rrmax
chance of a false trip. As k is made larger the relay becomes more secure but
rrmax
slower.
With a multi-winding transformer it is possible that the transformer might be
energized from any of its windings. The voltage required for calculating the flux
must then be obtained from the appropriate bus. Again, in an integrated substation

| Power transformer |     | algorithms |     |     |     |     |     |     |     | 199 |
| ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
it is assumed that this voltage could be made available from the module which is
| protecting | equipment |     | connected | to  | the energizing |     | bus. |     |     |     |
| ---------- | --------- | --- | --------- | --- | -------------- | --- | ---- | --- | --- | --- |
A similar algorithm for power transformer protection which also uses measured
voltages and currents has been proposed14. Using a description of a three-winding
(cid:4),
transformer in terms of the reciprocal inductance matrix the terminal description
| of the transformer |     | can         | be written  | as               |                 |            |           |      |     |       |
| ------------------ | --- | ----------- | ----------- | ---------------- | --------------- | ---------- | --------- | ---- | --- | ----- |
|                    |     |             |           |                 |                 | (cid:9)  |           |     |     |       |
|                    |     |             | (cid:1)I    |                  | (cid:4) (cid:4) | (cid:4)    |           |      |     |       |
|                    |     |             |             |                  |                 |            | (cid:9) v | dt   |     |       |
|                    |     |             | 1           |                  | 11 12           | 13         |           | 1    |     |       |
|                    |     |             | (cid:1)I  | = (cid:4)       | (cid:4)         | (cid:4)  | v         | dt  |     | (6.8) |
|                    |     |             | 2           |                  | 21 22           | 23         | (cid:9)   | 2    |     |       |
|                    |     |             | (cid:1)I    |                  | (cid:4) (cid:4) | (cid:4)    | v         | dt   |     |       |
|                    |     |             | 3           |                  | 31 32           | 33         |           | 3    |     |       |
| The sums           | of  | the entries | in each     | row              |                 |            |           |      |     |       |
|                    |     |             |             | (cid:4) =(cid:4) | +(cid:4)        | +(cid:4)   |           |      |     |       |
|                    |     |             |             | 10               | 11              | 12         | 13        |      |     |       |
|                    |     |             |             | (cid:4) =(cid:4) | +(cid:4)        | +(cid:4)   |           |      |     |       |
|                    |     |             |             | 20               | 21              | 22         | 23        |      |     |       |
|                    |     |             |             | (cid:4) =(cid:4) | +(cid:4)        | +(cid:4)   |           |      |     |       |
|                    |     |             |             | 30               | 11              | 32         | 33        |      |     |       |
correspondtoinverseshuntinductancesinanequivalentcircuitofthetransformer.If
we use the normal transformer equivalent circuit as a T-circuit, the series branches
of the T are the leakage inductances and the shunt element is the magnetizing
inductance. The (cid:4)’s are the inverse admittances in an equivalent (cid:7) network. The
(cid:4)
transfer inverse inductances are dominated by the leakage inductances, while
ik
(cid:4)
the driving point inverse io are dominated by the magnetizing inductances. The
algorithm consists of computing the shunt inverse inductances (cid:4) , (cid:4) , (cid:4) from
|     |     |     |     |     |     |     |     |     | 10 20 | 30  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
the measured voltages and currents and the known leakage inductances and testing
| the computed |     | values | against | a threshold. | For              | example, |         |                  |         |     |
| ------------ | --- | ------ | ------- | ------------ | ---------------- | -------- | ------- | ---------------- | ------- | --- |
|              |     |        |         | (cid:14)     | (cid:12) (cid:4) |          | (cid:4) | (cid:13)(cid:15) | (cid:4) |     |
(cid:4) = (cid:4) +(cid:4) + I − (cid:4) v dt+(cid:4) v dt / v dt
|     | 10  | 12  | 13  | 1   | 12  | 1   | 13  | 2   | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wheretrapezoidal integration isused toevaluatethe integrals. Thecomputed values
of the inverse shunt inductances can then be used as the flux is used, to restrain
the percentage differential relay without having to compute the harmonic content
of the currents. It should be noted that the driving point inverse inductances (cid:4)
io
are multiple manifestations of the single magnetizing inductance, and hence com-
(cid:4)
putation of all of the io represents unnecessary repeat calculations of the inverse
magnetizing inductance. In addition the procedure requires the measurement of all
of the voltages.
6.2.4 A restraint function based on the gap in inrush current
A somewhat unusual restraint technique for detecting inrush phenomena in power
transformers has been proposed in reference.15 It is noted that under certain types

200 Protection of transformers, machines and buses
of faults there may be significant amounts of second harmonic in the CT secondary
currents, which may lead to very long trip times for such faults. The solution pro-
posed by the authors is to identify the condition of magnetizing inrush by detecting
the presence of low current (a ‘gap’) when the transformer core is not in saturation.
It is noted by the authors that during inrush conditions the core is not saturated
for at least one quarter of a cycle. This gap in the differential current waveform
is detected, and when present it is used to restrain the relay from operating. The
authors state that this restraint principle avoids the delay in tripping caused by the
presence of second harmonic in the differential current for certain fault types. It is
stated that field experience with this relaying principle has been successful.
It is, of course, possible to adapt this restraint principle in computer relays. The
detection of a gap of quarter cycle in the current waveform will require that a fairly
highsamplingratebeusedsothatasufficientnumberofsampleswillcorrespondto
thecurrentgap.Ifanti-aliasingfiltersareemployedtoprocessthecurrentwaveform,
theireffectontheabilitytodetectthecurrentgapwouldalsohavetobeconsidered.
Thereisnorecordof acomputer relayimplementationusingthisrelayingprinciple.
6.3 Generator protection
Protection of generators with computers has not received as much attention as the
protection of lines or transformers. To begin with, the number of generator protec-
tion systems on a power system is small, since there are few generators on a power
system. Consequently, there is not as big an economic incentive to replace existing
relayingwithcomputerrelaysinthiscase.Secondly,theburdenofprotectingagen-
erating station often fallson a plant control system which must deal with the boiler,
turbine, generator, and exciter system as a whole; and often is already computer
based. Many protection systems in a generating plant are mechanical in nature. The
electrical side of the protection includes the stator and rotor winding protection,
and several other protection and alarm functions which are closer to being control
functions. These have been discussed in Chapter 2, and will be briefly mentioned
again later in this section.
6.3.1 Differential protection of stator windings
Early work in this area was constrained by the capability of the available
microcomputers.16 In the present stage of computer development, percentage
differential protection of stator windings is a relatively easy task. Assuming that
i i
1 2
Figure 6.6 Currents at the two ends of a generator winding

| Generator | protection |     | 201 |
| --------- | ---------- | --- | --- |
simultaneous samples of currents at the two ends of a stator winding are obtained
(see Figure 6.6), a sample by sample percentage differential relation could be used
| to detect | the presence | of a fault: |             |
| --------- | ------------ | ----------- | ----------- |
|           |              | (k)         | (k)+i (k)   |
|           |              | i d =       | i 1 2       |
|           |              | i (k) =     | i (k)−i (k) |
|           |              | r           | 1 2         |
(6.9)
|     |     | i (k) ≤  | Ki (k) do not trip |
| --- | --- | -------- | ------------------ |
|     |     | d        | r                  |
|     |     | i (k)>Ki | (k) trip           |
|     |     | d        | r                  |
whereKistheslopeofthepercentagedifferentialcharacteristic.Iftheestimationof
differentialandrestraintcurrentsismadeonaper-samplebasisasinEquation(6.9),
it would be necessary to take a vote among several samples to confirm that a fault
has indeed occurred, and that the differential current sample is not created by an
| anomalous | data sample | for one of | the currents. |
| --------- | ----------- | ---------- | ------------- |
A somewhat more secure decision is obtained if phasors estimated from i (k) and
1
i 2 (k) are used in this comparison. Either a mimic circuit must be used to eliminate
the influence of the DC offset in the current, or a full cycle DFT technique must
be used to calculate the phasors. The DC offset in the fault current of a generator
is almost certain to decay very slowly, hence a one cycle DFT would be immune
to errors created by DC offset. It is clear that a one cycle DFT makes for a relay
which operates in about one cycle, but this may be fast enough in most cases. The
percentage differential equation in terms of the phasors is similar to the sample
| version | of Equation | (6.9): |         |
| ------- | ----------- | ------ | ------- |
|         |             | I =    | |I +I | |
|         |             | d      | 1 2     |
|         |             | I =    | |I −I | |
|         |             | r      | 1 2     |
(6.10)
|     |     | I ≤ | KI do not trip |
| --- | --- | --- | -------------- |
|     |     | d   | r              |
>KI
|     |     | I d | r trip |
| --- | --- | --- | ------ |
Saturation of current transformers – although possible – is not a probable event in
the case of generator differential protection, as the current transformers are sized
generouslytoavoidsaturationinthefirstcoupleofcycles.Ifatransientmonitor(see
Section4.5)isusedtoinhibitoperationwhenacurrenttransformermaybesaturated,
the phasor comparison will not be made under conditions of CT saturation, and the
worst that could happen is that the relay will be slow to respond for internal faults
if the current transformers should saturate. A small amount of saturation could be
accommodatedwithavariableslopedifferentialrelay,asdescribedinSection6.5.If
differentialrelayingusingsamplesisbeingused,caremustbetakentoterminatethe
sample differential check when saturation is detected (for example by the transient
monitors).

202 Protection of transformers, machines and buses
X
(a) (b)
Figure 6.7 A generator with a ground fault. (a) Generator representation and external
fault.(b)Internalfault.Theinterconnectionofthesequencediagramstakesplaceinsidethe
machine boundary in the latter case
6.3.2 Other generator protection functions
Although the generator differential relay is far more sensitive than its counterpart
used in transformer protection, a ground fault close to the generator neutral would
not be detected if the fault current were less than the sensitivity (slope K) of the
differential characteristic. A sensitive ground fault detection scheme for computer
relaying of generators has been proposed (although there is no field experience
of such a scheme); the relaying scheme is based on the fact that when the stator
currents in a synchronous machine are unbalanced, the field current acquires an
inducedcurrentoftwicethefundamentalfrequency.17 Ifthefieldcurrentissampled
(whichcanonlybedoneeasilywhenthefieldcurrenttothegeneratorisfedthrough
slip rings), its second harmonic component can be calculated and used to indicate
thepresenceofstatorcurrentunbalance. Itthenremainstoverifythattheunbalance
is due to an internal fault, and not to some cause that is external to the generator.
Consider the generator shown in Figure 6.7(a). For the external fault shown, the
negative sequence current flows into the generator as viewed from its terminals; in
other words, the fault – which is the source of the negative sequence voltage – is
external to the generator. When the fault is inside the machine as in Figure 6.7(b),
the negative sequence current flows out from the generator. The ‘in’ and ‘out’ of
course imply a directional calculation. In the reference cited, the direction of the
negative sequence power is used as the restraining function: if the power flows into
the machine, the fault is external, and the presence of second harmonic in the field
current is disregarded. If, on the other hand, the negative sequence power flows out
of the generator, the presence of a second harmonic current indicates an internal
fault. By looking at the circuit diagrams in Figure 6.7, it should be clear that,
for an external fault, the negative sequence current will lag the negative sequence
voltage by almost 90◦, whereas, for an internal fault, the corresponding current will
lead the voltage, with a substantial in-phase component due to the system load.
It seems reasonable that the use of negative sequence reactive power flow may

Generator protection 203
be a better indicator of the direction of the fault than the active power. In any
case, both the restraining quantity (negative sequence real or reactive power) and
the tripping quantity (second harmonic current in the field winding) must reach a
value above a threshold before they can be taken into account, in order to allow for
normal residual unbalances and measurement errors. It should be noted that since
this technique depends upon load current, it does not offer any protection when the
generator carries no load current.
Negative sequence current in a generator is also useful in designing a protection
function to guard against excessive rotor heating during system unbalances. The
cause of the unbalance is usually outside the generator: often it is a system phe-
nomenon. The capability of a rotor to tolera(cid:9)te negative sequence current is defined
by the generator manufacturer in terms of i 2dt, and it is a simple matter for a
2
computer based relay to incorporate a thermal model of the rotor, and monitor the
calculated rotor temperature rise, to determine a more accurate operating limit for
the negative sequence current.
Other generator protection tasks, such as loss of field protection, reverse power
protection, inadvertent energization protection, volts per Hz protection, out-of-step
protection, are all based upon established principles. Computational techniques
described earlier, viz. phasor calculation and frequency calculation, are adequate
for all these tasks. As mentioned earlier, these functions are more in the nature of
control functions, and often the hardest part is to determine what should be done
to cope with an event. How to detect this condition is a much easier task.
It should also be noted that a generator protection system is subject to variable
frequency conditions during start-up and shut-down, and performance of all algo-
rithms at radically different frequencies must be established. Phasor calculations
are affected by the frequency: a phasor calculated by the recursive DFT formula
will rotate in the complex plane at a frequency equal to the difference between the
nominal system frequency and the actual frequency of the signal (see Chapter 8).
Indeed, if the frequency is substantially different from the nominal frequency, the
magnitude and rotational speed of the phasor will be variable even though the
sinusoid may be of a fixed magnitude and frequency. If the positive sequence pha-
sor is computed, these fluctuations in magnitude and speed disappear, and phasor
computations can once again be used.
6.3.3 Sampling rates locked to system frequency
A better alternative may be to use the speed of the generator as an input to the
relay system, and use a phase locked loop to adjust the sampling rate to be a
multiple of the actual system
frequency.18,19
The phasor calculations made with
DFT techniques are exact, and do not require special handling to correct for the
effect of off-nominal frequency. It should be noted that phase locked loops used in
determining sampling clock rates require some time to acquire and track the system
frequency, and sufficient safeguards must be built in to avoid instability of the

204 Protection of transformers, machines and buses
frequency tracking system due to step changes in the input waveforms. Computer
relays based on such principles have been reported in the references cited above.
6.4 Motor protection
Motorsratedfrom600voltsto4800voltsareusuallyprotectedbyfuses,whilethose
ratedat 2400voltsto13800voltsareprotected byrelays.18 Timeovercurrent relays
used for motor protection are no different from those used for feeder protection.
In providing protection for the larger motors with a computer, the currents and
voltages must be sampled, and phasors and symmetrical components calculated.
Time overcurrent relaying can then be done by taking the magnitude of the current
phasors. Another type of protection used for motors consists of protection against
an unbalanced source of supply. This can be provided by taking the magnitude of
the negative sequence current (or voltage) as a measure of the source unbalance,
and if it is found to exceed a pickup setting, the motor is tripped.
An interesting aspect of induction motor protection is to make the protection
respond to the temperature rise in the windings, rather than to the stator current as
would be provided by a time overcurrent
relay.19,20
The computer offers the ability
to create a thermal model of the stator and the rotor, which provides a winding
temperature estimate upon which the determination of a safe operating condition
can be based.
Time overcurrent relays must be set to trip for a locked rotor condition, yet must
tolerate the starting current for the time it takes for the motor to reach its operating
speed. If a motor starts with a high inertia load, then the overcurrent relay may trip
becauseofthelongertimetakenbythemotortoreachitsrunningspeed(andnormal
current). Similarly, it is difficult to set the overload relays, because the capacity of
the motor to tolerate overload is dependent upon the temperature of the windings
before the overload is applied. It is possible to calculate the power loss in the
stator and rotor windings from the terminal voltages and currents, and the machine
constants. This power loss is used in a thermal model which takes into account the
thermal capacity of the machine, its heat loss, and the ambient temperature. In one
implementation of such a model,20 a temperature sensor input is also provided to
make the thermal model more accurate, or even unnecessary. It should be noted
that these features are available in many conventional protection systems.
As with generator protection, motor protection is quite intimately connected with
motor control. Microprocessor based integrated protection and control packages are
becoming common in the industry.
6.5 Digital bus protection
Computer relaying of busbars attracted early
attention,15,21
and then the interest
flagged until recent times, when busbar protection became a part of an integrated
protection and control system for the entire substation.22–24 Bus protection in an
integrated system seems particularly appropriate, as all the inputs needed for bus

Digital bus protection 205
Bus section 1
CB 1 2 3
Line 1
Transf. 1
Line 2
Figure 6.8 A portion of a breaker-and-half substation. The bus protection computer for
bus section 1 can obtain the required currents from other protection computers
protection (currents in all circuit breakers and switches connected to the bus) are
usually available within all other protection systems in the substation. Consider bus
section 1 shown in Figure 6.8, where the protection computers for lines 1 and 2,
and transformer 1, use the currents in circuit breakers CB1, CB2, and CB3. These
current samples could be shared by their respective protection systems with a bus
protection computer through computer-to-computer links. The questions of reliabil-
ity and redundancy of equipment must be addressed separately. Some consideration
of these latter issues will be found in Chapter 9.
As mentioned in Section 2.5, the design of a bus protection system is dominated
byconsiderationofthecurrenttransformerperformance.Firstofall,busdifferential
relayingrequiresthatallcurrenttransformershaveidenticalturnsratios,anobjective
not easy to meet under all circumstances. Any mismatch between CT ratios must
be compensated by auxiliary current transformers which add their own errors to the
bus protection system CT mismatch error. In a computer relay, auxiliary current
transformers are not needed as any main CT ratio mismatch could be corrected
in software. However, a much more serious concern is the saturation of a CT for
an external fault (see Section 2.5). The very elegant solution offered by a high
impedance bus differential relay cannot be used in a computer based protection
system,aseachcurrentisacquiredindividually:noanalogsumofthefeedercurrents
isformed.(Thiscouldbedone,butwoulddefeatasignificantcostbenefitthatresults
from sharing the input information at the computer level.) A new approach to the
problem of bus protection in an integrated system must be found.
Disregarding the problem of CT saturation for the moment, it is clear that a
percentage differential relay, either based upon sample-by-sample comparison of
all the currents, or upon current phasors, can be used. The current phasors – having
significant filtering – provide asensitiveand accurate relayingscheme. Thelatteris
also a slower scheme: a reliable phasor estimate must be formed over a reasonable
data window before differential and restraining current phasors can be determined.
A combination of a phasor based and sample based percentage differential relaying
scheme has been included as a component of the bus protection package in one
commerciallyavailablesystem.23 Thephasorbasedschemecouldbeusedaslongas
there is no significant CT saturation: either early on during a fault before saturation
sets in, or much later after the CTs come out of saturation. The transient monitor

206 Protection of transformers, machines and buses
I I
d
I I
error r
(a) (b)
Figure6.9 Currenttransformermagnetizingcharacteristic.(a)Steadystatesecondarycur-
rent I produces a secondary voltage V, and the magnetizing current I . (b) A nonlinear
error
percentage differential characteristic
function is a convenient indicator of the state of the CT. A quarter cycle phasor
calculation coupled with a quarter cycle transient monitor would provide a suitable
computer based bus differential relay.
An innovation in percentage differential relaying is worth mentioning at this
point.24 In general, a percentage differential relay operates at a constant slope,
under the premise that the CT error (when no transient saturation is considered)
is proportional to the primary current. On the other hand, the CT saturation char-
acteristic clearly shows – see Figure 6.9(a) – that as the CT voltage increases due
to an increase in the secondary current, the errors increase disproportionately. It is
clear that such an error performance calls for a percentage differential characteris-
tic with a progressively increasing slope, as shown in Figure 6.9(b) This variable
slope characteristic would be desirable for both the sample based and the phasor
based percentage differential algorithm. It is provided in a crude form in many con-
ventional bus differential relays, and should be considered for all computer based
differential relays which use magnetic core current transformers.
A common concern with all differential protection is that the CT saturation
may set in a few milliseconds after the inception of a fault. Rather than devising
extremely short-window DFT algorithms, the sample based percentage differential
characteristic could be used to provide protection within the first few milliseconds.
Normally one would prefer to have at least three samples to make a secure decision
in order to eliminatethe possibility of being affectedby a singlebad datapoint. For
external faults, where the percentage differential relay produces restraints, it would
be secure to base such a decision on two or even on one sample: as it is almost
impossible that in case of an internal fault, a bad data point could be of exactly the
right magnitude and polarity to produce a no trip decision. For internal faults, the
decision to trip must be confirmed by a concurrence of three or more data points.
These ideas are illustrated in the flow chart of Figure 6.10.
ThesamplebaseddifferentialrelaymustbedisabledassoonasoneoftheCTssat-
urates. As mentioned earlier, the saturation onset could be detected by the transient

| Digital bus | protection |     |     |     | 207 |
| ----------- | ---------- | --- | --- | --- | --- |
Increment
Trip
counter
|     |        | yes             |     | yes     |     |
| --- | ------ | --------------- | --- | ------- | --- |
|     | Sample |                 |     | counter |     |
|     | ‘k’    | i d (k)>Ki(k) r |     | > limit |     |
|     |        | no              |     | no      |     |
Decrement
No trip
counter
if positive
Figure 6.10 A flow chart for a sample based percentage differential relay. To trip, the
counter must exceed a certain value. The logic is disabled when saturation is detected
∆i
2
∆i
1
Figure 6.11 Logic to determine CT saturation. The anti-aliasing filter influences the level
| setting needed | by the | logic |     |     |     |
| -------------- | ------ | ----- | --- | --- | --- |
monitor function. Alternatively, one could check for the change in the secondary
currentinonesampletime(seeFigure6.11).(cid:1)i isthechangeincurrentduringthe
1
fault while the CT is unsaturated. This is always less than some value determined
by the maximum bus fault current. If the largest expected symmetrical bus fault
| current from | a feeder | is I , then |     |     |     |
| ------------ | -------- | ----------- | --- | --- | --- |
f
|     |     | √           | ω(cid:1)t |     |        |
| --- | --- | ----------- | --------- | --- | ------ |
|     |     | |(cid:1)i < | (cid:1)i  |     |        |
|     |     | | 2I ×2sin  | ≡         |     | (6.11) |
|     |     | 1 f         | 2         | max |        |
where (cid:1)T is the sampling interval. When the CT saturation sets in, the change in
(cid:1)i
current is far more abrupt, and a test at each sample could be used to detect the
| onset of a | transient |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- |
if
|(cid:1)i |<M(cid:1)i
|     |     | k max(cid:1) | no saturation    |     |        |
| --- | --- | ------------ | ---------------- | --- | ------ |
|     |     | ≤M(cid:1)i   | saturation onset |     | (6.12) |
max(cid:1)
where M is an appropriate margin factor to be set somewhat greater than 1.0. Upon
detection of saturation onset, the sample based differential algorithm would be
disabled. The anti-aliasing filters will cushion the collapse of the secondary current
when the CT goes into saturation, as shown by the dotted line in Figure 6.11.

208 Protection of transformers, machines and buses
This effect must be considered to check whether the test defined by inequalities
in Equation (6.12) can be useful. Clearly this softening effect is more pronounced
when low sampling rates are used: they require lower cut-off frequencies in the
anti-aliasing filter. One solution to this problem may be to use a higher sampling
rate – indeed, this should always be the goal for obtaining an improvement in the
speed of response of all relays. Higher sampling rates will also provide many more
samples before the onset of saturation inthe bus relaying application. Alternatively,
one could obtain samples of the unfiltered currents (i.e. without the anti-aliasing
filters) to determine the onset of saturation. Yet another possibility would be to use
analog circuits which would provide a trigger indicating the start of CT saturation.
The analog mimic circuit discussed in Chapter 5, being essentially a differentiating
circuit, would provide such a trigger. The digital mimic circuit would also provide
the same function. Return of the CT to an unsaturated state should be confirmed
by the purity of its output waveform. Once again, this could be done through a
transient monitor function.
A completely different approach to bus protection could be realized through the
application of the traditional phase comparison or directional comparison relaying.
The direction of the current with respect to a polarizing voltage signal, or an appro-
priate residual current could be used to determine if all feeder currents from a bus
flow into the bus, indicating the presence of a fault. Similarly, one could use the
start of a half cycle of current waveform to initiate a phase comparison among all
thecurrentsconnectedtoabus.Sinceonlythestartofacurrenthalfcycleisusedto
determinethephase relationship,thefact that oneof theCTsmaygo intosaturation
is of no immediate concern. Although such schemes permit successful relaying in
the presence of early CT saturation, the protection provided is not as sensitive as
proper differential relaying – which uses magnitude as well as phase information.
Finally, it should be recalled that a great deal of supervision of bus arrangements
and switching schemes is often a part of bus protection systems. These functions
are far more simple in a computer based bus protection scheme.
6.6 Summary
Inthischapterwehaveexaminedalgorithmsfortheprotectionofdeviceswherethe
percentage differentialcharacteristicisappropriate. In power transformer protection
the fundamental issue is providing a restraining function which is capable of recog-
nizing magnetizing inrush and over-excitation conditions. Algorithms for harmonic
restraint of the transformer differential protection compute harmonics of the current
waveforms. The DFT calculations of the second and fifth harmonic of the restraint
current for each phase can be made practical by proper choice of sampling rate.
Transformer algorithms which use bus voltage measurements are possible in an
integrated substation protection system. Direct use of the bus voltage as a restraint
(restraining if the voltage is high) is possible and produces a potentially faster
algorithm than the harmonic restraint algorithm. The bus voltage measurements

Problems 209
can also be used to determine the slope of the flux-current characteristic of the
transformer. The resulting algorithm is considerably simpler than the Fourier cal-
culations involved in computing harmonics or current and voltage phasors. Finally,
although machine and bus protection are not yet as developed as transmission line
relaying, we have discussed some of the existing relays that have been designed or
are being investigated.
Problems
6.1 The cross-correlation with sinusoids3 techniques computes the n harmonic in
| the following | manner |     |     |     |     |
| ------------- | ------ | --- | --- | --- | --- |
(cid:5)N
1
|     |     | S = | i sin(2π(k−1)n/N) |     |     |
| --- | --- | --- | ----------------- | --- | --- |
|     |     | n   | k                 |     |     |
N
k=1
(cid:5)N
1
|     |     | C = | i cos(2π(k−1)n/N) |     |     |
| --- | --- | --- | ----------------- | --- | --- |
|     |     | n   | k                 |     |     |
N
k=1
(cid:29)
|         |            | I =2     | S2+C2         |                  |     |
| ------- | ---------- | -------- | ------------- | ---------------- | --- |
|         |            | n        | n n           |                  |     |
| Compare | the result | with the | non-recursive | DFT calculation. |     |
6.2 The finite impulse response algorithm4 forms the fundamental and second har-
monic from
|     |     | S =i +i | +i +i        | −i −i −i | −i  |
| --- | --- | ------- | ------------ | -------- | --- |
|     |     | 1 1     | 2 3          | 4 5 6 7  | 8   |
|     |     | C =i +i | −i −i        | −i −i +i | +i  |
|     |     | 1 1     | 2 3          | 4 5 6 7  | 8   |
|     |     | S =i +i | −i −i        | +i +i −i | −i  |
|     |     | 2 1     | 2 3          | 4 5 6 7  | 8   |
|     |     | C =i −i | −i +i        | +i −i −i | +i  |
|     |     | 2 1     | 2 (cid:29) 3 | 4 5 6 7  | 8   |
|     |     | =(π/16) | S2+C2        |          |     |
I n
|     |     |     | n   | n   |     |
| --- | --- | --- | --- | --- | --- |
Compare the results with the Walsh calculations. See Figures 3.4 and 4.12.
6.3 The so called rectangular Fourier transform is defined as
N(cid:5)−1
sign(sin(2πkn/N))
|     |     | S = | i   |     |     |
| --- | --- | --- | --- | --- | --- |
|     |     | n   | k   |     |     |
k=0
N(cid:5)−1
|     |     | C = | i sign(cos(2πkn/N)) |     |     |
| --- | --- | --- | ------------------- | --- | --- |
|     |     | n   | k                   |     |     |
k=0

| 210                |     |              | Protection      | of transformers, | machines | and buses |
| ------------------ | --- | ------------ | --------------- | ---------------- | -------- | --------- |
| If the fundamental |     | and harmonic | terms are       | defined as5      |          |           |
|                    |     |              | −(1/3)S −(1/5)S |                  |          |           |
S =S
|         |                | 1          | 1 3        | 5         |     |     |
| ------- | -------------- | ---------- | ---------- | --------- | --- | --- |
|         |                |            | +(1/3)C    | −(1/5)C   |     |     |
|         |                | C 1 =C     | 1 3        | 5         |     |     |
|         |                | S =S       | ,C = C for | n = 2 & 5 |     |     |
|         |                | n          | n n n      |           |     |     |
| compare | with the Walsh | expansion. |            |           |     |     |
6.4 Find the two columns for Table 6.1 that correspond to the third harmonic.
6.5 Reproduce the development of Equations (6.4) and (6.5) with a winding resis-
| tance r. |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
6.6 Assume a nonlinear magnetization curve for a current transformer. Show
that a percentage differential relay with fixed slope characteristic will either
mis-operate, or be insensitive, depending upon whether the percentage slope
is adjusted to correspond to the unsaturated or saturated portion of the
| magnetization | curve. |     |     |     |     |     |
| ------------- | ------ | --- | --- | --- | --- | --- |
6.7 Assume that a generator is feeding a one per unit load. For an internal ground
fault half-way between the phase a terminal and neutral, determine the amount
of negative sequence power flow at the machine terminals. Assume that the
machine load is entirely passive. What is the negative sequence power flow for
an external fault? What is the reactive power flow for each of these cases? Use
| appropriate | constants | for the | generator. |     |     |     |
| ----------- | --------- | ------- | ---------- | --- | --- | --- |
6.8 Determine the current settings specified in Equations (6.11) and (6.12) for
a current transformer with a turns ratio of 1000:5, and a maximum primary
fault current of 50000 amperes (symmetrical). Will these settings work if the
anti-aliasing filter shown in Figure 1.8(a) is used in the current input channel?
References
[1] Rockefeller, G.D. (1969) Fault protection with digital computer, IEEE Trans. on PAS,
| vol. 88, | no. 4, pp. 438–461. |     |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- | --- |
[2] Sykes, J.A. and Morrison, I.F. (1972) A proposed method of harmonic restraint dif-
ferential protection of transformers by digital computer, IEEE Trans. on PAS, vol. 91,
| no. 3, pp. | 1266–1276. |     |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- | --- |
[3] Malik,O.P., Dash,P.K.,Hope, G.S. (1976) Digitalprotection of a power transformer,
IEEE Publication 76CH1075-1 PWR Paper A76-191-7, IEEE PES Winter Meeting,
| January | 1976, pp. 1–7. |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- |
[4] Larson,R.R.,Flechsig,A.J.,Schweitzer,E.O.(1977)Anefficientinrushcurrentdetec-
tionalgorithmfordigitalrelayprotectionoftransformers,PaperA77-510-1,IEEEPES
| Summer | Meeting, 1977. |     |     |     |     |     |
| ------ | -------------- | --- | --- | --- | --- | --- |

References 211
[5] Rahman M.A. and Dash, P.K. Fast algorithm for digital protection of power trans-
formers (1982) IEE Proceedings – C Generation, Transmission and Distribution, vol.
| 129, Part | C, no. 2, pp. | 79–85. |     |     |     |
| --------- | ------------- | ------ | --- | --- | --- |
[6] Degens, A.J. (1982) Microprocessor-implemented digital filters for inrush detection,
| ElectricalPowerandEnergySystems, |     |     | vol. | 4, no. | 3, pp. 196–205. |
| -------------------------------- | --- | --- | ---- | ------ | --------------- |
[7] Thorp J.S. and Phadke, A.G. (1982) A microprocessor-based three-phase transformer
differential relay, IEEE Trans. on PAS, vol. 102, no. 2, pp. 426–432.
[8] HabibM.andMarin,M.A.(1987)Acomparativeanalysisofdigitalrelayingalgorithms
forthedifferentialprotectionofthree-phasetransformers,PICA,May1987,Montreal,
Canada.
[9] Einvall C.H. and Linders, J.R. (1975) A three-phase differential relay for transformer
| protection, | IEEE Trans. | on PAS, | vol. 94, | no. 6, | pp. 1971–1980. |
| ----------- | ----------- | ------- | -------- | ------ | -------------- |
[10] Harder,E.L.andMarter,W.E.(1948)PrinciplesandpracticesofrelayingintheUnited
| States, AIEE | Transactions, | vol. | 67, Part | II, pp. | 1005–1022. |
| ------------ | ------------- | ---- | -------- | ------- | ---------- |
[11] Thorp J.S. and Phadke, A.G. (1982) A microprocessor based voltage-restrained
three-phasetransformerdifferentialrelay,ProceedingsoftheSouthEasternSymposium
| on Systems | Theory, pp. | 312–316. |     |     |     |
| ---------- | ----------- | -------- | --- | --- | --- |
[12] Sykes,J.A.(1972)Anewtechniqueforhighspeedtransformerfaultprotectionsuitable
for digital computer implementation, IEEE PES Summer Meeting, 1972.
[13] Phadke, A.G. and Thorp, J.S. (1983) A new computer based, flux restrained, current
differential relay for power transformer protection, IEEE Trans. on PAS, vol. 102, no.
11, pp. 3624–3629.
[14] Inagaki, K., Higaki, M., Matsui, Y. etal. (1987) Digital protection method for power
transformers based on an equivalent circuit composed of inverse inductance, IEEE
| PES Summer | Meeting, | San Francisco, |     | July 1987. |     |
| ---------- | -------- | -------------- | --- | ---------- | --- |
[15] Giuliante, T. and Clough, G. (1991) Advances in the design of differential protection
for power transformers, Georgia Tech Protective Relaying Conference, Atlanta, GA,
pp. 1–12.
[16] Sachdev, M.S. Computer Relaying, IEEE Tutorial, Special Publication no. 79
| EH0148-7- | PWR, 1979, | Chapter | 6.  |     |     |
| --------- | ---------- | ------- | --- | --- | --- |
[17] Dash,P.K.,MalikO.P.andHope,G.S.(1977)Fastgeneratorprotectionagainstinternal
asymmetrical faults, IEEE Trans. on PAS, vol. PAS-96, no. 5, pp. 1498–1506.
[18] Benmouyal, G. An adaptive sampling interval generator for digital relaying (1989)
| IEEE PowerEngineeringReview, |     |     | vol. | 9, issue | 7, pp. 45–46. |
| ---------------------------- | --- | --- | ---- | -------- | ------------- |
[19] Adamiak, M.G., Dhruba, P.D., Gardell, J., etal. (1993) Performance assessment of a
new digital subsystem for generator protection, Twentieth Annual Western Protective
| Relay Conference, | October | 19–21, | 1993, | Spokane, | Washington. |
| ----------------- | ------- | ------ | ----- | -------- | ----------- |
[20] Concordia, C. (1951) SynchronousMachines,TheoryandPerformance, General Elec-
tric Company.
[21] AppliedProtectiveRelaying (1976) Chapter 7, Westinghouse Electric Corporation.
[22] Zocholl, S.E., Schweitzer III, E.O., and Aliaga-Zegarra, (1984) A. Thermal protection
of induction motors enhanced by interactive electrical and thermal methods, Trans. of
| IEEE on | PAS, vol. PAS-103, |     | no. 7, pp. | 1749–1755. |     |
| ------- | ------------------ | --- | ---------- | ---------- | --- |
[23] Zocholl,S.E.Determiningrelaysettingsforinductionmotorstatorandrotorprotection
usingthermalmodels(1987)ConferenceonComputerRelaying,Blacksburg,Virginia.

| 212 |     | Protection | of  | transformers, machines | and buses |
| --- | --- | ---------- | --- | ---------------------- | --------- |
[24] CoryB.J.andMoont,J.F.Applicationofdigitalcomputerstobusbarprotection(1970)
IEE Conference on the Application of Computers to Power System Protection and
| Metering, Bournemouth, | England, | pp. 201–209. |     |     |     |
| ---------------------- | -------- | ------------ | --- | --- | --- |
[25] Microprocessor Relays and Protection Systems, IEEE Tutorial Course, Special Publi-
cation 88EH0269-1-PWR, Winter Power Meeting of the PES, 1988.
[26] Udren E.A. and Sackin, M. Relaying features of an integrated microprocessor-based
substation control and protection system (1980) IEE Conference Publication 185,
| DevelopmentsinPowerSystemProtection, |     |     | London, | pp. 88–92. |     |
| ------------------------------------ | --- | --- | ------- | ---------- | --- |
[27] Udren, E.A. (1985) An integrated, microprocessor based system for relaying and
control of substations: Design features and testing program, 12th Annual Western
| Protective Relaying | Conference, | Spokane, | Washington. |     |     |
| ------------------- | ----------- | -------- | ----------- | --- | --- |

7
Hardware organization
in integrated systems
7.1 The nature of hardware issues
In Chapter 1, we discussed several hardware related questions – such as the com-
puter hierarchy in the substation, subsystems of a computer relay, and the analog
to digital converters. In this chapter, we will explore in greater detail some of the
characteristics, environment, and maintenance issues of computer relays which are
crucial to the success of field installations of these devices.
The computing power of microprocessors has been increasing steadily and dra-
maticallyoverthepastseveralyears.Itisthereforenotparticularlyusefultodescribe
and lock-in on the computer hardware capabilities of devices used in relaying at
present. On the other hand, one needs to be aware of some considerations which
stem from functional needs of relaying, and from relaying application considera-
tions it is possible to specify the hardware needs. One could view such a discussion
as pointing to the minimum acceptable capability required for satisfactory relaying
programs – anditfollowsthat,ascomputersgetbetter,theywillmeettherelaytask
requirements with even greater margins of computational capacity. We will make
an attempt to arrive at a description of the minimum hardware capability needed
for computer relays.
The three-level hierarchy of computers within the substation was shown in
Figure 1.12. Level I computers are the protection computers, and usually are
placed inside the substation control house. It is likely that in the future the
relays may reside outdoors next to the power apparatus. Should this be the case,
the environmental conditions in which the relays are placed would be far more
demanding thantheyareatpresent.LevelIIcomputersarecentraltothesubstation,
and are therefore placed in the control house also. It is extremely important that
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

214 Hardware organization in integrated systems
the physical environment inside the control house be carefully defined, so that both
the designers of the relay equipment on the one hand, and designers of substations
and control houses on the other, produce installations in which the capability of
the relays is matched to the conditions that exist inside the control house. We will
describe the station environment and quantitative specifications that have been
used for computer relays.
A somewhat different issue is that of hardware reliability through redundancy.
Wewillexaminethetraditionalpracticeofachievingdependabilitythroughduplica-
tion of hardware. However, other avenues for achieving greater dependability (and
perhaps security) are available with computer relays. We will consider these issues
later in this chapter.
Finally, we will discuss the question of servicing and maintaining the computer
based protection system, and training of station personnel in this new field.
7.2 Computers for relaying
We will now discuss considerations that affect and set limits for acceptable per-
formance for computers to be used for relaying. It has been recognized for some
time that impedance relaying remains an important technique for power system
protection, and furthermore it encompasses the most computationally demanding
algorithms. We will therefore use distance relaying considerations in order to arrive
at computational needs.
We begin with the basic feature of a distance relay which affects all aspects of
computer relays – the speed of response. It has been shown that the speed of a
distance relay is limited by the transient phenomena that accompany a fault, and
that considering the entire fault clearing process, it is not significantly beneficial at
presenttoachieverelayspeedsfasterthanaquarteroftheperiodofthefundamental
powerfrequency.1 Thusthefastestdesirablespeedofarelayresponsemaybetaken
tobebetweenfourandfivemilliseconds(dependinguponwhetherthepowersystem
is operated at 60Hz or 50Hz). To make a secure decision for relaying over this
period, more than two data samples are needed. Thus we reach the conclusion that
the analog input sampling frequency should be at least 12 times the fundamental
frequency of the analog input signals with a sampling interval of the order of
1.4 milliseconds. Since the relaying algorithms must execute between samples,
it is not advantageous to increase the sampling rate to double or triple (i.e. to
1440 or 2160Hz) this rate, as the algorithm execution time would then be reduced
to 0.7 or 0.5 milliseconds respectively. As most relaying algorithms seem to be
accommodated by a couple of thousand machine language instructions, a sampling
period of 0.5 millisecond would call for an average instruction time of the order of
250 nanoseconds. In fact such an algorithm would not leave any margin of safety,
and a more realistic average instruction time needed for a sampling rate of 2160Hz
would be 100 nanoseconds.

Computers for relaying 215
One could thus arrive at the conclusion that, with computers having an average
instruction time of 100 to 300 nanoseconds, satisfactory relaying algorithms could
be built around sampling frequencies of between 36 times and 12 times the power
system frequency. As computer capabilities increase in the coming years, sampling
rate used in relaying tasks is also likely to increase.
Perhapsweshouldrecallthat,inanintegratedcomputer system,thesampleddata
may also be used for oscillography. In such cases, it may be desirable to sample at
much higher rates to reproduce the higher frequency transients. If higher sampling
rates are used in the data acquisition units (see Figure 1.11), the sampled data must
be converted to lower frequency samples before relaying algorithms are invoked.
The data reduction must also simulate correct anti-aliasing filters that would go
with the lower sampling rate.
Having discussed the desirable instruction execution time for the computer and
the corresponding sampling rate, we will next consider the computer word length.
It is clear that 16 bit microcomputers are commonplace now, and 32 bit computers
are becoming available. The 16 bit computation goes well with the 12 bit A/D con-
verters currently in use. If we consider a typical computation involved in a relaying
algorithm (for example, the phasor calculations as in Chapter 3), we construct sums
of the type
(cid:5)N
X = a x
k k
k=1
The numbers a being sines or cosines of sampling angles are at most 1.0; thus the
k
accumulated sum X ≤ Nx . In the worst case, a set of 12 samples (for a complete
k
cycle of data) with x obtained from a 12 bit A/D converter would produce X
k
no greater than a 16 bit number. Of course, in reality, the Fourier sum calls for a
√
normalizingfactorof 2/N,butthisisgenerallyomittedintheinterestofeconomy
of computation.
IftheA/Dconverterisa16bitconverter,atleast20bitswillbeneededtocontain
the phasor, or a scaling procedure will be needed. However, scaling down would
throwawaysomeoftheprecisiondeliveredbythe16bitconverter.Consequently,a
16bitA/Dconverterwouldworkwellwitha32bitcomputertoproduceaprecision
in computation commensurate with the A/D system.
There is some evidence that a 32 bit computer and a 16 bit A/D converter would
be very desirable in order to meet the needs of a distance relay which must cope
with high currents for near faults, yet for some of the backup functions (or fault
detection functions) be responsive to very small fault currents. This is the issue of
dynamic range of the currents (and, to a lesser extent, of voltages) for which the
relay is responsible. As explained in Section 1.5, the 12 bit A/D converter resolves
1 part in 2048. If the largest possible current is scaled to produce a digital value of
2048 when it is fully offset, the corresponding current without a DC offset would
produceadigitalvalueofabout half,or1024. Ifwemaysetanacceptableerrordue

216 Hardware organization in integrated systems
toquantizationofnomorethan1%,thenthesmallestcurrentthatcouldbemeasured
with this accuracy would have a peak of about 50, since the quantization error is
equal to half the least significant bit – or 1/2. Thus, the 12 bit A/D converter may
respond to a dynamic current range of (50:1024) or about (1:20) and still produce
accurate digital values of current samples to within 1% of their peak value. This
dynamicrangeisnotquitesufficientinmanysituations.Inseveralrelaylocations,it
isdesirablethattherelaymeasurecurrentswithdynamicrangesofupto1:200.This
requirement can be met with an A/D converter with 14 bit resolution; and certainly
a16bitconverterwouldproduceadequateaccuracyoveradynamicrangeof1:800.
With such a system, even light load currents as well as maximum fault currents
could be read with high accuracy. It should be noted that 16 bit delta-sigma A/D
converters are becoming quite common, and are in use in some of the currently
manufactured relays.
Computer instruction execution time, word length, and A/D converter resolution
are the main features which influence the quality of measurement performed by
a relay. Other features which make for good overall performance are immunity to
interference,lowpowerconsumption(twofeaturesthatareatoddswitheachother),
adequate peripheral equipment, and assured supply of spare parts. Anticipating the
future availability of high speed direct digital transducer (CT and VT) outputs, the
computer should also be able to acquire these samples without significant software
overhead.
7.3 The substation environment
Physical conditions within an electric utility transmission substation are among the
most severe that can be imagined. In the outdoor station yard, the temperatures can
become very high: 120◦F (49◦C) in very hot regions of the world during summer,
and very cold: 60◦F (−51◦C) incold climatesduring thewinter.At agiven site, the
annual variation of the temperature may be 150◦F (65◦C), and within one day the
temperatures may change by 70◦F. The control house is usually a covered building
withfans and heaters, and issometimes air-conditioned. Although some substations
maybemannedofficetypebuildings,mostofthetimetheyareunmannedenclosures
made of corrugated steel sheets.
Inadditiontotheextremesoftemperatureandhumiditythatthesubstationequip-
ment must withstand, there is also a hostile electromagnetic environment. When
switching operations take place in the substation yard – especially with discon-
nect switches arcing in air – high levels of electromagnetic fields are set up in the
yard and control house. Faults occurring within the substation or near it also cause
ground currents and ground potential rise which may influence all protection and
controlequipmentwithinthestation.Inaddition,varioushighvoltageapparatusmay
have corona discharges of varying severity depending upon the weather. Further-
more, relay operation within the control house may generate transient fields which
may affect other relays and control equipment. And finally, the relays and other

Industry environmental standards 217
protection and control equipment may be affected by fields produced by hand-held
walkie-talkie type radio communication equipment.
The control house – where most protection equipment is located – generally pro-
vides considerable shielding from radiated interference originating in the substation
switchyard. Careful wiring practices and equipment shielding techniques must be
employed in designing relaying equipment in order to ensure that the equipment
will perform satisfactorily under all reasonable service conditions. The substation
designer and the protection designer use industry standards to arrive at environ-
mental specifications which are not exceeded inside the control house, and are
exceeded by the immunity built into the relays. Each country has an appropriate
standard to follow. Basically these standards specify a level for conducted Elec-
tromagnetic Interference (EMI), and some guides for temperature, humidity and
radiated interference. More recently, attention is being given to the Electromag-
netic Pulse (EMP) fields produced by nuclear warheads, but no standards exist as
yet for the EMP fields. We will discuss a few of the relevant standards and guides
in the next section.
7.4 Industry environmental standards
Anindustrystandardprovidesoperatingtemperatureandhumidityspecificationsfor
supervisory control, data acquisition and substation automatic control equipment.2
Althoughlaterrevisionsofthisstandardhaveindicatedthatthesespecificationsmay
not apply to protective relays, we could use the standard as a typical environmen-
tal specification document. For buildings without air-conditioning, the applicable
temperature range is 0◦C to 55◦C with an allowable rate of temperature change of
20◦C per hour. The humidity range is specified to be 10–95% without condensa-
tion. For outdoor equipment (for example in the substation yard), the applicable
temperature range is −25◦C to 60◦C. The 1974 ANSI/IEEE standard C37.90a for
relaying equipment specifies the permissible ambient air temperature close to the
relays to be −20◦C to 55◦C.3 A computer relaying system built for service in the
field has used a temperature specification of 0◦C to 55◦C.4 Standards for seismic
shock withstand are defined by another standard.5
Thecontrolhousewithinasubstationprovidessubstantialshieldingfromradiated
EMI. The wiring from the switchyard to the control house penetrates this shield,
and consequently the EMI induced in this wiring and conducted to the protection
equipmentremainsamajorsourceofconcern.TheANSI/IEEEstandardC37.90aof
1974 and its revision6 provide the standard for Surge Withstand Capability (SWC)
to be built into protective equipment.
Consider the relay system shown schematically in Figure 7.1. Its connections
to the outside world are through the four groups of circuits shown: analog inputs
(voltages and currents), digital inputs (through which external contact or switch
status is communicated to the relay), digital outputs, and power supply. EMI can
reachtherelaythroughanyofthesewires.Consequently,aspecificationisprovided

218 Hardware organization in integrated systems
Input Current Output
Circuits Circuits
Relay
System
Input Voltage Signal
Circuits Circuits
Station Other Power
Battery Supply(if used)
Figure 7.1 Relay input-output definition for Surge Withstand Capability test
for EMI level at the terminals where these wires enter the relay system. The EMI
may be transverse (differential mode), or longitudinal (common mode). These two
termsrefertointerferencevoltagesbetweenanypairofwires(transversemode)and
all wires and ground (common mode). The specifications are for a group of wires
at a time while the relay is operating normally. Thus, while the relay inputs and
outputs are connected normally, one group of wires (for example the current input
leads) is subjected to the SWC test. A typical set-up for these tests is as shown in
Figure 7.2. The surges are coupled through capacitors, and they are restricted to the
relay under test by blocking inductors in series with each wire.
The standard SWC test consists of two parts: (1) the oscillatory SWC test, and
(2) the fast transient test. The oscillatory test attempts to duplicate the EMI induced
in the wiring due to the switching operations or faults within the substation. It is
defined as an oscillatory wave at the terminals of the SWC generator in the fre-
quencyrangeof1.0MHzto1.5MHz,withthefirstpeakvalueof2.5to3.0kVcrest,
and the envelope decaying to 50% of the first peak in not less than 6 microseconds.
The source impedance of the test source (accounting for the energy in the wave)
should be in the range of 150–200Ohms. Further, the test wave is to be applied at
a rate of at least 50 applications per second for a minimum duration of 2.0 seconds.
ThesespecificationsareillustratedinFigure7.3.Thetestfrequency,energycontent,
Isolating
Reactors
Relay
Under
Test
Relay
Under
Coupling
Test
Capacitors
Test
Generator
(a) (b)
Figure 7.2 Transverse and longitudinal SWC testing of relay current input circuits.
(a) Transverse mode. (b) Longitudinal mode

Industry environmental standards 219
2.5–3.0 kV
V
50%
t
greater than
6µsec
repetition rate ≥ 50 per second
Total test duration: 2 seconds
Figure 7.3 The oscillatory SWC test specification
repetition rate etc. for the oscillatory SWC test have been arrived at after reviewing
a number of field observations in HV and EHV
substations.4,6
The fast transient SWC test has been added because it was found that these types
ofsurgesareintroducedintherelaywiringwheneverlowcurrentsinauxiliaryrelay
coils within the control house are interrupted. The contacts used for interrupting the
current may restrike repeatedly, causing a compound transient of several restrikes
and interruptions to occur until the coil current is finally extinguished. These tran-
sients have been proven to be particularly destructive in solid-state relays of early
designs. These phenomena are equally significant in determining the capability of
the computer relays.
The fast transient SWC test wave is unidirectional. Its rise time – defined to be
the time required to reach from 10% of its peak to 90% of its peak value – should
be 10 nanoseconds or less. The crest duration should remain above 90% of its peak
for at least 50 nanoseconds; and the decay time to 50% of its peak value should
be between 100 and 200 nanoseconds. The crest value of the voltage should be
between 4kV and 5kV. The source impedance of the test wave generator should
be80Ohmsor less. Thesepulsesshould be appliedat least 50timesper second, for
a test duration of at least two seconds. The polarity of the test wave should be both
positive and negative. The fast transient waveform specifications are illustrated in
Figure 7.4.
Note that both the oscillatory and unidirectional test wave specifications apply
to the waveform generator terminals under open circuit conditions. During the test
itself, these voltage magnitudes and decay rates will be affected by the relay equip-
ment under test.
It is also intended that the relay input quantities (power frequency voltages and
currents)duringtheSWCtestbeadjustedtovalueswhichputtherelayontheverge
of operation. It is required that the relay not change its status during the SWC tests.
It is of course understood that no permanent damage to the relay should occur as a
consequence of the SWC tests.

220 Hardware organization in integrated systems
V 100−200 nsec
1.0
0.5
t
<10 nsec
>50 nsec
• 50 times per second
• Total duration 2 seconds
Figure7.4 FasttransientSWCtestwaveform.Thiswaveformapproximatesthetransients
generated by switching an inductive circuit powered by the station battery in the control
house and repeated arcing of the interrupting contact
In addition to the ANSI/IEEE test described above, there are other standards
fromtheInternationalElectrotechnicalCommission(IEC)7andtheBritishElectrical
and Allied Manufacturers’ Association (BEAMA),8 and in some cases from large
ElectricUtilitycompanies.Ingeneral,thepeakvoltagesspecifiedbythesestandards
rangebetween1.5kVand6kV.Thetestgeneratorsourceimpedancevariesbetween
50ohms and 500ohms, and the test frequency ranges between 0.10 and 2MHz.
In addition to the conducted EMI standard provided by the SWC tests, radiated
interference9 and Electromagnetic Pulse phenomena10 should also be taken into
consideration.
As mentioned earlier, the various specifications and standards for environmental
conditions serve two functions: to help design a substation which will produce
conditions less severe than those specified by the standard, and to help design
equipment which can withstand conditions that exceed the standards. Thus the
standardsprovideacommon,welldefinedcompromisepositionforthemanufacturer
and user of the protective equipment. It is of course possible to use conditions
other than those defined by the standard – provided that the manufacturer and user
mutually agree to do so. From time to time, other phenomena and failure modes
of protective equipment may point out unforeseen conditions which may lead to
a modification of the standards. Therefore the environmental standards should be
viewed as dynamic statements about the current understanding of the phenomena
involved. In the context of computer relaying, it has not been considered necessary
to modify the existing standards.
7.5 Countermeasures against EMI
The design of relays – whether computer based or solid-state – must incorporate
SWC filtering on all wires which penetrate the relay enclosure. The SWC filter

Countermeasures against EMI 221
must reduce the transient surges defined by the SWC standard to acceptable levels
within the relay. One such filter was described in Chapter 1. Other filter designs are
possible, and will depend upon the capability of the circuit board where the signals
must be applied. To that extent, each SWC filter is an integral part of the relay
system and is designed to accommodate the specifications of the computer and its
peripheral hardware.
The substation design and wiring must also follow a procedure which will limit
the EMI signals at relay input terminals to a value specified by the SWC standard.
PerhapsthestrongestsourceofEMIinthesubstationisadisconnectswitchwhich
opens a capacitive current (such as a bus section or coupling capacitor device) and
has another capacitance to ground on the source side (again, either a bus section
or capacitive voltage transformer). As the current is interrupted (see Figure 7.5),
the arcing contacts reignite several times – and each time a high frequency high
voltage oscillation is
initiated.11,12
These phenomena produce induced voltages in
the control and signal wiring that connects the CT and CVT windings and circuit
breaker control wiring to the relay located in the control house. It has been found
that shielded wires reduce this coupling significantly.
Bothwiresofasignalshouldbecarriedinsideacommonshield.Theshieldshould
begrounded tothestationgroundmatatbothendsandpreferablyatasmanypoints
along the cable run as
practical.11,13
The signal circuit should be grounded at one
point only, generally inside the control house (see Figure 7.6). In addition, special
attentionshouldbepaidtogroundingofthecapacitivevoltagetransformer.Multiple
low resistance grounding wires should be used to ground the CVT base and thus
lower the surge impedance of the ground connection. The run of the wire trenches
should be as far as possible from the sources of EMI. Similar circuits (current
Secondary
wiring
Figure 7.5 Interruption of a capacitive current by a disconnect switch
Relay Signal
source
Stationground mat
Figure 7.6 Shield grounding on signal and control cables

| 222 |     |     | Hardware organization | in integrated | systems |
| --- | --- | --- | --------------------- | ------------- | ------- |
transformer secondary leads, for example) should be included in the same conduit.
Whereextremenoiseimmunityisdesired,doublyshieldedwiringmaybenecessary.
Shielding should be extended to all wiring that penetrates the control house – low
voltage power supply, auxiliary (i.e. non-relaying) control cables should all be
shielded and grounded carefully, as these wires can also bring EMI inside the
| control house | where it may | do damage. |     |     |     |
| ------------- | ------------ | ---------- | --- | --- | --- |
Surges generated inside the control house – for example by fluorescent lights,
switched inductive currents, etc. should be controlled through appropriate means.
The inductive current interrupters should be protected by capacitors or by metal
| oxide varistors   | of adequate | current handling | capability. |     |     |
| ----------------- | ----------- | ---------------- | ----------- | --- | --- |
| 7.6 Supplementary |             | equipment        |             |     |     |
For the sake of completeness, we now enumerate other equipment which, although
essential to the computer relaying functions, is no different from equipment needed
inconventional relayingsystems.Acomputer basedprotectionsystemmustinclude
this supplementary equipment, and some features of the relay architecture may be
| affected by | such equipment. |     |     |     |     |
| ----------- | --------------- | --- | --- | --- | --- |
| 7.6.1 Power | supply          |     |     |     |     |
The station service for protection is generally 125V DC supplied from station
battery. The battery is continuously charged by a charger of adequate capacity
connected to the AC station power supply. Occasionally other battery voltages such
as 48V or 250V may be encountered. A computer relay would require DC to
DC power converters to bring this battery voltage down to the usual computer
requirements of 5V DC and ±15V dc. With sufficient computer equipment within
a substation, it may become practical to furnish a battery system which supplies the
| computers       | directly through | their own | chargers. |     |     |
| --------------- | ---------------- | --------- | --------- | --- | --- |
| 7.6.2 Auxiliary | relays           |           |           |     |     |
These are electromechanical or solid-state isolating relays which provide multiple
closing and opening contacts which may be used for signaling and tripping duties.
| 7.6.3 Test | switches |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- |
At the time of commissioning a relay, and later during its periodic testing and cal-
ibration, the relay outputs must be isolated from the breaker trip coils, and at the
sametimetherelayinputsmust bedisconnected fromthecurrent andvoltage trans-
formers. This arrangement is shown schematically in Figure 7.7. In conventional
relays the test switch is a single device with multiple switching contactors which
control all connections to the relay in one operation. In the case of current trans-
former inputs, the secondary windings of the CT must not be open circuited; hence

| Redundancy | and backup |     |     | 223 |
| ---------- | ---------- | --- | --- | --- |
Station yard
|     |     | Inputs | Outputs |     |
| --- | --- | ------ | ------- | --- |
|     |     | {      | {       |     |
Relay
|     |     | {   | {   |     |
| --- | --- | --- | --- | --- |
Test Equipment
Figure 7.7 Relay test switches isolate the relay from the power system
those contacts must be shorted before the relay is isolated. Similarly, the breaker
trip coil and signaling circuits must be left in a secure quiescent state as the relay is
removed from service. This is usually accomplished by designing the test switch to
provide appropriate make-before-break and break-before-make contacts as needed.
| 7.6.4 | Interface panel |     |     |     |
| ----- | --------------- | --- | --- | --- |
A traditional relay panel consists of control switches, adjustment knobs, visual
indicatorsfor various settings, and alarmtargets.Allpresent dayoperator interfaces
have a mechanical aspect so that a control action has an associated tactile feeling.
The operator gets a sensation of having changed something physically, and he
is immediately rewarded by a mechanical display confirming the change he has
introduced. Although mechanical linkages may break, dial lights may burn out, and
atargetmayfallerroneously,thistypeofpanelistraditional,andallrelayengineers
| and field | personnel are | fond of such interface | panels. |     |
| --------- | ------------- | ---------------------- | ------- | --- |
On the other hand, a computer based relay can accommodate all required opera-
tionsandresponsesthroughanoperator’svideoconsoleandkeyboard.Certainly,for
such a ‘panel’, a serial port to which a console can be connected is all that needs to
be available on the relay front panel. In the present state-of-the-art some type of an
interface panel which emulates the present relay panels is being incorporated in all
computerrelaydesigns.Inmostcases,aconsoleportisalsoprovided,andinprinci-
plethisconsolemaybeavailableataremotelocationthroughacommunicationlink.
| 7.7 Redundancy |     | and backup |     |     |
| -------------- | --- | ---------- | --- | --- |
Aredundant protectionsystemprovidesbackupintheeventthatsomemisoperation
in the relaying system leads to a failure within the relay, or in any of its inputs (CT
andCVTsecondarycircuits).Oftenaredundantprotectionusesadifferentprinciple
of protection – for example, a step distance relay may be the redundant system for
a phase comparison system. The redundant system would guard against the failure
| to trip, | making the overall | protection more | dependable. |     |
| -------- | ------------------ | --------------- | ----------- | --- |

224 Hardware organization in integrated systems
In a computer relaying system, one could duplicate the two different relaying
principles within the same hardware. One would thus be providing for dependable
operation if one of the principles of protection were invalid for certain types of
faults. The need for hardware duplication remains, and therefore in a computer
relaying system as well one must provide for redundancy. However, as it is a com-
puter based system with communication capability, redundancy could be achieved
in many different ways.
One could arrange a single computer relay to serve as duplicate hardware for
all the other computer relays in the substation. Such a computer would have all
the inputs and outputs brought to it, and would, upon notification of a need to
back up a given relay, begin processing the inputs and outputs of that relay under
program control. This arrangement is shown in Figure 7.8. It should be clear that
the redundant relay in this scheme cannot be as fast as the front-line relay, as it
must be alerted to switch its mode of operation to that of the relay in question. The
delays involved need be no longer than a quarter-cycle of the fundamental power
frequency.
If the input-output systems are computer based, the connections to the relaying
processors are over a communication channel. A data highway type of connection
is then possible, although from the point of view of common mode failure, such an
arrangement may not be satisfactory. Furthermore, data transmission from all the
input-output systems situated in the substation to all the relaying processors in the
control house would require excessive rates of data transfer. A radial connection
from one input-output system to all the designated protection computers would
be less demanding of the channel speed (see Figure 7.9). One could provide for
the failure of the input-output system computers by duplicating them, although the
failure of the current transformer or voltage transformer secondary circuits would
disable both input-output systems. One could of course visualize duplication of
transducer secondary windings as well.
Another method of backup of the input-output system is possible in a computer
based system. One could use the analog data acquired by another computer relay
Substation
Host
Backup
Relay Relay Relay
I/O I/O I/O
Figure 7.8 A single redundant relay acts as a backup for computer relays in a substation.
The backup relay assignment is made by the host computer

| Servicing, training | and maintenance |     | 225 |
| ------------------- | --------------- | --- | --- |
. . . . . .
|     | Relay Relay | Relay Relay |     |
| --- | ----------- | ----------- | --- |
. . . . . .
|     | I/O I/O | I/O I/O |     |
| --- | ------- | ------- | --- |
(a) (b)
Figure 7.9 Connections between input-output systems and the protection computer.
| (a) Data highway. | (b) Radial connections |     |     |
| ----------------- | ---------------------- | --- | --- |
Substation
Host
Relay 1 Relay 2 Relay 3
I/O I/O I/O
X
Failure
Figure 7.10 Backup for failed analog input system through processor–processor links
to substitute for a failed analog input system. As shown in Figure 7.10, when the
input system of relay 2 fails, it could substitute for the missing data by using
information from relays 1 and 3. Thus, a missing voltage could be obtained if
voltages seen by relays 1 or 3 were electrically the same as those seen by relay 2.
MissingcurrentscouldbereconstructedbyinvokingKirchhoff’scurrentlawaround
| a power system | bus. |     |     |
| -------------- | ---- | --- | --- |
In summary, a computer based protection system offers many alternative ways
of providing hardware duplication. Duplication of hardware is still necessary –
processors as well as transducers must be duplicated – but for a given duplicated
hardware, far more flexibility in back up is achievable in a computer based system.
Functional backup, whether remote or local, can be achieved within the same
hardware by programming the appropriate functional algorithms.
| 7.8 Servicing, | training and | maintenance |     |
| -------------- | ------------ | ----------- | --- |
We include this section as a reminder that with computer relaying come a host
of other issues which must be addressed before these new systems can become

226 Hardware organization in integrated systems
acceptable field grade equipment. Certainly the most troublesome is the question
of maintainability of this equipment for many years after it is installed. It is well
known that traditional (i.e. conventional) electromechanical or solid-state relays
have a service life of 10–20 years, and in some cases 40 year old relays are still
in service. It does not seem likely that computer based relays can be (or should be)
maintained so long. It is a fact that the computer hardware technology advances
too rapidly: a five-year-old hardware chip is usually an obsolete one. It is no longer
available in the marketplace – neither should it be, because it has been replaced by
a superior product. In the face of this rapidly changing technology, the computer
based relay is unlikely to be a device with a 40 year life span. A standard computer
back-plane, into which a succession of compatible boards may be plugged in the
future, looks like a reasonable alternative. In any case, substantial rejuvenation
programs for computer based relays and integrated systems look like a concomitant
of this technology.
Maintenance of computer relays should be a simpler proposition. With
self-diagnostic capability of computer based devices, the defective sub-assemblies
should be identifiable. The replacement procedure could be generated on site,
with detailed, step-by-step advice to the maintenance engineer. With a common
hardware implementation for many – or all – substation computers, the spare part
inventory should be small.
The service and field personnel would certainly need training to install, calibrate
and repair these systems. There is a very large community of computer hardware
installers, repairmen, and diagnosticians. No doubt their expertise will be called
upon to train the substation personnel. In any case, although newer training proce-
dures are required, there should be no basic hindrance to this undertaking.
Themostinterestingaspectoftheentiresystemistheretrainingofrelayengineers
and system planners to adapt to this new technology. The relay engineer could
become a designer of relaying functions through the flexible software capability
of a computer relay. The manufacturer could furnish the hardware and a software
shell, in which the user could place a custom-designed application software. The
relays could be altered in the field automatically (as in case of adaptive relays),
or through centrally directed commands. The relays – in the event of an erroneous
operation – could be queried as to what led to the error. Hidden flaws in relay
design logic could thus be uncovered. The sequence of events and oscillography
information could be obtained at a central location within minutes of the event. All
these possibilities come with computer relaying – and relay engineers of the future
must begin to think in terms of these expanded roles for the computer relays.
7.9 Summary
In this chapter, we have dealt with present day hardware suitable for computer
relaying. Microcomputers with 16 bit word length and Analog to Digital Convert-
ers with 12 bit resolution seem to be adequate for all relaying needs. There is

References 227
some indication that the next generation of 32 bit computers and 16 bit ADCs
could lead to noticeable improvement in measurement functions performed by the
computer relays. We have described the available industry environmental standards
for temperature, humidity, seismic shock, and electromagnetic interference which a
computer relay must meet in the substations. We have also described some of the
established methods of combating EMI interference. And, finally, we have given a
general review of reliability and backup as influenced by hardware considerations.
References
[1] Thorp, J. S., Phadke, A. G., Horowitz, S. H. and Beehler, J. E. (1979) Limits to
impedance relaying, IEEE Trans. on PAS, vol. PAS-98, no. 1, pp. 246–260.
[2] IEEE Standard: Definition, Specification, Analysis of System used for Supervisory
Control, Data Acquisition, and Automatic Control, ANSI/IEEE C37.1-1979.
[3] Guide for Surge Withstand Capability (SWC) Tests, ANSI C37.90a-1974, IEEE Stan-
dard 472-1974.
[4] SubstationControlandProtectionProject – SystemRequirementsSpecifications,Elec-
tric Power Research Institute EL-1813, Interim Report, April 1981.
[5] IEEE Standard Seismic Testing of Relays, ANSI/IEEE C37.98- 1984.
[6] IEEE Standard: Surge Withstand Capability (SWC) Tests for Protective Relays and
RelaySystems,P472/D9,C37.90.1-198x.DraftDocumentofthePowerSystemRelay-
ing Committee, June 8, 1987.
[7] Single Input Energizing Quantity Measuring Relays with Dependent Specified Time,
International Electrotechnical Commission, IEC Standard, Publication 255-4, first edi-
tion, 1976.
[8] RecommendedTransientVoltageTestsApplicabletoTransistorizedRelays,TheBritish
ElectricalandAlliedManufacturers’Association(Inc.),Publicationno.219,November
1966.
[9] Withstand Capability of Relay Systems to Radiated Electromagnetic Interference,
ANSI37.90.2,IEEEStandardP734/D2,DraftDocumentofthePowerSystemRelaying
Committee, February 1981.
[10] The Effects of EMP on Protective Relaying Systems, Report by the EMP Working
Group of the Power System Relaying Committee of IEEE, 1986.
[11] Callow, J. A. and Mackley, K. W. Impulsive Overvoltages on Secondary Circuits
of 330kV Capacitor Voltage Transformer, Snowy Mountain Hydroelectric Authority,
CIGRE´ 1962, Report No. 136.
[12] Dietrich, R. E., Ramberg, H. C. and Barber, J. C. (1970) BPA Experience with EMI
measurements and shielding in EHV substations, Proceedings of the American Power
Conference, vol. 32, pp. 1054–1061.
[13] Kotheimer,W.C.(1969)Controlcircuittransients,PowerEngineering,PartI,vol.73,
pp. 42–45, January 1969; Part II, pp. 54–56, February 1969.

8
System relaying and control
8.1 Introduction
Thepresenceinthesubstationofmicroprocessorbaseddevices,whichareconstantly
processingdatareceivedfromthesystem,makesitpossibletoincludetheprotection
system as a part of a system-wide computer hierarchy dedicated to monitoring and
control. A relay can be regarded as a measuring system. As we have seen in the
previouschapters,almostallrelayingalgorithmsbeginwithsamplesofthemeasured
systemvoltagesandcurrents.Inmanycasesphasorvoltagesandcurrentsarecomputed
before relaying decisions are made. While faults occur extremely infrequently, the
phasorcalculationsarebeingperformedconstantly.Becauseoftheredundancybuilt
intotheprotectionsystemitselfandbecauseofthedigitalequipment’sselfdiagnostic
ability,thecomputerrelaybecomesahighlyreliablemeasuringdevice.
Themeasuringfunctionisalogicalcomplementtotheprotectionfunction.Infact,
thetwofunctionscancoexistifproperprioritiesaremaintained.Duringnormalsystem
conditionsthemeasuringfunctionwouldbeactive.Duringfaultconditionsmeasuring
would be suspended (themeasurements are of questionable value during faults) and
themeasurementsusedforrelayingdecisions.Thequestionofmeasurementaccuracy
shouldalsobeconsidered.Innormal(quasi-steadystate)operatingconditionsthefault
inducednon-fundamentalfrequencysignalsdiscussedinChapter5arenotseenbythe
relay.Inaddition,longerwindowalgorithmscanbeusedforthemeasurementfunction,
further reducing the error in the result (in an inverse time way, as in Figure 5.25).
Sincemeasurementsarenotrequiredatthehighraterequiredforrelaying,itispossible
toimaginedatawindowsofcyclesforthemeasurementfunction.Thetwofunctions
arecompatiblesolongassometrigger,suchasthetransientmonitor,isusedtoinitiate
therelayingcalculationsandsuspendthemeasurementfunction.
The fact that the relaying processors are connected through the substation host to
central computers in a fully integrated system is an additional benefit. Monitoring
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

230 System relaying and control
and control functions, both local and central, can have access to measurements
from the relaying processors. It is clear the local breaker control – high speed
reclosing,automaticreclosing,synchronizingchecks,busreconfiguration,etc. – can
be initiated by the host computer on the basis of data received from the protection
processors. Additional control functions would profit from the availability of such
datafromremotesubstations.Forexample,VARcontrolthroughcapacitorswitching
could be based on voltage information from neighboring buses. Bus reconfiguration
could be influenced by the configuration of adjacent buses.
This chapter is concerned with the relaying computer as a measuring device and
the use of those measurements in monitoring and control. The next two sections
describe a technique for extracting additional value from the phasor measurements
produced by the Fourier type algorithms.
8.2 Measurement of frequency and phase
An interesting and useful result can be obtained by examining the SCDFT
(Section 5.5) calculations of the positive sequence voltage for a balanced system
operating at a frequency different than the nominal power system frequency.1 If
we denote the nominal power system frequency and write the phase voltages as
1
v (t) D RefVejωtg D [VejωtCV Ł e(cid:21)jωt]
a
2
1
v (t) D RefVα2ejωtg D [Vα2ejωtCV ŁαŁ2 e(cid:21)jωt] (8.1)
b
2
1
v (t) D RefVαejωtg D [Vαejωt CV ŁαŁe(cid:21)jωt]
c
2
where V is the positive sequence phasor, α is ej2π/3 and ω is different from ω . If
o
we compute the positive sequence voltage with a full cycle window, for example,
corresponding to K samples per full cycle of the nominal frequency, ending at
sample L, from Equations (5.32) and (5.76)
(cid:5)L
V˜(L) D 2 1 [v (k(cid:1)t)Cαv (k(cid:1)t)Cα2v (k(cid:1)t)]e(cid:21)jkω o (cid:1)t (8.2)
1 K 3 a b c
kDL(cid:21)KC1
Using Equation (8.1)
(cid:5)L
V˜(L)
D
1 3Vejωk(cid:1)tejkω
o
(cid:1)t
1 3K
kDL(cid:21)KC1
(cid:5)L
1
C V
Ł(1CααŁ2 Cα2αŁ)e(cid:21)jωk(cid:1)te(cid:21)jkω
o
(cid:1)t
(8.3)
3K
kDL(cid:21)KC1

| Measurement | of frequency  |          | and phase |         |       |     |     |          | 231   |
| ----------- | ------------- | -------- | --------- | ------- | ----- | --- | --- | -------- | ----- |
|             |               |          |           |         |       | ααŁ | D   | (1CαŁCα) | D     |
| The last    | term in       | Equation | (8.3)     | is zero | since |     | 1,  | and      | 0. If |
| we let ω    | D ω C(cid:1)ω |          |           |         |       |     |     |          |       |
o
(cid:5)L
1
|     |     |     | V˜(L) | D   |     | Vejk(cid:1)ω(cid:1)t |     |     |     |
| --- | --- | --- | ----- | --- | --- | -------------------- | --- | --- | --- |
(8.4)
|     |     |     | 1   | K   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
kDL(cid:21)KC1
| The sum | in Equation |     | (8.4) can | be evaluated |          | and      | yields |          |     |
| ------- | ----------- | --- | --------- | ------------ | -------- | -------- | ------ | -------- | --- |
|         |             |     |           | (cid:26)     | (cid:18) | (cid:19) |        | (cid:27) |     |
K(cid:1)ω(cid:1)t
|     | V˜(L) |     | VejL(cid:1)ω(cid:1)t | sin |                  | (cid:19)e(cid:21)j(K(cid:21)1)(cid:1)ω(cid:1)t/2 |     |     |       |
| --- | ----- | --- | -------------------- | --- | ---------------- | ------------------------------------------------ | --- | --- | ----- |
|     |       | D   |                      |     | (cid:18)         | 2                                                |     |     | (8.5) |
|     |       | 1   |                      |     | (cid:1)ω(cid:1)t |                                                  |     |     |       |
Ksin
2
The bracketed term in Equation (8.5) represents an error in computing the pha-
sor caused by the power system operating at a frequency other than the nominal
frequency. It has both a magnitude and an angle. At a sampling rate of 12 samples
per cycle and a nominal power system frequency of 60Hz, the magnitude of the
bracketed term varies from .98869 to 1.0000 as the power system frequency varies
from 55 to 65Hz (a considerable range). The angle of the bracketed term is 2.7
degrees per Hz for the same system. The bracketed term is also unimportant in fre-
quency calculations since it is a constant, i.e. independent of L. For an interesting
discussion of the single phase version of these calculations where the second term
of Equation (8.3) is nonzero, the reader is referred to the discussion and closure of
| Reference | 1.  |     |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The part of Equation (8.5) that depends on the recursion number L is the angle
L(cid:1)ω(cid:1)t.
If we let the phase angle of the phasor computed at time L be denoted by
ψL
then
|     |     |     |     | (cid:5) D (cid:5) | C(cid:1)ω(cid:1)t |     |     |     | (8.6) |
| --- | --- | --- | --- | ----------------- | ----------------- | --- | --- | --- | ----- |
|     |     |     |     | L                 | L(cid:21)1        |     |     |     |       |
and since the time between samples is (cid:1)t seconds, the angular velocity of ψ is
given by
|     |     |     | d(cid:5) | (cid:5) | (cid:21)(cid:5) |            |     |     |       |
| --- | --- | --- | -------- | ------- | --------------- | ---------- | --- | --- | ----- |
|     |     |     |          |         | L               | L(cid:21)1 |     |     |       |
|     |     |     |          | D       |                 | D (cid:1)ω |     |     | (8.7) |
(cid:1)t
dt
In other words, the computed phasor rotates in the complex plane at a rate directly
related to difference between the actual power system frequency and the nominal.
(cid:1)f
With D 1 Hz the phasor rotates counterclockwise in the plane at a rate of one
revolution per second. If (cid:1)f D (cid:21)1 Hz, the rotation is clockwise. The effect is
very similar to a power system synchroscope. It is important to realize that this
calculation is possible because the sampling frequency is fixed at K samples per
| cycle of | the nominal | power | system | frequency. |     |     |     |     |     |
| -------- | ----------- | ----- | ------ | ---------- | --- | --- | --- | --- | --- |
The technique suggested by Equations (8.5) and (8.7) has much to recommend
it for the measurement of frequency and rate of change of frequency. It uses all
three phase voltages and is therefore less sensitive to error terms than techniques
basedonasinglephase. Itusesmuchmoreinformationthanmethodsbasedonzero
crossingtimesandismoreimmunetonoiseandharmonics.Infact,iftheharmonics

| 232 |     |     |     |     | System | relaying | and control |
| --- | --- | --- | --- | --- | ------ | -------- | ----------- |
are multiples of the nominal power system frequency they are completely rejected.
Lastly, the positive sequence voltage is a natural quantity to use in describing the
system. The model for static state estimation (Section 8.4) is, in fact, the positive
| sequence network. |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- |
The implementation of a frequency measurement scheme using these ideas is
relatively simple if it is recognized that it must take longer to measure small
frequency deviations than to measure large deviations. If we wait for the rotat-
ing phasor to sweep out a reasonable angle before computing the frequency, it
is clear that small frequency deviations will take longer and large deviations will
be measured more quickly. A reasonable angle was found to be approximately
| radians.1 |     |     |     |     | (cid:1)f |     |     |
| --------- | --- | --- | --- | --- | -------- | --- | --- |
0.5 The time it would take a phasor rotating at Hz to move through
| 0.5 radians | is  |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
0.5
D
|     |     | T   |     | seconds |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- |
2π(cid:1)f
If we assume that at least four raw measurements must be processed in order
to provide smoothing then the time necessary to obtain a frequency reading for a
| frequency deviation | of (cid:1)f | Hz is |     |     |     |     |     |
| ------------------- | ----------- | ----- | --- | --- | --- | --- | --- |
0.32
|     |     | T   | D   | seconds |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- |
(cid:1)f
Thus a frequency deviation of 0.1Hz would take 3.2 seconds while a 1Hz devi-
ation would take 0.32 seconds. In practice, simple averaging of the raw frequency
measurements was found to be adequate to smooth the estimates.
| 8.2.1 Least | squares | estimation | of  | f and df/dt |     |     |     |
| ----------- | ------- | ---------- | --- | ----------- | --- | --- | --- |
A more formal process for measuring frequency and rate of change of frequency
is to use a least squares estimation based upon certain number of phase angles of
the positive sequence measurements. Assuming that the vector of n phase angle
measurements is [φ] and it is assumed that the phase angle is a quadratic function
of time:
|     |     | φ   |        | t2  |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- |
|     |     |     | D a Ca | tCa |     |     |     |
|     |     |     | 0      | 1 2 |     |     |     |
Ifthephaseanglesareobtainedatintervalsof(cid:1)t,onemaywriteanover-determined
set of equations for solving for the coefficients a 0 , a 1 , and a 2 :
|     |   |    |     |     |    |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
 
|     | φ   | 1   | 0   | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |  φ  |    | (cid:1) | (cid:1) |    | a 0 |     |
| --- | ----- | --- | ------- | ------- | --- | --- | --- |
|     |     |  1 | t       | t2      |   |    |     |
|     | 1     | D   |         |         |     | a   |     |
|     |  Ð  |  Ð | Ð       | Ð       |    | 1   |     |
a
|     | φ   | 1   | (n(cid:21)1)(cid:1)t | (n(cid:21)1)2(cid:1)t2 |     | 2   |     |
| --- | --- | --- | -------------------- | ---------------------- | --- | --- | --- |
n(cid:21)1

Sampling clock synchronization 233
If the coefficient matrix in the above equation is denoted by [T], and the unknown
three-vectorof‘a’coefficientsisdenotedby[A],theleastsquaresestimateof[A]is
[A] D [TtT](cid:21)1Tt[φ]
Having calculated the coefficients, the frequency and rate of change of frequency
can be obtained by direct differentiation of the assumed polynomial expression
for φ:
f D f C(cid:1)f D f C(1/2π)(a C2a t)
0 0 1 2
and
df/dt D (1/2π)(2a )
2
f being the nominal system frequency. If one takes a sufficient number of phase
0
angle samples (for example, over two or three periods of the nominal power system
frequency), the above estimates are found to be very accurate.
The frequency measurement scheme has obvious application in load shedding
relays, for example. It imposes almost no additional computational burden on the
relaying computer and can be regarded as a by-product of the SCDFT calculation.
Coupled with another development (the next section) it forms the basis for the use
of measurements taken from the digital protection system in system wide control
and monitoring.
8.3 Sampling clock synchronization
Ithasbeenmentionedthatinanintegratedsubstationprotectionsystemitisassumed
that all sampling of voltages and currents would be synchronized. This has the
advantageofallowingdatasharingbetweenmodulesinabackupmode,asdiscussed
inSection6.8.Thevoltagesignalsusedintransformerprotectionmight beobtained
from line protection modules in such a system. The sampling clock synchronization
wouldhaveanotheradvantage,viz.allthephasorscomputedinthesubstationwould
be on a common reference. If we examine the recursive form for the DFT calcula-
tions in Equations (5.37) and (5.38), for example, it is clear that, if all the recursive
calculations are begun at the same instant and updated synchronously, the phasors
would all be with respect to the same reference angle. The fact that this reference
angle has no particular physical meaning is unimportant. The angle differences
between any two phasors computed with respect to this reference would be correct.
The obvious extension of these ideas is to synchronize sampling throughout the
system. Synchronizing to an accuracy of 1ms, in order to time-tag data, has been
reported.2 Experiments with common-reference phase angle measurements using
zero-crossing instants and radio receivers tuned to standard time broadcast sys-
tems have also been discussed.3–5 The required accuracy of synchronization can
be determined by observing that at a 60Hz power system frequency a timing error

234 System relaying and control
of 1µ sec. corresponds to an angular error of 0.0216 degrees (at 50Hz it is 0.018
degrees). It would seem that sampling accuracies in the neighborhood of 1 to 10µ
sec would be acceptable for almost all applications. Since the local oscillators that
supervise the timing are inherently very stable (10ppm, or less inaccuracy), an
interval of one second between synchronizations is reasonable.
The other important factors that determine the choice of a synchronizing system
are the cost and uninterrupted operation of the system over a long time span. There
arebasicallytwogroupsofsystems,dependingonthecommunicationmediumused:
satellite and radio broadcasting systems, or fiber optic link based systems. The use
of NAVSTAR satellite system to produce accuracies of a microsecond has been
reported.6 The NAVSTAR-based system has a receiver which is given the latitude,
longitude, and altitude of the substation. The signal received from the satellite is
processed to produce a synch pulse once a second which is accurate to within one
microsecond. The system also provides the time stamp through high speed RS232C
serial links (9600 Baud).
The use of fiber optic links is also an excellent choice if the high cost of imple-
mentation is not an obstacle. A fiber optic network is a good choice when the
hardware is already in the system for some other purpose and the extension of
its use is feasible. It should be noted that a dedicated fiber must be used for the
synchronizing pulse since multiplexing will destroy the time accuracy of the sny-
chronizing pulses. In the fiber system a master clock transmits the synch pulses
with time and reference state information through a fiber optic network to all mea-
suring systems. The fixed communication delays through the fiber system must be
accounted for in the measuring systems. In either system some technique must be
provided to guarantee that there are the correct number of samples between synch
pulses. A phase locked loop is suggested in the reference.6
8.4 Application of phasor measurements to state estimation
Real-time operation of the bulk power system has been greatly enhanced by the
introduction of state estimation algorithms. State estimation algorithms use mea-
surements of available quantities such as: real and reactive power flows, real and
reactive power injections, bus voltage magnitudes, and breaker status to estimate
the state of the system. The state is taken to be the set of bus voltage angles and
magnitudes. The estimated states are used in Energy Control Centers to determine
the appropriateness of operating regimes, including the impact of contingencies,
and to plan and take corrective action. The optimal power
flow,7,8
for example,
assumes that the current state of the system is known from a state estimator. The
transducers that make the measurements used in state estimation are called remote
terminal units (RTUs). The RTUs communicate with the supervisory control and
data acquisition system (SCADA) over dedicated telephone lines and/or microwave
channels.

| Application | of  | phasor measurements |     | to state | estimation |     |     | 235 |
| ----------- | --- | ------------------- | --- | -------- | ---------- | --- | --- | --- |
The commonly accepted state estimation algorithms are a form of the weighted
least squares (WLS) technique of Chapter 3.9 If the state of the system is taken as
θ
the vector V of bus voltage magnitudes, and the vector of bus voltage angles,
| then the | measurement |     | vector, | z, can | be written | as  |     |       |
| -------- | ----------- | --- | ------- | ------ | ---------- | --- | --- | ----- |
|          |             |     |         | zD     | h(V,θ)Cε   |     |     | (8.8) |
ThemeasurementinEquation(8.8)isnonlinear,sincethelineflowsandinjections
are nonlinear functions of the states. For example, the entry in h corresponding to
the measurement of the real power flow on a line connecting bus k to bus m is
given by
|     |     |      | D V2g | (cid:21)V | cosθ | CV  | sinθ     |     |
| --- | --- | ---- | ----- | --------- | ---- | --- | -------- | --- |
|     |     | P km | km    | k         | V m  | km  | k V m km |     |
k
|                           |     |     |     | Cjb   | andθ | D θ  | (cid:21)θ               |     |
| ------------------------- | --- | --- | --- | ----- | ---- | ---- | ----------------------- | --- |
| wherethelineadmittanceisg |     |     |     | jm km |      | km k | m .Theestimatoristermed |     |
static because the entire set of measurements z are assumed to be taken from the
ε,
system in a fixed (static) state. The measurement error vector, is assumed to
be independent from component to component with a diagonal covariance matrix
given by
|         |        |          |         | EfεεTg | DW         |     |     | (8.9) |
| ------- | ------ | -------- | ------- | ------ | ---------- | --- | --- | ----- |
| A model | of the | diagonal | entries | in W   | is given10 | as  |     |       |
w Dσ2
ii
i
|       |     |     | σ         | D(0.02mC0.0052f |     | )/3 |     |     |
| ----- | --- | --- | --------- | --------------- | --- | --- | --- | --- |
|       |     |     |           | i               |     | s   |     |     |
| where |     |     | (cid:29) |                 |     |     |     |     |

|     |     |     | P2          | CQ2 | for flow | measurements |     |     |
| --- | --- | --- | ----------- | --- | -------- | ------------ | --- | --- |
|     |     |     | (cid:29) mk | mk  |          |              |     |     |
mD

|     |     |     | P2CQ2 |     | for injection | measurements |     |     |
| --- | --- | --- | ----- | --- | ------------- | ------------ | --- | --- |
k k
|     |     |     | V k |     | for voltage | measurements |     | (8.10) |
| --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------ |
and
|     |     | f   | D full scale | value | of  | the instrumentation |     |     |
| --- | --- | --- | ------------ | ----- | --- | ------------------- | --- | --- |
s
These error models are appropriate to the early SCADA systems but are inappro-
priate when PMU measurements are considered. The concept of meter calibration
| has been | investigated |     | using PMU | measurements.11–13 |     |     |     |     |
| -------- | ------------ | --- | --------- | ------------------ | --- | --- | --- | --- |
Given any appropriate W the basic algorithm is to minimize the scalar perfor-
mance index
|     |     | J(V,θ) | D   | [z(cid:21)h(V,θ)]TW(cid:21)1[z(cid:21)h(V,θ)] |     |     |     |     |
| --- | --- | ------ | --- | --------------------------------------------- | --- | --- | --- | --- |
(8.11)

| 236 |     |     |     |     | System relaying | and control |
| --- | --- | --- | --- | --- | --------------- | ----------- |
bychoiceofVandθ(refertoSection3.7andequation(3.77)).SinceEquation(8.11)
isnonlinear it must besolved recursively. Oneapproach istomake a linear approx-
|            | h(V,θ) | kth           |        |         |         |     |
| ---------- | ------ | ------------- | ------ | ------- | ------- | --- |
| imation to | at     | the iteration | in the | form    |         |     |
|            |        |               |        | (cid:2) | (cid:3) |     |
V(cid:21)Vk
|     |     | h(V,θ) | D h(Vk,θk)CH |     |     |     |
| --- | --- | ------ | ------------ | --- | --- | --- |
θ(cid:21)θk
where H is a matrix of first partial derivatives of the components of h with respect
to the components of V and θ evaluated at Vk and θk, and the superscript k stands
kth
| for the value | at the | iteration. | If we write    |     |     |     |
| ------------- | ------ | ---------- | -------------- | --- | --- | --- |
|               |        |            | ∆V V(cid:21)Vk |     |     |     |
D
|     |     |     | ∆θ D θ(cid:21)θk |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | --- |
(8.12)
|     |     |     | ∆z D z(cid:21)h(Vk,θk) |     |     |     |
| --- | --- | --- | ---------------------- | --- | --- | --- |
then the solution for (cid:1)V and (cid:1)θ can be obtained from Equation (3.77), viz.
|     |     |     | (cid:2) | (cid:3) |     |     |
| --- | --- | --- | ------- | ------- | --- | --- |
∆V
|     |     | (HTW(cid:21)1H) |     | HTW(cid:21)1∆z |     |        |
| --- | --- | --------------- | --- | -------------- | --- | ------ |
|     |     |                 |     | D              |     | (8.13) |
∆θ
The gain matrix G D (HTW(cid:21)1H) is not inverted as it was in Equation (3.77)
because Equation (8.13) represents a large sparse set of equations. Equation (8.13)
willbesolvedusingsparsematrixtechniques(factoringthematrixG).Sincethegain
matrix,G,wouldhavetobeformedandfactoredateachstep,approximationswhich
use a constant and decoupled form of the gain matrix are used. The decoupling is
achievedbyorderingthemeasurementsintorealandreactivepartsintheform
|     |     |     | (cid:2) | (cid:3) |     |     |
| --- | --- | --- | ------- | ------- | --- | --- |
z
|     |     |     | z D | A   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
z
R
where
(cid:2) (cid:3)
P
|     |     | km  | Active | Flow Measurements |     |        |
| --- | --- | --- | ------ | ----------------- | --- | ------ |
|     | z   | D   |        |                   |     | (8.14) |
|     |     | A P | Active | Injections        |     |        |
k
and
 
|     |     | Q   | Reactive | Flow Measurements |     |     |
| --- | --- | --- | -------- | ----------------- | --- | --- |
km
 
|     | z   | D Q | Reactive | Injections |     | (8.15) |
| --- | --- | --- | -------- | ---------- | --- | ------ |
|     | R   | k   |          |            |     |        |
|     |     | V   | Voltage  | Magnitudes |     |        |
k
| so that Equation | (8.13) | becomes |                |                 |         |     |
| ---------------- | ------ | ------- | -------------- | --------------- | ------- | --- |
|                  |        | (cid:2) | (cid:3)(cid:2) | (cid:3) (cid:2) | (cid:3) |     |
|                  |        |         | ∆V             | ∆z              |         |     |
G 0
|     |     | AA  |      | D   | A   | (8.16) |
| --- | --- | --- | ---- | --- | --- | ------ |
|     |     | 0   | G ∆θ | ∆z  |     |        |
|     |     |     | RR   |     | R   |        |

| Application | of phasor measurements |     | to state estimation | 237 |
| ----------- | ---------------------- | --- | ------------------- | --- |
D θ D
The gain matrix is typically computed for V 1, and 0. A variety of other
| simplifying | assumptions | can also | be employed.9 |     |
| ----------- | ----------- | -------- | ------------- | --- |
One of the more important functions of a state estimator is to reject bad data.
The techniques employed involve the use of J(V,θ) and the individual residuals
solution.14,15
(cid:1)z evaluated at the It is clear that if the error terms are as described
i
by Equation (8.9) then the residuals must have a specific statistical description. If
theresidualsarenormalizedbytheirappropriatestandarddeviations,thenstatistical
tests can be used to determine whether some residuals are suspiciously high. If the
estimationisrepeatedwiththesesuspectmeasurementsremoved,andtheremaining
residuals are acceptable, then the bad data has been identified.
Typically, only a portion of the transmission network (the HV system with volt-
agesgreaterthan132kV)aremonitored.Whileitisdesirablefromasystemsecurity
point of view to estimate the state of the subtransmission system, extending the
estimatortolowervoltageswouldsignificantlyincreasethecomputationalandcom-
munication burden. The use of the measurements made by digital relaying devices
with synchronized sampling clocks has been suggested as a technique of extending
the estimator.16–18
| 8.4.1 | WLS estimator | involving | angle measurements |     |
| ----- | ------------- | --------- | ------------------ | --- |
A first possibility is to include the angle measurements directly in the WLS
algorithm.16 If some voltage angles are included the measurement vector can be
| modified | to  |     | (cid:2) (cid:3) |     |
| -------- | --- | --- | --------------- | --- |
z
z D A
z
R
where
 
|     |     | P   | Active Flow Measurements |     |
| --- | --- | --- | ------------------------ | --- |
km
 
|     | z   | D P | Active Injections | (8.17) |
| --- | --- | --- | ----------------- | ------ |
|     | A   | k   |                   |        |
θ
|     |     | k   | Direct Angle Measurements |     |
| --- | --- | --- | ------------------------- | --- |
and
 
|     |     | Q   | Reactive Flow Measurements |     |
| --- | --- | --- | -------------------------- | --- |
 km 
|     | z D | Q   | Reactive Injections | (8.18) |
| --- | --- | --- | ------------------- | ------ |
|     | R   | k   |                     |        |
|     |     | V   | Voltage Magnitudes  |        |
k
Theadditionoftheanglemeasurementstotheactivemeasurementshascreatedan
obvious symmetry to the measurement set, with the angles in active measurements
playing the same role as the voltage magnitudes in the reactive measurements. The
concept of including the angle measurements is not a new idea (see the discus-
sion of the reference17) but is not practical without the synchronized sampling of
the digital relays. The modifications to the WLS algorithm is quite simple. The

| 238 |     |     |     |     |     | System relaying | and control |
| --- | --- | --- | --- | --- | --- | --------------- | ----------- |
performance of the estimator on the IEEE 118 bus system for different numbers of
angle measurements of different qualities has been reported.16
There is an issue in dealing with the reference angle of the phasor measure-
ments (see the discussion and closure of the reference16). In the conventional WLS
algorithm one of the buses is chosen as the reference. The WLS estimates of the
bus voltage angles are with respect to this chosen reference. With synchronized
sampling the direct angle measurements are all with respect to a different (and
non-physical) reference which is determined by the instant sampling is initiated. If
the direct angle measurements are used without dealing with the reference problem
unreasonable results are to be expected. One possible solution is to install a phase
measuring device at the reference of the WLS system. The angle measured at the
reference then should be subtracted from all the other direct angle measurements.
There is a limitation involved in this solution since a failure of this single measure-
ment would make all the direct measurements useless. We will return to the issue
of a common reference after considering a second estimation technique using direct
phasor measurements.
| 8.4.2 Linear | state | estimator |     |     |     |     |     |
| ------------ | ----- | --------- | --- | --- | --- | --- | --- |
A more striking change in the state estimator is produced if only phasor measure-
set.17
ments are included in the measurements If we assume that real-time phasor
measurements are made of all positive sequence bus voltages and some positive
sequence currents in transmission lines and transformers, then the measurement
| vector is given | by  |     | (cid:2) | (cid:3) (cid:2) | (cid:3) |     |     |
| --------------- | --- | --- | ------- | --------------- | ------- | --- | --- |
ε
|     |     |     | V   | B   | B   |     |        |
| --- | --- | --- | --- | --- | --- | --- | ------ |
|     |     |     | z D | C   |     |     | (8.19) |
|     |     |     | I   |     | ε   |     |        |
|     |     |     | L   |     | L   |     |        |
where V and I are the true values of the bus voltages and selected line cur-
| B   | L   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
ε ε
rents and B and L are the errors in the measurements. It should be noted that
the measurement set contains exactly those quantities that would be produced
by line and transformer relays. While the voltage measurements alone are suffi-
cient to estimate the state (simply accept the measurement as the estimate) the
currents are included for redundancy, to detect and identify bad data, etc. If we
examine an entry I pq of the vector I L corresponding to a current measurement at
terminal p of an element connecting nodes p and q, as shown in Figure 8.1, we
can write
|     |     |        | (V   | )             |        |     |        |
| --- | --- | ------ | ---- | ------------- | ------ | --- | ------ |
|     |     | I pq D | y pq | p (cid:21)V q | D y po | V p | (8.20) |
where y pq and y po are the series and shunt admittances of the element. In general
then
[yATCy
|     |     |     | I L D |     | s ]V B |     | (8.21) |
| --- | --- | --- | ----- | --- | ------ | --- | ------ |

| Application | of phasor measurements |     | to state | estimation |     | 239 |
| ----------- | ---------------------- | --- | -------- | ---------- | --- | --- |
|             |                        |     | I        | I          |     |     |
|             |                        |     | pq       | qp         |     |     |
|             |                        | V   |          |            | V   |     |
|             |                        | p   |          |            | q   |     |
y pq
|     |        |             | y        | y          |               |     |
| --- | ------ | ----------- | -------- | ---------- | ------------- | --- |
|     |        |             | p0       | q0         |               |     |
|     | Figure | 8.1 Circuit | elements | connecting | nodes p and q |     |
where A is the current measurement-bus incidence matrix (defined much as the
element-bus incidence matrix16), y is a diagonal primitive admittance matrix of all
the series admittances of the metered lines or transformers, and y is the diagonal
S
primitive admittance matrix of all the shunt admittances of the metered elements at
the metered ends. If the total number of buses (excluding the reference) is n, the
total number of elements isb, and the number of current measurements ism, then y
is mðm, A is mðn and y is mðn. If the current at each end of every element
S
were measured then m D 2b. It is assumed, however, that m− 2b. The errors are
| assumed | to be zero mean | and | have covariance | given   | by      |     |
| ------- | --------------- | --- | --------------- | ------- | ------- | --- |
|         |                 |     |                 | (cid:2) | (cid:3) |     |
# $
W 0
|     |     |     | εεT D | D B |     |        |
| --- | --- | --- | ----- | --- | --- | ------ |
|     |     | E   | W     |     |     | (8.22) |
0 W
L
| Substituting | Equation | (8.21) into | (8.19)  |                 |         |     |
| ------------ | -------- | ----------- | ------- | --------------- | ------- | --- |
|              |          |             | (cid:2) | (cid:3) (cid:2) | (cid:3) |     |
|              |          |             | I       |                 | ε       |     |
B
|     |     | zD  |       | V B C |     | (8.23) |
| --- | --- | --- | ----- | ----- | --- | ------ |
|     |     |     | yATCy |       | ε   |        |
|     |     |     |       | s     | L   |        |
or
Cε
|     |     |     | z D | BV  |     | (8.24) |
| --- | --- | --- | --- | --- | --- | ------ |
B
Even though z, B, and V are complex, Equation (8.24) can be solved with the
B
leastsquaretechnique.Thatis,followingSection3.7,weminimizetherealquantity
|     |     | (z(cid:21)BV | )†W(cid:21)1(z(cid:21)BV |     | )   |     |
| --- | --- | ------------ | ------------------------ | --- | --- | --- |
|     |     |              | B                        |     | B   |     |
where † denotes the complex conjugate transpose of the array. The minimum is
| given by | the solution | of             |     |                 |     |        |
| -------- | ------------ | -------------- | --- | --------------- | --- | ------ |
|          |              | B†W(cid:21)1BV |     | D B†W(cid:21)1z |     | (8.25) |
B
or
|     |     |     | GV  | D B†W(cid:21)1z |     | (8.26) |
| --- | --- | --- | --- | --------------- | --- | ------ |
B
whereGisagainmatrixsimilartothatinEquation(8.13).Thealgorithmconsistsof
forming the matrix G and finding its LU factors (the factors can be stored and used

| 240 |     |     |     |     | System | relaying | and control |
| --- | --- | --- | --- | --- | ------ | -------- | ----------- |
until the network structure changes or the error description changes), computing
the right hand side of Equation (8.26) for each data scan, and solving Equation
(8.26). Note that no iteration is involved – the system and the measurements are
linear.
The structure of the G matrix is important in determining the practicality of the
algorithm. If we write G in terms of the partitions in the product
|     |     |     | (cid:2)   |     | (cid:3)(cid:2) | (cid:3) |     |
| --- | --- | --- | --------- | --- | -------------- | ------- | --- |
|     |     |     | W(cid:21) | 1 0 | I              |         |     |
∗ ∗
|     | GD[IjAy        | Cy  | ] B         |            |               |     |        |
| --- | -------------- | --- | ----------- | ---------- | ------------- | --- | ------ |
|     |                |     | s 0         | W(cid:21)1 | yATCy         |     |        |
|     |                |     |             | L          |               | s   |        |
|     | GDW(cid:21)1Cy | ∗   | W(cid:21)1y | CAy ∗      | W(cid:21)1yAT |     | (8.27) |
|     | B              | s   | L s         |            | L             |     |        |
|     | GDFC(HCH†)     |     |             |            |               |     | (8.28) |
where
|     |     |              | ∗           |     | ∗             |     |        |
| --- | --- | ------------ | ----------- | --- | ------------- | --- | ------ |
|     | F D | W(cid:21)1Cy | W(cid:21)1y | CAy | W(cid:21)1yAT |     | (8.29) |
|     |     | B            | s L         | s   | L             |     |        |
and
∗
|     |     | H   | D y | W(cid:21)1yAT |     |     | (8.30) |
| --- | --- | --- | --- | ------------- | --- | --- | ------ |
|     |     |     | s   | L             |     |     |        |
The first and second terms in F are real diagonal matrices (if W is diagonal- which
is our assumption), while the last term has the structure of an admittance matrix
for a resistive network. The primitive conductance matrix is a real diagonal matrix.
Indeed, F can be viewed as a conductance matrix for a system which has the
topology of the power system but whose elements are those shown in Figure 8.2.
Figure 8.2 is drawn for the element connecting nodes p and q. If only the voltages
aremeasuredthecircuitofFigure8.2(a)appliessinceonlythefirsttermofFwould
make a contribution at these buses. If current is measured at terminal p, the circuit
of Figure 8.2(b) applies, and if current is measured at both terminals the circuit in
Figure 8.2(c) results. The shunt conductances in Figure 8.2 are from the first two
terms in Equation (8.29) while the series terms are from the last term in Equation
F
(8.29). In all cases is real, sparse, and symmetric, independent of the X/R ratios
of the lines.
The remaining terms in G are from the matrix H. By direct calculation, if current
is measured at terminal p of the line connecting terminals p and q
|     |     | H   | D yŁ  | y /W |     |     | (8.31) |
| --- | --- | --- | ----- | ---- | --- | --- | ------ |
|     |     |     | pp po | pq   | pL  |     |        |
and
|     |     |      | (cid:21)yŁ | /W   |     |     |        |
| --- | --- | ---- | ---------- | ---- | --- | --- | ------ |
|     |     | H pq | D          | y pq | pL  |     | (8.32) |
po

| Application |     | of phasor | measurements |     | to  | state estimation |     |     |     | 241 |
| ----------- | --- | --------- | ------------ | --- | --- | ---------------- | --- | --- | --- | --- |
|2/W
|     |     |     |     |     |     |     |     | |y pq | pL  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
|     | p   |     |     |     | q   | p   |     |       |     | q   |
|     |     | 1   |     | 1   |     | |y  | |2  |       | 1   |     |
|     |     |     |     |     |     |     | p0  | 1     |     |     |
W
|     | W   | pB  |       | W   |        | W        | pB          | W     | qB  |     |
| --- | --- | --- | ----- | --- | ------ | -------- | ----------- | ----- | --- | --- |
|     |     |     |       | pq  |        |          |             | pB    |     |     |
|     |     |     | (a)   |     |        |          |             | (b)   |     |     |
|     |     |     |       |     |        | 1    +   |     1       |       |     |     |
|     |     |     |       |     | |y |2( |          |           ) |       |     |     |
|     |     |     |       |     | pq     | W        | W           |       |     |     |
|     |     |     |       |     |        | pL       | qL          |       |     |     |
|     |     |     | p     |     |        |          |             |       | q   |     |
|     |     |     | |y |2 |     |        |          |             | |y |2 |     |     |
|     |     |     | p0    |     | 1      |          | 1           | q0    |     |     |
|     |     |     | W     |     | W pB   |          | W qB        | W     |     |     |
|     |     |     | pL    |     |        |          |             | pL    |     |     |
(c)
Figure 8.2 Conductance of the network represented by matrix F. The labeled values
are conductances. (a) No current measurements at either end. (b) Current measurement
| at terminal |            | p. (c) | Current       | measurements |             | at both | ends |     |     |        |
| ----------- | ---------- | ------ | ------------- | ------------ | ----------- | ------- | ---- | --- | --- | ------ |
| and         | if current | is     | also measured |              | at terminal |         | q    |     |     |        |
|             |            |        |               |              |             | yŁ      | /W   |     |     |        |
|             |            |        |               |              | H qq        | D       | y pq | qL  |     | (8.33) |
qo
and
|      |     |         |              |     | H D     | (cid:21)yŁ | y /W |          |     | (8.34) |
| ---- | --- | ------- | ------------ | --- | ------- | ---------- | ---- | -------- | --- | ------ |
|      |     |         |              |     | qp      | qo         | pq   | qL       |     |        |
| Thus | for | current | measurements |     | at both | buses      | p    | and q    |     |        |
|      |     |         |              |     |         | %          |      | (cid:30) |     |        |
|      |     |         | (HCH†)       |     | D2Re    | yŁ         | /W   |          |     |        |
|      |     |         |              | pp  |         |            | y pq | pL       |     | (8.35) |
po
|     |     |     | (HCH†) |     | D(cid:21)yŁ | y     | /W   | (cid:21)y yŁ /W |     | (8.36) |
| --- | --- | --- | ------ | --- | ----------- | ----- | ---- | --------------- | --- | ------ |
|     |     |     |        | pq  |             | po pq | pL   | qo pq           | qL  |        |
|     |     |     | (HCH†) |     | D(cid:21)y  | yŁ    | /W   | (cid:21)yŁ y /W |     | (8.37) |
|     |     |     |        | qp  |             | po pq | pL   | qo pq           | qL  |        |
|     |     |     |        |     |             | %     |      | (cid:30)        |     |        |
|     |     |     | (HCH†) |     |             | yŁ    | /W   |                 |     |        |
|     |     |     |        | qq  | D2Re        |       | y pq | qL              |     | (8.38) |
po
If the element connecting p and q is a transmission line then y D y . If, in
|     |     |     |     |     |     |     |     |     | po  | qo  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | (W  | )   |
addition, the variance of the two measurements is the same D W then
|     |     |     |     |     |     |     |     |     | pL  | qL  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(HCH†) is a real symmetric matrix with admittance like structure. If the element
connecting p and q is a transformer with off-nominal turns ratio but with no losses,
(HCH†)
|     |     | is once | again | real and | symmetric. |     |     |     |     |     |
| --- | --- | ------- | ----- | -------- | ---------- | --- | --- | --- | --- | --- |

| 242 |     |     | System relaying | and control |
| --- | --- | --- | --------------- | ----------- |
If only one current is measured, at terminal p for example, then
|     |        |             | % (cid:30) |        |
| --- | ------ | ----------- | ---------- | ------ |
|     | (HCH†) | D2Re        | yŁ y /W    | (8.39) |
|     |        | pp          | po pq pL   |        |
|     | (HCH†) | D(cid:21)yŁ | /W         |        |
|     |        |             | y          | (8.40) |
|     |        | pq po       | pq pL      |        |
|     | (HCH†) |             | yŁ /W      |        |
|     |        | D(cid:21)y  |            | (8.41) |
|     |        | qp po       | pq pL      |        |
|     | (HCH†) | D0          |            | (8.42) |
qq
In this case the matrix (HCH†) is complex with rather small imaginary parts if
the X/R ratios of the lines are large. In general, the matrix G is a constant – with
symmetric current measurements it is real, sparse and symmetric and, if currents
are measured only at one end of some elements, it has complex off-diagonal
entries. Various techniques of avoiding the complex arithmetic involved with
a complex G including the use of pseudo current measurements have been
investigated.16 The reference angle problem does not exist for the linear state
estimator (LSE) since the reference is that produced by the synchronizing of the
samples.
| 8.4.3 Partitioned | state estimation |     |     |     |
| ----------------- | ---------------- | --- | --- | --- |
A partitioned state estimator would be one in which a portion of the network
had a measurement set consisting of complex flows and injections and where the
conventional WLS estimator was used, and a second distinct region where current
and voltage phasor measurements were made and the LSE used. Considering the
probable application, the WLS region will be referred to as the high voltage system
and the LSE region will be referred to as the low voltage system. A representation
of such a system is shown in Figure 8.3. Rather than approach the problem as
one large WLS system it has been proposed that the two types of estimators can be
combinedinawaythatsolvestheanglereferenceproblemmentionedearlier.18 The
basic problems in combining the two estimators are the treatment of the boundary
buses between the two systems and the question of reference angles for the two
systems.19–21
The boundary buses in question are taken as the high sides of transformers con-
necting to the low voltage network. These buses are assumed to be included in both
estimatorsand,sincethelowvoltagesystemisassumedtobeprotecteddigitally,the
phasor measurements of the boundary buses are available to both estimators. These
phasormeasurementscanbeincludedintheWLSestimatorasinEquation(8.17)or
ignored as desired. In either case, the WLS estimator is run, and produces estimates
of the boundary bus angles with a reference taken as one of the high voltage

Application of phasor measurements to state estimation 243
High Voltage System
WLS
Boundary
buses
Low Voltage System
LSE
Figure 8.3 Partitioned network. The boundary buses are the high side of the transformers
connecting the two systems
buses. Measurements of these same angles with the time synchronizing reference
are also available. The average difference between these angles (averaged over all
the boundary buses) is an accurate estimate of the difference in angle between the
two references. That is,
(cid:5)NB
1
φ D (φˆ Hv,i (cid:21)φ Lv,i ) (8.43)
NB
iD1
where NB is the number of boundary buses, θ Hv,i is the estimate of the ith bound-
ary bus angle form the WLS estimator and θ Lv,i is the measurement of the ith
boundary bus angle. The angle φ can be subtracted from the estimated boundary
bus angles and from the angles of the estimated currents at the boundary produced
by the WLS and these quantities used as measurements in the LSE algorithm.
ThevarianceoftheestimateinEquation(8.43)couldbefurtherreducedbyusingthe
estimated angles from the low voltage system rather than the measurements. This
would mean running the LSE algorithm twice, however. In either case, the esti-
mate in Equation (8.43) is highly accurate if there are a number of boundary buses.
Simulation results have been given for the partitioned estimator performance on the
IEEE 118 bus system20 where the WLS algorithm was used on the 345kV system
and the LSE algorithm was used on the 138kV system.
If a sufficient number of currents are measured the LSE algorithm has bad data
detection and identification properties comparable to WLS algorithms. In addition,
since a number of relaying devices make phasor measurements in the substation,
it is possible to pre-process data in the substation and reject bad data at a lower
level. A technique of voting, averaging, or setting flags for suspect data has been
described.15 The need for all of these various approaches can be understood by
considering the case of three voltage measurements made in a single substation. If

244 System relaying and control
allthreeagreewithinsometolerancethethreecouldbeaveragedandtransmitted.If
one of the three is very different from the other two, the average of the two similar
measurements could be transmitted to the control center. Finally, by considering
four voltage measurements grouped into two agreeing groups of two each, the need
for flagged data is seen. In this case the two averages would both be transmitted
but with flags indicating that at least one of the pair is ‘bad data’. The flags then
provideguidancetothebaddatadetectionandidentificationportionoftheestimator.
Just as in the WLS algorithm, conservation laws can be used at the substation
to provide consistency checks of flow measurements. In the LSE algorithm this
is simply the Kirchhoff current law. Combining the KCL check and the voltage
checks approximately 75% of the bad data produced in Monte Carlo simulation
was detected at the substation level.15
8.4.4 PMU locations
The selection of the location of PMUs has become an active research problem.19
A number of factors motivate the interest in optimum locations for the incremental
addition of PMUs to a system. Even if the SCADA system were ultimately to be
replaced,itcouldnotbedonerapidly.Theexpenseofhundredsoreventhousandsof
PMUs must be spread out over time. For some applications the number of possible
locations of PMUs may be limited. The use of PMUs in improved Power System
Stabilizers, or in joining adjacent state estimators are such examples. But the state
estimation problem involves virtually all power system buses. The first important
observation is that if line currents are measured, then the bus voltage measurement
can be extended from the PMU location to every bus that is connected to that
bus. Using a variety of approaches, multiple authors have concluded that only
approximately one third of the system buses need to have PMUs in order to learn
all the bus voltages.22–24 A third of the buses is still an imposing number of PMU
installations so attempts to phase in the PMUs have also been attempted. Slightly
different answers are obtained by different authors in these problems due to the
varyingamountsofpreprocessingontheproblem.Theextremesrangefromsolving
the problem on the original intact network to doing extensive network reductions
before placing PMUs.
The above is concerned with placing PMUs for state estimation. Because a large
number of PMUs are ultimately required the sequential solution of the problem is
an issue. Suppose the plan was to install 20 PMUs a year for fiveyears. It would be
most desirable if the best 20 locations were used in the first year and were a subset
of the best 100. It is more likely that the first 20 must be the best 20 of the best 100
but not necessarily the best 20. This is an interesting problem and different than
trying to find the best location for a reasonably small number of PMUs to solve
a control problem. The decision trees of Section 4.10.2 have been used to choose

Phasor measurements in dynamic state estimation 245
PMU locations for control.25 The trees’ ability to select a few variables for the
splitting nodes is an attractive way to chose PMU locations.
8.5 Phasor measurements in dynamic state estimation
TheestimationinSection8.4isstaticinthatthepowersystemisassumedtobeina
constantstatewhilethemeasurementsaremade.Sincethephasormeasurementsare
availableasoftenasonceacycle,itisclearthatmoredynamicestimationispossible
usingthesemeasurements.Tosimplyextendthestaticstateestimationalgorithmsto
a once-a-cycle time frame involves much more than making faster measurements,
however. The communication requirements imposed by the physical size of the
powersystemareformidable.Itisclearthatonlyselectedbusescouldbemonitored
at this high rate. A use of such a selected set of real-time measurements in power
system stability is given in Chapter 8 of Reference 19 (see Reference List). The
localuseofrapidreal-timemeasurements,wherecommunicationisnotanissue,isa
real possibility. The estimation of the internal states and parameters of synchronous
machines offers an obvious application of the use of such measurements.
Theestimationof machineparameters andinternalstates fromfielddatahas been
suggested.26–29 Either no angle measurements were used,26 or zero crossing infor-
mation was used to measure angles.27 An example of the use of measurements of
phasorsandlocalfrequencyinsuchanapplication29 wasbasedonthesystemshown
in Figure 8.4. It consists of a synchronous generator connected to an infinite bus
through a tie line. The linear models of the exciter controller, governor controller,
and turbine stage are shown in Figure 8.5. A transient was caused in the steady
state operation by connecting a load to the system through switch S. The model of
the synchronous machine30 assumes that the machine has one direct axis and one
quadrature axis winding on the stator, one direct and one quadrature axis damper
Governor Machine
Turbine
tie-line
+
ω
ref −
ω S
r
Exciter
V
t
−
+
V
ref
Figure 8.4 System used for dynamic estimation

| 246 |     |     |     |     |     |     | System relaying | and control |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- |
|     |     | V   | +   |     |     |     | V               |             |
|     |     | ref |     |     | K   |     | t               |             |
s
1 + sT
|     |     |     | −   |     |                    | s   |     |     |
| --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
|     |     |     | V   |     | Exciter controller |     |     |     |
t
|     |     | ω   | +   |     | K   |     | P   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | g   |     | g   |     |
ref
1 + sT
|     |     |     | −   |     |     | g   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ω
r
Governor controller
|     |     |     |     | P   |        |     | P   |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- |
|     |     |     |     | g   | 1      |     | m   |     |
|     |     |     |     |     | 1 + sT | T   |     |     |
Turbine stage
Figure8.5 Exciterandgovernorcontrollersandturbinestateofthesynchronousgenerator
winding on the rotor and the field winding (in the direct axis) on the rotor. The flux
linkages, rotor speed, and rotor angle form a convenient state for the machine. The
differential equations for the synchronous generator are in the form
|     |     |     | V           | D(cid:21)R | i (cid:21)λ˙ (cid:21)λ | ω   |     |        |
| --- | --- | --- | ----------- | ---------- | ---------------------- | --- | --- | ------ |
|     |     |     | d           |            | a d d                  | q   | r   |        |
|     |     |     | V           | D(cid:21)R | i (cid:21)λ˙ (cid:21)λ | ω   |     |        |
|     |     |     | q           |            | a q q                  | d   | r   |        |
|     |     |     | V           | D(cid:21)R | i (cid:21)λ˙           |     |     | (8.44) |
|     |     |     | f           |            | f f f                  |     |     |        |
|     |     |     | 0D(cid:21)R |            | (cid:21)λ˙             |     |     |        |
|     |     |     |             |            | kd i kd kd             |     |     |        |
(cid:21)λ˙
|                   |     |             | 0D(cid:21)R |              | kq i kq kq |         |      |     |
| ----------------- | --- | ----------- | ----------- | ------------ | ---------- | ------- | ---- | --- |
|                   |     |             |             | Dλ           | (cid:21)λ  |         |      |     |
|                   |     |             | T           | i            | i          |         |      |     |
|                   |     |             | e           | d q          | q d        |         |      |     |
| The flux linkages |     | are related | to          | the currents | as         | follows |      |     |
|                   |    |            |            |              |            |         |   |     |
λ
|     |     |     | L   | 0     | L L     | 0    | i         |        |
| --- | --- | --- | --- | ----- | ------- | ---- | --------- | ------ |
|     |    | d  |    |       | af      | akd  |   d    |        |
|     |     | λ   | 0  | L     | 0 0     | L    | i        |        |
|     |    | q  |     | q     |         |      | akq  q  |        |
|     |    | λ  |    |       |         |      |        |        |
|     |    | D  | L  | 0     | L L     | 0    |  i     | (8.45) |
|     |     | f   |     | af    | f       | fkd  | f         |        |
|     | λ  |    |    |       |         |      |        |        |
|     |     | kd  | L   | akd 0 | L fkd L | kd 0 | i kd      |        |
|     |     | λ   | 0   | L     | 0 0     | L    | i         |        |
|     |     | kq  |     | akq   |         |      | kq kq     |        |

| Phasor measurements |             | in          | dynamic  | state | estimation |     |     |            |     | 247 |
| ------------------- | ----------- | ----------- | -------- | ----- | ---------- | --- | --- | ---------- | --- | --- |
| where for           | the machine |             | used     |       |            |     |     |            |     |     |
|                     |            |             |          |       |            |     |     |            |    |     |
|                     |             | 0.005889    |          |       | 0.005335   |     |     | 0.005335   |     |     |
|                     | L           | D           |          | L     | D          |     | L   | D          |     |     |
|                     |             | d           |          |       | af         |     | akd |            |     |     |
|                     |            | D 0.005602  |          |       | D 0.005045 |     | D   | 0.005615   |    |     |
|                     | L          | q           |          | L     | akq        |     | L f |            |    |     |
|                     |            |             |          |       |            |     |     |            |    |     |
|                     | L          | D           | 0.005335 | L     | D 0.995345 |     | L   | D 0.005061 |    |     |
|                     |             | fkd         |          |       | kd         |     | kq  |            |     |     |
|                     |            | 0.0014      |          |       | 0.0012294  |     |     | 0.004349   |    |     |
|                     | R           | D           |          | R     | D          |     | R   | D          |     |     |
|                     |             | a           |          |       | f          |     | kd  |            |     |     |
|                     | R           | D 0.0132451 |          |       |            |     |     |            |     |     |
kq
| 8.5.1           | State | equation  |           |        |         |     |     |     |     |     |
| --------------- | ----- | --------- | --------- | ------ | ------- | --- | --- | --- | --- | --- |
| If we partition |       | the state | variables | as     | follows |     |     |     |     |     |
|                 |       |           |           | xT D[λ | λ λ     | λ λ |     |     |     |     |
v ]
|              |     |                |     | 1      | d f  | kd kq | q f |      |     |        |
| ------------ | --- | -------------- | --- | ------ | ---- | ----- | --- | ---- | --- | ------ |
|              |     |                |     | xT     | ω    | δ]    |     |      |     |        |
|              |     |                |     | D[P    | P    |       |     |      |     |        |
|              |     |                |     | 2      | q m  | r     |     |      |     |        |
| we can write | a   | state equation |     | in the | form |       |     |      |     |        |
|              |     |               |    |        |      |       |    |     |     |        |
|              |     |                |     |       |      |      |     |      |     |        |
|              |     |                | ž   |        | (ω ) |       | x 1 |      |     |        |
|              |     |               |    | A      |      | 0     |    |     |     |        |
|              |     |               | x  |        | 11 r |       |    |     |     |        |
|              |     |                | 1 D |       |      |      |     | CBu |     | (8.46) |
|              |     |               |    |        |      |       |    |      |     |        |
ž
|     |     |     |     | 0   |     | A   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | x   |     |     | 22  | x   |     |     |     |
|     |     |     | 2   |     |     |     | 2   |     |     |     |
where the entries in A are obtained from combining Equations (8.44), (8.45) and
thenumbersinFigure8.5(theequationisnonlinearinthestateω
from(8.44)).The
r
| input u | is given | by  |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:29)
|     |     | uT  | D [V | V   | V2CV2 | (V  | i CV | i ) 1] |     | (8.47) |
| --- | --- | --- | ---- | --- | ----- | --- | ---- | ------ | --- | ------ |
|     |     |     | d    | q   | d     | q   | d d  | q q    |     |        |
At each instant of time it is assumed that the following quantities are measured
|          |         |         |                  | ,V ,i | ,i ,i ,V      | ,ω     | ,   | δ   |     |        |
| -------- | ------- | ------- | ---------------- | ----- | ------------- | ------ | --- | --- | --- | ------ |
|          |         |         | V d              | q     | d q f         | f r    | and |     |     |        |
| The last | six are | written | as a measurement |       |               | vector |     |     |     |        |
|          |         |         | z(kC1)           |       | x(kC1)Cε(kC1) |        |     |     |     |        |
|          |         |         |                  | D     | H             |        |     |     |     | (8.48) |
whereεrepresentsthemeasurementerrorswhichareassumedtobezeromeanwith
covariancematrixQ.Thenonlineardependence oftheinputuonthemeasurements
andthenonlinear dependenceonω requirestheso-calledextendedKalmanfilter,31
r
which represents an approximate solution to the nonlinear filtering problem. The
extendedKalmanfiltersolutionalongwithanobserverbasedsolutiontotheestima-
tion problem has been given.29 It should be noted that the measurements made by
the SCDFT are particularly appropriate for this application – direct and quadrature

248 System relaying and control
components of voltages and currents are easily obtained, and the measurements of
δ and ω are natural.
r
8.6 Monitoring
8.6.1 Sequence of events analysis
The ability of the integrated protection system to store samples of analog quan-
tities and the status of contacts at every sampling instant makes it capable of
providing data for sequence of events analysis. The desirability of time-tagging
such information has been mentioned in the context of synchronized sampling.2
The oscillography function of present relaying algorithms is limited by their rela-
tively low sampling rates and the corresponding low bandwidth anti-aliasing filters
required. Thesignals that are passed bycommonly used anti-aliasingfiltersarelim-
ited to a few hundred Hz. The oscillographs that would be generated are unable to
reproduce some system phenomena such as switching surges, traveling waves (see
Chapter 9) or other high frequency components in voltages and currents. There is
a substantial amount of information in the low bandwidth oscillographs, however.
The low bandwidth oscillographs may be adequate for many uses.
With the steady improvement in the capability of microprocessors and A/D con-
verters it seems possible that the broader bandwidth oscillography function may
be performed by the integrated protection system in the future. It should be rec-
ognized that it is not necessary to increase the rate at which relaying calculations
are performed to provide the oscillography function. One possibility is to sample
at the high rate needed for oscillography (using anti-aliasing filters appropriate to
the higher sampling rate) and convert the high rate samples to properly filtered
low rate samples for the protection modules. A technique for this conversion along
with a common data format which could be used for data exchange is presented in
Appendixes III and IV.
8.6.2 Incipient fault detection
Anotherproblemwhichmayseesomeresolutionwithcomputermonitoringsystems
is that of detecting incipient faults in transformers. It is well known that most
internal faults in a power transformer begin as small discharge currents inside the
transformer tank. As these currents continue to flow, they cause further damage,
accelerate the insulation breakdown, and lead to more serious permanent faults. At
present, the incipient faults are detected by analyzing the gases collected in the
transformer tank as a by-product of the combustion process. It may be possible to
develop a technique to recognize the incipient fault condition by detecting certain
features of the transformer current. It would be very difficult to detect a change in
currentcausedbytheincipientfault:itistoosmallcomparedtothetransformerload
current. Perhaps the frequency content of the transformer current may be a unique

Control applications 249
feature of the incipient fault. In any case, it would be necessary to suppress the
steady state components from such a consideration, and also rather high sampling
rates may be needed to detect the expected high frequency components in the
incipient fault discharge current. Much work remains to be done in this area.
8.6.3 Breaker health monitoring
The performance of a circuit breaker can be monitored rather easily with the relays
used for tripping and reclosing the breaker. One of the main concerns in circuit
breaker operation is the arcing time of the main and auxiliary (if any are present)
contacts.Asthecurrentinthecircuitbreakerismonitoredbytherelay,itisasimple
matter to keep track of the changes in the breaker current as each contact interrupts
its current. The transient monitor function discussed in Section 5.5 provides a reli-
able indicator of changes in the breaker current after each successful interruption.
As the instant when the breaker trip coil is energized is known to the relay, rather
accurate information about the breaker contact arcing can be obtained and stored
in the memory of the relay. This information is of great value in determining the
servicing schedule for the breaker.
Bysimilartechniques,breakerpre-strikescanalsobemonitored.Sincetheinstant
of energizing the reclose coil of the breaker is known, the start of current flow in
the breaker could be timed. This can be compared with the expected start delay
based upon the contact travel time in its closing stroke. A premature current start
indicates pre-strike, and may once again indicate necessary breaker maintenance. It
is also be possible to monitor the pressure in the circuit breaker air supply system
to determine if a given trip or reclose operation could be carried out successfully.
In the case of insufficient air pressure, all breaker operations should be blocked,
and a service alarm issued.
8.7 Control applications
A number of wide-area control applications have been described in the literature
but few have found their way into the
field.19,32–37
Most are derived from linear
optimal control theory and have constant feedback gains. The applications include
the control of HVDC lines,33 excitation systems,34 power system stabilizers,36
and FACTS devices.37 A form of discrete control of DC lines was also pro-
posed where DC line flows were changed discretely based on a set of phasor
measurements.25 Decision trees were used to determine the situations in which the
DClineflowswerechanged.Allofthesecontrolswerefoundtoworkeffectivelyin
simulation.
The control of low frequency inter-area oscillations with remote phasor mea-
surements is a more developed idea. Low frequency oscillations are a growing
problem in modern large-scale power systems. The oscillations are associated with
under damped inter-area modes with frequencies less than one Hz. The extensive

| 250 |     |     |     |     |     |     |     | System relaying | and control |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- |
wide area measurement system and the numerous DC lines in the Chinese system
have created an opportunity to address these modes with a WAMS-based con-
system.38,39
trol The system is designed using pole placement techniques and uses
measurements of angles, frequencies and real power flows. It is adaptive, in that
the actual frequencies of the oscillation are measured with a fast real-time Prony
algorithm40
|     | and | the | gains adjusted |     | before | the | loop is | closed. |     |
| --- | --- | --- | -------------- | --- | ------ | --- | ------- | ------- | --- |
8.8 Summary
This chapter has emphasized the use of the digital relay as a measuring device. The
high reliability and data processing ability of the digital relay make the measuring
function a logical complement to the protection function. By synchronizing sam-
pling across the power system it is possible to obtain direct measurements of the
state of the system. These real-time measurements of the bus voltage angles and
magnitudes can be used to supplement or complement existing static state estima-
tion algorithms. A particularly elegant linear estimator is produced if only real-time
phasor measurements of bus voltages and line currents are used. The basic issue in
connecting the two types of estimators is that of establishing a relationship between
| the reference | angles |     | used in | each. |     |     |     |     |     |
| ------------- | ------ | --- | ------- | ----- | --- | --- | --- | --- | --- |
Real-time phasor measurements can also be used in estimating the internal states
and parameters of synchronous machines from measurements at their terminals.
Digital relays also can provide data for sequence of events analysis, incipient fault
analysis, and breaker health. It is easy to imagine microprocessor based relays as
the lowest level of a vast computer hierarchy dedicated to the integrated protection
| and control | of  | the bulk | power | system. |     |     |     |     |     |
| ----------- | --- | -------- | ----- | ------- | --- | --- | --- | --- | --- |
Problems
|     |     |     |     |     |     |     |     | (t) cosωt. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
8.1 Obtain the single phase version of equation v D Evaluate when
a
ω D 2π(60C0.1).Use12samplespercycleandanominalfrequencyof60Hz.
8.2 Verify Equations (8.25) and (8.26). Note that z must be expressed in terms of
real and imaginary parts and the objective quantity minimized with respect to
each.
| 8.3   |     |              |     | A A  |        | B   |          |         |     |
| ----- | --- | ------------ | --- | ---- | ------ | --- | -------- | ------- | --- |
| Write | out | the matrices |     | 11 , | 22 and | in  | Equation | (8.46). |     |
8.4 Obtain a least squares solution to the problem of simultaneously estimating the
| frequency |     | and the | rate | of change | of  | frequency. |     |     |     |
| --------- | --- | ------- | ---- | --------- | --- | ---------- | --- | --- | --- |
8.5 If the sampling instants have jitter, what is the influence on the frequency
measurement?
8.6 If phasors at different locations have time slews, develop state estimation algo-
| rithms | to  | estimate | the | constant | but | unknown | slews. |     |     |
| ------ | --- | -------- | --- | -------- | --- | ------- | ------ | --- | --- |

References 251
8.7 If each sample of voltage has an independent error with zero mean and a
standard deviation proportional to the sample, find the resulting error in the
positive sequence voltage and in the frequency.
8.8 Given voltage phase angle measurements at both ends of a line with a syn-
chronizing error of (cid:1)T, how much improvement can be made in the estimate
of the angle across the line by measuring the current at both ends? Assume
the current phasor measurements are synchronized with the respective voltage
phasor measurements.
References
[1] Phadke, A.G., Thorp, J.S., Adamiak, M.G. (1983) A new measurement technique for
tracking voltage phasors, local system frequency and rate of change of frequency,
IEEE Trans. on PAS., vol. 102, no. 5, pp. 1025–1038.
[2] Burnett, Jr., R.O. (1984) Field experience with absolute time synchronism between
remotely located fault recorders and sequence of event recorders, IEEE Trans. on
PAS, vol. 103, no. 7, pp. 1739–1742.
[3] Bonanomi,P.(1981)Phaseanglemeasurementswithsynchronizedclocks – principles
and applications, IEEE Trans. on PAS, vol. 100, no. 11, pp. 5036–5043.
[4] Missout, G., Beland, J. and Bedard, G. (1981) Dynamic measurement of the abso-
lute voltage angle on long transmission lines, IEEE Trans. on PAS, vol. 100, no. 11,
pp. 4428–4435.
[5] Missout,G., Beland, J.,Bedard, G. and Bussieres,P. (1984) Study of time dissemina-
tionmethodsusedonelectricpowersystemwithparticularreferencetoHydro-Quebec,
IEEE Trans. on PAS, vol. 103, no. 4, pp. 861–868.
[6] Phadke, A.G., Begovic, M.M., Centeno, V.A. et al. (1988) Coherent sampling for
system-wide digital relaying, NSF Workshop on Digital Relaying, Blacksburg, VA.
[7] SunD.I.,Ashley,B.,Bewer,A.etal.(1984)OptimalpowerflowbyNewtonapproach,
IEEE Trans. on PAS, vol. 103, no. 10, pp. 2864–2880.
[8] Stott,B.andHobson,E.(1978)Powersystemsecuritycontrolcalculationsusinglinear
programming, Part IandPartII, IEEE Trans. onPAS, vol.97, no.5, pp.1706–1731.
[9] Allemong, J.J., Radu, L. and Sasson, A.M. (1982) A fast and reliable state estima-
tion algorithm for AEP’s new control center, IEEE Trans. on PAS., vol. 101, no. 4,
pp. 933–945.
[10] Dopazo, J.F., Ehrmann, S.T., Klitin, O.A. et al. (1976) Implementation of the AEP
real-time monitoring system, IEEE Trans. on PAS, vol. 95, no. 5, pp. 1618–1629.
[11] Zhong,S.andAbur,A.(2005)Combinedstateestimationandmeasurementcalibration,
IEEE Trans. on Power Systems, vol. 20, no.1, pp. 458–465.
[12] Zhou, M. (2008) Phasor measurement unit calibration and applications in state esti-
mation. Ph.D. Dissertation, Virginia Tech.
[13] Phadke, A.G., Thorp, J.S., Nuqui, R.F. and Zhou, M. (2009) Recent developments in
stateestimationwithphasormeasurements,IEEE/PESPowerSystemsConferenceand
Exposition (PSCE),Seattle.
[14] Handshin,E.,Schweppe,F.C.,Kohloas,J.andFletcher,A.(1975)Baddataanalysisfor
powersystemstaticstateestimation,IEEETrans.onPAS.,vol.94,no.2,pp.329–338.

| 252 |     |     |     | System relaying | and control |
| --- | --- | --- | --- | --------------- | ----------- |
[15] Mili,L.,VanCursem,T.andRibbens-Pavella,M.(1985)Baddataidentificationmeth-
ods in power system state estimation – a comparative study, IEEE Trans. on PAS,
| vol. | 104, no. 11, pp. 3037–3049. |     |     |     |     |
| ---- | --------------------------- | --- | --- | --- | --- |
[16] Thorp, J.S., Phadke, A.G. and Karimi, K.J. (1985) Real time voltage-phasor mea-
surements for static state estimation, IEEE Trans. on PAS., vol. 104, no. 11,
pp. 3098–3108.
[17] Thorp, J.S., Phadke, A.G. and Karimi, K.J. (1986) State estimation with phasor mea-
| surements, | IEEE Trans. on | PWRS., vol. 1, | no. 1, pp. | 233–241. |     |
| ---------- | -------------- | -------------- | ---------- | -------- | --- |
[18] Karimi,K.J.,Thorp,J.S.andPhadke,A.G.(1986)Partitionedstateestimatorsandbad
data processing for static state estimators with phasor measurements, Proceedings of
the 1986 North American Power Symposium, Ithaca, NY, pp. 131–140.
[19] Phadke A.G. and Thorp, J.S. (2008) Synchronized Phasor Measurements and Their
| Applications, | Springer. |     |     |     |     |
| ------------- | --------- | --- | --- | --- | --- |
[20] Nuqui, R.F. and Phadke, A.G. (2005) Phasor measurement placement techniques for
complete and incomplete observability, IEEE Trans. on Power Delivery, vol. 20, no.
| 4, pp. | 2381–2388. |     |     |     |     |
| ------ | ---------- | --- | --- | --- | --- |
[21] Gou, B. and Abur, A. (2001) An improved measurement placement algorithm for
network observability, IEEE Trans. on Power Systems, vol. 16, no. 4, pp. 819–824.
[22] Abur,A.(2005)Optimalplacementofphasormeasurementsunitsforstateestimation,
| PSERC | Publication 06-58. |     |     |     |     |
| ----- | ------------------ | --- | --- | --- | --- |
[23] Rovnyak, S., Taylor, C.W. and Thorp, J.S. (1995) Real-time transient stability
prediction – possibilitiesforon-lineautomaticdatabasegenerationandclassifiertrain-
ing,SecondIFACSymposiumonControlofPowerPlantsandPowerSystems,Cancun,
Mexico.
[24] Jeffers,R. (2007) Wide Area State Estimation Techniques Using Phasor Measurement
Data. Virginia Tech Report prepared for Tennessee Valley Authority.
[25] StaggG.W.andEl-Abiad,A.H.(1968)ComputerMethodsonPowerSystemsAnalysis,
| McGraw-Hill | Company. |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
[26] Phadke,A.G.,Thorp,J.S.andKarimi,K.J.(1986)Powersystemmonitoringwithstate
vector measurements, Second International Conference on Power System Monitoring
| and Control, | Durham. |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- |
[27] de Mello, F.P., Hannet, L.N., Smith, D. and Wetzel, L. (1982) Derivation of syn-
chronous machine parameters from pole slipping conditions, IEEE Trans. on PAS.,
| vol. | 101, no. 9, pp. 3394–3402. |     |     |     |     |
| ---- | -------------------------- | --- | --- | --- | --- |
[28] Sugiyama, T., Nishiwaki, T., Tokedo, S. and Abe, S. (1982) Measurement of syn-
chronous machine parameters under operating conditions, IEEE Trans. on PAS,
| vol. | 101, no. 4, pp. 895–905. |     |     |     |     |
| ---- | ------------------------ | --- | --- | --- | --- |
[29] Namba,M.,Nishiwaki, T., Yokokawa,S. etal. (1981) Identification ofparameters for
power system stability analysis using Kalman filter, IEEE Trans. on PAS, vol. 100,
| no. 7, | pp. 3304–3311. |     |     |     |     |
| ------ | -------------- | --- | --- | --- | --- |
[30] Pillay, P., Phadke, A.G., Lindner, D.K. and Thorp, J.S. (1988) State estimation for a
synchronous machine: Observer and Kalman filter approach, Princeton Conference.
[31] Anderson P.M. and Fouad, A.A. (1981) Power System Control and Stability, Iowa
| State      | University Press, Ames,             | Iowa. |            |     |     |
| ---------- | ----------------------------------- | ----- | ---------- | --- | --- |
| [32] Gelb, | A. (1975) AppliedOptimalEstimation, |       | MIT Press. |     |     |

References 253
[33] Rostamkolai, N. (1986) Adaptive optimal control of AC/DC systems. Ph.D. Disserta-
| tion, Virginia | Tech. |     |     |
| -------------- | ----- | --- | --- |
[34] Rostamkolai,N.,Phadke,A.G.,Thorp,J.S.andLong,W.F.(1988)Measurementbased
optimalcontrolofhighvoltageAC/DCsystems,IEEETrans.onPowerSystems,vol.3
| no. 3, pp. | 1139–1145. |     |     |
| ---------- | ---------- | --- | --- |
[35] Manansala,E.C.andPhadke,A.G.(1991)Anoptimalcentralizedcontrollerwith non-
linear voltage control, ElectricMachinesand PowerSystems (19), pp. 139–156.
[36] Mili, L., Baldwin, T. and Phadke, A.G. (1991) Phasor measurements for voltage and
transientstabilitymonitoringandcontrol,WorkshoponApplicationofadvancedmath-
| ematics to | Power Systems, | San Francisco. |     |
| ---------- | -------------- | -------------- | --- |
[37] Snyder,A.F.,Hadjsaid,N.andGeorges,D.etal.(1998)Inter-areaoscillationdamping
withpowersystemstabilizersandsynchronizedphasormeasurements,PowerCon1998,
China.
[38] Smith, M.A. (1994) Improved dynamic stability using FACTS devices with phasor
| measurement | feedback. | MS Thesis, Virginia | Tech. |
| ----------- | --------- | ------------------- | ----- |
[39] Zhang, Z.S., Xie, X. and Wu, J. (2008) WAMS-based detection and early warning
of low-frequency oscillations in large scale power systems, Electric Power Systems
| Research, | 78, pp. 897–906. |     |     |
| --------- | ---------------- | --- | --- |
[40] Shi, J.H., Li, P., Wu, X.C. et al. (2008) Implementation of an adaptive continuous
real-time control based on WAMS, Monitoring of Power System Dynamic Perfor-
| mance, Saint | Petersburg. |     |     |
| ------------ | ----------- | --- | --- |
[41] Jinyu, X., Xiarong, X. et al. (2004) Dynamic tracking of low-frequency oscillations
with improved Prony method in wide-area measurement system, Proceedings of the
IEEE Power Engineering Society Meeting, vol. 1, pp. 1104–1109.

9
Relaying applications of traveling
waves
9.1 Introduction
In thischapter we will discuss some developments which are technically interesting
and promising. In doing so, we expose ourselves to the danger of dating this book.
Onlytimewilltellwhethertheseconceptsbecomewidelyacceptedrelayingpractices
orremainmerecuriosities.Ontheotherhand,wefeelthatabooksuchasoursisan
accountofthisfieldasweviewitnowandthereforeshouldtakenoteofwhateveris
technicallyinterestingandhassomechanceofbeingacceptedbytheindustry.
We will discuss the following topics in this chapter: traveling wave relaying, dif-
ferential relaying with phasors, and fault location. The developments in transducer
designandcommunicationsystemsbrought about byfiberoptictechnologyarealso
important new subjects which have been discussed in earlier chapters. These trans-
ducer and communication system advances seem certain of being widely accepted
by relay engineers. It turns out that high speed communication and data processing
isalso an essential element of traveling waverelaying and linedifferential relaying.
Fault location technology has clearly become an invaluable feature of most modern
distance relays. It goes without saying that all three concepts are motivated and
sustained by the development of computer relaying.
9.2 Traveling waves on single-phase lines
Any electrical disturbance propagates as a traveling wave on a transmission line. In
single-phase transmission lines, the waves are single-mode waves – i.e. they have a
singlepropagationvelocityandcharacteristicimpedance – whereasinathree-phase
transmission line there are at least two distinct modal velocities and characteristic
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

256 Relaying applications of traveling waves
impedances. In either case, the occurrence of a fault sets up these traveling waves
which propagate from the fault point towards the line terminals where relays are
located. It is possible to design relays which utilize these propagation phenomena
to detect the presence of a fault, and to determine the fault location. Since the
traveling waves constitute the earliest possible evidence available to a relay that a
faulthasoccurred,theserelayshavethepotentialofbecomingthefastestresponding
relays. On the other hand, the traveling wave phenomena tend to contain high
frequency signals (several kilohertz to megahertz, depending upon the location of
the fault), and consequently the data acquisition system (A/D conversions) must
have a correspondingly high bandwidth. At present, microcomputer systems would
be hard-pressed to handle the traveling wave relay tasks except in cases of very
long lines which produce long propagation delays. Nevertheless, the traveling wave
relays represent a new and interesting development in the field of relaying, and
although they may not be ‘computer relays’ in the manner of impedance relays
discussed earlier, we will consider their operating principle in this section.
Considerasingle-phase(twoconductorsinfreespace)transmissionlineshownin
Figure 9.1. Figure 9.1(a) shows the pre-fault conditions on the line. A fault occurs
at F, where the pre-fault voltage is e . The occurrence of a fault can be simulated
F
by superimposing on the pre-fault network voltages and currents produced by a
fault network consisting of a single source of magnitude −e at the fault point. The
F
relay is located at R, and is designed to sense the voltages and currents of the fault,
i.e. of the network of Figure 9.1(b). In other words, the relay senses deviations in
currents and voltages form their pre-fault values.
R F R F
e F −e F
(a) (b)
i
e
x i
(c)
Figure9.1 Single-phasetransmissionline.Wavepropagationinitiatedbyafault.(a)Initial
conditions. (b) Fault representation. (c) Wave phenomena

| Traveling waves | on single-phase |     | lines |     |     | 257 |
| --------------- | --------------- | --- | ----- | --- | --- | --- |
x
Now consider a point at a distance measured from the relay location along
the transmission line. The voltage and current at x obey the partial differential
equations1
|     |     |     |     | ∂e  | ∂i  |     |
| --- | --- | --- | --- | --- | --- | --- |
=−L
|     |     |     |     | ∂x  | ∂t  |       |
| --- | --- | --- | --- | --- | --- | ----- |
|     |     |     |     | ∂i  | ∂e  |       |
|     |     |     |     | =−C |     | (9.1) |
|     |     |     |     | ∂x  | ∂t  |       |
where L and C are the inductance and capacitance of the line per unit length. The
resistance of the line is assumed to be negligible. Solution of Equation (9.1) is
|     |     | e(x,t)=e |     | (x−vt)+e  | (x+vt)   |       |
| --- | --- | -------- | --- | --------- | -------- | ----- |
|     |     |          |     | f         | r        |       |
|     |     |          |     | 1         | 1        |       |
|     |     | i(x,t)=  |     | e (x−vt)− | e (x+vt) | (9.2) |
|     |     |          |     | f         | r        |       |
|     |     |          |     | Z         | Z        |       |
√
(L/C)
where Z = is the characteristic impedance of the transmission line, and
√
| v = 1/(L/C) | is the | velocity | of  | propagation. |     |     |
| ----------- | ------ | -------- | --- | ------------ | --- | --- |
| Example 9.1 |        |          |     |              |     |     |
An overhead line with two conductors having equal radii of 1cm and spacing
| between conductors |     | of 10 | meters | has L and | C given by2 |     |
| ------------------ | --- | ----- | ------ | --------- | ----------- | --- |
D
|     |     | L=4×10−71n |     |     | Henry/meter |     |
| --- | --- | ---------- | --- | --- | ----------- | --- |
0.779r
|     |     | =28.63×10−7 |     | Henry/meter |     |     |
| --- | --- | ----------- | --- | ----------- | --- | --- |
and
π×8.85×10−12
Farad/meter
C=n
1n(D/r)
|                |     | =4.025×10−12 |                | Farad/meter |     |     |
| -------------- | --- | ------------ | -------------- | ----------- | --- | --- |
| For this line, | the | velocity     | of propagation |             |     |     |
1
|     | (cid:31) |     |     |     | 2.95×108m/sec |     |
| --- | -------- | --- | --- | --- | ------------- | --- |
| v   | =        |     |     |     | =             |     |
(28.63×10−7×4.025×10−12)
| and the surge | impedance |     |     |     |     |     |
| ------------- | --------- | --- | --- | --- | --- | --- |
(cid:1)
(28.63×10−7)
843.3ohms
|     |     | Z = |     |     | =   |     |
| --- | --- | --- | --- | --- | --- | --- |
(4.02×10−12)

| 258 |     |     | Relaying applications | of traveling | waves |
| --- | --- | --- | --------------------- | ------------ | ----- |
Itshouldbenotedthatoftenthelineconstants(LandC)ofasingle-phaselineare
expressedin‘per-phase’ – i.e.betweeneachconductorandaneutralplanehalf-way
between the two conductors. In such a case, L becomes half and C becomes double
the values computed above, the velocity of propagation remains unchanged, and
the characteristic impedance becomes one-half of the value calculated above. This
per-phase procedure is useful because it leads directly to the per-phase concept in
a three-phase line. The Solution (9.2) of Equation (9.1) represents two traveling
wavefronts: e f traveling in the positive x direction (forward wave), and e r traveling
in the negative x direction (reverse wave). The voltage and currents at any point
on the line are made up of these forward and reverse components:
|     |     | e=e | +e  |     |     |
| --- | --- | --- | --- | --- | --- |
f r
|     |     | i=i | −i  |     | (9.3) |
| --- | --- | --- | --- | --- | ----- |
f r
The forward and reverse components of currents are related to corresponding
voltage components by the characteristic impedance Z. Figure 9.2 shows the rela-
tionships in a pictorial form for some assumed arbitrary shapes e f and e r . These
waves propagate with a velocity v, and the net voltage and current at any point on
the transmission line are given by superposition. As mentioned previously, we have
neglected the resistance of the transmission lines, as well as the dependence of L
upon the frequency of the voltage waves. Both of these effects are relatively minor
and cause attenuation and distortion of the waveforms as they propagate along the
line.3
Consider the occurrence of a fault as in Figure 9.2(b). The fault voltage, being a
portion of the power frequency sinusoid, is approximately constant (equal to −e ),
F
and it launches two waves, both (approximately) rectangular in shape and having
a magnitude of −e , moving away from the point of fault (see Figure 9.3). These
F
waves are reflected at any discontinuity (including at the terminal where the relay
is located). If k a is the reflection coefficient applicable at terminal a, the incoming
e
|     |     | f         |           | e r |     |
| --- | --- | --------- | --------- | --- | --- |
|     |     | Direction | Direction |     |     |
|     |     | of travel | of travel |     |     |
|     |     | i         | i         |     |     |
|     |     | f         | r         |     |     |
e
|     |            | e f             | r           |              |     |
| --- | ---------- | --------------- | ----------- | ------------ | --- |
|     | i          |                 |             | i            |     |
|     | f          |                 |             | r            |     |
|     |            | i               | i           |              |     |
|     |            | f               | r           |              |     |
|     | Figure 9.2 | Traveling waves | of voltages | and currents |     |

| Traveling waves | on single-phase | lines |     |     |     | 259 |
| --------------- | --------------- | ----- | --- | --- | --- | --- |
R
F
R
e r1 = k 1 e f1
|     | e   | e   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     | r1  | f1  |     |     | e   |     |
f1
−e
|     | i r1 | f i |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- |
f1
|     |     |     | i   | e f |     |     |
| --- | --- | --- | --- | --- | --- | --- |
f
Figure 9.3 Traveling waves created by a fault. The subscript f indicates the forward
traveling wave, and the subscript r indicates the reverse traveling wave with respect to the
| positive direction | of x |     |     |     |     |     |
| ------------------ | ---- | --- | --- | --- | --- | --- |
wave e causes a reflected wave moving in the forward (increasing x) direction,
r1
| with its accompanying |     | current: |      |     |     |     |
| --------------------- | --- | -------- | ---- | --- | --- | --- |
|                       |     | e        | =k e |     |     |     |
|                       |     | f2       | a r1 |     |     |     |
/Z
|     |     | i f2 | =k a i r1 = | e f2 |     | (9.4) |
| --- | --- | ---- | ----------- | ---- | --- | ----- |
i),
The voltages and currents at the termination are (e, t t where
|     |     | =e     | +e = (1+k  | )e   |     |       |
| --- | --- | ------ | ---------- | ---- | --- | ----- |
|     |     | e t r1 | f2         | a r1 |     |       |
|     |     | i =−i  | +i = −(1−k | )i   |     | (9.5) |
|     |     | t      | r1 f2      | a r1 |     |       |
The value of the reflection coefficient k depends upon the termination: if the ter-
a
mination is into another identical transmission line, there are no reflections, and k
a
+1,
is zero. If the termination is an open circuit, the reflection coefficient is and
at a short circuit the reflection coefficient is −1.0. For terminations into inductive
or capacitive circuits, the reflection coefficient is an operator (i.e. it is a function
of the Laplace variable s). If the termination is in other transmission lines, the
voltage e and the current i are launched as waves on these lines, to be reflected
| t   |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
further at their own terminations. The entire wave train, first launched by the fault,
thus travels up and down the network, fragmented by the reflections, until it is
dissipated through losses and the new steady state is established. When reflection
coefficients are real, a very convenient method of picturing this phenomenon is
through the Bewley lattice diagram.4 Consider the circuit shown in Figure 9.4. The
fault is at a distance d from terminal a. The propagation delays for the two seg-
a
ments are t (= d /v) and t (= d /v) respectively. At the fault point, the reflection
|     | a a | b b |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

| 260 |     |     |     | Relaying | applications | of traveling | waves |
| --- | --- | --- | --- | -------- | ------------ | ------------ | ----- |
|     |     |     |     |          | k            | k            |       |
|     |     |     |     |          | a            | b            |       |
e
|     |     |     |     |     | e   | f1  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
r1
e r1 τ
|     | τ   | τ   |     |     |     |     | b   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | a   | b   |     | τ   | τ   |     |     |
|     |     |     |     | a   | a e | e   |     |
|     |     |     |     |     | r2  | f3  |     |
(e + e )
|     | k   | k   | r1  | f2  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | a   | b   |     |     |     |     |     |
2τ
|     |     |      |          | a   | e   |     |     |
| --- | --- | ---- | -------- | --- | --- | --- | --- |
|     |     | −e   |          |     | r3  |     |     |
|     |     | F (e | + e + e  | )   |     |     |     |
|     |     |      | r1 f2 r3 |     |     |     |     |
3τ
a
Figure 9.4 Traveling waves and the Bewley lattice diagram for a two-terminal line
−1.0
coefficient is (since the fault is assumed to be a zero impedance fault).
Consequently,
|     |     | e   | =e = | −e  |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     | f1  | r1   | F   |     |     |     |
,e
|     |     | e f2 | =k a e r1 | r2 = k b | e f1 |     | (9.6) |
| --- | --- | ---- | --------- | -------- | ---- | --- | ----- |
|     |     | e    | =−e ,e    | = −e     |      |     |       |
|     |     | r3   | f2        | f3       | r2   |     |       |
These successive reflections are illustrated by the lattice diagram in Figure 9.4. The
voltages and currents at terminal a (as seen by a relay situated at that terminal) can
be obtained by adding all the components at terminal a in the lattice diagram. For
example, assuming k = −0.5, and −e = 1.0, the voltage and current waveforms
|     |     | a   | F   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
at terminals a,b, and F are as shown in Figure 9.5. If the power system behind the
relay location (terminal a) consists of other transmission lines with their own ter-
minations, they in turn will have similar lattice diagrams representing reflections at
their terminals. Reflections which return toward terminal a will once again impinge
upon it, and produce waves propagating on the faulted line. Consider one such line
a-c in Figure 9.6. Another line of infinite length is also assumed to exist in parallel
with line a-c. (The length of this line is assumed to be infinite in order to simplify
our discussion). The reflection coefficients at c and a for waves traveling on line
a-c are calculated as before. It is clear that the resulting waveforms at a are now
| far more | complex. |     |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- |
Sofarwehaveassumedthatthefaultvoltage−e isconstant.However,inreality,
F
it varies as a sine wave of power frequency. If a fault occurs at 100km from the
relay location, t a is about 0.33msec, and a 60Hz waveform may be considered to
be constant over a few travel times. For faults occurring at shorter distances, the
assumption of constancy of e F is closer to reality. In any case, it should be noted
that the steady state voltages and current at the relay location are sinusoidal, with
the current having a decaying DC offset whose magnitude depends upon the fault
incidence angle. The current and voltage at the relay location build up according
to the traveling wave considerations discussed so far and finally evolve into their
| respective | steady state | values. |     |     |     |     |     |
| ---------- | ------------ | ------- | --- | --- | --- | --- | --- |

| Traveling waves | on single-phase | lines |     |     | 261 |
| --------------- | --------------- | ----- | --- | --- | --- |
1.0
e a
t
i
a
t
|     |     | τ   | 3τ  | 5τ  |     |
| --- | --- | --- | --- | --- | --- |
|     |     | a   | a   | a   |     |
1.0
e
F
t
i
F
|     |     | 2τ  | 4τ  | t   |     |
| --- | --- | --- | --- | --- | --- |
2τ
|     |     | b a |     | a   |     |
| --- | --- | --- | --- | --- | --- |
Figure9.5 Voltageandcurrentwaveformsatlineterminalandfaultpointduetotraveling
waves
e
|     |     |     | a   | c a | F b |
| --- | --- | --- | --- | --- | --- |
e f1
|     | a   |     |     | e r1 |     |
| --- | --- | --- | --- | ---- | --- |
e τ
|     |     | b   |     |     | r2  |
| --- | --- | --- | --- | --- | --- |
τ b
|     |     | F   |     | a   |     |
| --- | --- | --- | --- | --- | --- |
e
|     |     |     |     | e f2 | f3  |
| --- | --- | --- | --- | ---- | --- |
c
|     |     |     |     | e r3 |     |
| --- | --- | --- | --- | ---- | --- |
add these components
to obtain e
a
Figure 9.6 Multiple reflections of waves created by the fault at F. One line at bus a is
assumed to be infinite in length for the sake of simplicity. The other line a-c is terminated
in a load impedance

| 262           |     |       |     |                |     | Relaying | applications | of traveling | waves |
| ------------- | --- | ----- | --- | -------------- | --- | -------- | ------------ | ------------ | ----- |
| 9.3 Traveling |     | waves |     | on three-phase |     | lines    |              |              |       |
Three-phase transmission lines consist of phases a, b and c, and a ground system
consistingofearthandgroundwires(iftheyarepresent).Asincaseofsingle-phase
transmission lines, the voltages and currents at a distance x from the line terminal
| are related | by partial |     | differential | equations |     |         |       |     |       |
| ----------- | ---------- | --- | ------------ | --------- | --- | ------- | ----- | --- | ----- |
|             |            |     |             |          |    |        |     |     |       |
|             |            |     | e            |           | L   | L L     | i     |     |       |
|             |            |     | ∂            | a         | s   | m m     | ∂ a   |     |       |
|             |            |     |             |          |    |        |     |     |       |
|             |            |     | e            | =         | − L | L L     | i     |     |       |
|             |            |     | ∂x           | b         | m   | s m     | ∂x b  |     |       |
|             |            |     | e            | c         | L m | L m L s | i c   |     |       |
|             |            |     |             |          |    |        |     |     |       |
|             |            |     | ∂ i          | a         | C s | C m C m | ∂ e a |     |       |
|             |            |     |             |          |    |        |     |     |       |
|             |            |     | i            | = −       | C   | C C     | e     |     | (9.7) |
|             |            |     | ∂x           | b         | m   | s m     | ∂x b  |     |       |
|             |            |     | i            |           | C   | C C     | e     |     |       |
|             |            |     |              | c         | m   | m s     | c     |     |       |
In Equation (9.7) we have assumed that the transmission line is transposed. The
self-inductance of each phase is L H/m, and the mutual inductance between any
S
twophases isL H/m.Similarly,thecapacitancebetweeneachphaseandgroundis
m
C S F/m, and the capacitance between any two phases is C m . Usually the quantities
L , L , C , C are expressed in terms of their positive and zero sequence values
| S m | S m |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(which are eigen values of the L and C matrices respectively):4
1
|     |     |     |     |     | (L  | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | L   | =   | +2L |     |     |     |
|     |     |     |     | s   | 3   | 0 1 |     |     |     |
1
|     |     |     |     |     | (L  | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | L   | =   | −L  |     |     |     |
|     |     |     |     | m   | 3   | 0 1 |     |     |     |
1
|     |     |     |     |     | (C  | )       |     |     |       |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | ----- |
|     |     |     |     | C s | =   | 0 +2C 1 |     |     | (9.8) |
3
1
|     |     |     |     |     | = (C | −C ) |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- |
|     |     |     |     | C m |      | 1 0  |     |     |     |
3
The corresponding circuit representation is shown in Figure 9.7. Note that
Figure 9.7(a) shows the conductor-to-conductor capacitances in a Wye connection,
whereas Figure 9.7(b) shows them in a delta connection. Equations (9.6) have a
traveling wave solution in modal quantities. Let 0, α ,β be the Clarke components
| of the voltages |     | and currents: |     |     |      |     |     |     |     |
| --------------- | --- | ------------- | --- | --- | ---- | --- | --- | --- | --- |
|                 |     |               |    |    |     |   |    |     |     |
|                 |     |               | i 0 |     | 1 1  | 1   | i a |     |     |
|                 |     |               |    |  1 |     |   |    |     |     |
|                 |     |               | iα  | =   | 2 −1 | − 1 | i   |     |     |
|                 |     |               |     |     | √    | √   | b   |     |     |
3
|     |     |     | iβ  |     | 0   | 3 − 3 | i   |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
c
|     |     |     |    |    |       |      |    |     |       |
| --- | --- | --- | --- | --- | ------ | ------ | --- | --- | ----- |
|     |     |     | e   |     | 1 1    | 1      | e   |     |       |
|     |     |     | 0   | 1   |        |        | a   |     |       |
|     |     |     |    |  = |  2 −1 | − 1  |    |     |       |
|     |     |     | eα  |     | √      | √      | e b |     | (9.9) |
3
|     |     |     | eβ  |     | 0   | 3 − 3 | e   |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
c

| Traveling waves | on three-phase |     | lines |     |     |     | 263 |
| --------------- | -------------- | --- | ----- | --- | --- | --- | --- |
L
s
L
m
|     |     | (C -C | )   |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- |
1 0 C
0
(a)
L s
L m
(C -C )/3
1 0
C
0
(b)
Figure 9.7 Multi-phase transmission line model. (a) Wye form. (b) Delta form
In this case, the solution of Equation (9.7) for voltages and currents at any point
| on the three-phase | line | is given | by   |      |      |     |     |
| ------------------ | ---- | -------- | ---- | ---- | ---- | --- | --- |
|                    |      |          | (x−v | t)+e | (x+v | t)  |     |
e =e
|     |     | 0   | f0    | 0    | r0   | 0   |        |
| --- | --- | --- | ----- | ---- | ---- | --- | ------ |
|     |     |     | (x−v  | t)+e | (x+v | t)  |        |
|     |     | eα  | =e fα |      | rα   |     | (9.10) |
|     |     |     |       | 1    |      | 1   |        |
|     |     |     | (x−v  | t)+e | (x+v | t)  |        |
|     |     | eβ  | =e fβ |      | rβ   |     |        |
|     |     |     |       | 1    |      | 1   |        |
i =i −i
|     |     | 0   | f0      | r0  |     |     |        |
| --- | --- | --- | ------- | --- | --- | --- | ------ |
|     |     | iα  | =i fα−i | rα  |     |     | (9.11) |
|     |     | iβ  | =i fβ−i | rβ  |     |     |        |
where
(cid:1)
|     |     |     | e    | e    |     | L   |     |
| --- | --- | --- | ---- | ---- | --- | --- | --- |
|     |     |     | f0 = | r0 = | Z = | 0   |     |
0
|     |     |     | i   | i   |     | C   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | f0  | r0  |     | 0   |     |
(cid:1)
|     |     |     | e fα | e rα |     | L   |        |
| --- | --- | --- | ---- | ---- | --- | --- | ------ |
|     |     |     | =    | =    | Z = | 1   | (9.12) |
1
|     |     |     | i fα | i rα |     | C   |     |
| --- | --- | --- | ---- | ---- | --- | --- | --- |
1
|     |     |     | e   | e   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | fβ  | rβ  |     |     |     |
|     |     |     | =   | =   | Z   |     |     |
|     |     |     | i   | i   | 1   |     |     |
|     |     |     | fβ  | rβ  |     |     |     |

| 264 |     |     |     | Relaying applications | of traveling | waves |
| --- | --- | --- | --- | --------------------- | ------------ | ----- |
and
1
|     |     |     | v = √ |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- |
0
L C
0 0
1
|     |     |     | v = √ |     |     | (9.13) |
| --- | --- | --- | ----- | --- | --- | ------ |
1
L C
1 1
In other words, phase voltages and currents should be viewed as being made up of
0,α,β components. Each of these components represents a mode of the propagation
Equation. The 0-mode has a characteristic impedance and velocity of propagation
| that are distinct | from those           | of the | α,β modes. |     |     |     |
| ----------------- | -------------------- | ------ | ---------- | --- | --- | --- |
| Example           | 9.2                  |        |            |     |     |     |
| Consider          | the L and C matrices | given  | below:     |     |     |     |
|                   |                     |        |           |     |     |     |
2.1 0.8 0.8
|     |    |         |             |     |     |     |
| --- | --- | ------- | ------------ | --- | --- | --- |
|     | L=  | 0.8 2.1 | 0.8 ×10−6H/m |     |     |     |
0.8 0.8 2.1
|     |     |        |        |                   |     |     |
| --- | ---- | ------ | ------ | ------------------ | --- | --- |
|     |      | 8.77   | −1.033 | −1.033             |     |     |
|     | C=  | −1.033 | 8.77   | −1.033  ×10−12F/m |     |     |
|     |      | −1.033 | −1.033 | 8.77               |     |     |
Then
|                   | 3.7×10−6H/m,      |            |     | 1.3×10−6H/m    |     |     |
| ----------------- | ----------------- | ---------- | --- | -------------- | --- | --- |
|                   | L =               |            |     | L =            |     |     |
|                   | 0                 |            |     | 1              |     |     |
|                   | = 6.704×10−12F/m, |            |     | = 9.8×10−12F/m |     |     |
|                   | C 0               |            |     | C 1            |     |     |
| The zero-sequence | mode              | parameters | are |                |     |     |
(cid:1)
L
|     |     | Z = | 0 = 742.9ohms |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- |
0
C
0
(cid:1)
1
|     |     | v = | =   | 2×108m/sec |     |     |
| --- | --- | --- | --- | ---------- | --- | --- |
0
L C
|         |              |      | 0 0        |     |     |     |
| ------- | ------------ | ---- | ---------- | --- | --- | --- |
| α       | β            |      |            |     |     |     |
| and the | and sequence | mode | parameters | are |     |     |
(cid:1)
L
1
|     |     | Z = | = 364.2ohms |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- |
1
C 1
(cid:1)
1
|     |     | v = | =   | 2.8×108m/sec |     |     |
| --- | --- | --- | --- | ------------ | --- | --- |
1
|     |     |     | L 1 C 1 |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- |

| Traveling       | waves on | three-phase | lines |            |     |     | 265 |
| --------------- | -------- | ----------- | ----- | ---------- | --- | --- | --- |
| 9.3.1 Traveling |          | waves       | due   | to faults5 |     |     |     |
Let the pre-fault voltages of phases a, b, and c be e , e , and e , respectively.
aF bF cF
−e −e
For a three-phasefault, the fault is represented by voltages −e aF , bF , cF at the
fault point. From Equations (9.8), the 0,α,β components of these voltages are given
| by (since | e + e | + e = | 0 at | any instant) |     |     |     |
| --------- | ----- | ----- | ---- | ------------ | --- | --- | --- |
|           | a     | b c   |      |              |     |     |     |
1
|     |     |     |     | (−e |     | )   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | e   | =   | −e  | −e  | = 0 |     |
|     |     | OF  | 3   | aF  | bF  | cF  |     |
1
|     |     |     |     | (−2e |       | )             |        |
| --- | --- | --- | --- | ---- | ----- | ------------- | ------ |
|     |     | eαF | =   | aF   | +e bF | +e cF = −e aF | (9.14) |
3
1
|     |     |     | =   | (−e +e | )   |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- |
|     |     | eβF |     | bF     | cF  |     |     |
3
The α and β components of voltages are launched as forward and reverse waves of
magnitude eαf , eαr , eβf , eβr . Their accompanying current waves are given by
|     |     |     |     | eαr, |     | eαf |        |
| --- | --- | --- | --- | ---- | --- | --- | ------ |
|     |     |     | iαr | =    | iαf | =   |        |
|     |     |     |     | Z    |     | Z   |        |
|     |     |     |     | 1    |     | 1   |        |
|     |     |     |     | eβr, |     | eβf |        |
|     |     |     | iβr | =    | iβf | =   | (9.15) |
|     |     |     |     | Z 1  |     | Z 1 |        |
(α,β)
As in the case of a single-phase transmission line, each mode now travels up
and down the line, and their travels can be catalogued by separate lattice diagrams
| as in Figure | 9.6. |     |     |     |     |     |     |
| ------------ | ---- | --- | --- | --- | --- | --- | --- |
For a b-c fault, the fault is defined by the boundary condition
e a =0
1
|     |     |     |     | e =− | e   |     | (9.16) |
| --- | --- | --- | --- | ---- | --- | --- | ------ |
|     |     |     |     | b    |     | bcF |        |
2
1
|     |     |     |     | e =+ | e   |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     | c    |     | bcF |     |
2
where e bcF is the pre-fault voltage between phases b and c. The above condition,
when substituted in the definition of Clarke components (Equation (9.9)) leads to
|     |     |     |     | e = | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |     |     |     | eα = | 0   |     | (9.17) |
| --- | --- | --- | --- | ---- | --- | --- | ------ |
1
|     |     |     |     | eβ = | √   | e bcF |     |
| --- | --- | --- | --- | ---- | --- | ----- | --- |
3
Similarly (see Problem 9.5), the modal waves launched by various types of faults
can be calculated. Table 9.1 lists the waves for the ten fault types possible on a
| three-phase | system. |     |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- | --- |

| 266 |     |     | Relaying | applications | of traveling | waves |
| --- | --- | --- | -------- | ------------ | ------------ | ----- |
0,α,β
Table 9.1 waves launched by faults on a three-phase transposed transmission line
| Fault type | e   |     | eα  |     |     | eβ  |
| ---------- | --- | --- | --- | --- | --- | --- |
0
1
| 3ph | 0   |     | −e  |     | −√ (e | −e )  |
| --- | --- | --- | --- | --- | ----- | ----- |
|     |     |     | aF  |     |       | bF cF |
3
|     |     |     | 1   |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- |
| ab  | 0   |     | − e |     | √   | e   |
|     |     |     |     | abF |     | abF |
|     |     |     | 2   |     | 2   | 3   |
1
| bc  | 0   |     | 0   |     | −√  | e   |
| --- | --- | --- | --- | --- | --- | --- |
bcF
3
|     |     |     | 1   |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- |
| ca  | 0   |     | − e |     | √   | e   |
|     |     |     | 2   | caF |     | caF |
2 3
|     | (e      | )    | (Z      | )e   | (Z    | )e      |
| --- | ------- | ---- | ------- | ---- | ----- | ------- |
|     | Z       | +e   | +Z      |      | −Z    |         |
| abg | − 0 aF  | bF   | − 1     | 0 aF | √ 0   | 1 aF    |
|     |         |      |         |      | 3(Z   | )       |
|     | Z 1 +2Z | 0    | Z 1 +2Z | 0    |       | +2Z     |
|     |         |      |         |      |       | 1 0     |
|     |         |      |         |      | (2Z   | )e      |
|     |         |      | Z e     |      |       | +Z      |
|     |         |      | + 0 bF  |      | −√ 1  | 0 bF    |
|     |         |      |         |      | 3(Z   | )       |
|     |         |      | Z 1 +2Z | 0    |       | 1 +2Z 0 |
|     | Z (e    | +e ) | Z (e +e | )    | (e    | −e )    |
| bcg | − 0 bF  | cF   | 1 bF    | cF   | − bF  | √ cF    |
|     | Z +2Z   |      | Z +2Z   |      |       | 3       |
|     | 1       | 0    | 1       | 0    |       |         |
|     | Z (e    | +e ) | (Z +Z   | )e   | (Z −Z | )e      |
|     | 0 aF    | cF   | 1       | 0 aF | 0     | 1 aF    |
| cag | −       |      | −       |      | √     |         |
|     | Z +2Z   |      | Z +2Z   |      | 3(Z   | +2Z )   |
|     | 1       | 0    | 1       | 0    |       | 1 0     |
|     |         |      | Z e     |      | (2Z   | +Z )e   |
|     |         |      | 0 cF    |      |       | 1 0 cF  |
|     |         |      | +       |      | −√    |         |
|     |         |      | Z +2Z   |      | 3(Z   | +2Z )   |
|     |         |      | 1       | 0    |       | 1 0     |
|     | Z e     |      | Z       | e    |       |         |
|     | 0       | aF   | 10      | aF   |       |         |
| ag  |         |      | −       |      |       | 0       |
|     | Z +2Z   |      | Z +2Z   |      |       |         |
|     | 0       | 1    | 0       | 1    |       |         |
√
|     | Z e     |     | Z e     |     |     | 3Z e  |
| --- | ------- | --- | ------- | --- | --- | ----- |
| bg  | 0       | bF  | 1       | bF  | −   | 1 bF  |
|     | Z 0 +2Z | 1   | Z 0 +2Z | 1   | Z 0 | +2Z 1 |
√
|     | Z e |     | Z e |     | 3Z  | e    |
| --- | --- | --- | --- | --- | --- | ---- |
|     | 0   | cF  | 1   | cF  |     | 1 cF |
cg
|     | Z +2Z |     | Z +2Z |     | Z +2Z |     |
| --- | ----- | --- | ----- | --- | ----- | --- |
|     | 0     | 1   | 0     | 1   | 0     | 1   |
0,α,β
Thus, every type of fault launches a set of waves at the point of a fault
inception.Thewavespropagatetowardsterminals,andarereflectedwithappropriate
reflection coefficients. In the case of unbalanced faults, the reflections at the fault
point are more complex: the wave of one type (0,α, or β) in general is reflected and
transmitted as waves of all three types. In other words, an unbalanced fault causes
coupling between various modes of propagation. The reflection and transmission
coefficient calculations are left as a problem for the reader (see Problem 9.7).

| Directional | wave relay |     |     |     |     |     | 267 |
| ----------- | ---------- | --- | --- | --- | --- | --- | --- |
It should also be noted that, although the characteristicimpedances and velocities
of propagation of the three modes are determined by the L and C matrices of
Equation (9.6), the definitions of the three modes (as for Clarke components) are
not unique. Other possibilities exist, the most common alternative definition being
| the Karrenbauer | transformation:6 |            |     |     |      |      |        |
| --------------- | ---------------- | ---------- | --- | --- | ---- | ---- | ------ |
|                 |                  |           |    |    |      |   |        |
|                 |                  | e          |     | 1   | 1 1  | e    |        |
|                 |                  | 0          |     | 1   |      | a    |        |
|                 |                  |           |    |    |      |   |        |
|                 |                  | e          | =   | 1   | −1 0 | e    | (9.18) |
|                 |                  | 1          |     | 3   |      | b    |        |
|                 |                  | e          |     | 1   | 0− 1 | e    |        |
|                 |                  | 2          |     |     |      | c    |        |
| 9.4 Directional |                  | wave relay |     |     |      |      |        |
As the waves created by faults travel in distinct directions (away from and towards
a fault point), it is possible to design a relay which depends upon the traveling
waves to determine the direction of the fault with respect to the relay location.
If two relays at the ends of a line detect a fault to be in the forward direction,
then the fault is in the zone of protection of both relays. This principle of relaying
(directional comparison) requires a communication channel between the two ends
to confirm that both relays see the fault in the forward direction.
Since a relay is located at the terminal of a transmission line, it would appear
that it sees waveforms that are affected by the discontinuity represented by the bus
through the reflection coefficients. As a matter of fact, the relays may be made to
see a specific traveling wave in a manner that is independent of the terminations.
Consider the ‘discriminant functions’ d and d associated with the forward and
|     |     |     |     | f   |     | r   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
reverse waves:6
d = e+Zi
f
|     |     |     |     | d = e−Zi |     |     | (9.19) |
| --- | --- | --- | --- | -------- | --- | --- | ------ |
r
where e and i are the modal voltages and currents (0,α, or β) at the relay location.
The relay treats the currents flowing into the line as positive. The forward current
wave i thus appears as positive to the relay, while the reverse current wave i
| f          |              |            |     |               |         |            | r      |
| ---------- | ------------ | ---------- | --- | ------------- | ------- | ---------- | ------ |
| appears to | be negative. | It follows |     | from Equation |         | (9.3) that |        |
|            |              | d =e+Zi    |     | = e           | +e +Z(i | −i )       |        |
|            |              | f          |     | f             | r       | f r        |        |
|            |              | =(e        |     | )+(e          |         | )          |        |
|            |              |            | +Zi |               | −Zi     |            | (9.20) |
|            |              |            | f   | f             | r       | r          |        |
|            |              | =e         | +Zi | =             |         |            |        |
|            |              |            | f   | f 2e          | f       |            |        |
=
| since e r | Zi r . Similarly, |     |     |         |     |     |     |
| --------- | ----------------- | --- | --- | ------- | --- | --- | --- |
|           |                   |     | d   | = e +Zi | =   | 2e  |     |
|           |                   |     | r   | r       | r   | r   |     |

| 268     |     |     | Relaying applications | of traveling | waves |
| ------- | --- | --- | --------------------- | ------------ | ----- |
| Example | 9.3 |     |                       |              |       |
The discriminant functions d and d at bus a of Figure 9.8 are shown in Figure 9.9.
f r
Note that the discriminant function d and d remain constant at 2e and 2e
|     |     |     | f r |     | f r |
| --- | --- | --- | --- | --- | --- |
respectively until the other reflections due to fault (at instants t ,t ...), or due
3 5
to reflections at bus c (at instants t ,t ...), cause a change in their values. If the
|     |     | 2   | 4   |     |     |
| --- | --- | --- | --- | --- | --- |
relay is not a discontinuity, only d r picks up at t 1 and d f must await reflections
| either at | the fault or at | bus c. |     |     |     |
| --------- | --------------- | ------ | --- | --- | --- |
|           |                 | s      | a F |     |     |
X
Figure 9.8 System one line diagram for traveling wave considerations
d
|     | f   |     | d r |     |     |
| --- | --- | --- | --- | --- | --- |
|     |     | t   |     | t   |     |
Figure9.9 DiscriminantfunctionsfortherelayatbusaforthesystemshowninFigure9.8.
Waves traveling towards the relay are termed reverse waves since the relay is assumed to
| be looking | into the line |     |     |     |     |
| ---------- | ------------- | --- | --- | --- | --- |
If the fault is behind the relay, d will pick up (i.e. become non-zero) first, and
f
d will pick up later due to successive reflections at the fault or at bus c. Thus we
r
may determine the direction of the fault according to the following logic:7
| (i) if d | picks up first, | the fault is behind | the relay |     |     |
| -------- | --------------- | ------------------- | --------- | --- | --- |
f
(ii) ifd picksupfirstorsimultaneouslywithd ,thefaultisintheforwarddirection.
| r   |     |     | f   |     |     |
| --- | --- | --- | --- | --- | --- |
The relationship (ii) above is maintained for a period equal to twice the travel
time between the forward fault and the relay location. It would appear that for a
near fault the duration of validity could be very brief since the travel time from the
fault would be very short. However, it has been observed6 that, for near faults, the
quick successive reflections build up the discriminant functions d and d d still
|     |     |     |     | f   | r r |
| --- | --- | --- | --- | --- | --- |
maintaining the required relationship (ii). The details are left as an exercise for the
| reader (see | Problem 9.8). |     |     |     |     |
| ----------- | ------------- | --- | --- | --- | --- |
Another concern with discriminant functions of Equation (9.20) is that, for faults
that occur at near zero voltage (i.e. when the pre-fault voltage is going through

Traveling wave distance relay 269
a zero), e and e are both very small. The traveling waves (and therefore the
f r
discriminants) are replicas of the (negative) pre-fault voltages. As time goes on,
these discriminant functions acquire the shape of a power frequency sine wave.
Recall that, although a sine wave is small in the beginning, its derivative there is
quite large, and one could construct modified discriminant functions6
(cid:1)
(cid:14) (cid:15)
1 d 2
d(cid:1) = d2+ (d )
f f ωdt f
(cid:1)
(cid:14) (cid:15)
1 d 2
d(cid:1) = d2+ (d ) (9.21)
r r ωdt r
Theseprimeddiscriminant functions areindependent of thefaultincidence angle.
Other versions of the traveling wave algorithm consider the fault trajectory in
the (e-Ki) plane, where K is a constant. Note that a constant discriminant function
given in Equation (9.19) defines a straight line in this plane, when K is set equal
to the characteristic impedance of the line. A decision about the direction of a fault
can be based upon whether the (e-Ki) trajectory crosses appropriate thresholds in
the (e-Ki)
plane.8,9
The constant K may be set equal to Z, the source impedance of
the network. In this case the current is shifted in phase by Z (the source impedance
being a complex quantity),10–12 so that eand Ki arein phase or inphase opposition
with each other depending upon whether the fault is in front of or behind the relay
location.Notethattheselatter(andsomeother)relays13 areinfactpowerfrequency
relays operating on incremental quantities, rather than traveling relays. When K is
made equal to Z, it is once again a mimic circuit used to suppress the DC offset
in the current and produce a phase shift in the current waveform. The traveling
wave components then become parasitic effects which must be ignored, and actual
relaying decisions are based upon fundamental frequency voltages and currents.
9.5 Traveling wave distance relay
Consider a single-phase transmission line with a relay at bus a and a fault at bus F
as shown in Figure 9.8. As explained in Section 9.2, the occurrence of the fault sets
up traveling waves which travel away from the fault. The waves are reflected at all
discontinuities according to the lattice diagram of Figure 9.4. If we were to find a
wave that went from the relay location towards the fault and started a timer as the
wave went through the relay location, the wave would be reflected by the fault and
return to the relay location. When the wave crosses the relay location in the reverse
direction, the timer is stopped. The timer reading would then correspond to twice
the travel time needed to traverse the distance to the fault.
Since the velocity of propagation of the wave is known, the distance to the fault
can be calculated. If we assume the distance sa to be about half of af in Figure 9.8,

270 Relaying applications of traveling waves
s a F
e
a
e
r1
t
1 e r1 t 1 t 2 t 3 t 4` t
t e f2 t
2
t 3 Z i a
e
r2
e
t f3
4
d
f
(a)
t
d
r
t
(b)
Figure 9.10 Voltage, current and discriminant functions for a fault. (a) System diagram
and the lattice diagram. (b) Waveforms. The reverse discriminant function arrives at the
relay location first because it is associated with the wave traveling towards the relay from
the fault
a fault with zero impedance, and a source of infinite short circuit capacity at bus s,
the traveling waves as seen by the relay can be obtained from the lattice diagram
shown in Figure 9.10. At time t , a wave reflected at the source behind the relay
2
crosses the relay and goes towards the fault. At time t this wave is reflected by the
3
fault and crosses the relay location in the reverse direction. Consequently, (t – t )
3 2
is twice the travel time between the relay location and the fault. The forward and
reverse discriminant functions for this case are also plotted in Figure 9.10. The
relay must be allowed to start its timer at t when the pickup of d indicates the
2 f
arrival of a wave after (or simultaneously) d has picked up. This, as was stated
r
in the last section, indicates a forward fault. Once the timer has started, it must
be stopped when d shows a waveform similar to the one which crossed the relay
r
location at t .
2
The square wave shapes shown in Figure 9.10 result from assumed zero
impedance in the fault and the source. If the source is inductive, the reflected
waves at the source will be exponential functions as shown in Figure 9.11. The
effect of fault arc resistance (when it is present) is to increase the voltage reflection
coefficient from −1.0 corresponding to a direct short-circuit to a value somewhat
closer to zero depending upon the resistance in the arc.

| Traveling | wave distance | relay |     |     |     | 271 |
| --------- | ------------- | ----- | --- | --- | --- | --- |
e
a
t
d
f
t
d
r
t
Figure 9.11 Discriminant wave functions for inductive termination
W
|     |     | d   | f   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
f
d r
W r
1
2
3
4
5
φ(τ)
5
|     |     | 1   | 2 3 4 |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- |
Figure 9.12 Discriminant functions and their cross-correlation functions
One could realize the starting and stopping operations of the timer by actually
using a clock, in which case adequate triggering mechanisms must be built in.
Alternatively,14,15
|     | one | could store | the waveform | of d around | the instant | t for a |
| --- | --- | ----------- | ------------ | ----------- | ----------- | ------- |
|     |     |             |              | f           |             | 2       |
timewindoww f spanningt 2 asshowninFigure9.12.Thecross-correlationfunction
of d (taken over the window w ) and d (taken over a winder w ) of equal duration
| f   |     |     | f r |     | r   |     |
| --- | --- | --- | --- | --- | --- | --- |
τ
at progressively increasing time delays may be used as an algorithmic measure
| for finding | the interval | (t – t ): |     |     |     |     |
| ----------- | ------------ | --------- | --- | --- | --- | --- |
3 2
t(cid:4)=wf
|     |     | ϕ(τ)= | (t)d | (t+τ)dt |     |        |
| --- | --- | ----- | ---- | ------- | --- | ------ |
|     |     |       | d    |         |     | (9.22) |
|     |     |       | f r  |         |     |        |
t=0

| 272 |     |     |     | Relaying | applications of traveling | waves |
| --- | --- | --- | --- | -------- | ------------------------- | ----- |
As has been pointed out,14 the DC component of d and d over windows w and
|     |     |     |     | f   | r   | f   |
| --- | --- | --- | --- | --- | --- | --- |
ϕ(τ)
w r produces a large (and variable) bias in which would mask the effect we
are seeking. It is therefore appropriate to modify Equation (9.22) by removing the
| mean of | d f and d | r from the cross-correlation |     | function. | Let |     |
| ------- | --------- | ---------------------------- | --- | --------- | --- | --- |
t(cid:4)=wf
1
|     |     |     | d = | d (t)dt |     |     |
| --- | --- | --- | --- | ------- | --- | --- |
|     |     |     | f   | f       |     |     |
w
f
t=0
t=(cid:4)wr+τ
1
|     |     |     | (τ)= | (t)dt |     |     |
| --- | --- | --- | ---- | ----- | --- | --- |
|     |     | d   |      | d     |     |     |
|     |     |     | r w  | f     |     |     |
r
t=0
ϕ(cid:1)τ
| A new | cross-correlation | function | is defined |     |     |     |
| ----- | ----------------- | -------- | ---------- | --- | --- | --- |
t=(cid:4)wf=wr
|     |     |             |       | #           | $      |        |
| --- | --- | ----------- | ----- | ----------- | ------ | ------ |
|     |     | ϕ(cid:1)τ = | (d −d | ) d (t+τ)−d | (τ) dt | (9.23) |
|     |     |             | f f   | r           | r      |        |
t=0
|     |     | ϕ(cid:1)(τ) |     |     |     | τ   |
| --- | --- | ----------- | --- | --- | --- | --- |
Both the function and its sampled data version become maximum when
becomes equal to (t – t ). The location of the fault can now be easily determined.
|     |     | 3 2 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Methodstofindthedistancetothefaultfromtravelingwavesarefraughtwithdif-
ficulty.Inathree-phasesystem,multi-modepropagationexists.Groundmodewaves
are subject to severe attenuation and distortion of wave shape as the waves propa-
gate along the transmission lines. Unbalanced faults and faults through impedance
further complicate matters by coupling different modes at the fault point. When
fault inception angles are such that traveling waves are small in magnitude, the
ϕ(cid:1)(τ)
maximum of the cross-correlation function is often lost in the measurement
noise. All these considerations make a traveling wave distance relay somewhat dif-
ficult to set. It could well be that it must be used in conjunction with other more
| conventional     | relaying | schemes. |              |     |     |     |
| ---------------- | -------- | -------- | ------------ | --- | --- | --- |
| 9.6 Differential |          | relaying | with phasors |     |     |     |
Differential relaying is the preferred protection method for power apparatus. We
have covered this principle in the discussion of transformer, generator, and bus
protection in Chapter 6. Differential protection of cables and transmission lines is
a relatively new subject, which we will consider in this section.
Differentialrelayingrequiresthatinformation(usuallycurrents)fromallterminals
ofthezonebeingprotectedbecombinedwitheachothertoformdifferentialcurrent.
If this exceeds a preset value, a fault may be said to exist inside the zone of
protection. Such a computation must be made at each terminal, and consequently
a communication channel must be assumed to exist between all terminals of the

| Differential | relaying | with | phasors |     |     |     | 273 |
| ------------ | -------- | ---- | ------- | --- | --- | --- | --- |
I
|     | 1   |     |     | I 2 |     |       |     |
| --- | --- | --- | --- | --- | --- | ----- | --- |
|     |     |     |     |     |     | I 1 I |     |
2
I 3
|     | 1   |     |     |     |     | 1   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- |
2
3
Figure 9.13 Differential relaying of a transmission line and the necessarycommunication
paths. Either a two-terminal line as shown on the left, or a multi-terminal line as on the
| right, | can be protected |     | by this | scheme |     |     |     |
| ------ | ---------------- | --- | ------- | ------ | --- | --- | --- |
protected line or cable. Figure 9.13 shows the communication channels needed for
differential protection of two- and multi-terminal transmission lines.
We may begin with a differential protection based upon phasors. The phasors
may be calculated from fractional cycle data, as discussed in Chapter 2. If I i is
the current phasor at terminal i (reference direction is positive when the current is
flowing into the zone of protection), the differential currents may be defined in the
| usual | manner: |     |     |     | (cid:11) | (cid:11) |     |
| ----- | ------- | --- | --- | --- | -------- | -------- | --- |
(cid:11)(cid:5) (cid:11)
(cid:11) (cid:11)
|     |     |     |     | |I  | | = (cid:11) | I(cid:11) | (9.24) |
| --- | --- | --- | --- | --- | ------------ | --------- | ------ |
|     |     |     |     | d   | (cid:11)     | i(cid:11) |        |
i
A single restraining current may be constructed by averaging the magnitudes of
all terminal currents, or one restraining current for every pair of terminals may be
constructed in order to maintain uniform sensitivity when one of the terminals of a
multi-terminallineis out of service. Thereader may refertoChapter 5,where these
considerations areexplained inthe context of multi-winding transformer protection.
It isclear that all the currentsin Equation (9.24) must be on acommon reference,
so that synchronized sampling clocks as described in Chapter 8 must be used.
It is also possible to achieve synchronization through pre-fault load flow on the
lines.16
transmission Assume that voltages and currents at each terminal of the
transmission line are measured in the period immediately before the occurrence of
a fault. All phasors withina stationcan certainly be synchronized. Thus the phasors
I andE areonthesamereference, but their referencemaybe atacertainunknown
i i
δ
angle with respect to a system-wide common reference. If the transmission line
i
is represented by a bus admittance matrix Y as shown in Figure 9.14, the bus
B
| injection | currents | and | voltages | are related |     | by:         |        |
| --------- | -------- | --- | -------- | ----------- | --- | ----------- | ------ |
|           |          |     |          |            |    |           |        |
|           |          |     |          | ejδ         |     | ejδ         |        |
|           |          |     |          | I           | 1   | E 1         |        |
|           |          |     |          |  1a        |    |  1a       |        |
|           |          |     |          | I ejδ      | 1   | E ejδ 1    |        |
|           |          |     |          | 1a          |    | 1a         |        |
|           |          |     |          |  δ         |    |  δ        |        |
|           |          |     |          |  I e j     | 1  |  E e j 1  |        |
|           |          |     | I =      | 1 c         | =   | Y 1 c       | (9.25) |
|           |          |     | B        |  j δ       |    | B  j δ    |        |
|           |          |     |          |  I e       | 2  |  E e 2    |        |
|           |          |     |          |  2 a       |    |  2 a      |        |
|           |          |     |          | I ejδ       | 1   | E ejδ 2     |        |
|           |          |     |          | 1b          |     | 2b          |        |
|           |          |     |          | ejδ         |     | ejδ         |        |
|           |          |     |          | I           | 2   | E 2         |        |
|           |          |     |          | 2c          |     | 2c          |        |

| 274 |     |           |     |     |            | Relaying | applications | of traveling | waves |
| --- | --- | --------- | --- | --- | ---------- | -------- | ------------ | ------------ | ----- |
|     |     | Station 1 |     |     |            |          |              | Station 2    |       |
|     |     |           | E   | I   |            |          | I E          |              |       |
|     |     |           | 1a  | 1a  |            |          | 2a 2a        |              |       |
|     |     | a         |     |     |            |          |              | a            |       |
|     |     |           | E   | I   | Admittance |          | I E          |              |       |
|     |     |           | 1b  | 1b  |            |          | 2b 2b        |              |       |
|     |     | b         |     |     | Matrix     |          |              | b            |       |
|     |     |           | E   | I   | Y          |          | I E          |              |       |
|     |     |           | 1c  | 1c  | B          |          | 2c 2c        |              |       |
|     |     | c         |     |     |            |          |              | c            |       |
reference for voltages
G
Figure 9.14 Two-terminal transmission line representation for synchronization of phasors
| with pre-fault |     | load flow |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
δ
1 may be assumed to be zero without loss of generality. Once could thus solve
Equation (9.25) as a redundant set of equations for a single unknown δ . For an
2
n-terminal line, the n-1 unknown angles could be found in a similar manner. The
details may be found in the literature.16 Once the unknown angles from a common
referencearedetermined,theseanglesaretobeheldconstantfordifferential-current
calculationsduringafaultperiod.Whennotransientisdetected,thesynchronization
is carried out continuously – perhaps as frequently as once a cycle.
When charging currents are significant, the differential current is no longer zero
for a no-fault condition. Thus in the case of long transmission lines or cables, the
differential relay must be made insensitive in order to accommodate the charging
current. An alternative method is to calculate a correction to the differential current
due to the charging currents. If we assume a two-terminal multi-phase π-section
representation of a transmission line, the charging currents I si at the terminal I are
| given by |     |     |     |    |    |    |   |     |        |
| -------- | --- | --- | --- | --- | --- | --- | ---- | --- | ------ |
|          |     |     |     | I   | sia |     | E ia |     |        |
|          |     |     |     |    |    |    |   |     |        |
|          |     |     | I   | = I | =   | Y   | E    |     | (9.26) |
|          |     |     | si  |     | sib | S   | ib   |     |        |
|          |     |     |     | I   |     |     | E    |     |        |
|          |     |     |     |     | sic |     | ic   |     |        |
whereY S istheshuntcapacitiveadmittancematrixatbusi.Thus,insteadofsending
I from terminal I to all other terminals, a compensated current I(cid:1)
| i   |     |     |     |     |              |      |     | i   |        |
| --- | --- | --- | --- | --- | ------------ | ---- | --- | --- | ------ |
|     |     |     |     |     | I(cid:1) = I | −I   |     |     | (9.27) |
|     |     |     |     |     | i            | i si |     |     |        |
is sent to the remote terminals. For no faults or external faults, the differential
I(cid:1)
current calculated with is zero even in the presence of charging currents. A
i
somewhat modified method for computing I(cid:1) must be used when dealing with a
i
multi-terminal transmission line, since the charging currents at the tap points must
also be reckoned with. This problem is left as an exercise at the end of this chapter.
| Additional | details | may | be  | found in | the literature.17 |     |     |     |     |
| ---------- | ------- | --- | --- | -------- | ----------------- | --- | --- | --- | --- |
It is clear that the differential protection principle described by Equations (9.26)
and(9.27)requiresvoltagemeasurement.Thismaynotalwaysbeavailableatevery

| Traveling wave | differential | relays |     |     |     |     |     | 275 |
| -------------- | ------------ | ------ | --- | --- | --- | --- | --- | --- |
terminal. One must either abandon the idea of compensation at all terminals, or use
it at those terminals where it is available. In any case, inaccuracies introduced by
such approximation must be allowed for by an appropriate de-sensitization of the
| differential  | relay. |                   |     |        |     |     |     |     |
| ------------- | ------ | ----------------- | --- | ------ | --- | --- | --- | --- |
| 9.7 Traveling |        | wave differential |     | relays |     |     |     |     |
As explained in earlier sections, a fault launches traveling waves, which ultimately
(after successive reflections and attenuations) produce standing wave patterns (i.e.
steady state conditions) on the transmission lines which are the phasor voltages and
currents used in the relaying principle described in Section 9.7. It is also possible
to define a differential relaying principle which may be based upon the traveling
waves.18,19
τ,
If the travel time between two ends of a line is and if at both ends of a line a
positive direction for forward propagation is into the zone of protection, it is clear
that the forward wave at a terminal becomes a reverse wave at the other terminal
| τ.  |     |     |     |     |     |     |     | +τ) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
in time Thus d at time t at terminal 1 in Figure 9.13 becomes d at (t at
|             |     | f   |     |         |       |     | r   |        |
| ----------- | --- | --- | --- | ------- | ----- | --- | --- | ------ |
| terminal 2: |     |     |     |         |       |     |     |        |
|             |     |     | d   | (t) = d | (t+τ) |     |     | (9.28) |
|             |     |     | f1  |         | r2    |     |     |        |
Equation (9.28) holds aslong as thereisno fault on the transmissionline. Recall-
ing that the discriminant functions defined by Equation (9.18) may be modified to
| the following | form: |     |     |     |          |     |          |     |
| ------------- | ----- | --- | --- | --- | -------- | --- | -------- | --- |
|               |       |     |     |     | (cid:14) |     | (cid:15) |     |
1
|     |     | d (t) = e | (t)+Zi | (t) | = Z i | (t)+ | e (t) | (9.29) |
| --- | --- | --------- | ------ | --- | ----- | ---- | ----- | ------ |
|     |     | f1        | 1      | 1   |       | 1    | 1     |        |
Z
and similarly
|     |     |     |     | (cid:14) |     |     | (cid:15) |     |
| --- | --- | --- | --- | -------- | --- | --- | -------- | --- |
1
|     |     | d (t+τ) | = Z | −i (t+τ)+ |     | e (t+τ) |     | (9.30) |
| --- | --- | ------- | --- | --------- | --- | ------- | --- | ------ |
|     |     | r2      |     | 2         |     | 2       |     |        |
Z
leaving the common factor Z out since it is a constant, one could construct a
differential current at the two terminals of a transmission line:
|     |     | (cid:14) |     |     |     |     | (cid:15) |     |
| --- | --- | -------- | --- | --- | --- | --- | -------- | --- |
1
|     |     | i = i (t)−i |     | (t+τ)+ | e (t)−e | (t+τ) |     | (9.31) |
| --- | --- | ----------- | --- | ------ | ------- | ----- | --- | ------ |
|     |     | d1 1        | 2   |        | 1       | 2     |     |        |
Z
1
|     |     | = {i (t+τ) |     | −i (t)}+ | {e  | (t−τ)−e | (t)} |        |
| --- | --- | ---------- | --- | -------- | --- | ------- | ---- | ------ |
|     |     | i d2 2     | 2   | 1        |     | 2       | 1    | (9.32) |
Z
If current and voltage samples at terminals 1 and 2 are taken τ seconds apart, the
differentialcurrentsi andi canbecomputedsimplyifthesamplesareexchanged
|     |     | d1 d2 |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- |
between the two terminals. As before, tolerances must be set for residual i which
d
may exist during external faults due to errors in the measurement process. Thus a

| 276 |     |     |     |     |     | Relaying applications |     | of traveling | waves |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | ------------ | ----- |
percentage differential relaying principle should be used, although the percentage
slope would be very small for a well designed data acquisition system.
In a three-phase system, multi-mode propagation must be considered. Thus
0,α,β differential currents must be evaluated and used separately. Usually the
zero-sequence characteristic impedance and velocity of propagation are signifi-
cantly different from the α and β mode parameters, as explained in Section 9.3.
Consequently, samples at the two terminals would have to be taken with delays
| τ   | τ   | τ   | τ   |     |     |     | α,β |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of 0 and 1 , where 0 and 1 are travel times of the 0 and modes respectively.
This would lead to a very complex sampling process, and an alternative might be
to use identical parameters for all the modes, and accept larger values of i and
d1
i for external faults. Yet another simplification may be to take samples at a fixed
d2
.18,19
delay (say τ ), and then use interpolation to determine samples τ
|     | 1   |     |     |     |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
It should be recalled that the steady state (phasor) solutions of the traveling
wave Equation lead to standing waves – made up of one traveling forward and
anotheroneinthereversedirection.Thus,whensteadystateconditionsarereached,
Equations (9.31) and (9.32) are equivalent to Equation (9.27). Verification of this
| is left as | an exercise | for        | the reader | (see  | Problem | 9.11).         |     |     |     |
| ---------- | ----------- | ---------- | ---------- | ----- | ------- | -------------- | --- | --- | --- |
| 9.8 Fault  | location    |            |            |       |         |                |     |     |     |
| 9.8.1      | Impedance   | estimation |            | based |         | fault location |     |     |     |
Although the transmission line protection algorithms discussed in Chapter 3 use
estimates of the fault location in making relaying decisions, these estimates need
only beaccurateenough todeterminewhether thefaultisintheappropriate zone of
protection.Moreaccurateestimatesofthefaultlocationaredesirableforinspection,
maintenance,andrepairoftheactualfault.Foralongtransmissionline,forexample,
an error in fault location of a few miles may be acceptable for a relaying decision
but would represent a long walk in rough terrain. While analog techniques for fault
reported,21
location have been the area of fault location represents another active
areaofalgorithmdevelopment.Afirststepinproducingamoreaccurateestimateof
faultlocationfromarelayingalgorithmistoincreasethedatawindowsignificantly.
As seen in Section 4.5, the accuracy of the estimate increases with the length of
the window. A longer data window does not completely solve the problem in the
| presence | of fault | resistance, | however. |     |     |     |     |     |     |
| -------- | -------- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
The difficulty produced by fault resistance can be appreciated by examining
Figure 9.15(a). The Figure shows a single-phase one-line diagram of a fault with
resistance R at a distance k of the line with line impedance Z connected between
f
sources with The´venin impedances of Z and Z respectively. The relationship
|         |             |     |             |     | S        | R            |     |     |        |
| ------- | ----------- | --- | ----------- | --- | -------- | ------------ | --- | --- | ------ |
| between | the current | I   | and voltage | V   | measured | by the relay | is  |     |        |
|         |             |     |             | V   | = kZI+I  | R            |     |     | (9.33) |
f f

| Fault | location |     |     |        |     |     |       |        | 277 |
| ----- | -------- | --- | --- | ------ | --- | --- | ----- | ------ | --- |
|       |          | kZ  |     | (1−k)Z |     |     | kZ    | (1−k)Z |     |
|       |          | I   |     |        |     |     | ∆I    |        |     |
|       | Z        |     |     |        |     |     | Z     |        |     |
|       | S        | +   |     |        | Z R |     | S     | I      | Z R |
|       |          |     |     |        |     |     | + R f | f      |     |
|       |          | V − | R   | I f    |     |     | ∆V    |        |     |
|       |          |     | f   |        |     |     | −     | −      |     |
|       | V        |     |     |        | V   |     |       |        |     |
|       | S        |     |     |        |     | R   |       | V 0    |     |
+
|     |     |     | (a) |     |     |     |     | (b) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 9.15 One line diagram of a faulted line. (a) The post-fault model. (b) The incre-
mental model
where I is the current through the fault resistance. The current I includes contri-
|     | f   |     |     |     |     |     |     | f   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
butions from both ends of the line and is unknown to the relay. If the current I f is
| in  | phase | with the | current | I, dividing | (9.33) | by  | I gives |     |     |
| --- | ----- | -------- | ------- | ----------- | ------ | --- | ------- | --- | --- |
V
kZ+γR
|     |     |     |     |     | =   |     |     |     | (9.34) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
f
I
where γ = I /I is real. The imaginary part of the computed impedance is correct
f
| and | can | be used | for fault | location. |     |     |     |     |     |
| --- | --- | ------- | --------- | --------- | --- | --- | --- | --- | --- |
The phase relationship will be true if the source at the remote end makes no
contribution to I , or for specific values of V and Z . In general, however, γ is
|     |     |     | f   |     |     |     | R R |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
not real and Equation (9.34) has errors in both the real and imaginary parts. Some
additional information about the system must be used to resolve the uncertainty.
For example, information from the remote end could be used to determine I and
f
Equation (9.33) could be multiplied by the conjugate of I f to yield:
Imag{V×I∗}
f
|     |     |     |     | k = |     |     |     |     | (9.35) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
Imag{Z×I×I∗}
f
I∗
since I R is real. The requirement of communication between the two ends is a
|     | f   | f f |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
limitation, and a number of techniques for accurate fault location using information
from only one end of the line have been suggested.21–25 All of these techniques
take advantage of the additional information provided by the pre-fault currents and
| voltages |     | seen by | the relay. |     |     |     |     |     |     |
| -------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
If we let I and V denote the pre-fault value of current and voltage at the relay
|           |     | p         | p        |     |        |              |              |     |     |
| --------- | --- | --------- | -------- | --- | ------ | ------------ | ------------ | --- | --- |
| terminals |     | in Figure | 9.15(a), | and | define | (cid:1)I and | (cid:1)V as: |     |     |
(cid:1)I = I−I
p
|     |     |     |     |     | (cid:1)V = | V−V |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
p
then the circuit in Figure 9.15(b) describes the relationship between the incremental
(cid:1)
quantities. The quantities can be computed by subtracting the stored pre-fault

| 278 |     |     | Relaying applications | of traveling | waves |
| --- | --- | --- | --------------------- | ------------ | ----- |
values from the post-fault values. A similar diagram is obtained if the transmis-
sion line is described by the telegraph equation Equation (9.1).21–24 The use of a
distributed model of the line seems unnecessary for reasonable length lines. If the
current (cid:1)I is assumed to be in phase with I , Equation (9.36) can be multiplied by
f
|               | (cid:1)I | obtain21 |     |     |     |
| ------------- | -------- | -------- | --- | --- | --- |
| the conjugate | of       | to       |     |     |     |
Imag{V×(cid:1)I∗}
|     |     | k = |     |     | (9.36) |
| --- | --- | --- | --- | --- | ------ |
Imag{Z×I×(cid:1)I∗}
Similar expressions are obtained for the distributed line model in a form that is
appropriate for Fourier23 or Laplace24 transform methods. The solution of the non-
linear algebraic Equations for k, I , and R using the Newton-Raphson Method
f f
proposed.22
has also been The use of a current distribution factor which relates the
incremental positivesequence current tothefaultcurrent hasalsobeensuggested.25
| 9.8.2 | Fault location | based on traveling | waves |     |     |
| ----- | -------------- | ------------------ | ----- | --- | --- |
When a fault occurs on a transmission line, it induces step wave changes in volt-
ages and currents which propagate towards the ends of the transmission line as
discussed in Sections 9.2 and 9.3. Consider a single phase transmission line shown
in Figure 9.16(a). A fault at a distance x from one terminal will produce traveling
waves which travel in both directions, arriving at instants T and T respectively
1 2
at the two terminals. If the arrival of the waves is identified on a common time
reference (in this case a GPS time signal), then knowing the difference between T
1
and T 2 and the velocity of propagation the distance to the fault can be estimated by
L/2−v(T )
|     |     | x = | 1 −T 2 |     | (9.37) |
| --- | --- | --- | ------ | --- | ------ |
x
0,α,β waves
x
are launched by
| T   |     |     |     | the fault |     |
| --- | --- | --- | --- | --------- | --- |
1
T 2
|     |     | T 2 -T 1 |     | Each of the  |     |
| --- | --- | -------- | --- | ------------ | --- |
0,α,β waves
|     |     | x = L/2 −v(T −T |     | produces three  |     |
| --- | --- | --------------- | --- | --------------- | --- |
2 1 )/2
components
at each
discontinuity
Beweley Diagram
(a)
(b)
Figure 9.16 Traveling waves generated by a transmission line fault. (a) Waves on
| single-phase | line and | (b) Waves on three-phase | line |     |     |
| ------------ | -------- | ------------------------ | ---- | --- | --- |

Other recent developments 279
The lattice diagram of wave propagation is commonly referred to as ‘Bewley
Diagram’. On a two conductor line the velocity of propagation is very nearly equal
to the speed of light, and knowing the length of the line L, the fault location can
be determined.
For a three-phase line, as discussed in Section 9.3, there are three modes of prop-
agationlaunchedbyafault:0,α,andβ.Thelattertwowavespropagateatthespeed
of light, while the 0 wave propagates at a slower speed (approximately 70% the
speedof lightfor most overheadlines).Eachwave,upon reachingthelineterminal,
produces three modes of reflected waves, and the multiplicity of propagating waves
soon make the wave arrival detection quite difficult. It is therefore necessary to
determine the arrival of first of the α, and β waves in order to determine the fault
location.Ithasbeenfoundinpracticethatcurrentwavesareeasiertodetectthanthe
voltagewaveswhenthevoltagetransducersmaybecapacitivevoltagedividers.27,28
Also, phase currents are converted to α, and β currents by using Equation (9.9) and
discriminant functions (see Equation (9.19)) are used to isolate arriving waves from
the terminal current signals. It has been reported in references 27 and 28 that the
fault location performance of such devices are excellent. The reader should consult
those references for additional information.
9.9 Other recent developments
Many recent developments have a direct bearing on computer relaying. We will
consider some of these developments now.
The fiber optic communication networks have been mentioned several times.
This technology permits very high data transmission rates (in several megabits per
second) and can be used for protection as well as for other communication needs.
Traditionally,protectiontaskshavedemandedanindependentcommunicationchan-
nel. In the case of the fiber optic links, a separate fiber within a bundle dedicated
to the relaying tasks may be an acceptable alternative. The most common fiber
system at present is one where the ground wires on transmission lines are replaced
by fiber-core ground wires. In time, it seems reasonable that such a fiber network
will provide sufficient channel capacity, high redundancy, and economic incentive
to become an integral part of protection systems.
Fiber optic systems are also being used to communicate relaying and control
signals between the substation yard and control house where the relays are located.
Theselinksarenotdisruptedbyelectromagneticinterference,andwithmultiplexing
could replace great deal of wiring from traditional substation designs. On the other
hand, these systems require that electronic systems be placed within the yard, and
hence that some enclosures and power supplies be distributed throughout the yard.
In any case, as such systems become commonplace, computer relaying will become
their natural extension.
Developments in electronic transducer technology were also mentioned in
Chapter 1. A number of electronic, digital current transformers have been tested

280 Relaying applications of traveling waves
and are being tried on power systems throughout the world. A corresponding
development in voltage transformers has not been as rapid, except the in case of
gas-insulated substations where a controlled environment between ground and the
high voltage conductors permits the installation of high precision electronic digital
voltage transformers. These newer electronic voltage and current transducers, since
they can provide sampled data directly, are a natural complement of a substation
computer system. The reader is referred to relevant technical literature on the
subject for additional details.28–30
9.10 Summary
In this chapter, we have introduced some concepts which are not in the main
stream of computer relaying applications. Traveling wave relaying has held high
promise, but has yet to be deployed in large quantities. Differential relaying of
transmission lines based either on data samples or on phasors has become quite
useful to utilities having sufficient communication capability and long transmission
linesortransmissionlineswithmultipletaps.Faultlocationtechnologyforoverhead
lines has progressed sufficiently so that locating faults with distance estimation is
quite accurate. Fault location based on wave propagation has also been accepted
andisreportedtoprovideverygoodresults,althoughunderstandably thenumber of
such installations is rather limited. Newer developments in technology arrive with
astonishing speed, and it is to be expected that in the field of computer relaying we
will see many such technologies adopted in the coming years.
Problems
9.1 Verify by direct substitution that expressions (9.2) are the solutions of
√
Equation (9.1). Show that the characteristic impedance is (L/C) and the
√
velocity of propagation is 1/ (L/C).
9.2 Given that the zero sequence inductance of a transmission line is three times
the positive sequence inductance, and that the zero sequence velocity of prop-
agation is 75% of the positive sequence velocity, what is the ratio of the zero
sequence to the positive sequence characteristic impedance?
9.3 If a transmission line with a characteristic impedance of Z ohms terminates
in a load impedance of Z(cid:1), what is the reflection coefficient at this terminal?
For a purely resistive Z, calculate the reflected wave if the incident wave is a
step function and Z(cid:1) is (a) purely inductive, and (b) purely capacitive.
9.4 Show that the Clarke and Karrenbauer transformation matrices given by
Equations (9.9) and (9.18) are similarity transformations on the L, C, LC,
and CL matrices of a transposed transmission line.

References 281
9.5 Validate the results given in Table 9.1. Often arguments of symmetry simplify
the computations. Remember that, in each case, the fault is simulated by the
application of negative prefault voltages at the point of fault.
9.6 Determine the relationship between the Karrenbauer components for each of
the faults listed in Table 9.1.
9.7 An unsymmetrical fault will create mixed reflected waves when a pure modal
wave strikes the fault. Determine the reflected waves of 0,α,β modes when a
pure α mode wave strikes a phase b-c fault.
9.8 Assume that a generator of infinite short-circuit capacity is connected to
a transmission line with a characteristic impedance of Z, and a velocity
of propagation ν. Calculate and plot the discriminant functions given by
Equation (9.20) through several successive reflections for a fault at a dis-
tance d. Thus show that the discriminant functions will maintain their relative
values for substantial periods even for faults at short distances from the
relay.
9.9 Assume that the capacitances of a three-phase transmission line can be
neglected. For such a case, perform the synchronization of phasors at the two
ends of the line. Assume zero mean random measurement noise of certain
variance. Determine the uncertainty in synchronization when all phasors are
measured with the assumed noise.
9.10 Forthethree-terminallineshowninFigure9.15,assumeaπ-sectionrepresen-
tationforeachofthelinesections.Ifthevoltagesandcurrentsattheterminals
are available, determine a formula for calculating the charging current con-
tribution from the capacitors at the tap point. This calculated compensation
must be used to create an accurate differential current.
9.11 Show that the traveling wave differential currents given by Equations (9.31)
and (9.32) become the phasor differential currents of Equation (9.27) when
steady state conditions are reached on the line. Recall that the steady state
condition can be viewed as a superposition of two constant waves traveling
in opposite directions – the standing wave phenomenon.
References
[1] Rudenberg, R. (1968) Electrical Shock Waves in Power Systems, Harvard University
Press, Cambridge, Massachusetts.
[2] Stevenson, Jr., William D. (1982) Elements of Power System Analysis, 4th edition,
McGraw-Hill Inc.
[3] Sunde, Erling D. (1949) Earth Conduction Effects in Transmission Systems, D. Van
Nostrand Company; (1968) Dover Publications, New York.

| 282 |     |     | Relaying applications | of traveling | waves |
| --- | --- | --- | --------------------- | ------------ | ----- |
[4] Bewley, L.V. (1933) Traveling Waves on Transmission Systems, John Wiley & Sons,
| Inc. New | York; (1963) | Dover Publications, | New York. |     |     |
| -------- | ------------ | ------------------- | --------- | --- | --- |
[5] McLaren, P.G. (1988) Traveling waves and ultra high speed relays, Chapter 6 in
Microprocessor Relays and Protection Systems, IEEE Tutorial Course, IEEE Special
| Publication | no. 88EH0269-1-PWR. |     |     |     |     |
| ----------- | ------------------- | --- | --- | --- | --- |
[6] Dommel H.W. and Michels, J.M. (1978) High speed relaying using traveling wave
| transient | analysis, IEEE | paper no. | A78, pp. 214–219. |     |     |
| --------- | -------------- | --------- | ----------------- | --- | --- |
[7] Mansour M.M. and Swift, G.W. (1986) Design and testing of a multi-micro-
processor traveling wave relay, IEEE Trans. on Power Delivery, vol. 1, no. 4,
pp. 74–82.
[8] Vitins, M. (1978) A correlation method for transmission line protection, IEEE Trans.
| on PAS, | vol. 97, no. 5, | pp. 1607–1617. |     |     |     |
| ------- | --------------- | -------------- | --- | --- | --- |
[9] Kohlas, J. (1973) Estimation of fault location on power lines, Proceedings of the 3rd
IFAC Symposium, The Hague/Delft, the Netherlands, pp. 393–402.
[10] Johns A.T. and Aggarwal, R.K. (1980) New ultra high speed directional blocking
scheme for transmission line protection, Developments in Power System Protection,
| IEE Conference | Publication | no. 185, | London, pp. 141–145. |     |     |
| -------------- | ----------- | -------- | -------------------- | --- | --- |
[11] Hedman,D.E.(1965)Propagationonoverheadtransmissionlines – I:Theoryofmodal
analysis;II:Earthconductioneffectsandpracticalresults,IEEETrans.onPAS,vol.84,
pp. 200–211.
[12] Engler, F. Lanz, O.E. Hanggli,M. andBacchini,G.(1985) Transient signalsand their
processinginanultrahighspeeddirectionalrelayforEHV/UHVlineprotection,IEEE
| Trans. on | PAS, vol. 104, | no. 6, pp. | 1463–1474. |     |     |
| --------- | -------------- | ---------- | ---------- | --- | --- |
[13] ChamiaM.andLiberman,S.(1978)UltrahighspeedrelayforEHV/UHVtransmission
lines – development,designandapplication,IEEE Trans.onPAS, vol. PAS-97, no.6,
pp. 2104–2116.
[14] McLaren, P.G., Rajendra, S., Shahab-Eldin, S. and Crossley, P.A. (1985) Ultra high
speed distance protection based on traveling waves, International Conference on
Developments in Power System Protection, IEE Conference Publication no. 249,
pp. 106–110.
[15] Takagi, T., Baba, J.I., Uemura, K. and Sakaguchi, T. (1978) Fault protection based
on traveling wave theory, Part II: sensitivity analysis and laboratory tests, IEEE paper
| no. A 78, | pp. 220–226. |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- |
[16] Thorp, J.S., Phadke, A.G., Horowitz, S.H. and Begovic, M.M. (1987) Some appli-
cations of phasor measurements to adaptive protection, Proceedings of the Fifteenth
| PICA Conference | of IEEE, | Montreal, | pp. 467–474. |     |     |
| --------------- | -------- | --------- | ------------ | --- | --- |
[17] Phadke A.G. and Hankun, H. (1986) Current differential relaying of multi-terminal
lineswithmicroprocessors,ProceedingsoftheMinnesotaPowerSystemsConference,
| Minneapolis, | pp. 1–8. |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- |
[18] Takagi,T.,Miki,T.,Makino,J.andMatori,I.M.(1978)Feasibilitystudyforacurrent
differentialcarrierrelaysystembasedontravelingwavetheory,IEEE paperno.A78,
pp. 132–133.
[19] Stranne, G., Kwong, W.S. and Lomas, T.H. (1986) A current differential relay
for use with digital communication systems: Its design and field experience, 13th
Annual Western Protective Relay Conference, Washington State University, Spokane,
Washington.

References 283
[20] Souillard, M., Sarquiz, P. and Mouton, L. (1974) Development of measurement prin-
ciples and of the technology of protection systems and fault location systems for
| three-phase | transmission | lines, | CIGRE´ | Paper no. | 34-02. |
| ----------- | ------------ | ------ | ------ | --------- | ------ |
[21] Takagi, T., Yamakoshi, Y., Yamaura, M. et al. (1982) Development of a new type
fault locator using the one-terminal voltage and current data, IEEE Trans. on PAS,
| vol. PAS-101, | no. 8, | pp. 2892–2898. |     |     |     |
| ------------- | ------ | -------------- | --- | --- | --- |
[22] Westlin,S.E.andBubenko,J.A.(1976)Newton-Raphsontechniqueappliedtothefault
| location | problem, IEEE | PES | Summer | Meeting, A76 | 334–3. |
| -------- | ------------- | --- | ------ | ------------ | ------ |
[23] Takagi,T.,Yamakoshi,Y.,Baba,J. etal.(1981)Anewalgorithmofanaccuratefault
location for EHV/UHV transmission lines: Part I – Fourier transformation method,
| IEEE Trans. | on PAS, | vol. PAS-100, |     | no. 3, pp. 1316–1323. |     |
| ----------- | ------- | ------------- | --- | --------------------- | --- |
[24] Takagi,T.,Yamakoshi,Y.,Baba,J. etal.(1982)ANewalgorithmofanaccuratefault
location for EHV/UHV transmission lines: Part II – Laplace transformation method,
| IEEE Trans. | on PAS, | vol. PAS-101, |     | no. 3, pp. 564–573. |     |
| ----------- | ------- | ------------- | --- | ------------------- | --- |
[25] Eriksson, L., Saha, M.M. and Rockefeller, G.D. (1985) An accurate fault locator with
compensation for apparent reactance in the fault resistance resulting from remote-end
| infeed, IEEE | Trans. | on PAS, | vol. PAS-104, | no. 2, | pp. 424–436. |
| ------------ | ------ | ------- | ------------- | ------ | ------------ |
[26] Gale, P.F. (1993) Overhead line fault location based on travelling waves and GPS,
precise measurements in power systems conference, Arlington, Virginia.
[27] Gale,P.F.,Taylor,P.V.,Naidoo,P. etal.(2001)Travellingwavefaultlocatorexperi-
ence on ESKOM’s transmission network, Developments in Power System Protection,
| IEE Conference | Publication |     | no. 479. |     |     |
| -------------- | ----------- | --- | -------- | --- | --- |
[28] Mouton, L., Stalewski A. and Bullo, P. (1978) Non conventional current and voltage
Electra,
| transformers, |     | no. 59, | pp. 91–122. |     |     |
| ------------- | --- | ------- | ----------- | --- | --- |
[29] Hild, H.A., Stern, C., Gambale, J.C. and Sun, S.C. (1975) Field installation and test
of an EHV current transducer, Trans. of IEEE on PAS, vol. 94, no. 1, pp. 37–44.
[30] Subjak,Jr.,J.S.(1975)AnEHVcurrenttransducerwithfeed-backcontrolledencoding,
| Trans. of | IEEE on PAS, | vol. | 94, no. | 6, pp. 2124–2130. |     |
| --------- | ------------ | ---- | ------- | ----------------- | --- |

10
Wide area measurement
applications
10.1 Introduction
The concept of adjusting the protection systems to adapt them to prevailing power
system conditions was first embodied in ‘Adaptive Relaying’ which will be dis-
cussed more fully in the following section. In more recent years the technology
of Wide Area Measurements based on synchronized Phasor Measurement Units
(PMUs) has become a vehicle for gathering very precise information about the
power system in real time.1 These measurements are finding applications in sev-
eral areas of power system operations including monitoring, control and protection.
Phasor measurement technology is able to create a precise snapshot of the power
system, which can be refreshed at rates approaching once per cycle of the power
frequency. Being able to track the power system performance through normal and
emergency conditions is clearly of great importance in adapting control and pro-
tection systems so that their response to system events is appropriate and optimal.
SeveralpromisingapplicationsofWAMSbasedadaptiverelayingwillbeconsidered
in Section 10.6.
10.2 Adaptive relaying
Adaptive relaying is a subject of relatively recent origin. It has been defined as
follows.2–6
Adaptive Protection is a protection philosophy which permits and seeks to make
adjustments to various protection functions in order to make them more attuned to
prevailing power system conditions.
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

286 Wide area measurement applications
The key concept is to change something in a protection system in response
to changes in the power system caused by changing loads, network switching
operations,orfaults.Toacertainextentallexistingprotectionsystemsmustaccom-
modate power system changes. Often this is achieved by making the relay settings
correct for all conceivable network conditions. For example, zone-3 of a relay must
be set such that it will cover the longest neighboring circuit (highest impedance)
regardless of whether or not any in-feed from other lines is present. Considerations
such as these often result in a protection system design that is deficient on two
counts: firstly not all possible system contingencies can be anticipated during the
design of the protection system, and secondly, the settings are not the best ones
possible for any single system configuration. Nevertheless, to the extent that a relay
settingor relaydesign catersfor variable systemconditions, it isan adaptive setting
and in this sense present protection practices are adaptive to a certain extent.
Another point to be made is that the distinction between control and protec-
tion functions becomes blurred when one begins to consider adaptive protection
functions. Many protection functions already encompass control: reclosing of cir-
cuit breakers is a case in point. As we begin to modify relay performance based
upon changing conditions on the power system, we approach the classic concept of
feed-back control. Indeed, adaptive relaying is in fact a feed-back control system.
Since adaptive relaying implies that relays must adapt to changing system con-
ditions, a hierarchy of computer relays with communication links must be assumed
to exist. The communications could be to other equipment within a substation, or
to computer networks of remote substations. Consequently, one could visualize an
adaptiveprotectionsystemwhichadaptstoitssubstationenvironment,oronewhich
is responsive to system needs. Clearly the latter is more comprehensive, but also
needslongdistancecommunication channels. Thisbecomespracticalwiththemod-
ern WAMS systems. Local communication within the substation is easy to achieve,
and quite possibly adaptive features which depend upon local communication alone
will be the first ones to be implemented.
Even where long distance communication is necessary, some adaptive features
call for a great deal of real-time data to be obtained from remote locations, while
others require modest amounts of non-real-time data. Adaptive systems requiring
modest data transactions are sure to be implemented before those requiring large
amounts of real-time data. At this time, fiber optic communication links offer the
only feasible medium for such voluminous data transfers. Fiber optic links are just
nowbeginningtobeinstalledonpowersystems.Assuchinstallationsbecomemore
commonplace, many more adaptive relaying concepts are likely to be accepted by
the industry.
10.3 Examples of adaptive relaying
The reader is referred to the literature for a more complete account of adaptive
relaying possibilities.2–7 Many of the examples discussed in the literature are much

| Examples | of adaptive relaying |     |     |     | 287 |
| -------- | -------------------- | --- | --- | --- | --- |
better discussed in the context of WAMS which will be covered in Sections 10.5
and 10.6. In this section we will consider only those adaptive protection functions
which require modest amounts of information external to the relay, which is often
available locally. We will now present some examples to illustrate the principles
involved.
protection8
| 10.3.1 | Transmission | line |     |     |     |
| ------ | ------------ | ---- | --- | --- | --- |
Traditionalprotectionof multi-terminal linescallsfor manycompromises. Consider
the three-terminal line shown in Figure 10.1. The zone settings of the relay at
locationA should besuchthat itremainssecurewhether or not thetapisinservice.
Consider a fault at F. The distance relay at bus A sees a fault impedance of
(I )I
|     |     | Z = Z +Z | +I      |     | (10.1) |
| --- | --- | -------- | ------- | --- | ------ |
|     |     | A        | F A C A |     |        |
where I and I are the contributions to the fault from terminals A and C
|     | A C |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
respectively. Equation (10.1) corresponds to a phase fault – similar equations hold
for ground faults also. If one does not wish to over-reach the end B for all system
conditions, the zone setting must be less than Z +Z whether or not the tap at C
A B
+Z ),
is in service. If one sets zone-1 of relay A at 90% of (Z A B it will protect a
smaller portion of the distance from the tap point to the end B when the tap is in
service. The zone-1 setting is thus less than desirable (i.e. 90% of the line) when
| the tap is | in service. |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- |
One could restore zone-1 setting to its proper value under all conditions by
making the relay adapt to system conditions. As mentioned previously, adaptability
canbeofdifferentvarietiesdependinguponthedemandsonecanmakeonavailable
communication channel capacity. For example, the status of breakers at B and C
could be communicated to the relay at A. When breaker C status is known to
|     |     |     | +Z  | ) +Z | +   |
| --- | --- | --- | --- | ---- | --- |
the relay at A, zone-1 setting there can be 0.9 (Z A B or 0.9 [Z A B (I A
I )/I ] depending upon whether the breaker at C is open or closed. To get this
C A
information from one terminal to the others, relatively small amounts of data need
tobecommunicatedbetweenterminals,andthestatusdatacanbesentwheneverthe
|     |     | A   | B   |     |     |
| --- | --- | --- | --- | --- | --- |
|     |     | I   | I   |     |     |
|     |     | A   | B   |     |     |
F
|     |     | Z   | Z   |     |     |
| --- | --- | --- | --- | --- | --- |
|     |     | A   | F   |     |     |
I
C
C
|     | Figure | 10.1 Three-terminal | line with a fault | at F |     |
| --- | ------ | ------------------- | ----------------- | ---- | --- |

288 Wide area measurement applications
status changes – they need not be sent at real-time data rates. A reasonable value
for the ratio of currents (I + I )/I may be used in making the zone calculations.
A C A
Similar considerations apply to relays at B and C.
Theapproximationsintroducedbytheassumedvaluesofcurrentsintheprocedure
described above can be eliminated if the actual equivalents of the network at each
terminalaresenttoeveryother terminalofthemulti-terminalline.Thiswillrequire
more data to be transmitted, but these too are not real-time data. Knowing the
The´ve´nin equivalent for the other terminals as well as the status of the associated
breakers, adaptive determination of the zone settings is possible. The procedure can
be improved even more if the terminal which determines that the fault is between
the tap point and the terminal communicates this information in real time to all
other terminals. Since the segment of the line on which the fault has occurred
is now known at each terminal (along with the equivalent circuit for the entire
multi-terminalsystem),zone-1canbesettoreachthedesireddistanceinthefaulted
segment from each terminal. The only margin which must be allowed is the usual
one for any possible transient over-reach.
The The´ve´nin equivalent circuits require significantly greater amounts of data
to be communicated to each terminal. Sequence impedance matrices and voltage
vectors must be sent from a central location where the equivalent circuits can be
determined.Althoughthesearenotreal-timedatainthesensethattheymustbesent
while the fault is on the system, they must be computed and communicated often
enoughtokeepthedatacurrent.Themostaccuratemulti-terminallineprotectioncan
be obtained if voltage and current measurements (either sampled data or phasors)
are communicated from each terminal to all the others in real time. Indeed, in this
case the differential protection principle described in Section 9.7 should be used,
instead of the stepped distance protection.
10.3.2 Transformer protection
Transformer protection using percentage differential relays was discussed in
Section 2.4. It was pointed out there that the slope of the differential characteristic
is adjusted to over-ride the false differential currents produced due to mismatches
in current transformer ratios, changing taps in a tap changing transformer, and
unequal errors in current transformers in the primary and secondary windings of
the transformer. Typical percentage slopes of the differential relays are set at 40%
to accommodate these false differential currents. Two of these three effects, viz.
current transformer ratio mismatch and changing tap position could be taken into
account by an adaptive percentage differential relay.
Consider the adaptive differential relay shown in Figure 10.2(a). The relay can
monitor input primary and secondary currents i and i when the transformer is car-
1 2
rying load current. Under healthy conditions, these two currents should be equal. If
they are not, there will be a false differential current which is due to the three
effects mentioned above. In this case, the relay will estimate a multiplication

| Examples | of adaptive relaying |     |     |     | 289 |
| -------- | -------------------- | --- | --- | --- | --- |
1:T
|     | I   |     | I   |     |     |
| --- | --- | --- | --- | --- | --- |
|     | 1   |     | 2   | 40% |     |
|     | 1:n | 1:n | 2   |     |     |
|     | i 1 |     | I   |     |     |
|     | 1   |     | i d |     |     |
2
N :N
1 2
~10%
Adaptive percentage
I
|     | differential relay |     |     | r   |     |
| --- | ------------------ | --- | --- | --- | --- |
|     |                    | (a) |     | (b) |     |
Figure 10.2 Adaptive percentage differential relay. (a) Relay with main transformer tap
input to the relay. (b) Reduction in the percentage differential slope
factor k to be applied to the secondary current i so that the two currents are
2 2
equal:
|     |     |     | i = k i |     | (10.2) |
| --- | --- | --- | ------- | --- | ------ |
1 2 2
The factor k is an estimate of the CT ratio mismatch and the effect of the tap
2
changer position on the main power transformer. (The tap changer position of the
main power transformer can also be sensed directly by the differential relay if
such a sensor indication is available.) This factor will be used in calculating the
differential and restraint currents in the differential relay algorithm, so that the
only remaining cause of the false differential current will be the effect of unequal
CT errors during fault conditions. Having removed two of the three causes of false
differentialcurrent,thepercentagedifferentialslopeoftherelaycannowbeadjusted
| downward | as illustrated | in Figure 10.2(b). |     |     |     |
| -------- | -------------- | ------------------ | --- | --- | --- |
Clearly the reduced percentage differential slope increases the sensitivity of the
relay, and thus it is made capable of sensing lower grade faults in the transformer.
| 10.3.3 | Reclosing |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- |
In many countries (including North America) the standard practice for handling
phase-to-phase and phase-to-ground faults is to used high speed three-phase clear-
ing, followed by high speed reclosing, and on detecting a sustained fault to follow
up with some number of automatic reclosing, and a final lock-out if the fault is
permanent. The first high speed reclosing is without supervisory interlocks (i.e.
without checking for voltages on either side of the breaker), and the speed of high
speed reclosing is determined by the system voltage – varying between 20 and
40 cycles. The automatic reclosing functions are usually controlled by conditions
on the network, and usually employ some checks and interlocks.
Since the high speed reclosing function does not check system conditions, it is
possible to reclose on an existing fault in the case of a permanent fault. Generators

290 Wide area measurement applications
which are near the fault are thus likely to be subjected to a repeat stress induced by
closing into a fault. In particular, the closing into a phase-to-phase fault is likely
to cause a severe shock to the generator and a consequent harmful effect on the
machine shaft life. It is therefore desirable to use an adaptive high speed reclosing
scheme which tests the system voltages before attempting the high speed recluse,
and blocks it if an existing fault is discovered.3 This is particularly desirable when
operation of relays near a generator is under consideration.
A simplified system with a generator, a transmission line, and a circuit breaker
is illustrated in Figure 10.3. It is assumed that the circuit breaker is capable of
operating each pole individually. At high speed reclose time, one pole of the circuit
breaker isclosed. The choice of which pole to close depends upon which phase had
the original fault. For example, if the initial fault was on phase b, the reclose opera-
tion is initiated on phase a or c. Let us assume that phase a is selected for reclosing
first. The voltages on all three phases are next measured (usually within one period
ofthefundamentalfrequency),anddependinguponthevoltagesonthethreephases
the condition of the line can be established. Following possibilities exist:
(a) There is no fault on the line. In this case phase-a voltage will be normal, and
phases b and c will have induced voltages which are in phase with phase-a
voltage, and their magnitudes will depend upon the conductor placement on
transmission line towers. These being known, could be pre-set in the relay as
norms for induced voltages for that line configuration. In this case the high
speed reclose operation could be completed on the remaining phases.
(b) There is a phase-a-to-ground fault on the line. In this case all phase voltages
will be low, and phase a current will be high.
(c) There is a phase-b-to-ground fault on the line. In this case phase b voltage will
be low, and phase c will have an induced voltage.
(d) There is a phase-b-to-phase-c fault on the line. In this case the induced voltages
on phases b and c will be exactly equal to each other.
a
b
c
normal a-g b-g b-c a-b
Figure 10.3 Reclosing on a transmission line with a phase-b to ground fault. The circuit
breaker tests the line with a single phase reclose and blocks further high speed reclose
operations if a standing fault is detected

WAMS architecture 291
(e) Thereisaphase-a-to-phase-bfaultontheline.Inthiscasethevoltageonphaseb
willbeequaltothevoltageonphasea,andcphasewillhaveaninducedvoltage.
In the last four cases further reclosing operation will be blocked, and the first
(closed) pole opened again. This adaptive reclosing scheme prevents the generator
to be subjected to a multi-phase fault on high speed reclosing, which is the most
damaging as far as generator shaft life is concerned.
10.4 Wide area measurement systems (WAMS)
Wide area measurements through synchronized phasor measurements have become
commonplaceonmanypowersystemsaroundtheworld.Thistechnologyofferspre-
cise measurements of positive sequence voltages and currents at remote locations.1
The instruments which perform these measurements are known as Phasor Measure-
mentUnits(PMUs).AgenericPMUisshowninFigure10.4.Thebasicstructureof
a PMU is very much like that of a computer relay. Input signals (consisting of volt-
ages at buses and feeder currents) are sampled and the sampled data converted to
positive sequence quantities as per the technique given in Chapter 5. The measure-
ments are time-tagged using a GPS clock. The measurements can be refreshed as
frequentlyasonceeverycycle.Thedetailswillbefoundinreference[1]citedabove.
The outputs of the PMUs with the accompanying time tags are available for
communication to local or remote sites. Where remote communication with several
PMUs is involved, the communication is through hubs which are known as Phasor
DataConcentrators(PDCs).PMUsandPDCsformahierarchicalstructurediscussed
in the next section. Main features of PMUs and PDCs are defined in an IEEE
standard (C37.118 and itssucceeding revisions) so that equipment manufactured by
different manufacturers can be inter-operable.
10.5 WAMS architecture
The WAMS system consists of PMUs where the measurements are carried out,
and PDCs where inputs from several PMUs are collected and passed on to various
applications as needed. This hierarchical arrangement is illustrated in Figure 10.5.
GPS receiver
Power system
signals
Output
data stream
Phasor Measurement
Unit
Figure 10.4 A generic phasor measurement unit. Three-phase voltage and current wave-
forms are sampled and then converted to positive sequence measurements

292 Wide area measurement applications
Archival
storage
Archival
PDC
storage Applications
Applications
PDC PDC PDC PDC
Archival
storage
PMU PMU PMU PMU
Applications
Figure 10.5 Hierarchy ofPMUs and PDCs to manage the wide area measurementsystem
The task of the Phasor Data Concentrator can be briefly summarized as follows.
It matches the time tags of data received from various PMUs so that a synchro-
nized data stream is created for applications, and communicated to upper levels of
hierarchy for further data concentration. PDCs (as well as PMUs) store archival
data which can be used for post-mortem analyses of major system events. In addi-
tion the PDCs may also have a GPS receiver so that latency of data received from
various PMUs can be measured, and outliers in propagation delays flagged for cor-
rective action to be taken. Applications of phasor data may reside at PMU levels
as well as at PDC levels. Clearly at higher levels of the hierarchy the volume of
data collected increases, and so does the latency of the data. There is thus a nat-
ural selection in applications which can be implemented at various levels of the
hierarchy. At PMU level, relatively fast actions can be taken using locally avail-
able data. At regional or central control centers, applications requiring data from
widerareaswithlongerdelaysaremoreappropriate.Thisdistinctioninapplications
holds for system monitoring and control applications, as well as for the protection
applications using WAMS.
The PMU and PDC architecture also permits data transmission in opposite direc-
tion on every communication link. Usually the data in the downward direction is
sparse and infrequent, mostly dealing with system management functions.
10.6 WAMS based protection concepts
Many of the ideas of adaptive protection become particularly attractive when wide
area measurements are used to achieve adaptability. Because of the delays in
gathering data at PDCs (typically of the order of 30–100 milliseconds), the adap-
tive protection functions which are based on WAMS must be relatively slower
acting. Most backup and system protection functions are of this type, and are ideal

WAMS based protection concepts 293
for adaptability using WAMS data. It should also be stated that as of now these
concepts are proposals for research and development for practical implementations
to follow in the future. It is also likely that newer ideas on such protection applica-
tionswillbeforthcominginthefuture,andthereaderisadvisedtoconsulttechnical
publications for evolving ideas.
We will now examine some of these concepts which have been discussed in
recent
publications.9,10
10.6.1 Adaptive dependability and security
During normal operation of power systems, a failure to trip quickly when a fault
occurs can leadto systeminstability. It istherefore imperativethat a fault iscleared
in primary clearing time without fail. This is the requirement of high dependabil-
ity in protection during normal system operation. This bias is appropriate when
the power system is in normal state. The bias towards dependability invariably
produces a reduction in security of protection.11 (Also see Section 2.1) However,
when thepower systemisinastressedstateafalsetrip – aconsequence of reduced
security – is far more destructive to the power system, as it may lead to cascad-
ing failures and a wide-spread blackout. WAMS data could be used at the control
center, and an assessment made of the state of the power system. When the system
is determined to be in a stressed state, it would be desirable to alter the protection
system bias in favor of increased security, with a possible reduction in dependabil-
ity. In doing so, it is accepted that there may be a fault for which there may be a
slight increase in the probability that the fault will not be cleared in normal time,
but the chance of a false trip is significantly reduced.
Figure 10.6 illustrates the principle of this scheme. From prior off-line analy-
sis of the power system, critical locations of protection systems are determined so
that a false trip of relays at those locations will increase the possibility of cas-
cading failures, and adaptive supervision of the system is desirable. Consider the
normal complement of protections at such a location. There are three independent
protection systems, and in order to achieve high dependability during normal sys-
tem operating conditions the outputs of the three protection systems are arranged
in a logical ‘OR’ configuration. This means that operation by any one of those
protection systems will lead to the trip of the circuit breaker. Of course, inse-
cure operation of any one protection system may lead to the start of cascading
failures.
Now consider the scenario at the control center where the WAMS based esti-
mation leads to the conclusion that the power system is in a critical state. Under
these conditions, the protection system bias could be changed in favor of increased
security. This is achieved by modifying the logic of the critical protection system
to a ‘VOTE’, so that at least two of the protection systems must agree that the
fault requires tripping of the circuit breakers before the trip is issued. This is best
achieved when the protection system consists of computer relays, and the logic is

294 Wide area measurement applications
Arbitration Logic
System State
Protection
No 1
Or
Protection
And
No 2
Vote
Protection
No 3
To
Circuit
Breakers
System Control Center
WAMS input
WAMS based system
state assessment
Critical Protection System
Figure 10.6 Adaptive control of dependability and security of protection systems based
on WAMS
not realized by hard-wired relaying systems. Of course this principle can be applied
at more locations if they are determined to be critical.
It should also be noted that there is always a possibility that two out of three pro-
tections may mis-operate, leading to an insecure operation. However, by changing
the logic to ‘VOTE’, the level of security has been increased very significantly.
10.6.2 Monitoring approach of apparent impedances towards relay
characteristics
Severalanalysesofblackoutshaverevealedthatsomeprotectionsettingsweremade
with certain assumptions about the power system – for example its expected load
level or stability oscillations following a major event. The relay settings made are
appropriate for the assumed system condition. However, over the years the power
system changes in its structure, operating strategy and loading patterns. Under ideal
circumstancestherelaysettingsmadewouldberevisedwitheachsignificantchange
in the power system. In most power systems this is not done on a regular basis,
because of shortage of manpower or scheduling difficulties. In any case, it has been
observed that as years go by, the prevailing relay settings are not appropriate for
the existing power system state and the criticality of some of the relay settings is
not noticed by the protection engineers.
In the case of various distance relays, it is possible to monitor the apparent
impedance trajectories during system load changes or stability swings with PMU
measurements. Remember that the conditions of concern are balanced conditions,

WAMS based protection concepts 295
and the impedance relays would see the positive sequence impedance which can
be obtained by dividing voltage phasors by feeder current phasors at the relay
locationinquestion. Duringloadchanges orstabilityswingsitwouldbepossibleto
comparetheapparentimpedancetrajectoryinrelationtotherelaycharacteristic,and
depending on how close the apparent impedance comes to the relay characteristic,
an alarm is communicated to the engineering office indicating that the relay setting
may need to be reconsidered. This alarm is not meant to take action in real time,
but to create a message to the engineering office that the relay setting may need a
revision. This function would identify critical protection functions which may be
in danger of causing a cascading failure due to unexpected operation of the relay.
Of course similar procedure may be implemented for overcurrent relays as well.
Consider the power system shown in Figure 10.7. At a critical location, the relay
characteristic would be available to the local PDC, and the PDC application would
track the apparent impedance trajectory for load changes, as in Figure 10.7(a), or
for stability swings, as in Figure 10.7(b). The margin settings used for creating the
alarm would be set by protection engineers and would also be available to the local
PDC application. This is one of the simplest applications of the PMU data, and
since all signals and controls are local it is relatively easy to implement.
10.6.3 WAMS based out-of-step relaying
Out-of-step relays are commonly employed in systems where instability between
two or more regions leads to a loss of synchronization and separation into two
or more islands. Consider the system depicted in Figure 10.8. During transient
stabilityswings of such asystem, most transmissionlinerelays willsee anapparent
Critical relay location
Power System
Stability
swing
X X Margin trajectory
Protective Protective
zones Loading zones
approach
R R
Margin
(a) (b)
Figure 10.7 Detection of apparent impedance trajectory approaching zones of protection

296 Wide area measurement applications
B
A
(a)
X
Z
Y
B
Z
Y R
A
(b)
Figure 10.8 Stability swing excursions in the zone of protection of a relay
impedance trajectory in the R-X plane. For example, the distance relay at bus A for
line A-B may see impedance trajectory Y-Y or Z-Z during two system swings of
differentseverity.Thefirsttrajectorycorrespondstoastableswing,whilethesecond
corresponds to an unstable swing. In any case, these impedance trajectories may
enter one of the trip zones of the relay as shown in Figure 10.8(b). The out-of-step
relays must be able to distinguish between a movement of the trajectory inside
a zone of protection due to a fault, from one caused by the stability oscillations.
Traditionally, this is achieved by using the criterion that, in case of a fault, the
trajectory is traversed very quickly, while a stability oscillation creates a slow
movement in the R-X plane.
Upon detection of an out-of-step condition, the next task of the protection system
is to permit selective tripping for clearly unstable cases so that the power system is
separated in islands, with a reasonable match between load and generation within
each island. At present, the places where tripping is permitted are pre-determined,
baseduponsimulationsperformedduringsystemplanningstudies.However,amore
appropriateprocedurewouldbetodetermineboththenatureofanin-progressswing
as well as desirable locations for separation in real time.
The first part of this problem – determining whether a given transient swing
which is in progress is one from which the system will or will not recover – is a
difficultone,butcanbeexpectedtobesolvedbyseveralofthetechniquescurrently
under investigation (such as parallel processing, use of transient energy functions
etc.). For systems which behave like a two-machine system, the problem can be

| WAMS | based protection | concepts |     |     |     | 297 |
| ---- | ---------------- | -------- | --- | --- | --- | --- |
P
|     |     | P      |     | e   | P      |     |
| --- | --- | ------ | --- | --- | ------ | --- |
|     |     | m      |     |     | m      |     |
|     |     | E1ejδ1 |     |     | E2ejδ2 |     |
(a)
|     |     |     | δ = (δ − δ | )   |     |     |
| --- | --- | --- | ---------- | --- | --- | --- |
1  2
|     |     | 0 1 | 2 3 | 4 5 . | . . n k |     |
| --- | --- | --- | --- | ----- | ------- | --- |
P′
m
|     |     | P   |     | A   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     |     | m   |     | 2   |     |     |
A 1
δ
(b)
|     |     | Figure 10.9 | Prediction | of  | stability swing |     |
| --- | --- | ----------- | ---------- | --- | --------------- | --- |
solved.12 Assume that the two-machine equivalent of the system is known through
dynamic state estimation. For a two-machine system, the stability oscillation can
| be predicted | by the | well known | equal | area criterion. |     |     |
| ------------ | ------ | ---------- | ----- | --------------- | --- | --- |
Consider the two-machine system shown in Figure 10.9(a) (representing a two
area system equivalent) in which a loss of generation in one area has caused the
toP(cid:1)
steadystatemechanicalpowertoshiftfromP m leavingthetransferimpedance
m
| unaffected. | The swing | equation | of the | two-machine | system is |        |
| ----------- | --------- | -------- | ------ | ----------- | --------- | ------ |
|             |           | Mδ¨      | = P −P | = P         | sinδ      | (10.3) |
|             |           |          | m      | e           | emax      |        |
where (δ = δ – δ ) and M is the equivalent moment of inertia of the two-machine
1 2
system. From successive real-time measurements of voltage and current phasors at
theterminalsoftheequivalentmachines,asetofelectricalpowerandcorresponding
δ 0,1,...,n}
rotor angle differences is measured in real time. Let P k and k {k =
representthesemeasurementsatinstantsk(cid:1)t,where(cid:1)tisthemeasurementinterval.
If we assume that the P−δ relationship is piece-wise linear, we may estimate P(cid:1)
m

| 298 |     |     |     |         |     | Wide | area | measurement | applications |
| --- | --- | --- | --- | ------- | --- | ---- | ---- | ----------- | ------------ |
|     |     |     |     | ,δ ).12 |     |      |      |             |              |
from the set of measurements (P If Pˆ(cid:1) is the estimate of P(cid:1)
|     |           |                  |     | k k       |     | m       |       | m       |        |
| --- | --------- | ---------------- | --- | --------- | --- | ------- | ----- | ------- | ------ |
|     |           |                  |     |           |     | (cid:2) |       | (cid:3) |        |
|     |           |                  | 2   |           |     | 1       |       | 1       |        |
|     | Pˆ(cid:1) | =                |     | [vtδ−vt1δ | ]+  |         | vtBP+ | vtP     | (10.4) |
|     | m         | ((cid:1)t)2(vtv) |     |           | 0   | vtv     |       |         |        |
3
where P and δ are vectors of electrical power and angle measurements
|     |     | P = | (P ,P,......P |     | )t,δ | = (δ | ,δ ,δ | )t  |     |
| --- | --- | --- | ------------- | --- | ---- | ---- | ----- | --- | --- |
|     |     |     | 0             |     | n−1  |      | 1 2   | n   |     |
P is a vector of differences between every power measurement and the first power
| measurement | P   |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|           |       | P =          | [(P −P  | ),(P | −P  | ),...(P | −P  | )]t |     |
| --------- | ----- | ------------ | ------- | ---- | --- | ------- | --- | --- | --- |
|           |       |              | 1       | 0    | 2 0 |         | n   | 0   |     |
| and v, B, | and 1 | are matrices | defined | by   |     |         |     |     |     |
v = (1,4,9,...n2)t
|     |     |     |     |    |     |    |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1000...0
|     |     |     |     |    |     |    |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2200...0

|     |     |     |     |              |            |     |     |     |     |
| --- | --- | --- | --- | ------------- | ---------- | ---- | --- | --- | --- |
|     |     |     |     | B = 3420...0 |            |     |     |     |     |
|     |     |     |     | .            | . . . .... |     |     |     |     |
|     |     |     |     | n             | . . .      | ...2 |     |     |     |
1 = (1,1,1,...1)t
Equation (10.4) is obtained by integrating Equation (10.3) over each sampling
interval, and assuming that the electrical power changes linearly between the two
measurements. The details of this derivation are left as an exercise (see Problem 2).
The new mechanical power P(cid:1) having been estimated from the measurements of
m
| δ,  |     | P−δ |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P and the complete curve can be determined, and finally an equal area com-
parisonmadebetweenareaA andthemaximumavailablemarginA inFigure10.9.
|     |     |     | 1   |     |     |     |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
If A is smaller than A , stability is predicted. Otherwise, the swing will be unsta-
| 1   |     | 2   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ble. In the simulations reported in the reference cited,12 a reliable estimate of P(cid:1)
m
(andthustheinferenceaboutthenatureofthestabilityoscillation)couldbereached
in about one-quarter of the period of the electromechanical oscillation.
A research project applied this theory to the interface between the states of
Florida and Georgia in the US. Although there are a large number of machines
in both of these systems, because of the peninsular nature of the Florida power
system the behavior of the system during stability swings can be approximated
by a two-machine equivalent – one representing the aggregate of Florida gener-
ators and the other the aggregate of the Eastern United States. This latter is of
course a very large system, and approaches an infinite bus in relation to the power

WAMS based protection concepts 299
Georgia
PMU PMU
Out of step
condition
Relay Relay
Figure 10.10 Adaptive out-of-step relaying for a two-machine like system
system of Florida. Thus, this (and similarly situated systems) are ideal candidates
for application of the two-machine out-of-step relaying concepts developed above.
Figure 10.10 shows the system in question. PMUs collected phase angles from
the two regions, and exchanged them with each other in order to construct a
two-machine model of the stability event. In such a system, equal area criterion
can be used to determine if an evolving swing is going to be stable or unstable.
Theproblembecomesmuchmorecomplexonlargeintegratednetworkscommon
in most modern economies. A possible solution for the stability problem in large
networks with the use of real-time data from WAMS may benefit from a two-step
approach. In the first step, the evolving swings of all generators of significant size
may be observed, and over a reasonable observation window groups of coherent
machines can be identified. See Figure 10.11(a). It is likely that in most practical
cases coherency of generators can be established in about 200–400 milliseconds
after the start of the disturbance.
Determination of coherency between machines facilitates the formation of coher-
entlyswinginggroupsasillustratedinFigure10.11(a).Whencoherencygroupshave
been determined there are two possible approaches to determining the outcome of
the swings as illustrated in Figure 10.11(b). The first approach is to assume that the
Extended Equal Area Criterion13 can be applied, and the stability outcome deter-
mined as in the case of a two-machine stability problem. Briefly, the principle of
ExtendedEqualAreapostulatesthatatthetimeofasystemsplit,eachevent ofsep-
arationissimilartothebehaviorofatwo-machinesystem.Itislikelythatasthesys-
tem event progresses, other coherent groups may be formed after each split, and the
ExtendedEqualAreaprinciplecanbeappliedsequentiallytotheseevolvinggroups.
As an alternative to the Extended Equal Area approach, one could consider the
swings of the coherent groups as time-series
functions,14,15
and a prediction of
the time-series leads to either a zero-crossing of the relative angle which leads to
stability,ortoamonotonicallyincreasingbehaviorwhichwouldindicateinstability.
Baseduponthispredictionoftheoutcome,onewoulddetermineappropriatecontrol
actions to be taken.

| 300 |     |     | Wide area measurement | applications |
| --- | --- | --- | --------------------- | ------------ |
Observation
window
PMU data
(a)
| Two machine equivalent |     | Time-series of swing curves |     |     |
| ---------------------- | --- | --------------------------- | --- | --- |
and prediction
|     | PMU | δ   | − δ |     |
| --- | --- | --- | --- | --- |
|     | PMU | 1   | 2   |     |
Time
|     |     | Observation | Prediction |     |
| --- | --- | ----------- | ---------- | --- |
Processing
|     | Center |     | Interval Interval |     |
| --- | ------ | --- | ----------------- | --- |
(b)
Figure 10.11 Out-of-step detection in large integrated networks
This subject remains an active area of research and newer developments can be
expected to offer other possibilities for real-time stability determination.
| 10.6.4 Supervision | of backup | zones |     |     |
| ------------------ | --------- | ----- | --- | --- |
Over-reaching zones of distance relays cover a large area in the R-X plane. This
exposes them to inadvertent tripping when no fault is present on the system. In
particular, zone-3 trips due to load excursions or due to stability swings are known
contributors to loss of security in the protection system. Various schemes to restrict
the exposure to zones of protection to such phenomena – for example using lens
shaped or figure-8 characteristics – does reduce the likelihood of unwanted trips
due to these effects. However, the fact remains that load power-factors can become
very unusual during major disturbances due to unusual flows of active and reactive
powers. As these phenomena are likely to occur when the power system is stressed
and in danger of cascading into a blackout, it is appropriate to consider remedial
actions which can be implemented using wide area measurements.
Zones 2 and 3 of step distance relays are both over-reaching zones. Zone-3 istra-
ditionally recognized as one of the most difficult settings to be made because of the

WAMS based protection concepts 301
B
B
A B B
B B
B
B
Zone 3 picks-up at A
Balanced Conditions at B? Yes.
Any Zone-1 picked up at B? If not Block Zone-3
Figure 10.12 Supervision of over-reaching zones of distance relays
need for adequate security. On the other hand, there are scenarios of contingencies
when zone-3 is deemed essential for dependable clearing operation following a
fault.16 It is then necessary to investigate ways in which the over-reaching zones
could be supervised by techniques which use wide area measurements.
PMUs located at neighboring buses offer an excellent tool for supervising the
operation of over-reaching zones in order to avoid inappropriate operation during
conditions of system stress.10 Consider the relays located at buses identified by ‘B’
in Figure 10.12. If an over-reaching zone of relay at ‘A’ picks up, then PMUs at
all the ‘B’ locations can be queried to determine if the apparent impedance seen
by them represents a fault in the direct trip zones of any of those relays. If none
of them see such a fault, then clearly the pick-up of an over-reaching zone at ‘A’
is due to something other than a fault, and it should be blocked. Note that this
action is to be taken only for balanced loading conditions at A and B locations,
since load encroachment or stability swings imply balanced operating conditions.
The distances from which measurements are to be obtained are modest, so that
communication delays should be insignificant.
10.6.5 Intelligent load shedding
Under-frequency load shedding and restoration is used in most power systems.
Occasionally, load shedding under supervisory control has also been exercised as
a part of a Remedial Action Scheme. It is clear that under-frequency load shed-
ding does not operate unless the power system breaks into islands creating load
generation imbalances, and there is an overall decay of system frequency in gen-
eration deficient islands. In many cases this action is too late, particularly if the
islands are created in an unexpected configuration. It would be desirable to activate
load shedding under supervisory control when significant loss of generation or load
takes place, although no islands are formed and the frequency does not begin its
decline.

302 Wide area measurement applications
Figure 10.13 Real-time ACE determination from tie flow deviation to perform intelligent
load shedding
Apossibleapproachtodetermininglossofgenerationinanetworkistodetermine
deviationofthetiepowerflows((cid:1)T)fromtheirscheduledvalues(seeFigure10.13).
This is traditionally measured as an element of the Area Control Error (ACE=
(cid:1)T − B(cid:1)f).17 The other element of ACE is (cid:1)f, the deviation in system frequency,
and B the average system load-frequency characteristic droop. Of course until the
tie lines are opened, the frequency deviation is zero, and tie flow deviation alone
signifies the generation shortfall. The shortfall can be used to estimate the amount
of load to be shed. This latter need not match exactly the tie-flow deviation. Other
factors to consider in such a scheme are the inertial response of generators to the
initial disturbance. Ultimately, the goal of such a scheme is to make appropriate
adjustments to system load in order to avoid more serious consequences in the
future – such as a system-wide blackout.
10.6.6 Adaptive loss-of-field
A loss-of-field condition for a generator is detected by a distance relay connected
at the terminals of a generator. If the generator field current is reduced due to
a hardware failure or due to some inappropriate control setting in the excitation
systemofthegenerator,thegeneratormayfaceoneoftwocontingencies: excessive
end-iron heating or steady state instability.11 Both conditions can be detected by
a distance relay with circular characteristics, as illustrated in Figure 10.14. When
the limiting contingency is end-iron heating, the relay setting is based only upon
the generator capability. However, when the limiting contingency is the approach
of steady state instability, the relay characteristic depends upon the impedance of
the generator and the The´ve´nin impedance of the power system, as seen from the
machine terminals.
The distance relay setting consists of two concentric circles which are offset
appropriately below the real axis, as shown in Figure 10.14. The inner circle is the
actual stability limit, which, if breached, will lead to loss-of-synchronization of the
generator and pole slipping and its eventual tripping. The outer circle is used to
create an alarm for system operators if the apparent impedance seen by the relay

WAMS based protection concepts 303
Field
winding
System Thévénin
Generator
impedance
X Apparent impedance
Strong system trajectory
R
Weak system
Figure10.14 Adaptiveloss-of-fieldrelay.Therelaysettingsareadaptivelyadjustedtothe
prevailing power system The´ve´nin impedance
continuesitsmovementfromoutsidetheouterzone,throughit,andapproachingthe
innerzonewhichwouldcreateexcessiveend-ironheatingorsteadystateinstability.
The offset of the circular characteristics as well as their radii are dependent
upon the two impedances mentioned above. Clearly, the machine impedance is a
constant. However, the system The´ve´nin impedance will depend upon the strength
of the power system. When the relay is set initially, it assumes certain conditions
to exist on the network. However, as a catastrophic event unfolds, many important
transmissionelementsmayhave tripped. Thiswouldcreateaweaker power system,
and a larger The´ve´nin impedance. Under certain conditions, it is entirely possible
that the weakened power system will lead to instability even before the outer zone
of the relay (as set originally) is reached.
The state of the power system is continuously monitored at the control center
throughmonitoringandstateestimationtasks.Itisthenpossibletodetermineinreal
time the changing system The´ve´nin impedance and communicate this information
to the generator loss-of-field relay. This would make the relay setting reflect the
prevailing power system state, thus improving security of the power system.
10.6.7 Intelligent islanding
Islanding of the power system is a natural extension of the out-of-step detection
function. For disturbances whichare going toleadto instabilitybetweentwocoher-
entgroupsofgenerators,itisalogicalsteptoseparatethepowersystemintoislands
which contain each coherent group of generators and some load. It is clear that the
loads or generators in the islands would have to be adjusted in order to continue
operation at a safe system frequency. In islands with excess generation it will be
necessary to shed generation of appropriate size, while for islands where there is
excess load it will be necessary that load be shed. The loads and generators in the

304 Wide area measurement applications
islands as initially formed would have to be in approximate match so that very
large adjustments would not be necessary; also, both loads and generators should
be available for control.
Wide area measurements available at the system control center will help identify
desired boundaries of separation depending upon which generators have formed a
coherentgroup,andwhatloadsandgenerationwithintheislandstobeformedwould
be controllable to the desired extent. Usually this requires out-of-step blocking at
undesirable points of separation, and out-of-step tripping at desired locations for
formingtheislands.Itmaywellbethatsomeislandingscenariosarepre-calculated,
based upon simulation studies and made available for action when system state
assessment indicates that such control actions are called for.
10.6.8 System wide integration of SIPS
SIPS – System Integrity Protection Scheme is the acronym currently recommended
by the IEEE Power System Relaying Committee to describe complex protection
and control systems commonly known as Remedial Action Schemes (RAS) or
Special Protection Schemes (SPS). The SIPS schemes usually bring in wide area
measurements such as power flows, switch and circuit breaker status etc. and use
pre-calculated responses to take action when power system reaches a state where
such a control action is needed. Usually these schemes are designed to enhance
powertransfercapabilitiesbetweenregionsofthepowersystem,andtakeimmediate
corrective action if a contingency condition occurs which does not permit that level
of power transfer. The power transfer limit may be imposed by thermal loading
limits, operating voltage limits, or stability limits of the network.
It isknown that inmany power systems several SIPSsystems have been installed
to take corrective action in response to many different sets of contingency condi-
tions. As each SIPS is designed to remedy one particular operational constraint, it
is possible that in an arbitrary system state, two or more SIPS may have conflicting
effects on the power system, negating the effect of the cure provided by one or
more of the installed SIPS.
A possible use of wide area measurement systems is to gather system-wide
real-time data at the control center, and then determine which of the SIPS should
be allowed to operate to steer the power system to a secure state or if a new control
action is needed. The role of the wide area measurement system is to provide a
sound basis to the system control center to use the most effective control strategy
in any given situation.
10.6.9 Load shedding and restoration
The load shedding function is designed to maintain a balance between load and
generation within a system. If the system has been islanded following a system
disturbance of the type described above, its frequency will begin to move towards

Summary 305
a new value determined by the mismatch between load and generation within the
island. If the load is in excess of generation, the frequency will decay and it will
become necessary to remove load soon enough before the frequency decays to such
an extent that generators must be taken out of service in order to prevent generator
damage. Usually load shedding is initiated by under-frequency relays installed in
substations, and load is shed in several frequency steps in order to make sure that
unnecessary load is not tripped beyond what is needed to arrest the frequency
decline above the dangerous level. Load restoration is the reverse process: load is
restored as the frequency returns to its normal value, and it is restored in steps with
sufficient coordination delays in order to avoid any cycling effects between load
shedding and restoration relays.
If the system does not form an island, the frequency remains substantially con-
stant. In this case, the load shedding relays cannot act, as they do not see the
necessary decay in frequency. However, the need to initiate load shedding is still
there: each system should attain load-generation balance within its boundary to
avoid overloading the tie-lines with its neighbors and risk a separation. This has
been discussed in Section 10.6.5.
Recently an interesting approach to power system restoration following a black-
out has been proposed.18 The restoration scheme uses Artificial Neural Networks
(ANNs) to facilitate service restoration in each island formed following a blackout.
Within each island the first ANN determines load forecast based upon pre-blackout
loaddataandcold-loadpick-upforthetypesofloadintheisland.ThesecondANN
determines the final expected island configuration taking into account the availabil-
ity of various resources and the load that could be served upon restoration. Based
upon these data, a switching sequence is generated which systematically restores
lines and transformers with due attention being paid to loading and voltage con-
straints that may be exist. Wide area measurements were used to provide inputs
to the ANNs, as well as to help determine the feasible switching sequence. The
technique was demonstrated on a 162 bus, 17 generator test system.
Several other contributions to the subject of power system restoration can be
found in the literature.19 Fast and successful service restoration on a power system
following a blackout is one of the most important counter-measures against catas-
trophic failures of power systems. As wide area measurements become integrated
inpowersystemmanagement, itistobeexpected thatintelligentservicerestoration
will receive increasing attention.
10.7 Summary
The synchronized phasor measurement technology was born out of the develop-
ments in computer relaying. The PMUs have been recognized as a major innova-
tion in precise measurements on power systems, and several applications of these
measurements to power system engineering are currently under development. In
this chapter we have provided an overview of current thinking on using these

306 Wide area measurement applications
measurements to improve power system protection – particularly as related to the
problemofpowersystemblackouts.Itisexpectedthatcomingyearswillseeimple-
mentation of these ideas. It is also the hope of the authors that future researchers
will be motivated to more fully integrate the computer relays with wide area mea-
surements in order to make the protection systems more dependable and secure
under a variety of system operating conditions.
Problems
10.1 Assume that the The´venin equivalents are known for the sources behind
the terminals of a three-terminal transmission line shown in Figure 10.1.
Assuming a fault occurs on one of the taps, and this fact is known to every
other terminal, devise an algorithm which will determine the fault location
accurately from each terminal. Also show that the effect of the fault arc
resistance upon the distance estimate can now be eliminated.
10.2 Verify that the result given in expression (10.5) is the least-squares solution
for estimating the new mechanical power transfer. The electrical power is
assumed to be piece-wise linear between two measurements, and the rotor
velocity at the end of one interval is the velocity at the beginning of the next
interval.
10.3 Derive a result similar to Equation (10.5) if the rotor angle movements are
calculated by the formula given in Chapter 14 of Reference 8 (below).
References
[1] Phadke, A. G. and Thorp, J. S. (2008) SynchronizedPhasor Measurementsand Their
Applications, Springer.
[2] Phadke, A. G. Horowitz, S. H. McCabe, A. G. (1990) Adaptive automatic reclosing,
Paperno.34-204,CIGRE´ 1990Session,August26-September1,1990,Paris,France.
[3] Horowitz,S.H.,Phadke,A.G.,andThorp,J.S.(1987)Adaptivetransmissionsystem
relaying, Paper no. 87 SM 625-77, IEEE PES Summer Meeting, San Francisco, July
1987.
[4] Phadke,A.G.,Thorp,J.S.andHorowitz,S.H.(1987)Impactofadaptiveprotectionon
powersystemcontrol,Proceedingsofthe9thPSCCConference,Lisbon,pp.283–290.
[5] Thorp,J.S.,Horowitz,S.H.andPhadke,A.G.(1988)Theapplicationofanadaptive
technology to power system protection and control, CIGRE´, Paris.
[6] Phadke, A. G., Thorp, J. S. and Horowitz, S. H. (1988) Study of Adaptive Trans-
mission System Protection and Control. Final report prepared for Oak Ridge National
Laboratory by Virginia Polytechnic Institute.
[7] Rockefeller, G. D., Wagner, C. L., Linders, J. R., et al. (1987) Adaptive transmis-
sion relaying concepts for improved performance, Paper no. 87 SM 632-3, IEEE PES
Summer Meeting, San Francisco.

References 307
[8] Stevenson, Jr., William D. (1982) ElementsofPowerSystemAnalysis, Fourth edition,
| McGraw-Hill | Inc. |     |     |
| ----------- | ---- | --- | --- |
[9] Phadke,A.G.,Novosel,D.andHorowitz,S.H.(2005)Wideareameasurementappli-
CIGRE´
cations in functionally integrated protection systems, Study Committee B5,
| Colloquium, | October | 2007, Madrid, | Spain. |
| ----------- | ------- | ------------- | ------ |
[10] PhadkeA.G.andNovosel,D.(2008)Wideareameasurementsforimprovedprotection
systems”, 8th Symposium on Power System Management, Cavtat, Croatia.
[11] Horowitz,S.H.andPhadke,A.G.(2008)PowerSystemRelaying,ThirdEdition,John
| Wiley and | Sons, Ltd. |     |     |
| --------- | ---------- | --- | --- |
[12] Centeno, V., De La Ree, J., Phadke, A. G. etal. (1993) Adaptive out-of-step relaying
using phasor measurement techniques, IEEE Computer Applications in Power, vol. 6,
no. 4.
[13] Xue, Y., Wehenkel, L., Belhomme, R. et al. Extended equal area criterion revisited
[EHVpowersystems],IEEETrans.onPowerSystems,vol.7,issue3,pp.1012–1022.
[14] Haque,M.H.,Rahim,A.H.M.A.(1988)Anefficientmethodofidentifyingcoherent
generators using Taylor series expansion, IEEE Trans. on Power Systems, vol. 3,
pp. 1112–1118.
[15] Haque, M. H. (1996) Novel method of finding the first swing stability margin of a
power system from time domain simulation, IEE Proceedings on Generation, Trans-
| mission, | and Distribution, | vol. 143, | no. 5. |
| -------- | ----------------- | --------- | ------ |
[16] Horowitz,S.H.andPhadke,A.G.(2006)ThirdZoneRevisited,IEEETrans.onPower
| Delivery, | 21(1), pp. 23–29. |     |     |
| --------- | ----------------- | --- | --- |
[17] Cohn, N. (1971) Control of Generation and Power Flow on Interconnected Systems,
| John Wiley | & Sons, Ltd. |     |     |
| ---------- | ------------ | --- | --- |
[18] Bretas, A. S. and Phadke, A. G. (2003) Artificial Neural Networks in power system
restoration, IEEE Trans. on Power Delivery, vol. 18, no. 4, pp. 1181–1186.
[19] Adibi, M. M. (2000) Power System Restoration Methodologies and Implementation
| Strategies, | IEEE Press, | Power Engineering | Series. |
| ----------- | ----------- | ----------------- | ------- |

| Appendix       |        |      | A   |     |     |
| -------------- | ------ | ---- | --- | --- | --- |
| Representative | system | data |     |     |     |
Computer relay design requires testing of algorithms with waveforms of currents
and voltages as they are found in realistic power systems. Simulation of transients
in a laboratory with physical system models or with simulation programs are useful
methods of generating such test waveforms. We have collected some representative
system constants for important power system elements which may be helpful in
| many simulation | studies. |     |     |     |     |
| --------------- | -------- | --- | --- | --- | --- |
| Transmission    | lines1   |     |     |     |     |
362kV transmission line with horizontal conductor arrangement. The series
impedance in ohms per mile at 60Hz is given below in a lower triangular matrix
for in order to save writing. The complete matrix is of course symmetric. The
ground wire effect has been included in the three-by-three matrix.
|     |    |     |     |     |    |
| --- | --- | --- | --- | --- | --- |
0.2920+j1.002
|     | =  0.1727+j0.4345 | 0.2359+j0.9934 |     |     |    |
| --- | ------------------ | -------------- | --- | --- | --- |
Z s
|     | 0.1687+j0.3549 | 0.1727+j0.4345 |     | 0.2920+j1.002 |     |
| --- | -------------- | -------------- | --- | ------------- | --- |
The shunt admittance matrix in micro-mhos per mile (again the lower triangular
| portion | only) is given by |     |     |     |     |
| ------- | ----------------- | --- | --- | --- | --- |
|         |                   |    |     |    |     |
j6.341
|     |     |  −j1.115 | j6.571 |    |     |
| --- | --- | --------- | ------ | --- | --- |
Y =
s
|                                   |     | −j0.333           | −j1.115 | j6.341  |     |
| --------------------------------- | --- | ----------------- | ------- | ------- | --- |
| ComputerRelayingforPowerSystems2e |     | byA.G.PhadkeandJ. |         | S.Thorp |     |
2009JohnWiley&Sons,Ltd

| 310 |     |     |     |     |     |     | Appendix A |
| --- | --- | --- | --- | --- | --- | --- | ---------- |
(b) 800kV transmission line with horizontal configuration. The series impedance
| matrix | is given | by  |     |     |     |     |     |
| ------ | -------- | --- | --- | --- | --- | --- | --- |
|        |          |    |     |     |     |     |    |
0.1165+j0.8095
|     |           | =  0.0097+j0.2961 |     | 0.1176+j0.7994  |     |                |    |
| --- | --------- | ------------------ | --- | --------------- | --- | -------------- | --- |
|     | Z         | s                  |     |                 |     |                |     |
|     |           | 0.0094+j0.2213     |     | 0.0097+j0.2961  |     | 0.1165+j0.8095 |     |
| and | the shunt | admittance         |     | matrix is given | by  |                |     |
|     |           |                    |     |                |     |               |     |
j7.125
|     |     |     | Y   | =  −j1.133 | j7.309 |    |     |
| --- | --- | --- | --- | ----------- | ------ | --- | --- |
s
|     |     |     |     | −j0.284 | −j1.133 | j7.125 |     |
| --- | --- | --- | --- | ------- | ------- | ------ | --- |
To simulate transposed lines, it is sufficiently accurate to replace all the
off-diagonal entries by their average value; and replace all the diagonal entries
by their average. If D are the diagonal entries and M the off-diagonal entries,
−
the positive and negative sequence values are given by (D M), while the zero
| sequence | values | are | given | by (D + 2M). |     |     |     |
| -------- | ------ | --- | ----- | ------------ | --- | --- | --- |
(c) Parallel Transmission Lines. The following data are for double circuit 500kV
| transmission |     | lines. | The series | impedance | matrix is       | given by |     |
| ------------ | --- | ------ | ---------- | --------- | --------------- | -------- | --- |
|              |     |        |            |           | (cid:2) (cid:3) |          |     |
Z Z
|     |     |     |     | Z = | s1 m |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- |
|     |     |     |     | s   | ZT   |     |     |
Z
|     |     |     |     |     | (cid:2) m s2 (cid:3) |     |     |
| --- | --- | --- | --- | --- | -------------------- | --- | --- |
Y Y
|     |     |     |     | Y = | s1 m |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- |
|     |     |     |     | s   | YT Y |     |     |
m s2
where
|     |     |    |     |     |     |     |    |
| --- | --- | --- | --- | --- | --- | --- | --- |
0.1964+j0.9566
|     |     |  0.1722+j0.3833 |     | 0.2038+j0.9477 |     |     |    |
| --- | --- | ---------------- | --- | -------------- | --- | --- | --- |
|     | Z   | =                |     |                |     |     |     |
s1
|     |     | 0.1712+j0.2976 |     | 0.1769+j0.3749 |     | 0.2062+j0.9397 |     |
| --- | --- | -------------- | --- | -------------- | --- | -------------- | --- |
|     |     |               |     |                |     |                |    |
0.2062+j0.9397
|     |     |                 |     |                |     |     |    |
| --- | --- | ---------------- | --- | -------------- | --- | --- | --- |
|     | Z   | = 0.1769+j0.3749 |     | 0.2038+j0.9477 |     |     |     |
s2
|     |     | 0.1712+j0.2976   |     | 0.1722+j0.3833 |     | 0.1964+j0.9566 |     |
| --- | --- | ---------------- | --- | -------------- | --- | -------------- | --- |
|     |     |                 |     |                |     |                |    |
|     |     | 0.1642+j0.2150   |     | 0.1701+j0.2422 |     | 0.1742+j0.2863 |     |
|     | ZT  |  0.1600+j0.1922 |     | 0.1657+j0.2120 |     | 0.1769+j0.3749 |    |
=
m
|     |     | 0.1548+j0.1769 |     | 0.1600+j0.1920 |     | 0.1642+j0.2150 |     |
| --- | --- | -------------- | --- | -------------- | --- | -------------- | --- |
|     |     |               |     |                |    |                |     |
j6.318
|     | Y   | =  −j1.092 |     | j6.522 |    |     |     |
| --- | --- | ----------- | --- | ------ | --- | --- | --- |
s1
|     |     | −j0.316 |     | −j1.092 j6.388 |     |     |     |
| --- | --- | ------- | --- | -------------- | --- | --- | --- |

| Power system |     |     |     |     |     | 311 |
| ------------ | --- | --- | --- | --- | --- | --- |
|              |    |     |    |     |     |     |
j6.388
|     | =  −j1.070  | j6.522   |         |     |     |     |
| --- | ------------ | -------- | -------- | --- | --- | --- |
|     | Y s2         |          |          |     |     |     |
|     | −j0.316      | −j1.092  | j6.318   |     |     |     |
|     |             |          |          |    |     |     |
|     | −j0.069      | −j0.1433 | −j0.4339 |     |     |     |
|     | YT  −j0.034 | −j0.0572 | −j0.1433 |    |     |     |
=
m
|     | −j0.025 | −j0.0344 | j0.0693 |     |     |     |
| --- | ------- | -------- | ------- | --- | --- | --- |
Transformers
A typical EHV auto-transformer rated at 250 MVA per phase and voltage ratings
of 800/345/34.5kV has leakage reactances of 12.2%, 57%, and 37.6% between
800/345kV, 800/34.5kV, and 345/34.5kV windings respectively. The magnetizing
current at rated voltage is 0.058%. The saturation characteristic is defined by two
additional points: a current of 0.015% at a voltage of 80%, and a current 0.29% at
a voltage of 115%. This information is generally adequate for simulating transient
phenomena of interest for relaying. Note that for the leakage reactances given, the
equivalent circuit has one branch with a negative reactance. If a physical model
is developed, the branch will probably be set equal to zero. A digital computer
simulation on the other hand can accommodate the negative value.
Generators
A modern 1300MW cross-compound generator has x of 1.92, x of 1.85, x ’ of
|     |     |     |     | d   | q   | d   |
| --- | --- | --- | --- | --- | --- | --- |
0.34 and x q ’ of 0.60 on its own base. The per unit rotor inertia constant is 8.1.
A 100MW hydro unit has x of 1.16, x of 0.75, x ’ of 0.40 and x ’ of 0.40 on its
|           |              | d             | q       | d   | q   |     |
| --------- | ------------ | ------------- | ------- | --- | --- | --- |
| own base. | Its per unit | rotor inertia | is 4.2. |     |     |     |
It is rare that any other constants will be needed in relaying studies. The transient
time constants of the generators are of the order of several seconds.
Power system
The power system used in relaying studies should contain sufficient complexity to
represent conditions seen by relays in actual service. Thus, in studying transmis-
sionlinerelaying,eachlineterminalshouldbeconnected toatleastfewotherlines.
Lines of 50 to 100 miles in length are not uncommon on a high voltage network,
and produce significant transient components in voltage and current waveforms
which may produce problems for the relays. It may be necessary to use detailed
π-sections)
line models (several two or three buses removed from the transmis-
sion line terminals. Multiple-winding transformers should be modeled correctly,
taking note of the proper zero and positive sequence impedances. Transformer core

312 Appendix A
saturation should also be modeled realistically, remembering that the inrush and
over-excitation transients are the key factors in determining the behavior of trans-
former relays. Models of current and voltage transformers should also be included.
If digital simulation of the power system is used, care should be taken to make sure
that the waveforms do not exhibit steep changes between time-steps of the simu-
lation due to the finite interval integration algorithm used. Often low pass filtering
of the output will take care of such phenomena. Averaging of successive time step
outputs may be sufficient in most cases.
References
[1] Transmission Line Reference Book: 345kV and Above, Second Edition, 1982, Electric
Power Research Institute, Palo Alto, California.

Appendix B
Standard sampling rates
Note: At the time of printing the first edition of this work, these sampling rates
were proposed to be a part of the standard COMTRADE. This standard has now
been in force for many years, and these rates are part of that standard.
In a substation with digital protection, monitoring, and control systems, many
sampling rates may be called for. Oscillography, for example, may require signals
sampled at several kHz, while relaying computers may need sampling rates of the
order of several hundred Hz. Also, it seems certain that in the future, as computers
and Analog to Digital Converters acquire greater capabilities, the entire spectrum
of sampling rates may be shifted upward. When sampling at various sampling rates
is required, it seems reasonable to sample at the highest feasible sampling rate in
the Data Acquisition Unit, and convert these samples to the required lower rates
within the subsystem which calls for the lower rate. The highest sampling process
shoulduseananti-aliasingfilterthatiscommensuratewiththatrate.Itthenbecomes
necessary to devise algorithms which will convert these data to the lower sampling
rateswiththeir correspondinganti-aliasingfilters.Thesameargumentisvalidwhen
we consider that the data may be obtained at one site, and used by some user as a
test case for off-line simulations or testing of algorithms. Here also, conversion to
another sampling rate with accompanying anti-aliasing filtering is needed.
An IEEE standard recommends two lists of sampling rates which lead to con-
venient sampling rate conversion algorithms.1 Let f and f be the sampling rates
1 2
at which the data are obtained and at which they are desired, respectively. It is
assumed that f is higher than f . If L and M are two integers, such that
1 2
Lf = Mf = f
1 2 LCM
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

314 Appendix B
| Table B.1     | Recommended   | sampling frequencies |            |
| ------------- | ------------- | -------------------- | ---------- |
| corresponding | to f          | =384×f               |            |
|               | LCM           | base                 |            |
| L,M           | Samples/cycle | f for 60Hz           | f for 50Hz |
| 1             | 384           | 23040                | 19200      |
| 2             | 192           | 11520                | 9600       |
| 3             | 128           | 7680                 | 6400       |
| 4             | 96            | 5760                 | 4800       |
| 6             | 64            | 3840                 | 3200       |
| 8             | 48            | 2880                 | 2400       |
| 12            | 32            | 1920                 | 1600       |
| 16            | 24            | 1440                 | 1200       |
| 24            | 16            | 960                  | 800        |
| 32            | 12            | 720                  | 600        |
| 48            | 8             | 480                  | 400        |
| 64            | 6             | 360                  | 300        |
| 96            | 4             | 240                  | 200        |
| Table B.2     | Recommended   | sampling frequencies |            |
| corresponding | to f =3200×f  |                      |            |
|               | LCM           | base                 |            |
| L,M           | Samples/cycle | f for 60Hz           | f for 50Hz |
| 1             | 3200          | 192000               | 160000     |
| 2             | 1600          | 96000                | 80000      |
| 4             | 800           | 48000                | 40000      |
| 5             | 640           | 38400                | 32000      |
| 8             | 400           | 24000                | 20000      |
| 10            | 320           | 19200                | 16000      |
| 16            | 200           | 12000                | 10000      |
| 20            | 160           | 9600                 | 8000       |
| 25            | 128           | 7680                 | 6400       |
| 32            | 100           | 6000                 | 5000       |
| 40            | 80            | 4800                 | 4000       |
| 50            | 64            | 3840                 | 3200       |
| 64            | 50            | 3000                 | 2500       |
| 80            | 40            | 2400                 | 2000       |
| 100           | 32            | 1920                 | 1600       |
| 160           | 20            | 1200                 | 1000       |
| 200           | 16            | 960                  | 800        |
| 320           | 10            | 600                  | 500        |
| 400           | 8             | 480                  | 400        |
| 800           | 4             | 240                  | 200        |

References 315
then relatively simple algorithms can be designed for the conversion process. It is
of course necessary that the data obtained at f and at f be appropriately filtered
1 2
to eliminate aliasing errors. At this time, it seems unlikely that any application of
digital signal processing in a substation will call for sampling rates higher than
3600 times per cycle. Based upon this, Tables B.1 and B.2. are proposed as the
standard sampling rate tables to be used in any sampling process. The DAU should
useashighasamplingrateaspossiblefromthesetables.Anyofthelowerratescan
then be obtained by simple algorithms. One such algorithm is given in Appendix C.
The tables list sampling frequencies for 60Hz and 50Hz power systems. It should
be noted that the present day relaying algorithms use only a few frequencies at
the lower end of these tables. Also, most of the known relaying algorithms use
frequencies from Table B.1.
References
[1] IEEEStandardCommonFormatforTransientDataExchange(COMTRADE)forPower
Systems. C37. 111–1991.

| Appendix   |         |           |     |          | C   |       |     |     |
| ---------- | ------- | --------- | --- | -------- | --- | ----- | --- | --- |
| Conversion | between | different |     | sampling |     | rates |     |     |
Note:ThisprogramistakenfromtheIEEEStandardC37.111whichisReference
1, listed at the end of this Appendix. Fortran program is not commonly used at
present, but we present it as a topic of interest, and also to give a flavor of the
early work in this area. Standard subroutines and functions are now available to
| do the decimation | process. |     |     |     |     |     |     |     |
| ----------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
TheseFORTRANprogramshavebeentakenfromaDraftdocument1,whichdeals
with various issues of standardization in the computer based substation systems.
The programs convert data between two compatible sampling rates in the sense of
Appendix B, with appropriate anti-aliasing filtering provided at the lower sampling
rate.Thefilterdesignisspecifiedbyitsimpulseresponsespecifiedoveronecycle.A
sample program which produces such a response for a given filter transfer function
is also provided.
| C   | PROGRAM       | CONVERT       |            |       |       |            |         |          |
| --- | ------------- | ------------- | ---------- | ----- | ----- | ---------- | ------- | -------- |
| C   | CONVERTS      | SAMPLES       |            | TAKEN |       | AT ONE     | RATE TO | A SECOND |
| C   | RATE          |               |            |       |       |            |         |          |
| C   | USER SUPPLIED |               | FILTER     |       | IS IN | FOR020.DAT |         |          |
| C   | DATA IS       | IN FOR021.DAT |            |       |       |            |         |          |
| C   | OUTPUT        | IS IN         | FOR025.DAT |       |       |            |         |          |
=
| C                                 | NFMAX            | THE | MAXIMUM |                   | LENGTH |       | OF THE FILTER |         |
| --------------------------------- | ---------------- | --- | ------- | ----------------- | ------ | ----- | ------------- | ------- |
|                                   | PARAMETER        |     | NFMAX   | =                 | 3600   |       |               |         |
| C                                 | 3600 CORRESPONDS |     |         | TO                | ONE    | CYCLE |               |         |
| C                                 | LFAC =           | THE | NUMBER  | OF                | TENTHS | OF    | A DEGREE      | BETWEEN |
| C                                 | SAMPLES          | IN  | INPUT   |                   |        |       |               |         |
|                                   | PARAMETER        |     | LFAC    | = 50              |        |       |               |         |
| ComputerRelayingforPowerSystems2e |                  |     |         | byA.G.PhadkeandJ. |        |       | S.Thorp       |         |
2009JohnWiley&Sons,Ltd

| 318 |           |                        |         |          |     |           |           | Appendix C |
| --- | --------- | ---------------------- | ------- | -------- | --- | --------- | --------- | ---------- |
| C   | FSAMP     | = THE                  | INPUT   | SAMPLING |     | FREQUENCY |           |            |
|     | PARAMETER | FSAMP                  |         | = 4320   |     |           |           |            |
| C   | NSIZE     | = THE                  | MAXIMUM | LENGTH   |     | OF        | THE INPUT | DATA       |
| C   | STRING    |                        |         |          |     |           |           |            |
|     | PARAMETER | NSIZE                  |         | = 720    |     |           |           |            |
|     | INTEGER*2 | DBUF(NSIZE)            |         |          |     |           |           |            |
|     | DIMENSION | HFIL(NFMAX),DTD(NFMAX) |         |          |     |           |           |            |
DATA N0/0/
| C   | GET FILTER | RESPONSE |     |     |     |     |     |     |
| --- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
READ(20,*)NA,NB
|     | IF(NB.LE.NFMAX) |     | GO  | TO 6 |     |     |     |     |
| --- | --------------- | --- | --- | ---- | --- | --- | --- | --- |
WRITE(6,5)
| 5   | FORMAT(3X,‘DECIMATION |     |     |     | FILTER | IS TOO | LONG’) |     |
| --- | --------------------- | --- | --- | --- | ------ | ------ | ------ | --- |
STOP
C
| 6   | NBF =              | NB/LFAC |        |       |             |     |          |     |
| --- | ------------------ | ------- | ------ | ----- | ----------- | --- | -------- | --- |
|     | IF(NB.EQ.NBF*LFAC) |         |        | GO TO | 10          |     |          |     |
|     | WRITE(6,*)‘FILTER  |         | LENGTH |       | INDIVISIBLE |     | BY LFAC’ |     |
STOP
C
| 10  | READ(20,*)(HFIL(JJ),JJ |     |     | = 1,NB) |     |     |     |     |
| --- | ---------------------- | --- | --- | ------- | --- | --- | --- | --- |
C
| C   | ***************************************************** |     |     |     |     |     |     |     |
| --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
C
WRITE(6,18)
| 18  | FORMAT(1H$, |     | ‘ENTER | TOTAL | NUMBER |     | OF SAMPLES | TO BE |
| --- | ----------- | --- | ------ | ----- | ------ | --- | ---------- | ----- |
$
PROCESSED’)
C
=
|     | READ(21,*)(DBUF(JJ),JJ |     |     | 1,ITIME) |     |     |     |     |
| --- | ---------------------- | --- | --- | -------- | --- | --- | --- | --- |
IPTR = 1
C
| 30  | WRITE(6,35)       |     |     |     |         |            |     |        |
| --- | ----------------- | --- | --- | --- | ------- | ---------- | --- | ------ |
| 35  | FORMAT(1H$,‘ENTER |     |     | THE | DESIRED | PROCESSING |     | RATE’) |
READ(6,*)DRATE
|     | MFAC                         | = IFIX(FSAMP*LFAC/DRATE) |     |     |     |     |       |     |
| --- | ---------------------------- | ------------------------ | --- | --- | --- | --- | ----- | --- |
|     | IF(MFAC*DRATE.EQ.FSAMP*LFAC) |                          |     |     |     | GO  | TO 40 |     |
C
|     | WRITE(6,*)‘RATE |     | IS  | UNACHIEVABLE |     | –   | TRY AGAIN’ |     |
| --- | --------------- | --- | --- | ------------ | --- | --- | ---------- | --- |
GO TO 30
C

| Conversion | between                  | different | sampling | rates |        |          |          |     | 319 |
| ---------- | ------------------------ | --------- | -------- | ----- | ------ | -------- | -------- | --- | --- |
| 40         | WRITE(6,*)‘INTERPOLATION |           |          |       | FACTOR |          | = ’,LFAC |     |     |
|            | WRITE(6,*)‘DECIMATION    |           |          |       | FACTOR | = ’,MFAC |          |     |     |
C
| C   | *************************************** |     |             |     |     |     |     |     |     |
| --- | --------------------------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| C   | DO                                      | 500 | I = 1,ITIME |     |     |     |     |     |     |
DT = (I-1)/4320
X = FLOAT(DBUF(IPTR)
WRITE(26,*)DT,X
C
|     | DO         | 120J | = 1,NBF-1      |     |     |     |     |     |     |
| --- | ---------- | ---- | -------------- | --- | --- | --- | --- | --- | --- |
|     | INDX       | =    | NBF+1-J        |     |     |     |     |     |     |
| 120 | ZTD1(INDX) |      | = ZTD1(INDX-1) |     |     |     |     |     |     |
|     | ZTD1(1)    |      | = X            |     |     |     |     |     |     |
C
N0 = N0+LFAC
|     | IF(N0.LT.MFAC) |     | GO  | TO  | 500 |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
C
N0 = N0-MFAC
C
|     | ZOUT | =    | 0.                   |     |     |     |     |     |     |
| --- | ---- | ---- | -------------------- | --- | --- | --- | --- | --- | --- |
|     | DO   | 130J | = 1,NBF              |     |     |     |     |     |     |
|     | INDX | =    | J*LFAC-N0            |     |     |     |     |     |     |
| 130 | ZOUT | =    | ZOUT+HFIL(X)*ZTD1(J) |     |     |     |     |     |     |
|     | ZOUT | =    | ZOUT/FSAMP           |     |     |     |     |     |     |
WRITE(25,*)DT,ZOUT
C
| 500 | CONTINUE |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
STOP
END
|     | PROGRAM                                               |     | FIR       |      |            |        |             |     |     |
| --- | ----------------------------------------------------- | --- | --------- | ---- | ---------- | ------ | ----------- | --- | --- |
| C   | ***************************************************** |     |           |      |            |        |             |     |     |
| C   | IMPUSLE                                               |     | INVARIANT |      | DESIGN FOR | SECOND | ORDER       |     |     |
| C   | LOW-PASS                                              |     | FILTER    | WITH | REAL POLES |        | AT – S1 AND | –   | S2  |
C
| C   | TRANSFER |     | FUNCTION |     | = A*S1*S2/(S+S1)(S+S2) |     |     |     |     |
| --- | -------- | --- | -------- | --- | ---------------------- | --- | --- | --- | --- |
C
| C   | SAMPLING |     | RATE    | OF 216000 | AT 60HZ |     |     |     |     |
| --- | -------- | --- | ------- | --------- | ------- | --- | --- | --- | --- |
| C   | 180000   |     | AT 50HZ |           |         |     |     |     |     |
C
| C   | ONE      | CYCLE | DURATION   |     | FINITE      | IMPULSE | RESPONSE | FILTER |     |
| --- | -------- | ----- | ---------- | --- | ----------- | ------- | -------- | ------ | --- |
| C   | OBTAINED |       | BY WRITING |     | THE PARTIAL |         | FRACTION |        |     |

320 Appendix C
| C   | EXPANSION                                        | OF THE   | TRANSFER |     | FUNCTION | AND FORMING |
| --- | ------------------------------------------------ | -------- | -------- | --- | -------- | ----------- |
| C   | THE IMPULSE                                      | RESPONSE |          | IN  | THE FORM |             |
| C   | H(T) = SUM(CI*EXP(-SI*T)                         |          |          |     |          |             |
| C   | ************************************************ |          |          |     |          |             |
|     | DIMENSION                                        | h(3600)  |          |     |          |             |
S1 = 394
S2 = 2630
| C   | MAKE GAIN | AT 60HZ |     | = 1 |     |     |
| --- | --------- | ------- | --- | --- | --- | --- |
=
| C   | G60 THE            | INVERSE | OF  | THE              | 60HZ | GAIN                  |
| --- | ------------------ | ------- | --- | ---------------- | ---- | --------------------- |
|     | G60 = (SQRT((S1**2 |         | +   | (377)**2)*(S2**2 |      | + (377)**2)))/(S1*S2) |
C1 = G60*S1*S2/(-S1+S2)
C2 = G60*S1*S2/(S1-S2)
WRITE(20,*)1,3600
C
|     | DO 100 I | = 1,3600 |     |     |     |     |
| --- | -------- | -------- | --- | --- | --- | --- |
DT = (I-1)/216000
H(I) = C1*EXP(-DT*S1)C2*EXP(-DT*S2)
|     | WRITE(20,*) | H(I) |     |     |     |     |
| --- | ----------- | ---- | --- | --- | --- | --- |
| 100 | CONTINUE    |      |     |     |     |     |
C
STOP
END
References
[1] IEEEStandardCommonFormatforTransientDataExchange(COMTRADE)forPower
| Systems. | C37. 111–1991. |     |     |     |     |     |
| -------- | -------------- | --- | --- | --- | --- | --- |

Appendix D
Standard for transient data exchange
Note: At the time of the first edition the IEEE Standard C37.111 was in a draft
form. It has now been issued as a standard by both IEEE and IEC, and is one
of the most used standards in the substation automation and monitoring systems.
This standard format is from a Draft document (now a standard)1 which has
developed and proposed several standards suitable for a computer based protection,
monitoring, and control systems. Although it is likely that some such standard will
be adopted by the industry, it may undergo substantial changes before it is actually
accepted. One should therefore investigate the status of these proposed documents
at the time they are to be used.
Itisrecognizedthattherearevarioussourcesoftransientrecordsfrompowersys-
tems,andmanypotentialusersofthesedata.Forexample,thedatamaybeobtained
from actual power system oscillographs, model system simulators, or digital com-
putersimulationprograms.Thedatacouldbeusedforpost-eventsequence-of-events
analysis, monitoring or equipment health, in checking the performance of various
protective devices, or as an aid in designing newer protection and control algo-
rithms. It thus becomes necessary to agree upon a standard for exchanging these
records between various people at various times in such a fashion that the user may
be assured of finding the data in a well known and agreed upon – in other words, a
standard – format. Many hardware designers would prefer to have such a standard,
so that their output and input, by conforming to this standard will have universal
interface capability.
Theproposedstandardacknowledgesthatoneoftheprimarymethodsofexchang-
ing data among different people would be by mailing the data in their own storage
medium. Therefore, the storage medium proposed in the standard is the 5-1/4 inch
floppydisketteoritsequivalent(suchasthenewer3-1/2inchmicrofloppydiskette)
prepared on the IBM or IBM compatible personal computer using PC-DOS OR
ComputerRelayingforPowerSystems2e byA.G.PhadkeandJ. S.Thorp
2009JohnWiley&Sons,Ltd

322 Appendix D
ms-dos operating systems. The files are in ASCII character format, and will be in
two parts. The first part is the HEADER, and contains such textual information as
the case description, signal conditioning applied to the signals, channels and the
signals recorded on each channel, sampling rate, units of signals on each channel,
time and date when the data were obtained, and any other information which helps
to interpret the data.
The second part of the file consists of the DATA, arranged in rows of sample
values taken at each sampling instant. The sample instant and sample number are
identified, and each data entry is separated by a comma from the next entry. A pro-
vision is made to identify bad samples (invalid samples) with special codes which
are identified in the header information. The reference cited provides an example
of a transient data case stored in the standard format.
References
[1] IEEEStandardCommonFormatforTransientDataExchange(COMTRADE)forPower
Systems. C37. 111–1991.

Index
| Adaptive          | relaying,   | 5,           | 285 |       | Cross-correlation, |              | 191, 271 |
| ----------------- | ----------- | ------------ | --- | ----- | ------------------ | ------------ | -------- |
| Agents,           | 132         |              |     |       | CT, 8,             | 27           |          |
| Amplitude         | modulation, |              | 71  |       | Current            | transformer, | 27, 164  |
| Analog-to-digital |             | converter,   |     | 8, 15 | Cut-off            | frequency,   | 83       |
| Anti-aliasing,    |             | 8, 83        |     |       | CVT, 27,           | 180          |          |
| Architecture,     |             | 6            |     |       |                    |              |          |
| Area control      |             | error (ACE), |     | 302   | Data window,       |              | 126      |
| Artificial        | Neural      | Networks,    |     | 129   | DC component,      |              | 51       |
| Auto-correlation, |             | 95           |     |       | DC offset,         | 149          |          |
|                   |             |              |     |       | Removal,           | 163          |          |
| Auxiliary         | current     | transformer, |     | 8     |                    |              |          |
| Auxiliary         | relays,     | 222          |     |       | Decision           | Trees,       | 131      |
|                   |             |              |     |       | Dependability,     |              | 28       |
| Back-up,          | 21          |              |     |       | DFT, 84            |              |          |
| BEAMA,            | 220         |              |     |       | Difference         | Equation,    | 171      |
Bewley lattice diagram, 259 Differential equation algorithm, 159
Blackman Harris Window, 123 Differential protection of stator
| Breaker         | health  | monitoring, |     | 250 | windings,    | 200      |         |
| --------------- | ------- | ----------- | --- | --- | ------------ | -------- | ------- |
| Bus protection, |         | 28,         | 189 |     | Differential | relay,   | 40, 191 |
| Butterworth     | filter, | 17,         | 120 |     | Digital      | filters, | 113     |
|                 |         |             |     |     | Directional  | relay,   | 30      |
Capacitive voltage transformer, Discrete Fourier Transform (DFT), 84
| 47,                               | 221         |     |     |                   | Discrete     | Time       |         |
| --------------------------------- | ----------- | --- | --- | ----------------- | ------------ | ---------- | ------- |
| Chebyshev,                        | 17          |     |     |                   | Systems,     | 109        |         |
| Circuit                           | breaker,    | 27  |     |                   |              |            |         |
|                                   |             |     |     |                   | Convolution, |            | 110     |
| Clarke                            | components, |     | 169 |                   | Fourier      | Transform, | 118     |
| Computer                          | relaying,   |     | 1   |                   | Ideal        | Low-pass,  | 118     |
| Convolution,                      |             | 76  |     |                   | Discriminant | function,  | 267     |
| Covariance,                       | 91          |     |     |                   | Distance     | relay,     | 35, 170 |
| ComputerRelayingforPowerSystems2e |             |     |     | byA.G.PhadkeandJ. |              | S.Thorp    |         |
2009JohnWiley&Sons,Ltd

324 Index
Electromagnetic interference (EMI), Inverse Fourier Transform, 65
| 217                   |            |             |     | Inverse             | time,           | 179     |     |
| --------------------- | ---------- | ----------- | --- | ------------------- | --------------- | ------- | --- |
| EMP, 217              |            |             |     | Inverse             | z Transform,    |         | 115 |
| EPROM,                | 7          |             |     | Islanding,          | 303             |         |     |
| Equal area            | criterion, | 297         |     |                     |                 |         |     |
|                       |            |             |     | Joint distribution, |                 | 90      |     |
| Estimation,           | 92         |             |     |                     |                 |         |     |
| excitation            | systems,   | 302         |     |                     |                 |         |     |
|                       |            |             |     | k-algorithm,        | 173             |         |     |
| Expectation,          |            | 89          |     |                     |                 |         |     |
|                       |            |             |     | Kalman              | filter,         | 96      |     |
| FACTS,                | 249        |             |     | Karrenbauer         | transformation, |         | 267 |
| Fast Transient        |            | test, 218   |     |                     |                 |         |     |
| Fault classification, |            | 130         |     | Least square        | solution,       |         | 93  |
|                       |            |             |     | Linear Phase,       |                 | 70, 122 |     |
| Fault location        |            | algorithms, | 2   |                     |                 |         |     |
| FFT, 85               |            |             |     | Load shedding,      |                 | 233     |     |
| Filter Bank,          | 126        |             |     | Loss of             | Field,          | 203,    | 302 |
| Filter Synthesis,     |            | 124         |     | Low pass            | filters         |         |     |
| Flattop               | Window,    | 123         |     | Butterworth,        |                 | 120     |     |
|                       |            |             |     | Chebeyshev,         |                 | 17      |     |
| Forward               | waves,     | 259         |     |                     |                 |         |     |
| Fourier               | series,    | 55          |     | Ideal,              | 67              |         |     |
| Exponential,          |            | 58          |     |                     |                 |         |     |
| Sine-cosine,          |            | 60          |     | Maintenance,        |                 | 213     |     |
| Fourier               | transform, | 63          |     | Modal quantities,   |                 | 262     |     |
|                       |            |             |     | Modes               | of propagation, |         | 266 |
| Fourier-Walsh         |            | expansion,  | 63  |                     |                 |         |     |
| Fractional            | cycle      | windows,    | 151 | Modulation,         | 71              |         |     |
MOV, 9
| Gain error, | 13          |     |     | Multiplexer,   | 10          |        |              |
| ----------- | ----------- | --- | --- | -------------- | ----------- | ------ | ------------ |
| Gaussian    | density,    | 34  |     | Multi-terminal |             | lines, | 273          |
| Gaussian    | pulse,      | 74  |     |                |             |        |              |
| Generator   | protection, |     | 189 | NAVSTAR        | satellites, |        | 234          |
|             |             |     |     | Negative       | sequence,   |        | 43, 180      |
| Hamming     | Window,     | 121 |     | Nonlinearity,  |             | 13     |              |
| Histogram,  | 87          |     |     | Nyquist        | rate,       | 83     |              |
| HVDC        | lines,      | 249 |     |                |             |        |              |
|             |             |     |     | Offset error,  | 13          |        |              |
| IEC, 220    |             |     |     | Orthogonal     | expansions, |        | 62           |
| IEC61850,   | 133         |     |     | Out-of-step    | relaying,   |        | 43, 203, 295 |
IEEE, 6
|                |               |            |     | Overcurrent      | relay,            | 26,        | 204        |
| -------------- | ------------- | ---------- | --- | ---------------- | ----------------- | ---------- | ---------- |
| Incipient      | fault         | detection, | 248 | Over-defined     |                   | equations, | 92         |
| Information    | matrix,       | 101        |     |                  |                   |            |            |
| Integration,   | 4             |            |     | Parks MaClellan, |                   | 125        |            |
| Interarea      | Oscillations, |            | 249 | Phasors,         | 62                |            |            |
| Interface      | panel,        | 223        |     | Phasor           | Data Concentrator |            | (PDC), 291 |
| Interpolation, |               | 107        |     | PMU, 235         |                   |            |            |

Index 325
| PMU          | locations, |               | 244  |     | Ratio,            | 30       |             |        |
| ------------ | ---------- | ------------- | ---- | --- | ----------------- | -------- | ----------- | ------ |
| Positive     | sequence,  |               | 171, | 203 | Time-overcurrent, |          | 32          |        |
| Power        | series,    | 113           |      |     | Reliability,      | 28,      | 205         |        |
| Power        | supply,    |               | 7    |     | Remanence,        | 41       |             |        |
| Probability, |            | 86            |      |     | Remedial          | Action   | Scheme      | (RAS), |
| Probability  |            | density,      | 88   |     | 304               |          |             |        |
| Probability  |            | distribution, |      | 88  | Remote            | terminal | unit (RTU), | 235    |
| Programming  |            | languages,    |      | 6   | Removal           | of dc    | offset,     | 163    |
| PROM,        | 7          |               |      |     | Reverse           | waves,   | 265         |        |
| Propagation  |            | velocity,     |      | 255 | R-X diagram,      |          | 36          |        |
Protection
| Bus,         | 205  |              |        |     | Sample              | and hold, | 10      |     |
| ------------ | ---- | ------------ | ------ | --- | ------------------- | --------- | ------- | --- |
|              |      |              |        |     | Sampling,           | 2,        | 22, 81  |     |
| Generator,   |      | 200          |        |     |                     |           |         |     |
| Motor,       |      | 204          |        |     | SCDFT,              | 172       |         |     |
| Series       |      | Compensated, |        | 183 | SCDR,               | 180       |         |     |
|              | Line |              |        |     | Security,           | 21,       | 51, 237 |     |
| Transformer, |      |              | 190    |     | Self-checking,      |           | 4       |     |
|              |      |              |        |     | Sequence-of-events, |           | 20      |     |
| Transmission |      |              | Lines, | 30  |                     |           |         |     |
| PSS,         | 244  |              |        |     | Shielding,          | 9,        | 217     |     |
|              |      |              |        |     | Shift theorem,      |           | 71      |     |
Quantization error, 12, 216 Special Protection System (SPS), 304
|               |             |            |     |     | Speed-reach       | consideration, |               | 147      |
| ------------- | ----------- | ---------- | --- | --- | ----------------- | -------------- | ------------- | -------- |
| RAM,          | 7           |            |     |     | Stability,        | 131,           | 245, 294      |          |
| Random        | process,    |            | 94  |     | Standard          | deviation,     | 90,           | 178      |
| Filtering     |             | of,        | 97  |     | State estimation, |                | 234           |          |
| Sample        |             | functions, |     | 94  | Dynamic,          | 245            |               |          |
| Random        | variables,  |            | 87  |     | Linear,           | 238            |               |          |
| Independence, |             |            | 91  |     | Partition,        | 242            |               |          |
| Expectation,  |             |            | 89  |     | Using             | Phasors,       | 245           |          |
| Ratio         | Test,       | 114        |     |     | Substation,       | 2,             | 190           |          |
| RC            | filter,     | 17         |     |     | Environment,      |                | 216           |          |
| Reactor       | protection, |            | 43  |     | Host,             | 20, 224,       | 229           |          |
| Redundancy,   |             | 205        |     |     | Sudden            | pressure       | relay,        | 42       |
| Relays        |             |            |     |     | Surge impedance,  |                | 221,          | 257      |
| Bus,          | 44          |            |     |     | Surge withstand   |                | capability    | (SWC),   |
| Differential, |             |            | 30  |     | 217               |                |               |          |
| Directional,  |             | 32         |     |     |                   |                |               |          |
|               |             |            |     |     | Swing equation,   |                | 297           |          |
| Distance,     |             | 35         |     |     | Symmetrical       |                | components,   | 170, 204 |
| Magnitude,    |             | 30         |     |     | Synchronization   |                | with phasors, | 274      |
| Motor,        |             | 204        |     |     | Synchronized      |                | sampling,     | 182      |
| Over-Current, |             |            | 30  |     | System            | integration,   | 4             |          |
Percentage Differential, 40 System Integrity Protection Scheme
| Pilot, | 30, | 39  |     |     | (SIPS), | 304 |     |     |
| ------ | --- | --- | --- | --- | ------- | --- | --- | --- |

| 326            |                    |          |                  |             |            | Index    |
| -------------- | ------------------ | -------- | ---------------- | ----------- | ---------- | -------- |
| Test switches, | 222                |          | Traveling        | wave        | relay, 256 |          |
| Training,      | 129, 214           |          | Traveling        | waves,      | 182,       | 248, 255 |
| Transfer       | function, 16,      | 67, 117  |                  |             |            |          |
| Transformer    | algorithms,        | 85, 190  | Unit step,       | 115         |            |          |
| Current        | derived restraint, | 191      |                  |             |            |          |
| Flux           | restraint, 195     |          | Variance,        | 90,         | 150, 241   |          |
| Inverse        | inductance,        | 199      |                  |             |            |          |
|                |                    |          | Walsh functions, |             | 63         |          |
| Transformer    | protection,        | 2, 130,  |                  |             |            |          |
| 189            |                    |          | Wavelets,        | 125         |            |          |
|                |                    |          | Weighted         | least       | square,    | 93, 235  |
| Transient      | monitor, 174,      | 194, 229 |                  |             |            |          |
| Transient      | response           |          | Wide Area        | Measurement |            |          |
|                |                    |          | System,          | 291         |            |          |
| Of current     | transformers,      | 46       |                  |             |            |          |
|                |                    |          | Wide Area        | Measurement |            |          |
| Of voltage     | transformers,      | 47       |                  |             |            |          |
| Transients,    | 8, 51, 182         |          | Protection       | and         | Control,   | 293      |
|                |                    |          | System,          | 291         |            |          |
| Transmission   | line algorithms,   | 137      |                  |             |            |          |
| Curve          | fitting, 149       |          | Windowing,       | 121         |            |          |
|                |                    |          | Windows,         | 121         |            |          |
| Differential   | equation,          | 155      |                  |             |            |          |
| Fourier,       | 149                |          |                  |             |            |          |
|                |                    |          | z Transforms,    |             | 113        |          |
| Kalman,        | 162                |          |                  |             |            |          |
|                |                    |          | Zero sequence,   |             | 35, 182,   | 262      |
| Recursive      | Fourier,           | 152      |                  |             |            |          |
| Walsh,         | 154                |          | Zones of         | protection, | 28,        | 295, 244 |