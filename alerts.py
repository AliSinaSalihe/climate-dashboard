# alerts.py
from template import make_header, FOOTER

def get_page_html(form_data, path="/alerts"):
    header = make_header(path, "Alerts")
    content = """
    <section id="alerts" class="section active">
      <h2>Emergency Alerts</h2>
      <div class="alert alert-danger"><div>🔥 Fire Warning – Sydney</div><div>28/05/2025</div></div>
      <div class="alert alert-warning"><div>⛈️ Severe Weather – Sydney</div><div>28/05/2025</div></div>
    </section>
    """
    return header + content + FOOTER
