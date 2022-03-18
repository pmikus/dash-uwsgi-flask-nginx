"""Plotly Dash HTML layout override."""

html_layout = u"""
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body class="dash-template">
            <header>
              <div class="nav-wrapper">
                <a href="/">
                    <h1>Title</h1>
                </a>
                <a href="">
                  <h1>Report</h1>
                </a>
                <nav>
                </nav>
              </div>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
"""
