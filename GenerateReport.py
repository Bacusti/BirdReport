from datetime import datetime, timezone

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bird Report</title>
</head>
<body>
    <h1>Bird Report</h1>
    <p>Last updated: {timestamp}</p>
</body>
</html>"""

with open("report.html", "w") as f:
    f.write(html)

print(f"Report generated at {timestamp}")
