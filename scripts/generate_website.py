import json

# Read docs/index.json
with open('docs/index.json') as f:
    index = json.load(f)

# Generate items
with open('docs/_sidebar.md', 'a') as f_sidebar:
    for item in index['index']:
        # Only process 
        f_sidebar.write(f'- [{item}](/{item}.md)\n')
        with open(f'docs/{item}.md', 'w') as f:
            f.write(f"# {index['index'][item]['name']}\n")
            f.write(f"\n")

            f.write(f"```shell\n")
            f.write(f"lip install {item}\n")
            f.write(f"```\n")
            f.write(f"\n")

            f.write(f"## Metadata\n")
            f.write(f"- Author: {index['index'][item]['author']}\n")
            f.write(f"- Homepage: <{index['index'][item]['homepage']}>\n")
            f.write(f"- License: {index['index'][item]['license']}\n")
            f.write(f"- Tooth Path: {index['index'][item]['tooth']}\n")
            f.write(f"\n")

            f.write(f"## Description\n")
            f.write(f"{index['index'][item]['description']}\n")
            f.write(f"\n")