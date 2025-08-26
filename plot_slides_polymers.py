# %%
from cacoca.run import run
from cacoca.output.plot_tools import change_output_subdir_by_filename

setup, cost_and_em_actual = run(config_filepath='config/config_slides_polymers.yml')
change_output_subdir_by_filename(setup.config, __file__)


# %% SECTOR COMPARISON  ============================================================================

from cacoca.output.plot_project_cost_time_curves import plot_project_cost_time_curves
from cacoca.run import run
from cacoca.output.plot_tools import change_output_subdir_by_filename


if 'cost_and_em_actual' not in globals():
    setup, cost_and_em_actual = run(config_filepath='config/config_slides_polymers.yml')
    change_output_subdir_by_filename(setup.config, __file__)

# === DEBUGGING-CODE HIER EINFÜGEN ===
#import pandas as pd
#print("--- DEBUGGING-AUSGABE ---")
#pd.set_option('display.max_columns', None)
#print("Verfügbare Projekte im DataFrame 'cost_and_em_actual':")
#print(cost_and_em_actual.loc[cost_and_em_actual["Project name"]=="Pyrolyse"])
#print("-------------------------")
# === ENDE DEBUGGING-CODE ===

project_names = [
#'Zement f)',
    'E-Steamcracker Naphtha',
    'Pyrolyse',
    'Pyrolyse E-Steamcracker',
    #'Hydrocracking',
    #'Hydrocracking E-Steamcracker',
    #'Gasifizierung-FT',
    #'Gasifizierung-FT E-Steamcracker'
    'Mechanisches Recycling'
    ]
#plot_project_cost_time_curves(cost_and_em_actual, config=setup.config, print_name='compare_sectors',
#                              **{'Project name': project_names})


# %% ALL PROJECTS  =================================================================================

import copy
from cacoca.setup.read_input import read_config
from cacoca.run import run
from cacoca.output.plot_project_cost_time_curves import plot_project_cost_time_curves
from cacoca.output.plot_tools import change_output_subdir_by_filename


if 'config' not in globals():
    config = read_config(filepath='config/config_slides_polymers.yml')
    change_output_subdir_by_filename(config, __file__)

config_all = copy.deepcopy(config)
config_all['projects_file'] = 'config/projects.csv'
setup_all, cost_and_em_all = run(config=config_all)

#plot_project_cost_time_curves(cost_and_em_all, config=setup_all.config, print_name='all_projects',
#                              color_by='Industry')


# %% STACKED BARS  =================================================================================

from cacoca.output.plot_stacked_bars import plot_stacked_bars, plot_stacked_bars_multi
from cacoca.run import run
from cacoca.output.plot_tools import change_output_subdir_by_filename


if 'cost_and_em_actual' not in globals():
    setup, cost_and_em_actual = run(config_filepath='config/config_slides_polymers.yml')
    change_output_subdir_by_filename(setup.config, __file__)

project_names = [
    #'Zement f)',
    'E-Steamcracker Naphtha',
    'Pyrolyse',
    'Pyrolyse E-Steamcracker',
    #'Hydrocracking',
    #'Hydrocracking E-Steamcracker',
    #'Gasifizierung-FT',
    #'Gasifizierung-FT E-Steamcracker'
    'Mechanisches Recycling'
    ]

plot_stacked_bars_multi(cost_and_em_actual, setup.config, project_names,
                        cost_per='product', emission_diff=False, project_ref="Pyrolyse")
for project_name in project_names:
    plot_stacked_bars(cost_and_em_actual, setup.config, project_name=project_name,
                      cost_per='product', emission_diff=False)
    #plot_stacked_bars(cost_and_em_actual, config, project_name=project_name,
    #                   cost_per='em_savings', is_diff=True)


# %% PRICE SCENARIOS  ==============================================================================

from cacoca.output.plot_price_scenarios import plot_price_scenarios
from cacoca.setup.setup import Setup
from cacoca.output.plot_tools import change_output_subdir_by_filename


if 'setup' not in globals():
    setup = Setup(config_filepath='config/config_slides_polymers.yml')
    change_output_subdir_by_filename(setup.config, __file__)

# plot_price_scenarios(setup)


# %% H2 SHARE SCENARIOS  ===========================================================================

from cacoca.output.plot_price_scenarios import plot_h2share_scenarios
from cacoca.setup.setup import Setup
from cacoca.output.plot_tools import change_output_subdir_by_filename


