import sys
from loguru import logger


logger.remove()
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>", colorize=True)


class Log:
    major_id = 0
    minor_id = 0

    def setup_method(self, method):
        Log.major_id += 1
        Log.minor_id = 1

    def log_pass(self):
        logger.info(f"Test Step {Log.major_id}.{Log.minor_id}: PASSED")
        Log.minor_id += 1

    def log_fail(self):
        logger.error(f"Test Step {Log.major_id}.{Log.minor_id}: FAILED")