import os
import tempfile

import pytest

def test_empty_db(client):
    """Start with a blank database."""

    # rv = client.get('/')
    assert 1 == 1
