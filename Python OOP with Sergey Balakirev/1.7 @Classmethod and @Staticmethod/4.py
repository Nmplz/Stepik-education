class Video:
    def create(self, name):
        self.name = name

    def play(self):
        return print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        if isinstance(video, Video):
            cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        if video_indx < len(cls.videos):
            music = cls.videos[video_indx]
            return music.play()


v1 = Video()
v2 = Video()

v1.create("Python")
v2.create("Python ООП")
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)
