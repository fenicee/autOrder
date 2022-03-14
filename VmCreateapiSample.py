import sys
from typing import List

from ecloudsdkcore.config.config import Config
from ecloudsdkecs.v1 import VmCreateapiRequest
from ecloudsdkecs.v1.client import Client


class VmCreateapiSample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
            access_key: str,
            access_secret: str,
            pool_id: str
    ) -> Client:
        """
        使用AK&SK初始化账号Client
        @param access_key:
        @param access_secret:
        @param pool_id:
        @return: Client
        @throws Exception
        """
        config = Config(
            access_key=access_key,
            access_secret=access_secret,
            pool_id=pool_id
        )
        return Client(config)

    @staticmethod
    def main(
            args: List[str]
    ) -> None:
        client = VmCreateapiSample.create_client("<YOUR AK>", "<YOUR SK>", "poolId")
        request = VmCreateapiRequest()

        client.vm_createapi(request)


if __name__ == '__main__':
    VmCreateapiSample.main(sys.argv[1:])