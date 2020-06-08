import logging
import logging.config
from os import path

class logger:
    """The logger class."""
    # use absolute path from where it is called rather than
    # # --> logging.config.fileConfig('log.cfg')s
    dirname = path.dirname(__file__)
    log_file_path = path.join(dirname, 'log.cfg')

    logging.config.fileConfig(log_file_path) 
    

    def getLogger(name):
        """Get the logger name.
         
        Parameters
        ----------
        name : string
        Name of the logger.
    
        Returns
        -------s
        logger : string
        Returns the logger.
        """
        logger = logging.getLogger(name)
        return logger
