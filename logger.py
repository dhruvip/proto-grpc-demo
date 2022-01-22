import logging
logging.basicConfig(
    format = (
        '%(asctime)s.%(msecs)s:%(name)s:%(thread)d'
        ':%(levelname)s [%(pathname)s (%(lineno)d) (%(process)d)]: %(message)s'),
    level = logging.INFO)
LOGGER = logging.getLogger('proto-demo')