"""Implements AppServices Class."""

from ecommerce_app.application_base import ApplicationBase
from ecommerce_app.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
import inspect

class AppServices(ApplicationBase):
    """AppServices Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = MySQLPersistenceWrapper(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')
    def get_all_products(self):
        """Get all products."""
        return self.DB.get_all_products()

    def add_product(self, name, price, description):
        """Add a product."""
        self.DB.add_product(name, price, description)
    def update_product(self, product_id, name, price, description):
        """Update a product."""
        self.DB.update_product(product_id, name, price, description)
    # COLLECTIONS

    def get_all_collections(self):
        """Get all collections."""
        return self.DB.get_all_collections()


    def add_collection(self, name, description):
        """Add a collection."""
        self.DB.add_collection(name, description)


    def update_collection(self, collection_id, name, description):
        """Update a collection."""
        self.DB.update_collection(collection_id, name, description)


    def delete_collection(self, collection_id):
        """Delete a collection."""
        self.DB.delete_collection(collection_id)