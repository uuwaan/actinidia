from setuptools import setup

setup(
    name="actinidia",
    version="999",
    python_requires=">=3.4",
    license="MIT",
    platforms=["Linux", "Windows", "Mac"],
    description="Set of text-based activity indicators",
    py_modules=["actinidia"],
    long_description=open("README.txt", "r", encoding="utf-8-sig").read(),
    author="Ivan Shcherbakov"
)
