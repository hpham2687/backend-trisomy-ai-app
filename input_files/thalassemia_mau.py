from pydantic import BaseModel
import json
import pandas as pd
import pickle
import numpy as np
from utils import NumpyEncoder,Model_input_12
def predict(input_param:Model_input_12):
    str=json.loads(input_param)
    scale1 = open('/root/Thalasemia/models_thalassemia/Model1/scaler7ts.pkl','rb')
    model1_path = open('/root/Thalasemia/models_thalassemia/Model1/lgbm7ts.sav','rb')
    scale2 =open('/root/Thalasemia/models_thalassemia/Model2/scaler7ts.pkl','rb')
    model2_path = open('/root/Thalasemia/models_thalassemia/Model2/lgbm7ts.sav','rb')
    sc1=pickle.load(scale1)
    scale1.close()
    sc2=pickle.load(scale2)
    scale2.close()
    model1=pickle.load(model1_path)
    model1_path.close()
    model2=pickle.load(model2_path)
    model2_path.close()
    input=[[str['ctm_rbc'],str['ctm_hgb'],str['ctm_hct'],str['ctm_mcv'],str['ctm_mch'],str['ctm_mchc'],str['ctm_rdw']]]
    input=np.array(input).reshape(1,-1)
    input1=sc1.transform(input)
    
    pred_kha_nang_mac_benh=model1.predict_proba(input1)[:,1][0]
    input2 =sc2.transform(input)
    pred_alpha_beta=model2.predict_proba(input2)[:,1][0]
    pred_alpha=pred_alpha_beta
    pred_beta=1-pred_alpha_beta
    datadict={
        "noGen":1-pred_kha_nang_mac_benh,
        "gen":pred_kha_nang_mac_benh,
        "betaGen":pred_beta,
        "alphaGen":pred_alpha
    }
    kl=json.loads(json.dumps(datadict,indent=4,cls=NumpyEncoder))
    return kl
