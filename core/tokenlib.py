"""
tokenlib.py - Public-safe token validation stubs
Note: Full cryptographic validation, clearance enforcement, and replay protection are protected in CogniPath-core.
"""


class TokenValidator:
    """
    Public-safe abstract interface for CogniPath token validation.

    The reference implementation lives in the private CogniPath-core repository
    and performs HMAC verification, replay protection, rate limiting, and
    clearance enforcement. This public class intentionally does not implement
    any of those mechanisms.

    Integrators should subclass TokenValidator and provide their own validate()
    implementation, or use the enterprise edition.
    """

    def validate(self, token):
        raise NotImplementedError(
            "TokenValidator.validate is a public-safe stub. "
            "Token validation is implemented in CogniPath-core (enterprise edition). "
            "Subclass TokenValidator and override validate() to provide your own implementation."
        )