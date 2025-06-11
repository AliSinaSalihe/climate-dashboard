# page6.py
from template import make_header, FOOTER

def get_page_html(form_data, path="/page6"):
    header = make_header(path, "Similarity")
    content = """
    <section id="similarity-analysis" class="section active">
      <h2>Find Similar Stations</h2>
      <div class="grid grid-3"><div class="card"><h3>Period 1</h3><input class="form-control" placeholder="2005"><input class="form-control" placeholder="2009"></div><div class="card"><h3>Period 2</h3><input class="form-control" placeholder="2010"><input class="form-control" placeholder="2015"></div><div class="card"><h3>Reference</h3><select class="form-control"><option>Melbourne</option></select></div></div>
      <button class="btn btn-primary" onclick="submitSimilarityRequest()">Compare</button>
      <div class="card" style="margin-top:1rem;"><h3>Results</h3><table class="data-table" data-sort-asc="true"><thead><tr><th>Name</th><th>P1</th><th>P2</th><th>Δ%</th><th>RefDiff</th></tr></thead><tbody></tbody></table></div>
    </section>
    """
    return header + content + FOOTER
