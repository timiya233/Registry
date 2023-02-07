import json
import os

# Read docs/index.json
with open('docs/index.json') as f:
    index = json.load(f)

# Generate items
with open('docs/_sidebar.md', 'a') as f_sidebar:
    for item in index['index']:
        # Only process 
        f_sidebar.write(f'- [{item}](/{item}.md)\n')
        with open(f'docs/{item}.md', 'w') as f:
            repo_user = index['index'][item]['repository'].split('/')[1]
            repo_name = index['index'][item]['repository'].split('/')[2]
            tooth_user = index['index'][item]['tooth'].split('/')[1]
            tooth_name = index['index'][item]['tooth'].split('/')[2]

            f.write(f"# {index['index'][item]['name']}\n\n")

            f.write(f"![GitHub tag (latest SemVer)](https://img.shields.io/github/v/release/{tooth_user}/{tooth_name}?label=VERSION&style=for-the-badge)")
            f.write("&emsp;")
            f.write(f"![GitHub Release Date](https://img.shields.io/github/release-date/{tooth_user}/{tooth_name}?label=PUBLISHED&style=for-the-badge)")
            f.write("&emsp;")
            if index['index'][item]['license'] != '':
                license_name = index['index'][item]['license'].replace('-', '--').replace('+', '%2B')
                f.write(f"![License](https://img.shields.io/badge/license-{license_name}-orange?style=for-the-badge)")
            else:
                f.write(f"![Copyright](https://img.shields.io/badge/copyright-{index['index'][item]['author']}-orange?style=for-the-badge)")



            f.write(f"\n\n")

            f.write(f"```shell\n")
            f.write(f"lip install {item}\n")
            f.write(f"```\n\n")

            f.write(f"{index['index'][item]['description']}\n\n")

            f.write(f"> Author:&emsp;[{index['index'][item]['author']}](https://github.com/{index['index'][item]['author']})\n")
            f.write(f">\n")
            f.write(f"> Homepage:&emsp;[{index['index'][item]['homepage']}]({index['index'][item]['homepage']})\n")
            f.write(f">\n")
            f.write(f"> Repository:&emsp;[{index['index'][item]['repository']}](https://{index['index'][item]['repository']})\n\n")

            f.write(f"---\n\n")
            
            if os.path.exists(f'readmes/{item}.md'):
                with open(f'readmes/{item}.md') as f_readme:
                    readme = f_readme.read()
                    f.write(f"{readme}\n")