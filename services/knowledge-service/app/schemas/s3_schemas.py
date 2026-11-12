from dataclasses import dataclass
from typing import Optional


@dataclass
class S3Config:
    bucket_name: str
    access_key: str
    secret_key: str
    region_name: str


@dataclass
class S3InputFile:
    file_name: str
    content_type: str
    bucket: str
    key: str
    
