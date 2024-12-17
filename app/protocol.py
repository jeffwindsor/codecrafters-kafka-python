from dataclasses import dataclass


def int_to_output(num, bytes):
    return num.to_bytes(bytes, byteorder="big")


def input_to_int(input) -> int:
    return int.from_bytes(input, byteorder="big")


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
        input_to_int(hex[:4]),
        input_to_int(hex[4:6]),
        input_to_int(hex[6:8]),
        input_to_int(hex[8:12]),
    )


@dataclass
class Response:
    message_size: int
    correlation_id: int


def encode_response(r: Response) -> bytes:
    error_code = 35
    return (
        int_to_output(r.message_size, 4)
        + int_to_output(r.correlation_id, 4)
        + int_to_output(error_code, 2)
    )
