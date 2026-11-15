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

TODAY: Day 3 — 2026-12-04 (Friday), working day: True, phases: ['P1'].
WEATHER: clear, cold, -3..4 °C, site lost day: False.

HAPPENINGS DRAWN BY THE EVENT ENGINE (you must turn each into a concrete, visible description and consequences):
[]

SCRIPTED DELIVERABLES DUE TODAY (must be in day_plan with the given owner; keep folder/area/disc/type/to/dept/mom_kind/attendees as given):
[
{
"day": 3,
"owner": "epc-planning-manager",
"kind": "document",
"title": "Level 1 and Level 2 Milestone Schedule (Baseline)",
"folder": "1/04",
"area": "G000",
"disc": "P",
"type": "&SCH",
"notes": "Narrative + milestone table; the L3 xlsx is generated automatically"
},
{
"day": 3,
"owner": "epc-engineering-lead",
"kind": "document",
"title": "Engineering Execution Plan and Deliverables List",
"folder": "3/02",
"area": "G000",
"disc": "E",
"type": "&PRC"
}
]

SCHEDULE STATUS (activities active or about to start; id | name | planned start-finish | forecast | % complete):
A020 | Kick-off meeting & team mobilisation | 2026-12-02→2026-12-10 | fc 2026-12-02→2026-12-10 | 60%
A030 | Project Execution Plan & procedures | 2026-12-03→2027-01-15 | fc 2026-12-03→2027-01-15 | 2%
A040 | Baseline schedule L1-L3 & approval | 2026-12-03→2027-01-10 | fc 2026-12-03→2027-01-10 | 5%
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
{"client-commercial-manager": [{"day": 1, "from": "client-project-manager", "kind": "cc", "ref": "HEL001-L-PM-QSE-HEP-0001", "subject": "Re: Confirmation of Contract Signature and Kick-off Meeting Arrangements", "summary": "copied for information"}, {"day": 1, "from": "client-project-manager", "kind": "request", "ref": "REQ-001-client-p", "subject": "Please prepare QSE input for the KOM on the advance payment guarantee, advance payment timing, and payment certification", "summary": "Please prepare QSE input for the KOM on the advance payment guarantee, advance payment timing, and payment certification and invoicing procedure.", "due_day": 1}, {"day": 2, "from": "epc-project-director", "kind": "action", "ref": "ACT-002-KOM-01", "subject": "Return QSE comments on draft APG and Performance Security forms", "summary": "Action from HEL001-MOM-KOM-001, due 2026-12-07", "due_day": 9}, {"day": 2, "from": "epc-project-director", "kind": "action", "ref": "ACT-002-KOM-02", "subject": "Confirm acceptability of HEP's proposed issuing bank and rating evidence requirements", "summary": "Action from HEL001-MOM-KOM-001, due 2026-12-09", "due_day": 9}, {"day": 2, "from": "epc-project-director", "kind": "mom", "ref": "HEL001-MOM-KOM-001", "subject": "Kick-off Meeting", "summary": "Minutes issued; review your actions"}, {"day": 2, "from": "epc-contracts-manager", "kind": "email", "ref": "D002_epc-contracts-manager_APG_and_Performance_Security_-_follow-up", "subject": "APG and Performance Security - follow-up on form approval and issuing bank after KOM", "summary": "Dear Omar,\n\nThank you for your time at today's Kick-off Meeting. As we noted when going through the NTP precondition checklist, HEP's letter HEL001-L-CM-HEP-QSE-0001 of 2 December submitted the forms of the Advance Payment Guarantee and the Performance Security for QSE's approval.\n\nI would be grateful if QSE would send its comments, or its approval of form, by Monday 7 December 2026 (ACTIONS-001-010). Please also confirm in writing whether the proposed issuing bank is acceptable to QSE. We cannot ask the bank to issue the instruments until we have both.\n\nThe APG relates to the 10% advance (USD 9,500,000) and the advance payment is due on 5 January 2027 (M03). We would like to hand over the instruments before NTP on 15 December. A response on 7 December leaves about one week to finalise and issue them.\n\nI have updated the NTP checklist to Rev B. I will send you the copy through document control. Please also confirm your authorised signatories in writing. I will send you HEP's insurance evidence ahead of your request REQ-001-client-c, which is due 12 December.\n\nKind regards,\nThomas Becker\nContracts & Commercial Manager, Helios EPC LLC"}, {"day": 2, "from": "client-project-manager", "kind": "cc", "ref": "HEL001-L-PM-QSE-HEP-0002", "subject": "Notice of Nomination of Client Representative (HEL001)", "summary": "copied for information"}, {"day": 2, "from": "client-project-manager", "kind": "email", "ref": "D002_client-project-manager_HEL001_-_Kick-off_follow-up_nomination_n", "subject": "HEL001 - Kick-off follow-up: nomination notice issued and QSE reporting protocol", "summary": "Colleagues, the Notice of Nomination of Client Representative has been issued to Helios EPC today (ACTIONS-001-013 closed). Please keep all contractual correspondence addressed to me with Sophie copied, and route payment and security matters through Omar. For lender reporting I need the Owner's Engineer's monthly inputs by the 3rd working day of each month; Bekzod to provide weekly site observations each Friday. Document review periods agreed at Kick-off apply from tomorrow. Regards, Khalid"}], "epc-project-director": [{"day": 2, "from": "epc-project-director", "kind": "action", "ref": "ACT-002-KOM-07", "subject": "Issue Project Execution Plan Rev A including the agreed reporting format, communication protocol and review periods", "summary": "Action from HEL001-MOM-KOM-001, due 2026-12-15", "due_day": 9}, {"day": 2, "from": "epc-planning-manager", "kind": "cc", "ref": "HEL001-L-PL-HEP-OWE-0001", "subject": "Baseline Schedule L1-L3 - Proposed Submission and Review Route (HEL001)", "summary": "copied for information"}, {"day": 2, "from": "epc-contracts-manager", "kind": "request", "ref": "REQ-002-epc-cont", "subject": "Please confirm that I may send HEP's signatory specimen sheet to QSE, and which persons are authorised to sign notices i", "summary": "Please confirm that I may send HEP's signatory specimen sheet to QSE, and which persons are authorised to sign notices in your absence.", "due_day": 4}, {"day": 2, "from": "client-project-manager", "kind": "letter", "ref": "HEL001-L-PM-QSE-HEP-0002", "subject": "Notice of Nomination of Client Representative (HEL001)", "summary": "Dear Mr Iyer,\nFurther to the Contract signed on 1 December 2026 between Qizilqum Solar Energy JSC (QSE) and Helios EPC LLC for the HELIOS 100 MW Solar PV + BESS Power Plant (HEL001), and to your letter HEL001-L-PM-HEP-QSE-0003 of 2 December 2026, QSE hereby gives formal notice that Mr Khalid Al-Mansoori, Client Project Manager, is nominated as the Employer's Representative (Client Representative) for the Contract with effect from today, 3 December 2026, in accordance with the Employer's administration provisions of the Contract (Clause 3 of the Conditions). This notice closes action ACTIONS-001-013 recorded at the Kick-off Meeting.\nWithin the limits notified below, the Client Representative is authorised to act for QSE in the following matters: (a) issuing and receiving notices, instructions and correspondence under the Contract; (b) review, comment, approval or rejection of submissions, including the Baseline Schedule, Project Execution Plan, design documents and proposed subcontractors, within the review periods agreed at Kick-off; (c) certification of Interim Payment Certificates and milestone payments, on the recommendation of the Owner's Engineer and the Client Commercial & Contracts M

YESTERDAY'S DIARY:
# Day 002 (2026-12-03, Thu)

**Phase(s):** P1  
**Weather:** overcast, moderate wind, -2..5 °C  
**Site manpower:** 0  

## Narrative
Day 2 is the Kick-off Meeting (Milestone M02), held as a full-day session at the QSE office in Tashkent from 10:00 to 16:30 under an overcast, windy and cold sky. Helios EPC presents its organisation, the outline Level 1-3 baseline schedule and the NTP precondition checklist, while QSE and Meridian set out reporting, communication and document review expectations. There is still no presence on the Qizilqum site; all work is office-based and focused on governance, the road to NTP on 15 December and the advance payment guarantee.

## What people did
- **Rajan Iyer** (Project Director): I chaired the Kick-off Meeting (M02) at the QSE Tashkent office from 10:00 to 16:30 and walked through organisation, the L1-L3 schedule outline, NTP preconditions, bank instrument forms and QSE's reporting, communication and review-period items. I recorded 10 decisions and 8 actions with owners and dates in the minutes, and confirmed the bank signatories and HEP's permit and land position to Thomas Becker. _[1 emails, 1 moms, 1 schedule, 2 requests]_
- **Aziz Karimov** (Planning Manager): I presented the outline Level 1-3 baseline schedule at the kick-off meeting and proposed the submission and approval route with Meridian under A040, targeting approval by 10 January. I issued the Stakeholder Register (Rev A) covering QSE, Meridian, UzGridCo, the Regional Administration, subcontractors and vendors. I also wrote to Meridian to formalise the schedule review workflow. _[1 documents, 1 letters, 1 emails, 1 schedule, 2 requests]_
- **Thomas Becker** (Contracts & Commercial Manager): I presented the NTP precondition checklist at the Kick-off Meeting, recorded QSE's verbal responses and issued Rev B of the checklist with the Project Director's signatory confirmation and the permit and land allocation positions. I then emailed Omar Hassan to chase QSE's approval of form and the issuing bank confirmation for the APG and Performance Security by 7 December. Every verbal response stays open until QSE confirms it in writing. _[1 documents, 1 emails, 2 registers, 2 requests]_
- **Khalid Al-Mansoori** (Client Project Manager): I hosted the Kick-off Meeting for QSE and led our items on lender reporting format, communication protocol and document review periods. I then issued the formal Notice of Nomination of Client Representative to Rajan Iyer, copied to Sophie Laurent and Omar Hassan, closing ACTIONS-001-013 a day ahead of its 4 December due date. _[1 letters, 1 emails, 1 registers, 2 requests]_

## Files produced
- MOM HEL001-MOM-KOM-001 Kick-off Meeting
- DOC HEL001-G000-P-&REG-00001-A Stakeholder Register → project/1_Project_Mgmt/02_Stakeholder_Register/HEL001-G000-P-&REG-00001-A_Stakeholder_Register.docx
- LETTER HEL001-L-PL-HEP-OWE-0001 → client-owners-engineer: Baseline Schedule L1-L3 - Proposed Submission and Review Route (HEL001)
- DOC HEL00

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

RULES
- Pick 2 to 7 roles to act today (fewer on quiet days; 0-1 on non-working days). Prefer roles with inbox items or scripted deliverables.
- Every must_produce item must be realistic for the phase and for that role. Letters need a to_role (a role id). Documents need folder (e.g. "1/04"), area, disc, type codes.
- Replies: if someone received a letter/request, the recipient should answer within a few days.
- Interpret surprises (kind=surprise) as something that becomes visible today through a report, inspection, letter or notice; list affected activities with slip_days (0 if unknown yet).
- Non-working day: usually empty day_plan; narrative only.
- Site manpower: 0 before mobilisation (~Day 90), ramping to ~900 at peak construction; productivity 1.0 normal, lower on bad weather.
Return ONLY JSON matching the schema.