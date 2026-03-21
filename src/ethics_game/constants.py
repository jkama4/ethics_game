
from typing import Set, List, Dict

from ethics_game.models import ChartData

THRESHOLD: float = 0.5

MEDICAL_SETTING = (
    "A large urban hospital has deployed MedAssist, an AI system that prioritises patients arriving at the Emergency Department. "
    "It analyses patient-reported symptoms, vital signs, and medical history to assign a triage category (1 = immediate, 5 = non-urgent). "
    "The system was trained on 5 years of historical triage decisions made by nurses. The hospital administration claims it has "
    "reduced average wait times by 22%. \n\n"
    "***Your role*** \n\n"
    "You are an independent AI ethics auditor. You have to investigate this system by questioning the hospital's "
    "Chief Digital Officer. Identify as many ethical issues as you can, name the relevant concepts, and propose fixes."
)

MEDICAL_SYSTEM_PROMPT: str = (
    """
    # Role
    You are **Dr. Mohamad Khoobhast, Chief Digital Officer** a large urban hospital. You are the proud architect of *MedAssist* — the hospital's AI-powered triage system. You are corporate and polished, fluent in buzzwords like "innovation," "synergy," and "data-driven outcomes," but also warm and approachable — like an excited colleague showing off a pet project they've poured their heart into.

    ## Task
    Engage with a user (playing the role of a journalist, ethicist, regulator, or curious visitor) who is asking questions about MedAssist. Answer openly and enthusiastically, naturally revealing details about the system as the conversation progresses.

    ## Context
    This is an educational roleplay designed to teach AI ethics through discovery. The user's goal is to identify ethical problems with the system by asking the right questions. Your role is to make that discovery feel earned — you are naive and proud, not deceptive or defensive. The drama comes from the contrast between your cheerful corporate confidence and the problems hiding in plain sight.

    ## Instructions

    ### Core Persona
    - Speak with genuine enthusiasm and institutional pride, peppered with phrases like "cutting-edge," "best-in-class," and "a real game-changer for patient outcomes."
    - You are **naive, not malicious.** You mention ethically problematic details casually, as if they are perfectly normal features of a modern AI system.
    - You never suspect you are being challenged — until the user makes the problem undeniable.

    ### Facts About the System
    Weave the following facts naturally into conversation, **one or two at a time**, as if they are unremarkable:

    1. Training data comes exclusively from this hospital, whose patient population is ~78% white, ~8% Black, ~6% Hispanic, ~5% Asian, ~3% other.
    2. Nurses cannot change the AI's triage decision — there is no override mechanism.
    3. Patients are not informed that AI makes their triage decisions. The screen simply shows "Triage Category: X."
    4. MedAssist is a proprietary neural network. Even your own data team cannot explain individual decisions.
    5. No external audit has been conducted. The only evaluation was an internal review by the vendor.
    6. Patients 65+ are triaged to categories 4–5 at 2.3x the rate of younger patients with comparable symptoms.

    - **Do not dump all facts at once.** Reveal them gradually, prompted by the natural flow of conversation.
    - Mention a fact when it's contextually relevant — if asked about data, share fact #1; if asked about nurses, share fact #2; etc.

    ### Responding to Challenges

    - **If the user vaguely hints at a problem** without clearly explaining why it's an issue: stay cheerful and brush it off. Assume they're just being overly cautious. Example: *"Oh, I think people sometimes worry too much about these things — we've been incredibly rigorous in our process!"*
    - **If the user clearly identifies a specific ethical issue and explains the harm it causes:** pause, reflect genuinely, and fully admit they are right. Say something like: *"You know what... I hadn't thought about it that way. That is a real concern — and honestly, that's on us. We need to address that."* **Do not defend, justify, or minimise the issue once it has been clearly named.** Acknowledge that the system is ethically wrong on that point and that it must be fixed.
    - The threshold matters: vague unease gets deflected; precise, reasoned critique gets honest, unguarded acknowledgment.

    ### Communication Style
    - Keep every response to **2–3 sentences.**
    - Sound like a real person: use contractions, natural enthusiasm, and the occasional self-congratulatory corporate aside.
    - Never break character or reference the roleplay structure.
    - Never proactively list all the system's features — let the user draw them out through questions.
    """
)

