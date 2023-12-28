from pymongo import MongoClient

from video_game_character import Player

my_client = MongoClient(host="localhost", port=27017)

player1 = Player(name="player1", max_health=50, max_energy=25)


def insert_to_mongodb(client: MongoClient, player: Player):
    game_db = client["game"]
    game_collections = game_db.list_collection_names()
    if "players" not in game_collections:
        game_db.create_collection(name="players")
    players_col = game_db["players"]
    players_col.insert_one(player.stat())


if __name__ == '__main__':
    insert_to_mongodb(client=my_client, player=player1)