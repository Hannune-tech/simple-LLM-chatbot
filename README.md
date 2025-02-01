# simple-LLM-chatbot

## Overview
This repository hosts a simple LLM chatbot that utilizes various API providers, focusing on pay-per-use pricing models instead of monthly subscriptions. The project aims to provide a cost-effective solution for using Language Model APIs while maintaining a flexible structure for future development.

Key aspects:
- Pay-per-use model to optimize costs
- Modular architecture for easy customization
- Clear separation between frontend and backend
- Extensible design for adding new features
- Support for multiple LLM API providers
- Option to integrate local models for users with personal servers


## Features

### Cost-Effective API Usage
- Utilizes pay-per-use pricing models from various LLM API providers
- Sidebar display for total billing information
- Real-time token usage and cost tracking for the current session

### Flexible Architecture
- Frontend built with Streamlit for rapid UI development
- Backend powered by FastAPI for efficient API handling
- Separation of concerns allowing easy integration of new API providers

### API Provider Support
- OpenAI GPT models
- Ollama (for local model deployment)
- Anthropic Claude models(TODO)

## Setup and Usage
1. Run `setup.sh` for setup
2. Add urls and api keys
3. Run `run.sh` for frontend and backend at the same time.

## Project Structure
frontend/<br>
├── main.py<br>
├── send_requests.py<br>
└── config.py<br>
backend/<br>
├── main.py<br>
└── models_api.py



## Future Enhancements
- Integration of Elasticsearch for conversation tracking
- Addition of more API providers
- Implementation of Socket.io or Redis for improved session management

## Contributing
Contributions to enhance the chatbot's functionality or add support for new API providers are welcome. Please read our contributing guidelines before submitting pull requests.


## License
MIT License
