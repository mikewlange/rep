from __future__ import division, print_function, absolute_import

from .interface import Classifier, Regressor
from .sklearn import SklearnClassifier, SklearnRegressor

try:
    from .tmva import TMVAClassifier, TMVARegressor
except:
    pass

try:
    from .xgboost import XGBoostClassifier, XGBoostRegressor
except:
    pass

try:
    from .nolearn import NolearnClassifier
except:
    pass
