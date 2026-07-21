---
zotero_item_key: CR5UBNXW
zotero_collection: ai-wiki
item_type: preprint
title: The AI Layoff Trap
authors:
- Brett Hemenway Falk
- Gerry Tsoukalas
date_published: '2026-06-03'
doi: 10.48550/arXiv.2603.20617
isbn: ''
url: http://arxiv.org/abs/2603.20617
citekey: ''
abstract: If AI displaces human workers faster than the economy can reabsorb them, it risks eroding the
  very consumer demand firms depend on. We show that knowing this is not enough for firms to stop it.
  In a competitive task-based model of a transitioning economy, each firm captures the full cost saving
  from automation but bears only a fraction of the demand loss it creates in the product market; the rest
  falls on rivals. This demand externality traps rational firms in an automation arms race, displacing
  workers well beyond what is collectively optimal. The resulting loss harms both workers and firm owners.
  More competition and “better” AI amplify the excess; wage adjustments and free entry cannot eliminate
  it. Neither can capital income taxes, worker equity, universal basic income, upskilling, or Coasean
  bargaining. A Pigouvian automation tax can. The results suggest that policy should address not only
  the aftermath of AI labor displacement but also the competitive incentives that drive it.
attachment: the-ai-layoff-trap.pdf
fulltext_source: pdf-converted
converter: pdftotext
notes: Acquired from Zotero collection `ai-wiki`. itemType `preprint` routed to raw/papers/ — confirm
  routing + identity at Process.
---

                                                                                The AI Layoff Trap

                                                                         Brett Hemenway Falk, Gerry Tsoukalas∗

                                                                                         June 3, 2026
                                                                               (first version: March 2, 2026)




arXiv:2603.20617v3 [econ.TH] 3 Jun 2026
                                                                                           Abstract
                                                      If AI displaces human workers faster than the economy can reabsorb them, it risks eroding
                                                  the very consumer demand firms depend on. We show that knowing this is not enough for firms
                                                  to stop it. In a competitive task-based model of a transitioning economy, each firm captures
                                                  the full cost saving from automation but bears only a fraction of the demand loss it creates
                                                  in the product market; the rest falls on rivals. This demand externality traps rational firms
                                                  in an automation arms race, displacing workers well beyond what is collectively optimal. The
                                                  resulting loss harms both workers and firm owners. More competition and “better” AI amplify
                                                  the excess; wage adjustments and free entry cannot eliminate it. Neither can capital income
                                                  taxes, worker equity, universal basic income, upskilling, or Coasean bargaining. A Pigouvian
                                                  automation tax can. The results suggest that policy should address not only the aftermath of
                                                  AI labor displacement but also the competitive incentives that drive it.

                                                  Keywords: artificial intelligence, automation, labor displacement, Pigouvian tax.




                                          1       Introduction

                                          The fear that technology will displace workers is at least as old as the Industrial Revolution (Ricardo,
                                          1821; Keynes, 1930). Historically, displacement has largely been self-correcting: automation of
                                          existing tasks has been offset by the creation of new tasks and occupations. What Acemoglu
                                          and Restrepo (2018, 2019) call the reinstatement effect has tended to stabilize the labor market.
                                          Whether this balance will hold in the age of AI is an open question: Autor et al. (2024) find
                                          that displacement has intensified over the past four decades while the creation of new work has not
                                          always kept pace, and early signs suggest the current wave is disproportionately affecting entry-level
                                          workers (Brynjolfsson et al., 2025a).
                                              ∗
                                              Hemenway Falk: University of Pennsylvania (fbrett@cis.upenn.edu), Tsoukalas: Boston University (ger-
                                          ryt@bu.edu). We thank Ricardo Caballero, Robert Engle, Rep. Bill Foster, Anindya Ghose, Kartik Hosanagar,
                                          Kose John, Leonid Kogan, Giacomo Mantegazza, Serguei Netessine, Fahad Saleh, Larry Summers, Prasanna Tambe,
                                          and S. Alex Yang for helpful comments and discussions. All errors are our own.


                                                                                                1
   Even if reinstatement eventually occurs, a problem arises along the way: displaced workers
are also consumers, and when their lost income is not replaced, each round of layoffs erodes the
purchasing power all firms depend on. At the limit, this becomes self-destructive: firms automate
their way to boundless productivity and zero demand. Public discourse increasingly treats this
dynamic as an inevitable process with no natural brake (van Geelen and Shah, 2026). But rational,
forward-looking firms should be the brake; if the cliff ahead is visible to all, why would they race
toward it?
   Yet the evidence suggests firms are heading in precisely that direction. In February 2026, Block
cut nearly half its 10,000-person workforce, with CEO Jack Dorsey stating that AI had made many
of those roles unnecessary and that “within the next year, the majority of companies will reach the
same conclusion” (Palmer, 2026). In 2025, U.S. employers announced more than a million job cuts,
and AI was explicitly cited in roughly 55,000 of them, led by technology firms and concentrated in
customer support, content moderation, and middle management (Bhaimiya, 2025). The exposure
extends beyond tech: Eloundou et al. (2024) estimate that roughly 80% of U.S. workers hold jobs
with tasks exposed to large language models. Early demand-side indicators are consistent with
the predicted strain: in Q1 2026, business investment overtook consumer spending as the leading
contributor to U.S. GDP growth (Bureau of Economic Analysis, 2026a), and the personal savings
rate fell to 3.6% in March, its lowest level since late 2022 (Bureau of Economic Analysis, 2026b).
None of this is hidden. Against this backdrop, we ask under what conditions rationality and
perfect foresight are enough to prevent competitive over-automation, what determines the size of
the distortion when they are not enough, and which proposed policy responses correct it.
   To answer these questions, we develop a task-based automation model inspired by Acemoglu
and Restrepo (2018), but refocused from the labor market to the product market: when automation
displaces workers, their forgone spending reduces every firm’s revenue. Each of several symmetric
firms chooses what fraction of its workforce to replace with AI. Automated tasks are performed at
lower cost, but integration frictions make each successive task harder to automate. On the demand
side, workers spend a fraction of their income on the sector’s output; firm owners spend less,
normalized to zero in the baseline. Some displaced wage income is recovered through reemployment
or transfers, but the remainder is lost to the sector. The model is deliberately stripped down to make
this channel transparent, and the demand cliff ahead visible to all firms. The baseline holds wages
fixed (relaxed in Section 5.3) and shuts down capital-income recycling (relaxed in Section 5.4);
other baseline assumptions are also relaxed in Section 5. Despite its parsimony, the framework
accommodates a range of policy instruments (Section 4) and robustness checks.


                                                  2
   We show that competition creates a demand externality that traps firms. An automating firm
captures the full cost saving but, under competitive pricing, bears only a fraction of the resulting
aggregate demand destruction; the rest falls on rivals. Each firm’s profit-maximizing automation
rate is a strictly dominant strategy that exceeds the cooperatively efficient level, so foresight alone
cannot prevent the race toward the cliff. The distortion deepens with competition: a monopolist
fully internalizes the externality, while fragmented markets exhibit the widest gap. In the frictionless
limit, where every task is equally easy to automate, the game sharpens into a Prisoner’s Dilemma
in which every firm displaces its entire human workforce with AI, even though collective restraint
would raise all profits. The resulting surplus loss is not a transfer from workers to firm owners; it
is a deadweight loss that harms both.
   Since the loss falls on both sides, a natural question is whether policy can correct it. We evaluate
six instruments against the externality margin. Upskilling and worker equity participation narrow
the wedge but cannot eliminate it. Nor can Coasean bargaining: because automation is a dominant
strategy, no voluntary agreement among firms is self-enforcing. Capital income taxes do not alter
the equilibrium automation rate, operating on profit levels rather than the per-task margin where
the externality resides. Neither does universal basic income: it raises the floor on living standards
but leaves the automation incentive unchanged. Only a Pigouvian automation tax, set equal to the
uninternalized demand loss per task, implements the cooperative optimum; its revenue can fund
retraining that raises income replacement, shrinking the externality over time and making the tax
potentially self-limiting.
   The core result is also robust to several generalizations. Higher AI productivity widens the wedge
rather than resolving it: each firm perceives a market-share gain from automating beyond rivals, but
at the symmetric equilibrium these gains cancel, leaving only the additional distortion. This Red
Queen effect means that “better” AI, far from mitigating the externality, amplifies it. Endogenous
wage adjustment, a key self-correcting channel in the framework of Acemoglu and Restrepo (2018),
raises the threshold at which the externality activates but, short of collapsing wages to AI’s cost,
cannot close the wedge once it does. Free entry, capital-income recycling, and richer product-market
structures likewise fail to eliminate the distortion.
   Those generalizations all stay within partial equilibrium. This raises the question whether the
demand-destruction channel is itself a partial-equilibrium artifact: in a frictionless multi-sector
general equilibrium (GE), the income lost to displacement could be reabsorbed elsewhere, and the
mechanism may vanish. We argue that both routes for this reabsorption are blocked for the mass-
market firms most exposed to AI. In the product market, displaced spending might rotate to other


                                                   3
goods, but saturation in high-income consumption (Matsuyama, 2002; Comin et al., 2021) and the
inability to retool production quickly (Ramey and Shapiro, 2001) keep it from returning to mass-
market producers. Yet another route runs through the interest rate. The income displaced workers
lose does not leave the economy: automation shifts it toward firm owners, who spend a smaller
share of their income than workers do, so aggregate saving rises. In a frictionless economy a falling
interest rate would put that saving back to work as investment and borrowing by others, holding
total demand steady. This adjustment stalls, though, when interest rates are already near zero and
cannot fall further, or when the income loss is lasting rather than temporary, so displaced workers
cannot borrow their way through it. Section A discusses these channels in detail.
   Our work contributes to several literatures. We build on the task-based approach to automation
(Zeira, 1998; Autor et al., 2003; Acemoglu and Restrepo, 2018, 2019), which emphasizes offsetting
forces that restore labor demand after displacement, notably new task creation and a self-correcting
wage channel. Acemoglu (2025) evaluates the aggregate productivity effects of AI within this
framework. These contributions focus on whether and how the labor market rebalances; we ask
what happens on the product-market side when rebalancing is slow or incomplete.
   A growing literature argues that automation may be excessive. The closest to our setting is
Beraja and Zorzi (2025), who show that automation is inefficient when displaced workers face
borrowing constraints during reallocation. Their mechanism operates through the labor market:
firms ignore the welfare cost imposed on credit-constrained workers. Ours runs through the product
market instead, with firms ignoring the demand they destroy for rivals. Two further differences
follow. Their inefficiency arises even for a single firm in isolation, whereas ours requires competition
and vanishes under monopoly. And while their planner corrects automation to protect worker
welfare, ours would reduce automation even with zero weight on workers, because over-automation
harms firm profits themselves. Other channels for excessive automation share the feature that
they would distort a single firm’s decision even in isolation: the technology ecosystem may be
biased toward “so-so” automation that displaces workers without large productivity gains (Acemoglu
and Restrepo, 2020), automation may disproportionately target high-rent tasks, dissipating worker
surplus rather than raising output (Acemoglu and Restrepo, 2026), and corrective taxation has
been justified by transitional frictions (Guerreiro et al., 2022) and distributional concerns (Costinot
and Werning, 2023). More recently, AI-specific channels of the same in-isolation type have been
identified through skill erosion, productivity mismeasurement, and copyright dynamics that can
depress long-run welfare absent regulation (Caosun and Aral, 2026; Bondi and Johnson, 2026; Yang
and Zhang, 2024). Our externality, by contrast, arises only under competition and persists even


                                                   4
when automation is highly productive, credit markets are complete, and the planner places no
weight on distribution.
    The demand externality we study belongs to the family of aggregate demand spillovers intro-
duced by Rosenstein-Rodan (1943) and formalized by Murphy et al. (1989). In their “big push”
models, demand complementarities across sectors can prevent individually unprofitable investments
from being made even though simultaneous adoption would be collectively profitable. Our mecha-
nism is the mirror image: individually profitable automation is collectively destructive because each
firm’s cost saving erodes the revenue base all firms share. Cooper and John (1988) provide the
canonical framework for coordination failures driven by aggregate demand externalities; our game
shares this setting of aggregate demand spillovers but not its strategic-complementarity structure:
automation here is a strictly dominant strategy, making the problem a true externality rather than
a coordination failure that communication could resolve. Benzell et al. (2015) show in a dynamic
overlapping-generations economy that automation can erode workers’ purchasing power and gen-
erate immiserating growth through capital-accumulation channels. Our contribution is distinct:
even absent these dynamic channels, and even when firms perfectly foresee the demand loss, de-
centralized competition alone induces excessive automation, because each firm captures the full
labor-cost saving while bearing only a fraction of the resulting aggregate demand destruction. Ko-
rinek and Stiglitz (2019) similarly examines AI-driven income redistribution at the aggregate level,
and Caballero (2026) models AI-driven labor displacement and capital concentration as generating
speculative-growth equilibria through a macro-financial funding feedback. Neither features the firm-
level strategic competition in which one firm’s automation choice imposes a demand externality on
rivals.
    The information systems literature has established that AI systems deliver substantial pro-
ductivity gains (Brynjolfsson et al., 2025b) and are increasingly deployed in strategic roles such
as pricing, where algorithms can spontaneously learn to collude (Banchio and Mantegazza, 2022;
Keppo et al., 2026). On the adoption side, Li et al. (2025) show that firms under labor-issue scrutiny
invest specifically in AI automation rather than other forms of IT, and Bastani and Cachon (2025)
show that as AI reliability improves, incentivizing effective human oversight becomes prohibitively
expensive, weakening a key check on automation. What this literature has not modeled is how
these individually documented phenomena interact across firms: each adoption decision is rational
in isolation, but collectively they erode the consumer demand all firms depend on. We provide
that model, connecting the micro-level evidence the IS literature has documented to a macro-level
market failure that no individual firm can prevent.


                                                  5
    The remainder of the paper is organized as follows. Section 2 presents the model. Section 3
derives the equilibrium and the over-automation wedge. Section 4 evaluates policy instruments.
Section 5 extends the model to AI productivity gains, endogenous entry, endogenous wages, capital-
income recycling, and richer product-market interaction. Section 6 discusses implications and limi-
tations.


2    Model

The baseline isolates the demand consequences of automation in the simplest environment that
supports the mechanism: symmetric firms, a single sector, and exogenous wages. We describe the
supply side (cost structure and automation choice), then the demand side (how displacement feeds
back into revenue), and finally the game firms play. Each assumption is relaxed in Section 5.
    Consider a sector with N ≥ 2 symmetric firms, indexed i = 1, . . . , N . It will later become useful
to think of each firm as having a single owner, for example the equity holder, who is entitled to the
firm’s operating profits.
    In the spirit of the task-based framework of Acemoglu and Restrepo (2018), each firm is endowed
with L > 0 task-positions. Initially all tasks are performed by human workers; a new technology
shock arrives, for example agentic AI, and each firm must decide how much of its workforce to
replace. In particular, firm i chooses an automation rate αi ∈ [0, 1]: tasks z ∈ [0, αi ] are performed
by AI at cost c per task, and tasks z ∈ (αi , 1] remain with human workers at wage w per task, with
0 ≤ c ≤ w. Since each automated task displaces one worker, αi is simultaneously the automation
rate and the fraction of the workforce laid off; we use the two descriptions interchangeably. Wages
are exogenous in the baseline; Section 5.3 endogenizes wages.
    In the perfect-substitutes limit of the CES task aggregator in Acemoglu and Restrepo (2018),
each task produces one unit of output regardless of mode, so firm output is Yi = L; Section 5.1 relaxes
this to allow AI to not only reduce costs, but also increase firm output. This normalization shuts
down productivity and quality margins so that the baseline captures only the spending consequences
of labor displacement.
    We follow the literature in assuming tasks are ordered by comparative advantage, making the
marginal task progressively harder to integrate; we capture this via a convex integration cost k2 Lαi2
with k ≥ 0, using the standard quadratic adjustment-cost specification (Lucas, 1967). Firm i’s total




                                                   6
production cost is therefore


                               Ci (αi ) = L αi c + (1 − αi )w + k2 L αi2 .
                                                             
                                                                                                   (1)


Defining the per-task cost saving from automation as s := w − c, the cost equation can be rewritten
as Ci = L(w − s αi ) + k2 L αi2 : each automated task saves s in labor costs but incurs the integration
friction.
    On the demand side, workers have a higher marginal propensity to consume (MPC) than owners
(Kaldor, 1956; Summers, 2014, 2015); workers spend a fraction λ ∈ (0, 1] of their income on the
sector’s good, generating the type of cross-firm demand linkage analyzed by Murphy et al. (1989).
Owners, by contrast, spend none of their income in the sector in the baseline (Section 5.4 relaxes
this). This MPC asymmetry implies that when automation displaces workers, income shifts toward
agents with a lower sectoral MPC, reducing aggregate expenditure on the sector. The asymmetry
itself has a structural foundation: under non-homothetic preferences in which mass-market goods
saturate at high incomes (Matsuyama, 2002; Comin et al., 2021; Boppart, 2014), marginal owner
income flows to a separate luxury segment rather than back to the modeled sector, and firms
specialized to mass-market production cannot quickly retool to capture the redirected demand
(Ramey and Shapiro, 2001; Cooper and Haltiwanger, 2006). Section A discusses the conditions
under which the demand destruction mechanism survives a fuller GE treatment.
    When firm j automates a fraction αj of its tasks, αj L workers are displaced. A fraction η ∈ [0, 1]
of displaced wage income is replaced via reemployment, transfers, or other sources (Jacobson et al.,
1993); the remainder, (1 − η)w per displaced worker, is lost to the sector.
                                                                    P
    Across all N firms, the total number of displaced workers is       j αj L, so total wage income
                                P
lost to displacement is (1 − η)w j αj L. Total labor income in the sector is therefore wLN − (1 −
     P
η)w j αj L, of which a fraction λ is spent on the sector’s good. Adding autonomous demand A > 0
(from outside the sector or from capital income), aggregate sectoral expenditure is

                                             h           P    i
                               D(α) = A + λwL N − (1 − η) j αj .                                   (2)


Writing ᾱ := N1
                   P
                   j αj for the average automation rate, this becomes D = A + λwLN [1 − (1 − η)ᾱ].

Defining the effective demand loss per automated task as


                                            ℓ := λ(1 − η)w,                                        (3)




                                                   7
this simplifies to D = A + λwLN − ℓLN ᾱ: demand falls linearly in the average automation rate.
       Firms sell their output on the product market at a uniform price that equates aggregate supply
and demand. Since all firms produce the same output Yi = L, total supply is N L and the market-
clearing price is p = D/(N L). Each firm earns revenue Revi = p · Yi = D/N , which, after
substituting (2), gives
                                                        A
                                           Revi =         + λwL − ℓLᾱ.                                         (4)
                                                        N
Firm i’s profit is πi = Revi −Ci . Substituting (4) and (1):


                                       πi = Π0 + L s αi − ℓᾱ − k2 αi2 ,
                                                                      
                                                                                                                (5)


where Π0 := A/N + (λ − 1)wL is the per-firm profit when no firm automates. Writing ᾱ =
     P
