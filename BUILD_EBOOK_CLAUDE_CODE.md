# Claude Code Task — Build the *Echoes of Eidolon: Book One* EPUB + PDF

You are running inside the `bkalaf/echoes-series` repo. Build two deliverables from the chapter Markdown files: a Kindle-safe **EPUB** and a 5.5×8.5″ **print PDF**, both with the cover, the decorative chapter headers, the embedded blackletter acrostic, and the corrected per-chapter beacons.

Do everything in a scratch build directory (e.g. `build/`) so the repo tree stays clean. Do **not** commit unless asked.

---

## 0. Prerequisites (check, install if missing)

- `pandoc` (≥ 3.1)
- `wkhtmltopdf` **and** `wkhtmltoimage` (the patched-Qt build)
- `python3` with `Pillow` (`pip install --break-system-packages Pillow`)
- `poppler-utils` (`pdfunite`, `pdftoppm`, `pdfinfo`)
- `zip` / `unzip`

If any are unavailable and can't be installed, stop and report which — don't silently produce a degraded build.

---

## 1. Inputs to locate in the repo

**Chapter files** — the 29 Markdown files (prologue, 25 chapters incl. `01_06b`, 3 interludes). They live under `chapters/` (or wherever the repo keeps generated prose). Each has an `eidolon-chapter-heading` div containing a `**Chapter N: Title**` line, a location line, a date line, and a `<span class="beacon beacon--COLOR">…</span>` beacon line (metaphysical chapters instead carry `Exact Location and Time Unknown`).

**`order.txt`** — the compile order (one filename stem per line, no extension). If present, prefer it; the `ORDER` list in the assembler below is the fallback and should match it.

**Art / font assets** — look for these (repo root, `assets/`, or `build/`):
- `unifrakturcook.ttf` (blackletter font — **required**, cannot be regenerated)
- `bk01.png` (cover, ~1024×1536 — **required**)
- `crestskyrend.png`, `crestaquilamatara.png`, `crestascentia.png`, `cresthellgate.png` (56×56 city crests)
- `mark.png` (Mark of the Orbs, ~120px tall, transparent)
- `flame-purple.png`, `flame-blue.png`, `flame-green.png`, `flame-yellow.png`, `flame-orange.png`, `flame-red.png` (~104px tall, transparent, phase-tinted)

If `mark.png` / `flame-*.png` are missing but the source SVGs (`mark_of_orbs.svg`, `beacon.svg`) exist, generate them per **§5**. The font, cover, and crests cannot be generated — if absent, stop and report.

---

## 2. Write the build scripts

Create `build/assemble.py` with **exactly** this content:

