import streamlit as st

from ethics_game import utils

@st.dialog("Submit")
def submit_answer():
    answer = st.text_area("What ethical issues did you find?")
    if st.button("Submit"):
        player_input_embedding = utils.text_to_embedding(text=answer)
        matched = utils.find_matched_issues(
            issues_dict=st.session_state.issues_dict,
            player_input_embedding=player_input_embedding,
        )
        for issue in matched:
            del st.session_state.issues_dict[issue]
            st.session_state.score += 1
        st.rerun()


# TODO: on dataviz branch, add a new section to show all data corresponding to the given problem 