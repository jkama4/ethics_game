import numpy as np

from langchain_huggingface import HuggingFaceEmbeddings

from typing import List, Tuple, Dict, Set

from ethics_game import models, constants

EMBEDDINGS = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

def text_to_embedding(
    text: str,
) -> Tuple[List[float]]:
    text = remove_stopwords(text=text)
    print(text)
    return EMBEDDINGS.embed_query(text=text)


def cosine_similarity(
    player_input_embedding: List[float], 
    issue_embedding: List[float],
) -> np.ndarray:
    dot: np.ndarray = np.dot(player_input_embedding, issue_embedding)
    return dot / (np.linalg.norm(player_input_embedding) * np.linalg.norm(issue_embedding))


# Load the selected scenario from the scenario configuration map, use medical as default
def setup_scenario(scenario_key: str = "medical") -> models.Scenario:
    config = constants.SCENARIO_CONFIGS.get(scenario_key, constants.SCENARIO_CONFIGS["medical"])
    setting = config["setting"]
    system_prompt = config["system_prompt"]
    scorecard = models.Scorecard(
        issue_descriptions=config["issue_descriptions"]
    )
    charts = config.get("charts", [])
    return models.Scenario(
        setting=setting,
        system_prompt=system_prompt,
        scorecard=scorecard,
        charts=charts,
    )

def issues_with_embeddings(
    issues: List[str]
) -> Dict[str, List[float]]:
    
    issues_dict: Dict[str, List[float]] = dict()

    for issue in issues:
        emb: List[float] = text_to_embedding(text=issue)
        issues_dict[issue] = emb

    return issues_dict


def find_matched_issues(
    issues_dict: Dict[str, List[float]],
    player_input_embedding: List[float],
) -> List[str]:

    matched = []
    for issue, emb in issues_dict.items():
        cos_similarity = cosine_similarity(
            player_input_embedding=player_input_embedding,
            issue_embedding=emb,
        )
        print(f"Cosine Similarity: {cos_similarity}")

        if cos_similarity >= constants.THRESHOLD:
            matched.append(issue)

    return matched


def remove_stopwords(
    text: str,
) -> str:
    
    words: List[str] = text.split()
    keywords: Set[str] = set()

    for word in words:
        if word not in constants.STOP_WORDS:
            keywords.add(word)

    return " ".join(list(keywords))