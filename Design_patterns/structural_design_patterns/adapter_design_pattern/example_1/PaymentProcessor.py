from Design_patterns.structural_design_patterns.adapter_design_pattern.example_1.adapters.LegacyBank import (
    LegacyBank,
    LegacyBankAdapter,
)
from Design_patterns.structural_design_patterns.adapter_design_pattern.example_1.adapters.Paypal import (
    Paypal,
    PaypalAdapter,
)
from Design_patterns.structural_design_patterns.adapter_design_pattern.example_1.adapters.Stripe import (
    Stripe,
    StripeAdapter,
)
from Design_patterns.structural_design_patterns.adapter_design_pattern.example_1.PaymentGateway import (
    PaymentGateway,
)


class PaymentProcessor:
    def __init__(self, payment_gateway: PaymentGateway) -> None:
        self.payment_gateway = payment_gateway

    def make_payment(self, amount: float) -> str:
        return self.payment_gateway.process_payment(amount)


if __name__ == "__main__":

    print(PaymentProcessor(PaypalAdapter(Paypal())).make_payment(100))

    print("")

    print(PaymentProcessor(StripeAdapter(Stripe())).make_payment(200))

    print("")

    print(PaymentProcessor(LegacyBankAdapter(LegacyBank())).make_payment(300))
