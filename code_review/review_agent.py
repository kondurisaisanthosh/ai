import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


ROOT_DIR = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT_DIR / ".env"
SKILLS_FILE = ROOT_DIR / "code_review" / "skills.md"

load_dotenv(ENV_FILE)

MODEL = os.getenv("OPENAI_MODEL")

if not MODEL:
    raise RuntimeError("OPENAI_MODEL is missing in .env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run(command):
    return subprocess.check_output(
        command,
        cwd=ROOT_DIR,
        text=True
    ).strip()

def get_repo_files():
    files = run(["git", "ls-files"]).splitlines()

    allowed = (
        ".java",
        ".xml",
        ".properties",
        ".yml",
        ".yaml",
        ".md",
    )

    ignored = (
        ".git/",
        ".venv/",
        "target/",
        "code_review/",
    )

    return [
        file for file in files
        if file.endswith(allowed)
           and not file.startswith(ignored)
    ]

def read_skills():
    return SKILLS_FILE.read_text(errors="ignore")

def build_code_context(files):
    parts = []

    for file in files:
        path = ROOT_DIR / file

        if not path.exists():
            continue

        content = path.read_text(errors="ignore")
        parts.append(f"""FILE: {file}```text{content}""")

    return "\n".join(parts)

def main():
    skills = read_skills()
    files = get_repo_files()
    code_context = build_code_context(files)

    if not code_context.strip():
        print("No code files found for review.")
        return 0

    prompt = f"""
        {skills}

        Project code:

        {code_context}
    """

    response = client.responses.create(
        model=MODEL,
        input=prompt,
    )

    output = response.output_text.strip()

    if output == "NO_WARNINGS":
        print("No issues found.")
    else:
        print()
        print("AI CODE REVIEW WARNINGS")
        print("-----------------------")
        print(output)
        print("-----------------------")
        print()

    return 0



if __name__ == "__main__":
    raise SystemExit(main())