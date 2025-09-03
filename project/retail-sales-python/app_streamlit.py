import os
import pandas as pd
import streamlit as st
import altair as alt

# DB / Models
from db import engine, Base, SessionLocal, Dataset
from models import Sale

# Ingest & Utils
from ingest import ingest_csv
from utils import (
    agg_store_total, agg_monthly_avg,
    agg_weekday_avg, rank_stores_by_month,
    forecast_store, export_insights_to_excel
)

try:
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    _HAVE_HW = True
except Exception:
    _HAVE_HW = False


# Init DB

Base.metadata.create_all(bind=engine)


# Streamlit setup

st.set_page_config(layout="wide", page_title="Retail Sales Analytics", initial_sidebar_state="expanded")


# 🔐 Login / Signup system

if "users" not in st.session_state:
    st.session_state.users = {}   # temporary in-memory {username: password}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

if not st.session_state.logged_in:
    st.title("🔐 Retail Sales Analytics - Login")

    choice = st.radio("Choose option", ["Login", "Sign Up"])

    if choice == "Sign Up":
        new_user = st.text_input("Create Username")
        new_pass = st.text_input("Create Password", type="password")
        if st.button("Register"):
            if new_user in st.session_state.users:
                st.error("⚠️ Username already exists. Please login.")
            elif new_user.strip() == "" or new_pass.strip() == "":
                st.error("⚠️ Username and password cannot be empty.")
            else:
                st.session_state.users[new_user] = new_pass
                st.success("✅ Registration successful! Please login.")

    elif choice == "Login":
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Login"):
            if user in st.session_state.users and st.session_state.users[user] == pwd:
                st.session_state.logged_in = True
                st.session_state.username = user
                st.success(f"Welcome {user}!")
                st.rerun()   
            else:
                st.error("❌ Invalid username or password.")

    st.stop()  

# Sidebar logout
st.sidebar.success(f"👤 Logged in as {st.session_state.username}")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()   



st.title("Retail Store Sales — Time Series Analytics")


def normalize_df_columns(df: pd.DataFrame) -> pd.DataFrame:
    colmap = {
        "date": "Date", "storeid": "StoreID", "store_id": "StoreID", "store": "StoreID",
        "sales": "Sales", "sale": "Sales", "weekday": "Weekday", "month": "Month",
        "sales_category": "SalesCategory", "salescategory": "SalesCategory",
        "cumulative_sales": "CumulativeSales", "cumulativesales": "CumulativeSales",
        "promo": "PromoDay", "promoday": "PromoDay", "promo_day": "PromoDay",
        "zscore": "Zscore", "z_score": "Zscore", "anomaly": "Anomaly",
        "footfall_est": "Footfall_Est", "footfall": "Footfall_Est",
    }
    df = df.rename(columns={c: colmap.get(c.lower(), c) for c in df.columns})
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df

def load_latest_dataset() -> pd.DataFrame:
    session = SessionLocal()
    d = session.query(Dataset).order_by(Dataset.uploaded_at.desc()).first()
    session.close()
    if not d:
        return pd.DataFrame()
    q = f"SELECT * FROM sales WHERE dataset_id = {d.id}"
    df = pd.read_sql(q, engine)
    return normalize_df_columns(df)

# Sidebar: Ingest
st.sidebar.header("Upload / Ingest")
uploaded = st.sidebar.file_uploader("Upload retail_sales.csv (Date, StoreID, Sales)", type=["csv"])
promo_input = st.sidebar.text_input("Promo dates (comma-separated YYYY-MM-DD)", value="")
dataset_name_input = st.sidebar.text_input("Dataset name (optional)", value="")

if uploaded is not None and st.sidebar.button("Ingest & Process"):
    try:
        os.makedirs("sample_data", exist_ok=True)
        tmp_path = os.path.join("sample_data", uploaded.name)
        with open(tmp_path, "wb") as f:
            f.write(uploaded.getbuffer())

        promos = [p.strip() for p in promo_input.split(",") if p.strip()]
        ds_name = dataset_name_input.strip() or uploaded.name
        new_id = ingest_csv(tmp_path, promo_dates=promos, dataset_name=ds_name)
        st.sidebar.success(f"Ingested dataset {new_id} — {ds_name}")
        st.rerun()
    except Exception as e:
        st.sidebar.error(f"Failed ingest: {e}")

