import sys
import threading
import io
class LoggerStream(io.StringIO):
    def __init__(self, callback_function, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback_function = callback_function

    def write(self, s):
        super().write(s)
        sys.__stdout__.write(s)  # Write to the original sys.stdout as well
        if self.callback_function:
            self.callback_function(s)




def start_logging():
    logger_stream = LoggerStream(callback_function=update_server_log)
    sys.stdout = logger_stream

# Start the logging in a separate thread
logging_thread = threading.Thread(target=start_logging)
logging_thread.daemon = True
logging_thread.start()