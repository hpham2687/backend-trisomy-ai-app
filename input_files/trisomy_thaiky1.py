import json
from utils import Model_input_trisomy,NumpyEncoder
import pickle
import numpy as np

def predict(input_param:Model_input_trisomy):
    str=json.loads(input_param)
    model21=open('/root/Thalasemia/models_trisomy/trisomy21/double21ver5.sav','rb')
    m21=pickle.load(model21)
    model21.close()
    model18=open('/root/Thalasemia/models_trisomy/trisomy18/double18ver5.sav','rb')
    m18=pickle.load(model18)
    model18.close()
    model13=open('/root/Thalasemia/models_trisomy/trisomy13/double13ver5.sav','rb')
    m13=pickle.load(model13)
    model13.close()
    input=[[str['tuoi'],str['co_khoangsangsaugay'],str['co_nangbachhuyetvungco_1'],str['mat_xuongmui_1'],str['nguc_ditattim_1'],str['d_mom_hcgb'],str['d_mom_pappa'],str['d_mom_nt']]]
    input=np.array(input).reshape(1,-1)
    predict21=m21.predict_proba(input)[:,1][0]
    predict18=m18.predict_proba(input)[:,1][0]
    predict13=m13.predict_proba(input)[:,1][0]
    datadict={
        "Trisomy21":np.float64(predict21),
        "Trisomy18":np.float64(predict18),
        "Trisomy13":np.float64(predict13)
    }
    kl=json.loads(json.dumps(datadict,indent=4,cls=NumpyEncoder))
    return kl