# Require upload before proceeding
if uploaded is None:
    st.info("Please upload a CSV to start analysis.")
    st.stop()
else:
    df = load_latest_dataset()

if df.empty:
    st.warning("Dataset ingestion did not return any rows. Please check your CSV.")
    st.stop()

# Sidebar options
store_list = ["All"] + sorted(df['StoreID'].dropna().unique().astype(str).tolist())
store_selector = st.sidebar.selectbox("Select store", options=store_list, index=0)
days_forecast = st.sidebar.number_input("Forecast days", min_value=7, max_value=90, value=14, step=1)
download_excel = st.sidebar.button("Export insights to Excel")

if download_excel:
    buf = export_insights_to_excel(df)
    st.sidebar.download_button("Download insights_export.xlsx", data=buf,
                               file_name="insights_export.xlsx",
                               mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


# Main charts

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Total Sales by Store")
    store_totals = agg_store_total(df)
    if not store_totals.empty:
        chart = alt.Chart(store_totals).mark_bar().encode(x="StoreID:O", y="Sales:Q", tooltip=["StoreID","Sales"])
        st.altair_chart(chart, use_container_width=True)

    st.subheader("Monthly Average Sales")
    monthly = agg_monthly_avg(df)
    if not monthly.empty:
        monthly['MonthName'] = monthly['Month'].apply(lambda m: pd.to_datetime(str(int(m)), format="%m").strftime("%b"))
        st.altair_chart(alt.Chart(monthly).mark_line(point=True).encode(x="MonthName:O", y="Avg:Q"), use_container_width=True)

    st.subheader("Weekday Average Sales")
    weekday = agg_weekday_avg(df)
    if not weekday.empty:
        st.altair_chart(alt.Chart(weekday).mark_bar().encode(x="Weekday:O", y="Avg:Q"), use_container_width=True)

with col2:
    st.subheader("Anomalies")
    anomalies = df[df['Anomaly'] == 'Anomaly'] if 'Anomaly' in df.columns else pd.DataFrame()
    st.dataframe(anomalies if not anomalies.empty else pd.DataFrame({"Message": ["No anomalies flagged."]}))

    st.subheader("Promo Impact")
    if 'PromoDay' in df.columns:
        promo_mean = df.groupby('PromoDay')['Sales'].mean().reset_index()
        promo_mean['Label'] = promo_mean['PromoDay'].map({True:'Promo', False:'Normal'})
        st.write(promo_mean[['Label','Sales']])
    else:
        st.write("PromoDay not present.")

    st.subheader("Top 5 Stores")
    st.table(store_totals.sort_values('Sales', ascending=False).head(5))

# Drilldown + Forecast

st.markdown("---")
st.header("Store Drilldown & Forecast")

if store_selector == "All":
    df_plot = df.groupby("Date")["Sales"].sum().reset_index()
else:
    df_plot = df[df["StoreID"] == int(store_selector)][["Date","Sales"]]

st.altair_chart(alt.Chart(df_plot).mark_line(point=True).encode(x="Date:T", y="Sales:Q"), use_container_width=True)

df_plot_idx = df_plot.set_index("Date").asfreq("D").fillna(0.0)
df_plot_idx["7day"] = df_plot_idx["Sales"].rolling(7, min_periods=1).mean()
st.subheader("7-day Rolling Average")
st.altair_chart(alt.Chart(df_plot_idx.reset_index()).mark_line().encode(x="Date:T", y="7day:Q"), use_container_width=True)

# Forecast
forecast_df = pd.DataFrame()
try:
    if store_selector == "All":
        ser = df.groupby("Date")["Sales"].sum().set_index("Date").asfreq("D").fillna(0.0)
        if _HAVE_HW and len(ser) >= 2:
            model = ExponentialSmoothing(ser, trend="add")
            fit = model.fit()
            pred = fit.forecast(days_forecast)
            forecast_df = pd.DataFrame({"date": pred.index, "forecast": pred.values})
    else:
        forecast_df = forecast_store(df, int(store_selector), periods=days_forecast)
except Exception:
    pass

if not forecast_df.empty:
    st.subheader(f"{days_forecast}-day Forecast")
    st.table(forecast_df.head(10))


# Rankings
st.markdown("---")
st.header("Store Monthly Ranking")
ranks = rank_stores_by_month(df)
if not ranks.empty:
    st.dataframe(ranks[["MonthName","StoreID","Sales","Rank"]])


st.markdown("---")
st.header("Retail Sales Data Analysis")

# Data Cleaning
st.subheader("Data Cleaning")
clean_df = df.copy()
clean_df["Sales"] = clean_df["Sales"].fillna(0)
clean_df = clean_df.drop_duplicates()
clean_df["Date"] = pd.to_datetime(clean_df["Date"], errors="coerce")
st.dataframe(clean_df.head())

# Time-Series Manipulation
st.subheader("Time-Series Manipulation")
ts_df = clean_df.copy()
ts_df = ts_df.set_index("Date").sort_index()
ts_df["Weekday"] = ts_df.index.day_name()
ts_df["Month"] = ts_df.index.month
st.dataframe(ts_df.head())

# Filtering
st.subheader("Filtering Examples")
store101 = ts_df[ts_df["StoreID"] == 101]
high_sales = ts_df[ts_df["Sales"] > 5000]
weekend_high = ts_df[(ts_df["Weekday"].isin(["Saturday", "Sunday"])) & (ts_df["Sales"] > 4000)]

filter_opt = st.radio("Show Filtering Results as:", ["Table", "Chart"], key="filter")
if filter_opt == "Table":
    st.write("➡️ StoreID=101", store101.head())
    st.write("➡️ Sales > 5000", high_sales.head())
    st.write("➡️ Weekends Sales > 4000", weekend_high.head())
else:
    st.altair_chart(
        alt.Chart(ts_df.reset_index()).mark_bar().encode(
            x="Weekday:O", y="Sales:Q", color="StoreID:N"
        ),
        use_container_width=True
    )

# Derived Columns
st.subheader("Derived Columns")
ts_df["CumulativeSales"] = ts_df.groupby("StoreID")["Sales"].cumsum()
ts_df["SalesCategory"] = pd.cut(
    ts_df["Sales"],
    bins=[-1,2999,4999,1e9],
    labels=["Low","Medium","High"]
)
derived_opt = st.radio("Show Derived Columns as:", ["Table", "Chart"], key="derived")
if derived_opt == "Table":
    st.dataframe(ts_df.head(10))
else:
    st.altair_chart(
        alt.Chart(ts_df.reset_index()).mark_line().encode(
            x="Date:T", y="CumulativeSales:Q", color="StoreID:N"
        ),
        use_container_width=True
    )

# Top 3 Stores
st.subheader("Top 3 Stores by Total Sales")
store_sales = ts_df.groupby("StoreID")["Sales"].sum().reset_index().rename(columns={"Sales":"TotalSales"})
top3 = store_sales.sort_values("TotalSales", ascending=False).head(3)
top_opt = st.radio("Show Top 3 Stores as:", ["Table", "Chart"], key="top3")
if top_opt == "Table":
    st.table(top3)
else:
    st.altair_chart(
        alt.Chart(top3).mark_bar().encode(x="StoreID:O", y="TotalSales:Q"),
        use_container_width=True
    )

# Export Results
st.subheader("Export Results")
csv1 = ts_df.reset_index().to_csv(index=False).encode("utf-8")
csv2 = store_sales.to_csv(index=False).encode("utf-8")
csv3 = ts_df.groupby("Weekday")["Sales"].mean().reset_index().to_csv(index=False).encode("utf-8")

st.download_button("⬇️ Download Cleaned Dataset", data=csv1, file_name="cleaned_retail_sales.csv", mime="text/csv")
st.download_button("⬇️ Download Store Sales Summary", data=csv2, file_name="store_sales_summary.csv", mime="text/csv")
st.download_button("⬇️ Download Weekday Sales Summary", data=csv3, file_name="weekday_sales_summary.csv", mime="text/csv")
