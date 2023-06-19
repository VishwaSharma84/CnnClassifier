echo [$(date)]: "START"
echo [$(date)]: "Creating python environment with 3.8 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "ACTIVATING ENVIRONMENT"
source activate ./env
echo [$(date)]: "installing requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"

