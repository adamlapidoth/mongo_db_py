from pymongo import MongoClient
from pymongo.database import Database

from video_game_character import Player, Item

my_client = MongoClient(host="localhost", port=27017)

potion = Item(name="potion", quantity=1, effects=[{"heal": 100}])
player1 = Player(name="player1", max_health=50, max_energy=25)
player2 = Player(name="player2", max_health=200, max_energy=300, items=[potion])


def insert_to_mongodb(client: MongoClient, player: Player):
    game_db = client["game"]
    game_collections = game_db.list_collection_names()
    if "players" not in game_collections:
        game_db.create_collection(name="players")
    players_col = game_db["players"]
    if not find_player_by_name(game_db, player.name):
        players_col.insert_one(player.stat())


def find_player_by_name(
    db: Database,
    player_name: str,
):
    return db.players.find_one({"name": player_name})


def load_player(db: Database, player_name: str) -> Player:
    player_dict = find_player_by_name(db, player_name)
    item_list = [Item(**it) for it in player_dict["items"]]
    player_obj = Player(
        name=player_dict["name"],
        max_health=player_dict["max_health"],
        max_energy=player_dict["max_energy"],
    )
    player_obj.items = item_list
    player_obj.health = player_dict["health"]
    player_obj.energy = player_dict["energy"]

    return player_obj


if __name__ == "__main__":
    insert_to_mongodb(client=my_client, player=player1)
    player1_loaded = load_player(my_client.game, player_name="player1")
    assert player1_loaded == player1
    insert_to_mongodb(client=my_client, player=player2)
    player2_loaded = load_player(my_client.game, player_name="player2")
    assert player2_loaded == player2
