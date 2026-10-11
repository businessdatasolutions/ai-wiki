---
title: Three Questions Every Agent Engineer Should Be Able To Answer
video_id: oVKGKdIAgtg
url: https://www.youtube.com/watch?v=oVKGKdIAgtg
channel: LangChain
duration: '14:07'
transcript: three-questions-every-agent-engineer-should-be-able-to-answer.md
stills_dir: ../images/three-questions-every-agent-engineer-should-be-able-to-answer/
stills_count: 12
extractor:
  model: gemini-3.8-flash
  processing: static
  resolution: default
  processing_rounds: 0
  frame_rule: end of display window minus 1s
  frames: 14 frames by stream seek, no download
acquired: '2026-10-11'
usage:
  total_tokens: 79940
  total_input_tokens: 77369
  total_cached_tokens: 75596
  total_output_tokens: 2571
  total_thought_tokens: 0
  total_tool_use_tokens: 0
notes: |
  Machine-read by gemini-3.8-flash; unverified. Stills are gitignored (raw/**/*.png).
  At Process, view each PNG, correct the reading against the pixels, and
  publish the selected stills as webp under wiki/assets/<source-page-slug>/.
---

# Stills: Three Questions Every Agent Engineer Should Be Able To Answer

Machine-read by `gemini-3.8-flash` (static processing) on 2026-10-11. **Unverified**: view each PNG and correct the reading before it reaches the wiki.

## 01 · [1:02] Did it fail?

- Kind: slide
- On screen: 0:49–1:03 · still taken at 1:02
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/01-01m02-did-it-fail.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=62s

On-screen content (machine-read):

```text
LANGCHAIN LABS
01 Did it fail?
```

Adds vs. narration (machine-read): Introduces the first core question an agent engineer must answer.

## 02 · [1:20] Can we make it fail again?

- Kind: slide
- On screen: 1:04–1:21 · still taken at 1:20
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/02-01m20-can-we-make-it-fail-again.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=80s

On-screen content (machine-read):

```text
LANGCHAIN LABS
01 Did it fail?
02 Can we make it fail again?
```

Adds vs. narration (machine-read): Adds the second core question on reproducibility of failures.

## 03 · [1:29] What changes make it stop failing?

- Kind: slide
- On screen: 1:22–1:30 · still taken at 1:29
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/03-01m29-what-changes-make-it-stop-failing.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=89s

On-screen content (machine-read):

```text
LANGCHAIN LABS
01 Did it fail?
02 Can we make it fail again?
03 What changes make it stop failing?
```

Adds vs. narration (machine-read): Adds the third core question on remediating agent failures.

## 04 · [1:44] Mining Production Traces

- Kind: diagram
- On screen: 1:31–1:45 · still taken at 1:44
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/04-01m44-mining-production-traces.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=104s

On-screen content (machine-read):

```text
DID IT FAIL? | LANGCHAIN LABS
Mining Production Traces
my_agent (12,482 traces)
#0142 user -> agent -> tool | tool error
#0318 user -> agent -> tool | loop
#0641 user -> agent -> user | correction
#0526 user -> agent -> tool | unlabeled
EVALUATORS SCAN (run trace thread) -> Selected + labeled:
#0142 Tool failure
#0318 Loop
#0641 Perceived error
Search · cluster · promote to eval task
```

Adds vs. narration (machine-read): Shows how evaluators scan production traces to filter and label specific failure patterns (tool failure, loop, perceived error) to promote into eval tasks.

## 05 · [2:26] Mining Production Traces

- Kind: diagram
- On screen: 1:55–2:27 · still taken at 2:26
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/05-02m26-mining-production-traces.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=146s

On-screen content (machine-read):

```text
DID IT FAIL? | LANGCHAIN LABS
Mining Production Traces
my_agent (12,482 traces)
#0142 user -> agent -> tool | tool error
#0318 user -> agent -> tool | loop
#0641 user -> agent -> user | correction
#0526 user -> agent -> tool | unlabeled
EVALUATORS SCAN (run trace thread) -> Selected + labeled:
#0142 Tool failure
#0318 Loop
#0641 Perceived error
Search · cluster · promote to eval task
```

Adds vs. narration (machine-read): Shows the production trace mining and categorization pipeline in full view.

## 06 · [3:06] Example: Perceived Error

- Kind: diagram
- On screen: 2:41–3:07 · still taken at 3:06
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/06-03m06-example-perceived-error.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=186s

On-screen content (machine-read):

```text
DID IT FAIL? | LANGCHAIN LABS
Example: Perceived Error
USER: Asks the agent to complete a task.
AGENT: Returns a plausible response.
USER: No — check the account history first, flag the renewal risk, then draft the reply. [Evidence about the earlier response appears later in the thread.]
EVIDENCE: Explicit or inferred
OUTPUT: Label + explanation
JUDGE: Specialized model trained on labeled conversational traces
SIGNALS ACROSS THE THREAD:
Correction · repeated request · rejected action · contradiction · acknowledged mistake · unresolved outcome
```

Adds vs. narration (machine-read): Details how user correction signals indicate perceived errors and how a specialized judge model evaluates conversational traces.

## 07 · [4:50] Reproducing Agent Failures

- Kind: diagram
- On screen: 4:10–4:51 · still taken at 4:50
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/07-04m50-reproducing-agent-failures.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=290s

On-screen content (machine-read):

