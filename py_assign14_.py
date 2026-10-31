
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Different logging levels
logging.debug("This is a debug message")
logging.info("Program execution started")
logging.warning("This is a warning message")
logging.error("An error has occurred")
logging.critical("This is a critical error")

# Logging inside a function
def divide(a, b):
    try:
        result = a / b
        logging.info("Division performed successfully")
        return result
    except ZeroDivisionError:
        logging.exception("Cannot divide by zero")

print("Result:", divide(10, 2))
divide(10, 0)

print("Logging operations completed.")
