# LTE-U Coexistence Lab

[Português (Brasil)](README.pt-BR.md)

Explore how an empirical availability target affects the number of unlicensed-band slots a simulated LTE-U system can plan to use. The lab estimates a capacity for each channel using a CSV of free-slot observations. It runs on Python 3.9+ with the standard library.

To contribute, pick a [beginner task](https://github.com/henrivalle/lteu-coexistence-lab/contribute) and run the quick check in the [contributing guide](CONTRIBUTING.md).

```bash
python3 -m lteu_lab examples/synthetic.csv --target 80
python3 -m lteu_lab examples/synthetic.csv --target 95
python3 -m unittest discover -s tests -v
```

The first run reports two slots on `lab-a` and five on `lab-b`, each available in four of five observations. Raising the target to 95% requires five of five observations, yielding zero and one slot respectively. Compare these outcomes and discuss what would change with a larger sample.

## Input and interpretation

The CSV has columns `channel` and `free_slots`. Each row is one equally weighted observation for one channel. Channel labels use up to 64 ASCII letters, digits, underscores, periods or hyphens and start with a letter or digit. Free slots are nonnegative integers. The target is a whole percentage from 1 to 100, with a default of 90.

For each channel the tool finds the largest integer number of slots that at least the target percentage of observations can support. The output includes the supported slots, the support count, the total sample count and the target. Each estimate applies to one channel. It describes the sample and provides no estimate of joint availability across channels or assurance about future observations.

## Research context

This educational lab uses a simplified concept from the public UFG research on LTE-U coexistence and stochastic resource allocation. Its implementation and examples were written for this project. The full research model studies additional decisions about infrastructure costs and user demand. [UFG dissertation](https://repositorio.bc.ufg.br/tede/items/c5e3a766-3108-4456-8739-180398accbea) · [SBRC paper](https://doi.org/10.5753/sbrc.2018.2459)

The code is available under [MIT](LICENSE). To report an issue, include the command, Python version, and a small synthetic CSV.
