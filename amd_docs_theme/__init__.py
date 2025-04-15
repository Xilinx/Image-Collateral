import os

def get_html_theme_path():
    """Return the HTML theme directory."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return cur_dir