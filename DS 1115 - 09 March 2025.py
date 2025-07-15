# Sample Question Solve 
# 1
class Player:
      def __init__(self,name:str,run:int,out:bool):
            self.name=name
            self.run=run
            self.out=out

      def update_run(self,runs):
            self.run=self.run+runs

class Team:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def add_players(self, player):
        self.players.append(player)

    def remove_players(self, player):
        self.players.remove(player)

    def get_total_runs(self):
        total_runs = sum(player.run for player in self.players)
        return total_runs

    def get_highest_scorer(self):
        if len(self.players) == 0:
            print("No Player Added Yet")
            return None
        else:
            max_run = self.players[0].run
            max_index = 0
            for i in range(1, len(self.players)):
                if self.players[i].run > max_run:
                    max_run = self.players[i].run
                    max_index = i
            return self.players[max_index]

def get_result(team1, team2):
    run_team1 = team1.get_total_runs()
    run_team2 = team2.get_total_runs()
        
    if run_team1 > run_team2:
        team_name = team1.name
        player = team1.get_highest_scorer()
    elif run_team2 > run_team1:
        team_name = team2.name
        player = team2.get_highest_scorer()
    else:
        print("The match is DRAW")
        return

    if player:
        player_name = player.name
        print(f"The winner of this match is {team_name} and the highest scorer of the game is {player_name}")

player1 = Player("Player A", 50, False)
player2 = Player("Player B", 70, True)
player3 = Player("Player C", 30, False)
player4 = Player("Player D", 40, True)

player5 = Player("Player E", 60, False)
player6 = Player("Player F", 90, True)
player7 = Player("Player G", 91, False)
player8 = Player("Player H", 35, True)

team1 = Team("Team Warriors")
team2 = Team("Team Titans")

team1.add_players(player1)
team1.add_players(player2)
team1.add_players(player3)
team1.add_players(player4)

team2.add_players(player5)
team2.add_players(player6)
team2.add_players(player7)
team2.add_players(player8)

get_result(team1,team2)

# 2
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    def days_in_month(self, month, year):
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        return days_in_months[month - 1]

    def __add__(self, days):
        day = self.day + days
        month = self.month
        year = self.year
        if day > self.days_in_month(month, year):
            day -= self.days_in_month(month, year)
            month += 1
            if month > 12:
                month = 1
                year += 1
        return Date(day, month, year)

    def __sub__(self, other):
        if self.year != other.year:
            return ValueError("This implementation only supports dates within the same year.")
        days1 = sum(self.days_in_month(m, self.year) for m in range(1, self.month)) + self.day
        days2 = sum(self.days_in_month(m, other.year) for m in range(1, other.month)) + other.day
        return abs(days1 - days2)

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

d1 = Date(9, 11, 2024)
d2 = Date(5, 11, 2024)

print(d1 + 25)
print(d1 - d2)
print(d1 == d2)