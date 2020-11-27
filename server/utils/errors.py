import logging 
from config import global_log_level
logging.basicConfig(level=global_log_level)
logger = logging.getLogger(__name__)


def error_response(error: Exception or str, status=500, toConsole=True): 
    """creates a generic error response tuple with the error message and status 500 

    Args:
        error (Exception or str): Either the actual exception class or an error string that will be returned
        status (int, optional): The HTTP status code to be returned with the error. Defaults to 500.
        toConsole (bool, optional): Whether to also print the error to the console. Defaults to True.

    Returns:
        tuple(dict(str,str), int): A tuple that looks like ({"error": <errorMsg}, <HttpStatusCode>)
    """
    if (toConsole):
        logger.error(error)
        print(error)
    return {"error": str(error)}, status