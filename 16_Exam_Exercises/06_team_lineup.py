def team_lineup(*args):
    players = {}
    for player_name, country_name in args:
        if country_name not in players:
            players[country_name] = []
        players[country_name].append(player_name)
    result = ""
    sorted_players = sorted(players.items(), key=lambda x: (-len(x[1]), x[0]))

    for country, players in sorted_players:
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"
    return result[:-1]


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))
