# -*- coding: utf-8 -*-
import os, re, glob, html, json, sys

D = "/home/user/PISA/notes/recherche"
OUT = "/home/user/PISA/notes/html"
os.makedirs(OUT, exist_ok=True)

CAS   = {1,2,3,4,5,6,7,8,9,10,11,12,13,30,32,34,38}
TRANS = {33,37,39,41}

def famille(n):
    if n == 0: return ("Synthèse", "syn")
    if n in TRANS: return ("Section transversale", "tra")
    if n in CAS: return ("Étude de cas", "cas")
    return ("Levier", "lev")

# ---------- inline markdown ----------
URL_RE = re.compile(r'(https?://[^\s<>"\'\)\]]+[^\s<>"\'\)\]\.,;:])')

def inline(t, linkify=True):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*([^*\n]+?)\*(?![\w*])', r'<em>\1</em>', t)
    t = t.replace('« ', '« ').replace(' »', ' »')
    if linkify:
        t = URL_RE.sub(lambda m: '<a href="%s" target="_blank" rel="noopener">%s</a>'
                       % (m.group(1), m.group(1)), t)
    return t

# ---------- niveau de preuve ----------
def classe_preuve(s):
    s = s.lower()
    if 'randomis' in s or 'méta-analyse' in s or 'essai contrôlé' in s: return 'fort'
    if 'quasi-exp' in s or 'discontinuité' in s or 'différences' in s or 'appariement' in s: return 'mid'
    if 'nul' in s or 'réfut' in s or 'non établi' in s: return 'nul'
    return 'faible'

PREUVE_RE = re.compile(r'(Niveau de preuve\s*(?:</strong>)?\s*:\s*)([^<]{3,220})')
def marquer_preuve(h):
    def rep(m):
        tete, suite = m.group(1), m.group(2)
        fin = re.search(r'[.;]\s|[.;]$', suite)
        clause = suite[:fin.start()] if fin else suite
        if len(clause) > 140:
            clause = clause[:140].rsplit(' ', 1)[0] + '\u2026'
        reste = suite[len(clause):]
        c = classe_preuve(clause)
        return ('<span class="ev ev-%s"><span class="ev-dot"></span>%s%s</span>%s'
                % (c, tete, clause, reste))
    return PREUVE_RE.sub(rep, h)

# ---------- bloc markdown ----------
def convert(md, num):
    lines = md.split('\n')
    out, i, n = [], 0, len(lines)
    dans_sources = False
    premier_para = True
    while i < n:
        l = lines[i]
        s = l.strip()
        if not s:
            i += 1; continue
        if s.startswith('# '):
            i += 1; continue                     # titre porté par l'en-tête de section
        if s.startswith('### '):
            out.append('<h4>%s</h4>' % inline(s[4:])); i += 1; continue
        if s.startswith('## '):
            titre = s[3:].strip()
            dans_sources = titre.lower().startswith('source')
            slug = 's%d-%s' % (num, re.sub(r'[^a-z0-9]+', '-', titre.lower())[:40].strip('-'))
            out.append('<h3 id="%s">%s</h3>' % (slug, inline(titre)))
            if dans_sources: out.append('<div class="biblio">')
            i += 1; continue
        if re.match(r'^-{3,}$', s):
            i += 1; continue
        if s.startswith('|'):
            tbl, j = [], i
            while j < n and lines[j].strip().startswith('|'):
                tbl.append(lines[j].strip()); j += 1
            out.append(table_html(tbl)); i = j; continue
        if s.startswith('- '):
            items, j = [], i
            while j < n and lines[j].strip().startswith('- '):
                buf = lines[j].strip()[2:]
                j += 1
                while j < n and lines[j].strip() and not lines[j].strip().startswith(('- ', '#', '|')) \
                      and not re.match(r'^-{3,}$', lines[j].strip()):
                    buf += ' ' + lines[j].strip(); j += 1
                items.append(buf)
            cls = ' class="refs"' if dans_sources else ''
            out.append('<ul%s>%s</ul>' % (cls, ''.join('<li>%s</li>' % inline(x) for x in items)))
            i = j; continue
        if re.match(r'^\d+\.\s', s):
            items, j = [], i
            while j < n and re.match(r'^\d+\.\s', lines[j].strip()):
                items.append(re.sub(r'^\d+\.\s', '', lines[j].strip())); j += 1
            out.append('<ol>%s</ol>' % ''.join('<li>%s</li>' % inline(x) for x in items))
            i = j; continue
        # paragraphe
        buf, j = s, i + 1
        while j < n and lines[j].strip() and not lines[j].strip().startswith(('#', '- ', '|')) \
              and not re.match(r'^\d+\.\s|^-{3,}$', lines[j].strip()):
            buf += ' ' + lines[j].strip(); j += 1
        cls = ''
        if premier_para and num != 0:
            cls = ' class="lede"'; premier_para = False
        out.append('<p%s>%s</p>' % (cls, marquer_preuve(inline(buf))))
        i = j
    if dans_sources: out.append('</div>')
    return '\n'.join(out)

