import sklearn.datasets
import pandas as pd

iris_data = sklearn.datasets.load_iris()
iris_data = pd.DataFrame(data=iris_data['data'], columns=iris_data['feature_names'])
iris_data.to_csv('./iris_data.csv')