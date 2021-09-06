# fastapi
import uvicorn
from fastapi import FastAPI
from decimal import Decimal
from Model.fastapiModels import SessionAdd2CardEvents

from Scripts.item2vec import wv
from Scripts.bm25_retriever import BM25Retriever
from Scripts.productDict import product_dict

import pandas as pd

# load product info
meta_df = pd.read_pickle("Data/meta_df.pkl")

## app
app = FastAPI()

# BM25
bm25Retriever = BM25Retriever(meta_df=meta_df)


def get_results(events):
    product_id = events["events"][-1]["productid"]
    product_name = product_dict.get(product_id, "")

    if product_id in wv:
        results = wv.most_similar(positive=[product_id])
        results = [{"productid":result[0], "score":result[1]} for result in results]
    else:
        results = bm25Retriever.most_similar(product_name, product_id)
    return results


@app.post("/predict")
def predict(sessionAdd2CardEvents: SessionAdd2CardEvents):
    sessionAdd2CardEvents = sessionAdd2CardEvents.dict()
    responses = get_results(sessionAdd2CardEvents)
    
    return {
         "recommendations": responses
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
