import redis

red = redis.Redis(host="172.17.0.1", port=6381, db=1)


def push(data, queue_name):
    red.rpush(queue_name, data)
    return

def flush():
    red.flushdb(asynchronous=false)
    return


def get(queue_name):
    got_msg = ""
    try:
        got_msg = red.lrange(queue_name, 0, 1)[0].decode("utf-8")
        red.lrem(queue_name, 1, got_msg)
    except IndexError:
        raise IndexError("No data")
    except:
       print("Error occurred, try again")
    return got_msg


def empty(queue_name):
    try:
        red.ltrim(queue_name, 0, 0)
    except:
        print("Error occurred, try again")
    return


def show_queue(queue_name):
    result = []
    try:
        que = red.lrange(queue_name, 0, -1)
        for string in que:
            result.append(string.decode("utf-8"))
    except:
        print("Error occurred, try again")
    return result


def show_delete_queue(queue_name):
    result = []
    try:
        que = red.lrange(queue_name, 0, -1)
        for string in que:
            result.append(string.decode("utf-8"))
    except:
        print("Error occurred, try again")
    return result


def create(queue_name):
    try:
        red.rpush(queue_name, "")
    except:
        print("Error occurred, try again")
    return