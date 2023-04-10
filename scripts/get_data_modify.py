import qlib
# region in [REG_CN, REG_US]
from qlib.constant import REG_CN


provider_uri = "../qlib_data/cn_data"  # target_dir
qlib.init(provider_uri=provider_uri, region=REG_CN)

# 下载数据
from qlib.tests.data import GetData
aa = GetData()
aa.qlib_data(target_dir = provider_uri, region="cn")
