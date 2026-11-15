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

TODAY: Day 5 — 2026-12-06 (Sunday), working day: False, phases: ['P1'].
WEATHER: overcast, moderate wind, -2..5 °C, site lost day: False.

HAPPENINGS DRAWN BY THE EVENT ENGINE (you must turn each into a concrete, visible description and consequences):
[]

SCRIPTED DELIVERABLES DUE TODAY (must be in day_plan with the given owner; keep folder/area/disc/type/to/dept/mom_kind/attendees as given):
[
{
"day": 5,
"owner": "epc-planning-manager",
"kind": "document",
"title": "Risk Register (Initial)",
"folder": "1/06",
"area": "G000",
"disc": "P",
"type": "&REG",
"notes": "at least 15 risks with probability/impact/mitigation/owner; also append to risk register"
},
{
"day": 5,
"owner": "epc-hse-manager",
"kind": "document",
"title": "Project HSE Management Plan",
"folder": "11/01",
"area": "G000",
"disc": "H",
"type": "&HSE"
}
]

SCHEDULE STATUS (activities active or about to start; id | name | planned start-finish | forecast | % complete):
A020 | Kick-off meeting & team mobilisation | 2026-12-02→2026-12-10 | fc 2026-12-02→2026-12-10 | 82%
A030 | Project Execution Plan & procedures | 2026-12-03→2027-01-15 | fc 2026-12-03→2027-01-15 | 7%
A040 | Baseline schedule L1-L3 & approval | 2026-12-03→2027-01-10 | fc 2026-12-03→2027-01-10 | 28%
A050 | Advance payment guarantee & advance payment | 2026-12-05→2027-01-05 | fc 2026-12-05→2027-01-05 | 3%
A060 | Notice to Proceed | 2026-12-15→2026-12-15 | fc 2026-12-15→2026-12-15 | 0%
A070 | HSE plan | 2026-12-10→2027-01-31 | fc 2026-12-10→2027-01-31 | 0%
A110 | Land allocation confirmation & cadastral passport | 2026-12-15→2027-02-15 | fc 2026-12-15→2027-02-15 | 0%
A120 | Environmental & social approvals (ESIA conditions) | 2026-12-15→2027-03-10 | fc 2026-12-15→2027-03-10 | 0%
A210 | Topographic survey | 2026-12-20→2027-01-25 | fc 2026-12-20→2027-01-25 | 0%
A220 | Geotechnical investigation & report | 2026-12-20→2027-02-20 | fc 2026-12-20→2027-02-20 | 0%
A310 | Design basis report | 2026-12-15→2027-01-20 | fc 2026-12-15→2027-01-20 | 0%
A710 | Subcontracting strategy & prequalification | 2026-12-10→2027-01-31 | fc 2026-12-10→2027-01-31 | 10%

