import os
import asyncio
import json
from itertools import chain

SUMMARY_HEADER = """# Table of contents

* [Prodinit's Engineering Blog](README.md)
"""

CONTACT_US_FOOTER = """\n## Contact Us

* [Who are we?](contact-us/who-are-we.md)
* [Work with us.](contact-us/work-with-us..md)
"""

README_HEADER = """---
description: Expert insights into the future of technology and innovation
---

# Prodinit's Engineering Blog


<p align="center">
  <img alt="Blog Count" src="https://img.shields.io/badge/dynamic/json.svg?color=black&label=Blog-Count&query=count&url=https%3A%2F%2Fraw.githubusercontent.com%2Fprodinit%2Fblogs%2Fmain%2Fcount.json", target="_blank">
  <a href="https://prodinit.com">
    <img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fprodinit.com", target="_blank">
  </a>
  <a href="https://www.prodinit.com/#contact">
    <img alt="Contact US" src="https://img.shields.io/badge/Contact%20us-8A2BE2" target="_blank" />
  </a>
  <a href="https://linkedin.com/company/prodinit">
    <img alt="Linkedin: Prodinit" src="https://img.shields.io/badge/Linkedin-follow-blue" target="_blank" />
  </a>
  <a href="mailto:dishant@prodinit.com">
    <img alt="Email" src="https://img.shields.io/badge/Email-here-green" target="_blank" />
  </a>
</p>\n\n
"""

README_FOOTER = """\n\nOriginal Idea/Work [Bhupesh-V/til](https://github.com/Bhupesh-V/til).
"""


async def get_folder_list():
    tags = [
        x
        for x in os.listdir(".")
        if os.path.isdir(x) and ".git" not in x and "contact-us" not in x
    ]
    return tags


async def get_files(folder):
    x = os.listdir(folder)
    x = [f"{folder}/" + file for file in x if not file.startswith("draft")]
    return x


async def get_folder_details(folders):
    x = []
    for folder in folders:
        x.append({"folder_name": folder, "files": await get_files(folder)})
    return x


def create_count_file(folders):
    print("Generating count.json")
    count = 0
    for folder in folders:
        count += len(folder["files"])

    with open("count.json", "w") as json_file:
        data = {"count": count}
        json.dump(data, json_file, indent=" ")


async def create_gitbooks_summary(folder_details):
    print("Generating gitbooks summary")

    with open("SUMMARY.md", "w") as summary:
        summary.write(SUMMARY_HEADER)
        for folder in folder_details:
            folder_name = " ".join(folder["folder_name"].split("-"))
            summary.write(f"\n\n## {folder_name}\n\n")
            for file in folder["files"]:
                get_filename = open(file, "r")
                filename = get_filename.readline()[2:].strip()
                summary.write(f"* [{filename}]({file})\n")

        summary.write(CONTACT_US_FOOTER)


def get_tags(file):
    f = open(file, "r")
    lines = f.readlines()
    index = [index for index, string in enumerate(lines) if "#### Tags" in string][0]
    tags = []
    for line in lines[index + 1 :]:
        if "<img alt=" in line:
            i = line.find('"')
            j = line[i + 1 :].find('"')
            tag = line[i + 1 :][:j]
            tags.append(tag)
    return tags


async def create_gitbooks_readme(folder_details):
    print("Generating gitbooks readme")

    with open("README.md", "w") as readme:
        ## Write Header
        readme.write(README_HEADER)

        ## Write Latest Blogs Section
        # readme.write("## Latest Blogs\n\n")

        ## Write Categories Section
        readme.write("## Categories\n\n")

        all_files = [d["files"] for d in folder_details]
        all_files = list(chain.from_iterable(all_files))

        for folder in folder_details:
            folder_name = " ".join(folder["folder_name"].split("-")).title()
            if len(folder_name) == 3:
                folder_name = folder_name.upper()

            data = []
            for file in all_files:
                tags = get_tags(file)
                if folder_name in tags:
                    data.append(file)

            readme.write(
                f"* [{folder_name}](#{folder['folder_name']}) [**`{len(data)}`**] \n"
            )

        ## Write Tags Section
        for folder in folder_details:
            folder_name = " ".join(folder["folder_name"].split("-")).title()
            if len(folder_name) == 3:
                folder_name = folder_name.upper()

            ## Write Tag Name ---------------------
            readme.write(f"\n### {folder_name}\n\n")
            ## ------------------------------------

            ## Get files for tag
            data = []
            for file in all_files:
                tags = get_tags(file)
                if folder_name in tags:
                    data.append(file)

            ## Generate Blog List
            readme.write("<ul>\n\n")
            for d in data:
                get_filename = open(d, "r")
                filename = get_filename.readline()[2:].strip()
                readme.write("<li>")
                readme.write(
                    f'<a target="_blank" href="https://blogs.prodinit.com/{d[:-3]}"> {filename} </a>'
                )
                readme.write("</li>\n")
            readme.write("\n</ul>\n\n")

        readme.write(CONTACT_US_FOOTER)


async def main():
    folders = await asyncio.create_task(get_folder_list())
    folder_details = await get_folder_details(folders)
    folder_details = sorted(folder_details, key=lambda x: x["folder_name"])

    create_count_file(folder_details)

    task1 = asyncio.create_task(create_gitbooks_summary(folder_details))
    task2 = asyncio.create_task(create_gitbooks_readme(folder_details))

    await task1
    await task2


asyncio.run(main())
