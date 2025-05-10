import streamlit 


def render(st: streamlit, scores: dict):

    # Convert dictionary to JavaScript-friendly format
    labels = list(scores.keys())
    values = list(scores.values())

    # HTML & JavaScript for Chart.js with smaller size
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            canvas {{
                width: 300px !important;  /* Set smaller width */
                height: 300px !important; /* Set smaller height */
            }}
        </style>
    </head>
    <body>
        <canvas id="spiderChart"></canvas>
        <script>
            const ctx = document.getElementById("spiderChart").getContext("2d");
            const spiderChart = new Chart(ctx, {{
                type: "radar",
                data: {{
                    labels: {labels},
                    datasets: [{{
                        label: "Personality Traits",
                        data: {values},
                        backgroundColor: "rgba(0, 123, 255, 0.2)",
                        borderColor: "rgba(0, 123, 255, 1)",
                        borderWidth: 2
                    }}]
                }},
                options: {{
                    responsive: false,  // Prevent auto-resizing
                    maintainAspectRatio: false,  // Allow custom sizing
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
    </html>
    """

    # Embed the chart in Streamlit with a smaller height
    st.title("Personality Traits Radar Chart")
    st.components.v1.html(html_code, height=350)  # Reduce height