def table_html(rows):
    cells = [[c.strip() for c in r.strip('|').split('|')] for r in rows]
    if len(cells) > 1 and all(re.match(r'^:?-{2,}:?$', c) for c in cells[1]):
        head, body = cells[0], cells[2:]
    else:
        head, body = cells[0], cells[1:]
    h = '<thead><tr>%s</tr></thead>' % ''.join('<th>%s</th>' % inline(c) for c in head)
    b = '<tbody>%s</tbody>' % ''.join(
        '<tr>%s</tr>' % ''.join('<td>%s</td>' % inline(c) for c in r) for r in body)
    return '<div class="tw"><table>%s%s</table></div>' % (h, b)

def titre_de(path):
    for l in open(path, encoding='utf8'):
        if l.startswith('# '): return l[2:].strip()
    return os.path.basename(path)

# ---------- CSS ----------
CSS = r"""
:root{
  --paper:#f4f6f7; --surface:#ffffff; --ink:#14212a; --body:#26333c;
  --muted:#5d6c76; --rule:#dce3e6; --rule-soft:#e8edef;
  --accent:#1f5c73; --accent-soft:#e4eef2; --accent-ink:#164657;
  --ev-fort:#0f6b52; --ev-mid:#8a6a12; --ev-faible:#5b6a74; --ev-nul:#9b3225;
  --rail:#eef1f3;
  --f-disp:"Newsreader",Georgia,"Times New Roman",serif;
  --f-body:"Source Serif 4",Georgia,"Times New Roman",serif;
  --f-ui:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:#0e1418; --surface:#151d22; --ink:#e7eef1; --body:#c9d5da;
    --muted:#8ea0aa; --rule:#26333a; --rule-soft:#1e2a30;
    --accent:#79b6cd; --accent-soft:#17303a; --accent-ink:#a5cfdf;
    --ev-fort:#4fb894; --ev-mid:#c9a53f; --ev-faible:#8ea0aa; --ev-nul:#d9705f;
    --rail:#111a1f;
  }
}
:root[data-theme="dark"]{
  --paper:#0e1418; --surface:#151d22; --ink:#e7eef1; --body:#c9d5da;
  --muted:#8ea0aa; --rule:#26333a; --rule-soft:#1e2a30;
  --accent:#79b6cd; --accent-soft:#17303a; --accent-ink:#a5cfdf;
  --ev-fort:#4fb894; --ev-mid:#c9a53f; --ev-faible:#8ea0aa; --ev-nul:#d9705f;
  --rail:#111a1f;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:1.5rem}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
body{margin:0;background:var(--paper);color:var(--body);
  font-family:var(--f-body);font-size:17px;line-height:1.62;
  -webkit-font-smoothing:antialiased;font-variant-numeric:oldstyle-nums proportional-nums}

/* ---- shell ---- */
.shell{display:grid;grid-template-columns:300px minmax(0,1fr);align-items:start}
.rail{position:sticky;top:0;height:100vh;overflow-y:auto;background:var(--rail);
  border-right:1px solid var(--rule);padding:1.6rem 0 3rem}
.rail-in{padding-inline:1.25rem}
.brand{font-family:var(--f-ui);font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin:0 0 .35rem}
.rail h1{font-family:var(--f-disp);font-size:1.12rem;line-height:1.25;font-weight:600;
  color:var(--ink);margin:0 0 1rem;text-wrap:balance}
.tools{display:flex;gap:.5rem;margin-bottom:1.1rem}
#q{flex:1;min-width:0;font-family:var(--f-ui);font-size:.82rem;padding:.45rem .6rem;
  border:1px solid var(--rule);border-radius:3px;background:var(--surface);color:var(--ink)}
#q::placeholder{color:var(--muted)}
#q:focus-visible,.tbtn:focus-visible,.rail a:focus-visible,main a:focus-visible{
  outline:2px solid var(--accent);outline-offset:2px}
.tbtn{display:inline-flex;align-items:center;justify-content:center;font-family:var(--f-ui);font-size:.82rem;padding:.45rem .6rem;border:1px solid var(--rule);
  border-radius:3px;background:var(--surface);color:var(--muted);cursor:pointer;line-height:1}
.tbtn:hover{color:var(--accent);border-color:var(--accent)}
.grp{font-family:var(--f-ui);font-size:.66rem;letter-spacing:.13em;text-transform:uppercase;
  color:var(--muted);margin:1.5rem 0 .5rem;padding-top:.7rem;border-top:1px solid var(--rule)}
.grp:first-of-type{border-top:0;padding-top:0;margin-top:.4rem}
.rail ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:1px}
.rail a{display:grid;grid-template-columns:1.85rem 1fr;gap:.35rem;align-items:baseline;
  font-family:var(--f-ui);font-size:.83rem;line-height:1.35;color:var(--body);
  text-decoration:none;padding:.32rem .45rem;border-radius:3px}
.rail a .n{font-size:.72rem;color:var(--muted);font-variant-numeric:tabular-nums}
.rail a:hover{background:var(--accent-soft);color:var(--accent-ink)}
.rail a.on{background:var(--accent-soft);color:var(--accent-ink);font-weight:500}
.rail a.on .n{color:var(--accent)}
.rail li.hide{display:none}
.grp.hide{display:none}
.none{font-family:var(--f-ui);font-size:.8rem;color:var(--muted);padding:.4rem .45rem}

/* ---- main ---- */
main{padding:3.5rem 3rem 8rem;min-width:0}
.wrap{max-width:41rem;margin:0 auto}
.mast{margin-bottom:3.5rem;padding-bottom:2rem;border-bottom:2px solid var(--ink)}
.mast .eyebrow{font-family:var(--f-ui);font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--accent);margin:0 0 .9rem}
.mast h2{font-family:var(--f-disp);font-weight:600;font-size:clamp(2rem,4.4vw,3rem);line-height:1.08;
  letter-spacing:-.015em;color:var(--ink);margin:0 0 .8rem;text-wrap:balance}
.mast .sub{font-family:var(--f-disp);font-size:1.24rem;line-height:1.42;color:var(--muted);
  font-style:italic;margin:0 0 1.6rem;font-weight:400}
.meta{display:flex;flex-wrap:wrap;gap:0 2rem;font-family:var(--f-ui);font-size:.78rem;color:var(--muted)}
.meta b{display:block;font-family:var(--f-ui);font-size:1.35rem;font-weight:500;color:var(--ink);
  font-variant-numeric:tabular-nums lining-nums;line-height:1.2}
.note{font-family:var(--f-ui);font-size:.82rem;line-height:1.55;color:var(--muted);
  border-left:2px solid var(--rule);padding-left:1rem;margin:1.8rem 0 0}

section{content-visibility:auto;contain-intrinsic-size:auto 1400px;
  padding-block:3.2rem;border-top:1px solid var(--rule-soft)}
section:first-of-type{border-top:0}
.kicker{display:flex;align-items:baseline;gap:.7rem;font-family:var(--f-ui);font-size:.7rem;
  letter-spacing:.13em;text-transform:uppercase;color:var(--muted);margin-bottom:.7rem}
.kicker .num{font-size:1.5rem;letter-spacing:0;font-weight:500;color:var(--accent);
  font-variant-numeric:tabular-nums lining-nums;line-height:1}
section h2{font-family:var(--f-disp);font-weight:600;font-size:clamp(1.5rem,3vw,2.05rem);
  line-height:1.15;letter-spacing:-.01em;color:var(--ink);margin:0 0 1.4rem;text-wrap:balance}
h3{font-family:var(--f-disp);font-weight:600;font-size:1.26rem;line-height:1.28;color:var(--ink);
  margin:2.6rem 0 .9rem;text-wrap:balance}
h4{font-family:var(--f-ui);font-weight:600;font-size:.9rem;letter-spacing:.01em;color:var(--ink);
  margin:2rem 0 .6rem}
p{margin:0 0 1.1rem}
.lede{font-size:1.18rem;line-height:1.5;color:var(--ink);letter-spacing:-.003em}
strong{font-weight:600;color:var(--ink)}
main ul,main ol{margin:0 0 1.2rem;padding-left:1.15rem;display:flex;flex-direction:column;gap:.55rem}
main li{padding-left:.15rem}
main a{color:var(--accent);text-decoration:underline;text-decoration-thickness:.5px;
  text-underline-offset:2px;overflow-wrap:anywhere}
main a:hover{color:var(--accent-ink)}

/* niveau de preuve */
.ev{font-family:var(--f-ui);font-size:.82em;letter-spacing:.005em}
.ev-dot{display:inline-block;width:.42em;height:.42em;border-radius:50%;margin-right:.42em;
  vertical-align:.08em}
.ev-fort .ev-dot{background:var(--ev-fort)} .ev-fort{color:var(--ev-fort)}
.ev-mid  .ev-dot{background:var(--ev-mid)}  .ev-mid{color:var(--ev-mid)}
.ev-faible .ev-dot{background:var(--ev-faible)} .ev-faible{color:var(--ev-faible)}
.ev-nul  .ev-dot{background:var(--ev-nul)}  .ev-nul{color:var(--ev-nul)}

/* tableaux */
.tw{overflow-x:auto;margin:0 0 1.6rem;border:1px solid var(--rule);border-radius:2px;
  background:var(--surface)}
table{border-collapse:collapse;width:100%;font-family:var(--f-ui);font-size:.79rem;line-height:1.45}
th,td{text-align:left;padding:.6rem .75rem;border-bottom:1px solid var(--rule-soft);
  vertical-align:top;font-variant-numeric:tabular-nums lining-nums}
th{font-weight:600;color:var(--ink);background:var(--accent-soft);white-space:nowrap;
  font-size:.72rem;letter-spacing:.04em;text-transform:uppercase}
tbody tr:last-child td{border-bottom:0}
td strong{font-weight:600}

/* bibliographie */
.biblio{font-family:var(--f-ui);font-size:.79rem;line-height:1.5;color:var(--muted)}
.biblio .refs{padding-left:0;list-style:none;gap:.6rem}
.biblio .refs li{padding-left:1.15rem;text-indent:-1.15rem}
.biblio em{font-style:italic;color:var(--body)}
.biblio a{color:var(--muted);text-decoration-color:var(--rule)}
.biblio a:hover{color:var(--accent)}

.top{position:fixed;right:1.25rem;bottom:1.25rem;font-family:var(--f-ui);font-size:.75rem;
  padding:.5rem .7rem;background:var(--surface);border:1px solid var(--rule);border-radius:3px;
  color:var(--muted);text-decoration:none;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.top:hover{color:var(--accent);border-color:var(--accent)}

.railtog{display:none}
@media (max-width:920px){
  .shell{grid-template-columns:1fr}
  .rail{position:static;height:auto;border-right:0;border-bottom:1px solid var(--rule);
    padding:1.1rem 0 1.3rem}
  .rail nav{display:none}
  .rail.open nav{display:block}
  .railtog{display:inline-block}
  main{padding:2.2rem 1.25rem 5rem}
  body{font-size:16px}
}
@media print{
  .rail,.top{display:none}.shell{display:block}main{padding:0}
  section{content-visibility:visible;break-inside:auto}
  :root{--paper:#fff;--surface:#fff}
}
"""

