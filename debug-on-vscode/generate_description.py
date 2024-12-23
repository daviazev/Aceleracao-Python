import random


DIGITS_MAP = {
    0: "zero",
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
}


def generate_description(integer):
    digits = list(str(integer))

    description = f"{DIGITS_MAP.get(int(digits[0]))}"
    for digit in digits[1:]:
        description += f" {DIGITS_MAP.get(digit)}"

    return description


def main():
    integer = random.randint(10000, 99999)

    description = generate_description(integer)

    print(f"Descrição do número {integer}: '{description}'")


if __name__ == "__main__":
    main()
