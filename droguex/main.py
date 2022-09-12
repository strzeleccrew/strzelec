from droguex.product_input_interface.input_interface import InputInterface


class Main:
    def __init__(self):
        self.interface = InputInterface()

    def main(self):
        while True:

            print(
                "Hello user. Choose what you want to do:\n"
                "1. Add new product\n"
                "0. Quit\n"
            )
            choice = input("Enter choice: ")
            if choice == "1":
                self.interface.warehouse_interface()
            elif choice == "0":
                break
            else:
                print("There is no such choice. Please enter valid choice")


if __name__ == '__main__':
    Main().main()
