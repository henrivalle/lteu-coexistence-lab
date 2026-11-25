import csv
import io
from pathlib import Path
import random
import subprocess
import sys
import unittest

from lteu_lab import capacity_at_support, read_samples


ROOT = Path(__file__).resolve().parents[1]


class CapacityTests(unittest.TestCase):
    def test_boundary_and_full_support(self):
        samples = [0, 2, 4, 4, 8]
        self.assertEqual(capacity_at_support(samples, 80), (2, 4))
        self.assertEqual(capacity_at_support(samples, 60), (4, 3))
        self.assertEqual(capacity_at_support(samples, 100), (0, 5))

    def test_result_agrees_with_exhaustive_search(self):
        rng = random.Random(25)
        for _ in range(30):
            samples = [rng.randrange(12) for _ in range(rng.randint(1, 15))]
            target = rng.randint(1, 100)
            with self.subTest(samples=samples, target=target):
                support = [sum(sample >= slots for sample in samples) for slots in range(max(samples) + 1)]
                expected = max(slots for slots, count in enumerate(support) if 100 * count >= target * len(samples))
                self.assertEqual(capacity_at_support(samples, target), (expected, support[expected]))

    def test_reject_invalid_inputs(self):
        for samples, target in (([], 50), ([1], 0), ([1], 101), ([-1], 50), ([True], 50)):
            with self.subTest(samples=samples, target=target), self.assertRaises(ValueError):
                capacity_at_support(samples, target)


class InputTests(unittest.TestCase):
    def test_csv_groups_channel_samples(self):
        data = io.StringIO("channel,free_slots\nch-2,1\nch-1,0\nch-2,3\n")
        self.assertEqual(read_samples(data), {"ch-2": [1, 3], "ch-1": [0]})

    def test_bad_csv_reports_the_source_line(self):
        for row in ("alpha,-1", "alpha,abc", "alpha", "alpha,2,extra", "=1,2"):
            with self.subTest(row=row), self.assertRaisesRegex(ValueError, "line 2"):
                read_samples(io.StringIO("channel,free_slots\n" + row + "\n"))

    def test_cli_example_and_usage_error(self):
        command = [sys.executable, "-m", "lteu_lab", "examples/synthetic.csv"]
        process = subprocess.run(command + ["--target", "80"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        rows = list(csv.DictReader(io.StringIO(process.stdout)))
        self.assertEqual([(r["channel"], r["slots"], r["support_count"]) for r in rows],
                         [("lab-a", "2", "4"), ("lab-b", "5", "4")])
        invalid = subprocess.run(command + ["--target", "105"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(invalid.returncode, 2)
        self.assertIn("--target", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
