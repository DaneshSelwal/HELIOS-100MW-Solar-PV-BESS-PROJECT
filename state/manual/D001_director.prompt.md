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

TODAY: Day 1 — 2026-12-02 (Wednesday), working day: True, phases: ['P1'].
WEATHER: clear, cold, 1..9 °C, site lost day: False.

HAPPENINGS DRAWN BY THE EVENT ENGINE (you must turn each into a concrete, visible description and consequences):
[]

SCRIPTED DELIVERABLES DUE TODAY (must be in day_plan with the given owner; keep folder/area/disc/type/to/dept/mom_kind/attendees as given):
[
{
"day": 1,
"owner": "epc-project-director",
"kind": "document",
"title": "Project Charter",
"folder": "1/01",
"area": "G000",
"disc": "P",
"type": "&PRC"
},
{
"day": 1,
"owner": "epc-project-director",
"kind": "document",
"title": "Project Organisation Chart and Responsibility Matrix",
"folder": "1/01",
"area": "G000",
"disc": "P",
"type": "&PRC"
},
{
"day": 1,
"owner": "epc-contracts-manager",
"kind": "letter",
"to": "client-commercial-manager",
"dept": "CM",
"title": "Submission of Advance Payment Guarantee and Performance Security"
}
]

SCHEDULE STATUS (activities active or about to start; id | name | planned start-finish | forecast | % complete):
A020 | Kick-off meeting & team mobilisation | 2026-12-02→2026-12-10 | fc 2026-12-02→2026-12-10 | 0%
A030 | Project Execution Plan & procedures | 2026-12-03→2027-01-15 | fc 2026-12-03→2027-01-15 | 0%
A040 | Baseline schedule L1-L3 & approval | 2026-12-03→2027-01-10 | fc 2026-12-03→2027-01-10 | 0%
A050 | Advance payment guarantee & advance payment | 2026-12-05→2027-01-05 | fc 2026-12-05→2027-01-05 | 0%
A060 | Notice to Proceed | 2026-12-15→2026-12-15 | fc 2026-12-15→2026-12-15 | 0%
A070 | HSE plan | 2026-12-10→2027-01-31 | fc 2026-12-10→2027-01-31 | 0%
A110 | Land allocation confirmation & cadastral passport | 2026-12-15→2027-02-15 | fc 2026-12-15→2027-02-15 | 0%
A120 | Environmental & social approvals (ESIA conditions) | 2026-12-15→2027-03-10 | fc 2026-12-15→2027-03-10 | 0%
A210 | Topographic survey | 2026-12-20→2027-01-25 | fc 2026-12-20→2027-01-25 | 0%
A220 | Geotechnical investigation & report | 2026-12-20→2027-02-20 | fc 2026-12-20→2027-02-20 | 0%
A310 | Design basis report | 2026-12-15→2027-01-20 | fc 2026-12-15→2027-01-20 | 0%
A710 | Subcontracting strategy & prequalification | 2026-12-10→2027-01-31 | fc 2026-12-10→2027-01-31 | 0%

