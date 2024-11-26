# Procedure:
This page documents our process for replicating the vulnerability detection research and creating our own model to compare against.

## Setup:

### Set up core directory:
*Since GitHub doesn't like large files, we have chosen to omit including the source project for this study.

1. Clone base project repo into folder "Source Programs".  
This folder should directly include the various python source files provided by the study as it will be referenced by our code later.

2. In the "Source Programs"/data/token, add a folder named SARD (This was probably omitted in the source repo since it represents intermediate data)

3. Clone the test data into a folder called "Source Data".



### Set up environment:
1. Download Anaconda from here: https://www.anaconda.com/download.  
When installing, make sure to add Anaconda to path variable.

2. Create and activate new Anaconda environment: 
```bash
conda create --name myenv python=3.7
conda activate myenv
```

3. In project directory, install Jupyter:
```bash
conda install jupyter
```

4. Install all required python packages specified in "Project_Documentation.pdf"  
e.g.
```bash
conda install xlrd=1.2.0
```
It is important that these versions all match the versions specified.  
You may also need to progressively install packages while running.

5. To make sure jupyter is using the correct python environment, enter the following in your current conda env:
```bash
conda install ipykernel
python -m ipykernel install --user --name your_env_name --display-name "Python (your_env_name)"
```

6. Run Jupyter Notebook and open "2_Application_Codes.ipynb"

7. In the notebook under the "Kernal" tab, select "Restart Kernel and Run All Cells..."
