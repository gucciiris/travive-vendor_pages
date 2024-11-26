import os
import json
from jinja2 import Environment, FileSystemLoader

# Load the template
env = Environment(loader=FileSystemLoader('/Users/ngocmai/Documents/TRAVIVE/generating_pages/project/templates/'))
template = env.get_template('page_template.html')

# Load data from JSON
with open('/Users/ngocmai/Documents/TRAVIVE/generating_pages/project/data/pages_data.json') as f:
    pages_data = json.load(f)

# Output directory for generated HTML
output_dir = '/Users/ngocmai/Documents/TRAVIVE/generating_pages/project/output'
os.makedirs(output_dir, exist_ok=True)

# Generate pages
for page in pages_data:
    output_path = os.path.join(output_dir, page['filename'])
    with open(output_path, 'w') as f:
        html_content = template.render(title=page['title'], content=page['content'])
        f.write(html_content)
        print(f"Generated: {output_path}")
