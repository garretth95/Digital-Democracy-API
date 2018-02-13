
# request object to be passed to queryDB after filled in from GET request

class RequestModule:

    # list ot object fields
    date = None
    state = None
    committee = None
    callType = None
    billType = None
    billNumber = None

    def __init__(self, date, state, committee, billType, billNumber, callType):
        self.date = date
        self.state = state
        self.committee = committee
        self.billType = billType
        self.billNumber = billNumber
        self.callType = callType


    def __str__(self):
        return "Date: " + self.date + "<br>State: " + self.state + "<br>Committee: " + self.committee + "<br>Call Type: " \
               + self.callType + "<br>Bill Type: " + self.billType + "<br>Bill Number: " + self.billNumber
# here is where we will write the front-end parsing function
