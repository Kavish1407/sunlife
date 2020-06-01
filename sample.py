import os
import logging
logging.basicConfig(level=logging.INFO)
x = os.environ["stackid"]
logging.info("stack id is:"+x)