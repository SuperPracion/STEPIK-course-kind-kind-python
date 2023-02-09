class MediaPlayer:
    def open(self, file):
        self.filename = file
        self.play()

    def play(self):
        print(f'Воспроизведение {self.filename}')


media1 = MediaPlayer()
media1.open('filemedia1')

media2 = MediaPlayer()
media2.open('filemedia2')