# CaCoCa-IREES fork

This repository contains the project-specific modification of the CaCoCa (Carbon Contracts Calculator) model used in:

> Maertens, R. (2026). *Techno-economic comparison of fossil, renewable-carbon and recycling pathways for polypropylene.*

The original CaCoCa model was developed by Dürrwächter et al. (2023). This fork adapts the process-comparison functionality for a techno-economic assessment of 14 polypropylene production pathways under different energy and carbon-price assumptions. The CCfD auction module of the original model is not used for the publication.

## Reproducibility scope

The repository reproduces the annual cost and emissions calculations from the **aggregated pathway inputs** used in the publication.

The file [`data/tech/basic/polymers.csv`](data/tech/basic/polymers.csv) contains one aggregated parameter set for each assessed polypropylene pathway. These values include the pathway-level CAPEX, additional OPEX, material and energy requirements, and direct process emissions per tonne of polypropylene. The CSV does **not** contain the individual process-step datasets from which the pathways were assembled.

The individual process-step assumptions, yields, allocation calculations, sources, and the aggregation from process steps to complete pathways are documented in the Supporting Information accompanying the publication. The aggregation was performed before the CaCoCa calculation, using openLCA. CaCoCa therefore starts from the aggregated pathway values in `polymers.csv`; it does not reconstruct the process chain from individual unit processes.

The final archived release, including the Supporting Information and the model files corresponding to the manuscript, is available via Zenodo:

- <https://doi.org/10.5281/zenodo.18694649>

## Installation

The Python version and packages are managed using [Poetry](https://python-poetry.org/docs/). From the repository root, install the dependencies with:

```bash
poetry install
```

Detailed generic CaCoCa installation instructions are available in [`doc/100_getting_started.md`](doc/100_getting_started.md).

## Reproducing the publication results

Run the project-specific analysis from the repository root:

```bash
poetry run python plot_slides_polymers.py
```

The script reads the pathway selection from [`config/projects_polymers.csv`](config/projects_polymers.csv), the model configuration from [`config/config_slides_polymers.yml`](config/config_slides_polymers.yml), and the input data described below.

The run writes the principal tabular results to:

- `results_baseline.csv`
- `results_all_projects.csv`

Figures are written to the configured output directory, normally `output/plot_slides_polymers/` and open in the local web browser.

## Input data and file structure

The principal publication-specific inputs are:

| File | Content |
|---|---|
| [`data/tech/basic/polymers.csv`](data/tech/basic/polymers.csv) | Aggregated techno-economic and emissions dataset for the 14 polypropylene pathways; not individual process steps |
| [`config/projects_polymers.csv`](config/projects_polymers.csv) | Pathway selection and project-specific technical assumptions |
| [`config/config_slides_polymers.yml`](config/config_slides_polymers.yml) | Model settings and selection of price scenarios |
| [`data/scenarios/basic/prices_co2.csv`](data/scenarios/basic/prices_co2.csv) | Direct process CO₂-price trajectories |
| [`data/scenarios/basic/prices_fuels.csv`](data/scenarios/basic/prices_fuels.csv) | Energy, material-feedstock, and hypothetical end-of-life CO₂-price trajectories |

All literature-based and author-assumption sources used in `polymers.csv` are identified in its source column. 

## Changing the CO₂-price scenario

The selected scenarios are defined in [`config/config_slides_polymers.yml`](config/config_slides_polymers.yml), under:

```yaml
scenarios_actual:
  prices:
```

Two separate components must be selected:

- `CO2`: the price applied to direct process emissions;
- `CO2 EoL`: the hypothetical price applied to fossil carbon released at end-of-life for the fossil-naphtha pathways.

### High CO₂-price trajectory

```yaml
CO2: 'Ariadne-Indikation-KN2045_Mix'
CO2 EoL: 'Ariadne-Indikation-KN2045_Mix'
```

### Low CO₂-price trajectory

```yaml
CO2: 'Ariadne-Indikation-ExPol'
CO2 EoL: 'Ariadne-Indikation-ExPol'
```

Both entries should normally be changed together. Otherwise, direct process emissions and the hypothetical end-of-life component would be priced using different trajectories.

The direct process CO₂ trajectories are stored in [`data/scenarios/basic/prices_co2.csv`](data/scenarios/basic/prices_co2.csv). The corresponding `CO2 EoL` trajectories are stored in [`data/scenarios/basic/prices_fuels.csv`](data/scenarios/basic/prices_fuels.csv).


## Interpretation and limitations

The repository supports reproduction of the pathway-level engineering cost calculation. It is not a market-deployment forecast, a system optimisation, or a complete consequential life-cycle assessment. In particular:

- technology-specific learning curves are not modelled;
- literature inputs represent different levels of technological maturity;
- feedstock availability and competing uses are not modelled;
- electricity and hydrogen are represented by annual average prices;
- carbon is not tracked through multiple recycling cycles;
- the hypothetical end-of-life CO₂ component is not a current production cost.

See the manuscript for the full methodological scope and limitations.

---

# Original CaCoCa model

CaCoCa (The Carbon Contracts Calculator) is a tool to model carbon contracts for difference (CCfDs) for industrial decarbonisation projects. Abatement-cost time curves can be calculated, and auctions of such carbon contracts can be modelled.

The generic example datasets inherited from the original CaCoCa repository are not used for the polypropylene results unless explicitly selected in the project configuration. Users applying the tool to other questions should supply and validate their own data.

## Generic quick start

Runs are configured using a YAML input file. Example input files are located in the `config` folder.

For a generic test run, go to the main directory and run:

```bash
poetry run python cacoca.py config/config.yml
```

## Contributors

The authors of the original CaCoCa model are:

Jakob Dürrwächter  
Robin Blömer  
Philipp Verpoort  
Paul Effing  
Johannes Eckstein  
Falko Ueckerdt

## Fork maintainer

Robert Maertens (IREES)

## License

CaCoCa is Copyright (C) 2023, Jakob Dürrwächter, Robin Blömer, Johannes Eckstein and Falko Ueckerdt and is released under the terms of the GNU General Public License v3.0. For the full license terms, see the included [`LICENSE`](LICENSE) file.

## Reference / Please cite

To cite the original CaCoCa model, use:

J. Dürrwächter, R. Blömer, P. Verpoort, P. Effing, J. Eckstein, F. Ueckerdt (2023). *CaCoCa: The Carbon Contracts Calculator.* Version 0.1.0, <https://github.com/JakobBD/cacoca>.

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

Further generic CaCoCa documentation is available in the [`doc/`](doc/) folder.
