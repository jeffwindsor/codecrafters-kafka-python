from dataclasses import dataclass
from enum import Enum, unique


def int_to_output(num, bytes):
    return num.to_bytes(bytes, byteorder="big")


def input_to_int(input) -> int:
    return int.from_bytes(input, byteorder="big")


# == Communication Protocol ==
@unique
class ErrorCode(Enum):
    NONE = 0
    UNSUPPORTED = 35


valid_api_versions = [0, 1, 2, 3, 4]


def is_valid_api_version(api_version: int) -> ErrorCode:
    return (
        ErrorCode.NONE if api_version in valid_api_versions else ErrorCode.UNSUPPORTED
    )


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


def encode_response(r: Request) -> bytes:
    error_code = is_valid_api_version(r.request_api_version)
    tag_buffer = 0
    throttle_time_ms = 0
    message = (
        # Header
        int_to_output(r.correlation_id, 4)
        # Body
        + int_to_output(error_code.value, 2)
        + int_to_output(2, 1)
        + int_to_output(r.request_api_key, 2)
        + int_to_output(min(valid_api_versions), 2)
        + int_to_output(max(valid_api_versions), 2)
        + int_to_output(tag_buffer, 2)
        + int_to_output(throttle_time_ms, 2)
        + int_to_output(tag_buffer, 2)
    )
    message_size = int_to_output(len(message), 4)

    return message_size + message
