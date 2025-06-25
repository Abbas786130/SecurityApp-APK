from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import numpy as np
import tensorflow as tf

MODEL_PATH = "model.tflite"

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.camera_url = "http://192.168.0.100:8080/video"  # Replace with your stream
        self.capture = None

        self.image = Image()
        self.btn_start = Button(text="Start Detection")
        self.btn_stop  = Button(text="Stop Detection")

        self.add_widget(self.image)
        self.add_widget(self.btn_start)
        self.add_widget(self.btn_stop)

        self.btn_start.bind(on_press=self.start_detection)
        self.btn_stop.bind(on_press=self.stop_detection)

        try:
            self.interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
            self.interpreter.allocate_tensors()
            self.input_details  = self.interpreter.get_input_details()
            self.output_details = self.interpreter.get_output_details()
        except Exception as e:
            self.add_widget(Label(text="Model load failed:\n" + str(e)))

    def start_detection(self, instance):
        self.capture = cv2.VideoCapture(self.camera_url)
        Clock.schedule_interval(self.update, 1/15)

    def stop_detection(self, instance):
        if self.capture:
            self.capture.release()
            self.capture = None

    def detect_person(self, frame):
        inp = cv2.resize(frame, 
                         (self.input_details[0]['shape'][2],
                          self.input_details[0]['shape'][1]))
        inp = np.expand_dims(inp, axis=0).astype(np.uint8)
        self.interpreter.set_tensor(self.input_details[0]['index'], inp)
        self.interpreter.invoke()
        boxes   = self.interpreter.get_tensor(self.output_details[0]['index'])
        classes = self.interpreter.get_tensor(self.output_details[1]['index'])
        scores  = self.interpreter.get_tensor(self.output_details[2]['index'])
        h, w, _ = frame.shape

        for box, cls, score in zip(boxes[0], classes[0], scores[0]):
            if score > 0.5 and int(cls) == 0:
                y1, x1, y2, x2 = box
                return True, (
                  int(x1*w), int(y1*h),
                  int((x2-x1)*w), int((y2-y1)*h)
                )
        return False, None

    def update(self, dt):
        if not self.capture: return
        ret, frame = self.capture.read()
        if not ret: return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        detected, bbox = self.detect_person(frame_rgb)
        if bbox:
            x,y,ww,hh = bbox
            cv2.rectangle(frame, (x,y), (x+ww,y+hh), (0,255,0), 2)

        buf = cv2.flip(frame, 0).tobytes()
        tex = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        tex.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = tex

class SecurityApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    SecurityApp().run()
