from typing import overload

def init() -> None:
    ...

def get_network_data() -> tuple[bytes, bytes, bytes]:
    ...

def get_remote_data(sock: int) -> tuple[bytes, int]:
    ...

def wifi_set_network(ssid: str) -> int:
    ...

def wifi_set_passphrase(ssid: str, passphrase: str) -> int:
    ...

def wifi_set_key(ssid: str, key_idx: int, passphrase: str) -> int:
    ...

def config(valid_params: int, local_ip: tuple[int, int, int, int], gateway: tuple[int, int, int, int], subnet: tuple[int, int, int, int]) -> None:
    ...

def set_dns(dns_server1: tuple[int, int, int, int], dns_server2: tuple[int, int, int, int]) -> None:
    ...

def set_hostname(hostname: str) -> None:
    ...

def disconnect() -> None:
    ...

def get_connection_status() -> int:
    ...

def get_mac_address() -> bytes:
    ...

def get_ip_address() -> tuple[int, int, int, int]:
    ...

def get_subnet_mask() -> tuple[int, int, int, int]:
    ...

def get_gateway_ip() -> tuple[int, int, int, int]:
    ...

def get_current_ssid() -> str:
    ...

def get_current_bssid() -> bytes:
    ...

def get_current_rssi() -> int:
    ...

def get_current_encryption_type() -> int:
    ...

def start_scan_networks() -> bool:
    ...

def get_scan_networks() -> int:
    ...

def get_ssid_networks(network_item: int) -> str:
    ...

def get_enc_type_networks(network_item: int) -> int:
    ...

def get_bssid_networks(network_item: int) -> int:
    ...

def get_channel_networks(network_item: int) -> int:
    ...

def get_rssi_networks(network_item: int) -> int:
    ...

def req_host_by_name(hostname: str) -> bool:
    ...

@overload
def get_host_by_name() -> tuple[int, int, int, int]|None:
    ...

@overload
def get_host_by_name(hostname: str) -> tuple[int, int, int, int]|None:
    ...

def get_fw_version() -> str:
    ...

def get_time() -> int:
    ...

def set_power_mode(mode: int) -> None:
    ...

def wifi_set_ap_network(ssid: str, channel: int) -> int:
    ...

def wifi_set_ap_passphrase(ssid: str, passphrase: str, channel: int) -> int:
    ...

def ping(ip_address: tuple[int, int, int, int], ttl: int) -> int:
    ...

def debug(on: int) -> None:
    ...

def get_temperature() -> float:
    ...

def pin_mode(esp_pin: int, mode: int) -> None:
    ...

def digital_write(esp_pin: int, value: int) -> None:
    ...

def analog_write(esp_pin: int, value: int) -> None:
    ...

def digital_read(esp_pin: int) -> bool:
    ...

@overload
def analog_read(esp_pin: int) -> int:
    ...

@overload
def analog_read(esp_pin: int, atten: int) -> int:
    ...

@overload
def server_start(ip_address: tuple[int, int, int, int], port: int, sock: int, protocol_mode: int) -> None:
    ...

@overload
def server_start(port: int, sock: int, protocol_mode: int) -> None:
    ...

@overload
def client_start(ip_address: tuple[int, int, int, int], port: int, sock: int, protocol_mode: int) -> None:
    ...

@overload
def client_start(hostname: str, ip_address: tuple[int, int, int, int], port: int, sock: int, protocol_mode: int) -> None:
    ...

def client_stop(sock: int) -> None:
    ...

def get_server_state(sock: int) -> int:
    ...

def get_client_state(sock: int) -> int:
    ...

def avail_data(sock: int) -> int:
    ...

def avail_server(sock: int) -> int:
    ...

def get_data(sock: int, peek: int) -> int|None:
    ...

def get_data_buf(sock: int) -> bytes|None:
    ...

def insert_data_buf(sock: int, data: bytes) -> bool:
    ...

def send_udp_data(sock: int) -> bool:
    ...

def send_data(sock: int, data: bytes) -> int:
    ...

def check_data_sent(sock: int) -> int:
    ...

def get_socket() -> int:
    ...

def wifi_set_ent_identity(identity: str) -> None:
    ...

def wifi_set_ent_username(username: str) -> None:
    ...

def wifi_set_ent_password(password: str) -> None:
    ...

def wifi_set_ent_enable() -> None:
    ...

def set_led(r: int, g: int, b: int) -> None:
    ...

def is_pressed() -> bool:
    ...

def is_sdcard_detected() -> bool:
    ...
