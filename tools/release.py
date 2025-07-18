import sys
import json
from pathlib import Path
import subprocess as cmd
from datetime import datetime
import converter.foundry as foundry
import converter
import converter.util as util


def get_active_branch_name():
    head_dir = Path(".") / ".git" / "HEAD"
    with head_dir.open("r") as f: content = f.read().splitlines()
    for line in content:
        if line[0:4] == "ref:":
            return line.partition("refs/heads/")[2]


if not get_active_branch_name() == "master":
    print("aborting, not on 'master' branch")
    sys.exit(1)

# Update the manifest
for pack_name, pack_def in foundry.packs.items():
    if (util.BUILD / pack_name).exists():
        foundry.module_definition["packs"].append(pack_def)

with (util.PROJECT / "module.json").open("w", encoding="utf-8") as fp:
    json.dump(foundry.module_definition, fp, indent=2, ensure_ascii=False)

tool_version = converter.__version__

# date of the data
data_date = (Path(__file__).parent.parent / "p5e-data" / "VERSION").read_text()

# Converting the date to Eu standard from US, which is then appended to the tool version
# This makes up the package version
date = datetime.strptime(data_date, "%m/%d/%Y").strftime("%y%m%d")
module_version = f"{tool_version}.{date}"

# Save the VERSION
with (Path(".") / "VERSION").open('w') as fp:
    fp.write(module_version)

# Add the module json and a tag, push them both
cmd.run("git add VERSION")
cmd.run("git add module.json")
cmd.run(f'git commit -m "Update manifest to {module_version}"')
cmd.run(f'git tag -a v{module_version} -m "Release of {module_version}"')
cmd.run("git push origin master")
cmd.run(f'git push origin v{module_version}')

# Note: GitHub release creation requires a personal access token
# You can create one at: https://github.com/settings/tokens
# For now, we'll skip the automatic GitHub release creation
print(f"Version {module_version} has been tagged and pushed.")
print(f"To create a GitHub release, go to: https://github.com/Albydo/p5e-foundryVTT/releases/new")
print(f"Use tag: v{module_version}")
print(f"Upload the file: dist/pokemon5e.zip")

# Uncomment and modify the following lines if you have a GitHub token:
# token = Path("~/Documents/signing/TOKEN_VTT").expanduser().read_text()
# cmd.run(f'githubrelease --github-token {token} release Albydo/p5e-foundryVTT create v{module_version} --publish --name "v{module_version}" "dist/pokemon5e.zip"')

