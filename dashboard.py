import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


all_df = pd.read_csv("all_data.csv")

datetime_columns = ["dateday"]
all_df.sort_values(by="dateday", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])


min_date = all_df["dateday"].min()
max_date = all_df["dateday"].max()
 
with st.sidebar:
    st.title("Silahkan Pilih Rentang Waktu")
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dateday"] >= str(start_date)) & 
                (all_df["dateday"] <= str(end_date))]

st.title("Penyawaan Sepeda")

st.header("Pengaruh Kecepatan Angin Terhadap Jumlah Penyewaan Sepeda")

correlation = main_df['windspeed'].corr(main_df['count'])



# Visualisasi
fig, ax = plt.subplots(figsize=(10, 6))  # Menggunakan subplots untuk membuat figur
ax.scatter(all_df['windspeed'], all_df['count'], alpha=0.5)  # Menggunakan sumbu 'ax' untuk scatter plot
ax.set_title('Pengaruh Kecepatan Angin terhadap Jumlah Penyewaan Sepeda')
ax.set_xlabel('Kecepatan Angin (windspeed)')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.grid(True)
st.pyplot(fig)  # Menampilkan plot menggunakan figur yang sama

st.write("Korelasi antara kecepatan angin (windspeed) dan jumlah penyewaan sepeda:", correlation)


st.header("Perbedaan Pola Penyewaan Sepeda Antara Pengguna Casual dan Pengguna Terdaftar (Registered)")
st.subheader("Berdasarkan Musim")
season_counts = main_df.groupby('season')['count'].sum().reset_index()

# Visualisasi dengan bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(season_counts['season'], season_counts['count'])  # Menggunakan sumbu 'ax' untuk bar chart
ax.set_title('Total Jumlah Penyewaan Sepeda berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Total Jumlah Penyewaan Sepeda')

# Menampilkan plot di Streamlit
st.pyplot(fig)

st.subheader("Berdasarkan Registered")
# Menghitung total jumlah penyewaan sepeda oleh pelanggan terdaftar berdasarkan musim (season)
season_registered = main_df.groupby('season')['registered'].sum().reset_index()

# Visualisasi dengan bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(season_registered['season'], season_registered['registered'])  # Menggunakan sumbu 'ax' untuk bar chart
ax.set_title('Total Jumlah Penyewaan Sepeda oleh Pelanggan Terdaftar berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Total Jumlah Penyewaan Sepeda oleh Pelanggan Terdaftar')

# Menampilkan plot di Streamlit
st.pyplot(fig)


st.subheader("Berdasarkan Casual")
# Menghitung total jumlah penyewaan sepeda oleh pelanggan biasa (casual) berdasarkan musim (season)
season_casual = main_df.groupby('season')['casual'].sum().reset_index()

# Visualisasi dengan bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(season_casual['season'], season_casual['casual'])  # Menggunakan sumbu 'ax' untuk bar chart
ax.set_title('Total Jumlah Penyewaan Sepeda oleh Pelanggan Biasa berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Total Jumlah Penyewaan Sepeda oleh Pelanggan Biasa')

# Menampilkan plot di Streamlit
st.pyplot(fig)