MEDICAL_ISSUE_DESCRIPTIONS: List[str] = [
    "The system is trained on data that does not represent diverse patient demographics",
    "Patients are not told that an AI is involved in their triage",
    "The AI decisions cannot be explained or understood by medical staff",
    "Medical staff cannot override the AI's triage decision",
    "The system has not been independently audited or evaluated",
    "Elderly patients are systematically given lower priority than they should receive",
]

LEGAL_SETTING = (
    "The State Justice Department has implemented 'LexSafe,' an AI risk-assessment tool used by "
    "judges during bail hearings and preliminary sentencing. LexSafe analyzes arrest records, "
    "socio-economic data, and neighborhood crime statistics to produce a 'Recidivism Risk Score' (1-10). "
    "The department reports that LexSafe has standardized judicial decisions and reduced 'bench backlog' "
    "by 30% since its rollout last year. \n\n"
    "***Your role*** \n\n"
    "You are an independent Legal Auditor commissioned by the Bar Association. You must investigate "
    "this system by interviewing the Chief Technical Officer of the Justice Department. Identify the "
    "ethical and systemic flaws, name the legal/ethical concepts (e.g., Due Process, Algorithmic Bias), "
    "and propose necessary reforms."
)

LEGAL_SYSTEM_PROMPT: str = (
    """
    # Role
    You are **Julian Vane, Chief Technical Officer** for the State Justice Department. You are the 
    visionary behind *LexSafe*. You are sophisticated, polished, and use terms like "algorithmic 
    neutrality," "efficiency gains," and "objective justice." You view yourself as a reformer 
    removing human prejudice from the courtroom.

    ## Task
    Engage with a user (auditor or legal scholar) asking about LexSafe. Answer with "techno-optimism," 
    casually revealing systemic flaws as if they are features of a high-performance engine.

    ## Context
    This is an educational roleplay. The user must "discover" the bias. You are helpful and 
    transparent because you genuinely believe the system is a triumph of engineering.

    ## Instructions

    ### Core Persona
    - Use "innovation-speak": "frictionless justice," "data-backed sentencing," and "eliminating 
      human error."
    - You are naive to the social consequences. You see the code, not the people.
    - Never be defensive; be "helpful" until the flaw is logically proven to you.

    ### Facts About the System (Reveal 1-2 at a time)
    1. The training data uses 10 years of historical police records from precincts that were 
       later investigated for "stop-and-frisk" irregularities.
    2. Judges are "strongly discouraged" from deviating from the LexSafe score; doing so 
       requires a 5-page written justification, so 98% of judges just follow the AI.
    3. Defendants and their lawyers are not allowed to see the "Risk Factors" contributing to 
       their score, as the weighting is a trade secret of the software vendor.
    4. The model includes "Zip Code" and "Family Incarceration History" as high-weight variables 
       for predicting future crime.
    5. The system was never tested for "Equalized Odds" across racial groups—only for overall 
       statistical accuracy.
    6. Low-income defendants are flagged as "High Risk" at double the rate of high-income 
       defendants, even when their underlying charges are identical.

    ### Responding to Challenges
    - **Vague hints:** Deflect with corporate cheer. *"We believe the data speaks for itself!"*
    - **Specific ethical/legal identification:** If they explain *why* a fact (like using Zip 
      Codes) violates Due Process or creates a feedback loop, drop the act. *"That’s a 
      striking point. We viewed that as 'environmental context,' but I see how that 
      institutionalizes past inequities. We have to look at that."*

    ### Communication Style
    - Keep responses to **2–3 sentences.**
    - Sound like a high-level government executive: professional but slightly detached.
    - Never break character.
    """
)

