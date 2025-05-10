import streamlit 


def render(st: streamlit, scores: dict):

    # Convert dictionary to JavaScript-friendly format
    labels = list(scores.keys())  # Assume scores is defined elsewhere
    values = list(scores.values())

    # HTML & JavaScript for Chart.js with scores as labels and no scale
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            canvas {{
                width: 300px !important;
                height: 300px !important;
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
                    labels: {labels}.map((label, index) => `${{label}}: ${{{values}[index]}}`), // Show scores in labels
                    datasets: [{{
                        label: "Personality Traits",
                        data: {values},
                        backgroundColor: "rgba(0, 123, 255, 0.2)",
                        borderColor: "rgba(0, 123, 255, 1)",
                        borderWidth: 2
                    }}]
                }},
                options: {{
                    responsive: false,
                    maintainAspectRatio: false,
                    scales: {{
                        r: {{
                            display: false // Hide the scale
                        }}
                    }}
                }}
            }});
        </script>
    </body>
    </html>
    """

    # Embed the chart in Streamlit
    st.title("Personality Traits Radar Chart")
    st.components.v1.html(html_code, height=350)