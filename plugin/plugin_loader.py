import importlib
import pkgutil
from pymul.plugins.base import BasePlugin

def discover_plugins():
    plugins = {}

    package = "pymul.plugins"
    for _, name, _ in pkgutil.iter_modules([package.replace(".", "/")]):
        module = importlib.import_module(f"{package}.{name}")
        plugin_class = getattr(module, "Plugin", None)

        if plugin_class and issubclass(plugin_class, BasePlugin):
            plugin = plugin_class()
            plugins[plugin.name] = plugin

    return plugins