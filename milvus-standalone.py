from pymilvus import connections, utility, MilvusException

connections.connect(host = "localhost", port = "19530")

try:
    #List all conncetions
    collections = utility.list_collections()
    print(f"List all conncetions:\n", collections)
except MilvusException as e:
    print(e)