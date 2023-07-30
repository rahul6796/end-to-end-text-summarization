
import setuptools


with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "end-to-end-text-summarization"
AUTHOR_USER_NAME = "rahul6796"
SRC_REPO = "text-summarizer"
AUTHOR_EMAIL = "prajapatirahul6796@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="text-summarization",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={
        "Bug_Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
    },
    package_dir={"" : "src"},
    packages=setuptools.find_packages(where="src")

)