(αi + j̸=i αj )/N to isolate firm i’s own action:

                                                                   
                                                  
                                                 ℓ    k      ℓ X
                              πi = Π0 + Lαi s −     − αi2 −     αj  .                                         (6)
                                                 N    2      N
                                                                           j̸=i


       Firms play a one-shot simultaneous-move game, each choosing αi to maximize πi ; the prod-
uct market then clears mechanically given the automation profile.1 The solution concept is Nash
equilibrium.
       Define aggregate owner surplus K and aggregate worker income W:

                                                  X
                                           K :=          πi
                                                    i

                                          W := wLN [1 − (1 − η)ᾱ].


We measure over-automation against two benchmarks: the cooperative optimum, which maxi-
mizes K, and a generalized social planner who maximizes


                                          S(µ) := µ W + (1 − µ) K


for a weight µ ∈ [0, 1] on workers.
   1
    An alternative would be a two-stage game in which firms first choose automation rates and then compete on
price or quantity. We abstract from this type of more elaborate second-stage product-market competition because
those strategic effects are already well studied and would obscure the novel mechanism we isolate here: the demand
externality from automation under full transparency. The qualitative results are plausibly robust to richer product-
market interaction, but closed-form solutions would become substantially more complex.




                                                              8
     Note that the environment assumes full transparency: every firm can directly observe how
automation maps into lost worker income and reduced aggregate spending. The question Section 3
answers is whether this visibility alone is sufficient for firms to curb automation in a competitive
setting.


3      Equilibrium and Over-Automation

This section derives the equilibrium, shows firms over-automate relative to the cooperative optimum,
and quantifies the resulting surplus loss. All proofs are collected in Section B.


3.1     Equilibrium and the Over-Automation Wedge

To characterize the equilibrium, consider firm i’s marginal incentive to automate. Recall from (3)
that ℓ(w) = λ(1 − η)w is the demand lost per displaced worker, proportional to the wage because
displaced workers’ forgone spending scales with their earnings. (We write simply ℓ when the wage
is held fixed; Section 5.3 endogenizes w.) From (6), firm i’s marginal profit from automation is
                                                        
                                        ∂πi       ℓ
                                            =L s−   − kαi .
                                        ∂αi       N

A marginal increase in automation saves s in labor costs but incurs friction kαi and reduces the
firm’s revenue by ℓ/N . The revenue loss is ℓ/N rather than ℓ because competitive pricing allocates
revenue equally across symmetric firms (4): firm i’s automation reduces aggregate demand by ℓL,
but only ℓL/N of this falls on firm i itself. Each firm therefore underestimates the social cost of
its automation, suggesting systematic over-automation in equilibrium. The following proposition
confirms this and quantifies the gap.

Proposition 1 (Equilibrium and over-automation). Suppose k > 0 (the frictionless case k = 0 is
treated separately in Corollary 1). In the model defined in Section 2, define the automation threshold

                                                  ℓ   λ(1 − η)w
                                         N ∗ :=     =           .                                  (7)
                                                  s     w−c

If N ≤ N ∗ , no firm automates (αN E = 0).
If N > N ∗ (equivalently, s > ℓ/N ):
    (i) Each firm’s strictly dominant strategy is αN E = min ((s − ℓ/N )/k, 1);
 (ii) The cooperative optimum is αCO = min (max (0, (s − ℓ)/k) , 1);



                                                     9
(iii) If ℓ < s < k + ℓ/N then both αN E and αCO are interior, and the over-automation wedge is

                                                      ℓ (1 − 1/N )
                                   αN E − αCO =                    > 0.
                                                            k

      This is strictly increasing in N and ℓ, and decreasing in k.
 (iv) If s ≤ ℓ, then αCO = 0, and so the wedge is αN E . Thus if s < k + ℓ/N , then αN E =
      (s − ℓ/N )/k, so the wedge is (s − ℓ/N )/k. On the other hand, if k + ℓ/N ≤ s, then αN E = 1,
      so the wedge is 1.

   The proposition follows from the private first-order condition derived above and its cooperative
counterpart: a planner setting a common rate for all firms faces the full demand loss ℓ per automated
task rather than the ℓ/N each firm perceives, yielding αCO = (s − ℓ)/k. Because rivals’ rates
                                       P
enter (6) only through the term −(ℓ/N ) j̸=i αj , which is independent of αi , the equilibrium rate
is a strictly dominant strategy: each firm over-automates even with perfect foresight about every
rival’s behavior.
   The case structure arises because both αN E and αCO lie in [0, 1]: each can be at no automation,
interior, or full automation depending on how the cost saving s compares to the demand-loss and
friction parameters. The wedge is widest where firms automate but the cooperative benchmark
would not (αCO = 0), and it shrinks to zero only once cost savings grow large enough (s ≥ k + ℓ)
to pin both rates at full automation. We caution against reading that zero as a benign region:
the demand externality is still present in firms’ incentives, but the αN E − αCO comparison can no
longer detect it once even the profit-only cooperative benchmark (µ = 0) prescribes displacing the
entire workforce. A more informative comparison there is to a planner who weights worker income,
for whom the gap stays strictly positive (Proposition 2). Parts (iii)–(iv) enumerate the relevant
combinations; the economic force is the same throughout.
   The wedge is strictly increasing in N : more competitive sectors exhibit wider automation gaps.
This runs counter to the standard intuition that competition disciplines firms to act in consumers’
interests; here, more competition dilutes each firm’s share of the demand loss, weakening the private
incentive to restrain. A monopolist (N = 1) fully internalizes the externality (αN E = αCO ); as
N → ∞, the wedge approaches its maximum of ℓ/k.
   From Proposition 1, a firm automates only when N > N ∗ = ℓ/s: the number of competitors
must be large enough that each firm’s share of the demand loss, ℓ/N , falls below its cost saving s.
As AI costs fall (c → 0), N ∗ → λ(1 − η) ≤ 1: the over-automation region expands to cover virtually
any market with N ≥ 2. For illustrative parameters (c/w = 0.30, λ = 0.5, η = 0.30, N → ∞),


                                                 10
                                              (a)                                1.0
                                                                                                       (b)                                      1.0
                                                                                                                                                                     (c)
                         1.0


                         0.8                                                     0.8                                                            0.8




Per-task cost saving s                                                                                                     Income replacement
                                                                                           N=N *
                                                                                                                                                0.6

                                                                   Demand loss
                         0.6                                                     0.6


                         0.4                                                     0.4                                                            0.4
                                                                                                                                                          N=N *
                                                                                 0.2                                                            0.2
                         0.2
                                                 N=N *
                                                                                                                                                0.0
                               1   2      3    4   5       6   7                       1   2      3        4   5   6   7                              1   2      3    4    5      6   7
                                       Number of firms N                                       Number of firms N                                              Number of firms N

Figure 1: The over-automation wedge αN E − αCO across the parameter space. Shading runs from
white (zero wedge) to black (wedge ≥ 0.50). Dashed lines mark the N = N ∗ boundary below which
no firm automates. (a) Number of firms vs. cost saving s = w − c at fixed wage (λ = 0.5, η = 0,
k = 1). (b) Number of firms vs. demand loss ℓ = λ(1 − η)w (c = 0.60, η = 0, k = 1). (c) Number
of firms vs. income replacement (c = 0.60, λ = 1, k = 1).


the wedge equals ℓ/k = αCO : firms in competitive markets automate at twice the cooperatively
efficient rate. This interior comparison should be read with a caveat: it presumes frictions are not
negligible relative to the cost saving (k > s, so that both rates stay interior as N → ∞). When
AI is both cheap and frictionless to integrate, both rates saturate at full automation and the wedge
collapses to the corner noted above, so the factor-of-two statement is specific to the interior regime.
Cheaper AI still worsens the outcome beyond that regime, tipping it into universal displacement,
even though the αN E − αCO wedge no longer registers it.
                         Figure 1 illustrates these comparative statics. In each panel, the dashed line marks the N =
N ∗ boundary below which no firm automates, and darker shading indicates a larger wedge. The
dominant pattern is that the wedge grows with N ; non-monotonicity in the other dimensions reflects
the regime shift at s = ℓ, where the cooperative optimum moves from zero to an interior solution.
                         When frictions are positive, integration costs moderate the equilibrium automation rate. The
next subsection shows that when frictions vanish (k → 0), this moderating force disappears and the
game reduces to a Prisoner’s Dilemma: full automation versus none.


3.2                            Frictionless Automation as a Prisoner’s Dilemma

When k = 0, marginal profit becomes the constant L(s − ℓ/N ), independent of the automation
level, and the outcome is all-or-nothing. If N ≤ N ∗ , no firm automates. If N > N ∗ , automating
is strictly dominant, and collectively harmful when the cost saving falls short of the demand loss

                                                                                                      11
(s < ℓ):

Corollary 1 (Frictionless limit). Suppose adjustment frictions vanish (k = 0) and the number of
firms exceeds the critical threshold (N > N ∗ ).
  (i) Full automation (αi = 1) is strictly dominant for every firm.
 (ii) If additionally the cost saving is less than the demand loss per task (s < ℓ), the cooperative
      optimum is no automation (αi = 0 for all i, yielding per-firm profit Π0 ); the equilibrium yields
      Π0 + L(s − ℓ) < Π0 . Total deadweight loss is N L(ℓ − s).

   Under the condition in part (ii) (s < ℓ), the Prisoner’s Dilemma structure makes the failure of
voluntary restraint transparent. A firm that holds back unilaterally (choosing αi = 0) still suffers
the revenue decline from rivals’ automation but forgoes the offsetting cost savings; a firm that
deviates (choosing αi = 1) captures the savings while imposing only a 1/N share of the demand
loss on itself. The resulting payoff matrix has the classic form: mutual restraint yields Π0 per firm,
while mutual automation yields Π0 + L(s − ℓ) < Π0 , yet defecting is individually rational regardless
of others’ choices. Because automating is strictly dominant (not merely a best response to others’
automating), no non-binding agreement can restore efficiency. Communication is cheap talk: even
if all firms acknowledge that collective restraint would raise profits, each firm’s individually optimal
action remains unchanged. This distinguishes the automation externality from pure coordination
failures (where firms simply need to agree on which equilibrium to play) and motivates the analysis
of Coasean bargaining in Section 4.5.


3.3   Over-Automation as Deadweight Loss

Is the over-automation wedge merely a redistribution from workers to firm owners, or does it reduce
total surplus? Recall the generalized planner introduced in the model section, who maximizes


                                      S(µ) = µ W + (1 − µ) K                                        (8)


for a weight µ ∈ [0, 1] on workers.

Proposition 2 (Generalized planner and surplus loss). Suppose k > 0 and N > N ∗ .
  (i) The µ-planner’s optimal automation rate is

                                                    s−ℓ       µℓ
                                       αSP (µ) :=       −            ,
                                                     k    λ(1 − µ) k



                                                    12
     where, as usual, αSP (µ) is the automation rate, and is thus restricted to the interval [0, 1]. At
     µ = 0 this reduces to αCO from Proposition 1.
 (ii) The surplus loss from the Nash equilibrium relative to the planner’s optimum is

                                            (1 − µ) N Lk  N E          2
                       S µ; αSP − S µ; αN E =                   − αSP (µ) ,
                               
                                                           α
                                                   2

     valid when the planner’s optimum αSP (µ) is interior.
(iii) (Pareto dominance.) αN E > αSP (µ) for every µ ∈ [0, 1), except when cost savings are large
     enough to pin both rates at full automation. Whenever the cooperative rate is interior (αCO <
     1), the Nash equilibrium is Pareto dominated by the cooperative optimum: workers and firm
     owners are both strictly worse off.

   Over-automation is not a transfer from workers to owners: it is a deadweight loss that harms
both sides (part (iii)). Workers lose wage income directly through displacement. Firm owners,
despite cutting costs on each automated task, also lose: collective displacement erodes demand
to the point where every firm’s equilibrium profit falls below its cooperative-optimum profit. No
redistribution between the two groups can make the Nash outcome efficient. Section A discusses
when this lost demand is genuinely destroyed rather than reabsorbed elsewhere, so that the loss is
real rather than merely pecuniary.
   When both αN E and αSP are interior, the total wedge between equilibrium and the planner’s
optimum decomposes into two distinct sources:

                                               ℓ(1 − 1/N )       µℓ
                          αN E − αSP (µ) =                 +            .                          (9)
                          |     {z     }            k        λ(1 − µ) k
                             total wedge
                                               |    {z   }   | {z }
                                             demand externality   distributional


The first term is the uninternalized demand externality from Proposition 1(iii): it is present even
when the planner places zero weight on workers (µ = 0) and cares only about aggregate profit. It
grows with N , approaching ℓ/k as N → ∞, so fragmented markets suffer disproportionately. The
second term is a distributional premium: the additional automation reduction a planner who values
worker income (µ > 0) would impose beyond the profit-maximizing benchmark. It is independent
of N but grows without bound as µ → 1; at µ̄ := λk αCO /(ℓ + λk αCO ) the planner prohibits
automation entirely. The surplus loss in (ii) is quadratic in this total wedge and scales with N L, so
both fragmentation and market size amplify the welfare cost.
   Figure 2 illustrates the Pareto dominance and the decomposition. To make the losses for the
two groups comparable, panels (a) and (b) normalize each payoff by its value at αCO , so a value

                                                  13
                                                           (a)                                                                     (b)                                                                 (c)
                                                                                                                                         =0                                                                              SP( )
                                                             Owner surplus                                                                                                     0.7
                                                             Worker income                                                                                                                                               NE
                                                                                                               1.2




Fraction of cooperative payoff
                                 1.2                                                                                                                                           0.6




                                                                                    Normalized worker income
                                                                                                                                                                               0.5



                                                                                                                                                             Automation rate
                                 1.0                                                                           1.0
                                                                                                                                                     CO
                                                                                                                                                                               0.4                                       CO
                                 0.8                                                                           0.8
                                                                                                                                                                               0.3
                                                                                                                                              NE

                                 0.6                                                                           0.6                                                             0.2
                                                CO                     NE
                                                                                                                                                                               0.1
                                 0.4                                                                           0.4       =1
                                                                                                                                                                               0.0
                                    0.0   0.2        0.4         0.6    0.8   1.0                                    0.80 0.85     0.90       0.95    1.00                        0.0   0.2      0.4         0.6   0.8           1.0
                                            Automation rate                                                          Normalized owner surplus                                                 Worker weight

Figure 2: Welfare consequences of over-automation. All panels use c = 0.30, λ = 0.5, η = 0.30,
N = 7, k = 1, A = 10. (a) Normalized owner surplus K and worker income W vs. automation rate
(1 = cooperative benchmark): both groups lose at αN E . (b) Factor payoff frontier: αCO at (1, 1),
αN E strictly southwest (Pareto dominated). (c) Planner’s optimum αSP (µ) vs. worker weight µ
(not normalized): the gap to αN E is the over-automation wedge, positive even at µ = 0.


of 1 corresponds to the cooperative benchmark. Panel (a) plots the normalized payoffs against the
common automation rate ᾱ: both curves peak at or before αCO and both fall below 1 at αN E . The
equilibrium rate lies to the right of the aggregate profit peak, so that both owner surplus and worker
income are lower than under cooperation. Workers bear the larger loss because their income declines
linearly in ᾱ, while the profit curve is concave and falls more gently. Panel (b) re-expresses the same
information as a factor payoff frontier: each point on the curve corresponds to a different common
automation rate, tracing out the (K, W) pairs as ᾱ increases. The cooperative rate sits at (1, 1) and
αN E is strictly to the southwest, confirming that moving from equilibrium to the cooperative rate
would make both groups better off. Panel (c) visualizes the decomposition in (9): the horizontal
line marks αN E , and the declining curve is the planner’s optimum αSP (µ). Even at µ = 0, the gap
is positive (the demand-externality term alone), and the required correction grows further as the
distributional premium widens with µ.
                                 Since the over-automation wedge is a structural externality that harms both factor classes, a
natural question is whether policy can close it.


4                                  Policy Instruments

Several instruments could in principle address the externality; the question is which ones operate
on the right margin. To answer it, we benchmark against the cooperative optimum αCO , which


                                                                                                                              14
maximizes aggregate profit without directly weighting worker welfare. This is deliberately the
weakest case for intervention: Proposition 2 shows that the demand externality alone reduces both
firm profits and worker income, and that placing any positive weight on workers (µ > 0) only widens
the wedge.
       Table 1 previews the results: only the Pigouvian automation tax fully corrects the distortion;
the remaining instruments cushion the losers or partially shrink the wedge, but none eliminates it.2

            Table 1: Policy instruments and their effects on the over-automation externality.
                                         Section     Changes N ∗ ?      Changes wedge?         Fixes externality?
  Upskilling/retraining (η)                 4.1            Yes                 Yes                   Partially
  Universal Basic Income (A)                4.2            No                  No                      No
  Capital income tax (t)                    4.3            No                  No                      No
  Worker equity (ϵ)                         4.4            Yes                 Yes                   Partially
  Coasean bargaining (M < N )               4.5            No                Partially                 No
  Automation tax (τ )                       4.6            Yes                 Yes                     Yes
 Note. Each row records whether the instrument alters the automation threshold N ∗ , the over-automation wedge
                      ℓ(1 − 1/N )/k, and whether it fully corrects the demand externality.


       One limitation should be noted: the analysis evaluates each instrument against a single margin,
the demand externality identified in Section 3, holding all other features of the economy fixed. In
practice, every instrument carries additional costs and benefits outside the model (administrative
burden, labor-market distortions, political feasibility) that a full welfare analysis would need to
weigh. Nonetheless, an instrument that does not operate on the externality margin cannot cor-
rect the distortion regardless of how it scores on other dimensions; the analysis below separates
instruments that can from those that cannot.


4.1      Displacement vs. Upskilling

The demand-loss parameter ℓ = λ(1 − η)w governs the externality’s magnitude. In the baseline
model, η ∈ [0, 1] represents the fraction of displaced wage income recovered through reemployment,
transfers, or other sources: higher η shrinks ℓ and thereby the over-automation wedge.
       But the parameter extends naturally beyond unity. When η > 1, upskilling and reabsorption
place displaced workers into higher-paying roles, automation increases aggregate labor income, and
   2
    The categorical ranking that follows is stated for the regime in which the externality is active and uninternalized:
λ < 1 (sectoral spending leaks), η < 1 (displacement is not fully reabsorbed), automation rates αi are noncontractible
and unobservable across firms, and N is large. The points at which a non-tax instrument appears to succeed (full
reabsorption η = 1, full recycling λ = 1, full profit-sharing ϵ = 1/λ, which requires ϵ > 1 when λ < 1, or a binding
grand coalition over observable automation) are boundary or knife-edge cases that we flag as each instrument is
discussed; each removes the very leakage or noncontractibility that constitutes the externality, so it confirms rather
than overturns the ranking.


                                                          15
loss ℓ turns negative, which we can interpret as a gain. This is the scenario invoked by AI optimists,
in which technological displacement is a stepping stone to better jobs. As the following corollary
shows, the sign reversal in ℓ flips the externality itself.

Corollary 2 (Sign of the externality). In the interior regime where both rates lie strictly in (0, 1)
(Lemma 1), the over-automation wedge is (αN E − αCO ) = ℓ (1 − 1/N )/k, which is maximized at
η = 0 (where ℓ = λw), positive for all η < 1, zero when η = 1 (where αN E = αCO = s/k), and
negative (under-automation) when η > 1.

   The logic is symmetric. When η < 1, displacement destroys demand, and each firm bears
