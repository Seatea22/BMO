import asyncio

from bmo import BMO


def main():
    bmo_obj = BMO()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(bmo_obj.input_registration_loop())
    loop.close()


if __name__ == '__main__':
    main()