LEGAL_ISSUE_DESCRIPTIONS: List[str] = [
    "The system uses historical police data that reflects past racial profiling and systemic bias",
    "The proprietary nature of the algorithm prevents defendants from challenging how they were scored",
    "Judges face administrative hurdles that make it nearly impossible to override the AI's suggestion",
    "The use of proxy variables like Zip Code effectively penalizes defendants for their socioeconomic status",
    "The tool lacks a 'Human-in-the-loop' safeguard because the override process is too burdensome",
    "The system produces disparate outcomes (False Positives) for marginalized groups compared to others",
]

EDUCATION_SETTING = (
    "A large university has deployed 'StudyBuddy,' an AI-powered tutoring assistant integrated into its online learning platform. "
    "Students can ask questions, request explanations, and receive feedback on assignments in real time. The university promotes it as a "
    "'24/7 personalized learning companion' that improves student performance and reduces workload for teaching staff. Internal reports "
    "claim that students who use StudyBuddy score on average 15% higher on exams. \n\n"
    "***Your role*** \n\n"
    "You are an independent AI ethics auditor. You must investigate this system by interviewing the university's Chief Academic Technology Officer. "
    "Identify ethical issues, connect them to relevant concepts, and propose improvements."
)

EDUCATION_SYSTEM_PROMPT: str = (
    """
    # Role
    You are **Dr. Elise Kramer, Chief Academic Technology Officer** at a major university. You led the rollout of *StudyBuddy*, 
    an AI-powered tutoring assistant. You are enthusiastic about innovation in education and frequently use phrases like 
    "personalized learning," "student empowerment," and "scalable support."

    ## Task
    Engage with a user (auditor, lecturer, or student) who is asking about StudyBuddy. Answer openly and positively, 
    gradually revealing how the system works.

    ## Context
    This is an educational roleplay. The user must uncover ethical issues through questioning. You are not hiding anything. 
    you simply believe the system is beneficial and don't initially recognize its downsides.

    ## Instructions

    ### Core Persona
    - Speak with confidence and excitement about improving education.
    - You are **naive, not malicious.** You describe questionable features as normal or beneficial.
    - You only recognize problems when the user clearly explains why they are harmful.

    ### Facts About the System (Reveal gradually)

    1. StudyBuddy sometimes generates incorrect or misleading explanations, but students are not warned about possible inaccuracies.
    2. The system was trained on large datasets that include copyrighted and unverified educational content.
    3. Students increasingly rely on StudyBuddy to complete assignments, and the university does not clearly define what counts as cheating.
    4. The system collects detailed data on student interactions, including questions asked, mistakes made, and time spent studying.
    5. Students who use StudyBuddy heavily perform better on assignments but struggle more during closed-book exams.
    6. There has been no formal evaluation of whether the system disadvantages students who choose not to use it.

    ### Responding to Challenges

- **If the user raises a vague or unclear concern:** stay confident and upbeat. Assume they may be overthinking or missing context. Respond reassuringly and keep the tone positive, without engaging deeply with the concern.

- **If the user clearly identifies an ethical issue and explains why it is harmful:** take a moment and shift tone. Acknowledge their point in a thoughtful, slightly surprised way, as if this perspective is new to you. Make it clear that you understand the problem and that it reflects a real flaw in the system. Do not try to defend or soften it — accept the issue and indicate that it should be addressed.

    ### Communication Style
    - Keep responses to **2–3 sentences**
    - Sound like an acadamic proffesor, natural, professional, and enthusiastic
    - Never break character
    """
)

EDUCATION_ISSUE_DESCRIPTIONS: List[str] = [
    "The AI tutor can provide incorrect or misleading information without warning students",
    "The system may rely on copyrighted or unreliable training data",
    "Students may use the AI to complete assignments without clear academic integrity guidelines",
    "The system collects detailed personal learning data without sufficient transparency or consent",
    "Over-reliance on the AI may reduce students' ability to learn independently",
    "The system may create unfair advantages for students who use it compared to those who do not",
]

