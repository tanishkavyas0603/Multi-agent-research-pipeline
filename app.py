"""
Streamlit UI for the multi-agent research pipeline defined in pipeline.py

Run with:
    streamlit run app.py

Make sure pipeline.py (and agents.py) are in the same folder, or on PYTHONPATH.
"""

import streamlit as st
from datetime import datetime

from pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔎",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []  # list of {topic, state, timestamp}
if "current" not in st.session_state:
    st.session_state.current = None

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.title("🔎 Research Assistant")
    st.caption("Search → Read → Write → Critique")

    st.divider()
    st.subheader("History")
    if not st.session_state.history:
        st.caption("No past runs yet.")
    else:
        for i, run in enumerate(reversed(st.session_state.history)):
            idx = len(st.session_state.history) - 1 - i
            label = f"{run['topic'][:28]}{'…' if len(run['topic']) > 28 else ''}"
            if st.button(label, key=f"hist_{idx}", use_container_width=True):
                st.session_state.current = run

    st.divider()
    if st.button("🗑️ Clear history", use_container_width=True):
        st.session_state.history = []
        st.session_state.current = None
        st.rerun()

# ---------------------------------------------------------------------------
# Main area
# ---------------------------------------------------------------------------
st.title("Multi-Agent Research Pipeline")
st.write(
    "Enter a topic and let the search agent, reader agent, writer, and critic "
    "collaborate to produce a reviewed research report."
)

with st.form("topic_form"):
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Latest advances in solid-state batteries",
    )
    submitted = st.form_submit_button("Run pipeline", type="primary")

if submitted:
    if not topic or not topic.strip():
        st.warning("Please enter a topic before running the pipeline.")
    else:
        status = st.status("Starting pipeline…", expanded=True)
        try:
            status.write("**Step 1 — Search agent** is looking for recent, reliable sources…")
            status.write("**Step 2 — Reader agent** will scrape the most relevant result…")
            status.write("**Step 3 — Writer** will draft the report…")
            status.write("**Step 4 — Critic** will review the draft…")

            with st.spinner("Running all agents — this can take a minute…"):
                state = run_research_pipeline(topic.strip())

            status.update(label="Pipeline complete ✅", state="complete", expanded=False)

            run_record = {
                "topic": topic.strip(),
                "state": state,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            st.session_state.history.append(run_record)
            st.session_state.current = run_record

        except Exception as e:
            status.update(label="Pipeline failed ❌", state="error", expanded=True)
            st.error(f"Something went wrong while running the pipeline:\n\n{e}")

# ---------------------------------------------------------------------------
# Display results
# ---------------------------------------------------------------------------
if st.session_state.current:
    run = st.session_state.current
    state = run["state"]

    st.divider()
    st.subheader(f"Results for: {run['topic']}")
    st.caption(f"Run at {run['timestamp']}")

    tab_report, tab_feedback, tab_search, tab_scraped = st.tabs(
        ["📄 Report", "🧐 Critic Feedback", "🔍 Search Results", "📖 Scraped Content"]
    )

    with tab_report:
        report = state.get("report", "")
        st.markdown(report if isinstance(report, str) else str(report))
        st.download_button(
            "Download report as .md",
            data=report if isinstance(report, str) else str(report),
            file_name=f"{run['topic'].replace(' ', '_')}_report.md",
            mime="text/markdown",
        )

    with tab_feedback:
        feedback = state.get("feedback", "")
        st.markdown(feedback if isinstance(feedback, str) else str(feedback))

    with tab_search:
        st.text(state.get("search_results", "No search results captured."))

    with tab_scraped:
        st.text(state.get("scraped_content", "No scraped content captured."))
else:
    st.info("Run a topic above to see the search results, scraped content, report, and critic feedback here.")
