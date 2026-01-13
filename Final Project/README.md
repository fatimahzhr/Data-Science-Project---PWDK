## Business Problem Understanding
Bisnis industri perhotelan bertumpu kepada tingkat pemesanan/booking kamar sebagai sumber pendapatan utama hotel, salah satu resiko yang menjadi permasalahan dalam industri perhotelan yaitu resiko pembatalan (cancellation) booking dari customer. Hal tersebut dapat menyebabkan hotel kehilangan revenue karena kamar yang sudah dibooking sulit untuk dijual kembali dan mengganggu management waktu operasional hotel. Oleh sebab itu management hotel perlu mengetahui dan menganalisis customer yang memiliki potensi membatalkan reservasi dengan menggunakan pendekatan data analysis dan machine learning.

City hotel dan resort hotel kerap mengalami pembatalan (cancellation) dari pelanggan, yang dapat berdampak signifikan terhadap bisnis hotel. Pembatalan ini menyebabkan potensi kehilangan pendapatan karena hotel telah mempersiapkan kedatangan tamu, seperti mengosongkan kamar dan mengatur operasional lainnya. Oleh karena itu, hotel perlu mengetahui dan memprediksi pelanggan mana yang benar-benar akan datang dan mana yang berpotensi membatalkan reservasi dengan menganalisis berbagai informasi, seperti waktu pemesanan, lama menginap, jumlah orang dewasa, anak-anak dan/atau bayi, serta ketersediaan tempat parkir, dan faktor-faktor relevan lainnya.

Target:

0: Tidak Batal
1: Batal
Stakeholder: Management Hotel

### Problem Statement
Booking cancellations dalam industri perhotelan memiliki dampak signifikan terhadap manajemen permintaan dan kinerja bisnis hotel. Pembatalan menghambat penyusunan peramalan permintaan yang akurat, yang merupakan komponen penting dalam revenue management. Selain itu, pembatalan juga menyebabkan potensi kehilangan pendapatan karena hotel telah mempersiapkan operasional sebelum kedatangan tamu, seperti mengalokasikan kamar, menyiapkan sumber daya manusia, dan mengatur layanan pendukung lainnya.
### Goals
1. Memprediksi pembatalan reservasi customer sehingga hotel dapat mengantisipasi potensi pembatalan lebih awal dan menurunkan cancellation rate.
2. Menganalisis faktor-faktor yang mempengaruhi pembatalan reservasi customer, sehingga hotel dapat melakukan perbaikan bisnis yang strategis.
### Metric Evaluation
Berdasarkan konsekuensi kerugiannya, maka kita harus berusaha untuk mengurangi biaya pembatalan booking oleh customer dengan mengurangi False Negative Rate, yaitu kondisi ketika booking yang sebenarnya batal justru diprediksi sebagai tidak batal. Oleh karena itu, fokus evaluasi model diarahkan pada metrik yang menekankan kemampuan mendeteksi pelanggan berisiko batal, yaitu:

Recall: Mengukur seberapa banyak pelanggan batal booking yang berhasil terdeteksi dengan benar oleh model.

### Limitation
- Dataset tidak menyediakan booking ID unik, sehingga potensi duplikasi data tidak dapat diverifikasi secara pasti, dan setiap observasi diasumsikan sebagai reservasi yang valid.
- Model ini dilatih menggunakan data booking periode 2015–2017. Oleh karena itu, prediksi dibatasi pada rentang waktu tersebut (historical behavior prediction) untuk menjaga konsistensi distribusi data dan reliabilitas prediksi.

## Data Source
https://www.sciencedirect.com/science/article/pii/S2352340918315191

