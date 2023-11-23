import sys
import io
import signal

class python_executor:
    def __init__(self):
        pass

    def timeout_handler(self, signum, frame):
        raise TimeoutError()

    def run_single(self, program, timeout=10):
        buffer = io.StringIO() # Create an in-memory buffer for the output
        stdout = sys.stdout # Save the original standard output
        sys.stdout = buffer # Redirect the standard output to the buffer
        signal.signal(signal.SIGALRM, self.timeout_handler) # Set the signal handler
        signal.alarm(timeout) # Set the alarm
        try:
            exec(program)
        except TimeoutError:
            sys.stdout = stdout  # Restore the original standard output
            return "Execution timed out"
        except Exception as e:
            # Handle the error here
            error_message = str(e)
            sys.stdout = stdout  # Restore the original standard output
            return error_message
        finally:
            signal.alarm(0) # Cancel the alarm

        sys.stdout = stdout # Restore the original standard output
        output = buffer.getvalue() # Get the output from the buffer
        return output

    def run(self, snippet):
        if snippet == None:
            return None
        exec_result = self.run_single(snippet)
        if exec_result and 'False' in exec_result:
            exec_result = 'False'
        else:
            exec_result = 'True'
        return exec_result