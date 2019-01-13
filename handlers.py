from databases import redis_client

class PostedComment:
    def __init__(self, msg):
        self.msg = msg

    def run(self):
        print("Handled by PostedComment")
        print(self.msg)
        redis_client().set(self.msg.key, self.msg.value['type'])
        return 'OK'
