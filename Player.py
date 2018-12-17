import wx
import wx.media

class Player(wx.Frame):
    def __init__(self, parent, title, file_path):
        wx.Frame.__init__(self, parent, title=title, size=(200, 200))
        self.file_path = file_path
        self.current_volume = 10

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.init_buttons(sizer, panel)

        self.media_player = wx.media.MediaCtrl(panel, style=wx.SIMPLE_BORDER)
        self.media_player.SetVolume(self.current_volume)
        self.load_song()
        sizer.Add(self.media_player)

        panel.SetSizer(sizer)
        self.Show()

    def init_buttons(self, sizer, panel):
        button_play = wx.Button(panel)
        button_play.SetLabel("Play/Pause")
        button_play.Bind(wx.EVT_BUTTON, self.play_or_pause)

        button_stop = wx.Button(panel)
        button_stop.SetLabel("Stop")
        button_stop.Bind(wx.EVT_BUTTON, self.stop)

        volume_text = wx.StaticText(panel, label = 'Volume',style = wx.ALIGN_CENTER)


        volume = wx.Slider(panel, value=self.current_volume, minValue=0, maxValue=100,
                        style=wx.SL_HORIZONTAL)
        volume.Bind(wx.EVT_SLIDER, self.change_volume)

        sizer.AddMany([(button_play, 0), (button_stop, 0), (volume_text, 0), (volume, 0, wx.EXPAND)])

    def change_volume(self, e):
        obj = e.GetEventObject()
        self.current_volume = obj.GetValue() / 100
        self.media_player.SetVolume(self.current_volume)

    def stop(self, e):
        state = self.media_player.GetState()
        if state == wx.media.MEDIASTATE_PLAYING:
            self.media_player.Stop()

    def play_or_pause(self, e):
        state = self.media_player.GetState()
        if state == wx.media.MEDIASTATE_STOPPED or state == wx.media.MEDIASTATE_PAUSED:
            self.media_player.Play()
        elif state == wx.media.MEDIASTATE_PLAYING:
            self.media_player.Pause()

    def load_song(self):
        self.media_player.Load(self.file_path)


def main():
    app = wx.App()
    p = Player(None, "player", r"C:\Users\Lyuda\PycharmProjects\Mp3Parser\30_Seconds_To_Mars-This_Is_War.mp3")
    app.MainLoop()

if __name__ == '__main__':
    main()
