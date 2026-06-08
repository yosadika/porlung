IEEE Guide for Protective Relay
Applications to Transmission Lines
IEEE Power and Energy Society
Sponsored by the
Power System Relaying Committee
IEEE
IEEE Std C37.113™-2015
3 Park Avenue
(Revision of
New York, NY 10016-5997
IEEE Std C37.113-1999)
USA
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113™-2015
(Revision of
IEEE Std C37.113-1999)
IEEE Guide for Protective Relay
Applications to Transmission Lines
Sponsor
Power System Relaying Committee
of the
IEEE Power and Energy Society
Approved 5 December 2015
IEEE-SA Standards Board
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

Abstract: Information on the concepts of protection of ac transmission lines is presented in this
guide. Applications of the concepts to accepted transmission line-protection schemes are also
presented. Many important issues, such as coordination of settings, operating times,
characteristics of relays, mutual coupling of lines, automatic reclosing, and use of communication
channels, are examined. Special protection systems, protection of multi-terminal lines, and single-
phase tripping and reclosing are also included. The impact of different electrical parameters and
system performance considerations on the selection of relays and protection schemes is
discussed.
The purpose of this guide is to provide a reference for the selection of relay schemes and to
assist less experienced protective relaying engineers in applying protection schemes to
transmission lines.
Keywords: distance protection, IEEE C37.113™, pilot protection, protective relaying, relay
application, relaying, transmission line protection

The Institute of Electrical and Electronics Engineers, Inc.
3 Park Avenue, New York, NY 10016-5997, USA
Copyright © 2016 by The Institute of Electrical and Electronics Engineers, Inc.
All rights reserved. Published 30 June 2016. Printed in the United States of America.
IEEE is a registered trademark in the U.S. Patent & Trademark Office, owned by The Institute of Electrical and Electronics Engineers,
Incorporated.
PDF: ISBN 978-1-5044-0654-3 STD20774
Print: ISBN 978-1-5044-0655-0 STDPD20774
IEEE prohibits discrimination, harassment, and bullying.
For more information, visit http://www.ieee.org/web/aboutus/whatis/policies/p9-26.html.
No part of this publication may be reproduced in any form, in an electronic retrieval system or otherwise, without the prior written permission
of the publisher.
2
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

Important Notices and Disclaimers Concerning IEEE Standards Documents
IEEE documents are made available for use subject to important notices and legal disclaimers. These notices
and disclaimers, or a reference to this page, appear in all standards and may be found under the heading
“Important Notice” or “Important Notices and Disclaimers Concerning IEEE Standards Documents.”
Notice and Disclaimer of Liability Concerning the Use of IEEE Standards
Documents
IEEE Standards documents (standards, recommended practices, and guides), both full-use and trial-use, are
developed within IEEE Societies and the Standards Coordinating Committees of the IEEE Standards
Association (“IEEE-SA”) Standards Board. IEEE (“the Institute”) develops its standards through a
consensus development process, approved by the American National Standards Institute (“ANSI”), which
brings together volunteers representing varied viewpoints and interests to achieve the final product.
Volunteers are not necessarily members of the Institute and participate without compensation from IEEE.
While IEEE administers the process and establishes rules to promote fairness in the consensus development
process, IEEE does not independently evaluate, test, or verify the accuracy of any of the information or the
soundness of any judgments contained in its standards.
IEEE does not warrant or represent the accuracy or content of the material contained in its standards, and
expressly disclaims all warranties (express, implied and statutory) not included in this or any other
document relating to the standard, including, but not limited to, the warranties of: merchantability; fitness
for a particular purpose; non-infringement; and quality, accuracy, effectiveness, currency, or completeness
of material. In addition, IEEE disclaims any and all conditions relating to: results; and workmanlike effort.
IEEE standards documents are supplied “AS IS” and “WITH ALL FAULTS.”
Use of an IEEE standard is wholly voluntary. The existence of an IEEE standard does not imply that there
are no other ways to produce, test, measure, purchase, market, or provide other goods and services related
to the scope of the IEEE standard. Furthermore, the viewpoint expressed at the time a standard is approved
and issued is subject to change brought about through developments in the state of the art and comments
received from users of the standard.
In publishing and making its standards available, IEEE is not suggesting or rendering professional or other
services for, or on behalf of, any person or entity nor is IEEE undertaking to perform any duty owed by any
other person or entity to another. Any person utilizing any IEEE Standards document, should rely upon his
or her own independent judgment in the exercise of reasonable care in any given circumstances or, as
appropriate, seek the advice of a competent professional in determining the appropriateness of a given
IEEE standard.
IN NO EVENT SHALL IEEE BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO:
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE PUBLICATION, USE OF, OR RELIANCE
UPON ANY STANDARD, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE AND
REGARDLESS OF WHETHER SUCH DAMAGE WAS FORESEEABLE.
Translations
The IEEE consensus development process involves the review of documents in English only. In the event
that an IEEE standard is translated, only the English version published by IEEE should be considered the
approved IEEE standard.
3
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

Official statements
A statement, written or oral, that is not processed in accordance with the IEEE-SA Standards Board
Operations Manual shall not be considered or inferred to be the official position of IEEE or any of its
committees and shall not be considered to be, or be relied upon as, a formal position of IEEE. At lectures,
symposia, seminars, or educational courses, an individual presenting information on IEEE standards shall
make it clear that his or her views should be considered the personal views of that individual rather than the
formal position of IEEE.
Comments on standards
Comments for revision of IEEE Standards documents are welcome from any interested party, regardless of
membership affiliation with IEEE. However, IEEE does not provide consulting information or advice
pertaining to IEEE Standards documents. Suggestions for changes in documents should be in the form of a
proposed change of text, together with appropriate supporting comments. Since IEEE standards represent a
consensus of concerned interests, it is important that any responses to comments and questions also receive
the concurrence of a balance of interests. For this reason, IEEE and the members of its societies and
Standards Coordinating Committees are not able to provide an instant response to comments or questions
except in those cases where the matter has previously been addressed. For the same reason, IEEE does not
respond to interpretation requests. Any person who would like to participate in revisions to an IEEE
standard is welcome to join the relevant IEEE working group.
Comments on standards should be submitted to the following address:
Secretary, IEEE-SA Standards Board
445 Hoes Lane
Piscataway, NJ 08854 USA
Laws and regulations
Users of IEEE Standards documents should consult all applicable laws and regulations. Compliance with
the provisions of any IEEE Standards document does not imply compliance to any applicable regulatory
requirements. Implementers of the standard are responsible for observing or referring to the applicable
regulatory requirements. IEEE does not, by the publication of its standards, intend to urge action that is not
in compliance with applicable laws, and these documents may not be construed as doing so.
Copyrights
IEEE draft and approved standards are copyrighted by IEEE under U.S. and international copyright laws.
They are made available by IEEE and are adopted for a wide variety of both public and private uses. These
include both use, by reference, in laws and regulations, and use in private self-regulation, standardization,
and the promotion of engineering practices and methods. By making these documents available for use and
adoption by public authorities and private users, IEEE does not waive any rights in copyright to the
documents.
Photocopies
Subject to payment of the appropriate fee, IEEE will grant users a limited, non-exclusive license to
photocopy portions of any individual standard for company or organizational internal use or individual,
non-commercial use only. To arrange for payment of licensing fees, please contact Copyright Clearance
Center, Customer Service, 222 Rosewood Drive, Danvers, MA 01923 USA; +1 978 750 8400. Permission
to photocopy portions of any individual standard for educational classroom use can also be obtained
through the Copyright Clearance Center.
4
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

Updating of IEEE Standards documents
Users of IEEE Standards documents should be aware that these documents may be superseded at any time
by the issuance of new editions or may be amended from time to time through the issuance of amendments,
corrigenda, or errata. An official IEEE document at any point in time consists of the current edition of the
document together with any amendments, corrigenda, or errata then in effect.
Every IEEE standard is subjected to review at least every ten years. When a document is more than ten
years old and has not undergone a revision process, it is reasonable to conclude that its contents, although
still of some value, do not wholly reflect the present state of the art. Users are cautioned to check to
determine that they have the latest edition of any IEEE standard.
In order to determine whether a given document is the current edition and whether it has been amended
through the issuance of amendments, corrigenda, or errata, visit the IEEE-SA Website at
http://ieeexplore.ieee.org/xpl/standards.jsp or contact IEEE at the address listed previously. For more
information about the IEEE SA or IEEE’s standards development process, visit the IEEE-SA Website at
http://standards.ieee.org.
Errata
Errata, if any, for all IEEE standards can be accessed on the IEEE-SA Website at the following URL:
http://standards.ieee.org/findstds/errata/index.html. Users are encouraged to check this URL for errata
periodically.
Patents
Attention is called to the possibility that implementation of this standard may require use of subject matter
covered by patent rights. By publication of this standard, no position is taken by the IEEE with respect to
the existence or validity of any patent rights in connection therewith. If a patent holder or patent applicant
has filed a statement of assurance via an Accepted Letter of Assurance, then the statement is listed on the
IEEE-SA Website at http://standards.ieee.org/about/sasb/patcom/patents.html. Letters of Assurance may
indicate whether the Submitter is willing or unwilling to grant licenses under patent rights without
compensation or under reasonable rates, with reasonable terms and conditions that are demonstrably free of
any unfair discrimination to applicants desiring to obtain such licenses.
Essential Patent Claims may exist for which a Letter of Assurance has not been received. The IEEE is not
responsible for identifying Essential Patent Claims for which a license may be required, for conducting
inquiries into the legal validity or scope of Patents Claims, or determining whether any licensing terms or
conditions provided in connection with submission of a Letter of Assurance, if any, or in any licensing
agreements are reasonable or non-discriminatory. Users of this standard are expressly advised that
determination of the validity of any patent rights, and the risk of infringement of such rights, is entirely
their own responsibility. Further information may be obtained from the IEEE Standards Association.
5
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

Participants
At the time this IEEE guide was completed, the D19 Working Group had the following membership:
Don Lukach, Chair
Jeffrey Barsch, Vice Chair
| Martin Best       | Alexis Mezco    | Mohindar Sachdev      |
| ----------------- | --------------- | --------------------- |
| Gustavo Brunello  | Dean Miller     | Phil Tatro            |
| David Circa       | John Miller     | Richard Taylor        |
| Stephen Conrad    | Joe Mooney      | Michael Thompson      |
| Randall Cunico    | James O’Brien   | Ian Tualla            |
| Alla Deronja      | Dean Ouellette  | Demetrios Tziouvaras  |
| Normann Fischer   | Claire Patti    | Jun Verzosa           |
| Dom Fontana       | Elmo Price      | Solveig Ward          |
| Gary Kobet        | Sam Sambasivan  | Roger Whittaker       |
| Walter McCannon   |                 | Zhiying Zhang         |

During work on the draft guide, both Richard Taylor and Mohindar Sachdev worked in the capacity of
Working Group Chair. Their contributions were greatly appreciated.
The following members of the individual balloting committee voted on this guide. Balloters may have
voted for approval, disapproval, or abstention.
| William Ackerman      | Jalal Gohari     | Joe Nims             |
| --------------------- | ---------------- | -------------------- |
| Ali Al Awazi          | Stephen Grier    | Gary Nissen          |
| Steven Alexanderson   | Randall Groves   | James O”Brien        |
| Jay Anderson          | Ajit Gwal        | Dean Ouellette       |
| John Anderson         | Roger Hedding    | Lorraine Padden      |
| Thomas Barnes         | David Horvath    | Christopher Petrola  |
| Jeffrey Barsch        | Gerald Johnson   | Michael Roberts      |
| G. Bartok             | Innocent Kamwa   | Charles Rogers       |
| David Beach           | John Kay         | Mohindar Sachdev     |
| Philip Beaumont       | James Kinney     | Steven Sano          |
| Martin Best           | Gary Kobet       | Bartien Sayogo       |
| Wallace Binder        | Boris Kogan      | Thomas Schossig      |
| Thomas Blair          | Jim Kulchisky    | Tony Seegers         |
| Clarence Bradley      | Saumen Kundu     | Nikunj Shah          |
| Chris Brooks          | Marc Lacroix     | Suresh Shrimavle     |
| Gustavo Brunello      | Chung-Yiu Lam    | Mark Simon           |
| William Byrd          | Michael Lauxman  | Jerry Smith          |
| Paul Cardinal         | Albert Livshitz  | Wayne Stec           |
| Suresh Channarasappa  | Don Lukach       | Michael Thompson     |
| Arvind Chaudhary      | Bruce Mackie     | Joe Uchiyama         |
| Stephen Conrad        | O. Malik         | John Vergis          |
| James Cornelison      | Omar Mazzoni     | Jane Verner          |
| Luis Coronado         | William McBride  | Quintin Verzosa      |
| Randall Crellin       | Walter McCannon  | Ilia Voloh           |
| Randall Cunico        | Dean Miller      | Yingli Wen           |
| Ratan Das             | John Miller      | Kenneth White        |
| Kevin Donahoe         | Joe Mooney       | Roger Whittaker      |
| Carlo Donati          | Adi Mulawarman   | Philip Winston       |
| Gary Donner           | Jerry Murphy     | Ray Young            |
| Randall Dotson        | R. Murphy        | Richard Young        |
| Frank Gerleve         | Bruce Muschlitz  | Jian Yu              |
|                       | Michael Newman   |                      |
6
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

When the IEEE-SA Standards Board approved this guide on 5 December 2015, it had the following
membership:
John D. Kulick, Chair
Jon Walter Rosdahl, Vice Chair
Richard H. Hulett, Past Chair
Konstantinos Karachalios, Secretary
Masayuki Ariyoshi  Joseph L. Koepfinger*  Stephen J. Shellhammer
| Ted Burse            | David J. Law        | Adrian P. Stephens  |
| -------------------- | ------------------- | ------------------- |
| Stephen Dukes        | Hung Ling           | Yatin Trivedi       |
| Jean-Philippe Faure  | Andrew Myles        | Phillip Winston     |
| J. Travis Griffith   | T. W. Olsen         | Don Wright          |
| Gary Hoffman         | Glenn Parsons       | Yu Yuan             |
| Michael Janezic      | Ronald C. Petersen  | Daidi Zhong         |
|                      | Annette D. Reilly   |                     |
*Member Emeritus

7
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

Introduction
This introduction is not part of IEEE Std C37.113-2015, IEEE Guide for Protective Relay Applications to Transmission
Lines.
This document is a revision of IEEE Std C37.113-1999 [B65]. This guide is intended to assist protection
engineers and technologists in effectively applying relays and protection systems to protect transmission
lines.
Several areas have been improved in this revision, most notably the following:
 Several clauses revised for uniformity of style and ease of understanding the issues discussed in
them
 Enhanced fundamental discussions
 Better defined technical discussion about length considerations
 Updated relay schemes with current technology
 Added Annex A that describes system studies
8
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

Contents
1. Overview ...................................................................................................................................................11
1.1 Scope ..................................................................................................................................................11
1.2 Purpose ...............................................................................................................................................12
2. Normative references .................................................................................................................................12
3. Definitions, device numbers, and abbreviations ........................................................................................12
3.1 Definitions ..........................................................................................................................................12
3.2 Device numbers ..................................................................................................................................15
3.3 Acronyms and abbreviations ..............................................................................................................15
4. Fundamentals .............................................................................................................................................16
4.1 General ...............................................................................................................................................16
4.2 Transmission line ................................................................................................................................16
4.3 Single-line representation of lines and equipment ..............................................................................17
4.4 Zone of protection ..............................................................................................................................19
4.5 Line-relaying selection .......................................................................................................................20
4.6 Redundancy and backup considerations .............................................................................................25
4.7 Autoreclosing methods .......................................................................................................................28
4.8 Effects of load on line relay applications and settings ........................................................................29
5. Impact of system configuration on selection of protection schemes .........................................................31
5.1 General ...............................................................................................................................................31
5.2 Length considerations .........................................................................................................................31
5.3 Line design considerations .................................................................................................................35
5.4 Number of line terminals ....................................................................................................................36
5.5 Lines terminated into transformers .....................................................................................................36
5.6 Weak electrical systems ......................................................................................................................43
5.7 Ground path configurations ................................................................................................................45
5.8 Transmission lines with distribution substation taps ..........................................................................48
5.9 Lines with devices for voltampere reactive and flow control .............................................................52
5.10 Parallel lines .....................................................................................................................................54
5.11 Lines with high-impedance ground returns ......................................................................................55
5.12 Terminal configuration considerations .............................................................................................57
5.13 Mutual coupling considerations ........................................................................................................59
6. Relay schemes ...........................................................................................................................................62
6.1 General ...............................................................................................................................................62
6.2 Non-pilot schemes ..............................................................................................................................62
6.3 Pilot schemes ......................................................................................................................................73
6.4 Other protection schemes ...................................................................................................................87
6.5 Directional ground overcurrent relay polarization ..............................................................................92
6.6 Problems associated with multi-terminal lines ...................................................................................96
6.7 Application considerations of distance relays ...................................................................................100
6.8 Relay considerations for series-compensated lines ...........................................................................114
6.9 Single-phase tripping and reclosing ..................................................................................................117
6.10 Application of distance relays to short lines ...................................................................................122
6.11 Relay considerations for system transients .....................................................................................126
7. Concluding remarks .................................................................................................................................131
9
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

Annex A (informative) System studies needed for setting relays ................................................................132
A.1 System studies—General .................................................................................................................132
A.2 Fault study .......................................................................................................................................132
A.3 Special studies .................................................................................................................................133
Annex B (informative) Bibliography...........................................................................................................134
10
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Guide for Protective Relay
Applications to Transmission Lines
IMPORTANT NOTICE: IEEE Standards documents are not intended to ensure safety, security, health,
or environmental protection, or ensure against interference with or from other devices or networks.
Implementers of IEEE Standards documents are responsible for determining and complying with all
appropriate safety, security, environmental, health, and interference protection practices and all
applicable laws and regulations.
This IEEE document is made available for use subject to important notices and legal disclaimers. These
notices and disclaimers appear in all publications containing this document and may be found under the
heading “Important Notice” or “Important Notices and Disclaimers Concerning IEEE Documents.” They
can also be obtained on request from IEEE or viewed at http://standards.ieee.org/IPR/disclaimers.html.
1. Overview
Each component on the electrical power system has protection problems unique to itself, but the concepts
associated with transmission line protection are fundamental to all other electrical devices and provide an
excellent starting point to examine and appreciate the implementation of protection of most components of
power systems. A study of transmission line protection leads to a better appreciation of protection-related
issues because transmission lines are links to substation buses and/or other equipment connected to the
lines. Electrical engineers and technologists working with electric power utilities; consultants and
manufacturers in general; and those working in designing, selecting, and maintaining protection systems in
particular would benefit from the information provided in this guide.
General specifications of relays are given in IEEE Std 37.90™, IEEE Standard for Relays and Relay
Systems Associated with Electric Power Apparatus.1 While protection of transmission lines is discussed in
this guide, protection of distribution lines is addressed in IEEE Std C37.230™, IEEE Guide for Protective
Relay Applications to Distribution Lines [B68].2
All interrupting devices are shown in the figures included in this guide. The isolators (disconnects) used in
conjunction with the interrupting devices are not shown in all figures. If they are not shown, they are
assumed to be provided for proper control and operation of the system.
1.1 Scope
Concepts of transmission line protection are discussed in this guide. Applications of these concepts to
various system configurations and line termination arrangements are presented. Many important issues,
1 Information on references can be found in Clause 2.
2 The numbers in brackets correspond to those of the bibliography in Annex B.
11
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
such as coordination of settings, operating times, characteristics of relays, impact of mutual coupling of
lines on the protection systems, automatic reclosing, and use of communication channels, are examined.
Special protection systems, multi-terminal lines, and single-phase tripping and reclosing are also included.
The impact that system parameters and system performance have on the selection of relays and relay
schemes is discussed as well.
1.2 Purpose
The purpose of this guide is to provide protection engineers with information that helps them to properly
apply relays and other devices to protect three-phase high-voltage transmission lines.
2. Normative references
The following referenced documents are indispensable for the application of this document (i.e., they must
be understood and used, so each referenced document is cited in text and its relationship to this document is
explained). For dated references, only the edition cited applies. For undated references, the latest edition of
the referenced document (including any amendments or corrigenda) applies.
IEEE Std C37.2™, IEEE Standard Electrical Power System Device Function Numbers, Acronyms, and
Contact Designations.3, 4
IEEE Std C37.90™, IEEE Standard for Relays and Relay Systems Associated with Electric Power Apparatus.
3. Definitions, device numbers, and abbreviations
3.1 Definitions
For the purposes of this document, the following terms and definitions apply. The IEEE Standards
Dictionary Online should be consulted for terms not defined in this clause.5
adaptive relay: A relay that can change its setting and/or relaying logic upon the occurrence of an external
signal or event.
adaptive relaying: A protection philosophy that permits, and seeks to make adjustments automatically, in
various protection functions to make them more attuned to prevailing power conditions.
apparent impedance: The impedance from a relay location to a fault as determined by a distance relay
from the applied current and voltage. It may be different from the actual impedance because of current
infeed or current outfeed at some point between the relay and the fault.
arc resistance: The impedance of an arc that is predominantly resistive; it is a function of the magnitude of
the current and length of the arc.
3 IEEE publications are available from the Institute of Electrical and Electronics Engineers (http://standards.ieee.org/).
4 The IEEE standards or products referred to in this clause are trademarks of the Institute of Electrical and Electronics Engineers, Inc.
5 IEEE Standards Dictionary Online is available at: http://ieeexplore.ieee.org/xpls/dictionary.jsp.
12
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
backup zone: The segment of the power system for which a relay or element within a relay offers
protection that is in addition to its primary protection zone. The backup protection zone relays or elements
are coordinated with the remote zone relays or elements and usually contain a coordination time delay. The
backup zone may disconnect more power system elements than those isolated by the operation of the relays
that protect the primary zone.
blocking signal: A logic signal, used in a pilot scheme, which is received from a remote terminal to
prevent the instantaneous (pilot time) tripping of the local terminal by the pilot scheme.
breaker failure: The failure of a circuit breaker to operate or to interrupt a fault.
breaker failure protection: A form of protection that is designed to detect the failure of a circuit breaker
to operate or to interrupt a fault. Upon detection of a breaker failure during a fault condition, the scheme is
designed to take appropriate action to clear the fault. Upon detection of a breaker failure during a non-fault
condition, the scheme may take other appropriate action.
NOTE—Detailed description of this protection function is given in IEEE Std C37.119™, IEEE Guide for Breaker
Failure Protection of Power Circuit Breakers [B67].
circuit switcher: A circuit interrupting device with a limited interrupting rating as compared with a circuit
breaker. It is often integrated with a disconnecting switch. Its design usually precludes the integration of
current transformers (CTs).
coordination of protection: The process of choosing current or voltage settings and time delay
characteristics of protective devices, such that operation of the devices will occur in a specified order to
minimize customer service interruption and power system isolation due to a power system disturbance.
cross polarization: The method used by a relay for determining directionality using the voltage(s) from a
healthy (unfaulted) phase(s). One example of this is quadrature polarization.
current differential scheme: A protection scheme designed to detect faults by measuring the differences
between the currents at the terminals of a transmission line.
dependability: The degree of certainty that a protection system will respond when the fault or abnormal
condition the protection system is intended to detect is present.
distance relay: A protective relay in which the response to the input quantities is primarily a function of
the impedance or a component of the impedance of the circuit between the relay and the point of fault.
dual polarization: The method used by a relay for determining directionality using both current and
voltage sources.
fault impedance: Impedance, resistive or reactive, between phase conductors or the phase conductor and
ground during a power system fault.
ground distance relay: A distance relay designed to detect phase-to-ground faults.
grounding transformer: Delta-wye or zigzag connected transformer(s) installed to establish a system
ground that provides a path for zero-sequence current flow assisting in detection of phase-to-ground faults.
hybrid scheme: A relay scheme (usually a pilot scheme) combining the logic of two or more conventional
schemes.
impedance relay: A distance relay in which the threshold of operation depends on the magnitude and
angle of the ratio of the voltage vector to the current vector applied to the relay.
infeed: A flow of fault current from a source that is physically located between a relay location and a fault
location.
13
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
lenticular characteristic: A distance relay characteristic having the shape of a lens on a resistance-
reactance (R-X) diagram.
mho unit: A distance relaying unit that has a circular tripping characteristic that passes through or is offset
from the origin on an R-X diagram.
multi-terminal line: A transmission line that has more than two terminals to which sources of power are
connected. A multi-terminal line can also be considered a line with multiple taps that may not have
connected sources.
outfeed: Flow of current out of a terminal of a line when there is a fault on the line.
overlapping protection: A situation in which the protected zone of one relay overlaps the protected zone
of another relay (usually done to ensure protection of equipment at the border of a protected zone). This is
often necessary due to the location of current transformers (CTs) on equipment.
permissive: Pertaining to a scheme that requires the receipt of a logic signal from the remote terminal(s)
before allowing the tripping of the circuit breaker(s) controlling the line.
phase comparison protection: A form of pilot protection that compares the phase angles of currents at the
terminals of a transmission line. Data from the relay at the remote terminal is provided to the local relay
using a communications channel. This data is utilized by the local relay to develop representations of the
phase angles of the currents measured by the remote relay. These representations are then compared with
the phase angles of the currents measured by the local relay.
phase distance relay: A distance relay designed to detect phase-to-phase and three-phase faults.
pilot scheme: A protection scheme involving relays at two or more line terminals that share data or logic
status via a communication channel for improving the tripping speed and/or coordination.
power swing: A transient power flow due to change in relative angles of generators on the system caused
by a change in transmission or generation configuration.
primary zone: The segment of the power system for which the relay or element within the relay is
principally responsible for protection.
quadrature polarization: A form of cross polarization in which the polarizing voltage is in quadrature
with the voltage of the faulted phase(s). Phase A voltage would be used for polarization during a short
circuit between phases B and C.
quadrilateral characteristic: A distance relay characteristic on an R-X diagram created by a directional
measurement, a reactance measurement, and two resistive measurements.
redundancy: A design of relaying, equipment, and tripping circuits developed with the goal of avoiding
the possibility that a single component failure will prevent the relaying from reliably sensing and isolating a
fault in the protected zone.
reliability: The ability of a protection system to operate correctly taking into consideration both
dependability and security.
security: The degree of certainty that a protection system will not respond when the fault or abnormal
condition the protection system is intended to detect is not present.
segregated phase comparison protection: Similar to phase comparison protection except that the phase
angle data of all phase currents (or all phase and ground currents) measured by the remote relay are sent
separately to the local relay for individual comparison with the phase angle of the currents measured by the
local relay.
14
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
self-checking (by a relay): Self-testing by microprocessor-based relays that checks operation of selected
modules of processor software as well as selected hardware components.
sequential tripping: A situation where a local relay cannot detect and trip for a line fault until one or more
of the remote terminals has opened to remove infeed.
single-phase tripping and reclosing: Opening the interrupters of a circuit breaker in one phase only to isolate
the faulted phase in the event of a single-phase-to-ground fault and reclosing them after some time delay.
source impedance: The impedance of the equivalent source behind a terminal of a transmission line used
in calculating the source impedance ratio for determining the electrical length of the line. In network
applications, this impedance can vary depending on the position of other circuit breakers and switches close
to the transmission line terminal.
source of fault current: A terminal that contributes current to a fault on the protected line.
source-to-line impedance ratio (SIR): The ratio of the source impedance behind a relay terminal to the
line impedance.
step distance: A non-pilot distance relay scheme using multiple reach settings (zones) with time delays
associated with some zones to provide coordination of protection.
switch onto fault protection: A protection scheme that trips the line circuit breaker if it is closed into a
fault. This protection scheme is to clear a line before the breaker at the remote terminal closes or in cases
where there is in insufficient voltage for polarizing the directional elements. Also referred to as line pickup
protection.
transfer trip: A pilot scheme that receives a logic signal from a remote terminal to trip the local terminal
with or without local supervision.
unblocking: Pilot scheme logic that allows a permissive pilot scheme local relay to trip within a time
window if a communication signal, such as an audio tone, power-line carrier, or frequency shift keying, is
lost from the remote relay. The logic is based on the possibility that the communications signal was
interrupted by the occurrence of a line fault.
untransposed: Refers to the physical positions of the phase conductors of a transmission line, which are
not interchanged periodically to balance the mutual impedances between phases.
3.2 Device numbers
The device numbers used in this guide are in accordance with IEEE Std C37.2, IEEE Standard Electrical
Power System Device Function Numbers, Acronyms, and Contact Designations.
3.3 Acronyms and abbreviations
ANSI American National Standards Institute
BCG phase B to phase C to ground fault
CT current transformer
CVT capacitance voltage transformer
DCB directional comparison blocking
DCUB directional comparison unblocking
DUTT direct underreaching transfer trip
EHV extra-high voltage
FSK frequency shift keying
GIC geomagnetically induced currents
15
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
HV high voltage
IOC instantaneous overcurrent
LOP loss of potential
MOV metal oxide varistor
NERC North American Electric Reliability Corporation
POTT permissive overreaching transfer trip
PSRC Power System Relaying Committee
pu per unit
PUTT permissive underreaching transfer trip
RO overreaching (relay element, in figures)
RU underreaching (relay element, in figures)
R-X resistance-reactance
SCADA supervisory control and data acquisition
SCV voltage at the swing center
SIR source-to-line impedance ratio
SVC static var compensator
TOC time overcurrent
UHV ultra-high voltage
var voltampere reactive
VT voltage transformer
4. Fundamentals
4.1 General
It is necessary to review two terms used in this guide before the fundamentals are discussed; the terms are
transmission line and zones of protection.
4.2 Transmission line
Terms such as transmission line, subtransmission line, and distribution line have different connotations
among different utilities. Many issues, such as what constitutes a line terminal, may also vary among
companies. Clauses of this guide address many line configurations and the effect those configurations may
have on the application of systems to protect lines.
For purposes of protection, a “line” is defined by the locations of circuit breakers (or other sectionalizing devices)
that are used to isolate the line from other parts of the power system. The line may include the sections of bus,
overhead conductor, underground cable, and other electrical apparatus (including line traps, series capacitors,
shunt reactors, and transformers) that fall between these circuit breakers. For example, segments from circuit
breaker CB 1 to circuit breaker CB 2 and from circuit breaker CB 3 to circuit breaker CB 4 in Figure 1 are
defined as lines. It would normally be assumed that a line exists when two or more stations are involved or the
circuit breakers are too far apart to allow interconnection of control cables and station ground mats.
Bus A Bus B
CB 1 CB 2
V V
S R
CB 3 CB 4
Figure 1 —Definition of line
16
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
4.3 Single-line representation of lines and equipment
There are many ways to represent electrical systems and the protection schemes applied to them:
 Three-line ac diagrams
 Single-line diagrams
 Single-line diagrams with current transformers (CTs) and voltage transformers (VTs)
 Single-line diagrams with protection, and other related equipment
 DC and ac schematics
 Relay functional diagrams
 Relay logic diagrams
 DC elementary diagrams
Connections of protective relays are shown in their broadest level (minimum detail) in a single-line
diagram shown in Figure 2. Connections shown as single lines are actually three-phase circuits. The relays
are represented as circles labeled “R” (for relay), connected to CTs and VTs. This type of single-line
diagram is useful for understanding the various zones of protection. One of the relays shown in Figure 2 is
labeled “21,” which indicates that this device is a distance relay that is provided to protect the line.
Function numbers are given in IEEE Std C37.2, as already stated in 3.2.
21 Relays R
Current Transformers
R R
Voltage Circuit Breakers
Transformers
R R
Figure 2 —One-line diagram of a sample transmission system
Protection characteristics can be shown on time-current diagrams, R-X diagrams, relay-reach versus
operating time diagrams, or distance to fault versus the zone operating time. Figure 3 shows one method of
representing protective relay characteristics. This particular characteristic is the current-versus-time
characteristic of a time overcurrent relay. The characteristic shows two regions: one in which the relay
operates, and the other in which the relay does not operate. The line separating the regions is the
characteristic curve of the relay. Figure 4 shows the method of representing the operating characteristics of
a distance relay on an R-X diagram. This characteristic, like that on the current-versus-time diagram, also
separates the operate and the non-operate regions. The region of where load plots is illustrated as well on
the R-X diagram.
17
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
10
1.0
0.1
0.01
1.0 10 100
18
Copyright © 2016 IEEE. All rights reserved.
)sdnoces(
emiT
Region of
operation
Region of
non-operation
Current
Multiples of Pick-up
Figure 3 —Extremely inverse time overcurrent characteristics
jX
Z
R
Region of
non-operation is
outside the circle
Z
L
Region of
operation
Load area
R
Figure 4 —Relay characteristics on the R-X plane
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
4.4 Zone of protection
There are many types of protection zones; the following basic protection zones are shown in Figure 5:
 Generator protection zone (a)
 Transformer protection zone (b)
 Bus protection zone (c)
 Line protection zone (d)
 Motor protection zone (e)
 Generator-transformer protection zone (f)
The boundaries of a measuring zone of protection, as applied to protective relays, are determined by the
locations of the CTs that provide currents to the relay; these currents represent the line currents.
Overlapping of zones of protection is an established protection concept whose application is shown in
Figure 6. The placement of CTs for part of station B of Figure 5 is shown in Figure 6. The CT connections
for the generator zone and bus zone relays are also shown in this figure. Detailed discussion of bus
protection is provided in IEEE Std C37.234™ [B69]. Detailed discussion of generator protection is
provided in IEEE Std C37.102™ [B60].
MOTORS
e e
c
b STATION C
c
STATION A STATION B
c
c
f b
a
d d
d d
f b
c
c
STATION B
d
Figure 5 —A sample power system and its zones of protection
19
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Line zone
relays Bus zone
relays
Transformer Generator
zone relays zone relays
Line zone
relays
Figure 6 —The principle of overlapping protection
The boundaries of the zone of protection of a line-protection scheme that uses pilot communication are
clearly defined. However, many line protection practices have unrestricted zones; the start of the zone is
defined by the CT location, but the extent of the zone is determined by measurement of system quantities
that may vary with generation and system configuration changes.
4.5 Line-relaying selection
4.5.1 General
The selection of a system for protecting a line requires that several factors, some of which are mutually
exclusive, should be considered. For example, knowledge of the most probable modes of failure,
recommendations of equipment suppliers, and good practical judgment can assist a protection engineer in
determining the emphasis that each factor should be given.
One of the most important considerations for selecting a protection system is reliability. The reliability of
protection systems is separated into two aspects: dependability and security. Dependability is relatively
easy to obtain in relay design or in the application of a number of relays. Testing using operating conditions
and redundancy are methods to ensure dependability. Security is difficult to attain; an almost infinite
variety of tests would be needed to simulate all possible conditions to which a relay may be exposed.
Various engineering practices can enhance dependability. These include the following:
 Application of redundant relay systems with independence of design.
 Application of redundant relay systems with different operating principles.
 Redundancy within the relay systems.
 Local backup methods.
 Remote backup methods.
Security can be enhanced by various practices, such as the following:
 Application of relays and relay systems that do not cause undesirable trips upon failure.
 Using protection systems that degrade into a fail-safe mode.
 Series-connected protection systems; for example, two-out-of-two protection systems require both
relay systems to operate to initiate a trip. While using two-out-of-two increases security, it reduces
dependability. Failure of one of the two systems would result in no operation during a fault.
20
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
 Using an independent disturbance detector to supervise the protection system.
 Improved monitoring and self-checking.
 Emphasis on high-quality components.
 Two or more protection systems can be used to protect a line, and a voting scheme can be used to
achieve a balance between dependability and security; for example, a voting scheme that uses two-
out-of-three trip logic.
Another important design consideration is selectivity and coordination of the protection system. Selectivity
is the ability of a protection system to cooperate with other protection systems to reduce the outage area
when a faulted component of the system is isolated from the system. Coordination refers to the process of
applying relays to operate for faults in their primary zone of protection and within their backup zones,
which extend beyond the primary zone. Within backup zones, the relay operation may be delayed to
coordinate with operation of the relay systems protecting the components in the extended zones. Selectivity
and coordination should be achieved to ensure maximum service continuity and security.
Fault-clearing time is an important consideration in the selection of a system for protecting lines.
Requirements for the speed of a relay should be carefully determined. If the operating speed is too slow,
system instability, excessive equipment damage, and adverse effects on customers’ equipment may result.
However, a faster operating speed of the protection system may compromise the security, coordination, and
selectivity of the protection system. There is a limit to the speed with which a protection system can
correctly respond to the occurrence of a fault. The limit is due to the operating principle of the relay, and
due to the transients that are present in voltages and currents experienced during faults and applied to the
protection system via the CTs and VTs (see 6.11).
The sensitivity of a protection system that refers to the minimum operating quantities required for the system
to detect a fault is an important factor. Most solid-state or numerical relays are more sensitive than their
electromagnetic and electromechanical predecessors. But certain problems, such as detecting high-impedance
ground faults, inherent system voltage unbalances, and high source-to-line impedance ratios (SIRs; see 5.2),
still challenge the sensitivity of relays and should be considered when protection systems are selected.
The design of a line-protection system may fail to recognize one of the more important design factors:
simplicity. The multifunction and programmable capabilities of modern relays have created an abundance
of special solutions to possible system problems. The implementation of these solutions challenges
protection engineers, who are responsible for setting relays, and operations and maintenance personnel. The
problems caused by incorrect or incomplete implementation of overly complex protection systems may
create more serious consequences than not providing solutions for special situations. Protection engineers
should carefully weigh the consequences and probability of each problem to determine if they justify using
the complex special solutions that might be available or could be developed.
Protection engineers have long pointed out the relatively low cost and high importance of protection
systems compared with the equipment they protect. However, it is important to achieve the required
protection at a reasonable cost. In recent years, more importance has been placed on economic analysis that
considered more than just the lowest initial cost. The additional factors considered include installation and
maintenance costs as well as the cost of unreliable protection. In addition, modern protection systems
usually offer many features that were not previously available; those features may result in improvements
in operations, restoration of the system, and post-fault analysis. The value of these improvements should be
considered in a complete economic evaluation of the available alternatives.
Pilot relaying schemes are used to achieve high-speed tripping for faults at all locations on the line. These
schemes require that, during a fault, information be transmitted between the protection systems that are
located in different substations to determine if the fault is inside or outside of the line-protection zone. This
is accomplished by using several different methods, ranging from direct hardwire communications to fiber
optic communication systems (see 6.3). Different protection schemes and communication channels have
different degrees of dependability and security. Knowledge of the communication options is necessary to
21
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
determine the reliability of the protection schemes being considered. The network configuration and local
system-loading requirements may also affect the suitability of pilot protection schemes.
4.5.2 Factors influencing line relaying selection
4.5.2.1 General
A number of factors affect the selection of an adequate protection system for a given application. Some of
the factors are described in 4.5.2.2 through 4.5.2.8.
4.5.2.2 Impact of line faults on the power system
4.5.2.2.1 General
One of the significant factors in determining the system for protecting a transmission line is the impact a fault on
the line will have on the power system. How the fault is detected and cleared is important to the remaining
system, not so much to the faulted line, except that high-speed clearing of line faults will reduce the damage to
the line hardware and increases the likelihood of a successful reclose. The greater the impact a fault on the line
will have to the power system may justify redundancy in protection, communication, and perhaps even dc
auxiliary supply. A fault on a medium-voltage, long, radial transmission line will have minimum effect on the
remaining system, so it may be adequately protected with a step-distance or overcurrent system; whereas a high-
voltage, short, line that is part of a closely tied network may require a pilot or a current differential system.
The determination of the type of line protection is usually based on factors such as the operating voltage of
the line, the length of the line, the proximity of the line to generating stations, power flows, stability
studies, regional and federal regulations, and customer service considerations.
Several factors related to the requirements of the power system or to the requirements of the configuration
of the line should be weighed in the selection of transmission line protection. These include the factors
outlined in 4.5.2.2.2 through 4.5.2.2.6.
Faster clearing of line faults will reduce the damage to the insulators and support hardware caused by the
arcing of the fault. This reduction in damage could increase the success rate of the autoreclosing.
4.5.2.2.2 Fault-clearing time requirements
The time in which a protection system should clear a fault is determined by considering issues such as
system stability and the effects of the durations of voltage sags on customers’ operations. The clearing time
consideration not only influences the selection of primary relays, but may also dictate the application of
local backup protection and selection of the type of inter-substation communications needed for the
application.
4.5.2.2.3 Line length
Very short lines or very long lines may require protection solutions specifically designed for those lines (see 5.2).
4.5.2.2.4 Capacity of sources
Closely related to the line length consideration is the capacity of the sources connected to a transmission
line. The source-capacity determines fault current levels and affects the ability of protection systems to
provide adequate selectivity. If the capacities of the sources are subject to significant variations due to
changes in operating conditions, some protection systems require flexibility for modifying the protection
system, or to automatically adapt to accommodate the impact of changes in the power system.
22
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
4.5.2.2.5 Line configuration
The number of terminals, effects of tapped loads, and impacts of series capacitors and shunt reactors have
considerable influence on the selection of a protection system. This issue is discussed in detail in Clause 5.
4.5.2.2.6 Line loading
The voltage-to-current ratio (impedance), as seen from a line terminal, can be small if the line is heavily
loaded. This impedance could lie in the operating characteristic of a distance relay provided to protect the
line. Protection systems that include load-blinding features or that are naturally immune to flow of load
currents should be used in such cases.
4.5.2.3 Communications
Many transmission-line-protection systems depend on communication between the line terminals. The
choice of the communication system is influenced by many factors, including most of the factors that
influence the selection of the protective relays.
If the choice of communication is dictated by factors independent of the choice of the protection system,
then the communication system will influence the protection to be applied. If the protection is chosen based
on factors independent of the communication system, then the communication selected should be
compatible with the protection requirements.
It is important to understand the difference between the goals and means of such protection when the need
for a communication-based protection system is considered. For example, improved stability is a goal and
short-fault clearing time is a means of achieving that goal. Utilities target to reduce the fault-clearing time
on transmission lines for technical reasons, such as to improve generator angular stability or to reduce
equipment damage that might occur if the flow of fault currents continued for longer periods of time.
There are several reasons for the need of high-speed clearing of faults on an entire line. Generator angular
stability is just one of the issues that require consideration to justify the need for communication-based
transmission line protection. Some of the other reasons for the need of using communication systems in
transmission line protection include the following:
 Limiting fault current damage by reducing fault-clearing times
 Allowing high-speed autoreclosing
 Technically simplifying single-phase tripping and reclosing applications
 Providing protection for remote transformers that do not have interrupting devices
 Adequately protecting multi-terminal and high SIR (short) lines
 Protecting weak infeed terminals and instantaneously clearing low-current faults along the entire
transmission line
 Providing breaker failure protection and transfer trip for multiple breaker terminals
 Limiting voltage sag to prevent voltage stability issues and voltage sag to nearby customer loads,
thereby improving power quality
 Avoiding fault-induced voltage collapse
Each of these aspects should be studied when determining the need for a communication-based protection
system. These considerations may be added to other uses for communication paths [e.g., need for substation
SCADA (supervisory control and data acquisition)] that may provide sufficient justification to permit pilot
protection to be implemented.
23
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Once the need for a communication-based protection scheme has been established, some additional general
requirements that should be determined include the following:
 The number of communication systems required
 Type of communication system, such as analog or digital
 Medium for communication, such as copper wire, fibre optic, or power-line carrier
 Need for alternative communication paths if the normal communication path/paths fail
 How to operate the line if the communication becomes unavailable
 How breaker/relay maintenance affects the protection at each terminal
This type of thorough analysis of the technical justification and operational requirements for pilot
protection should be integrated with the economic implications of those requirements in a comprehensive
review of the transmission line protection. This practice should be followed for selecting protection systems
for new transmission lines and also when protection is replaced on existing lines (PSRC Report [B40]).
A thorough discussion of the commonly applied pilot protection schemes and the interrelationships of
protection and communications is included in 6.3.
4.5.2.4 Failure modes
Protective relaying design should consider and reduce the negative effects of “single-point failures.” A single-
point failure is any one failure of a relay, breaker, dc auxiliary supply, communication system, or any other
component of the overall protection system. Redundant protection, local backup-protection, remote backup-
protection, and duplication of other system components are used to reduce the effects of single-point failures.
“Common-mode failure” is another design consideration. Common-mode failures are failures of multiple
functions due to the failure of one component or due to the same root cause. Examples would be failures
due to mechanical jolts, such as bumping the panel or earthquake vibrations. Other common-mode failures
could be application errors, setting errors, incorrect maintenance or calibration procedures, or inadequate
shielding from electromagnetic induction. Independence in the operating principles of the primary and
backup protection systems is a technique that may be applied to reduce the chances of common-mode
failures. Physical isolation or separation, use of equipment from different manufacturers, varying
maintenance personnel from time to time, and independent checks of settings and designs are other
techniques for reducing the possibility of common-mode failures.
4.5.2.5 Protective scheme design compromises
The design of a protection system may require considerable compromise. Reliability is, by definition, a
combination of dependability and security. Increasing dependability usually reduces security; a tradeoff is,
therefore, necessary. Other compromises are reliability versus cost, speed versus security, simplicity versus
complex features, independence of design and manufacture versus standardization, and old technology versus
new technology. All of these, and many more choices, should be considered at the design stage. A prudent relay
design engineer would document these choices, particularly the compromises and the reasons behind them. This
documentation process provides the operations department with the information necessary to evaluate the
protection in less technically-complex terminology. It would provide continuity and consistency over time so that
subsequent generations of protection personnel can better understand the reasons for certain practices.
The very act of documenting the reasons for choices and compromises often reveals other alternatives or
options and generally results in a better final design.
24
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
4.5.2.6 Past practices
The selection of protection usually takes into consideration past practices and the familiarity of the personnel
responsible for those practices. The selection of different protective systems may result in requirements for
development of new documentation and for additional training for the staff. Protection solutions can only be
effective if designed properly, installed and commissioned correctly, and supported sufficiently by operations
and maintenance personnel.
4.5.2.7 Old versus new technologies
Similar to the discussion on past practices is the issue of whether to sustain application of the old “tried and
proven” technologies or take advantage of the many advanced protection features provided by new
technologies. Often, the benefits of the new technologies in areas such as reduced maintenance
requirements and additional operational information provide the incentives to make the change. Newer
relay technologies also provide lower CT and VT burdens, better sensitivities, wider setting ranges, easier
setting changes, greater flexibility, and the ability to solve special protection problems. Multifunctional
relays also reduce panel wiring and panel space.
4.5.2.8 The future
While it is not possible to anticipate all changes to the line or to the surrounding system within the foreseeable
future, it is often prudent to select protection that is capable of handling changes in line loading, source
conditions, or effective line length. Other changes to CT ratios, communications, substation configuration,
etc., can be handled if the protection is selected and designed to be flexible and easy to modify or replace.
4.6 Redundancy and backup considerations
Redundancy is the design of relaying developed with the goal of avoiding the possibility that a single
component failure will prevent the relaying from reliably sensing and isolating a fault in the protected zone.
Backup protection is a form of protection that operates independently of specified components in the primary
protective system. It may duplicate the primary protection or may be intended to operate only if the primary
protection fails or is temporarily out of service. Many transmission lines are protected by two protection
systems, for example, the line from bus B to bus D shown in Figure 7 is protected by a differential protection
system as well as by a permissive overreaching transfer trip (POTT) protection system. Both protection
systems operate independently and ensure that the line is disconnected from the rest of the power system in
the event a fault occurs in the line-protection zone. The two protection systems are functionally equivalent
and do not share any components; therefore, they are deemed to be redundant protection systems.
Bus B
Bus D
Transmission Line
Communication Link
87 87
21 21
Communication Link
Figure 7 —Main 1 and main 2 systems for protecting a transmission line
25
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
These redundant protection systems are often referred to as main 1 and main 2, system 1 and system 2, system A
and system B, or similar descriptions for these redundant protection systems. The advantage of using redundant
protection systems is that the failure of one component of a protection system does not result in losing the ability
to isolate the protected circuit if a fault occurs on that circuit. This improves the reliability of the power system.
Redundant CTs, VTs, breaker trip coils, power circuit breakers, dc sources, communication channels,
and/or other system components can be used to improve the reliability of the power system.
Backup protection is achieved by using different protection systems or functions. These systems function
simultaneously with the primary protection systems, but their operation is delayed long enough to allow the
primary protection systems to isolate the fault first. Backup systems perform the tripping function only if
the primary protection systems fail to isolate the faulted line.
Redundant and backup protection of ac transmission lines can be provided by different methods, each with
varying levels of complexity. The practices in various utilities include the following:
 Using identical relay systems
 Using relays from the same manufacturer but with different models or principles
 Using relays from different manufacturers but with the same principles
 Using relays from different manufacturers with different principles
There are various tradeoffs in complexity, cost, dependability, and security in all of those alternatives. The
history in each utility is sometimes the deciding factor. Sometimes, one of the objectives is to lessen the
possibility of similar hardware and software design problems affecting both protection systems.
Backup protection can be divided into two types: local backup and remote backup. Local backup protection
refers to the protection system located at the substations where line terminals are located. The term “remote
backup” refers to detecting faults using protection systems that are located at substations other than the
substations where the line terminals are located.
The basic form of local backup protection is the inclusion of redundancy in the protection scheme. Typically,
the higher the voltage level, the greater is the redundancy provided in the protection systems. The use of local
backup reduces delays and loss of selectivity that occurs with the operation of remote backup protection. The
tradeoff occurs in extra cost for the additional equipment required for local backup protection.
A part of a transmission system protected by multiple-zone distance relays is shown in Figure 8. All lines in
this transmission system are protected with step-distance protection systems that use separate relay
elements for each zone using the setting philosophy detailed in 6.2.4.2. Also, no breaker failure or other
protective relays are provided. A fault on line from bus B to bus D would be detected by the distance relays
provided on the line at those buses and would isolate the line by opening circuit breakers B3 and D3.
Zone 2 elements of those relays provide backup protection for the failure of the zone 1 elements and
provide time-delayed protection of the line section from the end of zone 1 to the end of the line. The zone 3
elements of those relays provide local backup protection for the failure of zone 2 elements to clear faults
beyond the reach of the zone 1 elements as well as provide backup protection for the zone 1 elements. This
is because separate protection elements are used in the distance relays in this example. Zone 2 and/or
zone 3 elements of distance relays provided at circuit breakers A1, C2, E1, E2, and F4 would also detect
the fault in the forward direction if they are within the reach of the relay. They would open circuit breakers
A1, C2, E1, E2, and F4 after the set time delay in case the primary or local backup protection of the faulted
line failed to isolate the line from the system before the expiration of the coordination time delays. This
illustrates a drawback of remote backup protection in that it results in a complete loss of supply to the
affected substations, because all lines into the station have to be tripped to remotely clear the fault.
The operation of the remote backup protection is delayed more than the operating time of the local backup
protection to ensure that parts of the power system other than the faulted line are not unnecessarily de-energized.
26
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Where remote protection is required to provide secondary or backup protection, it should be verified that the
sensitivity of the remote backup protection would detect all types of faults and for all credible system
configurations. The effects of infeed from other lines at the remote terminals should be taken into account to
ensure complete coverage of the protected line. In some cases, it may be acceptable for remote backup relays to
operate sequentially if the remote backup relays cannot provide complete coverage of the line. Also, remote
backup protection should not operate during high system loads and during low levels of system voltage.
Bus A
A1
21
21
B1
Bus B
B2 B3 B4
21 21 21
Bus C Bus F
C2 F4
F
21 21
21
D3
Bus D
D1 D2
21 21
21 21
E1 E2
Bus E
Figure 8 —Remote backup protection of a transmission line
It is important to appreciate that one relay can provide local and/or remote backup protection
simultaneously to different components of a system, including transmission lines. Also, a transmission line
can have a number of different backup protection relays. Some elements within a protection system may
back each other up as well as back up the protection in other transmission lines. However, since different
elements within a single system may share some common components (such as power supply), completely
independent backup cannot be achieved within a single system.
27
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Some protection functions operate only for faults on a transmission line. These functions, such as pilot
wire, current differential, and phase comparison protection do not offer remote backup protection and can
be used only as primary functions. Other protection functions, such as overcurrent protection and step-
distance with overreaching zones, can detect faults on the transmission line they are provided for and parts
of adjacent protection zones. These functions offer remote backup and can be used as primary or local
backup functions as well.
The operation of some protection functions requires transfer of information between protection systems
provided at all the terminals of a line. It is always desirable to provide backup protection functions that do
not need communications between the terminals for detecting the fault and isolating the faulted line.
4.7 Autoreclosing methods
Automatic reclosing is discussed in detail in IEEE Std C37.104™ [B61]. Some comments are provided in
this subclause for readers’ ready reference.
Protective relays are applied to isolate faulted elements and maintain the integrity of electrical transmission
systems. The loss of a single line in the transmission system can have a great impact on the economics and
reliability of the system. Many system faults, such as those caused by lightning, wind, or tree branches, are
temporary in nature and may disappear once the faulted circuit is de-energized. Autoreclosing of line
circuit breakers is widely used to reduce the impact of these temporary faults by re-energizing and restoring
the faulted section of the transmission system.
Two methods of autoreclosing are typically applied on transmission lines; these are high-speed
autoreclosing and time-delayed autoreclosing. High-speed autoreclosing is initiated with high-speed relays
and consists of automatic closing of a circuit breaker with no intentional delay beyond an allowance for arc
deionization. Some benefits of high-speed autoreclosing include fast restoration of power to customers,
improved system stability, and immediate restoration of system capacity and reliability. It should be noted
that high-speed tripping of all line terminals needs to be present in order to apply this method of
autoreclosing. A time-delayed reclosing is sometimes attempted if high-speed reclosing does not succeed.
Time-delayed autoreclosing is implemented with a definite circuit breaker open interval. A time-delayed
autoreclose can be used following an unsuccessful initial high-speed autoreclose or where multiple-shot
autoreclosing is desired. The initial autoreclose dead time for a time-delayed autoreclose cycle can be as
low as 0.5 s and as high as 60 s.
Single-shot autoreclosing is the automatic closure of a circuit breaker one time only. Multiple-shot
autoreclosing is the automatic closure of a circuit breaker more than one time in a predetermined
autoreclose sequence. Autoreclosing on extra-high-voltage (EHV) systems is typically of the single-shot
type. Multiple-shot reclosing, however, has gained acceptance on lower voltage transmission systems even
though the success rate for additional dead-line autoreclose attempts is poor.
Various forms of supervision may be applied to autoreclose schemes. Autoreclose supervision prevents
autoreclosing for conditions that might cause undesired affects, such as damage to generators or motors, or
re-energizing faulted equipment such as transformers and reactors. Selective and adaptive autoreclosing are
other methods utilized to prevent autoreclosing for specific types of faults or system conditions.
Autoreclosing has evolved due to the availability of greater amounts of information through SCADA and
modern relaying systems, such as neural network-based devices. This evolution allows for more selective
schemes that improve the reclosing success rates and lessen damage to system components that might have
been caused by closing into permanent faults. The type of autoreclosing used typically depends on the
voltage level, customer requirements, stability considerations, and the proximity of generation.
28
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
4.8 Effects of load on line relay applications and settings
4.8.1 General
One of the principal influences on protective relay settings is load; hence, maximum load current level, in
turn, influences fault-detection sensitivity.
4.8.2 Phase overcurrent relays
Phase overcurrent relays are generally set such that they do not operate when system load is being supplied, as
well as during transient operating conditions, such as transformer inrush, motor starting, emergency loads, and
recoverable power swings. This usually requires an overcurrent pickup setting above a maximum load level.
The sensitivity that can be achieved is, therefore, somewhat coarse, but many applications in which phase
overcurrent relays are used do not require high sensitivity (for details, see 6.2.2 and 6.2.3).
4.8.3 Ground overcurrent relays
Ground overcurrent relays have the advantage of using current that is either zero or very small under normal
conditions. The sensitivity that can be achieved is substantially better than that afforded by phase overcurrent
relays. Only unbalanced load currents and system unbalances affect the setting of these devices. Balanced
system load has no impact on the ground overcurrent relay applications on transmission lines.
4.8.4 Directional overcurrent relays
Directional overcurrent relays have the same restrictions as phase and ground overcurrent relays for load
flow in their tripping direction. Properly selected directional elements block tripping for load flow and
faults in the non-tripping direction. For further discussion on directional overcurrent relays, see 6.2.3.
4.8.5 Phase distance relays
Phase distance relays have a relatively fixed reach along the line impedance depending on the shape of their
operating characteristics and settings. These relays are applied to operate when fault currents flow on the
protected line and to not operate when only load currents flow on the protected line. Phase distance relays
may sometimes require a setting for adequate fault coverage that might limit the line loading capability. A
detailed discussion of this issue is given in 6.7.2.
4.8.6 Ground distance relays
Ground distance relays are applied on transmission lines using phase currents, residual current, and phase
voltages as inputs. In some cases, the residual current is not zero during normal operation of the line
because of various reasons, such as unbalance in the loads on the three phases. This makes these relays
susceptible to false operation under heavy load conditions if not supervised by directional elements.
Sometimes, ground distance relays are supervised by ground fault detectors that are set after considering
such things as CT mismatch or load unbalance.
Ground distance relays are also susceptible to errors associated with ground fault resistance in the presence
of load-flow-induced source angle differences. The relays may overreach or underreach for leading and
lagging phases when phase-to-ground faults occur if some provisions are not included in the relay design to
compensate for these factors. Giuliante, McConnell, and Turner [B31] describe these provisions. These
problems can be taken care of by using more conservative settings of the relay.
29
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
4.8.7 Pilot systems—Two terminal lines
The influence of load on pilot systems depends largely on the nature of the protective relaying scheme. The
systems that use overreaching distance measurement, such as directional comparison blocking (DCB),
POTT, and directional comparison unblocking (DCUB), have the advantage of limited load sensitivity.
These systems are least affected by load currents, typically because the overreaching element does not
come near loading values. However, the pilot trip elements may approach loading impedances in very long
line applications. In some cases, the relays include blinders, load encroachment, or shaped characteristics
that prevent operation of the pilot system during balanced three-phase load conditions. The DCB, POTT,
and DCUB schemes are further described in 6.3.5.6, 6.3.5.4, and 6.3.5.7, respectively.
The distance relays are set short of the remote line terminal for direct underreaching transfer trip (DUTT)
schemes. This setting makes the scheme less susceptible to tripping under heavy load conditions. However,
the reach variation of the distance relay as a result of pre-fault load current is much more critical than for
the overreaching schemes for situations in which fault resistance is not zero. It is desirable that load or fault
current, or any combination of the two, should never cause operation of the zone 1 elements for any
condition other than a fault on the protected line. The DUTT scheme is further described in 6.3.5.2.
Phase comparison and current differential schemes are not normally susceptible to operation for load
currents flowing on the line because these schemes use the summation of current from each terminal of the
line, which is very low during normal load flow. Load does influence the setting of fault detectors in phase
comparison blocking schemes and in current differential schemes when operation following channel failure
is allowed. The use of channel trip inhibit circuits in these schemes prevents them from false tripping even
when their current-based fault detectors have operated. But if the channel trip inhibit circuits are not
provided or if they fail, this would result in incorrect operation of the protection system during normal
operating conditions or during faults external to the protected circuit. Current differential schemes may be
sensitive to tapped loads, and settings should be chosen accordingly. Also, high levels of through-load
currents may reduce the fault detection sensitivity of both phase comparison and current differential
schemes. This can happen because the phase angles of currents may shift beyond the operating region,
resulting in restraining the protection system during internal faults (weak-infeed and -outfeed conditions).
Line charging current is substantial in EHV transmission lines (more than 1 MVA reactive per kilometer
for a 500 kV line) and high-voltage cables. Special considerations may be required for setting fault
detectors used to protect those systems.
4.8.8 Pilot systems—Three terminal
An outfeed condition may occur even without load during an internal fault on a three-terminal line.
Depending on the type of protection system, this may result in an undesired delay in clearing the fault.
Three-terminal applications occasionally have at least one weak source. Therefore, care should be taken to
ensure that either the contribution to an internal fault exceeds the load current outfeed (discussed in 6.6.2),
or the relaying system used to protect the line is based on the total internal fault current similar to a
differential protection system.
4.8.9 Sensitive ground overcurrent fault protection
Sensitive ground-fault protection is used to reduce hazards for the public and protect equipment. While
transmission faults with fault impedance are not as common as faults in distribution systems, the severity
and adverse consequences of a transmission-line fault that is not detected can be significantly higher due to
the high energy levels that are present. This topic is further covered in a 2014 PSRC report, “Transmission
line applications of directional ground overcurrent relays” [B51].
The type of system grounding and specific fault impedance determine the magnitude of ground faults.
Faults that contain high impedance pose a challenge to distance relays. Directional ground overcurrent
30
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
relays may be set sensitive enough to detect these faults, but they could adversely impact security. The
balance between sensitivity and security is based on individual and company preferences. Limits exist on
how sensitive a relay is allowed to be set and is truly part of the “art” of protective relaying. In addition,
microprocessor relays provide a means to detect higher impedance faults that electro-mechanical relays
cannot. This allows the protection engineer to use a more sensitive ground protection setting.
Methods of setting directional ground overcurrent relays vary among companies, locations, etc. One
method sets the pickup to a small portion of a minimum expected fault current. This method inherently
allows for different system conditions and contingencies as well as for faults with impedance. However, it
may not encompass the desired sensitivity. Another method may set the ground relay for a fault with a set
value of impedance. Regardless of the method, setting the ground relay sensitive enough to detect faults
that ground impedance elements do not detect is desirable.
Due to an increased focus on sensitivity, factors that were previously discounted and were accounted for in
general tolerances have now become more important, and consideration for such factors is required. These
factors include maximum ground current (due to system imbalance) during heavy loads, the system model,
mutual coupling, instrument transformer inaccuracies, single-phase tripping, and contingencies.
The system model should be as accurate as needed to support the sensitivity of relay settings. Transmission
lines need to be correctly modeled; the models should include factors, such as specific cable types, series
compensation, structure type, earth resistivity, etc. Mutual coupling should be accurately modeled with the
correct orientation between line segments and the correct mutual coupling effects. Under-built distribution
lines may also need to be considered. Data recorded from system faults may be used to validate and revise
the model if it becomes necessary.
The selection of the time delay curve is a matter of preference. However, the ground relay should coordinate
with the ground distance relays and other ground overcurrent relays. In order to improve the coordination
requirements of the ground distance protection functions, trip times for line-end ground faults should be larger
than zone 2 delay times with a margin. Coordination with other similar relays at remote terminals need only
be effective for fault current levels defined by the fault impedance expected in an application.
5. Impact of system configuration on selection of protection schemes
5.1 General
This clause addresses the impact of system configuration on the selection of protection schemes: line
length, line design, number of line terminals, lines terminated in transformers, weak electrical systems,
ground path configurations, distribution taps, power flow control devices, parallel lines, high-impedance
return paths, and terminal configurations.
5.2 Length considerations
5.2.1 General
This clause is concerned with the influence of line length on the selection of schemes for protecting
transmission lines. Transmission lines may be classified as short, medium, or long.
A line is designated short if the SIR for the line is large. Transmission lines that have SIRs greater than 4
are classified as short lines. The lines that have SIRs of 0.5 to 4 are classified as medium lines. Finally,
lines that have SIR of less than 0.5 are classified as long lines.
31
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
The per unit (pu) impedance of a line of given length varies much more with the nominal voltage of the line
than the impedance of the line in ohms, because the per unit impedance varies with the square of the
voltage. This factor, together with the different short-circuit impedances at different voltage levels, means
that the nominal voltage of a line has a significant effect on the SIR, which, in turn, influences whether the
line is considered “short,” “medium,” or “long.”
For example, consider a 500 kV line whose positive sequence reactance is 0.332 Ω per km (0.5343 Ω per
mi). This corresponds to a reactance of 0.000133 pu per km (0.000214 pu per mi) on 100 MVA and 500 kV
base values. If the source impedance behind a relay terminal is 0.01 pu (corresponding to a fault level of 10
000 MVA), the following classifications apply:
 Line lengths less than about 18.7 km (11.6 mi) would result in an SIR > 4 and may be classified as
short lines.
 Line lengths greater than about 150.4 km (93.5 mi) would result in an SIR < 0.5 and may be
classified as long lines.
On the other hand, a 69 kV line, whose positive sequence reactance is 0.53 Ω per km (0.853 Ω per mi),
might have very different length classifications. For such a line, the reactance is 0.01113 pu per km
(0.0179 pu per mi) on 100 MVA and 69 kV base values. If the source impedance behind a relay terminal is
0.1 pu (corresponding to a fault level of 1000 MVA), the following classifications apply:
 Line lengths less than about 2.2 km (1.39 mi) would result in an SIR > 4 and may be classified as
short lines.
 Line lengths greater than about 18.0 km (11.2 mi) would result in an SIR < 0.5 and may be
classified as long lines.
These examples demonstrate the importance of source impedance and nominal voltage on the classification
of a line as “short,” “medium,” or “long.” Further, a line can be considered short from one terminal and
medium or long from the other depending upon the relative strengths of the sources behind the terminals.
To further complicate matters, the positive and zero sequence source impedances can vary considerably
such that a line could be short for ground faults and medium or long for phase faults, or vice-versa.
Although the physical length of lines is a factor in the SIR, it is inappropriate to describe the line as long,
medium, or short based on this consideration only.
5.2.2 Effect of source-to-line impedance ratio on line protection
A short line is a challenge for line protection because it makes it difficult for the relay to differentiate
between an in-zone fault and an out-of-zone fault. For a distance element, the higher the SIR (shorter the
line), the lower the restraining voltage at the relay for an out-of-zone fault. A very low voltage can be more
susceptible to measurement errors and transients, which can result in undesired overreach of an
underreaching element. The SIR is a way of quantifying the voltage divider circuit. For an overcurrent
relay, when the SIR is high, the faulted system is dominated by the source impedance, and the difference
between the fault current magnitude for an in-zone fault and an out-of-zone fault can be smaller than the
typical margins used for setting the pickup. More details on short line protection issues are covered in 5.6.6
and 6.10. Thomas and Somani provide additional discussion on SIRs [B101].
5.2.3 Calculating source-to-line impedance ratio for determining line length
A suggested method to calculate the source impedance for the purpose of classifying line length is to place
a short circuit at the remote bus (boundary of the line zone) and calculate the source impedance as the
voltage drop from the source to the relay location divided by the fault current. For the purpose of
illustrating the calculation, Figure 9 shows a transmission system that has been reduced to its two-source
32
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
equivalent with the line and transfer impedance branches. The transfer impedance branch that represents
the complex transmission system network surrounding the line of interest can have a significant effect on
the voltage at the relay for a fault at the zone boundary.
Fault at the line
|     |     |     |     | Z   | zone boundary |     |
| --- | --- | --- | --- | --- | ------------- | --- |
TRANSFER
V
DROP_SOURCE
|     | V X |     |       |       | V Y |     |
| --- | --- | --- | ----- | ----- | --- | --- |
|     |     | ZS  |       | Z     | ZS  |     |
|     |     | X   |       | LINE  | Y   |     |
|     |     |     | V     | I     |     |     |
|     |     |     | RELAY | RELAY |     |     |
|     | S X |     |       |       | S Y |     |
(a) Simplified System
V
DROP_SOURCE
V  = V V  = V
| X   | BASE_LN |     |     |     | Y BASE_LN |     |
| --- | ------- | --- | --- | --- | --------- | --- |
V
RELAY
|     |     |     |     | V  = 0 |     |     |
| --- | --- | --- | --- | ------ | --- | --- |
FAULT
(b) Voltage Profile While Faulted

Figure 9 —Method to calculate source impedance for use in determining the SIR
for classifying line length
Equation (1) and Equation (2) provide the source impedances for the phase and ground fault loops,
respectively.
| V   | V                  | −V      |       |     |     |      |
| --- | ------------------ | ------- | ----- | --- | --- | ---- |
| =   | DROP_SRC = BASE_LN | RELAY   |       |     |     |      |
| ZS  |                    |         |       |     |     | (1)  |
| 3PH | I                  | I       |       |     |     |      |
|     | RELAY              | RELAY   |       |     |     |      |
| V   |                    | V −V    |       |     |     |      |
| =   | DROP_SRC =         | BASE_LN | RELAY |     |     |      |
| ZS  |                    |         |       |     |     | (2)  |
| SLG | I I                | +(3I0   | ×k0)  |     |     |      |
|     | RELAY RELAY        |         | RELAY |     |     |      |
where
V    is the system base voltage, line to neutral, that defines voltage at the infinite bus behind the
BASE_LN
source impedance in primary units
| V    | is the phase-to-ground voltage at the relay for a fault at the remote bus   |     |     |     |     |     |
| ---- | --------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
RELAY
I        is the phase current at the relay for a fault at the remote bus
RELAY
| 3I0 |   is the zero sequence current at the relay for a fault at the remote bus  |     |     |     |     |     |
| --- | -------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
RELAY
k0      is the zero sequence compensation factor for the line as defined by Equation (3)
Z0 −Z1
| k0= L | L   |     |     |     |     | (3)  |
| ----- | --- | --- | --- | --- | --- | ---- |
3×Z1
L
where
Z1    is the positive sequence line impedance
L
Z0    is the zero sequence line impedance
L
33
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
The source impedances obtained by Equation (1) and Equation (2) are used in Equation (4) to obtain the
SIR. Z1  is used in the denominator of the equation to determine the SIR as that defines the zone
LINE
boundary that should not be overreached. The positive sequence impedance (Z1) is used for both three-
phase and single-line to ground fault because k0 is used to define ZS .
SLG
|       | ZS            | ZS      |      |
| ----- | ------------- | ------- | ---- |
| SIR = | 3PH   or  SIR | = SLG   | (4)  |
| 3PH   |               | SLG     |      |
|       | Z1            | Z1      |      |
|       | LINE          | LINE    |      |
It is often desirable to determine the SIR under N−1 conditions as well to determine if the line can get short
when the strongest source behind the local terminal is out of service.
5.2.4 Example source-to-line impedance ratio calculation
For this example, we have a line between bus W and bus E with the parameters listed in Table 1. The fault
values for terminal W are provided in Table 2. The fault values are obtained by placing a three-phase fault
at bus E under system normal (N−0) and with the strongest source behind the W terminal out (N−1). In this
case, bus W has one strong source and one weak source connected to the bus behind the relay.
Table 1 —Line parameters
Parameter  Value
Voltage  138 kV
Line length  41.53 mi
Z1  primary  34.29 Ω
LINE

Table 2 —Fault values for determining SIR for terminal W
Parameter  Value
|     | V RELAY |  for 3PH fault at remote bus E under N−0  43.5 kV  |     |
| --- | ------- | -------------------------------------------------- | --- |
|     | I RELAY |  for 3PH fault at remote bus E under N−0  1247 A   |     |
|     | V       |  for 3PH fault at remote bus E under N−1  16.3 kV  |     |
RELAY
|     | I   |  for 3PH fault at remote bus E under N−1  484 A  |     |
| --- | --- | ------------------------------------------------ | --- |
RELAY

The SIR for the system normal (N−0) case for phase protection is calculated as shown in Equation (5) and
Equation (6):
138 kV
−43.5 kV
3
| ZS  | =   | =28.39 Ω  | (5)  |
| --- | --- | --------- | ---- |
3PH_N−0
1247 A
28.39 Ω
= =0.8
| SIR     |         |     | (6)  |
| ------- | ------- | --- | ---- |
| 3PH_N−0 | 34.29 Ω |     |      |
An SIR of 0.8 is greater than 0.5, which indicates that this line should be considered a medium length or
borderline long line under N−0 conditions.
The SIR for the single contingency (N−1) case for phase protection is calculated as shown in Equation (7)
and Equation (8):
138 kV
−16.3 kV
3
| ZS      | =     | =130.94 Ω  | (7)  |
| ------- | ----- | ---------- | ---- |
| 3PH_N−1 | 484 A |            |      |
34
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
130.94 Ω
SIR = =3.8 (8)
3PH_N−1
34.29 Ω
An SIR of 3.8 is less than 4, which indicates that this line should be considered a medium length or
borderline short line under N−1 conditions.
Examining this line from terminal E provides the fault values in Table 3. Terminal E is connected to a
relatively strong bus with many lines into it.
Table 3 —Fault values for determining SIR for terminal E
Parameter Value
V for 3PH fault at remote bus W under N−0 64.9 kV
RELAY
I for 3PH fault at remote bus W under N−0 1898 A
RELAY
V for 3PH fault at remote bus W under N−1 62.0 kV
RELAY
I for 3PH fault at remote bus W under N−1 1813 A
RELAY
The SIR for the system normal (N−0) case for phase protection is calculated as shown in Equation (9) and
Equation (10):
138 kV
−64.9 kV
3
ZS = =7.78 Ω (9)
3PH_N−0
1898 A
7.78 Ω
SIR = =0.2 (10)
3PH_N−0
34.29 Ω
An SIR of 0.2 is less than 0.5, which indicates that this line should be considered long under N−0
conditions.
The SIR for the single contingency (N−1) case for phase protection is calculated as shown in Equation (11)
and Equation (12):
138 kV
−62.0 kV
3
ZS = =9.75 Ω (11)
3PH_N−1
1813 A
9.75 Ω
SIR = =0.3 (12)
3PH_N−1
34.29 Ω
An SIR of 0.3 is still less than 0.5, which indicates that under N−1 conditions, the line is still long.
The process would be similar for calculating the SIR for ground protection.
5.3 Line design considerations
5.3.1 General
Transmission lines are either overhead air-insulated lines or insulated cable systems and, in some cases, are
combinations of air-insulated lines and insulated cables. The electrical characteristics are significantly
different for these lines. The characteristics of overhead air-insulated lines are well understood. Key
35
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
characteristics of cables are reviewed in this clause. The issues associated with electrically connected
double circuit lines are also reviewed in this clause.
5.3.2 High-voltage cables
The series inductance of cable circuits is typically one-half to one-third of the series inductance of comparable
overhead lines. The reactance to a fault will, accordingly, be lower for cable systems. This should be
considered in the application of distance relays for protecting short lines. As a practical consideration, cable
systems are frequently used in urban or metropolitan areas where short lines are typical. Therefore, cables are
frequently protected using those techniques that are suitable for protecting short lines and lines that have low
total impedance, as discussed in a 1997 PSRC report, “Protective relaying considerations for transmission
lines with high voltage ac cables” [B45], and by Tziouvaras [B103].
5.3.3 Electrically connected double circuit transmission lines (bifurcated lines)
Phase conductors of parallel transmission lines are sometimes connected together to form a single
transmission line. Such a line is modeled either by assuming that each phase is composed of two
conductors of a single bundle or, more accurately, by assuming that the two lines are two circuits connected
in parallel. The calculations of line impedance are simplified if it is assumed that the lines are fully
transposed even though they most likely are not. Since the lines configured in this manner are generally not
very long, it may be reasonable to neglect the effect of the lines not being transposed.
Fault currents and apparent impedances, as seen by relays, are affected by a fault on one phase of one of the
transmission line circuits. The current on the unfaulted conductor will flow past the fault location to the next
jumper before crossing over; this results in an increase in the apparent impedance causing the impedance
relays to underreach. The worst case occurs where the lines are connected only at their terminals. This
problem can be reduced by adding jumpers at intermediate locations along the line length. An adequate
number of jumpers will negate the effect, because all single-conductor faults will then be near a jumper.
The effects can be studied if the jumpers near a point of interest (such as a fault near the far end) are
modeled as bus points and the conductors in between are treated as mutually coupled parallel lines.
Tziouvaras, Altuve, and Calero [B104] discuss these topics, as well as other topics such as the requirements to
cover a fault where the line shorts to the ground with the side closest to the jumper not faulted.
5.4 Number of line terminals
The number of terminals on a transmission line is a basic and important factor when selecting a protection
system. A particular terminal becomes significant to the selection of the protection system if it supplies
current to faults on the transmission line. All terminals that supply fault current need to be considered for
inclusion into the line-protection system.
5.5 Lines terminated into transformers
5.5.1 General
A typical line terminated into a transformer is shown in Figure 10. There are generally two approaches used
to protect this line and transformer combination: line current differential schemes described in 6.3.2 and
distance relay schemes described in 6.2.4.2. In either case, the implementation of separate transformer
differential protection is needed for the transformer, as described in IEEE Std C37.91™ [B56].
36
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
This subclause describes examples and protection issues of transmission lines terminated in transformers and
protected with instantaneous, underreaching step distance relays (generally zone 1). Additional line differential or
piloted distance schemes might be required for a complete protection of the system. The numerical values used
for setting relays depend on the practices of utilities and are not intended for use in all applications.
Bus A Z
T
kV L kV H Bus B
NCL NCH
Z
L
IL
NVL NVH
IH
VL VH
Relay A Relay B
Figure 10 —Typical transformer-line combination
Zimmerman and Roth [B108] discuss lines terminated into transformers.
Some issues, such as transformer magnetizing inrush, overexcitation, etc., are not discussed in this clause.
IEEE Std C37.91 [B56] discusses additional protection functions that are needed in such cases.
5.5.2 Considerations for line distance applications
The reach of a distance relay is measured from the location of the VTs; the fault direction is sensed by the
location and connections of the CTs. In Figure 10, using the VTs and CTs on the line side of the
transformer, V and I , are preferred. In all respects, except for the transfer trip requirement, these
H H
applications can be treated as normal line protection applications.
However, economic or other factors may dictate the use of the VTs and CTs measuring the low side (bus A
side) quantities V and I . These factors introduce additional application considerations, which are
L L
primarily the effects of the transformer impedance, phase shift introduced by wye-delta transformation, tap
changers, secondary impedance calculations, and the availability of ground fault (zero sequence) current.
Therefore, careful consideration should be given to the placement of VTs and CTs for these line distance
applications. This guide does not provide the mathematical equations needed to compensate for the phase
shift in line currents introduced by different power transformers. Microprocessor relays are available that
are programmed to cope with this shift.
The key criterion to set any type of instantaneous, step distance relay (non-piloted, zone 1) is not to
overreach the remote terminal. This is done to avoid tripping for external faults behind the remote bus. The
underreaching margin to apply to distance relays depends of several factors, such as utility practices, errors
in the calculation of line parameters, variation of the line ground impedance throughout the year, relay
accuracy, and CT/VT errors, among others. In the case of lines terminated in transformers, depending on
where the CT/VTs are located, one of the relays may need to measure the combination of the transformer
and line impedance. In these cases, the errors of the transformer impedance should be considered while
setting the relay, even though transformer impedance errors are much smaller than errors of the line
impedance. Guidance for underreaching factors is given in Clause 6.
The following subclauses, 5.5.3 to 5.5.6, provide a discussion of the application considerations for the
selected instrument transformer connections.
37
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
5.5.3 Preferred protection scheme—Use of V and I
H H
The preferred method to protect lines terminated in transformers is to utilize, if available, the CTs and VTs
located on the line (high-voltage) side. This scheme is shown in Figure 11.
87T
Bus A Z
T
kV kV Bus B
L H
N
CH Z
L
N
CL
N I N
VL H VH
V
V H
L
Relay A Relay B
Figure 11 —Preferred protection scheme for a line terminated into a transformer
This protection scheme separates the line and transformer into two separate measuring protection zones
supervised by separate relays. Both the transformer differential relay and line protection relay are high-
speed devices. Relay A and relay B are intended to detect faults on the transmission line and trip the line
circuit breakers at bus A and bus B. The transformer differential relay, 87T, is intended to detect faults in
the transformer protection zone. An 87T trip initiates the tripping of the line circuit breaker at bus A and
initiates a direct transfer trip via a communication channel to the line circuit breaker at bus B.
Line and transformer faults are easily discriminated with this approach. This approach also allows automatic
or manual reclosing for trips that result from line faults only. Because it is not desirable to reclose (energize) a
faulted transformer, 87T operations should block reclosing at both line terminals. Likewise, it is advisable to
autoreclose the remote end first to avoid subjecting the transformer to additional high current.
An alternate method to execute the transfer trip is to have the 87T operate a grounding switch located at the
transformer end and within the line’s protection zone. This is done to place a solid fault on the line, causing
an operation of the line protection and tripping the circuit breakers at both line ends. Drawbacks to this
approach are that it applies an additional fault on the system and also delays the clearing of the transformer
for the time it takes the grounding switch to close.
The method shown in Figure 11 allows the selection and application of the line-protection scheme
independent of the transformer protection scheme. If V and I are to be used for distance relay A, its
H H
setting is not supposed to overreach the remote terminal. Distance relay B can be used to partially protect
the transformer (back-up protection); its setting should include the totality of the line plus a good part of the
transformer impedance, without overreaching bus A.
5.5.4 Using V and I
H L
Another option for protecting a line terminated in a transformer is to use, for relay A, the voltage of the
high-voltage side of the transformer, V , and current from the low-voltage side of the transformer, I , as
H L
shown in Figure 12.
38
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
87T
Bus A Z
T Bus B
kV kV
L H
N
CL Z
L
N N
CL CH
N I N
VL L VH
V
V H
L
Relay A
Relay B
Figure 12 —Relay connected to use V and I
H L
Wye-delta connected transformers introduce a 30° phase shift between V and V that needs to be taken
L H
into consideration. The high-side voltages and currents lead the low-side voltages and currents by 30° for
ANSI connected transformers; therefore, 30° should be added to the measured angle of the line current I .
L
This may be accomplished by connecting the low-side CTs in delta. This correction is done in the software
of some microprocessor relays.
The impedance reach is measured from the high- or line-side VTs providing V , and the distance relay
H
zone 1 setting should not reach bus B. As shown in Equation (13), the low- or bus-side CT ratio and the
power transformer ratio should be taken into account for determining the impedance relay setting.
kV
N L
CL kV
Z = H Z (13)
SEC N PRI
VH
where
kV is the voltage on the high-voltage side of the transformer
H
kV is the voltage on the low-voltage side of the transformer
L
N is the turns ratio of the CTs on the low-voltage side of the transformer
CL
N is the turns ratio of the VTs on the high-voltage side of the transformer
VH
Z is the impedance seen from the high-voltage side of the transformer
PRI
Z is the impedance seen by the relay
SEC
For wye-delta transformer windings, zero-sequence current in the transmission line cannot be measured for
line-side faults when low-side current, I , is used for protection. Therefore, ground distance units using
L
zero-sequence compensation should not be used. Also, zero-sequence directional relays and zero-sequence
(ground) overcurrent relays cannot be relied upon.
Negative-sequence current flowing through the transformer is not blocked by the wye-delta transformation
as zero-sequence current is. However, the negative-sequence current, I , lags I by 30° for the ANSI
H2 L2
standard transformer connection. If the CTs are connected delta on the low side to provide the +30° phase
shift in phase currents, then the −30° phase shift in negative sequence current is accounted for. Negative
sequence directional and overcurrent units will accurately perform. For using compensation factors in a
microprocessor relay, the relay’s manufacturer may be consulted for correct implementation to assure
proper operation of negative-sequence elements.
If the transformer has a tap changer, its effect on the power transformation ratio may be included in
Equation (13). There are no further considerations if the transformer windings are wye-wye connected and there
39
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
is no delta winding. When the transformer is wye-wye connected or is an autotransformer with delta-tertiary
winding, the ground distance elements would underreach during single-phase- or two-phase-to-ground faults.
5.5.5 Using V and I
L L
The third option for protecting a line terminated in a transformer is to use the voltage of the low-voltage
side of the transformer, V , and current from the low-voltage side of the transformer, I , as shown in Figure
L L
13. This is generally the more practical connection when both line-side VTs and CTs are not available. The
impedance reach is measured from the bus side VT providing V , and the impedance setting should include
L
the entire transformer impedance Z . Transformer impedances should be calculated very accurately using
T
transformer test reports or should be obtained from the transformer manufacturer. The zone 1 reach should
be set at less than Z plus line impedance Z , so as not to overreach bus B.
T L
Bus A Z Bus B
kV T kV
L H
N
C
Z
L L
I
N VL L N VL
V
L
V
L
Relay A Relay B
Figure 13 —Relay connected to use V and I
L L
This connection method has a disadvantage of limiting the reach of line protection when Z is large
T
compared to Z . For example, set the zone 1 reach of relay A to 0.99 Z + 0.9 Z (pu). The multiplier 0.99
L T L
is used to allow for 1% positive error in the Z measurement (actual impedance is Z /0.99, but Z is
T T T
measured). If the measured Z had no error, the effective line reach from the transformer high side will be
T
0.9Z − 0.01Z . For a Z /Z ratio of 10, the effective line reach will be 0.8Z . If the error in the measured
L T T L L
Z is subtractive (actual impedance is 0.99Z ), the effective reach will be even less. As discussed in 5.5.4,
T T
the transformer taps should also be taken into account. However, the effect of the tap changer for this case
is even more pronounced because it not only changes the value of Z as seen from the low side but also
L
changes the value of Z (actual impedance is Z /0.99, but Z is measured).
T T T
Consideration should be given to transformer inrush currents that would include real-time simulation tests,
verification of relay settings, and countermeasures that cope with the phenomenon.
There are no further considerations if the transformer windings are wye-wye connected and there are no
limitations on phase or ground protection. However, for wye-delta transformer connections, the limitations
on ground protection with zero sequence quantities apply as discussed in 5.5.4. There is also no
requirement for phase shift correction with three-phase distance relays that compute phase distance using
line current and phase-to-phase voltages.
If the transformer is wye-wye with a delta tertiary winding, a part of the zero-sequence current in the event
of ground faults on the line will flow in the tertiary winding, and current seen by relay A will be less than
the zero-sequence current in the line. The relay would underreach if the zero-sequence current in the delta
winding is not measured and used by the relay.
40
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Issues are similar at relay B, with reaching through the transformer impedance to cover all of the zone. This
can be a significant issue depending on the type of relays applied. Zimmerman and Roth [B108] provide
further discussion on this topic.
5.5.6 Using V and I
L H
The fourth option for protecting a line terminated in a transformer is to use the voltage of the low-voltage
side of the transformer, V , and current from the high-voltage side of the transformer, I , as shown in
L H
Figure 14.
87T
Bus A Z
kV L T kV H Bus B
NCH Z
L
NCL NCH
NVL NVL IH
VL
VL
Relay A
Relay B
Figure 14 —Relay connected to use V and I
L H
Using these connections, the impedance reach is measured from the low or bus side VT that provides V ,
L
and the impedance setting should include the transformer impedance, Z , plus line impedance Z . Zone 1
T L
should not reach bus B.
The disadvantages of having the transformer impedance in the zone 1 setting discussed in 5.5.4 apply in
this case as well. Also, the high- or line-side CT ratio should include the power transformer ratio to
compute the correct secondary impedance on the low side base. Equation (14) can be used for this purpose.
kV
N H
CH kV
Z = L Z (14)
SEC N PRI
VL
where
kV is the voltage on the high-voltage side of the transformer
H
kV is the voltage on the low-voltage side of the transformer
L
N is the turns ratio of the CTs on the high-voltage side of the transformer
CH
N is the turns ratio of the VTs on the low-voltage side of the transformer
VL
Z is the impedance seen from the low-voltage side of the transformer
PRI
Z is the impedance seen by the relay
SEC
If the transformer has a tap changer, its effect on the power transformer ratio should be included as
discussed in 5.5.4.
Fault direction is determined from the CT location; therefore, faults in the transformer cannot be detected.
For wye-delta transformer connections, there is a 30° phase shift between I and I that should be
H L
corrected. Since primary ohms are computed on the low-side base voltage V , I should be shifted by −30º
L H
41
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
if an ANSI standard connected transformer is used. The correction may be done by connecting the high-
side CTs in delta for subtracting 30° from the angle of the high-side phase currents. This correction is done
with compensation factors in some microprocessor relays.
The zero-sequence voltage at the line terminal cannot be measured for line faults if the transformer is wye-
delta connected. Therefore, ground distance units and zero-sequence directional units that require zero
sequence voltage polarization should not be applied. Transformer neutral current or zero-sequence current
(derived from phase currents) can be used to identify a ground fault on the line or beyond bus B if the bus-
side transformer winding is delta connected and the line-side winding is wye connected, with neutral
connected to ground and the CTs are wye connected.
Negative-sequence voltage appears on both sides of a wye-delta transformer; however, V  lags V  by 30°
H2 L2
for the ANSI standard transformer connection. If the phase angle correction for phase currents with high-side
delta-connected CTs is applied as discussed above, then the negative sequence phase angle is accounted for.
The correction may also be done with compensation factors available in microprocessor relays.
5.5.7 Application summary at transformer end
A summary of the application considerations for the available CT and VT connections discussed in 5.5.3
through 5.5.6 is given in Table 4.
Table 4 —Application considerations for CT and VT connections for distance relays
| Connections  |       | Z  =R × Z |     |     |                             | Comments  |     |
| ------------ | ----- | --------- | --- | --- | --------------------------- | --------- | --- |
|              |       | SEC       | PRI |     |                             |           |     |
| V   I        | R = N |  / N      |     |     |                             |           |     |
| H H          | CH    | VH        |     |    | Preferred connection        |           |     |
|              |       |           |     |    | Distance is measured from V |           | H   |
  Will detect only line faults
| V   I   | R = N                    |  × R  / N   |     |     |                             |     |                       |
| ------- | ------------------------ | ----------- | --- | --- | --------------------------- | --- | --------------------- |
| H L     | CL                       | T VH        |     |    | Set Z 1  with minimum R     |     | T  – transformer tap  |
|         | R  = kV                  |  / kV ;     |     |     |                             |     |                       |
|         | T                        | L H         |     |    | Set Z  with maximum R       |     |  – transformer tap    |
|         | varies with tap changer  |             |     |     | 2                           |     | T                     |
|         |                          |             |     |    | Distance is measured from V |     |                       |
H

Will detect transformer and line faults
  Delta-wye winding phase angle corrections
  No zero-sequence relaying
V L   I H   R = N CH  × R T  / N VL     Set Z  with minimum R  – transformer tap
|     |                          |              |     |     | 1                           |     | T                   |
| --- | ------------------------ | ------------ | --- | --- | --------------------------- | --- | ------------------- |
|     | R T  = kV                | H  / kV L ;  |     |     |                             |     |                     |
|     |                          |              |     |    | Set Z  with maximum R       |     |  – transformer tap  |
|     | varies with tap changer  |              |     |     | 2                           |     | T                   |
|     |                          |              |     |    | Distance is measured from V |     |                     |
L
  Will detect only line faults

Delta-wye winding phase angle corrections
  No zero-sequence relaying
|         |       |            |     |    | Accuracy issues when Z  |     |  >> Z                 |
| ------- | ----- | ---------- | --- | --- | ----------------------- | --- | --------------------- |
|         |       |            |     |     |                         |     | T L                   |
| V   I   | R = N |  × T / N   |     |    |                         |     |                       |
| L L     | CL    | VH         |     |     | Set Z 1  with minimum R |     | T  – transformer tap  |
T = 0.95 to 1.05 (assumed);
|     |                          |     |     |    | Set Z  with maximum R       |     |  – transformer tap  |
| --- | ------------------------ | --- | --- | --- | --------------------------- | --- | ------------------- |
|     | varies with tap changer  |     |     |     | 2                           |     | T                   |
|     |                          |     |     |    | Distance is measured from V |     | L                   |
  Will detect transformer and line faults
  Delta-wye winding phase angle corrections

No zero-sequence relaying
|     |     |     |     |    | Accuracy issues when Z |     |  >> Z   |
| --- | --- | --- | --- | --- | ---------------------- | --- | ------- |
|     |     |     |     |     |                        |     | T L     |
42
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
5.5.8 Considerations for current differential applications
When protecting the line with differential protection, there are no issues if the current I is used by the
H
relay because the transformer is not in the line’s differential zone. When I is used, the transformer is in the
L
current differential zone, which needs to be accounted for primarily due to the wye-delta connections, a
delta tertiary in a wye-wye and autotransformer, and the tap changer.
In general, the effect of tap changers is easily accounted for in the differential operating current (sensitivity)
setting. Also, many current-only systems (differential, phase comparison, etc.) are immune to the effects of tap
changing. However, investigation of the possible effects to assure the proper application would be prudent.
Current differential relays can be applied normally to a two-winding, wye-wye connected transformer. A
phase shift correction and a zero-sequence current filter are required if the transformer is wye-delta
connected. This is generally achieved by connecting the CTs on the transformer’s wye-grounded side in
delta. Some relays provide settings to accommodate the phase shift and zero-sequence current filtering. For
some relays, adequate negative-sequence current should be available for detecting single phase-to-ground
faults on the line to assure correct operation.
Also, consideration of the need to restrain the differential element for inrush and overexcitation is desirable.
Line differential relays often send only phasor data and, therefore, cannot use typical harmonic methods.
Kasztenny and Perera [B74] provide a discussion of these topics.
5.6 Weak electrical systems
5.6.1 General
A power system may be considered weak when the source impedance is high compared to the line
impedance. Weak systems often have the following characteristics:
 The magnitudes of fault currents contributed by the system are relatively low.
 At the relay location, fault currents on the protected line are generally lower than the load currents.
 Voltage changes are large with load changes and under fault situations.
 The magnitudes of the available polarizing currents are relatively low.
Weak electrical systems may be found at any voltage level but are more prevalent at lower transmission
voltages. Long-line transmission systems with remote generation may also have the characteristics that
weak systems demonstrate. When small or single unit generators are installed and are connected to a power
system, weak system characteristics may be created because these units are small or because they are
occasionally off line. These situations are particularly challenging to the application of effective protection.
All weak systems present several challenges to the protection engineer. Some of these are addressed in the
following subclauses.
5.6.2 Contingency outage considerations
Different system configurations that occur as a result of system outages cause changes in source
impedances, network configurations, and load levels, resulting in changes in the levels of fault currents. For
example, backup sources may be connected to a system on a contingency basis, which will change
protection considerations. If additional protective equipment is needed to handle a contingency, proper
coordination between the schemes should be considered. Additional relays, modified relay settings, or
compromised protection/coordination (in some circumstances) may be required.
43
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
5.6.3 Sequential tripping
It is possible that all terminals of a line are connected to weak systems. Protection systems provided at all
terminals are not likely to see the fault on the line at its inception. For example, consider the system shown
in Figure 15 that experiences a fault at F. The current initially supplied through breaker 2 is significantly
less than the current through breaker 1. Therefore, the relays at breaker 2 may not be able to sense the fault
at its onset. The current through breaker 2 increases by a factor of more than 10 after breaker 1 opens.
Thus, the relays are now able to sense the fault and open breaker 2. Another case of sequential tripping
would be the amplification of fault impedance seen by distance relay at CB 1 due to high remote-end fault
current infeed. The impedance measured by the relay may fall into the restraining region of the relay
characteristic, as long as the remote-end infeed lasts; however, when the remote-end CB 2 trips, the fault
current infeed ceases and the local relay is able to operate and trip the local circuit breaker.
Bus A Bus B
0.05
F
1.0 0.10
CB 1 CB 3
Z = 1.0 0.05 Z = 9.75
S1 S2
E 1 Z = Z = 0.5 E 2
CB 2 L1 L2 CB 4
Bus A Bus B
0.555
F
0.481 0.074
CB 1 CB 3
Z = 1.0 0.481 Z = 9.75
S1 S2
E 1 Z = Z = 0.5 E 2
CB 2 L1 L2 CB 4
Note that all currents and impedances are given in pu values
Figure 15 —Example of sequential tripping
5.6.4 Fault detection
There may be insufficient current contribution to a fault on the protected line for a relay to reliably detect a
fault if the line is connected to a weak source. Special logic in pilot systems may be required in such cases.
This logic, known as weak infeed echo and weak infeed trip, is described in 6.3.6.
5.6.5 Weak source becoming a strong source
Varying system configurations may cause a source to become a weak or a strong source depending on the
generation connected at a bus. For example, a generator may be added at a location on the power system for
peaking only. When the peaking unit is in operation, the source may become a strong source, but when the
peaking unit is not in operation, the source becomes a weak source.
5.6.6 Coordinating relays on short lines (SIR > 4)
Consider the system shown in Figure 16, in which the source impedance, Z is much larger than the
S1
impedances of line segments, Z , Z , and Z . The currents for faults on one end of a line would be nearly
L1 L2 L3
of the same magnitude as the currents for faults on the other end of the line in this weak system. The only
44
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
possible differentiating feature that can be used for determining the faulted section is time if non-pilot
protection systems are to be used. The pickup settings at B1, B2, and B3 may be approximately the same.
In order to coordinate the tripping of the lines, time delay may be used to allow the relays at B3 to trip
before the relays at B2, and the relays at B2 to trip before the relays at B1.
Bus B1 Bus B2 Bus B3
1 2 3 4 5
Z S1 Z L1 Z L2 Z L3
E
1
Figure 16 —Example of a weak system
5.6.7 Multi-terminal lines
A multi-terminal line may have a weak source at one terminal compared to the sources at other terminals.
The protection system, provided at the terminal that is connected to the weak source, will not detect faults
beyond the tap as adequately as the protection systems provided at the other terminals that are connected to
strong sources. Thus, the terminals connected to the strong sources may have to be disconnected before the
protection system provided at the line terminal connected to the weak source can detect the fault. This will
result in sequential tripping and, therefore, slower fault clearing than would otherwise occur. The worst
case would be a combination of source impedances and line lengths that would require sequential time
delay clearing of two of the terminals for phase and/or ground faults. Protecting a multi-terminal line with
more than three terminals with distance protection relays could be complicated.
5.7 Ground path configurations
5.7.1 General
Positive-sequence voltage sources (generators) provide positive-sequence currents for all system faults,
whereas the unbalanced nature of a fault is the cause of negative- and zero-sequence voltages and currents.
The zero-sequence currents flow from the fault to the positive-sequence source through the zero-sequence
impedance between the fault and the source when a fault involving ground occurs. The zero-sequence
impedance is made up of one or more parallel impedances that provide a path for ground current to flow from
the fault back to the source. These impedances are often referred to as ground sources that are shunt paths (as
seen in the zero-sequence equivalent circuit) for ground current to flow. This is illustrated in Figure 17 for a
simple system with a single phase-to-ground fault in Blackburn’s Protective Relaying [B12].
Figure 17 shows two ground paths on the transmission system where grounding is provided by transformers
with both wye-grounded and delta windings. Although grounding is not the primary purpose of the power
transformers, they may be referred to as sources of zero-sequence current. Other grounding transformers,
such as a zigzag transformer, may also be applied for the specific purpose of providing a path for zero-
sequence current, which increases the level of available ground fault currents.
Figure 18(a) illustrates that because I current can circulate in the delta winding, zero-sequence current I
0 0
flows in each of the wye windings, thus permitting a ground path for the 3I current. Figure 18(b) shows a
0
transformer whose primary as well as secondary windings are wye-grounded connected. The neutrals of
both transformers are connected to the station ground mat, and the ground fault current flows through the
transformer windings via both the neutrals, as described in Blackburn’s Protective Relaying [B12].
45
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Transmission Network
Substation
1f − G
Generator
Step Up Transformer Auto-transformer
Z Z Z
G1 T PS
Positive Sequence Network
Z
Z Z PS
G2 T
Negative Sequence Network
Z Z Z
T P0 S0
Z
G0
Ground Paths
Z
T0
Zero Sequence Network
Figure 17 — Single-line diagram of a system and sequence network connections
for a single-phase-to-ground fault
46
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
I'
|     |     | I   |     | 0     |      |     | I   |
| --- | --- | --- | --- | ----- | ---- | --- | --- |
|     |     | 0   |     |       |      |     | 0   |
| I   | I   |     |     |       |      |     |     |
| 0   | 0   |     |     |       |      |     |     |
|     |     |     | I 0 |       | I' 0 |     | I 0 |
|     |     | I   |     |       |      | I 0 |     |
|     |     | 0   |     | I'    |      |     |     |
|     |     | 3I  |     | 0 3I' | 0    |     | 3I  |
|     |     |     | 0   |       |      |     | 0   |
I
0
|     | (a)  |     |     |     | (b)  |     |     |
| --- | ---- | --- | --- | --- | ---- | --- | --- |
Figur(ea 1)8 —Flow of zero-sequence currents in delta-w(ybe) and
grounded wye-grounded wye connected transformers
5.7.2 Effectively grounded systems
Most transmission systems are effectively grounded because all the neutrals of the wye windings are tied
physically to the station ground mat, thus minimizing the impedance between the neutral and the ground.
Although there may be no impedance between the transformer neutral and ground, the transformer may not
have sufficient capacity compared to the system to stabilize the phase-to-ground voltages during a fault.
Therefore, IEEE Std 142™ [B53] defines a system to be effectively grounded as follows:
It is grounded through a sufficiently low impedance such that for all system conditions the ratio of zero-sequence
reactance to positive-sequence reactance is positive and not greater than 3, as shown in Equation (15):
X
0
| ≤3  |     |     |     |     |     |     | (15)  |
| --- | --- | --- | --- | --- | --- | --- | ----- |
X
1
and the ratio of zero-sequence resistance to positive-sequence reactance is positive and not greater than 1,
as shown in Equation (16):
R
| 0 ≤1  |     |     |     |     |     |     | (16)  |
| ----- | --- | --- | --- | --- | --- | --- | ----- |
X
1
IEEE Std 142 [B53] discusses methods to attain an effectively grounded system.
5.7.3 Impedance-grounded systems
5.7.3.1 General
Some transmission systems do have impedance grounding for various reasons. These systems are either
resistance or reactance grounded and have the transformer neutrals connected to ground as shown in Figure 19.
|     |     | I   |     |     |     |     | I   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 0   |     |     |     |     | 0   |
| I   | I   |     |     | I   | I   |     |     |
| 0   | 0   |     |     | 0   | 0   |     |     |
|     |     |     | I   |     |     |     | I   |
|     |     |     | 0   |     |     | I   | 0   |
|     | I   |     |     |     |     | 0   |     |
0
| I   |     |     |     | I   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   |     |     |     |     | 0   |     |     |
|     |     | 3I  |     |     |     |     | 3I  |
|     |     |     | 0   |     |     |     | 0   |

|     | (a)  |     |     |     | (b)  |     |     |
| --- | ---- | --- | --- | --- | ---- | --- | --- |
Figure 19 —Grounding transformer neutrals via a resistance and via a reactance
|     | (a) |     |     |     | (b) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
47
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
5.7.3.2 Reactance-grounded systems
Three different types of reactance-grounded systems are high-reactance grounding, resonant grounding, and
low-reactance grounding.
High-reactance grounding is not applied for transmission system grounding and was discontinued as a
generator grounding practice many years ago, primarily for problems associated with arcing ground faults.
Resonant grounding is more common in Europe and other world locations than in North America. In this
scheme a reactor, also known as a Petersen Coil or ground fault neutralizer, with taps is sized to match the
total system to ground capacitance. Therefore, there will theoretically be no fault current for a phase-to-
ground fault and the fault arc will be quickly extinguished. Faults are cleared for about 75% of the phase-
to-ground faults without opening a breaker.
In theory, resonant grounding should significantly reduce the number of system outages, but there are some
disadvantages. Two of the disadvantages are as follows:
 The entire system, including transformers, should be fully insulated for line-to-line voltage.
 The ground reactor or its tap setting should be changed for different system configurations that
modify the effective shunt capacitance of the system.
Low-reactance grounding is occasionally applied at the neutral of large autotransformers with a delta tertiary
winding. A large autotransformer may provide a ground path resulting in an X0/X1 ratio substantially less than
one at that point in the system. For this case, the phase-to-ground fault current would be larger than the three-
phase fault current. A low-reactance ground would reduce the phase-to-ground fault current to the three-phase
fault current level or lower. Additionally, a low-reactance ground may be desirable to reduce ground fault
current in order to reduce the impact of mutual coupling with parallel circuits.
5.7.3.3 Resistance-grounded systems
Resistance grounding is not typically used in transmission systems but can reduce single phase-to-ground
fault currents. Line protection applications require different protection considerations than the conventional
effectively grounded system. When a resistor is applied between the neutral and ground, the phase-to-
ground fault current is more in phase with the faulted phase voltage. Also, the zero-sequence current and
polarizing voltage are more in phase.
5.8 Transmission lines with distribution substation taps
5.8.1 General
It is a common utility practice to tap transmission lines to serve distribution load. Figure 20 shows a typical
power system. The impedances of segments between bus 4 and bus 5 are shown as Z , Z , Z , Z , and
41 1T 2T 3T
Z . The impedance of the line segment 3T as seen by the distance relays provided at CB 12 for a fault at
25
bus 3 is the voltage drop in that segment due to the currents contributed from bus 1 plus the current
contributed from bus 2 divided by the current contributed from bus 1 only. This apparent impedance is,
therefore, not equal to the line impedance Z but is a larger value if there is current infeed from CB 21 or
3T
smaller value if there is a current outfeed from CB 21. More discussion on the impact of current outfeed
and current infeed is provided in 6.6.2 and 6.6.3. Similarly, the apparent impedance of the line segment 3T
seen by the relays provided at CB 21 is not equal to the impedance of that segment.
On a three-terminal line, the impedance “seen” by each relay will depend, in part, on the current
contributions from the other terminals. The impedance “seen” by a distance relay is not always the actual
line impedance from a relay terminal to the point of fault. The relay considerations surrounding the
protection of the lines between CB 12, CB 21, and bus 3 are discussed in 5.8.2 through 5.8.8.
48
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Bus 4 Bus 1 Bus 2 Bus 5
CB 41 CB 11 CB 22 CB 51
Z CB 12 CB 21 Z
41 T 25
Z 1T Z 2T
Z
3T
Bus 3
CB 31 MD 32 MD 33
M M
C S CS 34
Figure 20 —Transmission line with a distribution substation tap
5.8.2 Length and location of tap line
No significant relaying problems occur because of a tap on the line if the apparent impedance of the line
segment 3T is less than the impedances of line segments 1T or 2T. Setting compromises, such as the
desired reach, are required for relays at CB 12 if the apparent impedance of the line segment 3T as seen by
those relays is greater than the impedance of the line segment 2T. Similarly, setting compromises, such as
the reach, are required for relays at CB 21 if the apparent impedance of the line segment 3T as seen by
those relays is greater than the impedance of the line segment 1T. This issue is further complicated if the
impedance of the line segment 3T is greater than the combined impedance of line segment 1T and 2T.
5.8.3 Length of lines on adjoining buses
The time delay settings for the primary protection of the tapped line may have to be increased to allow
backup protection on adjacent lines to operate first for faults on the adjacent line when line relay settings
for the tapped line are extended because of its tap. For the example system in Figure 20, time delay should
be increased for the backup protection at CB 12 to coordinate with the backup protection for CB 22 for
faults at and beyond about 80% of CB 22’s zone 1 if the following conditions are satisfied:
 The apparent impedance of line segment 3T as seen by relays at CB 12 for a fault on bus 3 is
greater than the impedance of the line segment 2T.
 The apparent impedance seen by relays at CB 12 for a fault on bus 3 plus the impedance of the line
segment 1T is greater than the sum of the impedances of the line segments 1T and 2T plus the
apparent impedance of the line from bus 2 to bus 5 as seen by the relays at CB 22.
5.8.4 Relay settings limiting line loading
Whenever line relay settings are extended because of tapped lines, precautions should be taken to ensure
that the relay settings detect line faults without limiting power transfer or load-carrying capabilities below
acceptable values. Line loadability is discussed in detail in a 2001 IEEE PSRC report, “Transmission line
protective systems loadability” [B52].
5.8.5 Substation considerations that affect transmission line relaying
Generally, transmission line-protection systems are not designed to see tapped transformer faults or low-
voltage bus faults. The protection for these two types of faults is provided at the distribution station. The
relays at the distribution station trip the interrupting device associated with the transformer. Where breakers or
49
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
circuit switchers are not used as high-side interrupting devices, the relays initiate a transfer trip signal to the
remote breakers. In some applications, a ground switch provided on the high-voltage side of the distribution
station transformer is closed, but this practice is not a desirable option. Since transmission relaying is usually
not set to see transformer or low-voltage bus faults, if a breaker or circuit switcher fails to trip, local backup
should be provided at the distribution station. This local backup can be in the form of transfer trips, ground
switches, or air switches. When a ground switch is used, a motor-operated isolator is often connected on the
transmission-line side of the ground switch and transformer to allow reclosing of the transmission line after
the transformer has been isolated. More discussion of this issue is available in IEEE Std C37.91 [B56].
5.8.6 Use of circuit switchers for transformer protection
Circuit switchers rated below the high-voltage bus fault duty are sometimes used for protecting tapped
transformers. The circuit switcher may be blocked from tripping for high-current faults by the use of an
instantaneous overcurrent relay. The remote transmission line relaying should sense this particular fault and
initiate tripping. If the circuit switcher is not blocked for faults above its rating, the remote transmission
line relaying should be designed such that it trips before the circuit switcher trips.
5.8.7 Transformers as load taps on a transmission line
Transformers can be tapped off at any location on a transmission line. Figure 21, Figure 22, and Figure 23
show typical configurations. The key protection challenges, in addition to those provided in previous
clauses, indicated in these situations are described below. A transformer that is not a source of phase or
ground fault current requires no special attention, but a transformer that is a source of phase or ground
currents requires special attention.
Bus A Bus B
Line
Figure 21 —Load tapped near one terminal
Bus A Bus B
Line
Figure 22 —Load tapped near center of line
50
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Bus A Bus B
N.O.
Bus C Bus D
Figure 23 —Switch creates the potential for parallel multi-terminal lines
All tapped transformers should be provided with their own dedicated protection systems that operate as fast
as or faster than the line-protection systems for faults in the transformer. These dedicated transformer
protection systems will either isolate the faulted transformer or, if high fault-clearing facilities are not
available at the tapped station, will initiate tripping of the breakers at the remote terminals of the line
followed by automatic isolation of the transformer by a motor-operated disconnect switch. If the transfer
trip is inoperable, the remote line circuit breakers are required to interrupt the fault, having been initiated by
its own measuring relays. In some cases, the local motor-operated switch can be opened to aid in clearing
the fault by transferring the fault to the motor-operated switch as it opens. The switch becomes sacrificial in
nature, as the fault current would probably exceed the interrupting rating of the switch, but would minimize
the time that the transformer is experiencing the fault. Isolating the transformer automatically ensures that,
if the transmission line is re-energized, the faulted transformer is not re-energized with the line.
If transformers are connected to the lines as shown in Figure 23, closing the normally open (N.O.) switch
will result in a multi-terminal line. Further complications will result if the lines are mutually coupled.
It is usually difficult to provide instantaneous line protection that will trip for faults on the line but not trip
for high-side faults in the tapped station unless CTs and relays are provided at the tapped station and form a
part of the line-protection system. In view of the infrequency of such faults, it may be considered
acceptable to allow the line to trip simultaneously with the high-side interrupting device at the tapped
station for such faults. The line could then be automatically or manually reclosed, restoring the
transmission system with the tapped station (with the fault) isolated.
It is important that transmission line protection coordinates with low-side protection at the tapped station.
Low-side equipment (such as distribution feeders) is usually exposed to faults more frequently than the
high-voltage side of the station. Therefore, it is important that the instantaneous transmission line
protection should not be able to sense faults on the low side of the tapped station.
The most critical case is when the line terminal nearest to the tapped station is connected to a strong source,
and the remote terminal of the line is connected to a weak source, and the infeed from the weak-source
terminal does not desensitize significantly the protection at the strong-source terminal for faults in the
tapped station.
5.8.8 Transformer as a source to the transmission system
In some instances, it is possible that a distribution station includes local generation and the distribution
transformer becomes a source that feeds current to a fault on the transmission line. Thus, the fault current
contribution of the distribution transformer should be considered in the relay settings. The resulting infeed
can cause line distance relays to underreach. This potential exists whenever generation is connected to the
distribution bus, or whenever the distribution bus is connected to another distribution circuit served from a
51
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
different transmission line. If a positive-sequence source capable of supplying sustained current to a
transmission fault is available from the distribution system, provision to trip the source, or its feed to the
transmission system, should be provided. Also, if the transformer has a delta winding, and the high-voltage
winding is connected grounded wye, the transformer will be a ground source for zero-sequence currents,
causing a similar underreaching of the line ground relays.
If the transformer is a zero-sequence source, the resulting zero-sequence current infeed should be
considered when setting the remote ground distance relays or overcurrent relays. The zero-sequence current
infeed will desensitize both ground distance and ground overcurrent relays at the main terminals. Since the
presence of a zero-sequence source will also tend to reduce the zero-sequence voltage at the line terminals,
the performance of zero-sequence directional units should also be evaluated.
A transformer source to a transmission line may be delta connected on the line side and be a source of
positive- and negative-sequence currents to a single-phase-to-ground fault until the last ground source is
removed from the line. Then, the line will still be energized by this source; however, no appreciable current
can flow due to the delta transformer winding. The delta will remain a source of positive- and negative-
sequence current-flow if the ground source remains on the line (such as a wye-grounded /delta transformer
tapped to the line) after the main transmission line terminals open. The positive- and negative-sequence
source of back-feed should be eliminated for multiphase faults and for single-line-to-ground faults to
ensure arc extinction.
5.9 Lines with devices for voltampere reactive and flow control
5.9.1 General
Control devices are installed on transmission lines sometimes for making the transmission system more
efficient and controllable; these devices may affect protection systems provided to protect the line. Some of
the most commonly used devices are as follows:
 Shunt reactors
 Shunt capacitors
 Series capacitors
 Series reactors
 Phase-shifting transformers
 Static voltampere reactive (var) compensators (SVCs)
The application of these devices and possible problems they might create for the line-protection systems are
briefly discussed in this subclause.
5.9.2 Shunt reactors
Shunt reactors are applied on transmission lines to compensate for large line-charging currents and
capacitive loads. Shunt reactors, whether connected to the line or the bus, should have dedicated protective
relays. The reactor may be switched as a unit with the transmission line or may be connected to the bus
behind the line terminal. The reactor current may or may not be included in the current measured by the
line-protection system. The shunt reactors may affect the performance of line-protection systems when the
reactors are located within the line-protection zones.
Shunt reactors connected to the bus behind the line-protection system will generally not have a direct effect
on the line-protection system. These shunt reactors are protected with dedicated protection systems. Details
of those protection systems are given in IEEE Std C37.109™ [B62].
52
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
A reactor that is connected to the system within the line-protection zone will compensate for some of the
effects of line capacitance; some protection systems are adversely affected by the line-charging currents. The
line-protection system should be designed to be reliable in the event that the shunt reactor is out of service.
A reactor connected directly to the protected line allows the flow of “ring-down” currents, which are
oscillation currents caused by the line impedance, the shunt capacitance, and the reactor on line de-
energization. These ring-down currents will result in a gradually decaying line terminal voltage that may
affect an automatic reclosing scheme that is supervised by voltage detectors. The ring-down frequency, due to
partial compensation by the line reactor, is usually lower than the rated frequency of the power system. Any
relays that sense this oscillating current should be able to accommodate the impact of the reduced frequency
currents and voltages. The ring-down voltages may also affect the line-protection system during an attempt to
reclose the line, especially if there is a significant time interval between the closing of the individual phases of
the circuit breaker picking up the line. These voltages have been found to cause high-speed protection systems
to undesirably trip the line circuit breaker during line pickup when there is dissymmetry between closings of
phase, as described by Engelhardt [B29] and by Henville and Jodice [B33].
When a single phase is tripped with the intent of reclosing the circuit breaker in that phase, the faulted phase
may still be energized due to conduction of current through the distributed capacitance between the phases.
This is known as secondary arc phenomenon. The arc extinguishes if the current is low, such as in short lines,
or lines with large spacing between phases. The time for the ionized gasses to dissipate is considerably longer
than the deionization time if three-phase tripping were employed. On longer lines and double circuit lines, the
magnitude of the secondary arc current may be too large to self-extinguish. One method used to extinguish the
arc during this condition is a four-legged reactor, as described in the 1992 PSRC report, “Single phase tripping
and auto reclosing of transmission lines” [B47]. A neutral is formed for three-phase reactors, and the fourth
reactor is connected between the neutral and the ground. The reactor is sized to cause parallel resonance for
the circuit feeding the fault. This causes the secondary arc current magnitude to be very small, allowing the
arc to self-extinguish much sooner than would be the case if the four-legged reactor were not used.
5.9.3 Shunt capacitors
Shunt capacitors are used to provide additional var requirements or to increase power system voltages. Usually,
these devices are installed on transmission or distribution buses. In general, shunt capacitors are installed on the
bus and do not affect the line relays. Detailed discussion is provided in IEEE Std C37.99™ [B58].
When large shunt capacitors are connected behind a line terminal, high-magnitude, high-frequency currents
can flow from the capacitor into a close-in line fault as described by McCauley et al. [B85]. These currents
decay to a negligible value very quickly; i.e., in a few milliseconds. The high frequency of these out-rush
currents can cause very high voltage to be developed across CT secondary windings. If high voltages due to
shunt capacitor transient out-rush is a concern, surge suppression varistors may be connected across the CT
secondary windings as described by Drakos et al. [B22].
5.9.4 Series capacitors
Series capacitors are applied to improve stability, provide better load division on parallel transmission
paths, reduce voltage drop during severe system disturbances, or increase power transfer capability. The
capacitors may be installed at one end of the line, at both ends of the line, or at midline. The impedance
value of a series capacitor is typically between 25% and 75% of the line impedance. Capacitor overvoltage
protection is a part of capacitor bank protection, as described in IEEE Std C37.116™ [B66]. The
overvoltage protection consists of a parallel air gap and/or a metal oxide varistor (MOV). The purpose of
this protection is to bypass the capacitor if fault or load current will produce voltages that are high enough
to damage the capacitor. A bypass breaker is also used in the design for non-fault-related capacitor
protection, as well as for providing flexibility of operation. Line-protection schemes should also take into
consideration the possibility of air gap or MOV failure, unsymmetrical gap flashing, or MOV conduction.
53
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Series capacitors affect the performance of line distance relays; therefore, distance relays specifically
designed to protect series-compensated lines should be selected.
The effects of series capacitors on other relays in the nearby system should also be considered, even though
they are not applied directly on a series-compensated line. Some utilities require a comprehensive series of
transient performance tests to demonstrate the speed, dependability, and security of protection systems
applied on lines with series capacitors, or adjacent to such lines. Subclause 6.8 further discusses protection
of transmission lines with series capacitors.
5.9.5 Series reactors
Series reactors are typically applied for better load division on parallel paths or to limit fault current levels.
Series reactors often have their own protection, especially since certain internal faults might not be detected
by the line relays. Also, transient disturbances during energization and de-energization should be studied to
prevent any possible problems. Series reactors can be bypassed with a circuit switcher or another switching
device. Relay setting changes are usually required when the reactor is bypassed. This can be accomplished
with an adaptive relay system.
5.9.6 Phase-shifting transformers
Phase-shifting transformers are installed to control power flow between interconnected systems or parts of a
system. A phase-shifting transformer needs its own protection system that may consist of transformer
differential, neutral overcurrent, sudden pressure, and other relays. Location of the CTs and VTs for line-
protection relays with a phase-shifting transformer is important. CTs used on the bus side of the transformer
will be exposed to inrush currents flowing into the transformer bank, and VTs on the bus side will provide
voltages with different angles than the voltages from line side. VTs and CTs providing voltages and currents
to the line-protection devices should be located in such a manner that they continue to provide correct
information to the protection devices when bypass switches are operated to change the phase shift setting of
the transformer. Further discussion of this topic can be found in Bladow and Montoya [B13].
5.9.7 Static var compensators
An SVC uses thyristor valves to add or remove shunt-connected capacitors and/or reactors. SVCs are
applied for var compensating, voltage control, and stability control. SVCs are usually connected to buses
rather than lines. These devices are protected by dedicated protection, as described by Chano et al. [B17]
and Taylor et al. [B100].
5.10 Parallel lines
Parallel lines are defined as lines that share the same structures or right of way for all, or a portion of, their
length. If the lines are parallel for significant distances, mutual coupling between these lines may have an
effect on the performance of the relay protection system. Mutual coupling of parallel lines and its
consideration in line-protection systems are further discussed in 5.13.
Parallel lines also increase the possibility of inter-circuit (cross-country) faults, which involve one or more
phases of each of two or more separate circuits. These lines may or may not be of the same voltage. The
effects of inter-circuit faults on protective relaying vary based on the phases involved, the voltage levels,
and the types of relays on each of the circuits.
If the line-protection scheme on the parallel line is thought to have falsely tripped and the fault on the parallel
line can be localized with fair accuracy, a line inspection should be considered. A detailed analysis of the
specifics of the fault may then be used in making modifications for preventing the recurrence of that type of fault.
54
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Because of the relatively small number of the events that cause protection problems and the large number
of permutations that would need to be considered, the subject of inter-circuit faults is not discussed further
in this guide.
5.11 Lines with high-impedance ground returns
5.11.1 General
Transmission line design factors, such as tower footing resistance and ground wire shielding, directly affect
the ground return impedance. This clause examines the causes of high-impedance ground returns and their
effects on protection systems and schemes designed to cope with high-impedance ground return effects.
5.11.2 Causes of high-impedance ground returns
Both tower footing resistance and overhead shield-wires impact the impedance of ground returns. Certain
faults, such as those involving trees, may also result in high resistances in the path of the ground fault
current. Tower footing resistance is directly affected by the characteristics of the soil and the application of
ground rods and counterpoise. In areas where high soil resistivity prevails (e.g., lava flows, gravel base), it
may be difficult to achieve effective tower grounding.
Overhead shield wires generally have the effect of substantially reducing the zero-sequence impedance of
the line. In addition, they have the effect of significantly reducing the number of lightning flashovers. Some
utilities do not install overhead shield wires because of low keraunic levels, cost, and/or the limited benefit
of overhead shield wires in areas that have high soil resistivity.
Overhead shield wires reduce the effective tower footing resistance of the line by allowing ground current
from a flashover on one tower to flow to ground through several towers. The footing resistance of several
towers in parallel results in an overall reduction in effective resistance, as shown in Figure 24.
Figure 24 —Parallel connection of tower footing resistances
5.11.3 Range of possible tower footing resistance
An average tower footing resistance of about 20 Ω may be needed if the line is to be effectively protected
from excessive lightning strikes on the line. However, tower footing resistance can vary from less than 1 Ω
to several hundred ohms. Grounding resistances, in situations where the soil resistivity is high and no
overhead shield wire is used, have been measured to be as high as 800 Ω. These high resistances amplify
the problems associated with infeed from remote terminals and weak source conditions; a detailed
discussion of this topic is given by Lefrancois [B78].
55
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
5.11.4 Effects of high grounding resistance on the operation of line-protection systems
High-resistance ground faults present certain considerations and challenges to protecting transmission lines.
Some of the general factors that should be considered are as follows:
 Ground distance protection may be adversely affected and may not be sensitive enough to operate.
 Ground overcurrent relays may be set at levels such that they become more sensitive than distance
relays.
 The operating time of protection systems could increase; however, longer fault-clearing times can
usually be tolerated with reduced fault magnitudes.
 It may become more difficult to identify the faulted phase if single-phase tripping and reclosing is
to be applied.
 The accuracy of the fault-locating techniques based on impedance measurement may be reduced.
An example of the response of the ground protection systems during high-resistance ground faults provided
by an electric power utility is shown in Figure 25.
700
600
500
400
300
200
100
0
10 20 30 40 50 60 70 80 90 100
56
Copyright © 2016 IEEE. All rights reserved.
smhO
,egarevoC
evitsiseR
Bus A F Bus B
Bus A
Bus B
Percentage Distance from Terminal A
Figure 25 —Response of relay systems to high-impedance faults
at different locations on the line
The fault resistance coverage limit is for an example 500 kV transmission line. The limit is based on the
assumption that the total fault current is limited only by the fault resistance with the system and the
transmission line impedances are so small as to not be significant. The limit of about 300 Ω for a midline
fault is calculated from the total fault current being approximately 500 kV/(√3 × 300) = 962 A. For the
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
example system, at the midline location, 50% of the current (481 A) comes from each terminal of the line,
3000/5 A line CTs are used, and the pickup of the ground overcurrent relay is set at 0.5 A. Allowing for a
dependability factor of 1.5 (the fault current being at least 150% of the pickup setting of the overcurrent
relay, the limit is about 300 Ω for a midline fault. The fault-resistance coverage limit increases as the fault
location moves toward the line terminals. For example, Figure 25 shows that a ground fault near terminal A
with approximately 600 Ω fault resistance would be detected. After terminal A trips, the current in the fault
resistance decreases, and, therefore, the voltage drop in the fault resistance decreases. The consequence is
that the ground fault contribution from terminal B increases. This causes the terminal B protection system
to detect the fault and initiate line trip. Because this is only an example of an application, actual system data
should be used to evaluate the impact of fault impedance.
5.11.5 Substation ground sources
Sources of ground current for line-to-ground faults can be the same for any of the terminal configurations
shown in Figure 26. These sources could be a delta-wye transformer shown in Figure 26(a), an
autotransformer with the neutral grounded solidly shown in Figure 26(b), or through a zig-zag transformer
shown in Figure 26(c). A grounding transformer can be added at the substation if the ground current is not
sufficient to properly detect ground faults. In some cases, as in a switching station, all ground current is
supplied by remote sources.
(a) (c)
(b)
Figure 26 —Substation ground sources
5.12 Terminal configuration considerations
5.12.1 General
There are six basic configurations for terminating transmission lines:
 Single breaker
 Breaker-and-a-half
 Double breaker
 Double bus
 Ring bus
 Transfer bus
The bus configurations are covered in detail in IEEE Std C37.234 [B69]. The various bus configurations do
not typically affect line protection except where selection of the voltage source for the line protection is
concerned. Voltage sources for line protection are typically connected to the substation bus or to the line
side of the circuit breaker. Selection of the voltage source location is driven by cost factors, reliability,
utility practices, and operational needs. For example, it may be difficult to justify line-side potentials at
lower voltage due to the cost of providing a three-phase VT for each line position. However, on more
57
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
critical high-voltage circuits, line-side potentials may be required to meet reliability requirements so that a
single point of failure does not result in the removal of multiple line-protection schemes. When
synchronism checking is used, then a common approach is to apply a single-phase VT on either the line or
the bus and a three-phase VT on the opposite side of the breaker for line protection.
If a line is connected to a two-breaker terminal, such as a ring or breaker-and-a-half bus, a potentially long
forward-reaching and appropriately time-coordinated zone 3 may need to be set at the remote terminal of
this line for a failed breaker at the two-breaker terminal, to cut off contribution from an adjacent line or
transformer on the ring or breaker-and-a-half bus for a fault on the protected line. See 6.2.4 for more detail.
5.12.2 Transfer bus configuration
A transfer bus configuration may have an impact on the design of the line-protection scheme and is shown
in Figure 27. Several lines are connected to the main bus by circuit breakers dedicated to protect those
lines. An additional circuit breaker, a bus coupler circuit breaker, is provided; this circuit breaker is used to
connect the main bus with the transfer bus and provide an alternative connection for each circuit. This
allows a circuit breaker dedicated to an incoming or outgoing circuit to be removed from service without
interrupting the connection of the circuit with the station.
CB2
CB1
CB3
58
Copyright © 2016 IEEE. All rights reserved.
suB
refsnarT
suB
noitatS
901
201 21 22 202
11 12
101 102 31 32
Bus coupler
301 302
902
Figure 27 —A substation with transfer bus configuration
The transfer bus configuration results in some additional considerations for the protection of the lines
terminated at the station. During a bypass operation, there are two options to protect the transferred circuit.
The first is to connect the CTs, status, and trip circuit of the bus coupler breaker to the relays protecting the
transferred circuit. This requires the use of auxiliary switches to transfer the physical relay connections.
The second option is to use relays dedicated to the bus coupler breaker to protect the transferred circuit. It
is necessary that these relays be set to protect any of the circuits terminated at the station, which can be
accomplished using multiple settings groups in modern microprocessor relays. This option is complicated if
communications-based protection schemes are used on any of the circuits.
5.12.3 Stub bus configuration
In some breaker-and-a-half or ring bus configurations, a transmission line may have a disconnect switch to
separate the line from the main bus. Opening of the disconnect switch allows line maintenance or repair while
the line breakers can be closed to maintain bus continuity. In this configuration, the bus section between the
breakers and the line disconnect is referred to as a “stub bus.” While the line is cleared for maintenance, it
may be grounded at or near the location the work is taking place. If the relaying potentials are on the line side
of the disconnect switch, any distance or directional relays will be unable to operate due to a lack of a
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
polarizing signal (i.e., no line voltage). A line current differential relay will also operate incorrectly, as the
differential currents will not represent the actual fault currents (i.e., a stub bus fault results in a tripping of the
remote line breakers and a line fault results in tripping of the stub bus breakers). Additional stub bus
considerations are addressed in 8.16 of IEEE Std C37.234™-2009 [B69] and in IEEE Std C37.243™ [B70].
5.13 Mutual coupling considerations
Mutual coupling between transmission lines is common in power systems and may have a significant effect
on the behavior of the protection systems during faults involving ground. The positive- and negative-
sequence mutual impedances of parallel circuits are negligible; however, the zero-sequence mutual
couplings are usually significant and should be considered when setting relays for detecting ground faults.
A close-in external fault with the second circuit open and grounded at both ends, as shown in Figure 28, is
usually considered to evaluate the effects of mutual coupling on the protection systems applied to line A.
The purpose is to verify that the relays do not overreach for this condition. If the relay overreaches,
remedial action should be taken, such as the reach of the underreaching element may be reduced. For
example, the settings of the instantaneous overcurrent element may be increased or the reach of the zone 1
ground distance relay may be reduced.
Bus A Bus B
R
3I
0f
1Φ − G
Line A
S 1 OPEN Z 0m OPEN
Line B
S
2
3I
0m
Figure 28 —Circuit open and grounded at both ends
An internal single-line-to-ground fault very close to the remote bus with both lines in operation, as shown
in Figure 29, should also be considered to ensure that the overreaching pilot element detects the fault
without the need for sequential tripping. This may require that the reach of the overreaching zone be
increased, or the residual compensation factor may be increased if this adjustment is available in the relay.
With the increased reach of the overreaching element, current reversal blocking may have to be used to
prevent undesired operation during current reversal.
Bus A Bus B
R
3I
0f
1Φ − G
Line A
S 1 Z 0m
Line B
3I 0f S 2
Figure 29 —Fault near remote terminal
59
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
A close-in fault on the line side of the open breaker on the protection system applied to line B, as shown in
Figure 30, should be considered as well.
Bus A Bus B
R
3I
0f
Line A
S 1 Z 0m S 2
OPEN 1Φ − G
Line B
3I
0f
Figure 30 —Close-in fault near end
Sometimes, parallel lines have a common bus at one terminal but are connected to different buses at the
other terminal, as shown in Figure 31. A fault close to the end of the mutually coupled section on the line
whose circuit breaker is open should be considered for evaluating the impact of mutual coupling on
ground-fault protection systems. This also applies to mutually coupled lines that are not connected to a
common bus at either terminal, as shown in Figure 32.
Bus A Bus B
R
3I
0f
Line A
S 1 Z 0m S 2
1Φ − G
Line B
Bus C
OPEN
3I
0f
S
3
Figure 31 —Mutually coupled lines with one common bus
Bus A R Bus B
3I
0f
Line A
S 1 Z 0m S 2
Line B
Bus C Bus D
OPEN 3I
1Φ − G 0f
S S
3 4
Figure 32 —Mutually coupled lines without a common bus
60
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Two transmission lines that operate at different voltages and have different zero-sequence current sources
are mutually coupled sometimes, as shown in Figure 33. The effect of ground faults on the higher voltage
line can be the determining factor for the setting of relays for ground fault-protection of the healthy lower
voltage line. The setting calculations for the ground-fault protection system should be based on the
maximum external fault current that can be different from the remote-bus-fault current for mutually
coupled lines. Faults at the end of the mutually coupled section are often more important than the line-end
faults for lines that are mutually coupled for a portion of their length.
Bus A Bus B
R
3I
0f
S S
1 2
Z
0m
3I
0f
OPEN
S S
3 4
1Φ − G
Figure 33 —Mutually coupled lines at different voltages and different ground sources
Sequentially cleared faults can also cause problems in mutually coupled lines. The induced zero-sequence
current in an unfaulted, mutually coupled line can suddenly change direction in such cases. This sudden
reversal can cause problems on schemes that use zero-sequence polarized directional ground relays without
current reversal logic.
Zero-sequence voltage reversal can also cause problems. The effect is caused by zero-sequence current in
an unfaulted line that is mutually coupled to a faulted line when the zero-sequence sources at the ends of
the faulted and unfaulted lines are not strongly tied together. The induced current in the unfaulted line can
cause zero-sequence voltages at each end to have opposite polarity from each other, and can cause zero-
sequence (current or voltage) polarized directional ground overcurrent relays at both ends of the line to
identify it as a fault on the protected line. This can cause undesirable tripping of the unfaulted line,
especially in the directional comparison schemes [B2]. Phase comparison and current differential schemes
are not susceptible to the problems of zero-sequence mutual effect, because any influence from this source
manifests itself in the form of a “through” current.
The following guidelines are useful to avoid incorrect operation of the ground overcurrent relays caused by
the mutual coupling effect.
 Consider using current reversal logic in directional comparison schemes if zero-sequence
polarization is used for directional ground overcurrent protection.
 Consider using negative-sequence polarized directional ground overcurrent relays, current
differential relays, or phase-comparison pilot schemes.
 Consider using directionally controlled instantaneous ground overcurrent relays.
 Consider the application of relays with selectable setting groups.
61
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6. Relay schemes
6.1 General
Non-pilot, pilot, and special relay schemes used for protecting transmission lines are described in this
clause. Polarization of directional ground overcurrent relays and problems associated with multi-terminal
lines are also discussed. These are followed by considerations for protecting series-compensated lines,
single-phase tripping, and application of distance relays to short transmission lines. Finally, relay
considerations for system transients and application of multifunctional relays are addressed.
6.2 Non-pilot schemes
6.2.1 General
Non-pilot-type protection schemes include overcurrent relay schemes, directional overcurrent schemes, and
distance protection schemes. Overcurrent relay schemes are described in 6.2.2, overcurrent directional relay
schemes are described in 6.2.3, and distance protection schemes are described in 6.2.4.
6.2.2 Non-directional overcurrent relay schemes
Overcurrent protection is the simplest and least expensive form of fault protection that can be applied for
protecting transmission lines. The operating principles of these schemes depend only on magnitude of the current
applied to the relay. Two overcurrent elements are typically applied in each of the three phases. One is the time-
overcurrent element (shown as TOC in Figure 34); the operating time of this element could be fixed or could be
inversely proportional to the current magnitude. The other is an instantaneous-overcurrent element (shown as
IOC in Figure 34); this element operates with no intentional time delay. Often, two additional elements are also
included. One is a ground-time overcurrent element and the other is an instantaneous ground overcurrent
element. Connections of a three-phase overcurrent relay including the ground overcurrent facility are shown in
Figure 34. Various shapes of time-overcurrent characteristics that may be used are shown in Figure 35.
Phase currents or sequence currents can be used as the operating quantity. Phase overcurrent relays operate
for all possible fault types; the pickup settings of these relays should be higher than the current supplying
maximum-expected normal or emergency load. Negative- and zero-sequence overcurrent relays do not
operate for balanced loads or for three-phase faults; therefore, they can be set for pickup currents less than
the expected load currents.
TOC IOC
50/51
TOC IOC TOC IOC
50/51 50N/51N
TOC IOC
50/51
IOC = 50
TOC = 51
Figure 34 —Connections for overcurrent phase and ground relay
62
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
100
10
1
0.1
1 10 100
63
Copyright © 2016 IEEE. All rights reserved.
emiT
Moderately Inverse
Inverse
Very Inverse
Extremely Inverse
Multiples of PU
Figure 35 —Time-overcurrent curve shape comparison
Instantaneous tripping can be applied if the pickup point of the instantaneous unit can be set higher than the
maximum contribution to faults outside the protected line. The percentage of a line that can be protected by
an instantaneous overcurrent varies with line length and source impedance. Time delays are generally
required to achieve coordination with downstream protective devices if an entire non-radial line is to be
protected. Figure 36 shows an example of coordination between a relay with a time and instantaneous
element (the primary relay), and an upstream (backup relay) with only a time element. The pickup point of
the instantaneous unit must be set with sufficient margin so the relay will not operate for out-of-zone faults,
external faults on mutually coupled lines, low-side faults on tapped transformers, nor on transformer
magnetizing inrush current for tapped transformers on the line. With respect to transformer magnetizing
inrush, ground instantaneous overcurrent elements must be set above maximum inrush only if the
transformer is connected wye-grounded on the high side or for a grounded autotransformer with a closed
delta tertiary. Coordination of ground instantaneous overcurrent elements for transformer magnetizing
inrush is not required if the transformer is delta-connected on the high side.
The pickup value of the time element should be set to prevent tripping for the maximum load current that
can flow in the line in either direction. The time adjustment (time dial setting) should be set to produce the
fastest operating time that will not cause loss of coordination with upstream and downstream relays. The
effect of varying the time adjustment is illustrated in Figure 37 for a typical time overcurrent relay. Details
of standard inverse time characteristics are given in IEEE Std C37.112™ [B64].
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
64
Copyright © 2016 IEEE. All rights reserved.
)sdnoces(
emiT
10
Primary Relay
Backup Relay
1.0
0.1
Maximum Contribution to Faults
Outside the Protected Line
0.01
1.0 10 100
Current
Figure 36 —Coordination of time-overcurrent relays
Figure 37 —Varying time adjustment on overcurrent relay characteristic curves
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Non-directional overcurrent relay schemes find limited application on transmission lines because
transmission lines usually have energy sources connected to at least two terminals. The non-directional
relays have to be coordinated with protective devices both in front of and behind the line terminal. This
makes the coordination of non-directional relays an impossible task in many applications. These relays are
sometimes applied only at the terminal that contributes higher fault currents.
Non-directional overcurrent relays can be applied on long transmission lines if the contribution of fault current to
faults in the reverse direction (behind the terminal) is limited to small magnitudes because of the impedance of
the long line. Also, the magnitudes of fault currents for close-in faults in the forward direction are much higher
than the magnitudes of currents for faults beyond the remote terminal. In such applications, instantaneous, non-
directional phase and ground overcurrent protection can provide very fast and secure detection of close-in faults.
Overcurrent relay schemes are used primarily on distribution and subtransmission feeders where load and
fault currents flow in one direction (e.g., on radial feeders) and where the cost of protection equipment is
desired to be low. The choice of a time-overcurrent characteristic is based on sources, lines, and loads. In
general, the characteristic of the relays applied at a line terminal should closely match with the characteristics
of the downstream protective devices so that proper coordination is achieved at all fault-current levels.
Overcurrent relays that are set to underreach (similar to the setting of a zone 1 distance relay) also operate
instantaneously. The settings of these relays should be such that they do not operate for any fault external to
the line under any power system operating condition. The setting of all underreaching, instantaneous-
overcurrent relays becomes a complicated issue if system impedances and infeeds can change significantly
under normal operating conditions. The setting of underreaching, zero-sequence and ground instantaneous-
overcurrent functions is also complicated by the presence of mutually coupled lines (see 5.13 for further
discussion of the impact of mutual coupling of lines).
6.2.3 Directional overcurrent relay schemes
A directional overcurrent relay scheme usually consists of three or four measured time-overcurrent
elements. The three-phase elements can be used to calculate the residual ground current, or a fourth
measured element in the neutral leg can be used. The overcurrent elements are either supervised or
controlled by polarizing inputs that may be voltages, currents, or both. This arrangement allows the relay to
operate for current flows due to faults on the line side or the bus side of the relay.
Two options are generally used for combining the operation of the overcurrent and directional units. The first
option is to allow the circuit to be tripped if and only if both units operate. The second option is to control the
input to the overcurrent element, preventing its operation unless the directional element operates. In an
electromechanical relay scheme, for example, a directional relay contact can be installed in the shading coil
circuit of an overcurrent relay to control the operation of the overcurrent relay. This is often referred to as
“torque control” because the directional element controls the operating torque of the overcurrent relay.
One advantage of directional-torque control of the input over supervising the output of an instantaneous
overcurrent element is that there is no race between reset of the instantaneous overcurrent element and
operation of the directional element during current reversals. The directional element must operate before
the instantaneous element can operate.
Phase-directional relays are polarized by phase voltages, while the ground-directional relays are commonly
polarized with zero-sequence voltages, currents, or both, or with negative-sequence voltages. Other methods
of polarizing can also be used as discussed in 6.5.5. Zero-sequence voltage is obtained from the broken-delta
secondary of grounded-wye VTs that provide 3V as shown in Figure 38. In microprocessor-based relays, the
0
3V is calculated internally from the three-phase voltages applied to them as inputs. Zero-sequence current
0
polarization is only possible if there is a ground current source at the bus; zero-sequence current polarization is
further discussed in 6.5.3. Negative-sequence polarized directional units are often applied when zero-sequence
mutual coupling effects cause zero-sequence directional units to lose directionality.
65
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
High Voltage
a
b
c
G
Voltage Transformers
or Devices
G
Secondary
a
b
c
3V
0 G
X Y
V
ag
G 3V 0
Alternate if Double Secondary
X Y
Voltage Transformers or
Devices are Not Available
V
V ag V
cg bg
0
V
V = 3V bg
XY 0
V Phasors for a Phase “a” to Ground Fault
cg
Figure 38 —Zero-sequence polarizing voltage source
The time-overcurrent and instantaneous-overcurrent units used in directional overcurrent relay schemes are
virtually identical in operation and design to those used in non-directional overcurrent relay schemes,
except that the operation of one or both units is controlled or supervised by the directional unit.
Instantaneous-trip units, which themselves may or may not be directional, can be added to the scheme to
provide high-speed relay operation for close-in faults. Input currents to these relays are provided from CTs
located at the line terminal.
Negative-sequence relays can supplement the four basic overcurrent elements where needed. Three-phase
devices may sum the currents internally to produce negative-sequence and residual operating quantities
without the need for additional CT connections.
The procedure for coordinating directional overcurrent relays is similar to that used for coordinating
overcurrent relays. Fault coverage and/or operating times may be affected by network changes. The time
delay requirements often make them unsuitable for transmission line protection without using other protection
systems, such as transfer trip facilities. They are used, however, on lower voltage networks, especially for
ground-fault protection. The process of verifying coordination between the local relay and the relays at the
remote bus should take into consideration the instantaneous element applied for ground-fault protection of the
remote line. If the coordination between the protected line and the remote line is developed using the current
resulting from a fault just beyond the remote line instantaneous ground or distance relay, fault currents will be
somewhat lower at the local terminal, resulting in better coordination margins. In addition, if the remote bus
66
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
has additional sources, the effects of infeed from these sources improve coordination margin. The local relay
will reach less into the remote line as the current at the local terminal is lower.
Instantaneous directional ground overcurrent elements are often used in pilot scheme applications to
provide sensitive communications-assisted ground-fault protection. Phase-directional overcurrent relay
schemes are used primarily on distribution and subtransmission feeders when fault and/or load current can
flow in either direction. Directional relays are required at the terminal having the weaker source behind it,
usually the receiving end of a line. The pickup of the phase time-overcurrent elements has to be set higher
than the maximum load current expected to flow in the forward direction but may be set below the normal
load current in the reverse direction. Regardless of the particular method chosen, the pickup settings should
be as low as possible for fault detection sensitivity, but with sufficient margin above any non-fault-related
current flows. The instantaneous element pickup, time-current characteristic, and time-adjustment setting
requirements are similar to those of the non-directional overcurrent relays, with only faults in the forward
direction being considered. Directional ground overcurrent relays are commonly applied on all types of
transmission lines. The time-overcurrent elements are often used for backup protection. High-set
instantaneous ground directional elements are often used for direct tripping for close-in ground faults. The
topic of close-in faults is further discussed in 6.3.3.
Automatic reclosing is a special case of a system configuration change, as it represents a non-typical
operating scenario where one terminal of the line is closed while the other end is open, as shown in Figure
39. Instantaneous directional ground protection can cover a significant percentage of the line. A reclose of a
remote line onto a close-in fault (with its remote end open or closed) is often the external fault simulation
used to set the local terminal relay, as the loss of this line’s source will tend to force more ground current
through the terminal being set. A setting method for the local terminal relay that takes into consideration
the possible special configurations presented by reclosing and other typical maintenance outages would be
a solution to undesirable over-trips.
Bus A Bus B Ground Fault Bus C
to Set Relay
Reclose
Setting Open
Here
Relay Here
Ground
Sources?
Figure 39 —Reclosing
Removal of large remote ground sources during maintenance outages can have the same effect as that of
reclosing. The result is that more ground current will flow from the local terminal, thus impacting
overcurrent settings by possibly allowing overreach conditions. If the directional ground relay setting takes
into account the loss of the strongest remote source, then during normal operation, with all ground sources
in service, the relay’s reach will be shorter. Company practices vary, but, in general, a shorter reach is
preferred to that of possibly over-tripping when the source is removed.
Also, the grounding of a transmission line that is mutually coupled to the protected line for maintenance
activities can make a significant change to the network fault current distribution. The relay settings need to
account for this scenario, as the mutual coupling effect can significantly impact ground relay operation.
Power system modifications due to switching or maintenance can result in substantial changes to the
anticipated fault current flows. The switching duration can be brief and may not justify a complete settings
recalculation or the performing of a new coordination study immediately prior to the modification. The
effect of such single-contingency temporary changes to the power system can be included in the initial
settings calculations, with specific attention to possible overreaching of instantaneous elements.
A typical method employed for contingency analysis uses short-circuit analysis software that removes
network elements sequentially to analyze the effects of such outages. The choice of which network elements
67
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
are removed varies by the settings philosophy but should have the goal to identify the contingencies that have
significant impact. Frequently, loss of the network elements adjacent to the relay location will significantly
change ground fault currents, thus affecting the ground fault relays’ applications and settings.
Philosophy regarding the removal of significant zero-sequence current sources such as three-winding and
autotransformer banks with delta tertiary windings, as well as generator step-up transformers, can vary due
to the response such outages may initiate. Some utilities may consider the outage of these significant
elements to be an event that prompts the recalculation of nearby relay settings or the utilization of pre-
loaded alternate relay settings groups in the relays.
A 2014 PSRC report, “Transmission line applications of directional ground overcurrent relays” [B51], is a
helpful reference for applying directional ground relays to transmission lines.
6.2.4 Distance relay schemes
6.2.4.1 General
Distance relays operate by using voltage and current to determine if a fault is in the protection zone of the
relay. These relays are available for detecting phase faults as well as for detecting ground faults. The
characteristics of these relays can be shown on R-X diagrams. The values of the positive- and zero-
sequence impedances of the transmission line they protect are used to set these relays. The impedances of
two-terminal transmission lines are known parameters that are practically constant. The reach of these
relays is largely insensitive to network changes. However, on multi-terminal lines and transmission lines
with tapped lines, the apparent impedance is affected by network changes.
The term “impedance relay” is often used interchangeably with the term “distance relay,” although it is
only a convenient convention. Actually, there are several distance relay characteristics, of which the
impedance relay is only one. The basic distance relay characteristics are as follows:
a) Impedance: The impedance characteristic, shown in Figure 40(a), does not take into account the
phase angle between the voltage and the current applied to it. For this reason, the impedance
characteristic in the R-X plane is a circle with its center at the origin. The relay operates when the
measured impedance is less than the setting (i.e., it is within the circle). This unit, when used to
trip, should be supervised by a directional unit or be time delayed.
b) Mho: The characteristic of a self-polarized mho relay, shown in Figure 40(b), is a circle whose
circumference passes through the origin. The relay operates if the measured impedance falls within
the circle.
c) Offset mho: The characteristic of an offset mho relay in the R-X plane, shown in Figure 40(c), is a
circle that is shifted and includes the origin, thus providing better protection for close-in faults in the
forward as well as reverse directions. This unit, when used to trip, may be supervised by a directional
unit or may be time delayed if it is not intended for operating during faults in the reverse direction.
d) Reactance: This characteristic, shown in Figure 40(d), measures only the reactive component of
impedance. The characteristic of a reactance relay in the R-X plane is a straight line parallel to the R
axis. The reactance relay should be supervised by another function to ensure directionality and to
prevent tripping under load.
e) Quadrilateral: The quadrilateral characteristic has four sides, as shown in Figure 40(e). This
characteristic can be achieved by combining directional and reactance characteristics with two
resistive reach blinder characteristics.
f) Lenticular: The lenticular characteristic, shown in Figure 40(f), is similar to the mho relay, except
that it is lens-shaped rather than circular, thus reducing the sensitivity of the relay to load.
g) Polygon: The polygon characteristic, shown in Figure 41, is an extension of the quadrilateral
characteristic in which the characteristic can be tailored to suit the needs for special applications.
68
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
jX
| Restrain |     |     | jX  |     |
| -------- | --- | --- | --- | --- |
nZL
|     |     | Z   | nZL | Z1  |
| --- | --- | --- | --- | --- |
Maximum
|     |     | 1   |     | sensitivity |
| --- | --- | --- | --- | ----------- |
line
e
|     |     | Operate Maximum |     | at  |
| --- | --- | --------------- | --- | --- |
Sensitivity Angle r
p e Restrain
|     |     | δ   |     | O   |
| --- | --- | --- | --- | --- |
R
δ
Relay Location Directional
R
Relay Relay Location
Characteristic
Restrain
Mho Characteristic
| Z2 = -Z1 |     | Impedance |     |     |
| -------- | --- | --------- | --- | --- |
Characteristic

| —   |     | (a)  | (b)  |     |
| --- | --- | ---- | ---- | --- |
|     | jX  |      | jX   |     |
nZL
nZL Restrain
| Restrain |     | c e eristic |     |     |
| -------- | --- | ----------- | --- | --- |
ta n
Z1 a c t X1
|     | at e | Re ra c |     |         |
| --- | ---- | ------- | --- | ------- |
|     |      | h a     |     | Operate |
er C
p
O
|     |     | δ   | δ   |     |
| --- | --- | --- | --- | --- |
R
Relay Location R
Relay Location
Z2
Offset Mho
Characteristic

| —   |     | (c)  | (d)  |     |
| --- | --- | ---- | ---- | --- |
jX
X
|     | 1   | nZ  | jX  |     |
| --- | --- | --- | --- | --- |
L
1
Lenticular
|     | 2   | Characteristic |     |     |
| --- | --- | -------------- | --- | --- |
4
Restrain
e
at
|     |     | e r |     | e   |
| --- | --- | --- | --- | --- |
|     |     | p   |     | t   |
|     |     | O   |     | a   |
r
e
| Quadrilateral |     |     |     | p   |
| ------------- | --- | --- | --- | --- |
Restrain O
Characteristic
R R
Relay Location
Relay Location
3
Z
4
| —   |     | (e)  | (f)  |     |
| --- | --- | ---- | ---- | --- |
Figure 40 —Impedance, mho, offset mho, reactance, quadrilateral, and
lenticular characteristics implemented in distance relays
69
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
jX
nZ
L
Restrain
e
at
er
p
O
R
Relay
Location
Polygon
Characteristic
Figure 41 —Polygon characteristic implemented in distance relays
Numerous other distance relay characteristics have been designed by combining the basic impedance
characteristics described in this subclause. The response of the various characteristics is affected by the
polarizing signal used in them.
6.2.4.2 Step-distance schemes
Non-pilot application of distance relays is called step-distance protection. Several zones are set up to protect a
transmission line and provide backup protection of a remote bus (or buses) and some portions of the lines
emanating from the remote bus. The first zone, designated as zone 1, is normally set to trip with no intentional
time delay. To avoid unnecessary operation for faults beyond the remote terminal, zone 1 functions are
usually set for approximately 80% to 90% of the transmission line impedance. The intent of making the
setting less than the full line impedance setting is to prevent overreaching. This overreaching can be due to the
effect of load, fault impedance, fault contribution from the remote terminal, nonsymmetrical construction
where some fault loops are lower impedance, or errors in settings, calibrations, or instrument transformers.
The second zone, designated as zone 2, is set to protect the remainder of the line plus an adequate margin.
Zone 2 relays need to be time delayed to coordinate with relays at the remote bus. Typical time delays are in
the order of 15 cycles to 30 cycles of the fundamental frequency, although, depending on the application, they
may be set faster or slower. This time delay prevents instantaneous clearing of the local terminal for faults
beyond the remote terminal of the line. The reach setting of zone 2 may vary depending on the application. In
general, zone 2 settings should never overreach any zone 1 relay protecting other transmission lines emanating
from the remote terminal. If this overreach is unavoidable, coordination can be maintained by providing
additional time delay to the zone 2 that is overreaching, as shown in Figure 42. The minimum setting for
zone 2 that ensures full coverage of the line, with safety margin, is usually 120% of the line impedance. In
some cases, if there is no concern with reaching beyond the zone 1 elements at the remote terminal, the zone 2
elements may be set with a much higher margin. For example, in the case of short lines, settings as high as
200% of the line, or higher, may be helpful in increasing the dependability of the protection system.
Zone 3
Extended Zone 2 Time Zone 2
Normal Zone 2 Time Zone 2
Zone 1 Zone 1
Long Line Short Line Next Line
Figure 42 —Backup long line to short line
70
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Even though the transmission line is fully protected with zone 1 and zone 2 relays, a third forward-reaching
zone is often employed. This zone 3 is applied as remote backup for relay or station failures at the remote
terminal. This relay should be time delayed to coordinate with the zone 1 and zone 2 relays protecting other
lines emanating from the remote bus. Sometimes it is necessary to coordinate the zone 3 relay with
overcurrent relays protecting distribution load tapped from a transmission line. The relay should detect any
fault for which it is expected to provide backup and not limit the load-carrying capability of the line. The
setting of the zone 3 relay ideally will cover (with adequate margin and with consideration for infeed, if
required) the protected line, plus all of the longest line emanating from the remote station.
A possible problem with very long zone 3 (and sometimes zone 2) settings is that there may be insufficient
margin to ensure that the apparent impedance due to heavy load does not enter the operating characteristic of
the distance relay as described in a 2001 PSRC report, “Transmission line protective systems loadability”
[B52]. When considering the apparent impedance of the load, the maximum steady-state load is not always
the worst case to be considered. It is sometimes necessary to consider minimum apparent impedance due to
stable system swings, temporary line overloads, and heavy loads under reduced system voltage. If load
considerations or other problems prevent a sensitive enough setting, other forms of backup protection may be
applied, or some form of sequential tripping may be used. To employ sequential tripping, typically the remote
infeed source terminal would have protective relays set to trip and remove the infeed effect. With the infeed
removed, the zone 3 relay should then be applied to cover the longest remote line with adequate margin.
6.2.4.3 Zone 1 extension distance schemes
The zone 1 extension scheme requires no pilot channel and derives its name from the fact that the zone 1
functions are set to normally reach beyond the remote terminal of the transmission line. Simplified logic for
the scheme is as shown in Figure 43.
RO RU
|     |      | RU  |     |      | RO  |
| --- | ---- | --- | --- | ---- | --- |
|     | CB 1 |     |     | CB 2 |     |
Protected Line
|          | INITIATE  |       |       | INITIATE  |          |
| -------- | --------- | ----- | ----- | --------- | -------- |
|          | RECLOSE   |       |       | RECLOSE   |          |
|          | TRIP      |       |       | TRIP      |          |
|          | RO        | Timer | Timer |           | RO       |
| Circuit  |           |       |       |           | Circuit  |
| Breaker  |           | AND   | AND   |           | Breaker  |
| Reclosed | NOT       |       |       | NOT       | Reclosed |
|          |           | AND   | AND   |           |          |
|          | RU        |       |       |           | RU       |
RO = Overreaching Setting
RU = Underreaching Setting
Figure 43 —Extension of zone 1
The extension of the zone 1 is controlled by the output from an automatic reclosing relay that is an essential
part of this technique. No output is produced by automatic reclosing relay during normal operating
conditions, and the zone 1 setting reaches beyond the remote terminal of the transmission line.
High-speed tripping is initiated at both terminals of the line when a fault occurs within the overreaching zone
1 element. Outputs from the automatic reclosing relays at both terminals reduce the reach of zone 1 to values
similar to those used by step-distance schemes (see 6.2.4.2 for the usual reach of zone 1) and then reclose the
circuit breakers energizing the line. The line circuit breakers trip if the fault still persists and is in the zone 1
reach from both terminals. The protection now acts like the step-distance protection described in 6.2.4.2.
71
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
All lines adjacent to the fault are tripped for a fault that occurs beyond the remote terminal of a line but is within
the reach of the extended zone 1 setting of the line. However, this causes the settings of extended zone 1 to be
reduced to usual step-distance protection levels before the circuit breakers are reclosed. The fault (if it still exists)
is now beyond the pulled-back reach so that automatic reclosing restores to service all unfaulted lines. If the fault
is permanent and is located near a line terminal, the relay nearest to the fault will trip without time delay after a
reclosing attempt, and the relays at the remote terminals will trip after a time delay.
The scheme is dependable because it provides fast tripping for faults anywhere on the transmission line
without the use of a communications channel. It is insecure because it trips the line for all external faults
that are in the reach of the extended zone 1 setting. Note that all lines within reach of a common fault, and
using this type of scheme, will be tripped simultaneously for that fault. However, due to the infeed effect,
the overreach of the extended zone 1 is greatly reduced and typically extends along a small percentage of
the line out of the remote station such that close-in faults are usually the only ones at risk for over-tripping.
Given that infeed can contribute to the security of the scheme, it is typically applied on tightly networked
systems (i.e., networks with many interconnecting transmission lines).
6.2.4.4 Relay elements in step-distance schemes
The distance from the relay location to a line fault can be determined by measuring positive-sequence
impedance of the line from the relay location to the fault. The distance measurement is consistent because
the positive-sequence impedance per unit length of a homogenous line is constant. The distance to the fault
can also be determined by measuring the zero-sequence impedance of the line when a ground fault occurs,
but, unfortunately, the zero-sequence impedance per unit length of a line is not constant because the
moisture in the ground all along the line may not be the same and/or the geological formation of the ground
may not be same all along the line. Therefore, it is preferable to measure the positive-sequence impedance
of the line from the relay location to the fault.
Three relay elements are needed for detecting multiphase faults in each zone if electromechanical or solid-
state devices are used. The voltages and currents applied to the elements are listed in Table 5. Similarly,
three relay elements are needed for detecting single-phase-to-ground faults in each zone. The voltages and
currents applied to these elements are listed in Table 6.
Table 5 —Voltages and currents applied to distance relays for detecting multiphase faults
| Relay element  |     | Type of fault        |     | Voltage applied  |     | Current applied  |
| -------------- | --- | -------------------- | --- | ---------------- | --- | ---------------- |
|                |     | Phase A and phase B  |     | V A  − V         | B   | I A  − I B       |
1
|     |     | Phase A, phase B, and ground  |     | V  − V   |     | I  − I       |
| --- | --- | ----------------------------- | --- | -------- | --- | ------------ |
|     |     |                               |     | A        | B   | A B          |
|     |     | Phase B and phase C           |     | V  − V   |     | I  − I       |
| 2   |     |                               |     | B        | C   | B C          |
|     |     | Phase B, phase C, and ground  |     | V  − V   |     | I  − I       |
|     |     |                               |     | B        | C   | B C          |
|     |     | Phase C and phase A           |     | V  − V   |     | I  − I       |
| 3   |     |                               |     | C        | A   | C A          |
|     |     | Phase C, phase A, and ground  |     | V C  − V | A   | I C  − I A   |
Table 6 —Voltages and current applied to distance relays for detecting phase-ground faults
| Relay element                             |     | Type of fault      | Voltage applied  |     | Current applied  |          |
| ----------------------------------------- | --- | ------------------ | ---------------- | --- | ---------------- | -------- |
|                                           | 1   | Phase A to ground  |                  | V   | I                |  + 3I k  |
|                                           |     |                    |                  | A   | A                | 0        |
|                                           | 2   | Phase B to ground  |                  | V   | I                |  + 3I k  |
|                                           |     |                    |                  | B   | B                | 0        |
|                                           | 3   | Phase C to ground  |                  | V   | I                |  + 3I k  |
|                                           |     |                    |                  | C   | C                | 0        |
| The constant k in Table 6 is the ratio (Z |     |  − Z )/3Z          | .                |     |                  |          |
|                                           |     | 0 1 1              |                  |     |                  |          |
NOTE—Other operating principles, such as compensator relaying to detect  multiphase faults are discussed in
Protective Relaying Theory and Applications [B26]. Also, schemes with one compensator relay and one ground
directional overcurrent relay have been used to detect all types of faults on transmission lines.6

6 Notes in text, tables, and figures of a standard are given for information only and do not contain requirements needed to implement
this standard.
72
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.3 Pilot schemes
6.3.1 General
Pilot schemes use communication channels to send information from the local relay terminal to the remote
relay terminal. This information is used to achieve high-speed tripping for faults occurring on 100% of the
protected line. Both current differential schemes and directional comparison schemes are common. Current
differential systems transmit to and receive from the remote terminal(s) information on the current that can
be used to determine magnitudes and phase angles. The systems that exchange current phase angles or their
deviations are called phase-comparison systems. Current-differential and phase-comparison protection
schemes include both ac pilot-wire relays and digital current differential relays. Distance relays are also
arranged in pilot schemes using a communication channel to transmit binary information.
6.3.2 Current differential schemes
A basic current differential scheme is shown in Figure 44. Information from the relay at the remote
terminal is provided to the local relay using a communications channel. This information is compared with
the corresponding information collected by the local relay. When there is no fault on the line, the difference
between the two sets of information should be zero or equal to the tapped loads on the line. In practice, this
may not be the case due to CT errors, ratio mismatch, and line-charging currents.
Terminal 1 Transmission line Terminal 2
I I I
A1 F A2
Protection system 1 Communication Link Protection system 2
I + I = 0; no fault on the line
A1 A2
I + I ≠ 0 ( = I ); fault on the line
A1 A2 F
Figure 44 —Current differential protection of a transmission line
Information concerning both the phase and the magnitude of the currents at each terminal are needed at all
terminals for comparing the magnitude and phase angles and performing differential measurements. A
current differential scheme, therefore, requires a communication channel suitable for the transmission of
this data. A current differential scheme can operate for internal faults even for zero infeed at one or more of
the terminals provided the total current is greater than the sensitivity of the differential protection system.
There are two main types of current differential systems. The first type combines the currents at each terminal
into a composite signal and compares these composite signals through a communication channel to determine
if there is a fault in the line being protected. An example of this type of system is the ac pilot wire protection
scheme described in 6.3.3. The second type samples individual phase currents at each terminal, converts the
samples to a digital signal, and transmits these signals between terminals to determine if a fault is present on
the line. The second type of differential system, referred to as phase-segregated line differential relays,
includes most digital current differential relays. Specific measuring principles used in digital current
differential protection schemes include percentage differential, charge comparison, and alpha plane principles.
Detailed descriptions of these operating principles are available in IEEE Std C37.243 [B70].
73
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Current differential schemes tend to be more sensitive than distance-type schemes because they respond
only to the currents in the protected line. However, either tapped loads on the line must be included as
specific currents summed in the differential scheme or the relay current trip setting must be desensitized to
compensate for any tapped loads that are not included in the current summation. Because current-only
schemes require no potential to operate, they are not affected by system swing conditions or any problems
introduced via the potential inputs, such as the failure of a voltage-transformer fuse. On the other hand,
these schemes have no inherent remote backup capabilities.
The integrity of the communication channel is very important to the operation of current differential
schemes. For this reason, the communication channel should be highly reliable. Because the trip logic in
current differential schemes generally does not rely on permissive or blocking elements, channel
communications losses may cause misoperations; therefore, current differential protection schemes employ
communications channel supervision to block potential misoperations from loss of communications.
The advantages of current differential schemes are summarized as follows:
 No VTs needed
 Good for multi-ended lines
 Can detect high resistance faults
 Immune to power swings, current reversals, and high load flows
 Uniform trip time for all line faults without misoperation due to overreach
 No problems with series compensation
 Simple to set with no coordination problems
A summary of the disadvantages of current differential schemes includes the following:
 No inherent remote backup capability
 Trip current setting may need to be desensitized to account for tapped line load
 Cost and complexity of communications channel having suitable requirements for the scheme
 Trip output must be disabled for loss of communications
Current differential schemes need a communication channel for exchanging information, such as power system
frequency signals, audio tones, or digital and binary data, such as a transfer trip. Communications media can be
metallic pilot wires, dedicated fiber optic links, T1(E1)/SONET (Synchronous Digital Hierarchy)
communications networks, or Ethernet networks. Some digital current differential schemes have been operated
on audio tones over leased telephone lines or digital microwave. Power-line carrier channels are generally not
used for current differential relaying because either they do not have the bandwidth required by these schemes or
there are other technical limitations of power-line carrier that makes it unsuitable for the particular application.
6.3.3 AC pilot-wire relays
Traditional pilot-wire relays use a pair of metallic wires as the medium for sending information from one
terminal to the other. The communication is in the form of signals at power-system frequency. Pilot-wire
relays that are used traditionally on short lines are easy to apply. The traditional electromechanical pilot-wire
relays are one of two basic types, circulating-current types and opposed-voltage types, such as those shown in
Figure 45 and Figure 46, respectively. More details of these schemes are given in many references, such as
Protective Relaying Theory and Applications [B26] and Neher and McConnell [B89]. Both schemes use
mixing networks to convert the currents in the three phases and the residual current to a single quantity so as
to transmit the composite information on two pilot wires. It is necessary to take care to protect against the
dangers associated with ground potential rise.
74
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Some users have converted pilot-wire communication links to optical fiber links in conjunction with fiber
optic interfaces. This avoids the problems of ground potential rise and induced voltages.
| Terminal A |     |     |     | Terminal B |
| ---------- | --- | --- | --- | ---------- |
Transmission line
| Mixing transformer |     | Full-wave rectifiers | Mixing transformer |     |
| ------------------ | --- | -------------------- | ------------------ | --- |
Pilot wire
|             | R   |              | R   |             |
| ----------- | --- | ------------ | --- | ----------- |
|             | O   |              | O   |             |
| Saturating  |     | Insulating   |     | Saturating  |
| transformer |     | transformers |     | transformer |
R = Restraining coil
O = Operating coil
Figure 45 —Schematic connections of a circulating-current pilot-wire scheme
Protected line
| Mixing transformer |     |     |     | Mixing transformer |
| ------------------ | --- | --- | --- | ------------------ |
Pilot wire
| P           | R   |              | R   | P           |
| ----------- | --- | ------------ | --- | ----------- |
|             | O   | O            |     |             |
| Input       |     | Insulating   |     | Input       |
| transformer |     | transformers |     | transformer |
R = Restraining coil
O = Operating coil
P = Polarizing coil
Figure 46 —Schematic connections of an opposed-voltage pilot-wire scheme
75
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.3.4 Phase-comparison schemes
6.3.4.1 General
The phase-comparison technique compares the phase angle of the currents at the two terminals of the
protected line. The CTs and relays are connected as shown in Figure 47. The currents in the relays at the two
terminals are essentially equal and 180° out of phase when an external fault occurs on the power system; the
relays interpret this situation as an external fault and do not initiate a trip. On the other hand, the currents are
essentially in phase if a fault is on the protected line; the relays interpret the phase coincidence as a fault on
the line and initiate the tripping of the circuit breakers controlling the line. A secure communication channel
between the two line terminals is needed for this protection scheme to perform its intended function. This
channel could be over a medium such as power-line carrier, metallic pair, leased telephone lines, microwave,
or fiber optics. Communication lines with automatic change-in-path delays due to route switching may result
in reduction of relay security. Utilities can have control of the route switching of communication lines they
own but are not likely to have control of route switching of leased communication lines.
R R
CB A CB B
F1 F2 F3
INTERNAL FAULT, F2
EXTERNAL
FAULTS, F1 & F3
FAULT CURRENT AT A FAULT CURRENT AT B
Figure 47 —Phase-comparison relaying
Phase-comparison systems need inputs from the CTs associated with the line terminals. A composite
sequence-current filter network provides a single-phase voltage output proportional to positive-, negative-,
and zero-sequence currents in the line except for the segregated phase-comparison systems. The relay
converts the single-phase voltage output to a square wave (local square wave) during a fault condition and
keys the channel to the remote terminal for comparison of the local single-phase voltage output with the
received signal (remote square wave). Relay logic delays the local square wave by the duration equal to the
channel time to provide a reasonably accurate comparison.
Phase-comparison logic can be configured as either blocking or permissive. Unblocking phase comparison,
which is a special type of permissive scheme, is generally used if power-line carrier is the communication
medium.
6.3.4.2 Single phase comparison
A positive half-cycle of the local square wave is compared with a corresponding positive half-cycle of the
square waves received from the remote terminal by single phase-comparison schemes; this comparison is
performed by the relays at both terminals of the line. Single phase-comparison can be configured either in a
blocking mode or in a permissive mode.
76
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
A single phase-comparison system requires two fault detectors, one for keying the carrier on-off and the
other for tripping, when the scheme is configured in a blocking mode. The carrier start is set more
sensitively than the tripping unit. There is a possibility of tripping delay of one half-cycle because the
comparison of only positive half-cycles is performed. The remote signal is received and the comparison
blocks trip if a fault is beyond the remote terminal. A trip is initiated at a terminal if no signal is received
from the remote terminal. The consequence is that the phase comparison blocking system produces a trip
output if a fault on the protected line causes failure of the communication channel.
A single phase comparison requires one fault detector, a pilot channel, and breaker status logic (or a low-set
current detector) when configured in permissive mode. The sequence current fault detector allows the local
square wave to key the channel on and off at 60 Hz during a fault. A trip condition is satisfied when the
local and remote received square waves are essentially in phase. An open line terminal will cause a
constant permissive signal to be sent, thus allowing the closed end to trip for a faulted line. This form of
phase comparison is very secure in that a loss of channel does not result in tripping the line. A dependable
channel, such as direct on-baseband analog microwave, should be used.
6.3.4.3 Dual phase comparison
The logic of a dual phase-comparison system that requires a duplex channel for communication is shown in
Figure 48. This logic performs the comparison, like the single phase-comparison system, during both half-
cycles of the power system sine wave. This provides statistically faster tripping times than the single phase-
comparison systems provide. Dual phase-comparison systems use frequency-shift channel equipment for
transmitting signals continuously. Therefore, carrier start equipment is not needed.
Local Pos.
AND
Remote Pos.
TIMER
OR LOGIC Trip
CIRCUIT
Local Neg.
AND
Remote Neg.
Figure 48 —Dual phase-comparison logic
A dual phase-comparison system keys the carrier to its “mark” frequency when the local square wave goes
positive and keys to its “space” frequency when the square wave is negative. Comparison of the local
square wave to the received frequency from the remote terminal of the line indicates if the fault is on the
protected line or is external to the protected line. Relay logic allows delaying the local square wave by
duration equal to the channel time, as is done in single phase-comparison systems. When a power-line
carrier is used for communication, the communication signal may be lost during an internal fault. For this
reason, an unblocking version of the permissive scheme should be applied (more discussion of unblocking
versions is provided in 6.3.5.7).
6.3.4.4 Segregated phase comparison
Segregated phase-comparison systems work in a manner similar to the systems described in 6.3.4.2 and
6.3.4.3 except that the composite sequence-current filter network is eliminated. Square wave
representations of phase currents are transmitted to the remote end, where they are compared to the locally
generated square waves for coincidence. The comparison is done on each half-cycle. A decision is made to
trip the line if the waves are coincident for more than 4 ms.
An internal fault may not cause the line current at a terminal that is connected to a weak source to reverse
direction during a line fault, especially if the other terminal is connected to a strong source. A phase-
77
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
comparison scheme that looks at phase relationships of currents only would not detect a fault because phase
of the current at the terminal connected to a weak source did not reverse.
An offset keying scheme in which the width of the waveform is a function of the magnitude of the current
at the line terminal can take care of this problem. The trip decision is still based on the coincidence of the
local and remote square waves. Because magnitude information is present in the system, the relay responds
properly to outfeed conditions. Since the information on currents in the phases is kept separately, this
system can incorporate single-phase tripping schemes.
6.3.5 Directional comparison schemes
6.3.5.1 General
Directional comparison schemes use directional phase overcurrent relays, directional ground overcurrent
relays, and distance relay functions that have inherent directional properties. The following issues are
important when setting such relays for use in directional comparison schemes.
The main consideration in setting the overreaching (RO in figures) directional ground overcurrent function
is that it should not operate due to normal steady-state unbalances. Overreaching ground overcurrent relays
may be set quite sensitively so that they operate for faults remote from the protected line because steady-
state unbalances are usually quite small. The correct operation of the overreaching ground overcurrent
protection relies on pilot logic for preventing operation during external faults.
Zone 2 relays are usually set to overreach the remote terminal of the protected line with at least the same
margin as the margin used in the case of step-distance schemes. However, there is no concern for
coordination with relays at the remote terminal protecting other equipment. The zone 2 relay in a pilot
scheme may be set to overreach the line with greater margin than is set in step-distance schemes if it does
not also trip directly through a timer. There is no need to consider step time coordination with other
protection systems, because pilot-assisted zone 2 relays do not trip for faults in adjacent equipment. If there
is no concern for operating on load, zone 2 relays in pilot-assisted schemes that are set to overreach with
large margins may provide faster tripping than similar schemes in which a minimum margin is used but
may also be more susceptible to misoperation on stable swings. The use of a minimum margin, however,
reduces the possibility of a false trip in the case of failure to receive the blocking signal.
Directional comparison schemes may have to accommodate current reversals that accompany sequential
tripping of circuit breakers for faults on one of the parallel lines. This typically applies to ground
directional overcurrent elements but can also occur if zone 2 is set too long. See 6.3.5.10 for more details
on current-reversal guard logic.
Some pilot schemes use reverse-looking elements; these elements should be set to “see” farther than the
forward-looking overreaching function at the remote terminal. The positive sensitivity margin is required
for forward and reverse overcurrent elements in a pilot scheme, because the line impedance does not affect
the relative magnitude of current in each terminal for an external fault. This setting ensures that the reverse-
looking blocking function will always work if required to prevent undesired tripping of the forward-looking
function. The reverse-looking distance relay element setting should include adequate margin to ensure that
it actually “sees” farther than the remote forward-looking relay. For three-terminal lines, where fault
current may flow out of two terminals for an external fault, this division of fault current should be
considered in setting the reverse-looking relay elements to ensure a positive sensitivity margin.
In all cases, the speed and characteristics of reverse-looking elements should be checked to ensure that they
are at least as fast and sensitive as the forward-looking elements provided at the remote terminals. This
check should include verifying pickup levels (i.e., the reverse element should be set to pick up at a lower
value than the remote forward-reaching element) and directional polarization methods. It is very important
that the directional element be polarized using the same technique; for example, zero-sequence or negative-
sequence or current polarizations at both line terminals. The selection of the directional polarization method
78
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
can be an issue in relays that automatically select the directional polarization based upon measured
quantities. Slight differences in the measured values at the line terminals can result in the automatic
selection of different directional polarization methods at each line terminal. Therefore, it may be best to
select a single directional polarization method in some applications.
6.3.5.2 Direct underreaching transfer trip
The simplified logic for a DUTT scheme is shown in Figure 49. This scheme requires underreaching (RU
in figures) functions only and is usually applied with a frequency shift keying (FSK) channel. With this
type of channel, the guard frequency is transmitted during quiescent conditions, and the transmitter is keyed
to the TRIP frequency whenever one of the underreaching functions operates. Phase distance elements are
used almost exclusively for the detection of multiphase faults, whereas ground distance or directional
ground overcurrent elements are used for the detection of ground faults. The underreaching functions
should overlap in reach; otherwise, there would be a dead zone on the line where no faults would be
detected.
RU
RU
CB 1 Protected Line CB 2
TRIP TRIP
CB 1 CB 2
RU RU
OR OR
RCVR RCVR
XMTR XMTR
RU – underreaching trip function, must be set to reach short of remote terminal
and must overlap in reach with RU at remote terminal.
Figure 49 —Direct underreaching transfer trip
For ground elements, changes in the power system can result in reduced fault current contributions from the line
terminal, which causes a reduction in the effective reach of the directional ground overcurrent elements.
Consequently, it may not be possible to use directional ground overcurrent elements that meet the required reach.
For internal faults within the overlap zone, the underreaching functions at each end of the line will operate
and trip the breaker directly. At the same time, the underreaching function will key its respective
transmitter to send a direct transfer TRIP signal to the remote terminal of the line. Receipt of the TRIP
signal will also initiate tripping of the breaker. The scheme operates at high speed for close-in faults.
However, it does not operate for faults beyond the reach of the underreaching elements if the remote circuit
breaker is open or if the remote communication channel is inoperative. For this reason, DUTT schemes are
often used only as a supplement to other pilot-tripping schemes.
The DUTT received signal is converted to a trip without any local supervision. As such, its channel
requires more security than those schemes whose channels are supervised by a local measuring element.
79
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Security of the protection system may be jeopardized if only one communication channel is used at each
terminal because an erroneous output from the channel would initiate an instantaneous trip. Therefore, this
scheme is often applied with dual channels where both outputs should initiate trip to provide security.
Security can be further enhanced by requiring that one channel shifts up in frequency, while the other
channel shifts down in frequency to initiate a trip. Time-delayed backup tripping functions are added to trip
the line for faults beyond the reach of the underreaching functions when the remote circuit breaker is open.
The channel can be monitored on a continuous basis because the GUARD signal is transmitted
continuously. The consequence is that the channel check-back equipment is not required.
6.3.5.3 Permissive underreaching transfer trip
The permissive underreaching transfer trip (PUTT) scheme requires both overreaching (RO) and
underreaching (RU) functions. Simplified logic for the PUTT scheme is shown in Figure 50. Consider that
the underreaching functions at both terminals are set to reach 80% of the line and the overreaching
functions are set to reach well beyond the remote terminals. The RU units at both terminals would operate
if a fault occurs on the middle 60% of the line and circuit breakers at both terminals are tripped. The RU
unit at bus 1 does not operate if a fault is on the protected line but is beyond the reach of that RU unit. The
RO unit at bus 1 operates indicating that the fault is either on the protected line beyond the reach of the RU
unit or on a line emanating from the remote terminal. The RU unit provided at bus 2 detects the line fault
and transmits this information to the protection system at bus 1. The circuit breaker tripping is then
permitted.
RU
RO
RU
RO
CB 1 Protected Line CB 2
TRIP TRIP
CB 1 CB 2
RU RU
OR OR
XMTR XMTR
RO RO
AND AND
RCVR RCVR
RU – underreaching trip function, must be set to reach short of remote terminal and must
overlap in reach with RU at remote terminal.
RO – overreaching trip function, must be set to reach beyond remote end of line.
Figure 50 —Permissive underreaching transfer trip scheme
This scheme is similar to the DUTT scheme, except that the signal sent is a permissive signal and tripping
at each terminal is supervised by the RO units. A PUTT scheme is ineffective for faults beyond the RU
function’s reach near the open terminal when the remote breaker is open.
80
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.3.5.4 Permissive overreaching transfer trip
The POTT scheme requires overreaching functions. Phase distance functions are used almost exclusively
for the detection of multiphase faults, whereas ground distance functions or directional overcurrent
functions responding to ground faults, including zero- and negative-sequence elements, are used for the
detection of ground faults. The POTT scheme is sometimes applied with an FSK channel, in which the
GUARD frequency is sent in standby and TRIP frequency by an output from the overreaching functions.
Simplified logic for the POTT scheme is shown in Figure 51.
RO
RO
CB 1 Protected Line CB 2
TRIP TRIP
CB 1 CB 2
RO RO
AND AND
RCVR RCVR
XMTR XMTR
RO – overreaching trip function, must be set to reach beyond remote end terminal.
Figure 51 —Permissive overreaching transfer trip scheme
Detailed discussions of channel type use (FSK), single and dual frequency applications, the role of the
guard signal, and responses to loss of guard are given in IEEE Std C37.93™ [B57].
For a fault anywhere on the protected line shown in Figure 51, both overreaching functions at both
terminals of the line operate and provide an input to the AND gate. At the same time, the overreaching
functions key the transmitter to the TRIP signal. Receipt of the TRIP frequency at each terminal and an
output from the overreaching function will cause the AND gate to produce an output to initiate tripping.
For external faults, the overreaching function at only one end of the line operates and there is no output
from the AND gates; thus, tripping is not initiated at either terminal.
The scheme is very secure in that it does not trip for any external fault if the channel is inoperative.
Conversely, the scheme lacks dependability because it does not trip the line for an internal fault if the
channel is inoperative. The scheme may not trip at high speed for close-in faults at the terminals connected
to strong sources because the fastest tripping time that can be expected depends on the slowest function for
an internal fault. Some means should be used to key the transmitter at an open breaker if tripping is to be
initiated for faults seen at the other terminals. Breaker 52b keying is commonly used to provide this
requirement. Breaker 52b keying is inherently delayed one to two cycles to prevent a line from tripping for
a relay operation at the remote breaker for an external line or bus fault. Alternatively, open breaker echo or
weak feed echo functions, as described in 6.3.5.8, can be applied.
Distance elements protect the line in the event of failure of communication between the terminals. These
elements are set to trip after a time delay so as to coordinate with the protection systems provided on the
lines emanating from the remote terminal.
81
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.3.5.5 Zone acceleration
Simplified logic for the zone acceleration scheme is shown in Figure 52. This scheme requires the use of
RU functions that have the capability of changing their reach when a permissive signal is received from the
remote terminal of the line. The RU functions are set to overlap in reach to avoid a dead spot on the line.
This generally requires the use of ground distance functions for the detection of ground faults and phase
distance functions for detecting multiphase faults. The scheme is usually applied with an FSK channel. The
channel is operated at the GUARD frequency during quiescent conditions and is keyed to the TRIP
frequency by operation of any of the RU functions.
RU
RU
CB 1 Protected Line CB 2
TRIP TRIP
CB 1 CB 2
RU RU
Extended Reach of RU Extended Reach of RU
RCVR RCVR
XMTR XMTR
RU – underreaching trip function, must be set to reach short of remote terminal
and must overlap in reach with RU at remote terminal.
It must be capable of being switched in reach.
Figure 52 —Zone acceleration scheme
Tripping is initiated and the channel is keyed to the TRIP frequency when a fault occurs within the overlap
zone of the underreaching functions. Receipt of the TRIP frequency extends (accelerates) the reach of the
underreaching functions to a value greater than the line impedance. This extension in reach has no further
effect because tripping has already been initiated at both terminals of the line. The underreaching function at a
terminal operates and trips the circuit breaker controlling the line at that terminal if the fault is close to the
terminal and keys its transmitter to the TRIP frequency. Receipt of the TRIP frequency at the other terminal
extends the reach of its underreaching function that now detects the fault and initiates tripping. None of the
underreaching functions operate for external faults; therefore, tripping is not attempted at any terminal.
This scheme is very secure because it does not trip the line for external faults regardless of the state of the
channel. Conversely, it does not trip the line for end-zone faults if the channel is inoperative. Time-delayed
backup should be relied on to trip for this condition. High-speed tripping for close-in faults is provided at
the terminals connected to strong sources. Tripping for end-zone faults depends on the operation of the
remote underreaching function; it is then delayed by the channel operating time, propagation time, and
operating time of the extended underreaching function. Because the GUARD signal is transmitted
continuously, the channel can be monitored on a continuous basis.
82
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.3.5.6 Directional comparison blocking
Simplified logic for a DCB scheme is shown in Figure 53. This scheme requires overreaching tripping
functions (RO) and blocking functions (B in the figure). Distance functions are used almost exclusively for
detecting multiphase faults. Either ground distance functions or ground directional overcurrent functions
are used for detecting ground faults. An OFF-ON communications channel is typically used with this type
of scheme. The transmission line is used often as the communications medium. Audio tone over leased
phone lines, microwaves, and fiber optic media are also used sometimes. The transmitter is normally in the
OFF state when the transmission line is functioning normally but is keyed to the ON state by the operation
of a blocking function. Receipt of a signal from the remote terminal applies the NOT input to the
comparator to BLOCK it from producing an output.
RO B
B RO
CB 1 Protected Line CB 2
TRIP TRIP
CB 1 CB 2
TL1 TL1
RO C C RO
AND AND
O O
RCVR RCVR
B XMTR XMTR B
RO – overreaching trip function, must be set to reach beyond remote end of line.
B – blocking function, must be set to reach beyond overreaching trip function at remote end of line.
C – coordination time, required to allow time for blocking signal to be received
(set equal to channel time plus propagation time plus margin).
Figure 53 —Directional comparison blocking scheme
The tripping functions are set to reach beyond the remote terminal of the transmission line with sufficient
margin so that they detect faults anywhere on the transmission line. The blocking functions are used to
detect faults that are not on the protected line but that the remote tripping functions are capable of
detecting. Therefore, the blocking functions are set to reach further behind the terminal than the tripping
function at the remote terminal reaches.
A blocking function operates and keys its transmitter to send a blocking signal to the remote terminal if there
is a fault on the bus side of the relay. Receipt of the blocking signal from the remote terminal applied to the
AND gate produces a low output from the AND gate; therefore, the circuit breaker is restrained from tripping.
A coordinating timer (TL1 in the figure) is required to allow time for a blocking signal to be received from the
remote terminal. It is set to compensate for channel time, signal propagation time, and for any difference in
operating time that might result if the remote blocking function is slower than the local tripping function.
One or more tripping functions operate when there is a fault on the transmission line. The outputs of the
carrier tripping functions, which could be any of the forward pilot elements, are applied to the AND gate.
The blocking functions do not operate because the fault is inside the protection zone and no transmitter is
keyed. The AND gates at both terminals now produce outputs that allow the TL1 at each terminal to time
out and then initiate tripping.
The coordination problems between the blocking function at one terminal and the tripping function at the
remote terminal is reduced if both functions operate on the same principle ensuring that the blocking function
83
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
is at least as fast and sensitive as, or faster and more sensitive than, the tripping function that is further away
from the fault. Some DCB schemes use a non-directional element to start the carrier block signal, particularly
for ground faults, and then use a forward-directional element to stop (or squelch) the carrier block signal. This
allows faster tripping by setting timer TL1 shorter because non-directional elements are usually faster than
directional elements. Tucker et al. [B102] discuss issues applicable when using dissimilar relays.
This scheme is very dependable because it operates for faults anywhere on the protected line even if the
communication channel is out of service, but it lacks security because it overreaches and trips for fault
beyond the remote terminal if the communication channel is not working. This scheme does not require
breaker 52b switch keying, or any other means of switch keying, when the remote breaker is open to permit
tripping for faults anywhere on the line. It provides high-speed tripping (dependent on coordinating time
delay) for most source and line conditions. However, it may not trip the terminals of the transmission line
connected to a weak source if the fault levels are below the sensitivity of the tripping relays. Because a
communication channel is required to be keyed only during external faults, there is no way to monitor the
channel continuously. Therefore, a channel check-back system is used if it is desired to check the channel
on a periodic basis. The overreaching functions can be used to drive timers so that time-delayed backup
tripping can be provided for faults within reach of the overreaching functions.
6.3.5.7 Directional comparison unblocking
When a power-line carrier is used as the communication medium with a permissive overreaching
directional comparison scheme, the possibility exists that the carrier signal may be attenuated or may not be
received as a result of a fault on the line. If this occurs, tripping is not permitted because the permissive
signal has not been received. To overcome this possibility, unblocking logic can be provided in the
receiver. When the signal is lost, the unblocking logic will produce a permissive signal from the receiver
that will last for a short period of time (typically 150 ms to 300 ms).
If the signal loss is due to a fault, at least one of the overreaching permissive trip functions will be picked
up. Thus, tripping will be initiated when the unblocking output is produced. If none of the permissive trip
functions are picked up, the channel locks itself out 150 ms to 300 ms after the signal is lost and will stay
locked until the GUARD signal returns for a preset amount of time.
6.3.5.8 Hybrid schemes (with echo logic)
The directional comparison hybrid permissive schemes use both tripping and blocking functions. Phase
distance functions are used almost exclusively for detecting multiphase faults. Ground distance functions or
directional ground overcurrent functions are used for detecting ground faults. The communication channel
is keyed by the overreaching functions or by the receipt of a permissive signal from the remote terminal,
with no concurrent output of the blocking functions (B in the figure) at the local terminal. The latter method
of keying is referred to as “channel repeat” or “echo” keying. Simplified logic for the hybrid scheme is
shown in Figure 54. See 6.3.5.9 for more detailed discussion of echo logic.
For an internal fault that is detected by the overreaching functions at each terminal of the line, the scheme
works just like a POTT scheme described in 6.3.5.4 or DCUB scheme described in 6.3.5.7. The
overreaching functions key their respective transmitters and initiate tripping when the permissive signal is
received from the remote terminal.
This scheme, unlike the normal permissive scheme, initiates a trip when only one terminal detects the fault. This
is done by using the echo circuit. For example, consider a fault on the line that is detected by the overreaching
function at terminal 1 only (breaker 2 might be open, or the source at terminal 2 might be very weak; details on
tripping at this weak infeed terminal are discussed in 6.3.5.9. The overreaching functions at terminal 1 detect the
fault and send a permissive signal to terminal 2; the transmitter is keyed by the receipt of the permissive signal.
The hybrid permissive scheme, in this respect, works in a similar manner as a blocking scheme.
84
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
RO
B
| B   |     |     | RO  |
| --- | --- | --- | --- |
Protected Line
CB 1 CB 2
TRIP TRIP
CB 1 CB 2
|     | TL1 | TL1 |     |
| --- | --- | --- | --- |
| RO  | C   | C   | RO  |
AND AND
|     | 0   | 0   |     |
| --- | --- | --- | --- |
RCVR RCVR
|       | OR XMTR XMTR | OR  |     |
| ----- | ------------ | --- | --- |
| B AND |              | AND | B   |
RO – overreaching trip functions, must be set to reach beyond remote end of line.
B – blocking functions, must be set to reach beyond overreaching trip functions at remote end of line.

Figure 54 —Hybrid permissive scheme (with echo logic)
One or more of the overreaching functions operate and key the respective transmitter to the permissive
frequency for an external fault. Receipt of the permissive signal does not cause tripping at the remaining
terminals because the overreaching functions at those terminals do not operate. The received permissive
signal is not repeated because one or more of the blocking functions operated to block the repeat.
6.3.5.9 Weak infeed and echo logic used in hybrid permissive schemes
The logic shown in Figure 55 illustrates one method for initiating tripping at a terminal of the transmission
line  connected  to  a  weak  or  open  source.  The  logic  shown  outside  the  dashed  box  represents  the
conventional logic used in POTT and DCUB schemes. The logic shown inside the dashed box represents
the supplemental weak infeed tripping and echo keying logic. Weak infeed tripping logic requires echo
keying logic to echo a permissive TRIP back to the strong source terminal and reverse blocking elements to
block echo for an external fault.
21 (forward)
| OR 1 |     |     | KEY |
| ---- | --- | --- | --- |
67 (forward)
| Permissive Trip |     | AND 1 | TRIP |
| --------------- | --- | ----- | ---- |
Receive
X ECHO
| 21 (reverse) | AND 2 |     |     |
| ------------ | ----- | --- | --- |
| OR 2         |       | Y   | KEY |
67 (reverse)
TL WEAK
| 27L  |     | AND 3 | INFEED |
| ---- | --- | ----- | ------ |
| OR 3 |     | 0     | TRIP   |
59N or 50N

Figure 55 —Weak infeed and echo key logic
85
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Echo keying logic can be used independent of the weak infeed tripping logic. For example, echo keying
logic may be used at either line terminal as an alternative to 52b open-breaker keying; or it may be used at a
weak infeed source terminal simply to speed tripping at the strong source terminal, where sequential
tripping would occur at the weak terminal after the strong source is removed. The weak infeed terminal
source, as the term implies, is too weak to supply sufficient fault current to operate conventional-distance
or directional overcurrent relay elements for faults on the protected line. The remote line terminal is
assumed to have a sufficiently strong source to operate conventional relays. Successful sequential tripping
requires that the weak infeed terminal source should become sufficiently strong to permit conventional
relays to operate after the circuit breaker at the strong source terminal has tripped. If the weak source
remains too weak to operate conventional relays, then either direct-transfer tripping is required from the
strong source terminal, or weak infeed logic is needed at the weak source terminal.
The weak infeed logic varies with the relay and the manufacturer of the relay. One variation of weak infeed
logic is described in this subclause. This logic requires additional relay elements at the weak source
terminal to supplement the conventional forward-reaching distance and directional overcurrent relay
elements. A phase undervoltage relay (27L), a residual overvoltage relay (59N), or a sensitive residual
overcurrent relay (50N) is required to detect the occurrence of a fault. Because these elements operate for
internal and external faults, reverse-reaching distance (21) or directional overcurrent (67) relays are needed
to block keying and tripping for faults on the bus side of the relay.
The logic at the weak infeed terminal works as follows. None of the forward-reaching relays operate, but a
permissive trip is received from the remote terminal because of a fault on the line or a fault on the bus side
of the weak infeed terminal. If the reverse reaching relays do not operate, AND 2 produces an output to
echo key the transmitter, permitting the strong infeed terminal to trip with minimal time delay. A
pickup/dropout timer on the echo key output ensures that the echoed signal duration is shorter than the echo
delay to prevent keying signal lockup. AND 2 further provides one of the inputs to AND 3, which has a
second input provided by a drop in phase voltage (27L pickup), a rise in residual voltage (59N pickup), or
the presence of a small amount of zero-sequence current (50N pickup). If the output of AND 3 persists for
the pickup time of the security timer (TL), tripping is initiated at the weak infeed terminal of the line.
If the fault is behind the weak infeed terminal, the reverse-reaching relay elements operate to block echo
keying and weak infeed tripping. The reverse-reaching relay elements are required for the echo keying
logic, even if weak infeed logic is not used.
In summary, the weak infeed logic TRIP output asserts when the following three conditions occur
simultaneously:
 A permissive signal is received from the strong remote terminal, indicating that a fault has been
detected by the forward-reaching relay elements located there.
 There is no output from the reverse-reaching relay elements at the weak infeed terminal, indicating
that the fault is not behind the weak terminal.
 There is a drop in phase voltage or neutral overvoltage is detected at the weak terminal, indicating
that a fault exists.
The following are some advantages of the weak infeed and echo keying logic:
 Scheme dependability is improved because it permits tripping, via the echo feature, at any line
terminal where the fault is detected, regardless of whether the forward-reaching relay elements at
the other terminals operate. This feature eliminates the need to continuously key the transmitter
when the line circuit breaker is open.
 The scheme is secure in that it will not trip for any fault if the channel is inoperative.
 The scheme provides logic to initiate fast tripping of the weak infeed terminals of the line, thereby
avoiding delayed sequential tripping or no tripping.
86
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.3.5.10 Current-reversal guard logic for parallel lines used with schemes with
overreaching elements
Pilot schemes may have to accommodate sequential tripping of circuit breakers for faults on one of the
parallel lines shown in Figure 56. A fault on one line is seen by the relays at both ends of the faulted line as
well as by the relays at both ends of the unfaulted line. The fault initially appears to be behind the relays
provided on the unfaulted line at bus A but appears to be a forward fault to the relays provided on that line
at bus B terminal. Circuit breaker 3 would trip first because the fault is close to this terminal of the faulted
line. The current flow now changes direction in the unfaulted line, causing the relays protecting this line at
the bus A terminal CB 1 to see a forward fault and trip undesirably if the permissive signal is still being
received from the remote terminal CB 2. Most relaying systems use a current-reversal guard logic function,
also known as transient blocking logic, to introduce time delay for stabilizing the protection system during
fault current reversal. This is accomplished by signal continuation in the DCB scheme. Identification of a
fault as a reverse fault introduces a time-delayed reset of the blocking carrier. In the case of the POTT or
unblocking systems, the pilot signal is used to permit a trip. A time delay is used to allow the trip functions
at bus B and the transmitted permissive signal to reset through the current-reversal logic circuitry. DUTT
and PUTT systems do not require current-reversal blocking because the distance units that control the
channel are set to reach up to 80% to 90% of the line only.
Bus A Bus B
CB 1 CB 2
V V
S R
Fault
CB 3 CB 4
Figure 56 —A system with parallel lines
6.3.6 Superimposed principle relay and directional traveling wave relay
Principles of superimposing pre-fault and fault currents and directional traveling wave have been proposed
and implemented in solid-state and numerical relays. These principles are described by Dommel and
Michels [B21].
6.4 Other protection schemes
6.4.1 General
Several other protection schemes are being used at this time. Several schemes are described in this subclause.
6.4.2 Power swing considerations
6.4.2.1 General
Power swing is a variation in power flow that occurs when the generator rotor angles are advancing or
retarding relative to each other in response to changes in load magnitude and direction, line switching, loss of
generation, faults, and other system disturbances. Power swings can considerably reduce the voltage at the
line terminals, considerably increase line currents, and slightly change frequency as measured. As a result,
power swings can pose both security and dependability problems for many of the line-protection functions.
87
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Elevated currents and depressed voltages can resemble fault conditions and, therefore, can jeopardize security
of distance, undervoltage, and overcurrent functions. Changes in frequency can reduce accuracy of
polarization and directional methods that rely on memorized values of the polarizing quantities. The security
of some of the protection methods, such as line current differential, is not affected by power swings.
Subclause 6.4.2.3 briefly describes the need of power swing blocking for typical line-protection functions.
During power swings, many line-protection functions could also experience decrease in their dependability
as compared with no-swing conditions. Subclause 6.4.2.4 briefly describes protection dependability issues
during power swings.
Subclause 6.4.2.2 lists practical methods for detecting power swings. From this perspective, one
distinguishes between stable and unstable power swings. A power swing is considered stable if the
generators do not slip poles and the system reaches a new state of equilibrium, i.e., an acceptable operating
condition. An unstable power swing results in a generator or group of generators experiencing pole
slipping, called an out-of-step condition, for which some corrective action should be taken. One of such
corrective actions associated with line protection is a controlled separation of out-of-step systems by
tripping the connecting transmission line(s). Elmore [B25] and a PSRC report, “Power swing and out-of-
step considerations on transmission lines” [B43], describe details of the out-of-step tripping considerations.
Typically, a power swing relay element can be used to do the following:
 Detect a power swing (stable or unstable) with the application to secure protection functions that
might be susceptible to swings (power swing blocking).
 Detect an unstable power swing with the application to separate the system by tripping the
transmission line (out of step tripping).
 Often detect a fault during a power swing with the application to de-assert the power swing block
and/or adjust selected line-protection functions in order to regain some dependability for faults
during the power swing.
Typically, the elements of power swing protection discussed in this subclause (power swing blocking, out-
of-step tripping, and unblocking on faults during swings) are applied in a coordinated manner considering
system issues with a specific system-wide objective in mind.
6.4.2.2 Power swing detection
Traditional power swing detection methods that respond to the rate of change of the apparent impedance
are described by Elmore [B25] and a PSRC report, “Power swing and out-of-step considerations on
transmission lines” [B43]. Faults result in sudden changes of the impedance, while swings change the
apparent impedance at a relatively lower rate. Often, only the positive-sequence apparent impedance is
monitored by the power swing elements.
The rate of impedance change can be monitored by measuring the amount of time the impedance spends in
predefined areas of the impedance plane.
These areas can be shaped as circular, rectangular, or resistive blinders. In any case, the most outer region
used for swing detection should not overlap with the load area, and the most inner region should safely
encompass the operating zone of the protection functions that use the power swing block signal for
security. For this reason, the circular shapes better suit applications with mho distance functions, and the
rectangular shapes allow better coordination with quadrilateral distance functions. The resistive blinder
method does not limit the swing detection regions along the reactance axis; for this reason, it may be
considered easier to apply.
The methods based on the predefined areas of the impedance plane can operate in two or three steps. A
two-step method declares a swing when the apparent impedance enters the area between the outer and inner
88
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
shapes and stays there for a predefined period of time (a single-timer method). A three-step method
increases the security of power swing detection by requiring the impedance to enter and stay in the area
between the outer and middle shapes, and subsequently move and stay between the middle and inner shapes
(a two-timer method). In this way, a more accurate detection of the persistent and slow movement of the
apparent impedance is accomplished.
Classical power swing detection methods based on the predefined areas on the impedance plane are affected
by system impedances, while the power swing phenomenon itself reflects only interactions of the generator
rotors. This dependence complicates settings of the power swing elements. Proper application of the power
swing elements requires dynamic system models with properly selected contingencies in order to determine
possible trajectories of the apparent impedance during swings so that the impedance shapes can be set. It also
requires determining the rate of change of the impedance so that the element’s timers can be set.
A newer method uses a continually updated dZ/dt measurement of the rate of change of impedance. This
replaces the simplistic monitoring of the rate of change via timing in the predefined areas of the impedance
plane. The dZ/dt values between the minimum and maximum thresholds indicate a swing. High values of
dZ/dt point to discontinuity events such as faults, and low values of dZ/dt point to existing yet not cleared
faults. This method is less dependent on the location of the impedance trajectory during swings and less
prone to false operation during system faults.
Another new method uses a swing center voltage to detect power swings [B43]. Voltages and currents at a
line terminal allow a relatively precise estimation of a quantity proportional to the voltage at the swing center
(SCV). The rate of change of the SCV magnitude is a good approximation of the rate of change of the relative
angle between the systems. The method responds to a continually updated dSCV/dt measurement.
Both the dZ/dt and dSCV/dt methods allow relatively reliable detection of faults occurring during power
swing conditions (power swing unblocking).
6.4.2.3 Power swing blocking
Power swing blocking is applied to avoid random operation of protection elements due to power swings and
to allow enough time for system protection to rectify the abnormal system condition. A PSRC report,
“Performance of relaying during wide-area stressed conditions,” provides more details on this subject [B42].
Current-only functions, such as current differential and phase comparison, are relatively secure during
power swings because during a swing the currents at all line terminals sum up to zero (neglecting charging
currents, CT errors, and similar effects).
Directional comparison schemes are typically affected adversely unless they use current-only elements (for
example, current polarized ground directional overcurrent); another option is to use elements that are more
immune to swings (for example, negative-sequence directional overcurrent).
Overcurrent and voltage functions may be jeopardized depending on their pickup and time-delay settings.
Generally, more margins in the pickup thresholds compared with load and longer time delays make these
functions less prone to misoperation during power swings. Negative-sequence and zero-sequence
overcurrent protection functions are secure during power swings, unless an open-phase condition in the
protected line or in vicinity, or an external fault, causes considerable current unbalance. This unbalanced
current is subjected to a power swing the same way a positive-sequence current is and, therefore, may result
in misoperation of the negative-sequence- or zero-sequence-based functions.
Distance functions are affected through a combination of lower apparent impedance and memory
polarization, if applied as described by Cook [B18] and a PSRC report, “Performance of relaying during
wide-area stressed conditions” [B42]. Instantaneous underreaching directly tripping zones may be affected.
Instantaneous overreaching zones and reverse-looking blocking zones working in directional comparison
schemes may be affected as well. Time-delayed distance functions may be immune to swings if their time
89
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
delay is long enough to ride through the period of time when the apparent impedance stays inside their
operating characteristics.
Application of power swing blocking increases the integrity of the power system. In order to avoid
disrupting such large integral systems under major power system disturbances beyond their design limits, it
is beneficial to apply proper system protection, including controlled separation via out-of-step tripping.
6.4.2.4 Protection dependability during power swings
Power swings decrease dependability of many protection functions even if these functions are left
operational or, if blocked, become unblocked upon detecting a fault during a power swing. This is
particularly true during severe or unstable swings. When, during a line fault, the equivalent systems are
considerably out of phase, they will feed currents toward an internal fault that are out of phase. This current
flow pattern can impact the dependability of many protection functions.
In general, the following issues impact dependability during power swings:
 Directional elements may not perform well during swings. For example, during an unstable power
swing, it is extremely challenging to detect the direction of a three-phase fault. Negative-sequence
directional elements will be affected if there is a pre-existing system unbalance (e.g., open pole).
 Line terminal currents due to power swings may reach a value of a few times the CT nominal rating
and may flow considerably out of phase, creating similar effects as the load current during no-
swing conditions. This includes, for example, an infeed/outfeed effect for distance functions or
extra restraint for differential functions.
 Memory polarization or usage of incremental protection quantities may cause problems. The
memorized values reflect positions of the equivalent sources from the past, while the protected
system swing is changing its angular position.
Increasing dependability during power swings can be achieved through the combination of several items
summarized below and discussed in more detail in a PSRC report, “Power swing and out-of-step
considerations on transmission lines” [B43]:
 Canceling the block from the power system blocking element upon detecting a fault during a power
swing.
 Using negative-sequence elements to detect unbalanced faults.
 Using phase distance elements with time delay to detect three-phase balanced faults. These
elements can be quadrilateral with narrow blinders to allow better time coordination for a swing
entering the characteristic.
 Using non-directional distance elements with time delay to ensure detection of close-in faults,
particularly three-phase faults during unstable swings.
Application of these measures to regain dependability during power swings may result in decreased
security and unintended operation for external faults.
In many instances the decrease in dependability is temporary. When the stable swing subsides, or when the
unstable swing reaches a point of the sources being in synchronism, many protection functions will operate
within their specifications.
Detailed descriptions of the power swing and out-of-step protection are given in a couple of PSRC reports,
“Power swing and out-of-step considerations on transmission lines” [B43] and “Performance of relaying
during wide-area stressed conditions” [B42].
90
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.4.3 Switch onto a fault
Protection from switching onto a fault is provided to supplement distance protection schemes for close-in
faults that might not be detected because of the location of the VTs and lack of memory when a
transmission line is energized from a bus. This protection system becomes operational if the line circuit
breaker is opened. It then uses non-directional overcurrent relays that provide instantaneous tripping
immediately following the closing of the line circuit breaker. Sometimes, voltage level detectors are also
included in the scheme for increasing security and avoiding operation of the system on load pickup. These
protection systems are also called close-into-fault systems. These systems are especially necessary when
line-side VTs are used for distance relays. The system remains operational in a small time window in which
it trips the circuit breaker if a fault is detected. The use of non-directional impedance relays has also been
introduced for tripping the line when switched onto a fault. Switching onto fault logic can also be used to
clear the line with overreaching elements when the lead breaker closes and the remote breaker is still open.
6.4.4 Fault detector supervision
Fault detector supervision is used to enhance the security of a protection scheme. When used in this
function, the fault detector is placed in series with other protective devices trip circuits, only allowing the
device to operate if a fault is present on the system. It was originally used in electromechanical protection
schemes to prevent relay operation on loss of voltage, inadvertent tripping during relay testing, and
incorrect operation during line energization, or to enhance the seismic performance of a relay system. Since
fault detector supervision does increase the security of any system, it is still in common use in static and
microprocessor-based systems. The optimum setting is below minimum-expected fault current and above
maximum-expected load current; but the setting should always be below the minimum-expected fault
current irrespective of the expected load current.
6.4.5 Remote-breaker operation-detection scheme (loss of load)
Loss of load or remote-circuit-breaker operation-detection logic can be used to speed up fault clearing for
faults beyond the reach of the zone 1 distance relay or the instantaneous directional ground overcurrent
relay. This scheme is typically applied when communications for pilot relaying are not available.
When a fault occurs at the remote end of the protected line, zone 1 of the remote end protection operates
without intentional time delay. This will result in changes of the currents of the unfaulted phase(s) from
load current to line-charging currents if the fault is other than a three-phase or three-phase-to-ground fault.
At the same time, the relay would see the fault current in the faulted phase(s). If this condition exists for a
specified time (0.5 cycle to 1.0 cycle), a decision is made that the remote circuit breaker has opened. The
relay then operates in a similar way to a POTT scheme and trips the local circuit breaker without any
additional time delay. This scheme can operate incorrectly for faults on other lines if the load currents of
the unfaulted phases drop below the load current threshold setting. The issues to be considered should
include the following:
 Because of the principle of operation described above, the remote-breaker operation-detection
scheme will not operate for three-phase faults.
 The remote-circuit-breaker operation-detection scheme should not be considered equivalent to a
pilot scheme, although it offers some of the improvements of pilot schemes.
 Tapped load on the transmission line may prevent application of this scheme.
 The combination of load current and unbalanced fault current can cause low current in one phase,
which might cause this scheme to operate for a fault on an external circuit.
91
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.5 Directional ground overcurrent relay polarization
6.5.1 General
Several methods are available to polarize directional ground overcurrent relays. These methods and the
issues associated with them are addressed in 6.5.2 through 6.5.5. A PSRC report, “Considerations in
choosing directional polarizing methods for ground overcurrent elements in line protection applications,”
further discusses polarization [B37].
6.5.2 Zero-sequence voltage polarization
Some directional ground overcurrent relays determine if a fault is on the line side of the relay or on the bus
side of the relay by comparing the phasor relationship between the zero-sequence currents flowing in the
protected line (3I ) and the zero-sequence voltage (3V ) at the relay location. The zero-sequence voltage is
0 0
derived from the secondary voltages of VTs or capacitance voltage transformers (CVTs) by using a broken-
delta connection.
The magnitude of the zero-sequence voltage at the relay location depends on the location of the fault,
impedance of the zero-sequence source behind the relay location, and the sequence impedances of the
transmission line. The zero-sequence voltage at substations with large solidly grounded transformer banks
(small zero-sequence source impedance) should be checked for remote faults to ensure that an adequate
magnitude of 3V is present for proper operation of the ground directional systems. Modern ground-
0
directional relays are very sensitive, so this may not present a problem unless a standing zero-sequence
voltage is present due to relay voltage source inaccuracies or due to inherent imbalance of system voltages
caused by non-transposed lines.
Another method of polarization should be used if the magnitude of 3V is too low for some system fault
0
conditions. Refer to 6.5.3 through 6.5.5 for other polarization methods that could be used.
An incorrect 3V measurement at a relay can cause incorrect operation of the ground-directional relay. The
0
neutral of the VT secondary should be wired to the relay neutral and should be grounded at only one
location to ensure that the 3V measured at the relay location is correct. This issue is discussed further in
0
IEEE Std C57.13.3™ [B71].
6.5.3 Zero-sequence current polarization
Zero-sequence current polarization is commonly applied at substations where power transformers that can
provide polarizing current, I , are available. This method of polarization compares the phase angle of the
POL
zero-sequence current flowing in the polarizing source (transformer neutral) with 3I flowing in the line.
0
This method works only if the current used for polarization flows in the same direction regardless of the
fault location. Figure 57 shows an example of polarizing sources for various power transformer
configurations. Only the delta-wye grounded transformer shown in Figure 57(a) or a wye grounded/wye
grounded/delta transformer shown in Figure 57(e) and Figure 57(f) provides adequate ground polarizing
current for lines connected to the wye windings of the transformer. Current flowing in the neutral of an
autotransformer is also used as a current polarization source. None of the other transformer configurations
shown in Figure 57 are suitable for using current polarization because they do not always provide or allow
for a ground current path. CTs within the tertiary windings of autotransformers may be a suitable source of
ground polarization current in many situations. Guidelines for the use of tertiary winding CTs are contained
in IEEE Std C37.110™ [B63]. Three-winding transformers that may be suitable for providing I are also
pol
described by Blackburn [B11].
In some cases, the relative direction of I may change depending on the location of the fault. Figure 58(a)
pol
shows the current flows for a fault at bus C, and Figure 58(b) shows the current flows for a fault at bus B.
The direction of the flow of current in the neutral of the autotransformer shows that the current flow in the
transformer neutral is not suitable as a polarizing quantity for this case. Therefore, studies should be
92
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
conducted to ascertain the suitability of zero-sequence current polarizing sources. Another polarization
method should be used if an adequate source of I  is not available.
pol
Inadequate
Adequate
Source
Source
| (a) | I          |     | I = 0      |
| --- | ---------- | --- | ---------- |
|     | pol        | (b) |            |
|     | Inadequate |     | Inadequate |
|     | Source     |     | Source     |
| (c) | Source may | (d) | Source may |
be open
be open
|     | Adequate |     | Adequate |
| --- | -------- | --- | -------- |
|     | Source   |     | Source   |
LOAD
LOAD
| (e) |     | (f) |     |
| --- | --- | --- | --- |
Inadequate
Source
Inadequate
Source
LOAD
|     | Masked |     | Masked |
| --- | ------ | --- | ------ |
LOAD
| (g) | by load | (h) |     |
| --- | ------- | --- | --- |
by load
Inadequate
Inadequate
|     | Source | Source |     |
| --- | ------ | ------ | --- |
∠∠
| Ungrounded |     | No V | 0   |
| ---------- | --- | ---- | --- |
Present in
Aux
| No V         | 0  Present | Primary Voltage |     |
| ------------ | ---------- | --------------- | --- |
| in Secondary |            | of Aux VT       |     |
| (i)          |            | (j)             |     |

Figure 57 —Adequate and Inadequate polarizing sources
93
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
I = 132 Amps
F1
I = 1592 Amps
F1
I = 1724 Amps
F1
Bus B
Bus C
F
1
I = 1454 Amps
F1
I = 1648 Amps
F1
Bus A
(a) Fault F at Bus C
1
F
2
I = 3783 Amps
F2
I =
F2
6123 Amps
I = 2340 Amps
F2
Bus B
Bus C
I = 1611 Amps
F2
I = 1433 Amps
F2
Bus A
(b) Fault F at Bus B
2
Figure 58 —Changes in polarizing source for ground fault
94
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.5.4 Negative-sequence polarization
Negative-sequence directional relays determine the direction of a fault from the phase angles of the phasors of
the negative sequence voltage, V , and the negative sequence current in the line, I , at the relay location. The
2 2
negative-sequence voltage is derived from the secondary voltages of VTs or CVTs by using a negative-
sequence filter in a protective relay. Untransposed transmission systems or improperly adjusted relay voltage
sources present an inherent negative-sequence voltage (as they present an inherent zero-sequence voltage) that
could be of a magnitude that may be sufficient to incorrectly polarize negative-sequence directional relays.
Users should routinely check the standing negative-sequence (and zero-sequence) voltage of VTs and CVTs
during maintenance and take corrective actions if these standing voltages are sufficient to cause problems for
the polarizing process. Negative-sequence polarized directional relays have several advantages over zero-
sequence polarized directional relays.
Negative-sequence polarized relays are insensitive to zero-sequence mutual coupling associated with
protection of parallel transmission lines. This coupling can occasionally cause a zero-sequence polarized
directional relay to lose directional integrity in cases where the mutually coupled lines have a different
zero-sequence source at one or both ends of the line.
There is often more negative-sequence current than zero-sequence current for remote ground faults with high
fault resistance. This allows higher sensitivity with reasonable and secure sensitivity thresholds. Negative-
sequence current is accurately obtained from line-to-line quantities and is not affected by zero-sequence
currents in the line. The use of negative-sequence polarizing eliminates the need to connect another source,
beside the currents and voltages, to the relay. The negative-sequence polarization method works quite well in
most applications. However, the level of negative-sequence voltage measured at the relay terminals can be
very low when the negative-sequence source behind the relay terminal is strong (low negative-sequence
source impedance). An exceptionally low level of V is likely to be experienced for remote faults. Some
2
negative-sequence directional relays use a compensated negative-sequence voltage to overcome this problem.
There is a coupling between the positive and negative sequence networks when lines are not transposed. The
impact of this coupling increases when the line is heavily loaded; this could cause considerable negative-
sequence currents to flow in the line. These currents may appear to negative-sequence directional relays at
both terminals of the line to be currents due to an internal fault leading to undesired tripping of the line.
6.5.5 Other polarization methods
Other polarization methods exist in addition to zero-sequence voltage, zero-sequence current, and negative-
sequence polarization. Dual polarizing is a method where the residual ground current measured at the relay
is polarized by both a polarizing current measured at a grounding transformer and/or the zero-sequence
voltage measured at the relay. This method can be advantageous because polarizing current generally
provides good sensitivity for remote faults, and polarizing voltage can be used alternatively if the
polarizing current is removed from service. Negative-sequence impedance polarization, zero-sequence
impedance polarization, and virtual polarization are other methods that are used. Finally, voltage
compensation is a method that provides operating current (3I or 3I ) compensation to the polarizing
0 2
voltage (3V or 3V ) in instances when greater sensitivity of the polarizing quantity is necessary to detect
0 2
forward faults.
Undesired tripping can occur on transmission lines protected by a directional comparison pilot scheme for
remote ground faults where different polarizing methods are used at the two terminals of the line, as described
by Elmore and Price [B28]. Figure 59 shows a three-bus system in which the transmission line from bus A to
bus B is protected by a directional comparison pilot scheme. The relay R provided at the bus A terminal of
A
the line is a protection system that uses zero-sequence voltage and current for directional polarization. The
relay R provided at the bus B terminal of the line is a relay that uses negative-sequence voltage and current
B
for directional polarization. Both systems would see a remote fault on the line from bus A to bus C, or the line
from bus B to bus C, as a fault in the forward direction on the line they protect and undesirably trip the
transmission line from bus A to bus B. The tripping results if the negative- and zero-sequence currents flow in
95
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
opposite directions in the protected line and the situation appears at both terminals to be an internal fault. The
root cause is that different directional polarizing methods are used at the line terminals in this case.
This undesired tripping of a line would not occur if line and system negative- and zero-sequence impedances
were identical. Normally, these impedances are not identical and, therefore, ground faults in small sections of
the remote system parallel to the line appear as internal faults.
Bus A Bus B
R R
A I 0 Polarization I 2 Polarization B
S 1 S 2
1Φ − G
BUS C
S
3
Figure 59 —A single-phase-to-ground fault and ground fault relays on an adjacent line
6.6 Problems associated with multi-terminal lines
6.6.1 General
There are two challenges in applying protection for multi-terminal lines as discussed in a PSRC report,
“Protection aspects of multi-terminal lines” [B44]:
Trip all terminals simultaneously for an internal fault at any location on the line with any
expected distribution of current.
Do not trip any terminal for an external fault at any location on the system with any
expected distribution of current.
These challenges are further complicated by the very large number of line configurations with varying
numbers of terminals, lengths of lines, and capacities of energy sources and levels of loads. However, the
protective systems that are used for two-terminal lines may be adapted for use on multi-terminal lines by
choosing appropriate settings or by using additional hardware or software.
6.6.2 Current outfeed
Multi-terminal lines create the possibility of a current outfeed condition. Current outfeed occurs when, due to
system source, load, and impedance conditions, current flows out at one or more terminals of a line during an
internal fault. This outfeed condition may cause delay in operation or may result in sequential operation of
protection systems at different terminals for some types of relays and the communication systems used with
them. It is possible that some relays and pilots may not operate at all when current outfeed occurs.
Figure 60 shows an example of an outfeed condition. Distance and directional relays may be affected by
the outfeed current at bus B. Consider that the phase angles of all the impedances are identical and the
phase angles of all currents shown in this figure are identical as well, so that the calculations remain simple
and straightforward.
96
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
| Bus A |     |     |     |     |     | Bus C |     |
| ----- | --- | --- | --- | --- | --- | ----- | --- |
Fault
|     |      | I  = 1.0 |     | I  = 0.5 |     |      |     |
| --- | ---- | -------- | --- | -------- | --- | ---- | --- |
|     | CB A | A        |     | C        |     | CB C |     |
|     |      | Z  = 1.0 |     | Z  = 1.0 |     |      |     |
|     |      | A        |     | C        |     |      |     |
0.0 =
|     |     |     | 5.0 =  |     | I  = 0.5 |     |     |
| --- | --- | --- | ------ | --- | -------- | --- | --- |
DE
|     |     |     |     |     | Z  = 1.0 |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- |
DE
| Actual Impedance from Bus A |     |     | B B |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- |
I Z
to the Fault = 2.0 Ω
CB E
|     |     | CB B |     |     | CB D |     |     |
| --- | --- | ---- | --- | --- | ---- | --- | --- |
Bus B
|                       |     |     | E   | (I  |  × Z ) + (I |  × Z )    |     |
| --------------------- | --- | --- | --- | --- | ----------- | --------- | --- |
| APPARENT IMPEDANCE =  |     |     | A   | = A | A C         | C = 1.5 Ω |     |
|                       |     |     | I   |     | I           |           |     |
|                       |     |     | A   |     | A           |           |     |
Figure 60 —Current outfeed
The apparent impedance seen by the relay at bus A is 1.5 Ω due to the outfeed current at bus B. This
measured value is less than the actual impedance to the fault, which is 2.0 Ω. A reverse-looking or
blocking, distance, or directional relay at bus B would “see” an internal fault as an external fault and may
prevent the pilot protection from operating for this internal fault.
6.6.3 Current infeed
Multi-terminal lines create the likelihood of a current infeed condition. This infeed condition may cause a
distance relay not to see a fault beyond the location where the infeed of current occurs until the fault is
isolated from the bus closest to the fault.
Figure 61 shows a condition in which there is a current infeed from bus B when there is a fault on the line near
bus C. Consider that the phase angles of all the impedances are identical and the phase angles of all currents
shown in this figure are identical as well, so that the calculations remain simple and straightforward.
| Bus A |     |     |     |     |     | Bus C |     |
| ----- | --- | --- | --- | --- | --- | ----- | --- |
Fault
|     |      | I  = 0.5 |     | I   |  = 1.0 |      |     |
| --- | ---- | -------- | --- | --- | ------ | ---- | --- |
|     |      | A        |     |     | C      |      |     |
|     |      | Z  = 1.0 |     | Z   |  = 1.0 |      |     |
|     |      | A        |     |     | C      |      |     |
|     | CB A |          |     |     |        | CB C |     |
5.0 =  0.1 =
| Actual Impedance from Bus A |     |     | B B |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- |
I Z
to the Fault = 2.0 Ω
CB B
Bus B
|                       |     |     | E   | (I  × Z | ) + (I  × Z | )         |     |
| --------------------- | --- | --- | --- | ------- | ----------- | --------- | --- |
| APPARENT IMPEDANCE =  |     |     | A = | A       | A C         | C = 3.0 Ω |     |
|                       |     |     | I   |         | I           |           |     |
|                       |     |     | A   |         | A           |           |     |
Figure 61 —Current infeed
97
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
A distance relay at the bus A terminal of the line would see an apparent impedance of 3.0 Ω; this is greater
than the actual impedance to the fault. Current infeed has the effect of causing a distance relay to
underreach for all faults beyond the location where the infeed of current occurs. The distance relay could
interpret an internal fault as a fault beyond the remote bus, which is bus C in this case.
6.6.4 Relay applications on multi-terminal lines
6.6.4.1 General
This subclause covers the issues that concern relay applications on multi-terminal lines and briefly discusses
several communication-based relay schemes to protect such lines.
6.6.4.2 Distance relay setting considerations
Multi-terminal lines cause complications in the setting of both underreaching and overreaching distance relays.
Zone 1, or underreaching elements, should be set so as not to reach the nearest terminal without considering the
effects of current infeed from other terminals. This limitation may cause the application of some of the zone 1
elements to be ineffective on multi-terminal lines that have two of their terminals close together.
It might also result in a section of the line not covered under zone 1 of any relay, as discussed in a PSRC
report, “Protection aspects of multi-terminal lines” [B44]. One such case is shown in Figure 62. The thick
lines show the parts of the system covered by zone 1 elements. Clearly, the highlighted section of the line
becomes a “blind spot”; the zone 1 relays provided at the two terminals of the line are not able to detect
faults in this spot. Underreaching schemes cannot be employed for such cases.
Bus A Bus D
CB A Z EF = 1.7 CB D
E F
Z = 1.7 Z = 0.5
AE DF
Z BE = 0.3 Blind Spot
Z = 0.4
of 1 pu CF
CB B
Bus B CB C
Bus C
All Impedances are in per unit values
Figure 62 —A case of unsuitability of underreaching distance scheme
It can become a difficult problem to protect a multi-terminal line that has more than three terminals. Zone 2
elements are normally set to cover those portions of the protected line that are not covered by zone 1. For
multi-terminal lines, this setting requires that the effects of infeed and fault resistance be considered. The
settings required to cover the entire protected line with some margin could be large because the infeed
current can be quite significant. However, if the infeed is not present or is removed by the tripping of a
circuit breaker, this large setting may cause the zone 2 to reach beyond the zone 1 relays protecting the
lines emanating from the remote bus. If this happens, it may be necessary to coordinate the zone 2 timer of
98
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
the three-terminal line with the zone 2 timer of the remote line to maintain coordination. It is also important
to ensure that the large setting does not restrict the ability of the line to handle expected load.
Overreaching elements that are part of a pilot scheme are normally set to detect faults on the entire protected
line; all current infeeds are considered in this process. The coordination with elements protecting adjacent
lines is not normally a problem. The load transfer capability is not an issue either in most cases. A typical
setting for the overreaching functions would be at least 125% of the largest apparent impedance to the remote
terminals. This additional margin is important to ensure that the operation of the protection system is
consistent and is without unnecessary delay. These are two important operational features for pilot schemes.
The setting of zone 3 elements on multi-terminal lines is quite complex. The setting depends on the
protection requirements assigned to the zone 3 relay and the configurations of the stations at the remote
terminals of the multi-terminal line. The setting may require the consideration of the infeed within the
protected line, as well as any infeed that can flow into the remote terminal from other sources. Generally,
the effectiveness of zone 3 as remote backup protection is limited for most multi-terminal lines; this
requires that local backup or other forms of redundancy be applied.
It may be necessary to reduce the settings of overreaching elements to allow for sequential operation if infeed
requires the settings of those relays to be so large that they would restrict the load transfer capability of the
line or would result in losing coordination with protection systems on adjacent lines. Sequential operation
requires that all faults are detected by at least one of the terminals. The terminal that detects the fault is
allowed to trip, which removes its infeed contribution and allows the other terminals to detect the fault and
trip. This sequential operation adds significant time delays and may be unacceptable for many applications.
6.6.4.3 Direct underreaching transfer trip scheme
Refer to 6.3.5.2 for discussion of two-terminal DUTT schemes. A multi-terminal application follows the
same principles.
6.6.4.4 Permissive underreaching transfer trip scheme
Refer to 6.3.5.3 for discussion of two-terminal PUTT schemes. A multi-terminal application follows the
same principles.
6.6.4.5 Permissive overreaching transfer trip scheme
Refer to 6.3.5.4 for discussion of two-terminal POTT schemes.
A situation can arise when POTT is applied to a multi-terminal line in which the line is energized from one
terminal while all other terminals are open. There is a possibility that the line may be closed into a fault.
The logic should ensure that each open terminal echoes to all other terminals on the receipt of a permissive
signal; the logic should not require permission to be received from all terminals because this will not occur
for the reason that only one terminal has closed into the fault and all other terminals are open.
The POTT with echo and weak-infeed tripping scheme is a combination of the best features of the POTT
and DCB schemes. This combination may solve some of the problems associated with pilot relaying of
multi-terminal lines. As in a POTT scheme, tripping is initiated when a local overreaching relay operates
and a permissive signal is received from all the remote terminals. The same concerns regarding current
distribution at the tap point mentioned in 6.6.4.6 apply to POTT with echo and weak feed logic.
6.6.4.6 Directional comparison blocking scheme
Refer to 6.3.5.6 for discussion of two-terminal DCB schemes.
99
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
For multi-terminal schemes, current outfeed conditions may cause blocking of all terminals during internal
faults if the current outfeed exceeds the pickup of the carrier start element. For external faults, outfeed may
result in a current division at the tap point such that the blocking terminal may see less current than the
tripping terminal, resulting in lack of coordination.
6.6.4.7 Phase comparison protection
Phase comparison protection of multi-terminal lines may use individual phase currents or a composite
signal that is derived from the sequence components of the phase currents as the operating quantity, just as
is done for protecting two-terminal lines. The phase angles of the individual currents or of the composite
signal are compared via a communication channel. The current magnitude may be used by fault detectors to
improve system security. The relay currents during an external fault are approximately equal in magnitude
in two-terminal lines. These currents are out of phase for external faults and in phase for internal faults. On
a three-terminal line, the currents at the three relay locations may vary both in magnitude and phase angle
and, therefore, phase comparison is not normally a good choice for protecting multi-terminal lines.
6.6.4.8 Current differential protection
Current differential can also be applied to multi-terminal lines and is discussed in IEEE Std C37.243 [B70].
6.6.5 Transformer-terminated taps
The effect of a transformer-terminated tap on transmission line relaying depends on the transformer location
with respect to the other terminals, the transformer connections, and the location of circuit breakers at the
transformer. If the transformer is a zero-sequence source, the resulting zero-sequence current infeed should be
considered when setting the remote ground distance relays or directional overcurrent relays. The performance
of the ground directional overcurrent relays and line differential relays should also be evaluated, because the
presence of a zero-sequence source tends to reduce the zero-sequence voltage at the line terminals.
6.7 Application considerations of distance relays
6.7.1 General
Several application considerations are important when distance relays are used to protect transmission
lines. Five major concerns are discussed in 6.7.2 through 6.7.6.
6.7.2 Influence of load and fault resistance on distance relays
6.7.2.1 General
Distance relays discriminate between load and fault conditions by measuring both the magnitude and angle
of the impedance presented to them. Figure 63 illustrates the importance of measuring the angle, as well as
the magnitude, of the impedance. The self-polarized mho relay whose characteristic is shown in this figure
operates if the measured impedance is inside the circle. It can be seen that a fault near the end of the
transmission line (even with some resistance in the fault) presents to the relay an impedance with a much
larger angle than the angle for a heavy load that may have the same magnitude of impedance.
The effect of the reduced angle of the load impedance is that this impedance is outside the reach of the
distance relay. It is important in the application of distance relays to ensure that the impedance of the
maximum load (smallest impedance) presented to the relay is outside the operating characteristic with some
100
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
margin for security. The apparent impedance presented by loads should be considered under the smallest
possible power factor and the lowest possible voltage and, if applicable, under power swing conditions.
jX
Transmission Line
Impedance Locus
Fault
Location
Fault
Resistance
e
c
n
a
d
e
p Load
m
ult
I Impedance
a
F
R
Figure 63 —Effect of angle of impedance presented to a distance relay
The mho circle increases in diameter if the impedance setting is increased; this takes the mho circle closer
to the load impedance. A major contributing factor to the wide area disturbance that happened in North
America in August 2003 is known to be the undesirable operation of overreaching zones under system
stressed conditions. The followup investigations of this major disturbance prompted the North American
Electric Reliability Corporation (NERC) to require that severe loading of the system at a reduced voltage
level should not result in the load impedance to encroach into the impedance characteristics of relays
provided to protect lines as specified in NERC Standard PRC-023 [B90]. Several methods that shape the
characteristics of impedance relays to achieve this objective are described in 6.7.2.2.
Figure 63 shows that, as the fault resistance increases, it becomes progressively more difficult to
discriminate between a fault with high resistance and load. A variety of methods are used to allow a
distance relay to detect faults with high resistance without operating under load conditions. It is beyond the
scope of this guide to discuss all these methods, but two of the most common ones are the use of specially
shaped characteristics and special polarization techniques described in 6.7.2.2 and 6.7.2.3, respectively.
101
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.7.2.2 Specially shaped characteristics
There are a large number of specially shaped characteristics (some of which are described in 6.2.4) that can
be used to make a distance relay more sensitive to faults with high resistance while trying to maintain
insensitivity to heavy loads. The principle by which special characteristic shapes achieve this can be
understood by considering a quadrilateral characteristic shown in Figure 64.
jX
B
Quadrilateral
Characteristic
Zf
Mho
Characteristic
K L
Load Line
R
A
Figure 64 —Quadrilateral characteristic
The impedance as seen by the relay moves along the load line as the load increases. The distance relays with the
mho and quadrilateral characteristics cause undesired operation if the load impedance reaches the impedances
represented by L and K, respectively. Figure 64 also shows that the quadrilateral characteristic achieves good
fault resistance coverage while providing higher immunity to load. The resistive reach may be decreased further
for the relay with the quadrilateral characteristic to reduce sensitivity to the load. However, this will cause the
relay to be less sensitive to some faults inside the mho operating zone with a large fault resistance.
Numerical relays use specially shaped load blinders or load encroachment units that are both designed to
allow more coverage along the resistance axis of the impedance plane for faults and less resistance
coverage for loads. The blinder is basically formed from an impedance circle, with radius set by the user
and two straight lines crossing through the origin of the impedance plane. This allows the relay to cut the
area of the impedance characteristic that may result in an operation under maximum dynamic load
conditions, as shown by the cone-type blinders in Figure 65.
The radius of the circle is made less than the minimum dynamic load impedance, and the blinder angle is usually
set halfway between the worst case power factor angle and the line-impedance angle, as shown in Figure 66.
102
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
jX
OPERATE
RESTRAIN
R
RESTRAIN
OPERATE
Figure 65 —Cone-type load blinder
jX
RESTRAIN
s
u
c
o
L
e OPERATE
Blinder
n c angle
a
d
e
p
m
e
I
n
Li Blinder
Load area
R
Blinder impedance
setting
Figure 66 —Blinder to avoid load encroachment trip
103
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
In the case of a fault on the line, it is not necessary to avoid the impact of load. It is desirable if the blinder is,
therefore, bypassed for the faulted phase, allowing the full mho characteristic to become effective as shown in
Figure 66. Also, the disabled blinder characteristic is shown on the side in dotted lines in Figure 67 for
reference only. The load encroachment blocking element can be bypassed if unbalance is detected indicating
that the system is faulted. A method can use the ratio of I /I > threshold to bypass the load encroachment
2 1
blinders. The typical I /I ratio threshold setting with this method is 10% negative-sequence current.
2 1
Alternatively, a negative-sequence overcurrent element can be used to bypass the load encroachment blinder.
jX
RESTRAIN
Expanded
characteristic
s Blinder
u
c angle
o
L
e
c
n Blinder
a
d
e
p
m OPERATE
e
I
n
Li
Load Area
R
Blinder impedance
setting
Figure 67 —Removal of load blinder for faults
The use of phase undervoltage detectors is another method used to govern switching of the blinders. When
a fault occurs, the voltage is less than that experienced during normal operation of the power system.
Because low voltage is an indication of a fault on that phase, the protection system overrides the blinder
action and allows the distance zones to trip according to the entire zone shape. The undervoltage setting
should be lower than the lowest phase-to-neutral voltage under heavy power flow and depressed system-
voltage conditions. The typical maximum voltage setting is 70% of the nominal phase-to-neutral voltage.
This approach usually does not constrain the loadability limits of transmission lines. The benefit of
disabling the blinder is that the resistive coverage for faults near the relay location is higher.
Blinders and lenticular characteristics are shown in Figure 68. Lenticular characteristics have also been
used to allow more loadability so that blinders would not be necessary. Both of these characteristics can
impact fault coverage and should be reviewed for all aspects of their intended functions.
104
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Maximum sensitivity line
jX
jX
Line impedance
Blinder Blinder
e
t
A B
O
p e r a A B at e
r
e
p
O
Restrain
δ
R R
Relay
Restrain
Location
AB is the area of characteristic blocked to accommodate (b) Lenticular characteristic
load encroachment
(a) Mho relay with two load blinders
Figure 68 —The use of blinders with an mho characteristic and a lenticular characteristic
6.7.2.3 Special polarization techniques
There are a number of polarization techniques that can be used to increase sensitivity to faults with high
resistance while improving directionality and retaining immunity to load in addition to the specially shaped
characteristics, as discussed by Giuliante, McConnell, and Turner [B31]. Two techniques commonly used
are cross-polarization and memory polarization. An example of cross-polarization is the use of quadrature
polarization for ground distance functions. The directional element is quadrature polarized when A-phase
relay uses A-phase current and V voltage. Quadrature polarization is helpful under unbalanced fault
bc
conditions, such as single line-to-ground, phase-to-phase, and phase-to-phase-to-ground. In order to supply
a voltage for close-in three-phase faults, many relays have a type of polarization voltage called memory-
polarizing voltage. The effect of both techniques is to expand the operating characteristic, as shown in
Figure 69.
It appears from Figure 69 that a relay with an expanded characteristic might operate under load conditions,
as well as for faults behind the relay. However, the expanded characteristic shown in this figure applies for
faults in the forward direction only; a different characteristic applies for faults in the reverse direction. The
expansion due to quadrature polarization applies to unbalanced conditions only; therefore, quadrature
polarization does not increase the sensitivity to balanced load impedances. The expansion of the
characteristic due to the quadrature polarization lasts for the duration of the fault; however, the expansion
due to memory polarization lasts effectively as long as the memory polarization time constant. Memory
polarization does not allow operation under load conditions because load conditions are steady-state
conditions of the power system.
105
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
jX
Fault
Location
Fault
Resistance
e
c
n
a
d
e
p
m
ult
I
a
F
Load
Impedance
R
Expanded Characteristic due to
Quadrature or Memory Polarization
Figure 69 —Expanded mho characteristic due to polarization techniques
6.7.2.4 Influence of combined effect of load and fault resistance on an impedance
measurement
Operation of a distance relay may be significantly influenced by the combined effect of load and fault
resistance. The distance relay may operate incorrectly for a forward external fault or may not operate for an
internal fault if the value of the fault resistance is too large. The value of the fault resistance may be
particularly large for ground faults that represent the majority of faults on overhead lines. The discussion in
6.7.2.1 assumed that the fault resistance appears to a distance relay as a resistive component of the
measured impedance. However, this is not generally true. The distance relay response to faults with fault
resistance depends on a relay characteristic (shape and reach in the resistive direction) and the impedance
measurement technique. This subclause describes the impact of load and fault resistance on the impedance
measurement.
Figure 70 shows two power systems interconnected by a homogeneous transmission line that connects
bus G and bus H. The two power systems are shown by their equivalent generators and source impedances.
The transmission line, whose impedance is Z , is shown to have a fault through a resistance, R.
L f
106
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
|     | I sf V |     |          | V I rf |     |
| --- | ------ | --- | -------- | ------ | --- |
|     | Gf     |     |          | Hf     |     |
|     | Z      | mZ  | (1 − m)Z | Z      |     |
|     | s      | L   | L        | r      |     |
| V   | G      |     |          | H      | V   |
| s   |        |     |          |        | r   |
R I
f f

Figure 70 —A single-line diagram of two systems connected by a line experiencing a fault
The impedance Z  measured by a relay at terminal G for the fault is given by Equation (17). The voltages
G
and currents used in this discussion are phase-to-phase quantities used for phase-to-phase and phase-to-
phase-to-ground faults as listed:
V
Z = Gf
G
I
sf
| mZ  | ×I +R I |     |     |     |     |
| --- | ------- | --- | --- | --- | --- |
| = L | sf f f  |     |     |     |     |
I
|     | sf   |     |     |     | (17)  |
| --- | ---- | --- | --- | --- | ----- |
 I 
| =mZ | +R f |     |     |     |     |
| --- | ---- | --- | --- | --- | --- |
   
| L   | f I |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
 sf 
=mZ +R
k
| L   | f s |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
where
V Gf   is the voltage at bus G during the fault
I   is the current from bus G to the fault
sf
I is the total fault current
f
| k s  is the ratio of I | f  and I | sf   |     |     |     |
| ---------------------- | -------- | ---- | --- | --- | --- |
Z is the total line impedance
L
m  is the distance of the fault from bus G as a fraction of the line length
is the fault resistance
R f
The ratio of the fault current, I , and the current at the relay location, I , describes the effect of infeed from
|     |     | f   | sf  |     |     |
| --- | --- | --- | --- | --- | --- |
the remote terminal to the fault on the apparent impedance seen by a distance relay. Generally, the effect of
the remote infeed magnifies the apparent resistance of the fault, because I  is always larger than or equal to
f
I .
sf
The effect of remote infeed not only increases the apparent resistance of the fault, it may also change the
angle of the apparent fault impedance. If k  is a complex number, the fault resistance appears as an
s
impedance with a reactive component that can be inductive or capacitive depending on the argument of k .
s
This argument is zero if the currents I  and I  are in phase. This is the case if the infeed fault current from
sf f
the remote source, I , is either zero or is in phase with the relay current, I . The influence of the sign of the
|     | rf  |     | sf  |     |     |
| --- | --- | --- | --- | --- | --- |
argument of k  on the measured impedance is shown in Figure 71. A large value of fault resistance causes
s
the relay at terminal G to sense a fault that should be within the reach of the relay as a fault outside the
reach of the relay. The relay may operate incorrectly if the argument of k  is negative and the fault is
s
outside the reach in the forward direction.
107
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
jX
H
R for (k ) > 0
f s
R for (k ) = 0
f s
R for (k ) < 0
f s
R
G
Figure 71 —Influence of remote infeed on distance measurement
6.7.2.5 Influence of fault resistance and load on the quadrature-polarized mho characteristic
The impact of the combined effect of load and fault resistance on the operation of distance relays depends
on the relay characteristic. An example of a typical quadrature-polarized ground distance mho unit is
analyzed for a phase A-to-ground fault to illustrate this phenomenon. The operating characteristics for load
and no-load cases are shown in Figure 72. The operating and polarizing signals for a phase comparator unit
that operates when the operating signal lags the polarizing signal by 90° to 270° are given by Equation (18)
and Equation (19), respectively.
 Z −Z 
V =V −I + L0 L1I Z (18)
OP Gfa  Gfa Z Gf0  C
L1
V = jV (19)
POL Gbc
where
I is the phase A current flowing from bus G to the fault
Gfa
I is the zero-sequence current flowing from bus G to the fault
Gf0
V is the phase A voltage at bus G during the fault
Gfa
V is the phase B to phase C voltage at bus G during the fault
Gbc
Z is the zero-sequence impedance of the line from bus G to bus H
L0
Z is the positive-sequence impedance of the line from bus G to bus H
L1
Z is the impedance setting of the relay
C
j is the operator that advances a phasor by 90°
108
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Z = impedance setting
jX C
H
Z = offset impedance
0S
Z
C
Characteristic
with load
Characteristic
with no load
G
R
Z
0S
L
K
Figure 72 —Influence of load on mho relay characteristic
The operating characteristic of the relay has an offset, represented by impedance GL in Figure 72. The
offset impedance, Z , can be expressed as in Equation (20).
os
2d Z +d Z
Z = s2 s2 s0 s0 (20)
os Z I
2d + L0d + L
s2 Z s2 I
L1 Gf0
where
d is the current distribution factor in the zero-sequence network
s0
d is the current distribution factor in the negative-sequence network
s2
I is the zero-sequence current flowing from bus G to the fault
Gf0
I is the load current flowing from bus G to bus H before the occurrence of the fault
L
Z is the zero-sequence impedance of the line from bus G to bus H
L0
Z is the positive-sequence impedance of the line from bus G to bus H
L1
Z is the zero-sequence impedance of the source
s0
Z is the negative-sequence impedance of the source
s2
The distribution factors represent the ratio of the change in the current at the relay caused by the fault (fault
current minus the prefault load current) to the total fault current.
The characteristic increases with increase of the source impedances that adjusts the characteristic to larger
fault resistance. The characteristic also depends on the load current, I . In Figure 72, the no-load case
L
109
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
(I = 0) is compared to the load case. The characteristic for the no-load case is represented by the distance
L
from point G to point K.
6.7.2.6 High-resistance faults
Fault resistance is usually small in the case of phase-to-phase faults. On the other hand, ground faults
usually introduce high resistance in the fault loop. The most common faults on overhead lines are ground
faults that are caused by flashover of an insulator. The fault loop for ground faults includes tower
impedance, tower footing resistance, and arc resistance. Tower footing resistance can vary from less than
1 Ω to several hundred ohms. This is discussed in detail in 5.11.
The fault resistance may be particularly large in the case of tree contacts and conductors lying on the
ground. The problem with tree contacts may be reduced by appropriate maintenance of the transmission
lines. Distance relays cannot be set sensitive enough to detect these high-resistance faults. For this reason,
sensitive ground overcurrent relays are used.
Arc resistance depends on the magnitude of fault current and the length of the arc. The resistance is
inversely proportional to a function of the current magnitude and directly proportionally to a function of the
arc length. Since the length of the arc varies with time due to wind and magnetic forces, it is difficult to
estimate the maximum length; the minimum length is sometimes assumed to be the distance between
conductors or from a conductor to the nearest location of the supporting structure.
Various references, such as Elmore’s Protective Relaying Theory and Applications [B26], Mason’s The Art
and Science of Protective Relaying [B84], and GEC Alsthom’s Protective Relays Application Guide [B92],
give different formulas to calculate the arc resistance. The following two formulas have been derived from
the noted references and converted to metric units. Blackburn [B12] and Elmore [B26] give the arc voltage
of 440 V/ft for currents in excess of 100 A; this leads to Equation (21).
L
R =1444 (21)
arc I
where
I is the current in the arc in amperes
L is the estimated length of the arc in meters
R is the resistance of the arc in ohms
arc
1444 is a constant in volts per meter length of the arc
Mason [B84] gives an identical equation that gives an arc voltage of 550 V/ft for currents in excess of
1000 A. This leads to Equation (22) after a conversion to metric units, where the new constant is 1804 V/m
length of the arc.
L
R =1804 (22)
arc I
These two examples demonstrate that no exact formula exists for calculating arc resistance per unit length
of the arc. This is not a severe limitation, because there is also no precise method of determining arc length
(outside of laboratory conditions). A conservative approach would be to make generous assumptions about
arc length and use a formula that gives maximum resistance for the assumed length.
110
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.7.3 Possible loss of directionality on external phase-to-phase-to-ground faults
Zero-sequence current compensation in the operating quantity of ground distance relays is used to allow the
ground distance relay to measure the positive-sequence impedance of the line from the relay location to the
fault. However, this zero-sequence current compensation factor can cause misoperation of the forward-
looking element of the unfaulted phase during an external double line-to-ground fault [B3].
Consider the three-terminal line application shown in Figure 73. Although the three-terminal example is
shown, this issue applies to two-terminal lines as well.
|     | Bus A |     |     |     |     | Bus B |     |     |
| --- | ----- | --- | --- | --- | --- | ----- | --- | --- |
BCG
Protected Line
|     | CB 1 CB 2 |  = 6.0 ∠86o  Z |     |  = 18.0 ∠76o |     | CB 3 |     |     |
| --- | --------- | -------------- | --- | ------------ | --- | ---- | --- | --- |
Z
| E   |     | 1                                |     | 0   |     |     |     | E   |
| --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
| 1   |     | Line Tap 90% from Bus A to Bus B |     |     |     |     |     | 2   |
CB 4
Z  = 1.0 ∠ 90o
| 1   |     |     |     |     |     | CB 5 | Z  = 6.0 ∠ 87o |     |
| --- | --- | --- | --- | --- | --- | ---- | -------------- | --- |
1
| Z   |  = 1.0 ∠ 90o |     |     |     | Bus C |     |                 |     |
| --- | ------------ | --- | --- | --- | ----- | --- | --------------- | --- |
| 0   |              |     |     |     |       |     | Z  = 18.0 ∠ 76o |     |
0
 = 1.0 ∠ 88o
| E   |  = 67 V ∠ 0o |     |     | Z 1 |     | CB 6 |  = 67V ∠ 0o |     |
| --- | ------------ | --- | --- | --- | --- | ---- | ----------- | --- |
| 1   |              |     |     |     |     |      | E           |     |
2
 = 2.0 ∠ 85o
Z 0
E
|     |     |     |     | E  = 67 V ∠ 0o |     | 3   |     |     |
| --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
|     |     |     |     | 3              |     |     |     |     |
Figure 73 —External phases B and C to ground fault on a three-terminal line
The impedances shown in this figure are in ohms as seen by the relays and the voltages are in volts as seen
by the relays. The currents and voltages at circuit breaker 3 for the external phase B to phase C to ground
fault (BCG) on bus B are shown in Table 7.
Table 7 —Currents and voltages at circuit breaker 3
|     | Sequence currents and voltages  |                      |         |     | Phase voltages and currents  |            |     |     |
| --- | ------------------------------- | -------------------- | ------- | --- | ---------------------------- | ---------- | --- | --- |
|     |                                 | I  = 26.6 A          |  93°    |     | I  =0.3 A                    |  −96°      |     |     |
|     |                                 | 1                    |         |     | A                            |            |     |     |
|     |                                 | I  = 19.1 A          |  −89°   |     | I  = 42.5 A                  |  −13°      |     |     |
|     |                                 | 2                    |         |     | B                            |            |     |     |
|     |                                 | I  = 7.8 A           | ∠ −81°  |     | I  = 40.0 A ∠ −161°          |            |     |     |
|     |                                 | 0                    |         |     | C                            |            |     |     |
|     |                                 |  = 28.0 V ∠ −1.3°    |         |     |  = 84.0 V∠                   |            |     |     |
|     |                                 | V 1                  |         |     | V AG                         |  −1.3°     |     |     |
|     |                                 |  = 28.0 V∠           |         |     |                              |  = 0.0 V∠  |     |     |
|     |                                 | V                    |  −1.3°  |     | V                            |  0°        |     |     |
|     |                                 | 2  = 28.0 V ∠ −1.3°  |         |     | BG                           |  = 0.0 V∠  |     |     |
|     |                                 | V                    |         |     | V                            |  0°        |     |     |
|     |                                 | 0                    |         |     | CG                           |            |     |     |
|     |                                 |                      | ∠       |     |                              | ∠          |     |     |
|     |                                 |                      | ∠       |     |                              | ∠          |     |     |
The  operating  and  polarizing  signals  for  a  typical  ground-mho-distance  relay  can  be  expressed  by
Equation (23) and Equation (24):
| V =  | I Z +k I Z  | −V   |     |     |     |     |     | (23)  |
| ---- | ----------- | ---- | --- | --- | --- | --- | --- | ----- |
| OP   | A R1 0 0 R0 | AG   |     |     |     |     |     |       |
| V =V |             |      |     |     |     |     |     | (24)  |
POL AG
where
| I , I | , and I    are the phase A, phase B, and phase C currents, respectively  |     |     |     |     |     |     |     |
| ----- | ------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| A B   | C                                                                        |     |     |     |     |     |     |     |
I 1 , I 2 , and I 0    are the positive-, negative-, and zero-sequence currents, respectively
| V , V | , and V   are the phase A, phase B, and phase C voltages, respectively  |     |     |     |     |     |     |     |
| ----- | ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| A     | B C                                                                     |     |     |     |     |     |     |     |
V , V , and V   are the positive-, negative-, and zero-sequence voltages, respectively
| 1    | 2 0                                                      |     |     |     |     |     |     |     |
| ---- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Z    | is the positive-sequence impedance setting of the relay  |     |     |     |     |     |     |     |
R1
| Z    | is the zero-sequence setting of the relay  |     |     |     |     |     |     |     |
| ---- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
R0
k    is the zero-sequence current compensation factor for the mho function (k  = Z / Z )
| 0   |     |     |     |     |     |     | 0   | R0 R1 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- |
111
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
The voltage phasors that form the operating signal for a phase A mho-ground-distance relay (at CB 3 in
Figure 73) are shown in Figure 74 when the positive sequence reach of the relay is set at 6 Ω. The
polarizing signal, V = 67 0°, is assumed to be equal to the pre-fault value of V . Note that the
POL AG
magnitude of k I Z is larger than that of the restraint voltage V and, therefore, this unit will operate.
0 0 R0 AG
∠
(I Z ) = 1.8 V ∠ −11°
A R1
Magnified View
−V
AG
V
POL
k I Z
0 0 R0
OPERATING SIGNAL
Figure 74 —Operating signal for external phase B- and phase C-to-ground fault
on a three-terminal line
For the conditions of this example, the positive sequence impedance reach of the function is set to only
100% of the positive sequence impedance of the protected line. This setting is unrealistically short for an
overreaching distance function. The choice of the polarizing signal for the ground distance relay has little
effect on performance of the relay in this situation. Other means, therefore, are needed to prevent incorrect
112
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
operation. For example, a ground-directional relay may be used to supervise the mho relay. Also, all three
ground distance elements may be blocked from operating for multiphase faults if two or more ground
distance elements assert. This would then leave the phase distance elements, which do not overreach on
multiphase faults, to operate.
6.7.4 Consideration of voltage transfer for distance relays
Bus arrangements, such as double-bus or breaker-and-a-half, may use a transfer scheme that switches the
potential source from one bus to the other for the relays on a line. The transfer scheme may be automatic or
manual. Distance relays that lose their voltage source during a transfer operation should remain secure
during the transfer.
The security of the relays could be maintained by using current supervision functions, with the current level
detector set above load current, or by using loss-of-potential (LOP) logic. When relying on LOP logic, the
user should ascertain that the relay logic will correctly respond to the three-phase loss of potential and
block tripping during a manual transfer. If an automatic transfer scheme is used, the user should also
ascertain the LOP logic responds correctly, remembering that a fault may have caused the low-voltage
initiating the transfer and the fault may or may not be in the protection zone of the relay.
6.7.5 Loss of voltage
Loss of voltage can occur due to blown VT fuse(s) and depressed voltage due to close-in faults. These
issues are discussed in this clause.
A PSRC report, “Loss of ac voltage considerations for line protection,” further discusses this voltage topic
[B41].
6.7.6 Role of directional ground overcurrent protection used in conjunction with ground
distance relays
Directional ground overcurrent protection may be applied for backup protection to impedance relays and
sometimes specifically to provide sensitive protection for ground faults. The inclusion of zero-sequence
instantaneous units, within most applications of direction-comparison pilot schemes, provides excellent
sensitivity without having to be concerned about faults beyond the protected line. However, when pilot
relaying is not available, the directional ground overcurrent protection setting should take into account
various causes for zero-sequence current flow in transmission lines, such as zero-sequence currents due to
load and system unbalance. Setting levels should be a compromise between security against undesirable
trips for system unbalances and dependability of tripping all faults on the protected line.
The coordination of all elements that are used in a protection scheme must be checked against each other.
This checking is easier when only one type of element is used. However, most protection schemes use a
combination of definite-time and time-overcurrent functions that include both impedance and overcurrent
elements. The use of time-current plots can be useful to determine coordination, especially for definite-time
and time-overcurrent elements. However, impedance elements are not generally plotted with overcurrent
curves but must be considered in overall coordination. Therefore, a secure approach would be to do the
following items:
 Coordinate the overcurrent elements at the local terminal with the distance elements at the remote
terminal.
 Coordinate the overcurrent elements at the local terminal with the overcurrent elements at the
remote terminal.
113
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
 Coordinate the distance elements at the local terminal with the distance elements at the remote
terminal.
 Coordinate the distance elements at the local terminal with the overcurrent elements at the remote
terminal
A PSRC report, “Transmission line applications of directional ground overcurrent relays,” further discusses
this topic [B51].
6.8 Relay considerations for series-compensated lines
6.8.1 General
Series capacitors are applied to improve stability, provide better load division on parallel transmission
paths, reduce transmission losses, reduce voltage drop on severe system disturbances, or increase power
transfer capability, as discussed by Jancke, Fahlen, and Nerf [B72]. The impedance of a series capacitor
usually varies between 25% and 75% of the line impedance. The capacitors may be installed at one end of
the line, both ends of the line, or somewhere in the middle of the line.
Overvoltage protection is provided on the capacitor bank. This protection consists of a parallel air gap
and/or an MOV [B19]. The purpose of this protection is to limit the voltage across the capacitor bank
during faults or excessive load currents so that the capacitors are not damaged. A bypass breaker may also
be used in the design for protecting the air gap and/or the MOV from prolonged exposure to excessive
current flows, as well as to provide flexibility to the operating personnel. Detailed information on
protection of series-capacitor banks is provided in IEEE Std C37.116 [B66].
Line-protection schemes should take into consideration the possibility of air gap or MOV failure,
unsymmetrical gap-flashing, or MOV conduction, as discussed by Alexander et al. [B5] and by Andersson
and Elmore [B7]. Current differential and phase comparison protection schemes generally work properly
when applied to series-compensated lines. Allowing for the line-charging currents may result in reduced
sensitivity of the relay unless the relay includes features to compensate for line-charging currents. Since the
series-compensated lines are usually long and heavily loaded lines, the phase relationship of currents at the
two terminals should be evaluated carefully for determining the relay settings.
Special care should be taken in choosing and setting distance relays, as discussed by Marttila [B83],
because the impedance of the protected line is modified by the series capacitor and varies depending on the
state of the air gap and/or MOV conduction. However, the effects of the series capacitors are not limited to
the power system frequency. The effects of the series capacitors on other relays in the nearby system
should also be considered, even though they are not applied directly on a series-compensated line.
6.8.2 Current inversion
A current inversion is where the current is somewhat inverted in phase angle from where it would be
otherwise if the circuit were primarily inductive. This condition occurs when the current for an internal
fault appears to be entering at one end of the line and leaving at the other end. This can happen for a fault at
location 2 shown in Figure 75 if the source reactance, X , is less than the capacitive impedance, X . This
A C
may be an impractical condition for a bolted fault because the large fault current would ensure rapid
bypassing of the capacitors. However, in the case of a single-line-to-ground fault with large values of fault
resistance, the fault impedance can reduce the fault current below the bypass level. A current inversion can
affect the performance of both distance protection and phase comparison protection. It is preferable, from a
protection point of view, for the series capacitor size and location to be selected such that X is always
A
larger than X . Locating the series capacitor some distance away from the line terminal reduces the
C
probability of X becoming less than X .
A C
114
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
|     |     | 1   | Protective Gap |     | 3   |     | (a) |
| --- | --- | --- | -------------- | --- | --- | --- | --- |
| A   |     |     |                |     |     | B   |     |
X  = Source
|     | X A |     |     | X L | X B |     | A              |
| --- | --- | --- | --- | --- | --- | --- | -------------- |
|     |     |     | 2   |     |     |     | Impedance at A |
X B  = Source
Impedance at B
| V   |     |     |     |     |     | V   |                 |
| --- | --- | --- | --- | --- | --- | --- | --------------- |
| A   |     |     |     |     |     | B   | X  = Capacitor  |
C
Impedance
X L  = Line Impedance
|     |     | V   | V   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | r1  | r2  |     |     |     |     |
(b)
| V   |     |     |     |     |     | V   |                    |
| --- | --- | --- | --- | --- | --- | --- | ------------------ |
| A   |     |     |     |     |     | B   | Positive Sequence  |
Voltage Profile for
a 3 phase fault at 2
| A   |     | V   |     |     |     | B   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
r1
(c)
| V   |     |     |     |     |     | V   | Positive Sequence  |
| --- | --- | --- | --- | --- | --- | --- | ------------------ |
| A   |     |     |     |     |     | B   |                    |
Voltage Profile for
a 3 phase fault at 1
V r2
| A   |     |     |     |     |     | B   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
(d)
|     |     |     | V r2 |     |     |     | Negative Sequence  |
| --- | --- | --- | ---- | --- | --- | --- | ------------------ |
Voltage Profile for
| A   |     | V   |     |     |     | B   |              |
| --- | --- | --- | --- | --- | --- | --- | ------------ |
|     |     | r1  |     |     | V   |     | a fault at 3 |
3f

Figure 75 —Voltage inversion in a series compensated line
Settings can overcome the issue of current inversion by setting fault detectors in distance schemes or
thresholds in phase comparison schemes above the expected export current level. Current differential relay
schemes generally have no problems, as the differential current is high. Where series compensation is
applied to parallel lines or to back-to-back lines, a greater possibility for inversions exist at different fault
locations.
6.8.3 Voltage inversion
A voltage inversion occurs for a fault near a series capacitor when the voltage from the VTs that supply the
relay is capacitive. As a result, the voltage applied to the relay will be close to 180° out of phase from what
would be considered the “normal” position. Because distance relays are designed to work on inductive
systems, this voltage reversal can have an adverse effect on the relay performance.
Consider the system shown in Figure 75(a) and assume that a distance function is applied at station A,
looking toward station B, and that its potential, V , is supplied from the line side of the series capacitor.
r2
The voltage applied to the relay for a three-phase bus fault at location 1 shown in Figure 75(c), is the drop
across the series capacitor and, consequently, is reversed in phase compared to the phase normally
encountered for forward faults on an inductive system. A phasor diagram for this condition is shown in
Figure 76.
115
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore.  Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
The distance function will operate when the operating quantity (IZ − V) and the polarizing quantity are
substantially in phase. Many distance relays use some degree of memory polarization (shown as prefault
voltage, E, in Figure 76) as well as some degree of actual voltage at the relaying location (V shown in
r2
Figure 76). The duration of memory polarization is normally limited to the time required for an
instantaneous decision as to the direction and location of the fault. It is now apparent that the performance
of a distance relay in the presence of voltage inversion depends on the type of polarization. For instance, if
a relay is polarized with memory of full prefault voltage in combination with actual relay voltage and has a
finite memory time, the following two conditions should be noted:
a) The polarizing voltage is initially in phase with the source voltage, E, if the memory voltage is
larger than the actual relay voltage. The distance relay will not operate in this case as long as the
memory voltage lasts.
b) On the expiry of the memory time, the polarizing voltage becomes equal to the applied voltage, and
the distance function operates.
A similar condition can occur for an internal fault at location 2 shown in Figure 75(b) when the relay is
supplied potential V from the bus side of the series capacitors. The following two conditions should again
r1
be noted:
a) The polarizing voltage is initially in phase with the operating quantity (IZ − V) because of the
memory. For this condition, the distance function operates as long as the memory voltage lasts.
b) After the expiry of the memory time, the polarizing voltage becomes equal to the applied voltage,
and the distance functions do not operate anymore.
A voltage reversal can also occur in the zero- and negative-sequence networks if the net impedance from
the location from where the relay receives the voltage back to the source is capacitive. Consider the system
in Figure 75(a). For a single-line -to-ground fault at location 3, the negative- and zero-sequence voltages at
location 2, from which the relay receives the potential, are reversed if the source reactance is less than the
reactance of the series capacitor. Figure 75(d) shows the voltage profile for the negative-sequence network,
assuming that X is less than X . A negative-sequence directional function using that potential and looking
A C
toward station B would not operate correctly for this condition because of the voltage reversal. The
directional function can be designed with compensating features to overcome the effects of voltage reversal
so that the relay operates properly for these conditions.
The voltage on the bus side of the capacitor is not reversed; hence, a directional function that uses the bus-
side potential operates correctly for this condition. However, for a single-line-to-ground fault at location 2,
the potential on the bus side of the series capacitor will be reversed and, therefore, an uncompensated
directional function at that location will not operate properly. However, a relay with a compensated
function operates correctly. The difficulties in ensuring the correct response of directional functions
illustrate another difficulty in protecting systems where X is less than X and reinforce the desirability of
A C
designing the capacitor application such that X is always larger than X .
A C
I
f
IZ
V
r2
E (pre-fault)
IZ − V
Figure 76 —Phasor diagram of the voltage inversion example
116
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.8.4 System transients
The fault current may include a significant transient ac component with a frequency that is determined by
the impedance of the series capacitors and the system inductance. The frequency of this transient is
generally lower than the fundamental frequency of the system, because the value of X is less than the
C
value of total impedance to the fault. In theory, the transient could be higher than the fundamental
frequency fault near location 2 in Figure 75 if X is greater than X ; however, the high currents developed
C A
during a fault on such a system would cause operation of the series capacitor protection. The bypassing of
the series capacitor would preclude the higher frequencies.
A simple approach to setting distance relays on series-compensated lines is to set them based on the
“compensated impedance” of the transmission line. This approach is usually too simplistic because it deals
only with fundamental frequency signals and ignores the effects of the low-frequency transients. The
effects of low-frequency transients on the impedance measured by the distance relay are discussed by
Alexander et al. [B5], Andersson and Elmore [B7], and Mooney et al. [B88]. In Alexander et al. [B5], a
case is presented in which the zone 1 will operate for any reach setting applied to the zone 1 function.
Figure 5 of Andersson and Elmore [B7] shows the transient impedance plot for a compensated line. The
low-frequency transients of a series-compensated system cause the spiraling of the impedance trajectory;
this spiraling, in turn, may cause the zone 1 units to overreach. In Example 1 of Mooney et al. [B88], it is
shown that the zone 1 reach had to be reduced to approximately 50% of the “compensated impedance” in
order to prevent operation due to the low-frequency transients; thus, the setting of the zone 1 function
cannot be based solely on the fundamental frequency “compensated impedance” of the line. The exact
nature of these low-frequency transients varies with the power system and fault location. Transient tests of
protection systems on lines with series compensation, and on lines adjacent to series-compensated lines, are
usually very helpful in ensuring reliable applications and settings. These transient tests should include full
modeling of the transmission system around the capacitor, the series capacitor, and its overvoltage
protection systems so that all relevant transient signals are included in the tests.
6.9 Single-phase tripping and reclosing
6.9.1 General
In a single-phase tripping scheme, only the faulted phase of the transmission line is opened for a single-
line-to-ground fault, while all phases are tripped for any multiphase fault. Two ends of the transmission line
remain connected by two phases when a single-phase-to-ground fault occurs and single-phase tripping
takes place to isolate the fault. The single pole that was tripped would typically reclose after a time delay.
Stability studies typically show that there is improvement in system stability and power transfer capability
when single-phase tripping is applied. Detailed discussions of this subject and the various schemes used to
accomplish single-phase tripping are provided in a PSRC report, “Single phase tripping and auto reclosing
of transmission line” [B47], and Shperling and Fakheri [B96].
Application of single-phase tripping requires attention to a number of details that are not considered for
three-phase tripping schemes, or that need special consideration for single-phase tripping. These include the
following:
 Faulted phase selection
 Arc deionization
 Automatic reclose considerations
 Pole disagreement
 Effects of unbalanced currents
117
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.9.2 Benefits
De-energizing only the affected phase in case of single-phase-to-ground faults on a line while keeping the
two healthy phases connected, preserves—at least partially—system topology that has several benefits.
Some of the benefits are as follows:
 System stability is generally improved by maintaining power transfer capability, even though at a
reduced power level, during the autoreclose dead time.
 Although the three-phase trip remains the worst stability case to be accounted for, consideration of
single-phase tripping and reclosing improves system response, particularly under already reduced
margins or pre-existing contingencies.
 Reclosing from a single-phase trip creates lower power surges for connected generators and
reduces the negative impact on turbine shafts.
 Reclosing from a single-phase trip does not require checking for synchronism to ensure successful
re-connection of parts of the system that approach angular stability limits.
 Switching overvoltages are reduced when single-phase tripping and reclosing is adopted.
These benefits need to be weighed against the increased complexity of single-phase tripping protection
applications, and the capabilities of the installed circuit breakers.
6.9.3 Requirements
Single-phase tripping and reclosing applications impose extra requirements on both circuit breakers and
relays. Circuit breakers need to have mechanisms for implementing single-phase tripping and closing. The
former is achieved by having three independent trip coils and mechanisms controlled individually by the
tripping relays, and the latter is achieved typically by a single close coil that acts toward closing all phases
that are open at the time. In addition, circuit breakers need to report their positions to the tripping relays on
a per phase basis for pole discrepancy protection, open phase detection, and other applications.
Several protective functions need to accommodate the application of single-phase tripping. First, certain
protection functions, such as ground settings, may be exposed to misoperation during single-phase-open
conditions and require special treatment to avoid over-tripping. An equally important issue is that
protection coverage should be maintained for the two phases that remain energized during the single-phase
autoreclose cycle. Certain protection principles, such as directional overcurrent functions or some advanced
distance protection comparators, respond differently to faults superimposed on the pre-existing single-
phase-open condition.
The second issue is that trip commands may be issued by a number of protection functions that lack the
capacity to identify the affected phase or phases. Distance functions may not be perfect in identifying the
affected phase. Therefore, phase selection logic is needed for fast and reliable identification of single-
phase-to-ground faults.
The capability of the circuit breakers to reclose is the third issue. Tripping single-phase with no capabilities
to reclose is not desirable from a long-term power transfer perspective. Alternatively or additionally, pole
discrepancy logic should be used to prevent prolonged single-phase-open condition should the circuit
breaker fail to close or open one phase inadvertently.
The fourth issue is that several auxiliary protection and control functions need to be augmented to support
single-phase tripping and reclosing, such as breaker failure, open-phase detection, LOP, and autoreclosing
functions. The breaker-failure and open-phase-detection functions need to identify failed breaker operations or
open-phase conditions on a per phase basis. The single-phase versions of autoreclosure typically support
elaborate sequences depending on the fault type and shot count. Loss-of-potential detectors may require
blocking from the open-phase function to avoid spurious operation during single-phase autoreclose dead time.
118
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
The fifth issue concerns arc de-ionization and dead time. The timing of the reclose cycle may need to be
lengthened to allow the arc more time to extinguish and allow the system more time to stabilize.
The need for extra control issues for implementing single-phase tripping is the sixth issue. Treatment of the
middle breaker in breaker-and-a-half applications is a good example. Assuming a second fault occurs on a
parallel line during single-phase-open condition after tripping single-phase on the protected line, control
logic should be worked out between the two relays to solve the issue of tripping and reclosing the middle
breaker by the two protection zones that overlap at that breaker.
Due to the numbers and complexity of issues and requirements associated with single-phase tripping and
reclosing, it is strongly discouraged to apply generic line protection relays for single-phase tripping using
programmable logic. Instead, specialized line protection relays developed and tested for the single-phase
operation should be used.
6.9.4 Phase selection issues and techniques
All protection principles, except for the phase-segregated line current differential and phase comparison
schemes, lack the ability to provide reliable phase selection. For example, phase distance comparators
supervising phase A-B and C-A loops may pick up during a phase A-to-ground fault pointing incorrectly to
a double-line-to-ground fault. This is because of the inherent mechanism of distance comparators. This
happens to all generic mho and quadrilateral impedance relays unless extra checks, effectively in a form of
phase selection, are implemented for supervising the impedance loop measurements. Sensitive ground
directional functions responding to sequence quantities, such as negative-sequence overcurrent, or zero-
sequence wattmeter-type directional relays, lack the ability to identify the affected phase(s).
Phase selection logic is either embedded in distance functions or provided as a stand-alone supervising
element detached from the tripping functions. In the latter case, the phase selector can be conveniently used
to supervise any short-circuit protection function configured to trip single phase, including advanced
applications such as single-phase tripping from a weak-infeed logic.
Phase selectors are sensitive and as fast as the protection functions. Phase selection methods tend to be
proprietary solutions with no single dominating approach. Phase selectors often use either symmetrical
components in the line currents or incremental voltages and currents (superimposed components) to meet
the speed and sensitivity requirements.
Evolving faults impose extra requirements on phase selectors and single-phase tripping protection schemes
in general. Correct response under such conditions when the internal and external faults occur
simultaneously or near simultaneously is a technical challenge. Without communication, the remote relay
would indicate a multiphase fault when simultaneous internal and external single-line-to-ground faults
occur and, therefore, would incorrectly trip all three phases. Pilot-aided schemes that use multiple bits for
communication (multiple carrier subchannels) can solve this problem or at least improve accuracy of
single-phase tripping. This is accomplished by allowing the local relay to transmit some amount of extra
information related to the fault type in addition to the plain permission to trip.
6.9.5 Single-phase-open condition
Single-phase-open condition should be considered when engineering single-phase tripping applications.
Dependability requirements demand that tripping functions reach certain buses in either the primary or backup
modes when Single-phase-open conditions occur. For this purpose, short-circuit programs used for calculating
the settings should include provisions for superimposing Single-phase-open conditions and short circuits.
Such requirements may be more difficult to meet compared with three-phase tripping applications.
119
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Traditional distance comparators, such as mho or reactance characteristics, were originally devised
assuming no pre-existing open-phase conditions. With one phase open, these protection functions may
respond unexpectedly to load and short-circuit conditions.
The ground distance relay of the de-energized phase and the relays of the two associated phase-to-phase
loops see low voltage and/or voltage ringing due to the reactors during an open-phase condition when line-
side VTs are used. This could result in nuisance operation of the distance functions during the dead-time
used in single-phase tripping and reclosing. Therefore, as a typical solution, the three impedance loops are
selectively blocked from the open phase detector during the single-phase-open condition.
Significant levels of zero-sequence and negative-sequence currents are present due to the unbalanced power
transfer during the single-phase-open conditions. The voltages measured from line-side VTs also include
significant zero-sequence and negative-sequence voltage components. These unbalanced voltages and
currents are not caused by a short circuit (a shunt unbalance) but may impair the performance of the relay
schemes, such as security, dependability, or both, during the dead-time used in single-phase tripping and
reclosing schemes. The examples of protection functions affected in this manner include reactance line of
the quadrilateral characteristic polarized from the zero- and negative-sequence currents, explicit zero- or
negative-sequence directional supervision of the impedance functions, phase selector designed to respond
to symmetrical currents, and current reversal or switch-off transient logic based on unbalanced currents.
Typically, distance comparators are adjusted in order to maintain secure and dependable performance
during single-phase autoreclosure dead time on detecting the single-phase-open condition.
Polarization for distance functions should take into account the single-phase-open condition. Regardless of
the location of the voltage source (line- or bus-side VTs) one voltage signal is acquired from the point that
is isolated from the two energized conductors of the protected line. This creates inconsistent patterns
between voltages and currents during internal and external faults. For example, during an external ground
fault in the phase that is tripped and yet to be reclosed, the bus voltage may become depressed, with no
phase current measured in the open phase but extra zero-sequence current flowing in the two energized
phases. Or, during three-phase external faults, all three voltages may become symmetrically lowered while
the currents follow a pattern typical for a double-line-to-ground fault.
Ground directional functions such as negative- and zero-sequence directional overcurrent, or zero-sequence
wattmeter type, are affected by open-phase condition and are usually blocked during a single-phase-open
condition. Alternatively, their pickup levels are elevated during the open-phase condition to make sure these
functions respond to a fault and not unbalanced load components. Another solution is to use incremental
(superimposed) components in the symmetrical currents and voltages during open-phase conditions.
Single-phase-open condition affects operation of power swing blocking/out-of-step tripping and load
encroachment elements. These are the two other key functions that are typically based on measuring the
apparent impedance. Either the loop impedances (typically phase loops only) or the positive-sequence
impedances are measured for the purpose of power swing and load encroachment detection. When using
phase loop measurements, two out of three loops should be inhibited because one of the currents and/or
voltages does not signify the actual load on the line. When using the positive-sequence impedances, the
impact depends on the location of the voltage source (use of bus- or line-side VTs). Tripping single phase
shifts the apparent positive-sequence impedance on the impedance plane and may affect the power swing
blocking/out-of-step tripping functions.
Transients associated with shunt reactors provided on the line-side of the circuit breakers and capacitances
of the line play an important role in the performance of distance relays. The discharge voltage waveform is
relatively slowly damped and has a frequency that is only a few hertz lower than the fundamental
frequency. This may create a problem for frequency measurement and tracking/compensation algorithms: a
given relay may track to an inaccurate frequency, which results in lower accuracy of numerical protection
and problems with memory polarization. Often, the ringing voltages are dynamically removed from
frequency calculations during single-phase-open condition.
120
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
An open-phase condition at the remote terminal is a special case to consider; this can happen due to
misoperation of a relay or malfunction of the circuit breaker at the remote terminal. The local relay would
not declare an open phase based on the local information (circuit breaker status and/or current flow) and
would continue to keep all impedance loops operational. This situation, when combined with a reverse
external fault, may lead to a false trip due to the loss of directional integrity caused by the current pattern
resulting from the remote open-phase. Some relay designs attempt to detect the remote open-phase
condition based on the locally available signals. If phase-discrepancy logic is used, this potentially
dangerous condition is typically eliminated.
Detection of the open-phase condition is typically accomplished by monitoring the current and/or circuit
breaker status. Monitoring the current should include provision to cancel the line-charging current for better
sensitivity and accuracy.
Open-phase detectors for dual-breaker terminals need to handle extra conditions. The basic logic calls for a
given phase to be open in both circuit breakers in order to declare this phase open for applications such as
loop-selective blocking of the distance functions. With one circuit breaker out of service, its position is
ignored and the other circuit breaker is considered only as in a single circuit-breaker configuration.
6.9.6 Line-protection methods and single-phase trip initiation
Current-only phase-segregated protection methods such as line current differential and phase comparison
combine the tripping and phase-selection capabilities. They are not affected by evolving faults and could be
used directly for tripping individual phases of the circuit breakers. Mixed-mode current differential or
phase-comparison functions require stand-alone phase selectors.
Distance and ground directional functions call for special treatment when used for single-phase tripping.
This pertains to both phase-selection capabilities and security/dependability during the single-phase-open
time as described in 6.9.5.
As a rule, single-phase tripping is initiated only from instantaneous protection functions, such as pilot-aided
schemes, underreaching zone 1, zone 1 working in a zone extension mode, or high-set overcurrent
functions. Rarely, single-phase tripping is initiated from backup functions, overreaching time-delayed
zone 2 in particular. Zone 2 applications bring only marginal benefits, as the success rate is low when
reclosing after a prolonged fault. Reclosing after tripping in a backup mode is a problematic approach
regardless of whether single- or three-phase trip mode is implemented.
With sensitive current-based or voltage-aided phase selectors, it is possible to initiate single-phase tripping
from weak-infeed protection schemes; i.e., effectively using voltage symptoms for tripping with the
assistance of a communication scheme. Single-phase trip commands are supervised by monitoring the
capacity of the circuit breaker to close. If the breaker is not capable to reclose, single-phase trip requests are
converted into three-phase trip commands.
6.9.7 Autoreclose initiation
Single-phase autoreclosing, in addition to three-phase autoreclosing, is used to improve the chances of
successful reclosures following single- and multiphase faults as well as evolving faults.
A typical autoreclosing scheme supports multiple operating modes, which control the behavior of the
scheme in the following:
 Initiating a single-phase or three-phase operation
 Responding to an evolving fault during the single-phase dead time by tripping three phases or
locking out
 Dynamically adjusting timers depending on the fault type and shot count, etc.
121
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
The following issues review the single-phase and three-phase autoreclosing options:
 Different dead times are required for single-phase and three-phase autoreclosing schemes.
 Typically, single-phase trips call for longer times because the capacitive coupling of the two
energized phases with the faulted phase keep feeding the arc, making it more difficult for the air at
the fault location to de-ionize.
A typical single-phase autoreclosing scheme, for single-phase faults, trips the faulted phase but then trips
all three phases and locks out if the fault evolves to multiphase or if a second fault occurs before the reclose
cycle is complete. Some utilities may choose to trip three phases but continue with the reclose schedule
once the second fault occurs. If, for some multiphase faults, reclosing is desired, then for those faults the
scheme trips three phases and continues with the reclose schedule when the second fault occurs during the
dead time used in the scheme. The selected option depends on the protection philosophy of the utility. The
timers usually are adjusted to account for the occurrence of the second fault if the option of continuing the
autoreclosing procedure is selected.
In breaker-and-a-half and ring bus applications, the middle breaker between two adjacent lines zones
should be treated carefully. It may happen that a circuit breaker is ordered to open a phase following a fault
on one of the lines. A single-phase fault may occur on another line before the autoreclose sequence is
completed. The second fault may call for the circuit breaker to trip a different phase now. This would cause
the problem of when the tripped phases should be closed because only one control is available for closing
all three phases of the circuit breaker. As a result, a convenient solution is to trip all three phases of the
middle circuit breaker when the second single-phase trip command is placed and reclose this circuit breaker
after a successful autoreclosing sequence is finished on both lines.
Single-phase autoreclosing does not require checking for synchronism of the systems connected to the two
terminals of the line. High-speed autoreclosing may also be done without performing a synchrocheck.
Delayed three-phase trip and reclose procedures usually require synchrocheck supervision.
The single-phase autoreclosing scheme may be configured to use a pre-selected terminal to test the line.
The second terminal would check line-side voltage before reclosing. A three-phase trip is initiated and the
autoreclosing is locked out if the voltage does not recover within the set phase-discrepancy timer.
In general, a variety of operating modes and philosophies could be used for reclosing after single-phase
tripping. The schemes are complex and should be carefully studied before they are applied.
6.9.8 Breaker failure consideration
Breaker failure functions need to be specially designed to support single-phase tripping operations. IEEE
Std C37.119 [B67] provides discussion on this topic.
6.10 Application of distance relays to short lines
6.10.1 General
The problems associated with the use of distance relays for protecting short lines can be attributed to the
low voltages available to the distance relay for faults on the line when the SIR is high. Alexander,
Andrichak, and Tyska [B6] and Korejwo, Synal, and Trojal [B75] further discuss this topic.
122
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.10.2 Source-to-line impedance ratio
For a detailed discussion of SIR, see 5.2.
6.10.3 Speed of operation
Figure 77 shows operating speed versus fault location for different SIRs of a typical distance relay. This
figure illustrates the concept that the operating speed of a relay becomes slower as the SIR increases.
Slower speed could make the application of distance relays unacceptable because of power system stability
considerations. The latter would be a problem if the duration for which the memory circuit is effective
becomes shorter than the relay operating time; for example, a line-protection relay could operate for faults
on the bus side of the relay.
Figure 77 —The concept of operating time as a function of fault location
123
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.10.4 Directional integrity
The directional integrity of distance relays when the system voltage is depressed depends on the duration of
the memory circuit; this duration is typically a few cycles of the fundamental frequency. Decreased voltage
reduces the operating speed of the relay, and it is possible that the memory circuit action may expire before
the relay operates.
There are other causes for the reduction of the speed of operation of the relay. Some distance relays
determine the direction of the fault by comparing the phase angles of the operating quantity, say (IZ – V),
and the polarizing quantity, V . These relays could operate for a close-in three-phase fault just behind the
pol
relay if the phase of the polarizing voltage reverses because of the VT transients during this zero-voltage
fault if no memory action is used.
6.10.5 Transient overreach/underreach
A small value of IZ compared to the transient voltage of the CVT for a fault at the limit of relay reach could
cause the relay to underreach (if the CVT output is higher than it should be for a short duration) or
overreach (if the CVT output is lower than it should be for a short duration). An obvious solution to the
underreaching problem is to set the overreaching distance element significantly beyond the protected line in
pilot schemes. This would increase the operating quantity and thus improve the reliability and speed of the
distance-based scheme. Care should be taken to ensure that this extended setting does not cause the relay to
operate under heavy load conditions. One solution to the overreach problem is to shorten the zone 1 reach
of the relays and provide adequate margin for CVT transient voltage. However, many solid-state and
computer-based relays incorporate filters and logic that reduce this problem in most cases.
6.10.6 Minimum settings of distance relays
The problem of low settings of line distance relays is that, for lines that are very short or have a high SIR,
available fault current and voltage at the relay location may not provide adequate operating margins. All
distance relays have minimum settings criteria that should be met for proper operation. The following
concerns should be addressed:
 Impedance characteristic: Minimum fault operating currents should be known; usually, the
shorter the reach setting, the greater is the minimum current required for the relay to operate. The
reach of the relay decreases with lower relay voltages, as is shown in Figure 78, causing the relay to
underreach.
 Directional action: Minimum polarizing voltages should be known. Sensitivities in the range of
1% of rated voltage may be required; however, at this sensitivity, incorrect operations may occur
for reverse faults due to the effect of voltage drop in the arc at the fault.
 Memory action: Memory circuits of the relay are used for low-voltage conditions by supplying a
prefault voltage for polarizing. This circuit may have memory action that lasts only for a few cycles
of the fundamental frequency.
 Operating time: Tripping time may vary with the distance to the fault, relay setting, fault current
magnitude, and the magnitude of relay voltage, prior to the fault. See Figure 79. Usually, the lower
the ratio of the apparent impedance to impedance setting, the faster the operating speed of the relay,
except for low-current conditions. Under conditions of low current, the operating speed of the relay
may actually decrease.
 Maximum torque angle: Cable circuits may have a very small line impedance angle, especially
for pipe-type cables. This may require a maximum torque angle that is not available on the relay
and, thus, necessitate using a different maximum torque angle or using a different impedance
characteristic; for example, using a quadrilateral relay instead of an mho relay.
124
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
 Continuous ampere rating: A user should be aware of the continuous operating characteristics for
a particular setting. It is possible for a setting to violate the continuous ampere rating, especially if
the relay is an electromechanical style.
 CT and VT errors: It is possible for a marginal setting to be unusable because of errors in the CTs
and VTs. CT and VT errors may further reduce the available quantities to the relay where available
system voltages and currents are low.
 Relay settings: Arc impedance should be incorporated in the settings for zone 2 and zone 3 when
mho characteristics are used to protect the line. It may not be possible to increase the zone 1 reach
because of possible overreach beyond the remote terminal, although some relays automatically
adapt to this need.
1.0
0
0 V relay in per unit 0.1
125
Copyright © 2016 IEEE. All rights reserved.
gnittes
yaler
fo
tinu
rep
ni
Z
tnerappa
Figure 78 —Apparent relay reach versus relay voltage
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
I in per unit
relay
126
Copyright © 2016 IEEE. All rights reserved.
emiT
gnitarepO
90% Location of Fault in
50% Percent of Relay Setting
0%
Figure 79 —Variation of operating time with distance to fault
It may be necessary to perform fault studies under minimum conditions to confirm that the relay functions
properly. If the relay does not meet the minimum requirements, alternative relay schemes, such as current
differential, phase comparison, or pilot wire, should be considered.
6.11 Relay considerations for system transients
6.11.1 Nature of transients
Sporadic dampened phenomena occur in electrical systems; these phenomena are generally described as
transients and surges. These two terms are synonymous and interchangeable and are referred to as
“transients” in this clause. The PSRC report, “Distance element response to distorted waveforms,”
discusses the topic of distorted waveforms associated with transients [B38].
Transients that may be dampened oscillatory or may be unidirectional occur when some changes take place
in an electrical circuit, such as the opening or closing of a switch or circuit breaker. Transients may
originate in the primary equipment of a power system, in the secondary control equipment, or in the
instrument transformers connecting the two. This subclause discusses the nature of the transients, their
origin, and their impact on protection systems. The following types of transients are discussed in 6.11.2
through 6.11.5.
 Primary transients: Transients in the primary equipment that are converted faithfully to secondary
circuits by instrument transformers
 Coupled transients: Transients in the primary equipment that influence the secondary control wiring
by inductive or capacitive coupling
 Instrument transformer transients: Transients in the instrument transformers due to the nature of
their performance
 Secondary transients: Transients in the secondary equipment
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.11.2 Primary transients
6.11.2.1 General
The transients in the primary equipment are in several forms, such as dc offset, frequency transients,
asymmetrical breaker phase closing, and transformer inrush.
6.11.2.2 DC offset in the current
When a fault occurs, a dc offset may be present in the current because no instantaneous change of current
can occur in an inductive circuit, and because the current must lag the voltage by the power factor angle of
the system. The dc offset decays with a time constant equal to the L/R ratio of the system supplying the
fault. The magnitude of the initial offset depends on the point on wave at which the fault is initiated.
Figure 80(a) shows a fault current initiated about 30° before a voltage zero crossing, in a system with a
time constant of 100 ms.
Figure 80(b) shows a fault initiated at a voltage zero crossing, in a system with a time constant of 50 ms. It
can be seen that the magnitude of the symmetrical current is the same, while the initial offset is larger, and
the decay rate is faster than in Figure 80(a). This transient is often referred to as “transient dc offset.”
Transient dc offset has the potential to cause overreach of instantaneous line-protection systems. However,
the phenomenon is well understood, and modern line-protection systems are usually designed to effectively
reject the dc component. Otherwise, the manufacturer should be able to provide application instructions to
accommodate its presence by choosing suitable settings. Transient dc offset can also cause transient
saturation of CTs; this is discussed further in 6.11.2.5.
6.11.2.3 DC offset in the voltage
The voltage applied to a line relay may contain a decaying dc component if the source and line impedances
have different L/R ratios. Examples of applications where this effect might be present include a resistance-
grounded system supplying overhead lines, or a source composed of overhead lines supplying a cable
circuit. This dc offset may have some effect on the accuracy of the reach of distance relays and should be
discussed with the relay manufacturer in cases where significant dc offset in the voltage is a possibility.
6.11.2.4 High-frequency transients
These types of transients accompany the energization or short circuit of components containing shunt
capacitance, such as transmission lines, cables, and shunt capacitor banks. These transients are usually in
the kilohertz region and can be removed easily by using filters to ensure that they do not affect the
performance of protection systems. However, the frequency of the transients may approach a few multiples
of the fundamental frequency during disturbances on long EHV and ultra-high voltage (UHV) lines and
may be more difficult to filter out. The filtering causes a delay in the operation of protection systems and,
in some cases the delay may be significant. Protection systems designed for high-speed operation usually
incorporate special designs that reduce the effect of filter delays, as discussed by Ohura et al. [B91] and
Sidhu [B97].
127
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
2.0
1.5
1.0
0.5
0.0
0.1 0.2
-0.5
Time (s)
-1.0
-1.5
Voltage (V) Current (A)
-2.0
(a) Partial offset, T = 100 ms
2.0
1.5
1.0
0.5
0.0
0.1 0.2
-0.5
Time (s)
-1.0
-1.5
Voltage (V) Current (A)
-2.0
(b) Full offset, T = 50 ms
Figure 80 —DC offset in current: (a) half offset, T = 100 ms; (b) full offset, T = 50 ms
6.11.2.5 Low-frequency transients
Transients with a frequency lower than the fundamental frequency of the power system may result from the
effects of series capacitors (more details are given in 6.8) and shunt reactors. Transients that contain
frequencies of the same order of magnitude as fundamental frequency may also occur in systems with high-
voltage cables. Low-frequency transients may require that special filters be used in the protection systems
used in those applications as discussed by Ohura et al. [B91] and Sidhu [B97].
Generator rotor angle oscillations also cause low-frequency transients that may affect protection systems.
6.11.2.6 Asymmetrical breaker phase closing
Asymmetrical closing of circuit breakers may be a result of unavoidable differences in operating time, or as
a deliberate effort to reduce the effects of switching transients. The period of asymmetry is itself a transient
unbalance with fundamental frequency. If the asymmetry exists for an appreciable portion of the operating
time of the protection system, the series unbalance may appear as an unbalanced short circuit, as discussed
by Barnes and McConnell [B9]. This is of particular concern when the asymmetry happens on a circuit
breaker that is closing the second terminal of a transmission line to pick up load, since the unbalance
current may be sufficient to pick up sensitive ground overcurrent relays. Systems used to protect
transmission lines should be designed to accommodate the maximum expected unbalances.
128
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
6.11.2.7 Transformer inrush
Inrush currents flowing into transformers connected as taps on transmission lines contain currents of the
fundamental frequency. These currents are usually lower in magnitude than the fundamental frequency
currents due to a fault on the LV terminals of the transformer. Therefore, if the line-protection system is able
to remain secure for such faults, the transients would not normally result in undesirable operation of the line-
protection system. If the transformer inrush currents contain significant amounts of negative- or zero-sequence
currents, they may cause undesired operation of sensitive overcurrent relays intended to detect high-resistance
ground faults. These ground overcurrent relays may have to be desensitized or restrained by second harmonic
components to override the transformer inrush phenomenon. Inrush currents flowing in to delta-connected
transformer windings do not contain significant levels of zero-sequence currents.
6.11.3 Coupled transients
Protection systems for transmission lines should be designed and installed to operate correctly in the
presence of coupled transients. IEEE Std C37.90.1™ describes tests that ensure a consistent degree of
immunity to such transients for protection systems [B55]. Transient coupling mechanisms, effects, and
mitigation are discussed in more detail in Elmore (Ed.) [B26].
6.11.4 Instrument transformer transients
Conventional line-protection systems primarily use coupling capacitor VTs, CVTs, and wire-wound VTs
and CTs. Applications of nonconventional instrument transformers are not included in this guide.
Wire-wound VTs do not usually produce transients that affect protection systems. However, the secondary
circuit of a CVT contains inductive and capacitive components that, when subjected to a sudden change in
the primary voltage, introduce a dc offset component into the secondary voltage as well as a component
lower than the fundamental frequency. The result of these anomalies can cause the relay to lose directional
integrity, overreach, or respond slower than expected. CVT transients in general reduce the fundamental
component of fault voltage and can cause distance relays to calculate a smaller than actual apparent
impedance to the fault, with potential tendency of overreach for a zone 1 fault. The relay design may be
such as to reject the undesirable transients, or the manufacturer may be able to provide application
instructions to alleviate these effects by the choice of suitable settings. The transient performance of a CVT
is affected by the following factors:
 High or extra-high capacitance CVTs, higher step down transformer ratios, and CVTs with passive
ferroresonance suppression circuits display a better transient response.
 Small resistive burden, found in microprocessor relays, improves the CVT transient response if the
burden on the CVT is predominantly resistive and is not excessive.
 Higher SIR results in worse CVT transients for faults at the same location.
 Fault initiation angle influences the shape of CVT transients, and the resulting transient is worse for
faults at a voltage zero crossing.
The voltage provided by a CVT to a distance relay just after the inception of a fault is less than the voltage
that would have been provided by an ideal VT if it were installed at the relay location. The result is that the
impedance calculated by a numerical relay or interpreted by a solid-state or electromechanical relay is less
than the correct value. Distance relays, therefore, overreach at the inception of a fault. However, the voltage
output of the CVT increases to the true value in about two cycles of the fundamental frequency, and the
impedance seen by the relay becomes close to the true value. Several industry documents discuss CVT
transient response: Conference papers by Hou and Roberts [B34], PSRC report “EHV protection problems”
[B39], PSRC report “Transient response of coupling capacitor voltage transformers” [B49], Ohura et al.
[B91], and Tziouvaras et al. [B106].
129
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
CT transient saturation results in less than ideal reproduction of the primary current. This type of saturation
is caused by fault currents of very high magnitudes combined with high L/R ratios or currents of very low
frequency (such as transient dc offset). Depending on the relay design, CT saturation may result in
undesirable tripping of differential protection systems, underreach of overcurrent or distance relays, or
failure to operate, in extreme cases. CTs should be properly sized to produce sufficiently accurate
secondary currents for the required length of time so that the protection systems may operate correctly.
Figure 81 shows the phasors of polarizing voltage, and I Z used in implementing a self-polarized mho
F S
relay for detecting a fault in its protection zone. The phase angle between the phasors of V and
POL
(I Z − V ) is less than 90° and, therefore, the relay operates. If the CT saturates, its output reduces and
U S POL
the magnitude of the phasor representing the current is now smaller in magnitude than the magnitude of the
phasor when the CT does not saturate. The phase angle of the phasor also changes, but to a much smaller
value. The phase angle between V and (I Z − V ) now becomes greater than 90°, as is shown in
POL S S POL
Figure 81. Therefore, the relay does not operate for a fault in the operating zone of the relay. In other
words, the relay underreaches when CT saturation occurs.
Locus of (IZ ) phasor as I Phasor representing
s F
CT saturates fault current
V Phasor representing
POL
polarizing voltage
Z Replica impedance
s
I Z setting of the relay
u s
I Phasor CT output when
s
CT is not saturated
I Phasor CT output when
u
CT is saturated
θ
s
I Z
s s
θ
u
V
POL
Locus of current phasor
as CT saturates
I
F
Figure 81 —Impact of CT saturation on a self-polarized mho relay
The impact of CT saturation is a risk of underreaching of distance elements for faults near the relay reach
and a minor delay in the operation of the corresponding zone 1 element. However, as the fault location
approaches the relay reach on lines of moderate length, the fault current magnitude decreases, which
reduces the chances of CT saturation. For larger reach, such as zone 2 or zone 3 elements, particularly in
communication-assisted schemes (POTT, DCB, etc.), CT saturation has a limited impact on the final result,
aside from a slight delay in the operating time of the protection system, as discussed by Mooney [B87].
130
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
CT transient performance is discussed in more detail in the IEEE PSRC report, “Transient response of
current transformers” [B50].
6.11.5 Secondary transients
A transient originating in the secondary equipment affects protection systems used to protect transmission
lines to the same extent as most other protection systems. High-magnitude, high-frequency transients can
be generated by the interruption of an inductive current (such as the coil of an auxiliary relay). Such
transients can cause incorrect operation of protection systems, or even damage them. IEEE Std C37.90.1
[B55] describes tests that ensure a consistent degree of immunity of protection systems to such transients.
7. Concluding remarks
Several areas have been improved in this revision, most notably the following:
 Several clauses have been revised for uniformity of style and ease of understanding the issues
discussed in them.
 Enhanced fundamental discussions.
 Better defined the technical discussion about length considerations.
 Updated relay schemes with current technology.
 Added Annex A that describes system studies.
This guide is intended to assist protection engineers and technologists in effectively applying relays and
protection systems to protect transmission lines.
131
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Annex A
(informative)
System studies needed for setting relays
A.1 System studies—General
System studies are a basic calculation tool of the protective relaying engineer. There are two types of
studies: fault studies and special studies. Many utilities perform general fault studies annually and update
them when system changes occur. These are primarily planning studies. Fault studies are an essential tool
for relay engineers as they work toward protecting the system for all faults and abnormal conditions. The
special studies are conducted when relay settings are to be determined or when they are needed to support
system operations.
A.2 Fault study
Fault studies, or short-circuit studies, are developed at the nominal frequency from a load flow where the
system was linearized around an operating point. Fault studies are performed by using software packages.
Preparation of a general fault study is akin to the annual power flow preparation. It is used as the basis for
detailed studies, including screening for overdutied breakers as well as in facility studies when generator
owners petition transmission owners for connection studies. Accurate fault studies depend on short-circuit
models that are continually updated and often compared to actual system faults. For example, if single pole
tripping is applied, then the short-circuit currents with the pole open may be required to be calculated.
Often, the software packages include relational databases that allow the user to catalog and control relay
settings. Additionally, these programs provide graphical outputs for coordination of relays, including time
versus current curves for time overcurrent relays and impedance plots for distance relays.
One necessary function of a fault study program is the calculation of impedances of transmission lines,
transformers, generators, motors, capacitor banks, etc. from system parameters. The user inputs nameplate
data for the equipment and engineering design data for the transmission lines. Transmission engineering
design data includes tower and right-of-way geometries, spacing and tower footing resistances, and often
conductor sag. A positive- and zero-sequence “lumped impedance” model is calculated for the transmission
line. Often, the geometries vary from tower to tower. The relay engineer should input all the necessary
details. The most complicated calculation is the zero-sequence impedance calculation. It is complicated due
to the mutual coupling effect of transmission lines on the same towers and, to a lesser extent, other
transmission lines on the same right-of-way. Often, engineering judgment is used in arriving at the
“lumped” impedance parameters. Another uncertainty is often the differences in the parameters due to
differences between the line “as designed” and “as constructed.” Often, the differences of the parameters of
the line “as constructed” from “as designed” are ascertained by comparing the actual fault data with the
data obtained from fault studies after the line goes into service. It is difficult to develop zero-sequence
models of high-voltage cables. The fault study software may not be able to calculate the zero-sequence
impedance of a pipe-type cable. Zero-sequence impedance for pipe-type cables varies with fault current
flowing on the pipe. Techniques have been presented that do take into account the zero-sequence
impedance for pipe-type cables, as discussed in a 1997 PSRC report, “Protective relaying considerations
for transmission lines with high voltage ac cables” [B45], and Tziouvaras [B103].
There are also difficulties in detailed modeling of transformers in many situations. For example, it may not
be possible to calculate the zero-sequence impedances of four-winding transformers and zero-sequence
models of phase-angle regulating transformers from the nameplate data. In such cases, the relay engineer is
required to work with the designers of the transformer to arrive at a model of a transformer for use in the
132
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
zero-sequence network. Generator data is usually available for an accurate model. Developing models of
large motors, such as synchronous motors, can be a challenge, especially if the subtransient data is not
available or if the motor has been rewound.
A.3 Special studies
Special studies, such as transient stability and load flow studies, are used to help in the application of relays
and relay schemes and determining the relay settings. These studies prove that plans and operations meet
the criteria established by the regulating agencies, such as NERC. These studies are usually done
separately. Data requirements and conservative, worst case assumptions for modeling are different for each
type of study. Transient stability studies, which simulate transient response in the time domain, are useful
for setting breaker failure timing, out-of-step tripping or blocking schemes, and remedial action schemes
(formerly special protection schemes). Load-flow studies are for steady-state analysis and help determine
equipment load-carrying requirements under normal and contingency situations.
133
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
Annex B
(informative)
Bibliography
Bibliographical references are resources that provide additional or helpful material but do not need to be
understood or used to implement this standard. Reference to these resources is made for informational use only.
[B1] Alexander, G. E., and J. G. Andrichak, “Application of phase and ground distance relays to three
terminal lines,” Forty-ninth Annual Texas A&M Protective Relay Conference, Apr. 1996.
[B2] Alexander, G. E., and J. G. Andrichak, “Distance relay fundamentals,” Twenty-third Annual Western
Protective Relay Conference, Oct. 1996.
[B3] Alexander, G. E., and J. G. Andrichak, “Ground distance relaying: Problems and principles,” GER-
3793, General Electric Company Meter and Control Business Department, Malvern, PA, presented at the
Nineteenth Annual Western Protective Relay Conference, Oct. 1991.
[B4] Alexander, G. E., J. G. Andrichak, and S. D. Rowe, “Evaluating line relaying schemes in terms of
speed, security, and dependability,” Twenty-first Annual Western Protective Relay Conference, Oct. 1994.
[B5] Alexander, G. E., J. G. Andrichak, S. D. Rowe, and S. B. Wilkinson, “Series compensated line
protection—A practical evaluation,” Fifteenth Annual Western Protective Relay Conference, Oct. 1988.
[B6] Alexander, G. E., J. G. Andrichak, and W. Z. Tyska, “Relaying short lines,” Eighteenth Annual
Western Protective Relay Conference, Oct. 1991.
[B7] Andersson, F., and W. A. Elmore, “Overview of series-compensated line protection philosophies,”
Seventeenth Annual Western Protective Relay Conference, Washington State University, Pullman, WA,
Oct. 1990.
[B8] Angell, D., D. Arjona, and D. Beaudreau, “Present EHV line protection choices—One utility’s
perspective,” Twenty-first Annual Western Protective Relay Conference, Oct. 1994.
[B9] Barnes, H. C., and A. J. McConnell, “Some utility ground-relay problems,” Transactions of the American
Institute of Electrical Engineers, Power Apparatus and Systems, Part III, vol. 74, no. 3, pp. 417–428, June 1955.
[B10] Benmouyal, G., and S. Chano, “Characterization of phase and amplitude comparators in UHS
directional relays,” IEEE Transactions of Power Systems, vol. 12, no. 2, May 1997.
[B11] Blackburn, J. L., “Ground relay polarization,” Transactions of the American Institute of Electrical
Engineers, Power Apparatus and Systems, Part III, vol. 71, no. 1, Jan. 1952.
[B12] Blackburn, J. L., Protective Relaying: Principles and Applications. New York: Marcel Dekker, Inc.,
1987.
[B13] Bladow, J., and A. Montoya, “Experience with parallel EHV phase shifting transformers,” IEEE
Transactions on Power Delivery, vol. 6, no. 3, pp 1096–1100, July 1991.
[B14] Bolduc, L., “GIC observations and studies in the Hydro-Québec power system,” Journal of
Atmospheric and Solar-Terrestrial Physics, vol. 64, no. 16, pp. 1793–1802, Nov. 2002.
[B15] Cavero, L. P., “Adaptive distance relay characteristics,” Twenty-first Annual Western Protective
Relay Conference, Oct. 1994.
[B16] Chamia, M., and S. Liberman, “Ultra high speed relay for EHV/UHV transmission lines—
Development, design and application,” IEEE Transactions on Power Apparatus and Systems, vol. PAS-97,
no. 6, pp. 2104–2116, Nov./Dec. 1978.
134
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
[B17] Chano, S. R., A. Elneweihi, H. Bilodeau, G. E. Fenner, J. D. Huddleston, III, K. A. Stephan, T. E.
Wiedman, and P. B. Winston, “Static VAr compensator protection,” IEEE Transactions on Power
Delivery, vol. 10, no. 3, pp. 1224–1233, July 1995.
[B18] Cook, V., Analysis of Distance Protection. New York: John Wiley and Sons, Inc., 1985.
[B19] Courts, A. L., N. G. Hingorani, and G. E. Stemler, “A new series capacitor protection scheme using
nonlinear resistors,” IEEE Transactions on Power Apparatus and Systems, vol. 97, no. 4, pp. 1042–1052,
July/Aug. 1978.
[B20] Dierks, A., and J. McElray, “Analyzing polarization of impedance relays,” Fiftieth Annual Georgia
Tech Protective Relay Conference, Atlanta, GA, May 1996.
[B21] Dommel, H. W., and J. M. Michels, “High speed relaying using traveling wave transient analysis,”
IEEE PES Winter Meeting, A78214-9, New York, Jan./Feb. 1978.
[B22] Nishikaware, K. K., D. J. Maratukulam, C. F. Henville, J. E. Drakos, and P. S. Wong, “Back to back
switching of large 230 kV, grounded Y capacitor banks, field tests—Analysis of results and application
guidelines,” Proceedings, CEA, Engineering and Operating Conference, Mar. 1983.
[B23] Dzieduszko, J. W., “Combined-sequence phase comparison relaying,” Twenty-third Annual Western
Protective Relay Conference, Oct. 1996.
[B24] Electrical Transmission and Distribution Reference Book, 4th ed. East Pittsburgh, PA:
Westinghouse Electric Corporation, 1964.
[B25] Elmore, W. A., “The fundamentals of out-of-step relaying,” Thirty-fourth Annual Conference for
Protective Relay Engineers, Texas A&M University, College Station, TX, Apr. 1981.
[B26] Elmore, W. A., Ed. Protective Relaying Theory and Applications. New York, Basel, Hong Kong:
Marcel Dekker, Inc., 1994.
[B27] Elmore, W. A., F. Calero, and L. Yang, L., “Evolution of distance relaying principles,” Forty-eighth
Annual Texas A&M Protective Relay Conference, Apr. 1995.
[B28] Elmore, W. A., and E. D. Price, “Polarizing fundamentals,” Annual Conference for Protective Relay
Engineers, Texas A&M University, College Station, TX, Apr. 2000.
[B29] Engelhardt, K., “EHV shunt reactor protection—Application and experience,” Tenth Annual Western
Protective Relay Conference, Oct. 1983.
[B30] Engler, F., O. E. Lanz, M. Hanggli, and G. Bacchini, “Transient signals and their processing in an
ultra high-speed directional relay for EHV/UHV transmission line protection,” IEEE Transactions on
Power Apparatus and Systems, vol. PAS-104, no. 4, pp. 1463–1473, June 1985.
[B31] Giuliante, A. T., J. E. McConnell, and S. D. Turner, “Considerations for the design and application
of ground distance relays,” Forty-eighth Annual Texas A&M Protective Relay Conference, Apr. 1995.
[B32] Griffin, C.H., “Principles of ground relaying for high voltage and extra high voltage transmission
lines,” IEEE Transactions on Power Apparatus and Systems, vol. PAS-102, no. 2, pp. 420–432, Feb. 1983.
[B33] Henville, C. F., and J. A. Jodice, “Discover relay design and application problems using pseudo-
transient tests,” IEEE Transactions on Power Delivery, vol. 6, no. 4, pp. 1444–1452, Oct. 1991.
[B34] Hou, D., and J. Roberts, “Capacitive voltage transformers: Transient overreach concerns and
solutions,” Twenty-second Annual Western Protective Relay Conference, Oct. 1995.
[B35] IEC 61850, Communication networks and systems in substations.7
7 IEC publications are available from the International Electrotechnical Commission (http://www.iec.ch/). IEC publications are also
available in the United States from the American National Standards Institute (http://www.ansi.org/).
135
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
[B36] IEEE Power System Relaying Committee (PSRC), “Automatic reclosing of transmission lines,”
IEEE Transactions on Power Apparatus and Systems, vol. 103, no. 2, pp. 234–245, Feb. 1984.8, 9
[B37] IEEE Power System Relaying Committee (PSRC), “Considerations in choosing directional
polarizing methods for ground overcurrent elements in line protection applications,” prepared by Working
Group D-3 of the Line Protection Subcommittee, May 2014.
[B38] IEEE Power System Relaying Committee (PSRC), “Distance element response to distorted
waveforms,” prepared by Working Group D25 of the Line Protection Subcommittee, Jan. 2013.
[B39] IEEE Power System Relaying Committee (PSRC), “EHV protection problems,” IEEE Transactions
on Power Apparatus and Systems, vol. 100, no. 5, pp. 2399–2406, May 1981.
[B40] IEEE Power System Relaying Committee (PSRC), “Justifying pilot protection on transmission
lines,” prepared by Working Group D8, Jan. 2008.
[B41] IEEE Power System Relaying Committee (PSRC), “Loss of ac voltage considerations for line
protection,” prepared by Working Group D7 of the Line Protection Subcommittee, 2006.
[B42] IEEE Power System Relaying Committee (PSRC), “Performance of relaying during wide-area
stressed conditions,” prepared by Working Group C12 of the System Protection Subcommittee, May 2008.
[B43] IEEE Power System Relaying Committee (PSRC), “Power swing and out-of-step considerations on
transmission lines,” prepared by Working Group D6 of the Line Protection Subcommittee, July 2005.
[B44] IEEE Power System Relaying Committee (PSRC), “Protection aspects of multi-terminal lines,”
IEEE Special Publication 79TH0056-2-PWR, 1979, reprinted in Protective Relaying for Power Systems,
New York: IEEE Press, 1980.
[B45] IEEE Power System Relaying Committee (PSRC), “Protective relaying considerations for transmission
lines with high voltage ac cables,” IEEE Transactions on Power Delivery, vol. 12, no. 1, pp. 83–96, Jan. 1997.
[B46] IEEE Power System Relaying Committee (PSRC), “Shunt reactor protection practices,” IEEE
Transactions on Power Apparatus and Systems, vol. 103, no. 8, pp 1970–1976, Aug. 1984.
[B47] IEEE Power System Relaying Committee (PSRC), “Single phase tripping and auto reclosing of
transmission lines: IEEE committee report,” IEEE Transactions on Power Delivery, vol. 7, no. 1, pp. 182–
192, Jan. 1992.
[B48] IEEE Power System Relaying Committee (PSRC), “The effects of solar magnetic disturbances on
protective relaying,” IEEE Special Publication 90TH0357-PWR, July 1990.
[B49] IEEE Power System Relaying Committee (PSRC), “Transient response of coupling capacitor voltage
transformers—IEEE committee report,” IEEE Transactions on Power Apparatus and Systems, vol. 100,
no. 12, pp. 4811–4814, Dec. 1981.
[B50] IEEE Power System Relaying Committee (PSRC), “Transient response of current transformers,”
IEEE Transactions on Power Apparatus and Systems, vol. 96, no. 6, Nov./Dec. 1977
[B51] IEEE Power System Relaying Committee (PSRC), “Transmission line applications of directional
ground overcurrent relays,” prepared by Working Group D24 of the Line Protection Subcommittee,
Jan. 2014.
[B52] IEEE Power System Relay Committee (PSRC), “Transmission line protective systems loadability,”
prepared by Working Group D6 of the Line Protection Subcommittee, Mar. 2001.
[B53] IEEE Std 142™, IEEE Recommended Practice for Grounding of Industrial and Commercial Power
Systems.
[B54] IEEE Std 643™, IEEE Guide for Power Line Carrier Applications.
8 IEEE publications are available from the Institute of Electrical and Electronics Engineers (http://standards.ieee.org/).
9 The IEEE standards or products referred to in this clause are trademarks of the Institute of Electrical and Electronics Engineers, Inc.
136
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
[B55] IEEE Std C37.90.1™, IEEE Standard for Surge Withstand Capability (SWC) Tests for Relays and
Relay Systems Associated with Electric Power Apparatus.
[B56] IEEE Std C37.91™, IEEE Guide for Protecting Power Transformers.
[B57] IEEE Std C37.93™, IEEE Guide for Power System Protective Relay Applications of Audio Tones
Over Voice Grade Channels.
[B58] IEEE Std C37.99™, IEEE Guide for the Protection of Shunt Capacitor Banks.
[B59] IEEE Std C37.100™, IEEE Standard Definitions for Power Switchgear.
[B60] IEEE Std C37.102™, IEEE Guide for AC Generator Protection.
[B61] IEEE Std C37.104™, IEEE Guide for Automatic Reclosing of Circuit Breakers for AC Distribution
and Transmission Lines.
[B62] IEEE Std C37.109™, IEEE Guide for the Protection of Shunt Reactors.
[B63] IEEE Std C37.110™, IEEE Guide for the Application of Current Transformers Used for Protective
Relaying Purposes.
[B64] IEEE Std C37.112™, IEEE Standard Inverse-Time Characteristic Equations for Overcurrent Relays.
[B65] IEEE Std C37.113™-1999, IEEE Guide for Protective Relay Applications to Transmission Lines.
[B66] IEEE Std C37.116™, IEEE Guide for Protective Relay Application to Transmission-Line Series
Capacitor Banks.
[B67] IEEE Std C37.119™, IEEE Guide for Breaker Failure Protection of Power Circuit Breakers.
[B68] IEEE Std C37.230™, IEEE Guide for Protective Relay Applications to Distribution Lines.
[B69] IEEE Std C37.234™-2009, IEEE Guide for Protective Relay Applications to Power System Buses.
[B70] IEEE Std C37.243™, IEEE Guide for Application of Digital Line Current Differential Relays Using
Digital Communication.
[B71] IEEE Std C57.13.3™, IEEE Guide for Grounding of Instrument Transformer Secondary Circuits and
Cases.
[B72] Jancke, G., N. Fahlen, and O. Nerf, “Series capacitors in power systems,” IEEE Transactions on
Power Apparatus and Systems, vol. PAS-94, no. 3, pp. 915–925, May/June 1975.
[B73] Johns, T., M. A. Martin, A. Barker, E. P. Walker, and P. A. Crossley, “A new approach to E.H.V.
direction comparison protection using digital signal processing techniques,” IEEE Transactions on Power
Systems, vol. PWRD-1, no. 2, April 1986.
[B74] Kasztenny, B., and R. Perera, “Application considerations when protecting lines with tapped and in-
line transformers,” 2014 67th Annual Conference for Protective Relay Engineers, College Station, TX,
pp. 84–94, Mar. 31–Apr. 3, 2014.
[B75] Korejwo, E., B. Synal, and J. Trojal, “Short HV transmission line protection problems,” IEEE
Second International Conference on Developments in Power System Protection, 1980.
[B76] Kudo, H., H. Sasaki, K. Seo, M. Takahashi, K. Yoshida, and T. Maeda, “Implementation of a digital
distance relay using an interpolated integral solution of a differential equation,” IEEE Transactions on
Power Delivery, vol. 3, no. 4, pp. 1475–1484, Oct. 1988.
[B77] Kumm, J. J., and E. O. Schweitzer, “Statistical comparison and evaluation of pilot protection
schemes,” Twenty-third Annual Western Protective Relay Conference, Oct. 1996.
[B78] Lefrancois, M. J., “Mica 500 kV protection—A segregated phase comparison system with special
features for high tower footing resistance,” Fifth Annual Western Protective Relay Conference, Oct. 1978.
[B79] Mansour, M. M., and G. W. Swift, “A multi-microprocessor based traveling wave relay—Theory
and realization," IEEE Transactions on Power Delivery, vol. PWRD-1, no. 1, pp. 272–279, Jan. 1986.
137
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
[B80] Marttila, R. J., “Directional characteristics of distance relay mho elements: Part I—A new method of
analysis,” IEEE Transactions on Power Apparatus and Systems, vol. PAS-100, no. 1, pp. 96–102,
Jan. 1981.
[B81] Marttila, R. J., “Directional characteristics of distance relay mho elements: Part II—Results,” IEEE
Transactions on Power Apparatus and Systems, vol. PAS-100, no. 1, pp. 103–113, Jan. 1981.
[B82] Marttila, R. J., “Effect of transmission line loading on the performance characteristics of polyphase
distance relay elements,” IEEE Transactions on Power Delivery, vol. 3, no. 4, pp. 1466–1474, Oct. 1988.
[B83] Marttila, R. J., “Performance of distance relay mho elements on MOV-protected series-compensated
transmission lines,” IEEE Transactions on Power Delivery, vol. 7, no. 3, pp. 1167–1178, July 1992.
[B84] Mason, C. R., The Art and Science of Protective Relaying. New York: John Wiley and Sons, Inc.,
1956.
[B85] McCauley, M., D. L. Pelfrey, W. C. Roettger, and C. E. Wood, “The impact of shunt capacitor
installations on Power Circuit breaker application,” IEEE Transactions on Power Apparatus and Systems,
vol. PAS-99, no. 6, pp. 2210–-2222, Nov./Dec. 1980.
[B86] McLaren, P. G., G. W. Swift, Z. Zhang, E. Dirks, R. P. Jayasinghe, and I. Fernando, “A new
directional element for numerical distance relays,” IEEE Transactions on Power Delivery, vol. 10, no. 2,
pp. 666–675, Apr. 1995.
[B87] Mooney, J., “Distance element performance under conditions of CT saturation,” Schweitzer
Engineering Laboratories, 2007.
[B88] Mooney, J. B., D. Hou, C. F. Henville, and F. P. Plumtre, “Computer-based relay models simplify
relay-application studies,” Twentieth Annual Western Protective Relay Conference, Spokane, WA,
Oct. 1993.
[B89] Neher, J. H., and A. J. McConnell, “An improved A-C pilot-wire relay,” Transactions of the
American Institute of Electrical Engineers, vol. 60, no. 1, pp. 12–17, Jan. 1941.
[B90] NERC Standard PRC-023, Transmission Relay Loadability.
[B91] Ohura, Y, T. Matsuda, M. Suzuki, M. Yamamura, Y. Kurosawa, and T. Yokoyama, “Digital distance
relay with improved characteristics against distorted transient waveforms,” IEEE Transactions on Power
Delivery, vol. 4, no. 4, pp. 2025–2031, Oct. 1989.
[B92] Protective Relays Application Guide. Stafford, UK: GEC Alsthom, St. Leonards Works, 1987.
[B93] Redfern, M.A., J. Lopez, and R. O’Gorman, R., “A flexible protection scheme for multi-terminal
transmission lines", IEEE Power Engineering Society General Meeting, vol. 3, pp. 2678–2682. June 2005.
[B94] RUS Bulletin 1724-300, Design Guide for Rural Substations, U.S. Department of Agriculture, Rural
Utilities Service, June 2001.
[B95] Schweitzer, E. O., III., and J. Roberts, “Distance relay element design,” Nineteenth Annual Western
Protective Relay Conference, Oct. 1992.
[B96] Shperling, B. R., and A. Fakheri, “Single-phase switching parameters for untransposed EHV
transmission lines,” IEEE Transactions on Power Apparatus and Systems, vol. PAS-98, no. 2, pp. 643–654,
Apr. 1979.
[B97] Sidhu, T. S., “A microprocessor-based measuring unit for high-speed distance protection,” Canadian
Journal of Electrical and Computer Engineering, vol. 18, no. 3, pp. 117–126, July 1993.
[B98] Soudi, F., P. Tapia, E. A. Taylor, and D. A. Tziouvaras, “Protection of utility/cogeneration
interconnections,” Twentieth Annual Western Protective Relay Conference, Oct. 1993.
[B99] Strang, W. M., “Polarizing sources for directional relaying,” Sixteenth Annual Western Protective
Relay Conference, Texas A&M University, College Station, TX, Oct. 1989.
138
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE Std C37.113-2015
IEEE Guide for Protective Relay Applications to Transmission Lines
[B100] Taylor, E. R., Jr., I. A. Whyte, M. B. Brennen, and J. J. Bonk, “Static VAR generator application
and protection considerations,” Thirty-fourth Annual Texas A&M Relay Conference, Apr. 1981.
[B101] Thompson, M. J., and A. Somani, A., “A tutorial on calculating source impedance ratios for
determining line length,” 2015 68th Annual Conference for Protective Relay Engineers, College Station,
TX, pp. 833–841, Mar. 30–Apr. 2, 2015.
[B102] Tucker, W., A. Burich, M. Thompson, R. Anne, and S. Vasudevan, “Coordinating dissimilar line
relays in a communications-assisted scheme,” 2014 67th Annual Conference for Protective Relay
Engineers, College Station, TX, pp. 111–124, Apr. 2014.
[B103] Tziouvaras, D. A., “Protection of high-voltage AC cables,” Thirty Second Western Protective
Relay Conference, Oct. 2005.
[B104] Tziouvaras, D. A., H. J. Altuve, and F. Calero, “Protecting mutually coupled transmission lines:
Challenges and solutions,” Proceedings of the 40th Annual Western Protective Relay Conference, Spokane,
WA, Oct. 2013.
[B105] Tziouvaras, D. A., and W. D. Hawbaker “Novel applications of a digital relay with multiple setting
groups,” Proceedings of the Seventeenth Annual Western Protective Relay Conference, Spokane, WA,
Oct. 1990.
[B106] Tziouvaras, D. A., P. McLaren, G. Alexander, D. Dawson, J. Esztergalyos, C. Fromen,
M. Glinkowski, I. Hasenwinkle, M. Kezunovic, L. Kojovic, B. Kotheimer, R. Kuffel, J. Nordstrom, and
S. Zocholl, “Mathematical models for current, voltage, and coupling capacitor voltage transformers,” IEEE
Transactions on Power Delivery, vol. 15, no. 1, pp. 62–72, Jan. 2000.
[B107] Zimmerman, K., and J. B. Mooney, “Comparing directional element performance using field data,”
Eighth Annual Conference for Fault and Disturbance Analysis, Texas A&M University, College Station,
TX, Apr. 1993.
[B108] Zimmerman, K., and D. Roth, “Evaluation of distance and directional relay elements on lines with
power transformers or open-delta VTs,” 32nd Annual Western Protective Relay Conference, Spokane, WA,
Oct. 2005.
139
Copyright © 2016 IEEE. All rights reserved.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.

IEEE
standards.ieee.org
Phone: +1 732 981 0060 Fax: +1 732 562 1571
© IEEE
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on December 10,2016 at 22:27:14 UTC from IEEE Xplore. Restrictions apply.