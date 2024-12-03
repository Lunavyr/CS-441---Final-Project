# Procedure
This page outlines our process for expanding upon the results of Huang.

## Overview:
1. Create an environment to properly run the researchers source code.

2. Implement a BRNN with the same input so as to leverage the existing source code.

3. Create Jupyter notebooks for each combination of model and optimizer and output results.

## Breakdown:
1. Following the steps described in Setup.md, establish an anaconda environment with the provided "env.yml" file.

2. Inject all of the code in ./Code/BRNN.py into the researchers source code "SourceCode"/DLModel.py.  
This preserves the self-same interface which allows the source project to be leveraged with the novel RNN type, and allows cross-examination between models and optimizers

3. In ./Code/ there are Jupyter Notebooks used to generate data from each of our selected sets of model and optimizer.  
Again, this is a slight adaptation from the source material provided.  
(* Note the intermediate data in "Source Programs"/data/token/SARD needs to be periodically deleted in order to allow the program to regenerate token slices due to name collision during generation)