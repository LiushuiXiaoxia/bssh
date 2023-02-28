import os.path

ENV_DEVELOPMENT = 'development'
ENV_PRODUCTION = 'production'

currentEnv = ENV_PRODUCTION
if os.path.exists(os.path.join("./", '.git')):
    currentEnv = ENV_DEVELOPMENT

print(f'currentEnv = {currentEnv}')

class AppConfig(object):
    ENV = ''


def isDev():
    return currentEnv == ENV_DEVELOPMENT


def isProd():
    return not isDev()
