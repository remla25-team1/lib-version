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

3. Usage
After installation, you can import and use the VersionUtil class to get the project version:
```Python
from versionutil import VersionUtil

print(VersionUtil.get_version())
```
