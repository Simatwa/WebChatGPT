class WebSocketError(Exception):
    pass


class CookieExpiredError(Exception):
    pass


class VerificationError(Exception):
    pass


class MaximumRetrialError(Exception):
    pass
