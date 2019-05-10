from conda_smithy._version import get_versions
import conda_smithy.github_services as github

__version__ = get_versions()["version"]
del get_versions
