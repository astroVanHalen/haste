class Behavior:
    """
    Base class for all transaction behavior plugins.
    Behaviors DO NOT create transactions.
    Behaviors MUTATE transactions based on context.
    """

    def __init__(self, constraints=None):
        self.constraints = constraints

    def applies(self, context) -> bool:
        return True

    def apply(self, txn: dict, context: dict) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} must implement apply()")
