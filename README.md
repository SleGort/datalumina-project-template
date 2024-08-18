# Data Project Template

## Cookiecutter Data Science
This project template is a simplified version of the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org) template, created to suit the needs of Datalumina and made available as a GitHub template.

## Duplicating the .env File
To set up your environment variables, you need to duplicate the `.env.example` file and rename it to `.env`. You can do this manually or using the following terminal command:

```bash
cp .env.example .env # Linux, macOS, Git Bash, WSL
copy .env.example .env # Windows Command Prompt
```

This command creates a copy of `.env.example` and names it `.env`, allowing you to configure your environment variables specific to your setup.

## Adding Root Folder to Python's Module Search Path

If you're having trouble importing modules in a notebook or script, use this code to add the parent directory to the module search path:

```python
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
```
or alternatively:

```python
from pathlib import Path

# Get the root directory of the project
project_root = Path(__file__).parent.parent.absolute()
```

These code snippets assumes that the folder is directly below the parent folder. If you have nested subfolders you might want to call `os.path.dirname()` a couple of times.

## Project Organization
```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── external       <- Data from third-party sources
│   ├── interim        <- Intermediate data that has been transformed, data in this directory
│   │                     is what would be called for any feature engineering. (separate files)
│   ├── processed      <- The final, canonical data sets for modeling
│   ├── raw            <- The original, immutable data dump
│   └── test_set       <- Final test set, kept locked until model selection is complete.
│                         Only to be used for final generalization performance testing.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                         <- Source code for this project
   ├── __init__.py             <- Makes src a Python module
   ├── config.py               <- Store useful variables and configuration
   ├── dataset.py              <- Scripts to download or generate data
   ├── features.py             <- Code to create features for modeling
   ├── modeling                
   │   ├── __init__.py 
   │   ├── predict.py          <- Code to run model inference with trained models          
   │   └── train.py            <- Code to train models
   ├── plots.py                <- Code to create visualizations 
   └── services                <- Service classes to connect with external platforms, tools, or APIs
       └── __init__.py

                         
```
## Workflow

### Naming Convention
Files should be named using the following convention: `number-initials-description`, where:
- `number` is for ordering,
- `initials` are the creator's initials,
- `description` is a short, hyphen-separated summary.

**Example**: `1.0-jqp-initial-data-exploration`

### Processed Data Workflow
1. **Training Data**: Start with the full training dataset.
2. **Split**: Divide the data into a training set and a validation set.
3. **Validation**: Use the validation set to evaluate model generalizability during the model selection step.
4. **Model Selection**: Choose the best-performing model based on validation performance.
5. **Final Training**: Retrain the selected model using both the training and validation sets.
6. **Testing**: Apply the final model to the test set to evaluate its generalization performance.
7. **Production**: If the model performs well on the test set, consider moving it to production.

--------
