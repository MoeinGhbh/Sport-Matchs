from flask_sqlalchemy import SQLAlchemy
from config import app
import json


class titleError(Exception):
        """ exception of title class """


class turnamentError(Exception):
        """ exception of turnamnet class """

class teamError(Exception):
        """ exception of team class """

class matchesError(Exception):
        """ exception of matches class """

class scoresError(Exception):
        """ exception of scores class """

db = SQLAlchemy(app)


  # Title
  # Tournament
  # Team
  # Match
  # Scores of a Team in a Match

class Title(db.Model):
    __tableName__ = "title"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    state = db.Column(db.Integer,nullable=False)

    
    def Insert(self,_Title,_state):
        _Title = _Title.strip()
        _Title = _Title.lower()
        # print(_Title)
        # print(Title.query.filter_by(title=_Title).count())
        if Title.query.filter_by(title=_Title).count()==0:
            new_title = Title(title= _Title,state=_state)
            try:
                db.session.add(new_title)
                db.session.commit()
                return 'add Title'
            except:
                return 'error'

class Tournament(db.Model):
    __tableName__ = "tournament"
    id = db.Column(db.Integer, primary_key=True)
    tournament_name = db.Column(db.String(120), nullable=False)
    date_start_text = db.Column(db.String(120),nullable=False)
    # ForeignKey
    title = db.relationship('Title', backref='tournament', lazy=True)
    title_id = db.Column(db.Integer, db.ForeignKey('title.id'))

    
    def Insert(self,_Tournament,_title,_date_start_text):
        _Tournament=_Tournament.strip()
        _Tournament=_Tournament.lower()
        _title=_title.strip()
        _title=_title.lower()
        # print('count of tournemants')
        # print(Tournament.query.filter_by(tournament_name=_Tournament).count())
        if (Tournament.query.filter_by(tournament_name=_Tournament).count()==0):
                print(Title.query.filter_by(title=_title).count())
                if (Title.query.filter_by(title=_title).count()>0):
                    Title_id = Title.query.filter_by(title=_title).first().id
                    new_tournaments = Tournament(tournament_name=_Tournament,title_id=Title_id,date_start_text=_date_start_text)
                    db.session.add(new_tournaments)
                    db.session.commit()
                    return 'add Tournament'
                else:
                    raise turnamentError('forign key is not exist')
        else:
            print('tournament is exist')

class Team(db.Model):
    __tableName__ = "team"
    id = db.Column(db.Integer, primary_key=True)
    Team = db.Column(db.String(120), nullable=False)

    
    def Insert(self,_Team_id,_Team):
        if (Team.query.filter_by(id=_Team_id).count()==0):
            new_team = Team(id=_Team_id,Team=_Team)
            try:
                db.session.add(new_team)
                db.session.commit()
                print('add Team')
            except:
                return teamError('team is exist')
        else:
            return teamError('team is exist')

class Matches(db.Model):
    __tableName__ = "matches"
    id = db.Column(db.Integer, primary_key=True)
     # ForeignKey
    team1 = db.Column(db.Integer, db.ForeignKey('team.id'), unique=False, nullable=False)
    team2 =      db.Column(db.Integer, db.ForeignKey('team.id'), unique=False, nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), unique=False, nullable=False)

    
    def Insert(self,_Tournament,_Team1,_Team2):
        _Tournament = _Tournament.strip()
        _Tournament=_Tournament.lower()
        if (Tournament.query.filter_by(tournament_name=_Tournament).count()==1):
            _Tournament_id =  Tournament.query.filter_by(tournament_name=_Tournament).first().id
            if (Matches.query.filter_by(tournament_id=_Tournament_id).filter_by(team1=_Team1).filter_by(team2=_Team2).count()==0):
                new_matches = Matches(team1=_Team1,team2=_Team2,tournament_id=_Tournament_id)
                try:
                    db.session.add(new_matches)
                    db.session.commit()
                    print('add Matches')
                except:
                    return 'error'
            else:
                return matchesError('matche is exist')
        else:
            return matchesError('Turnament is not define')

