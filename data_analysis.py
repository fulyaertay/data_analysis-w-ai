# Import required libraries
import google.generativeai as genai
import pandas as pd


# Upload dataset
data = pd.read_csv('depression_data.csv')

# Set up Gemini API Key
GOOGLE_API_KEY = "YOUR_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Prepare analyses options
analyses = {
    1: "Analyze numerical variables Age, Number of Children, Income",
    2: "Analyze Marital Status, Education Level, Smoking Status",
    3: "Analyze Marital Status and Income",
    4: "Analyze Education Level and Income",
    5: "AnalyzeSmoking Status and Chronic Medical Conditions",
    6: "Analyze Physical Activity Level and Chronic Medical Conditions",
    7: "Analyze the correlation between Age and Income",
    8: "Analyze the correlation between Age and Number of Children",
    9: "Analyze socioeconomic factors and health outcomes",
    10: "Analyze Lifestyle choices and health outcomes",
    11: "Analyze family history and health outcomes"
}

# Show analyses options
def show_options():
    print("\nAvailable Analyses:")
    for key, description in analyses.items():
        print(f"{key}: {description}")

    # Input choice from user
    choice = int(input("\nEnter the number corresponding to the analysis you want to perform or 0 to exit: "))

    # Create prompt to send Gemini Model using 1000 samples of data file
    prompt = ""
    if choice in analyses:
        if choice == 1:
            prompt = f"Please Analyze numerical variables such as Age, Number of Children, and Income. Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        elif choice == 2:
            prompt = f"Please Analyze categorical variables such as Marital Status, Education Level, and Smoking Status. Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        elif choice == 3:
            prompt = f"Please Analyze between Marital Status and Income. Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        elif choice == 4:
            prompt = f"Please Analyze between Education Level and Income. Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        elif choice == 5:
            prompt = f"Please analyze the relationship between Smoking Status and Chronic Medical Conditions through cross-tabulation. Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        elif choice == 6:
            prompt = f"Please analyze the relationship between Physical Activity Level and Chronic Medical Conditions through cross-tabulation. Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        elif choice == 7:
            prompt = f"Please Analyze correlation between Age and Income. Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        elif choice == 8:
            prompt = f"Please Analyze the correlation between Age and Number of Children. Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        elif choice == 9:
            prompt = f"Please analyze the relationship between socioeconomic factors (Income, Education Level, Employment Status) and health outcomes (Chronic Medical Conditions). Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        elif choice == 10:
            prompt = f"Please analyze the relationship between lifestyle choices (Smoking, Physical Activity, Dietary Habits) and health outcomes (Chronic Medical Conditions). Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        elif choice == 11:
            prompt = f"Please analyze the relationship between Family History of Depression and health outcomes (Chronic Medical Conditions, Mental Health Issues). Here's a sample of the data: {data.head(1000).to_csv(index=False)}"
        
    else:
        print("Exiting the program..")
        exit()
    # Analyze choice with Generative Model
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Run model and show results to the user
    response = model.generate_content(prompt)
    print("\nAnalysis Result:")
    print(response.text)
    
# Start the program  
show_options()





