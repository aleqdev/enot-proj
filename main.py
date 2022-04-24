import stage
import config
import asyncio

async def main():
    s = await stage.StartupStage.new(config)
    while True:
        await s.start()
        while s.running:
            await s.display()
        s = await s.next()


if __name__ == "__main__":
    asyncio.run(main())