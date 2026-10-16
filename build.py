"""Builds the static site from content.py:  python3 build.py   ->  index.html + projects/*.html"""
import html
import pathlib

import content as C

ROOT = pathlib.Path(__file__).resolve().parent
e = html.escape


def head(title, desc, depth=0):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="name" href="{up}index.html">{e(C.NAME)}</a>
  <nav><a href="{up}index.html#projects">Projects</a><a class="hide-sm" href="{up}index.html#how">How I work</a><a class="hide-sm" href="{up}index.html#about">About</a><a href="{up}index.html#contact">Contact</a></nav>
</div></header>
<main>
"""


def foot():
    return f"""</main>
<footer><div class="wrap">All project data is fictitious: no real company, guest or employee data was used. · <a href="{C.GITHUB}">GitHub</a></div></footer>
</body>
</html>
"""


def contact_buttons(primary_first=True):
    items = []
    if C.EMAIL:
        items.append(("Email me", f"mailto:{C.EMAIL}"))
    if C.LINKEDIN:
        items.append(("LinkedIn", C.LINKEDIN))
    items.append(("GitHub", C.GITHUB))
    return "".join(f'<a class="btn{" primary" if i == 0 and primary_first else ""}" href="{e(u)}">{e(t)}</a>' for i, (t, u) in enumerate(items))


def index():
    cards = "".join(f"""
  <a class="card" href="projects/{p['slug']}.html">
    <div class="thumb"><img src="assets/img/{p['card_img']}" alt="{e(p['name'])} screenshot" loading="lazy"></div>
    <div class="body">
      <h3>{e(p['name'])}</h3>
      <p class="tag">{e(p['tagline'])}</p>
      <p class="result">{e(p['result'])}</p>
      <div class="chips">{''.join(f'<span>{e(t)}</span>' for t in p['tools'])}</div>
    </div>
  </a>""" for p in C.PROJECTS)
    steps = "".join(f'<div class="step"><b>{e(t)}</b><p>{e(d)}</p></div>' for t, d in C.HOW_I_WORK)
    resume = f'<a class="btn" href="{e(C.RESUME)}">Resume (PDF)</a>' if C.RESUME else ""
    about = "".join(f"<p>{e(p)}</p>" for p in C.ABOUT)
    return head(f"{C.NAME} · AI automation for operations", C.HEADLINE) + f"""
<div class="wrap">
<section class="hero">
  <h1>{e(C.HEADLINE)}</h1>
  <p class="sub">{e(C.SUBHEAD)}</p>
  <p class="intro">{e(C.INTRO)}</p>
  <div class="buttons"><a class="btn primary" href="#projects">See the projects</a>{resume}{contact_buttons(primary_first=False)}</div>
</section>
<section id="projects"><h2>Projects</h2><div class="cards">{cards}
</div></section>
<section id="how"><h2>How I work</h2><div class="steps">{steps}</div></section>
<section id="about" class="about"><h2>About</h2>{about}</section>
<section id="contact"><div class="contact"><h2>Contact</h2>
  <p>Open to AI automation, operations and business analyst roles on Oahu or remote.</p>
  <div class="buttons">{contact_buttons()}</div></div></section>
</div>
""" + foot()


def project(i, p):
    ul = lambda xs: "<ul>" + "".join(f"<li>{e(x)}</li>" for x in xs) + "</ul>"
    figs = "".join(f'<figure><img src="../assets/img/{f}" alt="{e(cap)}" loading="lazy"><figcaption>{e(cap)}</figcaption></figure>' for f, cap in p["images"])
    links = "".join(f'<a class="btn{" primary" if j == 0 else ""}" href="{e(u)}">{e(t)}</a>' for j, (t, u) in enumerate(p["links"]))
    prev_p, next_p = C.PROJECTS[i - 1], C.PROJECTS[(i + 1) % len(C.PROJECTS)]
    return head(f"{p['name']} · {C.NAME}", p["tagline"], depth=1) + f"""
<div class="wrap project">
  <div class="crumbs"><a href="../index.html#projects">← All projects</a></div>
  <h1>{e(p['name'])}</h1>
  <p class="tag">{e(p['tagline'])}</p>
  <div class="buttons">{links}</div>
  <div class="result-box">{e(p['result'])}</div>
  <div class="prose">
    <h2>The problem</h2><p>{e(p['problem'])}</p>
    <h2>What I built</h2>{ul(p['built'])}
  </div>
  {figs}
  <div class="prose">
    <h2>How I know it works</h2>{ul(p['proof'])}
    <h2>Results</h2>{ul(p['results'])}
    <h2>What I'd do next</h2>{ul(p['next'])}
    <p class="note">Tools: {e(' · '.join(p['tools']))}</p>
  </div>
  <div class="next-prev"><a href="{prev_p['slug']}.html">← {e(prev_p['name'])}</a><a href="{next_p['slug']}.html">{e(next_p['name'])} →</a></div>
</div>
""" + foot()


(ROOT / "index.html").write_text(index())
(ROOT / "projects").mkdir(exist_ok=True)
for i, p in enumerate(C.PROJECTS):
    (ROOT / "projects" / f"{p['slug']}.html").write_text(project(i, p))
print("built index.html and", len(C.PROJECTS), "project pages")
