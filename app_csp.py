# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:49:35 2024

@author: IT Department
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.app_logo import add_logo
from PIL import Image
from streamlit_extras.let_it_rain import rain

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/IT Department/Downloads/Streamlit Apps/multiple-disease-prediction-streamlit-app-main/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/IT Department/Downloads/Streamlit Apps/multiple-disease-prediction-streamlit-app-main/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/IT Department/Downloads/Streamlit Apps/multiple-disease-prediction-streamlit-app-main/saved_models/parkinsons_model.sav', 'rb'))


# add kitten logo
#logo = "https://drive.google.com/file/d/1USlyWZeb_gFbdGaNgCI89e7GwXDkJQSB/view?usp=sharing"

def add_logoo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

my_logo = add_logoo(logo_path="C:/Users/IT Department/Downloads/Streamlit Apps/multiple-disease-prediction-streamlit-app-main/pic/NCM_CSP_logo_blue.png", width=392, height=168)
st.sidebar.image(my_logo)

# OR
# st.sidebar.image(add_logoo(logo_path='C:/Users/IT Department/Downloads/qr_code/NCM_CSP_logo_blue.png', width=50, height=60)) 



# sidebar for navigation
with st.sidebar:
    selected = option_menu('NCM Warning Prediction System',

                           ['Cloud Seeding Program',
                            'Seeding Decision',
                            'Farmer Warning',
                            'Healthcare Warning'],
                           menu_icon='',
                           icons=['info-lg','cloud-hail', 'megaphone', 'heart-pulse'],
                           default_index=0)


# Cloud Seeding Program Page
if selected == 'Cloud Seeding Program':
    
