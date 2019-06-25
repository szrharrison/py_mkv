from distutils.core import setup

setup(
    name="py_mkv",
    packages=["py_mkv"],
    version="0.0.1-alpha",
    license="MIT",
    description="Python library for loading and performing operations on .mkv files",
    author="Scott Harrison",
    author_email="s.z.r.harrison@gmail.com",
    url="https://github.com/szrharrison/py_mkv",
    download_url="https://github.com/user/reponame/archive/v_01.tar.gz",  # I explain this later on
    keywords=["mkv", ".mkv", "video"],
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",  # The current state of the package "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
