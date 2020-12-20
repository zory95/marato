from scipy.cluster import hierarchy
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/covid-cleaned.csv', index_col='participant_id')

df = df.fillna(0)

df_posit = df.copy()
df_positive = df_posit.drop('final_diagnosis_code', axis=1)

axes1 = (0.1, 0.1, 0.15, 0.85)
axes2 = (axes1[0] + axes1[2], axes1[1], 0.65, axes1[3])
figsize = (10, 30)

f = plt.figure(figsize=figsize)

ax1 = f.add_axes(axes1)

y = pdist(df_positive)
link = hierarchy.ward(y)
link = hierarchy.optimal_leaf_ordering(link, y)
dg = hierarchy.dendrogram(link, labels=df_positive.index, orientation='left')
labels = ax1.get_yticklabels()
labels = [label.get_text() for label in labels]
ax1.set_yticks([])
ax1.set_xticks([])

df_positive['result'] = df_posit['final_diagnosis_code']

cols = df_positive.columns.values.tolist()

width = axes2[2]/len(cols)
left = axes2[0]
for col in cols:
    ax2 = f.add_axes((left, axes2[1], width, axes2[3]))
    left += width
    ax2.imshow(df_positive.loc[:, [col]].values, origin='lower', aspect='auto')
    ax2.set_xticks(range(1))
    ax2.set_xticklabels([col], rotation=90)
    ax2.set_yticks([])
ax2.yaxis.tick_right()
ax2.set_yticks(range(len(labels)))
ax2.set_yticklabels(labels)
plt.savefig('cluster.pdf')


