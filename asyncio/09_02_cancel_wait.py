import asyncio
from asyncio import FIRST_EXCEPTION

import aiohttp


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


def print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photos_by_album(task_name, album, session):
    print(f'{task_name=}')
    if not isinstance(album, int):
        await asyncio.sleep(2)
        raise RuntimeError('invalid album number')

    url = f'https://jsonplaceholder.typicode.com/albums/{album}/photos/'

    response = await session.get(url)
    photos_json = await response.json()

    sleeping_period = 3 if task_name == 't3' else 1
    print(f'{task_name=} sleeping')
    await asyncio.sleep(sleeping_period)
    print(f'{task_name=} finished sleeping')

    print(f'Finished task={task_name}')
    return [Photo.from_json(photo) for photo in photos_json]


async def main_wait():
    async with aiohttp.ClientSession() as session:
        tasks = [
            photos_by_album('t1', 1, session),
            photos_by_album('t2', 2, session),
            photos_by_album('t3', 3, session),
            photos_by_album('ta', 'a', session),
            photos_by_album('t5', 5, session)
        ]

        photos = []
        # done_tasks, pending_tasks = await asyncio.wait([asyncio.create_task(t) for t in tasks])
        done_tasks, pending_tasks = await asyncio.wait([asyncio.create_task(t) for t in tasks],
                                                       return_when=FIRST_EXCEPTION)

        for pending_task in pending_tasks:
            print(f'cancelling {pending_task}')
            print(pending_task.cancel())

        for done in done_tasks:
            try:
                result = done.result()
                photos.extend(result)
            except Exception as ex:
                print(repr(ex))

        print_photo_titles(photos)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    try:
        loop.create_task(main_wait())
        loop.run_forever()
    finally:
        print('Closing loop')
        loop.close()
