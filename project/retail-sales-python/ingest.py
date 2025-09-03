# ingest.py
import pandas as pd
from db import SessionLocal, Dataset
from models import Sale
from utils import clean_and_feature

def ingest_csv(filepath, promo_dates=None, dataset_name=None):
    """
    Reads a CSV file, cleans/features data, creates Dataset record, 
    inserts Sale rows, and returns dataset_id.
    """
    # Read raw CSV
    df_raw = pd.read_csv(filepath)

    # Clean & feature engineer
    df_feat = clean_and_feature(df_raw, promo_dates=promo_dates)

    # Open DB session
    session = SessionLocal()

    # Create new dataset entry
    new_dataset = Dataset(name=dataset_name or filepath)
    session.add(new_dataset)
    session.commit()
    dataset_id = new_dataset.id

    # Insert each row into Sales table
    for _, r in df_feat.iterrows():
        s = Sale(
            date = r['Date'].date(),
            store_id = int(r['StoreID']),
            sales = float(r['Sales']),
            weekday = str(r['Weekday']),
            month = int(r['Month']),
            sales_category = str(r['SalesCategory']),
            cumulative_sales = float(r['CumulativeSales']),
            promo_day = bool(r['PromoDay']),
            zscore = float(r['Zscore']),
            anomaly = str(r['Anomaly']),
            footfall_est = int(r['Footfall_Est']),
            dataset_id = dataset_id
        )
        session.add(s)

    session.commit()
    session.close()
    return dataset_id


# Allow command-line usage too
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Ingest retail sales CSV into DB")
    parser.add_argument("filepath", help="Path to CSV file")
    parser.add_argument("--promos", nargs="*", help="List of promo dates YYYY-MM-DD", default=[])
    parser.add_argument("--name", help="Dataset name", default=None)
    args = parser.parse_args()

    ds_id = ingest_csv(args.filepath, promo_dates=args.promos, dataset_name=args.name)
    print(f"Ingest complete: dataset_id={ds_id}")
