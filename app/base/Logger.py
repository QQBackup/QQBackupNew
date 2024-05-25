# base/Logger.py
import logging

logger = logging.getLogger(__name__)
handler = logging.FileHandler("output/logs/app.log")
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
