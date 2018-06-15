from django.shortcuts import render, redirect
from .models import Information
from django.http import HttpResponse

import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
import pydotplus

# Create your views here.

def ssl(request):
    return HttpResponse("0JKalS3lyVNq3gtVJDo27ytKHyOpx85aNhp2xfb7peE.wikKX2g8tw-P0l1b-2vXfe4QbK5TIo1sKBYnIMeI7J0")

def home(request):

	Asthma_Information = Information.objects.all()
	context = {'Asthma_Information': Asthma_Information}
	
	if request.method == "POST":

		posted_age = request.POST.get("age", "")
		posted_gender = request.POST.get("gender", "")
		posted_smoking= request.POST.get("smoking", "")
		posted_BH = request.POST.get("BH", "")
		posted_BW = request.POST.get("BW", "")
		posted_allergy = request.POST.get("allergy", "")
		posted_IgE = request.POST.get("IgE", "")
		posted_rhinosinusitis = request.POST.get("rhinosinusitis", "")
		posted_PFT = request.POST.get("PFT", "")
		posted_FVC = request.POST.get("FVC", "")
		posted_FEV1 = request.POST.get("FEV1", "")
		posted_PAH = request.POST.get("PAH", "")

		result = analysis(posted_age, posted_gender, posted_smoking, posted_BH, posted_BW, posted_allergy, posted_IgE, posted_rhinosinusitis, posted_PFT, posted_FVC, posted_FEV1, posted_PAH)			
		
		Asthma_Information = Information.objects.create(
			age = posted_age,
			gender = posted_gender,
			smoking = posted_smoking,
			BH = posted_BH,
			BW = posted_BW,
			allergy = posted_allergy,
			IgE = posted_IgE,
			rhinosinusitis = posted_rhinosinusitis,
			PFT = posted_PFT,
			FVC = posted_FVC,
			FEV1 = posted_FEV1,
			PAH = posted_PAH,
			)
		Asthma_Information.save()

		return render(request, "data_input.html", context)
	return render(request, "data_input.html", context)

def user(request):

	Asthma_Information = Information.objects.all()
	context = {'Asthma_Information': Asthma_Information}

	if request.method == "POST":
		
		posted_age = request.POST.get("age", "")
		posted_gender = request.POST.get("gender", "")
		posted_smoking= request.POST.get("smoking", "")
		posted_BH = request.POST.get("BH", "")
		posted_BW = request.POST.get("BW", "")
		posted_allergy = request.POST.get("allergy", "")
		posted_IgE = request.POST.get("IgE", "")
		posted_rhinosinusitis = request.POST.get("rhinosinusitis", "")
		posted_PFT = request.POST.get("PFT", "")
		posted_FVC = request.POST.get("FVC", "")
		posted_FEV1 = request.POST.get("FEV1", "")
		posted_PAH = request.POST.get("PAH", "")

		BMI = float(float(posted_BW) / (( float(posted_BH) / 100.0 ) ** 2.0))
		FF = float(float(posted_FEV1) / float(posted_FVC) * 100.0)
		
		df = pd.DataFrame(pd.read_excel("D:/Django/Asthma_app/templates/data/CGMH_152-1.xlsx"))
		df = df.dropna(axis=0, how='any')

		# 將氣喘狀態欄位歸為y,其餘欄位為X
		y = df.iloc[:,-1]
		X = df.iloc[:,:-1]
		
		#使用決策樹分析
		dt = tree.DecisionTreeClassifier(max_depth=8)
		dt.fit(X, y)
		clf = dt.fit(X, y)
		DT_list = clf.predict_proba([[int(posted_age), int(posted_gender), int(posted_smoking), float(posted_BH), float(posted_BW), BMI, int(posted_allergy), float(posted_IgE), int(posted_rhinosinusitis), int(posted_PFT), float(posted_FVC), float(posted_FEV1), FF, float(posted_PAH)]]) #實際數值
		DT_list = DT_list[0].tolist()
		for i in range(len(DT_list)):
			if(DT_list[i] == 1.0):
				DT_result = i

		#使用隨機森林分析
		rf = RandomForestClassifier(n_estimators=139, criterion="entropy", random_state=0, max_depth=None, bootstrap=False)
		rf.fit(X, y)
		Estimators = rf.estimators_
		for index, rf in enumerate(Estimators):
			filename = 'RandomForest.pdf'
		RF_list = rf.predict_proba([[int(posted_age), int(posted_gender), int(posted_smoking), float(posted_BH), float(posted_BW), BMI, int(posted_allergy), float(posted_IgE), int(posted_rhinosinusitis), int(posted_PFT), float(posted_FVC), float(posted_FEV1), FF, float(posted_PAH)]]) #實際數值
		RF_list = RF_list[0].tolist()
		for i in range(len(RF_list)):
			if(RF_list[i] == 1.0):
				RF_result = i

		Asthma_Information = Information.objects.create(
			age = posted_age,
			gender = posted_gender,
			smoking = posted_smoking,
			BH = posted_BH,
			BW = posted_BW,
			allergy = posted_allergy,
			IgE = posted_IgE,
			rhinosinusitis = posted_rhinosinusitis,
			PFT = posted_PFT,
			FVC = posted_FVC,
			FEV1 = posted_FEV1,
			PAH = posted_PAH,
			)
		Asthma_Information.save()

	return render(request, "visitor.html", locals())

