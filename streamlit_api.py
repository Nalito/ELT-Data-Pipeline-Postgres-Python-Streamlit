import streamlit as st
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to predict employee happiness
def predict_happiness(occupation, salary, level, vacation):
    # Preprocess the input features if needed
    # ...

    # Make the prediction using the trained model
    prediction = model.predict([[occupation, salary, level, vacation]])

    return prediction[0]

# Streamlit app
def main():
    # Set the title and description of the app
    st.title('Employee Happiness Prediction')
    st.write('Enter the employee details to predict their happiness.')

    # Get user inputs
    occupation = st.number_input('Occupation', min_value=0, max_value=5, step=1)
    salary = st.number_input('Salary', min_value=100000, max_value=750000, step=1)
    level = st.number_input('Level', min_value=0, max_value=2, step=1)
    vacation = st.number_input('Vacation', min_value=0, max_value=1, step=1)

    # Make the prediction when the user clicks the 'Predict' button
    if st.button('Predict'):
        prediction = predict_happiness(occupation, salary, level, vacation)
        st.write('Predicted Happiness: ', prediction, ' out of 5 stars')

# Run the app
if __name__ == '__main__':
    main()
