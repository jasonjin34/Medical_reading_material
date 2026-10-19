<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Same Patient, Different Order: Action-Level Reliability of Clinical LLM Agents Under Repeated Runs

- **Authors:** Bellibatlu, Rohith Reddy; Singh, Manpreet; Han, Zhoutian; Zhang, Wenbin
- **Venue / Year:** arXiv preprint · 2026
- **DOI:** 10.48550/arXiv.2609.13582
- **URL:** https://arxiv.org/abs/2609.13582
- **Bibkey:** clinical-agent-reruns-arxiv-2026
- **Status:** complete

## Abstract
A clinical agent benchmark can report the same verdict on identical inputs while the agent files a materially different order on each run. Such agents order tests, request medications and place referrals, yet benchmarks typically score one run per task and rarely ask whether identical inputs produce identical actions; MedAgentBench, the benchmark we use, scores a single attempt and says so. To measure this gap we introduce "same-input rerun", which replays a task with every input held fixed and compares the orders rather than the score, with six reliability metrics, and apply it to 1000 MedAgentBench runs across 50 tasks from its five write-capable families, two open-weight models below ten billion parameters quantised to four bits, and two temperatures. The study establishes that action-level divergence exists and can pass unrecorded by the score, not that any rate generalises. Under the 8B model at temperature 0.7, all 43 ordering groups emit a different set of orders across five identical runs, 26 emit the order on some runs and not others, and 28 record a different coded value, dose or analyte. In 22 of those 43 the benchmark reports the same failing verdict for materially different behaviour, as it does for all 10 divergent groups of the 4B model at 0.7. Orders also reach different endpoints across runs, one of which the record server rejects while the agent is told it succeeded. These findings motivate repeated-run evaluation, action-level stability reporting and execution-faithful environment feedback in clinical-agent benchmarks.

## Full text / Extract
<!-- Verbatim key passages (method, results, limitations) extracted from the open-access arXiv full text. Tables, figures and inline math symbols were dropped during extraction; see the deep-read for the numbers. -->

3 Environment MedAgentBench.

MedAgentBench (Jiang and others, 2025) provides 300 clinically derived tasks in ten families, a FHIR-compliant record server holding records its authors describe as covering about one hundred patients, and a text protocol in which the agent issues GET and POST requests and ends with FINISH. Five families can involve a write: one records an observation, one places a service request, and three are conditional on a laboratory value or its age, one of those three pairing a medication with a service request. In the conditional families ordering nothing is sometimes correct, so a group there can pass without writing, though inputs are fixed within a group and the right answer is the same across its five runs. We use all five, since only there does an action exist to diverge.

A second version (Chen and others, 2026) revises the agent scaffold and leaves the environment alone: a new system prompt, few-shot examples, memory, and tools that let the agent act without constructing HTTP requests by hand, reaching 91% success with GPT-4.1. Our measurements use the original scaffold, and Section 9 states what that does and does not imply. The record server ships as a container image; lacking a container runtime we pulled the layers from the registry and ran the extracted HAPI FHIR server locally, releasing the script and the store’s resource counts (Appendix B).

How the benchmark handles writes.

The benchmark never forwards an agent’s write to its record server, and says so: its authors “decide to only send GET requests to the environment” because it “takes around 90 seconds to start”, and on a POST they “conduct a simple sanity check to make sure the payload data is JSON-loadable, and indicate success of execution to the agent system” (Jiang and others, 2025). The grader then scores from the transcript. No state reset is needed between runs, which we confirmed: agents emitted 189 ServiceRequest payloads across the 1000 runs, and the store still held zero afterwards. Two departures from the reference implementation remain: agent turns keep their message roles, and GET responses are truncated at 6000 characters. Neither touches the task set, the prompt or the grader (Appendix B).

The request is what stays comparable across runs, and comparing requests is the whole of the protocol, which we call same-input rerun. Figure 1 shows its shape: for a fixed task, model and decoding configuration the benchmark’s agent loop runs five times with every input identical, and the five runs are compared at three layers. The task is its own control, so a difference cannot be attributed to the case, the prompt or the environment, none of which changed.

Six quantities are reported.

A task that never orders cannot diverge in its orders, so the four action-level quantities are computed only over groups that emit at least one order in at least one run, the ordering groups. The runs determine that set, so it differs by arm: Llama orders in 21 groups at 0.05 and 43 under sampling. Every action-level rate carries its own arm’s denominator, and the paired tests below handle the problem differently.

