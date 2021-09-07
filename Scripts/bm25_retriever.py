import pickle

class BM25Retriever:
    def __init__(self, meta_df, model_path="Model/bm25.pkl"):

        with open(model_path, "rb") as f:
            bm25 = pickle.load(f)

        self.bm25 = bm25
        self.meta_df = meta_df


    def most_similar(self, query_name, query_id, n=11):

        tokenized_query = query_name.split()
        doc_scores = self.bm25.get_scores(tokenized_query)

        results = []
        idx = (-doc_scores).argsort()[:n]
        for i in idx:
            if i != query_id:
                results.append({
                                "productid": self.meta_df.loc[i, "productid"],
                                "score": doc_scores[i]
                                })
        return results
