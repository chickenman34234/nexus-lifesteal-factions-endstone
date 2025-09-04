from endstone.plugin import Plugin


class NexusPlugin(Plugin):
    api_version = "0.10"

    def on_enable(self):
        self.logger.info("Nexus Plugin enabled!")

    def on_disable(self):
        self.logger.info("Nexus Plugin disabled!")
