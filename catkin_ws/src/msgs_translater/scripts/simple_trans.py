import rospy
from std_msgs.msg import String
import json
import websocket

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    msg = json.dumps(data.data)
    try:
        ws.send(msg)
    except Exception as e:
        rospy.logerr("Failed to send message via websocket: %s", str(e))
    finally:
        ws.close()


def listener():
    rospy.init_node('listener', anonymous=True)
    topic_name = "/visualization_marker"
    sub = rospy.Subscriber(topic_name, String. callback)

    global ws
    try:
        ws = websocket.create_connection("ws://localhost:9090")
        rospy.loginfo("Connected to websocket server")
    except Exception as e:
        rospy.logerr("Failed to connect to websocket server: %s", str(e))
        return
    
    rospy.spin()
    ws.close()


if __name__ == '__main__':
    listener()