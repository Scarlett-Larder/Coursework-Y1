
class StreamingAccount:

    def __init__(self):
        self._account_name = "Guest"
        self._membership_type = "Basic"
        self._stream_limit = 2

    @property
    def account_name(self):
        return self._account_name

def test_streaming_account():
    my_account = StreamingAccount()
    print(my_account.account_name)

test_streaming_account()