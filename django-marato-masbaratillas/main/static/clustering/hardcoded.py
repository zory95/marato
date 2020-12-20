import pandas as pd

df = pd.read_csv('./main/data/covid-cleaned.csv', index_col='participant_id')

df = df.fillna(0) #.applymap(lambda x: 0 if x == 0.5 else x)
df['final_diagnosis_code'] = df['final_diagnosis_code'].apply(lambda x: 0 if x!=1 else x)

smokers = df['smokers_home'] != 0

positive = (df['final_diagnosis_code'] == 1)

family = (df['sympt_epi'] != 0) | (df['housemember_symptoms___1'] != 0) | (df['home_confirmed'] != 0)
school = (df['school_symptoms'] != 0) | (df['school_symptoms_member___1'] != 0) \
         | (df['school_symptoms_member___2'] != 0) | (df['school_symptoms_member___4'] != 0) \
         | (df['school_confirmed'] != 0)

fever = df['fever'] != 0
tos = df['tos'] != 0
fatiga = df['fatiga'] != 0
odynophagia = df['odynophagia'] != 0
headache = df['headache'] != 0
resp = df['resp'] != 0
hepato = df['hepato'] != 0
splenomegaly = df['splenomegaly'] != 0
neuro = df['neuro'] != 0
shock = df['shock'] != 0
taste = df['taste_smell'] != 0
smell = df['smell'] != 0
hemorrhagies = df['hemorrhagies'] != 0
conjuntivitis = df['conjuntivitis'] != 0
gi_symptoms = df['gi_symptoms'] != 0
nasal_congestion = df['nasal_congestion'] != 0
abdominal_pain = df['abdominal_pain'] != 0
dyarrea = df['dyarrea'] != 0
dermatologic = df['dermatologic'] != 0
vomiting = df['vomiting'] != 0

many = tos & resp & odynophagia & nasal_congestion & fatiga & headache

print(len(df[~positive]), len(df[positive]))

SET_A = (family & school) & fever
A = df[SET_A & ~positive]
AA = df[SET_A & positive]
print(len(A), len(AA))

SET_B = family & school & odynophagia & hepato & splenomegaly
B = df[SET_B & ~positive]
BB = df[SET_B & positive]
print(len(B), len(BB))

SET_C = fever & many & smell
C = df[SET_C & ~positive]
CC = df[SET_C & positive]
print(len(C), len(CC))

SET_D = (family | school) & neuro & taste & smell
D = df[SET_D & ~positive]
DD = df[SET_D & positive]
print(len(D), len(DD))

SET_E = smokers & dermatologic & hepato & headache
E = df[SET_E & ~positive]
EE = df[SET_E & positive]
print(len(E), len(EE))

SET_F = neuro & shock & taste & smell & gi_symptoms & dermatologic
F = df[SET_F & ~positive]
FF = df[SET_F & positive]
print(len(F), len(FF))

SET_G = hepato & splenomegaly & headache & fatiga
G = df[SET_G & ~positive]
GG = df[SET_G & positive]
print(len(G), len(GG))

SET_H = family & abdominal_pain & fever
H = df[SET_H & ~positive]
HH = df[SET_H & positive]
print(len(H), len(HH))

SET_I = family & abdominal_pain & headache & vomiting
I = df[SET_I & ~positive]
II = df[SET_I & positive]
print(len(I), len(II))

SET_J = family & abdominal_pain & headache & fatiga
J = df[SET_J & ~positive]
JJ = df[SET_J & positive]
print(len(JJ), len(JJ))

SET_K = family & abdominal_pain & hepato & splenomegaly
K = df[SET_K & ~positive]
KK = df[SET_K & positive]
print(len(K), len(KK))

joint = df[(SET_A | SET_B | SET_C | SET_D | SET_E | SET_F | SET_G | SET_H | SET_I | SET_J | SET_K) & ~positive]
joint_pos = df[(SET_A | SET_B | SET_C | SET_D | SET_E | SET_F | SET_G | SET_H | SET_I | SET_J | SET_K) & positive]
print(len(joint), len(joint_pos))

print(len(joint)/len(df[~positive]), len(joint_pos)/len(df[positive]))
