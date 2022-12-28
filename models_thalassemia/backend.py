from ast import main
import pandas as pd
import pickle
def trisomy_fulldata(path):
    df=pd.read_csv(path)

    featuresdouble=["tuoi","d_mom_pappa","d_khoangsangsaugay","chieudaidaumong","d_tuoithai","d_mom_hcgb","mat_xuongsongmui"]

    X = df[featuresdouble].values
    filename21 = 'trisomy21forfun'
    filename18 = 'trisomy21forfun'
    filename13 = 'trisomy21forfun'

    infile21 = open(filename21,'rb')
    infile18 = open(filename18,'rb')
    infile13 = open(filename13,'rb')

    new_dict21 = pickle.load(infile21)
    infile21.close()
    new_dict18 = pickle.load(infile18)
    infile18.close()
    new_dict13 = pickle.load(infile13)
    infile13.close()
    y_pred_21=new_dict21.predict_proba(X)[:,1]*100
    y_pred_18=new_dict18.predict_proba(X)[:,1]*100
    y_pred_13=new_dict13.predict_proba(X)[:,1]*100
    df=df.drop(df.columns,axis=1)
    df=df.assign(predict_trisomy21=y_pred_21)
    df=df.assign(predict_trisomy18=y_pred_18)
    df=df.assign(predict_trisomy13=y_pred_13)
    return df
def trisomy_double(path):
    df=pd.read_csv(path)
 
    featuresdouble=["tuoi","d_mom_pappa","d_khoangsangsaugay","chieudaidaumong","d_tuoithai","d_mom_hcgb","mat_xuongsongmui"]

    X = df[featuresdouble].values
    filename21 = 'trisomy21forfun'
    filename18 = 'trisomy21forfun'
    filename13 = 'trisomy21forfun'

    infile21 = open(filename21,'rb')
    infile18 = open(filename18,'rb')
    infile13 = open(filename13,'rb')

    new_dict21 = pickle.load(infile21)
    infile21.close()
    new_dict18 = pickle.load(infile18)
    infile18.close()
    new_dict13 = pickle.load(infile13)
    infile13.close()
    y_pred_21=new_dict21.predict_proba(X)[:,1]*100
    y_pred_18=new_dict18.predict_proba(X)[:,1]*100
    y_pred_13=new_dict13.predict_proba(X)[:,1]*100
    df=df.drop(df.columns,axis=1)
    df=df.assign(predict_trisomy21=y_pred_21)
    df=df.assign(predict_trisomy18=y_pred_18)
    df=df.assign(predict_trisomy13=y_pred_13)
    return df
def trisomy_triple(path):
    df=pd.read_csv(path)
    features=["ctm_rbc","ctm_hgb","ctm_hct","ctm_mcv","ctm_mch","ctm_mchc","ctm_rdw","ctm_sathuyetthanh",
    "ctm_ferritinehuyetthanh","dd_hba1","dd_hba2","dd_hbe","dd_hbf","dd_hbh","dd_hbbar","dd_hbkhac"]
    featuresdouble=["tuoi","d_mom_pappa","d_khoangsangsaugay","chieudaidaumong","d_tuoithai","d_mom_hcgb","mat_xuongsongmui"]

    X = df[featuresdouble].values
    filename21 = 'trisomy21forfun'
    filename18 = 'trisomy21forfun'
    filename13 = 'trisomy21forfun'

    infile21 = open(filename21,'rb')
    infile18 = open(filename18,'rb')
    infile13 = open(filename13,'rb')

    new_dict21 = pickle.load(infile21)
    infile21.close()
    new_dict18 = pickle.load(infile18)
    infile18.close()
    new_dict13 = pickle.load(infile13)
    infile13.close()
    y_pred_21=new_dict21.predict_proba(X)[:,1]*100
    y_pred_18=new_dict18.predict_proba(X)[:,1]*100
    y_pred_13=new_dict13.predict_proba(X)[:,1]*100
    df=df.drop(df.columns,axis=1)
    df=df.assign(predict_trisomy21=y_pred_21)
    df=df.assign(predict_trisomy18=y_pred_18)
    df=df.assign(predict_trisomy13=y_pred_13)
    return df
def preprocess_data(path):
    
    pass
if __name__ == "__main__":
    PATH="D:\Bioinformatics\\trisomy\\Data\\Trisomy21New.csv"
    print(trisomy_fulldata(PATH))