JS = r"""
(function(){
  var root=document.documentElement, K='ak-theme';
  try{var t=localStorage.getItem(K); if(t) root.setAttribute('data-theme',t);}catch(e){}
  var btn=document.getElementById('theme');
  if(btn) btn.addEventListener('click',function(){
    var cur=root.getAttribute('data-theme');
    if(!cur) cur = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark':'light';
    var nxt = cur==='dark' ? 'light':'dark';
    root.setAttribute('data-theme',nxt);
    try{localStorage.setItem(K,nxt);}catch(e){}
  });
  var tog=document.getElementById('railtog'), rail=document.getElementById('rail');
  if(tog) tog.addEventListener('click',function(){rail.classList.toggle('open');});

  var links=[].slice.call(document.querySelectorAll('#toc a'));
  var items=links.map(function(a){
    var li=a.parentNode;
    return {a:a,li:li,txt:(a.textContent+' '+(a.dataset.k||'')).toLowerCase()};
  });
  var grps=[].slice.call(document.querySelectorAll('.grp'));
  var q=document.getElementById('q'), none=document.getElementById('none');
  if(q) q.addEventListener('input',function(){
    var v=q.value.trim().toLowerCase(), hits=0;
    items.forEach(function(it){
      var ok = !v || it.txt.indexOf(v)>-1;
      it.li.classList.toggle('hide',!ok); if(ok) hits++;
    });
    grps.forEach(function(g){
      var ul=g.nextElementSibling, vis=0;
      [].slice.call(ul.children).forEach(function(li){ if(!li.classList.contains('hide')) vis++; });
      g.classList.toggle('hide',vis===0);
    });
    if(none) none.style.display = hits? 'none':'block';
  });

  var byId={}; links.forEach(function(a){byId[a.getAttribute('href').slice(1)]=a;});
  var secs=[].slice.call(document.querySelectorAll('section[id]'));
  var cur=null;
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting) return;
      var a=byId[e.target.id]; if(!a||a===cur) return;
      if(cur) cur.classList.remove('on');
      a.classList.add('on'); cur=a;
      if(innerWidth>920){
        var r=a.getBoundingClientRect();
        if(r.top<80||r.bottom>innerHeight-80) a.scrollIntoView({block:'center'});
      }
    });
  },{rootMargin:'-15% 0px -70% 0px'});
  secs.forEach(function(s){io.observe(s);});
})();
"""

