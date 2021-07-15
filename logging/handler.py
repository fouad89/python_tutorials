import logging 

logger = logging.getLogger('example')

# create handler
stream_h = logging.StreamHandler()
# log fil
file_h = logging.FileHandler('file2.log')
    
# formatting and levels
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)


logger.warning('this is a warning')
logger.error('this is an error')
