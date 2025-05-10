import streamlit 

def render(st: streamlit, scores: dict):
    # Convert dictionary to JavaScript-friendly format
    labels = list(scores.keys())
    values = list(scores.values())

    # HTML & JavaScript for Chart.js with larger canvas but same chart size
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            .chart-container {{
                width: 400px;  /* Increase canvas size */
                height: 400px; /* Increase canvas size */
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px; /* Add padding to prevent cropping */
            }}
            canvas {{
                width: 300px !important;  /* Keep chart size small */
                height: 300px !important; /* Keep chart size small */
            }}
        </style>
    </head>
    <body>
        <div class="chart-container">
            <canvas id="spiderChart"></canvas>
        </div>
        <script>
            const ctx = document.getElementById("spiderChart").getContext("2d");
            const spiderChart = new Chart(ctx, {{
                type: "radar",
                data: {{
                    labels: {labels},
                    datasets: [{{
                        label: "Score",
                        data: {values},
                        backgroundColor: "rgba(134, 94, 173, 0.2)",
                        borderColor: "rgba(134, 94, 173, 1)",
                        borderWidth: 2
                    }}]
                }},
                options: {{
                    responsive: false,  // Prevent auto-resizing
                    maintainAspectRatio: false,  // Allow custom sizing
                    plugins: {{
                        legend: {{
                            display: false  // Hide the legend
                        }}
                    }},
                    scales: {{
                        r: {{
                            suggestedMin: 0,
                            suggestedMax: 5,
                            ticks: {{
                                display: false  // Hide tick labels
                            }},
                            grid: {{
                                display: false  // Hide grid lines
                            }},
                            angleLines: {{
                                display: false  // Hide angle lines
                            }}
                        }}
                    }}
                }}
            }});
        </script>
    </body>
    </html>
    """

    # Embed the chart in Streamlit with a larger canvas
    st.title("Personality Traits Radar Chart")
    st.components.v1.html(html_code, height=450, width=450)  # Increase iframe size