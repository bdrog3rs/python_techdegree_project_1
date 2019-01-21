import csv

Sharks = [0,0, 'Sharks']
Dragons = [0,0, 'Dragons']
Raptors = [0,0, 'Raptors']
league = [Sharks, Dragons, Raptors]

def assign_player(player):
  for team in league:
    if player['Soccer Experience'] == 'YES':
      if team[0] < 3:
        team.append(player)
        team[0]+=1
        return
    else:
      if team[1] < 3:
        team.append(player)
        team[1]+=1
        return

if __name__ == "__main__": 
  with open('soccer_players.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:    
      assign_player(row)
  for team in league:
    team_name = team[2]
    team = team[3:]
    for player in team:
      file_name = player['Name'].split(" ")[0].lower() + "_" + player['Name'].split(" ")[1].lower() + ".txt"
      with open(file_name, "a") as file:
        file.write(
          "Dear " + player['Guardian Name(s)'] + ":" + '\n' +'\n' +
          "Welcome to the youth soccer league! " + player['Name'] + " has been assigned to the " + team_name + " team. The first practice is January 24th at 5:00pm.  We're excited to have you in the league!"  
        )
    with open("teams.txt", "a") as file:
      file.write(team_name + "\n")       
      for player in team:
        file.write(player['Name'] + ", " + player['Soccer Experience'] + ", " + player['Guardian Name(s)'] + '\n')
      file.write("\n")