class Scores(db.Model):
    __tableName__ = "scores"
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('matches.team1'),db.ForeignKey('matches.team2'), unique=False, nullable=True)
    # team_id_2 = db.Column(db.Integer, db.ForeignKey('matches.team2'), unique=False, nullable=True)
    matche_id = db.Column(db.Integer, db.ForeignKey('matches.id'), unique=False, nullable=False)
    winner = db.Column(db.Integer, nullable=True)
    Score = db.Column(db.Integer, nullable=True)

    
    def Insert(self,_Tournament, _Team,_Score,_winner,_Team1,_Team2):
        _Tournament = _Tournament.strip()
        _Tournament=_Tournament.lower()
        if (Tournament.query.filter_by(tournament_name=_Tournament).count()>0):
            _Tournament_id =  Tournament.query.filter_by(tournament_name=_Tournament).first().id
            if (Matches.query.filter_by(tournament_id=_Tournament_id).filter_by(team1=_Team1).filter_by(team2=_Team2).count>0):
                _Matched_id = Matches.query.filter_by(tournament_id=_Tournament_id).filter_by(team1=_Team1).filter_by(team2=_Team2).first().id
                if (Scores.query.filter_by(matche_id=_Matched_id).filter_by(team_id=_Team).count()==0):
                    new_score = Scores(team_id=_Team,matche_id=_Matched_id,Score=_Score,winner=_winner)
                    try:
                        db.session.add(new_score)
                        db.session.commit()
                        print('add Score')
                    except:
                        return 'error'
            else:
                raise scoresError('matches is not exist')
        else:
            raise scoresError('turnament is not exist')


from sqlalchemy import text
import random

class report():

        def myjosn(self,row):
                return {
                    'title':row['title'],
                    'state':row['state'],
                    'tournament_name':row['tournament_name'],
                    'winner':row['winner'],
                    'score':row['Score'],
                    'Team':row['Team']
                }

        
        def report(self):
            SQLCommand="SELECT \
                                title.title, \
                                title.state, \
                                tournament.tournament_name, \
                                team.Team , \
                                scores.winner,\
                                scores.Score \
                        FROM title \
                                inner join tournament on title.id=tournament.title_id   \
                                inner join matches on matches.tournament_id=tournament.id \
                                inner join scores on (scores.team_id=matches.team1 or scores.team_id=matches.team2) and scores.matche_id=matches.id \
                                inner join team on team.id = scores.team_id" 

            sql = text(SQLCommand)
            cursor = db.engine.execute(sql)

       

            tmp={}
            i=0
            for row in cursor:
                i+=1
                tmp.update({i: report.myjosn(row)})

            # return json.dumps([{str(idx+1):report.myjosn(row)} for idx,row in enumerate(cursor)])

            return tmp


         
            
              # myText =''
            # for idx, val in enumerate(cursor):
            #     if myText !='':
            #         myText=myText+","
            #     txt1 = " \"{indx}\": ".format(indx=idx+1)
            #     txt2 = " \"title\":\"{title}\" ,".format(title=val[0])
            #     txt3 = " \"state\":\"{state}\" ,".format(state=val[1])
            #     txt4 = " \"tournament_name\":\"{tournament_name}\" ,".format(tournament_name=val[2])
            #     txt5 = " \"Team\":\"{Team}\" ,".format(Team=val[3])
            #     txt6 = " \"winner\":\"{winner}\" ,".format(winner=val[4])
            #     txt7 = " \"score\":\"{score}\" ".format(score=val[5])
            #     txt = txt1+"{"+txt2+txt3+txt4+txt5+txt6+txt7+"}"
            #     myText+=txt
            # myText="{"+myText+"}"
            # return json.loads(myText)