```python
import re, os
HERE=os.path.dirname(os.path.abspath(__file__))
ORDER=["01_00_prologue","01_01_the_royal_astronomers_tower","01_02_the_nomination",
"01_03_the_witnesses","01_interlude_the_choice_to_do_nothing","01_04_the_weight_of_the_beacon",
"01_05_the_core_of_the_conjunction","01_06_the_weight_of_the_roster","01_06b_the_room_between_stories","01_07_the_first_mirror",
"01_08_the_weight_of_being_asked","01_09_day_one_architecture","01_10_holes_in_the_wall",
"01_11_the_bountiful_harvest","01_12_the_unwound_core","01_13_the_thread_back_out",
"01_14_the_law_telling_us_to_forget","01_15_the_cities_that_disobeyed","01_16_rapid_acceptance",
"01_17_children_of_the_damned","02_interlude_the_doomsday_shelf","01_18_the_shelter_test",
"01_19_the_well_of_souls","01_20_the_red_thread_district","01_21_the_stupid_thread",
"01_22_go_with_the_eagle","01_23_restless_souls_at_stormspire","03_interlude_the_knots_and_the_nots",
"01_24_the_thread_through_the_maze"]
PHASE={"purple":"#7c3aed","blue":"#2563eb","green":"#16a34a","yellow":"#ca8a04","orange":"#ea580c","red":"#dc2626"}
CREST=[("skyrend peak","crestskyrend.png"),("aquila matara","crestaquilamatara.png"),
       ("luminthalas","crestascentia.png"),("pollyr fen","cresthellgate.png")]
AC_FIRST={"01_00_prologue","01_01_the_royal_astronomers_tower","01_02_the_nomination",
  "01_03_the_witnesses","01_interlude_the_choice_to_do_nothing","01_04_the_weight_of_the_beacon",
  "01_05_the_core_of_the_conjunction","01_06_the_weight_of_the_roster","01_06b_the_room_between_stories"}
AC_LAST={"01_07_the_first_mirror","01_08_the_weight_of_being_asked","01_09_day_one_architecture",
  "01_10_holes_in_the_wall","01_11_the_bountiful_harvest","01_12_the_unwound_core"}
OVERRIDE={
 "01_04_the_weight_of_the_beacon":("purple","Purple Beacon - 48-Hour Warning of Conjunction #1"),
 "01_05_the_core_of_the_conjunction":("purple","Purple Beacon - 48-Hour Warning of Conjunction #1"),
 "01_14_the_law_telling_us_to_forget":("green","Green Beacon - Day 4 of Conjunction #1"),
 "01_15_the_cities_that_disobeyed":("green","Green Beacon - Day 4 of Conjunction #1"),
 "01_17_children_of_the_damned":("yellow","Yellow Beacon - Day 12 of Conjunction #1"),
 "01_21_the_stupid_thread":("orange","Orange Beacon - Day 15 of Conjunction #1")}
MARK='<span class="hf-mark"><img src="mark.png" alt=""></span>'
def crest_for(loc):
    L=loc.lower()
    for k,f in CREST:
        if k in L: return f
    return None
def split_loc(loc):
    m=re.match(r'^(.*?),\s*(City of .*)$',loc)
    return (m.group(1).strip(),m.group(2).strip()) if m else ("",loc)
def split_date(d):
    m=re.match(r'^([A-Za-z]+,\s*\d+(?:st|nd|rd|th)?\s+of\s+[A-Za-z]+)(?:,\s*(.*))?$',d)
    if not m: return d,""
    wd=m.group(1).strip(); rest=(m.group(2) or "").strip()
    rest=re.sub(r'Conjunction Day\s*\d+,?\s*','',rest).strip().rstrip(',').strip()
    return wd,rest
def acrostic_html(name,title):
    pre,rest=(title.split(": ",1)+[""])[:2] if ": " in title else ("",title)
    if name in AC_FIRST:
        for i,c in enumerate(rest):
            if c.isalpha(): rest=rest[:i]+'<span class="acrostic">%s</span>'%c+rest[i+1:]; break
    elif name in AC_LAST:
        for i in range(len(rest)-1,-1,-1):
            if rest[i].isalpha(): rest=rest[:i]+'<span class="acrostic">%s</span>'%rest[i]+rest[i+1:]; break
    return (pre+": "+rest) if pre else rest
def build(name,text):
    m=re.search(r'<div class="eidolon-chapter-heading[^"]*"[^>]*>(.*?)</div>',text,flags=re.S)
    if not m: return text
    inner,rest=m.group(1),text[m.end():]
    title=None;meta=[];beacon=None
    for l in [x.strip() for x in inner.split("\n") if x.strip()]:
        if l.startswith("!["): continue
        tm=re.match(r'^\*\*(.+)\*\*$',l)
        if tm and title is None: title=tm.group(1); continue
        if "beacon beacon--" in l: beacon=l; continue
        meta.append(l)
    h1="# "+(title or "Untitled")
    if any("Exact Location and Time Unknown" in x for x in meta):
        loc=meta[0] if meta else "Exact Location and Time Unknown"
        box=(f'<div class="hframe hframe--light">\n{MARK}\n'
             f'<div class="cmeta"><p class="exact-loc">{loc}</p></div>\n</div>')
        ct=f'<p class="ct">{acrostic_html(name,title or "Untitled")}</p>'
        return h1+"\n\n"+box+"\n\n"+ct+"\n"+rest
    location=meta[0] if meta else ""; date=meta[1] if len(meta)>1 else ""
    ph=None; tag=""
    if beacon:
        bm=re.search(r'beacon beacon--(\w+)',beacon); ph=bm.group(1) if bm else None
        tag=re.sub(r'<span class="beacon[^>]*></span>\s*','',beacon).strip()
    if name in OVERRIDE: ph,tag=OVERRIDE[name]
    interior,city_state=split_loc(location)
    weekday_date,hour=split_date(date)
    cr=crest_for(location); coa=f'<img class="coa" src="{cr}" alt="">' if cr else ""
    hexc=PHASE.get(ph,"#333")
    rows=[]
    if interior:
        rows.append(f'<p class="loc-in">{coa} {interior} {coa}</p>')
        rows.append(f'<p class="loc">{city_state}</p>')
    else:
        rows.append(f'<p class="loc">{coa} {city_state} {coa}</p>')
    if weekday_date: rows.append(f'<p class="date">{weekday_date}</p>')
    if hour: rows.append(f'<p class="hour">{hour}</p>')
    if tag: rows.append(f'<p class="tag" style="color:{hexc}">{tag}</p>')
    box=(f'<div class="hframe hframe--{ph or "none"}">\n{MARK}\n<div class="cmeta">'
         +"".join(rows)+'</div>\n'
         f'<span class="hfire"><img src="flame-{ph}.png" alt=""></span>\n</div>')
    ct=f'<p class="ct">{acrostic_html(name,title or "Untitled")}</p>'
    return h1+"\n\n"+box+"\n\n"+ct+"\n"+rest
parts=[]
for n in ORDER:
    p=os.path.join(HERE,n+".md")
    if os.path.exists(p): parts.append(build(n,open(p).read()).strip())
    else: print("MISS",n)
open(os.path.join(HERE,"assembled.md"),"w").write("\n\n".join(parts)+"\n")
print("assembled",len(parts),"sections")
```

