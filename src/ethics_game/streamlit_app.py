import streamlit as st
from ethics_game.components import (
    init_session_state,
    render_sidebar,
    render_chat_history,
    check_win_condition,
    handle_player_input,
)

scenario_choice = st.sidebar.selectbox(
    "Select Scenario",
    options=["medical", "legal"],
    index=0,
)
init_session_state(scenario_choice)
render_sidebar()

st.title(f"Ethics Game: {scenario_choice.capitalize()} Audit")
st.info(f"**Setting:** {st.session_state.scenario_obj.setting}")

render_chat_history()
check_win_condition()
handle_player_input()