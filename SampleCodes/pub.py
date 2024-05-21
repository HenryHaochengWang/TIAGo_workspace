from websocket import create_connection

ws = create_connection("ws://localhost:9090")

msg = '{"op": "publish", "topic": "/visualization_marker", "type": "visualization_msgs/Marker"'

msg += ', "msg": \'{"header": {"frame_id": "base_link"}, "id": 1, "type": 1, "action": 0, "pose": {"position": {"x": 0., "y": 0.2, "z": 0.}, "orientation": {"x": 0.3, "y": 0.2, "z": 0.52, "w": 0.85}}, "scale": {"x": 0.2, "y": 0.3, "z": 0.1}, "color": {"r": 1., "g": 0., "b": 1., "a": 0.3}, "lifetime": 50000000000}\'}'

try:
    ws.send(msg)
    result = ws.recv()
    print("Received '%s'" % result)
finally:
    ws.close()