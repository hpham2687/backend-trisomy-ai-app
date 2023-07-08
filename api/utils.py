import json
import numpy as np
from pydantic import BaseModel
from typing import Optional
feature_double_ver5=['tuoi','co_khoangsangsaugay','co_nangbachhuyetvungco','mat_xuongmui',
'nguc_ditattim','d_mom_hcgb','d_mom_pappa','d_mom_nt']
feature_triple_ver5=["tuoi","co_nangbachhuyetvungco",'mat_xuongmui',
"mat_xuongsongmui",'nguc_ditattim','t_mom_ue3','t_mom_afp','t_mom_hcg']
feature_full_ver5=['tuoime','co_khoangsangsaugay','co_nangbachhuyetvungco','mat_xuongmui','nguc_ditattim','mat_xuongsongmui',
'd_mom_hcgb','d_mom_pappa','t_mom_ue3','t_mom_afp','t_mom_hcg']
class Model_input_trisomy(BaseModel):
    tuoi:Optional[int]=None 
    co_khoangsangsaugay:Optional[float]=None
    co_nangbachhuyetvungco_1:Optional[int]=None
    mat_xuongmui_1:Optional[int]=None
    nguc_ditattim_1:Optional[int]=None
    d_mom_hcgb:Optional[float]=None
    d_mom_pappa:Optional[float]=None
    d_mom_nt:Optional[float]=None
    co_nangbachhuyetvungco_2:Optional[int]=None
    mat_xuongmui_2:Optional[int]=None
    nguc_ditattim_2:Optional[int]=None
    mat_xuongsongmui:Optional[float]=None
    t_mom_ue3:Optional[float]=None
    t_mom_afp:Optional[float]=None
    t_mom_hcg:Optional[float]=None
 
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)