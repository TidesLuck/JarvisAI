import boto3
import asyncio
import os

class CloudSync:
    def __init__(self, cloud_config):
        self.s3 = boto3.client("s3")
        self.bucket = cloud_config["bucket"]
        self.sync_interval = cloud_config["sync_interval"]

    async def sync_knowledge(self):
        while True:
            for root, _, files in os.walk("data/knowledge"):
                for file in files:
                    local_path = os.path.join(root, file)
                    s3_path = local_path.replace("data/", "")
                    self.s3.upload_file(local_path, self.bucket, s3_path)
            await asyncio.sleep(self.sync_interval)