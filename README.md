# lib-version

A Python library that can be asked for its own version at runtime via a simple API. It uses Git tags + setuptools_scm to manage semantic versions automatically.

---

## Prerequisites

- Python 3.7+  
- Git (your code lives in a Git repository)

---

## Installation (Editable / Development)

1. **Create & activate a virtualenv**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   # .venv\Scripts\activate     # Windows PowerShell
    ```
2. **Install in editable mode**

    ```
    pip install --upgrade pip
    pip install -e .
    ```

    You’ll see something like:

    ```
    Successfully built lib-version
    Installing collected packages: lib-version
    Successfully installed lib-version-0.0.0+unknown
    ```
3. **Create a release tag**
    ```
    git tag v0.1.0
    git push origin --tags
    ```

    Reinstall the editable
    ```
    pip install -e .
    ```

    ```
    python -c "from versionutil import VersionUtil; print(VersionUtil.get_version())"
    #   0.1.0.post0   (in editable mode)
    #   or 0.1.0      (if you installed from a built wheel)
    ```

4. **Building in PyPI**
    ```
    pip install build
    python -m build

    python -c "from versionutil import VersionUtil; print(VersionUtil.get_version())"
    ```