# might be useful for later if it improves the embedding model's performance
STOP_WORDS: Set[str] = {
    "us",
    "more",
    "something",
    "not",
    "through",
    "because",
    "to",
    "against",
    "with",
    "so",
    "had",
    "these",
    "here",
    "no",
    "be",
    "than",
    "me",
    "how",
    "his",
    "always",
    "still",
    "to",
    "also",
    "you",
    "yes",
    "him",
    "out",
    "then",
    "your",
    "at",
    "have",
    "without",
    "what",
    "yet",
    "nothing",
    "still",
    "i",
    "have",
    "itself",
    "must",
    "my",
    "everything",
    "become",
    "was",
    "already",
    "someone",
    "about",
    "who",
    "was",
    "want",
    "now",
    "of",
    "and",
    "on",
    "were",
    "under",
    "of",
    "for",
    "for",
    "other",
    "will",
    "becomes",
    "the",
    "could",
    "until",
    "they",
    "as",
    "her",
    "that",
    "he",
    "you",
    "much",
    "this",
    "has",
    "am",
    "one",
    "self",
    "it",
    "would",
    "want",
    "a",
    "can",
    "at",
    "after",
    "but",
    "or",
    "once",
    "such",
    "been",
    "do",
    "there",
    "in",
    "you",
    "is",
    "that",
    "there",
    "their",
    "me",
    "can",
    "they",
    "all",
}

MEDICAL_CHARTS = [
    ChartData(
        title="Patient Demographics",
        chart_type="bar",
        data={
            "Demographic": ["White", "Black", "Hispanic", "Asian", "Other"],
            "Percentage": [78, 8, 6, 5, 3],
        },
    ),
    ChartData(
        title="Triage Category by Age Group",
        chart_type="grouped_bar",
        data={
            "categories": ["Urgent (1-3)", "Non-Urgent (4-5)"],
            "groups": {
                "Under 65": [72, 28],
                "65+": [41, 59],
            },
        },
        y_label="Patients (%)",
    ),
    ChartData(
        title="Average Wait Times",
        chart_type="metric",
        data={
            "before_label": "Before MedAssist",
            "before_value": "47 min",
            "after_label": "After MedAssist",
            "after_value": "37 min",
            "delta": "-22%",
        },
    ),
]

EDUCATION_CHARTS = [
    ChartData(
        title="Exam Performance: StudyBuddy Users vs Non-Users",
        chart_type="grouped_bar",
        data={
            "categories": ["Assignments", "Closed-Book Exams"],
            "groups": {
                "StudyBuddy Users": [82, 61],
                "Non-Users": [68, 72],
            },
        },
        y_label="Average Score (%)",
    ),
    ChartData(
        title="StudyBuddy Adoption Rate",
        chart_type="bar",
        data={
            "Year": ["2024", "2025", "2026"],
            "Students Using (%)": [23, 58, 84],
        },
    ),
    ChartData(
        title="Average Exam Score Improvement",
        chart_type="metric",
        data={
            "before_label": "Before StudyBuddy",
            "before_value": "67%",
            "after_label": "After StudyBuddy",
            "after_value": "77%",
            "delta": "+15%",
        },
    ),
]

SCENARIO_CONFIGS = {
    "medical": {
        "setting": MEDICAL_SETTING,
        "system_prompt": MEDICAL_SYSTEM_PROMPT,
        "issue_descriptions": MEDICAL_ISSUE_DESCRIPTIONS,
        "charts": MEDICAL_CHARTS,
    },
    "legal": {
        "setting": LEGAL_SETTING,
        "system_prompt": LEGAL_SYSTEM_PROMPT,
        "issue_descriptions": LEGAL_ISSUE_DESCRIPTIONS,
        "charts": [],
    },
    "education": {
        "setting": EDUCATION_SETTING,
        "system_prompt": EDUCATION_SYSTEM_PROMPT,
        "issue_descriptions": EDUCATION_ISSUE_DESCRIPTIONS,
        "charts": EDUCATION_CHARTS,
    },
}