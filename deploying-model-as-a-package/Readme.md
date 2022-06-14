# arnold-house-price-regression-model
This is a python package that help predict house prices using [House price data from Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data). This package was built for learning purpose

## Set-up
### Install Dev Dependencies
``` 
pip install -r requirements/requirements.txt
```
### Install Test Dependencies 
```
pip install -r requirements/test_requirements.txt
```
### Train model 
``` 
tox -e train
```
### Run test
```
tox -e test_package
```

### Published Package 
[You can find publish package here](https://pypi.org/project/arnold-house-price-regression-model/0.0.1/)
```
pip install arnold-house-price-regression-model
from arnold-house-price-regression-model import make_prediction
results = make_prediction(test_dataframe)
```



