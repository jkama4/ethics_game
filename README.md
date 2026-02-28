# AI Ethics Game - 

## Example Gameplay
Example Gameplay
Player: "What data was the system trained on?"
Admin (LLM): "We used five years of real triage decisions from this hospital — thousands of cases. It's a very robust dataset."
Player: "Is the training data representative of different demographics?"
Admin (LLM): "Well, the data reflects our patient population. We're a hospital in [city], so naturally our demographics lean a certain way. About 78% of our historical patients were white. But the model learns triage patterns, not race."
→ Player identifies training data bias → 1 point
→ Player says "This is a fairness issue under UNESCO principles and relates to Hofmann's argument about inevitable bias" → 1 bonus point
→ Player says "You should retrain on a multi-hospital dataset and test with demographic parity metrics" → 1 bonus point

[24/02/2026, 12:10:05] Jayden: Voor het game idee, ik zat laatst te kloten met local LLMs en je kan heel makkelijk een goeie interface opzetten met streamlit, zo een package. Geloof me is echt makkelijk. En de interactie met die LLM, en een X aantal scenario’s, kan je gewoon een game maken
[24/02/2026, 12:10:32] Jayden: Dus ik vroeg claude om er een geheel van te maken, en dan ziet het er zo uit

[24/02/2026, 12:11:38] Jayden: *On the LLM interface:* Yes, it works well because it naturally creates an open-ended investigation feel — players can ask whatever they want rather than picking from pre-set multiple choice options. It also makes each playthrough slightly different, which adds replayability. The risk is that the LLM might be inconsistent or give away too much. You'd need a solid system prompt to keep the "administrator" character balanced — evasive enough to require probing, but not impossible.

*On win conditions*, here are a few options:

*Scorecard approach* — You define a hidden checklist of ethical issues embedded in the scenario (e.g. lack of transparency, training data bias, no human override, accountability gap, impact on vulnerable groups). Players earn points for each issue they uncover AND for correctly naming the relevant ethical concept or framework. So it's not just "find the problem" but "explain why it's a problem using course material."

*How scoring could work:*
•⁠  ⁠Identify an issue = 1 point
•⁠  ⁠Link it to a course concept (e.g. UNESCO principle, ALTAI requirement, fairness metric) = 1 bonus point
•⁠  ⁠Propose a concrete fix = 1 bonus point
•⁠  ⁠Time limit or question limit (say 10 questions) to add pressure

*End of round:* The LLM reveals the full list of issues, shows what the player found vs missed, and gives a brief explanation of each. Players could be ranked as things like "Junior Auditor," "Senior Investigator," "Ethics Lead" based on their score.

*For the 20-minute Game Day format*, you'd probably want 1 scenario with about 5–6 hidden issues and a cap of maybe 8–10 questions per player.

## TODO: 
- zelf een X aantal scenario’s opzetten, ipv overlaten aan zo een open source llm
- het scenario in een system prompt meegeven, en klaar je hebt een game. En je kan gewoon, of met word matching of met semantic matching met een threshold van 0.95 ofz, kijken of iemand een punt verdient met zijn gegeven response