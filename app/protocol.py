from dataclasses import dataclass


def int_to_hex_string(num, bytes):
    """Converts an integer to a hexadecimal string of n bytes."""
    return num.to_bytes(bytes, byteorder="big").hex().upper()


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
        int(hex[:8], 16),
        int(hex[8:12], 16),
        int(hex[12:16], 16),
        int(hex[16:24], 16),
    )


@dataclass
class Response:
    message_size: int
    correlation_id: int


def encode_response(r: Response) -> bytes:
    message_size = int_to_hex_string(r.message_size, 4)
    correlation_id = int_to_hex_string(r.correlation_id, 4)
    return message_size + correlation_id
