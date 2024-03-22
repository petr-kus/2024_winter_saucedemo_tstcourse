import sys
import time
from loguru import logger


logger.remove()
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>", colorize=True)


def wait(t: float = 0.5) -> None:
    time.sleep(t)


class Log:
    major_id = 0
    minor_id = 0

    def setup_method(self, method):
        Log.major_id += 1
        Log.minor_id = 1

    def log_pass(self):
        if Log.minor_id == 1:
            print("\033[F\033[K", end="", flush=True) # HACK stderr: "DevTools listening in.." when running --headless=new chrome option
        logger.info(f"Test Step {Log.major_id}.{Log.minor_id}: PASSED")
        Log.minor_id += 1

    def log_fail(self):
        logger.error(f"Test Step {Log.major_id}.{Log.minor_id}: FAILED")