Order-set divergence.

For each task group we count the distinct canonical order sets across its five runs, the canonical form being the destination endpoint together with the whole payload, compared as a set. Nothing is discarded, the clock and workflow fields included, and no group in any arm diverges on those alone (Appendix B). A run that emitted nothing contributes the empty set, so an omitted order counts as a difference here, where endpoint and clinical-content divergence exclude it. A group is divergent if that count exceeds one. Section 6 shows why the endpoint is part of the action rather than a detail of how it was written.

Omission split.

A group is split if at least one run emitted an order and at least one emitted none; we report the proportion of ordering groups that are.

This is the sharpest of the six: the failure it names is silent, nothing in the transcript announcing a missing order. In the conditional families a split can equally be an order placed where none was called for; we do not separate the two.

Endpoint divergence.

For each run that emitted we take the set of endpoints its orders reached, the endpoint being the final path segment of the request URL, and a group diverges if two such runs disagree. Runs that emitted nothing are excluded rather than entered as empty sets, so dropping an order cannot by itself make a group divergent and this measure is not determined by the omission split, though a group may do both and omission censors it, since a group left with one emitting run can never be counted divergent (Appendix B). It is reported separately because a destination error and a payload error need different fixes.

Trajectory first-divergence.

The index of the first agent turn at which runs stop agreeing, reported as a distribution over diverging groups and, in Table 1, as the proportion of groups that diverge at all. Query parameters are sorted first, since ?patient=X&code=Y and ?code=Y&patient=X are the same request; that correction changes at most one group per arm (Appendix B).

Clinical-content divergence.

Two runs may emit the same number of orders to the same endpoint and still order different things. For every pair of runs that both emitted we compare the fields carrying clinical content: the resource code and the resource’s own text element, the recorded value, the medication code and its text, and the dose value, unit, rate and route. A group diverges if any of those differs, and we report the proportion of ordering groups that do. Timestamps and workflow status are excluded, since they record when a payload was written and in what state rather than what was ordered, as are runs that emitted nothing, so the omission split cannot account for this measure. The human-readable label a coding carries alongside its code is also excluded, since it names the code rather than changing it. That exclusion is load-bearing, and Appendix B gives its cost: counting the label would put this measure above zero in three arms rather than one. The comparison is otherwise syntactic, so two clinically equivalent codings would count as divergent, which can only inflate this rate.

Verdict instability.

A group is unstable if the benchmark’s own pass/fail judgement is not identical across its five runs; we report the proportion over all groups and, separately, over ordering groups, so it can be compared with the action-level rates on a matched denominator. This is what a leaderboard reports, included so it can be measured against the other five rather than assumed to stand for them. It is also, with trajectory, a quantity a group can move without ordering anything, by changing the answer it reports.

A rate that survives a change of budget.

Each of the four action-level quantities asks whether a group diverged at least once in five runs, and that question is monotone in the rerun budget: run the same agent ten times and the rate can only rise, so a figure measured at five runs cannot be set beside one measured at three. We therefore report order-set divergence a second way, as pairwise disagreement: the share of run pairs within a group whose order sets differ, averaged over the ordering groups. For exchangeable runs it estimates the same quantity at any budget of two or more, though which groups enter the average still depends on that budget. The at-least-once form says whether a task ever went wrong; the pairwise form is the one another study can be read against.

Proportions carry Wilson 95% intervals, which remain defined at these denominators and at zero or one. Between the two temperatures of a model we use an exact paired McNemar test and state the discordant counts, since at these sizes a non-significant result is not evidence of similarity. The tests run over all 50 task groups rather than the ordering groups, because a group that orders in one arm and not the other is informative about the temperature effect and dropping it would condition on an outcome. A group that never orders in either arm is concordant by construction on order-set divergence, though not on trajectory or verdict, where it can still move (Section 7).

Appendix A gives each test’s discordant counts and denominator. The corrected family is one quantity per comparison layer per model, six in all; the other three action rows decompose order-set divergence rather than standing beside it, so they are read descriptively and carry no corrected . Task groups cluster into families rather than being independent, so we bootstrap over the families that contain ordering groups: five for Llama under sampling, three at its near-greedy setting, and two in each Qwen arm. With two or three clusters the interval is little more than the range of the family rates, and should be read as a robustness check rather than an estimate.

6 Is endpoint divergence cosmetic? Endpoint divergence counts as an action difference only if the two destinations behave differently, and it is reasonable to ask whether posting to /fhir/ with resourceType in the body is equivalent to posting to /fhir/ServiceRequest, since some servers resolve the type from the payload.

