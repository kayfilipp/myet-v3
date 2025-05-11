import streamlit 

def render(st: streamlit, scores: dict):
    # Convert dictionary to JavaScript-friendly format
    labels = list(scores.keys())
    values = list(scores.values())

    # HTML & JavaScript for Chart.js with reduced top padding
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            .chart-container {{
                width: 500px;  
                height: 500px; 
                display: flex;
                justify-content: left;
                align-items: left;
            }}
            canvas {{
                width: 350px !important;  
                height: 350px !important; 
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
                        backgroundColor: "rgba(77, 25, 138,0.8)",
                        borderColor: "rgba(148, 0, 211, 1)",
                        borderWidth: 2,
                        pointBackgroundColor: "rgba(148, 0, 211, 0.1)"
                    }}]
                }},
                options: {{
                    responsive: false,  
                    maintainAspectRatio: false,  
                    layout: {{
                        padding: {{
                            bottom: 40,  
                            left: 40,  
                            right: 40  
                        }}
                    }},
                    plugins: {{
                        legend: {{
                            display: false  
                        }}
                    }},
                    scales: {{
                        r: {{
                            suggestedMin: 0,
                            suggestedMax: 5,
                            grid: {{
                                color: "rgb(200,200,200)"  
                            }},
                            angleLines: {{
                                color: "rgb(150,150,150)"  
                            }},
                            ticks: {{
                                display: false  
                            }},
                            pointLabels: {{
                                color: "white"  
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
    st.components.v1.html(html_code, height=550, width=550)  # Increase iframe size