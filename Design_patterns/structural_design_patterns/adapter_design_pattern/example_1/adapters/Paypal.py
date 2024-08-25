from Design_patterns.structural_design_patterns.adapter_design_pattern.example_1.PaymentGateway import (
    PaymentGateway,
)


class Paypal:
    def pay(self, amount: float) -> str:
        return f"Processed payment of ${amount} using Paypal."


class PaypalAdapter(PaymentGateway):
    def __init__(self, paypal: Paypal) -> None:
        self.paypal = paypal

    def process_payment(self, amount: float) -> str:
        return self.paypal.pay(amount)
