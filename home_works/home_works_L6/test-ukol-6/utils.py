# 1. CRITICAL   50<- highest severity
# 2. ERROR      40
# 3. WARNING    30 <- Default level
# 4. INFO       20
# 5. DEBUG      10 <- lowest severity

import logging
import time
from functools import wraps

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
logging.getLogger('selenium').setLevel(logging.CRITICAL)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            log.info(f"Execution Time: {execution_time:.4f} sec")
        return result
    return wrapper