def page(titre_page, eyebrow, h2, sous_titre, stats, note, sections, groupes):
    toc = []
    for nom, ids in groupes:
        if not ids: continue
        toc.append('<div class="grp">%s</div><ul>' % html.escape(nom))
        for num, t in ids:
            lbl = '%02d' % num if num else '—'
            toc.append('<li><a href="#s%d" data-k="%s"><span class="n">%s</span><span>%s</span></a></li>'
                       % (num, html.escape(t.lower()), lbl, html.escape(t)))
        toc.append('</ul>')
    statl = ''.join('<div><b>%s</b>%s</div>' % (v, html.escape(k)) for k, v in stats)
    return """<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(titre)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>%(css)s</style>
</head><body>
<div class="shell">
<aside class="rail" id="rail"><div class="rail-in">
  <p class="brand">AKT for Wallonia</p>
  <h1>%(h1)s</h1>
  <div class="tools">
    <input id="q" type="search" placeholder="Filtrer les sections…" aria-label="Filtrer les sections">
    <button class="tbtn" id="theme" type="button" aria-label="Basculer le thème" title="Thème clair ou sombre"><svg width="13" height="13" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M8 1.5a6.5 6.5 0 0 0 0 13z" fill="currentColor"/></svg></button>
    <button class="tbtn railtog" id="railtog" type="button" aria-label="Afficher le sommaire">☰</button>
  </div>
  <nav id="toc" aria-label="Sommaire">%(toc)s<p class="none" id="none" style="display:none">Aucune section.</p></nav>
</div></aside>
<main><div class="wrap">
  <header class="mast">
    <p class="eyebrow">%(eyebrow)s</p>
    <h2>%(h2)s</h2>
    <p class="sub">%(sub)s</p>
    <div class="meta">%(stats)s</div>
    <p class="note">%(note)s</p>
  </header>
  %(sections)s
</div></main>
</div>
<a class="top" href="#">↑ Haut</a>
<script>%(js)s</script>
</body></html>""" % dict(titre=html.escape(titre_page), css=CSS, js=JS, h1=html.escape(h2),
                         toc=''.join(toc), eyebrow=html.escape(eyebrow), h2=html.escape(h2),
                         sub=html.escape(sous_titre), stats=statl, note=note,
                         sections='\n'.join(sections))

