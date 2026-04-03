class Behavior:
    """
    Base class for all transaction behavior plugins.

    Behaviors DO NOT create transactions.
    Behaviors MUTATE transactions based on context.
    """

    def applies(self, _context) -> bool:
        """
        Return True if this behavior should be applied
        for the given context.

        Base behavior always applies.
        Subclasses may override.
        """
        return True

    def apply(self, txn: dict, context: dict) -> None:
        """
        Mutate the transaction in-place based on context.

        This method MUST be implemented by subclasses.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement apply()"
        )