only 1/N of the loss, producing over-automation. When η > 1, displacement creates demand
through higher reemployment wages, and each firm captures only 1/N of the gain, producing under-
automation. In both cases, the distortion grows with N : more competition dilutes each firm’s share
of the externality, whether that externality is negative or positive. A monopolist (N = 1) fully
internalizes in every case.
   The competitive forces are identical; only the sign of the demand externality differs. As Sec-
tion 4.6 will show, the same corrective instrument addresses both cases: a tax when η < 1, a subsidy
when η > 1.
   The case η > 1 is not merely theoretical. Historical technological transitions have often eventu-
ally reabsorbed displaced workers at higher wages (Acemoglu and Restrepo, 2019), and the current
AI buildout offers a concrete channel: the expansion of data centers, energy infrastructure, and
AI-adjacent services is creating skilled roles that can pay more than the positions automation dis-
places. If this reabsorption is fast enough to push η above unity, competitive firms will automate too
slowly. However, past displacement episodes have consistently produced η < 1: displaced workers
suffer large, persistent earnings losses (Jacobson et al., 1993), and there is little evidence yet that
AI-driven displacement will differ, placing most economies firmly in the over-automation regime.
   The policy implication is that raising η through retraining programs, wage insurance, and in-
centives for new firm creation is not merely a palliative for displaced workers but a direct lever
on the externality: every unit increase in η toward unity shrinks ℓ, narrows the over-automation
wedge, and reduces the burden placed on the corrective instruments analyzed below. Only at η = 1
does upskilling close the wedge outright (Corollary 2), but that is exactly where the demand loss
ℓ vanishes, so it marks the edge of the externality rather than a remedy within it. Pushing η past
unity would flip the distortion into under-automation, but this is a far less pressing concern: in that
regime, displaced workers are already thriving in higher-paying roles.


                                                    16
4.2   Universal Basic Income

Among the most discussed responses to automation-driven displacement is a universal basic income.
In the model, a UBI funded from general revenue maps to an increase in autonomous demand A:
because the transfer is unconditional, employed and displaced workers receive the same payment,
adding a constant to aggregate spending without altering the marginal income loss from displace-
ment. This distinguishes UBI from displacement-targeted transfers (wage insurance, severance),
which raise the income-replacement rate η and directly shrink ℓ; see Section 4.1. The results below
concern this modeled object and should not be read as a verdict on all UBI designs.
   Because UBI adds a constant to demand, it enters firm profit only through Π0 = A/N +
(λ − 1)wL, the baseline profit when no firm automates. This term drops out of the first-order
condition s − ℓ/N − kαi = 0: a higher A raises the profit floor but changes neither the cost saving s
nor the demand loss ℓ that determine the automation rate. Consequently, UBI alters neither the
automation threshold N ∗ = ℓ/s nor the over-automation wedge ℓ(1 − 1/N )/k. In the language of
game theory, UBI changes payoff levels but not the payoff differences that drive strategic behavior.
More generally, instruments that operate on profit levels can redistribute income but cannot correct
the externality; only instruments that change the per-task automation margin can.
   Despite not correcting the externality, UBI serves a complementary role. A higher Π0 cush-
ions profit losses from over-automation, while the transfer itself raises the floor on workers’ living
standards, buying time for corrective instruments that operate on the right margin.
   Within the model, UBI is a complement to the automation tax, not a substitute: a society that
relies solely on UBI will over-automate at the same rate, with a higher floor on living standards but
the same externality.
   This limitation is one of scope, not of magnitude: because UBI is unconditional, no level of
payment alters the marginal displacement decision. What UBI does support is the level of demand
and of living standards, a role that becomes constructive when the transfer is financed by the au-
tomation tax rather than from general revenue, which displacement itself erodes (Section 4.6). This
complementarity is specific to the regime in which a wedge exists: once automation is collectively
optimal, as when AI comes to dominate human labor, the corrective role disappears and only the
recycling role remains (Section 4.7).




                                                 17
4.3    Capital Income Taxation

If unconditional transfers do not alter the automation incentive, a natural alternative is to tax the
proceeds of automation directly. Consider a proportional tax t ∈ (0, 1) on capital income (profits),
with revenue rebated economy-wide (e.g., as general transfers, public goods, or debt service) so that
its contribution to this sector’s demand does not depend on the firms’ automation choices and is
absorbed into the autonomous component A.3 Firm i now maximizes (1 − t)πi , but because (1 − t)
is a positive scalar it cancels from the first-order condition: the equilibrium automation rate, the
threshold N ∗ , and the over-automation wedge are all unchanged. On the revenue side, A enters
per-firm profit only through the constant Π0 = A/N + (λ − 1)wL, which does not appear in the
first-order condition. If revenue instead funds displacement insurance that raises η, the externality
shrinks through ℓ, but the operative channel is η, not the profit tax itself.
    The distinction matters because capital income taxes are often conflated with robot taxes in the
policy debate. The robot taxes studied in the literature (e.g., Guerreiro et al., 2022) are per-unit
levies on adoption, which operate on the per-task margin; a proportional capital income tax is a
fundamentally different instrument that scales the entire profit function by (1 − t) and cancels from
the optimality condition. The failure is structurally identical to that of UBI (Section 4.2): both
instruments shift profit levels rather than operating on the margin where the externality resides. It
follows that a profit tax paired with an unconditional transfer, two level instruments, cannot correct
the externality either; the corrective leg must be the automation tax, with which such a transfer
instead becomes a complement (Section 4.6).


4.4    Worker Equity Participation

A market-based alternative to taxation, rooted in the profit-sharing literature (Weitzman, 1985),
gives workers a direct stake in the profits that automation generates. Unlike UBI, which enters
demand only through the level term A, profit-sharing flows through the profit function and therefore
interacts with automation decisions. Suppose each firm distributes a fraction ϵ ∈ [0, 1] of its profits
to workers (through ESOPs, equity grants, or co-determination mandates). Workers spend a λ-
fraction of this income in the sector, so profit-sharing recycles capital income back into demand.
                                                                                              P
    Aggregate demand now satisfies a fixed-point condition: D = A + λ[wage income + ϵ i πi ],
       P              P
where i πi = D − i Ci . Because profits depend on D, demand is determined simultaneously
   3
     The polar closed-loop case, in which revenue flows immediately to workers who spend a λ-fraction in the same
sector, is isomorphic to mandated worker equity at profit-sharing rate ϵ = t and is analyzed in Section 4.4: it narrows
the wedge but cannot close it whenever λ < 1.



                                                          18
with the automation decision; the proof solves this fixed point explicitly.

Proposition 3 (Worker equity reduces but cannot eliminate the wedge). Let ϵ ∈ [0, 1] and k > 0,
and suppose the equilibrium is interior. Define Nϵ := N − λϵ(N − 1).
  (i) The cooperative optimum is unchanged: αCO (ϵ) = (s − ℓ)/k, where, as usual αCO is restricted
     to [0, 1].
 (ii) The Nash equilibrium automation rate is αN E (ϵ) = (s − ℓ/Nϵ )/k (restricted to [0, 1]).
(iii) When both αN E and αCO are interior solutions, the over-automation wedge

                                                      ℓ(N − 1)(1 − λϵ)
                                   αN E (ϵ) − αCO =
                                                           k Nϵ

     is strictly decreasing in ϵ but strictly positive for all ϵ < 1/λ. The wedge vanishes only at
     ϵ = 1/λ, which requires ϵ > 1 whenever λ < 1.

   Part (i) is not immediate: profit-sharing changes the demand function by recycling capital
income into worker spending, so one might expect it to shift the planner’s optimum. The result
follows because the planner already controls all N firms and thus fully internalizes the demand
externality. In the planner’s first-order condition, the profit-sharing terms cancel: the modified
demand-loss parameter ℓϵ = ℓ − λϵs and the demand multiplier 1/(1 − λϵ) exactly offset, leaving
kα = s − ℓ regardless of ϵ.
   While the cooperative optimum is unaffected, the Nash equilibrium does shift. Intuitively, when
workers hold equity, part of the demand lost through displacement is recycled back through profit
shares; each firm therefore perceives a larger effective demand loss from its own automation than in
the baseline, and restrains accordingly. The magnitude of this shift is governed by the compound
parameter Nϵ = N − λϵ(N − 1). This parameter measures the effective demand-leakage divisor:
at ϵ = 0 it equals N , recovering the baseline in which each firm perceives demand loss ℓ/N per
automated task. As ϵ rises, Nϵ falls toward 1, pushing αN E toward the cooperative optimum.
   Despite this improvement, the recycling cannot fully close the wedge whenever λ < 1. Closing
the wedge requires the product λϵ to reach one, i.e., ϵ = 1/λ. When λ < 1 this exceeds the feasible
range ϵ ∈ [0, 1]: each unit of profit recycled to workers generates only λ units of sectoral demand,
so compensating for the leakage would require sharing more than the firm’s entire profit. Even at
ϵ = 1 (full profit-sharing), the wedge reduces to ℓ(N − 1)(1 − λ)/[k(N − λ(N − 1))], which remains
strictly positive. (The exception is the knife-edge λ = 1, ϵ = 1: there the demand fixed point (18)
has a vanishing divisor 1 − λϵ, so the wedge closes only in the limit λϵ → 1, and only because λ = 1
removes the spending leakage that drives the externality. For all λ < 1 it stays strictly positive.)

                                                 19
   The structural limitation is that the externality is fundamentally multilateral: each firm’s au-
tomation depresses demand for all N firms, and bilateral arrangements between a firm and its own
workers cannot reach the demand that leaks to rivals.
   A separate question is whether profit-sharing would arise voluntarily.

Corollary 3 (Voluntary profit-sharing does not arise). If each firm independently chooses its own
profit-sharing rate ϵi ∈ [0, 1] to maximize retained profit (1−ϵi )πi , then ϵi = 0 is a dominant strategy.

   The marginal cost of sharing is πi (a dollar-for-dollar reduction in retained earnings), while the
marginal demand benefit is only λπi /N : workers spend fraction λ of the shared profit in the sector,
and firm i captures 1/N of the resulting demand increase. Since λ/N < 1 for any N ≥ 2, the
cost strictly exceeds the benefit. This is a second-order coordination failure layered on top of the
automation externality itself, mirroring the Prisoner’s Dilemma structure of Section 3.2.
   Profit-sharing must therefore be mandated to have any effect, and even then it cannot substitute
for a corrective tax: it narrows the wedge but cannot eliminate it, and unlike a corrective tax
(Section 4.6), does not generate government revenue for retraining programs that would raise η.


4.5    Coasean Bargaining

None of the instruments considered so far fully closes the over-automation wedge, and worker equity
will not arise voluntarily (Corollary 3). A natural question is whether private ordering could succeed
where these instruments have not. By the Coase Theorem (Coase, 1960), if property rights over
the externality were well-defined and transaction costs sufficiently low, bargaining could achieve
the cooperative optimum without government intervention. To evaluate this possibility, it helps to
separate two questions: can bargaining between a firm and its own workers correct the externality,
and can bargaining among firms do so? As we show below, neither can.


Bargaining between a firm and its own workers. If displaced workers can bargain for com-
pensation, say a per-task severance payment σ, the firm’s effective cost saving falls from s to
s − σ, and the equilibrium automation rate drops. But the severance also recycles income into
demand: displaced workers spend a fraction λ of their compensation in the sector, reducing the
effective demand-loss parameter from ℓ to ℓ − λσ. The over-automation wedge therefore becomes
(1 − 1/N )(ℓ − λσ)/k, which is smaller but still positive. This is operationally equivalent to rais-
ing the income-replacement rate η by σ/w; the same logic applies to equity stakes through the
profit-sharing parameter ϵ (analyzed in Section 4.4). As Section 4.1 shows, raising η narrows the


                                                    20
wedge but cannot close it: the externality persists as long as displaced workers’ spending is not fully
replaced, which requires λσ = ℓ, i.e., full income replacement through bargaining alone.
   Moreover, the uninternalized portion of the externality does not fall on firm i’s own workers at
all. When firm i automates, the demand loss ℓ(1 − 1/N )L reduces revenue at rival firms, lowering
their owners’ profits (Equation (4)). Workers at rival firms who retain their positions continue to
earn w per task; they are not directly harmed and have no basis for negotiation with firm i. The
externality is therefore a firm-to-firm channel running through the product market, not a firm-to-
worker channel that bilateral bargaining can reach.


Firm-to-firm bargaining. Since the externality runs across firms, consider a coalition of M ≤ N
firms that jointly choose automation rates to maximize their combined profit, while the remaining
N − M firms play Nash.

Proposition 4 (Partial coalitions cannot eliminate the wedge). Let k > 0 and suppose the equilib-
rium is interior. A coalition of M firms that jointly maximizes its members’ combined profit chooses
the common automation rate
                                                  s − M ℓ/N
                                           αM =             .
                                                      k
The residual over-automation wedge relative to the cooperative optimum is

                                          ℓ(1 − M/N )
                           αM − αCO =                 >0      for all M < N.
                                               k

The wedge vanishes only when M = N : only the grand coalition replicates the cooperative optimum.

   The intuition is that a coalition of M firms internalizes M/N of the aggregate demand loss; the
rest accrues to non-members who enjoy the coalition’s restraint without bearing its cost. This is
the classic free-rider problem of collective restraint, whose sign-flipped twin is the under-provision
of trade credit among rival suppliers, which similarly worsens as the market fragments (Chod et al.,
2019). Four features of the automation externality prevent the grand coalition from forming. First,
voluntary agreements are not self-enforcing: in the frictionless limit (Corollary 1), automation is
strictly dominant, so a coalition member gains from deviating regardless of whether others honor
the agreement. This is not a coordination failure that communication can resolve; the Prisoner’s
Dilemma structure means no non-binding arrangement is stable. With convex costs (k > 0), the
deviation incentive is continuous but still positive. Second, the externality is multilateral and diffuse.
The Coase Theorem’s canonical applications involve bilateral or small-number settings; here, each
of N firms imposes demand losses on all N − 1 others. Each firm’s individual contribution to the

                                                   21
demand loss is ℓL/N , too small to motivate any single negotiation yet too large in aggregate to
ignore. This is precisely the large-numbers setting in which Coase (1960) himself acknowledged that
private bargaining breaks down. Third, the automation rate αi is not contractible among firms: it
is an internal organizational choice that rival firms cannot observe or verify, making binding private
agreements impractical. Fourth, automation decisions involve large sunk costs and are substantially
irreversible, so even in a repeated setting, trigger-strategy punishments cannot undo a deviation; a
firm that delays while rivals proceed loses market share (see Section 5.1 below); and large N makes
defection harder to detect and punishment harder to sustain.
    To summarize, the demand externality studied here is not a market failure that private ordering
can cure. Worker-side bargaining operates on within-firm channels (η, ϵ) that cannot reach the
cross-firm margin where the externality resides; firm-to-firm bargaining targets the right margin but
cannot sustain the grand coalition needed to close the wedge.4 The fundamental obstacle is incentive
compatibility, not transaction costs: even with costless negotiation, the automation game retains
its dominant-strategy structure. The only exceptions, the grand coalition M = N (Proposition 4)
and common ownership, require automation to be observable and contractible across firms, which
the maintained regime rules out. Correcting the externality therefore requires an instrument that
does not rely on voluntary agreement but instead changes each firm’s marginal automation incentive
directly.


4.6    Pigouvian Automation Tax

The classic remedy for a negative externality is a Pigouvian tax : a per-unit charge set equal to the
marginal external cost, so that every agent’s private incentive aligns with the social cost (Pigou,
1920). In contrast to many textbook externalities, where the harmed parties are outside the firms’
market (e.g., pollution), here the harmed parties are workers whose income constitutes the firms’
own demand. This means the tax rate, its revenue, and its incidence all interact through the same
labor-market channel, creating richer policy design questions than the standard case.

Proposition 5 (Pigouvian automation tax). Let τ ≥ 0 be a per-task automation tax, k > 0, and
suppose N > N ∗ and the equilibrium is interior.
  (i) The Nash equilibrium automation rate is αN E (τ ) = (s − τ − ℓ/N )/k. The rate
                                                             
                                                     ∗      1
                                                    τ =ℓ 1−
                                                            N
   4
     An alternative to bargaining is common ownership: a merger of M firms implements the coalition of Proposition 4,
internalizing M/N of the externality.


                                                         22
      implements αN E = αCO = (s − ℓ)/k.
 (ii) Under the tax at rate τ ∗ without rebate, each firm earns π tax = π CO − τ ∗ LαCO . With an
      exogenous lump-sum rebate (each firm’s receipt is independent of its own automation), each
      firm achieves exactly π CO .

   The optimal rate has a transparent economic interpretation: each firm already bears ℓ/N of the
demand loss from its own automation; the tax charges it for the remaining ℓ(1 − 1/N ) imposed on
rivals. For large N , τ ∗ ≈ ℓ = λ(1 − η)w, so setting the rate requires only sector-level observables.
Levying the tax, however, requires observing firm-level automation rates, a practical challenge,
though one that may be easing as AI adoption generates observable procurement records (Guerreiro
et al., 2022). Unlike rival firms in a Coasean bargaining setting (Section 4.5), a tax authority can
compel disclosure through mandatory reporting, payroll records, and procurement audits, making
approximate measurement feasible even when private verification is not. Because the welfare loss is
quadratic in the wedge (Proposition 2), even an imprecisely targeted tax yields a first-order gain.


Allocation of tax revenue. Proposition 5 pins down the rate; the remaining design question is
what to do with the revenue. Because the externality flows through the labor market, this choice
can affect structural parameters governing the distortion, not merely the distribution of gains.
   A lump-sum rebate to firms restores cooperative profits exactly (part (ii)), but returns revenue
to the firms that automate while leaving displaced workers, the harmed parties, uncompensated.
The more natural option is to direct revenue toward those workers. Two channels are available,
with different incentive properties.
   Direct transfers (wage insurance, severance supplements) raise η mechanically by replacing lost
income. The firm’s automation incentive is unaffected: it pays τ per automated task regardless of
where the revenue goes, and any resulting rise in η operates at the sector level, not through firm i’s
own automation, so its first-order condition is unchanged. But the standard moral-hazard con-
cern applies: generous income replacement may weaken workers’ incentive to retrain or reallocate,
sustaining η through transfers rather than through productive reabsorption.
   Funding retraining programs also raises η, but through human-capital investment rather than
income replacement. This channel is slower and harder to implement, yet it builds the capacity
for workers to re-enter the labor market at comparable or higher wages, making gains in η self-
sustaining. In principle, the resulting dynamic is self-reinforcing, complementing the analysis in
Section 4.1: the tax funds programs that raise η, which lowers ℓ, which reduces τ ∗ in future periods.
To the extent that reabsorption is successful, the required correction shrinks over time and the tax


                                                 23
is transitional rather than permanent, echoing the finding in Guerreiro et al. (2022) that the optimal
robot tax declines to zero as displaced cohorts retire and new workers choose occupations with full
knowledge of automation.
   A further use of revenue acts on the demand level rather than on the externality. Funding an