Create `build/book.css` with **exactly** this content:

```css
@font-face{font-family:'UnifrakturCook';src:url('unifrakturcook.ttf');font-weight:700;font-style:normal;}
@page{size:5.5in 8.5in;margin:0.55in 0.6in;}
html,body{margin:0;padding:0;}
body{font-family:"EB Garamond","Iowan Old Style",Georgia,serif;color:#17130f;font-size:12pt;line-height:1.5;}
.acrostic{font-family:'UnifrakturCook',serif;font-weight:700;font-size:1.35em;line-height:0;}
h1{display:none;}
.ct{text-align:center;font-variant:small-caps;letter-spacing:.02em;font-weight:700;font-size:17pt;line-height:1.3;margin:.7em 0 .15em;}
.ct .acrostic{font-family:'UnifrakturCook',serif;font-weight:700;font-size:1.35em;line-height:0;}
.hframe{page-break-before:always;break-before:page;border-top:1px solid #6b5d4f;border-bottom:1px solid #6b5d4f;
   border-left:3px double #6b5d4f;border-right:3px double #6b5d4f;
   text-align:center;padding:20px 22px 22px;margin:.35in 0 .35em;}
.hframe--light{page-break-before:always;break-before:page;border:none;padding:6px 22px 10px;margin:.35in 0 .35em;}
.hf-mark{display:block;text-align:center;margin:0 0 .8em;}
.hf-mark img{height:50px;width:auto;}
.hfire{display:block;text-align:center;margin:.8em 0 0;}
.hfire img{height:38px;width:auto;}
.cmeta{margin:0;}
.cmeta p{text-align:center;text-indent:0;margin:.12em 0;}
.loc-in{font-style:italic;color:#4a4038;font-size:11pt;line-height:2.7;margin:.1em 0 .3em;}
.loc{font-style:italic;color:#4a4038;font-size:11pt;margin:.05em 0 .15em;}
.date{font-style:italic;color:#4a4038;font-size:11pt;margin:.15em 0 0;}
.hour{font-style:italic;color:#4a4038;font-size:11pt;margin:0 0 .15em;}
.tag{font-variant:small-caps;letter-spacing:.03em;font-size:11pt;margin-top:.5em;}
.exact-loc{font-style:italic;color:#4a4038;font-size:11pt;}
img.coa{height:40px;width:auto;display:inline-block;vertical-align:middle;margin:0 11px;}
h2{text-align:left !important;font-weight:700;font-variant:small-caps;letter-spacing:.05em;
   font-size:13pt;color:#3a2f26;margin:1.6em 0 .7em;}
p{margin:0;text-indent:1.4em;line-height:1.5;text-align:justify;-webkit-hyphens:auto;hyphens:auto;}
h2+p,hr+p,.hframe+p,.hframe--light+p,.ct+p{text-indent:0;}
hr{border:0;margin:1.4em 0;}
hr::after{content:"\2756\00a0\00a0\2756\00a0\00a0\2756";color:#b09a80;font-size:.8em;letter-spacing:.1em;display:block;text-align:center;}
```

