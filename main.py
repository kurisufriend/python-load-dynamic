import os
import sys
import time
from events_def import events

sys.path.append("./scripts")

plugins = list(map(lambda n : n.split(".py")[0], filter(lambda n : n[-3:] == ".py", os.listdir("./scripts"))))
plugins_loaded = []

print(plugins)
for plugin in plugins:
    module = __import__(plugin)
    plugins_loaded.append(module)
    if events.ONCE in module.triggers:
        getattr(module, "run")(None)

for tick_count in range(1, 10):
    for plugin in plugins_loaded:
        if events.PER_TICK in plugin.triggers:
            getattr(plugin, "run")(tick_count)