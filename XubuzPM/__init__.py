
from .cli import cli

__all__ = (cli)
__version__ = "0.0.1"
__author__ = "Ayush K M"

XPM_SOURCES = "/etc/xpm/sources.list"

CACHE_FOLDER = "/var/cache/xpm"
CACHE_ARCHIVES = CACHE_FOLDER + "/archives"

if __name__ == "__main__":
	exit(0)
