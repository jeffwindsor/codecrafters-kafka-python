import pytest
from protocol import (
    Response,
    Request,
    int_to_hex_string,
    decode_request,
    encode_response,
)


def test_parse_correlation_id():
    given = (
        "00000023001200046F7FC66100096B61666B612D636C69000A6B61666B612D636C6904302E3100"
    )
    request = decode_request(given)
    response = Response(0, request.correlation_id)
    actual = encode_response(response)
    expected = "000000006F7FC661"

    assert actual == expected


def test_decode_request():
    assert decode_request("00000023001200046F7FC661") == Request(35, 18, 4, 1870644833)


def test_int_to_hex_string_valid_cases():
    # Test with a 4-byte representation
    assert int_to_hex_string(35, 4) == "00000023"

    # Test with a 2-byte representation
    assert int_to_hex_string(35, 2) == "0023"

    # Test with a maximum value for 2 bytes
    assert int_to_hex_string(65535, 2) == "FFFF"

    # Test with the maximum value for 4 bytes
    assert int_to_hex_string(65535, 4) == "0000FFFF"

    # Test zero value
    assert int_to_hex_string(0, 4) == "00000000"
    assert int_to_hex_string(0, 2) == "0000"


def test_int_to_hex_string_edge_cases():
    # Test with 1-byte representation of maximum value
    assert int_to_hex_string(255, 1) == "FF"

    # Test with 1-byte representation of zero
    assert int_to_hex_string(0, 1) == "00"