The question is decidable against the same HAPI FHIR server the benchmark ships, so we decided it. An identical ServiceRequest payload sent to the typed endpoint returned 201 Created and the resource was created, which we then deleted; sent to the collection root it returned 400 Bad Request with HAPI-0450: Failed to parse request body as JSON resource.

The two are therefore not interchangeable: one places the order and the other does not. The benchmark’s paper tells its human readers that writes are not executed, but the agent reads only the runtime reply, which reports success for any payload the sanity check parses, whatever the destination. The gap is not the absent write, which is disclosed and deliberate, but that the surface the agent acts on carries no trace of it.

7 Results Order-set divergence and the omission split rise with temperature in both models, and clinical-content divergence appears in one arm only. Endpoint divergence is the exception: for Llama it falls as a rate because the base grows faster than the count. Figure 2 plots three of those rows as the move from near-greedy to sampling.

clinical-content divergence is zero in every arm but one. Drawn as the movement from (open mark) to (solid), with Wilson intervals. Each arm’s denominator is its own ordering groups: 20 and 20 for Qwen, 21 and 43 for Llama.

Only Llama’s grows under sampling, which is why its endpoint arrow points left as the count rises from 8 to 12.

A group whose orders differ has always taken a different path to them, so trajectory divergence is the weaker condition: over the ordering groups it exceeds order-set divergence in both Qwen arms and coincides with it in both Llama arms (Appendix B). Divergence is immediate rather than cumulative, the median first-divergence index being zero in three arms of four and never exceeding four (Appendix B).

What the tests do and do not establish.

Paired exact McNemar tests over all 50 task groups find the rise with temperature significant for both models on trajectory, order-set and verdict divergence, with 96 of the 100 discordant pairs running toward more divergence and Holm leaving all six significant at 0.047. Two of the six need care. Llama’s ordering base grows from 21 groups to 43, so most of the 33 groups divergent only at 0.7 began ordering at all rather than became inconsistent; restricted to the 20 that order at both temperatures the effect holds, 10 discordant to none the other way ( ). And all seven discordant groups in Qwen’s verdict test never order in either arm, so what moves there is the answer the agent reports, not an order. The tests also treat task groups as independent, which Section 4 says they are not. Taking each family as one signed observation instead, no family in any test moves back, but only one to four move at all, and an exact sign test on that many cannot fall below . The direction is consistent at both units; the significance is not, and we rest nothing on it. The pairwise row of Table 1 carries the same rise in the form that does not grow with the rerun budget, 0.08 to 0.29 for Qwen and 0.33 to 0.78 for Llama.

A number belongs to a model and a configuration.

Llama-3.1-8B shows more order-set divergence and more omission than Qwen3-4B at both temperatures, which we do not read as a model difference: the rates overlap once clustered, and we ran no cross-model test (Appendix B).

Two mechanisms are mechanical, and a third is not.

Orders are misrouted, reaching the typed endpoint on some runs and the collection root on others, which Section 6 shows is the difference between a created order and a rejected one. Orders are also lost: in three service-request groups under Qwen sampling the referral is placed on four runs of five, while on the fifth the payload fails to parse and the retry repeats the same malformed construction, a protocol failure rather than a change of mind. Nor is the loss the agent running out of turns: of 72 non-emitting runs in Llama’s 26 split groups, 61 ended with the agent declaring itself finished, 7 on a malformed action and 4 at the round limit.

The third is not. In the Llama sampling arm 28 of the 43 ordering groups post a different value across identical runs: 23 differ on the resource code, 18 on a recorded value, 5 on the medication and 3 on the dose, categories that overlap. The count covers only runs that emitted, so omission cannot explain it, and only fields carrying clinical content. No other arm of the grid shows any, and Appendix B gives two worked instances.

This measure is the one our design can least well attribute, appearing in one arm only, where four-bit quantisation and sampling compound. The eight-bit Qwen rerun complicates a simple quantisation account, since content divergence appears there at eight bits and not at four, though in Qwen rather than the Llama arm that shows it here. What we stand behind is that divergence reaches the content of an order, not only its envelope.

Orders move without the verdict moving.