```text
CAN WE MAKE IT FAIL AGAIN? | LANGCHAIN LABS
Reproducing Agent Failures
Input-output evaluation:
Input -> Output -> Score
Environment-backed evaluation:
Initial state | Tools | Permissions
TRAJECTORY + STATE TRANSITIONS:
[State transition step points across trajectory] -> Final state -> Score
Context, tool semantics, permissions, and state changes may all be part of the failure being reproduced.
```

Adds vs. narration (machine-read): Contrasts basic input-output evaluation with environment-backed evaluation tracking initial state, tools, permissions, and trajectory state transitions.

## 08 · [6:15] World Spec + Task Spec

- Kind: diagram
- On screen: 5:29–6:16 · still taken at 6:15
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/08-06m15-world-spec-task-spec.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=375s

On-screen content (machine-read):

```text
CAN WE MAKE IT FAIL AGAIN? | LANGCHAIN LABS
World Spec + Task Spec
World spec (SHARED ACROSS TASKS):
- Tools + APIs
- Domain rules
- Prompts + skills
- Shared graders
Task spec (ONE ATTEMPT):
- User request
- Initial state
- Expected outcome
- Allowed actions
World spec + Task spec -> Runnable environment + task
Leakage: Task reveals a shortcut.
Difficulty: Generated tasks are too easy.
Reward: Grader rewards the wrong behavior.
```

Adds vs. narration (machine-read): Breaks down World Spec vs. Task Spec components and outlines failure points in benchmark creation (leakage, difficulty, reward gaming).

## 09 · [8:39] World Spec + Task Spec

- Kind: diagram
- On screen: 8:33–8:40 · still taken at 8:39
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/09-08m39-world-spec-task-spec.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=519s

On-screen content (machine-read):

```text
CAN WE MAKE IT FAIL AGAIN? | LANGCHAIN LABS
World Spec + Task Spec
World spec (SHARED ACROSS TASKS):
- Tools + APIs
- Domain rules
- Prompts + skills
- Shared graders
Task spec (ONE ATTEMPT):
- User request
- Initial state
- Expected outcome
- Allowed actions
World spec + Task spec -> Runnable environment + task
Leakage: Task reveals a shortcut.
Difficulty: Generated tasks are too easy.
Reward: Grader rewards the wrong behavior.
```

Adds vs. narration (machine-read): Re-displays World Spec and Task Spec components.

## 10 · [9:13] Turning Production Data into Tasks

- Kind: diagram
- On screen: 8:41–9:14 · still taken at 9:13
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/10-09m13-turning-production-data-into-tasks.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=553s

On-screen content (machine-read):

```text
CAN WE MAKE IT FAIL AGAIN? | LANGCHAIN LABS
Turning Production Data into Tasks
Frontier labs can acquire: Demonstrations · trajectories · preference labels · verifiers · expert review
Application teams observe: Real workflows · domain state · permissions and constraints · corrections · edge cases
SELECTED BEHAVIOR:
Task candidates
01 Specify the task (Request · initial state · expected outcome) -> 02 Build environment + grader (Tools · permissions · state · success criteria) -> 03 Run repeated attempts (Compare trajectories, outcomes, and variance)
QUALITY GATES: Deduplicate -> Remove leakage -> Calibrate difficulty -> Human review
```

Adds vs. narration (machine-read): Contrasts the data advantages of frontier labs vs application teams, and defines the pipeline and quality gates to convert production data into benchmark tasks.

## 11 · [12:21] A Fix Has to Beat the Same Failure

- Kind: diagram
- On screen: 11:11–12:22 · still taken at 12:21
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/11-12m21-a-fix-has-to-beat-the-same-failure.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=741s

On-screen content (machine-read):

```text
WHAT CHANGES MAKE IT STOP FAILING? | LANGCHAIN LABS
A Fix Has to Beat the Same Failure
STARTING POINT: Reproduced failure (Same task, Same environment)
HARNESS CHANGE: Change the system around the model:
- Tool schemas
- Context
- Prompts
- State or memory representation
- Routing + control flow
- Model selection
MODEL / WEIGHT CHANGE: Change the policy itself:
- SFT / distillation (Strong demonstrations or target trajectories)
- RL (A reliable reward or verifier)
VALIDATION: Rerun the same task:
- Repeated trials
- Held-out variants
- Regression tasks
```

Adds vs. narration (machine-read): Structures failure remediation into harness changes vs. model policy changes, followed by validation steps.

## 12 · [13:34] Re-evaluating After a Harness or Model Change

- Kind: diagram
- On screen: 12:39–13:35 · still taken at 13:34
- File: `../images/three-questions-every-agent-engineer-should-be-able-to-answer/12-13m34-re-evaluating-after-a-harness-or-model-change.png`
- At this moment: https://www.youtube.com/watch?v=oVKGKdIAgtg&t=814s

On-screen content (machine-read):

```text
CARRY THE LEARNING FORWARD | LANGCHAIN LABS
Re-evaluating After a Harness or Model Change
Harness change OR Model change -> Existing tasks + environments
- Known failures: Which are fixed, and which are still present?
- Regressions: What previously worked but now fails?
- Harness still required?: Which prompts, tools, context, routing, or model choices can be removed or simplified?
New production behavior updates the task and environment set.
```

Adds vs. narration (machine-read): Details the continuous learning loop, outlining questions to ask (known failures, regressions, harness necessity) upon updating models or harnesses.

## Skipped

- [03:19–03:31] Example: Perceived Error: same picture as still 06
- [06:47–07:46] World Spec + Task Spec: same picture as still 08
