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
    date_start_text = db.Column(db.String(120),nullable=False)
    state = db.Column(db.Integer,nullable=False)

    @staticmethod
    def Insert(_Title,_date_start_text,_state):
        _Title = _Title.strip()
        print(_Title)
        print(Title.query.filter_by(title=_Title).count())
        if Title.query.filter_by(title=_Title).count()==0:
            new_title = Title(title= _Title,date_start_text=_date_start_text,state=_state)
            try:
                db.session.add(new_title)
                db.session.commit()
                print('add Title')
            except:
                return 'error'
        # else:
        #     Title_info = Title.query.filter_by(title=_Title).first()
        #     title_id = Title_info.id
        #     print('title id is '+ str(title_id))



class Tournament(db.Model):
    __tableName__ = "tournamet"
    id = db.Column(db.Integer, primary_key=True)
    tournament = db.Column(db.String(120), nullable=False)
    title = db.relationship('Title', backref='tournamet', lazy=True)
    title_id = db.Column(db.Integer, db.ForeignKey('title.id'))

    @staticmethod
    def Insert(_Tournament):



        new_tournaments = Tournament(tournament=_Tournament,title_id=1)
        # try:
        db.session.add(new_tournaments)
        res = db.session.commit()
        print('add Tournament')
        #     return 200
        # except:
        #     return 500




class Team(db.Model):
    __tableName__ = "team"
    id = db.Column(db.Integer, primary_key=True)
    Team = db.Column(db.String(120), nullable=False)
    Team_id = db.Column(db.Integer,nullable=False)

    @staticmethod
    def Insert(_Team_id,_Team):
        new_team = Team(Team=_Team,Team_id=_Team_id)
        # try:
        db.session.add(new_team)
        db.session.commit()
        print('add Team')
        #     return 200
        # except:
        #     return 500

class Matches(db.Model):
    __tableName__ = "matches"
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(120), nullable=False)
    Tournament = db.Column(db.String(120), nullable=True)
    Team = db.Column(db.String(120), nullable=True)
    Match = db.Column(db.String(120), nullable=True)
    Scores= db.Column(db.Integer, nullable=True)



    def json(self):
        return {
                                    'id': self.id, 
                                    'Title': self.Title, 
                                    'Tournament': self.Tournament,
                                    'Team': self.Team,
                                    'Match': self.Match,
                                     'Scores': self.Scores
                                    }

    def __repr__(self):
        json_matches_table = {
                                'id': self.id, 
                                'Title': self.Title, 
                                'Tournament': self.Tournament,
                                'Team': self.Team,
                                'Match': self.Match,
                                'Scores': self.Scores
        }
        return json.dumps(json_matches_table)



class Scores(db.Model):
    __tableName__ = "scores"
    id = db.Column(db.Integer, primary_key=True)
    Scores = db.Column(db.String(120), nullable=False)

    # def Insert(_Title, _Tournament, _Team,_Match,_Score):
    #     new_match = Matches(Title= _Title,Tournament=  _Tournament, Team=_Team,Match=_Match,Scores=_Score)
    #     try:
    #         db.session.add(new_match)
    #         db.session.commit()
    #         return 200
    #     except:
    #         return 500
