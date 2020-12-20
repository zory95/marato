#! /usr/local/bin/python
#coding: utf-8
import pandas as pd
import numpy as np
from sklearn import linear_model

def readFile(file):
    df = pd.read_csv (file)
    return df

def sintomas(file):
    file1 = open(file, 'r')
    Lines = file1.readlines()
    sintomas = []
    # Strips the newline character
    for line in Lines:
        sintomas.append(line.strip())
    return sintomas

def bayes(xvar,yvar):
    reg = linear_model.BayesianRidge()
    X = np.array(xvar)
    Y = np.array(yvar)
    reg.fit(X, Y)
    return reg

def prueba(reg):
    count=0
    for x in range(10000):
        prueba=np.random.randint(1,3,size=(41))
        #print(prueba)
        resultado=reg.predict([prueba])
        print (resultado[0])
        if resultado[0] >= 1.5:
            count=count+1
    print(count)




def predecir(reg,datos):
    return reg.predict([datos])


def bayesianNet(datos):
    df=readFile('./main/data/covid-cleaned.csv')
    columnas=sintomas('./main/data/sintomas')
    #print(count)
    #LinearRegression
    #columnas=['fever','tos','cough_first','crup']
    ejey=['final_diagnosis_code']
    df1 = df.fillna(0)
    df3 = df1[columnas]
    df2 = df1[ejey]
    reg = bayes(xvar=df3,yvar=df2)
    return predecir(reg,datos)




def main():
    '''
    df=readFile('marato/data/covid-cleaned.csv')
    columnas=sintomas('sintomas')
    #print(count)
    #LinearRegression
    #columnas=['fever','tos','cough_first','crup']
    ejey=['final_diagnosis_code']
    df1 = df.fillna(-1)
    df3 = df1[columnas]
    df2 = df1[ejey]

    reg = bayes(xvar=df3,yvar=df2)
    '''
    prueba=np.random.randint(1,3,size=(41))
    bayesianNet(prueba)


    #prueba(reg)



    #print(reg.coef_)
    '''
    for col in df.columns:
        print(col)
    '''
    #columnas=['fever','highest_fever','total_days_fever','tos','cough_first','crup']
    #print(df[columnas])


if __name__ == "__main__":
    main()
