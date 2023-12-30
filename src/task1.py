from pymongo import MongoClient
from pymongo.database import Database

from video_game_character import Player

my_client = MongoClient(host="localhost", port=27017)

player1 = Player(name="player1", max_health=50, max_energy=25)


def insert_to_mongodb(client: MongoClient, player: Player):
    game_db = client["game"]
    game_collections = game_db.list_collection_names()
    if "players" not in game_collections:
        game_db.create_collection(name="players")
    players_col = game_db["players"]
    if not find_player_by_name(game_db, player.stat()["name"]):
        players_col.insert_one(player.stat())


def find_player_by_name(
    db: Database,
    player_name: str,
):
    return db.players.find_one({"name": player_name})


def load_player(db: Database, player_name: str) -> Player:
    player_dict = find_player_by_name(db, player_name)
    player_dict.pop("_id", None)
    player_dict.pop("health", None)
    player_dict.pop("energy", None)
    item_list = [Item(**it) for it in player_dict["items"]]
    player = Player(**player_dict)
    player.items = item_list
    return player


if __name__ == "__main__":
    insert_to_mongodb(client=my_client, player=player1)
    player1_loaded = load_player(my_client.game, player_name="player1")
    assert player1_loaded == player1