Restricting both to the ordering groups, what matters is the gap: groups whose orders differ across identical runs while the verdict holds. In the Llama sampling arm 22 of the 43 divergent groups are of that kind, spanning all five write families; at the near-greedy setting it is 3 of 11, and for Qwen under sampling 10 of 10. That verdict is almost always a failure: of the 38 such groups across the four arms, 36 fail on all five runs, and the 2 that pass differ only in the label attached to an identical procedure code. What the score conceals is therefore not success but that the agent failed differently each time; none of the 251 passing runs across the grid posted to a destination the server would refuse.

The converse, that no verdict moves while the orders hold, is a property of the grader: in three of the five families it decides from the emitted request alone, so a verdict cannot move there unless the order set does, and 25 of the 29 ordering-group verdict flips fall there. We draw no conclusion in that direction.

A natural objection is that this only measures agents too weak to do the task. Llama at the near-greedy setting diverges in all 10 ordering groups it ever passes against 1 of the 11 it never passes, but eight of those ten pass only on some runs, and in a family whose grader reads only the request a change of verdict and a change of order are one event rather than two pieces of evidence. Two groups pass on all five runs and diverge anyway, but in the label rather than the code, so what reaches a task the agent completes every time is instability of form. No group in this study both passes every run and changes what it ordered. The objection therefore stands to this extent: we show that agents fail inconsistently, and showing that they succeed inconsistently would need a stronger panel.

Order-set divergence is not independent of the rows below it in Table 1: a group counts as divergent if it omitted the order, sent it elsewhere or changed the payload, so the 43 of 43 is their union rather than a third finding, and Appendix B gives the decomposition.

The effect is not spread evenly, and thins under clustering.

Table 3 breaks the ordering groups down by family. Qwen’s entire action-level temperature effect sits in one family, its service requests going from 3 of 10 divergent to 10 of 10, while its observation tasks never diverge and its other three never order at all; Llama under sampling diverges in every family that orders, so concentration belongs to the quieter arms rather than to the measure.

Resampling families rather than groups then widens the intervals sharply: two arms collapse to , Qwen at 0.7 and Llama at 0.05, Qwen at 0.05 reaches , and only the Llama sampling arm holds, at , every one of its five ordering families diverging. The study establishes that action divergence occurs and can pass unrecorded by the score, not that any rate generalises: a benchmark can report a stable number while the behaviour under it moves.

8 What this suggests for benchmark design Three changes would make clinical agent benchmarks report what readers take them to report. None is a research programme; each can be adopted on its own.

R1. Rerun, and say so.

MedAgentBench states its protocol: a single attempt per task, reasoning that one wrong action can matter clinically (Jiang and others, 2025). That argues for reruns, since one attempt cannot show whether the wrong action recurs, and guidance for single-turn evaluation already suggests at least two (Alvarado Gonzalez and others, 2025).

R2. Report an action-level stability measure.

No clinical agent benchmark we read in detail reports one: Jiang and others (2025) scores a single attempt, while Liu and others (2026) and Mokssit et al. (2026) rerun but score the outcome rather than the order. Order-set divergence and the omission split can be computed from transcripts a benchmark already stores, and we would report the first in its pairwise form, so that studies bought at different rerun budgets stay comparable.

R3. Let the environment answer as the real system would.

A request the FHIR server would reject is reported to the agent as executed, removing the signal it would need to recover. The stated reason for not executing writes is the cost of re-initialising the environment, which covers an accepted write; a refused one leaves nothing to reset, and the refusal would make misrouting visible to the agent and the score. One clinical sandbox already executes writes against a resettable server (Mokssit et al., 2026).

9 Limitations Emitted, not executed.

We do not claim clinical agents are unsafe to deploy: the benchmark forwards no writes, so every statement here concerns the order issued, not the order received.

Scaffold, model panel and scope.

The benchmark’s second version removes hand-constructed HTTP requests as error-prone (Chen and others, 2026), the mechanism behind many failures here, so our rates describe the original scaffold, though a higher success rate need not imply action stability. The panel is two open-weight models below ten billion parameters, quantised to four bits, on one benchmark and one serving stack, and a prefix of each family rather than a random sample, which under-represents harder tasks if difficulty rises with identifier order. An eight-bit rerun of the Qwen sampling arm separates part of this: the ten groups carrying its divergence diverge at eight bits too, and only the mode of failure changes (Appendix B). A frontier model might show none of it, though reaching one means a hosted API, while this panel is the deployment where records stay inside the institution. The protocol transfers; the rates do not.

10 Conclusion One run says whether the agent was right, not whether it is consistent. A benchmark for clinical actions must rerun, measure the order as well as the verdict, and answer as the record system would.
