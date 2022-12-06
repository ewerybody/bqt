try:
    from PySide6.QtCore import *
    from PySide6.QtCore import __version__, __version_info__
except ImportError:
    from PySide2.QtCore import *
    from PySide2.QtCore import __version__, __version_info__
