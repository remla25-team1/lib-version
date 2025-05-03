from src/versionutil import VersionUtil

def test_version_format():
    version = VersionUtil.get_version()
    assert version.startswith("0.1.0")
