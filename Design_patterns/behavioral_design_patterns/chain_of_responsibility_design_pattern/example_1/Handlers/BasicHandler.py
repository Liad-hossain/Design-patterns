from Design_patterns.behavioral_design_patterns.chain_of_responsibility_design_pattern.example_1.BaseHandler import (
    SupportHandler,
)


class BasicSupportHandler(SupportHandler):
    def handle(self, request) -> str:
        if request == "password_reset":
            return "BasicSupportHandler: Resolved password reset issue."
        elif self.next_handler:
            return self.next_handler.handle(request)
        else:
            return "BasicSupportHandler: Unable to handle the request."
