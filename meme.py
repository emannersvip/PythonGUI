from guizero import App, TextBox, Drawing, Combo, Slider

def draw_meme():
    meme.clear()
    meme.image(0, 0, "cat.png")
    meme.text(20, 20, top_text.value, color=color.value, size=40, font="courier")
    meme.text(20, 510, bottom_text.value, color="blue", size=size.value, font=font.value)

app = App(title="meme", width=1210, height=745)

top_text = TextBox(app, text="top text", command=draw_meme)
bottom_text = TextBox(app, text="bottom text", command=draw_meme)
color = Combo(app,
              options=["black", "white", "red", "green", "blue", "orange"],
              selected="orange",
              command=draw_meme)
font = Combo(app,
             options=["times new roman", "courier", "verdana", "impact"],
             selected="times new roman",
             command=draw_meme)
size = Slider(app, start=20, end=60, command=draw_meme)

meme = Drawing(app, width="fill", height="fill")

draw_meme()
app.display()