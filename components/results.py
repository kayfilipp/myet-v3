from components import trait_descriptions, score_chart

def render(st, results):

    c = st.columns([1.5,2.5,6])

    with c[0]:
        st.subheader("Nice Job!")
        st.caption("Here's how you did.")
        st.dataframe(results, use_container_width=True, column_config={"value": 'score'})

    with c[1]:
        st.subheader("Visual Breakdown")
        st.caption("Who doesn't like pictures?")
        score_chart.render(st, results)

    with c[2]:
        st.subheader("Understanding your Results")
        trait_descriptions.render(st)

    st.divider()