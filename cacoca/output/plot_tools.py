import plotly as pl
import pandas as pd
import os


# define colors to use
def add_color(projects: pd.DataFrame = None, by_column: str = None):

    colors = projects.filter([by_column]).drop_duplicates()
    colors['color'] = get_color(colors[by_column].values.tolist())
    projects = projects.merge(colors, how='left', on=[by_column])

    return projects


def get_color(variables: list):
    n_scen = len(variables)
    if n_scen <= 10:
        cmap = pl.colors.qualitative.D3
    elif n_scen <= 24:
        cmap = pl.colors.qualitative.Dark24
    else:
        cmap = pl.colors.sample_colorscale('Viridis', n_scen + 1, colortype='rgb')

    return cmap[:n_scen]


def set_yrange_min_zero(fig: pl.graph_objs.Figure):
    yrange = list(fig.full_figure_for_development(warn=False).layout.yaxis.range)
    yrange[0] = min(yrange[0], -0.04 * yrange[1])
    yrange[1] = max(yrange[1], 1.04 * yrange[1])
    fig.update_yaxes(range=yrange)


def show_and_save(fig: pl.graph_objs.Figure, config: dict, base_name: str = None):
    """
    Show figure and export it for publication-ready usage.

    Exports:
      - .html (optional, if show_figures and show_figs_in_browser)
      - .svg (vector; best for Word -> PDF)
      - .png (high-res raster fallback)
    """

    # --- Show (optional) ---
    if config.get('show_figures', False):
        if config.get('show_figs_in_browser', False):
            pl.io.renderers.default = "browser"
        fig.show()

    # --- Save (optional) ---
    if not (base_name and config.get('save_figures', False)):
        return

    dir_path = config['output_dir']
    os.makedirs(dir_path, exist_ok=True)

    # Optional cropping
    if config.get('crop_figures', False):
        fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), title='')

    # Keep styling; avoid forcing small canvas size for export quality.
    # (Export resolution is controlled via scale/width/height in write_image.)
    fig.update_layout(font=dict(size=18))

    stem = os.path.join(dir_path, base_name)

    # --- Vector export: best quality in Word/PDF ---
    # Requires: pip install -U kaleido
    fig.write_image(stem + '.svg', format='svg')

    # --- High-res PNG fallback ---
    # scale=4 produces 4x pixel density relative to the layout size.
    fig.write_image(stem + '.png', format='png', scale=4)



display_names = {
    'steel_dri': 'Stahl DRI',
    'cement': 'Zement',
    'other_industries': 'Andere',
    'glass_and_ceramics': 'Glass',
    'basic_chemicals': 'Grundstoff-Chemie',
    'E-Steamcracker Naphtha': 'eCracker naphtha',
    'Referenz': 'Steamcracker naphtha',
    'Pyrolyse': 'Pyrolysis',
    'Pyrolyse E-Steamcracker': 'Pyrolysis eCracker',
    'Hydrocracking': 'Hydrocracking',
    'Hydrocracking E-Steamcracker': 'Hydrocracking eCracker',
    'Gasifizierung-FT': 'Gasification-FT',
    'Gasifizierung-FT E-Steamcracker': 'Gasification-FT eCracker',
    'Mechanisches Recycling': 'Mechanical recycling',
    'Methanolroute': 'Green methanol route',
    'Fischer-Tropsch': 'Fischer-Tropsch route',
    'Biomasse-DME-MTO': 'Dimethyl ether',
    'Effective CO2 Price': 'CO2-Preis (effektiv)',
    'Industry': 'Sektor',
    'Project name': 'Projekt',
    'compare_sectors': 'Sektorvergleich',
    'Abatement_cost': 'Vermeidungskosten',
    'Additional OPEX': 'Additional OPEX',
    'CAPEX annuity': 'CAPEX annuity',
    'h2share_influence': 'Einfluss des H2-Anteils',
    'ccsshare_influence': 'Einfluss des CCS-Anteils',
    'all': 'kombiniert',
    'h2': 'H2',
    'ng': 'Natural gas',
    'elec': 'Electricity',
    'ccoal': 'Kokskohle',
    'lowh2': '10-30% H2',
    'varyh2': '0-100% H2',
    'onlyh2': '100% H2',
    'prices': 'Preisannahmen',
    'Hydrogen': 'Hydrogen',
    'Natural Gas': 'Natural gas',
    'Electricity': 'Electricity',
    'Iron Ore': 'Eisenerz',
    'Injection Coal': 'Einblaskohle',
    'Scrap Steel': 'Stahlschrott',
    'Coking Coal': 'Kokskohle',
    'H2 Share': 'Anteil Wasserstoff',
    'all_projects': 'Alle Projekte',
    'CO2 Cost': 'Emissionskostendiff. (ETS)',
    'PCW': 'Post-consumer plastic waste',
    'CO2 EoL': 'EoL CO₂',
    'Naphta': 'Naphtha',
    'Biomass': 'Biomass',
    'Bioethanol': 'Bioethanol',
    'Biobutene': 'Biobuten',
}


def display_name(varname: str):
    if str(varname).startswith('sensitivity'):
        _, scen_name, h2name = varname.split('_')
        return f"Preisunsicherheit {display_name(scen_name)}, {display_name(h2name)}"
    else:
        return display_names.get(varname, varname)


def to_rgba(color: str, alpha: float):
    if isinstance(color, tuple):
        rgba = f"rgba{color + (alpha,)}"
    elif color.startswith("#"):
        rgba = f"rgba{pl.colors.hex_to_rgb(color) + (alpha,)}"
    else:
        rgba = color.replace("rgb", "rgba").replace(")", f", {alpha})")
    return rgba


def change_output_subdir_by_filename(config: dict, filename):
    subdirname = os.path.basename(filename)
    subdirname = os.path.splitext(subdirname)[0]
    if subdirname == os.path.split(config['output_dir'])[1]:
        return
    subdir = os.path.join(config['output_dir'], subdirname)
    if not os.path.exists(subdir):
        os.makedirs(subdir)
    config['output_dir'] = subdir
    return
