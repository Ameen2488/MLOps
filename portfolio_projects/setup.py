import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "MLOps"
AUTHOR_USER_NAME = "Ameen2488"
AUTHOR_EMAIL = "amnsid24@yahoo.com"

setuptools.setup(
    name=f"{AUTHOR_USER_NAME}/{REPO_NAME}",
    version=__version__,
    author=USER_NAME,
    author_email="[EMAIL_ADDRESS]",
    description="A small python package for cnn image classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)