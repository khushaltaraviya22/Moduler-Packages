if __name__ == "__main__":
    print('Welcome to Attribute Module')


def main():

    print('Explore Module Attributes:')

    module = input('Enter module name to explore:- ')

    print(f'Available Attributes in {module} module: \n {dir(module)}')