from flask import Blueprint, jsonify, abort, request
from ..models import Tweet, User, db
import hashlib
import secrets
import sqlalchemy


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all()  # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain username and password
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    # construct user account
    u = User(
        username=request.json['username'],
        password=request.json['password']
    )
    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(u.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PUT'])
def update(id: int):

    u = User(
        username=request.json['username'],
        password=request.json['password']
    )
    u = User.query.get_or_404(id)
    try:
        db.session.add(u)  # prepare UPDATE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    u = User.query.get_or_404(id)
    result = []
    for t in u.liked_tweets:
        result.append(t.serialize())
    return jsonify(result)


#Bonus 2 task
@bp.route('/<int:id>/likes/<int:id>', methods=['DELETE'])
def unlike(u_id: int, t_id: int):
    u = User.query.get_or_404(u_id)
    t = Tweet.query.get_or_404(t_id)

    stmt = sqlalchemy.delete(likes_table).where(
        sqlalchemy.and_(likes_table.c.user_id == u_id,
                        likes_table.c.tweet_id == t_id)
    )
