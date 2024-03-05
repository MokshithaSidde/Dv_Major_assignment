import pandas as pd

# Read CSV file
data = pd.read_csv("https://raw.githubusercontent.com/MokshithaSidde/Dv_Major_assignment/main/data_sam.csv")

# Calculate the ActualCost
data['ActualCost'] = data['RawMaterial'] + data['Workmanship'] + data['StorageCost']

# Calculate the SoldPrice
data['SoldPrice'] = data['EstimatedCost'] * 1.1

# Calculate the MarginOfProfit
data['MarginOfProfit'] = data['SoldPrice'] - data['ActualCost']

# Reorder the columns
data = data[['date', 'EstimatedCost', 'RawMaterial', 'Workmanship', 'StorageCost', 'ActualCost', 'SoldPrice', 'MarginOfProfit']]

# Export as HTML file
data.to_html('data_sam.html', index=False)

# HTML code with added structure and styling
html_code_template = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Supply Chain</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>

<body>
    {table_rows}
</body>

</html>
'''

# Insert the table rows into the HTML code template
html_code = html_code_template.format(table_rows=data.to_html(index=False))

# Write the complete HTML code to a file
with open('data_sam.html', 'w') as file:
    file.write(html_code)
