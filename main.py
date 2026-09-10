import pickle
import numpy as np
import pandas as pd
from fastapi import FastAPI

model = pickle.load(open("model.pkl", "rb"))

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Api Running"}

@app.get("/predict")
def predict_attack(
    dur: float,
    proto: str,
    service: str,
    state: str,
    spkts: int,
    dpkts: int,
    sbytes: int,
    dbytes: int,
    rate: float,
    sload: float,
    dload: float,
    sloss: int,
    dloss: int,
    sinpkt: float,
    dinpkt: float,
    sjit: float,
    djit: float,
    swin: int,
    stcpb: int,
    dtcpb: int,
    dwin: int,
    tcprtt: float,
    synack: float,
    ackdat: float,
    smean: int,
    dmean: int,
    trans_depth: int,
    response_body_len: int,
    ct_src_dport_ltm: int,
    ct_dst_sport_ltm: int,
    is_ftp_login: int,
    ct_ftp_cmd: int,
    ct_flw_http_mthd: int,
    is_sm_ips_ports: int
    ):
    data_dict = {
        "dur": dur, "proto": proto, "service": service, "state": state,
        "spkts": spkts, "dpkts": dpkts, "sbytes": sbytes, "dbytes": dbytes,
        "rate": rate, "sload": sload, "dload": dload, "sloss": sloss,
        "dloss": dloss, "sinpkt": sinpkt, "dinpkt": dinpkt, "sjit": sjit,
        "djit": djit, "swin": swin, "stcpb": stcpb, "dtcpb": dtcpb,
        "dwin": dwin, "tcprtt": tcprtt, "synack": synack, "ackdat": ackdat,
        "smean": smean, "dmean": dmean, "trans_depth": trans_depth,
        "response_body_len": response_body_len, "ct_src_dport_ltm": ct_src_dport_ltm,
        "ct_dst_sport_ltm": ct_dst_sport_ltm, "is_ftp_login": is_ftp_login,
        "ct_ftp_cmd": ct_ftp_cmd, "ct_flw_http_mthd": ct_flw_http_mthd,
        "is_sm_ips_ports": is_sm_ips_ports
    }

    input_df = pd.DataFrame([data_dict])
    numeric_cols = input_df.select_dtypes(include=[np.number]).columns
    input_df[numeric_cols] = np.log1p(input_df[numeric_cols])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(input_df)
    
    try:
        probability = model.predict_proba(input_df)
        confidence = float(np.max(probability))
    except AttributeError:
        confidence = 1.0

    is_attack = int(prediction[0])
    status = "Attack" if is_attack == 1 else "Normal"
    
    return {
        "prediction": is_attack,
        "status": status,
        "confidence": confidence
    }


