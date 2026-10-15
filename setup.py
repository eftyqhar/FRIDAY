from setuptools import setup, find_packages

setup(
    name="friday-agent",
    version="0.1.0",
    description="F.R.I.D.A.Y. - Autonomous Browser Copilot powered by Playwright & LLMs",
    author="Eftyqhar",
    py_modules=["main", "agent", "browser_manager", "config", "dom_annotator", "actions"],
    packages=find_packages(),
    install_requires=[
        "playwright>=1.49.0",
        "google-genai>=0.8.0",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
        "rich>=13.0.0",
        "pillow>=10.0.0",
    ],
    entry_points={
        "console_scripts": [
            "friday = main:main",
        ],
    },
    python_requires=">=3.10",
)
