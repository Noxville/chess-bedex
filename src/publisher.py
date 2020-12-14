import json
import time


class RMQPublisher:
    def __init__(self, game_id):
        self.game_id = game_id
        self.seq_idx = 1

    def send(self, payload):
        msg = {
            'version': '1.00',
            'path': "esports/chess/{}".format(self.game_id),
            'seqIdx': self.seq_idx,
            'timesent': int(round(time.time() * 1000)),
            'payload': payload.to_dict()
        }

        self.seq_idx += 1
        print(json.dumps(msg))
