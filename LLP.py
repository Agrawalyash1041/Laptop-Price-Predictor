### Importing Important Libraries

import streamlit as st
import pickle
import numpy as np
import sklearn
import scikit-learn

### Importing the data and model using pickle

dataset = pickle.load(open('Dataset.pkl','rb'))
model = pickle.load(open('rf_model.pkl','rb'))


### Deploying The Web 

### Creating The  Page Title

st.set_page_config(page_title = "Lapptop Price Predictor",
                   page_icon = '💻',
                   layout = 'wide')

### Title 

st.title('Laptop Price Preictor')
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

Ram = st.selectbox('Ram(Please Select the Ram)',[ 8, 16,  4,  2, 12,  6, 32, 24, 64])

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
    

st.subheader("Created By Yash.N.Agrawal")
 
   
    
    




