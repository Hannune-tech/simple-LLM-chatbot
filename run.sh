#!/bin/bash

# Start the backend server
python3 ./backend/main.py &

# Start the frontend server
streamlit run ./frontend/main.py &