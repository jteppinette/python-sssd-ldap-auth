import base64
import struct
from operator import itemgetter
from typing import Optional, Tuple, Union

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

METHODS = [
    {
        "algo": algorithms.AES,
        "mode": modes.CBC,
        "key_len": 32,
        "iv_len": 16,
    }
]

PopResult = Tuple[bytes, Union[bytes, Tuple]]


def pop(binary: bytes, length: int, unpack: Optional[str] = None) -> PopResult:
    """
    Return the remainding binary data and the requested binary segment.

    If the unpack keyword arguent is provided, then the requested segment
    will be unpacked accordingly. i.e. The unpack argument will be used as
    the unpack format. When using the unpack functionality, the second
    tuple index will be a tuple of unpacked items.
    """
    if len(binary) < length:
        raise Exception("requested segment too large")

    segment = binary[:length]
    remainder = binary[length:]

    if unpack:
        return remainder, struct.unpack(unpack, segment)

    return remainder, segment


def deobfuscate(token: str) -> str:
    """
    Consume an obfuscated token and return the unobfuscated password.
    """
    binary = base64.b64decode(token)

    binary, (method, ciphertext_len) = pop(binary, 4, "HH")

    try:
        properties = METHODS[method]
    except IndexError:
        raise Exception("unsupported method")

    algo, mode, key_len, iv_len = itemgetter("algo", "mode", "key_len", "iv_len")(
        properties
    )

    binary, encryption_key = pop(binary, key_len)
    binary, iv = pop(binary, iv_len)
    binary, ciphertext = pop(binary, ciphertext_len)

    cipher = Cipher(algo(encryption_key), mode(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()

    # Anything after \x00 can be thrown away.
    password_binary = decrypted.split(b"\x00")[0]

    # UTF-8 passwords are supported (and any subset encodings e.g. ASCII).
    return password_binary.decode("utf-8")
