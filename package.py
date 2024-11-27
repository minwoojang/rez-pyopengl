name = "pyopengl"

version = "3.1.5"

authors = [
    "Mike C. Fletcher"
]

description = \
    """
    Standard OpenGL bindings for Python.
    """

requires = [
    "cmake-3+",
    "pip",
    "python-3"
]

variants = [['platform-linux', 'arch-x86_64']]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "pyopengl-{version}".format(version=str(version))

def commands():
    env.PYTHONPATH.prepend("{root}")
