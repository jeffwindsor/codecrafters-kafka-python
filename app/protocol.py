from dataclasses import dataclass


def bytes_big_endian_to_int(value: bytes) -> int:
    return int.from_bytes(value, byteorder="big", signed=True)


def int_to_string_big_endian(value: int, number_of_bytes: int) -> str:
    if value < 0:
        raise ValueError("The value must be non-negative.")

    try:
        bytes = value.to_bytes(number_of_bytes, byteorder="big")
    except OverflowError:
        raise ValueError(
            f"The value {value} cannot be represented in {number_of_bytes} bytes."
        )

    return bytes.hex()


# == Communication Protocol ==
@dataclass
class Request:
    message_size: int
    request_api_key: int
    request_api_version: int
    correlation_id: int
    # client_id 	NULLABLE_STRING 	The client ID for the request
    # tag_buffer 	COMPACT_ARRAY 	Optional tagged fields


def decode_request(hex) -> Request:
    return Request(
        bytes_big_endian_to_int(hex[:4]),
        bytes_big_endian_to_int(hex[4:6]),
        bytes_big_endian_to_int(hex[6:8]),
        bytes_big_endian_to_int(hex[8:12]),
    )


@dataclass
class Response:
    message_size: int
    correlation_id: int


def encode_response(r: Response) -> str:
    message_size = int_to_string_big_endian(r.message_size, 4)
    correlation_id = int_to_string_big_endian(r.correlation_id, 4)
    return message_size + correlation_id
