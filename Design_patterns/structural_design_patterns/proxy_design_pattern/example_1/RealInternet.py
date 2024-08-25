from Design_patterns.structural_design_patterns.proxy_design_pattern.example_1.InternetInterface import (
    Internet,
)


class RealInternet(Internet):
    def connect_to(self, server_host: str) -> None:
        print(f"Connecting to {server_host}...")
