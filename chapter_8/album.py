def make_album(artist_name, album_title, number_of_songs = None):
    if number_of_songs:
        return {'Artist Name': artist_name.title(), 'Album Title': album_title.title(), 'Number of Songs': number_of_songs}
    return {'Artist Name': artist_name.title(), 'Album Title': album_title.title()}

# print(make_album('Disturbed', 'Indestructible'))
# print(make_album('linkin park', 'meteora', 14))
# print(make_album('Disturbed', 'asylum'))

while True:
    print("\nEnter the artist name and the album title (q to quit)")
    artist_name = input('Artist name: ')
    if artist_name == 'q':
        break
    album_title = input('Album title:')
    if album_title == 'q':
        break
    print(make_album(artist_name, album_title))
