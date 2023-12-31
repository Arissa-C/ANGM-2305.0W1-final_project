# Color Palette Generator

## Demo
Demo Video: <https://youtu.be/jLaLgraIED0>

## GitHub Repository
GitHub Repo: <https://github.com/Arissa-C/ANGM-2305.0W1-final_project.git>

## Description
My project is a "Color Palette Generator" which is like an advanced color picker. I got the idea for the Color Palette Generator after thinking about the Adobe Color interface and how much I hated its design. In design, Adobe Color is considered a very useful tool for artists to use when coming up with a color palette for a digital art piece, but I think as an essential tool for any digital artist, it needs to have a simple interface that doesn't hide necessary properties of color like saturation, or luminosity. That's why I decided to re-design the interface to a much simpler interface that would have an interactive color wheel, interactive value field (similar to the one in Photoshop), and color palette squares that you could adjust the properties of to get the desired palette. In my design interface, you select a square from the color palette and choose a pure hue (color) from the color wheel, similar to how you'd do it in Photoshop, Illustrator, Krita, and other digital art programs, with a color selector. Then you go to the HSL value field, which is a graph containing the saturation and brightness of the color, and adjust the brightness and saturation of the color. I also added sliders if the user wanted to adjust a specific property. I additionally added two buttons that either added or removed squares from the palette depending on what palette the user had in mind.

I utilized the pygame_gui library to be able to use the sliders for luminosity and saturation without having to program the sliders using Pygame. It made my code a lot less lengthy and made it a lot easier to set up the HSL value field. Additionally, using the pygame_gui library I was able to add buttons to control the amount of squares in the palette and add labels for each feature in the program. I was going to utilize that library to create the drop-down menu for the presets for the color schemes but that didn't happen. I also utilized the math module to be able to form the circle and get the color selector to circle the circle's surface to create an interactive color wheel.

Unfortunately, I was unable to add the drop-down list of presets for color schemes into the program because I underestimated how difficult it was going to be to code this interface. I will make sure to consider that if I ever want to code another complex program. Another thing to consider for the future is to not shoot so high for an incredibly complex program. I was thinking of making this program a lot more complex than it needed to be, and I was definitely not going to finish it on time if I had tried to make it as complex as I wanted it. Additionally, I realized that the tones, tints, and shades I was going to add to the program, were going to be redundant. Tone is the addition of grey to a color to make it duller which is what saturation essentially does, while tints and shades are how much white and black you add to a color respectively. Luminosity or brightness already controls the amount of white( light) and black (darkness) you add to a color so the tint and shades were just going to be unnecessary to the program. I also didn't add CMYK (which I wasn't going to anyway) because CMYK is used for printing and painting while the RGB color mode (which my program does use) is for digital art.

I know for a fact that future design considerations would include the presets for the color schemes because there is a surprising number of artists who don't know the color schemes and struggle with color in general. I would also consider allowing for as many squares as an artist wants since color palettes can go over 5 colors it's just that it's not **recommended** to go over 5 colors for simplicity's sake. I would also consider making the interface more spaced out and have presets of Windows that change the position of the Color Wheel, HSL Field, and Color Palette depending on what the user chooses. Also adding a preset of themes and colors for the background of the interface would be a nice touch to it, and make it feel more user-friendly. 

Some future areas of improvement for me as a programmer would be reading documentation in its entirety and making sure I understand the documentation I just read. That was an obstacle that made working on this project even more difficult. Also starting on a project as soon as possible would be a good idea next time, that way I won't need to rush things. Additionally, I should consider time constraints more often and consider what is tangible for me to achieve in the given amount of time, rather than thinking I'll get everything done quickly so I'll add as much as I want. For the program itself, I'd say optimizing the program better to function smoother because there were a lot of moments where it lagged *really* badly. Also utilizing more mouse inputs would be a big step of improvement for the future because it was a struggle trying to get the few mouse inputs I implemented to work properly. If I were to get a better grasp on using them for specific surfaces, objects, and sprites I could add as many mouse inputs into the program as I want and utilize multiple selectors for the program similar to Color Adobe.

**The repository should contain all of my files for the project, which means it should have:**

**project.py (contains the code for my program, it is inside of the src folder)**

**proposal.md (contains my original project proposal)**

**requirements.txt(contains the required libraries I used for the project)**

**README.md(contains the video link, repository link, and details about the project)**
(*it's also the document your reading right now*)

A Resource that helped me for my project:
<https://www.youtube.com/watch?v=thZLa5tkzYc>

