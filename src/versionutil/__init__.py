from ._version import version as __version__

class VersionUtil:
    @classmethod
    def get_version(cls) -> str:
        return __version__