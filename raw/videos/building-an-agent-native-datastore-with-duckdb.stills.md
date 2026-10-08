---
title: Building an agent-native datastore with DuckDB
video_id: vtll31BjojA
url: https://www.youtube.com/watch?v=vtll31BjojA
channel: MotherDuck
duration: '28:05'
transcript: building-an-agent-native-datastore-with-duckdb.md
stills_dir: ../images/building-an-agent-native-datastore-with-duckdb/
stills_count: 17
extractor:
  model: gemini-3.8-flash
  processing: static
  resolution: default
  processing_rounds: 0
  frame_rule: end of display window minus 1s
  frames: 18 frames by stream seek, no download
acquired: '2026-10-06'
usage:
  total_tokens: 158320
  total_input_tokens: 153627
  total_cached_tokens: 0
  total_output_tokens: 3862
  total_thought_tokens: 831
  total_tool_use_tokens: 0
notes: |
  Machine-read by gemini-3.8-flash; unverified. Stills are gitignored (raw/**/*.png).
  At Process, view each PNG, correct the reading against the pixels, and
  publish the selected stills as webp under wiki/assets/<source-page-slug>/.
---

# Stills: Building an agent-native datastore with DuckDB

Machine-read by `gemini-3.8-flash` (static processing) on 2026-10-06. **Unverified**: view each PNG and correct the reading before it reaches the wiki.

## 01 · [0:54] Building an agent-native datastore with DuckDB

- Kind: slide
- On screen: 0:10–0:55 · still taken at 0:54
- File: `../images/building-an-agent-native-datastore-with-duckdb/01-00m54-building-an-agent-native-datastore-with-duckdb.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=54s

On-screen content (machine-read):

```text
Building an agent-native datastore with DuckDB
Ashish Bagri
Co-founder and CTO, GlassFlow
Agents in Prod, Amsterdam
17th September, 2026
```

Adds vs. narration (machine-read): Introduces the speaker's role and event context.

## 02 · [2:39] What happened to checkout-service?

- Kind: slide
- On screen: 1:51–2:40 · still taken at 2:39
- File: `../images/building-an-agent-native-datastore-with-duckdb/02-02m39-what-happened-to-checkout-service.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=159s

On-screen content (machine-read):

```text
THE PROBLEM
What happened to checkout-service?
Prometheus | Loki | GitHub | Deploy log
one MCP server per tool
Four calls. Four sets of timestamps. Lined up inside the context window.
ONE MCP SERVER PER TOOL: 6 reads, 3 turns
A CORRELATED STORE: 1 read, 2 turns
THE STORE WAKES THE AGENT: 0 reads, context attached
Same incident, same agent. Single-runs, directional. Numbers in the README.
```

Adds vs. narration (machine-read): Quantifies the reduction in reads and agent turns between using separate MCP tools versus a correlated or push-based agent datastore.

## 03 · [4:34] The consumer changed

- Kind: slide
- On screen: 3:36–4:35 · still taken at 4:34
- File: `../images/building-an-agent-native-datastore-with-duckdb/03-04m34-the-consumer-changed.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=274s

On-screen content (machine-read):

```text
WHY AGENT-NATIVE
The consumer changed
THE DATA STACK WAS BUILT FOR ANALYSTS
a planning cycle, shape decided ahead | aggregations over everything | pull: someone asks | a human authors the model
AGENTS
mid-incident, mid-task | one entity, keyed, time-ordered | push: the data wakes them | they discover what they need at runtime
That is what we mean by agent-native: a store shaped by how agents read and what they add.
```

Adds vs. narration (machine-read): Contrasts the architectural assumptions of traditional analyst data stacks against the requirements of AI agents.

## 04 · [5:48] The consumer changed

- Kind: slide
- On screen: 5:26–5:49 · still taken at 5:48
- File: `../images/building-an-agent-native-datastore-with-duckdb/04-05m48-the-consumer-changed.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=348s

On-screen content (machine-read):

```text
WHY AGENT-NATIVE
The consumer changed
THE DATA STACK WAS BUILT FOR ANALYSTS
a planning cycle, shape decided ahead | aggregations over everything | pull: someone asks | a human authors the model
AGENTS
mid-incident, mid-task | one entity, keyed, time-ordered | push: the data wakes them | they discover what they need at runtime
That is what we mean by agent-native: a store shaped by how agents read and what they add.
```

