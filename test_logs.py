import logging
import logstash
import sys


def main():
    host = '0.0.0.0'

    test_logger = logging.getLogger('python-logstash-logger')
    test_logger.setLevel(logging.INFO)
    handler = logstash.TCPLogstashHandler(host, 5000, version=1)
    test_logger.addHandler(handler)

    test_logger.error('test error')
    test_logger.info('test info message')
    test_logger.warning('test warning message')

if __name__ == "__main__":
    main()