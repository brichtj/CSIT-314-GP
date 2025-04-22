# utils.py
import traceback

def log_exception(e: Exception):
    print(f"Error: {e}")
    print("Stack trace:")
    print(traceback.format_exc())
