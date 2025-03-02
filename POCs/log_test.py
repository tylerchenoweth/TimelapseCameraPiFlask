from flask import Flask
import logging
import sys
import time

app = Flask(__name__)

# Store the last 10 log messages
log_messages = []

class LimitedLogHandler(logging.StreamHandler):
    def emit(self, record):
        global log_messages
        log_messages.append(self.format(record))
        if len(log_messages) > 10:
            log_messages.pop(0)
        self.display_logs()

    def display_logs(self):
        """Clears the terminal and displays the 10 most recent logs, keeping the persistent text below."""
        sys.stdout.write("\033c")  # Clear screen
        sys.stdout.write("Recent Logs:\n")
        sys.stdout.write("\n".join(log_messages) + "\n")
        sys.stdout.write("\n=== Persistent Text Below ===\n")
        sys.stdout.write("This text remains at the bottom.\n")
        sys.stdout.flush()

# Set up Flask logging
log_handler = LimitedLogHandler()
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    return "Check your terminal!"

@app.route('/log')
def log_message():
    app.logger.info("Log route accessed")
    return "Logged a message!"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
