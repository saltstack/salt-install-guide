"""
Script to download Salt versions manifest and prep docs where version specific info is required
"""

from pathlib import Path
import json
import shutil
import requests

# Download and parse supported salt versions manifest
supported_versions_json = requests.get(
    "https://gitlab.com/saltstack/open/docs/salt-install-guide/-/snippets/2580440/raw/main/supported-versions.json"
)
supported_versions = supported_versions_json.json()
supported_major_versions = [
    full_version.split(".")[0]
    for full_version in supported_versions["supported_versions"]
]
supported_major_versions.sort(reverse=True)
supported_minor_versions = supported_versions["supported_versions"]
supported_minor_versions.sort(reverse=True)

# Assign vars
LATEST_MAJOR = supported_major_versions[0]
OLD_MAJOR = supported_major_versions[1]
LATEST_MINOR = supported_minor_versions[0]
OLD_MINOR = supported_minor_versions[1]
RC_RELEASE = supported_versions["release_candidate_version"]

# Check if three major versions of salt are currently supported
if len(supported_major_versions) > 2:
    THREE_VERSIONS = True
    OLDEST_MAJOR = supported_major_versions[2]
    OLDEST_MINOR = supported_minor_versions[2]
else:
    THREE_VERSIONS = False

# Prep template for modification
sitevars_template_file = Path("docs", "_templates", "sitevars.rst")
sitevars_updated_file = Path("docs", "sitevars.rst")
shutil.copyfile(sitevars_template_file, sitevars_updated_file)

# Update new sitevars file
with open(sitevars_updated_file, "r") as sitevars_updated_file_reader:
    sitevars_template = sitevars_updated_file_reader.read()
    sitevars_template_list = sitevars_template.splitlines()

# Find CURRENT* vars
for sitevars_line in sitevars_template_list:
    if "|current-major-version|" in sitevars_line:
        CURRENT_MAJOR = sitevars_line.split(" ")[-1]
        break
CURRENT_MINOR = None
for salt_minor_version in supported_minor_versions:
    if CURRENT_MAJOR in salt_minor_version:
        CURRENT_MINOR = salt_minor_version
        break

# Needed for testing new versions of salt
if CURRENT_MINOR == None:
    CURRENT_MINOR = f"{CURRENT_MAJOR}.0"

# Replace all var placeholders
sitevars_updated = (
    sitevars_template.replace("LATEST_MAJOR", LATEST_MAJOR)
    .replace("OLD_MAJOR", OLD_MAJOR)
    .replace("LATEST_MINOR", LATEST_MINOR)
    .replace("OLD_MINOR", OLD_MINOR)
    .replace("RC_RELEASE", RC_RELEASE)
    .replace("CURRENT_MAJOR", CURRENT_MAJOR)
    .replace("CURRENT_MINOR", CURRENT_MINOR)
)

if THREE_VERSIONS:
    sitevars_updated = sitevars_template.replace("OLDEST_MAJOR", OLDEST_MAJOR).replace(
        "OLDEST_MINOR", OLDEST_MINOR
    )

# Write dynamic sitevars file
with open(sitevars_updated_file, "w") as sitevars_updated_file_writer:
    sitevars_updated_file_writer.write(sitevars_updated)

# Write latest announcements file
latest_announcements = requests.get(
    "https://gitlab.com/saltstack/open/docs/salt-install-guide/-/snippets/3722105/raw/main/announcements.rst"
)
announcements_file = Path("docs", "topics", "announcements.rst")
with open(announcements_file, "w") as announcements_updated_file_writer:
    announcements_updated_file_writer.write(latest_announcements.text)
