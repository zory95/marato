import pandas as pd

input_vars = ["survey_type","home_confirmed","school_confirmed","school_symptoms","sympt_epi","housemember_symptoms___1",
              "housemember_symptoms___2", "housemember_symptoms___3", "housemember_symptoms___4",
              "housemember_symptoms___5", "resp", "tachypnea", "nasal_congestion", "highest_fever","tos",
              "cough_first","crup","crup_first","dysphonia","disfonia_first","nasal_congestion","nasal_first",
              "fatiga","fatigue_first","headache","headache_first","conjuntivitis","conj_first","ocular_pain",
              "ocular_first","gi_symptoms","gi_first","abdominal_pain","vomiting","dyarrea","dermatologic","skin_first",
              "rash","inflam_periferic","inflam_oral","adenopathies","lymph_first","hepato","hepato_first","splenomegaly",
              "spleno_first","hemorrhagies","hemorr_first","irritability","irritability_first","neuro","neuro_first",
              "confusion","seizures","nuchal_stiffness","hypotonia","peripheral_paralysis","shock","shock_first",
              "taste_smell", "smell", "smell_first"]
output_var = "covid"

def get_data(file):
    data = pd.read_csv(file).ffill().fillna(0)
    data2 = data["final_diagnosis_code"].transform(lambda x: x == 1)
    data.insert(0,"covid",data2)
    return data


if __name__ == "__main__":
    data = get_data("data/COPEDICATClinicSympt_DATA_2020-12-17_1642.csv")
    pd.set_option('display.max_columns', 2000)
    print(data)