OPEN ITEMS / INBOXES (role → pending items):
{"client-commercial-manager": [{"day": 0, "from": "epc-contracts-manager", "kind": "letter", "ref": "HEL001-L-CO-HEP-QSE-0001", "subject": "HEL001 EPC Contract — Confirmation of Executed Documents and Pre-Commencement Contractual Deliverables", "summary": "Dear Mr Hassan, Thank you and your colleagues for the signing ceremony today, 2026-12-01. We confirm that Helios EPC LLC has received its executed set of the EPC Contract (Agreement, Particular Conditions, Employer's Requirements and Schedules) and request that you confirm the Employer's set is complete and initialled as ours is, so that both parties hold identical controlled copies. For planning purposes, we note the following pre-commencement items: (a) the Kick-off Meeting on 2026-12-03; (b) delivery of the Contractor's insurance evidence before the Notice to Proceed; (c) the Advance Paymen", "due_day": 7}, {"day": 0, "from": "epc-project-director", "kind": "cc", "ref": "HEL001-L-PM-HEP-QSE-0001", "subject": "Confirmation of Contract Signature and Proposal for Kick-off Meeting", "summary": "copied for information"}], "epc-project-director": [{"day": 0, "from": "epc-document-controller", "kind": "cc", "ref": "HEL001-L-PM-HEP-QSE-0002", "subject": "Transmittal of Document Control and Numbering Procedure for review (HEL001)", "summary": "copied for information"}, {"day": 0, "from": "epc-document-controller", "kind": "request", "ref": "REQ-000-epc-docu", "subject": "Please approve the Document Control and Numbering Procedure (rev A, IFA) before it is circulated to QSE and OWE as a for", "summary": "Please approve the Document Control and Numbering Procedure (rev A, IFA) before it is circulated to QSE and OWE as a formal transmittal.", "due_day": 5}, {"day": 0, "from": "epc-planning-manager", "kind": "email", "ref": "D000_epc-planning-manager_Day_0_schedule_status_and_baseline_sched", "subject": "Day 0 schedule status and baseline schedule development plan", "summary": "Rajan,\n\nSchedule status at Day 0 (2026-12-01):\n\n1. A010 Contract signature is marked complete (actual finish 2026-12-01). The tender programme is frozen as Baseline-0 and is the starting point for the L1-L3 baseline (A040). Nothing else has started.\n\n2. The L1-L3 baseline will be submitted to Meridian (Sophie Laurent) for review by 2027-01-10. My development plan with the step dates is filed in 1_Project_Mgmt/04_Schedule.\n\n3. Key near-term dates: KOM on 2026-12-03 (I will present the schedule se"}], "epc-construction-manager": [{"day": 0, "from": "epc-contracts-manager", "kind": "email", "ref": "D000_epc-contracts-manager_HEL001_EPC_Contract_executed_key_terms_s", "subject": "HEL001 EPC Contract executed — key terms summary and notice discipline", "summary": "Colleagues, the EPC Contract was signed today. The Executive Summary and Key Terms is now in the Contracts folder (2/01). Please read Sections 7 and 8 in particular. Rule for everyone: any event that may delay the works, change scope or cost money must be reported to me the same day, in writing, with date, location and photos. The claim notice window is 28 days from awareness and a late notice can cost us the entitlement. I will issue all contractual notices; please do not send contractual state"}, {"day": 0, "from": "epc-project-director", "kind": "email", "ref": "D000_epc-project-director_HELIOS_-_Contract_signed_priorities_to_N", "subject": "HELIOS - Contract signed; priorities to NTP (15 Dec)", "summary": "Team,\n\nThe EPC Contract was signed today, 1 December. Thank you for the work that got us here. Kick-off with QSE and Meridian is proposed for Thursday 3 December in Tashkent; please be ready.\n\nPriorities up to NTP on 15 December:\n1. Aziz: draft Level 1-3 baseline schedule outline for kick-off (A040, approval target 10 Jan). Priya and Dilnoza to support.\n2. Thomas: advance payment guarantee draft with the bank (A050, advance due 5 Jan), NTP precondition checklist, permit and land allocation track"}, {"day": 0, "from": "epc-document-controller", "kind": "email", "ref": "D000_epc-document-controller_Document_numbering_scheme_in_force_from_", "subject": "Document numbering scheme in force from Day 0 (HEL001)", "summary": "Dear colleagues,\n\nThe Document Control and Numbering Procedure is now issued for internal use in the EDMS, pending approval by Rajan Iyer. From today, every document, letter and transmittal for HEL001 must use the numbering format in section 4 and the status codes in section 5. Documents are numbered automatically by the EDMS, so please register each document in the correct folder, area and discipline before you start work on it.\n\nPlease note that the review period in section 6 is provisional un"}], "epc-engineering-lead": [{"day": 0, "from": "epc-contracts-manager", "kind": "email", "ref": "D000_epc-contracts-manager_HEL001_EPC_Contract_executed_key_terms_s", "subject": "HEL001 EPC Contract executed — key terms summary and notice discipline", "summary": "Colleagues, the EPC Contract was signed today. The Executive Summary and Key Terms is now in the Contracts folder (2/01). Please read Sections 7 and 8 in particular. Rule for everyone: any event that may delay the works, change scope or cost money must be reported to me the same day, in writing, with date, location and photos. The claim notice window is 28 days from awareness and a late notice can cost us the entitlement. I will issue all contractual notices; please do not send contractual state"}, {"day": 0, "from": "epc-contracts-manager", "kind": "request", "ref": "REQ-000-epc-cont", "subject": "Provide the list of Employer's Requirements items that carry performance damages or guaranteed values, with clause refer", "summary": "Provide the list of Employer's Requirements items that carry performance damages or guaranteed values, with clause references, for the contract summary and notice tracker.", "due_day": 14}, {"day": 0, "from": "epc-project-director", "kind": "email", "ref": "D000_epc-project-director_HELIOS_-_Contract_s

YESTERDAY'S DIARY:
# Day 000 (2026-12-01, Tue)

**Phase(s):** P1  
**Weather:** heavy rain, earthworks stopped, -3..4 °C — **site lost day**  
**Site manpower:** 0  

## Narrative
Day 0: Helios EPC LLC and Qizilqum Solar Energy JSC sign the USD 95 M lump-sum turnkey EPC Contract for HELIOS (HEL001) in Tashkent this morning. All work is in the office, with no site presence yet. Heavy rain and near-freezing temperatures over the Qizilqum plateau don't matter today, because mobilisation is months away. The EPC home office spends the afternoon on the formal first steps: confirming signature to the Client, setting out the key contract terms for the team, putting document control in place before the first transmittals, and getting the Day 1 baseline ready.

## What people did
- **Thomas Becker** (Contracts & Commercial Manager): I collected the executed EPC Contract at the signing, checked it for initialling and annex completeness, and issued the Executive Summary and Key Terms for the project team. I set out the contractual notice calendar for the first 60 days and wrote to the Client's commercial manager to align on bonds, insurances, NTP and the kick-off. I also asked Finance-facing and engineering colleagues for the inputs I need for the bond and insurance submissions. _[1 documents, 1 letters, 1 emails, 4 registers, 4 requests]_
- **Rajan Iyer** (Project Director): I signed the EPC Contract on behalf of Helios EPC LLC and wrote to Khalid Al-Mansoori confirming execution and proposing the Kick-off Meeting for 3 December at the QSE Tashkent office, with a draft agenda attached. I briefed the HEP core team on the two-week priorities up to NTP on 15 December and asked planning, contracts, engineering, HSE and construction for their inputs. _[1 documents, 1 letters, 1 emails, 2 registers, 1 schedule, 5 requests]_
- **Nilufar Yusupova** (Document Controller): I issued the Document Control and Numbering Procedure (folder 1/07, rev A, IFA) so that numbering, revision, status, transmittal and correspondence rules are in force from Day 0, before the first outgoing letter is numbered. I also registered the outgoing transmittal letter to QSE, copied to the Owner's Engineer and our Project Director and Contracts Manager, and asked the Contracts Manager to confirm the review periods against the EPC Contract. _[1 documents, 1 letters, 1 emails, 2 requests]_
- **Aziz Karimov** (Planning Manager): I closed out A010 Contract signature at 100% and froze the tender programme as the data date 2026-12-01 starting point for the L1-L3 baseline (A040). I wrote the baseline schedule development plan, including the KOM schedule agenda section and the NTP precondition tracking list, and sent Rajan Iyer the Day 0 status email. I asked Mehmet Yildiz and Elena Petrova for WBS and procurement inputs by 2026-12-08. _[1 documents, 1 emails, 4 registers, 1 schedule, 2 requests]_

## Files produced
- DOC HEL001-G000-K-&CON-00001-A EPC Contract — Executive Summary and Key Terms → project/2_Contracts_an

OPEN ACTIONS, RFIs, NCRs:
ACTION ACTIONS-000-001 Issue insurance evidence (CAR/EAR, TPL, WC, cargo) to QSE before NTP (owner epc-contracts-manager, due 2026-12-14)
ACTION ACTIONS-000-002 Issue Advance Payment Guarantee (USD 9,500,000) to QSE to protect adva (owner epc-contracts-manager, due 2026-12-22)
ACTION ACTIONS-000-003 Deliver Performance Security per Particular Conditions (28 days from C (owner epc-contracts-manager, due 2026-12-29)
ACTION ACTIONS-000-004 Confirm Client attendees, Client Representative and OE contact for the (owner epc-project-director, due 2026-12-02)
ACTION ACTIONS-000-005 Prepare draft NTP precondition checklist and advance payment guarantee (owner epc-contracts-manager, due 2026-12-03)
ACTION ACTIONS-000-006 Provide WBS, engineering deliverable list and durations for baseline L (owner epc-engineering-lead, due 2026-12-08)
ACTION ACTIONS-000-007 Provide procurement packages, vendor lead times and PO dates for basel (owner epc-scm-lead, due 2026-12-08)

RULES
- Pick 2 to 7 roles to act today (fewer on quiet days; 0-1 on non-working days). Prefer roles with inbox items or scripted deliverables.
- Every must_produce item must be realistic for the phase and for that role. Letters need a to_role (a role id). Documents need folder (e.g. "1/04"), area, disc, type codes.
- Replies: if someone received a letter/request, the recipient should answer within a few days.
- Interpret surprises (kind=surprise) as something that becomes visible today through a report, inspection, letter or notice; list affected activities with slip_days (0 if unknown yet).
- Non-working day: usually empty day_plan; narrative only.
- Site manpower: 0 before mobilisation (~Day 90), ramping to ~900 at peak construction; productivity 1.0 normal, lower on bad weather.
Return ONLY JSON matching the schema.