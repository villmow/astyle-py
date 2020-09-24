from setuptools import setup, find_packages



setup(
    name='astyle',
    version='3.1',
    python_requires='>=3.6',
    description='',
    author='Johannes Villmow',
    author_email='johannes.villmow@hs-rm.de',
    license='mit',
    packages=find_packages(),
    # ext_modules=[CMakeExtension('astyle-src')],
    # cmdclass={
    #     'build_ext': build_ext,
    # }
)

