import pytest
from protocol import (
    Response,
    Request,
    int_to_output,
    decode_request,
    encode_response,
)


def test_parse_correlation_id():
    given = b"\x00\x00\x00\x23\x00\x12\x00\x04\x6f\x7f\xc6\x61"
    request = decode_request(given)
    response = Response(0, request.correlation_id)
    actual = encode_response(response)
    expected = b"\x00\x00\x00\x00\x6f\x7f\xc6\x61"

    assert actual == expected


def test_decode_request():
    given = b"\x00\x00\x00\x23\x00\x12\x00\x04\x6f\x7f\xc6\x61"
    assert decode_request(given) == Request(35, 18, 4, 1870644833)


def test_int_to_hex_string_valid_cases():
    # Test with a 4-byte representation
    assert int_to_output(35, 4) == b"\x00\x00\x00\x23"

    # Test with a 2-byte representation
    assert int_to_output(35, 2) == b"\x00\x23"

    # Test with a maximum value for 2 bytes
    assert int_to_output(65535, 2) == b"\xff\xff"

    # Test with the maximum value for 4 bytes
    assert int_to_output(65535, 4) == b"\x00\x00\xff\xff"

    # Test zero value
    assert int_to_output(0, 4) == b"\x00\x00\x00\x00"
    assert int_to_output(0, 2) == b"\x00\x00"


def test_int_to_hex_string_edge_cases():
    # Test with 1-byte representation of maximum value
    assert int_to_output(255, 1) == b"\xff"

    # Test with 1-byte representation of zero
    assert int_to_output(0, 1) == b"\x00"
