"""
noxfile
~~~~~~~

Nox configuration script

Modified from original source found in the Salt project:
- https://github.com/saltstack/salt
"""

import datetime
import os
import shutil
import sys
from pathlib import Path

# fmt: off
if __name__ == "__main__":
    sys.stderr.write(
        "Do not execute this file directly. Use nox instead, it will know how to handle this file\n"
    )
    sys.stderr.flush()
    exit(1)
# fmt: on

import nox  # isort:skip
from nox.command import CommandFailed  # isort:skip

# Global Path Definitions
REPO_ROOT = os.path.abspath(os.path.dirname(__file__))
# Python versions to run against
_PYTHON_VERSIONS = ("3", "3.6", "3.7", "3.8", "3.9", "3.10")

# Nox options
#  Reuse existing virtualenvs
nox.options.reuse_existing_virtualenvs = True
#  Don't fail on missing interpreters
nox.options.error_on_missing_interpreters = False

# Change current directory to REPO_ROOT
os.chdir(REPO_ROOT)

RUNTESTS_LOGFILE = os.path.join(
    "artifacts",
    "logs",
    "runtests-{}.log".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")),
)

# Prevent Python from writing bytecode
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"


def _get_session_python_version_info(session):
    try:
        version_info = session._runner._real_python_version_info
    except AttributeError:
        old_install_only_value = session._runner.global_config.install_only
        try:
            # Force install only to be false for the following chunk of code
            # For additional information as to why see:
            #   https://github.com/theacodes/nox/pull/181
            session._runner.global_config.install_only = False
            session_py_version = session.run(
                "python",
                "-c"
                'import sys; sys.stdout.write("{}.{}.{}".format(*sys.version_info))',
                silent=True,
                log=False,
                external=True,
            )
            version_info = tuple(
                int(part) for part in session_py_version.split(".") if part.isdigit()
            )
            session._runner._real_python_version_info = version_info
        finally:
            session._runner.global_config.install_only = old_install_only_value
    return version_info


def _get_pydir(session):
    version_info = _get_session_python_version_info(session)
    if version_info < (3, 5):
        session.error("Only Python >= 3.6 is supported")
    return "py{}.{}".format(*version_info)


def _install_requirements(session, transport):
    # Latest pip, setuptools, and wheel
    install_command = ["--progress-bar=off", "-U", "pip", "setuptools", "wheel"]
    session.install(*install_command, silent=True)

    # Install requirements
    requirements_file = os.path.join("docs/requirements.txt")
    install_command = ["--progress-bar=off", "-r", requirements_file]
    session.install(*install_command, silent=True)


@nox.session(name="docs-versions-update", python="3")
def docs_versions_update(session):
    """
    Run tools/version-updater.py but don't build Sphinx HTML
    """
    pydir = _get_pydir(session)

    # Latest pip, setuptools, and wheel
    install_command = ["--progress-bar=off", "-U", "pip", "setuptools", "wheel"]
    session.install(*install_command, silent=True)

    # Install requirements
    requirements_file = Path("docs", "requirements.txt")
    install_command = ["--progress-bar=off", "-r", str(requirements_file)]
    session.install(*install_command, silent=True)

    # Pull down latest Salt version manifest and update sitevars, etc.
    if download_versions:
        version_updater_script = Path("tools", "version-updater.py")
        session.run("python", str(version_updater_script), external=True)


@nox.session(name="docs-html", python="3")
@nox.parametrize("clean", [False, True])
@nox.parametrize("gen_sitevars", [False, True])
def docs_html(session, clean, gen_sitevars):
    """
    Build Sphinx HTML Documentation
    """
    pydir = _get_pydir(session)

    # Latest pip, setuptools, and wheel
    install_command = ["--progress-bar=off", "-U", "pip", "setuptools", "wheel"]
    session.install(*install_command, silent=True)

    # Install requirements
    requirements_file = Path("docs", "requirements.txt")
    install_command = ["--progress-bar=off", "-r", str(requirements_file)]
    session.install(*install_command, silent=True)

    # Update sitevars from tools/supported-versions.json manifest
    if gen_sitevars:
        version_updater_script = Path("tools", "version-updater.py")
        session.run("python", str(version_updater_script), external=True)

    # Run sphinx
    build_dir = Path("docs", "_build", "html")
    sphinxopts = "-Wn"
    if clean:
        sphinxopts += "E"
    args = [sphinxopts, "--keep-going", "docs", str(build_dir)]
    session.run("sphinx-build", *args, external=True)


@nox.session(python="3")
def docs(session) -> None:
    """
    Build and serve the Sphinx HTML documentation, with live reloading on file changes, via sphinx-autobuild.

    Note: Only use this in INTERACTIVE DEVELOPMENT MODE. This SHOULD NOT be called
        in CI/CD pipelines, as it will hang.
    """
    pydir = _get_pydir(session)

    # Latest pip, setuptools, and wheel
    install_command = ["--progress-bar=off", "-U", "pip", "setuptools", "wheel"]
    session.install(*install_command, silent=True)

    # Install requirements
    requirements_file = Path("docs", "requirements.txt")
    install_command = ["--progress-bar=off", "-r", str(requirements_file)]
    session.install(*install_command, silent=True)

    # Install autobuild req
    install_command = ["--progress-bar=off", "-U", "sphinx-autobuild"]
    session.install(*install_command, silent=True)

    # Launching LIVE reloading Sphinx session
    build_dir = Path("docs", "_build", "html")
    args = ["--watch", ".", "--open-browser", "docs", str(build_dir)]
    if build_dir.exists():
        shutil.rmtree(build_dir)
        # Generate sitevars
        version_updater_script = Path("tools", "version-updater.py")
        session.run("python", str(version_updater_script), external=True)

    session.run("sphinx-autobuild", *args)
