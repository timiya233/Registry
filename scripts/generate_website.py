import json
import os

# Read docs/index.json
with open('docs/index.json', encoding='utf-8') as f:
    index = json.load(f)

# Generate items
with open('docs/_sidebar.md', 'a', encoding='utf-8') as f_sidebar:
    for alias in index['index']:

        # Add to sidebar
        f_sidebar.write(f"- [{index['index'][alias]['name']}](/{alias}.md)\n")

        # Generate docs
        with open(f'docs/{alias}.md', 'w', encoding='utf-8') as f:
            item = index['index'][alias]

            f.write(f"# {item['name']}\n\n")

            tooth_user = item['tooth'].split('/')[1]
            tooth_name = item['tooth'].split('/')[2]

            f.write(f"![GitHub tag (latest SemVer)](https://img.shields.io/github/v/release/{tooth_user}/{tooth_name}?label=VERSION&style=for-the-badge)")
            f.write("&emsp;")

            f.write(f"![GitHub Release Date](https://img.shields.io/github/release-date/{tooth_user}/{tooth_name}?label=PUBLISHED&style=for-the-badge)")
            f.write("&emsp;")

            if item['license'] != '':
                license_name = item['license'].replace('-', '--').replace('+', '%2B')
                f.write(f"![License](https://img.shields.io/badge/license-{license_name}-orange?style=for-the-badge)")
            elif item['repository'] != '':
                repo_user = item['repository'].split('/')[1]
                repo_name = item['repository'].split('/')[2]
                f.write(f"![License](https://img.shields.io/github/license/{repo_user}/{repo_name}?color=orange&style=for-the-badge)")
            else:
                author_name = item['author'].replace('-', '--').replace('+', '%2B')
                f.write(f"![Copyright](https://img.shields.io/badge/copyright-{author_name}-orange?style=for-the-badge)")


            f.write(f"\n\n")

            f.write(f"```shell\n")
            f.write(f"lip install {alias}\n")
            f.write(f"```\n\n")

            f.write(f"{item['description']}\n\n")

            for tag in item['tags']:
                tag_type_dict = {
                    "reserved": [
                        "featured"
                    ],
                    "type": [
                        "utility",
                        "plugin",
                        "module",
                        "mod",
                        "modpack",
                        "addon",
                        "world",
                        "integration"
                    ],
                    "ecosystem": [
                        "ll",
                        "llse",
                        "llnet",
                        "bdsx",
                        "pnx",
                        "bds"
                    ]
                }

                color = "inactive"

                if tag in tag_type_dict['reserved']:
                    color = "important"
                elif tag in tag_type_dict['type']:
                    color = "blue"
                elif tag in tag_type_dict['ecosystem']:
                    color = "blueviolet"

                tag = tag.replace('-', '--')
                f.write(f"![{tag}](https://img.shields.io/badge/-{tag}-{color}?style=flat)")
                f.write("&nbsp;")

            f.write(f"\n\n")

            f.write(f"> Author:&emsp;[{item['author']}](https://github.com/{item['author']})\n")

            if item['homepage'] != '':
                f.write(f">\n")
                f.write(f"> Homepage:&emsp;[{item['homepage']}]({item['homepage']})\n")

            if item['repository'] != '':
                f.write(f">\n")
                f.write(f"> Repository:&emsp;[{item['repository']}](https://{item['repository']})\n")

            f.write(f"\n")

            f.write(f"---\n\n")
            
            if os.path.exists(f'readmes/{alias}.md'):
                with open(f'readmes/{alias}.md', encoding='utf-8') as f_readme:
                    readme = f_readme.read()
                    f.write(f"{readme}\n")
