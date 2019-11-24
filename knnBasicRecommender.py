import numpy as np
from surprise import Dataset
from surprise.model_selection import cross_validate
from surprise.model_selection import KFold
from surprise import KNNBasic

# Load dataset
dataset = 'ml-100k'
data = Dataset.load_builtin(dataset)

# Set KFold validation and ensure random state remains consistent between all models
kf = KFold(n_splits=3, random_state = 0)

# Use RMS error and mean abs error as metrics
out = cross_validate(KNNBasic(), data, ['rmse', 'mae'], kf)

# Format outputs from surprise CV method out
meanTestRMSE = '{:.3f}'.format(np.mean(out['test_rmse']))
meanTestMAE = '{:.3f}'.format(np.mean(out['test_mae']))

# Print results
print("\nKNN Basic Recommender Model has achieved:")
print("    RMSE: " + meanTestRMSE)
print("    MAE : " + meanTestMAE)