Adds vs. narration (machine-read): nothing beyond the narration

## 05 · [6:35] What we set out to build

- Kind: slide
- On screen: 5:49–6:36 · still taken at 6:35
- File: `../images/building-an-agent-native-datastore-with-duckdb/05-06m35-what-we-set-out-to-build.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=395s

On-screen content (machine-read):

```text
FOUR PROPERTIES, NONE NEGOTIABLE
What we set out to build
LOSSLESS
No model in the write path. Store the original record. A summary is a read, not a write.
ORGANISED
Keyed by entity, one timeline per thing, catalogued.
SERVED TWO WAYS
Pull: the agent asks and gets the correlated window. Push: a condition fires and wakes the agent with the context attached.
AGENT-SHAPED
The agent sees what exists and adds sources, views and triggers itself. Nothing is frozen at setup.
```

Adds vs. narration (machine-read): Outlines four explicit design principles for an agent-native datastore.

## 06 · [7:38] The 29th of May: twelve components

- Kind: slide
- On screen: 7:24–7:39 · still taken at 7:38
- File: `../images/building-an-agent-native-datastore-with-duckdb/06-07m38-the-29th-of-may-twelve-components.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=458s

On-screen content (machine-read):

```text
WHAT PEOPLE LIKE US DRAW FIRST
The 29th of May: twelve components
1. Ingest connectors
2. NATS JetStream stream
3. Bronze writer
4. S3 bronze store
5. Silver compute
6. ClickHouse silver store
7. Catalog service
8. Pull serving
9. Trigger engine, JetStream KV
10. Push dispatch, queue + DLQ
11. MCP server
12. Control plane
Every box is operationally correct; I would defend any of them in a design review.
[Architecture diagram depicting flow from external sources through ingestion, brokers, storage tiers, compute, trigger engines, MCP server, and agents]
```

Adds vs. narration (machine-read): Displays the initial 12-component architecture blueprint showing pipeline and storage layers before simplification.

## 07 · [8:22] Who was actually going to run this

- Kind: slide
- On screen: 7:50–8:23 · still taken at 8:22
- File: `../images/building-an-agent-native-datastore-with-duckdb/07-08m22-who-was-actually-going-to-run-this.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=502s

On-screen content (machine-read):

```text
MAY VS SEPTEMBER
Who was actually going to run this
* Open source, MIT, runs on a laptop, pip install, two commands, no Docker.
* No external database, no broker, no ops team. AI engineers, not a platform team.
* Sub-minute freshness at team scale. Millions of events, not trillions.
* The agent is the query planner, introspectable, and it speaks SQL.
May: [12-component architecture diagram]
September: One Python process / One DuckDB file / One events table
Operationally correct, and adoption-fatal.
```

Adds vs. narration (machine-read): Compares the complex May architecture against the consolidated single-file DuckDB architecture chosen in September.

## 08 · [9:39] One table, nine columns, every source

- Kind: slide
- On screen: 8:57–9:40 · still taken at 9:39
- File: `../images/building-an-agent-native-datastore-with-duckdb/08-09m39-one-table-nine-columns-every-source.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=579s

On-screen content (machine-read):

```text
INSIDE THE FILE, 1 OF 5
One table, nine columns, every source
CREATE TABLE events (
source TEXT, -- which source
key_value TEXT, -- the entity
event_type TEXT,
text TEXT, -- what the agent reads
payload JSON, -- the record, untouched
labels JSON, -- {"service": "api-server", "value": 0.42}
event_time TIMESTAMPTZ,
ingest_time TIMESTAMPTZ
);
Lossless is the payload column.
Organised is the labels column plus the key.
The entity is the label you marked primary, copied into its own column.
Metrics, logs, alerts, commits, poll results, agent memory, agent findings: rows in this table.
Twenty-three other tables in the same file: catalog, counters, runs, secrets. Backup is cp.
```

Adds vs. narration (machine-read): Provides the exact SQL schema of the core events table and explains the role of each column.

## 09 · [10:51] No indexes on the events table