unconditional transfer does not raise η or enter any firm’s first-order condition; it returns revenue
to autonomous demand A. The contrast with Section 4.3 is this: a profit tax paired with such
a transfer stacks two level instruments and leaves the wedge intact, whereas the automation tax
paired with it corrects the margin and recycles the revenue into demand, the working form of the
complement anticipated in Section 4.2. In a post-labor economy, where the corrective term vanishes,
this recycling becomes the entire policy (Section 4.7).
   In practice, a mix of transfers and retraining is likely optimal: short-run transfers to cushion
displacement while longer-run retraining builds durable gains in η. The Pigouvian tax therefore has
the potential to do double duty: it corrects the externality at the margin, and its revenue can be
recycled to shrink the distortion over time.


4.7   The Post-Labor Limit

What does the model say when AI replaces most human labor? The problem does not vanish; it
changes. During the transition, firms automate too much and both workers and owners lose. In the
post-labor limit the cost saving is so large that automating every task maximizes profit, since the
demand lost per task is limited while the cost saving is not. Demand does not fall to zero but settles
at a floor set by autonomous spending and replaced income, and the over-automation wedge closes
(Proposition 1). What remains wrong is not too much automation but that the eliminated wages do
not return. Even a planner who values workers (µ > 0) now optimally automates fully: αSP (µ) in
Proposition 2 binds at 1 for any fixed µ < 1. The remaining failure is distributional, not allocative,
so an automation tax has no margin left to correct. A profit tax, useless for correction during the
transition because it cancels from each firm’s automation decision (Section 4.3), now has no margin
left to distort, which makes it the natural instrument for the one task that remains. A universal
basic income funded by such a tax returns part of the owners’ surplus to households as spending,
rebuilding the demand floor by raising autonomous demand A (Section 4.2). Workers gain directly,
and because firm profits depend on that demand, firms gain too. This is the role UBI could not
play in the transition but can play here (Section 4.2). The transfer must be mandated, since firms
will not provide it on their own (Corollary 3), and because households spend only a fraction λ
in the sector, the recycling is partial. The post-labor case is thus the limit of our result, not an


                                                 24
exception. The failure is now distributional rather than allocative, and the corrective instrument is
a profit-funded UBI rather than an automation tax.


5     Extensions

The baseline isolates the demand externality in the simplest environment that supports it. A natural
concern is that the result depends on what has been held fixed: endogenous wage adjustment might
close the wedge, free entry might discipline the market to an efficient scale, higher AI productivity
might resolve the demand problem by expanding the pie, and capital-income recycling might offset
the spending lost through displacement. This section takes up each of these objections, along with
richer product-market interaction, and shows that the externality is robust to all of them and, in
some cases, amplified. Table 2 previews the results.

       Table 2: Extensions of the baseline model and effects on the over-automation result.
                                     Section   Modifies N ∗ ?      Wedge effect        Eliminates externality?
 AI productivity (ϕ > 1)               5.1     Yes (lowers)            Widens                   No
 Endogenous entry                      5.2         No           Persists (can widen)            No
 Endogenous wages                      5.3     Yes (raises)           Narrows                   No
 Capital-income recycling (η̂ > 0)     5.4     Yes (raises)           Narrows                 Partially
 Imperfect competition                 5.5         n/a                 Persists                 No
   Note. Each row records how the generalization affects the automation threshold N ∗ (for AI productivity, the
formula N ∗ = ℓ/s is unchanged, but the market-share term lowers the firm count at which automation begins), the
    over-automation wedge, and whether it eliminates the demand externality. The externality survives all five
                             generalizations under empirically plausible parameters.




5.1    AI Productivity

In the baseline, AI and human workers produce the same output per task and so the automation
incentive is purely cost-driven. In practice, AI can replace humans while also raising output per
task (e.g., autonomous agentic coding agents, higher-throughput customer service bots). To capture
this, we add a productivity advantage on top of the cost saving. A natural conjecture is that this
output channel mitigates the demand problem by making the economy more productive. We show
the opposite is true: higher AI output per task widens the over-automation wedge.
    Let an AI-performed task produce ϕ ≥ 1 units of output, while a human-performed task pro-
duces 1 unit. With ϕ > 1, firm i’s output becomes


                             Yi (αi ) = [ϕαi + (1 − αi )]L = [1 + (ϕ − 1)αi ]L.



                                                      25
                                                                                              P
