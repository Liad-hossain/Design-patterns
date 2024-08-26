from Design_patterns.behavioral_design_patterns.chain_of_responsibility_design_pattern.example_1.BaseHandler import (
    SupportHandler,
)


class ManagerSupportHandler(SupportHandler):
    def handle(self, request) -> str:
        if request == "billing_dispute":
            return "ManagerSupportHandler: Resolved billing dispute."
        elif self.next_handler:
            return self.next_handler.handle(request)
        else:
            return "ManagerSupportHandler: Unable to handle the request."
