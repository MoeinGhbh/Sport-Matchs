from flask_sqlalchemy import SQLAlchemy
from config import app
import json


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

    @staticmethod
    def Insert(_Title,_state):
        _Title = _Title.strip()
        _Title = _Title.lower()
        # print(_Title)
        # print(Title.query.filter_by(title=_Title).count())
        if Title.query.filter_by(title=_Title).count()==0:
            new_title = Title(title= _Title,state=_state)
            try:
                db.session.add(new_title)
                db.session.commit()
                print('add Title')
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

    @staticmethod
    def Insert(_Tournament,_title,_date_start_text):
        _Tournament=_Tournament.strip()
        _Tournament=_Tournament.lower()
        _title=_title.strip()
        _title=_title.lower()
        # print('count of tournemants')
        # print(Tournament.query.filter_by(tournament_name=_Tournament).count())
        if (Tournament.query.filter_by(tournament_name=_Tournament).count()==0):
            Title_id = Title.query.filter_by(title=_title).first().id
            new_tournaments = Tournament(tournament_name=_Tournament,title_id=Title_id,date_start_text=_date_start_text)
            try:
                db.session.add(new_tournaments)
                res = db.session.commit()
                print('add Tournament')
            except:
                return 'error'
        else:
            print('tournament is exist')

class Team(db.Model):
    __tableName__ = "team"
    id = db.Column(db.Integer, primary_key=True)
    Team = db.Column(db.String(120), nullable=False)

    @staticmethod
    def Insert(_Team_id,_Team):
        if (Team.query.filter_by(id=_Team_id).count()==0):
            new_team = Team(id=_Team_id,Team=_Team)
            try:
                db.session.add(new_team)
                db.session.commit()
                print('add Team')
            except:
                return 'error'

class Matches(db.Model):
    __tableName__ = "matches"
    id = db.Column(db.Integer, primary_key=True)
     # ForeignKey
    team1 = db.Column(db.Integer, db.ForeignKey('team.id'), unique=False, nullable=False)
    team2 =      db.Column(db.Integer, db.ForeignKey('team.id'), unique=False, nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), unique=False, nullable=False)

    @staticmethod
    def Insert(_Tournament,_Team1,_Team2):
        _Tournament = _Tournament.strip()
        _Tournament=_Tournament.lower()
        _Tournament_id =  Tournament.query.filter_by(tournament_name=_Tournament).first().id
        if (Matches.query.filter_by(tournament_id=_Tournament_id).filter_by(team1=_Team1).filter_by(team2=_Team2).count()==0):
            new_matches = Matches(team1=_Team1,team2=_Team2,tournament_id=_Tournament_id)
            try:
                db.session.add(new_matches)
                db.session.commit()
                print('add Matches')
            except:
                return 'error'

class Scores(db.Model):
    __tableName__ = "scores"
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('matches.team1'),db.ForeignKey('matches.team2'), unique=False, nullable=True)
    # team_id_2 = db.Column(db.Integer, db.ForeignKey('matches.team2'), unique=False, nullable=True)
    matche_id = db.Column(db.Integer, db.ForeignKey('matches.id'), unique=False, nullable=False)
    winner = db.Column(db.Integer, nullable=True)
    Score = db.Column(db.Integer, nullable=True)

    @staticmethod
    def Insert(_Tournament, _Team,_Score,_winner,_Team1,_Team2):
        _Tournament = _Tournament.strip()
        _Tournament=_Tournament.lower()
        _Tournament_id =  Tournament.query.filter_by(tournament_name=_Tournament).first().id
        
        _Matched_id = Matches.query.filter_by(tournament_id=_Tournament_id).filter_by(team1=_Team1).filter_by(team2=_Team2).first().id



        if (Scores.query.filter_by(matche_id=_Matched_id).filter_by(team_id=_Team).count()==0):
            new_score = Scores(team_id=_Team,matche_id=_Matched_id,Score=_Score,winner=_winner)
            try:
                db.session.add(new_score)
                db.session.commit()
                print('add Score')
            except:
                return 'error'




    # def json(self):
    #     return {
    #                                 'id': self.id, 
    #                                 'Title': self.Title, 
    #                                 'Tournament': self.Tournament,
    #                                 'Team': self.Team,
    #                                 'Match': self.Match,
    #                                  'Scores': self.Scores
    #                                 }

    # def __repr__(self):
    #     json_matches_table = {
    #                             'id': self.id, 
    #                             'Title': self.Title, 
    #                             'Tournament': self.Tournament,
    #                             'Team': self.Team,
    #                             'Match': self.Match,
    #                             'Scores': self.Scores
    #     }
    #     return json.dumps(json_matches_table)




