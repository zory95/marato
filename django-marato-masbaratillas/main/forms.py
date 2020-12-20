from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

SI_NO = [
    ('0', 'Select'),
    ('1', 'Si'),
    ('2', 'No')
]
FEVER = [
    ('0', 'Select'),
    ('1', '37.5-38'),
    ('2', '38-39'),
    ('3', '>39')

]
SI_NO_DES = [
    ('0', 'Select'),
    ('1', 'Si'),
    ('2', 'No'),
    ('0.5', 'Desconocido')
]

NOR_PAT = [
    ('0', 'Select'),
    ('1', 'Normal'),
    ('2', 'Patología')
]
IN_UN_COM = [
    ('0', 'Incomplete'),
    ('1', 'Unverified'),
    ('2', 'Complete')
]
class TourismForm(forms.Form):

    smokers_home= forms.CharField(label="Fumadores en casa", widget=forms.Select(choices=SI_NO))
    sympt_epi= forms.CharField(label="Sintomáticos en casa", widget=forms.Select(choices=SI_NO))
    housemember_symptoms___1=forms.CharField(label="Padre sintomático", widget=forms.Select(choices=SI_NO))
    home_confirmed= forms.CharField(label="Confirmados de COVID-19 en casa", widget=forms.Select(choices=SI_NO))
    school_symptoms= forms.CharField(label="Sintomáticos en la escuela", widget=forms.Select(choices=SI_NO))
    school_symptoms_member___1=forms.CharField(label="Profesor sintomático en la escuela", widget=forms.Select(choices=SI_NO))
    school_symptoms_member___2=forms.CharField(label="Alumno de la misma clase sintomático en la escuela", widget=forms.Select(choices=SI_NO))
    school_symptoms_member___4=forms.CharField(label="Otras personas sintomáticas en la escuela", widget=forms.Select(choices=SI_NO))
    school_confirmed=forms.CharField(label="Confirmados de COVID-19 en la escuela", widget=forms.Select(choices=SI_NO))
    fever= forms.CharField(label="Tiene fiebre", widget=forms.Select(choices=SI_NO))
    highest_fever= forms.CharField(label="Fiebre más alta", widget=forms.Select(choices=FEVER))
    tos= forms.CharField(label="Tos", widget=forms.Select(choices=SI_NO_DES))
    dysphonia= forms.CharField(label="Disfonía", widget=forms.Select(choices=SI_NO_DES))
    resp= forms.CharField(label="Disnea", widget=forms.Select(choices=SI_NO_DES))
    ausc_resp= forms.CharField(label="Auscultación respiratoria", widget=forms.Select(choices=NOR_PAT))
    odynophagia= forms.CharField(label="odinofagia", widget=forms.Select(choices=SI_NO_DES))
    nasal_congestion= forms.CharField(label="Congestión nasal", widget=forms.Select(choices=SI_NO_DES))
    fatiga= forms.CharField(label="Fatiga", widget=forms.Select(choices=SI_NO_DES))
    headache= forms.CharField(label="Dolor de cabeza", widget=forms.Select(choices=SI_NO_DES))
    conjuntivitis= forms.CharField(label="conjuntivitis", widget=forms.Select(choices=SI_NO_DES))
    gi_symptoms= forms.CharField(label="Síntomas gastrointestinales", widget=forms.Select(choices=SI_NO))
    abdominal_pain= forms.CharField(label="Dolor abdominal", widget=forms.Select(choices=SI_NO_DES))
    vomiting= forms.CharField(label="Vómitos", widget=forms.Select(choices=SI_NO_DES))
    dyarrea= forms.CharField(label="Diarrea", widget=forms.Select(choices=SI_NO_DES))
    dermatologic= forms.CharField(label="manifestaciones dermatológicas", widget=forms.Select(choices=SI_NO))
    hepato= forms.CharField(label="Hepatomegalia", widget=forms.Select(choices=SI_NO_DES))
    splenomegaly= forms.CharField(label="Esplenomegalia", widget=forms.Select(choices=SI_NO_DES))
    hemorrhagies= forms.CharField(label="Hemorragias", widget=forms.Select(choices=SI_NO_DES))
    neuro= forms.CharField(label="Manifestaciones neurológicas", widget=forms.Select(choices=SI_NO))
    shock= forms.CharField(label="Shock", widget=forms.Select(choices=SI_NO))
    taste_smell= forms.CharField(label="Alteración del gusto", widget=forms.Select(choices=SI_NO))
    smell= forms.CharField(label="Alteración del olfato", widget=forms.Select(choices=SI_NO))
    #comorbi_binary= forms.CharField(label="Comorbilidad", widget=forms.Select(choices=SI_NO))
    #cardiopathy___1= forms.CharField(label="Cardiopatia", widget=forms.Select(choices=SI_NO_DES))
    #hypertension___1= forms.CharField(label="Hipertensión en la escuela", widget=forms.Select(choices=SI_NO_DES))
    pulmonar_disease___1= forms.CharField(label="Enfermedad pulmonar", widget=forms.Select(choices=SI_NO_DES))
    asma___1= forms.CharField(label="Asma", widget=forms.Select(choices=SI_NO_DES))
    nephrology___1= forms.CharField(label="Nefrología", widget=forms.Select(choices=SI_NO_DES))
    hepatic___1= forms.CharField(label="Hepático/a", widget=forms.Select(choices=SI_NO_DES))
    neurologic___1= forms.CharField(label="Neurológico/a", widget=forms.Select(choices=SI_NO_DES))
    diabetes___1= forms.CharField(label="Diabético/a", widget=forms.Select(choices=SI_NO_DES))
    idp___1= forms.CharField(label="Inmunodeficiencia primaria", widget=forms.Select(choices=SI_NO_DES))
    neoplasia___1= forms.CharField(label="Neoplasia", widget=forms.Select(choices=SI_NO_DES))
    vih_others___1= forms.CharField(label="VIH", widget=forms.Select(choices=SI_NO_DES))
    flu_binary= forms.CharField(label="Ha recibido la vacuna de la gripe", widget=forms.Select(choices=SI_NO))
    vaccines_binary= forms.CharField(label="Vacunas de rutina actualizadas", widget=forms.Select(choices=SI_NO))
    comorbidities_complete= forms.CharField(label="Estado de la  Comorbilidad", widget=forms.Select(choices=IN_UN_COM))
    num_fever= forms.CharField(label="Días con fiebre", widget=forms.NumberInput(attrs={'min': 0, 'max': 15, 'type': 'number',}))
