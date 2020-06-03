import logging
import logging.config
from os import path

class logger:
    """The logger class."""
    # use absolute path from where it is called rather than
    # --> logging.config.fileConfig('log.cfg')
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'log.cfg')
    logging.config.fileConfig(log_file_path) 
    
    # create a default logger
    logger = logging.getLogger('default logger')
    
    
    def setLoggerName(name):
        """Set the logger name.
         
        Parameters
        ----------
        name : string
        Name of the logger.
    
        Returns
        -------
        logger : string
        Returns the logger.
        """
        logger = logging.getLogger(name)
        return logger
    
    
