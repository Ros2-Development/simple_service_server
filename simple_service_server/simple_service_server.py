import rclpy
from rclpy.node import Node
from simple_msgs.srv import AddTwoInt


class SimpleServiceServer(Node):
    def __init__(self):
        super().__init__("simple_service_server")

        self.get_logger().info("Service Server Running !!!")

        self.service_ = self.create_service(AddTwoInt,"add_two_int", self.serviceCallBack)

    def serviceCallBack(self, request, response):
        self.get_logger().info(f"new request received a:{request.a} , b: {request.b}")
        response.sum = request.a + request.b

        self.get_logger().info("Returning sum %d"%response.sum)
        return response
    

def main():
    rclpy.init()
    simple_service_server = SimpleServiceServer()
    rclpy.spin(simple_service_server)
    simple_service_server.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()



