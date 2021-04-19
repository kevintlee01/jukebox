class Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.playCount = 0
        self.started = False

    def getName(self):
        return self.name

    def getArtist(self):
        return self.artist

    def incrementPlayCount(self):
        self.playCount += 1

    def resetPlayCount(self):
        self.playCount = 0

    def getPlayCount(self):
        return self.playCount

    def isPlaying(self):
        return self.started

    def playSong(self):
        self.started = True

    def stopSong(self):
        self.started = False
