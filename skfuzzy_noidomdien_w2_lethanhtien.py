# -*- coding: utf-8 -*-
"""skfuzzy_noidomdien_w2_lethanhtien

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1szA4d0l1r6XlBwqbGDO24PHSEKYDGpk8
"""

pip install scikit-fuzzy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

time=ctrl.Antecedent(np.arange(10,401,0.5),'time')
rice=ctrl.Antecedent(np.arange(100,2001,0.5),'rice')
power=ctrl.Consequent(np.arange(0,101,0.5),'power')

time['rat cham']=fuzz.trimf(time.universe,(10,10,15))
time['cham']=fuzz.trimf(time.universe,(10,15,30))
time['trung binh']=fuzz.trimf(time.universe,(15,30,60))
time['nhanh']=fuzz.trimf(time.universe,(30,60,120))
time['rat nhanh']=fuzz.trimf(time.universe,(80,400,400))
rice['rat it']=fuzz.trimf(rice.universe,(100,100,200))
rice['it']=fuzz.trimf(rice.universe,(100,200,500))
rice['trung binh']=fuzz.trimf(rice.universe,(500,1000,1500))
rice['nhieu']=fuzz.trimf(rice.universe,(1000,1500,2000))
rice['rat nhieu']=fuzz.trimf(rice.universe,(1500,2000,2000))
power['rat yeu']=fuzz.trimf(power.universe,(0,0,20))
power['yeu']=fuzz.trimf(power.universe,(0,20,40))
power['trung binh']=fuzz.trimf(power.universe,(40,60,80))
power['manh']=fuzz.trimf(power.universe,(60,80,100))
power['rat manh']=fuzz.trimf(power.universe,(80,100,100))

rule1 = ctrl.Rule(time['rat nhanh'] & rice['rat it'],power['trung binh'])
rule2 = ctrl.Rule(time['rat nhanh'] & rice['it'],power['trung binh'])
rule3 = ctrl.Rule(time['rat nhanh'] & rice['trung binh'],power['manh'])
rule4 = ctrl.Rule(time['rat nhanh'] & rice['nhieu'],power['rat manh'])
rule5 = ctrl.Rule(time['rat nhanh'] & rice['rat nhieu'],power['rat manh'])
rule6 = ctrl.Rule(time['nhanh'] & rice['rat it'],power['trung binh'])
rule7 = ctrl.Rule(time['nhanh'] & rice['it'],power['trung binh'])
rule8 = ctrl.Rule(time['nhanh'] & rice['trung binh'],power['manh'])
rule9 = ctrl.Rule(time['nhanh'] & rice['nhieu'],power['manh'])
rule10 = ctrl.Rule(time['nhanh'] & rice['rat nhieu'],power['rat manh'])
rule11 = ctrl.Rule(time['trung binh'] & rice['rat it'],power['yeu'])
rule12 = ctrl.Rule(time['trung binh'] & rice['it'],power['yeu'])
rule13 = ctrl.Rule(time['trung binh'] & rice['trung binh'],power['trung binh'])
rule14 = ctrl.Rule(time['trung binh'] & rice['nhieu'],power['manh'])
rule15 = ctrl.Rule(time['trung binh'] & rice['rat nhieu'],power['manh'])
rule16 = ctrl.Rule(time['cham'] & rice['rat it'],power['rat yeu'])
rule17 = ctrl.Rule(time['cham'] & rice['it'],power['yeu'])
rule18 = ctrl.Rule(time['cham'] & rice['trung binh'],power['yeu'])
rule19= ctrl.Rule(time['cham'] & rice['nhieu'],power['trung binh'])
rule20 = ctrl.Rule(time['cham'] & rice['rat nhieu'],power['manh'])
rule21 = ctrl.Rule(time['rat cham'] & rice['rat it'],power['rat yeu'])
rule22 = ctrl.Rule(time['rat cham'] & rice['it'],power['rat yeu'])
rule23 = ctrl.Rule(time['rat cham'] & rice['trung binh'],power['yeu'])
rule24= ctrl.Rule(time['rat cham'] & rice['nhieu'],power['trung binh'])
rule25 = ctrl.Rule(time['rat cham'] & rice['rat nhieu'],power['trung binh'])

powerOn_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25])
powerOn=ctrl.ControlSystemSimulation(powerOn_ctrl)
powerOn.input['time']=60
powerOn.input['rice']=400
powerOn.compute()
print('power value:',powerOn.output['power'])
power.view(sim=powerOn)

