import logging
# we can set the logging basic config such as time and format 

#logging.basicConfig(level= , format= , datefmt= )

logging.basicConfig(
     filename='log_file_name.log',
     level=logging.DEBUG, 
     format= '[%(asctime)s] - %(name)s -  %(levelname)s - %(message)s',
     datefmt='%m/%d/%Y %H:%M:%S'
 )

# using helper for customised logger
import helper

# tutorial about logging
"""
There are 5 levels into logging
"""

# logging.debug("This is for debugging")
# logging.info("Info message")
# # more severe logging

# logging.warning("Warning")
# logging.error("This is error")
# logging.critical("This is critical")

