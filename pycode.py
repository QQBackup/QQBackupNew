from app.base.ConfigManager import ConfigManager
from app.base.ProcessManager import ProcessManager


config = ConfigManager()
pm = ProcessManager(config)
# print(pm.next_feature_sets)
pm.set_feature_chain([i[0] for i in pm.next_feature_sets])
# print(pm.config)
# print(pm.next_feature_sets)
pm.set_feature_chain([i[0] for i in pm.next_feature_sets])
# print(pm.config)
# print(pm.next_feature_sets)
# while True:
#     print(pm.config)
#     conf_name, conf_value = input("conf, value: ").split()
#     pm.config.set(conf_name, conf_value)
#     print([i.validate() for i in pm.feature_chain])
pm.config.set("dumper_local_folder", "./slowtable_123456789.db")
pm.config.set("qq_number", "123456789")
pm.config.set("Stub", "stub")
print(f"{pm.feature_chain=}\n{pm.runnable=}")
pm.run()
