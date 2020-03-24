import redis

zmienna = "działa"
print(zmienna)

red = redis.Redis(host="172.17.0.1", port=6381, db=1)


def redis_push(message, author):
    red.rpush(author, message)
    print("Pushed " + message + " as " + author)
    return


def redis_get(author):
    try:
        got_msg = red.lrange(author, 0, 1)[0].decode("utf-8")
        red.lrem(author, 1, got_msg)
        print("Got " + got_msg + " from " + author)
    except:
        print("Error occurred, try again")
    return


def redis_empty(author):
    try:
        red.ltrim(author, -1, 0)
        print("Emptied messages from " + author)
    except:
        print("Error occurred, try again")
    return


def redis_show_queue(author):
    try:
        que = red.lrange(author, 0, -1)
        print("Messages from " + author)
        for string in que:
            print(string.decode("utf-8"))
    except:
        print("Error occurred, try again")
    return


def redis_create(author):
    try:
        red.rpush(author, "")
        print("Created queue " + author)
    except:
        print("Error occurred, try again")
    return


controller = ""

me = "client"
print("Things you may want to do:")
print("Send message? (send X)")
print("Receive message? (receive from X)")
print("Delete messages? (delete from X) {deletes all, without showing}")
print("Create new conversation? (create new)")
print("Show all messages? (show from X) {no deleting}")
print("Quit (quit)")

while "quit" not in controller:

    controller = input("Tell me what do you want to do:")

    if controller.startswith("send"):
        redis_push(author=me, message=controller[4:])
    elif controller.startswith("receive"):
        redis_get(controller[13:])
    elif controller.startswith("delete"):
        redis_empty(controller[12:])
    elif controller.startswith("create"):
        redis_create(me)
    elif controller.startswith("show"):
        redis_show_queue(controller[10:])
    elif "quit" not in controller:
        print("Wrong command")

    if controller == "quit":
        controller = "quit"
    else:
        controller = ""
