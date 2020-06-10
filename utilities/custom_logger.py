import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    #gets the name of the class/method from which this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    #by default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(
        filename="selenium_test_zalando.log",mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter(
        '---%(asctime)s - %(name)s - %(levelname)s--- %(message)s, line %(lineno)s',
        datefmt = '%Y/%m/%d(%a) at %H:%M:%S')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger