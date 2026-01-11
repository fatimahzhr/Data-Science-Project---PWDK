import streamlit as st
import pickle
import pandas as pd
from datetime import date

# ======================
# LOAD MODEL
# ======================
with open("Hotel Booking Prediction.sav", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Hotel Cancellation Prediction", layout="wide")

st.title("🏨 Hotel Booking Cancellation Prediction")
st.write("Aplikasi ini memprediksi kemungkinan pembatalan booking hotel.")

# ======================
# ARRIVAL DATE
# ======================
st.subheader("📅 Arrival Date")

col_date1, col_date2 = st.columns(2)

with col_date1:
    arrival_date = st.date_input(
        "Pilih Tanggal Kedatangan",
        min_value=date(2015, 1, 1),
        max_value=date(2017, 12, 31)
    )

arrival_date_year = arrival_date.year
arrival_date_month = arrival_date.month
arrival_date_week_number = arrival_date.isocalendar().week
arrival_date_day_of_month = arrival_date.day

# ======================
# NUMERIC INPUT
# ======================
st.subheader("🔢 Booking Details")

col1, col2, col3 = st.columns(3)

with col1:
    lead_time = st.number_input("Lead Time (hari)", min_value=0, value=50)
    stays_in_weekend_nights = st.number_input("Weekend Nights", min_value=0, value=1)
    stays_in_week_nights = st.number_input("Week Nights", min_value=0, value=2)
    adr = st.number_input("ADR", min_value=0.0, value=100.0)

with col2:
    previous_cancellations = st.number_input("Previous Cancellations", min_value=0, value=0)
    previous_bookings_not_canceled = st.number_input("Previous Bookings Not Canceled", min_value=0, value=0)
    booking_changes = st.number_input("Booking Changes", min_value=0, value=0)
    days_in_waiting_list = st.number_input("Waiting List Days", min_value=0, value=0)

with col3:
    required_car_parking_spaces = st.number_input("Parking Spaces", min_value=0, value=0)
    total_of_special_requests = st.number_input("Special Requests", min_value=0, value=0)
    total_guest = st.number_input("Total Guest", min_value=1, value=2)
    is_repeated_guest = st.selectbox("Repeated Guest?", [0, 1])

# ======================
# CATEGORICAL INPUT
# ======================
st.subheader("🏷️ Booking Category")

col4, col5, col6 = st.columns(3)

with col4:
    hotel = st.selectbox("Hotel Type", ["Resort Hotel", "City Hotel"])
    meal = st.selectbox("Meal", ["BB", "HB", "FB", "SC", "Undefined"])

with col5:
    market_segment = st.selectbox(
        "Market Segment",
        ["Online TA", "Offline TA/TO", "Direct", "Corporate", "Complementary", "Groups", "Aviation"]
    )
    distribution_channel = st.selectbox(
        "Distribution Channel",
        ["TA/TO", "Direct", "Corporate", "GDS"]
    )

with col6:
    reserved_room_type = st.selectbox(
        "Reserved Room Type",
        ["A", "B", "C", "D", "E", "F", "G", "H"]
    )
    deposit_type = st.selectbox(
        "Deposit Type",
        ["No Deposit", "Non Refund", "Refundable"]
    )
    customer_type = st.selectbox(
        "Customer Type",
        ["Transient", "Transient-Party", "Contract", "Group"]
    )

# ======================
# PREDICTION
# ======================
if st.button("🔮 Predict Cancellation"):

    input_df = pd.DataFrame([{
        "hotel": hotel,
        "lead_time": lead_time,
        "arrival_date_year": arrival_date_year,
        "arrival_date_month": arrival_date_month,
        "arrival_date_week_number": arrival_date_week_number,
        "arrival_date_day_of_month": arrival_date_day_of_month,
        "stays_in_weekend_nights": stays_in_weekend_nights,
        "stays_in_week_nights": stays_in_week_nights,
        "is_repeated_guest": is_repeated_guest,
        "previous_cancellations": previous_cancellations,
        "previous_bookings_not_canceled": previous_bookings_not_canceled,
        "booking_changes": booking_changes,
        "days_in_waiting_list": days_in_waiting_list,
        "adr": adr,
        "required_car_parking_spaces": required_car_parking_spaces,
        "total_of_special_requests": total_of_special_requests,
        "total_guest": total_guest,
        "meal": meal,
        "market_segment": market_segment,
        "distribution_channel": distribution_channel,
        "reserved_room_type": reserved_room_type,
        "deposit_type": deposit_type,
        "customer_type": customer_type
    }])

    probability = model.predict_proba(input_df)[0][1]

    st.subheader("📊 Prediction Result")

    if probability >= 0.6:
        st.error(f"⚠️ High Risk of Cancellation\n\nProbability: {probability:.2%}")
    else:
        st.success(f"✅ Low Risk of Cancellation\n\nProbability: {probability:.2%}")