# =============================================================================
#     # Devider
#     st.divider()
# =============================================================================
    
    st.image(add_logoo(logo_path='C:/Users/IT Department/Downloads/Streamlit Apps/multiple-disease-prediction-streamlit-app-main/pic/csp banner ewbsite.png', width=2000, height=432)) 
    
    
    
    # page title
    st.header('Cloud Seeding Program', divider='rainbow')
    
    st.markdown("*Hackathon* is **really** ***cool***.")
    st.markdown(''':red[Cloud Seeding Program] :orange[can] :green[increase] :blue[the chance of rainning for some cloud.] :violet[for some]
    :gray[regions in] :rainbow[Saudi Arabia].''')
    st.markdown("Testing Emojis &mdash;\
            🌧️:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


    
    multi =  '''هـو نـوع مـن عمليـات تعديـل الطقـس الـذي يهـدف
إلــى تغييــر كميــة أو نــوع هطــول األمطــار

الــذي
يســقط مــن الســحب، وذلــك بنشــر وإطــاق أنــواع
مختصــه مــن المــواد الكيميائيــة فــي الهــواء

والتــي
تسـاعد علـى تكاثـف السـحب أو النــوى الجليديـة، ممـا
يغيــر العمليــات الفيزيائيــة الدقيقــة داخــل الســحابة. .
'''
    st.markdown(multi)
    
    # Divider
    st.divider()


    st.image(add_logoo(logo_path='C:/Users/IT Department/Downloads/Streamlit Apps/multiple-disease-prediction-streamlit-app-main/pic/radargif.gif', width=1036, height=680)) 


# =============================================================================
# # logo and title
# st.write("a logo and text next to eachother")
# col1, mid, col2 = st.beta_columns([1,1,20])
# with col1:
#     st.image('C:/Users/IT Department/Downloads/Streamlit Apps/multiple-disease-prediction-streamlit-app-main/pic/NCM_CSP_logo_blue.png', width=60)
# with col2:
#     st.write('A Name')
# =============================================================================



##########################################################################
# rain animation
def example():
    rain(
        emoji="💧",
        font_size=25,
        falling_speed=2,
        animation_length="infinite",
    )
##########################################################################


# Seeding Decision Page
if selected == 'Seeding Decision':
    
    
    # loading the saved model
    loaded_model = pickle.load(open('C:/Users/IT Department/Downloads/Streamlit Apps/multiple-disease-prediction-streamlit-app-main/saved_models/seeding_model.sav', 'rb'))


    # creating a function for Prediction

    def seeding_prediction(input_data):
        

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)
        print(input_data_as_numpy_array)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        print(input_data_reshaped)

        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if (prediction[0] == 0):
          return 'Clouds are not Suitable for seeding'
        else:
          return '--->  Clouds Suitable for seeding'
      
    

    # page title
    st.title('Seeding Decision using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    

    with col1:
        showalter_Index = st.text_input('Showalter index value')

    with col2:
        Lifted_index  = st.text_input('Lifted index value')

    with col3:
        LIFT_computed_virtual_temp  = st.text_input('LIFT using virtual temperature value')

    with col1:
        SWEAT_index  = st.text_input('SWEAT index value')

    with col2:
        K_index  = st.text_input('K index value')

    with col3:
        Tot_tot_index  = st.text_input('Totals totals index value')

    with col1:
        CINS_virtual_temperature  = st.text_input('CINS using virtual temperature value')

    with col2:
        Convective_Available_Potential_Energy  = st.text_input('CAPE value')
     
    
# =============================================================================
#     # getting the input data from the user
#     
#     
#     showalter_Index = st.text_input('Showalter index value')
#     Lifted_index  = st.text_input('Lifted index value')
#     LIFT_computed_virtual_temp  = st.text_input('LIFT computed using virtual temperature value')
#     SWEAT_index  = st.text_input('SWEAT index value')
#     K_index  = st.text_input('K index value')
#     Tot_tot_index  = st.text_input('Totals totals index value')
#     CINS_virtual_temperature  = st.text_input('CINS using virtual temperature value')
#     Convective_Available_Potential_Energy  = st.text_input('Convective Available Potential Energy value')
#     
# =============================================================================
    


    # code for Prediction
    decision = ''
    
    # creating a button for Prediction
    
    if st.button('Seeding Test Result'):
        decision = seeding_prediction([showalter_Index, Lifted_index, LIFT_computed_virtual_temp, SWEAT_index, K_index, Tot_tot_index, CINS_virtual_temperature, Convective_Available_Potential_Energy])
        example()
        
    st.success(decision)
    

# =============================================================================
#     # getting the input data from the user
#     col1, col2, col3 = st.columns(3)
# 
#     with col1:
#         Pregnancies = st.text_input('Number of Pregnancies')
# 
#     with col2:
#         Glucose = st.text_input('Glucose Level')
# 
#     with col3:
#         BloodPressure = st.text_input('Blood Pressure value')
# 
#     with col1:
#         SkinThickness = st.text_input('Skin Thickness value')
# 
#     with col2:
#         Insulin = st.text_input('Insulin Level')
# 
#     with col3:
#         BMI = st.text_input('BMI value')
# 
#     with col1:
#         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
# 
#     with col2:
#         Age = st.text_input('Age of the Person')
# 
# 
#     # code for Prediction
#     diab_diagnosis = ''
# 
#     # creating a button for Prediction
# 
#     if st.button('Diabetes Test Result'):
# 
#         user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
#                       BMI, DiabetesPedigreeFunction, Age]
# 
#         user_input = [float(x) for x in user_input]
# 
#         diab_prediction = diabetes_model.predict([user_input])
# 
#         if diab_prediction[0] == 1:
#             diab_diagnosis = 'The person is diabetic'
#         else:
#             diab_diagnosis = 'The person is not diabetic'
# 
#     st.success(diab_diagnosis)
# =============================================================================

# Farmer Warning Page
if selected == 'Farmer Warning':

    # page title
    st.title('Farmer Warning using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Healthcare Warning":

    # page title
    st.title("Healthcare Warning using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Healthcare Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by  Muhammed Alhaddad
</div>
"""
st.markdown(footer,unsafe_allow_html=True)


