from pathlib import Path

from setuptools import find_packages
from setuptools import setup

DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with Path.open(DOCS_PATH, encoding="utf-8") as f1:
        with Path.open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="chatgpt-web",
    version="0.0.1",
    license="GNU v3",
    author="Simatwa Caleb",
    author_email="simatwacaleb@proton.com",
    description="Reverse Engineered ChatGPT Web-version ",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/Simatwa/ChatGPT-Web",
    project_urls={"Bug Report": "https://github.com/Simatwa/ChatGPT-Web/issues/new"},
    entry_points={
        "console_scripts": [
            # Update these with your actual console scripts
            "chatgpt-web = chatgpt_web.console:main",
        ],
    },
    install_requires=[
        "requests==2.28.2",
        "python-dotenv==1.0.0",
        "rich",
    ],
    long_description=Path.open(PATH, encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["BingChat"],  # Update this with your actual Python modules
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
        "Programming Language :: Python :: 3.12"
    ],
)