# import streamlit as st
# import pandas as pd
# import google.generativeai as genai

# # Configure the Google Generative AI with your API key
# api_key = "AIzaSyDg9kb3rOzT05MhCU32rJDOGdz2eXTTp9c"
# genai.configure(api_key=api_key)

# # Load your stats table (replace with the actual data source)
# document_id = '1vvANStnsBL1aq0qoDdieRYvnYH49ZQXC'

# def fetch_data(sheet_name):
#     # Replace spaces in the sheet name with %20 for URL encoding
#     sheet_name_encoded = sheet_name.replace(" ", "%20")
#     url = f'https://docs.google.com/spreadsheets/d/{document_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_encoded}'
#     return pd.read_csv(url)

# # def generate_match_report(match_data):
# #     """
# #     Generate a data-driven report for the selected match using Google Generative AI.

# #     Args:
# #         match_data (pd.DataFrame): The filtered match data containing relevant statistics.

# #     Returns:
# #         str: A generated report highlighting key aspects of the match.
# #     """
# #     # Convert match data to a readable format for the prompt
# #     match_details = match_data.to_dict('records')

# #     # Create a prompt with key match information
# #     prompt = f"""
# #     You are a sports analyst creating a report on a football match. Here is the match data:

# #     {match_details}

# #     Based on this data, provide a detailed report on the match. Highlight the performance of each team, the outcome,
# #     key statistics (such as goals scored, attempts on goal, shots on target, and cards), and any notable observations.
# #     Also, provide insights on how each team performed in relation to their opponent, and mention any standout players or moments.
# #     Ensure the report is professional, engaging, and data-driven.
# #     """

# #     # Call the Google Generative AI to generate the report
# #     response = genai.generate(prompt=prompt, max_tokens=500)

# #     # Extract the generated text from the response
# #     report = response.generations[0].text.strip()

# #     return report
# # def generate_match_report(match_data):
# #     """
# #     Generate a data-driven report for the selected match using Google Generative AI.

# #     Args:
# #         match_data (pd.DataFrame): The filtered match data containing relevant statistics.

# #     Returns:
# #         str: A generated report highlighting key aspects of the match.
# #     """
# #     # Convert match data to a readable format for the prompt
# #     match_details = match_data.to_dict('records')

# #     # Create a prompt with key match information
# #     prompt = f"""
# #     You are a sports analyst creating a report on a football match. Here is the match data:

# #     {match_details}

# #     Based on this data, provide a detailed report on the match. Highlight the performance of each team, the outcome,
# #     key statistics (such as goals scored, attempts on goal, shots on target, and cards), and any notable observations.
# #     Also, provide insights on how each team performed in relation to their opponent, and mention any standout players or moments.
# #     Ensure the report is professional, engaging, and data-driven.
# #     """

# #     # Initialize the generative model
# #     model = genai.GenerativeModel("gemini-1.5-flash")

# #     # Call the model to generate the report
# #     response = model.generate(prompt=prompt, max_tokens=500)

# #     # Extract the generated text from the response
# #     report = response.generations[0].text.strip()

# #     return report

# def generate_match_report(match_data):
#     """
#     Generate a data-driven report for the selected match using Google Generative AI.

#     Args:
#         match_data (pd.DataFrame): The filtered match data containing relevant statistics.

#     Returns:
#         str: A generated report highlighting key aspects of the match.
#     """
#     # Convert match data to a readable format for the prompt
#     match_details = match_data.to_dict('records')
#     # st.write(match_details)

#     # Create a prompt with key match information
#     prompt = f"""
#     You are a sports analyst creating a report on a football match. Here is the match data:

#     {match_details}

#     Based on this data, provide a detailed report on the match. Highlight the performance of each team, the outcome,
#     key statistics (such as goals scored, attempts on goal, shots on target, and cards), and any notable observations.
#     Also, provide insights on how each team performed in relation to their opponent, and mention any standout players or moments.
#     Ensure the report is professional, engaging, and data-driven.
#     """

#     # Call the model to generate the report
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(prompt)
#     # response = genai.generate(prompt=prompt, max_tokens=500)  # Use the correct function here

#     # Extract the generated text from the response
#     # report = response.generations[0].text.strip() if response.generations else "No report generated."
#     report = response.text.strip() if hasattr(response, 'text') else "No report generated."
#     return report


# # Streamlit app layout
# def main():
#     st.title("Matchday Sports News Generator")

