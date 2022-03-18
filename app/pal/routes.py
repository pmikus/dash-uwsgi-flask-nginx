"""Routes for parent Flask app.
"""

from flask import current_app as app
from flask import render_template


@app.route(u"/")
def home():
    """Landing page.
    """

    return render_template(
        u"index.jinja2",
        title=u"Title",
        description=u"Description",
        template=u"home-template"
    )
