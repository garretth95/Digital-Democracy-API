

# request object to be passed to queryDB after filled in from GET request

class RequestModule:

    # list ot object fields

    bid = None

    def __init__(self, bid):
        self.bid = bid


# here is where we will write the front-end parsing function
