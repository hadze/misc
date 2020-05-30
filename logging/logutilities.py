import logging
import logging.config

class logger:
    """The logger class."""
     
    logging.config.fileConfig('log.cfg')
    
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
    
    