def index(request):

	Asthma_Information = Information.objects.all()
	context = {'Asthma_Information': Asthma_Information}
	
	if request.method == "POST":

		posted_age = request.POST.get("age", "")
		posted_gender = request.POST.get("gender", "")
		posted_smoking= request.POST.get("smoking", "")
		posted_BH = request.POST.get("BH", "")
		posted_BW = request.POST.get("BW", "")
		posted_allergy = request.POST.get("allergy", "")
		posted_IgE = request.POST.get("IgE", "")
		posted_rhinosinusitis = request.POST.get("rhinosinusitis", "")
		posted_PFT = request.POST.get("PFT", "")
		posted_FVC = request.POST.get("FVC", "")
		posted_FEV1 = request.POST.get("FEV1", "")
		posted_PAH = request.POST.get("PAH", "")
		
		result = analysis(posted_age, posted_gender, posted_smoking, posted_BH, posted_BW, posted_allergy, posted_IgE, posted_rhinosinusitis, posted_PFT, posted_FVC, posted_FEV1)
		
		Asthma_Information = Information.objects.create(
			age = posted_age,
			gender = posted_gender,
			smoking = posted_smoking,
			BH = posted_BH,
			BW = posted_BW,
			allergy = posted_allergy,
			IgE = posted_IgE,
			rhinosinusitis = posted_rhinosinusitis,
			PFT = posted_PFT,
			FVC = posted_FVC,
			FEV1 = posted_FEV1,
			PAH = posted_PAH,
			)
		Asthma_Information.save()
		
	return render(request, "index.html", locals())

def analysis(posted_age, posted_gender, posted_smoking, posted_BH, posted_BW, posted_allergy, posted_IgE, posted_rhinosinusitis, posted_PFT, posted_FVC, posted_FEV1, posted_PAH):

	#os.environ["PATH"] += os.pathsep + 'graphviz/bin' # graphviz位置

	df = pd.DataFrame(pd.read_excel("D:/Django/Asthma_app/templates/data/CGMH_152-1.xlsx"))
	df = df.dropna(axis=0, how='any')

	# 將氣喘狀態欄位歸為y,其餘欄位為X
	y = df.iloc[:,-1]
	X = df.iloc[:,:-1]

	#使用決策樹分析
	dt = tree.DecisionTreeClassifier(max_depth=8)
	dt.fit(X, y)
	BMI = float(float(posted_BW) / (( float(posted_BH) / 100.0 ) ** 2.0))
	FF = float(float(posted_FEV1) / float(posted_FVC) * 100.0)
	# 预测實際數值
	clf = dt.fit(X, y)
	list = clf.predict_proba([[int(posted_age), int(posted_gender), int(posted_smoking), float(posted_BH), float(posted_BW), BMI, int(posted_allergy), float(posted_IgE), int(posted_rhinosinusitis), int(posted_PFT), float(posted_FVC), float(posted_FEV1), FF, float(posted_PAH)]])  #實際數值
	list = list[0].tolist()
	for i in range(len(list)):
		if(list[i] == 1.0):
			result = i
	return result