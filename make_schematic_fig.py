from optimization.diffusion_objective import DiffusionObjective
from input_data.dataset import Dataset
import torch as torch
import pandas as pd
import os
import numpy as np
from utils.plot_results_schematic import plot_results_schematic
from optimization.optimization_routines import diffEV_multiples
from utils.save_results import save_results
from utils.organize_x import organize_x

# get this file's directory
dir_path = os.path.dirname(os.path.realpath(__file__))

data_input = pd.read_csv(f"{dir_path}/input_GR27_feldspar_in.csv")
lnd0aa_bounds = (
    -5,
    50,
)  # The user should really be able to pick any numerical values they want here (Good to list its in units of 1/s)
Ea_bounds = (
    50,
    500,
)  # User should also be able to pick any number >0 for these bounds. List in kJ/mol
# mineral_name = "kspar"
time_add = []  # Add extra time in seconds
temp_add = [] # Add extra time in degrees C
sample_name = "GR27_few" # Sample name
max_domains_to_model = 8
geometry = "plane sheet"  # options are "plane sheet", or "spherical". Spherical should be default.
omit_value_indices = [32,33,34,35,36,37,38
]  # Values you want to be ignored in your fit


dataset = Dataset("diffEV", data_input)

misfit_stat = "percent_frac"
objective = DiffusionObjective(
    dataset,
    time_add=torch.tensor(time_add),
    temp_add=torch.tensor(temp_add),
    omitValueIndices=omit_value_indices,
    stat=misfit_stat,
    geometry=geometry,
    punish_degas_early = False
)

#This is intermed fit
#params = [1.73365444341471E-13, 3.91457517581200E+02,	4.62200768821121E+01,	3.90180663316288E+01	,3.28200751498657E+01,	2.72285786410262E+01	,2.24478990017536E+01	,6.93795393437542E+00,	4.81875188588035E+00,	2.22805911996708E-01,	6.39612889665484E-02,	9.76777710994787E-02,	3.73290912608320E-02	,1.98939822739980E-01,	3.52387260186070E-01,	7.29078123887070E-02,	4.66218454753439E-02]


# Make sure to use N-1 fracs!!!!! 

#this is worst fit
params1 = [335.567569632889	,39.146708523014,	30.172067488491	,29.664945364352	,21.426549193225	,17.402606427365	,15.964857224130,	6.284379579256,	-1.294279037535	,0.040535788100,	0.090277919616,	0.039701739596,	0.130310332905	,0.315146514821	,0.119667233118	,0.064814470901]

#This is intermed fit, I think.
params10_iters = [230.29062270957700,	26.32738565111700,	21.01574544927630,	18.67933154744840,	15.06584155918690	,13.01063165853310,	10.21103524972350	,2.48250506541692,	2.08754725778547,	0.01466558806171,	0.09944617583433,	0.09633836659125,	0.08881280810348,	0.10831924375069,	0.25398035235847,	0.15386570956638]	


#This is the best fit
params2 = [203.4051170073080,	22.1030687809260,	17.0748149047615	,15.0706445401833,	11.9060986689941	,9.3202365368750	,7.5105734475051,	7.0419866850301,	-2.1777011006856	,0.0120768431131	,0.1113516525620	,0.0886579646641	,0.1193161196527,	0.1273228207440	,0.0664113825405	,0.1781775180193]





plot_results_schematic(
    params2,
    dataset,
    objective,
    params10_iters,
    plot_path = dir_path+"/schematic_fig",
    params3 = params1
    
)





