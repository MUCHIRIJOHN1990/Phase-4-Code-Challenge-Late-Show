# routes.py

from flask import Blueprint, request
from flask_restful import Api, Resource

from models import Appearance, Episode, Guest, db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


class EpisodesList(Resource):

    def get(self):
        episodes = Episode.query.all()
        return [
            episode.to_dict(rules=('-appearances', )) for episode in episodes
        ], 200


class EpisodeDetail(Resource):

    def get(self, episode_id):
        episode = Episode.query.get(episode_id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return episode.to_dict()


class GuestsList(Resource):

    def get(self):
        guests = Guest.query.all()
        return [guest.to_dict(rules=('-appearances', ))
                for guest in guests], 200


class AppearanceList(Resource):

    def post(self):
        data = request.get_json()
        rating = data.get('rating')
        episode_id = data.get('episode_id')
        guest_id = data.get('guest_id')

        errors = []

        # Validate presence
        if rating is None:
            errors.append("Rating is required.")
        if episode_id is None:
            errors.append("Episode ID is required.")
        if guest_id is None:
            errors.append("Guest ID is required.")

        # Validate rating range
        if rating is not None and not (1 <= rating <= 5):
            errors.append("Rating must be between 1 and 5.")

        # Validate foreign keys
        episode = Episode.query.get(episode_id)
        if not episode:
            errors.append("Episode not found.")
        guest = Guest.query.get(guest_id)
        if not guest:
            errors.append("Guest not found.")

        if errors:
            return {"errors": errors}, 400

        # Create Appearance
        appearance = Appearance(rating=rating, episode=episode, guest=guest)
        db.session.add(appearance)
        db.session.commit()

        return appearance.to_dict(), 201


# Add Resources to API
api.add_resource(EpisodesList, '/episodes')
api.add_resource(EpisodeDetail, '/episodes/<int:episode_id>')
api.add_resource(GuestsList, '/guests')
api.add_resource(AppearanceList, '/appearances')
