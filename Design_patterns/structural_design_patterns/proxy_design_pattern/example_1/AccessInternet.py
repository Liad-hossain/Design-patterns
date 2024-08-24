from Design_patterns.structural_design_patterns.proxy_design_pattern.example_1.ProxyInternet import ProxyInternet
from Design_patterns.structural_design_patterns.proxy_design_pattern.example_1.RealInternet import RealInternet

# Client code
employee_internet = ProxyInternet()

# Regular employee trying to access a restricted site
employee_internet.connect_to("socialmedia.com")
# Output: Access Denied: socialmedia.com is restricted!

# Regular employee trying to access an allowed site
employee_internet.connect_to("workrelatedsite.com")
# Output: Connecting to workrelatedsite.com...

# Manager with full access (this example assumes the manager bypasses the proxy, but you could enhance the proxy to check roles)
manager_internet = RealInternet()
manager_internet.connect_to("socialmedia.com")
# Output: Connecting to socialmedia.com...
