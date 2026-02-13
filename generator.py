import csv
import os

# --- STEP 1: INITIALIZE DATA ---
total_revenue = 0
total_customers = 0
total_deals = 0
avg_revenue = 0
rows_data = []
table_html = ""

# --- STEP 2: DATA PROCESSING ---
if not os.path.exists('sales_data.csv'):
    print("❌ ERROR: 'sales_data.csv' not found!")
else:
    with open('sales_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_revenue += int(row['revenue'])
            total_customers += int(row['customers'])
            total_deals += int(row['deals_closed'])
            rows_data.append(row)

    if rows_data:
        avg_revenue = total_revenue / len(rows_data)

    # Build the Table Rows
    for row in rows_data:
        table_html += f"""
        <tr>
            <td>{row['month']}</td>
            <td style="font-weight: bold;">${int(row['revenue']):,}</td>
            <td>{row['customers']}</td>
            <td>{row['deals_closed']}</td>
        </tr>"""

# --- STEP 3: THE HTML (Fixed Triple Quotes) ---
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Sales Analytics Dashboard</title>
    <style>
        body {{
            font-family: 'Inter', -apple-system, sans-serif;
            background-color: #eef2f7; 
            margin: 0;
            padding: 60px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        h1 {{ color: #2d3436; margin-bottom: 40px; font-weight: 800; }}
        .dashboard {{ display: flex; gap: 25px; margin-bottom: 50px; width: 100%; max-width: 900px; }}
        .card {{
            background: white;
            padding: 30px 20px;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            flex: 1;
            text-align: center;
            border: 1px solid #dcdde1;
            transition: all 0.3s ease;
        }}
        .card:hover {{
            transform: scale(1.08);
            box-shadow: 0 20px 35px rgba(0,0,0,0.1);
            border-color: #3498db;
        }}
        .card h3 {{ margin: 0; font-size: 12px; color: #636e72; text-transform: uppercase; }}
        .card p {{ margin: 15px 0 0; font-size: 28px; font-weight: 900; color: #2f3640; }}
        table {{
            width: 100%;
            max-width: 900px;
            background: white;
            border-collapse: separate;
            border-spacing: 0;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            border: 1px solid #dcdde1;
        }}
        th {{ background-color: #2f3640; color: white; padding: 18px; text-align: left; }}
        td {{ padding: 16px 18px; border-bottom: 1px solid #f1f2f6; transition: 0.2s; }}
        tr:hover td {{ background-color: #f5f6fa; color: #3498db; }}
    </style>
</head>
<body>
    <h1>📊 Sales Analytics</h1>
    <div class="dashboard">
        <div class="card"><h3>Total Revenue</h3><p>${total_revenue:,}</p></div>
        <div class="card"><h3>Monthly Avg</h3><p>${avg_revenue:,.0f}</p></div>
        <div class="card"><h3>Customers</h3><p>{total_customers}</p></div>
        <div class="card"><h3>Deals</h3><p>{total_deals}</p></div>
    </div>
    <table>
        <thead><tr><th>MONTH</th><th>REVENUE</th><th>CUSTOMERS</th><th>DEALS</th></tr></thead>
        <tbody>
            {table_html}
        </tbody>
    </table>
</body>
</html>
"""

# Write the file
with open('report.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Success! Open 'report.html' now.")