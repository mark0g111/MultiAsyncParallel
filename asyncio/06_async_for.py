import asyncio


async def fetch_doc(doc):
    print(f'opening file {doc}')
    await asyncio.sleep(3)
    return doc


async def get_pages(docs):
    for cur_dock in docs:
        doc = await fetch_doc(cur_dock)
        print(f'get pages from file {cur_dock}')
        for page in doc:
            await asyncio.sleep(1)
            yield page


async def main():
    async for page in get_pages(['doc1', 'doc2']):
        print(f'finally {page}')


if __name__ == '__main__':
    asyncio.run(main())