OPEN ITEMS / INBOXES (role → pending items):
{"client-commercial-manager": [{"day": 3, "from": "epc-project-director", "kind": "cc", "ref": "HEL001-L-PM-HEP-QSE-0004", "subject": "Acknowledgement of Nomination of Client Representative (HEL001)", "summary": "copied for information"}], "epc-project-director": [{"day": 4, "from": "epc-scm-lead", "kind": "email", "ref": "D004_epc-scm-lead_Procurement_and_logistics_summary_for_PE", "subject": "Procurement and logistics summary for PEP Rev A", "summary": "Rajan,\n\nOne-page summary for PEP Rev A, from the Procurement Plan and Package List Rev A (folder 4/01):\n\nPackages: 9 supply packages (modules, trackers, inverter stations, BESS, transformer and HV, MV switchgear, cables, SCADA/BoP, OHTL materials) and 4 subcontracts (civil, MMS/tracker installation, electrical, substation/OHTL).\n\nM06 route: RFQ to SunPeak and two alternates on 21 Dec 2026, bids 22 Jan, technical and commercial evaluation to 5 Feb, your approval and QSE/Meridian vendor approval, contract signature 15 Feb 2027. First modules on site 20 Jul 2027 (M09), 206,500 modules in about 335 containers through to 30 Nov 2027.\n\nLogistics and customs: rail from China via Kazakhstan to the Navoi railhead and road to site; European equipment via the Middle Corridor or Turkey. Modules and BESS DDP site, other equipment DAP site. Customs broker to be appointed by 29 Jan 2027; duty and VAT exemption certificates to be confirmed by Thomas and QSE.\n\nKey risk: the 220/33 kV transformer (36-40 weeks) against M10 energisation on 20 Jan 2028. It needs the technical specification from Elena by 18 Dec so that I can issue RFQ on 4 Jan and award on 12 Feb 2027. Late specifications are my main concern for all RFQ dates.\n\nMehmet"}, {"day": 4, "from": "epc-contracts-manager", "kind": "cc", "ref": "HEL001-L-CO-HEP-GOV-0001", "subject": "Construction Permit File - Parallel Lodging with Basic Design Review and Applicable Standards (HEL001)", "summary": "copied for information"}, {"day": 4, "from": "epc-engineering-lead", "kind": "email", "ref": "D004_epc-engineering-lead_PEP_Rev_A_input_-_Engineering_and_design", "subject": "PEP Rev A input - Engineering and design management summary (re REQ-003-epc-proj)", "summary": "Rajan,\n\nBelow is the engineering and design management input for PEP Rev A, consistent with the Engineering Execution Plan and Deliverables List (HEL001-G000-E-&PRC-00001-A) and the review periods agreed at the Kick-off Meeting.\n\n1. DESIGN STAGES\n- Stage 1, Design Basis (A310, 15 Dec 2026 - 20 Jan 2027): site data, grid code requirements, standards, load and climatic criteria, PV/BESS/220 kV basis. Submitted to OWE as a report for review.\n- Stage 2, Basic Design (to M04, 15 Mar 2027): single line diagrams, plant layout (PV1-PV4, BES, PSS, GSS, TL1), DC/AC sizing and energy yield basis, earthing and lightning concept, MV/LV cable concept, BESS and substation concept, SCADA architecture, preliminary civil and foundation concept, technical specifications for long-lead packages.\n- Stage 3, Detailed Design (from M04): issued-for-construction drawings and calculations released per area (PV1-PV4, BES, PSS, GSS, TL1) in line with M05 mobilisation (1 Mar 2027) and M08 first piles (12 Apr 2027); piling and foundation packages are released first.\n- Stage 4, Vendor documents and As-Built: vendor drawings and FAT documents reviewed within the same cycle; as-built set compiled progressively and issued before PAC (M14, 31 May 2028).\n\n2. REVIEW CYCLE WITH OWE\n- Drawings, calculations and specifications: 10 working days per OWE review, comments consolidated by Sophie Laurent. Plans and procedures 14 days; RFIs/TQs 5 working days; method statements and ITPs 7 working days.\n- HEP responds to comments within 5 working days and resubmits; a second review is planned at 5 working days. Planning assumption: one full review plus one short re-review per Basic Design package.\n- Deemed-approval wording is to be confirmed by Thomas Becker from the Contract; until then I plan on written approval or Code B/C status only.\n- Document numbering and status codes follow the Document Control and Numbering Procedure; Nilufar Yusupova logs all submissions and review dates in the design document register."}, {"day": 4, "from": "epc-construction-manager", "kind": "email", "ref": "D004_epc-construction-manager_PEP_Rev_A_input_-_Construction_and_site_", "subject": "PEP Rev A input - Construction and site organisation summary", "summary": "Rajan,\n\nIn response to REQ-003-epc-proj, here is the Construction input for PEP Rev A. The one-page summary is registered in 5/01 (Construction and Site Organisation Summary, Rev A). Key points:\n\n1. Mobilisation sequence to M05 (1 March 2027)\n- From 20 Dec 2026: topographic survey and geotechnical investigation (A210, A220), plus survey of the 12 km access track from the A-380. This needs land access from QSE (A110).\n- Jan-Feb 2027: camp units, offices, power, water, welfare ordered or rented; HSE plan issued by Jamshid on 31 Jan; site induction from first access.\n- Feb 2027: access track upgrade, site entrance, laydown set-out, fenced camp zone.\n- 1 Mar 2027 (M05): camp, offices, first aid, security gate and induction point working; core HEP site team on site.\n- March: civil, MMS, electrical and substation subcontractors mobilise in stages. First piles 12 Apr (M08), first modules 20 Jul (M09).\n\n2. Temporary facilities: main camp and offices (HEP, QSE, OWE), separate subcontractor yards, laydown for 206,500 modules, trackers and 28 inverter stations with a controlled receiving point, generator power until grid, tanker water, sanitation, clinic and fire-fighting. No settlements within 6 km, so we plan to be self-sufficient.\n\n3. Working arrangement: Monday to Saturday, day shift in winter, early starts in summer, Sunday rest and maintenance. Sunday work only with my approval and HSE notice. Daily diary, daily toolbox talk, weekly construction report and the Thursday progress meeting.\n\n4. Points I need you to wa

YESTERDAY'S DIARY:
# Day 004 (2026-12-05, Sat)

**Phase(s):** P1  
**Weather:** clear, cold, -2..6 °C  
**Site manpower:** 0  

## Narrative
Day 4 is a cold, clear Saturday. All HELIOS work is still office-based in Tashkent with no presence at the Qizilqum site yet. Helios EPC sets out its commercial and supply strategy: SCM issues the Procurement Plan and Package List, and Contracts issues the Subcontracting Strategy and Prequalification Criteria. Engineering and Construction send their one-page inputs for PEP Rev A to the Project Director ahead of the 7 December deadline.

## What people did
- **Mehmet Yıldız** (Supply Chain Manager): I issued Rev A of the Procurement Plan and Package List with nine supply packages and four subcontracts, with RFQ and award dates, incoterms and the logistics route to Navoi. I sent the vendor lead times and PO dates to Aziz for the baseline L3 (ACTIONS-000-007), a one-page summary to Rajan, and the package list and cargo insurance points to Thomas. The transformer lead time against M10 is my main concern, and I need Elena's specifications by 18 December. _[1 documents, 3 emails, 13 registers, 2 requests]_
- **Thomas Becker** (Contracts & Commercial Manager): I issued Rev A of the Subcontracting Strategy and Prequalification Criteria covering the civil, MMS, electrical and substation/OHTL packages, with back-to-back terms, local content, HSE/QA, financial and bonding criteria. I asked Mehmet Yıldız to align the package list with the Procurement Plan by 9 December before questionnaires go out, and wrote to Shavkat Bobojonov on parallel lodging of the construction permit file (REQ-003). _[1 documents, 1 letters, 1 emails, 2 registers, 1 schedule, 4 requests]_
- **Elena Petrova** (Engineering Manager): I answered Rajan's request REQ-003 with a one-page engineering and design management summary for PEP Rev A, covering design stages, the 10-working-day OWE review cycle and the Basic Design route to M04. I flagged that the geotechnical report (A220, forecast finish 20 February 2027) leaves almost no float to the 15 March Basic Design approval, and asked Planning for a tie into the baseline. _[1 emails, 1 registers, 2 requests]_
- **Sanjay Mehta** (Construction Manager): I put together the one-page construction and site organisation summary for PEP Rev A and sent it to Rajan with the M05 mobilisation sequence, temporary facilities and the Mon-Sat arrangement. I acknowledged Aziz's L3 request and told him subcontractor mobilisation and duration assumptions will follow once the subcontracting strategy is issued. I also asked HSE, Engineering and Contracts for the inputs I need before 1 March. _[1 documents, 2 emails, 2 registers, 3 requests]_

## Files produced
- DOC HEL001-G000-P-&PRC-00001-A Procurement Plan and Package List → project/4_Procurement/01_Procurement_Plan/HEL001-G000-P-&PRC-00001-A_Procurement_Plan_and_Package_List.docx
- DOC HEL001-G000-K-&PRC-00001-A Subcontracting Strategy and Prequalification Criteria → project/14_Subcontr

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