def rendre(paths):
    secs, entries = [], []
    for p in paths:
        b = os.path.basename(p)
        num = int(b.split('-')[0])
        t = titre_de(p)
        fam, _ = famille(num)
        corps = convert(open(p, encoding='utf8').read(), num)
        lbl = ('<span class="num">%02d</span>' % num) if num else ''
        secs.append('<section id="s%d"><div class="kicker">%s<span>%s</span></div>'
                    '<h2>%s</h2>%s</section>' % (num, lbl, html.escape(fam), html.escape(t), corps))
        entries.append((num, t))
    return secs, entries

# ============ rapport complet ============
tous = sorted(glob.glob(D + "/[0-9][0-9]-*.md"))
syn_p = [p for p in tous if os.path.basename(p).startswith('00-')]
sec_p = [p for p in tous if not os.path.basename(p).startswith('00-')]
secs, entries = rendre(syn_p + sec_p)

g_syn, g_cas, g_lev, g_tra = [], [], [], []
for num, t in entries:
    (g_syn if num == 0 else g_tra if num in TRANS else g_cas if num in CAS else g_lev).append((num, t))

mots = sum(len(open(p, encoding='utf8').read().split()) for p in tous)
note = ('Chaque section a été rédigée après vérification adversariale de son matériau de recherche, '
        'puis les contradictions entre sections ont été arbitrées sur source primaire et les sources '
        'douteuses vérifiées une à une. Les mentions de niveau de preuve sont signalées dans le texte : '
        '<span class="ev ev-fort"><span class="ev-dot"></span>essai randomisé ou méta-analyse</span>, '
        '<span class="ev ev-mid"><span class="ev-dot"></span>quasi-expérimental</span>, '
        '<span class="ev ev-faible"><span class="ev-dot"></span>corrélationnel ou descriptif</span>.')

