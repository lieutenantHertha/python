import logging
import Employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    '%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('demo.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

stream_formatter = logging.Formatter(
    '%(pathname)s:%(name)s:%(levelname)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)


def add(x, y):
    logger.info('{}+{}={}'.format(x, y, x + y))
    return x + y


def sub(x, y):
    logger.info('{}-{}={}'.format(x, y, x - y))
    return x - y


def mul(x, y):
    logger.info('{}*{}={}'.format(x, y, x * y))
    return x * y


def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by ZERO.')
    else:
        logger.info('{}/{}={}'.format(x, y, result))


add(2, 3)
sub(10, 5)
mul(3, 6)
div(9, 4)