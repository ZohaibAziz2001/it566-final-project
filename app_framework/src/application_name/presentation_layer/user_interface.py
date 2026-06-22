"""Implements the applicatin user interface."""

from application_name.application_base import ApplicationBase
from application_name.service_layer.app_services import AppServices
import inspect
import json

class UserInterface(ApplicationBase):
    """UserInterface Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = AppServices(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')




  def start(self):
    """Start main user interface"""

    self._logger.log_debug(
        f'{inspect.currentframe().f_code.co_name}: User interface started'
    )

    while True:
        print('\n=== E-Commerce Products and Collections ===')
        print('1. Products')
        print('2. Collections')
        print('3. Product-Collection Relationships')
        print('4. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            print('Products menu coming soon...')

        elif choice == '2':
            print('Collections menu coming soon...')

        elif choice == '3':
            print('Relationships menu coming soon...')

        elif choice == '4':
            print('Goodbye')
            break

        else:
            print('Invalid choice')
