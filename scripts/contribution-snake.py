"""Render a snake over the signed-out GitHub contribution calendar."""

import re
import sys
from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path


COLORS = ("#283550", "#4b6194", "#6b78c8", "#9b8af2", "#d0b8ff")
SNAKE = ("#a0ffdf", "#74eacd", "#5ad3b8", "#46b99f", "#379383")
MONTHS = ("jan.", "fév.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc.")
STEP = 15


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = {}

    def handle_starttag(self, tag, attrs):
        cell = dict(attrs)
        if tag == "td" and "ContributionCalendar-day" in cell.get("class", "").split():
            row, column = map(int, re.fullmatch(r"contribution-day-component-(\d+)-(\d+)", cell["id"]).groups())
            self.days[column, row] = date.fromisoformat(cell["data-date"]), int(cell["data-level"])


def walk(active):
    first_column, first_row = min(active, default=(38, 3))
    column, row = max(0, first_column - 5), first_row
    path = [(column, row)]
    for target_column, target_row in sorted(active) or [(52, 3)]:
        while row != target_row:
            row += 1 if row < target_row else -1
            path.append((column, row))
        while column < target_column:
            column += 1
            path.append((column, row))
    return path


def position(cell):
    column, row = cell
    return 44 + column * STEP, 72 + row * STEP


def render(days):
    active = {cell for cell, (_, level) in days.items() if level}
    path = walk(active)
    last = max(1, len(path) - 1)
    duration = max(4, min(10, last * .14))
    visited = {}
    for frame, cell in enumerate(path):
        visited.setdefault(cell, frame)

    shapes = []
    for cell, (day, level) in sorted(days.items()):
        x, y = position(cell)
        motion = ""
        if cell in active:
            delay = duration * visited[cell] / last
            motion = f' class="food" style="--at:{delay:.3f}s;--restore:{duration + .55:.3f}s;--color:{COLORS[level]}"'
        shapes.append(f'<rect x="{x}" y="{y}" width="11" height="11" rx="3" fill="{COLORS[level]}"{motion}/>')
        if day.weekday() == 6 and day.day <= 7:
            shapes.append(f'<text x="{x}" y="63" class="label">{MONTHS[day.month - 1]}</text>')

    legend = [
        f'<rect x="{740 + index * 12}" y="190" width="9" height="9" rx="2" fill="{color}"/>'
        for index, color in enumerate(COLORS)
    ]

    style = []
    for offset, color in reversed(list(enumerate(SNAKE))):
        frames = []
        for frame in range(last + 1):
            x, y = position(path[min(len(path) - 1, max(0, frame - offset))])
            frames.append(f"{frame / last:.5%}{{transform:translate({x}px,{y}px)}}")
        style.append(f"@keyframes crawl-{offset}{{{''.join(frames)}}}")
        x, y = position(path[max(0, len(path) - 1 - offset)])
        shapes.append(
            f'<g class="snake" transform="translate({x} {y})" style="--crawl:crawl-{offset}">'
            f'<rect width="11" height="11" rx="3.5" fill="{color}"/>'
            + ('<circle cx="7.3" cy="3.7" r="1.15" fill="#192541"/>' if offset == 0 else "")
            + "</g>"
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="896" height="215" viewBox="0 0 896 215" role="img" aria-labelledby="title">
<title id="title">Serpent animé sur le calendrier public des contributions GitHub de LeoBgn</title>
<style>
  .label {{ font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11px; fill: #aab8d7; }}
  .food {{ animation: eat .2s var(--at) forwards, restore .35s var(--restore) forwards; }}
  .snake {{ animation: var(--crawl) {duration:.3f}s linear both, leave .35s {duration + .5:.3f}s forwards; }}
  @keyframes eat {{ to {{ fill: {COLORS[0]}; }} }}
  @keyframes restore {{ from {{ fill: {COLORS[0]}; }} to {{ fill: var(--color); }} }}
  @keyframes leave {{ to {{ opacity: 0; }} }}
  {chr(10).join(style)}
  @media (prefers-reduced-motion: reduce) {{
    .food {{ animation: none; }}
    .snake {{ display: none; }}
  }}
</style>
<rect x="1" y="1" width="894" height="213" rx="19" fill="#11182c" stroke="#465780" stroke-width="2"/>
<text x="44" y="32" fill="#e2d9ff" font-family="ui-monospace, monospace" font-size="15" font-weight="700">CONTRIBUTIONS / @LEOBGN</text>
<text x="835" y="31" text-anchor="end" class="label">CALENDRIER PUBLIC · 12 MOIS</text>
<path d="M44 44H835" stroke="#344262"/>
{chr(10).join(shapes)}
<path d="M44 183H835" stroke="#344262"/>
<text x="44" y="199" class="label">Une case par jour</text>
<text x="731" y="199" text-anchor="end" class="label">Moins</text>
{chr(10).join(legend)}
<text x="835" y="199" text-anchor="end" class="label">Plus</text>
</svg>
'''


def main():
    calendar = Calendar()
    calendar.feed(sys.stdin.read())
    days = calendar.days
    dates = sorted(day for day, _ in days.values())
    if len(days) not in (365, 366) or any(
        following - current != timedelta(days=1) for current, following in zip(dates, dates[1:])
    ) or any(not (0 <= column < 54 and 0 <= row < 7 and 0 <= level < len(COLORS))
             for (column, row), (_, level) in days.items()):
        raise SystemExit("GitHub did not return a valid one-year public calendar")
    Path("assets/contribution-snake.svg").write_text(render(days), encoding="utf-8")


if __name__ == "__main__":
    main()