- Kind: slide
- On screen: 10:20–10:52 · still taken at 10:51
- File: `../images/building-an-agent-native-datastore-with-duckdb/09-10m51-no-indexes-on-the-events-table.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=651s

On-screen content (machine-read):

```text
INSIDE THE FILE, 2 OF 5
No indexes on the events table
[Timeline blocks t1 through t9 with t8 and t9 highlighted]
blocks of ~120,000 rows, columns stored separately, min and max kept per column per block
* Tares only appends, so new events carry newer times.
* A one-minute filter skips every old block by its summary. Only the last block or two are read.
* The hot queries never touch the payload column.
* No time window? Two small counter tables, updated in the same transaction as the insert.
```

Adds vs. narration (machine-read): Visualizes DuckDB block-skipping mechanics across append-only timestamps without secondary indexes.

## 10 · [11:50] One read query

- Kind: slide
- On screen: 11:30–11:51 · still taken at 11:50
- File: `../images/building-an-agent-native-datastore-with-duckdb/10-11m50-one-read-query.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=710s

On-screen content (machine-read):

```text
INSIDE THE FILE, 3 OF 5
One read query
SELECT event_time, source, text, labels FROM (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY source
    ORDER BY event_time DESC AS rn
  FROM events
  WHERE source IN (...)
    AND event_time >= ...
    AND json_extract_string(labels, '$.service') = 'api-server'
)
WHERE rn <= 12
ORDER BY event_time;
Correlation is a window function, not a join.
Sources correlate by stamping the same label with the same value.
Twelve newest per source. The store keeps everything. The read returns a bounded timeline.
The only way an agent pulls data. read and query are this query. A view is a saved source list plus filters.
```

Adds vs. narration (machine-read): Shows the exact SQL query used to pull and window correlated timelines across disparate event sources.

## 11 · [12:39] A trigger is a GROUP BY

- Kind: slide
- On screen: 12:09–12:40 · still taken at 12:39
- File: `../images/building-an-agent-native-datastore-with-duckdb/11-12m39-a-trigger-is-a-group-by.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=759s

On-screen content (machine-read):

```text
INSIDE THE FILE, 4 OF 5
A trigger is a GROUP BY
SELECT key_value,
  SUM(CAST(json_extract_string(labels, '$.alert_active') AS DOUBLE))
FROM events
WHERE source IN (...)
  AND event_time >= now() - 1 minute
GROUP BY key_value;
Then, in Python, per entity:
predicate  "> 0"
cooldown   one row per trigger + entity
context    the read query, 15 minutes
Runs after every ingest batch, at most once per ten seconds, on the same thread as the insert.
Detect on one minute. Hand over fifteen. The agent sees the deploy before the spike.
No streaming state, no queue, no in-memory window. The trigger engine from the May diagram is this query.
```

Adds vs. narration (machine-read): Details the SQL aggregation and Python logic used to trigger agent wakeups on incoming batches.

## 12 · [13:20] The agent's data model is the catalog

- Kind: slide
- On screen: 13:03–13:21 · still taken at 13:20
- File: `../images/building-an-agent-native-datastore-with-duckdb/12-13m20-the-agent-s-data-model-is-the-catalog.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=800s

On-screen content (machine-read):

```text
INSIDE THE FILE, 5 OF 5
The agent's data model is the catalog
create_source(labels)
derive(view)
create_trigger
subscribe
remember
Each one is an insert into a catalog table. The events table does not change.
Connectors added, labels added, labels renamed. The schema of events has not changed for any of it.
The schema is fixed and boring, so agents shape everything above it. DuckDB makes the one fixed table fast enough that nobody designs anything below it.
```

Adds vs. narration (machine-read): Lists the primary catalog modification primitives available to agents.

## 13 · [14:32] What it cost, and what it gave

- Kind: slide
- On screen: 13:38–14:33 · still taken at 14:32
- File: `../images/building-an-agent-native-datastore-with-duckdb/13-14m32-what-it-cost-and-what-it-gave.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=872s

On-screen content (machine-read):

```text
THE HONEST VERSION
What it cost, and what it gave
WHAT IT COST
Memory: Sizes itself to the host; OOM killed at ~1M events in a container. Now 60% of the cgroup, spill to disk.
Disk: Usage is stat() on the file, never a query. Ingest pauses at 95% of the volume.
Start degraded, not dead: If the file cannot be opened, the console still serves and says only.
Labels are going-forward only: The payload is lossless so a retest is always possible. Today the product trades that for a cheap edit.
The labels column is JSON: Every source flit can table on day one. It is the parse on every hot query now. Next: a typed MAP.
No retention: The file grows. Herocost with Parquet offload is next: an export, not a migration.
WHAT DUCKDB GAVE
SQLITE: the file without the analytics
A SERVER: the analytics without the file
DUCKDB: one process and one file, analytical SQL over JSON events at millions of rows, no index designed
```

Adds vs. narration (machine-read): Catalogs operational failure modes, resource guardrails, and contrasts DuckDB against SQLite and database server models.

## 14 · [16:24] Demo: building an AI SRE with Tares

- Kind: slide
- On screen: 15:33–16:25 · still taken at 16:24
- File: `../images/building-an-agent-native-datastore-with-duckdb/14-16m24-demo-building-an-ai-sre-with-tares.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=984s

