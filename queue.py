class MyQueue(object):
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def __repr__(self):
        return "In {}, out {}".format(self.inbox, self.outbox)

    def peek(self):
        if len(self.outbox) > 0:
            return self.outbox[-1]
        elif len(self.inbox) > 0:
            return self.inbox[0]
        else:
            return None

    def pop(self):
        self.update_outbox()
        if len(self.outbox) > 0:
            return self.outbox.pop()

    def put(self, value):
        self.inbox.append(value)

    def update_outbox(self):
        if len(self.outbox) == 0:
            while len(self.inbox) > 0:
                self.outbox.append(self.inbox.pop())