open(OUT + "/rapport-reformes-scolaires.html", "w", encoding='utf8').write(page(
    "Réformes scolaires : la preuve",
    "Revue de preuves internationale · septembre 2026",
    "Ce qui fait réussir une réforme scolaire",
    "Quarante et une sections pour fonder une version 2.0 du Pacte pour un Enseignement d’excellence.",
    [("mots", "{:,}".format(mots).replace(",", " ")), ("sections", str(len(entries) - 1)),
     ("études de cas", str(len(g_cas))), ("leviers", str(len(g_lev)))],
    note, secs,
    [("Synthèse", g_syn), ("Études de cas", g_cas), ("Leviers", g_lev), ("Sections transversales", g_tra)]))

# ============ synthèse seule ============
ssecs, sentries = rendre(syn_p)
smots = len(open(syn_p[0], encoding='utf8').read().split())
# ancres de sous-titres pour le sommaire de la synthèse
sub = re.findall(r'<h3 id="(s0-[^"]+)">(.*?)</h3>', ssecs[0])
toc_syn = [(0, "Synthèse générale")]
syn_html = page(
    "Synthèse générale des réformes",
    "Synthèse · septembre 2026",
    "Ce qui fait réussir une réforme scolaire",
    "La synthèse générale : invariants, hiérarchie des leviers, délais, erreurs de conception et priorités pour la Fédération Wallonie-Bruxelles.",
    [("mots", "{:,}".format(smots).replace(",", " ")),
     ("sections synthétisées", "41"), ("corpus d’origine", "170 000 mots")],
    note, ssecs, [("Sommaire", toc_syn)])
# sommaire de la synthèse : ses propres sous-parties
nav = ['<div class="grp">Sommaire</div><ul>'] + [
    '<li><a href="#%s" data-k="%s"><span class="n">%d</span><span>%s</span></a></li>'
    % (i, re.sub('<[^>]+>', '', t).lower(), k + 1, re.sub('<[^>]+>', '', t))
    for k, (i, t) in enumerate(sub)] + ['</ul>']
syn_html = re.sub(r'<nav id="toc" aria-label="Sommaire">.*?<p class="none"',
                  '<nav id="toc" aria-label="Sommaire">' + ''.join(nav) + '<p class="none"',
                  syn_html, flags=re.S)
syn_html = syn_html.replace('<section id="s0">', '<section id="s0" style="padding-top:0;border-top:0">')
open(OUT + "/synthese-reformes-scolaires.html", "w", encoding='utf8').write(syn_html)

for f in ("rapport-reformes-scolaires.html", "synthese-reformes-scolaires.html"):
    p = OUT + "/" + f
    print("%-42s %8.1f Ko" % (f, os.path.getsize(p) / 1024))
