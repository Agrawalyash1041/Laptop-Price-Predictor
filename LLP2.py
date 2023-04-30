### Importing Important Libraries

import streamlit as st
import pickle
import numpy as np
from streamlit_lottie import st_lottie
import requests

### Importing the data and model using pickle

dataset = pickle.load(open('Dataset.pkl','rb'))
model = pickle.load(open('rf_model.pkl','rb'))


### Deploying The Web 

### Creating The  Page Title

st.set_page_config(page_title = "Lapptop Price Predictor",
                   page_icon = '💻',
                   layout = 'wide')

### Deploying the Animation

## Creating a user defined function

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


## Loading assets
lottie_laptop = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_efx3aac9.json")





### Title 

### Deploying animation

with st.container():
    left_column, right_column = st.columns(2)
    with right_column:
        st_lottie(lottie_laptop, height=400, key="coding")
        with left_column:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            
            
            
            
            st.title(' Laptop Price Predictor')
    
        
        
        
        
        
st.write("---")   
st.subheader('Hello User , Welcome to this Laptop Price Predicting Interface')
st.text("This Prediction model has a accuracy of 82% only")



### Company

Brand = st.selectbox('Brand(Please Select the Brand of Laptop)',dataset['Company'].unique()) 

### Type of Laptop

     
Type = st.selectbox('Laptop Type(Please Select the Type of Laptop)',dataset['TypeName'].unique())

## Inches 

Inches = st.number_input('Inches (PLease input the Screen Size)')

### Processor 

Processor = st.selectbox('Name of the Processor (Please Select the Name of Processor)',dataset['Processor_Brand'].unique())

### GPU 

GPU = st.selectbox('GPU Brand (Please Select the Brand of GPU)',dataset['Gpu_Brand'].unique())

### Ram 

Ram = st.selectbox('Ram(Please Select the Ram)',[2,4,6,8,12,16,24,32,64])

### HDD 

HDD = st.selectbox('HDD(Please Select amount of HDD )',[ 0,32,128,500,1000,2000])

### SSD

SSD = st.selectbox('SSD(Please Select amount of SSD )',[ 0,8,16,32,64,128,180,240,256,512,768,1000,1024])

### Weight 

Weight = st.number_input('Weight of the Laptop (PLease input the Weight of Laptop)')

### OS 

OS = st.selectbox('OS(Please Select Operating System )',dataset['OS'].unique())

## IPS 

IPS = st.selectbox('IPS Display(Please Select if there is IPS Display or Not )',['No','Yes'])

### Touchscreen 

Touchscreen = st.selectbox('Touchscreen Display(Please Select if there is Touchscreen Display or Not )',['No','Yes'])
     
     

        
        
### Predicting the Model


if st.button('Predict Price'):
    if IPS == 'Yes':
        IPS = 1 
    else:
        IPS = 0
        
    if Touchscreen == 'Yes':
        Touchscreen = 1
    else:
        Touchscreen = 0
            
    group = np.array([Brand,Type,Inches,Processor,GPU,Ram,HDD,SSD,Weight,OS,IPS,Touchscreen])
    group = group.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(model.predict(group)[0]))))
    st.snow()
    
    ### Deploying the animation
    

st.text("If you want to change the Configuragtion Please Reload the website for better Results")
st.write("")
st.write("")
st.write("")

### Contact Info 

st.subheader("By Yash.N.Agrawal")
st.write("")
st.write("")
st.write("")

st.subheader("Feel free to contact the Devloper 😉")
st.write("")
st.write("")

st.markdown("[🎉 Instagram ](https://www.instagram.com/agrawalyash1041/)")
st.write("")
st.markdown("[ 📧 Gmail ](    https://mail.google.com/mail/?view=cm&fs=1&to=yashagrawal1041@gmail.com&su=SUBJECT&body=BODY)")



   
    





 
   
    
    




