import configparser

def config_test(in_file):
    config = configparser.ConfigParser()
    config.read(in_file)
    return config

# 实例化
cfg = config_test('config.cfg')
# 获取[main]下的name值
print(cfg.get('main','name'))
# 判断section是否有file
print(cfg.has_section('file'))
# 判断section为main下的option是否有qwer
print(cfg.has_option('main','qwer'))
# 查看全部section
print(cfg.sections())