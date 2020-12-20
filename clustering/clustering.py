from scipy.cluster import hierarchy
from scipy.spatial.distance import pdist
import pandas as pd
import numpy as np


class PredictorClustering:
    def __init__(self, input_model, max_clusters=10):
        """
        :type input_model: pd.DataFrame or str
        """
        if type(input_model) == pd.DataFrame:
            self._model_df = input_model.copy()
        else:
            self._model_df = pd.read_csv(input_model)
            self._model_df.fillna(0)
            self._model_df = self._model_df.sample(frac=1).reset_index(drop=True)

        y = pdist(self._model_df)
        link = hierarchy.ward(y)
        link = hierarchy.optimal_leaf_ordering(link, y)
        clust_list = hierarchy.fcluster(link, max_clusters, criterion='maxclust')
        self._model_df['cluster'] = clust_list
        self._num_different_sets = len(set(clust_list))
        self._calculate_centers()

    def _calculate_centers(self):
        centers = []
        for cluster in range(1, self._num_different_sets + 1):
            list_points = self._model_df[self._model_df['cluster'] == cluster]
            center = list_points.sum(axis=1)/len(list_points)
            centers.append(center)
        self.centers = pd.concat(centers)

    def predict(self, input_data):
        if type(input_data) == dict:
            input_data = pd.DataFrame.from_dict(input_data)

        distances = []
        dist = np.linalg.norm(pd.concat((self.centers[:, self.centers.columns != 'final_diagnosis_code'].values,
                                         input_data[:, input_data.columns != 'final_diagnosis_code'].values)))
        print(dist)


def equal_sample(full_data, frac=1.0, seed=0):
    positives = full_data[full_data['final_diagnosis_code'] == 1]
    negatives = full_data[full_data['final_diagnosis_code'] == 0]

    rs = np.random.RandomState(seed=seed)

    positives = positives.sample(frac=1).reset_index(drop=True)
    negatives = negatives.sample(frac=1).reset_index(drop=True)

    positives_sample = positives.sample(frac=frac, random_state=rs)
    negatives_sample = negatives.sample(n=len(positives_sample), random_state=rs)
    model_df = pd.concat((positives_sample, negatives_sample))
    model_df = model_df.sample(frac=1, random_state=rs).reset_index(drop=True)

    return model_df


if __name__ == '__main__':
    full_data = pd.read_csv('../data/covid-cleaned.csv', index_col='participant_id')
    full_data.fillna(0)

    model_df = equal_sample(full_data)
    test = full_data[~full_data.isin(model_df)]

    pc = PredictorClustering(model_df, max_clusters=10)
    for idx, row in test.iterrows:
        pc.predict(row)
