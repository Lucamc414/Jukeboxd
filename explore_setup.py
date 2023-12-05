from app import app, db
from app.models import Review
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def initialise_reviews():
    reviews = [
    {'title': 'Thriller', 'artist': 'Michael Jackson', 'review': "An absolute masterpiece! Michael Jackson's Thriller is a timeless classic that never gets old. The production is top-notch, and every track is a hit. A must-listen for all music lovers.", 'rating': 5, 'album': 'Thriller', 'username': 'user1'},
    {'title': 'Highway 61 Revisited', 'artist': 'Bob Dylan', 'review': "Bob Dylan's poetic lyrics and unique voice shine in Highway 61 Revisited. A true folk-rock gem that takes you on a lyrical journey. Highly recommended for those who appreciate profound songwriting.", 'rating': 4, 'album': 'Highway 61 Revisited', 'username': 'user2'},
    {'title': 'Kind of Blue', 'artist': 'Miles Davis', 'review': "Miles Davis's Kind of Blue is a jazz masterpiece. The smooth, improvisational style creates a soothing atmosphere. A perfect album to unwind and appreciate the artistry of jazz.", 'rating': 5, 'album': 'Kind of Blue', 'username': 'user3'},
    {'title': 'IV', 'artist': 'Led Zeppelin', 'review': "Led Zeppelin's IV is a rock classic that defines the genre. Each track is a powerhouse, showcasing the band's musical prowess. A rock masterpiece that stands the test of time.", 'rating': 4, 'album': 'IV', 'username': 'user4'},
    {'title': 'OK Computer', 'artist': 'Radiohead', 'review': "OK Computer is a sonic journey into the future. Radiohead's experimental approach and thought-provoking lyrics make this album a groundbreaking work of art. A must-listen for fans of alternative rock.", 'rating': 5, 'album': 'OK Computer', 'username': 'user5'},
    {'title': 'Rumours', 'artist': 'Fleetwood Mac', 'review': "Rumours is a timeless classic filled with emotional depth and captivating melodies. Fleetwood Mac's chemistry is evident in every song. A true masterpiece that deserves its place in music history.", 'rating': 5, 'album': 'Rumours', 'username': 'user6'},
    {'title': 'Purple Rain', 'artist': 'Prince', 'review': "Prince's Purple Rain is a pop/R&B sensation. The iconic title track and soulful ballads showcase Prince's musical genius. A groundbreaking album that pushed the boundaries of the genre.", 'rating': 4, 'album': 'Purple Rain', 'username': 'user7'},
    {'title': 'Nevermind', 'artist': 'Nirvana', 'review': "Nirvana's Nevermind revolutionized the rock scene. The raw energy and Kurt Cobain's distinctive voice make this album a grunge classic. An essential addition to any rock music collection.", 'rating': 4, 'album': 'Nevermind', 'username': 'user8'},
    {'title': 'Exile on Main St.', 'artist': 'The Rolling Stones', 'review': "Exile on Main St. captures the essence of rock 'n' roll. The Rolling Stones deliver a gritty and soulful performance, making each track memorable. A rock masterpiece that never gets old.", 'rating': 5, 'album': 'Exile on Main St.', 'username': 'user9'},
    {'title': 'The Rise and Fall of Ziggy Stardust', 'artist': 'David Bowie', 'review': "David Bowie's Ziggy Stardust is a glam rock triumph. The concept album tells a captivating story, and Bowie's charismatic persona shines through. A must-listen for fans of theatrical rock.", 'rating': 4, 'album': 'The Rise and Fall of Ziggy Stardust', 'username': 'user10'},
    {'title': 'A Night at the Opera', 'artist': 'Queen', 'review': "Queen's A Night at the Opera is a musical spectacle. Freddie Mercury's operatic vocals and the band's diverse instrumentation create a unique listening experience. An iconic album that transcends genres.", 'rating': 5, 'album': 'A Night at the Opera', 'username': 'user11'},
    {'title': 'Who\'s Next', 'artist': 'The Who', 'review': "The Who's Who's Next is a rock powerhouse. The energetic performances and Pete Townshend's songwriting brilliance make this album a classic. A must-have for any rock enthusiast.", 'rating': 4, 'album': 'Who\'s Next', 'username': 'user12'},
    {'title': 'Legend', 'artist': 'Bob Marley & The Wailers', 'review': "Bob Marley's Legend is a reggae masterpiece. The album is a compilation of Marley's greatest hits, showcasing his influential and soulful reggae sound. A timeless collection for reggae fans.", 'rating': 5, 'album': 'Legend', 'username': 'user13'},
    {'title': 'Hotel California', 'artist': 'The Eagles', 'review': "The Eagles' Hotel California is a rock masterpiece. The title track and the album's overall storytelling make it a classic. A must-listen for those who appreciate intricate guitar work and thoughtful lyrics.", 'rating': 4, 'album': 'Hotel California', 'username': 'user14'},
    {'title': 'At Folsom Prison', 'artist': 'Johnny Cash', 'review': "Johnny Cash's At Folsom Prison is a raw and powerful live recording. The emotion in Cash's voice and the authenticity of the performance make it a landmark album in country music history.", 'rating': 5, 'album': 'At Folsom Prison', 'username': 'user15'},
    {'title': 'The Joshua Tree', 'artist': 'U2', 'review': "U2's The Joshua Tree is a rock epic. The anthemic sound and Bono's emotive vocals create a sonic landscape that leaves a lasting impact. A quintessential album for rock enthusiasts.", 'rating': 4, 'album': 'The Joshua Tree', 'username': 'user16'},
    {'title': 'Born to Run', 'artist': 'Bruce Springsteen', 'review': "Bruce Springsteen's Born to Run is a rock and roll masterpiece. The title track and the entire album capture the spirit of freedom and rebellion. A must-listen for fans of classic rock.", 'rating': 5, 'album': 'Born to Run', 'username': 'user17'},
    {'title': 'Pet Sounds', 'artist': 'The Beach Boys', 'review': "The Beach Boys' Pet Sounds is a pop/rock triumph. Brian Wilson's innovative production and the harmonious vocals create a sonic masterpiece. An album that pushed the boundaries of pop music.", 'rating': 4, 'album': 'Pet Sounds', 'username': 'user18'},
    {'title': 'The Chain', 'artist': 'Fleetwood Mac', 'review': "Fleetwood Mac's The Chain is a rock anthem. The powerful vocals and the dynamic instrumentation make it a standout track in rock history. A must-listen for fans of classic rock.", 'rating': 5, 'album': 'The Chain', 'username': 'user19'}
]

    with app.app_context():
        for data in reviews:
            review = Review(**data)
            db.session.add(review)

        db.session.commit()



if __name__ == "__main__":
    initialise_reviews()




