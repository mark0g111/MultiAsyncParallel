import asyncio

import aiohttp as aiohttp

from async_decorator import async_measure_time


def print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photos_by_album(task_name, album, session):
    print(f'{task_name}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'
    response = await session.get(url)
    photos_json = await response.json()

    return [Photo.from_json(photo) for photo in photos_json]


@async_measure_time
async def main():
    async with aiohttp.ClientSession() as session:
        photos = await photos_by_album('Task 1', 3, session)
        print_photo_titles(photos)


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
