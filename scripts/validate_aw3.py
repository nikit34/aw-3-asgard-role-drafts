#!/usr/bin/env python3
"""Validate AW-3 role draft structure, contradictions, and basic completeness."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "unit-tester/add/200-larixon-test-infra.md",
    "unit-tester/replace/011-test-style.md",
    "unit-tester/replace/020-coverage.md",
    "unit-tester/replace/031-repository-tests.md",
    "unit-tester/replace/032-usecase-tests.md",
    "unit-tester/replace/033-viewmodel-tests.md",
    "unit-tester/replace/034-mapper-tests.md",
    "integ-tester/replace/037-multi-market-tests.md",
    "integ-tester/add/200-larixon-test-devices.md",
    "integ-tester/extend/036-accessibility-tests.md",
    "integ-tester/add/210-playwright-web-tests.md",
]

COMPLETENESS_HINTS = {
    "unit-tester/add/200-larixon-test-infra.md": {
        "required": ["bamboo", "testdebugunittest", "testtjdebugunittest", "test fixture", "ios"],
        "warn": ["la-baz", "build/reports/kover/html/index.html"],
    },
    "unit-tester/replace/011-test-style.md": {
        "required": ["junit 5", "mockk", "kotest", "action_condition_expectedresult", "assertions"],
        "warn": ["quick", "nimble"],
    },
    "unit-tester/replace/020-coverage.md": {
        "required": ["kover", "repository", "usecase", "viewmodel", "mapper"],
        "warn": ["jacoco", "bamboo"],
    },
    "integ-tester/replace/037-multi-market-tests.md": {
        "required": ["bz", "tj", "mn", "gdpr", "emongolia"],
        "warn": ["ja", "pn", "sl"],
    },
    "integ-tester/add/200-larixon-test-devices.md": {
        "required": [
            "stand1.dev.larixon.com",
            "connectedtjdebugandroidtest",
            "allure/testops",
            "browserstack",
            "project/168/launches",
            "project/69/launches",
        ],
        "warn": ["plan key"],
    },
    "integ-tester/extend/036-accessibility-tests.md": {
        "required": ["left-to-right", "48dp"],
        "warn": ["talkback", "voiceover"],
    },
    "integ-tester/add/210-playwright-web-tests.md": {
        "required": ["disabled", "web", "hybrid", "playwright"],
        "warn": ["repo", "base urls", "allure"],
    },
}

ALLOWED_PLAYWRIGHT_FILES = {
    "README.md",
    "integ-tester/add/210-playwright-web-tests.md",
}
ALLOWED_BROWSERSTACK_FILES = {
    "README.md",
    "integ-tester/add/200-larixon-test-devices.md",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def all_markdown_files() -> list[Path]:
    return sorted(ROOT.rglob("*.md"))


def line_count(path: Path) -> int:
    return len(read(path).splitlines())


def find_absolute_paths(text: str) -> list[str]:
    return re.findall(r"(/Users/permi/[^\s`]+)", text)


def contains_all(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []
    passes: list[str] = []

    # Structure
    for rel_path in REQUIRED_FILES:
        full_path = ROOT / rel_path
        if full_path.exists():
            passes.append(f"required file exists: {rel_path}")
        else:
            failures.append(f"missing required file: {rel_path}")

    # File size / AW-3 line budget
    for md_file in all_markdown_files():
        count = line_count(md_file)
        if count <= 400:
            passes.append(f"line budget ok: {rel(md_file)} ({count} lines)")
        else:
            warnings.append(f"line budget over 400: {rel(md_file)} ({count} lines)")

    # Local source references in README must exist
    readme = ROOT / "README.md"
    if readme.exists():
        for abs_path in find_absolute_paths(read(readme)):
            if Path(abs_path).exists():
                passes.append(f"README source path exists: {abs_path}")
            else:
                warnings.append(f"README source path missing locally: {abs_path}")

    # Explicit contradiction guards
    for md_file in all_markdown_files():
        text = read(md_file)
        rel_path = rel(md_file)

        if "MOB-617" in text:
            failures.append(f"MOB-617 residue found: {rel_path}")

        if "Playwright" in text and rel_path not in ALLOWED_PLAYWRIGHT_FILES:
            failures.append(f"unexpected Playwright mention outside allowed files: {rel_path}")

        if "BrowserStack" in text and rel_path not in ALLOWED_BROWSERSTACK_FILES:
            lowered = text.lower()
            qualified = (
                "do not silently assume browserstack" in lowered
                or "browserstack as out of scope" in lowered
                or "browserstack or another cloud-device lab" in lowered
                or "not be described as a baseline runner" in lowered
            )
            if not qualified:
                failures.append(f"unexpected BrowserStack mention outside allowed files: {rel_path}")

        for idx, line in enumerate(text.splitlines(), start=1):
            lowered = line.lower()
            if "bamboo" in lowered and (
                "trigger" in lowered or "start" in lowered or "run bamboo" in lowered
            ):
                if "do not" not in lowered and "not " not in lowered and "outside" not in lowered:
                    failures.append(
                        f"possible tester-owned Bamboo execution phrasing: {rel_path}:{idx}"
                    )

    # Completeness heuristics from AW-3
    for rel_path, hints in COMPLETENESS_HINTS.items():
        full_path = ROOT / rel_path
        if not full_path.exists():
            continue
        text = read(full_path)

        lowered = text.lower()

        for needle in hints.get("required", []):
            if needle in lowered:
                passes.append(f"required hint present in {rel_path}: {needle}")
            else:
                warnings.append(f"required hint missing in {rel_path}: {needle}")

        for needle in hints.get("warn", []):
            if needle not in lowered:
                warnings.append(f"optional completeness hint missing in {rel_path}: {needle}")

    print("AW-3 validation report")
    print(f"root: {ROOT}")
    print()
    print(f"FAIL: {len(failures)}")
    for item in failures:
        print(f"- {item}")
    print()
    print(f"WARN: {len(warnings)}")
    for item in warnings:
        print(f"- {item}")
    print()
    print(f"PASS: {len(passes)}")
    for item in passes:
        print(f"- {item}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
