from Song import Song
import random

class PlayList:
    def __init__(self):
        self.songs = []
        self.playingIndex = -1

    def addSong(self, name, artist):
        self.songs.append(Song(name, artist))

    def removeSong(self, name, artist):
        index = -1

        for i in range(len(self.songs)):
            if self.songs[i].getName() == name and self.songs[i].getArtist() == artist:
                index = i

        if index == -1:
            print("Song Not Found!")
        else:
            print("Song : {} by {} has been removed!".format(self.songs[index].getName(), self.songs[index].getArtist()))
            del self.songs[index]

    def shuffleSongs(self):
        for i in range(len(self.songs)):
            r = random.randint(0, i)
            self.songs[i], self.songs[r] = self.songs[r], self.songs[i]

    def playSong(self, name, artist):
        index = -1

        for i in range(len(self.songs)):
            self.songs[i].stopSong()
            if self.songs[i].getName() == name and self.songs[i].getArtist() == artist:
                index = i

        if index == -1:
            print("Song Not Found!")
        else:
            print("Started Playing : {} by {}".format(self.songs[index].getName(), self.songs[index].getArtist()))
            self.playingIndex = index
            self.songs[index].playSong()

    def stopPlaying(self):
        self.songs[self.playingIndex].stopSong()

    def playNext(self):
        self.songs[self.playingIndex].stopSong()

        if self.playingIndex+1 < len(self.songs):
            self.playingIndex += 1
            self.songs[self.playingIndex].playSong()
        else:
            self.playingIndex = -1

    def printPlayList(self):
        for song in self.songs:
            print("{} by {}, Playing? {}".format(song.getName(), song.getArtist(), song.isPlaying()))

if __name__ == "__main__":
    playlist = PlayList()
    playlist.addSong("Song1", "Artist1")
    playlist.addSong("Song2", "Artist2")
    playlist.addSong("Song3", "Artist3")
    playlist.addSong("Song4", "Artist4")
    playlist.playSong("Song2", "Artist2")
    playlist.playSong("Song3", "Artist3")
    playlist.printPlayList()
    print("")
    playlist.playNext()
    playlist.printPlayList()
    print("")
    playlist.stopPlaying()
    playlist.printPlayList()
