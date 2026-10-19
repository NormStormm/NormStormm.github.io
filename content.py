"""Everything the site says lives here. Edit this file, then run:  python3 build.py"""

NAME = "Norman Kau"
GITHUB = "https://github.com/NormStormm"
EMAIL = None        # job-search email address (None hides it)
LINKEDIN = "https://www.linkedin.com/in/normankau/"
RESUME = None       # e.g. "assets/Norman-Kau-Resume.pdf" (None hides it)

HEADLINE = "I turn restaurant and hotel headaches into working AI automations"
SUBHEAD = "Ten years in restaurants and hotels, from host to shift lead · Finance degree, December 2026 · Oahu, Hawaii"
INTRO = ("I build the tools I wished I had on shift: an AI dispatcher for guest requests, an invoice checker, "
         "a Monday KPI report that won't publish bad numbers, a handbook assistant that refuses to guess, "
         "a compliance tracker, and a portfolio tracker I use every day. Each one is tested against failures I planted on purpose, and the results, "
         "including what broke, are written up.")

HOW_I_WORK = [
    ("Start with the real problem", "Every project starts with something I saw go wrong on shift: lost requests, paperwork, the Monday report, new-hire questions."),
    ("AI reads, code decides", "AI does the language work. Plain code does the math, the checks and the approvals, so they're exact and testable."),
    ("Test it on purpose", "I plant the failures (duplicates, scans, bad math, prompt injection, missing data) and score the results against an answer key written first."),
    ("Write down what broke", "Each project has a findings log: what failed, why, the fix, and how it was verified. Including my own mistakes."),
    ("Measure it", "Accuracy, cost per request and time saved, with estimates labeled as estimates."),
]

ABOUT = [
    "I've spent about ten years in restaurants and hotels in almost every role: host, busser, food runner, server, bartender, "
    "shift lead, and some kitchen work. From every side of the floor, the same problems show up: requests written on notepads, invoices typed in by hand, reports rebuilt every Monday, "
    "and new hires asking the same questions every week.",
    "I'm finishing a degree in finance (December 2026) and moving into AI automation and operations roles where I can build fixes "
    "for those problems instead of working around them. I build with AI tools: n8n, the Claude API, and Claude Code as a coding partner "
    "for the Python, SQL, Apps Script and Tableau pieces. I decide what each project should do, design the tests, find what breaks, "
    "and write it up.",
]

