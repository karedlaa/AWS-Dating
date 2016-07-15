from pubnub import Pubnub

PUBNUB_PUBLISH_KEY = "pub-c-487cbe24-d413-4eba-b857-765d0eb5164f"
PUBNUB_SUBSCRIBE_KEY = "sub-c-4b9d290c-ece0-11e5-8346-0619f8945a4f"
PUBNUB_SECRET_KEY = "sec-c-ZmIxZGFjY2QtYWRjYS00NTJkLWJjYzQtOWZhMzJhYTNjNDUy"

CHANNEL = "channel2"

if __name__ == "__main__":
    pubnub = Pubnub(publish_key=PUBNUB_PUBLISH_KEY,
                    subscribe_key=PUBNUB_SUBSCRIBE_KEY,
                    secret_key=PUBNUB_SECRET_KEY,
                    cipher_key='',
                    ssl_on=False
                    )

    pubnub.publish(CHANNEL, "My first message")
