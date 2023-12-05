from app import app, db
from app.models import Albums
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def initialise_database():
    albums_data = [

    {'title': 'Thriller', 'artist': 'Michael Jackson', 'genre': 'Pop/R&B'},
    {'title': 'Highway 61 Revisited', 'artist': 'Bob Dylan', 'genre': 'Folk/Rock'},
    {'title': 'Kind of Blue', 'artist': 'Miles Davis', 'genre': 'Jazz'},
    {'title': 'IV', 'artist': 'Led Zeppelin', 'genre': 'Rock'},
    {'title': 'OK Computer', 'artist': 'Radiohead', 'genre': 'Rock'},
    {'title': 'Rumours', 'artist': 'Fleetwood Mac', 'genre': 'Rock'},
    {'title': 'Purple Rain', 'artist': 'Prince', 'genre': 'Pop/R&B'},
    {'title': 'Nevermind', 'artist': 'Nirvana', 'genre': 'Rock'},
    {'title': 'Exile on Main St.', 'artist': 'The Rolling Stones', 'genre': 'Rock'},
    {'title': 'The Rise and Fall of Ziggy Stardust', 'artist': 'David Bowie', 'genre': 'Rock'},
    {'title': 'A Night at the Opera', 'artist': 'Queen', 'genre': 'Rock'},
    {'title': 'Who''s Next', 'artist': 'The Who', 'genre': 'Rock'},
    {'title': 'Legend', 'artist': 'Bob Marley & The Wailers', 'genre': 'Reggae'},
    {'title': 'Hotel California', 'artist': 'The Eagles', 'genre': 'Rock'},
    {'title': 'At Folsom Prison', 'artist': 'Johnny Cash', 'genre': 'Country'},
    {'title': 'The Joshua Tree', 'artist': 'U2', 'genre': 'Rock'},
    {'title': 'Born to Run', 'artist': 'Bruce Springsteen', 'genre': 'Rock'},
    {'title': 'Pet Sounds', 'artist': 'The Beach Boys', 'genre': 'Pop/Rock'},
    {'title': 'The Chain', 'artist': 'Fleetwood Mac', 'genre': 'Rock'},
    {'title': 'Appetite for Destruction', 'artist': 'Guns N'' Roses', 'genre': 'Rock'},
    {'title': 'Wish You Were Here', 'artist': 'Pink Floyd', 'genre': 'Rock'},
    {'title': 'Back in Black', 'artist': 'AC/DC', 'genre': 'Rock'},
    {'title': 'Bridge Over Troubled Water', 'artist': 'Simon & Garfunkel', 'genre': 'Folk/Rock'},
    {'title': 'Sign o'' the Times', 'artist': 'Prince and the Revolution', 'genre': 'Pop/R&B'},
    {'title': 'London Calling', 'artist': 'The Clash', 'genre': 'Punk/Rock'},
    {'title': '(What''s the Story) Morning Glory?', 'artist': 'Oasis', 'genre': 'Rock'},
    {'title': 'Are You Experienced', 'artist': 'Jimi Hendrix', 'genre': 'Rock'},
    {'title': 'The Bends', 'artist': 'Radiohead', 'genre': 'Rock'},
    {'title': 'Bad', 'artist': 'Michael Jackson', 'genre': 'Pop/R&B'},
    {'title': 'The Doors', 'artist': 'The Doors', 'genre': 'Rock'},
    {'title': 'To Pimp a Butterfly', 'artist': 'Kendrick Lamar', 'genre': 'Hip-Hop'},
    {'title': 'In Utero', 'artist': 'Nirvana', 'genre': 'Rock'},
    {'title': 'Sticky Fingers', 'artist': 'The Rolling Stones', 'genre': 'Rock'},
    {'title': 'Darkness on the Edge of Town', 'artist': 'Bruce Springsteen', 'genre': 'Rock'},
    {'title': 'Is This It', 'artist': 'The Strokes', 'genre': 'Rock'},
    {'title': 'The Velvet Underground & Nico', 'artist': 'The Velvet Underground', 'genre': 'Rock'},
    {'title': 'Remain in Light', 'artist': 'Talking Heads', 'genre': 'New Wave/Rock'},
    {'title': 'Songs in the Key of Life', 'artist': 'Stevie Wonder', 'genre': 'Soul/R&B'},
    {'title': 'Tusk', 'artist': 'Fleetwood Mac', 'genre': 'Rock'},
    {'title': 'Blonde on Blonde', 'artist': 'Bob Dylan', 'genre': 'Folk/Rock'},
    {'title': 'Ten', 'artist': 'Pearl Jam', 'genre': 'Rock'},
    {'title': 'Synchronicity', 'artist': 'The Police', 'genre': 'New Wave/Rock'},
    {'title': 'Imagine', 'artist': 'John Lennon', 'genre': 'Rock'},
    {'title': 'Stankonia', 'artist': 'OutKast', 'genre': 'Hip-Hop'},
    {'title': 'Odelay', 'artist': 'Beck', 'genre': 'Alternative Rock'},
    {'title': 'Disintegration', 'artist': 'The Cure', 'genre': 'Goth Rock'},
    {'title': 'Fleetwood Mac', 'artist': 'Fleetwood Mac', 'genre': 'Rock'},
    {'title': 'Definitely Maybe', 'artist': 'Oasis', 'genre': 'Rock'},
    {'title': 'Pearl', 'artist': 'Janis Joplin', 'genre': 'Blues/Rock'},
    {'title': 'Ready to Die', 'artist': 'The Notorious B.I.G.', 'genre': 'Hip-Hop'},
    {'title': 'Damn the Torpedoes', 'artist': 'Tom Petty and the Heartbreakers', 'genre': 'Rock'},
    {'title': 'The Queen Is Dead', 'artist': 'The Smiths', 'genre': 'Alternative Rock'},
    {'title': 'Harvest', 'artist': 'Neil Young', 'genre': 'Folk/Rock'},
    {'title': 'At San Quentin', 'artist': 'Johnny Cash', 'genre': 'Country'},
    {'title': 'Unknown Pleasures', 'artist': 'Joy Division', 'genre': 'Post-Punk/Rock'},
    {'title': 'Let It Bleed', 'artist': 'The Rolling Stones', 'genre': 'Rock'},
    {'title': 'Automatic for the People', 'artist': 'R.E.M.', 'genre': 'Alternative Rock'},
    {'title': 'AM', 'artist': 'Arctic Monkeys', 'genre': 'Indie Rock'},
    {'title': 'Electric Ladyland', 'artist': 'The Jimi Hendrix Experience', 'genre': 'Rock'},
    {'title': 'Dookie', 'artist': 'Green Day', 'genre': 'Punk/Rock'},
    {'title': 'Kid A', 'artist': 'Radiohead', 'genre': 'Rock'},
    {'title': 'Rage Against the Machine', 'artist': 'Rage Against the Machine', 'genre': 'Alternative Metal'},
    {'title': 'American IV: The Man Comes Around', 'artist': 'Johnny Cash', 'genre': 'Country'},
    {'title': 'Dummy', 'artist': 'Portishead', 'genre': 'Trip-Hop'},
    {'title': 'Elephant', 'artist': 'The White Stripes', 'genre': 'Rock'},
    {'title': 'Goodbye Yellow Brick Road', 'artist': 'Elton John', 'genre': 'Pop/Rock'},
    {'title': 'Meat Is Murder', 'artist': 'The Smiths', 'genre': 'Alternative Rock'},
    {'title': 'Metallica', 'artist': 'Metallica', 'genre': 'Metal'},
    {'title': 'Funeral', 'artist': 'Arcade Fire', 'genre': 'Indie Rock'},
    {'title': 'L.A. Woman', 'artist': 'The Doors', 'genre': 'Rock'},
    {'title': 'Abbey Road', 'artist': 'The Beatles', 'genre': 'Rock'},
    {'title': 'Graceland', 'artist': 'Paul Simon', 'genre': 'World/Folk'},
    {'title': 'Beggars Banquet', 'artist': 'The Rolling Stones', 'genre': 'Rock'},
    {'title': 'Rumours', 'artist': 'Fleetwood Mac', 'genre': 'Rock'},
    {'title': 'The Clash', 'artist': 'The Clash', 'genre': 'Punk/Rock'},
    {'title': 'Illmatic', 'artist': 'Nas', 'genre': 'Hip-Hop'},
    {'title': 'Physical Graffiti', 'artist': 'Led Zeppelin', 'genre': 'Rock'},
    {'title': 'Hunky Dory', 'artist': 'David Bowie', 'genre': 'Rock'},
    {'title': 'Unplugged', 'artist': 'Eric Clapton', 'genre': 'Blues/Rock'},
    {'title': 'My Beautiful Dark Twisted Fantasy', 'artist': 'Kanye West', 'genre': 'Hip-Hop'},
    {'title': 'Blood on the Tracks', 'artist': 'Bob Dylan', 'genre': 'Folk/Rock'},
    {'title': 'Doolittle', 'artist': 'Pixies', 'genre': 'Alternative Rock'},
    {'title': 'Hail to the Thief', 'artist': 'Radiohead', 'genre': 'Rock'},
    {'title': 'good kid, m.A.A.d city', 'artist': 'Kendrick Lamar', 'genre': 'Hip-Hop'},
    {'title': 'Some Girls', 'artist': 'The Rolling Stones', 'genre': 'Rock'},
    {'title': 'Revolver', 'artist': 'The Beatles', 'genre': 'Rock'},
    {'title': 'Be Here Now', 'artist': 'Oasis', 'genre': 'Rock'},
    {'title': 'Vs.', 'artist': 'Pearl Jam', 'genre': 'Rock'},
    {'title': 'American III: Solitary Man', 'artist': 'Johnny Cash', 'genre': 'Country'},
    {'title': 'Loaded', 'artist': 'The Velvet Underground', 'genre': 'Rock'},
    {'title': 'Whatever People Say I Am, That''s What I''m Not', 'artist': 'Arctic Monkeys', 'genre': 'Indie Rock'},
    {'title': 'Amnesiac', 'artist': 'Radiohead', 'genre': 'Rock'},
    {'title': 'The Head on the Door', 'artist': 'The Cure', 'genre': 'New Wave/Rock'},
    {'title': 'Mirage', 'artist': 'Fleetwood Mac', 'genre': 'Rock'},
    {'title': 'Exodus', 'artist': 'Bob Marley & The Wailers', 'genre': 'Reggae'},
    {'title': 'Sea Change', 'artist': 'Beck', 'genre': 'Alternative Rock'},
    {'title': 'Led Zeppelin II', 'artist': 'Led Zeppelin', 'genre': 'Rock'},
    {'title': 'Blood Sugar Sex Magik', 'artist': 'Red Hot Chili Peppers', 'genre': 'Rock'}
]
    

    with app.app_context():
        for data in albums_data:
            album = Albums(**data)
            db.session.add(album)

        db.session.commit()



if __name__ == "__main__":
    initialise_database()




