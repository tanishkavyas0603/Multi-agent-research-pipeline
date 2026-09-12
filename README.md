---
title: Multi Agent Research Pipeline
emoji: 🚀
colorFrom: red
colorTo: red
sdk: streamlit
sdk_version: "1.58.0"
app_file: app.py
pinned: false
license: mit
---

live link: https://tanishka06vyas-multi-agent-research-pipeline.hf.space/
🤖 Multi-Agent Research Pipeline
📌 Overview

A Multi-Agent AI Research System that automates the research workflow using specialized AI agents. Instead of relying on a single LLM, the system divides the task among multiple agents that search, analyze, write, and review information to generate high-quality research reports.

🚀 Features
🔍 Intelligent Search Agent for information retrieval
📖 Reader Agent for extracting key insights
✍️ Writer Agent for generating structured reports
🧐 Critic Agent for reviewing and improving output
🧠 Multi-agent workflow
📄 Automatic research report generation
⚡ Fast and modular architecture
🛠️ Tech Stack
Python
LangGraph
LangChain
OpenAI GPT Models
Tavily Search API
Hugging Face Spaces
Gradio
dotenv

Project Architecture:
            User Query
                 │
                 ▼
         Search Agent
                 │
                 ▼
         Reader Agent
                 │
                 ▼
         Writer Agent
                 │
                 ▼
         Critic Agent
                 │
                 ▼
      Final Research Report

Project Structure:
multi-agent-research-pipeline/
│
├── agents.py
├── app.py
├── pipeline.py
├── prompts.py
├── requirements.txt
├── README.md
├── .env.example
└── assets/

Enviornment variables:
Create a new .env
OPENAI_API_KEY=your_key
TAVILY_API_KEY=your_key

🎯 Future Improvements
PDF export
Citation generation
Multiple search providers
Memory-enabled agents
Parallel agent execution
Research history
🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests.

📜 License

MIT License

👩‍💻 Author

Tanishka Vyas