| Feature                        | Description                                                                |
| ------------------------------ | -------------------------------------------------------------------------- |
| hotel                          | Type of hotel: Resort Hotel or City Hotel.                                 |
| is_canceled                    | Indicates whether the booking was canceled (1) or not (0).                 |
| lead_time                      | Number of days between the booking date and the arrival date.              |
| arrival_date_year              | Year of arrival date.                                                      |
| arrival_date_month             | Month of arrival date.                                                     |
| arrival_date_week_number       | Week number of the year for the arrival date.                              |
| arrival_date_day_of_month      | Day of the month of arrival date.                                          |
| stays_in_weekend_nights        | Number of weekend nights (Saturday or Sunday) booked or stayed.            |
| stays_in_week_nights           | Number of weekday nights (Monday to Friday) booked or stayed.              |
| adults                         | Number of adults included in the booking.                                  |
| babies                         | Number of babies included in the booking.                                  |
| meal                           | Type of meal booked (SC, BB, HB, FB, or Undefined).                        |
| country                        | Country of origin of the customer.                                         |
| market_segment                 | Market segment designation (e.g., Online TA, Direct, Corporate).           |
| distribution_channel           | Booking distribution channel (e.g., TA/TO, Direct, Corporate).             |
| is_repeated_guest              | Indicates whether the booking was made by a repeated guest (1) or not (0). |
| previous_cancellations         | Number of previous bookings canceled by the customer.                      |
| previous_bookings_not_canceled | Number of previous bookings not canceled by the customer.                  |
| reserved_room_type             | Code representing the room type reserved by the customer.                  |
| assigned_room_type             | Code representing the room type assigned to the booking.                   |
| booking_changes                | Number of changes made to the booking after creation.                      |
| deposit_type                   | Type of deposit applied (No Deposit, Non Refund, Refundable).              |
| agent                          | Identifier of the travel agency that made the booking (anonymized).        |
| company                        | Identifier of the company responsible for the booking (anonymized).        |
| days_in_waiting_list           | Number of days the booking was on the waiting list before confirmation.    |
| customer_type                  | Type of customer (Transient, Transient-Party, Group, Contract).            |
| adr                            | Average Daily Rate (total lodging revenue divided by number of nights).    |
| required_car_parking_spaces    | Number of car parking spaces required.                                     |
| total_of_special_requests      | Number of special requests made by the customer.                           |
| reservation_status             | Final reservation status (e.g., Check-Out, No-Show).                       |
| reservation_status_date        | Date when the last reservation status was set.                             |


## Step of Work
### 1. Exploratory Data Analysis (EDA)
Tahap awal dilakukan untuk memahami karakteristik data serta perilaku dan pola reservasi hotel.
### 2. Data Preprocessing
Tahap ini bertujuan menyiapkan data agar siap digunakan dalam pemodelan.
- Handling Missing Values: Menangani nilai kosong dengan pendekatan yang sesuai untuk menjaga konsistensi dan kualitas data.
- Handling Noisy Data & Filtering: Mengurangi noise dan melakukan filtering pada data yang tidak relevan atau berpotensi mengganggu performa model.
- Feature Selection: Menghapus kolom yang tidak digunakan atau tidak relevan dengan tujuan prediksi, seperti identifier dan kolom pasca-kejadian (data leakage).
- Encoding: Variabel kategorikal diubah menggunakan One-Hot Encoding agar dapat diproses oleh algoritma machine learning.
- Scaling: Fitur numerik dilakukan scaling menggunakan RobustScaler untuk mengurangi pengaruh outlier.
- Handling Imbalanced Data: Ketidakseimbangan kelas ditangani menggunakan Random Over Sampling (ROS) untuk meningkatkan kemampuan model dalam mendeteksi kelas minoritas (cancellation).
- Train–Test Split: Data dibagi menjadi data latih (70%) dan data uji (30%)
### 3. Modeling & Benchmarking
Beberapa algoritma klasifikasi diuji dan dibandingkan untuk menemukan model dengan performa terbaik, antara lain:
- Logistic Regression (LR)
- K-Nearest Neighbors (KNN)
- Decision Tree (DT)
- Random Forest (RF)
- XGBoost (XGB)
- AdaBoost (ADB)
- Gradient Boosting (GB)
- LightGBM (LGBM)

Benchmarking dilakukan dengan fokus pada recall. Berdasarkan hasil benchmarking, XGBoost dan Random Forest dipilih sebagai kandidat utama karena memiliki nilai recall tertinggi dalam mendeteksi booking yang berisiko cancel.
### 4. Hyperparameter Tuning
Hyperparameter tuning dilakukan menggunakan GridSearchCV untuk mengoptimalkan performa kedua model terpilih dan menemukan kombinasi parameter terbaik.
### 5. Model Evaluation
Berdasarkan hasil evaluasi menyeluruh, XGBoost dipilih sebagai final model karena memberikan keseimbangan terbaik antara performa, stabilitas, dan kemampuan generalisasi.

📊 Model Performance (Test Set)

| Metric | Value |
|------|------|
| Accuracy | 80% |
| Recall (Canceled Booking) | 85% |
| Precision (Canceled Booking) | 69% |
| F1-score (Canceled Booking) | 76% |


Classification report tersebut menunjukkan bahwa dengan model XGBoost yang telah di tuning. Model dapat mendeteksi sebagian besar pelanggan yang akan cancel (recall = 85%).

### 6. Model Interpretability
Untuk memahami kontribusi setiap fitur terhadap prediksi, dilakukan analisis feature importance menggunakan SHAP (SHapley Additive exPlanations). Analisis ini membantu menjelaskan faktor-faktor utama yang memengaruhi keputusan model serta meningkatkan transparansi dan kepercayaan terhadap hasil prediksi.
