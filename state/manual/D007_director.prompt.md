You are the SIMULATION DIRECTOR of HELIOS, an EPC project simulation. You never appear in documents. Your job today is to
decide what happens on the project and who works on what, so that the project team (AI agents) produce realistic documents.

PROJECT: HELIOS 100 MW Solar PV + BESS Power Plant (HEL001), Qizilqum Solar Site, Navoi Region, Uzbekistan. 100 MWac / 128 MWp PV (4 blocks PV1-PV4, single-axis trackers, 620 Wp modules), BESS 50 MW / 100 MWh, 220 kV grid connection via 9 km OHTL. Site: Flat to gently undulating desert plateau ~45 km north-east of Navoi city, elevation 310-335 m, sandy loam over gypsum-cemented layers, sparse vegetation, no settlements within 6 km. Access via 12 km unpaved track from the A-380 highway. Nearest 220 kV substation 9 km south. CONTRACT: EPC lump-sum turnkey (FIDIC Silver Book 2017 based, amended), USD 95,000,000, signed 2026-12-01 (Day 0), NTP 2026-12-15, advance 10%, retention 5%, delay LDs 0.5%/week capped 10%, time for completion 18 months, PAC target 2028-05-31. PARTIES: EPC Helios EPC LLC (HEP); Client Qizilqum Solar Energy JSC (QSE) — Independent power producer (IPP) SPV owned by a Gulf-based renewable investor and a local partner; holds a 25-year PPA. Owner's Engineer Meridian Energy Consultants (OWE); grid operator UzGridCo (National Electric Grid Operator, fictional) (GRD); authorities Navoi Regional Administration & State Construction Inspectorate (fictional) (GOV). MILESTONES: M00 Contract Signature 2026-12-01; M01 Notice to Proceed 2026-12-15; M02 Kick-off Meeting 2026-12-03; M03 Advance Payment received 2027-01-05; M04 Basic Design approved 2027-03-15; M05 Site Mobilisation 2027-03-01; M06 Module Supply Contract signed 2027-02-15; M07 Construction Permit obtained 2027-03-20; M08 First piles driven 2027-04-12; M09 First module delivery on site 2027-07-20; M10 Plant substation energised 2028-01-20; M11 Grid back-feed / first power 2028-02-15; M12 BESS commissioning complete 2028-04-15; M13 Performance test passed 2028-05-15; M14 Provisional Acceptance (PAC) 2028-05-31. Site works Mon-Sat.

