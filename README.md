# Solar Industry AI Assistant

A Streamlit-powered chatbot that provides expert insights on solar energy with knowledge Areas :-
- Solar Panel Technology 
- Installation Processes 
- Maintenance Requirements 
- Cost & ROI Analysis 
- Industry Regulations 
- Market Trends 
 Adapting its responses based on user expertise.
 Built using Groq API and LangChain.

 Project Link : https://solarassistant.streamlit.app/

## Features
- **Adaptive Responses:** Tailors explanations for technical and non-technical users.
- **Technical Mode:** Provides industry standards, efficiency metrics, and technical specifications.
- **Non Technical Mode:** Uses analogies, emojis, and cost-based insights for easy understanding.


- **User-Friendly Interface:** Built with Streamlit for an interactive chat experience.





## Installation and  Setup
 **1) Clone the repository:** 
```bash
  git clone https://github.com/ouibhav/SolarAssisstant.git 
  cd SolarAssisstant
```
**2) Create a virtual environment and Install Dependencies:** 
  
  ```bash
  python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
**3) Set up environment variables:** 

  - Create a .env file in the project root.
  - Add your Groq API key:
  

```bash
  GROQ_API_KEY=your_api_key_here
```

**4) Running the Application**



```bash
  streamlit run app.py
```
## Implementation Details
**groq_client.py** 
- Defines the GroqClient class for interacting with the Groq API.
- Implements adaptive responses based on user expertise.
**app.py** 
- Initializes the chatbot UI with Streamlit.
- Provides sidebar controls for expertise level and model selection.
- Manages session state to store chat history.

## Example Usecases:
- Asking question **"Explain PID in solar arrays"** in **Technical Mode**
![Image](https://github.com/user-attachments/assets/096a28f6-1b02-43d9-b80a-266738166ef0)

- Asking same question **"Explain PID in solar arrays"** in **Non Technical Mode**
![Image](https://github.com/user-attachments/assets/9da37482-b2cb-41e8-b638-2401525df206)

- Asking a **Technical** question:
![Image](https://github.com/user-attachments/assets/2897a19a-b716-48ff-8442-2215d99512dd)

- Asking a **Non Technical** question:
![Image](https://github.com/user-attachments/assets/01e508c5-6986-4405-a091-7f25937301f3)


## Future Improvements
- Add support for more AI models.
- Implement a database for storing user interactions.
- Enhance response generation with retrieval-augmented generation (RAG).

