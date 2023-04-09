import pickle
import streamlit as st
import pandas as pd
from warnings import filterwarnings
filterwarnings('ignore')
# App Header
st.header('')
# Model Import n
model = pickle.load(open('Model\Log_Model.pkl', 'rb'))
standarscalr = pickle.load(open('Model\Scalar.pkl', 'rb'))

Age = st.number_input('Enter Your Age : ')
Total_Purchase = st.number_input("Enter Your Total Purchase : ")
Account_Manager = st.selectbox(
    "Are You Account Manager? -> Yes : 1 |  No : 0 ", (0, 1,))
Years = st.number_input('Enter A Years Point -> Ex:7.66')
Num_Sites = st.number_input("Enter Your Num_Sites -> Ex:12,9,8")
Onboard_date_year = int(st.number_input('Enter A Onboard Date Year'))
Onboard_date_month = int(st.number_input('Enter A Onboard Date Month'))
Onboard_date_date = int(st.number_input('Enter A Onboard Date Date'))
Location_Pincode = int(st.number_input('Enter A Onboard Location Pincode'))
Onboard_date_hours = int(st.number_input("Enter A Onboard Date Hours"))
Onboard_date_minits = int(st.number_input("Enter A Onboard Date Minit"))
Onboard_date_second = int(st.number_input("Enter A Onboard Date Second"))


x_test = pd.DataFrame([[Age, Total_Purchase, Account_Manager, Years, Num_Sites, Onboard_date_year, Onboard_date_month,
                      Onboard_date_date, Location_Pincode, Onboard_date_hours, Onboard_date_minits, Onboard_date_second]])

x_test_sc = standarscalr.transform(x_test)
result = model.predict(x_test_sc)[0]
if st.button('Predict'):
    if result == 1:
        st.write("This Is A Churn")
    else:
        st.write("This Not A Churn")
else:
    st.write(".......")

# ['Item_Weight', 'Item_Fat_Content', 'Item_Fat_Content', 'Item_Type',
#  'Item_MRP', 'Outlet_Establishment_Year', 'Outlet_Size',
#  'Outlet_Location_Type', 'Outlet_Type', 'Item_Outlet_Sales']
