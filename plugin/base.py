class BasePlugin:
    name = "base"
    description = ""

    def install(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError

    def info(self):
        return {
            "name": self.name,
            "description": self.description
        }