#     # Load data and display matchday IDs
#     data = fetch_data("team stats")
#     matchday_ids = data['matchday'].unique()

#     # Matchday selection
#     selected_matchday_id = st.selectbox('Select Matchday ID', matchday_ids)

#     # Filter data by selected matchday
#     filtered_data = data[data['matchday'] == selected_matchday_id]

#     # Remove the first two columns
#     filtered_data = filtered_data.iloc[:, 2:]

#     # Extract unique match names after filtering
#     unique_match_names = filtered_data['match_name'].unique()

#     # Create a dropdown for match names
#     selected_match_name = st.selectbox('Select Match Name', unique_match_names)

#     # Filter data by selected match name
#     match_data = filtered_data[filtered_data['match_name'] == selected_match_name]

#     # Display the filtered match data
#     st.write(f"Data for Matchday ID: {selected_matchday_id} and Match: {selected_match_name}")
#     st.dataframe(match_data)

#     # Generate the match report when the user clicks the button
#     if st.button("Generate Match Report"):
#         with st.spinner("Generating report..."):
#             report = generate_match_report(match_data)
#             st.success("Report Generated!")
#             st.write(report)

# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configure the Google Generative AI with your API key
api_key = "AIzaSyDg9kb3rOzT05MhCU32rJDOGdz2eXTTp9c"
genai.configure(api_key=api_key)

# Load your stats table (replace with the actual data source)
document_id = '1vvANStnsBL1aq0qoDdieRYvnYH49ZQXC'

def fetch_data(sheet_name):
    # Replace spaces in the sheet name with %20 for URL encoding
    sheet_name_encoded = sheet_name.replace(" ", "%20")
    url = f'https://docs.google.com/spreadsheets/d/{document_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_encoded}'
    return pd.read_csv(url)

def generate_match_report(match_data, custom_prompt):
    """
    Generate a data-driven report for the selected match using Google Generative AI.

    Args:
        match_data (pd.DataFrame): The filtered match data containing relevant statistics.
        custom_prompt (str): The custom prompt provided by the user.

    Returns:
        str: A generated report highlighting key aspects of the match.
    """
    # Convert match data to a readable format for the prompt
    match_details = match_data.to_dict('records')
    # st.write(match_details)

    # Replace placeholder in the custom prompt with the match details
    formatted_prompt = custom_prompt.format(match_details=match_details)

    # Call the model to generate the report
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(formatted_prompt)

    # Extract the generated text from the response
    report = response.text.strip() if hasattr(response, 'text') else "No report generated."

    return report

# Streamlit app layout
def main():
    st.title("Matchday Sports News Generator")

    # Load data and display matchday IDs
    data = fetch_data("team stats")
    matchday_ids = data['matchday'].unique()

    # Matchday selection
    selected_matchday_id = st.selectbox('Select Matchday ID', matchday_ids)

    # Filter data by selected matchday
    filtered_data = data[data['matchday'] == selected_matchday_id]

    # Remove the first two columns
    filtered_data = filtered_data.iloc[:, 2:]

    # Extract unique match names after filtering
    unique_match_names = filtered_data['match_name'].unique()

    # Create a dropdown for match names
    selected_match_name = st.selectbox('Select Match Name', unique_match_names)

    # Filter data by selected match name
    match_data = filtered_data[filtered_data['match_name'] == selected_match_name]

    # Display the filtered match data
    st.write(f"Data for Matchday ID: {selected_matchday_id} and Match: {selected_match_name}")
    st.dataframe(match_data)

    # Text input for custom prompt
    default_prompt = """
    You are a sports analyst creating a report on a football match. Here is the match data:

    {match_details}

    Based on this data, provide a detailed report on the match. Highlight the performance of each team, the outcome,
    key statistics (such as goals scored, attempts on goal, shots on target, and cards), and any notable observations.
    Also, provide insights on how each team performed in relation to their opponent, and mention any standout players or moments.
    Ensure the report is professional, engaging, and data-driven.
    """
    custom_prompt = st.text_area("Enter your custom prompt", default_prompt, height=200)

    # Generate the match report when the user clicks the button
    if st.button("Generate Match Report"):
        with st.spinner("Generating report..."):
            report = generate_match_report(match_data, custom_prompt)
            st.success("Report Generated!")
            st.write(report)

if __name__ == "__main__":
    main()
