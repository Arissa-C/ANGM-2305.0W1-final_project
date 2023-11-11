# Color Palette Generator

## Repository
[GitHub Repository](https://github.com/Arissa-C/ANGM-2305.0W1-final_project.git)

## Description
This program will open up an interactive screensaver that allows the user to pick out a series of colors for a color palette using a color picker on an accurate color wheel combined with interactive sliders to specify the needed shade, tone, tint, saturation, and luminance. From what I found the websites that are used to generate color palettes don't have the best user interface that is accessible to a wide range of digital artists and don't have a lot of ways for artists to customize the color palette directly, so I think it would be beneficial to have a customizable color palette generator that has a simple interface to use.

## Features
- **Feature 1**: An interactive color wheel 
- Use the draw circle tool for the color wheel (and specify the y value to make the circle divided up into sections for each color) and use mouse input/follow mouse functions in Pygame to allow for an interactive color wheel with a selector cursor or point (***The selectors should have labels that state which square is affected by a change in color***)
- **Feature 2**: An interactive value square that determines tint, tone, shade, saturation, and luminance if the user chooses one of the aforementioned options to adjust
- Use the draw square tool for the value square, and mouse input/follow cursor functions. For the options use mouse inputs and buttons to interact to change the layout of the value square depending on which option was chosen 
- **Feature 3**: Buttons that give the artist the option to select a color scheme (***Analogous, Complementary, Triatic, Tetratic, etc.***) to go off of when selecting colors on the color wheel
- Mouse input (Use mouse inputs) over a drawn rectangle (button) that once clicked should give multiple selection points on the color wheel based on the type of color scheme. The user should have the ability to move the selection points around by using a Mouse Cursor function.
- **Feature 4**: Displays a strip of the customized color palette, with each square color determined by the selections made on the color wheel or value square.
-  Multiple Draw rectangle functions, use a color function and a user input function to change the color.

## Challenges
- Learn more about the interactive features of the Pygame library such as mouse input, and follow cursor input.
- Learn how to change an aspect of the screen saver using mouse input, specifically the function of it and color (this is for the value square).
- ***Make sure the color wheel is accurate based on categories such as Primary, Secondary, Tertiary, Warm, Cool, and Complementary colors***

## Outcomes

**Ideal Outcome**:
- For the program build a visually pleasing color palette from the color wheel, value square, and color schemes (***if applied***). The color wheel is correctly formatted to display multiple colors in the correct order by warm to cold colors and complementary colors are directly across from one another. The value square changes the color variant it displays based on the selected option (tint, shade, etc.) and displays the correct variants of color based on the chosen option. Both will affect a specific square in the color palette strip displayed at the bottom of the screensaver.

**Minimal Viable Outcome**:
- The minimal viable outcome would be that the program allows the user to pick a color for a specific square in the palette build a palette out of hues and add shade, tint, and tones. This would unfortunately mean that there are no buttons for the color schemes or color categories, but it would still be a working color palette generator.

## Milestones

- **Week 1**
  1. Design the layout of the screen saver and start planning out my code (Do this weekend)
  2. Start developing the main function which contains the display size, color of the window, event loop function, etc.
  3. Implement the class function for the color wheel and add an event loop for the color wheel

- **Week 2**
  1. Implement value square with specifications for Tones, Tints, Shades, Saturation, or Luminance
  2. Add event loop for value square
  3. Add a Palette strip below the color wheel and value square

- **Week N (Final)**
  1. Add options for color schemes and color categories for color picker on the color wheel
  2. Optimize the program to have a better performance
  3. Showcase final program
