---
type: concept
aliases: ["attack surface management", "ASM", "external attack surface", "EASM", "external attack surface management"]
tags: [attack-surface-management, cybersecurity, infosec, exposure-management, shadow-it]
confidence: 0.75
last_confirmed: "2026-09-19"
accessed_at: "2026-09-19"
source_count: 6
relationships:
  - type: depends-on
    target: osint
    via: "ASM uses OSINT techniques to discover externally visible assets"
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# Attack Surface Management

The continuous discipline of **discovering, cataloguing, and monitoring every externally observable asset** that belongs to an organisation, so that exposure is known before an attacker uses it. The operating principle, in the framing of [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]]: *"You can't protect what you can't see."*

## Working definition

Attack-surface management (ASM) — sometimes "external attack surface management" (EASM) when the scope is specifically internet-visible assets — answers four operational questions on a continuous loop:

1. **What assets does my organisation expose to the public internet?** (Servers, subdomains, certificates, cloud buckets, APIs, IoT, ICS/SCADA, login panels.)
2. **Which exposed assets are known to my security team, and which are not?** (The unknown set is **shadow IT** — forgotten dev servers, legacy systems, employee-spun cloud resources.)
3. **What is the security posture of each exposed asset?** (Vulnerabilities, misconfigurations, leaked credentials, exposed code.)
4. **What changed since the last scan?** (New asset appeared, old asset became vulnerable, certificate expired, credential leaked.)

The discipline is *continuous* by construction — the attack surface drifts as the organisation deploys new services, employees leave systems behind, and the internet itself reshuffles around it.

## Key claims

### ASM presupposes OSINT — the discovery layer is the same

Per [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]]: the platforms that map an organisation's attack surface — Shodan, Censys, FOFA, ZoomEye, FullHunt, SecurityTrails, SpiderFoot — are the same platforms attackers use for reconnaissance. ASM is **defensive [[osint|OSINT]] organised as continuous practice**. The asymmetry between attacker and defender is not in the tools; it is in *who runs them first and how often*.

### The five-step OSINT workflow is the ASM workflow

The same five-step recon flow that an attacker would run against a target is the workflow a defender runs against their own organisation (TechLatest 2026):

1. **Discover infrastructure** — Shodan / Censys / FOFA / ZoomEye to enumerate exposed services.
2. **Enumerate domains & certificates** — crt.sh / SecurityTrails / FullHunt for subdomains and certificate-transparency-derived assets.
3. **Analyse web technologies** — URLScan and Grep.app to detect tech stacks and find leaked secrets in public code.
4. **Check identity exposure** — Hunter / HIBP / DeHashed for harvested emails and breach exposure.
5. **Correlate vulnerabilities** — Vulners (CVEs + exploits) and GreyNoise (separate targeted-vs-noise) to prioritise.

The deliverable is a current map of *what an attacker would learn in two hours of free-tier recon*, which is the question [[2026-04-10-khan-osint-information-gathering-like-a-hacker|Khan 2026]] answered narratively for her own organisation.

### Shadow IT is the load-bearing failure mode

Both wiki sources foreground **shadow IT** — unmanaged, forgotten, or unauthorized assets — as the most exploitable category of attack surface. Khan 2026 found a public GitHub repo with internal API endpoints and a commented-out admin credential that *had been there for three years*. TechLatest 2026 names "shadow IT" explicitly as one of the four Shodan attack-surface-discovery use cases (alongside forgotten servers, old dev systems, misconfigured cloud assets). The pattern: ASM doesn't fail because the team didn't deploy correctly; it fails because the *known set of assets to monitor* doesn't include the ones nobody remembers.

### Five operational best-practices

Per TechLatest 2026, the operational discipline:

1. **Continuously monitor your attack surface** using external scanning against your own infrastructure.
2. **Monitor credential leaks** by tracking employee email exposure in breach datasets.
3. **Audit public repositories** for secrets, API keys, tokens, credentials.
4. **Track shadow IT** — actively hunt unmanaged or unauthorized assets.
5. **Automate reconnaissance** by integrating OSINT platforms into SIEM pipelines, SOC workflows, and threat-intelligence systems.

### Detection-first beats response-first

Both sources converge on a posture: the future of cybersecurity belongs to organisations that **continuously map their attack surface, automate intelligence collection, detect exposure early, and respond faster than attackers** (TechLatest 2026). Khan 2026's narrative is the worked example — once the audit was run, leadership rotated credentials and set up automated public-repo secret scanning. The fix came *after* the discovery; the discovery was the bottleneck.

## Debates and supersession

