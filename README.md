# lib-version

`lib-version` is a lightweight Python utility to retrieve the version of a project from its Git metadata using [setuptools-scm](https://pypi.org/project/setuptools-scm/).

## Installation

You don’t need to clone this repository. Install the library directly from the prebuilt distribution files.

1. **Download the latest `.whl` or `.tar.gz`** from the [GitHub repository's](https://github.com/remla25-team1/lib-version/dist).

2. Install the package using `pip`:

```bash
pip install https://github.com/remla25-team1/lib-version/dist/lib_version-0.1.1-py3-none-any.whl

# source distribution
pip install https://github.com/remla25-team1/lib-version/dist/lib_version-0.1.1.tar.gz
```

## Usage

After installation, you can import and use the VersionUtil class to get the project version:
```Python
from versionutil import VersionUtil

print(VersionUtil.get_version())
```

Expected output:
```bash
x.y.z 
# current version is 0.1.1
```

## Running tests
Clone the repository and run the tests like this:
```bash
git clone https://github.com/remla25-team1/lib-version.git
cd lib-version
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

## Automatic Versioning
We have two types of tags: vX.X.X or vX.X.X-pre-DATE-XXX. The first version is used for production. These will always be versions that work. The latter tag is an experimental model for developing purposes, this doesn't always have to be a working version. The version bump is now done automatically, so if v0.0.1 already exists, it will automatically bump the VERSION.txt up one count. Same story for the experimental tags, they will be based on the VERSION.txt as a base and increment based on date and based on last three digits if there are multiple models on the same day.
To trigger the automated version release:

1) Go to repo model-training on GitHub.
2) Click on the "Actions" tab.
3) Select "Versioning Workflow (SemVer + Dated Pre-Releases) " from the list on the left.
4) Click the “Run workflow” button and choose the type of version you want.
5) When this workflow has finished, go to Release model-training from the list on the left
6) You will now see that this workflow has been triggered automatically by the previous workflow.

