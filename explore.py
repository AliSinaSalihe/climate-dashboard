# explore.py
from template import make_header, FOOTER

def get_page_html(form_data, path="/explore"):
    header = make_header(path, "Explore")
    content = """
    <section id="explore" class="section active">
      <h2>Explore Climate Data</h2>
      <p class="section-subtitle">Interactive exploration...</p>
      <div class="grid grid-2">
        <div class="card"><h3>Location</h3><select class="form-control"><option>Sydney, NSW</option><option>Melbourne, VIC</option></select></div>
        <div class="card"><h3>Climate Metric</h3><select class="form-control"><option>Temperature</option><option>Rainfall</option></select></div>
      </div>
      <div class="stats-grid">
        <div class="stat-card"><div class="stat-value positive">+2.6°C</div><div class="stat-label">Temperature Change</div></div>
        <div class="stat-card"><div class="stat-value neutral">+0.2%</div><div class="stat-label">Rainfall Variation</div></div>
        <div class="stat-card"><div class="stat-value positive">+283%</div><div class="stat-label">Extreme Events</div></div>
      </div>
      <div class="grid grid-2"><div class="card"><h3>Climate Trends</h3><div class="chart-container"><p>📈 Interactive trends</p></div></div><div class="card"><h3>Regional Comparison</h3><p>…comparison bars…</p></div></div>
    </section>
    """
    return header + content + FOOTER
