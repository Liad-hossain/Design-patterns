from Design_patterns.behavioral_design_patterns.chain_of_responsibility_design_pattern.example_1.BaseHandler import (
    SupportHandler,
)


class TechnicalSupportHandler(SupportHandler):
    def handle(self, request) -> str:
        if request == "technical_issue":
            return "TechnicalSupportHandler: Resolved technical issue."
        elif self.next_handler:
            return self.next_handler.handle(request)
        else:
            return "TechnicalSupportHandler: Unable to handle the request."
