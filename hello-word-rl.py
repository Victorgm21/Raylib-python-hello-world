import pyray

# Initialization
# --------------------------------------------------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib example - basic window")
pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second

# Main game loop
while not pyray.window_should_close():
    # Update
    # ----------------------------------------------------------------------------------
    # TODO: Update your variables here
    # ----------------------------------------------------------------------------------
    # Draw
    # ----------------------------------------------------------------------------------
    pyray.begin_drawing()
    pyray.clear_background(pyray.WHITE)
    pyray.draw_text("Hello world", 325, 225, 24, pyray.MAGENTA)
    pyray.end_drawing()

# De-Initialization
# --------------------------------------------------------------------------------------
pyray.close_window()  # Close window and OpenGL context
# --------------------------------------------------------------------------------------
