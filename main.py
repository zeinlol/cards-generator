from time import sleep

from card_numbers import generate_random_card_number


def main():
    while True:
        card_num = generate_random_card_number()
        print(card_num)


if __name__ == '__main__':
    main()

# TODO add arguments
# choose prefix
# choose number of cards
# generate cvv or not
# output file
# json output


