# dashboard.py
from template import make_header, FOOTER

def get_page_html(form_data, path="/"):
    header = make_header(path, "Dashboard")
    content = """
    <section id="dashboard" class="section active">
      <div class="hero">
        <div class="hero-content">
          <h1>A database for global-to-local climate impacts</h1>
          <p>Your trusted source for climate trends across Australia…</p>
        </div>
      </div>
      <div class="grid grid-2" style="margin-top:2rem;">
        <div class="card"><h3>📅 Data Range</h3><p>…from <strong>Jan 1910</strong> to <strong>Dec 2023</strong>.</p></div>
        <div class="card"><h3>❄️ Coldest Station</h3><p><strong>-8.5°C</strong> at <strong>Charlotte Pass, NSW</strong>.</p></div>
        <div class="card"><h3>🌧️ Wettest Station</h3><p><strong>Tully Sugar Mill, QLD</strong> recorded the highest rainfall at <strong>800 mm</strong> in a single day.</p></div>
        <div class="card"><h3>📍 Most Monitored Region</h3><p><strong>New South Wales</strong> has the most active stations.</p></div>
      </div>
    </section>
    """
    return header + content + FOOTER
