"""Implements the application user interface."""

from ecommerce_app.application_base import ApplicationBase
from ecommerce_app.service_layer.app_services import AppServices
import inspect


class UserInterface(ApplicationBase):
    """UserInterface Class Definition."""

    def __init__(self, config: dict) -> None:
        """Initializes object."""
        self._config_dict = config
        self.META = config["meta"]

        super().__init__(
            subclass_name=self.__class__.__name__,
            logfile_prefix_name=self.META["log_prefix"]
        )

        self.DB = AppServices(config)

        self._logger.log_debug(
            f'{inspect.currentframe().f_code.co_name}: It works!'
        )

    def start(self):
        """Start main user interface."""

        self._logger.log_debug(
            f'{inspect.currentframe().f_code.co_name}: User interface started'
        )

        while True:
            print("\n=== E-Commerce Products and Collections ===")
            print("1. Products")
            print("2. Collections")
            print("3. Product-Collection Relationships")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.products_menu()

            elif choice == "2":
                self.collections_menu()

            elif choice == "3":
                print("Relationships menu coming soon...")

            elif choice == "4":
                print("Goodbye")
                break

            else:
                print("Invalid choice")

    def products_menu(self):
        """Display the Products menu."""

        while True:
            print("\n=== Products Menu ===")
            print("1. View Products")
            print("2. Add Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                products = self.DB.get_all_products()

                print("\n=== Products ===")

                if not products:
                    print("No products found.")
                else:
                    for product in products:
                        print(product)

            elif choice == "2":
                name = input("Product name: ")
                price = float(input("Price: "))
                description = input("Description: ")

                self.DB.add_product(
                    name,
                    price,
                    description
                )

                print("Product added successfully!")

            elif choice == "3":
                product_id = int(input("Product ID: "))
                name = input("New product name: ")
                price = float(input("New price: "))
                description = input("New description: ")

                self.DB.update_product(
                    product_id,
                    name,
                    price,
                    description
                )

                print("Product updated successfully!")

            elif choice == "4":
                product_id = int(input("Product ID to delete: "))

                self.DB.delete_product(product_id)

                print("Product deleted successfully!")

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

    def collections_menu(self):
        """Display the Collections menu."""

        while True:
            print("\n=== Collections Menu ===")
            print("1. View Collections")
            print("2. Add Collection")
            print("3. Update Collection")
            print("4. Delete Collection")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                collections = self.DB.get_all_collections()

                print("\n=== Collections ===")

                if not collections:
                    print("No collections found.")
                else:
                    for collection in collections:
                        print(collection)

            elif choice == "2":
                name = input("Collection name: ")
                description = input("Description: ")

                self.DB.add_collection(
                    name,
                    description
                )

                print("Collection added successfully!")

            elif choice == "3":
                collection_id = int(input("Collection ID: "))
                name = input("New collection name: ")
                description = input("New description: ")

                self.DB.update_collection(
                    collection_id,
                    name,
                    description
                )

                print("Collection updated successfully!")

            elif choice == "4":
                collection_id = int(input("Collection ID to delete: "))

                self.DB.delete_collection(collection_id)

                print("Collection deleted successfully!")

            elif choice == "5":
                break

            else:
                print("Invalid choice.")