ORGANISATION (role ids → people):
- epc-project-director: Rajan Iyer, Project Director (HEP)
- epc-planning-manager: Aziz Karimov, Planning Manager (HEP)
- epc-planning-engineer-1: Priya Nair, Planning Engineer (HEP)
- epc-planning-engineer-2: Dilnoza Rashidova, Planning Engineer (Procurement & Engineering interface) (HEP)
- epc-scm-lead: Mehmet Yıldız, Supply Chain Manager (HEP)
- epc-buyer: Li Wei, Procurement Engineer / Buyer (HEP)
- epc-engineering-lead: Elena Petrova, Engineering Manager (HEP)
- epc-construction-manager: Sanjay Mehta, Construction Manager (HEP)
- epc-contracts-manager: Thomas Becker, Contracts & Commercial Manager (HEP)
- epc-hse-manager: Jamshid Tursunov, HSE Manager (HEP)
- epc-qaqc-manager: Arun Pillai, QA/QC Manager (HEP)
- epc-document-controller: Nilufar Yusupova, Document Controller (HEP)
- client-project-manager: Khalid Al-Mansoori, Client Project Manager (QSE)
- client-owners-engineer: Sophie Laurent, Owner's Engineer Lead (OWE)
- client-commercial-manager: Omar Hassan, Client Commercial & Contracts Manager (QSE)
- client-site-representative: Bekzod Nazarov, Client Site Representative (QSE)
- sub-civil: Rustam Ergashev, Project Manager (Navoi Qurilish LLC) — Civil works — site clearing, grading, access roads, drainage, fencing, piling, foundations for inverter stations and substation, cable trenches
- sub-mms: Erkin Saidov, Site Manager (SteelPro Montaj LLC) — Mounting structure and tracker installation, module mounting
- sub-electrical: Farrukh Abdullaev, Project Manager (UzElectroMontaj JSC) — DC and AC electrical works — string cabling, combiner boxes, MV cabling, inverter station installation, earthing, SCADA field cabling
- sub-substation: Sergey Volkov, Project Director (GridWorks Central Asia LLP) — 33/220 kV plant substation, 220 kV OHTL (9 km), grid interface works, protection and SCADA
- vendor-modules: Chen Yu, Key Account Manager (SunPeak Solar Technology Co.) — 206,500 PV modules 620 Wp TOPCon bifacial, DDP site
- vendor-inverters: Hans Müller, Project Sales Manager (VoltEdge Power Electronics GmbH) — 28 central inverter stations 3.6 MVA incl. MV transformers and switchgear
- vendor-trackers: Carlos Mendes, Regional Sales Director (AxisTrack Systems S.A.) — Single-axis trackers for 128 MWp incl. piles design support
- vendor-bess: Zhang Min, Project Manager (CellCore Energy Storage Ltd.) — 50 MW / 100 MWh LFP BESS containers, PCS, EMS, DDP site, supervision of installation and commissioning
- grid-operator: Ulugbek Mirzaev, Head of Grid Connections, Navoi Region (UzGridCo (fictional national grid operator)) — Grid connection agreement, grid code compliance, protection coordination, energisation permits
- local-authority: Shavkat Bobojonov, Deputy Head, Construction Supervision (Navoi Regional Administration / State Construction Inspectorate (fictional)) — Construction permit, land allocation confirmation, environmental approvals, customs liaison, inspections

TODAY: Day 7 — 2026-12-08 (Tuesday), working day: True, phases: ['P1'].
WEATHER: rain, partial stoppage, -3..6 °C, site lost day: True.

HAPPENINGS DRAWN BY THE EVENT ENGINE (you must turn each into a concrete, visible description and consequences):
[]

SCRIPTED DELIVERABLES DUE TODAY (must be in day_plan with the given owner; keep folder/area/disc/type/to/dept/mom_kind/attendees as given):
[
{
"day": 7,
"owner": "epc-planning-manager",
"kind": "document",
"title": "Progress Measurement and Reporting Procedure",
"folder": "1/07",
"area": "G000",
"disc": "P",
"type": "&PRC"
},
{
"day": 7,
"owner": "epc-engineering-lead",
"kind": "letter",
"to": "local-authority",
"dept": "EN",
"title": "Request for Topographic and Geotechnical Survey Access and Land Allocation Confirmation"
}
]

SCHEDULE STATUS (activities active or about to start; id | name | planned start-finish | forecast | % complete):
A020 | Kick-off meeting & team mobilisation | 2026-12-02→2026-12-10 | fc 2026-12-02→2026-12-10 | 93%
A030 | Project Execution Plan & procedures | 2026-12-03→2027-01-15 | fc 2026-12-03→2027-01-15 | 45%
A040 | Baseline schedule L1-L3 & approval | 2026-12-03→2027-01-10 | fc 2026-12-03→2027-01-10 | 30%
A050 | Advance payment guarantee & advance payment | 2026-12-05→2027-01-05 | fc 2026-12-05→2027-01-05 | 6%
A060 | Notice to Proceed | 2026-12-15→2026-12-15 | fc 2026-12-15→2026-12-15 | 0%
A070 | HSE plan | 2026-12-10→2027-01-31 | fc 2026-12-10→2027-01-31 | 0%
A110 | Land allocation confirmation & cadastral passport | 2026-12-15→2027-02-15 | fc 2026-12-15→2027-02-15 | 0%
A120 | Environmental & social approvals (ESIA conditions) | 2026-12-15→2027-03-10 | fc 2026-12-15→2027-03-10 | 0%
A210 | Topographic survey | 2026-12-20→2027-01-25 | fc 2026-12-20→2027-01-25 | 0%
A220 | Geotechnical investigation & report | 2026-12-20→2027-02-20 | fc 2026-12-20→2027-02-20 | 0%
A310 | Design basis report | 2026-12-15→2027-01-20 | fc 2026-12-15→2027-01-20 | 0%
A710 | Subcontracting strategy & prequalification | 2026-12-10→2027-01-31 | fc 2026-12-10→2027-01-31 | 10%

