import asyncio
import websockets
import pyroboy
import redis
import struct
from pyroboy.face_recognition import FaceRec

ENCONDING_LENGTH = 128

class FaceOracle:
    def __init__(self):
        self.r = redis.Redis(host='172.17.0.1', port=6379, db=0)
        self.start_server = websockets.serve(self.recognize, 'localhost', 8765)

    def start(self):
        asyncio.get_event_loop().run_until_complete(self.start_server)
        asyncio.get_event_loop().run_forever()

    def get_known_faces(self):
        # key = neo4j node id
        # value = binary face encoding

        keys = self.r.keys()
        values = []
        for k in keys:
            value = self.r.get(key)
            values.append(struct.unpack('%sd' % ENCONDING_LENGTH, value))
        return keys,values

    async def recognize(self, websocket, path):
        face_encoding = await websocket.recv()
        ids, known_faces = self.get_known_faces()
        idx = FaceRec.match_face(face_encoding, ids)
        if idx:
            await websocket.send(int(keys[idx].decode('utf-8')))
        await websocket.send(-1)

if __name__ == '__main__':
    oracle = FaceOracle()
    oracle.start()
