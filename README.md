# CaCoCa-IREES fork

This repository contains a project-specific modification of the CaCoCa (Carbon Contracts Calculator) model used in:

Maertens, R. (2026): Techno-economic assessment of green primary and secondary plastics production pathways.

The original CaCoCa model was developed by Dürrwächter et al. (2023). This fork extends the model for techno-economic assessment of polypropylene production pathways under different energy and carbon price scenarios.

## Reproducibility

The scripts required to reproduce the results of the associated publication are included in this repository.

To reproduce the main results:

1. Install dependencies via Poetry (`poetry install`)
2. Run the project-specific script:

   poetry run python plot_slides_polymers.py


## Data sources

All techno-economic input data used in the publication are derived from literature sources cited in the manuscript. The example data included in the original CaCoCa repository are not used for the published results.

## Scenario and technology inputs

Key techno-economic and price inputs used in the study are provided in:

- scenarios/basic/
- tech/basic/polymers.csv

These files contain the parameter values used in the published model runs.

----

# CaCoCa

CaCoCa (The Carbon Contracts Calculator) is a tool to model carbon contracts for difference (CCfDs) for industrial decarbonization projects. Abatement cost time curves can be calculated, and auctions of such carbon contracts (where the projects bidding the lowest carbon price are awarded contracts) can be modeled.

The techno-economic input data provided in this repository is incomplete and not to be relied upon. It only serves as an example for the functionality of the code. It is advised to use your own data.

## Installation

The Python version and packages are managed using [Poetry](https://python-poetry.org/docs/). Packages are listed in the file [pyproject.toml](pyproject.toml). Detailed instructions for installation can be found in the [documentation](doc/100_getting_started.md).

## Quick start / basic run

Runs are configured using a YAML input file. Example input files are located in the `config` folder.

For a test run, go to the main directory and run

```
poetry run python cacoca.py config/config.yml
```

This should create some lines of stdout for the different auction rounds.

## Contributors

The authors of CaCoCa are:

Jakob Dürrwächter\
Robin Blömer\
Philipp Verpoort\
Paul Effing\
Johannes Eckstein\
Falko Ueckerdt

## Fork maintainer

Robert Maertens (IREES)

## License

CaCoCa is Copyright (C) 2023, Jakob Dürrwächter, Robin Blömer, Johannes Eckstein and Falko Ueckerdt and is released under the terms of the
GNU General Public License v3.0. For the full license terms see
the included [`LICENSE` file](LICENSE).

## Reference / Please cite

To cite CaCoCa, please use:

J. Dürrwächter, R.Blömer, P. Verpoort, P. Effing, J. Eckstein, F. Ueckerdt (2023). _CaCoCa: The Carbon Contracts Calculator._ Version 0.1.0, <https://github.com/JakobBD/cacoca>.

A BibTeX entry for LaTeX users is:

 ```latex
@Manual{,
  title = {CaCoCa: The Carbon Contracts Calculator},
  author = {Jakob Dürrwächter and Robin Blömer and Philipp Verpoort and Paul Effing and Johannes Eckstein and Falko Ueckerdt},
  year = {2023},
  note = {Version 0.1.0},
  url = {https://github.com/JakobBD/cacoca},
}
```

## Documentation

Further documentation can be found in the [`doc/` folder](doc/).


