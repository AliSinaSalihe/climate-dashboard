# forecast.py
from template import make_header, FOOTER

def get_page_html(form_data, path="/forecast"):
    header = make_header(path, "Forecasts")
    content = """
    <section id="forecast" class="section active">
      <h2>Explore by Station</h2>
      <div class="grid grid-3">
        <div class="card"><h3>Select State</h3><select class="form-control"><option>NSW</option><option>VIC</option></select></div>
        <div class="card"><h3>Latitude Range</h3><input class="form-control" type="number"><input class="form-control" type="number"></div>
        <div class="card"><h3>Metric</h3><select class="form-control"><option value="MaxTemp">Max Temp</option><option value="Rainfall">Rainfall</option></select></div>
      </div>
      <button class="btn btn-primary" onclick="filterData()">Submit</button>
      <div class="card" style="margin-top:1.5rem;"><h3>Matches</h3><table class="data-table" data-sort-asc="true"><thead><tr><th onclick="sortTable(0)">Name</th><th onclick="sortTable(1)">Region</th><th onclick="sortTable(2)">Lat</th><th onclick="sortTable(3)">Value</th></tr></thead><tbody></tbody></table></div>
    </section>
    """
    return header + content + FOOTER
