import streamlit as st
from typing import List, Dict
from ethics_game import llm, utils, models

scenario: models.Scenario = utils.setup_scenario()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "score" not in st.session_state:
    st.session_state.score = 0
if "issues_dict" not in st.session_state:
    st.session_state.issues_dict = utils.issues_with_embeddings(
        issues=scenario.scorecard.issue_descriptions
    )

st.title("Ethics Game")
st.sidebar.metric("Score", f"{st.session_state.score} / {len(scenario.scorecard.issue_descriptions)}")
st.write(f"***Setting***\n\n{scenario.setting}")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.score == len(scenario.scorecard.issue_descriptions):
    st.success("You have found all issues!")

if player_input := st.chat_input("Ask a question..."):
    player_input_embedding: List[float] = utils.text_to_embedding(text=player_input)
    print(f"Player input: {player_input}")

    matched = utils.find_matched_issues(
        issues_dict=st.session_state.issues_dict,
        player_input_embedding=player_input_embedding,
    )

    for issue in matched:
        del st.session_state.issues_dict[issue]
        st.session_state.score += 1

    st.session_state.messages.append({"role": "user", "content": player_input})

    response = llm.call(
        system_prompt=scenario.system_prompt,
        history=st.session_state.messages,
    )
    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()