Under perfect competition, revenue is allocated by output share: Revi = D · Yi /                j Yj .   At a
symmetric profile all firms produce the same output Ȳ = [1 + (ϕ − 1)α]L, so Revi = D/N as in the
baseline. Differentiating with respect to αi and evaluating at the symmetric profile yields

                             ∂ Revi               ℓL            D(ϕ − 1)(N − 1)
                                      =        −            +                      .                     (10)
                              ∂αi sym             N}
                                               | {z             N 2 [1 + (ϕ − 1)α]
                                                                |       {z       }
                                             demand loss         market-share gain


The first term is the baseline demand externality, which depends only on ℓ and N and is therefore
independent of ϕ. The second is new: a deviating firm raises its output above rivals and captures a
larger share of expenditure. This market-share gain is positive whenever ϕ > 1, raising the private
incentive to automate above the baseline.
   To quantify the effect, we combine cost saving, demand loss, and market-share gain into the
first-order condition. The symmetric equilibrium equates marginal integration cost to the combined
benefit:
                                             ℓ   D(α) (ϕ − 1)(N − 1)
                                  kα = s −     +                      .
                                             N   N 2 [1 + (ϕ − 1)α] L
Because D(α) is linear in α, clearing the denominator yields a quadratic whose positive root is the
unique equilibrium; however, the resulting expression is less transparent than the baseline formula,
so the comparative statics below are established via a monotone crossing argument.

Proposition 6 (AI productivity widens the over-automation wedge). Let k > 0 and suppose the
equilibrium is interior.
  (i) The Nash equilibrium automation rate is increasing in AI productivity: αN E (ϕ) > αN E (1) for
      ϕ > 1.
 (ii) The cooperative optimum and the generalized planner’s optimum, however, are unchanged:
      αCO (ϕ) = αCO (1) and αSP (µ; ϕ) = αSP (µ; 1) for all µ ∈ [0, 1].
(iii) Consequently, the over-automation wedge αN E (ϕ) − αSP (µ; ϕ) is strictly increasing in ϕ for
      every µ ∈ [0, 1].

   The mechanism is a Red Queen effect: each firm perceives a market-share gain from automating
beyond rivals, but at the symmetric equilibrium all firms expand equally, so the gains cancel. By
contrast, the cost saving s enters each firm’s profit identically regardless of rivals’ choices, so it shifts
αN E and αCO equally and leaves the wedge unchanged.
   Part (ii) holds because total sectoral revenue equals total expenditure D under market clearing,
and D (2) depends on worker income, not output: higher ϕ raises output but lowers the price
in proportion, leaving the planner’s objective invariant to ϕ. Together with part (i), this yields

                                                       26
part (iii): better AI raises the equilibrium automation rate without shifting the efficient benchmark,
so the distortion grows with AI capability.
   The wider wedge also carries a policy implication. Because the market-share motive adds a
second distortion on top of the demand externality, the baseline Pigouvian rate τ ∗ = ℓ(1 − 1/N ) no
longer suffices: implementing αCO requires an additional correction equal to the market-share term
in (10), divided by L, evaluated at the cooperative rate, which is strictly positive whenever ϕ > 1.
That said, the lower price means each dollar of spending buys more physical output, so the welfare
measure S(µ), built from nominal flows, understates the real consumption gains from higher ϕ. The
proposition identifies a strategic distortion, not a claim that higher AI productivity reduces total
welfare on net.


5.2     Endogenous Entry

So far the number of firms has been exogenous. With free entry, one might expect the over-
automation problem to be self-correcting: surplus erosion lowers profits, marginal firms exit, and
the remaining industry settles at an efficient scale. Whether this logic goes through, however,
depends on how the entry margin interacts with the automation decision.
   Consider a two-stage game: firms pay a fixed cost κ ≥ 0 to enter, then simultaneously choose
automation rates. Given N entrants, the stage-2 Nash equilibrium yields per-firm operating profit
Π∗ (N ). A pure-strategy free-entry equilibrium is an integer N ≥ 1 such that


                               Π∗ (N ) ≥ κ     and      Π∗ (N + 1) ≤ κ :                            (11)


incumbents weakly prefer to remain active, while an additional entrant would not recover the fixed
cost.
   Because the frictionless (k = 0) and convex-cost (k > 0) regimes shape the profit schedule in
qualitatively different ways, we treat each in turn. The frictionless case sets λ = 1 for clean closed
forms; the qualitative results hold for any λ ∈ (0, 1], as the assumption affects only profit levels, not
the structure of the entry regimes.
   In the frictionless benchmark (k = 0), automation is all-or-nothing. When ℓ > s, the profit
schedule drops discretely at N ∗ : below the threshold no firm automates, while above it full au-
tomation is dominant (Corollary 1) and per-firm profit falls by ∆ := L(ℓ − s) > 0 (Figure 4 in the
appendix illustrates). Write m := ⌊N ∗ ⌋ for the largest integer not exceeding N ∗ . We assume, as
a genericity condition, that the threshold is not itself an integer: N ∗ ∈
                                                                         / N. Because the number of


                                                   27
firms is a whole number, this places every market size strictly below the threshold (no firm auto-
mates) or strictly above it (all do), with no ambiguous case sitting exactly on the boundary. The
condition is innocuous, failing only on the measure-zero set of parameters for which ℓ/s is exactly
a whole number.5

Proposition 7 (Endogenous entry in the frictionless benchmark). Suppose k = 0, λ = 1, ℓ > s,
0 < κ < A, and, generically, N ∗ ∈
                                 / N. The per-firm equilibrium profit schedule
                                                
                                                A/N
                                                                if N ≤ N ∗ ,
                                       ∗
                                     Π (N ) =
                                                A/N − ∆         if N > N ∗ ,
                                                


is strictly decreasing on N. The unique pure-strategy free-entry equilibrium has N F E = max{N ∈
N : Π∗ (N ) ≥ κ} firms. Three regimes arise depending on the entry cost:

  (i) Low entry cost (κ ≤ A/(m + 1) − ∆): N F E = ⌊A/(κ + ∆)⌋ ≥ m + 1. Every firm fully
         automates.

 (ii) Intermediate entry cost (A/(m+1)−∆ < κ < A/m): N F E = m. No firm automates, yet each
         earns strictly positive profit A/m > κ. The threat of automation deters further entry: one
         additional firm would trigger full automation, dropping per-firm profit to A/(m + 1) − ∆ < κ.

(iii) High entry cost (κ ≥ A/m): N F E = ⌊A/κ⌋ ≤ m. No firm automates. Entry costs, not the
         automation externality, limit the number of firms.

       When case (i) arises, the Prisoner’s Dilemma of Corollary 1 materializes under free entry: all
firms automate, demand contracts, and every firm would be better off had none automated. Case (iii)
is the standard free-entry outcome: entry costs are high enough that the market never approaches
the automation threshold, and the externality is irrelevant. Case (ii) is the most distinctive: the
threat of automation functions as an endogenous entry barrier, sustaining positive profits without
any automation actually occurring, at the cost of sustaining market power.
       The convex-cost case is less stark but more robust. With k > 0, the automation rate αN E (N ) =
(s − ℓ/N )/k varies continuously in N , so the profit schedule no longer jumps at N ∗ and the entry-
deterrence mechanism of Proposition 7(ii) does not arise.
   5
    Exactly at an integer threshold, s = ℓ/N , so each firm’s private gain from automating is zero and every firm is
indifferent over its own rate; yet a rival’s automation still lowers the firm’s payoff by contracting demand D. The
stage-2 equilibrium profit is then not single-valued, and pinning it down would require an arbitrary selection rule,
which the assumption avoids.



                                                        28
Proposition 8 (Endogenous entry with convex costs). Suppose k > 0, ℓ > s, κ > 0, and Π0 (1) > κ
(the market is viable). A free-entry equilibrium N F E satisfying (11) exists. If N F E > N ∗ , then
αN E (N F E ) > αCO : over-automation persists under free entry.

       Generically, N F E exceeds N ∗ whenever zero-automation profits at the threshold, Π0 (N ∗ ), ex-
ceed κ.6 Free entry then pins down the number of firms but does not alter the strategic incen-
tives within the automation subgame: each firm still bears only a fraction 1/N F E of the demand
loss.    Over-automation persists because ℓ > s forces αCO = 0, so the realized wedge equals
αN E (N F E ) = min((s − ℓ/N F E )/k, 1) > 0 (the interior expression ℓ(1 − 1/N F E )/k applies only
where the cooperative rate is itself interior). If N F E ≤ N ∗ , no firm automates and the outcome is
efficient, but only because the market is too concentrated for the private automation incentive to
activate.
       Taken together, the two propositions deliver a common lesson: free entry reshapes the over-
automation problem but does not resolve it. If anything, the standard tendency toward excess
entry (Mankiw and Whinston, 1986) widens the wedge by fragmenting the market further.
       The entry margin reveals an unintended side effect of UBI (Section 4.2). By raising autonomous
demand A, UBI increases per-firm profit Π0 = A/N + (λ − 1)wL at any given N , attracting
additional entrants until the zero-profit condition (11) binds at a larger N F E . Since the realized
over-automation rate αN E = min((s − ℓ/N )/k, 1) is increasing in N under the maintained ℓ > s
(where αCO = 0), a policy designed to cushion displacement can paradoxically widen the very
externality that causes it.


5.3      Endogenous Wages

A central insight of Acemoglu and Restrepo (2018) is that endogenous wage adjustment can stabilize
the automation path: as firms automate, displaced workers increase labor supply, pushing wages
down; lower wages narrow the cost saving from automation and discourage further displacement.
This self-correcting feedback is a natural candidate for resolving the demand externality identified
above. We show that it raises the threshold at which the externality activates and, short of driving
wages all the way to AI’s cost c, cannot close the wedge once it does; the only wage path that
eliminates the wedge does so by collapsing worker income, so wage flexibility resolves the inefficiency
only at a distributional cost a planner who values workers (µ > 0) would reject.
   6
     In a numerical grid over c/w ∈ {0.1, . . . , 0.5}, λ ∈ {0.3, . . . , 1}, η ∈ {0, . . . , 0.3}, k ∈ {0.5, 1, 2}, and κ ∈
{0.1, . . . , 5}, N F E exceeds N ∗ in over 94% of parameterizations satisfying the proposition’s conditions; the exceptions
arise only when the entry cost is high enough that the market barely supports more than N ∗ firms.



                                                            29
       In Acemoglu and Restrepo (2018), wages are determined by labor-market clearing in a full general
equilibrium; we adopt a reduced-form representation that captures the key qualitative feature of
their mechanism. Let the wage depend on the aggregate automation rate: w(ᾱ) with w(ᾱ) > c and
w′ (ᾱ) ≤ 0; firms take the prevailing wage as given when choosing αi . This specification requires only
that wages fall when aggregate labor-market slack increases, a property shared by efficiency-wage
models, where the no-shirking wage declines with unemployment (Shapiro and Stiglitz, 1984). In
our setting, automation displaces workers into the labor pool, generating exactly this type of slack.
       Both the cost saving s(w) = w − c and the demand-loss parameter ℓ(w) = λ(1 − η)w are
increasing in the wage, so falling wages affect both sides of the automation margin: they shrink
the private incentive to automate (the self-correcting channel) and reduce the demand loss per
automated task. The equilibrium automation rate is therefore a fixed point in which automation,
wages, and the externality are jointly determined. Despite this richer feedback, the threshold
N ∗ = ℓ/s = λ(1 − η)w/(w − c) rises as wages fall, because the cost saving s = w − c contracts faster
than the demand loss ℓ = λ(1 − η)w. The structural source of the distortion, however, is unaffected.

Proposition 9 (Robustness to wage adjustment). Let k > 0, let w : [0, 1] → (c, ∞) be differentiable
with w′ (ᾱ) ≤ 0, and suppose firms are wage-takers in both the Nash and the cooperative comparison.7
  (i) At any symmetric equilibrium with N > N ∗ (w(ᾱ)), the Nash automation rate exceeds the
         cooperative optimum: αN E > αCO , unless the cost saving is so large that both rates pin at full
         automation (s(ᾱ) ≥ k + ℓ(ᾱ)), where the strict inequality lapses.
 (ii) Endogenous wage adjustment raises the threshold: N ∗ (w(ᾱ)) ≥ N ∗ (w(0)) for all ᾱ ∈ [0, 1],
         with strict inequality whenever w(ᾱ) < w(0), c > 0, and η < 1 (at c = 0 the threshold
         N ∗ = λ(1 − η), and at η = 1 the threshold N ∗ = 0, are independent of the wage, so wage
         decline does not move them).

       Competitive pricing allocates revenue as Revi = D/N at any wage level, so each firm bears
only a fraction of the demand destruction its automation causes regardless of whether w is high or
low. Wage adjustment changes the magnitude of ℓ but not the fraction each firm internalizes; that
fraction is a property of market structure, not of factor prices.
       The strongest version of the self-correcting argument is that wages could fall far enough to shut
   7
    The cooperative benchmark αCO is the common automation rate that maximizes aggregate firm profit when
firms remain price-takers in the labor market, so the wage is taken parametrically and only evaluated at w(ᾱ) at
the symmetric equilibrium. This isolates the cross-firm demand externality from a separate monopsonistic-incidence
channel that would arise if a coalition exploited the wage schedule w(ᾱ) directly. Such coordination is, in any case, not
a feasible benchmark for legal firm conduct: joint suppression of wages by competing employers is a per se antitrust
violation in the United States and analogous jurisdictions. The relevant cooperative outcome is therefore one firms
could lawfully implement, e.g., a coordinated cap on automation, with the wage left to the labor market.


                                                           30
the externality down entirely. As w → c, the cost saving s → 0 while N ∗ → ∞: eventually N ∗
exceeds N and no firm finds automation privately worthwhile. At the pure-efficiency benchmark
µ = 0 this is a genuine resolution: full wage flexibility extinguishes the cost saving that drives the
race, so the over-automation wedge disappears. But the resolution is Pyrrhic. When wages are
driven to near the AI cost, workers who retain their jobs earn little more than the machines that
would replace them, and aggregate purchasing power collapses through wage depression rather than
displacement. The externality vanishes only because so little income is left per worker that the
wedge between private and social incentives becomes negligible. The demand problem has not been
solved; it has merely been hidden behind near-subsistence wages: a labor market that “self-corrects”
only by impoverishing its workforce has transmuted displacement into depressed living standards.
The cure fails as a corrective device for two reasons, not because the externality is indestructible: it
works only if wages can fall all the way to c, which subsistence and minimum-wage floors rule out,
and even where wages are fully flexible a planner who places positive weight on workers (µ > 0)
counts the wage depression that does the correcting as a welfare loss, not a fix. More generally,
wage flexibility changes when the externality bites; whether full flexibility can also dissolve it turns
on the maintained wage floor and on the weight placed on workers, not on the externality alone.
   The analysis above sets µ = 0, so the planner cares only about firm profits. A planner who also
values worker welfare (µ > 0) would find wage depression no more acceptable than displacement,
demanding a larger correction, yet wage adjustment provides the same compression of ℓ. Endogenous
wages therefore close a smaller share of the gap, making them even less adequate as a corrective
mechanism. Corollary 4 in the appendix confirms this: whenever the µ-planner’s marginal benefit gµ
is strictly decreasing (which holds for all µ up to a threshold µ̄, and beyond it when integration
frictions dominate wage sensitivity), the over-automation result extends to any µ ∈ [0, 1) under
endogenous wages.


5.4   Capital Income Recycling

Section 4.1 showed that raising η, the fraction of displaced income recovered by workers, shrinks
the demand-loss parameter ℓ and narrows the over-automation wedge. A natural counterpart on
the capital side is that owners spend their profits: if their consumption offsets the spending lost
through displacement, the demand externality might disappear. We show that recycling narrows
the wedge but cannot close it under empirically plausible parameters.
   Suppose capital owners consume a fraction η̂ ∈ [0, 1) of their capital income in the sector. Total
sector profit is Π = D − N L(w − sᾱ). Adding capital consumption η̂Π to aggregate demand and


                                                  31
solving for D yields
                                         A + (λ − η̂)wLN   ℓη̂ LN
                                  D=                     −        ᾱ,                               (12)
                                              1 − η̂       1 − η̂
where
                                               ℓη̂ = ℓ − η̂s

is the effective demand-loss parameter: each automated task loses ℓ in worker spending, but owners
recycle η̂ of the per-task saving s back into demand. When η̂ = 0, ℓη̂ = ℓ and eq. (12) reduces to
eq. (2). This is the frictionless (k = 0) specialization; for k > 0 the fixed point carries an additional
minus (η̂k/[2(1 − η̂)])L j αj2 term (derived in the proof of Proposition 10).
                          P

    Competitive pricing still gives Revi = D/N . The first-order condition becomes L(s − ℓη̂ /[N (1 −
η̂)]), giving a modified threshold
                                                        ℓη̂
                                            Nη̂ :=             .
                                                     s(1 − η̂)
Proposition 10 (Capital income recycling). Suppose k = 0. When there is capital income recycling
at rate η̂,
  (i) When ℓη̂ > 0, full automation is dominant if and only if N > Nη̂ .
 (ii) The externality vanishes (ℓη̂ ≤ 0) only when η̂ ≥ ℓ/s.

    Part (ii) requires η̂ ≥ ℓ/s = λ(1 − η)w/(w − c): owners must recycle enough of each task’s
cost saving to replace the demand that displaced workers would have generated. When ℓ > s, the
required rate exceeds one, so recycling is impotent precisely where the externality is most harmful,
since ℓ > s implies αCO = 0 and firms automate when the planner would prefer none. When
ℓ < s, elimination is feasible in principle, but the planner already prefers positive automation
(Proposition 1) and the wedge is quantitatively smaller.
    The frictionless case gives the sharpest result, but the structure carries over when frictions are
positive. The proof of Proposition 10 extends the result to k > 0. The Nash equilibrium generalizes
to αN E = (s − ℓ/N̂ )/k, where N̂ = N (1 − η̂) + η̂ is an effective market size that interpolates
between N (no recycling) and 1 (full recycling), making each firm behave as though it faced fewer
competitors. The cooperative optimum, however, is unchanged: the 1/(1 − η̂) multiplier scales total
profit without shifting the optimizer.
    The upshot parallels Section 4.1: recycling raises the fraction of demand loss each firm inter-
nalizes from 1/N to 1/N̂ , but cannot push it to one. Addressing how income is spent narrows the
wedge but does not close it, because the underlying dilution across firms persists.




                                                     32
5.5      Imperfect Product-Market Competition and Task Complementarity

The baseline assumes competitive pricing and perfect substitution across tasks. Relaxing either
changes the magnitude of over-automation but not its existence, because neither alters the one
fact the externality rests on: automation reduces the level of aggregate expenditure by displacing
workers, and each firm bears only a fraction of that loss. We give the argument informally; a formal
treatment is left for future work.


Second-stage price or quantity competition. Suppose firms compete on quantities or prices
after choosing automation. This changes how a given level of expenditure is divided among firms
and rewards a firm that automates more than its rivals with a larger market share. Neither force
removes the externality. However expenditure is split, each firm still bears only a fraction of the
demand its own automation destroys, so over-automation persists whenever a firm lacks full market
power; with differentiated products the uninternalized loss scales with the share of the market the
firm does not capture. The market-share motive cancels across firms at the symmetric equilibrium,
echoing the Red Queen effect of Section 5.1, and under Cournot is partly self-correcting, since a
firm that gains share also absorbs more of the demand loss it causes. As long as firms lack full
market power, market structure moves the size of the wedge without changing its sign; only in the
monopoly limit, where a single firm internalizes the entire demand loss it causes, does the wedge
close.


CES task aggregation. The baseline takes the perfect-substitutes limit of the CES task aggre-
gator in Acemoglu and Restrepo (2018). Under imperfect substitution, automating the marginal
task yields diminishing output gains, which restrains automation from the supply side and shrinks
the wedge; when tasks are complements the restraint is stronger still. Either way the demand side
is unchanged, so the externality remains positive as long as displaced workers lose income.

    In every case the source of the distortion is the same and survives: firms do not internalize
the demand they destroy. Richer modeling moves the magnitude, not the mechanism, which the
baseline isolates in its starkest form.


6     Discussion

This paper develops a simple model with a stark insight. Even as AI-driven layoffs sweep across
industries, and even as every firm recognizes that vanishing paychecks mean vanishing customers,


                                                33
not one of them will stop. Each firm reaps the full savings of replacing its own workers yet bears
only a sliver of the demand it destroys; the rest lands on rivals. No firm can afford to be the one
that holds back. This is the trap: an automation arms race that only intensifies as AI improves,
that leaves workers and firm owners alike worse off, and that no market force can break. We close by
discussing implications for empirics and policy, and then the scope and limitations of the analysis.


Empirical implications. Anthropic CEO Dario Amodei has warned that AI-driven displacement
will be “unusually painful,” “much broader” and “much faster” than previous technological shocks
(Bhaimiya, 2026). If that assessment proves correct and income replacement remains incomplete,
the model points, perhaps counterintuitively, to where the problem is most severe: not dominant
technology firms but fragmented industries deploying the most capable AI (Propositions 1 and 6).
The distinguishing empirical signature would be profit erosion. Standard competitive models predict
that cost-reducing technology raises profits; profit erosion that coincides with mass layoffs would
be difficult to rationalize without the externality (Proposition 2). That said, this signature requires
displacement at a scale and speed beyond what has materialized so far. If reabsorption keeps pace
with automation, the externality may remain too small to detect, and the paper’s contribution
is identifying a structural vulnerability rather than diagnosing an active crisis. Three settings
where AI-driven displacement is already under way offer concrete starting points: customer support,
where thousands of firms are simultaneously replacing agents with agentic AI (Budman, 2025);
software services, where tools that enable one engineer to replace a multi-person team (Son, 2025)
create measurable shifts in headcount-to-output ratios; and back-office operations across competing
financial institutions, where regulatory reporting makes both adoption rates and revenue outcomes
unusually transparent.


Policy implications. Much of the policy debate around AI-driven displacement focuses on how
to respond after the fact, through retraining, income support, or regulation. Our results reframe the
question: do competitive incentives drive firms to automate beyond what is collectively optimal?
Even a planner who places zero weight on worker welfare would reduce the automation rate below the
equilibrium level (Proposition 2). Because over-automation leaves both firms and workers worse off,
correcting it is a matter of eliminating waste, not of redistributing gains between them. Universal
basic income, perhaps the most widely discussed response, raises living standards but does not
change a single firm’s incentive to automate (Section 4.2). Collective bargaining faces the same
wall: because automation is a dominant strategy, no voluntary agreement among firms to restrain



                                                  34
layoffs is self-enforcing (Section 4.5). By Tinbergen’s principle, a distinct market failure requires a
distinct instrument; only a Pigouvian automation tax supplies it (Table 1). This ordering reverses
only in the post-labor limit, where the arms race has nothing left to correct and a profit-funded
basic income becomes the operative policy rather than a palliative (Section 4.7).
   One practical consideration bears on implementation: the model is a closed-sector game, and
a unilateral automation tax could push adoption offshore, strengthening the case for multilateral
coordination or border-adjustment mechanisms analogous to those used in carbon policy.


Scope, limitations, and future directions. The model is deliberately simple: one sector, one
period, symmetric firms. Each of these choices is conservative, meaning the real problem is likely
worse than what we show.
   A single sector understates the externality. In a multi-sector economy, layoffs in one sector reduce
spending on every sector’s output, creating reinforcing demand spirals. Platform ecosystems make
the point concrete: when a platform automates seller support, gig logistics, or content moderation,
the lost spending cascades across an entire ecosystem of complementors.
   A related concern is whether the demand channel survives general equilibrium: in a frictionless
multi-sector economy, displaced wage income would rotate to other consumption and the mechanism
would seem to dissolve. Two structural facts block the rotation. Mass-market goods saturate at
high incomes, so the marginal capital-income dollar leaves the modeled sector; and mass-sector
firms cannot quickly retool to capture redirected luxury spending. The firms least able to escape
the PD are therefore precisely those most exposed to the rotation failure: mass-market producers,
where the policy debate is loudest. A deeper version of the objection concerns not where the lost
spending goes but the interest rate. Displaced workers do not save more; they take an income hit
and, if anything, dissave or borrow. The extra desired saving comes instead from the redistribution
toward owners, who consume a smaller share of their income. In a frictionless economy the interest
rate falls until that extra desired saving is spent elsewhere. The demand loss is then transferred
through the interest rate rather than destroyed, and standard efficiency reasoning sees no role for a
corrective tax. This is correct in a frictionless economy. But it also pinpoints when the externality
is instead real: the case where the interest rate cannot fall far enough. That happens when rates
are already near zero (Farhi and Werning, 2016; Caballero and Farhi, 2018), or when displaced
workers cannot borrow against future income because financial markets are incomplete (Greenwald
and Stiglitz, 1986). Both conditions are squarely relevant to mass AI displacement. Only when the
rate is so constrained is the lost spending genuinely destroyed, so the corrective tax of Proposition 5


                                                  35
is warranted precisely under these frictions, not in the frictionless benchmark. Section A works
through these channels, including this interest-rate channel, and argues each is blocked or non-
binding for mass-market firms; a fuller GE treatment is in development.
   The static setting misses two dynamic forces that pull in opposite directions. AI investments
are largely irreversible, and Proposition 7 shows that even the threat of automation can reshape
market structure before any displacement occurs, strengthening the case for early policy action.
Working the other way, the income-replacement rate η rises over time as displaced workers retrain
and new occupations emerge (Acemoglu and Restrepo, 2019), so the optimal tax should shrink as
the economy adjusts (Section 4.6).
   Symmetry rules out heterogeneity across firms and workers, and endogenizing AI development
could compound the problem: firms racing to automate may invest disproportionately in labor-
replacing AI rather than labor-augmenting AI (Acemoglu and Restrepo, 2018), feeding the very
arms race the model identifies.
   These extensions point on net toward a larger problem, not a smaller one; the one self-correcting
force is gradual reabsorption (a rising income-replacement rate η), which shrinks the corrective tax
over time without removing the externality. A further connection worth exploring is the interaction
with algorithmic pricing: when AI systems that automate tasks also set prices, collusive markups
may partially internalize the demand externality but simultaneously strengthen the private incen-
tive to automate (Banchio and Mantegazza, 2022; Keppo et al., 2026). Pursuing these and other
extensions, along with the empirical tests outlined above, are promising directions for future work.


References
Daron Acemoglu. The simple macroeconomics of AI. Economic Policy, 40(121):13–58, 2025.

Daron Acemoglu and Pascual Restrepo. The race between man and machine: Implications of technology for
  growth, factor shares, and employment. American Economic Review, 108(6):1488–1542, 2018.

Daron Acemoglu and Pascual Restrepo. Automation and new tasks: How technology displaces and reinstates
  labor. Journal of Economic Perspectives, 33(2):3–30, 2019.

Daron Acemoglu and Pascual Restrepo. The wrong kind of AI? Artificial intelligence and the future of labour
  demand. Cambridge Journal of Regions, Economy and Society, 13(1):25–35, 2020.

Daron Acemoglu and Pascual Restrepo. Automation and rent dissipation: Implications for wages, inequality,
  and productivity. Quarterly Journal of Economics, 141(2):1521–1579, 2026.




                                                    36
David H. Autor, Frank Levy, and Richard J. Murnane. The skill content of recent technological change: An
  empirical exploration. Quarterly Journal of Economics, 118(4):1279–1333, 2003.

David H. Autor, Caroline Chin, Anna Salomons, and Bryan Seegmiller. New frontiers: The origins and
  content of new work, 1940–2018. Quarterly Journal of Economics, 139(3):1399–1465, 2024.

Martino Banchio and Giacomo Mantegazza. Artificial intelligence and spontaneous collusion. Working paper,
  Bocconi University and USC Marshall School of Business, 2022.

Hamsa Bastani and Gérard P. Cachon. The human-AI contracting paradox. Working paper, The Wharton
  School, University of Pennsylvania, December 2025. SSRN 5962739.

Seth G. Benzell, Laurence J. Kotlikoff, Guillermo LaGarda, and Jeffrey D. Sachs. Robots are Us: Some
  economics of human replacement. Working Paper 20941, National Bureau of Economic Research, February
  2015.

Martin Beraja and Nathan Zorzi. Inefficient automation. Review of Economic Studies, 92(1):69–96, 2025.

Sawdah Bhaimiya. AI job cuts: Amazon, Microsoft, and more cite AI for 2025 layoffs. CNBC, 2025.

Sawdah Bhaimiya. Anthropic CEO Dario Amodei warns AI may cause ‘unusually painful’ disruption to jobs.
  CNBC, 2026.

Tommaso Bondi and Gentry Johnson. Skill atrophy and AI productivity measurement. Technical report,
  Cornell Tech, April 2026. SSRN 6169671.

Timo Boppart. Structural change and the Kaldor facts in a growth model with relative price effects and
  non-Gorman preferences. Econometrica, 82(6):2167–2196, 2014.

Erik Brynjolfsson, Bharat Chandar, and Ruyu Chen. Canaries in the coal mine? Six facts about the recent
  employment effects of artificial intelligence. Working paper, Stanford Digital Economy Lab, November
  2025a.

Erik Brynjolfsson, Danielle Li, and Lindsey Raymond. Generative AI at work. Quarterly Journal of Eco-
  nomics, 140(2):889–942, 2025b.

Scott Budman. Salesforce CEO confirms 4,000 layoffs “because I need less heads” with AI. CNBC, 2025.

Bureau of Economic Analysis. Gross domestic product, first quarter 2026 (advance estimate). https:
  //www.bea.gov/news/2026/gdp-advance-estimate-1st-quarter-2026, April 2026a. Accessed May 5,
  2026.

Bureau of Economic Analysis. Personal income and outlays, march 2026. https://www.bea.gov/news/
  2026/personal-income-and-outlays-march-2026, April 2026b. Accessed May 5, 2026.


                                                   37
Ricardo J. Caballero. Speculative-growth and the AI “Bubble”. Technical report, Massachusetts Institute of
  Technology, May 2026.

Ricardo J. Caballero and Emmanuel Farhi. The safety trap. The Review of Economic Studies, 85(1):223–274,
  2018. doi: 10.1093/restud/rdx013.

Michael Caosun and Sinan Aral. The augmentation trap: AI productivity and the cost of cognitive offloading.
  Technical Report 2604.03501, arXiv, 2026. URL https://arxiv.org/abs/2604.03501.

Jiri Chod, Evgeny Lyandres, and S. Alex Yang. Trade credit and supplier competition. Journal of Financial
  Economics, 131(2):484–505, 2019. doi: 10.1016/j.jfineco.2018.08.008.

R. H. Coase. The problem of social cost. Journal of Law and Economics, 3:1–44, 1960.

Diego Comin, Danial Lashkari, and Martí Mestieri. Structural change with long-run income and price effects.
  Econometrica, 89(1):311–374, 2021.

Russell Cooper and Andrew John. Coordinating coordination failures in Keynesian models. Quarterly
  Journal of Economics, 103(3):441–463, 1988.

Russell W. Cooper and John C. Haltiwanger. On the nature of capital adjustment costs. Review of Economic
  Studies, 73(3):611–633, 2006.

Arnaud Costinot and Iván Werning. Robots, trade, and Luddism: A sufficient statistic approach to optimal
  technology regulation. Review of Economic Studies, 90(5):2261–2291, 2023.

Tyna Eloundou, Sam Manning, Pamela Mishkin, and Daniel Rock. GPTs are GPTs: Labor market impact
  potential of LLMs. Science, 384(6702):1306–1308, 2024. doi: 10.1126/science.adj0998.

Emmanuel Farhi and Iván Werning. A theory of macroprudential policies in the presence of nominal rigidities.
  Econometrica, 84(5):1645–1704, 2016. doi: 10.3982/ECTA11883.

Bruce C. Greenwald and Joseph E. Stiglitz. Externalities in economies with imperfect information and
  incomplete markets. The Quarterly Journal of Economics, 101(2):229–264, 1986. doi: 10.2307/1891114.

João Guerreiro, Sergio Rebelo, and Pedro Teles. Should robots be taxed? Review of Economic Studies, 89
  (1):279–311, 2022.

Louis S. Jacobson, Robert J. LaLonde, and Daniel G. Sullivan. Earnings losses of displaced workers. American
  Economic Review, 83(4):685–709, 1993.

Nicholas Kaldor. Alternative theories of distribution. Review of Economic Studies, 23(2):83–100, 1956.

Jussi Keppo, Yuze Li, Gerry Tsoukalas, and Nuo Yuan. On the fragility of AI agent collusion. Working
  paper, Boston University and National University of Singapore, January 2026. SSRN 5386338.


                                                    38
John Maynard Keynes. Economic possibilities for our grandchildren. In Essays in Persuasion, pages 358–373.
  Macmillan, London, 1930.

Anton Korinek and Joseph E. Stiglitz. Artificial intelligence and its implications for income distribution and
  unemployment. In Ajay Agrawal, Joshua Gans, and Avi Goldfarb, editors, The Economics of Artificial
  Intelligence: An Agenda. University of Chicago Press, Chicago, 2019.

Boshuo Li, Ni Huang, and Wei Shi. Forced to change? Media exposure of labor issues and firm artificial
  intelligence investment. Information Systems Research, 37(1):156–175, 2025. doi: 10.1287/isre.2022.0402.

Robert E. Lucas. Adjustment costs and the theory of supply. Journal of Political Economy, 75(4):321–334,
  1967.

N. Gregory Mankiw and Michael D. Whinston. Free entry and social inefficiency. RAND Journal of Eco-
  nomics, 17(1):48–58, 1986.

Kiminori Matsuyama. The rise of mass consumption societies. Journal of Political Economy, 110(5):1035–
  1070, 2002.

Kevin M. Murphy, Andrei Shleifer, and Robert W. Vishny. Industrialization and the big push. Journal of
  Political Economy, 97(5):1003–1026, 1989.

Annie Palmer. Block laying off about 4,000 employees, nearly half of its workforce. CNBC, 2026.

Arthur Cecil Pigou. The Economics of Welfare. Macmillan, London, 1920.

Valerie A. Ramey and Matthew D. Shapiro. Displaced capital: A study of aerospace plant closings. Journal
  of Political Economy, 109(5):958–992, 2001.

David Ricardo. On the Principles of Political Economy and Taxation. John Murray, London, 3rd edition,
  1821.

Paul N. Rosenstein-Rodan. Problems of industrialisation of Eastern and South-Eastern Europe. Economic
  Journal, 53(210/211):202–211, 1943.

Carl Shapiro and Joseph E. Stiglitz. Equilibrium unemployment as a worker discipline device. American
  Economic Review, 74(3):433–444, 1984.

Hugh Son. Goldman Sachs is piloting its first autonomous coder in major AI milestone for Wall Street.
  CNBC, 2025.

Lawrence H. Summers. U.S. economic prospects: Secular stagnation, hysteresis, and the zero lower bound.
  Business Economics, 49(2):65–73, 2014.

Lawrence H. Summers. Demand side secular stagnation. American Economic Review, 105(5):60–65, 2015.


                                                     39
James van Geelen and Alap Shah. The 2028 Global Intelligence Crisis. Citrini Research, February 2026.
  URL https://www.citriniresearch.com/p/2028gic.

Martin L. Weitzman. The simple macroeconomics of profit sharing. American Economic Review, 75(5):
  937–953, 1985.

S. Alex Yang and Angela Huyue Zhang. Generative AI and copyright: A dynamic perspective. Technical
  report, Working paper, 2024. SSRN 4716233.

Joseph Zeira. Workers, machines, and economic growth. Quarterly Journal of Economics, 113(4):1091–1117,
  1998.




                                                  40
A     General-Equilibrium Robustness of the Demand Channel

The paper assumes some fraction of displaced wage income leaks out of the modeled sector. A
reasonable GE objection is that this lost income should rotate back through another channel, which
would eliminate the demand destruction mechanism. We address this by listing the channels through
which a GE model could plausibly undo the core result, explaining in each case why it is unlikely
to do so, particularly for the firms most exposed to AI displacement.


Channel 1: Owners absorb the lost spending. If owners spent each additional dollar of
income the way workers spend wages, automation would simply shift income between groups and
the demand destruction mechanism would vanish. But empirically, they do not. Wealthy owners
have already covered their basic needs and bought their durables, so additional income, whether
from rising profits or rising asset prices, flows to luxury, savings, or further asset accumulation, not
back to the mass-market goods displaced workers used to buy (Matsuyama, 2002; Comin et al.,
2021; Boppart, 2014). Mass-sector demand therefore falls, and the over-automation mechanism
would continue to apply.


Channel 2: Mass-market firms move to where the dollars now go. If owner spending leaves
the mass market, mass-market firms may try to follow. This is not always possible. Production is
tied to the factories already built, the brand earned over years, the distribution network already
in place, and the workforce already trained, and reallocating any of these takes time and money
(Ramey and Shapiro, 2001; Cooper and Haltiwanger, 2006). On the timescale of AI displacement,
retooling may not be an option. The Prisoner’s Dilemma logic of Corollary 1 also rules out a
unilateral pause: a firm that holds back to reposition loses cost savings now and recoups luxury
revenue years later, if at all. Much of the redirected demand is unlikely to be captured by the firms
that lost the original wages, so the demand destruction at the firm level is likely to persist.


Channel 3: Displaced workers find new jobs. Displaced workers who find new jobs recover
some of the lost income, which shrinks the wedge. We already account for this through η, and
Corollary 2 works through the consequences. The inefficiency vanishes only at η = 1: at η < 1
the market over-automates, at η > 1 it under-automates. Our result requires only η < 1, and the
historical record on displaced workers shows large and persistent earnings losses long after layoffs
(Jacobson et al., 1993). A richer labor-market model might refine how η evolves over time, but its
trajectory under AI displacement is uncertain; to the extent reabsorption is slow, reemployment


                                                  41
alone would not eliminate the externality. And even if reemployment does eventually catch up,
some of the over-automation damage could already be done in the interim: laid-off workers may
bear sharp transitional losses, and the automation investments that displaced them are largely
irreversible (Section 6).


Channel 4: Wages fall and the externality closes on its own. Section 5.3 represents wage
adjustment in reduced form, with a wage schedule w(ᾱ). The objection is that a fuller GE treatment
of wage formation might close the externality where the reduced form does not. There are reasons
to doubt that it would. The competitive demand-allocation mechanism is largely independent of
how wages are formed: each firm’s demand loss is still spread across all N firms in equal shares, so
each firm tends to bear only a fraction of the demand it destroys (Proposition 9). And the wage
adjustment that would close the externality, namely wages falling close to AI’s cost c, is constrained
in practice by subsistence and minimum-wage floors; even if those constraints did not bind, the
resolution would be Pyrrhic, with retained workers earning barely more than the machines that
would replace them. Where wages are fully flexible and can fall all the way to AI’s cost c (µ = 0),
this adjustment eliminates the wedge in the limit, but only by extinguishing the cost saving that
drives automation, so the efficiency gain is purchased entirely through depressed worker incomes;
once a wage floor binds or workers receive positive weight, even that limiting route is foreclosed.


Channel 5: A flexible interest rate absorbs the demand loss. The deepest GE objection
is not about where displaced income goes within the product market. It is about the interest
rate. Displaced workers cut their consumption because they have lost income, not because they
choose to save more; on standard smoothing logic they would, if anything, dissave or borrow. The
extra desired saving comes instead from the redistribution toward owners, who have a lower overall
propensity to consume and so save a larger share of their income, raising aggregate desired saving.
This channel lies outside our framework: the model is a one-shot game with no intertemporal saving,
investment, or real interest rate, so whether the leakage is reabsorbed depends on a dynamic GE
closure we do not formalize here. We therefore treat it as a robustness argument rather than a
model result. In a frictionless economy the real interest rate falls in response. It keeps falling until
the extra saving is matched by extra investment and spending by others, so total output returns
to potential. The demand loss is then not destroyed but transferred through the interest rate. An
externality that works purely through a price in this way is called pecuniary. The classic efficiency
result for competitive markets says it warrants no corrective tax.



                                                  42
    This objection is correct under its premises. It is also useful, because it identifies exactly when
the externality is real rather than merely pecuniary: when the interest rate cannot fall far enough
to do the absorbing. Two such conditions are directly relevant to AI displacement. The first is
when interest rates are already near zero. The central bank then cannot push them low enough to
offset the extra saving, so the gap shows up as lost output rather than a lower rate. This is the
welfare-relevant aggregate demand externality formalized by Farhi and Werning (2016). The “safety
trap” of Caballero and Farhi (2018) is a prominent instance, there driven specifically by a shortage
of safe assets. The second condition is incomplete financial markets (Greenwald and Stiglitz, 1986).
Displaced workers typically cannot borrow against uncertain future retraining income. The interest-
rate adjustment that lets an unconstrained household smooth through the shock therefore does not
help them, even when the rate is free to move. Under either condition the externality is real, not
pecuniary, and the companion general-equilibrium project is built around the first.


Summary. Our result requires one thing: that displaced wage income not return in full to the
modeled sector. Channels 1, 2, and 3 each appear to block that rotation under realistic conditions for
mass-market firms exposed to AI, and Channel 4 narrows but is unlikely to close the gap. Channel 5
is different in kind, and lies outside the static model: it asks whether the lost demand is genuinely
destroyed or merely transferred through the interest rate, a question that turns on a dynamic GE
closure rather than on our one-shot framework. It shows the externality stays real under one of two
conditions: interest rates near zero, or incomplete financial markets. Taken together, the argument
is that the conclusion would likely survive a full GE treatment, with the externality biting hardest
at mass-market firms.


B     Proofs

Proof of Proposition 1.
Preamble and part (i): Nash equilibrium. From eq. (6), we have
                                                                
                                               
                                              ℓ    k      ℓ X
                           πi = Π0 + Lαi s −     − αi2 −     αj 
                                              N    2      N
                                                                    j̸=i


    Differentiating with respect to αi (only the terms involving αi contribute, since the rivals’ sum




                                                  43
P
  j̸=i αj is a constant from firm i’s perspective):

                                                            
                                      ∂πi             ℓ
                                          =L       s−     − kαi .                                       (13)
                                      ∂αi             N

The second derivative is
                                             ∂ 2 πi
                                                    = −kL < 0,
                                             ∂αi2
so πi is strictly concave in αi .
    Setting the first-order condition to zero:
                                     
                               ℓ                                          s − ℓ/N
                          L s−   − kαi = 0                =⇒      αi∗ =           .
                               N                                             k

    Now, αi is restricted to the range [0, 1] (since it is the fraction of work automated).
                            2
    If αi∗ > 1, then since ∂∂απ2i < 0, ∂α
                                       ∂πi
                                          i
                                            > 0 for αi < αi∗ , so in this case, the maximum value of πi (αi )
                                i

occurs at αi = 1.
                                ∂πi
    Similarly, if αi∗ < 0, then ∂α i
                                     < 0 for αi > αi∗ , so in this case, the maximum value of πi (αi )
occurs at αi = 0. Note that αi∗ < 0 if and only if s < ℓ/N , i.e., N < ℓ/s = N ∗ ; this establishes the
preamble claim that no firm automates when N ≤ N ∗ .
   Note that αi∗ does not depend on any rival’s choice αj (j ̸= i): the rivals’ automation levels
                                            P
enter only through the additive term −(ℓ/N ) j̸=i αj , which does not affect the first-order condition.
Hence firm i’s optimal strategy is independent of α−i (a dominant strategy), and is to set

                                                     s − ℓ/N
                                              αi =           ,
                                                        k

provided the right-hand side lies in [0, 1]; otherwise αi = 0 or αi = 1 at the respective boundary.
Since every firm solves the same problem, the unique symmetric Nash equilibrium has αi = αN E
for all i.

    Part (ii): Cooperative optimum. Summing the per-firm profit (5) over all N firms, the sector’s




                                                     44
total profit is

                                       N
                                       X
                             πtot :=         πi
                                       i=1
                                       N                              
                                       X                       k
                                  =          Π0 + L sαi − ℓᾱ − αi2
                                                               2
                                       i=1
                                                                              N
                                                  X                     kL X 2
                                  = N Π0 + Ls           αi − LℓN ᾱ −       αi .
                                                                         2
                                                   i                          i=1

        P
Using     i αi = N ᾱ, this simplifies to

                                                                         N
                                                                  kL X 2
                                 πtot = N Π0 + N Lᾱ(s − ℓ) −         αi .
                                                                   2
                                                                        i=1


The first two terms depend on α only through ᾱ; the last term, − kL                    2
                                                                                     P
                                                                   2                 i αi , is maximized (least

negative) when the αi are as equal as possible, by convexity of x2 . Formally, for any fixed ᾱ,
P 2          2
  i αi ≥ N ᾱ with equality if and only if αi = ᾱ for all i (by the QM–AM inequality). Hence the

optimum is symmetric: αi = α for all i, and ᾱ = α. Substituting:

                                                                   kN Lα2
                                  πtot = N Π0 + N Lα(s − ℓ) −             .                               (14)
                                                                     2

This is a concave quadratic in α:

                        ∂πtot                                   ∂ 2 πtot
                              = N L(s − ℓ) − kN Lα,                      = −kN L < 0.
                         ∂α                                      ∂α2

Setting the first-order condition to zero:

                                                                             s−ℓ
                              N L(s − ℓ) − kN Lα = 0          ⇒    α∗ =          .
                                                                              k

Since πtot is strictly concave, this is the unique global maximum on R. Restricting to α ∈ [0, 1]: if
(s − ℓ)/k > 1, strict concavity implies ∂πtot /∂α > 0 on [0, 1], so the constrained maximum is α = 1;
if (s − ℓ)/k < 0, then ∂πtot /∂α < 0 on [0, 1], so the constrained maximum is α = 0. Thus

                                                          s−ℓ
                                                  αCO =       ,
                                                           k

with boundary values 0 or 1 when the expression falls outside [0, 1].



                                                        45
   Part (iii): Over-automation wedge. Suppose N > N ∗ , so αN E = (s − ℓ/N )/k > 0 by (i).
   Case s > ℓ. Restrict to ℓ < s < k + ℓ/N , so both αN E = (s − ℓ/N )/k and αCO = (s − ℓ)/k are
interior. Subtracting:

                                    s − ℓ/N   s−ℓ   ℓ − ℓ/N   ℓ (1 − 1/N )
                     αN E − αCO =           −     =         =              .
                                       k       k       k            k

This is strictly positive for N ≥ 2 because ℓ > 0 and 1 − 1/N > 0.
   For k + ℓ/N ≤ s < k + ℓ, αN E = 1 while αCO = (s − ℓ)/k ∈ (0, 1), so the wedge is 1 − (s − ℓ)/k;
this equals the plateau ℓ(1 − 1/N )/k at s = k + ℓ/N and decreases to 0 as s approaches k + ℓ. For
s ≥ k + ℓ both rates equal 1 and the wedge is 0.
   For the comparative statics, write the wedge as W = ℓ(1 − 1/N )/k:

                    ∂W      ℓ
                        =       >0                              (increasing in N ),
                    ∂N    kN 2
                    ∂W    1 − 1/N
                        =          >0                           (increasing in ℓ),
                     ∂ℓ       k
                    ∂W      ℓ(1 − 1/N )
                        =−              <0                      (decreasing in k).
                    ∂k          k2

   Part (iv): Boundary cases.
   When s ≤ ℓ, then (s − ℓ)/k ≤ 0, so αCO = 0. So the wedge is αN E − αCO = αN E . Since
we are in the setting where N > N ∗ , we have (s − ℓ/N )/k > 0. It is still possible, however, that
(s − ℓ/N )/k > 1.
   If s < k + ℓ/N , then αN E = (s − ℓ/N )/k, and this is the wedge. If s ≥ k + ℓ/N , then αN E is a
corner case, αN E = 1, and this is the wedge.

                                          µℓ
Lemma 1 (Boundary cases). Write δ(µ) := λ(1−µ) for the additional planner correction beyond
αCO . Then, for k > 0
  (i) αN E is interior if and only if ℓ/N < s < k + ℓ/N ; Note that N > N ∗ is equivalent to s > ℓ/N .
 (ii) αCO is interior if and only if ℓ < s < k + ℓ;
(iii) αSP (µ) is interior if and only if ℓ + δ(µ) < s < k + ℓ + δ(µ).
Each interval has width k. Because ℓ/N < ℓ < ℓ+δ(µ) for µ > 0, the three windows are progressively
shifted to the right: interior automation arises at the lowest cost savings under Nash behavior, at
intermediate savings under cooperation, and only at the highest savings under the social planner.


Proof of Lemma 1. Each claim follows by checking when the raw formula lies strictly in (0, 1).



                                                   46
                            ℓ
                            N               ℓ       k+ Nℓ ℓ+δ              k+ℓ             k+ℓ+δ
                                                                                                   s
                  NE
              α
               αCO
               αSP
                                                     δ

                                     width= k

Figure 3: Interior regions for αN E , αCO , and αSP (µ) as functions of the cost saving s, where
δ = µℓ/[λ(1 − µ)]. Each shaded bar spans the values of s for which the corresponding automation
rate is strictly interior. All three intervals have the same width k; they are shifted rightward by the
progressively larger demand-loss terms that each objective internalizes.


   (i) Nash equilibrium. From Proposition 1(i), αN E = (s − ℓ/N )/k. The raw formula (s − ℓ/N )/k
is strictly positive iff s > ℓ/N (i.e., when N > N ∗ ), and strictly less than one iff s < k + ℓ/N .
   (ii) Cooperative optimum. From Proposition 1(ii), αCO = (s−ℓ)/k. The raw expression (s−ℓ)/k
is strictly positive iff s > ℓ, and strictly less than one iff s < k + ℓ.
   (iii) Social planner. From Proposition 2(i), αSP (µ) = (s − ℓ)/k − µℓ/[λ(1 − µ)k]. Collecting
terms, αSP (µ) = s − ℓ − δ(µ) /k, which is strictly positive iff s > ℓ + δ(µ) and strictly less than
                              

one iff s < k + ℓ + δ(µ).
   Finally, ℓ/N < ℓ holds because N ≥ 2 and ℓ > 0, and ℓ < ℓ + δ(µ) for every µ ∈ (0, 1), since
then δ(µ) = µℓ/[λ(1 − µ)] > 0 (at η = 1 the demand loss vanishes, ℓ = 0, so δ(µ) = 0 and the
windows coincide; αSP (µ) is defined only for µ < 1, where δ(µ) is finite).

Proof of Corollary 1 (Frictionless limit, corollary of Proposition 1).


  (i) With k = 0, firm i’s profit from (6) becomes
                                                                                   
                                                              
                                                           ℓ           ℓ X
                                  πi = Π0 + L αi s −              −              αj  .
                                                           N           N
                                                                           j̸=i


      This is affine in αi , with slope L(s − ℓ/N ). Crucially, the slope does not depend on rivals’
      choices α−i : rival automation affects the level of firm i’s profit (through the last term) but
      not the marginal return to αi . The optimal αi therefore does not depend on α−i , making it a
      dominant strategy.
      When N > N ∗ (equivalently s > ℓ/N ), the slope is strictly positive. Since πi is linear and
      increasing in αi on [0, 1], the unique optimum is the upper boundary αi∗ = 1. This holds for



                                                    47
     every firm simultaneously, so αi = 1 for all i is the unique Nash equilibrium.
 (ii) Assume additionally that the cost saving is less than the demand loss: s < ℓ. With k = 0,
                                                 P
      aggregate profit from (5) is linear in ᾱ:   i πi = N Π0 + N L(s − ℓ)ᾱ. Since s − ℓ < 0,

     this is strictly decreasing in ᾱ, so the profit-maximizing cooperative outcome is ᾱ = 0 (no
     automation), yielding per-firm profit Π0 .
     At the Nash equilibrium (ᾱ = 1), per-firm profit is Π0 + L(s − ℓ). Since s − ℓ < 0, we have
     Π0 + L(s − ℓ) < Π0 : every firm earns strictly less than under cooperation. The per-firm profit
     loss is Π0 − [Π0 + L(s − ℓ)] = L(ℓ − s). Across N firms, the total deadweight loss is N L(ℓ − s).
     For the demand loss, from eq. (2):


                                        D = A + λwLN − ℓLN ᾱ.


     At ᾱ = 0: DCO = A + λwLN . At ᾱ = 1: DN E = A + λwLN − ℓLN . Hence DCO − DN E =
     ℓLN .



Proof of Proposition 2.


 (i) The µ-planner chooses ᾱ to maximize S(µ) = µ W + (1 − µ) K from (8). We compute each
     derivative in turn. Recall that W = wLN [1 − (1 − η)ᾱ], so

                                          dW
                                              = −wN L(1 − η).                                    (15)
                                          dᾱ

     Since ℓ = λ(1 − η)w, this equals −ℓ N L/λ. Recall that K = N [Π0 + L((s − ℓ)ᾱ − k2 ᾱ2 )] (e.g.
     eq. (14)), so
                                         dK                     
                                             = N L (s − ℓ) − k ᾱ .                              (16)
                                         dᾱ
     Combining:

                     dS     dW            dK     µ ℓ NL                            
                         =µ     + (1 − µ)     =−        + (1 − µ) N L (s − ℓ) − k ᾱ .
                     dᾱ    dᾱ           dᾱ       λ

     Setting this to zero and dividing by N L > 0:

                                                             µℓ
                                       (1 − µ) (s − ℓ) − k ᾱ =   .
                                                                λ




                                                  48
    Dividing both sides by (1 − µ) > 0 and isolating k ᾱ:

                                         µℓ                                               µℓ
                   (s − ℓ) − k ᾱ =            ,          =⇒        k ᾱ = (s − ℓ) −            .
                                      λ(1 − µ)                                         λ(1 − µ)

    Dividing by k, we find
                                                    s−ℓ         µℓ
                                      αSP (µ) =         −                                           (17)
                                                     k    λ · (1 − µ) · k
    This optimum will be valid as long as 0 ≤ αSP ≤ 1. To find the bounds, define µ̄ to be the
    value where αSP (µ̄) = 0. Then, solving for µ̄, we have

                                                               µ̄ℓ
                                            s−ℓ=
                                                          λ · (1 − µ̄)
                                                     ⇓
                                                            λ(s − ℓ)
                                                   µ̄ =
                                                          ℓ + λ(s − ℓ)

    From eq. (17), we have that αSP is decreasing in µ, so if µ > µ̄, then eq. (17) will be negative.
    Similarly, setting µ to be the value where αSP (µ) = 1, we have

                                                               µℓ
                                        s−ℓ−k =
                                                          λ · (1 − µ)

                                                     ⇓
                                                            λ(s − ℓ − k)
                                                   µ=
                                                          ℓ + λ(s − ℓ − k)

    Then for µ ≤ µ, we have eq. (17) is greater than 1.
(ii) Recall


     S = µ · W + (1 − µ) · K      (eq. (8))

       = µ · wLN [1 − (1 − η)ᾱ] + (1 − µ) · N Π0 + L (s − ℓ)ᾱ − k2 ᾱ2
                                                                        
                                                                                (eqs. (8) and (14))

       = N µ wL (1 − (1 − η)ᾱ) + (1 − µ) Π0 + L (s − ℓ)ᾱ − k2 ᾱ2
                                                                   
                                                                                    
                                            ℓ                             (1 − µ)N Lk
                                                                                          ᾱ2
                             
       = N µ wL + (1 − µ)Π0 + N L −µ + (1 − µ)(s − ℓ) ᾱ + −
         |        {z         }              λ                                  2
                   a              |             {z           }       |        {z        }
                                                          b                               1
                                                                                          2γ


    where in the linear term we used w(1 − η) = ℓ/λ from (3). This is a quadratic S = a +
    b ᾱ + 12 γ ᾱ2 , with γ = −(1 − µ) N Lk < 0 strictly negative. Completing the square around the



                                                     49
     maximum x∗ = −b/γ:


                             f (x) = a + bx + 12 γ x2 = f (x∗ ) + 12 γ (x − x∗ )2 ,


     and therefore
                             f (x∗ ) − f (x) = − 12 γ (x − x∗ )2 = 12 |γ| (x − x∗ )2 ,

     where the last equality uses γ ≤ 0. Applying this with x∗ = αSP (µ) (the planner’s optimum,
     which coincides with the unconstrained vertex when it lies in [0, 1]), x = αN E , and |γ| =
     (1 − µ) N Lk:
                                                   (1 − µ) N Lk N E
                         S(αSP ) − S(αN E ) =                  [α   − αSP (µ)]2 .
                                                         2
(iii) Recall from (9), the wedge decomposes as:

                                                     ℓ(1 − 1/N )       µℓ
                               αN E − αSP (µ) =                  +            .
                                                          k        λ(1 − µ) k

     The first term, ℓ(1 − 1/N )/k, is strictly positive because ℓ > 0 and N ≥ 2. The second
     term, µ ℓ/[λ(1 − µ) k], is strictly positive for any µ ∈ (0, 1) and equals zero at µ = 0. Hence
     αN E > αCO ≥ αSP (µ) for all µ ∈ [0, 1), since the distributional term µ ℓ/[λ(1 − µ) k] ≥ 0 is
     subtracted from αCO .
     For worker income: from eq. (15), W = wLN [1 − (1 − η)ᾱ] is affine and strictly decreasing
     in ᾱ (since (1 − η) > 0 under the maintained assumption η < 1). Therefore αN E > αCO
     implies W(αN E ) < W(αCO ).
     For owner surplus: from eq. (16), dK/dᾱ = N L[(s − ℓ) − k ᾱ], which equals zero at ᾱ =
     (s − ℓ)/k = αCO and is strictly negative for ᾱ > αCO (since k > 0). Hence K is strictly
     decreasing on (αCO , αN E ], so K(αN E ) < K(αCO ).
     Provided s < k + ℓ, so that αCO < 1 and the interval (αCO , αN E ] is nonempty, both W
     and K are strictly lower at the Nash equilibrium than at the cooperative optimum, so neither
     class can be made better off by moving from αCO to αN E : the Nash equilibrium is Pareto
     dominated. At s ≥ k + ℓ both rates equal 1 and the two profiles coincide, so the dominance
     is weak.



Proof of Corollary 2 (Sign of the externality). The wedge formula αN E − αCO = ℓ (1 − 1/N )/k
follows from the same computation as Proposition 1(iii), now with ℓ = λ(1 − η)w of either sign; it



                                                    50
holds whenever both rates are interior (Lemma 1). The three sign cases follow from the sign of ℓ:
η < 1 gives ℓ > 0 (positive wedge), η = 1 gives ℓ = 0 (zero wedge, and both rates reduce to s/k),
and η > 1 gives ℓ < 0 (negative wedge). At η = 0, ℓ = λw is maximal, so the wedge λw(1 − 1/N )/k
is maximized.

Proof of Proposition 3 (Worker equity). With profit-sharing ϵ, aggregate demand satisfies

                                                                   
                                 D = A + λ wLN (1 − (1 − η)ᾱ) + ϵ Π ,
                                           |      {z         }
                                                  wage income

                                 P                            k 2
where total profit is Π = D −        i Ci = D − N L(w − sᾱ + 2 ᾱ ). Substituting the expression for Π

into the demand equation and collecting D terms on the left-hand side:


                 D(1 − λϵ) = A + λ wLN (1 − (1 − η)ᾱ) − λϵ N L w − sᾱ + k2 ᾱ2 .
                                                                                



Expanding the right-hand side and grouping by powers of ᾱ:

                                  A + λ(1 − ϵ)wLN − ℓϵ LN ᾱ − λϵ k2 N Lᾱ2
                             D=                                             ,                     (18)
                                                 1 − λϵ

where ℓϵ := ℓ − λϵs = λ(1 − η)w − λϵ(w − c).
                                                                                P
   (i) Cooperative optimum. The planner maximizes total profit Π = D −            i Ci by choosing the

common automation rate α at a symmetric profile. Differentiating D (from the expression above)
with respect to α:
                                        ∂D   −ℓϵ LN − λϵkN Lα
                                           =                  .
                                        ∂α        1 − λϵ
                             P                   k 2
Differentiating total cost   i Ci = N L(w − sα + 2 α ):

                                          P
                                        ∂( i Ci )
                                                  = N L(−s + kα).
                                          ∂α
                                 P
Setting ∂Π/∂α = ∂D/∂α − ∂(         i Ci )/∂α = 0 and rearranging:


                                                    ℓϵ N L + λϵkN Lα
                                   N L(s − kα) =                     .
                                                          1 − λϵ

Multiplying both sides by (1 − λϵ):


                                      (s − kα)(1 − λϵ) = ℓϵ + λϵkα.



                                                    51
Expanding the left-hand side and collecting α terms:

                                               
                                kα (1 − λϵ) + λϵ = s(1 − λϵ) − ℓϵ .
                                  |     {z      }
                                           =1


Substituting ℓϵ = ℓ − λϵs, the right-hand side becomes s − sλϵ − ℓ + λϵs = s − ℓ. Hence kα = s − ℓ,
giving αCO (ϵ) = (s − ℓ)/k, independent of ϵ.
   (ii) Nash equilibrium. Competitive pricing gives Revi = D/N . The owner maximizes (1 − ϵ)πi .
For ϵ ∈ [0, 1) we have (1 − ϵ) > 0, so the FOC reduces to ∂πi /∂αi = 0; the full-sharing endpoint
ϵ = 1 is reached by continuity, except in the knife-edge λϵ = 1 (only λ = 1, ϵ = 1) where the worker-
equity demand fixed point (18) has divisor 1 − λϵ = 0 and requires the separate limiting treatment
of Proposition 3. Since D depends on αi only through ᾱ (and the ᾱ2 term), and ∂ ᾱ/∂αi = 1/N ,
differentiating Revi = D/N with respect to αi and evaluating at a symmetric profile yields

                               ∂ Revi   1 ∂D    −ℓϵ L − λϵkLα
                                      =  ·    =               .
                                ∂αi     N ∂αi    N (1 − λϵ)

Combining with the cost derivative ∂Ci /∂αi = L(−s + kα), the symmetric FOC ∂ Revi /∂αi −
∂Ci /∂αi = 0 becomes:
                                                   ℓϵ + λϵkα
                                      s − kα −                = 0.
                                                   N (1 − λϵ)
Define Nϵ := N (1 − λϵ) + λϵ = N − λϵ(N − 1). Collecting the α terms on the left-hand side:
                                                  
                                   N (1 − λϵ) + λϵ           ℓϵ
                              kα                     =s−            .
                                     N (1 − λϵ)          N (1 − λϵ)
                                 |       {z        }
                                     = Nϵ /[N (1−λϵ)]


Multiplying both sides by N (1 − λϵ)/Nϵ :

                                                s N (1 − λϵ) − ℓϵ
                                       kα =                       .
                                                       Nϵ

Substituting ℓϵ = ℓ − λϵs into the numerator:

                                                              
                   s N (1 − λϵ) − (ℓ − λϵs) = s N (1 − λϵ) + λϵ − ℓ = s Nϵ − ℓ.


Hence kα = (sNϵ − ℓ)/Nϵ = s − ℓ/Nϵ , giving αN E (ϵ) = (s − ℓ/Nϵ )/k.




                                                        52
    (iii) Wedge. Subtracting the cooperative optimum from the Nash rate:

                                            s − ℓ/Nϵ s − ℓ   ℓ − ℓ/Nϵ   ℓ(Nϵ − 1)
                     αN E (ϵ) − αCO =               −      =          =           .
                                                k      k         k        k Nϵ

Since Nϵ = N − λϵ(N − 1), we have Nϵ − 1 = (N − 1) − λϵ(N − 1) = (N − 1)(1 − λϵ), so the wedge
becomes
                                                        ℓ(N − 1)(1 − λϵ)
                                           W (ϵ) =                       .
                                                             k Nϵ
To show the wedge is strictly decreasing in ϵ, write W = ℓ(N − 1)(1 − λϵ)/[k(N − λϵ(N − 1))] and
apply the quotient rule. The numerator is f (ϵ) = 1 − λϵ with f ′ = −λ, and the denominator is
g̃(ϵ) = N − λϵ(N − 1) with g̃ ′ = −λ(N − 1). By the quotient rule:

                     f ′ g̃ − f g̃ ′
                
             d f                       −λ[N − λϵ(N − 1)] + λ(N − 1)(1 − λϵ)  −λ
                   =           2
                                     =                   2
                                                                            = 2 < 0.
             dϵ g̃          g̃                        Nϵ                     Nϵ

Hence ∂W/∂ϵ = −λℓ(N − 1)/(kNϵ2 ) < 0: the wedge is strictly decreasing. Setting W = 0 requires
1 − λϵ = 0, i.e., ϵ = 1/λ, which satisfies ϵ ≥ 1 whenever λ ≤ 1.

Proof of Corollary 3 (Voluntary profit-sharing). Firm i chooses ϵi ∈ [0, 1] to maximize retained
profit (1 − ϵi )πi . Differentiating with respect to ϵi :

                                      d                              ∂πi
                                         (1 − ϵi )πi = −πi + (1 − ϵi )     .
                                     dϵi                               ∂ϵi

When firm i shares ϵi of its profit, its workers receive ϵi πi and spend λϵi πi in the sector. Firm i
captures 1/N of the resulting demand increase, so ∂πi /∂ϵi = λπi /N . Evaluating at ϵi = 0:
                                                             
                                              λπi        λ
                                        −πi +     = πi     − 1 < 0,
                                              N          N

since λ ≤ 1 and N ≥ 2. This left-endpoint sign is not sufficient on its own, because πi itself rises
with ϵi through the demand feedback, so we verify that retained profit falls throughout [0, 1] for
every rival profile. Fix the other firms’ shares at {ϵj }j̸=i and let π̂i denote firm i’s profit absent
its own-sharing feedback (its profit at ϵi = 0, holding rivals fixed), with π̂i > 0 in the maintained
                                           P
interior equilibrium. Writing Mi := N −λ j̸=i ϵj , the own-sharing channel gives πi = π̂i +λϵi πi /Mi ,
hence πi (ϵi ) = π̂i /(1 − λϵi /Mi ) and

                                                 Mi π̂i (1 − ϵi )                     Mi π̂i (Mi − λ)
               Ri (ϵi ) := (1 − ϵi )πi (ϵi ) =                    ,   Ri′ (ϵi ) = −                   .
                                                  Mi − λϵi                             (Mi − λϵi )2



                                                            53
        P
Since   j̸=i ϵj ≤ N −1, we have Mi ≥ N −λ(N −1) = N (1−λ)+λ, so for λ < 1, Mi −λ ≥ N (1−λ) > 0

and Mi − λϵi ≥ Mi − λ > 0; thus Ri′ (ϵi ) < 0 for every ϵi ∈ [0, 1] and every rival profile. Retained
profit is therefore strictly decreasing on all of [0, 1], so ϵi = 0 is the unique optimum regardless of
the other firms’ choices, a strictly dominant strategy. (Only at the knife-edge λ = 1 with all rivals
fully sharing, where Mi = 1, does Ri′ ≡ 0 and ϵi = 0 becomes weakly optimal, the same λ = 1
degeneracy noted above.)

Proof of Proposition 4. Partition the N firms into a coalition M of size M and a fringe of N −M
non-members. Let
                                                 1    X
                                       αF :=        ·   αi                                        (19)
                                               N −M
                                                        i̸∈M

be the average automation rate of fringe firms. At a symmetric profile where all coalition members
choose αM , the average automation rate is

                                            M αM + (N − M )αF
                                     ᾱ =                     .
                                                    N

From (6), a coalition member i’s profit is
                                                                
                                               
                                              ℓ    k      ℓ X
                           πi = Π0 + Lαi s −     − αi2 −     αj  .
                                              N    2      N
                                                                   j̸=i


Then
                                                                  
                                  
                                 ℓ    k      ℓ   X          X
              πi = Π0 + Lαi s −     − αi2 −            αj +     αj 
                                 N    2      N
                                                j∈M\{i}       ∈M
                                                             j/
                                                                      
                                  
                                 ℓ    k      ℓ   X
                 = Π0 + Lαi s −     − αi2 −            αj + (N − M )αF  .
                                 N    2      N
                                                         j∈M\{i}


Under a symmetric strategy, where all firms in the coalition follow the same strategy αi = αM , we
have
                                                                             
                          M       ℓ     k M 2     ℓ           M            F
                                                                              
            πi = Π0 + L α    s−       −     α   −      (M − 1)α + (N − M )α
                                 N      2          N
                                                              
                          M      ℓM       k M 2     ℓ         F
               = Π0 + L α    s−        −     α    − (N − M )α
                                  N       2         N
                                   F
                                                               
                        ℓ(N − M )α          M     ℓM       k M 2
               = Π0 − L              +L α      s−        −   α
                             N                     N       2


                                                  54
The coalition chooses αM to maximize
                                         P                                            P
                                             i∈M πi . At the symmetric equilibrium,   i∈M πi = M πi , so

maximizing the individual firm’s profit in the coalition also maximizes the coalition profits. Taking
the derivative, we find
                                                               
                    ∂πi       Mℓ      M         ℓ     M  (M − 1)ℓ
                        =L s−    − kα     =L s−   − kα −
                   ∂αM        N                 N           N

The additional term −(M − 1)ℓ/N (relative to eq. (13)) arises because each coalition member
internalizes the demand loss its automation imposes on the other M − 1 members, each of whom
loses ℓL/N in revenue. Setting the first-order condition to zero:

                                                    s − M ℓ/N
                                             αM =             ,
                                                        k

clamped to [0, 1]. At M = 1, this reduces to αN E = (s − ℓ/N )/k. At M = N , it reduces to
αCO = (s − ℓ)/k.
   When both αM and αCO are interior, the residual wedge is

                                         s − M ℓ/N   s−ℓ   ℓ(1 − M/N )
                            αM − αCO =             −     =             ,
                                             k        k         k

which is strictly positive for M < N and zero only at M = N .

Proof of Proposition 5 (Pigouvian automation tax).


  (i) Under the tax, firm i’s profit from (6) becomes
                                                                      
                                                     
                                                    ℓ    k      ℓ X
                             πi = Π0 + Lαi s − τ −     − αi2 −     αj  .
                                                    N    2      N
                                                                          j̸=i


     The first-order condition is s − τ − ℓ/N − kαi = 0, giving αN E (τ ) = (s − τ − ℓ/N )/k. Setting
     αN E (τ ) = αCO = (s − ℓ)/k yields τ ∗ = ℓ − ℓ/N = ℓ(1 − 1/N ).
 (ii) At τ = τ ∗ , all firms choose αCO . Per-firm profit is π tax = π(αCO )−τ ∗ LαCO = π CO −τ ∗ LαCO .
     Total tax revenue is τ ∗ LN αCO . Rebated as an exogenous lump sum (each firm’s receipt is fixed
     independently of its own automation choice, so it does not re-enter the first-order condition),
     each firm receives τ ∗ LαCO , restoring profit to π CO without altering the marginal incentive
     that pins down τ ∗ .




                                                     55
Proof of Proposition 6 (AI productivity widens the over-automation wedge).

                                                                                                P
  (i) With ϕ > 1, perfect competition allocates revenue by output share: Revi = D · Yi /          j Yj ,

     which reduces to D/N only once the symmetric profile αi = α is imposed. The derivative below
                                                                               P
     is taken on this general form, so that the dependence of the denominator j Yj on αi (the
     source of the market-share gain) is retained before symmetry is substituted. The firm’s first-
     order condition equates the marginal benefit of automation to its marginal cost: ∂ Revi /∂αi +
     sL − kLαi = 0, where sL is the per-unit cost saving from replacing a worker with AI and
     kLαi is the marginal integration friction. Substituting the marginal revenue from (10) and
     rearranging, the symmetric first-order condition is

                                             ℓ   D(α) (ϕ − 1)(N − 1)
                                  kα = s −     +                      .
                                             N   N 2 [1 + (ϕ − 1)α] L

     Define LHS(α) = kα and let RHS(α) denote the right-hand side. The left-hand side is strictly
     increasing (slope k). The right-hand side is strictly decreasing: the market-share term has
     numerator proportional to D(α) = A + λwLN − ℓLN α (decreasing in α) and denominator
     factor 1 + (ϕ − 1)α (increasing in α). Hence LHS = RHS has a unique solution.
     To show αN E (ϕ) > αN E (1), evaluate both sides at the baseline equilibrium α = αN E (1) =
     (s − ℓ/N )/k: LHS = s − ℓ/N , while RHS = s − ℓ/N + (positive market-share term) > LHS.
     Since LHS is increasing and RHS is decreasing, the unique crossing must occur at αN E (ϕ) >
     αN E (1).
                                             P               P
 (ii) The cooperative planner maximizes        i πi   = D−     i Ci .   Total revenue equals aggregate
     demand D regardless of how output is allocated across firms: expenditure D is pinned down
     by (2), so reallocating output shares does not change total revenue. The planner’s first-order
     condition therefore depends only on costs:
                                        P
                                      ∂( i πi )
                                                = −ℓL + sL − kLαi ,
                                        ∂αi

     which is independent of ϕ. Setting to zero gives αCO (ϕ) = (s − ℓ)/k = αCO (1).
     For the generalized planner: S(µ) = µ W + (1 − µ) K. Worker income W = wLN [1 − (1 − η)ᾱ]
                                                   P
     does not depend on ϕ. Owner surplus K = D − i Ci at symmetric profiles, and neither D (2)
     nor Ci (1) depends on ϕ. Hence S(µ) is ϕ-invariant at every symmetric ᾱ, and αSP (µ; ϕ) =
     αSP (µ; 1) for all µ.
(iii) Combining (i) and (ii): αN E (ϕ) > αN E (1) while αSP (µ; ϕ) = αSP (µ; 1) for all µ, so the wedge


                                                  56
      αN E (ϕ) − αSP (µ; ϕ) is strictly larger than αN E (1) − αSP (µ; 1) for every µ. Since αN E (ϕ) is
      increasing in ϕ (by the same LHS/RHS argument with a larger market-share term), the wedge
      is strictly increasing in ϕ.



Proof of Proposition 7 (Endogenous entry, frictionless benchmark). We assume k = 0 (friction-
less case), λ = 1 (full recycling), 0 < κ < A (entry is costly but the market is viable for at least one
firm), ℓ > s (so that N ∗ > 1 by Corollary 1), and the genericity condition N ∗ ∈
                                                                                / N (so no integer
firm count sits exactly at the indifference cutoff and every integer N lies strictly on one branch of
the profit schedule).

   Step 1: the profit schedule is strictly decreasing on N. Let m = ⌊N ∗ ⌋, so m ≤ N ∗ < m + 1.
For N ≤ N ∗ , corollary 1 gives α = 0, so by (5) with λ = 1: Π∗ (N ) = A/N , which is strictly
decreasing. For N > N ∗ , full automation is dominant (corollary 1), and per-firm profit drops
by ∆ = L(ℓ − s) > 0, giving Π∗ (N ) = A/N − ∆, also strictly decreasing. At the crossing:
Π∗ (m) = A/m > A/(m + 1) > A/(m + 1) − ∆ = Π∗ (m + 1). Hence Π∗ is strictly decreasing on N.

   Step 2: existence and uniqueness of N F E . Since κ < A, Π∗ (1) = A > κ. Since ∆ > 0,
Π∗ (N ) → −∆ < 0 as N → ∞. The set S = {N ∈ N : Π∗ (N ) ≥ κ} is therefore nonempty and
finite. Let N F E = max S. By strict monotonicity, Π∗ (N F E ) ≥ κ and Π∗ (N F E + 1) < κ, so N F E
satisfies (11) and is unique.

   Step 3: characterization by regime. We determine N F E by checking which integers are in S.
   On the no-automation branch (N ≤ m): Π∗ (N ) = A/N ≥ κ iff N ≤ A/κ. So the viable integers
on this branch are {1, . . . , min(⌊A/κ⌋, m)}.
   On the full-automation branch (N ≥ m + 1): Π∗ (N ) = A/N − ∆ ≥ κ iff N ≤ A/(κ + ∆).
The smallest integer on this branch is m + 1, so viable integers exist iff m + 1 ≤ A/(κ + ∆), i.e.
κ + ∆ ≤ A/(m + 1). When nonempty, the viable set is {m + 1, . . . , ⌊A/(κ + ∆)⌋}.
   Since N F E is the largest viable integer overall:
   Case (i): (low entry cost) κ + ∆ ≤ A/(m + 1). The full-automation branch contains viable
integers up to ⌊A/(κ + ∆)⌋ ≥ m + 1. Since κ + ∆ > κ, we have A/(κ + ∆) < A/κ, so the full-
automation branch’s maximum does not exceed the no-automation branch’s maximum in absolute
terms, but it exceeds m (the cap on the no-automation branch). Hence N F E = ⌊A/(κ + ∆)⌋ ≥
m + 1 > N ∗ , and every firm fully automates. See fig. 4(a).
   Case (ii): (intermediate entry cost) κ + ∆ > A/(m + 1) and κ < A/m. The first condition
means A/(m + 1) − ∆ < κ, so Π∗ (m + 1) = A/(m + 1) − ∆ < κ. Since Π∗ is decreasing, no integer

                                                  57
above N ∗ is viable. The second condition gives A/κ > m, so ⌊A/κ⌋ ≥ m. Hence the largest viable
integer on the no-automation branch is m, and N F E = m. Profit is Π∗ (m) = A/m > κ (strict,
since A/κ > m implies A/m > κ). In this case since N F E = m < N ∗ (strict, since N ∗ ∈
                                                                                      / N), no
firm automates. See fig. 4(b).
      Case (iii): (high entry cost) κ ≥ A/m. Then A/κ ≤ m, so ⌊A/κ⌋ ≤ m. Since κ + ∆ > κ ≥
A/m > A/(m + 1), no integer on the full-automation branch is viable (same argument as case (ii)).
Hence N F E = ⌊A/κ⌋. Since N F E = ⌊A/κ⌋ ≤ m ≤ N ∗ , no firm automates. See fig. 4(c).

      These three cases exhaust all κ ∈ (0, A). When κ > A, then N F E = 0.

per-firm                                    per-firm                                     per-firm
 profit       (a) Low entry cost             profit    (b) Intermediate entry cost        profit          (c) High entry cost



                                                                                               κ



                            ∆                     κ                     ∆                                               ∆

      κ
                       N∗       NFE    N                      NFE N
                                                                    ∗
                                                                                     N              NFE            N∗            N



Figure 4: Per-firm profit as a function of the number of firms in the frictionless benchmark (k = 0,
λ = 1). In each panel, profit follows A/N for N ≤ N ∗ (no automation) and drops discretely by
∆ = L(ℓ − s) at N ∗ when full automation becomes dominant. The red dot marks the free-entry
equilibrium N F E . (a) Low entry cost: N F E lies above N ∗ and all firms automate. (b) Intermediate
entry cost: N F E = ⌊N ∗ ⌋; the threat of automation deters the marginal entrant, sustaining positive
profits without any automation occurring. (c) High entry cost: N F E falls well below N ∗ ; entry
costs alone limit competition and the automation threshold is never approached.


Proof of Proposition 8 (Endogenous entry with convex costs). First, we show that the per-firm
profit is decreasing in N . From eq. (5), we can write


                                              π N E (N ) = A/N + C + g(N )                                                      (20)


where


                                           C := (λ − 1)wL                                                                       (21)

                                      g(N ) := L αN E (N ) (s − ℓ) − k2 αN E (N )
                                                                                 
                                                                                                                                (22)


Since A/N is strictly decreasing on N, it suffices to show that g is weakly decreasing for N ∈ N.
First, note that g(·) is decreasing in αN E

                                               dg                      NE
                                                                           
                                                    = L   (s − ℓ) − k α                                                         (23)
                                              dαN E

                                                               58
By assumption ℓ > s, so the derivative is always negative. Then, by Proposition 1, we have
                                             
                                    NE
                                              0                       if N ≤ sℓ
                                α        =           
                                                         s−ℓ/N
                                                                                              (24)
                                              min
                                                           k , 1       if N > sℓ


So αN E is non-decreasing in N . Thus g(αN E (N )) is non-increasing in N .
   Since A/N is decreasing in N , and g αN E (N ) is non-increasing in N , so π N E (N ) = A/N +
                                                   

C + g(N ) is strictly decreasing in N , i.e., π N E (N ) > π N E (N + 1).
     Now, let
                                         S := {N ∈ N : π N E (N ) ≥ κ}                         (25)

Since π N E (1) = Π0 (1) > κ by assumption, the set S is non-empty. To see that S is finite, we need
to show that limN →∞ π N E < κ. First,

                                                              s
                                    α∞ := lim αN E (N ) = min 1,                               (26)
                                         N →∞                    k

So
                                 lim g(N ) = L α∞ (s − ℓ) − k2 α∞ ≤ 0
                                                                
                                                                                               (27)
                                N →∞

because s < ℓ (by assumption), with strict inequality whenever s > 0 (at s = 0, α∞ = 0 and the
limit is 0). Thus


                lim π N E (N ) = lim [A/N + C + g(N )] = (λ − 1)wL + lim g(N ) ≤ 0             (28)
                N →∞             N →∞                                              N →∞


Here C = (λ − 1)wL ≤ 0 (equality only at λ = 1) and limN →∞ g(N ) ≤ 0, so limN →∞ π N E ≤ 0 < κ;
since κ > 0 the inequality relative to κ is strict, and the set S is finite. Let


                                              N F E := max (N ∈ S)                             (29)


Then π N E (N F E ) ≥ κ and π N E (N F E + 1) < κ, so N F E satisfies (11). If N F E > N ∗ , then
αN E (N F E ) = min (s − ℓ/N F E )/k, 1 > 0; since ℓ > s implies αCO = max{0, (s − ℓ)/k} = 0, we
                                       

have αN E (N F E ) > αCO , so over-automation persists.

Proof of Proposition 9 (Endogenous wages). The symmetric equilibrium is a fixed point: ᾱ such
that ᾱ = αN E (w(ᾱ)).




                                                          59
    (i) At a symmetric rate αi = α for all i, we have ᾱ = α and, from (5),


                                   πi = Π0 + L s α − ℓ α − k2 α2 .
                                                                


                      P
Aggregate profit is     i πi = N πi .   Consistent with the wage-taking convention, we differentiate
at fixed w and evaluate the resulting condition at the equilibrium wage w(α); differentiating with
respect to α and dividing by N L yields the planner’s per-firm marginal benefit of automation:

                                                                              
    g(α) := s(α) − ℓ(α) − kα = w(α) − c − λ(1 − η)w(α) − kα = w(α) 1 − λ(1 − η) − c − kα,


where we used s = w − c and ℓ = λ(1 − η)w. By contrast, each firm’s profit from (6) depends on ᾱ
only through its own revenue share ℓ/N . Differentiating with respect to αi and dividing by L gives
the private marginal benefit:
                                                                  
                                     ℓ(α)                 λ(1 − η)
                      h(α) := s(α) −      − kα = w(α) 1 −            − c − kα.
                                      N                      N

Differentiating, g ′ (α) = w′ (α)[1 − λ(1 − η)] − k; the first term is weakly negative and k > 0, so
g ′ < 0. The same argument applies to h (whose coefficient 1 − λ(1 − η)/N > 0 for N ≥ 2), so both
are strictly decreasing. Note that g(α) = h(α) − ℓ(α)(1 − 1/N ) for all α. At the NE fixed point,
h(αN E ) = 0 by definition, so


                      g(αN E ) = 0 − ℓ(αN E )(1 − 1/N ) = −ℓ(αN E )(1 − 1/N ) < 0.


Since g is strictly decreasing and g(αCO ) = 0 (the planner’s optimality condition), the inequality
g(αN E ) < 0 = g(αCO ) implies αCO < αN E . This argument zeroes both first-order conditions
(h(αN E ) = 0 and g(αCO ) = 0), so it presumes both rates interior. At the full-automation corner,
where s(ᾱ) ≥ k + ℓ(ᾱ) pins αN E = αCO = 1, the automation-rate gap is zero and the strict
inequality lapses; the externality persists in firms’ incentives but the rate comparison can no longer
register it.
    (ii) From (7), the threshold is N ∗ (w) = λ(1 − η)w/(w − c). Applying the quotient rule:

                       ∂N ∗   λ(1 − η)(w − c) − λ(1 − η)w   −λ(1 − η)c
                            =                   2
                                                          =            < 0,
                        ∂w              (w − c)              (w − c)2

so N ∗ is strictly decreasing in w when c > 0 and η < 1 (and weakly otherwise: at c = 0 or η = 1
the derivative is zero and N ∗ is wage-invariant). Since w′ (ᾱ) ≤ 0 by assumption, w(ᾱ) ≤ w(0) for


                                                   60
all ᾱ ≥ 0. Combining: N ∗ (w(ᾱ)) ≥ N ∗ (w(0)), with strict inequality whenever w(ᾱ) < w(0), c > 0,
and η < 1.

Corollary 4 (Generalized planner under wage adjustment). Under the conditions of Proposition 9,
                                                                     
let µ ∈ [0, 1) and define gµ (α) := s(w(α)) − ℓ(w(α)) 1 + µ/(λ(1 − µ)) − kα. If gµ is strictly
decreasing, then αN E > αSP (µ) whenever the planner’s rate is interior (s(ᾱ) < k + ℓ(ᾱ) + δ(µ)).

Proof sketch. The argument mirrors part (i) of Proposition 9, replacing the cooperative planner’s
marginal benefit g with the µ-planner’s. The µ-planner maximizes S(µ) = µ W + (1 − µ) K over a
common rate α, taking wages as given. From the proof of Proposition 2, the first-order condition is

                                                        µ ℓ(α)
                                (1 − µ) s(α) − ℓ(α) − kα =       ,
                                                             λ

which can be rewritten as gµ (α) = 0. This function relates to the private marginal benefit h(α) =
s(α) − ℓ(α)/N − kα from the proof of Proposition 9 by
                                                                 
                                                     1      µ
                            gµ (α) = h(α) − ℓ(α) 1 −   +            .
                                                     N   λ(1 − µ)

At the Nash equilibrium, h(αN E ) = 0, so
                                                                 
                                                     1      µ
                          gµ (αN E ) = −ℓ(αN E ) 1 −   +            < 0,
                                                     N   λ(1 − µ)

since ℓ > 0, N ≥ 2, and µ > 0. At the planner’s fixed point, gµ (αSP (µ)) = 0 by definition. If
gµ is strictly decreasing, the inequality gµ (αN E ) < 0 = gµ (αSP ) implies αSP (µ) < αN E , exactly
as in the µ = 0 case. As in Proposition 9, this zeroes gµ and so holds on the interior; once
s(ᾱ) ≥ k + ℓ(ᾱ) + δ(µ) pins αSP (µ) = αN E = 1 (Lemma 1), the gap closes and the strict inequality
lapses.
   It remains to verify monotonicity. Differentiating:
                                                                 
                                                              µ
                           gµ′ (α) = w′ (α)1 − (1 − η) λ +              − k.
                                                             1−µ

Define the bracket as Cµ := 1 − (1 − η)[λ + µ/(1 − µ)]. At µ = 0, C0 = 1 − λ(1 − η) ≥ 0, which is
the coefficient used in the proof of Proposition 9; since w′ ≤ 0, the product w′ C0 ≤ 0 and g0′ < 0
follows immediately. For µ > 0, Cµ decreases. As long as Cµ ≥ 0, the same argument applies; this
holds for all µ ≤ µ̄ := [1 − (1 − η)λ]/[2 − η − (1 − η)λ] (approximately 0.48 at λ = 0.5, η = 0.30).
When Cµ < 0, the product w′ Cµ ≥ 0, so gµ′ < 0 requires k > |w′ (α)| · |Cµ |: integration frictions

                                                 61
must dominate wage sensitivity.
   As a numerical illustration, consider w(ᾱ) = 1 − 0.5 ᾱ, c = 0.30, λ = 0.5, η = 0.30, k = 1,
N = 7, and µ = 0.3. The equilibrium rates are αN E ≈ 0.44, αCO ≈ 0.26, and αSP (0.3) ≈ 0.04,
confirming αSP < αCO < αN E . The distributional premium is substantial: the µ-planner would
reduce automation to near zero, well below the cooperative optimum that already lies far below the
Nash rate.

Proof of Proposition 10 (Capital income recycling). We derive the result for general k ≥ 0; the
proposition’s two parts follow from the k = 0 specialization.
    Aggregate demand is D = A + λwLN − ℓLN ᾱ + η̂Π, where total profit is Π = D − N L(w −
sᾱ) − k2 L j αj2 . Substituting and solving for D:
           P



                        D(1 − η̂) = A + (λ − η̂)wLN − ℓη̂ LN ᾱ − η̂k                  2
                                                                            P
                                                                   2 L              j αj ,


                                                                    P
with ℓη̂ = ℓ − η̂s. When k = 0 this gives (12). Since N ᾱ = αi +    j̸=i αj , differentiating:


                                       ∂D      ℓη̂ L   η̂kL
                                           =−        −      αi .
                                       ∂αi    1 − η̂ 1 − η̂

Revenue Revi = D/N gives ∂ Revi /∂αi = −ℓη̂ L/[N (1 − η̂)] − η̂kLαi /[N (1 − η̂)]. Firm i’s marginal
profit, including the direct cost saving sL and marginal friction kLαi , is
                                                                            !
                             ∂πi          ℓη̂                N̂
                                 =L s−            − kαi ·                       ,
                             ∂αi       N (1 − η̂)         N (1 − η̂)


where N̂ := N (1 − η̂) + η̂. This depends only on αi , so the equilibrium is in strictly dominant
strategies.
   Part (i): k = 0. The marginal profit reduces to L(s − ℓη̂ /[N (1 − η̂)]), a constant independent
                                                                        ℓ
                                                                        η̂
of αi . This is positive if and only if sN (1 − η̂) > ℓη̂ , i.e. N > s(1−η̂) = Nη̂ . Thus, when ℓη̂ > 0
so that Nη̂ > 0, full automation is strictly dominant when N > Nη̂ and no automation is strictly
dominant when N < Nη̂ , reproducing the structure of Corollary 1; when ℓη̂ ≤ 0 the marginal profit
L(s − ℓη̂ /[N (1 − η̂)]) is positive for every N , so full automation is unconditionally dominant, the
case characterized in part (ii).
   Part (ii). ℓη̂ = ℓ − η̂s ≤ 0 if and only if η̂ ≥ ℓ/s.




                                                    62
   Extension to k > 0. Setting the first-order condition to zero:
                                                                 
                               N (1 − η̂)               ℓη̂               sN̂ − ℓ       s − ℓ/N̂
                      αN E =                    s−                    =             =            .
                                  k N̂               N (1 − η̂)            k N̂            k

This is positive if and only if N̂ > N ∗ , reproducing Proposition 1 with N replaced by N̂ . At a
                                                           N
symmetric profile (αj = α for all j), total profit is Π = 1−η̂ [Π0 + L(s − ℓ)α − k2 Lα2 ]. The 1/(1 − η̂)
multiplier scales the objective without changing the optimizer, so αCO = max{0, (s − ℓ)/k}, the
same as in Proposition 1.




                                                         63
