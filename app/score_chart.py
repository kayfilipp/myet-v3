import streamlit 


def render(st: streamlit, scores: dict):

    _html = f"""
    <head>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <canvas id="spiderChart"></canvas>

        <script>
            const scores = {scores};

            const labels = Object.keys(scores);
            const values = Object.values(scores);

            const ctx = document.getElementById("spiderChart").getContext("2d");
            const spiderChart = new Chart(ctx, {{
                type: "radar",
                data: {{
                    labels: labels,
                    datasets: [{{
                        label: "Personality Traits",
                        data: values,
                        backgroundColor: "rgba(0, 123, 255, 0.2)",
                        borderColor: "rgba(0, 123, 255, 1)",
                        borderWidth: 2
                    }}]
                }},
                options: {{
                    scales: {{
                        r: {{
                            suggestedMin: 0,
                            suggestedMax: 5
                        }}
                    }}
                }}
            }});
        </script>
    </body>

    """

    st.markdown(_html, unsafe_allow_html=True)