On-screen content (machine-read):

```text
Demo: building an AI SRE with Tares
1 One read, all the context
Everything about a service, from every source, in one list. An agent gets it in a single call.
2 The alert wakes the agent
Something breaks, the trigger fires, and the agent writes its diagnosis onto the timeline. No one prompts it.
3 The agent decides what to watch
It creates its own view and trigger.
4 The next run knows the last one
The new diagnosis starts from the previous finding.
```

Adds vs. narration (machine-read): Defines the 4-step workflow demonstrated in the live AI SRE walkthrough.

## 15 · [17:02] What you can build with Tares

- Kind: slide
- On screen: 16:33–17:03 · still taken at 17:02
- File: `../images/building-an-agent-native-datastore-with-duckdb/15-17m02-what-you-can-build-with-tares.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=1022s

On-screen content (machine-read):

```text
BEYOND THE DEMO
What you can build with Tares
AI SRE: An alert fires; the agent reads the service's timeline and writes the diagnosis before anyone opens a dashboard. (PROMETHEUS, LOKI, GITHUB, ALERTMANAGER)
Shared code context: Commits land; when a change matters, the agent opens a pull request against the team's context repo. (GITHUB)
Challenger for your coding agent: Every Claude Code session on a timeline; a second model challenges the plan each commit; the pair exchange. (CLAUDE CODE SESSIONS)
Root cause for agent traces: An alert from your tracing tool wakes the agent; it investigates over MCP and posts the report back. (OTLP TRACES, WEBHOOKS)
Anything with a failure mode: Failed jobs, sandbox runs, voice calls, a polled status page: a timeline, a trigger on failure, a finding. (WEBHOOK, HTTP POLLING, POSTGRES)
```

Adds vs. narration (machine-read): Outlines specific use cases for Tares along with their corresponding input integrations.

## 16 · [17:49] Thank you. Try it, and stay in touch.

- Kind: slide
- On screen: 17:26–17:50 · still taken at 17:49
- File: `../images/building-an-agent-native-datastore-with-duckdb/16-17m49-thank-you-try-it-and-stay-in-touch.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=1069s

On-screen content (machine-read):

```text
GlassFlow
Thank you.
Try it, and stay in touch.
github.com/glassflow/tares
Star the repo if it is useful to you, and tell us what you build with it.
Ashish Bagri, CTO GlassFlow
MIT: uv tool install tares then tares up
[QR code to GitHub repository]
```

Adds vs. narration (machine-read): Provides installation commands and link to the open-source repository.

## 17 · [27:55] Tares UI and Claude Code Demo

- Kind: screen
- On screen: 17:51–27:56 · still taken at 27:55
- File: `../images/building-an-agent-native-datastore-with-duckdb/17-27m55-tares-ui-and-claude-code-demo.png`
- At this moment: https://www.youtube.com/watch?v=vtll31BjojA&t=1675s

On-screen content (machine-read):

```text
Tares Web UI & Terminal Integration
- Project: AI SRE demo
- Demo stack: Prometheus, api-server, log container
- Sources: demo_alerts (prometheus_alerts), demo_logs (loki), demo_metrics (prometheus)
- Views: service_timeline (key: service, api-server)
- Triggers: incident (condition: sum(alert_active) > 0 over 1m, window: 15m)
- Subscribers: incident-first-look (Tares agent)
- Claude Code integration running automated diagnosis on triggered incidents and updating Tares catalog views and triggers for p99 latency spikes.
```

Adds vs. narration (machine-read): Demonstrates the end-to-end operation of Tares ingesting logs/metrics, triggering an agent via Prometheus alert, producing an incident diagnosis, and creating follow-up views/triggers programmatically.

## Skipped

- [15:19–15:32] What it cost, and what it gave: same picture as still 13
