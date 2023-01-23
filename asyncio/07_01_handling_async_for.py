import asyncio
import time

import aiohttp


def print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photos_by_album(task_name, album, session):
    print(f'{task_name}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'
    response = await session.get(url)
    photos_json = await response.json()

    return [Photo.from_json(photo) for photo in photos_json]


async def download_albums(albums):
    async with aiohttp.ClientSession() as session:
        for album in albums:
            if not isinstance(album, int):
                raise RuntimeError('invalid album number')
            yield await photos_by_album(f't{album}', album, session)


async def main():
    try:
        async for photos in download_albums([1, 2, 'a', 4]):
            print_photo_titles(photos)
    except Exception as ex:
        print(repr(ex))


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.album_id = album_id
        self.photo_id = photo_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


if __name__ == '__main__':
    asyncio.run(main())
    time.sleep(3)
    print('main ended')
