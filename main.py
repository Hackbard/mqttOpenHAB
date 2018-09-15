import configparser
import logging


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    logging.getLevelName(config.get('LOG', 'LEVEL'))

    log_level = logging._nameToLevel.get(config.get('LOG', 'LEVEL'))
    log_file = config.get('LOG', 'FILE')

    logging.basicConfig(level=log_level, filename=log_file, format='%(relativeCreated)6d %(levelname)s %(message)s')

    logging.info("Start Service")


if __name__ == '__main__':
    main()
