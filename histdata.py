# histdata.py
from template import make_header, FOOTER

def get_page_html(form_data, path="/historical"):
    header = make_header(path, "Historical Data")
    content = """
    <section id="historical" class="section active">
      <h2>Historical Climate Data</h2>
      <div class="card"><h3>Select Location</h3><select class="form-control"><option>Sydney</option><option>Melbourne</option></select></div>
      <div class="card" style="margin-top:1rem;"><h3>Analysis</h3><div class="chart-container"><p>📈 Trends (2015–2024)</p></div></div>
    </section>
    """
    return header + content + FOOTER
