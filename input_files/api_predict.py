from fastapi import FastAPI
import uvicorn
import json
from utils import Model_input_trisomy,Model_input_12
app=FastAPI()
@app.post('/thalassemia_predict')
def thalassemia(input_param:Model_input_12):
    """
    Input(json):
    +Chỉ số máu    
    ctm_rbc:float 
    ctm_hgb:float
    ctm_hct:float
    ctm_mcv:float
    ctm_mch:float
    ctm_mchc:float
    ctm_rdw:float
    +Chỉ số sắt huyết thanh
    ctm_sathuyetthanh:float
    ctm_ferritinehuyetthanh:float
    +Chỉ số điện di huyết sắc tố
    dd_hba1:float
    dd_hba2:float
    dd_hbe:float
    dd_hbh:float
    dd_hbbar:float
    dd_hbkhac:float
    dd_hbf:float
    Output(json):
    noGen:Khả năng bệnh nhân không mang gen bệnh
    gen:Khả năng bệnh nhân mang gen bệnh
    betaGen:Khả năng mang gen beta thalassemia nếu người đó mang gen bệnh
    alphaGen:Khả năng mang gen alpha thalassemia nếu người đó mang gen bệnh
    """
    input_param=input_param.json()
    str=json.loads(input_param)
    if(str['ctm_rbc']!=None and str['ctm_sathuyetthanh']!=None and str['dd_hba1']!=None):
        import thalassemiia_full
        return thalassemiia_full.predict(input_param)
    elif(str['ctm_rbc']!=None and str['ctm_sathuyetthanh']!=None and str['dd_hba1']==None):
        import thalassemia_mau_sat
        return thalassemia_mau_sat.predict(input_param)        
    elif(str['ctm_rbc']!=None and str['ctm_sathuyetthanh']==None):
        import thalassemia_mau
        return thalassemia_mau.predict(input_param)
    else:
        return    
@app.post('/trisomy_predict')
def trisomy(input_param:Model_input_trisomy):
    """
    Input(json)
    +Chung
    tuoi:Tuổi thai phụ(int)
    +Thai kỳ 1:
    -Siêu âm thai kỳ 1
    co_khoangsangsaugay:Khoảng sáng sau gáy(float)
    co_nangbachhuyetvungco_1:Nang bạch huyết vùng cổ thai kỳ 1(int:1=có,0=không)
    mat_xuongmui_1:Xương mũi thai kỳ 1(int:1=có,0=Không)
    nguc_ditattim_1:Dị tật tim thai kỳ 1(int:1=có,0=Không)
    -Double test
    d_mom_hcgb:Free-beta-hcg hiệu chỉnh(float)
    d_mom_pappa:Pappa hiệu chỉnh(float)
    d_mom_nt:Khoảng sáng sau gáy hiệu chỉnh(float)
    +Thai kỳ 2:
    -Siêu âm thai kỳ 2
    co_nangbachhuyetvungco_2:Nang bạch huyết vùng cổ thai kỳ 2(int:1=có,0=không)
    mat_xuongmui_2:Xương mũi thai kỳ 2(int:1=có,0=Không)
    nguc_ditattim_2:Dị tật tim thai kỳ 2(int:1=có,0=Không)
    mat_xuongsongmui:Độ dài xương sống mũi(float)
    -Triple test
    t_mom_ue3:Ue3 hiệu chỉnh(float)
    t_mom_afp:AFP hiệu chỉnh(float)
    t_mom_hcg:HCG hiệu chỉnh(float)

    Output(json):
    Trisomy21:Khả năng bị trisomy 21
    Trisomy18:Khả năng bị trisomy 18
    Trisomy13:Khả năng bị trisomy 13    
    """
    input_param=input_param.json()
    str=json.loads(input_param)
    if(str['d_mom_hcgb']!=None and str['t_mom_ue3']!=None and str['co_khoangsangsaugay']!=None and str['mat_xuongmui_2']!=None):
        import trisomy_full
        return trisomy_full.predict(input_param)
    elif(str['d_mom_hcgb']!=None and str['co_khoangsangsaugay']!=None and (str['t_mom_ue3']==None or str['mat_xuongmui_2']==None)):
        import trisomy_thaiky1
        return trisomy_thaiky1.predict(input_param)
    elif((str['d_mom_hcgb']==None or str['co_khoangsangsaugay']==None) and str['t_mom_ue3']!=None and str['mat_xuongmui_2']!=None):
        import trisomy_thaiky2
        return trisomy_thaiky2.predict(input_param)
    else:
        return
if __name__ == "__main__":
    uvicorn.run(app, host="103.179.191.178",port=23)