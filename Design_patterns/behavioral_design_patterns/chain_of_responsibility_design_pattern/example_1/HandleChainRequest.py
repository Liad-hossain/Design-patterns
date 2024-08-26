from Design_patterns.behavioral_design_patterns.chain_of_responsibility_design_pattern.example_1.Handlers.BasicHandler import (
    BasicSupportHandler,
)
from Design_patterns.behavioral_design_patterns.chain_of_responsibility_design_pattern.example_1.Handlers.ManagerHandler import (
    ManagerSupportHandler,
)
from Design_patterns.behavioral_design_patterns.chain_of_responsibility_design_pattern.example_1.Handlers.TechnicalHandler import (
    TechnicalSupportHandler,
)


def handle_support_request(request) -> str:
    handler_chain = BasicSupportHandler(
        TechnicalSupportHandler(ManagerSupportHandler()),
    )

    result = handler_chain.handle(request)

    return result


if __name__ == "__main__":
    requests = ["password_reset", "technical_issue", "billing_dispute", "unknown_issue"]

    for req in requests:
        print(f"Request: {req}")
        print(f"Response: {handle_support_request(req)}\n")
