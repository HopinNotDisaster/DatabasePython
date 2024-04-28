import redis
import threading


def subscribe(*args):
    client = redis.StrictRedis(password="123456")

    # 获取  订阅实例
    ps = client.pubsub()
    # 监听指定频道
    ps.subscribe(args)
    # 开始监听频道
    for message in ps.listen():
        print(f"消息", message)
    client.close()


def publish():
    while 1:
        # 发布消息的线程
        info = input("输入频道与消息， 使用:分割\n")
        change, message = info.split(":")
        if change and message:
            client = redis.StrictRedis(password="123456")
            client.publish(change, message)
        else:
            print(f"输入格式错误请从新输入")


def main():
    t_publish = threading.Thread(target=publish)
    t_publish.start()

    t_sub01 = threading.Thread(target=subscribe, args=('c1', 'c2', 'c3'))
    t_sub01.start()

    t_sub02 = threading.Thread(target=subscribe, args=('c4', 'c3'))
    t_sub02.start()

    t_publish.join()
    t_sub01.join()
    t_sub02.join()


if __name__ == '__main__':
    # 主线程
    main()
