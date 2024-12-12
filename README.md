# Virtual HR - Mock Interview Simulator

Virtual HR is a web application that simulates mock interviews using the power of AI. The tool allows users to upload their resumes in PDF format, specify a job description, and engage in interactive, AI-driven mock interviews tailored to their profile.

## Features

- **Resume Processing**: Upload a PDF resume, and the app extracts its content for analysis.
- **Job Description Integration**: Enter the desired job role or description to generate context-specific interview questions.
- **AI-Powered Mock Interviews**: Leverages Google Gemini API to simulate realistic interview scenarios.
- **Interactive Q&A Loop**: Provides iterative question-and-answer rounds to enhance interview preparedness.

## Tech Stack

- **Frontend**: Streamlit for an interactive user interface.
- **Backend**: Python for core functionality.
- **APIs**: Google Gemini API for generating interview responses.
- **Libraries**:
  - PyPDF2: For extracting text from uploaded PDF resumes.
  - dotenv: For secure API key management.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/virtual-hr.git
   cd virtual-hr
   ```

2. **Install Dependencies**
   Ensure you have Python installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   - Create a `.env` file in the project root.
   - Add your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```
   Open the displayed local URL in your browser to use the app.

## How It Works

1. **Upload Your Resume**: Provide a PDF file of your resume.
2. **Enter Job Role**: Specify the job role or description.
3. **Start Mock Interview**: Begin the interview process and interact with the AI for practice.
4. **Iterate**: Answer questions, receive feedback, and prepare for real interviews.

## Contributions

Contributions are welcome! Feel free to fork this repository and submit pull requests for new features or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Powered by [Google Gemini API](https://cloud.google.com/generative-ai) and [Streamlit](https://streamlit.io/).
- Inspired by the need for efficient and personalized interview preparation tools.

---

### Contact

If you have any questions or suggestions, feel free to reach out at hariprasathnt@yahoo.com .s

