from Design_patterns.structural_design_patterns.adapter_design_pattern.example_1.PaymentGateway import (
    PaymentGateway,
)


class LegacyBank:
    def pay_amount(self, amount: float) -> str:
        return f"Processed payment of ${amount} using LegacyBank."


class LegacyBankAdapter(PaymentGateway):
    def __init__(self, legacy_bank: LegacyBank) -> None:
        self.legacy_bank = legacy_bank

    def process_payment(self, amount: float) -> str:
        return self.legacy_bank.pay_amount(amount)
