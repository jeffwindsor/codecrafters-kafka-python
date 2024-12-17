import pytest
from protocol import (
    Request,
    int_to_output,
    decode_request,
    encode_response,
)


def to_bytes(hex_string: str) -> bytes:
    return bytes.fromhex(hex_string)


# def test_parse_correlation_id():
#     given = to_bytes("00000023001200046f7fc661")
#     actual = encode_response(decode_request(given))
#     expected = to_bytes("000000006f7fc6610023")

#     assert actual == expected


def test_decode_request():
    given = to_bytes("00000023001200046f7fc661")
    assert decode_request(given) == Request(35, 18, 4, 1870644833)


def test_int_to_hex_string_valid_cases():
    # Test with a 4-byte representation
    assert int_to_output(35, 4) == to_bytes("00000023")

    # Test with a 2-byte representation
    assert int_to_output(35, 2) == to_bytes("0023")

    # Test with a maximum value for 2 bytes
    assert int_to_output(65535, 2) == to_bytes("ffff")

    # Test with the maximum value for 4 bytes
    assert int_to_output(65535, 4) == to_bytes("0000ffff")

    # Test zero value
    assert int_to_output(0, 4) == to_bytes("00000000")
    assert int_to_output(0, 2) == to_bytes("0000")


def test_int_to_hex_string_edge_cases():
    # Test with 1-byte representation of maximum value
    assert int_to_output(255, 1) == to_bytes("ff")

    # Test with 1-byte representation of zero
    assert int_to_output(0, 1) == to_bytes("00")