- **Open question — automation depth.** Both sources advocate automation but neither names a specific reference architecture for an ASM pipeline at production scale. The "AI-Augmented Offensive & Defensive Security" category named in TechLatest 2026 (LLMs + [[ai-agents]] correlating OSINT sources, generating attack graphs) is the plausible future of automated ASM but is still at vendor-narrative depth.
- **Does AI favour the attacker or the defender? (added 2026-09-19)** [[2026-09-10-alim-pydata-ai-security-paradox-asymmetric-threats|Alim]] argues the attacker: recon and exploit generation are nearly free, while patching a large legacy estate is as slow as ever. [[2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness|Mozilla's]] roughly 500 bugs fixed in a month argues the defender. A working reconciliation is that both sides now find vulnerabilities cheaply, but only the defender still has to ship the fix, so the answer depends on patch velocity rather than detection. Neither source measures time-to-exploit against time-to-patch, which is the number that would settle it. **Half-answered 2026-09-19:** [[2026-06-09-cloudflare-investor-day-2026|Cloudflare Investor Day 2026]] charts time-to-exploit falling to under 24 hours in 2026 (see the section below), but cites no source for the series. Time-to-patch is still unmeasured anywhere in the corpus. **Open.**
- **No supersession events yet.** Young concept page; no prior wiki claim to retire.

## Related pages

- [[osint]] — the discovery discipline ASM depends on.
- [[ai-agents]] / [[agent-harness]] — the substrate AI-augmented ASM relies on.
- [[2026-04-10-khan-osint-information-gathering-like-a-hacker|Khan 2026]] — narrative worked example of a one-off audit.
- [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]] — platform catalogue and continuous-workflow framing.

## AI-generated code as an attack surface (added 2026-08-30)

Two 2025 measurements add a surface that ASM's asset-discovery framing does not naturally cover: **the code your own agents write**. Full treatment at [[ai-generated-code-quality]].

**Slopsquatting.** [[2025-06-12-spracklen-package-hallucinations-code-generating-llms|Spracklen et al. (USENIX Security '25)]] generated **2.23M code samples** from **16 models**; **440,445 (19.7%)** contained at least one hallucinated package, across **205,474 unique fictional package names** (≥5.2% commercial models, 21.7% open-source). The mechanism is what makes it an attack surface rather than a bug: **the same model invents the same name repeatedly**, so a *predictable* fictional name can be pre-registered by an attacker on PyPI or npm — the authors' own framing is *"a novel form of package confusion attack."* 205,474 names is the size of the surface, and it is freely derivable by anyone who can run the same models. The control is mechanical and available today: **verify every agent-added dependency against the registry before merge.**

**The flaw baseline.** [[2025-07-30-veracode-2025-genai-code-security-report|Veracode]]: **45% of AI-generated samples introduce OWASP Top 10 vulnerabilities**, with **Java at 72%** against Python's 38% and **XSS failing in 86%** of relevant samples — and, critically, performance **flat regardless of model size or training sophistication**. Security is not on the capability curve, so this is a standing exposure, not a transitional one. [[2026-03-30-liu-debt-behind-the-ai-boom|Liu et al.]] then show **22.7% of AI-introduced issues are still present at the latest repository revision**: the exposure is not being closed.

For the merge-time control that operationalises this, see the *data security* dimension in [[agentic-pull-requests]].

## The asymmetry, restated for the AI era (added 2026-09-19)

This page's premise is that attacker and defender use the same tools, and the asymmetry lies in *"who runs them first and how often."* [[2026-09-10-alim-pydata-ai-security-paradox-asymmetric-threats|Alim (PyData, Sep 2026)]] argues AI tilts that asymmetry toward the attacker. Everyone got faster, but *"attackers gain infinite patience and machine speed — automated recon, tireless fuzzing, exploit generation … at near zero cost,"* while the defender's bottleneck was never discovery.

His image is **the wounded buffalo circled by hyenas**: *"Everyone is quicker, but the asymmetry favors the pack."* The buffalo is any large firm with a big legacy estate: *"AI is actually making them more vulnerable just because patching is still slow even though we have AI"*. Patches must still be tested in lower environments and validated without breaking production.

For ASM this shifts the load-bearing metric. The detection-first posture above assumes that finding exposure early is the bottleneck. If the attacker's reconnaissance is now continuous and free, the detection advantage narrows and **time from discovery to deployed fix** becomes the defender's real variable. Detection stays necessary, but it no longer differentiates. The counter-case is [[2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness|Mozilla]]; see *Debates*.

## Time from disclosure to exploitation: the attacker's window, charted (added 2026-09-19)

[[2026-06-09-cloudflare-investor-day-2026|Cloudflare Investor Day 2026]] includes the series the asymmetry debate above needs, **average time between vulnerability disclosure and confirmed exploitation**:

| 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.3 yrs | 1.9 yrs | 1.3 yrs | 11 mo | 10 mo | 5 mo | 56 days | 23 days | **<24 hrs** |

It is titled *"Frontier AI models change the attack landscape"*, projected to fall further in 2027, and set beside Cloudflare's post *"Project Glasswing: what Mythos showed us"* on testing security-focused models against its own infrastructure.

If the series is right, it settles one half of [[2026-09-10-alim-pydata-ai-security-paradox-asymmetric-threats|Alim's]] argument. Once exploitation follows disclosure within a day, **no patch cycle that includes testing in lower environments can close the window**, and the detection-first posture this page describes has to assume exploitation is already under way. It also reframes ASM's purpose: continuous discovery of the exposed surface matters less for finding problems first than for knowing **what to isolate** when a disclosure lands.

**Treat it with caution.** The slide cites **no source and no method** for a chart other pages will want to quote. It comes from an investor presentation by a security vendor, and its steepest drop coincides with a model release the vendor has reason to dramatise. The direction matches public time-to-exploit reporting; the specific values are Cloudflare's. [[2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness|Mozilla's]] defender-side results are the counterweight: the same class of model that shortens the attacker's window also found roughly 500 bugs in a month for a defender.
