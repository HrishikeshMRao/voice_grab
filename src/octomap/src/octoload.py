#!/usr/bin/env python3
import rclpy
from moveit_msgs.msg import PlanningScene, PlanningSceneWorld
from octomap_msgs.msg import Octomap
from rclpy.node import Node


class OctoHandler(Node):
    def __init__(self):
        super().__init__('moveit_octomap_handler')
        self.mapMsg = None

        self.subscription = self.create_subscription(
            Octomap,
            'octomap_full',
            self.octomap_callback,
            1)
        
        self.publisher1 = self.create_publisher(
            PlanningScene,
            'move_group/monitored_planning_scene',
            1)
        
        self.publisher2 = self.create_publisher(
            PlanningScene,
            '/planning_scene',
            1)
        
        self.timer = self.create_timer(4.0, self.publish_scene)

    def octomap_callback(self, msg):
        psw = PlanningSceneWorld()
        psw.octomap.header.stamp = self.get_clock().now().to_msg()
        psw.octomap.header.frame_id = 'world'
        psw.octomap.octomap = msg
        psw.octomap.origin.position.x = 0.0
        psw.octomap.origin.position.y = 0.0
        psw.octomap.origin.position.z = 0.0
        psw.octomap.origin.orientation.w = 1.0
        
        ps = PlanningScene()
        ps.world = psw
        ps.is_diff = True
        self.mapMsg = ps
    
    def publish_scene(self):
        if self.mapMsg is not None:
            self.publisher1.publish(self.mapMsg)
            self.publisher2.publish(self.mapMsg)


def main(args=None):
    rclpy.init(args=args)
    octo_handler = OctoHandler()
    rclpy.spin(octo_handler)
    octo_handler.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
        