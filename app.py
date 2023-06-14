import pickle
import streamlit as st

model = pickle.load(open('cc_clustering.sav','rb'))

st.title('Prediksi Segmentasi Pengguna Kartu Kredit')

col1, col2= st.columns(2)

with col1:
    BALANCE = st.number_input('SBerapa saldo yang tersisa? ')
    BALANCE_FREQUENCY = st.selectbox('Seberapa sering saldo diperbarui? (1 = frequently updated, 0 = not frequently updated)', (0, 1))
    PURCHASES = st.number_input('Berapa jumlah pembelian yang dilakukan pada akun?')
    ONEOFF_PURCHASES = st.number_input('Berapa jumlah pembelian maksimum dalam sekali transaksi?')
    INSTALLMENTS_PURCHASES = st.number_input('Berapa jumlah pembelian yang dilakukan secara cicilan?')
    CASH_ADVANCE = st.number_input('Berapa uang muka yang diberikan oleh pengguna?')
    PURCHASES_FREQUENCY = st.selectbox('Seberapa sering melakukan pembelian?(1 = frequently updated, 0 = not frequently updated)', (0, 1))
    ONEOFF_PURCHASES_FREQUENCY = st.selectbox('Seberapa sering pembelian dilakukan secara sekaligus? (1 = frequently updated, 0 = not frequently updated)', (0, 1))
    PURCHASES_INSTALLMENTS_FREQUENCY = st.selectbox('Frekuensi pembelian angsuran(1 = frequently updated, 0 = not frequently updated)', (0, 1))
with col2:
    CASH_ADVANCE_FREQUENCY = st.number_input('Seberapa sering uang muka dibayarkan?')
    CASH_ADVANCE_TRX = st.number_input('Berapa jumlah Transaksi yang dilakukan dengan "Cash in Advance/Bayar dimuka"')
    PURCHASES_TRX = st.number_input('Berapa jumlah transaksi pembelian yang dilakukan?')
    CREDIT_LIMIT = st.number_input('Berapa limit kartu kredit pengguna?')
    PAYMENTS = st.number_input('Berapa jumlah pembayaran yang dilakukan oleh pengguna?')
    MINIMUM_PAYMENTS = st.number_input('Berapa jumlah minimum pembayaran yang dilakukan oleh pengguna?')
    PRC_FULL_PAYMENT = st.number_input('Berapa presentase pembayaran penuh yang dilakukan oleh pengguna?')
    TENURE = st.selectbox('Berapa jangka waktu layanan kartu kredit untuk pengguna?', (6,7,8,9,10,11,12))

data_cluster = [BALANCE, BALANCE_FREQUENCY, PURCHASES, ONEOFF_PURCHASES, 
                INSTALLMENTS_PURCHASES, CASH_ADVANCE, PURCHASES_FREQUENCY,
                ONEOFF_PURCHASES_FREQUENCY, PURCHASES_INSTALLMENTS_FREQUENCY, 
                CASH_ADVANCE_FREQUENCY, CASH_ADVANCE_TRX, PURCHASES_TRX, CREDIT_LIMIT, 
                PAYMENTS, MINIMUM_PAYMENTS, PRC_FULL_PAYMENT, TENURE]

cluster = ''

if st.button('Prediksi'):
    cluster = model.predict([data_cluster])

    if cluster[0] == 0:
        st.write('Berdasarkan analisa, pengguna masuk ke dalam cluster : Cluster 0 (limit kredit pengguna paling rendah & Pengguna sangat jarang memperbaharui isi saldo)')
    elif cluster[0] == 1:
        st.write('Berdasarkan analisa, pengguna masuk ke dalam cluster : Cluster 1 (limit kredit rendah & Pengguna jarang memperbaharui isi saldo)')
    elif cluster[0] == 2:
        st.write('Berdasarkan analisa, pengguna masuk ke dalam cluster : Cluster 2 (limit kredit pengguna rata-rata & pengguna cukup sering memperbaharui isi saldo)')
    elif cluster[0] == 3:
        st.write('Berdasarkan analisa, pengguna masuk ke dalam cluster :  Cluster 3 (limit kredit pengguna pengguna tinggi & pengguna sering memperbaharui isi saldo)')
    elif cluster[0] == 4:
        st.write('Berdasarkan analisa, pengguna masuk ke dalam cluster :  Cluster 4 (limit kredit pengguna paling tinggi & Pengguna sangat sering memperbaharui isi saldo)')