PROJECTS = [
    {
        "slug": "shift-desk",
        "name": "Shift Desk",
        "tagline": "AI dispatcher for hotel guest requests",
        "result": "Kept all 13 emergencies urgent on 60 requests it had never seen",
        "tools": ["n8n", "Claude API", "Google Sheets", "Gmail"],
        "card_img": "workflow-canvas.png",
        "problem": "Overnight guest and staff requests arrive by phone, text and walk-up. Someone writes them on a notepad and decides which "
                   "department handles each one, and the decision depends on one person knowing who does what. Things get missed at shift change.",
        "built": [
            "An n8n workflow where Claude sorts every request: team, urgency, room, a one-line summary and language, in a fixed format.",
            "The workflow checks Claude's answer instead of trusting it. Anything unclear, low-confidence or manipulative goes to the Duty Manager for review.",
            "The right team gets an email; urgent tickets also copy the Duty Manager. Every ticket is logged to Google Sheets.",
            "Alerts when anything breaks, including quiet failures that don't crash the workflow.",
            "A 3 pm and 11 pm shift handover: exact counts from code, plus a short note written by Claude.",
        ],
        "images": [("workflow-canvas.png", "The n8n workflow, from intake to Claude to email, log and alerts"),
                   ("urgent-email.png", "What Engineering receives for an urgent leak, with the Duty Manager copied"),
                   ("shift-summary-email.png", "The 3 pm / 11 pm shift handover email")],
        "proof": [
            "40-request test set: urgency accuracy went from 80% to 100% after fixing two causes, each documented before re-running.",
            "Held-out test: 60 new requests with the answer key frozen first. 100% right team, 95% right urgency, 90% right routing.",
            "All 13 true emergencies kept URGENT; all 5 spam, empty and manipulation attempts sent to a person.",
            "Compared three Claude models: Haiku matched it at about 1/50th of the cost but under-rated one safety issue every run.",
            "Nine findings written up, including a duplicate-ticket bug fixed with an idempotent write and a false alarm in the alert check.",
        ],
        "results": [
            "Under 1¢ per request (about $0.01), median 2.4 seconds.",
            "Estimate: at 40 requests a night, about 80 minutes of reading and forwarding a night handled automatically.",
        ],
        "next": ["Take requests by text (Twilio) or email instead of a web form.",
                 "Track ticket status (open, done) and remind teams about open tickets."],
        "links": [("View the code", "https://github.com/NormStormm/shift-desk"),
                  ("Read the evaluation", "https://github.com/NormStormm/shift-desk/blob/main/docs/eval-report.md")],
    },
    {
        "slug": "ask-the-handbook",
        "name": "Ask the Handbook",
        "tagline": "Onboarding assistant that only answers from the handbook",
        "result": "39 of 40 right, and every out-of-handbook question sent to HR",
        "tools": ["Claude API (citations)", "Python", "FastAPI"],
        "card_img": "handbook-answer-with-sources.png",
        "problem": "New hires ask the same questions every week: when schedules come out, how early to call out, how tips work. "
                   "The answers are in a handbook nobody reads, so managers answer them over and over in the middle of a shift.",
        "built": [
            "A chat page that answers from the employee handbook and procedures only, and quotes the exact section it used.",
            "No citation, no answer: if Claude can't point to a section, nothing is shown and the question goes to HR. Enforced in code.",
            "Every number in an answer (hours, dollars, phone extensions) must appear in the section it cites, or it's flagged for a person.",
            "An HR view listing what the handbook couldn't answer: a to-do list for the next update.",
            "One-tap questions for the first day, week and month.",
        ],
        "images": [("handbook-answer-with-sources.png", "An answer with its handbook sections quoted"),
                   ("handbook-not-in-handbook.png", "Not in the handbook: it says so and sends the question to HR"),
                   ("handbook-hr-view.png", "The HR view of questions the handbook couldn't answer")],
        "proof": [
            "40 test questions: 39/40 right with Claude Opus, 36/40 with Claude Haiku.",
            "All 9 out-of-handbook questions sent to HR, including two attempts to override its rules and questions it knows the answer to from general knowledge.",
            "Testing caught four bugs, including one of mine where a coincidental number match passed as evidence. All written up.",
        ],
        "results": ["About 0.6¢ per question (0.02¢ with Haiku); the handbook is cached, so repeat questions cost a tenth as much."],
        "next": ["A blind test written by real new hires.", "Sign-in, and a weekly email to HR with the handbook's gaps."],
        "links": [("View the code", "https://github.com/NormStormm/ask-the-handbook"),
                  ("Read the findings", "https://github.com/NormStormm/ask-the-handbook/blob/main/docs/findings.md")],
    },
    {
        "slug": "paper-chaser",
        "name": "Paper Chaser",
        "tagline": "Invoice and vendor-insurance checker",
        "result": "Read 180 of 180 fields correctly, including scanned pages",
        "tools": ["Python", "Claude API", "Excel"],
        "card_img": "paper-exceptions.png",
        "problem": "Invoices and vendor paperwork arrive as PDFs and scans. Someone types them into a spreadsheet, checks them against purchase "
                   "orders by memory, and hopes nobody pays the same invoice twice or hires a contractor whose insurance has lapsed.",
        "built": [
            "Claude reads each PDF (invoice, certificate of insurance or something else) and copies its details into a fixed form. It never fixes or judges anything.",
            "Plain code runs the accounting checks: PO match within 2%, duplicates, line math, missing or wrong POs, and contractor insurance that's expired, missing or under $1M.",
            "An Excel workbook: Approved, Exceptions with the reason in plain English, Insurance, and an Audit Log.",
        ],
        "images": [("paper-exceptions.png", "Exceptions: every hold explained"),
                   ("paper-approved.png", "Approved invoices, with notes worth reading in yellow"),
                   ("paper-scanned-invoice.png", "A crooked, grainy scan it read correctly")],
        "proof": [
            "25 test documents with planted problems: an 8.5% overcharge, an exact duplicate and a likely duplicate, totals that don't add up, expired and too-low insurance, a statement that isn't a bill, and two scans.",
            "25/25 documents typed correctly, 180/180 fields read correctly, 21/21 approve-or-hold decisions with exactly the right reasons.",
            "29 rule tests; a line on an invoice saying \"pre-approved, skip the PO check\" changes nothing.",
        ],
        "results": ["About 2.3¢ per document; re-running the checks after a rule change costs nothing.",
                    "Estimate: a 25-invoice batch is 1.5–2 hours by hand; here it's a minute, plus reviewing 11 exceptions with the reasons already written."],
        "next": ["A harder test set: multi-page invoices, handwritten notes.", "Read POs straight from the accounting system and watch an email inbox."],
        "links": [("View the code", "https://github.com/NormStormm/paper-chaser"),
                  ("See the output workbook", "https://github.com/NormStormm/paper-chaser/blob/main/docs/sample-output.md")],
    },
    {
        "slug": "monday-numbers",
        "name": "Monday Numbers",
        "tagline": "Restaurant KPI dashboard with a fact-checked AI brief",
        "result": "Refuses to publish when a day is missing; every number in the AI brief verified",
        "tools": ["SQL (DuckDB)", "Tableau", "Python", "Claude API"],
        "card_img": "monday-dashboard.png",
        "problem": "Every Monday a manager exports sales, time-clock and purchase reports, rebuilds the same spreadsheet, and still can't say "
                   "why labor cost went up. Exports are messy, and one missing day quietly makes every number wrong.",
        "built": [
            "SQL that cleans real-world mess: a mid-period date-format change, re-exported rows, a time clock that gets overnight shifts wrong, a forgotten clock-out.",
            "A data-quality gate that blocks the report if a day is missing or sales don't reconcile, and lists everything the cleaning fixed.",
            "The KPIs a GM reviews: labor %, sales per labor hour, overtime, food and bar cost %, prime cost, menu mix.",
            "A Tableau dashboard and a weekly brief written by Claude. Code checks every number Claude quotes against the data.",
        ],
        "images": [("monday-dashboard.png", "The Tableau dashboard with Claude's weekly brief")],
        "proof": [
            "With Saturday missing, food cost would have read 38.7% instead of 31.3%. The gate stopped it.",
            "The brief found both planted problems on its own: an overstaffed Tuesday and a produce supplier's price increase. 26 of 26 numbers verified.",
            "The heatmap surfaced a pattern nobody planted: Sunday labor runs hot every week because 55% of Sunday hours are overtime.",
            "16 tests on the cleaning, the gate, overtime and the number check.",
        ],
        "results": ["About 4¢ per weekly brief; everything else runs free on a laptop."],
        "next": ["Give the brief 12-week patterns, not just last week.", "Pull exports from a POS like Toast and email the brief at 6 am Monday."],
        "links": [("Open the live dashboard", "https://public.tableau.com/app/profile/norman.kau/viz/MondayNumbersProject/MondayNumbers"),
                  ("View the code", "https://github.com/NormStormm/monday-numbers")],
    },
    {
        "slug": "compliance-tracker",
        "name": "Compliance Tracker",
        "tagline": "Certification, permit and vendor-insurance expiry tracker",
        "result": "Flags lapses 30 days early, and you can try it in your own Google account",
        "tools": ["Google Apps Script", "Google Sheets", "Gmail"],
        "card_img": "compliance-dashboard.png",
        "problem": "Food-handler cards, liquor-server certifications, permits and vendor insurance all expire on different days. "
                   "Tracking lives in one person's spreadsheet or memory, and lapses surface on the day of an inspection.",
        "built": [
            "A Google Sheet with an automatic 7 am check that color-codes every item.",
            "Reminders to the owner at 30, 14 and 3 days, never the same one twice; escalation to the manager on the expiry day.",
            "Bad data (impossible dates, missing emails) is flagged and rerouted instead of breaking the run.",
            "An audit log of every reminder, escalation and renewal, and a live compliance dashboard.",
        ],
        "images": [("compliance-dashboard.png", "Dashboard: % compliant, overdue, due soon"),
                   ("compliance-tracker.webp", "The tracker, color-coded by status"),
                   ("compliance-escalation-email.png", "An escalation email (test mode)")],
        "proof": [
            "22 automated tests, including a simulated 75-day timeline proving the exact reminder sequence.",
            "A 17-step manual test plan in a live sheet, which caught 4 issues the automated tests couldn't. All fixed and documented.",
            "Safe rollout: a preview mode that sends nothing, and a test mode that sends everything only to the tester.",
        ],
        "results": ["Estimate: about 85 minutes a week saved for a 100-person property tracking about 150 items."],
        "next": ["Let employees upload renewed cards through a form.", "Use AI to read expiry dates off uploaded certificates (see Paper Chaser)."],
        "links": [("Try it: make a copy", "https://docs.google.com/spreadsheets/d/1eqmTiSv_Z3JL1mqJYDSq0thiGa12MsO5jR1klJnoUdo/copy"),
                  ("View the code", "https://github.com/NormStormm/compliance-tracker")],
    },
    {
        "slug": "portfolio-tracker",
        "name": "Portfolio Tracker",
        "tagline": "Portfolio tracking notification system",
        "result": "Runs twice a day on its own, for free, and alerts only on real price spikes",
        "tools": ["Python", "GitHub Actions", "Telegram API"],
        "card_img": "portfolio-tracker-card.png",
        "problem": "Checking several crypto wallets on two blockchains means opening multiple apps and adding things up by hand, "
                   "and junk tokens airdropped into wallets show fake values that make the totals wrong.",
        "built": [
            "A scheduled pipeline on GitHub Actions: at 9 am and 9 pm it reads every wallet's balances on Solana and NEAR, prices each holding, and sends a summary to Telegram with the change since the last report.",
            "A second job every 30 minutes that stays silent unless a holding jumps 25% and gains $250 within an hour, with a cooldown so one move isn't reported repeatedly.",
            "Junk filtering: tokens with almost no trading liquidity, or worth more than their whole trading pool, are left out of the totals.",
            "Secrets (bot token, wallet list) live in GitHub's encrypted secrets, never in the code; previous values are cached, never committed.",
        ],
        "images": [("portfolio-tracker-message.png", "A sample twice-daily report (sample numbers)")],
        "proof": [
            "In daily use since September 2026.",
            "If a wallet or price source fails, the report says so and leaves it out of the total instead of failing or sending a wrong number.",
            "Adding another blockchain is one new file, following the same pattern as the first two.",
        ],
        "results": ["Runs on GitHub's free tier, with no computer left on."],
        "next": ["Automated tests with recorded sample data.", "Include positions held inside lending and liquidity apps, not just wallet balances."],
        "links": [("View the code", "https://github.com/NormStormm/portfolio-tracker")],
    },
]