OPEN ITEMS / INBOXES (role → pending items):
{"client-commercial-manager": [], "epc-project-director": [], "epc-construction-manager": [{"day": 5, "from": "epc-hse-manager", "kind": "email", "ref": "D005_epc-hse-manager_Project_HSE_Management_Plan_Rev_A_-_earl", "subject": "Project HSE Management Plan Rev A - early-access HSE requirements for survey and geotech crews", "summary": "Dear Sanjay,\n\nThank you for your request for HSE inputs ahead of the 1 March 2027 mobilisation. Rev A of the Project HSE Management Plan is in preparation and will be issued for internal review shortly. Below are the requirements that apply to the survey and geotechnical crews from 20 December 2026, so that your mobilisation sequence can be planned now.\n\n1. Induction: every person must complete the general site induction at the induction point before first access. Crews are inducted before they leave camp or the access gate, and each carries an induction card. No card, no access. Induction is about 60 minutes, in Russian and Uzbek, with English for expatriates.\n\n2. Permit to work: no drilling, excavation or trial pit work starts without a permit. Excavation permits are needed before any trial pit or borehole deeper than 1.2 m, and a service location check is required before any ground penetration.\n\n3. Emergency response and first aid: each survey crew of 10 persons or fewer needs one trained first aider and a first-aid kit in each vehicle. Each vehicle needs radio or satellite communication. The emergency numbers are 103 ambulance, 101 fire and 102 police, and these must be posted at each work area. The medical evacuation route from the work area through the 12 km access track to Navoi needs to be confirmed with you before 20 December.\n\n4. Climate and daily controls: winter temperatures are between -2 and 5 C. Crews need thermal clothing, a heated rest point and wind checks before any work at height or near cranes. Daily pre-start toolbox talks are mandatory and recorded.\n\n5. Traffic: the access track has a 30 km/h speed limit and convoy rules. Drivers must have a valid licence and the vehicle must pass a daily check.\n\nTo close the gap before 1 March, I would be grateful if you could confirm the camp clinic, fire-fighting and induction point arrangements, and the nominated hospital for the emergency route. I will reflect your confirmations in Rev A.\n\nBest regards,\nJ"}, {"day": 5, "from": "epc-hse-manager", "kind": "request", "ref": "REQ-005-epc-hse-", "subject": "Confirm camp clinic, fire-fighting, induction point arrangements and the nominated hospital and medical evacuation route", "summary": "Confirm camp clinic, fire-fighting, induction point arrangements and the nominated hospital and medical evacuation route for the 20 December survey and geotechnical crews (REQ-004-epc-cons), before M05.", "due_day": 10}], "epc-engineering-lead": [{"day": 4, "from": "epc-construction-manager", "kind": "request", "ref": "REQ-004-epc-cons", "subject": "Provide site layout, camp and laydown location constraints and design package timing for the permit file so I can finali", "summary": "Provide site layout, camp and laydown location constraints and design package timing for the permit file so I can finalise the temporary facilities layout.", "due_day": 12}, {"day": 5, "from": "epc-planning-manager", "kind": "request", "ref": "REQ-005-epc-plan", "subject": "Confirm in writing the frozen specification dates for P05 (18 Dec), P02 and P03 (31 Dec), and advise whether a phased ge", "summary": "Confirm in writing the frozen specification dates for P05 (18 Dec), P02 and P03 (31 Dec), and advise whether a phased geotechnical report can be issued by end January 2027.", "due_day": 8}, {"day": 6, "from": "epc-planning-manager", "kind": "request", "ref": "REQ-006-epc-plan", "subject": "Confirm the transformer specification freeze date and the number of 220/33 kV units so that the L3 long-lead logic again", "summary": "Confirm the transformer specification freeze date and the number of 220/33 kV units so that the L3 long-lead logic against M10 can be fixed in the baseline.", "due_day": 9}, {"day": 6, "from": "epc-project-director", "kind": "email", "ref": "D006_epc-project-director_22033_kV_transformer_technical_specifica", "subject": "220/33 kV transformer technical specification required by 18 December", "summary": "Elena,\n\nMehmet has flagged the 220/33 kV transformer as the main schedule risk on the project, and I agree with him. It is R-001 in Aziz's register (score 20). With a 36-40 week manufacturing lead time, a PO on 12 February 2027 gives delivery between 15 November and 15 December 2027. That leaves about five weeks at best before M10 plant substation energisation on 20 January 2028 for installation, testing and commissioning. Every day lost on the specification is a day lost on M10, and we cannot recover it by hurrying the factory.\n\nPlease hold 18 December 2026 for the issued technical specification for the 220/33 kV power transformer. This is an instruction, not a target. Mehmet needs it to issue the RFQ on 4 January 2027 and award on 12 February 2027, and the QSE and Meridian vendor approval step has to fit inside that window.\n\nWhat I need from you:\n1. Confirm by Wednesday 9 December that 18 December is secure, and name who is writing it. If you need input from Sergey Volkov (GridWorks) on the 220 kV interface, from UzGridCo through Thomas on the grid code and protection requirements, or from Aziz on the single line diagram, tell me today so I can chase them myself.\n2. Issue the specification in a form that can go straight to RFQ: rating, vector group, tap changer range, impedance, losses evaluation, cooling, bushings and cable boxes, tests, FAT, transport and delivery to site. Where a value depends on the Basic Design or on the grid operator, state the assumption and the range, and do not wait for the final number. A conditional specification on 18 December is better than a perfect one in January.\n3. Send it to Meridian for early review under

YESTERDAY'S DIARY:
# Day 006 (2026-12-07, Mon)

**Phase(s):** P1  
**Weather:** clear, cold, -5..7 °C  
**Site manpower:** 0  

## Narrative
Day 6 is a cold, clear Monday and the busiest office day of the week so far, with all work still in the Tashkent office and nobody at the Qizilqum site. The PEP Rev A inputs fall due today: Aziz Karimov compiles the comprehensive Project Execution Plan from the engineering, procurement, construction, HSE and risk inputs, and Rajan Iyer reviews and approves it for internal issue. Arun Pillai issues the first revision of the Project Quality Management Plan, and QSE returns its comments on the draft Advance Payment Guarantee and Performance Security forms as agreed at the Kick-off Meeting.

## What people did
- **Aziz Karimov** (Planning Manager): I compiled Project Execution Plan Rev A from the engineering, procurement, construction, HSE and risk inputs received on Days 4-5 and the KOM agreements on reporting, communication and review periods. I built in milestones M00-M14, the L1-L3 baseline approach (A040) and the 220/33 kV transformer long-lead exposure against M10. I sent it to Rajan Iyer for approval and raised A030 progress to 45%. _[1 documents, 1 emails, 1 registers, 1 schedule, 3 requests]_
- **Arun Pillai** (QA/QC Manager): I issued Rev A of the Project Quality Management Plan for HELIOS today, covering the quality policy, organisation, document review interface, design review, vendor surveillance and FAT, ITPs, NCR handling, audits and records handover. I sent the quality section summary to Aziz Karimov for PEP Rev A and answered the HSE and contracts requests on the QMP interfaces. _[1 documents, 3 emails, 2 registers, 1 requests]_
- **Rajan Iyer** (Project Director): I reviewed the PEP Rev A inputs from Mehmet, Elena and Sanjay and the compiled draft from Aziz, and approved it for internal issue with a short list of comments to close by 11 December. I instructed Elena to hold 18 December for the 220/33 kV transformer technical specification, since it drives RFQ on 4 January and the M10 energisation date. _[2 emails, 2 registers, 3 requests]_
- **Omar Hassan** (Client Commercial & Contracts Manager): I returned QSE's comments on the draft Advance Payment Guarantee and Performance Security forms to Thomas Becker by letter today, as the action was due today. I also set out what QSE needs on the issuing bank's rating evidence and the signatory documents, so that the forms can be agreed by 11 December ahead of NTP. _[1 letters, 2 requests]_

## Files produced
- DOC HEL-M-PM-HEP-QSE-04-0A Project Execution Plan → project/1_Project_Mgmt/03_Project_Execution_Plan/HEL-M-PM-HEP-QSE-04-0A_Project_Execution_Plan.docx
- DOC HEL001-G000-Q-&AQA-00001-A Project Quality Management Plan → project/10_Quality_Assurance_and_Control/01_Quality_Management_Plan/HEL001-G000-Q-&AQA-00001-A_Project_Quality_Management_Plan.docx
- LETTER HEL001-L-CO-QSE-HEP-0002 → epc-contracts-manager: QSE Comments on Draft Advance Payment Guarantee and Perfor

OPEN ACTIONS, RFIs, NCRs:
ACTION ACTIONS-000-001 Issue insurance evidence (CAR/EAR, TPL, WC, cargo) to QSE before NTP (owner epc-contracts-manager, due 2026-12-14)
ACTION ACTIONS-000-002 Issue Advance Payment Guarantee (USD 9,500,000) to QSE to protect adva (owner epc-contracts-manager, due 2026-12-22)
ACTION ACTIONS-000-003 Deliver Performance Security per Particular Conditions (28 days from C (owner epc-contracts-manager, due 2026-12-29)
ACTION ACTIONS-000-004 Confirm Client attendees, Client Representative and OE contact for the (owner epc-project-director, due 2026-12-02)
ACTION ACTIONS-000-005 Prepare draft NTP precondition checklist and advance payment guarantee (owner epc-contracts-manager, due 2026-12-03)
ACTION ACTIONS-000-006 Provide WBS, engineering deliverable list and durations for baseline L (owner epc-engineering-lead, due 2026-12-08)
ACTION ACTIONS-000-007 Provide procurement packages, vendor lead times and PO dates for basel (owner epc-scm-lead, due 2026-12-08)
ACTION ACTIONS-001-008 Incorporate Project Director comments in Document Control Procedure re (owner epc-document-controller, due 2026-12-10)
ACTION ACTIONS-001-010 Obtain QSE approval of form and issuing bank confirmation for APG and  (owner epc-contracts-manager, due 2026-12-07)
ACTION ACTIONS-001-011 Present NTP precondition checklist at KOM (owner epc-contracts-manager, due 2026-12-03)
ACTION ACTIONS-001-012 HEP to issue revised KOM agenda including QSE items (reporting format, (owner epc-project-director, due 2026-12-02)
ACTION ACTIONS-001-013 QSE to issue formal Client Representative nomination notice (owner client-project-manager, due 2026-12-04)
ACTION ACT-002-KOM-01 Return QSE comments on draft APG and Performance Security forms (owner client-commercial-manager, due 2026-12-07)
ACTION ACT-002-KOM-02 Confirm acceptability of HEP's proposed issuing bank and rating eviden (owner client-commercial-manager, due 2026-12-09)
ACTION ACT-002-KOM-03 Submit signatory specimen sheet and power of attorney for APG and Perf (owner epc-contracts-manager, due 2026-12-11)
ACTION ACT-002-KOM-04 Issue first L2 draft schedule for OWE sight and submit baseline L1-L3  (owner epc-planning-manager, due 2026-12-21)
ACTION ACT-002-KOM-05 Provide design package timing for the construction permit file and iss (owner epc-engineering-lead, due 2026-12-08)
ACTION ACT-002-KOM-06 Confirm in writing the status of land allocation decree and cadastral  (owner client-project-manager, due 2026-12-10)
ACTION ACT-002-KOM-07 Issue Project Execution Plan Rev A including the agreed reporting form (owner epc-project-director, due 2026-12-15)
ACTION ACT-002-KOM-08 Provide consolidated OWE contact list and review matrix for document r (owner client-owners-engineer, due 2026-12-08)
ACTION ACTIONS-003-026 Confirm permit-file design package durations and issue first design do (owner epc-engineering-lead, due 2026-12-08)
ACTION ACTIONS-004-030 Provide subcontractor mobilisation dates and duration assumptions to P (owner epc-construction-ma

RECENT MEETING MINUTES:
progress report (cut-off last day of month, issued by the 5th) with weekly look-ahead and a one-page dashboard. Agreed structure: summary, progress against baseline (S-curve, planned vs actual), engineering, procurement, construction, HSE, quality, commercial, risks and look-ahead. First report covers December 2026, due 5 January 2027. Weekly progress meeting to be held Thursdays; format to be reflected in the PEP.
- Communication protocol: Agreed: formal correspondence by numbered letter under the HEL001-L-DEPT-FROM-TO scheme, with email used for coordination only and confirmed by letter where it affects scope, time or cost. Single points of contact per party, acknowledgement of letters within 2 working days, and a shared document platform managed by Nilufar Yusupova. Notices under the Contract are sent to the addresses in the Agreement and copied to the project managers.
- Document review periods: QSE and OWE requested review periods. Agreed: 10 working days for engineering drawings, calculations and specifications; 14 days for plans and procedures (PEP, HSE plan, QMP); 5 working days for RFIs and technical queries; 7 working days for method statements and ITPs. Comments to be consolidated by OWE (Sophie Laurent). Deemed-approval wording to be taken from the Contract and confirmed by Thomas Becker. HEP will submit the first design document register by 15 December.
- Early mobilisation, HSE and next steps: Sanjay Mehta outlined mobilisation planning ahead of 1 March 2027 (M05), with site survey and geotechnical investigation (A210, A220) starting from 20 December. Jamshid Tursunov's HSE plan will be issued by 31 January 2027, with a site induction regime from first access. Next weekly progress meeting on 10 December. I closed the meeting at 16:30; ACTIONS-001-011 and ACTIONS-001-012 are closed through the actions below.

Actions:
- Return QSE comments on draft APG and Performance Security forms (owner client-commercial-manager, due 2026-12-07)
- Confirm acceptability of HEP's proposed issuing bank and rating evidence requirements (owner client-commercial-manager, due 2026-12-09)
- Submit signatory specimen sheet and power of attorney for APG and Performance Security, and finalise agreed forms (owner epc-contracts-manager, due 2026-12-11)
- Issue first L2 draft schedule for OWE sight and submit baseline L1-L3 schedule for approval (owner epc-planning-manager, due 2026-12-21)
- Provide design package timing for the construction permit file and issue first design document register (owner epc-engineering-lead, due 2026-12-08)
- Confirm in writing the status of land allocation decree and cadastral passport (A110) (owner client-project-manager, due 2026-12-10)
- Issue Project Execution Plan Rev A including the agreed reporting format, communication protocol and review periods (owner epc-project-director, due 2026-12-15)
- Provide consolidated OWE contact list and review matrix for document review periods (owner client-owners-engineer, due 2026-12-08)


RULES
- Pick 2 to 7 roles to act today (fewer on quiet days; 0-1 on non-working days). Prefer roles with inbox items or scripted deliverables.
- Every must_produce item must be realistic for the phase and for that role. Letters need a to_role (a role id). Documents need folder (e.g. "1/04"), area, disc, type codes.
- Replies: if someone received a letter/request, the recipient should answer within a few days.
- Interpret surprises (kind=surprise) as something that becomes visible today through a report, inspection, letter or notice; list affected activities with slip_days (0 if unknown yet).
- Non-working day: usually empty day_plan; narrative only.
- Site manpower: 0 before mobilisation (~Day 90), ramping to ~900 at peak construction; productivity 1.0 normal, lower on bad weather.
Return ONLY JSON matching the schema.