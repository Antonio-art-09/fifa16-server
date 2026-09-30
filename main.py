import asyncio
import database

database.init_db()

async def handle_ps4(reader, writer):
    print("¡PS4 conectada a FIFA 16 Online!")
    data = await reader.read(100)
    writer.write(b'\x00\x00\x00\x00\x00\x00\x00\x01')
    await writer.drain()

async def main():
    server = await asyncio.start_server(handle_ps4, '0.0.0.0', 42127)
    print("Servidor listo en la nube.")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
