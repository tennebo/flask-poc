"""JSON encoding functions.
"""

import datetime

from flask.json import JSONEncoder


class IsoJSONEncoder(JSONEncoder):
    """Custom encoder to serialize dates into ISO-8601 format."""

    def default(self, obj):
        """If the argument is a date, return its ISO representation."""
        if isinstance(obj, datetime.date):
            return obj.isoformat()

        return super().default(obj)
