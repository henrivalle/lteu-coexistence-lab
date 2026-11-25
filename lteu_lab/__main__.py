import argparse
import csv
from pathlib import Path
import sys

from . import capacity_at_support, read_samples


def main() -> int:
    parser = argparse.ArgumentParser(description="Estimate per-channel free slots at a minimum observed support.")
    parser.add_argument("samples", type=Path, help="CSV with channel and free_slots columns")
    parser.add_argument("--target", type=int, default=90, metavar="PERCENT", help="integer percentage from 1 to 100")
    args = parser.parse_args()
    if not 1 <= args.target <= 100:
        parser.error("--target must be an integer from 1 to 100")

    try:
        with args.samples.open(encoding="utf-8-sig", newline="") as stream:
            samples = read_samples(stream)
    except (OSError, ValueError, csv.Error) as error:
        parser.error(str(error))

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("channel", "slots", "support_count", "sample_count", "target_percent"))
    for channel, values in sorted(samples.items()):
        slots, support_count = capacity_at_support(values, args.target)
        writer.writerow((channel, slots, support_count, len(values), args.target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
