"""https://www.codewars.com/kata/592e830e043b99888600002d/train/python"""
import string


def encode(message, key):
    alpha_dict = {alpha: num for num, alpha in enumerate(string.ascii_lowercase, start=1)}
    decode_message = [alpha_dict[i] for i in message]
    key_list = list(map(int, str(key)))
    full_key_list = (key_list * (int(len(decode_message) // len(key_list)) + 1))[:len(decode_message):]
    return [a + b for a, b in zip(decode_message, full_key_list)]


print(encode("scout", 1939))
