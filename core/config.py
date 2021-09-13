import os

env = os.environ.get


DEBUG = env("DEBUG", True)
PREFIX = env("PREFIX", "")
