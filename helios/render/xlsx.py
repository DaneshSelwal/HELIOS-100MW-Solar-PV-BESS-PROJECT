"""Render real Excel files: registers, tables, schedules with a Gantt sheet."""
from __future__ import annotations
import datetime as dt, pathlib
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HDR_FILL = PatternFill("solid", fgColor="1F3A5F"); HDR_FONT = Font(bold=True, color="FFFFFF")
THIN = Side(style="thin", color="BBBBBB"); BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def _sheet_table(ws, columns: list[str], rows: list[list], title: str | None = None, widths: dict | None = None):
    r0 = 1
    if title:
        ws.cell(row=1, column=1, value=title).font = Font(bold=True, size=14, color="1F3A5F"); r0 = 3
    for i, c in enumerate(columns, 1):
        cell = ws.cell(row=r0, column=i, value=c); cell.fill = HDR_FILL; cell.font = HDR_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center"); cell.border = BORDER
    for j, row in enumerate(rows, r0 + 1):
        for i, v in enumerate(row, 1):
            cell = ws.cell(row=j, column=i, value=v); cell.border = BORDER
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            if isinstance(v, (dt.date, dt.datetime)):
                cell.number_format = "DD-MMM-YYYY"
    for i, c in enumerate(columns, 1):
        w = (widths or {}).get(c) or min(max(12, len(str(c)) + 2, *(len(str(r[i - 1])) // 1 + 2 for r in rows[:50] if i - 1 < len(r))) if rows else 14, 60)
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = ws.cell(row=r0 + 1, column=1)


def table(path: pathlib.Path, *, sheet: str, columns: list[str], rows: list[list], title: str | None = None,
          extra_sheets: list[tuple[str, list[str], list[list]]] | None = None) -> pathlib.Path:
    wb = Workbook(); ws = wb.active; ws.title = sheet[:31]
    _sheet_table(ws, columns, rows, title)
    for name, cols, rws in extra_sheets or []:
        _sheet_table(wb.create_sheet(name[:31]), cols, rws)
    path.parent.mkdir(parents=True, exist_ok=True); wb.save(str(path)); return path


def schedule(path: pathlib.Path, *, title: str, activities: list[dict], data_date: dt.date,
             week_start: dt.date | None = None, weeks: int = 80) -> pathlib.Path:
    """activities: [{id, wbs, name, start, finish, pred:[...], weight, pct_complete?, actual_start?, actual_finish?}]"""
    wb = Workbook(); ws = wb.active; ws.title = "Activities"
    cols = ["ID", "WBS", "Activity", "Start", "Finish", "Dur (d)", "Predecessors", "Weight %", "% Complete", "Actual Start", "Actual Finish", "Status"]
    rows = []
    for a in activities:
        s, f = _d(a["start"]), _d(a["finish"])
        pct = a.get("pct_complete", 0) or 0
        status = "Complete" if pct >= 100 else ("In progress" if pct > 0 else ("Not started" if s > data_date else "Late start" if not a.get("actual_start") else "In progress"))
        rows.append([a["id"], a["wbs"], a["name"], s, f, (f - s).days + 1, ", ".join(a.get("pred", [])), a.get("weight", 0),
                     pct, _d(a["actual_start"]) if a.get("actual_start") else None, _d(a["actual_finish"]) if a.get("actual_finish") else None, status])
    _sheet_table(ws, cols, rows, f"{title}   (data date {data_date:%d %b %Y})", {"Activity": 55, "Predecessors": 22})
    # Gantt sheet: one column per week
    g = wb.create_sheet("Gantt")
    ws0 = week_start or (min(_d(a["start"]) for a in activities) - dt.timedelta(days=min(_d(a["start"]) for a in activities).weekday()))
    g.cell(row=1, column=1, value="ID").font = HDR_FONT; g.cell(row=1, column=1).fill = HDR_FILL
    g.cell(row=1, column=2, value="Activity").font = HDR_FONT; g.cell(row=1, column=2).fill = HDR_FILL
    g.column_dimensions["B"].width = 50
    for w in range(weeks):
        c = g.cell(row=1, column=3 + w, value=(ws0 + dt.timedelta(weeks=w)).strftime("%d%b%y"))
        c.font = Font(size=7, bold=True, color="FFFFFF"); c.fill = HDR_FILL; c.alignment = Alignment(text_rotation=90)
        g.column_dimensions[get_column_letter(3 + w)].width = 2.2
    plan_fill = PatternFill("solid", fgColor="9DB7D5"); done_fill = PatternFill("solid", fgColor="2E7D32"); ms_fill = PatternFill("solid", fgColor="C62828")
    for i, a in enumerate(activities, 2):
        g.cell(row=i, column=1, value=a["id"]); g.cell(row=i, column=2, value=a["name"])
        s, f = _d(a["start"]), _d(a["finish"]); pct = (a.get("pct_complete") or 0) / 100
        w_s = (s - ws0).days // 7; w_f = (f - ws0).days // 7
        n = max(1, w_f - w_s + 1)
        for w in range(w_s, w_f + 1):
            if 0 <= w < weeks:
                cell = g.cell(row=i, column=3 + w)
                if a.get("milestone"):
                    cell.fill = ms_fill
                else:
                    cell.fill = done_fill if (w - w_s + 1) <= round(pct * n) else plan_fill
    # data-date line
    dd = (data_date - ws0).days // 7
    if 0 <= dd < weeks:
        for i in range(1, len(activities) + 2):
            g.cell(row=i, column=3 + dd).border = Border(left=Side(style="thick", color="C62828"))
    g.freeze_panes = "C2"
    path.parent.mkdir(parents=True, exist_ok=True); wb.save(str(path)); return path


def _d(x) -> dt.date:
    return x if isinstance(x, dt.date) else dt.date.fromisoformat(str(x))
