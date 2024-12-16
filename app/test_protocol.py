import pytest
from protocol import (
    Response,
    Request,
    int_to_string_big_endian,
    decode_request,
    encode_response,
)


def test_parse_correlation_id():
    given = (
        "00000023001200046f7fc66100096b61666b612d636c69000a6b61666b612d636c6904302e3100"
    )
    request = decode_request(given)
    response = Response(0, request.correlation_id)
    actual = encode_response(response)
    expected = "000000006f7fc661"

    assert actual == expected


def test_int_to_string_big_endian_valid_cases():
    # Test with a 4-byte representation
    assert int_to_string_big_endian(35, 4) == "00000023"

    # Test with a 2-byte representation
    assert int_to_string_big_endian(35, 2) == "0023"

    # Test with a maximum value for 2 bytes
    assert int_to_string_big_endian(65535, 2) == "ffff"

    # Test with the maximum value for 4 bytes
    assert int_to_string_big_endian(65535, 4) == "0000ffff"

    # Test zero value
    assert int_to_string_big_endian(0, 4) == "00000000"
    assert int_to_string_big_endian(0, 2) == "0000"


def test_int_to_string_big_endian_invalid_cases():
    # Test with a negative value
    with pytest.raises(ValueError, match="The value must be non-negative."):
        int_to_string_big_endian(-1, 4)

    # Test with a value that exceeds the byte size
    with pytest.raises(ValueError, match="cannot be represented in 2 bytes."):
        int_to_string_big_endian(65536, 2)  # 65536 exceeds 2 bytes


def test_int_to_string_big_endian_edge_cases():
    # Test with 1-byte representation of maximum value
    assert int_to_string_big_endian(255, 1) == "ff"

    # Test with 1-byte representation of zero
    assert int_to_string_big_endian(0, 1) == "00"
