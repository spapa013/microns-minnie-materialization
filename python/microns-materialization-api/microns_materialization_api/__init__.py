from microns_utils import config_utils

_repo = 'microns-materialization'
_package = 'microns-materialization-api'

__version__ = config_utils.get_package_version(repo=_repo, package=_package)