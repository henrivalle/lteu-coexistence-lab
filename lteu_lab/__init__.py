"""Estimate empirical free-slot capacities for individual channels."""

from bisect import bisect_left
import csv
import re
from typing import TextIO


def capacity_at_support(samples: list[int], target: int) -> tuple[int, int]:
    """Return the maximum supported capacity and the number of matching samples."""
    if type(target) is not int or not 1 <= target <= 100:
        raise ValueError("target must be an integer from 1 to 100")
    if not samples or any(type(value) is not int or value < 0 for value in samples):
        raise ValueError("samples must contain nonnegative integers")

    ordered = sorted(samples)
    required_count = (len(ordered) * target + 99) // 100
    slots = ordered[len(ordered) - required_count]
    support_count = len(ordered) - bisect_left(ordered, slots)
    return slots, support_count


def read_samples(stream: TextIO) -> dict[str, list[int]]:
    """Load one synthetic observation per CSV row, grouped by channel."""
    reader = csv.DictReader(stream, strict=True)
    header = reader.fieldnames or []
    if len(header) != 2 or set(header) != {"channel", "free_slots"}:
        raise ValueError("expected two columns named channel and free_slots")

    samples: dict[str, list[int]] = {}
    for row in reader:
        channel = (row.get("channel") or "").strip()
        slot_text = (row.get("free_slots") or "").strip()
        prefix = f"line {reader.line_num}"
        if None in row or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}", channel):
            raise ValueError(f"{prefix}: invalid channel or extra columns")
        try:
            slots = int(slot_text)
        except ValueError as exc:
            raise ValueError(f"{prefix}: free_slots must be a nonnegative integer") from exc
        if slots < 0:
            raise ValueError(f"{prefix}: free_slots must be a nonnegative integer")
        samples.setdefault(channel, []).append(slots)

    if not samples:
        raise ValueError("expected at least one observation")
    return samples
