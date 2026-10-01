"""Reproduce the Fermi estimate from the saved official data; no dependencies."""

import json
from math import prod
from pathlib import Path


def main():
    source = Path(__file__).parent / "sources" / "madrid-undergraduate-enrolment.json"
    data = json.loads(source.read_text(encoding="utf-8"))["data"]
    rows = [row for row in data if row["Año"] == "2025"]
    if len(rows) != 18 or len({row["Concepto"] for row in rows}) != 18:
        raise ValueError("Expected 18 distinct university rows for 2024/25")
    if any(row["Estado dato"] != "Provisional" for row in rows):
        raise ValueError("Source status changed; review the written provenance")

    exact_anchor = sum(int(row["Valor"]) for row in rows)
    anchor = round(exact_anchor / 10_000) * 10_000
    assumptions = {
        "A1 relevant studies": (0.05, 0.10, 0.15),
        "A2 years 2-4": (0.60, 0.75, 0.80),
        "A3 experience gap": (0.30, 0.50, 0.70),
        "A4 commitment": (0.10, 0.20, 0.30),
    }
    base = [values[1] for values in assumptions.values()]
    print(f"2024/25 provisional anchor: {exact_anchor:,}; rounded: {anchor:,}")
    cumulative = anchor
    for (name, values) in assumptions.items():
        cumulative *= values[1]
        print(f"{name}: {values[1]:.0%} -> {cumulative:,.0f}")
    print(f"Headline: approximately {round(cumulative / 1000) * 1000:,} students/year")
    print(f"Exact-anchor result (before headline rounding): {exact_anchor * prod(base):,.3f}")
    print("One-at-a-time sensitivity (low / base / high):")
    for index, (name, values) in enumerate(assumptions.items()):
        outputs = []
        for value in values:
            changed = base.copy()
            changed[index] = value
            outputs.append(f"{anchor * prod(changed):,.0f}")
        print(f"  {name}: {' / '.join(outputs)}")
    low = anchor * prod(values[0] for values in assumptions.values())
    high = anchor * prod(values[2] for values in assumptions.values())
    print(f"Combined stress cases: {low:,.0f} / {high:,.0f} (not a confidence interval)")


if __name__ == "__main__":
    main()
