import packages.dateTime_module as dm
import packages.math_module as mm
import packages.random_module as rm
import packages.uuid_module as um
import packages.file_module as fm
import packages.attribute_module as am


print('=============================================')
print('Welcome to Multi-Utility Toolkit')


while True:
    print('=============================================')
    print('1. DateTime and Time Operations')
    print('2. Mathematical Operations')
    print('3. Random Data Generation')
    print('4. Generate Unique Identifiers (UUID)')
    print('5. File Operations (Custom Module)')
    print('6. Explore Module Attributes (dir())')
    print('7. Exit')
    print('=============================================')

    choice = int(input('Enter your choice: '))

    match choice:
        case 1:
            dm.main()
        case 2:
            mm.main()
        case 3:
            rm.main()
        case 4:
            um.generate_uuid()
        case 5:
            fm.main()
        case 6:
            am.main()
        case 7:
            break
        case _:
            print('\nInvalid choice!\n')