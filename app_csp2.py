# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:49:35 2024

@author: IT Department
"""

import numpy as np
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_extras.let_it_rain import rain
import datetime


# page config function
st.set_page_config(
    page_title="Cloud Seeding Program",
    page_icon=":droplet:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

def add_logoo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

my_logo = add_logoo(logo_path="pic/NCM_CSP_logo_blue.png", width=392, height=168)
st.sidebar.image(my_logo)

# OR
# st.sidebar.image(add_logoo(logo_path='C:/Users/IT Department/Downloads/qr_code/NCM_CSP_logo_blue.png', width=50, height=60)) 



# sidebar for navigation
with st.sidebar:
    selected = option_menu('Tailored Warning System',

                           
                           ['Informed Cloud Seeding Decision',
                            'Farming and food',
                            'Health',
                            'Flood',
                            'Air Quality',
                            'Tourism',
                            'Public weather services'],
                           menu_icon='⚠️',
                           icons=['cloud-hail', 'megaphone', 'heart-pulse','water','wind','globe-americas','megaphone'],
                           default_index=0)








# Cloud Seeding Program Page
if selected == 'Cloud Seeding Program':
    
# =============================================================================
#     # Devider
#     st.divider()
# =============================================================================
    

# =============================================================================
# # this to make banner in middel but it didn't looks good
#     col1, col2, col3 = st.columns(3)
#     
#     with col1:
#         st.write(' ')
#     
#     with col2:
#         st.image(add_logoo(logo_path='C:/Users/IT Department/Downloads/Streamlit Apps/multiple-disease-prediction-streamlit-app-main/pic/csp banner ewbsite.png', width=2000, height=150)) 
#     
#     with col3:
#         st.write(' ')
# =============================================================================
    
    
    st.image(add_logoo(logo_path='pic/csp banner ewbsite.png', width=1450, height=200)) 
    
    
    
    # page title centered:
    st.markdown("<h3 style='text-align: center; color: black;'>البرنامج الإقليمي لإستمطار السحب</h1>", unsafe_allow_html=True)
    #st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)

    # text under title centered
    st.markdown("<h5 style='text-align: center; color: black;'>هـو نـوع مـن عمليـات تعديـل الطقـس الـذي يهـدف إلــى تغييــر كميــة أو نــوع هطــول األمطــار الــذي يســقط مــن الســحب، وذلــك بنشــر وإطــاق أنــواع مختصــه مــن المــواد الكيميائيــة فــي الهــواء والتــي تسـاعد علـى تكاثـف السـحب أو النــوى الجليديـة، ممـا يغيــر العمليــات الفيزيائيــة الدقيقــة داخــل الســحابة. </h2>", unsafe_allow_html=True)

    # page title
   # st.header('Cloud Seeding Program', divider='rainbow')





    
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



    
    #st.image(add_logoo(logo_path='pic/radargif.gif', width=1036, height=680)) 
    
    left_co, cent_co,last_co = st.columns(3)
    with left_co: 
        st.image(add_logoo(logo_path='pic/sky.jpg', width=1036, height=680))
    with cent_co:
        st.image(add_logoo(logo_path='pic/cloud11.jpg', width=1036, height=680))
    with last_co: 
        st.image(add_logoo(logo_path='pic/plane2.jpg', width=1036, height=680))
        
        
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
    return "Clouds are Suitable for Seeding"
##########################################################################
# =============================================================================
# =============================================================================
# =============================================================================

def modelfun(ind1,ind2,ind3,ind4,ind5,ind6,ind7,ind8,ind9):
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
            return example()
      
    

    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    

    with col1:
        showalter_Index = st.text_input('Showalter index value',value=ind1)

    with col2:
        Lifted_index  = st.text_input('Lifted index value',value=ind2)

    with col3:
        LIFT_computed_virtual_temp  = st.text_input('LIFT using virtual temperature value',value=ind3)

    with col1:
        SWEAT_index  = st.text_input('SWEAT index value',value=ind4)

    with col2:
        K_index  = st.text_input('K index value',value=ind5)

    with col3:
        Tot_tot_index  = st.text_input('Totals totals index value',value=ind6)

    with col1:
        CINS_virtual_temperature  = st.text_input('CINS using virtual temperature value',value=ind7)

    with col2:
        Convective_Available_Potential_Energy  = st.text_input('CAPE value',value=ind8)
    with col3:
        Jefferson_index = st.text_input('Jefferson index',value=ind9)
     
    
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
        
        
        st.success(decision)
# =============================================================================
# =============================================================================
# =============================================================================

# Seeding Decision Page
if selected == 'Informed Cloud Seeding Decision':
    



    # =============================================================================
    # page title
    #st.title('Cloud Seeding Predictive Decision Support System Using Artificial Intelligent Model')

    
    # image titale 
    st.markdown("<h3 style='text-align: center; color: black;'>Process Overview</h3>", unsafe_allow_html=True)

    # image of the ai page 
    st.image(add_logoo(logo_path='pic/ai1.png', width=1450, height=200))
    st.divider()


    # =============================================================================

    
    st.markdown("<h3 style='text-align: left; color: black;'>Cloud Seeding Predictive Decision Support System Using Artificial Intelligent Model</h3>", unsafe_allow_html=True)

    
    # =============================================================================


    #### 
    
    st.write('')
    genre = st.radio(
    "***Select a City:***",
    ["Riyadh", "Abha", "Hail"],
    captions = ["Central Region", "Southwest Region", "Northwest Region"],
    horizontal = 1,
    index = None
    )

    st.divider()

    if genre == 'Abha':
        st.write('')
        st.markdown("<h3 style='text-align: left; color: black;'>No Data Available.</h1>", unsafe_allow_html=True)
    
    elif genre == 'Hail':
        st.write('')
        st.markdown("<h3 style='text-align: left; color: black;'>No Data Available.</h1>", unsafe_allow_html=True)
    
    elif genre == 'Riyadh':
        
        
        # ==========================================
        dateBut = st.date_input("Select Date", datetime.date(2023, 3, 1))
        print(dateBut)
       
        st.divider()
       
        
       
        if dateBut == datetime.date(2023, 3, 2):
            print('second print')
            print(dateBut)
            print('ffdf')
            
            
            
            modelfun(-0.44,-0.36, -0.91, 311.75, 33.7, 49, -143.63, 134.09, 22.02)
            
        # ==========================================
            
        elif dateBut == datetime.date(2023, 3, 4):
            
                
                modelfun(-4.14, -1.58, -2.13, 304.8, 41.6, 53.8, -154.9, 570.58, 27.41)
            
        # ------------------------------------------
                

        else: 
            st.write('')
            
    

    else: 
        st.write('')
        


    

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
<p>Developed with ❤ by  Cloud Seeding Team
</div>
"""
st.markdown(footer,unsafe_allow_html=True)


