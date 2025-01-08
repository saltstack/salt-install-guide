"""
Script to download Salt versions manifest and prep docs where version specific info is required
"""

from pathlib import Path
import json
import shutil

# Parse supported salt versions manifest
supported_versions_json = Path("tools", "supported-versions.json")
with open(supported_versions_json, "r") as supported_versions_json_reader:
    supported_versions = json.load(supported_versions_json_reader)
supported_minor_versions = list(supported_versions["versions"].keys())
supported_major_versions = [
    version_entry.split(".")[0] for version_entry in supported_minor_versions
]
supported_major_versions.sort(reverse=True)
supported_minor_versions.sort(reverse=True)

# Discover default install version
non_default = []
for supported_minor_version in supported_minor_versions:
    if supported_versions["versions"][supported_minor_version]["default"]:
        default_version = supported_minor_version
    else:
        non_default.append(supported_minor_version)

# Assign vars
LATEST_MAJOR = supported_major_versions[0]
ONE_MAJOR = default_version.split(".")[0]
TWO_MAJOR = non_default[0].split(".")[0]
LATEST_MINOR = supported_minor_versions[0]
ONE_MINOR = default_version
TWO_MINOR = non_default[0]
LATEST_SUPPORT_TYPE = supported_versions["versions"][LATEST_MINOR]["type"]
ONE_SUPPORT_TYPE = supported_versions["versions"][ONE_MINOR]["type"]
TWO_SUPPORT_TYPE = supported_versions["versions"][TWO_MINOR]["type"]
ONE_RELENV_PYTHON = supported_versions["versions"][ONE_MINOR]["relenv_python"]
TWO_RELENV_PYTHON = supported_versions["versions"][TWO_MINOR]["relenv_python"]
RC_FULL_VERSION = supported_versions["release_candidate_version"]

# Check if three major versions of salt are currently supported
if len(supported_major_versions) > 2:
    THREE_VERSIONS = True
    THREE_MAJOR = non_default[1].split(".")[0]
    THREE_MINOR = non_default[1]
    THREE_SUPPORT_TYPE = supported_versions["versions"][THREE_MINOR]["type"]
    THREE_RELENV_PYTHON = supported_versions["versions"][THREE_MINOR]["relenv_python"]
else:
    THREE_VERSIONS = False

# Prep template for modification
sitevars_template_file = Path("docs", "_templates", "sitevars.rst")
sitevars_updated_file = Path("docs", "sitevars.rst")
shutil.copyfile(sitevars_template_file, sitevars_updated_file)

# Update new sitevars file
with open(sitevars_updated_file, "r") as sitevars_updated_file_reader:
    sitevars_template = sitevars_updated_file_reader.read()

# Replace all var placeholders
sitevars_updated = (
    sitevars_template.replace("LATEST_MAJOR", LATEST_MAJOR)
    .replace("ONE_MAJOR", ONE_MAJOR)
    .replace("TWO_MAJOR", TWO_MAJOR)
    .replace("LATEST_MINOR", LATEST_MINOR)
    .replace("ONE_MINOR", ONE_MINOR)
    .replace("TWO_MINOR", TWO_MINOR)
    .replace("LATEST_SUPPORT_TYPE", LATEST_SUPPORT_TYPE)
    .replace("ONE_SUPPORT_TYPE", ONE_SUPPORT_TYPE)
    .replace("TWO_SUPPORT_TYPE", TWO_SUPPORT_TYPE)
    .replace("TWO_LOWER_SUPPORT_TYPE", TWO_SUPPORT_TYPE.lower())
    .replace("ONE_RELENV_PYTHON", ONE_RELENV_PYTHON)
    .replace("TWO_RELENV_PYTHON", TWO_RELENV_PYTHON)
    .replace("RC_FULL_VERSION", RC_FULL_VERSION)
)

if THREE_VERSIONS:
    sitevars_updated = (
        sitevars_updated.replace("THREE_MAJOR", THREE_MAJOR)
        .replace("THREE_MINOR", THREE_MINOR)
        .replace("THREE_SUPPORT_TYPE", TWO_SUPPORT_TYPE)
        .replace("THREE_RELENV_PYTHON", THREE_RELENV_PYTHON)
    )

# Write dynamic sitevars file
with open(sitevars_updated_file, "w") as sitevars_updated_file_writer:
    sitevars_updated_file_writer.write(sitevars_updated)
