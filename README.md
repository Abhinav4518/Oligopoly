# AI Interactive Study Tool - Oligopoly

This is an interactive study assistant inspired by NotebookLM, built for the Markaroo internship assignment. It processes AQA Economics content (Oligopoly) and YouTube lectures into a multi-modal study guide.

## Features
1.  **Audio Two-Person Dialogue:** Simulates a teacher-student podcast using `gTTS` (Google Text-to-Speech) to explain Interdependence and Price Rigidity.
2.  **Video Summaries:** Embeds relevant lectures with synthesized bullet points for exam preparation.
3.  **Interactive Q&A:** A chat interface allowing students to query the knowledge base about specific concepts like the "Kinked Demand Curve" or "Nash Equilibrium".

## How to Run Locally
1.  Clone the repo.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run the app: `streamlit run app.py`

## Tech Stack
* **Python & Streamlit:** For rapid interactive UI development.
* **gTTS:** For generating audio explanations.
