1. clone repository
git clone https://github.com/Akshaya-code-create/ai-ops-assistant-trulymadly.git
cd ai-ops-assistant-trulymadly

2. Install dependencies
pip install -r requirements.txt

3. Add your API keys to .env (copy .env.example)
cp .env.example .env
Edit .env with real keys

4. Run (one command)
python main.py


Test Examples
Try these in http://localhost:8000/docs -> POST /process:

text
1. "Get weather in Warangal" 
2. "Find top Python repositories on GitHub"
3. "Search FastAPI repos and get Delhi weather"
4. "Top 3 Streamlit repositories"
