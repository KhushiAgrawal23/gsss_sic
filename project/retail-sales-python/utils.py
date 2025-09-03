# utils.py
import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# --- Feature engineering ---
def clean_and_feature(df, promo_dates=None):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Weekday'] = df['Date'].dt.day_name()

    # simple sales category
    q1, q3 = df['Sales'].quantile([0.25, 0.75])
    df['SalesCategory'] = pd.cut(df['Sales'], bins=[-np.inf, q1, q3, np.inf], labels=['Low','Medium','High'])

    # cumulative
    df['CumulativeSales'] = df.groupby('StoreID')['Sales'].cumsum()

    # promo flag
    df['PromoDay'] = df['Date'].isin(pd.to_datetime(promo_dates)) if promo_dates else False

    # zscore
    df['Zscore'] = (df['Sales'] - df['Sales'].mean()) / df['Sales'].std(ddof=0)
    df['Anomaly'] = np.where(df['Zscore'].abs() > 2, "Anomaly", "Normal")

    # footfall estimation (assume avg spend per customer = 500)
    df['Footfall_Est'] = (df['Sales'] / 500).astype(int)

    return df

# Aggregations
def agg_store_total(df):
    return df.groupby('StoreID')['Sales'].sum().reset_index()

def agg_monthly_avg(df):
    # ✅ ensure Month exists
    if 'Month' not in df.columns:
        df['Month'] = pd.to_datetime(df['date']).dt.month
    return df.groupby('Month')['Sales'].mean().reset_index(name='Avg')

def agg_weekday_avg(df):
    if 'Weekday' not in df.columns:
        df['Weekday'] = pd.to_datetime(df['date']).dt.day_name()
    return df.groupby('Weekday')['Sales'].mean().reset_index(name='Avg')

def series_by_store(df, store_id):
    return df[df['StoreID'] == store_id].sort_values('Date')[['Date','Sales']]

def rank_stores_by_month(df: pd.DataFrame):
    monthly = df.groupby(['Month','StoreID'])['Sales'].sum().reset_index()
    monthly['Rank'] = monthly.groupby('Month')['Sales'].rank(ascending=False, method='min').astype(int)
    # Use the existing Month column or convert from Date if needed
    if 'Month' not in monthly.columns and 'Date' in df.columns:
        monthly['Month'] = pd.to_datetime(df['Date']).dt.month
    monthly['MonthName'] = monthly['Month'].apply(lambda m: pd.to_datetime(str(m), format='%m').strftime('%b'))
    return monthly.sort_values(['Month','Rank'])


# Forecast
def forecast_store(df, store_id=None, periods=14):
    if store_id:
        series = df[df['StoreID']==store_id].set_index('Date')['Sales']
    else:
        series = df.groupby('Date')['Sales'].sum()
    series = series.asfreq('D').fillna(0)
    model = ExponentialSmoothing(series, trend='add', seasonal=None, damped_trend=True)
    fit = model.fit(optimized=True)
    pred = fit.forecast(periods)
    return pd.DataFrame({'Date': pred.index, 'Forecast': pred.values})

# Excel export
def export_insights_to_excel(df):
    import io
    from openpyxl import Workbook

    wb = Workbook()
    ws = wb.active
    ws.title = "Insights"
    for col, name in enumerate(df.columns, 1):
        ws.cell(row=1, column=col, value=name)
    for row in df.itertuples(index=False, name=None):
        ws.append(row)

    buf = io.BytesIO()
    wb.save(buf)
    buf.seek(0)
    return buf

