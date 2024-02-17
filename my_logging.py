class Logger:
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

    def __init__(self):
        self.queue = []

    def debug(self, message):
        self.queue.append((self.DEBUG, message))

    def info(self, message):
        self.queue.append((self.INFO, message))

    def warning(self, message):
        self.queue.append((self.WARNING, message))

    def error(self, message):
        self.queue.append((self.ERROR, message))

    def critical(self, message):
        self.queue.append((self.CRITICAL, message))

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def __str__(self):
        levels = {10: "DEBUG", 20: "INFO", 30: "WARNING", 40: "ERROR", 50: "CRITICAL"}
        return "\n".join([f"{levels[level]}: {msg}" for level, msg in self.queue])


if __name__ == "__main__":
    logger = Logger()
    logger.debug("Starting up")
    logger.info("Doing something")
    logger.warning("Uh oh")
    logger.error("That's not good")
    logger.critical("System meltdown")

    print(logger)  # Prints all logged messages
