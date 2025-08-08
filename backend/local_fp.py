import pandas as pd, boto3, json
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
import os

s3 = boto3.client("s3")
BUCKET = os.getenv("AWS_BUCKET_NAME", "retail-dataset-cyril")

def process_local_and_save(file_stream, min_support, min_conf, job_id):
    transactions = {}
    for chunk in pd.read_csv(file_stream, chunksize=100000):
        for _, row in chunk.iterrows():
            inv = row['InvoiceNo']
            desc = str(row['Description']).strip()
            if pd.isna(desc): continue
            transactions.setdefault(inv, set()).add(desc)
    txns = [list(s) for s in transactions.values()]
    te = TransactionEncoder()
    te_ary = te.fit(txns).transform(txns)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    freq = fpgrowth(df, min_support=min_support, use_colnames=True)
    rules = association_rules(freq, metric="confidence", min_threshold=min_conf)
    key = f"results/{job_id}/rules.json"
    s3.put_object(Bucket=BUCKET, Key=key, Body=json.dumps(rules.to_dict(orient='records')).encode())
    return