if 'setup' not in globals():
    setup = Setup(config_filepath='config/config_slides_polymers.yml')
    change_output_subdir_by_filename(setup.config, __file__)

project_names = [
    #'Zement f)',
    'E-Steamcracker Naphtha',
    'Pyrolyse',
    'Pyrolyse E-Steamcracker',
    #'Hydrocracking',
    #'Hydrocracking E-Steamcracker',
    #'Gasifizierung-FT',
    #'Gasifizierung-FT E-Steamcracker'
    'Mechanisches Recycling'
    ]
#plot_h2share_scenarios(setup, project_names, 'h2share', 'vary_h2share')


# %% INFLUENCE OF H2 SHARE  ========================================================================

from cacoca.output.plot_project_cost_time_curves import plot_project_cost_time_curves
from cacoca.run import run
from cacoca.output.plot_tools import change_output_subdir_by_filename


if 'cost_and_em_actual' not in globals():
    setup, cost_and_em_actual = run(config_filepath='config/config_slides_polymers.yml')
    change_output_subdir_by_filename(setup.config, __file__)

project_names = [
    'Pyrolyse']
#plot_project_cost_time_curves(cost_and_em_actual, config=setup.config,
#                              print_name='h2share_influence', **{'Project name': project_names})


# %% ABSOLUTE HYDROGEN DEMAND  =====================================================================

from cacoca.output.plot_absolute_hydrogen_demand import plot_absolute_hydrogen_demand
from cacoca.run import run
from cacoca.calc.calc_derived_quantities import add_absolute_hydrogen_demand
from cacoca.output.plot_tools import change_output_subdir_by_filename


if 'cost_and_em_actual' not in globals():
    setup, cost_and_em_actual = run(config_filepath='config/config_slides_polymers.yml')
    change_output_subdir_by_filename(setup.config, __file__)

cost_and_em_actual = add_absolute_hydrogen_demand(cost_and_em_actual, setup)

project_names = [
    'Pyrolyse']
#plot_absolute_hydrogen_demand(cost_and_em_actual, setup, project_names)


# %% INFLUENCE OF UNCERTAINTIES  ===================================================================

import copy
from cacoca.run import run
from cacoca.setup.read_input import read_config
from cacoca.output.plot_project_cost_time_curves import plot_project_cost_time_curves
from cacoca.output.plot_tools import change_output_subdir_by_filename


if 'config' not in globals():
    config = read_config(filepath='config/config_slides_polymers.yml')
    change_output_subdir_by_filename(config, __file__)

project_names_dict = {
    'lowh2': 'Pyrolyse',
    'varyh2': 'Pyrolyse',
    'onlyh2': 'Pyrolyse'
}

uct_prm_definitions = {
    "Hydrogen": {
        'is_relative': False,
        'std_scenario': 'Test',
        'data_frame': 'prices',
        'filters': {
            'Component': 'Hydrogen'
            }
    },
    "Natural Gas": {
        'is_relative': True,
        'std_value': 0.1,
        'data_frame': 'prices',
        'filters': {
            'Component': 'Natural Gas'
            }
    },
    "Electricity": {
        'is_relative': True,
        'std_value': 0.1,
        'data_frame': 'prices',
        'filters': {
            'Component': 'Electricity'
            }
    },
    "CO2": {
        'is_relative': True,
        'std_value': 0.2,
        'data_frame': 'prices',
        'filters': {
            'Component': 'CO2'
            }
    }
}
# uncertain_parameters:

sens_scenarios = {
    "all": ['Hydrogen', 'Natural Gas', 'Electricity', 'CO2'],
    "h2": ['Hydrogen'],
    "ng": ['Natural Gas'],
    "elec": ['Electricity']
}

for scen_name, uct_prms in sens_scenarios.items():

    config_sens = copy.deepcopy(config)
    config_sens['uncertain_parameters'] = [uct_prm_definitions[up] for up in uct_prms]

    setup, cost_and_em_sens = run(config=config_sens)

    #for h2name, project_name in project_names_dict.items():
        #plot_project_cost_time_curves(cost_and_em_sens,
        #                              config=setup.config,
        #                              print_name=f'sensitivity_{scen_name}_{h2name}',
        #                              **{'Project name': [project_name]})


# %%
