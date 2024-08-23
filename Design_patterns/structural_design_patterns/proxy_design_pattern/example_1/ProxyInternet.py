from Design_patterns.structural_design_patterns.proxy_design_pattern.example_1.InternetInterface import Internet
from Design_patterns.structural_design_patterns.proxy_design_pattern.example_1.RealInternet import RealInternet


class ProxyInternet(Internet):
    def __init__(self):
        self.real_internet = RealInternet()
        self.banned_sites = ["socialmedia.com", "streamingservice.com", "gamingplatform.com"]

    def connect_to(self, server_host: str) -> None:
        if server_host in self.banned_sites:
            print(f"Access Denied: {server_host} is restricted!")
        else:
            self.real_internet.connect_to(server_host)
