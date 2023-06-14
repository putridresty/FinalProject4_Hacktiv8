import pickle
import streamlit as st

model = pickle.load(open('cc_clustering.sav','rb'))

st.title('Credit Card User Segmentation Prediction')

col1, col2= st.columns(2)

with col1:
    BALANCE = st.number_input('Balance')
    BALANCE_FREQUENCY = st.number_input('Balance Frequency')
    PURCHASES = st.number_input('Purchases')
    ONEOFF_PURCHASES = st.number_input('One Off Purchases')
    INSTALLMENTS_PURCHASES = st.number_input('Installments Purchases')
    CASH_ADVANCE = st.number_input('Cash Advance')
    PURCHASES_FREQUENCY = st.number_input('Purchases Frequency (0-1)')
    ONEOFF_PURCHASES_FREQUENCY = st.number_input('One Off Purchases Frequency (0-1)')
    PURCHASES_INSTALLMENTS_FREQUENCY = st.number_input('Purchases Installments Frequency (0-1)')
with col2:
    CASH_ADVANCE_FREQUENCY = st.number_input('Cash Advance Frequency')
    CASH_ADVANCE_TRX = st.number_input('Cash Advance Transaction')
    PURCHASES_TRX = st.number_input('Purchases Transaction')
    CREDIT_LIMIT = st.number_input('Credit Limit')
    PAYMENTS = st.number_input('Payments')
    MINIMUM_PAYMENTS = st.number_input('Minimum Payments')
    PRC_FULL_PAYMENT = st.number_input('Price Full Payment')
    TENURE = st.number_input('Tenure (6-12)')

data_cluster = [BALANCE, BALANCE_FREQUENCY, PURCHASES, ONEOFF_PURCHASES, 
                INSTALLMENTS_PURCHASES, CASH_ADVANCE, PURCHASES_FREQUENCY,
                ONEOFF_PURCHASES_FREQUENCY, PURCHASES_INSTALLMENTS_FREQUENCY, 
                CASH_ADVANCE_FREQUENCY, CASH_ADVANCE_TRX, PURCHASES_TRX, CREDIT_LIMIT, 
                PAYMENTS, MINIMUM_PAYMENTS, PRC_FULL_PAYMENT, TENURE]

cluster = ''

if st.button('Process'):
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
