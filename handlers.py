class PostedComment:
    def __init__(self, msg):
        self.msg = msg

    def run(self):
        print("Handled by PostedComment")
        print(self.msg)
