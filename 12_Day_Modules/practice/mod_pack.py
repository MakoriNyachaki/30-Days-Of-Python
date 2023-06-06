from __future__ import print_function
import random
import string

"""
Write a function which generates a six digit/character random_user_id.
    print(random_user_id());
      '1ee33d'

Modify the previous task. Declare a function named user_id_gen_by_user.
It doesn’t take any parameters but it takes two inputs using input().
One of the inputs is the number of characters and the second input is
the number of IDs which are supposed to be generated.
"""


def main():
    no_of_ids, size_of_id = map(
            int, input('Enter no. of ids and size of id separated'
                       'by space: ').split(' ')
            )
    for i in range(no_of_ids):
        print(random_user_id(size_of_id))


def random_user_id(size: int) -> str:
    return ''.join(
            [
                random.choice(string.ascii_lowercase + string.digits)
                for n in range(size)
                ]
            )


if __name__ == '__main__':
    main()
