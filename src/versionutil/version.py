import importlib.metadata

import importlib.metadata

class VersionUtil:
    @classmethod
    def get_version(cls) -> str:
        try:
            # explicitly ask for the distribution name
            return importlib.metadata.version("lib-version")
        except importlib.metadata.PackageNotFoundError:
            return "0.0.0+unknown"
