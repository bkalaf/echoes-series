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
