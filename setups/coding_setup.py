import os
import subprocess
import webbrowser
from core.logger import logger

def start_coding_setup():
  logger.info("Starting coding environment setup.")

  try:
    #1. open apps
    vscode_path = "C:\\Users\\91835\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    subprocess.Popen(vscode_path)
    subprocess.Popen("Notepad.exe")
    
    #2. open websites
    webbrowser.open("https://chatgpt.com")
    webbrowser.open("https://stackoverflow.com")
    webbrowser.open("https://github.com")
    
    #3. open files/folders
    project_path = "C:\\Users\\91835\\Desktop\\Completed-Projects\\vexa"
    os.startfile(project_path)
    
    logger.info("Coding environment setup completed.")
    
  except Exception as e:
    logger.error(f'Error during coding setup: {e}')