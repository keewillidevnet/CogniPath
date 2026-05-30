"""
test_tokenlib.py - Public-safe unit test for TokenValidator stub.

The public TokenValidator is intentionally a stub. This test asserts that
calling validate() raises NotImplementedError, which is the open-core contract:
integrators must subclass and provide their own implementation, or use the
enterprise edition from CogniPath-core.
"""

import pytest
from core.tokenlib import TokenValidator


def test_validate_raises_not_implemented():
    """The public stub must clearly signal that it is not a working validator."""
    validator = TokenValidator()
    with pytest.raises(NotImplementedError) as exc_info:
        validator.validate({"raw": "anything", "uuid": "anything"})
    # Confirm the error message points integrators to the right place
    assert "enterprise edition" in str(exc_info.value).lower() or \
           "cognipath-core" in str(exc_info.value).lower()
