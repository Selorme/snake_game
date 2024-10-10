# Snake Game

A classic Snake Game implemented in Python using the Turtle graphics library. The player controls a snake that grows in length by eating food, with the objective of achieving the highest score without colliding with the walls or itself.

## Features

- **Player Controls**: Use the arrow keys to control the direction of the snake.
- **Food Consumption**: The snake grows longer each time it consumes food, and the score increases.
- **Collision Detection**: The game detects collisions with walls and the snake's own body, resetting the score and snake length upon collision.
- **Score Tracking**: Displays the current score and resets when the game ends.

## Setup Instructions

### 1. Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/Selorme/snake_game.git
```

Navigate into the project directory:

```bash
cd snake-game
```

### 2. Install Dependencies

Make sure you have Python 3.x installed. You can check your version using:

```bash
python --version
```

This game requires the Turtle graphics library, which is included in Python's standard library. No additional installations are necessary.

### 3. Run the Game

Run the game using Python:

```bash
python main.py
```

The game window will open, allowing you to play the Snake Game.

## Code Explanation

1. **Imports**: The script imports necessary modules from the Turtle graphics library and custom classes for the snake, food, and scoreboard.
2. **Game Setup**: Initializes the game screen, sets up the background color, and creates instances of the `Snake`, `Food`, and `Score` classes.
3. **Control Mechanics**: Listens for key presses (arrow keys) to control the snake's movement.
4. **Game Loop**: Contains the main game loop that updates the screen, moves the snake, and checks for collisions:
   - **Food Collision**: If the snake's head collides with food, the food is refreshed, the snake grows, and the score updates.
   - **Wall Collision**: If the snake collides with the wall, the score resets and the snake resets.
   - **Tail Collision**: If the snake collides with itself, the score resets and the snake resets.
5. **Exit Mechanism**: Allows the user to click on the screen to exit the game.

## Classes

### `Snake`

Controls the snake's movement, growth, and resets.

### `Food`

Handles the creation and refreshing of food on the screen.

### `Score`

Tracks the player's current score, updates it, and resets it when necessary.

## License

This project is licensed under the MIT License.