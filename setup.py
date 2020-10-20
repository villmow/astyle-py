import os
import pathlib

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext as build_ext_orig


class CMakeExtension(Extension):

    def __init__(self, name):
        # don't invoke the original build_ext for this special extension
        super().__init__(name, sources=[])


class build_ext(build_ext_orig):

    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)
        super().run()

    def build_cmake(self, ext):
        print("extension_name", ext.name)

        cwd = pathlib.Path(ext.name).absolute()
        # these dirs will be created in build_py, so if you don't have
        # any python sources to bundle, the dirs will be missing
        build_temp = pathlib.Path(self.build_temp).absolute()
        build_temp.mkdir(parents=True, exist_ok=True)
        # extdir = pathlib.Path(self.get_ext_fullpath(ext.name))
        # extdir.mkdir(parents=True, exist_ok=True)

        # example of cmake args
        # config = 'Debug' if self.debug else 'Release'
        cmake_args = [
            # '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + str(extdir.parent.absolute()),
            '-DBUILD_SHARED_LIBS=1'
        ]

        # example of build args
        build_args = [
            # '--config', config,
            # '--', '-j4'
        ]

        os.chdir(str(build_temp))
        self.spawn(['cmake', str(cwd)] + cmake_args)
        # if not self.dry_run:
        self.spawn(['make'])

        lib = build_temp / "libastyle.so"
        lib = lib.absolute()
        link = build_temp.parent / "libastyle.so"

        assert lib.exists()

        relative_target = lib.relative_to(link.parent)

        link.symlink_to(relative_target)

        # Troubleshooting: if fail on line above then delete all possible
        # temporary CMake files including "CMakeCache.txt" in top level dir.
        os.chdir(str(cwd))



setup(
    name='astyle',
    version='3.1',
    python_requires='>=3.6',
    description='',
    author='Johannes Villmow',
    author_email='johannes.villmow@hs-rm.de',
    license='mit',
    packages=find_packages(),
    ext_modules=[CMakeExtension('astyle-src')],
    cmdclass={
        'build_ext': build_ext,
    }
)

