import os
import logging
logging.basicConfig(level=logging.INFO)
x = os.getenv("stackid")
logging.info("stack id is:"+x)