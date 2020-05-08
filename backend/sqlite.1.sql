SELECT 
title.title,title.state,tournament.tournament_name,
team.Team , scores.winner,scores.Score FROM matches 
	inner join team on matches.team1 = team.id OR matches.team2=team.id
    inner join scores on (matches.team1=scores.team_id or matches.team2=scores.team_id)
    inner join tournament on tournament.id = matches.tournament_id
    inner join title on title.id=tournament.id
    