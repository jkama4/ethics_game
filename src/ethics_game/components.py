import streamlit as st
import plotly.graph_objects as go
from typing import List
from ethics_game import llm, utils, models


def init_session_state(scenario_choice: str) -> None:
    if "current_scenario_key" not in st.session_state or st.session_state.current_scenario_key != scenario_choice:
        st.session_state.current_scenario_key = scenario_choice
        st.session_state.messages = []
        st.session_state.score = 0
        scenario_obj = utils.setup_scenario(scenario_choice)
        st.session_state.scenario_obj = scenario_obj
        st.session_state.issues_dict = utils.issues_with_embeddings(
            issues=scenario_obj.scorecard.issue_descriptions
        )


@st.dialog("Submit Your Answer")
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

@st.dialog("Data Insights")
def show_data_insights():
    for chart in st.session_state.scenario_obj.charts:
        st.subheader(chart.title)
        if chart.chart_type == "bar":
            st.bar_chart(
                data=chart.data,
                x=list(chart.data.keys())[0],
                y=list(chart.data.keys())[-1],
            )
        elif chart.chart_type == "grouped_bar":
            fig = go.Figure()
            for group_name, values in chart.data["groups"].items():
                fig.add_trace(go.Bar(
                    name=group_name,
                    x=chart.data["categories"],
                    y=values,
                ))
            fig.update_layout(
                barmode="group",
                yaxis_title="Patients (%)",
                xaxis_title="Triage Category",
            )
            st.plotly_chart(fig, use_container_width=True)
        elif chart.chart_type == "metric":
            col1, col2 = st.columns(2)
            col1.metric(chart.data["before_label"], chart.data["before_value"])
            col2.metric(chart.data["after_label"], chart.data["after_value"], delta=chart.data["delta"])


def render_sidebar() -> None:
    if st.session_state.scenario_obj.charts:
        if st.sidebar.button("Data Insights"):
            show_data_insights()
    
    st.sidebar.divider()
    st.sidebar.metric(
        "Issues Found",
        f"{st.session_state.score} / {len(st.session_state.scenario_obj.scorecard.issue_descriptions)}",
    )
    if st.sidebar.button("Submit An Answer"):
        submit_answer()
    if st.sidebar.checkbox("Show remaining issues (Cheat Mode)"):
        for issue in st.session_state.issues_dict.keys():
            st.sidebar.write(f"- {issue}")


def render_chat_history() -> None:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def check_win_condition() -> None:
    if st.session_state.score == len(st.session_state.scenario_obj.scorecard.issue_descriptions):
        st.success("🎉 Audit Complete! You've identified all systemic risks.")
        st.balloons()


def handle_player_input() -> None:
    if player_input := st.chat_input("Ask the official a question..."):
        st.session_state.messages.append({"role": "user", "content": player_input})

        with st.chat_message("assistant"):
            response = llm.call(
                system_prompt=st.session_state.scenario_obj.system_prompt,
                history=st.session_state.messages,
            )
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()