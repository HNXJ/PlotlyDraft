import Datasets
import Methods
import Connect
import Viewer

import Learning
import Representational

import numpy as np
import pandas as pd
import warnings


##############################################################################


warnings.filterwarnings("ignore")

# dataset = Datasets.Dataset()
# dataset.load_laminar_data(path="Data/")
# dataset.print_all_content()
# trials_block = dataset.get_trials(key='block', l=0, r=600)
# trials_trial = dataset.get_trials(key='trial', l=0, r=600)
trials = [i for i in range(0, 600, 1)]

##############################################################################

sample_inds = []*6

for i in trials:
    if dataset.cue_s[i] == 1 and dataset.cue_cr[i] == 0: # pred & A
        sample_inds[0].append(i)
    if dataset.cue_s[i] == 2 and dataset.cue_cr[i] == 0: # pred & B
        sample_inds[0].append(i)
    if dataset.cue_s[i] == 3 and dataset.cue_cr[i] == 0: # pred & C
        sample_inds[0].append(i)
    if dataset.cue_s[i] == 1 and dataset.cue_cr[i] == 1: # unpred & A
        sample_inds[0].append(i)
    if dataset.cue_s[i] == 2 and dataset.cue_cr[i] == 1: # unpred & B
        sample_inds[0].append(i)
    if dataset.cue_s[i] == 3 and dataset.cue_cr[i] == 1: # unpred & C
        sample_inds[0].append(i)
        
### TODO: RSA/RDM test 2X3 -> 6 class 

# trials = [i for i in range(0, 100, 1)]
# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-1000ms.txt")
# [tsc] = Datasets.load_list("Data/1-600-tsc-1000ms.txt")
# [tgc, times] = Datasets.load_list("Data/1-600-tgc-250ms.txt")

# rdm_ = Representational.time_rdm(x=tsc, p_dim=3, t_dim=0, trials=trials)

# Representational.time_rdm_plot(rdm_, title="RDM", dlabel="Trials", times=times)

###############################################################################