from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, TourismForm
from .ml_model import logic_layer
from django.contrib import messages
import os

from .static.sergio.bayes import *
from .static.ruben.predict import *
from .static.clustering.hierarchical import *

# Create your views here.
res = None

def index(request):
    return render(request=request,
                  template_name='main/index1.html')

def predict(request):
    return render(request=request,
                  template_name='main/predict.html', context={"tourist": res})


def index2(request):
    if request.method == 'POST':
        form = TourismForm(request.POST)

        if form.is_valid():

            file1 = open('./main/data/sintomas', 'r')
            Lines = file1.readlines()
            sintomas = []
            # Strips the newline character
            for line in Lines:
                sintomas.append(line.strip())
            datos=[]

            for s in sintomas:
                datos.append(float(form.cleaned_data[s]))
                #df[s]=float(form.cleaned_data[s])

            datos_neuro=datos.copy()
            datos_neuro.append(float(form.cleaned_data['comorbidities_complete']))

            sintomas_neuro=[]
            sintomas_neuro=sintomas.copy()
            sintomas_neuro.append('comorbidities_complete')






            df = pd.DataFrame([datos_neuro], columns=sintomas_neuro)




            print(df)

            resultadoBayes = bayesianNet(datos)
            print(resultadoBayes)

            resultneu=neuronal(df)
            #clustering()
            return render(request=request, template_name='main/predict.html', context={"resultadoBayes": resultadoBayes[0],"resultneu":resultneu[0][0]})
            #redirect("/predict",resultadoBayes= resultadoBayes)
        else:
            problem = form.errors.as_data()
            # This section is used to handle invalid data
            messages.error(request, list(list(problem.values())[0][0])[0])
            form = TourismForm()
    form = TourismForm()
    return render(request=request, template_name='main/index2.html', context={"form": form})


def about(request):
    return render(request=request,
            template_name="main/about.html")


def under_construction(request):
    messages.info(request, "This page coming soon..")
    return render(request=request,
            template_name="main/under_construction.html")


















'''
smokers_home =form.cleaned_data['smokers_home']
sympt_epi=form.cleaned_data['sympt_epi']
#housemember_symptoms___1=form.cleaned_data['housemember_symptoms___1']
home_confirmed=form.cleaned_data['home_confirmed']
school_symptoms=form.cleaned_data['school_symptoms']
#school_symptoms_member___1=form.cleaned_data['school_symptoms_member___1']
#school_symptoms_member___2=form.cleaned_data['school_symptoms_member___2']
#school_symptoms_member___4=form.cleaned_data['school_symptoms_member___4']
school_confirmed=form.cleaned_data['school_confirmed']
fever=form.cleaned_data['fever']
highest_fever=form.cleaned_data['highest_fever']
tos=form.cleaned_data['tos']
dysphonia=form.cleaned_data['dysphonia']
resp=form.cleaned_data['resp']
ausc_resp=form.cleaned_data['ausc_resp']
odynophagia=form.cleaned_data['odynophagia']
nasal_congestion=form.cleaned_data['nasal_congestion']
fatiga=form.cleaned_data['fatiga']
headache=form.cleaned_data['headache']
conjuntivitis=form.cleaned_data['conjuntivitis']
gi_symptoms=form.cleaned_data['gi_symptoms']
abdominal_pain=form.cleaned_data['abdominal_pain']
vomiting=form.cleaned_data['vomiting']
dyarrea=form.cleaned_data['dyarrea']
dermatologic=form.cleaned_data['dermatologic']
hepato=form.cleaned_data['hepato']
splenomegaly=form.cleaned_data['splenomegaly']
hemorrhagies=form.cleaned_data['hemorrhagies']
neuro=form.cleaned_data['neuro']
shock=form.cleaned_data['shock']
taste_smell=form.cleaned_data['taste_smell']
smell=form.cleaned_data['smell']
pulmonar_disease___1=form.cleaned_data['pulmonar_disease___1']
asma___1=form.cleaned_data['asma___1']
nephrology___1=form.cleaned_data['nephrology___1']
hepatic___1=form.cleaned_data['hepatic___1']
neurologic___1=form.cleaned_data['neurologic___1']
diabetes___1=form.cleaned_data['diabetes___1']
idp___1=form.cleaned_data['idp___1']
neoplasia___1=form.cleaned_data['neoplasia___1']
vih_others___1=form.cleaned_data['vih_others___1']
flu_binary=form.cleaned_data['flu_binary']
vaccines_binary=form.cleaned_data['vaccines_binary']
comorbidities_complete=form.cleaned_data['comorbidities_complete']
num_fever=form.cleaned_data['num_fever']

'''
