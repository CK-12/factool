import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(log_format)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logging.basicConfig(
    format=log_format,
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)