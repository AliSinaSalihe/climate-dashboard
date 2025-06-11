# template.py

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="/style.css">
  <script src="/script.js" defer></script>
</head>
<body>
  <header class="header">
    <div class="logo">PROVIDE Climate Risk Dashboard</div>
    <nav class="nav">
      <a class="nav-item {home_active}" href="/">Dashboard</a>
      <a class="nav-item {explore_active}" href="/explore">Explore</a>
      <a class="nav-item {forecast_active}" href="/forecast">Forecasts</a>
      <a class="nav-item {historical_active}" href="/historical">Historical Data</a>
      <a class="nav-item {alerts_active}" href="/alerts">Alerts</a>
      <a class="nav-item {page6_active}" href="/page6">Similarity</a>
    </nav>
  </header>
  <main class="container">
"""

FOOTER = """
  </main>
</body>
</html>
"""

def make_header(path, title):
    return HEADER.format(
      title=title,
      home_active    = "active" if path=="/" else "",
      explore_active = "active" if path=="/explore" else "",
      forecast_active= "active" if path=="/forecast" else "",
      historical_active="active" if path=="/historical" else "",
      alerts_active  = "active" if path=="/alerts" else "",
      page6_active   = "active" if path=="/page6" else ""
    )
