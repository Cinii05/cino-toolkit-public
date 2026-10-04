# Routing and precedence

This skill owns workflow-level automation diagnosis.

## Route to this skill when

The user asks to audit a business workflow for automation opportunities, decide which manual process to automate, map a current workflow and rank bottlenecks, judge whether an automation opportunity is justified before a solution exists, or define the smallest testable automation from raw operational evidence.

## Precedence with other Cino Toolkit skills

### cino-critical-review wins when
There is already a concrete plan, specification, vendor choice, claim, proposal, or implementation decision and the user mainly wants it challenged or second-opinioned.

### grill-me wins when
The user explicitly wants an interactive question-by-question interview or wants a plan/design developed conversationally.

### cino-product-design-review wins when
The target is website/app visual design, UX, accessibility, responsiveness, interaction states, or design-system quality.

### tmc-ui-master wins when
The target is The Moving Chain frontend/UI/UX work.

### cino-video-intelligence wins when
The primary task is to inspect, transcribe, fact-check, or extract evidence from video/social media.

### teach-programming-step-by-step wins when
The user primarily wants to learn how automation/code/tooling works rather than receive a business workflow audit.

### unslop wins when
The primary task is rewriting or humanising prose.

## Tie-break rule

Route by the user's immediate requested decision, not isolated keywords such as audit, automation, review, or AI.

If the request is “critique this automation plan,” use Critical Review.
If the request is “look at how this business works and tell me what is worth automating,” use Automation Opportunity Audit.

## Sequential composition

Some requests legitimately require more than one skill. Use the evidence-producing skill first, then this audit.

Example:
- A screen recording or social video showing a business workflow -> cino-video-intelligence extracts time-coded evidence first.
- The resulting workflow evidence -> cino-automation-opportunity-audit diagnoses bottlenecks and automation opportunities.

Do not treat a valid sequence as a routing collision.

## Verification boundary

Local routing fixtures are pre-install contract tests. They prove the written precedence table is internally consistent; they do not prove ChatGPT's installed router will activate the same skill. Before publication, install the candidate and run the same ambiguous prompts through the real skill-discovery/activation surface.
