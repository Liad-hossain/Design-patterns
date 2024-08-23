from Design_patterns.structural_design_patterns.adapter_design_pattern.example_1.PaymentGateway import PaymentGateway


class Stripe:
    def charge(self, amount: float) -> str:
        return f"Processed payment of ${amount} using Stripe."


class StripeAdapter(PaymentGateway):
    def __init__(self, stripe: Stripe) -> None:
        self.stripe = stripe

    def process_payment(self, amount: float) -> str:
        return self.stripe.charge(amount)
