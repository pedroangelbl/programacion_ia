"""
Partiendo del código disponible en fichero adjunto añade la funcionalidad necesaria
para ofrecer la variante lagarto, Spock del juego piedra, papel o tijeras.

Usa las diferentes situaciones de juego, junto con su resultado,
del archivo victories.xml que se adjunta.

Sustituye el diccionario Victories por alguna referencia que permita acceder al
contenido de victories.xml.
"""

import random
from enum import IntEnum
from statistics import mode
import xml.etree.ElementTree as ET


class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


NUMBER_RECENT_ACTIONS = 5


def load_rules(xml_file):
    """
    Carga las reglas del juego desde un archivo XML, creando un diccionario que mapea
    cada acción con las que vence y el mensaje explicativo.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    rules = {}

    # Itera sobre todas las victories y las guarda en el diccionario rules
    for victory in root.findall("victory"):
        winner = GameAction[victory.get("choice")]
        loser = GameAction[victory.get("against")]
        message = victory.text.strip()

        if winner not in rules:
            rules[winner] = {}

        rules[winner][loser] = message

    return rules


def assess_game(user_action, computer_action, rules):
    """
    Determina el resultado comparando las acciones del usuario y 
    ordenador usando las reglas del XML.
    """
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        return GameResult.Tie

    if user_action in rules and computer_action in rules[user_action]:
        print(f"{rules[user_action][computer_action]}. You won!")
        return GameResult.Victory

    if computer_action in rules and user_action in rules[computer_action]:
        print(f"{rules[computer_action][user_action]}. You lost!")
        return GameResult.Defeat

    print("Unexpected result.")
    return GameResult.Tie


def get_computer_action(user_actions_history, game_history, rules):
    """
    - Si no hay historial, elige aleatoriamente.
    - Si hay historial, usa IA básica: analiza las últimas 5 jugadas del usuario 
    y elige la acción que le gane a su movimiento más frecuente.
    """
    # No previous user actions => random computer choice
    if not user_actions_history or not game_history:
        computer_action = get_random_computer_action()
    # Alternative AI functionality
    # Choice that would beat the user's most frequent recent choice
    else:
        most_frequent_recent_computer_action = GameAction(
            mode(user_actions_history[-NUMBER_RECENT_ACTIONS:])
        )
        computer_action = get_winner_action(most_frequent_recent_computer_action, rules)

    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    """
    Pide al usuario seleccionar una opción (0-4)
    """
    game_choices = [
        f"{game_action.name}[{game_action.value}]" for game_action in GameAction
    ]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def get_random_computer_action():
    """
    Devuelve una acción aleatoria
    """
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)

    return computer_action


def get_winner_action(game_action, rules):
    """
    Dada una acción, devuelve la que la vence
    """
    for winner, losers in rules.items():
        if game_action in losers:
            return winner
    return get_random_computer_action()


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == "y"


def main():
    rules = load_rules("victories.xml")
    game_history = []
    user_actions_history = []

    while True:
        try:
            user_action = get_user_action()
            user_actions_history.append(user_action)
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action(user_actions_history, game_history, rules)
        game_result = assess_game(user_action, computer_action, rules)
        game_history.append(game_result)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()
