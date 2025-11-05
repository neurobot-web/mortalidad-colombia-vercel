import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the Dash app
from app import app, server

# Vercel serverless function handler
def handler(request):
    return server