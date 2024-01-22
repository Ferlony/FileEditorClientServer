from asyncio import run

import uvicorn

from router import app
from config_dataclass import ConfigData


async def main():
    config = uvicorn.Config("main_server:app",
                            host=ConfigData.config_host,
                            port=ConfigData.config_port,
                            log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    run(main())