---

## 3. Stage and assemble

```bash
mkdir -p build && cd build
# chapter files (adjust source path to wherever prose lives)
cp ../chapters/*.md .
# assets (adjust source paths)
cp ../unifrakturcook.ttf ../bk01.png ../crest*.png ../mark.png ../flame-*.png . 2>/dev/null || true
# assemble.py and book.css were written above into build/
python3 assemble.py            # -> build/assembled.md ; must print "assembled 29 sections" with NO "MISS" lines
```

If `assemble.py` prints any `MISS <name>` line, a chapter file is absent or misnamed — fix before continuing.

---

## 4. Build EPUB, then PDF

**EPUB** (real embedded font + cover; then strip the acrostic `<span>` out of the TOC so the puzzle isn't announced):

```bash
pandoc assembled.md -o echoes_book1.epub --toc --toc-depth=1 --split-level=1 \
  -c book.css --epub-embed-font=unifrakturcook.ttf --epub-cover-image=bk01.png \
  --metadata title="Echoes of Eidolon: Book One" --metadata author="R H Dykeman" --metadata lang=en-US

rm -rf _ex && mkdir _ex && (cd _ex && unzip -o -q ../echoes_book1.epub)
for f in $(find _ex -name 'nav.xhtml' -o -name 'toc.ncx'); do
  sed -i -E 's#<span class="acrostic">([^<])</span>#\1#g' "$f"
done
rm -f echoes_book1.epub
(cd _ex && zip -X0 ../echoes_book1.epub mimetype >/dev/null && zip -Xr9D ../echoes_book1.epub . -x mimetype >/dev/null)
```

**PDF** (self-contained HTML → wkhtmltopdf, page numbers footed, cover merged in front):

```bash
pandoc assembled.md -o book.html --standalone --embed-resources -c book.css \
  --metadata title="Echoes of Eidolon: Book One"
wkhtmltopdf --page-width 5.5in --page-height 8.5in \
  --margin-top 0.5in --margin-bottom 0.6in --margin-left 0.6in --margin-right 0.6in \
  --enable-local-file-access --load-error-handling ignore --load-media-error-handling ignore \
  --footer-center "[page]" --footer-font-size 8 --footer-font-name "Georgia" --footer-spacing 4 \
  book.html body.pdf
printf '<!DOCTYPE html><html><body style="margin:0;padding:0;"><img src="bk01.png" style="width:5.5in;height:8.5in;display:block;margin:0;"></body></html>' > cover.html
wkhtmltopdf --page-width 5.5in --page-height 8.5in --margin-top 0 --margin-bottom 0 --margin-left 0 --margin-right 0 \
  --enable-local-file-access --disable-smart-shrinking cover.html cover.pdf
pdfunite cover.pdf body.pdf echoes_book1.pdf
```

---

## 5. Generate the PNG art *only if* `mark.png` / `flame-*.png` are missing (SVGs required)

wkhtmltoimage is used as an SVG rasterizer (ImageMagick's SVG delegate is usually absent). Then Pillow trims transparent margins and resizes.

```bash
python3 - <<'PY'
import re, subprocess, os
from PIL import Image
def raster(svg_path, out_png, px):
    svg=re.sub(r'<\?xml[^>]*\?>\s*','',open(svg_path).read())
    svg=re.sub(r'<svg ', f'<svg style="height:{px}px;width:auto;display:block" ', svg, count=1)
    open("_r.html","w").write('<!DOCTYPE html><html><head><meta charset="utf-8"></head><body style="margin:0;background:transparent">'+svg+'</body></html>')
    subprocess.run(["wkhtmltoimage","--enable-local-file-access","--transparent","-f","png","_r.html",out_png],check=True)
    im=Image.open(out_png).convert("RGBA"); im=im.crop(im.split()[3].getbbox())
    w,h=im.size; im=im.resize((max(1,round(w*px/h)),px),Image.LANCZOS); im.save(out_png)
# Mark
if not os.path.exists("mark.png"): raster("mark_of_orbs.svg","mark.png",120)
# Flames: tint beacon.svg's black fill per phase
COL={"purple":"#7c3aed","blue":"#2563eb","green":"#16a34a","yellow":"#ca8a04","orange":"#ea580c","red":"#dc2626"}
base=re.sub(r'<\?xml[^>]*\?>\s*','',open("beacon.svg").read())
for k,v in COL.items():
    if os.path.exists(f"flame-{k}.png"): continue
    open(f"_flame-{k}.svg","w").write(base.replace("fill:rgb(0%,0%,0%)",f"fill:{v}").replace('fill="#000000"',f'fill="{v}"'))
    raster(f"_flame-{k}.svg", f"flame-{k}.png", 104)
print("art generated")
PY
```

(If `beacon.svg` uses a different black-fill encoding, adjust the `.replace(...)` targets so the tint lands.)

---

## 6. Verify before declaring done

```bash
# EPUB: 30 xhtml sections (28 body + cover + title), font + cover embedded, TOC plain
unzip -l echoes_book1.epub | grep -cE 'text/.*\.xhtml'      # ~30
unzip -p echoes_book1.epub $(unzip -l echoes_book1.epub|grep -oE 'EPUB/[^ ]*toc.ncx') | grep -c '<navPoint'  # ~29
# PDF: 5.5x8.5, ~316 pages, cover on page 1
pdfinfo echoes_book1.pdf | grep -E 'Pages|Page size'
pdftoppm -png -r 80 -f 1 -l 1 echoes_book1.pdf _p1 && echo "rendered p1 (should be the cover)"
```

Also confirm the acrostic renders: the visible chapter titles keep the blackletter `.acrostic` letter (spelling **HORROR IS A REGRET** — first letters prologue→Ch6, the **A** in Chapter 7 "A Room Between Stories", last letters Ch8→Ch13), while the TOC shows plain titles.

---

## Design constraints (do not "fix" these — they're deliberate)

- **Kindle ignores CSS `transform`, absolute positioning, and data-URI `@font-face`.** So: font is embedded via `--epub-embed-font` (a real font file), and all header art is normal-flow `<img>` PNG. Do not switch to inline SVG or CSS-positioned art.
- **Acrostic = HORROR IS A REGRET**, anchored to files + title first/last letters via `AC_FIRST`/`AC_LAST`. Styled blackletter in the body; stripped from the TOC in §4. Chapter 7 "A Room Between Stories" supplies the **A** and must stay in `AC_FIRST`.
- **Beacons are a start-of-chapter snapshot.** The `OVERRIDE` map corrects six chapters (04/05→purple, 14/15→green, 17→yellow, 21→orange); leave it.
- **Header order:** hidden top-level `# H1` (splits the EPUB + feeds the plain TOC) → the `.hframe` box (Mark, crest-flanked interior location, city/state, weekday+date, hour, beacon tag, flame) → the visible `.ct` title *after* the box. Metaphysical chapters use the borderless `.hframe--light` with "Exact Location and Time Unknown".
- Cover is page 1 of both outputs; author is **R H Dykeman**.

## Open items to surface to the author (do NOT auto-decide)

1. **`01_09` / `01_10` beacon:** currently **green** (matching their "Conjunction Day 1" label). If the green beacon truly onsets at 5 pm, they'd open **blue** instead — ask before changing.
2. **Chapter 1 header:** it currently shows the **purple** beacon at the top, but Ch1 opens with the beacon *dark* — the purple lights mid-chapter at the Hour of the Singularity. If the author wants "dark at start," give `01_01` a light/no-beacon header (or add an `OVERRIDE` entry rendering no flame). Left as-is pending their call.
3. **Math (`$$…$$` in Chapter 1):** pandoc renders it as **MathML** in the EPUB (fine on Apple Books/Kobo/newer Kindle, spotty on old Kindle firmware) and **wkhtmltopdf does not render math at all** in the PDF. For a universal result, pre-render each equation to a transparent PNG (e.g. matplotlib mathtext) and swap the `$$…$$` for the image before building. Flag this; don't ship the PDF with invisible equations without noting it.

---

## Output

Produce `build/echoes_book1.epub` and `build/echoes_book1.pdf`. Report page count, section/TOC counts, and any `MISS`/missing-asset warnings. Do not commit unless the author asks.
