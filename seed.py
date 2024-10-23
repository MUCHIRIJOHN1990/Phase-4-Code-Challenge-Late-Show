# seed.py

from app import app, db
from models import Appearance, Episode, Guest

app.app_context().push()


def seed():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create Episodes
    episode1 = Episode(date="1/11/99", number=1)
    episode2 = Episode(date="1/12/99", number=2)

    # Create Guests
    guest1 = Guest(name="Michael J. Fox", occupation="actor")
    guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    guest3 = Guest(name="Tracey Ullman", occupation="television actress")

    # Create Appearances
    appearance1 = Appearance(rating=4, episode=episode1, guest=guest1)
    appearance2 = Appearance(rating=5, episode=episode2, guest=guest3)

    # Add to session
    db.session.add_all(
        [episode1, episode2, guest1, guest2, guest3, appearance1, appearance2])

    # Commit
    db.session.commit()


if __name__ == '__main__':
    seed()
    print("Database seeded successfully!")
