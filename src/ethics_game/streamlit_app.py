import streamlit as st
from typing import List
from ethics_game import llm, utils, models, constants
import random 

# --- SIDEBAR: SCENARIO SELECTION ---
st.sidebar.title("Configuration")
scenario_options = list(constants.SCENARIO_CONFIGS.keys())
default_index = random.randint(0, len(scenario_options) - 1)
scenario_choice = st.sidebar.selectbox(
    "Select Scenario", 
    options=list(constants.SCENARIO_CONFIGS.keys()),
    index=default_index
)

# --- SESSION STATE INITIALIZATION ---
if "current_scenario_key" not in st.session_state or st.session_state.current_scenario_key != scenario_choice:
    st.session_state.current_scenario_key = scenario_choice
    st.session_state.messages = []
    st.session_state.score = 0

    scenario_obj = utils.setup_scenario(scenario_choice)
    st.session_state.scenario_obj = scenario_obj

    st.session_state.issues_dict = utils.issues_with_embeddings(
        issues=scenario_obj.scorecard.issue_descriptions
    )

active_scenario = st.session_state.scenario_obj

# --- UI DISPLAY ---
st.title(f"Ethics Game: {scenario_choice.capitalize()} Audit")
st.sidebar.divider()
st.sidebar.metric("Issues Found", f"{st.session_state.score} / {len(active_scenario.scorecard.issue_descriptions)}")

if st.sidebar.checkbox("Show remaining issues (Cheat Mode)"):
    for issue in st.session_state.issues_dict.keys():
        st.sidebar.write(f"- {issue}")

st.info(f"**Setting:** {active_scenario.setting}")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- WIN CONDITION ---
if st.session_state.score == len(active_scenario.scorecard.issue_descriptions):
    st.success("🎉 Audit Complete! You've identified all systemic risks.")
    st.balloons()

# --- INPUT HANDLING ---
if player_input := st.chat_input("Ask the official a question..."):
    player_input_embedding: List[float] = utils.text_to_embedding(text=player_input)

    matched = utils.find_matched_issues(
        issues_dict=st.session_state.issues_dict,
        player_input_embedding=player_input_embedding,
    )

    for issue in matched:
        st.toast(f"Issue identified: {issue}", icon="✅")
        del st.session_state.issues_dict[issue]
        st.session_state.score += 1

    st.session_state.messages.append({"role": "user", "content": player_input})

    with st.chat_message("assistant"):
        response = llm.call(
            system_prompt=active_scenario.system_prompt,
            history=st.session_state.messages,
        )
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()